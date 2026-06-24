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

## Current state (HEAD `aa3e7fd`; working tree clean modulo `public/dashboard.html`)
- **44 promoted findings / 5 rejected.** Corpus **208** active. Graph **2205 nodes / 2413 links**
  (`dirty:false`). **66 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`. **59 queued gaps** remain.
- **17 of 17 domains grounded** — breadth bar fully met. Prior sessions closed breadth + the seven
  item-2 blog→primary corners + six deep formula/spec arcs (PMI/PPMI, always-valid inference, Nygard
  ADR, RAGAS/ARES, FActScore/RARR, MCP spec internals).
- **This session — TEN reachable-frontier arcs**, each full gather→ingest→fold→draft→self-verify→
  independent-review→promote→re-ground→commit (all PROMOTED on first review; zero rejects; the only
  edits were honest pre-promote demotions of over-claims the reviewers or self-checks caught):
  - **17** Citation interchange formats — CSL-JSON official schema (45-type enum, required `[type,id]`),
    BibTeX btxdoc §3.1 entry-type field tables, schema.org `citation`/`ScholarlyArticle` — d59d1279b, `d5cd7b4`.
    Closed g9f10da22, g58e984b2, gccab40e9.
  - **16/05** GAIA (arXiv:2311.12983; 466 Q, human 92% vs GPT-4 15%) + BrowseComp (arXiv:2504.12516;
    1,266 Q, human 29.2% vs Deep Research 51.5%) task design + scores — d69d7458e, `7ac04c0`. Closed
    g97730f96, g23784af9, g5b7fa51c.
  - **16** Multi-hop QA benchmarks — HotpotQA (1809.09600, 112,779 Q, joint EM/F1), 2WikiMultiHopQA
    (2011.01060, 192,606 Q), MuSiQue (2108.00573, ~25K 2-4hop) — dcd1309fb, `5fb1a89`. Closed g2d31d5f9.
  - **09** KG2RAG full-PDF (arXiv:2502.06864) — chunk-expansion (m=1) algorithm + HotpotQA magnitudes
    (retrieval F1 0.436 vs 0.357) — d6c359091, `7a7ce48`. Closed g2af7d2ae.
  - **16** LLM-as-judge reliability — MT-Bench (2306.05685; position-bias 65%, 85% vs 81% human agreement),
    Judging-the-Judges (2406.12624; Scott's π), TruLens RAG-Triad — d4c45dd7e, `a779589`. Closed g3a31cd3d,
    gebd8db54, g3e19a7c9. (NOTE: the gap's `2401.10020` was MIS-LABELED — that id is "Self-Rewarding LMs";
    substituted the genuine judge primaries.)
  - **15** BM25 formula (IR-book Okapi HTML; k_1∈[1.2,2], b=0.75) + probabilistic idf justification
    (RSJ relevance weight, idf=log(N/df) at S=s=0) — d0fefa5d5, `be481c3`. Closed g1a6f7e17, gfa66fdc9.
  - **01** GRADE official Working Group handbook (4 levels, 5 downgrade + 3 upgrade domains, certainty≠
    recommendation) — upgraded a vendor-blog source to primary — d628b3d0f, `cba71a4`. Closed g9879bed2.
  - **14** Self-RAG (2310.11511) + Toolformer (2302.04761) full per-benchmark result tables — d154759ce,
    `5e4fbae`. Closed g64e0a010, g50593678.
  - **17** MCP Tools/Prompts wire shapes + Security Best Practices (confused-deputy, token-passthrough,
    session-hijacking) — completes the MCP corner alongside d3c246500 — d4562e116, `bfbc668`. Closed gdb207ceb.
  - **10** FSM-guided constrained decoding (Outlines, 2307.09702; regex→FSM index, O(1) masking) — d270b0177,
    `aa3e7fd`. Closed gc4e28042.
  Root `SYNTHESIS.md` re-grounded after each (now 44 findings, graph 2205/2413).
- **Gather technique that worked every time:** for clean math/spec content, prefer **HTML** primaries
  (IR-book, schema.org, MCP spec) — markitdown preserves LaTeX-in-img-alt-text and avoids PDF garble that
  bit the prior PMI/SGNS arc. arXiv PDFs still fine for prose+tables (grep the number whitespace-insensitively
  before trusting it). Always patch the corpus `source` to the real URL for `.md`/PDF ingests.

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
Verified against HEAD `aa3e7fd` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (44/5 findings, corpus 208 active, 66 assertions, 17/17 grounded domains, graph
2205/2413) read live from state.json + graph.json; the graphify `--update` recipe below is the
exact flow run this session 10× (detect→restrict detect.json to ONLY the new source `.md`s→AST
empty→ONE extraction subagent per ≤22-file chunk→build_merge(prune=changed sources only)→
build_from_json+cluster+to_json→replay→graph_events→set-graph→integrity). Design specs
live in `docs/superpowers/specs/` (6 files; umbrella `2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session (committed `d5cd7b4`→`aa3e7fd`): **ten reachable-frontier arcs** — see Current state
for per-arc finding ids, commits, and closed gaps. All promoted on first independent review (zero rejects
this session). The proven gather technique: bypass `search.py`, feed the **exact** primary URL. For clean
math/spec, prefer **HTML** sources (IR-book, schema.org, MCP spec, GRADE handbook) — markitdown keeps
LaTeX in img-alt-text and avoids the PDF garble that forced honest demotions in the prior PMI/SGNS arc;
arXiv **PDFs** are fine for prose+result-tables. ALWAYS grep the fetched bytes for the load-bearing
number/formula whitespace-insensitively before ingesting, **patch the corpus `source` to the real URL**,
and self-verify every reported figure against the source before the reviewer (who re-greps them). Two
recurring traps fixed inline this session: (a) extraction subagents *guess* cross-corpus node ids for
similarity edges — harmless, dedup/prune handles them; (b) a gap's named arXiv id can be WRONG (the
"Judging-the-Judges 2401.10020" was actually "Self-Rewarding LMs") — verify the fetched title matches.

