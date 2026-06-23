---
id: d2c5150e6
topic: 02-statistical-causal-inference
title: "Two Calculi for the Same Question: Pearl's do-Calculus and Rubin's Potential Outcomes as Complementary Engines for Identifying Causal Effects"
status: draft
---

## Thesis

Two formal traditions dominate modern causal inference, and they answer the same
question — *what is the effect of an intervention, recovered from data that were
not produced by that intervention?* — with different machinery. Pearl's
structural tradition encodes assumptions as a directed acyclic graph (DAG) and
manipulates an explicit intervention operator, `do(·)`, to decide whether and how
a causal effect can be written in terms of observable quantities [c3a6803c7].
Rubin's potential-outcomes tradition encodes each unit's two (or more) unrealized
worlds as counterfactual random variables and reduces causal estimation to a
missing-data problem governed by the treatment-assignment mechanism [c8d67f5ca].
The traditions are not rivals so much as two coordinate systems over one terrain:
the assumption that licenses graphical adjustment (a confounder set that blocks
all backdoor paths) is the same content as the assumption that licenses
potential-outcomes estimation (conditional unconfoundedness of the treatment
indicator). This finding traces what each framework *is*, how each *identifies*
an effect, where they *differ*, and what their shared rigor demands of an
autonomous AI research system designing its own experiments.

## What the frameworks are

**Pearl: a ladder and an operator.** Pearl organizes causal reasoning into three
levels, each requiring strictly stronger assumptions than the last: association
(seeing) answers `P(Y=y | X=x)` and is the domain of standard statistics and
machine learning; intervention (doing) answers `P(Y=y | do(X=x))`, the
distribution of `Y` when `X` is actively set; and counterfactual (imagining)
answers what `Y` would have been had `X` differed, given what was actually
observed [c3a6803c7]. The `do(·)` operator is what distinguishes intervention
from observation, and `P(Y | X=x)` may differ from `P(Y | do(X=x))` precisely
when confounders affect both `X` and `Y` [c3a6803c7]. Answering an interventional
question from observational data therefore requires causal assumptions, typically
encoded as a DAG [c3a6803c7]. DAGs are powerful because they let a researcher map
out every assumption about the data-generating process and then read off which
statistical adjustments are needed to isolate the treatment-to-outcome effect
[ce7635d71].

**Rubin: counterfactual outcomes and an assignment mechanism.** In the Rubin
causal model, each unit has potential outcomes under each treatment level, and
the causal (treatment) effect is the difference between these two potential
outcomes [c8d67f5ca]. A causal effect is well defined only when one can, at least
conceptually, manipulate the world so that either outcome could occur — hence the
slogan *no causation without manipulation*; asking for the causal effect of an
unmanipulable attribute such as a person's height on their weight is ill-posed
because there is no way, even conceptually, to set it [c8d67f5ca]. The
introduction of potential outcomes lets statisticians conduct rigorous causal
inference inside a familiar joint probability distribution, making the gap
between association and causation explicit [c9b3b6fa1]. The (population) average
treatment effect (ATE) is defined as the expectation of the unit-level treatment
effect [c9b3b6fa1]; an individual treatment effect can be any function of the
potential outcomes, but the difference is by far the most commonly used
definition [c3e20420a]. A peer-reviewed review notes that over roughly the last
50 years the potential-outcomes framework has become one of the most widely used
approaches for defining, identifying, and estimating causal effects [c3e20420a].

## How each framework identifies an effect from observational data

**The core obstacle is shared.** We can never observe both potential outcomes for
the same unit at once — the *fundamental problem of causal inference* — so causal
estimation always rests on assumptions plus statistical method [c7944da9a]. It is
impossible by definition to observe more than one treatment's effect on the same
subject over the same period [c8d67f5ca].

