# Synthesis — Building an AI Research System

Cross-topic distillation of the Phase-1 spike. Each pattern links to the per-topic
findings ([docs/findings/](docs/findings/)) that support it.

## The recurring architecture

A single pipeline shape recurs across the spike, independent of which topic surfaced it.
A research run is **protocol-first**: it freezes a machine-readable plan — question,
sub-questions, inclusion/exclusion criteria, target source types — *before* any retrieval,
then diffs actual behavior against that plan
([01](docs/findings/01-methodology-epistemics.md)). The plan decomposes the question into
3–5 sub-queries that deliberately span multiple *perspectives*, not just more retrieval
([05](docs/findings/05-ai-deep-research-systems.md),
[13](docs/findings/13-reference-systems-case-studies.md)).

Each sub-question is answered by **hybrid retrieval (dense + BM25) followed by a
cross-encoder reranker** — the two highest-ROI, low-regret upgrades every retrieval source
agrees on ([06](docs/findings/06-rag-retrieval.md),
[04](docs/findings/04-applied-research-playbooks.md)) — with a **graph / community-summary**
path routed in for global, thematic, multi-hop questions that flat vector RAG structurally
cannot answer ([09](docs/findings/09-knowledge-compilation-graphs.md)). Retrieved passages
go through **per-source claim extraction**, then **cross-source conflict detection**, then a
**citation-embedded synthesizer** that may only use the gathered references and emits a
per-statement provenance trail ([05](docs/findings/05-ai-deep-research-systems.md),
[08](docs/findings/08-grounding-truth.md), [07](docs/findings/07-agentic-orchestration.md)).

The whole run is **observable and reproducible**: end-to-end tracing from query → sources →
citations → answer, a PRISMA-style record of how many sources were found / screened / kept /
rejected, and tracked, versioned runs in the MLflow mold
([05](docs/findings/05-ai-deep-research-systems.md),
[01](docs/findings/01-methodology-epistemics.md),
[11](docs/findings/11-research-pipeline-engineering.md)). The convergence is striking:
Perplexity's teardown, the open-source clones, STORM, GPT-Researcher, and Anthropic's
multi-agent system describe the *same* skeleton — the differentiator is the orchestration
layer, not the model.

**Thesis:** every reference system converges on one pipeline — *freeze a plan → decompose
into multi-perspective sub-questions → hybrid+rerank (and graph) retrieval → per-source
claim extraction → conflict resolution → citation-embedded synthesis → traced, reproducible
run* — and the engineering value lives in that orchestration layer, not the underlying LLM.

## Load-bearing patterns

- **Two-stage research-then-write** — A pre-writing/research phase produces an outline plus a
  cited reference set; a separate writing phase may only draw on those references. STORM and
  GPT-Researcher both enforce this split, and STORM measures it (+25% organized, +10% broader
  coverage vs. an outline-driven RAG baseline). (findings:
  [13](docs/findings/13-reference-systems-case-studies.md),
  [05](docs/findings/05-ai-deep-research-systems.md))
- **Multi-perspective sub-questioning for breadth** — Decompose the topic into many
  sub-questions *and* seek diverse perspectives per topic; perspective diversity (simulated
  expert dialogue or a planner-generated objective set), not raw retrieval volume, is what
  drives organized, broad output and suppresses single-shot hallucination. (findings:
  [05](docs/findings/05-ai-deep-research-systems.md),
  [13](docs/findings/13-reference-systems-case-studies.md),
  [01](docs/findings/01-methodology-epistemics.md))
- **Hybrid + graph retrieval, reranked** — Dense+BM25 hybrid with a cross-encoder reranker is
  the universal low-regret baseline; chunking quality dominates outcomes; a GraphRAG
  local/global path (Leiden community detection, ~1200-token chunks) is added situationally
  for thematic/multi-hop questions rather than as a universal upgrade. (findings:
  [06](docs/findings/06-rag-retrieval.md),
  [09](docs/findings/09-knowledge-compilation-graphs.md),
  [04](docs/findings/04-applied-research-playbooks.md))
- **Provenance / citation-first** — Treat attribution as a first-class, per-statement step (a
  dedicated CitationAgent pass), with citation IDs embedded *before* generation and CSL-JSON
  as the machine-readable carrier — not a post-hoc formatting pass. (findings:
  [08](docs/findings/08-grounding-truth.md),
  [07](docs/findings/07-agentic-orchestration.md),
  [17](docs/findings/17-specs-standards.md))
- **Faithfulness as an atomic metric behind a multi-judge gate** — Score faithfulness as the
  share of atomic answer statements grounded in the *exact* retrieved context, paired with
  noise-sensitivity and entity-recall so retrieval vs. generation failures separate. Judge
  with a validated multi-judge ensemble at temperature 0, swap positions on pairwise
  comparisons, forbid self-judging, and wire it into a deployment regression gate plus a daily
  production sample. (findings: [08](docs/findings/08-grounding-truth.md),
  [16](docs/findings/16-evaluation-benchmarks.md))
- **Decompose-before-concluding (cost-tiered prompting)** — Prompting technique is an explicit
  accuracy-vs-cost dial (few-shot → CoT → self-consistency → ToT; ReAct when external info is
  needed; structured output for format compliance). Choose by task type rather than defaulting
  to the most expensive path. (findings:
  [10](docs/findings/10-context-prompt-engineering.md))
