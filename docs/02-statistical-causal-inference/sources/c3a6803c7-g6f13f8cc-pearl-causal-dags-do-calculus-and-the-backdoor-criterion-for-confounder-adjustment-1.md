[Skip to main content](https://theorempath.com/topics/causal-inference-pearl#main-content)
[TheoremPath](https://theorempath.com/)
  * [Curriculum](https://theorempath.com/curriculum)
  * [Paths](https://theorempath.com/paths)
  * [Labs](https://theorempath.com/labs)
  * [Diagnostic](https://theorempath.com/diagnostic)
  * [Case Study](https://theorempath.com/case-study)
  * [Blog](https://theorempath.com/blog)
  * [Search](https://theorempath.com/search)


[Sign in](https://theorempath.com/sign-in)
Module
Methodology
Prerequisites
  * [L0ACommon Probability Distributions](https://theorempath.com/topics/common-probability-distributions)
  * [L0BBayesian Estimation](https://theorempath.com/topics/bayesian-estimation)
  * [L3Causal Inference Basics](https://theorempath.com/topics/causal-inference-basics)
  * [L3Double/Debiased Machine Learning](https://theorempath.com/topics/double-debiased-machine-learning)


[Home](https://theorempath.com/)/[Curriculum](https://theorempath.com/curriculum)/Causal Inference and the Ladder of Causation
Methodology
# Causal Inference and the Ladder of Causation
Pearl's three-level hierarchy: association, intervention, counterfactual. Structural causal models, do-calculus, the adjustment formula, and why prediction is not causation.
AdvancedTier 1StableCore spine~50 min
Prerequisites
[Common Probability Distributions](https://theorempath.com/topics/common-probability-distributions)[Bayesian Estimation](https://theorempath.com/topics/bayesian-estimation)[Causal Inference Basics](https://theorempath.com/topics/causal-inference-basics)[Double Debiased Machine Learning](https://theorempath.com/topics/double-debiased-machine-learning)+ 1 more
[Quiz (9)](https://theorempath.com/quiz/causal-inference-pearl)[Pulse Check](https://theorempath.com/mastery/causal-inference-pearl/pulse)[Prereq Map](https://theorempath.com/unlock/causal-inference-pearl)
## Why This Matters
A prediction model tells you P(Y∣X)P(Y \mid X)P(Y∣X): given observed features, what outcome is likely. A causal model tells you P(Y∣do(X))P(Y \mid do(X))P(Y∣do(X)): if you intervene to set XXX to a particular value, what happens to YYY. These are different quantities. Knowing that umbrellas correlate with rain does not mean distributing umbrellas will cause rain.
Pearl's framework provides the formal machinery for distinguishing association from causation. It defines three levels of causal reasoning, shows that each level requires strictly more information than the one below, and gives algorithms (do-calculus) for computing causal and counterfactual quantities from a combination of data and assumptions encoded in a directed acyclic graph (DAG).
For ML practitioners, this matters directly. Feature importance scores measure association, not causation. Attention weights show what the model looks at, not what causes the output. Confounders in training data produce spurious correlations that fail under distribution shift. Causal reasoning is the tool for understanding when a model's learned associations will generalize and when they will break.
Embedded Causal Diagram
### The key move is to block the backdoor path
The same data can support two different quantities: an observed association and a causal effect. What changes is whether the confounder still opens the path from treatment to outcome.
Observed associationThe confounder still changes treatment assignmentXWYIntervention or valid adjustmentThe confounding path is blocked or cutXWY
X
Severity
The confounder that changes both treatment assignment and outcome.
W
Treatment
The intervention or decision whose effect you want to estimate.
Y
Outcome
The result after treatment, policy, or exposure.
Observed quantity
P(Y∣W) answers: among treated units, how do outcomes differ?
If severity affects both who gets treated and how they do, this mixes the treatment effect with selection.
Causal target
P(Y∣do(W)) asks what would change if treatment were actively set.
Randomization cuts the confounder-to-treatment arrow by design. In observational work, you try to block the same path with the right adjustment set.
## The Ladder of Causation
Pearl organizes causal reasoning into three levels, each requiring strictly stronger assumptions than the previous.
Definition
**Level 1: Association (Seeing)**
**Association** answers questions of the form: given that I observe X=xX = xX=x, what is the probability of Y=yY = yY=y?
P(Y=y∣X=x)P(Y = y \mid X = x)P(Y=y∣X=x)
This is the domain of standard statistics and machine learning. It requires only observational data. Regression, classification, and density estimation all operate at this level. Association captures correlation, conditional probability, and prediction, but cannot distinguish causes from effects.
Definition
**Level 2: Intervention (Doing)**
**Intervention** answers questions of the form: if I actively set XXX to xxx (regardless of what XXX would have been), what is the probability of Y=yY = yY=y?
P(Y=y∣do(X=x))P(Y = y \mid do(X = x))P(Y=y∣do(X=x))
This is the domain of experiments and policy decisions. The do(⋅)do(\cdot)do(⋅) operator distinguishes intervention from observation. P(Y∣X=x)P(Y \mid X = x)P(Y∣X=x) may differ from P(Y∣do(X=x))P(Y \mid do(X = x))P(Y∣do(X=x)) whenever there exist confounders that affect both XXX and YYY. Answering interventional questions from observational data requires causal assumptions, typically encoded as a DAG.
Definition
**Level 3: Counterfactual (Imagining)**
**Counterfactual** answers questions of the form: given that I observed X=x′X = x'X=x′ and Y=y′Y = y'Y=y′, what would YYY have been if XXX had been xxx instead?
P(Yx=y∣X=x′,Y=y′)P(Y_x = y \mid X = x', Y = y')P(Yx​=y∣X=x′,Y=y′)
This is the domain of attribution, regret, and individual-level reasoning. Counterfactuals require the full structural causal model, not just the DAG. They condition on what actually happened and ask about what would have happened under a different intervention. This level is strictly more informative than Level 2: two SCMs can agree on all interventional distributions but disagree on counterfactuals.
The hierarchy is strict: Level 1 information cannot answer Level 2 questions (without additional assumptions), and Level 2 information cannot answer Level 3 questions (without the full SCM). Each level requires a stronger model of the data-generating process.
## Structural Causal Models
Definition
**Structural Causal Model (SCM)** M=(U,V,F,P(U))
A **structural causal model** MMM consists of:
  * UUU: a set of **exogenous (background) variables** , determined outside the model
  * V={V1,…,Vn}V = \\{V_1, \ldots, V_n\\}V={V1​,…,Vn​}: a set of **endogenous variables** , determined inside the model
  * F={f1,…,fn}F = \\{f_1, \ldots, f_n\\}F={f1​,…,fn​}: a set of **structural equations** , where each Vi=fi(pa(Vi),Ui)V_i = f_i(\text{pa}(V_i), U_i)Vi​=fi​(pa(Vi​),Ui​) expresses ViV_iVi​ as a function of its parents and an exogenous noise term UiU_iUi​
  * P(U)P(U)P(U): a probability distribution over the exogenous variables


The structural equations are **asymmetric** : Vi=fi(pa(Vi),Ui)V_i = f_i(\text{pa}(V_i), U_i)Vi​=fi​(pa(Vi​),Ui​) means the parents cause ViV_iVi​, not that ViV_iVi​ causes its parents. This asymmetry distinguishes structural equations from statistical regression equations.
Definition
**Causal DAG**
The **causal DAG** GGG associated with an SCM MMM has one node for each endogenous variable ViV_iVi​ and a directed edge from VjV_jVj​ to ViV_iVi​ whenever VjV_jVj​ appears in the structural equation for ViV_iVi​. The DAG encodes the qualitative causal structure: which variables directly cause which others. The DAG does not encode the functional forms or noise distributions.
Example
#### Drug, Recovery, and Age
Consider three variables: age (AAA), drug treatment (DDD), and recovery (RRR). Structural equations:
A=UA,D=fD(A,UD),R=fR(A,D,UR)A = U_A, \quad D = f_D(A, U_D), \quad R = f_R(A, D, U_R)A=UA​,D=fD​(A,UD​),R=fR​(A,D,UR​)
Age causally affects both treatment assignment (doctors prescribe differently for older patients) and recovery (older patients recover more slowly). The DAG has edges A→DA \to DA→D, A→RA \to RA→R, and D→RD \to RD→R. Age is a confounder for the effect of DDD on RRR.
The observational distribution P(R∣D)P(R \mid D)P(R∣D) conflates the drug's causal effect with the confounding through age. The interventional distribution P(R∣do(D))P(R \mid do(D))P(R∣do(D)) isolates the drug's causal effect by conceptually randomizing treatment, breaking the A→DA \to DA→D arrow.
## The do-Operator and Truncated Factorization
Definition
**The do-Operator**
The **do-operator** do(X=x)do(X = x)do(X=x) represents an external intervention that sets variable XXX to value xxx, overriding the structural equation for XXX. In the modified SCM MxM_xMx​, the equation for XXX is replaced by X=xX = xX=x, and all other equations remain unchanged.
The interventional distribution is defined as:
P(Y=y∣do(X=x))=PMx(Y=y)P(Y = y \mid do(X = x)) = P_{M_x}(Y = y)P(Y=y∣do(X=x))=PMx​​(Y=y)
where PMxP_{M_x}PMx​​ is the distribution induced by the modified model.
Definition
**Truncated Factorization**
In a causal DAG with variables V1,…,VnV_1, \ldots, V_nV1​,…,Vn​, the observational distribution factorizes as:
P(v1,…,vn)=∏i=1nP(vi∣pa(vi))P(v_1, \ldots, v_n) = \prod_{i=1}^n P(v_i \mid \text{pa}(v_i))P(v1​,…,vn​)=∏i=1n​P(vi​∣pa(vi​))
Under intervention do(X=x)do(X = x)do(X=x), the interventional distribution is obtained by deleting the factor for XXX and substituting X=xX = xX=x:
P(v1,…,vn∣do(X=x))=∏i:Vi≠XP(vi∣pa(vi))∣X=xP(v_1, \ldots, v_n \mid do(X = x)) = \prod_{i: V_i \neq X} P(v_i \mid \text{pa}(v_i)) \bigg|_{X=x}P(v1​,…,vn​∣do(X=x))=∏i:Vi​=X​P(vi​∣pa(vi​))​X=x​
This is the **truncated factorization formula**. It formalizes the idea that intervention breaks the causal mechanism that normally determines XXX while leaving all other mechanisms intact.
## d-Separation
Definition
**d-Separation**
In a DAG GGG, a path between nodes XXX and YYY is **blocked** by a set of nodes ZZZ if it contains:
  1. A chain A→B→CA \to B \to CA→B→C or fork A←B→CA \leftarrow B \to CA←B→C where B∈ZB \in ZB∈Z, or
  2. A collider A→B←CA \to B \leftarrow CA→B←C where B∉ZB \notin ZB∈/Z and no descendant of BBB is in ZZZ.


XXX and YYY are **d-separated** by ZZZ in GGG (written X⊥GY∣ZX \perp_G Y \mid ZX⊥G​Y∣Z) if and only if every path between XXX and YYY is blocked by ZZZ.
Under the **causal Markov property** (which follows from the SCM construction), d-separation in the DAG implies conditional independence in the distribution: X⊥GY∣Z⟹X⊥Y∣ZX \perp_G Y \mid Z \implies X \perp Y \mid ZX⊥G​Y∣Z⟹X⊥Y∣Z. The **faithfulness assumption** is the converse direction — that every conditional independence in the distribution corresponds to a d-separation in the DAG — and is a separate, stronger assumption that can fail when multiple causal effects cancel exactly.
d-Separation is the graphical criterion that determines which conditional independence relations hold in the observational distribution generated by an SCM. It is the tool for determining whether a set of covariates is sufficient to block confounding paths.
## The Backdoor Criterion
Theorem
### Backdoor Criterion and Adjustment Formula
Statement
A set of variables ZZZ satisfies the **backdoor criterion** relative to an ordered pair (X,Y)(X, Y)(X,Y) in a DAG GGG if and only if:
  1. No node in ZZZ is a descendant of XXX.
  2. ZZZ blocks every path between XXX and YYY that contains an arrow into XXX (a "backdoor path").


If ZZZ satisfies the backdoor criterion, then the causal effect of XXX on YYY is identifiable and given by the **adjustment formula** :
P(Y=y∣do(X=x))=∑zP(Y=y∣X=x,Z=z)P(Z=z)P(Y = y \mid do(X = x)) = \sum_z P(Y = y \mid X = x, Z = z) \, P(Z = z)P(Y=y∣do(X=x))=∑z​P(Y=y∣X=x,Z=z)P(Z=z)
For continuous variables, the sum becomes an integral.
Intuition
Backdoor paths are non-causal paths from XXX to YYY that flow through common causes (confounders). These paths create spurious associations between XXX and YYY in the observational data. The backdoor criterion identifies sets of variables ZZZ that, when conditioned on, block all these spurious paths without blocking any causal paths. The adjustment formula computes the interventional distribution by stratifying on ZZZ: within each stratum, the remaining association between XXX and YYY is causal.
Proof Sketch
By the truncated factorization formula:
P(y∣do(x))=∑v∖{x,y}∏i:Vi≠XP(vi∣pa(vi))∣X=xP(y \mid do(x)) = \sum_{v \setminus \\{x, y\\}} \prod_{i: V_i \neq X} P(v_i \mid \text{pa}(v_i))\bigg|_{X=x}P(y∣do(x))=∑v∖{x,y}​∏i:Vi​=X​P(vi​∣pa(vi​))​X=x​
Partition the variables into ZZZ (the adjustment set) and the rest. Condition (1) ensures that conditioning on ZZZ does not block any causal path from XXX to YYY (no descendants of XXX in ZZZ). Condition (2) ensures that conditioning on ZZZ blocks all non-causal (backdoor) paths. Under these conditions, the marginalization over the non-ZZZ variables can be factored, and the result simplifies to the adjustment formula. The key step uses d-separation: after conditioning on ZZZ, XXX is d-separated from all non-descendants that are not on a causal path, so the truncated product reduces to P(Y∣X,Z)P(Y \mid X, Z)P(Y∣X,Z) weighted by P(Z)P(Z)P(Z).
Why It Matters
The backdoor criterion provides an actionable test: given a proposed DAG, check whether a set of measured covariates blocks all backdoor paths. If yes, you can estimate the causal effect from observational data using standard regression or stratification. If no such set exists among the measured variables, the causal effect is not identifiable by backdoor adjustment (though it may still be identifiable by other methods such as the front-door criterion or instrumental variables).
Failure Mode
The backdoor criterion assumes the DAG is correct. If the true causal structure differs from the assumed DAG (a missing edge, a reversed arrow, an unmeasured confounder), the adjustment formula gives a biased estimate of the causal effect. The DAG itself is an assumption, not something that can be fully verified from data. Domain knowledge is required to specify it.
Conditioning on a descendant of XXX (violating condition 1) introduces post-treatment bias. Conditioning on a collider opens a non-causal path and introduces collider bias. Both are common errors in applied work.
[report a correction →](https://theorempath.com/contact?subject=Errata%3A%20Theorem%20backdoor-criterion%20%E2%80%94%20Backdoor%20Criterion%20and%20Adjustment%20Formula&theorem=backdoor-criterion)
## The Front-Door Criterion
Definition
**Front-Door Criterion**
A set of variables MMM satisfies the **front-door criterion** relative to (X,Y)(X, Y)(X,Y) if and only if:
  1. MMM intercepts all directed paths from XXX to YYY.
  2. There is no unblocked backdoor path from XXX to MMM.
  3. All backdoor paths from MMM to YYY are blocked by XXX.


If the front-door criterion is satisfied:
P(Y=y∣do(X=x))=∑mP(M=m∣X=x)∑x′P(Y=y∣X=x′,M=m)P(X=x′)P(Y = y \mid do(X = x)) = \sum_m P(M = m \mid X = x) \sum_{x'} P(Y = y \mid X = x', M = m) \, P(X = x')P(Y=y∣do(X=x))=∑m​P(M=m∣X=x)∑x′​P(Y=y∣X=x′,M=m)P(X=x′)
The front-door criterion is useful when there is an unmeasured confounder between XXX and YYY, but the causal effect is mediated entirely through a measurable intermediate variable MMM.
Example
#### Smoking, Tar, and Cancer
Consider the classic example: smoking (XXX) causes tar deposits (MMM), and tar causes cancer (YYY). There may be an unmeasured genetic factor (UUU) that causes both smoking tendency and cancer risk. The DAG has edges X→M→YX \to M \to YX→M→Y and U→XU \to XU→X, U→YU \to YU→Y.
The backdoor criterion fails for the pair (X,Y)(X, Y)(X,Y) because UUU is unmeasured. But the front-door criterion is satisfied by M=tarM = \text{tar}M=tar: tar intercepts all directed paths from smoking to cancer, there is no backdoor path from smoking to tar (the U→XU \to XU→X arrow is into XXX, not into MMM), and all backdoor paths from tar to cancer are blocked by XXX. The front-door formula identifies the causal effect of smoking on cancer even with the unmeasured confounder.
## Simpson's Paradox as a Causal Phenomenon
[Simpson's paradox](https://theorempath.com/topics/simpsons-paradox) occurs when a statistical trend that appears in several groups reverses when the groups are combined (or vice versa). The "paradox" is not a statistical error. It is a signal that the data involve confounding and that the correct analysis depends on the causal structure.
Example
#### Simpson's Paradox in Treatment Data
A drug appears effective overall: recovery rate is higher in the treated group (73%) than the untreated group (69%). But within each gender subgroup, the drug appears harmful: treated men recover less often than untreated men (70% vs. 80%), and treated women recover less often than untreated women (20% vs. 30%).
The resolution depends on the causal DAG. If gender is a confounder (it affects both treatment assignment and recovery), then the stratified analysis is correct and the drug is harmful. If gender is a mediator (treatment affects recovery partly through gender-related mechanisms), then the aggregated analysis is correct. Simpson's paradox shows that statistical tables alone cannot answer causal questions. You need the DAG.
## What Pearl's Framework Does NOT Do
Pearl's framework provides the language and calculus for answering causal questions given a causal model (DAG or SCM). It does not solve the following problems:
  1. **Model specification** : the framework does not tell you what the correct DAG is. That requires domain knowledge, prior experiments, or causal discovery algorithms (which have strong assumptions of their own).
  2. **Causal discovery from data alone** : while constraint-based algorithms (PC, FCI) and score-based algorithms (GES) can learn DAG structure from data under strong assumptions (faithfulness, causal sufficiency), these assumptions frequently fail in practice. Data alone cannot distinguish between Markov-equivalent DAGs.
  3. **Finite-sample estimation** : the identification formulas (adjustment, front-door) tell you what to estimate, not how well you can estimate it. Estimation efficiency, confidence intervals, and sensitivity analysis require separate statistical tools.
  4. **Unmeasured confounders** : if the causal effect is not identifiable from the observed variables (no valid adjustment set, no front-door path, no instrument), Pearl's framework tells you the problem is unsolvable with the given data. It does not manufacture a solution.


## Connections to ML
**Feature importance is not causal.** SHAP values, permutation importance, and gradient-based saliency measure how much a feature contributes to the model's prediction. They do not measure how much changing that feature in the real world would change the outcome. A model that uses "hospital ID" to predict mortality is not telling you that the hospital causes death.
**Attention weights are not explanations.** Attention weights show where the model allocates computation. They do not indicate causal relationships between input tokens and the output. Two models can have identical predictions with different attention patterns.
**Confounding in observational ML.** Models trained on observational data learn associations, including spurious ones created by confounders. A model trained to predict recidivism from criminal records inherits confounding from the criminal justice system (e.g., over-policing of certain areas creates more arrest records, not more crime). Distribution shift often breaks exactly those associations that were confounded.
**Causal fairness.** In causal-fairness analyses, a prediction is treated as fair only if it does not depend on protected attributes through prohibited causal pathways. This requires specifying the causal DAG and defining fairness as a constraint on the causal effect of the protected attribute, not merely on the statistical association.
## Common Confusions
Watch Out
#### Pearl does not claim all questions are causal
Pearl does not claim all questions are causal. His hierarchy shows that some questions require causal assumptions that no amount of data can substitute for. The point is not "use DAGs everywhere" but "know which questions your data can and cannot answer." A prediction task (Level 1) does not need causal reasoning. An intervention question (Level 2) does. Conflating the two is the error.
Watch Out
#### DAGs do not prove causation from data
A DAG is a set of causal assumptions, not a conclusion derived from data. Drawing arrows in a DAG does not make the causal claims true. The DAG must be justified by domain knowledge, prior experiments, or explicit argument. The framework's value is in making these assumptions explicit and testable (via d-separation implications), not in eliminating the need for them.
Watch Out
#### Correlation is not causation, but neither is regression
Adding control variables to a regression does not automatically yield causal estimates. If you control for a collider, you introduce bias. If you control for a mediator, you block part of the causal effect. The choice of what to control for must be guided by the causal DAG, not by statistical criteria like p-values or model fit. "Adjusting for everything" is not a valid causal strategy.
Watch Out
#### The Rubin and Pearl frameworks are not in opposition
The potential outcomes framework (Rubin) and the structural causal model framework (Pearl) address the same problems with different notation. Potential outcomes Y(x)Y(x)Y(x) correspond to counterfactual values in an SCM. The backdoor criterion gives conditions under which the Rubin-style ignorability assumption holds. The frameworks are complementary, not competing. Pearl's DAGs make assumptions visible; Rubin's potential outcomes make estimands precise.
## Exercises
ExerciseCore
Problem
Consider a DAG with three variables: X→YX \to YX→Y and Z→XZ \to XZ→X, Z→YZ \to YZ→Y (so ZZZ is a common cause of XXX and YYY). Does the empty set satisfy the backdoor criterion for the effect of XXX on YYY? Does {Z}\\{Z\\}{Z} satisfy it? Write out the adjustment formula for the case where {Z}\\{Z\\}{Z} satisfies the criterion.
Hint
Reveal Solution
ExerciseCore
Problem
In the DAG X→M→YX \to M \to YX→M→Y with X→YX \to YX→Y (direct and indirect effects), does {M}\\{M\\}{M} satisfy the backdoor criterion for the total effect of XXX on YYY? Explain why or why not.
Hint
Reveal Solution
ExerciseAdvanced
Problem
Prove that the truncated factorization formula is equivalent to the adjustment formula when the backdoor criterion is satisfied. Start from the truncated factorization for P(y∣do(x))P(y \mid do(x))P(y∣do(x)) in a DAG with variables {X,Y,Z}\\{X, Y, Z\\}{X,Y,Z} and edges Z→XZ \to XZ→X, Z→YZ \to YZ→Y, X→YX \to YX→Y.
Hint
Reveal Solution
ExerciseResearch
Problem
Consider an ML model trained to predict YYY from (X,Z)(X, Z)(X,Z) on observational data. The true causal DAG has an unmeasured confounder UUU with U→XU \to XU→X and U→YU \to YU→Y, plus the paths X→YX \to YX→Y and Z→YZ \to YZ→Y (with ZZZ unconfounded). The model achieves low prediction error on the training distribution. Under what distribution shifts will the model fail, and why? Relate your answer to the distinction between P(Y∣X)P(Y \mid X)P(Y∣X) and P(Y∣do(X))P(Y \mid do(X))P(Y∣do(X)).
Hint
Reveal Solution
## References
**Canonical:**
  * Pearl, _Causality: Models, Reasoning, and Inference_ (2nd ed., 2009), Chapters 1-4, 7
  * Pearl, Glymour, and Jewell, _Causal Inference in Statistics: A Primer_ (2016), Chapters 1-4


**Technical foundations:**
  * Pearl, "Causal Diagrams for Empirical Research," _Biometrika_ 82(4), 1995
  * Tian and Pearl, "On the Identification of Causal Effects," _UAI_ 2002


**Connections to potential outcomes:**
  * Imbens and Rubin, _Causal Inference for Statistics, Social, and Biomedical Sciences_ (2015), Chapters 1-3
  * Richardson and Robins, "Single World Intervention Graphs," _CSSS Working Paper_ 128, 2013


**ML applications:**
  * Peters, Janzing, and Scholkopf, _Elements of Causal Inference_ (2017), Chapters 1-4, 6
  * Scholkopf et al., "Toward Causal Representation Learning," _Proceedings of the IEEE_ 109(5), 2021


## Next Topics
Natural extensions from Pearl's causal framework:
  * **[Decision theory foundations](https://theorempath.com/topics/decision-theory-foundations)** : the formal framework for choosing actions under uncertainty, which causal reasoning supports


What to do next
[ Test your understanding Take the adaptive diagnostic to find your level ](https://theorempath.com/diagnostic)
Where this fits
[ Browse curriculum Layers 0A through 5 ](https://theorempath.com/curriculum)[ Find your gaps BFS prereq checklist ](https://theorempath.com/gap-finder)
Last reviewed: April 17, 2026
Canonical graph
## Required before and derived from this topic
These links come from prerequisite edges in the curriculum graph. Editorial suggestions are shown here only when the target page also cites this page as a prerequisite.
[Full prerequisite chain](https://theorempath.com/topics/causal-inference-pearl/prerequisites)[All derived topics](https://theorempath.com/topics/causal-inference-pearl/leads-to)
### Required prerequisites
4
  * [Common Probability Distributions](https://theorempath.com/topics/common-probability-distributions)layer 0A · tier 1
  * [Double/Debiased Machine Learning](https://theorempath.com/topics/double-debiased-machine-learning)layer 3 · tier 1
  * [Bayesian Estimation](https://theorempath.com/topics/bayesian-estimation)layer 0B · tier 2
  * [Causal Inference Basics](https://theorempath.com/topics/causal-inference-basics)layer 3 · tier 3


### Derived topics
2
  * [Decision Theory Foundations](https://theorempath.com/topics/decision-theory-foundations)layer 2 · tier 2
  * [Causal Inference for Policy Evaluation](https://theorempath.com/topics/causal-inference-for-policy-evaluation)layer 4 · tier 2


Graph-backed continuations
[Decision Theory Foundations](https://theorempath.com/topics/decision-theory-foundations)[Causal Inference for Policy Evaluation](https://theorempath.com/topics/causal-inference-for-policy-evaluation)
TheoremPath. Structured study for machine learning theory.
[About](https://theorempath.com/about)[Methodology](https://theorempath.com/methodology)[Evidence](https://theorempath.com/evidence)[Lean](https://theorempath.com/lean)[References](https://theorempath.com/references)[Blog](https://theorempath.com/blog)[Curriculum](https://theorempath.com/curriculum)[Papers](https://theorempath.com/papers)[Graph](https://theorempath.com/atlas)[Paths](https://theorempath.com/paths)[Diagnostic](https://theorempath.com/diagnostic)[Search](https://theorempath.com/search)[Contact](https://theorempath.com/contact)[Privacy](https://theorempath.com/privacy)[Terms](https://theorempath.com/terms)[Disclaimer](https://theorempath.com/disclaimer)

