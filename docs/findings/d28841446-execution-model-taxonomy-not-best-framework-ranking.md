# Agent orchestration frameworks: a durable execution-model taxonomy, not a best-framework ranking

id: d28841446
topic: 12-tooling-landscape
status: draft

The honest, durable distinction across LangGraph, LlamaIndex, DSPy and AutoGen is
their **execution / control-flow model** — graph/state-machine vs. data/query
engine vs. compile-time prompt optimizer vs. multi-agent conversation. That
taxonomy is what the corpus describes consistently and is partly anchored to
primary documentation; the comparative "best framework," rating, and benchmark
claims are vendor/blog opinion and are treated here as attributed, non-load-bearing.
This provenance split matters because seven of the eight corpus sources are blogs,
listicles, or SEO research-marketing; only Microsoft Learn is an official doc, and
the DSPy arXiv paper referenced second-hand is **not** in the corpus.

## Provenance ledger (read first)

- Of eight sources, exactly one is a primary publisher: **Microsoft Learn**
  (`learn.microsoft.com/en-us/agent-framework`), official documentation for the
  Microsoft Agent Framework [cd8246394]. The other seven are blogs/listicles:
  a personal blog (youngju.dev) [ceffb4254], two posts on the agentmarketcap.ai
  blog [c16f75073][c1fcdd537], two Medium posts [cfa5d5702][c5a8a3639], an
  AIMultiple research-marketing page [c8bb89d7e], and a chatforest.com "14
  frameworks compared" review listicle [c9929aba1].
- Consequently, load-bearing claims below are limited to (a) the *shape* of each
  execution model, which the blogs describe convergently and which the one primary
  doc corroborates for the framework-vs-raw-SDK axis [cd8246394], and (b) the
  framework-vs-SDK abstraction tradeoff stated in official docs [cd8246394].
  All ratings, download counts, latency percentages, and "best for X" verdicts are
  reported as **attributed blog claims**, not as established fact.

## The four execution models (the durable axis)

- **LangGraph — directed graph / state machine.** Multiple sources describe it
  identically: agent systems are modeled as a directed graph whose nodes are
  functions/agents and whose conditional edges route a typed shared state, with
  checkpointing that makes runs resumable and supports time-travel debugging
  [c16f75073][c9929aba1]. The personal-blog account adds the concrete API
  (`StateGraph`, nodes as functions, edges as conditions, state accumulated via
  reducers, `graph.compile(checkpointer=...)`) and frames LangGraph as the
  LangChain team's own state-graph library built for branches/loops/human-in-the-loop
  that linear chains could not express [ceffb4254]. A Medium explainer describes
  the same "graph-based orchestration" with stateful nodes and loop/branch control
  [cfa5d5702]. *Convergent across blogs; no primary LangGraph doc is in this corpus,
  so this shape is best-supported-by-multiple-blogs, not doc-anchored.*
- **LlamaIndex — data / query engine (RAG-first).** Sources consistently cast it as
  data-centric: ingest from many sources, index, then serve via query engines and
  chat engines for retrieval-augmented generation and structured extraction
  [cfa5d5702]; one blog summarizes 2026 LlamaIndex as "agents-capable but RAG-first"
  with loaders, multi-tier indexes, GraphRAG and query routing [ceffb4254]. *Blog-
  convergent.*
- **DSPy — compile-time prompt optimizer, not an orchestrator.** The clearest
  framing: DSPy treats LLM calls as typed program modules (Predict, ChainOfThought,
  ReAct) and *optimizes* them against a metric using labeled examples — you declare
  *what* the pipeline should produce and an optimizer (e.g. BootstrapFewShot,
  MIPROv2) tunes the prompts [c16f75073]. A second source reinforces that DSPy
  optimizes prompts *within* workflows rather than orchestrating agents, framing
  pipeline development as a compilation problem over Signatures + Modules + an
  Optimizer [c9929aba1]. *Blog-convergent. The DSPy foundational arXiv paper is
  cited only second-hand by a blog and is not in this corpus.*
- **AutoGen (AG2) — multi-agent conversation.** Its GroupChat model routes messages
  between agents in a conversation thread rather than a graph, so agents negotiate
  and backtrack until they converge, with native human-in-the-loop as a first-class
  primitive [c16f75073]. *Blog-only description.*