**What's left (59 queued gaps). Still-REACHABLE clean primaries for a next session (highest-leverage first):**
- **Confidence sequences / always-valid multiple testing** (02, `gf72694e5`/`g32860b29`) — Howard, Ramdas,
  McAuliffe, Sekhon "Time-uniform… confidence sequences" (arXiv:1810.08240) + FWER/FDR under continuous
  monitoring. Math-heavy PDF (garble risk — state canonical form + note lossiness); extends the grounded
  always-valid finding dc588b7cc.
- **Causal identification strategies** (02, `g67421383`, + worked-ATE `ge2ff9cf2`) — IV / diff-in-diff / RDD.
  Foundational; needs careful primary sourcing (original method papers, not a book).
- **Reasoning-technique additions** (10) — Chain-of-Draft / token-budget reasoning (`g14b00688`, arXiv:2502.18600);
  structured-decoding schema-keyword compilation (`g3460ddda`, applied layer atop the now-grounded Outlines FSM).
- **Framework orchestration primitives** (12) — LangGraph Send/Command (`g7ee5f8a1`), AutoGen Topic/Subscription
  pub-sub (`g5d365921`) — official framework docs, clean but less durable than papers.
- **MCDA / AHP** (03, `g284a18b9`) — Saaty's analytic hierarchy process (consistency ratio). Reachable prose+formula.
- **biblatex expanded entry types** (17, `g0ac0c33b`) + **field-level CSL↔BibTeX↔schema.org crosswalk** (`g3518bee2`)
  — low-value extensions of the citation-formats finding (CTAN biblatex.pdf).
- **DEAD-SOURCE (leave queued, don't burn an arc re-confirming):** 06 controlled ColBERT-vs-cross-encoder
  single-table head-to-head (`ga344680a`/`g1fef4d1f`); 13 independent third-party GPT-Researcher cost/latency +
  STORM-vs-flat measurement (`gb02c7fd4`/`g4ae1798d`/`g32a8d1e8`); 12 neutral reproducible cross-framework
  latency/cost/accuracy benchmark (`g2d6b3b0c`); 02 sample-size under SUTVA/interference (`gd78c76ea`, needs
  network-interference/cluster-randomization literature) + empirical SUTVA-failure base rates (`g449073fd`);
  11 vendor-neutral CDC/index-freshness *standard* (`g172a5217`/`g860ec004`, no neutral spec exists — stays
  framework-doc-relayed). Each probed across sessions — no clean primary exists.
- Other older breadth-frontier gaps (true-GraphRAG shared-benchmark numbers, deep-research closed-agent
  internals) remain in the queue; reachability unverified — probe before committing an arc.

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

**Definitive bar:** 17 of 17 domains grounded — breadth complete. Across sessions the corpus now holds
**44 promoted findings** on peer-reviewed papers + official specs: prior sessions closed breadth, the
seven item-2 blog→primary corners, and six deep formula/spec arcs (PMI/PPMI, always-valid inference,
Nygard ADR, RAGAS/ARES, FActScore/RARR, MCP spec internals); **this session added ten reachable-frontier
arcs** (citation interchange formats, GAIA/BrowseComp, multi-hop QA benchmarks, KG2RAG full-PDF, LLM-judge
reliability + RAG-Triad, BM25 + probabilistic idf, GRADE official handbook, Self-RAG/Toolformer result
tables, MCP Tools/Prompts + security, FSM-guided constrained decoding). SYNTHESIS's "Not yet grounded" is
split-honest between (a) **still-reachable clean primaries** the next session can take (confidence sequences,
IV/DiD/RDD identification, Chain-of-Draft, framework orchestration primitives, MCDA/AHP, biblatex) and
(b) **confirmed dead-source** corners the direct-fetch path can't get (controlled ColBERT-vs-cross-encoder
single-table head-to-head; independent third-party GPT-Researcher measurement; neutral cross-framework
benchmark; SUTVA-interference sizing; vendor-neutral CDC/freshness standard) — left queued, honestly
labeled, not faked as done.
