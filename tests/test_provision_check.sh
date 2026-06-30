#!/usr/bin/env bash
# provision_check nudges when unprovisioned, is silent when provisioned, always exit 0.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
# Unprovisioned: nudge on stdout, exit 0.
out="$(ORS_VENV= CLAUDE_PLUGIN_DATA= HOME="$TMP/empty" bash "$ROOT/scripts/provision_check.sh")"; rc=$?
{ [ "$rc" -eq 0 ] && printf '%s' "$out" | grep -q "open-research-system:setup"; } \
  && echo "ok: nudges + exit 0" || { echo "MISS: rc=$rc out=$out"; fail=1; }
# Provisioned: silent, exit 0.
mkdir -p "$TMP/venv/bin"; printf '#!/bin/sh\n' > "$TMP/venv/bin/python"; chmod +x "$TMP/venv/bin/python"
out="$(ORS_VENV="$TMP/venv" bash "$ROOT/scripts/provision_check.sh")"; rc=$?
{ [ "$rc" -eq 0 ] && [ -z "$out" ]; } && echo "ok: silent when provisioned" \
  || { echo "MISS: rc=$rc out='$out'"; fail=1; }
# hooks.json valid + wires the check.
python3 -c "import json;h=json.load(open('$ROOT/hooks/hooks.json'));assert 'SessionStart' in h['hooks']" \
  && grep -q 'provision_check.sh' "$ROOT/hooks/hooks.json" && echo "ok: hook wired" \
  || { echo "MISS: hooks.json"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
