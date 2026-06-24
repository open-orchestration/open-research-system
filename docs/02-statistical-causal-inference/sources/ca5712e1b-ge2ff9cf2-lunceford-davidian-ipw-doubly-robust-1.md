| STATISTICS | IN MEDICINE |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
23:2937–2960
| Statist. Med. | 2004; | (DOI: 10.1002/sim.1903) |     |     |     |     |
| ------------- | ----- | ----------------------- | --- | --- | --- | --- |
Strati(cid:1)cation and weighting via the propensity score in
estimation of causal treatment e(cid:2)ects: a comparative study
|     | Jared | K. Lunceford1;∗;† | and Marie | Davidian2 |     |     |
| --- | ----- | ----------------- | --------- | --------- | --- | --- |
1Merck Research Laboratories; RY34-A316; P.O. Box 2000; Rahway; NJ 07065-0900; U.S.A.
2Department of Statistics; North Carolina State University; Box 8203; Raleigh; NC 27695; U.S.A.
SUMMARY
Estimation of treatment e(cid:2)ects with causal interpretation from observational data is complicated be-
cause exposure to treatment may be confounded with subject characteristics. The propensity score, the
probability of treatment exposure conditional on covariates, is the basis for two approaches to adjusting
for confounding: methods based on strati(cid:1)cation of observations by quantiles of estimated propensity
scores and methods based on weighting observations by the inverse of estimated propensity scores. We
review popular versions of these approaches and related methods o(cid:2)ering improved precision, describe
theoretical properties and highlight their implications for practice, and present extensive comparisons of
performance that provide guidance for practical use. Copyright ? 2004 John Wiley & Sons, Ltd.
KEY WORDS: covariatebalance;doublerobustness;inverse-probability-of-treatment-weighted-estimator;
|     | observational | data            |     |     |     |     |
| --- | ------------- | --------------- | --- | --- | --- | --- |
|     |               | 1. INTRODUCTION |     |     |     |     |
Observational data are often the basis for epidemiological and other investigations seeking to
make inference on the e(cid:2)ect of treatment exposure on a response. Randomized studies aim to
balance distributions of subject characteristics across groups, so that groups are similar except
for the treatments. However, with observational data, treatment exposure may be associated
with covariates that are also associated with potential response, and groups may be seriously
imbalanced in these factors. Consequently, unbiased treatment comparisons from observational
data require methods that adjust for such confounding of exposure to treatment with subject
characteristics, and inferences with a causal interpretation cannot be made without appropriate
adjustment.
∗Correspondence
to: Jared K. Lunceford, Merck Research Laboratories, RY34-A316, P.O. Box 2000, Rahway,
| NJ 07065-0900, | U.S.A.                    |     |     |     |     |     |
| -------------- | ------------------------- | --- | --- | --- | --- | --- |
| †E-mail:       | jared lunceford@merck.com |     |     |     |     |     |
Contract=grant sponsor: NIH; contract=grant numbers: R01-CA085848 and R37-AI031789
|           |                   |              |     | Received | September      | 2003 |
| --------- | ----------------- | ------------ | --- | -------- | -------------- | ---- |
| Copyright | ? 2004 John Wiley | & Sons, Ltd. |     |          | Accepted April | 2004 |

