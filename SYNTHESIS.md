# Synthesis — Building an AI Research System (grounded)

What the **verified evidence** supports about how to build a definitive research
system. Every claim here links to a *promoted* finding — one that passed citation,
faithfulness, and independent-reviewer gates on primary/official sources. Claims that
the earlier spike asserted but that no promoted finding yet backs are quarantined under
[Not yet grounded](#not-yet-grounded) rather than stated as fact.

Grounding status: **11 promoted findings across 10 of 17 domains** (01, 02, 03, 05, 06,
07, 08, 09, 16, 17). The methodology half (01 epistemics, 02 statistical/causal, 03
decision frameworks) is now grounded — the engine can defend its *epistemic credibility*,
not just its architecture/eval/interop. The applied/tooling/case-study domains (04,
10–15) are not yet researched — so the planning-template, prompting, and
reference-architecture layers below remain deliberately open.

## What the evidence supports

### Retrieval: hybrid + rerank is the low-regret baseline; heavier strategies are task-dependent
Sparse (BM25) and dense retrieval are complementary; "contextual retrieval" is an
architecture, not a product; and a reranker earns its place only on top of disciplined
chunking — the highest-ROI, low-regret upgrade
([hybrid/contextual RAG](docs/findings/dc97efcf9-hybrid-retrieval-contextual-rag-tradeoffs.md)).
On *shared* benchmarks the heavier strategies do not uniformly win: true GraphRAG's edge
over single-vector dense is **task-dependent** (mixed on chat, decisive on multi-hop
synthesis), BM25 beats SOTA dense on financial text+table corpora, and ColBERT
late-interaction trades index size for sub-linear rerank cost — all from peer-reviewed
sources, not vendor blogs
([GraphRAG/ColBERT shared-benchmark evidence](docs/findings/d73a9474e-graphrag-colbert-shared-benchmark-primary-evidence.md)).
**Implication:** default to hybrid+rerank; prove naive retrieval insufficient on *your*
corpus before adding GraphRAG or late-interaction.

### Deep-research agents beat search-augmented chat LLMs — but citation accuracy and volume trade off
On DeepResearch-Bench, purpose-built deep-research agents measurably outscore
search-augmented chat models, and a real, unresolved tension surfaces in the citation
metrics: **citation accuracy and citation volume pull against each other** (one system
over-cites, another cites less but more accurately)
([DeepResearch-Bench](docs/findings/dc6ee6f7f-deepresearch-bench-agents-beat-search-llms-citation-accuracy-tradeoff.md)).
**Implication:** the differentiator is the orchestration layer, not the base model; and
"more citations" is not "better grounded" — they must be measured separately.

### Self-correcting loops: the halt decision is the hard part, and it must be externally bounded
ReAct / Reflexion / CRAG / Self-RAG / multi-agent debate are better understood by *where
the halt decision lives and what bounds it* than by what each adds. An unbounded "iterate
until dry" loop is the dominant failure mode; the reliable bound is **external** (a hard
iteration cap + a force-complete guard), not the model's own self-judgment
([halt decision](docs/findings/d5c35de17-halt-decision-self-correcting-loops.md)).
**Implication:** every loop in the engine ships with an explicit external bound; "the
model decides when it's done" is a bug, not a design.

### Grounding: faithfulness is an atomic-statement metric, computed by structured LLM-judging over NLI entailment
Faithfulness = share of atomic answer statements entailed by the *exact* retrieved
context, computed via constrained JSON-schema LLM judging (not free-form prose) over an
NLI/entailment substrate; it is distinct from factual correctness, which anchors on
different evidence. The metric is only trustworthy after calibration against human labels
(position-swap, no verbosity reward)
([faithfulness machinery](docs/findings/dfa42bc8a-faithfulness-measurement-machinery.md)).
**Implication:** the engine's own promotion gate *is* a faithfulness check, so it inherits
exactly these confounds — it must judge structurally and stay calibrated.

### Knowledge graph: extraction method and community structure are the cost-fidelity levers
When compiling a source-of-truth KG corpus, the two measured levers are *how triples are
extracted* (a dependency-parser extractor retains ~94% of LLM-extraction context
precision at a fraction of the cost) and *how community/centrality structure is exploited*
(heavy-tailed degree distributions justify surfacing high-degree hub/"god" nodes)
([KG cost-fidelity levers](docs/findings/d37b490ee-extraction-method-and-community-structure-cost-fidelity-levers.md)).
**Implication:** the index build, not query time, is the cost center; tier the models
(cheap extraction, expensive summary).

