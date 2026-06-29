#!/usr/bin/env bash
# The dashboard skill must (a) copy the UI into the target's .research/dashboard so
# the project owns a standalone copy, and (b) wire ALL six data/UI paths the server
# honors to the target — including GV_EVENTS (live feed) and GV_RUNLOG (loop panel),
# which an earlier version omitted, so those panels silently read the plugin dir.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SK="$ROOT/skills/dashboard/SKILL.md"
fail=0

for v in GV_GRAPH GV_STATE GV_RUNLOG GV_EVENTS GV_HTML GV_DASHBOARD; do
  grep -q "${v}=" "$SK" || { echo "MISS: dashboard skill does not set ${v}"; fail=1; }
done
[ "$fail" = 0 ] && echo "ok: all six GV_* set"

# The UI is copied into the target's .research/dashboard, and the HTML is served from
# that copy (not straight from the plugin bundle).
grep -q '\.research/dashboard' "$SK" || { echo "MISS: no .research/dashboard copy target"; fail=1; }
grep -qE 'cp .*public/' "$SK" || { echo "MISS: no cp of public/ UI into the target"; fail=1; }
grep -q 'GV_HTML="\$DASH/index.html"' "$SK" 2>/dev/null \
  || grep -qE 'GV_HTML=.*\.research/dashboard' "$SK" \
  || { echo "MISS: GV_HTML not served from the target copy"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