2938
|     |     | J. K. LUNCEFORD | AND | M. DAVIDIAN |     |
| --- | --- | --------------- | --- | ----------- | --- |
For comparing two treatments, ‘treated’ and ‘control’, say, the propensity score is the proba-
bility of exposure to treatment conditional on observed covariates [1]. Properties of the propen-
sity score that facilitate causal inferences are given by Rosenbaum and
Rubin [1] (see also References [2,3]), and applications of methods using adjustments based
on propensity scores are increasingly widespread, e.g. References [4–6]. A popular method
for estimating the (causal) di(cid:2)erence of two treatment means is that of Rosenbaum and
Rubin [7], where individuals are strati(cid:1)ed based on estimated propensity scores and the dif-
ference estimated as the average of within-stratum e(cid:2)ects. An alternative approach is to ad-
just for confounding by using estimated propensity scores to construct weights for individual
| observations | [8,9]. |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- |
In this paper, we review approaches using strati(cid:1)cation and weighting based on propensity
scores for making causal inferences from observational data and contrast their performance.
A main objective is to provide a mostly self-contained introduction to these methods and
their underpinnings, a description of their properties that highlights insights with implications
for practice, and a demonstration of relative performance that suggests guidelines for appli-
cation. In Section 2, we discuss the framework of counterfactuals or potential outcomes [10],
which formalizes the notion of ‘causal e(cid:2)ect,’ and assumptions required to justify adjustments
for confounding. We describe popular propensity-score-based approaches and describe some
additional methods that may be less familiar to practitioners that may improve upon these.
Section 3 presents theoretical properties of the estimators, and Section 4 reports on extensive
| comparative         | simulations.  |       |        |            |       |
| ------------------- | ------------- | ----- | ------ | ---------- | ----- |
|                     | 2. ESTIMATORS | BASED | ON THE | PROPENSITY | SCORE |
| 2.1. Counterfactual | framework     |       |        |            |       |
Let Z be an indicator of observed treatment exposure (Z=1 if treated, Z=0 if control) and X
be a vector of covariates measured prior to receipt of treatment (baseline) or, if measured post-
treatment, not a(cid:2)ected by either treatment. Each individual is assumed to have an associated
random vector (Y ;Y ), where Y and Y are the values of the response that would be seen
|     | 0 1 | 0   | 1   |     |     |
| --- | --- | --- | --- | --- | --- |
if, possibly contrary to the fact of what actually happened, s=he were to receive control or
treatment, respectively. Consequently, Y and Y are referred to as counterfactuals (or potential
|     |     |     | 0 1 |     |     |
| --- | --- | --- | --- | --- | --- |
outcomes) and may be viewed as inherent characteristics of the individual. The response Y
actually observed is assumed to be that would be seen under the exposure actually received,
| formalized as |     |      |           |     |     |
| ------------- | --- | ---- | --------- | --- | --- |
|               |     | Y =Y | Z +(1−Z)Y |     | (1) |
|               |     |      | 1         | 0   |     |
Thus, (Y;Z;X) are observed on each individual. It is important to distinguish between the
observed response Y and the counterfactual responses Y and Y . The latter are hypothetical
|     |     |     |     | 0 1 |     |
| --- | --- | --- | --- | --- | --- |
and may never be observed simultaneously; however, they are a convenient construct allowing
| precise statement | of questions | of interest, | as we now | describe. |     |
| ----------------- | ------------ | ------------ | --------- | --------- | --- |
The distributions of Y and Y may be thought of as representing the hypothetical distribu-
|     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- |
tions of response for the population of individuals were all individuals to receive control or
be treated, respectively, so the means of these distributions correspond to the mean response
if all individuals were to receive each treatment. Hence, a di(cid:2)erence in these means would
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2939
|                 |        | ESTIMATION | OF              | CAUSAL TREATMENT      | EFFECTS |     |     |
| --------------- | ------ | ---------- | --------------- | --------------------- | ------- | --- | --- |
| be attributable | to, or | caused     | by, the         | treatments. Formally, | then,   |     |     |
|                 |        |            | (cid:3)=(cid:1) | −(cid:1) =E(Y         | )−E(Y ) |     |     |
|                 |        |            |                 | 1 0                   | 1 0     |     |     |
is referred to as the average causal e(cid:2)ect (of the treated state relative to control). Estimation
| of (cid:3) is thus | of central | interest | in comparing | treatments. |     |     |     |
| ------------------ | ---------- | -------- | ------------ | ----------- | --- | --- | --- |
This framework makes it possible to formalize the di(cid:4)culty in estimating (cid:3), and thus mak-
ing causal statements, from observational data. The counterfactuals are never both observed
for any subject; thus, whether estimation of (cid:3) is possible relies on whether E(Y 0 ) and E(Y 1 )
may be identi(cid:1)ed from the observed data (Y;Z;X). The sample average response in the treated
group estimates E(Y |Z=1), the mean of observed responses among subjects observed to be
|Z=1)
treated, which from (1) is equal to E(Y but is di(cid:2)erent from E(Y ), the mean if
|     |     |     |     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
the entire population were treated, and similarly for control. In a randomized trial, as Z is
determined for each participant at random, it is unrelated to how s=he might potentially re-
spond, and thus (Y ;Y )(cid:1)Z, where (cid:1) denotes statistical independence. Here, using (1), we
0 1
thus have E(Y |Z=1)=E(Y |Z=1)=E(Y ), and similarly E(Y |Z=0)=E(Y ), verifying
|     |     |     | 1   | 1   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
that the sample average di(cid:2)erence is an unbiased estimator for (cid:3) with a causal interpre-
tation, as widely accepted. However, in an observational study, because treatment exposure
Z is not controlled, Z may not be independent of (Y ;Y ); indeed, the same characteris-
0 1
tics that lead an individual to be exposed to a treatment may also be associated, or ‘con-
founded,’ with his=her potential response. In this case, E(Y |Z=1)=E(Y |Z=1)(cid:1)=E(Y )
|     |           |                  |     |     |     | 1   | 1   |
| --- | --------- | ---------------- | --- | --- | --- | --- | --- |
|     | |Z=0)=E(Y | |Z=0)(cid:1)=E(Y |     |     |     |     |     |
and E(Y ), so that the di(cid:2)erence of observed sample averages
|     |     | 0   |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
is not an unbiased estimator for (cid:3). It is important to distinguish between the conditions
(Y ;Y )(cid:1)Z and Y (cid:1)Z. The former involves potential responses, which are indeed inde-
0 1
pendent of treatment assignment under randomization, while the latter involves the observed
response and is unlikely to be true under any circumstances unless treatment has no e(cid:2)ect.
)(cid:1)Z
In an observational study, although (Y 0 ;Y 1 is unlikely to hold, it may be possible
to identify subject characteristics related to both potential response and treatment exposure,
referred to as ‘confounders.’ If we believe that X contains all such confounders, then, for
X,
individuals sharing a particular value of there would be no association between the exposure
states and the values of potential responses; i.e. treatment exposure among individuals with a
X
particular is essentially at random. Formally, Y 0 , Y 1 are independent of treatment exposure
| conditional | on X, written |     |     |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- | --- | --- |
)(cid:1)Z|X
|     |     |     |     | (Y ;Y |     |     | (2) |
| --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | 0 1   |     |     |     |
Rosenbaum and Rubin [1] refer to (2) as the assumption of strongly ignorable treatment
assignment; (2) has also been called the assumption of no unmeasured confounders [9]. One
must appreciate that (2) is an assumption; willingness to assume (2) requires the analyst to
X
have con(cid:1)dence that contains all characteristics related to both treatment and response and
| that there | are no additional, |     | unmeasured | such confounders. |     |     |     |
| ---------- | ------------------ | --- | ---------- | ----------------- | --- | --- | --- |
(Y;Z;X).
The bene(cid:1)t of (2) is that E(Y 0 ) and E(Y 1 ) may be identi(cid:1)ed from The regression
relationship E(Y |Z;X) depends only on the observed data, so is identi(cid:1)able. Then the average
for Z=1 over all X satis(cid:1)es E{E(Y |Z=1;X)}=E{E(Y |Z=1;X)}=E{E(Y |X)}=E(Y ),
|     |     |     |     |     | 1   | 1   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
where the (cid:1)rst equality is from (1), the second follows from (2), and the outer expectation
is with respect to the distribution of X; similarly, E{E(Y |Z=0;X)}=E(Y ). Thus, it should
0
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2940 J. K. LUNCEFORD AND M. DAVIDIAN
be possible to make inferences on (cid:3) if (2) may be assumed to hold. Methods using the
propensity score are one way to achieve this.
2.2. The propensity score
The propensity score e(X)=P(Z=1|X), 0¡e(X)¡1, is the probability of treatment given
the observed covariates. Rosenbaum and Rubin [1] showed that X(cid:1)Z|e(X), so individuals
from either treatment group with the same propensity score are ‘balanced’ in that the dis-
tribution of X is the same regardless of exposure status. Rosenbaum and Rubin show that
if (2) holds, in addition (Y ;Y )(cid:1)Z|e(X), so that treatment exposure is unrelated to the
0 1
counterfactuals for individuals sharing the same propensity score. We now review ways these
developments may be exploited to derive estimators for (cid:3) from observed data (Y;Z;X ),
i i i
i=1;:::;n, an i.i.d. sample containing both treated and control subjects.
In practice, the propensity score is unlikely to be known, so it is routine to estimate it
from the observed data (Z;X ), i=1;:::;n, by assuming that e(X) follows a parametric
i i
model, e.g. a logistic regression model e(X;R)={1+exp(−XTR)}−1, R(p×1). Interaction
and higher-order terms may also be included. Here, R may be estimated by the maximum
likelihood (ML) estimator Rˆ solving
(cid:1)n (cid:1)n Z −e(X ;R)
(Z;X ;R)= i i @=@R{e(X ;R)}=0 (3)
(cid:2) i i e(X ;R){1−e(X ;R)} i
i=1 i=1 i i
We assume that the analyst is pro(cid:1)cient at modelling e(X;R), so that it is correctly speci(cid:1)ed,
and write e=e(X;R) and e =@=@R{e(X;R)}, with subscript i when evaluated at X .
(cid:2) i
2.3. Estimation of (cid:3) based on strati(cid:1)cation
The popular approach using strati(cid:1)cation on estimated propensity scores to estimate (cid:3) in-
volves the following steps: (i) Estimate R as in (3) and calculate estimated propensity scores
eˆ =e(X ;Rˆ) for all i; (ii) form K strata according to the sample quantiles of the eˆ, where
i i i
the jth sample quantile qˆ, j=1;:::;K, is such that the proportion of eˆ6qˆ is roughly j=K,
j i j
qˆ =0, and qˆ =1; (iii) within each stratum, calculate the di(cid:2)erence of sample means of the
0 K
Y for each treatment; and (iv) estimate (cid:3) by a weighted sum of the di(cid:2)erences of sample
i
means across strata, where weighti(cid:1)ng is by the proportion of observations falling in each stra-
tum. De(cid:1)ning Qˆ =(qˆ ;qˆ]; n = n I(eˆ ∈Qˆ ), the number of individuals in stratum j; and
(cid:1) j j−1 j j i=1 i j
n = n ZI(eˆ ∈Qˆ ) is the number of these who are treated, the estimator using a weighted
1j i=1 i i j
sum is
(cid:2) (cid:3)(cid:4) (cid:5)
(cid:1)K n (cid:1)n (cid:1)n
(cid:3)ˆ = j n−1 ZYI(eˆ ∈Qˆ )−(n −n )−1 (1−Z)YI(eˆ ∈Qˆ ) (4)
S n 1j i i i j j 1j i i i j
j=1 i=1 i=1
As the weights n =n≈K−1, they may be replaced by K−1 to yield an average across strata.
j
The rationale follows from the property (Y ;Y )(cid:1)Z|e(X) when (2) holds. Because treat-
0 1
ment exposure is essentially at random for individuals with the same propensity value, we
expect mean comparisons within this group to be unbiased. Identifying individuals sharing
exactly the same propensity value may be infeasible in practice, so strati(cid:1)cation attempts to
achieve groups where this at least holds approximately. Consequently, (cid:3)ˆ may be a biased
S
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2941
estimator of (cid:3), as some residual confounding within strata may remain. Rosenbaum and Ru-
bin [1,7] advocate the use of quantiles (K=5), a choice made in most published applications.
Intuitively, these results require that the propensity model be correctly speci(cid:1)ed. Thus, it is
often recommended [5,7] that, following (ii), the analyst examine the degree of balance for
each element of X within each stratum using standard statistical tests. Evidence that balance
has not been achieved may re(cid:5)ect an incorrect model and the need for re(cid:1)nement, followed
by a return to (i).
To reduce residual within-stratum confounding, a variation on (4) is often advocated [2,11].
Here, steps (iii) and (iv) are modi(cid:1)ed as follows: (iii) within each stratum j=1;:::;K, (cid:1)t a
regression model of the form m(j)(Z;X;Q(j)) representing the postulated regression relationship
E(Y |Z;X) within stratum j and, based on the resulting estimate Qˆ(j), estimate treatment e(cid:2)ect
in stratum j by averaging over X in j as
i
(cid:3)ˆ(j) =n−1
(cid:1)n
I(eˆ ∈Qˆ ){m(j)(1;X ;Qˆ(j))−m(j)(0;X ;Qˆ(j))} (5)
j i j i i
i=1
and (iv) estimate (cid:3) by the average or weighted sum of the
(cid:3)ˆ(j)
, e.g. using the average
(cid:3)ˆ =K−1
(cid:1)K
(cid:3)ˆ(j) (6)
SR
j=1
Ordinarily, the m(j) are taken to be the same function of Z and X for all j. E.g. for a linear
model, m(j)(Z;X;Q(j))=(cid:3)(j)+(cid:3)(j)Z +XTQ(j); here, (cid:3)ˆ(j) = (cid:3)ˆ(j) for each j.
0 Z X Z
Within-stratum regression modelling is intended to eliminate any remaining imbalances
within strata. In Section 3.2, we demonstrate that while (cid:3)ˆ does not yield a consistent esti-
S
mator for (cid:3) in general, (cid:3)ˆ is consistent as long as the models m(j) all coincide with the
SR
true, overall regression relationship E(Y |Z;X), but may be inconsistent otherwise.
2.4. Estimation of (cid:3) based on weighting
Rather than seeking unbiased estimation within strata, weighting methods attempt to obtain
an unbiased estimator for (cid:3) in a way akin to that proposed by Horvitz and Thompson [12].
Under (1), as Z(1−Z)=0, E{ZY=e(X)}=E{ZY =e(X)}, so that, assuming (2),
1
(cid:4) (cid:5) (cid:6) (cid:4) (cid:7) (cid:5)(cid:8) (cid:4) (cid:5)
(cid:7)
E
e
Z
(X
Y
)
=E E I(Z
e
=
(X
1
)
)Y 1(cid:7) (cid:7)Y
1
;X =E
e(
Y
X
1
)
E{I(Z=1)|Y
1
;X} =E(Y
1
)
where (2) implies E{I(Z=1)|Y ;X}=e(X), allowing the last equality; and we have used
1
Z=I(Z=1). Similarly, E[(1−Z)Y={1−e(X)}]=E(Y ). This suggests immediately the esti-
0
mator for (cid:3) proposed by Rosenbaum [3] and others
(cid:1)n ZY (cid:1)n (1−Z)Y
(cid:3)ˆ =n−1 i i −n−1 i i =(cid:1)ˆ −(cid:1)ˆ (7)
IPW1 eˆ 1−eˆ 1;IPW1 0;IPW1
i=1 i i=1 i
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2942
|                            |          |         |            | J. K. | LUNCEFORD |                     | AND M. DAVIDIAN |      |           |           |     |     |
| -------------------------- | -------- | ------- | ---------- | ----- | --------- | ------------------- | --------------- | ---- | --------- | --------- | --- | --- |
| E{Z=e(X)}=E{E(Z|X)=e(X)}=1 |          |         |            |       | and       | E[(1−Z)={1−e(X)}]=1 |                 |      | suggest   |           |     |     |
|                            |          | (cid:9) | (cid:10)   |       | (cid:9)   |                     | (cid:10)        |      |           |           |     |     |
|                            |          |         | −1(cid:1)n |       |           |                     | −1(cid:1)n      |      |           |           |     |     |
|                            |          |         | (cid:1)n Z | ZY    | (cid:1)n  | 1−Z                 | (1−Z)Y          |      |           |           |     |     |
|                            | (cid:3)ˆ |         | i          | i     | i −       |                     | i               | i    | i         | −(cid:1)ˆ |     |     |
|                            | IPW2     | =       |            |       |           |                     |                 |      | =(cid:1)ˆ |           |     | (8) |
|                            |          |         | eˆ         | eˆ    |           | 1−eˆ                |                 | 1−eˆ | 1;IPW2    | 0;IPW2    |     |     |
|                            |          |         | i=1 i      | i=1   | i i=1     |                     | i i=1           | i    |           |           |     |     |
The estimator for a single mean in (8) is known as a ratio estimator in the sampling literature.
As (7) and (8) involve weighting the observations in each group by the inverse of the prob-
ability of being in that group, ‘IPW’ denotes ‘inverse probability weighting,’ and (cid:3)ˆ and
IPW1
(cid:3)ˆ are popular approaches based on such weighting. However, they are special cases of a
IPW2
broader class of estimators that may be deduced by viewing the situation as a ‘missing data’
problem discussed in a landmark paper by Robins, Rotnitzky, and Zhao [13]. To appreciate
this, consider (cid:1) . Identifying (Y ;Z;X) as the ‘full data,’ Y is only observed for individuals
|     |     | 1   |     |     | 1   |     |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with Z=1 (and is ‘missing’ for those with Z=0), so that the probability of a ‘complete case’
is P(Z=1|X) if treatment is related to X. Inverse weighting in the (cid:1)rst terms of (cid:3)ˆ and
IPW1
| (cid:3)ˆ |     |     |     |     |     |     |     |     |     | −1−1) |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
allows each ‘complete case’ i to count for him=herself and (eˆ other ‘missing’
| IPW2 |     |     |     |     |     |     |     |     |     | i   |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
subjects with like characteristics X in estimating (cid:1) . From this ‘missing data’ perspective,
|     |     |     |     |     | i   |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the Robins et al. theory may be used to describe the class of all consistent, semiparametric
estimators for (cid:1) and (cid:1) and hence (cid:3); i.e. estimators that do not require the distribution of
1 0
;X)
(Y 1 ;Y 0 to be speci(cid:1)ed. The theory shows that all such estimators for (cid:3) involve ‘inverse
weighting’ of ‘complete cases’ and are consistent if the complete-case probability (i.e. the
propensity score) is correctly modeled, so should be approximately unbiased in (cid:1)nite sam-
|     |     |     |     |     |     |     | (cid:3)ˆ | (cid:3)ˆ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
ples. The class includes simple estimators such as and [for (cid:1) , the complete-case
|     |     |     |     |     |     |     | IPW1 |     | IPW2 | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
probability is P(Z=0|X)=1−P(Z=1|X)], but others are possible. We describe two alter-
| native | estimators |     | here. |     |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The theory of Robins et al. [13] identi(cid:1)es the estimator within the class having the smallest
| (large-sample) |               | variance, |        | the (locally) | semiparametric |        | e(cid:4)cient | estimator |      |       |       |     |
| -------------- | ------------- | --------- | ------ | ------------- | -------------- | ------ | ------------- | --------- | ---- | ----- | ----- | --- |
|                |               | (cid:1)n  |        |               | (X             |        | (cid:1)n      |           |      | (X    |       |     |
|                |               |           | ZY −(Z | −eˆ)m         | ;Qˆ            | )      | (1−Z)Y        |           | +(Z  | −eˆ)m | ;Qˆ ) |     |
|                | (cid:3)ˆ =n−1 |           | i i    | i             | i 1 i          | 1 −n−1 |               | i i       | i    | i 0   | i 0   | (9) |
|                | DR            |           |        |               |                |        |               |           | 1−eˆ |       |       |     |
|                |               |           |        | eˆ i          |                |        |               |           |      | i     |       |     |
|                |               | i=1       |        |               |                |        | i=1           |           |      |       |       |     |
Here m (X;Q )=E(Y |Z=z;X) is the regression of the response on X in group z, z=0;1,
|     | z   | z   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
depending on parameters Q , and Qˆ is an estimator for Q based on the data from subjects
|     |     |     |     | z   | z   |     |     | z   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with Z=z. Each term in (cid:3)ˆ has the form of those in (cid:3)ˆ and (cid:3)ˆ but ‘augmented’
|     |     |     |     | DR  |     |     |     | IPW1 |     | IPW2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
(e.g. Reference [14]) by an expression involving the regression; it is this ‘augmentation’ that
serves to increase e(cid:4)ciency. Unlike (cid:3)ˆ , (cid:3)ˆ , and (cid:3)ˆ , (cid:3)ˆ requires speci(cid:1)cation of this
|     |     |     |     |     | S   | IPW1 | IPW2 | DR  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
(cid:3)ˆ
regression model; however, because is the e(cid:4)cient estimator in the class, in large samples,
DR
it has smaller variance than (cid:3)ˆ or (cid:3)ˆ , often dramatically so. Moreover, Scharfstein
|     |     |     |     |     | IPW1 | IPW2 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
et al. [15, Section 3.2.3] note that (cid:3)ˆ has a so-called ‘double-robustness’ property that the
DR
estimator remains consistent if either (i) the propensity score model is correctly speci(cid:1)ed but
the two regression models m and m are not or (ii) the two regression models are correctly
|     |     |     |     | 0   | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
speci(cid:1)ed but the propensity score model is not, although under these conditions it need no
|     |     |     |     |     | (cid:3)ˆ |     | (cid:3)ˆ |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
longer be most e(cid:4)cient. Neither nor need be consistent if e is incorrectly
|     |     |     |     |     | IPW1 |     | IPW2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
speci(cid:1)ed, as the motivating arguments earlier in this section would no longer be valid.
It is also possible to derive other estimators in the Robins et al. class that do not incor-
porate regression modeling by attempting to improve directly upon estimation of (cid:1) and (cid:1) .
1 0
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2943
With R known, the estimators for (cid:1) and (cid:1) in (cid:3)ˆ and (cid:3)ˆ solve
1 0 IPW1 IPW2
(cid:4) (cid:9) (cid:10)(cid:5) (cid:4) (cid:9) (cid:10)(cid:5)
(cid:1)n Z(Y −(cid:1) ) Z −e (cid:1)n (1−Z)(Y −(cid:1) ) Z −e
i i 1 +(cid:4) i i =0 and i i 0 −(cid:4) i i =0
e 1 e 1−e 0 1−e
i=1 i i i=1 i i
(10)
respectively, where ((cid:4) ;(cid:4) )=((cid:1) ;(cid:1) ) yields (cid:3)ˆ and ((cid:4) ;(cid:4) )=(0;0) gives (cid:3)ˆ . This
0 1 0 1 IPW1 0 1 IPW2
suggests improving upon (cid:3)ˆ and (cid:3)ˆ by identifying constants (cid:4) ;(cid:4) that minimize
IPW1 IPW2 0 1
the large-sample variance of solutions to the equations in (10), given by (cid:4) = − E
1
{Z(Y − (cid:1) )=e2}=E{(Z − e)2=e2} and (cid:4) = − E{(1 − Z)(Y − (cid:1) )=(1 − e)2}=E{(Z − e)2=
1 0 0
(1−e)2}, which motivates estimating these constants by solving
(cid:11) (cid:9) (cid:10)(cid:12) (cid:11) (cid:9) (cid:10)(cid:12)
(cid:1)n (Z(Y −(cid:1) ) Z −e 2 (cid:1)n (1−Z)(Y −(cid:1) ) Z −e 2
i i 1 +(cid:4) i i =0 and i i 0 +(cid:4) i i =0
e2 1 e (1−e)2 0 1−e
i=1 i i i=1 i i
(11)
In practice, one would estimate R, solving (10) and (11) jointly with (3), yielding
(cid:4) (cid:9) (cid:10)(cid:5) (cid:9) (cid:10)
(cid:1)n Z C −1(cid:1)n ZY C
(cid:3)ˆ = i 1− 1 i i 1− 1
IPW3 eˆ eˆ eˆ eˆ
i=1 i i i=1 i i
(cid:4) (cid:9) (cid:10)(cid:5) (cid:9) (cid:10)
(cid:1)n 1−Z C −1(cid:1)n (1−Z)Y C
− i 1− 0 i i 1− 0
1−eˆ 1−eˆ 1−eˆ 1−eˆ
i=1 i i i=1 i i
=(cid:1)ˆ −(cid:1)ˆ (12)
1;IPW3 0;IPW3
(cid:13)
(cid:1)n (cid:1)n
C = {(Z −eˆ)=eˆ} {(Z −eˆ)=eˆ}2
1 i i i i i i
i=1 i=1
(cid:13)
(cid:1)n (cid:1)n
C =− {(Z −eˆ)=(1−eˆ)} {(Z −eˆ)=(1−eˆ)}2
0 i i i i i i
i=1 i=1
Unlike (7) and (8), in the (cid:1)rst term of (12), each weight eˆ
−1
is proportionately scaled by
i
a measure of how the sample, weighted exposure indicators Z=eˆ deviate from their expec-
i i
tation (if R were known) of 1, and similarly for the second term. In large samples, C , C
0 1
should be close to 0, but for smaller n, this scaling proportionately reduces or increases each
‘complete-case’ weight. For (cid:3)ˆ and (cid:3)ˆ , inverse weighting an observation by a very
IPW1 IPW2
small complete-case probability can result in numerical instability, particularly when n is not
large. Thus, the scaling has the e(cid:2)ect in practice of o(cid:2)ering stability in the case where some
complete-case probabilities may be small or are highly variable. Interestingly, the ‘augmenta-
tion’ incorporated in (cid:3)ˆ tends to lessen such instability problems in practice.
DR
As we demonstrate in Section 4, estimators like (cid:3)ˆ that do not incorporate regression
IPW3
models, although improving in precision over (cid:3)ˆ and (cid:3)ˆ , cannot achieve the e(cid:4)ciency
IPW1 IPW2
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2944
|     |     |     |     | J. K. | LUNCEFORD AND M. DAVIDIAN |     |     |
| --- | --- | --- | --- | ----- | ------------------------- | --- | --- |
gains possible through ‘augmentation’ involving regression as in (cid:3)ˆ . Hirano and Imbens [16]
DR
report on a practical application of weighted methods and advocate incorporation of regression
| models | as  | in (9) | for this | reason. |     |     |     |
| ------ | --- | ------ | -------- | ------- | --- | --- | --- |
2.5. Summary
|     |     |     |     |     |     | (cid:3)ˆ | (cid:3)ˆ |
| --- | --- | --- | --- | --- | --- | -------- | -------- |
It is important to recognize that incorporation of regression modelling in and is
|     |     |     |     |     |     | DR  | SR  |
| --- | --- | --- | --- | --- | --- | --- | --- |
di(cid:2)erent from a popular alternative to all estimators previously discussed, that of estimation
|     | directly |     |     |     |     | E(Y |Z;X)=(cid:3) | +(cid:3) Z+ |
| --- | -------- | --- | --- | --- | --- | ----------------- | ----------- |
of (cid:3) from a regression model. For example, for a linear model 0 Z
| XT(cid:3) |     |     |     |     |     | |Z=1;X)}− |     |
| --------- | --- | --- | --- | --- | --- | --------- | --- |
, under (2), it is straightforward to verify that (cid:3)=E(Y )−E(Y )=E{E(Y
|     | X   |     |     |     | 1   | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
E{E(Y |Z=0;X)}=(cid:3) . For models nonlinear in X such as the logistic, this di(cid:2)erence may
Z
X.
not have a closed form, as each term involves integration over the distribution of In either
case, the direct modelling approach has serious drawbacks; Rubin [17] o(cid:2)ers an excellent
discussion. When dim(X) is large, ensuring that the regression model is correct, and hence
that a consistent estimator for (cid:3) will be obtained, is di(cid:4)cult. In addition, if the distributions of
some confounders do not overlap substantially in the treated and control groups, the regression
X
relationship is determined primarily by treated subjects in one region of the space and by
control subjects in another, so that estimates of causal e(cid:2)ects using direct modelling are
(cid:3)ˆ
essentially based on extrapolation. In contrast, the regression modelling used by largely
SR
circumvents this, as X and Z should be approximately independent within-strata. Moreover,
(cid:3)ˆ
by ‘double robustness,’ even if the regression models in are incorrect, this estimator,
DR
which incorporates regression models only as a way to gain e(cid:4)ciency over simpler weighted
| estimators, |     | will still | be consistent. |     |     |     |     |
| ----------- | --- | ---------- | -------------- | --- | --- | --- | --- |
|Z;X)
When the true regression is linear and var(Y is constant, direct modelling may be
implemented by ordinary least squares (OLS), which is ML estimation if Y |Z;X has a normal
|Z;X)
distribution. If, in fact, these conditions hold, and the chosen model for E(Y is correctly
speci(cid:1)ed by the analyst, then standard large sample theory implies that the resulting estimator
for (cid:3) will be consistent and the most e(cid:4)cient. One would thus expect the direct regression
approach to outperform those based on propensity scores; however, such gains would be at the
risk of the disadvantages noted above. In Section 4, we investigate these issues empirically.
The same considerations apply to ML estimation for any regression model, e.g., logisitic
| regression |     | for binary | response. |          |          |     |     |
| ---------- | --- | ---------- | --------- | -------- | -------- | --- | --- |
|            |     | (cid:3)ˆ   | (cid:3)ˆ  | (cid:3)ˆ | (cid:3)ˆ |     |     |
As noted, , , , and are all members of the class of consistent, semi-
|     |     | IPW1 | IPW2 | IPW3 | DR  |     |     |
| --- | --- | ---- | ---- | ---- | --- | --- | --- |
parametric estimators of Robins et al. [13]. However, as shown in Section 3.2, for (cid:1)xed K,
| (cid:3)ˆ |     |     |     |     | (cid:3)ˆ (cid:3)ˆ |     |     |
| -------- | --- | --- | --- | --- | ----------------- | --- | --- |
is not consistent and evidently neither nor makes use of inverse weighting, so
S S SR
these estimators are not members of this class. Thus, although insights into additional proper-
|     | (cid:3)ˆ | (cid:3)ˆ | (cid:3)ˆ |     | (cid:3)ˆ |     |     |
| --- | -------- | -------- | -------- | --- | -------- | --- | --- |
ties of , , , and follow easily from the Robins et al. theory, as shown
|     |     | IPW1 IPW2 | IPW3 |     | DR  |     |     |
| --- | --- | --------- | ---- | --- | --- | --- | --- |
next in Sections 3.1 and 3.3, those for (cid:3)ˆ and (cid:3)ˆ must be deduced separately.
S SR
|     |     |     |     | 3.  | THEORETICAL PROPERTIES |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- |
In this section we summarize properties of the estimators and highlight the practical insights
that can be deduced from these. The large-sample properties for weighted estimators follow
from the general framework of Reference [13] and may also be obtained directly from the
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2945
standard theory of M-estimation, as we describe in Section 3.1. The properties for strati(cid:1)cation
estimators to our knowledge have not been elucidated and are sketched in Section 3.2.
3.1. Weighted estimators
Properties of (cid:3)ˆ , (cid:3)ˆ , (cid:3)ˆ , and (cid:3)ˆ when e is correctly speci(cid:1)ed may be deduced
IPW1 IPW2 IPW3 DR
by viewing them as solutions to a set of estimating equations. To(cid:1)obtain (cid:3)ˆ
IPW1
and (cid:3)ˆ
IPW2
,
one solves jointly in ((cid:3);R) (3) and an equation of the form n (Y;Z;X ;(cid:3);R)=0
i=1 (cid:3) i i i
that follows from (7) or (8). For (cid:3)ˆ , implied by (12) also depends on (cid:4) , (cid:4) ,
IPW3 (cid:3) 0 1
and this equation is solved jointly with those in (11) and (3); similarly correspond-
(cid:3)
i(cid:1)ng to (cid:3)ˆ
DR
in (9) depends on Q
0
, Q
1
, which are estimated by solving equations of the form
n I(Z =z) (Y;X ;Q )=0, z=0;1, as for OLS or logistic regression.
i=1 i (cid:3)z i i z
This representation allows application of the theory of M-estimation; a review is given by
Stefanski and Boos [18]. From Equation (3) of Reference [18], because the expectations of
, , and for (cid:3)ˆ , (cid:3)ˆ , and (cid:3)ˆ are zero at the true values of R, (cid:4) , (cid:4) , and (cid:3),
(cid:2) (cid:4) (cid:3) IPW1 IPW2 IPW3 0 1
the estimators of these quantities converge in probability to the true values, and hence, (cid:3)ˆ ,
IPW1
(cid:3)ˆ , and (cid:3)ˆ are consistent for (cid:3) , the true value of (cid:3). (This may be seen equivalently
IPW2 IPW3 0
by substituting the true values of R, (cid:4) , and (cid:4) in (7), (8), and (12) and applying the law
0 1
of large numbers directly.) A similar argument shows that (cid:3)ˆ converges in probability to
DR
(cid:3) , even if the models m are not correctly speci(cid:1)ed, as the corresponding still has mean
0 z (cid:3)
zero. The theory [18, Section 2] then implies that each estimator is such that n1=2((cid:3)ˆ −(cid:3) )
0
converges in distribution to a N(0;(cid:6)) random variable.
It instructive to (cid:1)rst consider the (unlikely) case where R is known, so that e(X;R) is a
known function of X and joint solution with (3) is unnecessary. Under these conditions, for
(cid:3)ˆ ;(cid:3)ˆ , and (cid:3)ˆ , the large-sample variances are
IPW1 IPW2 IPW3
(cid:9) (cid:10) (cid:4) (cid:5)
Y2 Y2 (Y −(cid:1) )2 (Y −(cid:1) )2
(cid:6)∗ = E 1 + 0 −(cid:3)2; (cid:6)∗ =E 1 1 + 0 0
IPW1 e 1−e 0 IPW2 e 1−e
(cid:4) (cid:5) (cid:9) (cid:10) (cid:9) (cid:10) (13)
(Y −(cid:1) )2 (Y −(cid:1) )2 Y −(cid:1) Y −(cid:1)
(cid:6)∗ = E 1 1 + 0 0 +(cid:4) E 1 1 +(cid:4) E 0 0 +2(cid:4) (cid:4)
IPW3 e 1−e 1 e 0 1−e 1 0
where expectations are with respect to the distribution of (Y ;Y ;X) and all parameters are
0 1
equal to their true values. It may be shown that (cid:6)∗ ¿(cid:6)∗ . If, as in practice, R is estimated,
IPW2 IPW3
then the variances become, with E =E[e eT={e(1−e)}],
(cid:2)(cid:2) (cid:2) (cid:2)
(cid:4)(cid:9) (cid:10) (cid:5)
Y Y
(cid:6) =(cid:6)∗ −HT E−1H ; H =E 1 + 0 e (14)
IPW1 IPW1 (cid:2);1 (cid:2)(cid:2) (cid:2);1 (cid:2);1 e 1−e (cid:2)
(cid:4)(cid:9) (cid:10) (cid:5)
Y −(cid:1) Y −(cid:1)
(cid:6) =(cid:6)∗ −HT E−1H ; H =E 1 1 + 0 0 e (15)
IPW2 IPW2 (cid:2);2 (cid:2)(cid:2) (cid:2);2 (cid:2);2 e 1−e (cid:2)
(cid:4)(cid:9) (cid:10) (cid:5)
Y −(cid:1) +(cid:4) Y −(cid:1) +(cid:4)
(cid:6) =(cid:6)∗ −HT E−1H ; H =E 1 1 1 + 0 0 0 e (16)
IPW3 IPW3 (cid:2);3 (cid:2)(cid:2) (cid:2);3 (cid:2);3 e 1−e (cid:2)
thus exhibiting the interesting property that estimating R, even if its true value is known,
leads to smaller (large-sample) variance for these estimators than using the true value. Thus,
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2946 J. K. LUNCEFORD AND M. DAVIDIAN
even if the functional form of the propensity score is known exactly, it is bene(cid:1)cial from an
e(cid:4)ciency standpoint to estimate it anyway. We have found in empirical studies like those in
Section 4 that in general (cid:6) ¿(cid:6) ¿(cid:6) .
IPW1 IPW2 IPW3
For (cid:3)ˆ , similar arguments show that its large-sample variance is
DR
(cid:14)(cid:15) (cid:15) (cid:16)
2
1−e e
(cid:6) =(cid:6)∗ −E {E(Y |X)−(cid:1) }+ {E(Y |X)−(cid:1) } (17)
DR IPW2 e 1 1 1−e 0 0
The Robins et al. [13] theory guarantees that (cid:6) 6(cid:6) , (cid:6) , and (cid:6) . As long as the
DR IPW1 IPW2 IPW3
propensity and regression models do not share parameters, (cid:6) is the same whether R and
DR
Q , Q are known or estimated.
0 1
The components of the expressions in (14)–(17) may be estimated from the observed data,
yielding approximate sampling variances for (cid:3)ˆ , (cid:3)ˆ , (cid:3)ˆ , and (cid:3)ˆ . Alternatively,
IPW1 IPW2 IPW3 DR
variance estimates may be obtained via the empirical sandwich method [18, Sections 2 and
3], which we have found to be more stable in practice. Speci(cid:1)cally, for propensity models of
the form {1+exp(−WTR)}−1, where W is a function of elements in X, approximate sampling
(cid:1)
variances are computed as n−2 n Iˆ2 , where
i=1 i
Iˆ = Z i Y i − (1−Z i )Y i −(cid:3)ˆ −(Z −eˆ)HˆT Eˆ −1W (18)
IPW1;i eˆ 1−eˆ IPW1 i i (cid:2);1 (cid:2)(cid:2) i
i i
Iˆ = Z i (Y i −(cid:1)ˆ 1;IPW2 ) − (1−Z i )(Y i −(cid:1)ˆ 0;IPW2 ) −(Z −eˆ)HˆT Eˆ −1W (19)
IPW2;i eˆ 1−eˆ i i (cid:2);2 (cid:2)(cid:2) i
i i
Z(Y −(cid:1)ˆ )+(cid:4)ˆ (Z −eˆ) (1−Z)(Y −(cid:1)ˆ )−(cid:4)ˆ (Z −eˆ)
Iˆ = i i 1;IPW3 1 i i − i i 0;IPW3 0 i i
IPW3;i eˆ 1−eˆ
i i
−(Z −eˆ)HˆT Eˆ −1W (20)
i i (cid:2);3 (cid:2)(cid:2) i
ZY −m (X ;Qˆ )(Z −eˆ) (1−Z)Y +m (X ;Qˆ )(Z −eˆ)
Iˆ = i i 1 i 1 i i − i i 0 i 0 i i −(cid:3)ˆ (21)
DR;i eˆ (1−eˆ) DR
i i
(cid:1) (cid:1) (cid:17)(cid:1)
Eˆ
−1
=n−1 n eˆ(1−eˆ)WWT, (cid:4)ˆ = − n {Z(Y −(cid:1)ˆ )=eˆ2} n {(Z −eˆ)=eˆ}2, and
(cid:2)(cid:2) (cid:1) i=1 i i i i 1 i=(cid:17)1(cid:1) i i 1;IPW3 i i=1 i i i
(cid:4)ˆ =− n {(1−Z)(Y −(cid:1)ˆ )=(1−eˆ)2} n {(Z −eˆ)=(1−eˆ)}2. The terms Hˆ , Hˆ ,
0 i=1 i i 0;IPW3 i i=1 i i i (cid:2);1 (cid:2);2
and Hˆ are empirical versions of the terms in (14)–(16):
(cid:2);3
(cid:4) (cid:5)
(cid:1)n ZY(1−eˆ) (1−Z)Yeˆ
Hˆ =n−1 i i i + i i i W
(cid:2);1 eˆ 1−eˆ i
i=1 i i
(cid:4) (cid:5)
(cid:1)n Z(Y −(cid:1)ˆ )(1−eˆ) (1−Z)(Y −(cid:1)ˆ )eˆ
Hˆ =n−1 i i 1;IPW2 i + i i 0;IPW2 i W
(cid:2);2 eˆ 1−eˆ i
i=1 i i
(cid:4) (cid:5)
(cid:1)n Z(Y −(cid:1)ˆ +(cid:4)ˆ )(1−eˆ) (1−Z)(Y −(cid:1)ˆ +(cid:4)ˆ )eˆ
Hˆ =n−1 i i 1;IPW3 1 i + i i 0;IPW3 0 i W
(cid:2);3 eˆ 1−eˆ i
i=1 i i
In Section 4, we demonstrate performance of these formul(cid:7).
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2947
3.2. Strati(cid:1)cation estimators
Here, we present a heuristic account of large-sample results for (cid:3)ˆ and (cid:3)ˆ based on repre-
S SR
senting the strati(cid:1)cation and within-stratum estimation schemes for each as solutions to sets
of estimating equations. Because in practice it is standard to take a predetermined number
of strata K regardless of sample size (K=5 is most common), we view K as (cid:1)xed (so not
depending on n). As in Section 3.1, assume e is correctly speci(cid:1)ed.
Both (cid:3)ˆ and (cid:3)ˆ involve estimation not only of R by solving (3), as before, but also of
S SR
the true quantiles q=(q 1 ;:::;q K−1 )T, which may be carried out by solving
(cid:1)n (cid:1)n
S(X ;q;R)= I(e6q)−j=K=0; j=1;:::;K −1 (22)
qj i j i j
i=1 i=1
These equations do not have zero solutions for some n, but this technicality does not a(cid:2)ect
the spirit of the discussion below. We may rewrite (4) in an asymptotically equivalent form
by replacing n =n with its limit K−1 and writing pˆ =n =n as
j j 1j
(cid:11) (cid:12) (cid:11) (cid:12)
(cid:3)ˆ =n−1 (cid:1)n Z i Y i (cid:1)K I(eˆ i ∈Qˆ j ) −n−1 (cid:1)n (1−Z i )Y i (cid:1)K I(eˆ i ∈Qˆ j ) (23)
S K pˆ K 1=K −pˆ
i=1 j=1 j i=1 j=1 j
This shows that (cid:3)ˆ also requires estimation of the probabilities p=(p ;:::;p )T that an
S 1 K
individual is treated and has propensity score in Q j =(q j−1 ;q j ], where q 0 =0, q K =1; the
estimator pˆ =n =n follows from solving the equations
j 1j
(cid:1)n (cid:1)n
p S j (Z i ;X i ;q j−1 ;q j ;p j ;R)= Z i I(e i ∈Q j )−p j =0; j=1;:::;K (24)
i=1 i=1
Instead, calculation of (cid:3)ˆ involves solving in Q(j) for j=1;:::;K
SR
(cid:1)n (cid:1)n
(cid:3) S (j) (Y i ;Z i ;X i ;q j−1 ;q j ;Q(j))= I(e i ∈Q j ){Y i −m(j)(Z i ;X i ;Q(j))}m (cid:3) (j)(Z i ;X i ;Q(j))=0
i=1 i=1
(25)
where m(j) is the vector of partial derivatives of m(j) with respect to elements of Q(j). We
(cid:3)
are now in a position to characterize fully each estimator and evaluate properties.
First consider (cid:3)ˆ . Even with e(X;R) correctly speci(cid:1)ed, as noted in Section 2.3, we expect
S
(cid:3)ˆ to be inconsistent due to failure of strati(cid:1)cation to eliminate all confounding, an observa-
S
tion we may now formalize. Noting that (3), (22), and (24) have expectation zero at the true
values of X=(qT;pT;RT)T, we may conclude from [18, Section 2] that solving these equations
jointly yields consistent estimators for the elements of X. Thus, considering the asymptoti-
cally equivalent form (23), we may replace eˆ, Qˆ , and pˆ by their true values and apply the
i j j
law of lar
(cid:1)
ge numbers directly to see that (cid:3)ˆ
S
converges in proba
(cid:1)
bility to (cid:3)∗=(cid:1)
1
∗−(cid:1)
0
∗, where
(cid:1)∗=K−1 K E{Y eI(e∈Q )}=E{eI(e∈Q )}, and (cid:1)∗=K−1 K E{Y (1 − e)I(e∈Q )}=
1 j=1 1 j j 0 j=1 0 j
[K−1−E{eI(e∈Q
j
)}]. It is straightforward to see that a su(cid:4)cient condition for (cid:3)∗=(cid:3)
0
is (Y ;Y )(cid:1)X, in which case confounding is not an issue, as would be expected, but, in
0 1
general, (cid:3)∗ (cid:1)=(cid:3)
0
so that (cid:3)ˆ
S
is not consistent. The hope in practice, of course, is that
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2948
|     |     |     |     | J. K. | LUNCEFORD | AND | M.  | DAVIDIAN |     |     |     |
| --- | --- | --- | --- | ----- | --------- | --- | --- | -------- | --- | --- | --- |
|(cid:3)∗ − (cid:1)(cid:3) | is ‘small.’ Thus, (cid:3)ˆ estimates (cid:3)∗, and from (23) an estimating equation for
|          | 0   |             |                   |     | S     |     |     |     |     |     |     |
| -------- | --- | ----------- | ----------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
|          | n   |             | ;X;(cid:3)∗;X)=0, |     |       |     |     |     |     |     |     |
| (cid:3)∗ | is  |   S (Y ;Z   |                   |     | where |     |     |     |     |     |     |
|          | i=1 | (cid:3) ∗ i | i                 |     |       |     |     |     |     |     |     |
(cid:1)K
|     |     |   S (Y;Z;X;(cid:3)∗;X)=ZYK−1 |     |     |     |     | I(e | ∈Q )=p | −(1−Z)YK−1 |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --- |
|     |     | (cid:3)∗                     | i i |     | i   | i   | i   | j      | j          | i i |     |
j=1
(cid:1)K
|     |     |     |     |     | ×   |       | ∈Q )=(K−1−p |     | )−(cid:3)∗ |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ---------- | --- | --- |
|     |     |     |     |     |     | I(e i | j           |     | j          |     |     |
j=1
|     |     | (cid:1) |     |     |     |     |     |     |     | (cid:3)ˆ Xˆ |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
Writing =(  S;:::;  S ;  S;:::;  S ;  )T, we thus see that and jointly solve
|     |     | (cid:5) q1 | qK−1 | p1  | pK  | (cid:2) |     |     |     | S   |     |
| --- | --- | ---------- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- |
(cid:1)n
|     |     |     | {(cid:1)T | (Z        | ;X ;X);  | S (Y | ;Z ;X;(cid:3)∗;X)}T=0 |     |     |     | (26) |
| --- | --- | --- | --------- | --------- | -------- | ---- | --------------------- | --- | --- | --- | ---- |
|     |     |     |           | (cid:5) i | i        | ∗ i  | i                     |     |     |     |      |
(cid:3)
i=1
in X and (cid:3)∗. The properties of (cid:3)ˆ may be derived from (26) by appealing to M-estimation
S
arguments [18]. Consider (cid:1)rst the ‘ideal’ situation where the q, p , and R are all known.
|     |     |     |     |     |     |     |     |     |     | j j |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Letting f(·) be the density of the propensity score and E(·|e) be conditional expectation given
e
n1=2((cid:3)ˆ
the propensity score, it may be shown under these conditions that −(cid:3)∗) converges
S
| in distribution |     | to a N(0;(cid:6)∗) |     | random | variable, |     | where |     |     |     |     |
| --------------- | --- | ------------------ | --- | ------ | --------- | --- | ----- | --- | --- | --- | --- |
S
(cid:18)
|     |     |              |     | (cid:1)K | qj                 |     |     |     | (cid:1)K |        |     |
| --- | --- | ------------ | --- | -------- | ------------------ | --- | --- | --- | -------- | ------ | --- |
|     |     | (cid:6)∗=K−2 |     | p−2      | E(Y2|t)tf(t)dt+K−2 |     |     |     |          | −p )−2 |     |
(1=K
|     |     | S   |     | j   |      | 1   | e   |     |     | j   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | j=1 | qj−1 |     |     |     | j=1 |     |     |
(cid:18)
qj
|     |     |     | ×   | E(Y2|t)(1−t)f(t)dt−(cid:3)2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 0                           |     | e   |     | ∗   |     |     |     |
qj−1
Comparing this expression to those in (13) suggests that (cid:3)ˆ has di(cid:2)erent properties from
S
(cid:6)∗
weighted estimators, as depends critically on the density of the propensity score. In the
S
more realistic case where the q, p , and R are estimated, via M-estimation arguments for
|     |     |     |     | j   | j   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nonsmooth   functions [18, Section 4] to account for nondi(cid:2)erentiability of some elements
| of (26) | in  | q and R, | the variance |     | is  |     |     |     |     |     |     |
| ------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
j
=(cid:6)∗+(cid:2)
|     |     |     |     | (cid:6) |     | +(cid:2) | +(cid:2) |           |     |     | (27) |
| --- | --- | --- | --- | ------- | --- | -------- | -------- | --------- | --- | --- | ---- |
|     |     |     |     |         | S S | p        | qp       | (cid:2)qp |     |     |      |
where (cid:2), (cid:2) , and (cid:2) are quantities modifying the ‘ideal’ variance (cid:6)∗ due to estimation in
|     | p   | qp (cid:2)qp |         |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | p,  | q, R;        | (cid:2) |     |     |     |     | R   |     |     | q p |
turn of and e.g. is the e(cid:2)ect of estimating rather than knowing it if and
(cid:2)qp
are estimated (see the Appendix). In contrast to the situation in (14), (15), and (16), it is not
possible to deduce that any of (cid:2), (cid:2) , or (cid:2) in (27) are negative, which would imply that
|     |     |     |     | p   | qp  | (cid:2)qp |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
p, q,
estimation of and=or R reduces variance relative to the (unlikely) situation where they
are known.
(cid:3)ˆ
We may follow a similar argument for SR . This estimator requires joint solution of (3),
(22), and (25); as above, solving the (cid:1)rst two jointly leads to consistent estimators for R
and the q. Substituting these in (25), from the theory of M-estimation [18, Section 2],
j
the resulting estimators Qˆ(j), j=1;:::;K, solving (25) converge in probability to some Q (j)
∗
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2949
satisfying E{ (cid:3) S (j) (Y;Z;X;q j−1 ;q j ;Q ∗ (j))}=0 for each j, where Q ∗ (j) depend on the functions
m(j) used. Now, substituting n =n≈K−1 in (5), we may rewrite (6) as
j
(cid:1)n (cid:1)K
(cid:3)ˆ =n−1 I(eˆ ∈Qˆ ){m(j)(1;X;Qˆ(j))−m(j)(0;X ;Qˆ(j))} (28)
SR i j i i
i=1j=1
(cid:1)
Then, applying the law of large numbers to (28), (cid:3)ˆ
SR
converges in probability to (cid:3)∗∗= K
j=1
E[I(e∈Q j ){ (cid:1) m(j)(1;X;Q ∗ (j))−m(j)(0;X;Q ∗ ( (cid:1) j))}]; e.g. for the linear model example following
(5), (cid:3)∗∗= K j=1 E{I(e∈Q j )}Q ∗ (j)=K−1 K j=1 Q ∗ (j). If the within-stratum regression models
m(j)(Z;X;Q(j)) are chosen such that they are all of the exact form of the true regression rela-
tionship E(Y |Z;X)=m(Z;X;Q 0 ), say, for some m and true value Q 0 , then Q ∗ (j)=Q 0 for each j,
as under these conditions E{ (cid:3) S (j) (Y;Z;X;q j−1 ;q j ;Q 0 )}=E(I(e∈Q j )E[{Y −m(Z;X;Q 0 )}|Z;X]
m (Z;X;Q ))=0 because the inner conditional expectation is zero. Thus, using (2) and m(z;X;
(cid:3) 0
Q )=E(Y |Z=z;X)
0
(cid:1)K
(cid:3)∗∗= E[I(e∈Q
j
){E(Y |Z=1;X)−E(Y |Z=0;X)}]
j=1
(cid:14)(cid:11) (cid:12) (cid:16)
(cid:1)K
=E I(e∈Q ) {E(Y |X)−E(Y |X)} =E{E(Y |X)−E(Y |X)}=(cid:3)
j 1 0 1 0 0
j=1
where we use the facts that the sum over j of the indicators of stratum membership is one for
any (cid:1)xed X and E{E(Y |X)−E(Y |X)} is equal to the true value of (cid:3). This demonstrates
1 0
that (cid:3)ˆ is a consistent estimator for (cid:3) as long as the m(j) have the same form as the true
SR 0
regression relationship. However, if the m(j) are chosen di(cid:2)erently, and hence incorrectly,
this argument does not hold, and (cid:3)∗∗ (cid:1)=(cid:3)
0
in general. Hence, choice of the within-stratum
regression models is critical for consistency of (cid:3)ˆ . In contrast, by ‘double robustness,’ (cid:3) ,
SR DR
will be consistent regardless of whether the regression models chosen for ‘augmentation’ are
correct. In Section 4, we demonstrate these properties empirically.
Analogous to the results for (cid:3)ˆ , again by the theory of M-estimation, it may be shown
S
that in general n1=2((cid:3)ˆ
SR
−(cid:3)∗∗) converges in distribution to a normal random variable with
variance similar in form to that in (27); thus, no general insights are possible.
Such theory is not used in practice; rather, it is routine to approximate the sampling vari-
ance of (cid:3)ˆ by treating (cid:3)ˆ as the average of K independent, within-stratum, treatment e(cid:2)ect
S S
estimates as
(cid:1)K
K−2 (cid:6)ˆ2 (29)
j
j=1
assuming an equal number of individuals per stratum, where (cid:6)ˆ2 is an estimate of the variance
j
of the di(cid:2)erence between the treatment means in stratum j given by (cid:6)ˆ2=n−1s2 + (n −
(cid:1) (cid:1) j 1j 1j j
n )−1s2 , s2 =n−1 n I(eˆ ∈Qˆ )(ZY −y(cid:8) )2, s2 =(n −n )−1 n I(eˆ ∈Qˆ ){(1−Z)Y −
1j 0j 1j (cid:1)1j i=1 i j i i 1j 0j j (cid:1)1j i=1 i j i i
y(cid:8) }2, y(cid:8) =n−1 n I(eˆ ∈Qˆ )ZY, and y(cid:8) =(n −n )−1 n I(eˆ ∈Qˆ )(1−Z)Y. Similarly,
0j 1j 1j i=1 i j i i 0j j 1j i=1 i j i i
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2950
|     |     |     |     | J. K. | LUNCEFORD |     | AND M. DAVIDIAN |     |     |     |     |
| --- | --- | --- | --- | ----- | --------- | --- | --------------- | --- | --- | --- | --- |
the sampling variance of (cid:3)ˆ is approximated in practice by an expression of the form (29)
SR
with (cid:6)ˆ2 replaced by an estimate of the variance of m(j)(1;X;Qˆ(j))−m(j)(0;X;Qˆ(j)) based on
j
the (cid:1)t of the regression model in stratum j; e.g., for the linear model example after (6), this
(cid:3)ˆ(j),
would be the estimated sampling variance of obtainable directly from standard regression
Z
software.
| 3.3. | E(cid:2)ect | of additional |     | covariates |     |     |     |     |     |     |     |
| ---- | ----------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
X
In the previous development, it was assumed that is associated with both treatment exposure
and potential response and that (2) holds. For (cid:3)ˆ , a common guideline is that it is preferable
S
to ‘over-model’ the propensity score by including additional covariates unrelated to treatment
exposure rather than run the risk of excluding relevant ones [5,19]. In fact, intuition would
suggest that including such covariates when they are correlated with potential response could
provide additional information on (cid:3). It is possible to gain formal insight as follows.
Suppose V is an additional set of covariates, exclusive of X, that (i) is not associated with
treatment exposure but (ii) is associated with potential response. More precisely, (i) may be
written as P(Z=1|X;V)=P(Z=1|X), and (ii) implies that the conditional distributions of
Y and Y given (Z;X;V) depend on V. Suppose that the analyst is willing to assume strong
0 1
|              |     |       |      | X V, |      |     |     |     |     |     |     |
| ------------ | --- | ----- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
| ignorability |     | given | both | and  | i.e. |     |     |     |     |     |     |
)(cid:1)Z|(X;V)
|     |     |     |     |     | (Y ;Y |     |     |     |     |     | (30) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
0 1
It is straightforward to show using manipulations similar to those in Reference [20] that here
(30) implies that (2) also holds. Thus, it is possible to specify a model P(Z=1|X;V)=
| e(X;V;R;S), |     |     | S   |     |     | (q×1) |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
where is an additional parameter corresponding to terms in the model
involving V, such that this model reduces to the true propensity score e(X;R) (depending on
X and R only) when S=0, its ‘true’ value, and the assumptions underlying the derivations
of (14)–(17) and (27) hold. Suppose, then, that the chosen propensity score model satis(cid:1)es
e(X;V;R;0)=e(X;R)=e and is such that @=@R{e(X;V;R;S)}| =e depending on X and R
(cid:7)=0 (cid:2)
e(X;V;R;S)=[1+exp{−(XTR+VTS)}]−1.
| only; | e.g. | as for | the logistic | model |     |     |     |     |     |     |     |
| ----- | ---- | ------ | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Under these circumstances, for all methods, (cid:3) will be estimated jointly with both the
previous additional parameters and S. The e(cid:2)ect of including V in the propensity model may
thus be deduced by considering the previous estimating equations for each estimator, replacing
| e(X;R) | by  | e(X;V;R;S), |     | and adding | the     | additional | equation |     |     |     |     |
| ------ | --- | ----------- | --- | ---------- | ------- | ---------- | -------- | --- | --- | --- | --- |
|        |     | (cid:1)n    |     | −e(X       | ;V;R;S) |            |          |     |     |     |     |
Z
|     |     |     |     | i             | i i |          | @=@S{e(X | ;V;R;S)}=0 |     |     | (31) |
| --- | --- | --- | --- | ------------- | --- | -------- | -------- | ---------- | --- | --- | ---- |
|     |     |     | e(X | ;V;R;S){1−e(X |     | ;V;R;S)} |          | i i        |     |     |      |
|     |     |     | i   | i             |     | i i      |          |            |     |     |      |
i=1
|      |      | @=@S{e(X;V;R;S)} |     |           |     |        | S=0     |            |         | X   | V;  |
| ---- | ---- | ---------------- | --- | --------- | --- | ------ | ------- | ---------- | ------- | --- | --- |
| Note | that |                  |     | evaluated |     | at the | ‘truth’ | may depend | on both | and | in  |
V=[e(X;V;R;S){1−e(X;V;R;S)}].
| the | logistic | example, |     | this partial | derivative | is  |     |     |     | In  | general, |
| --- | -------- | -------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | -------- |
write e =@=@S{e(X;V;R;S)}| , with subscript i when evaluated at (X ;V).
|     | (cid:7) |     |     | (cid:7)=0 |     |     |     |     | i i |     |     |
| --- | ------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Incorporating the additional estimating equation (31) for each estimator, it may be shown
by M-estimation arguments [18] that all weighted estimators still are consistent and such that
n1=2((cid:3)ˆ −(cid:3)
) converges in distribution to a mean-zero normal random variable, now with
0
di(cid:2)erent variance (cid:6)V. De(cid:1)ning E =E[e eT={e(1−e)}] and E =E[e eT={e(1−e)}], and
|     |     |     |     |     | (cid:7)(cid:7) | (cid:7) (cid:7) |     | (cid:7)(cid:2) | (cid:7) (cid:2) |     |     |
| --- | --- | --- | --- | --- | -------------- | --------------- | --- | -------------- | --------------- | --- | --- |
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2951
|         |     |                               |                | ESTIMATION |                | OF CAUSAL  | TREATMENT |     | EFFECTS |     |     |
| ------- | --- | ----------------------------- | -------------- | ---------- | -------------- | ---------- | --------- | --- | ------- | --- | --- |
| letting | H   | =E                            | −E             | E−1ET      | , for          | (cid:3)ˆ , |           |     |         |     |     |
|         |     | (cid:7)(cid:2) (cid:7)(cid:7) | (cid:7)(cid:2) |            | (cid:7)(cid:2) | IPW2       |           |     |         |     |     |
(cid:2)(cid:2)
|     |     |          |          | −(H | −E        | E−1H           | )TH−1(H                  |                | −E E−1H                  |                          |      |
| --- | --- | -------- | -------- | --- | --------- | -------------- | ------------------------ | -------------- | ------------------------ | ------------------------ | ---- |
|     |     | (cid:6)V | =(cid:6) |     |           |                |                          |                |                          | )                        | (32) |
|     |     | IPW2     | IPW2     |     | (cid:7);2 | (cid:7)(cid:2) | (cid:2)(cid:2) (cid:2);2 | (cid:7)(cid:2) | (cid:7);2 (cid:7)(cid:2) | (cid:2)(cid:2) (cid:2);2 |      |
where H =E[{(Y −(cid:1) )=e+(Y −(cid:1) )=(1−e)}e ] , with similar expressions for (cid:6)V and
|          |     | (cid:7);2 | 1   | 1   | 0   | 0   |     | (cid:7) |     |     | IPW1 |
| -------- | --- | --------- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- |
| (cid:6)V |     |           |     |     |     |     |     |         |     | V   |      |
. From (32) and these analogous expressions, the e(cid:2)ect of including in the propensity
IPW3
score model is to reduce the variance relative to that in the case where V is excluded.
The practical implication is that, at least in large samples, for these weighted estimators,
incorporating covariates in the propensity model that are not related to treatment exposure but
are associated with potential response will always lead to precision for estimating (cid:3) at least
| as  | great | as that attained |     | by disregarding |     | such | covariates. |     |     |     |     |
| --- | ----- | ---------------- | --- | --------------- | --- | ---- | ----------- | --- | --- | --- | --- |
When V is considered, the form of the semiparametric e(cid:4)cient estimator, which now is
that with smallest large-sample variance among all estimators in the Robins et al. [13] class
;X;V)
under the condition that the distribution of (Y ;Y is unspeci(cid:1)ed, is di(cid:2)erent from (9),
|     |     |     |     |     |     |     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which does not acknowledge availability of V. In particular, we now have
(cid:1)n ZY −(Z −eˆˆ)m∗(X ;V;Tˆ ) (cid:1)n (1−Z)Y +(Z −eˆˆ)m∗(X ;V;Tˆ )
|     | (cid:3)ˆ =n−1 |     | i i | i   | i 1 | i i | 1 −n−1 |     | i i | i i 0 | i i 0 |
| --- | ------------- | --- | --- | --- | --- | --- | ------ | --- | --- | ----- | ----- |
DR
|     |     |     |     |     | eˆˆ |     |     |     |     | 1−eˆˆ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
|     |     | i=1 |     |     | i   |     |     | i=1 |     | i     |     |
(33)
eˆˆ
where =e(X ;V;Rˆ;Sˆ), and m∗(X;V;T )=E(Y |Z=z;X;V) is the regression of Y on (X;V)
|     | i   | i   | i   |     | z   | z   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | T   |     | Tˆ  |     |     |
in group z;z=0;1, depending on parameters z estimated by z from subjects with Z=z.
As before, this estimator requires modelling of the regression and maintains the ‘double-
| robustness’ |     | property. | The | large            | sample | variance | of  | (33) |          |     |          |
| ----------- | --- | --------- | --- | ---------------- | ------ | -------- | --- | ---- | -------- | --- | -------- |
|             |     |           |     | (cid:14)(cid:15) |        |          |     |      | (cid:15) |     | (cid:16) |
2
|     |     |     |     |     | 1−e |     |     |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:6)V =(cid:6)∗ −E {E(Y |X;V)−(cid:1) }+ {E(Y |X;V)−(cid:1) }
|     |     |          |          |     |     | 1   |     | 1   |     | 0   | 0   |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | DR       | IPW2     |     | e   |     |     |     | 1−e |     |     |
|     |     | (cid:6)V | 6(cid:6) |     |     |     |     |     |     |     |     |
and satis(cid:1)es DR , so that a potential gain in e(cid:4)ciency over disregarding information
|     |     | V DR |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on Y in is achieved. Of course, (cid:6)V 6(cid:6)V ;(cid:6)V , and (cid:6)V as well.
|     |                       |     |     |     |          | DR  | IPW1 | IPW2 | IPW3 |     |     |
| --- | --------------------- | --- | --- | --- | -------- | --- | ---- | ---- | ---- | --- | --- |
|     | e(X;V;R;0)=e;(cid:3)ˆ |     |     |     | (cid:3)ˆ |     |      |      |      |     |     |
As and still converge in probability to (cid:3)∗ and (cid:3)∗∗ in general;
|     |     |     |     | S   | SR  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
however, the large-sample variances change. For example, for (cid:3)ˆ , by similar arguments, where
S
now (31) is solved jointly with the previous equations, the variance is (see the appendix)
|     |         |     |     |     |     | (cid:6)V | +(cid:2)           |     |     |     |         |
| --- | ------- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | --- | ------- |
|     |         |     |     |     |     | =(cid:6) |                    |     |     |     | (34)    |
|     |         |     |     |     |     | S        | S (cid:7)(cid:2)qp |     |     |     |         |
|     | (cid:2) |     |     |     |     |          |                    |     | S   |     | (p;q;R) |
where represents the additional e(cid:2)ect of estimating rather than knowing it if
(cid:7)(cid:2)qp
are estimated; as before, it is not possible to show (cid:2) 60. A similar development holds
(cid:7)(cid:2)qp
(cid:3)ˆ
for , where we still have (cid:3)∗∗=(cid:3) if the m(j) are chosen according to the true regression
|     | SR  |     |     |     |     | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
relationship. Thus, in contrast to the results for weighted estimators, it is not immediately
V
evident whether incorporating covariates into the propensity model leads to a reduction in
variance for these estimators over not. In Section 4, we investigate this issue empirically.
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2952 J. K. LUNCEFORD AND M. DAVIDIAN
4. SIMULATION STUDIES
In practice, several covariates will likely be available for modelling the propensity score. To
investigate relative performance in such a realistic setting, we carried out simulations involving
a number of continuous and discrete covariates and a continuous response such that (cid:3) ¿0,
0
where larger values of the response are preferred, so that treatment is bene(cid:1)cial.
We considered covariates X=(X ;X ;X )T associated with both treatment exposure and
1 2 3
potential response, i.e. confounders, and covariates V=(V ;V ;V )T associated with potential
1 2 3
response but not treatment exposure, so that the e(cid:2)ect of adding such covariates as in Section
3.3 could be gauged. In particular, in all scenarios, Z was generated as Bernoulli according
to the true propensity score e(X;R)={1+exp(−(cid:2) −(cid:2) X −(cid:2) X −(cid:2) X )}−1, not involving
0 1 1 2 2 3 3
elements of V, and the response Y was generated according to
Y =(cid:8) +(cid:8) X +(cid:8) X +(cid:8) X +(cid:8) Z +(cid:9) V +(cid:9) V +(cid:9) V +(cid:10); (cid:10)∼N(0;1) (35)
0 1 1 2 2 3 3 4 1 1 2 2 3 3
and ]=((cid:8) ;(cid:8) ;(cid:8) ;(cid:8) ;(cid:8) )T=(0;−1;1;−1;2)T, so that in all cases (cid:3) =(cid:8) =2. Settings of
0 1 2 3 4 0 4
R=((cid:2) ;(cid:2) ;(cid:2) ;(cid:2) )T and ^=((cid:9) ;(cid:9) ;(cid:9) )T were chosen to represent di(cid:2)erent degrees of asso-
0 1 2 3 1 2 3
ciation, as described below. All scenarios are such that values of X associated with lower
responses are also associated with increased propensity for treatment, so that subjects with a
covariate pro(cid:1)le indicating poor response are those more likely to be treated.
The joint distribution of (X;V) was speci(cid:1)ed by taking X ∼ Bernoulli (0.2) and then gener-
3
ating V as Bernoulli with P(V =1|X )=0:75X + 0:25(1 − X ). Conditional on
3 3 3 3 3
X ;(X ;V ;X ;V )T was then generated as multivariate normal N((cid:2) ;(cid:3) ), where
3 1 1 2 2 X3 X3
     
