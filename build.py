#!/usr/bin/env python3
"""Static site builder for nanvel.name blog.

Usage:
    uv run python build.py
"""

import re
import shutil
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

BLOG_ROOT = Path(__file__).parent
OUT = BLOG_ROOT / "_site"
TEMPLATES_DIR = BLOG_ROOT / "templates"
DOMAIN = "blog.nanvel.com"

SKIP_DIRS = {".git", "templates", "_site", ".github", ".idea", "__pycache__"}
SKIP_SUFFIXES = {".py", ".toml", ".txt", ".cfg", ".ini"}
# Asset extensions copied alongside pages
ASSET_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp4", ".zip", ".ico"}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Page:
    path: Path
    uri: str          # e.g. "2025/03/gold-ledger"
    title: str
    tags: list[str]
    created: datetime
    modified: datetime
    html: str
    place: str = ""
    comments: bool = False
    description: str = ""
    image: str = ""


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _parse_dt(value) -> datetime:
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day)
    s = str(value)
    for fmt in ("%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return datetime(2000, 1, 1)


def _resolve_obsidian_links(text: str) -> str:
    """Convert [[path|display]] and [[path]] to root-absolute markdown links."""
    def replace(m: re.Match) -> str:
        inner = m.group(1)
        if "|" in inner:
            path, display = inner.split("|", 1)
        else:
            path = display = inner
        return f"[{display}](/{path}/)"
    return re.sub(r"\[\[([^\]]+)\]\]", replace, text)


def _absolutize_assets(text: str, dir_uri: str) -> str:
    """Rewrite relative asset references to absolute paths.

    Pages are served from /<uri>/ but assets live at /<dir_uri>/<file>,
    so relative references in markdown would resolve incorrectly.
    """
    base = f"/{dir_uri}"

    # Markdown images: ![alt](relative)
    def fix_img(m: re.Match) -> str:
        alt, path = m.group(1), m.group(2)
        if re.match(r"https?://|/|#", path):
            return m.group(0)
        return f"![{alt}]({base}/{path})"
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", fix_img, text)

    # Markdown links to local assets: [text](file.pdf)
    def fix_asset_link(m: re.Match) -> str:
        link_text, path = m.group(1), m.group(2)
        if re.match(r"https?://|/|#|\[", path):
            return m.group(0)
        if Path(path).suffix.lower() in ASSET_SUFFIXES:
            return f"[{link_text}]({base}/{path})"
        return m.group(0)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", fix_asset_link, text)

    # HTML attributes: data="file" and src="file" (object/embed tags)
    def fix_html_attr(m: re.Match) -> str:
        attr, path = m.group(1), m.group(2)
        if re.match(r"https?://|/|#", path):
            return m.group(0)
        return f'{attr}="{base}/{path}"'
    text = re.sub(r'\b(data|src)="([^"]*\.[a-zA-Z0-9]+)"', fix_html_attr, text)

    return text


_MD = markdown.Markdown(
    extensions=["toc", "fenced_code", "tables", "attr_list"],
    extension_configs={"toc": {"anchorlink": True}},
)


def parse_page(path: Path) -> Page | None:
    content = path.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return None

    try:
        end = content.index("\n---", 3)
    except ValueError:
        return None

    fm = yaml.safe_load(content[3:end]) or {}
    body = content[end + 4:].lstrip("\n")

    tags_raw = fm.get("tags", [])
    if isinstance(tags_raw, str):
        tags = [t.strip() for t in tags_raw.split(",")]
    else:
        tags = [str(t).strip() for t in tags_raw]

    # URI = path relative to blog root, without extension
    uri = str(path.relative_to(BLOG_ROOT).with_suffix(""))
    # source dir relative to blog root (for asset absolutizing)
    dir_uri = str(path.parent.relative_to(BLOG_ROOT))

    body = _resolve_obsidian_links(body)
    body = _absolutize_assets(body, dir_uri)

    _MD.reset()
    html = _MD.convert(body)

    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_m.group(1)) if title_m else path.stem

    created_raw = fm.get("created", "2000-01-01")
    modified_raw = fm.get("modified", created_raw)

    return Page(
        path=path,
        uri=uri,
        title=title.strip(),
        tags=tags,
        created=_parse_dt(created_raw),
        modified=_parse_dt(modified_raw),
        html=html,
        place=fm.get("place", ""),
        comments=str(fm.get("comments", "false")).lower() == "true",
        description=str(fm.get("description", "")),
        image=str(fm.get("image", "")),
    )


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------

def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    # --- Parse all pages -------------------------------------------------
    all_pages: list[Page] = []
    for path in sorted(BLOG_ROOT.rglob("*.md")):
        if any(d in SKIP_DIRS for d in path.parts):
            continue
        page = parse_page(path)
        if page:
            all_pages.append(page)

    all_pages.sort(key=lambda p: p.created, reverse=True)

    all_tags = sorted({tag for page in all_pages for tag in page.tags})

    # --- Copy source assets to _site (mirror directory structure) --------
    for path in BLOG_ROOT.rglob("*"):
        if any(d in SKIP_DIRS for d in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix in SKIP_SUFFIXES or path.suffix == ".md":
            continue
        dest = OUT / path.relative_to(BLOG_ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)

    # Copy static template assets
    shutil.copy2(TEMPLATES_DIR / "style.css", OUT / "style.css")
    shutil.copy2(TEMPLATES_DIR / "favicon.ico", OUT / "favicon.ico")

    # --- Jinja2 environment ----------------------------------------------
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)
    year = datetime.now().year
    base_ctx = {"all_tags": all_tags, "year": year}

    page_tmpl = env.get_template("page.html")
    index_tmpl = env.get_template("index.html")
    tag_tmpl = env.get_template("tag.html")
    sitemap_tmpl = env.get_template("sitemap.xml")

    # --- Render individual pages -----------------------------------------
    for page in all_pages:
        out_dir = OUT / page.uri
        out_dir.mkdir(parents=True, exist_ok=True)
        html = page_tmpl.render(**base_ctx, page=page, current_tag=None)
        (out_dir / "index.html").write_text(html, encoding="utf-8")

    # --- Index (blog-tagged pages only) ----------------------------------
    blog_pages = [p for p in all_pages if "blog" in p.tags]
    html = index_tmpl.render(**base_ctx, pages=blog_pages, current_tag=None)
    (OUT / "index.html").write_text(html, encoding="utf-8")

    # --- Tag pages -------------------------------------------------------
    (OUT / "tags").mkdir(exist_ok=True)
    for tag in all_tags:
        tag_pages = [p for p in all_pages if tag in p.tags]
        out_dir = OUT / "tags" / tag
        out_dir.mkdir(exist_ok=True)
        html = tag_tmpl.render(**base_ctx, pages=tag_pages, current_tag=tag)
        (out_dir / "index.html").write_text(html, encoding="utf-8")

    # --- Sitemap ---------------------------------------------------------
    xml = sitemap_tmpl.render(pages=all_pages)
    (OUT / "sitemap.xml").write_text(xml, encoding="utf-8")

    # --- 404 -------------------------------------------------------------
    (OUT / "404.html").write_text(
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<title>404 Not Found</title>'
        '<link rel="stylesheet" href="/style.css"/></head>'
        '<body><h1>404 Not Found</h1><p><a href="/">Home</a></p></body></html>',
        encoding="utf-8",
    )

    # --- CNAME for custom domain -----------------------------------------
    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")

    print(f"Built {len(all_pages)} pages · {len(all_tags)} tags → _site/")


if __name__ == "__main__":
    build()
