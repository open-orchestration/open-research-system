# Handoff — open-research-system (operating the research engine)

Paste into a fresh session to continue. Self-contained. The engine is BUILT and
RUNNING; this handoff is about *operating* it (gather → process → synthesize),
not building more of it.

## What this is
`open-research-system` (`/Users/joshua/Documents/GitHub/open-research-system`, branch `main`)
is an autonomous, loop-driven research engine. Goal: compile a primary-sourced,
citation-gated knowledge base across 17 research domains (`docs/NN-*/`) good enough to
synthesize "the definitive research system." Three flows coordinate through one on-disk
ledger — **`.research/state.json`** ("the agent forgets, the repo remembers"):
- **search** (`scripts/search_flow.sh`) — drains queued gaps → crawl4ai search+fetch →
  junk-filter → drops `.md` into `ingest/`.
- **ingest+graph** (`scripts/ingest_flow.sh` + the **graphify** skill) — normalizes
  sources into `docs/<topic>/sources/` with durable content-hash ids, records corpus,
  folds into the knowledge graph.
- **process** (`.claude/process.md`) — turns corpus into findings, human-free promotion
  via an **independent AI reviewer** (`.claude/review.md`).
The convergence orchestrator (`scripts/orchestrator.py`) decides phase
(`gather`/`deepen`/`synthesize`) as a stateless function of state signals.

