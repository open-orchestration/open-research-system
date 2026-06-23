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

## Current state (HEAD `8d9dbfd`; working tree clean modulo `public/dashboard.html`)
- **15 promoted findings / 3 rejected.** Corpus **111**. Graph **1521 nodes / 1482 links**
  (`dirty:false`). **43 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`.
- **12 of 17 domains grounded** (have a primary-sourced promoted finding):
  01 epistemics, 02 statistical-causal, 03 decision-frameworks, 05 deep-research (2),
  06 rag-retrieval (2), 07 agentic-orchestration (2), 08 grounding-truth,
  09 knowledge-graphs, 12 tooling-landscape, 13 reference-systems,
  16 evaluation-benchmarks, 17 specs-standards.
  **Methodology half (01/02/03) AND the tooling/reference-systems case studies (12/13)
  are now grounded.**
- **5 domains still empty/thin** (the remaining gap to "definitive"):
  04 applied-playbooks, 10 context-prompt-eng, 11 pipeline-eng, 14 papers, 15 textbooks.

## Working tree (clean at handoff)
All research work is committed through `8d9dbfd`. Outstanding, NOT to be touched/committed:
- `public/dashboard.html` — modified separately in the user's IDE, not part of research work.
- Noise, never commit: `.research/*.log`, `graphify-out/`. `.graphify/graph.json` is
  gitignored (rebuildable from corpus + assertion overlay).

Two SYNTHESIS files, two owners (don't merge them): `docs/findings/SYNTHESIS.md` = flat
auto-index (`promote.py` appends a line per promote — leave to the script); root
`SYNTHESIS.md` = human cross-domain distillation, re-grounded against the promoted findings
with a "Not yet grounded" section. Re-run the re-ground pass after new findings land.

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
Verified against HEAD `8d9dbfd` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (13/3 findings, corpus 98, 38 assertions, 10 grounded domains, graph 1436/1364)
read live from state.json + graph.json; the graphify `--update` recipe below is the exact
flow run this session (detect→AST→cache→2 extraction subagents→build_merge→to_json→replay).
Design specs live in `docs/superpowers/specs/` (6 files; umbrella
`2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE (committed through `8d9dbfd`):
- **Methodology cluster (01/02/03) grounded** (`ecd3a60`): 02 Pearl/Rubin causal; 01
  GRADE/PRISMA/Cochrane + claim-extraction/NLI + calibration; 03 ACH + weighted-criteria MCDM.
- **05/07 backlog deepened, 06 rejected** (`06ca23c`): 05 "benchmark-accuracy is the only
  cross-vendor comparable"; 07 "the head-to-head that isn't"; 06 draft rejected for citing
  an AI-aggregator (emergentmind) as if arXiv — the provenance gate held.
- **Applied/tooling half started — 12 + 13 grounded** (`8d9dbfd`): 12 agent-framework
  execution-model taxonomy (graph/state · query-engine · compile-time-optimizer ·
  conversation), framed as a durable axis not a ranking; 13 STORM (NAACL-paper-backed
  two-stage research-then-write, +25%/+10% on FreshWiki) + GPT-Researcher. 13's assertions
  ground the formerly-speculative synthesis nodes (two-stage, multi-perspective, tiering).
- Root `SYNTHESIS.md` re-grounded after each arc (now 15 findings / 12 domains).

**THE NEXT STEP — finish the applied half (04 / 10 / 11), then the literature spine (14/15).**
Same gather→fold→process arc each. Suggested gaps (`state.py add-gap --origin human`, ~3 each):
- 10 context-prompt-eng: prompting-technique ladder (few-shot → CoT → self-consistency → ToT)
  with when-each-wins evidence; context-window management / retrieval-augmented prompting;
  structured-output / JSON-schema prompting.
- 11 pipeline-eng: reproducible tracked runs (MLflow / experiment tracking); indexing-pipeline
  orchestration (incremental re-index, freshness); eval-in-CI for RAG/agent regressions.
- 04 applied-playbooks: end-to-end "build a deep-research agent" playbooks — blog-heavy domain,
  anchor to anything primary and attribute the rest.
- 14 papers / 15 textbooks: canonical papers (ReAct, Toolformer, Self-RAG, multi-agent surveys)
  + an IR textbook (Manning IR) — pure-primary domains, easy provenance.

**Provenance is THE live reject axis** (3 rejects, 2 on this exact failure): tell every drafter
to open each source, read its `source_url`, and label primary-paper/official-doc/repo vs
aggregator/blog/marketing — load-bearing claims must rest on primaries; blog claims are
attributed and non-load-bearing. The 07 and 13 findings are the model of an honest
provenance-tiered result; the 06 reject is the cautionary tale (aggregator dressed as arXiv).

Also pending / lower-priority:
- **Re-assert 07's cross-links.** `df8e7fa14`'s own graph node now exists after the 12/13 fold —
  add its 3 skipped assertions (→ `d5c35de17` halt-decision, → `findings_07_multiagent_15x_cost`,
  → `concept_halt_decision_axis`); verify exact node ids in `.graphify/graph.json` first.
- **06 still wants the real arXiv ColBERT primaries** (2004.12832, 2112.01488) — gap queued.
- **12 taxonomy + 13 GPT-Researcher internals want doc-anchoring** — gaps queued for official
  framework docs/repos (taxonomy is blog-convergent; only framework-vs-SDK is primary-anchored).
- **02 A/B-test power gap and 03 MADR-record-format gap** still queued (budget-skipped / dry).

**Definitive bar:** grounded technical engine (05-09) + eval (16) + standards (17) +
methodology (01/02/03) + tooling/reference-systems (12/13) are DONE. NOT yet "definitive"
until the remaining applied/literature domains (04/10/11/14/15) are grounded and SYNTHESIS's
"Not yet grounded" shrinks to genuinely-unresearched corners (currently: cost-tiered prompting
ladder for 10, pipeline-eng for 11, A/B power for 02, MADR record-format for 03, doc-anchoring
for 12/13, plus 04/14/15).
