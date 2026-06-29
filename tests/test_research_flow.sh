#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f skills/research/SKILL.md || { echo "FAIL: skills/research/SKILL.md missing"; exit 1; }
# the flow must reference the three load-bearing steps
grep -q "ors plan apply" skills/research/SKILL.md || { echo "FAIL: no ors plan apply step"; exit 1; }
grep -q "validate" skills/research/SKILL.md || { echo "FAIL: no validation/halt step"; exit 1; }
grep -qi "goal.md\|/goal" skills/research/SKILL.md || { echo "FAIL: no handoff to /goal loop"; exit 1; }
echo "PASS research flow doc"
