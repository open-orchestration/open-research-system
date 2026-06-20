#!/usr/bin/env bash
# Static checks: the canvas wires up cytoscape, the WS-first/buffer/seed
# sequence, and a distinct asserted-edge style. No browser automation.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
H="$ROOT/public/index.html"

[ -f "$H" ] || { echo "FAIL: $H missing"; exit 1; }
need(){ grep -qF "$1" "$H" || { echo "FAIL: index.html missing: $1"; exit 1; }; }

need "cytoscape"
need 'integrity="sha512-'   # CDN script must carry Subresource Integrity
need 'new WebSocket("ws://" + location.host + "/ws")'
need 'fetch("/graph")'
need "buffer.push"
need 'edge[origin = "asserted"]'

echo "PASS graph view html"
