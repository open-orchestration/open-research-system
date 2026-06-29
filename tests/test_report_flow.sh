#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f skills/report/SKILL.md || { echo "FAIL: skills/report/SKILL.md missing"; exit 1; }
grep -qi "plan" skills/report/SKILL.md && grep -qi "findings" skills/report/SKILL.md \
  || { echo "FAIL: report flow must read plan + findings"; exit 1; }
grep -qi "citation\|\[c" skills/report/SKILL.md || { echo "FAIL: report must carry citations"; exit 1; }
echo "PASS report flow doc"
