|     | Manipulation |               | of the     | Running     | Variable  | in the |
| --- | ------------ | ------------- | ---------- | ----------- | --------- | ------ |
|     | Regression   | Discontinuity |            | Design:     | A Density | Test∗  |
|     |              |               | Justin     | McCrary     |           |        |
|     |              |               | University | of Michigan |           |        |
|     |              |               | December   | 2006        |           |        |
Abstract
Standard sufficient conditions for identification in the regression discontinuity design are continuity
of the conditional expectation of counterfactual outcomes in the running variable. These continuity
assumptions may not be plausible if agents are able to manipulate the running variable. This paper
develops a test of manipulation related to continuity of the running variable density function. The
methodology is applied to popular elections to the House of Representatives, where sorting is neither
expected nor found, and to roll-call voting in the House, where sorting is both expected and found.
∗Ithanktwoanonymousrefereesforcomments,theeditorsformultiplesuggestionsthatsubstantiallyimprovedthepaper,
JackPorter,JohnDiNardo,andSerenaNgfordiscussion,JonahGelbachforcomputingimprovements,andMing-YenCheng
| for manuscripts. | Any errors | are my own. |     |     |     |     |
| ---------------- | ---------- | ----------- | --- | --- | --- | --- |

I. Introduction
Onereasonfortheincreasingpopularityineconomicsofregressiondiscontinuityapplicationsisthepercep-
tion that the identifying assumptions are quite weak. However, while some applications of the design can
be highly persuasive, many are subject to the criticism that public knowledge of the treatment assignment
rule may invalidate the continuity assumptions at the heart of identification.
Consider a hypothetical example. A doctor plans to randomly assign heart patients to a statin and a
placebo to study the effect of the statin on heart attack within ten years. The doctor randomly assigns
patients to two different waiting rooms, A and B, and plans to give those in A the statin and those in B the
placebo. If some of the patients learn of the planned treatment assignment mechanism, we would expect
them to proceed to waiting room A. If the doctor fails to divine the patients’ contrivance and follows the
original protocol, random assignment of patients to separate waiting rooms may be undone by patient
sorting after random assignment. In the regression discontinuity context, an analogous evaluation problem
may occur in the common case where the treatment assignment rule is public knowledge (cf., Lee 2007).
In this paper, I propose a formal test for sorting of this type. The test is based on the intuition that,
in the example above, we would expect for waiting room A to become crowded. In the regression discon-
tinuity context, this is analogous to expecting the running variable to be discontinuous at the cutoff, with
surprisingly many individuals just barely qualifying for a desirable treatment assignment and surprisingly
fewfailingtoquality. Thistestwillbeinformativewhenmanipulationoftherunningvariableismonotonic,
in a sense to be made specific below.
The proposed test is based on an estimator for the discontinuity at the cutoff in the density function of
the running variable. The test is implemented as a Wald test of the null hypothesis that the discontinuity
is zero. The estimator, which is a simple extension of the local linear density estimator (Cheng, Fan and
Marron 1997), proceeds in two steps. In the first step, one obtains a finely-gridded histogram. In the
second step, one smooths the histogram using local linear regression, separately on either side of the cutoff.
To efficiently convey sensitivity of the discontinuity estimate to smoothing assumptions, one may augment
a graphical presentation of the second-step smoother with the first-step histogram, analogous to presenting
local averages along with an estimated conditional expectation.
This test complements existing specification checks in regression discontinuity applications. Authors
routinely report on the smoothness of pre-determined characteristics around the cutoff (e.g., DiNardo and
Lee2004). Iftheparticularpre-determinedcharacteristicstheresearcherhasatdisposalarerelevanttothe
problem, this method should be informative about any sorting around the discontinuity. However, in some
1

applications pre-determined characteristics are either not available, or those which are available are not
relevant to the outcome under study. By way of contrast, the density test may always be conducted, since
data on the running variable is required for any analysis. The method is also useful in applications where
a discontinuous density function is itself the object of interest. For example, Saez (1999, 2002) measures
tax avoidance using the discontinuity in the density of income reported to the Internal Revenue Service.
Toshowhowtheestimatorworksinpractice,Iapplythemethodologytotwodistinctsettings. Thefirst
setting is popular elections to the United States House of Representatives, considered in Lee’s (2001, 2007)
incumbency study. In this context, it is natural to assume that the density function of the Democratic
voteshare is continuous at 50 percent. The data do not reject this prediction.1 The second setting is
roll call votes in the House. In this context, the vote tally for a given bill is expected to be subject to
manipulation. Althoughthenumberofrepresentativeswouldseemtomakecoordinationbetweenmembers
difficult, these problems are overcome by a combination of the repeated game aspect of roll call votes and
the fact that a representative’s actual vote becomes public knowledge, enabling credible commitments and
vote contracting. In this setting, the density test provides strong evidence of manipulation.
The remainder of the paper is organized as follows. Section II defines manipulation and distinguishes
between partial and complete manipulation. Section III describes the estimator and discusses smoothing
parameter methods and inference procedures. Section IV motivates the manipulation problem with a
hypothetical job training program. Section V presents the results of a small simulation study. Section VI
presents the empirical analysis, and Section VII concludes. Appendix I gives a proof of the proposition of
| Section            | III, and Appendix | II describes  | the | data.    |              |     |     |     |
| ------------------ | ----------------- | ------------- | --- | -------- | ------------ | --- | --- | --- |
| II. Identification |                   | under Partial | and | Complete | Manipulation |     |     |     |
Let Y denote an outcome and D a binary treatment. The outcome depends on treatment according to
| i   |     |     | i     |              |               |     |     |     |
| --- | --- | --- | ----- | ------------ | ------------- | --- | --- | --- |
|     |     |     | Y i = | α i +β i D i | = α+βD i +ε i |     |     | (1) |
where α i and β i are random variables with means α and β, respectively, and ε i = α i −α+(β i −β)D i
(cf., Card’s (1999) appendices). In counterfactual notation, α = Y and β = Y − Y , where Y is
|     |     |     |     |     | i i0 | i i1 | i0  | i0  |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
the outcome that would obtain, were D = 0, and Y is the outcome that would obtain, were D = 1.
|     |     |     | i   |     | i1  |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Equation (1) is viewed as a structural equation, in the sense that the manner in which i is induced into
| 1However, | see Snyder | (2005). |     |     |     |     |     |     |
| --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
2

participation in the program does not affect (Y ,Y ) under exogeneity.2 As noted by Hahn, Todd and
i0 i1
van der Klaauw (2001, hereinafter HTV), and following Imbens and Angrist (1994), the average β for a
i
specific subpopulation is identifiable under continuity of the conditional expectations of α and β , given
i i
an underlying index. This index is here termed the “running variable” and denoted R .
i
Underlying R is an unobservable index R that is the running variable that would obtain, were there
i i0
noprogram. ThismaybedifferentfromR . Therunningvariableismanipulated whenR 6= R . Although
i i i0
R is not observed, it is well-defined conceptually. For example, van der Klaauw (2002) studies the impact
i0
of scholarships on students’ enrollment decisions, where scholarships are assigned discontinuously on the
basis of a linear combination of SAT and high school grade point average (GPA). It is straightforward
to conceptualize of the linear combination of the ith student’s SAT and GPA that would obtain, if the
university in question did not run such a scholarship program.
I interpret the identification results of HTV as holding under continuity assumptions pertaining to the
unobservable index R . Formally, throughout the paper I assume that
i0
E[α |R = r], E[β |R = r], and f (r) are continuous in r (A0)
i i0 i i0 Ri0
where f (r) is the density of R . Although this assumption is very weak, it is sufficient for a regression
Ri0 i0
discontinuityestimatorbasedontheindexR toidentifyalocalaveragetreatmenteffect.3 Theconditional
i0
expectation restrictions in (A0) are HTV’s identification assumptions, but (A0) is stronger than their
assumptionsbecauseoftheadditionalrestrictionthatthedensityfunctionbecontinuous. Formostsettings
in which continuity of the conditional expectations is plausible, continuity of the density will be plausible.
If there is no manipulation, then (A0) holds with R replacing R , and identification of meaningful
i i0
parameters can be obtained. Sufficient conditions for lack of manipulation include timing, such as when
the program is announced simultaneously with implementation, and lack of agent interest in obtaining
any particular training assignment, for example. However, when individuals know of the selection rule for
treatment,areinterestedinbeingtreated,andhavetimetoadjusttheirbehavioraccordingly,manipulation
can be important. In Section IV, below, I give an example of a job training program where manipulation is
expected and show how manipulation leads to erroneous inferences. The density test detects manipulation
easilyinthissetting. Intheexample,theidentificationproblemarisesbecausetheincentivesoftheprogram
2This is Heckman’s (2005, p. 11) assumption (A-2). In the statistics literature, this is subsumed under the stable unit
treatment value assumption (SUTVA). See Rubin (1980, 1986). I also abstract from general equilibrium effects.
3Fordiscussionofthelocalaveragetreatmenteffectparameter,seeAngrist,ImbensandRubin(1996)andHeckman,Urzua
and Vytlacil (2006), for example.
3

