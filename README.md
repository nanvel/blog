# Blog

Source for [blog.nanvel.com](https://blog.nanvel.com).

## Local preview

```bash
uv run python scripts/build.py && python -m http.server 8000 --directory _site
```

Open `http://localhost:8000`.

## Preprocessing

One-time script to migrate frontmatter and links to Obsidian format:

```bash
python scripts/preprocess.py          # dry-run
python scripts/preprocess.py --apply  # write changes
```

## Deploy

Push to `master` — GitHub Actions builds and deploys automatically.
