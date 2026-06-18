# Findings — Grounding & Truth

**Question:** What does this category teach for building an AI research system?

> **Source-set note:** This topic has only 4 gathered source files (an earlier arXiv collision dropped one). Claims below are drawn from those four; coverage of citation-attribution mechanics is thinner than other topics.

## Key claims (cited)
- Faithfulness is the share of answer statements grounded in the retrieved context: `faithfulness = (statements supported by context) / (total statements in answer)`. RAGAS computes it by using an LLM to decompose the answer into atomic statements and verify each against the context, so a half-supported answer scores 0.5 — [Master LLM Evaluation: RAGAS and LLM-as-Judge](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals)
- Faithfulness alone misses retrieval-noise failures: RAGAS v0.2+ adds Noise Sensitivity (incorrect claims from irrelevant retrieved chunks) and Context Entity Recall (whether critical named entities appear in context) to catch failure modes faithfulness does not — [Master LLM Evaluation: RAGAS and LLM-as-Judge](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals)
- LLM-as-judge carries quantified, systematic biases: verbosity bias inflates scores ~15% for longer answers, GPT-4 shows ~40% inconsistency when a pairwise comparison is reversed (position bias), plus self-enhancement bias — so judges must be validated, comparisons run twice with positions swapped, and a model should never judge its own outputs against competitors without human validation — [Master LLM Evaluation: RAGAS and LLM-as-Judge](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals)
- Ensembling judges reduces single-judge bias: the FACTS Grounding leaderboard uses three LLM judges; Vectara's FaithJudge similarly finds multiple judges can improve effectiveness, though individual strong judges (o3-mini-high) sometimes beat the majority vote on specific subsets — [Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards](https://arxiv.org/html/2505.04847v1)
- FaithJudge leverages human hallucination annotations to outperform automated detectors (including Vectara's own HHEM model) and produces leaderboard rankings across 30 models — i.e., human-annotated reference hallucinations meaningfully sharpen automated faithfulness scoring — [Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards](https://arxiv.org/html/2505.04847v1)
- Statement-level, attribution-aware evaluation (scoring grounding, provenance, and conflict-handling per atomic statement, with tool-specific provenance embedded) gives a more reliable trust signal than output-only quality scores — [Evaluating Faithfulness in Agentic RAG Systems for e-Governance Applications](https://www.mdpi.com/2504-2289/9/12/309)
- In a production agentic-RAG e-governance build, the triple-extraction stage hit 0.999 precision / 0.962 recall / 0.980 F1 over 1591 triples — high precision keeps hallucinations near-zero, and high recall ensures comprehensive coverage; faithfulness was scored by three independent judges (GPT-4.1, Claude Sonnet-4.0, Gemini 2.5 Pro) at temperature 0 for reproducibility — [Evaluating Faithfulness in Agentic RAG Systems for e-Governance Applications](https://www.mdpi.com/2504-2289/9/12/309)
- A continuous evaluation loop — sample production traffic, compute faithfulness and relevancy daily, gate deployments on a regression suite, and route low-scoring responses to human review — is what separates a system that drifts toward hallucination from one that stays reliable — [Master LLM Evaluation: RAGAS and LLM-as-Judge](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals)

## Convergent vs contested
- **Convergent:** Faithfulness must be measured at the atomic-statement level against retrieved context; LLM judges have real, measurable biases and need multiple judges + human validation + deterministic (temp 0) config; grounding evaluation should be a continuous gate, not a one-off.
- **Contested / open:** Whether ensembling judges always beats a single strong judge is unsettled (individual models sometimes win per-subset). RAG grounding reduces but does not eliminate hallucination — even GraphRAG suffers noise propagation and entity-resolution errors — so no source claims a solved problem.

## Implications for the system (Phase 2)
- Make faithfulness an atomic-statement metric over the exact retrieved context, and pair it with noise-sensitivity and entity-recall so retrieval failures surface separately from generation failures.
- Use a multi-judge ensemble at temperature 0, swap positions on pairwise comparisons, and forbid self-judging; keep a human-annotated reference set to calibrate the judges.
- Wire grounding evals into a deployment gate (regression suite) and a daily production sample with human review of low-scoring outputs.
- Treat citation attribution as a first-class, per-statement provenance step (the CitationAgent in topic 07) rather than a post-hoc formatting pass.

## Gaps found → re-scan
- Only 4 sources, and citation/attribution *mechanics* (how to anchor a claim to a precise source span) are described conceptually but not implemented in detail. Re-scan: "citation span attribution claim-to-source anchoring grounding generation".
- No coverage of conflicting-source resolution policy at scale. Re-scan: "conflicting sources contradiction resolution trust weighting research synthesis".
