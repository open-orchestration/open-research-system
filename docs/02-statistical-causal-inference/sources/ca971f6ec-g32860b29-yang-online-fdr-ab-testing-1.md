A framework for Multi-A(rmed)/B(andit) testing
with online FDR control
Fanny Yang(cid:63) Aaditya Ramdas†,(cid:63) Kevin Jamieson(cid:63) Martin J. Wainwright†,(cid:63)
Department of Statistics†, and
Department of Electrical Engineering and Computer Sciences(cid:63)
UC Berkeley, Berkeley, CA 94720
Abstract
We propose an alternative framework to existing setups for controlling false alarms
when multiple A/B tests are run over time. This setup arises in many practical appli-
cations, e.g. when pharmaceutical companies test new treatment options against control
pills for different diseases, or when internet companies test their default webpages versus
variousalternativesovertime. OurframeworkproposestoreplaceasequenceofA/Btests
by a sequence of best-arm MAB instances, which can be continuously monitored by the
data scientist. When interleaving the MAB tests with an an online false discovery rate
(FDR) algorithm, we can obtain the best of both worlds: low sample complexity and any
time online FDR control. Our main contributions are: (i) to propose reasonable defini-
tions of a null hypothesis for MAB instances; (ii) to demonstrate how one can derive an
always-valid sequential p-value that allows continuous monitoring of each MAB test; and
(iii) to show that using rejection thresholds of online-FDR algorithms as the confidence
levelsfortheMABalgorithmsresultsinbothsample-optimality,highpowerandlowFDR
at any point in time. We run extensive simulations to verify our claims, and also report
results on real data collected from the New Yorker Cartoon Caption contest.
1 Introduction
For most modern internet companies, wherever there is a metric that can be measured (e.g.,
time spent on a page, click-through rates, conversion of curiousity to a sale), there is almost
alwaysarandomizedtrialbehindthescenes,withthegoalofidentifyinganalternativewebsite
design that provides improvements over the default design. The use of such data-driven
decisions for perpetual improvement is colloquially known as A/B testing in the case of two
alternatives, or A/B/n testing for several alternatives. Given a default configuration and
several alternatives (e.g., color schemes of a website), the standard practice is to divert a
small amount of scientist-traffic to a randomized trial over these alternatives and record the
desired metric for each of them. If an alternative appears to be significantly better, it is
implemented; otherwise, the default setting is maintained.
Atfirstglance,thisprocedureseemsintuitiveandsimple. However,incaseswheretheaim
is to optimize over one particular metric, this common tool suffers from several downsides.
(1) First, whereas some alternatives may be clearly worse than the default, others may only
have a slight edge. If one wishes to minimize the amount of time and resources spent on
this randomized trial the more promising alternatives should intuitively get a larger share of
the traffic than the clearly-worse alternatives. Yet typical A/B/n testing frameworks allocate
trafficuniformlyoveralternatives. (2)Second,companiesoftendesiretocontinuouslymonitor
anongoingA/Btestastheymayadjusttheirterminationcriteriaastimegoesbyandpossibly
stop earlier or later than originally intended. However, just as if you flip a coin long enough,
a long string of heads is eventually inevitable, the practice of continuous monitoring (without
1
7102
voN
81
]LM.tats[
2v87350.6071:viXra

mathematicallycorrectingforit)caneasilyfoolthetestertobelievethataresultisstatistically
significant, when in reality it is not. This is one of the reasons for the lack of reproducibility
of scientific results, an issue recently receiving increased attention from the public media.
(3) Third, the lack of sufficient evidence or an insignificant improvement of the metric may
make it undesirable from a practical or financial perspective to replace the default. Therefore,
whenacompanyrunshundredstothousandsofA/Btestswithinayear,ideallythenumberof
statistically insignificant changes that it made should be small compared to the total number
of changes made. Controlling the false alarm rate of each individual test at a desired level α
however does not achieve this type of control, also known as controlling the false discovery
rate. Of course, it is also desirable to detect better alternatives (when they exist), and to do
so as quickly as possible.
In this paper, we provide a novel framework that addresses the above shortcomings of
A/B or A/B/n testing. The first concern is tackled by employing recent advances in adaptive
sampling like the pure-exploration multi-armed bandit (MAB) algorithm. For the second
concern, we adopt the notion of any-time p-values for guilt-free continuous monitoring, and
we make the advantages and risks of early-stopping transparent. Finally, we handle the third
issue using recent advances in online false discovery rate (FDR) control. Hence the combined
framework can be described as doubly-sequential (sequences of MAB tests, each of which is
itself sequential). Although each of those problems has been studied in hitherto disparate
communities, how to leverage the best of all worlds, if at all possible, has remained an open
problem. The main contributions of this paper are in merging these ideas in a combined
framework and presenting the conditions under which it can be shown to yield near-optimal
sample complexity, near-optimal best-alternative discovery rate, as well as FDR control.
While the above concerns raised about A/B/n testing were discussed using the example of
modern internet companies, the same concerns carry forward qualitatively to other domains,
like pharmaceutical companies running sequential clinical trials with a control (often placebo)
and a few treatments (like different doses or drug substances). In a manufacturing or food
production setting, one may be interested in identifying (perhaps cheaper) substitutes for in-
dividual materials without compromising the quality of a product too much. In a government
setting, pilot programs are funded in search of improvements over current programs and it is
desirablefromasocialwelfarestandpointandcosttolimittheadoptionofineffectivepolicies.
The remainder of this paper is organized as follows. In Section 2, we lay out the primary
goals of the paper, and describe a meta-algorithm that combines adaptive sampling strategies
with FDR control procedures. Section 3 is devoted to the description of a concrete procedure,
along with some theoretical guarantees on its properties. In Section 4, we describe the results
of our extensive experiments on both simulated and real-world data sets that are available to
us, before we conclude with a discussion in Section 6.
2 Formal experimental setup and a meta-algorithm
In this section we first formalize the setup of a typical A/B/n test and provide a high-
level overview of our proposed combined framework aimed at addressing the shortcomings
mentioned in the introduction. A specific instantiation of this meta-algorithm along with
detailed theoretical guarantees are specified in Section 3.
For concreteness, we refer to the system designer, whether a tech company or a phar-
maceutical company, as a (data) scientist. We assume that the scientist needs to possibly
conduct an infinite number of experiments sequentially, indexed by j. Each experiment has
one default setting, referred to as the control, and K = K(j) alternative settings, called the
2

treatments or alternatives. The scientist must return one of the K +1 options that is the
“best” according to some predefined metric, before the next experiment is started. Such a
setup is a simple mathematical model both for clinical trials run by pharmaceutical labs, and
A/B/n testing used at scale by tech companies.
One full experiment consists of steps of the following kind: In each step, the scientist
assigns a new person—who arrives at the website or who enrolls in the clinical trial—to one
of the K +1 options and obtains a measurable outcome. In practice, the role of the scientist
could be taken by an adaptive algorithm, which determines the assignment at time step j by
careful consideration of all previous outcomes. Borrowing terminology from the multi-armed
bandit(MAB)literature, werefertoeachoftheK+1optionsasanarm, andeachassignment
to arm i is termed “pulling arm i”. For concreteness, we assign the index 0 to the default or
control arm, and note that this index is known to the algorithm.
Weassumethattheobservablemetricfromeachpullofarmi = 0,1,...,K correspondsto
an independent draw from an unknown probability distribution with expectation µ . Ideally,
i
if the means were known, we would use them as scores to compare the arms where higher is
better. In the sequel we use µ := max µ to denote the mean of the best arm. We refer
i(cid:63) i
i=1,...,K
the reader to Table 1 for a glossary of the notation used throughout this paper.
2.1 Some desiderata and difficulties
Giventhesetupabove,howcanwemathematicallydescribetheguaranteesthatthecompanies
mightdesirefromanimprovedmultiple-A/B/ntestingframework? Whichpartsofthepuzzle
can be directly transferred from known results, and what challenges remain?
In order to answer the first question, let us adopt terminology from the hypothesis testing
literature and view each experiment as a test of a null hypothesis. Any claim that an alter-
native arm is the best is called a discovery, and if such a claim is erroneous then it is called
a false discovery. When multiple hypotheses need to be tested, the scientist needs to define
the quantity it wants to control. While we may desire that the probability of even a single
false discovery—called the family-wise error rate—is small, this is usually far too stringent
for a large and unknown number of tests. For this reason, [1] proposed that it may be more
interesting to control the expected ratio of false discoveries to the total number of discoveries
(called the False Discovery Rate, or FDR for short) or ratio of expected number of false dis-
coveries to the expected number of total discoveries (called the modified FDR or mFDR for
short). Over the past decades, the FDR and its variants like mFDR have become standard
quantities for multiple testing applications. In the following, if not otherwise specified, we use
the term FDR to denote both measures in order to simplify the presentation. In Section 3,
we show that both mFDR and FDR can be controlled for different choices of procedures.
2.1.1 Challenges in viewing an MAB instance as a hypothesis test
In our setup, we want to be able to control the FDR at any time in an online manner. Online
FDR procedures were first introduced by Foster and Stine [2], and have since been studied
by other authors (e.g., [3, 4]). A typical online FDR procedure is based on comparing a
valid p-value Pj with carefully-chosen levels α for each hypothesis test1. We reject the null
j
hypothesis, represented as R = 1, when Pj α and we set R = 0 otherwise.
j j j
≤
As mentioned, we want to use adaptive MAB algorithms in each experiment to test each
hypothesis, since they can find a best arm among K+1 with near-optimal sample complexity.
1AvalidPj mustbestochasticallydominatedbyauniformdistributionon[0,1],whichwehenceforthrefer
to as super-uniformly distributed.
3

