---
id: d0651b724
topic: 04-applied-research-playbooks
title: "The definitive deep-research agent architecture: planner-executor-publisher spine, the retrieval choice underneath it, the orchestration primitive that runs it, and the one axis on which it can be benchmarked"
status: draft
---

# The definitive deep-research agent architecture: planner-executor-publisher spine, the retrieval choice underneath it, the orchestration primitive that runs it, and the one axis on which it can be benchmarked

A deep-research agent is not one design decision but four stacked ones, and eight prior
findings each pin down a layer. This synthesis composes them into a single durable answer
to: *what is the canonical control-flow spine, what retrieval sits under it, which
orchestration primitive runs it, and how the whole thing can honestly be benchmarked.* It
draws on `da592d4f8` (GPT-Researcher's documented internals), `dbc0e9395` (STORM's
paper-backed pipeline vs. GPT-Researcher, with provenance tiering), `d603c3334` (the
convergent blog-consensus playbook), `d6ccd6b1c` (ColBERT late-interaction economics),
`dc97efcf9` (hybrid / contextual retrieval tradeoffs), `d1fb5a112` (LangGraph vs. AutoGen
dispatch primitives), `d28841446` (the orchestration execution-model taxonomy), and
`d369c3d06` (benchmark accuracy as the only cross-vendor comparable). The contribution
here is the *stack*: how the spine, the retrieval engine, the orchestration primitive, and
the benchmark nest into one system, where reference systems genuinely converge, and where
they only appear to.

## Provenance note

Every load-bearing claim below is anchored on a strong primary — a named paper or an
official framework doc, cited inline as `[c<id>]`: GPT-Researcher's official README
[c1bb33cc6] and its official LangGraph multi-agents docs [cb547d339] (with the prior
docs-landing-page capture [cfc0c8e73] used only where it is the supporting source); the
STORM paper [c3bf6d346] [c9c58e239] and Stanford OVAL's first-party project page
[c2713ec8f]; the ColBERT paper (arXiv:2004.12832) [cbb096e41] and ColBERTv2
(arXiv:2112.01488) [c7b11e5a5]; the LangGraph Graph-API docs [cc413ffed] and Microsoft's
AutoGen core docs [cce59d029]; and, for the benchmark layer, vendor-neutral aggregator
leaderboards that collect BrowseComp scores [c2713d958] [cc9ebf39f], a secondary
deep-research market write-up that reports the same scores [ceb7cfb9f], and the
*Deep Research Agents* survey (arXiv:2506.18096) [cbda2cb4e]. Sibling findings (`d…` ids)
are referenced in prose only to map territory; they are never the citation of record.
Where a primary is a third-party code-wiki rather than the paper (the STORM
`StormInformationTable` pipeline) it is marked as such inline. Numeric claims were
verified whitespace-insensitively against the source bytes; two ColBERT figures
(`61` ms re-rank latency, `7B` FLOPs/query) are read from the paper's results table whose
column headers are "Re-ranking Latency (ms)" and "FLOPs/query". ColBERT's abstract phrasing
("two orders-of-magnitude faster", "four orders-of-magnitude fewer FLOPs per query") is
rendered run-together in the paper's PDF→markdown extraction and is quoted here in its
canonical spaced form; the component tokens are byte-verified.

## The spine — planner → executor → publisher is the settled pattern, and reference systems converge on it

The canonical control flow has three stages, and GPT-Researcher's README states it in the
project's own words: "the core idea is to utilize 'planner' and 'execution' agents — the
planner generates research questions, while the execution agents gather relevant
information," after which "the publisher then aggregates all findings into a comprehensive
report" [c1bb33cc6]. At a finer grain the same source documents the executor loop as: use a
crawler agent to gather information for each question, summarize-and-source-track each
resource, then filter-and-aggregate summaries into the final report [c1bb33cc6]. That is the
**decompose → gather-per-question-with-provenance → aggregate** spine, and it is the
open-source precedent for the pattern (`da592d4f8`).

STORM is a different system that lands on the *same* two-phase spine from the academic side.
The paper decomposes long-form grounded writing into a **pre-writing** stage that researches
the topic, collects references, and produces an outline, and a **writing** stage that
generates the article with citations *from those collected references* [c3bf6d346]
[c9c58e239]; Stanford OVAL's project page restates the same two-stage framing in first-party
prose [c2713ec8f]. The convergence is real and is the load-bearing claim of this section:
both a production OSS agent [c1bb33cc6] and a peer-reviewed system [c3bf6d346] separate a
gather-references phase from a write-only-from-references phase. This is why `dbc0e9395`
treats the "research-then-write" split as the strongest-evidenced pattern in the corpus, and
practitioner blogs converge on the same spine as a matter of consensus (`d603c3334`) — but
the consensus is not the citation of record; the two primaries are.

## Where reference systems genuinely DIVERGE — outline-driven breadth vs. plan-then-execute, and the review gate

The spine is shared; the *mechanism that generates breadth* and the *quality gate* are not.

