# Tier 1 — concurrent queue burn (parallel search+ingest)

**Status:** approved design, pre-plan.
**Scope:** make the engine drain its gap queue with a configurable number of concurrent
search+ingest workers, without corrupting the shared `.research/state.json` spine or the
single global knowledge graph. Graph writes stay serial.

## 1. Goal

Today one `/goal` cycle runs search+ingest **sequentially per topic** (a bash `for` loop).
The slow part is network (crawl4ai search+fetch); the unsafe part is shared-state mutation.
Tier 1 separates them: fan out the network-bound work across `budget.max_workers` topic
workers, while every `state.json` mutation passes through a cross-process lock and the
single graph is still written by exactly one serial step.

This is the prerequisite the §2 "Concurrency reality" decision deferred: the spec chose
interleave + subagent fan-out and noted true parallelism needs per-id, append-only writes —
but `state.json` is a single rewritten blob and the budget is shared, so any real
parallelism first needs a transaction lock. Tier 1 supplies it.

## 2. Locked decisions

| Decision | Choice | Rationale |
|---|---|---|
| Shard key | **topic** | gaps carry a topic; `ingest_flow` already routes by topic, so per-topic work is naturally disjoint — no two workers touch the same gap or the same inbox files. |
| Lock | advisory `fcntl.flock(LOCK_EX)` on a **stable sidecar** `.research/state.lock` | `save()` does tmp-write + `os.replace`, which swaps the inode; a lock on the state file's own fd would not protect the replacement. The sidecar never moves. `fcntl` is stdlib — no dependency. |
| Lock scope | **per mutation**, not per flow | each `state.py` CLI call is a separate process that acquires the lock briefly; fetch/junk-filter happen entirely outside any lock. Holding a lock across a whole `search_flow` run would serialize the workers and defeat the point. |
| Budget contract | **strict, reserve-before-fetch** | worker atomically reserves budget up front, fetches only within the reservation, refunds the unused remainder after junk-filtering. Kept sources can never exceed `sources_per_cycle`, and no fetch is wasted on discard. |
| Worker count | `budget.max_workers`, default **4** | tunable per-run, lives with the rest of the governor. Absent key → getter defaults to 4 (back-compat for the already-committed `state.json`). |
| Parallelized | search **and** ingest (per topic) | both run inside each topic worker. The graph step stays serial. |
| Graph | unchanged — serial, next cycle's step 1 | workers only fetch + record corpus + set `graph.dirty`; the existing serial step-1 `graphify --update` + replay + event append drains it. Tier 1 never changes how the single global graph is written. |

## 3. Components

### 3.1 `state.py` — transaction lock + strict budget

- `locked_state(root)` — context manager. Opens (creating if absent) `.research/state.lock`,
  `flock(LOCK_EX)`, loads `state.json`, yields the dict, saves it under the lock, releases
  on exit (fd close). On a worker crash the OS drops the `flock` automatically — no stale lock.
- Every **mutating** CLI subcommand routes its load→mutate→save through `locked_state` instead
  of the current bare `load()` … `save()`. Read-only subcommands (`list-gaps`, `budget-status`,
  `budget-remaining`, `next-gap`, `candidates`) need no lock.
- `budget_reserve(state, n) -> granted`: `granted = min(n, remaining)`; `spent.sources += granted`;
  return `granted`. This is the atomic reservation primitive. CLI: `budget-reserve --sources N`
  (prints `granted`).
- `budget_refund(state, n)`: `spent.sources = max(0, spent.sources - n)`. CLI: `budget-refund --sources N`.
- `budget_spend_source` and its CLI stay (raw increment, used by tests); `search_flow` no longer
  calls it.
- `load_default()` budget block gains `"max_workers": 4`. Getter usage is `budget.get("max_workers", 4)`
  everywhere so an older on-disk state still works.
- `budget-status` output gains `max_workers` so the driver can read it.

### 3.2 `search_flow.sh` — reserve-before-fetch + `--inbox`

- New optional `--inbox DIR` (default `$ROOT/ingest`); drops kept markdown into `$INBOX/...`.
- Per gap: reserve up front — `granted=$($SP budget-reserve --sources "$PER_GAP")`; if `granted -le 0`
  break. Fetch at most `granted` URLs, junk-filter, keep `K ≤ granted`. After the gap, refund the
  remainder — `$SP budget-refund --sources $((granted - K))` (no-op when `K == granted`).
