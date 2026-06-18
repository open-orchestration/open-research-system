# open-research-system — Research Catalog

**Purpose:** Taxonomy of the field "how to do AI-assisted research → decisions →
actionable knowledge", the sources to mine per area, and the phased research plan.
This is the contract the spike executes against. Topic slugs match `docs/NN-*` dirs.

## Categories

### 01-methodology-epistemics  (P0)
**Scope:** How research itself should be done (human + AI): framing → search → eval →
synthesis → verification, including primary/qualitative methods.
**Sub-topics:** question/objective framing; search strategy & query formulation; source
credibility/authority/currency; bias detection; claim extraction & cross-referencing;
synthesis & sense-making; verification/contradiction resolution; confidence/evidence
weighting; primary & qualitative methods (interviews, surveys, ethnography, sampling,
triangulation); knowledge management (Zettelkasten, evergreen notes).
**Sources to mine:** Booth "Craft of Research"; Cochrane Handbook (systematic review);
PRISMA; "How to Read a Paper" (Greenhalgh); Zettelkasten / Ahrens "How to Take Smart
Notes"; Andy Matuschak evergreen notes.
**Priority:** P0

### 02-statistical-causal-inference  (P1)
**Scope:** Quantitative spine for defensible decisions.
**Sub-topics:** significance/p-values & misconceptions; effect size; confidence
intervals; Bayesian vs frequentist; hypothesis testing; regression; time-series;
causal inference; experimental design & power analysis; Monte Carlo.
**Sources to mine:** Gelman "Statistical Rethinking"/McElreath; Pearl "Book of Why";
"Statistics Done Wrong"; Cohen power analysis; ASA statement on p-values.
**Priority:** P1

### 03-decision-frameworks  (P0)
**Scope:** Turning findings into recorded, defensible decisions.
**Sub-topics:** MADR/ADR; decision matrices (weighted criteria); Analysis of Competing
Hypotheses (ACH); cost-benefit; SWOT; risk modeling; stress/scenario/sensitivity
analysis; go/no-go & ship/no-ship gates.
**Sources to mine:** MADR (adr.github.io / madr.dev); Michael Nygard "Documenting
Architecture Decisions"; Heuer "Psychology of Intelligence Analysis" (ACH); decision
matrix / Pugh matrix references.
**Priority:** P0

### 04-applied-research-playbooks  (P2)
**Scope:** Concrete research genres with their own methods.
**Sub-topics:** competitive teardown; market/TAM sizing; trend & weak-signal detection;
cohort/retention; A/B experimentation; idea validation; SEO/intent; systematic
literature review.
**Sources to mine:** Porter "Competitive Strategy"; "Lean Analytics"; Trustworthy
Online Controlled Experiments (Kohavi); jobs-to-be-done literature.
**Priority:** P2

### 05-ai-deep-research-systems  (P0)
**Scope:** Existing AI systems that do research end-to-end — to teardown.
**Sub-topics:** deep-research agents (OpenAI/Google/Anthropic Deep Research); STORM
(Stanford); GPT-Researcher; Perplexity / Elicit-class; open-source clones & their
architectures.
**Sources to mine:** STORM paper + repo (stanford-oval/storm); GPT-Researcher
(assafelovic/gpt-researcher); OpenAI/Google/Anthropic Deep Research write-ups; Elicit
methodology posts.
**Priority:** P0

### 06-rag-retrieval  (P0)
**Scope:** Retrieval architectures powering research systems.
**Sub-topics:** naive→advanced RAG; GraphRAG; agentic RAG; embeddings; vector stores;
hybrid (BM25 + dense) search; rerankers; chunking; context management.
**Sources to mine:** Microsoft GraphRAG (paper + repo); "Retrieval-Augmented
Generation" (Lewis 2020); Anthropic Contextual Retrieval; LlamaIndex/LangChain RAG
docs; reranker papers (Cohere/ColBERT).
**Priority:** P0

### 07-agentic-orchestration  (P0)
**Scope:** Coordinating agents/loops to execute research.
**Sub-topics:** planner-worker; fan-out/verify; debate/critique loops; multi-agent
patterns; loop-engineering (iterate-until-dry); reward/policy design (RL: exploration,
PPO/offline/inverse); shared context/state stores; orchestration patterns
(sequential/parallel/pipeline/map-reduce/hierarchical).
**Sources to mine:** Anthropic "Building effective agents" + multi-agent research
system post; LangGraph docs; AutoGen; ReAct paper; Reflexion; CRAG; Self-RAG.
**Priority:** P0

