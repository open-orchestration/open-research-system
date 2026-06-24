| Tree      | of Thoughts: |     |        | Deliberate |             | Problem |     | Solving      |
| --------- | ------------ | --- | ------ | ---------- | ----------- | ------- | --- | ------------ |
|           | with         |     | Large  | Language   |             | Models  |     |              |
| ShunyuYao |              |     | DianYu |            | JeffreyZhao |         |     | IzhakShafran |
PrincetonUniversity GoogleDeepMind GoogleDeepMind GoogleDeepMind
3202 ceD 3  ]LC.sc[  2v10601.5032:viXra
| ThomasL.Griffiths   |     |     |     | YuanCao        |     |     | KarthikNarasimhan   |     |
| ------------------- | --- | --- | --- | -------------- | --- | --- | ------------------- | --- |
| PrincetonUniversity |     |     |     | GoogleDeepMind |     |     | PrincetonUniversity |     |
Abstract
| Language        | models | are       | increasingly | being             | deployed       | for   | general      | problem solving   |
| --------------- | ------ | --------- | ------------ | ----------------- | -------------- | ----- | ------------ | ----------------- |
| across          | a wide | range     | of tasks,    | but are           | still confined | to    | token-level, | left-to-right     |
| decision-making |        | processes |              | during inference. | This           | means | they         | can fall short in |
tasksthatrequireexploration,strategiclookahead,orwhereinitialdecisionsplay
| apivotalrole. |     | Tosurmountthesechallenges,weintroduceanewframeworkfor |     |     |     |     |     |     |
| ------------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
languagemodelinference,“TreeofThoughts”(ToT),whichgeneralizesoverthe
popular“ChainofThought”approachtopromptinglanguagemodels,andenables
explorationovercoherentunitsoftext(“thoughts”)thatserveasintermediatesteps
| towardproblemsolving. |     |     | ToTallowsLMstoperformdeliberatedecisionmaking |     |     |     |     |     |
| --------------------- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
byconsideringmultipledifferentreasoningpathsandself-evaluatingchoicesto
decidethenextcourseofaction,aswellaslookingaheadorbacktrackingwhen
| necessarytomakeglobalchoices. |     |     |     | OurexperimentsshowthatToTsignificantly |     |     |     |     |
| ----------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
enhanceslanguagemodels’problem-solvingabilitiesonthreenoveltasksrequiring
non-trivialplanningorsearch:Gameof24,CreativeWriting,andMiniCrosswords.
Forinstance,inGameof24,whileGPT-4withchain-of-thoughtpromptingonly
| solved4%oftasks,ourmethodachievedasuccessrateof74%. |                                                       |     |     |     |     |     | Coderepowithall |     |
| --------------------------------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
| prompts:                                            | https://github.com/princeton-nlp/tree-of-thought-llm. |     |     |     |     |     |                 |     |
1 Introduction
Originallydesignedtogeneratetext,scaled-upversionsoflanguagemodels(LMs)suchasGPT[25,
26,1,23]andPaLM[5]havebeenshowntobeincreasinglycapableofperforminganeverwider
range of tasks requiring mathematical, symbolic, commonsense, and knowledge reasoning. It is
perhapssurprisingthatunderlyingallthisprogressisstilltheoriginalautoregressivemechanismfor
generatingtext,whichmakestoken-leveldecisionsonebyoneandinaleft-to-rightfashion. Issuch
asimplemechanismsufficientforaLMtobebuilttowardageneralproblemsolver? Ifnot,what
problemswouldchallengethecurrentparadigm,andwhatshouldbealternativemechanisms?
Theliteratureonhumancognitionprovidessomecluestoanswerthesequestions. Researchon“dual
process”modelssuggeststhatpeoplehavetwomodesinwhichtheyengagewithdecisions–afast,
automatic,unconsciousmode(“System1”)andaslow,deliberate,consciousmode(“System2”)
[30, 31, 16, 15]. These two modes have previously been connected to a variety of mathematical
modelsusedinmachinelearning. Forexample,researchonreinforcementlearninginhumansand
otheranimalshasexploredthecircumstancesunderwhichtheyengageinassociative“modelfree”
learningormoredeliberative“modelbased”planning[7]. Thesimpleassociativetoken-levelchoices
ofLMsarealsoreminiscentof“System1”,andthusmightbenefitfromaugmentationbyamore
deliberate“System2”planningprocessthat(1)maintainsandexploresdiversealternativesforcurrent
37thConferenceonNeuralInformationProcessingSystems(NeurIPS2023).

(cid:41)(cid:76)(cid:91)(cid:3)(cid:70)(cid:82)(cid:79)(cid:82)(cid:85)(cid:3)(cid:11)(cid:69)(cid:92)(cid:3)(cid:60)(cid:88)(cid:84)(cid:76)(cid:68)(cid:81)(cid:12)
(cid:48)(cid:68)(cid:85)(cid:78)(cid:3)(cid:71)(cid:76)(cid:73)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)(cid:3)(cid:69)(cid:92)(cid:3)(cid:70)(cid:82)(cid:79)(cid:82)(cid:85)
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:740)(cid:740)(cid:669)(cid:740)(cid:411)(cid:270)(cid:309)(cid:361)(cid:264)(cid:270)(cid:412)
(cid:671)(cid:671) (cid:671)(cid:671) (cid:671)(cid:671)
(cid:671)(cid:671)
(cid:671)(cid:671)
(cid:97)(cid:202)(cid:288)(cid:309)(cid:343)(cid:403)(cid:356)(cid:390)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)
(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:740)(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:740)(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412)
(cid:689)(cid:202)(cid:690)(cid:740)(cid:71)(cid:106) (cid:689)(cid:230)(cid:690)(cid:740)(cid:29)(cid:309)(cid:201) (cid:689)(cid:231)(cid:690)(cid:740)(cid:29)(cid:309)(cid:201)(cid:705)(cid:146)(cid:29) (cid:689)(cid:237)(cid:690)(cid:740)(cid:201)(cid:309)(cid:201)(cid:740)(cid:689)(cid:309)(cid:361)(cid:343)(cid:349)(cid:690)
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412)
(cid:740)(cid:740)(cid:411)(cid:270)(cid:309)(cid:361)(cid:264)(cid:270)(cid:412)
(cid:671)(cid:671) (cid:671)(cid:671) (cid:671)(cid:671)
(cid:671)(cid:671)
(cid:671)(cid:671)
(cid:97)(cid:202)(cid:288)(cid:309)(cid:343)(cid:403)(cid:356)(cid:390)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)
(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:740)(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412) (cid:740)(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412)
(cid:689)(cid:202)(cid:690)(cid:740)(cid:71)(cid:302)(cid:340)(cid:361)(cid:412)(cid:705)(cid:106)(cid:361)(cid:412)(cid:340)(cid:361)(cid:412)(cid:740) (cid:689)(cid:231)(cid:690)(cid:740)(cid:29)(cid:270)(cid:202)(cid:273)(cid:302)(cid:740)(cid:309)(cid:409)(cid:740)(cid:154)(cid:270)(cid:309)(cid:361)(cid:264)(cid:270)(cid:412)(cid:740) (cid:689)(cid:231)(cid:690)(cid:740)(cid:146)(cid:242)(cid:294)(cid:409)(cid:740)(cid:29)(cid:309)(cid:302)(cid:349)(cid:403)(cid:349)(cid:356)(cid:242)(cid:302)(cid:231)(cid:390)(cid:740)
(cid:689)(cid:237)(cid:690)(cid:740)(cid:201)(cid:343)(cid:242)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740)(cid:154)(cid:270)(cid:309)(cid:361)(cid:264)(cid:270)(cid:356)(cid:349)(cid:740)(cid:689)(cid:201)(cid:309)(cid:201)(cid:690)
(cid:137)(cid:343)(cid:309)(cid:301)(cid:340)(cid:412)(cid:273)(cid:302)(cid:264)(cid:740)(cid:689)(cid:71)(cid:106)(cid:690) (cid:137)(cid:343)(cid:309)(cid:301)(cid:340)(cid:412)(cid:273)(cid:302)(cid:264)(cid:740)(cid:689)(cid:29)(cid:309)(cid:201)(cid:690) (cid:384)(cid:403)(cid:412)(cid:270)(cid:740)(cid:29)(cid:309)(cid:201)(cid:740)(cid:689)(cid:29)(cid:309)(cid:201)(cid:705)(cid:146)(cid:29)(cid:690)
Figure1: SchematicillustratingvariousapproachestoproblemsolvingwithLLMs. Eachrectangle
box represents a thought, which is a coherent language sequence that serves as an intermediate
steptowardproblemsolving. Seeconcreteexamplesofhowthoughtsaregenerated,evaluated,and
searchedinFigures2,4,6.
choicesinsteadofjustpickingone,and(2)evaluatesitscurrentstatusandactivelylooksaheador
backtrackstomakemoreglobaldecisions.
Todesignsuchaplanningprocess,wereturntotheoriginsofartificialintelligence(andcognitive
science),drawinginspirationfromtheplanningprocessesexploredbyNewell,Shaw,andSimon
startinginthe1950s[21,22]. Newellandcolleaguescharacterizedproblemsolving[21]assearch
throughacombinatorialproblemspace,representedasatree. WethusproposetheTreeofThoughts
(ToT)frameworkforgeneralproblemsolvingwithlanguagemodels. AsFigure1illustrates,while
existingmethods(detailedbelow)samplecontinuouslanguagesequencesforproblemsolving,ToT
activelymaintainsatreeofthoughts,whereeachthoughtisacoherentlanguagesequencethatserves
asanintermediatesteptowardproblemsolving(Table1). Suchahigh-levelsemanticunitallowsthe
LMtoself-evaluatetheprogressdifferentintermediatethoughtsmaketowardssolvingtheproblem
through a deliberate reasoning process that is also instantiated in language (Figures 2,4,6). This
implementationofsearchheuristicsviaLMself-evaluationanddeliberationisnovel,asprevious
search heuristics are either programmed or learned. Finally, we combine this language-based
capabilitytogenerateandevaluatediversethoughtswithsearchalgorithms,suchasbreadth-first
search(BFS)ordepth-firstsearch(DFS),whichallowsystematicexplorationofthetreeofthoughts
withlookaheadandbacktracking.
Empirically,weproposethreenewproblemsthatchallengeexistingLMinferencemethodsevenwith
thestate-of-the-artlanguagemodel,GPT-4[23]: Gameof24,CreativeWriting,andCrosswords
(Table1). Thesetasksrequiredeductive,mathematical,commonsense,lexicalreasoningabilities,
andawaytoincorporatesystematicplanningorsearch. WeshowToTobtainssuperiorresultson
allthreetasksbybeinggeneralandflexibleenoughtosupportdifferentlevelsofthoughts,different
waystogenerateandevaluatethoughts,anddifferentsearchalgorithmsthatadapttothenatureof
differentproblems. Wealsoanalyzehowsuchchoicesaffectmodelperformancesviasystematic
ablationsanddiscussfuturedirectionstobettertrainanduseLMs.
2 Background
We first formalize some existing methods that use large language models for problem-solving,
whichourapproachisinspiredbyandlatercomparedwith. Weusep todenoteapre-trainedLM
θ
with parameters θ, and lowercase letters x,y,z,s,··· to denote a language sequence, i.e.x =
(x[1],···,x[n])whereeachx[i]isatoken,sothatp (x)=
(cid:81)n
p (x[i]|x[1...i]). Weuseuppercase
θ i=1 θ
lettersS,···todenoteacollectionoflanguagesequences.
Input-output (IO) prompting is the most common way to turn a problem input x into output
y with LM: y ∼ p (y|prompt (x)), where prompt (x) wraps input x with task instructions
θ IO IO
and/orfew-shotinput-outputexamples. Forsimplicity,letusdenotepprompt(output | input) =
θ
p (output|prompt(input)),sothatIOpromptingcanbeformulatedasy ∼pIO(y|x).
θ θ
2

Chain-of-thought (CoT) prompting [38] was proposed to address cases where the mapping of
inputxtooutputyisnon-trivial(e.g.whenxisamathquestionandyisthefinalnumericalanswer).
Thekeyideaistointroduceachainofthoughtsz ,···,z tobridgexandy, whereeachz isa
1 n i
coherentlanguagesequencethatservesasameaningfulintermediatesteptowardproblemsolving
(e.g.z couldbeanintermediateequationformathQA).TosolveproblemswithCoT,eachthought
i
z ∼ pCoT(z | x,z ) is sampled sequentially, then the output y ∼ pCoT(y|x,z ). In
i θ i 1···i−1 θ 1···n
practice, [z ,y] ∼ pCoT(z ,y|x) is sampled as a continuous language sequence, and the
1···n θ 1···n
decompositionofthoughts(e.g.iseachz aphrase,asentence,oraparagraph)isleftambiguous.
i
Self-consistency with CoT (CoT-SC) [36] is an ensemble approach that samples k i.i.d.chains
of thought: [z(i) ,y(i)] ∼ pCoT(z ,y|x) (i = 1···k), then returns the most frequent output:
1···n θ 1···n
argmax #{i | y(i) = y}. CoT-SC improves upon CoT, because there are generally different
y
thoughtprocessesforthesameproblem(e.g.differentwaystoprovethesametheorem), andthe
outputdecisioncanbemorefaithfulbyexploringarichersetofthoughts. However,withineach
chainthereisnolocalexplorationofdifferentthoughtsteps,andthe“mostfrequent”heuristiconly
applieswhentheoutputspaceislimited(e.g.multi-choiceQA).
3 TreeofThoughts: DeliberateProblemSolvingwithLM
Agenuineproblem-solvingprocessinvolvestherepeateduseofavailableinforma-
tiontoinitiateexploration,whichdiscloses,inturn,moreinformationuntilaway
toattainthesolutionisfinallydiscovered.——Newelletal.[21]
Researchonhumanproblem-solvingsuggeststhatpeoplesearchthroughacombinatorialproblem-
space–atreewherethenodesrepresentpartialsolutions,andthebranchescorrespondtooperators
thatmodifythem[21,22]. Whichbranchtotakeisdeterminedbyheuristicsthathelptonavigatethe
problem-spaceandguidetheproblem-solvertowardsasolution. Thisperspectivehighlightstwokey
shortcomingsofexistingapproachesthatuseLMstosolvegeneralproblems: 1)Locally,theydonot
exploredifferentcontinuationswithinathoughtprocess–thebranchesofthetree. 2)Globally,they
donotincorporateanytypeofplanning,lookahead,orbacktrackingtohelpevaluatethesedifferent
options–thekindofheuristic-guidedsearchthatseemscharacteristicofhumanproblem-solving.
Toaddresstheseshortcomings,weintroduceTreeofThoughts(ToT),aparadigmthatallowsLMsto
exploremultiplereasoningpathsoverthoughts(Figure1(c)). ToTframesanyproblemasasearch
overatree,whereeachnodeisastates=[x,z ]representingapartialsolutionwiththeinputand
1···i
thesequenceofthoughtssofar. AspecificinstantiationofToTinvolvesansweringfourquestions:
1. Howtodecomposetheintermediateprocessintothoughtsteps; 2. Howtogeneratepotential
thoughtsfromeachstate;3. Howtoheuristicallyevaluatestates;4. Whatsearchalgorithmtouse.
1.Thoughtdecomposition. WhileCoTsamplesthoughtscoherentlywithoutexplicitdecomposition,
ToTleveragesproblempropertiestodesignanddecomposeintermediatethoughtsteps. AsTable1
shows,dependingondifferentproblems,athoughtcouldbeacoupleofwords(Crosswords),alineof
equation(Gameof24),orawholeparagraphofwritingplan(CreativeWriting). Ingeneral,athought
shouldbe“small”enoughsothatLMscangeneratepromisinganddiversesamples(e.g.generating
awholebookisusuallytoo“big”tobecoherent),yet“big”enoughsothatLMscanevaluateits
prospecttowardproblemsolving(e.g.generatingonetokenisusuallytoo“small”toevaluate).
2.ThoughtgeneratorG(p ,s,k). Givenatreestates = [x,z ],weconsidertwostrategiesto
θ 1···i
generatekcandidatesforthenextthoughtstep:
(a) Sample i.i.d.thoughts from a CoT prompt (Creative Writing, Figure 4): z(j) ∼
pCoT(z |s) = pCoT(z |x,z ) (j = 1···k). This works better when the thought
θ i+1 θ i+1 1···i
spaceisrich(e.g.eachthoughtisaparagraph),andi.i.d.samplesleadtodiversity;
(b) Proposethoughtssequentiallyusinga“proposeprompt”(Gameof24,Figure2;Crosswords,
Figure 6): [z(1),···,z(k)] ∼ ppropose(z(1···k) | s). This works better when the thought
θ i+1
spaceismoreconstrained(e.g.eachthoughtisjustawordoraline),soproposingdifferent
thoughtsinthesamecontextavoidsduplication.
3.StateevaluatorV(p ,S). Givenafrontierofdifferentstates,thestateevaluatorevaluatesthe
θ
progress they make towards solving the problem, serving as a heuristic for the search algorithm
to determine which states to keep exploring and in which order. While heuristics are a standard
approachtosolvingsearchproblems,theyaretypicallyeitherprogrammed(e.g.DeepBlue[3])or
3

