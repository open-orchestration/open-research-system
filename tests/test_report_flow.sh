#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f .claude/report.md || { echo "FAIL: .claude/report.md missing"; exit 1; }
grep -qi "plan" .claude/report.md && grep -qi "findings" .claude/report.md \
  || { echo "FAIL: report flow must read plan + findings"; exit 1; }
grep -qi "citation\|\[c" .claude/report.md || { echo "FAIL: report must carry citations"; exit 1; }
echo "PASS report flow doc"
