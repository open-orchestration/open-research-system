|     | RARR: |                       | Researching |             |       | and Revising      | What |                | Language    |                | Models | Say,   |     |
| --- | ----- | --------------------- | ----------- | ----------- | ----- | ----------------- | ---- | -------------- | ----------- | -------------- | ------ | ------ | --- |
|     |       |                       |             |             | Using | Language          |      | Models         |             |                |        |        |     |
|     |       | LuyuGao1⋄∗            |             | ZhuyunDai2∗ |       | PanupongPasupat2∗ |      |                |             | AnthonyChen3⋄∗ |        |        |     |
|     |       | ArunTejasviChaganty2∗ |             |             |       | YichengFan2∗      |      | VincentY.Zhao2 |             |                |        | NiLao2 |     |
|     |       |                       | HongraeLee2 |             |       | Da-ChengJuan2     |      |                | KelvinGuu2∗ |                |        |        |     |
1CarnegieMellonUniversity,2GoogleResearch,3UCIrvine
|     |     |     |     |     | luyug@cs.cmu.edu |     | anthony.chen@uci.edu |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
{zhuyundai,ppasupat,arunchaganty,yichengfan,vzhao,nlao,hrlee,dacheng,kguu}@google.com
Abstract
Text generation model
|     | Language | models | (LMs) | now | excel | at many |     |     |     |     |     |     |     |
| --- | -------- | ------ | ----- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
The marathon world record is  ● Show the task definition
|     | tasks | such as | question | answering, | reasoning, |     |     |     |     |     | Original model  |     |     |
| --- | ----- | ------- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- | --------------- | --- | --- |
3202 yaM 13  ]LC.sc[  3v62780.0122:viXra 2:01:39, set by Eliud Kipchoge  output,  x ○ orig → (revised, attrib_report)
|     | and dialog. | However, |     | they sometimes |     | gener- |     | of Kenya in 2018. |     |     |     |     |     |
| --- | ----------- | -------- | --- | -------------- | --- | ------ | --- | ----------------- | --- | --- | --- | --- | --- |
● Show the evaluation metric
|     | ateunsupportedormisleadingcontent. |     |     |     |     | Auser |     |     |     |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
○ attribution
|     | cannoteasilydeterminewhethertheiroutputs |     |     |     |     |     |     |     |     |     | Document  |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
Research ○ preservation
|     |     |     |     |     |     |     |     |     | & Revision |     | Corpus |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --- | --- |
aretrustworthyornot,becausemostLMsdo ● Illustrate that one model should be able to handle
|     | not have | any | built-in | mechanism | for | attribu- |     |     |     |     |     |     |     |
| --- | -------- | --- | -------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
different generators, different tasks
|     | tiontoexternalevidence. |     |     | Toenableattribution |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Revised output,  y
Attribution report,  A
|     | while | still preserving |     | all the | powerful | advan- |     |     |     |     |     |     |     |
| --- | ----- | ---------------- | --- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
tagesofrecentgenerationmodels,wepropose The marathon world  [npr.org] 2022 ... Kipchoge shaved
|     |     |     |     |     |     |     |     | record is 2:01:39 2:01:09,  |     |     | 30 seconds … to finish in 2:01:09 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --------------------------------- | --- | --- |
RARR(RetrofitAttributionusingResearchand set by Eliud Kipchoge of  [wikipedia.org] … Kipchoge is a
Kenya in 2018 2022.
Revision),asystemthat1)automaticallyfinds Kenyan long-distance runner …
|     | attribution | for | the output | of  | any text | genera- |     |     |     |     |     |     |     |
| --- | ----------- | --- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Human / automatic evaluation
tionmodel,and2)post-editstheoutputtofix
unsupportedcontentwhilepreservingtheorigi-
|     | naloutputasmuchaspossible. |        |               |                  | Whenapplied |         |     |                   |       |     |                    |       |     |
| --- | -------------------------- | ------ | ------------- | ---------------- | ----------- | ------- | --- | ----------------- | ----- | --- | ------------------ | ----- | --- |
|     | to the                     | output | of several    | state-of-the-art |             | LMs     |     |                   |       |     |                    |       |     |
|     |                            |        |               |                  |             |         |     | Attribution score |       |     | Preservation score |       |     |
|     | on a diverse               | set    | of generation |                  | tasks,      | we find |     |                   |       |     |                    |       |     |
|     |                            |        |               |                  |             |         |     |                   | A → y |     |                    | x → y |     |
thatRARRsignificantlyimprovesattribution
whileotherwisepreservingtheoriginalinputto
|     |     |     |     |     |     |     | Figure1: |     | TheEditingforAttributiontask. |     |     | Theinput |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------------------------- | --- | --- | -------- | --- |
amuchgreaterdegreethanpreviouslyexplored x is a text passage produced by a generation model.
|     | editmodels. | Furthermore,theimplementation |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
OurResearch&Revisionmodeloutputsanattribution
ofRARRrequiresonlyahandfuloftrainingex-
reportAcontainingretrievedevidencesnippets,along
amples,alargelanguagemodel,andstandard
witharevisionywhosecontentcanbeattributedtothe
websearch.1
|     |     |     |     |     |     |     | evidence | in  | A while | preserving |     | other properties | of x |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ---------- | --- | ---------------- | ---- |
suchasstyleorstructure.
1 Introduction
Generativelanguagemodels(LMs)andothertext
|     |     |     |     |     |     |     | or  | unsupported |     | content, | colloquially | called | “hal- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------------ | ------ | ----- |
generationmodelsarenowthebackboneofmany lucinations” (Maynez et al., 2020; Menick et al.,
AIsystems. Forexample, largelanguagemodels 2022). To make LMs more trustworthy, we want
canperformmulti-stepreasoning(Nyeetal.,2021;
tojustifyeachgenerationbyanattributionreport
Weietal.,2022),generateplans(Ahnetal.,2022), (Rashkin et al., 2021; Bohnet et al., 2022) that
use tools and APIs (Shin et al., 2021; Thoppilan containssupportingevidencefromtrustedsources
| et al., | 2022), | and | answer | open-domain |     | questions |     |     |     |     |     |     |     |
| ------- | ------ | --- | ------ | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
(e.g.,encyclopediaorarticles)whereappropriate.
(Petronietal.,2019;Robertsetal.,2020).
|     |     |     |     |     |     |     | Most | existing |     | LMs, | such | as those based | on  |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | ---- | ---- | -------------- | --- |
Despitetheseincredibleadvances,state-of-the-
|     |     |     |     |     |     |     | sequence-to-sequence |     |     |     | architectures, | lack | a built- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | -------------- | ---- | -------- |
artLMsstillfrequentlyproducebiased,misleading,
|     |     |     |     |     |     |     | in  | mechanism |     | for attribution. |     | Even retrieval- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------- | --- | --------------- | --- |
∗Leadcontributors.PleaseseeContributionssectionfor augmentedmodels(Guuetal.,2020;Lewisetal.,
details.⋄WorkdoneduringaninternshipatGoogleResearch.
2020),whichretrieverelevantdocumentsandthen
1Wereleaseopen-sourceimplementationsofRARR,the
|            |     |           |         |            |      |             | condition |     | on them      | to  | generate | text, still    | do not |
| ---------- | --- | --------- | ------- | ---------- | ---- | ----------- | --------- | --- | ------------ | --- | -------- | -------------- | ------ |
| evaluation |     | pipeline, | and the | evaluation | sets | at https:// |           |     |              |     |          |                |        |
|            |     |           |         |            |      |             | guarantee |     | attribution. |     | Prior    | work has shown | that   |
github.com/anthonywchen/RARR.

retrieval-augmented models generate text that ei- Combined figure v1d
Query Generation
ther includes additional information outside the
q q
retrieved documents (Dziri et al., 2022), ignores 1 N
When did Millie What channel was Millie
the documents altogether (Krishna et al., 2021), Inbetween premiere? Inbetween on?
orevencontradictsthedocuments(Longpreetal.,
Retrieval Retrieval
2021). Infact,occasionallyignoringtheretrievals
[fandom.com]
canmakethemodelsmorerobusttobadretrievals {e 1,j } {e N,j } … the first series
[f[afannddoomm.c.coomm]] [c[coommeeddyy.c.coo.u.ukk]] premiered on
(Khandelwaletal.,2020),illustratingthatend-task …… t hthee fi firsrst ts seerireiess MMilillileie I nInbbeetwtweeeenn. . 1 October 2014.
ppreremmieiereredd o onn CCBBBBCC s sitictcoomm
performanceandattributionarenotalwaysaligned. 1 1O Occtotobbeer r2 2001414.. aabboouut ta a y yoouunngg … … [comedy.co.uk]
Millie Inbetween.
CBBC sitcom
Instead of constraining LMs to generate at- about a young …
Agreement Agreement
tributed text, we propose a model-agnostic ap- Output Attribution
Report A={e, .., e }
proach to improve the attribution of any existing 1 M
Edit Edit skipped
LM:RetrofitAttributionusingResearchandRevi-
sion(RARR).Theapproachisinspiredbyworkson
Millie Inbetween Millie Inbetween Millie Inbetween
fact-checking2 where simple research-and-revise premiered on 24 premiered on 1 premiered on 1
February 2014 October 2014 October 2014
workflows are effective at attributing or correct- on CBBC. on CBBC. on CBBC.
ingunattributedclaimsmadebyhumans(Thorne Input Passage x Output Passage y
etal.,2018;Schusteretal.,2021;ThorneandVla-
Figure2: AnoverviewofRARR,whichimprovesattri-
chos, 2021). As shown in Figure 1, after gener- butionforatextpassageviaResearch&Revision.Given
ating text with the LM, RARR does research to theinputtextpassage,theresearchstageusesaquery
retrieverelevantevidence,andthenrevisesthetext generatortoraisequestionsaboutdifferentaspectsof
tomakeitconsistentwiththeevidencewhilepre- the text. The retriever then searches for evidence to
investigateeachquery. Therevisionstagefirstrunsan
serving qualities like style or structure, enabling
agreement model to detect disagreement between the
the revised text to be seamlessly used in place of
textandtheevidence,thenrunsaneditmodeltorevise
the original. RARR can be viewed as a retrieval-
the text if needed. Finally, M evidence snippets are
augmented model where retrieval happens after
selectedtoformanattributionreport.
generationratherthanbefore. ThisallowsRARR
to stand on the shoulders of giant LMs without
havingtomodifythemtosupportattribution. 2 Taskformulation
InourefforttoexpandthescopeofResearch&
We propose the task of Editing for Attribution as
Revisionmodelstohandletheoutputofarbitrary
follows. AsFigure1shows,theinputtothesystem
LMs,wemakethefollowingcontributions. First,
isatextpassagexproducedbyagenerationmodel.
weformalizetheEditingforAttributiontaskand
The output is a revised text passage y along with
proposenewmetricsthatevaluaterevisionmodels
an attribution report A, which contains evidence
notjustontheirabilitytoproducewell-attributed
snippets e ,...,e that support the content in y.
1 M
revisions,butalsoontheirabilitytootherwisepre-
Optionally,theattributionreportcancontainaddi-
serve original properties of the text. Second, we
tionalinformationsuchasthealignmentbetween
usethesemetricstobenchmarkhowexistingre-
evidencesnippetsandrelevantpartsiny.
vision models perform on various types of LM
Weproposetomeasurethequalityoftherevised
outputs such as knowledge-intensive statements,
text y and attribution report A along two dimen-
reasoning chains, and dialog responses. Finally,
sions: (1) attribution: how much of the revised
we find that existing revision models do not al-
text y can be attributed to the evidence in A, and
waysgeneralizeacrossmanytasks(andwerenot
(2) preservation: how much the revised text y
originallyintendedto),andthereforeproposeanew
preservesaspectsoftheoriginaltextx.
research-and-revisemodelthatleveragesthepower
offew-shotpromptinginlargelanguagemodelsto
2.1 Measuringattribution
robustlygeneralizeacrossdomains.
Previously, Rashkin et al. (2021) proposed At-
2Inthispaper,wegenerallyavoidtheterm“fact-checking” tributable to Identified Sources (AIS), a human
otherthantoreferencerelevantliterature,becauseweonly evaluationframeworkwhichconsidersabinaryno-
addressattribution,andattributiondoesnotentailcorrectness.
tion of attribution. Roughly speaking, a text pas-
Evenifaclaimisattributedtoaparticularsource,itdoesnot
guaranteethatthesourceis“correct”(Menicketal.,2022). sage y is attributable to a set A of evidence if a

generichearerwouldaffirmthestatement“Accord- and Vlachos, 2021). Different tasks have differ-
ingtoA,y”underthecontextofy. Asystemeither ent requirements for what should be preserved.
receivesfullcredit(1.0)ifallcontentiny canbe Here,wedesireasimplemetricthatcanbereadily
attributedtoA,andnocredit(0.0)otherwise. computedformanytasksandthatgenerallypenal-
Weproposeamorefine-grained,sentence-level izesunnecessarychanges. Wethusdefineametric
extensionofAIS.WeaskannotatorstogiveanAIS basedonthecharacter-levelLevenshteineditdis-
scoreforeachsentencesofy,andthenreportthe tance(Levenshtein,1965)betweenxandy:
averageAISscoreacrossallsentences:
(cid:18) (cid:19)
Lev(x,y)
Pres (x,y) = max 1− ,0 (3)
Attr (y,A) = avgAIS(s,A). (1) Lev length(x)
AIS
s∈y
Thismetricis1.0ifxandy arethesame,and0.0
SincetheAISscoreisbinary,thiseffectivelymea-
ify completelyoverwritesallpartsofx. Pres is
suresthepercentageofsentencesiny thatarefully Lev
generallysensitivetoanykindofchange,butcer-
attributedtoA. Whenjudgingeachsentence,we
tainlydoesnotcaptureallnotionsofpreservation
alsogiveannotatorsaccesstothesurroundingsen-
(e.g.,preservingrhymeschemesorpuns).
tences and other necessary context, such as the
We want the revision to preserve the original
question that the text passage responded to. We
intentwhileavoidingsuperfluousedits. Toreflect
also impose the maximum number of evidence
this,wefinallycombinethetwometricsas
snippetsintheattributionreportAtomakeitcon-
ciseenoughforboththeannotatoranddownstream
Pres (x,y) = Pres (x,y)·Pres (x,y).
comb intent Lev
users. Bymanuallyinspecting30examplesfrom
(4)
ourbenchmarks,wefoundM = 5snippetstobe
whichis0.0iftherevisionchangestheintentand
sufficientforfullattribution.
equal to Pres (x,y) otherwise. Since Pres
Lev intent
During model development, we define an au-
requires human annotation, we use Pres as an
Lev
tomated metric, auto-AIS (Attr ), that approxi-
auto automatedmetricformodeldevelopment.
mateshumanAISjudgments. Weutilizethenatural
language inference (NLI) model from Honovich 2.3 Discussion
etal.(2022),whichcorrelateswellwithAISscores.
Optimizing for attribution alone cannot ensure a
For each sentence s of y, and for each evidence
good revision: for example, an adversarial editor
snippeteinA,letNLI(e,s)bethemodelprobabil-
couldensure100%attributionbysimplyreplacing
ityofeentailings. Wethendefine
theinputxwiththetextofanyarbitraryretrieved
document, which is trivially attributable to itself.
Attr (y,A) = avg maxNLI(e,s). (2)
auto
s∈y e∈A Ideally,wewanttomaximizebothattributionand
preservation,whilenavigatinganytradoffsbetween
To improve accuracy, we decontextualize (Choi
thetwo. Inourexperiments,wereportbothmetrics,
etal.,2021)eachsentencebasedontheentirecon-
aswellastheirharmonicmean(F1 ,analogous
text of y before computing the scores. See Ap- AP
tohowrecallandprecisionarecombinedinF1).
pendixBforimplementationdetails.
Weemphasizethatthisevaluationschemedoes
2.2 Measuringpreservation notrequireany“gold”or“reference”edits(unlike
many prior evaluations of text revision models),
Tomeasurepreservation,wefirstaskannotatorsto
whichareoftenonlyavailableforspecializeddo-
decideiftherevisionpreservesthetext’soriginal
mains. This enables us to broaden the scope to a
intent(completely,somewhat,ornotatall—see
muchwiderrangeofgenerationtasks.
Appendix C for exact rubrics). Like AIS evalua-
tion,wegiveannotatorsthenecessarysurrounding
3 Approach
context. WedefinethebinarymetricPres (x,y)
intent
to be 1.0 if the revision completely preserves the WenowpresentRetrofitAttributionusingResearch
originalintent,and0.0otherwise. andRevision(RARR),asimplemethodforsolving
However, evenifarevisionpreservesintent, it the Editing for Attribution task. As illustrated in
maystillmakesuperfluousmodifications,suchas Figure 2, given an input passage x, the research
reorderingwords,changingtextualstyle,orinclud- stage first generates a set of queries {q ,...,q },
1 N
ing unnecessary additional information (Thorne eachinvestigatingoneaspectofxthatpotentially

(a)Querygenerationx→{q1,...,qN} are then ranked based on their relevance to the
Yousaid:Yournoseswitchesbackandforthbetweennostrils.Whenyou
|     |     |     |     |     |     | query. Forthis,weuseanexistingquery-document |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
sleep,youswitchaboutevery45minutes.Thisistopreventabuildupof
mucus.It’scalledthenasalcycle. relevancemodeltrainedfollowingNietal.(2021),
Toverifyit,
a)Igoogled:Doesyournoseswitchbetweennostrils? which computes a relevance score S (q,e)
relevance
b)Igoogled:Howoftendoesyournostrilsswitch? betweenaqueryq andanevidencesnippete. We
c)Igoogled:Whydoesyournostrilswitch?
d)Igoogled:Whatisnasalcycle? then keep the top J = 1 evidence for each query.
(b)Agreementmodel(y,q,e)→{0,1} Thefinalretrievalresultis[(q ,e ),...,(q ,e ),
Yousaid:Yournoseswitches...(sameasabove)...nasalcycle. 1 11 1 1J
Ichecked:Howoftendoyournostrilsswitch? ...,(q N ,e N1 ),...,(q N ,e NJ )],wheree ij denotes
Ifoundthisarticle:Althoughwedon’tusuallynoticeit,duringthenasal the jth evidence for the ith query, and N denotes
cycleonenostrilbecomescongestedandthuscontributeslesstoairflow,
whiletheotherbecomesdecongested.Onaverage,thecongestionpattern the total number of queries from CQGen (which
switchesaboutevery2hours,accordingtoasmall2016studypublished
| inthejournalPLOSOne. |     |     |     |     |     | canbedifferentforeachinputx). |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
Yournose’sswitchingtimeisaboutevery2hours,not45minutes.
Thisdisagreeswithwhatyousaid.
|     | (c)Editmodel(y,q,e)→newy |     |     |     |     | 3.2 Revisionstage |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
Yousaid:Yournoseswitches...(sameasabove)...nasalcycle.
Ichecked:Howoftendoyournostrilsswitch?
Ifoundthisarticle:Althoughwe...(sameasabove)...PLOSOne. After retrieving evidence, certain parts of x may
Thissuggests45minutesswitchtimeinyourstatementiswrong. nowbeproperlyattributed,butotherpartsremain
Myfix:Yournoseswitchesbackandforthbetweennostrils.Whenyou
sleep,youswitchaboutevery2hours.Thisistopreventabuildupof unattributedandshouldberevised. Asillustrated
mucus.It’scalledthenasalcycle.
inFigure2,therevisionstageinitializestheoutput
|           |          |     |          |          |      | y = x. | Then for each | retrieved | (q,e) | = (q ,e ), |
| --------- | -------- | --- | -------- | -------- | ---- | ------ | ------------- | --------- | ----- | ---------- |
| Figure 3: | Examples | of  | few-shot | examples | used | to     |               |           |       | i ij       |
promptthePaLMmodel(blue=input;red=output). theagreementmodelchecksiftheevidenceedis-
agreeswiththecurrentoutputyregardingtheissue
|     |     |     |     |     |     | inqueryq. | Ifadisagreementisdetected,theedit |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --------------------------------- | --- | --- | --- |
requiresattribution. Foreachqueryq i ,itretrieves model edits y to agree with e; otherwise, it does
webdocumentsandselectsthebestevidencesnip-
|         |           |     |          |     |            | nothing.      | Theprocesscontinuesuntilallretrievals |     |     |     |
| ------- | --------- | --- | -------- | --- | ---------- | ------------- | ------------------------------------- | --- | --- | --- |
| pets {e | ,e ,...}. | The | revision |     | stage then | re-           |                                       |     |     |     |
|         | i1 i2     |     |          |     |            | areprocessed. |                                       |     |     |     |
visestheoriginaltextxusingtheretrievalresults
{(q ,e ),...},yieldingarevisedtexty.
1 11
|                                          |            |     |      |     |             | Agreementmodel    |        | Theagreementmodeltakes   |            |            |
| ---------------------------------------- | ---------- | --- | ---- | --- | ----------- | ----------------- | ------ | ------------------------ | ---------- | ---------- |
| Most                                     | components | for | RARR | are | implemented |                   |        |                          |            |            |
|                                          |            |     |      |     |             | the partially     | edited | passage                  | y, a query | q, and the |
| usingfew-shotprompting(Brownetal.,2020). |            |     |      |     |             | We                |        |                          |            |            |
|                                          |            |     |      |     |             | evidenceeasinput. |        | Itthendecideswhetherboth |            |            |
usePaLM(Chowdheryetal.,2022)asourlanguage
y andeimplythesameanswertothequestionin
| model. | Figure 3 | shows | some | few-shot | examples |         |                         |     |     |               |
| ------ | -------- | ----- | ---- | -------- | -------- | ------- | ----------------------- | --- | --- | ------------- |
|        |          |       |      |          |          | q. This | form of question-guided |     |     | agreement was |
weuse,whileAppendixDliststhefullprompts.
|     |     |     |     |     |     | previouslyexploredbyHonovichetal.(2021). |     |     |     | We  |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
implementthisbyfew-shotpromptingPaLMusing
3.1 Researchstage
achain-of-thoughtstyleprompt(Weietal.,2022),
Query generation We perform comprehensive whereweaskthemodeltoexplicitlystatetheim-
question generation (CQGen) which produces a pliedanswersforbothy andebeforeproducingits
sequenceofquestionscoveringallaspectsofthe
judgmentabouttheiragreement.
| passage | x that need | to  | be verified |     | and attributed. |     |     |     |     |     |
| ------- | ----------- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | --- |
Asimilarstrategyhasbeenemployedtotraintext-
|                                    |     |     |     |     |         | Edit model           | The | edit model       | is run | only if a dis- |
| ---------------------------------- | --- | --- | --- | --- | ------- | -------------------- | --- | ---------------- | ------ | -------------- |
| planningmodels(Narayanetal.,2022). |     |     |     |     | Aprompt |                      |     |                  |        |                |
|                                    |     |     |     |     |         | agreementisdetected. |     | Themodeltakesy,q |        | ande           |
withsixhumandemonstrationswassufficientfor
|         |            |       |     |       |             | asinput,andoutputsanewversionofy |     |     |     | thataims |
| ------- | ---------- | ----- | --- | ----- | ----------- | -------------------------------- | --- | --- | --- | -------- |
| PaLM to | adequately | learn | the | task. | To increase |                                  |     |     |     |          |
toagreewithewhileotherwiseminimallyaltering
| diversity | and coverage, |     | we sample |     | from our | CQ- |     |     |     |     |
| --------- | ------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- |
y. Weagainusefew-shotpromptingandchain-of-
| Gen model | three | times | and | take the | union | of the |     |     |     |     |
| --------- | ----- | ----- | --- | -------- | ----- | ------ | --- | --- | --- | --- |
thought,whereweaskthemodeltofirstidentifya
resultingqueries.
|                   |     |                        |     |     |     | particularspaniny |             | thatneedstobeeditedbefore |            |            |
| ----------------- | --- | ---------------------- | --- | --- | --- | ----------------- | ----------- | ------------------------- | ---------- | ---------- |
|                   |     |                        |     |     |     | generating        | the revised | y.                        | This helps | reduce the |
| Evidenceretrieval |     | ForeachqueryfromCQGen, |     |     |     |                   |             |                           |            |            |
editor’sdeviationfromthecurrenty.3
| weuseGoogleSearchtoretrieveK |     |     |     | =   | 5webpages. |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
Weextractcandidateevidencesnippetsfromeach
web page by running a sliding window of four 3Theeditoroccasionallyproduceslargeeditsthatbringthe
newrevisionclosetoebutfarfromthecurrenty.Sincethis
| sentences | across | the page, | breaking |     | at document |     |     |     |     |     |
| --------- | ------ | --------- | -------- | --- | ----------- | --- | --- | --- | --- | --- |
israrelydesirable,werejecteditswitheditdistanceabove50
| headings. | The evidence |     | snippets | for | each | query |     |     |     |     |
| --------- | ------------ | --- | -------- | --- | ---- | ----- | --- | --- | --- | --- |
charactersor0.5timestheoriginaltextlength.