However the traditional MAB setup does not account for the asymmetry between the arms as
isthecaseinatestingsetup,withonebeingthedefault(control)andothersbeingalternatives
(treatments). This is the standard scenario in A/B/n testing applications, as for example a
company might prefer wrong claims that the control is the best (false negative), rather than
wrong claims that an alternative is the best (false positive), simply because new system-wide
adoption of selected alternatives might involve high costs. What would be a suitable null
hypothesis in this hybrid setting? To allow continuous monitoring, is it possible to define and
compute always-valid p-values that are super-uniformly distributed under the null hypothesis
when computed at any time t? (This could be especially challenging given that the number
| of samples | from | each | the arm | is random, | and | different |     | for each arm.) |     |
| ---------- | ---- | ---- | ------- | ---------- | --- | --------- | --- | -------------- | --- |
In addition to asymmetry, the practical scientist might have a different incentive than the
ideal outcome for MAB algorithms. In particular, he/she might not want to find the best
alternative if it is not substantially better than the control. Indeed, if the net gain made by
adopting a new alternative is small, it might be offset by the cost of implementing the change
from the existing default choice. By similar reasoning, we may not require identifying the
single best arm if there is a set of arms with similar means that are all larger than the rest.
We propose a sensible null-hypothesis for each experiment which incorporates the approx-
imation and improvement notions as described above and provide an always valid p-value
which can be easily calculated at each time step in the experiment. We show that a slight
modification of the usual LUCB algorithm caters to this specific null-hypothesis while still
| maintaining |             | near-optimal | sample  |     | complexity. |     |     |     |     |
| ----------- | ----------- | ------------ | ------- | --- | ----------- | --- | --- | --- | --- |
| 2.1.2       | Interaction |              | between | MAB | and         | FDR |     |     |     |
In order to take advantage of the sample efficiency of best-arm bandit algorithms, it is crucial
to set the confidence levels close to what is needed. Given a user-defined level α, at each
hypothesis j, online FDR procedures automatically output the significance level α j which are
| “needed” | to  | guarantee | FDR | control, | based | on past | decisions. |     |     |
| -------- | --- | --------- | --- | -------- | ----- | ------- | ---------- | --- | --- |
desired FDR level
𝛼𝛼
Online FDR procedure
|     |     |      |     |             | )    |     |     |               | )   |
| --- | --- | ---- | --- | ----------- | ---- | --- | --- | ------------- | --- |
|     |     |      |     |             |      |     | j+1 | j+1 j+1       |     |
|     | …   |      |     |             |      |     |     |               | …   |
|     |     | 𝛼𝛼𝑗𝑗 | Exp | j 𝑅𝑅𝑗𝑗(𝛼𝛼𝑗𝑗 |      |     | 𝛼𝛼  | Exp j+𝑅𝑅1 (𝛼𝛼 |     |
|     |     |      |     |             | Test |     |     | Test          |     |
|     |     | MAB  |     |             |      |     | MAB | j+1  j+1      |     |
𝑝𝑝𝑗𝑗(𝛼𝛼𝑗𝑗)
|     |     |     |     |     |            |     |     | 𝑝𝑝 (𝛼𝛼 ) j+1  | j+1             |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ------------- | --------------- |
|     |     |     |     |     | 𝑝𝑝𝑗𝑗 <𝛼𝛼𝑗𝑗 |     |     | 𝑝𝑝 < 𝛼𝛼       |                 |
|     |     |     |     |     |            |     |     | MA B-F DR     |  meta algorithm |
Figure 1. Diagram of the MAB-FDR meta algorithm designed to achieve online FDR control
along with near-optimal sample complexity. The green arrows symbolize interaction between
theMABandFDRproceduresviatheFDRtestlevelsα j andrejectionindicatorvariablesR j .
Notice that the Pj-values are now dependent as each α depends on R ,...,R . The eyes
|           |     |          |            |            |     |     |            | j 1 | j 1 |
| --------- | --- | -------- | ---------- | ---------- | --- | --- | ---------- | --- | --- |
| represent |     | possible | continuous | monitoring | by  | the | scientist. |     | −   |
4

Can we directly set the MAB confidence levels to the output levels α from the online
j
FDR procedure? If we do, our p-values are not independent across different hypotheses
anymore: Pj directlydependsontheFDRlevelsα andeachα inturndependsonpastMAB
j j
rejections, thus on past MAB p-values (see Figure 1). Does the new interaction compromise
FDR guarantees?
Although known online FDR procedures [2, 4] guarantee FDR control for independent
p-values, this does not hold for dependent p-values in general. Hence FDR control guarantees
cannot simply be obtained out of the box. In particular, it is not a priori obvious that the
introduced dependence between the p-values does not cause problems, i.e. violates necessary
conditions for FDR control type theorems. A key insight that emerges from our analysis is
that an appropriate bandit algorithm actually shapes the p-value distribution under the null
in a good way that allows us to control FDR.
2.2 A meta-algorithm
Procedure 1 summarizes our doubly-sequential procedure, with a corresponding flowchart in
Figure 1. We will prove theoretical guarantees after instantiating the separate modules. Note
that our framework allows the scientist to plug in their favorite best-arm MAB algorithm
or online FDR procedure. The choice for each of them determines which guarantees can be
proven for the entire setup. Any independent improvement in either of the two parts would
immediately lead to an overall performance boost of the overall framework.
Procedure 1 MAB-FDR Meta algorithm skeleton
1. The scientist sets a desired FDR control rate α.
2. For each j = 1,2,...:
Experimentj receivesadesignatedcontrolarmandsomenumberofalternativearms.
•
An online-FDR procedure returns an α that is some function of the past values
j
•
P(cid:96) j−1 .
{ }(cid:96)=1
An MAB procedure with inputs (a) the control arm and K(j) alternative arms, (b)
•
confidence level α , and (c) (optional) a precision (cid:15) 0, is executed and if the proce-
j
≥
dure self-terminates, returns a recommended arm.
Throughout the MAB procedure, an always valid p-value is constructed continuously
•
for each time t using only the samples collected up to that time from the j-th experi-
j
ment: for any t, it is a random variable P [0,1] that is super-uniformly distributed
t
∈
whenever the control-arm is best.
WhentheMABprocedureisterminatedattimet(eitherbyitselforbyauser-defined
• j
stoppingcriterionthatmaydependonP ),ifthearmwiththehighestempiricalmean
t
is not the control arm and P j α , then we return Pj := P j , and the control arm is
t j t
≤
rejected in favor of this empirically best arm.
3 A concrete procedure with guarantees
We now take the high-level road map given in Procedure 1, and show that we can obtain a
concrete, practically implementable framework with FDR control and power guarantees. We
5

first discuss the key modeling decisions we have to make in order to seamlessly embed MAB
algorithms into an online FDR framework. We then outline a modified version of a commonly
used best-arm algorithm, before we finally prove FDR and power guarantees for the concrete
| combined procedure. |      |            |                  |     |          |     |     |     |
| ------------------- | ---- | ---------- | ---------------- | --- | -------- | --- | --- | --- |
| 3.1 Defining        | null | hypotheses | and constructing |     | p-values |     |     |     |
Our first task is to define a null hypothesis for each experiment. As mentioned before, the
choice of the null is not immediately obvious, since we sample from multiple distributions
adaptively insteadofindependently. Inparticular,wewillgenerallynothavethesamenumber
ofsamplesforallarms. Givenadistributionwithdefaultmeanµ andalternativedistributions
0
K
with means µ i , we propose that the null hypothesis for the j-th experiment should be
{ }i=1
defined as
j
|     |     | H 0 : µ | 0 µ i (cid:15) for | all i = | 1,...,K. |     |     | (1) |
| --- | --- | ------- | ------------------ | ------- | -------- | --- | --- | --- |
|     |     |         | ≥ −                |         |          |     |     |     |
In words, the null corresponds to there being no alternative arm that is (cid:15)-better than the
control arm.
It remains to define a p-value for each experiment that is stochastically dominated by a
uniform random variable under the null; such a p-value is said to be superuniform. In order
to simplify notation below, we omit the index j for the experiment and retain only the index
i for the choice of arms. In order to be able to use a p-value at arbitrary times in the testing
procedure and to allow scientists to monitor the algorithm’s progress in real time, it is helpful
|     | always valid | p-value, |     |     |     |     |     |     |
| --- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
to define an as previously defined by Johari et al. [5]. An always valid
p-value is a stochastic process P ∞ such that for all fixed and random stopping times T,
t t=1
|     | P   | {   | }   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
under any distribution over the arm rewards such that the null hypothesis is true, we have
0
P
|     |     |     | (P  | α) α. |     |     |     | (2) |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
0 T
|     |     |     | ≤   | ≤   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
When all arms are drawn independently an equal number of times, by linearity of expectation
one can regard the distance of each pair of samples as a random variable drawn i.i.d. from a
distribution with mean µ˜ := µ µ . We can then view the problem as testing the standard
|     |     | i 0 | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
−
hypothesis H : µ˜ > (cid:15). However, when the arms are pulled adaptively, a different solution
0 i
−
needs to be found—indeed, in this case, the sample means are not unbiased estimators of
the true means, since the number of times an arm was pulled now depends on the empirical
| means of all | the arms. |     |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
Our strategy is to construct always valid p-values by using the fact that p-values can
be obtained by inverting confidence intervals. To construct always-valid confidence bounds,
we resort to the fundamental concept of the law of the iterated logarithm (LIL), for which
non-asymptotic versions have been recently derived and used for both bandits and testing
| problems (see | [6], [7]). |              |     |     |     |     |     |     |
| ------------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| To elaborate, | define     | the function |     |     |     |     |     |     |
(cid:115)
|     |     |       | log(1)+3log(log(1))+ |     | 3 log(log(en)) |     |     |     |
| --- | --- | ----- | -------------------- | --- | -------------- | --- | --- | --- |
|     | ϕ   | (δ) = | δ                    | δ   | 2              | .   |     | (3) |
n
n
If µ is the empirical average of independent samples from a sub-Gaussian distribution, then
(cid:98)i,n
it is known (see, for instance, [8, Theorem 8]) that for all δ (0,1), we have
∈
|     | ∞   |     |     | ∞   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:110) (cid:16) (cid:91) (cid:17) (cid:16) (cid:91) (cid:17)(cid:111)
| P   |     |     | P   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
max µ (cid:98)i,n µ i > ϕ n (δ 0.1) , µ (cid:98)i,n µ i < ϕ n (δ 0.1) δ, (4)
|     | { − |     | ∧ } | {   | − − | ∧   | } ≤ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | n=1 |     |     | n=1 |     |     |     |     |
6

| where | δ   | 0.1 := | min   | δ,0.1      | .   |        |              |     |        |      |     |     |
| ----- | --- | ------ | ----- | ---------- | --- | ------ | ------------ | --- | ------ | ---- | --- | --- |
|       | ∧   |        | {     |            | }   |        |              |     |        |      |     |     |
| We    | are | now    | ready | to propose |     | single | arm p-values |     | of the | form |     |     |
(cid:110) (cid:111)
|     |     |     |       |           |       |                 |       |          | γ            |                 | γ               |     |
| --- | --- | --- | ----- | --------- | ----- | --------------- | ----- | -------- | ------------ | --------------- | --------------- | --- |
|     |     | P : | = sup | γ         | [0,1] | µ               | ϕ     | (        | )            | µ               | +ϕ ( )+(cid:15) | (5) |
|     |     | i,t |       |           |       | (cid:98)i,ni(t) |       | ni(t) 2K |              | (cid:98)0,n0(t) | n0(t) 2         |     |
|     |     |     |       | ∈         |       | |               | −     |          | ≤            |                 |                 |     |
|     |     |     |       | (cid:110) |       |                 |       |          |              | (cid:111)       |                 |     |
|     |     |     | = sup | γ         | [0,1] | LCB             | i (t) | UCB 0    | (t)+(cid:15) |                 |                 |     |
|     |     |     |       | ∈         |       | |               | ≤     |          |              |                 |                 |     |
Here we set P = 1 if the supremum is taken over an empty set. Given these single arm
i,t
| p-values, |     | the always-valid |     | p-value |     | for the | experiment    |     | is defined | as  |     |     |
| --------- | --- | ---------------- | --- | ------- | --- | ------- | ------------- | --- | ---------- | --- | --- | --- |
|           |     |                  |     |         |     | P :=    | min           | min | P .        |     |     | (6) |
|           |     |                  |     |         |     | t       |               |     | i,s        |     |     |     |
|           |     |                  |     |         |     |         | s≤t i=1,...,K |     |            |     |     |     |
We claim that this procedure leads to an always valid p-value (with proof in Appendix 5.1).
Proposition 1. The sequence ∞ defined via equation is an always valid p-value.
|     |          |     |          |       |         | P t          |     |                |     | (6) |     |     |
| --- | -------- | --- | -------- | ----- | ------- | ------------ | --- | -------------- | --- | --- | --- | --- |
|     |          |     |          |       | {       | } t=1        |     |                |     |     |     |     |
| See | Section  | 5.1 | for the  | proof | of this | proposition. |     |                |     |     |     |     |
| 3.2 | Adaptive |     | sampling |       | for     | best-arm     |     | identification |     |     |     |     |
In the traditional A/B testing setting described in the introduction, samples are allocated
uniformly to the different alternatives. But by allocating different numbers of samples to
the alternatives, decisions can be made with the same statistical significance using far fewer
samples. Suppose moreover that there is a unique maximizer i := arg max µ , so that
(cid:63) i
i=0,1,...,K
|     |     |     |     |     | ∆ i := | µ i(cid:63) | µ i > 0 | for | all | i = i (cid:63) . |     |     |
| --- | --- | --- | --- | --- | ------ | ----------- | ------- | --- | --- | ---------------- | --- | --- |
|     |     |     |     |     |        | −           |         |     |     | (cid:54)         |     |     |
Thenforanyδ (0,1),best-armidentificationalgorithmsforthemulti-armedbanditproblem
∈
|     |     |     |     |     |     |     |     |     |     | most2 | (cid:80) ∆−2log(1/δ) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------- | --- |
can identify i (cid:63) with probability at least 1 δ based on at total
|     |     |     |     |     |     |     | −   |     |     |     | i(cid:54)=i(cid:63) i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
samples (see the paper [9] for a brief survey and [10] for an application to clinical trials). In
contrast, if samples are allocated uniformly to the alternatives under the same conditions,
Kmax∆−2log(K/δ)
then the most natural procedures require samples before returning i (cid:63)
|      |             |     |          |     |     |     | i(cid:54)=i(cid:63) |     | i   |     |     |     |
| ---- | ----------- | --- | -------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
| with | probability |     | at least | 1   | δ.  |     |                     |     |     |     |     |     |
−
However, standard best-arm bandit algorithms do not incorporate asymmetry as induced
by null-hypotheses as in definition (1) by default. Furthermore, recall that a practical sci-
entist might desire the ability to incorporate approximation and a minimum improvement
requirement. More precisely, it is natural to consider the requirement that the returned arm
i satisfiestheboundsµ µ +(cid:15)andµ µ (cid:15)forsome(cid:15) > 0. Forthosereadersunfamil-
| b   |     |     |     | i b ≥ | 0   |     | i b ≥ i(cid:63)− |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
iar with best-arm MAB algorithms, it is likely helpful to first grasp the entire framework in
the special (cid:15) = 0 throughout, before understanding it in full generality with the complications
introduced by setting (cid:15) > 0. In the following we present a modified MAB algorithm based on
| the | common | LUCB | algorithm |     | (see | [11, | 12]). |     |     |     |     |     |
| --- | ------ | ---- | --------- | --- | ---- | ---- | ----- | --- | --- | --- | --- | --- |
InsidetheloopofAlgorithm1,weuseh 0,1,...,K todenotethecurrentempirically-
t
|     |     |     |     |     |     |     | ∈   | {   |     | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
best arm, (cid:96) to denote the most promising contender among the other arms that has not yet
t
been sampled enough to be ruled out. The parameter (cid:15) 0 is a slack variable, and the
≥
algorithm is easiest to first understand when (cid:15) = 0. We provide a visualization of how
(cid:15) affects the stopping condition in Figure 2. Step (a) checks if h is within (cid:15) of the true
t
2Here
|     | we  | have | ignored | some | doubly-logarithmic |     | factors. |     |     |     |     |     |
| --- | --- | ---- | ------- | ---- | ------------------ | --- | -------- | --- | --- | --- | --- | --- |
7

Algorithm 1 Best-arm identification with a control arm for confidence δ and precision (cid:15) 0
≥
For all t let n (t) be the number of times arm i has been pulled up to time t. In addition, for
i
each arm i let µ (t) = 1 (cid:80)ni(t) r (τ), define
(cid:98)i ni(t) τ=1 i
LCB (t) := µ ϕ ( δ ) and UCB (t) := µ +ϕ (δ).
i (cid:98)i,ni(t) − ni(t) 2K i (cid:98)i,ni(t) ni(t) 2
1. Set t = 1 and sample every arm once.
2. Repeat: Compute h = arg max µ (t), and (cid:96) = arg max UCB (t)
t (cid:98)i t i
i=0,1,...,K i=0,1,...,K,i(cid:54)=ht
(a) If LCB (t) > UCB (t) (cid:15), for all i = 0, then output 0 and terminate.
0 i
− (cid:54)
Else if LCB (t) > UCB (t) (cid:15) and LCB (t) > UCB (t)+(cid:15), then output h and
ht (cid:96)t
−
ht 0 t
terminate.
(b) If(cid:15) > 0, letu = argmax UCB (t)andpullalldistinctarmsin 0,u ,h ,(cid:96) once.
t i(cid:54)=0 i t t t
{ }
If (cid:15) = 0, pull arms h and (cid:96) and set t = t+1.
t t
highest mean, and if it is also at least (cid:15) greater than the true mean of the control arm (or
is the control arm), terminates with this arm h . Step (b) ensures that the control arm is
t
sufficiently sampled when (cid:15) > 0. Step (c) pulls h and (cid:96) , reducing the overall uncertainty in
t t
the difference between their two means.
The following proposition applies to Algorithm 1 run with a control arm indexed by i = 0
with mean µ and alternative arms indexed by i = 1,...,K with means µ , respectively. Let
0 i
i denote the random arm returned by the algorithm assuming that it exits, and define the
b
set
(cid:63) := i = 0 µ max µ (cid:15) and µ > µ +(cid:15) . (7)
S {
(cid:63)
(cid:54) |
i(cid:63)
≥ i=1,...,K
i
−
i(cid:63) 0
}
Note that the mean associated with any index i (cid:63), assuming that the set is non-empty,
(cid:63)
∈ S
is guaranteed to be (cid:15)-superior to the control mean, and at most (cid:15)-inferior to the maximum
mean over all arms.
µ
⇤ UCB
µ + ✏ l t ✏
0 LCB
µ ✏ h t ✏
⇤   µ UCB
0
0
0 1 2 3 4 5 0 h l …
t t
Control arm Alternative arms Control arm Alternative arms
(a) (b)
Figure 2. (a) The means of arms 1,2,3 are within (cid:15) of the best arm, but only arms 1,2
{ } { }
are at least (cid:15) better than the control arm 0. Thus, returning any of arms 3,4,5 would result
{ }
in a false discovery when (cid:15)>0. (b) An example of the stopping condition being critically met
and returning a non-control arm h . While LCB > UCB (cid:15) is satisfied with some slack,
t ht (cid:96)t
−
LCB >UCB +(cid:15) is just barely satisfied.
ht 0
8

Proposition 2. The algorithm 1 terminates in finite time with probability one. Furthermore,
suppose that the samples from each arm are independent and sub-Gaussian with scale 1. Then
| for | any | δ (0,1) | and | (cid:15) | 0, Algorithm | 1   | has the following |     | guarantees: |     |     |
| --- | --- | ------- | --- | -------- | ------------ | --- | ----------------- | --- | ----------- | --- | --- |
|     |     | ∈       |     | ≥        |              |     |                   |     |             |     |     |
(a) Suppose that µ > max µ (cid:15). Then with probability at least 1 δ, the algorithm
|     |     |     | 0   |     |     | i − |     |     |     | −   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1,...,K
|     |     |     |     |     |     |     | (cid:16) |     |     | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- |
exits with after taking at most (cid:80)K − 2log(Klog(∆(cid:101) − 2)/δ) time steps with
|     |           |      | i b = 0 |     |     |                  | O            | ∆(cid:101) |       |     |     |
| --- | --------- | ---- | ------- | --- | --- | ---------------- | ------------ | ---------- | ----- | --- | --- |
|     |           |      |         |     |     |                  | i=0          | i          |       | i   |     |
|     | effective | gaps |         |     |     |                  |              |            |       |     |     |
|     |           |      |         |     |     | ∆(cid:101)0 = (µ | 0 +(cid:15)) | max µ      | j and |     |     |
−j=1,...,K
|     |     |     |     |     |     | ∆(cid:101)i = (µ | 0 +(cid:15)) µ | i . |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | -------------- | --- | --- | --- | --- |
−
(b) Otherwise, suppose that the set (cid:63) as defined in equation (7) is non-empty. Then with
S
probability at least 1 δ, the algorithm exits with i (cid:63) after taking at most
b
|     | (cid:16) (cid:80)K |            |                       | −           |        | (cid:17)  |            | ∈              | S                   |                  |     |
| --- | ------------------ | ---------- | --------------------- | ----------- | ------ | --------- | ---------- | -------------- | ------------------- | ---------------- | --- |
|     | O                  | ∆(cid:101) | −2log(Klog(∆(cid:101) |             | −2)/δ) | time      | steps with | effective      | gaps                |                  |     |
|     |                    | i=0        | i                     |             | i      |           |            |                |                     |                  |     |
|     |                    |            |                       |             |        | (cid:26)  |            |                |                     | (cid:27)         |     |
|     |                    |            |                       | ∆(cid:101)0 | = min  | max       | µ (µ       | +(cid:15)),max | ∆ ,(cid:15)         | and              |     |
|     |                    |            |                       |             |        |           | j 0        |                | 0                   |                  |     |
|     |                    |            |                       |             |        | j=1,...,K | −          |                | { }                 |                  |     |
|     |                    |            |                       |             |        | (cid:26)  | (cid:26)   |                |                     | (cid:27)(cid:27) |     |
|     |                    |            |                       | ∆(cid:101)i | = max  | ∆ ,min    | max        | µ (µ           | +(cid:15)),(cid:15) | .                |     |
|     |                    |            |                       |             |        | i         |            | j              | 0                   |                  |     |
|     |                    |            |                       |             |        |           | j=1,...,K  | −              |                     |                  |     |
See Section 5.2 for the proof of this claim. Part (a) of Proposition 2 guarantees that when no
alternative arm is (cid:15)-superior to the control arm (i.e. under the null hypothesis), the algorithm
stops and returns the control arm after a certain number of samples with probability at least
1 δ, where the sample complexity depends on (cid:15)-modified gaps between the means µ and
0
−
µ . Part (b) guarantees that if there is in fact at least one alternative that is (cid:15)-superior to
i
the control arm (i.e. under the alternative), then the algorithm will find at least one of them
that is at most (cid:15)-inferior to the best of all possible arms with the same sample complexity
and probability.
|     |     |     |     |     |     |     | (cid:16) |     |     | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- |
Note that the required number of samples O (cid:80)K ∆(cid:101) −2log(Klog(∆(cid:101) −2)/δ) in Proposi-
|     |     |     |     |     |     |     |     | i=0 | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion 2 is comparable, up to log factors, with the well-known results in [11, 12] for the case
(cid:15) = 0, with the modified gaps ∆(cid:101)i replacing ∆ = µ µ . Indeed, the nearly optimal sample
|     |     |     |     |     |     |     | i   | i(cid:63) i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
−
complexityresultof[12]impliesthatthealgorithmterminatesundersettings(a)and(b)after
|     |      |       | ∆−2log(Klog(∆−2)/δ)+ |     |     |     | (cid:80)            | ∆−2log(log(∆−2)/δ)) |     |         |            |
| --- | ---- | ----- | -------------------- | --- | --- | --- | ------------------- | ------------------- | --- | ------- | ---------- |
| at  | most | O(max |                      |     |     |     |                     |                     |     | samples | are taken. |
|     |      |       | j(cid:54)=i(cid:63)  | j   |     | j   | i(cid:54)=i(cid:63) | i                   | i   |         |            |
In our development to follow, we now bring back the index for experiment j, in particular
usingPj todenotethequantityP j atanystoppingtimeT. Herethestoppingtimecaneither
T
| be  | defined  | by the | scientist, |     | or in       | an algorithmic | manner.     |     |     |     |     |
| --- | -------- | ------ | ---------- | --- | ----------- | -------------- | ----------- | --- | --- | --- | --- |
| 3.3 | Best-arm |        | MAB        |     | interacting |                | with online | FDR |     |     |     |
After having established null hypotheses and p-values in the context of best-arm MAB algo-
rithms, we are now ready to embed them into an online FDR procedure. In the following, we
consider p-values for the j-th experiment Pj := P j which is just the p-value as defined in
Tj
| equation |     | (6) at | the stopping |     | time | T , which | depends | on α | .   |     |     |
| -------- | --- | ------ | ------------ | --- | ---- | --------- | ------- | ---- | --- | --- | --- |
|          |     |        |              |     |      | j         |         |      | j   |     |     |
We denote the set of true null and false null hypotheses up to experiment J as (J)
0
H
and 1 (J) respectively, where we drop the argument whenever it’s clear from the context.
H
1
The variable R j = Pj≤αj indicates whether a the null hypothesis of experiment j has been
9

rejected, where R = 1 denotes a claimed discovery that an alternative was better than the
j
control. The false discovery rate (FDR) and modified FDR up to experiment J are then
defined as
|     |     |        |     |     | (cid:80)  |     |     |             | E(cid:80)  |       |     |     |
| --- | --- | ------ | --- | --- | --------- | --- | --- | ----------- | ---------- | ----- | --- | --- |
|     |     |        |     |     |           | R   |     |             |            |       | R   |     |
|     |     |        |     | E   | j∈H0      | j   |     |             |            | j∈H0  | j   |     |
|     |     | FDR(J) |     | :=  |           |     |     | and mFDR(J) | :=         |       | .   | (8) |
|     |     |        |     |     | (cid:80)J |     |     |             | E(cid:80)J |       |     |     |
|     |     |        |     |     | R         | 1   |     |             |            | R     | +1  |     |
|     |     |        |     |     | i=1       | i ∨ |     |             |            | i=1 i |     |     |
Here the expectations are taken with respect to distributions of the arm pulls and the re-
spective sampling algorithm. In general, it is not true that control of one quantity implies
control of the other. Nevertheless, in the long run (when the law of large numbers is a good
approximation),onedoesnotexpectamajordifferencebetweenthetwoquantitiesinpractice.
The set of true nulls thus includes all experiments where H j is true, and the FDR
|     |     |     |     |     | 0   |     |     |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
H
and mFDR are well-defined for any number of experiments J, since we often desire to control
N.
FDR(J) or mFDR(J) for all J In order to measure power, we define the (cid:15)-best-arm
∈
| discovery |     | rate |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as
E(cid:80)
|     |     |     |     |                |     |     |      | R 1               | 1                          |     |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | ---- | ----------------- | -------------------------- | --- | --- | --- |
|     |     |     |     |                |     |     | j∈H1 | j µib ≥µi(cid:63) | −(cid:15) µib ≥µ0+(cid:15) |     |     |     |
|     |     |     |     | (cid:15)BDR(J) |     | :=  |      |                   |                            |     |     | (9) |
1 (J)
|     |     |     |     |     |     |     |     | |H  | |   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We provide a concrete procedure 2 for our doubly sequential framework, where we use a
particular online FDR algorithm due to Javanmard and Montanari [4] known as LORD; the
reader should note that other online FDR procedure could be used to obtain essentially the
same set of guarantees. Given a desired level α, the LORD procedure starts off with an initial
“α-wealth”ofW(0) < α. Basedonainifinitesequence γ ∞ thatsumstoone, andthetime
i }i=1
{
of the most recent discovery τ , it uses up a fraction γ of the remaining α-wealth to test.
|     |     |     |     |     | j   |     |     | j−τj |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Whenever there is a rejection, we increase the α-wealth by α W(0). A feasible choice for a
−
stopping time in practice is T j := min T(α j ),M , where M is a maximal number of samples
|     |     |     |     |     |     |     | {   | }   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the scientist wants to pull and T(α ) is the stopping time of the best-arm MAB algorithm
j
| run | at confidence |     | α   | .   |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
Procedure 2 MAB-LORD: best-arm identification with online FDR control
(cid:80)∞
1. Initialize W(0) < α, set τ 0 = 0, and choose a sequence γ i s.t. γ i = 1
|     |       |      |         |         |      |     |       |       | { } | i=1 |     |     |
| --- | ----- | ---- | ------- | ------- | ---- | --- | ----- | ----- | --- | --- | --- | --- |
|     | 2. At | each | step j, | compute | α    | = γ | W(τ   | ) and |     |     |     |     |
|     |       |      |         |         |      | j   | j−τj  | j     |     |     |     |     |
|     | W(j   | +1)  | = W(j)  |         | α +R | (α  | W(0)) |       |     |     |     |     |
|     |       |      |         |         | j    | j   |       |       |     |     |     |     |
|     |       |      |         | −       |      | −   |       |       |     |     |     |     |
3. Output α and run Algorithm 1 using α -confidence and stop at a stopping time T .
|     |     |     | j   |     |     |     |     | j   |     |     |     | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4. Algorithm 1 returns Pj and we reject the null hypothesis if Pj α .
j
≤
1
5. Set R j = Pj≤αj ,τ j = τ j−1 jR j , update j = j +1 and go back to step 2.
∨
The following theorem provides guarantees on mFDR and power for the MAB-LORD proce-
dure.
| Theorem |     | 1 (Online |     | mFDR | control | for | MAB-LORD). |     |     |     |     |     |
| ------- | --- | --------- | --- | ---- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
(a) Procedure 2 achieves mFDR control at level α for stopping times T = min T(α ),M .
|     |              |     |     |        |     |             |     |             |     | j   | j   |     |
| --- | ------------ | --- | --- | ------ | --- | ----------- | --- | ----------- | --- | --- | --- | --- |
|     |              |     |     |        |     |             |     |             |     |     | {   | }   |
| (b) | Furthermore, |     | if  | we set | M = | , Procedure |     | 2 satisfies |     |     |     |     |
∞
|     |     |     |     |     |     |                |     | (cid:80)J 1 |          |     |     |      |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | -------- | --- | --- | ---- |
|     |     |     |     |     |     |                |     | j∈H1        | (1 α j ) |     |     |      |
|     |     |     |     |     |     | (cid:15)BDR(J) |     | j=1         | −        |     |     |      |
|     |     |     |     |     |     |                |     |             | .        |     |     | (10) |
|     |     |     |     |     |     |                | ≥   | (J)         |          |     |     |      |
1
|     |     |     |     |     |     |     |     | |H  | |   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10

The proof of this theorem can be found in Section 5.3. Note that by the arguments in
the proof of Theorem 1, mFDR control itself is actually guaranteed for any generalized α-
investingprocedure[3]combinedwithanybest-armMABalgorithm. Infactwecoulduseany
adaptive stopping time T which depend on the history only via the rejections R ,...,R .
j 1 j−1
Furthermore, using a modified LORD proposed by Javanmard and Montanari [13], we can
also guarantee FDR control– which can be found in Appendix B.
It is noteworthy that small values of α do not only guarantee smaller FDR error but also
higher BDR. However, there is no free lunch — a smaller α implies a smaller α at each
j
experiment, which in turn causes the best-arm MAB algorithm to employ a larger number of
pulls in each experiment.
4 Experimental results
In the following, we describe the results of experiments 3 on both simulated and real-world
datasetstoillustratethepropertiesandguaranteesofourproceduredescribedinSection3. In
particular, we show that the mFDR is indeed controlled over time and that MAB-FDR (used
interchangeablywithMAB-LORDhere)ishighlyadvantageousintermsofsamplecomplexity
and power compared to a straightforward extension ofA/B testing that is embedded in online
FDR procedures. Unless otherwise noted, we set (cid:15) = 0 in all of our simulations to focus on
the main ideas and keep the discussion concise.
There are two natural frameworks to compare against MAB-FDR. The first, called AB-
FDR or AB-LORD, swaps the MAB part for an A/B (i.e. A/B/n) test (uniformly sampling
all alternatives until termination). The second comparator swaps the online FDR control for
independenttestingatαforallhypotheses–wecallthisMAB-IND.Formally,AB-FDRswaps
step3inProcedure2with“Output α and uniformly sample each arm until stopping time T .”
j j
while MAB-IND swaps step 4 in Procedure 2 with “The algorithm returns Pj and we reject
the null hypothesis if Pj α.”. In order to compare the performances of these procedures,
≤ log(j∨2)
we ran three sets of simulations using Procedure 2 with (cid:15) = 0 and γ j = 0.07 √ as in [4].
je logj
The first two sets are on artificial data (Gaussian and Bernoulli draws from sets of randomly
drawn means µ ), while the third is based on data from the New Yorker Cartoon Caption
i
Contest (Bernoulli draws).
Our experiments are run on artificial data with Gaussian/Bernoulli draws and real-world
Bernoulli draws from the New Yorker Cartoon Caption Contest. Recall that the sample
complexity of the best-arm MAB algorithm is determined by the gaps ∆ = µ µ . One
j i(cid:63)
−
j
of the main relevant differences to consider between an experiment of artificial or real-world
natureisthusthedistributionofthemeansµ fori = 1,...,K. Theartificialdatasimulations
i
are run with a fixed gap between the mean of the best arm µ and second best arm µ , which
i(cid:63) 2
we denote by ∆ = µ µ . In each experiment (hypothesis), the means of the other arms are
i(cid:63)− 2
set uniformly in [0,µ ]. For our real-world simulations with the cartoon contest, the means
2
for the arms in each experiment are not arbitrary but correspond to empirical means from the
caption contest. In addition, the contests actually follow a natural chronological order (see
details below), which makes this dataset highly relevant to our purposes. In all simulations,
60% of all the hypotheses are true nulls, and their indices are chosen uniformly.
3The code for reproducing all experiments and plots in this paper is publicly available at
https://github.com/fanny-yang/MABFDR
11

| 4.1 | Power | and | sample |     | complexity |     |     |     |     |     |
| --- | ----- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- |
ThefirstsetofsimulationscomparesMAB-FDRagainstAB-FDR.Theyconfirmthatthetotal
number of necessary pulls to determine significance (which we refer to as sample complexity)
is much smaller for MAB-FDR than for AB-FDR. In the MAB-FDR framework, this also
| effectively |     | leads | to higher | power | given | a fixed | truncation | time. |     |     |
| ----------- | --- | ----- | --------- | ----- | ----- | ------- | ---------- | ----- | --- | --- |
Two types of plots are used to demonstrate the superiority of our procedure: for one we
fix the number of arms and plot the (cid:15)BDR with (cid:15) = 0 (which we call BDR for short) for both
procedures over different choices of truncation times M. For the other we fix M and show
how the sample complexity varies with the number of arms. Note that low BDR means that
the bandit algorithm often reaches truncation time before it could stop.
| 4.1.1 | Simulated |     | Gaussian |     | and | Bernoulli | trials |     |     |     |
| ----- | --------- | --- | -------- | --- | --- | --------- | ------ | --- | --- | --- |
For the Gaussian draws, we set µ = 8. The gap to the second best arm is ∆ = 3 so that all
i(cid:63)
means µ are drawn uniformly between Unif [0,5]. The number of hypotheses is fixed
i(cid:54)=i(cid:63)
∼
to be 500. For Bernoulli draws we choose the maximum mean to be µ i(cid:63) = 0.4, ∆ = 0.3 so
that all means µ are drawn uniformly between Unif [0,0.1]. The number of hypotheses
i(cid:54)=i(cid:63)
∼
is fixed at 50. We display the empirical average over 100 runs where each run uses the
same hypothesis sequence (indicating which hypotheses are true and false) and sequence of
means µ i for each hypothesis. The only randomness we average over comes from the random
Gaussian/Bernoulli draws which cause different rejections R and α , so that the randomness
|     |     |     |     |     |     |     |     | j   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in each draw propagates through the online FDR procedure. The results can be seen in
| Figures | 3   | and 4. |     |     |     |     |     |     |     |     |
| ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
0001/ selpmas fo rebmun latoT
|     |     | MAB-LORD |     |     | AB-LORD |     |     | MAB-LORD |     | AB-LORD |
| --- | --- | -------- | --- | --- | ------- | --- | --- | -------- | --- | ------- |
1.0
160
140
0.8
120
|     | RDB 0.6 |     |     |     |     |     | 100 |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
80
0.4
60
40
0.2
20
0.0
0
|     | 100 | 200               | 300 | 400 500 | 600 | 700 800 |     | 20 40          | 60  | 80 100 120 |
| --- | --- | ----------------- | --- | ------- | --- | ------- | --- | -------------- | --- | ---------- |
|     |     | Truncation time T |     |         |     |         |     | Number of arms |     |            |
S
|     |     |     |     | (a) |     |     |     |     | (b) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 3. (a) Power vs. truncation time T (per hypothesis) for 50 arms and (b) Sample
S
complexity vs. # arms for truncation time M = 300 for Gaussian draws with fixed µ = 8,
i(cid:63)
| ∆=3 | over | 500 | hypotheses |     | with 200 | non-nulls, | averaged | over 100 runs. |     |     |
| --- | ---- | --- | ---------- | --- | -------- | ---------- | -------- | -------------- | --- | --- |
The power at any given truncation time is much higher for MAB-FDR than AB-FDR.
This is because the best-arm MAB is more likely to satisfy the stopping criterion before any
given truncation time than the uniform sampling algorithm. The plot in Fig. 3(a) suggests
that the actual stopping time of the algorithm is concentrated between 160 and 200 while it
| is much | more | spread | out | for | the uniform | algorithm. |     |     |     |     |
| ------- | ---- | ------ | --- | --- | ----------- | ---------- | --- | --- | --- | --- |
The sample complexity plot in Fig. 3(b) qualitatively shows how the total number of
necessary arm pulls for AB-FDR increases much faster with the number of arms than for the
12

|     | MAB-LORD |     | AB-LORD |     | 0001/ selpmas fo rebmun latoT |          |     |         |
| --- | -------- | --- | ------- | --- | ----------------------------- | -------- | --- | ------- |
|     |          |     |         |     |                               | MAB-LORD |     | AB-LORD |
1.0
250
0.8
200
0.6
RDB
150
0.4
100
0.2
|     | 0.0               |       |       |     |     | 50             |       |       |
| --- | ----------------- | ----- | ----- | --- | --- | -------------- | ----- | ----- |
|     | 5                 | 10 15 | 20    | 25  |     | 5 10 15        | 20 25 | 30 35 |
|     | Truncation time T |       | /1000 |     |     |                |       |       |
|     |                   |       | S     |     |     | Number of arms |       |       |
|     |                   | (a)   |       |     |     |                | (b)   |       |
Figure 4. (a) Power over truncation time T (per hypothesis) for 50 arms and (b) Sample
S
complexity over number of arms for truncation time M =5000 for Bernoulli draws with fixed
µ =0.7, ∆=0.3 over 50 hypotheses with 20 non-nulls, averaged over 100 runs.
i(cid:63)
MAB-FDR, before it plateaus at the truncation time multiplied by the number of hypotheses.
Recall that whenever the best-arm MAB stops before the truncation time in each hypothesis,
the stopping criterion is met, i.e. the best arm is identified with probability at least 1 α j ,
−
| so that | the power | is bound | to be close | to one | whenever | T = T(α | ).  |     |
| ------- | --------- | -------- | ----------- | ------ | -------- | ------- | --- | --- |
|         |           |          |             |        |          | j j     |     |     |
For Bernoulli draws we choose the maximum mean to be µ = 0.4, ∆ = 0.3 so that all
i(cid:63)
means µ are drawn uniformly between Unif [0,0.1]. The number of hypotheses is fixed
i(cid:54)=i(cid:63)
∼
at 50. Otherwise the experimental setup is identical to those discussed in the main text for
| Gaussians. | The plots | for Bernoulli |     | data can | be found | in Fig. 4. |     |     |
| ---------- | --------- | ------------- | --- | -------- | -------- | ---------- | --- | --- |
The behavior for both Gaussian and Bernoullis are comparable, which is not surprising
due to the choice of the subGaussian LIL bound. However one may notice that the choice
of the gap of ∆ = 3 vs. ∆ = 0.3 drastically increases sample complexity so that the phase
| transition | for power | is shifted | to very | large | T . |     |     |     |
| ---------- | --------- | ---------- | ------- | ----- | --- | --- | --- | --- |
S
| 4.1.2 | Application | to New | Yorker | captions |     |     |     |     |
| ----- | ----------- | ------ | ------ | -------- | --- | --- | --- | --- |
In the simulations with real data we consider the crowd-sourced data collected for the New
Yorker Magazine’s
Cartoon Caption contest: for a fixed cartoon, captions are shown to
individuals online one at a time and they are asked to rate them as ‘unfunny’, ‘somewhat
funny’, or ‘funny’. We considered 30 contests4 where for each contest, we computed the
fraction of times each caption was rated as either ‘somewhat funny’ or ‘funny’. We treat each
caption as an arm, but because each caption was only shown a finite number of times in the
dataset, we simulate draws from a Bernoulli distribution with the observed empirical mean
computed from the dataset. When considering subsets of the arms in any given experiment,
we always use the captions with the highest empirical means (i.e. if n = 10 then we use the
| 10 captions | that had | the highest | empirical | means |     | in that contest). |     |     |
| ----------- | -------- | ----------- | --------- | ----- | --- | ----------------- | --- | --- |
Although MAB-FDR still outperforms AB-FDR by a large margin, the plots in Figure 5
alsoshowhowthepowerandsamplecomplexitynotablydifferfromourtoysimulation, where
4Contestnumbers520-551,excluding525and540astheywerenotpresent.
Fulldatasetanditsdescription
| is available | at https://github.com/nextml/NEXT-data/. |     |     |     |     |     |     |     |
| ------------ | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
13

we seem to have chosen a rather benign distribution of means - in this setting, the gap ∆ is
| much | lower, | often | around | 0.01. |     |     |     |     |
| ---- | ------ | ----- | ------ | ----- | --- | --- | --- | --- |
∼
|     |     | MAB-LORD |     | AB-LORD |     |     |     |     |
| --- | --- | -------- | --- | ------- | --- | --- | --- | --- |
0001/ selpmas fo rebmun latoT
|     |     |     |     |     |     | MAB-LORD | AB-LORD |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --- |
0.7
4000
0.6
3800
0.5
3600
RDB 0.4
3400
0.3
|     | 0.2 |     |     |     |     | 3200 |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     | 0.1 |     |     |     |     | 3000 |     |     |
0.0
2800
|     | 10  | 20 30          | 40  | 50 60 | 70 80 | 10 20 30       | 40 50 60 | 70 80 |
| --- | --- | -------------- | --- | ----- | ----- | -------------- | -------- | ----- |
|     |     | Number of arms |     |       |       | Number of arms |          |       |
|     |     |                | (a) |       |       |                | (b)      |       |
Figure 5. (a) BDR over number of arms, i.e. truncation time per hypothesis for 10 arms
and(b)SamplecomplexityovernumberofarmsfortruncationtimeM =130000forBernoulli
|     | draws, 30 | hypotheses | with | 12 non-nulls | and averaged | over 100 runs. |     |     |
| --- | --------- | ---------- | ---- | ------------ | ------------ | -------------- | --- | --- |
| 4.2 | mFDR      | and        | FDR  | control      |              |                |     |     |
In this section we use simulations to demonstrate the second part of our meta algorithm
which deals with the control of the false discovery rate or its modified version. Since bandit
algorithms have a very high best-arm discovery guarantee which in practice even exceeds its
theoretical guarantee of at least 1 α , mFDR and FDR plots on MAB-FDR directly do
j
−
not lead to very insightful plots - namely the constant 0 line. However, we can demonstrate
that even under adversarial conditions, i.e. when the P-value under the null is much less
concentrated around one than obtained via the best arm bandit algorithm, mFDR or the
false discovery proportion (FDP) in each run are still controlled at any time t as Theorem 1
guarantees. Albeit not exactly reflecting mFDR control in the case of MAB-FDR but in fact
in an even harder setting, results from these experiments can be regarded as valuable on their
own - it emphasizes the fact that Theorem 1 guarantees mFDR control independent of the
adaptive sampling algorithm and specific choice of p-value as long as it is always valid.
For Figure 6, we again consider Gaussian draws with the same settings as described in 4.1.
This time however, for each true null hypothesis we skip the bandit experiment and directly
Pj
draw [0,1] to compare with the significance levels α j from our online FDR procedure 2.
∼
As mentioned above, by Theorem 1, mFDR should still be controlled as it only requires
the p-values to be super-uniform. In Figure 6(a) we plot the instantaneous false discovery
(cid:80)
|     |     |     |     |     |     |     | j∈H0J | Rj  |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
proportion (number of false discoveries over total discoveries) FDP(J) = over the
|     |     |     |     |     |     |     | (cid:80)T | Rj  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- |
j=1
hypothesis index for different runs with the same settings. Apart from fluctuations in the
beginning due to the relatively small denominator, we can observe how the guarantee for
E
the FDR(J) = FDP(J), with its empirical value depicted by the red line, transfers to the
| control | of each | individual |     | run (blue | lines). |     |     |     |
| ------- | ------- | ---------- | --- | --------- | ------- | --- | --- | --- |
In Figure 6, we compare the mFDR (which in fact coincides with the FDR in this plot) of
MAB-FDR using different multiple testing procedures, including MAB-IND and a Bonferroni
(cid:80)∞
type correction. The latter uses a simple union bound and chooses α j such that α j α
j=1 ≤
14

0.20
0.15
0.10
0.05
0.00
0 200 400 600 800 1000
Hypothesis index
)J(PDF
0.5
0.4
0.3
0.2
0.1
0.0
0.1 0.3 0.5 0.7 0.9
Proportion of alternatives π 1
RDFm
MAB-LORD
MAB-IND
MAB-Bonf.
(a) (b)
Figure 6. (a) Single runs of MAB-LORD (blue) and their average (red) with uniformly
drawn p-values for null hypotheses and Gaussian draws for non-nulls with µ =8, ∆=3 and
i(cid:63)
T =200, 500 hypotheses with 200 true nulls and 30 arms, the desired mFDR level is α=0.1
S
(b)mFDRoverdifferentproportionsofnon-nullsπ ,withsamesettings,averagedover80runs.
1
and thus trivially allows for any time FWER, and thus FDR control. In our simulations we
use α = 6α . As expected, Bonferroni is too conservative and barely makes any rejections
j π2j2
whereas the naive MAB-IND approach does not control FDR. LORD avoids both extremes
and controls FDR while having reasonable power.
5 Proofs
In this section we provide the proofs of the main results in the paper.
5.1 Proof of Proposition 1
For any fixed γ (0,1), we have the equivalence
∈
γ γ
µ ϕ ( ) > µ +ϕ ( )+(cid:15) p γ.
(cid:98)i,ni(t) − ni(t) 2K (cid:98)0,n0(t) n0(t) 2 ⇐⇒ i,t ≤
If max µ µ +(cid:15), then we have
i 0
i=1,...,K ≤
(cid:32)K ∞ (cid:33)
(cid:91) (cid:91)(cid:110) (cid:111)
P µ ϕ ( γ ) > µ +ϕ ( γ )+(cid:15)
(cid:98)i,ni(t) − ni(t) 2K (cid:98)0,n0(t) n0(t) 2
i=1t=1
(cid:32)K ∞ (cid:33)
(cid:92) (cid:92)(cid:110) (cid:111)
= 1 P µ ϕ ( γ ) µ +ϕ ( γ )+(cid:15)
− (cid:98)i,ni(t) − ni(t) 2K ≤ (cid:98)0,n0(t) n0(t) 2
i=1t=1
(cid:32)∞ K ∞ (cid:33)
(cid:92)(cid:110) (cid:111) (cid:92) (cid:92)(cid:110) (cid:111)
1 P µ µ +ϕ ( γ ) µ ϕ ( γ ) µ
≤ − 0 ≤ (cid:98)0,t t 2 ∩ (cid:98)i,ni(t) − ni(t) 2K ≤ i
t=1 i=1t=1
(cid:32)∞ (cid:33) K (cid:32)∞ (cid:33)
(cid:91)(cid:110) (cid:111) (cid:88) (cid:91)(cid:110) (cid:111)
P µ > µ +ϕ ( γ ) + P µ ϕ ( γ ) > µ
≤ 0 (cid:98)0,t t 2 (cid:98)i,ni(t) − ni(t) 2K i
t=1 i=1 t=1
γ γ
+K = γ
≤ 2 2K
(cid:16) (cid:110) (cid:111)(cid:17)
by equation (4). Thus, we have P (cid:83)K (cid:83)∞ p γ γ, which completes the proof.
i=1 t=1 i,t ≤ ≤
15

| 5.2 | Proof |     | of Proposition |     |     | 2   |     |     |     |     |     |     |     |
| --- | ----- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Here we prove that the algorithm 1 terminates in finite time. The technical proof for sample
complexity is moved to the Appendix C. It suffices to argue for δ/2 0.1 and we discuss the
≤
| other | case | at the | end. |     |     |     |     |     |     |     |     |     |     |
| ----- | ---- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof of termination in finite time First we prove by contradiction that the algorithm
terminates in finite time with probability one for the case µ max µ (cid:15).
|     |     |     |     |     |     |     |     |     |     | 0   | i=1,...,K i |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | ≥   |             | −   |     |
Assuming that there exist runs for which the algorithm does not terminate, the set of
| arms | defined | by  |     |      |         |     |     |     |                     |       |        |     |     |
| ---- | ------- | --- | --- | ---- | ------- | --- | --- | --- | ------------------- | ----- | ------ | --- | --- |
|      |         |     |     | S := | i : LCB | (t) | UCB | (t) | (cid:15) infinitely | often | (i.o.) |     |     |
|      |         |     |     |      |         | 0   |     | i   |                     |       |        |     |     |
|      |         |     |     | {    |         | ≤   |     | −   |                     |       | }      |     |     |
is necessarily non-empty for these runs. We now show that this assumption yields a contra-
| diction | so  | that |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P(Algorithm does not terminate) P(LCB (t) max UCB (t) (cid:15) i.o.) = 0 (11)
|     |     |     |     |     |     |     |     | 0   |     |           | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
|     |     |     |     |     |     |     | ≤   |     | ≤   | i=1,...,K | −   |     |     |
First take note that by definition of the algorithm, if an arm i is drawn infinitely often
(i.o.), then so is the control arm 0 and we have LCB 0 (t) µ 0 as well as UCB i (t) µ i as
|     |     |     |     |     |     |     |     |     |     | →   |     |     | →   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t . Thisfollowsbythelawoflargenumberscombinedwiththefactthatϕ ,ϕ 0
|     |     |     |     |     |     |     |     |     |     |     |     | ni(t) n0(t) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
| →   | ∞   |     |     |     |     |     |     |     |     |     |     |             | →   |
as t , since ϕ 0 as n . Since for the null hypothesis we have µ > µ (cid:15), it
|         |      |     | n   |       |     |              |     |           |          |            |     | 0   | i   |
| ------- | ---- | --- | --- | ----- | --- | ------------ | --- | --------- | -------- | ---------- | --- | --- | --- |
|         | → ∞  |     |     | →     |     | → ∞          |     | t(cid:48) |          | t(cid:48). |     |     | −   |
| follows | that | LCB | (t) | > UCB | (t) | (cid:15) for | all | t         | for some |            |     |     |     |
|         |      |     | 0   |       | i   | −            |     | ≥         |          |            |     |     |     |
This argument implies that all arms i S can only be drawn a finite number of times, i.e.
∈
n (t) < for all i S. However, the fact that they are not drawn i.o. implies that h = i
| i   |     |     |     |     |     |     |     |     |     |     |     |     | t        |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
|     | ∞   |     |     | ∈   |     |     |     |     |     |     |     |     | (cid:54) |
and (cid:96) = i i.o. for all i S, so that there exists i(cid:48) S such that max UCB (t) UCB i(cid:48)(t)
|      | t             |     |     |      |      |        |     |                  |           |               | i∈S | i   |      |
| ---- | ------------- | --- | --- | ---- | ---- | ------ | --- | ---------------- | --------- | ------------- | --- | --- | ---- |
|      | (cid:54)      |     |     | ∈    |      |        |     |                  | (cid:54)∈ |               |     | ≤   |      |
| i.o. | By definition |     | of  | S we | then | obtain |     |                  |           |               |     |     |      |
|      |               |     |     |      |      | LCB 0  | (t) | UCB i(cid:48)(t) |           | (cid:15) i.o. |     |     | (12) |
|      |               |     |     |      |      |        | ≤   |                  | −         |               |     |     |      |
i(cid:48)
However, since S, inequality (12) cannot hold and equation (11) is proved.
(cid:54)∈
Anearlyidenticalargumenttotheaboveshowsthatthestoppingconditionismetinfinite
time.
| 5.3 | Proof |     | of Theorem |     | 1   |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We now turn to the proof of Theorem 1, splitting our argument into parts (a) and (b),
respectively.
| 5.3.1 | Proof |     | of part | (a) |     |     |     |     |     |     |     |     |     |
| ----- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In order for generalized alpha-investing procedures such as LORD to successfully control the
mFDR, it is sufficient that p-values under the null be conditionally super-uniform, meaning
| that | for | all j | ,   | we have |     |     |     |     |     |     |     |     |     |
| ---- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     | ∈   | H   |     |       |     |      |     |     |          |     |     |      |
| --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | -------- | --- | --- | ---- |
|     |     |     |     |     | P (Pj | α   | j−1) | α   | (R  | ,...,R ) |     |     | (13) |
|     |     |     |     |     | 0     |     | j    |     | j 1 | j−1      |     |     |      |
|     |     |     |     |     |       | ≤   | |F   | ≤   |     |          |     |     |      |
where j−1 is the σ-field induced by R ,...,R . Note that as long as condition (13) is
|     |     |     |     |     |     |     | 1   | j−1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | F   |     |     | Pj  |     |     |     |     |     |     |     |     |     |
satisfied, T j and thus could potentially depend on α j , i.e. the rejection indicator variables
P1,...,Pj−1.
R 1 ,...,R j−1 and potentially See Aharoni and Rosset [3] for further details.
16

It thus suffices to show that condition (13) holds for our definition of p-value in our
framework. We know that by Proposition 1 we have for any random stopping time, thus any
fixed truncation time M, that P (P j α ) α . We now show that the same bound also
0 T ≤ j ≤ j
holds for the (α -dependent) bandit stopping time T(α ), i.e. that P (P j α ) α .
j j 0 T(αj) ≤ j ≤ j
Under the null hypothesis, the best arm is at most (cid:15) better than the control arm, i.e.
µ > µ (cid:15), so that by Proposition 2 we have that with probability 1 α , i = 0, i.e.
0 i j b
− ≥ −
LCB (t) > UCB (t) (cid:15) for all i = 0. Hence, LCB (t) UCB (t) < (cid:15), and thus, by the
0 i i 0
− j (cid:54) −
definition of the p-values, P = 1 for all i with probability 1 α . It finally follows
i,T(αj) ≥ − j
that P (P j α ) α .
0 T(αj) ≤ j ≤ j
Putting things together, under the true null hypothesis (omitting the index j to
0
∈ H
simplify notation) we directly have that for any α
j
P
0
(P
T
j
j
(α
j
)
≤
α
j
) = P
0
(cid:0) P
T
j
(αj) ≤
α
j
(cid:12) (cid:12)T(α
j
)
≤
M (cid:1)P
0
(T(α
j
)
≤
M)
+P
0
(cid:0) P
M
j
≤
α
j
(cid:12) (cid:12)T(α
j
) > M (cid:1)P
0
(T(α
j
) > M)
α (P (T(α ) M)+P (T(α ) > M)) = α
j 0 j 0 j j
≤ ≤
for all fixed α even when the stopping time T(α ) is dependent on α . This is equivalent to
j j j
stating that for any sequence R ,...,R we have
1 j−1
P (Pj α (R ,...,R ) j−1) = P (P j α (R ,...,R ))
0 ≤ j 1 j−1 |F 0 T(αj(R1,...,Rj−1)) ≤ j 1 j−1
α (R ,...,R )
j 1 j−1
≤
and the proof is complete.
5.3.2 Proof of part (b)
Itsufficestoprovethatforasingleexperimentj andM = ,wehaveP (P j α ) 1 α
∞ 1 T(αj) ≤ j ≥ − j
where P is the distribution of a non-null experiment j. First observe that at stopping time
1
j j
T(α ) of Algorithm 1, either P α or P = 1 for all i. The former event happens
j i,T(αj) ≤ j i,T(αj)
whenever the algorithm exits with i (cid:63), i.e. when LCB (t) UCB (t) (cid:15) holds. Then,
b ∈ S i b ≥ (cid:96)t −
j
by definition of the p-value in equation (6) and (cid:96) we must have that P α . As a
t i b ,T(αj) ≤ j
consequence, by Proposition 2, we have
P (P j α ) P(P j α )
1 T(αj) ≤ j ≥ T(αj) ≤ j
P (Algorithm 1 exits withi (cid:63))
1 b
≥ ∈ S
1 α
j
≥ −
and the proof is complete.
6 Discussion
The recent focus in popular media about the lack of reproducibility of scientific results erodes
the public’s confidence in published scientific research. To maintain high standards of pub-
lished results and claimed discoveries, simply increasing the statistical significance standards
ofeachindividualexperimentalwork(e.g., rejectatlevel0.001ratherthan0.05)woulddrasti-
cally hurt power. We take the alternative approach of controlling the ratio of false discoveries
17

to claimed discoveries at some desired value (e.g., 0.05) over many sequential experiments.
Thismeansthatthestatisticalsignificanceforvalidatingadiscoverychangesfromexperiment
to experiment, and could be larger or smaller than 0.05, requiring less or more data to be
collected. Unlike earlier works on online FDR control, our framework synchronously inter-
acts with adaptive sampling methods like MABs over uniform sampling to make the overall
sampling procedure as efficient as possible. We do not know of other works in the literature
combining the benefits of adaptive sampling and FDR control. It should be clear that any
improvement, theoretical or practical, to either online FDR algorithms or best-arm identifi-
cation in MAB (or their variants), immediately results in a corresponding improvement for
our MAB-FDR framework.
More general notions of FDR with corresponding online procedures have recently been
developed by Ramdas et al [14]. In particular, they incorporate the notion of memory and
a priori importance of each hypothesis. This could prove to be a valuable extension for our
setting, especially in cases when only the percentage of wrong rejections in the recent past
matters. It would be useful to establish FDR control for these generalized notions of FDR as
well.
There are several directions that could be explored in future work. First, it would be
interesting to extend the MAB aspect (in which each arm is univariate) of our framework
to more general settings. Balasubramani and Ramdas [7] show how to construct sequential
tests for many multivariate nonparametric testing problems, using LIL confidence intervals,
which can again be inverted to provide always valid p-values. It might be of interest to
marry the ideas in our paper with theirs. For example, the null hypothesis might be that
the control arm has the same (multivariate) mean as other arms (K-sample testing), and
under the alternative, we would like to pick the arm whose mean is furthest away from the
control. A more complicated example could involve dependence, where we observe pairs of
arms, and the null hypothesis is that the rewards in the control arm are independent of the
alternatives, and if the null is false we may want to pick the most correlated arm. The work
by Zhao et al. [15] on tightening LIL-bounds could be practically relevant. Recent work on
sequential p-values by Malek et al. [16] also naturally fit into our framework. Lastly, in this
work we treat samples or pulls from arms as identical from a statistical perspective; it might
be of interest in subsequent work to extend our framework to the contextual bandit setting,
in which the samples are associated with features to aid exploration.
Acknowledgements
This work was partially supported by Office of Naval Research MURI grant DOD-002888,
Air Force Office of Scientific Research Grant AFOSR-FA9550-14-1-001, and National Science
Foundation Grants CIF-31712-23800 and DMS-1309356.
References
[1] Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate: a practical and
powerful approach to multiple testing,” Journal of the Royal Statistical Society. Series
B (Methodological), pp. 289–300, 1995.
[2] D. P. Foster and R. A. Stine, “α-investing: a procedure for sequential control of ex-
pected false discoveries,” Journal of the Royal Statistical Society: Series B (Statistical
Methodology), vol. 70, no. 2, pp. 429–444, 2008.
18

[3] E. Aharoni and S. Rosset, “Generalized α-investing: definitions, optimality results and
application to public databases,” Journal of the Royal Statistical Society: Series B (Sta-
| tistical | Methodology), |     | vol. | 76, no. | 4, pp. | 771–794, | 2014. |     |     |
| -------- | ------------- | --- | ---- | ------- | ------ | -------- | ----- | --- | --- |
[4] A. Javanmard and A. Montanari, “Online rules for control of false discovery rate and
|                 |     |              |     | The | Annals | of Statistics, |     |       |     |
| --------------- | --- | ------------ | --- | --- | ------ | -------------- | --- | ----- | --- |
| false discovery |     | exceedance,” |     |     |        |                |     | 2017. |     |
[5] R. Johari, L. Pekelis, and D. J. Walsh, “Always valid inference: Bringing sequential
| analysis | to A/B | testing,” |     | arXiv preprint |     | arXiv:1512.04922, |     | 2015. |     |
| -------- | ------ | --------- | --- | -------------- | --- | ----------------- | --- | ----- | --- |
[6] K. G. Jamieson, M. Malloy, R. D. Nowak, and S. Bubeck, “lil’UCB: An optimal explo-
ration algorithm for multi-armed bandits,” in COLT, vol. 35, 2014, pp. 423–439.
[7] A. Balsubramani and A. Ramdas, “Sequential nonparametric testing with the law of the
iterated logarithm,” in Proceedings of the Thirty-Second Conference on Uncertainty in
| Artificial | Intelligence. |     | AUAI | Press, | 2016, | pp. | 42–51. |     |     |
| ---------- | ------------- | --- | ---- | ------ | ----- | --- | ------ | --- | --- |
[8] E. Kaufmann, O. Capp´e, and A. Garivier, “On the complexity of best arm identification
in multi-armed bandit models,” The Journal of Machine Learning Research, 2015.
[9] K. Jamieson and R. Nowak, “Best-arm identification algorithms for multi-armed bandits
in the fixed confidence setting,” in Information Sciences and Systems (CISS), 2014 48th
| Annual | Conference |     | on. IEEE, | 2014, | pp. | 1–6. |     |     |     |
| ------ | ---------- | --- | --------- | ----- | --- | ---- | --- | --- | --- |
[10] S. S. Villar, J. Bowden, and J. Wason, “Multi-armed bandit models for the optimal
design of clinical trials: benefits and challenges,” Statistical science: a review journal of
| the Institute |     | of Mathematical |     | Statistics, |     | vol. 30, | no. 2, | p. 199, 2015. |     |
| ------------- | --- | --------------- | --- | ----------- | --- | -------- | ------ | ------------- | --- |
[11] S.Kalyanakrishnan, A.Tewari, P.Auer, andP.Stone, “Pacsubsetselectioninstochastic
multi-armed bandits,” in Proceedings of the 29th International Conference on Machine
| Learning | (ICML-12), |     | 2012, | pp. 655–662. |     |     |     |     |     |
| -------- | ---------- | --- | ----- | ------------ | --- | --- | --- | --- | --- |
[12] M. Simchowitz, K. Jamieson, and B. Recht, “The simulator: Understanding adaptive
sampling in the moderate-confidence regime,” arXiv preprint arXiv:1702.05186, 2017.
[13] A. Javanmard and A. Montanari, “On online control of false discovery rate,” arXiv
| preprint | arXiv:1502.06197, |     |     | 2015. |     |     |     |     |     |
| -------- | ----------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
[14] A. Ramdas, F. Yang, M. J. Wainwright, and M. I. Jordan, “Online control of the false
|           |        |       |          |          |                   | Advances |     | in Neural Information | Processing |
| --------- | ------ | ----- | -------- | -------- | ----------------- | -------- | --- | --------------------- | ---------- |
| discovery | rate   | with  | decaying | memory,” |                   | in       |     |                       |            |
| Systems   | (NIPS) | 2017, | arXiv    | preprint | arXiv:1710.00499, |          |     | 2017.                 |            |
[15] S. Zhao, E. Zhou, A. Sabharwal, and S. Ermon, “Adaptive concentration inequalities for
sequential decision problems,” in Advances In Neural Information Processing Systems,
| 2016, pp. | 1343–1351. |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] A. Malek, Y. Chow, M. Ghavamzadeh, and S. Katariya, “Sequential multiple hypothesis
testing with type I error control,” in The 20th International Conference on Artificial
| Intelligence | and | Statistics, |     | 2017, | 2017, pp. | 1343–1351. |     |     |     |
| ------------ | --- | ----------- | --- | ----- | --------- | ---------- | --- | --- | --- |
19

A Notation
| Notation |     | Terminology |     | and | explanation |     |     |     |     |     |
| -------- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- |
MAB (pure exploration for best-arm identification in) multi-armed bandits
FDR(J) the expected ratio of # false discoveries to # discoveries up to experiment J
mFDR(J) the ratio of expected # false discoveries to expected # discoveries
α target for FDR or mFDR control after any number of experiments
BDR(J) the best arm discovery rate (generalization of test power)
(cid:15)BDR(J) the (cid:15)-best arm discovery rate (softer metric than BDR)
LCB,UCB the lower and upper confidence bounds used in the best-arm algorithms
N
| j   |     | experiment |     | counter | (number |     | of MAB | instances) |     |     |
| --- | --- | ---------- | --- | ------- | ------- | --- | ------ | ---------- | --- | --- |
∈
| T N |     | stopping | time | for | the | j-th experiment |     |     |     |     |
| --- | --- | -------- | ---- | --- | --- | --------------- | --- | --- | --- | --- |
j
∈
P j ,P [0,1] always valid p-value after time t (in experiment j, explicit or implicit)
t t
∈
Pj always valid p-value for experiment j at its stopping time T
j
Pj, j−1
α [0,1] threshold set by the online FDR algorithm for using p
| j ∈ |     |     |     |     |     |     |     |     | { i }i=1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
N
T(α j ) stopping time for the j-th experiment, when experiment uses α j
∈
| 0   |     | the control |     | or default |     | arm |     |     |     |     |
| --- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
1,...,K K = K(j) alternatives or treatment arms (experiment j implicit)
| {               | }   |          |         |           |           |       |              |             |     |     |
| --------------- | --- | -------- | ------- | --------- | --------- | ----- | ------------ | ----------- | --- | --- |
| i 0,...,K       |     | K +1     | options | or        | “all      | arms” |              |             |     |     |
| ∈ {             | }   |          |         |           |           |       |              |             |     |     |
| i (cid:63) ,i b |     | the best | of      | all arms, | and       | the   | arm returned | by MAB      |     |     |
| µ ,µ            |     | the mean | of      | the       | i-th arm, | and   | the mean     | of the best | arm |     |
i ∗
N
t,n (t) total number of pulls, number of times arm i is pulled up to time t
i
∈
|         |     | Table | 1:  | Common  | notation |     | used throughout | the | paper. |     |
| ------- | --- | ----- | --- | ------- | -------- | --- | --------------- | --- | ------ | --- |
| B Notes | on  | FDR   |     | control |          |     |                 |     |        |     |
We can prove FDR control for our framework using the specific online FDR procedure called
LORD ’15 introduced in [13]. When used in Procedure 2, the only adjustment that needs to
be made is to reset W(j+1) to α in step 2 after every rejection, yielding α = αγ for any
|     |     |     |     |           |     |     |     |     | j j − τj |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | -------- | --- |
|     | ∞   |     |     | (cid:80)∞ |     |     |     |     |          |     |
sequence γ j such that γ j = 1. We call the adjusted procedure MAB- L O RD’ for
|     | { }j=1 |     |     | j=1 |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
short.
Theorem 2 (Online FDR control for MAB-LORD). (a) MAB-LORD’ achieves mFDR and
FDR control at a specified level α for stopping times T = min T(α ),M .
|                  |     |       |       |     |             |     |           | j   | j   |     |
| ---------------- | --- | ----- | ----- | --- | ----------- | --- | --------- | --- | --- | --- |
|                  |     |       |       |     |             |     |           |     | { } |     |
| (b) Furthermore, |     | if we | set M | =   | , MAB-LORD’ |     | satisfies |     |     |     |
∞
|     |     |     |     |     |                |     | (1    | α)  |     |      |
| --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | --- | ---- |
|     |     |     |     |     | (cid:15)BDR(J) |     | −     | .   |     | (14) |
|     |     |     |     |     |                |     | ≥ (J) |     |     |      |
|     |     |     |     |     |                |     | |H 1  | |   |     |      |
Note that LORD as in [13] is less powerful than in [4] since the values α in the former
j
can be much smaller than those in [4], which could in fact exceed the level α. Therefore, for
| FDR control | we  | currently | do  | have | to sacrifice | some | power. |     |     |     |
| ----------- | --- | --------- | --- | ---- | ------------ | ---- | ------ | --- | --- | --- |
Proof. We leverage the proposition that can be obtained from a slightly more careful analysis
| of the procedure |     | than | in [13]. |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
20

P
Proposition 3. If (Pj α τ ) α , i.e. the distribution of the p values under the
|     |     | 0   |     | j   | j   | j   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | ≤   | |   | ≤   |     |     |     |     |     | −   |     |     |
null are superuniform conditioned on the last rejection, using the online LORD’15 procedure
| controls | the FDR | at each | t.  |     |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Note that this proposition allows online FDR control for any, possibly dependent, p-
values which are conditionally superuniform. This condition is not equivalent to (13) in
general, it is in fact less restrictive since the probability is conditioned only on a function
τ = max k j : R = 1 of all past rejections. Formally, the sigma algebra induced by
| (cid:101)j |     | k   |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|            | { ≤ |     | }   |     |     |     |     |     |     |     |     |     |     |
τ is contained in j−1 and hence P (Pj α τ ) P (Pj α R ,...,R ) by the
| j−1 |     |     |     |     | 0   |     | j j−1 |     | 0   | j   | 1   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     | F   |     |     |     | ≤   | |     | ≤   |     | ≤   | |   |     |     |
tower property. Finally, utilizing the fact that our p-values are conditionally super-uniform as
proven in Section 5.3.1, i.e. inequality (13) holds, the condition for Proposition 3 is fulfilled
| and the   | proof is | complete.   |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.1 Proof | of       | Proposition |     | 3   |     |     |     |     |     |     |     |     |     |
Let τ denote the time of the i-th rejection with τ = 0 (note that this is different from τ ).
| (cid:101)i |     |     |     |     |     |     | (cid:101)0 |     |     |     |     |     | j   |
| ---------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(cid:80)t
and define k(t) = R . Let H be the j th hypothesis that was rejected. We adjust an
|          |            | j=1 | j   |     | j   | −   |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| argument | from [13]. |     |     |     |     |     |     |     |     |     |     |     |     |
First observe that k(t) = (cid:96) = τ t,τ > t and FDP(t) = FDP(τ ) so that
|     |     |     |     |     | (cid:101)(cid:96) | (cid:101)(cid:96)+1 |     |     |     |     | (cid:101)k(t) |     |     |
| --- | --- | --- | --- | --- | ----------------- | ------------------- | --- | --- | --- | --- | ------------- | --- | --- |
|     |     | {   |     | }   | { ≤               |                     | }   |     |     |     |               |     |     |
(cid:80)
|         |        |     |     | t        |               | R   |      |                   |     |           |     |     |     |
| ------- | ------ | --- | --- | -------- | ------------- | --- | ---- | ----------------- | --- | --------- | --- | --- | --- |
| EFDP(t) | EFDP(τ |     |     | (cid:88) | E(cid:2) j∈H0 | j   |      | (cid:3)           |     |           |     |     |     |
|         | =      |     | )   | =        |               |     | k(t) | = (cid:96) P(k(t) | =   | (cid:96)) |     |     |     |
k(t)
|     |     |     |     |     |     | (cid:96) | |   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:96)=1
|     | t          |        |             | (cid:96) |                  |                    |            |         |     |         |     |     |         |
| --- | ---------- | ------ | ----------- | -------- | ---------------- | ------------------ | ---------- | ------- | --- | ------- | --- | --- | ------- |
|     | (cid:88)   |        |             | (cid:88) | 1                |                    |            |         |     |         |     |     |         |
|     |            |        |             |          | E(cid:2) Hi∈H0   |                    |            | (cid:3) |     |         |     |     |         |
|     | =          | P(k(t) | = (cid:96)) |          |                  | k(t)               | = (cid:96) |         |     |         |     |     |         |
|     |            |        |             |          | (cid:96)         | |                  |            |         |     |         |     |     |         |
|     | (cid:96)=1 |        |             | i=1      |                  |                    |            |         |     |         |     |     |         |
|     | t          |        |             | (cid:96) | (cid:80)τ        |                    | 1          |         |     |         |     |     |         |
|     | (cid:88)   |        |             | (cid:88) |                  | (cid:101)i         | R j        | j∈H0    |     |         |     |     |         |
|     |            |        |             |          | E(cid:2)E(cid:0) | j=τ (cid:101)i−1+1 |            |         |     | (cid:1) |     |     | (cid:3) |
= P(k(t) = (cid:96)) τ (cid:101)0 ,...,τ (cid:101)i−1 τ (cid:101)(cid:96) t,τ (cid:101)(cid:96)+1 > t
|     |            |     |     |     |     |     | (cid:96) | |   |     |     | | ≤ |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|     | (cid:96)=1 |     |     | i=1 |     |     |          |     |     |     |     |     |     |
Since for the LORD ’15 procedure, we have α = γ , and thus for all positive integers
|     |     |     |     |     |     |     | t   | t−τt |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
i, the random variables R j with j τ (cid:101)i−1 are conditionally independent of τ (cid:101)0 ,...,τ (cid:101)i−2 given
≥
τ . Additionally noting that τ = τ for all j τ by definition of τ and τ, using
| (cid:101)i−1 |     |     |     | (cid:101)i−1 |     | j   |     | (cid:101)i−1 |     |     | (cid:101) |     |     |
| ------------ | --- | --- | --- | ------------ | --- | --- | --- | ------------ | --- | --- | --------- | --- | --- |
≥
| E (1    | τ ) | α we | obtain |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 pj≤αj | j   | j    |        |     |     |     |     |     |     |     |     |     |     |
| ≤
|     | (cid:80) |                     |                         |     |                     |              |                  | (cid:80)τ           |          | 1    |                |         |     |
| --- | -------- | ------------------- | ----------------------- | --- | ------------------- | ------------ | ---------------- | ------------------- | -------- | ---- | -------------- | ------- | --- |
|     |          |                     | (cid:101)i](cid:84)j∈H0 | R   |                     |              |                  | (cid:101)i          | R        | j    |                |         |     |
|     | E(cid:0) | j∈(τ (cid:101)i−1,τ |                         | j   |                     |              | (cid:1) E(cid:0) | j =τ (cid:101)i−1+1 |          | j∈H0 |                | (cid:1) |     |
|     |          |                     |                         |     | τ (cid:101)0 ,...,τ | (cid:101)i−1 | =                |                     |          |      | τ (cid:101)i−1 |         |     |
|     |          |                     | (cid:96)                |     | |                   |              |                  |                     | (cid:96) |      | |              |         |     |
|     |          |                     |                         |     |                     |              | (cid:80)τi       |                     | 1        | E[R  |                |         |     |
|     |          |                     |                         |     |                     |              |                  |                     | j∈H0     |      | j τ j ]        |         |     |
|     |          |                     |                         |     |                     |              |                  | j=τi−1+1            |          |      | |              |         |     |
|     |          |                     |                         |     |                     |              | ≤                |                     | (cid:96) |      |                |         |     |
(cid:80)τ
|     |     |     |     |     |     |     |     | i   | α j | α   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j =τi−1+1
.
|     |     |     |     |     |     |     | ≤   | (cid:96) | ≤   | (cid:96) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
The last inequality follows since between any two rejection times τ ,τ , we have
k k+1
|     |     |     |     |     | τ            |          | ∞   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | (cid:88) k+1 | (cid:88) |     |     |     |     |     |     |     |
|     |     |     |     |     | α            | i α      | γ i | α.  |     |     |     |     |     |
|     |     |     |     |     |              | ≤        | ≤   |     |     |     |     |     |     |
|     |     |     |     |     | i=τ k        | i=1      |     |     |     |     |     |     |     |
(cid:80)t
| Since | P(k(t) | = (cid:96)) | = 1 it | follows | that | FDR | control | is obtained. |     |     |     |     |     |
| ----- | ------ | ----------- | ------ | ------- | ---- | --- | ------- | ------------ | --- | --- | --- | --- | --- |
(cid:96)=1
21

C Proof of sample complexity for Proposition 2
In the sequel we use (cid:38), for inequality and equality up to constant factors.
∼
Define i = argmax µ (breaking ties arbitrarily) and n (t) to be the number of
(cid:63) i=0,1,...,K i i
times sample i was drawn until time t. For any i 0,1,...,K and η R we define the
∈ { } ∈
following key quantity
τ (η,ξ) := min n N : 2ϕ ( δ ) < max η µ ,ξ (15)
i { ∈ n 2K {| − i | }}
(cid:46) min (cid:8) (η µ )−2log(Klog(η µ )−2)/δ),ξ−2log(Klog(ξ−2)/δ) (cid:9)
i i
− −
where we set τ (µ ,0) = , but this case does not arise in our analysis.
i i
∞
Let us define the events
∞
(cid:92)
= µ µ ϕ ( δ ) .
E i {| (cid:98)i,n − i | ≤ n 2K }
n=1
(cid:16) (cid:17)
By a union bound and the LIL bound in (4), we have for δ/2K < 0.1 that P (cid:83)K c
i=0Ei ≤
K+1δ δ for K 2. For δ > 0.1, note that for all δ(cid:48) < δ we have ϕ (δ(cid:48)) ϕ (δ) so that
2K ≤ ≥ 2K n ≤ n
P( c) = P(ϕ ( δ ) < µ µ )
E i n 2K (cid:98)i,n − i
P(ϕ (0.1) < µ µ ) δ i = 1,...,K
≤ n (cid:98)i,n − i ≤ 2K ∀
Throughout the rest of the proof we assume the events hold.
i
E
The following simple lemma regarding the key quantity τ will be used throughout the
i
proof.
Lemma 1. Fix i 0,1,...,K and η > 0. For any t N, whenever n (t) τ (η,ξ) we
i i
∈ { (cid:84) } ∈ ≥
have that under the event , we have
i=0,...,KE i
UCB (t) max η,µ +ξ if η µ
i i i
≤ { } ≥
LCB (t) min η,µ ξ if η µ
i i i
≥ { − } ≤
Proof. Assume n (t) τ (η,ξ). If η µ we have by definition of that
i i i i
≥ ≥ E
UCB (t) = µ +ϕ (δ) µ +2ϕ ( δ ) < µ +max η µ ,ξ
i (cid:98)i,ni(t) ni(t) 2 ≤ i ni(t) 2K i { − i }
and if η µ
i
≤
LCB (t) = µ ϕ ( δ ) µ 2ϕ ( δ ) > µ max µ η,ξ = µ +min η µ , ξ
i (cid:98)i,ni(t) − ni(t) 2K ≥ i − ni(t) 2K i − { i − } i { − i − }
C.1 Proof of Proposition 2 (a) µ > max µ (cid:15)
0 i
i=1,...,K −
Ateachtimetwhichdoesnotsatisfythestoppingcondition,arm0andargmax UCB (t)
i=1,...,K i
are pulled. Note that by Lemma 1
µ0+( max µi−(cid:15)) µ0+( max µi−(cid:15)) µ0+( max µi−(cid:15))
n (t) τ ( i=1,...,K ,0) = LCB (t) min i=1,...,K ,µ i=1,...,K
{ 0 ≥ 0 2 } ⇒ 0 ≥ { 2 0 } ≥ 2
(16)
22

