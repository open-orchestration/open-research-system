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

## Current state (HEAD `0a73960`; working tree clean modulo `public/dashboard.html`)
- **28 promoted findings / 4 rejected.** Corpus **172** active. Graph **1798 nodes / 1912 links**
  (`dirty:false`). **66 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`.
- **17 of 17 domains grounded** — the breadth bar is fully met. Every domain has ≥1 finding
  past the citation + faithfulness + independent-reviewer gates.
- **The narrow item-2 corners are now closed.** This session upgraded seven blog-tier claims to
  primaries/official docs, each a full gather→ingest→fold→draft→review→promote arc:
  - **06** late-interaction economics on the real arXiv ColBERT/ColBERTv2 papers (d6ccd6b1c,
    `fe8dbe5`) — redraft of the rejected aggregator-sourced angle, now primary-only.
  - **12** execution-model taxonomy doc-anchored on LangGraph/LlamaIndex/AutoGen official docs
    + the DSPy arXiv paper (de92d6feb, `1637eb2`).
  - **15** vector semantics (cosine, distributional hypothesis, word2vec) on the genuine SLP3
    Ch.5 "Embeddings" chapter — closing the named cosine corner (ddc396092, `bb26a3c`).
  - **13** GPT-Researcher internals on the repo README + multi-agent docs (da592d4f8, `c0d8adf`).
  - **11** index-freshness mechanism on the LlamaIndex IngestionPipeline docs (da2a65c0c, `0d270a2`).
  - **03** ADR/MADR decision-record format on adr.github.io + the MADR template (decf6989c, `f4c6c89`).
  - **02** A/B experiment-design power on Kohavi et al. DMKD 2009 (d740bae09, `0a73960`).
  Root `SYNTHESIS.md` was re-grounded after each (now 28 findings, graph 1798/1912).

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
Verified against HEAD `0a73960` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (28/4 findings, corpus 172 active, 66 assertions, 17/17 grounded domains, graph
1798/1912) read live from state.json + graph.json; the graphify `--update` recipe below is the
exact flow run this session (detect→drop state.json/dashboard.html→AST→cache→ONE extraction
subagent per ≤22-file chunk→build_merge→to_json→replay), run 7× this session. Design specs
live in `docs/superpowers/specs/` (6 files; umbrella `2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session (committed `fe8dbe5`→`0a73960`): **all seven narrow item-2 corners closed**
(06/12/15/13/11/03/02 — see Current state for the per-arc commits). Root `SYNTHESIS.md`
re-grounded after each. The proven technique that did it (search engine keeps landing on
TOC/landing pages): bypass `search.py` and feed the **exact** URL as a `.url` file (official
docs pages, via crawl4ai — records the real URL as provenance) or `curl` the **PDF** into
`ingest/` (arXiv/journal papers). ALWAYS sanity-check the fetched bytes contain the
load-bearing prose before ingesting (grep the key formula/term), and **patch the corpus
`source` to the real URL** for PDFs (ingest records them as `file://`).

**What's left is no longer "blog→primary on an already-grounded domain" — it's the harder
frontier.** 67 gaps remain queued, but they are deeper/net-new, and several need sources the
direct-fetch + search-drain reliably can't get (independent third-party reproductions,
controlled same-corpus head-to-heads that may not exist as a single published table). Honest
priority order for a next session:
- **PPMI defining formula** (15) — the cleanest remaining win: SLP3 Ch.5 defers tf-idf/PPMI to
  its **Ch.11** (`https://web.stanford.edu/~jurafsky/slp3/11.pdf` — verify the 2026-draft
  numbering, the chapters renumbered: ch.5=Embeddings, ch.6=Neural Networks). Gaps
  `g1919d0da`/`g857b90f5`.
- **Controlled cross-encoder-vs-ColBERT head-to-head** (06) — a peer-reviewed same-corpus
  NDCG/recall table; current controlled sources are blogs. May not exist cleanly (the prior
  session already found this hard). Gaps `ga344680a`/`gade3c1ff`/`g1fef4d1f`.
- **Independent GPT-Researcher cost/latency + STORM-vs-flat-planner head-to-head** (13) — the
  ~5min/~$0.4 figures are now grounded but only as the project's *self-report*; a third-party
  measurement is queued (`gb02c7fd4`/`g4ae1798d`).
- **Sequential/peeking A/B corrections + sizing under interference** (02) — Kohavi 2009 grounds
  the fixed-horizon case; continuous-monitoring corrections queued (`g3d3c22b9`/`gd78c76ea`).
- **Nygard's original four-field ADR template + decision-log numbering** (03) — corpus has
  MADR's expanded schema, not Nygard's 2011 original (`gf8ab7685`/`g4a91aeef`).
- The older breadth-frontier gaps (GraphRAG shared-benchmark, deep-research benchmark numbers,
  MCP spec internals, RAGAS/ARES primary formulas, etc.) predate this session and remain.

**Verify live before trusting any of the above** — `state.py candidates`, `list-gaps`,
`check_integrity.py`. Gap ids drift as work proceeds.

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

**Definitive bar:** 17 of 17 domains grounded — breadth complete — AND the seven narrow
item-2 corners (the blog→primary upgrades on already-grounded domains) now closed on
primaries/official docs. SYNTHESIS's "Not yet grounded" is now only the harder frontier:
independent reproductions, controlled same-corpus head-to-heads, and a few clean-but-deferred
formulas (PPMI, Nygard's original ADR fields). These are the next-session targets, several
needing sources the direct-fetch path can't reliably get.