### 08-grounding-truth  (P0)
**Scope:** Making outputs faithful and checkable.
**Sub-topics:** citation/attribution; hallucination mitigation; LLM-as-judge;
evaluation of research outputs; faithfulness metrics; research-output quality/style
auditing (anti-AI-isms).
**Sources to mine:** "LLM-as-a-judge" survey; RAGAS; TruLens; FActScore; attribution
papers (RARR); Anthropic/OpenAI eval cookbooks.
**Priority:** P0

### 09-knowledge-compilation-graphs  (P0)
**Scope:** Turning findings into a queryable source-of-truth.
**Sub-topics:** source-of-truth maintenance; normative docs; knowledge-graph
construction (god nodes / nodes / edges); community detection & centrality; synthesis→
decision pipelines; retrieval-optimized knowledge stores.
**Sources to mine:** graphify skill (`~/.claude/skills/graphify`); GraphRAG community
detection; knowledge-graph construction surveys; PKG / Roam/Obsidian graph models.
**Priority:** P0

### 10-context-prompt-engineering  (P1)
**Scope:** Prompt/context techniques for research tasks.
**Sub-topics:** context engineering; CoT/ToT/ReAct; constitutional/role-based;
long-context vs RAG trade-offs; token/context compression; output parsing.
**Sources to mine:** Anthropic prompt engineering + context engineering guides; "Chain
of Thought" (Wei); "Tree of Thoughts"; DSPy.
**Priority:** P1

### 11-research-pipeline-engineering  (P2)
**Scope:** Ops layer for repeatable research pipelines.
**Sub-topics:** data pipelines/ETL; experiment tracking; model registry/lineage; drift
& retraining; reproducibility infra.
**Sources to mine:** "Designing Data-Intensive Applications" (relevant chapters);
MLflow/W&B docs; dvc; reproducibility checklists.
**Priority:** P2

### 12-tooling-landscape  (P1)
**Scope:** Frameworks and tools to build with.
**Sub-topics:** orchestration frameworks (LangGraph, LlamaIndex, DSPy, AutoGen); search
APIs; scrapers (crawl4ai); converters (markitdown); MCP / agent-tool integration.
**Sources to mine:** crawl4ai (unclecode/crawl4ai); markitdown (microsoft/markitdown);
MCP spec (modelcontextprotocol.io); LangGraph/LlamaIndex/DSPy docs.
**Priority:** P1

### 13-reference-systems-case-studies  (P1)
**Scope:** Concrete systems to teardown beyond #5.
**Sub-topics:** open-source research agents; production write-ups; postmortems.
**Sources to mine:** engineering blogs (Anthropic, Perplexity); notable GitHub repos.
**Priority:** P1

### 14-papers  (P1)
**Scope:** Canonical papers underpinning the field.
**Sub-topics:** RAG, agents, retrieval, eval, KG papers.
**Sources to mine:** arXiv (RAG/agents/eval); collect per-topic during deep dives.
**Priority:** P1

### 15-textbooks-longform  (P2)
**Scope:** Long-form references for depth.
**Sub-topics:** research methods texts; ML/IR textbooks.
**Sources to mine:** "Introduction to Information Retrieval" (Manning); research-methods
textbooks.
**Priority:** P2

### 16-evaluation-benchmarks  (P1)
**Scope:** How research-system quality is measured.
**Sub-topics:** research-QA benchmarks; faithfulness/groundedness metrics; agent
benchmarks.
**Sources to mine:** RAGAS; TruthfulQA; HotpotQA / multi-hop QA; GAIA; BrowseComp.
**Priority:** P1

### 17-specs-standards  (P2)
**Scope:** Interop & format standards.
**Sub-topics:** citation formats (BibTeX/CSL); schema.org; ADR formats; MCP schema.
**Sources to mine:** CSL spec; schema.org; MADR schema; MCP spec.
**Priority:** P2

## Research Phases
1. **Breadth scan** — one gather pass per category (P0 first), capture canonical sources.
2. **Deep dives** — P0 categories full-text gather + ingest (start: 05, 06, 07, 09).
3. **Synthesize** — per-topic findings → `docs/findings/`, roll up into `SYNTHESIS.md`.
4. **Graph** — graphify the corpus, surface god nodes, flag gaps, re-scan as needed.
