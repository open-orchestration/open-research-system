# How Anthropic Built Their Multi-Agent Research System: Architecture ...

Source: https://cuizhanming.com/anthropic-multi-agent-research-architecture/

[**Colourful Codes**](https://cuizhanming.com/)
  * [Home](https://cuizhanming.com/)
  * [Curriculum](https://cuizhanming.com/cv)
  * [Contact](https://cuizhanming.com/contact)
  * [Old Blog ](https://old.cuizhanming.com/)


🎨 Modern ▼
✨
Modern Clean & contemporary
✓
📰
Classic Traditional blog style
✓
[ai](https://cuizhanming.com/categories#ai),  [architecture](https://cuizhanming.com/categories#architecture),  [engineering](https://cuizhanming.com/categories#engineering), 
# How Anthropic Built Their Multi-Agent Research System: Architecture Lessons from Production
![Cui](https://cuizhanming.com/assets/images/avatar.jpg) Cui [Follow](https://twitter.com/zhanmingcui) Mar 24, 2026 ·  8 mins read 
![How Anthropic Built Their Multi-Agent Research System: Architecture Lessons from Production](https://cuizhanming.com/assets/images/2026/2026-03-24-anthropic-multi-agent-research-architecture-header.svg)
Share this 
[Share](https://www.addtoany.com/share#url=https%3A%2F%2Fcuizhanming.com%2Fanthropic-multi-agent-research-architecture%2F&title=How%20Anthropic%20Built%20Their%20Multi-Agent%20Research%20System%3A%20Architecture%20Lessons%20from%20Production%20%7C%20Colourful%20Codes) [Facebook](https://cuizhanming.com/#facebook) [Twitter](https://cuizhanming.com/#twitter)
Claude’s new Research capabilities represent a significant evolution in AI agent architecture—moving from single-agent systems to coordinated multi-agent orchestration at production scale. Anthropic’s engineering team recently shared the architectural principles and hard-won lessons from building this system. Here’s what makes their approach work.
## The Core Problem: Why Multi-Agent?
Research tasks are inherently unpredictable. You can’t hardcode a fixed path for exploring complex topics—the process is dynamic and path-dependent. When humans conduct research, they continuously update their approach based on discoveries, following leads that emerge during investigation.
This unpredictability is precisely why AI agents excel at research. But there’s a catch: **single agents hit limits**. Even generally-intelligent agents operating alone face constraints when the work requires:
  * **Parallel exploration** of multiple independent directions
  * **Context beyond what fits** in a single window (>200K tokens)
  * **Interfacing with numerous complex tools** simultaneously


Multi-agent systems solve this through distributed context windows and parallel reasoning capacity.
## Performance Impact: The Numbers
Anthropic’s internal evaluations show compelling results:
**Multi-agent (Opus 4 lead + Sonnet 4 workers) vs. Single Opus 4:**
  * **90.2% improvement** on internal research benchmarks
  * **80% of performance variance** explained by token usage alone
  * **15x token usage** compared to single-agent chat (4x for single agents)


### What Drives Performance?
Analysis of the BrowseComp evaluation (which tests browsing agents’ ability to locate hard-to-find information) revealed three factors explaining 95% of variance:
  1. **Token usage** (80% of variance) - More tokens = more reasoning capacity
  2. **Tool calls** - Parallel execution enables breadth-first exploration
  3. **Model choice** - Upgrading to Sonnet 4 > doubling token budget on Sonnet 3.7


**Example success case:** When asked to identify all board members of IT companies in the S&P 500, the multi-agent system decomposed the task across subagents and found correct answers. The single-agent system failed with slow, sequential searches.
## Architecture: Orchestrator-Worker Pattern
The Research system uses a **lead agent** coordinating specialized **subagents** that operate in parallel.
### The Flow

```
User Query
    ↓
LeadResearcher Agent
    ├─ Analyzes query
    ├─ Develops strategy
    ├─ Spawns parallel Subagents
    │       ↓
    │   Subagent 1: AI agent companies 2025
    │   Subagent 2: Market trends analysis  
    │   Subagent 3: Technical capabilities
    │       ↓
    │   [Each performs iterative web searches]
    │       ↓
    ├─ Synthesizes findings
    ├─ Decides: more research needed?
    │   ├─ Yes → spawn more subagents
    │   └─ No → proceed to citation
    ↓
CitationAgent
    ├─ Processes documents
    ├─ Identifies specific locations
    ├─ Attributes all claims to sources
    ↓
Final Research Report (with citations)

```

### Key Architectural Choices
**1. Memory Persistence**
When context exceeds 200K tokens, truncation is inevitable. The LeadResearcher saves its plan to Memory to retain critical context across truncations.
**2. Interleaved Thinking**
Subagents use Claude’s extended thinking mode to:
  * Plan their approach before executing
  * Evaluate tool results after each search
  * Identify gaps and refine next queries adaptively


**3. Dynamic Multi-Step Search**
Unlike static RAG (Retrieval Augmented Generation), which fetches chunks based on similarity, the system:
  * Dynamically finds relevant information
  * Adapts to new findings in real-time
  * Analyzes results iteratively to formulate high-quality answers


## Prompt Engineering Principles for Multi-Agent Systems
Building a production multi-agent system required extensive prompt iteration. Here are the key principles that worked:
### 1. Think Like Your Agents
**Problem:** Without understanding agent behavior, prompt changes are shots in the dark.
**Solution:** Build simulations in Anthropic Console using exact prompts/tools from production. Watch agents work step-by-step.
**Failure modes revealed:**
  * Agents continuing when they already had sufficient results
  * Overly verbose search queries
  * Incorrect tool selection


### 2. Teach the Orchestrator to Delegate
**Problem:** Vague instructions led to duplicated work and gaps.
Early attempts: _“Research the semiconductor shortage”_
**Result:**
  * One subagent explored 2021 automotive chip crisis
  * Two others duplicated work on 2025 supply chains
  * No effective division of labor


**Solution:** Detailed task descriptions with:
  * Clear objective
  * Expected output format
  * Guidance on tools and sources to use
  * Explicit task boundaries


### 3. Scale Effort to Query Complexity
**Problem:** Agents struggled to judge appropriate effort.
**Solution:** Embed explicit scaling rules in prompts:
  * **Simple fact-finding:** 1 agent, 3-10 tool calls
  * **Direct comparisons:** 2-4 subagents, 10-15 calls each
  * **Complex research:** 10+ subagents with divided responsibilities


Without these guidelines, early versions over-invested in simple queries.
### 4. Tool Design is Critical
**Insight:** Agent-tool interfaces are as critical as human-computer interfaces.
**Problem:** With MCP servers exposing external tools, agents encounter unseen tools with varying description quality. Bad descriptions send agents down wrong paths.
**Solution:** Explicit heuristics embedded in prompts:
  * Examine all available tools first
  * Match tool usage to user intent
  * Search web for broad external exploration
  * Prefer specialized tools over generic ones


**Innovation:** Tool-testing agent that:
  * Attempts to use flawed MCP tools
  * Rewrites tool descriptions to avoid failures
  * Tests tools dozens of times to find nuances
  * **Result:** 40% decrease in task completion time for future agents


### 5. Let Agents Improve Themselves
**Discovery:** Claude 4 models excel at prompt engineering.
**Process:**
  1. Give model a prompt + failure mode
  2. Model diagnoses why agent is failing
  3. Model suggests improvements


**Application:** Tool description improvement resulted in dramatically faster task completion.
### 6. Start Wide, Then Narrow
**Strategy:** Mirror expert human research—explore landscape before drilling into specifics.
**Problem:** Agents default to overly long, specific queries returning few results.
**Solution:** Prompt agents to:
  1. Start with short, broad queries
  2. Evaluate what’s available
  3. Progressively narrow focus


### 7. Guide the Thinking Process
**Extended thinking** serves as a controllable scratchpad:
**LeadResearcher uses thinking to:**
  * Plan approach
  * Assess which tools fit the task
  * Determine query complexity and subagent count
  * Define each subagent’s role


**Subagents use interleaved thinking to:**
  * Evaluate quality of tool results
  * Identify gaps
  * Refine next query


**Impact:** Improved instruction-following, reasoning, and efficiency in testing.
### 8. Parallel Tool Calling Transforms Speed
**Early approach:** Sequential searches → painfully slow
**Two kinds of parallelization:**
  1. **Lead agent:** Spins up 3-5 subagents in parallel (not serially)
  2. **Subagents:** Use 3+ tools in parallel per agent


**Result:** Up to **90% reduction** in research time for complex queries
* * *
## Evaluation Challenges for Multi-Agent Systems
Traditional evals assume AI follows the same steps each time. Multi-agent systems are non-deterministic—different paths can reach the same correct answer.
**Key evaluation insights:**
**1. Observability is Essential**
With multiple agents exploring in parallel, you need:
  * Step-by-step execution traces
  * Tool call logs for each subagent
  * Intermediate thinking outputs
  * Success/failure metrics per subtask


**2. Focus on Outcomes, Not Paths**
Don’t evaluate whether the agent took a specific sequence of steps. Evaluate whether it:
  * Found all required information
  * Cited sources correctly
  * Arrived at accurate conclusions
  * Used resources efficiently


**3. Fast Iteration Loops**
Anthropic built test cases that:
  * Represent real-world complexity
  * Cover common failure modes
  * Run quickly enough for rapid iteration
  * Provide clear signal on regressions


## When to Use (and Not Use) Multi-Agent Systems
### Good Fit: Tasks With
✅ **High parallelization potential** (breadth-first exploration)  
✅ **Information exceeding single context windows**  
✅ **Numerous complex tools** requiring specialized handling  
✅ **Value justifying 15x token cost** compared to chat
### Poor Fit: Domains With
❌ **Few truly parallelizable tasks** (e.g., most coding)  
❌ **Need for all agents to share the same context**  
❌ **Many real-time dependencies** between agents  
❌ **Tight token budgets** or low-value tasks
**Economic reality:** Multi-agent systems burn through tokens fast (15x chat). They require tasks where the value is high enough to pay for increased performance.
## Practical Takeaways for Builders
If you’re building multi-agent systems, Anthropic’s lessons translate to these actionable principles:
### Architecture
  1. **Use orchestrator-worker patterns** for coordinating parallel work
  2. **Persist critical context** explicitly (don’t rely on infinite context windows)
  3. **Design for dynamic adaptation** , not static pipelines
  4. **Implement interleaved thinking** for continuous plan refinement


### Prompting
  1. **Simulate before deploying** - build exact replicas in sandboxes to observe behavior
  2. **Embed scaling heuristics** - teach effort-to-complexity matching explicitly
  3. **Invest in tool descriptions** - they’re as important as the tools themselves
  4. **Start broad, narrow iteratively** - don’t let agents over-specify too early


### Evaluation
  1. **Measure outcomes, not paths** - embrace non-determinism in agent behavior
  2. **Build observability first** - you can’t improve what you can’t see
  3. **Create fast feedback loops** - rapid iteration beats perfect evals


### Economics
  1. **Calculate value-to-cost ratio** - 15x token usage needs 15x+ value
  2. **Parallelize ruthlessly** - it’s the key performance multiplier
  3. **Upgrade models aggressively** - Sonnet 4 > 2x Sonnet 3.7 budget


## The Future of Multi-Agent Systems
Anthropic’s Research feature demonstrates that multi-agent systems work at production scale when designed with clear principles. The key insight: **intelligence scales through coordination** , not just through better individual models.
Just as human societies became exponentially more capable through collective intelligence, AI agents will unlock new capabilities through effective multi-agent orchestration. But this requires:
  * **Thoughtful architecture** (orchestrator-worker patterns)
  * **Extensive prompt engineering** (heuristics, not rigid rules)
  * **Outcome-based evaluation** (embracing non-determinism)
  * **Economic viability** (matching cost to task value)


As LLMs continue improving, multi-agent systems become increasingly viable. The 90.2% performance improvement Anthropic achieved suggests we’re still in early days of exploring this space.
The question isn’t whether multi-agent systems will become standard—it’s which architectural patterns will emerge as best practices. Anthropic’s production experience provides a valuable starting point.
* * *
## Further Reading
  * [Anthropic Research Feature Announcement](https://www.anthropic.com/news/research)
  * [Claude Extended Thinking Documentation](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  * [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
  * [Anthropic Console for Agent Simulation](https://console.anthropic.com/)


**Source:** [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) - Anthropic Engineering Blog
[anthropic](https://cuizhanming.com/tags#anthropic) [claude](https://cuizhanming.com/tags#claude) [multi-agent systems](https://cuizhanming.com/tags#multi-agent%20systems) [ai agents](https://cuizhanming.com/tags#ai%20agents) [system design](https://cuizhanming.com/tags#system%20design) [prompt engineering](https://cuizhanming.com/tags#prompt%20engineering)
##### Join Newsletter
Get the latest news right in your inbox. We never spam! 
Subscribe
![Cui](https://cuizhanming.com/assets/images/avatar.jpg)
##### Written by Cui [Follow](https://twitter.com/zhanmingcui)
Hi, I am Z, the coder for cuizhanming.com! 
Load Comments 
Click to load Disqus comments
[ ![](https://assets/images/2026/2026-03-23-nvidia-zero-trust-ai-factories-header.svg) Building Zero-Trust AI Factories: NVIDIA's Approach to Confidential Computing](https://cuizhanming.com/nvidia-zero-trust-ai-factories/)
[ Claude Code Auto Mode: Balancing Safety and Autonomy ![](https://cuizhanming.com/assets/images/2026/2026-03-27-claude-code-auto-mode-balancing-safety-and-autonomy-header.png) ](https://cuizhanming.com/claude-code-auto-mode-balancing-safety-and-autonomy/)
Copy link
✓
Thanks for sharing!
Find any service
[AddToAny](https://www.addtoany.com "Share Buttons")
[More…](https://cuizhanming.com/anthropic-multi-agent-research-architecture/#addtoany "Show all")
**Colourful Codes** Copyright © 2026. [Github](https://github.com/cuizhanming)

