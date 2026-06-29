#!/usr/bin/env bash
# Shared helpers for spike scripts.

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

# Resolve a topic arg to its docs dir, creating docs/NN-<slug> on miss.
# The arg is slugified first, so free-text topic names ("columnar storage")
# match slug dirs ("01-columnar-storage"). Autonomous flow: topics are
# discovered at runtime, so a missing dir is created, not an error.
# ponytail: next-NN under concurrent ingest can dup a prefix (distinct slugs
# stay distinct dirs); per-topic locking only if numbering must be gapless.
resolve_topic_dir() {
  local root="$1" slug match next base
  base="${DOCS_BASE:-.research/docs}"
  slug="$(slugify "$2")"
  match=$(find "$root/$base" -maxdepth 1 -type d -name "*${slug}*" 2>/dev/null \
            | grep -E '/[0-9]{2}-[^/]+$' | head -1)
  if [ -z "$match" ]; then
    next=$(find "$root/$base" -maxdepth 1 -type d 2>/dev/null \
             | grep -oE '/[0-9]{2}-' | tr -dc '0-9\n' | sort -n | tail -1)
    next=$(printf '%02d' $(( 10#${next:-0} + 1 )))
    match="$root/$base/${next}-${slug}"
    mkdir -p "$match" || { echo "could not create topic dir '$match'" >&2; return 1; }
  fi
  echo "$match"
}

MARKITDOWN="${MARKITDOWN:-$HOME/.local/bin/markitdown}"

# Fetch a URL to markdown via crawl4ai; prints markdown to stdout.
fetch_link() {
  local url="$1" py="$HOME/.venvs/crawl4ai/bin/python" f="$HOME/.venvs/crawl4ai/fetch_md.py"
  "$py" "$f" "$url" 2>/dev/null
}

# Transcribe a YouTube/video URL to text via youtube-transcript-api; prints to stdout.
transcribe_video() {
  local url="$1" py="$HOME/.venvs/crawl4ai/bin/python"
  "$py" - "$url" <<'PY' 2>/dev/null
import sys, re
url = sys.argv[1]
m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
if not m:
    sys.exit(1)
from youtube_transcript_api import YouTubeTranscriptApi as A
try:
    data = A().fetch(m.group(1)); segs = [s.text for s in data]
except Exception:
    data = A.get_transcript(m.group(1)); segs = [s["text"] for s in data]
print("# " + url + "\n\n" + " ".join(segs))
PY
}