| 3.3 Attributionreport |     |     |     |     |     |     | PaLMoutputsonNQ(factoidstatements) |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
MillieInbetweenisaBritishcomedytelevisionseries.Itpremieredon
Finally,weselectatmostM = 5evidencesnippets 24February2014onBBCOne.ThefirstserieswasproducedbyJohn
YorkeandPhilClymer.
| toformanattributionreportA. |     |     |     | Notethatduringev- |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
PaLMoutputsonSQA(reasoningchains)
idenceretrievalandrevision,wemayhaveencoun- ThehighestpointofMountWycheproofis70metres.EdmundHillary
teredandusedmorethanM snippets. Ourgoalis climbedMountEverest,whichis8,848metres.SoMountWycheproof
wouldbeabreezeforEdmundHillary.
tofindasubsetofsnippetsthatmaximizescover-
LaMDAoutputsonQReCC(knowledge-intensivedialogs)
age over the potentially attributable points in the WhenwasWelshsocialreformerRobertOwenborn? 

passage,asrepresentedbythequeriesq ,...,q . R o bertOwenwasbornon14May1771
|        |               |     |       |      | 1           | N                       |     |     |     |     | context |
| ------ | ------------- | --- | ----- | ---- | ----------- | ----------------------- | --- | --- | --- | --- | ------- |
|        |               |     |       |      |             | .. .                    |     |     |     |     |       |
| We use | the relevance |     | model | from | Section 3.1 | as Didhehaveanotherjob? |     |     |     |     |         |
In1810hemovedtoManchesterandestablishedadraper’sshop.
| a proxy | for measuring |     | how | much | an evidence | e   |     |     |     |     |     |
| ------- | ------------- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
coversthepointraisedbyaqueryq.
|                      |               |     |      |        | Then,weex- | Figure4:                                  | Examplesofinputpassages. |     |     |     | ForQReCC, |
| -------------------- | ------------- | --- | ---- | ------ | ---------- | ----------------------------------------- | ------------------------ | --- | --- | --- | --------- |
| haustivelysearchforA |               |     | ⊆ {e | ,...,e | }ofsize    |                                           |                          |     |     |     |           |
|                      |               |     |      | 11     | NJ         | priordialogturnsarealsogivenasthecontext. |                          |     |     |     |           |
| atmostM              | thatmaximizes |     |      |        |            |                                           |                          |     |     |     |           |
N
|           |     |      | (cid:88) |           |         | the output                        | text | (Bohnet | et  | al., 2022; | Kryscinski |
| --------- | --- | ---- | -------- | --------- | ------- | --------------------------------- | ---- | ------- | --- | ---------- | ---------- |
| Cover(A,q |     | ) := | maxS     |           | (q ,e). | (5)                               |      |         |     |            |            |
|           | 1:N |      |          | relevance | i       |                                   |      |         |     |            |            |
|           |     |      | e∈A      |           |         | etal.,2020;GoyalandDurrett,2021). |      |         |     |            | Acommon    |
i=1
|     |     |     |     |     |     | alternative | is to | evaluate | whether |     | the output text |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | -------- | ------- | --- | --------------- |
4 Relatedwork contains the same factual information as the ev-
|     |     |     |     |     |     | idence; | e.g., by | checking | if  | both | yield the same |
| --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | --- | ---- | -------------- |
Fact-checking
Ourresearchbuildsuponworks
|     |     |     |     |     |     | answer | to the same | question |     | (Wang | et al., 2020). |
| --- | --- | --- | --- | --- | --- | ------ | ----------- | -------- | --- | ----- | -------------- |
toidentifywhetheraclaimissupportedorrefuted
WeusethisnotionofattributioninRARR’sagree-
bythegivenevidence(Thorneetal.,2018;Wang,
mentmodelratherthanforevaluation.
| 2017; Karadzhov         |     | et  | al., 2017; | Augenstein          |     | et al.,                   |     |     |     |                |     |
| ----------------------- | --- | --- | ---------- | ------------------- | --- | ------------------------- | --- | --- | --- | -------------- | --- |
| 2019;Waddenetal.,2020). |     |     |            | Inreal-worldscenar- |     |                           |     |     |     |                |     |
|                         |     |     |            |                     |     | Retrieval-augmentedmodels |     |     |     | Modelswithare- |     |
iossuchastheonewhichRARRoperatesin,rele-
|     |     |     |     |     |     | trieval | component | have | seen | successes | in ques- |
| --- | --- | --- | --- | --- | --- | ------- | --------- | ---- | ---- | --------- | -------- |
vantevidencemaynotbeprovided,necessitating
|     |     |     |     |     |     | tion answering |     | (Chen | et  | al., 2017; | Lee et al., |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | ---------- | ----------- |
retrieval(Fanetal.,2020;Piktusetal.,2021).
|                              |     |     |     |               |     | 2019; Nakano |         | et al., | 2021), | machine    | translation |
| ---------------------------- | --- | --- | --- | ------------- | --- | ------------ | ------- | ------- | ------ | ---------- | ----------- |
|                              |     |     |     |               |     | (Zhang       | et al., | 2018),  | code   | generation | (Hayati     |
| Post-hoceditingforfactuality |     |     |     | Recentworkhas |     |              |         |         |        |            |             |
gone beyond checking the validity of a claim to etal.,2018),languagemodeling(Khandelwaletal.,
correctingapieceoftexttobefactuallyconsistent 2020),andotherknowledge-intensivetasks(Lewis
with a set of evidence via post-hoc editing (Shah etal.,2020). Theirretrievalsarenotnecessarilyat-
tributions(Dzirietal.,2022;Longpreetal.,2021)
etal.,2020;ThorneandVlachos,2021;Schuster
etal.,2021;Balachandranetal.,2022;Caoetal., andtypicallyarenotusedtoreviseanexistingout-
2020; Iso et al., 2020). FRUIT (Logan IV et al., put. An exception is LaMDA (Thoppilan et al.,
2022),alanguagemodelfordialogthatperforms
| 2022) | and PEER | (Schick |     | et al., | 2022) both | im- |     |     |     |     |     |
| ----- | -------- | ------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
plementaneditorthatisfine-tunedonWikipedia revisionbytrainingonhumanannotations.
edithistorywiththegoalofupdatingoutdatedin-
| formation | and | collaborative |     | writing | respectively. | 5 Experiments |     |     |     |     |     |
| --------- | --- | ------------- | --- | ------- | ------------- | ------------- | --- | --- | --- | --- | --- |
Evidence-basedFactualErrorCorrection(EFEC;
ThorneandVlachos,2021)alsoimplementsafull 5.1 Evaluationsetups
research-and-reviseworkflowtrainedonWikipedia
RARRaspirestobeageneral-purposemethodfor
| passages(Thorneetal.,2018). |     |     |     | Akeydifferentia- |     |           |     |             |     |     |                 |
| --------------------------- | --- | --- | --- | ---------------- | --- | --------- | --- | ----------- | --- | --- | --------------- |
|                             |     |     |     |                  |     | improving | the | attribution | of  | any | text generation |
torofRARRisitsabilitytoedittheoutputofany
|            |       |         |       |            |     | modelinanytextdomain. |            |     | Wethusconstructeval- |     |                 |
| ---------- | ----- | ------- | ----- | ---------- | --- | --------------------- | ---------- | --- | -------------------- | --- | --------------- |
| generation | model | without | being | restricted | by  | the                   |            |     |                      |     |                 |
|            |       |         |       |            |     | uation                | benchmarks | by  | taking               | the | task input from |
domain,task,ortheneedfortrainingdata.
threediversedatasets,andpromptingdifferentgen-
Measuringattribution Akeypartofimproving erationmodelstoproducelong-formoutputswhich
attributionisbeingabletoquantifyit. Apartfrom maycontain“hallucinations,”asdemonstratedin
human evaluation (Rashkin et al., 2021), several Figure4. Theselong-formoutputsserveasinput
automatedevaluationmethodshavebeenproposed. textpassagestoRARR.Wegenerate150develop-
Ourworkusesanentailment-basedmetric,which mentand150testpassagesforeachcombination
measureswhetherthereferencedevidenceentails ofgenerationmodelandsourcedataset.

Factoidstatements WepromptPaLM540Band Attribution Preservation
GPT-3text-davinci-002togeneratelong-forman-
|     |     |     |     |     |     | Model | auto-AIS |     | AIS | intent Lev | comb | F1  |
| --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | ---------- | ---- | --- |
AP
swerstoquestionsfromtheNaturalQuestionsdev
PaLMoutputsonNQ
set (NQ; Kwiatkowski et al., 2019). The result- EFEC 45.6→64.3 35.4→48.3 16.0 39.1 10.4 17.1
ingpassagesaremostlycoherentbutoftencontain LaMDA 39.5→49.9 18.3→30.4 26.0 39.6 21.1 24.9
|                 |     |            |          |     |            | RARR 45.6→54.9 |     | 35.4→43.4 |     | 90.0 89.6 | 83.1 | 57.0 |
| --------------- | --- | ---------- | -------- | --- | ---------- | -------------- | --- | --------- | --- | --------- | ---- | ---- |
| factual errors. |     | This setup | examines | the | ability to |                |     |           |     |           |      |      |
PaLMoutputsonSQA
attributeadiverserangeoffactoidknowledge.
|     |     |     |     |     |     | EFEC 37.8→58.6 |     | 24.5→51.7 |     | 6.0 31.0 | 3.8 | 7.1 |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | -------- | --- | --- |
|     |     |     |     |     |     | 32.7→43.2      |     | 15.8→27.0 |     |          |     |     |
Reasoningchains Languagemodelscangener- LaMDA 40.0 46.4 33.7 30.0
|     |     |     |     |     |     | RARR 37.6→45.1 |     | 24.5→31.5 |     | 92.6 89.9 | 84.6 | 45.9 |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | --------- | ---- | ---- |
atereasoningchainstoanswercomplexquestions
| (Weietal.,2022). |     | WeusePaLMandGPT-3togen- |     |     |     |                | LaMDAoutputsonQReCC |           |     |           |      |      |
| ---------------- | --- | ----------------------- | --- | --- | --- | -------------- | ------------------- | --------- | --- | --------- | ---- | ---- |
|                  |     |                         |     |     |     | EFEC 19.1→47.4 |                     | 13.2→48.7 |     | 39.7 39.4 | 23.7 | 31.9 |
eratereasoningchainsfortheStrategyQAtrainset
|     |     |     |     |     |     | LaMDA 16.4→36.2 |     | 16.0→27.1 |     | 21.3 24.8 | 12.0 | 16.6 |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | --------- | ---- | ---- |
(SQA;Gevaetal.,2021). Thissetuptestswhether RARR 18.8→29.4 13.2→28.3 95.6 80.2 78.1 41.5
therevisionmodelcanprovidebetterattributionfor
intermediatestepsofreasoning,whilepreserving Table1: Evaluationresults. Forattribution,wereport
theAISscoresofthetextsbothbeforeandafterediting
theoverallreasoningprocess.
|     |     |     |     |     |     | (before → | after). | For | preservation, | we  | report | intent |
| --- | --- | --- | --- | --- | --- | --------- | ------- | --- | ------------- | --- | ------ | ------ |
Knowledge-intensive dialogs We consider the preservation Pres intent , Levenshtein similarity Pres Lev ,
|                |         |         |           |              |         | andthecombinedPres             |     |      | . WesummarizeAttr |     |     | and |
| -------------- | ------- | ------- | --------- | ------------ | ------- | ------------------------------ | --- | ---- | ----------------- | --- | --- | --- |
| conversational |         | QA task | from      | the QReCC    | dev set |                                |     | comb |                   |     |     | AIS |
|                |         |         |           |              |         | Pres usingtheirharmonicmean(F1 |     |      |                   |     | ).  |     |
| (Anantha       | et al., | 2021).  | Given     | the previous | dia-    | comb                           |     |      |                   | AP  |     |     |
| log turns,     | which   | are     | rounds of | questions    | and an- |                                |     |      |                   |     |     |     |
swers (Q ,A ,Q ,A ,...,Q ), we use LaMDA ToapplyLaMDAonagiventextx,wesimplyset
|     | 1 1 | 2   | 2   | k   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andGPT-3toanswertothefinalquestionQ
|                           |     |     |                    |     | k condi- | thebaseresponseinstep1tox,andthenrunsteps |               |     |                  |     |        |     |
| ------------------------- | --- | --- | ------------------ | --- | -------- | ----------------------------------------- | ------------- | --- | ---------------- | --- | ------ | --- |
| tionedonthedialoghistory. |     |     | Theanswertendstobe |     |          |                                           |               |     |                  |     |        |     |
|                           |     |     |                    |     |          | 2 and3                                    | (we callthese |     | latter twostages |     | “LaMDA |     |
context-dependent,featuringpronounsandimplicit Research”). LaMDA was trained as a dialog sys-
references. Alldialogturnsaregivenalongsidethe tem, and always expects a dialog context where
answerasinputstotherevisionmodel.
|     |     |     |     |     |     | theuserspeaksfirst. |     | So,fornon-dialogtasks,we |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------------ | --- | --- | --- | --- |
insertanartificialuserutteranceasdialoghistory:
5.2 Models
|     |     |     |     |     |     | “Tellmesomethinginteresting.” |     |     |     | Fortheattribution |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ----------------- | --- | --- |
WecompareRARRtoseveralsystemsthathavea
|     |     |     |     |     |     | report, we | take | all evidence | documents |     | retrieved |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --------- | --- | --------- | --- |
research-and-reviseworkflow.
byLaMDAduringitsresearchprocess.
| EFEC                                    | WeconsiderEFEC(ThorneandVlachos, |          |          |        |             |           |                                 |       |             |        |           |         |
| --------------------------------------- | -------------------------------- | -------- | -------- | ------ | ----------- | --------- | ------------------------------- | ----- | ----------- | ------ | --------- | ------- |
|                                         |                                  |          |          |        |             | RARR      | Ourmodelusesfew-shotpromptingon |       |             |        |           |         |
| 2021)asarepresentativefine-tunededitor. |                                  |          |          |        | EFEC        |           |                                 |       |             |        |           |         |
|                                         |                                  |          |          |        |             | PaLM 540B | for                             | query | generation, | the    | agreement |         |
| fine-tunes                              | a T5-based                       |          | model to | revise | text condi- |           |                                 |       |             |        |           |         |
|                                         |                                  |          |          |        |             | model,    | and the                         | edit  | model.      | We use | the       | same    |
| tioned on                               | multiple                         | evidence | snippets |        | using both  |           |                                 |       |             |        |           |         |
|                                         |                                  |          |          |        |             | prompts   | for all                         | tasks | except      | when   | the       | context |
semi-supervisedandfully-supervisedapproaches.
comesfromadialog,whereweslightlymodifythe
| We compare |     | against | their fully-supervised |     | ap- |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
promptstousethedialogcontext(e.g.,CQGennow
proach,whichperformedbestintheirexperiments.
|           |     |        |           |       |            | maps dialog             | context |     | + x to queries). |               | The | query- |
| --------- | --- | ------ | --------- | ----- | ---------- | ----------------------- | ------- | --- | ---------------- | ------------- | --- | ------ |
| EFEC uses | a   | neural | retrieval | model | (Karpukhin |                         |         |     |                  |               |     |        |
|           |     |        |           |       |            | evidencerelevancemodelS |         |     |                  | isapretrained |     |        |
relevance
etal.,2020)toretrievefromWikipedia;however,
T5-largemodel(Raffeletal.,2020)fine-tunedfol-
notallpassagesinourexperimentsaresupported
lowingNietal.(2021)onMSMARCO(Nguyen
| byWikipediaarticles. |              |     | Tomorefairlycomparethe |            |         |                |     |              |     |       |              |     |
| -------------------- | ------------ | --- | ---------------------- | ---------- | ------- | -------------- | --- | ------------ | --- | ----- | ------------ | --- |
|                      |              |     |                        |            |         | et al., 2016). |     | See Appendix |     | D for | the few-shot |     |
| editing              | capabilities | of  | EFEC,                  | we instead | use the |                |     |              |     |       |              |     |
promptingstrategiesandmoremodelingdetails.
evidenceretrievedbyourresearchstages(CQGen
| andwebsearch). |     | NotethattheEFECeditorcondi- |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.3 Results
tionsonmultiplepiecesofevidenceatonce,while
Forthemainexperiments,wereportresultsonpas-
oureditoriterativelyconditionsononeatatime.
sagesgeneratedbyPaLMandLaMDA.Resultson
LaMDA LaMDA(Thoppilanetal.,2022)gener- GPT-3passagesshowsimilartrends(AppendixA).
atesresponsesinthreesteps: 1)generatea“base Table1andFigure5showattributionandpreser-
response”;2)generatesearchqueriesfromthebase vationresultsforeachmodelanddataset. Wealso
response;3)generatea“revisedresponse”condi- reportF1 ,theharmonicmeanofthetwometrics,
AP
tionedonthebaseresponseandretrievedevidence. whichisshownaslevelcurvesinFigure5.

