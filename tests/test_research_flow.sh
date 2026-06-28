#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f .claude/research.md || { echo "FAIL: .claude/research.md missing"; exit 1; }
# the flow must reference the three load-bearing steps
grep -q "plan.py apply" .claude/research.md || { echo "FAIL: no plan.py apply step"; exit 1; }
grep -q "validate" .claude/research.md || { echo "FAIL: no validation/halt step"; exit 1; }
grep -qi "goal.md\|/goal" .claude/research.md || { echo "FAIL: no handoff to /goal loop"; exit 1; }
echo "PASS research flow doc"
