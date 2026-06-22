# The 2026 AI deep-research tool landscape: architectures, vendor strategies, and tool selection

status: draft
topic: 05-ai-deep-research-systems

By mid-2026 "deep research" has split into three tiers: frontier-lab agents from OpenAI,
Google, and Anthropic; battle-tested open-source agents led by GPT Researcher; and
specialized research assistants such as Perplexity, Elicit, Consensus, and NotebookLM. The
sources agree on why the category exists and broadly on how these systems are built, while
diverging sharply on vendor strategy and on which tool fits which job.

## Why deep-research agents exist

The motivation is consistent across sources: objective manual research can take weeks and
large resources [c1b024617], LLMs trained on outdated information hallucinate and become
irrelevant for current tasks [c1b024617], and current models have token limits insufficient
for generating long research reports [c1b024617]. Deep-research agents address all three by
gathering live external sources and assembling cited reports automatically.

## The common architecture

The dominant pattern is a planner–executor–publisher pipeline. GPT Researcher's planner
generates research questions, execution agents gather information from 20+ sources, and a
publisher aggregates the results into comprehensive reports with citations [cc7b02e60]. Its
internal design is a set of classes and modules that manage the research lifecycle, with a
query flowing through internal function calls and data structures [c3d184ff8]. It is
provider-agnostic — working with any LLM and supporting web, local, hybrid, and a recursive
"Deep Research" mode [cc7b02e60]. As of June 2026 it is the longest-running and most
battle-tested agent in the ecosystem (27.6k stars, Apache-2.0, v3.5.0 shipped May 28, 2026)
[cc7b02e60], and is positioned as the first open deep-research agent built for both web and
local research [c1b024617].

## Where the frontier labs diverge

Among the frontier labs the architectures converge but the *strategies* do not. A 2026
enterprise comparison covering architecture, orchestration, memory, and security frames
OpenAI as betting on vertical integration — owning the model, the developer API, and the
enterprise productivity layer — while Google bets on platform depth, spanning TPU chips to
the Workspace inbox with 200+ models and the A2A protocol [cb6ceb956]. The pace is rapid:
OpenAI's agent strategy alone spans three layers all shipped between February and April 2026
[c81d54eba], and adoption is broad — one source reports 89% of business teams now use AI
agents, the average organization runs 12, and 93% of leaders believe scaling agents in the
next year confers a competitive edge [c81d54eba]. The product surface is wide, spanning the
GPT-5.4 family with the Responses API and Agents SDK, Gemini 3.1 Pro with Vertex AI, and the
Claude Opus/Sonnet/Haiku line with Claude Code and Constitutional AI [cf862bd6d], alongside
competing multi-agent coding frameworks (Claude Code, OpenAI Codex, Google Antigravity)
[cf862bd6d].

## Choosing a tool

The specialized assistants are best understood as use-case-specific rather than
interchangeable. Perplexity suits knowledge workers and journalists who need cited,
verifiable answers from web sources, priced at $20/mo Pro and $40/user/mo enterprise
[cf841afde], and is characterized as a fast answer engine with citations, model choice, and
research modes [c2026b5cf]. Elicit is purpose-built for systematic literature workflows —
paper search, systematic reviews, extraction, and research tables [c2026b5cf]; Consensus
targets peer-reviewed paper search with evidence summaries [c2026b5cf]; and NotebookLM
grounds its answers in the user's own uploaded sources [c2026b5cf]. For teams needing a
self-hosted, provider-agnostic pipeline, the open-source GPT Researcher fills the
build-it-yourself slot [cc7b02e60]. The practical takeaway: match the tool to the evidence
type — open web (Perplexity), academic corpus (Elicit/Consensus), private documents
(NotebookLM), or custom infrastructure (GPT Researcher).
