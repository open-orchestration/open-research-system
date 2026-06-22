[![The AI Engineer](https://substackcdn.com/image/fetch/$s_!Aaa2!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4da2c93c-e2ec-4f9e-9325-fc9889333554_400x400.png)](https://theaiengineer.substack.com/)
# [![The AI Engineer](https://substackcdn.com/image/fetch/$s_!WNCM!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d59ab7f-e8e2-413a-9440-75e54a314187_210x40.webp)](https://theaiengineer.substack.com/)
SubscribeSign in
![User's avatar](https://substackcdn.com/image/fetch/$s_!UoTk!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b3dca43-c984-41cc-a31a-b210ec08bddb_1024x1024.jpeg)
Discover more from The AI Engineer
Become dangerously good at AI Engineering.
Over 24,000 subscribers
Subscribe
By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).
Already have an account? Sign in
# Single-Agent Patterns
### ReAct, Plan-and-Execute, ReWOO, and Reflexion: same agent, four different ways to fail
[![Paolo Perrone's avatar](https://substackcdn.com/image/fetch/$s_!UoTk!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b3dca43-c984-41cc-a31a-b210ec08bddb_1024x1024.jpeg)](https://substack.com/@paoloap)
[Paolo Perrone](https://substack.com/@paoloap)
Apr 16, 2026
12
18
Share
## The Decision Pain
You built your first agent. It works on the demo. Then a customer asks it to do three things at once and it calls the same API four times, hallucinates an intermediate result, and returns a confidently wrong answer 40 seconds later.
You look at the logs. The agent reasoned about every step correctly in isolation. It just couldn’t see the full picture. It never planned ahead, never checked its own work, and you had no way to tell it to.
The problem isn’t the model. The problem is how you wired the loop. There are four established patterns for single-agent reasoning, and picking the wrong one is the difference between a reliable system and an expensive random walk. Here’s how to actually decide.
## TL;DR
  * **ReAct** (Reason + Act): the default. Think, act, observe, repeat. One LLM call per step. Great for exploratory tasks. Gets expensive fast on long chains.
  * **Plan-and-Execute** : plan all steps upfront, then execute sequentially with a cheaper model. Replans on failure. Fewer LLM calls, lower cost, inspectable before execution starts.
  * **ReWOO** (Reasoning Without Observation): plan once with placeholders, run all tools in parallel, synthesize at the end. Only 2 LLM calls total. 5x token efficiency over ReAct. Breaks if a tool returns something unexpected.
  * **Reflexion** : after each attempt, the agent critiques its own output and retries with that critique in memory. Improved HumanEval coding pass rates from 80% to 91%. Expensive: every retry is a full run.
  * **Pick based on the failure mode you can live with** : wasted tokens (ReAct), rigidity (ReWOO), latency (Reflexion), or replanning complexity (Plan-and-Execute).


**Next up: we’re breaking down how agent evaluation actually works, from tracing to benchmarks. Don’t miss it.**
Subscribe
## What Are We Even Comparing?
Before we evaluate individual patterns, let’s set the playing field.
Every AI agent, at its core, is an LLM running in a loop. It receives a goal, decides what to do next, takes an action (usually calling a tool), reads the result, and repeats until it’s done or gives up. We covered the fundamentals of this loop in [What is an AI Agent?](https://theaiengineer.substack.com/p/what-is-an-ai-agent) and the tool-calling mechanism that powers it in [What is Function Calling?](https://theaiengineer.substack.com/p/what-is-function-calling).
The patterns in this issue are all **single-agent** architectures: one LLM instance making decisions. Multi-agent systems (where multiple specialized agents coordinate) are a different problem entirely, and we’ll cover those in a dedicated comparison.
The differences between these four patterns come down to three design choices:
  1. **When does the agent plan?** Before execution (upfront), during execution (per-step), or not at all?
  2. **How many LLM calls does each task require?** One per step, two total, or N times the number of retries?
  3. **How does the agent handle failure?** Adapt on the fly, replan, ignore it, or retry with self-critique?


Every agent architecture you’ll encounter in production is some combination of answers to those three questions.
> **⚠️ Confusion Alert:** “Agent patterns” and “agent frameworks” are different things. ReAct is a _pattern_ : a way of structuring reasoning. LangGraph is a _framework_ : a library that implements multiple patterns. You can build a ReAct agent in LangGraph, CrewAI, or raw Python. The pattern is the architecture. The framework is the plumbing.
**Scope:** We’re comparing four single-agent reasoning patterns. We’re NOT covering multi-agent orchestration (CrewAI, AutoGen), prompt-only techniques (chain-of-thought, few-shot), or agent frameworks themselves. Those are separate issues.
[![](https://substackcdn.com/image/fetch/$s_!U2H3!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fd8fec4-c088-406d-a377-52fcf50bc999_1400x386.png)](https://substackcdn.com/image/fetch/$s_!U2H3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fd8fec4-c088-406d-a377-52fcf50bc999_1400x386.png)
## Head-to-Head Breakdown
Patterns are ordered simplest to most complex: ReAct, Plan-and-Execute, ReWOO, Reflexion. Each builds on concepts from the previous one.
### ReAct (Reason + Act)
**In one sentence:** The agent thinks about what to do next, does it, reads the result, and repeats until done.
[![](https://substackcdn.com/image/fetch/$s_!DGjA!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0805c014-12fd-4598-b338-3bc83ad123e5_1400x290.png)](https://substackcdn.com/image/fetch/$s_!DGjA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0805c014-12fd-4598-b338-3bc83ad123e5_1400x290.png)
ReAct, introduced by Yao et al. in 2022, is the pattern that made tool-using agents practical. The name says it: **Reason** about the situation, **Act** on that reasoning. The loop runs Thought → Action → Observation → Thought → Action → Observation until the agent decides it has enough information to answer.
This is what `create_react_agent` in LangGraph gives you out of the box. It’s what most no-code agent platforms run under the hood. If someone says “agent” without further qualification, they almost always mean a ReAct loop.
> 🏗️ **Engineering Lesson:** ReAct’s biggest operational advantage is debuggability. Every thought step is logged, so when something breaks, you can trace exactly where the reasoning went wrong. In regulated industries (finance, healthcare), this audit trail isn’t optional. One practitioner using LangGraph for 40+ client projects put it simply: they moved from AutoGPT’s unstructured loops to ReAct specifically because they could finally trace why the agent chose wrong.[1](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-1)
👍 **The good:**
  * Naturally adaptive. If a tool fails or returns something unexpected, the agent re-reasons on the next step and changes course.
  * Grounding reduces hallucinations. By acting and observing real results between reasoning steps, the agent stays tethered to reality instead of chaining unsupported inferences.
  * Universally supported. Every major framework (LangGraph, LangChain, NeMo) has a ReAct implementation. It’s the default starting point.


👎 **The bad:**
  * Token cost scales linearly with task complexity. Every step requires a full LLM call with the entire conversation history. A 10-step task means 10 LLM calls, each one longer than the last because context accumulates.
  * Prone to reasoning loops. If the agent gets confused, it can enter repetitive cycles where it keeps calling the same tool with the same input, burning tokens without making progress.
  * Myopic by design. The agent only sees one step ahead. It can’t optimize the overall path because it never plans globally.


🎯 **Best for:** Exploratory tasks where the next step depends heavily on the previous result. Customer support agents that need to look up account info, check policies, and compose a response dynamically. Research assistants that search, read, and synthesize.
🚧 **The ceiling:** When your task consistently needs more than 5-7 reasoning steps, ReAct’s per-step LLM calls become a cost and latency problem. If you’re spending more on agent reasoning than on the actual tools, it’s time to separate planning from execution.[2](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-2)
### Plan-and-Execute
**In one sentence:** A planner LLM creates a full step-by-step plan upfront, a cheaper executor runs each step, and a replanner adjusts if anything breaks.
[![](https://substackcdn.com/image/fetch/$s_!yuhe!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d1e5e8c-96bf-4d96-b067-057d90d2023c_1400x320.png)](https://substackcdn.com/image/fetch/$s_!yuhe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d1e5e8c-96bf-4d96-b067-057d90d2023c_1400x320.png)
Plan-and-Execute addresses ReAct’s fundamental limitation: the agent never sees the big picture. Instead of deciding one step at a time, a powerful model (like GPT-4o or Claude Sonnet) analyzes the full task and generates a plan: a DAG of subtasks with dependencies. A simpler, cheaper model then executes each step. If a step fails, a replanner revises the remaining steps.
The plan is inspectable before execution starts. You can log it, validate it, or show it to a human for approval. You know what the agent will try to do before it starts doing it.
👍 **The good:**
  * Drastically fewer LLM calls. The planner makes one LLM call. The executor runs tools directly without re-reasoning each step. A replanner call fires only on failure
  * You can use different models for different phases. An expensive reasoning model plans, a cheap fast model executes. This alone cuts costs significantly compared to running a frontier model on every ReAct step.
  * The executor skips the per-step reasoning overhead that dominates ReAct latency. A 10-step task that needs 10 LLM calls in ReAct needs 1-2 in Plan-and-Execute


👎 **The bad:**
  * Rigid when reality surprises you. If step 3 returns something the planner didn’t anticipate, the plan can derail. Replanning helps, but adds complexity and latency.
  * The planner can only plan for what it can foresee. Novel edge cases or ambiguous tasks produce bad plans, and a bad plan sends the executor confidently down the wrong path for every remaining step.
  * More architectural complexity to build and maintain than a ReAct loop.


🎯 **Best for:** Well-defined multi-step workflows where you can reasonably predict the sequence. Processing insurance claims, generating financial reports, orchestrating data pipeline tasks. Anything where you’d write a checklist for a human to follow.
🚧 **The ceiling:** When the problem space is too dynamic or too ambiguous for upfront planning. If replanning fires on most tasks, you’re paying the planning cost AND the adaptation cost. At that point, you’re better off with ReAct’s step-by-step flexibility or a graph-based agent that can handle branching natively.
**Know an engineer who’s wiring their first agent loop and wondering why it keeps calling the same API? Forward this.**
[Share](https://theaiengineer.substack.com/p/the-4-single-agent-patterns?utm_source=substack&utm_medium=email&utm_content=share&action=share)
### ReWOO (Reasoning Without Observation)
**In one sentence:** Two LLM calls total: one to plan every step with placeholders for results it doesn’t have yet, one to synthesize after all tools run in parallel. 
[![](https://substackcdn.com/image/fetch/$s_!vQKQ!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d0dce38-3634-486b-8b1c-f9ffbb024405_1400x300.png)](https://substackcdn.com/image/fetch/$s_!vQKQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d0dce38-3634-486b-8b1c-f9ffbb024405_1400x300.png)
ReWOO separates planning from execution even more aggressively than Plan-and-Execute. The planner writes out every step in one pass, using variables for results it can’t see yet: “#E1 = Search[’2024 Australian Open winner’]. #E2 = Search[’hometown of #E1’].” The worker executes all tool calls, running independent ones in parallel. The solver reads every result and produces the final answer.
👍 **The good:**
  * Token efficiency is unmatched. The original paper reports 5x token efficiency and 4% accuracy improvement on HotpotQA compared to ReAct.[3](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-3)
  * Parallel execution. Independent tool calls run simultaneously. For tasks like “get weather in three cities,” ReWOO fires all three searches at once instead of waiting for each one.
  * Modular failure isolation. If one tool fails, the solver can still work with the other results. The system doesn’t halt on a single failure.


👎 **The bad:**
  * Zero mid-execution adaptation. If step 2’s result means step 4 should change, ReWOO won’t catch that. The plan was locked in during the first LLM call.
  * Placeholder dependency chains can break. If #E1 returns something the planner didn’t expect, #E2 (which references #E1) may get garbage input.
  * Requires predictable task structures. If you can’t anticipate which tools you’ll need upfront, ReWOO can’t plan for them.


🎯 **Best for:** Standardized operational workflows with multiple independent data lookups. Generating reports from several independent data sources. Multi-hop Q&A where the questions are known upfront.
🚧 **The ceiling:** Any task where tools might return unexpected results that should change the plan. If you need conditional branching (”if the API returns X, do this; if it returns Y, do that”), ReWOO’s upfront planning can’t handle it. Fall back to Plan-and-Execute with replanning or ReAct.[4](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-4)
### Reflexion
**In one sentence:** After each full attempt, the agent evaluates its own output, writes a verbal self-critique, stores it in memory, and retries with that critique as context.
[![](https://substackcdn.com/image/fetch/$s_!c2Vh!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac3c3ce1-1644-4858-8c5d-ad5c9d750ddb_1400x360.png)](https://substackcdn.com/image/fetch/$s_!c2Vh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac3c3ce1-1644-4858-8c5d-ad5c9d750ddb_1400x360.png)
Reflexion, introduced by Shinn et al.[5](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-5), adds something the other three patterns lack: the ability to learn from failure within a single session. After the agent produces a result, an evaluator scores it (run the unit tests, validate against a schema, or check the output against expected results). If the score is below threshold, a self-reflection module generates a natural language analysis of what went wrong. That reflection goes into an episodic memory buffer, and the agent retries the entire task with its past mistakes as context.
This is the pattern that makes agents meaningfully better at coding tasks. On HumanEval, Reflexion improved GPT-4’s pass rate from 80% to 91%. On decision-making tasks in AlfWorld, ReAct + Reflexion completed 130 out of 134 tasks.[6](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-6)
We explored the concept of agent memory in [Agent Memory](https://theaiengineer.substack.com/p/agent-memory). Reflexion’s episodic memory buffer is a specific implementation: short-term, verbal, scoped to the current task.
👍 **The good:**
  * Genuine improvement across retries. Unlike simply re-running the same prompt (which often produces the same error), Reflexion’s verbal memory steers the agent away from previously failed approaches.
  * The only pattern here that gets better on the same task. ReAct, Plan-and-Execute, and ReWOO run once and return whatever they get. Reflexion runs, fails, learns why, and tries again with that knowledge.
  * Works with any underlying pattern. You can add Reflexion on top of ReAct, Plan-and-Execute, or even ReWOO.


👎 **The bad:**
  * Expensive. Every retry is a full task execution. If the agent needs 3 attempts, that’s 3x the cost of a single run, plus the evaluation and reflection overhead.
  * Self-evaluation is only as good as the evaluator. If the agent can’t tell its output is wrong (or if “wrong” is subjective), reflections become vague and unhelpful. A 2025 replication study found that single-agent Reflexion consistently repeats earlier misconceptions across retries because the same model generates both the output and the critique, reinforcing its own blind spots.[7](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-7)
  * Latency multiplies with retries. Not viable for real-time applications where the user is waiting.


🎯 **Best for:** Tasks with clear, automated success criteria. Code generation (run the tests), data extraction (validate against a schema), mathematical reasoning (check the answer). Anything where you can tell the agent definitively whether it succeeded.
🚧 **The ceiling:** When success criteria are ambiguous (”write a good email”), Reflexion has nothing to reflect on. The evaluator can’t score what it can’t define. Also hits diminishing returns fast: most improvement lands on retries 1-2. By retry 4-5, the same model generating both output and critique tends to reinforce its own blind spots.
## The Decision Flowchart
You've seen all four. Here's how to pick the right one for whatever you're building.
[![](https://substackcdn.com/image/fetch/$s_!DOpY!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff103648a-2de4-4a61-b919-aeee72feae05_1400x480.png)](https://substackcdn.com/image/fetch/$s_!DOpY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff103648a-2de4-4a61-b919-aeee72feae05_1400x480.png)
**Walking through the branches:**
**Does each step depend on the previous result?** If yes, you need a pattern that can adapt mid-execution. That rules out ReWOO, which plans the whole thing upfront.
**Do you need self-correction?** If the task has clear pass/fail criteria and getting it right matters more than speed, Reflexion gives you the retry-with-memory loop. If speed matters more than perfection, ReAct’s per-step adaptation is enough.
**Is token cost the top priority?** If yes, ReWOO gets you down to 2 LLM calls with parallel tool execution. If not, Plan-and-Execute gives you the safety of replanning when steps fail.
## The Hybrid Approach 
Most production agents don’t use a single pure pattern. The practical approach:
  * **ReAct + Reflexion** is the most common hybrid. Run a ReAct loop, and if the result fails validation, enter a Reflexion retry cycle. This gives you step-by-step adaptation for the common case and self-correction for the hard ones.
  * **Plan-and-Execute with ReAct fallback.** Plan upfront. If a step returns something unexpected and the replanner can’t handle it, drop into a ReAct loop for that specific step. LangGraph makes this easy with conditional edges.
  * **ReWOO for the fast path, Plan-and-Execute for the fallback.** Try ReWOO first. If any tool returns an error or empty result, replan with Plan-and-Execute. This gets you ReWOO’s speed on the 80% of tasks that are straightforward.


**When combining is NOT worth it:** If your task is simple enough for a ReAct loop to handle in 3-4 steps, adding planning or reflection overhead makes everything slower and harder to debug. Don’t architect for complexity you don’t have.
## The Honest Take
The single-agent pattern you choose matters less than two things most teams get wrong first:
  1. **Your tools.** We covered this in [Why AI Agents Keep Failing in Production](https://theaiengineer.substack.com/p/why-ai-agents-keep-failing-in-production): most agent failures are tool failures, not reasoning failures. A perfectly architected ReAct loop calling a flaky API will still fail.
  2. **Your evaluation.** If you can’t measure whether the agent succeeded, no pattern will save you. Build the eval before you pick the architecture.


To be real: the majority of agents in production today are ReAct loops. Not because ReAct is optimal, but because it’s simple, well-supported, and good enough for most use cases. I’ve watched teams spend weeks building Plan-and-Execute architectures for tasks that a 4-step ReAct loop handled fine. The other three patterns exist for specific failure modes that appear at scale: cost (ReWOO), complex planning (Plan-and-Execute), and correctness (Reflexion). If you don’t have those failure modes yet, start with ReAct and let the failures tell you when to graduate.
**Know someone about to pick their first agent pattern? Save them a week.**
[Share](https://theaiengineer.substack.com/p/the-4-single-agent-patterns?utm_source=substack&utm_medium=email&utm_content=share&action=share)
## Where to Next?
  * **Go deeper:**[Multi-Agent Patterns: Agentic RAG, CUA, A2A](https://theaiengineer.substack.com/p/multi-agent-patterns) covers what happens when one agent isn’t enough.
  * **Go simpler:**[What is an AI Agent?](https://theaiengineer.substack.com/p/what-is-an-ai-agent) for the fundamentals of the agent loop.
  * **Go adjacent:**[Agent Memory](https://theaiengineer.substack.com/p/agent-memory) explains the memory systems that Reflexion and other patterns depend on.


Be honest: are you still running a raw ReAct loop, or did you already hit the wall?
[Leave a comment](https://theaiengineer.substack.com/p/the-4-single-agent-patterns/comments)
[1](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-1)
AgixTech, [Technical Reasoning Loops: ReAct, ReWOO, and CoT Patterns in Production](https://agixtech.com/technical-reasoning-loops-react-rewoo-and-cot-patterns-in-production/) (2026). 
[2](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-2)
Yao et al., [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (2022).
[3](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-3)
AgixTech, [Technical Reasoning Loops: ReAct, ReWOO, and CoT Patterns in Production ](https://agixtech.com/technical-reasoning-loops-react-rewoo-and-cot-patterns-in-production/)(2026). 
[4](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-4)
Xu et al., [ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323) (2023). 
[5](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-5)
Shinn et al., [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (2023). 
[6](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-6)
Shinn et al., [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366), Table 2 and Section 4.1 (2023). 
[7](https://theaiengineer.substack.com/p/the-4-single-agent-patterns#footnote-anchor-7)
Ozer et al., [MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs](https://arxiv.org/html/2512.20845v1) (2025). 
* * *
#### Subscribe to The AI Engineer
By Paolo Perrone · Launched 4 months ago
Become dangerously good at AI Engineering.
Subscribe
By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).
[![Matteo Quaglio's avatar](https://substackcdn.com/image/fetch/$s_!gb8T!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa57c78d9-6d53-488e-aa85-d7eb4d2008f7_144x144.png)](https://substack.com/profile/174990981-matteo-quaglio)[![Douglas Mustapick's avatar](https://substackcdn.com/image/fetch/$s_!qG6H!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff59e06e5-65bd-4e00-b76d-5836362031a6_1448x1750.jpeg)](https://substack.com/profile/366964559-douglas-mustapick)[![Yevheniya's avatar](https://substackcdn.com/image/fetch/$s_!KHdg!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F715b902b-b84c-460e-8f37-5ffa28145416_2048x2048.png)](https://substack.com/profile/420670319-yevheniya)[![Paolo Perrone's avatar](https://substackcdn.com/image/fetch/$s_!UoTk!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b3dca43-c984-41cc-a31a-b210ec08bddb_1024x1024.jpeg)](https://substack.com/profile/12567301-paolo-perrone)[![ToxSec's avatar](https://substackcdn.com/image/fetch/$s_!J0tu!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcc231af-becb-46d7-a503-8314a6b5e870_3840x3840.png)](https://substack.com/profile/8759131-toxsec)
12 Likes
[](https://substack.com/note/p-194009974/restacks?utm_source=substack&utm_content=facepile-restacks)
12
18
Share
PreviousNext
#### Discussion about this post
CommentsRestacks
![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)
[![Pa Cu's avatar](https://substackcdn.com/image/fetch/$s_!5pia!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13659e73-17b7-477e-9afd-fcb159018ff9_144x144.png)](https://substack.com/profile/345362193-pa-cu?utm_source=comment)
[Pa Cu](https://substack.com/profile/345362193-pa-cu?utm_source=substack-feed-item)
[Apr 17](https://theaiengineer.substack.com/p/the-4-single-agent-patterns/comment/245160880 "Apr 17, 2026, 6:29 PM")
Liked by Paolo Perrone
I used what I wrote you originally and asked Gemini to make it cordial
[Like (1)](javascript:void\(0\))ReplyShare
[![ToxSec's avatar](https://substackcdn.com/image/fetch/$s_!J0tu!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcc231af-becb-46d7-a503-8314a6b5e870_3840x3840.png)](https://substack.com/profile/8759131-toxsec?utm_source=comment)
[ToxSec](https://substack.com/profile/8759131-toxsec?utm_source=substack-feed-item)
[Apr 16](https://theaiengineer.substack.com/p/the-4-single-agent-patterns/comment/244636846 "Apr 16, 2026, 6:13 PM")
Liked by Paolo Perrone
“If you can’t measure whether the agent succeeded, no pattern will save you.”
absolutely this! makes a huge difference.
[Like (1)](javascript:void\(0\))ReplyShare
[16 more comments...](https://theaiengineer.substack.com/p/the-4-single-agent-patterns/comments)
TopLatestDiscussions
[How Perplexity Built Their Search Engine](https://theaiengineer.substack.com/p/how-perplexity-built-their-search)
[The architecture behind 30 million cited answers a day.](https://theaiengineer.substack.com/p/how-perplexity-built-their-search)
Jun 12 • [Paolo Perrone](https://substack.com/@paoloap)
33
3
![](https://substackcdn.com/image/fetch/$s_!BSbv!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1eef2cb9-67f0-4b39-9c31-49bd17ae2657_965x430.png)
[What is Semantic Search?](https://theaiengineer.substack.com/p/what-is-semantic-search-f45)
[How Machines Started Understanding Meaning](https://theaiengineer.substack.com/p/what-is-semantic-search-f45)
Jun 6 • [Paolo Perrone](https://substack.com/@paoloap)
22
2
![](https://substackcdn.com/image/fetch/$s_!-D7u!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff481b053-d84f-4e91-82b1-e44470660bcc_1030x380.png)
[Why Does AI Need a GPU?](https://theaiengineer.substack.com/p/why-does-ai-need-a-gpu)
[The architectural difference that decides where AI runs.](https://theaiengineer.substack.com/p/why-does-ai-need-a-gpu)
Jun 10 • [Paolo Perrone](https://substack.com/@paoloap)
28
4
2
![](https://substackcdn.com/image/fetch/$s_!X6YN!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F185afb3e-69f2-4a1b-9eed-196c0e767d5c_1200x544.png)
See all
### Ready for more?
Subscribe
© 2026 Paolo Perrone · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)
[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)
[Substack](https://substack.com) is the home for great culture