learned(e.g.AlphaGo[29]). Weproposeathirdalternative,byusingtheLMtodeliberatelyreason
aboutstates. Whenapplicable,suchadeliberateheuristiccanbemoreflexiblethanprogrammed
rules,andmoresample-efficientthanlearnedmodels. Similartothethoughtgenerator,weconsider
twostrategiestoevaluatestateseitherindependentlyortogether:
(a) Value each state independently: V(p ,S)(s) ∼ pvalue(v|s) ∀s ∈ S, where a value
|     |     |     |     | θ   | θ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
prompt reasons about the state s to generate a scalar value v (e.g.1-10) or a classifica-
tion(e.g.sure/likely/impossible)thatcouldbeheuristicallyturnedintoavalue. Thebasis
ofsuchevaluativereasoningcanvaryacrossproblemsandthoughtsteps. Inthiswork,we
exploreevaluationviafewlookahead simulations(e.g.quicklyconfirmthat5,5,14can
reach24via5+5+14,or“hot l”canmean“inn”viafilling“e”in“ ”)pluscommonsense
(e.g.123aretoosmalltoreach24,ornowordcanstartwith“tzxc”). Whiletheformer
mightpromote“good”states,thelattercouldhelpeliminate“bad”states. Suchvaluations
donotneedtobeperfect,andonlyneedtobeapproximatelyhelpfulfordecisionmaking.
1[s
(b) Voteacrossstates: V(p ,S)(s) = = s∗], wherea“good”states∗ ∼ pvote(s∗|S)is
|     |     | θ   |     |     |     |     | θ   |
| --- | --- | --- | --- | --- | --- | --- | --- |
votedoutbasedondeliberatelycomparingdifferentstatesinS inavoteprompt. When
problemsuccessishardertodirectlyvalue(e.g.passagecoherency),itisnaturaltotoinstead
comparedifferentpartialsolutionsandvoteforthemostpromisingone. Thisissimilar
inspirittoa“step-wise”self-consistencystrategy, i.e.cast“whichstatetoexplore”asa
multi-choiceQA,anduseLMsamplestovoteforit.
Forbothstrategies,wecouldprompttheLMmultipletimestoaggregatethevalueorvoteresultsto
tradetime/resource/costformorefaithful/robustheuristics.
Algorithm1ToT-BFS(x,p θ ,G,k,V,T,b) Algorithm2ToT-DFS(s,t,p ,G,k,V,T,v )
|     |     |     |     |     |     | θ   | th  |
| --- | --- | --- | --- | --- | --- | --- | --- |
Require: Inputx,LMp ,thoughtgeneratorG()Require: Currentstates,stept,LMp
|     |     | θ   |     |     |     |     | θ ,thought |
| --- | --- | --- | --- | --- | --- | --- | ---------- |
&sizelimitk,statesevaluatorV(),steplimitT,
generatorG()andsizelimitk,statesevaluator
| breadthlimitb. |     |     |     | V(),steplimitT,thresholdv |     |     |     |
| -------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
th
| S ←{x}       |     |     |     | ift>T | thenrecordoutputG(p |     | ,s,1) |
| ------------ | --- | --- | --- | ----- | ------------------- | --- | ----- |
| 0            |     |     |     |       |                     |     | θ     |
| fort=1,···,T | do  |     |     | endif |                     |     |       |
S ′ ←{[s,z]|s∈S ,z ∈G(p ,s,k)} fors′ ∈G(p ,s,k) do ▷sortedcandidates
| t      |       | t−1 t | θ   |     | θ           |       |               |
| ------ | ----- | ----- | --- | --- | ----------- | ----- | ------------- |
| V ←V(p | ,S ′) |       |     |     | ,{s′})(s)>v |       |               |
| t      | θ t   |       |     |     | ifV(p θ     | thres | then ▷pruning |
(cid:80)
| S t ←argmax | S⊂S     | ′,|S|=b  | V t (s) |        | DFS(s′,t+1) |     |     |
| ----------- | ------- | -------- | ------- | ------ | ----------- | --- | --- |
|             |         | t        | s∈S     |        |             |     |     |
| endfor      |         |          |         |        | endif       |     |     |
| returnG(p   | ,argmax | V (s),1) |         | endfor |             |     |     |
|             | θ       | s∈ST T   |         |        |             |     |     |
4. Searchalgorithm. Finally,withintheToTframework,onecanplugandplaydifferentsearch
algorithmsdependingonthetreestructure. Weexploretworelativelysimplesearchalgorithmsand
leavemoreadvancedones(e.g.A*[11],MCTS[2])forfuturework:
(a) Breadth-firstsearch(BFS)(Algorithm1)maintainsasetofthebmostpromisingstates
perstep. ThisisusedforGameof24andCreativeWritingwherethetreedepthislimit
(T ≤3),andinitialthoughtstepscanbeevaluatedandprunedtoasmallset(b≤5).
(b) Depth-firstsearch(DFS)(Algorithm2)exploresthemostpromisingstatefirst,untilthe
final output is reached (t > T), or the state evaluator deems it impossible to solve the
problemfromthecurrents(V(p ,{s})(s) ≤ v foravaluethresholdv ). Inthelatter
|     |     |     | θ   |     | th  |     | th  |
| --- | --- | --- | --- | --- | --- | --- | --- |
case,thesubtreefromsisprunedtotradeexplorationforexploitation. Inbothcases,DFS
backtrackstotheparentstateofstocontinueexploration.
Conceptually,ToThasseveralbenefitsasamethodforgeneralproblem-solvingwithLMs: (1)Gener-
ality. IO,CoT,CoT-SC,andself-refinementcanbeseenasspecialcasesofToT(i.e. treesoflimited
depthandbreadth;Figure1). (2)Modularity. ThebaseLM,aswellasthethoughtdecomposition,
generation, evaluation, and search procedures can all be varied independently. (3) Adaptability.
Differentproblemproperties,LMcapabilities,andresourceconstraintscanbeaccommodated. (4)
Convenience. Noextratrainingisneeded,justapre-trainedLMissufficient. Thenextsectionwill
showhowtheseconceptualbenefitstranslatetostrongempiricalperformanceindifferentproblems.
4 Experiments
Weproposethreetasksthatarehardevenwhensamplingfromthestate-of-the-artlanguagemodel,
GPT-4 [23], using standard IO prompting or chain-of-thought (CoT) prompting. We show how
4

|     | Gameof24 |     |     |     | CreativeWriting |     | 5x5Crosswords |     |
| --- | -------- | --- | --- | --- | --------------- | --- | ------------- | --- |
Input 4numbers(491013) 4randomsentences 10clues(h1.presented;..)
|     | An  | equation | to reach | 24  | Apassageof4paragraphs |     | 5x5 letters: | SHOWN; |
| --- | --- | -------- | -------- | --- | --------------------- | --- | ------------ | ------ |
Output
|     | (13-9)*(10-4)=24 |     |     |     | endinginthe4sentences |     | WIRRA;AVAIL;... |     |
| --- | ---------------- | --- | --- | --- | --------------------- | --- | --------------- | --- |
Thoughts 3 intermediate equations A short writing plan Wordstofillinforclues:
|     | (13-9=4(left4,4,10); |     |     | 10- | (1.Introduce | a book that | (h1.shown;v5.naled;...) |     |
| --- | -------------------- | --- | --- | --- | ------------ | ----------- | ----------------------- | --- |
|     | 4=6(left4,6);4*6=24) |     |     |     | connects...) |             |                         |     |
#To(cid:689)T(cid:202)(cid:690)steps(cid:71)(cid:302)(cid:340)(cid:361)(cid:412)(cid:669)(cid:740)(cid:641)3(cid:740)(cid:646)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640) (cid:689)(cid:230)(cid:690) (cid:51)(cid:85)(cid:82)(cid:83)(cid:82)(cid:86)(cid:72)(cid:3)(cid:51)(cid:85)(cid:82)(cid:80)1(cid:83)(cid:87) 5-1(cid:55)0(cid:75)(cid:82)((cid:88)v(cid:74)a(cid:75)(cid:87)ri(cid:3)a(cid:42)b(cid:72)(cid:81)le(cid:72)(cid:85))(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)
|                                                        | Table1:                                                | Tasko(cid:691)     | (cid:309) v(cid:302) (cid:242) e(cid:740)                                                                                                                                                                       | (cid:242)r (cid:389) v(cid:202) (cid:301)i e (cid:340) (cid:294)w(cid:242) (cid:692) (cid:740).            | Input,output,though(cid:47)t(cid:48)examplesar(cid:641) |     | e(cid:740)(cid:780) (cid:740)(cid:646) i (cid:740)n(cid:784) (cid:740)(cid:638) (cid:640) b(cid:740) (cid:689) (cid:294) l(cid:242) u(cid:409) (cid:412) (cid:669) e(cid:740) (cid:638) (cid:637).            | (cid:740)(cid:638) (cid:640) (cid:740)(cid:638) (cid:640)(cid:690) |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
|                                                        |                                                        |                    | (cid:71) (cid:302) (cid:340) (cid:361) (cid:412)                                                                                                                                                                | (cid:669)(cid:740) (cid:641) (cid:740)(cid:646) (cid:740) (cid:638) (cid:637) (cid:740)(cid:638) (cid:640) |                                                         |     | (cid:638)(cid:637) (cid:740)(cid:714) (cid:740) (cid:641) (cid:740)(cid:784) (cid:740) (cid:643) (cid:740) (cid:689) (cid:294) (cid:242) (cid:409) (cid:412) (cid:669) (cid:740) (cid:643) (cid:740)(cid:646) | (cid:740) (cid:638)(cid:640) (cid:690)                             |
| (cid:641)(cid:780)(cid:646)(cid:784)(cid:638)(cid:640) | (cid:638)(cid:637)(cid:705)(cid:641)(cid:784)(cid:643) | (cid:671)(cid:671) | (cid:137)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)(cid:740)(cid:302)(cid:242)(cid:389)(cid:412)(cid:740)(cid:349)(cid:356)(cid:242)(cid:340)(cid:349)(cid:669)(cid:740)(cid:740)(cid:740) |                                                                                                            |                                                         |     | (cid:691)(cid:667)(cid:667)(cid:667)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740)(cid:294)(cid:273)(cid:302)(cid:242)(cid:349)(cid:671)(cid:692)                                                              |                                                                    |
(cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)(cid:740)(cid:638)(cid:640)(cid:690) (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:643)(cid:740)(cid:646)(cid:740)(cid:638)(cid:640)(cid:690)
deliberatesearchintreesofthoughts(ToT)producesbetterresults,andmoreimportantly,interesting
andpr(cid:638)(cid:640)o(cid:705)(cid:643)m(cid:784)(cid:644)ising(cid:638)(cid:640)(cid:705)(cid:646)n(cid:784)(cid:641)eww(cid:671)a(cid:671)ys(cid:689)t(cid:231)o(cid:690) usela(cid:57)n(cid:68)(cid:79)g(cid:88)u(cid:72)a(cid:3)(cid:51)g(cid:85)e(cid:82)(cid:80)m(cid:83)(cid:87)odelstosolveproblemsrequi(cid:55)r(cid:75)i(cid:82)n(cid:88)g(cid:74)(cid:75)s(cid:87)e(cid:3)a(cid:40)(cid:89)r(cid:68)c(cid:79)h(cid:88)(cid:68)o(cid:87)r(cid:76)(cid:82)p(cid:81)lanning.
Unless(cid:689)(cid:294)(cid:242)(cid:409)(cid:412)o(cid:669)(cid:740)(cid:644)(cid:740)(cid:646)t(cid:690)herw(cid:689)(cid:294)(cid:242)i(cid:409)(cid:412)(cid:669)s(cid:740)(cid:641)(cid:740)(cid:643)e(cid:690) (cid:41)(cid:383) (cid:202) (cid:294)(cid:361) (cid:202) (cid:356)(cid:242) (cid:740)(cid:273)(cid:409) (cid:740)(cid:264)(cid:403)(cid:383)(cid:242) (cid:302)(cid:740) (cid:302)(cid:361) (cid:301) (cid:230)(cid:242) (cid:343) (cid:349) (cid:740)(cid:231)(cid:202)(cid:302) (cid:740) ntsusingaChatComplet(cid:689)(cid:638)i(cid:640)o(cid:740)(cid:714)(cid:740)n(cid:638)(cid:637)(cid:690)(cid:740)m(cid:678)(cid:740)(cid:638)(cid:640)o(cid:740)(cid:784)(cid:740)d(cid:640)(cid:740)e(cid:678)(cid:740)(cid:638)(cid:640)G(cid:740)(cid:784)(cid:740)(cid:640)P(cid:646)T-41
|                           |     | stated, | wep (cid:343)(cid:242)(cid:202)(cid:231)(cid:270)(cid:740)(cid:639)(cid:641)(cid:740)(cid:689)(cid:349)(cid:361)(cid:343)(cid:242)(cid:683)(cid:294)(cid:273)(cid:291)(cid:242)(cid:294)(cid:390)(cid:683)(cid:273)(cid:301)(cid:340)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)(cid:690) e r | f o r m e x | p e r i m e |                  |                                                                                                                                                           | witha |
| ------------------------- | --- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
|                           |     |         |                                                                                                                                                                                                                                                                                                                   |             |             | (cid:47)(cid:48) | (cid:638)(cid:637)(cid:740)(cid:780)(cid:740)(cid:638)(cid:640)(cid:740)(cid:780)(cid:740)(cid:638)(cid:640)(cid:740)(cid:784)(cid:740)(cid:640)(cid:643) |       |
| samplingtemperatureof0.7. |     |         | (cid:638)(cid:637)(cid:740)(cid:638)(cid:641)(cid:669)(cid:740)(cid:638)(cid:637)(cid:740)(cid:780)(cid:740)(cid:638)(cid:641)(cid:740)(cid:784)(cid:740)(cid:639)(cid:641)(cid:667)(cid:740)(cid:349)(cid:361)(cid:343)(cid:242)                                                                                 |             |             |                  |                                                                                                                                                           |       |
(cid:641)(cid:780)(cid:643)(cid:784)(cid:638)(cid:637) (cid:641)(cid:678)(cid:643)(cid:784)(cid:639)(cid:641) (cid:671)(cid:671) (cid:691)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740)(cid:242)(cid:389)(cid:202)(cid:301)(cid:340)(cid:294)(cid:242)(cid:349)(cid:692) (cid:154)(cid:270)(cid:242)(cid:343)(cid:242)(cid:740)(cid:403)(cid:349)(cid:740)(cid:302)(cid:309)(cid:740)(cid:384)(cid:202)(cid:390)(cid:740)(cid:408)(cid:309)(cid:740)(cid:309)(cid:230)(cid:356)(cid:202)(cid:273)(cid:302)(cid:740)(cid:639)(cid:641)(cid:740)(cid:384)(cid:403)(cid:412)(cid:270)(cid:740)
| (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:638)(cid:637)(cid:690) | (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:639)(cid:641)(cid:690) |     |     |     |     |     | (cid:411)(cid:270)(cid:242)(cid:349)(cid:242)(cid:740)(cid:302)(cid:361)(cid:301)(cid:230)(cid:242)(cid:343)(cid:349)(cid:667)(cid:740)(cid:273)(cid:301)(cid:340)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242) |     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)(cid:740)(cid:638)(cid:640)
4.1 Gameof24
Game(cid:41)of(cid:76)(cid:91)2(cid:3)(cid:70)4(cid:82)is(cid:79)(cid:82)a(cid:85)(cid:3)m(cid:11)(cid:69)a(cid:92)th(cid:3)(cid:60)em(cid:88)(cid:84)at(cid:76)i(cid:68)c(cid:81)al(cid:12)reasoningchallenge,wherethegoalistouse4numbersandbasic
arithmeticoperations(+-*/)toobtain24. Forexample,giveninput“491013”,asolutionoutput
(cid:48)(cid:68)(cid:85)(cid:78)(cid:3)(cid:71)(cid:76)(cid:73)(cid:73)(cid:3)(cid:83)(cid:85)(cid:82)(cid:80)(cid:83)(cid:87)(cid:3)(cid:90)(cid:76)(cid:87)(cid:75)(cid:3)(cid:70)(cid:82)(cid:79)(cid:82)(cid:85)
couldbe“(10-4)*(13-9)=24”.
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412)(cid:669)(cid:740)(cid:641)(cid:740)(cid:646)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)
|                    |                                                                                                                                |                                                                                                                                                  |                                                                                                                                                                                                                 | (cid:11)(cid:68)(cid:12)(cid:3)(cid:51)(cid:85)(cid:82)(cid:83)(cid:82)(cid:86)(cid:72)(cid:3)(cid:51)(cid:85)(cid:82)(cid:80)(cid:83)(cid:87) |     |                  | (cid:55)(cid:75)(cid:82)(cid:88)(cid:74)(cid:75)(cid:87)(cid:3)(cid:42)(cid:72)(cid:81)(cid:72)(cid:85)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)                                                                                                     |     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|                    |                                                                                                                                |                                                                                                                                                  | (cid:691)(cid:309)(cid:302)(cid:242)(cid:740)(cid:242)(cid:389)(cid:202)(cid:301)(cid:340)(cid:294)(cid:242)(cid:692)(cid:740)                                                                                  |                                                                                                                                                |     |                  | (cid:641)(cid:740)(cid:780)(cid:740)(cid:646)(cid:740)(cid:784)(cid:740)(cid:638)(cid:640)(cid:740)(cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)(cid:740)(cid:638)(cid:640)(cid:690) |     |
|                    |                                                                                                                                |                                                                                                                                                  | (cid:71)(cid:302)(cid:340)(cid:361)(cid:412)(cid:669)(cid:740)(cid:641)(cid:740)(cid:646)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)                                                                 |                                                                                                                                                |     | (cid:47)(cid:48) | (cid:638)(cid:637)(cid:740)(cid:714)(cid:740)(cid:641)(cid:740)(cid:784)(cid:740)(cid:643)(cid:740)(cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:643)(cid:740)(cid:646)(cid:740)(cid:638)(cid:640)(cid:690)                   |     |
| (cid:671)(cid:671) | (cid:638)(cid:637)(cid:705)(cid:641)(cid:784)(cid:643)                                                                         | (cid:641)(cid:780)(cid:646)(cid:784)(cid:638)(cid:640)                                                                                           | (cid:137)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)(cid:740)(cid:302)(cid:242)(cid:389)(cid:412)(cid:740)(cid:349)(cid:356)(cid:242)(cid:340)(cid:349)(cid:669)(cid:740)(cid:740)(cid:740) |                                                                                                                                                |     |                  | (cid:691)(cid:667)(cid:667)(cid:667)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740)(cid:294)(cid:273)(cid:302)(cid:242)(cid:349)(cid:671)(cid:692)                                                                                                    |     |
|                    | (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:643)(cid:740)(cid:646)(cid:740)(cid:638)(cid:640)(cid:690) | (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:638)(cid:637)(cid:740)(cid:638)(cid:640)(cid:740)(cid:638)(cid:640)(cid:690) |                                                                                                                                                                                                                 |                                                                                                                                                |     |                  |                                                                                                                                                                                                                                                     |     |
(cid:638)(cid:640)(cid:705)(cid:643)(cid:784)(cid:644) (cid:638)(cid:640)(cid:705)(cid:646)(cid:784)(cid:641) (cid:671)(cid:671) (cid:11)(cid:69)(cid:12)(cid:3)(cid:57)(cid:68)(cid:79)(cid:88)(cid:72)(cid:3)(cid:51)(cid:85)(cid:82)(cid:80)(cid:83)(cid:87) (cid:55)(cid:75)(cid:82)(cid:88)(cid:74)(cid:75)(cid:87)(cid:3)(cid:40)(cid:89)(cid:68)(cid:79)(cid:88)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)
(cid:41)(cid:383)(cid:202)(cid:294)(cid:361)(cid:202)(cid:356)(cid:242)(cid:740)(cid:273)(cid:409)(cid:740)(cid:264)(cid:403)(cid:383)(cid:242)(cid:302)(cid:740)(cid:302)(cid:361)(cid:301)(cid:230)(cid:242)(cid:343)(cid:349)(cid:740)(cid:231)(cid:202)(cid:302)(cid:740)
| (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:644)(cid:740)(cid:646)(cid:690) | (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:641)(cid:740)(cid:643)(cid:690) |     |                                                                                                                                                                                                                                                                                                           |     |     |                  | (cid:689)(cid:638)(cid:640)(cid:740)(cid:714)(cid:740)(cid:638)(cid:637)(cid:690)(cid:740)(cid:678)(cid:740)(cid:638)(cid:640)(cid:740)(cid:784)(cid:740)(cid:640)(cid:740)(cid:678)(cid:740)(cid:638)(cid:640)(cid:740)(cid:784)(cid:740)(cid:640)(cid:646)                                                       |     |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
|                                                                                                     |                                                                                                     |     | (cid:343)(cid:242)(cid:202)(cid:231)(cid:270)(cid:740)(cid:639)(cid:641)(cid:740)(cid:689)(cid:349)(cid:361)(cid:343)(cid:242)(cid:683)(cid:294)(cid:273)(cid:291)(cid:242)(cid:294)(cid:390)(cid:683)(cid:273)(cid:301)(cid:340)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)(cid:690) |     |     | (cid:47)(cid:48) | (cid:638)(cid:637)(cid:740)(cid:780)(cid:740)(cid:638)(cid:640)(cid:740)(cid:780)(cid:740)(cid:638)(cid:640)(cid:740)(cid:784)(cid:740)(cid:640)(cid:643)(cid:740)(cid:154)(cid:270)(cid:242)(cid:343)(cid:242)(cid:740)(cid:403)(cid:349)(cid:740)(cid:302)(cid:309)(cid:740)(cid:384)(cid:202)(cid:390)(cid:740) |     |
(cid:638)(cid:637)(cid:740)(cid:638)(cid:641)(cid:669)(cid:740)(cid:638)(cid:637)(cid:740)(cid:780)(cid:740)(cid:638)(cid:641)(cid:740)(cid:784)(cid:740)(cid:639)(cid:641)(cid:667)(cid:740)(cid:349)(cid:361)(cid:343)(cid:242)
| (cid:641)(cid:780)(cid:643)(cid:784)(cid:638)(cid:637)                                     | (cid:641)(cid:678)(cid:643)(cid:784)(cid:639)(cid:641)                                     |                    |                                                                                                                                         |     |     |     | (cid:408)(cid:309)(cid:740)(cid:309)(cid:230)(cid:356)(cid:202)(cid:273)(cid:302)(cid:740)(cid:639)(cid:641)(cid:740)(cid:384)(cid:403)(cid:412)(cid:270)(cid:740)(cid:411)(cid:270)(cid:242)(cid:349)(cid:242)(cid:740)(cid:230)(cid:403)(cid:264)(cid:740) |     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
|                                                                                            |                                                                                            | (cid:671)(cid:671) | (cid:691)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740)(cid:242)(cid:389)(cid:202)(cid:301)(cid:340)(cid:294)(cid:242)(cid:349)(cid:692) |     |     |     |                                                                                                                                                                                                                                                              |     |
| (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:638)(cid:637)(cid:690) | (cid:689)(cid:294)(cid:242)(cid:409)(cid:412)(cid:669)(cid:740)(cid:639)(cid:641)(cid:690) |                    | (cid:638)(cid:637)(cid:740)(cid:638)(cid:640)(cid:740)(cid:638)(cid:640)                                                                |     |     |     | (cid:302)(cid:361)(cid:301)(cid:230)(cid:242)(cid:343)(cid:349)(cid:667)(cid:740)(cid:273)(cid:301)(cid:340)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)                                                                                  |     |
Figure2: ToTinagameof24. TheLMispromptedfor(a)thoughtgenerationand(b)valuation.
TaskSetup. Wescrapedatafrom4nums.com,whichhas1,362gamesthataresortedfromeasyto
hardbyhumansolvingtime,anduseasubsetofrelativelyhardgamesindexed901-1,000fortesting.
Foreachtask,weconsidertheoutputassuccessifitisavalidequationthatequals24andusesthe
inputnumberseachexactlyonce. Wereportthesuccessrateacross100gamesasthemetric.
Baselines. Weuseastandardinput-output(IO)promptwith5in-contextexamples. Forchain-of-
thought(CoT)prompting,weaugmenteachinput-outputpairwith3intermediateequations,each
operatingontworemainingnumbers. Forexample,giveninput“491013”,thethoughtscouldbe
“13-9=4(left: 4410);10-4=6(left: 46);4*6=24(left: 24)”. Foreachgame,wesampleIO
andCoTpromptingfor100timesforaverageperformance. WealsoconsideraCoTself-consistency
baseline,whichtakesthemajorityoutputfrom100CoTsamples,andaniterative-refineapproachon
topofanIOsampleforatmost10iterations. Ateachiteration,theLMisconditionedonallprevious
historyto“reflectonyourmistakesandgeneratearefinedanswer”iftheoutputisincorrect. Note
thatitusesgroundtruthfeedbacksignalsaboutequationcorrectness.
ToTSetup. ToframeGameof24 intoToT,itis natural todecomposethethoughtsinto 3steps,
eachanintermediateequation. AsshowninFigure2(a),ateachtreenode,weexacttheremaining
numbersandprompttheLMtoproposesomepossiblenextsteps. Thesame“proposeprompt”is
usedforall3thoughtsteps,thoughitonlyhasoneexamplewith4inputnumbers. Weperforma
breadth-firstsearch(BFS)inToT,whereateachstepwekeepthebestb=5candidates. Toperform
deliberateBFSinToT,asshowninFigure2(b),wepromptLMtoevaluateeachthoughtcandidateas
“sure/maybe/impossible”withregardtoreaching24. Theaimistopromotecorrectpartialsolutions
thatcanbeverdictedwithinfewlookaheadtrials,andeliminateimpossiblepartialsolutionsbasedon
“toobig/small”commonsense,andkeeptherest“maybe”. Wesamplevalues3timesforeachthought.
1ExperimentsweredonebetweenMay5-16,2023.
5