so that t > n (t) makes sure that there were enough draws for the particular arm 0 (since it’s
0
drawn every time). For i = 0 we have
(cid:54)
(µ0+(cid:15))+ max µi (µ0+(cid:15))+ max µi (µ0+(cid:15))+ max µi
n (t) τ ( i=1,...,K ,0) = UCB (t) max i=1,...,K ,µ i=1,...,K .
{ i ≥ i 2 } ⇒ i ≤ { 2 i } ≤ 2
(17)
(cid:80)K
which makes t > n (t) a necessary condition.
i=0 i
Reversely whenevert > (cid:80)K n (t), forall armsi = 0we have UCB (t)
(µ0+(cid:15))+
i=
m
1,
a
..
x
.,K
µi
.
i=0 i (cid:54) i ≤ 2
In essence, once arm i has been sampled n (t) times, because of (17), it will not be sampled
i
again - either, because all of the other UCB (t) satisfy the same upper bound, the algorithm
i
(µ0+(cid:15))+ max µi
will have stopped, or, if for some i we have UCB (t) > i=1,...,K that will be the arm
i 2
that is drawn. Thus,
µ0+( max µi−(cid:15)) (cid:88) K (µ0+(cid:15))+ max µi
t B (µ,δ) := τ ( i=1,...,K ,0)+ τ ( i=1,...,K ,0)
{ ≥ 1 0 2 i 2 }
i=1
= LCB (t) UCB (t) (cid:15) i = 0 ,
0 i
⇒ { − ≥ − ∀ (cid:54) }
i.e., thestoppingconditionismet, wherethefirsttermaccountsforsatisfying (16), thesecond
term accounts for satisfying (17) for all i = 0, and the third term accounts for satisfying
(cid:54)
Equation (18). Denoting T(δ) as the stopping time of the algorithm, this implies that with
probability at least 1 δ, we have T(δ) B (µ,δ) and arm 0 is returned.
1
− ≤
Let us now simplify the expression to make it more accessible to the reader and arrive at
the theorem statement. Defining ∆(cid:101)i := max η µ
i
,ξ as the effective gap in the definition
{| − | }
of τ (η,ξ) in Equation (15), it is straightforward to verify that the effective gap associated
i
with arm 0 is equal to
∆(cid:101)0 (µ
0
+(cid:15)) max µ
j
,
∼ −j=1,...,K
and the effective gap for any other arm i is equal to
∆(cid:101)i (cid:38) (µ
0
+(cid:15)) µ
i
.
−
Usingthesequantities,wecanseethattheupperboundB
1
(µ,δ)scaleslike (cid:80)K
i=0
∆(cid:101) −
i
2log(Klog(∆(cid:101) −
i
2)/δ).
C.2 Proof of Proposition 2 (b) max µ = µ > µ +(cid:15)
i i(cid:63) 0
i=1,...,K
At each time t which does not satisfy the stopping condition, arm 0 is pulled. Note again
that by Lemma 1
(µ (cid:15))+µ
n (t) τ (
(µi(cid:63) −(cid:15))+µ0,0)
= UCB (t) max
(µi(cid:63) −(cid:15))+µ0,µ i(cid:63)
−
0
.
{ 0 ≥ 0 2 } ⇒ 0 ≤ { 2 0 } ≤ 2
The following claim is key to proving this case (where u (0,1) be an absolute constant
∈
to be defined later).
Claim 1. Under the event (cid:84) , for any u 2 and µ¯ [max µ ,µ ], we have
i=0,...,KE i ≤ 7 ∈ j(cid:54)=i(cid:63) j i(cid:63)
K K
(cid:88) (cid:88)
s 2 τ (µ¯,u(cid:15)) : LCB (s) µ 5u(cid:15) or UCB (s) µ +u(cid:15) < τ (µ¯,u(cid:15)) (18)
|{ ≥ i hs ≤ i(cid:63) − 2 (cid:96)s ≥ i(cid:63) }| i
i=0 i=0
23

