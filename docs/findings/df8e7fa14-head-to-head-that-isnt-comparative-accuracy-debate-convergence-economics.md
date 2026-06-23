---
status: draft
topic: 07-agentic-orchestration
id: df8e7fa14
---

# The head-to-head that isn't: comparative accuracy, debate convergence, and per-iteration economics of self-correcting agent loops

A practitioner choosing between self-correction strategies (ReAct, Reflexion,
CRAG, Self-RAG) or deciding how to run a multi-agent debate wants three numbers:
which method is *more accurate*, when a debate has *converged*, and what each
extra iteration *costs*. This finding establishes which of those numbers are
actually backed by primary evidence in this corpus — and the load-bearing result
is that the promised clean "head-to-head accuracy benchmark" does not exist here.
What *is* primary-sourced is narrower but stronger: a RAG accuracy *ceiling*, and
a controlled debate-protocol study showing convergence is a tunable design choice,
not an emergent property of "more rounds."

## Sub-questions framed

1. **Provenance:** For the comparative-accuracy claim, which sources are primary
   papers vs. blogs/aggregators/synthetic tutorials, and is a same-benchmark
   head-to-head of ReAct/Reflexion/CRAG/Self-RAG actually available?
2. **Method (debate):** How does a controlled study decide when a debate has
   converged, what role does the judge play, and how many rounds?
3. **Evidence (accuracy):** What accuracy numbers rest on genuine primary sources,
   and under what setup?
4. **Economics:** What does an extra self-correction iteration cost, and how
   trustworthy are those numbers?
5. **Application:** Given only the verifiable evidence, what should an open engine
   adopt?

## Key claims (cited)

### The promised head-to-head accuracy benchmark is not in this corpus

- The corpus item whose filename advertises a "reproducible head-to-head accuracy
  benchmark — ReAct vs Reflexion vs CRAG vs Self-RAG / PopQA / TriviaQA" resolves
  to **three different publishers, none of which run that comparison.** The first
  is the arXiv *CRAG — Comprehensive RAG Benchmark* paper (arXiv:2406.04744, NeurIPS
  2024 Datasets and Benchmarks Track), which benchmarks RAG systems generally, not
  the four named loop strategies against each other [c1acffb70]. The second is a
  marktechpost *tutorial* whose "benchmark" is a **simulated mock**: each strategy's
  score is computed as `base_confidence = 0.7` plus a fixed per-strategy bonus plus
  `np.random.uniform(-0.1, 0.1)` — i.e. random numbers, not LLM outputs on PopQA or
  TriviaQA [c764cbe7d]. The third is the *llm-stats.com* CRAG leaderboard, an
  aggregator page restating the CRAG benchmark, not an originating experiment
  [c8393450b].
- Consequently, **no apples-to-apples ReAct-vs-Reflexion-vs-CRAG-vs-Self-RAG
  accuracy table on a shared dataset is available from these sources.** The
  per-method accuracy figures that do appear are each from a *different* originating
  paper and *different* benchmark (e.g. Reflexion on HumanEval/AlfWorld, ReWOO on
  HotpotQA), reported second-hand, and therefore cannot be lined up as a fair
  comparison [c6e7ab381].

### The accuracy numbers that *are* primary-sourced describe a ceiling, not a ranking

- From the CRAG paper directly (primary): most advanced LLMs alone reach **≤34%**
  accuracy on CRAG; adding RAG "in a straightforward manner" raises this **only to
  44%**; and **state-of-the-art industry RAG solutions answer only 63% of questions
  without any hallucination** [c1acffb70]. This is a ceiling on RAG factual QA
  generally — it says nothing about which *self-correction loop* is best.
- The per-method accuracy deltas in the corpus are blog-relayed restatements of
  originating papers, not primary: Reflexion improved GPT-4's HumanEval pass rate
  **from 80% to 91%** and ReAct+Reflexion completed 130/134 AlfWorld tasks; ReWOO
  reported **5x token efficiency and a 4% accuracy improvement on HotpotQA** vs
  ReAct [c6e7ab381]. These are useful directional signals but rest on a Substack
  practitioner article (The AI Engineer / Paolo Perrone), so they are carried as
  attributed, not as primary head-to-head evidence [c6e7ab381].

### Multi-agent debate convergence is a tunable design choice, decided by the judge

