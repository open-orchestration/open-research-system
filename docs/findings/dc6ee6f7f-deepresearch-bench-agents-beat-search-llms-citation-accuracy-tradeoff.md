# What DeepResearch-Bench numbers reveal: deep-research agents beat search-augmented LLMs, and citation accuracy trades off against citation volume

status: draft
topic: 05-ai-deep-research-systems

The prior survey of this category established the convergent planner→retrieve→synthesize
pipeline qualitatively but had no comparative evaluation numbers, cost figures, or
citation-accuracy data. The newly gathered corpus closes that gap: it contains the
DeepResearch-Bench paper (arXiv:2506.11763) with a full leaderboard, plus the bench's
two evaluation frameworks and architecture teardowns of the open-source agents. This
finding leans on those quantitative results to answer questions the earlier qualitative
landscape could not: *how much* better are purpose-built deep-research agents than
search-augmented chat LLMs, *where* they differ, and what the citation metrics expose as
an unresolved tradeoff.

## DeepResearch-Bench: what it measures

DeepResearch-Bench is a benchmark of 100 PhD-level research tasks (50 Chinese, 50 English)
hand-crafted by 100+ domain experts across 22 distinct fields [c840a2e0d]. The task
distribution was derived empirically: the authors analyzed 96,147 raw user queries from a
web-search-enabled LLM chatbot, filtered to 44,019 that genuinely require multi-round
search-and-synthesis, and classified them into the 22 domains so the benchmark mirrors
real deep-research demand [c840a2e0d]. It scores agents with two complementary frameworks:
**RACE** (Reference-based Adaptive Criteria-driven Evaluation with dynamic weighting) for
report *quality*, and **FACT** (Framework for Factual Abundance and Citation
Trustworthiness) for *information-retrieval and citation* quality [c840a2e0d]. The paper
is 31 pages, 5 figures, by Du, Xu, Zhu, Wang, and Mao [cc3dca8e9].

## Purpose-built agents decisively outscore search-augmented LLMs

The headline quantitative result: dedicated Deep Research Agents (DRAs) substantially
outperform leading LLMs equipped only with a search tool on report quality. On the RACE
Overall score, **Gemini-2.5-Pro Deep Research led at 48.88 and OpenAI Deep Research
followed at 46.98** [c840a2e0d]. The best *search-augmented LLM*, Claude-3.7-Sonnet
w/Search, reached only 40.67 RACE Overall — and among raw search-LLMs it was the top
performer, with most GPT-4o/4.1-with-search variants landing in the 30–35 range
[c840a2e0d]. Perplexity Deep Research (42.25) and Grok Deeper Search (40.24) sat between
the frontier DRAs and the search-LLMs [c840a2e0d]. This is direct, falsifiable evidence
for a claim the earlier landscape could only assert: the orchestration layer, not just the
underlying model, drives report quality — the same Claude/Gemini model families appear on
both sides of the gap, yet the agent harnesses score markedly higher [c840a2e0d].

Capability differences are not uniform across dimensions. OpenAI Deep Research achieved the
highest Instruction-Following sub-score (49.27) despite trailing Gemini on Overall,
indicating the RACE dimensions capture genuinely distinct skills rather than one latent
"goodness" axis [c840a2e0d].

## The citation tradeoff: abundance vs. accuracy

The FACT framework surfaces a real tension the quality scores hide. **Gemini-2.5-Pro Deep
Research produced an exceptional 111.21 average effective citations — far more than any
competitor — yet its citation *accuracy* was only 81.44%** [c840a2e0d]. By contrast,
**Perplexity Deep Research had the highest citation accuracy at 90.24% but a much lower
effective-citation count of 31.26** [c840a2e0d]. Among search-augmented LLMs, Claude-3.5
and Claude-3.7 Sonnet posted the highest accuracy of all (94.04% and 93.68%) but with
tiny effective-citation counts (9.78 and 32.48) [c840a2e0d]. In other words, the agent
that grounds the most claims is not the one that grounds them most reliably — citation
volume and citation precision pull in opposite directions across the leaderboard, and no
single system dominated both [c840a2e0d]. For a system that treats provenance as a
first-class guarantee, this is the central design tension the numbers expose.

## The benchmark is itself an LLM-as-judge system — and validates that choice