**Pearl identifies by blocking backdoor paths.** A set `Z` satisfies the backdoor
criterion relative to `(X, Y)` if no node in `Z` is a descendant of `X` and `Z`
blocks every path from `X` to `Y` that contains an arrow into `X` (a backdoor
path); when it does, the effect is identifiable via the adjustment formula
`P(Y=y | do(X=x)) = Σ_z P(Y=y | X=x, Z=z) P(Z=z)` [c3a6803c7]. Backdoor paths are
the non-causal routes through common causes that create spurious association;
conditioning on a valid `Z` blocks them without blocking any causal path, so the
residual within-stratum association is causal [c3a6803c7]. By properly closing
backdoors one can estimate a causal quantity from observational data [ce7635d71].
When a confounder is unmeasured and the backdoor criterion fails, the front-door
criterion can still identify the effect if a mediator `M` intercepts all directed
paths from `X` to `Y`, with no unblocked backdoor path from `X` to `M`, and all
backdoor paths from `M` to `Y` blocked by `X` [c3a6803c7]. The canonical case is
smoking → tar → cancer with an unmeasured genetic confounder of smoking and
cancer: the backdoor criterion fails, but the front-door formula recovers the
effect through tar [c3a6803c7]. More generally, the three rules of do-calculus
translate expressions containing `do(·)` into expressions over observed data
alone, letting one identify and then estimate an effect [c28d754ad]; the rules
form a complete set of operations for deciding identifiability [c3e4277ef]. A
practitioner-oriented blog presents the backdoor and front-door criteria as two
"quick-and-easy graphical tests" that complement the full do-calculus for
checking identifiability [c3e4277ef].

**Rubin identifies through the assignment mechanism.** The assignment mechanism —
the method by which units receive treatment — governs estimation of the average
causal effect, and randomization is one such mechanism [c8d67f5ca]. The key
identifying assumption is independence, also called unconfoundedness or
ignorability: the potential outcomes are independent of treatment assignment,
which holds when treatment is assigned randomly with respect to them and amounts
to there being no unobserved confounders [c7944da9a]. Formally, treatment
indicator `Z` is unconfounded (ignorable) when `(Y(1), Y(0)) ⊥ Z` in the
potential-outcome-augmented distribution [c9b3b6fa1]. Pure unconfoundedness is too
strong for observational data, where confounders generally exist, so one
conditions on covariates `X` to obtain conditional unconfoundedness (strong
ignorability), `(Y(1), Y(0)) ⊥ Z | X` [c9b3b6fa1]. Because exact conditioning on
high-dimensional `X` is sparse, estimation leans on a balancing score `b(X)`
satisfying `X ⊥ Z | b(X)`; the propensity score is the coarsest such balancing
score, and under conditional unconfoundedness, matching on the propensity score
removes confounding as well as matching on all confounders while collapsing the
problem to one dimension [c9b3b6fa1]. A second pillar is the stable unit treatment
value assumption (SUTVA): one unit's potential outcomes do not vary with the
treatments assigned to other units [c9b3b6fa1], a no-interference condition that
goes beyond mere independence [c8d67f5ca]. The review adds the practical estimand/
estimator distinction — the estimand is the target of inference, the estimator the
rule for approximating it from data [c3e20420a] — and recommends estimating the
propensity score even when the estimator does not use it, because the estimated
score helps assess the tenability of the positivity assumption [c3e20420a].

## Tension and convergence: Pearl versus Rubin

The two frameworks express *the same identifying content in different notation*.
Pearl's requirement — a covariate set `Z` that blocks every backdoor path — is the
graphical face of Rubin's conditional unconfoundedness `(Y(1), Y(0)) ⊥ Z | X`: a
backdoor-admissible adjustment set is exactly a set rendering treatment ignorable
given covariates [c3a6803c7][c9b3b6fa1]. One source author records the same
recognition from the practitioner side: Rubin's ignorability assumption
`Y_x ⊥ X | Z` long felt only intuitively connected to reading confounders off a
DAG, and Pearl's do-calculus is what makes the connection between DAGs and
ignorability explicit [c28d754ad]. Randomized assignment is where the two
collapse together: randomization makes the potential outcomes independent of
treatment [c7944da9a], which in graphical terms severs every arrow into the
treatment so that no backdoor path remains to block.

The frameworks also diverge in genuine ways. Rubin's *no causation without
manipulation* restricts well-posed causal questions to manipulable treatments
[c8d67f5ca], a discipline less syntactically enforced in the graphical tradition,
where one can draw an arrow out of any node. Pearl's tradition contributes the
front-door criterion, which recovers an effect through a mediator even when an
unmeasured confounder makes the backdoor/ignorability route unavailable
[c3a6803c7] — a maneuver with no equally natural expression in bare
potential-outcomes notation. And the two traditions partition the same workflow
differently: Pearl's identification formulas tell you *what* to estimate, not how
well it can be estimated — finite-sample efficiency, confidence intervals, and
sensitivity analysis are separate statistical tools — while the potential-outcomes
literature foregrounds exactly that estimation layer through matching, propensity
scores, inverse-probability weighting, and doubly robust estimators
[c3a6803c7][c9b3b6fa1].

