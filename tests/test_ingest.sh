#!/usr/bin/env bash
# Plain-bash test harness for ingest.sh (no bats dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
pass=0; fail=0
ok(){ echo "ok: $1"; pass=$((pass+1)); }
no(){ echo "FAIL: $1"; fail=$((fail+1)); }

# Case 1: errors with no files in ingest/
TMP="$(mktemp -d)"; mkdir -p "$TMP/ingest" "$TMP/.research/docs/06-rag-retrieval/sources"
touch "$TMP/ingest/.gitkeep"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/ingest.sh" 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"no files"* ]]; } && ok "errors with empty ingest" || no "should error on empty ingest (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 2: converts a file into the target topic's sources/
TMP="$(mktemp -d)"; mkdir -p "$TMP/ingest" "$TMP/.research/docs/06-rag-retrieval/sources"
printf 'hello world' > "$TMP/ingest/note.md"
out="$(env REPO_ROOT="$TMP" MARKITDOWN="cat" bash "$ROOT/scripts/ingest.sh" 06-rag-retrieval 2>&1)"; rc=$?
{ [ "$rc" -eq 0 ] && [ -f "$TMP/.research/docs/06-rag-retrieval/sources/note.md" ]; } && ok "converts into topic sources" || no "should write note.md (rc=$rc out=$out)"
rm -rf "$TMP"

echo "--- ingest: $pass passed, $fail failed ---"
[ "$fail" -eq 0 ]
