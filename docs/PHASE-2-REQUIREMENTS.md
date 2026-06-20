# Phase 2 — Requirements (seeded from the spike)

Evidence-backed requirements for building the actual research system. Each cites the
spike finding(s) / synthesis pattern that justifies it. Source of truth for the Phase-2
brainstorm.

## Confirmed by evidence

- **Protocol-first runs** — freeze a machine-readable plan (question, sub-questions,
  inclusion/exclusion criteria, target source types) *before* any retrieval, then diff
  actual behavior against it. — basis: SYNTHESIS "The recurring architecture" thesis;
  `docs/findings/01-methodology-epistemics.md`.
- **Multi-perspective sub-questioning, not raw retrieval volume** — decompose into 3–5
  sub-queries that span perspectives; perspective diversity is what drives organized,
  broad output and suppresses single-shot hallucination. — basis: SYNTHESIS pattern
  "Multi-perspective sub-questioning for breadth"; `docs/findings/05-ai-deep-research-systems.md`,
  `docs/findings/13-reference-systems-case-studies.md`.
- **Two-stage research-then-write** — a pre-writing/research phase produces an outline +
  cited reference set; the writing phase may only draw on those references (STORM:
  +25% organized, +10% coverage vs. outline-driven RAG baseline). — basis: SYNTHESIS
  pattern "Two-stage research-then-write"; `docs/findings/13-reference-systems-case-studies.md`,
  `docs/findings/05-ai-deep-research-systems.md`.
- **Hybrid (dense + BM25) + cross-encoder rerank as the default retrieval baseline**, with
  a graph / community-summary path routed in for thematic/multi-hop questions. — basis:
  SYNTHESIS pattern "Hybrid + graph retrieval, reranked"; `docs/findings/06-rag-retrieval.md`,
  `docs/findings/09-knowledge-compilation-graphs.md`, `docs/findings/04-applied-research-playbooks.md`.
- **Provenance / citation-first** — per-statement attribution as a first-class step, citation
  IDs embedded *before* generation, machine-readable carrier (CSL-JSON) — not a post-hoc
  formatting pass. — basis: SYNTHESIS pattern "Provenance / citation-first";
  `docs/findings/08-grounding-truth.md`, `docs/findings/07-agentic-orchestration.md`,
  `docs/findings/17-specs-standards.md`.
- **Faithfulness as an atomic-statement metric behind a multi-judge gate** — score the
  share of atomic answer statements grounded in the *exact* retrieved context, paired with
  noise-sensitivity and entity-recall; gate releases on it. — basis: SYNTHESIS pattern
  "Faithfulness as an atomic metric behind a multi-judge gate"; `docs/findings/08-grounding-truth.md`,
  `docs/findings/16-evaluation-benchmarks.md`.
- **Cost-tiered prompting / technique selection** — prompting technique is an explicit
  accuracy-vs-cost dial (few-shot → CoT → self-consistency → ToT; ReAct when external info
  is needed); choose by task type, not default to the most expensive. — basis: SYNTHESIS
  pattern "Decompose-before-concluding (cost-tiered prompting)"; `docs/findings/10-context-prompt-engineering.md`.
- **Durable, checkpointed orchestrator-worker, cost-gated** — LeadResearcher spawns 3–5
  parallel subagents with explicit objectives/boundaries/output formats; durable execution
  (checkpoints, resumable state, retry, per-subagent tracing) from day one; the expensive
  multi-agent path is gated behind a value/cost check. — basis: SYNTHESIS pattern "Durable
  orchestrator-worker, cost-gated"; `docs/findings/07-agentic-orchestration.md`,
  `docs/findings/05-ai-deep-research-systems.md`.
- **Indexing pipeline as the cost center** — incremental indexing, model tiering (cheap
  extraction, expensive summary), token-budget caps, parallel extraction queue. — basis:
  SYNTHESIS pattern "Indexing pipeline as the cost center"; `docs/findings/09-knowledge-compilation-graphs.md`,
  `docs/findings/11-research-pipeline-engineering.md`.
- **MADR decision records as output** — the system emits MADR-style records (context →
  considered options w/ pros-cons → decision → consequences → status) for its own
  non-obvious choices; rejected alternatives are required, not optional. — basis: SYNTHESIS
  pattern "MADR decision records as output"; `docs/findings/03-decision-frameworks.md`,
  `docs/findings/01-methodology-epistemics.md`.
