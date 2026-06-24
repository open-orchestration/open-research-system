---
id: d69d7458e
topic: 16-evaluation-benchmarks
title: "GAIA and BrowseComp: task design and reported human-vs-agent accuracy scores"
status: draft
---

# GAIA and BrowseComp: task design and reported human-vs-agent accuracy scores

This finding grounds the concrete task design and the actual reported accuracy numbers for two primary agentic/deep-research evaluation benchmarks — GAIA (Meta AI / HuggingFace) [c57655b9e] and BrowseComp (OpenAI) [cedea9fbe] — both taken from their own primary papers. It complements finding d6fad1a98, which frames the high-level evaluation regimes for a deep-research system; this finding supplies the specific question counts, difficulty structure, grading method, and per-system scores rather than restating that framing.

## GAIA — multi-step general-assistant questions

GAIA is composed of 466 carefully devised questions with their answers, of which answers to 300 are retained (not released) for a held-out test set [c57655b9e]. Questions are organized into three levels of difficulty, loosely defined by the number of steps and the number of different tools/capabilities an annotator needed to answer them [c57655b9e]:

- **Level 1** questions generally require no tools, or at most one tool but no more than 5 steps [c57655b9e].
- **Level 2** questions generally involve more steps — roughly between 5 and 10 — and combining different tools [c57655b9e].
- **Level 3** questions are for a near-perfect general assistant, requiring arbitrarily long sequences of actions, use of any number of tools, and access to the world in general [c57655b9e].

Answers are factoid, concise, and unambiguous — a question is designed to admit a single short correct answer (a number, as few words as possible, or a comma-separated list), making them easy to verify [c57655b9e]. Because there is exactly one correct answer, evaluation is done via quasi-exact-match, which is robust to token-generation randomness since only the final answer is scored [c57655b9e].

The design philosophy is an asymmetry of difficulty: GAIA targets questions that are conceptually simple (though potentially tedious) for humans yet challenging for the most advanced AIs [c57655b9e]. The headline reported result is that human respondents obtain 92% versus 15% for GPT-4 equipped with plugins [c57655b9e]. The 92% aggregate human score is the fraction of correct answers by annotators on valid questions, aggregated across all levels [c57655b9e]; the paper's per-level human-annotator scores are 93.9% (Level 1), 91.8% (Level 2), and 87.3% (Level 3) [c57655b9e]. The corresponding per-level GPT-4-with-plugins scores in the paper's results table are 30.3% (Level 1), 9.7% (Level 2), and 0% (Level 3) [c57655b9e]. The markitdown conversion garbled this table's layout, but the per-level cells and the abstract's headline 92% vs. 15% are unambiguous in the prose [c57655b9e].

## BrowseComp — hard-to-find-fact web browsing

BrowseComp ("Browsing Competition") comprises 1,266 challenging problems that require persistently navigating the internet in search of hard-to-find, entangled information [cedea9fbe]. It was collected purely by human trainers following instructions adapted from SimpleQA [cedea9fbe]. The construction method is deliberately inverted: trainers start with a fact (a "seed" — a person, event, or artifact) and create a question for which the answer is hard to find but easy to verify [cedea9fbe]. Three checks enforced difficulty: existing models at the time could not solve the question; trainers performed five simple Google searches and confirmed the answer was not surfaced; and the task had to be hard enough that another person would not easily solve it [cedea9fbe]. Following prior practice, the dataset includes a canary string for leakage detection [cedea9fbe].

Grading is simple because every reference answer is a single short string: an AI model judges whether a predicted answer is semantically equivalent to the reference answer, using the same grading prompt as Humanity's Last Exam [cedea9fbe]. Models are also asked to report a confidence score, supporting a calibration-error metric alongside accuracy [cedea9fbe].

The reported scores (paper's accuracy table, Table 3) for models evaluated on BrowseComp [cedea9fbe]:

- **GPT-4o** (no browsing): 0.6% accuracy [cedea9fbe].
- **GPT-4o with browsing**: 1.9% accuracy [cedea9fbe].
- **GPT-4.5**: 0.9% accuracy [cedea9fbe].
- **OpenAI o1** (no browsing, stronger reasoning): 9.9% accuracy [cedea9fbe].
- **OpenAI Deep Research** (agent model trained for persistent web browsing): 51.5% accuracy — "solving around half of the problems" [cedea9fbe].

Enabling browsing for GPT-4o produced only a modest gain (0.6% to 1.9%), indicating that browsing alone is insufficient without strategic reasoning, while o1's higher score suggests some answers can be surfaced through inference over internal knowledge [cedea9fbe]. For the human baseline, OpenAI asked the trainers who built the questions to also try to solve questions they had not created: of the 1,255 examples in the campaign, trainers solved 29.2% (367/1,255) and gave up after two hours on 70.8% (888/1,255); on the solvable subset, the trainer's answer matched the reference answer 86.4% of the time (317/367) [cedea9fbe]. The markitdown conversion garbled this results table's layout, but each cited cell is legible in the source text.

## Synthesis

These two benchmarks stress different competencies. GAIA stresses multi-step tool use by a general assistant — planning and completing a number of steps that combine web browsing, coding, multi-modality, and file reading — and grades a quasi-exact-match factoid answer [c57655b9e]. BrowseComp stresses persistent web browsing for a single hard-to-find fact whose answer is easy to verify once located, requiring depth and persistence rather than broad tool orchestration [cedea9fbe]. Both matter for evaluating a deep-research system: GAIA probes whether the agent can orchestrate multiple tools across a reasoning trace, while BrowseComp probes whether it can keep searching and synthesizing across many pages until it surfaces an obscure answer.

Their shared design signature is a large human-vs-model accuracy gap built in by construction: GAIA reports 92% human vs. 15% for GPT-4 with plugins [c57655b9e], and BrowseComp reports a 29.2% human-trainer solve rate against models that range from near-zero (GPT-4o, 0.6%) up to OpenAI Deep Research at 51.5% [cedea9fbe]. In GAIA the questions are easy for humans and hard for AI; in BrowseComp they are hard for both, with the strongest agent (Deep Research) being the only system to exceed the human-trainer baseline — both designs deliberately separate genuine research capability from surface pattern-matching.