The proof of this claim can be found in Appendix C.3. Note that for all s we have that
LCB (s) µ 5u(cid:15) and UCB (s) µ +u(cid:15) = LCB (s) UCB (s) (cid:15).
hs ≥ i(cid:63) − 2 (cid:96)s ≤ i(cid:63) ⇒ hs ≥ (cid:96)s −
(cid:80)K
Intuitivelytheinequality(18)thuslimitsthenumberoftimesthatfort 2 τ (µ¯,u(cid:15)),the
≥ i=0 i
criterion LCB (s) UCB (s) (cid:15) is not fulfilled. We refer to the times when the condition
hs
≥
(cid:96)s
−
on the left hand side of inequality (18) is fulfilled, as “good” times.
Applying Claim 1 with µ¯ = max
µi(cid:63) +µj
and u =
µi(cid:63) −(µ0+(cid:15))
we then observe that on
j(cid:54)=i(cid:63) 2 5(cid:15)
the “good” times, we have
µ +(µ +(cid:15)) (µ (cid:15))+µ
LCB µ 5u(cid:15) = i(cid:63) 0 = i(cid:63) − 0 +(cid:15),
ht ≥ i(cid:63) − 2 2 2
so that we directly obtain that with probability at least 1 δ,
−
K
T(δ) B (µ,δ) := τ ( (µi(cid:63) −(cid:15))+µ0,0)+3 (cid:88) τ (max µi(cid:63) +µj,min 2(cid:15), µi(cid:63) −(µ0+(cid:15)) ).
≤ 2 0 2 i j(cid:54)=i(cid:63) 2 {7 5 }
i=0
Let us now simplify the expression. It is straightforward to verify that the effective gap
associated with arm 0 is equal to
(cid:26) (cid:26) (cid:27)(cid:27)
∆(cid:101)0 (cid:38) min µi(cid:63) −(
2
µ0+(cid:15)) ,max m
j(cid:54)=
a
i
x
(cid:63)
µi(cid:63)
2
+µj
−
µ
0
, 2
7
(cid:15)
(cid:26) (cid:27)
4
(cid:38) min µ (µ +(cid:15)),max ∆ , (cid:15)
i(cid:63)
−
0
{
0
7 }
and the effective gap for any other arm i is equal to
(cid:26) (cid:27)
∆(cid:101)i = max
|
m
j(cid:54)=
a
i
x
(cid:63)
µi(cid:63)
2
+µj
−
µ
i |
,min
{
2
7
(cid:15), µi(cid:63) −(
5
µ0+(cid:15))
}
(cid:38) max ∆ ,min µ (µ +(cid:15)),(cid:15)
{
i
{
i(cid:63)
−
0
}}
where we recall that ∆ = µ µ if i = i , and ∆ = µ max µ otherwise.
i i(cid:63)
−
i
(cid:54)
(cid:63) i(cid:63) i(cid:63)
−
j(cid:54)=i(cid:63) j
Using these quantities, the upper bound B (µ,δ) on the stopping time T(δ) scales like
2
(cid:80)K ∆(cid:101) −2log(Klog(∆(cid:101) −2)/δ). This concludes the proof of the proposition.
i=0 i i
C.3 Proof of Claim 1
Let µ¯ [max µ ,µ ] and τ := τ (µ¯,u(cid:15)). The following result is a a key ingredient for the
∈
j(cid:54)=i(cid:63) j i(cid:63) i i
proof of the claim.
Proposition 4. For any time t and u 1/2,
≤
K
(cid:110) (cid:88) (cid:111)
s t : h = i τ
s (cid:63) i
|{ ≤ }| ≥
i=0
= UCB (t) µ¯+u(cid:15) LCB (t) µ¯ u(cid:15)
⇒ {
(cid:96)t
≤ }∩{
ht
≥ − }
= LCB (t) UCB (t) (cid:15) .
⇒ {
ht
−
(cid:96)t
≥ − }
Proof. If h = i then some i = i is assigned to (cid:96) and UCB (s) max µ¯,µ +u(cid:15) µ¯+u(cid:15)
s (cid:63) (cid:63) s i i
(cid:54) ≤ { } ≤
whenever n (s) τ (µ¯,u(cid:15)). Because (cid:96) is the highest upper confidence bound, the sum over
i i s
≥
all τ represents exhausting all arms (i.e., pigeonhole principle). An analogous result holds for
i
LCB (t).
i(cid:63)
24

