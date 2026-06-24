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

## Current state (HEAD `f4aab5e`; working tree clean modulo `public/dashboard.html`)
- **34 promoted findings / 5 rejected.** Corpus **186** active. Graph **1969 nodes / 2114 links**
  (`dirty:false`). **66 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`.
- **17 of 17 domains grounded** — breadth bar fully met. The seven narrow item-2 blog→primary
  corners were closed in a prior session; this session worked the **deeper frontier**.
- **This session — six deep-frontier arcs (one a reject→redraft), each full gather→ingest→fold→draft→review→promote:**
  - **15** PMI/PPMI defining formulas (Church-Hanks 1990 + Levy-Goldberg 2014 shifted-PMI) + tf-idf-in-NLP
    (SLP3 Ch.11) — d7289dbd9, `3822ef7`. Closed g1919d0da, g857b90f5.
  - **02** continuous-monitoring/peeking A/B corrections — always-valid inference + mSPRT (Johari et al.,
    *Operations Research*/arXiv:1512.04922). First draft **d21f3389c REJECTED** by the AI reviewer (it inverted
    the M-vs-log(1/α) efficiency condition); redrafted **dc588b7cc PROMOTED**, `aa5f6e8`. Closed g3d3c22b9.
  - **03** Nygard's original five-section ADR template + decision-log numbering (his 2011 post + Nat Pryce
    adr-tools) — d657c1d86, `b45431a`. Closed g4a91aeef, gf8ab7685.
  - **16** RAGAS + ARES primary metric formulas (Es et al. 2309.15217 F=|V|/|S|, AR cosine; Saad-Falcon
    2311.09476 judges+PPI) — d636208ea, `73ae911`. Closed g324348e1.
  - **08** FActScore atomic-fact precision + RARR attribution editing (Min 2305.14251, Gao 2210.08726) —
    d1ad78766, `13a4bc0`. Closed g4668dd58.
  - **17** MCP spec internals (official 2025-06-18 spec: primitives, stdio vs Streamable HTTP, OAuth 2.1,
    Resources subscribe/list_changed mapped onto the append-only store) — d3c246500, `f4aab5e`. Closed
    g0d8366cb, g6fb2909d, gf369dd48.
  Root `SYNTHESIS.md` re-grounded after each (now 34 findings, graph 1969/2114).
- **Two named-hard gaps confirmed dead-source this session** (search + direct-fetch both failed):
  **06** peer-reviewed controlled ColBERT-vs-cross-encoder NDCG table (ga344680a) — no single clean published
  table exists; the candidate arXiv 2408.16672 is the Jina-ColBERT-v2 *model* paper, not a controlled
  head-to-head. **13** independent third-party GPT-Researcher cost/latency + STORM-vs-flat measurement
  (gb02c7fd4/g4ae1798d) — only the project's own repo/FAQ exist; no third-party measurement. Both left
  queued (honest dead-source, not done).

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
Verified against HEAD `f4aab5e` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (34/5 findings, corpus 186 active, 66 assertions, 17/17 grounded domains, graph
1969/2114) read live from state.json + graph.json; the graphify `--update` recipe below is the
exact flow run this session 6× (detect→drop state.json/dashboard.html→AST→cache→ONE extraction
subagent per ≤22-file chunk→build_merge→to_json→replay), run 7× this session. Design specs
live in `docs/superpowers/specs/` (6 files; umbrella `2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session (committed `3822ef7`→`f4aab5e`): **six deep-frontier arcs** (15 PMI/PPMI+tf-idf,
02 always-valid/peeking, 03 Nygard ADR, 16 RAGAS/ARES, 08 FActScore/RARR, 17 MCP spec internals —
see Current state for per-arc commits + closed gaps; the 02 arc demonstrates the reject→redraft loop
working: the AI reviewer caught an inverted efficiency condition, the redraft fixed it and promoted).
Root `SYNTHESIS.md` re-grounded after each. The proven gather technique (search engine keeps landing
on TOC/landing pages): bypass `search.py` and feed the **exact** URL as a `.url` file (official-doc
pages, via crawl4ai — records the real URL as provenance) or `curl` the **PDF** into `ingest/`
(arXiv/journal). ALWAYS grep the fetched bytes for the load-bearing formula/term before ingesting
(markitdown squashes whitespace — grep whitespace-insensitively), and **patch the corpus `source` to
the real URL** for PDFs (ingest records them `file://`; `.url`/link ingests already record the URL).
The reviewer is strict and **verifies numbers/formulas against the source** — self-verify every
reported figure (grep the source) before dispatching the reviewer; honestly demote anything garbled
by PDF→markdown conversion rather than reporting it as exact.

**What's left (142 open gaps) is the deeper frontier — but several are still REACHABLE clean
primaries**, not dead-source. Honest priority for a next session:
- **Citation interchange formats** (17, `g9f10da22`/`g58e984b2`/`gccab40e9`) — CSL-JSON full type
  enumeration + JSON Schema (dhimmel/csl-schema), BibTeX, schema.org `ScholarlyArticle`/citation
  property. All official specs / fetchable. Cleanest remaining win.
- **GAIA + BrowseComp task design + reported scores** (16/05, `g97730f96`/`g23784af9`/`g5b5fa51c`) —
  GAIA = arXiv:2311.12983, BrowseComp = OpenAI paper/blog. Fetchable primaries; a prior source was
  mislabeled (held DRB instead) so this needs the genuine papers.
- **Multi-hop QA benchmarks** (16, `g2d31d5f9`) — HotpotQA / 2WikiMultiHopQA / MuSiQue construction +
  metrics, all arXiv primaries.
- **KG2RAG full-PDF** (09, `g2af7d2ae`) — HotpotQA result magnitudes + chunk-expansion algorithm
  (corpus has abstract-only c520aee3f); fetch the full arXiv PDF.
- **RAGAS/ARES bias magnitudes + Judging-the-Judges** (08, `g3a31cd3d`) — the metric *formulas* are now
  grounded (d636208ea); what remains is the reproducible-bias-magnitude numbers + Judging-the-Judges
  (2401.10020). TruLens RAG-Triad primary also still open (`gebd8db54`).
- **DEAD-SOURCE (leave queued, don't burn an arc re-confirming):** 06 controlled ColBERT-vs-cross-encoder
  single-table head-to-head (`ga344680a`); 13 independent GPT-Researcher cost/latency + STORM-vs-flat
  measurement (`gb02c7fd4`/`g4ae1798d`). Both probed this session — no clean primary exists.
- Other older breadth-frontier gaps (true-GraphRAG shared-benchmark numbers, deep-research closed-agent
  internals, interference/SUTVA A/B sizing `gd78c76ea`) remain; the interference one needs a different
  primary (network-interference / cluster-randomization literature) than the always-valid result.

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

**Definitive bar:** 17 of 17 domains grounded — breadth complete — the seven item-2 blog→primary
corners closed in a prior session, and this session **six deep-frontier formula/spec arcs** (PMI/PPMI,
always-valid inference, Nygard's original ADR, RAGAS/ARES, FActScore/RARR, MCP spec internals) grounded
on peer-reviewed papers + official specs. SYNTHESIS's "Not yet grounded" is now split-honest between
(a) **still-reachable clean primaries** the next session should take (citation interchange formats CSL-JSON/
BibTeX/schema.org, GAIA/BrowseComp scores, multi-hop QA benchmark construction, KG2RAG full-PDF) and
(b) **confirmed dead-source** corners the direct-fetch path can't get (controlled ColBERT-vs-cross-encoder
single-table head-to-head; independent third-party GPT-Researcher measurement) — left queued, honestly
labeled, not faked as done.
