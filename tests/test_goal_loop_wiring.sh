#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
grep -q "meter.py update" .claude/goal.md || { echo "FAIL: goal.md missing meter step"; exit 1; }
grep -q "dimension_gate.py" .claude/goal.md || { echo "FAIL: goal.md missing dimension gate"; exit 1; }
grep -q '"stop"' .claude/goal.md || grep -q "D.stop" .claude/goal.md || { echo "FAIL: goal.md not stopping on D.stop"; exit 1; }
grep -q "add-dim-candidate" .claude/process.md || { echo "FAIL: process.md not emitting candidates"; exit 1; }
echo "PASS loop wiring"