### Evaluation: two distinct regimes, with different reliability properties
A research system has two things to prove. (1) Its **web-research agent** finds and
reasons over correct answers — evaluated by frozen-corpus agent benchmarks (Deep Research
Bench's RetroSearch freezes the web so re-runs are comparable, and scores the *trace* for
hallucination/tool-use/forgetting, not just the final answer; primary-sourced). (2) Its
**RAG stays grounded** — evaluated by decomposed harnesses (RAGAS/ARES/TruLens) that split
quality into retrieval vs generation metrics
([two evaluation regimes](docs/findings/d6fad1a98-two-evaluation-regimes-frozen-web-agent-benchmarks-vs-decomposed-rag-harnesses.md)).
**Implication:** freeze the corpus for comparable re-runs; evaluate the trace; keep the
agent-benchmark and RAG-harness regimes separate.

### Interoperability: build adapters against the actual specs (MCP, CSL-JSON, MADR)
Three independent seams, each with an official spec: expose capabilities to AI clients via
**MCP** (two-layer protocol, JSON-RPC data layer, Tools/Resources/Prompts primitives);
emit machine-readable citations via **CSL-JSON** (typed array of items, `id`/`type`/
`date-parts`); record the engine's own decisions via **MADR** (lean Markdown template,
status/date/context front-matter)
([interop primitives](docs/findings/d75f0cdee-interop-primitives-mcp-csl-madr.md)).
**Implication:** emit CSL-JSON for citations and MADR records for non-obvious choices;
expose the engine over MCP.

### Epistemics: grade evidence, reconcile contradictions, bound your own confidence
Three established human-methodology pillars map onto the engine's gates. **Source
credibility / evidence synthesis** — GRADE rates certainty (High/Moderate/Low/Very Low),
downgrading on risk-of-bias, inconsistency, indirectness, imprecision, and publication
bias, with the per-domain rationale documented; PRISMA mandates *reporting* the
search-and-selection trail; Cochrane supplies the method layer. **Claim
extraction / contradiction resolution** — pipelines split text into atomic, decontextualized
claims (Claimify reports ~99% entailed by the source sentence) and run NLI three-way
(entailment/contradiction/neutral) to surface conflicts for verification. **Calibration**
— confidence must be validated against observed frequency, not asserted
([grade/reconcile/calibrate](docs/findings/dc577f3e2-grade-reconcile-calibrate-evidence-pipeline.md)).
**Implication:** the citation gate is the engine's GRADE-style per-claim rationale; the
multi-judge review gate is its faithfulness-entailment check; both inherit GRADE/PRISMA's
discipline of separating *what was found* from *how certain it is* — and must stay
calibrated, since the calibration evidence in corpus is narrow (a vision-detection paper).

### Causal rigor: Pearl's do-calculus and Rubin's potential outcomes are complementary engines
Two traditions answer the same question — what causes what from observational data.
**Pearl**: a DAG encodes assumptions; the do-operator distinguishes intervention from
observation; the backdoor criterion picks the adjustment set that blocks confounding
(front-door handles unobserved confounders via a mediator); do-calculus is the complete
identifiability machinery. **Rubin**: potential outcomes frame the *fundamental problem of
causal inference* (only one outcome is observable per unit), identified under
unconfoundedness/ignorability + SUTVA, with the propensity score the coarsest balancing
score. Entrop's recognition that DAG d-separation and Rubin ignorability are the same
condition is the bridge
([two calculi](docs/findings/d2c5150e6-pearl-do-calculus-rubin-potential-outcomes-complementary.md)).
**Implication:** for the engine's own experiments, separate estimand from estimator,
probe positivity/overlap before trusting an effect, and treat **SUTVA as the assumption
most likely to break silently** when units share a cache, model, or rate limit.

