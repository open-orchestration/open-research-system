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
