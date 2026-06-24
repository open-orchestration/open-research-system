---
id: d740bae09
topic: 02-statistical-causal-inference
title: "Designing a Randomized Experiment That Can Detect an Effect: OEC, Power, Type I/II Error, and What Sets the Sample Size"
status: draft
---

## Thesis

Identifying a causal effect and *detecting* one are different problems. A
companion finding works out how to identify an effect — Pearl's do-calculus and
Rubin's potential outcomes give the conditions under which a causal quantity can
even be written in terms of observable data [d2c5150e6]. But once randomization
is on the table — the gold-standard assignment mechanism those frameworks
formalize — the binding question shifts from *can the effect be identified?* to
*is the experiment powerful enough to see it?* A peer-reviewed survey of
controlled web experiments answers that second question concretely: it names the
metric to optimize (the OEC), defines statistical power and the two error types
that trade off against it, and gives an explicit formula for the minimum sample
size [c2a793560]. This finding traces that experiment-design layer — choosing the
outcome, fixing the error rates, computing the sample size, and earning trust in
the randomization — and draws out what it means for an autonomous research engine
that runs its own A/B tests.

## The OEC: pick one outcome, and pick it in advance

The paper's first design decision is *what to measure*. It defines the **Overall
Evaluation Criterion (OEC)** as "a quantitative measure of the experiment's
objective," noting that statistics usually calls this the Response or Dependent
Variable and that synonyms include Outcome, Evaluation metric, Performance
metric, or Fitness Function [c2a793560]. Although an experiment may have multiple
objectives and admit a scorecard approach, the authors are emphatic that
selecting **a single metric** — possibly a weighted combination of objectives —
is "highly desired and recommended," because a single metric forces tradeoffs to
be made once across many experiments and aligns the organization behind a clear
objective [c2a793560]. They also warn that a good OEC should not be short-term
focused (e.g., clicks); it should include factors that predict long-term goals
[c2a793560].

Two constraints on the OEC are load-bearing for design validity. First, **the
choice of OEC must be made in advance** (a planned comparison); otherwise there
is an increased risk of finding apparently significant results by chance — what
the paper calls familywise Type I error — and the standard multiple-comparison
adjustments (Bonferroni, Tukey, Scheffé, Dunnett, and others) all essentially
tighten the confidence level and thereby reduce statistical power [c2a793560].
Second, the variance of the OEC directly drives how many users the experiment
needs (below), so the *choice* of metric is also a power decision: the paper
notes that lower-variability OEC components (e.g., conversion probability, bounded
0–100%) have smaller standard deviation than purchase units, which in turn have
smaller standard deviation than revenue [c2a793560].

## Effect, power, and the two error types

The paper defines the **Effect** as "the difference in OECs for the variants,
i.e. the mean of the Treatment minus the mean of the Control" [c2a793560]. (The
brief is correct that the phrase "effect size" as such does not appear; the
paper's own term is *Effect*, defined this way.) Effect magnitude is the lever on
detectability: "Larger differences are easier to detect, so great ideas will
unlikely be missed," whereas "Type II errors are more likely when the effects are
small" [c2a793560].

Around that the paper lays out the standard hypothesis-testing machinery in its
own terms. A Treatment is accepted as statistically significantly different when
the test **rejects the null hypothesis**, which is that the OECs are not different
[c2a793560]. The factors that govern the test are:

- **Confidence level** — commonly set to 95%, meaning that 5% of the time the
  experiment will incorrectly conclude there is a difference when there is none,
  a **Type I error**; all else equal, raising this level reduces power
  [c2a793560].
- **Power** — commonly desired around 80–95%, though "not directly controlled";
  if the null hypothesis is false (there is a real difference in OECs), the power
  is the probability of determining that the difference is statistically
  significant [c2a793560]. The paper defines power directly as "the probability
  of correctly rejecting the null hypothesis ... when it is false" — i.e., the
  ability to detect a difference when it indeed exists [c2a793560].
- **Type II error** — retaining the null hypothesis when it is false [c2a793560].
- **Standard error** — the smaller the Std-Err, the more powerful the test; for a
  mean of *n* independent observations, the standard error is the estimated
  standard deviation divided by the square root of *n* [c2a793560].

So the two error rates trade off against power through opposite levers: a stricter
confidence level controls Type I error but costs power (raising Type II error),
while a smaller standard error — bought with more data or a lower-variance metric
— raises power without loosening the Type I rate. The paper gives three concrete
ways to reduce the standard error and thereby raise power: increase the sample
size (usually by running the experiment longer), use OEC components with
inherently lower variability, and filter out users who were never exposed to the
variants but were still counted in the OEC (e.g., for a checkout-page change,
analyze only users who reached the page, since everyone else adds noise)
[c2a793560].

## What sets the sample size

