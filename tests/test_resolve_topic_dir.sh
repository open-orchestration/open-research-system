#!/usr/bin/env bash
# resolve_topic_dir must find an existing topic dir OR create the next NN-<slug>
# one, slugifying the arg first (autonomous planner seeds free-text topic names).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/scripts/lib.sh"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0

# 1. Free-text topic, empty root => creates docs/01-columnar-storage and returns it.
d="$(resolve_topic_dir "$TMP" "columnar storage")" \
  || { echo "MISS: returned nonzero on create"; fail=1; }
[ "$d" = "$TMP/docs/01-columnar-storage" ] \
  && echo "ok: created $d" || { echo "MISS: got '$d'"; fail=1; }
[ -d "$d" ] && echo "ok: dir exists" || { echo "MISS: dir not created"; fail=1; }

# 2. Slug form of same topic resolves to the SAME dir (idempotent, slugify parity).
d2="$(resolve_topic_dir "$TMP" "columnar-storage")"
[ "$d2" = "$d" ] && echo "ok: idempotent on slug" || { echo "MISS: '$d2' != '$d'"; fail=1; }

# 3. New topic picks the next free NN (continues numbering past existing dirs).
d3="$(resolve_topic_dir "$TMP" "Vectorized Execution")"
[ "$d3" = "$TMP/docs/02-vectorized-execution" ] \
  && echo "ok: next NN" || { echo "MISS: got '$d3'"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