| PaLM outputs on NQ |     | PaLM outputs on SQA |     | LaMDA outputs on QReCC |     |     |                                                     |     |     |     |     |     |
| ------------------ | --- | ------------------- | --- | ---------------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
| 100                |     |                     |     |                        |     |     | x:JusticeAshokKumarMathurheadedthe7thcentralpaycom- |     |     |     |     |     |
EFEC
|                      |       |     |     |     |     |     | missioninIndia. |     | Itwascreatedin2014andsubmittedits |     |     |     |
| -------------------- | ----- | --- | --- | --- | --- | --- | --------------- | --- | --------------------------------- | --- | --- | --- |
| )SIA( noitubirttA 80 | LaMDA |     |     |     |     |     | reportin2016.   |     |                                   |     |     |     |
RARR
| 60  |     |     |     |     |     |     | Attribution:50% |     |     |     | Preservation:100% |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ----------------- | --- |
40
EFEC:The7thcentralpaycommissioninIndiawascreatedin2014.
|     |     |     |     |     |     |     | Attribution:100% |     |     |     | Preservation:0% |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --------------- | --- |
20
| 0    |       |          |       |       |              | LaMDA:Iheardthe7thCPCmaderecommendationsforincreasingthe |     |     |     |     |     |     |
| ---- | ----- | -------- | ----- | ----- | ------------ | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 0 25 | 50 75 | 100 0 25 | 50 75 | 100 0 | 25 50 75 100 |                                                          |     |     |     |     |     |     |
Preservation (Prescomb) minimumsalarypayfromRs7066to18kpermonthfornew
centralgovernmentemployees.
Figure 5: Attribution and preservation scores. Attribution:0% Preservation:0%
Dashedlinesindicatethehighestattributionscoreob-
RARR:JusticeAshokKumarMathurheadedthe7thcentralpaycom-
|     |     |     |     |     |     |     | missioninIndia. |     | Itwascreatedin2014andsubmittedits |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------------------- | --- | --- | --- |
tainedbyanyofthemodelsbeforeediting:pointsabove
reportin2015.
| thelinehavebetterattributionafterrevision. |              |     |                         |     | Thecon- |     |                  |     |     |     |                   |     |
| ------------------------------------------ | ------------ | --- | ----------------------- | --- | ------- | --- | ---------------- | --- | --- | --- | ----------------- | --- |
|                                            |              |     |                         |     |         |     | Attribution:100% |     |     |     | Preservation:100% |     |
| toursareF1                                 | levelcurves: |     | pointsalongacontourhave |     |         |     |                  |     |     |     |                   |     |
AP evidence:The 7th Central Pay Commission (Chair: Justice A. K.
equivalentF1 . Differentmodelsmakeverydifferent Mathur)submitteditsreportonNovember19,2015.The
AP
trade-offsbetweenattributionandpreservation. Only CommissionhadbeenappointedinFebruary2014,tolook
atremunerationforcentralgovernmentemployees....
| RARRhasarobustF1 |     | AP acrossalltasks. |     |     |     |          |                                  |             |     |     |              |         |
| ---------------- | --- | ------------------ | --- | --- | --- | -------- | -------------------------------- | ----------- | --- | --- | ------------ | ------- |
|                  |     |                    |     |     |     | Figure6: | Examplemodeloutputsandhumanjudg- |             |     |     |              |         |
|                  |     |                    |     |     |     | ment     | of their                         | attribution |     | and | preservation | scores. |
RARRsignificantlyimprovesattributionwhile
|            |      |                 |     |       |             | EFEC  | reduces | the | passage     | x into | a single | sentence. |
| ---------- | ---- | --------------- | --- | ----- | ----------- | ----- | ------- | --- | ----------- | ------ | -------- | --------- |
| preserving | most | of the original |     | text. | In terms of |       |         |     |             |        |          |           |
|            |      |                 |     |       |             | LaMDA | changes |     | the writing | style. | RARR     | preserves |
F1 ,RARRistheonlymethodthatperformsro- the structure of the input passage. We show one evi-
AP
bustly across all three datasets, and significantly denceretrievedbyRARRtohelpexplaintheexample.
outperformspriormethodsonNQandSQA.
WefoundthatRARRistheonlymethodthatpre-
|     |     |     |     |     |     | Analyzingthebaselines |     |     |     | AsexemplifiedinFig- |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------- | --- | --- |
servestheoriginalintentofxover90%ofthetime
ure6,EFECfrequentlyattemptstosummarizethe
—EFECandLaMDAonlymanagetopreservethe
originalintent6–40%ofthetime. Wealsoseethat entire passage into one sentence, or drops later
|                                       |     |     |     |     |          | sentences.                             |     | This | is likely | due | to EFEC’s | training |
| ------------------------------------- | --- | --- | --- | --- | -------- | -------------------------------------- | --- | ---- | --------- | --- | --------- | -------- |
| editingiscrucialtoimproveattribution: |     |     |     |     | ifweonly |                                        |     |      |           |     |           |          |
|                                       |     |     |     |     |          | data,whichwaslimitedtosinglesentences. |     |      |           |     |           | This     |
retrieveevidencetosupporttheoriginalresponse
xwithoutediting,attributionrangesfromthelow behaviorgenerallyincreasestheattributionscore,
10stomid30s. Afterediting,RARRcanincrease because it is usually easier to make one sentence
|     |     |     |     |     |     | fully | attributable |     | than | many sentences. |     | However, |
| --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ---- | --------------- | --- | -------- |
attributionbyupto13%absolute,whilechanging
only10–20%ofthetext. indatasetswheretheclaimcontainsmultiplesen-
AsnotedinSection2,onecansacrificepreserva- tences(NQandSQA),suchabehavioryieldslow
preservationscores,andalsoresultsinoutputsthat
| tionforhigherattribution. |                                 |     | EFECisabletoobtain |     |     |                     |     |     |                       |     |     |     |
| ------------------------- | ------------------------------- | --- | ------------------ | --- | --- | ------------------- | --- | --- | --------------------- | --- | --- | --- |
|                           |                                 |     |                    |     |     | arelessinformative. |     |     | WeexpectthatEFECcould |     |     |     |
| strongF1                  | AP onQReCCbymakinglargerchanges |     |                    |     |     |                     |     |     |                       |     |     |     |
to the text in exchange for a higher attribution performmuchbetterifitstrainingdatawereaug-
score. However,itoccupiesaverydifferentpoint mentedtoincludemultiplesentences. LaMDARe-
searchachievessimilarattributionscorestoRARR.
fromRARRontheattribution-preservationtrade-
|     |     |     |     |     |     | But | as mentioned |     | in  | Section | 5.2, the | intent and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------- | -------- | ---------- |
offcurve,asvisualizedinFigure5.
linguisticstyleoftheoutputtendtodeviatefrom
| 6 Analysis |     |     |     |     |     | the        | input, | resulting                       | in  | lower | preservation | scores |
| ---------- | --- | --- | --- | --- | --- | ---------- | ------ | ------------------------------- | --- | ----- | ------------ | ------ |
|            |     |     |     |     |     | (Figure6). |        | Weemphasizethatthisisnotapurely |     |       |              |        |
6.1 Qualitativeanalysis
|     |     |     |     |     |     | apples-to-apples |     |     | comparison |     | since | LaMDA was |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ---------- | --- | ----- | --------- |
Human oracle To understand the remaining notoptimizedforpreservation. Overall,theseex-
headroominourtask,weask: whatistheminimal perimentsaremainlymeanttoillustratethatprior
amount of editing needed to make a text passage models were simply not designed for the task of
fullyattributed?
Theanswerwoulddependonthe EditingforAttribution,ratherthantomarkRARR
| qualityoftheLMthatgeneratedthetextaswellas |     |                          |     |     |     | asthebestmethod. |     |     |     |     |     |     |
| ------------------------------------------ | --- | ------------------------ | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
| thetaskdifficulty.                         |     | Asanapproximation,weman- |     |     |     |                  |     |     |     |     |     |     |
ually edited 30 examples in our NQ benchmark Analyzing RARR For the research stage, the
untilwejudgedthemtobe100%attributable. We questiongenerationmodelhadcomprehensivecov-
achievedapreservationscoreof88%,which(when erage: amanualinspectionof40examplesshows
combinedwith100%attribution)translatesto93.6 > 80% with questions that fully cover all aspects
F1 ,indicatingasignificantheadroom. oftheinputtext. Theretrieverwasstrongestatre-
AP

(a)Correctlyrevisinganentity cessfully revised an incorrect claim, but did not
y: IfSheKnewWhatSheWantswaswrittenbyHenryRoth.
revisesubsequentreasoningstepsthatdependon
e: [en.wikipedia.org]“IfSheKnewWhatSheWants”isasongwrittenby
Americansinger-songwriterJulesShearandintroducedon...
|     |     |     |     |     | theearlierclaim(Figure7e). |     |     | Inthiscase,further |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------------------ | --- |
y′: IfSheKnewWhatSheWantswaswrittenbyJulesShear.
(b)Correctlyrevisinganumber editingtoimprovelogicalcoherencecouldhelp.
y: GodSavetheQueenbecametheBritishnationalanthemin1745....
e: [www.britannica.com]TheoldestnationalanthemisGreatBritain’s“God
|     |     |     |     |     | 6.2 Ablations |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
SavetheQueen,”whichwasdescribedasanationalanthemin1825,...
y′: GodSavetheQueenbecametheBritishnationalanthemin1825....
(Theyear1745waswhenthesongwasfirstperformed.) Ablatingquerygeneration RARRusesgener-
(c)Performinganecessarylargerrevision ated questions as search queries for evidence re-
y:
| “It’s My Party” | is a song written | and composed | by American | singer- |     |     |     |     |     |
| --------------- | ----------------- | ------------ | ----------- | ------- | --- | --- | --- | --- | --- |
songwriterandproducerWalterGold. Thesongwaspublishedin1962 trieval. Weconsidertwonaturalalternatives: using
andfirstrecordedbyAmericansinger-songwriter,producerandarranger
LesleyGore. the entire input passage as a single search query,
e:
[secondhandsongs.com]Song:It’sMyPartywrittenbyJohnGluck,Wally orusingeachsentenceasasearchquery. Forthe
Gold,SeymourGottlieb,HerbertWeiner...
y′:
“It’sMyParty”isasongwrittenandcomposedbyJohnGluck,WallyGold, former, we retrieve J = 3 evidence snippets to
SeymourGottliebandHerbWeiner.Thesongwaspublishedin1963and
firstrecordedbyAmericansingerLesleyGore. maketheamountaclosermatchtoothermethods.
(d)Confusedbymisleadingevidence
y: IntheHeatoftheNightisapoliceproceduralcrimedramaTVseriesproduced TheresultsareinTable2. Usingtheentireinput
byMGMTelevision. ItairedonNBCfromSeptember8,1988toMay3, passageasthequerygivespoorresults, asthere-
1992....
e: [metv.com]WatchIntheHeatoftheNightonMeTV. trievedevidencetendstonotfocusonpotentially
y′: IntheHeatoftheNightisapoliceproceduralcrimedramaTVseriesproduced
byMGMTelevision.ItairedonMeTVfromSeptember8,1988toMay3, unattributedpartsinthepassage. Usingsentences
1992....
|     |     |     |     |     | as queries | gives results | closer | to the | full CQGen, |
| --- | --- | --- | --- | --- | ---------- | ------------- | ------ | ------ | ----------- |
(TheshowdidactuallyaironNBCinthe1980s,butthemodelfailstorealize
thatMeTVisare-runmuchlaterintime.)
butacloseranalysisrevealstwocaveats.
(e)Improvedattribution,butreasoningdoesn’tadapttonewinfo
(Q:DoesHomerSimpsonneedtwohandsworthoffingerstocountto5?) First, sentences-as-queries are more effective
y: HomerSimpsonhas5fingersand2hands.Therefore,hedoesnotneedtwo
handsworthoffingerstocountto5.Heonlyneedonehandtocountto5. whensuchsentences“mimic”contentontheWeb,
e: [refinery29.com]Othericonicanimatedcharacters,suchasHomerSimpson andarelesseffectiveotherwise. InTable3,wetest
andhisbrood,...onlyhavefourfingers,too.
y′: HomerSimpsonhas4fingersand2hands.Therefore,hedoesnotneedtwo thisbyexcludingallofWikipediafromwebsearch
handsworthoffingerstocountto5.Heonlyneedonehandtocountto5.
(Havingonly4fingersperhand,hedoesneedtwohandstocountto5.) results (since many PaLM outputs for NQ have
|                                            |     |     |     |     | a Wikipedia | style). | The attribution |     | performance |
| ------------------------------------------ | --- | --- | --- | --- | ----------- | ------- | --------------- | --- | ----------- |
| Figure7: ExamplerevisionsfromRARR,bothgood |     |     |     |     |             |         |                 |     |             |
ofsentences-as-queriesdropssignificantly,while
| andbad. y=partiallyeditedpassage;e=evidence;y′ |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CQGenismorerobust.
=passageaftereditingwithe.
|     |     |     |     |     | Second,  | sentence-as-queries |           | tends        | to retrieve |
| --- | --- | --- | --- | --- | -------- | ------------------- | --------- | ------------ | ----------- |
|     |     |     |     |     | passages | that may            | encourage | confirmation | bias.       |
searchingcontentinvolvingdistinctentities(e.g.,a Considertheexample“GeorgiaiscalledthePeach
| movie,amajorevent,oraperson). |     |     | Incontrast,we |     |            |            |          |          |          |
| ----------------------------- | --- | --- | ------------- | --- | ---------- | ---------- | -------- | -------- | -------- |
|                               |     |     |               |     | State, but | California | actually | produces | the most |
found significant headroom for better attribution peaches.” Retrieval using sentences-as-queries
ofstatementsinvolvinggenericobjectsandmore foundanarticleechoingthatCaliforniaproduces
abstract claims (e.g. “Video games require elec- themostpeaches,whileCQGengeneratedthemore
tricity.”—sincethisisobvioustomosthumans,re- impartial query “Which state produces the most
trievedarticlesfromthewebtendtoaddressrelated peaches?” and found a newer article saying that
butdifferenttopics). Wesuspectthatasignificant SouthCarolinareplacedCaliforniaasthetoppeach
amountofattributionheadroomonourbenchmarks
|     |     |     |     |     | producer. | Inthiscase,RARRusingCQGenneeds |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------------------------------ | --- | --- | --- |
wouldbenefitfromabetterresearchstage. tosacrificemorepreservationscoretoeditthetext,
Fortherevisionstage,RARRwasabletorevise leading to a lower F1 score. This underscores
AP
manyunattributedclaims,especiallythoseinvolv- thatattributionalonecannotmeasure“correctness”
ingentitiesandnumbers(Figures7aand7b). Itcan sincenotallevidenceisup-to-dateorreliable.
alsoperformlargerrevisionswhennecessary(Fig-
|                    |      |          |      |         | Ablating | agreement | model | We try | removing |
| ------------------ | ---- | -------- | ---- | ------- | -------- | --------- | ----- | ------ | -------- |
| ure 7c). Moreover, | RARR | abstains | from | editing |          |           |       |        |          |
theagreementmodel,whicheffectivelyforcesthe
| whentheclaimisalreadywell-attributed: |     |     |     | onNQ, |          |            |         |       |              |
| ------------------------------------- | --- | --- | --- | ----- | -------- | ---------- | ------- | ----- | ------------ |
|                                       |     |     |     |       | model to | revise the | passage | based | on every re- |
amongtheinputswithnear-perfectattribution(pre-
|                  |                              |     |     |     | trievedevidence.                            |     | TheresultsareshowninTable2. |     |     |
| ---------------- | ---------------------------- | --- | --- | --- | ------------------------------------------- | --- | --------------------------- | --- | --- |
| editAttr         | > 0.9),RARRdoesnotmakeanedit |     |     |     |                                             |     |                             |     |     |
| AIS              |                              |     |     |     | Asexpected,morerevisionleadstolesspreserva- |     |                             |     |     |
| in90%ofthecases. | However,thesystemalsohas     |     |     |     |                                             |     |                             |     |     |
tionscoreandspuriouschangestothetextpassage,
| severalshortcomings. | Someerroneouseditsarise |     |     |     |     |     |     |     |     |
| -------------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
asdemonstratedinFigure8.
| from misleading | irrelevant | evidence | (Figure | 7d). |     |     |     |     |     |
| --------------- | ---------- | -------- | ------- | ---- | --- | --- | --- | --- | --- |
We also observed an interesting challenge when Impactondownstreamtaskperformance We
revising reasoning chains, where the model suc- have measured preservation using the metric de-

|       |     | PaLMoutputsonNQ |      |        | PaLMoutputsonSQA |      |     |     | LaMDAoutputsonQReCC |      |      |     |
| ----- | --- | --------------- | ---- | ------ | ---------------- | ---- | --- | --- | ------------------- | ---- | ---- | --- |
| Model |     | Attr            | Pres | F1     | Attr             | Pres |     | F1  | Attr                |      | Pres | F1  |
|       |     |                 | auto | Lev AP | auto             |      | Lev | AP  |                     | auto | Lev  | AP  |
FullRARR 45.6→54.9 89.6 68.1 37.6→45.1 89.9 60.0 18.8→29.4 80.2 43.1
noagreementmodel 45.6→50.6 82.6 62.8 37.8→46.9 83.4 60.0 18.8→28.8 72.0 41.2
query=input 45.4→47.2 98.4 63.8 39.4→30.3 98.8 46.4 19.7→20.6 96.3 34.0
query=sentence 49.1→52.1 97.0 67.8 43.7→44.3 98.8 61.2 19.0→19.6 97.0 32.6
Table2: Ablationresults. Wereporttheautomaticmetrics: Attr auto ,Pres Lev ,andharmonicmeanbetweenthetwo
(F1 ). Weshowauto-AISscoresbothbeforeandafterediting(before→edit),withrespecttotheattributionreport
AP
Aproducedbythemodel. Eventhoughsentence-as-queriesmayachievesimilarF1 asRARR,itislessrobustto
AP
corpusshiftsandtendstoretrievepassagesthatmayencourageconfirmationbias.
|     |     | NQF1 | SQAF1 |     | that | RARR | not | only | preserves | the | short | answer |
| --- | --- | ---- | ----- | --- | ---- | ---- | --- | ---- | --------- | --- | ----- | ------ |
|     |     |      | AP    | AP  |      |      |     |      |           |     |       |        |
accuracybutactuallyimprovesitbyroughly5%.
| Model | orig | nowiki | orig | nowiki |     |     |     |     |     |     |     |     |
| ----- | ---- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
FullRARR 68.1 64.3 60.0 57.6 ForSQA,eachoriginaltextisareasoningchain
query=sentence 67.8 60.3 61.2 56.7 thathelpstoanswerayes/noquestion. Wefeedthe
|     |     |     |     |     | SQAquestionandy |     |     |     | backintoPaLMandprompt |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --------------------- | --- | --- | --- |
Table3: TheimpactofexcludingWikipediafromthe
ittooutputayes/noanswer,andevaluateanswer
retrievalcorpus.CQGen(fullRARR)ismorerobustto
Wikipedia’sabsence,whileusingsentences-as-queries accuracy. Here,wefindthatincreasingattribution
|     |     |     |     |     | comes | at  | a slight | cost | in downstream |     | task | perfor- |
| --- | --- | --- | --- | --- | ----- | --- | -------- | ---- | ------------- | --- | ---- | ------- |
suffersabiggerdropinperformance.
|     |     |     |     |     | mance:                    | answer |     | accuracy | drops |                   | modestly | for all |
| --- | --- | --- | --- | --- | ------------------------- | ------ | --- | -------- | ----- | ----------------- | -------- | ------- |
|     |     |     |     |     | revisionmodels(upto2.6%). |        |     |          |       | Wesuspectthatthis |          |         |
x: TheCrown-of-thornsstarfishisnativetotheGreatBarrierReef...The
starfishwasintroducedtotheGreat-Barrier-Reefbyoceancurrents. may be due to noisy retrievals, which sometimes
e: [invasivespeciesinfo.gov]Ballastwaterisoneofthemajorpathwaysfor
theintroductionofnonindigenousmarinespecies... provide misleading evidence (exemplifiedin Fig-
y: TheCrown-of-thornsstarfishisnativetotheGreatBarrierReef...The
starfishwasintroducedtotheGreat-Barrier-Reefbyballastwater. ure 7d). Furthermore, even though revisions can
addressfactoiderrorsinthepassage(e.g.,“Homer
| Figure 8: Disabling                                |     | the agreement | model | leads | to      |     |       |          |      |        |      |      |
| -------------------------------------------------- | --- | ------------- | ----- | ----- | ------- | --- | ----- | -------- | ---- | ------ | ---- | ---- |
|                                                    |     |               |       |       | Simpson |     | has 5 | fingers” | from | Figure | 7e), | RARR |
| over-edits. Here,theevidenceedoesnotexplicitlydis- |     |               |       |       |         |     |       |          |      |        |      |      |
currentlydoesnottrytomodifysubsequentreason-
agreewithx,butwithoutanagreementmodeltodetect
ingstepswhichmaynolongerbelogicallyentailed
this,theeditmodelmakesanunsupportedchange.
(e.g.,“Heonlyneedsonehandtocountto5”).
7 Conclusion
|     |     |     |     |     | Language |              | models | have      | developed |     | increasingly |     |
| --- | --- | --- | --- | --- | -------- | ------------ | ------ | --------- | --------- | --- | ------------ | --- |
|     |     |     |     |     | good     | “procedural” |        | knowledge |           | of  | what should  | be  |
discussedandhowitshouldbepresented,butoften
| Figure9: DownstreamtaskperformanceonNQand |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
struggletomemorize“factoid”knowledgeandpro-
SQA.RARR’srevisionsleadtobetteransweraccuracy
|     |     |     |     |     | duceunsubstantiatedclaims. |     |     |     |     | WeproposedRARR, |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --------------- | --- | --- |
onNQ.NomodelsimprovedansweraccuracyonSQA.
aframeworkforrevisingsuchclaimstomakethem
|     |     |     |     |     | attributable |     | to the | researched |     | evidence. |     | From ex- |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | ---------- | --- | --------- | --- | -------- |
fined in Section 2.2. However, another measure perimentsontextpassagesgeneratedbydifferent
modelsonvariousdomains,weshowedthatRARR
ofpreservationiswhethertherevisedtextcanstill
canrevisethepassagestoimproveattributionwhile
| be used to perform |     | the task | that it was | originally |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
generatedfor. FollowingEFEC,wequantitatively preservingotherdesirablepropertiessuchaswrit-
evaluatethisonshortanswertasksNQandSQA, ingstyleorstructure. Furthermore,RARRsitson
topofexistinggenerationmodelswithoutneeding
andwesummarizetheresultinFigure9.
tore-designorre-trainLMs.
| For NQ, each | original |     | text x is a long-form |     | re- |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sponsetoafactoidquestion. Todeterminewhether Major headroom still remains, as discussed in
therevisedtexty stillservesthispurpose,wefeed Section6andtheLimitationssection. Wehopeour
the factoid question and y back into PaLM and analysisofRARRwouldhelpwithdevelopingnew
promptittoextractashortanswerfromy. Wefind approachesforintegratingattributiontoLMs.

8 Limitations
|             |        |                 |           | thandeleteclaimsthatitcannotattribute. |           |                | Someof       |
| ----------- | ------ | --------------- | --------- | -------------------------------------- | --------- | -------------- | ------------ |
|             |        |                 |           | these claims                           | genuinely | do not require | attribution, |
| Limitations | of our | task definition | Depending |                                        |           |                |              |
butothersarehallucinationandshouldberemoved.
ontheapplication,attributionandpreservationmay
Judgingwhetheraclaimrequiresattributioncanbe
notdeserveequalweight. Forinstance,ifthereare subjectiveandchallenging. Finally, ourmodelis
multipleacceptableoptionsfortheoutput,suchas computationallycostly,sinceitisbasedonprompt-
inadialogsystem,wemighttrade-offpreservation
|     |     |     |     | ing a large | language model. | One | potential solu- |
| --- | --- | --- | --- | ----------- | --------------- | --- | --------------- |
forattribution,similartohowLaMDAbehavesin
tionistoleveragerecentsyntheticdatageneration
| ourexperiments.                         |     |                           |     | recipestotrainasmallermodel(Leeetal.,2021; |     |     |     |
| --------------------------------------- | --- | ------------------------- | --- | ------------------------------------------ | --- | --- | --- |
| Ourevaluationmetricsalsodonotmeasureall |     |                           |     | Schicketal.,2022).                         |     |     |     |
| aspectsofattribution.                   |     | Forinstance,somesentences |     |                                            |     |     |     |
areself-evidentanddonotrequireattribution(e.g.,
9 Ethicalconsiderations
| “Iagree.”) | butwouldbepenalizedinourevaluation. |     |     |     |     |     |     |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Itisalsonecessarytonotethatlinguisticassertions Partial attribution When RARR is not 100%
| havevaryingscope: |     | forexample,thereisadiffer- |     |     |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- | --- |
successfulinmakingtextconsistentwithretrieved
ence between “Frozen is a scary movie” and “I evidence, the revised text will be partially at-
gotscaredwatchingFrozen”—whileexpressinga tributed. Onecouldidentifyunattributedpartsus-
similarsentiment,theformermakesamoregeneral
|     |     |     |     | ingeithertheautomatedattributionscore(Attr |     |     | AIS ) |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- | ----- |
statementthatmanywoulddisagreewith,whilethe ortherelevancescoresusedtogeneratetheattribu-
latter is scoped to the speaker’s own experience. tionreport(Section3.3). Suchinformationshould
In some applications, one could even argue that bepresentedtoavoidmisleadingreadersintothink-
| the latter | case does not | require attribution, | since |     |     |     |     |
| ---------- | ------------- | -------------------- | ----- | --- | --- | --- | --- |
ingthattheentirerevisionisattributed.
| the speaker | is their own | source-of-truth. | In addi- |     |     |     |     |
| ----------- | ------------ | ---------------- | -------- | --- | --- | --- | --- |
tion to varying scope, utterances can also make Evidence trustworthiness RARR seeks to im-
assertions with varying levels of directness. For proveattribution forthe output of any generative
example,accordingtostandardlinguistics,“John model. However,evenifRARRcanattributecon-
atesomeofthecookies”yieldstheimplicaturethat tenttoaparticularsource,theusermuststillcon-
all
John did not eat of the cookies, even though siderwhetherthesourceitselfistrustworthy. Even
it is not logically entailed. This raises the ques- for sources that are traditionally considered “au-
tion of which implicatures or implied assertions thoritative” (such as an encyclopedia), there may
shouldbedetectedandattributed,whichshouldbe still be factual inaccuracies or biases. This work
explored in future work. For more nuances, we doesnotaddressthequestionofwhetherasource
refertoRashkinetal.(2021). istrustworthy,ortherelatedtopicofmisinforma-
Forpreservation,wewishtoexploreotherprop- tion. Whilewedonotprovideameansforjudging
ertiesthatshouldbepreserved,suchasdiscourse trustworthiness,thedesignofRARRdoesallowfor
orlogicalcoherence. Additionally,iftheinputtext theresearchstagetorestrictitssearchoverauser-
passageiscompletelymisguidedorflawed,itcan specified corpus, based on what the user deems
| be difficult | to revise | the text without | significant | trustworthy. |     |     |     |
| ------------ | --------- | ---------------- | ----------- | ------------ | --- | --- | --- |
changes,whichwouldbeheavilypenalizedbythe
currentmetrics. Conflictingevidence Thereisalsothepossibility
thatsomecontentmaybesimultaneouslysupported
Limitations of our model While we aspire to by certain sources, while contradicted by others.
improve attribution for arbitrary text, it is clear Thiscaneasilyoccurforcontentinvolvingsubjec-
that RARR is not yet fully general. For example, tiveorimpreciseclaims. Thecurrentimplementa-
the current implementation of RARR would not tionandevaluationforRARRdoesnotexplicitly
bewell-preparedtoeditpoetry(wherepreserving address this issue — we adopted a “permissive”
rhyme matters) or long documents, primarily be- definitionofattribution,whereweconsidercontent
causewedonotprovideexamplesofsuchinputs tobeattributedifthereexistsanysourcethatsup-
inourfew-shotLLMprompts. However,wedobe- portsit. Forsomeapplications,amorerestrictive
lievethatfuturedevelopersmaybeabletoquickly definitionthatrequiresbothexistenceofsupport-
adaptRARRtosuchtasksbysimplychangingthe ing sources and absence of contradicting sources
| prompts. | Second,RARRtendstopreserverather |     |     | wouldbeneeded. |     |     |     |
| -------- | -------------------------------- | --- | --- | -------------- | --- | --- | --- |

Acknowledgments
|     |     |     |     |     |     |     | Kelvin Guu). | Advised |     | on model |     | design | and con- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | -------- | --- | ------ | -------- |
tributedmanypartsofthewriting.
WewishtothankRaphaelHoffmann,SlavPetrov,
|          |              |     |          |     |          |       | Yicheng | Fan: | Worked | with | Kelvin | Guu | to de- |
| -------- | ------------ | --- | -------- | --- | -------- | ----- | ------- | ---- | ------ | ---- | ------ | --- | ------ |
| Dipanjan | Das, Michael |     | Collins, |     | Iftekhar | Naim, |         |      |        |      |        |     |        |
velopthefirstprototypeofRARR.Proposedmulti-
KristinaToutanova,WilliamCohen,SundeepTiru-
pleretrievalstrategiesandimplementedtheEFEC
| malareddy,SamerHassan,QuocLeandHeng-Tze |     |     |     |     |     |     | baseline. |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Chengfortheirresearchmentorship,feedbackand
|          |        |          |     |     |      |          | VincentZhao: |     | Co-hostedandmentoredLuyu |     |     |     |     |
| -------- | ------ | -------- | --- | --- | ---- | -------- | ------------ | --- | ------------------------ | --- | --- | --- | --- |
| support. | We are | grateful | to  | Hao | Zhou | and Petr |              |     |                          |     |     |     |     |
Gao(studentresearcher)inprototypingRARR.En-
PilarforhelpingusexperimentwithLaMDAand
abledbulkinferenceforPaLM.Proposedthedown-
| motivatingourdialogexperiments. |     |     |     |     | Wealsowish |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
streamtaskevaluation.
| to thank | Tal Schuster | for      | pointing    |     | us to | relevant |        |                                    |     |     |     |     |     |
| -------- | ------------ | -------- | ----------- | --- | ----- | -------- | ------ | ---------------------------------- | --- | --- | --- | --- | --- |
|          |              |          |             |     |       |          | NiLao: | Researchmentorship,advisingandcon- |     |     |     |     |     |
| work in  | the fact     | checking | literature, |     | and   | helping  |        |                                    |     |     |     |     |     |
tributedmanypartsofthewriting.
| usreproduceit. | WethankVitalyNikolaev,David |     |     |     |     |     |             |     |                             |     |     |     |     |
| -------------- | --------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --------------------------- | --- | --- | --- | --- |
|                |                             |     |     |     |     |     | HongraeLee: |     | Researchmentorshipandadvis- |     |     |     |     |
ReitterandRoeeAharoniforhelpingususeAIS
|     |     |     |     |     |     |     | ing. HelpedintegrateRARRwithGoogleSearch |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
andauto-AIS.WealsowishtothankJianmoNiand
andevaluateLaMDA.
HongleiZhuangfordevelopingthequery-evidence
|     |     |     |     |     |     |     | Da-ChengJuan: |     | Researchmentorshipandearly |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------------- | --- | --- | --- | --- |
relevancemodelweuse,DanielAndorfordevelop-
designdiscussions.
ingthesentencedecontextualizationmodelweuse,
|         |          |             |           |     |     |        | KelvinGuu: |     | Proposedtheoriginalresearch-and- |     |     |     |     |
| ------- | -------- | ----------- | --------- | --- | --- | ------ | ---------- | --- | -------------------------------- | --- | --- | --- | --- |
| and Ran | Tian for | the initial | prototype |     | of  | CQGen. |            |     |                                  |     |     |     |     |
Finally, we thank Kathy Meier-Hellstern, Philip reviseconcept,implementedthefirstprototype,ini-
|     |     |     |     |     |     |     | tiatedtheprojectandinvolvedallcollaborators. |     |     |     |     |     | Im- |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
ParhamandDianeKorngiebelfortheirthoughtful
plementedbaselines(togetherwithYichengFan).
feedbackonethicalconsiderations.
Researchmentorship,oversawprojectcoordination
andpaperwriting.
Contributions
| LuyuGao: | DesignedRARR’sfew-shotprompting |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
References
strategiesandimplementedthefirstPaLM-based
| prototype. | Analyzed | results, |     | and | advised | on the |             |     |           |     |           |     |           |
| ---------- | -------- | -------- | --- | --- | ------- | ------ | ----------- | --- | --------- | --- | --------- | --- | --------- |
|            |          |          |     |     |         |        | Michael Ahn | et  | al. 2022. | Do  | as I can, | not | as I say: |
designofhumanandautomaticevaluation.
|            |     |                              |     |     |     |     | Groundinglanguageinroboticaffordances. |     |     |     |     |     | ArXiv, |
| ---------- | --- | ---------------------------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ------ |
| ZhuyunDai: |     | Proposedtheevaluationsetupof |     |     |     |     | abs/2204.01691.                        |     |     |     |     |     |        |
editinglong-formgenerationsfromPaLM/LaMDA
|                      |     |     |                       |     |     |     | Raviteja Anantha, |          | Svitlana | Vakulenko, |            | Zhucheng | Tu,        |
| -------------------- | --- | --- | --------------------- | --- | --- | --- | ----------------- | -------- | -------- | ---------- | ---------- | -------- | ---------- |
| onvariousQAdatasets. |     |     | HostedandmentoredLuyu |     |     |     |                   |          |          |            |            |          |            |
|                      |     |     |                       |     |     |     | Shayne            | Longpre, | Stephen  |            | G. Pulman, |          | and Srini- |
Gao(studentresearcher)inprototypingRARR.Im-
|     |     |     |     |     |     |     | vasChappidi.2021. |     |     | Open-domainquestionanswer- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | -------------------------- | --- | --- | --- |
plementedthefinalmodels,designedoverallexper- ing goes conversational via question rewriting. In
NAACL.
iments,andobtainedmainresultsandablations(to-
| getherwithIcePasupat). |     |     | Contributedmanyparts |     |     |     |                      |     |     |           |        |           |     |
| ---------------------- | --- | --- | -------------------- | --- | --- | --- | -------------------- | --- | --- | --------- | ------ | --------- | --- |
|                        |     |     |                      |     |     |     | Isabelle Augenstein, |     |     | Christina | Lioma, | Dongsheng |     |
ofthewriting.
|             |                               |     |     |     |     |     | Wang,                                 | Lucas | Chaves | Lima, | Casper | Hansen, | Chris- |
| ----------- | ----------------------------- | --- | --- | --- | --- | --- | ------------------------------------- | ----- | ------ | ----- | ------ | ------- | ------ |
| IcePasupat: | Implementedthefinalmodels,de- |     |     |     |     |     |                                       |       |        |       |        |         |        |
|             |                               |     |     |     |     |     | tianHansen,andJakobGrueSimonsen.2019. |       |        |       |        |         | Mul-   |
signedoverallexperiments,andobtainedmainre- tiFC:Areal-worldmulti-domaindatasetforevidence-
|                                           |     |     |     |     |     |     | basedfactcheckingofclaims. |     |     |     | InEMNLP. |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | -------- | --- | --- |
| sultsandablations(togetherwithZhuyunDai). |     |     |     |     |     | Au- |                            |     |     |     |          |     |     |
tomatedexperimentalinfrastructure,conducteder-
VidhishaBalachandran,HannanehHajishirzi,William
roranalyses,andoversawmanypartsofthepaper
|              |     |                             |     |     |     |     | Cohen,andYuliaTsvetkov.2022.                    |     |     |     | Correctingdiverse |          |     |
| ------------ | --- | --------------------------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | ----------------- | -------- | --- |
| writing.     |     |                             |     |     |     |     | factualerrorsinabstractivesummarizationviapost- |     |     |     |                   |          |     |
|              |     |                             |     |     |     |     | editingandlanguagemodelinfilling.               |     |     |     |                   | InEMNLP. |     |
| AnthonyChen: |     | Developedtheautomaticevalu- |     |     |     |     |                                                 |     |     |     |                   |          |     |
ationforattributionandpreservationandworked
BerndBohnet,VinhQuangTran,PatVerga,RoeeAha-
| with Arun | Chaganty | to  | design | human | evaluation. |     |              |     |        |       |         |         |       |
| --------- | -------- | --- | ------ | ----- | ----------- | --- | ------------ | --- | ------ | ----- | ------- | ------- | ----- |
|           |          |     |        |       |             |     | roni, Daniel |     | Andor, | Livio | Baldini | Soares, | Jacob |
Developedtheopen-sourceimplementation(GPT- Eisenstein,KuzmanGanchev,JonathanHerzig,Kai
| 3 RARR), | made | improvements |     | to  | prompts, | and |     |     |     |     |     |     |     |
| -------- | ---- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Hui,TomKwiatkowski,JiMa,JianmoNi,TalSchus-
helpedwithwriting. ter, William W. Cohen, Michael Collins, Dipanjan
Das,DonaldMetzler,SlavPetrov,andKellieWebster.
| ArunChaganty: |     | Ledandimplementedallhu- |     |     |     |     |       |            |          |     |            |     |            |
| ------------- | --- | ----------------------- | --- | --- | --- | --- | ----- | ---------- | -------- | --- | ---------- | --- | ---------- |
|               |     |                         |     |     |     |     | 2022. | Attributed | question |     | answering: |     | Evaluation |
man evaluation. Proposed the two-dimensional andmodelingforattributedlargelanguagemodels.
| attribution | + preservation |     | metric |     | (together | with |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | ------ | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ArXiv.

SamuelR.Bowman,GaborAngeli,ChristopherPotts, ShirleyAnugrahHayati,RaphaëlOlivier,PravalikaAv-
and Christopher D. Manning. 2015. A large anno- varu,PengchengYin,AnthonyTomasic,andGraham
tatedcorpusforlearningnaturallanguageinference. Neubig.2018. Retrieval-basedneuralcodegenera-
| InEMNLP. |     |     |     |     |     |     | tion. InEMNLP. |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
DanHendrycks,CollinBurns,StevenBasart,AndyZou,
TomB.Brown,BenjaminMann,NickRyder,Melanie
MantasMazeika,DawnSong,andJacobSteinhardt.
| Subbiah, | Jared | Kaplan, | Prafulla |     | Dhariwal, | Arvind |     |     |     |     |     |     |
| -------- | ----- | ------- | -------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- |
Neelakantan,PranavShyam,GirishSastry,Amanda 2021. Measuringmassivemultitasklanguageunder-
| Askell,  | Sandhini |     | Agarwal, | Ariel     | Herbert-Voss, |        | standing.   | InICLR.      |     |                 |     |       |
| -------- | -------- | --- | -------- | --------- | ------------- | ------ | ----------- | ------------ | --- | --------------- | --- | ----- |
| Gretchen | Krueger, |     | T. J.    | Henighan, | Rewon         | Child, |             |              |     |                 |     |       |
|          |          |     |          |           |               |        | OrHonovich, | RoeeAharoni, |     | JonathanHerzig, |     | Hagai |
AdityaRamesh,DanielM.Ziegler,JeffWu,Clemens
Taitelbaum,DoronKukliansy,VeredCohen,Thomas
Winter,ChristopherHesse,MarkChen,EricSigler,
|     |     |     |     |     |     |     | Scialom, | Idan Szpektor, |     | Avinatan | Hassidim, | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | -------- | --------- | --- |
MateuszLitwin,ScottGray,BenjaminChess,Jack
|          |                    |            |     |                |         |       | Y.Matias.2022. | TRUE:Re-evaluatingfactualcon- |     |          |     |           |
| -------- | ------------------ | ---------- | --- | -------------- | ------- | ----- | -------------- | ----------------------------- | --- | -------- | --- | --------- |
| Clark,   | ChristopherBerner, |            |     | SamMcCandlish, |         | Alec  |                |                               |     |          |     |           |
|          |                    |            |     |                |         |       | sistency       | evaluation.                   | In  | Workshop | on  | Document- |
| Radford, | Ilya               | Sutskever, |     | and Dario      | Amodei. | 2020. |                |                               |     |          |     |           |
Languagemodelsarefew-shotlearners. InNeurIPS. groundedDialogueandConversationalQuestionAn-
swering.
| Mengyao                         | Cao, | Yue | Dong,                     | Jiapeng | Wu, and  | Jackie |                |                |          |             |               |            |
| ------------------------------- | ---- | --- | ------------------------- | ------- | -------- | ------ | -------------- | -------------- | -------- | ----------- | ------------- | ---------- |
|                                 |      |     |                           |         |          |        | Or Honovich,   | Leshem         | Choshen, |             | Roee Aharoni, | Ella       |
| ChiKitCheung.2020.              |      |     | Factualerrorcorrectionfor |         |          |        |                |                |          |             |               |            |
|                                 |      |     |                           |         |          |        | Neeman,        | Idan Szpektor, |          | and Omri    | Abend.        | 2021.      |
| abstractivesummarizationmodels. |      |     |                           |         | InEMNLP. |        |                |                |          |             |               |            |
|                                 |      |     |                           |         |          |        | Q2: Evaluating | factual        |          | consistency | in            | knowledge- |
groundeddialoguesviaquestiongenerationandques-
DanqiChen,AdamFisch,JasonWeston,andAntoine
|              |     |                               |     |     |     |     | tionanswering. | InEMNLP. |     |     |     |     |
| ------------ | --- | ----------------------------- | --- | --- | --- | --- | -------------- | -------- | --- | --- | --- | --- |
| Bordes.2017. |     | ReadingWikipediatoansweropen- |     |     |     |     |                |          |     |     |     |     |
domainquestions. InACL. HayateIso,ChaoQiao,andHangLi.2020. Fact-based
|        |       |            |           |     |         |       | textediting. | InACL. |     |     |     |     |
| ------ | ----- | ---------- | --------- | --- | ------- | ----- | ------------ | ------ | --- | --- | --- | --- |
| Eunsol | Choi, | Jennimaria | Palomaki, |     | Matthew | Lamm, |              |        |     |     |     |     |
Tom Kwiatkowski, Dipanjan Das, and Michael GeorgiKaradzhov,PreslavNakov,LluísMàrquez,Al-
| Collins.           | 2021. | Decontextualization: |                 |     | Making | sen- |                                            |     |     |     |     |       |
| ------------------ | ----- | -------------------- | --------------- | --- | ------ | ---- | ------------------------------------------ | --- | --- | --- | --- | ----- |
|                    |       |                      |                 |     |        |      | bertoBarrón-Cedeño,andIvanKoychev.2017.    |     |     |     |     | Fully |
| tencesstand-alone. |       |                      | TACL,9:447–461. |     |        |      |                                            |     |     |     |     |       |
|                    |       |                      |                 |     |        |      | automatedfactcheckingusingexternalsources. |     |     |     |     | In    |
RANLP.
| Aakanksha | Chowdhery |     | et  | al. 2022. | PaLM: | Scal- |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
ing language modeling with pathways. ArXiv, VladimirKarpukhin,BarlasOg˘uz,SewonMin,Patrick
| abs/2204.02311. |     |     |     |     |     |     | Lewis,LedellYuWu,SergeyEdunov,DanqiChen, |     |     |                          |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | ------------------------ | --- | --- |
|                 |     |     |     |     |     |     | andWentauYih.2020.                       |     |     | Densepassageretrievalfor |     |     |
NouhaDziri,SivanMilton,MoYu,OsmarZaiane,and open-domainquestionanswering. InEMNLP.
| Siva | Reddy. | 2022. | On the | origin | of hallucinations |     |     |     |     |     |     |     |
| ---- | ------ | ----- | ------ | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
in conversational models: Is it the datasets or the UrvashiKhandelwal,OmerLevy,DanJurafsky,Luke
|                                               |                |     |                        |     |     |     | Zettlemoyer,andMikeLewis.2020. |         |     |                         | Generalization |     |
| --------------------------------------------- | -------------- | --- | ---------------------- | --- | --- | --- | ------------------------------ | ------- | --- | ----------------------- | -------------- | --- |
| models?                                       | InNAACL.       |     |                        |     |     |     |                                |         |     |                         |                |     |
|                                               |                |     |                        |     |     |     | throughmemorization:           |         |     | Nearestneighborlanguage |                |     |
| AlexanderR.Fabbri,WojciechKryscinski,BryanMc- |                |     |                        |     |     |     | models.                        | InICLR. |     |                         |                |     |
| Cann,                                         | RichardSocher, |     | andDragomirRadev.2021. |     |     |     |                                |         |     |                         |                |     |
SummEval: Re-evaluatingsummarizationevaluation. TusharKhot,AshishSabharwal,andPeterClark.2018.
| TACL,9:391–409. |     |     |     |     |     |     | SciTaiL:Atextualentailmentdatasetfromscience |     |         |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | ------- | --- | --- | --- |
|                 |     |     |     |     |     |     | questionanswering.                           |     | InAAAI. |     |     |     |
AngelaFan,YacineJernite,EthanPerez,DavidGrang-
|            |         |     |             |     |             |       | Kalpesh Krishna, | Aurko | Roy, | and | Mohit Iyyer. | 2021. |
| ---------- | ------- | --- | ----------- | --- | ----------- | ----- | ---------------- | ----- | ---- | --- | ------------ | ----- |
| ier, Jason | Weston, |     | and Michael |     | Auli. 2019. | ELI5: |                  |       |      |     |              |       |
Hurdlestoprogressinlong-formquestionanswering.
| Longformquestionanswering. |     |     |     | InACL. |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
InNAACL.
| Angela | Fan, Aleksandra |     | Piktus, | Fabio | Petroni, | Guil- |     |     |     |     |     |     |
| ------ | --------------- | --- | ------- | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- |
WojciechKryscinski,BryanMcCann,CaimingXiong,
| laume                                  | Wenzek, | Marzieh |     | Saeidi,  | Andreas | Vlachos, |             |                |       |            |                |             |
| -------------------------------------- | ------- | ------- | --- | -------- | ------- | -------- | ----------- | -------------- | ----- | ---------- | -------------- | ----------- |
|                                        |         |         |     |          |         |          | and Richard | Socher.        | 2020. | Evaluating |                | the factual |
| AntoineBordes,andSebastianRiedel.2020. |         |         |     |          |         | Gener-   |             |                |       |            |                |             |
|                                        |         |         |     |          |         |          | consistency | of abstractive |       | text       | summarization. | In          |
| atingfactcheckingbriefs.               |         |         |     | InEMNLP. |         |          |             |                |       |            |                |             |
EMNLP.
MorGeva,DanielKhashabi,EladSegal,TusharKhot,
|                                 |     |                                 |     |     |              |     | Tom Kwiatkowski                        | et  | al. 2019. | Natural | Questions: | A     |
| ------------------------------- | --- | ------------------------------- | --- | --- | ------------ | --- | -------------------------------------- | --- | --------- | ------- | ---------- | ----- |
| DanRoth,andJonathanBerant.2021. |     |                                 |     |     | DidAristotle |     |                                        |     |           |         |            |       |
|                                 |     |                                 |     |     |              |     | benchmarkforquestionansweringresearch. |     |           |         |            | TACL, |
| usealaptop?                     |     | aquestionansweringbenchmarkwith |     |     |              |     |                                        |     |           |         |            |       |
7:453–466.
TACL,9:346–361.
implicitreasoningstrategies.
KentonLee,Ming-WeiChang,andKristinaToutanova.
TanyaGoyalandGregDurrett.2021. Annotatingand 2019. Latent retrieval for weakly supervised open
modeling fine-grained factuality in summarization. domainquestionanswering. InACL.
InNAACL.
KentonLee,KelvinGuu,LuhengHe,TimothyDozat,
KelvinGuu,KentonLee,ZoraTung,PanupongPasupat, and Hyung Won Chung. 2021. Neural data
and Ming-Wei Chang. 2020. REALM: Retrieval- augmentation via example extrapolation. ArXiv,
| augmentedlanguagemodelpre-training. |     |     |     |     |     | InICML. | abs/2102.01335. |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- | --- | --- | --- |

VladimirI.Levenshtein.1965. Binarycodescapableof Fabio Petroni, Tim Rocktäschel, Patrick Lewis, An-
correctingdeletions,insertions,andreversals. Soviet tonBakhtin,YuxiangWu,AlexanderH.Miller,and
physics.Doklady,10:707–710. SebastianRiedel.2019. Languagemodelsasknowl-
|     |     |     |     |     |     |     | edgebases? | InEMNLP. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- | --- | --- |
PatrickLewis,EthanPerez,AleksandaraPiktus,Fabio
AleksandraPiktus,FabioPetroni,VladimirKarpukhin,
Petroni,VladimirKarpukhin,NamanGoyal,Hein-
DmytroOkhonko,SamuelBroscheit,GautierIzacard,
| rich Kuttler, |     | Mike Lewis, | Wen | tau | Yih, Tim | Rock- |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
täschel, Sebastian Riedel, and Douwe Kiela. 2020. PatrickLewis,BarlasOuguz,EdouardGrave,Wen
Retrieval-augmented generation for knowledge- tauYih,andSebastianRiedel.2021. Thewebisyour
intensiveNLPtasks. InNeurIPS. oyster-knowledge-intensivenlpagainstaverylarge
|     |     |     |     |     |     |     | webcorpus. | ArXiv,abs/2112.09924. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | --- | --- | --- | --- |
RobertLLoganIV,AlexandrePassos,SameerSingh,
ColinRaffel,NoamM.Shazeer,AdamRoberts,Kather-
| andMing-WeiChang.2022.            |     |     |     | FRUIT:Faithfullyre- |          |     |                                |                |     |         |              |     |       |
| --------------------------------- | --- | --- | --- | ------------------- | -------- | --- | ------------------------------ | -------------- | --- | ------- | ------------ | --- | ----- |
|                                   |     |     |     |                     |          |     | ine Lee,                       | Sharan Narang, |     | Michael | Matena,      |     | Yanqi |
| flectingupdatedinformationintext. |     |     |     |                     | InNAACL. |     |                                |                |     |         |              |     |       |
|                                   |     |     |     |                     |          |     | Zhou,WeiLi,andPeterJ.Liu.2020. |                |     |         | Exploringthe |     |       |
limitsoftransferlearningwithaunifiedtext-to-text
| Shayne             | Longpre, | Kartik       | Kumar | Perisetla, |           | Anthony |                 |          |           |     |          |      |       |
| ------------------ | -------- | ------------ | ----- | ---------- | --------- | ------- | --------------- | -------- | --------- | --- | -------- | ---- | ----- |
|                    |          |              |       |            |           |         | transformer.    | JMLR,21. |           |     |          |      |       |
| Chen,              | Nikhil   | Ramesh,      | Chris | DuBois,    | and       | Sameer  |                 |          |           |     |          |      |       |
| Singh.             | 2021.    | Entity-based |       | knowledge  | conflicts | in      |                 |          |           |     |          |      |       |
|                    |          |              |       |            |           |         | Hannah Rashkin, | Vitaly   | Nikolaev, |     | Matthew  |      | Lamm, |
| questionanswering. |          | InEMNLP.     |       |            |           |         |                 |          |           |     |          |      |       |
|                    |          |              |       |            |           |         | Lora Aroyo,     | Michael  | Collins,  |     | Dipanjan | Das, | Slav  |
Petrov,GauravSinghTomar,IuliaTurc,andDavid
| Joshua Maynez, |     | Shashi | Narayan, | Bernd | Bohnet, | and |               |                                   |     |     |     |     |     |
| -------------- | --- | ------ | -------- | ----- | ------- | --- | ------------- | --------------------------------- | --- | --- | --- | --- | --- |
|                |     |        |          |       |         |     | Reitter.2021. | Measuringattributioninnaturallan- |     |     |     |     |     |
RyanT.McDonald.2020. Onfaithfulnessandfactu- guagegenerationmodels. ArXiv,abs/2112.12870.
| alityinabstractivesummarization. |     |     |     |     | InACL. |     |               |       |         |     |      |             |     |
| -------------------------------- | --- | --- | --- | --- | ------ | --- | ------------- | ----- | ------- | --- | ---- | ----------- | --- |
|                                  |     |     |     |     |        |     | Adam Roberts, | Colin | Raffel, | and | Noam | M. Shazeer. |     |
Jacob Menick, Maja Trebacz, Vladimir Mikulik, 2020. Howmuchknowledgecanyoupackintothe
| John | Aslanides, | Francis  | Song,  | Martin | Chadwick, |           |                             |     |     |     |          |     |     |
| ---- | ---------- | -------- | ------ | ------ | --------- | --------- | --------------------------- | --- | --- | --- | -------- | --- | --- |
|      |            |          |        |        |           |           | parametersofalanguagemodel? |     |     |     | InEMNLP. |     |     |
| Mia  | Glaese,    | Susannah | Young, |        | Lucy      | Campbell- |                             |     |     |     |          |     |     |
Gillingham,GeoffreyIrving,andNathanMcAleese. TimoSchick,JaneDwivedi-Yu,ZhengbaoJiang,Fabio
2022. Teachinglanguagemodelstosupportanswers Petroni,PatrickLewis,GautierIzacard,QingfeiYou,
withverifiedquotes. ArXiv,abs/2203.11147. ChristoforosNalmpantis,EdouardGrave,andSebas-
|     |     |     |     |     |     |     | tianRiedel.2022. |     | PEER:Acollaborativelanguage |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------------- | --- | --- | --- | --- |
Reiichiro Nakano, Jacob Hilton, S. Arun Balaji, Jeff model. ArXiv,abs/2208.11663.
| Wu, | Long Ouyang, |     | Christina | Kim, | Christopher |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
TalSchuster,AdamFisch,andReginaBarzilay.2021.
| Hesse, | Shantanu | Jain, | Vineet | Kosaraju, |     | William |     |     |     |     |     |     |     |
| ------ | -------- | ----- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
GetyourvitaminC!robustfactverificationwithcon-
| Saunders, | Xu  | Jiang, | Karl Cobbe, |     | Tyna | Eloundou, |     |     |     |     |     |     |     |
| --------- | --- | ------ | ----------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
GretchenKrueger, KevinButton, MatthewKnight, trastiveevidence. InNAACL.
| Benjamin | Chess, | and | John | Schulman. | 2021. | We- |     |     |     |     |     |     |     |
| -------- | ------ | --- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
DarshJ.Shah,TalSchuster,andReginaBarzilay.2020.
bGPT:Browser-assistedquestion-answeringwithhu-
|              |     |                       |     |     |     |     | Automatic | fact-guided | sentence |     | modification. |     | In  |
| ------------ | --- | --------------------- | --- | --- | --- | --- | --------- | ----------- | -------- | --- | ------------- | --- | --- |
| manfeedback. |     | ArXiv,abs/2112.09332. |     |     |     |     |           |             |          |     |               |     |     |
AAAI.
| Shashi Narayan, |     | Joshua | Maynez, | Reinald |     | Kim Am- |               |             |     |        |     |          |     |
| --------------- | --- | ------ | ------- | ------- | --- | ------- | ------------- | ----------- | --- | ------ | --- | -------- | --- |
|                 |     |        |         |         |     |         | Richard Shin, | Christopher |     | H Lin, | Sam | Thomson, |     |
playo,KuzmanGanchev,AnnieLouis,FantineHuot,
|     |     |     |     |     |     |     | Charles | Chen, Subhro | Roy, | Emmanouil |     | Antonios |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ---- | --------- | --- | -------- | --- |
Dipanjan Das, and Mirella Lapata. 2022. Condi- Platanios,AdamPauls,DanKlein,JasonEisner,and
tionalgenerationwithaquestion-answeringblueprint. BenjaminVanDurme.2021. Constrainedlanguage
ArXiv,abs/2207.00397. modelsyieldfew-shotsemanticparsers. InEMNLP.
TriNguyen,MirRosenberg,XiaSong,JianfengGao, RomalThoppilanetal.2022. LaMDA:Languagemod-
Saurabh Tiwary, Rangan Majumder, and Li Deng. elsfordialogapplications. ArXiv,abs/2201.08239.
| 2016.                        | MS MARCO: |     | A human | generated    |     | machine |                                    |     |     |     |     |           |     |
| ---------------------------- | --------- | --- | ------- | ------------ | --- | ------- | ---------------------------------- | --- | --- | --- | --- | --------- | --- |
|                              |           |     |         |              |     |         | JamesThorneandAndreasVlachos.2021. |     |     |     |     | Evidence- |     |
| readingcomprehensiondataset. |           |     |         | InCoCo@NIPS. |     |         |                                    |     |     |     |     |           |     |
InACL.
basedfactualerrorcorrection.
| Jianmo | Ni, Chen  | Qu,     | Jing Lu, | Zhuyun |         | Dai, Gus- |                     |     |         |          |         |          |       |
| ------ | --------- | ------- | -------- | ------ | ------- | --------- | ------------------- | --- | ------- | -------- | ------- | -------- | ----- |
|        |           |         |          |        |         |           | James Thorne,       |     | Andreas | Vlachos, |         | Christos |       |
| tavo   | Hernández | Ábrego, | Ji       | Ma,    | Vincent | Zhao,     |                     |     |         |          |         |          |       |
|        |           |         |          |        |         |           | Christodoulopoulos, |     | and     | Arpit    | Mittal. |          | 2018. |
YiLuan,KeithB.Hall,Ming-WeiChang,andYinfei
FEVER:alarge-scaledatasetforfactextractionand
| Yang.2021.  |                       | Largedualencodersaregeneralizable |     |     |     |     |               |          |          |     |       |           |     |
| ----------- | --------------------- | --------------------------------- | --- | --- | --- | --- | ------------- | -------- | -------- | --- | ----- | --------- | --- |
|             |                       |                                   |     |     |     |     | verification. | InNAACL. |          |     |       |           |     |
| retrievers. | ArXiv,abs/2112.07899. |                                   |     |     |     |     |               |          |          |     |       |           |     |
|             |                       |                                   |     |     |     |     | David Wadden, | Kyle     | Lo, Lucy | Lu  | Wang, | Shanchuan |     |
MaxwellNye,AndersJohanAndreassen,GuyGur-Ari,
Lin,MadeleinevanZuylen,ArmanCohan,andHan-
Henryk Michalewski, Jacob Austin, David Bieber, naneh Hajishirzi. 2020. Fact or fiction: Verifying
David Dohan, Aitor Lewkowycz, Maarten Bosma, scientificclaims. InEMNLP.
| David | Luan, | Charles | Sutton, | and Augustus |     | Odena. |     |     |     |     |     |     |     |
| ----- | ----- | ------- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
2021. Show your work: Scratchpads for interme- AlexWang, KyunghyunCho, andMikeLewis.2020.
diate computation with language models. ArXiv, Askingandansweringquestionstoevaluatethefac-
| abs/2112.00114. |     |     |     |     |     |     | tualconsistencyofsummaries. |     |     |     | InACL. |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------ | --- | --- |

WilliamYangWang.2017. “Liar,liarpantsonfire”: A datasets. Wewillreleasethisopen-sourceversion
newbenchmarkdatasetforfakenewsdetection. In ofRARRthatusesGPT-3asthebackbone.
ACL.
|     |     |     |     |     |     |     | Results | on GPT-3 passages |     | Table | 5   | shows au- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ----- | --- | --------- |
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
tomatedevaluationresultsonpassagesgenerated
| Bosma, | Ed Chi, | Quoc | Le, and | Denny | Zhou. | 2022. |          |                                   |     |     |     |     |
| ------ | ------- | ---- | ------- | ----- | ----- | ----- | -------- | --------------------------------- | --- | --- | --- | --- |
|        |         |      |         |       |       |       | byGPT-3. | Theresultsfollowthesametrendasthe |     |     |     |     |
Chainofthoughtpromptingelicitsreasoninginlarge
languagemodels. ArXiv,abs/2201.11903. resultsonPaLMandLaMDApassages.
Adina Williams, Nikita Nangia, and Samuel R. Bow- Challengingdomains Wereportresultsontasks
| man. | 2018. | A broad-coverage |     | challenge |     | corpus |     |     |     |     |     |     |
| ---- | ----- | ---------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
whereattributionwasparticularlyhard,andsignifi-
| for sentence |     | understanding | through |     | inference. | In  |     |     |     |     |     |     |
| ------------ | --- | ------------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
cantfutureworkisneeded.
NAACL.
Weconsiderednewsarticlesummariesproduced
Jingyi Zhang, Masao Utiyama, Eiichiro Sumita, Gra- bysummarizationmodelsfromSummEval(Fabbri
hamNeubig,andSatoshiNakamura.2018. Guiding et al., 2021) (e.g., “John Doe was left homeless
neuralmachinetranslationwithretrievedtranslation
whenthestormshitStatenIsland,NewYork...”).
| pieces. | InNAACL. |     |     |     |     |     |                          |     |     |                     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------- | --- | --- |
|         |          |     |     |     |     |     | ResultsareshowninTable6. |     |     | First,wenotethatthe |     |     |
Yuan Zhang, Jason Baldridge, and Luheng He. 2019. before-editauto-AISscoresforallmodelsarelow.
PAWS:Paraphraseadversariesfromwordscrambling. Thesenewsarticlesummariesareoftenaboutless
InNAACL.
|     |     |     |     |     |     |     | widely  | known people    | and     | events, | which            | is chal- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ------- | ------- | ---------------- | -------- |
|     |     |     |     |     |     |     | lenging | for retrievers, | leading | to      | low attribution. |          |
A Additionalexperimentsandanalysis
Forexample,ourquerygeneratormayask“where
Model variance The main experiments in Sec- doesJohnDoelive”butgetresultsforadifferent
tion5arebasedonasinglerun. Weranautomated JohnDoe. EFECandLaMDAalsofacethisissue,
evaluationon3randomrunsofRARR,usingPaLM
|     |     |     |     |     |     |     | but instead | trade preservation |     | for | attribution | and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | --- | --- | ----------- | --- |
outputsonNQasinputpassages. Thestandardde- rewritethetexttoadifferenttopic. Thisresultsug-
viationsofAttr ,Pres ,andF1 are1.2,0.5, geststhatusingwebsearchwithstandardquestion
|     |     | auto | Lev | AP  |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and1.0respectively. generationmethodsmayfailtocaptureimportant
contextfromtheinput,andisnotsufficientforthe
| Impact | of the | retriever | choice | We  | tried | using |     |     |     |     |     |     |
| ------ | ------ | --------- | ------ | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
attributiontask.
| Microsoft | Bing | in place | of Google |     | Search, | with |     |     |     |     |     |     |
| --------- | ---- | -------- | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
Wealsoconsideredlong-formexplanationsgen-
nearidenticalresults(<1%difference).
|        |          |       |      |            |     |     | erated by    | PaLM for | the ELI5 | dataset   | (Fan | et al., |
| ------ | -------- | ----- | ---- | ---------- | --- | --- | ------------ | -------- | -------- | --------- | ---- | ------- |
|        |          |       |      |            |     |     | 2019) (Table | 6). ELI5 | was      | collected | from | online  |
| Impact | of model | scale | Many | components |     | in  |              |          |          |           |      |         |
RARRworkbyfew-shotpromptingPaLM,alarge forums,somanyanswerstendtohavesubjective
540BparameterLM.ToassessthebenefitofLM opinionsinsteadofspecificentitiesandfacts(e.g.,
|          |             |      |      |      |           |     | “Howdoourbrainsinterpretscarymusic? |     |     |     |     | Tome, |
| -------- | ----------- | ---- | ---- | ---- | --------- | --- | ----------------------------------- | --- | --- | --- | --- | ----- |
| scaling, | we replaced | PaLM | 540B | with | a smaller |     |                                     |     |     |     |     |       |
scarymusicoftensoundsalittlebitlikeaperson
| 62B parameter |     | PaLM. | As shown | in  | Table | 4, we |     |     |     |     |     |     |
| ------------- | --- | ----- | -------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
foundthat540Boutperforms62Bbyalargemar- ...”),andarethusdifficulttoattribute. Sometimes
gin,suggestingthatRARRcouldpotentiallyfurther the whole output is based on a false premise and
|                             |     |     |     |               |     |     | needs to | be completely | rewritten, |     | in which | case |
| --------------------------- | --- | --- | --- | ------------- | --- | --- | -------- | ------------- | ---------- | --- | -------- | ---- |
| improvewithevenmorescaling. |     |     |     | Wealsoexperi- |     |     |          |               |            |     |          |      |
mentedwithkeepingtheeditorstageat540Bwhile RARRcannotsatisfactorilyeditduetoourrevision
shrinkingthequerygenerationstageto64B—this threshold(Section3.2).
|         |              |       |             |     |       |      | Finally, | we considered |     | technical | explanations |     |
| ------- | ------------ | ----- | ----------- | --- | ----- | ---- | -------- | ------------- | --- | --------- | ------------ | --- |
| yielded | a relatively | small | performance |     | drop, | sug- |          |               |     |           |              |     |
gesting that model scaling is more important for toquestionsfromtheMMLUdataset(Hendrycks
| theeditor. |     |     |     |     |     |     | et al., 2021) | which | covers | diverse | subjects | from |
| ---------- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------ | ------- | -------- | ---- |
socialscience,humanities,STEM,andothers.4
An
Impactofmodeltype Few-shotpromptinghas exampleinputlookslike “Everytimeyouremove
| proven | to be | effective | for many | recent | large | lan- |     |     |     |     |     |     |
| ------ | ----- | --------- | -------- | ------ | ----- | ---- | --- | --- | --- | --- | --- | --- |
anedgefromacompletegraph,youdivideitinto
| guagemodels. |     | Wetryreplacingthequerygenera- |     |     |     |     |                         |     |     |                   |     |     |
| ------------ | --- | ----------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | ----------------- | --- | --- |
|              |     |                               |     |     |     |     | twoconnectedcomponents. |     |     | So,acompletegraph |     |     |
tionmodel,agreementmodel,andeditmodelwith with 13 vertices must have 12 connected compo-
| GPT-3                                | text-davinci-003. |     | The | few-shot | prompts |     |         |                   |     |          |         |     |
| ------------------------------------ | ----------------- | --- | --- | -------- | ------- | --- | ------- | ----------------- | --- | -------- | ------- | --- |
|                                      |                   |     |     |          |         |     | nents.” | Results are shown |     | in Table | 7. RARR | im- |
| wereslightlytunedtofittheGPT-3model. |                   |     |     |          | Table4  |     |         |                   |     |          |         |     |
4MMLUhasquestionsfrom57subjects;wetook10ran-
| shows the | results, | which | are | slightly | better | than |     |     |     |     |     |     |
| --------- | -------- | ----- | --- | -------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
domquestionfromeachtopicandgeneratedanswerexplana-
RARRimplementedwithPaLM540Bonallthree
tionsbypromptingPALM540B.

PaLMoutputsonNQ PaLMoutputsonSQA LaMDAoutputsonQReCC
Model Attr Pres F1 Attr Pres F1 Attr Pres F1
auto Lev AP auto Lev AP auto Lev AP
FullRARR 45.6→54.9 89.6 68.1 37.6→45.1 89.9 60.0 18.8→29.4 80.2 43.1
qgen62B,editor540B 45.9→54.6 87.8 67.4 37.0→40.5 90.0 55.9 15.8→28.4 76.1 41.4
qgen62B,editor62B 45.9→49.9 91.0 64.4 37.0→38.3 93.0 54.2 15.8→21.9 71.6 33.5
GPT-3 44.3→55.0 90.6 68.5 38.6→46.6 89.3 61.2 18.3→28.6 89.8 43.4
Table 4: Additional ablation results. We report the automatic metrics: Attr , Pres , and harmonic mean
auto Lev
betweenthetwo(F1 ). Weshowauto-AISscoresbothbeforeandafterediting(before→edit),withrespecttothe
AP
attributionreportAproducedbythemodel.
GPT-3outputsonNQ GPT-3outputsonSQA GPT-3outputsonQReCC
Model Attr Pres F1 Attr Pres F1 Attr Pres F1
auto Lev AP auto Lev AP auto Lev AP
EFEC 48.3→66.8 41.5 51.2 32.6→50.6 29.4 37.2 26.4→53.1 39.0 44.9
LaMDA 36.2→61.1 45.9 52.4 22.3→27.3 43.3 33.5 19.0→33.9 28.3 30.8
PaLMRARR 48.3→57.2 89.6 69.8 32.6→36.3 91.6 52.0 26.4→31.1 87.7 45.9
GPT-3RARR 48.0→59.3 91.8 72.0 34.7→37.0 91.8 52.8 23.2→25.3 89.7 39.5
Table5: ResultsonpassagesfromGPT-3. Wereporttheautomaticmetrics: Attr ,Pres ,andharmonicmean
auto Lev
betweenthetwo(F1 ). Weshowauto-AISscoresbothbeforeandafterediting(before→edit),withrespecttothe
AP
attributionreportAproducedbythemodel. TheresultsshowsimilartrendsastheresultsonpassagesfromPaLM
andLaMDAinTable1.
Model Attr Pres F1 (Morerecentmodelsgavesimilarresults.) While
auto Lev AP
each sentence may contain multiple claims that
SummEval
EFEC 17.9→34.6 20.9 26.0 couldbeattributedindependently,thereiscurrently
LaMDA 10.3→28.8 28.1 28.4
nolinguisticconsensusonwhatconstitutesaclaim.
RARR 18.3→16.9 92.9 28.6
Insteadofdependingonaparticulardefinitionof
ELI5
claims,weusesentencesasclaimsforsimplicity
EFEC 18.2→41.2 17.2 24.2
LaMDA 19.9→40.1 31.2 35.1 andreproducibility. Thesamesegmentationisalso
RARR 18.5→18.9 97.2 31.7 usedforhumanevaluation.
Table6: ResultsonELI5andSummEval. Decontextualization We decontextualize each
sentenceinthetextpassagebeforecomputingthe
RARR attribution score. We use the model from Choi
MMLUCategory Attr Pres F1
auto Lev AP et al. (2021), which is a T5 model fine-tuned to
Humanities 26.6→29.6 6.6 45.0
map the input “[HEAD] [SEP] context and pas-
SocialSciences 35.5→40.7 7.6 56.5
STEM 37.8→41.5 7.2 57.4 sage [start] sentence [end]” to the output
Other 36.9→41.7 7.1 57.6 “[OPCODE] decontextualizedsentence”,wherethe
OPCODE can be “done” (success), “un” (unneces-
Table7: RARRresultsonMMLU.
sary),or“imp”(impossible). Wefeedthepassage’s
context(questionsforNQandSQA;dialogcontext
for QRECC) along with the passage itself to the
proves attribution of the explanations on all four
input. Weusebeamsearchwithbeamsize8and
categories of MMLU, although the increases are
discardanyresultwhosenumberoftokensdiffer
relativelysmall. WealsofoundthatRARR’sper-
bymorethan4.
formance is low on examples with mathematical
reasoning,asthesearebeyondthecapabilityofthe
NLI model We obtained a newer version of
editmodelwithourcurrentprompt.
the end-to-end NLI model from the authors of
Honovich et al. (2022), which was trained on
B Detailsonautomatedevaluation
MNLI, SNLI, FEVER, PAWS, SciTail and Vita-
Sentence splitting When computing the attri- minC(Williamsetal.,2018;Bowmanetal.,2015;
bution score, we use spaCy en_core_web_sm Thorneetal.,2018;Zhangetal.,2019;Khotetal.,
v3.0.0a1tosegmentthetextpassageintosentences. 2018; Schuster et al., 2021). The model is a T5

|     |     |     |     |     |     | responsesduringthepilotannotationruns. |     |     |     |     | Wehad |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ----- |
3annotatorsrateeachexampleinthepilotphase
|     |     |     |     |     |     | to measure | inter-annotator |     | agreement, | and | had a |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ---------- | --- | ----- |
singleraterannotateeachexampleafterwards.
|     |     |     |     |     |     | C.1 Instructions: |          | Overview      |                 |         |         |
| --- | --- | --- | --- | --- | --- | ----------------- | -------- | ------------- | --------------- | ------- | ------- |
|     |     |     |     |     |     | In this           | task you | will evaluate | the             | quality | of text |
|     |     |     |     |     |     | generated         | by a     | system        | (the “passage”) | based   | on      |
howwellitrepresentsinformationfrommultiple
piecesof“evidence”.
Wewillbeusingtwocategoriestoevaluatethe
|           |                                            |     |     |     |     | quality | of the | passage: | Attribution | and | Intent |
| --------- | ------------------------------------------ | --- | --- | --- | --- | ------- | ------ | -------- | ----------- | --- | ------ |
| Figure10: | Violinplotillustratingthestrongcorrelation |     |     |     |     |         |        |          |             |     |        |
between human AIS and auto-AIS labels on our NQ Similarity. You will evaluate these categories in
benchmark. Pearson correlation is 0.74 (N=450). y- succession. In some tasks, you will only evalu-
axisisauto-AISscore,thetwoviolinscorrespondtoa ateAttribution. Thetaskinterfacewillguideyou
| humanlabelof0or1. |     |     |     |     |     | throughtheflow;youcanalsoseetheoveralltask |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
flowinthediagrambelow.
modelfine-tunedtomaptheinput“premise: evi- Note: Thepassagemayappearveryfluentand
|                   |        |                           |     |              |     | well-formed,                          | but | still contain             | slight | inaccuracies |     |
| ----------------- | ------ | ------------------------- | --- | ------------ | --- | ------------------------------------- | --- | ------------------------- | ------ | ------------ | --- |
| dence hypothesis: |        | claimsentence”toeither“1” |     |              |     |                                       |     |                           |        |              |     |
|                   |        |                           |     |              |     | thatarenoteasytodiscernatfirstglance. |     |                           |        | Payclose     |     |
| (entailed)        | or “0” | (not entailed).           |     | As suggested | by  |                                       |     |                           |        |              |     |
|                   |        |                           |     |              |     | attentiontothetext.                   |     | Readitcarefullyasyouwould |        |              |     |
theauthors,weusetheprobabilityofproducing“1”
whenproofreading.
astheentailmentscore.
|           |       |     |           |            |     | C.2 Instructions: |     | Attribution |     |     |     |
| --------- | ----- | --- | --------- | ---------- | --- | ----------------- | --- | ----------- | --- | --- | --- |
| Comparing | human | and | automated | evaluation |     |                   |     |             |     |     |     |
Weconductedcorrelationstudiesbetweenhuman In this step, you will evaluate how much of the
and automatic metrics and found strong Pearson passage is attributable to one or more pieces of
correlation(attribution=0.74;preservation=0.62). evidence(Figure11).
We visualize the correlation between human and Intheinterface,thepassageoftextandthecon-
automated attribution scores on NQ and SQA in textinwhichitwasgeneratedisshownontheleft,
Figure 10. We found that the AIS scores from andeach pieceofevidenceis shownon theright.
human correlate well with auto-AIS scores, with Youwilluseallthree(context,passage,evidence)
somebiasfornon-attributedsentencestobejudged toanswerthefollowingquestionforeachsentence
asattributedbyauto-AIS. inthepassage: Isalloftheinformationprovidedby
thissentencefullysupportedbyatleastonepiece
| C Detailsonhumanevaluation |         |     |            |     |          | ofevidence? |     |             |          |     |        |
| -------------------------- | ------- | --- | ---------- | --- | -------- | ----------- | --- | ----------- | -------- | --- | ------ |
| To end-goal                | of RARR | is  | to improve | the | attribu- |             |     |             |          |     |        |
|                            |         |     |            |     |          | Determining | the | information | provided |     | by the |
tion of generation models through post-editing sentence. Threepointsarekeywhendetermining
while preserving the original intent. Attribution informationprovidedbythesentence:
andpreservationarebothsubjectivepropertiesthat
may change with even small edits. In the main 1. The context and the other sentences of the
passageareoftencriticalinunderstandingthe
paper,wepresenttwoautomaticmetricstoconve-
nientlygaugetheseproperties,butrelyonahuman informationprovidedbythesentence.
| evaluation | as the | gold standard. |     | In this | section, |     |     |     |     |     |     |
| ---------- | ------ | -------------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- |
2. Thecontextshouldonlybeusedtounderstand
wedescribehowweconductedthehumanevalua-
theinformationprovidedbythesentence.
tionandwhatinstructionsandexamplesannotators
wereprovided.
|     |     |     |     |     |     | 3. The | evidence | should | be completely |     | ignored |
| --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | ------------- | --- | ------- |
forthisstep.
| Rater recruitment |     | and | training | We  | engaged |     |     |     |     |     |     |
| ----------------- | --- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
withavendorsupplieroffull-timecrowdworkers
Considerthefollowingexample:
| to recruit | human | annotators | for | our task. | Anno- |     |     |     |     |     |     |
| ---------- | ----- | ---------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
tators were asked to review the instructions be- Context: who plays doug williams in
low and were provided direct feedback on their daysofourlives

Figure11: Screenshotofinterfacetoannotate attributionat thesentencelevel. annotatorswereaskedtomark
sentencesasbeingfullyattributableornotfullyattributablebyclickingeachsentence,andratingeachpieceof
evidenceasbeingusefulornotinhelpingdetermineattributionofthepassage. Annotatorswerealsopresentedwith
thecontextofthegeneration.
Figure12: Screenshotofthepreservationinterface. Annotatorsareaskedtoreadcomparetwopassagesandrate
howsimilartheintentconveyedbythetwopassagesis.

Passage: In the American daytime Ingeneral,useyourbestjudgmenttodetermine
drama Days of Our Lives, Doug the information provided by the passage. If the
Williams and Julie Williams are por- passageishardtounderstandandyouareunsure
trayedbyBillHayesandSusanSeaforth whattheintendedmeaningofthepassageis,mark
| Hayes. |     |     |     |     |     | thesentencesasnotattributedandenteracomment |     |     |              |      |     |
| ------ | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | ------------ | ---- | --- |
|        |     |     |     |     |     | with an explanation.                        |     | As  | one example, | take | the |
following:
| In the | above | example, | the meaning |     | of the pas- |     |     |     |     |     |     |
| ------ | ----- | -------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
sage is clear even without seeing the query. But Context: howmanyNBAchampionships
| consideranotherexample: |                       |       |                |          |     | didMichaelJordanwin?                        |                         |                        |     |     |     |
| ----------------------- | --------------------- | ----- | -------------- | -------- | --- | ------------------------------------------- | ----------------------- | ---------------------- | --- | --- | --- |
|                         |                       |       |                |          |     | Passage:                                    | itisthebestteamintheNBA |                        |     |     |     |
| Context:                | who                   | plays | doug           | williams | in  |                                             |                         |                        |     |     |     |
| daysofourlives          |                       |       |                |          |     | Determiningiftheinformationaccuratelyrepre- |                         |                        |     |     |     |
| Passage:                | heisplayedbyBillHayes |       |                |          |     |                                             |                         |                        |     |     |     |
|                         |                       |       |                |          |     | sentstheevidence.                           |                         | Twopointsarekeywhende- |     |     |     |
| Passage(interpreted):   |                       |       | DougWilliamsis |          |     |                                             |                         |                        |     |     |     |
terminingwhethertheinformationaccuratelyrep-
playedbyBillHayesindaysofourlives resentstheevidence: Wheninterpretingapieceof
evidence,useonlythetitleandtextofthatspecific
| In this        | case the  | pronoun    | “he”       | depends     | on the  |                                              |     |                          |     |     |     |
| -------------- | --------- | ---------- | ---------- | ----------- | ------- | -------------------------------------------- | --- | ------------------------ | --- | --- | --- |
|                |           |            |            |             |         | evidence. Completelyignorethecontext,passage |     |                          |     |     |     |
| context,       | but it is | clear that | the        | intended    | meaning |                                              |     |                          |     |     |     |
|                |           |            |            |             |         | andallotherevidence.                         |     | Checkalltheinformationin |     |     |     |
| of the passage |           | can be     | reasonably | interpreted | as      |                                              |     |                          |     |     |     |
|                |           |            |            |             |         | asentence. Ifonlysomeinformationissupported  |     |                          |     |     |     |
“DougWilliamsisplayedbyBillHayesindaysof
|            |                                     |     |     |     |     | by the evidence, | mark | the | sentence | as not | fully |
| ---------- | ----------------------------------- | --- | --- | --- | --- | ---------------- | ---- | --- | -------- | ------ | ----- |
| ourlives”. | Thisinterpretationisthe“information |     |     |     |     |                  |      |     |          |        |       |
attributable.
providedbythepassage”.
Considerthefollowingexample:
| Pronounssuchashe/she/it/theyetc. |     |     |     |     | areonecase |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
wherecontextisneededtofigureouttheintended
|         |        |        |           |        |         | Context: | whendidrebamcentirerecord |     |     |     |     |
| ------- | ------ | ------ | --------- | ------ | ------- | -------- | ------------------------- | --- | --- | --- | --- |
| meaning | of the | system | response. | Here’s | another |          |                           |     |     |     |     |
backtogod
example(givenwithparaphrasesoftheinformation
|     |     |     |     |     |     | Passage: | Back | to God | was released | by  |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ------------ | --- | --- |
highlightedbelow):
McEntirein2017.
Context: whenisthelasttimetheuslost Evidence: “BacktoGod”isasongper-
formedbyAmericansinger,RebaMcEn-
basketballattheolympics
|          |                            |           |          |     |        | tire. It was | released |             | as the | second sin- |     |
| -------- | -------------------------- | --------- | -------- | --- | ------ | ------------ | -------- | ----------- | ------ | ----------- | --- |
| Passage: | Thelasttimetheylostwasin   |           |          |     |        |              |          |             |        |             |     |
|          |                            |           |          |     |        | gle from     | her      | 2017 album, | Sing   | it Now:     |     |
| 2004,    | when                       | Argentina | defeated |     | the US |              |          |             |        |             |     |
|          |                            |           |          |     |        | Songs of     | Faith    | & Hope,     | on     | January 20, |     |
| 89–79.   | Mostrecently,theywongoldin |           |          |     |        |              |          |             |        |             |     |
2017.
2016.
| Passage | (interpreted): |     | The | last | time |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
Intheaboveexample,itisreasonabletoconclude
| the | United | States | lost basketball |     | at the |                   |          |     |         |             |     |
| --- | ------ | ------ | --------------- | --- | ------ | ----------------- | -------- | --- | ------- | ----------- | --- |
|     |        |        |                 |     |        | that the evidence | supports |     | all the | information | in  |
Olympicswasin2004.
thepassage,andwecanmarkthepassageasbeing
The context should only be used to determine fullyattributable. Butconsideranotherexample:
theinformationprovidedbythepassage;attimes,
|     |     |     |     |     |     | Context: | who | won | the womens | 2017 |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---------- | ---- | --- |
thepassagemaybeaboutaslightlydifferenttopic
ncaabasketballtournament
thanthecontext,forexample:
|     |     |     |     |     |     | Passage: | South | Carolina | Gamecocks |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | --------- | --- | --- |
wonthe2017NCAAWomen’sDivision
| Context:             |     | the south | west | wind | blows |                        |     |     |     |     |     |
| -------------------- | --- | --------- | ---- | ---- | ----- | ---------------------- | --- | --- | --- | --- | --- |
| acrossnigeriabetween |     |           |      |      |       | IBasketballTournament. |     |     |     |     |     |
Passage: The Harmattan is a dry and Evidence: The South Carolina Game-
cocksdefeatedtheMississippiStateBull-
dustynortheasterlytradewindthatblows
across West Africa from December to dogs,67–55,toclaimtheirfirst-everna-
| March. | Itisverydustybecauseitblows |     |     |     |     | tionalchampionship. |     |     |     |     |     |
| ------ | --------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
acrosstheSahara.
Inthiscase,whiletheevidencealsomentionsthe
Here, the passage talks about a northeasterly “SouthCarolinaGamecocks”,itisn’tclearthatthe
wind, while the context asks about a south-west nationalchampionshipbeingmentionedisindeed
wind,butthepassagecanbefullyunderstood. the 2017 NCAA Women’s Division I Basketball

Tournament. Thepassageshouldbemarkedasnot • Moreontheconceptof“accuraterepresen-
| attributable. |     |     |     |     |     | tation”. | Wetakeasinspirationthejournalist’s |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | -------- | ---------------------------------- | --- | --- | --- | --- |
Finally,whenthepassagecontainsmultiplesen- conceptionof“accuraterepresentation”. For
tences,evaluatewhethereachsentencecanbefully example,takethisexcerptonAccuracyinthe
|            |        |         |        |     |             | NPR | Ethics | Handbook: | “When |     | quoting or |
| ---------- | ------ | ------- | ------ | --- | ----------- | --- | ------ | --------- | ----- | --- | ---------- |
| attributed | to one | or more | pieces | of  | evidence—it |     |        |           |       |     |            |
ispossibleforonesentencetobeattributedwhile paraphrasinganyone... considerwhetherthe
anotherisnot. Forexample: sourcewouldagreewiththeinterpretation...”
Inotherwords,ifyouhadwrittenthesource
Context: who won the womens 2017 document,considerwhetheryouwouldview
ncaabasketballtournament thesystemresponseasanaccuraterepresenta-
Passage: South Carolina Gamecocks tionofinformationinthatsourcedocument.
wonthe2017NCAAWomen’sDivision
IBasketballTournament.Thefinalscore
|           |     |              |     |      |     | C.3 Instructions: |     | IntentSimilarity |     |      |         |
| --------- | --- | ------------ | --- | ---- | --- | ----------------- | --- | ---------------- | --- | ---- | ------- |
| is 67-55. | The | championship |     | game | was |                   |     |                  |     |      |         |
|           |     |              |     |      |     | In this step,     | you | will evaluate    | how | much | similar |
heldinDallas,Texas.
thepassageistoanotherpassage(Figure12).
| Evidence1: |     | TheSouthCarolinaGame- |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intheinterface,thepassageAandpassageBare
cocksdefeatedtheMississippiStateBull-
bothtextgeneratedbyasystem—giventhesame
dogs,67–55,toclaimtheirfirst-everna-
|     |     |     |     |     |     | context in | which | it was generated. |     | You | will use |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------------- | --- | --- | -------- |
tionalchampionship.
allthree(context,passageA,passageB)toanswer
| Evidence2: |      | The2017NCAAWomen’s |            |     |         |                       |            |                       |         |     |           |
| ---------- | ---- | ------------------ | ---------- | --- | ------- | --------------------- | ---------- | --------------------- | ------- | --- | --------- |
|            |      |                    |            |     |         | thefollowingquestion: |            | Howsimilaristheintent |         |     |           |
| Division   | I    | Basketball         | Tournament |     | was     |                       |            |                       |         |     |           |
|            |      |                    |            |     |         | expressed             | by Passage | A and                 | Passage |     | B? Please |
| played     | from | Friday,            | March      | 17  | to Sun- |                       |            |                       |         |     |           |
ignoreanydifferencesindetails.
| day, | April | 2, 2017, | with | the Final | Four |     |     |     |     |     |     |
| ---- | ----- | -------- | ---- | --------- | ---- | --- | --- | --- | --- | --- | --- |
Twopointsarekeywhendeterminingwhether
playedattheAmericanAirlinesCenter
thetwopassagesconveythesameintent:
inDallas,TexasonMarch31andApril
2.
1. Judgethesimilaritysolelybasedonthesimi-
larityinthetypeandquantityofinformation
The first two sentences cannot be attributed to providedbyeachpassage.
eitherevidenceforthesamereasonastheprevious
example,butthelastsentenceisfullysupportedby 2. Ignore any differences in factual details be-
| Evidence2andshouldbemarkedasattributed. |                              |     |     |     |     | tweenthetwopassages. |     |     |     |     |     |
| --------------------------------------- | ---------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
| Ingeneral,                              | youshoulduseyourbestjudgment |     |     |     |     |                      |     |     |     |     |     |
Considerthefollowingexamples:
indeterminingwhetheralloftheinformationpro-
| videdbythepassageis“anaccuraterepresentation |     |     |     |     |     | Context: |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
whopaysmedicalbillsingreat
ofinformationinatleastoneevidence”. SeeTable britainwheredoesthemoneycomefrom
| 8foradditionalexamples. |     |     |     |     |     | topaythesebills |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
Wegivethefollowingfinalnotesofguidance: Passage A: Britain’s National Health
|     |     |     |     |     |     | Service | (NHS) | is paid | for through |     | gen- |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | ----------- | --- | ---- |
• Markingevidenceasuseful. Whenreview- eraltaxationandnationalinsurance. In
ingeachpieceofevidence,markitasuseful
2017/18,theNHSbudgetwas£176.5bn.
ifithelpsyoujudgetheattributabilityofany PassageB:Britain’sNationalHealthSer-
sentence, and mark it not useful if not. In vice (NHS) is paid for through general
| the     | above | example | Evidence | 1      | is not useful |           |     |          |         |        |     |
| ------- | ----- | ------- | -------- | ------ | ------------- | --------- | --- | -------- | ------- | ------ | --- |
|         |       |         |          |        |               | taxation. | In  | 2017/18, | the NHS | budget |     |
| because | it    | didn’t  | contain  | enough | context to    |           |     |          |         |        |     |
was£118bn.
actually help you assess if the passage was Rating: Verysimilar.PassageAisabout
attributable,butEvidence2wasuseful. thesametopicasPassageB,withasim-
ilarlevelofdetailandstyleofpresenta-
• Contradictingevidence. Markasentenceas tion. Theymaydifferinfactualdetails.
beingattributedifanypieceofevidencesup-
portsit: iftwopiecesofevidencecontradict Theaboveexampleshouldberated“verysimilar”
eachother,butoneofthemsupportsthepas- becausebothpassagesincludeinformationabout
sage,markthesentenceasfullyattributable. (1)howtheNHSispaidfor,and(2)whatitsbudget

| Context+Passage |     |     |     | Evidences |     |     |     | Notes |     |     |     |
| --------------- | --- | --- | --- | --------- | --- | --- | --- | ----- | --- | --- | --- |
Context:whoplayedmorticiain 1/TheAddamsFamily(1973TVseries): TheAddams Whiletheevidencesupportsthe
theaddamsfamilytvshow FamilyisanAmericananimatedsitcomadaptationofthe show being aired in 1973, it
TheAddamsFamilyisanAmer- CharlesAddamscomic.Theserieswasproducedin1973 doesn’t specify the exact date
icananimatedsitcomTVseries. andwasrebroadcastthefollowingseason. (September24,1973).
It was first aired on NBC on 2/TheAddamsFamily(TVSeries1964–1966): When Similarly, while the evidence
The Addams Family went off the air in 1966, network mentions Carolyn Jones as be-
| September | 24, 1973. | Carolyn |     |     |     |     |     |     |     |     |     |
| --------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
executivesinchargeofchildren’sprogrammingforNBC ingavoiceactor,itdoesn’tsay
JonesplayedtheroleofMorti-
|     |     |     |     | broughtthembackin1973fortheirownSaturdayMorn- |     |     |     | sheplayedtheroleofMortica. |     |     |     |
| --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- |
cia.
ingcartoonshowfeaturingthevoicesofCarolynJones
fromtheoriginalseries.
Context: when will the la 1/SagradaFamília-Wikipedia:TheBasílicaiTempleEx- While Evidence 2 mentions
sagradafamiliabefinished piatoridelaSagradaFamíliaisachurchintheEixample Gaudi,itisn’tclearthisisaref-
The La Sagrada Familia is a districtofBarcelona,Catalonia,Spain,andiscurrently erencetoAntoniGaudiandfur-
largeRomanCatholicchurchin thelargestunfinishedRomanCatholicchurch. therdoesn’tsaythathedesigned
Barcelona.ItisdesignedbyAn- 2/FindOutSagradaFamilia’sExpectedFinishDate:Vis- thechurch.
itingthebreathtakingSagradaFamiliatodayalsomeans
| toni Gaudi. | It started | construc- |     |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
witnessingtheslowprogresstowardsthecompletionofthe
tionin1882,andtheconstruc-
project.SagradaFamiliaisnowexpectedtobecompleted
| tion is still | going | on. The | esti- |     |     |     |     |     |     |     |     |
| ------------- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
in2026,thecentenaryofGaudi’sdeath.It’sareasonable
mateddatetofinishis2026.
inferencethatLaSagradaFamiliaisthesameasSagrada
Familia,eventhoughthenamesdifferslightly.
|     |     |     |     | Table8: | Additionalexamplesforannotatingattribution. |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
in2017/18was,thoughtheydifferintheiractual ident of and (3a) who their vice-president is. In
answerstothesequestions. contrast,whilePassageBsharesinformationabout
|          |     |     |        |       |            | (1a), it also | includes | information | about    | (2b) | how   |
| -------- | --- | --- | ------ | ----- | ---------- | ------------- | -------- | ----------- | -------- | ---- | ----- |
| Context: |     | who | is the | owner | of reading |               |          |             |          |      |       |
|          |     |     |        |       |            | the Reading   | owner    | made their  | fortune, | (3b) | their |
footballclub
companypositionandhowlongtheyhelditforand
PassageA:Reading’sownerisYongge
(4b)whatthecompanyalsoowns.
| Dai.                           | YonggeDaiisalsothepresidentof |     |     |     |     |          |      |        |         |          |     |
| ------------------------------ | ----------------------------- | --- | --- | --- | --- | -------- | ---- | ------ | ------- | -------- | --- |
| ChinesecompanyDaiYonggeRealEs- |                               |     |     |     |     | Context: |      |        |         |          |     |
|                                |                               |     |     |     |     |          | what | is the | numbers | of total |     |
tate.Yongge’sson,DaiXiuLi,isRead- elected member of indian parliment in
| ing’svice-president. |     |           |     |       |        | presenttime                      |     |     |     |     |     |
| -------------------- | --- | --------- | --- | ----- | ------ | -------------------------------- | --- | --- | --- | --- | --- |
| Passage              |     | B:        |     |       |        |                                  |     |     |     |     |     |
|                      |     | Reading’s |     | owner | is Dai | PassageA:Thetotalnumberofelected |     |     |     |     |     |
Yongge. Yongge’sbrotherandsisterpair membersoftheLokSabhais543.
behind the Reading FC takeover—Dai PassageB:Thetotalnumberofelected
| YonggeandDaiXiuLi—hasmadetheir |     |     |     |     |     | membersoftheRajyaSabhais238. |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
fortunethroughamassivepropertyem- Rating: Not at all similar. Passage A is
pire. Mr Dai, has been the chairman of aboutasignificantlydifferenttopicthan
| Renhe | Commercial   |     |       | since 1999, | which      | PassageB. |     |     |     |     |     |
| ----- | ------------ | --- | ----- | ----------- | ---------- | --------- | --- | --- | --- | --- | --- |
| is an | organisation |     | owned | by          | his sister |           |     |     |     |     |     |
behind a vast network of underground Eventhoughthepassageslookverysimilar,the
aboveexampleshouldberated“notatallsimilar”
shoppingcentresinChina.
|         |                            |     |     |     |     | because | the two passages |     | are about | significantly |     |
| ------- | -------------------------- | --- | --- | --- | --- | ------- | ---------------- | --- | --------- | ------------- | --- |
| Rating: | Somewhatsimilar.PassageAis |     |     |     |     |         |                  |     |           |               |     |
about the same topic as Passage B, but different topics: “the Lok Sabha” vs “the Rajya
Sabha”.
differssubstantiallyinlevelofdetailor
| styleofpresentation. |     |     |     | Theymaydifferin |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
D Detailsonthemodel
factualdetails.
|     |     |     |     |     |     | Few-shot | prompting | with | LLMs | We  | imple- |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ---- | --- | ------ |
Theaboveexampleshouldberated“somewhat
|     |     |     |     |     |     | ment many | sub-tasks | within | RARR | using | few- |
| --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | ---- | ----- | ---- |
similar”becausebothpassagesarestillaboutthe
shotpromptingofLLMs(alsoknownasin-context
sametopic—Reading’sowner—butdiffersubstan-
learning(Brownetal.,2020))asfollows:
| tially in | the information |     | they | discuss: | Passage A |     |     |     |     |     |     |
| --------- | --------------- | --- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- |
includes information about (1a) who Reading’s 1. For each sub-task, we manually author
owner is, (2a) which company they are the pres- a small number of training examples:

(input ,output ) for j = 1,...,J, where
j j
J ranges between 5 and 10 and where both
theinputandoutputarestrings.
2. We form the following prompt: input ⋄
1
output ⊕input ⋄output ⊕...⊕input ⋄
1 2 2 J
output ⊕ new_input, where ⋄ denotes a
J
newline character and ⊕ denotes a double
newlinecharacter.
3. Toperforminferenceonanewinput,wecon-
dition the LLM on the prompt and sample
continuationsofthepromptupuntilthenext
doublenewlinecharacter.
AllofourpromptsareincludedinFigures13,14,
and 15. The contextual version used for QReCC
areinFigures16,17,and18.
Modelstatistics Weimplementedmostpartsof
RARRwiththePALMmodelwhichhas540Bpa-
rameters. WepromptedPALMwithoutanytrain-
ing or finetuning. We used a TPU v2-128 to run
inferencewithPALM.
Wemanuallywroteourpromptsbyeye-balling
quality on a dozen of examples from a separate
validationset. Wetuneourhyperparametersonthe
validation set as well. We used sampling temper-
ature 0.7 for all generation tasks. For each input
text, we sample 3 question generations, and for
eachquestionweretrieve5results. Foragreement
gateandediting,weonlysample1generation. We
reject an editing if the edit distance is more than
50charactersormorethanhalfoftheoriginaltext
length.
E Detailsonthedataset
AsexplainedinSection5.1,wegenerated150de-
velopmentand150testpassagesforeachofthe6
combinationsofdatasetandmodel: (NQ,PaLM),
(SQA,PaLM),(QReCC,LaMDA),(NQ,GPT-3),
(SQA,GPT-3),(QReCC,GPT-3). Figures19,20,
21,and22arethefew-shotpromptsusedtogener-
atethepassages.
Followingthecorrespondingdatasets,allgener-
atedpassagesareinEnglish. Theauthorshaveman-
uallylookedthroughmostofthedataandfoundno
personalidentifiers.

| [web] I will | check things | you said | and ask | questions. |
| ------------ | ------------ | -------- | ------- | ---------- |
1
2
3 (1) You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This
| is to prevent | a buildup | of mucus.   | It’s called | the nasal cycle. |
| ------------- | --------- | ----------- | ----------- | ---------------- |
| 4 To verify   | it,       |             |             |                  |
| a) I googled: | Does your | nose switch | between     | nostrils?        |
5
| 6 b) I googled: | How often     | does your | nostrils | switch? |
| --------------- | ------------- | --------- | -------- | ------- |
| 7 c) I googled: | Why does your | nostril   | switch?  |         |
| 8 d) I googled: | What is nasal | cycle?    |          |         |
9
10 (2) You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
| 11 To verify     | it,       |          |                   |                |
| ---------------- | --------- | -------- | ----------------- | -------------- |
| 12 a) I googled: | Where was | Stanford | Prison Experiment | was conducted? |
13
14 (3) You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency
| list. It      | is named after | Vaclav Havel | and       | Samih Hakimi. |
| ------------- | -------------- | ------------ | --------- | ------------- |
| 15 To verify  | it,            |              |           |               |
| a) I googled: | What does      | Havel-Hakimi | algorithm | do?           |
16
| 17 b) I googled: | Who are Havel-Hakimi |     | algorithm | named after? |
| ---------------- | -------------------- | --- | --------- | ------------ |
18
19 (4) You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
| Dirty Dancing. | The song | was produced | by Michael | Lloyd. |
| -------------- | -------- | ------------ | ---------- | ------ |
| To verify      | it,      |              |            |        |
20
| 21 a) I googled: | Who sings    | "Time of | My Life"?   |              |
| ---------------- | ------------ | -------- | ----------- | ------------ |
| 22 b) I googled: | Which film   | is "Time | of My Life" | from?        |
| 23 c) I googled: | Who produced | the song | "Time       | of My Life"? |
24
(5) You said: Kelvin Hopins was suspended from the Labor Party due to his membership in the Conservative Party.
25
| 26 To verify     | it,            |        |           |                   |
| ---------------- | -------------- | ------ | --------- | ----------------- |
| 27 a) I googled: | Why was Kelvin | Hopins | suspended | from Labor Party? |
28
29 (6) You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual
| discipline       | that has its       | roots in    | the 1800s. |                          |
| ---------------- | ------------------ | ----------- | ---------- | ------------------------ |
| 30 To verify     | it,                |             |            |                          |
| 31 a) I googled: | What philosophical |             | tradition  | is social work based on? |
| 32 b) I googled: | What year          | does social | work       | has its root in?         |
33
| (7) You said: | {text} |     |     |     |
| ------------- | ------ | --- | --- | --- |
34
| 35 To verify | it, |     |     |     |
| ------------ | --- | --- | --- | --- |
36 _____
Figure13: Few-shotpromptforquerygeneration. Toincreasediversityandcoverage,wesamplethemodelthree
timesandcombinetheresultinglistsofqueries.

