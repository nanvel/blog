#!/usr/bin/env python3
"""
Preprocess blog markdown files:
  1. Convert frontmatter from custom format to Obsidian YAML (labels -> tags)
  2. Convert /path and https://blog.nanvel.com/path links to Obsidian [[path|text]]

Usage:
  python preprocess.py           # dry-run: print changed files + diffs
  python preprocess.py --apply   # write changes to disk
"""

import re
import sys
from pathlib import Path

BLOG_ROOT = Path(__file__).parent.parent
NANVEL_RE = re.compile(r"^https?://nanvel\.name")

# Keys preserved in output order; everything else appended after
FIELD_ORDER = ["created", "modified", "place", "comments", "visible", "description", "keywords"]

# Labels that the generic CamelCase→kebab algorithm gets wrong
_TAG_OVERRIDES: dict[str, str] = {
    "i-os": "ios",          # iOS → i-os without override
    "type-script": "typescript",  # TypeScript → type-script without override
}


def slugify_tag(label: str) -> str:
    """Convert a label to a lowercase kebab-case tag slug."""
    # Insert hyphen between lowercase→uppercase transition
    s = re.sub(r"([a-z])([A-Z])", r"\1-\2", label)
    # Insert hyphen between acronym run and the next TitleWord (e.g. DynamoDB→Dynamo-DB)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", s)
    slug = s.lower()
    return _TAG_OVERRIDES.get(slug, slug)


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple[dict[str, str | list[str]], str]:
    """
    Parse the custom header format (no --- fences, labels may span multiple
    indented lines) and return (meta_dict, body_text).

    Returns ({}, content) when no recognizable frontmatter is found.
    """
    lines = content.splitlines(keepends=True)
    meta: dict[str, str | list[str]] = {}
    i = 0
    current_key: str | None = None
    current_values: list[str] = []

    def flush():
        if current_key is None:
            return
        if current_key == "labels":
            meta[current_key] = current_values[:]
        else:
            meta[current_key] = current_values[0] if current_values else ""

    while i < len(lines):
        line = lines[i].rstrip("\n").rstrip("\r")

        # Blank line → end of frontmatter
        if not line.strip():
            flush()
            i += 1
            break

        # key: value line
        m = re.match(r"^([a-z]+): (.*)$", line)
        if m:
            flush()
            current_key = m.group(1)
            current_values = [m.group(2).strip()]
            i += 1
            continue

        # 8-space or tab-indented continuation (only meaningful for labels)
        if (line.startswith("        ") or line.startswith("\t")) and current_key == "labels":
            val = line.strip()
            if val:
                current_values.append(val)
            i += 1
            continue

        # Not a frontmatter line — bail out (file starts with content, e.g. #)
        flush()
        break

    # flush in case file ended without blank line
    flush()

    if not meta:
        return {}, content

    body = "".join(lines[i:])
    return meta, body


def format_frontmatter(meta: dict[str, str | list[str]]) -> str:
    """Render meta dict as Obsidian YAML frontmatter block."""
    lines = ["---"]

    # tags (from labels)
    if "labels" in meta:
        tags = meta["labels"]
        tags_list = tags if isinstance(tags, list) else [tags]
        slugs = [slugify_tag(t) for t in tags_list]
        lines.append(f"tags: [{', '.join(slugs)}]")

    for key in FIELD_ORDER:
        if key in meta:
            lines.append(f"{key}: {meta[key]}")

    # anything not already handled
    handled = {"labels"} | set(FIELD_ORDER)
    for key, val in meta.items():
        if key not in handled:
            lines.append(f"{key}: {val}")

    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Link conversion
# ---------------------------------------------------------------------------

# Matches [text](url) where url is a /single-slash path or https://nanvel.name
# Excludes protocol-relative URLs like //external.com
_LINK_RE = re.compile(
    r"\[([^\]]+)\]\(((?:/[^/]|https?://nanvel\.name)[^)]*)\)"
)

# Code fence detector – we skip substitutions inside ``` blocks
_FENCE_RE = re.compile(r"^```", re.MULTILINE)


def convert_links(body: str) -> str:
    """Replace internal markdown links with Obsidian [[path|text]] links."""

    # Split on code fences. re.split consumes the ``` separator, so we must
    # restore it before every part after the first (both opening and closing fences).
    # parts[0], parts[2], parts[4] … are outside fences → process for links
    # parts[1], parts[3], parts[5] … are inside fences  → leave untouched
    parts = _FENCE_RE.split(body)
    result = []
    for idx, part in enumerate(parts):
        if idx > 0:
            result.append("```")  # restore the consumed fence marker
        if idx % 2 == 1:
            result.append(part)   # inside code block — leave as-is
        else:
            result.append(_LINK_RE.sub(_replace_link, part))

    return "".join(result)


def _replace_link(m: re.Match) -> str:
    text = m.group(1)
    url = m.group(2)

    # Strip the nanvel.name host prefix
    url = NANVEL_RE.sub("", url)
    # Strip leading slash to get a relative path
    path = url.lstrip("/")

    if text == path:
        return f"[[{path}]]"
    return f"[[{path}|{text}]]"


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------

def already_converted(content: str) -> bool:
    """True if the file already has Obsidian YAML frontmatter."""
    return content.startswith("---\n") or content.startswith("---\r\n")


def process_file(path: Path) -> str | None:
    """
    Return the new file content if changes are needed, else None.
    """
    original = path.read_text(encoding="utf-8")

    if already_converted(original):
        return None

    meta, body = parse_frontmatter(original)

    if meta:
        new_fm = format_frontmatter(meta)
        new_body = convert_links(body)
        new_content = new_fm + "\n\n" + new_body.lstrip("\n")
    else:
        # No frontmatter — just convert links in the whole file
        new_content = convert_links(original)

    if new_content == original:
        return None
    return new_content


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    apply = "--apply" in sys.argv

    md_files = sorted(
        p for p in BLOG_ROOT.rglob("*.md")
        if ".git" not in p.parts and ".idea" not in p.parts
    )

    changed = 0
    for path in md_files:
        new_content = process_file(path)
        if new_content is None:
            continue

        rel = path.relative_to(BLOG_ROOT)
        changed += 1

        if apply:
            path.write_text(new_content, encoding="utf-8")
            print(f"  updated  {rel}")
        else:
            print(f"\n{'='*60}")
            print(f"  {rel}")
            print(f"{'='*60}")
            # Show first 30 lines of new content as preview
            preview_lines = new_content.splitlines()[:30]
            print("\n".join(preview_lines))
            if len(new_content.splitlines()) > 30:
                print("  ...")

    print(f"\n{'applied' if apply else 'would change'} {changed}/{len(md_files)} files")
    if not apply and changed:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
