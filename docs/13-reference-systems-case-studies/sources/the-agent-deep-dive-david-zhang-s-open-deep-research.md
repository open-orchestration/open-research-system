# The Agent Deep Dive: David Zhang's Open Deep Research

Source: https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research

[ ![Langfuse Logo](https://langfuse.com/langfuse-wordart-white.svg)![Langfuse Logo](https://langfuse.com/langfuse-wordart.svg) ](https://langfuse.com/)[by ClickHouse](https://clickhouse.com)
Product
[Overview](https://langfuse.com/docs)[LLM Observability](https://langfuse.com/docs/observability/overview)[Prompt Management](https://langfuse.com/docs/prompt-management/overview)[Evaluation](https://langfuse.com/docs/evaluation/overview)[Metrics](https://langfuse.com/docs/metrics/overview)
[ langfuse Get Started with Tracing Step-by-step guide to ingesting your first trace using OpenAI, LangChain, or the SDKs. Get Started with Tracing This guide walks you through ingesting your first trace. Read docs ](https://langfuse.com/docs/get-started)
Resources
[Academy](https://langfuse.com/academy)[Workshop](https://langfuse.com/workshop)[Blog](https://langfuse.com/blog)[Changelog](https://langfuse.com/changelog)[Roadmap](https://langfuse.com/docs/roadmap)[Users](https://langfuse.com/users)[Example Project](https://langfuse.com/docs/demo)[Walkthroughs](https://langfuse.com/guides)[Support](https://langfuse.com/support)
[ langfuse ClickHouse Langfuse joins ClickHouse Our goal continues to be building the best AI engineering platform Read story ](https://langfuse.com/blog/joining-clickhouse)
[Docs](https://langfuse.com/docs)[Changelog](https://langfuse.com/changelog)[Pricing](https://langfuse.com/pricing)
[`Launch App``L`](https://langfuse.com/cloud)
[`Get Demo``G`](https://langfuse.com/talk-to-us)
Categories
[+ All [72]](https://langfuse.com/blog)[+ agents [3]](https://langfuse.com/blog?tag=agents)[+ announcement [8]](https://langfuse.com/blog?tag=announcement)[+ architecture [4]](https://langfuse.com/blog?tag=architecture)[+ engineering [13]](https://langfuse.com/blog?tag=engineering)[+ evaluation [4]](https://langfuse.com/blog?tag=evaluation)[+ example [2]](https://langfuse.com/blog?tag=example)[+ guide [19]](https://langfuse.com/blog?tag=guide)[+ integration [6]](https://langfuse.com/blog?tag=integration)[+ launchweek [4]](https://langfuse.com/blog?tag=launchweek)[+ update [20]](https://langfuse.com/blog?tag=update)
Receive Updates
One email per month with our latest ships and product announcements.
Subscribe
![The Agent Deep Dive: David Zhang’s Open Deep Research](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Fthe-agent-deep-dive.png&w=3840&q=75)
# The Agent Deep Dive: David Zhang’s Open Deep Research
This blog post explores David Zhang’s open-source framework for iterative AI research. We look at the system’s query process, parallel search executions, and markdown report creation, and compare it to both OpenAI’s and Perplexity’s research solutions.
![Picture Jannik Maierhöfer](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fjannikmaierhoefer.jpg&w=96&q=75)Jannik Maierhöfer
AI-driven research is evolving fast. While Google pioneered Deep Research, OpenAI popularized it and Perplexity and Grok followed, open-source alternatives are just as exciting and help to understand how one of the first forms of autonomous _useful_ agents works. In this post, I take a closer look at the inner workings of open [deep-research](https://github.com/dzhng/deep-research) by David Zhang ([dzhng](https://github.com/dzhng))—a lightweight, transparent framework for iterative AI research.
At under 500 lines of code, `deep-research` packs a surprising punch. It runs recursive research loops, refining queries based on the information it finds—no hidden logic, no unnecessary dependencies, just a clean, modular setup that’s easy to hack or extend.
I decided to put it to the test. With [Langfuse](https://github.com/langfuse/langfuse), I traced its execution (thanks to [@hassiebp](https://github.com/hassiebp) for instrumenting it in this [fork](https://github.com/hassiebp/deep-research-with-langfuse)), broke down its decision-making, and measured performance. Below, I’ll show how it works, why it’s worth a look, and how it compares to other AI deep research tools.
* * *
## [Why I Like This Agent](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#why-i-like-this-agent)
  * **Simple** – Minimalist design, easy to modify, and fully open-source.
  * **Iterative Research** – Runs deep research loops, refining its queries at each step.
  * **Control Depth & Breadth** – Users define how far (depth) and wide (breadth) the research should go.
  * **Parallel Execution** – Fires off multiple queries at once, speeding up research.


**Tech Stack** :
  * **o3-mini** as the language model for SERP generation, learnings, and the final report.
  * **Firecrawl** for executing SERP queries.


Despite its minimal footprint, the framework is robust enough to generate meaningful follow-up questions, refine its search, and compile a structured final report. This simplicity makes it an approachable playground for anyone looking to experiment with or build upon an iterative AI research agent.
* * *
## [How Does the Agent Work?](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#how-does-the-agent-work)
To see how `deep-research` holds up, I asked it a more nuanced question:
> "I don't get how Whisper is fully open source (MIT), yet ChatGPT's speech-to-text is vastly better than Perplexity's and Apple's. Can you help me figure this out?"
This isn’t a simple fact lookup—it requires synthesizing multiple sources, filtering insights, and producing structured responses.
With a breadth of 4 and a depth of 2 (which are the two configuration options that are available), we might see the agent generate multiple parallel queries—and then refine those queries after it sees what the search turned up. You’d end up with a thorough markdown report summarizing everything, plus any missing links the agent found intriguing.
Each iteration of this loop can be viewed as an event within Langfuse. Tracking these events provides a step-by-step replay of the agent’s logic—useful for debugging and fine-tuning. Here’s the public trace in Langfuse:
[**Link to Public Trace**](https://cloud.langfuse.com/project/cm6y5qfi901bzad07tyaeg3no/traces/fd9be9b8-ffd2-435b-ba90-45a0af649954)
![Gantt
chart](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Fgatt.png&w=3840&q=75)
_Note: The chart above is a Gantt-like overview of query processes._
Next, let’s break down each step of the research loop in more detail.
### [1. Initial Query](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#1-initial-query)
The system message and user prompt are created. This is where the agent sets the context.
![Initial
Query](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Fsystem-prompt.png&w=3840&q=75)
### [2. Follow-Up Questions](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#2-follow-up-questions)
The agent proposes up to three follow-up questions based on the initial prompt.
![Follow Up
Questions](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Ffollow-up-1.png&w=3840&q=75)
### [3. Search Queries](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#3-search-queries)
Based on those follow-up questions, the agent generates SERP queries to investigate the topic further.
![Search
Queries](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Fserp-queries.png&w=3840&q=75)
### [4. Search Engine Calls](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#4-search-engine-calls)
The system then spawns multiple queries to a search API (in this case, Firecrawl).
![Search Engine
Calls](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Fcontext.png&w=3840&q=75)
### [5. Learnings from the Content](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#5-learnings-from-the-content)
After retrieving the search results, the agent processes them and generates up to three “learnings” (insights). It also proposes new follow-up questions, continuing the loop if necessary.
![Learnings](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Flearnings.png&w=3840&q=75)
![Follow Up
Questions](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Ffollow-up.png&w=3840&q=75)
### [6. Markdown Report](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#6-markdown-report)
Finally, once the maximum research breadth (e.g., 4) and depth (e.g., 2) are reached, the agent compiles a Markdown report summarizing key findings. It uses all the intermediate “learnings” from previous steps to form a coherent answer.
![Markdown
Report](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-02-20-the-agent-deep-dive-open-deep-research%2Ffinal-report.png&w=3840&q=75)
Thanks to the instrumentation we added above, all these steps are tracked in Langfuse—timestamps, search calls, LLM calls, and final outputs—providing a transparent view of how the agent arrives at its answer.
* * *
## [Comparison With Other AI Research Tools](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#comparison-with-other-ai-research-tools)
Although `deep-research` is a small, open-source project, I wanted to see how it fares alongside two well-known AI tools: OpenAI’s ChatGPT (with advanced research features or higher usage tiers) and Perplexity Pro.
To keep it fair, I ran the **same** question on all three:
### [David Zhang’s Open Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#david-zhangs-open-deep-research)
  * **Time to finish** : ~3 minutes and 34 seconds
  * **Estimated model usage cost** : ~$0.71
  * **Generated report length** : ~12k characters
  * **Trace** : [Langfuse Link](https://cloud.langfuse.com/project/cm6y5qfi901bzad07tyaeg3no/traces/fd9be9b8-ffd2-435b-ba90-45a0af649954)


### [OpenAI’s Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#openais-deep-research)
  * **Time to finish** : ~6 minutes
  * **Insights** : ~27 sources
  * **Generated report length** : ~87k characters
  * **Costs** : Hard to pin down exactly; it likely depends on o3 and crawler usage.
  * **Example link** : [OpenAI Example Thread](https://chatgpt.com/share/67aa55e9-1cb4-8009-a3c1-69607e6ca1cd)


### [Perplexity Pro Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#perplexity-pro-deep-research)
  * **Time to finish** : ~3 minutes
  * **Insights** : ~49 sources
  * **Report length** : ~8k characters
  * **Link to Perplexity Thread** : [Perplexity Deep Research Example](https://www.perplexity.ai/search/i-don-t-get-how-whisper-is-ful-Uuq8BQh8SyOOkAuOeG0j_Q)


## [Takeaways](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#takeaways)
  * `deep-research` is impressively agile for a lean, open-source tool.
  * Perplexity’s product can pull in a larger number of sources quickly, leveraging its specialization on web search.
  * OpenAI’s Deep Research produced a lengthy report, utilized more sources, and conducted a thorough investigation based on follow-up searches. Overall, the reasoning capabilities (o3, post-training for this use case) are significantly stronger than those of the other contestants.


Ultimately, if you want transparency, low cost, and hackability, David Zhang’s `deep-research` stands out. If you need huge reports or integrated browsing at scale, you may prefer a more mature commercial solution.
## [Other Open Source Research Agent Frameworks](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#other-open-source-research-agent-frameworks)
If you’re interested in exploring similar projects, check out these options:
  * [Hugging Face’s open-deep-research](https://github.com/huggingface/smolagents/tree/gaia-submission-r1/examples/open_deep_research)
  * [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
  * [jina-ai/node-DeepResearch](https://github.com/jina-ai/node-DeepResearch)


## [What's Next?](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#whats-next)
I will do more deep dives on interesting OSS agents to dissect how they work and what's interesting about them. Email me if you have suggestions: agent-deep-dive@langfuse.com
* * *
Was this page helpful?
Good
Bad
[Support](https://langfuse.com/support)
* * *
[PreviousEvaluating and Monitoring Voice AI Agents](https://langfuse.com/blog/2025-01-22-evaluating-voice-ai-agents)[NextLangfuse February Update](https://langfuse.com/blog/2025-02-28-langfuse-february-update)
[GitHub](https://github.com/langfuse/langfuse)[Discord](https://langfuse.com/discord)[X](https://x.com/langfuse)[YouTube](https://www.youtube.com/@langfuse)[LinkedIn](https://www.linkedin.com/company/langfuse/)
Product
  * [Observability](https://langfuse.com/docs/observability/overview)
  * [Prompt Management](https://langfuse.com/docs/prompt-management/overview)
  * [Evaluations](https://langfuse.com/docs/evaluation/overview)
  * [Metrics](https://langfuse.com/docs/metrics/overview)
  * [Langfuse for Agents](https://langfuse.com/agents)
  * [Playground](https://langfuse.com/docs/prompt-management/features/playground)
  * [Pricing](https://langfuse.com/pricing)
  * [Enterprise](https://langfuse.com/enterprise)


Developers
  * [Documentation](https://langfuse.com/docs)
  * [Self-Hosting](https://langfuse.com/self-hosting)
  * [SDKs](https://langfuse.com/docs/observability/sdk/overview)
  * [Integrations](https://langfuse.com/integrations)
  * [API Reference](https://langfuse.com/docs/api-and-data-platform/overview)
  * [Status](https://status.langfuse.com)
  * [Talk to Us](https://langfuse.com/talk-to-us)


Resources
  * [Blog](https://langfuse.com/blog)
  * [Changelog](https://langfuse.com/changelog)
  * [Roadmap](https://langfuse.com/docs/roadmap)
  * [Interactive Demo](https://langfuse.com/docs/demo)
  * [Customers](https://langfuse.com/users)
  * [AI Engineering Library](https://langfuse.com/library)
  * [Workshop](https://langfuse.com/workshop)
  * [Guides & Cookbooks](https://langfuse.com/guides)


Company
  * [About Us](https://langfuse.com/about)
  * [Careers](https://langfuse.com/careers)
  * [Handbook](https://langfuse.com/handbook)
  * [Press](https://langfuse.com/press)
  * [Security](https://langfuse.com/security)
  * [Support](https://langfuse.com/support)
  * [Open source](https://langfuse.com/handbook/chapters/open-source)


[Terms](https://langfuse.com/terms)[Privacy](https://langfuse.com/privacy)[Imprint](https://langfuse.com/imprint)[Cookie Policy](https://langfuse.com/cookie-policy)
© 2022–2026 Langfuse GmbH
/ Finto Technologies Inc.
Design by [Altalogy](https://altalogy.com/?ref=langfuse)
On this page
[Why I Like This Agent](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#why-i-like-this-agent)[How Does the Agent Work?](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#how-does-the-agent-work)[1. Initial Query](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#1-initial-query)[2. Follow-Up Questions](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#2-follow-up-questions)[3. Search Queries](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#3-search-queries)[4. Search Engine Calls](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#4-search-engine-calls)[5. Learnings from the Content](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#5-learnings-from-the-content)[6. Markdown Report](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#6-markdown-report)[Comparison With Other AI Research Tools](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#comparison-with-other-ai-research-tools)[David Zhang’s Open Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#david-zhangs-open-deep-research)[OpenAI’s Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#openais-deep-research)[Perplexity Pro Deep Research](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#perplexity-pro-deep-research)[Takeaways](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#takeaways)[Other Open Source Research Agent Frameworks](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#other-open-source-research-agent-frameworks)[What's Next?](https://langfuse.com/blog/2025-02-20-the-agent-deep-dive-open-deep-research#whats-next)
[🐐Hiring in Europe and SFLooking for GOATS!](https://langfuse.com/careers)
[GitHub](https://github.com/langfuse/langfuse)[X](https://x.com/langfuse)
`Ask AI``A`
`A`

