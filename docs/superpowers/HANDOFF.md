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

## Current state (HEAD `06ca23c`; working tree clean modulo `public/dashboard.html`)
- **13 promoted findings / 3 rejected.** Corpus **98**. Graph **1436 nodes / 1364 links**
  (`dirty:false`). **38 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`.
- **10 of 17 domains grounded** (have a primary-sourced promoted finding):
  01 epistemics, 02 statistical-causal, 03 decision-frameworks, 05 deep-research (2),
  06 rag-retrieval (2), 07 agentic-orchestration (2), 08 grounding-truth,
  09 knowledge-graphs, 16 evaluation-benchmarks, 17 specs-standards.
  **The methodology/rigor half (01/02/03) is now grounded** — the largest former blocker.
- **7 domains still empty/thin** (the remaining gap to "definitive"):
  04 applied-playbooks, 10 context-prompt-eng, 11 pipeline-eng, 12 tooling-landscape,
  13 reference-systems, 14 papers, 15 textbooks. These are the applied/tooling/case-study
  layer — the "how others built it" and "what to actually run" half.

## Working tree (clean at handoff)
All research work is committed through `06ca23c`. Outstanding, NOT to be touched/committed:
- `public/dashboard.html` — modified separately in the user's IDE, not part of research work.
- Noise, never commit: `.research/*.log`, `graphify-out/`. `.graphify/graph.json` is
  gitignored (rebuildable from corpus + assertion overlay).

Two SYNTHESIS files, two owners (don't merge them): `docs/findings/SYNTHESIS.md` = flat
auto-index (`promote.py` appends a line per promote — leave to the script); root
`SYNTHESIS.md` = human cross-domain distillation, re-grounded against the 8 findings with
a "Not yet grounded" section. Re-run the re-ground pass after new findings land.

Commit recipe for new work: stage explicitly (never `git add .`/`-A`), Conventional
Commit `chore(research): …`, no co-author trailer.

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
Verified against HEAD `06ca23c` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (13/3 findings, corpus 98, 38 assertions, 10 grounded domains, graph 1436/1364)
read live from state.json + graph.json; the graphify `--update` recipe below is the exact
flow run this session (detect→AST→cache→2 extraction subagents→build_merge→to_json→replay).
Design specs live in `docs/superpowers/specs/` (6 files; umbrella
`2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE (committed through `06ca23c`):
- **Methodology cluster (01/02/03) grounded** (`ecd3a60`): 9 human gaps → search-drain →
  graphify fold → 3 promoted findings (02 Pearl/Rubin causal; 01 GRADE/PRISMA/Cochrane +
  claim-extraction/NLI + calibration; 03 ACH + weighted-criteria MCDM). 8 assertions.
- **05/07 backlog deepened, 06 backlog rejected** (`06ca23c`): 05 "benchmark-accuracy is
  the only cross-vendor comparable"; 07 "the head-to-head that isn't"; 06 draft rejected
  for citing an AI-aggregator (emergentmind) as if arXiv — the provenance gate held.
- Root `SYNTHESIS.md` re-grounded twice (13 findings / 10 domains; added the
  provenance-tiering meta-finding).

**THE NEXT STEP — seed + ground the applied/tooling half (start 12 + 13).** The engine
can now defend its architecture, eval, interop, AND epistemic credibility, but not yet
"how others built it / what to actually run." Do one full gather→fold→process arc per
domain (same recipe as the methodology cluster):
1. **Add gaps** (`state.py add-gap --origin human`), ~3 per domain:
   - 12 tooling-landscape: LangGraph vs LlamaIndex vs DSPy vs AutoGen (orchestration model,
     not marketing); when to use a framework vs raw SDK; observability/tracing tooling.
   - 13 reference-systems: STORM / GPT-Researcher / open-source deep-research architectures
     (two-stage research-then-write, multi-perspective sub-questioning) from their papers/repos.
2. **Search-drain** per-topic (`budget-reset` before each), background.
3. **Ingest+graph** (stage per-topic inbox → `ingest_flow --inbox` → `rm -rf .research/inbox-*`
   → graphify `--update` → replay → integrity).
4. **Process** each into a finding (drafter → verify → reviewer). **Provenance is the live
   reject axis** — tooling/framework material is heavily vendor-marketed; anchor load-bearing
   claims to source repos/official docs/papers, attribute blog claims. Two 06 rejects this
   corpus prove the gate punishes aggregator-as-primary; tell the drafter to verify each
   source_url's real publisher and label primary vs aggregator/blog (the 07 finding is the
   model of an honest provenance-tiered result).

Also pending / lower-priority:
- **Re-assert 07's cross-links after the next fold.** `df8e7fa14`'s own graph node didn't
  exist yet when it was drafted, so its 3 proposed assertions (→ `d5c35de17` halt-decision,
  → `findings_07_multiagent_15x_cost`, → `concept_halt_decision_axis`) were skipped. After
  the next graphify `--update` the node `findings_df8e7fa14_*` will exist — add them then.
- **06 still wants the real arXiv ColBERT primaries** (2004.12832, 2112.01488) — a gap is
  queued; a clean redraft of the late-interaction-economics angle needs them, not aggregators.
- Empty domains remaining after 12/13: 04 applied-playbooks, 10 context-prompt-eng,
  11 pipeline-eng, 14 papers, 15 textbooks.

**Definitive bar:** grounded technical engine (05-09) + eval (16) + standards (17) +
methodology (01/02/03) are DONE. NOT yet "definitive" until the applied/tooling/case-study
half (12, 13, then 04/10/11/14/15) is grounded and SYNTHESIS's "Not yet grounded" shrinks
to genuinely-unresearched corners (currently: A/B power for 02, MADR record-format for 03,
STORM/GPT-Researcher for 13, cost-tiered prompting for 10, plus 11/12/14/15).
