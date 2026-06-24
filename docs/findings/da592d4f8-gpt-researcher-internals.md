---
id: da592d4f8
topic: 13-reference-systems-case-studies
title: "GPT-Researcher's documented internals: the planner-executor-publisher loop, the 7-role LangGraph editorial team, and its self-reported deep-research cost/latency"
status: draft
---

# GPT-Researcher's documented internals: planner-executor-publisher, the 7-role editorial team, and self-reported cost/latency

This finding grounds GPT-Researcher's architecture in its **own primary sources** — the official repository README (assafelovic/gpt-researcher) [c1bb33cc6] and the maintainers' official LangGraph multi-agents documentation page [cb547d339] — rather than the docs landing page the prior finding had available. It refines, not repeats, the existing case-study finding dbc0e9395, which contrasted STORM's paper-backed pipeline against GPT-Researcher but could support "only the high-level pattern" for GPT-Researcher because its capture was a docs landing page. Here the two documented control flows (the single-agent core loop and the multi-agent editorial team), the named roles, and the project's self-reported cost/latency are stated in the projects' own words. The STORM-vs-GPT-Researcher comparison in dbc0e9395 is not re-argued.

## Provenance (read first)

Both cited sources are **primary** for GPT-Researcher: the README is from the official repo (`raw.githubusercontent.com/assafelovic/gpt-researcher/master/README.md`) [c1bb33cc6], and the multi-agents page is from the maintainers' official docs site (`docs.gptr.dev`) [cb547d339]. The cost and latency numbers below are **self-reported by the project in its own README** — they are not independently measured or third-party-verified, and are presented here strictly as the project's own claims.

## Q1 — What is GPT-Researcher's core control flow?

The README states the core idea is to use **'planner' and 'execution' agents**: "The planner generates research questions, while the execution agents gather relevant information. The publisher then aggregates all findings into a comprehensive report." [c1bb33cc6] This is the planner → executor → publisher spine.

The README enumerates the concrete steps of this single-agent core loop [c1bb33cc6]:

- Create a task-specific agent based on a research query.
- Generate questions that collectively form an objective opinion on the task.
- Use a crawler agent for gathering information for each question.
- Summarize and source-track each resource.
- Filter and aggregate summaries into a final research report.

Two mechanics worth noting because they parallel this engine's discipline: the loop generates **multiple sub-questions** to "form an objective opinion" before gathering, and it explicitly performs **summarize-and-source-track** per resource before aggregation [c1bb33cc6]. The README does not, in this section, quantify how many questions are generated or detail the filtering criteria.

## Q2 — What is the multi-agent "editorial team," and what does each role do?

Separate from the single-agent core loop, GPT-Researcher ships a **multi-agent assistant** built on LangGraph (and AG2), which the README and docs both describe as "inspired by the recent STORM paper" and showing "how a team of AI agents can work together to conduct research on a given topic, from planning to publication." [c1bb33cc6][cb547d339] An average run is documented as generating "a 5-6 page research report in multiple formats such as PDF, Docx and Markdown." [c1bb33cc6][cb547d339]

The LangGraph docs state the research team "is made up of 7 AI agents" and give each role's documented responsibility [cb547d339]:

- **Human** — "The human in the loop that oversees the process and provides feedback to the agents."
- **Chief Editor** — "Oversees the research process and manages the team. This is the 'master' agent that coordinates the other agents using Langgraph."
- **Researcher** (gpt-researcher) — "A specialized autonomous agent that conducts in depth research on a given topic." (This is the single-agent core loop of Q1 used as a sub-component.)
- **Editor** — "Responsible for planning the research outline and structure."
- **Reviewer** — "Validates the correctness of the research results given a set of criteria."
- **Revisor** — "Revises the research results based on the feedback from the reviewer." (The docs name this role both "Revisor" and, in the prose, "Reviser/Revises".)
- **Writer** — "Responsible for compiling and writing the final report."
- **Publisher** — "Responsible for publishing the final report in various formats."

The docs note the count is "7 AI agents" while also listing the Human-in-the-loop; the documented seven specialized AI roles are Chief Editor, Researcher, Editor, Reviewer, Revisor, Writer, and Publisher, with the Human as an overseeing participant [cb547d339]. Nothing beyond these one-line descriptions is documented per role on this page, so no further behavior is asserted here.

## Q3 — How does the editorial team run, and where is the parallelism?

The docs frame the process as five stages: "1. Planning stage, 2. Data collection and analysis, 3. Review and revision, 4. Writing and submission, 5. Publication." [cb547d339] The more specific step sequence (per the architecture diagram) is [cb547d339]:

- **Browser** (gpt-researcher) — "Browses the internet for initial research based on the given research task."
- **Editor** — "Plans the report outline and structure based on the initial research."
- **For each outline topic (in parallel):**
  - **Researcher** (gpt-researcher) — "Runs an in depth research on the subtopics and writes a draft."
  - **Reviewer** — "Validates the correctness of the draft given a set of criteria" and provides feedback.
  - **Revisor** — "Revises the draft until it is satisfactory based on the reviewer feedback."
- **Writer** — "Compiles and writes the final report including an introduction, conclusion and references section from the given research findings."
- **Publisher** — "Publishes the final report to multi formats such as PDF, Docx, Markdown, etc."

The load-bearing detail the prior finding lacked: the per-outline-topic research → review → revise sub-loop runs **in parallel across outline topics** [cb547d339]. The docs also state this LangGraph example "uses the OpenAI API only for optimized performance." [cb547d339]

## Q4 — What cost and latency does the project itself report, and under what model/config?

GPT-Researcher's README describes a "Deep Research" feature — "an advanced recursive research workflow" using "a tree-like exploration pattern" with "configurable depth and breadth" and "concurrent processing for faster results" [c1bb33cc6]. For that feature, the README's own bullets report:

- "⏱️ Takes ~5 minutes per deep research" [c1bb33cc6]
- "💰 Costs ~$0.4 per research (using `o3-mini` on 'high' reasoning effort)" [c1bb33cc6]

These two figures are **self-reported by the project in its README** [c1bb33cc6]. They are not independently measured, not benchmarked by a third party, and carry no stated sample size, query distribution, or methodology. The model/config qualifier is explicit and narrow: the ~$0.4 figure is tied specifically to `o3-mini` at "high" reasoning effort, and both figures apply to the Deep Research recursive workflow — not to the single-agent core loop (Q1) or the LangGraph editorial team (Q2/Q3), for which no cost or latency figure is given in either source.

## Application to this engine

- **The planner → executor → publisher spine is the open-source precedent for decompose-gather-aggregate**, and it is documented at a finer grain than the prior finding captured: explicit sub-question generation, per-resource summarize-and-source-track, then filter-and-aggregate [c1bb33cc6]. This engine's research-then-record split mirrors that ordering.
- **A review/revise gate is a first-class, named stage in the multi-agent variant** (Reviewer validates against criteria; Revisor revises until satisfactory) [cb547d339] — concrete support for placing a validation/faithfulness gate after drafting rather than trusting first-pass output, complementing dbc0e9395's "grounding is necessary but insufficient" point.
- **Parallelism is per-outline-topic, not per-source**: the editorial team fans out research+review+revise across outline topics concurrently after a single planning pass [cb547d339], a cheaper parallelization unit than per-question fan-out.
- **Treat the cost/latency figures as a vendor self-report, not a benchmark.** ~5 min and ~$0.4/run hold only for the Deep Research recursive workflow on `o3-mini` at "high" reasoning effort [c1bb33cc6]; they are not a measured cost model for the engine's own workload.
