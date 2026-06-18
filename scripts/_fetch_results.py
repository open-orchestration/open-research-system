#!/usr/bin/env python
"""Fetch each search result to markdown. Usage: _fetch_results.py <search.json> <out_dir> <fetch_md.py>"""
import json, sys, subprocess, re, pathlib

search_json, out_dir, fetch = sys.argv[1], sys.argv[2], sys.argv[3]
py = sys.executable
data = json.loads(pathlib.Path(search_json).read_text())
for r in data:
    url = r.get("url")
    if not url:
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", (r.get("title") or url).lower())[:60].strip("-") or "src"
    # Distinct URLs can share a title (e.g. arxiv /abs/ + /html/); suffix on collision
    # so neither source is silently overwritten.
    dest = pathlib.Path(out_dir) / f"{slug}.md"
    n = 2
    while dest.exists():
        dest = pathlib.Path(out_dir) / f"{slug}-{n}.md"
        n += 1
    try:
        md = subprocess.run([py, fetch, url], capture_output=True, text=True, timeout=120).stdout
        dest.write_text(f"# {r.get('title','')}\n\nSource: {url}\n\n{md}")
        print(f"fetched: {url} -> {dest}")
    except (subprocess.SubprocessError, OSError) as e:
        print(f"FAIL {url} {e}", file=sys.stderr)
