# Findings — Agentic Orchestration

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Anthropic's research system uses an orchestrator-worker pattern: a LeadResearcher analyzes the query, develops a strategy, and spawns 3–5 parallel subagents (each running iterative searches), then synthesizes and hands off to a dedicated CitationAgent before producing the final report — [How Anthropic Built Their Multi-Agent Research System: Architecture Lessons from Production](https://cuizhanming.com/anthropic-multi-agent-research-architecture/)
- The multi-agent design trades roughly 15x the token usage of a single chat, so it is only justified when the task delivers 15x+ value; good fits are breadth-first exploration, information exceeding a single context window, and numerous complex tools — [How Anthropic Built Their Multi-Agent Research System: Architecture Lessons from Production](https://cuizhanming.com/anthropic-multi-agent-research-architecture/)
- Parallelization is the dominant performance lever: the lead agent spins up subagents in parallel and each subagent issues 3+ tool calls in parallel, yielding up to a 90% reduction in research time for complex queries — [How Anthropic Built Their Multi-Agent Research System: Architecture Lessons from Production](https://cuizhanming.com/anthropic-multi-agent-research-architecture/)
- Delegation must be explicit: each subagent needs a concrete objective, task boundaries, an output format, and tool guidance, or subagents duplicate work or leave gaps (e.g. two subagents repeated near-identical 2025 supply-chain searches) — [How Anthropic Built a Multi-Agent Research System](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent)
- The orchestrator-workers *workflow* differs from fixed parallelization by determining subtasks dynamically at runtime; it suits tasks where you cannot predict the subtasks needed (multi-file code changes, multi-source search) — [Building Effective AI Agents \| Anthropic](https://www.anthropic.com/research/building-effective-agents)
- Agents are stateful and errors compound: minor failures cascade in long-running processes, so the system needs durable execution, retry logic, checkpoints, and the ability to resume from the failure point rather than restart — [How we built our multi-agent research system \| Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Evaluate outcomes, not paths: because multi-agent runs are non-deterministic, judge whether the system found all required information, cited sources correctly, and reached accurate conclusions — and use end-state evaluation (with discrete checkpoints) for state-mutating agents rather than turn-by-turn analysis — [How we built our multi-agent research system \| Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Anthropic's five composable patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) are cumulative — each introduces failure modes the previous lacked; prompt chaining is cheapest when chain depth is capped — [Building Effective Agents: An Engineering Reference (2026)](https://buildingeffectiveagents.com/patterns/)

## Convergent vs contested
- **Convergent:** Orchestrator-worker with parallel subagents + a separate citation pass is the de-facto architecture for breadth-first research; observability (per-subagent traces, tool logs, intermediate thinking) is essential; outcome-based evaluation beats path-based for non-deterministic agents.
- **Contested / open:** The 15x token cost is asserted from Anthropic's own production but no source independently benchmarks the value/cost ratio; the "right" number of subagents (3–5) is heuristic, not derived. Whether to prefer a flexible orchestrator vs. fixed parallelization is task-dependent and not settled.

## Implications for the system (Phase 2)
- Adopt an orchestrator (LeadResearcher) + parallel subagents + dedicated CitationAgent topology; gate the multi-agent path behind a value/cost check so cheap queries fall back to single-agent.
- Build durable execution from day one: checkpoints, resumable state, retry logic, and per-subagent trace logging — these are prerequisites, not later additions, because errors compound.
- Make subagent task specs explicit (objective, boundaries, output format, tool list) to prevent the duplicate-work failure mode.
- Define evaluation around end-state outcomes (coverage, citation correctness, accuracy) with checkpoint-level state checks, not fixed trajectories.

## Gaps found → re-scan
- No source gives concrete numbers on context-window compression / external-memory handoff mechanics for long-horizon runs beyond a high-level mention. Targeted re-scan: "agent context compaction summarize spawn fresh subagent clean context memory handoff".
- Thin on evaluator-optimizer and routing failure modes specifically for research; re-scan: "evaluator-optimizer loop research quality gate prompt".
