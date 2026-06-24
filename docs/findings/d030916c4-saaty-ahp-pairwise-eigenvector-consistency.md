id: d030916c4
topic: 03-decision-frameworks
title: "AHP: pairwise comparisons on a 1–9 scale with a built-in consistency check, a more rigorous MCDA than flat weighted-scoring"
status: draft

# AHP: pairwise comparisons on a 1–9 scale with a built-in consistency check, a more rigorous MCDA than flat weighted-scoring

A sibling finding [d1b3c3b4c] treats flat weighted-criteria scoring (each criterion
gets a weight, each option a score, aggregate to one number) as the auditable
record of a multi-criteria choice. The Analytic Hierarchy Process (AHP) pursues
the same goal — an auditable, multi-criteria tradeoff ranking — but is a more
rigorous member of the same family: instead of asking the analyst to assert
weights directly, it *derives* them from structured pairwise comparisons and adds
a consistency check that flat weighted-scoring has no equivalent of. This finding
grounds what AHP is, in the words of its inventor.

## Sub-questions

1. What is AHP and what are its four decomposition steps?
2. What is the 1–9 fundamental scale, and how are criterion priorities obtained?
3. How does pairwise elicitation plus matrix-derived priorities differ from flat weighted-scoring?
4. What does the consistency check buy, and what is *not* grounded in this source?

## Method — what AHP is and its four steps

AHP is a theory of measurement through **pairwise comparisons** that relies on
the judgements of experts to derive **priority** scales measuring intangibles in
relative terms [cf1c73bf5]. The source is Thomas L. Saaty's own 2008 overview;
Saaty originated AHP, so this is a creator-authored primary statement of the
method's definition [cf1c73bf5].

To make a decision, AHP **decompose**s it into these steps [cf1c73bf5]:
(1) define the problem and the kind of knowledge sought; (2) structure the
decision **hierarchy** from the top (the goal), through intermediate **criteria**,
down to the **alternatives** at the bottom; (3) construct **pairwise comparison
matrices**, each element compared against those below it using the scale; and
(4) use the resulting priorities to weight the levels and **synthesize** an
overall ranking [cf1c73bf5].

## Method — the 1–9 fundamental scale and how priorities are derived

Pairwise judgements are entered on a **fundamental scale** of absolute numbers
running 1 through 9 [cf1c73bf5]. Its named anchors are: 1 = **Equal importance**
("two activities contribute equally to the objective"); 3 = **Moderate importance**
("experience and judgement slightly favour one activity over another"); 5 =
**Strong importance** (experience and judgement strongly favour one activity);
7 = **Very strong** importance; and 9 = **Extreme importance** [cf1c73bf5]. The
even values 2, 4, 6, 8 are intermediate values between the two adjacent named
judgements [cf1c73bf5].

From a completed comparison matrix, AHP produces priorities as a **derived
scale** — a set of relative weights — which can then be compared against real
data [cf1c73bf5]. A worked example in the paper yields a derived priority vector
with weights including 0.177, 0.116, 0.190, and 0.327 [cf1c73bf5].

## Method — how this differs from flat weighted-scoring

Flat weighted-criteria scoring [d1b3c3b4c] asks the analyst to state each
criterion's weight directly and then aggregates weighted scores into a single
total. AHP differs on two mechanically distinct points, both grounded here:

- **Weights are elicited, not asserted.** Rather than naming a weight per
  criterion, the analyst makes pairwise comparisons on the 1–9 fundamental scale,
  and the priorities are *derived* from the comparison matrix as a derived scale
  [cf1c73bf5]. This converts a single hard judgement ("how important is cost,
  exactly?") into many smaller relative ones ("is cost moderately or strongly
  more important than speed?").
- **The problem is structured as a hierarchy.** AHP arranges goal → criteria →
  alternatives explicitly and synthesizes priorities down the levels [cf1c73bf5],
  whereas flat weighted-scoring works from one undifferentiated list of weighted
  criteria [d1b3c3b4c].

## Evidence — the consistency check

Because the comparisons are many and human, the judgements may be inconsistent;
measuring and improving inconsistency is **a concern of the AHP** [cf1c73bf5].
The paper reports a worked example whose **consistency** ratio is **0.022**
[cf1c73bf5]. This is the capability flat weighted-scoring lacks: directly-asserted
weights carry no internal redundancy against which inconsistency could even be
measured, so there is nothing to flag. AHP's redundant pairwise structure makes
inconsistency a quantity it can report.

## Application

AHP is not a paper exercise: the overview names real deployments, including the
allocation of research-and-development funds at **Xerox** and decisions at
**Ford** [cf1c73bf5]. For this research engine, AHP is the method to reach for
when a contested multi-criteria ranking needs defensible weights *and* a check on
whether the elicited judgements hang together — a stronger guarantee than the flat
weighted matrix in [d1b3c3b4c], at the cost of more elicitation.

## Gaps found

- **Consistency mechanics are ungrounded here.** This 2008 overview reports the
  consistency ratio only as a concept and a single worked result (0.022)
  [cf1c73bf5]. It does *not* cleanly contain the Consistency Index formula
  CI = (λmax − n)/(n − 1), the Random Index (RI) table, or the conventional
  "CR < 0.10 is acceptable" threshold — those tokens do not appear in the
  extracted bytes. The CI/RI/0.10-threshold machinery remains ungrounded and
  needs Saaty's earlier methodological papers (e.g. 1977/1987/1990) to ground.
- **"Principal eigenvector" not named in this source.** The standard AHP
  derivation obtains priorities as the principal eigenvector of the comparison
  matrix, but the word "eigenvector" does not grep cleanly in this extraction;
  the source supports only that priorities are a *derived scale* from the
  comparison matrix [cf1c73bf5]. The eigenvector mechanism is left ungrounded
  here.
- **Lossy table rows.** The fundamental-scale and example tables are fragmented
  across markdown pipes in this PDF→markdown conversion. The named anchors
  (1/3/5/7/9) and the example weights quoted above were each confirmed
  whitespace-insensitively; other numeric cells in those tables were not
  transcribed and should be re-verified against the original PDF before use.
