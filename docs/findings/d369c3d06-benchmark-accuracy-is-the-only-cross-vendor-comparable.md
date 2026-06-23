---
status: draft
topic: 05-ai-deep-research-systems
id: d369c3d06
title: Benchmark accuracy is the only cross-vendor comparable for frontier deep-research agents; cost, latency, and internal architecture are vendor-reported and not independently verified
---

# Benchmark accuracy is the only cross-vendor comparable for frontier deep-research agents; cost, latency, and architecture are vendor-reported and not independently verified

The two prior findings for this category leaned on benchmark *results* — the
DeepResearch-Bench leaderboard and the halt/citation tradeoff. This finding steps back to
a question that sits underneath any cross-vendor comparison: **of the dimensions on which
named frontier deep-research agents (OpenAI DR, Gemini DR, Perplexity DR, Grok DeepSearch)
are routinely compared — accuracy, cost, latency, and internal architecture — which carry
authoritative provenance, and which are vendor-reported or inferred and therefore unsafe
to treat as established fact?** The corpus answers cleanly: the four dimensions do *not*
share an evidentiary footing, and an open research engine should weight them accordingly.

## What the corpus actually is: a provenance gradient

The nine corpus sources fall into three distinct provenance tiers, and the tier — not the
specificity of the number — is what determines how much weight a claim can bear.

- **Authoritative / academic.** Only one source is a primary scholarly artifact: the arXiv
  survey *Deep Research Agents: A Systematic Examination and Roadmap* (arXiv:2506.18096),
  which formally defines "Deep Research agents" and names OpenAI DR, Gemini DR, Grok
  DeepSearch, and Perplexity DR as the industry exemplars [cbda2cb4e]. It is the corpus's
  only authoritative basis for what these agents *are* and how they are *structured*.
- **Aggregator leaderboards.** Steel leaderboards and LLM-Stats publish source-linked,
  reproducible benchmark scores across many models — secondary but methodologically
  transparent and vendor-neutral [c2713d958][cc9ebf39f].
- **Vendor and marketing sources.** Parallel.ai's own blog (a deep-research API vendor),
  benchlm.ai (a model-ranking/affiliate aggregator), and consumer comparison blogs
  (TrendlyAI, a cookie-walled comparison site) supply most of the cost and latency figures
  [ceb7cfb9f][c3d36ff44][c18cb025a][cf650704e][c99407eeb]. A ByteByteGo newsletter supplies
  a blog-level reconstruction of closed-agent internals [cfa313c43].

## Accuracy: the one cross-vendor comparable, because the benchmark definition is shared

Accuracy is the only dimension where competing agents are scored against a *common, named,
externally-defined* yardstick. BrowseComp was developed by OpenAI and documented in a
benchmark paper (arXiv:2504.12516), so a "BrowseComp accuracy" number means the same task
distribution regardless of who reports it [ceb7cfb9f]. DeepResearch-Bench is likewise a
fixed instrument — 100 PhD-level tasks across 22 fields, scoring multistep web exploration,
targeted retrieval, and higher-order synthesis [c3d36ff44]. Because the instrument is
shared, the *relative ordering* survives even when a single vendor reports it: purpose-built
deep-research tiers reach tens of percent on BrowseComp (e.g. a 45% tier, a 58%
high-compute tier) while Perplexity's deep research sits at roughly 6–8% on the same
benchmark [ceb7cfb9f]. Independent aggregator leaderboards exist for exactly this reason —
Steel maintains a sourced BrowseComp leaderboard for agentic web-research systems
[c2713d958], and LLM-Stats ranks 49 models on BrowseComp with a published average score
[cc9ebf39f] — giving the accuracy dimension a vendor-neutral cross-check that no other
dimension in the corpus has.

The honest caveat: even shared-benchmark numbers are configuration-sensitive and often
self-reported. Parallel's own methodology states it reports "the highest numbers we were
able to achieve across multiple configurations" of competitors' APIs, with explicit
favorable configs (GPT-5 at high reasoning, high search context) and *excluded* runs where
a competitor scored 0% win rate [c3d36ff44]. So accuracy is the most comparable dimension,
but a single-vendor accuracy table is still an advocacy document; the aggregator
leaderboards [c2713d958][cc9ebf39f] are the load-bearing form of this claim.

## Cost and latency: specific, attributed, and structurally non-comparable

Cost and latency figures in the corpus are numerous and precise-looking, yet every
load-bearing one traces to a vendor or aggregator, and the agents are not even priced on a
common unit. Parallel reports its own tiers at \$10 / \$100 / \$300 / \$2,400 per 1,000
runs (Core/Pro/Ultra/Ultra8x) [ceb7cfb9f]. Against that, it reports Gemini Deep Research
Max at *roughly* \$2,500 per 1,000 queries and explicitly flags it "(estimated)", and lists
OpenAI deep research cost as "Not published" — OpenAI does not publish per-query pricing for
programmatic use [ceb7cfb9f][c3d36ff44]. Latency is reported only as coarse bands ("minutes
to tens of minutes," "minutes to hours") rather than measured wall-clock distributions
[ceb7cfb9f]. benchlm.ai aggregates such figures but is itself a ranking/affiliate site, not
a measurement authority [c18cb025a]. None of these are independently reproduced, the units
differ (per-query vs per-1,000, consumer subscription vs API), and one of the headline
numbers is self-labelled an estimate — so these must be carried as *attributed,
non-load-bearing* ("Parallel reports ~\$2,500/1k for Gemini DR Max, estimated"), never as
the established cost of a competitor's product.

## Internal architecture of closed agents: reported and inferred, not observed

The corpus's architecture material splits the same way. The authoritative survey gives a
*generic* DR-agent structure — dynamic reasoning, adaptive task planning, and multi-step
interaction with web resources and analytical tools — abstracted across the field rather
than reverse-engineered from any one closed product [cbda2cb4e]. That generic
decompose→retrieve→synthesize loop is safe to assert. What is *not* safe is any claim about
the specific internal pipeline of OpenAI DR or Gemini DR: the corpus's source for closed-agent
internals is a ByteByteGo newsletter [cfa313c43] and consumer comparison blogs
[c99407eeb][cf650704e], i.e. third-party reconstructions of black-box systems. Closed-agent
internals must therefore be framed as *reported/inferred* structure, attributed to the
reconstructing source, not stated as ground truth.

## What an open research engine should take from this

The actionable conclusion is an evidence-weighting rule, not a feature list. (1) Treat
**benchmark accuracy on a named shared instrument** (BrowseComp, DeepResearch-Bench) as the
only dimension on which frontier DRAs can be honestly *compared*, and prefer vendor-neutral
aggregator leaderboards [c2713d958][cc9ebf39f] over any single vendor's table [c3d36ff44].
(2) Treat **cost and latency** as attributed, non-load-bearing context — useful for
order-of-magnitude intuition, never as a basis for a head-to-head ranking, because the units
differ and the numbers are vendor-reported or self-estimated [ceb7cfb9f][c18cb025a]. (3)
Anchor **architecture** to the field-level survey abstraction [cbda2cb4e] and explicitly
mark any closed-agent internal detail as a third-party reconstruction [cfa313c43]. The
strongest move an open, reproducible engine can make against this corpus is to inherit only
what is externally defined and independently checkable — the shared benchmarks — and to
treat the marketing-grade cost/latency/architecture layer as exactly that.
