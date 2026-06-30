#!/usr/bin/env bash
# SessionStart nudge: if research deps are not provisioned, print one line pointing
# at /open-research-system:setup. Never blocks a session — always exits 0.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ors_venv >/dev/null 2>&1 \
  || echo "open-research-system: research deps not provisioned — run /open-research-system:setup"
exit 0