RACE is a reference-based LLM-as-judge pipeline, and the paper quantifies how trustworthy
that is. Against human experts (70+ annotators with Master's degrees, each capped at three
queries to diversify perspective), the full RACE framework reached a human-consistency
**Overall score of 72.56%, versus 60.46% for a vanilla-prompt baseline**, and notably
exceeded the human inter-annotator agreement of 68.44% [c840a2e0d]. Ablations show the
*reference-based comparison* is the load-bearing component: removing it caused the largest
drop (Overall 72.56→68.19) — relative scoring against a high-quality reference report,
not absolute scoring, is what makes the judge discriminative [c840a2e0d]. Judge-model
choice was made on a cost/quality basis: Gemini 2.5 Pro Preview gave the best consistency
(72.56%) at $0.13/query and was selected over o3 (68.58% at $0.37) and o4-mini (71.63% at
the cheapest $0.04) [c840a2e0d].

The benchmark is a live artifact, not a frozen paper. Following Google's announced
June 17, 2026 deprecation of Gemini-2.5-Pro, the maintainers re-benchmarked three frontier
reasoning models as replacement evaluators on a 200-article human-annotated subset and
switched the official RACE evaluator to **GPT-5.5 (71.82 Overall, beating Gemini-3.1-Pro's
70.58 and Claude-Opus-4-7's 70.11)**, with GPT-5.4-mini for the FACT pipeline [c2fa5c707].
A successor, DeepResearch Bench II, was released 6 Feb 2026 with a different evaluation
focus, while the original DRB continues to be maintained [c2fa5c707]. Any score
comparison must therefore be pinned to a specific evaluator generation — the evaluator
itself moved, so cross-date leaderboard numbers are not directly comparable [c2fa5c707].

## Architecture teardowns explain *why* the orchestration matters

The open-source teardowns make the "orchestration is the moat" claim concrete. GPT
Researcher uses an explicit planner/executor pattern: a `ResearchConductor`
(gpt_researcher/skills/researcher.py) handles query planning, sub-query generation, and
retriever coordination; a `BrowserManager` runs parallel URL scraping via a `WorkerPool`;
and a `ContextManager` filters and compresses gathered information to fit LLM context
windows [c3d184ff8]. The design is explicitly inspired by the Plan-and-Solve and RAG
papers, and addresses misinformation/speed by parallelizing agent work [c3d184ff8]. The
planner decomposes the task into a set of questions that "collectively form an objective
opinion," crawler agents gather from 20+ web sources in parallel, and a publisher
aggregates findings into a cited report with source tracking [cc7b02e60]. Crucially, the
teardown is candid about the ceiling: GPT Researcher's report quality "is bounded by the
underlying model and search provider you configure — it's an orchestration layer, not a
trained research model" [cc7b02e60]. It also integrates the Model Context Protocol (MCP)
so retrieval can hit GitHub repos, databases, and custom APIs alongside web search
(e.g. `RETRIEVER=tavily,mcp` for hybrid retrieval) [c1b024617].

## Specialized tools occupy a different niche than frontier agents

The product-comparison sources show the category has bifurcated. Frontier-lab offerings in
2026 are framed as enterprise agent *platforms*: within hours on April 22, 2026 OpenAI
launched Workspace Agents (90+ connectors, built on the AgentKit connector framework
introduced Oct 2025), Google unveiled the Gemini Enterprise Agent Platform (consolidating
Vertex AI and Agentspace), and Salesforce expanded Agentforce — and Gemini 3.1 Pro offers
the largest production context window at 2M tokens vs. 1M for OpenAI and Claude
[cb6ceb956]. Meanwhile the *research-assistant* tools are positioned by task fit rather
than raw model power: Perplexity is the "best overall starting point" for fast cited web
research (Pro $20/mo, Enterprise $40/user/mo) but has "occasional citation quality issues
on niche topics" [cf841afde][c2026b5cf], whereas Elicit is purpose-built for systematic
literature review — paper discovery, screening, and sentence-level data extraction from
full-text PDFs [cf841afde]. The selection logic is explicit: use Perplexity for current
web sources, Elicit/Consensus for peer-reviewed literature, NotebookLM/Claude when you
already hold the sources [c2026b5cf].

## What this adds beyond the prior landscape

Three things the qualitative survey could not supply, now grounded in numbers:
(1) the quality gap between purpose-built DRAs and search-augmented LLMs is real and
roughly 6–8 RACE points at the top [c840a2e0d]; (2) citation abundance and citation
accuracy are in tension, so a provenance-first system cannot optimize one as a proxy for
the other [c840a2e0d]; (3) an LLM-as-judge eval can exceed human inter-annotator
agreement *if* it is reference-based, but the evaluator model itself drifts over time and
must be version-pinned [c840a2e0d][c2fa5c707].