- A controlled study (arXiv:2603.28813, primary) isolates *protocol* effects from
  *model* effects by holding model/prompts/decoding fixed and varying only the
  debate protocol across **20 events × 5 seeds (n=100 matched runs)**: Within-Round
  (agents see only current-round peers), Cross-Round (full prior-round context),
  Rank-Adaptive Cross-Round (a judge model reorders agents and silences one per
  round), and a No-Interaction baseline [c7de7f558].
- Convergence ("Consensus Formation") is **not** maximized by more peer visibility.
  RA-CR reaches the highest consensus (mean **0.647**, 95% CI [0.555, 0.734]),
  far above Cross-Round (**0.359**), Within-Round (**0.434**), and the
  No-Interaction baseline (**0.325**) [c7de7f558]. The paper frames this as a
  **trade-off between interaction and convergence**: Within-Round produces the
  highest peer-referencing (0.320) but No-Interaction produces the highest argument
  diversity (0.717) — i.e. the protocol that talks the most is not the one that
  agrees the fastest [c7de7f558].
- The **judge is structural, not advisory.** One judge model (mistral) plays two
  roles: a condition-uniform intra-turn reranker that picks the better of two
  candidate drafts per turn in *every* protocol, and an adaptive controller that, in
  RA-CR only, ranks agents for the next round and silences the lowest each round
  [c7de7f558]. Convergence is thus an engineered output of judge-driven scheduling,
  not an emergent property of letting agents talk longer.

### Per-iteration economics are vendor/practitioner estimates, not measured benchmarks

- A practitioner blog models the cost of self-correction explicitly: single-pass RAG
  ≈ **$0.003/request**; agentic RAG at a 2-iteration average ≈ **$0.006** (~2x); and
  a 4-iteration worst case ≈ **$0.010** (~3–4x), driven mostly by repeated reflection
  and a larger accumulated-context generation call [cc583c0d6]. The same source notes
  the blended cost depends entirely on routing: ~25% of traffic on the agentic path
  at 2.5x average ≈ +37% total cost (acceptable); ~75% on the agentic path ≈ triple
  cost [cc583c0d6].
- These dollar figures are illustrative model estimates from a single author's blog
  (aloknecessary.github.io), not measured production telemetry, and are carried as
  attributed and non-load-bearing [cc583c0d6]. Two vendor sources corroborate the
  *direction* (per-iteration overhead is real and must be controlled) without adding
  independent measured numbers: a GreenNode guide on measuring and controlling
  inference cost for RAG/agents [c8c70c097] and an n1n.ai / Towards Data Science piece
  on caching architectures to cut the latency and token cost of agentic RAG
  iterations [ce3791ef9].

## Tension / what is genuinely uncertain

- **The "head-to-head" framing is unsupported.** Treating ReAct/Reflexion/CRAG/
  Self-RAG accuracy figures as comparable is a category error here: they come from
  different papers, benchmarks, and base models, relayed by a blog [c6e7ab381], plus
  a simulated tutorial whose numbers are literally `np.random` [c764cbe7d].
- **Domain narrowness of the debate result.** The convergence numbers are from a
  single-domain (macroeconomic forecasting) case study with one judge model and
  n=100 matched runs; the authors themselves frame it as a controlled case study,
  so the RA-CR > CR consensus advantage should not be over-generalized [c7de7f558].
- **Cost numbers are model estimates, not measurements.** The 2x–4x multiplier is an
  author's per-request cost model, not benchmarked spend [cc583c0d6].

## Application — what an open engine should adopt

- **Do not advertise or rely on a self-correction accuracy ranking.** The honest
  state of evidence is a RAG *ceiling* (≤34% LLM-only → 44% naive RAG → 63% SOTA
  without hallucination [c1acffb70]) plus per-method, per-benchmark anecdotes
  [c6e7ab381]. Pick a loop by failure mode and cost profile, not by a comparative
  accuracy table that this corpus cannot supply.
- **If running multi-agent debate, treat convergence as a scheduled output.** Use a
  judge to rank and silence agents (the RA-CR pattern) when consensus is the goal,
  and accept the diversity trade-off; do not expect more rounds or more peer
  visibility to converge a debate on their own [c7de7f558].
- **Budget self-correction by routing, not by hope.** Plan for a ~2x–4x per-request
  cost multiplier on the agentic path and gate the share of traffic that takes it
  [cc583c0d6]; pair this with caching to recover repeated-iteration cost
  [ce3791ef9] and explicit inference-cost measurement [c8c70c097].
