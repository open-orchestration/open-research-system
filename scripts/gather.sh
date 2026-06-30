#!/usr/bin/env bash
# Gather sources for a topic via crawl4ai (search + fetch), off the harness web path.
# Usage: gather.sh <topic> "<query>"
# Env: DRY_RUN=1 prints commands instead of running. N=<int> results (default 8).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"

topic="${1:-}"; query="${2:-}"
[ -n "$topic" ] || { echo "usage: gather.sh <topic> <query>" >&2; exit 2; }
dir="$(resolve_topic_dir "$ROOT" "$topic")" || exit 1
[ -n "$query" ] || { echo "missing query" >&2; exit 2; }

N="${N:-8}"
PY="$(ors_venv)/bin/python"
SEARCH="$HERE/crawl4ai/search.py"
FETCH="$HERE/crawl4ai/fetch_md.py"
out="$dir/sources"; mkdir -p "$out"
search_cmd="$PY $SEARCH \"$query\" $N"

if [ "${DRY_RUN:-}" = "1" ]; then
  echo "would run: $search_cmd"
  echo "would fetch each result via: $PY $HERE/_fetch_results.py <search.json> $out $FETCH"
  exit 0
fi

echo "searching: $query"
results_file="$out/_search_$(slugify "$query").json"
"$PY" "$SEARCH" "$query" "$N" > "$results_file"
# Fetch each URL to markdown via the helper file (no stdin/heredoc collision).
# Large output stays on disk — index with context-mode, do not raw-read.
"$PY" "$HERE/_fetch_results.py" "$results_file" "$out" "$FETCH"
echo "Gathered into $out. Index with context-mode; synthesize into ${DOCS_BASE:-.research/docs}/findings/."