### Decision-making: ACH for contested findings, weighted criteria for auditable records
**Analysis of Competing Hypotheses** enumerates hypotheses, builds an evidence×hypothesis
matrix, and scores by *fewest inconsistencies* — surviving disconfirmation, not
accumulating confirmation (evidence consistent with all hypotheses has zero diagnostic
value). Its enduring value is **auditability**, not bias-reduction: a 2024 peer-reviewed
synthesis (Wilcox & Mandel) finds ACH as a whole shows little-to-no benefit on judgment
quality and discourages mandating it. **Weighted multi-criteria** scoring is method-dependent
— different weighting schemes reorder the *entire* ranking, so multiple methods should be
used and the weights+method recorded
([ACH & weighted criteria](docs/findings/d1b3c3b4c-ach-and-weighted-criteria-for-contested-judgments.md)).
**Implication:** adopt ACH's *structure* (explicit hypothesis set, seek disconfirmation)
for cross-source conflict detection and the reviewer gate, but record decisions as
auditable weighted-criteria entries rather than mandating the full ACH ritual. (The MADR
record *format* itself is not yet grounded — corpus has the scoring methods, not the ADR
template.)

## Tensions & open questions (from the promoted findings)
- **Citation accuracy vs volume** — measured but mechanistically unexplained; no source in
  corpus shows *why* one agent over-cites or how per-claim accuracy is computed
  ([05](docs/findings/dc6ee6f7f-deepresearch-bench-agents-beat-search-llms-citation-accuracy-tradeoff.md)).
- **GraphRAG/ColBERT not on one shared benchmark** — the primaries use different corpora
  (enterprise PDFs, financial text+table, FineWeb), so cross-method numbers aren't directly
  comparable; GraphRAG is baselined only vs dense, not tuned hybrid
  ([06](docs/findings/d73a9474e-graphrag-colbert-shared-benchmark-primary-evidence.md)).
- **LLM-as-judge reliability** — judges carry variance and bias, so any eval/promotion gate
  must be validated against a human-labeled set before it can gate anything
  ([08](docs/findings/dfa42bc8a-faithfulness-measurement-machinery.md),
  [16](docs/findings/d6fad1a98-two-evaluation-regimes-frozen-web-agent-benchmarks-vs-decomposed-rag-harnesses.md)).
- **Reranker economics unquantified by primaries** — concrete latency/$/NDCG numbers in
  corpus came from marketing blogs (a finding was rejected over it); a controlled
  ColBERT-vs-cross-encoder benchmark is still ungathered
  ([06](docs/findings/d73a9474e-graphrag-colbert-shared-benchmark-primary-evidence.md)).

## Not yet grounded
The earlier spike asserted these as a complete pipeline; **no promoted finding backs them
yet** — they await the empty domains and must not be treated as evidenced:
- **A/B-test power & effect-size methodology** — 02's finding covers causal identification
  (DAGs, do-calculus, potential outcomes) but not experiment-design power; that gap is queued.
- **MADR/ADR decision-record *format*** (fields, template, Nygard practice) — 03 grounds the
  *scoring methods* (ACH, weighted MCDM) but not the record schema; queued as a 03 gap.
- **Two-stage research-then-write, multi-perspective sub-questioning (STORM/GPT-Researcher)** — 13 (0 corpus).
- **Cost-tiered prompting (few-shot→CoT→self-consistency→ToT)** — 10 (0 corpus).
- **Orchestrator-worker cost model (the ~15×-tokens / 3–5-subagent / ~90%-latency figures)** —
  these came from the old topic-07 stub; the *promoted* 07 finding covers halt-bounding only.
- **MLflow-style reproducible tracked runs, indexing-pipeline tooling** — 11 (0 corpus).
- **Tooling landscape (LangGraph/LlamaIndex/DSPy/AutoGen comparison)** — 12 (0 corpus).
- **Canonical papers (ReAct, Toolformer, multi-agent surveys) and IR textbook grounding** — 14, 15 (0/stub).

## Graph reading
A graphify pass over the corpus currently yields **1436 nodes / 1358 links** (32 of those
links are human-free asserted edges in the committed overlay, tagged `_origin:asserted`;
`.graphify/GRAPH_REPORT.md`). The graph now contains the *findings* as concept nodes, not
just the sources — so traversal crosses finding→source→concept, and the asserted edges
wire domains together (e.g. eval-benchmarks → grounding-truth, KG-extraction → god-nodes).
Earlier centrality readings in this file (147 files / 445 nodes / 61 communities) are
obsolete and were removed; re-run `graphify` and read the current `GRAPH_REPORT.md` for
god-node and bridge rankings rather than trusting a pinned snapshot.

---
*The auto-maintained index of every promoted finding lives at
[docs/findings/SYNTHESIS.md](docs/findings/SYNTHESIS.md) (appended by `promote.py`). This
file is the human cross-domain distillation; that one is the flat list.*