- **Durable orchestrator-worker, cost-gated** — Breadth-first research maps onto a
  LeadResearcher that spawns 3–5 parallel subagents with explicit objectives/boundaries/output
  formats, then a separate citation pass. Parallelization is the dominant latency lever (~90%
  time reduction) but costs ~15x the tokens of a single chat — so the expensive multi-agent
  path is gated to tasks whose value clears the bar; start single-agent linear and earn the
  parallelism once tracing can measure it. (findings:
  [07](docs/findings/07-agentic-orchestration.md),
  [05](docs/findings/05-ai-deep-research-systems.md),
  [12](docs/findings/12-tooling-landscape.md))
- **Indexing pipeline as the cost center** — The graph/index build, not query time, is where
  cost concentrates: incremental indexing, model tiering (cheap extraction, expensive
  summary), token-budget caps, and a parallel extraction queue. (findings:
  [09](docs/findings/09-knowledge-compilation-graphs.md),
  [11](docs/findings/11-research-pipeline-engineering.md))
- **MADR decision records as output** — The system emits MADR-style records (context →
  considered options w/ pros-cons → decision → consequences → status) for its own non-obvious
  choices — scope cuts, source-trust thresholds, conflict resolutions — making its reasoning
  auditable and re-litigable; rejected alternatives are required, not optional. (findings:
  [03](docs/findings/03-decision-frameworks.md),
  [01](docs/findings/01-methodology-epistemics.md))
- **Reproducible, tracked, standards-grounded runs** — Runs are versioned and restorable
  (MLflow-style logging of params, artifacts, metrics, dependencies), grounded in primary
  references (Manning's *Introduction to Information Retrieval* for the IR layer) and emitted in
  open interchange formats (CSL-JSON for citations, MCP as the agent-integration backbone).
  (findings: [11](docs/findings/11-research-pipeline-engineering.md),
  [15](docs/findings/15-textbooks-longform.md),
  [17](docs/findings/17-specs-standards.md))

## Tensions & open questions

- **Token cost vs. breadth.** The orchestrator-worker design buys ~90% latency reduction at
  ~15x token cost; the value/cost ratio is asserted from Anthropic's own production but
  independently un-benchmarked, and the "right" subagent count (3–5) is heuristic, not derived
  ([07](docs/findings/07-agentic-orchestration.md)).
- **Heavy retrieval vs. low-regret baseline.** Agentic RAG and GraphRAG can cost ~10x and add
  ~5s latency; one benchmark found a commercial reranker gave "no notable advantage," while
  another found SOTA RAG answered 63% of factual questions vs. 44% for plain retrieval — payoff
  is corpus-dependent, so prove naive RAG insufficient on *your* data first
  ([06](docs/findings/06-rag-retrieval.md), [04](docs/findings/04-applied-research-playbooks.md)).
- **RAG vs. long-context.** The emerging hybrid (RAG narrows millions → top 50–200, then a
  100K+ context window reasons over them) blurs the either/or, but the routing rule between
  precise-fact and global-synthesis modes is unsettled
  ([06](docs/findings/06-rag-retrieval.md), [10](docs/findings/10-context-prompt-engineering.md)).
- **Simulated dialogue vs. flat parallel planner.** STORM's perspective-discovery + simulated
  expert conversation vs. GPT-Researcher's flat parallel-question planner both produce breadth;
  whether the multi-agent conversation earns its cost is unresolved by the sources
  ([13](docs/findings/13-reference-systems-case-studies.md)).
- **LLM-as-judge reliability.** Judges carry quantified biases (verbosity ~+15%, ~40%
  position-bias inconsistency, self-enhancement), so evaluation itself needs validation against
  a human-annotated reference set before it can gate anything
  ([08](docs/findings/08-grounding-truth.md), [16](docs/findings/16-evaluation-benchmarks.md)).

## Corpus gaps (from the breadth scan)

These honestly-flagged thin spots define the deep-dive backlog for Phase 2:

- **[02](docs/findings/02-statistical-causal-inference.md)** — almost entirely
  Bayesian-vs-frequentist *philosophy*; no Pearl (DAGs, do-calculus, backdoor criterion), no
  potential-outcomes/counterfactuals, no statistical-power/A-B methodology.
- **[04](docs/findings/04-applied-research-playbooks.md)** — badly skewed (4/5 cohort-retention,
  1 TAM); marketing-blog tier; competitive analysis, trend detection, and A/B-test methodology
  named in the catalog but never gathered.
- **[08](docs/findings/08-grounding-truth.md)** — only 4 sources; citation *span* attribution
  and conflicting-source resolution-at-scale described conceptually but not implemented.
- **[11](docs/findings/11-research-pipeline-engineering.md)** — MLflow-skewed; broader
  pipeline-orchestration and reproducibility tooling underexplored.
- **[14](docs/findings/14-papers.md)** — 3/5 "papers" are near-empty stub landing pages; no
  canonical agent/orchestration papers (ReAct, Toolformer, multi-agent surveys) — needs full
  PDF bodies fetched.
- **[16](docs/findings/16-evaluation-benchmarks.md)** — omits OpenAI/Anthropic/Gemini Deep
  Research architectures and gives no comparative cost/latency/citation-accuracy numbers across
  systems.
- **[17](docs/findings/17-specs-standards.md)** — CSL-only (4/5); missing BibTeX spec, MADR/ADR
  templates, and the MCP specification (cited by topic 13 as the agent-integration backbone).
- Cross-topic: framework comparisons ([07](docs/findings/07-agentic-orchestration.md),
  [10](docs/findings/10-context-prompt-engineering.md)) lean on a single author — independent
  LangGraph/CrewAI/AutoGen benchmarks are needed.

## Graph reading

_(placeholder — filled in Task 7 after graphify identifies god nodes)_
