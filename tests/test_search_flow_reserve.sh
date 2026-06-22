#!/usr/bin/env bash
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
export REPO_ROOT="$TMP"
mkdir -p "$TMP/.research" "$TMP/scripts"
# stub crawl tools: SEARCH prints 5 fake urls, FETCH prints clean prose
cat > "$TMP/fakesearch.py" <<'PY'
import json,sys
print(json.dumps([{"url":f"http://e/{i}"} for i in range(int(sys.argv[2]))]))
PY
cat > "$TMP/fakefetch.py" <<'PY'
print("This is a substantial clean research document about retrieval methods. " * 40)
PY
# seed budget=8 and two gaps for one topic
python3 "$ROOT/scripts/state.py" budget-reset --root "$TMP" >/dev/null
python3 "$ROOT/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "alpha question" >/dev/null
python3 "$ROOT/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "beta question" >/dev/null
IN="$TMP/ingest/.work/06-x"
PER_GAP=3 PY=python3 SEARCH="$TMP/fakesearch.py" FETCH="$TMP/fakefetch.py" \
  bash "$ROOT/scripts/search_flow.sh" --topic 06-x --inbox "$IN"
# assert: kept files landed in the scoped inbox, and budget spent == files kept (no overspend)
files="$(find "$IN" -name '*.md' | wc -l | tr -d ' ')"
spent="$(python3 -c "import json;print(json.load(open('$TMP/.research/state.json'))['budget']['spent']['sources'])")"
echo "files=$files spent=$spent"
[ "$files" = "$spent" ] || { echo "FAIL: spent ($spent) != files ($files)"; exit 1; }
[ "$spent" -le 8 ] || { echo "FAIL: overspent $spent"; exit 1; }
[ "$files" -ge 1 ] || { echo "FAIL: nothing landed in scoped inbox"; exit 1; }
echo "PASS search_flow reserve"
