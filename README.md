# open-research-system

Definitive source-of-truth for **AI-assisted research → decisions → actionable knowledge**.

> **Status:** Phase 1 — research spike. Cataloging the field, gathering sources,
> synthesizing. The system itself (template, scaffolder, agents) is Phase 2, built
> from what this spike learns. Sibling repo: `open-job-system`.

## Layout
- `RESEARCH-CATALOG.md` — the 17-category taxonomy, sources to mine, research phases.
- `docs/NN-topic/` — gathered source material per category.
- `docs/findings/` — synthesized, cited findings.
- `SYNTHESIS.md` — cross-topic distillation.
- `ingest/` — drop local files (PDF/docx/…); `scripts/ingest.sh` converts them.
- `scripts/gather.sh` — drives the crawl4ai deep-research workflow per topic.
- `.graphify/` — relational model of the corpus (god nodes/nodes/edges); generated, gitignored.

## Quickstart
1. Drop files into `ingest/`, run `scripts/ingest.sh`.
2. Gather a topic: `scripts/gather.sh 06-rag-retrieval "advanced RAG architectures 2025"`.
3. Synthesize into `docs/findings/` and `SYNTHESIS.md`.
4. Run graphify; review `.graphify/GRAPH_REPORT.md`.

### Continuous ingest loop
- Drop sources (files/links/videos/raw text) into `ingest/`.
- `scripts/ingest_flow.sh <topic>` normalizes them into `docs/<topic>/sources/`, records each in `.research/state.json` with a durable id + lifecycle, and flags the graph dirty.
- The graph is updated incrementally (graphify `--update`); deltas append to `.research/graph-events.jsonl` (the realtime-view feed + audit log).
- Run the loop hands-off with `/loop` (uses `.claude/loop.md`).

### Autonomous search loop
- Queue a research gap: `python3 scripts/state.py add-gap --topic 06-rag-retrieval --desc "hybrid retrieval rerank 2025"`.
- `scripts/search_flow.sh --topic <T>` drains that topic's queued gaps within the source budget (`budget.sources_per_cycle`): it searches + fetches via crawl4ai, drops non-junk results into `ingest/`, and marks each gap done (or re-queues it; failed after 3 attempts).
- Search is run **per topic** so the ingest flow routes each batch correctly: for every topic with queued gaps, run `scripts/search_flow.sh --topic <T>` then `scripts/ingest_flow.sh <T>`.
- Reset the per-cycle budget with `python3 scripts/state.py budget-reset`; inspect it with `python3 scripts/state.py budget-status`.
- Run hands-off on a slow interval, e.g. `/loop 10m for each topic with queued gaps, run scripts/search_flow.sh --topic <T> then scripts/ingest_flow.sh <T>`.