Method Success (a) Success rate with nodes visited (b) Samples failed at each step
IOprompt 7.3% CoT
ToT (b=5)
CoTprompt 4.0% 0.6 0.6
CoT-SC(k=100) 9.0%
ToT(ours)(b=1) 45%
0.4 0.4
ToT(ours)(b=5) 74%
IO+Refine(k=10) 27% 0.2 IO (best of k) 0.2
CoT (best of k)
IO(bestof100) 33%
ToT (b=1...5)
CoT(bestof100) 49% 0.0
0 25 50 75 100 1 2 3 4 Correct
Table2: Gameof24Results. Figure3: Gameof24(a)scaleanalysis&(b)erroranalysis.
Results. AsshowninTable2,IO,CoT,andCoT-SCpromptingmethodsperformbadlyonthetask,
achievingonly7.3%,4.0%,and9.0%successrates. Incontrast,ToTwithabreadthofb=1already
achievesasuccessrateof45%, whileb = 5achieves74%. Wealsoconsideranoraclesetupfor
IO/CoT,bycalculatingthesuccessrateusingbestofksamples(1≤k ≤100). TocompareIO/CoT
(bestofk)withToT,weconsidercalculatingthetreenodesvisitedpertaskinToTacrossb=1···5,
andmapthe5successratesinFigure3(a),treatingIO/CoT(bestofk)asvisitingknodesinabandit.
Notsurprisingly,CoTscalesbetterthanIO,andbestof100CoTsamplesachieveasuccessrateof
49%,butstillmuchworsethanexploringmorenodesinToT(b>1).
Erroranalysis. Figure3(b)breaksdownatwhichstepCoTandToTsamplesfailthetask,i.e.the
thought(inCoT)orallbthoughts(inToT)areinvalidorimpossibletoreach24. Notably,around
60%ofCoTsamplesalreadyfailedthetaskaftergeneratingthefirststep,orequivalently,thefirst
threewords(e.g.“4+9”). Thishighlightstheissueswithdirectleft-to-rightdecoding.
4.2 Creativewriting
Next,weinventacreativewritingtaskwheretheinputis4randomsentencesandtheoutputshould
beacoherentpassagewith4paragraphsthatendinthe4inputsentencesrespectively. Suchataskis
open-endedandexploratory,andchallengescreativethinkingaswellashigh-levelplanning.
Tasksetup. Wesamplerandomsentencesfromrandomwordgenerator.comtoform100inputs,and
there is no groundtruth passage for each input constraint. As we find that GPT-4 can follow the
inputconstraintsmostofthetime,wefocusonevaluatingpassagecoherencyintwoways: usinga
GPT-4zero-shotprompttoprovidea1-10scalarscore,orusinghumanjudgmentstocomparepairs
ofoutputsfromdifferentmethods. Fortheformer,wesample5scoresandaveragethemforeachtask
output,andwefindthese5scoresusuallyconsistent,withastandarddeviationofaround0.56on
averageacrossoutputs. Forthelatter,weemployasubsetoftheauthorsinablindstudytocompare
thecoherencyofCoTvs.ToTgeneratedpassagepairs,wheretheorderofpassagesisrandomflipped
over100inputs.
Baselines. Giventhecreativenatureofthetask,bothIOandCoTpromptsarezero-shot. Whilethe
formerpromptstheLMtodirectlygenerateacoherentpassagegiveninputconstraints,thelatter
promptstheLMtofirstmakeabriefplanthenwritethepassage,i.e.theplanservesastheintermediate
thoughtstep. Wegenerate10IOandCoTsamplespertask. Wealsoconsideraniterative-refine
(k ≤5)methodontopofarandomIOsampleforeachtask,wheretheLMisconditionedoninput
constraintsandthelastgeneratedpassagetodecideifthepassageisalready“perfectlycoherent”,
andifnotgeneratearefinedone.
ToTsetup. WebuildaToTwithdepth2(andonly1intermediatethoughtstep)—theLMfirst
generatesk =5plansandvotesforthebestone(Figure4),thensimilarlygeneratek =5passages
basedonthebestplanthenvoteforthebestone. Herethebreadthlimitb=1,asonlyonechoiceis
keptperstep. Asimplezero-shotvoteprompt(“analyzechoicesbelow,thenconcludewhichismost
promisingfortheinstruction”)isusedtosample5votesatbothsteps.
Results. Figure5(a)showsaverageGPT-4scoresacross100tasks,whereToT(7.56)isdeemedto
generatemorecoherentpassagesthanIO(6.19)andCoT(6.93)onaverage. Whilesuchanautomatic
metricmightbenoisy,Figure5(b)confirmsthefindingbyshowingthathumanspreferToTover
CoTin41outof100passagepairs,whileonlypreferCoToverToTin21(other38pairsarefound
“similarlycoherent”). Lastly,iterative-refineismoreeffectiveonthisnaturallanguagetask,where
6