A direct consequence of Proposition 4 is that even though we don’t know which arm will
be assigned to h at any given time t, we do know that if h = i for a sufficient number of
t t (cid:63)
(cid:80)K
times, namely τ times, the termination criteria will be met. Thus, assume h = i and
i=0 i t (cid:54) (cid:63)
note that
h = i, µ < µ 5u(cid:15), µ min µ¯,µ 3u(cid:15)
{ t i i(cid:63) − 2 (cid:98)i,ni(t) ≥ { i(cid:63) − 2 }}
= min µ¯,µ 3u(cid:15) µ µ +ϕ ( δ )
⇒ { i(cid:63) − 2 } ≤ (cid:98)i,ni(t) ≤ i ni(t) 2K
= n (t) < τ
i i
⇒ { }
where the last line follows from µ + ϕ ( δ ) < min µ¯,µ + u(cid:15) min µ¯,µ 3u(cid:15)
i ni(t) 2K { i } ≤ { i(cid:63) − 2 }
(cid:80)K
whenever n (t) τ . Furthermore, the following Proposition 5, says for t 2 τ we have
i ≥ i ≥ i=0 i
that µ min µ¯,µ 3u(cid:15) .
(cid:98)ht,n ht (t) ≥ { i(cid:63) − 2 }
Proposition 5. For any time t,
K
(cid:88)
t 2 τ = µ min µ¯,µ 3u(cid:15) .
{ ≥ i } ⇒ { (cid:98)ht,n ht (t) ≥ { i(cid:63) − 2 }}
i=0
The proof of the proposition can be found in Section C.4.
Combining this fact with the display immediately above and the observation that some
i = h , we have that s 2 (cid:80)K τ : µ µ 5u(cid:15) < (cid:80)K τ . Now, on one of these
t |{ ≥ i=0 i i(cid:63) − hs ≥ 2 }| i=0 i
times t such that h = i,n (t) τ ,µ µ < 5u(cid:15) , we have
{ t i ≥ i i(cid:63) − i 2 }
LCB (t) = µ ϕ ( δ ) µ 2ϕ ( δ ) min µ¯,µ u(cid:15) µ 5u(cid:15).
i (cid:98)i,ni(t) − ni(t) 2K ≥ i − ni(t) 2K ≥ { i − } ≥ i(cid:63) − 2
The above display with the next proposition completes the proof of Equation 18.
Proposition 6. For any time t,
K
(cid:88)
t τ = max UCB (t) µ +u(cid:15) .
{ ≥
i
} ⇒ {i=0,1,...,K
i
≤
i(cid:63)
}
i=0
Proof. Note that
UCB (t) µ +u(cid:15) = µ +u(cid:15) UCB (t) = µ +ϕ (δ) µ +2ϕ ( δ )
{ i ≥ i(cid:63) } ⇒ { i(cid:63) ≤ i (cid:98)i,ni(t) ni(t) 2 ≤ i ni(t) 2K }
= n (t) < τ
i i
⇒ { }
sinceµ +2ϕ ( δ ) < max µ¯,µ +u(cid:15) µ +u(cid:15)whenevern (t) τ . Now, becauseateach
i ni(t) 2K { i } ≤ i(cid:63) i ≥ i
time t, the arm argmax UCB (t) is pulled because it is either h or (cid:96) , we conclude
j=0,1,...,K j t t
that this arm can only be pulled τ times before satisfying UCB (t) µ +u(cid:15).
i i
≤
i(cid:63)
C.4 Proof of Proposition 5
The above proposition implies,
K (cid:40) K (cid:41)
(cid:88) (cid:88)
t 2 τ = s t : h = i τ .
i s (cid:63) i
{ ≥ } ⇒ |{ ≤ (cid:54) }| ≥
i=0 i=0
25

