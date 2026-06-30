#!/usr/bin/env bash
# ors_venv resolves a venv with bin/python by precedence, else fails with a nudge.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/scripts/lib.sh"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
mkstub() { mkdir -p "$1/bin"; printf '#!/bin/sh\n' > "$1/bin/python"; chmod +x "$1/bin/python"; }

# 1. ORS_VENV wins when valid.
mkstub "$TMP/a"
got="$(ORS_VENV="$TMP/a" CLAUDE_PLUGIN_DATA="$TMP/b" ors_venv)"
[ "$got" = "$TMP/a" ] && echo "ok: ORS_VENV wins" || { echo "MISS: got '$got'"; fail=1; }

# 2. CLAUDE_PLUGIN_DATA/venv next when ORS_VENV unset.
mkstub "$TMP/b/venv"
got="$(ORS_VENV= CLAUDE_PLUGIN_DATA="$TMP/b" ors_venv)"
[ "$got" = "$TMP/b/venv" ] && echo "ok: plugin-data venv" || { echo "MISS: got '$got'"; fail=1; }

# 3. Nudge + nonzero when nothing resolves (HOME redirected so ~/.venvs is absent).
out="$(ORS_VENV= CLAUDE_PLUGIN_DATA= HOME="$TMP/empty" ors_venv 2>&1)"; rc=$?
{ [ "$rc" -ne 0 ] && printf '%s' "$out" | grep -q "open-research-system:setup"; } \
  && echo "ok: fail nudges to setup" || { echo "MISS: rc=$rc out=$out"; fail=1; }

# 4. Helpers bundled in the plugin.
[ -f "$ROOT/scripts/crawl4ai/search.py" ] && [ -f "$ROOT/scripts/crawl4ai/fetch_md.py" ] \
  && echo "ok: helpers bundled" || { echo "MISS: helpers not bundled"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