(cid:181)(cid:343)(cid:403)(cid:356)(cid:242)(cid:740)(cid:202)(cid:740)(cid:231)(cid:309)(cid:270)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740)(cid:641)(cid:740)(cid:349)(cid:270)(cid:309)(cid:343)(cid:412)(cid:740)(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:349)(cid:667)(cid:740)(cid:154)(cid:270)(cid:242)(cid:740)(cid:242)(cid:302)(cid:237)(cid:740)(cid:349)(cid:242)(cid:302)(cid:356)(cid:242)(cid:302)(cid:231)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740)(cid:242)(cid:202)(cid:231)(cid:270)(cid:740)(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:740)(cid:301)(cid:361)(cid:349)(cid:412)(cid:740)(cid:230)(cid:242)(cid:669)(cid:740)(cid:638)(cid:667)(cid:740)(cid:71)(cid:412)(cid:740)(cid:403)(cid:349)(cid:302)(cid:729)(cid:411)(cid:740)
(cid:689)(cid:202)(cid:690)(cid:740) (cid:237)(cid:273)(cid:409)(cid:409)(cid:403)(cid:231)(cid:361)(cid:294)(cid:412)(cid:740)(cid:408)(cid:309)(cid:740)(cid:237)(cid:309)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:273)(cid:409)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:288)(cid:361)(cid:349)(cid:412)(cid:740)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:309)(cid:302)(cid:740)(cid:390)(cid:309)(cid:361)(cid:343)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:667)(cid:740)(cid:639)(cid:667)(cid:740)(cid:71)(cid:412)(cid:740)(cid:231)(cid:202)(cid:361)(cid:264)(cid:270)(cid:412)(cid:740)(cid:270)(cid:273)(cid:301)(cid:740)(cid:309)(cid:409)(cid:409)(cid:740)(cid:264)(cid:361)(cid:202)(cid:343)(cid:237)(cid:740)(cid:411)(cid:270)(cid:202)(cid:412)(cid:740)(cid:349)(cid:340)(cid:202)(cid:231)(cid:242)(cid:740)(cid:349)(cid:301)(cid:242)(cid:294)(cid:294)(cid:242)(cid:237)(cid:740)(cid:309)(cid:409)(cid:740)
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:349)(cid:242)(cid:202)(cid:343)(cid:242)(cid:237)(cid:740)(cid:349)(cid:356)(cid:242)(cid:202)(cid:291)(cid:667)(cid:740)(cid:640)(cid:667)(cid:740)(cid:181)(cid:270)(cid:242)(cid:302)(cid:740)(cid:349)(cid:270)(cid:242)(cid:740)(cid:237)(cid:403)(cid:237)(cid:302)(cid:722)(cid:411)(cid:740)(cid:294)(cid:273)(cid:291)(cid:242)(cid:740)(cid:202)(cid:740)(cid:264)(cid:361)(cid:390)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:384)(cid:202)(cid:349)(cid:740)(cid:411)(cid:343)(cid:390)(cid:273)(cid:302)(cid:264)(cid:740)(cid:408)(cid:309)(cid:740)(cid:340)(cid:403)(cid:231)(cid:291)(cid:740)(cid:270)(cid:242)(cid:343)(cid:740)(cid:361)(cid:340)(cid:668)(cid:740)(cid:349)(cid:270)(cid:242)(cid:740)(cid:349)(cid:356)(cid:202)(cid:343)(cid:356)(cid:242)(cid:237)(cid:740)(cid:361)(cid:349)(cid:273)(cid:302)(cid:264)(cid:740)(cid:349)(cid:403)(cid:264)(cid:302)(cid:740)(cid:294)(cid:202)(cid:302)(cid:264)(cid:361)(cid:202)(cid:264)(cid:242)(cid:667)(cid:740)(cid:641)(cid:667)(cid:740)
(cid:41)(cid:202)(cid:231)(cid:270)(cid:740)(cid:340)(cid:242)(cid:343)(cid:349)(cid:309)(cid:302)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:291)(cid:302)(cid:309)(cid:384)(cid:349)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:270)(cid:202)(cid:349)(cid:740)(cid:202)(cid:740)(cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:309)(cid:409)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:202)(cid:343)(cid:242)(cid:667)(cid:740)(cid:740)
(cid:638) (cid:638)(cid:667)(cid:740)(cid:71)(cid:302)(cid:412)(cid:343)(cid:309)(cid:237)(cid:361)(cid:231)(cid:242)(cid:740)(cid:202)(cid:302)(cid:237)(cid:740)(cid:242)(cid:389)(cid:340)(cid:294)(cid:202)(cid:273)(cid:302)(cid:740)(cid:411)(cid:270)(cid:242)(cid:740)(cid:408)(cid:242)(cid:231)(cid:270)(cid:302)(cid:403)(cid:342)(cid:361)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740) (cid:639) (cid:638)(cid:667)(cid:740)(cid:71)(cid:302)(cid:412)(cid:343)(cid:309)(cid:237)(cid:361)(cid:231)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:302)(cid:740)(cid:361)(cid:302)(cid:361)(cid:349)(cid:361)(cid:202)(cid:294)(cid:740)(cid:349)(cid:242)(cid:294)(cid:409)(cid:714)(cid:270)(cid:242)(cid:294)(cid:340)(cid:740)(cid:230)(cid:309)(cid:309)(cid:291)(cid:668)(cid:740)
(cid:689)(cid:230)(cid:690)(cid:740) (cid:237)(cid:309)(cid:273)(cid:302)(cid:264)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:639)(cid:667)(cid:740)(cid:146)(cid:384)(cid:403)(cid:356)(cid:231)(cid:270)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:740)(cid:349)(cid:356)(cid:309)(cid:343)(cid:390)(cid:740)(cid:202)(cid:230)(cid:309)(cid:361)(cid:412)(cid:740) (cid:301)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:273)(cid:302)(cid:264)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:202)(cid:349)(cid:740)(cid:202)(cid:740)(cid:301)(cid:242)(cid:356)(cid:202)(cid:340)(cid:270)(cid:309)(cid:343)(cid:740)(cid:407)(cid:309)(cid:343)(cid:740)(cid:242)(cid:301)(cid:230)(cid:343)(cid:202)(cid:231)(cid:273)(cid:302)(cid:264)(cid:740)
(cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:638) (cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:639) (cid:671)(cid:671) (cid:137)(cid:294)(cid:202)(cid:302)(cid:349) (cid:202) (cid:202) (cid:302) (cid:740)(cid:349) (cid:740) (cid:403) (cid:202) (cid:412)(cid:361) (cid:349)(cid:412) (cid:202) (cid:343) (cid:412) (cid:309) (cid:403)(cid:309) (cid:302) (cid:302) (cid:202) (cid:740) (cid:361) (cid:384) (cid:412) (cid:270) (cid:729)(cid:349) (cid:242) (cid:740)(cid:410) (cid:343) (cid:273) (cid:242) (cid:343)(cid:349) (cid:740)(cid:202) (cid:412)(cid:740) (cid:740) (cid:411) (cid:384) (cid:273)(cid:301) (cid:309)(cid:301) (cid:242)(cid:740) (cid:202) (cid:273)(cid:302) (cid:302) (cid:740) (cid:740) (cid:349) (cid:361) (cid:340) (cid:349) (cid:202) (cid:242) (cid:231) (cid:349) (cid:242) (cid:740)(cid:349) (cid:740)(cid:640) (cid:403)(cid:264) (cid:667)(cid:740) (cid:302) (cid:35) (cid:740) (cid:242)(cid:349)(cid:231)(cid:343)(cid:273)(cid:230)(cid:242)(cid:740) (cid:231) (cid:410)(cid:343) (cid:270) (cid:309) (cid:202) (cid:301) (cid:294)(cid:294)(cid:242) (cid:740)(cid:202) (cid:302) (cid:349) (cid:264) (cid:412)(cid:343) (cid:242) (cid:309) (cid:349) (cid:302) (cid:667)(cid:740)(cid:639) (cid:202) (cid:667) (cid:361) (cid:740)(cid:35) (cid:356)(cid:349) (cid:403) (cid:668) (cid:349) (cid:740)(cid:273) (cid:231) (cid:302) (cid:361) (cid:231) (cid:349) (cid:294) (cid:349) (cid:361) (cid:740) (cid:237) (cid:411)(cid:270) (cid:273)(cid:302) (cid:242) (cid:264) (cid:740)(cid:361) (cid:740)(cid:411) (cid:302) (cid:270) (cid:242) (cid:242) (cid:389) (cid:740) (cid:340) (cid:349)(cid:301) (cid:242)(cid:231) (cid:242) (cid:356) (cid:294) (cid:242) (cid:294)(cid:740) (cid:237) (cid:309) (cid:740) (cid:409) (cid:411) (cid:740) (cid:270) (cid:349) (cid:273) (cid:340) (cid:302) (cid:202) (cid:264) (cid:231) (cid:349) (cid:242) (cid:740) (cid:667) (cid:294) (cid:740) (cid:242) (cid:640) (cid:202) (cid:667)(cid:740) (cid:343)(cid:302)(cid:242)(cid:237)(cid:740) (cid:671)
(cid:689)(cid:640)(cid:740)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740) (cid:294)(cid:202)(cid:302)(cid:264)(cid:361)(cid:202)(cid:264)(cid:242)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:383)(cid:309)(cid:403)(cid:237)(cid:740)(cid:361)(cid:302)(cid:384)(cid:202)(cid:302)(cid:356)(cid:242)(cid:237)(cid:740)(cid:202)(cid:412)(cid:356)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:641)(cid:667)(cid:740)(cid:154)(cid:270)(cid:242)(cid:740) (cid:35)(cid:242)(cid:349)(cid:231)(cid:343)(cid:273)(cid:230)(cid:242)(cid:740)(cid:202)(cid:740)(cid:384)(cid:309)(cid:301)(cid:202)(cid:302)(cid:729)(cid:349)(cid:740)(cid:231)(cid:294)(cid:242)(cid:383)(cid:242)(cid:343)(cid:740)(cid:408)(cid:202)(cid:231)(cid:412)(cid:403)(cid:231)(cid:740)(cid:407)(cid:309)(cid:343)(cid:740)(cid:202)(cid:383)(cid:309)(cid:403)(cid:237)(cid:273)(cid:302)(cid:264)(cid:740)(cid:361)(cid:302)(cid:384)(cid:202)(cid:302)(cid:356)(cid:242)(cid:237)(cid:740)
(cid:309)(cid:301)(cid:403)(cid:412)(cid:356)(cid:242)(cid:237)(cid:690) (cid:410)(cid:273)(cid:302)(cid:202)(cid:294)(cid:740)(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:740)(cid:242)(cid:389)(cid:340)(cid:294)(cid:202)(cid:273)(cid:302)(cid:349)(cid:740)(cid:270)(cid:309)(cid:384)(cid:740)(cid:242)(cid:383)(cid:242)(cid:343)(cid:390)(cid:309)(cid:302)(cid:242)(cid:740)(cid:270)(cid:202)(cid:349)(cid:740) (cid:202)(cid:412)(cid:356)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:202)(cid:412)(cid:740)(cid:202)(cid:740)(cid:230)(cid:202)(cid:343)(cid:667)(cid:740)(cid:641)(cid:667)(cid:740)(cid:29)(cid:309)(cid:302)(cid:356)(cid:242)(cid:301)(cid:340)(cid:294)(cid:202)(cid:356)(cid:242)(cid:740)(cid:270)(cid:309)(cid:384)(cid:740)(cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)
(cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:349)(cid:740)(cid:309)(cid:409)(cid:740)(cid:309)(cid:412)(cid:270)(cid:242)(cid:343)(cid:349) (cid:689)(cid:637)(cid:683)(cid:642)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)(cid:349)(cid:690) (cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:349)(cid:740)(cid:309)(cid:409)(cid:740)(cid:309)(cid:302)(cid:242)(cid:349)(cid:242)(cid:294)(cid:409)(cid:740)(cid:231)(cid:202)(cid:302)(cid:740)(cid:349)(cid:270)(cid:202)(cid:340)(cid:242)(cid:740)(cid:309)(cid:302)(cid:242)(cid:729)(cid:349)(cid:740)(cid:403)(cid:237)(cid:242)(cid:302)(cid:412)(cid:403)(cid:356)(cid:390)(cid:667) (cid:689)(cid:640)(cid:683)(cid:642)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)(cid:349)(cid:690)
(cid:137)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242) (cid:137)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242) (cid:671)(cid:671)
(cid:638) (cid:639) (cid:689) (cid:180) (cid:231) (cid:309) (cid:690)(cid:740) (cid:356)(cid:242)(cid:349) (cid:1) (cid:231) (cid:242) (cid:349) (cid:1) (cid:231) (cid:242) (cid:349)(cid:242) (cid:294) (cid:302) (cid:1) (cid:231) (cid:242) (cid:349) (cid:302) (cid:242) (cid:242) (cid:294) (cid:302) (cid:294) (cid:1) (cid:231) (cid:242) (cid:349) (cid:302) (cid:242) (cid:237) (cid:242) (cid:294) (cid:302) (cid:409) (cid:202)(cid:1) (cid:231) (cid:343) (cid:349) (cid:202) (cid:294) (cid:302) (cid:242) (cid:237) (cid:242) (cid:294) (cid:302) (cid:409) (cid:202) (cid:714) (cid:202) (cid:242) (cid:294) (cid:740) (cid:302) (cid:242) (cid:294)(cid:242) (cid:343) (cid:237) (cid:294) (cid:409) (cid:349) (cid:202) (cid:714) (cid:302)(cid:202) (cid:294) (cid:242) (cid:273) (cid:740) (cid:390) (cid:237) (cid:343) (cid:294) (cid:740) (cid:342) (cid:294)(cid:409) (cid:202) (cid:301) (cid:349) (cid:202) (cid:714)(cid:273) (cid:740)(cid:242) (cid:231) (cid:390) (cid:343) (cid:294) (cid:740) (cid:409) (cid:202) (cid:399) (cid:202) (cid:301)(cid:714) (cid:349)(cid:740) (cid:273) (cid:242) (cid:231) (cid:361) (cid:390) (cid:343) (cid:294) (cid:740)(cid:309) (cid:714) (cid:399) (cid:302) (cid:349) (cid:301) (cid:273) (cid:273) (cid:343) (cid:294)(cid:390) (cid:242) (cid:231) (cid:340) (cid:740) (cid:302) (cid:309) (cid:399) (cid:302) (cid:301)(cid:273) (cid:273) (cid:273) (cid:390) (cid:242) (cid:231)(cid:740) (cid:302) (cid:340) (cid:356) (cid:301) (cid:399)(cid:302) (cid:309) (cid:343)(cid:302) (cid:273) (cid:231) (cid:343) (cid:302)(cid:399) (cid:264) (cid:340) (cid:356)(cid:242)(cid:309) (cid:302) (cid:302)(cid:242) (cid:273)(cid:302) (cid:343)(cid:309) (cid:302) (cid:340) (cid:309) (cid:264) (cid:356)(cid:242) (cid:302)(cid:273)(cid:302) (cid:302) (cid:340) (cid:740) (cid:343) (cid:302) (cid:309)(cid:237) (cid:302)(cid:264) (cid:356)(cid:242) (cid:242) (cid:242) (cid:383) (cid:302)(cid:302) (cid:302) (cid:343) (cid:740) (cid:309) (cid:264) (cid:242) (cid:242) (cid:231) (cid:343) (cid:242) (cid:383) (cid:302) (cid:740)(cid:302) (cid:264)(cid:740) (cid:309) (cid:231) (cid:242) (cid:202) (cid:302) (cid:242) (cid:242) (cid:231) (cid:242) (cid:383)(cid:309) (cid:302) (cid:740) (cid:242) (cid:231) (cid:242) (cid:202) (cid:412) (cid:242) (cid:242) (cid:301) (cid:231) (cid:383) (cid:740) (cid:231) (cid:242) (cid:302) (cid:231) (cid:242) (cid:202) (cid:242) (cid:242) (cid:383) (cid:412) (cid:349) (cid:403) (cid:231) (cid:301) (cid:231) (cid:231) (cid:242) (cid:242) (cid:270) (cid:202)(cid:309)(cid:412) (cid:349) (cid:403) (cid:301) (cid:231) (cid:231) (cid:237) (cid:242) (cid:740) (cid:202) (cid:242) (cid:270) (cid:242) (cid:309)(cid:412) (cid:349) (cid:403) (cid:301) (cid:408) (cid:231) (cid:740) (cid:740) (cid:302) (cid:270) (cid:242) (cid:412)(cid:309) (cid:301) (cid:231) (cid:349) (cid:403) (cid:740) (cid:231) (cid:408)(cid:309) (cid:302) (cid:740) (cid:740) (cid:302) (cid:270) (cid:242) (cid:309) (cid:349) (cid:403) (cid:231) (cid:408) (cid:740) (cid:309) (cid:302) (cid:270) (cid:740) (cid:740) (cid:302) (cid:270) (cid:309) (cid:242) (cid:740) (cid:230) (cid:412)(cid:408) (cid:231) (cid:242) (cid:740) (cid:309) (cid:302) (cid:740) (cid:302) (cid:242) (cid:270) (cid:340)(cid:740) (cid:230) (cid:412)(cid:740) (cid:231)(cid:740) (cid:309) (cid:302) (cid:302) (cid:740) (cid:309)(cid:270) (cid:340) (cid:242) (cid:302)(cid:202) (cid:231) (cid:740) (cid:230) (cid:302)(cid:412)(cid:740) (cid:740) (cid:309) (cid:343) (cid:270) (cid:340) (cid:242) (cid:202) (cid:740) (cid:230) (cid:403) (cid:740) (cid:412)(cid:740) (cid:356)(cid:270)(cid:309) (cid:302) (cid:343) (cid:356) (cid:242) (cid:340) (cid:231) (cid:230)(cid:242) (cid:412)(cid:202) (cid:403) (cid:740) (cid:356) (cid:309)(cid:384) (cid:302) (cid:343)(cid:242) (cid:242) (cid:242) (cid:231) (cid:202)(cid:740) (cid:403) (cid:349) (cid:309) (cid:242) (cid:237) (cid:356)(cid:384) (cid:343) (cid:302) (cid:242) (cid:242) (cid:202) (cid:231)(cid:403) (cid:349) (cid:302) (cid:242) (cid:237) (cid:356) (cid:302) (cid:384)(cid:242) (cid:242) (cid:242) (cid:740) (cid:231)(cid:403) (cid:740) (cid:356) (cid:349) (cid:302) (cid:242) (cid:237) (cid:384) (cid:273) (cid:242) (cid:242) (cid:231) (cid:242) (cid:740) (cid:231)(cid:740) (cid:242) (cid:302) (cid:349) (cid:384) (cid:242) (cid:237) (cid:302)(cid:273) (cid:242) (cid:242) (cid:242) (cid:740)(cid:242) (cid:237)(cid:740) (cid:242) (cid:302) (cid:301) (cid:302) (cid:242) (cid:242) (cid:242) (cid:273) (cid:302)(cid:740) (cid:242) (cid:412) (cid:740) (cid:740) (cid:242) (cid:302) (cid:301) (cid:242) (cid:302)(cid:273)(cid:740)(cid:302) (cid:242) (cid:237) (cid:740) (cid:412)(cid:740) (cid:349) (cid:740) (cid:242) (cid:302) (cid:302)(cid:273) (cid:301) (cid:740) (cid:242) (cid:302) (cid:202) (cid:237) (cid:242) (cid:230) (cid:412)(cid:740) (cid:302)(cid:740) (cid:411) (cid:301) (cid:740) (cid:740) (cid:242) (cid:302) (cid:202) (cid:237) (cid:412) (cid:230) (cid:740) (cid:740) (cid:301) (cid:408) (cid:411)(cid:270) (cid:740)(cid:302)(cid:740) (cid:242) (cid:343) (cid:202) (cid:237)(cid:740) (cid:230) (cid:740) (cid:349) (cid:356) (cid:411) (cid:309) (cid:270) (cid:740) (cid:740) (cid:237)(cid:242) (cid:343) (cid:202)(cid:202) (cid:230) (cid:242) (cid:349) (cid:356) (cid:411) (cid:202) (cid:740)(cid:270) (cid:740)(cid:242) (cid:242) (cid:230)(cid:343)(cid:202)(cid:740) (cid:411) (cid:242) (cid:349) (cid:356)(cid:202) (cid:270) (cid:740) (cid:242) (cid:231) (cid:242) (cid:740) (cid:340) (cid:343) (cid:403) (cid:202) (cid:294) (cid:349) (cid:270)(cid:242) (cid:356)(cid:202) (cid:340) (cid:231) (cid:242) (cid:343) (cid:294) (cid:740) (cid:409) (cid:403) (cid:273) (cid:202) (cid:356) (cid:294) (cid:242) (cid:202) (cid:669) (cid:340) (cid:343)(cid:242) (cid:231) (cid:294) (cid:302) (cid:202) (cid:740) (cid:409) (cid:403) (cid:242) (cid:740) (cid:273) (cid:714) (cid:202) (cid:294) (cid:202) (cid:669) (cid:340) (cid:231) (cid:242) (cid:294)(cid:740) (cid:302) (cid:740) (cid:403) (cid:409) (cid:273) (cid:740) (cid:714)(cid:294) (cid:270) (cid:202) (cid:231) (cid:264) (cid:29) (cid:340) (cid:669) (cid:740) (cid:294)(cid:403) (cid:302) (cid:740) (cid:343) (cid:409) (cid:273) (cid:740) (cid:714)(cid:349) (cid:340)(cid:270) (cid:202) (cid:294)(cid:669) (cid:264) (cid:29) (cid:302)(cid:273) (cid:740) (cid:343)(cid:202)(cid:740) (cid:242) (cid:714) (cid:202) (cid:669) (cid:740) (cid:270) (cid:270) (cid:302)(cid:264) (cid:29) (cid:242) (cid:740)(cid:740) (cid:343)(cid:202) (cid:231) (cid:202)(cid:242)(cid:270) (cid:740) (cid:270) (cid:264) (cid:264) (cid:29)(cid:740) (cid:294)(cid:343)(cid:202) (cid:231) (cid:242) (cid:309) (cid:302) (cid:264) (cid:29) (cid:740) (cid:340) (cid:270) (cid:270) (cid:264) (cid:343)(cid:294) (cid:202) (cid:242) (cid:231) (cid:309) (cid:343) (cid:740) (cid:340) (cid:270) (cid:270) (cid:264) (cid:294) (cid:202) (cid:403) (cid:412) (cid:231)(cid:740) (cid:740) (cid:202) (cid:270)(cid:309) (cid:343)(cid:202) (cid:340) (cid:264) (cid:270) (cid:294) (cid:231) (cid:231) (cid:230) (cid:403) (cid:740) (cid:740) (cid:309) (cid:202) (cid:264)(cid:343) (cid:340) (cid:202) (cid:270) (cid:231) (cid:294)(cid:202) (cid:230) (cid:403) (cid:340)(cid:309) (cid:242) (cid:740) (cid:270)(cid:202) (cid:343)(cid:202) (cid:294) (cid:309) (cid:231) (cid:294) (cid:403) (cid:230) (cid:340) (cid:242) (cid:343) (cid:740) (cid:202) (cid:740)(cid:242) (cid:202) (cid:740) (cid:294) (cid:231)(cid:403) (cid:309) (cid:270) (cid:294) (cid:230) (cid:202) (cid:340) (cid:349) (cid:242) (cid:202)(cid:309) (cid:638) (cid:242) (cid:231) (cid:740) (cid:294) (cid:309) (cid:270) (cid:294) (cid:302) (cid:340) (cid:242) (cid:309) (cid:638) (cid:242) (cid:242) (cid:668) (cid:349) (cid:294)(cid:294) (cid:309) (cid:740) (cid:340)(cid:270) (cid:242) (cid:302) (cid:291) (cid:740) (cid:294) (cid:309) (cid:242) (cid:638)(cid:668) (cid:349) (cid:740) (cid:264) (cid:270) (cid:384) (cid:671) (cid:302) (cid:294) (cid:291) (cid:740) (cid:242) (cid:309) (cid:638)(cid:740) (cid:729)(cid:270) (cid:668) (cid:349) (cid:264) (cid:384) (cid:409) (cid:671) (cid:302) (cid:349)(cid:291) (cid:740)(cid:638) (cid:242) (cid:668) (cid:729) (cid:349) (cid:302)(cid:264) (cid:740) (cid:384)(cid:270) (cid:714) (cid:671) (cid:291) (cid:740) (cid:349) (cid:668) (cid:349)(cid:740) (cid:29) (cid:242) (cid:729) (cid:264) (cid:384) (cid:740)(cid:740) (cid:270) (cid:671) (cid:349) (cid:349)(cid:231) (cid:270) (cid:740) (cid:264) (cid:729) (cid:29) (cid:242) (cid:384) (cid:403) (cid:740)(cid:740) (cid:270) (cid:349) (cid:349) (cid:231) (cid:294) (cid:668) (cid:691) (cid:270) (cid:740) (cid:242) (cid:309) (cid:29) (cid:403) (cid:740) (cid:270) (cid:242)(cid:740)(cid:349) (cid:242) (cid:231) (cid:242) (cid:294) (cid:740) (cid:667) (cid:668) (cid:270)(cid:29) (cid:309) (cid:270)(cid:403) (cid:301) (cid:667) (cid:740)(cid:349) (cid:231) (cid:242) (cid:309) (cid:302) (cid:294) (cid:668) (cid:294) (cid:270)(cid:667) (cid:309) (cid:403) (cid:740) (cid:301) (cid:349)(cid:740) (cid:692) (cid:242) (cid:309) (cid:302) (cid:340) (cid:294)(cid:403) (cid:668) (cid:273) (cid:270) (cid:309) (cid:740) (cid:301) (cid:403) (cid:740) (cid:356)(cid:740) (cid:294)(cid:242) (cid:302) (cid:668) (cid:309) (cid:202) (cid:302) (cid:273) (cid:231) (cid:301)(cid:740) (cid:740) (cid:29) (cid:403)(cid:242) (cid:356) (cid:740) (cid:242) (cid:302) (cid:309) (cid:302) (cid:202) (cid:301) (cid:273) (cid:231) (cid:740) (cid:230)(cid:291) (cid:403) (cid:231) (cid:242) (cid:356)(cid:242) (cid:302) (cid:202) (cid:273)(cid:740) (cid:302) (cid:231)(cid:270) (cid:291) (cid:403) (cid:231) (cid:356) (cid:242) (cid:242) (cid:302)(cid:273) (cid:202) (cid:273) (cid:309) (cid:309) (cid:740) (cid:231) (cid:302) (cid:291) (cid:302)(cid:231) (cid:302) (cid:202) (cid:242) (cid:242)(cid:639) (cid:273) (cid:412) (cid:309) (cid:309) (cid:740) (cid:302) (cid:291) (cid:231) (cid:343) (cid:242) (cid:302)(cid:309) (cid:639) (cid:273) (cid:412) (cid:309) (cid:667) (cid:291) (cid:302) (cid:740) (cid:231) (cid:264) (cid:740) (cid:740) (cid:343) (cid:302) (cid:403) (cid:340) (cid:273) (cid:309) (cid:639) (cid:412)(cid:667) (cid:740) (cid:309) (cid:71) (cid:264)(cid:291) (cid:231) (cid:740) (cid:740) (cid:302) (cid:343) (cid:273) (cid:309) (cid:340) (cid:639) (cid:412)(cid:667) (cid:740) (cid:412) (cid:309) (cid:71) (cid:302)(cid:264) (cid:309) (cid:740) (cid:343) (cid:740) (cid:340) (cid:409) (cid:242) (cid:407)(cid:729)(cid:667) (cid:740) (cid:412) (cid:309) (cid:740)(cid:71) (cid:264) (cid:343) (cid:349) (cid:740) (cid:309) (cid:740) (cid:340) (cid:409) (cid:407) (cid:263) (cid:231) (cid:309) (cid:343) (cid:264) (cid:309) (cid:740) (cid:412)(cid:740)(cid:71) (cid:740) (cid:340)(cid:309) (cid:740) (cid:409) (cid:407) (cid:263) (cid:231) (cid:309) (cid:242) (cid:639) (cid:740) (cid:412) (cid:343)(cid:202) (cid:740)(cid:309) (cid:309) (cid:231)(cid:343) (cid:409) (cid:407)(cid:740) (cid:263) (cid:231) (cid:309) (cid:242) (cid:343) (cid:740) (cid:309) (cid:202) (cid:309) (cid:343) (cid:407) (cid:740) (cid:343)(cid:740) (cid:412) (cid:263) (cid:309)(cid:231) (cid:309) (cid:302) (cid:242) (cid:343)(cid:202) (cid:309) (cid:309) (cid:202) (cid:343) (cid:343) (cid:349) (cid:309) (cid:740) (cid:412)(cid:273) (cid:343) (cid:242) (cid:302) (cid:202) (cid:309) (cid:202)(cid:302) (cid:302) (cid:343) (cid:343) (cid:349) (cid:302) (cid:740) (cid:412)(cid:273) (cid:202) (cid:740) (cid:409) (cid:740) (cid:302) (cid:343)(cid:202) (cid:343) (cid:302) (cid:349) (cid:740) (cid:231) (cid:412)(cid:202) (cid:302) (cid:273) (cid:302) (cid:740) (cid:740) (cid:263) (cid:356) (cid:264) (cid:202)(cid:740) (cid:242) (cid:412)(cid:302) (cid:349) (cid:231) (cid:202) (cid:302) (cid:273) (cid:740) (cid:740) (cid:309) (cid:242) (cid:202) (cid:302) (cid:264) (cid:242) (cid:242) (cid:302)(cid:273) (cid:302) (cid:231) (cid:202) (cid:740) (cid:740)(cid:231) (cid:740) (cid:309) (cid:302)(cid:302)(cid:264) (cid:242) (cid:231) (cid:202)(cid:343) (cid:740) (cid:270) (cid:411) (cid:302) (cid:740) (cid:231) (cid:740) (cid:309) (cid:264) (cid:302) (cid:356) (cid:231) (cid:242) (cid:273) (cid:270) (cid:411) (cid:349) (cid:270) (cid:740)(cid:264) (cid:231) (cid:309) (cid:740) (cid:302) (cid:356) (cid:302) (cid:349) (cid:242)(cid:412) (cid:273) (cid:270) (cid:411) (cid:309) (cid:270) (cid:231) (cid:740) (cid:740) (cid:740) (cid:356) (cid:302) (cid:349) (cid:242) (cid:242) (cid:667) (cid:270) (cid:273) (cid:411)(cid:740) (cid:740) (cid:270) (cid:202)(cid:740) (cid:343) (cid:356) (cid:740)(cid:356) (cid:302) (cid:270) (cid:411) (cid:349) (cid:242) (cid:411) (cid:242) (cid:273) (cid:270) (cid:740) (cid:71)(cid:343) (cid:740) (cid:242) (cid:356)(cid:242) (cid:302)(cid:302) (cid:349) (cid:242) (cid:411) (cid:270)(cid:242) (cid:270) (cid:412) (cid:343) (cid:740) (cid:343) (cid:740) (cid:242) (cid:356) (cid:242) (cid:242) (cid:242) (cid:411) (cid:302) (cid:270) (cid:343) (cid:740)(cid:740) (cid:343)(cid:242) (cid:343) (cid:356) (cid:740) (cid:242) (cid:740)(cid:242) (cid:242) (cid:242) (cid:411)(cid:231)(cid:302) (cid:270) (cid:343) (cid:343) (cid:343) (cid:273) (cid:242) (cid:242)(cid:740) (cid:242) (cid:242) (cid:412) (cid:242) (cid:342) (cid:302) (cid:270) (cid:302) (cid:343) (cid:343)(cid:740) (cid:242) (cid:242) (cid:740) (cid:309) (cid:242) (cid:412) (cid:349) (cid:242) (cid:740) (cid:342) (cid:343) (cid:302) (cid:340)(cid:343)(cid:242) (cid:740) (cid:242) (cid:340) (cid:361) (cid:356) (cid:242) (cid:302)(cid:412) (cid:349) (cid:740) (cid:342) (cid:302) (cid:340) (cid:242)(cid:412) (cid:242) (cid:740) (cid:340) (cid:361) (cid:412) (cid:202)(cid:242)(cid:349) (cid:342) (cid:740) (cid:340) (cid:412)(cid:273) (cid:740) (cid:273) (cid:202) (cid:412)(cid:340) (cid:342)(cid:361) (cid:302) (cid:349) (cid:202) (cid:740) (cid:302) (cid:340) (cid:343) (cid:412)(cid:273) (cid:343) (cid:273) (cid:202) (cid:343) (cid:340) (cid:361) (cid:740) (cid:202) (cid:349) (cid:302) (cid:343) (cid:412) (cid:242) (cid:273) (cid:343) (cid:340) (cid:273)(cid:361) (cid:202) (cid:202)(cid:242) (cid:242) (cid:264) (cid:202) (cid:349) (cid:302) (cid:343)(cid:242) (cid:349) (cid:273) (cid:273) (cid:202) (cid:343)(cid:202) (cid:237) (cid:264) (cid:349) (cid:264)(cid:302)(cid:349) (cid:343) (cid:231) (cid:273) (cid:202) (cid:242) (cid:349) (cid:343)(cid:202) (cid:740) (cid:202) (cid:237) (cid:264) (cid:343) (cid:349) (cid:264) (cid:242)(cid:340) (cid:349) (cid:412) (cid:202) (cid:740) (cid:356) (cid:740) (cid:202) (cid:349) (cid:264)(cid:343) (cid:237)(cid:242) (cid:264) (cid:264) (cid:242) (cid:349) (cid:340) (cid:740) (cid:273)(cid:740) (cid:349) (cid:202) (cid:237) (cid:343)(cid:202) (cid:264) (cid:242) (cid:349) (cid:264) (cid:242) (cid:302)(cid:340) (cid:237)(cid:740) (cid:740) (cid:202) (cid:302) (cid:343)(cid:202) (cid:242)(cid:740) (cid:242) (cid:264) (cid:242) (cid:340) (cid:202) (cid:340) (cid:740)(cid:343) (cid:411)(cid:343) (cid:302) (cid:202) (cid:242) (cid:264)(cid:242) (cid:264) (cid:242)(cid:740) (cid:340) (cid:667) (cid:237) (cid:343)(cid:349) (cid:270) (cid:302) (cid:202) (cid:264) (cid:242) (cid:242) (cid:242) (cid:740) (cid:270)(cid:340) (cid:667) (cid:237) (cid:343)(cid:349) (cid:302) (cid:740) (cid:740) (cid:242)(cid:740) (cid:340) (cid:270) (cid:740) (cid:340)(cid:691) (cid:340) (cid:302) (cid:667) (cid:242) (cid:343) (cid:237) (cid:242) (cid:349) (cid:740) (cid:349) (cid:349) (cid:740) (cid:340) (cid:270) (cid:740) (cid:667) (cid:667) (cid:237) (cid:691) (cid:349) (cid:740) (cid:242) (cid:349) (cid:349) (cid:740) (cid:667)(cid:740) (cid:340) (cid:270) (cid:667) (cid:242) (cid:237)(cid:740) (cid:740) (cid:242) (cid:667)(cid:691)(cid:667) (cid:740)(cid:740) (cid:340) (cid:242) (cid:349) (cid:349) (cid:667) (cid:384)(cid:340) (cid:692) (cid:740)(cid:231) (cid:740) (cid:242) (cid:691)(cid:740)(cid:667)(cid:667) (cid:343)(cid:242) (cid:302) (cid:349) (cid:349)(cid:740) (cid:667) (cid:384) (cid:740)(cid:692) (cid:691) (cid:740) (cid:231) (cid:242) (cid:667) (cid:202) (cid:667) (cid:349)(cid:412) (cid:242) (cid:154) (cid:302) (cid:349) (cid:667) (cid:384) (cid:740) (cid:403) (cid:692)(cid:667) (cid:740) (cid:242) (cid:231) (cid:667) (cid:356) (cid:667) (cid:412) (cid:154) (cid:403) (cid:412) (cid:302) (cid:384) (cid:692) (cid:343) (cid:242) (cid:740) (cid:403)(cid:340) (cid:667) (cid:231) (cid:383) (cid:356) (cid:270) (cid:242) (cid:412) (cid:692)(cid:154) (cid:403) (cid:302) (cid:412)(cid:270) (cid:740) (cid:403)(cid:202) (cid:383)(cid:302)(cid:356) (cid:270) (cid:412) (cid:242) (cid:154)(cid:740) (cid:403) (cid:412)(cid:270) (cid:242) (cid:242) (cid:403) (cid:302) (cid:242) (cid:154) (cid:356) (cid:383) (cid:740) (cid:270) (cid:264) (cid:242) (cid:403) (cid:412)(cid:270) (cid:242) (cid:302) (cid:356) (cid:411) (cid:242) (cid:740) (cid:231)(cid:383) (cid:270) (cid:242) (cid:740)(cid:270)(cid:740) (cid:231) (cid:242)(cid:230) (cid:302) (cid:270) (cid:411) (cid:242) (cid:242) (cid:270) (cid:343) (cid:740) (cid:230) (cid:740) (cid:740) (cid:412)(cid:242) (cid:231)(cid:302) (cid:230) (cid:242) (cid:242) (cid:411)(cid:270) (cid:740) (cid:202)(cid:740) (cid:230)(cid:740) (cid:390)(cid:302)(cid:231) (cid:403) (cid:242) (cid:242) (cid:230) (cid:411)(cid:242) (cid:242) (cid:740) (cid:270) (cid:230) (cid:383) (cid:740) (cid:349) (cid:231) (cid:390) (cid:340) (cid:230) (cid:242) (cid:740) (cid:242) (cid:242) (cid:270) (cid:230)(cid:740) (cid:231) (cid:740) (cid:349) (cid:349) (cid:390)(cid:361) (cid:242) (cid:242) (cid:668) (cid:242) (cid:230) (cid:740) (cid:242) (cid:411)(cid:740) (cid:740) (cid:270)(cid:349) (cid:390) (cid:349) (cid:361)(cid:242) (cid:242)(cid:412) (cid:668) (cid:242) (cid:740) (cid:411) (cid:349) (cid:270)(cid:740) (cid:740) (cid:349) (cid:740)(cid:349) (cid:349)(cid:242) (cid:361) (cid:412) (cid:668) (cid:740) (cid:740)(cid:230) (cid:411) (cid:349) (cid:270) (cid:349) (cid:349) (cid:740) (cid:349) (cid:740) (cid:349) (cid:242) (cid:231) (cid:361) (cid:273)(cid:668) (cid:412) (cid:242) (cid:740) (cid:411) (cid:349) (cid:270) (cid:349) (cid:740) (cid:349)(cid:302) (cid:242) (cid:740) (cid:668) (cid:231) (cid:390) (cid:273) (cid:412) (cid:242) (cid:740) (cid:242) (cid:270) (cid:349) (cid:270) (cid:740) (cid:384) (cid:349)(cid:301) (cid:302) (cid:242) (cid:412)(cid:231) (cid:273) (cid:349) (cid:740) (cid:242) (cid:242) (cid:270) (cid:740) (cid:264) (cid:301) (cid:242) (cid:302) (cid:301) (cid:231)(cid:740) (cid:273) (cid:309)(cid:242) (cid:361) (cid:242) (cid:270) (cid:242)(cid:264) (cid:403) (cid:231) (cid:302) (cid:301) (cid:301) (cid:309) (cid:242)(cid:740) (cid:242) (cid:270) (cid:412) (cid:264) (cid:301)(cid:403) (cid:301) (cid:349) (cid:411)(cid:242) (cid:270)(cid:309) (cid:740) (cid:242) (cid:349) (cid:270) (cid:264) (cid:231)(cid:403) (cid:301) (cid:740) (cid:411) (cid:309) (cid:270) (cid:273)(cid:740) (cid:242) (cid:349) (cid:231) (cid:309) (cid:301) (cid:740) (cid:403) (cid:740) (cid:309) (cid:242) (cid:302)(cid:411)(cid:270) (cid:740) (cid:740) (cid:242) (cid:349)(cid:408) (cid:231) (cid:309) (cid:403) (cid:740) (cid:242) (cid:740) (cid:242)(cid:411) (cid:411)(cid:270) (cid:409) (cid:349) (cid:740) (cid:231) (cid:408) (cid:403) (cid:309) (cid:309) (cid:264) (cid:740) (cid:740) (cid:242) (cid:242) (cid:270) (cid:270) (cid:349) (cid:403) (cid:409) (cid:231) (cid:740) (cid:740) (cid:740) (cid:309) (cid:408)(cid:309)(cid:740) (cid:242) (cid:242) (cid:349) (cid:343) (cid:403) (cid:740) (cid:409)(cid:740) (cid:740) (cid:408) (cid:740) (cid:740) (cid:740)(cid:309) (cid:242) (cid:242) (cid:242) (cid:349) (cid:294) (cid:343) (cid:409) (cid:403) (cid:411) (cid:242)(cid:408) (cid:740) (cid:740) (cid:740) (cid:740) (cid:740) (cid:309) (cid:202) (cid:349) (cid:294) (cid:639) (cid:343) (cid:403)(cid:740) (cid:242) (cid:740) (cid:740) (cid:740)(cid:740) (cid:270) (cid:309) (cid:740) (cid:342) (cid:202) (cid:349)(cid:403) (cid:294) (cid:639)(cid:411) (cid:343) (cid:740) (cid:242) (cid:231) (cid:740)(cid:667) (cid:349) (cid:342) (cid:202)(cid:294)(cid:740) (cid:639) (cid:242) (cid:270) (cid:242) (cid:740) (cid:231) (cid:361) (cid:667) (cid:291) (cid:294)(cid:202) (cid:342) (cid:639)(cid:740) (cid:231)(cid:202)(cid:361) (cid:667) (cid:740) (cid:291) (cid:342) (cid:639) (cid:242) (cid:740) (cid:273)(cid:231) (cid:667) (cid:361) (cid:291)(cid:202) (cid:343)(cid:231) (cid:740) (cid:273) (cid:667) (cid:301) (cid:361) (cid:291)(cid:202) (cid:343)(cid:242) (cid:740) (cid:273) (cid:740) (cid:291)(cid:202) (cid:343)(cid:242) (cid:740) (cid:273) (cid:740) (cid:237)(cid:202) (cid:343) (cid:740) (cid:242) (cid:242) (cid:740) (cid:237)(cid:202) (cid:242) (cid:740)(cid:740) (cid:740) (cid:237) (cid:740) (cid:309) (cid:740)(cid:237)(cid:740) (cid:409) (cid:740) (cid:740)
(cid:41)(cid:76)(cid:91)(cid:3)(cid:70)(cid:82)(cid:79)(cid:82)(cid:85)(cid:3)(cid:11)(cid:69)(cid:92)(cid:3)(cid:60)(cid:88)(cid:84)(cid:76)(cid:68)(cid:81)(cid:12)
(cid:56)(cid:86)(cid:72)(cid:3)(cid:85)(cid:72)(cid:71)(cid:18)(cid:74)(cid:85)(cid:72)(cid:72)(cid:81)(cid:3)(cid:87)(cid:82)(cid:3)(cid:86)(cid:75)(cid:82)(cid:90)(cid:3)(cid:73)(cid:76)(cid:81)(cid:68)(cid:79)(cid:3)(cid:70)(cid:75)(cid:82)(cid:76)(cid:70)(cid:72)
(cid:181)(cid:343)(cid:403)(cid:356)(cid:242)(cid:740)(cid:202)(cid:740)(cid:231)(cid:309)(cid:270)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740)(cid:641)(cid:740)(cid:349)(cid:270)(cid:309)(cid:343)(cid:412)(cid:740)(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:349)(cid:667)(cid:740)(cid:154)(cid:270)(cid:242)(cid:740)(cid:242)(cid:302)(cid:237)(cid:740)(cid:349)(cid:242)(cid:302)(cid:356)(cid:242)(cid:302)(cid:231)(cid:242)(cid:740)(cid:309)(cid:409)(cid:740)(cid:242)(cid:202)(cid:231)(cid:270)(cid:740)(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:740)(cid:301)(cid:361)(cid:349)(cid:412)(cid:740)(cid:230)(cid:242)(cid:669)(cid:740)(cid:638)(cid:667)(cid:740)(cid:71)(cid:412)(cid:740)(cid:403)(cid:349)(cid:302)(cid:729)(cid:411)(cid:740)
(cid:689)(cid:202)(cid:690)(cid:740) (cid:237)(cid:273)(cid:409)(cid:409)(cid:403)(cid:231)(cid:361)(cid:294)(cid:412)(cid:740)(cid:408)(cid:309)(cid:740)(cid:237)(cid:309)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:273)(cid:409)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:288)(cid:361)(cid:349)(cid:412)(cid:740)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:309)(cid:302)(cid:740)(cid:390)(cid:309)(cid:361)(cid:343)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:667)(cid:740)(cid:639)(cid:667)(cid:740)(cid:71)(cid:412)(cid:740)(cid:231)(cid:202)(cid:361)(cid:264)(cid:270)(cid:412)(cid:740)(cid:270)(cid:273)(cid:301)(cid:740)(cid:309)(cid:409)(cid:409)(cid:740)(cid:264)(cid:361)(cid:202)(cid:343)(cid:237)(cid:740)(cid:411)(cid:270)(cid:202)(cid:412)(cid:740)(cid:349)(cid:340)(cid:202)(cid:231)(cid:242)(cid:740)(cid:349)(cid:301)(cid:242)(cid:294)(cid:294)(cid:242)(cid:237)(cid:740)(cid:309)(cid:409)(cid:740)
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:349)(cid:242)(cid:202)(cid:343)(cid:242)(cid:237)(cid:740)(cid:349)(cid:356)(cid:242)(cid:202)(cid:291)(cid:667)(cid:740)(cid:640)(cid:667)(cid:740)(cid:181)(cid:270)(cid:242)(cid:302)(cid:740)(cid:349)(cid:270)(cid:242)(cid:740)(cid:237)(cid:403)(cid:237)(cid:302)(cid:722)(cid:411)(cid:740)(cid:294)(cid:273)(cid:291)(cid:242)(cid:740)(cid:202)(cid:740)(cid:264)(cid:361)(cid:390)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:384)(cid:202)(cid:349)(cid:740)(cid:411)(cid:343)(cid:390)(cid:273)(cid:302)(cid:264)(cid:740)(cid:408)(cid:309)(cid:740)(cid:340)(cid:403)(cid:231)(cid:291)(cid:740)(cid:270)(cid:242)(cid:343)(cid:740)(cid:361)(cid:340)(cid:668)(cid:740)(cid:349)(cid:270)(cid:242)(cid:740)(cid:349)(cid:356)(cid:202)(cid:343)(cid:356)(cid:242)(cid:237)(cid:740)(cid:361)(cid:349)(cid:273)(cid:302)(cid:264)(cid:740)(cid:349)(cid:403)(cid:264)(cid:302)(cid:740)(cid:294)(cid:202)(cid:302)(cid:264)(cid:361)(cid:202)(cid:264)(cid:242)(cid:667)(cid:740)(cid:641)(cid:667)(cid:740)
(cid:41)(cid:202)(cid:231)(cid:270)(cid:740)(cid:340)(cid:242)(cid:343)(cid:349)(cid:309)(cid:302)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:291)(cid:302)(cid:309)(cid:384)(cid:349)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:270)(cid:202)(cid:349)(cid:740)(cid:202)(cid:740)(cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:309)(cid:409)(cid:740)(cid:384)(cid:270)(cid:309)(cid:740)(cid:390)(cid:309)(cid:361)(cid:740)(cid:202)(cid:343)(cid:242)(cid:667)(cid:740)(cid:740)
(cid:71)(cid:302)(cid:340)(cid:361)(cid:412) (cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:638)(cid:740)(cid:740)(cid:740) (cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:639)(cid:740)(cid:740)(cid:740) (cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:640)(cid:705)(cid:642)(cid:740)(cid:740)(cid:740)
(cid:689)(cid:230)(cid:690)(cid:740) (cid:638)(cid:667)(cid:740)(cid:71)(cid:302)(cid:412)(cid:343)(cid:309)(cid:237)(cid:361)(cid:231)(cid:242)(cid:740)(cid:202)(cid:302)(cid:237)(cid:740)(cid:242)(cid:389)(cid:340)(cid:294)(cid:202)(cid:273)(cid:302)(cid:740)(cid:411)(cid:270)(cid:242)(cid:740)(cid:408)(cid:242)(cid:231)(cid:270)(cid:302)(cid:403)(cid:342)(cid:361)(cid:242)(cid:740) (cid:638)(cid:667)(cid:740)(cid:71)(cid:302)(cid:412)(cid:343)(cid:309)(cid:237)(cid:361)(cid:231)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:302)(cid:740)(cid:361)(cid:302)(cid:361)(cid:349)(cid:361)(cid:202)(cid:294)(cid:740)(cid:349)(cid:242)(cid:294)(cid:409)(cid:714)(cid:270)(cid:242)(cid:294)(cid:340)(cid:740)(cid:230)(cid:309)(cid:309)(cid:291)(cid:668)(cid:740)
(cid:309)(cid:409)(cid:740)(cid:237)(cid:309)(cid:273)(cid:302)(cid:264)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:639)(cid:667)(cid:740)(cid:146)(cid:384)(cid:403)(cid:356)(cid:231)(cid:270)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:740) (cid:301)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:273)(cid:302)(cid:264)(cid:740)(cid:202)(cid:740)(cid:270)(cid:202)(cid:302)(cid:237)(cid:349)(cid:356)(cid:202)(cid:302)(cid:237)(cid:740)(cid:202)(cid:349)(cid:740)(cid:202)(cid:740)(cid:301)(cid:242)(cid:356)(cid:202)(cid:340)(cid:270)(cid:309)(cid:343)(cid:740)(cid:407)(cid:309)(cid:343)(cid:740)
(cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:638) (cid:740)(cid:137)(cid:294)(cid:202)(cid:302)(cid:740)(cid:639)(cid:740)(cid:740)(cid:671)(cid:671) (cid:137)(cid:294)(cid:202)(cid:302)(cid:349) (cid:349) (cid:349) (cid:356) (cid:340) (cid:309) (cid:202) (cid:343) (cid:231) (cid:390) (cid:242) (cid:740)(cid:202) (cid:740)(cid:640) (cid:230) (cid:667) (cid:309) (cid:740)(cid:35) (cid:361) (cid:242) (cid:412)(cid:740) (cid:349) (cid:202) (cid:231) (cid:302) (cid:343)(cid:273) (cid:740) (cid:230) (cid:202)(cid:349) (cid:242) (cid:412) (cid:740)(cid:202) (cid:343)(cid:309) (cid:740)(cid:349) (cid:302) (cid:403)(cid:412) (cid:202) (cid:361) (cid:361) (cid:202) (cid:412) (cid:412) (cid:729)(cid:349) (cid:403)(cid:309) (cid:740)(cid:410) (cid:302) (cid:273)(cid:343) (cid:740) (cid:349) (cid:384) (cid:412) (cid:270) (cid:740)(cid:411) (cid:242) (cid:273)(cid:301) (cid:343)(cid:242) (cid:242) (cid:740)(cid:202) (cid:740)(cid:273) (cid:740) (cid:302)(cid:740) (cid:242) (cid:411)(cid:270) (cid:301) (cid:273)(cid:302) (cid:230) (cid:264) (cid:343)(cid:202) (cid:349)(cid:740) (cid:231) (cid:294) (cid:273) (cid:242) (cid:302) (cid:202) (cid:264) (cid:343)(cid:302) (cid:740)(cid:231) (cid:242) (cid:270) (cid:237) (cid:202) (cid:740) (cid:294) (cid:410) (cid:294) (cid:343) (cid:242) (cid:309) (cid:302) (cid:301) (cid:264)(cid:242) (cid:740)(cid:202) (cid:349) (cid:349) (cid:667)(cid:740) (cid:412) (cid:639) (cid:343) (cid:667) (cid:309) (cid:740)(cid:35) (cid:302) (cid:403) (cid:202) (cid:349) (cid:361) (cid:231) (cid:356) (cid:361) (cid:349) (cid:349) (cid:668)(cid:740) (cid:349) (cid:273)(cid:302) (cid:740)(cid:411) (cid:231) (cid:270) (cid:294) (cid:242) (cid:361) (cid:740) (cid:237) (cid:361) (cid:273) (cid:302) (cid:302) (cid:242) (cid:264) (cid:389) (cid:740)(cid:411) (cid:340) (cid:270) (cid:242) (cid:242) (cid:231) (cid:740) (cid:356) (cid:349) (cid:242) (cid:301) (cid:237) (cid:242) (cid:740) (cid:294)(cid:294)(cid:740)(cid:309)(cid:409)(cid:740) (cid:638) (cid:639) (cid:671) (cid:671) (cid:667) (cid:671)(cid:671)(cid:667)(cid:667)
(cid:384)(cid:309)(cid:301)(cid:202)(cid:302)(cid:740)(cid:361)(cid:349)(cid:242)(cid:349)(cid:740)(cid:349)(cid:403)(cid:264)(cid:302)(cid:740)(cid:294)(cid:202)(cid:302)(cid:264)(cid:361)(cid:202)(cid:264)(cid:242)(cid:740)(cid:408)(cid:309)(cid:740)(cid:202)(cid:383)(cid:309)(cid:403)(cid:237)(cid:740) (cid:349)(cid:340)(cid:202)(cid:231)(cid:242)(cid:667)(cid:740)(cid:640)(cid:667)(cid:740)(cid:35)(cid:242)(cid:349)(cid:231)(cid:343)(cid:273)(cid:230)(cid:242)(cid:740)(cid:202)(cid:740)(cid:384)(cid:309)(cid:301)(cid:202)(cid:302)(cid:729)(cid:349)(cid:740)(cid:231)(cid:294)(cid:242)(cid:383)(cid:242)(cid:343)(cid:740)(cid:408)(cid:202)(cid:231)(cid:412)(cid:403)(cid:231)(cid:740)(cid:407)(cid:309)(cid:343)(cid:740)(cid:202)(cid:383)(cid:309)(cid:403)(cid:237)(cid:273)(cid:302)(cid:264)(cid:740) (cid:671)
(cid:361)(cid:302)(cid:384)(cid:202)(cid:302)(cid:356)(cid:242)(cid:237)(cid:740)(cid:202)(cid:412)(cid:356)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:641)(cid:667)(cid:740)(cid:154)(cid:270)(cid:242)(cid:740)(cid:410)(cid:273)(cid:302)(cid:202)(cid:294)(cid:740) (cid:361)(cid:302)(cid:384)(cid:202)(cid:302)(cid:356)(cid:242)(cid:237)(cid:740)(cid:202)(cid:412)(cid:356)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:302)(cid:740)(cid:202)(cid:412)(cid:740)(cid:202)(cid:740)(cid:230)(cid:202)(cid:343)(cid:667)(cid:740)(cid:641)(cid:667)(cid:740)(cid:29)(cid:309)(cid:302)(cid:356)(cid:242)(cid:301)(cid:340)(cid:294)(cid:202)(cid:356)(cid:242)(cid:740)(cid:270)(cid:309)(cid:384)(cid:740)
(cid:340)(cid:202)(cid:343)(cid:202)(cid:264)(cid:343)(cid:202)(cid:340)(cid:270)(cid:740)(cid:242)(cid:389)(cid:340)(cid:294)(cid:202)(cid:273)(cid:302)(cid:349)(cid:740)(cid:270)(cid:309)(cid:384)(cid:740)(cid:242)(cid:383)(cid:242)(cid:343)(cid:390)(cid:309)(cid:302)(cid:242)(cid:740)(cid:270)(cid:202)(cid:349)(cid:740) (cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:349)(cid:740)(cid:309)(cid:409)(cid:740)(cid:309)(cid:302)(cid:242)(cid:349)(cid:242)(cid:294)(cid:409)(cid:740)(cid:231)(cid:202)(cid:302)(cid:740)(cid:349)(cid:270)(cid:202)(cid:340)(cid:242)(cid:740)(cid:309)(cid:302)(cid:242)(cid:729)(cid:349)(cid:740)
(cid:137)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242) (cid:137)(cid:202)(cid:349)(cid:349)(cid:202)(cid:264)(cid:242) (cid:671)(cid:671) (cid:237)(cid:273)(cid:409)(cid:263)(cid:242)(cid:343)(cid:242)(cid:302)(cid:412)(cid:740)(cid:340)(cid:242)(cid:343)(cid:231)(cid:242)(cid:340)(cid:412)(cid:403)(cid:309)(cid:302)(cid:349)(cid:740)(cid:309)(cid:409)(cid:740)(cid:309)(cid:412)(cid:270)(cid:242)(cid:343)(cid:349) (cid:403)(cid:237)(cid:242)(cid:302)(cid:412)(cid:403)(cid:356)(cid:390)(cid:667)
(cid:638) (cid:639) (cid:637)(cid:683)(cid:642)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)(cid:349) (cid:640)(cid:683)(cid:642)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)(cid:349) (cid:302)(cid:683)(cid:642)(cid:740)(cid:383)(cid:309)(cid:356)(cid:242)(cid:349)
(cid:180)(cid:309) (cid:689)(cid:231) (cid:356) (cid:690) (cid:242) (cid:740) (cid:349) (cid:1) (cid:231) (cid:343) (cid:349) (cid:1) (cid:231) (cid:343) (cid:349) (cid:242) (cid:242) (cid:294)(cid:1) (cid:231) (cid:343) (cid:349) (cid:242) (cid:302) (cid:242) (cid:242) (cid:294) (cid:342) (cid:1) (cid:231) (cid:343) (cid:349) (cid:242)(cid:294) (cid:302) (cid:242) (cid:242)(cid:294) (cid:342) (cid:409) (cid:1) (cid:231) (cid:343) (cid:349) (cid:202) (cid:294) (cid:302) (cid:202) (cid:242) (cid:242) (cid:242) (cid:294) (cid:342) (cid:361) (cid:409)(cid:294) (cid:202) (cid:202)(cid:302) (cid:714)(cid:242) (cid:242) (cid:242) (cid:294)(cid:361) (cid:343) (cid:294) (cid:342) (cid:409) (cid:202) (cid:202) (cid:294)(cid:714) (cid:302) (cid:242) (cid:273)(cid:361) (cid:273) (cid:343) (cid:390)(cid:294) (cid:342) (cid:409) (cid:740) (cid:202) (cid:714) (cid:202) (cid:294) (cid:301) (cid:343) (cid:273) (cid:273) (cid:343) (cid:390)(cid:294) (cid:361) (cid:231)(cid:740) (cid:409) (cid:202) (cid:714) (cid:202) (cid:399) (cid:301) (cid:343) (cid:273) (cid:273) (cid:390) (cid:242) (cid:231)(cid:343) (cid:294) (cid:740) (cid:361) (cid:399) (cid:301) (cid:343) (cid:714) (cid:309) (cid:273) (cid:242)(cid:273) (cid:231) (cid:273) (cid:390) (cid:343) (cid:294) (cid:740) (cid:399) (cid:340) (cid:309) (cid:301) (cid:237) (cid:343) (cid:302) (cid:242) (cid:273) (cid:273) (cid:273) (cid:231) (cid:390) (cid:740) (cid:340) (cid:302) (cid:309) (cid:399) (cid:237) (cid:302) (cid:301) (cid:273) (cid:343)(cid:242) (cid:231) (cid:340) (cid:302) (cid:343)(cid:237) (cid:740) (cid:302) (cid:309) (cid:399) (cid:264) (cid:273) (cid:242) (cid:302) (cid:343) (cid:302) (cid:242) (cid:340) (cid:740) (cid:264) (cid:309)(cid:237) (cid:302) (cid:309) (cid:273) (cid:343) (cid:302) (cid:242) (cid:302) (cid:740) (cid:264) (cid:309) (cid:340) (cid:740) (cid:237) (cid:302) (cid:302)(cid:302) (cid:242) (cid:242) (cid:343) (cid:242) (cid:383) (cid:309) (cid:302) (cid:740) (cid:740) (cid:264) (cid:302) (cid:242)(cid:302) (cid:242) (cid:242) (cid:383) (cid:740) (cid:343)(cid:309) (cid:740) (cid:264) (cid:302) (cid:231) (cid:237) (cid:242) (cid:202) (cid:242) (cid:242) (cid:383) (cid:302) (cid:242) (cid:740) (cid:309) (cid:231) (cid:237) (cid:242) (cid:202) (cid:302) (cid:242) (cid:242) (cid:383) (cid:412) (cid:301) (cid:740) (cid:231) (cid:231) (cid:237) (cid:242) (cid:740) (cid:202) (cid:302) (cid:242) (cid:412)(cid:242) (cid:383) (cid:301) (cid:349) (cid:231) (cid:403) (cid:740) (cid:231) (cid:237) (cid:242) (cid:202) (cid:270) (cid:412) (cid:309) (cid:301) (cid:349) (cid:231) (cid:403) (cid:740) (cid:231) (cid:237) (cid:242) (cid:242) (cid:202) (cid:270) (cid:309)(cid:412) (cid:242)(cid:349) (cid:403) (cid:301) (cid:231) (cid:740)(cid:242) (cid:270) (cid:740) (cid:302) (cid:309) (cid:242) (cid:412) (cid:349) (cid:403) (cid:301) (cid:302) (cid:231) (cid:740)(cid:242) (cid:231)(cid:740) (cid:302) (cid:302) (cid:270) (cid:242) (cid:309) (cid:349) (cid:302)(cid:403) (cid:231)(cid:740) (cid:302) (cid:242) (cid:302) (cid:740)(cid:270) (cid:242) (cid:270) (cid:309) (cid:302) (cid:356) (cid:231) (cid:302) (cid:230) (cid:412) (cid:740) (cid:740) (cid:242) (cid:302) (cid:270) (cid:242) (cid:356)(cid:302) (cid:242) (cid:230) (cid:231) (cid:412) (cid:740) (cid:302) (cid:740) (cid:740) (cid:302) (cid:270) (cid:309) (cid:356)(cid:242) (cid:230) (cid:302) (cid:242) (cid:412) (cid:202) (cid:231) (cid:740) (cid:740) (cid:302) (cid:309)(cid:270) (cid:302) (cid:356)(cid:242) (cid:242)(cid:230) (cid:202)(cid:412)(cid:740) (cid:403) (cid:740) (cid:309) (cid:302) (cid:356)(cid:270) (cid:302) (cid:242) (cid:356)(cid:242) (cid:202) (cid:230) (cid:231) (cid:412) (cid:403) (cid:740) (cid:309) (cid:302) (cid:231) (cid:356) (cid:302) (cid:384) (cid:242) (cid:242) (cid:231) (cid:202) (cid:403) (cid:740) (cid:356) (cid:231) (cid:309) (cid:302) (cid:302) (cid:242) (cid:237) (cid:384) (cid:231) (cid:242)(cid:242) (cid:202) (cid:403) (cid:231) (cid:356) (cid:242) (cid:237) (cid:384) (cid:302) (cid:302) (cid:242) (cid:242)(cid:231) (cid:740) (cid:403) (cid:231) (cid:242) (cid:237) (cid:740) (cid:356)(cid:349)(cid:384) (cid:302) (cid:242) (cid:242) (cid:273) (cid:231) (cid:740) (cid:242)(cid:740)(cid:231) (cid:242) (cid:237) (cid:349) (cid:242) (cid:384)(cid:242) (cid:302) (cid:242) (cid:273)(cid:740) (cid:740) (cid:242)(cid:740) (cid:349) (cid:242)(cid:242) (cid:237) (cid:302)(cid:273) (cid:242) (cid:301) (cid:408) (cid:242) (cid:740) (cid:242) (cid:740)(cid:302) (cid:740) (cid:242) (cid:349) (cid:302) (cid:740) (cid:301) (cid:408)(cid:740) (cid:273) (cid:242)(cid:309) (cid:302) (cid:242) (cid:740) (cid:237) (cid:740) (cid:242) (cid:740) (cid:349) (cid:301) (cid:408) (cid:302) (cid:309)(cid:740) (cid:273) (cid:302) (cid:740) (cid:242) (cid:237)(cid:740) (cid:242) (cid:230) (cid:301) (cid:408) (cid:302) (cid:740) (cid:309) (cid:411)(cid:740) (cid:740) (cid:302) (cid:237) (cid:242) (cid:230) (cid:740) (cid:340)(cid:740) (cid:411) (cid:301) (cid:408) (cid:740) (cid:309) (cid:270) (cid:242) (cid:302) (cid:237) (cid:230) (cid:343) (cid:340)(cid:740) (cid:740) (cid:411) (cid:356) (cid:270)(cid:740) (cid:309) (cid:242) (cid:343) (cid:340) (cid:237) (cid:343) (cid:230) (cid:202)(cid:740) (cid:411) (cid:356) (cid:270) (cid:242) (cid:740) (cid:202) (cid:242) (cid:343) (cid:343)(cid:340) (cid:202) (cid:230) (cid:242) (cid:356) (cid:740) (cid:242) (cid:411)(cid:270) (cid:202) (cid:343) (cid:242) (cid:231) (cid:343)(cid:202) (cid:740) (cid:242) (cid:340) (cid:242) (cid:403) (cid:356)(cid:202) (cid:270) (cid:231) (cid:349) (cid:340) (cid:343) (cid:740) (cid:242) (cid:343) (cid:294) (cid:202) (cid:403) (cid:242) (cid:273) (cid:356)(cid:202) (cid:231) (cid:349) (cid:340)(cid:740) (cid:669)(cid:294) (cid:343) (cid:403) (cid:242)(cid:302) (cid:202) (cid:273) (cid:242)(cid:242) (cid:740) (cid:202) (cid:349) (cid:340) (cid:202) (cid:231) (cid:669)(cid:294) (cid:740) (cid:302) (cid:403) (cid:273) (cid:242) (cid:242) (cid:740)(cid:740) (cid:202) (cid:669) (cid:349) (cid:340) (cid:231) (cid:302) (cid:294) (cid:302) (cid:264) (cid:29) (cid:740) (cid:242) (cid:740) (cid:403)(cid:740) (cid:273) (cid:343) (cid:202) (cid:669) (cid:349) (cid:302)(cid:340) (cid:264) (cid:29) (cid:294)(cid:740) (cid:302) (cid:242) (cid:343) (cid:273) (cid:740)(cid:202) (cid:202) (cid:302) (cid:412) (cid:264) (cid:29)(cid:669) (cid:740) (cid:270) (cid:302) (cid:740) (cid:343) (cid:242) (cid:740)(cid:202) (cid:231) (cid:412)(cid:202) (cid:302) (cid:740)(cid:264) (cid:29) (cid:740) (cid:270) (cid:264)(cid:740) (cid:343)(cid:202) (cid:412) (cid:231)(cid:740) (cid:202)(cid:740) (cid:270) (cid:302) (cid:309) (cid:264) (cid:29)(cid:264) (cid:270) (cid:343)(cid:202) (cid:231) (cid:202)(cid:412)(cid:740) (cid:740) (cid:309)(cid:270) (cid:264) (cid:343) (cid:270) (cid:740) (cid:202) (cid:202) (cid:231) (cid:403) (cid:309) (cid:412)(cid:740) (cid:740) (cid:343) (cid:270) (cid:270) (cid:202) (cid:264)(cid:349)(cid:740) (cid:202) (cid:231)(cid:403) (cid:202) (cid:231) (cid:309) (cid:343) (cid:740)(cid:202) (cid:349) (cid:270) (cid:740) (cid:264) (cid:202) (cid:231)(cid:403) (cid:242) (cid:202)(cid:294) (cid:202) (cid:309)(cid:340) (cid:349) (cid:343) (cid:242) (cid:202) (cid:270) (cid:740) (cid:231) (cid:242) (cid:294) (cid:403) (cid:294) (cid:340) (cid:242) (cid:202) (cid:349) (cid:343)(cid:202)(cid:294) (cid:740) (cid:231) (cid:242)(cid:242) (cid:294)(cid:294) (cid:740) (cid:403) (cid:340) (cid:270)(cid:242) (cid:202) (cid:409) (cid:349) (cid:294)(cid:202) (cid:242)(cid:294) (cid:638) (cid:231) (cid:242) (cid:740) (cid:294) (cid:270)(cid:340) (cid:242) (cid:409) (cid:302)(cid:294) (cid:242) (cid:714) (cid:638)(cid:740) (cid:294) (cid:242) (cid:270) (cid:668) (cid:349) (cid:294) (cid:409) (cid:340) (cid:302) (cid:242) (cid:294)(cid:714) (cid:740) (cid:638) (cid:242) (cid:668)(cid:740) (cid:294) (cid:270) (cid:349)(cid:270) (cid:302) (cid:264)(cid:409) (cid:384) (cid:714) (cid:740) (cid:740) (cid:294) (cid:638) (cid:242) (cid:668) (cid:349) (cid:270) (cid:740) (cid:270) (cid:264) (cid:384) (cid:691) (cid:302) (cid:740) (cid:740) (cid:409)(cid:714)(cid:270) (cid:638) (cid:242) (cid:668) (cid:349) (cid:264) (cid:384) (cid:242) (cid:691)(cid:740) (cid:667) (cid:302) (cid:740) (cid:270) (cid:714) (cid:242)(cid:270) (cid:667)(cid:668) (cid:349)(cid:691) (cid:242)(cid:264) (cid:667) (cid:384) (cid:740)(cid:294) (cid:270) (cid:667)(cid:740) (cid:242)(cid:349) (cid:667) (cid:270) (cid:242) (cid:692) (cid:667)(cid:691) (cid:264) (cid:340) (cid:384) (cid:294) (cid:270) (cid:667) (cid:403) (cid:740) (cid:242) (cid:667) (cid:349) (cid:692) (cid:242) (cid:740) (cid:340) (cid:294) (cid:667) (cid:294) (cid:691) (cid:668) (cid:667) (cid:403)(cid:270) (cid:349) (cid:242) (cid:667) (cid:740) (cid:692) (cid:29)(cid:740) (cid:242) (cid:340) (cid:294) (cid:740) (cid:242) (cid:668) (cid:403) (cid:667) (cid:294) (cid:667) (cid:270) (cid:301) (cid:349)(cid:740) (cid:29) (cid:667)(cid:740)(cid:230)(cid:692) (cid:242)(cid:294) (cid:740) (cid:668) (cid:340) (cid:403) (cid:294) (cid:667) (cid:301)(cid:740) (cid:29) (cid:740) (cid:349) (cid:230) (cid:242)(cid:270) (cid:740) (cid:740)(cid:692) (cid:294) (cid:668) (cid:340) (cid:403) (cid:301) (cid:273)(cid:740) (cid:230) (cid:740) (cid:309)(cid:29)(cid:270) (cid:242) (cid:740) (cid:740) (cid:294) (cid:668) (cid:302) (cid:202) (cid:273)(cid:740) (cid:301) (cid:309) (cid:270) (cid:309) (cid:230) (cid:740) (cid:29) (cid:242) (cid:740) (cid:302) (cid:202) (cid:273) (cid:309) (cid:309) (cid:740) (cid:301) (cid:309)(cid:270) (cid:230)(cid:291) (cid:302) (cid:231) (cid:202) (cid:273) (cid:309) (cid:403) (cid:309) (cid:309) (cid:740) (cid:291) (cid:270) (cid:231)(cid:302) (cid:202) (cid:291) (cid:309) (cid:231)(cid:273)(cid:403) (cid:273) (cid:309) (cid:309) (cid:309) (cid:291) (cid:231) (cid:291) (cid:302)(cid:231) (cid:202) (cid:302) (cid:403) (cid:309) (cid:273) (cid:309) (cid:309) (cid:242) (cid:729) (cid:291) (cid:231) (cid:291) (cid:231) (cid:302)(cid:273) (cid:343) (cid:309) (cid:349)(cid:403) (cid:309) (cid:242) (cid:729) (cid:291) (cid:231) (cid:302) (cid:291)(cid:264) (cid:231) (cid:343) (cid:349) (cid:273) (cid:740)(cid:309) (cid:403) (cid:340) (cid:242) (cid:729) (cid:740) (cid:264) (cid:343) (cid:349) (cid:302) (cid:639) (cid:291) (cid:231) (cid:740) (cid:340) (cid:273) (cid:309) (cid:231)(cid:242) (cid:729)(cid:740) (cid:264) (cid:740) (cid:639) (cid:343) (cid:740) (cid:349) (cid:302) (cid:340) (cid:309) (cid:231)(cid:740) (cid:242) (cid:729)(cid:407) (cid:740) (cid:740) (cid:639) (cid:264) (cid:309) (cid:309) (cid:343) (cid:740) (cid:349)(cid:231) (cid:340)(cid:309) (cid:740) (cid:407) (cid:740) (cid:740) (cid:309) (cid:309) (cid:639) (cid:264) (cid:343) (cid:309) (cid:740) (cid:231) (cid:340)(cid:309) (cid:407) (cid:740) (cid:740) (cid:302) (cid:309) (cid:309) (cid:740) (cid:343) (cid:639) (cid:309) (cid:202) (cid:409) (cid:309) (cid:231) (cid:407) (cid:740) (cid:343) (cid:302) (cid:309) (cid:343) (cid:309) (cid:740) (cid:202) (cid:409)(cid:309) (cid:309) (cid:263) (cid:343) (cid:302) (cid:356) (cid:407) (cid:740) (cid:309) (cid:740) (cid:412) (cid:343) (cid:309) (cid:202) (cid:409)(cid:263) (cid:343) (cid:309)(cid:356) (cid:242) (cid:202)(cid:302) (cid:740) (cid:412) (cid:242) (cid:309) (cid:343) (cid:273) (cid:202) (cid:409)(cid:263) (cid:356) (cid:242) (cid:202)(cid:343)(cid:740) (cid:412) (cid:242) (cid:302) (cid:302)(cid:273) (cid:202) (cid:409) (cid:343) (cid:740) (cid:263)(cid:302)(cid:242) (cid:202) (cid:356)(cid:242) (cid:343) (cid:302) (cid:740) (cid:412)(cid:273) (cid:231) (cid:343) (cid:740) (cid:302)(cid:263) (cid:349) (cid:242) (cid:202) (cid:356) (cid:302) (cid:264) (cid:242) (cid:740) (cid:412)(cid:273) (cid:231) (cid:343) (cid:740) (cid:302) (cid:412) (cid:349) (cid:309) (cid:264) (cid:242) (cid:202) (cid:302) (cid:242) (cid:231) (cid:740)(cid:273) (cid:343) (cid:740) (cid:412) (cid:349) (cid:302) (cid:667) (cid:309) (cid:264) (cid:740) (cid:202)(cid:302)(cid:740) (cid:231) (cid:740) (cid:412) (cid:343) (cid:740) (cid:270) (cid:411) (cid:667) (cid:349) (cid:309) (cid:302) (cid:740)(cid:264) (cid:202)(cid:740)(cid:71)(cid:740) (cid:231) (cid:412) (cid:270) (cid:667) (cid:411) (cid:302)(cid:740) (cid:349) (cid:309) (cid:202) (cid:270) (cid:264) (cid:412)(cid:71) (cid:740) (cid:740) (cid:270) (cid:411) (cid:242) (cid:302) (cid:412)(cid:667) (cid:270)(cid:740) (cid:309) (cid:202) (cid:71)(cid:412)(cid:740)(cid:740) (cid:740) (cid:242) (cid:302) (cid:740) (cid:270) (cid:411)(cid:270) (cid:242) (cid:667)(cid:412) (cid:740) (cid:231)(cid:202) (cid:71)(cid:740) (cid:343) (cid:273) (cid:242) (cid:740) (cid:740)(cid:302) (cid:242) (cid:270) (cid:411)(cid:270) (cid:231)(cid:412)(cid:740) (cid:343) (cid:302) (cid:71) (cid:273)(cid:740) (cid:740) (cid:242) (cid:242) (cid:309) (cid:242) (cid:302) (cid:231) (cid:270) (cid:343) (cid:302) (cid:412)(cid:740) (cid:273) (cid:343)(cid:740) (cid:242) (cid:309) (cid:740) (cid:242) (cid:242) (cid:231) (cid:302) (cid:356) (cid:302) (cid:343) (cid:343) (cid:740) (cid:242) (cid:740) (cid:273)(cid:302) (cid:309) (cid:242) (cid:740) (cid:242)(cid:356) (cid:302) (cid:343) (cid:231) (cid:302) (cid:242) (cid:343) (cid:302) (cid:242)(cid:740) (cid:242) (cid:273) (cid:309) (cid:356) (cid:302) (cid:412) (cid:342) (cid:242) (cid:343) (cid:302) (cid:302)(cid:302) (cid:242)(cid:740) (cid:242) (cid:309) (cid:343) (cid:412) (cid:356) (cid:342) (cid:302) (cid:242) (cid:302) (cid:740) (cid:343) (cid:302) (cid:242) (cid:343) (cid:412) (cid:342) (cid:340) (cid:361) (cid:302) (cid:740) (cid:356) (cid:242) (cid:302) (cid:242)(cid:242) (cid:302) (cid:242) (cid:343) (cid:340) (cid:361) (cid:412)(cid:740) (cid:242) (cid:342) (cid:242)(cid:302) (cid:242) (cid:349) (cid:340) (cid:231) (cid:361) (cid:273) (cid:343) (cid:202) (cid:242) (cid:242) (cid:412)(cid:740) (cid:342) (cid:302) (cid:343) (cid:349) (cid:231) (cid:273) (cid:202)(cid:340) (cid:361) (cid:343)(cid:242) (cid:242) (cid:740) (cid:412) (cid:356) (cid:349) (cid:343) (cid:349) (cid:231) (cid:273) (cid:202) (cid:242) (cid:340) (cid:361) (cid:242) (cid:412) (cid:242) (cid:356) (cid:349) (cid:273)(cid:343) (cid:349)(cid:349) (cid:231) (cid:242)(cid:273) (cid:202) (cid:349) (cid:412) (cid:356) (cid:302) (cid:349) (cid:273) (cid:349) (cid:237) (cid:343)(cid:242) (cid:349) (cid:231) (cid:273) (cid:202) (cid:349) (cid:740) (cid:302)(cid:412)(cid:273) (cid:356)(cid:349) (cid:237) (cid:349) (cid:202) (cid:343)(cid:242) (cid:411) (cid:349) (cid:740) (cid:302) (cid:264) (cid:412) (cid:237) (cid:273) (cid:356)(cid:202) (cid:740) (cid:349) (cid:349) (cid:411)(cid:740) (cid:242) (cid:349) (cid:270) (cid:264) (cid:264) (cid:302) (cid:242) (cid:202) (cid:740)(cid:237) (cid:273) (cid:349)(cid:411)(cid:270)(cid:740) (cid:264) (cid:349) (cid:740) (cid:264) (cid:242)(cid:740) (cid:302) (cid:202) (cid:237) (cid:411)(cid:270) (cid:340) (cid:302) (cid:242) (cid:264) (cid:740) (cid:242) (cid:740)(cid:242) (cid:264) (cid:740) (cid:202) (cid:340) (cid:302) (cid:242) (cid:411) (cid:740) (cid:270) (cid:242)(cid:264) (cid:242) (cid:264) (cid:740) (cid:740)(cid:340) (cid:302) (cid:242)(cid:667) (cid:242) (cid:237) (cid:242) (cid:740) (cid:270) (cid:264) (cid:242) (cid:740) (cid:340)(cid:740) (cid:667) (cid:242) (cid:237) (cid:340) (cid:302) (cid:242) (cid:242) (cid:740) (cid:740) (cid:740) (cid:340)(cid:740) (cid:343) (cid:667) (cid:242) (cid:237) (cid:740) (cid:340) (cid:691) (cid:302) (cid:242)(cid:740) (cid:242)(cid:740) (cid:340) (cid:202) (cid:343) (cid:349) (cid:740) (cid:740) (cid:349) (cid:667) (cid:242) (cid:237) (cid:691)(cid:740) (cid:667) (cid:202) (cid:343) (cid:740) (cid:340) (cid:349)(cid:740) (cid:349) (cid:667)(cid:740) (cid:691)(cid:667) (cid:242) (cid:237) (cid:343) (cid:667) (cid:242) (cid:740) (cid:202) (cid:340) (cid:667) (cid:349) (cid:343) (cid:740) (cid:340) (cid:349) (cid:667) (cid:740) (cid:692) (cid:667) (cid:343) (cid:691) (cid:242) (cid:340) (cid:667) (cid:202) (cid:740) (cid:202) (cid:349) (cid:667) (cid:343)(cid:349) (cid:302) (cid:692) (cid:740) (cid:343) (cid:242) (cid:740) (cid:667) (cid:340) (cid:691)(cid:667) (cid:242) (cid:202) (cid:202) (cid:349) (cid:667) (cid:302) (cid:692) (cid:154) (cid:349) (cid:740) (cid:264) (cid:343) (cid:242) (cid:242) (cid:202) (cid:667) (cid:340) (cid:667) (cid:302) (cid:356) (cid:154) (cid:667)(cid:740) (cid:231) (cid:692) (cid:264) (cid:242) (cid:343) (cid:242) (cid:202) (cid:340) (cid:667) (cid:356) (cid:154) (cid:302) (cid:231) (cid:264) (cid:242) (cid:270) (cid:343) (cid:740)(cid:692) (cid:242) (cid:202) (cid:412)(cid:356) (cid:231) (cid:154) (cid:242) (cid:270) (cid:343) (cid:302) (cid:264) (cid:740) (cid:202)(cid:242) (cid:412) (cid:302) (cid:403)(cid:356)(cid:242) (cid:270) (cid:343) (cid:231) (cid:154) (cid:242)(cid:264) (cid:202) (cid:412) (cid:383) (cid:302) (cid:403)(cid:356) (cid:242) (cid:340) (cid:242) (cid:270) (cid:343) (cid:231) (cid:202) (cid:383)(cid:412) (cid:302) (cid:403) (cid:231) (cid:740) (cid:242) (cid:340) (cid:242)(cid:242) (cid:270) (cid:343)(cid:202) (cid:383) (cid:231) (cid:412) (cid:302) (cid:740) (cid:403) (cid:230)(cid:340) (cid:270) (cid:242) (cid:242) (cid:242) (cid:202) (cid:231) (cid:383) (cid:740)(cid:230) (cid:302)(cid:740) (cid:270)(cid:403) (cid:340) (cid:242) (cid:242) (cid:242) (cid:231)(cid:230) (cid:230) (cid:383) (cid:740) (cid:242)(cid:270) (cid:740) (cid:349) (cid:349) (cid:242) (cid:340) (cid:242)(cid:230)(cid:740) (cid:242) (cid:231) (cid:230) (cid:349) (cid:349) (cid:270) (cid:740) (cid:242) (cid:242)(cid:740) (cid:668) (cid:230) (cid:349) (cid:390) (cid:242) (cid:349) (cid:349) (cid:740) (cid:230) (cid:740) (cid:270) (cid:384)(cid:740) (cid:242) (cid:668) (cid:349) (cid:390)(cid:230) (cid:242) (cid:349) (cid:349) (cid:349)(cid:740) (cid:740)(cid:384) (cid:412) (cid:740) (cid:740) (cid:668) (cid:349) (cid:390) (cid:349) (cid:230) (cid:740) (cid:242) (cid:361) (cid:349) (cid:349) (cid:384) (cid:412) (cid:740) (cid:242) (cid:740) (cid:668) (cid:740) (cid:403) (cid:349) (cid:390) (cid:349) (cid:361) (cid:412) (cid:740) (cid:740) (cid:384) (cid:242) (cid:412) (cid:740) (cid:403) (cid:231)(cid:740) (cid:668) (cid:349) (cid:390) (cid:349) (cid:361) (cid:349) (cid:242) (cid:412) (cid:740) (cid:740) (cid:242) (cid:412) (cid:384) (cid:740) (cid:403) (cid:231) (cid:270) (cid:349)(cid:349) (cid:361) (cid:242) (cid:270)(cid:412) (cid:412) (cid:740) (cid:231) (cid:242)(cid:273) (cid:270) (cid:740) (cid:403) (cid:349) (cid:301) (cid:242) (cid:270) (cid:361) (cid:302) (cid:412) (cid:273) (cid:270) (cid:740) (cid:231) (cid:242) (cid:740) (cid:403) (cid:301) (cid:349) (cid:270) (cid:242) (cid:302) (cid:309) (cid:273)(cid:411)(cid:740) (cid:412)(cid:270) (cid:231) (cid:301) (cid:349)(cid:302) (cid:309) (cid:264) (cid:270) (cid:242) (cid:411)(cid:740) (cid:273)(cid:270) (cid:349) (cid:270) (cid:301) (cid:309) (cid:403) (cid:264) (cid:411) (cid:302) (cid:270) (cid:270)(cid:740) (cid:273) (cid:349) (cid:301) (cid:403) (cid:264) (cid:231) (cid:740) (cid:740) (cid:309) (cid:411) (cid:302) (cid:270) (cid:242) (cid:349) (cid:740) (cid:403) (cid:411) (cid:408) (cid:231) (cid:740) (cid:740) (cid:264) (cid:309) (cid:242) (cid:411)(cid:270) (cid:349) (cid:242) (cid:411) (cid:408) (cid:231) (cid:740) (cid:740) (cid:403) (cid:740) (cid:270) (cid:309) (cid:264) (cid:242)(cid:270)(cid:242) (cid:349) (cid:411) (cid:408) (cid:411) (cid:231) (cid:740) (cid:270) (cid:309) (cid:740) (cid:740) (cid:403) (cid:242)(cid:740) (cid:242) (cid:411) (cid:411) (cid:408) (cid:740) (cid:740) (cid:270) (cid:309)(cid:242) (cid:270) (cid:231) (cid:740) (cid:740) (cid:740)(cid:403)(cid:242) (cid:242) (cid:294) (cid:411) (cid:740) (cid:242) (cid:411) (cid:408) (cid:270)(cid:740) (cid:270) (cid:309) (cid:740)(cid:403)(cid:349) (cid:202)(cid:294) (cid:740) (cid:242) (cid:740) (cid:242) (cid:411)(cid:270) (cid:242) (cid:740) (cid:270) (cid:309) (cid:403)(cid:349)(cid:740) (cid:202)(cid:294) (cid:740) (cid:740) (cid:740) (cid:242) (cid:411) (cid:242) (cid:270) (cid:349) (cid:231) (cid:403) (cid:202) (cid:740) (cid:740)(cid:301) (cid:294) (cid:740) (cid:242)(cid:639) (cid:740) (cid:242) (cid:270) (cid:231) (cid:349)(cid:403) (cid:202) (cid:301) (cid:740) (cid:740)(cid:639) (cid:294) (cid:291) (cid:242) (cid:231) (cid:349) (cid:301) (cid:202) (cid:667) (cid:639) (cid:291) (cid:740) (cid:740) (cid:242) (cid:231) (cid:740) (cid:242) (cid:667) (cid:301) (cid:291) (cid:639)(cid:740) (cid:202) (cid:231) (cid:740) (cid:242) (cid:667) (cid:301) (cid:291) (cid:639) (cid:202) (cid:740) (cid:740) (cid:242) (cid:667) (cid:291) (cid:740) (cid:309) (cid:202) (cid:740) (cid:740) (cid:242) (cid:667) (cid:740) (cid:309)(cid:740) (cid:202)(cid:740) (cid:242) (cid:740) (cid:409) (cid:309)(cid:740) (cid:202) (cid:409) (cid:740) (cid:309) (cid:740) (cid:740)(cid:409)(cid:740) (cid:740) (cid:309)(cid:409)(cid:740)(cid:409)(cid:740)(cid:740)
Figure4: AstepofdeliberatesearchinarandomlypickedCreativeWritingtask. Giventheinput,the
LMsamples5differentplans,thenvotes5timestodecidewhichplanisbest. Themajoritychoiceis
usedtoconsequentlywritetheoutputpassagewiththesamesample-voteprocedure.
(a) GPT-4 coherency scores (b) Human coherency comparison Method SuccessRate(%)
40 LetterWord Game
8
IO 38.7 14 0
30
CoT 40.6 15.6 1
6 20 38 41 ToT(ours) 78 60 20
+beststate 82.4 67.5 35
4 10 21
-prune 65.4 41.5 5
-backtrack 54.6 20 5
IO CoT ToT IO ToT 0
+refine+refine CoT > ToT Similar ToT > CoT Table3: MiniCrosswordsresults.
Figure5: CreativeWritingresults.
itimprovesIOcoherencyscorefrom6.19to7.67,andToTcoherencyscorefrom7.56to7.91. We
believeitcouldbethoughtofasathirdapproachtothoughtgenerationintheToTframework,where
newthoughtscanarisefromrefiningoldthoughtsinsteadofi.i.d.orsequentiallygenerated.
4.3 Minicrosswords
InGameof24andCreativeWriting,ToTisrelativelyshallow—atmost3thoughtstepsareneeded
toreachthefinaloutput. Hereweexplore5×5minicrosswordsasahardersearchprobleminvolving
naturallanguage. Again,thegoalisnotjusttosolvethetask,asmoregeneralcrosswordscanbe
readilysolvedwithspecializedNLPpipelines[34]thatleverageslarge-scaleretrievalinsteadofLM.
Rather,weaimtoexplorethelimitofLMasageneralproblemsolverthatexploresitsownthoughts
andguidesitsownexplorationwithdeliberatereasoningasheuristics.
Tasksetup. WescrapedatafromGooBix,whichcontains156gamesof5×5minicrosswords. As
weobserveadjacentgamescontainsimilarclues,weuse20gameswithindices1,6,···,91,96for
testing,andgames136,141,146,151,156forprompting. Foreachtask,theinputdescribesthe5
horizontalcluesand5verticalclues,andtheoutputshouldbeaboardof5×5=25letterstosolve
thecrosswords. Forevaluation,weconsiderthreelevelsofsuccess: theportionofcorrectletters(25
pergame),words(10pergame),andgames.
Baselines. We provide 5 example input-output pairs in the IO prompt, and in the CoT prompt
additionallyincludeintermediatewordsintheorderh1..5thenv1..5. Weruneachpromptfor10
samplesandaveragetheresults.
ToTsetup. Weleverageadepth-firstsearch(Algorithm2)thatkeepsexploringthemostpromising
subsequentwordclueuntilthestateisnolongerpromising, thenbacktracktotheparentstateto
explorealternativethoughts. Tomakesearchtractable,subsequentthoughtsareconstrainednotto
changeanyfilledwordsorletters,sothattheToThasatmost10intermediatesteps. Forthought
generation, ateachstatewetranslateallexistingthoughts(e.g.“h2.motor; h1.tasks”forthestate
inFigure6(a))intoletterconstraintsforremainingclues(e.g.“v1.Toheap: tm ;...”) andprompt
aproposalprompt5timestocomeupwithcandidatesforwhereandwhattofillinthenextword.
Importantly,wealsoprompttheLMtogiveaconfidencelevelfordifferentthoughts,andaggregate
7

