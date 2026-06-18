# open-research-system — Research-Spike Spec (Phase 1)

**Date:** 2026-06-17
**Status:** Approved (brainstorming) — pending implementation plan
**Sibling reference:** `/Users/joshua/Documents/GitHub/open-job-system` (same build philosophy: catalog → gather → synthesize → distill; different domain)

## 1. Purpose

Build the **knowledge base for a definitive source-of-truth on how to do research →
build concrete decisions → compile into actionable knowledge**, with a focus on
AI-assisted research. The repo is the *rulebook*; it does **not** host individual
research projects (those run outside it, phase 2+).

This spec covers **Phase 1: the research spike** only. We mirror how open-job-system
was actually built — catalog the field, gather the best sources, synthesize — so the
eventual system architecture emerges from evidence rather than from a premature guess.

### Two-phase framing
- **Phase 1 (this spec):** research spike. Produce a cataloged, gathered, synthesized,
  graph-modeled knowledge corpus on building AI research systems + research methodology.
- **Phase 2 (later, separate spec):** design + build the actual system (reference
  architecture, run template, scaffolder, agents) — *derived from* phase-1 findings.

The earlier brainstorm (6-stage non-linear spine, MADR decision unit, graphify
node/edge schema) is **not** a phase-1 commitment. It is recorded in Appendix A as a
**working hypothesis** the spike tests and refines.

## 2. Goals / Non-Goals

### Goals
- `RESEARCH-CATALOG.md` — the 17-category taxonomy of the field + sources to mine +
  phased research plan (cloned *shape* from the sibling, domain swapped).
- `docs/NN-topic/` — gathered/curated source material per category.
- `ingest/` — drop-zone contract for files already in hand → markitdown → corpus.
- `SYNTHESIS.md` (+ per-topic findings) — distilled, cited knowledge.
- graphify over the corpus — god nodes / nodes / edges relational view.

### Non-Goals (Phase 1)
- No system build: no reference architecture, no run template, no scaffolder, no
  production agents. Those are Phase 2.
