#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(mktemp -d)"
trap 'rm -rf "$ROOT"' EXIT
cat > "$ROOT/plan.json" <<'JSON'
{"shape":"comparison","entities":["777","A380"],
 "dimensions":[{"name":"fuel","why":"x"},{"name":"range","why":"y"}],
 "topics":[],
 "seed_gaps":[{"topic":"fuel","desc":"777 fuel"},{"topic":"range","desc":"A380 range"}],
 "rationale":"r"}
JSON
python3 scripts/plan.py apply --root "$ROOT" --question "777 vs A380" --budget 1000000 --plan-file "$ROOT/plan.json"
# goal record + queued gaps + run budget present
python3 - "$ROOT" <<'PY'
import json, sys
s = json.load(open(sys.argv[1] + "/.research/state.json"))
assert s["goal"]["shape"] == "comparison", s["goal"]
assert len([g for g in s["gaps"] if g["status"] == "queued"]) == 2
assert s["budget"]["run"]["token_ceiling"] == 1000000
assert s["budget"]["dimension_alpha"]["wealth"] == 5
print("e2e state OK")
PY
# budget stop fires when spent >= ceiling
python3 scripts/state.py set-run-spent --root "$ROOT" --tokens 1000000
python3 scripts/orchestrator.py decide --root "$ROOT" | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["stop"] and d["budget_exhausted"], d; print("e2e stop OK")'
echo "PASS planner e2e"
