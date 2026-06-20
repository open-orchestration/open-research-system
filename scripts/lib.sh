#!/usr/bin/env bash
# Shared helpers for spike scripts.

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

# Resolve a topic arg (slug or NN prefix) to its docs dir; echo path or exit 1.
resolve_topic_dir() {
  local root="$1" arg="$2" match
  match=$(find "$root/docs" -maxdepth 1 -type d -name "*${arg}*" | grep -E '/[0-9]{2}-[^/]+$' | head -1)
  [ -n "$match" ] || { echo "no topic dir matches '$arg'" >&2; return 1; }
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
