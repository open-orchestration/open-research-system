#!/usr/bin/env bash
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
export REPO_ROOT="$TMP"
# resolve_topic_dir matches an EXISTING .research/docs/NN-* dir, so the topic must pre-exist.
mkdir -p "$TMP/.research" "$TMP/.research/docs/06-rag-retrieval"
IN="$TMP/ingest/.work/06-rag-retrieval"; mkdir -p "$IN"
printf 'clean research text about retrieval %.0s' {1..40} > "$IN/cabc12345-sample-1.md"
bash "$ROOT/scripts/ingest_flow.sh" 06-rag-retrieval --inbox "$IN"
landed="$(find "$TMP/.research/docs/06-rag-retrieval/sources" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
archived="$(find "$IN/_done" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
echo "landed=$landed archived=$archived"
[ "$landed" -ge 1 ] || { echo "FAIL: source not normalized into topic dir"; exit 1; }
[ "$archived" -ge 1 ] || { echo "FAIL: source not archived into scoped _done"; exit 1; }

# default-inbox regression: no --inbox flag still drains $ROOT/ingest
TMP2="$(mktemp -d)"; export REPO_ROOT="$TMP2"
mkdir -p "$TMP2/.research" "$TMP2/.research/docs/06-rag-retrieval" "$TMP2/ingest"
printf 'clean default-inbox text %.0s' {1..40} > "$TMP2/ingest/cdef67890-d.md"
bash "$ROOT/scripts/ingest_flow.sh" 06-rag-retrieval
def_landed="$(find "$TMP2/.research/docs/06-rag-retrieval/sources" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
rm -rf "$TMP2"
[ "$def_landed" -ge 1 ] || { echo "FAIL: default inbox regressed"; exit 1; }

echo "PASS ingest_flow inbox"
