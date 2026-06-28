# Handoff — open-research-system: PLANNER + PACKAGING phase

Paste into a fresh session to continue. Self-contained. This phase makes the engine a
**reusable, one-prompt research tool that runs inside any project**. It is distinct from the
earlier research-corpus work (see `docs/superpowers/HANDOFF.md` / `HANDOFF-SYNTHESIS.md` for
that history — do not re-derive it).

## Where we are

Repo: `/Users/joshua/Documents/GitHub/open-research-system`, branch `main`. `python3`, not
`python`. Verify live: `python3 -m unittest discover -s tests -p 'test_*.py'` (expect **164 OK**),
the 4 shell smokes (`bash tests/test_research_flow.sh` / `test_goal_loop_wiring.sh` /
`test_planner_e2e.sh` / `test_report_flow.sh` → all PASS), and `python3 scripts/check_integrity.py`
→ `integrity OK`. HEAD ≈ `81897cc` or later.

**Sub-project A — "The Planner" — DONE and merged to main** (merge commit `151b165`, 20 TDD
commits, fresh-implementer + independent-reviewer per task, one final whole-branch review).
It adds, on top of the existing `/goal` autonomous loop + deterministic `orchestrator.py`:
- **One-prompt bootstrap** — `.claude/research.md` (`/research "<prompt>" [--budget N] [--root D]`):
  classify research shape (comparison/survey/causal/how-to/chronology) → emit a plan JSON →
  `scripts/plan.py apply` validates it (invalid plan halts pre-launch), writes machine-readable
  `goal`+`plan` into `state.json`, seeds the gap queue, inits the run budget → hands off to `/goal`.
- **Dimension-discovery control loop** (`scripts/dimension_gate.py` + `orchestrator.accept_eligible`
  + `state.py` helpers): mid-run, the process flow emits **dimension candidates**; corroboration
  accumulates across cycles; a streaming-multiple-testing α-wealth gate accepts/rejects (4 axes:
  goal-relevance, corroboration≥K, distinctness, comparability). Accepted dims seed gaps and
  self-extend the plan. Converges by construction (α-wealth cap + accept-seeds-gaps keeps the loop
  in `deepen` until researched).
- **Total-run token metering** (`scripts/meter.py`) → `budget.run.tokens_spent` →
  `orchestrator.decide` emits `budget_exhausted` + `stop`. Run stops on plateau OR budget OR cycle-cap.
- **On-demand report** — `.claude/report.md` (`/report`): narrative from `goal`+`plan`+findings.
- **Integrity** validates `plan.candidate_dimensions` cites resolve to corpus.

Key files: NEW `scripts/plan.py`, `scripts/meter.py`, `scripts/dimension_gate.py`,
`.claude/research.md`, `.claude/report.md`; MODIFIED `scripts/state.py`, `scripts/orchestrator.py`,
`scripts/check_integrity.py`, `.claude/goal.md`, `.claude/process.md`. Design spec:
`docs/superpowers/specs/2026-06-28-planner-bootstrap-design.md`. Plan:
`docs/superpowers/plans/2026-06-28-planner-bootstrap.md`. SDD progress ledger (gitignored):
`.superpowers/sdd/progress.md`.

## NOT done — two remaining gaps (this is the work)

**The headline goal — "use ORS from another project to research that project" — is NOT yet possible.**

### Gap 1 — A has never had a real live run (validate before trusting it)
All of A is unit/smoke-tested; the tests **stub the flows**. No actual `/research "..."` → autonomous
loop → real cited findings run has executed. Before building anything else, do ONE cheap live run
**inside the ORS repo** to validate the whole chain end-to-end and fix whatever the real flow breaks:
- Pick a small throwaway question + a small `--budget` (e.g. a few hundred k tokens).
- Run the `.claude/research.md` flow, then the `/goal` loop, watch: plan written to `state.json`,
  gaps seeded, search/ingest/process/review actually fire, dimension candidates emitted + gated,
  `meter.py` updates `budget.run`, `decide` stops on plateau/budget. Set `CLAUDE_TRANSCRIPT_PATH`
  so metering is real, not the estimate fallback (else token budget is approximate).
