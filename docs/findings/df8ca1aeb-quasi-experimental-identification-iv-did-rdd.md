---
id: df8ca1aeb
topic: 02-statistical-causal-inference
title: "Quasi-experimental identification when you cannot randomize: IV/LATE, difference-in-differences, and regression discontinuity each buy a local effect with a design-specific assumption"
status: draft
---

# Quasi-experimental identification: IV/LATE, DiD, and RDD

## Thesis

When a randomized controlled trial is impossible, three quasi-experimental
designs recover a credible causal effect from observational data — but each
buys identification with a *different* assumption, and each pays for that
credibility by identifying a *local* or *sub-population* effect rather than the
full-population average treatment effect (ATE). Instrumental variables identify
the **Local Average Treatment Effect (LATE)** on compliers under
exclusion + monotonicity [c13c50bdd]; difference-in-differences identifies the
treatment effect on the treated by removing time-common shocks under a
common-trends assumption [c49a7ccc4]; regression discontinuity identifies a
**local** effect at a cutoff under continuity of the conditional expectation
functions [c213028d1]. They are the observational-identification complements to
the two formal *calculi* of causal identification — Pearl's do-calculus and
Rubin's potential outcomes [d2c5150e6]: the calculi say *when* an effect is
identifiable; these designs are the concrete strategies that satisfy those
conditions without randomization.

## Sub-question 1 — What does IV identify, and why is it "local"?

Imbens & Angrist (1994) work in the potential-outcomes / Rubin (1974)
framework, in which the individual-level causal effect Y(1) − Y(0) is never
jointly observed because only one potential outcome is realized per unit
[c13c50bdd]. Their central result is that, under their conditions, an
instrument identifies not the population ATE but the **Local Average Treatment
Effect** — the average effect *for the subpopulation whose treatment status is
moved by the instrument* (the "compliers") [c13c50bdd]. This is what makes the
estimand "local": it speaks only to units the instrument actually shifts, not
to always-takers or never-takers.

Two assumptions do the work. **Monotonicity (Condition 2):** for any two
instrument values the instrument moves participation in only one direction —
"either D_i(z) ≥ D_i(w) for all i, or D_i(z) ≤ D_i(w) for all i" — i.e. there
are no units who do the opposite of what the instrument encourages [c13c50bdd].
An **exclusion restriction** requires the instrument to affect the outcome only
through the treatment channel [c13c50bdd].

For a binary instrument Z, the paper's Theorem 1 shows LATE is recovered by
comparing the average of the outcome Y and of the treatment D at two values of
the instrument — conceptually the ratio

  LATE = [E(Y | Z=1) − E(Y | Z=0)] / [E(D | Z=1) − E(D | Z=0)]

(the Wald/grouping form of the IV estimator). **Lossiness note:** the source
is a PDF→markdown conversion whose math notation is partly garbled (potential
outcomes render as `y(1)`/`y(O)`, subscripts are mangled), so the formula above
is stated in its canonical conceptual form rather than transcribed
character-for-character from the source; the prose statement of the estimand —
comparing Y and D across two instrument values — is what is verifiable in the
source [c13c50bdd].

## Sub-question 2 — DiD's second-difference logic, and what Card–Krueger found

Difference-in-differences exploits a natural experiment: a policy that changes
in one group ("treatment") but not another ("control"). Card & Krueger (1994)
use **New Jersey's minimum wage rising from $4.25 to $5.05 on April 1, 1992**,
with **Pennsylvania** (no change) as the control, comparing fast-food
employment before and after [c49a7ccc4]. The DiD estimator is the *second*
difference: (change in NJ employment) − (change in PA employment). The first
difference within each state removes fixed level differences between states;
the second difference removes any shock common to both states over the period,
so it is unbiased only under the parallel-trends / common-trends assumption
(absent the policy, NJ and PA employment would have moved in parallel)
[c49a7ccc4].