lead to sorting on the running variable. Generally, manipulation can lead E[α |R = r] and E[β |R = r]
i i i i
to be discontinuous at the cutoff, despite continuity of E[α |R = r] and E[β |R = r].
i i0 i i0
Only some varieties of manipulation lead to identification problems. I draw a distinction between
partial and complete manipulation. Partial manipulation occurs when the running variable is under the
agent’s control, but also has an idiosyncratic element. Typically, partial manipulation of the running
variable does not lead to identification problems. Examples of regression discontinuity settings where
partial manipulation is arguably plausible include van der Klaauw (2002) and DiNardo and Lee (2004), for
example.4 Complete manipulation occurs when the running variable is entirely under the agent’s control.
Typically, complete manipulation of the running variable does lead to identification problems. Examples
of regression discontinuity settings in which complete manipulation is a potential threat to validity include
Hahn, Todd and van der Klaauw (1999) and Jacob and Lefgren (2004), for example.5
Propositions 2 and 3 of Lee (2007) establish that, under mild regularity conditions, identification of
meaningful parameters can be obtained under partial manipulation. As Lee notes, the critical assumption
underlying both propositions is that the conditional density function f (r|w) be continuous in r, where
R|W
W represents potential confounders (“types”). This is an intuitive identifying assumption: if the running
variablehasacontinuousdensityconditionalontype, thenforeverytypeofpersonthechanceofarunning
variable draw just above the cutoff is equal to the chance of a running variable draw just below the cutoff.
The assumption is not directly testable, since types are unobserved. However, Lee stresses the important
idea that this assumption implies continuity of the conditional expectation of any baseline characteristic
in the running variable. It is thus easy to test the identifying assumption using standard estimators for
conditional expectations, such as local linear regression or global polynomial regression. Such tests are
already commonly reported in applications.
This paper develops a complementary testing procedure. The idea of the test is that continuity in r of
4vanderKlaauw(2002)studiestheeffectofscholarshipsonenrollmentforacollegethatassignsscholarshipsdiscontinuously
using an index that is a linear combination of SAT score and high school grade point average (p. 1255). van der Klaauw
does not state whether students could have had prior knowledge of the formula used, but it seems plausible that even if they
had, it wouldbe difficult to controlprecisely the valueof such an index. Similarly, it might be difficult to control one’s grade
pointaverageperfectly. DiNardoandLee(2004)studytheimpactofunionizationonestablishmentoutcomes. Firmsbecome
unionized based on a majority vote of the employees. While firms and unions certainly attempt to manipulate the vote tally,
it would be difficult for either to do so perfectly, particularly since union certification elections are secret ballot.
5Hahn et al. (1999) study the impact of equal employment opportunity laws on employment of racial minorities, taking
advantage of the fact that the 1964 Civil Rights Act, as amended, covers only those firms with 15 or more employees.
Employers presumably maintain perfect control over labor inputs. This raises the possibility that a firm owner with a taste
for discrimination, who would otherwise find it profit-maximizing to employ 15, 16, or 17 employees, for example, would
elect to employ 14 employees to preclude the possibility of litigation alleging violations of the Civil Rights Act (cf., Becker
1957). JacobandLefgren(2004)studytheimpactofsummerschoolandgraderetentionontestscores,wherethetreatments
depend discontinuously on separate pre-tests. In that context, because the treatment assignment rule is public knowledge, it
is possible that those grading the pre-test would be motivated to influence a student’s treatment assignment by strategically
mismeasuring the student’s actual score (see authors’ discussion, p. 231).
4

the conditional density f (r|w) implies continuity of f (r), the density of the running variable. Thus, a
R|W R
natural specification test in applications is a test of the continuity of the running variable density function.
The density test may not be informative unless the existence of the program induces agents to adjust
the running variable in one direction only. Manipulation is monotonic if either R ≥ R for all i or
i i0
R ≤ R for all i. Consider a hypothetical example based on the Jacob and Lefgren (2004) study, in which
i i0
the probability of summer school is a discontinuous function of test scores, and teachers are in charge of
grading examinations for summer school. Assume students attend summer school if and only if assigned
to attend, so that in the absence of manipulation, the local average treatment effect equals the average
treatment effect (ATE). Let the ATE be zero, but assume students have heterogeneous treatment effects
of summer school; summer school helps half and harms half. Teachers discern these treatment effects, and
manipulate the scores of those who would be helped and who just barely passed, so that they fail and have
to go to summer school. Similarly, teachers manipulate the scores of those who would be harmed and who
just barely failed, so that they pass and avoid going to summer school. Estimated treatment effects of the
program would be positive, because of teacher manipulation of scores. However, because the manipulation
is non-monotonic, and because those whose scores are adjusted up are equally numerous as those whose
scores are adjusted down, the density test will fail to detect manipulation.
The density test could also fail, even when there is no failure of identification. Assume teachers give
bonus points to some of those who just barely fail the exam (perhaps to reduce the size of summer
school classes), and substract points from no student. Then the density test would suggest a failure of
identification. However, if teachers select at random which students receive bonus points, then an ATE
would be identified. These examples clarify that a running variable with a continuous density is neither
necessary nor sufficient for identification except under auxiliary assumptions.6
III. Estimation and Inference Procedures
To estimate potentially discontinuous density functions, economists have used either traditional histogram
techniques (DiNardo and Lee 2004, Saez 2002), or kernel density estimates which smooth over the point of
potential discontinuity (DiNardo, Fortin and Lemieux 1996, Saez 1999, Jacob and Lefgren 2004). Neither
procedure allows for point estimation or inference. One could estimate a kernel density function separately
for points to the left and right of the point of discontinuity, but at boundaries a kernel density estimator
is badly biased, as is well-known (e.g., Marron and Ruppert 1994).
6I thank the editors for their emphasis of this important point.
5

One method that corrects for boundary bias is the local linear density estimator developed by Cheng,
FanandMarron(1993)andCheng(1994).7,8 Thegroundsforfocusingonthelocallineardensityestimator
are theoretical and practical. Theoretically, the estimator weakly dominates other proposed methods.
Cheng et al. (1997) show that for a boundary point the local linear method is 100 percent efficient among
linear estimators in a minimax sense.9 Practically, the first-step histogram is of interest in its own right,
because it provides an analogue to the local averages typically accompanying conditional expectation
estimates in regression discontinuity applications. Moreover, among nonparametric methods showing good
performance at boundaries, local linear density estimation is simplest.
A. Estimation
Implementing the local linear density estimator involves two steps. The first step is a very under-
smoothed histogram. The bins for the histogram are defined carefully enough that no one histogram bin
includes points both to the left and right of the point of discontinuity. The second step is local linear
smoothing of the histogram. The midpoints of the histogram bins are treated as a regressor, and the
normalized counts of the number of observations falling into the bins are treated as an outcome variable.
To accomodate the potential discontinuity in the density, local linear smoothing is conducted separately
for the bins to the right and left of the point of potential discontinuity, here denoted c.
The first-step histogram is based on the frequency table of a discretized version of the running variable,
(cid:185) (cid:186) (cid:189) (cid:190)
R −c b b b b b b b
i
g(R ) = b+ +c ∈ ...,c−5 ,c−3 ,c− ,c+ ,c+3 ,c+5 ,... (2)
i
b 2 2 2 2 2 2 2
wherebacisthegreatestintegerina.10,11 Defineanequi-spacedgridX ,X ,...,X ofwidthbcoveringthe
1 2 J
7PublishedpapersdescribingthelocallineardensityapproachincludeFanandGijbels(1996),Cheng(1997a,b),and Cheng
et al. (1997). The general idea of “pre-binning” the data before density estimation, and the conclusion that estimators based
onpre-binneddatadonotsufferintermsofpracticalperformancedespitetheoreticallossofinformation,arebothmucholder
than the idea of local linear density estimation; see, for example, Jones (1989) and references therein.
8Competing estimators for estimating a density function at a boundary are also available. Estimators from the statistics
literature include modified kernel methods (see, e.g., Chu and Cheng 1996, Cline and Hart 1991) and wavelet methods (for
references, see Hall, McKay and Turlach 1996). Among the better-known methods, one with good properties is Rice (1984).
Boundary folding methods are also used (see, for example, Schuster 1985), but their properties are not favorable. Marron
and Ruppert (1994) give a three-step transformation method. An older method with favorable properties is the smoothed
histogramapproachdevelopedbyGawronskiandStadtmu¨ller(1980,1981) andrecentlyexploredbyBouezmarniandScaillet
(2005). Theselastauthorsalsodiscusstheuseofasymmetrickernelsforcircumventingtheboundarybiasofkernelestimators.
Bouezmarni and Scaillet appear to be the first authors in economics to estimate a density function at a boundary using a
nonparametric method, but they do not discuss local linear density estimation. Parametric models involving discontinuous
densityfunctionshavebeenstudiedextensivelyineconomics;seeAigner,AmemiyaandPoirier(1976)foranearlypaperand
Chernozhukov and Hong (2004) for references.
9FanandGijbels(1996)giveagooddiscussionofthisresultanddiscussfurtherresultsregardingdeepersensesofefficiency.
10Thegreatestintegerinaistheuniqueintegerksuchthatk≤a<k+1(“roundtotheleft”). Insoftware,thisistypically
known as the floor function, which is not the same as the int function, because negatives are handled differently.
11Equation (2) will result in observations with R =c being assigned to the bin c+ b, which is valid if ties are assigned to
i 2
6