- **Loop-engineering / orchestration** — cataloged as a *topic to research* (#7), but
  not built.
- No web UI, no database — files + graphify only.
- This repo never holds per-topic run outputs.

## 3. Repository layout (Phase 1)

```
open-research-system/
├── README.md                      # what this is, spike status, how to navigate
├── RESEARCH-CATALOG.md            # 17-category taxonomy + sources + research phases
├── SYNTHESIS.md                   # distilled cross-topic findings (grows during spike)
├── ingest/                        # drop-zone for files in hand (PDF/docx/… )
├── docs/
│   ├── 01-methodology-epistemics/
│   ├── 02-statistical-causal-inference/
│   ├── 03-decision-frameworks/
│   ├── 04-applied-research-playbooks/
│   ├── 05-ai-deep-research-systems/
│   ├── 06-rag-retrieval/
│   ├── 07-agentic-orchestration/
│   ├── 08-grounding-truth/
│   ├── 09-knowledge-compilation-graphs/
│   ├── 10-context-prompt-engineering/
│   ├── 11-research-pipeline-engineering/
│   ├── 12-tooling-landscape/
│   ├── 13-reference-systems-case-studies/
│   ├── 14-papers/
│   ├── 15-textbooks-longform/
│   ├── 16-evaluation-benchmarks/
│   ├── 17-specs-standards/
│   ├── findings/                  # per-topic synthesized findings (cited)
│   ├── diagrams/
│   └── superpowers/specs/         # this spec + future specs
├── scripts/
│   ├── gather.sh                  # drives crawl4ai deep-research workflow per topic
│   └── ingest.sh                  # markitdown convert ingest/ → docs sources, index
└── graphify-out/                  # graphify report over the corpus (committed)
```

`.graphify/` caches gitignored; `graphify-out/GRAPH_REPORT.md` committed (match sibling).

## 4. The 17-category catalog

`RESEARCH-CATALOG.md` defines, for each category: scope, key sub-topics, named sources
to mine, and priority. Categories:

1. **Research methodology & epistemics** — framing, search strategy, source
   credibility/bias, claim extraction, synthesis, verification; primary/qualitative
   methods (interviews, surveys, ethnography, sampling, triangulation).
2. **Statistical & causal inference** — significance/p-values, effect size, Bayesian
   vs frequentist, causal inference, experimental design & power, Monte Carlo.
3. **Decision-making frameworks** — MADR/ADR, decision matrices, analysis of competing
   hypotheses; risk modeling, stress/scenario/sensitivity analysis.
4. **Applied research playbooks** — competitive teardown, market/TAM sizing,
   trend/weak-signal, cohort/retention, A/B experimentation, idea validation,
   SEO/intent, systematic literature review.
5. **AI deep-research systems** — deep-research agents, STORM, GPT-Researcher,
   Perplexity/Elicit-class (teardowns).
6. **RAG & retrieval architectures** — naive→advanced, GraphRAG, agentic RAG,
   embeddings/vector stores, hybrid search, rerankers.
7. **Agentic orchestration** — planner-worker, fan-out/verify, debate/critique,
   loop-engineering; reward/policy design (RL: exploration, PPO/offline/inverse);
   shared context/state stores.
8. **Grounding & truth** — citation/attribution, hallucination mitigation,
   LLM-as-judge, eval; research-output quality/style auditing.
9. **Knowledge compilation & graphs** — source-of-truth maintenance, knowledge-graph
   construction (god nodes/nodes/edges), synthesis→decision, retrieval-optimized stores.
10. **Context & prompt engineering for research** — context engineering, CoT/ToT/ReAct,
    long-context vs RAG.
11. **Research-pipeline engineering** — data pipelines/ETL, experiment tracking, model
    registry/lineage, drift/retraining, reproducibility infra.
12. **Tooling landscape** — frameworks (LangGraph/LlamaIndex/DSPy), search APIs,
    scrapers (crawl4ai), converters (markitdown); MCP / agent-tool integration.
13. **Reference systems / case studies** — concrete systems to teardown.
14. **Papers & canonical write-ups.**
15. **Textbooks & long-form references.**
16. **Evaluation & benchmarks** — research-QA benchmarks, faithfulness metrics.
17. **Specs / standards** — citation formats, schema, interop.

## 5. Gathering engine

- **Web gather:** route through the throttle-proof crawl4ai-wired deep-research
  workflow at `/Users/joshua/.claude/workflows/deep-research-crawl4ai.js`
  (search + fetch + verify off the harness web path). `scripts/gather.sh` wraps it per
  category/topic; output lands in the matching `docs/NN-topic/`.
- **Ingest:** files dropped in `ingest/` → `markitdown <in> -o <out>.md` → indexed via
  context-mode; never raw-read into context (per user global instructions). Becomes
  source material for the relevant topic dirs.
- **Context discipline:** large gather output processed with context-mode
  (`ctx_execute_file` / `ctx_search`); only derived findings enter the working context.

## 6. Synthesis & graph

- Per-topic findings written to `docs/findings/` with citations back to gathered
  sources; cross-topic distillation accrues in `SYNTHESIS.md`.
- graphify run over the corpus produces the relational model: sources, claims,
  findings, topics as nodes; cites/supports/refutes/informs as edges; high-centrality
  hubs surfaced as god nodes (e.g. the architectures and methods everything references).
- The graph is the bridge to Phase 2: god nodes + dense clusters indicate the load-
  bearing concepts the eventual system architecture must be built around.

## 7. Suggested research phases (executed under a later plan)

1. **Breadth scan** — one pass per category: map the landscape, capture canonical
   sources, name the systems/papers worth deep dives.
2. **Deep dives** — prioritized categories (5, 6, 7, 9 first — the AI-research-system
   core), full-text gather + ingest.
3. **Synthesize** — per-topic findings → `SYNTHESIS.md`.
4. **Graph** — graphify the corpus, identify god nodes, flag gaps → re-scan as needed.

## 8. Definition of done (Phase 1)

- `RESEARCH-CATALOG.md` complete (17 categories populated with sources).
- Each `docs/NN-topic/` has gathered material for at least the breadth scan.
- `SYNTHESIS.md` captures the cross-cutting findings.
- graphify report committed with god nodes identified.
- A short "Phase 2 requirements" note distilled from the synthesis (what the real
  system must do), seeding the next spec.

## Appendix A — Working hypothesis (NOT a Phase-1 commitment)

Captured from brainstorming; to be validated/refined by the spike, then formalized in
the Phase-2 design:

- **6-stage non-linear spine:** Scope → Gather → Evaluate → Synthesize → Decide →
  Compile, with feedback edges (any stage may re-scope on a discovered gap; dynamic
  adjust + scale).
- **Decision unit:** MADR 4.0 ADR, consistent with the sibling repo.
- **graphify schema (candidate):** node types Topic/Source/Claim/Finding/Decision/
  Option/Gap; edge types cites/supports/refutes/synthesizes/informs/weighs/supersedes/
  raises/rescopes/derives_from; god nodes = high-centrality hubs from community
  detection.
- **Phase-2 shape (candidate):** two-plane repo (normative `docs/` + operational
  `tooling/`), reusable run template, `new_project.py` scaffolder stamping runs to an
  external path, thin stage-aligned agents/skills.