(cid:408)(cid:202)(cid:349)(cid:291)(cid:349)
(cid:408)(cid:202)(cid:349)(cid:291)(cid:349)
(cid:48)(cid:88)(cid:79)(cid:87)(cid:76)(cid:83)(cid:79)(cid:72)(cid:3)
(cid:85)(cid:88)(cid:81)(cid:86)
(cid:51)(cid:68)(cid:85)(cid:86)(cid:72)(cid:15)(cid:3)(cid:73)(cid:76)(cid:79)(cid:87)(cid:72)(cid:85)(cid:3)(cid:82)(cid:88)(cid:87)(cid:3)
(cid:11)(cid:86)(cid:82)(cid:73)(cid:87)(cid:3)
(cid:81)(cid:82)(cid:81)(cid:16)(cid:73)(cid:76)(cid:89)(cid:72)(cid:16)(cid:79)(cid:72)(cid:87)(cid:87)(cid:72)(cid:85)(cid:15)(cid:3)
(cid:86)(cid:72)(cid:79)(cid:73)(cid:16)(cid:70)(cid:82)(cid:81)(cid:86)(cid:76)(cid:86)(cid:87)(cid:72)(cid:81)(cid:70)(cid:92)(cid:34)(cid:12)
(cid:86)(cid:70)(cid:82)(cid:85)(cid:72)(cid:15)(cid:3)(cid:68)(cid:74)(cid:74)(cid:85)(cid:72)(cid:74)(cid:68)(cid:87)(cid:72)
(cid:62)(cid:11)(cid:10)(cid:89)(cid:22)(cid:17)(cid:3)(cid:72)(cid:79)(cid:82)(cid:83)(cid:72)(cid:10)(cid:15)(cid:3)(cid:22)(cid:17)(cid:21)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:75)(cid:21)(cid:17)(cid:3)(cid:89)(cid:68)(cid:79)(cid:88)(cid:72)(cid:10)(cid:15)(cid:3)(cid:21)(cid:17)(cid:19)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:75)(cid:20)(cid:17)(cid:3)(cid:83)(cid:68)(cid:85)(cid:70)(cid:75)(cid:10)(cid:15)(cid:3)
(cid:20)(cid:17)(cid:28)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:89)(cid:24)(cid:17)(cid:3)(cid:70)(cid:82)(cid:89)(cid:72)(cid:87)(cid:10)(cid:15)(cid:3)(cid:19)(cid:17)(cid:25)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:19)(cid:20)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:75)(cid:21)(cid:17)(cid:3)
(cid:80)(cid:72)(cid:85)(cid:76)(cid:87)(cid:10)(cid:15)(cid:3)(cid:19)(cid:17)(cid:23)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:89)(cid:20)(cid:17)(cid:3)(cid:68)(cid:79)(cid:79)(cid:82)(cid:90)(cid:10)(cid:15)(cid:3)(cid:19)(cid:17)(cid:21)(cid:12)(cid:15)(cid:3)(cid:11)(cid:10)(cid:89)(cid:21)(cid:17)(cid:3)(cid:74)(cid:85)(cid:76)(cid:81)(cid:71)(cid:10)(cid:15)(cid:3)(cid:19)(cid:17)(cid:20)(cid:12)(cid:15)(cid:3)
(cid:11)(cid:10)(cid:75)(cid:23)(cid:17)(cid:3)(cid:79)(cid:72)(cid:83)(cid:72)(cid:85)(cid:10)(cid:15)(cid:3)(cid:19)(cid:17)(cid:20)(cid:12)(cid:64)
(cid:20)(cid:17) (cid:48)(cid:68)(cid:91)
(cid:21)(cid:17) (cid:48)(cid:68)(cid:91)(cid:3)(cid:90)(cid:76)(cid:87)(cid:75)(cid:82)(cid:88)(cid:87)(cid:3)
(cid:38)(cid:75)(cid:82)(cid:82)(cid:86)(cid:72)(cid:3)
(cid:89)(cid:76)(cid:82)(cid:79)(cid:68)(cid:87)(cid:72)
(cid:22)(cid:17) (cid:39)(cid:41)(cid:54)
(cid:10)(cid:89)(cid:22)(cid:17)(cid:3)(cid:72)(cid:79)(cid:82)(cid:83)(cid:72)(cid:10)
(cid:411)(cid:740)(cid:202)(cid:740)(cid:349)(cid:740)(cid:291)(cid:740)(cid:349) (cid:71)(cid:302)(cid:340)(cid:361)(cid:412)(cid:740)(cid:29)(cid:294)(cid:361)(cid:242)(cid:349) (cid:689)(cid:202)(cid:690)
(cid:301)(cid:740)(cid:309)(cid:740)(cid:411)(cid:740)(cid:309)(cid:740)(cid:343) (cid:55)(cid:55)(cid:75) (cid:55) (cid:75) (cid:55) (cid:82) (cid:75) (cid:82) (cid:75) (cid:88) (cid:82) (cid:88) (cid:82) (cid:74) (cid:88) (cid:74) (cid:88) (cid:75) (cid:74) (cid:75) (cid:74) (cid:87) (cid:75) (cid:87) (cid:75) (cid:3) (cid:87) (cid:3) (cid:87) (cid:51) (cid:3) (cid:51) (cid:3) (cid:85) (cid:51) (cid:85) (cid:51) (cid:82) (cid:85) (cid:82) (cid:85) (cid:83) (cid:82) (cid:83) (cid:82) (cid:82) (cid:83) (cid:82) (cid:83) (cid:86) (cid:82) (cid:86) (cid:82) (cid:68) (cid:86) (cid:68) (cid:86) (cid:79) (cid:68) (cid:79) (cid:68) (cid:86) (cid:79) (cid:86) (cid:79) (cid:86) (cid:86) (cid:39)(cid:41)(cid:54)(cid:3)
(cid:712)(cid:740)(cid:712)(cid:740)(cid:712)(cid:740)(cid:712)(cid:740)(cid:712) (cid:270)(cid:270)(cid:641) (cid:270) (cid:641)(cid:667)(cid:740) (cid:641) (cid:667)(cid:349)(cid:740) (cid:667) (cid:349)(cid:55)(cid:202) (cid:740)(cid:349) (cid:202)(cid:294)(cid:75)(cid:309) (cid:202) (cid:294)(cid:309)(cid:82) (cid:294) (cid:302) (cid:309) (cid:302)(cid:740)(cid:88) (cid:302) (cid:689)(cid:740)(cid:349)(cid:689)(cid:74) (cid:740) (cid:349)(cid:361) (cid:689)(cid:349) (cid:75)(cid:361)(cid:343) (cid:361) (cid:242)(cid:343)(cid:87)(cid:242) (cid:343) (cid:690)(cid:3) (cid:242) (cid:690) (cid:690) (cid:51)(cid:85)(cid:82)(cid:83)(cid:82)(cid:86)(cid:68)(cid:79)(cid:86) (cid:50)(cid:85)(cid:71)(cid:72)(cid:85)
(cid:349) (cid:712) (cid:740) (cid:740) (cid:202) (cid:712) (cid:740) (cid:740) (cid:294) (cid:712) (cid:740)(cid:309) (cid:740)(cid:712) (cid:740)(cid:302) (cid:740)(cid:712) (cid:270)(cid:639)(cid:667)(cid:301)(cid:309)(cid:356)(cid:309)(cid:343) (cid:383) (cid:383) (cid:383) (cid:383) (cid:642) (cid:640) (cid:383) (cid:383) (cid:642) (cid:640) (cid:667) (cid:667) (cid:740) (cid:740) (cid:270) (cid:383) (cid:642) (cid:640) (cid:667) (cid:667) (cid:349) (cid:349) (cid:740) (cid:740) (cid:270) (cid:383) (cid:642) (cid:667) (cid:667) (cid:349) (cid:349) (cid:641)(cid:343) (cid:412) (cid:740) (cid:740)(cid:642) (cid:349) (cid:349) (cid:641) (cid:343)(cid:667) (cid:237)(cid:343) (cid:412)(cid:740) (cid:667)(cid:740) (cid:273)(cid:343) (cid:237) (cid:667) (cid:343) (cid:412) (cid:349) (cid:343) (cid:740) (cid:667) (cid:349) (cid:302)(cid:273) (cid:740) (cid:343) (cid:237) (cid:349) (cid:343) (cid:390)(cid:343) (cid:302) (cid:349) (cid:202) (cid:273) (cid:264)(cid:237) (cid:343) (cid:390) (cid:343) (cid:302) (cid:740) (cid:202) (cid:294) (cid:264)(cid:237) (cid:689) (cid:390) (cid:740) (cid:740)(cid:309) (cid:343) (cid:294) (cid:294) (cid:264) (cid:689) (cid:689) (cid:740)(cid:390) (cid:740) (cid:309) (cid:309) (cid:343) (cid:270) (cid:294)(cid:302) (cid:689) (cid:689) (cid:740)(cid:390) (cid:309) (cid:740)(cid:270) (cid:294) (cid:384) (cid:302) (cid:689) (cid:403)(cid:689) (cid:740) (cid:309) (cid:740)(cid:270) (cid:264) (cid:384)(cid:689) (cid:294)(cid:403)(cid:689) (cid:740) (cid:690) (cid:309) (cid:349) (cid:264) (cid:384)(cid:689) (cid:294)(cid:403) (cid:270) (cid:690) (cid:309) (cid:349) (cid:264) (cid:361) (cid:384)(cid:270) (cid:690) (cid:690) (cid:361) (cid:384) (cid:343) (cid:270) (cid:690)(cid:690) (cid:242) (cid:343) (cid:690)(cid:690) (cid:242) (cid:690) (cid:690) (cid:202)(cid:264)(cid:264)(cid:343)(cid:242)(cid:264)(cid:202)(cid:356)(cid:242) (cid:270) (cid:270) (cid:641) (cid:640)(cid:667) (cid:667) (cid:740) (cid:740) (cid:264) (cid:349)(cid:202) (cid:343)(cid:202) (cid:294)(cid:309) (cid:302) (cid:302) (cid:237)
(cid:671)(cid:671)(cid:671) (cid:671) (cid:671)(cid:383) (cid:671)(cid:383) (cid:640) (cid:640) (cid:667)(cid:740) (cid:667) (cid:349) (cid:740)(cid:349) (cid:412)(cid:343) (cid:412) (cid:273) (cid:343) (cid:302) (cid:273)(cid:302) (cid:264) (cid:264) (cid:740)(cid:689) (cid:740) (cid:270) (cid:689)(cid:270) (cid:403)(cid:264) (cid:403)(cid:264) (cid:270) (cid:270) (cid:690) (cid:690) (cid:383)(cid:640)(cid:667)(cid:740)(cid:349)(cid:412)(cid:343)(cid:273)(cid:302)(cid:264)
(cid:270)(cid:638)(cid:667)(cid:408)(cid:202)(cid:349)(cid:291)(cid:349) (cid:671) (cid:671) (cid:671) (cid:671) (cid:671)(cid:671)
(cid:689)(cid:230)(cid:690)
(cid:689)(cid:230)(cid:202)(cid:231)(cid:291)(cid:412)(cid:343)(cid:202)(cid:231)(cid:291)(cid:690)
(cid:54)(cid:87)(cid:68)(cid:87)(cid:72)(cid:3)(cid:40)(cid:89)(cid:68)(cid:79)(cid:88)(cid:68)(cid:87)(cid:82)(cid:85)(cid:3)(cid:11)(cid:82)(cid:89)(cid:72)(cid:85)(cid:3)(cid:72)(cid:68)(cid:70)(cid:75)(cid:3)(cid:70)(cid:79)(cid:88)(cid:72)(cid:12)
(cid:383)(cid:640)(cid:667)(cid:740)(cid:137)(cid:343)(cid:242)(cid:356)(cid:242)(cid:302)(cid:412)(cid:403)(cid:309)(cid:361)(cid:349)(cid:670)(cid:740)(cid:410)(cid:294)(cid:309)(cid:384)(cid:242)(cid:343)(cid:390)(cid:669)(cid:740)(cid:712)(cid:712)(cid:712)(cid:712)(cid:712)(cid:740)(cid:349)(cid:361)(cid:343)(cid:242)
(cid:270)(cid:640)(cid:667)(cid:264)(cid:343)(cid:202)(cid:302)(cid:237) (cid:270)(cid:641)(cid:667)(cid:349)(cid:202)(cid:294)(cid:309)(cid:302) (cid:383)(cid:638)(cid:667)(cid:740)(cid:201)(cid:309)(cid:740)(cid:270)(cid:242)(cid:202)(cid:340)(cid:669)(cid:740)(cid:411)(cid:301)(cid:712)(cid:349)(cid:712)(cid:740)(cid:691)(cid:667)(cid:667)(cid:667)(cid:692)(cid:740)(cid:273)(cid:301)(cid:340)(cid:309)(cid:349)(cid:349)(cid:273)(cid:230)(cid:294)(cid:242)
(cid:671)(cid:671)
(cid:671)(cid:671) (cid:689)(cid:349)(cid:361)(cid:230)(cid:412)(cid:343)(cid:242)(cid:242)(cid:740)(cid:340)(cid:343)(cid:361)(cid:302)(cid:242)(cid:237)(cid:690) (cid:383)(cid:642)(cid:667)(cid:740)(cid:35)(cid:242)(cid:349)(cid:403)(cid:231)(cid:231)(cid:202)(cid:356)(cid:309)(cid:343)(cid:670)(cid:740)(cid:301)(cid:309)(cid:343)(cid:242)(cid:740)(cid:237)(cid:343)(cid:390)(cid:669)(cid:740)(cid:349)(cid:343)(cid:712)(cid:302)(cid:712)(cid:740)(cid:691)(cid:667)(cid:667)(cid:667)(cid:692)(cid:740)(cid:301)(cid:202)(cid:390)(cid:230)(cid:242)
Figure6: InMiniCrosswords,(a)howthoughtsareproposedandaggregatedinapriorityqueue
fordepth-firstsearch(DFS),and(b)howastateisevaluatedbasedonthepossibilityoffillingin
eachremainingwordclue,andprunedifanyremainingclueisdeemednotpossibletofillbytheLM.
ThenDFSbacktrackstotheparentstateandexplorethenextpromisingthoughtforclue.
these across proposals to obtain a sorted list of next thoughts to explore (Figure 6(a)). For state
evaluations,wesimilarlytranslateeachstateintoletterconstraintsforremainingclues,thenevaluate
foreachclueifitispossibletofillgiventheconstraints. Ifanyremainingclueisdeemed“impossible”
tofillin(e.g.“v1. Toheap: tm s ”),thentheexplorationofthestate’ssubtreeisprunedandDFS
backtrackstoitsparenttoexplorethenextpromisingthought. WelimitDFSsearchstepsto100,and
simplyrenderthedeepestexploredstate(thefirstexploredoneifmultiple)intothefinaloutput.
Results. AsshowninTable3,IOandCoTpromptingmethodsperformpoorlywithaword-level
success rate less than 16%, while ToT significantly improves all metrics, achieving a word-level
successrateof60%andsolving4outof20games. Suchanimprovementisnotsurprising,givenIO
andCoTlackmechanismstotrydifferentclues,makechangestodecisions,orbacktrack.
Oracle and ablation studies. When outputting from the oracle best DFS state (instead of the
heuristicallydeterminedbeststate)pertask, ToTperformanceisevenhigherandactuallysolves
7/20games(Table3,“+beststate”),indicatingoursimpleoutputheuristicscanbereadilyimproved.
Interestingly,sometimeswhenthecrosswordsgameisactuallysolved,thestateevaluatormightstill
deemsomewordsas“impossible”andprune—possiblybecause5×5crosswordsbydesignhave
somerareorobseletewordsthatGPT-4cannotrecognize2. Giventhestateevaluationasapruning
heuristicisimperfect,wealsoexploreablatingthepruning,andfindtheperformancegenerallyworse
(Table3,“-prune”). However,itcouldactuallyfindthecorrectsolutionfor4/20games(thoughonly
outputting1viaheuristic),3ofwhicharegamesToT+pruningcannotsolvewithin100steps. Thus,
betterheuristicsforDFSpruningarecriticalforproblemsolvinginthiscase. Lastly,weconfirmthe
importanceofbacktrackingbyrunninganablationthatkeepsfillingthemostpromisingclueforat
most20steps,allowingoverwrites. Thisissimilartoa“greedy”BFSsearchwithbreadthlimitof
b=1,andperformspoorlywithawordlevelsuccessofonly20%(Table3,“-backtrack”).
5 RelatedWork
Planning and decision making. Smart planning and decision making are critical to achieving
predefinedgoals. Astheyaretrainedonvastamountofworldknowledgeandhumanexamples,LMs
areknowntohavealreadyabsorbedrichcommonsensethatmakesitpossibletoproposereasonable
plans conditioned on problem setting and environmental states [12, 42, 37, 13, 35, 41, 40]. Our
proposedToTapproachextendsexistingplanningformulationsbyconsideringmultiplepotentially
feasibleplanssimultaneouslyateachproblem-solvingstep,andproceedingwiththemostpromising
ones. Theintegrationbetweenthoughtsamplingandvaluefeedbackorganicallyintegratesplanning
anddecision-makingmechanisms,enablingeffectivesearchinsideasolutiontree. Ontheotherhand,
traditionaldecision-makingproceduresusuallyrequiretrainingdedicatedrewardandpolicymodels
as in reinforcement learning (for example CHAI [33]), whereas we use the LM itself to provide
thevalueestimatesfordecisionmaking. RAP[9]isaconcurrentworkthattreatslanguagemodel
2Forexample,“agend”isanobsoleteformof“agendum”,butGPT-4deemsitatypofor“agenda”.External
retrievalorwebinteractioncouldaugmentLMforproblemsolvingunderknowledgeuncertainty.
8