**Breadth mechanism.** STORM generates coverage by **multi-perspective question asking**:
it discovers diverse perspectives on the topic and simulates conversations in which writers
carrying different perspectives interrogate a topic expert grounded on trusted sources, then
curates that into an outline [c3bf6d346] [c9c58e239]. The paper measures the payoff: against
an outline-driven retrieval-augmented baseline, more of STORM's articles are judged
**organized (by a 25% absolute increase) and broad in coverage (by 10%)** [c3bf6d346]. That
is direct evidence that *perspective diversity*, not retrieval volume, drives organized and
broad output. GPT-Researcher instead generates breadth by **plan-then-execute
sub-questioning** — the planner emits research questions and execution agents fan out per
question [c1bb33cc6]. Same goal (breadth), different generator (simulated multi-perspective
dialogue vs. a planned question set).

**The quality gate, and provenance tiering.** GPT-Researcher's multi-agent variant makes
review a *first-class, named stage*: its official docs define a seven-role editorial team —
Chief Editor, Researcher (gpt-researcher), Editor, Reviewer, Revisor, Writer, Publisher —
in which the **Reviewer validates the correctness of the research results against a set of
criteria** and the **Revisor revises based on that feedback** [cb547d339]. Its parallelism
unit is **per-outline-topic**: after a single planning pass, the team fans research +
review + revise across outline topics in parallel [cb547d339] — a cheaper fan-out unit than
per-question. STORM has no such adversarial gate and the paper is explicit about why one is
needed: even when grounded, STORM still exhibits source-bias transfer and over-association
[c3bf6d346], so grounding is necessary but insufficient and a faithfulness/citation gate
downstream of retrieval is warranted (`dbc0e9395`). The honest provenance line: the
fine-grained role list and review gate rest on official docs [cb547d339] [c1bb33cc6], while
GPT-Researcher's self-reported run economics — **~5 minutes and ~$0.4 per deep-research run
using `o3-mini` at "high" reasoning effort** [c1bb33cc6] — are a vendor self-report for one
recursive workflow, not a measured cost model.

## The retrieval choice underneath the spine — late interaction vs. hybrid, grounded in the primaries

The executor's gather step is a retrieval problem, and the durable choice is between
**late-interaction** retrieval and **hybrid lexical+dense** retrieval.

**When late interaction (ColBERT) earns its place.** ColBERT independently encodes query and
document into bags of per-token embeddings and scores relevance as a sum, over query tokens,
of the maximum cosine similarity ("MaxSim") to the document's embeddings [cbb096e41]. Because
the document side is query-independent, every document is fed through BERT **once, offline**
at indexing time, collapsing per-query cost to embedding transfer plus a pruning-friendly
MaxSim [cbb096e41]. The paper frames the payoff in its abstract as being competitive with
BERT-based rankers "while executing two orders-of-magnitude faster and requiring four
orders-of-magnitude fewer FLOPs per query" [cbb096e41] — concretely **over 170× speedup and
14,000× fewer FLOPs** in the re-rank configuration [cbb096e41]. The measured table: re-ranking
BM25's top-1000 with ColBERT reaches **MRR@10 = 34.9** at **61** ms and **7B** FLOPs/query,
versus BERT-large at 36.5 MRR@10 but **340T** FLOPs/query [cbb096e41]. Critically, MaxSim is
pruning-friendly enough to drive *end-to-end* retrieval over the full collection, not just
re-ranking: end-to-end ColBERT reports **Recall@1000 = 96.8** versus **81.4** for a
rerank-on-top-of-BM25 configuration capped at BM25's recall [cbb096e41] — that recall gap is
the quantitative case for end-to-end late interaction (`d6ccd6b1c`). The design's liability is
index size — the end-to-end L2 index is **154 GiB** on MS MARCO [cbb096e41] — which ColBERTv2
neutralizes via residual compression that reduces "the space footprint of late interaction by
**6–10×** while preserving quality" [c7b11e5a5].

**When hybrid retrieval is the right default instead.** For most RAG-style corpora the
evidence converges on combining signals rather than choosing one: retrieval quality improves
when dense embeddings and BM25 are combined rather than used alone (`dc97efcf9`), and
"contextual retrieval" is an *architecture* — context generation, embedding, a lexical index,
fusion, reranking — not a single product, so those stages should be separated before any
library (ColBERT included, as one reranking option) is chosen. The settled rule: late
interaction is a deliberate **offline-cost-for-query-cost reallocation** worth it when query
latency/FLOPs at scale dominate and the index-size cost is acceptable after v2 compression
[cbb096e41] [c7b11e5a5]; hybrid lexical+dense is the broader default, with a reranker earning
its place only on top of disciplined chunking (`dc97efcf9`).

## The orchestration primitive that runs the spine — two dispatch philosophies

How the planner-executor-publisher graph is *dispatched* is its own decision, and the durable
axis is the **execution model**, not a best-framework ranking (`d28841446`). Two official-doc
primaries define the two ends of the dispatch spectrum.

