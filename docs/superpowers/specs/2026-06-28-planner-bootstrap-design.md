# Design — The Planner: one-prompt research bootstrap

**Date:** 2026-06-28
**Status:** approved design, pre-implementation
**Sub-project:** A of 2 (A = Planner / bootstrap brain; B = portability / packaging, specced later)

## Goal

Turn a single natural-language prompt — e.g. *"use the open-research-system to research
the Boeing 777 and Airbus A380 to build an in-depth comparison"* — into a fully autonomous
research run that decomposes the question, researches it across many dimensions until
plateau or budget exhaustion, and leaves behind a cited set of findings a report can be
generated from. No human steps after the prompt.

## What already exists (do not rebuild)

The autonomy core is already built and stays untouched in structure:

- **Autonomous multi-cycle loop** — `/goal` (`.claude/goal.md`) runs cycles until
  `orchestrator.py decide` reports `goal_met`, or a cycle cap fires.
- **Deterministic phase machine** — `orchestrator.py` (pure stateless math over
  `state.json`): gather → deepen → synthesize, self-correcting.
- **Budget model** — per-cycle `tokens_per_cycle`, `sources_per_cycle`, `max_subagents`,
  `max_workers`, per-phase flow weights.
- **Four flows** — search / ingest / process / review (`.claude/*.md`), all gates
  (cite_check + faithfulness self-check + independent reviewer + graded promotion).
- **Realtime graph UI** — `graph_view_server.py` + `public/dashboard.html` + live deltas.
- **Partial path-rooting** — `state.py load(root)` and `orchestrator --root` already take a
  root; new artifacts must follow suit so Sub-project B is *extraction, not rework*.

## What this sub-project adds (the real work)

1. A **Planner** that decomposes one prompt into a machine-readable research plan and
   launches the existing loop.
2. A **machine-readable goal/plan** in `state.json` (the engine currently has no record of
   *what* it is researching).
3. A **dimension-discovery control loop** so the plan self-extends as new comparison
   dimensions are discovered mid-run, while still converging.
4. **Total-run token metering + stop logic** (the per-cycle budget is not a run ceiling).
5. An **on-demand report assembler** (`/report`) that builds a narrative doc from findings.

## Decisions (from brainstorming)

- **Plan shape:** auto-detected per prompt (comparison / survey / causal / how-to /
  chronology). Comparison → entities × dimensions; survey → topic taxonomy.
- **Autonomy:** fully autonomous after the prompt — no human approval gate. Budget is the
  only guardrail; plan validation is the only pre-launch halt.
- **Budget unit:** tokens per run. Primary stop is plateau; secondary is the token ceiling;
  cycle cap is the backstop.
- **Deliverable:** cited findings + the filled plan structure (matrix data); a separate
  `/report` command assembles a narrative doc on demand (not auto-generated at run end).

## Approach (chosen)