- The top-of-file single `budget-remaining` read (current line 21) is replaced by the per-gap
  reservation; the local `remaining` accumulator is removed (it was the race).
- Gap status transitions (`done` / requeue / `failed` after 3) and run-log records are unchanged
  in meaning; they now mutate state under the lock via the same CLI.

### 3.3 `ingest_flow.sh` — `--inbox`

- New optional second arg `--inbox DIR` (default `$ROOT/ingest`). Drains `$INBOX/*`, with
  `_done/` and `_failed/` resolved under `$INBOX`. Routing to `docs/<topic>/sources/` is unchanged.

### 3.4 `.claude/goal.md` step 3 — parallel driver

Replace the sequential `for T in …` loop with a worker pool sharded by topic:

```
W=$(python3 scripts/state.py budget-status | python3 -c 'import json,sys;print(json.load(sys.stdin)["max_workers"])')
python3 scripts/state.py list-gaps --status queued | cut -f2 | sort -u | \
  xargs -P "$W" -I{} bash -c '
    T="{}"; IN="ingest/.work/$T"; mkdir -p "$IN"
    bash scripts/search_flow.sh --topic "$T" --inbox "$IN"
    bash scripts/ingest_flow.sh "$T" --inbox "$IN"
  '
```

Each topic's fetches are isolated in `ingest/.work/<topic>/`, so parallel `ingest_flow`s never
share files or mis-route. `ingest/.work/` is git-ignored and emptied by each worker's own drain.
Human flat-drops into `ingest/` remain handled by the serial cycle step 1, unchanged.

## 4. Data flow

```
N topic workers (xargs -P max_workers), each:
  reserve budget ── fetch ── junk-filter ── refund unused      [network, no lock held]
        │                                                        (reserve/refund are brief locked ops)
        └── drop kept .md → ingest/.work/<topic>/
            ingest_flow <topic> --inbox ingest/.work/<topic>/
                └── normalize, add_corpus_entry (locked), set graph.dirty
  ─────────────────────── join ───────────────────────
next cycle step 1 (serial, one writer):
  graphify --update ── assertions replay ── graph_events append ── clear dirty
```

## 5. Error handling

- Worker crash mid-fetch: `flock` auto-released by OS; reserved-but-unspent budget is **not**
  auto-refunded (the reservation stands), so a crashed worker only under-utilizes the budget —
  never overspends. The reservation is cleared by the next `budget-reset`, which is **manual
  today** (the loop does not auto-reset — see README); since the engine treats the budget as a
  standing cap, a leaked reservation only lowers throughput until the next reset. Acceptable;
  auto-refund is a Tier-2 refinement.
- One topic worker failing does not abort the pool (`xargs` continues other topics; `search_flow`
  keeps `set -uo pipefail`, not `-e`).
- Torn read of `state.json` is impossible for writers (they hold the lock); read-only commands
  tolerate a torn read by the existing atomic-replace guarantee (a reader sees either the old or
  new whole file, never a partial — `os.replace` is atomic).

## 6. Testing (stdlib `unittest` + bash, no pip)

- `locked_state` lost-update: spawn **N subprocesses** (not threads — `flock` is per open-file-
  description / per process), each appending a distinct gap via the CLI; assert all N survive in
  the final state. Without the lock this loses updates; with it, none.
- `budget_reserve` strictness: from `remaining=R`, run M>R concurrent `budget-reserve --sources 1`
  subprocesses; assert total granted == R and `spent.sources` never exceeds `sources_per_cycle`.
- `budget_refund` clamps at 0; reserve-then-refund round-trips to the original `spent`.
- `max_workers`: present in `load_default`; getter defaults to 4 when the key is absent.
- bash smoke: two topics with queued gaps, `max_workers=2`, scoped inboxes; assert each topic's
  sources land only under its own `docs/<topic>/sources/` (no cross-routing) and the budget total
  is respected.

## 7. Non-goals (Tier 2)

Per-gap workers and atomic gap-claim (unnecessary at topic grain); multiple concurrent `/goal`
loops; parallel graph writes; auto-refund of a crashed worker's reservation; dynamic worker
autoscaling.
