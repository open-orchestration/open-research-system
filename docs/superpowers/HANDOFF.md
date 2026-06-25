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

## Current state (HEAD `16f3150`; working tree clean modulo `public/dashboard.html`)
- **54 promoted findings / 5 rejected.** Corpus **220** active. Graph **2473 nodes / 2786 links**
  (`dirty:false`; unchanged — this session was a process-cycle finding off already-ingested corpus, no fold).
  **66 graph assertions** (overlay `.research/graph-assertions.jsonl`).
  Phase `deepen`. **51 queued gaps** (all dead-source/no-clean-primary/redundant — see Next steps).
- **This session — one process-cycle finding, no gap-chasing** (PROMOTED on first independent review):
  **02** **RDD estimation & validity in practice** (Lee & Lemieux, NBER w14723, `c213028d1`): RD as a
  *local randomized experiment* → **local linear** at the boundary (global polynomials + raw kernel
  averages biased; LL "reduces the bias by an order of magnitude", Hahn et al. 2001) → bandwidth by
  boundary-specific **leave-one-out cross-validation** / RD-tuned plug-in (ROT const 2.702, ∝N^−1/5) →
  falsify with **McCrary** density test + **continuity-of-covariates** check. d8d9c5187, `16f3150`.
  Deliberately complements the identification-level finding df8ca1aeb (which it cross-references) instead
  of re-deriving it. Queued one honest residual gap `ge53e646b` (named placebo/non-cutoff test +
  polynomial-order-selection criterion — not in Lee-Lemieux; would need Cattaneo rdrobust / Gelman-Imbens).
- **The process/candidates cycle is now also exhausted of defensible material.** All three ≥3-uncited
  topics were assessed live this session: **06** = the dead-source RAG-head-to-head corpus (skip, confirmed);
  **15-textbooks** = its uncited corpus is the blog trio (geeksforgeeks / dasroot.net / edge-ai-vision —
  reject-tier provenance) plus IIR/J&M **landing pages with no formulas**, and IR-eval metrics are already
  densely grounded by d2fbbb962 + d8b594416 → no defensible new finding; **02** = the remaining 5 uncited
  chunks are *other chunks of papers already grounded* (confidence sequences, Card-Krueger, Imbens-Angrist,
  Lunceford-Davidian, Yang online-FDR) whose key themes the existing findings already cover → a second slice
  would be redundancy-rejected. RDD was the one separable survey-half worth a complement; it's now taken.
- **17 of 17 domains grounded** — breadth bar fully met. Prior sessions closed breadth + the seven
  item-2 blog→primary corners + six deep formula/spec arcs (PMI/PPMI, always-valid inference, Nygard
  ADR, RAGAS/ARES, FActScore/RARR, MCP spec internals) + ten reachable-frontier arcs (citation
  formats, GAIA/BrowseComp, multi-hop QA, KG2RAG, LLM-judge, BM25/idf, GRADE, Self-RAG/Toolformer,
  MCP tools/prompts, FSM constrained decoding).