**Skill + thin planner script.** A `/research` skill performs the LLM decomposition and
emits a plan JSON; a pure-code `scripts/plan.py` validates it, writes `goal` + `plan` into
`state.json`, seeds the gap queue, initializes the run budget, then hands off to the
**unchanged** `/goal` loop. Rejected alternatives: a pure-Python planner (decomposition is
inherently semantic — fights the engine's LLM-flow grain) and folding planning into
`orchestrator.py` (would inject an LLM step into the deterministic, verifiable orchestrator
and destroy that property).

## §1 — Components & data flow

```
/research "777 vs A380 comparison" --budget 2M
   │
   ▼
[Planner skill]  (LLM: classify shape → emit plan.json)
   │
   ▼
[scripts/plan.py]  (pure code: validate plan, write goal+plan into state.json,
   │                seed gap queue, init budget.run + budget.dimension_alpha)
   │   (invalid plan → HALT before launch — the only pre-launch stop)
   ▼
[/goal loop]  ← UNCHANGED orchestrator + flows, now budget-metered per cycle
   │  search → ingest → graphify → process(draft+gates) → review(promote)
   │  + plan-growth gate (§1.5) once per cycle
   │  each cycle: meter cumulative tokens; stop if plateau OR spent≥ceiling OR cycle-cap
   ▼
plateau → docs/findings/*.md (cited) + plan.json matrix filled with finding refs
   │
   ▼  (later, on demand)
[/report]  → comparison-report.md (narrative + tables + citations)
```

New `state.json` blocks (all written through `--root`):

- `goal`: `{question, shape, created_at}` — the machine-readable "what am I researching";
  feeds dimension relevance scoring and the synthesize framing.
- `plan`: `{entities[], dimensions[], topics[], candidate_dimensions[], rejected_dimensions[]}`
  — the matrix/taxonomy; each accepted dimension/topic links the findings that fill it.
- `budget.run`: `{token_ceiling, tokens_spent, started_at}` — total-run metering alongside
  the existing per-cycle budget.
- `budget.dimension_alpha`: `{wealth, spent}` — the α-budget governing plan growth (§1.5).

## §1.5 — Dimension-discovery control loop

**Principle:** accepting a new dimension is a streaming-multiple-testing problem — the same
discipline the engine already applies to promotion. Grounded in the corpus's own findings:
online-FDR / LORD alpha-investing (`d42ec736c`) and always-valid sequential inference
(`dc588b7cc`). Each candidate dimension is a "test"; the false-acceptance rate is controlled
across the stream so the plan grows yet still converges.

```
each cycle:
  process/ingest flows read sources → emit DIMENSION CANDIDATES (not just gaps)
        ▼
  plan-growth gate (one batched step/cycle):
    merge candidates into plan.candidate_dimensions, accumulating INDEPENDENT
    evidence across cycles
        ▼
    score each pending candidate on 4 axes:
      1 goal-relevance  — LLM judges candidate vs stored goal.question
      2 corroboration   — ≥ K independent sources raise it (the load-bearing auto-signal)
      3 distinctness    — not a duplicate / sub-facet of an existing dimension
      4 comparability   — (comparison shape) BOTH entities are scoreable on it
        ▼
    accept (all pass + α-wealth>0 + run-budget headroom):
        add to plan.dimensions, spend α-wealth, seed gaps (entity × new dim), log
    reject (fails an axis, OR pending > TTL cycles with no new corroboration):
        move to plan.rejected_dimensions (never re-proposed), log
    else: stays pending (accumulating corroboration)
        ▼
  new gaps flow into the SAME loop → search→ingest→process→findings → fill new matrix cells
```

**Convergence guarantees (what makes hands-off safe):**

- **α-wealth tightening** (LORD alpha-investing, `d42ec736c`): accepting spends wealth; the
  corroboration bar rises as wealth depletes. Early run accepts readily; late run demands
  overwhelming evidence. The candidate stream dries up by construction.
- **Run-budget headroom:** a candidate whose gaps cannot be funded within the remaining
  token ceiling is rejected — no half-researched columns.
- **Rejected set:** rejected dimensions are recorded and never re-proposed (idempotent).
- **Extended `goal_met`:** plateau now additionally requires *no accept-eligible candidates*
  and *no acceptance for K cycles* (dimension-stability), on top of the existing
  "no queued gaps / no processable / drafts done."

**Candidate record:**
```
plan.candidate_dimensions[] = {
  name, first_seen_cycle, last_seen_cycle,
  evidence_cites: [c…],   # deduped → independent-source count = corroboration
  corroboration: int,
  status: "pending"
}
```

The gate runs once per cycle inside the `/goal` loop (batched, for token efficiency and so
corroboration is counted across the accumulated pool, not per-proposal).

**Tunable defaults** (config in `state.json`, overridable per run):
- corroboration threshold `K` = **3** independent sources (the base bar before α-tightening).
- pending TTL = **3** cycles with no new corroboration → reject.
- dimension α-wealth initial = a small fraction of nominal capacity, e.g. **5** "free"
  accepts of credit, spent down per acceptance (the bar rises as it depletes).
- cycle cap = **25** (reuse the existing `/goal` backstop, `K >= 25` in `goal.md`).
These are starting values to be calibrated during implementation against a real run, not
load-bearing constants.

## §2 — Planner decomposition contract

The single LLM step, with a strict schema so `plan.py` validates deterministically.

```
INPUT:  { question: str, budget_tokens: int, root: str }
OUTPUT (plan.json — emitted by the LLM):
{
  shape: "comparison" | "survey" | "causal" | "how-to" | "chronology",
  entities:   [str],              # comparison/causal; [] otherwise
  dimensions: [ {name, why} ],    # comparison/causal axes
  topics:     [ {name, why} ],    # survey/how-to/chronology
  seed_gaps:  [ {topic, desc} ],  # the initial queue
  rationale:  str
}
```

- **Shape classifier first:** the LLM picks the shape, which determines whether `dimensions`
  or `topics` is populated. Unknown shape falls back to `survey`.
- **Seed-gap generation:** comparison → one gap per `entity × dimension` cell; survey → gaps
  per topic. Count capped from `budget_tokens` (no seeding 400 gaps on a 500k budget).
- **`plan.py` (pure code):** enum check, non-empty-by-shape, dedup names, cap counts; then
  write `goal` + `plan`, seed gaps, init `budget.run` + `budget.dimension_alpha`. Invalid
  plan → halt, do not launch.
- **Initial plan need not be perfect** — §1.5 self-extends it. Model-only decomposition (no
  upfront scoping search) keeps the plan cheap.

## §3 — Token metering & stop logic

Budget is the only guardrail, so this is load-bearing.

- **Metering source (primary):** `scripts/meter.py` reads the active Claude Code session
  transcript (the same source `ctx-stats` / `caveman-stats` parse) and sums output tokens
  since run-start, writing `budget.run.tokens_spent` each cycle.
- **Fallback:** if the transcript is unreachable, a conservative per-cycle estimate
  (subagents dispatched × average output) accumulated via `runlog`.
- **Backstop:** the existing cycle cap. The run is never unbounded.
- **Stop logic** — one check folded into `orchestrator.decide`, so `/goal` inherits it with
  no new control flow:
  ```
  stop when ANY:
    goal_met                              (plateau, incl. dimension-stability) ← primary
    run.tokens_spent ≥ run.token_ceiling                                       ← budget
    cycle K ≥ cap                                                              ← backstop
  ```
- On a non-plateau stop, finish the current cycle's gates cleanly (no half-promoted
  findings), then report it was cut short — "stopped on budget: N findings, M dimensions,
  P pending candidates" — distinct from a converged plateau.

