#!/usr/bin/env bash
# Structural lint for the spike repo. Exit non-zero on any missing piece.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
check() { local label="$1"; shift; if "$@"; then echo "ok: $label"; else echo "MISS: $label"; fail=1; fi; }

# Top-level files
for f in README.md .gitignore RESEARCH-CATALOG.md SYNTHESIS.md; do
  check "$f exists" test -f "$ROOT/$f"
done

# Required dirs
for d in ingest docs docs/findings docs/diagrams scripts tests; do
  check "$d/ exists" test -d "$ROOT/$d"
done

# 17 topic dirs
topics=(01-methodology-epistemics 02-statistical-causal-inference 03-decision-frameworks \
04-applied-research-playbooks 05-ai-deep-research-systems 06-rag-retrieval \
07-agentic-orchestration 08-grounding-truth 09-knowledge-compilation-graphs \
10-context-prompt-engineering 11-research-pipeline-engineering 12-tooling-landscape \
13-reference-systems-case-studies 14-papers 15-textbooks-longform \
16-evaluation-benchmarks 17-specs-standards)
for t in "${topics[@]}"; do
  check "docs/$t/README.md" test -f "$ROOT/docs/$t/README.md"
  check "docs/$t/sources/" test -d "$ROOT/docs/$t/sources"
done

# RESEARCH-CATALOG must reference all 17 topic slugs
if [ -f "$ROOT/RESEARCH-CATALOG.md" ]; then
  for t in "${topics[@]}"; do
    check "catalog mentions $t" grep -qF -- "$t" "$ROOT/RESEARCH-CATALOG.md"
  done
fi

[ "$fail" -eq 0 ] && echo "ALL OK" || echo "LINT FAILED"
exit "$fail"
