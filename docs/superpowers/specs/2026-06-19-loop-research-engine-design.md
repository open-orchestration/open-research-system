# Loop-Driven Research Engine — Design Spec

**Status:** approved design, pre-implementation
**Date:** 2026-06-19
**Scope of this spec:** the always-on research engine for `open-research-system`, built on Claude
Code's loop primitives. Covers the shared state spine, the phase-weighted budget governor, three
concurrent flows (search / ingest+graph / process), graph enrichment via asserted edges, and a
separable realtime graph view. The websocket UI is specified as a separable sub-project.

## 1. Goal

Turn the manual research spike into a continuously-running engine with three concurrent flows —
**search** (find sources), **ingest+graph** (normalize sources and incrementally update the
knowledge graph), and **process** (turn corpus into findings) — while humans drop sources (files,
videos, images, links, raw text) into an inbox at any time. Findings are human-gated before they
become "real."

The engine is **wiring, not greenfield**: the repo already has search (`scripts/gather.sh`), ingest
(`scripts/ingest.sh`), the graph (`.graphify/`), findings (`docs/findings/`), and synthesis
(`SYNTHESIS.md`). This design adds loop prompts, a state ledger, a review gate, a graph-assertion
overlay, and a delta event stream.

## 2. Locked decisions

| Decision | Choice | Rationale |
|---|---|---|
| Runtime | Claude Code `/loop` + `/goal` in an open session | Native loop primitives; zero custom infra |
| Durability | Session-alive (phase 1) | Simplest; prove the design before durable Routines/Actions |
| Orchestration | Start as **A** (independent loops + state file), converge to **C** (cheap watcher-loop + reasoning-goal) | Match cost/cadence split without a monolithic controller |
| Human-in-the-loop | **Gated findings**: search/ingest/graph autonomous; process emits drafts → review queue → human promotes | Loop-engineering "stay in the loop" + spike faithfulness gate |
| Search trigger | **Both** human-seeded queries and auto gap-driven discovery, under a budget cap | Autonomous discovery without runaway cost |
| Graph updates | `graphify --update` (incremental merge), **not** full rebuilds | graphify supports incremental natively; cheaper, enables realtime deltas |

### Concurrency reality
Session-scoped scheduled tasks fire **between turns**, not mid-response — the three loops
**interleave** (one acts at a time), they are not hard-parallel. True within-cycle parallelism comes
from **subagents** dispatched inside a flow's turn. For research workloads, interleaving is
acceptable; nothing requires real-time parallelism.

### Loop primitive constraints (verified)
- `/loop` + scheduled tasks use `CronCreate`/`CronList`/`CronDelete`; ≤50 tasks/session; fire between
  turns; **session-scoped** (die on new session, survive `--resume`); recurring tasks **expire after 7
  days**; deterministic jitter on fire times. Bare `/loop` self-paces.
- `/goal` runs until a verifiable condition is met; reliable for long horizons; wants a concrete
  success check.
- Durable alternatives (phase 2): Routines (Anthropic-managed), Desktop scheduled tasks, GitHub
  Actions.
- **The spine is an on-disk state file.** The model forgets between runs; the repo does not. Flows
  coordinate through `state.json`, never through conversation memory.

## 3. Architecture

### Repo mapping (reuse + 4 new artifacts)
```
ingest/                       EXISTS — human drop zone (the inbox); watched
docs/NN-topic/sources/        EXISTS — normalized corpus sources land here
docs/findings/                EXISTS — PROMOTED findings only
.graphify/                    EXISTS — generated graph (gitignored), incrementally updated
scripts/gather.sh, ingest.sh  EXISTS — flows call these

+ .research/state.json            NEW — the spine (queues, budget, corpus ledger, drafts)
+ .research/graph-assertions.jsonl NEW — asserted edges overlay (committed, append-only)
+ .research/graph-events.jsonl     NEW — append-only delta log (UI feed + audit)
+ docs/findings/_drafts/          NEW — draft findings awaiting human promotion
+ .claude/loop.md + per-flow prompt files  NEW — the loop prompts
```

### Derived vs. authored structure
Two durability classes, mirrored across the design:
- **Derived / disposable** (regenerated, gitignored): `.graphify/` graph, extracted markdown.
- **Authored / durable** (committed): `state.json`, `graph-assertions.jsonl`, promoted findings,
  native source files.

## 4. State spine — `.research/state.json`

One file to start; split if it grows (`ponytail: single file until it hurts`).