- **Reproducible, tracked, standards-grounded runs** — versioned/restorable runs (MLflow-mold
  logging of params, artifacts, metrics, dependencies); open interchange formats (CSL-JSON,
  MCP as the agent-integration backbone); end-to-end tracing query → sources → citations →
  answer; PRISMA-style found/screened/kept/rejected record. — basis: SYNTHESIS pattern
  "Reproducible, tracked, standards-grounded runs"; `docs/findings/11-research-pipeline-engineering.md`,
  `docs/findings/15-textbooks-longform.md`, `docs/findings/17-specs-standards.md`.
- **Graph-structured knowledge with god-node surfacing** — compile the corpus into a graph
  with community detection + centrality so load-bearing concepts surface explicitly. — basis:
  SYNTHESIS "Graph reading"; `docs/findings/09-knowledge-compilation-graphs.md`.

## Working hypothesis — verdict

- **6-stage non-linear spine (Scope → Gather → Evaluate → Synthesize → Decide → Compile +
  feedback):** **Revised.** The spine's *shape* held up — every reference system (Perplexity
  teardown, the open-source clones, STORM, GPT-Researcher, Anthropic multi-agent) converges on
  the same skeleton, and the spike's own protocol-first execution validated freezing a plan
  before retrieval (SYNTHESIS "The recurring architecture"; `docs/findings/05`, `13`, `01`).
  Revision: the evidence demands an **explicit conflict-detection / verification stage between
  Synthesize and Decide** — the canonical pipeline is *per-source claim extraction → cross-source
  conflict detection → citation-embedded synthesis*, i.e. conflict resolution is its own
  load-bearing step, not folded into Evaluate or Decide (`docs/findings/05`, `08`,
  `13`). Feedback edges (any stage may re-scope on a discovered gap) are confirmed by the
  protocol-diff and gap-rescan loops the spike actually ran (`docs/findings/01`).
- **MADR as decision unit:** **Confirmed.** MADR core (context → options w/ pros-cons →
  decision → consequences → status) is the recommended record for the system's own non-obvious
  choices, with rejected alternatives as required output and a one-sentence canonical form for
  minor decisions. — basis: `docs/findings/03-decision-frameworks.md`.
- **graphify node/edge schema + god nodes:** **Confirmed.** The directed graphify pass built a
  real graph (147 files → 445 nodes, 521 edges, 61 communities; `.graphify/GRAPH_REPORT.md`)
  and god nodes surfaced by degree centrality. Caveat the schema must encode: the two highest-degree
  nodes were the catalog and the spec — structural hubs, not concepts — so god-node reading must
  go through cross-community bridges, not raw degree. — basis: SYNTHESIS "Graph reading";
  `docs/findings/09-knowledge-compilation-graphs.md`.
- **Phase-2 two-plane repo + template + new_project.py scaffolder + thin agents:** **Confirmed
  (structurally).** The spike itself ran on the normative-`docs/` + operational two-plane shape
  and the convergent finding is that the value lives in the orchestration layer, not the model —
  which a thin, stage-aligned agent/skill layer over a reusable run template directly serves.
  The scaffolder/template pattern is validated by the requirement for reproducible, versioned,
  restorable runs (one stamped run dir per research project). — basis: SYNTHESIS architecture
  thesis + "Reproducible, tracked, standards-grounded runs"; `docs/findings/11-research-pipeline-engineering.md`.
  Not independently stress-tested at scale — carry as confirmed-by-design, revisit in the brainstorm.

## Revised / new requirements the spike surfaced

- **Explicit conflict-detection / verification stage** as its own pipeline step between claim
  extraction and synthesis (see spine revision above). — basis: `docs/findings/05`, `08`, `13`.
- **CitationAgent topology** — a dedicated per-statement citation pass distinct from the
  synthesizer, with citation IDs embedded before generation. — basis: SYNTHESIS
  "Provenance / citation-first"; `docs/findings/07`, `08`.
- **Multi-judge faithfulness ensemble** — temperature 0, position-swap on pairwise comparisons,
  forbid self-judging, calibrate against a human-annotated reference set, wire into a deployment
  regression gate + daily production sample. — basis: `docs/findings/08`, `16`.
