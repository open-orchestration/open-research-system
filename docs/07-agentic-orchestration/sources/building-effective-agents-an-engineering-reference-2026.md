# Building Effective Agents: An Engineering Reference (2026)

Source: https://buildingeffectiveagents.com/patterns/

[$building.effective.agents](https://buildingeffectiveagents.com/)[Patterns](https://buildingeffectiveagents.com/patterns/)[Architecture](https://buildingeffectiveagents.com/agent-architecture/)[How to build](https://buildingeffectiveagents.com/how-to-build-an-ai-agent/)[Frameworks](https://buildingeffectiveagents.com/frameworks/)[Evaluation](https://buildingeffectiveagents.com/evaluating-an-agent/)[Failure modes](https://buildingeffectiveagents.com/failure-modes/)[Glossary](https://buildingeffectiveagents.com/glossary/)Menu
[Patterns](https://buildingeffectiveagents.com/patterns/)[Architecture](https://buildingeffectiveagents.com/agent-architecture/)[How to build](https://buildingeffectiveagents.com/how-to-build-an-ai-agent/)[Frameworks](https://buildingeffectiveagents.com/frameworks/)[Evaluation](https://buildingeffectiveagents.com/evaluating-an-agent/)[Failure modes](https://buildingeffectiveagents.com/failure-modes/)[Glossary](https://buildingeffectiveagents.com/glossary/)
[Home](https://buildingeffectiveagents.com/)/Patterns
Last verified: April 2026
· Patterns · Index
# The five patterns.
Anthropic's December 2024 paper names five composable patterns that cover most production agent designs. Each essay quotes the original definition, explains when the pattern is appropriate, names public projects that use it, and links public benchmarks where they exist.
The patterns are _composable_ : a routing pattern often feeds into a prompt chain; an orchestrator-worker often wraps an evaluator-optimizer at the worker layer; a parallelization pattern can sit inside any of the others. The patterns are also _cumulative_ : each one introduces failure modes the previous one did not have.
The naming and the five-way split are [Anthropic's](https://www.anthropic.com/research/building-effective-agents). The cited public examples and benchmark links are independent.
[ P01 Prompt chaining → A linear sequence of LLM calls where each step's output feeds the next. Reduces error by giving each call fewer degrees of freedom. WhenTasks that decompose cleanly into stages: outline then draft then revise; parse then validate then transform. Cost classCheapest of the five patterns when chain depth is capped. ](https://buildingeffectiveagents.com/patterns/prompt-chaining/)[ P02 Routing → A classifier picks one of N specialised handlers. The classifier may itself be an LLM or a deterministic rule. WhenInput classes have meaningfully different cost or quality requirements: cheap model for FAQ, reasoning model for complex query, human escalation for the boundary case. Cost classAdds a small classification call per input. Saves cost when most inputs route to a cheaper handler. ](https://buildingeffectiveagents.com/patterns/routing/)[ P03 Parallelization → Fan out to N independent calls and aggregate. Two flavours: sectioning (sub-tasks) and voting (same task, multiple attempts). WhenThe task has independent sub-parts, or higher confidence comes from multiple votes on the same prompt. Cost classLinear in N. Latency is bounded by the slowest call, not the sum. ](https://buildingeffectiveagents.com/patterns/parallelization/)[ P04 Orchestrator-worker → A central LLM plans, dispatches subtasks to worker LLMs, then merges. Powerful but expensive when the planner over-decomposes. WhenComplex tasks where the subtasks are not known until the input arrives. Cost classMost expensive of the five patterns. Worth a worker-cap and a per-task budget cap. ](https://buildingeffectiveagents.com/patterns/orchestrator-worker/)[ P05 Evaluator-optimizer → A generator proposes a candidate, an evaluator critiques it, the loop repeats until the evaluator accepts or a budget is hit. WhenQuality matters more than latency, the evaluator can articulate clear acceptance criteria, and the task is amenable to iterative refinement. Cost classVariable. Cost is dominated by the iteration count; cap iterations. ](https://buildingeffectiveagents.com/patterns/evaluator-optimizer/)
Read next
[Agent architecture→](https://buildingeffectiveagents.com/agent-architecture/)[Failure modes→](https://buildingeffectiveagents.com/failure-modes/)[Frameworks→](https://buildingeffectiveagents.com/frameworks/)[Glossary→](https://buildingeffectiveagents.com/glossary/)
building.effective.agents
An independent engineering reference for AI agent patterns, frameworks, evaluation, and failure modes. Cited primary sources only. Third-person reference voice.
[Read the methodology →](https://buildingeffectiveagents.com/methodology/)
Reference
  * [Five Patterns](https://buildingeffectiveagents.com/patterns/)
  * [Agent architecture](https://buildingeffectiveagents.com/agent-architecture/)
  * [Frameworks](https://buildingeffectiveagents.com/frameworks/)
  * [Evaluation](https://buildingeffectiveagents.com/evaluating-an-agent/)
  * [Failure modes](https://buildingeffectiveagents.com/failure-modes/)
  * [Multi-agent systems](https://buildingeffectiveagents.com/multi-agent-systems/)


Library
  * [How to build](https://buildingeffectiveagents.com/how-to-build-an-ai-agent/)
  * [Glossary](https://buildingeffectiveagents.com/glossary/)
  * [FAQ](https://buildingeffectiveagents.com/faq/)
  * [Methodology](https://buildingeffectiveagents.com/methodology/)


Sister sites
  * [whatisanaiagent.com](https://whatisanaiagent.com)
  * [digitalsignet.com](https://digitalsignet.com)


Last verified: April 2026 · Editorial discipline: [the seven rules](https://buildingeffectiveagents.com/methodology/)
Published by [Digital Signet](https://digitalsignet.com)
[Privacy](https://digitalsignet.com/legal/privacy)[Cookies](https://digitalsignet.com/legal/cookies)[Terms](https://digitalsignet.com/legal/terms)[Accessibility](https://digitalsignet.com/legal/accessibility)

