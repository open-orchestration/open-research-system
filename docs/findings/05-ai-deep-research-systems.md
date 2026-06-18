# Findings — AI Deep-Research Systems

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- STORM (Stanford OVAL, NAACL 2024) splits long-form report generation into a **pre-writing stage** (research the topic, collect references, build an outline) and a **writing stage** (generate the full article with citations from that outline) — research and writing are deliberately separated. — [Stanford STORM Research Project](https://storm-project.stanford.edu/research/storm/)
- STORM's pre-writing engine is its core trick: it (1) discovers diverse *perspectives* on the topic, (2) simulates conversations where writers holding those perspectives ask questions to a topic expert grounded on trusted internet sources, then (3) curates the answers into an outline — "Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking." — [Stanford STORM Research Project](https://storm-project.stanford.edu/research/storm/)
- Multi-perspective simulated questioning measurably beats single-prompt generation: STORM's articles were judged more organized (+25% absolute) and broader in coverage (+10%) than an outline-driven RAG baseline. — [GitHub - stanford-oval/storm](https://github.com/stanford-oval/storm)
- The simulated conversation is not theater — each turn lets the writer agent ask *follow-up* questions based on prior answers, mimicking how a human digs deeper after encountering surprising information. — [STORM: Building Wikipedia-Style Reports Through Simulated Expert Conversations](https://starlog.is/articles/ai-agents/stanford-oval-storm)
- Co-STORM adds human-in-the-loop collaborative curation, where the human can either observe the agent discourse to understand the topic or inject utterances to steer the discussion focus. — [GitHub - stanford-oval/storm](https://github.com/stanford-oval/storm)
- GPT-Researcher uses a planner/executor/publisher decomposition: a planner generates the research sub-questions, parallel execution agents gather information per question, and a publisher aggregates and filters the summaries into one comprehensive cited report. — [GitHub - assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- These systems exist specifically to counter base-LLM failure modes: LLMs hallucinate from outdated training data and have token limits insufficient for long reports, and "selective web sources can introduce bias" — so the architecture is built around fresh retrieval, breadth of sources, and forming an *objective* multi-question view. — [GitHub - assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- A known residual risk even in STORM is "source bias transfer and over-association of unrelated facts" — grounding in retrieved sources reduces but does not eliminate distortion. — [Stanford STORM Research Project](https://storm-project.stanford.edu/research/storm/)

## Convergent vs contested
- **Convergent:** Both leading systems converge on the same blueprint — *decompose the topic into many sub-questions, retrieve per question (grounded in fresh external sources), then synthesize with citations.* Both treat breadth of perspective/source and explicit citation as the antidote to single-shot LLM hallucination, and both separate planning from writing.
- **Contested / open:** Mechanism differs — STORM gets breadth via *perspective discovery + simulated expert dialogue*; GPT-Researcher via a *planner generating an objective question set + parallel agents*. Whether simulated multi-agent conversation is worth its cost vs. a flat parallel-question planner is unresolved by the sources. Both also warn outputs "can make mistakes; please always check important information."

## Implications for the system (Phase 2)
- Adopt the two-stage spine: a research/pre-writing phase that produces an outline + a cited reference set, strictly *before* a writing phase that may only use those references — this is the central, evidence-backed pattern.
- Generate breadth deliberately: decompose into sub-questions AND seek multiple *perspectives* per topic; the +25%/+10% STORM result is direct evidence that perspective diversity, not just more retrieval, drives organized/broad output.
- Support follow-up questioning (iterative deepening on surprising findings) and an optional human-steer hook (Co-STORM style), and run sub-question gathering in parallel (GPT-Researcher) for latency.

## Gaps found → re-scan
- Sources cover STORM and GPT-Researcher well but omit **OpenAI/Anthropic/Gemini Deep Research** product architectures (named in the search) and give no comparative eval numbers across systems, latency/cost figures, or failure-rate benchmarks. Deep-dive queries: "OpenAI Deep Research / Gemini Deep Research agent architecture and evaluation", and "deep-research agent cost, latency, and citation-accuracy benchmarks".
