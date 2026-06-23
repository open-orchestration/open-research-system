---
id: d1b3c3b4c
topic: 03-decision-frameworks
title: "Structuring contested judgments: ACH for competing findings and weighted criteria for auditable AI decision records"
status: draft
---

# Structuring contested judgments: ACH for competing findings and weighted criteria for auditable AI decision records

When an AI research engine reaches a contested judgment — two findings disagree,
or several candidate answers survive the evidence — it needs a discipline that is
auditable rather than a confident-sounding narrative. Two families of method bear
on this: Analysis of Competing Hypotheses (ACH), the structured analytic
technique from intelligence analysis, and weighted multi-criteria scoring for
recording how a choice was made. This finding separates what each method
genuinely prescribes (anchored to authoritative sources) from what is asserted
mostly in vendor material, and is candid about a corpus gap: none of the eight
sources actually documents the MADR/ADR template the topic names.

## Method — what ACH actually is, step by step

ACH is a structured analytic technique developed by Richards J. Heuer Jr. at the
CIA and formalized in *Psychology of Intelligence Analysis* (1999) [cc594055a].
Its canonical procedure, attributed by a citing reference work to Heuer's book,
runs: (1) identify *all* plausible hypotheses, preferably brainstormed by
analysts with different perspectives, rather than choosing one likely hypothesis
and marshalling evidence for it; (2) list the evidence and arguments — including
assumptions and deductions — for and against each hypothesis; (3) build a matrix
with hypotheses as columns and evidence as rows, applying evidence against each
hypothesis "in an attempt to disprove as many theories as possible" — the step
Heuer calls the most important [c03622383]. A widely used eight-step articulation
expands this into: enumerate hypotheses *before* examining evidence (so the set
is not anchored on whatever is most salient); list evidence atomically and treat
absence of an expected observable as evidence; mark each matrix cell Consistent,
Inconsistent, Not-applicable, or ambiguous; refine for diagnosticity; count
inconsistencies; examine critical assumptions; report with calibrated confidence;
and define future indicators [cc594055a].

The mechanically distinctive move is **diagnosticity**: evidence that is
consistent with *all* hypotheses has zero diagnostic value no matter how strong
it feels, while evidence consistent with exactly one hypothesis is maximally
diagnostic [cc594055a]. The selection rule follows from this — the favored
hypothesis is the one with the **fewest inconsistencies**, not the most
supporting evidence, because evidence can support many hypotheses at once whereas
a single strong disconfirmation can eliminate one outright [cc594055a]. A blog
framing aimed at a general audience describes ACH the same way — a tool for
making decisions "when information is limited, contradictory, or incomplete"
[cf07b946c] — but the load-bearing procedural claims here rest on the
Heuer-citing reference [c03622383] and the eight-step articulation [cc594055a],
not on that promotional source.

## Method — what weighted-criteria scoring prescribes

Weighted scoring evaluates options against multiple criteria: each criterion gets
a weight reflecting its importance, each option is scored on each criterion, and
the weighted scores are aggregated (Total = Σ weightᵢ × scoreᵢ) into one number
[c3bc7a0b1]. Beyond the simple weighted sum, the multi-criteria decision-making
(MCDM) literature includes the Analytic Hierarchy Process, which structures
criteria hierarchically and derives weights from pairwise comparisons with a
consistency check, and distance-based methods such as TOPSIS that rank options by
closeness to an ideal and anti-ideal solution [c3bc7a0b1]. These descriptions
come from a vendor blog and are treated as illustrative; the load-bearing claims
about weighting are drawn from the peer-reviewed review below.

## Evidence — why disconfirmation and weight-choice are the crux

The reason ACH privileges disconfirmation is structural, not stylistic: because a
piece of evidence can be consistent with several hypotheses simultaneously, "most
supporting evidence" is not a discriminating metric, so survival-by-disconfirmation
is the more powerful analytical move than winner-by-confirmation [cc594055a].
ACH's recognized strengths are that the matrix is **auditable** and
**backtrackable** — a decision-maker can reconstruct the sequence of evidence and
rules that produced the conclusion [c03622383].

For weighted scoring, the peer-reviewed MCDM review establishes that the choice of
weighting method is itself decisive: criterion weights significantly influence
the outcome, the selection of a weighting method "directly influences the accuracy
and reliability of the decision outcomes," and different methods produce different
weights that change the *entire ranking order*, not merely the top alternative
[c510bd8a1]. Because of this, the review recommends using *multiple* weighting
methods and comparing them rather than trusting one, and classifies methods as
subjective (the decision-maker assigns weights), objective (a mathematical
algorithm derives them from the data), or combinative [c510bd8a1]. The practical
upshot for an engine: a single weighted-criteria score is not a fact about the
world; it is an artifact of a weighting choice that should be recorded and
stress-tested.

