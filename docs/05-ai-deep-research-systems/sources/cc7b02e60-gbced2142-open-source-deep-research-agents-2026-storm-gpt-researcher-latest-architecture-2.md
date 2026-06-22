[Essays](https://rywalker.com/)[Research](https://rywalker.com/research)[Projects](https://rywalker.com/projects)[About](https://rywalker.com/about)`⌘K`
[← Back to research](https://rywalker.com/research)
Published March 15, 2026•Updated June 11, 2026·4 min read·company
# GPT Researcher
GPT Researcher — the OG open-source deep research agent. Autonomous planner/execution architecture produces detailed, factual research reports with citations from 20+ sources. 27.6k stars, Apache-2.0, Python, v3.5.0 shipped May 2026.
<https://gptr.dev>[ ↗](https://gptr.dev)
[autoresearch](https://rywalker.com/research/t/autoresearch)[deep-research](https://rywalker.com/research/t/deep-research)[open-source](https://rywalker.com/research/t/open-source)[python](https://rywalker.com/research/t/python)[github](https://rywalker.com/research/t/github)[agent-frameworks](https://rywalker.com/research/t/agent-frameworks)
Key takeaways
  * The original open-source deep research agent — planner generates research questions, execution agents gather information from 20+ sources, publisher aggregates into comprehensive reports with citations
  * 27.6k stars and 3.7k forks as of June 2026, Apache-2.0 license, active since May 2023. The longest-running and most battle-tested deep research agent in the ecosystem — v3.5.0 shipped May 28, 2026
  * Works with any LLM provider. Supports web research, local document research, hybrid modes, and a recursive Deep Research mode. Claude Code skill integration via skills.sh
  * Free and self-hosted — no paid cloud tier. You bring your own LLM and search API keys; a typical research run costs roughly $0.10 in API usage


FAQ
What is GPT Researcher?
An autonomous deep research agent that generates detailed, factual research reports with citations. It creates a research plan, dispatches crawler agents to gather information, then aggregates findings into a comprehensive report.
How does GPT Researcher differ from ChatGPT or Claude deep research?
GPT Researcher is fully open source (Apache-2.0), works with any LLM provider, and can research both web sources and local documents. Proprietary alternatives are locked to their respective platforms.
How much does GPT Researcher cost?
The software is free under Apache-2.0 with no hosted paid tier. You supply your own LLM and search API keys; the project estimates an average research task takes about three minutes and costs roughly $0.10 in API usage.
## Overview
GPT Researcher is the original open-source deep research agent — an autonomous system that produces detailed, factual, and unbiased research reports with citations. Created in May 2023 by Assaf Elovic, it predates the deep research wave by nearly two years and remains the most-starred open-source deep research tool on [GitHub](https://rywalker.com/research/t/github) at 27.6k stars.
The core architecture uses a planner/execution pattern: the planner generates research questions from a user query, crawler agents gather information from 20+ web sources in parallel, and a publisher aggregates all findings into a comprehensive report with source tracking.
**Key stats (as of June 11, 2026):** 27,643 stars, 3,721 forks, Apache-2.0 license, [Python](https://rywalker.com/research/t/python), active development since May 2023 — last push May 28, 2026.
* * *
## Status & Releases
Development remains active. Since this profile's original date (March 2026), the project has shipped v3.4.4 (April 16, 2026) and v3.5.0 (May 28, 2026), continuing a steady monthly-ish release cadence that goes back to 2023. The repo is not archived and carries 218 open issues — normal load for a project this size.
Beyond standard web research, the docs cover multi-agent research teams (planning through publication), hybrid web + local document research, and a recursive Deep Research mode.
* * *
## Architecture
The agent follows a structured pipeline:
  1. **Create a task-specific agent** based on the research query
  2. **Generate questions** that collectively form an objective opinion on the task
  3. **Use crawler agents** to gather information for each question in parallel
  4. **Summarize and source-track** each resource
  5. **Filter and aggregate** summaries into a final research report


The parallelized approach addresses key problems with naive LLM research: it reduces hallucination by cross-referencing multiple sources, increases speed through concurrent crawling, and mitigates bias by drawing from diverse sources.
* * *
## Pricing & Licensing  
| Tier  | Price  | Includes  |  
| --- | --- | --- |  
| Open source  | $0 (Apache-2.0)  | Full agent, web/local/hybrid research, multi-agent flows, Deep Research mode — self-hosted  |  
| API usage (BYO keys)  | ~$0.10 per research run  | Your own LLM + search provider keys; average task takes ~3 minutes  |  
There is no commercial hosted tier as of June 2026 — GPT Researcher is a self-hosted tool, not a SaaS.
* * *
## Competitive Position
**Strengths:** Longest-running deep research agent. Battle-tested, well-documented, large community. Apache-2.0 license. Works with any LLM provider. Claude Code skill integration.
**Weaknesses:** Prompt-based approach (no fine-tuned model). Newer tools like Tongyi DeepResearch are beating it on benchmarks with RL-trained specialized models.
* * *
## Cautions
  * Report quality is bounded by the underlying model and search provider you configure — it's an orchestration layer, not a trained research model
  * Per-run API costs (~$0.10 average) scale with depth settings; recursive Deep Research runs cost more
  * The prompt-based architecture is losing benchmark ground to RL-trained agents, so expect the gap to widen on hard research tasks


* * *
## What Developers Say
Community sentiment on Hacker News is modest in volume but consistently positive, centering on control and configurability. Comparing it to proprietary deep research products, sublimefire wrote: "I do prefer tools like GPT researcher where you are in control over sources and search engines." On cost flexibility, jimmySixDOF noted "there are so many ways to configure GPT Researcher for all kinds of budgets." On maintenance, wluk observed: "The creator of the project, Assaf, has been nothing but friendly." Notably, the project has never had a large standalone HN thread — its 27k-star adoption grew through GitHub and word of mouth rather than a viral launch.
* * *
## Bottom Line
**Recommended** if you want a self-hosted, provider-agnostic deep research agent with full control over sources, search engines, and cost — it's the most mature open option, still actively shipping (v3.5.0, May 2026).
**Not recommended** if you need state-of-the-art benchmark performance on hard research tasks — RL-trained agents like Tongyi DeepResearch now lead there — or if you want a managed SaaS with zero setup.
**Outlook:** Stable and durable. Three years of continuous releases and 27.6k stars make it the default open-source baseline for the category, even as fine-tuned challengers pass it on benchmarks.
* * *
_Research by Ry Walker Research •[methodology](https://rywalker.com/research/methodology)_
Sources
  * [[1]](https://rywalker.com/research/gpt-researcher#cite-1) [assafelovic/gpt-researcher GitHub](https://github.com/assafelovic/gpt-researcher)
  * [[2]](https://rywalker.com/research/gpt-researcher#cite-2) [GPT Researcher Documentation](https://docs.gptr.dev)
  * [[3]](https://rywalker.com/research/gpt-researcher#cite-3) [gpt-researcher releases (GitHub)](https://github.com/assafelovic/gpt-researcher/releases)
  * [[4]](https://rywalker.com/research/gpt-researcher#cite-4) [GPT Researcher FAQ — cost per research run](https://docs.gptr.dev/docs/faq)
  * [[5]](https://rywalker.com/research/gpt-researcher#cite-5) [Hacker News comment — sublimefire on deep research tools (Apr 2025)](https://news.ycombinator.com/item?id=43758273)
  * [[6]](https://rywalker.com/research/gpt-researcher#cite-6) [Hacker News comment — jimmySixDOF on configurability (Mar 2025)](https://news.ycombinator.com/item?id=43266335)
  * [[7]](https://rywalker.com/research/gpt-researcher#cite-7) [Hacker News comment — wluk on project maintenance (Dec 2024)](https://news.ycombinator.com/item?id=42411131)


[Share on X](https://twitter.com/intent/tweet?text=GPT%20Researcher%20%7C%20Ry%20Walker%20Research&url=https%3A%2F%2Frywalker.com%2Fresearch%2Fgpt-researcher)[Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Frywalker.com%2Fresearch%2Fgpt-researcher)
On this page
  * [Overview](https://rywalker.com/research/gpt-researcher#overview)
  * [Status & Releases](https://rywalker.com/research/gpt-researcher#status--releases)
  * [Architecture](https://rywalker.com/research/gpt-researcher#architecture)
  * [Pricing & Licensing](https://rywalker.com/research/gpt-researcher#pricing--licensing)
  * [Competitive Position](https://rywalker.com/research/gpt-researcher#competitive-position)
  * [Cautions](https://rywalker.com/research/gpt-researcher#cautions)
  * [What Developers Say](https://rywalker.com/research/gpt-researcher#what-developers-say)
  * [Bottom Line](https://rywalker.com/research/gpt-researcher#bottom-line)


Key takeaways
  * The original open-source deep research agent — planner generates research questions, execution agents gather information from 20+ sources, publisher aggregates into comprehensive reports with citations
  * 27.6k stars and 3.7k forks as of June 2026, Apache-2.0 license, active since May 2023. The longest-running and most battle-tested deep research agent in the ecosystem — v3.5.0 shipped May 28, 2026
  * Works with any LLM provider. Supports web research, local document research, hybrid modes, and a recursive Deep Research mode. Claude Code skill integration via skills.sh
  * Free and self-hosted — no paid cloud tier. You bring your own LLM and search API keys; a typical research run costs roughly $0.10 in API usage


FAQ
What is GPT Researcher?
An autonomous deep research agent that generates detailed, factual research reports with citations. It creates a research plan, dispatches crawler agents to gather information, then aggregates findings into a comprehensive report.
How does GPT Researcher differ from ChatGPT or Claude deep research?
GPT Researcher is fully open source (Apache-2.0), works with any LLM provider, and can research both web sources and local documents. Proprietary alternatives are locked to their respective platforms.
How much does GPT Researcher cost?
The software is free under Apache-2.0 with no hosted paid tier. You supply your own LLM and search API keys; the project estimates an average research task takes about three minutes and costs roughly $0.10 in API usage.
![Cincinnati skyline](https://rywalker.com/cincy.svg)
Made in Cincinnati
[X](https://twitter.com/rywalker)[LinkedIn](https://linkedin.com/in/rywalker)[GitHub](https://github.com/ryw)