- **This session — NINE reachable-frontier arcs** (the entire prior-handoff priority list + companions),
  each full gather→ingest→fold→draft→self-verify→independent-review→promote→re-ground→commit (all
  PROMOTED on first review; zero rejects; only edits were honest pre-promote demotions the self-checks/
  reviewers caught). The reachable single-primary frontier is now **exhausted**:
  - **02** Nonparametric LIL-rate **confidence sequences** (Howard, Ramdas, McAuliffe, Sekhon,
    arXiv:1810.08240): CS def `P(∀t: θ_t∈CI_t)≥1−α`, sub-Gaussian CS `µ̂±1.7√[(loglog2t+0.72log(10.4/α))/t]`,
    LIL rate, line(non-shrinking)-vs-curved(shrinking) boundary — d541a8e56, `b9849c8`. Closed gf72694e5.
  - **02** Quasi-experimental **identification IV/DiD/RDD** — Imbens-Angrist 1994 LATE (monotonicity,
    exclusion, compliers), Card-Krueger 1994 DiD (NJ $4.25→$5.05), Lee-Lemieux 2010 RDD (sharp/fuzzy,
    continuity) — df8ca1aeb, `ee9ec0a`. Closed g67421383.
  - **10** **Chain-of-Draft** primary (arXiv:2502.18600): GSM8K GPT-4o CoT 95.4%/205tok→CoD 91.1%/44tok,
    "five words at most", honest ~4pp drop for ~79% fewer tokens; "7.6%" is across-task — d6432467b,
    `3454a67`. Closed g14b00688 (upgraded the blog-relayed claim in d0cce1cec).
  - **12** **LangGraph Send/Command + AutoGen Topic/Subscription** orchestration primitives (official
    docs): Send=dynamic fan-out, Command=update+goto, Topic=(type,source), TypeSubscription, broadcast
    vs direct — d1fb5a112, `d07fba2`. Closed g7ee5f8a1, g5d365921.
  - **03** **Saaty AHP** (own 2008 overview): pairwise on 1–9 scale, 4 decomposition steps, eigenvector
    priorities, consistency-ratio concept (0.022 example) — d030916c4, `f2d2e91`. Closed g284a18b9.
    (CI=(λmax−n)/(n−1)/RI/0.10-threshold NOT in this overview — honest gap.)
  - **02** Propensity-score **IPW + doubly-robust ATE estimation** (Lunceford-Davidian 2004, Stat. Med.):
    PS adjustment via stratification/IPW, doubly-robust = consistent if EITHER PS or outcome model right
    ("two chances to be right") — d77c7f685, `9c60321`. Closed ge2ff9cf2.
  - **17** **biblatex** modern entry types (CTAN manual): @online/@electronic/@www (required +locator
    doi/eprint/url), @thesis (type+institution), @dataset, @software=@misc; modern fields urldate/eprint/
    doi/pubstate — de47719c4, `f359134`. Closed g0ac0c33b.
  - **16** **JSONSchemaBench** (arXiv:2501.10868): 10K real-world schemas, 6 frameworks; Guidance highest
    coverage (19 cats), best supports 2× the worst; constrained decoding HELPS — +50% speed, +4% downstream
    — dd09194c4, `be0a91e`. Closed ge419534b (process gap).
  - **02** **Online FDR for A/B-test streams** (Yang, Ramdas, Jamieson, Wainwright, arXiv:1706.05378):
    always-valid sequential p-values + LORD (alpha-investing, α-wealth) → any-time mFDR control over a
    stream — d42ec736c, `6e7e1e6`. Closed g32860b29 (the multiple-testing residual dc588b7cc flagged).
  Root `SYNTHESIS.md` re-grounded after each (now 54 findings, graph 2473/2786).
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
Verified against HEAD `6e7e1e6` (working tree clean modulo the unrelated
`public/dashboard.html`): all cited scripts exist (`search_flow.sh ingest_flow.sh
orchestrator.py state.py assertions.py promote.py cite_check.py check_integrity.py
graph_events.py runlog.py`); `.claude/` has `goal.md loop.md process.md review.md`; state
numbers (53/5 findings, corpus 220 active, 66 assertions, 17/17 grounded domains, graph
2473/2786) read live from state.json + graph.json; the graphify `--update` recipe below is the
exact flow run this session 9× (detect→restrict detect.json to ONLY the new source `.md`s→AST
empty→ONE extraction subagent per ≤22-file chunk→build_merge(prune=changed sources only)→
build_from_json+cluster+to_json→replay→graph_events→set-graph→integrity). Design specs
live in `docs/superpowers/specs/` (6 files; umbrella `2026-06-17-open-research-system-design.md`).

## Next steps (pick up here)
DONE this session (committed `b9849c8`→`6e7e1e6`): **nine reachable-frontier arcs** — see Current state
for per-arc finding ids, commits, and closed gaps. All promoted on first independent review (zero rejects).
This session **closed the entire prior-handoff priority list** (confidence sequences, IV/DiD/RDD,
Chain-of-Draft, LangGraph/AutoGen primitives, MCDA/AHP, biblatex) **plus its companions** (worked-ATE
IPW/doubly-robust, online-FDR multiple-testing) **plus one high-value adjacent** (JSONSchemaBench).
The proven gather technique still holds: bypass `search.py`, feed the **exact** primary URL; prefer
**HTML** for clean math/spec; arXiv **PDFs** fine for prose+tables (markitdown ligature/table garble is
real — state canonical form + note lossiness, never transcribe a garbled equation). ALWAYS grep the
fetched bytes for the load-bearing number/formula whitespace-insensitively before ingesting, **patch the
corpus `source` to the real URL**, and self-verify every figure against the source before the reviewer.
NEW trap fixed this session: a >700KB ingested source overflows a bash `$(…)` variable so shell `grep`
silently returns 0 — **verify large sources in Python** (`re.sub(r'\s+','',open(p).read())`), not a shell var.
Author-hosted PDFs (McGill/Berkeley/Baylor faculty pages, CTAN, journal DOIs) reliably reach paywalled
econ/stats primaries that direct publisher links 404 — search by title, grep the result list for an
`.edu`/CTAN host.