| 1 [web] | I will check | some | things | you said. |     |     |     |     |
| ------- | ------------ | ---- | ------ | --------- | --- | --- | --- | --- |
2
3 (1) You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This
| is to        | prevent | a buildup | of mucus.     | It’s    | called the | nasal cycle. |     |     |
| ------------ | ------- | --------- | ------------- | ------- | ---------- | ------------ | --- | --- |
| 4 I checked: | How     | often do  | your nostrils | switch? |            |              |     |     |
5 I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus
contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every
| 2 hours,    | according | to  | a small | 2016 study  | published | in the journal  | PLOS One. |     |
| ----------- | --------- | --- | ------- | ----------- | --------- | --------------- | --------- | --- |
| Your nose’s | switching |     | time is | about every | 2 hours,  | not 45 minutes. |           |     |
6
| 7 This disagrees |     | with what | you said. |     |     |     |     |     |
| ---------------- | --- | --------- | --------- | --- | --- | --- | --- | --- |
8
9 (2) You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
| 10 I checked: | Who | published | the Little | House | books? |     |     |     |
| ------------- | --- | --------- | ---------- | ----- | ------ | --- | --- | --- |
I found this article: These are the books that started it all – the stories that captured the hearts and imaginations of
11
children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books
| remain         | a favorite | to this | day.           |     |                |     |     |     |
| -------------- | ---------- | ------- | -------------- | --- | -------------- | --- | --- | --- |
| 12 The Little  | House      | books   | were published | by  | HarperCollins. |     |     |     |
| 13 This agrees | with       | what    | you said.      |     |                |     |     |     |
14
15 (3) You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
| 16 I checked: | Where | was Stanford |     | Prison Experiment | conducted? |     |     |     |
| ------------- | ----- | ------------ | --- | ----------------- | ---------- | --- | --- | --- |
17 I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set
out to examine the psychological effects of authority and powerlessness in a prison environment.
| The Stanford | Prison | Experiment |     | was conducted | in Jordan | Hall. |     |     |
| ------------ | ------ | ---------- | --- | ------------- | --------- | ----- | --- | --- |
18
| 19 This agrees | with | what | you said. |     |     |     |     |     |
| -------------- | ---- | ---- | --------- | --- | --- | --- | --- | --- |
20
21 (4) You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual
| discipline    | that | has its    | roots | in the 1800s. |        |     |     |     |
| ------------- | ---- | ---------- | ----- | ------------- | ------ | --- | --- | --- |
| 22 I checked: | When | did social | work  | have its      | roots? |     |     |     |
23 I found this article: The Emergence and Growth of the Social work Profession<br><br> Social work’s roots were planted in
the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and
| settlement        | houses   | were      | established. |        |            |     |     |     |
| ----------------- | -------- | --------- | ------------ | ------ | ---------- | --- | --- | --- |
| 24 Social         | work has | its roots | in the       | 1880s, | not 1800s. |     |     |     |
| 25 This disagrees |          | with what | you said.    |        |            |     |     |     |
26
(5) You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency
27
| list.         | It is named | after  | Vaclav       | Havel and  | Samih Hakimi. |     |     |     |
| ------------- | ----------- | ------ | ------------ | ---------- | ------------- | --- | --- | --- |
| 28 I checked: | What        | is the | Havel-Hakimi | algorithm? |               |     |     |     |
29 I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree
sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm.
| The algorithm |     | was published | by  | Havel (1955), | and later | by Hakimi | (1962). |     |
| ------------- | --- | ------------- | --- | ------------- | --------- | --------- | ------- | --- |
30 Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists, or
proving that one cannot find a positive answer, not converting the adjacency matrix of a graph into its adjacency list.
| 31 This disagrees |     | with what | you said. |     |     |     |     |     |
| ----------------- | --- | --------- | --------- | --- | --- | --- | --- | --- |
32
(6) You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
33
| Dirty         | Dancing. | The song | was produced | by        | Michael Lloyd. |            |        |     |
| ------------- | -------- | -------- | ------------ | --------- | -------------- | ---------- | ------ | --- |
| 34 I checked: | Who      | was the  | producer     | of "(I’ve | Had) The       | Time of My | Life"? |     |
35 I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd,
was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at
| Stanford       | University. |      |           |            |        |     |     |     |
| -------------- | ----------- | ---- | --------- | ---------- | ------ | --- | --- | --- |
| 36 "Time       | of My Life" | was  | produced  | by Michael | Lloyd. |     |     |     |
| 37 This agrees | with        | what | you said. |            |        |     |     |     |
38
39 (7) You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved
| inappropriately |     | towards    | a Labour | Party      | activist, Ava | Etemadzadeh. |     |     |
| --------------- | --- | ---------- | -------- | ---------- | ------------- | ------------ | --- | --- |
| 40 I checked:   | Why | was Kelvin | Hopins   | suspeneded | from the      | Labor Party? |     |     |
41 I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against
him was able to be concluded, the party has confirmed. Kelvin Hopkins was accused in 2017 of inappropriate physical
contact and was suspended by the Labour party pending an investigation.This agrees with what you said.
42 Kelvin Hopins was suspended because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party
| activist,      | Ava  | Etemadzadeh. |           |     |     |     |     |     |
| -------------- | ---- | ------------ | --------- | --- | --- | --- | --- | --- |
| 43 This agrees | with | what         | you said. |     |     |     |     |     |
44
45 (8) You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
| 46 I checked: | Who | led the | British | side in | the battle | of Lexington | and Concord? |     |
| ------------- | --- | ------- | ------- | ------- | ---------- | ------------ | ------------ | --- |
47 I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant
| Colonel           | Francis | Smith.    | There were    | 700 British | regulars.       |        |                    |       |
| ----------------- | ------- | --------- | ------------- | ----------- | --------------- | ------ | ------------------ | ----- |
| 48 The British    | side    | was led   | by Lieutenant |             | Colonel Francis | Smith, | not General Thomas | Hall. |
| 49 This disagrees |         | with what | you said.     |             |                 |        |                    |       |
50
| 51 (9) You | said:   | {text} |     |     |     |     |     |     |
| ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| I checked: | {query} |        |     |     |     |     |     |     |
52
| 53 I found | this article: |     | {evidence} |     |     |     |     |     |
| ---------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
54 _____
Figure14: Few-shotpromptfortheagreementmodel,whichuseschain-of-thoughtprompting.

