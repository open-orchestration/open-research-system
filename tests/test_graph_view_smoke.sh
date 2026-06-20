#!/usr/bin/env bash
# End-to-end against the real CLI: launch the server on a free port over temp
# artifacts, assert GET / serves the canvas, GET /graph serves the snapshot,
# and an appended event line arrives over the WebSocket. Stdlib only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
SRV_PID=""
cleanup() { [ -n "$SRV_PID" ] && kill "$SRV_PID" 2>/dev/null || true; rm -rf "$TMP"; }
trap cleanup EXIT

printf '' > "$TMP/events.jsonl"
echo '{"nodes":[{"id":"seed"}],"links":[]}' > "$TMP/graph.json"
LOG="$TMP/server.log"

# Bind an ephemeral port (--port 0); the server prints the actual port it bound,
# so there is no free-port race.
python3 "$ROOT/scripts/graph_view_server.py" --host 127.0.0.1 --port 0 \
  --events "$TMP/events.jsonl" --graph "$TMP/graph.json" \
  --html "$ROOT/public/index.html" >"$LOG" 2>&1 &
SRV_PID=$!

PORT=""
for _ in $(seq 1 50); do
  PORT="$(sed -n 's#.*http://127.0.0.1:\([0-9][0-9]*\).*#\1#p' "$LOG" | head -1)"
  [ -n "$PORT" ] && break
  sleep 0.1
done
[ -n "$PORT" ] || { echo "FAIL: server did not report a port"; cat "$LOG"; exit 1; }

python3 - "$PORT" "$TMP" "$ROOT" <<'PY'
import json, socket, sys, time, urllib.request
port, tmp, root = int(sys.argv[1]), sys.argv[2], sys.argv[3]

html = urllib.request.urlopen(f"http://127.0.0.1:{port}/").read().decode("utf-8")
assert "cytoscape" in html, "GET / did not serve the canvas"

graph = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/graph"))
assert graph["nodes"][0]["id"] == "seed", "GET /graph snapshot wrong"

s = socket.create_connection(("127.0.0.1", port), timeout=5)
s.settimeout(5)
s.sendall(b"GET /ws HTTP/1.1\r\nHost: x\r\nUpgrade: websocket\r\n"
          b"Connection: Upgrade\r\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
          b"Sec-WebSocket-Version: 13\r\n\r\n")
resp = s.recv(1024).decode("latin-1")
assert "101" in resp and "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=" in resp, "bad handshake"

time.sleep(0.3)
with open(f"{tmp}/events.jsonl", "a", encoding="utf-8") as fh:
    fh.write('{"new_nodes":["live1"],"new_edges":[],"edge_origins":{}}\n')

frame = s.recv(4096)
assert frame[0] == 0x81, "not a text frame"
_b1 = frame[1]
_off = 2 if _b1 < 126 else (4 if _b1 == 126 else 10)
payload = frame[_off:]
assert json.loads(payload.decode("utf-8"))["new_nodes"] == ["live1"], "delta not received"
s.close()
print("PASS graph view smoke")
PY