**What's left (50 queued gaps) — the reachable single-primary frontier is EXHAUSTED.** Every remaining
queued gap is one of: (a) confirmed dead-source, (b) no clean primary exists (implementation detail or a
synthesis across sources), or (c) bookkeeping (a breadth gap already satisfied in substance by a promoted
finding whose `status` was never flipped). Do **not** burn an arc on these without a genuinely new source:
- **No clean primary (probed this session, confirmed):**
  - `g3460ddda` schema-keyword→regex→FSM **compilation algorithm** (10) — lives in the `outlines` library
    *source*, not a paper; the Outlines paper (d270b0177) abstracts it and JSONSchemaBench (dd09194c4)
    benchmarks behavior, not the compilation. No paper publishes the per-keyword table as a contribution.
  - `g3518bee2` field-level **CSL↔BibTeX↔schema.org crosswalk** (17) — no single source publishes a
    bidirectional field-level map; would be synthesized. The *type-level* concordance is already in d59d1279b.
  - **FWER** (stricter than FDR) under continuous monitoring — Yang et al. (d42ec736c) controls **mFDR**, not
    FWER; the FWER-under-optional-stopping criterion would need a different primary.
- **DEAD-SOURCE (handoff-confirmed across sessions, leave queued):** 06 controlled ColBERT-vs-cross-encoder
  single-table head-to-head (`ga344680a`/`g1fef4d1f`) and true-GraphRAG-vs-tuned-hybrid shared-benchmark
  (`gb5db13e7`/`g6b3b56d5`); 13/05 independent third-party GPT-Researcher cost/latency + closed-agent internals
  (`gb02c7fd4`/`gcccbc027`); 12 neutral reproducible cross-framework benchmark (`g2d6b3b0c`); 02 sample-size
  under SUTVA/interference (`gd78c76ea`) + SUTVA-failure base rates (`g449073fd`); 11 vendor-neutral CDC/
  index-freshness *standard* (`g172a5217`/`g860ec004`). No clean primary — each probed repeatedly.
- **The process/candidates cycle has now been worked to exhaustion too** (this session — see Current state):
  the one defensible non-redundant complement (02 RDD estimation/validity, d8d9c5187) is taken; 15-textbooks'
  uncited corpus is blog-tier + content-free landing pages, and 02's residual uncited chunks are extra slices
  of already-grounded papers. Below is the prior assessment, still accurate for what it labels —
- **(prior-session note) If a future session wants more grounding,** the next move *was* the **process/candidates cycle**
  (not gap-chasing): `state.py candidates` shows topics with ≥3 *uncited* corpus sources (currently 06, 15,
  02) — turn that already-gathered material into findings. CAUTION: 06's uncited corpus is the dead-source
  RAG-head-to-head material that was rejected on provenance; 15-textbooks is the more promising untapped vein.
  Otherwise the corpus is at a natural plateau: 54 findings, 17/17 domains, every reachable clean primary grounded,
  and both the gap frontier AND the process/candidates cycle are now exhausted of defensible non-redundant material.

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
**54 promoted findings** on peer-reviewed papers + official specs: prior sessions closed breadth, the
seven item-2 blog→primary corners, six deep formula/spec arcs, and ten reachable-frontier arcs; **this
session added nine more** (confidence sequences, IV/DiD/RDD identification, Chain-of-Draft, LangGraph/
AutoGen orchestration primitives, Saaty AHP, propensity-score IPW/doubly-robust ATE estimation, biblatex
modern entry types, JSONSchemaBench constrained-decoding reliability, online-FDR for A/B-test streams) —
which **closed the entire prior priority list plus its companions**. The reachable single-primary frontier
is now **exhausted**: SYNTHESIS's "Not yet grounded" is left split-honest between (a) **no-clean-primary**
corners (schema-keyword compilation algorithm — lives in library source; field-level CSL↔BibTeX↔schema.org
crosswalk — synthesis-only; FWER-under-optional-stopping — stricter than the grounded mFDR) and
(b) **confirmed dead-source** corners the direct-fetch path can't get (controlled ColBERT-vs-cross-encoder
head-to-head; true-GraphRAG-vs-tuned-hybrid shared benchmark; independent third-party GPT-Researcher/closed-
agent measurement; neutral cross-framework benchmark; SUTVA-interference sizing; vendor-neutral CDC/freshness
standard) — left queued, honestly labeled, not faked as done. The process/candidates cycle has now also been
worked to exhaustion: the single separable survey-half worth a complement (02 RDD estimation/validity) is grounded,
and the remaining ≥3-uncited topics are blog-tier (15), dead-source (06), or redundant same-paper chunks (02).
Both frontiers — gap-driven and process-driven — are now at their defensible limit.
