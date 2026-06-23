---
id: dc577f3e2
topic: 01-methodology-epistemics
title: "Grade, reconcile, calibrate: how a rigorous research system rates evidence, resolves contradictions, and bounds its own confidence"
status: draft
---

# Grade, reconcile, calibrate: how a rigorous research system rates evidence, resolves contradictions, and bounds its own confidence

Three epistemic pillars sit under any defensible research system: a way to
**grade** how much trust a body of evidence earns, a way to **reconcile**
claims that conflict across sources, and a way to **calibrate** the confidence
the system reports back. The established methods for each pillar were built for
human evidence synthesis (Cochrane/PRISMA/GRADE) and for machine fact-checking
(claim extraction, contradiction retrieval). This finding maps those methods
onto each other and onto this engine's own gates, and marks where the
correspondence breaks.

## Provenance note

Load-bearing claims are anchored to authoritative primary sources: the
**PRISMA statement** site (`prisma-statement.org`) [c0d5f9ccd], **Cochrane**
methods/handbook material (`cochrane.org`) [c29d066dc] [c325692a1], and two
peer-review-track **arXiv** papers — document-level claim extraction
[c7b505a18] and Bayesian confidence calibration [c6d1362a1] [cd0f2b84b]. The
GRADE-framework mechanics are stated by a **vendor blog** (researchgold.org)
[cc2b152ec]; that source is an SEO marketing page for an evidence-synthesis
service, so its framing is attributed ("the blog describes…") and the GRADE
*system* it summarizes is the globally adopted Working Group framework, not the
vendor's invention [cc2b152ec]. The Claimify pipeline is described by a
**Microsoft Research blog** [cde4586b2] and the contradiction-retrieval survey
by an **aggregator** (emergentmind.com) [ca4fbe169]; both are attributed and
non-load-bearing for the thesis.

## Pillar 1 — Grading evidence: GRADE rates certainty; PRISMA reports the trail; Cochrane fixes the method first

GRADE is the framework for rating the *certainty* of a body of evidence, and
the researchgold blog describes it as separating the certainty of evidence from
the strength of any recommendation, rating evidence at four levels — High,
Moderate, Low, Very Low [cc2b152ec]. The blog describes evidence as starting
"high" for randomized trials and "low" for observational studies, then being
moved by five downgrade domains — risk of bias, inconsistency, indirectness,
imprecision, and publication bias — and three upgrade domains for observational
data [cc2b152ec]. Crucially, the blog notes GRADE judgments should be made by at
least two reviewers with an explicit documented rationale for each
downgrade/upgrade decision [cc2b152ec] — i.e., the grade is auditable, not a
bare score.

PRISMA plays a different role: it is a **reporting** guideline, designed to
improve how a systematic review is reported — completely documenting why the
review was done, what methods were used, and what was found [c0d5f9ccd]. This
methods-versus-reporting split matters: PRISMA does not tell you how to grade
evidence, it tells you to disclose the grading you did. Cochrane sits upstream
of both, maintaining the Handbook for Systematic Reviews of Interventions and
the MECIR methodological expectations as the authoritative method layer
[c29d066dc] [c325692a1].

The transferable principle across all three: **trust is earned through a
pre-specified, transparent, auditable process, not asserted.** GRADE forces an
explicit reason for every certainty change [cc2b152ec]; PRISMA forces the trail
to be reported [c0d5f9ccd]; Cochrane forces the method to be fixed before the
evidence is seen [c29d066dc].

## Pillar 2 — Reconciling claims: extract atomically, decontextualize, then test for contradiction

