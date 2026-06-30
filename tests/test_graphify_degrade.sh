#!/usr/bin/env bash
# The loop's graph-update step is guarded: if graphify is unavailable, it skips (not aborts).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOOP="$ROOT/skills/_flows/loop.md"
fail=0
# Flatten newlines first — the guard prose may wrap across lines.
flat="$(tr '\n' ' ' < "$LOOP")"
printf '%s' "$flat" | grep -qiE "graphify skill is (available|installed)" \
  && echo "ok: availability guard" || { echo "MISS: no availability guard"; fail=1; }
printf '%s' "$flat" | grep -qiE "skip the graph update|status skip" \
  && echo "ok: skip path" || { echo "MISS: no skip path"; fail=1; }
[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"; exit "$fail"