- Expect rough edges — the flows were never executed, only grep-checked. Treat failures as real
  bugs to fix in A.

### Gap 2 — Sub-project B "The Package" (portability/distribution) — UNBUILT
This is what makes ORS usable from another project. Was deliberately deferred; A was built
**root-aware on purpose** so B is mostly *extraction, not rework*. B must:
1. **Full root-awareness.** `state.py`/`orchestrator.py`/`plan.py`/`meter.py`/`dimension_gate.py`
   already take `--root`. STILL cwd-bound (need fixing): the shell flows (`scripts/gather.sh`,
   `scripts/search_flow.sh`, `scripts/ingest_flow.sh`, `scripts/ingest_flow.sh`), the graphify skill
   invocation, and the `.claude/*.md` flows that call `python3 scripts/X.py` (ORS-relative). Engine
   code lives in ORS; research artifacts must land in the **target** project (`<target>/.research`,
   `<target>/docs`, `<target>/.graphify`).
2. **Packaging.** `/research` + `/report` are `.claude/*.md` agent procedures in the ORS repo today —
   not invocable from another project. Package ORS as a Claude Code plugin/skill so `/research` works
   from any repo. **Read `~/.claude/SKILLS-AND-PLUGINS-GUIDE.md` first** (per the user's global
   CLAUDE.md, it is the canonical skill-vs-plugin decision framework + authoring bar).
3. **Portable dashboard.** `graph_view_server.py` + `public/dashboard.html` serve ORS-local paths;
   make the realtime graph UI run against the target project's `.graphify`/state.
4. **Metering wiring.** Ensure whatever launches a run sets `CLAUDE_TRANSCRIPT_PATH` (or an
   equivalent), so the run budget is metered, not estimated.

## How to proceed (use the superpowers workflow — the user runs subagent-driven)

1. **First: validate A live** (Gap 1). If it surfaces bugs in A, fix them in main (small commits,
   tests, the repo's discipline) before B.
2. **Then: brainstorm → spec → plan → build B.** Invoke `superpowers:brainstorming` for B (the user
   expects the brainstorm→writing-plans→subagent-driven-development flow used for A). Decompose B if
   it's still too big (e.g. root-awareness refactor vs packaging vs portable-dashboard as separate
   specs). One spec → one plan → SDD execution each.

## Hard rules (do not relax)
- `python3` only. stdlib-only in engine scripts (no new deps without cause). New `state.json` blocks
  stay additive, read via `.get()`, never added to `check_integrity.REQUIRED_KEYS`, `DEFAULT_STATE`
  unmodified; backward-compat is load-bearing (verified airtight in A).
- **Protected files — never stage/commit unless the user explicitly says so:** `public/dashboard.html`
  is the user's file (they have committed it once explicitly; still treat as theirs). `.research/*.log`
  is now gitignored. `.graphify/` and `graphify-out/`-style generated output stay out of git.
- Commits: explicit staging (never `git add .` / `-A`), Conventional Commits, **no co-author trailer**,
  small/scoped. Branch off main for B (don't implement on main without consent); no git worktrees
  (CLAUDE.md override — use a branch or dev container).
- TDD per task; independent reviewer per task; one final whole-branch review (most-capable model);
  `check_integrity.py` green before claiming done.

## Quick orientation commands
```
python3 -m unittest discover -s tests -p 'test_*.py'      # 164 OK
for t in research_flow goal_loop_wiring planner_e2e report_flow; do bash tests/test_$t.sh; done
python3 scripts/check_integrity.py                         # integrity OK
sed -n '1,60p' docs/superpowers/specs/2026-06-28-planner-bootstrap-design.md
cat .superpowers/sdd/progress.md                           # SDD ledger (what landed, review notes)
```