| [web] | I will fix | some things | you | said. |     |     |     |     |
| ----- | ---------- | ----------- | --- | ----- | --- | --- | --- | --- |
1
2
3 (1) You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This
| is to        | prevent | a buildup | of mucus.     | It’s    | called the | nasal | cycle. |     |
| ------------ | ------- | --------- | ------------- | ------- | ---------- | ----- | ------ | --- |
| 4 I checked: | How     | often do  | your nostrils | switch? |            |       |        |     |
I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus
5
contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every
| 2 hours,        | according | to a       | small 2016 | study   | published      | in the | journal PLOS | One. |
| --------------- | --------- | ---------- | ---------- | ------- | -------------- | ------ | ------------ | ---- |
| 6 This suggests |           | 45 minutes | switch     | time in | your statement |        | is wrong.    |      |
7 My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to
| prevent | a buildup | of mucus. | It’s | called | the nasal | cycle. |     |     |
| ------- | --------- | --------- | ---- | ------ | --------- | ------ | --- | --- |
8
9 (2) You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
| 10 I checked: | who | led the | British | side in | the battle | of Lexington | and Concord? |     |
| ------------- | --- | ------- | ------- | ------- | ---------- | ------------ | ------------ | --- |
11 I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant
| Colonel          | Francis | Smith.         | There were | 700 British | regulars. |     |        |     |
| ---------------- | ------- | -------------- | ---------- | ----------- | --------- | --- | ------ | --- |
| 12 This suggests |         | General Thomas | Hall       | in your     | statement | is  | wrong. |     |
13 My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.
14
15 (3) You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
| I checked: | where | was Stanford | Prison | Experiment |     | conducted. |     |     |
| ---------- | ----- | ------------ | ------ | ---------- | --- | ---------- | --- | --- |
16
17 I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set
out to examine the psychological effects of authority and powerlessness in a prison environment.
| 18 This suggests |     | Encina Hall | in your | statement | is  | wrong. |     |     |
| ---------------- | --- | ----------- | ------- | --------- | --- | ------ | --- | --- |
19 My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
20
21 (4) You said: Phoenix Mills Ltd., a diversified business conglomerate, was established in 1854. It has a history of over
160 years.
| 22 I checked: | When | was Phoenix | Mills | Ltd. | founded? |     |     |     |
| ------------- | ---- | ----------- | ----- | ---- | -------- | --- | --- | --- |
23 I found this article: Phoenix Mills Ltd was incorporated in the year 1905. The company began their operations as a textile
manufacturing company on 17.3 acres of land at Lower Parel in Mumbai. In the year 1959 the company was listed in the
| Bombay        | Stock Exchange. |          |                  |     |         |                |           |     |
| ------------- | --------------- | -------- | ---------------- | --- | ------- | -------------- | --------- | --- |
| This suggests |                 | the year | of establishment |     | 1854 in | your statement | is wrong. |     |
24
25 My fix: Phoenix Mills Ltd., a diversified business conglomerate, was established in 1905. It has a history of over 160
years.
26
27 (5) You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency
| list.         | It is named | after  | Vaclav       | Havel and  | Samih | Hakimi. |     |     |
| ------------- | ----------- | ------ | ------------ | ---------- | ----- | ------- | --- | --- |
| 28 I checked: | What        | is the | Havel-Hakimi | algorithm? |       |         |     |     |
29 I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree
sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm.
| The algorithm |     | was published    | by  | Havel (1955), | and           | later | by Hakimi (1962). |           |
| ------------- | --- | ---------------- | --- | ------------- | ------------- | ----- | ----------------- | --------- |
| This suggests |     | the Havel-Hakimi |     | algorithm’s   | functionality |       | in your statement | is wrong. |
30
31 My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists,
or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi
32
33 (6) You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
| Dirty         | Dancing. | The song | was produced | by        | Phil Ramone. |          |              |     |
| ------------- | -------- | -------- | ------------ | --------- | ------------ | -------- | ------------ | --- |
| 34 I checked: | Who      | was the  | producer     | of "(I’ve | Had)         | The Time | of My Life"? |     |
35 I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd,
was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at
| Stanford      | University. |          |          |          |         |                |           |     |
| ------------- | ----------- | -------- | -------- | -------- | ------- | -------------- | --------- | --- |
| This suggests |             | "Time of | My Life" | producer | name in | your statement | is wrong. |     |
36
37 My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty
| Dancing. | The song | was produced |     | by Michael | Lloyd. |     |     |     |
| -------- | -------- | ------------ | --- | ---------- | ------ | --- | --- | --- |
38
39 (7) You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels
with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
| 40 I checked: | What | is the | area of | Phoenix | Market City | in Pune? |     |     |
| ------------- | ---- | ------ | ------- | ------- | ----------- | -------- | --- | --- |
41 I found this article: Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall
in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
| 42 This suggests |     | the 1.4 million | square | feet | of built-up | space | in your statment | is wrong. |
| ---------------- | --- | --------------- | ------ | ---- | ----------- | ----- | ---------------- | --------- |
43 My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with
approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
44
| 45 (8) You       | said:         | {text}     |     |     |     |     |     |     |
| ---------------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
| 46 I checked:    | {query}       |            |     |     |     |     |     |     |
| 47 I found       | this article: | {evidence} |     |     |     |     |     |     |
| 48 This suggests |               | _____      |     |     |     |     |     |     |
Figure15: Few-shotpromptfortherevisionmodel,whichuseschain-of-thoughtprompting.