The paper makes the sample-size requirement explicit rather than leaving it
qualitative. For a desired power of 80%, it gives a formula (its Formula 2) for
the number of users *n* in each (equal-sized) variant. Described faithfully in
words: **the required per-variant sample size is sixteen times the variance of
the OEC, divided by the square of the sensitivity** — where the sensitivity (the
paper's Δ) is "the amount of change you want to detect" [c2a793560]. (The
markitdown conversion of the PDF squashes the typeset equation; rendered cleanly
it is n = 16σ²/Δ², with σ² the OEC variance and Δ the minimum change to detect.)
The coefficient 16 is what delivers 80% power — "an 80% probability of rejecting
the null hypothesis that there is no difference between the Treatment and Control
if the true mean is different ... by Δ" — and the paper notes you can replace the
16 with 21 to raise power to 90% [c2a793560]. It also cites a more conservative
alternative (its Formula 3, after Wheeler) for 90% power, n = (4rσ/Δ)², where *r*
is the number of variants [c2a793560]. The authors stress that even a rough
estimate of the standard deviation in this formula is helpful in planning an
experiment [c2a793560].

This formula crystallizes the three design inputs that *determine* how big the
experiment must be: the **variance of the OEC** (σ², larger variance demands more
users — hence the value of a low-variance metric), the **minimum detectable
change** (Δ, in the denominator and squared, so halving the effect you insist on
catching roughly quadruples the required sample), and the **desired power** (fixed
by the coefficient — 16 for 80%, 21 for 90%) [c2a793560]. The paper's practical
checklist makes the same point procedurally: to **determine the minimum sample
size**, "Decide on the statistical power, the effect you would like to detect, and
estimate the variability of the OEC through an A/A test," then compute the minimum
sample size and hence the experiment's running time [c2a793560]. It flags the
common failure mode directly: "A common mistake is to run experiments that are
underpowered" [c2a793560]. To maximize power and minimize running time, it
recommends a 50/50 split of users across the two variants in an A/B test
[c2a793560].

## What randomization and the A/A test buy

The whole edifice rests on the assignment being genuinely random. In the simplest
controlled experiment — the A/B test — users are *randomly* exposed to Control (A)
or Treatment (B), and the paper underlines that "the key here is 'random'": users
cannot be distributed "any old which way," and no factor can influence the
assignment decision [c2a793560]. Proper randomization is also what makes the
analysis formulas valid — the paper notes its confidence-interval formulas assume
the covariance between the Treatment and Control means is zero, "which will be
true in a controlled experiment when the randomization is carried out properly"
[c2a793560]. This is the experiment-design counterpart to the identification
story in the companion finding: randomization is the assignment mechanism that
makes the average causal effect estimable without modeling confounders, the point
where Pearl's and Rubin's frameworks collapse together [d2c5150e6].

The paper's tool for *validating* both the variability estimate and the
randomization machinery is the **A/A test** (also called a Null Test): instead of
an A/B test, you exercise the experimentation system, assigning users to one of
two groups but exposing them to exactly the same experience [c2a793560]. An A/A
test serves two purposes: (i) it collects data to assess variability for power
calculations — i.e., it supplies the σ² that the sample-size formula needs — and
(ii) it tests the experimentation system itself, since the null hypothesis should
be rejected about 5% of the time when a 95% confidence level is used [c2a793560].
The paper reports A/A tests catching real defects: robots that accepted cookies
caused "much more than 5% false positives for an A/A test," a signal that the
pipeline was biased and the comparison untrustworthy [c2a793560]. The A/A test is
therefore both the front end of the design loop (estimate variance → size the
experiment) and a continuous integrity check on the randomization the entire
causal claim depends on.

## Application: experiment design for an autonomous research engine

A system that runs its own A/B tests — over prompt variants, retrieval
strategies, or routing policies — inherits this design discipline directly.
First, it must commit to **one OEC, chosen in advance**, ideally a low-variance
metric that predicts the long-term goal rather than a noisy short-term proxy,
because choosing the metric after seeing results inflates familywise Type I error
and a high-variance metric inflates the sample size it will need [c2a793560].
Second, it must **size the experiment before running it**: decide the desired
power and the minimum effect worth detecting, estimate the OEC's variance from an
A/A test, and compute the minimum per-variant sample size — the paper's formula
makes the cost legible (variance up → more data; minimum detectable change
halved → roughly four times the data; 80%→90% power → coefficient 16→21)
[c2a793560]. Skipping this step is the named common mistake of running
underpowered experiments that cannot detect the effect they were built to find
[c2a793560]. Third, it should **run a periodic A/A test** as a self-check: a
null comparison should reject at roughly the configured rate, and a higher
false-positive rate is direct evidence that the randomization or data pipeline is
biased — exactly the failure that would silently corrupt every causal estimate
the engine reports [c2a793560]. Finally, it should default to a **50/50
assignment** to maximize power per unit of running time [c2a793560]. Where the
companion finding tells the engine *whether* an effect is identifiable
[d2c5150e6], this layer tells it *how much data* a randomized experiment needs to
see that effect — and how to know the experiment is trustworthy before believing
its result.
