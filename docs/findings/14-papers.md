# Findings — Papers & Canonical Write-ups

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- RAG must be evaluated as a hybrid system: retrieval and generation are distinct components with distinct failure modes, and evaluation depends on dynamic knowledge sources — so a single end-to-end score is insufficient; you measure each subsystem plus the join. — [Retrieval Augmented Generation Evaluation in the Era of Large Language Models: A Comprehensive Survey (2504.14891)](https://arxiv.org/abs/2504.14891)
- The comprehensive 2025 survey scopes RAG evaluation across four axes — system performance, factual accuracy, safety, and computational efficiency — and compiles RAG-specific datasets and frameworks via a meta-analysis of high-impact papers, i.e. evaluation is multi-dimensional, not just accuracy. — [Retrieval Augmented Generation Evaluation in the Era of Large Language Models (2504.14891)](https://arxiv.org/abs/2504.14891)
- The "Auepora" (Unified Evaluation Process of RAG) survey frames evaluation around quantifiable retrieval and generation metrics — relevance, accuracy, and faithfulness — defined over (output, ground-truth) pairs, giving a reusable evaluation skeleton rather than an ad-hoc metric grab-bag. — [Evaluation of Retrieval-Augmented Generation: A Survey (2405.07437)](https://arxiv.org/abs/2405.07437)
- Both surveys independently flag that current RAG benchmarks have limitations and that the field still needs better datasets — meaning off-the-shelf benchmarks will under-cover a real deployment's failure modes. — [Evaluation of Retrieval-Augmented Generation: A Survey (2405.07437)](https://arxiv.org/abs/2405.07437)
- Agentic RAG (planning, tool use, iterative retrieval by an agent rather than a single retrieve-then-generate pass) is recognized as a distinct, surveyed sub-field — the deep-research architecture sits on a documented research lineage, not just blog practice. — [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://ui.adsabs.harvard.edu/abs/2025arXiv250109136S/abstract)

## Convergent vs contested
- **Convergent:** Decompose evaluation by component (retrieval vs generation); faithfulness/relevance/accuracy are the recurring core metrics; current benchmarks are acknowledged as incomplete. Two of the surveys share authors (Yu, Gan, Zhang, Liu) and reinforce the same Auepora-style decomposition.
- **Contested / open:** What "good enough" thresholds are, and how to weight safety/efficiency against accuracy, are left open. The agentic-RAG survey implies iterative/agentic evaluation needs metrics beyond the static retrieve-then-generate frame, but the canonical surveys are still anchored to single-pass RAG.

## Implications for the system (Phase 2)
- Build the eval harness around the Auepora skeleton: separate retrieval metrics (relevance/recall) from generation metrics (faithfulness/accuracy), scored over (output, ground-truth) pairs, before adding any composite score.
- Treat safety and computational efficiency as first-class eval dimensions alongside accuracy, per the 2504.14891 four-axis framing — budget and refusal behavior get measured, not assumed.
- Because published benchmarks are acknowledged as incomplete, plan a project-specific golden set in addition to standard benchmarks.

## Gaps found → re-scan
- Three of five "papers" sources are near-empty stub pages (abstract/indexing landing pages: ads.harvard.edu and semanticscholar entries with ~140–220 bytes) — only 2504.14891 and 2405.07437 carry real abstract text. Re-scan to fetch full HTML/PDF bodies of the two RAG surveys and the agentic-RAG survey (2501.09136) for concrete metric formulas and dataset tables.
- No canonical agent/orchestration papers (e.g. ReAct, Toolformer, multi-agent surveys) were gathered here; targeted re-scan: "ReAct / agent planning / multi-agent LLM canonical paper arxiv" to balance the RAG-evaluation skew.