| 1 [web] | I will read | the context | and | check | only the | last thing | you said by asking | questions. |
| ------- | ----------- | ----------- | --- | ----- | -------- | ---------- | ------------------ | ---------- |
2
3 (1) Context: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes.
| 4 You said: | This     | is to prevent | a            | buildup of | mucus. | It’s called | the nasal cycle. |     |
| ----------- | -------- | ------------- | ------------ | ---------- | ------ | ----------- | ---------------- | --- |
| 5 To verify | what     | you just      | said,        |            |        |             |                  |     |
| 6 a) I      | googled: | Why does      | your nostril | switch     | during | sleep?      |                  |     |
| b) I        | googled: | What is nasal | cycle?       |            |        |             |                  |     |
7
| 8 c) I | googled: | What is the | nostril | switching | during | sleep called? |     |     |
| ------ | -------- | ----------- | ------- | --------- | ------ | ------------- | --- | --- |
9
10 (2) Context: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
11 You said: It is a psychological study to observe the behaviors of conflict and violence that happen between inmates and
| prisoners    | in real  | prisons.  |               |     |              |        |             |     |
| ------------ | -------- | --------- | ------------- | --- | ------------ | ------ | ----------- | --- |
| 12 To verify | what     | you just  | said,         |     |              |        |             |     |
| 13 a) I      | googled: | What type | of experiment | was | the Stanford | Prison | Experiment? |     |
| 14 b) I      | googled: | What was  | the objective | of  | the Stanford | Prison | Experiment? |     |
15
16 (3) Context: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency
list.
| 17 You said: | It is    | named after          | Vaclav | Havel     | and Samih | Hakimi. |     |     |
| ------------ | -------- | -------------------- | ------ | --------- | --------- | ------- | --- | --- |
| 18 To verify | what     | you just             | said,  |           |           |         |     |     |
| 19 a) I      | googled: | Who are Havel-Hakimi |        | algorithm | named     | after?  |     |     |
20
21 (4) Context: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
Dirty Dancing.
| 22 You said: | The      | song was     | produced | by Michael | Lloyd    | in the same    | year.     |     |
| ------------ | -------- | ------------ | -------- | ---------- | -------- | -------------- | --------- | --- |
| 23 To verify | what     | you just     | said,    |            |          |                |           |     |
| 24 a) I      | googled: | Who produced | the      | song "Time | of My    | Life"?         |           |     |
| 25 b) I      | googled: | When was     | the song | "Time of   | My Life" | by Bill Medley | produced? |     |
26
27 (5) Context: The Late Show with Stephen Colbert is an American late-night talk show hosted by Stephen Colbert, which
| premiered | on September |     | 8, 2015. |     |     |     |     |     |
| --------- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
28 You said: Produced by Spartina Productions and CBS Television Studios, it is the second iteration of CBS’ Late Show
franchise.
| To verify | what | you just | said, |     |     |     |     |     |
| --------- | ---- | -------- | ----- | --- | --- | --- | --- | --- |
29
| 30 a) I | googled: | Who produces | "The           | Late Show | with Stephen | Colbert"?       |     |     |
| ------- | -------- | ------------ | -------------- | --------- | ------------ | --------------- | --- | --- |
| 31 b) I | googled: | What are     | the iterations | of        | CBS’ Late    | Show franchise? |     |     |
32
33 (6) Context: Super Mario Sunshine was released on GameCube in 2002. In the game, Mario uses a tool strapped to his back
| called | FLUDD, | which stands | for | The Flash | Liquidizer | Ultra Dousing | Device. |     |
| ------ | ------ | ------------ | --- | --------- | ---------- | ------------- | ------- | --- |
34 You said: It can be used to spray water at objects or enemies. This allows Mario to change his movements, kill enemies,
| or clean     | up hazards | on          | the floor. |             |          |                |           |     |
| ------------ | ---------- | ----------- | ---------- | ----------- | -------- | -------------- | --------- | --- |
| 35 To verify | what       | you just    | said,      |             |          |                |           |     |
| 36 a) I      | googled:   | What is the | main       | function    | of FLUDD | in Super Mario | Sunshine? |     |
| b) I         | googled:   | What can    | FLUDD in   | Super Mario | Sunshine | be used        | on?       |     |
37
| 38 c) I | googled: | In Super | Mario Sunshine, | can | Mario | change movement | with FLUDD? |     |
| ------- | -------- | -------- | --------------- | --- | ----- | --------------- | ----------- | --- |
| 39 d) I | googled: | In Super | Mario Sunshine, | can | Mario | kill enemies    | with FLUDD? |     |
40 e) I googled: In Super Mario Sunshine, can Mario clean up hazards on the floor with FLUDD?
41
| (7) Context: | {context} |     |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
42
| 43 You said: | {text} |          |       |     |     |     |     |     |
| ------------ | ------ | -------- | ----- | --- | --- | --- | --- | --- |
| 44 To verify | what   | you just | said, |     |     |     |     |     |
45 _____
Figure16: Contextualversionofthequerygenerationprompt. Thepromptworkswellfordialogcontextsfrom
QReCCeventhoughthefew-shotexamplesarenotformattedassuch.

