#!/usr/bin/env bash
# Drain one topic's gap queue within the source budget: search, fetch,
# junk-filter, drop good markdown into ingest/ for the ingest flow to record.
# Usage: search_flow.sh --topic <topic>
set -uo pipefail   # NOT -e: one bad gap/result must not abort the cycle.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"
PY="${PY:-$HOME/.venvs/crawl4ai/bin/python}"
SEARCH="${SEARCH:-$HOME/.venvs/crawl4ai/search.py}"
FETCH="${FETCH:-$HOME/.venvs/crawl4ai/fetch_md.py}"
PER_GAP="${PER_GAP:-5}"
SP="python3 $HERE/state.py"

topic=""
[ "${1:-}" = "--topic" ] && topic="${2:-}"
[ -n "$topic" ] || { echo "usage: search_flow.sh --topic <topic>" >&2; exit 2; }
mkdir -p "$ROOT/ingest"

remaining="$($SP budget-remaining --root "$ROOT")"
[ "$remaining" -gt 0 ] || { echo "search: budget spent ($remaining remaining)"; exit 0; }

while [ "$remaining" -gt 0 ]; do
  line="$($SP next-gap --root "$ROOT" --topic "$topic")"
  [ -n "$line" ] || { echo "search: no queued gaps for $topic"; break; }
  gid="$(printf '%s' "$line" | cut -f1)"
  desc="$(printf '%s' "$line" | cut -f3)"
  n="$PER_GAP"; [ "$remaining" -lt "$n" ] && n="$remaining"

  results="$("$PY" "$SEARCH" "$desc" "$n" 2>/dev/null)" || results="[]"
  urls="$(printf '%s' "$results" | jq -r '.[].url' 2>/dev/null)"
  kept=0; i=0
  while IFS= read -r url; do
    [ -n "$url" ] || continue
    [ "$remaining" -gt 0 ] || break
    i=$((i+1))
    tmp="$(mktemp)"
    "$PY" "$FETCH" "$url" > "$tmp" 2>/dev/null || { rm -f "$tmp"; continue; }
    if python3 "$HERE/junk.py" check "$tmp"; then
      slug="$(slugify "$desc")"
      mv "$tmp" "$ROOT/ingest/${gid}-${slug}-${i}.md"
      kept=$((kept+1)); remaining=$((remaining-1))
    else
      rm -f "$tmp"
    fi
  done <<< "$urls"

  if [ "$kept" -gt 0 ]; then
    $SP set-gap --root "$ROOT" --id "$gid" --status done >/dev/null
    $SP budget-spend --root "$ROOT" --sources "$kept" >/dev/null
    echo "search: gap $gid -> $kept source(s) into ingest/"
  else
    $SP set-gap --root "$ROOT" --id "$gid" --status requeue --requeue >/dev/null
    # Fail permanently after 3 attempts. Default -1 if the gap vanished, so the
    # comparison never errors and a missing gap is simply not failed.
    att="$(python3 -c "import json,sys;print(next((g['attempts'] for g in json.load(open(sys.argv[1]+'/.research/state.json'))['gaps'] if g['id']==sys.argv[2]), -1))" "$ROOT" "$gid")"
    [ "$att" -ge 3 ] && $SP set-gap --root "$ROOT" --id "$gid" --status failed >/dev/null
    echo "search: gap $gid produced no non-junk sources (attempt $att)"
  fi
done
echo "Done. New sources (if any) await the ingest cycle."
