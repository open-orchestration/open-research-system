Time-uniform, nonparametric, nonasymptotic confidence sequences
Steven R. Howard1 Aaditya Ramdas2,3 Jon McAuliffe1,4 Jasjeet Sekhon1,5
Departments of Statistics1 and Political Science5, UC Berkeley
Departments of Statistics and Data Science2 and Machine Learning3, Carnegie Mellon
The Voleon Group4
{stevehoward,jonmcauliffe,sekhon}@berkeley.edu, aramdas@stat.cmu.edu
August 9, 2022
Abstract
Aconfidencesequenceisasequenceofconfidenceintervalsthatisuniformlyvalidoveranunbounded
timehorizon. Ourworkdevelopsconfidencesequenceswhosewidthsgotozero,withnonasymptoticcov-
erage guarantees under nonparametric conditions. We draw connections between the Cram´er-Chernoff
method for exponential concentration, the law of the iterated logarithm (LIL), and the sequential
probability ratio test—our confidence sequences are time-uniform extensions of the first; provide tight,
nonasymptotic characterizations of the second; and generalize the third to nonparametric settings, in-
cluding sub-Gaussian and Bernstein conditions, self-normalized processes, and matrix martingales. We
illustrate the generality of our proof techniques by deriving an empirical-Bernstein bound growing at a
LILrate,aswellasanovelupperLILforthemaximumeigenvalueofasumofrandommatrices. Finally,
we apply our methods to covariance matrix estimation and to estimation of sample average treatment
effect under the Neyman-Rubin potential outcomes model.
1 Introduction
It has become standard practice for organizations with online presence to run large-scale randomized ex-
periments, or “A/B tests”, to improve product performance and user experience. Such experiments are
inherently sequential: visitors arrive in a stream and outcomes are typically observed quickly relative to
the duration of the test. Results are often monitored continuously using inferential methods that assume a
fixed sample, despite the known problem that such monitoring inflates Type I error substantially (Armitage
et al., 1969; Berman et al., 2018). Furthermore, most A/B tests are run with little formal planning and
fluid decision-making, compared to clinicaltrials or industrial quality control, the traditionalapplications of
sequential analysis.
This paper presents methods for deriving confidence sequences as a flexible tool for inference in sequential
experiments(DarlingandRobbins,1967a;Lai,1984;JennisonandTurnbull,1989). Forα∈(0,1),a(1−α)-
confidencesequenceisasequenceofconfidencesets(CI )∞ ,typicallyintervalsCI =(L ,U )⊆R,satisfying
t t=1 t t t
a uniform coverage guarantee: after observing the tth unit, we calculate an updated confidence set CI for
t
the unknown quantity of interest θ , with the uniform coverage property
t
P(∀t≥1:θ ∈CI )≥1−α. (1)
t t
With only a uniform lower bound (L ), i.e., if U ≡ ∞, we have a lower confidence sequence. Likewise, if
t t
L ≡ −∞ we have an upper confidence sequence given by (U ). Theorems 1 to 3 and Lemma 2 are our key
t t
tools for constructing confidence sequences. All build upon the general framework for uniform exponential
concentration introduced in Howard et al. (2020), which means our techniques apply in diverse settings:
scalar, matrix, and Banach-space-valued observations, with possibly unbounded support; self-normalized
bounds applicable to observations satisfying weak moment or symmetry conditions; and continuous-time
scalar martingales. Our methods allow for flexible control of the “shape” of the confidence sequence, that
is, how the sequence of intervals shrinks in width over time. As a simple example, given a sequence of i.i.d.
1
2202
guA
6
]TS.htam[
9v04280.0181:viXra

|                   | 1.0 |     |     |     |     | .borp egarevocsim evitalumuC |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
| sdnuob ecnedifnoC |     |     |     |     |     | 0.6                          |     |     |     |     |     |
0.5
0.4
0.0

|     | −0.5 | Empirical mean       |     |     |     | 0.2 |     |                      |     |     |     |
| --- | ---- | -------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
|     | −1.0 |                      |     |     |     | 0.0 |     |                      |     |     |     |
|     | 101  | 102                  | 103 | 104 | 105 |     | 101 | 102                  | 103 | 104 | 105 |
|     |      | Number of samples, t |     |     |     |     |     | Number of samples, t |     |     |     |
Pointwise CLT        Pointwise Hoeffding        Linear boundary        Curved boundary
Figure 1: Left panel shows 95% pointwise confidence intervals and uniform confidence sequences for the mean of a
Rademacher random variable, using one simulation of 100,000 i.i.d. draws. Right panel shows cumulative chance of
miscoverage based on 10,000 replications; flat grey line shows the nominal target level 0.05. The CLT intervals are
asymptotically pointwise valid (these are similar to the exact binomial confidence intervals, which are nonasymp-
totically pointwise valid). The pointwise Hoeffding intervals are nonasymptotically pointwise valid. The confidence
sequence based on a linear boundary, as in Lemma 1, is valid uniformly over time and nonasymptotically, but does
not shrink to zero width. Finally, the confidence sequence based on a curved boundary is valid uniformly and
nonasymptotically, while also shrinking towards zero width; here we use the two-sided normal mixture boundary,
| (14), | qualitatively | similar | to the stitched | bound | (2). |     |     |     |     |     |     |
| ----- | ------------- | ------- | --------------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
observations(X )∞ froma1-sub-Gaussiandistributionwhosemeanµwewouldliketoestimate,Theorem1
t t=1
yields the following (1−α)-confidence sequence for µ, a special case of the more general bound (10):
(cid:114)
|     |     |     | (cid:80)t | X    | loglog(2t)+0.72log(10.4/α) |     |     |     |     |     |     |
| --- | --- | --- | --------- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | i=1       | i    |                            |     |     |     |     |     |     |
|     |     |     |           | ±1.7 |                            |     |     |     | .   |     | (2) |
|     |     |     | t         |      |                            |     | t   |     |     |     |     |
(cid:112)
The O( t−1loglogt) asymptotic rate of this bound matches the lower bound implied by the law of the
iterated logarithm (LIL), and nonasymptotic bounds of this form are called finite LIL bounds (Jamieson
et al., 2014).
| We  | develop confidence | sequences | that | possess | the following |     | properties: |     |     |     |     |
| --- | ------------------ | --------- | ---- | ------- | ------------- | --- | ----------- | --- | --- | --- | --- |
(P1) Nonasymptotic and nonparametric: our confidence sequences offer coverage guarantees for all
sample sizes, without exact distributional assumptions or asymptotic approximations.
(P2) Unbounded sample size: ourmethodsdonotrequireafinalsamplesizetobechosenaheadoftime.
They may be tuned for a planned sample size but always permit additional sampling.
(P3) Arbitrary stopping rules: we make no assumptions on the stopping rule used by an experimenter
|     | to decide | when to | end the experiment, |     | or when | to act | on certain | inferences. |     |     |     |
| --- | --------- | ------- | ------------------- | --- | ------- | ------ | ---------- | ----------- | --- | --- | --- |
(P4) Asymptotically zero width: the interval widths of our confidence sequences shrink towards zero at
√
|     | a 1/ t | rate, ignoring | log factors, | just | as with | pointwise | confidence |     | intervals. |     |     |
| --- | ------ | -------------- | ------------ | ---- | ------- | --------- | ---------- | --- | ---------- | --- | --- |
These properties give us strong guarantees and broad applicability. An experimenter may always choose to
gather more samples, and may stop at any time according to any rule—the resulting inferential guarantees
holdunderthestatedassumptionswithoutanyapproximations. Ofcourse,thisflexibilitycomeswithacost:
our intervals are wider than those that rely on asymptotics or make stronger assumptions, for example, a
known stopping rule. Typical, fixed-sample confidence intervals derived from the central limit theorem do
notsatisfyanyof(P1)-(P3),andaccommodatinganyonepropertynecessitateswiderintervals; weillustrate
this in Figure 1. It is perhaps surprising that these four properties come at a numerical cost of less than
doubling the fixed-sample, asymptotic interval width—the discrete mixture bound illustrated in Figure 9
stays within a factor of two of the fixed-sample CLT bounds over five orders of magnitude in time.
2

1.1 Related work
The idea of a confidence sequence goes back at least to Darling and Robbins (1967a). They are called
repeated confidence intervals by Jennison and Turnbull (1984, 1989) (with a focus on finite time horizons)
andalways-validconfidenceintervals byJoharietal.(2015). Theyaresometimeslabeledanytimeconfidence
intervals in the machine learning literature (Jamieson and Jain, 2018).
Prior work on sequential inference is often phrased in terms of a sequential hypothesis test, defined as a
stopping rule and an accept/reject decision variable, or in terms of an always-valid p-value (Johari et al.,
2015). In Section 6 we discuss the duality between confidence sequences, sequential hypothesis tests, and
always-validp-values. WeshowinLemma3thatdefinition(1)isequivalenttorequiringP(θ ∈CI )≥1−α
τ τ
for all stopping times τ, or even for all random times τ, not necessarily stopping times. Hence the choice of
definition (1) over related definitions in the literature is one of convenience.
Recent interest in confidence sequences has come from the literature on best-arm identification with fixed
confidence for multi-armed bandit problems. Garivier (2013), Jamieson et al. (2014), Kaufmann et al.
(2016),andZhaoetal.(2016)presentmethodssatisfyingproperties(P1)-(P4)forindependent,sub-Gaussian
observations. Our results are sharper and more general, and our Bernstein confidence sequence scales with
thetruevarianceinnonparametricsettings. Confidencesequencesareakeyingredientinbest-armselection
algorithms(JamiesonandNowak,2014)andrelatedmethodsforsequentialtestingwithmultiplecomparisons
(Yang et al., 2017; Malek et al., 2017; Jamieson and Jain, 2018). Our results improve and generalize such
methods.
MaurerandPontil(2009)andAudibertetal.(2009)proveempirical-Bernsteinboundsforfixedtimesorfinite
timehorizons. Ourempirical-Bernsteinboundholdsuniformlyoverinfinitetime. Balsubramani(2014)takes
a different approach to deriving confidence sequences satisfying properties (P1)-(P4) by lower bounding a
mixturemartingale. ThisworkwasextendedinBalsubramaniandRamdas(2016)toanempirical-Bernstein
bound,theonlyinfinite-horizon,empirical-Bernsteinconfidencesequenceweareawareofinpriorwork. Our
resultremovesamultiplicativepre-factorandyieldssharperbounds. Weemphasizethatourprooftechnique
is quite different from all three of these existing empirical-Bernstein bounds; see Appendix A.8.
The simplest confidence sequence satisfying properties (P1)-(P3) follows by inverting a suitably formulated
sequential probability ratio test (SPRT, (Wald, 1945)), such as in Section 3.6 of Howard et al. (2020). Wald
worked in a parametric setting, though it is known that the normal SPRT depends only on sub-Gaussianity
(e.g., Robbins (1970)). The resulting confidence sequence does not shrink towards zero width as t → ∞
(property P4), a problem which stems from the choice of a single point alternative λ. Numerous extensions
havebeendevelopedtoremedythisdefect,andourworkismostcloselytiedtotwoapproaches. First,inthe
(cid:82) (cid:81)
method of mixtures, one replaces the likelihood ratio with a mixture [f (X )/f (X )]dF(λ), which is
i λ i 0 i
still a martingale (Ville, 1939; Wald, 1945; Darling and Robbins, 1968; Robbins and Siegmund, 1969, 1970;
Robbins, 1970; Lai, 1976b; de la Pen˜a et al., 2007; Balsubramani, 2014; Bercu et al., 2015; Kaufmann and
Koolen, 2018). Second, epoch-based analyses choose a sequence of point alternatives λ ,λ ,... approaching
1 2
the null value, with corresponding error probabilities α ,α ,... approaching zero so that a union bound
1 2
yieldsthedesirederrorcontrol(DarlingandRobbins,1967b;RobbinsandSiegmund,1968;Kaufmannetal.,
2016).
The literature on self-normalized bounds makes extensive use of the method of mixtures, sometimes called
pseudo-maximization (de la Pen˜a et al., 2004, 2007; de la Pen˜a, Klass and Lai, 2009; de la Pen˜a, Lai and
Shao, 2009; Garivier, 2013); these works introduced the idea of using a mixture to bound a quantity with
a random intrinsic time V . These results are mostly given for fixed samples or finite time horizon, though
t
de la Pen˜a et al. (2004, Eq. 4.20) includes an infinite-horizon curve-crossing bound. Lai (1976b) treats
confidencesequencesfortheparameterofanexponentialfamilyusingmixturetechniquessimilartothoseof
Section3.2. Likemostworkonthemethodofmixtures,Lai’sworkfocusedontheparametricsetting(which
we discuss in Section 4.4), while we focus on the application of mixture bounds to nonparametric settings.
Johari et al. (2017) adopt the mixture approach for a commercial A/B testing platform, where properties
(P2) and (P3) are critical to provide an “off-the-shelf” solution for a variety of clients. Their application
relies on asymptotics which lack rigorous justification. In Section 4.2 we give nonasymptotic justification
for a similar confidence sequence under a finite-sample randomization inference model, and in Section 5 we
demonstrate how our methods control Type I error in situations where asymptotics fail.
3

1.2 Outline
Weorganizeourresultsusingthesub-Gaussian,sub-gamma,sub-Bernoulli,sub-Poissonandsub-exponential
| settings defined |     | in Section | 2.  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1. The stitching method gives new closed-form sub-Gaussian or sub-gamma boundaries (Theorem 1).
Oursub-gammatreatmentextendspriorsub-Gaussianworktocoveranymartingalewhoseincrements
have finite moment-generating function in a neighborhood of zero; see Proposition 1. Our proof is
transparent and flexible, accommodating a variety of boundary shapes, including those growing at
√
the rate O( tloglogt) with a focus on tight constants, though we do not recommend this bound in
| practice | unless | closed-form |     | simplicity |     | is vital. |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
2. Conjugate mixtures give one- and two-sided boundaries for the sub-Bernoulli, sub-Gaussian, sub-
Poisson and sub-exponential cases (Section 3.2) which avoid approximations made for analytical con-
venience. The sub-Gaussian boundaries are unimprovable without further assumptions (Section 3.6).
These boundaries include a common tuning parameter which is critical in practice and we discuss why
|     | √   |     |     |     |     |     |     |     | √   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
their O( tlogt) growth rate may be preferable to the slower O( tloglogt) rate (Section 3.5).
3. Discrete mixtures facilitatenumericalcomputationofboundarieswithagreatdealofflexibility, atthe
cost of slightly more involved computations (Theorem 2). Like conjugate mixture boundaries, these
boundaries avoid unnecessary approximations and are unimprovable in the sub-Gaussian case.
4. Finally, for sub-Gaussian processes, the inverted stitching method (Theorem 3) gives numerical upper
bounds on the crossing probability of any increasing, strictly concave boundary over a limited time
range. We show that any such boundary yields a uniform upper tail inequality over a finite horizon,
| and | compute | its | crossing | probability. |     |     |     |     |     |     |     |
| --- | ------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Building on this foundation, we present a a state-of-the-art empirical-Bernstein bound (Theorem 4) for any
sequenceofboundedobservationsusinganewself-normalizationprooftechnique. Weillustrateourmethods
with two novel applications: the nonasymptotic, sequential estimation of average treatment effect in the
Neyman-Rubin potential outcomes model (Section 4.2), and the derivation of uniform matrix bounds and
covariancematrixconfidencesequences(Corollary3andSection4.3). WegivesimulationresultsinSection5.
Section 6 discusses the relationship of our work to existing concepts of sequential testing. Proofs of main
| results are      | in Appendix |     | A, with | others | deferred   | to  | Appendix | C.  |     |     |     |
| ---------------- | ----------- | --- | ------- | ------ | ---------- | --- | -------- | --- | --- | --- | --- |
| 2 Preliminaries: |             |     |         | linear | boundaries |     |          |     |     |     |     |
Given a sequence of real-valued observations (X )∞ , suppose we wish to estimate the average conditional
|              |     |                |     |         |                                 | t   | t=1 |     |                |                   |     |
| ------------ | --- | -------------- | --- | ------- | ------------------------------- | --- | --- | --- | -------------- | ----------------- | --- |
|              |     | :=t−1(cid:80)t | E   |         | ateachtimetusingthesamplemeanX¯ |     |     |     | :=t−1(cid:80)t |                   |     |
| expectationµ | t   |                |     | i−1 X i |                                 |     |     |     | t              | X i ;hereweassume |     |
|              |     |                | i=1 |         |                                 |     |     |     |                | i=1               |     |
anunderlyingfiltration(F )∞ towhich(X )isadapted,andE denotesexpectationconditionalonF . Let
|     |     |     | t t=1 |     |     | t   |     | t   |     |     | t   |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
S := (cid:80)t (X −E X ), the zero-mean deviation of our sample sum from its estimand at time t. Given
| t i=1 | i   | i−1 | i   |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|       |     |     |     |     |     |     |     | :R  | →R  |     |     |
α∈(0,1), suppose we can construct a uniform upper tail bound u satisfying
|     |     |     |     |     |          |        |       | α       | ≥0 ≥0 |     |     |
| --- | --- | --- | --- | --- | -------- | ------ | ----- | ------- | ----- | --- | --- |
|     |     |     |     |     | P(cid:0) |        |       | (cid:1) |       |     |     |
|     |     |     |     |     |          | ∃t≥1:S | ≥u (V | ) ≤α    |       |     | (3) |
|     |     |     |     |     |          |        | t α   | t       |       |     |     |
)∞
for some adapted, real-valued intrinsic time process (V t , an appropriate time scale to measure the
t=1
(squared) deviations of (S ). This uniform upper bound on the centered sum (S ) yields a lower confidence
|     |     |     | t   |     |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sequence for (µ ) with radius t−1u (V ): P(cid:0) ∀t≥1:X¯ −t−1u (V )≤µ (cid:1) ≥1−α.
|     |     | t   |     | α   | t   |     | t   | α t | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Notethatanassumptionontheuppertailof(S )yieldsalowerconfidencesequencefor(µ );acorresponding
|     |     |     |     |     |     | t   |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assumption on the lower tail of (S ) yields an upper confidence sequence for (µ ). In this paper we formally
|     |     |     |     | t   |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
focusonuppertailbounds,fromwhichlowertailboundscanbederivedbyexamining(−S t )inplaceof(S t ).
Ingeneral, theleftandrighttailsof(S )maybehavedifferentlyandrequiredifferentsetsofassumptions, so
t
thatourupperandlowerconfidencesequencesmayhavedifferentforms. Regardless,wecanalwayscombine
upper and lower confidence sequences using a union bound to obtain a two-sided confidence sequence (1).
When the (X ) are independent with common mean µ, the resulting confidence sequence estimates µ, but
t
the setup requires neither independence nor a common mean. In general, the estimand µ may be changing
t
4

at eachtime t; Section 4.2givesan applicationto causalinference in whichthis changing estimandis useful.
In principle, µ may also be random, although none of our applications involve random µ .
|     |     | t   |     |     |     |     |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To construct uniform boundaries u satisfying inequality (3), we build upon the following general condition
α
| (Howard | et al., | 2020, | Definition | 1): |     |     |     |     |     |     |     |     |     |
| ------- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition 1 (Sub-ψ condition). Let (S )∞ ,(V )∞ be real-valued processes adapted to an underlying
|     |     |     |     |     |     | t t=0 | t t=0 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
filtration (F )∞ with S =V =0 and V ≥0 for all t. For a function ψ : [0,λ ) → R and a scalar
|     | t   | t=0 | 0   | 0   |     | t   |     |     |     |     | max |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l 0 ∈ [1,∞), we say (S t ) is l 0 -sub-ψ with variance process (V t ) if, for each λ ∈ [0,λ max ), there exists a
| supermartingale |       | (L      | (λ))∞ | w.r.t. | (F ) such | that   | EL (λ)≤l    |           | and          |       |     |     |     |
| --------------- | ----- | ------- | ----- | ------ | --------- | ------ | ----------- | --------- | ------------ | ----- | --- | --- | --- |
|                 |       | t       | t=0   |        | t         |        | 0           | 0         |              |       |     |     |     |
|                 |       |         |       | exp{λS |           | −ψ(λ)V | }≤L         | (λ)       | a.s. for all | t.    |     |     | (4) |
|                 |       |         |       |        |           | t      | t           | t         |              |       |     |     |     |
| For given       | ψ and | l , let | Sl0   | be the | class of  | pairs  | of l -sub-ψ | processes | (S           | ,V ): |     |     |     |
|                 |       | 0       | ψ     |        |           |        | 0           |           |              | t t   |     |     |     |
Sl0 :={(S ,V ):(S ) is l -sub-ψ with variance process (V )}. (5)
|     |     |     | ψ   | t   | t   | t   | 0   |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
When stating that a process is sub-ψ, we typically omit l 0 from our terminology for simplicity. In scalar
cases, we always have l =1, while in matrix cases l =d, the dimension of the (square) matrices.
|     |     |     | 0   |     |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Where does Definition 1 come from? The jumping-off point is the martingale method for concentration
inequalities ((Hoeffding, 1963; Azuma, 1967; McDiarmid, 1998); (Raginsky et al., 2013, section 2.2)), itself
basedontheclassicalCram´er-Chernoffmethod((Cram´er,1938;Chernoff,1952);(Boucheronetal.,2013,sec-
tion2.2)). ThemartingalemethodstartsoffwithanassumptionoftheformE eλ(Xt−E t−1Xt) ≤eψ(λ)σ 2 for
|     |     |     |     |     |     |     |     |     |     |     | t−1 |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allt≥1,λ∈R. Then,denotingS := (cid:80)t (X −E X )andV := (cid:80)t σ2,theprocessexp{λS −ψ(λ)V }
|     |     |     |     | t    |     | i   | i−1 | i   | t   | i   |     | t   | t   |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | λ∈R. |     | i=1 |     |     | i=1 |     |     |     |     |
is a supermartingale for each Unlike the martingale method assumption, Definition 1 allows the ex-
ponential process to be upper bounded by a supermartingale, and it permits (V ) to be adapted rather than
t
predictable. We also restrict our attention to λ≥0 to derive one-sided bounds.
Intuitively, the process exp{λS −ψ(λ)V } measures how quickly S has grown relative to intrinsic time V ,
|     |     |     |     | t   |     | t   |     |     | t   |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and the free parameter λ determines the relative emphasis placed on the tails of the distribution of S t , i.e.,
onthehighermoments. LargervaluesofλexaggeratelargermovementsinS , andψ captureshowmuchwe
t
mustcorrespondinglyexaggerateV . ψ isrelatedtotheheavy-tailednessofS andthereadermaythinkofit
|     |     |     |     |     | t   |     |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as a cumulant-generating function (CGF, the logarithm of the moment-generating function). For example,
suppose (X ) is a sequence of i.i.d., zero-mean random variables with CGF ψ(λ):=logEeλX1 which is finite
t
|     |     |     |     |     | :=  |     |     |     | :=  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for all λ ∈ [0,λ max ). Then, setting V t t, we see that L t (λ) exp{λS t −ψ(λ)V t } is itself a martingale,
for all λ ∈ [0,λ ). Indeed, in all scalar cases we consider, L (λ) is just equal to exp{λS −ψ(λ)V }. See
|     |     | max |     |     |     |     |     |     | t   |     |     | t   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AppendixTables3and4,drawnfromHowardetal.(2020),foracatalogofsufficientconditionsforaprocess
to be sub-ψ using the five ψ functions defined below. We use many of these conditions in what follows.
We organize our uniform boundaries according to the ψ function used in Definition 1. First recall the
logEeλXt
Cram´er-Chernoff bound: if (X t ) are independent zero-mean with bounded CGF ≤ ψ(λ) for all
(cid:80)t
t ≥ 1 and λ ∈ R, then writing S = X , we have P(S ≥ x) ≤ e−tψ(cid:63)(x/t) for any x > 0, where ψ(cid:63)
|     |     |     |     |     | t   | i=1 | i   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
denotes the Legendre-Fenchel transform of ψ. Equivalently, writing z (t) := tψ(cid:63)−1(t−1logα−1), we have
α
P(S
≥ z (t)) ≤ α for any fixed t and α ∈ (0,1). In other words, the function z gives a high-probability
| t   | α   |     |     |     |     |     |     |     |     |     | α   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
upper bound at any fixed time t for any sum of independent random variables with CGF bounded by
ψ. When we extend this concept to boundaries holding uniformly over time, there is no longer a unique,
minimized boundary, and the following definition captures the class of valid boundaries.
Definition2. Givenψ :[0,λ )→Randl ≥1,afunctionu:R→Riscalledanl -sub-ψ uniformbound-
|          |          |             |     | max  |     | 0   |     |     |     |     | 0   |     |     |
| -------- | -------- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ary with | crossing | probability |     | α if |     |     |     |     |     |     |     |     |     |
P(∃t≥1:S
|     |     |     |     |     | sup        |     |     | ≥u(V | ))≤α. |     |     |     | (6) |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ---- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |            |     |     | t    | t     |     |     |     |     |
|     |     |     |     |     | (St,Vt)∈Sl | 0   |     |      |       |     |     |     |     |
ψ
Although u does depend on the constant l 0 in Definition 1, for simplicity we typically omit this dependence
| from our | notation, | writing |     | simply | that u | is a sub-ψ | uniform | boundary. |     |     |     |     |     |
| -------- | --------- | ------- | --- | ------ | ------ | ---------- | ------- | --------- | --- | --- | --- | --- | --- |
Five particular ψ functions play important roles in our development; below, we take 1/0=∞ in the upper
| bounds | on λ: |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5

|     |     | (cid:16) |            | (cid:17) |     |     |     |     |     |     |
| --- | --- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| •   |     | 1        | gehλ+he−gλ |          |     |     |     |     |     |     |
ψ (λ):= log on 0 ≤ λ< ∞, the scaled CGF of a centered random variable (r.v.)
| B,g,h |     | gh  | g+h |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
supported on two points, −g and h, for some g,h > 0, for example a centered Bernoulli r.v. when
g+h=1.
| • ψ (λ):=λ2/2 |     | on 0≤λ<∞, |     | the | CGF | of a standard | Gaussian | r.v. |     |     |
| ------------- | --- | --------- | --- | --- | --- | ------------- | -------- | ---- | --- | --- |
N
• ψ (λ) := c−2(ecλ −cλ−1) on 0 ≤ λ < ∞ for some scale parameter c ∈ R, which is the CGF of a
P,c
centered unit-rate Poisson r.v. when c=1. By taking the limit, we define ψ =ψ .
|     |     |     |     |     |     |     |     |     | P,0 | N   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• ψ (λ) := c−2(−log(1−cλ)−cλ) on 0 ≤ λ < 1/(c∨0) for some scale c ∈ R, which is the CGF of a
E,c
centered unit-rate exponential r.v. when c=1. By taking the limit, we define ψ =ψ .
E,0 N
• R,
ψ (λ) := λ2/(2(1−cλ)) on 0 ≤ λ < 1/(c∨0) (taking 1/0 = ∞) for some scale parameter c ∈
G,c
which we refer to as the sub-gamma case following Boucheron et al. (2013). This is not the CGF of a
gamma r.v. but is a convenient upper bound which also includes the sub-Gaussian case at c = 0 and
| permits | analytically |     | tractable | results | below. |     |     |     |     |     |
| ------- | ------------ | --- | --------- | ------- | ------ | --- | --- | --- | --- | --- |
Sub-gamma
|     |     | Sub-Bernoulli |     |     |     | Sub-Poisson |     |     |                 |     |
| --- | --- | ------------- | --- | --- | --- | ----------- | --- | --- | --------------- | --- |
|     |     |               |     | c<0 |     |             |     | c<0 |                 |     |
|     |     | Sub-Gaussian  |     |     |     |             |     |     | Sub-exponential |     |
c<0
Figure 2: Relations among sub-ψ boundaries: each arrow indicates that a sub-ψ boundary at the source node can
also serve as a sub-ψ boundary at the destination node, with appropriate modifications to their parameters. Details
| are in Proposition |     | 11. |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
One may freely scale ψ by any positive constant and divide V by the same constant so that Definition 1
t
ψ(cid:48)(cid:48)(0
remains satisfied; by convention, we scale all ψ functions above so that + ) = 1. When we speak of a
sub-gamma process (or uniform boundary) with scale parameter c, we mean a sub-ψ process (or uniform
G,c
boundary),andlikewiseforothercases. Weoftenwriteψ ,ψ ,etc.,droppingtherangeandscaleparameters
|     |     |     |     |     |     |     | B P |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
from our notation. As we summarize in Figure 2 and detail in Proposition 11, certain general implications
hold among sub-ψ boundaries. In particular, any sub-Gaussian boundary can also serve as a sub-Bernoulli
boundary; anysub-Poissonboundaryservesasasub-Gaussianorsub-Bernoulliboundary; and,importantly,
any sub-gamma or sub-exponential boundary can serve as a sub-ψ boundary in any of the other four cases.
Indeed, a sub-gamma or sub-exponential boundary applies to many cases of practical interest, as detailed
below.
istwice-differentiableandψ(0)=ψ(cid:48)(0
| Proposition1. |     | Supposeψ |     |     |     |     |     | + )=0. | Suppose,foreachc>0, | u c (v)isa |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | ------ | ------------------- | ---------- |
sub-gamma or sub-exponential uniform boundary with crossing probability α for scale c. Then v (cid:55)→u (k v)
k1 2
is a sub-ψ uniform boundary for some constants k ,k >0 depending only on ψ.
|     |     |     |     |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition 1 restates Howard et al. (2020, Proposition 1), which shows that any process (S t ) which is
sub-ψ is also sub-gamma and sub-exponential, if ψ satisfies the conditions of Proposition 1. Note that these
conditions are satisfied for any mean-zero random variable if the CGF exists in a neighborhood of zero, so
| the conditions | are | quite weak | (Jorgensen, |     | 1997, | Theorem | 2.3). |     |     |     |
| -------------- | --- | ---------- | ----------- | --- | ----- | ------- | ----- | --- | --- | --- |
Example 1 (ConfidencesequenceforthevarianceofaGaussiandistributionwithunknownmean). Suppose
X ,X ,... are i.i.d. draws from a N(µ,σ2) distribution and we wish to sequentially estimate σ2 when µ is
1 2
|     |     | :=σ−2(cid:80)t+1(X |     |     | −X¯ |     |     |     | X¯ :=t−1(cid:80)t |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- |
also unknown. Let S )2−t for t=1,2,..., where X is the sample
|     |     | t   | i=1 | i   | t+1 |     |     |     | t i=1 | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
mean. This S is a centered and scaled sample variance, and as in Darling and Robbins (1967a), we use
t
the fact that S t is a cumulative sum of independent, centered Chi-squared random variables each with one
degree of freedom (see Appendix H for details). Such a centered Chi-squared distribution has variance two
| and CGF equal |     | to 2ψ . |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
E,2
Thus (S ) is 1-sub-exponential with variance process V =2t and scale parameter c=2. We may uniformly
| t   |     |     |     |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bound the upper deviations of S using any sub-exponential uniform boundary, for example the gamma-
t
exponential mixture boundary of Proposition 9. Or, we can use Proposition 11 to deduce that (S ) is
t
6

sub-gamma with scale c=2 (and the same variance process) and use the closed-form stitched boundary of
| Theorem | 1.  |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The above constructions yield lower confidence sequences for the variance. To obtain an upper confidence
sequence, we use the fact that (−S t ) is 1-sub-exponential with scale parameter c=−2. Now Proposition 11
implies that (−S ) is sub-gamma with scale c=−1, so the stitched boundary again applies, while Proposi-
t
tion 11 implies that (−S ) is also sub-Gaussian, so we may alternatively use the normal mixture boundary
t
of Proposition 6. Since ψ is uniformly smaller than ψ , the above analysis yields tighter bounds than
|                  |     | G,−1     |            |     |         |          | N   |     |     |
| ---------------- | --- | -------- | ---------- | --- | ------- | -------- | --- | --- | --- |
| the sub-Gaussian |     | approach | of Darling | and | Robbins | (1967a). |     |     |     |
The simplest uniform boundaries are linear with positive intercept and slope. This is formalized in Howard
| et al. (2020), | partially | restated | below. |     |     |     |     |     |     |
| -------------- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
Lemma 1 ((Howard et al., 2020), Theorem 1). For any λ∈[0,λ max ) and α∈(0,1),
|            |         |          |               |        | log(l       | /α) | ψ(λ) |     |     |
| ---------- | ------- | -------- | ------------- | ------ | ----------- | --- | ---- | --- | --- |
|            |         |          |               | u(v):= |             | 0   |      |     |     |
|            |         |          |               |        |             |     | + ·v |     | (7) |
|            |         |          |               |        |             | λ   | λ    |     |     |
| is a sub-ψ | uniform | boundary | with crossing |        | probability | α.  |      |     |     |
While Lemma 1 provides a versatile building block, the O(V ) growth of u(V ) may be undesirable. Indeed,
|     |     |     |     |     |     |     | t   | t   | √   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
from a concentration point of view, the typical deviations of S tend to be only O( V ), so the bound will
|     |     |     |     |     |     |     | t   |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rapidly become loose for large t. From a confidence sequence point of view, recall that the confidence radius
for the mean is given by u(V t )/t. Typically, V t = Θ(t) a.s. as t → ∞, so the confidence radius will be
asymptotically zero width if and only if u(v)=o(v). In other words, we cannot achieve arbitrary estimation
precision with arbitrarily large samples unless the uniform boundary is sublinear. We address this problem
in Section 3, building upon Lemma 1 to construct curved sub-ψ uniform boundaries.
| 3 Curved |     | uniform | boundaries |     |     |     |     |     |     |
| -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
WepresentourfourmethodsforcomputingcurveduniformboundariesinSections3.1to3.4. InSection3.5,
we discuss how to tune boundaries, a necessity for good performance in practice, and we describe the
| unimprovability |     | of sub-Gaussian | mixture |     | bounds    | in Section | 3.6. |     |     |
| --------------- | --- | --------------- | ------- | --- | --------- | ---------- | ---- | --- | --- |
| 3.1 Closed-form |     | boundaries      |         | via | stitching |            |      |     |     |
Our analytical “stitched” bound is useful in the sub-Gaussian case or, more generally, the sub-gamma case
| with scale | c. We | require three | user-chosen |           | parameters: |     |                 |     |     |
| ---------- | ----- | ------------- | ----------- | --------- | ----------- | --- | --------------- | --- | --- |
| • a scalar | η     | >1 determines | the         | geometric | spacing     | of  | intrinsic time, |     |     |
• a scalar m > 0 which gives the intrinsic time at which the uniform boundary starts to be nontrivial,
and
• an increasing function h:R →R such that (cid:80)∞ 1/h(k)≤1, which determines the shape of the
|            |     |              | ≥0   | >0  |     |     | k=0 |     |     |
| ---------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
| boundary’s |     | growth after | time | m.  |     |     |     |     |     |
Recalling the scale parameter c for the ψ function above and the constant l in Definition 1, we define the
|           |          |      |     | G   |     |     |     | 0   |     |
| --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| stitching | function | S as |     |     |     |     |     |     |     |
α

|     |     |           |     |     |     |     | (cid:96)(v):=logh(log | ( v)) | +log(l 0), |
| --- | --- | --------- | --- | --- | --- | --- | --------------------- | ----- | ---------- |
|     |     | (cid:113) |     |     |     |     |                     | η m   | √ α        |
S (v):= k2v(cid:96)(v)+k2c2(cid:96)2(v)+k c(cid:96)(v), where k :=(η1/4+η−1/4)/ 2, (8)
|     | α   | 1   | 2   |     | 2   |     | 1 √       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     |     |     |     |     |     |     | k :=(   |     |     |
|     |     |     |     |     |     |     | 2 η+1)/2, |     |     |
anddefinethestitchedboundaryasu(v)=S (v∨m). NoteS (v)≤k (cid:112) v(cid:96)(v)+2ck (cid:96)(v)whenc>0,while
|     |     |     |     |     | α   |     | α 1 |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
S (v) ≤ k v(cid:96)(v) when c ≤ 0, with equality in the sub-Gaussian case (c = 0). These simpler expressions
| α   | 1   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
may sometimes be preferable. For notational simplicity we suppress the dependence of S α on h, η, l 0 , and
c; we will discuss specific choices as necessary. In the examples we consider, (cid:96)(v) grows as O(logv) or
(cid:112)
O(loglogv) as v ↑ ∞, so the first term, k V (cid:96)(V ), dominates for sufficiently large V , specifically when
|     | √   |     |     |     | 1 t | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)(cid:29)2c2
| V t /(cid:96)(V t |     | η.  |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7

Final boundary
t
S rof yradnuoB
Linear uniform
Chernoff bounds
0
|     | η0  | η1  |     |     |     |     | η2  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V
t
Figure 3: Illustration of Theorem 1, stitching together linear boundaries to construct a curved boundary. We break
time into geometrically-spaced epochs ηk ≤V <ηk+1, construct a linear uniform bound using Lemma 1 optimized
t
for each epoch, and take a union bound over all crossing events. The final boundary is a smooth analytical upper
| bound to | the piecewise | linear bound. |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 1 (Stitched boundary). For any c≥0,α∈(0,1),η >1,m>0, and h:R →R increasing
|     |     |     |     |     |     |     |     |     |     | ≥0  | ≥0  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
such that (cid:80)∞ 1/h(k)≤1, the function v (cid:55)→ S (v ∨m) is a sub-gamma uniform boundary with crossing
|     | k=0 |     |     |     | α   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
probability α. Further, for any sub-ψ G process (S t ) with variance process (V t ) and any v 0 ≥m,
∞
|     |     |     |     |     |     |     | (cid:88) |     | α   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
P(∃t≥1:V
|     |     |     | t   | ≥v 0 | and S t ≥S | α (V | t ))≤ |     |     | .   |     | (9) |
| --- | --- | --- | --- | ---- | ---------- | ---- | ----- | --- | --- | --- | --- | --- |
h(k)
|     |     |     |     |     |     |     | k=(cid:98)log | (v0/m)(cid:99) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | --- | --- | --- | --- |
η
The first sentence above says that the probability of S crossing S (V ∨m) at least once is at most α, while
|     |     |     |     |     |     | t   | α t |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesecondsaysthat,evenifitdoeshappentocrossonceormore,theprobabilityoffurthercrossingsdecaysto
zerobeyondlargerandlargerintrinsictimesv . Notethat(9)impliesP(sup V =∞ and S ≥S (V ) infinitely often)=
|     |     |     |     |     | 0   |     |     | t   | t   |     | t α t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
0. The proof of Theorem 1, given with discussion in Appendix A.1, follows by taking a union bound over
a carefully chosen family of linear boundaries, one for each of a sequence of geometrically-spaced epochs;
see Figure 3. The high-level proof technique is standard, often referred to as “peeling” in the bandit lit-
erature, and closely related to chaining elsewhere in probability theory. Our proof generalizes beyond the
sub-Gaussiancaseandinvolvescarefulparameterchoicesinordertoachievetightconstants. Inbrief,within
each epoch, thereare manypossiblelinear boundaries, andwe have found thatoptimizingthelinear bound-
ary for the geometric mean of the epoch endpoints strikes a good balance between tight constants and
analytical simplicity in the final boundary. Appendix G gives a detailed comparison of constants arising
| from our | bound with | similar bounds | from | the | literature. |     |     |     |     |     |     |     |
| -------- | ---------- | -------------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
The boundary shape is determined by choosing the function h and setting the nominal crossing probabil-
kth
ity in the epoch to equal α/h(k). Then Theorem 1 gives a curved boundary which grows at a rate
| (cid:16)(cid:113) |     | (cid:17) |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
O V t logh(log V t ) as V t ↑ ∞. The more slowly h(k) grows as k ↑ ∞, the more slowly the resulting
η
boundary will grow as V ↑∞. A simple choice is exponential growth, h(k)=ηsk/(1−η−s) for some s>1,
|     |     | √ t |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
yielding S (v)=O( vlogv). A more interesting example is h(k)=(k+1)sζ(s) for some s>1, where ζ(s)
α
is the Riemann zeta function. Then, when l 0 = 1, Theorem 1 yields the polynomial stitched boundary: for
c≥0,
(cid:115)
|     |         | (cid:18)  |                    |      |        | (cid:19) | (cid:18)    |                    |      |        | (cid:19) |      |
| --- | ------- | --------- | ------------------ | ---- | ------ | -------- | ----------- | ------------------ | ---- | ------ | -------- | ---- |
|     |         |           | (cid:16)ηv(cid:17) |      | ζ(s)   |          |             | (cid:16)ηv(cid:17) |      | ζ(s)   |          |      |
|     | S (v)=k | v sloglog |                    | +log |        |          | +ck sloglog |                    | +log |        | ,        | (10) |
|     | α       | 1         |                    |      | αlogsη |          | 2           |                    |      | αlogsη |          |      |
|     |         |           |                    | m    |        |          |             |                    | m    |        |          |      |
where the second term is neglected in the sub-Gaussian case since c = 0. This is a “finite LIL bound”,
(cid:112)
so-called because S (v) ∼ sk2vloglogv, matching the form of the law of the iterated logarithm (Stout,
|     | α   |     | 1   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1970). We can bring sk2 arbitrarily close to 2 by choosing η and s sufficiently close to one, at the cost of
1
inflating the additive term log(ζ(s)/(logsη)). Briefly, increasing η increases the size of each epoch in the
aforementioned peeling argument, which reduces the looseness of the union bound over epochs. But the
larger we make the epochs, the further each linear boundary deviates from the ideal curved shape at the
ends of the epochs, which inflates our final boundary. The choice of s involves a similar tradeoff: increasing
s causes us to exhaust more of our total error probability budget on earlier epochs, decreasing the constant
8

term (which matters most for early times), at the cost of a union bound over smaller error probabilities
in later epochs, which shows up as an increase in the leading constant. We discuss parameter tuning in
more practical terms in Section 3.5. For example, take η =2,s=1.4,m=1; if S is a sum of independent,
t
| zero-mean, | 1-sub-Gaussian |          | observations, |     | we obtain |          |     |          |                          |     |     |
| ---------- | -------------- | -------- | ------------- | --- | --------- | -------- | --- | -------- | ------------------------ | --- | --- |
|            |                | (cid:32) |               |     | (cid:115) |          |     |          | (cid:19)(cid:19)(cid:33) |     |     |
|            |                |          |               |     |           | (cid:18) |     | (cid:18) |                          |     |     |
5.2
|     |     | P   | ∃t≥1:S | ≥1.7 | t   | loglog(2t)+0.72log |     |     |     | ≤α. | (11) |
| --- | --- | --- | ------ | ---- | --- | ------------------ | --- | --- | --- | --- | ---- |
|     |     |     |        | t    |     |                    |     |     | α   |     |      |
Figure 9 in Appendix G compares a sub-Gaussian stitched boundary to a numerically-computed discrete
1)1.4,
mixture bound with a mixture distribution roughly corresponding to h(k) ∝ (k + as described in
Appendix A.6. This discrete mixture boundary acts as a lower bound (see Section 3.6) and shows that not
too much is lost by the approximations involved in the stitching construction. Figure 10 compare the same
stitched boundary to related bounds from the literature; our bound shows slightly improved constants over
| the best | known bounds. |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Although our stitching construction begins with a sub-gamma assumption, it applies to other sub-ψ cases,
includingsub-Bernoulli,sub-Poissonandsub-exponentialcases;seeFigure2andProposition1. Further,our
stitched bounds apply equally well in continuous-time settings to Brownian motion, continuous martingales,
martingaleswithboundedjumps,andmartingaleswhosejumpssatisfyaBernsteincondition;seeCorollary8.
While our focus is on nonasymptotic results, Theorem 1 makes it easy to obtain the following general upper
| asymptotic | LIL, proved | in  | Appendix | A.2: |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Corollary 1. Suppose (S ) is sub-ψ with variance process (V ) and ψ(λ)∼λ2/2 as λ↓0. Then
|     |     |     | t   |     |     |     |     | t        |          |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     |     |     |     |     | (cid:26) | (cid:27) |     |     |
S
|     |     |     | limsup√ |     | t   | ≤1  | on  | supV | =∞  | .   | (12) |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- | ---- |
t
2V loglogV
|     |           |         | t→∞ |            | t   | t   |     | t   |     |     |     |
| --- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| 3.2 | Conjugate | mixture |     | boundaries |     |     |     |     |     |     |     |
(cid:82)
ForappropriatechoiceofmixingdistributionF,theintegral exp{λS −ψ(λ)V }dF(λ)willbeanalytically
|     |     |     |     |     |     |     |     |     | t   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tractable. Since, under Definition 1, this mixture process is upper bounded by a mixture supermartingale
(cid:82)
L (λ)dF(λ), such mixtures yield closed-form or efficiently computable curved boundaries, which we call
t
conjugate mixture boundaries. This approach is known as the method of mixtures, one of the most widely-
studied techniques for constructing uniform bounds (Ville, 1939; Wald, 1945; Darling and Robbins, 1968;
Robbins, 1970; Robbins and Siegmund, 1969, 1970; Lai, 1976b; Kaufmann and Koolen, 2018). Unlike the
stitched bound of Theorem 1, which involves a small amount of looseness in the analytical approximations,
mixture boundaries involve no such approximations and, in the sub-Gaussian case, are unimprovable in
the sense described in Section 3.6. We restate the following standard idea behind the method of mixtures
using our definitions, with a proof in Appendix A.3. The proof details a technical condition on product
| measurability | which | we require | of  | L . |     |     |     |     |     |     |     |
| ------------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
| Lemma | 2. For any | probability | distribution |     | F   | on [0,λ | ) and | α∈(0,1), |     |     |     |
| ----- | ---------- | ----------- | ------------ | --- | --- | ------- | ----- | -------- | --- | --- | --- |
max
|     |     |     |     | (cid:40) |     | (cid:90) |     |     |     | (cid:41) |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | -------- | --- |
l
|     |     |     | M (v):=sup |     | s∈R: | exp{λs−ψ(λ)v}dF(λ)< |     |     |     | 0   | (13) |
| --- | --- | --- | ---------- | --- | ---- | ------------------- | --- | --- | --- | --- | ---- |
α
α
|     |     |     |     |     |     | (cid:124) |     | (cid:123)(cid:122) | (cid:125) |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------------ | --------- | --- | --- |
=:m(s,v)
isasub-ψ uniformboundarywithcrossingprobabilityα,solongasthesupermartingale(L )ofDefinition1is
t
product measurable when the underlying probability space is augmented with the independent random variable
λ.
For each of our conjugate mixture bounds, we compute m(s,v) in closed-form. The boundary u(v) can then
be computed by numerically solving the equation m(s,v)=l /α in s, as we show in Appendix D. When an
0
identical sub-ψ condition applies to (−S t ) as well as (S t ), we may apply a uniform boundary to both tails
andtakeaunionbound,obtainingatwo-sidedconfidencesequence. However,mixingoverλ∈Rratherthan
λ ∈ R yields a two-sided bound directly, so in some cases we present two-sided variants along with their
≥0
one-sided counterparts. We give details for the following conjugate mixture boundaries in Appendix A.3:
9

| • one-,       | two-sided         | normal        | mixture | boundaries |            | (sub-Gaussian |                  | case);      |        |     |
| ------------- | ----------------- | ------------- | ------- | ---------- | ---------- | ------------- | ---------------- | ----------- | ------ | --- |
| • one-,       | two-sided         | beta-binomial |         | mixture    | boundaries |               | (sub-Bernoulli   |             | case); |     |
| • one-sided   | gamma-Poisson     |               |         | mixture    | boundary   | (sub-Poisson  |                  | case);      | and    |     |
| • one-sided   | gamma-exponential |               |         | mixture    | boundary   |               | (sub-exponential |             | case). |     |
| The two-sided | normal            | mixture       |         | boundary   | has        | a closed      | form             | expression: |        |     |
(cid:115)
|     |     |     |     |        |     |          | (cid:18) | l2(v+ρ) | (cid:19) |      |
| --- | --- | --- | --- | ------ | --- | -------- | -------- | ------- | -------- | ---- |
|     |     |     |     | u(v):= |     | (v+ρ)log |          | 0       | .        | (14) |
α2ρ
The one-sided normal mixture boundary has a similar, closed-form upper bound, making these especially
√
convenient. It is clear from (14) that the normal mixture boundary grows as O( vlogv) asymptotically,
and this rate is shared by all of our conjugate mixture boundaries. Indeed, Proposition 2 below, proved in
AppendixA.4, showsthatsucharateholdsforanymixtureboundaryasgivenby (13)wheneverthemixing
distribution is continuous with positive density at and around the origin, a property which holds for all
mixturedistributionsusedinourconjugatemixtureboundaries, subjecttoregularityconditionsonψ which
hold for the CGF of any nontrivial, mean-zero r.v. and specifically for the five ψ functions in Section 2.
Proposition 2. Assume (i) ψ is nondecreasing, ψ(0) = ψ(cid:48)(0 ) = 0, ψ(cid:48)(cid:48)(0 ) = c > 0, and ψ has three
|     |     |     |     |     |     |     |     | +   | +   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
continuous derivatives on a neighborhood including the origin; and (ii) F has density f (w.r.t. Lebesgue)
which is continuous and positive on a neighborhood including the origin. Then
(cid:115)
|     |     |     |     |     | (cid:20) | (cid:18) |     | (cid:19) | (cid:21) |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | -------- | --- |
cl2v
|     |     |     | M (v)= | v   | clog |     | 0   | +o(1) | as v →∞. | (15) |
| --- | --- | --- | ------ | --- | ---- | --- | --- | ----- | -------- | ---- |
α
2πα2f2(0)
Note that f need not place mass on all of [0,λ ), only near the origin, for the asymptotic rate to hold.
max
Proposition 2 shows how the asymptotic behavior of any such mixture bound depends only on the behavior
of ψ and f near the origin, a result reminiscent of the central limit theorem. Analogous, related results for
λ2/2
the sub-Gaussian special case using ψ(λ) = can be found in Robbins and Siegmund (1970, Section 4)
| and Lai (1976a, | Theorem |     | 2), in | some cases | under | weaker | assumptions |     | on F. |     |
| --------------- | ------- | --- | ------ | ---------- | ----- | ------ | ----------- | --- | ----- | --- |
In contrast to previous derivations of conjugate mixture boundaries in the literature, all of our conjugate
mixture boundaries include a common tuning parameter ρ>0 which controls the sample size for which the
boundaryisoptimized. Suchtuningiscriticalinpractice,asweexplaininSection3.5,buthasbeenignoredin
muchpriorwork. Additionally, withtheexceptionofthesub-Gaussiancase, mostpriorworkonthemethod
of mixtures has focused on parametric settings. We instead emphasize the applicability of these bounds to
nonparametric settings. For example, when the observations are bounded, one may construct a confidence
sequencemakinguseofempirical-Bernsteinestimates(Theorem4)basedonourgamma-exponentialmixture
(Proposition 9). See Appendix J for other conditions in which mixture bounds yield nonparametric uniform
boundaries.
| 3.3 Numerical |     | bounds |     | using | discrete |     | mixtures |     |     |     |
| ------------- | --- | ------ | --- | ----- | -------- | --- | -------- | --- | --- | --- |
In applications, one may not need an explicit closed-form expression so long as the bound can be easily
computed numerically. Our discrete mixture method is an efficient technique for numerical computation of
curvedboundariesforprocessessatisfyingDefinition1. Itpermitsarbitrarymixturedensities,thusproducing
√
boundaries growing at the rate O( vloglogv). Recall that the shape of the stitched bound was determined
by the user-specified function h. For the discrete mixture bound, one instead specifies a probability density
f over finite support (0,λ] for some λ∈(0,λ ). We first discretize f using a series of support points λ ,
|     |     |     |     |     |     | max |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
geometrically spaced according to successive powers of some η >1, and an associated set of weights w k :
√
|     |     |     | λ      |     |     | λ(η−1)f(λ |      | η)  |                   |      |
| --- | --- | --- | ------ | --- | --- | --------- | ---- | --- | ----------------- | ---- |
|     |     | :=  |        |     |     | :=        |      | k   |                   |      |
|     |     | λ k |        | and | w k |           |      |     | for k =0,1,2,.... | (16) |
|     |     |     | ηk+1/2 |     |     |           | ηk+1 |     |                   |      |
10

Theorem 2 (Discrete mixture bound). Fix ψ :[0,λ )→R, α ∈ (0,1), λ∈(0,λ ), and a probability
|     |     |     |     |     | max |     |     | max |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
density f on (0,λ] that is nonincreasing and positive. For supports λ and weights w defined in (16),
|     |     |     |     |          |     |     | k   | k        |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- |
|     |     |     |     | (cid:40) |     |     |     | (cid:41) |     |
∞
|     |     |     |          | s∈R: | (cid:88) |       |      | l 0 |      |
| --- | --- | --- | -------- | ---- | -------- | ----- | ---- | --- | ---- |
|     |     | DM  | (v):=sup |      | w exp{λ  | s−ψ(λ | )v}< | ,   | (17) |
|     |     |     | α        |      | k        | k     | k    | α   |      |
k=0
| is a sub-ψ uniform |     | boundary | with crossing | probability | α.  |     |     |     |     |
| ------------------ | --- | -------- | ------------- | ----------- | --- | --- | --- | --- | --- |
We suppress the dependence of DM on f, l , λ and η for notational simplicity. Though Theorem 2 is a
|     |     |     | α   |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
straightforward consequence of the method of mixtures, our choice of discretization (16) makes it effective,
broadly applicable, and easy to implement. See Appendix A.5 for the proof of this result. Figure 9 includes
an example bound, demonstrating a slight advantage over stitching. Appendix A.6 describes a connection
betweenthestitchinganddiscretemixturemethods,includingacorrespondencebetweenthealpha-spending
function h and the mixture density f. Finally, we note that the method can be applied even when f is not
monotone; one must simply choose the discretization (16) more carefully, using known properties of f.
| 3.4 Inverted | stitching |     | for | arbitrary | boundaries |     |     |     |     |
| ------------ | --------- | --- | --- | --------- | ---------- | --- | --- | --- | --- |
In the method of mixtures, we choose a mixing distribution F and the machinery yields a boundary M α .
Likewise, in the stitching construction of Theorem 1, we choose an error decay function h and obtain a
boundary S . Here, we invert the procedure: we choose a boundary function g(v) and numerically compute
α
an upper bound on its S -upcrossing probability using a stitching-like construction.
t
R R
Theorem 3. For any nonnegative, strictly concave function g : → and v max >1, the function
(cid:40)
|     |     |     |     |        | g(1∨v), v | ≤v  | ,   |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | --- | --- | --- |
|     |     |     |     | u(v):= |           | max |     |     |     |
(18)
|                   |         |          |                              |                                           | ∞, otherwise |         |     |          |     |
| ----------------- | ------- | -------- | ---------------------------- | ----------------------------------------- | ------------ | ------- | --- | -------- | --- |
| is a sub-Gaussian | uniform | boundary |                              | with crossing                             | probability  | at most |     |          |     |
|                   |         |          | (cid:100)log η vmax(cid:101) | (cid:26) 2(g(ηk+1)−g(ηk))(ηg(ηk)−g(ηk+1)) |              |         |     | (cid:27) |     |
(cid:88)
|     |     | l inf |     | exp − |          |     |     | .   | (19) |
| --- | --- | ----- | --- | ----- | -------- | --- | --- | --- | ---- |
|     |     | 0     |     |       | ηk(η−1)2 |     |     |     |      |
η>1
k=0
The proof is in Appendix A.7. For simplicity we restrict to the sub-Gaussian case; examination of the
proof will show that the method applies in other sub-ψ cases as well, since we simply apply Lemma 1 to
appropriately chosen lines, but more involved numerical calculations will be necessary, as the closed-form
(19)nolongerapplies. AsimilarideawasconsideredbyDarlingandRobbins(1968),usingamixtureintegral
approximation instead of an epoch-based construction to derive closed-form bounds. Theorem 3 requires
numerical summation but yields tighter bounds with fewer assumptions. As an example, Theorem 3 with
| η =2.99 shows | that           |          |           |          |                         |     |                   |     |      |
| ------------- | -------------- | -------- | --------- | -------- | ----------------------- | --- | ----------------- | --- | ---- |
|               |                | (cid:16) |           |          |                         |     | (cid:17)          |     |      |
|               |                | P        | ≤1020     |          | (cid:112)               |     |                   |     |      |
|               |                | ∃t:1≤V   | t         | and      | S t ≥1.7 V t (loglog(eV |     | t )+3.46) ≤0.025. |     | (20) |
| This boundary | is illustrated |          | in Figure | 9.       |                         |     |                   |     |      |
| 3.5 Tuning    | boundaries     |          | in        | practice |                         |     |                   |     |      |
All uniform boundaries involve a tradeoff of tightness at different intrinsic times: making a bound tighter
for some range of times requires making it looser at other times. Roughly speaking, the choice of a uniform
boundary involves choosing both what time the bound should be optimized for (e.g., should the bound
be tightest around 100 observations or around 100,000 observations?) as well as how quickly the bound
degrades as we move away from the optimized-for time (e.g., if we optimize for 100 samples, will the bound
be twice as wide when we reach 1,000 samples, or will it stay within a factor of two until we reach 1,000,000
samples?). A boundary which decays more slowly will necessarily not be as tight around the optimized-for
time. In brief, linear boundaries decay the most quickly, conjugate mixture boundaries decay substantially
more slowly, and polynomial stitched boundaries decay even more slowly; we feel that mixture boundaries
| strike a good | balance | in practice. |     |     |     |     |     |     |     |
| ------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
11

6
|     |     |     |     |     |     |     | Polynomial stitching, c | =1, m =100 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | ---------- | --- |
|     |     |     |     |     |     |     | Polynomial stitching, c | =0, m =100 |     |
v
| 4   |     |     |     |     |     |     | Discrete mixture LIL, m | =50 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
)v(u
|     |     |     |     |     |     |     | Gamma mixture, c =1, m | =300 |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | ---- | --- |
|     |     |     |     |     |     |     | Normal mixture, m =300 |      |     |
2
|     |     |     |     |     |     |     | Gamma mixture, c =1, m   | =5,000 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ------ | --- |
|     |     |     |     |     |     |     | Normal mixture, m =5,000 |        |     |
0
|     | 101 |     | 102 | 103 |     | 104 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v
√
Figure 4: Comparison of normalized uniform boundaries u(v)/ v optimized for different intrinsic times. Normal
mixture uses Appendix Proposition 6, while gamma mixture uses Appendix Proposition 9. Polynomial stitched
boundary is given in (10), with η = 2 and s = 1.4. Discrete mixture applies Theorem 2 to the density f(λ) =
/[λlog1.4(0.38e/λ)]
0.4·1 0≤λ≤0.38 with η = 1.1, and λ max = 0.38; see Appendix A.6 for motivation. All boundaries
use α=0.025.
Here, we explain how to optimize uniform boundaries for a particular time and discuss the above tradeoff
in more detail. Let W (x) be the lower branch of the Lambert W function, the most negative real-valued
|     |     | −1  |     |     |     | √   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solution in z to zez = x. Consider the unitless process S / V , and the corresponding uniform boundary
|     | √   |     |     |     |     | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v (cid:55)→u(v)/ √ v. Sinceallofouruniformboundariesu(v)havepositiveinterceptatv √ =0,andallgrowatleast
attherate vloglogv asv →∞, thenormalizedboundaryu(v)/ v divergesasv →0andv →∞. Forthe
√
two-sided normal mixture (14), there is a unique time m at which u(v)/ v is minimized; m is proportional
| to tuning | parameter | ρ as | follows: |     |     |     |     |     |     |
| --------- | --------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
Proposition 3. Let u(v) be the two-sided normal mixture boundary (14) with parameter ρ>0.
√
(a) For fixed ρ>0, the function v (cid:55)→u(v)/ v is uniquely minimized at v =m with m given by
(cid:18) α2(cid:19)
m
|     |     |     |     |     | =−W | −      | −1. |     | (21) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---- |
|     |     |     |     |     |     | −1 el2 |     |     |      |
ρ
0
(b) For fixed m>0, the choice of ρ which minimizes the boundary value u(m) is also determined by (21).
The above result is proved in Appendix C.1; it is a matter of elementary calculus, but addresses a question
that has received little attention in the literature. Figure 4 includes the normalized versions of two normal
mixture boundaries optimized for different times, m = 300 and m = 5,000. Optimizing for the range of
values of V most relevant in a particular application will yield the tightest confidence sequences. However,
t
as the figure shows, one need not have a very precise range of times, so long as one uses a conservatively
√
lowvalueform, becauseu(v)/ v growsslowlyaftertimem. √ Indeed, forthenormalmixtureboundarywith
√
α=0.05 and l =1, we have u(m)/ m≈3.0 and u(100m)/ 100m≈3.6, so that the penalty for being off
0
| by two | orders of | magnitude | is modest. |     |     |     |     |     |     |
| ------ | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
The one-sided normal mixture boundary of Appendix Proposition 6 with crossing probability α is nearly
identical to the two-sided normal mixture boundary with crossing probability 2α, so one may choose ρ as
in Proposition 3 with α doubled. For the gamma-exponential mixture and other non-sub-Gaussian uniform
boundaries, Proposition 3 provides a good approximation in practice. Figure 4 includes gamma-exponential
mixture boundaries with the same ρ values as each corresponding normal mixture boundary. Though the
normalized gamma-exponential mixture boundary with m=300 clearly reaches its minimum at v >m, this
choice of ρ seems reasonable. Discrete mixtures can be similarly tuned by adjusting the precision of the
| mixing | distribution, | but | require additional |     | considerations | (Appendix | E). |     |     |
| ------ | ------------- | --- | ------------------ | --- | -------------- | --------- | --- | --- | --- |
Comparing the sub-Gaussian stitched boundary, discrete mixture boundary, and normal mixture boundary
optimized for m = 300 in Figure 4 illustrates another important point for practice: although the normal
12

mixture bound grows more quickly than the others as v → ∞, it remains smaller over about three orders
of magnitude. This makes it preferable for many real-world applications, as the longest feasible duration of
an experiment is rarely more than two orders of magnitude larger than the earliest possible stopping time.
For example, many online experiments run for at least one week to account for weekly seasonality effects,
and very few such experiments last longer than 100 weeks. As both the normal mixture and the discrete
mixture are unimprovable in general (Section 3.6), the difference is attributable to the choice of mixture, or
alternatively,tothefactthatthenormalmixturetradestightnessaroundtheoptimized-fortimeinexchange
for looseness at much later times. The lesson is that the O(vloglogv) rate, while asymptotically optimal in
certainsettingsandusefulfortheoryandsomeapplications,maynotbepreferableinallreal-worldscenarios.
| 3.6 Unimprovability |     | of  | uniform | boundaries |     |     |     |     |
| ------------------- | --- | --- | ------- | ---------- | --- | --- | --- | --- |
Definition 2 of a sub-ψ boundary u involves only an upper bound on the u-crossing probability of any sub-
ψ process (S t ). One may reasonably ask for corresponding lower bounds on the u-crossing probability to
quantify how tight this boundary is. In the ideal case, we might desire a boundary u such that the true
u-crossing probability of some process (S ) is equal to the upper bound. In nonparametric settings, we
t
cannot achieve this goal for every sub-ψ process. However, we might still ask that there exists some sub-ψ
process for which the true u-crossing probability is arbitrarily close to the upper bound, so that the upper
bound on crossing probability is unimprovable in general. That is, we might ask that the inequality on the
| supremum | in Definition | 2 holds with | equality. |     |     |     |     |     |
| -------- | ------------- | ------------ | --------- | --- | --- | --- | --- | --- |
The fact we wish to point out, known in various forms, is that in the scalar, sub-Gaussian case, exact
mixture bounds are unimprovable in the above sense. It is in this sense that the discrete mixture bound
in Figure 9 provides a lower bound, showing that the sub-Gaussian polynomial stitched bound cannot be
improved by much. The following result shows that, for any exact, sub-Gaussian mixture boundary M , as
α
defined in Lemma 2 for ψ =ψ , there exists a sub-Gaussian process whose true M -crossing probability is
|     |     | N   |     |     |     |     | α   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
arbitrarily close to α. The result is similar to Theorem 2 of Robbins and Siegmund (1970), which gives a
more general invariance principle, but requires conditions on the boundary that appear difficult to verify for
arbitrary mixture boundaries M . Recall that S1 is the class of pairs of processes (S ,V ) such that (S )
|                   |        |            | α              | ψN       |          |          | t t | t    |
| ----------------- | ------ | ---------- | -------------- | -------- | -------- | -------- | --- | ---- |
| is 1-sub-Gaussian | with   | variance   | process (V     | t ).     |          |          |     |      |
| Proposition       | 4. For | any exact, | 1-sub-Gaussian | mixture  | boundary | M α ,    |     |      |
|                   |        |            | sup            | P(∃t≥1:S | ≥M       | (V ))=α. |     | (22) |
|                   |        |            |                |          | t        | α t      |     |      |
(St,Vt)∈S1
ψN
WeproveProposition4inAppendixC.2. Ingeneral,foreachαthereisaninfinitevarietyofboundariesthat
are unimprovable in the above sense, differing in when they are loose and tight. These different boundaries
willyieldconfidencesequenceswhicharelooseortightatdifferentsamplesizes,or,equivalently,areefficient
for detecting different effect sizes. Such a boundary cannot be tightened everywhere without increasing the
crossing probability.
4 Applications
Afterpresentinganempirical-Bernsteinconfidencesequenceforboundedobservations,weapplyouruniform
boundaries to causal effect estimation and matrix martingales. We also consider estimation for a general,
| one-parameter | exponential         | family. |            |     |          |     |     |     |
| ------------- | ------------------- | ------- | ---------- | --- | -------- | --- | --- | --- |
| 4.1 An        | empirical-Bernstein |         | confidence |     | sequence |     |     |     |
The following novel result is proved in Appendix A.8 using a self-normalization argument, which leads to its
attractive simplicity. Recall the estimand µ :=t−1(cid:80)t E X , the average conditional expectation.
|     |     |     |     | t   | i−1 | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
13

Theorem 4. Suppose X ∈[a,b] a.s. for all t. Let (X(cid:98)t ) be any [a,b]-valued predictable sequence, and let u
t
be any sub-exponential uniform boundary with crossing probability α for scale c=b−a. Then
|     |     |     |     |       |                     |     | (cid:16)  | (cid:80)t |             | (cid:17) |     |     |      |
| --- | --- | --- | --- | ------ | ------------------- | --- | --------- | --------- | ----------- | --------- | --- | --- | ---- |
|     |     |     |     |        |                     |     | u         | (X        | −X(cid:98)i | )2        |     |     |      |
|     |     |     |     |        | (cid:12) (cid:12)X¯ |     | (cid:12)  | i=1       | i           |           |     |     |      |
|     |     |     | P   | ∀t≥1: |                     | −µ  | (cid:12)< |           |             | ≥1−2α.   |     |     | (23) |
|     |     |     |     |        |                     | t   | t         | t         |             |           |     |     |      |
This is an empirical-Bernstein bound because it uses the sum of observed squared deviations to estimate
the true variance, much like a classical t-test. Hence the confidence radius scales with the true standard
deviationforsufficientlylargesamples,regardlessofthesupportdiameterb−a,andwithnopriorknowledge
of the true variance. Note also that this bound does not require that observations share a common mean.
The confidence statement (23) holds for any sequence of predictions (X(cid:98)i ), but predictions closer to the
E
conditional expectations, X(cid:98)i ≈ X , will yield smaller confidence intervals on average. A simple choice
i−1 i
is the mean, X(cid:98)t = (t−1)−1(cid:80)t − 1X , which will be effective when the samples are i.i.d., for example. But
|     |     |     |     | i=  | 1 i |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the predictions (X(cid:98)i ) can also make use of trends, seasonality, stratification or regression (in the presence of
covariates), machine learning algorithms, or any other information that may aid with prediction.
(cid:80)t
For an explicit example, assume X ∈ [0,1] and define the empirical variance as V(cid:98)t := (X −X¯ )2.
|     |     |     |     |     | i   |     |     |     |     |     |     | i=1 i | i−1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Invoking Theorem 4 with the polynomial stitched bound (10) using c = 1, η = 2, m = 1, and h(k) ∝ k1.4,
| we have | the following |     | 95%-confidence |     |     | sequence | for µ | :   |     |     |     |     |     |
| ------- | ------------- | --- | -------------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
t
(cid:113)
|     |     |     |     | 1.7 (V(cid:98)t | ∨1)(loglog(2(V(cid:98)t |     | ∨1))+3.8)+3.4loglog(2(V(cid:98)t |     |     |     | ∨1))+13 |     |     |
| --- | --- | --- | --- | --------------- | ----------------------- | --- | -------------------------------- | --- | --- | --- | ------- | --- | --- |
X¯
|     |     |     | t ± |     |     |     |     |     |     |     |     | .   | (24) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
t
Whenaclosedformisnotrequired,thegamma-exponentialmixture(Proposition9)mayyieldtighterbounds
than stitching; simulations in Section 5 demonstrate the use of Theorem 4 with this mixture.
| 4.2 Estimating |     |     | ATE | in  | the | Neyman-Rubin |     |     | model |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----- | --- | --- | --- | --- |
As one illustration of Theorem 4, we consider the sequential estimation of average treatment effect under
the Neyman-Rubin potential outcomes model (Neyman, 1923/1990; Rubin, 1974; Imbens and Rubin, 2015).
We imagine a sequence of experimental units, each with real-valued potential outcomes under control and
treatment denoted by {Y t (0),Y t (1)} t∈N, respectively. These potential outcomes are fixed, but we observe
only one outcome for each unit in the experiment. We assign a randomized treatment to each unit, denoted
by the {0,1}-valued random variable Z ∈ F , observing Yobs := Y (Z ). Here treatment is assigned by
|     |     |     |     |     |     | t   | t   |     | t   | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
flipping a coin for each subject, with a bias possibly depending on previous observations. This treatment
assignment is the only source of randomness. Specifically, let P :=E Z and suppose 0<P <1 a.s. for
|     |     |     |     |     |     |     |     |     | t   | t−1 | t   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
all t; then we permit P t to vary between individuals and to depend on past outcomes. This accommodates
Efron’s biased coin design Efron (1971) and related covariate balancing methods.
At each step t, having treated and observed units 1,...,t, we wish to draw inference about the estimand
| :=t−1(cid:80)t |     |     |     |     |     |     |     |     |     |     |     | )∞  |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ATE t [Y i (1)−Y i (0)]. In particular, we seek a confidence sequence for (ATE t . To construct
|     |     | i=1 |     |     |     |     |     |     |     |     |     | t=1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
our estimator, we may utilize any predictions Y(cid:98)t (0) and Y(cid:98)t (1) for each unit’s potential outcomes; these
random variables must be F -measurable, for each t. We then employ the inverse probability weighting
t−1
estimator
|     |     |     |     |     |     |     | (cid:18) |     | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
Z −P
X :=Y(cid:98)t (1)−Y(cid:98)t (0)+ t t (Y obs−Y(cid:98)t (Z )), (25)
|     |     |     |     | t   |     |     |     |       |     | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | P   | ( 1−P | )   |     |     |     |     |
|     |     |     |     |     |     |     |     | t t   |     |     |     |     |     |
which is (conditionally) unbiased for the individual treatment effect Y (1)−Y (0). As with Theorem 4,
|     |     |     |     |     |     |     |     |     |     |     | t t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
better predictions will lead to shorter confidence intervals, but the coverage guarantee holds for any choice
of predictions, and a reasonable choice would be the average of past observed outcomes. See Aronow and
| Middleton | (2013) | for | a similar | strategy |     | for fixed-sample |     | estimation. |     |     |     |     |     |
| --------- | ------ | --- | --------- | -------- | --- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- |
We assume bounded potential outcomes; for simplicity we assume Y t (k) ∈ [0,1] for all t ≥ 1,k = 0,1, and
we assume predictions are likewise bounded. We further assume that treatment probabilities are uniformly
bounded away from zero and one. Then, an empirical-Bernstein confidence sequence for ATE follows from
t
| Theorem | 4, where | we  | use | X(cid:98)t =Y(cid:98)t | (1)−Y(cid:98)t | (0) | so that  |           |           |                   |         |     |      |
| ------- | -------- | --- | --- | ---------------------- | -------------- | --- | -------- | --------- | --------- | ----------------- | ------- | --- | ---- |
|         |          |     |     | t                      |                |     | t        | (cid:18)  | (cid:19)2 |                   |         |     |      |
|         |          |     |     | (cid:88)               |                |     | (cid:88) | Z −       | P         |                   |         |     |      |
|         |          |     | V   | :=                     | (X −X(cid:98)i | )2  | =        | i         | i         | (Y obs−Y(cid:98)i | (Z ))2. |     | (26) |
|         |          |     | t   |                        | i              |     |          |           |           | i                 | i       |     |      |
|         |          |     |     |                        |                |     |          | P i ( 1 − | P i )     |                   |         |     |      |
|         |          |     |     | i=1                    |                |     | i=1      |           |           |                   |         |     |      |
14

TLC ot suidar BCU fo oitaR 3
0.3
t
ETA rof BCU
2
0.2
0.1
1
0.0
0
|     |     |     | 102 | 103           |     | 104 105 | 102 |     | 103           | 104 105 |     |     |
| --- | --- | --- | --- | ------------- | --- | ------- | --- | --- | ------------- | ------- | --- | --- |
|     |     |     |     | t (log scale) |     |         |     |     | t (log scale) |         |     |     |
Figure5: Upperhalfof95%empirical-BernsteinconfidencesequenceforATE t underBernoullirandomizationbased
on one simulated sequence of i.i.d. observations, P ≡0.5, Y (0)∼Ber(0.5), Y (1)=ξ ∨Y (0) where ξ ∼Ber(0.2).
|     |     |     |     |     |     | t   | i   |     | i   | i i | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Grey line shows estimand ATE . Dotted line shows fixed-sample confidence bounds based on difference-in-means
t
estimator and normal approximation; these bounds fail to cover the true ATE at many times. Our bound uses
t
|     | (cid:80)t − | 1Y obs1 | (cid:80)t | − 11 |     |     |     |     |     |     |     |     |
| --- | ----------- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Y(cid:98)t (k)= i Zi=k / Zi=k , α=0.05 and a gamma-exponential mixture bound with ρ=12.6, chosen to
|          | i=  | 1         |      | i= 1      |     |     |     |     |     |     |     |     |
| -------- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| optimize | for | intrinsic | time | V t =100. |     |     |     |     |     |     |     |     |
Corollary 2. Suppose P ∈ [p ,1−p ] a.s., Y (k) ∈ [0,1] and Y(cid:98)t (k) ∈ [0,1] for all t ≥ 1,k = 0,1. Let
|     |     |     |     | t min |     | min t |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
u be any sub-exponential uniform boundary with scale 2/p and crossing probability α. Then
min
|     |     |     |     |     | (cid:18) |                              |     | (cid:19) |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | ---------------------------- | --- | -------- | --- | --- | --- | ---- |
|     |     |     |     |     |          | (cid:12) (cid:12)X¯ (cid:12) | u(V | t )      |     |     |     |      |
|     |     |     |     |     | P ∀t≥1:  | −ATE (cid:12)<               |     | ≥1−2α.   |     |     |     | (27) |
|     |     |     |     |     |          | t t                          | t   |          |     |     |     |      |
For u, one may choose the gamma-exponential mixture boundary (Proposition 9) or the stitched boundary
(10) with c = 2 . Figure 5 illustrates our strategy on simulated data. Over the range t = 100 to
pmin
t =100,000 displayed, our bound is about twice as wide as the fixed-sample CLT bound, with the ratio
√
growing at a slow O( logt) rate thereafter. Of course the fixed-sample CLT bound provides no uniform
| coverage | guarantee. |     |          |           |     |        |     |     |     |     |     |     |
| -------- | ---------- | --- | -------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
| 4.3      | Matrix     |     | iterated | logarithm |     | bounds |     |     |     |     |     |     |
Our second application is the construction of iterated logarithm bounds for random matrix sums and their
use in sequential covariance matrix estimation. The curved uniform bounds given in Section 3 may be
applied to matrix martingales by taking (S ) to be the maximum eigenvalue process of the martingale and
t
(V ) the maximum eigenvalue of the corresponding matrix variance process. Howard et al. (2020, Section 2)
t
give sufficient conditions for Definition 1 to hold in this matrix case. Then Theorem 1 yields a novel matrix
finiteLIL;herewegiveanexampleforboundedincrements. Wedenotethespaceofsymmetric, real-valued,
d×d matrices by Sd; γ (·) denotes the maximum eigenvalue; (cid:96) (v) = sloglog(ηv/m)+log dζ(s) ; and
|         |     |             | max |      |     |     |     | η,s |     |     | αlogsη |     |
| ------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- |
| k (η),k | (η) | are defined | in  | (8). |     |     |     |     |     |     |        |     |
1 2
|     |     |     |     | )∞  | Sd-valued |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Corollary 3. Suppose (Y t is a matrix martingale such that γ max (Y t −Y t−1 )≤b a.s. for all
|     |     |     | (cid:80)t | t=1 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t. Let V := γ ( E (Y −Y )2) and S := γ (Y ). Then for any η >1,s>1,m>0,α∈(0,1),
|     | t   | max | i=1 | t−1 t | t−1 | t max | t   |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
we have
|     |     |     | (cid:18) |     |     | (cid:112) |     | bk (η) |     | (cid:19) |     |     |
| --- | --- | --- | -------- | --- | --- | --------- | --- | ------ | --- | -------- | --- | --- |
P ∃t≥1:S ≥k (η) (V ∨m)(cid:96) (V ∨m)+ 2 (cid:96) (V ∨m) ≤α. (28)
|     |     |     |     |     | t 1 | t η,s | t   |     | η,s t |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
3
The result follows using the polynomial stitched boundary after invoking Fact 1(c) and Lemma 2 of Howard
etal.(2020)(cf. (Tropp,2011)),whichshowthat(S t )issub-gammawithvarianceprocess(V t ),scalec=b/3,
and l = d. Beyond bounded increments, the same bound holds for any sub-gamma process. As evidenced
0
| by Proposition |     | 1,  | this is | a very | general | condition. |     |     |     |     |     |     |
| -------------- | --- | --- | ------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- |
Taking η and s arbitrarily close to one and using the final result of Theorem 1, we obtain the following
asymptotic matrix upper LIL, proved in Appendix A.9. Here we denote the martingale increments by
| ∆Y t | :=Y t −Y | t−1 | .   |     |     |     |     |     |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15

(cid:16) (cid:17)
Corollary4. Let(Y )∞ beaSd-valued,square-integrablemartingale,anddefineV =γ (cid:80)t E ∆Y2 .
t t=1 t max i=1 i−1 t
Then
(cid:26) (cid:27)
γ (Y )
limsup√ max t ≤1 a.s. on supV =∞ (29)
t
2V loglogV
t→∞ t t t
whenevereither(1)theincrements(∆Y )arei.i.d.,or(2)theincrements(∆Y )satisfyaBernsteincondition
t t
on higher moments: for some c>0, for all t and all k >2, E (∆Y )k (cid:22)(k!/2)ck−2E ∆Y2.
t−1 t t−1 t
TheBernsteinconditionholdsiftheincrementsareuniformlybounded,γ (∆Y )≤cforsomec>0. Also,
max t
inthei.i.d.case,P(V →∞)=1andthen(29)statesthatlimsup γ (Y )/ (cid:112) 2γ (E∆Y2)tloglogt≤1,
t t→∞ max t max 1
a.s. on {sup V =∞}. When d=1, this recovers the classical upper LIL, showing that Corollary 4 cannot
t t
be improved uniformly, but we are not aware of an appropriate lower bound for the general matrix case.
We now consider the nonasymptotic sequential estimation of a covariance matrix based on bounded vector
observations (Rudelson, 1999; Vershynin, 2012; Gittens and Tropp, 2011; Tropp, 2015; Koltchinskii and
Lounici, 2017). In particular, we observe a sequence of independent, mean zero, Rd-valued random vectors
x with common covariance matrix Σ = Ex xT. We wish to estimate Σ using an operator-norm confidence
t t t
ball cent
√
ered at the empirical covariance matrix Σ(cid:98)t := t−1(cid:80)t
i=1
x
i
xT
i
. For fixed-sample estimation, when
(cid:107)x (cid:107) ≤ b a.s. for all i∈[t], the analysis of Tropp (2015, section 1.6.3) implies
i 2
(cid:32) (cid:114) (cid:33)
2b(cid:107)Σ(cid:107) log(2d/α) 4blog(2d/α)
P (cid:107)Σ(cid:98)t −Σ(cid:107)
op
≥ op
t
+
3t
≤α. (30)
We use a sub-Poisson uniform boundary to obtain a uniform analogue:
√
Corollary 5. Let (x )∞ be a sequence of Rd-valued, independent random vectors with Ex =0, (cid:107)x (cid:107) ≤ b
t t=1 t t 2
a.s. and Ex xT =Σ for all t. If u is a sub-Poisson uniform boundary with crossing probability α and scale
t t
2b, then
(cid:18) (cid:19)
1
P ∃t≥1:(cid:107)Σ(cid:98)t −Σ(cid:107)
op
≥
t
u(bt(cid:107)Σ(cid:107)
op
) ≤α. (31)
For example, using the polynomial stitched bound with scale c=2b/3 and m=b(cid:107)Σ(cid:107) , Corollary 5 gives a
op
(cid:112)
(1−α)-confidence sequence for Σ with operator norm radius O( t−1loglogt). This bound has the closed
form
(cid:32) (cid:114) (cid:33)
b(cid:107)Σ(cid:107) (cid:96)(t) 4bk (cid:96)(t)
P ∃t≥1:(cid:107)Σ(cid:98)t −Σ(cid:107)
op
≥k
1 t
op +
3
2
t
≤α, (32)
where (cid:96)(t)=sloglog(ηt)+log dζ(s) , and k ,k are defined in (8).
αlogsη 1 2
In other words, with high probability, we have for all t≥1 that
(cid:114)
blog(dlogt) blog(dlogt)
(cid:107)Σ(cid:98)t −Σ(cid:107)
op
(cid:46)
t
+
t
. (33)
Compared to the fixed-sample result (30), we obtain uniform control by adding a factor of loglogt. We are
not aware of other results like these for sequential covariance matrix estimation. Figure 6 illustrates the
confidence sequence of Corollary 5 on simulated data using a discrete mixture boundary with the mixture
density fLIL defined in (85).
s
4.4 One-parameter exponential families
Suppose (X ) are i.i.d. from an exponential family in mean parametrization, with sufficient statistic T(X)
t
having mean in some set Ω. For each µ∈Ω, we write the density as f (x)=h(x)exp{θ(µ)T(x)−A(θ(µ))}
µ
where A(cid:48)(θ(µ)) = µ. Let ψ be the cumulant-generating function of T(X )−µ when ET(X ) = µ, that
µ 1 1
is, ψ (λ):=A(λ+θ(µ))−A(θ(µ))−λµ, with ψ (λ) := ∞ if the RHS does not exist. Writing S (µ) :=
µ µ t
(cid:80)t
T(X )−tµ, the process exp{λS (µ)−tψ (λ)} is the likelihood ratio testing H : θ = θ(µ) against
i=1 i t µ 0
H :θ =θ(µ)+λ, and if we use a method-of-mixtures uniform boundary, the resulting confidence sequence
1
willbedualtoafamilyofmixturesequentialprobabilityratiotests,asdiscussedinSection6. Toobtainatwo-
sided confidence sequence, we use the “reversed” CGF ψ˜ (λ)= ψ (−λ). We summarize these observations
µ µ
as follows; see Lai (1976b, Theorem 1) for a related result.
16

|     |     |                                  | =200 |     |     |                                  | =500 |     |     |                   | =2,000 |     |     |     |
| --- | --- | -------------------------------- | ---- | --- | --- | -------------------------------- | ---- | --- | --- | ----------------- | ------ | --- | --- | --- |
|     |     |                                  | t    |     |     |                                  | t    |     |     |                   | t      |     |     |     |
|     |     | etanidrooc dnoceS Confidence set |      |     |     | etanidrooc dnoceS Confidence set |      |     |     | etanidrooc dnoceS |        |     |     |     |
Confidence set
|     |     |                  | True Σ |     |     |                  | True Σ |     |     |                  | True Σ |     |     |     |
| --- | --- | ---------------- | ------ | --- | --- | ---------------- | ------ | --- | --- | ---------------- | ------ | --- | --- | --- |
|     |     | First coordinate |        |     |     | First coordinate |        |     |     | First coordinate |        |     |     |     |
Figure 6: The matrix confidence sequence of Corollary 5 based on one simulated sequence. Observations are drawn
|     |     |     | √ √ |     | √   | √   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i.i.d. taking values ±( 2 2)T, ±(1/ 2 −1/ 2)T each with probability 1/4, with covariance matrix Σ= 1(53),
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 4 35 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
which is represented by the ellipse xTΣ−1x = 1. Confidence ball with level α = 0.05 is represented by shaded
area between ellipses corresponding to elements of the confidence ball with minimal and maximal trace. Confidence
sequencefromCorollary5usesb=4andadiscretemixtureboundarywithψ=ψ G usingc=2b/3, mixturedensity
fLIL from (85) with s=1.4 matching (11), η=1.1 and λ=0.262 chosen as described in Appendix E.
1.4
|     |     | Bernoulli(0.5) |     |     |     | Bernoulli(0.01) |     |     |     | Three point |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --------------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
etar evitisop eslaF
0.20
0.20
|     |     | 0.15 |     |     |     | 0.15 |     |     |     | 0.10 |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
0.10
0.10
0.05
|     |     | 0.05 |         |         |     | 0.05 |     |         |     |      |     |         |     |     |
| --- | --- | ---- | ------- | ------- | --- | ---- | --- | ------- | --- | ---- | --- | ------- | --- | --- |
|     |     | 0.00 |         |         |     | 0.00 |     |         |     | 0.00 |     |         |     |     |
|     |     |      | 101 102 | 103 104 | 105 | 101  | 102 | 103 104 | 105 | 101  | 102 | 103 104 | 105 |     |
|     |     |      |         |         |     |      |     |         |     |      |     |         |     |     |
1.00
10.0
htdiw IC 1.00
|     |     | 0.30 |     |     |     | 0.10 |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
1.0
0.10
0.01
0.03
0.1
|     |     |     | 101 102           | 103 104            | 105 | 101               | 102                      | 103 104 | 105 | 101               | 102            | 103 104 | 105 |     |
| --- | --- | --- | ----------------- | ------------------ | --- | ----------------- | ------------------------ | ------- | --- | ----------------- | -------------- | ------- | --- | --- |
|     |     |     | Number of samples |                    |     | Number of samples |                          |         |     | Number of samples |                |         |     |     |
|     |     |     |                   | Beta-Binomial      |     |                   | Pointwise Bernoulli      |         |     |                   | Hoeffding      |         |     |     |
|     |     |     |                   | Naive SN           |     |                   | Empirical Bernstein      |         |     |                   |                |         |     |     |
Figure 7: Summary of 1,000 simulations, each with 100,000 i.i.d. observations from the indicated distribution. Top
panels show the proportion of replications in which the 95%-confidence sequence has excluded the true mean by
time t. Bottom panels show the mean confidence interval width. The “three point” distribution takes values −1.408
and 1 with probability 0.495 each, and takes value 20 with probability 0.01. “Hoeffding” uses a normal mixture
boundary (14), while“Beta-Binomial” uses the beta-binomial mixture (Proposition 7). “Pointwise Bernoulli” uses a
nonasymptotic bound based on the Bernoulli KL-divergence which is valid pointwise but not uniformly. “Empirical
Bernstein”usesthestrategygiveninTheorem4withagamma-exponentialmixtureboundary,Proposition9. “Naive
SN”usesanormalmixtureboundarywithanempiricalvarianceestimate,whichdoesnotguaranteecoverage. Inall
| cases, ρ | is chosen | to optimize |     | for a sample | size | of t=500. |     |     |     |     |     |     |     |     |
| -------- | --------- | ----------- | --- | ------------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Corollary 6. Suppose, for each µ∈Ω, u µ is a sub-ψ µ uniform bound with crossing probability α 1 , and u˜ µ
| is a sub-ψ˜ | uniform     |     | bound | with crossing |              | probability | α       | . Defining |       |         |     |     |     |      |
| ----------- | ----------- | --- | ----- | ------------- | ------------ | ----------- | ------- | ---------- | ----- | ------- | --- | --- | --- | ---- |
|             | µ           |     |       |               |              |             | 2       |            |       |         |     |     |     |      |
|             |             |     |       | CI            | t :={µ∈Ω:−u˜ |             | µ (t)<S | t          | (µ)<u | µ (t)}, |     |     |     | (34) |
| we have     | P(∀t≥1:ET(X |     | )∈CI  | )≥1−α         |              | −α          | .       |            |       |         |     |     |     |      |
|             |             |     | 1     | t             |              | 1           | 2       |            |       |         |     |     |     |      |
17

5 Simulations
In1 Figure 7 we illustrate the error control of some of our confidence sequences for estimating the mean of
an i.i.d. sequence of observations (X ) with bounded support [a,b]. We compare four strategies:
i
1. TheHoeffdingstrategyexploitsthefactthatboundedobservationsaresub-Gaussian(Hoeffding,1963;
cf. Howardetal.,2020,Lemma3(c)). Weuseatwo-sidednormalmixtureboundary(14)withvariance
| process | V =(b−a)2t/4. |     |     |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- | --- |
t
2. The beta-binomial strategy uses the stronger condition that bounded observations are sub-Bernoulli
(Hoeffding, 1963; cf. Howard et al., 2020, Fact 1(b)), accounting for the true mean as well as the
boundedness, but possibly failing to take account of the true variance. For hypothesized true mean µ,
thisstrategyusesthebeta-binomialmixtureboundarygiveninProposition7, withparametersg(µ)=
µ−a and h(µ) = b−µ, and variance process V t (µ) = g(µ)h(µ)t. The confidence set for the mean is
(cid:80)t
{µ∈[a,b]:−f (V (µ))≤ X −tµ≤f (V (mu))}. Thisismoreefficientlycomputed
|     | g(µ),h(µ) | t   | i=1 | i h(µ),g(µ) | t   |     |     |
| --- | --------- | --- | --- | ----------- | --- | --- | --- |
(cid:80)t
using the mixture supermartingale m(S ,V ) of (57), as {µ∈[a,b]:m( X −tµ,V (µ))<1/α}.
|     |     |     |     | t t |     | i=1 i | t   |
| --- | --- | --- | --- | --- | --- | ----- | --- |
3. The pointwise Bernoulli strategy uses the same sub-Bernoulli condition as the beta-binomial strategy,
but relies on a fixed-sample Cram´er-Chernoff bound which is valid pointwise but not uniformly over
|     |     |     |     | ψ(cid:63)(S | logα−1, |     |     |
| --- | --- | --- | --- | ----------- | ------- | --- | --- |
time. Specifically, we reject mean µ if V t t /V t ) ≥ where S t is the sum of centered
B
observations as usual, V = (µ − a)(b − µ)t, and we set g =µ−a,h=b−µ in ψ , with ψ(cid:63) its
|                  |     | t          |     |     |     |     | B B |
| ---------------- | --- | ---------- | --- | --- | --- | --- | --- |
| Legendre-Fenchel |     | transform. |     |     |     |     |     |
4. The empirical-Bernstein strategy uses an empirical estimate of variance, thus achieving a confidence
width scaling with the true variance in all three cases. Here we use Theorem 4 with a gamma-
exponential mixture boundary (Proposition 9). For predictions, we use the mean of past observations:
| =(t−1)−1(cid:80)t |     | − 1X |     |     |     |     |     |
| ----------------- | --- | ---- | --- | --- | --- | --- | --- |
| X(cid:98)t        |     | i .  |     |     |     |     |     |
|                   |     | i= 1 |     |     |     |     |     |
5. The naive self-normalized (“Naive SN”) strategy plugs the empirical variance estimate, the sum of
squaredpredictionerrorsfromTheorem4,intothetwo-sidednormalmixture(14). Itignoresthefacts
that the observations are not sub-Gaussian with respect to their true variance and that the variance
is estimated. This strategy is similar to that of Johari et al. (2017) and does not guarantee coverage.
Though it will sometimes control false positives, coverage rates can easily be inflated for asymmetric,
| heavy-tailed | distributions, | as we | illustrate. |     |     |     |     |
| ------------ | -------------- | ----- | ----------- | --- | --- | --- | --- |
We present three cases of bounded distributions. The first case is the easiest, with Ber(0.5) observations.
Herethesub-Gaussianvarianceparameterbasedontheboundednessoftheobservationsisequaltothetrue
variance,sotheHoeffdingstrategyperformswell. Theempirical-Bernsteinstrategyisonlyalittlewider,and
all four successfully control false positives. The story changes with the more difficult Ber(0.01) distribution,
however. The Hoeffding boundary is far too wide, since it fails to make use of information about the true
variance. Thebeta-binomialboundusesinformationaboutvarianceprovidedbythefirstmomenttoachieve
the correct scaling. The naive self-normalized strategy, on the other hand, yields confidence intervals that
are too small and fail to control false positive rate. The empirical-Bernstein strategy, though only slightly
widerthanthenaiveboundforlargesamplesizes, givesjustenoughextrawidthtocontrolthefalsepositive
rate and is nearly as narrow as the beta-binomial bound. The final, three-point distribution takes values
−1.408 and 1 with probability 0.495 each, and takes value 20 with probability 0.01. Here the beta-binomial
strategyyieldsconfidenceintervalsthataretoowide. Inthismostdifficultcase,onlytheempirical-Bernstein
| strategy yields | tight intervals | while controlling |     | false positive | rates.  |     |     |
| --------------- | --------------- | ----------------- | --- | -------------- | ------- | --- | --- |
| 6 Implications  |                 | for sequential    |     | hypothesis     | testing |     |     |
We have organized our presentation around confidence sequences and closely related uniform concentration
bounds due to our belief that they offer a useful “user interface” for sequential inference. However, our
methods also yield always-valid p-values (Johari et al., 2015) for sequential tests. Indeed, a slew of related
1The repository https://github.com/gostevehoward/cspaper contains code to reproduce all simulations and plots in this
paper. Uniform boundaries themselves are implemented in R and Python packages at https://github.com/gostevehoward/
confseq.
18

definitions from the literature are equivalent or “dual” to one another. Here we briefly discuss these connec-
tions. The following result, proved in Appendix C.4, gives equivalent formulations of common definitions in
| sequential | testing. |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 3. Let (A )∞ be an adapted sequence of events in some filtered probability space and let A :=
|        |     | t t=1           |     |                 |     |     |     |     |     |     |     |     | ∞   |
| ------ | --- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| limsup | A   | . The following |     | are equivalent: |     |     |     |     |     |     |     |     |     |
| t→∞    |     | t               |     |                 |     |     |     |     |     |     |     |     |     |
(cid:83)∞
| (a) P( |     | A )≤α. |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t=1 t
P(A
| (b) | )≤α | for all | random | (not | necessarily | stopping) | times | T.  |     |     |     |     |     |
| --- | --- | ------- | ------ | ---- | ----------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
T
P(A
| (c) | τ )≤α | for all | stopping | times | τ, possibly | infinite. |     |     |     |     |     |     |     |
| --- | ----- | ------- | -------- | ----- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Ourdefinitionofconfidencesequences(1),basedonDarlingandRobbins(1967a)andLai(1984),differsfrom
P(θ
that Johari et al. (2015), who require that τ ∈CI τ )≥1−α for all stopping times τ. They allow τ =∞
by defining CI := liminf CI . By taking A := {θ ∈/ CI } in Lemma 3, we see that the distinction
|     |     | ∞   | t→∞ | t   |     | t   | t   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is immaterial, and furthermore that we could equivalently define confidence sequences in terms of arbitrary
random times, not necessarily stopping times. This generalizes Proposition 1 of Zhao et al. (2016).
Always-valid p-values and tests of power one Asanalternativetoconfidencesequences, Joharietal.
(2015)defineanalways-validp-valueprocess forsomenullhypothesisH asanadapted,[0,1]-valuedsequence
0
| )∞  |     | P   |     |     |     |     |     | P   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(p satisfying (p ≤α)≤α for all stopping times τ, where denotes probability under the null H .
| t t=1 |     | 0 τ |     |     |     |     |     | 0   |     |     |     |     | 0   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TakingA :={p ≤α}inLemma3showsthatwemayreplacethisdefinitionwithanequivalentoneoverall
t t
|     |     |     |     |     |     |     |     |     | P   | N   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
random times, not necessarily stopping times, or with the uniform condition 0 (∃t ∈ : p t ≤ α) ≤ α. By
analogy to the usual dual construction between fixed-sample p-values and confidence intervals, one can see
that confidence sequences are dual to always-valid p-values, and both are dual to sequential tests, as defined
by a stopping time and a binary random variable indicating rejection (Johari et al., 2015, Proposition 5). In
particular,forthenullH :θ =θ(cid:63),if(CI )isa(1−α)-confidencesequenceforθ,itisclearthatatestwhich
|     |     |     | 0   |     | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stopsandrejectsthenullassoonasθ(cid:63) ∈/ CI controlstypeIerror: P (reject H )=P (∃t∈N:θ(cid:63) ∈/ CI )≤α.
|     |     |     |     |     | t   |     |     | 0   | 0   | 0   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Typically, then, aconfidencesequencebasedonanyofthecurveduniformboundsinthispaper, withradius
u(v) = o(v), will yield a test of power one (Darling and Robbins, 1967b; Robbins, 1970). In particular, for
|     |     |     |     | X¯  |     |     |     | X¯  | a .s. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
a confidence sequence with limits ±u(V ), it is sufficient that → θ and limsup V /t < ∞ a.s.,
|     |     |     |     |     | t t |     |     | t   |     |     | t→∞ t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
conditions that usually hold. These conditions imply that the radius of the confidence sequence, u(V )/t,
t
|     |     |     |     | X¯  |     |     |     |     | θ(cid:63) |     | θ(cid:63), |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- |
approaches zero, while the center t is eventually bounded away from whenever θ (cid:54)= so that the
| confidence | sequence | eventually |     | excludes | θ(cid:63) with | probability | one. |     |     |     |     |     |     |
| ---------- | -------- | ---------- | --- | -------- | -------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
In the one-parameter exponential family case considered in Section 4.4, as noted above, the exponential
process exp{λS (µ)−tψ (t)} is exactly the likelihood ratio for testing H : θ = θ(µ) against H : θ =
|     |     | t   | µ   |     |     |     |     |     | 0   |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θ(µ) + λ. From the definitions (34) and (2) we see that, when using a mixture uniform boundary, a
µ(cid:63)
sequential test which rejects as soon as the confidence sequence of Corollary 6 excludes can be seen
(cid:82)
as equivalently rejecting as soon as either of the mixture likelihood ratios exp{λS −ψ (λ)t}dF(λ) or
t µ(cid:63)
(cid:82) exp{−λS −ψ (−λ)t}dF(λ) exceeds 2/α. Thus a sequential hypothesis test built upon a mixture-based
t µ(cid:63)
confidence sequence is equivalent to a mixture sequential probability ratio test (Robbins, 1970) in the para-
metric setting. As discussed in Appendix A.6, stitching can be viewed as an approximation to certain
mixture bounds, so that hypothesis tests based on stitched bounds are also approximations to mixture
SPRTs. Importantly, our confidence sequences are natural nonparametric generalizations of the mixture
| SPRT, | recovering | various | mixture | SPRTs | in  | the parametric | settings. |     |     |     |     |     |     |
| ----- | ---------- | ------- | ------- | ----- | --- | -------------- | --------- | --- | --- | --- | --- | --- | --- |
Pros and cons of the running intersection Our definition (1) of a confidence sequence allows for
the parameter θ to vary with t. It is common in the literature on sequential testing to assume a single,
t
stationaryparameter,θ ≡θ,butthisassumptionhasatroublesomeconsequenceinthecontextofconfidence
t
P(∀t
sequences. If the confidence sequence (CI t ) satisfies : θ ∈ CI t ) ≥ 1−α, then the running intersection
C(cid:102)I := ∩ CI is also uniformly valid for θ, is never larger and may be much smaller. This was observed
| t   | s≤t | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by Darling and Robbins (1967b), and is used in the implementation of Johari et al. (2017), for example. (In
the language of sequential testing, if (p )∞ is an always-valid p-value process, then so is (min p )∞ .)
|     |     |     |     |     | t t=1 |     |     |     |     |     | s≤t | s t=1 |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- |
However, the intersected intervals C(cid:102)I may become empty at some point. This is particularly likely if
t
the underlying parameter is drifting over time, contrary to the assumption of stationarity or identically-
distributed observations, and such a drift would be the likely interpretation of this event in practice. In this
19

non-stationary case, the non-intersected sequence is the more sensible one to use. The solution of Johari
et al. (2017) is to “reset” the experiment, discarding data accumulated up to that point, on the rationale
thatsuchaneventindicatesthatpreviousdataarenolongerrelevanttoestimationofthecurrentparameter
of interest. However, this means that our confidence sequence can go from a very high precision estimate
at some time t to knowing almost nothing at time t+1, which is difficult for an experimenter to interpret
and could lead to misleading inference just before the reset. Jennison and Turnbull (1989) make a case for
the non-intersected intervals on slightly different grounds, arguing that estimation at time t ought to be
a function of the sufficient statistic at that time. Shifting to the potential outcomes model in Section 4.2
neatlyavoidsthisissue: becausetheestimandischangingateachtime, thenon-intersectedintervalsarethe
only reasonable choice for estimating ATE and no conceptual difficulty remains.
t
7 Summary and future work
We have discussed four techniques for deriving curved uniform boundaries, each improving upon past work,
with careful attention paid to constants and to practical issues. By building upon the general framework
of Howard et al. (2020), we have emphasized the nonparametric applicability of our boundaries. A leading
example of the utility of this approach is the general empirical-Bernstein bound, with an application to
sequential causal inference, and we have also shown how our framework immediately yields novel results for
matrix martingales.
7.1 Other related work
We introduced the method of mixtures and the epoch-based analyses in Section 1.1. Two other methods of
extending the SPRT deserve mention, though they are distinct from our approaches. First, the approach
of Robbins and Siegmund (1972, 1974) examines (cid:81) f (X )/f (X ) where λˆ is a “nonanticipating”
i λˆ i−1 i 0 i i−1
estimate based on X ,...,X . This is similar to a generalized likelihood ratio but modified to retain the
1 i−1
martingaleproperty(cf. Wald(Wald,1947,section10.5),(LordenandPollak,2005)). Second,thesequential
(cid:81)
generalized likelihood ratio approach examines sup f (X )/f (X ), which is not a martingale under the
λ i λ i 0 i
null (Siegmund and Gregory, 1980; Lai, 1997; Kulldorff et al., 2011).
The concept of test (super)martingales expounded by Shafer et al. (2011) is related to our methods for con-
ducting inference based on Ville’s inequality applied to nonnegative supermartingales. Their main example
is the Beta mixture for i.i.d. Bernoulli observations, an example which originated with Ville (1939) and
discussedbyRobbins(1970)andLai(1976b). Arecent“safetesting”frameworkofGru¨nwaldetal.(2019)is
also tightly related. In terms of these frameworks, our work can be viewed as constructing “safe confidence
intervals” (and thus safe tests) using nonparametric test supermartingales.
Averydifferentapproachisthatofgroupsequentialmethods(Pocock,1977;O’BrienandFleming,1979;Lan
and DeMets, 1983; Jennison and Turnbull, 2000). These methods rely on either exact discrete distributions
or asymptotics to assume exact normality of group increments, either of which permits computation of
sequential boundaries via numerical integration. The resulting confidence sequences are tighter than ours,
but lack nonasymptotic guarantees or closed-form results and do not support continuous monitoring.
A related problem is that of terminal confidence intervals, in which one assumes a rigid stopping rule and
wishestoconstructaconfidenceintervalupontermination. Siegmund(1978)gaveananalyticaltreatmentof
the problem; numerical methods are also available for group sequential tests (Jennison and Turnbull, 2000,
section 8.5). However, the idea of a rigid stopping rule is often restrictive.
7.2 Future work
We discuss in Appendix I how our work may be extended to martingales in smooth Banach spaces and
real-valued, continuous-time martingales. It may be fruitful to explore applications in those areas.
Our consideration of optimality has been limited to the discussion in Section 3.6. It would be valuable to
furtherexplorevariousoptimalitypropertiesfornonasymptoticuniformbounds. Forexample,itisstandard
in sequential testing to compute the expected sample size to reject a null under parametric alternatives.
Though we target less restrictive assumptions, it may be instructive to compute bounds in special cases.
20

Second, a natural counterpoint to our uniform concentration bounds would be a set of uniform anticon-
centration bounds. This would yield a nonasymptotic extension of the “lim inf” half of the classical LIL.
Balsubramani (2014, Theorem 3) gives one such interesting result. Last, in practice, one will rarely require
updated inference after every observation, and may be content to take observations in groups. Further, one
maybesatisfiedwithafinitetimehorizonGarivierandLeonardi(2011). Thisisthedomaininwhichgroup-
sequentialmethodsshine,butSPRT-basedmethodscanbemadecompetitivebyestimatingthe“overshoot”
of the stopped supermartingale (Lai and Siegmund, 1977, 1979; Siegmund, 1985; Whitehead and Stratton,
1983). Itwouldbeinterestingtounderstandwhethersuchimprovementsworkoutinnonparametricsettings.
Acknowledgments
Howard thanks ONR Grant N00014-15-1-2367. Sekhon thanks ONR grants N00014-17-1-2176 and N00014-
15-1-2367. Ramdas thanks NSF grant DMS1916320. We thank Boyan Duan and Ian Waudby-Smith as well
| as the referees/AE | for useful | suggestions. |     |     |     |
| ------------------ | ---------- | ------------ | --- | --- | --- |
References
Armitage,P.,McPherson,C.K.andRowe,B.C.(1969),‘Repeatedsignificancetestsonaccumulatingdata’,
| Journal | of the Royal | Stat. Society, | Series | A 132(2), 235–244. |     |
| ------- | ------------ | -------------- | ------ | ------------------ | --- |
Aronow, P. M. and Middleton, J. A. (2013), ‘A class of unbiased estimators of the average treatment effect
| in randomized | experiments’, | Journal | of  | Causal Inference | 1(1), 135–154. |
| ------------- | ------------- | ------- | --- | ---------------- | -------------- |
Audibert, J.-Y., Munos, R. and Szepesv´ari, C. (2009), ‘Exploration–exploitation tradeoff using variance
estimates in multi-armed bandits’, Theoretical Computer Science 410(19), 1876–1902.
Azuma, K. (1967), ‘Weighted sums of certain dependent random variables.’, Tohoku Mathematical Journal
19(3), 357–367.
Balsubramani, A. (2014), ‘Sharp Finite-Time Iterated-Logarithm Martingale Concentration’,
| arXiv:1405.2639 | .   |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Balsubramani, A. and Ramdas, A. (2016), Sequential Nonparametric Testing with the Law of the Iterated
Logarithm, in ‘Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence’,
| UAI’16, | AUAI Press, | pp. 42–51. |     |     |     |
| ------- | ----------- | ---------- | --- | --- | --- |
Bercu, B., Delyon, B. and Rio, E. (2015), Concentration Inequalities for Sums and Martingales, Springer
| International | Publishing, | Cham. |     |     |     |
| ------------- | ----------- | ----- | --- | --- | --- |
Bercu,B.andTouati,A.(2008),‘Exponentialinequalitiesforself-normalizedmartingaleswithapplications’,
| The Annals | of Applied | Probability | 18(5), | 1848–1869. |     |
| ---------- | ---------- | ----------- | ------ | ---------- | --- |
Berman, R., Pekelis, L., Scott, A. and Van den Bulte, C. (2018), p-hacking and false discovery in A/B
| testing, | Technical Report | 3204791, | SSRN. |     |     |
| -------- | ---------------- | -------- | ----- | --- | --- |
Boucheron, S., Lugosi, G. and Massart, P. (2013), Concentration inequalities: a nonasymptotic theory of
| independence, | 1st edn, | Oxford | University | Press, Oxford. |     |
| ------------- | -------- | ------ | ---------- | -------------- | --- |
Chernoff, H. (1952), ‘A measure of asymptotic efficiency for tests of a hypothesis based on the sum of
| observations’, | The Annals | of Mathematical |     | Statistics 23(4), | 493–507. |
| -------------- | ---------- | --------------- | --- | ----------------- | -------- |
Cram´er, H. (1938), ‘Sur un nouveau th´eor`eme-limite de la th´eorie des probabilit´es’, Actualit´es Scientifiques
736.
Darling,D.A.andRobbins,H.(1967a),‘ConfidenceSequencesforMean,Variance,andMedian’,Proceedings
| of the National | Academy | of Sciences | 58(1), | 66–68. |     |
| --------------- | ------- | ----------- | ------ | ------ | --- |
Darling, D. A. and Robbins, H. (1967b), ‘Iterated Logarithm Inequalities’, Proceedings of the National
| Academy | of Sciences | 57(5), 1188–1192. |     |     |     |
| ------- | ----------- | ----------------- | --- | --- | --- |
21

Darling,D.A.andRobbins,H.(1968),‘SomeFurtherRemarksonInequalitiesforSampleSums’,Proceedings
| of the | National | Academy |     | of Sciences | 60(4), | 1175–1182. |     |
| ------ | -------- | ------- | --- | ----------- | ------ | ---------- | --- |
de la Pen˜a, V. H. (1999), ‘A General Class of Exponential Inequalities for Martingales and Ratios’, The
| Annals | of Probability |     | 27(1), | 537–564. |     |     |     |
| ------ | -------------- | --- | ------ | -------- | --- | --- | --- |
de la Pen˜a, V. H., Klass, M. J. and Lai, T. L. (2004), ‘Self-normalized processes: exponential inequalities,
moment bounds and iterated logarithm laws’, The Annals of Probability 32(3), 1902–1933.
de la Pen˜a, V. H., Klass, M. J. and Lai, T. L. (2007), ‘Pseudo-maximization and self-normalized processes’,
| Probability |     | Surveys | 4, 172–192. |     |     |     |     |
| ----------- | --- | ------- | ----------- | --- | --- | --- | --- |
delaPen˜a,V.H.,Klass,M.J.andLai,T.L.(2009),‘Theoryandapplicationsofmultivariateself-normalized
| processes’, | Stochastic |     | Processes |     | and their | Applications | 119(12), 4210–4227. |
| ----------- | ---------- | --- | --------- | --- | --------- | ------------ | ------------------- |
de la Pen˜a, V. H., Lai, T. L. and Shao, Q.-M. (2009), Self-normalized processes: limit theory and statistical
| applications, |     | Springer, | Berlin. |     |     |     |     |
| ------------- | --- | --------- | ------- | --- | --- | --- | --- |
Delyon, B. (2009), ‘Exponential inequalities for sums of weakly dependent variables’, Electronic Journal of
| Probability |            | 14, 752–779. |              |        |     |               |         |
| ----------- | ---------- | ------------ | ------------ | ------ | --- | ------------- | ------- |
| Durrett,    | R. (2017), |              | Probability: | Theory |     | and Examples, | 5a edn. |
Efron, B. (1971), ‘Forcing a sequential experiment to be balanced’, Biometrika 58(3), 403–417.
Fan,X.,Grama,I.andLiu,Q.(2015),‘Exponentialinequalitiesformartingaleswithapplications’,Electronic
| Journal | of Probability |     | 20(1), | 1–22. |     |     |     |
| ------- | -------------- | --- | ------ | ----- | --- | --- | --- |
Freedman, D. A. (1975), ‘On Tail Probabilities for Martingales’, The Annals of Probability 3(1), 100–118.
Fulks,W.(1951),‘AGeneralizationofLaplace’sMethod’,ProceedingsoftheAmericanMathematicalSociety
2(4), 613–622.
Garivier, A. (2013), Informational confidence bounds for self-normalized averages and applications, in ‘2013
| IEEE | Information |     | Theory | Workshop |     | (ITW)’, IEEE, | pp. 1–5. |
| ---- | ----------- | --- | ------ | -------- | --- | ------------- | -------- |
Garivier, A. and Leonardi, F. (2011), ‘Context tree selection: A unifying view’, Stochastic Processes and
| their | Applications |     | 121(11), | 2488–2506. |     |     |     |
| ----- | ------------ | --- | -------- | ---------- | --- | --- | --- |
Gittens, A. and Tropp, J. A. (2011), ‘Tail bounds for all eigenvalues of a sum of random matrices’, ACM
| Report | 2014-02, | Caltech |     | .   |     |     |     |
| ------ | -------- | ------- | --- | --- | --- | --- | --- |
Gru¨nwald, P., de Heide, R. and Koolen, W. (2019), ‘Safe testing’, arXiv:1906.07801 .
Hoeffding, W. (1963), ‘Probability Inequalities for Sums of Bounded Random Variables’, Journal of the
| American | Statistical |     | Association |     | 58(301), | 13–30. |     |
| -------- | ----------- | --- | ----------- | --- | -------- | ------ | --- |
Howard, S. R., Ramdas, A., McAuliffe, J. and Sekhon, J. (2020), ‘Time-uniform Chernoff bounds via non-
| negative | supermartingales’, |     |     | Probability |     | Surveys 17, | 257–317. |
| -------- | ------------------ | --- | --- | ----------- | --- | ----------- | -------- |
Imbens, G. W. and Rubin, D. B. (2015), Causal Inference for Statistics, Social, and Biomedical Sciences:
| An Introduction, |     |     | 1 edn, | Cambridge | University | Press. |     |
| ---------------- | --- | --- | ------ | --------- | ---------- | ------ | --- |
Jamieson, K. and Jain, L. (2018), A bandit approach to multiple testing with false discovery control, in
‘Proceedings of the 32nd International Conference on Neural Information Processing Systems’, pp. 3664–
3674.
Jamieson,K.,Malloy,M.,Nowak,R.andBubeck,S.(2014),lil’UCB:AnOptimalExplorationAlgorithmfor
Multi-ArmedBandits, in‘ProceedingsofThe27thConferenceonLearningTheory’, Vol.35, pp.423–439.
Jamieson, K. and Nowak, R. (2014), Best-arm identification algorithms for multi-armed bandits in the fixed
confidence setting, in ‘48th Annual Conference on Information Sciences and Systems (CISS)’, pp. 1–6.
Jennison, C. and Turnbull, B. W. (1984), ‘Repeated confidence intervals for group sequential clinical trials’,
| Controlled | Clinical |     | Trials | 5(1), | 33–45. |     |     |
| ---------- | -------- | --- | ------ | ----- | ------ | --- | --- |
22

Jennison, C. and Turnbull, B. W. (1989), ‘Interim Analyses: The Repeated Confidence Interval Approach’,
| Journal | of the | Royal Statistical |     | Society, | Series | B 51(3), | 305–361. |
| ------- | ------ | ----------------- | --- | -------- | ------ | -------- | -------- |
Jennison, C. and Turnbull, B. W. (2000), Group sequential methods with applications to clinical trials,
| Chapman | & Hall/CRC, |     | Boca | Raton. |     |     |     |
| ------- | ----------- | --- | ---- | ------ | --- | --- | --- |
Johari, R., Koomen, P., Pekelis, L. and Walsh, D. (2017), Peeking at A/B Tests: Why it matters, and what
| to do about | it, | ACM Press, | pp. | 1517–1525. |     |     |     |
| ----------- | --- | ---------- | --- | ---------- | --- | --- | --- |
Johari, R., Pekelis, L. and Walsh, D. J. (2015), ‘Always valid inference: Bringing sequential analysis to A/B
| testing’,  | arXiv      | preprint | arXiv:1512.04922 |               |     | .           |        |
| ---------- | ---------- | -------- | ---------------- | ------------- | --- | ----------- | ------ |
| Jorgensen, | B. (1997), | The      | Theory           | of Dispersion |     | Models, CRC | Press. |
Kaufmann, E., Capp´e, O. and Garivier, A. (2016), ‘On the complexity of best-arm identification in multi-
armed bandit models’, The Journal of Machine Learning Research 17(1), 1–42.
Kaufmann, E. and Koolen, W. (2018), ‘Mixture martingales revisited with applications to sequential tests
| and confidence |     | intervals’, | arXiv:1811.11419 |     |     | .   |     |
| -------------- | --- | ----------- | ---------------- | --- | --- | --- | --- |
Koltchinskii, V. and Lounici, K. (2017), ‘Concentration inequalities and moment bounds for sample covari-
| ance operators’, |     | Bernoulli | 23(1), | 110–133. |     |     |     |
| ---------------- | --- | --------- | ------ | -------- | --- | --- | --- |
Kulldorff, M., Davis, R.L.,Kolczak†,M.,Lewis, E., Lieu,T.andPlatt,R.(2011), ‘AMaximizedSequential
Probability Ratio Test for Drug and Vaccine Safety Surveillance’, Sequential Analysis 30(1), 58–78.
Lai, T. L. (1976a), ‘Boundary Crossing Probabilities for Sample Sums and Confidence Sequences’, The
| Annals | of Probability | 4(2), | 299–312. |     |     |     |     |
| ------ | -------------- | ----- | -------- | --- | --- | --- | --- |
Lai, T. L. (1976b), ‘On Confidence Sequences’, The Annals of Statistics 4(2), 265–280.
Lai, T. L. (1984), ‘Incorporating scientific, ethical and economic considerations into the design of clinical
trials in the pharmaceutical industry: a sequential approach’, Communications in Statistics - Theory and
| Methods | 13(19), | 2355–2368. |     |     |     |     |     |
| ------- | ------- | ---------- | --- | --- | --- | --- | --- |
Lai,T.L.(1997),‘Onoptimalstoppingproblemsinsequentialhypothesistesting’,StatisticaSinica7(1),33–
51.
Lai, T. L. and Siegmund, D. (1977), ‘A Nonlinear Renewal Theory with Applications to Sequential Analysis
| I’, The | Annals | of Statistics | 5(5), | 946–954. |     |     |     |
| ------- | ------ | ------------- | ----- | -------- | --- | --- | --- |
Lai, T. L. and Siegmund, D. (1979), ‘A Nonlinear Renewal Theory with Applications to Sequential Analysis
| II’, The | Annals | of Statistics | 7(1), | 60–76. |     |     |     |
| -------- | ------ | ------------- | ----- | ------ | --- | --- | --- |
Lan, K. K. G. and DeMets, D. L. (1983), ‘Discrete Sequential Boundaries for Clinical Trials’, Biometrika
| 70(3), 659–663. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Lorden,G.andPollak,M.(2005),‘Nonanticipatingestimationappliedtosequentialanalysisandchangepoint
| detection’, | The | Annals | of Statistics |     | 33(3), | 1422–1454. |     |
| ----------- | --- | ------ | ------------- | --- | ------ | ---------- | --- |
Malek,A.,Katariya,S.,Chow,Y.andGhavamzadeh,M.(2017),Sequentialmultiplehypothesistestingwith
| Type I | error control, | in  | ‘Artificial | Intelligence |     | and Statistics’, | pp. 1468–1476. |
| ------ | -------------- | --- | ----------- | ------------ | --- | ---------------- | -------------- |
Maurer, A. and Pontil, M. (2009), Empirical Bernstein bounds and sample variance penalization, in ‘Pro-
| ceedings | of the | Conference | on  | Learning | Theory’. |     |     |
| -------- | ------ | ---------- | --- | -------- | -------- | --- | --- |
McDiarmid, C. (1998), Concentration, in M. Habib, C. McDiarmid, J. Ramirez-Alfonsin and B. Reed, eds,
‘Probabilistic Methods for Algorithmic Discrete Mathematics’, Springer, New York, pp. 195–248.
Morters, P. and Peres, Y. (2010), Brownian Motion, Cambridge University Press, Cambridge.
Neyman, J. (1923/1990), ‘On the Application of Probability Theory to Agricultural Experiments, Essay on
| Principles, | Section | 9’, Statistical |     | Science | 5(4), | 465–480. |     |
| ----------- | ------- | --------------- | --- | ------- | ----- | -------- | --- |
O’Brien, P. C. and Fleming, T. R. (1979), ‘A Multiple Testing Procedure for Clinical Trials’, Biometrics
| 35(3), 549–556. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
23

Pinelis, I. (1992), An Approach to Inequalities for the Distributions of Infinite-Dimensional Martingales,
in ‘Probability in Banach Spaces, 8: Proceedings of the Eighth International Conference’, Birkh¨auser,
| Boston, | MA, pp. 128–134. |     |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- |
Pinelis, I. (1994), ‘Optimum Bounds for the Distributions of Martingales in Banach Spaces’, The Annals of
| Probability | 22(4), 1679–1706. |     |     |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- | --- | --- |
Pocock, S. J. (1977), ‘Group Sequential Methods in the Design and Analysis of Clinical Trials’, Biometrika
64(2), 191–199.
Raginsky,M.,Sason,I.etal.(2013),‘Concentrationofmeasureinequalitiesininformationtheory,communi-
cations,andcoding’,FoundationsandTrendsinCommunicationsandInformationTheory10(1-2),1–246.
Robbins, H. (1970), ‘Statistical Methods Related to the Law of the Iterated Logarithm’, The Annals of
| Mathematical | Statistics | 41(5), | 1397–1409. |     |     |     |     |
| ------------ | ---------- | ------ | ---------- | --- | --- | --- | --- |
Robbins, H. and Siegmund, D. (1968), Iterated logarithm inequalities and related statistical procedures, in
‘MathematicsoftheDecisionSciences,PartII’,AmericanMathematicalSociety,Providence,pp.267–279.
Robbins, H. and Siegmund, D. (1969), ‘Probability Distributions Related to the Law of the Iterated Loga-
| rithm’, | Proc. of the | National | Academy |     | of Sciences | 62(1), | 11–13. |
| ------- | ------------ | -------- | ------- | --- | ----------- | ------ | ------ |
Robbins, H. and Siegmund, D. (1970), ‘Boundary crossing probabilities for the Wiener process and sample
| sums’, The | Annals | of Mathematical |     | Statistics |     | 41(5), 1410–1429. |     |
| ---------- | ------ | --------------- | --- | ---------- | --- | ----------------- | --- |
Robbins, H. and Siegmund, D. (1972), A class of stopping rules for testing parametric hypotheses, The
| Regents | of the University |     | of California. |     |     |     |     |
| ------- | ----------------- | --- | -------------- | --- | --- | --- | --- |
Robbins,H.andSiegmund,D.(1974),‘TheExpectedSampleSizeofSomeTestsofPowerOne’,The Annals
| of Statistics | 2(3), 415–436. |     |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- | --- |
Rubin, D. B. (1974), ‘Estimating causal effects of treatments in randomized and nonrandomized studies.’,
| Journal | of educational | Psychology |     | 66(5), | 688. |     |     |
| ------- | -------------- | ---------- | --- | ------ | ---- | --- | --- |
Rudelson,M.(1999),‘RandomVectorsintheIsotropicPosition’,JournalofFunctionalAnalysis164(1),60–
72.
Shafer, G., Shen, A., Vereshchagin, N.andVovk, V.(2011), ‘TestMartingales, BayesFactorsandp-Values’,
| Statistical | Science | 26(1), | 84–101. |     |     |     |     |
| ----------- | ------- | ------ | ------- | --- | --- | --- | --- |
Siegmund, D. (1978), ‘Estimation Following Sequential Tests’, Biometrika 65(2), 341.
Siegmund, D. (1985), Sequential Analysis, Springer New York, New York, NY.
Siegmund, D. and Gregory, P. (1980), ‘A Sequential Clinical Trial for Testing p 1 = p 2 ’, The Annals of
| Statistics | 8(6), 1219–1228. |     |     |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- | --- | --- |
Stout, W. F. (1970), ‘The Hartman-Wintner Law of the Iterated Logarithm for Martingales’, Annals of
| Mathematical | Statistics | 41(6), | 2158–2160. |     |     |     |     |
| ------------ | ---------- | ------ | ---------- | --- | --- | --- | --- |
Tropp, J. A. (2011), ‘Freedman’s inequality for matrix martingales’, Electronic Communications in Proba-
| bility 16, | 262–270. |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- |
Tropp, J. A. (2012), ‘User-friendly tail bounds for sums of random matrices’, Foundations of Computational
| Mathematics | 12(4), | 389–434. |     |     |     |     |     |
| ----------- | ------ | -------- | --- | --- | --- | --- | --- |
Tropp, J. A. (2015), ‘An Introduction to Matrix Concentration Inequalities’, Foundations and Trends in
| Machine | Learning | 8(1-2), | 1–230. |     |     |     |     |
| ------- | -------- | ------- | ------ | --- | --- | --- | --- |
van de Geer, S. (1995), ‘Exponential Inequalities for Martingales, with Application to Maximum Likelihood
Estimation for Counting Processes’, The Annals of Statistics 23(5), 1779–1801.
Vershynin, R. (2012), Introduction to the non-asymptotic analysis of random matrices, in ‘Compressed
| Sensing: | Theory and | Applications’, |     | Cambridge |     | University | Press. |
| -------- | ---------- | -------------- | --- | --------- | --- | ---------- | ------ |
24

Ville, J. (1939), E´tude Critique de la Notion de Collectif., Gauthier-Villars, Paris.
Wald, A. (1945), ‘Sequential Tests of Statistical Hypotheses’, Annals of Mathematical Statistics 16(2), 117–
186.
| Wald, A. (1947), | Sequential | Analysis, | John | Wiley & Sons, | New York. |     |     |     |
| ---------------- | ---------- | --------- | ---- | ------------- | --------- | --- | --- | --- |
Whitehead, J. and Stratton, I. (1983), ‘Group Sequential Clinical Trials with Triangular Continuation Re-
| gions’, Biometrics |     | 39(1), 227–236. |     |     |     |     |     |     |
| ------------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
Widder, D. V. (1942), Laplace Transform, Princeton University Press, Princeton.
Yang, F., Ramdas, A., Jamieson, K. G. and Wainwright, M. J. (2017), A framework for Multi-
A(rmed)/B(andit)testingwithonlineFDRcontrol,in‘31stConferenceonNeuralInformationProcessing
Systems’.
Zhao, S., Zhou, E., Sabharwal, A. and Ermon, S. (2016), Adaptive concentration inequalities for sequential
decision problems, in ‘30th Conference on Neural Information Processing Systems’.
| A Proofs | of  | main | results |     |     |     |     |     |
| -------- | --- | ---- | ------- | --- | --- | --- | --- | --- |
In this section we give proofs of our main results along with selected discussion of and intuition for proof
techniques.
| A.1 Proof | of Theorem |     | 1   |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ηk <ηk+1
The idea behind Theorem 1 is to divide intrinsic time into geometrically spaced epochs, ≤V t for
some η > 1. We construct a linear boundary within each epoch using Lemma 1 and take a union bound
overcrossingeventsofthedifferentboundaries. Theresulting,piecewise-linearboundarymaythenbeupper
bounded by a smooth, concave function. Figure 3 illustrates the construction.
As discussed in Section 3.1, the function h determines the nominal crossing probability α/h(k) allocated to
the kth epoch, and we have mentioned the choices h(k)=ηsk/(1−η−s) and h(k)=(k+1)sζ(s). One may
substitute a series converging yet more slowly; for example, h(k)∝(k+2)logs(k+2) for s>1 yields
|     |          |     |               |              |            | (cid:18) log1−s(3/2) | (cid:19) |      |
| --- | -------- | --- | ------------- | ------------ | ---------- | -------------------- | -------- | ---- |
|     | logh(log | V   | )=loglog (η2V | )+slogloglog | (η2V )+log |                      | ,        | (35) |
|     |          | η   | t η           | t            | η t        | s−1                  |          |      |
matching related analysis in Darling and Robbins (1967b), Robbins and Siegmund (1969), Robbins (1970),
and Balsubramani (2014). In practice, the bound (35) appears to behave like bound (10) with worse con-
stants. However,thefactthatthestitchingapproachcanrecoverkeytheoreticalresultslikethesegivessome
| indication | of its power. |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Proof of Theorem 1. Weprovetheresultinthecasem=1forsimplicity. Thegeneralresultmaybeobtained
√ √
by considering S / m in place of S , V /m in place of V , and c/ m in place of c. See Appendix F for
|     | t   |     | t t |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
details.
We first compute ψ−1(u) by taking the positive solution to the quadratic equation given by ψ (λ) = u,
|     | G   |     |     |     |     |     | G   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
yielding
|     |     |     |             | (cid:112) | 2         |     |     |      |
| --- | --- | --- | ----------- | --------- | --------- | --- | --- | ---- |
|     |     |     | ψ−1(u)=−cu± | c2u2+2u=  |           | ,   |     | (36) |
|     |     |     | G           |           | (cid:112) |     |     |      |
|     |     |     |             |           | c+ c2+2/u |     |     |      |
√
| where we have | used the | identity | 1+x−1= | √ x | . Let |     |     |     |
| ------------- | -------- | -------- | ------ | --- | ----- | --- | --- | --- |
1+x+1
√ (cid:114)
|     |     |     |        | 2u     | c2u (cid:114) u |     |     |      |
| --- | --- | --- | ------ | ------ | --------------- | --- | --- | ---- |
|     |     |     | K(u):= | =      | 1+ +c .         |     |     | (37) |
|     |     |     |        | ψ−1(u) | 2 2             |     |     |      |
G
25

K(u) will appear below. Now we start from the line-crossing inequality of Lemma 1: reparametrizing
| r =logα−1, | we  | have | for any | r >0,λ>0 |          |     |           |                    |           |      |     |     |      |
| ---------- | --- | ---- | ------- | -------- | -------- | --- | --------- | ------------------ | --------- | ---- | --- | --- | ---- |
|            |     |      |         |          | (cid:32) |     |           |                    | (cid:33)  |      |     |     |      |
|            |     |      |         |          |          |     | r+ψ       | G (λ)V             | t         |      |     |     |      |
|            |     |      |         | P        | ∃t≥1:S   |     | ≥         |                    | ≤l        | e−r. |     |     | (38) |
|            |     |      |         |          |          | t   |           | λ                  |           | 0    |     |     |      |
|            |     |      |         |          |          |     | (cid:124) | (cid:123)(cid:122) | (cid:125) |      |     |     |      |
gλ,r(Vt)
|     |     |     |     |     | ηk  |     | ηk+1 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
We divide intrinsic time into epochs ≤ V t < for each k = 0,1,..., and we will construct a linear
boundary over each epoch by carefully choosing values for λ and r and using the probability bound (38).
|     |     |     |     |     |     |     |     |     | k   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We choose λ so that the “standardized” boundary takes equal values at both endpoints of the epoch:
k
ψ−1(r
g (ηk)/ηk/2 = g (ηk+1)/η(k+1)/2. This equation is solved by λ = /ηk+1/2), which yields,
| λk,rk |               | λk,rk |     |       |     |          |                           |        |           | k                 | G   | k   |      |
| ----- | ------------- | ----- | --- | ----- | --- | -------- | ------------------------- | ------ | --------- | ----------------- | --- | --- | ---- |
| after | some algebra, |       |     |       |     |          |                           |        |           |                   |     |     |      |
|       |               |       |     |       |     | (cid:18) | (cid:19)(cid:34)(cid:114) |        | (cid:114) | (cid:35)(cid:114) |     |     |      |
|       |               |       |     |       |     | r        |                           | ηk+1/2 |           | v                 | r v |     |      |
|       |               |       | g   | (v)=K |     | k        |                           |        | +         |                   | k   |     | (39) |
λk,rk
|     |     |     |     |     |     | ηk+1/2 |     | v   |     | ηk+1/2 | 2   |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------ | --- | --- | --- |
Ourgoal, afterchoosingr below, istoupperboundthisexpressionbyafunctionofv alone, independentof
k
Notingthattheterminsquarebracketsin(39)reachesitsmaximumoverthekth
| k.    |              |      |                   |         |     |             |          |             |       |         |         | epochattheendpoints, |      |
| ----- | ------------ | ---- | ----------------- | ------- | --- | ----------- | -------- | ----------- | ----- | ------- | ------- | -------------------- | ---- |
| v =ηk | and v =ηk+1, |      | and substituting  |         | the | expression  |          | (37) for    | K(u), | we have |         |                      |      |
|       |              |      | (cid:32)(cid:115) |         |     |             | (cid:33) |             |       |         |         |                      |      |
|       |              |      |                   | c2r     |     | (cid:114) r |          | η1/4+η−1/4√ |       |         |         |                      |      |
|       |              |      |                   |         | k   |             | k        |             |       |         |         | ηk <ηk+1.            |      |
|       | g λk,rk      | (v)≤ | 1+                |         | +c  |             |          | √           |       | r k v,  | for all | ≤v                   | (40) |
|       |              |      |                   | 2ηk+1/2 |     | 2ηk+1/2     |          |             | 2     |         |         |                      |      |
√
| The inequality | ηk+1/2 |     | ≥v/   | η yields |            |     |                   |     |       |       |          |     |      |
| -------------- | ------ | --- | ----- | -------- | ---------- | --- | ----------------- | --- | ----- | ----- | -------- | --- | ---- |
|                |        |     |       |          |            |     | (cid:32)(cid:114) | √   |       |       | (cid:33) |     |      |
|                |        |     |       |          | η1/4+η−1/4 |     |                   |     | ηc2r2 | η1/4r |          |     |      |
|                |        |     | g     | (v)≤     | √          |     | r                 | v+  | k +c  | √     | k        |     | (41) |
|                |        |     | λk,rk |          |            |     | k                 |     |       |       |          |     |      |
|                |        |     |       |          |            | 2   |                   |     | 2     | 2     |          |     |      |
(cid:113)
|     |     |     |     | =   | k2r | v+k2c2r2+ck |     | r , | for all | ηk ≤v | <ηk+1, |     | (42) |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------- | ----- | ------ | --- | ---- |
|     |     |     |     |     | 1   | k 2         | k   | 2 k |         |       |        |     |      |
using the definition (8) of k and k . Now let r = log(l h(k)/α), which we choose to ensure total error
|     |     |     |     | 1   | 2   |     | k   | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
probability will be bounded by α via a union bound. Note that h is nondecreasing and k ≤log V over the
η t
epoch, so that r ≤(cid:96)(v) over the epoch, recalling the definition (8) of (cid:96)(v). We conclude
k
(cid:113)
g (v)≤ k2v(cid:96)(v)+k2c2(cid:96)2(v)+ck (cid:96)(v)=S (v), (43)
|     |     |     |     | λk,rk |     | 1   | 2   |     | 2   |     | α   |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for all ηk ≤v <ηk+1. This final expression no longer depends on k, showing that the final boundary S (v)
α
majorizes the corresponding linear boundary g (v) over each epoch ηk ≤ v < ηk+1 for k = 0,1,....
λk,rk
Hence
|     |     |     |     |     | S (v)≥ming |     |       | (v) for | all v | ≥1. |     |     | (44) |
| --- | --- | --- | --- | --- | ---------- | --- | ----- | ------- | ----- | --- | --- | --- | ---- |
|     |     |     |     |     | α          |     | λk,rk |         |       |     |     |     |      |
k≥0
But the first linear boundary g λ0,t0 (v) passes through S α (1) and has positive slope, which implies
|     |     |     |     | S   | (1∨v)≥ming |     |       | (v) | for all | v >0. |     |     | (45) |
| --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | ------- | ----- | --- | --- | ---- |
|     |     |     |     |     | α          |     | λk,rk |     |         |       |     |     |      |
k≥0
Now taking a union bound over the probability bounds given by (38) for k =0,1,..., we have
|     |     |     | (cid:18) |     |     |       | (cid:19) | ∞        |      | ∞        |      |     |      |
| --- | --- | --- | -------- | --- | --- | ----- | -------- | -------- | ---- | -------- | ---- | --- | ---- |
|     |     |     |          |     |     |       |          | (cid:88) |      | (cid:88) | 1    |     |      |
|     |     |     | P ∃t≥1:S |     | ≥m  | in g  | (V )     | ≤l       | e−rk | =α       |      | ≤α. | (46) |
|     |     |     |          |     | t   | λk,rk | t        | 0        |      |          |      |     |      |
|     |     |     |          |     | k≥  | 0     |          |          |      |          | h(k) |     |      |
|     |     |     |          |     |     |       |          | k=0      |      | k=0      |      |     |      |
Combining (46) with (45) proves that v (cid:55)→ S (1 ∨ v) is a sub-gamma uniform boundary with crossing
α
| probability | α.  |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For the second statement (9), we simply restrict the union bound to epochs k ≥ (cid:98)log V t (cid:99), which restricts
η
| the sum | in (46) | accordingly. |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
26

We have given a stitched bound which is constant for v < m, but inspection of the proof shows that one
may improve the bound to be linear with positive slope on v < m, by extending the linear bound over the
first epoch to cover all v > 0. This seems of limited utility for theoretical work, and we recommend other
bounds over the stitched bound for practice, so we do not pursue this point further.
The idea of taking a union bound over geometrically spaced epochs is standard in the proof of the classical
law of the iterated logarithm (Durrett, 2017, Theorem 8.5.1). The idea has been extended to finite-time
bounds by Darling and Robbins (1967b), Jamieson et al. (2014), Kaufmann et al. (2016), and Zhao et al.
(2016), usually when the observations are independent and sub-Gaussian; the technique is sometimes called
“peeling”. Ofcourse,Theorem1generalizestheseconstructionsmuchbeyondtheindependentsub-Gaussian
case, but it also achieves tighter constants for the sub-Gaussian setting. Here, we briefly discuss how the
| improved | constants | arise. |     |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Both Jamieson et al. (2014) and Zhao et al. (2016) construct a constant boundary rather than a linear
increasing boundary over each epoch. They apply Doob’s maximal inequality for submartingales (Durrett,
2017, Theorem 4.4.2), as in Hoeffding (1963, eq. 2.17), to obtain boundaries similar to that of Freedman
(1975). As illustrated in Howard et al. (2020, Figure 2), the linear bounds from Lemma 1 are stronger than
corresponding Freedman-style bounds, and the additional flexibility yields tighter constants.
Both Darling and Robbins (1967b) and Kaufmann et al. (2016) use linear boundaries within each epoch
analogous to those of Lemma 1. Both methods share a great deal in common with ours, and Darling and
Robbinsgiveconsiderationtogeneralcumulant-generatingfunctions. RecallfromLemma1thatsuchlinear
boundariesmaybechosentooptimizeforsomefixedtimeV =m. Ourmethodchoosesthelinearboundary
t
ηk+1/2,
within each epoch to be optimal at the geometric center of the epoch, i.e., at V t√ = so that at both
epoch endpoints the boundary will be equally “loose”, that is, equal multiples of V . Darling and Robbins
t
choose the boundaries to be tangent at the start of the epoch, hence their boundary is looser than ours at
the end of the epoch. Kaufmann et al. choose the boundary as we do, but appear to incur more looseness
| in the subsequent |     | inequalities |     | used | to construct | a smooth |     | upper | bound. |     |     |     |
| ----------------- | --- | ------------ | --- | ---- | ------------ | -------- | --- | ----- | ------ | --- | --- | --- |
| A.2 Proof         | of  | Corollary    |     | 1    |              |          |     |       |        |     |     |     |
ψ(λ)≤(1+(cid:15))λ2/2
Fix any (cid:15)>0 and choose a>0 small enough that for all λ∈(0,a). Using the fact that
ψ (λ)≥λ2/2 for c≥0, we have ψ(λ)≤(1+(cid:15))ψ (λ) for all λ∈(0,a), so that (S ) is sub-gamma with
| G,c         |     |          |          |                |     | G,1/a              |         |              |       |           | t   |      |
| ----------- | --- | -------- | -------- | -------------- | --- | ------------------ | ------- | ------------ | ----- | --------- | --- | ---- |
| scale c=1/a | and | variance | process  | ((1+(cid:15))V |     | t ). Now           | Theorem | 1            | shows | that      |     |      |
|             |     |          | (cid:18) |                |     |                    |         |              |       | (cid:19)  |     |      |
|             |     |          | P supV   | =∞             | and | S ≥u((1+(cid:15))V |         | ) infinitely |       | often =0, |     | (47) |
|             |     |          |          | t              |     | t                  |         | t            |       |           |     |      |
t
(cid:112)
where we may choose u(v)∼ 2(1+(cid:15))vloglogv (see (10) and discussion thereafter), so that u((1+(cid:15))v)∼
(cid:112)
| 2(1+(cid:15))2vloglogv. |     | It  | follows | that |     |     |     |     |          |          |     |     |
| ----------------------- | --- | --- | ------- | ---- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|                         |     |     |         |      |     |     |     |     | (cid:26) | (cid:27) |     |     |
S t
|               |                |     | limsup  |           |                 |           | ≤1  | on  | supV | =∞ . |     | (48) |
| ------------- | -------------- | --- | ------- | --------- | --------------- | --------- | --- | --- | ---- | ---- | --- | ---- |
|               |                |     |         | (cid:112) | 2(1+(cid:15))2V |           |     |     |      | t    |     |      |
|               |                |     | t→∞     |           |                 | t loglogV | t   |     | t    |      |     |      |
| As (cid:15)>0 | was arbitrary, |     | we are  | done.     |                 |           |     |     |      |      |     |      |
| A.3 Conjugate |                |     | mixture | proofs    |                 |           |     |     |      |      |     |      |
Proof of Lemma 2. Assume (S ) is sub-ψ with variance process (V ), so that, for each λ ∈ [0,λ ), we
|     |     |     |     | t   |     |     |     |     | t   |     |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have exp{λS −ψ(λ)V } ≤ L (λ) where (L (λ))∞ is a nonnegative supermartingale. We will show that
|     | t   |     | t   | t   |     | t t=0 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
(cid:82)
| M := L | (λ)dF(λ) | is  | a supermartingale |     |     | with respect | to  | (F ). |     |     |     |     |
| ------ | -------- | --- | ----------------- | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
| t      | t        |     |                   |     |     |              |     | t     |     |     |     |     |
Formally, for this proof, we augment the underlying probability space with the random variable λ having
R,
distribution F over the Borel σ-field on independent of everything else. For each t, we require L to be
t
a random variable on this product space, i.e., it must be product measurable. Now Definition 1 stipulates
|     |     |     | E(L |     |     |     |     |     |     | E(L |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that L t ∈σ(λ,F t ) and t | λ,F t−1 )≤L t−1 for each t≥1, and additionally, 0 | λ)≤l 0 a.s. In other
words, (L ) is a supermartingale with respect to the filtration given by G := σ(λ,F ) on this augmented
|     | t   |     |     |     |     |     |     |     |     | t   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
space. Finally, we have M = E(L | F ). These facts follow directly from the definition and properties of
|             |              |     | t   |     | t t |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| conditional | expectation. |     |     |     |     |     |     |     |     |     |     |     |
27

We claim that (M ) is a supermartingale with respect to (F ) on this augmented space. Indeed,
|     |     | t     |         |     |        |         |     | t     |     |      |       |         |      |
| --- | --- | ----- | ------- | --- | ------ | ------- | --- | ----- | --- | ---- | ----- | ------- | ---- |
|     | E(M | | F   | )=E(E(L | |   | F )| F | )=E(E(L |     | | λ,F |     | )| F | )≤E(L | | F )   | (49) |
|     |     | t t−1 |         | t   | t      | t−1     |     | t     | t−1 | t−1  |       | t−1 t−1 |      |
bythesupermartingaleproperty,andthislastexpressionisequaltoM . Furthermore,EM =EE(L | λ)≤
|           |     |        |               |     |      |      |       |        | t−1 |     |     | 0   | 0   |
| --------- | --- | ------ | ------------- | --- | ---- | ---- | ----- | ------ | --- | --- | --- | --- | --- |
|           | E(L |        |               | E|M | |=EM |      |       |        |     |     |     |     |     |
| l 0 since | 0   | | λ)≤l | 0 a.s., hence |     | t    | t ≤l | 0 for | all t. |     |     |     |     |     |
Now Definition 1 and Ville’s maximal inequality for nonnegative supermartingales (Durrett, 2017, exercise
4.8.2) yield
|     |     | (cid:18) | (cid:90) |          |        |           |     | l (cid:19) | (cid:18) |     |     | l (cid:19) |      |
| --- | --- | -------- | -------- | -------- | ------ | --------- | --- | ---------- | -------- | --- | --- | ---------- | ---- |
|     |     | P        |          |          |        |           |     | 0          | ≤P       |     |     | 0          |      |
|     |     | ∃t≥1:    |          | exp{λS t | −ψ(λ)V | t }dF(λ)≥ |     |            | ∃t≥1:M   |     | t ≥ | ≤α.        | (50) |
|     |     |          |          |          |        |           |     | α          |          |     |     | α          |      |
P(∃t≥1:S
In other words, t ≥M α (V t ))≤α by the definition of M α , which is the desired conclusion.
In the sub-Gaussian case, the following boundary is well-known (Robbins, 1970, example 2).
Proposition 5 (Two-sided normal mixture). Suppose both (S ) and (−S ) are sub-Gaussian with variance
|         |             |         |     |      |            |     |     | t   |     | t   |     |     |     |
| ------- | ----------- | ------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| process | (V t ). Fix | α∈(0,1) | and | ρ>0, | and define |     |     |     |     |     |     |     |     |
(cid:115)
|     |     |     |     |        |     |          |     | (cid:18) l2(v+ρ) | (cid:19) |     |     |     |      |
| --- | --- | --- | --- | ------ | --- | -------- | --- | ---------------- | -------- | --- | --- | --- | ---- |
|     |     |     |     | u(v):= |     |          |     | 0                |          |     |     |     |      |
|     |     |     |     |        |     | (v+ρ)log |     |                  |          | .   |     |     | (51) |
α2ρ
| Then P(∀t≥1:|S |     | |<u(V | ))≥1−α. |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     | t     | t       |     |     |     |     |     |     |     |     |     |     |
√
We have included the bound in Figures 4 and 9; although its O( V t logV t ) rate of growth is worse than
the finite LIL discrete mixture bound, it can achieve tighter control over about three orders of magnitude of
intrinsic time. This makes the normal mixture preferable in many practical situations when a sub-Gaussian
assumption applies. When only a one-sided sub-Gaussian assumption holds, the normal mixture still yields
| a sub-Gaussian |     | uniform | boundary. |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition 6 (One-sided normal mixture). For any α∈(0,1) and ρ>0, the boundary
|     |     |     |         | (cid:26) | (cid:114) |     | (cid:26) |        | (cid:27) | (cid:18) | (cid:19) | (cid:27) |      |
| --- | --- | --- | ------- | -------- | --------- | --- | -------- | ------ | -------- | -------- | -------- | -------- | ---- |
|     |     |     |         |          |           | 4ρ  |          | s2     |          | s        |          | l        |      |
|     |     | NM  | (v)=sup | s∈R:     |           |     | exp      |        | Φ        | √        |          | < 0 .    | (52) |
|     |     |     | α       |          |           | v+ρ |          | 2(v+ρ) |          | v+ρ      |          | α        |      |
is a sub-Gaussian uniform boundary with crossing probability α. Furthermore, we have the following closed-
| form upper | bound: |     |     |     |     |           |     |          |           |     |          |     |     |
| ---------- | ------ | --- | --- | --- | --- | --------- | --- | -------- | --------- | --- | -------- | --- | --- |
|            |        |     |     |     |     | (cid:115) |     | (cid:18) | (cid:114) |     | (cid:19) |     |     |
l v+ρ
|     |     |     | NM  | (v)≤N(cid:103)M | (v):= |     | 2(v+ρ)log |     | 0   |     | +1  | .   | (53) |
| --- | --- | --- | --- | --------------- | ----- | --- | --------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | α               | α     |     |           |     |     |     |     |     |      |
|     |     |     |     |                 |       |     |           |     | 2 α | ρ   |     |     |      |
The boundary NM is easily evaluated to high precision by numerical root-finding, and the closed-form
α
approximation is excellent: numerical calculations indicate that N(cid:103)M (v)/NM (v) < 1.007 uniformly
|           |     |          |     |     |     |     |     |     | 0.025 |     |     | 0.025 |     |
| --------- | --- | -------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
| when ρ=1, | for | example. |     |     |     |     |     |     |       |     |     |       |     |
Proof of Proposition 6. To obtain the explicit upper bound N(cid:103)M in (53) from the exact boundary (52), we
α
usetheinequality1−Φ(x)≤e−x2/2 forx>0, whichfollowsfromastandardCram´er-Chernoffbound. This
implies
|        | (cid:114) | 4ρ    | (cid:26) s2 | (cid:27)  | (cid:18) s  | (cid:19) | (cid:114) 4ρ | (cid:20) | (cid:26) | s2  | (cid:27) | (cid:21)   |      |
| ------ | --------- | ----- | ----------- | --------- | ----------- | -------- | ------------ | -------- | -------- | --- | -------- | ---------- | ---- |
|        |           | exp   |             | Φ         | √           | ≥        |              | exp      |          |     | −1       | , for s>0. | (54) |
|        | v+ρ       |       | 2(v+ρ)      |           | v+ρ         |          | v+ρ          |          | 2(v+ρ)   |     |          |            |      |
| We set | the RHS   | equal | to l /α     | and solve | to conclude |          |              |          |          |     |          |            |      |
0
(cid:115)
|     |     |     |     |     |     |     | (cid:18) l (cid:114) | v+ρ | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | -------- | --- | --- | --- | --- |
0
|     |     |     | NM  | (v)≤ | 2(v+ρ)log |     |     |     | +1  | =N(cid:103)M | (v), |     | (55) |
| --- | --- | --- | --- | ---- | --------- | --- | --- | --- | --- | ------------ | ---- | --- | ---- |
|     |     |     |     | α    |           |     | 2 α | ρ   |     |              | α    |     |      |
so long as NM (v)>0. But we are guaranteed that NM (v)>0, because the LHS of the inequality in (52)
|     |     | α   |     |     |     |     |     | α   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is increasing in s on s≥0 and no larger than one when s=0, while the RHS l 0 /α≥1.
The fact that NM is a sub-Gaussian uniform boundary follows directly from Lemma 2, and therefore N(cid:103)M
|     |     | α   |     |     |     |     |     |     |     |     |     |     | α   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is as well.
28

Whenasub-Bernoulliconditionholds,aswithboundedobservations,thefollowingbeta-binomialboundaryis
tighterthanthenormalmixture. Simplerversionsofthisboundaryhavelongbeenstudiedfori.i.d.Bernoulli
sampling(Ville,1939;Robbins,1970;Lai,1976b;Shaferetal.,2011). Below,B (a,b)= (cid:82)x pa−1(1−p)b−1dp
x 0
denotestheincompleteBetafunction, whoseimplementationisavailableinstatisticalsoftwarepackages; B
1
is the ordinary Beta function.
Proposition 7 (Two-sidedbeta-binomialmixture). Suppose(S )issub-Bernoulliwithvarianceprocess(V )
t t
andrangeparametersg,h, while(−S )issub-Bernoulliwithvarianceprocess(V )andrangeparametersh,g.
t t
Fix any ρ>gh, let r =ρ−gh, and define
(cid:26) (cid:20) (cid:19) (cid:27)
r+v l
f (v) := sup s∈ 0, :m (s,v)< 0 , (56)
g,h g g,h α
(cid:16) (cid:17)
(g+h)v/gh B 1 r g + (g v + − h g ) s,r h + (g v + + h h ) s
where m (s,v) := · . (57)
g,h (cid:2) gv/h+shv/g−s (cid:3)1/(g+h) B (cid:16) r , r (cid:17)
1 g(g+h) h(g+h)
Then P(∀t≥1:−f (V )<S <f (V ))≥1−α.
g,h t t h,g t
As with the normal mixture, we have a one-sided variant as well.
Proposition 8 (One-sidedbeta-binomialmixture). Fix any g,h>0, α∈(0,1), and ρ>gh. Let r =ρ−gh
and define
(cid:26) (cid:20) (cid:19) (cid:27)
r+v l
f (v) := sup s∈ 0, :m (s,v)< 0 , (58)
g,h g g,h α
(cid:16) (cid:17)
(g+h)v/gh B h/(g+h) r g + (g v + − h g ) s,r h + (g v + + h h ) s
where m (s,v) := · . (59)
g,h (cid:2) gv/h+shv/g−s (cid:3)1/(g+h) B (cid:16) r , r (cid:17)
h/(g+h) g(g+h) h(g+h)
Then f is a sub-Bernoulli uniform boundary with crossing probability α and range parameters g,h.
g,h
In the sub-Bernoulli case, we first rewrite the exponential process exp{λS −ψ (λ)V } in terms of the
t B t
transformed parameter p = [1 + (h/g)e−λ]−1. This is motivated by the transform from the canonical
parameter to the mean parameter of a Bernoulli family, but keep in mind that we make no parametric
assumption here, these are merely analytical manipulations. Then a truncated Beta distribution on p ∈
[g/(g+h),1] yields the one-sided beta-binomial uniform boundary, while an untruncated mixture yields the
two-sided boundary.
Proof of Propositions 7 and 8. For simplicity of notation, we will assume here that the problem has been
scaled so that g + h = 1, e.g., by replacing X with X /(g + h). Using the sub-Bernoulli ψ function
t t
ψ (λ)= 1 log (cid:0) gehλ+he−gλ(cid:1) , the exponential integrand in our mixture is
B gh
exp
(cid:26)
λs−
v
log
(cid:0) gehλ+he−gλ(cid:1) (cid:27)
=
pv/h+s(1−p)v/g−s
, (60)
gh gv/h+shv/g−s
after substituting the one-to-one transformation
gehλ (cid:18) ph (cid:19)
p=p(λ):= , so that λ=log , (61)
gehλ+he−gλ (1−p)g
followed by some algebra. We wish to integrate against a Beta mixture density on p with parameters r/h
and r/g, which has mean p=g, corresponding to λ=0. For Proposition 8, we must also truncate to λ≥0,
i.e., to p≥g. The appropriately normalized mixture integral is then
(cid:16) (cid:17)
1 ·
(cid:82)
g
1 pv/h+s+r/h−1(1−p)v/g−s+r/g−1dp
= 1 ·
B
h
r+
g
v −s,r+
h
v +s
, (62)
gv/h+shv/g−s (cid:82)1 pr/h−1(1−p)r/g−1dp gv/h+shv/g−s B (cid:16) r, r (cid:17)
g h g h
29

using the fact that B (a,b) = (cid:82)x pa−1(1−p)b−1dp = (cid:82)1 pb−1(1−p)a−1dp. This gives the closed-form
x
|     |     |     |     | 0   |     |     |     | 1−x |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mixture (59). (To obtain the formula for general g +h (cid:54)= 1, substitute g/(g +h) for g, h/(g +h) or h,
| s/(g+h) | for s, v/(g+h)2 |     | for | v, and | r/(g+h)2 | for | r.) |     |     |     |     |     |     |
| ------- | --------------- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
The proof of Proposition 7 is nearly identical, but we integrate over the full Beta mixture rather than
truncating.
To verify that our choice of r ensures that λ has approximate precision ρ under the full (not truncated)
mixture distribution, we use the delta method to calculate the approximate variance of λ for large r based
| on the variance | of  | p under | the | full Beta | mixture:         |     |           |      |      |     |     |     |      |
| --------------- | --- | ------- | --- | --------- | ---------------- | --- | --------- | ---- | ---- | --- | --- | --- | ---- |
|                 |     |         |     |           | (cid:34)(cid:18) |     | (cid:35)  |      |      |     |     |     |      |
|                 |     |         |     |           |                  | 1   | (cid:19)2 | gh   |      | 1   |     |     |      |
|                 |     |         |     | Varλ≈     |                  |     |           | ·    | =    | .   |     |     | (63) |
|                 |     |         |     |           | p(1−p)           |     |           | r +1 | r+gh |     |     |     |      |
gh
p=g
| Setting | this equal | to 1/ρ | yields | r =ρ−gh | as  | desired. |     |     |     |     |     |     |     |
| ------- | ---------- | ------ | ------ | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
When tails are heavier than Gaussian, the normal mixture boundary is not applicable. However, the fol-
lowing sub-exponential mixture boundary, based on a gamma mixing density, is universally applicable,
as described in Proposition 1. Like the normal mixture, the gamma-exponential mixture is unimprov-
able as described in Section 3.6. Below we make use of the regularized lower incomplete gamma function
(cid:82)x
γ(a,x):=( ua−1e−udu)/Γ(a), available in standard statistical software packages.
0
| Proposition | 9   | (Gamma-exponential |          |     | mixture).       | Fix | c>0,ρ>0 |            | and define |     |     |     |      |
| ----------- | --- | ------------------ | -------- | --- | --------------- | --- | ------- | ---------- | ---------- | --- | --- | --- | ---- |
|             |     |                    |          |     | (cid:26)        |     |         | l (cid:27) |            |     |     |     |      |
|             |     |                    |          | :=  |                 |     |         | 0          |            |     |     |     |      |
|             |     |                    | GE α (v) |     | sup s≥0:m(s,v)< |     |         | ,          |            |     |     |     | (64) |
α
ρ
|     |       |     |        |     | (cid:0)ρ(cid:1)       | 2           | (cid:0)v+ρ(cid:1) | (cid:0)v+ρ,cs+v+ρ(cid:1) |       |     | (cid:26) | (cid:27) |      |
| --- | ----- | --- | ------ | --- | --------------------- | ----------- | ----------------- | ------------------------ | ----- | --- | -------- | -------- | ---- |
|     |       |     |        |     |                       | c           | Γ                 | γ                        |       |     | cs+v     |          |      |
|     | where |     | m(s,v) | :=  | c2                    |             |                   | c2                       | c2 c2 | exp |          | .        | (65) |
|     |       |     |        |     | Γ (cid:0) ρ (cid:1) γ | (cid:0) ρ , | ρ (cid:1)         | (cid:0)cs+v+ρ(cid:1)v    | + ρ   |     | c2       |          |      |
2
|     |     |     |     |     | c 2 | c 2 c | 2   | c2  | c   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Then GE α is a sub-exponential uniform boundary with crossing probability α for scale c.
The gamma-exponential mixture is the result of evaluating the mixture integral in (13) with mixing density
|     |     |     | dF  |     | 1   | (ρ/c)ρ/c2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
(c−1−λ)ρ/c2−1e−ρ(c−1−λ)/c.
|     |     |     |     | =            |     |         |     |     |     |     |     |     | (66) |
| --- | --- | --- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     | dλ  | γ(ρ/c2,ρ/c2) |     | Γ(ρ/c2) |     |     |     |     |     |     |      |
Thisisagammadistributionwithshapeρ/c2andscaleρ/cappliedtothetransformedparameteru=c−1−λ,
truncated to the support [0,c−1]. The distribution has mean zero and variance equal to 1/ρ, making it
comparable to the normal mixture distribution used above. As ρ → ∞, the gamma mixture distribution
convergestoanormaldistributionandconcentratesaboutλ=0,theregimeinwhichψ E (λ)∼ψ N (λ),which
gives some intuition for why the gamma-exponential mixture recovers the normal mixture when ρ(cid:29)c2.
| Proof of | Proposition | 9.  | We need | only     | show     | that |              |     |     |     |     |     |      |
| -------- | ----------- | --- | ------- | -------- | -------- | ---- | ------------ | --- | --- | --- | --- | --- | ---- |
|          |             |     |         | (cid:90) | 1/c      |      |              |     |     |     |     |     |      |
|          |             |     | m(s,v)= |          | exp{λs−ψ |      | (λ)v}f(λ)dλ, |     |     |     |     |     | (67) |
E
0
(ρ/c)ρ/c2
|     |     |       |       |              | 1   |     |         | (c−1−λ)ρ/c2−1e−ρ(c−1−λ)/c. |     |     |     |     |      |
| --- | --- | ----- | ----- | ------------ | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | ---- |
|     |     | where | f(λ)= |              |     |     |         |                            |     |     |     |     | (68) |
|     |     |       |       | γ(ρ/c2,ρ/c2) |     |     | Γ(ρ/c2) |                            |     |     |     |     |      |
Then the fact that GM is a sub-exponential uniform boundary follows as a special case of Lemma 2.
α
Proving (67) is an exercise in calculus. Substituting the definition of ψ and removing common terms, it
E
| suffices | to show that        |                            |     |     |     |              |     |     |     |     |     |     |     |
| -------- | ------------------- | -------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|          | Γ (cid:0)v+ρ(cid:1) | γ (cid:0)v+ρ,cs+v+ρ(cid:1) |     |     |     | (cid:90) 1/c |     |     |     |     |     |     |     |
c−ρ/c2 c2 c2 c2 e(cs+v)/c2 (1−cλ)v/c2 eλ(s+v/c)(c−1−λ)ρ/c2−1e−ρ(c−1−λ)/cdλ.
|     |                       |     |     |     | =   |     |     |     |     |     |     |     | (69) |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | (cid:0)cs+v+ρ(cid:1)v |     | + ρ |     |     |     |     |     |     |     |     |     |      |
|     |                       |     | c 2 |     |     | 0   |     |     |     |     |     |     |      |
c2
30

After change of variables u= (cid:0)cs+v+ρ(cid:1) (c−1−λ), the right-hand side is equal to
c
|     |     | (cid:18) |        | (cid:19)−v | + ρ       |            |     | (cid:90) (cs+v+ρ)/c2 |                   |     |     |     |     |
| --- | --- | -------- | ------ | ---------- | --------- | ---------- | --- | -------------------- | ----------------- | --- | --- | --- | --- |
|     |     |          | cs+v+ρ |            | c 2 cv/c2 | e(cs+v)/c2 |     |                      | u(v+ρ)/c2−1e−udu. |     |     |     |     |
(70)
c
0
Now the definition of the regularized lower incomplete gamma function and a bit of algebra finishes the
argument.
A similar mixture boundary holds in the sub-Poisson case, making use of the regularized upper incomplete
| gamma function |     | γ¯(a,x):=( | (cid:82)∞ | ua−1e−udu)/Γ(a). |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x
| Proposition | 10  | (Gamma-Poisson |     |     | mixture). | Fix      | c>0,ρ>0 | and      | define |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --------- | -------- | ------- | -------- | ------ | --- | --- | --- | --- |
|             |     |                |     |     |           | (cid:26) |         | (cid:27) |        |     |     |     |     |
l 0
|     |     |     | GP  | (v) := | sup | s≥0:m(s,v)<         |     |                      | ,                        |     |            |           | (71) |
| --- | --- | --- | --- | ------ | --- | ------------------- | --- | -------------------- | ------------------------ | --- | ---------- | --------- | ---- |
|     |     |     | α   |        |     |                     |     | α                    |                          |     |            |           |      |
|     |     |     |     |        |     | (cid:0)ρ(cid:1)ρ/c2 |     | (cid:0)cs+v+ρ(cid:1) | (cid:0)cs+v+ρ,v+ρ(cid:1) |     |            |           |      |
|     |     |     |     |        |     |                     | Γ   |                      | γ¯                       |     | (cid:110)v | (cid:111) |      |
|     |     |     |     |        |     | c2                  |     | c2                   | c2                       | c2  |            |           |      |
where m(s,v) := (cid:0)ρ(cid:1) (cid:0)ρ, ρ(cid:1) exp . (72)
|     |     |     |     |     | Γ   | γ¯  |     | (cid:0)v+ρ(cid:1)(cs+v+ρ)/c2 |     |     | c2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | c2  | c2  | c2  |                              |     |     |     |     |     |
c2
Then GP is a sub-Poisson uniform boundary with crossing probability α for scale c.
α
Proof of Proposition 10. TheprooffollowsthesamecontoursasthatofProposition8. Usingthesub-Poisson
(λ)=c−2(ecλ−cλ−1),
| ψ function | ψ P |     |     |          | the      | exponential |                  | integrand | in our | mixture | is  |     |     |
| ---------- | --- | --- | --- | -------- | -------- | ----------- | ---------------- | --------- | ------ | ------- | --- | --- | --- |
|            |     |     |     | (cid:26) | (cid:18) |             | (cid:19)(cid:27) |           |        |         |     |     |     |
ecλ−cλ−1
|     |     |     | exp | λs−v |     |     |     | =θ(cs+v)/c2 | e(1−θ)v/c2 | ,   |     |     | (73) |
| --- | --- | --- | --- | ---- | --- | --- | --- | ----------- | ---------- | --- | --- | --- | ---- |
c2
after substituting the one-to-one transformation θ =θ(λ):=ecλ, so that λ=c−1logθ. We integrate against
a gamma mixing distribution on θ with shape and scale parameters both equal to β := ρ/c2, truncated to
| θ ≥1, so | that λ≥0: |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:82)∞ θ(cs+v+ρ)/c2−1e−(v+ρ)θ/c2dθ (cid:0)ρ(cid:1)ρ/c2 (cid:0)cs+v+ρ(cid:1) (cid:0)cs+v+ρ,v+ρ(cid:1)
|       |           |                  |     |     |     |                 |     | Γ                            |     | γ¯        |          | (cid:110)v | (cid:111) |
| ----- | --------- | ---------------- | --- | --- | --- | --------------- | --- | ---------------------------- | --- | --------- | -------- | ---------- | --------- |
| ev/c2 | 1         |                  |     |     |     | = c2            | ·   | c2                           |     | · c2      | c2       | exp        | . (74)    |
|       | (cid:82)∞ |                  |     |     |     | (cid:0)ρ(cid:1) |     |                              |     | (cid:0)ρ, | ρ(cid:1) |            |           |
|       |           | θρ/c2−1e−ρθ/c2dθ |     |     |     | Γ               |     | (cid:0)v+ρ(cid:1)(cs+v+ρ)/c2 |     | γ¯        |          |            | c2        |
|       | 1         |                  |     |     |     | c2              |     |                              |     | c2        | c2       |            |           |
c2
This yields the closed-form mixture (72). To verify that our choice of β ensures that λ has approximate
precision ρ under the full (not truncated) mixture distribution, we use the delta method to calculate the
approximate variance of λ for large β based on the variance of θ under the full gamma mixture:
|     |     |     |     |     |       | (cid:20) | (cid:21) |     |     |     |     |     |      |
| --- | --- | --- | --- | --- | ----- | -------- | -------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |       |          | 1        | 1   | 1   |     |     |     |      |
|     |     |     |     |     | Varλ≈ |          |          | · = | .   |     |     |     | (75) |
|     |     |     |     |     |       |          | c2θ2     | β   | ρ   |     |     |     |      |
θ=1
| A.4 Proof | of         | Proposition |             |     | 2     |      |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | ----------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Under the | conditions | of          | Proposition |     | 2, we | have |     |     |     |     |     |     |     |
(cid:90) λmax
|     |     |     |     | m(s,v)= |     |     | exp{λs−ψ(λ)v}f(λ)dλ. |     |     |     |     |     | (76) |
| --- | --- | --- | --- | ------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ---- |
0
Note that m(s,v) is nondecreasing in s and nonincreasing in v (since ψ ≥0 by our assumptions on ψ).
Choose δ ∈ (0,λ ) so that ψ has three continuous derivatives and f is continuous and positive on [0,δ);
max
suchavalueofδ mustexistbyconditions(i)and(ii). BeforeprovingProposition2,westateseverallemmas.
(0,ψ(cid:48)(δ)),
Lemma 4. Under the conditions of Proposition 2, for any b ∈ we have m(bv,v) < ∞ and
| m(bv,v)→∞ | as  | v →∞. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
31

Proof. Observe
(cid:90) λmax
|     |     | m(bv,v)= | exp{v[λb−ψ(λ)]}f(λ)dλ. |     |     | (77) |
| --- | --- | -------- | ---------------------- | --- | --- | ---- |
0
Note d [λb−ψ(λ)]=b−ψ(cid:48)(λ)<0forallλ≥δbyourconditiononb. Hencetheintegrandexp{v[λb−ψ(λ)]}
dλ
is decreasing on λ ≥ δ and bounded above by evδb on λ ≤ δ (since ψ ≥ 0). The integrand is therefore uni-
| formly bounded | on [0,λ | ), so that m(bv,v)<∞. |     |     |     |     |
| -------------- | ------- | --------------------- | --- | --- | --- | --- |
max
Now Laplace’s asymptotic approximation (Widder, 1942, Chapter VII.2, Theorem 2b) yields
|     |     | (cid:90) |     | Cevψ(cid:63)(b) |     |     |
| --- | --- | -------- | --- | --------------- | --- | --- |
δ
|     |     | exp{v[λb−ψ(λ)]}f(λ)dλ∼ |     | √ , | as v →∞, | (78) |
| --- | --- | ---------------------- | --- | --- | -------- | ---- |
v
0
where C > 0 is a constant not depending on v. (The condition b < ψ(cid:48)(δ) ensures that the maximizer of
λb−ψ(λ)lieswithin[0,δ).) SincetheLHSof (78)lowerboundsm(bv,v)whiletheRHSdivergesasv →∞,
| we must | have m(bv,v)→∞ | as v →∞. |     |     |     |     |
| ------- | -------------- | -------- | --- | --- | --- | --- |
Lemma 5. Under the conditions of Proposition 2, m(M α (v),v)=l 0 /α for all v sufficiently large.
[0,ψ(cid:48)(δ)v)
Proof. Let C(v) := for v > 0. Lemma 4 shows that m(s,v) < ∞ for all s ∈ C(v). Since m(s,v)
is nondecreasing in s, we may apply dominated convergence to find that s (cid:55)→ m(s,v) is continuous at all
s∈C(v). Condition(i)ofProposition2impliesψ ≥0,sothatm(0,v)≤1≤l 0 /αforallv. Finally,Lemma4
shows that sup m(s,v)→∞ as v →∞. Hence, for v sufficiently large, there exists s∈C(v) such that
s∈C(v)
| m(s,v)>l | /α. |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
0
We have argued that, for any sufficiently large v, m(0,v) ≤ l /α < m(s¯,v) < ∞ for some s¯< ψ(cid:48)(δ)v, and
0
m(·,v) is continuous on [0,s¯]. The conclusion follows from the definition (13) of M .
α
| Lemma | 6. Under the conditions | of Proposition | 2, lim | M (v)=∞. |     |     |
| ----- | ----------------------- | -------------- | ------ | -------- | --- | --- |
v→∞ α
Proof. Suppose for the sake of contradiction that there exists a > 0 such that M (v) ≤ a for all v. Then,
α
sincem(s,v)isnondecreasingins,m(M (v),v)≤m(a,v)forallv. Butforsufficientlylargev,wecanwrite
α
a = bv for some b < ψ(cid:48)(δ), so that Lemma 4 implies m(a,v) < ∞ for sufficiently large v. Since condition
(i) of Proposition 2 implies ψ ≥ 0, we have m(s,v) is decreasing in v, and dominated convergence yields
m(a,v)→0 as v →∞. But this implies m(M (v),v)→0, contradicting Lemma 5.
α
We have shown that limsup M α (v)=∞. But since m(s,v) is nondecreasing in s and nonincreasing in
v→∞
v, Lemma 5 implies M (v) must be nondecreasing in v. It follows that lim M (v)=∞.
|       | α                       |                |                |     | v→∞ α |     |
| ----- | ----------------------- | -------------- | -------------- | --- | ----- | --- |
| Lemma | 7. Under the conditions | of Proposition | 2, M (v)=o(v). |     |       |     |
α
Proof. Suppose for the sake of contradiction that M (v) ≥ bv for all v sufficiently large, for some 0 < b <
α
ψ(cid:48)(δ).
Then(againusingthefactthatm(s,v)isnondecreasingins)lim v→∞ m(M α (v),v)≥lim v→∞ m(bv,v)=
| ∞ by Lemma | 4, contradicting | Lemma | 5.  |     |     |     |
| ---------- | ---------------- | ----- | --- | --- | --- | --- |
Proof of Proposition 2. WeinvokeTheorem4ofFulks(1951), settingFulks’hequaltoourv, Fulks’k equal
to our M (v), Fulks’ φ equal to our ψ, Fulks’ ψ equal to the identity function, Fulks’ f equal to our f, and
α
Fulks’ b equal to our λ . Fulks’ assumptions (A1)-(A4) now read as follows.
max
(A1) requires ψ(0) =ψ(cid:48)(0 ) =0, ψ(cid:48)(cid:48)(0 ) > 0, ψ has three continuous derivatives in a neighborhood of the
|         |                   | +                 | +       |     |     |     |
| ------- | ----------------- | ----------------- | ------- | --- | --- | --- |
| origin, | and ψ is positive | and nondecreasing | on (0,λ | ).  |     |     |
max
(A2) requires conditions on the identity function which are trivially satisfied.
(A3) requires f to be integrable and to be continuous and positive at the origin.
| (A4) requires | M (v)→∞ | as v →∞ | and M (v)=o(v). |     |     |     |
| ------------- | ------- | ------- | --------------- | --- | --- | --- |
|               | α       |         | α               |     |     |     |
32

exp(λs−ψ(λ)v)
●
●
●
|     |     |     |     | exp(λ |     | s−ψ(λ | )v) |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ●   |     |       | 5   |       | 5   |     |     |     |     |     |     |
|     |     | ●   |     | ●     |     |       |     |     |     |     |     |     |     |
●
●
|     |     | ●   |     |     | w 5 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
●
●●●●●●●●●●●●●●●●●●
|     |     |     |     |     | ●   |     |     |     | f(λ) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     | 0   |     |     |     |     | ●   |     |     |      |     |     |     |     |
|     |     |     |     |     |     |     |     | ●   | ●    |     | ●   |     |     |
|     | 0   | …λλ | λ λ | λ   | λ   | λ   |     | λ   | λ    |     | λ λ |     |     |
|     |     | 9   | 8 7 | 6 5 | 4   | 3   |     | 2   | 1    |     | 0   | max |     |
λ
Figure 8: Illustration of Theorem 2. Mixture density f(λ) is discretized on a grid (λ )∞ which gets finer as
k k=0
λ↓0. Resulting discrete mixture weights are represented by areas within green bars. Integrand exp{λs−ψ(λ)v} is
evaluated at grid points λ k , illustrated by purple points. Multiplying one integrand evaluation exp{λ k s−ψ(λ k )v}
| by the corresponding |     | weight | w k | gives one | term | of the | sum | (17). |     |     |     |     |     |
| -------------------- | --- | ------ | --- | --------- | ---- | ------ | --- | ----- | --- | --- | --- | --- | --- |
(A1) and (A3) are satisfied by conditions (i) and (ii) of Proposition 2. (A4) is satisfied by Lemmas 6 and 7.
√
For Fulks’ Theorem 4, it remains to verify that v = o(M α (v)). But if this were not true, then we could
apply Theorem 1 or Theorem 2 of Fulks (1951) to conclude that m(M (v),v)→0 as v →∞, contradicting
α
| Lemma 5. | So Fulks’ | Theorem |     | 4 yields |             |     |           |     |          |          |     |     |      |
| -------- | --------- | ------- | --- | -------- | ----------- | --- | --------- | --- | -------- | -------- | --- | --- | ---- |
|          |           |         |     |          |             |     | (cid:114) |     | (cid:26) | (cid:27) |     |     |      |
|          |           |         |     |          |             |     |           | 2π  | M2(v)    |          |     |     |      |
|          |           |         |     | m(M      | (v),v)∼f(0) |     |           | exp | α        | .        |     |     | (79) |
α
|             |     |            |     |          |       |        |       | cv  | 2cv |     |     |     |     |
| ----------- | --- | ---------- | --- | -------- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- |
| Using Lemma | 5   | to set m(M | α   | (v),v)=l | 0 /α, | we may | write |     |     |     |     |     |     |
(cid:114)
|           |               |     |      |             |             | 2π  | (cid:26) M2(v) | (cid:27) | l eo(1) |     |     |     |      |
| --------- | ------------- | --- | ---- | ----------- | ----------- | --- | -------------- | -------- | ------- | --- | --- | --- | ---- |
|           |               |     |      |             |             |     |                | α        | 0       |     |     |     |      |
|           |               |     |      |             | f(0)        | exp |                | =        |         | ,   |     |     | (80) |
|           |               |     |      |             |             | cv  | 2cv            |          | α       |     |     |     |      |
| which can | be rearranged |     | into | the desired | conclusion. |     |                |          |         |     |     |     |      |
Wehaveprovedtheresultforone-sidedbounds,butanearly-identicalargumentappliestotwo-sidedbounds
| such as Proposition |          | 7.         |         |     |        |              |     |     |     |     |     |     |     |
| ------------------- | -------- | ---------- | ------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
| A.5 Proof           |          | of Theorem |         | 2   |        |              |     |     |     |     |     |     |     |
| Recall the          | discrete | mixture    | support |     | points | and weights, |     |     |     |     |     |     |     |
√
|     |     |      | λ      |     |     | λ(η−1)f(λ |     | k    | η)  |               |     |     |      |
| --- | --- | ---- | ------ | --- | --- | --------- | --- | ---- | --- | ------------- | --- | --- | ---- |
|     |     | λ := |        | and | w   | :=        |     |      | for | k =0,1,2,.... |     |     | (81) |
|     |     | k    | ηk+1/2 |     |     | k         |     | ηk+1 |     |               |     |     |      |
O(η−k)
Figure 8 illustrates the construction. To see heuristically why the exponentially-spaced grid λ k =
|     |     |     |     |     |     | (cid:8) |     | (cid:9) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |
makes sense, observe that the integrand exp λs−λ2v/2 is a scaled normal density in λ with mean s/v
|     |     |     | √   |     |     |     |     |     |     |     |     | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and standard deviation 1/ v. In the regime relevant to our curved boundaries, s is of order v, ignoring
√
logarithmic factors. Hence the integrand at time v has both center and spread of order 1/ v, so as v →∞,
therelevantscaleoftheintegrandshrinks. Withthegridλ =O(η−k)wehaveλ −λ =O(λ ),ensuring
|     |     |     |     |     |     |     |     | k   |     |     | k k+1 | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
thattheresolutionofthegridaroundthepeakoftheintegrandmatchesthescaleoftheintegrandasv →∞.
The discrete mixture bound is a valid mixture boundary in its own right, based on a discrete mixing distri-
bution, but we may wish to know how well it approximates the continuous-mixture boundary from which it
is derived. To illustrate the accuracy of the discrete mixture construction, we compare it to the one-sided
normal mixture bound, Proposition 6. By using the same half-normal mixing density in Theorem 2 and
setting η = 1.05, λ = 100, we may evaluate a corresponding discrete mixture bound DM α . With ρ = 14.3,
33

α = 0.05 and l = 1, numerical calculations indicate that DM (v)/NM (v) ≤ 1.004 for 1 ≤ v ≤ 106,
|     |     |     | 0   |     |     |     |     |     |     | α α |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
suggesting that Theorem 2 gives an excellent conservative approximation to the corresponding continuous
mixtureboundaryoveralargepracticalrange. Ofcourse,whenaclosedformisavailableasinProposition6,
one should use it in practice. But an exact closed form integral is rarely available as it is in Proposition 6,
and substantial looseness often accompanies closed-form approximations which provably maintain crossing
probabilityguarantees. Insuchcases,unlessaclosedformisrequired,Theorem2ispreferable. Seefigure10
for an example; in this figure, the bounds of Balsubramani (2014) and Darling and Robbins (1968) involve
| closed-form |     | mixture | integral | approximations. |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |     |         |          |                 |     |     |     |     | √   |     | √   | √   |     |
Proof of Theorem 2. Because f is nonincreasing, f(λ)≥f(λ η) on the interval [λ / η,λ η], which has
|     |     |     |     |     |     |     |           |     | k          |     | k   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | √   |     | (cid:80)∞ |     | (cid:82) ∞ |     |     |     |     |
widthλ (η−1)/ηk+1 =w /f(λ η). Hence w ≤ f(λ)dλ=1. LetGb eadiscr etedistribution
|     | m   | a x |     | (cid:80)∞ k | k   |     |     | k= 0 | k 0 |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
which p la c es mass w / w at the point λ . B y Le mma 2, we know the mixture bound M applied to
|     |     |     | k   | j=0 | j   |     | k   |     |     |     |     | α   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the discrete mixture distribution G yields a sub-ψ uniform boundary with crossing probability α. But
∞
|     |     |     |     | (cid:88) |       |       |      |     | (cid:90)            |     |     |     |      |
| --- | --- | --- | --- | -------- | ----- | ----- | ---- | --- | ------------------- | --- | --- | --- | ---- |
|     |     |     |     | w        | exp{λ | s−ψ(λ | )v}≤ |     | exp{λs−ψ(λ)v}dG(λ), |     |     |     | (82) |
|     |     |     |     |          | k     | k     | k    |     |                     |     |     |     |      |
k=0
so DM α ≥ M α . That is, our discrete mixture approximation DM α is a conservative overestimate of a
corresponding exact mixture boundary M , and can only have a lower crossing probability. So the discrete
α
mixture bound DM satisfies the desired probability inequality P(∃t:S ≥DM (V ))≤α.
|     |           |     | α   |            |     |         |     |               |     | t   | α t |     |     |
| --- | --------- | --- | --- | ---------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- |
| A.6 | Stitching |     | as  | a discrete |     | mixture |     | approximation |     |     |     |     |     |
Suppose we wish to analytically approximate the discrete mixture boundary DM of Theorem 2 in the
α
sub-Gaussian case ψ =ψ . Clearly the sum is lower bounded by the maximum summand, which gives
N
|     |     |     |     |            |     | (cid:26)  |     |     |           |          | (cid:27) |     |      |
| --- | --- | --- | --- | ---------- | --- | --------- | --- | --- | --------- | -------- | -------- | --- | ---- |
|     |     |     |     |            |     | s∈R:sup[w |     |     |           |          | l 0      |     |      |
|     |     |     |     | DM (v)≤sup |     |           |     |     | exp{λ s−ψ | (λ )v}]< |          |     | (83) |
|     |     |     |     | α          |     |           |     | k   | k         | N k      | α        |     |      |
k≥0
|     |     |     |     |     |      | (cid:26) log(l | /w  | α)  | λ (cid:27) |     |     |     |      |
| --- | --- | --- | --- | --- | ---- | -------------- | --- | --- | ---------- | --- | --- | --- | ---- |
|     |     |     |     |     |      |                | 0   | k   | k          |     |     |     |      |
|     |     |     |     |     | =min |                |     | +   | v .        |     |     |     | (84) |
|     |     |     |     |     |      |                | λ   |     | 2          |     |     |     |      |
|     |     |     |     |     | k≥0  |                | k   |     |            |     |     |     |      |
The last expression is the pointwise minimum of a collection of linear boundaries of the form presented in
Lemma 1, each chosen with a different λ k , and with nominal crossing rates w k α so that a union bound
(cid:80)
over crossing events yields total crossing probability w α ≤ α. This is very similar to the stitching
k k
| construction, |     | with | a slightly | different |     | choice | of the | sequence | λ . |     |     |     |     |
| ------------- | --- | ---- | ---------- | --------- | --- | ------ | ------ | -------- | --- | --- | --- | --- | --- |
k
By equating w from Theorem 2 with 1/h(k) from Theorem 1, this observation allows us to view a
k
stitched bound with function h(k) as an approximation to a mixture bound with mixture density f(λ) =
Θ(1/λh(logλ−1))
as λ ↓ 0. For exponential stitching, this yields f(λ) = Θ(1)—densities approaching a
nonzeroconstantasλ↓0, includingthehalf-normaldistribution, correspondtoexponentialstitchedbound-
√
aries growing at a rate V t logV t . For polynomial stitching, we have the corresponding mixture density
(s−1)ss−11
|     |     |     |     |     | fLIL(λ):= |     |     |          | 0≤λ≤exp(−s) | ,   |     |     | (85) |
| --- | --- | --- | --- | --- | --------- | --- | --- | -------- | ----------- | --- | --- | --- | ---- |
|     |     |     |     |     | s         |     |     | λlogsλ−1 |             |     |     |     |      |
matchingthedensityfromBalsubramani(2014,Lemma12)(wetruncateatλ=e−s toensurethedensityis
nonincreasing). The “slower” function h(k)∝klogsk corresponds to f(λ)=Θ(1/λ(logλ−1)(loglogλ−1)s),
| the | density | from | example    | 3 of | Robbins | (1970). |     |     |     |     |     |     |     |
| --- | ------- | ---- | ---------- | ---- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| A.7 | Proof   |      | of Theorem |      | 3       |         |     |     |     |     |     |     |     |
The proof follows a straightforward idea. We break time into epochs ηk ≤ V < ηk+1. Within each epoch
t
|     |     |     |     |     |     |     |     |     | (ηk,g(ηk)) |     | (ηk+1,g(ηk+1)). |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | --- |
we consider the linear boundary passing through the points and This line lies
below g(V ) throughout the epoch, and its crossing probability is determined by its slope and intercept as
t
| in Lemma |      | 1. Taking     | a   | union bound      | over | epochs |     | yields | the result. |     |     |     |     |
| -------- | ---- | ------------- | --- | ---------------- | ---- | ------ | --- | ------ | ----------- | --- | --- | --- | --- |
| We       | need | the following |     | lemma concerning |      | g:     |     |        |             |     |     |     |     |
34

Lemma 8. If g is nonnegative and strictly concave on R , then g(v) is nondecreasing and g(v)/v is strictly
≥0
| decreasing |     | on v >0. |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. If s < 0 is a supergradient of g at some point t, then g(t + u) < g(t) + su < 0 for sufficiently
large u, contradicting the non-negativity of g. So g is nondecreasing. Now fix 0 < x < y and let s be any
supergradientofg atx. Fromnonnegativityandconcavitywehave0≤g(0)≤g(x)−xs,sothats≤g(x)/x.
| Strict | concavity |     | then implies | g(y)<g(x)+s(y−x)≤g(x)y/x. |     |     |     |      |     |     |     |     |     |     |
| ------ | --------- | --- | ------------ | ------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|        |           |     |              |                           |     | ηk  |     | ηk+1 |     |     |     |     |     |     |
Proof of Theorem 3. Fix any η > 1. On ≤ v < we lower bound g(v) by the line a +b v passing
|     |     |     |     |     |     |     |     |     |     |     |     | k   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
through the points (ηk,g(ηk)) and (ηk+1,g(ηk+1)). This line has intercept and slope
ηg(ηk)−g(ηk+1)
|     |     |     |     |     |     | a   | =   |     | ,   |     |     |     |     | (86) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
k
η−1
g(ηk+1)−g(ηk)
|     |     |     |     |     |     | b   | =   |         | .   |     |     |     |     | (87) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | k   |     | ηk(η−1) |     |     |     |     |     |      |
Note a > 0 and b ≥ 0 by Lemma 8. We bound the upcrossing probability of this linear boundary using
|     | k   |     | k   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 1:
|     |     |     |     |     |     |     |     | (cid:26) 2(g(ηk+1)−g(ηk))(ηg(ηk)−g(ηk+1)) |     |     |     |     | (cid:27) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | -------- | --- |
P(∃t≥1:S
|     |     |     | ≥a  | +b V | )≤l | e−2akbk | =l exp | −   |     |          |     |     | .   | (88) |
| --- | --- | --- | --- | ---- | --- | ------- | ------ | --- | --- | -------- | --- | --- | --- | ---- |
|     |     |     | t k | k    | t 0 |         | 0      |     |     | ηk(η−1)2 |     |     |     |      |
The conclusion follows from a union bound over epochs and from the arbitrary choice of η.
Inspection of the proof reveals that the crossing probability bound (19) is valid not only for the boundary
u given in (18), but also for a similar boundary which is finite and linear for all v < 1 and v > v . This
max
| follows | by    | extending | the     | linear | boundaries | over | the | first and | last epochs. |     |     |     |     |     |
| ------- | ----- | --------- | ------- | ------ | ---------- | ---- | --- | --------- | ------------ | --- | --- | --- | --- | --- |
| A.8     | Proof | of        | Theorem |        | 4          |      |     |           |              |     |     |     |     |     |
|         |       |           |         |        |            |      |     |           |              |     | :=  | E   |     | :=  |
For the proof, we take a = 0,b = 1 without loss of generality. Write Y t X t − t−1 X t and δ t
|     |     |     |     |     |     |     |     |     |     | (cid:110) |     |     |     | (cid:111) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- |
X(cid:98)t −E X . ThenY −δ =X −X(cid:98)t ∈[−1,1]. Wewillshowthatexp λ (cid:80)t Y −ψ (λ) (cid:80)t (Y −δ )2
|     | t−1               | t   | t   | t             | t   |       |         |     |      |     | i   | E   | i   | i   |
| --- | ----------------- | --- | --- | ------------- | --- | ----- | ------- | --- | ---- | --- | --- | --- | --- | --- |
|     |                   |     |     |               |     |       |         |     |      | i=1 |     |     | i=1 |     |
| is  | a supermartingale |     | for | each λ∈[0,1), |     | where | we take | c=1 | in ψ | .   |     |     |     |     |
E
|     |     |     |     |     |     |     |     |     | (cid:8) | (λ)ξ2(cid:9) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --- | --- | --- |
The proof of Lemma 4.1 in Fan et al. (2015) shows that exp λξ−ψ ≤1+λξ for all λ∈[0,1) and
E
| ξ ≥−1. | Applied |     | to ξ =y−δ, |     | we have  |     |                  |                 |     |     |     |     |     |      |
| ------ | ------- | --- | ---------- | --- | -------- | --- | ---------------- | --------------- | --- | --- | --- | --- | --- | ---- |
|        |         |     |            |     | (cid:8)  |     | (λ)(y−δ)2(cid:9) |                 |     |     |     |     |     |      |
|        |         |     |            |     | exp λy−ψ |     |                  | ≤eλδ(1+λ(y−δ)). |     |     |     |     |     | (89) |
E
Since Y −δ ≥−1, E Y =0, and δ is predictable, the above inequality implies
|     | t   | t   | t−1 | t   |         | t     |       |           |            |      |     |     |     |      |
| --- | --- | --- | --- | --- | ------- | ----- | ----- | --------- | ---------- | ---- | --- | --- | --- | ---- |
|     |     |     |     | E   | (cid:8) |       |       | )2(cid:9) | ≤eλδt(1−λδ |      |     |     |     |      |
|     |     |     |     |     | exp     | λY −ψ | (λ)(Y | −δ        |            | )≤1, |     |     |     | (90) |
|     |     |     |     | t−1 |         | t     | E     | t t       |            | t    |     |     |     |      |
1−x≤e−x
| using |     |     | in the    | final | step.     |     |     |     |     |     |     |           |     |     |
| ----- | --- | --- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|       |     |     | (cid:80)t |       | (cid:80)t |     |     |     |     |     |     | (cid:80)t |     |     |
ThisshowsthatS = Y = X −tµ issub-exponentialwithvarianceprocessV = (Y −δ )2 =
|           |     |     | t   | i=1 i | i=1 | i   | t    |     |     |     |     | t   | i=1 i | i   |
| --------- | --- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- | --- | --- | ----- | --- |
| (cid:80)t |     | )2  |     |       |     |     | P(∃t |     |     |     |     |     |       |     |
(X i −X(cid:98)i and scale c = 1. It follows that : S t ≥ u(V t )) ≤ α. A similar argument applied with
i=1
−X in place of X shows that P(∃t:−S ≥u(V ))≤α, and a union bound finishes the proof.
|     | t   |     | t   |     |     | t   | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WeremarkthattheproofsofMaurerandPontil(2009,Theorem11),Audibertetal.(2009,Theorem1),and
Balsubramani and Ramdas (2016) follow very different arguments. All three proofs involve a Bennett-type
concentration bound for the sample mean with a radius depending on the true variance, combined via a
union bound with a concentration bound for the sample variance. Audibert et al. (2009) and Balsubramani
and Ramdas (2016) achieve the latter bound using another Bennett/Bernstein-type inequality and the in-
equality EX4 ≤EX2 for |X|≤1, while Maurer and Pontil (2009) use a self-bounding property to achieve a
concentration inequality for the sample variance directly (Maurer and Pontil, 2009, Theorem 7).
In contrast, our argument avoids the union bound over the sample mean and sample variance bounds. We
achievethisbyconstructinganexponentialsupermartingalewhichdirectlyrelatesthedeviationsofS t tothe
“online” empirical variance V . In terms of proof technique, our method owes much more to the literature
t
on self-normalized bounds (de la Pen˜a, 1999, de la Pen˜a et al., 2004, Bercu and Touati, 2008, Delyon, 2009
and especially Fan et al., 2015) than to the literature on empirical-Bernstein bounds.
35

| A.9 Proof | of Corollary |     | 4   |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For case (1), Lemma 3(f) and Lemma 2 of Howard et al. (2020) (cf. Delyon, 2009) show that S =γ (Y )
|     |     |     |     |     |          |     |           |     | t   | max t |
| --- | --- | --- | --- | --- | -------- | --- | --------- | --- | --- | ----- |
|     |     |     |     |     | (cid:16) |     | 2(cid:17) |     |     |       |
is sub-Gaussian with variance process V(cid:101)t =γ (cid:80)t ∆Y 2+ 2E∆Y . Invoking Corollary 1, we have
|     |     |     |     | max |     | i=1 | i 3 i    |          |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     | S   |     |     | (cid:26) | (cid:27) |     |     |
t
|     |     | limsup |     | (cid:113)                      | ≤1  | a.s. | on supV(cid:101)t =∞ | .           |           | (91) |
| --- | --- | ------ | --- | ------------------------------ | --- | ---- | -------------------- | ----------- | --------- | ---- |
|     |     | t→∞    |     | 2V(cid:101)t loglogV(cid:101)t |     |      | t                    |             |           |      |
|     |     |        |     |                                |     |      | t−1(cid:80)t         | ∆Y 2+2E∆Y 2 | a .s. EY2 |      |
Applying the strong law of large numbers elementwise, we have i i → as t → ∞,
|     |     |     |     |     |     |     | i=1 | 3   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and the continuity of the maximum eigenvalue map over the set of positive semidefinite matrices ensures
that t−1V(cid:101)t a → .s. γ (EY 2) = t−1V . Hence, so long as EY 2 > 0 we conclude that, with probability one,
|     | max | 1   | t   |     |     |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:113)
|     |     |     |     | (cid:112) (EY |     |     |     |     |     | EY  |
| --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
sup V(cid:101)t = ∞ and V(cid:101)t loglogV(cid:101)t ∼ γ 2)tloglogt, completing the proof for case (1). (If 2 = 0
| t              |        |     |          | max     | 1      |              |     |     |     | 1   |
| -------------- | ------ | --- | -------- | ------- | ------ | ------------ | --- | --- | --- | --- |
| then the event | {sup V | =∞} | is empty | and the | result | is vacuous.) |     |     |     |     |
t t
In case (2), Fact 1(d) and Lemma 2 of Howard et al. (2020) (cf. Tropp, 2012) show that (S ) defined
t
as above is sub-gamma with variance process (V ) and scale c. The conclusion now follows directly from
t
| Corollary 1. |              |     |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A.10 Proof   | of Corollary |     |     | 5   |     |     |     |     |     |     |
The argument is adapted from Tropp (2015). Let X :=x xT −Σ. The triangle inequality implies (cid:107)X (cid:107) ≤
|     |     |     |     |     | i   | i   | i   |     |     | i op |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
(cid:107)x xT(cid:107) +(cid:107)Σ(cid:107) ≤ 2b. Hence, by Fact 1(c) and Lemma 2 of Howard et al. (2020) (cf. Tropp, 2012),
| i i op | op  |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:16) (cid:80)t (cid:17)
| S =γ  | X is  | sub-Poisson |     | with scale | c=2b     | and      | variance process |     |     |     |
| ----- | ----- | ----------- | --- | ---------- | -------- | -------- | ---------------- | --- | --- | --- |
| t max | i=1 i |             |     |            |          |          |                  |     |     |     |
|       |       |             |     |            | (cid:32) | (cid:33) |                  |     |     |     |
t
(cid:88)
|     |     |     |     | V =γ  | EX2 |     |     |     |     | (92) |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | t max |     | i   |     |     |     |      |
i=1
|     |     |     |     |     | (cid:32) |     | (cid:33) |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
t
|     |     |     |     |     | (cid:88)(cid:2)E[(x | xT)2]−Σ2(cid:3) |     |     |     |      |
| --- | --- | --- | --- | --- | ------------------- | --------------- | --- | --- | --- | ---- |
|     |     |     |     | =γ  |                     |                 |     |     |     | (93) |
|     |     |     |     | max |                     | i               | i   |     |     |      |
i=1
t
|     |     |     |     | (cid:88) | (cid:0)E[(x | xT)2] | (cid:1) |     |     |      |
| --- | --- | --- | --- | -------- | ----------- | ----- | ------- | --- | --- | ---- |
|     |     |     |     | ≤ γ      |             |       | .       |     |     | (94) |
|     |     |     |     |          | max         | i i   |         |     |     |      |
i=1
Inthefinalstep,weneglectthenegativesemidefiniteterm−Σ2andusethefactthatthemaximumeigenvalue
of a sum of positive semidefinite matrices is bounded by the sum of the maximum eigenvalues. We continue
by using (cid:107)x xT(cid:107)=(cid:107)x (cid:107)2 ≤b and the fact the expectation respects the semidefinite order to obtain
i i i 2
t
|     |     |     |     | (cid:88) |     | (cid:0)E(cid:107)x | xT(cid:1)   |     |     |      |
| --- | --- | --- | --- | -------- | --- | ------------------ | ----------- | --- | --- | ---- |
|     |     |     |     | V ≤      | γ   |                    | (cid:107)2x |     |     | (95) |
|     |     |     |     | t        | max |                    | i 2 i i     |     |     |      |
i=1
|     |     |     |     | ≤tb(cid:107)Σ(cid:107) |     | .   |     |     |     | (96) |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | ---- |
op
Plugging this upper bound on V t into the discrete mixture bound of Theorem 2 gives the result.
| B Implications |     | among |     | sub-ψ | boundaries |     |     |     |     |     |
| -------------- | --- | ----- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
TogetherwithTable1,thefollowingpropositionformalizestherelationshipsillustratedinFigure2,restating
Proposition 2 of Howard et al. (2020) in the language of uniform boundaries. The first row of Table 1 uses
the function
(cid:40) h2−g2
|     |     |     |     |          |           |     | , g <h |     |     |      |
| --- | --- | --- | --- | -------- | --------- | --- | ------ | --- | --- | ---- |
|     |     |     |     | ϕ(g,h):= | 2log(h/g) |     |        |     |     | (97) |
|     |     |     |     |          | gh,       |     | g ≥h.  |     |     |      |
36

|     |     |     |     |     | ψ   | ψ   |     | a   | Restriction |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |     |     |     |     | 1   | 2   |     |     |             |     |     |     |
ϕ(g,h)
|     |     |     | (1) |     | ψ   | ψ     |     |     | any g,h>0 |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --------- | --- | --- | --- |
|     |     |     |     |     | N   | B,g,h |     | gh  |           |     |     |     |
(g+h)2
|     |     |     | (2)  |     | ψ     | ψ       |     |     | any g,h>0 |     |     |     |
| --- | --- | --- | ---- | --- | ----- | ------- | --- | --- | --------- | --- | --- | --- |
|     |     |     |      |     | N     | B,g,h   |     | 4gh |           |     |     |     |
|     |     |     | (3)  |     | ψ     | ψ       |     | 1   | any g     | >−c |     |     |
|     |     |     |      |     | P,c   | B,g,g+c |     |     |           |     |     |     |
|     |     |     | (5)  |     | ψ     | ψ       |     | 1   |           |     |     |     |
|     |     |     |      |     | G,c   | P,3c    |     |     |           |     |     |     |
|     |     |     | (6)  |     | ψ     | ψ       |     | 1   |           |     |     |     |
|     |     |     |      |     | E,c   | G,2c/3  |     |     |           |     |     |     |
|     |     |     | (7)  |     | ψ G,c | ψ E,c   |     | 1   | c≥0       |     |     |     |
|     |     |     | (8)  |     | ψ     | ψ       |     | 1   | c<0       |     |     |     |
|     |     |     |      |     | G,c   | E,2c    |     |     |           |     |     |     |
|     |     |     | (9)  |     | ψ     | ψ       |     | 1   | c<0       |     |     |     |
|     |     |     |      |     | P,c   | G,c/2   |     |     |           |     |     |     |
|     |     |     | (10) |     | ψ N   | ψ P,c   |     | 1   | any c<0   |     |     |     |
|     |     |     | (11) |     | ψ     | ψ       |     | 1   |           |     |     |     |
|     |     |     |      |     | B,g,h | P,−g    |     |     |           |     |     |     |
Table1: Foreachrow,ifuisasub-ψ uniformboundary,subjecttothegivenrestriction,thenv(cid:55)→u(av)isasub-ψ
|                   |     |        |            | 1   |           |             |     |                 |     |     |     | 2   |
| ----------------- | --- | ------ | ---------- | --- | --------- | ----------- | --- | --------------- | --- | --- | --- | --- |
| uniform boundary. |     | ϕ(g,h) | is defined | in  | (97). See | Proposition |     | 11 for details. |     |     |     |     |
Proposition 11. For each row in Table 1, if u is a sub-ψ 1 uniform boundary, and the given restrictions
are satisfied, then v (cid:55)→ u(av) is a sub-ψ uniform boundary for the given constant a. Furthermore, when
2
we allow only transformations of the form v (cid:55)→u(av), these capture all possible implications among the five
sub-ψ boundary types defined above, and the given constants are the best possible (in the case of row (2), the
constant (g+h)2/4gh is the best possible of the form k/gh where k depends only on the total range g+h).
A reader who is familiar with Howard et al. (2020) will note that the arrows in Figure 2 are reversed with
respect to Figure 4 in their paper. Indeed, since any sub-Bernoulli process is also sub-Gaussian, it follows
that any sub-Gaussian uniform boundary is also a sub-Bernoulli uniform boundary, and so on.
| C Additional |     |                | proofs |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C.1 Proof    |     | of Proposition |        |     | 3   |     |     |     |     |     |     |     |
Let k :=(l /α)2. For part (a), we will set the derivative of the squared objective u2(v)/v to zero:
0
|     |     |     | (cid:20)(cid:16) ρ(cid:17)(cid:18) |     | (cid:18) | (cid:19)(cid:19)(cid:21) |     | (cid:18) |       | (cid:19) |     |      |
| --- | --- | --- | ---------------------------------- | --- | -------- | ------------------------ | --- | -------- | ----- | -------- | --- | ---- |
|     |     | d   |                                    |     | k(v+ρ)   |                          |     | ρ        | k(v+ρ | 1        |     |      |
|     |     |     | 1+                                 | log |          |                          | =−  | log      |       | + =0.    |     | (98) |
v2
|     |     | dv  | v   |     | ρ   |     |          |              | ρ        | v            |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | -------- | ------------ | --- | ---- |
|     |     |     |     |     |     |     | (cid:18) | v+ρ (cid:19) | (cid:26) | v+ρ (cid:27) | 1   |      |
|     |     |     |     |     |     |     | −        |              | exp −    | =−           | .   | (99) |
|     |     |     |     |     |     |     |          | ρ            |          | ρ            | ek  |      |
We solve this equation using the lower branch W since we know −(v+ρ)/ρ≤−1:
−1
(cid:18) (cid:19)
|     |     |     |     |     | v+ρ |     |     | 1   |     |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     | =−W |     | −   | ,   |     |     | (100) |
−1
|                     |         |                |          |          |          | ρ      |                  | ek       |          |       |     |       |
| ------------------- | ------- | -------------- | -------- | -------- | -------- | ------ | ---------------- | -------- | -------- | ----- | --- | ----- |
| which is equivalent |         | to             | (21).    |          |          |        |                  |          |          |       |     |       |
| For part            | (b), we | optimize       | the      | squared  | boundary | u2(v): |                  |          |          |       |     |       |
|                     |         |                | (cid:20) |          | (cid:18) |        | (cid:19)(cid:21) | (cid:18) | (cid:19) |       |     |       |
|                     |         |                | d        |          | k(v+ρ)   |        |                  | k(v+ρ)   |          | v     |     |       |
|                     |         |                |          | (v+ρ)log |          |        | =log             |          |          | − =0. |     | (101) |
|                     |         |                | dρ       |          |          | ρ      |                  |          | ρ        | ρ     |     |       |
| which is equivalent |         | to             | (98).    |          |          |        |                  |          |          |       |     |       |
| C.2 Proof           |         | of Proposition |          |          | 4        |        |                  |          |          |       |     |       |
First, Robbins and Siegmund (1970, Theorem 1) show that, for B(t) a standard Brownian motion,
|     |     |     |     | P(∃t∈(0,∞):B(t)≥M |     |     |     | (t))=α. |     |     |     | (102) |
| --- | --- | --- | --- | ----------------- | --- | --- | --- | ------- | --- | --- | --- | ----- |
α
37

Let (X
t
)∞
t=1
be any i.i.d. sequence of mean-zero random variables with unit variance and EeλX1 ≤ eλ
√
2/2,
for example standard normal or Rademacher random variables. For each m ∈ N, let S(m) := (cid:80)t X / m
t i=1 i
and V(m) :=t/m, noting that (S(m)) is sub-Gaussian with variance process (V(m)). Our proof rests upon a
t t t
standard application of Donsker’s theorem, detailed below, which shows that, for any T ∈N,
(cid:16) (cid:17)
lim P ∃t∈[mT]:S(m) ≥M (V(m)) =P(∃t∈(0,T]:B(t)≥M (t)). (103)
t α t α
m→∞
To obtain the desired conclusion from (103), we write, for any m∈N and T ∈N,
(cid:16) (cid:17) (cid:16) (cid:17)
P ∃t∈N:S(m) ≥M (V(m)) ≥P ∃t∈[mT]:S(m) ≥M (V(m)) . (104)
t α t t α t
Take m→∞ and use (103) to find, for any T ∈N,
(cid:16) (cid:17)
liminfP ∃t∈N:S(m) ≥M (V(m)) ≥P(∃t∈(0,T]:B(t)≥M (t)). (105)
t α t α
m→∞
Now take T →∞ to obtain
(cid:16) (cid:17)
liminfP ∃t∈N:S(m) ≥M (V(m)) ≥P(∃t∈(0,∞):B(t)≥M (t))=α, (106)
t α t α
m→∞
by (102). But for each m∈N, S(m) is sub-Gaussian with variance process V(m), so that
t t
(cid:16) (cid:17)
P ∃t∈N:S(m) ≥M (V(m)) ≤α. (107)
t α t
Together, (106) and (107) yield
(cid:16) (cid:17)
lim P ∃t∈N:S(m) ≥M (V(m)) =α. (108)
t α t
m→∞
Since (S(m),V(m))∈S1 for each m, the conclusion follows.
t t ψN
Toprove(103),wewillusethefactthatM :R →R iscontinuous,increasingandconcave,asprovedin
α ≥0 ≥0
Lemma9below. Foreacht∈R letS(mt)beequaltoS formt∈Nandalinearinterpolationotherwise
>0 mt
(withS(0)=0). LetC[0,T]denotethespaceofcontinuous,real-valuedfunctionson[0,T]equippedwiththe
sup-norm,andletP denotetheprobabilitymeasureforstandardBrownianmotion. Wefirstuseacorollary
0
of Donsker’s theorem: for any ϕ : C[0,T] → R continuous P -a.s., we have (Durrett, 2017, Theorems 8.1.5,
0
8.1.11)
(cid:18) (cid:19)
S(m·)
ϕ √ → d ϕ(B(·)) as m→∞. (109)
m
We let ϕ(f) := sup [f(t)−M (t)], so that by compactness of [0,T] and continuity of f and M ,
t∈[0,T] α α
√
d
ϕ(f) ≥ 0 if and only if f(t) ≥ M (t) for some t ∈ [0,T]. Now ϕ(S(m·)/ m) → ϕ(B(·)), and note that
α
ϕ(B(·)) has a continuous distribution: the distribution when M (t) ≡ 0 is well-known by the reflection
α
principle, and the measure for the Brownian motion with drift B(t)−M (t)+M (0) is equivalent to the
α α
measure for B(t) by the Cameron-Martin theorem (Morters and Peres, 2010, Theorem 1.38). Hence
(cid:18) (cid:19)
S(mt)
P ∃t∈[0,T]: √ ≥M (t) →P(∃t∈[0,T]:B(t)≥M (t)). (110)
m α α
ButbecauseM (t)isconcave,thelinearinterpolationofS(·)cannotaddanynewupcrossingsbeyondthose
α
in (S ):
t
(cid:18) (cid:19) (cid:18) (cid:19)
S(mt) S
P ∃t∈[0,T]: √ ≥M (t) =P ∃x∈[mT]: √x ≥M (x/m) (111)
m α m α
(cid:16) (cid:17)
=P ∃t∈[mT]:S(m) ≥M (V(m)) . (112)
t α t
Combining (112) with (110) yields (103), completing the proof.
Lemma 9. The function M :R →R is continuous, increasing and concave.
α ≥0 ≥0
38

Proof. Continuity of M (v) is clear from the continuity of exp{λs−ψ(λ)v} in s and v, which also implies
α
(cid:90)
l 0
|     |     |     |     |     | exp{λM |     | (v)−ψ(λ)v}dF(λ)= |     |     |     |     | (113) |
| --- | --- | --- | --- | --- | ------ | --- | ---------------- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |        |     | α                |     |     | α   |     |       |
for all v > 0. That is, the left-hand side is constant in v, hence has derivative with respect to v equal to
zero. We may exchange the derivative and integral by Theorem A.5.1 of Durrett (2017), noting that the
integrand is positive and continuously differentiable in v and F is a probability measure. This yields
A(v)
|     |     |     |     |     | M(cid:48) | (v)= |     | >0, |     |     |     | (114) |
| --- | --- | --- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | ----- |
α
B(v)
(cid:90)
ψ(λ)eλMα(v)−ψ(λ)vdF(λ)
|     |     |     |     |     | where | A(v):= |     |     |     |     |     | (115) |
| --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | ----- |
(cid:90)
|     |     |     |     |     | and | B(v):= | λeλMα(v)−ψ(λ)vdF(λ). |     |     |     |     | (116) |
| --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | --- | --- | ----- |
Both A(v) > 0 and B(v) > 0 since the integrands are positive, which shows that M is increasing. Differ-
α
| entiating | again | yields,                    | after | some | algebra,          |                           |     |     |                       |     |     |       |
| --------- | ----- | -------------------------- | ----- | ---- | ----------------- | ------------------------- | --- | --- | --------------------- | --- | --- | ----- |
|           |       |                            |       |      | (cid:90) (cid:18) | [λA(v)−ψ(λ)B(v)]2(cid:19) |     |     |                       |     |     |       |
|           |       | B2(v)M(cid:48)(cid:48)(v)= |       |      |                   | −                         |     |     | eλMα(v)−ψ(λ)vdF(λ)≤0, |     |     | (117) |
α
B(v)
| since | the integrand |     | is now | nonpositive, |     | showing | that | M is | concave. |     |     |     |
| ----- | ------------- | --- | ------ | ------------ | --- | ------- | ---- | ---- | -------- | --- | --- | --- |
α
| C.3 | Proof | of  | Corollary |     | 6   |     |     |     |     |     |     |     |
| --- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Write µ(cid:63) := ET(X ).We have noted in the discussion preceding the result that the exponential process
1
exp{λS (µ)−tψ (λ)} is the likelihood ratio testing H : θ = θ(µ) against H : θ = θ(µ)+λ. It is well-
|     | t   | µ   |     |     |     |     |     | 0   |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
known that the likelihood ratio is a martingale under the null. Hence (S (µ(cid:63))) is sub-ψ with variance
t µ(cid:63)
|     |     |     |     |     |     |     | P(∃t | (µ(cid:63)) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- |
process V t = t, and it follows immediately that : S t ≥ u µ(cid:63) (t)) ≤ α 1 . Apply the same argument
with −X in place of X to conclude that P(∃t : −S (µ(cid:63)) ≥ u˜ (t)) ≤ α . A union bound completes the
|     | t   |     | t   |     |     |     |     | t   | µ(cid:63) |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
argument.
| C.4 | Proof       | of      | Lemma | 3       |           |     |          |     |           |     |          |       |
| --- | ----------- | ------- | ----- | ------- | --------- | --- | -------- | --- | --------- | --- | -------- | ----- |
| The | implication | (a)⇒(b) |       | follows | from      |     |          |     |           |     |          |       |
|     |             |         |       |         | (cid:34)∞ |     | (cid:35) |     |           |     | ∞        |       |
|     |             |         |       |         | (cid:91)  |     |          |     |           |     | (cid:91) |       |
|     |             |         |       | A =     | A         | ∩{T | =t}      | ∪[A | ∩{T =∞}]⊆ |     | A .      | (118) |
|     |             |         |       | T       |           | t   |          | ∞   |           |     | t        |       |
|     |             |         |       |         | t=1       |     |          |     |           |     | t=1      |       |
=inf{t∈N:A (cid:83)∞
It is clear that (b)⇒(c). For (c)⇒(a), take τ t occurs}, so that A τ = A t .
t=1
| D   | Computing |     | conjugate |     |     | mixture |     | bounds |     | by  | root-finding |     |
| --- | --------- | --- | --------- | --- | --- | ------- | --- | ------ | --- | --- | ------------ | --- |
In this section we demonstrate that our conjugate mixture boundaries, which involve the supremum M (v)
α
defined in (13), can be computed via root-finding. We assume that ψ is CGF-like, a property which holds
| for | all of the | ψ functions | in  | Section | 2:  |     |     |     |     |     |     |     |
| --- | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition 3 (Howard et al., 2020, Definition 2). A real-valued function ψ with domain [0,λ max ) is
called CGF-like if it is strictly convex and twice continuously differentiable with ψ(0) = ψ(cid:48)(0 ) = 0 and
+
| sup |     | ψ(λ)=∞. | For | such | a function, |     | we write |     |     |     |     |     |
| --- | --- | ------- | --- | ---- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
λ∈[0,λmax)
|     |     |     |     |     |     | ¯b:= | sup | ψ(cid:48)(λ)∈(0,∞]. |     |     |     | (119) |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------------------- | --- | --- | --- | ----- |
λ∈[0,λmax)
39

Lemma 2 implies that, with probability at least 1−α, m(S ,V )<l /α for all t, where
|     |     |     |     |     |     |     | t t | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
|     |     |     |     |     | m(s,v)= | exp{λs−ψ(λ)v}dF(λ). |     |     | (120) |
| --- | --- | --- | --- | --- | ------- | ------------------- | --- | --- | ----- |
We are interested in the set A(v) := {s ∈ R : m(s,v) < l /α} for fixed v ≥ 0. It is clear that m(0,v) ≤
0
1 < l 0 /α whenever l 0 ≥ 1 (which holds in all cases we consider), since ψ ≥ 0, v ≥ 0 and F is a probability
distribution. So 0∈A(v) always. We show below that, in addition, A(v) is always an interval.
Forone-sidedboundaries,F issupportedonλ≥0,andsolongasF isnotapointmassatzero(whichwould
beanuninterestingmixture),m(s,v)isstrictlyincreasinginswheneverm(s,v)<∞. Hencem(s,v)=l /α
0
| for at most | one | value | of s(cid:63)(v)>0, |     | in which | case A(v)=(−∞,s(cid:63)(v)). |     |     |     |
| ----------- | --- | ----- | ------------------ | --- | -------- | ---------------------------- | --- | --- | --- |
It is possible that m(s,v)<l /α for all s where the integral converges. To examine this case, we fix v >0,
0
| which is | the interesting |       | case | in practice, | and | make | two observations: |     |     |
| -------- | --------------- | ----- | ---- | ------------ | --- | ---- | ----------------- | --- | --- |
| •        |                 | <¯bv, |      |              |     |      |                   |     |     |
Whenever s we have m(s,v) < ∞. Indeed, in this case, exp{λs−ψ(λ)v} → 0 as λ → ∞, and
as the integrand is continuous in λ, it must be uniformly bounded. It follows immediately that we can
| have | m(s,v)=∞ |     | only | when¯b<∞. |     |     |     |     |     |
| ---- | -------- | --- | ---- | --------- | --- | --- | --- | --- | --- |
• Whenever¯b<∞,wehaveS ≤¯bV a.s.,aconsequenceofTheorem1(a)ofHowardetal.(2020),which
t t
|     |     | P(∃t |     | a+¯bV |     |     |     |     |     |
| --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- |
shows that : S ≥ ) = 0 for all a > 0. (To verify this fact, note we must have λ = ∞
|     |     |     | t   |     | t   |     |     |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
when¯b<∞ in order for the CGF-like condition sup ψ(λ)=∞ to hold.)
λ∈[0,λmax)
Hence,when¯b=∞weneednotworryaboutm(s,v)=∞. When¯b<∞,itsufficestocheckm(¯bv,v),which
|     |     | m(¯bv,v)≥l |     |     |     |     |     | s∈[0,¯bv]. |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | ---------- | --- |
may be infinite. If /α, then we search for a root of m(s,v)=l /α in the interval If
|     |     |     |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m(¯bv,v) < l /α, it suffices to take M (v) =¯bv+(cid:15) for any (cid:15) > 0. In practice, it seems more reasonable to
|     | 0   |     |     |     | α   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bound¯bv
take the upper and use a closed confidence set instead of an open one.
For two-sided boundaries, when F has support on both λ>0 and λ<0, in general we require the technical
condition
(cid:90)
|λ|kexp{λs−ψ(λ)v}dF(λ)<∞,
|     |     |     |     |     |     |     |     | for k =1,2. | (121) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- |
This ensures that we may differentiate m(s,v) twice with respect to s, exchanging the derivative and the
integral both times (Durrett, 2017, Theorem A.5.3). Hence, whenever condition (121) holds,
(cid:90)
d2
|     |     |     |     | m(s,v)= |     | λ2exp{λs−ψ(λ)v}dF(λ)≥0, |     |     | (122) |
| --- | --- | --- | --- | ------- | --- | ----------------------- | --- | --- | ----- |
ds2
so that m(s,v) is convex in s for each v ≥ 0. As m(0,v) < l 0 /α, we conclude that m(s,v) = l 0 /α for at
most one value s(cid:63)(v)>0 and one value s (v)<0, and A(v)=(s (v),s(cid:63)(v)). A similar discussion as above
|         |          |     |        |          | (cid:63) |     |                 | (cid:63) |     |
| ------- | -------- | --- | ------ | -------- | -------- | --- | --------------- | -------- | --- |
| applies | when¯b<∞ |     | and we | may have | m(s,v)=∞ |     | for some values | of s.    |     |
AsProposition5yieldsaclosed-formresult,onlyProposition7requiresthatweverifycondition(121). From
| the proof | of Proposition |     | 7 in | Appendix | A.3,               | it suffices | to show that       |     |       |
| --------- | -------------- | --- | ---- | -------- | ------------------ | ----------- | ------------------ | --- | ----- |
|           |                |     |      |          | (cid:90) 1(cid:12) | (cid:18)    | (cid:19)(cid:12) k |     |       |
|           |                |     |      |          | (cid:12)           | p           | (cid:12)           |     |       |
|           |                |     |      |          | (cid:12)log        |             | pa(1−p)bdp<∞       |     | (123) |
(cid:12)
|     |     |     |     |     | (cid:12) | 1−p | (cid:12) |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- |
0
for some a,b>0 and k =1,2. This follows from the fact that the integrand is continuous on p∈(0,1) and
| approaches | zero | as p→0   | and | p→1,    | so it | is bounded.    |     |     |     |
| ---------- | ---- | -------- | --- | ------- | ----- | -------------- | --- | --- | --- |
| E Tuning   |      | discrete |     | mixture |       | implementation |     |     |     |
In Section 3.5 we have discussed the choice of mixing precision in order to tune a mixture bound for a
particular range of sample sizes. For discrete mixtures, the value λ must also be chosen, and this depends
on the minimum relevant value of V : making λ larger will make the resulting bound tighter over smaller
t
values of V t at the cost of a looser bound for larger values of V t . In practice, for ψ = ψ G , setting λ =
40

[c+ (cid:112) m/2logα−1]−1 will ensure the bound is tight for V ≥ m. Furthermore, when evaluating DM (v) in
|     |     |     |     |     |     |     | t   |     |     |     |     | α   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
practice, the sum can be truncated after k = (cid:100)log (λ[c+ 5v/logα−1])(cid:101) terms. The remainder of this
|                  |     |                |     |     | max |     | η   |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| section explains |     | these choices. |     |     |     |     |     |     |     |     |     |     |
We wish to understand what range of values of λ our discrete mixture must cover to ensure we get a tight
bound for all V ∈[m,v ]. At V =m the value of λ which yields the optimal linear bound from Lemma 1
|          | t               | max       |     | t   |     |        |      |     |     |     |     |       |
| -------- | --------------- | --------- | --- | --- | --- | ------ | ---- | --- | --- | --- | --- | ----- |
| is found | by optimizing   |           |     |     |     |        |      |     |     |     |     |       |
|          |                 |           |     |     |     | logα−1 | ψ(λ) |     |     |     |     |       |
|          |                 |           |     |     |     | +      |      | ·m, |     |     |     | (124) |
|          |                 |           |     |     |     | λ      | λ    |     |     |     |     |       |
| yielding | the first-order | condition |     |     |     |        |      |     |     |     |     |       |
logα−1
|     |     |     |     |     | λψ(cid:48)(λ)−ψ(λ)= |     |     |     | .   |     |     | (125) |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | ----- |
m
| For ψ =ψ | , this | becomes |     |     |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
G
|          |        |     |     |     |     | λ2       | logα−1 |     |     |     |     |       |
| -------- | ------ | --- | --- | --- | --- | -------- | ------ | --- | --- | --- | --- | ----- |
|          |        |     |     |     |     |          | =      | ,   |     |     |     | (126) |
|          |        |     |     |     |     | 2(1−cλ)2 |        | m   |     |     |     |       |
| which is | solved | by  |     |     |     |          |        |     |     |     |     |       |
1
|     |     |     |     |     | λ(cid:63)(m)= |     |     |     | .   |     |     | (127) |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | ----- |
(cid:112)
|     |     |     |     |     |     | c+  | m/2logα−1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Large values of λ are necessary to achieve tight bounds for small V . Hence, to ensure good performance
|     |     |     |     | (cid:112) |     |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
at V = m we choose λ = [c+ m/2logα−1]−1. Similarly, to ensure the sum safely covers V = v we
| t   |     |     |     |     |     |     |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
ensure λ ≤ [c + 10v/2logα−1]−1 (using an arbitrary “fudge factor” of ten), which yields k =
|     | kmax |     |     |     |     |     |     |     |     |     |     | max |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112) 5v/logα−1])(cid:101).
| (cid:100)log η (λ max | [c+ |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We note that η must also be chosen, but the only tradeoff here is computational. Smaller values of η lead
to more accurate approximations of the discrete mixture to the target continuous mixture, but require more
terms to be summed. We have found η = 1.1 to provide excellent approximations in the examples we have
examined.
F Intrinsic time, change of units and minimum time conditions
In this section we point out that a bound expressed in terms of intrinsic time yields an infinite family of
relatedboundsviascaling,andthat“minimumtime”conditionsinsuchbounds(suchasm∨V inTheorem1)
t
| can be freely | scaled | as well. | Suppose |     | we have | a uniform | bound | of  | the form |     |     |     |
| ------------- | ------ | -------- | ------- | --- | ------- | --------- | ----- | --- | -------- | --- | --- | --- |
P(∃t≥1:S
|     |     |     |     |     |     | ≥u  | (m∨V | ))≤α, |     |     |     | (128) |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | ----- |
|     |     |     |     |     |     | t   | c    | t     |     |     |     |       |
where intrinsic time V has the same units as S2, as usual, and c is some parameter with the same units as
|     |     | t   |     |     |     | t   |     |     |     |     | √   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S . Then, fixing any γ >0 and applying the bound (128) to the scaled observations X / γ, which amounts
| t           |           |     |          |     |      |          |                  |     |     |     | t   |       |
| ----------- | --------- | --- | -------- | --- | ---- | -------- | ---------------- | --- | --- | --- | --- | ----- |
| to a change | of units, | we  | have     |     |      |          |                  |     |     |     |     |       |
|             |           |     | (cid:18) |     |      | (cid:18) | (cid:19)(cid:19) |     |     |     |     |       |
|             |           |     |          |     | S    |          | V                |     |     |     |     |       |
|             |           | α≥P | ∃t≥1:    | √   | t ≥u | √ m∨     | t                |     |     |     |     | (129) |
|             |           |     |          |     |      | c/ γ     |                  |     |     |     |     |       |
|             |           |     |          |     | γ    |          | γ                |     |     |     |     |       |
(cid:18) (cid:19)
|     |     |           |     |     |          |     |       |     |       | √    | v   |       |
| --- | --- | --------- | --- | --- | -------- | --- | ----- | --- | ----- | ---- | --- | ----- |
|     |     | =P(∃t≥1:S |     |     | ≥h (γm∨V | )), | where | h   | (v):= | γu √ | .   | (130) |
|     |     |           |     |     | t c      | t   |       | c   |       | c/ γ | γ   |       |
By changing units we have obtained a new bound on S t with different minimum time γm and a different
shape. Forexample, applyingthischangeofunitstothestitchedboundary (8)withm=1yieldsthefamily
of bounds
(cid:115)
|     |     | (cid:32) |        |     |     |                | (cid:18) | (cid:19) | (cid:18) | (cid:19)(cid:33) |     |       |
| --- | --- | -------- | ------ | --- | --- | -------------- | -------- | -------- | -------- | ---------------- | --- | ----- |
|     |     |          |        |     |     |                | γ∨V      |          | γ∨V      |                  |     |       |
|     |     | P        | ∃t≥1:S | ≥k  |     | (γ∨V )(cid:96) |          | t +ck    | (cid:96) | t ≤α             |     | (131) |
|     |     |          |        | t   | 1   | t              |          |          | 2        |                  |     |       |
|     |     |          |        |     |     |                | γ        |          |          | γ                |     |       |
41

Polynomial stitching (ours)
Inverted stitching (ours)
Discrete mixture (ours)
yradnuoB
Normal mixture
Hoeffding bound
CLT bound
0
|     | 0   |     |     |     |     |                                                                |     | 105 |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | V   | t                                                              |     |     |     |     |     |
Figure9: Pointwiseanduniformboundsforindependent1-sub-Gaussianobservations,α=0.025. Alltuningparam-
(cid:112)
eters are chosen to optimize roughly for time V = 104. The dotted lines show the Hoeffding bound 2V logα−1,
|     |     |     |     |     |     | t   |     | √   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which is nonasymptotically pointwise valid, and the CLT bound z V , which is asymptotically pointwise valid.
1−α t
|     |     |     |     |     |     |     | 104, |     | (k+1)1.4ζ(1.4). |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --------------- | --- | --- |
Polynomial stitching uses Theorem 1 with η = 2.04, m = and h(k) = The inverted stitching
|     |     | (cid:112) |     |     |     |     |     |     |     |     | 1020, |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
boundary is 1.7 (V t ∨104)(log(1+log((V t ∨104)/104)+3.5), using Theorem 3 with η = 2.99, v max = and
error rate 0.82α to account for finite horizon and ensure a fair comparison. Discrete mixture applies Theorem 2
to the density f(λ) = 0.4·1 /[λlog1.4(λ e/λ)] with η = 1.1 and λ = 0.044; see Appendix A.6 for
|             |     |            |     | 0≤λ≤λmax      |      |      | max     |     | max |     |     |
| ----------- | --- | ---------- | --- | ------------- | ---- | ---- | ------- | --- | --- | --- | --- |
| motivation. |     | The normal |     | mixture bound | (53) | uses | ρ=1260. |     |     |     |     |
foranyγ >0, withthedefinitionof(cid:96)unchangedfrom(8). Noteonlytheargumentof(cid:96)hasbeenscaled. We
started with a single bound (8) expressed in terms of V and ended up with a family of bounds on the same
t
processS ,oneforeachvalueofγ. Indeed,thetuningparameterminTheorem1isobtainedbyexactlythis
t
argument. The effect is more clear if we let c=0 and examine the upper bound on the normalized process
√
| S / | V : then | for | any γ | >0, with | probability |     | at least 1−α, |     |     |     |     |
| --- | -------- | --- | ----- | -------- | ----------- | --- | ------------- | --- | --- | --- | --- |
t t
|     |     |     |     |     |     |    | (cid:114)           |         |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ------- | --- | --- | ----- |
|     |     |     |     |     |     |     | (cid:16) (cid:17)   |         |     |     |       |
|     |     |     |     |     |     | k | V                   |         |     |     |       |
|     |     |     |     |     | S   |     | 1 (cid:96) t , when | V t ≥γ, |     |     |       |
|     |     |     |     |     | √   | t ≤ | γ                   |         |     |     | (132) |
(cid:113)
|     |     |     |     |     | V   | k | γ(cid:96)(1), |       |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | --- | --- |
|     |     |     |     |     |     | t   | when          | V <γ. |     |     |     |
|     |     |     |     |     |     |     | 1 Vt          | t     |     |     |     |
Now the right-hand depends on V only through V /γ, so that the effect of changing γ is simply to multi-
|     |     |     |     |     | t   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
plicatively shift the bound backwards or forwards in time without changing the bounded process.
| G   | Detailed |     | comparison |     |     | of  | finite LIL | bounds |     |     |     |
| --- | -------- | --- | ---------- | --- | --- | --- | ---------- | ------ | --- | --- | --- |
Figures 9 and 10 compare our finite LIL bounds to several existing bounds. Below we restate the original
results from the various papers giving finite LIL bounds included in Figure 10. In table 2, for ease of
| comparison, |     | we write | all | bounds | in the   | form |                   |     |     |     |       |
| ----------- | --- | -------- | --- | ------ | -------- | ---- | ----------------- | --- | --- | --- | ----- |
|             |     |          |     |        | P(∃t≥1:S |      | (cid:112)         |     |     |     |       |
|             |     |          |     |        |          |      | ≥A t(loglogBt+C), |     |     |     | (133) |
t
valid for independent 1-sub-Gaussian observations. When the original bound holds only for t ≥ n instead
of t ≥ 1, we apply a change of units argument to replace loglogBt with loglogBnt and t ≥ n with t ≥ 1,
so that all bounds are comparable (see Appendix F). When bounds are expressed in terms of intrinsic time
V (Balsubramani, 2014), this is formally justified. When they are expressed in terms of nominal time
t
(Darling and Robbins, 1967b, 1968) this is only a heuristic argument, but we conjecture that proofs of
such bounds could be generalized to justify this scaling. When observations are i.i.d. from an infinitely
divisible distribution, the change is formally justified by replacing each observation X with a sum of n i.i.d.
i
(cid:80)n
| “pseudo-observations” |     |     |     | Z i such | that | Z i | ∼X 1 . |     |     |     |     |
| --------------------- | --- | --- | --- | -------- | ---- | --- | ------ | --- | --- | --- | --- |
i=1
•
Jamieson and Nowak (2014), Lemma 1: for i.i.d. sub-Gaussian observations with variance parameter
σ2,
(cid:115)
(cid:32) (cid:18) (cid:19)(cid:33) (cid:18) (cid:19)1+(cid:15)
|     |     |        |     | √    |                               |     | log((1+(cid:15))t) |     | 2+(cid:15) | δ   |         |
| --- | --- | ------ | --- | ---- | ----------------------------- | --- | ------------------ | --- | ---------- | --- | ------- |
|     | P   | ∃t≥1:S |     | ≥(1+ | (cid:15)) 2σ2(1+(cid:15))tlog |     |                    |     | ≤1−        |     | . (134) |
t
|     |     |     |     |     |     |     | δ   |     | (cid:15) | log(1+(cid:15)) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- |
42

| 2,000 |     |     |     |     |     |     |     |     |     | Jamieson et al. (2013) |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
Balsubramani (2014)
Zhao et al. (2016)
Darling & Robbins (1967b)
Kaufmann et al. (2016)
| yradnuoB |     |     |     |     |     |     |     |     |     | Darling & Robbins (1968) |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
Polynomial stitching (ours)
Inverted stitching (ours)
Discrete mixture (ours)
0
|     | 0   |     |     |     |     |     |     |     | 105 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V
t
Figure 10: Finite LIL bounds for independent 1-sub-Gaussian observations, α = 0.025. The dotted lines show the
√
(cid:112)
Hoeffding bound 2V t logα−1, which is nonasymptotically pointwise valid, and the CLT bound z 1−α V t , which is
(k+1)1.4ζ(1.4).
asymptotically pointwise valid. Polynomial stitching uses Theorem 1 with η = 2.04 and h(k) =
(cid:112)
The inverted stitching boundary is 1.7 V (log(1+logV )+3.5), using Theorem 3 with η = 2.99, v = 1020,
|     |     |     |     |     | t   | t   |     |     |     |     |     | max |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and error rate 0.82α to account for finite horizon. Discrete mixture applies Theorem 2 to the density f(λ) =
0.4·1 /[λlog1.4(4e/λ)] with η = 1.1, and λ = 4; see Appendix A.6 for motivation. The normal mixture
| 0≤λ≤4      |      |          |              |     | max            |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| bound (53) | uses | ρ=0.129. | See Appendix |     | G for details. |     |     |     |     |     |     |     |     |
•
Zhao et al. (2016), Theorem 1: for sub-Gaussian observations with variance parameter 1/4,
|     |     |     | (cid:16) |     | (cid:112)   |     |         |     | (cid:17)        |     |     |     |       |
| --- | --- | --- | -------- | --- | ----------- | --- | ------- | --- | --------------- | --- | --- | --- | ----- |
|     |     |     | P ∃t≥1:S |     | ≥ atlog(log |     | t+1)+bt |     | ≤ζ(2a/c)e−2b/c. |     |     |     | (135) |
|     |     |     |          |     | t           |     | c       |     |                 |     |     |     |       |
• Kaufmannetal.(2016),Lemma7: forindependentsub-Gaussianobservationswithvarianceparameter
σ2,
√
|              | (cid:16) |         |                               |     |              | (cid:17) | √    | (cid:18) (cid:18) | 1 (cid:19)(cid:19)(cid:18) | x   | (cid:19)η |     |       |
| ------------ | -------- | ------- | ----------------------------- | --- | ------------ | -------- | ---- | ----------------- | -------------------------- | --- | --------- | --- | ----- |
|              | P        |         | (cid:112) 2σ2t(x+ηloglog(et)) |     |              |          |      |                   |                            |     |           | e−x |       |
|              |          | ∃t≥1:S  | t ≥                           |     |              |          | ≤ eζ | η                 | 1−                         | √   | +1        |     | (136) |
|              |          |         |                               |     |              |          |      |                   | 2x                         | 2 2 |           |     |       |
| •            |          |         |                               |     |              |          |      |                   | (cid:80)t c2,              |     |           |     |       |
| Balsubramani |          | (2014), | Theorem                       | 4:  | for |X t |≤c | t a.s.   | and  | V t =             |                            |     |           |     |       |
i=1 i
|     |     | (cid:18) |     |         | (cid:18) 2 (cid:19) |           |                |     |     |           | (cid:19) |     |       |
| --- | --- | -------- | --- | ------- | ------------------- | --------- | -------------- | --- | --- | --------- | -------- | --- | ----- |
|     |     | P        |     |         |                     | (cid:112) |                |     |     |           |          |     |       |
|     |     | ∃t≥1:V   |     | ≥173log |                     | :S ≥      | 3V (2loglog(3V |     | /2S | )+logα−1) | ≤α.      |     | (137) |
|     |     |          | t   |         | α                   | t         | t              |     | t t |           |          |     |       |
Though the bound is stated for bounded observations, the proof holds for any observations sub-
Gaussianwithvarianceparameters(c2),asnotedinsection5.2ofBalsubramani(2014). Balsubramani
t
suggests removing the initial time condition by imposing a constant bound over t ≤ 173log(2/α)
(section 5.3). We instead remove the condition by a change of units, as discussed in Appendix F.
•
Darling and Robbins (1967b), eq. 22: for i.i.d. observations sub-Gaussian with variance parameter 1,
|     | (cid:18) |     | 1+η(cid:112) |     |     |     |     |     | (cid:19) |     | 1   |     |     |
| --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
P ∃t≥ηj
|     |     | :S  | t ≥ √ | t(2cloglogt−2cloglogη+2loga) |     |     |     |     | ≤                |     |     | .   | (138) |
| --- | --- | --- | ----- | ---------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | ----- |
|     |     |     | 2     | η                            |     |     |     |     | a(c−1)(j−1/2)c−1 |     |     |     |       |
Darling and Robbins consider results for a general bound ϕ(λ) on the moment-generating function of
theobservations. Theresultinvolvesthetermh(v )wherethefunctionh(λ):=1/2+λ−2logϕ(λ)and
t
| v t | is unspecified | but | bounded. |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• DarlingandRobbins(1968), eq. 2.2andtheexamplethatfollows: fori.i.d.observationssub-Gaussian
| with | variance | parameter | 1,  |     |     |     |     |     |     |     |     |     |     |
| ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
√
(cid:16) (cid:17) (cid:90) ∞ A loglogt+C (cid:26) A2(loglogt+C) (cid:27)
|     | P      |     | (cid:112)       |     |     |     |     |     |       |     |     |     |       |
| --- | ------ | --- | --------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
|     | ∃t≥3:S |     | ≥A t(loglogt+C) |     | ≤   |     |     |     | exp − |     |     | dt. | (139) |
|     |        | t   |                 |     |     |     | t   |     |       |     | 2   |     |       |
m
43

DarlingandRobbinsgiveaclosed-formupperboundfortheright-handsideof (139). Weinsteadeval-
uate it numerically, using readily-available implementations of the upper incomplete gamma function:
√
(cid:90) ∞ A loglogt+C (cid:26) A2(loglogt+C) (cid:27)
exp − dt
t 2
m √
2πAe−C (cid:18) A2−2 (cid:19)
= P G≥ (loglogm+C) , (140)
(A−2)3/2 2
where G∼Γ(3/2,1).
• Polynomial stitching as in (10) with c=0.
• Inverted stitching with g(v) = A (cid:112) v(loglog(ev)+C) as in (20). We set v = 1020 which covers
max
42 epochs with η = 2.994. To make for a fair comparison with polynomial stitching, observe that
in 42 epochs with s = 1.4, polynomial stitching “spends” (cid:80)42 k−1.4/ζ(1.4) ≈ 0.820 of its crossing
k=1
probability α, so we run inverted stitching with α=0.820·0.025.
• Normal mixture as in (53) with ρ≈0.13:
(cid:115)
(cid:18) (cid:114) (cid:19)
v
u(v)≈ 2(v+0.13)log 20 1+ +1 . (141)
0.13
This is not a LIL boundary, so is not included in Table 2.
Source and parameter settings A B C
Jamieson and Nowak (2014) (1+ √ (cid:15)) (cid:112) 2(1+(cid:15)) 1+(cid:15) 1 log (cid:16) 2+(cid:15) (cid:17)
1+(cid:15) α(cid:15)log1+(cid:15)(1+(cid:15))
(cid:15)=0.033 (1.7) (1.033) (10.966)
√
Balsubramani (2014) 6 865log (cid:0)2(cid:1) (logα−1)/2
2 δ
(2.45) (1137) (1.844)
√ (cid:16) (cid:17)
Zhao et al. (2016) 2 a c c log ζ(2a/c)
2a αlog2a/cc
a=0.7225,c=1.1 (1.7) (1.1) (6.173)
(cid:113) (cid:16) (cid:17)
Darling and Robbins (1967b) (1+η) c ηj 1log 1
2η c α(c−1)(j−1/2)c−1logcη
j =1,c=1.4,η =1.429 (1.7) (1.429) (4.518)
√
Kaufmann et al. (2016) 2η e x(α,η)/η
η =1.3 (1.7) (2.718) (4.427)
Darling and Robbins (1968) A 3 C(α,A)
A=1.7 (1.7) (3) (3.945)
Polynomial stitching (10) (η1/4+η−1/4) (cid:112)s η 1log ζ(s)
2 s αlogsη
s=1.4,η =2.041 (1.7) (2.041) (3.782)
Inverted stitching (Theorem 3) A e C(α,A,η)
η =2.994, nominal error rate 0.82α (1.7) (2.718) (3.454)
Table 2: Comparison of parameters A,B,C for finite LIL boundaries expressed in the form
P(∃t≥1:S ≥A (cid:112) t(loglogBt+C))≤α for sums of independent 1-sub-Gaussian observations, with α = 0.025.
t
Functions x(α,η) and C(α,...) are given by numerical root-finding to set the corresponding error bound equal to
α.
44

| H   | Details |     | of  | Example |     | 1   |     |     |     |     |     |     |
| --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Write X =µ+σZ for t=1,2,... where Z ,Z ,... are i.i.d. N(0,1) random variables. Substituting into
|     | t          |     | t      |      |     |     | 1 2 |     |     |     |     |     |
| --- | ---------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| the | definition | of  | S , we | find |     |     |     |     |     |     |     |     |
t
t+1
|     |     |     |     |     |     |     | (cid:88)(cid:0) | −Z¯   | (cid:1)2 |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | -------- | --- | --- | ----- |
|     |     |     |     |     |     | S   | =               | Z     | −t,      |     |     | (142) |
|     |     |     |     |     |     | t   |                 | i t+1 |          |     |     |       |
i=1
|     | Z¯  | :=t−1(cid:80)t |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where Z . Evidently the distribution of S depends on neither µ nor σ2. Furthermore, direct
|             | t   |       | i=1  | i   |            |       |       | t          |     |     |     |     |
| ----------- | --- | ----- | ---- | --- | ---------- | ----- | ----- | ---------- | --- | --- | --- | --- |
| calculation |     | shows | that | the | increments | of (S | ) may | be written | as  |     |     |     |
t
t
|     |     |     |     |     |     |       |     |         | (cid:0) −Z¯ | (cid:1)2 |     |       |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------- | ----------- | -------- | --- | ----- |
|     |     |     |     |     | ∆S  | =S −S |     | =       | Z           | −1       |     | (143) |
|     |     |     |     |     |     | t t   | t−1 | t+1     | t+1         | t        |     |       |
|     |     |     |     |     |     |       |     | =:Y2−1, |             |          |     | (144) |
t
(cid:112)
where we define Y := t/(t+1)(Z −Z¯ ) for t = 1,2,... (and take S = 0 by convention). Noting
|     |     |     | t   |     |     | t+1 | t   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that Z ∼ N(0,1) is independent of Z¯ ∼ N(0,t−1), we see that Y ∼ N(0,1) for each t. Finally, a
|     | t+1 |     |     |     |     | t   |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EY
straightforward calculation shows that Y = 0 for all i (cid:54)= j, so that Y ,Y ,... are i.i.d. It follows that
|     |     |     |     |     |     | i   | j   |     |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∆S ,∆S ,... are i.i.d. centered Chi-squared random variables each with one degree of freedom. The CGF
1 2
| of  | this distribution |     | is  |     |           |     |           |     |     |        |     |       |
| --- | ----------------- | --- | --- | --- | --------- | --- | --------- | --- | --- | ------ | --- | ----- |
|     |                   |     |     |     |           |     | log(1−2λ) |     |     |        | 1   |       |
|     |                   |     |     |     | logEeλ∆S1 | =−  |           | −λ, | for | all λ< | .   | (145) |
|     |                   |     |     |     |           |     |           | 2   |     |        | 2   |       |
which is equal to 2ψ (λ) with scale c=2. As the increments of (S ) are i.i.d., it suffices for Definition 1 to
|     |     |     | E   |     |     |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
logEeλ∆St
| have |     |     | ≤ψ(λ)∆V |     | , and we | have shown | this | holds | with equality. |     |     |     |
| ---- | --- | --- | ------- | --- | -------- | ---------- | ---- | ----- | -------------- | --- | --- | --- |
t
We have shown that (S ) is sub-exponential with scale c = 2 and variance process V = 2t. Recall that
t t
Definition 1 depends only on λ ≥ 0. However, since (145) holds for all λ < 1/2 and not just 0 ≤ λ < 1/2,
replacing ∆S with −∆S shows that (−S ) is sub-exponential with scale c=−2.
|     |           | t   |     | t   |        | t      |     |        |     |     |                 |      |
| --- | --------- | --- | --- | --- | ------ | ------ | --- | ------ | --- | --- | --------------- | ---- |
| I   | Extension |     |     | to  | smooth | Banach |     | spaces | and |     | continuous-time | pro- |
cesses
Though we have focused on discrete-time processes taking values in R or Sd, our uniform boundaries also
apply to discrete-time martingales in general smooth Banach spaces and to real-valued, continuous-time
martingales. InthissectionwebrieflyreviewconceptsfromHowardetal.(2020,Sections3.4-3.5)tohighlight
the possibilities. First, let (Y t ) t∈N be a martingale taking values in a separate Banach space (X,(cid:107)·(cid:107)). Our
uniform boundaries apply to any function Ψ:X →R satisfying the following property:
Definition 4 ((Pinelis, 1994)). A function Ψ : X → R is called (2,D)-smooth for some D > 0 if, for all
x,v ∈X,wehave(a)Ψ(0)=0,(b)|Ψ(x+v)−Ψ(x)|≤(cid:107)v(cid:107),and(c)Ψ2(x+v)−2Ψ2(x)+Ψ2(x−v)≤2D2(cid:107)v(cid:107)2.
For example, the norm induced by the inner product in any Hilbert space is (2,1)-smooth, and the Schatten
√
| p-norm | is  | (2, | p−1)-smooth |     | for p≥2. |     |     |     |     |     |     |     |
| ------ | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Corollary 7. Let(Y ) beamartingaletakingvaluesinaseparableBanachspace(X,(cid:107)·(cid:107)), andΨ:X →R
t t∈N
:=1∨D.
| is  | (2,D)-smooth; |     | denote | D   | (cid:63) |     |     |     |     |     |     |     |
| --- | ------------- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(a) Suppose (cid:107)∆Y (cid:107)≤c a.s. for all t for constants (c ). Then, for any sub-Gaussian boundary f with
|     |          |             | t   | t   |       |             |     | t   |     |     |     |     |
| --- | -------- | ----------- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
|     | crossing | probability |     | α   | and l | =2, we have |     |     |     |     |     |     |
0
|     |     |     |     |     |     | (cid:32) |     |     | (cid:32) | (cid:33)(cid:33) |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- | ---------------- | --- | --- |
t
(cid:88)
|     |     |     |     |     |     | P ∃t≥1:Ψ(Y |     | )≥f | D2       | c2  | ≤α. | (146) |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | -------- | --- | --- | ----- |
|     |     |     |     |     |     |            |     | t   | (cid:63) | i   |     |       |
i=1
(b) Suppose (cid:107)∆Y (cid:107) ≤ c a.s. for all t for c>0. Then, for any sub-Poisson boundary f with crossing
t
|     | probability |     | α, l | 0 =2, | and scale | c, we have |     |          |     |     |                  |     |
| --- | ----------- | --- | ---- | ----- | --------- | ---------- | --- | -------- | --- | --- | ---------------- | --- |
|     |             |     |      |       | (cid:32)  |            |     | (cid:32) | t   |     | (cid:33)(cid:33) |     |
(cid:88)
|     |     |     |     |     | P   | ∃t≥1:Ψ(Y | )≥f | D2       | E   | (cid:107)X (cid:107)2 | ≤α. | (147) |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --------------------- | --- | ----- |
|     |     |     |     |     |     |          | t   | (cid:63) | i−1 | i                     |     |       |
i=1
45

TheresultfollowsdirectlyfromtheproofofCorollary10inHowardetal.(2020),whichshowsthatS =Ψ(Y )
t t
is sub-Gaussian or sub-Poisson with appropriate variance process (V ) for each case, building upon the work
t
of Pinelis (1992, 1994). For example, let (Y ) be a martingale taking values in any Hilbert space, with (cid:107)·(cid:107)
t
the induced norm, and suppose (cid:107)∆Y t (cid:107)≤1 a.s. for all t. Then Corollary 7(a) with a normal mixture bound
yields
|     |     |     | (cid:32) |     | (cid:115) | (cid:18) | (cid:19)(cid:33) |     |     |
| --- | --- | --- | -------- | --- | --------- | -------- | ---------------- | --- | --- |
4(t+ρ)
|     |     |     | P ∃t≥1:(cid:107)Y |     | (cid:107)≥ (t+ρ)log |     | ≤α. |     | (148) |
| --- | --- | --- | ----------------- | --- | ------------------- | --- | --- | --- | ----- |
t
α2ρ
Next, let (S ) t∈R be a continuous-time, real-valued process. Replacing discrete-time processes in Defini-
t ≥0
tion 1 with continuous-time processes, and invoking the continuous-time version of Ville’s inequality, our
stitched, mixture and inverted stitching results extend straightforwardly to continuous time. Below we give
two examples which follow from Fact 2 of Howard et al. (2020). Here (cid:104)S(cid:105) denotes the predictable quadratic
t
| variation | of (S ). |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
t
| Corollary | 8. Let | (S ) | be a real-valued |     | process. |     |     |     |     |
| --------- | ------ | ---- | ---------------- | --- | -------- | --- | --- | --- | --- |
t t∈R
≥0
(a) If (S ) is a locally square-integrable martingale with a.s. continuous paths, and f is a sub-Gaussian
t
P(∃t∈(0,∞):S
stitched, mixture or inverted stitching uniform boundary, then ≥f((cid:104)S(cid:105) ))≤e−2ab.
|     |     |     |     |     |     |     |     | t t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b) If (S ) is a local martingale with ∆S ≤ c for all t, and f is a sub-Poisson mixture bound for scale c
|     | t   |     |     | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
or a sub-gamma stitched bound for scale c/3, then P(∃t∈(0,∞):S ≥f((cid:104)S(cid:105) ))≤α.
t t
Forexample,if(S )isastandardBrownianmotion,thenCorollary8(a)withapolynomialstitchedboundary
t
| yields, for | any η >1,s>1, |            |            |     |                    |                     |        |                  |     |
| ----------- | ------------- | ---------- | ---------- | --- | ------------------ | ------------------- | ------ | ---------------- | --- |
|             | (cid:32)      |            |            |     | (cid:115) (cid:18) |                     |        | (cid:19)(cid:33) |     |
|             |               |            | η1/4+η−1/4 |     |                    |                     | ζ(s)   |                  |     |
|             | P             | ∃t∈(0,∞):S | ≥          | √   | (1∨t)              | sloglog(η(1∨t))+log |        | ≤α.              |     |
|             |               |            | t          |     |                    |                     | αlogsη |                  |     |
2
| J Sufficient |     | conditions |     | for | Definition | 1   |     |     |     |
| ------------ | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- |
Table 3 offers a summary of sufficient conditions for Definition 1 to hold when (S t ) is a scalar process, while
Table 4 gives conditions for matrix-valued processes. See Howard et al. (2020, Section 2) for details.
46

|     |     |     |     | Condition | on S t |     | ψ   | V   | t   |     |
| --- | --- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- |
(cid:80)t
|     | Discrete  | time, S | =     | X , one-sided |        |     |     |           |       |     |
| --- | --------- | ------- | ----- | ------------- | ------ | --- | --- | --------- | ----- | --- |
|     |           |         | t i=1 | i             |        |     |     |           |       |     |
|     | Bernoulli | II      |       | X ≤h,E        | X2 ≤gh |     | ψ   | ght       |       |     |
|     |           |         |       | t             | t−1 t  |     | B   |           |       |     |
|     |           |         |       |               |        |     |     | (cid:80)t | E X2  |     |
|     | Bennett   |         |       | X t ≤c        |        |     | ψ P |           | i−1   |     |
|     |           |         |       |               |        |     |     |           | i=1 i |     |
(cid:80)t
|     | Bernstein |         |     | E (X   | )k ≤ k!ck−2E | X2  | ψ   |           | E X2      |     |
| --- | --------- | ------- | --- | ------ | ------------ | --- | --- | --------- | --------- | --- |
|     |           |         |     | t−1 t  | 2 t−1        | t   | G   |           | i=1 i−1 i |     |
|     | ∗Heavy    | on left |     | E T (X | )≤0 for all  | a>0 | ψ   | (cid:80)t | X2        |     |
|     |           |         |     | t−1 a  | t            |     | N   |           | i=1 i     |     |
(cid:80)t X2
|     | Bounded | below |     | X ≥−c |     |     | ψ   |     |       |     |
| --- | ------- | ----- | --- | ----- | --- | --- | --- | --- | ----- | --- |
|     |         |       |     | t     |     |     | E   |     | i=1 i |     |
(cid:80)t
|     | Discrete   | time, S | =     | X , two-sided |     |     |          |     |     |     |
| --- | ---------- | ------- | ----- | ------------- | --- | --- | -------- | --- | --- | --- |
|     |            |         | t i=1 | i             |     |     |          |     |     |     |
|     | Parametric |         |       | X i ∼ id F    |     |     | logEeλX1 | t   |     |     |
t
|     | Bernoulli | I   |     | −g ≤X | ≤h  |     | ψ   | ght |     |     |
| --- | --------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |           |     |     |       | t   |     | B   |     |     |     |
(cid:80)t
|     | Hoeffding-KS |     |     | −g ≤X | ≤h  |     | ψ   |     | ϕ(g ,h             | )   |
| --- | ------------ | --- | --- | ----- | --- | --- | --- | --- | ------------------ | --- |
|     |              |     |     | t     | t t |     | N   |     | i=1 i i            |     |
|     |              |     |     |       |     |     |     |     | (cid:16) (cid:17)2 |     |
(cid:80)t gi+hi
|     | Hoeffding  | I   |     | −g ≤X | ≤h    |     | ψ   |           |       |     |
| --- | ---------- | --- | --- | ----- | ----- | --- | --- | --------- | ----- | --- |
|     |            |     |     | t     | t t   |     | N   |           | i=1 2 |     |
|     | ∗Symmetric |     |     | X ∼−X | |F    |     | ψ   | (cid:80)t | X2    |     |
|     |            |     |     | t     | t t−1 |     | N   |           | i     |     |
i=1
|     |                 |     |     | E     |     |     |     | 1(cid:80)t | (cid:0) X2+2E | X2(cid:1) |
| --- | --------------- | --- | --- | ----- | --- | --- | --- | ---------- | ------------- | --------- |
|     | Self-normalized |     | I   | X2    | <∞  |     | ψ   |            |               |           |
|     |                 |     |     | t−1 t |     |     | N   | 3          | i=1 i         | i−1 i     |
|     |                 |     |     |       |     |     |     | 1(cid:80)t | (cid:0)       | )2(cid:1) |
|     | Self-normalized |     | II  | E X2  | <∞  |     | ψ   |            | (X )2         | +E (X     |
|     |                 |     |     | t−1 t |     |     | N   | 2          | i=1 i         | + i−1 i − |
Cubic self-normalized E |X |3 <∞ ψ (cid:80)t (cid:0) X2+E |X |3(cid:1)
|     |     |     |     | t−1 t |     |     | G   |     | i   | i−1 i |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- |
i=1
|     | Continuous | time, | one-sided |       |     |     |     |                     |     |     |
| --- | ---------- | ----- | --------- | ----- | --- | --- | --- | ------------------- | --- | --- |
|     | Bennett    |       |           | ∆S ≤c |     |     | ψ   | (cid:104)S(cid:105) |     |     |
|     |            |       |           | t     |     |     | P   |                     | t   |     |
m!cm−2V
|     | Bernstein |     |     | W m,t ≤ | t   |     | ψ G | V   | t   |     |
| --- | --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
2
|     | Continuous | time, | two-sided |          |     |     |          |                     |     |     |
| --- | ---------- | ----- | --------- | -------- | --- | --- | -------- | ------------------- | --- | --- |
|     | L´evy      |       |           | EeλS1 <∞ |     |     | logEeλS1 | t                   |     |     |
|     | Continuous |       | paths     | ∆S t ≡0  |     |     | ψ N      | (cid:104)S(cid:105) |     |     |
t
Table 3: Summary of sufficient conditions a real-valued, discrete- or continuous-time process (S t ) to be sub-ψ with
the given variance process. We assume (S ) is a martingale in every case except the starred ones (∗), when the first
t
moment E|X | need not exist. See Howard et al. (2020, Section 2) for details. One-sided conditions yield a bound
t
on right-tail deviations only, while two-sided conditions yield bounds on both tails. For continuous-time cases, ∆S
t
denotes the jumps of (S t ) and (cid:104)S(cid:105) denotes the predictable quadratic variation. For the heavy on left case, the
t
truncation function is defined as T a (y):=(y∧a)∨−a for a>0 (Bercu and Touati, 2008). The function ϕ used in
the Hoeffding-KS case is defined in (97). The process W in the continuous-time Bernstein case is defined in Fact
m,t
| 2(c) | of Howard | et al. | (2020) | (cf. van de Geer | (1995)). |     |     |     |     |     |
| ---- | --------- | ------ | ------ | ---------------- | -------- | --- | --- | --- | --- | --- |
47

(cid:80)t
|     |     |     |     | Condition | on  | Y = | X   | ψ   | Z   |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |           |     | t   | i=1 | t   |     | t   |     |     |
One-sided
,E X2
|     | Bernoulli | II  |     | X t (cid:22)hI | d   | t−1 (cid:22)ghI | d   | ψ   | B ghtI | d   |     |     |
| --- | --------- | --- | --- | -------------- | --- | --------------- | --- | --- | ------ | --- | --- | --- |
t
(cid:80)t
|     | Bennett   |       |     | X (cid:22)cI    |                |         |     | ψ   |           | E X2      |     |     |
| --- | --------- | ----- | --- | --------------- | -------------- | ------- | --- | --- | --------- | --------- | --- | --- |
|     |           |       |     | t               | d              |         |     |     | P         | i=1 i−1 i |     |     |
|     | Bernstein |       |     | E               | (X )k (cid:22) | k!ck−2E | X2  | ψ   | (cid:80)t | E X2      |     |     |
|     |           |       |     | t−1             | t              | 2       | t−1 | t   | G         | i=1 i−1 i |     |     |
|     |           |       |     |                 |                |         |     |     | (cid:80)t | X2        |     |     |
|     | Bounded   | below |     | X t (cid:23)−cI | d              |         |     | ψ   | E         |           |     |     |
|     |           |       |     |                 |                |         |     |     |           | i=1 i     |     |     |
Two-sided
|     | Bernoulli | I   |     | −gI | (cid:22)X (cid:22)hI |     |     | ψ   | ghtI |     |     |     |
| --- | --------- | --- | --- | --- | -------------------- | --- | --- | --- | ---- | --- | --- | --- |
|     |           |     |     | d   | t                    | d   |     |     | B    | d   |     |     |
(cid:80)t
Hoeffding-KS −G t I d (cid:22)X t (cid:22)H t I d ψ N ϕ(G i ,H i )I d
i=1
|     |           |     |     |               |           |             |     |     | (cid:80)t | (cid:0)Gi+ | (cid:1)2 |     |
| --- | --------- | --- | --- | ------------- | --------- | ----------- | --- | --- | --------- | ---------- | -------- | --- |
|     | Hoeffding | I   |     | −G I          | (cid:22)X | (cid:22)H I |     | ψ   |           | Hi         | I        |     |
|     |           |     |     | t             | d t       | t d         |     |     | N         | i=1 2      | d        |     |
|     | Hoeffding | II  |     | X2 (cid:22)A2 |           |             |     | ψ   | (cid:80)t | A2         |          |     |
|     |           |     |     | t             | t         |             |     |     | N         | i=1 i      |          |     |
(cid:80)t
|     | ∗Symmetric      |     |     | X ∼−X | |F    |     |     | ψ   |            | X2      |     |           |
| --- | --------------- | --- | --- | ----- | ----- | --- | --- | --- | ---------- | ------- | --- | --------- |
|     |                 |     |     | t     | t     | t−1 |     |     | N          | i=1 i   |     |           |
|     |                 |     |     |       |       |     |     |     | 1(cid:80)t | (cid:0) |     | X2(cid:1) |
|     | Self-normalized |     | I   | E     | X2 <∞ |     |     | ψ   |            | X2+2E   |     |           |
|     |                 |     |     | t−1   | t     |     |     |     | N 3        | i=1 i   | i−1 | i         |
Self-normalized II E X2 <∞ ψ 1(cid:80)t (cid:0) (X )2 +E (X )2(cid:1)
|     |       |                 |     | t−1 | t        |     |     |     | N         | i            | + i−1 | i −       |
| --- | ----- | --------------- | --- | --- | -------- | --- | --- | --- | --------- | ------------ | ----- | --------- |
|     |       |                 |     |     |          |     |     |     | 2         | i=1          |       |           |
|     |       |                 |     | E   |          |     |     |     | (cid:80)t | (cid:0) X2+E |       | |3(cid:1) |
|     | Cubic | self-normalized |     |     | |X |3 <∞ |     |     | ψ   |           |              | |X    |           |
|     |       |                 |     | t−1 | t        |     |     |     | G         | i=1 i        | i−1 i |           |
(cid:80)t
Table4: SummaryofsufficientconditionsforDefinition1whenY = X withX ∈Hd,thespaceofHermitian,
|     |     |     |     |     |     |     |     | t   | i=1 | i t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d×dmatrices,takingS =γ (Y )andV =γ (Z ). WeassumeEX =0andhence(Y )isamartingaleinevery
|     |     |     | t   | max t | t   | max t |     |     | t   |     | t   |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
caseexceptthesymmetric∗ case,whenthefirstmomentE|X |neednotexist. SeeHowardetal.(2020,Section2)for
t
details. One-sidedconditionsyieldaboundonright-taildeviationsonly,whiletwo-sidedconditionsyieldsboundson
| both | tails. | The function | ϕ used | in the | Hoeffding-KS | case | is defined |     | in (97). |     |     |     |
| ---- | ------ | ------------ | ------ | ------ | ------------ | ---- | ---------- | --- | -------- | --- | --- | --- |
48