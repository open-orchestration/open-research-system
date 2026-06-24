# Synthesis — Building an AI Research System (grounded)

What the **verified evidence** supports about how to build a definitive research
system. Every claim here links to a *promoted* finding — one that passed citation,
faithfulness, and independent-reviewer gates on primary/official sources. Claims that
the earlier spike asserted but that no promoted finding yet backs are quarantined under
[Not yet grounded](#not-yet-grounded) rather than stated as fact.

Grounding status: **27 promoted findings across all 17 of 17 domains** (01–17). Every
domain now has at least one finding that passed the citation + faithfulness +
independent-reviewer gates on primary/official sources. The methodology half (01 epistemics,
02 statistical/causal, 03 decision frameworks) is grounded — the engine can defend its
*epistemic credibility*, not just its architecture/eval/interop — as is the
applied/tooling/case-study half (04 playbooks, 10 prompting/context, 11 pipeline-ops, 12
tooling, 13 reference-systems, 14 foundational papers), and now the **textbook bedrock**
(15: tf-idf and the retrieval-evaluation metrics on the IR-book chapters, plus vector
semantics — cosine, the distributional hypothesis, word2vec — on the genuine SLP3 chapter). What
remains is not an empty domain but a set of narrow per-domain corners — blog-tier claims
awaiting a primary upgrade — listed under [Not yet grounded](#not-yet-grounded).

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
corpus before adding GraphRAG or late-interaction. The *cost* case for late interaction is
now primary-grounded: the ColBERT/ColBERTv2 papers themselves show it reallocates
BERT-grade understanding to a one-time offline document encoding, collapsing query-time cost
to embedding transfer plus a pruning-friendly MaxSim (~170× speedup, ~14,000× fewer
FLOPs/query vs a BERT reranker at competitive MRR@10); the design's one liability — a
per-token index an order of magnitude larger — is what v2's residual compression cuts from
154 GiB to 16–25 GiB (6–10×) at 50–250 ms/query with no reported quality loss
([late-interaction economics](docs/findings/d6ccd6b1c-late-interaction-colbert-economics.md)).

### Deep-research agents beat search-augmented chat LLMs — but citation accuracy and volume trade off
On DeepResearch-Bench, purpose-built deep-research agents measurably outscore
search-augmented chat models, and a real, unresolved tension surfaces in the citation
metrics: **citation accuracy and citation volume pull against each other** (one system
over-cites, another cites less but more accurately)
([DeepResearch-Bench](docs/findings/dc6ee6f7f-deepresearch-bench-agents-beat-search-llms-citation-accuracy-tradeoff.md)).
**Implication:** the differentiator is the orchestration layer, not the base model; and
"more citations" is not "better grounded" — they must be measured separately.

For frontier *named* agents specifically, **benchmark accuracy (GAIA/BrowseComp,
vendor-neutral leaderboards) is the only cross-vendor comparable** — cost, latency, and
"internal architecture of closed agents" are vendor-reported or third-party-reconstructed,
not independently verified, and must be carried as attributed, never as fact
([benchmark-accuracy-only](docs/findings/d369c3d06-benchmark-accuracy-is-the-only-cross-vendor-comparable.md)).
And the self-correction methods (ReAct/Reflexion/CRAG/Self-RAG) have **no clean
same-benchmark head-to-head** — published deltas come from different papers on different
setups; only the CRAG benchmark and a controlled multi-agent-debate study are genuine
primaries, while per-iteration cost figures are author estimates
([the head-to-head that isn't](docs/findings/df8e7fa14-head-to-head-that-isnt-comparative-accuracy-debate-convergence-economics.md)).
**Meta-implication:** across deep-research and orchestration, the durable evidence is
benchmark accuracy under stated conditions; cost/latency/architecture are the axis where
vendor marketing masquerades as fact — tier provenance explicitly or the gate rejects (it
did, twice this corpus).

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
auditable weighted-criteria entries rather than mandating the full ACH ritual. The decision
*record format* is now grounded too: an **Architectural Decision Record (ADR)** captures a
single decision and its rationale, and the collection forms a **decision log**; the official
**MADR** template prescribes the fields — Context and Problem Statement, Decision Drivers,
Considered Options, Decision Outcome (chosen option + justification), Consequences (Good/Bad),
Confirmation, and Pros and Cons of the Options — the ADR community site crediting Michael
Nygard's 2011 post as the popularizing origin
([ADR/MADR record format](docs/findings/decf6989c-adr-madr-decision-record-format.md)). So the
scoring *methods* PRODUCE a decision and the ADR/MADR *format* RECORDS it with rationale and
consequences — complementary halves.

### Tooling: choose by execution model, not by ranking — and treat framework comparisons as opinion
Agent frameworks differ on a **durable execution-model axis** that outlives any "best
framework" listicle: LangGraph is a graph/state-machine (nodes, conditional edges, typed
state, checkpointing), LlamaIndex is data/query-engine-first, DSPy is a compile-time prompt
*optimizer* used alongside an orchestrator (not a replacement for one), and AutoGen routes
multi-agent *conversation* (GroupChat) rather than a graph
([execution-model taxonomy](docs/findings/d28841446-execution-model-taxonomy-not-best-framework-ranking.md)).
The four-way taxonomy is now **doc-anchored to each framework's own primary docs/paper**,
not blog-convergent: LangGraph's `StateGraph` (nodes/edges over reducer-merged shared state
stepped in Pregel-style super-steps), LlamaIndex's `@step` methods consuming/emitting typed
events with a validated event graph, AutoGen Core's message-passing agents over a
standalone-or-distributed runtime, and DSPy's declarative modules+signatures compiled by
teleprompters (quantitatively raising program quality "from 33% to 82%" and "from 32% to
46%") — DSPy correctly placed as a *compile-time* optimizer orthogonal to the three runtime
models ([doc-anchored execution models](docs/findings/de92d6feb-execution-models-doc-anchored.md)).
Still vendor/blog opinion, not evidence: every comparative ranking/latency/cost/adoption
number.
**Implication:** pick orchestration by the control-flow shape the task needs; do not trust
framework leaderboards — the *shapes* are now primary-grounded, the *rankings* are not.

### Reference systems: STORM proves research-then-write + multi-perspective questioning (paper-backed)
The strongest primary-sourced case study is **STORM** (Shao et al., NAACL 2024): a two-stage
pipeline that separates **pre-writing** (perspective-guided question asking + simulated
expert conversations → outline) from **writing** (outline → cited article), measured on
FreshWiki to produce articles judged **+25% more organized and +10% broader in coverage**
than an outline-driven RAG baseline — and honest about its own failure modes (source-bias
transfer, over-association of unrelated facts). STORM also tiers models per task (cheap LM
for conversation/question-gen, powerful LM for outline/article). **GPT-Researcher** is a
second reference point, and its internals are now **repo/doc-grounded** rather than
landing-page-only: a `planner`/`execution` agent core (planner generates research questions,
execution agents gather per-question, publisher aggregates) plus a separate 7-role LangGraph
"editorial team" (Chief Editor, Researcher, Editor, Reviewer, Revisor, Writer, Publisher)
that runs Researcher/Reviewer/Revisor in parallel per outline topic; the project
*self-reports* "~5 minutes" and "~$0.4 per research (o3-mini on high reasoning effort)" for
its recursive Deep Research workflow — a vendor self-report, not an independent benchmark
([STORM/GPT-Researcher case studies](docs/findings/dbc0e9395-storm-paper-backed-pipeline-vs-gpt-researcher-with-provenance-tiering.md),
[GPT-Researcher internals](docs/findings/da592d4f8-gpt-researcher-internals.md)).
**Implication:** separate research from writing as distinct stages; drive breadth with
multi-perspective sub-questioning; tier model cost per stage — these are now evidenced
patterns, not speculation.

### Foundations: the canonical papers the whole engine inherits
The agent/RAG mechanisms this system rests on are paper-established: **ReAct** (interleave
thought/action/observation; arXiv:2210.03629), **Self-RAG** (retrieve on demand, then
self-assess relevance/support/utility via reflection tokens; arXiv:2310.11511), and
**Toolformer** (self-supervised decide-which/when/args for tool calls; arXiv:2302.04761),
with the tool-learning survey mapping the internal-vs-external planner space
([foundational papers](docs/findings/de3e9818e-foundational-agent-rag-papers.md)).
**Implication:** the engine's loop *is* ReAct; its citation-gate + faithfulness check *is*
Self-RAG's per-segment support assessment; its search/ingest tools *are* Toolformer's
decide-when-to-call discipline — these are inherited theory, not invention.

### Textbook bedrock: tf-idf and the retrieval-evaluation metrics, grounded on the canonical chapters
The engine's retrieval-scoring and evaluation vocabulary is now defined from the field's
canonical textbook chapter prose rather than blog summaries. *Introduction to Information
Retrieval* (Manning, Raghavan & Schütze; chs. 6 & 8) supplies **idf_t = log(N/df_t)**,
the composite **tf-idf_{t,d} = tf_{t,d} × idf_t** and the document-as-vector overlap
score; the set-based measures (precision, recall, **F = 2PR/(P+R)**) with the textbook's
own argument for why **accuracy fails under class skew** (>99.9% nonrelevant); and the
ranked-retrieval measures (precision–recall curve, interpolated precision, **MAP**,
Precision@k, **R-precision ≡ break-even point**, and **nDCG** for graded relevance)
([textbook bedrock](docs/findings/d2fbbb962-textbook-grounded-retrieval-scoring-and-evaluation-metrics.md)).
**Vector semantics is now grounded too**, on the genuine SLP3 chapter (Jurafsky & Martin,
2026 draft, Ch.5 "Embeddings") that the earlier mislabeled ingest missed — the prior "SLP3
ch.6" file was actually the *Neural Networks* chapter. The new finding grounds the
**distributional hypothesis**, the count-based word-context/term-document matrices, **cosine
similarity** (the length-normalized dot product, `a·b = |a||b|cosθ`, normalized so similarity
reflects co-occurrence *direction* rather than word frequency — the specifically-named
previously-ungrounded item), the sparse→dense motivation, and **word2vec / skip-gram with
negative sampling** (static embeddings as a self-supervised classifier's learned weights)
([vector semantics](docs/findings/ddc396092-vector-semantics-cosine-embeddings.md)). That
finding is split-honest about its scope: SLP3 Ch.5 *defers tf-idf to its Ch.11* and mentions
PPMI only in passing, so a defining PPMI formula stays ungrounded. **Implication:** these are
the primary definitions a downstream scoring/embedding component can trust as bedrock;
cosine — long the named open corner — is now closed on chapter prose.

### Prompting & context: escalate cost only when it pays; don't stuff the context window
On the prompting ladder (few-shot → CoT → self-consistency → ToT), the rungs are now
**paper-anchored** from the originating works, retiring the earlier blog-relayed numbers:
**chain-of-thought** is an *emergent* ability of scale — with PaLM-540B + 8 exemplars it
lifts GSM8K 17.9→56.9% (+39 pts) but does not help (and can hurt) small models
(arXiv:2201.11903); **self-consistency** samples diverse reasoning paths and majority-votes
the answer, adding ~+17.9 pts on GSM8K at the cost of N× inference (arXiv:2203.11171); and
**tree-of-thoughts** adds deliberate BFS/DFS search with LM self-evaluation, taking
Game-of-24 from 4% (GPT-4 CoT) to 74% but at materially higher API cost and only where the
task actually needs search (arXiv:2305.10601)
([paper-anchored ladder](docs/findings/d0b1fc5c6-paper-anchored-prompting-ladder.md)).
The complementary context-management half is **lost-in-the-middle** (arXiv:2307.03172):
long-context accuracy is highest when relevant text sits at the beginning or end and
degrades in the middle, even for long-context models — so prefer **targeted retrieval over
context-stuffing**, and escalate the reasoning ladder only when expected value beats added
token cost
([prompting/context](docs/findings/d0cce1cec-prompting-ladder-context-management-paper-anchored-vs-blog-relayed.md)).

### Operations: reproducible tracking is docs-settled; index freshness is convention
**MLflow** (official docs) supplies the reproducibility model the engine already mirrors —
runs/params/metrics/artifacts + a registry with **stage promotion and lineage** (the analogue
of this engine's draft→finding promotion and finding→cited-corpus-id lineage). The
index-freshness *mechanism* now has an **official-doc anchor**, not just blog convergence:
LlamaIndex's IngestionPipeline docs document per-(node+transformation) **caching** (re-runs
reuse cached results when the cache is persisted) and **docstore-backed document management**
that maps `doc_id → document_hash` to upsert on a changed hash, skip on an unchanged one, and
dedup — i.e. selective reprocessing keyed on a content hash rather than full re-index
([index-freshness mechanism](docs/findings/da2a65c0c-index-freshness-ingestion-pipeline.md)).
This is one framework's documented mechanism, not a vendor-neutral CDC standard; the
*trigger cadence* and *drift detection* remain blog-relayed
([pipeline ops](docs/findings/d470b6824-reproducible-tracking-docs-anchored-index-freshness-blog-relayed.md)).

### Applied playbooks: architecture converges (anchored); RAG retrieval craft is blog-consensus
A genuine arXiv DR survey and a reputable practitioner build-log (mcp-agent, derived from
Anthropic's "Building Effective Agents") independently converge on the
**planner/orchestrator → dynamic subagents → synthesis** spine, with two generalizable moves:
**prefer deterministic code checks over LLM self-judgment**, and **externalize memory** rather
than bind to the context window. The production-RAG craft (structure-aware chunking, hybrid +
rerank, filter-before-search) is dev-agency blog-consensus — sensible defaults, not evidence
([applied playbooks](docs/findings/d603c3334-convergent-playbook-anchored-architecture-blog-consensus-rag-craft.md)).

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
- **Cross-encoder reranker economics still unquantified by primaries** — the ColBERT
  *late-interaction* economics are now primary-grounded from the arXiv papers themselves
  (2004.12832, 2112.01488: FLOPs, latency, recall, index-storage compression)
  ([06](docs/findings/d6ccd6b1c-late-interaction-colbert-economics.md)). What remains
  blog-only is the *cross-encoder* reranker side: concrete latency/$/NDCG figures still come
  from marketing blogs or an AI-summary aggregator (emergentmind) — a 06 finding was rejected
  this session for citing that aggregator while claiming arXiv provenance — and there is still
  no controlled, same-corpus ColBERT-vs-cross-encoder head-to-head NDCG/recall table from a
  peer-reviewed source.

## Not yet grounded
Every domain is grounded, but these specific claims are **not yet backed by a promoted
finding** — each is a narrow corner awaiting a primary-source upgrade, and must not be
treated as evidenced until gathered:
- **A/B-test power & effect-size methodology** — 02's finding covers causal identification
  (DAGs, do-calculus, potential outcomes) but not experiment-design power; that gap is queued.
- **Nygard's original four-field ADR template + decision-log numbering convention** — the
  ADR/MADR record *format* is now grounded on the official ADR site + MADR template
  ([ADR/MADR format](docs/findings/decf6989c-adr-madr-decision-record-format.md)), but the
  corpus has MADR's expanded schema, not Nygard's original four fields, and the log
  numbering/file-naming scheme (the "ADR-0123" reference) is unspecified in-corpus. Both queued.
- **PPMI weighting formula** — cosine, the distributional hypothesis, and word2vec are now
  grounded on the genuine SLP3 Ch.5 "Embeddings" chapter
  ([vector semantics](docs/findings/ddc396092-vector-semantics-cosine-embeddings.md)), but
  that chapter *defers tf-idf to its Ch.11* and mentions PPMI only in passing as word2vec's
  implicit weighting — no defining PMI/PPMI formula is in any ingested chapter yet (queued).
- **Prompting-ladder cost-normalized curve** — the CoT/self-consistency/ToT *benchmark
  numbers* are now paper-anchored from the originating works (Wei 2201.11903, Wang 2203.11171,
  Yao 2305.10601), but no source gives an accuracy-per-token/dollar head-to-head on a shared
  benchmark, nor results on 2025-era reasoning-tuned models, so the escalation economics stay a
  qualitative rule, not a measured curve. Two 10 gaps queued.
- **Vendor-neutral index-freshness spec** — the freshness *mechanism* is now doc-anchored on
  LlamaIndex's IngestionPipeline (caching + docstore hash dedup/upsert)
  ([index-freshness](docs/findings/da2a65c0c-index-freshness-ingestion-pipeline.md)), but that
  is one framework's docs, not a vendor-neutral CDC/freshness *standard*; the trigger cadence
  (event-driven vs scheduled) and drift detection stay blog-relayed. Those remain queued.
- **Orchestrator-worker cost model (the ~15×-tokens / 3–5-subagent / ~90%-latency figures)** —
  these came from the old topic-07 stub; the *promoted* 07 findings cover halt-bounding and
  the no-clean-head-to-head provenance result, not the cost multipliers.
- **A/B-test power, controlled cross-encoder-vs-ColBERT head-to-head, independent
  GPT-Researcher cost/latency + STORM-vs-flat-planner head-to-head, Nygard's original ADR
  template** — all have queued gaps (see the tensions above and the per-domain notes); each is
  a narrow ungathered corner, not an empty domain. (GPT-Researcher's *internals* are now
  repo/doc-grounded; the MADR record format is grounded; the framework execution-model taxonomy
  is doc-anchored — what stays open there is only comparative ranking/cost numbers, inherently
  vendor opinion.)

## Graph reading
A graphify pass over the corpus currently yields **1786 nodes / 1890 links** (66 of those
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