```jsonc
{
  "budget": {
    "tokens_per_cycle": 200000,
    "max_subagents": 8,
    "phase": "gather",                 // gather | deepen | synthesize  (human-set; flow may suggest)
    "weights": {                       // share of effort -> subagent count per flow, per phase
      "gather":     { "search": 0.7, "ingest": 0.3, "process": 0.0 },
      "deepen":     { "search": 0.4, "ingest": 0.3, "process": 0.3 },
      "synthesize": { "search": 0.1, "ingest": 0.1, "process": 0.8 }
    },
    "spent": { "tokens": 0, "sources": 0, "cycle_started_at": null }
  },
  "gaps":   [ { "id": "g001", "topic": "06-rag-retrieval", "desc": "...", "origin": "human|process",
               "status": "queued|in_progress|done|failed", "attempts": 0 } ],
  "inbox":  [ { "id": "i001", "path|url": "...", "type": "file|link|video|image|rawtext",
               "status": "new|ingesting|done|failed" } ],
  "corpus": [ { "id": "c001", "title": "...", "source": "...", "topic": "11-...",
               "lifecycle": "reference|active|archived", "native_path": "...",
               "extracted_path": "...", "lossy": false, "ingested_at": "..." } ],
  "graph":  { "dirty": true, "last_update": null, "node_count": 0, "edge_count": 0 },
  "assertions": { "count": 0, "file": ".research/graph-assertions.jsonl" },
  "drafts": [ { "id": "d001", "topic": "...", "path": "docs/findings/_drafts/...",
               "cites": ["c001","c008"], "confidence": 0.0,
               "status": "draft|in_review|promoted|rejected" } ]
}
```

This folds in:
- **findings-11** (records discipline): durable per-unit `id`, metadata at ingest, the `lifecycle`
  facet (`reference|active|archived`), native + extracted forms with a `lossy` flag.
- **findings-13** (deep-research loop): `gaps` is the reflect/re-scan backlog; process emits gaps,
  search consumes them.

## 5. Phase-weighted budget governor

Budget is a **policy, not a constant**. Each flow's parallelism is derived from the active phase:

```
subagents(flow) = round(budget.max_subagents * budget.weights[phase][flow])
```
capped by the hard `tokens_per_cycle`. A flow with weight `0.0` does not run that cycle.

- **gather** (early): search fans out ~6 subagents, ingest ~2, **process = 0** (no corpus to process).
- **deepen** (mid): effort splits across all three.
- **synthesize** (late): process gets ~6, search idles to ~1.

The phase **is** the breadth/depth dial from findings-13 made operational: gather = breadth, synthesize
= depth.

**Who sets `phase`:** human-set field. The process/ingest flow may write a *suggestion* into state when
corpus signals cross a threshold (e.g. "42 sources, gap-backlog=3 → recommend `deepen`") but never
auto-flips. Keeps the human in the loop; avoids a fragile auto-classifier in v1.

**Deferred — orchestrator self-tuning:** once search+process run under one `/goal` (convergence to C),
the orchestrator may auto-tune the `weights` table itself based on its read of research state (graph
density plateau, gap-backlog depth, source-novelty rate, draft-acceptance ratio). v1 keeps weights a
static human-set table with suggestions only. `ponytail: weights stay a static table in v1; orchestrator
self-adjusts later if the heuristic proves out.`

## 6. The flows

Each flow has: a trigger, a queue slice it owns, a subagent fan-out, and a **cheap local verifiable
success check** (a loop without a check is a loop making mistakes unattended). No flow self-certifies
*quality* — quality is the human gate.

### ① Search flow — `/loop` ~10m (converges into the `/goal`)
- **Reads:** `gaps[]` (human + process-authored), `budget`.
- **Does:** pop queued gaps within budget → fan out `subagents(search)` workers running `gather.sh`
  (crawl4ai search+fetch) → drop raw markdown into `ingest/` → mark gap `done`, decrement
  `budget.spent`.
- **Success check:** each popped gap yields ≥1 non-junk source file in `ingest/` (junk-detect guards
  the GitHub "Uh oh"/JS-shell and empty-page failures observed in the source-gathering work). On
  failure, re-queue the gap with `attempts++`; after K attempts mark `failed` and surface.
- **Idle:** no queued gaps or budget spent → exit cheap.

