#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Minimal fake repo: one topic dir + ingest + scripts + lib
mkdir -p "$TMP/docs/11-x/sources" "$TMP/ingest" "$TMP/scripts"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/ingest_lib.py" \
   "$ROOT/scripts/ingest_flow.sh" "$TMP/scripts/"
printf '# Hello\n\nsome content\n' > "$TMP/ingest/notes.md"

REPO_ROOT="$TMP" bash "$TMP/scripts/ingest_flow.sh" 11-x

fail=0
# corpus file written under sources/
n=$(find "$TMP/docs/11-x/sources" -name '*.md' | wc -l | tr -d ' ')
[ "$n" = "1" ] && echo "ok: one source file" || { echo "MISS: source file count=$n"; fail=1; }
# state records exactly one corpus entry and graph dirty
python3 - "$TMP" <<'PY' || fail=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
assert len(st["corpus"]) == 1, st["corpus"]
assert st["graph"]["dirty"] is True
assert st["corpus"][0]["lifecycle"] == "active"
print("ok: state has one active corpus entry, graph dirty")
PY
# native moved out of ingest/
[ -f "$TMP/ingest/_done/notes.md" ] && echo "ok: native archived" || { echo "MISS: native not archived"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