## Current state (HEAD `44bfc7d`; root SYNTHESIS.md re-grounded, uncommitted)
- **8 promoted findings / 2 rejected.** Corpus **79**. Graph **1360 nodes / 1249 links**
  (`dirty:false`). **24 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`. 30 gaps done, **23 queued**.
- **7 of 17 domains grounded** (have a primary-sourced promoted finding):
  05 deep-research, 06 rag-retrieval (2 findings), 07 agentic-orchestration,
  08 grounding-truth, 09 knowledge-graphs, 16 evaluation-benchmarks, 17 specs-standards.
- **10 domains still empty/thin** (the gap to "definitive"):
  01 epistemics (2 corpus), 02 statistical-causal (0), 03 decision-frameworks (4, no
  finding), 04 applied-playbooks (0), 10 context-prompt-eng (0), 11 pipeline-eng (0),
  12 tooling-landscape (0), 13 reference-systems (0), 14 papers (0), 15 textbooks (0).
  The **research-methodology half (01/02/03)** is the biggest hole — it's what makes
  outputs rigorous vs merely retrieved.

## UNCOMMITTED right now (commit first thing)
- **`SYNTHESIS.md`** (repo root) — re-grounded against the 8 promoted findings: cites
  only real findings, quarantines un-evidenced claims under "Not yet grounded", refreshes
  stale graph numbers. Commit: `docs(research): re-ground root SYNTHESIS against the 8 promoted findings`.
- NOT mine, leave alone: `public/dashboard.html` (modified separately in the user's IDE).
- Noise, never commit: `.research/*.log`, `graphify-out/`. `.graphify/graph.json` is
  gitignored (rebuildable from corpus + assertion overlay).
- Two SYNTHESIS files, two owners: `docs/findings/SYNTHESIS.md` = flat auto-index
  (`promote.py` appends to it — leave to the script); root `SYNTHESIS.md` = human
  cross-domain distillation (the one just re-grounded). Don't merge them.
Commit recipe: stage explicitly (never `git add .`/`-A`), Conventional Commit, no
co-author trailer.

## How to run each operation (verified working this session)

### Search-drain queued gaps (network; run in background)
Per-topic, reset budget before each topic so each gets a fresh 8-source grant
(`sources_per_cycle=8`, `PER_GAP=5` reserve → a 2-gap topic splits 5+3):
```
for t in <topic1> <topic2>; do
  python3 scripts/state.py budget-reset --root .
  bash scripts/search_flow.sh --topic "$t"
done
```
Gaps with ≥1 non-junk source flip `done`; dry gaps requeue (fail after 3 attempts).

### Ingest staged sources (sources land in `ingest/`, span topics)
`ingest_flow.sh` drains the WHOLE inbox under one topic, so route per-topic via staged
inboxes (filenames are `<gapid>-<slug>-N.md`; map gap→topic from state):
```
# stage: move each ingest/*.md into .research/inbox-<topic>/ by its gap-id->topic
for t in <topics>; do bash scripts/ingest_flow.sh "$t" --inbox ".research/inbox-$t"; done
rm -rf .research/inbox-*    # ingest_flow leaves _done dups inside the inbox — delete them
```
This sets `graph.dirty=true`.

### Fold into the graph (graphify `--update`, the LLM step)
`cp .graphify/graph.json .graphify/.graphify_old.json` first. Then run the graphify skill's
`--update` flow (see `~/.claude/skills/graphify/references/update.md`): detect_incremental →
populate `.graphify_detect.json` (`files`=changed, `all_files`=full) → AST → cache-check →
chunk uncached (~22/chunk) → dispatch `general-purpose` extraction subagents (verbatim
prompt from `references/extraction-spec.md`, write to `.graphify/.graphify_chunk_NN.json`)
→ merge → `build_merge(prune_sources=changed)` → `save_manifest` → build/cluster → `to_json`.
Then the **loop tail** (`.claude/loop.md` steps 3-6):
```
python3 scripts/assertions.py replay   # re-merge overlay as _origin:asserted (idempotent)
python3 scripts/graph_events.py append --old .graphify/.graphify_old.json --new .graphify/graph.json --events .research/graph-events.jsonl
python3 scripts/state.py set-graph --dirty false --node-count <N> --edge-count <E>
python3 scripts/check_integrity.py     # must pass
```
Skip community labeling (cosmetic; the engine consumes graph.json directly). Clean up
`.graphify/.graphify_*` temp + `.graphify_old.json` after.

### Process cycle (one topic → one finding)
1. `python3 scripts/state.py candidates` → top topic T (needs ≥3 uncited corpus).
2. Get T's uncited sources (id→`extracted_path`), dispatch a `general-purpose` DRAFTER
   subagent: read sources + existing finding, frame 3-5 sub-questions, write
   `docs/findings/_drafts/<id>-<slug>.md` (id from `state.py gen-id d "T|title"`,
   `status: draft` header, every claim an inline `[c<id>]` citation), pass
   `cite_check.py`, do a faithfulness self-check, RETURN id/title/cites/gaps/assertions.
3. Verify yourself: re-run `cite_check.py`; confirm each assertion node-id exists in
   `graph.json` and relation ∈ {bridges,supports,contradicts,refines}.
4. `state.py add-draft …`; `add-gap … --origin process` for each; `assertions.py add …`;
   `check_integrity.py`.
5. Dispatch a FRESH `general-purpose` REVIEWER subagent (rubric verbatim from
   `.claude/review.md`, never the drafter's context). Parse last line
   `VERDICT: promote|reject`. `promote.py promote <id>` or
   `promote.py reject <id> --reason "ai-independent: …"`. Log each step via `runlog.py`.
   Run `check_integrity.py` after.

## Gotchas learned this session (don't relearn the hard way)
- **Provenance is the reject axis.** cite_check only proves a cited id exists; the AI
  reviewer rejects findings whose LOAD-BEARING claims rest on marketing/SEO/vendor blogs
  even when faithful (this killed the first 06 draft). Anchor the thesis to primary
  papers/official docs; attribute blog claims "X describes…" and keep them non-load-bearing.
  A rejected draft frees its sources + emits gaps → search hunts better sources → redraft
  on a narrower, defensible angle (this is how 06 was later promoted).
- **Assertion `--from`/`--to` are GRAPH node ids** (`nodes[].id` in `.graphify/graph.json`),
  NEVER `c…` corpus ids (those go in `--cites`). `relation` is EXACTLY one of
  bridges|supports|contradicts|refines. Drafters got both wrong twice — `.claude/process.md`
  step 7 now spells this out; verify against graph.json before `assertions.py add` or
  integrity fails on phantom nodes.
- **graphify manifest staleness balloons `--update`.** If the manifest is stale,
  detect_incremental reports hundreds of "changed" files. `save_manifest` after every
  reconcile keeps the next update small (this session: 315-file balloon once, then
  ~18-31 files per pass).
- **Inbox staging leaves `_done` dups.** `ingest_flow --inbox` moves processed files to
  `<inbox>/_done` — `rm -rf .research/inbox-*` after, or graphify re-extracts byte-identical
  dups under different node ids.
- **Assertions survive rejection and graph rebuilds.** The overlay is append-only and
  committed; replay strips+re-merges every cycle, so graph.json can be deleted/rebuilt freely.

## Cross-check (this handoff vs the repo)
Verified against HEAD `44bfc7d` (+ uncommitted root SYNTHESIS.md re-ground): all cited scripts exist
(`search_flow.sh ingest_flow.sh orchestrator.py state.py assertions.py promote.py
cite_check.py check_integrity.py graph_events.py runlog.py`); `.claude/` has
`goal.md loop.md process.md review.md`; state numbers (8/2 findings, corpus 79, 24
assertions, 23 queued gaps, 7 grounded domains) read live from state.json; command
recipes are the exact invocations used to promote findings this session. One discrepancy
fixed: the prior HANDOFF.md described pre-#6 build state (branch `phase1-research-spike`,
"next = sub-project #6") — obsolete, overwritten by this file. Design specs live in
`docs/superpowers/specs/` (6 files; umbrella `2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session: committed the 8th/7th findings (`44bfc7d`); re-grounded root
`SYNTHESIS.md` (uncommitted — commit it first, see above).

**THE NEXT STEP — seed + ground the methodology cluster (01/02/03).** This is the
rigor half and the single biggest blocker to "definitive": the engine can currently
defend its architecture/eval/interop but not its *epistemic credibility*. Do it as one
full gather→fold→process arc, exactly like the 16/17 seed this session:
1. **Add gaps** (`state.py add-gap --origin human`), ~3 per domain:
   - 02 statistical-causal: Pearl DAGs/do-calculus/backdoor criterion; potential-outcomes
     & counterfactuals; statistical power / effect size / A-B test methodology.
   - 01 epistemics: source-credibility & evidence-synthesis (Cochrane/PRISMA, GRADE);
     claim extraction / cross-referencing / contradiction resolution.
   - 03 decision-frameworks: Analysis of Competing Hypotheses (ACH); MADR/decision-matrix
     for AI-assisted decisions.
2. **Search-drain** them (per-topic, `budget-reset` before each — see runbook above), in
   background.
3. **Ingest+graph** the landed sources (stage per-topic inbox → `ingest_flow --inbox` →
   `rm -rf .research/inbox-*` → graphify `--update` → replay → integrity).
4. **Process** each into a finding (drafter → verify → reviewer gate). Anchor claims to
   primary sources (Pearl, Cochrane, the ACH literature) — these domains have real
   primary literature, so provenance should be easy to satisfy.

Then: process the existing backlog (no new search — 05:11 uncited, 06:8, 07:8, 03:4),
and seed 12 tooling-landscape + 13 reference-systems. After 01/02/03 land, re-run the
re-grounding pass on `SYNTHESIS.md` (move the now-grounded methodology claims out of
"Not yet grounded").

**Definitive bar:** grounded technical engine (05-09) + eval (16) + standards (17) are
done. NOT yet "definitive" until the methodology half (01/02/03) is grounded and the
"Not yet grounded" section of SYNTHESIS has shrunk to genuinely-unresearched corners.
