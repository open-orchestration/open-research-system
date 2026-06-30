#!/usr/bin/env bash
# No engine script hardcodes the author's personal dep paths; helpers resolve to the bundle.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

# Consumer hardcode check — excludes the single documented fallback inside ors_venv's
# for-loop (identified by the trailing '"; do' that closes the for-item list).
if grep -nE '\$HOME/\.venvs/crawl4ai|\$HOME/\.local/bin/markitdown' \
     "$ROOT/scripts/lib.sh" "$ROOT/scripts/gather.sh" "$ROOT/scripts/search_flow.sh" \
   | grep -v '"$HOME/\.venvs/crawl4ai"; do'; then
  echo "MISS: hardcoded personal dep path remains"; fail=1
else echo "ok: no hardcoded personal paths"; fi

# Helpers referenced from the bundle.
grep -q 'LIB_DIR/crawl4ai/fetch_md.py' "$ROOT/scripts/lib.sh" \
  && echo "ok: lib.sh uses bundled fetch_md" || { echo "MISS: lib.sh fetch_md"; fail=1; }
grep -qE 'crawl4ai/search\.py' "$ROOT/scripts/gather.sh" "$ROOT/scripts/search_flow.sh" \
  && echo "ok: flows use bundled search.py" || { echo "MISS: flows search.py"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
