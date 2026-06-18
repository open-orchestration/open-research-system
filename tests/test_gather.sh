#!/usr/bin/env bash
# Plain-bash test harness for gather.sh (no bats dependency).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
pass=0; fail=0
ok(){ echo "ok: $1"; pass=$((pass+1)); }
no(){ echo "FAIL: $1"; fail=$((fail+1)); }

mkroot(){ local t; t="$(mktemp -d)"; mkdir -p "$t/docs/06-rag-retrieval/sources"; echo "$t"; }

# Case 1: errors without a query
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/gather.sh" 06-rag-retrieval 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"query"* ]]; } && ok "errors without query" || no "should error w/o query (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 2: errors on unknown topic
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" bash "$ROOT/scripts/gather.sh" 99-nope "q" 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && [[ "$out" == *"no topic dir"* ]]; } && ok "errors on unknown topic" || no "should error unknown topic (rc=$rc out=$out)"
rm -rf "$TMP"

# Case 3: dry-run prints the search command for a valid topic+query (no network)
TMP="$(mkroot)"
out="$(env REPO_ROOT="$TMP" DRY_RUN=1 bash "$ROOT/scripts/gather.sh" 06-rag-retrieval "advanced RAG" 2>&1)"; rc=$?
{ [ "$rc" -eq 0 ] && [[ "$out" == *"search.py"* ]] && [[ "$out" == *"advanced RAG"* ]]; } && ok "dry-run prints search cmd" || no "dry-run failed (rc=$rc out=$out)"
rm -rf "$TMP"

echo "--- gather: $pass passed, $fail failed ---"
[ "$fail" -eq 0 ]
