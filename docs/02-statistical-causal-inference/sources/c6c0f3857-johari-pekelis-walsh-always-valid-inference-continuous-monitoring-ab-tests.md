| Always |     | Valid |     | Inference: |     |        | Continuous |     | Monitoring | of  |
| ------ | --- | ----- | --- | ---------- | --- | ------ | ---------- | --- | ---------- | --- |
|        |     |       |     |            |     | A/B    | Tests      |     |            |     |
|        |     |       |     |            |     | Ramesh | Johari*    |     |            |     |
DepartmentofManagementScienceandEngineering,StanfordUniversity,rjohari@stanford.edu
|     |     |     |     |     |     | Leo | Pekelis† |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
OpenDoor,Inc,lpekelis@gmail.com
9102 luJ 61  ]TS.htam[  3v22940.2151:viXra
|     |     |     |     |     |     | David | Walsh‡ |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- |
DepartmentofStatistics,StanfordUniversity,dwalsh@stanford.edu
A/B tests are typically analyzed via frequentist p-values and confidence intervals; but these inferences are
wholly unreliable if users endogenously choose samples sizes by continuously monitoring their tests. We
define always valid p-values and confidence intervals that let users try to take advantage of data as fast as
it becomes available, providing valid statistical inference whenever they make their decision. Always valid
inferencecanbeinterpretedasanaturalinterfaceforasequentialhypothesistest,whichempowersusersto
implementamodifiedtesttailoredtothem.Inparticular,weshowinanappropriatesensethatthemeasures
wedeveloptradeoffsamplesizeandpowerefficiently,despitealackofpriorknowledgeoftheuser’srelative
preference between these two goals. We also use always valid p-values to obtain multiple hypothesis testing
control in the sequential context. Our methodology has been implemented in a large scale commercial A/B
| testing | platform | to  | analyze | hundreds | of thousands |     | of experiments | to  | date. |     |
| ------- | -------- | --- | ------- | -------- | ------------ | --- | -------------- | --- | ----- | --- |
1. Introduction
This paper reports on novel statistical methodology underlying the implementation of a large-
scale commercial experimentation platform for web applications and services.1 Web applications
typically optimize their product offerings using randomized controlled trials (RCTs); in industry
parlance this is known as A/B testing. The rapid rise of A/B testing has led to the emergence of
a number of widely used platforms that handle the implementation of these experiments (Kohavi
| et al. 2013, | Tang | et  | al. 2010). |     |     |     |     |     |     |     |
| ------------ | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
∗
| RJ was   | a technical  | advisor | to          | Optimizely, | Inc., | when      | this work   | was carried | out. |     |
| -------- | ------------ | ------- | ----------- | ----------- | ----- | --------- | ----------- | ----------- | ---- | --- |
| † LP was | employed     | by      | Optimizely, | Inc.,       | when  | this work | was carried | out.        |      |     |
| ‡ DJW    | was employed | by      | Optimizely, | Inc.,       | when  | this work | was carried | out.        |      |     |
1

Johari, Pekelis, and Walsh: AlwaysValidInference
2
Figure 1 A typical dashboard from a large commercial A/B testing platform service. The graph depicts the
“chance to beat baseline” of a test, which measures 1−p over time, where p is the p-value after n
n n
observationsofthenullhypothesisthattheclickthroughrateintreatmentandcontrolisidentical.This
particulartestisaA/Atest:boththetreatmentandcontrolarethesame.Thegraphshowsthat1−p
n
rises above the 95% significance threshold if the user continuously monitors the test, triggering a Type
I error.
AstandardA/Btestwithtwovariations(controlandtreatment)involvestestingthenull hypoth-
esis that both groups share the same parameter (e.g., customer conversion rate from clicking on
a link to a sale) against the alternative hypothesis that they are different. The A/B testing plat-
form communicates experimental results to the user via frequentist parameter testing measures,
i.e., p-values and confidence intervals. Besides well known properties of their optimality (see, e.g.,
Lehmann et al. 1986), these measures imply an exceptionally simple “user interface”; the user
implementsamechanisticrule(thresholdthep-valueattheirdesiredTypeIerrorrateα)thatdoes
not require further knowledge of experiment details. This has two valuable consequences, under-
pinning their ubiquity in industrial practice: first, the same interface can be employed by many
users, each with their own α; and second, experimental results can be analyzed by users without
advanced statistical training.
These desirable outcomes only obtain, however, when p-values and confidence intervals are used
as intended. In A/B testing practice, users are not constrained to simply analyze the output of
an experiment; they can also adjust the experimental design in response to the data observed.

Johari, Pekelis, and Walsh: AlwaysValidInference
3
This type of behavior can entirely undermine statistical reliability. A particularly pervasive form
of this behavior is commonplace: users continuously monitor the p-values and confidence intervals
reportedinordertosetthesamplesizeofanexperimentdynamically(Miller2010).Figure1shows
how a typical dashboard enables such behavior.
The incentive to continuously monitor experiments is strong because the opportunity cost of
longer experiments is large. There is value to detecting true effects as quickly as possible, or giving
upifitappearsthatnoeffectwillbedetectedsoonsothattheymaytestsomethingelse.Mostusers
further lack good prior understanding of their cost elasticity as well as the effect size they seek,
frustrating attempts to optimize run-time in advance. Indeed, the ability to trade off maximum
detection with minimum run-time dynamically is a crucial benefit of the availability of real-time
data in modern A/B testing environments.
No correction for continuous monitoring is typically made in industrial practice. Consequently,
the resulting feedback loop between the statistical output and the experimental design undermines
inferential validity, as computations are performed under the naive assumption of their indepen-
dence. Very high false positive probabilities are obtained—well in excess of the nominal α that the
user can tolerate. Even with 10,000 samples (a sample size which is quite common in online A/B
testing), Type I error can easily increase fivefold.
Our challenge is the following: can we deliver efficient inference in a simple interface, but in an
environment where users continuously monitor experiments, and where their priorities regarding
run-time and detection are not known in advance? We develop a statistical approach that addresses
this challenge, and report on an implementation in a commercial A/B testing platform. A key to
our framework is that we employ the same interface as a traditional A/B testing platform: we
present the user with p-values and confidence intervals. However, our measures have the following
properties.First,TypeIerroriscontrolledunderanydata-dependentruletheusermightchooseto
stop the experiment (i.e., any stopping time for the data). Continuous monitoring does not inflate
Type I error. Second, in a sense we make precise below, we show that if the user stops when our

Johari, Pekelis, and Walsh: AlwaysValidInference
4
p-value drops below her personal α, the resulting rule approximately obtains an efficient trade-off
for run-time and detection, even with no advance knowledge of her preferences.
In more detail, our contributions are as follows.
1. Type I error control: Always valid p-values and confidence intervals. Our first contribution is
to develop p-values that control Type I error in a strong sense. In particular, we ask: what
p-value processes control Type I error at any data-dependent stopping time the user might
choose? We refer to such p-values as always valid p-values (and analogously, always valid
confidence intervals). We show how these always valid p-value processes can be constructed
using sequential hypothesis tests (Wald 1945, Siegmund 1985, Lai 2001, Siegmund 1978); in
particular, we identify a duality between always valid p-values and those sequential tests that
donotacceptH infinitetime,knownassequential tests of power one(RobbinsandSiegmund
0
1974). Under this duality, the natural policy of stopping the first time that the always p-value
process crosses the level α implements the corresponding sequential test of power one. In this
wayweretainthesimple“userinterface”ofp-values,butguaranteeTypeIerrorcontrolunder
continuous monitoring.
2. Efficientlytradingoffpowerandrun-time:Themixturesequentialprobabilityratiotest.Having
controlled Type I error, we then ask: how can we efficiently trade off power and run-time? The
challenge for an A/B testing platform, as noted above, is that users’ objective functions—and
in particular, their relative prioritization of run-time and detection—are not typically known
in advance. We aim to find always valid p-value processes that lead to an efficient tradeoff for
the user.
It is evident that without restricting the class of user models we consider, no meaningful
result is possible; the space of potential user preferences over run-time and detection is vast
(and some are unreasonable, e.g., preferring long experiments that do not detect effects).
Instead, we focus on users that generally want short tests and good detection, modeled as
follows: the user stops at either the first time the p-value process crosses α, or at a fixed

Johari, Pekelis, and Walsh: AlwaysValidInference
5
maximum failure time M, whichever comes first. A larger M indicates greater patience, and
a corresponding preference for detection of smaller effects. While this class does not capture
all possible objective functions, it does allow us to capture what we consider to be the most
interesting axis of user heterogeneity: how much they care about power versus how much they
care about run-time.
Ourmaincontributionistodemonstratethatalwaysvalidp-valuesderivedfromaparticular
classofsequentialtestsknownasmixture sequential probability ratio tests(mSPRTs)(Robbins
1970) achieve an efficient tradeoff between power and run-time for such users to first order in
M as M →∞. We achieve this result for settings where the data is generated from a single-
parameter exponential family. This result provides evidence that the mSPRT can produce
always valid p-values that yield valuable inference for most users, albeit in the limit where M
is very large. We therefore complement our theory with empirical analysis that compares the
mSPRT to other sequential tests at finite values of M. These empirical results demonstrate
that the mSPRT delivers high performance in the regime relevant for practical application.
ThemSPRTinvolvesstoppingthefirsttimeamixtureofthelikelihoodratioofalternativeto
nullcrossesathreshold,wherethemixtureisoverpotentialvaluesofthealternative.Although
first order efficiency as M →∞ holds for any mixing distribution, the mixing distribution
plays an important role in second order performance. In particular, as power approaches one
when M →∞ for mSPRTs, we choose among this class by optimizing the mixing distribution
to minimize run-time. Formally, in a Bayesian setting (where effect sizes are drawn from a
prior), we find a particular choice of mSPRT that minimizes expected run-time in the limit
where M →∞. The run-time minimizing choice of mSPRT has an appealingly simple form:
e.g.,whenthereisaGaussianprioroneffectsizes,theoptimalmSPRTapproximatelymatches
the variance of the mixing distribution to the variance of the prior distribution of effect sizes.
We also complement this theoretical investigation with numerics to study the sensitivity of
performance to the choice of mixing distribution at finite values of M. We find that although

Johari, Pekelis, and Walsh: AlwaysValidInference
6
the mixing distribution can have a significant impact on performance, there is also robustness,
in that a well-chosen mixing distribution can deliver good performance in a wide-range of
conditions.
3. Implementation in a commercial A/B testing platform. As noted above, a key contribution of
our work is the deployment of our methods in a commercial A/B testing platform, used by
thousandsofcustomersworldwide.Themaintechnicalchallengeinimplementationisthatour
resultsaboveonoptimalityofthemSPRTarederivedinasingle-streamsetting,whereasingle
unknown parameter of a data-generating process is being tested; by contrast, in A/B testing,
since there are two variations (control and treatment), we are in a two-stream setting. We
extend our work to this setting, essentially by treating additional parameters besides the true
treatment effect as nuisance parameters; this is the method that is deployed in the platform.
We also report both empirically and theoretically on a comparison of our methodology with
classical fixed horizon testing. We find that our approach can deliver equivalent power as fixed
horizon testing, with a sublinear sample size, suggesting that even statistically savvy users
would receive results faster using our approach in practice.
We note further that in a companion conference paper, we provide greater detail on the
implementation of our work in the large commercial A/B testing platform described above;
the reader is referred to Johari et al. (2017).
4. Multiple hypothesis testing. Finally, we note that a major practical advantage of always valid
p-values is that we can employ them within existing methodology that uses these measures
as inputs to provide error guarantees in multiple hypothesis testing, despite the sequential
nature of A/B testing. In particular, we can control the family-wise error rate (FWER), as
wellasthefalse discovery rate(FDR)inthesequentialsettingundersomeassumptionsonthe
user’s stopping time. We also study false coverage rate (FCR) control for confidence intervals.
This combination of sequential testing and multiple hypothesis testing corrections is novel
to our work, and enabled because of the introduction of always valid p-values. The resulting

| Johari, Pekelis, |     | and Walsh: | AlwaysValidInference |     |
| ---------------- | --- | ---------- | -------------------- | --- |
7
FDR- and FCR-controlling procedures have also been implemented in the commercial service
| described |     | above, | as part of | the same deployment. |
| --------- | --- | ------ | ---------- | -------------------- |
Taken together, we preserve the benefits of p-values and confidence intervals, while modernizing
their computation to account for continuous monitoring as well as multiple hypothesis testing.
The remainder of the paper is organized as follows. In Section 2, we present related literature.
In Section 3, we describe our basic model and notation. In Section 4, we introduce always valid
p-values and confidence intervals. In Section 5, we study the design of efficient always valid p-value
processes via the use of the mSPRT, both theoretically and empirically. In Section 6, we discuss
details of deployment and implementation, and particularly the adaptation of our basic theory to
two streams of data. In Section 7, we discuss multiple hypothesis testing. Finally, we conclude in
Section 8.
| 2. Related      |     | work       |         |     |
| --------------- | --- | ---------- | ------- | --- |
| 2.1. Sequential |     | hypothesis | testing |     |
Thedesiretotesthypothesesusingdatathatarrivessequentiallyovertimeisfarfromnew.Rather,
sequential analysisisa maturefield withrootsdatingbacktoWald(1945), andsequential testsare
widely used in areas such as pharmaceutical clinical trials. For its history, methodology and theory,
we direct the reader to the encyclopedic resource of Ghosh and Sen (1991); see also Siegmund
| (1985) | for an | introduction | to the | topic. |
| ------ | ------ | ------------ | ------ | ------ |
In fact, there has been recent interest in implementing existing sequential tests in online experi-
mentation (Miller 2015). However, adoption has been limited, because the tests function as “black
boxes” until the single stopping time when the null hypothesis is accepted or rejected. Inference at
general stopping times is not attainable. Thus an off-the-shelf sequential test can provide value for
a single experimenter only if the test is specifically optimized to her preferences over power and
run-time. On the other hand, by using sequential tests as building blocks to construct always valid
p-values and confidence intervals, this paper obtains a real-time interface that can better handle
| users with | heterogeneous |     | preferences. |     |
| ---------- | ------------- | --- | ------------ | --- |

Johari, Pekelis, and Walsh: AlwaysValidInference
8
2.2. Sequential confidence intervals and the LIL
Our always valid confidence intervals are not the first attempt to construct sequences of intervals
whichcontainanunknownparameterwithuniformlyhighprobabilityoveraninfinitetime-horizon.
While our always valid measures emerge from a hypothesis testing framework, such intervals may
derived by appealing directly to the Law of the Iterated Logarithm (LIL), which governs the
asymptotic behavior of large deviations in sample averages. This approach dates back to Dar-
ling and Robbins (1967) and Robbins (1970), where the constructed intervals are referred to as
“confidence sequences”. Since then, LIL-type bounds have been obtained for broader classes of
(suitably normalized) martingales; for a comprehensive summary, we defer to de la Pen˜a et al.
(2008). Further, work such as Balsubramani (2014) has tightened the LIL at finite samples, while
Zhao et al. (2016) extends various classical concentration inequalities to hold at data-dependent
stopping times. Independent of our work in this paper, related work has leveraged these LIL-type
bounds for the construction of always valid confidence intervals for a range of parametric and
non-parametric settings (Balsubramani and Ramdas 2015, Howard et al. 2018).
In Section 5.6.3, we compare the empirical performance of our always valid measures derived
from the mSPRT against these LIL-based intervals as vehicles for trading off power against run-
time. We note that the LIL provides intervals whose size shrinks at a faster asymptotic rate than
the mSPRT, and so offers better inference for users who are willing to wait until power very close
to one is achieved. For most users, however, our empirical investigation suggests the stronger finite
sample performance of the mSPRT would result in a more efficient trade-off. For this reason, we
consider it the most appropriate choice for an A/B testing platform.
2.3. Bandit algorithms
While the work described in this paper largely addresses A/B testing carried out using the toolkit
of statistical inference (i.e., hypothesis testing), it is worth noting that A/B testing is often used
to find the best alternative. For example, a marketing team may be interested in testing two
designs for the same web page, with the only goal to maximize conversion rate. The latter type of

Johari, Pekelis, and Walsh: AlwaysValidInference
9
problem has been extensively studied in the literature on multi-armed bandits (Bubeck et al. 2012,
Lattimore and Szepesv´ari 2018). This has led to some use of bandit algorithms in industry in place
of hypothesis testing (Scott 2015).
Twovariantsofthebanditproblemformulationarerelevant:thepure explorationproblem(when
the rewards during the experiment are ignored) (Bubeck et al. 2009), and the more widely studied
regret minimization problem where the rewards earned during experimentation are also optimized
as part of the objective function. The pure exploration problem is more relevant to the industrial
experimentation scenarios that inspired this paper, as in these situations the experimentation
period is relatively short compared to the lifespan of any “winning” feature that is deployed.
Therefore the rewards earned during experimentation itself can be safely ignored. In solving the
pure exploration problem, the allocation of treatments to incoming traffic is modified dynamically,
in order to provide a decision at some minimal stopping time on which treatment is the best.
We note here that much of the interest in sequential confidence intervals has arisen in connection
with the literature on pure-exploration bandits, where the target error bounds are of a different
flavor than the Type I error rate control sought in this paper. While we seek to control the
probability of falsely detecting any treatment effect when no such effect exists, the typical focus in
that literature is on probably almost correct (PAC) bounds (Even-Dar et al. 2002, Kalyanakrishnan
et al. 2012). There it is only necessary to identify the winning treatment with high probability
in the case that a treatment effect exists and exceeds some pre-specified threshold. For instance,
Kaufmann et al. (2014) uses such a formulation to characterize the complexity of pure-exploration
problems. Jamieson et al. (2014) and Abbasi-Yadkori et al. (2011) each present bandit algorithms,
which improve regret by leveraging sequential confidence intervals that are always valid in the
PAC sense. PAC-style bounds are typically not sufficient for an A/B testing platform, because the
threshold on treatment effects sought cannot be tailored to the heterogeneous users.
Finally,inlightofthisdiscussiononbandits,itisworthnotingwhyourownworkemphasizesthe
hypothesis testing viewpoint as opposed to a pure-exploration multi-armed bandit approach. The

Johari, Pekelis, and Walsh: AlwaysValidInference
10
main point we make here is that at the same time as the best alternative is sought prospectively,
there is also a post-experiment interest in inference; in particular, the experimenter often wants
a confidence interval on the effect size of a variation that does not win. Part of the reason is
operational: if the gain of a winning variation is insufficient over the status quo, the deployment
cost may not be worthwhile. Such confidence intervals are also strategically important, as they
provide guidance on what types of experiments may be worth trying in the future. Our observation
is that the hypothesis testing framework remains the dominant form of A/B testing in industrial
deployment, at least partly for such reasons, and for this reason we have focused our attention on
this setting. However, bandit methods are also practically valuable, and developing methods for
inference with adaptive allocation remain interesting directions for future work. We return to this
point in our conclusion, Section 8.
2.4. Sequential multiple hypothesis testing
There has also been recent interest in achieving multiple hypothesis testing controls in sequential
contexts. For the most part, work in this area considers a different form of streaming data to
the one described in this paper: Demets and Lan (1994), Foster and Stine (2008) and Javanmard
and Montanari (2016) provide so-called “α-spending” and “α-investing” methods to control the
family-wise error rate (FWER) or the false discovery rate (FDR) when experiments are performed
sequentially, but within each experiment the data is accessed only once.
However, recent work has started to address the within-experiment data arrival process that
characterizes A/B testing. Yang et al. (2017) combines α-investing with sequential hypothesis test-
ing to enable FDR control in this regime. Jamieson and Jain (2018) goes a step further, allocating
traffic to treatments dynamically with the goal of achieving statistical significance quickly, while
still bounding FDR. Malek et al. (2017) investigates when always valid p-values can be used to
achieve other multiple testing bounds beyond FWER and FDR.

Johari, Pekelis, and Walsh: AlwaysValidInference
11
3. Preliminaries
To begin, we suppose that our data can be modeled as independent observations from an expo-
nential family X=(X )∞ i ∼ idF , where the parameter θ takes values in Θ⊂Rp. Throughout the
n n=1 θ
paper, (F )∞ will denote the filtration generated by (X )∞ and P will denote the measure
n n=1 n n=1 θ
(on any space) induced under the parameter θ. Our focus is on testing a simple null hypothesis
H :θ=θ against the composite alternative H :θ(cid:54)=θ . (In Section 6 we adapt our analysis to
0 0 1 0
two-sample hypothesis testing, as is needed to test differences between control and treatment in
an A/B test.)
Decision rules. In general, a decision rule is a pair (T,δ), where T is a (possibly infinite)
stopping time for (F )∞ that denotes the sample size at which the test is ended, and δ is a
n n=1
binary-valued, (F )-measurable random variable, where δ=1 indicates that H is rejected; note
T 0
that δ=0 must hold a.s. if T =∞. Note that we allow the possibility that the decision rule can
be data-dependent; when T is not data-dependent, we refer to the rule as a fixed horizon decision
rule.
Type I error. Type I error is the probability of erroneous rejection under the null, i.e., P (δ=
θ0
1). We assume that the user wants to bound Type I error at level α∈(0,1).
Sequential tests. Given α, we typically consider a family of decision rules parameterized by α.
Formally, a sequential test is a family of decision rules (T(α),δ(α)) indexed by α∈(0,1) such that:
1. The decision rules are nested: T(α) is a.s. nonincreasing in α, and δ(α) is a.s. nondecreasing
in α.
2. For each α, the Type I error is bounded by α: P (δ=1)≤α.
θ0
Note that sequential tests allow the possibility that the decision rules are data-dependent, though
strictly speaking fixed horizon decision rules are allowed in this definition as well.
Fixed horizon testing.Underthedefaultfixedhorizontestingapproach,werestricttodecision
rules (n,δ), where the stopping time is required to be deterministic. In this setting, the objective
is to maximize the power (the probability of detection under H ) at that n. Indeed, for data in an
1

Johari, Pekelis, and Walsh: AlwaysValidInference
12
exponential family, for any given n, there exist a family of uniformly most powerful (UMP) tests
parameterized by α, each of which maximizes power uniformly over θ among tests with Type I
error rate α. These tests reject the null if a particular test statistic τ exceeds a threshold k(α)
n
| (see, e.g., | Chapter | 4 of Lehmann | et al. 1986). |     |     |     |
| ----------- | ------- | ------------ | ------------- | --- | --- | --- |
While the tests maximize power for the given n, the power increases as n is increased, and so the
user must choose n to trade off power against the opportunity cost of waiting for more samples.
The challenge for the user is that the power is a steep function of the true θ, so good advance
| knowledge | on the size | of the effect | sought is | required. |     |     |
| --------- | ----------- | ------------- | --------- | --------- | --- | --- |
The fixed horizon user interaction model. Testing platforms typically allow users to imple-
ment their optimal test via p-values. Specifically, the p-value at time n corresponding to the UMP
test is:
|     |     |     | p =inf{α:τ | ≥k(α)}. |     |     |
| --- | --- | --- | ---------- | ------- | --- | --- |
|     |     |     | n          | n       |     |     |
In other words, this p-value is the smallest α such that the α-level test with sample size n rejects
H .
0
The process p provides sufficient information for the user to implement her desired test with
n
ease: she waits for her chosen n, and rejects the null hypothesis if p ≤α. In addition, p ensures
|     |     |     |     |     | n n |     |
| --- | --- | --- | --- | --- | --- | --- |
transparencyinthefollowingsense:sinceeachruleδ (α)controlsTypeIerroratlevelα,anyother
n
user can threshold the p-value obtained at her own appropriate α˜ level to satisfy her desired Type
I error bound.
In fact, to control Type I error, we require only that the p-value is super-uniform:
|     |     |     | ∀s∈[0,1], | P (p ≤s)≤s. |     | (1) |
| --- | --- | --- | --------- | ----------- | --- | --- |
0 n
More generally, we refer to any [0,1]-valued, (F )-measurable random variable p that satisfies (1)
n n
| as a fixed | horizon p-value | process | for the choice | of sample size | n.  |     |
| ---------- | --------------- | ------- | -------------- | -------------- | --- | --- |
Confidence intervals can be constructed from the tests δ (α) associated with fixed horizon p-
n
|     | :θ=θ˜at | θ˜∈Θ |     |     |     |     |
| --- | ------- | ---- | --- | --- | --- | --- |
values for H each by considering the set of θ that are not rejected. What matters
0

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- | --- |
13
is the following coverage bound: a (1 − α)-level fixed horizon confidence interval is any (F )-
n
| measurable | random | set CI ⊂Θ | where |     |     |     |
| ---------- | ------ | --------- | ----- | --- | --- | --- |
n
P
|     |     |     | ∀θ∈Θ, | (θ∈CI | )≥1−α. | (2) |
| --- | --- | --- | ----- | ----- | ------ | --- |
θ n
| 4. Always | valid | inference |     |     |     |     |
| --------- | ----- | --------- | --- | --- | --- | --- |
Our goal is to let the user stop the test whenever they want, in order to trade off power with
run-time as they see fit; the p-value they obtain should control Type I error. Our first contribution
is the definition of always valid p-values as those processes that achieve this control.
Definition 1. A sequence of fixed horizon p-values (p ) is an always valid p-value process if given
n
any (possibly infinite) stopping time T with respect to (F ), there holds:
n
|     |     |     | ∀s∈[0,1], | P (p | ≤s)≤s. | (3) |
| --- | --- | --- | --------- | ---- | ------ | --- |
θ0 T
The following theorem demonstrates that always valid p-values are in a natural correspondence
| with sequential | tests. |             |                 |       |      |     |
| --------------- | ------ | ----------- | --------------- | ----- | ---- | --- |
| Theorem         | 1.     |             |                 |       |      |     |
|                 | 1. Let | (T(α),δ(α)) | be a sequential | test. | Then |     |
p =inf{α:T(α)≤n,δ(α)=1}
n
| defines | an always | valid p-value | process. |     |     |     |
| ------- | --------- | ------------- | -------- | --- | --- | --- |
2. For any always valid p-value process (p )∞ , a sequential test (T˜(α),δ˜(α)) is obtained from
n n=1
| (p  | )∞ as follows: |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
n
n=1
|     |     |     | T˜(α)=inf{n:p |     | ≤α}; | (4) |
| --- | --- | --- | ------------- | --- | ---- | --- |
n
δ˜(α)=1{T˜(α)<∞}.
(5)
(T˜(α),δ˜(α))
If (p )∞ was derived as in part (1) and T = ∞ whenever δ = 0, then =
n n=1
(T(α),δ(α)).

|     |     |     |     | Johari, | Pekelis, and Walsh: AlwaysValidInference |
| --- | --- | --- | --- | ------- | ---------------------------------------- |
14
Proof of Theorem 1. For the first result, nestedness implies the following identity for any s∈
[0,1],n≥1,ε>0:
|     | {p  | ≤s}⊂{T(s+ε)≤n,δ(s+ε)=1}⊂{δ(s+ε)=1}. |     |     |     |
| --- | --- | ----------------------------------- | --- | --- | --- |
n
Therefore:
|     | P (p | ≤s)≤P | (∪ {p ≤s})≤P | (δ(s+ε)=1)≤s+ε. |     |
| --- | ---- | ----- | ------------ | --------------- | --- |
|     | θ0   | T     | θ0 n n       | θ0              |     |
The result follows on letting ε→0. For the converse, it is immediate from the definition that the
| tests are nested | and δ(α)=0   | whenever | T(α)=∞.    | For any ε>0 |           |
| ---------------- | ------------ | -------- | ---------- | ----------- | --------- |
|                  | P (δ(α)=1)=P |          | (T(α)<∞)≤P | (p          | ≤α+ε)≤α+ε |
|                  | θ0           |          | θ0         | θ0 T(α)     |           |
where the last inequality follows from the definition of always validity. Again the result follows on
letting ε→0. (cid:50)
The p-value defined in part (1) of the theorem is not the unique always valid p-value associated
with that family of sequential tests (i.e., for which part (2) holds). However, among such always
valid p-values it is a.s. minimal at every n, resulting from the fact that it is a.s. monotonically
non-increasing in n. Thus we have a one-to-one correspondence between monotone always valid
p-value processes and families of sequential tests that do not give up for failure; i.e., where δ=0
implies T =∞. These processes can be seen as the natural representation of those sequential tests
| in a streaming | p-value format. |     |     |     |     |
| -------------- | --------------- | --- | --- | --- | --- |
T˜(α)
The new user interaction model. The time represents the natural stopping time of a
hypothetical user who incurs no opportunity cost from longer experiments. By thresholding the
p-value at α at that time, she recovers the underlying sequential test and is able to reject H
0
whenever δ=0. Of course, a real user cannot wait forever, so she must stop the test and threshold
the p-value at some potentially earlier, a.s. finite stopping time. In so doing, she sacrifices some
detectionpower.Thistrade-offfortheuserbetweenpowerandaveragerun-timeisacentralconcern
| of our proposed | design, and | is studied | in more | detail in Section | 5.  |
| --------------- | ----------- | ---------- | ------- | ----------------- | --- |

Johari, Pekelis, and Walsh: AlwaysValidInference
15
Confidence intervals. Always valid CIs are defined analogously and may be constructed from
always valid p-values just as in the fixed horizon context. Proposition 1 follows immediately from
the definitions.
Definition 2. A sequence of fixed-horizon (1−α)-level confidence intervals (CI ) is an always
n
valid (1−α)-level confidence interval process if, given any stopping time T with respect to (F ),
n
there holds:
∀θ∈Θ, P (θ∈CI )≥1−α. (6)
θ T
Proposition 1. Suppose that, for each θ˜∈Θ, (pθ˜) is an always valid p-value process for the test
n
of θ=θ˜. Then
(cid:8) (cid:9)
CI = θ:pθ >α
n n
is an always valid (1−α)-level CI process.
5. Efficient always valid p-values via the mSPRT
As noted in the preceding section, users who continuously monitor experiments are making a
dynamic tradeoff between two objectives: detecting true effects with maximum probability and
minimizingthetypicallengthofexperiments.Asignificantchallengefortheplatformisthatalways
valid p-values must be designed without prior knowledge of the user’s preferences. We are led,
therefore, to consider the following design problem: how should always valid p-values be designed
to lead users to an efficient tradeoff between power and run-length, without access to the user’s
preferences in advance?
Inthissectionwefirstintroduceanaturalmodelofuserbehaviorthatencodesatradeoffbetween
power and run-length, where users are characterized by their Type I error tolerance, α, and the
maximumnumberofobservationsM theycanafford.Weassumethatsuchauserstopsandrejects
H at either the first time the always valid p-value crosses α, or at time M, whichever comes first.
0
Werefertosuchauserasatype (M,α) user.Westudyefficiencyofanalwaysvalidp-valueprocess
via the power profile and relative run-length profile that the process induces for an (M,α) user

Johari, Pekelis, and Walsh: AlwaysValidInference
16
across possible treatment effects; the former gives the probability that true effects are detected by
thisuser,andthelattergivestheexpectedrun-lengthforsuchauser,normalizedbyM.Informally,
our goal is to deliver high power at low relative run-lengths.
To achieve this goal, we consider always valid p-value processes derived from a particular family
of sequential tests, the mixture sequential probability ratio tests (mSPRT). The mSPRT stops the
firsttimeamixture(overtreatmenteffects)oflikelihoodratiosagainstthenullcrossesathreshold.
ThesewerefirstintroducedbyRobbins(1970).ThemSPRTprovidesaneasilyimplementedfamily
of always valid p-value processes, as we discuss further in Section 6. In this section, we focus on
the efficiency properties of the mSPRT, by comparing it to feasible decision rules induced by other
sequential tests.
We begin our study in Section 5.3 by considering first-order efficiency of the mSPRT, in the
limit where α →0. We first note that for users where M is relatively large or relatively small
compared to log(1/α), efficiency (in an appropriate sense) is a relatively weak requirement, and
easily established in particular for the mSPRT. Thus the more interesting analysis is for users
where M ∼log(1/α). For such users, we establish that the mSPRT satisfies a desirable first-order
efficiency property: there is no other feasible decision rule that yields a relative run-length that is
lower on some non-null effects, while meeting the size constraint α and yielding higher power at
all non-null effects.
First-orderefficiencyisimportant,butdoesnottellthecompletestory.Inparticular,thepreced-
ing efficiency result does not depend on the mixing distribution employed by the mSPRT, whereas
we should certainly expect that finite M (or fixed α) performance will be influenced by the choice
of the mixing distribution. In Section 5.4 we theoretically investigate the importance of the choice
of prior. We first theoretically investigate this question by considering a Bayesian setting where
effects are drawn from a prior G. We characterize the expected run-length minimizing mixture
for type (M,α) users where M ∼log(1/α). Specialized to the setting of normal data, we note the
intuitive result that this optimal mixture involves “matching” the prior in an appropriate sense.

Johari, Pekelis, and Walsh: AlwaysValidInference
17
In Section 5.6.1, we carry out an empirical investigation of the role of the choice of mixing distri-
bution for (M,α) users; while we find that the choice of mixture matters, we also find that the
performance of the mSPRT is surprisingly robust to misspecification.
We conclude our analysis by comparing the mSPRT to other decision rules. First, in Section 5.5
we compare the mSPRT to fixed-horizon testing. In particular, we show that for (M,α) users, the
mSPRTprovidesanimprovementoverfixed-horizontestingintheα→0limit,evenwhenthefixed-
horizon test is tailored to prior knowledge. In Section 5.6.2, we complement this theoretical result
with empirical comparison of the mSPRT to fixed-horizon testing, demonstrating the practical
benefits for (M,α) users. Second, we note the mSPRT is only one of many possible choices of
sequential tests in the literature that satisfy desirable optimality criteria. We conclude our study
of efficiency of the mSPRT in Section 5.6.3, where we empirically compare its performance to other
always valid p-value processes derived from sequential tests (including the LIL approach discussed
in Section 2). These empirical results demonstrate that the mSPRT delivers high performance in
the regime of M and α relevant for practical application.
The section is organized as follows. First, we present our theoretical results on first-order effi-
ciency (Section 5.3), choice of mixing distribution (Section 5.4), and comparison to fixed-horizon
testing (Section 5.5). Next, in Section 5.6, we present our empirical results in a simulation set
up involving a single stream of normal data, and present an empirical investigation of the depen-
dence on the prior (Section 5.6.1), an empirical comparison of the mSPRT to fixed-horizon testing
(Section 5.6.2), and a comparison to other sequential testing approaches (Section 5.6.3).
5.1. The user model
Of course, any specific user’s preferences will be highly nuanced. In our analysis, for technical
simplicityweconsiderthefollowingusermodel:weassumeuserpreferencescanbecharacterizedby
a parameter M representing the maximum number of observations that the user is willing to wait,
together with their Type I error tolerance α. Given an always valid p-value process, we consider
a simple model of user behavior: users stop at either the first time the p-value drops below α (in

Johari, Pekelis, and Walsh: AlwaysValidInference
18
which case they reject the null), or at time M (in which case they do not reject the null unless the
| p-value | at time M | is also | below α), whichever | occurs | first. |     |
| ------- | --------- | ------- | ------------------- | ------ | ------ | --- |
We refer to such a user as a (M,α) user. In the remainder of the section, our goal will be to
make near-optimal tradeoffs between power and run-length for users in the limit where α→0,
without prior knowledge of their preferences, (M,α). Given the equivalence to a sequential test
(T(α),δ(α)), we define the (M,α) user’s decision rule by T(M,α)(cid:44)min{T(α),M}, and remark
| that δ(M,α)=1 | if    | and only | if T(α)≤M. |     |     |     |
| ------------- | ----- | -------- | ---------- | --- | --- | --- |
| 5.2. The      | mSPRT |          |            |     |     |     |
The always valid p-values we employ are derived from a particular family of sequential tests: the
mixture sequential probability ratio test (mSPRT) (Robbins 1970). We begin by imposing slight
restrictions on the data model: we assume that the data is real valued and drawn from a single
parameter exponential family, f (x)=F(cid:48)(x)=f (x)exp(θx−ψ(θ)), where tests are of the natural
|     |     |     | θ   | θ 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
parameter θ, Θ is an open interval, ψ(cid:48)(cid:48)(θ)>0 for all θ, and E|X |4 <∞. The function ψ(θ) is
1
| referred | to as the | log partition | function | for the family. |     |     |
| -------- | --------- | ------------- | -------- | --------------- | --- | --- |
The mSPRT is parameterized by a mixing distribution H over Θ, which we restrict to have
everywhere continuous and positive derivative. Given an observed sample average s up to time n,
n
))n.
the likelihood ratio of θ against θ is (f (s )/f (s Thus we define the mixture likelihood ratio
|              |      |     | 0    | θ n θ0              | n              |     |
| ------------ | ---- | --- | ---- | ------------------- | -------------- | --- |
| with respect | to H | as  |      |                     |                |     |
|              |      |     |      | (cid:90) (cid:18) f | (s ) (cid:19)n |     |
|              |      |     |      | θ                   | n              |     |
|              |      |     | ΛH(s | )=                  | dH(θ).         | (7) |
|              |      |     | n n  | f                   | (s )           |     |
|              |      |     |      | θ0                  | n              |     |
Θ
| The mSPRT | is then | defined | by:              |     |         |     |
| --------- | ------- | ------- | ---------------- | --- | ------- | --- |
|           |         |         | TH(α)=inf{n:ΛH(S |     | )≥α−1}; |     |
and (8)
|     |     |     |                | n       | n         |     |
| --- | --- | --- | -------------- | ------- | --------- | --- |
|     |     |     | δH(α)=1(cid:8) | TH(α)<∞ | (cid:9) , | (9) |
(cid:80)n
where S = X /n. The choice of threshold α−1 on the likelihood ratio ensures Type I error
|     | n i=1 | i   |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
is controlled at level α, via standard martingale techniques (Siegmund 1985). Intuitively, ΛH(S )
n n

Johari, Pekelis, and Walsh: AlwaysValidInference
19
represents the evidence against H in favor of a mixture of alternative hypotheses, based on the
0
first n observations. The test rejects H if the accumulated evidence ever becomes large enough.
0
Our first motivation for considering mSPRTs is that they are tests of power one (Robbins and
Siegmund 1974): for all α and θ(cid:54)=θ , there holds:,
0
P (T(α)<∞,δ(α)=1)=1.
θ
In other words, for the hypothetical user who can wait forever, any mSPRT delivers power one for
any alternative. Second, mSPRTs have been studied from a decision-theoretic framework, where
the cost of longer experiments is taken to be the terminal sample size multiplied by some cost c
per observation. The goal there is to balance this penalty against the costs associated with Type
I and Type II errors. mSPRTs are found to be asymptotically optimal as c→0 (Lai 2001). This is
a large data limit, analogous to the α→0, M →∞ setup of this paper.
For later reference, we note the following result due to Pollak and Siegmund (1975): for any
mixing distribution H, as α→0,
TH(α)/log(1/α)→I(θ,θ )−1:={(θ−θ )ψ(cid:48)(θ)−(ψ(θ)−ψ(θ ))}−1 (10)
0 0 0
holds in probability and in L2, where ψ(θ) is the log-partition function for the family F . This
θ
result characterizes the run-length of the mSPRT in the small α limit, and plays a key role in our
subsequent study of efficiency.
5.3. First-order efficiency in the α→0 limit
Wenowformalizeourstudyofthepowerandrun-lengthtradeoffforan(M,α)user.Inthissection,
the set of (T(M,α),δ(M,α)) decision rules is referred to as the set of feasible decision rules for an
(M,α) user.
We first map the two objectives of the user to formal quantities of interest. First, an (M,α) user
will want to choose her decision rule to maximize the power profile ν(θ)=P (δ=1) over θ(cid:54)=θ .
θ 0
Second, she will want to minimize the relative run-length profile, i.e., the run-length measured
against the maximum available to her, ρ(θ)=E (T)/M, viewed as a function of θ.
θ

Johari, Pekelis, and Walsh: AlwaysValidInference
20
Perfect efficiency would entail ρ(θ)=0 and ν(θ)=1 for all θ(cid:54)=θ . Of course, perfect efficiency
0
is generally unattainable for feasible decision rules. In this section we study the best achievable
performance a user can hope for, in the limit where α→0.
Our analysis depends on the characterization of run-length of the mSPRT in (10). The conse-
quence is that if we produce always valid p-values using the mSPRT, then in the limit as α→0
the study of efficiency divides into three cases depending on the relative values of M and log(1/α).
We consider these cases in turn.
“Aggressive” users: M (cid:29)log(1/α). Users in this regime are aggressive; α is large relative to
the maximum run-length they have chosen. In this regime, any mSPRT asymptotically recovers
perfect efficiency in the limit where α is small. Intuitively, because the user is willing to wait a
substantially longer time than log(1/α), a sublinear fraction of their maximum run-length is used
bythemSPRT;sincethemSPRTisatestofpower1,thismeanstheuserreceivespowernear100%
in return for a near-zero run-length profile. The proof of the following result follows immediately
from (10).
Proposition 2. Given any mixture H, let ρ(θ) and ν(θ) be the relative run-length and power
profiles, respectively, associated with (TH(M,α),δH(M,α)). If α → 0 and M → ∞ such that
M/log(1/α)→∞, we have ρ(θ)→0 and ν(θ)→1 at each θ(cid:54)=θ .
0
“Conservative” users: M (cid:28)log(1/α).Usersinthisregimeareconservative;αissmallrelative
to the maximum run-length they have chosen. In this case, experimentation is not productive: the
user is unwilling to wait long enough to detect any effects. Thus any mSPRT trivially performs as
well as any feasible decision rule for the user.
Proposition 3. For each (M,α), and any feasible decision rule, let ν be the associated power
profile. Then if α→0,M →∞ such that M/log(1/α)→0, we have ν(θ)→0 for each θ.
“Goldilocks” users: M ∼ log(1/α). This is the interesting case, where experimentation is
worthwhile but statistical analysis is non-trivial. To proceed we require an additional definition.

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |
| ---------------- | ---------- | -------------------- | --- | --- |
21
For a family of sequential tests, we want to define a measure of the worst-case efficiency over θ(cid:54)=θ
0
for an (M,α) user. Informally, we define this as the relative efficiency of the truncated test they
obtain by minimizing the relative run-length everywhere, compared with any other test that offers
| at least | as good power | everywhere. | This is formalized | as follows. |
| -------- | ------------- | ----------- | ------------------ | ----------- |
Definition 3. Given a sequential test (T(α),δ(α)), let ρ(θ;α,M) and ν(θ;α,M) be the relative
run-length and power profiles associated with (T(M,α),δ(M,α)). The relative efficiency of this
| test at | (M,α) is |     |     |     |
| ------- | -------- | --- | --- | --- |
ρ(θ)
|     |     |     | φ(M,α)= inf inf |     |
| --- | --- | --- | --------------- | --- |
ρ(θ;α,M)
(T,δ)θ(cid:54)=θ0
where the infimum is taken over all weakly more powerful, feasible decision rules: i.e., over tests
such that T ≤M a.s. , P (δ=1)≤α), and for all θ(cid:54)=θ there holds ν(θ)≥ν(θ;α,M).
|     |     | θ0  |     | 0   |
| --- | --- | --- | --- | --- |
Our main result demonstrates that in the regime where M ∼log(1/α), any mSPRT has relative
| efficiency | approaching | unity when | α→0. |     |
| ---------- | ----------- | ---------- | ---- | --- |
Theorem 2. Suppose ψ(cid:48)(cid:48) is absolutely continuous and there is an open interval around θ where
0
ψ(cid:48)(cid:48)(θ)<∞. Given any H, let φ(M,α) be the efficiency of the mSPRT (TH(α),δH(α)). If α→
| 0,M →∞ | such that | M =O(log(α−1)), | we have φ(M,α)→1. |     |
| ------ | --------- | --------------- | ----------------- | --- |
Note that this result is not dependent on the mixing distribution H. This is a consequence of
the fact that we study efficiency only to first-order in the limit as α→0. However, as we find in
the next section, the choice of prior can have an important second order effect on performance.
| 5.4. The | role of the | mixing distribution | H   |     |
| -------- | ----------- | ------------------- | --- | --- |
InthissectionweinvestigatetheimpactofthechoiceofthemixingdistributionH onperformance.
Asnotedintheprecedingsection,itisuserswithM ∼log(1/α)wherethereisameaningfultradeoff
between run-length and power; therefore we focus our attention on the role of H for this class of
users. Theorem 2 establishes that for these users any mSPRT is asymptotically efficient as α→0,
i.e., that no other test can offer a uniform improvement at every θ to first order in that limit.

|     |     |     |     |     |     |     |     | Johari, | Pekelis, and Walsh: AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------------------------- | --- |
22
However, the choice of H does influence the tradeoff between performance at different effect sizes,
and this tradeoff will yield a relevant second order effect on performance.
In this subsection, we consider a Bayesian setting where we have a prior θ∼G under H . The
1
followingtheoremgivesthemixingdistributionH thatminimizestherelativerun-lengthonaverage
over this prior for a “Goldilocks” user with parameters (M,α) (i.e., a user with M ∼log(1/α)).
| Theorem |     | 3.  |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Suppose G is absolutely continuous with respect to Lebesgue measure, and let H be
γ
a parametric family, γ∈Γ, with density h positive and continuous on Θ. Let ρ (θ) be the profile of
γ γ
relative run-lengths associated with (THγ(M,α),δHγ(M,α)). Then up to o(1) terms as α→0 and
with M =O(log(1/α)), the average relative run-length E {ρ (θ)} is minimized by any γ∗ such
θ∼G γ
that:
γ∗∈argmin−E
|     |     |     |     |     |     |     | 1 I(θ,θ |     | )−1logh (θ), | (11) |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- |
|     |     |     |     |     |     | θ∼G | A(M,α)  | 0   | γ            |      |
γ∈Γ
|     | where | A(M,α)={θ:I(θ,θ |     |     | )≥log(1/α)/M}. |     |     |     |     |     |
| --- | ----- | --------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
0
If h (θ)=q(γ ,γ )eγ1θ−γ2ψ(θ) is a conjugate prior for f , the data distribution, then γ∗ solves:
|     | γ   |     | 1 2 |     |     |     |     | θ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E
|     |     |     |     | ∂q(γ | ,γ  | )/∂γ |       | 1 θI(θ,θ | )−1 |     |
| --- | --- | --- | --- | ---- | --- | ---- | ----- | -------- | --- | --- |
|     |     |     |     |      | 1   | 2 1  | = θ∼G | A        | 0 . |     |
E
|     |     |     |     | ∂q(γ | ,γ  | )/∂γ | 1   | ψ(θ)I(θ,θ | )−1 |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- | --------- | --- | --- |
|     |     |     |     |      | 1   | 2 2  | θ∼G | A         | 0   |     |
We remark here that, consistent with our finding of first-order optimality for any choice of H
in Theorem 2, it follows from our proof that the choice of γ does not impact E {ρ (θ)} to first
θ∼G γ
| order | in  | the limiting | regime | of  | Theorem | 3.  |     |     |     |     |
| ----- | --- | ------------ | ------ | --- | ------- | --- | --- | --- | --- | --- |
Heuristically, the mSPRT rejects H when there is sufficient evidence in favor of any H :θ(cid:54)=θ ,
|     |     |     |     |     |     | 0   |     |     | 1   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
weightedbythedistributionH overalternatives.Thuswemightexpectoptimalsamplingefficiency
whenH ismatchedtotheprior.Ifwespecializetonormaldata,f (x)=φ(x−θ),acenterednormal
θ
prior, G(θ)=Φ(θ), and consider normal mixtures, h (θ)= 1φ(θ), this intuition is mostly accurate.
|     |            |     | τ       |        |           |          | γ        |     | γ γ |     |
| --- | ---------- | --- | ------- | ------ | --------- | -------- | -------- | --- | --- | --- |
| In  | that case, | the | optimal | choice | of mixing | variance | becomes: |     |     |     |
Φ(−b)
|     |     |     |     |     |     | γ2∗=τ2 |     |     |     | (12) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
1φ(b)−Φ(−b)
b

| Johari, Pekelis, | and | Walsh: | AlwaysValidInference |     |     |     |     |     |
| ---------------- | --- | ------ | -------------------- | --- | --- | --- | --- | --- |
23
| (cid:16) |     | (cid:17)1/2 |     |     |     |     |     |     |
| -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
2logα−1
for b= , equal to the prior variance multiplied by a factor correcting for anticipated
Mτ2
truncation. Sampling efficiency is improved by weighting towards larger effects when few samples
| are available | and | smaller | effects | where | there is | ample | data. |     |
| ------------- | --- | ------- | ------- | ----- | -------- | ----- | ----- | --- |
WesubsequentlyinvestigatetheimportanceofthechoiceofH empiricallyinSection5.6.1below.
| 5.5. Comparison |     | to fixed-horizon |     | testing |     |     |     |     |
| --------------- | --- | ---------------- | --- | ------- | --- | --- | --- | --- |
We now theoretically compare decisions based on mSPRT p-values with fixed-horizon testing.
In general, the fixed-horizon sample size must be chosen in reference to the effect sizes where
detection is needed; therefore, we compare performance of the mSPRT to a fixed-horizon test that
| is calibrated | to  | have good | average | power | over | the prior | G.  |     |
| ------------- | --- | --------- | ------- | ----- | ---- | --------- | --- | --- |
For convenience, we focus on the normal case G=N(0,τ2), and fix H =N(0,(γ∗)2). We consider
two rival tests for an arbitrary “Goldilocks” user: the mSPRT truncated at M, and the fixed-
horizon test chosen to have the same average power over this prior. For α small, the former has
lower average relative run-length over G, as formalized in the following proposition.
Proposition 4. Suppose G=N(0,τ2) and H =N(0,(γ∗)2) (cf. Theorem 3), and let ν∗(θ;α,M)
and ρ∗(θ;α,M) be the power profile and relative run-length profile of the resulting mSPRT trun-
cated at M. Let n∗ be the sample size such that the UMP fixed-horizon test at sample size n∗ has
expected power matching the truncated mSPRT, i.e., equal to E [ν∗(θ;α,M)]. Let ρ (θ;α,M) be
|              |            |          |            |               |         |       | θ∼G             | f              |
| ------------ | ---------- | -------- | ---------- | ------------- | ------- | ----- | --------------- | -------------- |
| the relative | run-length |          | profile of | this fixed    | horizon | test. |                 |                |
|              |            |          |            |               |         |       | E [ρ∗(θ;M,α)]/E |                |
| If α→0,M     |            | →∞, such | that M     | =O(log(1/α)), |         | then  |                 | [ρ (θ;α,M)]→0. |
|              |            |          |            |               |         |       | θ∼G             | θ∼G f          |
We subsequently empirically compare the mSPRT decision rule to fixed-horizon testing with
single stream data in Section 5.6.2 below. We also make this comparison again in Section 6.2, using
experiment data from the large-scale commercial A/B testing platform where these methods were
deployed.

|     |     |     |     |     | Johari, Pekelis, | and Walsh: | AlwaysValidInference |
| --- | --- | --- | --- | --- | ---------------- | ---------- | -------------------- |
24
| 5.6. | Empirical | analysis |     |     |     |     |     |
| ---- | --------- | -------- | --- | --- | --- | --- | --- |
In this subsection we complement our preceding theoretical analysis with a number of empirical
analyses. For all our simulations, we assume the normal data, prior, and mixture setup leading
to (12): i.e., normal data with f (x)=φ(x−θ), a centered normal prior with G(θ)=Φ(θ), and
θ
τ
normalmixingdistributionwithh (θ)= 1φ(θ).Informally,oursimulationsevaluateperformanceof
γ
γ γ
differentdecisionrulesfor(M,α)users, onaverage overeffectsizesdrawn fromtheprior. Formally,
for each tuple (α,M,τ), we draw effect sizes θ ∼G, b=1,...,B, and we simulate a stream of data
b
|     |     | i idF |     |     |     |     | (cid:80)B |
| --- | --- | ----- | --- | --- | --- | --- | --------- |
X =(X )M ∼ . We estimate average power and run-length profiles by νˆ= 1 1
| b   | n n=1 | θb  |     |     |     |     | B b=1 {Tb≤M} |
| --- | ----- | --- | --- | --- | --- | --- | ------------ |
(cid:80)B
and ρˆ= 1 min{T ,M}, where T corresponds to the first rejection time of test T(α) for
|     | BM  | b=1 | b   | b   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
H :θ=0 with data X . Finally, we compare average power νˆ and average run-length ρˆ across a
| 0       |           | b   |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- | --- |
| variety | of tests. |     |     |     |     |     |     |
{1e−4,1e−2,1e−1}, τ2
We select (α,M,τ) over the grid generated by outer product of α ∈ ∈
| {1e−4,1e−2,1e−1}, |     |     | {1e1,...,1e7}, |       | 1e4.              |         |                  |
| ----------------- | --- | --- | -------------- | ----- | ----------------- | ------- | ---------------- |
|                   |     | M ∈ |                | and B | = Rough estimates | suggest | these are enough |
Monte Carlo simulations for low variability. The effect size distributions were designed to approx-
imate reality for online experimenters, as τ2=1e−4 roughly matches a 10% relative improvement
on 1% conversion rate, 1e−2 a 100% improvement, and 1e−1 a 1000% improvement.
To achieve comparison across the wide range of parameters, we present results relative to the
M˜,
| re-parameterized |     | maximum | run-length | defined | as follows: |     |     |
| ---------------- | --- | ------- | ---------- | ------- | ----------- | --- | --- |
(cid:18) logα−1(cid:19)−1
M˜
=M .
τ2
5.6.1. The role of the mixing distribution H: Empirics Nominally, the dependence of
γ∗ on M presents a challenge. However, as we now demonstrate, the choice of mixing distribution
is quite robust with respect to variation in M, though getting γ “in the ballpark” is important.
We simulate the mSPRT for five different mixing regimes, γ ∈{γ∗,1,1e−1τ,τ,1e1τ}. Figure 2
depicts results. Across all cases, we find that γ misspecification of around one order of magnitude
leads to a less than 5% drop in average power, and no more than a 10% increase in average run-
length. Missing γ∗ by two orders of magnitude, however, can result in a 20% drop in average power

Johari, Pekelis, and Walsh: AlwaysValidInference
25
Figure 2 ResultsofempiricalinvestigationintotheroleofmixingdistributionH forthemSPRT.Fouralternative
mixingregimesarecompared,γ∈{1,1e−1τ,τ,1e1τ},toγ∗ (cf.Theorem3),showingrobustnessinrela-
tivepower(ν(γ)/ν(γ∗))andrun-length(ρ(γ)/ρ(γ∗))tomixingmisspecificationof1orderofmagnitude
across a variety of scenarios. The few cases where γ(cid:54)=γ∗ achieves superior results indicate a break-
down of asymptotics leading to Theorem 3. Note: we do not show results for severely under-powered
parameter combinations (νˆ<0.1), as the variance in estimates distracts from the overall picture.
and a 40% increase in average run-length. Note that we do not show results for severely under-
powered parameter combinations (νˆ<0.1), as the variance in estimates distracts from the overall
picture.
The story does change for “non-Goldilocks” users. As M˜ grows, νˆ→1 regardless of γ, resulting
in muted gains from H optimization, while ρˆ shows little sensitivity to M˜. Lastly, we remark on
thefewcaseswhereγ(cid:54)=γ∗ achievessuperiorresults.Theseallhaveα=0.1andM˜ <1.0,indicating
a horizon for the breakdown of asymptotics used in Theorem 3 for finite sample regimes.
5.6.2. Empirical comparison to fixed-horizon testing RecallthatProposition4givesthe
improvement in expected run-length of the mSPRT decision rule over an optimized fixed-horizon
test, asymptotically as α→0. We now evaluate this asymptotic result in a finite sample setting.
Figure 3 shows the benefit from stopping early outweighs the cost of additional slack in always
valid decision boundaries at reasonable power levels (ρˆ≥0.5), regardless of parameter values.

Johari, Pekelis, and Walsh: AlwaysValidInference
26
Figure 3 Average run-time for optimally tuned mSPRT (ρ∗) and fixed-horizon UMP test (ρ ), chosen to have
f
sameaveragepoweroverdistributionofeffectsizes.TheasymptoticresultofProposition4isshownto
hold in many finite sample settings.
We also make a similar comparison in Section 6.2, using data from over 10,000 experiments with
two streams (treatment and control) from the large-scale commercial A/B testing platform where
these methods were deployed. (See Figure 5 and the discussion in Section 6.2 for further details.)
5.6.3. Empirical comparison to other sequential testing approaches As noted above,
asymptotic first-order efficiency is almost certainly not unique to the mSPRT, even across (M,α)
users. The discussion in Section 2.2 of our paper, and in particular Section 4.1.1 of Kaufmann et al.
(2014), highlights tests of the form:
(cid:40) (cid:41)
(cid:18)
2β(n,α)
(cid:19)1/2
Tβ(α)=inf n : S >
n n
as a reasonable alternative class of candidates. In this section we compare the mSPRT to two
testsoftheprecedingform,fromRobbins(1970)andKaufmannetal.(2014)respectively.Formally,
withinthesimulationframeworkspecifiedabove,wecomparedecisionrulesfor(M,α)usersderived
from the following sequential tests:
1. the H-optimal mSPRT derived in this paper (denoted mSPRT opt in the plots);
2. the test proposed in Section 3 of Robbins (1970), characterized by β(n,α) = n+1log(n+1)
n 2α
(denoted r70 in the plots); and

Johari, Pekelis, and Walsh: AlwaysValidInference
27
3. a “LIL based” test with β(n,α)=log(α−1)+3loglog(α−1)+ 3loglog(e∗n) from Kaufmann
2
et al. (2014) (denoted k14 in the plots).
In Figure 4 we show that across all finite sample regimes examined, mSPRT opt has optimal
averagepowerandrun-lengthwhiler70andk14viefordominance.Theseresultshighlightageneral
phenomenon. While multiple decision rules may make the “Goldilocks” user perfectly efficient in
the limit, they differ in preferential treatment for some (M,α) users over others. Concretely, the
improved rate of efficiency gain for k14 comes at the cost of lower efficiency for low to moderate
M˜.
The mSPRT is given an advantage as it is optimally tuned to the user’s M via γ∗, but we stress
thatwhilesometuningisadvised,finitesampleefficiencyispracticallyrobusttoH misspecification.
Even for users who truncate at 100x the typical run-length (M˜ =100), mSPRT opt has roughly
5% improvement on average power over its peers, which is within the two order of magnitude
misspecification range identified in Section 5.6.1. Average run-length remains 20% better for all
M˜ ≥1e1, and up 40% better in some cases (τ =1e−2,α=0.1).
6. Deployment
Onetechnicalchallengeremainsbeforethealwaysvalidp-valuesandconfidenceintervalsderivedin
theprevioussectionmaybeusedinA/Btesting.Whilethosemeasuresaddressinferenceforasingle
parameterinasingleIIDsequenceofdata,incomingvisitorstoanA/Btestareactuallyrandomized
into two streams where each stream receives a distinct treatment. In this section, we summarize
how the measures can be modified to address the two most typical goals in practice: inference on
the difference in means between two streams of normally distributed data, and inference on the
differenceinsuccessprobabilitiesforbinary-valueddata(bothofthesearecommonlyreferredtoas
the difference in “conversion rates”). The discussion is limited to p-values, but the results may be
extended to confidence intervals in the usual way. Since January 2015, these two-stream p-values
and confidence intervals have been implemented in a large scale platform serving thousands of
clients, ranging from small businesses to large enterprises.

Johari, Pekelis, and Walsh: AlwaysValidInference
28
Figure 4 Averagepower(ν)andrelativerun-length(ρ)overadistributionofeffectsizes,comparedfor3always
validdecisionboundaries:theH-optimalmSPRT(mSPRT opt),aproposalinRobbins(1970)(r70),and
a “LIL based” test from Kaufmann et al. (2014) (k14). The optimally tuned mSPRT is strictly more
efficient at all but the smallest levels of truncation, and continues to be substantially so even at very
large truncation, despite the improved rate of efficiency gain for k14.
In the case of normal data, we develop a two-stream mSPRT which gives exact uniform Type I
error control for testing the composite null hypothesis that the two means are equal. Extending the
asymptotic theory of the previous section, we find that first-order efficiency for trading off power
and run-time in the α→0 limit is still obtained. As in the single stream case, our two-stream
mSPRT is parameterized by a mixing parameter H over the unknown treatment effect. Theorem
3 carries over to this setting, indicating how this mixture should be tailored to the distribution
of anticipated effects, in order to obtain good performance at moderate α. Much of the technical
details are deferred to Appendix B.

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- | --- |
29
For binary data, our two-stream mSPRT achieves approximate uniform Type I error control by
appealing to the Central Limit Theorem. In this case, we use empirical data from our deployment
to detail the efficiency gain over fixed-horizon testing. As in Sections 5.5 and 5.6.2, we see that the
mSPRT, which is optimized to a prior for the treatment effect, can trade off power and run-time
better than a comparably optimized fixed-horizon test. Of particular practical importance, the
mSPRT is seen to outperform any fixed-horizon test that the experimenter might select herself,
| unless          | she has far better | prior information | than the platform | does. |     |     |
| --------------- | ------------------ | ----------------- | ----------------- | ----- | --- | --- |
| 6.1. Two-stream | p-values           |                   |                   |       |     |     |
We represent observations in the two streams by IID sequences X=(X )∞ and Y=(Y )∞ . For
|     |     |     |     | n   | n=1 | n n=1 |
| --- | --- | --- | --- | --- | --- | ----- |
normaldata,wehaveX ∼N(µ ,σ2),Y ∼N(µ ,σ2)whereµ andµ areunknown,whilethevari-
|     |     | n 0 | n 1 | 0 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
anceσ2
isassumedknownandcommontobothstreams.Forbinarydata,X ∼Bernoulli(p ),Y ∼
|     |     |     |     |     | n   | 0 n |
| --- | --- | --- | --- | --- | --- | --- |
Bernoulli(p ), where p ,p ∈(0,1) are unknown. The conversion rate difference is θ=µ −µ or
|     | 1   | 0 1 |     |     |     | 1 0 |
| --- | --- | --- | --- | --- | --- | --- |
θ=p 1 −p 0 respectively. In either case, we want to test the composite null hypothesis H 0 :θ=0
| against | H :θ(cid:54)=0. |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- |
1
We make the simplification that visitors arrive in pairs with one visitor assigned to each treat-
ment, so that observations are obtained as a sequence of pairs (W )∞ =(X ,Y ),(X ,Y ),.... An
|     |     |     |     | n   | 1 1 | 2 2 |
| --- | --- | --- | --- | --- | --- | --- |
n=1
alwaysvalidp-valueisunderstoodasaprocessadaptedtothefiltrationgeneratedbythissequence,
which controls Type I error uniformly over both the composite null hypothesis and the choice
of stopping time. This model closely approximates the treatment allocation typically adopted in
practice, where visitors arrive individually and each visitor is allocated to each treatment with
50% probability independently of all other visitors. A similar approach can be used even if the
allocation to each group is not even, as long as it is fixed in advance. Extensions to other allocation
policies, such as data-dependent bandit schemes, will be the subject of future work.
For normal data, we view (W )∞ as a single stream of IID data from a bivariate distribution
n n=1
parameterized by the pair (θ,µ), where µ=(µ +µ )/2. It is straight forward to show that, after
0 1
fixing µ=µ∗ arbitrarily, this distribution corresponds to the one-parameter exponential family

|     |     |     |     | Johari, Pekelis, | and Walsh: AlwaysValidInference |     |
| --- | --- | --- | --- | ---------------- | ------------------------------- | --- |
30
(cid:16) (cid:17)
f (w)∝φ y− x−θ , where w=(x,y). Hence we may implement the mSPRT based on f , i.e. we
| θ   | √   |     |     |     |     | θ   |
| --- | --- | --- | --- | --- | --- | --- |
σ 2
threshold the mixture likelihood ratio given in (7) with s = 1 (cid:80)n w . For any µ∗, this mSPRT
|     |     |     |     | n     | i   |     |
| --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     | n i=1 |     |     |
controls Type I error for testing the simple null H :θ=0,µ=µ∗ against H :θ(cid:54)=0,µ=µ∗, and
|     |     |     | 0   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- |
so the p-value derived from this mSPRT is always valid for testing the composite null hypothesis.
In Appendix B, we show that it satisfies natural analogues of the single-stream optimality results
| described | in Section | 5.  |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- |
Unfortunately for binary data, the distribution of W does not reduce to a one-parameter expo-
n
nential family. Nonetheless we set p=(p +p )/2 and denote the density of W by f . Then, for
|     |     |     | 0 1 |     | n   | θ,p |
| --- | --- | --- | --- | --- | --- | --- |
any θ and p∗, in the limit as n→∞, the likelihood ratio against the pair (θ ,p∗) in favor of (θ,p∗)
0
| approaches | (f˜(s )/f˜ | (s ))n, where | (with w=(x,y)): |              |            |     |
| ---------- | ---------- | ------------- | --------------- | ------------ | ---------- | --- |
|            | θ n        | θ0 n          |                 |              |            |     |
|            |            | (cid:32)      | (cid:33)        |              |            |     |
|            | f˜(w)=φ    |               | y−x−θ           |              |            |     |
|            |            |               |                 | , p∗=p∗−θ/2, | p∗=p∗+θ/2. |     |
|            | θ          | (cid:112)     |                 | 0            | 1          |     |
p∗(1−p∗)+p∗(1−p∗)
|     |     | 0   | 0 1 1 |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
We compute the mSPRT p-values based on this density using the sample means in each stream
as plug-in estimates for p∗ and p∗. If α is moderate, the mSPRT terminates with high probability
|     |     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
before this asymptotic distribution becomes accurate, so Type I error is not controlled. However,
for α small, simulation shows that these p-values are approximately always valid.
| 6.2. Real-world | improvement |     |     |     |     |     |
| --------------- | ----------- | --- | --- | --- | --- | --- |
Now we use empirical data to document the improvement of our two-stream mSPRT over fixed-
horizon testing for binary data. For this purpose, 10,000 experiments were randomly sampled from
those binary experiments run on a large-scale commercial A/B testing platform in early 2015.
Customers of the platform in 2015 could purchase subscriptions at one of four tiers: Bronze,
Silver,GoldorPlatinum.Customersinthehighertierstendedtobelarger,betteroptimizedorgani-
zations,whoweretargetingsmallereffectsizes.Byseparatingoutthe10000experimentsaccording
to the subscription tier of the experimenters, we can investigate how the two-stream mSPRT per-
forms under different true effect distributions. This mirrors how we varied the prior G for the
numerical simulations presented in Section 5. Specifically, for each tier, we found that the observed

Johari, Pekelis, and Walsh: AlwaysValidInference
31
Figure 5 The empirical distribution of sample size ratios between the mSPRT and suitably optimized fixed-
horizon tests over 10,000 randomly selected experiments, divided up by the subscription tier of the
customer on the platform. See main text for details.
(cid:112)
datawasconsistentwithanormaldistributionoftrueeffectsizesθ/ p∗(1−p∗)+p∗(1−p∗)across
0 0 1 1
experiments, so we fit a centered normal prior G with unknown variance for the effect under the
alternative hypothesis. For this fitting, shrinkage has been applied to the distribution of observed
effect sizes via James-Stein estimation (James and Stein 1961) to address the statistical noise in
these observed values.
In Figure 5, we compare the run-time of the mSPRT optimized to the fitted distribution, G,
against the fixed-horizon test at which 80% average power over G is obtained. The red curve is
the empirical distribution for the ratio between the sample size where the mSPRT terminates and
this fixed-horizon. For all tiers, the ratio falls below one with high probability. The black curves
compare the mSPRT against the fixed-horizon test that the experimenter might choose if she has
additional information about the effect size sought, beyond what is captured in the distribution,
G. Here we suppose that she can estimate the unknown effect up to some specified relative error,
and then she selects the sample size that provides 80% power at her lower bound for the effect.
In fact, a very precise estimate is required to achieve a run-time improvement over the mSPRT
(a relative error below 50% would rarely be achievable in practice). Further discussion of Figure
5, and of the broader practical gains associated with our two-stream mSPRT p-values, is given in
our companion paper, Johari et al. (2017).

Johari, Pekelis, and Walsh: AlwaysValidInference
32
7. Multiple testing
In this final section, we examine how always valid p-values and confidence intervals may be com-
bined with existing multiple testing procedures when several experiments are conducted simulta-
neously. One option is to derive inference measures for each test individually, and these bound
the expected proportion of the experiments that incur a Type I error, i.e., the false positive rate.
However, that approach can be insufficient if the combination of Type I errors across multiple
experiments can have a disproportionate impact on the user’s ability to make good decisions. In
the multiple testing literature, fixed-horizon p-values and confidence intervals are taken as input,
and the procedures output q-values and corrected confidence intervals that are designed to satisfy
a global error constraint that better reflects the overall cost to the user.
Obtaining the same error controls with a data-dependent sample size is highly non-trivial, even
ifthestoppingruleisfixedbytheplatform.However,alwaysvalidityprovidesanopportunitytodo
so,whilestillofferingtheusersubstantiallatitudetochooseherownstoppingtime.Inwhatfollows,
weconsidertwoleadingmultipletestingerrorconstraints:family-wiseerrorrate(FWER)andfalse
discovery rate (FDR), defined below. We obtain conditions on the user’s stopping time that ensure
these objectives can be bounded by supplying always valid p-values and confidence intervals as
input to fixed-horizon procedures in popular use. In this sense, we say that these procedures, as
well as the error constraints, “commute” with always validity over a class of stopping times. The
resulting always valid q-values and corrected confidence intervals have both been adopted in the
large-scale commercial A/B testing platform, in appropriate contexts.
Wesupposethatmexperimentsareinitiatedatonce,andateachsuccessivesteponeobservation
is made simultaneously on every experiment.
7.1. Error constraints
We focus on the two error functions most extensively studied. The first is the family-wise error
rate (FWER):
FWER=maxP (δ =1 for at least one i s.t. θi=θi).
θ i 0
θ

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- | --- |
33
| This is    | the worst-case | probability     | of incurring             | any false positive. |     |          |
| ---------- | -------------- | --------------- | ------------------------ | ------------------- | --- | -------- |
| The second | is the         | false discovery | rate (FDR):              |                     |     |          |
|            |                |                 | (cid:26) #{1≤i≤m:θi=θi,δ |                     | =1} | (cid:27) |
i
|     |     | FDR=maxE |     |           | 0     | .   |
| --- | --- | -------- | --- | --------- | ----- | --- |
|     |     |          | θ   | #{1≤i≤m:δ | =1}∧1 |     |
|     |     |          | θ   |           | i     |     |
Thisistheworst-caseaverageproportionoffalsepositivesamongthoseexperimentswherethenull
hypothesis is rejected. As an example, consider a user who runs multiple experiments in order to
compare the performance of the same two variations across different metrics. Each arriving visitor
produces one observation for each experiment. FWER control across these experiments may be
useful if she must prioritize performance on every metric, so a mistake in just one experiment can
be very costly. FDR control may be useful if good performance on balance over many metrics is
sufficient.
| 7.2. Fixed-horizon |     | procedures |     |     |     |     |
| ------------------ | --- | ---------- | --- | --- | --- | --- |
The goal of a multiple testing procedure is to make a decision on whether to reject or accept
each null hypothesis, such that a global error constraint holds. In general, the existing multiple
testingliteratureassumesafixed-horizonframework.ThestandardproceduretocontroltheFWER
is the Bonferroni correction (Dunn 1961): this takes fixed-horizon p-values as input and rejects
|     |     |     |     | p(j)≤α/m, |     | p(1),...,p(m) |
| --- | --- | --- | --- | --------- | --- | ------------- |
hypotheses (1),...(j) where j is maximal such that and are the p-values
arranged in increasing order. For FDR, the standard procedure is Benjamini-Hochberg (Benjamini
and Hochberg 1995), abbreviated as BH. Given fixed-horizon p-values, two versions of BH are used
depending on whether the data are known to be independent across experiments. If independence
holds (BH-I), the procedure rejects hypotheses (1),...,(j) where j is maximal such that p(j) ≤
αj/m; in general (BH-G), the procedure chooses the maximal j such that:
αj
|     |     |     | p(j)≤ |     | .   |     |
| --- | --- | --- | ----- | --- | --- | --- |
m (cid:80)m 1/r
r=1
For the purposes of an A/B testing platform, such a procedure can be viewed as a mapping from
the m fixed-horizon p-values to so-called q-values that can be displayed on an identical dashboard

Johari, Pekelis, and Walsh: AlwaysValidInference
34
(see Appendix). By thresholding each q-value at α, a user can bound the given error function at
her desired level. The practical advantages of p-values described in Section 1 are preserved: the
same q-values can be used by many naive users, each with their own α.
Lastly, these procedures have similar interpretations for confidence intervals. Here the goal is to
control false coverage when the user selects some subset of the experiments. One difference is while
users typically only view the p-values of significant experiments, they may wish to gauge the range
of plausible parameter values even in those experiments where the null hypothesis is not rejected.
FortheBonferroniprocedure,andanysetofconfidenceintervalsIi(α),constructingnewintervals
Ii(α/m) bounds the probability that a confidence interval fails to cover the true value on any of
the selected experiments, giving FWER control.
The analogy to FDR is the False Coverage Rate (FCR) (Benjamini and Yekutieli 2005): the
expectedproportionoftheselectedconfidenceintervalsthatincurfalsepositives,setatzeroifnone
are selected. Benjamini and Yekutieli (2005) give a procedure to obtain FCR control at a fixed
horizon when the experiment selection rule is known: the nominal level α is replaced by Rα/m for
some R defined in terms of the rule. Here we extend their approach to address unknown selection
rules in the fixed-horizon context, which we later use as a first step for sequential FCR control over
classes of stopping times.
We restrict to selection rules that are the union of the discoveries and some fixed set J of
experiments, with j =|J|(cid:28)m, which are always of interest to the user. Theorem 4 then gives
a procedure which bounds the FCR in terms of j. The proof is given in the Appendix. For the
procedure described in Benjamini and Yekutieli (2005), it is the aggressive selection rules that
choose few experiments which can obtain the highest FCR, and roughly speaking R is a measure
of how few experiments the rule can select. Our approach is to be conservative over the unknown
selection rule, taking R for each interval to be the fewest number of experiments that could be
selected, given that this interval corresponds to a selected experiment.

| Johari, Pekelis, |     | and Walsh: | AlwaysValidInference |     |     |     |
| ---------------- | --- | ---------- | -------------------- | --- | --- | --- |
35
| Theorem | 4.  |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- |
Given fixed-horizon p-values p, let SBH be the rejection set under BH-I, RBH =
|SBH|, and (CIi(1−s))m be the corresponding fixed-horizon CIs at each level s∈(0,1). Define
i=1
| the corrected |     | confidence | intervals: |     |     |     |
| ------------- | --- | ---------- | ---------- | --- | --- | --- |

 
|     |     |     |     | CIi(1−RBHα/m) |     | i∈SBH; |
| --- | --- | --- | --- | -------------- | --- | ------ |
|     |     |     |     | i             |     |        |
C˜I = (13)
 
|     |     |     |     |  CIi(1−(RBH+1)α/m) |     | i∈/SBH. |
| --- | --- | --- | --- | -------------------- | --- | ------- |
Then for any J, if the selection rule is the experiments J∪S , the FCR is at most α(1+j/m).
BH
| 7.3. Commuting |     | with | always | validity |     |     |
| -------------- | --- | ---- | ------ | -------- | --- | --- |
Propositions 7 and 8 in Appendix C establish that Bonferroni and BH-G commute with always
validity on all p-value processes. The reason is that, for any always valid p-values and any stopping
time, the set of p-values evaluated at that time defines a set of fixed-horizon p-values. This is
particularly useful as p-value processes may be replaced by q-value processes on a user’s streaming
dashboard and still enjoy always valid robustness guarantees. It is easy to show that Bonferroni
| commutes | with | always | validity | for confidence | intervals | as well. |
| -------- | ---- | ------ | -------- | -------------- | --------- | -------- |
BH-I does not commute with always validity over independent p-value processes, however,
because stopping times that depend on every experiment can introduce correlation in the p-values
at that time (see the Appendix for an example). Nonetheless, for many natural choices of this
stopping time, FDR control is still achieved for any independent always valid p-values. Theorem 5
| gives a    | sufficient | condition |     | on the stopping | time. |     |
| ---------- | ---------- | --------- | --- | --------------- | ----- | --- |
| Definition |            | 4.        |     |                 |       |     |
Given independent always valid p-values p , let SBH be the rejections when BH-I
n n
| is applied | to  | these at | level | α and let RBH | =|SBH|. Define: |     |
| ---------- | --- | -------- | ----- | ------------- | --------------- | --- |
n n
RBH
|     |     |     |     | T        | =inf{t : | =r}; |
| --- | --- | --- | --- | -------- | -------- | ---- |
|     |     |     |     |          | r t      |      |
|     |     |     |     | T+=inf{t | : RBH    | >r}; |
|     |     |     |     |          | r t      |      |
αr
|     |     |     |     | Ti=inf{t | : pi≤ | }.  |
| --- | --- | --- | --- | -------- | ----- | --- |
|     |     |     |     |          | r t   | m   |
Now, if p−i ,p−i ,... are the p-values for the experiments other than i placed in ascending
(1),n (2),n
order, consider a modified BH procedure that rejects hypotheses (1),...,(k) where k is maximal

|     |     |     |     |     |     |     |     | Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | -------------------- | --- |
36
such that p−i ≤α(k+1)/m, in parallel to the fixed horizon approach in Benjamini and Hochberg
(k),n
(SBH)−i
(1995). Define the rejection set as those obtained under the original BH-I procedure if
n 0
| pi  |     | (RBH)−i=|(SBH)−i| |     |     |              |         |              |     |     |     |     |
| --- | --- | ----------------- | --- | --- | ------------ | ------- | ------------ | --- | --- | --- | --- |
| =0. | Let |                   |     |     | and          | define: |              |     |     |     |     |
| n   |     | n                 | 0   | n   | 0            |         |              |     |     |     |     |
|     |     |                   |     |     | (T )−i=inf{t |         | : (RBH)−i=r} |     |     |     |     |
r
|     |     |     |     |     |              | 0   | n 0           |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | --- | --- | --- |
|     |     |     |     |     | (T+)−i=inf{t |     | : (RBH)−i>r}. |     |     |     |     |
|     |     |     |     |     | r            | 0   | n             | 0   |     |     |     |
We have the following theorem. The proof can be found in Appendix C.
Theorem 5. Given a stopping time T, let m be the number of truly null hypotheses and let I be
0
| the set | of  | null hypotheses |     | i such | that: |     |     |     |     |     |     |
| ------- | --- | --------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
m
|     |     |     |     | (cid:88) (cid:16) |        |      | (cid:12)          |        | (cid:17) |     |      |
| --- | --- | --- | --- | ----------------- | ------ | ---- | ----------------- | ------ | -------- | --- | ---- |
|     |     |     |     | P                 | )−i    | <(T+ | )−i (cid:12) Ti≤T |        |          |     |      |
|     |     |     |     |                   | (T r−1 | ≤ T  |                   | , T <∞ | >1       |     | (14) |
|     |     |     |     |                   | 0      |      | r−1 0 (cid:12)    | r      |          |     |      |
r=1
| Then | the | rejection | set | SBH | has FDR | at most |     |     |     |     |     |
| ---- | --- | --------- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- |
T
|     |     |     |     |     |     | (cid:18) m | |I| (cid:80)m 1(cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------------- | --- | --- | --- | --- |
0
|     |     |     |     |     |     | α + | k=2 k | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     | m   | m     |     |     |     |     |
In particular, if we permit only stopping times where I is empty, BH-I controls FDR and so
| commutes |     | with | always | validity | over all | independent | processes. |     |     |     |     |
| -------- | --- | ---- | ------ | -------- | -------- | ----------- | ---------- | --- | --- | --- | --- |
We can develop intuition for (14) by evaluating the condition on common examples. Perhaps the
most natural stopping time for a user is the first time some fixed number x≤m hypotheses are
| rejected; | i.e.     | T   | =inf | {n : R | =x}.     | In that case, |          |          |     |          |          |
| --------- | -------- | --- | ---- | ------ | -------- | ------------- | -------- | -------- | --- | -------- | -------- |
|           |          |     | n    |        | n        |               |          |          |     |          |          |
|           | (cid:16) |     |      |        | (cid:12) |               | (cid:17) | (cid:16) |     | (cid:12) | (cid:17) |
| P         |          |     |      |        |          |               | =P       |          |     |          |          |
(T )−i ≤ T <(T+ )−i (cid:12) Ti≤T , T <∞ (T )−i ≤ T <(T+ )−i (cid:12) T <∞
|     | r−1 | 0   | x   | r−1 | 0 (cid:12) r | x x |     | r−1 0 | x r−1 | 0 (cid:12) x |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ----- | ----- | ------------ | --- |
foreachi.Thisprobabilityis1ifr=xand0otherwise,soI isindeedemptyandFDRiscontrolled.
Ontheotherhand,anaturalstoppingtimewhereI isnon-emptyforsomep-valuesisthefirsttime
that significance is reached in any of a given subset of experiments, where this subset has between
two and (m−1) elements. A proof is given in Appendix C, together with simulations showing that
| FDR | control | can | be violated |     | in this | case. |     |     |     |     |     |
| --- | ------- | --- | ----------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
Corrected confidence interval processes that give approximate FCR control can be derived with
analogous restrictions by combining the results of Theorem 5 and the methods in Theorem 4.

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |     |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
37
| Definition | 5.       |     |             |             |     |         |       |     |     |
| ---------- | -------- | --- | ----------- | ----------- | --- | ------- | ----- | --- | --- |
|            | If pi,θ0 | is  | the p-value | for testing |     | H :θi=θ | , let |     |     |
|            |          | n   |             |             |     | 0       | 0     |     |     |
αr
|     |     |     | Ti,θ0    |        | pi,θ0              |                   |     |     |     |
| --- | --- | --- | -------- | ------ | ------------------ | ----------------- | --- | --- | --- |
|     |     |     | =inf{t   |        | :                  | ≤                 | }   |     |     |
|     |     |     | r        |        | t                  | m                 |     |     |     |
|     |     |     | (T )−i,J | =inf{t | : |(SBH)−i∪J\i|=r} |                   |     |     |     |
|     |     |     | r 0      |        |                    |                   |     |     |     |
|     |     |     |          |        |                    | n                 | 0   |     |     |
|     |     |     | (T+)−i,J | =inf{t | :                  | |(SBH)−i∪J\i|>r}. |     |     |     |
|     |     |     | r 0      |        |                    | n                 | 0   |     |     |
The last two stopping times denote the first times at least r and more than r experiments other
| than i, respectively, |     | are selected. |     |     |     |     |     |     |     |
| --------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
If p−i ,p−i ,... are the p-values for the experiments other than i placed in ascending order,
| (1),n | (2),n |     |     |     |     |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
consider another modified BH procedure that rejects hypotheses (1),...,(k) where k is maximal
such that
k
p−i
|     |     |     |     |     |       | ≤α  | ,   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     | (k),n | m   |     |     |     |
These are the rejections obtained under the original BH-I procedure if pi =1. We define stopping
n
|     |     |     |     |     | )−i,J | (T+)−i,J |     |     |     |
| --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
times associated with this procedure (T and analogous to the two stopping times
|     |     |     |     | r   | 1   |     | r 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
above.
| We have | the following | theorem. |     |     |     |     |     |     |     |
| ------- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Theorem | 6.            |          |     |     |     |     |     |     |     |
Given independent always valid p-values p and corresponding CIs (CIi(1−s))m
|         |                |        |     |            |            |     | n   | n   | i=1 |
| ------- | -------------- | ------ | --- | ---------- | ---------- | --- | --- | --- | --- |
| at each | level s∈(0,1), | define | new | confidence | intervals: |     |     |     |     |


|     |     |     |  CIi(1−RBHα/m) |     |     |     | i∈SBH; |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | ------ | --- | --- |

|     |     |     | C˜I i | n   | n   |     |     | n   |      |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
|     |     |     | =     |     |     |     |     |     | (15) |
n


|     |     |     |  CI | i(1−(R | BH+1)α/m) |     | i∈/S | BH. |     |
| --- | --- | --- | ----- | ------ | --------- | --- | ---- | --- | --- |
|     |     |     |       | n      | n         |     |      | n   |     |
Let J be a set of experiments and let T be a stopping time such that the following conditions hold
| for every | i, where θi | is the | true parameter |     | value | for that | hypothesis: |     |     |
| --------- | ----------- | ------ | -------------- | --- | ----- | -------- | ----------- | --- | --- |
m
|     |     | (cid:88) | P((T )−i,J |     | <(T+)−i,J|Ti,θi |     |     |        |      |
| --- | --- | -------- | ---------- | --- | --------------- | --- | --- | ------ | ---- |
|     |     |          |            | ≤T  |                 |     | ≤T  | <∞)≤1; | (16) |
|     |     |          | r          | 0   | r               | 0   | r   |        |      |
r=1
m
|     |     | (cid:88) | P((T )−i,J |     | <(T+)−i,J|Ti,θi |     |     |        |      |
| --- | --- | -------- | ---------- | --- | --------------- | --- | --- | ------ | ---- |
|     |     |          |            | ≤T  |                 |     | ≤T  | <∞)≤1. | (17) |
|     |     |          | r          | 1   | r               | 1   | r   |        |      |
r=1
|     |     |     |     |     |     |     | (C˜I i |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
Then under the selection rule J∪SBH, the intervals ) have FCR at most α(1+j/m).
|     |     |     |     | T   |     |     | T   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Johari, Pekelis, and Walsh: AlwaysValidInference
38
8. Conclusion
Our paper derives always valid p-values and confidence intervals for A/B testing. These allow
heterogeneoususerstocontinuouslymonitortheirexperimentsandtoderiveinferencesatanytime,
which efficiently trade-off power and run-time for their needs. In addition, we have identified how
these measures may be combined with multiple hypothesis testing corrections to achieve sequential
multiple testing controls.
We have only needed to place weak assumptions on the data generating processes; namely that
observations are binary or normally distributed and independent across successive visitors entering
the experiment. However, in some contexts, A/B testing data can be heavily right-tailed (Fithian
and Wager 2014). Various methods for modeling this skewed data are used in practice, and con-
struction of always valid inference measures under these models would be a useful extension to
this paper. Further, the assumption of independence can fail due to seasonal effects, which induces
correlations between visitors who arrive at similar times during the experiment. Our implementa-
tion paper (Johari et al. 2017) provides a simple heuristic (a “reset policy”) which identifies when
seasonality may have led to inaccurate inference measures and applies conservative corrections to
address this. In future work, we aim to tackle the issue in more detail, deriving inference measures
from an extension of the mSPRT that models the time dependence directly.
This paper has only considered the case where incoming visitors are randomized to treatments
independently of the data collected so far. In fact, it can be shown that the inference measures
achieve Type I error control at any stopping time, even if treatments are assigned according to a
banditalgorithm(seeSection2).Unifyingthesemeasureswithbanditapproacheswouldbevaluable
future work. In particular, one might ask what allocation policy enables the mSPRT to achieve
significance most quickly, or how the power and relative run-time profiles of always valid measures
are impacted if the allocation is optimized to another objective such as regret minimization.
Endnotes

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- | --- | --- |
39
1. The platform is named Optimizely (http://www.optimizely.com). The methodology of this
paper forms the core of the statistical backend of the Optimizely platform. Throughout the paper,
we refer to the platform as “a large commercial A/B testing platform” or similar.
References
Abbasi-Yadkori Y, P´al D, Szepesv´ari C (2011) Improved algorithms for linear stochastic bandits. Advances
| in Neural | Information |     | Processing | Systems, | 2312–2320. |     |     |
| --------- | ----------- | --- | ---------- | -------- | ---------- | --- | --- |
Balsubramani A (2014) Sharp finite-time iterated-logarithm martingale concentration. arXiv preprint
| arXiv:1405.2639 |     | .   |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
BalsubramaniA,RamdasA(2015)Sequentialnonparametrictestingwiththelawoftheiteratedlogarithm.
| arXiv preprint |     | arXiv:1506.03486 |     | .   |     |     |     |
| -------------- | --- | ---------------- | --- | --- | --- | --- | --- |
Benjamini Y, Hochberg Y (1995) Controlling the false discovery rate: a practical and powerful approach to
multiple testing. Journal of the Royal Statistical Society. Series B (Methodological) 289–300.
BenjaminiY,YekutieliD(2001)Thecontrolofthefalsediscoveryrateinmultipletestingunderdependency.
| Annals of | statistics | 1165–1188. |     |     |     |     |     |
| --------- | ---------- | ---------- | --- | --- | --- | --- | --- |
Benjamini Y, Yekutieli D (2005) False discovery rate–adjusted multiple confidence intervals for selected
| parameters. | Journal | of  | the American | Statistical |     | Association | 100(469):71–81. |
| ----------- | ------- | --- | ------------ | ----------- | --- | ----------- | --------------- |
Bubeck S, Cesa-Bianchi N, et al. (2012) Regret analysis of stochastic and nonstochastic multi-armed bandit
| problems. | Foundations |     | and Trends(cid:13)R | in  | Machine | Learning | 5(1):1–122. |
| --------- | ----------- | --- | ------------------- | --- | ------- | -------- | ----------- |
Bubeck S, Munos R, Stoltz G (2009) Pure exploration in multi-armed bandits problems. International
| conference | on Algorithmic |     | learning | theory, | 23–37 | (Springer). |     |
| ---------- | -------------- | --- | -------- | ------- | ----- | ----------- | --- |
Darling D, Robbins H (1967) Confidence sequences for mean, variance, and median. Proceedings of the
| National | Academy | of Sciences |     | of the United | States | of America | 58(1):66. |
| -------- | ------- | ----------- | --- | ------------- | ------ | ---------- | --------- |
delaPen˜aVH,LaiTL,ShaoQM(2008)Self-normalized processes: Limit theory and Statistical Applications
| (Springer | Science | & Business |     | Media). |     |     |     |
| --------- | ------- | ---------- | --- | ------- | --- | --- | --- |
Demets DL, Lan KG (1994) Interim analysis: the alpha spending function approach. Statistics in medicine
13(13-14):1341–1352.

Johari, Pekelis, and Walsh: AlwaysValidInference
40
Dunn OJ (1961) Multiple comparisons among means. Journal of the American Statistical Association
56(293):52–64.
Even-DarE,MannorS,MansourY(2002)Pacboundsformulti-armedbanditandmarkovdecisionprocesses.
International Conference on Computational Learning Theory, 255–270 (Springer).
Fithian W, Wager S (2014) Semiparametric exponential families for heavy-tailed data. Biometrika
102(2):486–493.
Foster DP, Stine RA (2008) α-investing: a procedure for sequential control of expected false discoveries.
Journal of the Royal Statistical Society: Series B (Statistical Methodology) 70(2):429–444.
Ghosh BK, Sen PK (1991) Handbook of sequential analysis (CRC Press).
HoeffdingW(1960)Lowerboundsfortheexpectedsamplesizeandtheaverageriskofasequentialprocedure.
The Annals of Mathematical Statistics 352–368.
Howard SR, Ramdas A, McAuliffe J, Sekhon J (2018) Uniform, nonparametric, non-asymptotic confidence
sequences. arXiv preprint arXiv:1810.08240 .
James W, Stein C (1961) Estimation with quadratic loss. Proceedings of the fourth Berkeley symposium on
mathematical statistics and probability, volume 1, 361–379.
JamiesonK,JainL(2018)Abanditapproachtomultipletestingwithfalsediscoverycontrol.arXiv preprint
arXiv:1809.02235 .
JamiesonK,MalloyM,NowakR,BubeckS(2014)lil’ucb:Anoptimalexplorationalgorithmformulti-armed
bandits. Conference on Learning Theory, 423–439.
Javanmard A, Montanari A (2016) Online rules for control of false discovery rate and false discovery
exceedance. arXiv preprint arXiv:1603.09000 .
Johari R, Koomen P, Pekelis L, Walsh D (2017) Peeking at a/b tests: Why it matters, and what to do
about it. Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, 1517–1525, KDD ’17 (New York, NY, USA: ACM), ISBN 978-1-4503-4887-4, URL
http://dx.doi.org/10.1145/3097983.3097992.
KalyanakrishnanS,TewariA,AuerP,StoneP(2012)Pacsubsetselectioninstochasticmulti-armedbandits.
ICML, volume 12, 655–662.

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |
| ---------------- | ---------- | -------------------- | --- | --- |
41
KaufmannE,Capp´eO,GarivierA(2014)Onthecomplexityofa/btesting.arXiv preprint arXiv:1405.3224
.
Kohavi R, Deng A, Frasca B, Walker T, Xu Y, Pohlmann N (2013) Online controlled experiments at large
scale. Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and
| data | mining, 1168–1176 | (ACM). |     |     |
| ---- | ----------------- | ------ | --- | --- |
LaiTL(2001)Sequentialanalysis:Someclassicalproblemsandnewchallenges.Statistica Sinica 11:303–408.
LaiTL,SiegmundD(1977)Anonlinearrenewaltheorywithapplicationstosequentialanalysisi.TheAnnals
of Statistics 5(5):946–954, URL http://dx.doi.org/10.1214/aos/1176343950.
Lai TL, Siegmund D (1979) A nonlinear renewal theory with applications to sequential analysis ii. The
Annals of Statistics 7(1):60–76, URL http://dx.doi.org/10.1214/aos/1176344555.
Lai TL, Wang JQ (1994) Asymptotic expansions for the distributions of stopped random walks and first
| passage   | times. The     | Annals of Probability | 1957–1992.  |            |
| --------- | -------------- | --------------------- | ----------- | ---------- |
| Lattimore | T, Szepesv´ari | C (2018) Bandit       | algorithms. | preprint . |
Lehmann EL, Romano JP, Casella G (1986) Testing statistical hypotheses, volume 150 (Wiley New York et
al).
Malek A, Katariya S, Chow Y, Ghavamzadeh M (2017) Sequential multiple hypothesis testing with type i
| error | control. Artificial | Intelligence | and Statistics, | 1468–1476. |
| ----- | ------------------- | ------------ | --------------- | ---------- |
Miller E (2010) How not to run an A/B test URL http://www.evanmiller.org/
| how-not-to-run-an-ab-test.html, |     |     | blog post. |     |
| ------------------------------- | --- | --- | ---------- | --- |
Miller E (2015) Simple sequential a/b testing URL http://www.evanmiller.org/
| sequential-ab-testing.html, |     |     | blog post. |     |
| --------------------------- | --- | --- | ---------- | --- |
Pollak M, Siegmund D (1975) Approximations to the expected sample size of certain sequential tests. The
Annals of Statistics 3(6):1267–1282, URL http://dx.doi.org/10.1214/aos/1176343284.
Robbins H (1970) Statistical methods related to the law of the iterated logarithm. The Annals of Mathe-
| matical | Statistics | 1397–1409. |     |     |
| ------- | ---------- | ---------- | --- | --- |
RobbinsH,SiegmundD(1974)Theexpectedsamplesizeofsometestsofpowerone.TheAnnalsofStatistics
415–436.

|     |     |     |     |     |     |     |     | Johari, | Pekelis, | and Walsh: AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------------------------- | --- |
42
Scott SL (2015) Multi-armed bandit experiments in the online service economy. Applied Stochastic Models
|     | in Business | and | Industry | 31(1):37–45. |     |     |     |     |     |     |     |
| --- | ----------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Siegmund D (1978) Estimation following sequential tests. Biometrika 65(2):341–349.
Siegmund D (1985) Sequential analysis: tests and confidence intervals (Springer).
Tang D, Agarwal A, O’Brien D, Meyer M (2010) Overlapping experiment infrastructure: More, better,
faster experimentation. Proceedings of the 16th ACM SIGKDD international conference on Knowledge
|     | discovery | and | data mining, | 17–26 | (ACM). |     |     |     |     |     |     |
| --- | --------- | --- | ------------ | ----- | ------ | --- | --- | --- | --- | --- | --- |
Wald A (1945) Sequential tests of statistical hypotheses. The Annals of Mathematical Statistics 16(2):117–
186.
Yang F, Ramdas A, Jamieson K, Wainwright MJ (2017) A framework for multi-a (rmed)/b (andit) testing
|     | with online | fdr | control. | arXiv | preprint | arXiv:1706.05378 |     | .   |     |     |     |
| --- | ----------- | --- | -------- | ----- | -------- | ---------------- | --- | --- | --- | --- | --- |
Zhao S, Zhou E, Sabharwal A, Ermon S (2016) Adaptive concentration inequalities for sequential decision
|          | problems. | Advances | in  | Neural     | Information | Processing |     | Systems, | 1343–1351. |     |     |
| -------- | --------- | -------- | --- | ---------- | ----------- | ---------- | --- | -------- | ---------- | --- | --- |
| Appendix | A:        | Proofs   | of  | optimality | results     |            |     |          |            |     |     |
Proof of Theorem 2. To establish asymptotic efficiency, given (M,α), it is sufficient to find
some θ , where for every feasible test (T∗,δ∗) with ν∗(θ )≥ν(θ ;M,α), we have that ρ∗(θ )≥
|     | 1   |     |     |     |     |     |     | 1   | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ρ(θ ;M,α)(1+o(1)).
1
SincethefamilyF canbeequivalentlyviewedasexponentialtiltsofanyθ(cid:48)∈Θ,weassumeθ =0
|     |     |     | θ   |     |     |     |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wlog and write I(θ):=I(θ,0). Theorem 2 of Lai and Siegmund (1977) can be used to establish
that a normal approximation holds asymptotically for P (δ(M,α)=0); in particular, we have that
θ
| for | any fixed | θ,  |     |                      |     |                     |     |     |          |     |     |
| --- | --------- | --- | --- | -------------------- | --- | ------------------- | --- | --- | -------- | --- | --- |
|     |           |     |     | (δ(M,α)=0)=Φ¯(cid:8) |     |                     |     |     | (cid:9)  |     |     |
|     |           |     | P   |                      |     | log(1/α)1/2B(M,α,θ) |     |     | (1+o(1)) |     |     |
θ
|     | (cid:16) | I(θ)3 | (cid:17)1/2(cid:16) |     |     | (cid:17) |     |     |     |     |     |
| --- | -------- | ----- | ------------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
whereB= M −I(θ)−1 .Ontheotherhand,standardresultsonthelogpartition
|          |         | θ2ψ(cid:48)(cid:48)(θ) |          | log(1/α)          |     |             |     |          |     |          |     |
| -------- | ------- | ---------------------- | -------- | ----------------- | --- | ----------- | --- | -------- | --- | -------- | --- |
| function | ψ imply |                        | that for | fixed (M,α),      |     |             |     |          |     |          |     |
|          |         |                        |          |                   |     |             |     | (cid:18) | Mθ2 | (cid:19) |     |
|          |         |                        |          | log(1/α)1/2B(θ)∼η |     | log(1/α)1/2 |     |          |     |          |     |
−η
|     |     |     |     |     |     | 2   |     | log(1/α) |     | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
as θ→0, where η and η are both positive constants. Combining the two results, it follows that
|     |               |     | 2         | 3        |      |                 |     |     |     |     |     |
| --- | ------------- | --- | --------- | -------- | ---- | --------------- | --- | --- | --- | --- | --- |
|     | (cid:113)     |     | (cid:112) |          |      |                 |     |     |     |     |     |
| for | θ = log(1/α)( |     | 2/η       | +η ), we | have | that eventually |     |     |     |     |     |
|     | 1             |     | 2         | 3        |      |                 |     |     |     |     |     |
M
|     |     |     |     |                 |     |     | (cid:16)(cid:112) |     | (cid:17) |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | ----------------- | --- | -------- | --- | --- |
|     |     |     |     | P (δ(M,α)=0)≤Φ¯ |     |     | 2log(1/α)         |     | :=β      |     |     |
|     |     |     |     | θ1              |     |     |                   |     |          | 1   |     |

| Johari, Pekelis, | and | Walsh: | AlwaysValidInference |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- |
43
i.e. the mSPRT has power at least 1−β at θ in the limit. Suppose that (T∗,δ∗) is another feasible
|     |     |     |     |     | 1   | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
test that achieves this power at θ . Once α is sufficiently small that 0<α+β <1, we can take
1 1
advantageofalowerboundontheexpectedsamplesizeofsequentialtestingprocedures(Hoeffding
| 1960) to | show | that for | any θ∈(0,θ |     | ),  |     |     |     |     |     |
| -------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |       | |log(α+β |     | )|− 1θ2ψ(cid:48)(cid:48)(θ)|log(α+β |     |     | )|1/2 |     |
| --- | --- | --- | ----- | -------- | --- | ----------------------------------- | --- | --- | ----- | --- |
|     |     |     | E     |          |     | 1                                   | 1   |     | 1     |     |
|     |     |     | (T∗)≥ |          |     | 2                                   |     |     |       |     |
|     |     |     | θ     |          |     | max{I(θ),I(θ,θ                      |     | )}  |       |     |
1
=I(θ)−1log(1/α)(1+o(1))
By continuity, the result holds at θ also. Comparing the above expression with (10) gives the
1
(cid:50)
| desired | inequality | on  | the relative | run-times |     | at θ . |     |     |     |     |
| ------- | ---------- | --- | ------------ | --------- | --- | ------ | --- | --- | --- | --- |
1
Proof of Proposition 3. Again wlog we assume θ =0. We fix θ(cid:54)=0, and for contradiction, we
0
suppose that there is some β <1 such that feasible tests with P (δ∗(M,α)=0)≤β exist in this
θ
limit. CombiningthisType II errorboundwiththeType Ierrorboundatα,the samelowerbound
of Hoeffding (1960) used above implies the existence of some κ such that
E (T∗)≥κlog(1/α)(1+o(1)).
θ
In the limit, this expectation exceeds M, so T∗ must certainly exceed M with positive probability.
(cid:50)
We now prove three lemmas that will let us prove Theorem 3 and Proposition 4.
| Lemma | 1.    |               |         |        |     |          |      |         |       |     |
| ----- | ----- | ------------- | ------- | ------ | --- | -------- | ---- | ------- | ----- | --- |
|       | Given | H,θ(cid:54)=θ | , there | exists | a   | λ>0 such | that | for any | 0<ε<1 |     |
0
|     |     |     | (cid:26)  |     |          |     | (cid:18) | (cid:19)(cid:27) |         |      |
| --- | --- | --- | --------- | --- | -------- | --- | -------- | ---------------- | ------- | ---- |
|     |     |     |           |     | log(1/α) |     | log(1/α) |                  |         |      |
|     |     |     | P |TH(α)− |     |          | |>ε |          |                  | =O(αλ). | (18) |
θ
|     |     |     |     |     | I(θ,θ | )   | I(θ,θ | )   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |       | 0   |       | 0   |     |     |
Proof. The proof follows by combining Lemmas 2 and 3 of Pollak and Siegmund (1975) with
Lemma 6 of Lai and Wang (1994). Lemma 3 of Pollak and Siegmund (1975) provides the upper
bound for the case TH(α)< log(1/α). The other comes from well known exponential concentration
I(θ,θ0)
bounds on the maximum deviation of a sample average from the corresponding mean (Lemma 2
of Pollak and Siegmund (1975)), combined with the method of proof of Lemma 6 of Lai and Wang
| (1994), | which | shows | similar bounds |     | for stopping | times | of    | the form |     |     |
| ------- | ----- | ----- | -------------- | --- | ------------ | ----- | ----- | -------- | --- | --- |
|         |       |       |                | T   | =inf{n≥n     |       | :nξ(S | )≥a},    |     |     |
|         |       |       |                | a   |              | a     | n     |          |     |     |
where ξ is a smooth, positive function and S is the sample average after n observations, and a
n
standard application of Jensen’s inequality to bound TH(α) by stopping times of the above form.
(cid:50)

|     |     |     |     |     |     |     |     | Johari, | Pekelis, | and Walsh: | AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | -------------------- | --- |
44
| Lemma 2. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let
|     |     |     |     |     | (cid:26) |     |     |     | (cid:27) |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- |
log(1/α)
|            |        |           |     | A=  | θ:I(θ,θ | )≥        |         |     | .    |                   |     |      |
| ---------- | ------ | --------- | --- | --- | ------- | --------- | ------- | --- | ---- | ----------------- | --- | ---- |
|            |        |           |     |     |         | 0         |         | M   |      |                   |     |      |
| Then there | holds: |           |     |     |         |           |         |     |      |                   |     |      |
|            |        | Mρ(M,α)=E |     |     | (cid:8) | E (TH(α)) | (cid:9) |     |      | (cid:0) A¯(cid:1) |     |      |
|            |        |           |     |     | 1       |           | +MPr    |     |      | +o(1).            |     | (19) |
|            |        |           |     |     | θ∼G     | A θ       |         |     | G(θ) |                   |     |      |
Proof. Let 0 < ε < 1. Define two times, n = (1 − ε)log(1/α)/I(θ,θ ), n = (1 +
|     |     |     |     |     |     |     | 1   |     |     |     | 0 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ε)log(1/α)/I(θ,θ ). For θ ∈ A¯, we have the following bounds, where the final inequality is an
0
| application | of (10) | in probability: |             |     |          |               |     |     |          |        |     |     |
| ----------- | ------- | --------------- | ----------- | --- | -------- | ------------- | --- | --- | -------- | ------ | --- | --- |
|             |         | M ≥E            | (T(M,α))≥(n |     |          | ∧M)P (TH(α)>n |     | )   |          |        |     |     |
|             |         |                 | θ           |     | 1        | θ             |     | 1   |          |        |     |     |
|             |         |                 |             |     | ≥(1−ε)MP | (TH(α)>n      |     |     |          |        |     |     |
|             |         |                 |             |     |          |               |     |     | )≥(1−ε)M | +o(1). |     |     |
|             |         |                 |             |     |          | θ             |     | 1   |          |        |     |     |
Let
|     |     |     |     | (cid:26) |     |     | (cid:18) |     | (cid:19)(cid:27) |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- | ---------------- | --- | --- | --- |
log(1/α)
|     |     |     | Bε= |     | θ:I(θ,θ | )≥(1+ε) |     |     |     | ,   |     |     |
| --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
0
M
| for θ∈Bε, | M ≥n | . Thus |     |     |     |     |     |     |     |     |     |     |
| --------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     |     |     |     |     |     | (cid:90) |     |     |     |     | (cid:90) |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- |
E (TH(α))≥E (T(M,α))≥E (T(n ,α))≥ TH(α)dP =E (TH(α))− TH(α)dP .
| θ   | θ   |     |     | θ   | 2   |          |     |     | θ   | θ   |          | θ   |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- |
|     |     |     |     |     |     | TH(α)≤n2 |     |     |     |     | TH(α)>n2 |     |
L2
| By Cauchy-Schwartz, |     | (10) | in  | and | Lemma | 1,  |     |     |     |     |     |     |
| ------------------- | --- | ---- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
TH(α)dP (cid:0)E (TH(α)2)P (TH(α)≥n (cid:1)1/2 =O(α−λ/2logα−1/2)=o(1).
|     |     |     | θ ≤ | θ   |     | θ   |     | 2 ) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TH(α)>n2
For θ∈A\Bε,
(cid:90)
| E (TH(α))≥E |     | (T(M,α))=E |     |     | (TH(α))+ |     |     | −TH(α)}dP |     |     |     |     |
| ----------- | --- | ---------- | --- | --- | -------- | --- | --- | --------- | --- | --- | --- | --- |
{n
| θ   |     | θ   |     | θ   |     |     |     | S   |     | θ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TH(α)≥n2
|     |     |     |     |     |            | (cid:90)   |     |           |            | (cid:90) |         |     |
| --- | --- | --- | --- | --- | ---------- | ---------- | --- | --------- | ---------- | -------- | ------- | --- |
|     |     |     |     | ≥E  | (TH(α))+   |            |     | −TH(α)}dP |            |          | TH(α)dP |     |
|     |     |     |     |     |            |            | {n  |           |            | −        |         |     |
|     |     |     |     | θ   |            |            |     | S         |            | θ        |         | θ   |
|     |     |     |     |     |            | M≤T<n2     |     |           |            | TH(α)>n2 |         |     |
|     |     |     |     | ≥E  | (TH(α))−(n | −M)+o(1)≥E |     |           | (TH(α))−εM |          | +o(1).  |     |
|     |     |     |     | θ   |            | 2          |     |           | θ          |          |         |     |
Putting the three cases together, we integrate over θ∼G to obtain (19), up to some error linear
in ε. To justify this step, it is easy to check that each term is finite. The result now holds on letting
| ε→0.     |     |     |     |       |            |                   |     |     |          |     |     | (cid:50) |
| -------- | --- | --- | --- | ----- | ---------- | ----------------- | --- | --- | -------- | --- | --- | -------- |
| Lemma 3. | Let |     |     |       |            |                   |     |     |          |     |     |          |
|          |     |     |     |       |            | (cid:32)(cid:114) |     |     | (cid:33) |     |     |          |
|          |     |     |     |       | (cid:90) 1 | 1                 |     |     |          |     |     |          |
|          |     |     |     | C(α)= |            | Φ log(1/α)(x2−1)  |     |     |          | dx, |     |          |
2
0
|     |     |     |     |      | (cid:90) 1 | (cid:16)(cid:112) |     |     | (cid:17) |     |     |     |
| --- | --- | --- | --- | ---- | ---------- | ----------------- | --- | --- | -------- | --- | --- | --- |
|     |     |     | C   | (α)= |            | Φ log(1/α)(x−1)   |     |     | dx.      |     |     |     |
f
0

| Johari, Pekelis, | and Walsh: |     | AlwaysValidInference |     |     |     |     |     |     |     |
| ---------------- | ---------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
45
For the prior G=N(0,τ2), let ν(M,α) be the average power of the mSPRT. If M =O(log(1/α)),
√
|     |     |     |     |     |     |     | (cid:18)   |     | (cid:19)1/2 |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- |
|     |     |     |     |     |     | 2   | 2 log(1/α) |     |             |     |
ν(M,α)∼C(α)
|     |     |     |     |     |     |     | τ   | M   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let ν (n,α) be the average power of the fixed-horizon test with sample size n. If n=Ω(log(1/α)),
f
√
|     |     |     |     |           |     |     | (cid:18)   |     | (cid:19)1/2 |     |
| --- | --- | --- | --- | --------- | --- | --- | ---------- | --- | ----------- | --- |
|     |     |     |     |           |     | 2   | 2 log(1/α) |     |             |     |
|     |     |     |     | ν (n,α)∼C |     | (α) |            |     |             |     |
|     |     |     |     | f         |     | f   |            |     |             |     |
|     |     |     |     |           |     |     | τ          | n   |             |     |
Proof. Wlog we suppose θ =0. We begin with the fixed horizon result. It is simple to show
0
(cid:112)
| that z 1−2α | ∼ 2log(1/α) |     | as α→0. |     | Hence |     |     |     |     |     |
| ----------- | ----------- | --- | ------- | --- | ----- | --- | --- | --- | --- | --- |
√
|       |               |          | (θ)=Φ¯(cid:0) |              |      | (cid:1) | =Φ¯(cid:0)   |     |         | (cid:1) |
| ----- | ------------- | -------- | ------------- | ------------ | ---- | ------- | ------------ | --- | ------- | ------- |
|       |               | ν        |               | |θ|          | n−z  |         | log(1/α)1/2S |     | (θ,n,α) |         |
|       |               |          | f             |              |      | 1−2α    |              |     | f       |         |
|       |               | (cid:16) |               | (cid:17)−1/2 | √    |         |              |     |         |         |
| where | S (θ,n,α)=|θ| |          | log(1/α)      |              | − 2. |         |              |     |         |         |
f
n
√
| Let B | ={θ : | A (θ,n,α)≥ |     | 2}.      | We split      | up  | the average |        | power as |     |
| ----- | ----- | ---------- | --- | -------- | ------------- | --- | ----------- | ------ | -------- | --- |
|       | f     | f          |     |          |               |     |             |        |          |     |
|       |       |            |     | (cid:90) | 1             |     | (cid:90)    |        | 1        |     |
|       |       |            | ν = | ν        | (θ) φ(θ/τ)dθ+ |     |             | −ν (θ) | φ(θ/τ)dθ |     |
|       |       |            | f   | f        | τ             |     |             | f      | τ        |     |
|       |       |            |     | Bf       |               |     | B¯          |        |          |     |
f
denoting the two terms by (i) and (ii) respectively. For θ ∈B , the standard tail bound on the
f
Φ¯(x)≤x−1φ(x)
| normal | CDF, |     |                        | gives |     |     |                            |     |     |     |
| ------ | ---- | --- | ---------------------- | ----- | --- | --- | -------------------------- | --- | --- | --- |
|        |      |     | Φ¯(cid:0) log(1/α)1/2S |       |     |     | (cid:1) ≤(4πlog(1/α))−1/2α |     |     |     |
(θ,n,α)
f
=o(α),
sothat(i)=o(α)aswell.Forterm(ii),wenotethatB¯ →{0}sothatφ(θ/τ)∼1.This,thechange
f
|             | (cid:16)     |     | (cid:17)−1/2 |       |          |     |               |     |      |     |
| ----------- | ------------ | --- | ------------ | ----- | -------- | --- | ------------- | --- | ---- | --- |
| of variable | x= 2log(1/α) |     |              | θ and | symmetry | of  | the integrand |     | give |     |
n
√
|     |     |       | 2   | 2 (cid:18) log(1/α) |     | (cid:19)1/2(cid:90) | 2                |     |     |         |
| --- | --- | ----- | --- | ------------------- | --- | ------------------- | ---------------- | --- | --- | ------- |
|     |     |       |     |                     |     |                     | Φ¯(cid:0)        |     |     | (cid:1) |
|     |     | (ii)∼ |     |                     |     |                     | (logα−1)1/2(x−1) |     |     | dx.     |
|     |     |       | τ   |                     | n   |                     |                  |     |     |         |
0
| The result | follows | on noting |     | Φ¯(cid:0) log(1/α)1/2(x−1) |     |     | (cid:1) =o(1) | when | x>1. |     |
| ---------- | ------- | --------- | --- | -------------------------- | --- | --- | ------------- | ---- | ---- | --- |
For the mSPRT, we use the normal approximation to the tail probabilities of the mSPRT stop-
ping time from Theorem 2 of Lai and Siegmund (1977) which, in the case of standard normal data,
gives
|     |     |     | P   | (T(α)>M)∼Φ¯(cid:8) |     |     | log(1/α)1/2S(θ,M,α) |     | (cid:9) |     |
| --- | --- | --- | --- | ------------------ | --- | --- | ------------------- | --- | ------- | --- |
θ
|     |     |     | (cid:110) (cid:16) |     | (cid:17) (cid:111) |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | ------------------ | --- | --- | --- | --- | --- |
where S(θ,M,α)= √1 θ2 log(1/α) −2 . The rest of the proof proceeds as for the fixed horizon
|     |     | 2 2 |     | √ M |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
test,exceptwithB={θ : S≥ 2}andchangesintheintegrandof(ii)asstatedintheproposition.
(cid:50)

|     |     |     |     |     |     |     |     | Johari, | Pekelis, | and | Walsh: AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --------------------------- | --- |
46
The next two results rely on equation (67) of Lai and Siegmund (1979), which gives an approx-
E
imation to (T(α)) as α→0. We re-print the equation here in our notation for easy reference:
θ
|       |                   |     |     | (cid:20) | (cid:18) logα−1(cid:19) |      | (cid:18) | 2π(H(cid:48)(θ))2(cid:19) |     |     | (cid:21) |            |
| ----- | ----------------- | --- | --- | -------- | ----------------------- | ---- | -------- | ------------------------- | --- | --- | -------- | ---------- |
|       |                   |     |     | 1        |                         |      |          |                           |     | σ2  | E[R2]    |            |
|       | )E (T(α))=logα−1+ |     |     |          |                         |      |          |                           |     |     |          |            |
| I(θ,θ |                   |     |     | log      |                         | −log |          |                           |     | −   | +        | +o(1) (20) |
0 θ 2 I(θ,θ ) ψ(cid:48)(cid:48)(θ) ψ(cid:48)(cid:48)(θ) 2E[R]
0
where prime and double prime denote first and second derivative, H(cid:48) is assumed to exist in a
neighborhood of θ, σ2=EX2−(EX )2, and R=inf{n:S >0}, the renewal time of S at 0.
|     |     |     |     |     | 1   |     |     | n   |     |     |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
The authors also note that while the renewal term is in general difficult to evaluate, it simplifies
| in the | normal | case | f (x)=φ(x−θ) |     | to the | following | expression: |     |     |     |     |     |
| ------ | ------ | ---- | ------------ | --- | ------ | --------- | ----------- | --- | --- | --- | --- | --- |
θ
|     |     |     |     | E[R2] |     |     |        | (cid:18) | (cid:19) |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ------ | -------- | -------- | --- | --- | --- |
|     |     |     |     |       |     | 1   |        | θ        |          |     |     |     |
|     |     |     |     |       | =2+ |     | θ2−2θB |          |          |     |     |     |
2E[R]
|     |     |     |     |     |     | 2   |     | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where
∞
(cid:88)
|     |     |     |     | B(u)= | k−1/2φ(uk1/2)−uΦ(−uk1/2), |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
k=1
| which | we use | in the | proof of | Proposition | 4   | below. |     |     |     |     |     |     |
| ----- | ------ | ------ | -------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Proof of Theorem 3. Combining Lemma 2 with (20), we find that, up to o(1),
|     |     |     | Mρ(M,α)=−2E |     |     | 1 I(θ,θ | )−1logh |     | (θ)+K(G,α) |     |     |     |
| --- | --- | --- | ----------- | --- | --- | ------- | ------- | --- | ---------- | --- | --- | --- |
|     |     |     |             |     | θ∼G | A       | 0       |     | γ          |     |     |     |
for some function K not depending on γ. The stated γ∗ is the minimizer of this expression. (cid:50)
Proof of Proposition 4. FromLemma3,weseethattomatchtheaveragepowerofthetruncated
mSPRT (ν =ν), the calibrated fixed-horizon test must have sample size O(M); i.e. ρ =O(1).
|         | f             |     |         |              |     |     |     |     |     |     |     | f   |
| ------- | ------------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Thus it | is sufficient |     | to show | that ρ=o(1). |     |     |     |     |     |     |     |     |
I(θ,0)=θ2/2.
Again we take θ =0 wlog, so for standard normal data We invoke Lemma 2 and
0
|        |         |       |         |        |             |     |     | (cid:16)  | (cid:17)1/2 |     |     |     |
| ------ | ------- | ----- | ------- | ------ | ----------- | --- | --- | --------- | ----------- | --- | --- | --- |
| attack | the two | terms | in that | result | separately. | Let | δ=  | 2log(1/α) |             | .   |     |     |
M
√
|     |     |     |     |     | (cid:90) δ 1 |     | 2   | 2 (cid:18) log(1/α) |     | (cid:19)1/2 |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ------------------- | --- | ----------- | --- | --- |
(A¯)=2
|     |     | Pr  |          |     | φ(θ/τ)dθ∼ |     |     |     |     |     | =o(1) |     |
| --- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | ----- | --- |
|     |     |     | θ∼N(0,τ) |     | τ         |     |     | τ   | M   |     |       |     |
0
| by similar | arguments |     | to those | in the | proof | of Lemma |     | 3.  |     |     |     |     |
| ---------- | --------- | --- | -------- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- |
The first term in Lemma 2 is more complicated. By equation (20) for the case of Normal data,
|     |     |     | E (T(α))=2θ−2log(1/α)+θ−2loglog(1/α)+D |     |     |     |     |     |     | θ−2log|θ| |     |     |
| --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     |     |     | θ                                      |     |     |     |     |     |     | 1         |     |     |
(21)
|     |     |     |     | θ−2+D |     |     | θ−1B(θ/2)+o(1) |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|     |     |     |     | +D    |     | +D  |                |     |     |     |     |     |
|     |     |     |     | 2     |     | 3 4 |                |     |     |     |     |     |
as α→0. It remains to show that each term in (21) has o(M) expectation on 1 . We focus on
A
| terms 1, | 3 & | 6 as the | remainder | are    | clearly    | lower    | order.   |     |                   |          |                           |     |
| -------- | --- | -------- | --------- | ------ | ---------- | -------- | -------- | --- | ----------------- | -------- | ------------------------- | --- |
| Term     | 1.  |          |           |        |            |          |          |     |                   |          |                           |     |
|          |     |          |           |        |            | (cid:18) | (cid:19) |     | (cid:26) (cid:18) | (cid:19) | (cid:18) (cid:19)(cid:27) |     |
|          |     |          |           |        | (cid:90) ∞ | 1        | θ        | 4   | τ                 | δ        | δ                         |     |
|          |     | E        |           | θ−2)=4 | θ−2        |          |          |     |                   | −Φ¯      |                           |     |
|          |     |          | (1        |        |            | φ        | dθ=      |     | φ                 |          |                           |     |
|          |     | θ∼N(0,τ) | A         |        |            | τ        | τ        | τ2  | δ                 | τ        | τ                         |     |
δ

Johari, Pekelis, and Walsh: AlwaysValidInference
47
which is bounded over α∈(0,1−ε). It follows that
√
2 2
(cid:18)
log(1/α)
(cid:19)1/2
E (1 θ−2)log(1/α)∼ M =o(M).
θ∼N(0,τ) A τ M
Term 3. By calculus,
(cid:90) ∞
E (1 θ−2log|θ|}∝ θ−2logθe−θ2/2τ2
θ∼N(0,τ) A
δ
1 (cid:20) 1 (cid:18) 1 δ2 (cid:19)
= √ Γ − , logδ
4 2τ 2 2τ2
(cid:18) 3 3 1 1 δ2 (cid:19)(cid:21)
+ δ−1MeijerG {{},{ , },{{0, , },{}}, ,
2 2 2 2 2τ2
The MeijerG term is asymptotically constant as δ→0, and
(cid:18) 1 δ2 (cid:19) √
Γ − , →2 2τδ−1.
2 2τ2
It follows that
(cid:20) (cid:18) (cid:19)(cid:21)
δlogδ
E (1 θ−2log|θ|)∝M K (Mlog(1/α))−1/2+K
θ∼N(0,τ) A 1 2 log(1/α)
where K are both constants depending on τ. Both terms in the bracketed sum clearly converge to
i
0 since δ→0.
Term 6. By standard bounds on the normal CDF, B(u)≥0 and
(cid:18)(cid:90) ∞ (cid:19)
B(u)≤u−2 x−3/2φ(ux1/2)dx+φ(u)
1
=θ−2(3φ(θ)−2θΦ(−θ))
Hence,
E (1 θ−1B(θ/2))≤K E (1 θ−3φ(θ/2))+K
θ∼N(0,τ) A 3 θ∼N(0,τ) A 4
≤K δ−2eK5δ2 −K Γ(0,K δ2)+K ,
4 7 6 4
where δ−2=M/log(α−2)=o(M) and Γ(0,K δ2)∼logK /δ2=O(logδ)=o(M). (cid:50)
6 6
Appendix B: Optimality for two-stream normal data
Given a choice of mixing distribution H, the two-stream p-values are derived from the mSPRT
which rejects the null if
(cid:32) (cid:33)n
(cid:90) f˜(S )
ΛH(S )= θ n dH(θ) (22)
n n f˜ (S )
Θ θ0 n
ever exceeds α, where S = 1 (cid:80)n W . First we notice that ΛH depends on the data only through
n n i=1 i n
(−1,1)TS ∼N(θ,2σ2/n), so the power and the run-time of this test do not depend on µ. Let
n

Johari, Pekelis, and Walsh: AlwaysValidInference
48
νH(θ;M,α), ρH(θ;M,α) be the power and average relative run-length of the truncated test. We
| say that | the relative | efficiency | of  | this test at | (M,α) is |     |
| -------- | ------------ | ---------- | --- | ------------ | -------- | --- |
ρ∗(θ,µ)
φH(M,α)=
|     |     |     |     |     | inf inf |     |
| --- | --- | --- | --- | --- | ------- | --- |
(T∗,δ∗)θ(cid:54)=θ0,µρH(θ;M,α)
where the infimum is taken over all tests with T∗ ≤M a.s., sup ν(θ ,µ)≤α, and for all θ(cid:54)=θ ,
µ 0 0
ν∗(θ,µ)≥νH(θ;M,α).
inf
µ
| Proposition | 5.  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
For any H, if α→0,M →∞ such that M =O(log(α−1)), we have φH(M,α)→1.
Proof. Fix µ=µ∗ arbitrarily. Then any (T∗,δ∗) satisfying the above conditions is also feasible
|     |     | ,µ=µ∗ |     |     | ,µ=µ∗. | (cid:50) |
| --- | --- | ----- | --- | --- | ------ | -------- |
for testing H :θ=θ against H :θ(cid:54)=θ The result follows by Theorem 2.
|     | 0   | 0   |     | 1   | 0   |     |
| --- | --- | --- | --- | --- | --- | --- |
Now we consider any prior for the pair (θ,µ) under H , such that θ∼N(0,τ2) marginally. For
1
normal mixtures H =N(0,γ2), let ρ (M,α) be the average power and relative run-time over this
γ
prior.
Proposition 6. To leading order as α→0,M →∞,M =O(log(α−1)), ρ is minimized by
γ
Φ(−b)
γ2∗=τ2
1φ(b)−Φ(−b)
b
|     | (cid:16) | (cid:17)1/2 |     |     |     |     |
| --- | -------- | ----------- | --- | --- | --- | --- |
2σ2logα−1
| where | b=  | .   |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
Mτ2
(cid:50)
| Proof. | Immediate | from | Theorem | 3.  |     |     |
| ------ | --------- | ---- | ------- | --- | --- | --- |
Now we compare the truncated mSPRT to the fixed-horizon t-test based on the difference
between the sample means in the two streams, which is calibrated to have the same average power
on this prior. Noting that the fixed-horizon sample size does not depend on µ, we see that Propo-
| sition 4           | carries over | to two-stream |        | normal data.   |     |     |
| ------------------ | ------------ | ------------- | ------ | -------------- | --- | --- |
| Appendix           | C: Multiple  | testing       |        |                |     |     |
| C.1. Commutativity |              | with          | always | valid p-values |     |     |
| Proposition        | 7.           |               |        |                |     |     |
Let (pi)m be always valid p-values, and let T be an arbitrary stopping time.
n i=1
Then the set of decisions obtained by applying Bonferroni to p controls FWER at level α.
T
p1,...,pm
Proof. For all θ, the variables satisfy the property that, for the truly null hypotheses
|     |     |     |     | T T |     |     |
| --- | --- | --- | --- | --- | --- | --- |
i with θi =θi, pi is marginally super-uniform. Hence there is a vector of (correlated) fixed-horizon
|     | 0 T |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
p-values with the same distribution as p , and so Bonferroni applied to the always valid p-values
T
| must control | FWER. |     |     |     |     | (cid:50) |
| ------------ | ----- | --- | --- | --- | --- | -------- |
Proposition 8. Let (pi)m be always valid p-values, and let T be an arbitrary stopping time. The
n i=1
set of decisions obtained by applying the BH-G procedure to p controls FDR at level α.
T

| Johari, | Pekelis, | and Walsh: |     | AlwaysValidInference |     |     |     |     |     |     |     |     |     |
| ------- | -------- | ---------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
49
We cannot use the same proof here as for Proposition 7, because Theorem 1.3 in Benjamini and
Yekutieli (2001), which establishes that BH-G controls FDR under arbitrary correlation, requires
that the fixed-horizon p-values be strictly uniform (rather than super-uniform). Instead, we rely
| on the | following | lemma.   |     |     |          |            |      |            |     |              |            |     |     |
| ------ | --------- | -------- | --- | --- | -------- | ---------- | ---- | ---------- | --- | ------------ | ---------- | --- | --- |
| Lemma  | 4.        |          |     |     |          |            |      |            |     |              |            |     |     |
|        |           |          |     |     |          | m (cid:90) | kα/m |            |     | m            |            |     |     |
|        |           |          |     |     | (cid:88) | 1          |      |            |     | α (cid:88) 1 |            |     |     |
|        |           |          |     |     | sup      |            |      | f(x)dx=    |     |              |            |     |     |
|        |           |          |     |     |          | k          |      |            | m   | k            |            |     |     |
|        |           |          |     |     | f∈F k=1  | (k−1)α/m   |      |            |     | k=1          |            |     |     |
|        |           | :[0,1]→R |     |     |          | (cid:82)x  |      |            |     |              |            |     |     |
| where  | F ={f     |          |     | :   | F(x)=    | f(x)dx≤x   |      | , F(1)=1}, |     | m≥1,         | and 0≤α≤1. |     |     |
|        |           |          |     | +   |          | 0          |      |            |     |              |            |     |     |
Proof. Since f ∈ F are bounded, we restate the optimization in terms of F = F(kα), and
k
m
F ≡0,
0
m
(cid:88)1
|     |     |     |     |     | sup | (F  | −F  | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k k−1
k
F1,...,Fmk=1
kα
|     |           |     |               | subject | to  | 0≤F | ≤   | , F | ≥F  | k=1,...,m. |     |     |     |
| --- | --------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |           |     |               |         |     | j   | m   | k   | k−1 |            |     |     |     |
| The | objective | can | be rearranged |         | as  |     |     |     |     |            |     |     |     |
m−1
|     |     |     |     |     |     | (cid:88) | 1   |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |          |     | F + | F   |     |     |     |     |
|     |     |     |     |     |     |          |     | k   | m   |     |     |     |     |
|     |     |     |     |     |     | k(k+1)   |     |     | m   |     |     |     |     |
k=1
| which | is clearly | maximized |     | by  | F = | kα for | all k. |     |     |     |     |     | (cid:50) |
| ----- | ---------- | --------- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | -------- |
k
m
Proof of Proposition 8. Adapting the proof given in Benjamini and Yekutieli (2001) now is
straight-forward. Translating into the sequential notation of this paper, the only non-immediate
| step | is to show |     |     |                     |                 |      |     |     |            |             |         |     |     |
| ---- | ---------- | --- | --- | ------------------- | --------------- | ---- | --- | --- | ---------- | ----------- | ------- | --- | --- |
|      |            |     |     | (cid:88)1(cid:88) m | m               |      |     |     |            |             |         |     |     |
|      |            |     |     |                     | P(cid:0)        |      |     |     |            |             | (cid:1) |     |     |
|      |            |     |     |                     |                 | Ti≤T | <Ti | , T | ≤T         | <T+ , T ≤∞  |         |     |     |
|      |            |     |     |                     | k               | k    |     | k−1 | r          | r           |         |     |     |
|      |            |     |     | k=1                 | r=k             |      |     |     |            |             |         |     |     |
|      |            |     |     | (cid:88)1 m         | (cid:18) (k−1)α |      |     | kα  | (cid:19) α | (cid:88)1 m |         |     |     |
P
|     |     |     | ≤   |     |     |     | ≤pi | ≤   | ≤   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | k   | m   | T   | m   | m   | k   |     |     |     |
|     |     |     |     | k=1 |     |     |     |     |     | k=1 |     |     |     |
for all truly null hypotheses i. The first inequality is a restatement of definitions, and the second
follows from Lemma 4 since by always-validity pi is super-uniform. (cid:50)
T
Proof of Theorem 5. We assume wlog that the truly null hypotheses are i=1,...,m . Letting
0
V denote the number of true null rejected at n, the FDR can be expanded as
n
|     | (cid:32) | m          |     |       |      | (cid:33) | m0       | m          |               |       |           |              |     |
| --- | -------- | ---------- | --- | ----- | ---- | -------- | -------- | ---------- | ------------- | ----- | --------- | ------------ | --- |
|     |          | (cid:88) 1 |     |       |      |          | (cid:88) | (cid:88) 1 |               |       |           |              |     |
|     | E        |            | V 1 |       | 1    |          | =        |            | P(cid:0) Ti≤T | , T ≤ | T <T+ , T | <∞ (cid:1) . |     |
|     |          |            | T   |       | +}   | T<∞      |          |            |               | r     |           |              |     |
|     |          | r          |     | {Tr ≤ | T<Tr |          |          | r          | r             |       | r         |              |     |
|     |          | r=1        |     |       |      |          | i=1      | r=1        |               |       |           |              |     |
Note that the sets {T ≤ T <T+} are disjoint and cover any location of T. Consider the terms in
r
r
the sum over i∈I and i∈/I separately. For i∈/I, we bound the probability in the third equality by
|          |      |        | (cid:16) |      |          | (cid:12)      |       |      | (cid:17) αr   | (cid:16) | (cid:12)          |        | (cid:17) |
| -------- | ---- | ------ | -------- | ---- | -------- | ------------- | ----- | ---- | ------------- | -------- | ----------------- | ------ | -------- |
| P(cid:0) | Ti≤T |        | (cid:1)P |      | <T+      | (cid:12) Ti≤T |       |      |               | P        | <T+ (cid:12) Ti≤T |        |          |
|          |      | , T <∞ |          | T ≤T |          |               | ,     | T <∞ | ≤             | T ≤T     |                   | , T <∞ |          |
|          | r    |        |          | r    | r        | (cid:12) r    |       |      | M             | r        | r (cid:12) r      |        |          |
|          |      |        |          | αr   | (cid:16) |               |       |      | (cid:12)      |          | (cid:17)          |        |          |
|          |      |        | =        | P    | (T       | )−i ≤         | T <(T | )−i+ | (cid:12) Ti≤T | , T <∞   |                   |        |          |
|          |      |        |          |      | r−1      | 0             |       | r−1  | 0 (cid:12)    | r        |                   |        |          |
M

|     |     |     |     |     |     | Johari, | Pekelis, and | Walsh: AlwaysValidInference |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------ | --------------------------- | --- |
50
where the first inequality follows from always-validity of sequential p-values, and the last equality
because the modified BH procedure on the m−1 hypothesis other than the ith makes equivalent
| rejections | at time | T when | Ti≤T. |     |     |     |     |     |     |
| ---------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
r
| For i∈I, | arguing | as  | in the             | proof | of Proposition | 8 shows    |                     |     |     |
| -------- | ------- | --- | ------------------ | ----- | -------------- | ---------- | ------------------- | --- | --- |
|          |         |     | m                  |       |                |            | m                   |     |     |
|          |         |     | (cid:88)1 P(cid:0) |       |                |            | (cid:1) α (cid:88)1 |     |     |
|          |         |     |                    | Ti≤T  | , T ≤ T        | <T+ , T <∞ | ≤                   | .   |     |
|          |         |     |                    | r     | r              | r          |                     |     |     |
|          |         |     | r                  |       |                |            | m                   | k   |     |
|          |         |     | r=1                |       |                |            | k=1                 |     |     |
The proof is completed on application of (14) to the terms in the first expansion with i∈/ I and
| re-ordering | of the   | resulting | terms. |        |           |     |     |     | (cid:50) |
| ----------- | -------- | --------- | ------ | ------ | --------- | --- | --- | --- | -------- |
| BH-I        | does not | commute   | with   | always | validity: |     |     |     |          |
| Example     | 1.       |           |        |        |           |     |     |     |          |
Let m=4, with p , i≤3, be a.s. constant across n with p ∼U(0,1), and let p =
|     |     |     |     | i,n |     |     |     | 1,1 | 4,1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,p 2,n =0forn≥2.Thesearefeasiblealwaysvalidp-valueprocesseswhenthe1st3hypothesesare
null and the 4th is non-null. Consider the following stopping time: T =1 if any null hypothesis is
less than α/4, any two nulls are less than α/2, or all three nulls are less than 3α/4, and otherwise
T =2. Straightforward calculation shows the standard BH procedure applied to p gives an FDR
T
α(2−9α+45α2)>α
| of α+ |     |     |     | for all | 0<α<1. |     |     |     |     |
| ----- | --- | --- | --- | ------- | ------ | --- | --- | --- | --- |
16
C.2. q-values
| For Bonferroni, | the | q-values |     | are given | by  |     |     |     |     |
| --------------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- |
qi=(pim)∧1.
| For BH | with independence |     | or  | general | dependence | respectively, |     |     |     |
| ------ | ----------------- | --- | --- | ------- | ---------- | ------------- | --- | --- | --- |
(cid:80)m
|     |     |     |     | (cid:18) | p(k)m (cid:19) | (cid:18) p(k)m | 1/r (cid:19) |     |     |
| --- | --- | --- | --- | -------- | -------------- | -------------- | ------------ | --- | --- |
q(j)=min
|     |     |     |     |     | ∧1 or | min | r=1 | ∧1. |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     | k     | k   |     |     |     |
|     |     |     |     | k≥j |       | k≥j |     |     |     |
The q-values for both Bonferroni and BH-I are currently displayed on the industry platform in
| different | contexts. |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| C.3. FCR  | control   |     |     |     |     |     |     |     |     |
Proof of Theorem 4. By Lemma 1 in Benjamini and Yekutieli (2005),
(cid:88)(cid:88)1 m m
|     |     |      |     |     | P(|J∪SBH|=r,i∈J∪SBH,θi∈/C˜I |     |     | i   |     |
| --- | --- | ---- | --- | --- | --------------------------- | --- | --- | --- | --- |
|     |     | FCR= |     |     |                             |     |     | )   |     |
r
i=1 r=1
On the event i∈J ∪SBH, there are two possibilities. If i∈SBH, we can say RBH ≤|J ∪S |. If
BH
i∈/SBH, we can say further that RBH+1≤|J∪S |. In either case, it follows that CIi(1−α|J∪
BH
| |/m)⊂C˜I | i   |        |         |     |         |     |     |     |     |
| -------- | --- | ------ | ------- | --- | ------- | --- | --- | --- | --- |
| S        | ,   | and so | the FCR | is  | at most |     |     |     |     |
BH
m m
(cid:88)(cid:88)1
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m))
r
i=1 r=1

| Johari, Pekelis, | and Walsh: | AlwaysValidInference |     |     |     |
| ---------------- | ---------- | -------------------- | --- | --- | --- |
51
Case 1: i∈/J.
{|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m)}
={|J∪(SBH)−i|=r−1,pi≤αr/m,θi∈/CIi(1−αr/m)}
0
⊂{|J∪(SBH)−i|=r−1,θi∈/CIi(1−αr/m)}
0
| These two | events | are independent, | so  |     |     |
| --------- | ------ | ---------------- | --- | --- | --- |
(cid:88)1 m
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m))
r
r=1
(cid:88)1 m
P(|J∪(SBH)−i|=r−1)P(θi∈/CIi(1−αr/m))
≤
|     |     | r   | 0   |     |     |
| --- | --- | --- | --- | --- | --- |
r=1
|     |     | α m |     | α   |     |
| --- | --- | --- | --- | --- | --- |
(cid:88) P(|J∪(SBH)−i|=r−1)=
≤
|     |     | m   | 0   | m   |     |
| --- | --- | --- | --- | --- | --- |
r=1
Case 2: i∈J.
m
(cid:88)1
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m))
r
r=1
m
(cid:88)1
|     | ≤   | P(|J∪SBH|=r,θi∈/CIi(1−αr/m)) |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- |
r
r=1
m
(cid:88)1
|     | =   | P(|J∪SBH|=r|θi∈/CIi(1−αr/m))P(θi∈/CIi(1−αr/m)) |     |     |     |
| --- | --- | ---------------------------------------------- | --- | --- | --- |
r
r=1
m
α (cid:88)
|     | ≤   | P(|J∪SBH|=r|θi∈/CIi(1−αr/m)) |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- |
m
r=1
Since SBH is a function only of the p-values and the data streams are independent, the events
{|J∪SBH|=r} and {θi∈/CIi(1−αr/m))} are conditionally independent given pi. Hence,
P(|J∪SBH|=r|θi∈/CIi(1−αr/m))≤maxP(|J∪SBH|=r|pi=ρ)
ρ
It is easily seen that this maximum must be attained at either ρ=0 or ρ=1, so
P(|J∪SBH|=r|θi∈/CIi(1−αr/m))
≤P(|J∪SBH|=r|pi=0)+P(|J∪SBH|=r|pi=1)
=P(|J∪(SBH)−i\i|=r−1)+P(|J∪(SBH)−i\i|=r−1)
|     |     |     | 0   |     | 1   |
| --- | --- | --- | --- | --- | --- |
Thus
(cid:88)1 m
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m))
r
r=1
(cid:40) (cid:41)
|     | α   | m                     |     | m                    |     |
| --- | --- | --------------------- | --- | -------------------- | --- |
|     |     | (cid:88)              |     | (cid:88)             |     |
|     | ≤   | P(|J∪(SBH)−i\i|=r−1)+ |     | P(|J∪(SBH)−i\i|=r−1) |     |
|     | m   |                       | 0   |                      | 1   |
|     |     | r=1                   |     | r=1                  |     |
2α
=
m