reasoningasplanningwithitsinternalworldmodel,andproposesaMCTS-basedmethodsimilarto
ToT.However,itstasksaresimplerthanours,anditsframeworklacksthemodularitytoincorporate
differenttreesearchalgorithms.
Self-reflection. Using LLMs to assess the viability of their own predictions is becoming an in-
creasingly important procedure in problem solving. [28, 20, 24] introduced the “self-reflection”
mechanism,inwhichLMsprovidefeedbacktotheirgenerationcandidates. [4]improvesLMscode
generationaccuracybyinjectingfeedbackmessagesgeneratedbytheLMitselfbasedonitscode
executionresults. Similarly,[17]alsointroduces“critic”orreviewstepsovertheactionsandstates,
deciding the next action to take in solving computer operation tasks. Another recent work very
relevant to ours is “self-eval guided decoding” [39]. Similar to our method, self-eval decoding
also follows a tree-search procedure with leaves sampled from stochastic beam search decoding,
whicharethenevaluatedbyLLMitselfwithcarefullypreparedself-evalprompts. Theirapproach
however,usesthePALformulation [8]whichrepresentsthoughtsascodes,whichmakesitdifficult
totacklechallengingtaskslikecreativewritingwhichweconsiderinthispaper. OurTree-of-Thought
formulationisthusmoreversatileandhandleschallengingtasksonwhichGPT-4onlyachievesvery
lowaccuracywithstandardprompts.
Program-guidedLLMgeneration.Ourproposalisalsorelatedtorecentadvancementsthatorganize
LM’sbehaviorwithsystematicprocedures[14,44,6,43]orsymbolicprogramguidance.Forexample,
Schlagetal.[27]embedsLMsinanalgorithmicsearchproceduretohelpsolveproblemslikequestion
answeringstep-by-step,inwhichthesearchtreesareexpandedbyrelevantparagraphsthatmight
provideanswers. Thisapproachhoweverdiffersfromoursinthattreesareexpandedbysampling
external paragraphs instead of the LM’s own thoughts, and there is no reflection or voting steps.
Anotherapproach,LLM+P[18],goesonestepfurtheranddelegatestheactualplanningprocesstoa
classicalplanner.
Classicalsearchmethods. Lastbutnotleast,ourapproachcanbetreatedasamodernrendition
ofclassicalsearchmethodsforproblemsolving. Forexampleitcanbeconsideredasaheuristic
searchalgorithmlikeA*[10],inwhichtheheuristicateachsearchnodeisprovidedbytheLM’sself-
assessment. Fromthisperspective,ourmethodisalsorelatedtoNeuroLogicA*esquedecoding[19],
whichisinspiredbyA*searchbutintroduceslook-aheadheuristicsthatareefficientforLMsto
improve the beam-search or top-k sampling decoding. This method however is constrained to
sentencegenerationtasks,whereasourframeworkaredesignedforcomplex,multi-stepproblem
solvingguardedbyvaluefeedback.
6 Discussion
Limitationsandfuturedirections. DeliberatesearchsuchasToTmightnotbenecessaryformany
existingtasksthatGPT-4alreadyexcelsat(seeAppendixB.1),andasaninitialstepthisworkonly
exploresthreerelativelysimpletasksthatchallengesGPT-4(seeAppendixB.2forsomeGPT-3.5
experimentresults)andcallsofbettersearchandplanningabilitiesincorporatedwithLMs. However,
as we begin to deploy LMs for more real-world decision making applications (e.g.coding, data
analysis,robotics,etc.),morecomplextaskscouldemergeandpresentnewopportunitiestostudy
theseresearchquestions. Also,searchmethodslikeToTrequiresmoreresources(e.g.GPT-4API
cost)thansamplingmethodsinordertoimprovetaskperformances,butthemodularflexibilityof
ToTallowsuserstocustomizesuchperformance-costtradeoffs,andongoingopen-sourceefforts[32]
shouldreadilyreducesuchcostsinthenearfuture. Moredetailsaboutcostandefficiencyarein
AppendixB.3. Lastly,thisworkfocusesonusinganoff-the-shelfLM,andfine-tuningLMsusing
aToT-stylehigh-levelcounterfactualdecisionmaking(e.g.deliberatingoverpotentialchoicesfor
thenextparagraph,insteadofpredictingthenexttoken)mightpresentopportunitiestoenhancethe
problem-solvingcapabilitiesofLMs.
Conclusion. Theassociative“System1”ofLMscanbebeneficiallyaugmentedbya“System2”
based on searching a tree of possible paths to the solution to a problem. The Tree of Thoughts
framework provides a way to translate classical insights about problem-solving into actionable
methods for contemporary LMs. At the same time, LMs address a weakness of these classical
methods,providingawaytosolvecomplexproblemsthatarenoteasilyformalized,suchascreative
writing. WeseethisintersectionofLMswithclassicalapproachestoAIasanexcitingdirection.
9