### ② Ingest + graph flow — `/loop` ~2m (cheap, frequent, responsive to human drops)
- **Reads:** `ingest/` dir + `inbox[]`.
- **Does:** for each new drop — normalize by type:
  - markdown / link → crawl4ai (already markdown, or fetch)
  - PDF / docx / pptx / xlsx / image → **markitdown**
  - video / YouTube → transcript (markitdown, with the `youtube-transcript-api` fallback that the
    markitdown path needs when its bundled extractor fails)
  - raw text → as-is

  Then assign **durable `id` + metadata + `lifecycle="active"`** → move to
  `docs/NN-topic/sources/<id>-slug.md`, keep native + extracted, set `lossy` → append to
  `state.corpus` → set `graph.dirty=true`. If dirty: run **`graphify --update`** (incremental merge),
  **replay the assertions overlay** (§6④), append the resulting `graph_diff` delta to
  `graph-events.jsonl` (§7), update `graph.node_count`/`edge_count`, clear `dirty`.
- **Success check:** `state.corpus` count rises by the number of files drained; `graphify --update`
  exits 0 and `node_count` does not decrease unexpectedly. Mismatch → flag, leave `dirty=true`, do not
  claim the corpus advanced.
- **Continuous updates, not rebuilds:** uses `graphify --update`; an occasional `cluster-only` or full
  integrity pass is a deferred maintenance task, not the hot path. Optionally run
  `python3 -m graphify.watch ingest/ --debounce 3` so a fan-out wave of source drops coalesces into one
  incremental update.

### ③ Process flow — `/goal` (gated by phase weight; **0 subagents in `gather`**)
- **Reads:** `corpus[]`, `.graphify/`, existing findings.
- **Does:** pick a topic with enough un-processed sources → run the **two-stage deep-research loop**
  (plan 3–5 sub-questions across perspectives → read corpus + graph → draft a finding with inline
  citations to `corpus` ids) → write to `docs/findings/_drafts/` with `status:"draft"` → emit any new
  `gaps[]` discovered (closes the loop to search) → optionally append graph assertions (§7) for links
  it perceives but the auto-pass missed.
- **Success check:** every claim cites a real `corpus` id that exists; a faithfulness self-check passes.
  Otherwise keep `draft` and do not surface for review.
- **Output contract (HITL):** draft → review queue → human **promotes** to `docs/findings/` +
  `SYNTHESIS.md`, or **rejects**.

### ④ Graph enrichment — asserted edges
Solves the findings-13 god-node caveat (god-node reading must traverse cross-community **bridges**, not
raw degree). Because the graph is incrementally updated from the corpus, hand-added edges must live in
an overlay that survives updates rather than inside the generated graph.

- **Store — `.research/graph-assertions.jsonl`** (append-only, committed):
  ```jsonc
  { "id":"a017", "from":"<node_id>", "to":"<node_id>",
    "relation":"bridges|supports|contradicts|refines",
    "rationale":"both describe citation-first provenance across different communities",
    "cites":["c003","c008"], "author":"ai", "confidence":0.8, "created_at":"..." }
  ```
- **Replay:** after each `graphify --update`, merge the overlay's edges into `graph.json`, each tagged
  `source:"asserted"` so god-node/bridge analysis can distinguish asserted from observed structure and
  can weight or quarantine asserted edges.
- **Author:** the process flow (and optionally a slow dedicated enrichment `/loop`) appends one
  assertion line when it perceives a missing link, with rationale + cited `corpus` ids.
- **Gating:** the graph layer is autonomous; assertions are a reversible, logged overlay → auto-applied
  and always recorded. Pruning a line and re-updating removes the edge. `author`/`confidence`/`cites`
  keep each asserted edge accountable (ties to the MADR/provenance requirement).

## 7. Realtime graph view (separable sub-project)

`graphify --update` already computes `graph_diff(G_old, G_new) → {new_nodes, new_edges}` on every
merge — that is the event payload; no extra delta computation needed.

```
ingest flow -> graphify --update -> graph_diff delta
            -> append to .research/graph-events.jsonl   (append-only: UI feed + audit log)
ws bridge (thin, ~30 lines): tail graph-events.jsonl -> push new lines over WebSocket
browser view: cytoscape/vis-network canvas -> nodes/edges animate in as they arrive
```

- The engine is **headless**; this is a **view that consumes the event stream**. The engine only needs
  to *emit* `graph-events.jsonl` (nearly free). The websocket bridge + canvas is a thin follow-on,
  specced separately, and does **not** block the core engine.