1 −1 1 0:5 −0:5 −0:5
     
     
 1  −1  0:5 1 −0:5 −0:5
(cid:2) 1 =     (cid:2) 0 =     and (cid:3) 1 =(cid:3) 0 =    
−1  1  −0:5 −0:5 1 0:5 
     
−1 1 −0:5 −0:5 0:5 1
Values for ] and ^ were taken such that each positively-correlated pair (X ;V );k=1;2, has
k k
coe(cid:4)cients of the same sign in (35) and thus X and V have similar and correlated e(cid:2)ects
k k
on response. Overall, the values for ];R, and ^ result in lower response values and larger
probabilities of treatment exposure when X =1 and conversely when X =0. Note that (35)
3 3
implies E(Y |Z=z;X;V)=(cid:8) +(cid:8) X +(cid:8) X +(cid:8) X +(cid:8) z+(cid:9) V +(cid:9) V +(cid:9) V =m∗(X;V;T )
0 1 1 2 2 3 3 4 1 1 2 2 3 3 z z
for z=0;1, where T =((cid:8) ;(cid:8) ;(cid:8) ;(cid:8) ;(cid:9) ;(cid:9) ;(cid:9) )T, T =((cid:8)∗;(cid:8) ;(cid:8) ;(cid:8) ;(cid:9) ;(cid:9) ;(cid:9) )T, and (cid:8)∗=(cid:8) +(cid:8) .
0 0 1 2 3 1 2 3 1 0 1 2 3 1 2 3 0 0 4
Moreover, this formulation implies expressions of the form E(Y |Z=z;X)=m (X;Q )=(cid:3) +
z z 0
(cid:3) X +(cid:3) X +(cid:3) X +(cid:8) z for some Q =((cid:3) ;(cid:3) ;(cid:3) ;(cid:3) )T;Q =((cid:3)∗;(cid:3) ;(cid:3) ;(cid:3) )T, and (cid:3)∗=(cid:3) +(cid:8) .
1 1 2 2 3 3 4 0 0 1 2 3 1 0 1 2 3 0 0 4
Settings of R and ^ that achieve the features described above were chosen to represent
varying degrees of association of the corresponding covariate to Z or Y. Three settings of
^ were used to examine the in(cid:5)uence of the strength of the association between V and re-
sponse when over-(cid:1)tting the propensity score: ^str=(−1:0;1:0;1:0)T;^mod=(−0:5;0:5;0:5)T,
and ^no=(0;0;0)T , where superscripts no, mod, and str denote ‘no,’ ‘moderate,’ and ‘strong’
association. When ^=^no;V is associated with neither potential response nor treatment expo-
sure, so from Section 3.3 we expect no bene(cid:1)t to including it in an analysis. Two
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2953
|     | ESTIMATION |     | OF CAUSAL | TREATMENT |     | EFFECTS |     |     |     |
| --- | ---------- | --- | --------- | --------- | --- | ------- | --- | --- | --- |
settings Rstr=(0:0;0:6;−0:6;0:6)T and Rmod=(0:0;0:3;−0:3;0:3)T were considered, correspond-
X,
ing to strong and moderate association of Z and yielding marginal exposure probabilities
P(Z=1)=0:38 (str) and 0.42 (mod). For each of the six combinations of (^;R), 1000 Monte
n=1000
Carlo (MC) data sets were generated for and 5000 to emulate many published
applications. For each, (cid:3) was estimated using (cid:3)ˆ ;(cid:3)ˆ ;(cid:3)ˆ ;(cid:3)ˆ , and (cid:3)ˆ and (cid:3)ˆ
|     |     |     |     |     | IPW1 | IPW2 IPW3 | DR  |     | S SR |
| --- | --- | --- | --- | --- | ---- | --------- | --- | --- | ---- |
X
with K=5 two ways: (i) including only the true confounders in the propensity score,
as described in Sections 2.4 and 2.3, thus (cid:1)tting the true propensity model e(X;R) above
by ML, and (ii) including both X and V as described in Section 3.3, (cid:1)tting the propensity
e(X;V;R;S)={1+exp(−(cid:2) −(cid:2) −(cid:2) −(cid:2) −(cid:7) −(cid:7) −(cid:7) )}−1
| model |     |     | X   | X   | X   | V   | V   | V   | by ML. |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|       |     | 0   | 1 1 | 2 2 | 3 3 | 1 1 | 2 2 | 3 3 |        |
For (cid:3)ˆ , in (i), we (cid:1)t the correct linear models m (X;Q ) implied above, and in (ii) we (cid:1)t
| DR  |     |     |     |     | z   | z   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
instead m∗(X;V;T ); z=0;1, both by OLS. For (cid:3)ˆ , we similarly (cid:1)t within each stratum the
| z   | z         |     |         | SR  |     |     |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     | E(Y |Z;X) | E(Y | |Z;X;V) |     |     |     |     |     |     |
true models for and for (i) and (ii), respectively. As discussed in
Section 2.5, because OLS is ML estimation in this situation and hence serves as a ‘bench-
mark,’ we also estimated (cid:3) =(cid:8) by directly (cid:1)tting the true models for (i) E(Y |Z;X) and
0 4
(cid:3)ˆ
| (ii) E(Y |Z;X;V) | by this method, | denoted |     | .   |     |     |     |     |     |
| ---------------- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ML
|     |     |     | (cid:3)ˆ |     |     |     | (cid:3)ˆ | (cid:3)ˆ |     |
| --- | --- | --- | -------- | --- | --- | --- | -------- | -------- | --- |
To investigate ‘double robustness’ of and sensitivity of and to incorrect
|     |     |     |     | DR  |     |     | SR  | ML  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
speci(cid:1)cation of regression models, for both (i) and (ii), we also implemented these estimators
using the correct propensity models but mismodelling the relevant regression relationships
by leaving (X ;V ) and X out of the models for E(Y |Z;X;V) and E(Y |Z;X), respectively,
1 1 1
| (cid:3)ˆ | (cid:3)ˆ |     |     | (cid:3)ˆ |     |     |     |     |     |
| -------- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- |
denoted by DR∗ and SR∗. Similarly, for , we (cid:1)t these misspeci(cid:1)ed models directly by
ML
(cid:3)ˆ
| OLS, denoted | by ML∗. |     |     |     |     |     |     |                    |          |
| ------------ | ------- | --- | --- | --- | --- | --- | --- | ------------------ | -------- |
|              |         |     |     |     |     |     |     | (cid:3)ˆ ;(cid:3)ˆ | (cid:3)ˆ |
Table I summarizes results in the case where the regression models in DR SR , and ML
correspond to the true relationships; as (cid:3)ˆ performed uniformly more poorly than the
IPW1
(cid:3)ˆ
other IPW estimators, it is omitted for brevity. Biases for all estimators but are less than
S
(cid:3)ˆ
3 per cent in all scenarios, so are not shown. Those for S under conditions (i) and (ii)
can be substantial, particularly when associations are strong, demonstrating the inconsistency
|     |     |     |     |     |     | (cid:3)ˆ |     |     | (cid:3)ˆ |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- |
of this estimator. Thus, although MC standard deviation of S is smaller than that of IPW2
and (cid:3)ˆ in many cases, e(cid:4)ciency gains of the latter estimators over (cid:3)ˆ as measured by
| IPW3 |     |     |     |     |     |     |     | S   |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MC mean square error (MSE) ratio are considerable. In principle, in smaller sample sizes,
biased estimators may outperform estimators with larger sampling variance, as the bias is
small relative to the variance. However, in our experience, we have found this not to be true
for (cid:3)ˆ , with this estimator having bias far exceeding the bias |(cid:3)∗ −(cid:3) | predicted by the
| S   |     |     |     |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:3)ˆ
theory. The result is that weighted estimators achieve e(cid:4)ciency gains over at both small
S
and large sample sizes, with comparable performance only in a limited range of moderate
|     |     |     |     |     | (cid:3)ˆ |     |     |     | (cid:3)ˆ |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | -------- |
sample sizes (see Reference [21]). The estimator has smaller variance than ,
|     |     |     |     |     | IPW3 |     |     |     | IPW2 |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
particularly when R=Rstr, showing that this estimator does indeed increase e(cid:4)ciency over
|     |     |     |     |     | (cid:3)ˆ | (cid:3)ˆ |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
simpler weighted estimators. However, the results for and shows that incorporation
|     |     |     |     |     | DR  |     | SR  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of regression modelling yields a substantial payo(cid:2). For the former, as predicted by the the-
(cid:3)ˆ
ory, MC standard deviations for these estimator are uniformly smaller than those for
IPW2
| (cid:3)ˆ |     |     |     |     |     |     |     | (cid:3)ˆ |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
and IPW3 , which is re(cid:5)ected in dramatically improved e(cid:4)ciencies relative to S . In scenar-
ios involving strong association between X and treatment exposure, (cid:3)ˆ outperforms (cid:3)ˆ ,
|     |     |     |     |     |     |     |     | SR  | DR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with smaller variance and hence higher relative e(cid:4)ciency; otherwise, these two estimators
exhibit approximately equivalent performance. Consistent with its ‘benchmark’ role, the ML
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2954 J. K. LUNCEFORD AND M. DAVIDIAN
Table I. Monte Carlo results, multivariate confounder, correct regression modelling. Bias is bias of (cid:3)ˆ
S S
(percentoftruevalue(cid:3) =2:0).Foreach(^;R)setting,(i)denotesestimatorsusingXonly,(ii)denotes
0
estimators using X and V as in Section 3. MC MSE ratios are computed as MC MSE
S
=MC MSEm ,
where m denotes the indicated estimator and MC MSE is MC bias squared plus MC variance.
MC standard deviation MSE ratio
^ R Bias (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ SR IPW2 IPW3 DR ML
S S SR IPW2 IPW3 DR ML
n=1000
^str Rstr (i) −28.4 0.184 0.151 0.454 0.234 0.167 0.134 15.65 1.73 5.92 12.79 19.91
(ii) −28.5 0.151 0.087 0.450 0.208 0.097 0.077 45.80 1.72 7.01 37.03 59.38
Rmod (i) −16.0 0.153 0.118 0.150 0.138 0.119 0.117 8.99 5.59 6.61 8.85 9.28
(ii) −15.9 0.125 0.072 0.120 0.103 0.071 0.069 22.65 8.09 11.01 22.83 24.47
^mod Rstr (i) −22.3 0.136 0.106 0.356 0.180 0.116 0.093 19.41 1.71 5.92 16.25 25.05
(ii) −22.6 0.128 0.089 0.361 0.175 0.099 0.078 27.81 1.68 6.25 22.39 36.11
Rmod (i) −12.7 0.111 0.083 0.112 0.100 0.083 0.082 11.26 6.19 7.66 11.12 11.46
(ii) −12.8 0.103 0.070 0.103 0.089 0.070 0.068 15.32 7.17 9.44 15.56 16.40
^no Rstr (i) −16.1 0.109 0.091 0.252 0.138 0.098 0.080 13.80 1.81 5.43 11.97 17.86
(ii) −16.1 0.111 0.092 0.263 0.140 0.099 0.080 13.66 1.67 5.35 11.89 17.96
Rmod (i) − 9.0 0.088 0.069 0.090 0.081 0.069 0.067 8.35 4.96 6.04 8.32 8.71
(ii) − 9.0 0.086 0.069 0.091 0.082 0.069 0.067 8.27 4.83 5.93 8.24 8.68
n=5000
^str Rstr (i) −28.5 0.079 0.064 0.206 0.110 0.070 0.059 80.22 7.75 26.1 67.0 95.15
(ii) −28.5 0.067 0.039 0.203 0.102 0.042 0.035 219.05 8.00 30.10 183.10 265.80
Rmod (i) −16.2 0.067 0.052 0.066 0.061 0.052 0.051 40.93 25.40 29.50 40.60 41.73
(ii) −16.1 0.051 0.030 0.050 0.044 0.030 0.030 118.81 42.20 55.00 119.20 121.57
^mod Rstr (i) −22.3 0.061 0.047 0.168 0.088 0.052 0.043 92.57 7.16 25.30 73.70 112.09
(ii) −22.4 0.057 0.039 0.168 0.084 0.045 0.035 130.78 7.23 27.20 102.00 162.67
Rmod (i) −12.6 0.052 0.038 0.050 0.046 0.039 0.038 44.79 26.90 31.80 43.70 45.28
(ii) −12.7 0.046 0.031 0.043 0.039 0.031 0.031 70.00 35.10 43.70 68.90 70.89
^no Rstr (i) −16.1 0.047 0.038 0.118 0.065 0.042 0.034 73.03 7.52 24.00 60.70 92.28
(ii) −16.1 0.048 0.038 0.119 0.065 0.042 0.034 73.25 7.49 24.10 60.80 92.32
Rmod (i) − 9.2 0.039 0.031 0.038 0.036 0.031 0.031 36.75 24.40 27.80 36.50 37.82
(ii) − 9.2 0.040 0.031 0.038 0.036 0.031 0.031 36.61 24.10 27.50 36.30 37.67
estimator exceeds (under Rstr) or attains similar performance to (under Rmod) that of (cid:3)ˆ
DR
and (cid:3)ˆ .
SR
Comparison of results under (i) and (ii) con(cid:1)rm the reduction in variance expected from the
theory in Section 3.3 for weighted estimators when ‘over-(cid:1)tting’ the propensity score using
prognostic covariates, i.e. when ^=^mod or ^str. The few instances of slight e(cid:4)ciency loss
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2955
at n=1000 are resolved at n=5000. Gains achieved by (cid:3)ˆ are most dramatic. Moreover,
DR
for a particular R setting, including V in the analysis with (cid:3)ˆ when ^=^mod or ^str results
DR
in MC standard deviation equal to that possible when there is no association between V and
response (^=^no). In contrast, the other weighted estimators gain e(cid:4)ciency by including V,
but an increase in the magnitude of ^ is associated with an increase in variance. Although
theory in Section 3.3 is not informative for (cid:3)ˆ and (cid:3)ˆ , the empirical results suggest that
S SR
their sampling variation is also reduced by such ‘over-(cid:1)tting’. In fact, we have evaluated
(cid:2) in (34) in numerous situations and found its sign always to be negative.
(cid:7)(cid:2)qp
Table II shows analogous results for (cid:3)ˆ SR∗;(cid:3)ˆ DR∗, and (cid:3)ˆ ML∗. ‘Double robustness’ of (cid:3)ˆ DR∗
is con(cid:1)rmed; under all scenarios, the bias of this estimator is less than 1 per cent and is
thus not shown. Moreover, the e(cid:4)ciency of this estimator relative to (cid:3)ˆ , which uses correct
DR
regression models, only su(cid:2)ers noticeably when R=Rstr and is superior to that of (cid:3)ˆ and
IPW2
(cid:3)ˆ in every case, showing that ‘augmentation’ of usual weighted estimators by regression
IPW3
relationships may increase precision even if the models are not exactly correct. In contrast,
failure to incorporate the correct regression relationship leads to bias of (cid:3)ˆ SR∗, although its
magnitude is smaller than that of (cid:3)ˆ in Table I. This feature results in considerably poorer
S
e(cid:4)ciency of (cid:3)ˆ SR∗ relative to (cid:3)ˆ DR∗. The drawback of direct regression modelling is clearly
evident; using an incorrect model yields signi(cid:1)cant bias and consequently drastically inferior
performance. These results suggest that, if one insists on estimators like (cid:3)ˆ or (cid:3)ˆ that
SR ML
involve regression modelling explicitly, the former is ‘safer.’ The nature of the mismodelling
we have examined was chosen deliberately to be rather extreme to demonstrate the potential
pitfalls of these approaches; here, disregarding X in the regression modelling disregards a
1
confounder, emphasizing how sensitive these estimators are to violation of key assumptions
in the regression model, a situation to which (cid:3)ˆ is robust.
DR
To further assess the quality of inference, we calculated nominal 95 per cent Wald con(cid:1)-
dence intervals for (cid:3) as estimate ±1:96× estimated standard deviation for each estimator,
0
using the sandwich method based on (18)–(21) for the weighted estimators, using (29) for (cid:3)ˆ
S
and the analogous approach for (cid:3)ˆ , and using the usual OLS standard error for (cid:3)ˆ . Table
SR ML
III shows Monte Carlo coverage probabilities for case (i). Low coverages for (cid:3)ˆ are due to
S
the residual biases in Table I, as estimated standard errors from (29) performed well, closely
tracking the MC standard deviations. Coverage for (cid:3)ˆ and (cid:3)ˆ achieves the nominal
IPW2 IPW3
level under Rmod, with somewhat optimistic performance when this association is strong. No-
tably, coverages for (cid:3)ˆ ;(cid:3)ˆ , and (cid:3)ˆ attain the nominal level in all cases; moreover, so
DR SR ML
do those for (cid:3)ˆ DR∗, despite augmentation by the ‘wrong’ regression model. In contrast, due to
the biases in Table II, coverages based on (cid:3)ˆ SR∗ and (cid:3)ˆ ML∗ are far from nominal.
The foregoing results take K=5 for (cid:3)ˆ , as is common in practice; however, with larger
S
sample sizes, one might re(cid:1)ne the balancing e(cid:2)ect of strati(cid:1)cation by increasing K. Table IV
shows for case (i) performance of (cid:3)ˆ when the number of strata was doubled from K=5 to
S
10. While MC standard deviations and standard errors for (cid:3)ˆ are similar and remain fairly
S
constant from K=5 to 10, bias is reduced by roughly 65 per cent in all scenarios, yielding
improved coverage (although still not at the nominal level). However, performance of (cid:3)ˆ is
S
still inferior to that of the other estimators, and, because residual bias, although smaller than
for K=5, remains constant as n increases, coverage worsens for n=5000.
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2956
|     |     | J. K. LUNCEFORD |     | AND M. DAVIDIAN |     |     |     |     |
| --- | --- | --------------- | --- | --------------- | --- | --- | --- | --- |
Table II. MonteCarloresults,multivariateconfounder,incorrectregressionmodelling.Bias andBias
|     |     |     |     |     |     |     | SR∗ | ML∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:3)ˆ (cid:3)ˆ
are bias of SR∗ and ML∗ (percent of true value (cid:3) =2:0). All other entries are as in Table I.
0
|     |     |     | MC  | standard | deviation |     | MSE ratio |     |
| --- | --- | --- | --- | -------- | --------- | --- | --------- | --- |
^ R Bias SR∗ Bias ML∗ (cid:3)ˆ SR∗ (cid:3)ˆ DR∗ (cid:3)ˆ ML∗ SR∗ DR∗ ML∗
n=1000
| ^str Rstr | −11.9      | −35.2 |       |       |       |      |       |      |
| --------- | ---------- | ----- | ----- | ----- | ----- | ---- | ----- | ---- |
|           | (i)        |       | 0.166 | 0.207 | 0.164 | 4.24 | 8.30  | 0.68 |
|           | −          | −23.6 |       |       |       |      |       |      |
|           | (ii) 8.3   |       | 0.107 | 0.141 | 0.120 | 8.96 | 17.53 | 1.47 |
| Rmod      | (i) − 6.7  | −18.0 | 0.131 | 0.121 | 0.152 | 3.62 | 8.55  | 0.83 |
|           | (ii) − 4.5 | −12.0 | 0.085 | 0.074 | 0.109 | 7.69 | 21.52 | 1.67 |
| ^mod Rstr | (i) − 9.8  | −28.4 | 0.118 | 0.141 | 0.124 | 4.17 | 10.99 | 0.64 |
|           | (ii) − 7.8 | −21.5 | 0.102 | 0.121 | 0.106 | 6.36 | 15.03 | 1.12 |
| Rmod      | (i) − 5.3  | −14.7 | 0.092 | 0.085 | 0.110 | 3.89 | 10.57 | 0.78 |
|           | (ii) − 4.2 | −11.2 | 0.077 | 0.072 | 0.094 | 5.88 | 14.79 | 1.28 |
| ^no Rstr  | (i) − 7.3  | −21.0 | 0.103 | 0.118 | 0.101 | 3.61 | 8.34  | 0.62 |
|           | (ii) − 6.8 | −18.8 | 0.101 | 0.118 | 0.100 | 4.05 | 8.40  | 0.77 |
| Rmod      | −          | −10.9 |       |       |       |      |       |      |
|           | (i) 3.8    |       | 0.075 | 0.070 | 0.087 | 3.58 | 8.08  | 0.73 |
|           | −          | −     |       |       |       |      |       |      |
|           | (ii) 3.5   | 9.6   | 0.073 | 0.070 | 0.085 | 3.94 | 8.03  | 0.90 |
n=5000
| ^str Rstr | −12.2      | −35.3 |               |       |       |       |        |      |
| --------- | ---------- | ----- | ------------- | ----- | ----- | ----- | ------ | ---- |
|           | (i)        |       | 0.069         | 0.084 | 0.074 | 5.15  | 46.74  | 0.65 |
|           | −          | −23.7 |               |       |       |       |        |      |
|           | (ii) 8.6   |       | 0.047         | 0.058 | 0.055 | 10.32 | 98.13  | 1.45 |
| Rmod      | −          | −18.3 |               |       |       |       |        |      |
|           | (i) 6.9    |       | 0.056         | 0.053 | 0.065 | 4.93  | 39.50  | 0.79 |
|           | −          | −12.2 |               |       |       |       |        |      |
|           | (ii) 4.8   |       | 0.035         | 0.031 | 0.049 | 10.32 | 114.02 | 1.72 |
| ^mod Rstr | (i) − 9.9  | −28.4 | 0.052         | 0.067 | 0.058 | 4.83  | 44.57  | 0.63 |
|           | (ii) − 7.9 | −21.4 | 0.045         | 0.056 | 0.049 | 7.62  | 64.86  | 1.10 |
| Rmod      | (i) − 5.5  | −14.7 | 0.042         | 0.039 | 0.050 | 4.83  | 42.89  | 0.74 |
|           | (ii) − 4.3 | −11.1 | 0.034         | 0.031 | 0.043 | 7.82  | 68.23  | 1.30 |
| ^no Rstr  | (i) − 7.4  | −21.3 | 0.041         | 0.053 | 0.044 | 4.50  | 37.79  | 0.58 |
|           | (ii) − 6.9 | −19.1 | 0.042         | 0.052 | 0.043 | 5.06  | 39.55  | 0.72 |
| Rmod      | (i) − 4.1  | −11.1 | 0.034         | 0.032 | 0.040 | 4.46  | 35.36  | 0.71 |
|           | (ii) − 3.8 | − 9.9 | 0.034         | 0.032 | 0.039 | 5.09  | 35.19  | 0.88 |
|           |            |       | 5. DISCUSSION |       |       |       |        |      |
We have reviewed and compared two principal approaches to estimating average causal e(cid:2)ects
from observational data using the propensity score, those based on strati(cid:1)cation and weighting.
We hope that this presentation serves as a resource to practitioners who wish to appreciate
the rationale for and di(cid:2)erences between these two classes of techniques and to understand
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2957
|     |     |            | ESTIMATION  | OF       | CAUSAL        | TREATMENT |     | EFFECTS  |             |         |     |
| --- | --- | ---------- | ----------- | -------- | ------------- | --------- | --- | -------- | ----------- | ------- | --- |
|     |     | Table III. | Monte Carlo | coverage | probabilities |           | for | case (i) | in Tables I | and II. |     |
^ R (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ (cid:3)ˆ
|     |     | S   | SR  | SR∗ |     | IPW2 | IPW3 |     | DR DR∗ | ML  | ML∗ |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | ------ | --- | --- |
n=1000
| ^str | Rstr | 13.5 | 94.7 | 71.5 | 88.4 |     | 88.0 | 94.5 | 94.3 | 94.6 | 1.3  |
| ---- | ---- | ---- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | ---- |
|      | Rmod | 44.8 | 94.8 | 83.6 | 94.1 |     | 93.6 | 94.9 | 95.1 | 94.6 | 32.8 |
^mod Rstr
|     |     | 9.8 | 95.4 | 68.1 | 88.1 |     | 87.3 | 95.8 | 94.5 | 95.2 | 0.2 |
| --- | --- | --- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | --- |
Rmod
|     |      | 38.1 | 95.0 | 82.6 | 94.9 |     | 93.9 | 95.3 | 95.1 | 95.0 | 26.1 |
| --- | ---- | ---- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | ---- |
| ^no | Rstr | 15.1 | 94.1 | 70.6 | 89.2 |     | 88.9 | 94.8 | 93.9 | 95.3 | 1.7  |
|     | Rmod | 49.1 | 95.6 | 85.4 | 94.6 |     | 94.7 | 95.7 | 95.5 | 95.6 | 32.5 |
n=5000
| ^str | Rstr | 0.0 | 95.3 | 9.0  | 91.5 |     | 91.5 | 95.6 | 95.2 | 94.7 | 0.0 |
| ---- | ---- | --- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | --- |
|      | Rmod | 0.1 | 95.7 | 37.5 | 95.6 |     | 95.2 | 95.9 | 95.7 | 95.8 | 0.0 |
^mod Rstr
|     |     | 0.0 | 94.9 | 4.6 | 91.0 |     | 90.8 | 94.3 | 93.2 | 95.0 | 0.0 |
| --- | --- | --- | ---- | --- | ---- | --- | ---- | ---- | ---- | ---- | --- |
Rmod
|     |     | 0.1 | 94.3 | 28.8 | 94.9 |     | 94.5 | 94.5 | 95.0 | 94.0 | 0.0 |
| --- | --- | --- | ---- | ---- | ---- | --- | ---- | ---- | ---- | ---- | --- |
^no Rstr
|     |      | 0.0 | 95.4 | 8.6      | 91.5 |     | 90.3 | 95.6 | 93.9 | 96.4     | 0.0 |
| --- | ---- | --- | ---- | -------- | ---- | --- | ---- | ---- | ---- | -------- | --- |
|     | Rmod | 0.3 | 95.1 | 34.8     | 95.5 |     | 95.7 | 94.9 | 94.4 | 94.8     | 0.0 |
|     |      |     |      | (cid:3)ˆ |      |     |      |      |      | (cid:3)ˆ |     |
Table IV. Monte Carlo results for at K=10 for case (i) Table I. Bias is bias of expressed as
|     |     |     |     | S   |     |     |     |     |     | S   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
percentage of the true value (cid:3) =2:0. MC SD is Monte Carlo standard deviation, Ave SE is the average
0
of estimated standard errors of (cid:3)ˆ using (29), and Coverage is Monte Carlo coverage of 95 per cent
S
(cid:3)ˆ
con(cid:1)dence interval. MSE ratios are as in Table I; is still based on K=5 as in previous tables.
SR
|     |     |     |     |     |     |     |     |     | MSE | ratio |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
^ R
|     |     | Bias | MC  | SD (Ave | SE) | Coverage |     | IPW2 | IPW3 | DR  | SR  |
| --- | --- | ---- | --- | ------- | --- | -------- | --- | ---- | ---- | --- | --- |
n=1000
| ^str | Rstr | −9.9 | 0.188 |     | (0.167) |     | 72.9 | 0.39 | 1.23 | 2.82 | 3.28 |
| ---- | ---- | ---- | ----- | --- | ------- | --- | ---- | ---- | ---- | ---- | ---- |
|      | Rmod | −5.3 |       |     |         |     |      |      |      |      |      |
|      |      |      | 0.133 |     | (0.135) |     | 88.4 | 1.26 | 1.50 | 2.05 | 2.06 |
| ^mod | Rstr | −7.9 |       |     |         |     |      |      |      |      |      |
|      |      |      | 0.141 |     | (0.122) |     | 72.4 | 0.34 | 1.32 | 3.55 | 3.98 |
|      | Rmod | −4.4 | 0.099 |     | (0.098) |     | 85.0 | 1.39 | 1.69 | 2.40 | 2.58 |
| ^no  | Rstr | −6.0 | 0.111 |     | (0.097) |     | 73.9 | 0.39 | 1.25 | 2.95 | 3.18 |
|      | Rmod | −3.2 | 0.077 |     | (0.078) |     | 87.7 | 1.35 | 1.56 | 2.09 | 3.09 |
n=5000
| ^str | Rstr | −10.0 | 0.077 |     | (0.076) |     | 25.0 | 0.99 | 3.38 | 8.78  | 11.21 |
| ---- | ---- | ----- | ----- | --- | ------- | --- | ---- | ---- | ---- | ----- | ----- |
|      | Rmod | −5.5  |       |     |         |     |      |      |      |       |       |
|      |      |       | 0.059 |     | (0.059) |     | 53.1 | 3.57 | 4.13 | 5.62  | 5.92  |
| ^mod | Rstr | −7.7  |       |     |         |     |      |      |      |       |       |
|      |      |       | 0.055 |     | (0.055) |     | 19.3 | 1.07 | 3.82 | 10.04 | 12.17 |
|      | Rmod | −4.3  | 0.042 |     | (0.043) |     | 48.1 | 3.84 | 4.55 | 6.58  | 6.20  |
| ^no  | Rstr | −5.7  | 0.047 |     | (0.045) |     | 26.9 | 1.14 | 3.40 | 7.97  | 10.64 |
|      | Rmod | −3.1  | 0.035 |     | (0.034) |     | 54.8 | 3.29 | 3.81 | 5.20  | 5.27  |
their relative performance. Strategies based on matching on propensity scores or adjusting for
the propensity score in direct regression modelling [2], which we did not consider, are also
popular.
Theoretical and empirical results indicate that the popular version of strati(cid:1)cation via esti-
mated propensity scores based on within-stratum sample mean di(cid:2)erences and a (cid:1)xed number
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2958 J. K. LUNCEFORD AND M. DAVIDIAN
of strata can lead to biased inference due to residual confounding, and the e(cid:2)ect of this bias
becomes more serious with increasing sample size. Using more strata can increase the sample
size at which the trade-o(cid:2) of bias and variability involved in e(cid:4)ciency takes place, but stra-
tifying on quintiles seems to be the most popular approach in practice, even for substantial
sample sizes. Thus, as the ‘trade-o(cid:2)’ point will be unknown for any speci(cid:1)c problem, this
approach should be used with caution. An interesting avenue for future research would be to
establish guidelines for choosing the number of strata based on theoretical analysis of the rate
at which the number of strata should increase with sample size to eliminate bias. A modi(cid:1)-
cation of strati(cid:1)cation based instead on within-stratum regression estimates of treatment e(cid:2)ect
can eliminate this bias and achieve dramatic improvements in e(cid:4)ciency, but correct speci(cid:1)ca-
tion of the regression model is essential; otherwise, bias and degradation of performance can
result. In this regard, this approach is similar to estimating causal e(cid:2)ects via direct regression
modelling but is less sensitive to mismodelling.
Methods based on weighting are consistent and o(cid:2)er approximately unbiased inference for
practical sample sizes. The semiparametric e(cid:4)cient estimator identi(cid:1)ed by the theory of Robins
et al. [13], which incorporates regression modelling as a way to gain e(cid:4)ciency, also yields
high precision. Although strati(cid:1)cation based on regression and direct modelling can outperform
this approach under some conditions, this estimator enjoys the unique ‘double robustness’
property in that it continues to lead to unbiased estimation of the average causal e(cid:2)ect even
if the regression models involved do not coincide with the true relationship, a(cid:2)ording the
analyst broad protection against misspeci(cid:1)cation not available with these other approaches.
The results presented here support routine use of this estimator in practice.
APPENDIX A: DERIVATION OF (27) AND (34)
Applying the results in Section A.3.6 of Reference [22] to (26), we have
(cid:25)
=A−1(B −A A−1B −BT A−TAT +A A−1B A−TAT )A−T (A36)
22 22 21 11 12 12 11 21 21 11 11 11 21 22
S
where the matrices in this expression follow from tedious evaluation of the required derivatives
and covariance matrix. In particular, it may be shown that A = −1, and
22
   
E 0 E F F 0
A 11 =    E p qq q −I K E p q(cid:2) (cid:2)   ; B 11 =     F q T q p q F p qp p F p(cid:2)    
0 0 −E 0 FT E
(cid:2)(cid:2) p(cid:2) (cid:2)(cid:2)
Here, E qq =diag{f e (q 1 );f e (q 2 );:::;f e (q K−1 )}; E p (i; q j)=q j f e (q j ); i=(cid:26)j;−q j f e (q j );i=j +1, and
zero otherwise (K×K−1); and E (K−1×p) has jth row @=@RT{ qjf(t)dt} and E (K×p)
(cid:26) q(cid:2) 0 e p(cid:2)
has jth row @=@RT{ qj tf(t)dt}, where di(cid:2)erentiation is with respect to R in f(·) only. In ad-
qj−1 e e
dition, F is symmetric with (i;j) upper-triangular element (i=K)(1−j=K); F(i;j)=p (1−i=K);
qq qp j
i¿j; =−p (i=K);i¡j(K −1×K); F (K×K) is symmetric with F(j;j)=p (1−p );F(i;j)=
j pp pp j j pp
−pp ; and F (K×p) has jth row E{I(e∈Q )eT}, where the expectation is with respect to
i j p(cid:2) (cid:26) j (cid:2) (cid:26)
the distribution of X. De(cid:1)ning h =p−1 qj E(Y |t)tf(t)dt and h =(1=K−p )−1 qj E(Y |t)
1j j qj−1 1 e 0j j qj−1 0
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

ESTIMATION OF CAUSAL TREATMENT EFFECTS 2959
(1 − t)f(t)dt; j=1;:::;K, and g =E(Y |q )q (p−1 − p−1) and g =E(Y |q )(1 − q )
e 1j 1 j j j j+1 0j 0 j j
{(1=K−p )−1−(1=K−p )−1}; j=1;:::;K−1, then A =(E E E ); BT =(FT FT
j j+1 21 (cid:3)q (cid:3)p (cid:3)(cid:2) 12 q(cid:3) p(cid:3)
FT )T, where E (1×K) has jth element (p K)−1h −(1−K )−1h , respectively; E (1×
(cid:2)(cid:3) (cid:3)p j 1j pj 0j (cid:3)q
K −1) has elements K−1(g −g )f(q ); and E (1×p) is given by
1j 0j e j (cid:3)(cid:2)
(cid:14) (cid:11) (cid:12)(cid:16)
(cid:18) (cid:18)
(cid:1)K qj qj
@=@RT (p K)−1 E(Y |t)tf(t)dt−(K−1−p )−1 E(Y |t)(1−t)f(t)dt
j 1 e j 0 e
j=1 qj−1 qj−1
where di(cid:2)erentiation is with respect to R in f(·). Similarly, FT (1×K) has jth element
e (cid:1) p(cid:3)
K−1h −p (cid:3)∗; FT (1×K −1) has elements K−1 j (h −h −(cid:3)∗); and FT (1×p) is
(cid:1)1j j q(cid:3) i=1 1i 0i (cid:2)(cid:3)
K−1 K [p−1E{Y I(e∈Q )eT}+(1=K −p )−1E{Y I(e∈Q )eT}].
j=1 j 1 j (cid:2) j 0 j (cid:2)
Substituting these expressions in (36) and simplifying yields (27), with (cid:2) =E F +
p (cid:3)p p(cid:3)
FT ET +E F ET ;(cid:2) =−H (E FT +FT )T−(E FT +FT )HT +H F HT , and
p(cid:3) (cid:3)p (cid:3)p pp (cid:3)p qp (cid:3)q (cid:3)p qp q(cid:3) (cid:3)p qp q(cid:3) (cid:3)q (cid:3)q qq (cid:3)q
(cid:2) =(H −H E )E−1(FT +E FT )T+(FT +E FT )E−1(H −H E )T+(H −
(cid:2)qp (cid:3)(cid:2) (cid:3)q q(cid:2) (cid:2)(cid:2) (cid:2)(cid:3) (cid:3)p (cid:2)p (cid:2)(cid:3) (cid:3)p (cid:2)p (cid:2)(cid:2) (cid:3)(cid:2) (cid:3)q q(cid:2) (cid:3)(cid:2)
H E )E−1(H −H E )T, where H =(E +E E )E−1 and H =E +E E .
(cid:3)q q(cid:2) (cid:2)(cid:2) (cid:3)(cid:2) (cid:3)q q(cid:2) (cid:3)q (cid:3)q (cid:3)p pq qq (cid:3)(cid:2) (cid:3)(cid:2) (cid:3)p p(cid:2)
To obtain the second term in (34), let E (1×q) equal
(cid:3)(cid:7)
(cid:14) (cid:11) (cid:12)(cid:16)
(cid:18) (cid:18)
(cid:1)K qj qj
@=@ST (p K)−1 E(Y |t)tf(t)dt−(K−1−p )−1 E(Y |t)(1−t)f(t)dt
j 1 e j 0 e
j=1 qj−1 qj−1
(cid:27)(cid:26) (cid:28) (cid:29) (cid:26) (cid:30)
Let E (K−1×q) and E (K×q) have jth rows @=@ST qfj (t)dt and @=@ST qj tf(t)dt ,
q(cid:7) p(cid:7) 0 e qj−1 e
respectively. Also let F (K×q) be the matrix with jth row E{I(e∈Q )eT}, and FT (1×p)
(cid:1) p(cid:7) j (cid:7) (cid:7)(cid:3)
is K−1 K [p−1E{Y I(e∈Q )eT}+(1=K −p )−1E{Y I(e∈Q )eT}]. De(cid:1)ning H =E −
j=1 j 1 j (cid:7) j 0 j (cid:7) (cid:3)(cid:7) (cid:3)(cid:7)
E E , D =H −H E−1ET −H (E −E E−1ET ), and G =(F −E E−1F )T+
(cid:3)p p(cid:7) (cid:7) (cid:3)(cid:7) (cid:3)(cid:2) (cid:2)(cid:2) (cid:7)(cid:2) (cid:3)q q(cid:7) q(cid:2) (cid:2)(cid:2) (cid:7)(cid:2) (cid:7) (cid:7)(cid:3) (cid:7)(cid:2) (cid:2)(cid:2) (cid:2)(cid:3)
E (FT −E E−1E )T, one can show that (cid:9) =D H−1GT+G H−1DT+D H−1DT.
(cid:3)p p(cid:7) (cid:7)(cid:2) (cid:2)(cid:2) (cid:2)p (cid:7)(cid:2)qp (cid:7) (cid:7)(cid:2) (cid:7) (cid:7) (cid:7)(cid:2) (cid:7) (cid:7) (cid:7)(cid:2) (cid:7)
REFERENCES
1.Rosenbaum PR, Rubin DB. The central role of the propensity score in observational studies for causal e(cid:2)ects.
Biometrika 1983; 70:41–55.
2.D’Agostino RB. Tutorial in biostatistics: propensity score methods for bias reduction in the comparison of a
treatment to a non-randomized control group. Statistics in Medicine 1998; 17:2265–2281.
3.Rosenbaum PR. Propensity score. In Encyclopedia of Biostatistics, Armitage P, Colton T (eds), vol. 5. Wiley:
New York, 1998; 3551–3555.
4.ShepardsonLB,YoungnerSJ,Spero(cid:2)T,RosenthalGE.Increasedriskofdeathinpatientswithdo-not-resuscitate
orders. Medical Care 1999; 37:727–737.
5.Perkins SM, Tu W, Underhill MG, Zhou XH, Murray MD. The use of propensity scores in
pharmacoepidemiologic research. Pharmacoepidemiology and Drug Safety 2000; 9:93–101.
6.Allen-Ramey FC, Duong PT, Goodman DC, Sajjan SG, Nelsen LM, Santanello NC, Markson LE. Treatment
e(cid:2)ectiveness of inhaled corticosteroids and leukotriene modi(cid:1)ers for patients with asthma: an analysis from
managed care data. Allergy and Asthma Proceedings 2003; 24:43–51.
7.Rosenbaum PR, Rubin DB. Reducing bias in observational studies using subclassi(cid:1)cation on the propensity
score. Journal of the American Statistical Association 1984; 79:516–524.
8.Rosenbaum PR. Model-based direct adjustment. Journal of the American Statistical Association 1987; 82:
387–394.
9.Robins JM, Herna(cid:10)n M, Brumback B. Marginal structural models and causal inference in epidemiology.
Epidemiology 2000; 11:550–560.
10.Rubin DR. Estimating causal e(cid:2)ects of treatments in randomized and nonrandomized studies. Journal of
Educational Psychology 1974; 66:688–701.
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960

2960 J. K. LUNCEFORD AND M. DAVIDIAN
11.Polsky D, Mandelblatt JS, Weeks JC, Venditti L, Hwang Y, Glick HA, Hadley J, Schulman KA. Economic
evaluation of breast cancer treatment: considering the value of patient choice. Journal of Clinical Oncology
2003; 21:1139–1146.
12.Horvitz DG, Thompson DJ. A generalization of sampling without replacement from a (cid:1)nite universe. Journal
of the American Statistical Association 1952; 47:663–685.
13.Robins JM, Rotnitzky A, Zhao LP. Estimation of regression coe(cid:4)cients when some regressors are not always
observed. Journal of the American Statistical Association 1994; 89:846–866.
14.Robins JM. Robust estimation in sequentially ignorable missing data and causal inference models. Proceedings
of the American Statistical Association Section on Bayesian Statistical Science 1999; 6–10.
15.ScharfsteinDO,RotnitzkyA,RobinsJM.RejoindertoAdjustingfornonignorabledrop-outusingsemiparametric
nonresponse models. Journal of the American Statistical Association 1999; 94:1135–1146.
16.Hirano K, Imbens GW. Estimation of causal e(cid:2)ects using propensity score weighting: an application to data on
right heart catheterization. Health Services and Outcomes Research Methodology 2001; 2:259–278.
17.Rubin DR. Estimating causal e(cid:2)ects from large data sets using propensity scores. Annals of Internal Medicine
1997; 127:757–763.
18.Stefanski LA, Boos DD. The calculus of M-estimation. The American Statistician 2002; 56:29–38.
19.McIntosh MW, Rubin DB. On estimating the causal e(cid:2)ects of DNR orders. Medical Care 1999; 37:722–726.
20.Dawid AP. Conditional independence in statistical theory. Journal of the Royal Statistical Society, Series B
1979; 41:1–31.
21.Lunceford JK. Estimating causal treatment e(cid:2)ects via the propensity score and estimating survival distributions
in clinical trials that follow two-stage randomization designs. Unpublished Ph.D. dissertation, North Carolina
State University, 2001; available at http://www.lib.ncsu.edu/.
22.Carroll RJ, Ruppert D, Stefanski LA. Measurement Error in Nonlinear Models. Chapman & Hall, London;
1995.
Copyright ? 2004 John Wiley & Sons, Ltd. Statist. Med. 2004; 23:2937–2960