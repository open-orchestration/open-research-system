#!/usr/bin/env bash
# The packaged skills/flows must not instruct an agent to write legacy root-level
# research files into a target project. The original corpus spike kept
# RESEARCH-CATALOG.md and SYNTHESIS.md at the repo root; the plugin namespaces all
# output under $DOCS_BASE/ (.research/docs). Regression guard for target-root pollution.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

# No executed skill/flow may name the legacy catalog at all (it no longer exists in
# the autonomous flow — the planner's state.json plan replaced it).
if grep -rIn "RESEARCH-CATALOG" "$ROOT/skills" >/dev/null 2>&1; then
  echo "MISS: skills/ reference legacy RESEARCH-CATALOG"; grep -rIn "RESEARCH-CATALOG" "$ROOT/skills"; fail=1
else echo "ok: no RESEARCH-CATALOG in skills/"; fi

# Every SYNTHESIS.md mention under skills/ must be path-qualified to findings/, so an
# agent following the prose writes it under $DOCS_BASE/findings, never the project root.
while IFS= read -r line; do
  [ -n "$line" ] || continue
  printf '%s' "$line" | grep -q "findings" \
    || { echo "MISS: unqualified SYNTHESIS.md -> $line"; fail=1; }
done < <(grep -rIn "SYNTHESIS\.md" "$ROOT/skills" 2>/dev/null)
[ "$fail" = 0 ] && echo "ok: all SYNTHESIS.md refs qualified under findings/"

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
