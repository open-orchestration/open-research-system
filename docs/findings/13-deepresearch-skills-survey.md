# Deep-Research Skills & Systems Survey

Survey of 9 public deep-research skills/systems + the Claude prompting and cookbook references,
gathered to harden the Phase-2 *process*. Sources in
`docs/13-reference-systems-case-studies/sources/deepresearch-skills/`,
`docs/10-context-prompt-engineering/sources/`, `docs/12-tooling-landscape/sources/`.

## The convergent pipeline (every system agrees)

All research-specific systems collapse to the same loop. This is the reference architecture:

1. **Clarify** — turn the raw question into research parameters + follow-up questions before any search.
2. **Plan** — decompose into 3–5 sub-queries spanning *different facets/perspectives* (not volume).
3. **Search per sub-query** — fresh external sources, top 5–10 each.
4. **Extract** — pull key learnings/claims + evidence per page.
5. **Reflect → deepen** — detect gaps, generate new directions, recurse while depth budget remains.
6. **Synthesize** — outline first, then write only from the collected references, with inline citations.

The differentiator across systems is the **orchestration layer**, not the model. Same Claude/GPT/Gemini
families everywhere — discipline in retrieval, source ranking, and citation is the moat.

## Per-source signal

- **dzhng/deep-research** — cleanest spec of the loop. Two explicit dials: **breadth** (sub-queries per
  level) and **depth** (recursion levels). Each iteration carries forward accumulated *learnings* as
  context. This is the model to copy for our `gather → reflect → re-gather` control flow. **Confirms** the
  spike's "Multi-perspective sub-questioning" + "Two-stage research-then-write" requirements.
- **Weizhena/Deep-Research-skills** — two-phase (outline generation → deep investigation),
  **human-in-the-loop checkpoints at every stage**. Inspired by RhinoInsight's control-mechanisms paper
  (arXiv 2511.18743) — worth a deep-dive. Validates a *gated* pipeline over a fire-and-forget agent.
- **Alibaba-NLP/DeepResearch (Tongyi)** — 30.5B MoE (3.3B active), purpose-built for long-horizon
  information-seeking; SOTA on BrowseComp/HLE/FRAMES. Key process idea: **two inference paradigms** —
  plain **ReAct** for baseline, and an **IterResearch "Heavy" mode** = test-time scaling for the hard
  ceiling. Maps to our "cost-tiered technique selection" requirement: a cheap default path + an expensive
  path gated behind value.
- **bytedance/deer-flow (github-deep-research)** — productionized DeerFlow 2.0; Docker/sandbox deploy,
  one-line `npx skills add`. Reference for *packaging and deployment sizing*, less for novel method.
- **Orchestra-Research/AI-Research-SKILLs** — best **skill-packaging template**: `SKILL.md` (50–150 line
  quick ref: metadata, when-to-use, patterns, links) + `references/` (deep docs, real GitHub issues,
  releases, file-structure) + `scripts/` + `assets/`. Quality bar: 300KB+ docs from official sources.
- **glebis/claude-skills** — general skill collection (Zoom, Granola, etc.), *not* research-specific.
  Useful only as a packaging/CHANGELOG/auto-sync convention reference.
- **skillsllm / llmbase listings** — discovery directories; the github-deep-research entry points back to
  DeerFlow. Low independent signal.
- **github.com/topics/deepresearch** — 113 repos; Tongyi (19.5k★) is the head. Backlog of candidates for a
  future pass (jina-ai/node-DeepResearch surfaced).

## What this adds to our process (Phase-2 deltas)

- **Adopt explicit breadth/depth dials** (dzhng) as first-class run parameters, with carried-forward
  learnings between recursion levels. Already implied by the spike; now has a concrete reference impl.
- **Add human-in-the-loop gates** (Weizhena) at outline-approval and pre-write, not just at the end.
- **Two-tier inference** (Tongyi): cheap ReAct default + a gated "heavy" test-time-scaling mode for hard
  questions — concretizes the spike's cost-tiered requirement.
- **Standardize our skills on the Orchestra template** when Phase-2 work becomes reusable skills:
  thin `SKILL.md` + fat `references/`.

## Prompting & cookbook references (process hygiene)

From `claude-prompting-best-practices` — directly actionable for our agent prompts:
- Wrap mixed content in **XML tags** (`<instructions>`, `<context>`, `<example>`); nest for hierarchy.
- **3–5 structured, diverse examples** beat prose instruction for output shape.
- Give every subagent a **role**; be explicit and add quality modifiers ("go beyond the basics…").
- **Claude 4.6+: prefill on the last turn is removed** (400 error); use adaptive thinking + the effort
  parameter instead of `budget_tokens`. Affects how we'd wire any API-level orchestrator.

## Source-quality caveats

- `claude-cookbooks` and parts of `skillsllm` rendered as GitHub's JS "Uh oh" shell / nav-chrome — the
  README bodies are thin in the captured markdown. The cookbook *recipe list* (RAG, tool-use, eval) is a
  known quantity but not richly captured here; re-fetch via raw README if we need the recipe inventory.
- Listing pages (topics, skillsllm, llmbase) are discovery-only, not primary method sources.

## OpenAI Deep Research API (vendor reference)

`docs/05-ai-deep-research-systems/sources/openai-deep-research-api-guide.md`. Confirms the convergent
pipeline from the production side and adds concrete design points:

- **Three-step process, and the cheap-model split:** ChatGPT's Deep Research = (1) **Clarification** —
  an *intermediate cheap model* (gpt-4.1) gathers intent/preferences/constraints; (2) **Prompt
  rewriting** — same cheap model expands the input into a detailed prompt; (3) **Deep research** — the
  expensive agentic model runs only on the fully-formed prompt. Maps cleanly onto our "cost-tiered
  technique selection": use a cheap model for clarify+rewrite, reserve the expensive path for the run.
- **The API does *not* clarify or rewrite** — the deep-research model expects fully-formed prompts up
  front; the developer owns steps 1–2. So our orchestrator must *build* the clarify→rewrite front-end,
  it isn't free. (Reinforces Weizhena's human-in-the-loop outline gate.)
- **Required tool set is narrow and specialized:** web search, file search (vector stores), and remote
  **MCP servers that implement a `search`+`fetch` interface** for browsing; code interpreter for
  analysis. Function calling is *not* supported. Signals our retrieval layer should expose exactly that
  search/fetch shape (and our MCP, if we build one, must conform).
- **Long-horizon = background mode + webhooks:** runs take *tens of minutes*; the guide mandates async
  background execution with webhook completion rather than synchronous request/timeout. Validates the
  spike's "durable, checkpointed orchestrator" requirement at the API tier.
- **Security: prompt injection via tool results is the named threat** — malicious web pages / MCP
  `search` responses (even "0 results + instructions") can exfiltrate vector-store/CRM data. Our process
  needs an untrusted-content boundary on everything retrieved before it reaches a tool-calling step.

## Re-scan backlog

- RhinoInsight control-mechanisms paper (arXiv 2511.18743) — the theory behind Weizhena's gating.
- Tongyi **IterResearch / "Heavy" mode** mechanics — how test-time scaling is actually structured.
- DeerFlow 2.0 architecture (multi-agent graph) vs. the flat dzhng loop — settle flexible-orchestrator
  vs. fixed-parallelization, still contested from the spike.