BroaderImpact
ToTisaframeworkthatempowersLMstomoreautonomouslyandintelligentlymakedecisions
and solve problems. While current tasks are limited to reasoning and search problems, future
applicationsinvolvinginteractionwithexternalenvironmentsorhumanscouldbringpotentialdanger,
e.g.facilitating harmful uses of LMs. On the other hand, ToT also improves the interpretability
ofmodeldecisionsandtheopportunityforhumanalignment,astheresultingrepresentationsare
readable,high-levellanguagereasoninginsteadofimplicit,low-leveltokenvalues.
Acknowledgements
SYandKNacknowledgesupportfromanOracleCollaborativeResearchawardandtheNational
ScienceFoundationunderGrantNo. 2239363. Anyopinions,findings,conclusions,orrecommenda-
tionsexpressedinthismaterialarethoseoftheauthor(s)anddonotnecessarilyreflecttheviewsof
theNationalScienceFoundation. SYisalsosupportedbytheHaroldW.DoddsFellowshipfrom
Princeton.
References
[1] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,A.Neelakantan,P.Shyam,
G. Sastry, A. Askell, et al. Language models are few-shot learners. Advances in neural
informationprocessingsystems,33:1877–1901,2020.
[2] C. Browne, E. J. Powley, D. Whitehouse, S. M. M. Lucas, P. I. Cowling, P. Rohlfshagen,
S.Tavener,D.P.Liebana,S.Samothrakis,andS.Colton. Asurveyofmontecarlotreesearch
methods. IEEETransactionsonComputationalIntelligenceandAIinGames,4:1–43,2012.
[3] M.Campbell,A.J.HoaneJr,andF.-h.Hsu. Deepblue. Artificialintelligence,134(1-2):57–83,
2002.
[4] X.Chen,M.Lin,N.Scha¨rli,andD.Zhou. Teachinglargelanguagemodelstoself-debug,2023.
[5] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W.
Chung,C.Sutton,S.Gehrmann,etal. Palm: Scalinglanguagemodelingwithpathways. arXiv
preprintarXiv:2204.02311,2022.
[6] A.CreswellandM.Shanahan. Faithfulreasoningusinglargelanguagemodels. arXivpreprint
arXiv:2208.14271,2022.
[7] N. D. Daw, Y. Niv, and P. Dayan. Uncertainty-based competition between prefrontal and
dorsolateralstriatalsystemsforbehavioralcontrol. Natureneuroscience, 8(12):1704–1711,
2005.
[8] L.Gao,A.Madaan,S.Zhou,U.Alon,P.Liu,Y.Yang,J.Callan,andG.Neubig. Pal: Program-
aidedlanguagemodels,2023.
[9] S.Hao,Y.Gu,H.Ma,J.J.Hong,Z.Wang,D.Z.Wang,andZ.Hu. Reasoningwithlanguage
modelisplanningwithworldmodel. arXivpreprintarXiv:2305.14992,2023.
[10] P.E.Hart, N.J.Nilsson, andB.Raphael. Aformalbasisfortheheuristicdeterminationof
minimumcostpaths. IEEETransactionsonSystemsScienceandCybernetics,4(2):100–107,
1968. doi: 10.1109/TSSC.1968.300136.
[11] P.E.Hart, N.J.Nilsson, andB.Raphael. Aformalbasisfortheheuristicdeterminationof
minimumcostpaths. IEEEtransactionsonSystemsScienceandCybernetics,4(2):100–107,
1968.
[12] W.Huang, P.Abbeel, D.Pathak, andI.Mordatch. Languagemodelsaszero-shotplanners:
Extractingactionableknowledgeforembodiedagents,2022.
[13] W.Huang,F.Xia,T.Xiao,H.Chan,J.Liang,P.Florence,A.Zeng,J.Tompson,I.Mordatch,
Y. Chebotar, et al. Inner monologue: Embodied reasoning through planning with language
models. arXivpreprintarXiv:2207.05608,2022.
10