Before claims can be cross-referenced they must be isolated as discrete,
verifiable, standalone units. The arXiv document-level extraction paper frames
this as two coupled problems: selecting *salient, check-worthy* claim sentences
(recast as extractive summarization) and then **decontextualizing** them —
rewriting each sentence so it is understandable out of context [c7b505a18]. Its
case studies show decontextualization resolving a coreference ("He" → "President
Obama") and adding a scoping modifier so a claim stands alone [c7b505a18]; it
also reports the hard limit that some sentences *cannot* be decontextualized
because the needed information is absent from the source [c7b505a18]. The
Microsoft Research blog describes the same shape in Claimify's four stages —
sentence splitting with context, selection of verifiable content, disambiguation
against context, and decomposition into standalone claims — and reports that 99%
of Claimify's extracted claims are entailed by their source sentence [cde4586b2].

Once claims are atomic, conflict detection is a classification problem. The
contradiction-retrieval survey describes casting it as Natural Language
Inference / Recognizing Textual Entailment over three labels — Entailment,
Contradiction, and Unknown/Neutral — applied to pairs of claims about the same
target [ca4fbe169]. The aggregator describes this powering fact-checking
pipelines that flag emerging contradictory claims to prioritize human
verification [ca4fbe169]. The reconciliation principle: **surface conflict
mechanically (entailment/contradiction over atomic claims), then route to a
verdict**, rather than silently averaging sources.

## Pillar 3 — Calibrating confidence: the reported number must track the real hit rate

The Bayesian-calibration arXiv paper is narrower than its title suggests and
must be read precisely: it is about calibrating the **confidence scores of an
object-detection model**, using stochastic variational inference to place
distributions over calibration parameters and thereby produce not just a single
calibrated estimate but a *prediction interval* quantifying the epistemic
uncertainty of the calibration mapping itself [cd0f2b84b] [c6d1362a1]. It is not
a general prescription for research-system belief updating. The transferable
idea — and the only load-bearing one — is its core distinction: a reported
confidence should reflect observed frequency, and the model should additionally
express how uncertain *it is about its own confidence* [cd0f2b84b]. That is the
epistemic-calibration target: a 70%-confidence output should be right about 70%
of the time, and the system should know when it lacks the data to even make that
claim.

## Tension: where the human methods and the automation diverge

These methods do not compose frictionlessly. (1) **Method vs. reporting** is a
real seam — PRISMA's completeness can be satisfied without GRADE's certainty
judgment ever being rigorous, because they govern different things [c0d5f9ccd]
[cc2b152ec]. (2) **Check-worthiness is observer-relative**: the extraction paper
explicitly notes a claim worth checking to one fact-checking organization may
not be to another, so "which claims matter" is not fully automatable [c7b505a18].
(3) **GRADE was built for trials, not the open web** — its downgrade domains
(e.g., publication bias, RCT-vs-observational starting points) assume a clinical
evidence base [cc2b152ec], so a web research system inherits the *spirit*
(explicit, documented certainty downgrades) more than the literal domains. (4)
The calibration paper's machinery is domain-specific (vision detection) and does
not transfer as a turnkey method [c6d1362a1].

## Application: this engine's gates map onto these pillars — and where they fall short

This engine's own discipline is a partial, recognizable instance of all three
pillars. Its **citation-gate** (every claim carries an inline corpus citation;
dangling citations fail) is the operational core of Pillar 1's auditability and
Pillar 2's atomic-claim requirement — each assertion is bound to a source the
way GRADE binds each judgment to a documented rationale [cc2b152ec] and the way
claim extraction binds each claim to a source sentence [c7b505a18] [cde4586b2].
Its **faithfulness check** (does the cited source actually entail the claim) is
the same entailment test that claim extraction reports as its quality bar — 99%
of claims entailed by source [cde4586b2] — and that contradiction retrieval runs
as NLI [ca4fbe169]. Its **reviewer / provenance-tier rule** (reject findings
whose load-bearing claims rest on promotional sources; attribute blog claims as
non-load-bearing) is a coarse GRADE-style certainty downgrade: vendor/SEO
provenance lowers the trust a claim earns, exactly as GRADE downgrades for risk
of bias [cc2b152ec], and PRISMA-style disclosure of the source trail makes the
downgrade auditable [c0d5f9ccd].

Where it falls short: the engine has **no explicit certainty rating** attached to
each finding the way GRADE produces a High/Moderate/Low label with documented
per-domain rationale [cc2b152ec]; provenance tiering is binary-ish (primary vs.
promotional) rather than a graded, multi-domain assessment. It has **no
quantified self-calibration** — nothing checks whether its confidence tracks its
real hit rate, nor expresses uncertainty about that confidence, which is the
calibration target [cd0f2b84b]. And contradiction handling is done by a human
drafter reading sources, not by a mechanical entailment/contradiction pass over
extracted atomic claims [ca4fbe169] [c7b505a18] — so conflicts can be silently
smoothed rather than surfaced. The pillars name the upgrades: a graded
certainty label per finding, an automated contradiction sweep, and a measured
calibration loop.