- Asserted edges (§6④) flow through the same stream tagged `source:"asserted"`, so the UI can render
  AI-added links distinctly, live.
- `--debounce` on the watcher coalesces a subagent fan-out into one update, preventing graph/UI thrash.
- `ponytail: WebSocket per the explicit ask; SSE or browser file-tail is a lazier equivalent if the ws
  server proves to be overhead.`

## 8. Data flow — one source's journey
```
human drop OR search subagent     ->  ingest/<raw>
  ingest loop: detect type -> normalize (markitdown | crawl4ai | raw)
             -> assign durable id + metadata + lifecycle="active"
             -> docs/NN-topic/sources/<id>-slug.md   (native kept, lossy flag set)
             -> state.corpus += entry ; graph.dirty=true
  graphify --update (incremental) -> replay assertions -> append graph_diff to graph-events.jsonl
  process goal (if phase weight > 0): read corpus+graph -> draft cites [corpus_id]
             -> docs/findings/_drafts/ ; emit new gaps[] ; maybe append assertions
  HUMAN: review draft -> promote to docs/findings/ + SYNTHESIS.md   OR reject
  retention cycle: active sources age -> "archived" (findings-11 lifecycle)
```

## 9. Error handling — crash-safety by design
- `state.json` is the only source of truth; **every flow is idempotent** — re-running a cycle is
  harmless (durable ids + `status` fields guard double-work). Session dies → `--resume` picks up from
  state.
- Failed/junk fetch → re-queue gap with `attempts++`; after K tries mark `failed` + surface.
- Unparseable ingest → `ingest/_failed/` + log; the loop continues, never crashes.
- Budget spent → flows exit cheap until the next cycle resets `spent`.
- `graphify --update` fails → leave `dirty=true`, retry next cycle; do not claim corpus advanced.
- **No real races:** loops interleave between turns; `status:"ingesting"/"in_review"` stops a later
  cycle grabbing in-flight work. When C converges to true parallel subagents, writes stay per-id and
  append-only — no shared-file contention. The graph watcher's debounce coalesces concurrent drops.

## 10. Verification & testing (extends existing `tests/`)
- **Schema/integrity check:** `state.json` valid; every `corpus` entry has a real file; every draft
  cite resolves to a `corpus` id; no orphan sources; every assertion references existing node ids.
- **Dry-run:** `DRY_RUN=1` per flow (already in `gather.sh`) to exercise logic without spending tokens.
- **Fixture self-check:** a tiny `ingest/` drop → run one ingest cycle → assert corpus + graph
  advanced and a `graph-events.jsonl` delta was appended. (Smallest thing that fails if the logic
  breaks.)

## 11. Build order (sub-projects)
1. **Spine + ingest flow** — `state.json`, the ingest loop (normalize → durable id/metadata/lifecycle →
  `graphify --update` → graph-events delta), schema/integrity test. Proves the substrate end-to-end
  with human drops only.
2. **Search flow** — gap queue + budget governor + `gather.sh` fan-out, junk-detect + re-queue.
3. **Process flow** — deep-research draft loop + review gate + gap emission.
4. **Graph enrichment** — assertions overlay + replay.
5. **Realtime view** — websocket bridge + canvas (separable; non-blocking).
6. **Convergence A→C** — merge ingest+graph into one fast loop, fold search+process under one budgeted
  `/goal`; then (deferred) orchestrator weight self-tuning.

Each sub-project gets its own spec → plan → implementation cycle. This spec covers the architecture all
six share; sub-project #1 (spine + ingest) is the first implementation plan.

## 12. Out of scope (this spec)
- Durable runtime (Routines / Desktop tasks / GitHub Actions) — phase 2.
- Orchestrator weight auto-tuning — deferred to convergence.
- The websocket UI's visual design — its own sub-project spec.
- Whether the doc-organization theme becomes catalog topic #18 — separate catalog decision.

## 13. Provenance
Grounded in this session's research passes: `docs/findings/13-deepresearch-skills-survey.md`
(deep-research loop, clarify/cheap-vs-run/expensive, search+fetch tool shape, injection boundary),
`docs/findings/11-document-organization-records.md` (durable ids, metadata-at-ingest, lifecycle facet,
ESI/Bates provenance), and the loop-engineering corpus
(`docs/07-agentic-orchestration/sources/loop-engineering/`: `/loop`, `/goal`, scheduled tasks,
ralph-loop, the state-file-as-spine pattern, comprehension-debt warning).