[14] J. Jung, L. Qin, S. Welleck, F. Brahman, C. Bhagavatula, R. L. Bras, and Y. Choi. Maieu-
tic prompting: Logically consistent reasoning with recursive explanations. arXiv preprint
arXiv:2205.11822,2022.
[15] D.Kahneman. Thinking,fastandslow. Macmillan,2011.
[16] D.Kahneman,S.Frederick,etal.Representativenessrevisited:Attributesubstitutioninintuitive
judgment. Heuristicsandbiases: Thepsychologyofintuitivejudgment,49(49-81):74,2002.
[17] G.Kim,P.Baldi,andS.McAleer. Languagemodelscansolvecomputertasks,2023.
[18] B.Liu,Y.Jiang,X.Zhang,Q.Liu,S.Zhang,J.Biswas,andP.Stone. Llm+p: Empowering
largelanguagemodelswithoptimalplanningproficiency,2023.
[19] X. Lu, S. Welleck, P. West, L. Jiang, J. Kasai, D. Khashabi, R. L. Bras, L. Qin, Y. Yu,
R.Zellers,N.A.Smith,andY.Choi. Neurologica*esquedecoding:Constrainedtextgeneration
withlookaheadheuristics. InNorthAmericanChapteroftheAssociationforComputational
Linguistics,2021.
[20] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri,
S.Prabhumoye,Y.Yang,S.Welleck,B.P.Majumder,S.Gupta,A.Yazdanbakhsh,andP.Clark.
Self-refine: Iterativerefinementwithself-feedback,2023.
[21] A.Newell,J.C.Shaw,andH.A.Simon. Reportonageneralproblemsolvingprogram. InIFIP
congress,volume256,page64.Pittsburgh,PA,1959.
[22] A.Newell,H.A.Simon,etal. Humanproblemsolving. Prentice-Hall,1972.
[23] OpenAI. Gpt-4technicalreport. ArXiv,abs/2303.08774,2023.
[24] D.Paul,M.Ismayilzada,M.Peyrard,B.Borges,A.Bosselut,R.West,andB.Faltings. Refiner:
Reasoningfeedbackonintermediaterepresentations,2023.
[25] A.Radford,K.Narasimhan,T.Salimans,I.Sutskever,etal. Improvinglanguageunderstanding
bygenerativepre-training. OpenAIblog,2018.
[26] A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskever,etal. Languagemodelsare
unsupervisedmultitasklearners. OpenAIblog,1(8):9,2019.
[27] I.Schlag,S.Sukhbaatar,A.Celikyilmaz,W.tauYih,J.Weston,J.Schmidhuber,andX.Li.
Largelanguagemodelprograms,2023.
[28] N.Shinn,B.Labash,andA.Gopinath. Reflexion: anautonomousagentwithdynamicmemory
andself-reflection,2023.
[29] D.Silver,J.Schrittwieser,K.Simonyan,I.Antonoglou,A.Huang,A.Guez,T.Hubert,L.Baker,
M.Lai,A.Bolton,etal. Masteringthegameofgowithouthumanknowledge. nature,550
(7676):354–359,2017.
[30] S.A.Sloman. Theempiricalcasefortwosystemsofreasoning. Psychologicalbulletin,119(1):
3,1996.
[31] K.E.Stanovich. Whoisrational? Studiesofindividualdifferencesinreasoning. Psychology
Press,1999.
[32] H.Touvron,T.Lavril,G.Izacard,X.Martinet,M.-A.Lachaux,T.Lacroix,B.Rozie`re,N.Goyal,
E.Hambro, F.Azhar, etal. Llama: Openandefficientfoundationlanguagemodels. arXiv
preprintarXiv:2302.13971,2023.
[33] S.Verma,J.Fu,S.Yang,andS.Levine. Chai: Achatbotaifortask-orienteddialoguewith
offlinereinforcementlearning. InProceedingsofthe2022ConferenceoftheNorthAmerican
Chapter of theAssociation for Computational Linguistics: Human Language Technologies,
pages4471–4491,2022.
11

[34] E.Wallace,N.Tomlin,A.Xu,K.Yang,E.Pathak,M.Ginsberg,andD.Klein. Automated
crosswordsolving. arXivpreprintarXiv:2205.09665,2022.
[35] L.Wang,W.Xu,Y.Lan,Z.Hu,Y.Lan,R.K.-W.Lee,andE.-P.Lim. Plan-and-solveprompting:
Improvingzero-shotchain-of-thoughtreasoningbylargelanguagemodels,2023.
[36] X.Wang,J.Wei,D.Schuurmans,Q.Le,E.Chi,andD.Zhou. Self-consistencyimproveschain
ofthoughtreasoninginlanguagemodels. arXivpreprintarXiv:2203.11171,2022.
[37] Z.Wang,S.Cai,A.Liu,X.Ma,andY.Liang. Describe,explain,planandselect: Interactive
planningwithlargelanguagemodelsenablesopen-worldmulti-taskagents,2023.
[38] J.Wei,X.Wang,D.Schuurmans,M.Bosma,E.Chi,Q.Le,andD.Zhou. Chainofthought
promptingelicitsreasoninginlargelanguagemodels. arXivpreprintarXiv:2201.11903,2022.
[39] Y. Xie, K. Kawaguchi, Y. Zhao, X. Zhao, M.-Y. Kan, J. He, and Q. Xie. Decomposition
enhancesreasoningviaself-evaluationguideddecoding,2023.
[40] S.Yang,O.Nachum,Y.Du,J.Wei,P.Abbeel,andD.Schuurmans. Foundationmodelsfor
decisionmaking: Problems,methods,andopportunities,2023.
[41] S.Yao,J.Zhao,D.Yu,N.Du,I.Shafran,K.Narasimhan,andY.Cao. ReAct: Synergizing
reasoningandactinginlanguagemodels. arXivpreprintarXiv:2210.03629,2022.
[42] S. Zhang, Z. Chen, Y. Shen, M. Ding, J. B. Tenenbaum, and C. Gan. Planning with large
languagemodelsforcodegeneration. InTheEleventhInternationalConferenceonLearning
Representations,2023. URLhttps://openreview.net/forum?id=Lr8cOOtYbfL.
[43] D.Zhou,N.Scha¨rli,L.Hou,J.Wei,N.Scales,X.Wang,D.Schuurmans,C.Cui,O.Bousquet,
Q.Le,etal. Least-to-mostpromptingenablescomplexreasoninginlargelanguagemodels.
arXivpreprintarXiv:2205.10625,2022.
[44] X. Zhu, J. Wang, L. Zhang, Y. Zhang, R. Gan, J. Zhang, and Y. Yang. Solving math word
problemviacooperativereasoninginducedlanguagemodels. arXivpreprintarXiv:2210.16257,
2022.
12

A Code,Prompts,Trajectories
Allcodeisavailableathttps://github.com/princeton-nlp/tree-of-thought-llm.
All prompts are available at https://github.com/princeton-nlp/tree-of-thought-llm/
tree/master/src/tot/prompts.
Trajectories are available at https://github.com/princeton-nlp/tree-of-thought-llm/
tree/master/logs.
B AdditionalExperimentResults
Given the motivation of exploring and extending the capability frontier of language models, our
experiments in the main paper have focused on a setup with the state-of-the-art language model
(GPT-4),andthreehardtasksinventedtochallengeit. Here,wereportadditionalexperimentswith
weakerLLMoreasiertasks,anddiscusscostandefficiency.
GSM8K StrategyQA GPT-4 GPT-3.5 GPT-4 GPT-3.5
IO 51 73 IO 7.3% 6% IO 6.19 4.47
CoT 86 82 CoT 4.0% 3% CoT 6.93 5.16
ToT 90 83 ToT 74% 19% ToT 7.56 6.62
Table4: Newtaskswith Table5: Gameof24with Table6: CreativeWritingwith
zero-shotToTandGPT-4. GPT-4vsGPT-3.5. GPT-4vs.GPT-3.5.
B.1 Extensiontonewtasks(GSM8k,StrategyQA)withzero-shotToT
WhilemorecommonNLPtasksmightbetooeasyforGPT-4anddonotrequireToT(whichiswhy
weconsideredhardernewtasks),webelieveapplyingToTtonewtaskscouldbestraightforward.
Forexample,weimplementedasimpleandgenericzero-shotToT-BFSsimilartocreativewriting
(sample5problemsolvingstrategiesthenvoteforthebestone;thensample5solutionsbasedonthe
beststrategythenvoteforthebestone)forGSM8KandStrategyQAwithfewextralinesofcode:
# define the answer format of new tasks
gsm8k_format = ‘"the answer is n" where n is a number’
strategyqa_format = ‘either "the answer is yes" or "the answer is no"’
# define zero-shot io prompting
standard_prompt = ‘Answer the following question with {format}: {input}’
# define thought format for zero-shot cot and zero-shot tot
cot_prompt = ‘‘‘Answer the following question: {input}
Make a strategy then write. Your output should be of the following format:
Strategy:
Your strategy about how to answer the question.
Answer:
Your answer to the question. It should end with {format}.
’’’
# define zero-shot voting used for zero-shot tot
vote_prompt = ‘‘‘Given an instruction and several choices,
decide which choice is most promising.
Analyze each choice in detail, then conclude in the last line
"The best choice is {s}", where s the integer id of the choice.
’’’
13

Weevaluatedonasubsetof100randomGSM8KtestandStrategyQAdevquestions. Asshown
inTable4andasexpected,ToTimprovesoverCoTonbothtasks(butonlyslightly,givenGPT-4
+CoTisalreadyverygoodonsuchtasks,andStrategyQA’sbottleneckisexternalknowledge,not
reasoning). Considering computational costs, it is more suitable to try smaller LLMs + ToT for
traditionalNLPtasks,orGPT-4+ToTforhardtasksthatchallengeGPT-4+CoT’sreasoning.
B.2 ExtensiontonewLMs(GPT-3.5)
TounderstandhowToTworkswithotherLLMs,wealsoranGPT-3.5-turboforCreativeWriting
(Table6)andGameof24(Table5). Onbothtasks,“ToT>CoT>IO”remainstrueforGPT-3.5. On
CreativeWriting,wefindGPT-3.5+ToToutperformGPT-4+IO,andsimilartoGPT-4+CoT,which
suggestsToTcouldalsoworkwellonweakerlanguagemodels.
OnGameof24(wechanged1-shotproposalpromptto3-shottomakeitwork),GPT-3.5+ToT’s
19% is far worse than GPT-4+ToT’s 74%. To further understand the importance of generation
vs. evaluation, we ran GPT-4 generation + GPT-3.5 evaluation (64%) and GPT-3.5 generation +
GPT-4evaluation(31%). Thissuggeststhegame’sbottleneckisthoughtgeneration,anddifferent
generation/evaluationlanguagemodelsmightattaindecentresultswhilereducingcosts.
B.3 Costandefficiency
RunningToTrequiressignificantlymorecomputationsthanIOorCoTprompting. Forexample,in
Gameof24(Table7below),solvingaproblemwithToTrequires5.5kcompletiontokens,closeto
100CoTtrials(6.7ktokens). ButtheperformanceofToTisbetterthanbestof100independentCoT
trials.
Gameof24 Generate/Prompttokens Costpercase Success
IO(bestof100) 1.8k/1.0k $0.13 33%
CoT(bestof100) 6.7k/2.2k $0.47 49%
ToT 5.5k/1.4k $0.74 74%
Table7: CostanalysisonGameof24.
OnCreativeWriting(Table8below),wefoundToTtakesaround5xcompletiontokensandmoney
cost,whichisintuitiveasb=5andmosttokensaregeneratedpassages.
CreativeWriting Generate/Prompttokens Costpercase
IO 0.9k/0.4k $0.06
CoT 0.9k/0.4k $0.07
ToT 4k/2.9k $0.32
Table8: CostanalysisonGameof24.
SocompletingGameof24andCreativeWriting’smainToTexperimentscostaround0.74×100+
0.32×100 = 106 dollars. Crosswords’ DFS experiments should be also within 100 dollars. In
general,costandefficiencyofToThighlydependonthepromptsandsearchalgorithmsused,and
couldrequire5-100timesmoregeneratedtokensthanCoT.Someactionableinsights:
• WerecommendusingToTontasksrequiringdeliberatereasoning,onwhichCoTstruggles.
• FlexibilityofToTallowssomeperformance-costtradeoff,e.g.,changebeamsizeorvote
number in BFS, few-shot vs. zero-shot prompting, GPT-3.5 vs. GPT-4, etc. One could
configurethesetupbasedonsomeresourceconstraintsorperformancegoal.
• Thereismuchspaceforimprovingefficiency,e.g.,BFScouldearlystopwhensolutionis
found,ortrimdownbeamsizetowhensomethoughtsare”impossible”.
• We believe that more computation is indeed required in order for the model to achieve
strongerintelligence,andthisshouldnotbecomeablockingissueasinthelongrun,(open-
source)LMswillbecomemuchcheaperandmoreefficient. Itisalsoagreatdirectionhow
tobettertrain/finetuneLMsforthoughtgenerationand/orevaluation.
14