| 1 [web] | I will | check some | things | you said. |     |     |     |     |
| ------- | ------ | ---------- | ------ | --------- | --- | --- | --- | --- |
2
3 (1) Context: Your nose switches back and forth between nostrils. It’s called the nasal cycle. This is to prevent a buildup
of mucus.
| 4 You said:  | When | you sleep, | you           | switch about | every 45 | minutes. |     |     |
| ------------ | ---- | ---------- | ------------- | ------------ | -------- | -------- | --- | --- |
| 5 I checked: | How  | often do   | your nostrils | switch?      |          |          |     |     |
I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus
6
contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every
| 2 hours, | according        | to        | a small   | 2016 study  | published | in the journal  | PLOS | One. |
| -------- | ---------------- | --------- | --------- | ----------- | --------- | --------------- | ---- | ---- |
| 7 Your   | nose’s switching |           | time is   | about every | 2 hours,  | not 45 minutes. |      |      |
| 8 This   | disagrees        | with what | you said. |             |           |                 |      |      |
9
| 10 (2) Context: |     | The Little | House      | books is          | a series of | American | children’s | novels. |
| --------------- | --- | ---------- | ---------- | ----------------- | ----------- | -------- | ---------- | ------- |
| 11 You said:    | The | books were | published  | by HarperCollins. |             |          |            |         |
| 12 I checked:   | Who | published  | the Little | House             | books?      |          |            |         |
13 I found this article: These are the books that started it all – the stories that captured the hearts and imaginations of
children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books
| remain        | a favorite  | to this | day.           |     |                |     |     |     |
| ------------- | ----------- | ------- | -------------- | --- | -------------- | --- | --- | --- |
| 14 The Little | House       | books   | were published | by  | HarperCollins. |     |     |     |
| 15 This       | agrees with | what    | you said.      |     |                |     |     |     |
16
(3) Context: The Stanford Prison Experiment is a psychological study to observe the behaviors of conflict and violence
17
| that | happen between | inmates | and | prisoners | in real | prisons. |     |     |
| ---- | -------------- | ------- | --- | --------- | ------- | -------- | --- | --- |
18 You said: It was conducted in the basement of Jordan Hall, Stanford’s psychology building.
| 19 I checked: | Where | was Stanford |     | Prison Experiment | conducted? |     |     |     |
| ------------- | ----- | ------------ | --- | ----------------- | ---------- | --- | --- | --- |
20 I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set
out to examine the psychological effects of authority and powerlessness in a prison environment.
| 21 The Stanford |             | Prison Experiment |           | was conducted | in Jordan | Hall. |     |     |
| --------------- | ----------- | ----------------- | --------- | ------------- | --------- | ----- | --- | --- |
| 22 This         | agrees with | what              | you said. |               |           |       |     |     |
23
24 (4) Context: Social work is a profession that is based in the philosophical tradition of humanism.
| 25 You said:  | It   | is an intellectual |      | discipline | that has | its roots | in the 1800s. |     |
| ------------- | ---- | ------------------ | ---- | ---------- | -------- | --------- | ------------- | --- |
| 26 I checked: | When | did social         | work | have its   | roots?   |           |               |     |
I found this article: The Emergence and Growth of the Social work Profession<br><br> Social work’s roots were planted in
27
the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and
| settlement | houses    | were      | established. |        |            |     |     |     |
| ---------- | --------- | --------- | ------------ | ------ | ---------- | --- | --- | --- |
| 28 Social  | work has  | its roots | in the       | 1880s, | not 1800s. |     |     |     |
| 29 This    | disagrees | with what | you said.    |        |            |     |     |     |
30
| 31 (5) Context: |     | The Havel-Hakimi |     | algorithm | is named after | Vaclav | Havel and | Samih Hakimi. |
| --------------- | --- | ---------------- | --- | --------- | -------------- | ------ | --------- | ------------- |
32 You said: It is an algorithm for converting the adjacency matrix of a graph into its adjacency list.
| 33 I checked: | What | is the | Havel-Hakimi | algorithm? |     |     |     |     |
| ------------- | ---- | ------ | ------------ | ---------- | --- | --- | --- | --- |
34 I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree
sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm.
| The algorithm |     | was published | by  | Havel (1955), | and later | by Hakimi | (1962). |     |
| ------------- | --- | ------------- | --- | ------------- | --------- | --------- | ------- | --- |
35 Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists, or
proving that one cannot find a positive answer, not converting the adjacency matrix of a graph into its adjacency list.
| 36 This | disagrees | with what | you said. |     |     |     |     |     |
| ------- | --------- | --------- | --------- | --- | --- | --- | --- | --- |
37
38 (6) Context: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
Dirty Dancing.
| 39 You said:  | The | song was | produced | by Michael | Lloyd in | the same   | year.  |     |
| ------------- | --- | -------- | -------- | ---------- | -------- | ---------- | ------ | --- |
| 40 I checked: | Who | was the  | producer | of "(I’ve  | Had) The | Time of My | Life"? |     |
I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd,
41
was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at
| Stanford    | University. |             |           |          |            |        |     |     |
| ----------- | ----------- | ----------- | --------- | -------- | ---------- | ------ | --- | --- |
| 42 The song | "Time       | of My Life" | was       | produced | by Michael | Lloyd. |     |     |
| 43 This     | agrees with | what        | you said. |          |            |        |     |     |
44
45 (7) Context: Super Mario Sunshine was released on GameCube in 2002. In the game, Mario uses a tool strapped to his back
| called | FLUDD. |     |     |     |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
46 You said: FLUDD stands for Functional Language in a Unified Design Discipline. It can be used to spray water at objects
or enemies. This allows Mario to change his movements, kill enemies, or clean up hazards on the floor.
| 47 I checked: | What | does FLUDD | stands | for in | Super Mario | Sunshine? |     |     |
| ------------- | ---- | ---------- | ------ | ------ | ----------- | --------- | --- | --- |
48 I found this article: The Flash Liquidizer Ultra Dousing Device, abbreviated and better known as FLUDD or F.L.U.D.D.,
is a multipurpose water pack from Super Mario Sunshine invented by Professor Elvin Gadd, indicated by the Gadd Science,
| Incorporated |     | logo at the | base | of its nozzle | exclusively | during | the cutscene | at Pinna Park. |
| ------------ | --- | ----------- | ---- | ------------- | ----------- | ------ | ------------ | -------------- |
49 In Super Mario Sunshine, FLUDD stands for the Flash Liquidizer Ultra Dousing Device, not Functional Language in a Unified
| Design  | Discipline. |           |           |     |     |     |     |     |
| ------- | ----------- | --------- | --------- | --- | --- | --- | --- | --- |
| 50 This | disagrees   | with what | you said. |     |     |     |     |     |
51
| 52 (8) Context: |         | {context} |            |     |     |     |     |     |
| --------------- | ------- | --------- | ---------- | --- | --- | --- | --- | --- |
| 53 You said:    | {text}  |           |            |     |     |     |     |     |
| 54 I checked:   | {query} |           |            |     |     |     |     |     |
| 55 I found      | this    | article:  | {evidence} |     |     |     |     |     |
_____
56
|     |     |     | Figure17: | Contextualversionoftheagreementmodelprompt. |     |     |     |     |
| --- | --- | --- | --------- | ------------------------------------------- | --- | --- | --- | --- |