|     |     |     |     |     |     |     |     |     | Johari, Pekelis, and | Walsh: AlwaysValidInference |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --------------------------- | --- | --- |
52
(cid:50)
| Summing | over | all | i now | gives the | desired | result. |     |     |     |     |     |     |
| ------- | ---- | --- | ----- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Proof of Theorem 6. By the same argument as in Theorem 4, we find that the FCR is at most
|     |     | (cid:88)(cid:88)1 | m m |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m),T
<∞)
|     |         |       |       | r       | T   |           | T   |     | T   |     |     |     |
| --- | ------- | ----- | ----- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
|     |         | i=1   | r=1   |         |     |           |     |     |     |     |     |     |
|     | Case 1: | i∈/J. | As in | Theorem | 4,  | we obtain |     |     |     |     |     |     |
m
(cid:88)1
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m),T
<∞)
|     |     |     |     | r   | T   |     |     | T   | T   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r=1
m
(cid:88)1
|     |     |     | ≤   | P(|J∪(SBH)−i|=r−1,θi∈/CIi(1−αr/m),T |     |     |     |     |     | <∞) |     |     |
| --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | r                                   |     | T 0 |     |     | T   |     |     |     |
r=1
m
(cid:88)1
|     |     |     | =   | P((T | )−i,J | ≤T  | <(T | )−i,J+,Ti,θi | ≤T <∞) |     |     |     |
| --- | --- | --- | --- | ---- | ----- | --- | --- | ------------ | ------ | --- | --- | --- |
|     |     |     |     |      | r−1   |     | r−1 |              |        |     |     |     |
|     |     |     |     | r    | 0     |     |     | 0            | r      |     |     |     |
r=1
m
|     |     |     |     | α (cid:88) |     |          |     |              |        |     |     |     |
| --- | --- | --- | --- | ---------- | --- | -------- | --- | ------------ | ------ | --- | --- | --- |
|     |     |     | ≤   | P((T       |     | )−i,J ≤T | <(T | )−i,J+|Ti,θi | ≤T <∞) |     |     |     |
|     |     |     |     |            | r−1 |          |     | r−1          |        |     |     |     |
|     |     |     |     | m          |     | 0        |     | 0            | r      |     |     |     |
r=1
α
≤
m
|     | Case 2: | i∈J. | As before, |     |     |     |     |     |     |     |     |     |
| --- | ------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m
(cid:88)1
P(|J∪SBH|=r,i∈J∪SBH,θi∈/CIi(1−αr/m))
|     | r   |     | T   |     | T   |     | T   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r=1
m
α (cid:88)
|     | ≤   |     | P(|J∪SBH|=r|θi∈/CIi(1−αr/m)) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | m   |                              | T   |     | T   |     |     |     |     |     |     |
r=1
m
α (cid:88)
|     | =   |     | P(|J∪SBH|=r|Ti,θi |     |     | ≤T  | <∞) |     |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |                   | T   |     | r   |     |     |     |     |     |     |
m
r=1
m
α (cid:88)
|     | ≤   |     | maxP(|J∪SBH|=r|pi |     |     | =ρ,Ti,θi |     | ≤T  | <∞) |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|     |     |     |                   |     | T   | T        | r   |     |     |     |     |     |
|     |     | m   | ρ                 |     |     |          |     |     |     |     |     |     |
r=1
|     |     | (cid:40) | m        |     |     |     |     |     | m        |     |     | (cid:41) |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- |
|     |     | α        | (cid:88) |     |     |     |     |     | (cid:88) |     |     |          |
≤ P(|J∪(SBH)−i\i|=r−1|Ti,θi ≤T <∞)+ P(|J∪(SBH)−i\i|=r−1|Ti,θi ≤T <∞)
|     |     | m   |     | T   | 0   |     | r   |     |     | T 1 | r   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | r=1 |     |     |     |     |     | r=1 |     |     |     |
m
α(cid:110)(cid:88)
|     | =   |     | P((T | )−i,J | ≤T  | <(T | )−i,J+|Ti,θi |     | ≤T <∞) |     |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | ------------ | --- | ------ | --- | --- | --- |
|     |     |     |      | r−1   |     | r−1 |              |     |        |     |     |     |
|     |     | m   |      | 0     |     |     | 0            | r   |        |     |     |     |
r=1
m
|     |     |     |     | (cid:88) |       |     |     |              |        | (cid:111) |     |     |
| --- | --- | --- | --- | -------- | ----- | --- | --- | ------------ | ------ | --------- | --- | --- |
|     |     |     | +   | P((T     | )−i,J | ≤T  | <(T | )−i,J+|Ti,θi | ≤T <∞) |           |     |     |
|     |     |     |     |          | r−1   |     | r−1 |              |        |           |     |     |
|     |     |     |     |          | 1     |     |     | 1            | r      |           |     |     |
r=1
2α
≤
m
(cid:50)
| Finally | we  | sum over | i.  |     |     |     |     |     |     |     |     |     |
| ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
