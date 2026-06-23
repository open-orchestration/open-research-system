---
id: dbc0e9395
topic: 13-reference-systems-case-studies
title: "Primary-source case studies: STORM's research-then-write pipeline (paper-backed) and GPT-Researcher's planner-executor, with provenance tiering"
status: draft
---

# Primary-source case studies: STORM's research-then-write pipeline and GPT-Researcher's planner-executor

This finding reads two reference deep-research systems against their **primary** sources and is explicit about which architectural details are backed by the peer-reviewed paper / official repo versus a third-party summary. The corpus contains the actual NAACL 2024 paper for STORM (via ACL Anthology [c3bf6d346] and the arXiv preprint [c9c58e239]), Stanford OVAL's own STORM project page [c2713ec8f], a third-party AI-generated code-wiki of the STORM repository [cc06c6ce1], and GPT-Researcher's official documentation site [cfc0c8e73]. Provenance tiers are stated per claim because two prior findings this corpus were rejected for treating non-primary summaries as primary.

## Provenance ledger (read first)

- **c3bf6d346 — PRIMARY PAPER.** Hosted on `aclanthology.org/2024.naacl-long.347`: the peer-reviewed proceedings version of Shao, Jiang, Kanell, Xu, Khattab, Lam, "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models," NAACL 2024, ACL, DOI 10.18653/v1/2024.naacl-long.347, pages 6252–6278 [c3bf6d346]. Highest-tier evidence.
- **c9c58e239 — PRIMARY (preprint).** The arXiv listing `arxiv.org/abs/2402.14207` of the same paper [c9c58e239]. Equivalent author-stated claims to c3bf6d346.
- **c2713ec8f — OFFICIAL PROJECT PAGE (Stanford OVAL).** `storm-project.stanford.edu`; first-party but a project/marketing page that restates the paper's abstract and method, not the paper's measurement detail [c2713ec8f].
- **cc06c6ce1 — THIRD-PARTY AI CODE-WIKI (NOT primary).** `deepwiki.com/stanford-oval/storm` is an auto-generated wiki of the GitHub repo; it cites repo files (e.g. `README.md`, `knowledge_storm/lm.py`) but is itself a machine summary. Used here only for implementation/code-structure detail, always attributed as such [cc06c6ce1].
- **cfc0c8e73 — OFFICIAL DOCS (landing page only).** `docs.gptr.dev`, GPT-Researcher's own documentation site linking to `github.com/assafelovic/gpt-researcher`; the captured page is the top-level landing page, so it supports only high-level positioning, not internal architecture detail [cfc0c8e73].

## Method: what each system does

STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) targets the **pre-writing stage** of long-form, grounded article generation and decomposes the task into two stages: a pre-writing stage that researches the topic, collects references, and produces an outline; and a writing stage that generates the full article with citations from those references [c3bf6d346][c9c58e239]. The paper states the pre-writing stage is modeled by (1) discovering diverse perspectives on the given topic, (2) simulating conversations in which writers carrying different perspectives pose questions to a topic expert grounded on trusted Internet sources, and (3) curating the collected information to create an outline [c3bf6d346][c9c58e239]. Stanford OVAL's project page restates this same two-stage / multi-perspective framing in first-party prose [c2713ec8f].

At the implementation level, the third-party DeepWiki summary of the repo describes STORM as a deterministic linear 4-stage pipeline — Knowledge Curation (simulated writer/expert conversations using perspective-guided question asking), Outline Generation (organizing collected info into a hierarchy via a `StormInformationTable`), Article Generation (section-by-section writing with retrieved info), and Article Polishing (lead section, de-duplication) — with each stage completing before the next begins [cc06c6ce1]. The same summary describes a data pipeline transforming Topic → search queries → `Information` objects → `DialogueTurn` Q&A-with-citation pairs → `StormInformationTable` → `StormArticle` [cc06c6ce1]. These code-structure specifics are attributed to the AI code-wiki, not the paper.

GPT-Researcher is described by its official docs as an open-source autonomous agent for comprehensive online research, with a separate multi-agent assistant in which "a team of AI agents can work together to conduct research on a given topic, from planning to publication" [cfc0c8e73]. The captured landing page supports the planning-to-publication framing but does not, on its own, expose internal planner/executor module names; that level of detail would require the linked repo/docs subpages, which are not in this captured source.

## Evidence: which claims are measured

The paper's measurement is concentrated on the pre-writing stage. STORM is evaluated against an outline-driven retrieval-augmented baseline using **FreshWiki**, a dataset of recent high-quality Wikipedia articles the authors curated, plus outline-quality assessments and feedback from experienced Wikipedia editors [c3bf6d346][c9c58e239]. The headline result, stated in the paper's abstract: compared with the baseline, more of STORM's articles were judged organized (a **25% absolute increase**) and broad in coverage (a **10%** increase) [c3bf6d346][c9c58e239]. The Stanford project page additionally notes the authors define metrics and demonstrate "a correlation between the pre-writing quality and the final article quality," motivating the focus on pre-writing [c2713ec8f]. No comparable measured evaluation of GPT-Researcher is present in its captured source [cfc0c8e73].

## Tension and self-reported limits

The two architectures diverge on *how* they manufacture breadth. STORM's paper-backed mechanism is perspective discovery plus simulated multi-perspective expert dialogue, with curation into an outline before any writing [c3bf6d346]. GPT-Researcher's documented framing is a multi-agent planning-to-publication flow [cfc0c8e73]. The captured sources do not provide a head-to-head comparison or cost/latency numbers, so whether simulated multi-agent conversation is worth its cost versus a flatter planner-driven approach is not resolved by this corpus.

STORM is candid about residual failure modes even with grounding: the paper reports that expert feedback "helps identify new challenges for generating grounded long articles, such as **source bias transfer and over-association of unrelated facts**" [c3bf6d346][c9c58e239]. Grounding in retrieved sources reduces but does not eliminate distortion — a limitation stated by the authors themselves, not inferred.

## Application to this engine

- **Adopt the two-stage spine, paper-backed.** The strongest evidence in this corpus is for separating a research/pre-writing phase (collect references + build outline) from a writing phase that consumes only those references [c3bf6d346][c9c58e239]; this engine's research-then-record discipline mirrors that split.
- **Generate breadth by multi-perspective sub-questioning, not just more retrieval.** STORM's measured +25% organized / +10% coverage gain over a plain outline-driven RAG baseline is direct evidence that perspective diversity, not retrieval volume alone, drives organized and broad output [c3bf6d346][c9c58e239].
- **Tier models by task to control cost.** The DeepWiki summary documents STORM assigning cheaper models to conversation simulation and question generation and more powerful models to outline and article generation [cc06c6ce1]; treated as an implementation pattern (attributed, not paper-backed), this supports cost-tiered prompting in the pipeline.
- **Treat grounding as necessary but insufficient.** Because STORM still reports source-bias transfer and over-association even when grounded [c3bf6d346], a faithfulness/citation gate downstream of retrieval is warranted rather than assuming retrieval alone yields neutral, well-attributed text.
- **Keep a planner/executor decomposition available for parallel gathering.** GPT-Researcher's documented planning-to-publication multi-agent flow [cfc0c8e73] is the open-source precedent for decomposing a topic and gathering per-question, though the captured source supports only the high-level pattern.