## §4 — Report assembler (on demand)

`/report` (skill) reads `goal`, `plan` (filled matrix), and `docs/findings/*.md`, and writes
`docs/comparison-report.md`: a narrative with one section per dimension/topic, the comparison
matrix as a table, and citations resolved from the findings' `c…` ids. Deterministic and
regenerable; never part of the autonomous loop. Out of scope for the first implementation
plan if it grows the plan too large — it can be its own small follow-up plan.

## §5 — Error handling

- **Invalid plan** → halt before launch (the de-facto misread-prompt guardrail in
  fully-autonomous mode).
- **Flow failures** → reuse existing handling: gaps re-queued, failed-after-3-attempts,
  per-cycle integrity check halts a broken cycle.
- **Metering unavailable** → fall back to estimate → cycle-cap backstop.
- **Dimension thrash** → prevented by α-budget tightening + rejected-set + caps (§1.5).

## §6 — Testing

Stdlib asserts, the repo's existing `tests/` pattern — no frameworks, no fixtures.

- `plan.py`: each shape → correct structure + seed gaps; invalid plan rejected.
- dimension gate: accept / reject / pending transitions; corroboration accumulation across
  cycles; α-wealth tightening; pool-dries-up convergence.
- `meter.py`: transcript parse + fallback estimate.
- `orchestrator`: extend existing tests for the run-budget stop and dimension-stability in
  `goal_met`.
- end-to-end smoke: canned prompt + stubbed flows → reaches plateau.

## §7 — Portability constraints (for Sub-project B; honored now)

- Every new path goes through the existing `--root` parameter; no new cwd-hardcoded paths.
- `goal` / `plan` / `budget.run` live in `state.json` (already root-scoped), not in new
  top-level files.
- The `/research`, `/report` skills and `meter.py` must accept a target root so B can point
  the engine at another project's directory without rework.

## Out of scope (this sub-project)

- Packaging ORS as its own installable repo/tool and running against an external project
  directory (Sub-project B).
- Multi-model cost/dollar budgets (token budget only for now).
- An upfront scoping search to improve the initial plan (model-only decomposition; the
  dimension loop compensates).