(cid:80)
|     |     |     |     |     |     |     |     |     |     | 1 n |     |     | ).12,13 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
support of g(R ) and define the (normalized) cellsize for the jth bin, Y = 1(g(R ) = X The
|     |     | i   |     |     |     |     |     |     |     | j nb i=1 |     | i   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
first-step histogram is the scatterplot (X ,Y ). The second step smooths the histogram using local linear
|     |     |     |     |     | j   | j                     |     |     |                            |            |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------------------- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     |     | isgivenbyf(cid:98)(r) |     |     | φ(cid:98) ,where(φ(cid:98) | ,φ(cid:98) |     |     |     |     |
regression. Formally,thedensityestimateatr = 1 1 2 )minimizeL(φ 1 ,φ 2 ,r) =
(cid:80)
| J   |     |     | −r)}2K((X |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{Y −φ −φ (X −r)/h){1(X > c)1(r ≥ c)+1(X < c)1(r < c)}, K(·) is a kernel
| j=1 | j 1 | 2   | j   |     | j   |     | j   |     |     | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
function, here chosen as the triangle kernel K(t) = max{0,1−|t|}, and h is the bandwidth, or the window
regression.14
width defining which observations are included in the In words, the second step smooths the
histogram by estimating a weighted regression using the bin midpoints to explain the height of the bins,
giving most weight to the bins nearest where one is trying to estimate the density. It is straightforward to
estimate the entire density function, f(r), by looping over evaluation points r.
Define the parameter of interest to be the log difference in height, or
|     |     |     | θ   | =   | lnlimf(r)−lnlimf(r) |     |     | ≡   | lnf+−lnf− |     |     |     |     | (3) |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | r↓c                 |     | r↑c |     |           |     |     |     |     |     |
While one can estimate f+ and f− using f(cid:98)(r) for r just above and below c, respectively, it is easier and
more accurate to estimate two separate local linear regressions, one on either side of c, with X − c as
j
regressor. The log difference of the coefficients on the intercepts then estimates θ. Formally,
| θ(cid:98) | lnf(cid:98)+−lnf(cid:98)− |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ≡         |                           |     |     |     |     |     |     |     |     |     |     |     |     | (4) |
|           |                          |     |     |     |     |     |    |    |     |     |     |     |     |    |
(cid:88) (cid:181) (cid:182) + +  (cid:88) (cid:181) (cid:182) − − 
|         |          |      | X −c            | S    | −S      | (X −c) |         |          |      | X −c       | S     | −S            | (X −c) |      |
| ------- | -------- | ---- | --------------- | ---- | ------- | ------ | ------- | -------- | ---- | ---------- | ----- | ------------- | ------ | ---- |
|         |          |      | j               | n ,2 | n ,1    | j      |         |          |      | j          | n ,2  | n ,1          | j      |      |
| =       | ln       | K    |                 |      |         |        | Y j −ln |          | K    |            |       |               |        | Y j  |
|         |         |      | h               | S+   | S+ −(S+ |        | )2     |         |      | h          | S−    | S− −(S−       |        | )2  |
|         |          |      |                 | n,2  | n,0     | n,1    |         |          |      |            | n,2   | n,0           | n,1    |      |
|         | Xj>c     |      |                 |      |         |        |         | Xj<c     |      |            |       |               |        |      |
|         | (cid:80) |      |                 |      |         |        |         | (cid:80) |      |            |       |               |        |      |
| whereS+ |          |      |                 |      | −c)k    | andS−  |         |          |      |            | −c)k. |               |        |      |
|         | =        |      | K((X j −c)/h)(X |      | j       |        | =       |          | K((X | j −c)/h)(X | j     | Understandard |        |      |
|         | n,k      | Xj>c |                 |      |         |        | n,k     | Xj<c     |      |            |       |               |        |      |
θ(cid:98)is
nonparametric regularity conditions, consistent and asymptotically normal.
Proposition. Let f(·) be a density function which, everywhere except at c, has three continuous and
bounded derivatives. Let K(t) = max{0,1−|t|} be the triangle kernel, and suppose that h → 0, nh → ∞,
treatment. If ties are assigned to control, re-define g(R )=dRi−ceb− b +c, where dae is 1 plus the greatest integer in a.
|     |     |     |     |     |     |     | i b | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
12Defining a grid covering the support of g(R ) is necessary to account for “zero count” bins.
i
13Note that these values of X are deterministic in the sense that c and b are treated as constants. The endpoint X
|     |     |     | j   |     |     |     |     |     |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(X J ) may always be chosen arbitrarily small (large) so that it is well beyond the support of g(R i ) with no consequences for
estimationoftheoveralldensityanywherewithin[R+h,R−h],where[R,R]isthesupportoftheoriginalR . Thus,without
i
lossofgenerality,wemayalsodefineX =l+(j−1)b,wherel=b(Rmin−c)/bcb+(b/2)+c,andJ =b(Rmax−Rmin)/bc+2.
j
However, if global polynomial fitting is used, as in the automatic bandwidth selector discussed in Section III.B, below, then
the grid should fall strictly in the range [R,R]. This is not necessary if modeling a density with unbounded support.
14Givenitsgenerallyminimalroleinperformance,thekernelfunctionmaybechosenonthebasisofconvenience.
However,
the triangle kernel is boundary optimal (Cheng et al. 1997). At interior points, where the Epanechnikov kernel K(t) =
max{0,0.75(1−t2)} is optimal, the local linear density estimator is primarily used for graphical purposes and informal
inference. Hencethereislittlecosttousingthetrianglekerneleverywhere,andthisistheconventionIadoptforSectionsIV,
| V, and VI, | below. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7

√
h2
b/h → 0, and nh −→ H ∈ [0,∞). Then if R ,R ,...,R (cid:195) is a random (cid:33) sample with density f(r),
|     |                |           | (cid:181) |     | (cid:181) |     | (cid:182)(cid:182) |     | 1 2 |       | n     |     |     |     |
| --- | -------------- | --------- | --------- | --- | --------- | --- | ------------------ | --- | --- | ----- | ----- | --- | --- | --- |
| √   | (cid:179)      | (cid:180) |           |     |           |     |                    |     |     | −f+00 | −f−00 |     |     |     |
|     |                | d         |           | 24  | 1         | 1   |                    |     | H   |       |       |     |     |     |
|     | nh θ(cid:98)−θ | − →       | N B,      |     |           | +   | , where            | B   | =   |       | −     | .   |     |     |
|     |                |           |           |     | f+        | f−  |                    |     |     | f+    | f−    |     |     |     |
|     |                |           |           | 5   |           |     |                    |     | 20  |       |       |     |     |     |
The proof, given in Appendix I, builds on an unpublished proof of Cheng (1994).
θ(cid:98)of
|     | The | proposition | implies |     | an approximate |     | standard |     | error | for |     |     |     |     |
| --- | --- | ----------- | ------- | --- | -------------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- |
(cid:115)
|     |     |     |     |     |     |           |     | (cid:181) |            | (cid:182)  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ---------- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     |     |           |     | 1 24      | 1          | 1          |     |     |     |     |
|     |     |     |     |     |     | σ(cid:98) | =   |           | +          |            |     |     |     | (5) |
|     |     |     |     |     |     | θ         |     | nh 5      | f(cid:98)+ | f(cid:98)− |     |     |     |     |
As shown in the simulation study in Section V, below, t-tests constructed using this standard error are
| very | nearly | normally | distributed |     |     | under | the null | hypothesis. |     |     |     |     |     |     |
| ---- | ------ | -------- | ----------- | --- | --- | ----- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
However, the normal distribution in question is not quite centered at zero if the bandwidth is of order
n−1/5, the rate which minimizes the asymptotic mean squared error. This is typical of a nonparametric
setting; atuningparameterthatisgoodforestimationpurposesisnotnecessarilygoodfortestingpurposes
θ(cid:98)
(Pagan and Ullah 1999). Practically, this means that a confidence region for constructed using the
standard error above will give good coverage accuracy for the probability limit of θ(cid:98), as opposed to good
coverage accuracy for θ. Two approaches are taken in the literature to circumvent this problem. First,
relative to a bandwidth which is believed to minimize the mean squared error, one can choose a bandwidth
smaller than that. The hope is that the bias is thereby sufficiently reduced that it may be ignored. Second,
bias.15
one can estimate the This bells the cat in that it requires choosing another bandwidth. Following
Horowitz (2001) and Hall (1992), I focus on undersmoothing. A simple undersmoothing method is to take
a reference bandwidth and to divide it by 2 (Hall 1992). Section V presents simulation evidence on the
success of this strategy in connection with the reference bandwidth described in the next subsection.
| B.  | Binsize | and | Bandwidth |     | Selection |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For a fixed bandwidth, the estimator described above is robust to different choices of binsize provided
| that | h/b               | > 10, say. | To  | understand |          | this      | robustness, | decompose |           |      | f(cid:98)+ as |     |     |     |
| ---- | ----------------- | ---------- | --- | ---------- | -------- | --------- | ----------- | --------- | --------- | ---- | ------------- | --- | --- | --- |
|      |                   |            |     |            |          | (cid:181) |             | (cid:182) |           |      |               |     |     |     |
|      | √                 |            |     |            | (cid:88) |           |             |           |           | −c)√ |               |     |     |     |
|      | nh(f(cid:98)+−f+) |            |     | 1          |          |           | X j −c      | χ 2       | −χ 1 (X   | j    |               | 1   |     |     |
|      |                   |            | =   | (cid:112)  |          | K         |             |           |           |      | nb(Y          | − p | )   | (6) |
|      |                   |            |     |            |          |           |             |           |           | )2   |               | j   | j   |     |
|      |                   |            |     | h/b        |          |           | h           | χ         | 2 χ 0 −(χ | 1    |               | b   |     |     |
Xj>c
|     |     |     |     |     |          | (cid:181) |     | (cid:182) |     |      | (cid:181) |     | (cid:182)             |     |
| --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | --- | ---- | --------- | --- | --------------------- | --- |
|     |     |     |     |     | (cid:88) |           |     |           |     | −c)√ |           |     |                       |     |
|     |     |     |     | 1   |          | X         | −c  | χ −χ      | (X  |      | 1         |     |                       |     |
|     |     |     | +   |     |          | K         | j   | 2         | 1   | j    | nh p      | −f+ | ≡ A +E[f(cid:98)+−f+] |     |
|     |     |     |     |     |          |           |     |           |     |      |           | j   | n                     |     |
|     |     |     |     | h/b |          |           | h   | χ χ       | −(χ | )2   | b         |     |                       |     |
|     |     |     |     |     | Xj>c     |           |     | 2         | 0   | 1    |           |     |                       |     |
15In their survey, H¨ardle and Linton (1994) discuss only undersmoothing. Pagan and Ullah (1999) discuss a variety of
procedures, but do not provide recommendations. In the related context of local linear regression, Fan and Gijbels (1996)
recommend estimating the bias using a two-step procedure; a pilot bandwidth is required for this procedure. Davison and
Hinkley (1997) suggest the use of the bootstrap to estimate the bias of the kernel density estimator, but Hall (1992) shows
| that | this | method performs |     | badly. |     |     |     |     |     |     |     |     |     |     |
| ---- | ---- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8

|     |     | (cid:80) |     |     |     | (cid:82) |     |     |
| --- | --- | -------- | --- | --- | --- | -------- | --- | --- |
1/2
where χ = 1 K((X −c)/h)(X −c)k, k = 0,1,2 and 1p = f(X +bu)du.16 As shown
|     | k h/b | Xj>c | j   | j   |     | b j −1/2 | j   |     |
| --- | ----- | ---- | --- | --- | --- | -------- | --- | --- |
formally in Appendix I, A tends towards a normal distribution. The quality of the normal approximation
n
does not turn on the magnitude of b. Intuitively, the second step smoother averages over the Y j , which are
themselves averages. If b is small, then the Y are not particularly normal, but the second step smoothing
j
compensates. If b is large, then the Y are very nearly normal, and not much averaging needs to happen in
j
the second step. The second sum in this decomposition gives the finite-sample bias of the estimator. Two
| Taylor | approximations   | and | the algebra | of regressions | show that               |     |           |     |
| ------ | ---------------- | --- | ----------- | -------------- | ----------------------- | --- | --------- | --- |
|        |                  |     | (cid:88)    |                | √ (cid:169)             |     | (cid:170) |     |
|        |                  |     | b           | χ 2 −χ         | 1 ht j                  |     |           |     |
|        | E[f(cid:98)+−f+] |     | = K(t       | )              | nh h2t2f00++O(h3)+O(b2) |     |           | (7) |
|        |                  |     |             | j              |                         | j   |           |     |
|        |                  |     | h           | χ 2 χ 0 −(χ    | 1 )2                    |     |           |     |
Xj>c
where t = (X −c)/h. Since the t sequence is b/h apart, this is a Riemann approximation to the area
|     | j   | j   |     | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
under a curve. The height of the curve in question is dominated by the h2 term since h > b. The analysis
√
|     | nh(f(cid:98)−−f−) |     |     |     | θ(cid:98)does |     |     |     |
| --- | ----------------- | --- | --- | --- | ------------- | --- | --- | --- |
for is symmetric. Thus, good performance of not appear to require a careful choice
of binsize. This point is substantiated in the simulation study in Section V, below.
Goodperformanceofθ(cid:98)doesrequireagoodchoiceofbandwidth, however. Probablythebestmethodof
bandwidth selection is visual inspection of the first-step histogram and the second-step local linear density
function estimate, under a variety of choices forb and h. With software, it is easy to inspect both functions
seconds.17
within a few One of the practical advantages of the two-step estimation method described
here is visual. Suppose that as part of a pilot investigation, one has estimated the first-step histogram
using binsize b and the second-step local linear smoother using bandwidth h. Graphically, superimposing
the local linear smoother on the scatterplot (X ,Y ) reveals rapidly the likely consequences of choosing a
|     |     |     |     | j   | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
different bandwidth. The effectiveness of subjective bandwidth choice has been noted in related contexts
| by Pagan | and | Ullah (1999) | and Deaton | (1997), | for example. |     |     |     |
| -------- | --- | ------------ | ---------- | ------- | ------------ | --- | --- | --- |
Less subjective methods include cross-validation (Stone 1974, 1977) and plug-in estimators. Cheng
(1997a) proposes a plug-in bandwidth selector tailored to local linear density estimation, analogous to the
Sheather and Jones (1991) selector that is popular in standard density estimation settings. Her method
(cid:82)
requires estimating the integral of the squared second derivative, (f(2)(r))2dr. As is standard in the
(cid:82)
literature, she uses a bandwidth other than h to estimate (f(2)(r))2dr; to find the optimal bandwidth
(cid:82)
f(2)(r)f(4)(r)dr,
for this ancillary task requires approximating and we are back where we started. Cheng
16Ananalogousdecompositioncanbeusedtomotivateanestimatorthatreplacestakesthelogofthehistogramcountsbefore
smoothing. Due to the covariance structure of the Y and the nonlinearity of ln(·), a rigorous demonstration of asymptotic
j
normality does not appear straightforward unless one fixes b and redefines the parameter of interest. Nonetheless, such an
|     |     |     | θbis, |     |     | θb, |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
estimator is consistent whenever and has the same asymptotic variance as provided nb→∞.
17Software
(STATA version 9) is available from the author for a period of 3 years from the date of publication.
9

(1994, Section 4.5.2) notes that the method fares poorly in the boundary setting, where the integrals are
(particularly) hard to estimate with any accuracy, and suggests further modifications.
To be practical, bandwidth selection rules need to be easy to implement. My own view is that the
best method is subjective choice, guided by an automatic procedure, particularly if the researcher agrees
to report how much the chosen bandwidth deviates from the recommendations of the automatic selector.
Here is a simple automatic bandwidth selection procedure that may be used as a guide:
1. Compute the first-step histogram using the binsize (cid:98)b = 2σ(cid:98)n−1/2, where σ(cid:98) is the sample standard
deviation of the running variable.
2. Using the first-step histogram, estimate a global 4th order polynomial separately on either side of
(cid:104) (cid:105)
(cid:177)(cid:80) 1/5
the cutoff. For each side, compute κ σ˘2(b−a) f˘00(X )2 , and set (cid:98)h equal to the average of
j
.
the these two quantities, where κ = 3.348, σ˘2 is the mean-squared error of the regression, b − a
equals X −c for the right-hand regression and c−X for the left-hand regression, and f˘00(X ) is
J 1 j
the estimated second derivative implied by the global polynomial model.18
The second step of this algorithm is based on the rule-of-thumb bandwidth selector of Fan and Gijbels
(1996, Section 4.2). After implementing this selector, displaying the first-step histogram based on (cid:98)b and
the curve f(cid:98)(r) based on (cid:98)h provides a very detailed sense of the distribution of the running variable, upon
which subjective methods can be based. The selection method outlined in the above algorithm is used in
the simulation study in Section V, below, where an automatic method is needed. In the empirical work in
Section VI, where subjective methods are feasible, this selection method is used as a guide.
IV. Theoretical Example
To motivate the potential for identification problems caused by manipulation, consider a simple labor
supply model. Agents strive to maximize the present discounted value of utility from income over two
periods. Each agent chooses to work full- or part-time in each period. Part-time work requires supplying
a fraction f of full-time labor supply and receiving a fraction f of full-time income. Each worker has
i i
a different fraction f , which is determined unilaterally by the employer prior to period 1 on the basis
i
of production technology. Earnings in period 1 are given by R = α H , where H = 1 if the individual
i i i i
works full-time and H = f if the individual works part-time. Between periods 1 and 2, a job training
i i
program takes place. Agents are eligible for participation if they pass a means test based on period 1
income: program participation is indicated by D = 1(R ≤ c), where c is the earnings threshold. Earnings
i i
18Theconstantκisbasedonvariousintegralsofthekernelusedinthesecondstep. Thestandardformula(seeequation(4.3)
ofFanandGijbels1996)doesnotapplytotheboundarycase(seeequations(3.20)and(3.22)ofFanandGijbels). Theconstant
cited is specific to the triangle kernel in the boundary case.
10

in period 2 are given by Y = α +β D , as in equation (1).
i i i i
Iftheprogramdidnotexist,agentswouldsupplyfulllaborinbothperiods. InthenotationofSectionII,
above, this means that R = α . However, the existence of the program raises the possibility that agents
i0 i
will manipulate the running variable, withholding labor supply to meet the means test and gain access to
job training. Schematically, the decision problem can be represented as
Figure 1. The Agent’s Problem
(cid:169)(cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
(cid:169) (cid:72)
Part-Time Work (H = f ) Full-Time Work (H = 1)
i i i
(cid:169) (cid:169) (cid:169) (cid:169) (cid:169) (cid:169)
(cid:169)(cid:72)
(cid:72) (cid:72) (cid:72) (cid:72) (cid:72) (cid:72) (cid:169) (cid:169) (cid:169) (cid:169) (cid:169)
(cid:169)(cid:169)(cid:72)(cid:72)
(cid:72) (cid:72) (cid:72) (cid:72) (cid:72)
R i = f i α i ≤ c, obtain R i = f i α i > c, obtain R i = α i ≤ c, obtain R i = α i > c, obtain
u(f i α i )+δu(α i +β i ) u(f i α i )+δu(α i ) u(α i )+δu(α i +β i ) u(α i )+δu(α i )
where δ is the discount factor. For well-paid agents with α > c/f , the model predicts H = 1; for such
i i i
an agent, reducing labor supply is never worth it, because even under part-time work, the agent will not
satisfy the means test. For poorly-paid agents with α ≤ c, the model similarly predicts H = 1, but for
i i
a different reason: such an agent satisfies the means test for the program, even if working full-time. The
remaining agents, those with latent wages satisfying c < α ≤ c/f , may find it worthwhile to reduce labor
i i
supply, because otherwise they will fail the means test. These agents reduce labor supply in response to
the program if and only if u(f α )+δu(α +β ) > u(α )+δu(α ). There will always exist a value β large
i i i i i i i
enoughtoinduceanagenttoselectH = f . Ifβ andα arecorrelated, aswouldbeexpectedinthegeneral
i i i i
case, then this leads the conditional expectation of counterfactual outcomes in R to be discontinuous. A
i
necessary condition for the utility inequality above to hold is β > 0. Under concave utility a sufficient
i
(cid:177)
condition is β > (u(α )−u(f α )) δu0(α ). Under linear utility, this condition is also necessary, and we
i i i i i
(cid:177)
may characterize those who reduce their labor supply as those with c < α ≤ c/f and β > α (1−f ) δ.
i i i i i
Figure 2 shows the implications of these behavioral effects using a simulated data set on 50,000 agents
withlinearutility. Thesimulationtakes(α ,β )tobedistributedasindependentnormals, withE[α ] = 12,
i i i
V[α ] = 9, E[β ] = 0, and V[β ] = 1, and the f distribution to be uniform on [0,1] and independent of
i i i i
(α ,β ). The earnings threshold is set at c = 14.
i i
11

This data generating process is consistent with (A0). If the program did not exist, then period 1
earnings would be R = α . The conditional expectation of α given R is thus just the 45 degree line,
i0 i i i0
which is continuous; the conditional expectation of β given R is flat, which is likewise continuous; and
i i0
the density of R is the normal density, hence continuous. Panel A of Figure 2 is a local linear regression
i0
estimate of the conditional expectation of β given R . The smoothness of the conditional expectation
i i0
indicates the validity of (A0).
However, even though (A0) is satisfied, agents’ endogenous labor supply creates an identification prob-
lem. The actual running variable is not R , but R , which is manipulated by those agents who find it
i0 i
worthwhile to do so. Panel B gives a local linear regression estimate of the conditional expectation of β
i
given R . This panel highlights the identification problem. The estimated curve is strongly discontinuous
i
near the earnings threshold—those agents who stand to gain from the program self-select to supply less
labor and hence are displaced from just to the right of the earnings threshold to just to the left, leading to
sample selection effects which operate discontinuously at the earnings threshold.
In empirical work, it is not possible to estimate conditional expectations such as those in panels A
and B, because β = Y − Y is unobservable. However, it is possible carry out a density test. Panel
i i1 i0
C presents an estimate of the density function of R , estimated using the local linear density estimation
i0
technique described in Section III, above. The density function is estimated and plotted for evaluation
points r = X ,X ,...,X . The bandwidth and binsize were chosen subjectively following inspection of
1 2 J
the automatic choices delivered by the algorithm outlined in Section III.B, above.19 The density estimate
is consistent with continuity at the earnings threshold, as expected.
Panel D instead gives the density function of R .20 In contrast with panel C, the estimated curve is
i
strongly discontinuous at the earnings threshold. The graph furnishes evidence of the economic behavior
described by the model above: agents self-select into the job training program by manipulating the value
of the running variable that will determine treatment assignment. This leads there to be slightly too few
agents just above the means test threshold, and slightly too many agents just below.
V. Simulation Evidence
Table 1 presents the results of a small simulation study on the performance of θ(cid:98) as an estimator and
as part of a testing procedure. In the table, “Design I” corresponds to the data generating process
underlying Panel C from Figure 2—50,000 independent draws from the N(12,3) distribution. There are
19The recommended binsize and bandwidth were b=0.03 and h=1.5, and I chose b=0.05 and h=0.9.
20In the interest of maintaining comparability, the binsize and bandwidth are kept the same in panels C and D.
12

1,000 replication data sets used. For each data set, I calculate θ(cid:98)using the binsize and bandwidth produced
by the algorithm specified in Section III.B (“A. Basic, Basic”). In addition to the “basic” implementation
of the algorithm, I consider a modified rule that undersmooths the bandwidth, setting it equal to half the
size of the basic bandwidth (“B. Basic, Half”). This allows assessment of the bias reduction that comes
with undersmoothing. Finally, I consider two non-basic binsizes, corresponding to half the basic binsize
width (“C. Half, Basic”) and twice the basic binsize width (“D. Twice, Basic”). This is to assess the
robustness of the estimator to binsize choices.
The simulation corroborates the good performance suggested by the theoretical work of Section III.
The estimator has generally small bias which declines as the bandwidth shrinks. As well, the standard
error suggested by the proposition represents well the approximate underlying standard deviation of the
estimator. Importantly, t-tests using the proposition have size of roughly 6 percent.
√
Approximating the distribution of nh(θ(cid:98)−θ) with a normal distribution is highly accurate. Figure 3
presents the normal Q-Q plot for the t-test of the (true) null hypothesis of continuity, where the t-tests
stem from the 1,000 replications reported in rows A and B of Table 1. Panel A (B) corresponds to row A
(B). It is clear from the figure that the quality of the fit is quite good, even far out into the tails where it
is most relevant for testing. Comparing panels A and B in the figure, we see that undersmoothing nearly
eliminates the estimator’s bias.
Perhaps surprisingly, these happy results carry over to much smaller samples. Design II reports results
for 1,000 replications of data sets with only 1,000 observations from the same data generating process as
Design I. The bias of the estimator remains manageable, and the accuracy of the variance estimates is
striking. The size of tests using the estimation scheme proposed, even with such small sample sizes, is
roughly 4 to 7 percent. Space precludes the presentation of any further normal Q-Q plots, but these are
similar to those shown in Figure 3, in that neither skewness nor fat tails is indicated.
Finally, these results also carry over to much more challenging density functions with multiple modes.
Design III reports results for 1,000 replications of data sets with 10,000 observations from a 75-25 mixture
of normals with mean 0 and variance 1 and mean 4 and variance 1. The cutoff point was taken to be at
2. This is a challenging point for local linear density estimation in this setting, because it is just to the
left of a local minimum of the true density, where the density function is strongly quadratic. However, the
estimator continues to enjoy bias of small magnitude, and t-tests using the estimator and its estimated
standard error lead to size of 5 to 7 percent.
13

VI. Empirical Example
One of the better examples of the regression discontinuity design is the incumbency study of Lee (2001).
Political scientists have postulated that there is an incumbency advantage for both parties and individual
candidates,wherebyhavingwontheelectiononcemakesiteasiertowintheelectionsubsequently. Credibly
establishing the magnitude of any incumbency advantage is challenging because of strong selection effects.
Lee notes that in a two-party system with majority rule, incumbency is assigned discontinuously at 50
percent on the basis of the popular vote and uses the regression discontinuity design to assess the party
incumbency effect for popular elections to the United States House of Representatives.
The complete manipulation phenomena described in Section II seems unlikely to occur in this instance,
because voters are unlikely to be able to coordinate to manipulate the vote tally, and because democratic
safeguards are presumably sufficient to prevent vote fraud.21 Thus, a natural expectation is for the density
function of the vote share to be smooth. I test this notion formally using the techniques outlined above.
Specifically, using data on the votes cast for each candidate in contested elections to the U.S. House
of Representatives involving a Democratic candidate, 1900-1990, I estimate the density function of the
“Democraticmargin”,definedasthefractionofallvotes(voteshare)receivedbytheDemocraticcandidate,
less the largest vote share received by any other candidate in the election.22 Defined in this way, the
Democratic candidate wins the election if and only if the Democratic margin is positive.23
Figure 4 gives an estimate of the density function of the Democratic margin. The curve was estimated
using the estimator outlined in Section III, with evaluation points r = X ,X ,...,X . The binsize and
1 2 J
bandwidth were chosen subjectively after using the automatic procedure outlined in Section III.B as a
pilot estimate. The automatic procedure in this case seems to oversmooth at the mode in this setting.24
The estimated curve gives little indication of strong discontinuity near zero. Indeed, the density appears
generally quite smooth. Importantly, the first-step histogram reveals that this is not the result of over-
smoothing. The estimated parameter θ(cid:98)is presented in Table 2, along with the proposition standard error.
As expected, a t-test of the null hypothesis of continuity fails to reject.
ThecompletemanipulationproblemdescribedinSectionIIisunlikelytooccurinafairpopularelection,
21Democraticsafeguardsmaynotalwaysbesufficient. Greenberg(2000)discussesthefamouslycontested1960presidential
election between Richard Nixon and John F. Kennedy. See also Snyder (2005), who uses the estimator described here to
analyze close elections to the United States House involving an incumbent.
221,591electionsduringthisperiodinvolveasinglecandidate. Ofthecontestedelections,95.3percentinvolveaDemocratic
candidate, and 92.5 percent involve a Republican candidate.
23ThisdefinitionoftherunningvariableisslightlydifferentfromthatinLee(2007), butdifferslittleasapracticalmatter,
particularly for the post-1948 period pertaining to Lee’s study.
24I use a binsize of b=0.004 and a bandwidth of h=0.02. The automatic procedure would select b=0.004 and h=0.13.
14

becausecoordinationofvotersisdifficultandthereislittlediscretioninmeasuringthevotetally. However,
in other election contexts, coordination is feasible and complete manipulation may be a concern.
A leading example of this type of coordination is roll call voting in the House of Representatives.
Coordination is expected in this context. First, the volume of bills before the House and the long tenure
of most representatives conspire to create a repeated game. Second, a representative’s vote is public
knowledge, allowing for credible commitments to contracts over voting. In such a context, side payments
for a representative’s vote do not have to involve (illegal) monetary compensation, but may pertain simply
to votes on future bills. Riker’s (1962) size principle then implies that the most likely bills to be put to
vote on the House floor are those expected to narrowly pass.
Figure 5 presents an estimated density function for the percent voting “yeay” on all roll call votes in
the House from 1857–2004.25,26 The curve was estimated using the estimator outlined in Section III, with
evaluation points r = X ,X ,...,X . The binsize and bandwidth were again chosen subjectively after
1 2 J
using the automatic procedure. Much more so than the vote share density, the roll call density exhibits
very specific features near the cutoff point that are hard for any automatic procedure to identify.27
The figure strongly suggests that the underlying density function is discontinuous at 50 percent. Out-
comes within a handful of votes of the cutoff are much more likely to be won than lost; the first-step
histogram indicates that the passage of a roll call vote by 1 to 2 votes is 2.6 times more likely than the
failure of a roll call vote by 1 to 2 votes. Although the magnitude of the effect is not as extreme, the
second-step smoother corroborates the suggestion of the first-step histogram. Table 2 presents the esti-
mated log discontinuity in the discontinuity, which is a large 52 percent. The effect is precisely estimated,
with a t-ratio of 6.6.
Theseempiricalresultsareconsistentwithamanipulationhypothesis. Inparticular, theresultssuggest
thatitwouldbeamistaketoviewthemajorityvoteelectionprocedureintheU.S.HouseofRepresentatives
as generating quasi-random assignment of policy decisions emerging from the House.
25Stratifying the votes into before and after 1900 subperiods results in highly similar estimates with less precision.
26The density estimator is allowed to be discontinuous at 50 percent but nowhere else, despite the existence of bills which
require a supermajority vote for passage (e.g., two-thirds approval for constitutional amendments and veto overrides), so 50
percent is not the cutoff for passage for all bills. However, bills requiring a supermajority for passage are rare, and the data
do not allow me to determine the cutoff for the given bill. Consequently, I focus on the potential discontinuity at 50 percent,
viewing this as being slightly attenuated due to the unobserved supermajority bills.
27Iuseabinsizeofb=0.003andabandwidthofh=0.03. Theautomaticprocedurewouldselectb=0.0025andh=0.114.
15

VII. Conclusion
This paper describes identification problems encountered in the regression discontinuity design pertaining
to manipulation of the running variable and describes a simple test for manipulation. The test involves
estimationofthediscontinuityinthedensityfunctionoftherunningvariableatthecutoff. Consistencyand
asymptotic normality of the log discontinuity in the density at the cutoff was demonstrated theoretically,
and inference procedures discussed. The methodology was applied to two distinct settings, one in which
manipulation is unexpected and is not detected, and another in which manipulation is expected and
demonstrated.
The context of most regression discontinuity applications is such that the treatment assignment rule is
public knowledge. I have argued that this will often make it plausible that the agents under study engage
in manipulation of the running variable in order to obtain desirable treatment assignments, and I have
emphasized that manipulation will often lead to violations of the assumptions necessary for identification.
Thestandardspecificationtestusedcurrentlyinregressiondiscontinuityapplicationsisatestforconti-
nuity of the conditional expectation of pre-determined characteristics in the running variable at the cutoff.
Such tests are a natural and powerful way to assess the plausibility of the identifying assumptions. The
density test proposed here complements these methods and is expected to be powerful when manipulation
is monotonic, as discussed above. The density test may be particularly important for applications where
pre-determined characteristics are not available, or are not relevant to the substantive topic studied.
| Appendix |     | I. Proof |     | of Proposition |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)
n
|     | Because    | of the | linearity | of Y    | = 1       | 1(g(R    |     | ) = X ), | we have |         |     |     |     |     |       |
| --- | ---------- | ------ | --------- | ------- | --------- | -------- | --- | -------- | ------- | ------- | --- | --- | --- | --- | ----- |
|     |            |        |           |         | j nb      | i=1      | i   | j        |         |         |     |     |     |     |       |
|     |            | S+ T+  | −S+       | T+      | (cid:88)J |          |     | S+       | −S+     | ht      |     |     |     |     |       |
|     |            | n,2    | n,0       | n,1 n,1 |           |          |     | n,2      | n,1     | j       |     |     |     |     |       |
|     | f(cid:98)+ | =      |           |         | =         | K(t )1(t | >   | 0)       |         |         | Y   |     |     |     | (A.1) |
|     |            | S+ S+  | −S+       | S+      |           | j        | j   | S+ S+    | −S+     | S+      | j   |     |     |     |       |
|     |            | n,2    | n,0       | n,1 n,1 | j=1       |          |     | n,2 n,0  |         | n,1 n,1 |     |     |     |     |       |
(cid:88)n (cid:88)J S + −S + ht (cid:88)n (cid:88)J (cid:88)n
|       |     | 1      |       |      |      | n ,2     | n ,1 | j 1   |     |     | 1   |          | 1    |       |     |
| ----- | --- | ------ | ----- | ---- | ---- | -------- | ---- | ----- | --- | --- | --- | -------- | ---- | ----- | --- |
|       |     | =      | K(t   | )1(t | > 0) |          |      | 1(g(R | )   | = X | ) ≡ | Z        | ≡    | Z     |     |
|       |     |        |       | j    | j    | S+ S+    | −S+  | S+    | i   | j   |     | ijn      |      | in    |     |
|       |     | n      |       |      |      |          |      | b     |     |     | n   |          | n    |       |     |
|       |     | i=1    | j=1   |      |      | n,2 n,0  | n,1  | n,1   |     |     |     | i=1 j=1  |      | i=1   |     |
|       |     |        |       |      |      | (cid:80) |      |       |     |     |     | (cid:80) |      |       |     |
|       |     |        |       | S+   | hk   | J        |      | 0)tk, |     | T+  | hk  | J        |      | 0)tkY |     |
| where | t   | = (X − | c)/h, |      | ≡    | K(t      | )1(t | >     | and |     | ≡   | K(t      | )1(t | >     | ,   |
|       | j   | j      |       | n,k  |      | j=1      | j    | j     | j   | n,k |     | j=1      | j j  |       | j j |
and analogously for f(cid:98)−. The proof proceeds by calculating E[f(cid:98)+] and V[f(cid:98)+] and verifying the skewness
conditionoftheLyapunovcentrallimittheorem(Rao1965, p. 107), whichappliessinceZ isindependent
in
i0
of Z i0n for 6= i. Independence follows since Z in is just a transformation of R i and since X 1 ,X 2 ,...,X J
are constants (see footnote 13). By Riemann approximation (see Cheng 1994, Lemma 4, for example), we
(cid:82)
∞
have S+ = (hk+1/b)S++O(hk−1b), where S+ = tkK(t)dt, k = 0,1,2,... For the triangle kernel with
|     | n,k    |             | k   |       |      | k                 |     | 0       |     |           |           |     |     |     |       |
| --- | ------ | ----------- | --- | ----- | ---- | ----------------- | --- | ------- | --- | --------- | --------- | --- | --- | --- | ----- |
| k = | 0,1,2, | S+ is equal | to  | 1, 1, | and  | 1 , respectively. |     | We have |     |           |           |     |     |     |       |
|     |        | k           |     | 2 6   | 12   |                   |     |         |     |           |           |     |     |     |       |
|     |        |             |     |       |      |                   |     |         |     | (cid:181) | (cid:182) |     |     |     |       |
|     |        |             |     | S     | + −S | + ht              |     | b       |     |           | b2        |     |     |     |       |
|     |        |             |     |       | n ,2 | n ,1 j            |     |         |     |           |           |     |     |     |       |
|     |        |             |     |       |      |                   | =   | 6(1−2t  | )+O |           |           |     |     |     | (A.2) |
|     |        |             |     | S+    | S+   | −S+ S+            |     | h       | j   |           | h2        |     |     |     |       |
|     |        |             |     | n,2   | n,0  | n,1 n,1           |     |         |     |           |           |     |     |     |       |
16

Using Taylor and Riemann approximation we have
(cid:181) (cid:182)
(cid:88)J b b (cid:161) (cid:162)
E[f(cid:98)+] = E[Z ] = K(t )1(t > 0)6(1−2t )f(c+ht )+O +O b2 (A.3)
in j j j j
h h
j=1
(cid:90) (cid:181) (cid:182)
1 b (cid:161) (cid:162)
= (1−t)6(1−2t)f(c+ht)dt+O +O b2
h
0 (cid:181) (cid:182)
1 1 b (cid:161) (cid:162)
= f+−h2 f+00 +O(h3)+O +O b2
210 h
 
1 1 (cid:161) (cid:162) 1 (cid:88)J (cid:88)J
V[f(cid:98)+] = V[Z ] = E[Z2 ]−E2[Z ] =  E[Z Z ]−E2[Z ] (A.4)
n in n in in n ijn ikn in
j=1k=1
 
(cid:181) (cid:182)
1 (cid:88)J b2 1 b2
=  K2(t )1(t > 0)36(1−2t )2 p −E2[Z ]+O
n h2 j j j b2 j in nh2
j=1
(cid:181)(cid:90) (cid:182) (cid:181) (cid:182) (cid:181) (cid:182)
1 1 b2 b
= (1−t)236(1−2t)2f(c+ht)dt−hE2[Z ] +O +O
nh in nh2 n
0 (cid:181) (cid:182)
1 24 1
= f++O
nh 5 n
since E[Y ] = f(X )+O(b2), where the only terms from the double summation which matter are those for
j j
which j = k since the histogram bins are mutually exclusive. For the Lyapunov condition, calculate
 
(cid:163)(cid:175) (cid:175) (cid:164) (cid:163)(cid:175) (cid:175) (cid:164) (cid:88)J (cid:88)K (cid:88)L
E (cid:175)Z −E[Z ](cid:175)3 ≤ 8E (cid:175)Z (cid:175)3 ≤ 8E |Z |·|Z |·|Z | (A.5)
in in in ijn ikn iln
j=1k=1 l=1
(cid:181) (cid:182)
(cid:88)J (cid:175) (cid:175) 1 (cid:88)J b b
= 8 E[(cid:175)Z (cid:175)3 ] = 8 K3(t )1(t > 0)63|1−2t |3f(c+ht )+O
ijn h2 h j j j j h
j=1 j=1
(cid:90) (cid:181) (cid:182) (cid:181) (cid:182)
1 1 b 1
= 8 (1−t)363|1−2t|3f(c+ht)dt+O = O
h2 h h2
0
Combining the expression for the variance with the skewness bound, we have
(cid:179) (cid:80) (cid:175) (cid:175) (cid:180) 1/3 (cid:179) (cid:161) (cid:177) (cid:162) (cid:180) 1/3
n E[(cid:175)Z −E[Z ](cid:175)3 ] O n h2 (cid:179) (cid:180)
i=1 in in
(cid:179) (cid:180) ≤ (cid:179) (cid:180) = O (nh)−1/6 (A.6)
(cid:80) 1/2 (cid:161) (cid:177) (cid:162) 1/2
n V[Z ] O n h
i=1 in
so that the Lyapunov condition is satisfied since nh → ∞. Thus, and by symmetry,
(cid:181) (cid:182) (cid:181) (cid:182)
√ (cid:179) (cid:180) 24 √ (cid:179) (cid:180) 24
nh f(cid:98)+−f+ − d → N B+, f+ and nh f(cid:98)−−f− − d → N B−, f− (A.7)
5 5
where B+ = −H 1 f+00 and B− = −H 1 f−00. To strengthen this result to joint asymptotic normality,
20 20
define U = λ+Z+ + λ−Z−, where the Z from above is redefined to be Z+ and Z− denotes the
in in in in in in
analogous quantity to the left of c. Observe that U is independent of U for all i0 6= i. Then we have
in i0n
E[U ] = λ+f+ +λ−f− +O(h2) and V[U ] = (24/5)(λ+)2(f+/h)+(24/5)(λ−)2(f−/h)+o(1/h), where
in in
the latter follows since C[Z+,Z−] = −E[Z+]E[Z−] = −f+f− + O(h2). Using the results from above,
in in in in
we have E[|U − E[U ]|3] ≤ 8E[|U |3] ≤ 8|λ+|3E[|Z+|3] + 8|λ−|3E[|Z−|3] = O(1/h2) and it is then
in in in in in
straightforward to verify the Lyapunov condition as above. Since this holds for every vector (λ+,λ−), the
17

Cram´er-Wold device (White 2001, p. 114) implies joint asymptotic normality with a diagonal asymptotic
(cid:179) (cid:180)
0
variance matrix. Define τ(f+,f−) = lnf+ −lnf− = θ, note that ∇τ = 1 , −1 , and apply the delta
f+ f−
method to conclude
|              |             |             | (cid:181) | (cid:181) | (cid:182)(cid:182) |       |
| ------------ | ----------- | ----------- | --------- | --------- | ------------------ | ----- |
|              |             | √ (cid:179) | (cid:180) | 24 1      | 1                  |       |
|              |             | θ(cid:98)−θ | d         |           |                    |       |
|              |             | nh          | − → N     | B,        | +                  | (A.8) |
|              |             |             |           | 5 f+      | f−                 |       |
| B+           | B−          |             |           |           |                    |       |
| where B = −  | . (cid:165) |             |           |           |                    |       |
| f+           | f−          |             |           |           |                    |       |
| Appendix II. | Data        |             |           |           |                    |       |
Data on popular elections to the U.S. House of Representatives are taken from ICPSR Study # 7757.
These are the same data used by Lee (2001, 2007), but I have engaged in neither the data augmentation
nor the cleaning procedures he conducted. Data on roll call votes are taken from
http://www.voteview.com/partycount.htm, awebsitemaintainedbyKeithT.Poole oftheUniversityof
California,SanDiego. ThissamewebsiteisthebasisforthedataonDW-Nominatescores. Finally,dataon
partycontroloftheHousearetakenfromhttp://arts.bev.net/roperldavid/politics/congress.htm,
a website maintained by L. David Roper of the Virginia Polytechnic Institute and State University.
Alldataandprogramsareavailablefromtheauthorforaperiodof3yearsfromthedateofpublication.
References
Aigner, Dennis J., Takeshi Amemiya, and Dale J. Poirier, “On the Estimation of Production Frontiers:
Maximum Likelihood Estimation of the Parameters of a Discontinuous Density Function,” Interna-
| tional Economic | Review, | 1976, 17 | (2), 377–396. |     |     |     |
| --------------- | ------- | -------- | ------------- | --- | --- | --- |
Angrist, Joshua D., Guido W. Imbens, and Donald B. Rubin, “Identification of Causal Effects Using
Instrumental Variables,” Journal of the American Statistical Association, June 1996, 91 (434), 444–
455.
Becker, Gary S., The Economics of Discrimination, Chicago: University of Chicago Press, 1957.
Bouezmarni, Taoufik and Olivier Scaillet, “Consistency of Asymmetric Kernel Density Estimators and
Smoothed Histograms with Application to Income Data,” Econometric Theory, April 2005, 21 (2),
390–412.
Card, David E., “The Causal Effect of Education on Earnings,” in Orley Ashenfelter and David E. Card,
eds., The Handbook of Labor Economics, Vol. 3A, Amsterdam: Elsevier, 1999.
Cheng, Ming-Yen, “On Boundary Effects of Smooth Curve Estimators (Dissertation),” April 1994. Un-
published manuscript Series # 2319, Institute for Statistics, University of North Carolina.
, “A Bandwidth Selector for Local Linear Density Estimators,” Annals of Statistics, 1997, 25 (3),
1001–1013.
, “Boundary Aware Estimators of Integrated Density Products,” Journal of the Royal Statistical
| Society, Series | B, 1997, | 59 (1), 191–203. |     |     |     |     |
| --------------- | -------- | ---------------- | --- | --- | --- | --- |
, Jianqing Fan, and James S. Marron, “Minimax Efficiency of Local Polynomial Fit Estimators at
Boundaries,” May 1993. Unpublished manuscript Series # 2098, Institute for Statistics, University of
North Carolina.
, , and , “On Automatic Boundary Corrections,” The Annals of Statistics, August 1997, 25
(4), 1691–1708.
18

Chernozhukov, Victor and Han Hong, “Likelihood Estimation and Inference in a Class of Nonregular
Econometric Models,” Econometrica, September 2004, 72 (5), 1445–1480.
Chu,C.K.andP.E.Cheng,“EstimationofJumpPointsandJumpValuesofaDensityFunction,”Statistica
| Sinica, 1996, | 6 (1), | 79–96. |     |     |     |
| ------------- | ------ | ------ | --- | --- | --- |
Cline, Darren B.H. and Jeffrey D. Hart, “Kernel Estimation of Densities with Discontinuities or Discon-
| tinuous Derivatives,” |     | Statistics, | 1991, | 22 (1), | 69–84. |
| --------------------- | --- | ----------- | ----- | ------- | ------ |
Davison, Anthony C. and David V. Hinkley, Bootstrap Methods and Their Application, New York: Cam-
| bridge University |     | Press, | 1997. |     |     |
| ----------------- | --- | ------ | ----- | --- | --- |
Deaton, Angus, The Analysis of Household Surveys : A Microeconomic Approach to Development Policy,
| Washington, | D.C.: | World | Bank, 1997. |     |     |
| ----------- | ----- | ----- | ----------- | --- | --- |
DiNardo,JohnE.andDavidS.Lee,“EconomicImpactsofNewUnionizationonPrivateSectorEmployers:
1984-2001,” Quarterly Journal of Economics, November 2004, 119 (4), 1383–1441.
DiNardo, John, Nicole Fortin, and Thomas Lemieux, “Labor Market Institutions and the Distribution of
Wages, 1973-1992: A Semi-Parametric Approach,” Econometrica, 1996, 64 (5), 1001–1044.
Fan, Jianqing and Irene Gijbels, Local Polynomial Modelling and Its Applications, New York: Chapman
| and Hall, | 1996. |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Gawronski, Wolfgang and Ulrich Stadtmu¨ller, “On Density Estimation by Means of Poisson’s Distribu-
| tion,” Scandinavian |     | Journal | of Statistics, | 1980, | 7 (2), 90–94. |
| ------------------- | --- | ------- | -------------- | ----- | ------------- |
and , “Smoothing Histograms by Means of Lattice- and Continuous Distributions,” Metrika,
| 1981, 28 | (3), 155–164. |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- |
Greenberg, David, “Was Nixon Robbed? The Legend of the Stolen 1960 Presidential Election,” Slate,
| October 16, | 2000. |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
Hahn, Jinyong, Petra Todd, and Wilbert van der Klaauw, “Identification and Estimation of Treatment
Effects with a Regression Discontinuity Design,” May 1999. NBER Working Paper # 7131.
, ,and ,“IdentificationandEstimationofTreatmentEffectswithaRegressionDiscontinuity
| Design,” | Econometrica, |     | February | 2001, 69 (1), | 201–209. |
| -------- | ------------- | --- | -------- | ------------- | -------- |
Hall, Peter, “Effect of Bias Estimation on Coverage Accuracy of Bootstrap Confidence Intervals for a
Probability Density,” The Annals of Statistics, June 1992, 20 (2), 675–694.
, Ian McKay, and Berwin A. Turlach, “Performance of Wavelet Methods for Functions with Many
| Discontinuities,” |     | Annals | of Statistics, | 1996, | 24 (6), 2462–2476. |
| ----------------- | --- | ------ | -------------- | ----- | ------------------ |
H¨ardle,WolfgangandOliverLinton,“AppliedNonparametricMethods,”inRobertF.EngleandDanielL.
McFadden, eds., The Handbook of Econometrics, Vol. 4, New York: Elsevier, 1994, pp. 2297–2341.
Heckman, James J., “The Scientific Model of Causality,” Sociological Methodology, August 2005, 35 (1),
1–98.
,SergioUrzua,andEdwardVytlacil,“UnderstandingInstrumentalVariablesinModelswithEssential
Heterogeneity,” Review of Economics and Statistics, August 2006, 88 (3), 389–432.
Horowitz, Joel L., “The Bootstrap,” in James J. Heckman and Edward Leamer, eds., The Handbook of
| Econometrics, | Vol. | 5, New | York: Elsevier, | 2001, | pp. 3463–3568. |
| ------------- | ---- | ------ | --------------- | ----- | -------------- |
19

Imbens, Guido W. and Joshua D. Angrist, “Identification and Estimation of Local Average Treatment
Effects,” Econometrica, March 1994, 62 (2), 467–475.
Jacob, Brian A. and Lars Lefgren, “Remedial Education and Student Achievement: A Regression-
Discontinuity Analysis,” Review of Economics and Statistics, 2004, 86 (1), 226–244.
Jones, M. Chris, “Discretized and Interpolated Kernel Density Estimates,” Journal of the American
Statistical Assocation, 1989, 84 (407), 733–741.
Lee, David S., “The Electoral Advantage to Incumbency and Voters’ Valuation of Politicians’ Experience:
A Regression Discontinuity Analysis of Elections to the U.S. House,” August 2001. NBER Working
Paper # 8441.
, “Randomized Experiments from Non-random Selection in U.S. House Elections,” Journal of Econo-
metrics, forthcoming 2007.
Marron, James S. and David Ruppert, “Transformations to Reduce Boundary Bias in Kernel Density
Estimation,” Journal of the Royal Statistical Society, Series B, 1994, 56 (4), 653–671.
Pagan, Adrian and Aman Ullah, Nonparametric Econometrics, New York: Cambridge University Press,
1999.
Rao, C. Radhakrishna, Linear Statistical Inference and Its Applications, 1st ed., New York: John Wiley
and Sons, 1965.
Rice, John, “Boundary Modification for Kernel Regression,” Communications in Statistics, A, 1984, 13
(7), 893–900.
Riker, William H., The Theory of Political Coalitions, New Haven: Yale University Press, 1962.
Rubin, Donald B., “Randomization Analysis of Experimental Data: The Fisher Randomization Test:
Comment,” Journal of the American Statistical Association, September 1980, 75 (371), 591–593.
, “Statistics and Causal Inference: Which Ifs Have Causal Answers,” Journal of the American Sta-
tistical Association, December 1986, 81 (396), 961–962.
Saez, Emmanuel, “Do Taxpayers Bunch at Kink Points?,” September 1999. NBER Working Paper #
7366.
, “Do Taxpayers Bunch at Kink Points?,” April 2002. Unpublished manuscript, University of Cali-
fornia, Berkeley.
Schuster, Eugene F., “Incorporating Support Constraints into Nonparametric Estimators of Densities,”
Communications in Statistics, A, 1985, 14 (5), 1123–1136.
Sheather, Simon J. and M. Chris Jones, “A Reliable Data-Based Bandwidth Selection Method for Kernel
Density Estimation,” Journal of the Royal Statistical Society, Series B, 1991, 53 (3), 683–690.
Snyder,Jason,“DetectingManipulationinU.S.HouseElections,”January2005. Unpublishedmanuscript,
Haas School of Business, University of California, Berkeley.
Stone, Mervyn, “Cross-Validation and Multinomial Prediction,” Biometrika, December 1974, 61 (3), 509–
515.
, “Asymptotics For and Against Cross-Validation,” Biometrika, April 1977, 64 (1), 29–35.
20

van der Klaauw, Wilbert, “Estimating the Effect of Financial Aid Offers on College Enrollment: A
Regression-Discontinuity Approach,” International Economic Review, November 2002, 43 (4), 1249–
1287.
White, Halbert, Asymptotic Theory for Econometricians, San Diego: Academic Press, 2001.
21

Figure 2. Hypothetical Example:
Gaming the System with an Income-Tested Job Training Program

A. Conditional Expectation of Returns to Treatment  B. Conditional Expectation of Returns to Treatment
with No Pre-Announcement and No Manipulation with Pre-Announcement and Manipulation
| 0.50                             |     |     | 0.50                             |     |     |     |
| -------------------------------- | --- | --- | -------------------------------- | --- | --- | --- |
| etamitsE noitatcepxE lanoitidnoC |     |     | etamitsE noitatcepxE lanoitidnoC |     |     |     |
| 0.30                             |     |     | 0.30                             |     |     |     |
| 0.10                             |     |     | 0.10                             |     |     |     |
`
| -0.10 |        |     | -0.10 |        |     |     |
| ----- | ------ | --- | ----- | ------ | --- | --- |
| -0.30 |        |     | -0.30 |        |     |     |
| -0.50 |        |     | -0.50 |        |     |     |
| 5     | 10     | 15  | 20 5  | 10     | 15  | 20  |
|       | Income |     |       | Income |     |     |

|     | C. Density of Income  |     |     | D. Density of Income  |     |     |
| --- | --------------------- | --- | --- | --------------------- | --- | --- |
with No Pre-Announcement and No Manipulation with Pre-Announcement and Manipulation
| 0.16             |        |     | 0.16             |        |     |     |
| ---------------- | ------ | --- | ---------------- | ------ | --- | --- |
| 0.14             |        |     | 0.14             |        |     |     |
| 0.12             |        |     | 0.12             |        |     |     |
| etamitsE ytisneD |        |     | etamitsE ytisneD |        |     |     |
| 0.10             |        |     | 0.10             |        |     |     |
| 0.08             |        |     | 0.08             |        |     |     |
| 0.06             |        |     | 0.06             |        |     |     |
| 0.04             |        |     | 0.04             |        |     |     |
| 0.02             |        |     | 0.02             |        |     |     |
| 0.00             |        |     | 0.00             |        |     |     |
| 5                | 10     | 15  | 20 5             | 10     | 15  | 20  |
|                  | Income |     |                  | Income |     |     |

Figure 3. Quality of Normal Approximation
A. t-test Based on Proposition Standard Error,
No Undersmoothing
4
3
2
1
0
-1
-2
-3
-4
-4 -3 -2 -1 0 1 2 3 4
Quantile of Normal Distribution
noitubirtsiD
tset-t
fo
elitnauQ
B. t-test Based on Proposition Standard Error,
Undersmoothing
4
3
2
1
0
-1
-2
-3
-4
-4 -3 -2 -1 0 1 2 3 4
Quantile of Normal Distribution
noitubirtsiD
tset-t
fo
elitnauQ

Figure 4. Democratic Vote Share Relative to Cutoff:
Popular Elections to the House of Representatives, 1900-1990
150
120
90
60
30
0
-1 -0.8 -0.6 -0.4 -0.2 0 0.2 0.4 0.6 0.8 1
Democratic Margin
tnuoC
ycneuqerF
1.60
1.40
1.20
1.00
0.80
0.60
0.40
0.20
0.00
etamitsE
ytisneD
Figure 5. Percent Voting Yeay:
Roll Call Votes, U.S. House of Representatives, 1857-2004
300
250
200
150
100
50
0
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Percent Voting in Favor of Proposed Bill
tnuoC
ycneuqerF
2.50
2.00
1.50
1.00
0.50
0.00
etamitsE
ytisneD

Table 1. Simulation Results
Rule for Binsize, Range of Range of Estimator Proposition Standard Error
Design Bandwidth Binsizes (b) Bandwidths (h) Bias Std. Dev. Mean Size, t-test
I A. Basic, Basic [0.027, 0.027] [1.45, 1.56] -0.0064 0.0353 0.0345 0.0630
B. Basic, Half [0.027, 0.027] [0.73, 0.78] -0.0018 0.0513 0.0489 0.0600
C. Half, Basic [0.013, 0.013] [1.45, 1.54] -0.0063 0.0354 0.0346 0.0640
D. Twice, Basic [0.053, 0.054] [1.46, 1.61] -0.0066 0.0351 0.0343 0.0600
II A. Basic, Basic [0.182, 0.196] [2.44, 3.45] -0.0420 0.1800 0.1763 0.0580
B. Basic, Half [0.183, 0.196] [1.22, 1.72] -0.0059 0.2564 0.2532 0.0430
C. Half, Basic [0.091, 0.098] [2.46, 3.44] -0.0424 0.1793 0.1757 0.0670
D. Twice, Basic [0.366, 0.393] [2.35, 3.46] -0.0423 0.1809 0.1775 0.0670
III A. Basic, Basic [0.040, 0.040] [0.851, 1.01] 0.0252 0.1598 0.1484 0.0650
B. Basic, Half [0.040, 0.040] [0.426, 0.506] 0.0011 0.2079 0.2010 0.0560
C. Half, Basic [0.020, 0.020] [0.812, 0.950] 0.0222 0.1608 0.1516 0.0610
D. Twice, Basic [0.080, 0.081] [0.912, 1.11] 0.0307 0.1575 0.1440 0.0690
Notes: Table presents simulation results for 3 different data generating processes and 4 different binsize and bandwidth
selection rules. See text for details.

Table 2. Log Discontinuity Estimates
Popular
|     | Elections Roll Call Votes |         |
| --- | ------------------------- | ------- |
|     | -0.060                    | 0.521   |
|     | (0.108)                   | (0.079) |
| N   | 16,917                    | 35,052  |
Note: Standard errors in parentheses.  See text for details.