A shared and load-bearing warning unites them: adjustment is not automatically
benign. Adding control variables to a regression does not by itself yield causal
estimates — conditioning on a collider introduces bias and conditioning on a
mediator blocks part of the causal effect, so what to control for must be chosen
by the causal structure, not by p-values or model fit, and "adjusting for
everything" is not a valid strategy [c3a6803c7]. In observational data the
independence/ignorability assumption is routinely violated because people
self-select into treatment on observed and unobserved characteristics, so naive
observational comparisons are almost always incapable of recovering causal effects
without an explicit identification strategy [c7944da9a].

## Boundary conditions: what neither framework manufactures

The rigor is in being honest about what cannot be done. Pearl's framework supplies
the language and calculus for answering causal questions *given a causal model*; it
does not tell you the correct DAG (that needs domain knowledge, prior experiments,
or discovery algorithms with strong assumptions of their own), it does not perform
reliable causal discovery from data alone (data cannot distinguish
Markov-equivalent DAGs), and if no valid adjustment set, front-door path, or
instrument exists, it declares the effect unidentifiable rather than fabricating a
solution [c3a6803c7]. On the Rubin side, violating SUTVA — through spillovers,
interference, or general-equilibrium effects — yields biased estimates because the
counterfactuals being compared are no longer valid, so designs must explicitly
account for interference (e.g., cluster-randomized trials, network models)
[c7944da9a]. Wikipedia's worked example makes the interference concrete: if a
treated unit's behavior changes a housemate's diet and thereby that housemate's
blood pressure, the housemate's outcome depends on both units' assignments and
SUTVA fails [c8d67f5ca].

## Application: causal rigor for an autonomous AI research system

An AI research engine that runs its own experiments and mines its own logs is
exactly the setting these frameworks discipline. Three implications follow.

First, **prefer assignment control over post-hoc adjustment.** Randomized
assignment makes potential outcomes independent of treatment [c7944da9a] and, in
graphical terms, removes every backdoor path, so where the system can randomize
(which prompt variant, which retrieval strategy, which agent a task is routed to)
it should, because randomization is the assignment mechanism that makes the
average causal effect estimable without modeling confounders [c8d67f5ca]. When the
system can only observe — comparing runs it did not assign — it must treat the
comparison as confounded by self-selection and is, by default, almost certainly
unable to recover the true effect from a naive contrast [c7944da9a].

Second, **adjust by structure, not by convenience.** When randomization is
impossible, the system must name a covariate set that blocks all backdoor paths
(equivalently, that renders treatment conditionally unconfounded) before it
trusts an adjusted estimate [c3a6803c7][c9b3b6fa1], and it must resist the
tempting default of throwing every available feature into the model:
conditioning on a collider or a mediator actively injects bias, so the
adjustment set must come from an explicit causal diagram of the pipeline, not
from feature availability or fit statistics [c3a6803c7]. Where a key confounder
is unmeasured, a front-door route through a measured mediator may still identify
the effect [c3a6803c7]; where no identification route exists, the honest output
is "unidentifiable," not a number [c3a6803c7].

Third, **state the estimand, check the assumptions, and respect interference.**
The system should separate the estimand (the causal quantity it wants) from the
estimator (the procedure it runs) [c3e20420a], and should sanity-check
identification assumptions it cannot guarantee — for instance estimating a
propensity-style score to probe whether positivity/overlap actually holds across
the populations being compared [c3e20420a], since lack of overlap (propensity
near 0 or 1) signals strata where the effect cannot be estimated efficiently
[c9b3b6fa1]. Finally, SUTVA is the assumption most likely to break silently in a
shared system: if experimental units interact — agents sharing a cache, a model,
a rate limit, or an environment — one unit's treatment can change another's
outcome, biasing every estimate, and the remedy is a design that isolates units
or explicitly models the interference (cluster-level assignment, network-aware
analysis) [c7944da9a][c8d67f5ca].
