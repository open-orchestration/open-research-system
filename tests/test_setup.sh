#!/usr/bin/env bash
# setup.sh is idempotent: a pre-provisioned venv + present graphify => no install runs.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
# Stub a provisioned venv (fake python + markitdown).
mkdir -p "$TMP/venv/bin"
for b in python markitdown crawl4ai-setup pip; do printf '#!/bin/sh\n' > "$TMP/venv/bin/$b"; chmod +x "$TMP/venv/bin/$b"; done
# Shim graphify/uv/pip on PATH that RECORD calls (must not be invoked when idempotent).
mkdir -p "$TMP/shim"
for b in graphify uv pip; do printf '#!/bin/sh\necho "%s $@" >> "%s/calls.log"\n' "$b" "$TMP" > "$TMP/shim/$b"; chmod +x "$TMP/shim/$b"; done
# graphify present => no install. ORS_VENV provisioned => no build.
out="$(ORS_VENV="$TMP/venv" PATH="$TMP/shim:$PATH" bash "$ROOT/scripts/setup.sh" 2>&1)"; rc=$?
[ "$rc" -eq 0 ] && echo "ok: exit 0" || { echo "MISS: rc=$rc"; fail=1; }
printf '%s' "$out" | grep -q "already provisioned" && echo "ok: reports provisioned" || { echo "MISS: no provisioned msg"; fail=1; }
# graphify present (shim on PATH) => its installer never called; uv/pip never called.
if [ -f "$TMP/calls.log" ] && grep -qE "uv tool install|pip install" "$TMP/calls.log"; then
  echo "MISS: ran install when already provisioned"; fail=1
else echo "ok: no install on idempotent run"; fi
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