1 [web] I will fix some things you said.
2
3 (1) Context: Your nose switches back and forth between nostrils. It’s called the nasal cycle. This is to prevent a buildup
of mucus.
4 You said: When you sleep, you switch about every 45 minutes.
5 I checked: How often do your nostrils switch?
6 I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus
contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every
2 hours, according to a small 2016 study published in the journal PLOS One.
7 This suggests 45 minutes switch time in your statement is wrong.
8 My fix: When you sleep, you switch about every 2 hours.
9
10 (2) Context: The Little House books is a series of American children’s novels.
11 You said: The books were published by Amberjack Publishing.
12 I checked: Who published the Little House books?
13 I found this article: These are the books that started it all – the stories that captured the hearts and imaginations of
children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books
remain a favorite to this day.
14 This suggests Amberjack Publishing in your statement is wrong.
15 My fix: The books were published by HarperCollins.
16
17 (3) Context: The Stanford Prison Experiment is a psychological study to observe the behaviors of conflict and violence
that happen between inmates and prisoners in real prisons.
18 You said: It was conducted in the basement of Encina Hall, Stanford’s psychology building.
19 I checked: where was Stanford Prison Experiment conducted.
20 I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set
out to examine the psychological effects of authority and powerlessness in a prison environment.
21 This suggests Encina Hall in your statement is wrong.
22 My fix: It was conducted in the basement of Jordan Hall, Stanford’s psychology building.
23
24 (4) Context: The Havel-Hakimi algorithm is named after Vaclav Havel and Samih Hakimi.
25 You said: It is an algorithm for converting the adjacency matrix of a graph into its adjacency list.
26 I checked: What is the Havel-Hakimi algorithm?
27 I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree
sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm.
The algorithm was published by Havel (1955), and later by Hakimi (1962).
28 This suggests the Havel-Hakimi algorithm’s functionality in your statement is wrong.
29 My fix: It constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot
find a positive answer.
30
31 (5) Context: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
Dirty Dancing.
32 You said: The song was produced by Phil Ramone in the same year.
33 I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
34 I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd,
was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at
Stanford University.
35 This suggests "Time of My Life" producer name in your statement is wrong.
36 My fix: The song was produced by Michael Lloyd in the same year.
37
38 (6) Context: Phoenix Market City Pune is located on 21 acres of prime property in Pune. The mall is owned and operated by
Phoenix Mills Limited.
39 You said: It is spread across four levels with approximately 1.4 million square feet of built-up space.
40 I checked: What is the area of Phoenix Market City in Pune?
41 I found this article: Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall
in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
42 This suggests the 1.4 million square feet of built-up space in your statment is wrong.
43 My fix: It is spread across four levels with approximately 3.4 million square feet of built-up space.
44
45 (7) Context: {context}
46 You said: {text}
47 I checked: {query}
48 I found this article: {evidence}
49 This suggests _____
Figure18: Contextualversionoftherevisionmodelprompt.

1 [web] I will think step by step and answer your question.
2
3 Question: is growing seedless cucumber good for a gardener with entomophobia
4 Explanation: Entomophobia is a fear of insects. Plants need insects to pollinate them. Seedless fruits such as seedless
cucumbers do not require pollination, so seedless fruits do not require insects. This makes good for people with
entomophobia.
5 Answer: Yes
6
7 Question: Who was british pm and viceroy during quit india movement?
8 Explanation: The Quit India Movement was launched in 8th August 1942. The british PM at that time was Winston Churchill.
The british viceroy during the movement is Victor Hope, usually referred to as Lord Linlithgow.
9 Answer: Winston Churchil and Lord Linlithgow
10
11 Question: Which year does game over man come out on netflix?
12 Explanation: Game Over, Man! is an action-comedy movie released in March 23, 2018, on Netflix. It’s director is Kyle
Newacheck. The movie stars Anders Holm, Adam DeVine, and Blake Anderson.
13 Answer: March 23, 2018
14
15 Question: would it be very difficult for Nuno Gomes to dive to the Red Sea’s deepest point?
16 Explanation: Nuno Gomes’ deepest dive in the Red Sea to date is 317 metres. The Red Sea has a maximum depth of over 3,000
metres. So it would be difficult for Nuno Gomes to the deepest point of the Red sea.
17 Answer: Yes
18
19 Question: Are chinchillas cold-blooded?
20 Explanation: Chinchillas are rodents, which are mammals. All mammals are warm-blooded.
21 Answer: No
22
23 Question: what are the chemo drugs for gastric cancer?
24 Explanation: Chemotherapy can be given for gastric cancer before or after surgery. Usually you have a combination of 2 or
3 drugs. The most common types are: epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and fluorouracil
(ECF); or fluorouracil, folinic acid, oxaliplatin and docetaxel (FLOT).
25 Answer: epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and fluorouracil (ECF); or fluorouracil,
folinic acid, oxaliplatin and docetaxel (FLOT)
26
27 Question: How many sacks does Clay Matthews have in his career?
28 Explanation: Clay Matthews III had 383 solo tackles, 136 assists, and 91.5 sacks. His father, Clay Matthews Jr., also
palyed in NFL and had 69.5 sacks in his career.
29 Answer: 91.5 (Clay Matthews III) and 69.5 (Clay Matthews Jr.)
30
31 Question: In the U.S., the most deaths are caused by
32 Explanation: The leading cause of death in the U.S. is heart disease, causing nearly 700,000 deaths annually. The second
most common cause of deaths is cancer.
33 Answer: heart disease
34
35 Question: the rank of indian economy in terms of nominal gdp is
36 Explanation: India’s GDP is economy is $2.94 trillion. It is the fifth-largest in the world. The top GDP contries are
United States, China, Japan, Germany and India.
37 Answer: 5
38
39 Question: {question}
40 Explanation: _____
Figure19: ThePaLMpromptforgeneratinglong-formanswerstoquestionsfromNQandSQA.

| 1 I will | think step | by step | and answer | your | question. |     |     |     |
| -------- | ---------- | ------- | ---------- | ---- | --------- | --- | --- | --- |
2
| 3 1. Question: | Is  | growing | seedless | cucumber | good for | a gardener | with entomophobia? |     |
| -------------- | --- | ------- | -------- | -------- | -------- | ---------- | ------------------ | --- |
4 2. Explanation: Entomophobiaisafearofinsects. Plantsneedinsectstopollinatethem. Seedlessfruitssuchasseedless
cucumbers do not require pollination so seedless fruits do not require insects. This is good for people with entomophobia.
| 5 3. Answer: | Yes. |     |     |     |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
6
| 7 1. Question: | Who | was British | PM  | and Biceroy | during | Quit India | Movement? |     |
| -------------- | --- | ----------- | --- | ----------- | ------ | ---------- | --------- | --- |
8 2. Explanation: TheQuitIndiaMovementwas launchedin8thAugust1942. TheBritishPMat thattimewasWinstonChurchill.
The British Biceroy during the movement was Victor Hope, usually referred to as Lord Linlithgow.
| 9 3. Answer: | Winston | Churchil | and | Lord Linlithgow. |     |     |     |     |
| ------------ | ------- | -------- | --- | ---------------- | --- | --- | --- | --- |
10
| 11 1. Question: | Which | year | does Game | Over Man | come out | on Netflix? |     |     |
| --------------- | ----- | ---- | --------- | -------- | -------- | ----------- | --- | --- |
12 2. Explanation: Game Over, Man! is an action-comedy movie. Its director is Kyle Newacheck. The movie stars Anders Holm,
| Adam DeVine,  | and   | Blake     | Anderson. | The movie | was released | March | 23, 2018 | on Netflix. |
| ------------- | ----- | --------- | --------- | --------- | ------------ | ----- | -------- | ----------- |
| 13 3. Answer: | March | 23, 2018. |           |           |              |       |          |             |
14
15 1. Question: Would it be very difficult for Nuno Gomes to dive to the Red Sea’s deepest point?
16 2. Explanation: Nuno Gomes’ deepest dive in the Red Sea to date is 317 meters. The Red Sea has a maximum depth of over
3,000 meters. So it would be difficult for Nuno Gomes to dive to the deepest point of the Red Sea.
| 17 3. Answer: | Yes. |     |     |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
18
| 19 1. Question: | Are | chinchillas | cold-blooded? |     |     |     |     |     |
| --------------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- |
20 2. Explanation: Chinchillas are rodents. Rodents are mammals. All mammals are warm-blooded.
| 21 3. Answer: | No. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
22
| 1. Question: | What | are the | chemo | drugs for | gastric cancer? |     |     |     |
| ------------ | ---- | ------- | ----- | --------- | --------------- | --- | --- | --- |
23
24 2. Explanation: Chemotherapy can be given for gastric cancer before or after surgery. Usually you have a combination
of 2 or 3 drugs. The most common types are: epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and
| fluorouracil | (ECF); | or  | fluorouracil, | folinic | acid, | oxaliplatin | and docetaxel | (FLOT). |
| ------------ | ------ | --- | ------------- | ------- | ----- | ----------- | ------------- | ------- |
25 3. Answer: Epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and fluorouracil (ECF); or fluorouracil,
| folinic | acid, oxaliplatin |     | and docetaxel | (FLOT). |     |     |     |     |
| ------- | ----------------- | --- | ------------- | ------- | --- | --- | --- | --- |
26
| 27 1. Question: | How | many sacks | does | Clay Matthews | have | in his | career? |     |
| --------------- | --- | ---------- | ---- | ------------- | ---- | ------ | ------- | --- |
28 2. Explanation: Clay Matthews has been pro linebacker for 11 seasons. Ten of the seasons he played for Green Bay Packers,
while his last season was with Los Angeles Rams, dedicated to his hometown. Clay Matthews III had 383 solo tackles, 136
assists, and 91.5 sacks. His father, Clay Matthews Jr., also played in NFL and had 69.5 sacks in his career.
| 29 3. Answer: | 91.5 | (Clay Matthews | III) | and 69.5 | (Clay | Matthews | Jr.). |     |
| ------------- | ---- | -------------- | ---- | -------- | ----- | -------- | ----- | --- |
30
| 31 1. Question: | In  | the U.S., | the most | deaths | are caused | by? |     |     |
| --------------- | --- | --------- | -------- | ------ | ---------- | --- | --- | --- |
32 2. Explanation: According to the Centers for Disease Control and Prevention, there were 3 million deaths in 2018. The
leading cause of death in the U.S. is heart disease, causing nearly 700,000 deaths annually. The second most common cause
| of deaths     | is cancer. |          |     |     |     |     |     |     |
| ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| 33 3. Answer: | Heart      | disease. |     |     |     |     |     |     |
34
| 35 1. Question: | The | rank of | Indian | economy in | terms of | nominal | GDP is? |     |
| --------------- | --- | ------- | ------ | ---------- | -------- | ------- | ------- | --- |
2. Explanation: The top GDP contries are United States, China, Japan, Germany, and India. India’s GDP is economy is $2.94
36
| trillion.     | It is | the fifth-largest |     | economy | in the world. |     |     |     |
| ------------- | ----- | ----------------- | --- | ------- | ------------- | --- | --- | --- |
| 37 3. Answer: | 5.    |                   |     |         |               |     |     |     |
38
| 39 1. Question: | Who | won season | 16 on | Dancing | with the | Stars? |     |     |
| --------------- | --- | ---------- | ----- | ------- | -------- | ------ | --- | --- |
40 2. Explanation: Dancing with the Stars is an American dance competition television series that premiered on June 1, 2005,
| on ABC.       | The 16th | season   | premiered | on March | 18, 2013. | It was | won by Kellie | Pickler. |
| ------------- | -------- | -------- | --------- | -------- | --------- | ------ | ------------- | -------- |
| 41 3. Answer: | Kellie   | Pickler. |           |          |           |        |               |          |
42
| 43 1. Question:    | {question} |       |     |     |     |     |     |     |
| ------------------ | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| 44 2. Explanation: |            | _____ |     |     |     |     |     |     |
Figure20: TheGPT-3promptforgeneratinglong-formanswerstoquestionsfromNQandSQA.

| 1 Hi, I      | will think | step by  | step and answer | your       | question. |               |     |     |
| ------------ | ---------- | -------- | --------------- | ---------- | --------- | ------------- | --- | --- |
| 2 Is growing | seedless   | cucumber | good for        | a gardener | with      | entomophobia? |     |     |
3 Yes. Entomophobia is a fear of insects. Plants need insects to pollinate them. Seedless cucumber fruit does not require
| pollination. | So         | seedless  | cucumber does | not require | insects. |          |                 |     |
| ------------ | ---------- | --------- | ------------- | ----------- | -------- | -------- | --------------- | --- |
| 4 Here       | is another | question. | Which year    | does game   | over     | man come | out on netflix? |     |
5 Game Over, Man! is an American action-comedy movie. It was released on March 23, 2018, on Netflix. It is directed by Kyle
| Newacheck, | written    | by Anders | Holm,    | and starring | himself,  | Adam    | DeVine, | and Blake Anderson. |
| ---------- | ---------- | --------- | -------- | ------------ | --------- | ------- | ------- | ------------------- |
| 6 Here     | is another | question. | What are | the chemo    | drugs for | gastric | cancer? |                     |
7 Chemotherapy can be given for gastric cancer before or after surgery. Usually you have a combination of 2 or 3 drugs. The
most common types are: epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and fluorouracil (ECF); or
| fluorouracil, |                  | folinic acid,   | oxaliplatin | and           | docetaxel   | (FLOT). |     |     |
| ------------- | ---------------- | --------------- | ----------- | ------------- | ----------- | ------- | --- | --- |
| 8 Here        | is another       | question.       | Was N.W.A   | a album?      |             |         |     |     |
| 9 N.W.A       | was an American  | hip             | hop group   | from Compton, | California. |         |     |     |
| 10 Were       | they successful? |                 |             |               |             |         |     |     |
| 11 They       | has sold         | over 10 million | units       | in the United | States      | alone.  |     |     |
| How many      | singles          | did it          | have?       |               |             |         |     |     |
12
| 13 The group | NWA        | released 8 | singles. |     |     |     |     |     |
| ------------ | ---------- | ---------- | -------- | --- | --- | --- | --- | --- |
| 14 Here      | is another | question.  | {Q1}     |     |     |     |     |     |
15 {A1}
16 ...
{Qk}
17
18 _____
Figure21: TheLaMDApromptforgeneratinganswerstoquestionsfromQReCC.Eachlineisaconversationturn.
ThedialogcontextfromQReCCcontainsroundsofquestionsandanswers(Q ,A ,Q ,A ,...,Q ).
1 1 2 2 k
| 1 I will | think step | by step | and answer | your question. |     |     |     |     |
| -------- | ---------- | ------- | ---------- | -------------- | --- | --- | --- | --- |
2
| 3 Is growing | seedless | cucumber | good for | a gardener | with | entomophobia? |     |     |
| ------------ | -------- | -------- | -------- | ---------- | ---- | ------------- | --- | --- |
4 Yes. Entomophobia is a fear of insects. Plants need insects to pollinate them. Seedless cucumber fruit does not require
| pollination. | So  | seedless | cucumber does | not require | insects. |     |     |     |
| ------------ | --- | -------- | ------------- | ----------- | -------- | --- | --- | --- |
5
| 6 Which | year does | game over | man come | out on netflix? |     |     |     |     |
| ------- | --------- | --------- | -------- | --------------- | --- | --- | --- | --- |
7 Game Over, Man! is an American action-comedy movie. It was released on March 23, 2018, on Netflix. It is directed by Kyle
| Newacheck, | written | by Anders | Holm, | and starring | himself, | Adam | DeVine, | and Blake Anderson. |
| ---------- | ------- | --------- | ----- | ------------ | -------- | ---- | ------- | ------------------- |
8
| 9 What | are the chemo | drugs | for gastric | cancer? |     |     |     |     |
| ------ | ------------- | ----- | ----------- | ------- | --- | --- | --- | --- |
10 Chemotherapy can be given for gastric cancer before or after surgery. Usually you have a combination of 2 or 3 drugs. The
most common types are: epirubicin, cisplatin and capecitabine (ECX) ; epirubicin, cisplatin and fluorouracil (ECF); or
| fluorouracil, |     | folinic acid, | oxaliplatin | and | docetaxel | (FLOT). |     |     |
| ------------- | --- | ------------- | ----------- | --- | --------- | ------- | --- | --- |
11
| 12 Was N.W.A | an album?        |                 |           |               |             |        |     |     |
| ------------ | ---------------- | --------------- | --------- | ------------- | ----------- | ------ | --- | --- |
| 13 N.W.A     | was an American  | hip             | hop group | from Compton, | California. |        |     |     |
| 14 Were      | they successful? |                 |           |               |             |        |     |     |
| They         | has sold         | over 10 million | units     | in the United | States      | alone. |     |     |
15
| 16 How many | singles | did they | have? |     |     |     |     |     |
| ----------- | ------- | -------- | ----- | --- | --- | --- | --- | --- |
17 N.W.A had eight singles, including "Straight Outta Compton", "Express Yourself", "Gangsta Gangsta", "Dopeman" and "Alwayz
Into Somethin’".
18
{Q1}
19
20 {A1}
21 ...
22 {Qk}
23 _____
|     | Figure22: |     | TheGPT-3promptforgeneratinganswerstoquestionsfromQReCC. |     |     |     |     |     |
| --- | --------- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
