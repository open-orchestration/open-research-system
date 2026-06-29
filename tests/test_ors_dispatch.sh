#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ORS="$ROOT/bin/ors"
fail=0

# 1. Generic python verb resolves to scripts/<verb>.py (plan.py prints usage on --help).
"$ORS" plan --help >/dev/null 2>&1 && echo "ok: plan verb runs" \
  || { echo "MISS: plan verb"; fail=1; }

# 2. Alias: decide -> orchestrator.py (has a 'decide' subcommand).
"$ORS" decide --help >/dev/null 2>&1 && echo "ok: decide alias" \
  || { echo "MISS: decide alias"; fail=1; }

# 3. Shell-flow verb: search -> search_flow.sh (usage exit 2 when no --topic).
"$ORS" search >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: search alias" \
  || { echo "MISS: search alias"; fail=1; }

# 3b. Remaining shell-flow aliases: exit 2 with no args.
"$ORS" dim    >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: dim alias"    || { echo "MISS: dim alias";    fail=1; }
"$ORS" ingest >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: ingest alias" || { echo "MISS: ingest alias"; fail=1; }
"$ORS" gather >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: gather alias" || { echo "MISS: gather alias"; fail=1; }

# 4. Unknown verb exits 2.
"$ORS" nonsense >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: unknown verb exit 2" \
  || { echo "MISS: unknown verb"; fail=1; }

# 5. Defaults exported (run a verb that echoes them via a tiny probe).
out="$(REPO_ROOT= DOCS_BASE= "$ORS" __envprobe 2>/dev/null)"
echo "$out" | grep -q "REPO_ROOT=$PWD" && echo "ok: REPO_ROOT default" \
  || { echo "MISS: REPO_ROOT default ($out)"; fail=1; }
echo "$out" | grep -q "DOCS_BASE=.research/docs" && echo "ok: DOCS_BASE default" \
  || { echo "MISS: DOCS_BASE default ($out)"; fail=1; }

# 6. decide alias actually routes to orchestrator's `decide` subcommand (not just --help).
TMP_D="$(mktemp -d)"; mkdir -p "$TMP_D/.research"
cat > "$TMP_D/.research/plan-input.json" <<'JSON'
{"shape":"survey","entities":[],"dimensions":[],"topics":[{"name":"t","why":"x"}],
 "seed_gaps":[{"topic":"t","desc":"d"}],"rationale":"r"}
JSON
"$ORS" plan apply --root "$TMP_D" --question "q" --budget 100000 --plan-file "$TMP_D/.research/plan-input.json" >/dev/null 2>&1
dout="$("$ORS" decide --root "$TMP_D" --apply 2>&1)"
echo "$dout" | grep -q '"phase"' && echo "ok: decide routes to subcommand" || { echo "MISS: decide routing ($dout)"; fail=1; }
rm -rf "$TMP_D"

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