Now consider the event
h = i ,(cid:96) = i = µ µ +ϕ (δ) µ +ϕ (δ) µ +2ϕ ( δ )
{ t (cid:54) (cid:63) t } ⇒ i(cid:63) ≤ (cid:98)i(cid:63),ni(cid:63) (t) ni(cid:63) (t) 2 ≤ (cid:98)i,ni(t) ni(t) 2 ≤ i ni(t) 2K
= µ µ 2ϕ ( δ )
⇒ { i(cid:63) − i ≤ ni(t) 2K }
= n (t) < τ n (t) τ ,µ µ 2ϕ ( δ )
⇒ { i i }∪{ i ≥ i i(cid:63) − i ≤ ni(t) 2K }
= n (t) < τ n (t) τ ,µ µ max µ¯ µ ,u(cid:15)
⇒ {
i i
}∪{
i
≥
i i(cid:63)
−
i
≤ {| −
i
| }}
= n (t) < τ n (t) τ ,µ µ < u(cid:15) n (t) τ ,i = i
⇒ {
i i
}∪{
i
≥
i i(cid:63)
−
i
}∪{
i
≥
i (cid:63)
}
by the definition of τ . Because at each time s t we have that some i = (cid:96) , if s t : h =
i s s
(cid:80)K ≤ |{ ≤ (cid:54)
i τ , we have that
(cid:63) }| ≥ i=0 i
K
(cid:88)
t 2 τ = i : n (t) τ and µ µ < u(cid:15) n (t) τ and i = i .
{ ≥
i
} ⇒ {∃
i
≥
i i(cid:63)
−
i
}∪{
i
≥
i (cid:63)
}
i=0
We use the fact that such an (cid:96) = i = i exists that satisfies µ µ < u(cid:15) to say
t
(cid:54)
(cid:63) i(cid:63)
−
i
i = i : µ µ ϕ ( δ ) µ max µ µ ,u(cid:15) /2 µ 3u(cid:15)
∃ (cid:54) (cid:63) (cid:98)i,ni(t) ≥ i − ni(t) 2K ≥ i − { i(cid:63) − i } ≥ i(cid:63) − 2
or (cid:96) = i and
t (cid:63)
µ µ ϕ ( δ ) µ max µ µ¯,u(cid:15) /2 = min µ¯,µ 1u(cid:15) .
(cid:98)i(cid:63),ni(cid:63) (t) ≥ i(cid:63) − ni(cid:63) (t) 2K ≥ i(cid:63) − { i(cid:63) − } { i(cid:63) − 2 }
Because µ max µ , the proof of the claim is complete.
(cid:98)ht,n
ht
(t)
≥
i=0,1,...,K (cid:98)i,ni(t)
26