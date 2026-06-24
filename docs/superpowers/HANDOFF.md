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

## Current state (HEAD `172379c`; working tree clean modulo `public/dashboard.html`)
- **21 promoted findings / 4 rejected.** Corpus **159**. Graph **1653 nodes / 1662 links**
  (`dirty:false`). **60 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`.
- **17 of 17 domains grounded** — the breadth bar is fully met. Every domain has ≥1 finding
  past the citation + faithfulness + independent-reviewer gates. Grounded: 01 epistemics,
  02 statistical-causal, 03 decision-frameworks, 04 applied-playbooks, 05 deep-research (2),
  06 rag-retrieval (2), 07 agentic-orchestration (2), 08 grounding-truth, 09 knowledge-graphs,
  10 context-prompt-eng (2), 11 pipeline-eng, 12 tooling-landscape, 13 reference-systems,
  14 papers, 15 textbooks-longform, 16 evaluation-benchmarks, 17 specs-standards.
- **No empty domains remain.** 15 was grounded this session on the actual IR-book chapter
  prose (d2fbbb962); 10 was upgraded blog→paper-anchored (d0b1fc5c6, the CoT/self-consistency/
  ToT originating papers); 07's head-to-head cross-links re-asserted. What's left is depth:
  narrow per-domain gaps that upgrade a blog-tier claim to primary (see Next steps).

## Working tree (clean at handoff)
All research work is committed through `ac8965d`. Outstanding, NOT to be touched/committed:
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
Verified against HEAD `ac8965d` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (13/3 findings, corpus 98, 38 assertions, 10 grounded domains, graph 1436/1364)
read live from state.json + graph.json; the graphify `--update` recipe below is the exact
flow run this session (detect→AST→cache→2 extraction subagents→build_merge→to_json→replay).
Design specs live in `docs/superpowers/specs/` (6 files; umbrella
`2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session (committed through `172379c`): **all 17 domains grounded.** The arcs:
methodology 01/02/03 (`ecd3a60`); 05/07 deepened + 06 reject (`06ca23c`); tooling/reference
12/13 (`8d9dbfd`); applied/literature 04/10/11/14 + 15 reject (`ac8965d`); **ground 15 on the
IR-book chapter prose (`d5bee4b`); re-assert 07's 3 head-to-head cross-links (`40782e0`);
paper-anchor the 10 prompting ladder (`172379c`).** Root `SYNTHESIS.md` re-grounded after each
(now 21 findings / 17 domains).

**Breadth is fully done; the last mile is the remaining narrow item-2 gaps.** Each upgrades a
blog-tier claim to primary on an *already-grounded* domain — small and self-contained, NOT a
full 17-domain sweep. The proven technique for primaries that the search engine keeps missing
(it lands on TOC/landing pages): bypass `search.py` and feed the **exact** URLs as `.url`
files (HTML chapters) or download the **PDF** into `ingest/` directly (arXiv papers) — ingest
records the real URL/file as provenance, then run the normal fold→draft→review→promote arc.
This is how 15 (IR-book `.url` chapters) and 10 (arXiv PDFs) were grounded this session.

Remaining queued gaps (pick whichever matters most):
- **06: real arXiv ColBERT primaries** (2004.12832 Khattab, 2112.01488 ColBERTv2/Santhanam) —
  enables a clean redraft of the rejected late-interaction-economics angle. 06 currently has
  the most uncited corpus; gaps `g1099431b`/`ga344680a`/`gade3c1ff` name these.
- **11: official ingestion-docs / CDC spec** for index-freshness (currently blog-only; gap
  `g541ae49b`).
- **12: framework docs** (LangGraph/LlamaIndex/DSPy/AutoGen official docs, DSPy arXiv) to
  doc-anchor the execution-model taxonomy (gaps `g570ec33f`/`g7d75ddab`).
- **13: GPT-Researcher repo/docs** for planner/executor/publisher internals (gaps
  `g77ddbc9c`/`g4ae1798d`).
- **02: A/B-test power / effect-size** experiment-design (gap `g483338f1`); **03: MADR/ADR
  record format** (gap `g5abb13ba`).
- **15 follow-up:** the ingested "SLP3 ch.6" PDF is actually the *Neural Networks* chapter —
  the genuine vector-semantics/embeddings chapter (tf-idf in NLP, PPMI, cosine) is still
  ungathered (gap queued); cosine normalization stays ungrounded.

**Provenance is THE reject axis** (4 rejects, 3 on this exact failure). Every drafter must open
each source, read its `source_url`, and label primary-paper/official-doc/repo vs
aggregator/blog/marketing — load-bearing claims rest on primaries, blog claims are attributed
and non-load-bearing. The promotable shape is **split-honest**: a genuine-primary load-bearing
core + openly-demoted blog material (findings 10/11/04/14 are models). The cautionary tales: 06
(aggregator dressed as arXiv) and 15 ("textbook bedrock" whose formulas were blog-sourced).

**Gotcha surfaced this arc — source-node ids drift across re-extraction.** An earlier 05
assertion pointed at a `sources_…` node that the next fold renamed, failing integrity. Fix was
to re-point the overlay line to the current id. **Prefer stable concept/synthesis/findings
nodes over `sources_…` nodes when asserting** — they survive rebuilds; source nodes don't.

**Definitive bar:** 17 of 17 domains grounded — breadth complete. SYNTHESIS's "Not yet
grounded" is now only a handful of narrow queued corners (each a blog→primary upgrade on an
already-grounded domain). Closing those is the last mile to "definitive."
