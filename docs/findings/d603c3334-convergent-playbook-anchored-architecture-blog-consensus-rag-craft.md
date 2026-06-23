---
id: d603c3334
topic: 04-applied-research-playbooks
title: "Applied playbooks split by evidence tier: deep-research architecture is anchored to a survey and a practitioner write-up; production-RAG retrieval craft is only blog-consensus"
status: draft
---

# Applied playbooks split by evidence tier: deep-research architecture is anchored; production-RAG retrieval craft is only blog-consensus

## Provenance ledger (read first)

This corpus is sharply tiered, and the tiers must not be blurred — this domain is the most blog-prone in the engine and a prior "textbook bedrock" draft was rejected for letting blog content carry load-bearing weight.

- **c9076a7c4 — reputable / academic.** arXiv:2506.18096v2, "Deep Research Agents: A Systematic Examination And Roadmap" [c9076a7c4]. A peer-style survey with an explicit taxonomy; can carry load-bearing claims about DR-agent architecture.
- **c7be4e16f — reputable-engineering (practitioner).** AI Alliance "MCP (and Beyond) in the Enterprise" guide, write-up by Sarmad Qadri (creator of the open-source `mcp-agent` project), explicitly built on and citing Anthropic's "Building Effective Agents" [c7be4e16f]. First-party engineering experience report; can carry load-bearing orchestration claims.
- **c81451a7e — official cookbook (existence only).** OpenAI Cookbook page for the `deep_research_api` "agents" notebook [c81451a7e]. The captured page is GitHub file-tree chrome ("LoadingViewer requires iframe"); the notebook body did not render, so it anchors only the *existence* of an official deep-research-agent example, no extractable technical claim.
- **ca7ef615f — generic blog.** NKKTech (offshore dev agency) "RAG Implementation Playbook 2026" [ca7ef615f]. Detailed but vendor self-reported; non-load-bearing.
- **c67e4a6e0 — generic blog.** 47Billion (dev agency) "RAG System in Production: Why It Fails" [c67e4a6e0]. Non-load-bearing.
- **c7981aff3 — generic blog.** Developers.dev (dev agency) "Production-Ready RAG Playbook" [c7981aff3]. Non-load-bearing.
- **cdf469c3b — generic blog.** LinkedIn article "The Architect's Guide to RAG Chunking" by Yasogaran S [cdf469c3b]. Non-load-bearing.
- **cd1728c0b — MIS-FETCH, uncited.** Labelled "multi-agent system design patterns," but the captured content is the Altium Develop PCB-design software product/pricing page (zero agent/LLM/RAG content). Carries no claim in this finding.

Net: 2 reputable anchors (one survey, one practitioner) plus an official-cookbook existence marker, against 4 generic agency/social blogs and 1 mis-fetch. The architecture layer is anchored; the RAG retrieval-craft layer is honestly only convergent practitioner consensus.

## Method: the convergent deep-research playbook (anchored)

The survey systematises DR agents around a small set of axes: information acquisition contrasts **API-based retrieval vs browser-based exploration**; tools are modular (code execution, multimodal input, MCP integration for extensibility); and the core taxonomy splits **static vs dynamic workflows**, with agent composition split into **single-agent vs multi-agent** configurations [c9076a7c4]. Planning is further typed by how user intent is handled: planning-only (no clarification), intent-to-planning (clarify before planning), and unified intent-planning (generate a plan, then request user confirmation) [c9076a7c4].

