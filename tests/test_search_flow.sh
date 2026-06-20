#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/scripts" "$TMP/ingest" "$TMP/docs/06-x/sources"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/junk.py" \
   "$ROOT/scripts/search_flow.sh" "$TMP/scripts/"

# Fake search: ignores args, prints two results (one good, one junk).
cat > "$TMP/scripts/fake_search.py" <<'PY'
import json
print(json.dumps([{"url": "http://x/good", "title": "Good Source"},
                  {"url": "http://x/junk", "title": "Junk Source"}]))
PY
# Fake fetch: clean markdown for /good, a JS-shell page for /junk.
cat > "$TMP/scripts/fake_fetch.py" <<'PY'
import sys
url = sys.argv[1]
if url.endswith("/good"):
    print("# Good Source\n\n" + ("real content " * 60))
else:
    print("Just a moment...")
PY

# Seed a queued gap.
REPO_ROOT="$TMP" python3 "$TMP/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "hybrid retrieval" >/dev/null

PY=python3 SEARCH="$TMP/scripts/fake_search.py" FETCH="$TMP/scripts/fake_fetch.py" REPO_ROOT="$TMP" \
  bash "$TMP/scripts/search_flow.sh" --topic 06-x || { echo "MISS: search_flow exited nonzero"; exit 1; }

fail=0
# Exactly one good source dropped into ingest/ (junk excluded).
n=$(find "$TMP/ingest" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
[ "$n" = "1" ] && echo "ok: one non-junk source in ingest/" || { echo "MISS: ingest .md count=$n"; fail=1; }
# Gap marked done; budget spent by 1.
python3 - "$TMP" <<'PY' || fail=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
assert st["gaps"][0]["status"] == "done", st["gaps"][0]
assert st["budget"]["spent"]["sources"] == 1, st["budget"]["spent"]
print("ok: gap done, budget spent=1")
PY
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
