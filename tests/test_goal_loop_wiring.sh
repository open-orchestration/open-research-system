#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
grep -q "ors meter update" skills/_flows/goal.md || { echo "FAIL: goal.md missing meter step"; exit 1; }
grep -q "ors dim" skills/_flows/goal.md || { echo "FAIL: goal.md missing dimension gate"; exit 1; }
grep -q '"stop"' skills/_flows/goal.md || grep -q "D.stop" skills/_flows/goal.md || { echo "FAIL: goal.md not stopping on D.stop"; exit 1; }
grep -q "add-dim-candidate" skills/_flows/process.md || { echo "FAIL: process.md not emitting candidates"; exit 1; }
echo "PASS loop wiring"