## Framework vs. raw model SDK (the one doc-anchored axis)

- The Microsoft Agent Framework documentation states what the framework abstraction
  *provides* over raw LLM calls: an agent wraps an LLM with persistent identity,
  system instructions, tools, memory, and a runtime loop; the doc explicitly frames
  the choice as raw LLM calls (full control, no dependency beyond the model SDK) vs.
  the framework (opinionated abstractions that handle common patterns at the cost of
  an added dependency), noting that raw calls leave memory and tool orchestration as
  work you must write yourself [cd8246394]. This is the only abstraction-tradeoff
  claim in the corpus resting on a primary source.
- A Medium explainer adds the conceptual distinction — frameworks impose a specific
  architecture and guide application flow, SDKs offer more flexibility — and raises
  the lock-in tension symmetrically: proprietary no-code platforms risk vendor
  lock-in, but pro-code is itself tightly coupled to specific SDKs/frameworks, so
  dependency is not unique to either choice [c5a8a3639]. *Attributed opinion.*
- The "frameworkless" case is asserted but not independently evidenced: a blog
  claims a team cut response time from 4.2s to 2.5s (~40%) by replacing a LangChain
  agent with ~200 lines of raw SDK calls, and that in its benchmarks LangChain
  consumed the most tokens/wall-clock time while LangGraph (predetermined tool per
  node) delivered the lowest latency of graph frameworks [c1fcdd537]. These numbers
  are single-blog, un-replicated anecdote/benchmark and are **non-load-bearing**.

## Convergent vs. contested

- **Convergent (load-bearing, multi-source):** the four frameworks occupy distinct
  execution models — graph/state-machine, data/query engine, compile-time optimizer,
  conversation — and are complementary rather than directly substitutable; DSPy in
  particular is positioned to be used *alongside* an orchestrator, not as a
  replacement [c16f75073][c9929aba1]. The framework-vs-raw-SDK tradeoff (abstraction
  convenience vs. control/dependency) is corroborated by primary docs [cd8246394].
- **Contested / opinion-only:** every comparative *ranking* — chatforest's 4–4.5/5
  ratings and "best for" verdicts [c9929aba1], adoption/download figures (e.g.
  "~47M PyPI downloads", "600–800 companies", DSPy "~550x cost reduction",
  "5–46% over hand-written prompts") [c9929aba1][c16f75073], and the frameworkless
  latency numbers [c1fcdd537] — comes from blogs/listicles or is relayed second-hand
  from papers not in the corpus. Treat as attributed, not as evidence.

## Implications for an open research engine choosing orchestration

- Choose on **execution model fit**, the one durable, multi-source axis: a research
  engine that needs auditable, resumable, branch/loop control with human checkpoints
  maps onto the graph/state-machine model [ceffb4254][c16f75073]; deep retrieval over
  proprietary corpora maps onto the data/query-engine model [cfa5d5702]; prompt-
  quality optimization against a metric (where labeled eval data exists) maps onto
  the compile-time-optimizer model and composes with, rather than replaces, an
  orchestrator [c16f75073][c9929aba1].
- Weigh the framework-vs-raw-SDK decision on the doc-anchored tradeoff — abstraction
  convenience (memory, tools, runtime loop handled) vs. control and minimal
  dependencies [cd8246394] — and explicitly **discount blog latency/cost/ranking
  claims** when justifying the choice, since none are independently verifiable here.

## Gaps found → re-scan

- No primary LangGraph, LlamaIndex, DSPy, or AutoGen documentation/repo is in the
  corpus; the execution-model shapes rest on convergent blogs plus one Microsoft doc.
  Re-scan official docs/repos (langchain-ai/langgraph, run-llama/llama_index,
  stanfordnlp/dspy, microsoft/autogen) to doc-anchor each control-flow model.
- The DSPy arXiv paper (referenced only second-hand) is absent; gather it to
  promote the "compile-time optimization beats hand-written prompts" claim from
  blog-relayed to peer-reviewed.
- All quantitative comparison (latency, token cost, adoption, accuracy deltas) is
  blog/listicle-sourced; a neutral, reproducible benchmark would be needed before
  any comparative performance claim could be load-bearing.