The paper's headline empirical result is **"no indication that the rise in the
minimum wage reduced employment"** — contradicting the textbook competitive
prediction that a binding minimum wage cuts employment [c49a7ccc4]. This is
stated here as *the finding of that paper*, not as settled labor economics: the
result was and remains contested, and the load-bearing methodological point for
this finding is the second-difference identification logic, not the empirical
verdict.

## Sub-question 3 — What makes RD variation "as good as random"?

Regression discontinuity exploits a rule that assigns treatment based on
whether an observed forcing/running variable crosses a **cutoff**. In **sharp
RD**, treatment is a deterministic, discontinuous function of the running
variable — treatment = 1[X ≥ c] [c213028d1]. In **fuzzy RD** (a term Lee &
Lemieux attribute to Trochim 1984), crossing the cutoff changes the
*probability* of treatment but not from 0 to 1; the design is then identified
like IV, using the jump in treatment probability at the cutoff as the
instrument [c213028d1].

Identification rests on **continuity** of the conditional expectation functions
of the potential outcomes at the cutoff [c213028d1]. Lee & Lemieux's
interpretive contribution is that the variation in treatment near the cutoff is
**"as good as randomized"** — not by assumption, but as a *consequence* of
agents' inability to precisely control the running variable right at the
threshold [c213028d1]. Because identification holds only at the threshold, RD
identifies a **local** effect — the treatment effect for units at the cutoff —
not a population-wide ATE [c213028d1].

## Sub-question 4 — How these complement the identification calculi and the experimentation findings

These three designs are observational/quasi-experimental — they are what you
reach for *when you cannot randomize*. That distinguishes them from the
experimentation-side findings in this topic: A/B power and effect-size sizing
[d740bae09] and anytime-valid confidence sequences [d541a8e56] govern *designed*
randomized experiments, where assignment is under your control. The
quasi-experimental designs instead manufacture a credible source of as-if-random
variation from policy rules, instruments, or thresholds.

They are also distinct from, but downstream of, the two identification *calculi*
[d2c5150e6]: Pearl's do-calculus and Rubin's potential outcomes provide the
formal conditions under which a causal effect is identifiable; IV, DiD, and RDD
are concrete research designs whose assumptions (exclusion + monotonicity;
common trends; continuity at the cutoff) are the practical means of meeting
those conditions without an experiment. Imbens & Angrist's reliance on the
Rubin (1974) potential-outcomes framework [c13c50bdd] makes the linkage to
[d2c5150e6] explicit.

The unifying load-bearing thesis: each design trades full-population generality
for a credible *local* or *sub-population* effect under a design-specific
assumption — LATE on compliers via exclusion + monotonicity [c13c50bdd]; the
effect on the treated via common trends [c49a7ccc4]; a local-at-the-cutoff
effect via continuity [c213028d1].

## Gaps found

- **Estimation under selection-on-observables is not covered here.** These three
  primaries are *identification* strategies, not estimation-under-confounding
  recipes; a worked IPW / doubly-robust ATE estimation finding (ge2ff9cf2)
  remains ungrounded in this corpus.
- **No formal parallel-trends test / event-study in Card–Krueger.** The
  common-trends assumption is stated as the identifying assumption; the source
  does not provide a formal pre-trend test or event-study decomposition, so this
  finding does not claim one [c49a7ccc4].
- **Mangled math notation in the IV PDF.** Potential outcomes render as
  `y(1)`/`y(O)` and subscripts are garbled, so the Wald/LATE estimand is stated
  conceptually rather than transcribed; the byte-verifiable claims are the prose
  statements of LATE, monotonicity, the exclusion restriction, and the
  Rubin framework [c13c50bdd]. The tokens "Wald", "complier", and "defier" do
  not appear as clean concatenated tokens in the converted source, so those
  terms are used here as standard nomenclature for the concepts the paper
  defines, not quoted from it.
