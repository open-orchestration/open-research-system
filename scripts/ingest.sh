#!/usr/bin/env bash
# Convert every file in ingest/ to markdown via markitdown, into a topic's sources/.
# Usage: ingest.sh [topic]   (topic defaults to docs/findings staging if omitted)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"

shopt -s nullglob
files=("$ROOT"/ingest/*)
real=(); for f in "${files[@]+"${files[@]}"}"; do [ "$(basename "$f")" = ".gitkeep" ] || real+=("$f"); done
[ "${#real[@]}" -gt 0 ] || { echo "no files in ingest/" >&2; exit 1; }

if [ "${1:-}" ]; then dest="$(resolve_topic_dir "$ROOT" "$1")/sources"; else dest="$ROOT/docs/findings"; fi
mkdir -p "$dest"

for f in "${real[@]+"${real[@]}"}"; do
  base="$(basename "${f%.*}")"
  # markitdown prints markdown to stdout; redirect to the destination. stderr carries
  # a harmless pydub/ffmpeg warning we discard.
  "$MARKITDOWN" "$f" > "$dest/${base}.md" 2>/dev/null
  echo "ingested: $f -> $dest/${base}.md"
done
echo "Done. Index with context-mode before reading; do not raw-read."