The practitioner write-up independently reproduces this shape through three real iterations of an MCP-based deep-research agent: (1) a fixed orchestrator with planning, execution, and synthesis layers (taken directly from Anthropic's "Building Effective Agents" orchestrator pattern); (2) an "adaptive" workflow that defines subagents dynamically after analysing the objective, uses a FIFO TODO queue, and moves accumulated results into external memory instead of growing the context window; and (3) a "Deep Orchestrator" adding deterministic plan verification and a simple policy engine [c7be4e16f]. The convergence is the load-bearing claim: a survey taxonomy (static→dynamic, single→multi, intent-clarifying planning) and an independent build log land on the same architecture — planner/orchestrator that decomposes, parallel/dynamic subagents that execute and accumulate context, and a synthesis step [c9076a7c4][c7be4e16f]. An official OpenAI cookbook ships a deep-research-agent example in the same lineage [c81451a7e].

## Evidence: which guidance is anchored vs blog-consensus

**Anchored (reputable sources).** Two failure-mitigation moves come from the practitioner report and generalise cleanly:

- **Prefer deterministic code checks over LLM judgement wherever possible.** Plan verification — dependency-graph validation, confirming named servers/agents actually exist — is done in code *before* execution; on failure the planner is asked to re-plan. The author frames this as an Evaluator-Optimizer variant but stresses "if we can check something deterministically with code, always prefer that over doing the same with an LLM" [c7be4e16f].
- **Externalise memory; bound context deliberately.** Accumulating every prior step in the prompt binds the agent to the context window; moving results into external knowledge/memory is what made the adaptive design work [c7be4e16f]. The survey names the symmetric benchmark-side failures — sequential-execution inefficiency and restricted external-knowledge access — as real limitations of current systems [c9076a7c4].

**Blog-consensus (NOT load-bearing, attributed).** Four independent agency/social blogs converge on a production-RAG retrieval playbook. The convergence across unaffiliated authors is itself the only signal here; none of it is anchored to a primary or official source, and the quantitative results are vendor self-reported:

- **Chunking is the highest-leverage decision; fixed-size is the weak default.** Structure-aware chunking (by heading/section/row/function, with title-and-path metadata prefixed) beats naive fixed-size splitting, which "slices sentences mid-clause" [ca7ef615f][cdf469c3b]. NKKTech self-reports retrieval@5 rising 64%→91% from a fixed→structure-aware switch on a legal corpus [ca7ef615f]; treat as illustrative, not evidence.
- **Hybrid retrieval + reranking + metadata filtering, layered.** Dense vector search alone fails on exact matches (codes, section numbers, acronyms); combining it with sparse/BM25 via Reciprocal Rank Fusion, then reranking the top 20–50 candidates, then filtering by access/metadata *before* search, is the consensus stack [ca7ef615f][c67e4a6e0][c7981aff3].
- **Two-layer, eval-driven iteration.** Evaluate retriever (recall@K, MRR, NDCG@K) and generator (faithfulness, answer relevance, citation accuracy) separately, on a golden query–document set, and gate deploys on a regression eval run in CI [ca7ef615f][c7981aff3][c67e4a6e0]. n-gram metrics (BLEU/ROUGE) are explicitly called inadequate because they measure surface overlap, not factual grounding [c67e4a6e0].
- **Filter-before-search for access control.** Post-retrieval filtering is named an insecure anti-pattern; permission metadata must constrain the query itself [c7981aff3][ca7ef615f].

## Tension: anti-patterns and where the playbooks are thin

- **The "more sources / bigger model fixes it" anti-pattern.** Blogs converge that most teams over-optimise the LLM and under-invest in everything before retrieval and everything measured after generation — "garbage in, garbage out" is the data-engineering framing [c67e4a6e0][c7981aff3]. This is consensus, not measured.
- **Static-plan-upfront vs adaptive replanning is unsettled.** The fixed orchestrator worked only "for tasks where a full plan could be determined upfront"; the author iterated to dynamic subagents and a replanning policy engine precisely because static plans broke on open-ended objectives [c7be4e16f]. The survey presents static and dynamic as co-existing categories rather than ranking them [c9076a7c4] — so the choice is task-dependent, not resolved.
- **No independent RAG benchmark.** Every RAG number in this corpus (64%→91%, +23 points from hybrid+rerank+filter, ">80% chunk-coverage" targets) is a single agency's self-report on private client data [ca7ef615f][cdf469c3b]; no source independently reproduces them.
- **The official cookbook gap.** The one OpenAI primary source in this corpus did not render its body [c81451a7e], so the most authoritative would-be anchor contributes only existence, not method.

## Application to this engine

- The engine already implements the anchored architecture: an orchestrator-worker spine with parallel subquestioning and a separate citation/provenance pass — exactly the convergent shape [c9076a7c4][c7be4e16f]. The transferable additions are the two practitioner moves: **deterministic pre-execution checks** (this drafter's own `cite_check.py` and graph-node verification are instances of "check it in code, not with an LLM" [c7be4e16f]) and **externalised memory with bounded context** rather than accumulating every step in-prompt [c7be4e16f].
- Adopt the blog-consensus RAG craft as *engineering defaults to test*, never as cited authority: structure-aware chunking with path metadata, hybrid + rerank + filter-before-search, and a two-layer eval gate (retrieval recall@K + generator faithfulness) run in CI [ca7ef615f][c67e4a6e0][c7981aff3][cdf469c3b]. Any of these claims needs a primary/peer-reviewed source before it can be load-bearing in a promoted finding — the RAG-retrieval and grounding domains (06, 08) are where that anchoring already lives.
