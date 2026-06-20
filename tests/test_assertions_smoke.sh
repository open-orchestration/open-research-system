#!/usr/bin/env bash
# End-to-end: seed corpus + graph -> add assertion -> replay -> integrity clean
# -> prune -> replay -> assertion gone. Stdlib only; no network.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/.graphify"
# Minimal corpus entry (extracted file must exist for integrity).
echo "src" > "$TMP/e.md"
python3 "$ROOT/scripts/state.py" add-corpus --root "$TMP" \
  --title T --source S --topic t --native n --extracted e.md --id c0000aaaa >/dev/null
# Minimal node_link graph with two nodes.
cat > "$TMP/.graphify/graph.json" <<'JSON'
{"nodes":[{"id":"node_x"},{"id":"node_y"}],"links":[]}
JSON

AID="$(python3 "$ROOT/scripts/assertions.py" add --root "$TMP" \
  --from node_x --to node_y --relation bridges \
  --rationale "bridge" --cites c0000aaaa)"
echo "added $AID"

python3 "$ROOT/scripts/assertions.py" replay --root "$TMP"
COUNT="$(python3 -c "import json,sys; g=json.load(open('$TMP/.graphify/graph.json')); print(sum(1 for l in g['links'] if l.get('_origin')=='asserted'))")"
[ "$COUNT" = "1" ] || { echo "FAIL: expected 1 asserted link, got $COUNT"; exit 1; }

python3 "$ROOT/scripts/check_integrity.py" --root "$TMP"

python3 "$ROOT/scripts/assertions.py" prune --root "$TMP" "$AID"
python3 "$ROOT/scripts/assertions.py" replay --root "$TMP"
COUNT2="$(python3 -c "import json,sys; g=json.load(open('$TMP/.graphify/graph.json')); print(sum(1 for l in g['links'] if l.get('_origin')=='asserted'))")"
[ "$COUNT2" = "0" ] || { echo "FAIL: expected 0 asserted links after prune, got $COUNT2"; exit 1; }

# Success-check invariant: asserted links == active overlay lines.
ACTIVE="$(python3 -c "import sys; sys.path.insert(0,'$ROOT/scripts'); import assertions; print(len(assertions.load_overlay('$TMP')))")"
[ "$ACTIVE" = "0" ] || { echo "FAIL: expected 0 active assertions, got $ACTIVE"; exit 1; }

echo "PASS assertions smoke"
