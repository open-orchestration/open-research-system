Identification and Estimation of Local Average Treatment Effects

Guido W. Imbens; Joshua D. Angrist

Econometrica, Vol. 62, No. 2. (Mar., 1994), pp. 467-475.

Stable URL:
http://links.jstor.org/sici?sici=0012-9682%28199403%2962%3A2%3C467%3AIAEOLA%3E2.0.CO%3B2-2

Econometrica is currently published by The Econometric Society.

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at
http://www.jstor.org/about/terms.html. JSTOR's Terms and Conditions of Use provides, in part, that unless you have obtained
prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in
the JSTOR archive only for your personal, non-commercial use.

Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at
http://www.jstor.org/journals/econosoc.html.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed
page of such transmission.

The JSTOR Archive is a trusted digital repository providing for long-term preservation and access to leading academic
journals and scholarly literature from around the world. The Archive is supported by libraries, scholarly societies, publishers,
and foundations. It is an initiative of JSTOR, a not-for-profit organization with a mission to help the scholarly community take
advantage of advances in technology. For more information regarding JSTOR, please contact support@jstor.org.

http://www.jstor.org
Sat Mar 29 17:06:27 2008

Econornetrica, Vol. 62, No. 2 (March,  19941,467-475

IDENTIFICATION AND ESTIMATION  O F  LOCAL AVERAGE

TREATMENT EFFECTS'

1.  INTRODUCTION

RANDOMASSIGNMENT  OF  TREATMENT  and  concurrent  data  collection  on  treatment  and
control groups is the norm in medical evaluation research. In contrast, the use of  random
assignment  to  evaluate  social  programs  remains  controversial.  Following  criticism  of
parametric  evaluation  models  (e.g.,  Lalonde  (1986)), econometric  research  has  been
geared  towards  establishing  conditions  that  guarantee  nonparametric  identification  of
treatment effects in observational  studies, i.e. identification without  relying on functional
form  restrictions  or  distributional assumptions.  The focus has been  on identification  of
average  treatment  effects  in  a  population  of  interest,  or on  the  average  effect  for  the
subpopulation  that  is  treated.  The  conditions  required  to  nonparametrically  identify
these  parameters  can  be  restrictive,  however,  and  the  derived  identification  results
fragile. In particular, results in Chamberlain  (19861, Manski (1990),Heckman (1990),and
Angrist  and  Imbens  (1991) require  that  there  be  some  subpopulation  for  whom  the
probability  of  treatment is  zero,  at least in the limit.

The  purpose  of  this  paper  is  to  show  that  even  when  there  is  no  subpopulation
available for whom  the probability  of  treatment is zero, we  can  still identify  an  average
treatment  effect of  interest  under  mild  restrictions  satisfied  in  a  wide  range  of  models
and  circumstances.  We  call  this  a  local  average  treatment  effect  (LATE).  Examples  of
problems  where  the  local  average  treatment  effect  is  identified  include  latent  index
models  and  evaluations  based  on natural  experiments  such  as  those  studied  by  Angrist
(1990)  and  Angrist  and  Krueger  (1991).  LATE  is  the  average  treatment  effect  for
individuals whose treatment status is influenced by  changing an exogenous regressor  that
satisfies an  exclusion restriction.

2.  IDENTIFICATION OF CAUSAL EFFECTS

The framework  we  use  is  essentially  similar  to  that  outlined  by  Rubin  (1974, 1990),
Heckrnan  (1990), and  described  in  our  previous  paper  on  identification  of  treatment
effects  (Angrist  and  Imbens  (1991)).  It  defines  causal  effects  in  terms  of  potential
outcomes  or  counterfactuals  rather  than  in  terms  of  the  parameters  of  a  regression
model. Let  y ( 0 )  be the response without the treatment or program  for individual i.  x ( 1 )
is  the  response  with  treatment.  Di  is  an  indicator  of  treatment.  We  observe  Di  and
x = y ( D i )  = D i .  x ( 1 )  + ( 1  - D i ) .  y ( 0 )  for  a  random  sample of  individuals. The individ-
ual  treatment  effect, or  causal  effect, is  y ( 1 )  - y(O) but  since  x ( l )   and  y(O) are never
observed for the same individual we are forced to rely on comparisons between different
individuals and estimate  average treatment effects.

The  solution  to  the  identification  problem  dominating  the  evaluation  of  medical
treatments is random  assignment  to treatment  and  control  groups. This guarantees that
E [ y ( j ) J D i= 01  = E [ y ( j ) I D ,= 11  for j  = 0 , l .  In  that  case  an  unbiased  estimator for  the

'We  are grateful  to Gary  Chamberlain,  Larry  Katz,  Don  Rubin,  Geert  Ridder,  Jim  Heckrnan,
Charles  Manski,  seminar  participants  at  Harvard/MIT,  New  York  University,  the  Institute  for
Research on Poverty at the University of Wisconsin, and the University of  Chicago, two anonymous
referees  and a co-editor for comments and suggestions, and to the  NSF for financial support  under
Grants SES9122477 and SES9122627.

468

G.  W.IMBENS  AND  J. D.  ANGRIST

average  treatment  effect,  E[Y,.(l) - Y,(O)],  is  available  in  the  difference  of
treatment/control  averages, EDiY,/EDi - E(1-  Di)Y,/E(l  - Di).

the

In  the  evaluation  of  social programs,  researchers  have  often  relied  on  instrumental
variables  strategies to identify treatment effects. We define an instrumental variable,  Zi,
to be  a variable  independent  of  the  responses  Y,(O) and  Y,(l), and  correlated  with  the
participation  indicator Di. In  order to formalize this, let 2 be the support of  Zi. Define
for  each  z E 3 a  random variable  D i ( ~ ) . 2  Di(z) is  equal to zero  if  an  individual would
not  participate  if  he  or  she had  the  instrument  Zi equal to  z,  and it  is  equal to  one if
that individual would participate with  Z = z. Clearly, we cannot observe the entire set of
potential participation  indicators {Di(z)lz E 31, but we can think about them in the same
way  we  think  about  Y,(O)  and  Y,(l)  even  though  they  are  not  observed.  We  observe
(Zi,D,,Y,)  for  a  random  sample  of  individuals,  where  D i= Di(Zi), the  participation
indicator  associated with  Zi, and  Y,= y(Di), the response variable  given  the participa-
tion  status  Di. The formal condition  defining an instrument is the following.

CONDITION1(Existence of  Instruments):  Let  Z be  a random uariable such  that  (i)  for
all  w E 3  the  triple  (Y,(O), Y,(1), Di(w))  is  jointly  independent  of  Zi,  and,  (ii) P(w)=
E[Di lZi = w] is a nontriuial function  of  w.

Part  (ii)  of  Condition  1 is  testable  in  a  given  application.  Part  (i)  is  similar  to  an
exclusion restriction  in a regression model. It is not testable and has to be considered  on
a case by  case basis. Note that random assignment of  Zi does not guarantee that part (i)
is  satisfied  because  although  random  assignment  implies  that  Zi  is  independent  of
Di(w),  it  does  not  imply  that  Zi  is  independent  of  Y,(O),Y,(l). In  a  related  paper
(Angrist, Imbens, and Rubin (1993)), we  discuss conditions  similar to this in great detail,
and investigate the implications of  violations of  these  conditions.

In  econometric program  evaluation,  linear  latent  index  models  are  often  employed
(see, for  example, Heckman  and  Robb (1985), and Heckman  and Hotz (1989)). In  these
models, the participation decision is typically modeled  by  a latent index

with the observed participation indicator, Di, related to the unobserved latent index, D;,
by

The response, Y,,is related  to the treatment via  the equation

In this notation  the counterfactuals are Y,(O) = P o+ s,, Y,(1) = P o+ PI + s,, and  D,(z) =
lIy,  + z .y l  + V,  > 0)  for  z E 2,where  11.1 is  the  indicator  function. In  this  regression
framework  Condition  1 is satisfied if  Z,  is  independent  of  E ,   and  v,. The advantage  of
our setup is that it  allows us to avoid the functional form and  distributional  assumptions
inherent  in these models.

Chamberlain (1986), Heckman (1990), and Angrist and Imbens (1991) have each noted
that Condition  1 by  itself  is not  enough to identify any  average treatment e f f e ~ t . ~  To see

The D,(z) notation  was suggested  to us by  Gary Chamberlain.
Manski  (1990) shows conditions  similar  to Condition  1 are  informative  in  the  sense  that  they
sharpen bounds on population averages of  bounded  functions  of  the treatment effect. However, we
focus  on  (point)  identification  of  average  treatment  effects  without  restrictions  on  the  range  of
outcomes.

LOCAL  AVERAGE  TREATMENT  EFFECTS

469

this,  compare  the  expectation  E [ y l Z i  = z ]  for  two  points  of  support,  z  and  w,  with
P ( z )  > P ( w ) : ~

- E [ D , ( w ) .  y ( 1 )  + ( I  - D,(w)) . E;.(O)IZ= w].

Using the independence  in  Condition  1, this is equal to

Equation  (1)  highlights  an  identification  problem  arising  in  the  use  of  IV  to  estimate
average  treatment  effects. The difference  in  equation  (1)  can  be  zero  or  even  negative
despite a strictly positive causal effect of  D  on  Y  for  all individuals. For example, if

the  difference  is zero. Intuitively the problem  here is that the treatment effect for those
who shift from nonparticipation to participation  when  Z  is switched from  z  to w can be
cancelled out by  the treatment effect of  those who shift from participation  to nonpartici-
pation.

One commonly invoked condition  that  prevents  this  is  the  assumption  of  a  constant
treatment effect, a = X(1) - y(0), for all individuals in  the population. Then  E[Y,IZ, =
z ]  - E[Y,IZ, = w]  is  equal  to  a . [P(z) - P(w)],  and  a  is  clearly  identified.  A  second
approach  is  to  assume  the  existence  of  a  value  of  the  instrument,  w,  such  that  the
probability  of  participation  conditional  on  that  value,  P(w),  is  equal  to  zero.  Then
Pr [D,(z) - Di(w) = - 11= 0,  and  the  difference  EIY;IZi =z ]  - E[Y, IZ, = w] is  equal to
P(z).E[Y,(l) - Y,(0)(Di(z)= 11. In  this case the average treatment  effect for the treated
is  identified.  This  type  of  condition  is  explored  in  Heckman  (1990)  and  Angrist  and
Imbens  (1991).  Below  we  present  a  third  assumption  that  solves  the  identification
problem  by  preventing  shifts in participation status in  the opposite  direction.

CONDITION2  (Monotonicity):  For  all  z, w E3, either  Di(z) > Di(w)  for  all  i,  or

Di(z) 9 Di(w) for  all i.

This  condition  ensures  that  the  instrument  affects  the  participation  or  selection
decision in  a monotone way. That is, if  people are more likely, on average, to participate
given  Z = w than given Z  = z, then  anyone  who would participate given Z = z  must also
participate  given  Z = w.  Similar  to  Condition  1,  this  condition  is  fundamentally
untestable, and its validity has to be argued in the context of  a particular application (see
Section  4).  Note  that  in  the  linear  latent  index  model  discussed  above,  Condition  2  is
automatically satisfied.

We  assume that  these conditional expectations  are finite.

470

G .  W.  IMBENS  AND  J.  D. ANGRIST

Our main  result  is the following:

THEOREM1:  If  Conditions  1 and  2  hold,  then  we  can  identify  the following  auerage

treatment effect:

from  the joint  distribution of  Y,  D, and Z, for  all z and w in  the support of  Z such  that
EIE;IZi = z ]  and E[Y IZi = w] are finite, and P ( z )  # P(w).

PROOF: Let  Condition  2  be  satisfied  with  Di(z)  Di(w).  Then  Pr [Di(z) - D,(w) =

- 11 = 0 which implies that the second term  in  (1) is  equal to zero, and

Dividing both  sides by  P(z) - P(w) shows that the local average treatment effect can be
Q.E.D.
expressed in terms of  moments of  the joint  distribution  of  (Y, D, 2).

The local average treatment effect is analogous to a regression coefficient estimated in
linear  models with  individual  effects using panel  data.  In  models with  fixed  effects, the
data are only informative about the impact of  binary  regressors on  individuals for whom
the value  of  the regressor  changes over the period  of  observation. Under Theorem  1 the
treatment  effect  identified  is  an  average  for  those  who  can  be  induced  to  change
participation status by  a change in  the  instrument.

3.  INSTRUMENTAL VARIABLES ESTIMATION

Theorem 1implies that local average treatment effects can be estimated by  comparing
the  average of  outcome Y and treatment  D  at two different values of  the instrument  Z.
This is exactly what the instrumental variables approach estimates in the case of  a binary
instrument.  One way  to exploit a multi-valued  instrument is to estimate the ratio  of  the
covariance of  Y and some scalar function  g(Z), and the covariance of  D  and  g(Z). If  Z
is a scalar random variable, then  the choice g(z) =z  leads to the standard  IV estimator.
If  Z  is  a vector,  g(z) is often  an  estimate of  P(z). To guarantee that  the  IV estimand,
Cov(Y, g(Z))/Cov(D,  g(Z)),  is  a  weighted  average  of  local  average  treatment  effects
with nonnegative weights, we  impose the following condition  on the function  g(z):

CONDITION3:  g(z) is a function from  the support of  Z  to  8 such that
(i)  either  for  all  Z , W E ~ ,
P(z) G P(w) implies g(z) z g(w);

P r ( z ) < P ( w )   implies  g(z)<g(w),

or,  for  all  Z , W E ? I ,

(ii)  Cov(D, g(Z)) # 0.

There  are  three  important  cases where  Condition  3(i)  is  immediately  satisfied.  The
first  is the basis of  Theorem 1. If  Z  is binary, it is clear  that  P ( z )  is either increasing or
decreasing in  g(z). The  second  case is where  g(z) = E[D,IZ, = z] = P(z). For example,
in  the  linear latent  index model,  g(z) = E[D,IZ, = z ]  = Pr(y, + y,z  + v > 0). The third
case is where Z  is a scalar random variable, and both  g(z) and  P ( z )  are monotone in  z.
The following theorem  gives the relation between IV estimators and the local average
treatment  effects  defined  in  the  previous  section.  To  avoid  additional  notation  and
smoothness  assumptions,  and  because  the  examples  in  Section  4  all  involve  discrete
instruments, it  is formulated  in  terms of  instruments with discrete support.

LOCAL  AVERAGE  TREATMENT  EFFECTS

471

THEOREM2:  Suppose  that  Conditions  1, 2,  and  3  are  satisfied.  Let  Z  be  a  discrete
random  variable  with  support  (z,, z,, . . . ,z,},  ordered  in  such  a  way  that  if  l < m  then
P(z,) < P(z,).  Then, if  Cov(D, g ( Z ) )  # 0, the N estimator for  the effect of  D on Y  using
g ( Z )  as an znstrument estimates

a:"=  C O V ( Y ,  g ( ~ ) ) / C o v ( D ,  g ( Z ) )  =  C Ak.a,k,,k&,,

K

k =  1

with weights

where  T ,  = Pr  ( Z  = z,)  and  a ,  ,,  is  the  local  average  treament  effect  E[Y,(l)-
Y,(0)(Di(z,)= 1, D i ( z k - , )  = 01.  ~ t $ e  Giights A,  are  nonnegative and  add  up to one.

PROOF:  See Appendix.

The  second  part  o f   this  section  analyzes  the  asymptotic  distribution  o f  the  IV
estimator.  W e  consider  here  the  case  where  g ( z )  is  a  known  function  o f   z.  In  the
Appendix we  derive  the  asymptotic  distribution  for  the case where  g ( . )  depends  on an
unknown  parameter  which  is  estimated  jointly  with  the  average  treatment  effect a:'.
That case includes two-stage procedures where in the first stage the conditional expecta-
tion o f  D  given  Z  is estimated.

THEOREM3:  Let  (Y,,Di, Z i ) E 1  be  N  independent, identically distributed  random  uari-
ables, and  g ( . )  a function from  the support of  Z  to  3 such that  Cov(D, g ( Z ) )  + 0 ,  and  let
&iVbe  t h ~

instrumental variables estimator,  given  by

where  Y =  C E l x / N  and  D  = C E I D i / N .  Assume  that  all  variances and  covariances are
finite.  As N  goes  to infinity,

with  E  = Y -  E [ Y ]  -a;'.

( D  - E [ D ] ) .

PROOF:  See Appendix.

In  textbook  discussions  o f  instrumental  variables  estimation  often the  assumption
E [ E ' ~ z  = z ]  = u 2  is  made.  In  that  case  the  variance  in  Theorem  3  simplifies  to  the
standard  IV  variance, ( r 2 .  Var ( g ( ~ ) ) / C o v 2

( D ,  g ( Z ) ) .

4.  EXAMPLES

In  this  section  we  give  a  number  o f   examples  and  discuss  the  applicability  o f
Conditions  1, 2, and  3. The examples  exploit  the manner  in which  a particular  program
or  treatment  is  implemented  to create  instruments  that  are  exogenous.  Evaluations  o f
this  type  are  sometimes  referred  to  as  natural  experiments,  in  contrast  with  the
identification achieved  in  clinical  trials where  individuals  are  directly  randomized  into
treatment  and  control groups.

472

G.  W.  IMBENS  AND  J.  D.  ANGRIST

EXAMPLE1 (Draft  Lottery):  Angrist  (1990)  uses  the  Vietnam-era  draft  lottery  to
estimate  the  effect  of  veteran  status  on  earnings. The  instrument  is  the  draft  lottery
number,  randomly  assigned to  date of  birth  and  used  to  determine  priority  for  military
conscription. The average probability of  serving in  the military falls with  lottery number.
Condition  1  requires  that  potential  earnings  with  and  without  military  service  be
independent  of  the  lottery  number.  This is  a  standard  IV  assumption  which  would  be
violated  if, for  example,  lottery  numbers  are related  to earnings through  some variable
other  than  veteran  status.  Condition  2  requires  that  someone who  would  serve  in  the
military with lottery number  k  would also serve in the military with lottery number  1  less
than  k ,  which  seems  plausible.  In  the  Angrist  draft  lottery  application,  g ( z )  is  an
estimate  of  P(z),  and  Condition  3 is  therefore  satisfied. The average  effect  of  veteran
status identified  under  Theorem  1 is  for  men who would  have served with a  low lottery
number, but  not with  a high lottery  number.

EXAMPLE2 (Administrative ~ c r e e n i n ~ ) : ~

Suppose applicants for a social program  are
screened by  two  officials. The two  officials are likely  to  have  different  admission  rates,
even  if  the  stated  admission  criteria  are  identical.  Since  the  identity  of  the  official  is
probably immaterial  to the response, it seems plausible that Condition  1 is satisfied. The
instrument  is binary  so Condition  3 is trivially  satisfied. However,  Condition  2  requires
that  if  official A  accepts  applicants with  probability  P(O),  and  official B  accepts people
with probability  P(1) > P(O),  official B must  accept  any  applicant who would  have been
accepted  by  official  A.  This  is  unlikely  to  hold  if  admission  is  based  on  a  number  of
criteria. Therefore, in this example we  cannot  use Theorem  1 to identify a local average
treatment  effect  nonparametrically  despite  the  presence  of  an  instrument  satisfying
Condition  1.

EXAMPLE3  (Randomization  of  Intention  to  Treat):6  Let  the  instrument  be  an
indicator for  assignment to treatment group in a randomized  trial. The actual treatment
indicator,  D,  may  differ  from  the  instrument  Z  because  some  individuals  may  not
comply  with  their  assignment.  Condition  1 requires  that  the  two  counterfactual  out-
comes, say health status if  treated and health  status if  untreated, are independent  of  the
original  assignment.  Condition  2 requires  that  anyone who would  take  the  treatment  if
assigned to the control  group would also take the treatment  if  assigned to the treatment
group. This seems plausible  if  noncompliance  is the result of  a decision by  patients. The
instrument is binary so Condition 3 is satisfied. The treatment  effect identified here is the
average treatment  effect for  those who always comply with their  assignment.

Dept.  of  Economics, Haruard  University, Cambridge, M A  02138, U.S.A.,  and  NBER
and

Dept. of  Economics,  The Hebrew  Uniuersity of Jerusalem,  Mt.  Scopus, Jerusalem  91905,

Israel,  and  NBER

Manuscript received December,  1991;final revision receiued May,  1993.

APPENDIX

PROOFOF  THEOREM2:  We  start  with  three  preliminary  observations:  First,  without  loss  of
generality, we  assume  that the first version of  Condition 3 applies.  Given that the points of  support
are ordered, this  implies that if  1 < m, then  g ( z , )  bg(z,)  and that  Cov(D, g ( Z ) )  > 0.

This example was suggested  to us by  Geert Ridder.

6~  similar example is discussed  in  Robins (1989).

LOCAL  AVERAGE  TREATMENT  EFFECTS

473

Second, given the  K + 1 points in  the  support  of  Z ,  we  can  define  K  X ( K+ 1 ) / 2  local average
treatment  effects  a,,,zm,  one  for  each  (unordered)  pair  of  points  of  support  ( z , , 2,").  These
K x ( K + 1 ) / 2  local average treatment effects are related  in  the following way  (using the definition
of ffz,,z,):

Third, the conditional expectation of  Y given  Z  = z k  for  k > 1 can  be written  as

for all k # I ,  k # i n ,  and I  # rn.

The IV procedure  estimates

First  we  analyze the  numerator  of  this expression:

where  the  factor  multiplying  azk,,,_,  is equal  to the numerator  of  A,  in  (2). A similar calculation
shows that the  denominator  of  a:'

in ( 3 ) is equal to the  denominator  of  A,  in (2).

The  weights  Ak  clearly  add  up  to  one.  They  are  nonnegative  because  P ( z k )> P ( z ~ - ~ )and
which  follows from  the  ordering  of  the  points  of  support,  and  this  in  turn  implies
Q.E. D.

g ( z k )  > g ( ~ ~ - ~ )
that  C f = k ~ ,. ( g ( z , )- E [ g ( Z ) ] ) .  0 for all k.

PROOFOF  THEOREM3:  We  give the proof  for the case where  g ( . )  is estimated, which  will  as a
special case give the variance for the known  g ( . ) case. Let  g ( z ,  0 )  be a known function, with  0  an
unknown  parameter  to  be  estimated  in  the  first  stage.  A1s0,~let $ ( Z ,  D,0)  be  the  estimating
equation  for  0.  That  is,  0  is  characterized  by  C L I & ( Z n ,D,,@) = 0.  We  assume  that  there  is  a
unique solution  to E $ ( Z ,  D , 0) = 0 and that  E [ d $ ( Z ,D, 0)/a0)l has a full rank.  B,''
can be written
as the second  element of  the solution  to

474

G.  W.  IMBENS  AND  J.  D.  ANGRIST

where  y is  a  nuisance  paramete!,
the  asymptotic variance of  f i ( ( 0   - U)', + - y,&bv - a!')'

equal  to  E [ Y ]- a".  E [ D ] .Using  standard  asymptotic  theory,

is equal to V = T - ' ~ ( 1 . ' ) - ' ,  with

where  E  is  again  equal to  Y - E [ Y ]- m i V .  ( D  - E [ D ] )= Y - y -cubV.  D.

Substitution of  these matrices  in the variance formula V = T 1 ~ ( T ' ) - 'gives the desired variance

of  a ( & ' ' -

a;')  as the  bottom  right  element of  V.

If  g(z5  is  a  known  function,  the  first  column  and  row  of  T  and  A  can  be  removed,  and  the

asymptotic variance  of  f i ( & L v  - a;')

is equal to the (2,Z)  element of

The relevant  matrices  are invertible  because Cov(D, g ( Z ) )# 0  and  E [ d $ ( Z ,  D ,  U ) / d U ]   # 0 .

The  reason  that  the  variance  of  the  IV  estimator  is  affected  by  the  first  stage  estimation  of
g ( Z ,  0 )  is that  Condition  1 implies only that  E [ g ( Z ,  0 ) .  E ]  = 0, not  necessarily that  E [ E  IZ  = Z ]  = 0.
The  latter  is  often  assumed  in  textbook  discussions  of  instrumental  variables,  and  making  this
assumption  implies that the variance  of the IV estimator is not  affected by  the first stage estimation
because  E [ E.dg/dU(Z, U ) ]  is equal to zero.
Q.E. D.

REFERENCES

ANGRIST,J.  D. (1990): "Lifetime  Earnings  and  the  Vietnam  Era  Draft  Lottery:  Evidence  from

Social Security Administrative  Records,"  American  Economic Review, 80, 313-336.

ANGRIST,J. D., AND  A. KRUEGER (1991): "Does  Compulsory School Attendance Affect Schooling

and Earnings,"  Quarterly Journal  of  Economics,  106, 979-1014.

ANGRIST,J.  D.,  AND  G.  W.  IMBENS (1991): "Sources  of  Identifying  Information  in  Evaluation

Models,"  NBER  Technical  Working Paper  117.

ANGRIST,J.  D.,  G.  W.  IMBENS,AND  D.  RUBIN(1993): "Identification  of  Causal  Effects  Using

Instrumental  Variables,"  NBER  Working Paper.

CHAMBERLAIN,G.  (1986): "Asymptotic  Efficiency  in  Semi-parametric  Models  with  Censoring,"

Journal  of Econometrics, 32, 189-218.

HECKMAN,J.  J.  (1990): "Varieties  of  Selection  Bias,"  American  Economic  Review,  Papers  and

Proceedings,  80, 313-338.

HECKMAN,J. J., AND  J. HOTZ(1989): "Choosing  Among Alternative Nonexperimental Methods for
Estimating  the  Impact  of  Social  Programs:  The  Case  of  Manpower  Training,"  Journal  of  the
American  Statistical Association,  84, 862-874.

HECKMAN,

J .  J.,

AND  R.  ROBB (1985): "Alternative Methods  for Evaluating  the  Impact of  Interven-
tions,"  in  Longitudinal  Analysis  of  Labor  Market  Data,  ed. by  J .   Heckman  and  B.  Singer.  New
York:  Cambridge  University Press.

LOCAL  AVERAGE  TREATMENT  EFFECTS

475

LALONDE, R.  J.  (1986):  "Evaluating  the  Econometric  Evaluations  of  Training  Programs  Using

Experimental Data,"  American  Economic Review,  76, 602-620.

MANSKI,C. F. (1990):  "The  Selection  Problem,"  University of  Wisconsin, Social Systems Research

Institute  Working Paper 9012.

ROBINS,J. M. (1989):  "The  Analysis of  Randomized  and Non-Randomized AIDS Treatment Trials
Using a New Approach  to Causal Inference  in Longitudinal Studies,"  in  Health  Service Research
Methodology: A  Focus  on AIDS,  ed.  by  L.  Sechrest,  H.  Freeman,  and  A.  Bailey.  Washington,
D.C.:  NCHSR,  U.S. Public Health  Service.

RUBIN, D. (1974):  "Estimating  Causal Effects of  Treatments in  Randomized  and  Non-randomized

Studies,"  Journal  of  Educational  Psychology, 66, 688-701.

-(1990):  "Comment:  Neyman (1923) and Causal Inference in Experiments and Observational

Studies,"  Statistical  Science, 5, 472-480.

http://www.jstor.org

LINKED CITATIONS
- Page 1 of 2 -

You have printed the following article:

Identification and Estimation of Local Average Treatment Effects
Guido W. Imbens; Joshua D. Angrist
Econometrica, Vol. 62, No. 2. (Mar., 1994), pp. 467-475.
Stable URL:
http://links.jstor.org/sici?sici=0012-9682%28199403%2962%3A2%3C467%3AIAEOLA%3E2.0.CO%3B2-2

This article references the following linked citations. If you are trying to access articles from an
off-campus location, you may be required to first logon via your library web site to access JSTOR. Please
visit your library's website or contact a librarian to learn about options for remote access to JSTOR.

References

Lifetime Earnings and the Vietnam Era Draft Lottery: Evidence from Social Security
Administrative Records
Joshua D. Angrist
The American Economic Review, Vol. 80, No. 3. (Jun., 1990), pp. 313-336.
Stable URL:
http://links.jstor.org/sici?sici=0002-8282%28199006%2980%3A3%3C313%3ALEATVE%3E2.0.CO%3B2-H

Does Compulsory School Attendance Affect Schooling and Earnings?
Joshua D. Angrist; Alan B. Krueger
The Quarterly Journal of Economics, Vol. 106, No. 4. (Nov., 1991), pp. 979-1014.
Stable URL:
http://links.jstor.org/sici?sici=0033-5533%28199111%29106%3A4%3C979%3ADCSAAS%3E2.0.CO%3B2-P

Varieties of Selection Bias
James Heckman
The American Economic Review, Vol. 80, No. 2, Papers and Proceedings of the Hundred and
Second Annual Meeting of the American Economic Association. (May, 1990), pp. 313-318.
Stable URL:
http://links.jstor.org/sici?sici=0002-8282%28199005%2980%3A2%3C313%3AVOSB%3E2.0.CO%3B2-G

http://www.jstor.org

LINKED CITATIONS
- Page 2 of 2 -

Choosing Among Alternative Nonexperimental Methods for Estimating the Impact of Social
Programs: The Case of Manpower Training
James J. Heckman; V. Joseph Hotz
Journal of the American Statistical Association, Vol. 84, No. 408. (Dec., 1989), pp. 862-874.
Stable URL:
http://links.jstor.org/sici?sici=0162-1459%28198912%2984%3A408%3C862%3ACAANMF%3E2.0.CO%3B2-R

Evaluating the Econometric Evaluations of Training Programs with Experimental Data
Robert J. LaLonde
The American Economic Review, Vol. 76, No. 4. (Sep., 1986), pp. 604-620.
Stable URL:
http://links.jstor.org/sici?sici=0002-8282%28198609%2976%3A4%3C604%3AETEEOT%3E2.0.CO%3B2-P

[On the Application of Probability Theory to Agricultural Experiments. Essay on Principles.
Section 9.] Comment: Neyman (1923) and Causal Inference in Experiments and Observational
Studies
Donald B. Rubin
Statistical Science, Vol. 5, No. 4. (Nov., 1990), pp. 472-480.
Stable URL:
http://links.jstor.org/sici?sici=0883-4237%28199011%295%3A4%3C472%3A%5BTAOPT%3E2.0.CO%3B2-A

