# Findings — Statistical & Causal Inference

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Frequentist statistics treats parameters as fixed unknowns and probability as long-run frequency; it evaluates the likelihood of the observed data under the null, using p-values and confidence intervals — and its strength is standardization/objectivity (no researcher prior enters the test). — [Bayesian or Frequentist: Choosing your statistical approach](https://statsig.com/perspectives/bayesian-or-frequentist-choosing-your-statistical-approach)
- The Bayesian approach instead updates a prior distribution with observed data to produce a posterior, and is "particularly valuable in situations with limited data or when prior information is available," yielding a direct probability/certainty statement about the parameter. — [Comparing Frequentist and Bayesian Approaches - Statology](https://www.statology.org/comparing-frequentist-and-bayesian-approaches/)
- P-values are widely misinterpreted — a p-value is the probability of data at least as extreme *given the null is true*, not the probability the hypothesis is true; this misuse drives overemphasis on significance instead of effect size and practical significance. — [Bayesian or Frequentist: Choosing your statistical approach](https://statsig.com/perspectives/bayesian-or-frequentist-choosing-your-statistical-approach)
- The Bayes Factor is the Bayesian analogue of the decision rule: it converts prior odds to posterior odds by weighing the evidence for two competing hypotheses, and lets pre-existing knowledge be incorporated formally into the test. — [Decision Rules in Frequentist and Bayesian Hypothesis Testing: P-Value and Bayes Factor](https://www.ssph-journal.org/journals/international-journal-of-public-health/articles/10.3389/ijph.2025.1608258/full)
- Multiple-comparison correction is a required guardrail: it reduces statistical power but controls the overall false-positive rate across many tests. — [Bayesian or Frequentist: Choosing your statistical approach](https://statsig.com/perspectives/bayesian-or-frequentist-choosing-your-statistical-approach)
- The choice of framework is contextual, not dogmatic — it depends on the research question, availability of prior information, computational resources, and organizational standards; mature practitioners advocate using whichever fits the task. — [Bayesian or Frequentist: Choosing your statistical approach](https://statsig.com/perspectives/bayesian-or-frequentist-choosing-your-statistical-approach)
- A subtle technical caution: Bayesian posterior intervals do not necessarily provide correct frequentist coverage under model misspecification, even asymptotically — i.e. "credible interval ≠ confidence interval," and conflating them is an error. — [Bayesian inferences and frequentist evaluations | Statistical Modeling](https://statmodeling.stat.columbia.edu/2026/03/07/bayesian-inferences-and-frequentist-evaluations/)

## Convergent vs contested
- **Convergent:** Both frameworks are legitimate; p-values are routinely misused; effect size and practical significance matter more than a binary "significant/not"; priors are the defining feature that makes Bayesian methods strong with sparse data and dangerous if the prior is wrong.
- **Contested / open:** Whether credible and confidence intervals can be treated interchangeably (the Columbia stats source says no, under misspecification); and whether Bayesian framing should be the default for decision-making vs. frequentist control of error rates.

## Implications for the system (Phase 2)
- When the system reports a quantitative finding, surface effect size + interval, not just a "significant" verdict, and label which framework/interpretation the number carries (e.g. "credible interval" vs "confidence interval" are not the same claim).
- Treat priors explicitly: where the system carries forward prior evidence into a synthesis, make that prior visible and challengeable, since the prior dominates conclusions under thin evidence.
- Add a multiple-comparison / multiple-hypothesis guard when the system runs many sub-queries and aggregates positive findings, to avoid manufacturing false positives from breadth.

## Gaps found → re-scan
- Sources are almost entirely Bayesian-vs-frequentist *philosophy*; they are thin on causal inference proper. **No Pearl** (DAGs, do-calculus, confounding, backdoor criterion), no potential-outcomes / counterfactuals, and no concrete statistical-power or A/B-test methodology. Deep-dive queries: "Pearl do-calculus DAG confounding backdoor criterion practical guide", "potential outcomes counterfactual causal inference", and "statistical power analysis and sample-size determination for experiments".