## Tension — where these methods mislead

The strongest, most authoritative caution in the corpus is about ACH itself. A
peer-reviewed critical review (Wilcox & Mandel, *Intelligence and National
Security*, 2024) examined seven articles describing six experiments testing ACH
and concluded that ACH "as a whole — has little to no overall benefit on judgment
quality, and may even harm it," even though some individual aspects might be
beneficial; the authors explicitly discourage intelligence organizations from
mandating ACH training or use [c521f3f34]. This is the load-bearing tension and
it rests on the peer-reviewed source, not on the enthusiastic secondary accounts.
A tertiary reference corroborates the gap between reputation and evidence: ACH "is
widely believed to help overcome cognitive biases, though there is a lack of
strong empirical evidence to support this belief" [c03622383].

The mechanism critiques are specific. ACH treats items of evidence as, on their
own, consistent or inconsistent with hypotheses, treats the hypothesis set as a
"flat" list, cannot represent subordinate argumentation, demands many discrete
judgments that contribute little to discerning the best hypothesis, and at
realistic scale can leave analysts disoriented [c03622383]. Its other weaknesses:
the process is time-consuming and cumbersome at scale, the matrix is a static
snapshot in time, it is sensitive to unreliable evidence, and — per
social-constructivist critics — it does not address the problematic initial
*formation* of the hypothesis set, where cultural and identity factors can
pre-screen which hypotheses are even considered, reinforcing confirmation bias in
those that survive [c03622383]. A blog summary of ACH's benefits and limitations
echoes the bias-reduction and structure claims [c7b513d7d], but those are
attributed and non-load-bearing here.

For weighted matrices the corresponding trap is false precision. The peer-reviewed
review's own finding — that different weighting methods yield different rankings
[c510bd8a1] — is itself the warning: a clean aggregate number can flip with a
defensible change of weighting method, so a decision matrix that reports only the
winning total hides the fragility of that result.

## Application — how this engine should structure and record contested judgments

A defensible design borrows ACH's *auditable structure* while heeding the evidence
that the full ritual may not improve judgment [c521f3f34][c03622383]:

- **Model competing findings as an explicit hypothesis set.** When findings
  conflict, enumerate the candidate conclusions up front and seek
  *disconfirming* evidence for each, scoring the favored conclusion by fewest
  inconsistencies rather than most support [cc594055a]. This directly counters an
  engine's tendency to confirm its first plausible answer.
- **Persist the evidence×hypothesis matrix as the audit surface.** ACH's
  durable value in the evidence is auditability and backtrackability
  [c03622383] — record which evidence discriminated between conclusions
  (high diagnosticity) and which did not [cc594055a], so a reviewer can replay
  the reasoning.
- **Treat any weighted score as provisional.** If the engine ranks options by
  weighted criteria, record the weights *and the weighting method*, and report
  sensitivity by trying more than one method, because rankings are method-dependent
  [c510bd8a1].
- **Calibrate and record confidence and tripwires.** State the conclusions *not*
  chosen and what future evidence would overturn the assessment [cc594055a], and
  attach a confidence level rather than a bare verdict.
- **Do not mandate the heavy ritual.** Given the peer-reviewed verdict that ACH as
  a whole shows little-to-no benefit and may harm judgment [c521f3f34], adopt its
  beneficial aspects (explicit hypothesis enumeration, disconfirmation-seeking,
  the auditable matrix) selectively rather than imposing the full eight-step
  procedure on every decision.

## Honest gaps

- **No MADR/ADR coverage in this corpus.** Despite file names referencing "MADR"
  and "decision records," none of the eight sources documents the MADR template,
  its fields, or ADR practice; the weighted-criteria sources [c3bc7a0b1][c510bd8a1]
  cover MCDM, not the record format. Claims about how to *format* an AI decision
  record cannot be grounded here and need a dedicated MADR source.
- **Weighted-scoring "why decisions fail" statistics** (e.g. bias frequencies) and
  AHP/TOPSIS process descriptions come from a vendor blog [c3bc7a0b1] and are not
  treated as load-bearing.
- **Whether ACH's auditability survives its lack-of-benefit verdict** — i.e. is a
  structure worth keeping for transparency even if it does not improve accuracy —
  is a design judgment this corpus frames but does not resolve [c521f3f34][c03622383].
