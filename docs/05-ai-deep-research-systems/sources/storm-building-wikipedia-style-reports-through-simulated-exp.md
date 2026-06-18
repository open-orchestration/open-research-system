# STORM: Building Wikipedia-Style Reports Through Simulated Expert ...

Source: https://starlog.is/articles/ai-agents/stanford-oval-storm

> your AI agent picks dependencies from memory; give it dated facts — [try starlog.dev ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=memory) [vet your agent's deps ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=memory) vibe-coding is fine. vibe-importing isn’t. — [try starlog.dev ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=vibe) [vibe-importing isn’t fine ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=vibe) your agent has never seen your private packages — [try starlog.dev ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=private) [facts for private packages ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=private) a linter for the dependencies your AI agent picks — [try starlog.dev ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=linter) [a linter for agent deps ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=banner&utm_content=linter)
×
[ [STARLOG] ](https://starlog.is/)
[Articles](https://starlog.is/) [Search](https://starlog.is/search) [RSS](https://starlog.is/rss.xml) [starlog.dev ↗](https://starlog.dev/?utm_source=starlog.is&utm_medium=header&utm_content=nav "facts-vetting for AI coding agents") [Login](https://starlog.is/login)
[ ← Back to Articles ](https://starlog.is/) [ AI Agents ](https://starlog.is/categories/ai-agents)
# STORM: Building Wikipedia-Style Reports Through Simulated Expert Conversations
★ 28.2k Python 91/100 May 9, 2026
[ ![Rob Ragan](https://starlog.is/avatars/rob-ragan.svg) Rob Ragan Offensive security researcher and AI agent architect. Founder of Starlog. ](https://starlog.is/authors/rob-ragan) [ [ View on GitHub ] ](https://github.com/stanford-oval/storm)
[ ▶ LISTEN HD ]
1x
[Hook](https://starlog.is/articles/ai-agents/stanford-oval-storm#hook) [Context](https://starlog.is/articles/ai-agents/stanford-oval-storm#context) [Technical](https://starlog.is/articles/ai-agents/stanford-oval-storm#technical-insight) [Gotcha](https://starlog.is/articles/ai-agents/stanford-oval-storm#gotcha) [Verdict](https://starlog.is/articles/ai-agents/stanford-oval-storm#verdict)
# STORM: Building Wikipedia-Style Reports Through Simulated Expert Conversations
## Hook
What if the best way to make an LLM research a topic wasn't to ask it directly, but to make it argue with itself? STORM's 70,000+ users are proving that simulated expert conversations generate deeper research than any single prompt ever could.
## Context
Ask GPT-4 to write a comprehensive article about quantum computing, and you'll get something that sounds authoritative but lacks depth, misses important perspectives, and hallucinates citations. The problem isn't the model's capability—it's that a single prompt forces the LLM into a local minimum of knowledge. Human researchers don't work this way. They start broad, discover perspectives they hadn't considered, ask follow-up questions, chase down references, and iteratively refine their understanding.
STORM, developed by Stanford's Oval lab and published at NAACL 2024, tackles this by breaking knowledge curation into stages that mirror human research workflows. Instead of generating articles directly, it first conducts research through simulated conversations between a Wikipedia writer persona and topic experts, grounded in web search results. This pre-writing stage discovers diverse perspectives, generates outlines, and collects properly cited references before any article writing begins. The result is a system that has been tested by over 70,000 users for Wikipedia-style article creation, demonstrating that architecture matters as much as model size when building LLM research systems.
## Technical Insight
STORM's architecture is built on two foundational insights: perspective diversity and conversational iteration. The pre-writing stage begins with perspective-guided question asking, where the system first identifies similar topics to discover viewpoints the researcher might not have considered. For a topic like "impact of social media on democracy," STORM doesn't just ask obvious questions—it surveys related articles to discover perspectives from psychology, political science, technology ethics, and media studies angles.
The system then simulates conversations between a writer agent and multiple expert agents, each grounded in real-time web search results. Here's how you might customize the conversation depth using STORM's Python API:

```
from knowledge_storm import STORMWikiRunnerArguments, STORMWikiRunner
from knowledge_storm import STORMWikiLMConfigs
from dspy import OpenAI

# Configure LLM settings for different components
lm_configs = STORMWikiLMConfigs()
lm_configs.set_conv_simulator_lm(OpenAI(model='gpt-4', max_tokens=500))
lm_configs.set_question_asker_lm(OpenAI(model='gpt-4', max_tokens=300))
lm_configs.set_outline_gen_lm(OpenAI(model='gpt-4', max_tokens=1000))
lm_configs.set_article_gen_lm(OpenAI(model='gpt-4', max_tokens=3000))

# Configure research depth
args = STORMWikiRunnerArguments(
    max_conv_turn=5,  # Conversation depth per perspective
    max_perspective=3,  # Number of expert perspectives
    search_top_k=10,  # References per search query
)

runner = STORMWikiRunner(args, lm_configs)
runner.run(
    topic='Impact of Social Media on Democracy',
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True
)

```

This modular design, built on DSPy, allows you to swap LLM providers (via litellm), customize retrieval sources, or even replace components entirely. The conversation simulation isn't just theater—each turn allows the writer agent to ask follow-up questions based on previous answers, mimicking how humans dig deeper when they encounter surprising information.
The writing stage then synthesizes the collected outline and references into a coherent article with proper citations. Because references were collected during conversation simulation rather than generated post-hoc, citation accuracy improves dramatically. STORM tracks which search results supported which parts of the conversation, creating a grounded citation graph.
Co-STORM extends this architecture with human-in-the-loop collaboration, introducing a turn management protocol where human users can interrupt LLM experts, steer conversations, and contribute their own knowledge. The system maintains a dynamic mind map that organizes discovered information hierarchically, reducing cognitive load when exploring complex topics. This collaborative discourse model represents a shift from autonomous agents toward AI systems that augment human research workflows rather than replacing them.
The technical cleverness lies in how STORM avoids the pitfalls of naive RAG implementations. Instead of retrieving once and generating, it interleaves retrieval with iterative questioning. Instead of a single perspective, it explicitly seeks diversity. Instead of direct article generation, it builds scaffolding through outlines and structured conversations. These architectural choices compound: better questions lead to better retrieval, which enables deeper follow-ups, which produce richer outlines, which guide more coherent article generation.
## Gotcha
STORM is not a magic "research paper generator" button. The output requires substantial human editing and fact-checking—the developers explicitly position it as a pre-writing tool, not a publication-ready article creator. You're essentially getting a well-researched first draft with an outline and citations that need verification. For Wikipedia articles or comprehensive reports, this is valuable. For blog posts or marketing content where you need polish and voice, the editing overhead might exceed writing from scratch.
The economics can also hurt. Simulating multiple conversation turns with multiple expert perspectives means many LLM API calls per article—potentially dozens of GPT-4 requests for a single topic. During testing, comprehensive reports can cost $5-15 in API fees depending on topic complexity and configuration. If you're generating hundreds of reports, those costs compound quickly. The retrieval quality ceiling is another constraint: STORM can only be as good as its search backend. If your topic requires access to specialized databases, academic journals, or proprietary sources that aren't web-accessible, the simulated conversations will be grounded in incomplete information. The system also struggles with highly narrow or emerging topics where there aren't enough similar articles to discover diverse perspectives—the perspective-guided approach assumes a landscape of related content to survey.
## Verdict
Use if you're building research tools for academics, journalists, or content strategists who need comprehensive reports on unfamiliar topics with proper citations. STORM excels when research breadth matters more than writing polish, when you're willing to invest API costs for quality, and when your topics are well-covered enough on the web to support perspective discovery. It's particularly valuable if you're creating Wikipedia-style encyclopedic content or need to get up to speed on complex topics quickly with a structured outline and reference list. Skip if you need publication-ready content without editing, are working with highly specialized topics in closed domains, need fast answers rather than deep research, or are optimizing for API cost efficiency over research thoroughness. For quick summaries or narrow technical documentation, traditional RAG or search-based systems will serve you better at a fraction of the cost.
##  // KNOWLEDGE GRAPH 
Interactive dependency map powered by [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
CONCEPTS FILES
+ - FIT LAYOUT EXPAND
// WALKTHROUGH
< PREV NEXT >
Knowledge graph could not be loaded.
##  // RELATED 
[ AI Agents LobeHub: The Agent Orchestration Platform That Treats AI as Your Employee, Not Your Chatbot ★ 78.5k Jun 10, 2026 ](https://starlog.is/articles/ai-agents/lobehub-lobehub) [ AI Agents SkillOpt: Training Prompt Libraries Like Neural Networks for Frozen LLMs ★ 7.6k Jun 16, 2026 ](https://starlog.is/articles/ai-agents/microsoft-skillopt) [ AI Agents Building a Stateful Email Client on the Edge: Inside Cloudflare's Agentic Inbox ★ 4.6k Jun 16, 2026 ](https://starlog.is/articles/ai-agents/cloudflare-agentic-inbox) [ AI Agents OpenSRE: Building the SWE-bench for Production Incidents ★ 6.7k Jun 9, 2026 ](https://starlog.is/articles/ai-agents/tracer-cloud-opensre)
[ AI Agents LobeHub: The Agent Orchestration Platform That Treats AI as Your Employee, Not Your Chatbot ★ 78.5k Jun 10, 2026 ](https://starlog.is/articles/ai-agents/lobehub-lobehub)
[ AI Agents SkillOpt: Training Prompt Libraries Like Neural Networks for Frozen LLMs ★ 7.6k Jun 16, 2026 ](https://starlog.is/articles/ai-agents/microsoft-skillopt)
[ AI Agents Building a Stateful Email Client on the Edge: Inside Cloudflare's Agentic Inbox ★ 4.6k Jun 16, 2026 ](https://starlog.is/articles/ai-agents/cloudflare-agentic-inbox)
Offsec tools & AI agent intel. No noise. Delivered direct. 
[ Subscribe ]
// SHARE 
[ [ X ] ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fstarlog.is%2Farticles%2Fai-agents%2Fstanford-oval-storm&text=STORM%3A%20Building%20Wikipedia-Style%20Reports%20Through%20Simulated%20Expert%20Conversations)[ [ LinkedIn ] ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fstarlog.is%2Farticles%2Fai-agents%2Fstanford-oval-storm&title=STORM%3A%20Building%20Wikipedia-Style%20Reports%20Through%20Simulated%20Expert%20Conversations)[ [ Reddit ] ](https://www.reddit.com/submit?url=https%3A%2F%2Fstarlog.is%2Farticles%2Fai-agents%2Fstanford-oval-storm&title=STORM%3A%20Building%20Wikipedia-Style%20Reports%20Through%20Simulated%20Expert%20Conversations)[ [ HN ] ](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fstarlog.is%2Farticles%2Fai-agents%2Fstanford-oval-storm&t=STORM%3A%20Building%20Wikipedia-Style%20Reports%20Through%20Simulated%20Expert%20Conversations)
##  // CODEBASE INTELLIGENCE 
Architecture Overview Architecture Diagram Repository Health Components Entry Points Core Abstractions Quality Signals
Metrics below are heuristic approximations computed from repository structure, not authoritative measurements.
Data Flow Decision Guide
#### Best for
#### Skip when
Dependencies
agentic-ragdeep-researchemnlp2024knowledge-curationlarge-language-modelsnaaclnlpreport-generationretrieval-augmented-generation
> Curated by [Rob Ragan](https://www.linkedin.com/in/robragan/) // Offsec & AI agent intel. No noise. 
> Partner inquiries: partner@starlog.is
> [starlog.dev](https://starlog.dev/?utm_source=starlog.is&utm_medium=footer&utm_content=global) — facts-vetting for AI coding agents → 

