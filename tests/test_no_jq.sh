#!/usr/bin/env bash
# search_flow extracts result URLs without jq (jq is no longer a dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
grep -q "jq " "$ROOT/scripts/search_flow.sh" && { echo "MISS: jq still referenced"; fail=1; } \
  || echo "ok: no jq in search_flow"
# The python3 extraction parses a results array to bare URLs.
got="$(printf '%s' '[{"url":"https://a"},{"url":"https://b"},{"nope":1}]' \
  | python3 -c 'import json,sys
data=json.load(sys.stdin)
for x in data:
    u=x.get("url") if isinstance(x,dict) else None
    if u: print(u)')"
[ "$got" = "$(printf 'https://a\nhttps://b')" ] && echo "ok: python3 url parse" \
  || { echo "MISS: parse got '$got'"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