**LangGraph — explicit graph edges with per-branch state.** `Send` lets a node dispatch to
other nodes with *independent* state per branch, enabling map-reduce fan-out where the number
of branches is not known until runtime [cc413ffed]. `Command` fuses a state update with
routing in a single return value — it can "combine state updates and routing," `goto` a named
node, and even hand control to a parent graph via `graph=Command.PARENT` [cc413ffed]. The
sender *names exactly* which node(s) run next and what state each receives.

**AutoGen — decoupled publish/subscribe.** A **Topic** has a Topic Type and a Topic Source; a
**Subscription** maps topics to agents and the runtime uses subscriptions to decide who
receives a broadcast [cce59d029]. `TypeSubscription` implements type-based subscription,
mapping a Topic Type → Agent Type, and the docs state it is the **preferred** way to declare
subscriptions because it is **portable and data-independent** [cce59d029]. Here the publisher
names a *topic, not a recipient*; the subscription layer resolves who is addressed.

The settled choice rule (`d1fb5a112`, `d28841446`): a research engine that needs auditable,
resumable, branch/loop control with human checkpoints maps onto the graph/state-machine model
(`Send`/`Command`) [cc413ffed]; event-driven, loosely-coupled multi-agent collaboration where
senders should not know recipients maps onto the pub/sub model [cce59d029]. The
planner-executor-publisher spine above is naturally a graph (explicit stages, per-question
fan-out, a review→revise loop), which is why GPT-Researcher's multi-agent variant is itself
built on LangGraph [cb547d339].

## How the whole thing is benchmarked — and the honest comparability limit

The composed system's quality is, across vendors, comparable on **exactly one axis: benchmark
accuracy on a named, shared instrument** — the conclusion the sibling finding `d369c3d06`
establishes. Because a named benchmark (BrowseComp, DeepResearch-Bench) denotes the same task
distribution regardless of who runs it, a "BrowseComp accuracy" number is comparable across
vendors in a way no other reported figure is. The load-bearing evidence for that axis is the
*vendor-neutral aggregator leaderboards* that collect those scores — Steel's sourced BrowseComp
leaderboard [c2713d958] and LLM-Stats' BrowseComp model ranking [cc9ebf39f] — which give the
accuracy axis a cross-check no other dimension has. A deep-research market write-up reports the
same pattern illustratively (purpose-built deep-research tiers reach tens of percent on
BrowseComp while general models sit far lower) [ceb7cfb9f]; it references BrowseComp but is a
secondary market source, not the benchmark itself, so it is read as corroboration, not the
citation of record.

The comparability limit is sharp: cost, latency, and internal architecture are **vendor-
reported and not independently verified** (`d369c3d06`). Cost/latency units differ across
vendors and are self-estimated [ceb7cfb9f] [c3d36ff44]; closed-agent internals are known only
at the field-survey abstraction level [cbda2cb4e] or as third-party reconstruction. So the
benchmark layer's rule for an open engine: inherit only what is externally defined and
independently checkable — the shared accuracy benchmarks [c2713d958] [cc9ebf39f] — and treat
the cost/latency/architecture layer as attributed context, never as a head-to-head ranking.

## Honest limits

- **The spine is documented, the internals partly so.** GPT-Researcher's planner-executor-
  publisher flow and seven-role team are stated in its own README and docs [c1bb33cc6]
  [cb547d339]; STORM's two-stage pipeline is paper-backed [c3bf6d346], but the code-structure
  specifics (`StormInformationTable`, the four-stage `Knowledge Curation → Outline Generation
  → Article Generation → Polishing` linear pipeline) come from a third-party code-wiki
  [cc06c6ce1], not the paper, and are attributed accordingly.
- **STORM's +25% / +10% gains are vs. one baseline.** They are an absolute increase in
  organized/broad judgments against an *outline-driven retrieval-augmented* baseline
  [c3bf6d346] — not a cross-system leaderboard number and not transferable to other tasks.
- **ColBERT figures are MS MARCO passage-ranking specific.** The 170× / 14,000× / 96.8-vs-81.4
  numbers [cbb096e41] and the 6–10× v2 compression [c7b11e5a5] are measured on that collection
  and do not automatically transfer to other corpora.
- **Orchestration primitives are doc-anchored, not benchmarked.** `Send`/`Command` [cc413ffed]
  and Topic/Subscription [cce59d029] are primary for *how each API works*; no primary,
  reproducible benchmark comparing the frameworks' latency or cost exists in the corpus, so any
  comparative performance claim would be blog-relayed and non-load-bearing (`d28841446`).
- **Accuracy is the only honest cross-vendor axis.** Even shared-benchmark numbers are
  configuration-sensitive and often self-reported [ceb7cfb9f]; aggregator leaderboards
  [c2713d958] [cc9ebf39f] are the load-bearing form, and cost/latency/architecture comparisons
  are not supportable across vendors [cbda2cb4e].
