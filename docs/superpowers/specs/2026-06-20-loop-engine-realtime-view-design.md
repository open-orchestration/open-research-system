# Sub-project #5 — Realtime graph view (design)

Date: 2026-06-20. Umbrella spec: `2026-06-19-loop-research-engine-design.md` §7.

## Goal

A browser view that watches the knowledge graph grow live. The engine is
**headless** and already appends a delta record to `.research/graph-events.jsonl`
on every ingest cycle. This sub-project is a **view that consumes that stream** —
it never blocks or mutates the core engine. Started manually
(`python3 scripts/graph_view_server.py`), it serves a canvas and pushes each new
delta to the browser as it lands. AI-asserted edges (sub-project #4) render
distinctly from corpus-extracted edges, live.

## Settled decisions (brainstorm)

- **Transport: true WebSocket, hand-rolled on stdlib — no pip.** RFC6455
  server→client framing is small for a push-only feed (SHA-1 handshake +
  text-frame encoding). Keeps the repo's Python-3-stdlib-only convention intact
  while delivering the WebSocket the spec asks for. The `websockets` library is
  convenience, not necessity here, and is **not** added.
- **Asserted-edge distinction: enrich the event payload.** `graph_events` carries
  per-edge provenance so the stream is self-describing; the UI reads a tag rather
  than cross-referencing the overlay file. (Spec §7 carryover option (a).)
- **Canvas: cytoscape.js via CDN** (single file, clean incremental `cy.add`).
- **Scope: minimal live graph.** Nodes + edges animate in, asserted edges styled
  distinctly, auto-layout, node `id` labels. No filters/search/details panel —
  those are later work.
- **Seed/stream race: open WS first, buffer, then seed.** Avoids the gap where a
  delta appends between `fetch('/graph')` and the WS opening.

## Components

### 1. `graph_events.py` enrichment (the #4→#5 carryover)

`diff(old, new)` returns one new key, `edge_origins`: for each edge in
`new_edges`, look up its `_origin` in the **new** graph's `links` and record only
non-default origins (i.e. `"asserted"`), keyed `"<source>|<target>"`.

`append_event` writes the key through:

```json
{"ts": "2026-06-20T...", "new_nodes": ["n1"], "new_edges": [["a","b"]], "edge_origins": {"a|b": "asserted"}}
```

- **Backward-compatible.** Only asserted edges appear in `edge_origins`; extracted
  edges are absent and the UI defaults them to `"extracted"`. Existing consumers
  (none today besides the UI) ignore the extra key.
- `loop.md` is **unchanged** — it still calls
  `graph_events.py append --old .graphify/.graphify_old.json --new .graphify/graph.json --events .research/graph-events.jsonl`.
- Origin lookup uses the same `_origin` field assertions replay writes (NOT
  `source`, which is the node_link endpoint key). Consistent with #4.

### 2. `scripts/graph_view_server.py` — stdlib `ThreadingHTTPServer`

Routes on a `BaseHTTPRequestHandler`:

- `GET /` → the static HTML canvas (`public/index.html`).
- `GET /graph` → current `.graphify/graph.json` verbatim (snapshot seed);
  `{}` with 200 if the graph file is absent.
- `GET /ws` with `Upgrade: websocket` → RFC6455 handshake, then **this client's
  own thread** seeks to the current end of `graph-events.jsonl`, polls for
  newly-appended **complete** lines (newline-terminated; a torn final line waits
  for its newline), wraps each in a text frame, and sends. The thread exits when a
  send raises (client disconnected).

Design notes:

- **No client registry, no lock.** `ThreadingHTTPServer` gives one thread per
  connection; each WS client tails the file independently from its own offset.
  `ponytail: per-client poll-tail; a shared broadcaster only if client count ever
  matters.`
- **Poll, don't inotify.** Stdlib has no portable file-watch; a short
  `time.sleep` poll loop tracking byte offset is the stdlib-correct tail.
  `ponytail: poll-tail; swap for inotify only if latency matters.`
- **Configurable paths.** Events-file path, graph-file path, html path, host, and
  port come from argv/env (defaults: `.research/graph-events.jsonl`,
  `.graphify/graph.json`, `public/index.html`, `127.0.0.1`, `8000`) so tests point
  at temp files and an ephemeral port. Binds **localhost only** by default — the
  server is unauthenticated, so wider exposure would leak graph contents.

#### RFC6455 specifics (push-only subset)

- Handshake: `base64(sha1(Sec-WebSocket-Key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"))`
  → `Sec-WebSocket-Accept`; reply `101 Switching Protocols` with
  `Upgrade/Connection/Sec-WebSocket-Accept` headers.
- Text frame: byte0 `0x81` (FIN + opcode 1). Length: `<126` → one byte;
  `126..65535` → `0x7E` + 2-byte big-endian; `≥65536` → `0x7F` + 8-byte
  big-endian. Server→client frames are **unmasked**. Payload is UTF-8.
- Client→server frames (masked) are not parsed beyond best-effort: a failed/closed
  socket just ends the thread. No ping/pong (`ponytail: add ping keepalive only if
  proxies drop idle sockets`).

### 3. Static HTML canvas — cytoscape.js via CDN

`public/index.html`. On load:

1. Open `WebSocket('ws://' + location.host + '/ws')`; while not yet seeded,
   **buffer** incoming delta messages.
2. `fetch('/graph')` → add snapshot nodes/edges to cytoscape, set `seeded = true`,
   then drain the buffer (cytoscape `add` is idempotent on `id`, so a snapshot/
   delta overlap is harmless). Snapshot edges set `origin` from each link's
   `_origin` field (default `"extracted"`) so seeded asserted edges style the same
   as delta ones.
3. Each delta: `cy.add` the `new_nodes` (data `{id}`) and `new_edges`
   (data `{id: "s|t", source, target, origin: edge_origins["s|t"] || "extracted"}`),
   then run an incremental layout.
4. Style: `edge[origin = "asserted"]` rendered distinctly (dashed + accent color);
   nodes labelled by `id`.

## Data flow

```
ingest cycle -> graphify --update -> assertions replay -> graph_events append
                                                          (-> graph-events.jsonl)
graph_view_server (separate manual process):
   tails graph-events.jsonl  -> WS text frame -> browser
   serves /graph snapshot + / canvas
browser: seed from /graph, then animate deltas from WS
```

The view is strictly downstream of the append-only log — it cannot affect engine
correctness or throughput.

## Testing (stdlib `unittest` + bash smoke)

- **Handshake vector:** RFC6455 canonical example —
  key `dGhlIHNhbXBsZSBub25jZQ==` → accept `s3pPLMBiTxaQ9kYGzzhZRbK+xOo=`.
- **Frame encoding:** short (`<126`) and medium (`126..65535`) payload lengths
  produce the correct header bytes; FIN+text opcode `0x81`; unmasked.
- **`diff` provenance:** an asserted edge in the new graph yields
  `edge_origins["a|b"] == "asserted"`; an extracted edge is absent from the map;
  existing `new_nodes`/`new_edges` output is unchanged.
- **End-to-end smoke (bash + raw socket, no browser):** start the server on an
  ephemeral port against a temp events file, perform the handshake over a raw
  socket, assert `101` + correct `Sec-WebSocket-Accept`, append a delta line to
  the temp file, read the next frame, decode it, and assert the delta JSON
  arrived. Stdlib `socket`/`http`/`hashlib` only — no browser automation.

## Conventions honored

- Python 3 stdlib only; no pip, no pytest; tests are `unittest` + bash
  `test_*.sh`. No lint/type suppression comments.
- The server is a **view**: read-only on engine artifacts, never writes
  `.research/` or `.graphify/`, never part of a loop. Started manually.
- New artifacts: `scripts/graph_view_server.py`, `public/index.html`,
  `tests/test_graph_view_server.py` (+ the `diff` provenance assertion alongside
  existing `graph_events` tests), a bash smoke `test_*.sh`, and a README
  "Realtime graph view" section (launch command + what the browser shows).

## Non-goals (later work)

Filters, search, node/edge detail panels, relation-type edge labels, a legend,
authentication, multi-graph/topic switching, ping/pong keepalive, inotify, a
shared broadcaster.