- **Technique-selection routing layer** — route each subtask to the cheapest technique that
  meets the accuracy bar (and route retrieval mode: precise-fact vector vs. global/thematic graph)
  rather than committing to one path. — basis: `docs/findings/10`, `06`, `09`.
- **Cost controls given the ~15x token multiplier** — value/cost gate before the multi-agent
  path; start single-agent linear and earn parallelism once tracing can measure it; treat the
  index build (not query time) as the cost center with model tiering + token caps. — basis:
  SYNTHESIS "Tensions"; `docs/findings/07`, `09`, `11`.
- **Corpus + graph versioning** — versioned, restorable runs *and* incremental/versioned
  index/graph builds (the cost center), so a run is reproducible end-to-end. — basis:
  `docs/findings/11`, `09`.
- **Multi-domain source-credibility rubric + per-claim certainty grade** — score sources on
  provenance/transparency/recency/corroboration (not a single trust score) and attach a
  per-claim certainty grade to output. — basis: `docs/findings/01`, `09`.
- **Multiple-comparison / multiple-hypothesis guard** — when the system fans out many
  sub-queries and aggregates positive findings, guard against manufacturing false positives.
  — basis: `docs/findings/02-statistical-causal-inference.md`.

## Dropped

None — the hypothesis held up. The 6-stage spine, MADR unit, graphify schema, and two-plane
repo all survived the evidence; the only changes were a revision (an explicit conflict/verify
stage) and additive requirements above. No component was argued against.

## Deep-dive backlog (corpus gaps to fill before/with Phase 2)

Honestly-flagged thin spots from the breadth scan (SYNTHESIS "Corpus gaps"), ordered by the
graph reading's priority signal:

- **`02` statistical/causal (top priority — high centrality, thin):** almost entirely
  Bayesian-vs-frequentist philosophy; no Pearl (DAGs, do-calculus, backdoor criterion), no
  potential-outcomes/counterfactuals, no statistical-power/A-B methodology. The stats node sits
  high in the graph reading, so this gap is the most load-bearing to close.
- **`04` applied playbooks:** badly skewed (4/5 cohort-retention, 1 TAM), marketing-blog tier;
  competitive analysis, trend detection, and A/B-test methodology named in the catalog but never
  gathered.
- **`08` grounding/truth:** only 4 sources; citation-*span* attribution mechanics and
  conflicting-source resolution-at-scale described conceptually, not implemented.
- **`11` pipeline engineering:** MLflow-skewed; broader pipeline-orchestration and
  reproducibility tooling underexplored.
- **`14` papers:** 3/5 "papers" are near-empty stub landing pages; no canonical
  agent/orchestration papers (ReAct, Toolformer, multi-agent surveys) — fetch full PDF bodies.
- **`16` evaluation/benchmarks:** named benchmarks GAIA / BrowseComp / HotpotQA gathered only
  secondhand (or not at all); omits OpenAI/Anthropic/Gemini Deep Research architectures and gives
  no comparative cost/latency/citation-accuracy numbers — fetch primary benchmark papers + RAGAS.
- **`17` specs/standards:** CSL-only (4/5); missing BibTeX spec, MADR/ADR templates, and the MCP
  specification (cited by topic 13 as the agent-integration backbone).
- **Cross-topic:** framework comparisons (`07`, `10`) lean on a single author — independent
  LangGraph / CrewAI / AutoGen benchmarks are needed.

## Open questions for Phase-2 brainstorming

- How does loop-engineering / orchestration (the deferred topic) map onto the spine's feedback
  edges — i.e. where exactly do re-scope / gap-rescan loops attach, and what triggers them?
- Build-vs-adopt for the orchestration substrate (LangGraph / LlamaIndex / CrewAI / AutoGen) —
  the corpus leans on a single author, so this needs independent evaluation before committing.
- Where do the human intervention points sit — high-importance entity/relationship review, judge
  calibration, scope-cut sign-off, low-faithfulness output review?
- What is the routing rule between precise-fact (vector) and global-synthesis (graph/long-context)
  retrieval modes — the RAG-vs-long-context boundary is unsettled in the sources.
- Does the simulated-dialogue breadth mechanism (STORM) earn its cost over a flat parallel-question
  planner (GPT-Researcher), and at what corpus size?
- What are the "good enough" faithfulness/coverage thresholds that gate a release, and how are they
  calibrated against the human-annotated reference set?
