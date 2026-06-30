#!/usr/bin/env bash
# search_flow extracts result URLs without jq (jq is no longer a dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
grep -q "jq " "$ROOT/scripts/search_flow.sh" && { echo "MISS: jq still referenced"; fail=1; } \
  || echo "ok: no jq in search_flow"

# Exact production python3 program from scripts/search_flow.sh (the urls= block).
PROG='import json,sys
try: data=json.load(sys.stdin)
except Exception: data=[]
for x in data:
    u=x.get("url") if isinstance(x,dict) else None
    if u: print(u)'

# valid array: two urls extracted; element without url key skipped
got="$(printf '%s' '[{"url":"https://a"},{"url":"https://b"},{"nope":1}]' \
  | python3 -c "$PROG" 2>/dev/null)"
[ "$got" = "$(printf 'https://a\nhttps://b')" ] && echo "ok: python3 url parse (valid array)" \
  || { echo "MISS: parse got '$got'"; fail=1; }

# malformed JSON: except branch sets data=[], must print nothing
got="$(printf '%s' 'not json' | python3 -c "$PROG" 2>/dev/null)"
[ -z "$got" ] && echo "ok: python3 url parse (malformed json)" \
  || { echo "MISS: malformed json got '$got'"; fail=1; }

# empty string: json.load fails, except branch, must print nothing
got="$(printf '%s' '' | python3 -c "$PROG" 2>/dev/null)"
[ -z "$got" ] && echo "ok: python3 url parse (empty string)" \
  || { echo "MISS: empty string got '$got'"; fail=1; }

# empty array: valid JSON but no elements, must print nothing
got="$(printf '%s' '[]' | python3 -c "$PROG" 2>/dev/null)"
[ -z "$got" ] && echo "ok: python3 url parse (empty array)" \
  || { echo "MISS: empty array got '$got'"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
