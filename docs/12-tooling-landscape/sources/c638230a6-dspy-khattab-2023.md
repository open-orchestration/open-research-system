Preprint
DSPY: COMPILING DECLARATIVE LANGUAGE
MODEL CALLS INTO SELF-IMPROVING PIPELINES
OmarKhattab,1ArnavSinghvi,2
ParidhiMaheshwari,4ZhiyuanZhang,1
KeshavSanthanam,1SriVardhamanan,6SaifulHaq,6
AshutoshSharma,6ThomasT.Joshi,7HannaMoazam,8
HeatherMiller,3,9MateiZaharia,2ChristopherPotts1
1StanfordUniversity,2UCBerkeley,3CarnegieMellonUniversity,
4AmazonAlexaAI,5DashworksTechnologies,Inc.,
6IITBombay,7CaleraCapital,8Microsoft,9TwoSigmaInvestments
okhattab@cs.stanford.edu
ABSTRACT
TheMLcommunityisrapidlyexploringtechniquesforpromptinglanguagemod-
els (LMs) and for stacking them into pipelines that solve complex tasks. Un-
fortunately, existing LM pipelines are typically implemented using hard-coded
“prompt templates”, i.e. lengthy strings discovered via trial and error. Toward a
moresystematicapproachfordevelopingandoptimizingLMpipelines,weintro-
duceDSPy,aprogrammingmodelthatabstractsLMpipelinesastexttransforma-
tiongraphs,i.e. imperativecomputationgraphswhereLMsareinvokedthrough
declarative modules. DSPy modules are parameterized, meaning they can learn
(bycreatingandcollectingdemonstrations)howtoapplycompositionsofprompt-
ing, finetuning, augmentation, and reasoning techniques. We design a compiler
that will optimize any DSPy pipeline to maximize a given metric. We conduct
twocasestudies,showingthatsuccinctDSPyprogramscanexpressandoptimize
sophisticated LM pipelines that reason about math word problems, tackle multi-
hopretrieval,answercomplexquestions,andcontrolagentloops. Withinminutes
ofcompiling,afewlinesofDSPyallowGPT-3.5andllama2-13b-chattoself-
bootstrap pipelines that outperform standard few-shot prompting (generally by
over 25% and 65%, respectively) and pipelines with expert-created demonstra-
tions (by up to 5–46% and 16–40%, respectively). On top of that, DSPy pro-
grams compiled to open and relatively small LMs like 770M-parameter T5 and
llama2-13b-chat are competitive with approaches that rely on expert-written
promptchainsforproprietaryGPT-3.5.
DSPyisavailableathttps://github.com/stanfordnlp/dspy.
1 INTRODUCTION
Languagemodels(LMs)areenablingresearcherstobuildNLPsystemsathigherlevelsofabstrac-
tionandwithlowerdatarequirementsthaneverbefore(Bommasanietal.,2021). Thisisfuelingan
explodingspaceof“prompting”techniques—andlightweightfinetuningtechniques—foradapting
LMstonewtasks(Kojimaetal.,2022),elicitingsystematicreasoningfromthem(Weietal.,2022;
Wangetal.,2022b),andaugmentingthemwithretrievedsources(Guuetal.,2020;Lazaridouetal.,
2022;Khattabetal.,2022)orwithtools(Yaoetal.,2022;Schicketal.,2023). Mostofthesetech-
niquesareexploredinisolation,butinteresthasbeengrowinginbuildingmulti-stagepipelinesand
agents that decompose complex tasks into more manageable calls to LMs in an effort to improve
performance (Qi et al., 2019; Khattab et al., 2021a; Karpas et al., 2022; Dohan et al., 2022; Khot
etal.,2022;Khattabetal.,2022;Chenetal.,2022;Pourreza&Rafiei,2023;Shinnetal.,2023).
Unfortunately, LMs are known to be sensitive to how they are prompted for each task, and this is
exacerbatedinpipelineswheremultipleLMcallshavetointeract effectively. Asaresult, theLM
1
3202
tcO
5
]LC.sc[
1v41730.0132:viXra

Preprint
callsinexistingLMpipelinesandinpopulardeveloperframeworksaregenerallyimplementedusing
hard-coded‘prompttemplates’,thatis,longstringsofinstructionsanddemonstrationsthatarehand
craftedthroughmanualtrialanderror. Wearguethatthisapproach,whilepervasive,canbebrittle
andunscalable—conceptuallyakintohand-tuningtheweightsforaclassifier.Agivenstringprompt
mightnotgeneralizetodifferentpipelinesoracrossdifferentLMs,datadomains,oreveninputs.
TowardamoresystematicapproachtodesigningAIpipelines,weintroducetheDSPyprogramming
model.1 DSPy pushes building new LM pipelines away from manipulating free-form strings and
closertoprogramming(composingmodularoperatorstobuildtexttransformationgraphs)wherea
compilerautomaticallygeneratesoptimizedLMinvocationstrategiesandpromptsfromaprogram.
Wedrawinspirationfromtheconsensusthatemergedaroundneuralnetworkabstractions(Bergstra
et al., 2013), where (1) many general-purpose layers can be modularly composed in any complex
architectureand(2)themodelweightscanbetrainedusingoptimizersinsteadofbeinghand-tuned.
To this end, we propose the DSPy programming model (Sec 3). We first translate string-based
promptingtechniques,includingcomplexandtask-dependentoneslikeChainofThought(Weietal.,
2022)andReAct(Yaoetal.,2022),intodeclarativemodulesthatcarrynatural-languagetypedsig-
natures.DSPymodulesaretask-adaptivecomponents—akintoneuralnetworklayers—thatabstract
anyparticulartexttransformation,likeansweringaquestionorsummarizingapaper. Wethenpa-
rameterizeeachmodulesothatitcanlearnitsdesiredbehaviorbyiterativelybootstrappinguseful
demonstrationswithinthepipeline. InspireddirectlybyPyTorchabstractions(Paszkeetal.,2019),
DSPymodulesareusedviaexpressivedefine-by-runcomputationalgraphs. Pipelinesareexpressed
by(1)declaringthemodulesneededand(2)usingthesemodulesinanylogicalcontrolflow(e.g.,
ifstatements,forloops,exceptions,etc.)tologicallyconnectthemodules.
WethendeveloptheDSPycompiler(Sec4),whichoptimizesanyDSPyprogramtoimprovequality
orcost.Thecompilerinputsaretheprogram,afewtraininginputswithoptionallabels,andavalida-
tionmetric. Thecompilersimulatesversionsoftheprogramontheinputsandbootstrapsexample
traces of each module for self-improvement, using them to construct effective few-shot prompts
or finetuning small LMs for steps of the pipeline. Optimization in DSPy is highly modular: it is
conductedbyteleprompters,2whicharegeneral-purposeoptimizationstrategiesthatdeterminehow
the modules should learn from data. In this way, the compiler automatically maps the declarative
modulestohigh-qualitycompositionsofprompting,finetuning,reasoning,andaugmentation.
ProgrammingmodelslikeDSPycouldbeassessedalongmanydimensions,butwefocusontherole
ofexpert-craftedpromptsinshapingsystemperformance. Weareseekingtoreduceorevenremove
theirrolethroughDSPymodules(e.g., versionsofpopulartechniqueslikeChainofThought)and
teleprompters.Wereportontwoexpansivecasestudies:mathwordproblems(GMS8K;Cobbeetal.
2021)andmulti-hopquestionanswering(HotPotQA;Yangetal.2018)withexplorationsofchain
ofthought,multi-chainreflection,multi-hopretrieval,retrieval-augmentedquestionanswering,and
agent loops. Our evaluations use a number of different compiling strategies effectively and show
that straightforward DSPy programs outperform systems using hand-crafted prompts, while also
allowingourprogramstousemuchsmallerandhencemoreefficientLMseffectively.
Overall,thisworkproposesthefirstprogrammingmodelthattranslatespromptingtechniquesinto
parameterized declarative modules and introduces an effective compiler with general optimiza-
tion strategies (teleprompters) to optimize arbitrary pipelines of these modules. Our main contri-
butions are empirical and algorithmic: with DSPy, we have found that we can implement very
short programs that can bootstrap self-improving multi-stage NLP systems using LMs as small as
llama2-13b-chat and T5-Large (770M parameters). Without hand-crafted prompts and within
minutes to tens of minutes of compiling, compositions of DSPy modules can raise the quality of
simple programs from 33% to 82% (Sec 6) and from 32% to 46% (Sec 7) for GPT-3.5 and, simi-
larly,from9%to47%(Sec6)andfrom22%to41%(Sec7)forllama2-13b-chat.
1DSPy is pronounced dee-ess-pie. It’s the second iteration of our earlier Demonstrate–Search–Predict
framework(DSP;Khattabetal.2022).ThispaperintroducesthekeyconceptsinDSPy.Formoreextensiveand
up-to-datedocumentationoftheframework,wereferreaderstohttps://github.com/stanfordnlp/dspy.
2Wederivethenametele-promptersfromthenotionofabstractingandautomatingthetaskofprompting,
inparticular,suchthatithappensatadistance,withoutmanualintervention.
2

Preprint
2 RELATED WORK
ThisworkisinspiredbytherolethatTorch(Collobertetal.,2002),Theano(Bergstraetal.,2010;
2011;Al-Rfouetal.,2016), Chainer(Tokuietal.,2015), andothersplayedinthedevelopmentin
deeplearningbyprovidingpowerfulabstractions.Asimilartransformationisemergingwithhigher-
levelpipelinesofLMs,andweareseekingtoofferasolidconceptualframeworkandprogramming
abstractionsforwhatwecallfoundationmodelprogramming. Wedrawondifferentiableprogram-
ming(Wangetal.,2018)butappliedtoLMcallsratherthanneuralnetworks,andborrowsyntactic
elementsfromPyTorch(Paszkeetal.,2019).
In-contextlearning(McCannetal.2018;Radfordetal.2018;Brownetal.2020)isakeymechanism
for foundation model programming. A growing body of work has revealed that, especially with
instruction tuning (Ouyang et al., 2022), we can elicit sophisticated behavior via prompting (Wei
etal.,2022;Wangetal.,2022b;Pressetal.,2022;Yaoetal.,2022;Khotetal.,2022;Madaanetal.,
2023). Similarly, forms of weak supervision that would normally require task-specific (Khattab
etal.,2021a;b)orhand-built(Ratneretal.,2016;Hancocketal.,2018)heuristicsarenowdoneby
LMs(Wangetal.,2022b;Zelikmanetal.,2022;Zhangetal.,2022;Shaoetal.,2023).
In-contextlearningmethodsnowroutinelyinvoketools, leadingtoLMpipelinesthatuseretrieval
models(Chenetal.,2017;Lewisetal.,2020;Guuetal.,2020;Lazaridouetal.,2022;Izacardetal.,
2022), multimodal foundation models, and more traditional tools like APIs (Nakano et al., 2021)
and calculators. A number of toolkits have been developed to facilitate this, including LangChain
(Chase, 2022), Semantic Kernel (Microsoft, 2023), LlamaIndex (Liu, 2022), and many other re-
trieval and agent libraries. These toolkits provide pre-packaged chains and agents that connect
LMswithnumerousaccessibletools. However,theysufferfromthepervasivepromptengineering
challenges we address in DSPy: they express task-specific behavior through hand-written prompt
templates(fordetaileddiscussion,seeAppendixB).
ResearchersarestartingtoapplydiscreteoptimizationandRLtofindeffectiveprompts, generally
forasinglelogicalLMcall(Guoetal.,2023;Pryzantetal.,2023;Huangetal.,2022;Yangetal.,
2023). DSPy seeks to generalize this space: it offers a rich framework for optimizing arbitrary
pipelinesfromhigh-leveldeclarativesignatures,bybootstrappinghigh-qualitymulti-stagedemon-
strations with constraints. In this framework, DSPy teleprompters may apply optimization using
model selection techniques like cross-validation or, in principle, with sophisticated techniques in-
volvingRLandLMfeedback(Huetal.,2023;Zhaoetal.,2023a;Shinnetal.,2023)orlearnedor
Bayesianhyperparameteroptimizationmethods(Bergstraetal.,2013;Akibaetal.,2019).
The present paper seeks to motivate DSPy as a programming model and to report new empirical
findings from applying the DSPy compiler. This is inspired by formative work by Bergstra et al.
(2010;2013),Paszkeetal.(2019),andWolfetal.(2020),whosupporttheirrespectiveprogramming
modelswithamixofbenchmarknumbersandsomequalitativemeasures. Forthecurrentpaper,we
focus on showing that DSPy and its compiler allow us to build outstanding LM systems without
hand-craftedpromptstrings,butinsteadfromtrulymodularunits,andthatthisopensupdoorsfor
systematicallyexploringarichdesignspaceataveryhighprogrammaticlevelofabstraction.
3 THE DSPY PROGRAMMING MODEL
WepresentDSPy,whichtreatsLMsasabstractdevicesfortextgeneration,3andoptimizestheirus-
ageinarbitrarycomputationalgraphs. DSPyprogramsareexpressedinPython:eachprogramtakes
thetaskinput(e.g., aquestiontoanswerorapapertosummarize)andreturnstheoutput(e.g., an
answerorasummary)afteraseriesofsteps. DSPycontributesthreeabstractionstowardautomatic
optimization: signatures,modules,andteleprompters. Signaturesabstracttheinput/outputbehavior
ofamodule;modulesreplaceexistinghand-promptingtechniquesandcanbecomposedinarbitrary
pipelines;andtelepromptersoptimizeallmodulesinthepipelinetomaximizeametric.
3WeassumeaccesstooneormoreLMs,whichconsumeapromptstringandreturntextcompletions.This
maybeapromptableLMcapableofin-contextlearning(e.g.,GPT-3.5orLlama2-7b)orasmallerfinetuneable
LM(e.g.,T5-base).AnLMmaybeselectedasthedefault;operationswilluseitunlessconfiguredotherwise.
3

Preprint
3.1 NATURALLANGUAGESIGNATURESCANABSTRACTPROMPTING&FINETUNING
Insteadoffree-formstringprompts,DSPyprogramsusenaturallanguagesignaturestoassignwork
totheLM.ADSPysignatureisnatural-languagetypeddeclarationofafunction:ashortdeclarative
spec that tells DSPy what a text transformation needs to do (e.g., “consume questions and return
answers”), rather than how a specific LM should be prompted to implement that behavior. More
formally,aDSPysignatureisatupleofinputfieldsandoutputfields(andanoptionalinstruction).
Afieldconsistsoffieldnameandoptionalmetadata.4 Intypicalusage,therolesoffieldsareinferred
byDSPyasafunctionoffieldnames. Forinstance,theDSPycompilerwillusein-contextlearning
tointerpretquestiondifferentlyfromanswerandwilliterativelyrefineitsusageofthesefields.
Signaturesoffertwobenefitsoverprompts: theycanbecompiledintoself-improvingandpipeline-
adaptivepromptsorfinetunes. Thisisprimarilydonebybootstrapping(Sec4)usefuldemonstrating
examples for each signature. Additionally, they handle structured formatting and parsing logic to
reduce(or,ideally,avoid)brittlestringmanipulationinuserprograms.
Inpractice,DSPysignaturescanbeexpressedwithashorthandnotationlikequestion -> answer,
sothatline1inthefollowingisacompleteDSPyprogramforabasicquestion-answeringsystem
(withline2illustratingusageandline3theresponsewhenGPT-3.5istheLM):
1qa = dspy.Predict("question -> answer")
2qa(question="Where is Guaran´ı spoken?")
3# Out: Prediction(answer=’Guaran´ı is spoken mainly in South America.’)
In the shorthand notation, each field’s name indicates the semantic role that the input (or output)
field plays in the transformation. DSPy will parse this notation and expand the field names into
meaningful instructions for the LM, so that english document -> french translation would
promptforEnglishtoFrenchtranslation. Whenneeded,DSPyoffersmoreadvancedprogramming
interfacesforexpressingmoreexplicitconstraintsonsignatures(AppendixA).
3.2 PARAMETERIZED&TEMPLATEDMODULESCANABSTRACTPROMPTINGTECHNIQUES
Akintotypesignaturesinprogramminglanguages,DSPysignaturessimplydefineaninterfaceand
providetype-likehintsontheexpectedbehavior. Touseasignature,wemustdeclareamodulewith
thatsignature,likeweinstantiatedaPredictmoduleabove. Amoduledeclarationlikethisreturns
afunctionhavingthatsignature.
ThePredictModule ThecoremoduleforworkingwithsignaturesinDSPyisPredict(simplified
pseudocodeinAppendixD.1). Internally,Predictstoresthesuppliedsignature,anoptionalLMto
use (initially None, but otherwise overrides the default LM for this module), and a list of demon-
strationsforprompting(initiallyempty). LikelayersinPyTorch,theinstantiatedmodulebehavesas
acallablefunction: ittakesinkeywordargumentscorrespondingtothesignatureinputfields(e.g.,
question), formats a prompt to implement the signature and includes the appropriate demonstra-
tions,callstheLM,andparsestheoutputfields. WhenPredictdetectsit’sbeingusedincompile
mode,itwillalsointernallytrackinput/outputtracestoassisttheteleprompteratbootstrappingthe
demonstrations.
OtherBuilt-inModules DSPymodulestranslatepromptingtechniquesintomodularfunctionsthat
supportanysignature,contrastingwiththestandardapproachofpromptingLMswithtask-specific
details(e.g.,hand-writtenfew-shotexamples).Tothisend,DSPyincludesanumberofmoresophis-
ticatedmoduleslikeChainOfThought,ProgramOfThought,MultiChainComparison,andReAct.5
ThesecanallbeusedinterchangeablytoimplementaDSPysignature. Forinstance,simplychang-
4Stringdescriptionsofthetaskandthefieldsarealsooptionalandusuallyomitted.Fieldscancarryoptional
fieldprefixanddescription. Bydefault,fieldsareassumedtoholdfree-formstrings;weareactivelyexploring
optionaldatatypeasawaytospecifyconstraintsonvalidvalues(e.g.,boolorint)andmoregracefullyhandle
formattingandparsinglogic,thoughthisfeatureisnotcoretoDSPyatthetimeofwriting.
5These modules generalize prompting techniques from the literature, respectively, by Wei et al. (2022),
Chenetal.(2022),Yoranetal.(2023),andYaoetal.(2022)and,indoingso,generalizetheideasonzero-shot
promptingandrationaleself-generationfromKojimaetal.(2022),Zelikmanetal.(2022),Zhangetal.(2022),
andHuangetal.(2022)toparameterizedmodulesthatcanbootstraparbitrarymulti-stagepipelines.
4

Preprint
| Predict |     | ChainOfThought |     |     |     |     |     |
| ------- | --- | -------------- | --- | --- | --- | --- | --- |
ing to in the above program leads to a system that thinks step by step
beforecommittingtoitsoutputfield.
Importantly, all of these modules are implemented in a few lines of code by expanding the user-
Predict
defined signature and calling one or more times on new signatures as appropriate. For
instance,weshowasimplifiedimplementationofthebuilt-inChainOfThoughtbelow.
1class ChainOfThought(dspy.Module):
| 2   | def __init__(self, | signature): |     |     |     |     |     |
| --- | ------------------ | ----------- | --- | --- | --- | --- | --- |
# Modify signature from ‘*inputs -> *outputs‘ to ‘*inputs -> rationale, *outputs‘.
3
4 rationale_field = dspy.OutputField(prefix="Reasoning: Let’s think step by step.")
|     | signature | = dspy.Signature(signature).prepend_output_field(rationale_field) |     |     |     |     |     |
| --- | --------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
5
6
| 7   | # Declare    | a sub-module              | with | the modified | signature. |     |     |
| --- | ------------ | ------------------------- | ---- | ------------ | ---------- | --- | --- |
|     | self.predict | = dspy.Predict(signature) |      |              |            |     |     |
8
9
|     | def forward(self, | **kwargs): |     |     |     |     |     |
| --- | ----------------- | ---------- | --- | --- | --- | --- | --- |
10
| 11  | # Just | forward the            | inputs | to the sub-module. |     |     |     |
| --- | ------ | ---------------------- | ------ | ------------------ | --- | --- | --- |
| 12  | return | self.predict(**kwargs) |        |                    |     |     |     |
Thisisafully-fledgedmodulecapableoflearningeffectivefew-shotpromptingforanyLMortask.
We contrast that with Appendix C, which copies long reasoning prompts hand-written by sources
rangingfromrecentresearchtopopularpromptinglibraries.
Parameterization Uniquely,DSPyparameterizesthesepromptingtechniques. Tounderstandthis
parameterization, observe that any LM call seeking to implement a particular signature needs to
specifyparametersthatinclude: (1)thespecificLMtocall(Chenetal.,2023), (2)thepromptin-
structions(Yangetal.,2023)andthestringprefixofeachsignaturefieldand,mostimportantly,(3)
thedemonstrationsusedasfew-shotprompts(forfrozenLMs)orastrainingdata(forfinetuning).
We focus primarily on automatically generating and selecting useful demonstrations. In our case
studies,wefindthatbootstrappinggooddemonstrationsgivesusapowerfulwaytoteachsophisti-
catedpipelinesofLMsnewbehaviorssystematically.
Tools DSPyprogramsmayusetools,whicharemodulesthatexecutecomputation. Wesupportre-
trievalmodelsthroughadspy.Retrievemodule. Atthetimeofwriting,DSPyhasbuilt-insupport
for ColBERTv2, Pyserini, and Pinecone retrievers, and we have explored experimental dspy.SQL
forexecutingSQLqueriesanddspy.PythonInterpreterforexecutingPythoncodeinasandbox.
Programs DSPymodulescanbecomposedinarbitrarypipelinesinadefine-by-runinterface. In-
spireddirectlybyPyTorchandChainer,onefirstdeclaresthemodulesneededatinitialization,allow-
ingDSPytokeeptrackofthemforoptimization,andthenoneexpressesthepipelinewitharbitrary
codethatcallsthemodulesinaforwardmethod.
|     |     |     |     |     | Asasimpleillustration, |     | weofferthefollowing |
| --- | --- | --- | --- | --- | ---------------------- | --- | ------------------- |
simplebutcompleteretrieval-augmentedgeneration(RAG)system.
1class RAG(dspy.Module):
| 2   | def __init__(self, | num_passages=3): |     |     |     |     |     |
| --- | ------------------ | ---------------- | --- | --- | --- | --- | --- |
3 # ‘Retrieve‘ will use the user’s default retrieval settings unless overriden.
|     | self.retrieve | = dspy.Retrieve(k=num_passages) |     |     |     |     |     |
| --- | ------------- | ------------------------------- | --- | --- | --- | --- | --- |
4
5 # ‘ChainOfThought‘ with signature that generates answers given retrieval & question.
|     | self.generate_answer |     | = dspy.ChainOfThought("context, |     |     | question | -> answer") |
| --- | -------------------- | --- | ------------------------------- | --- | --- | -------- | ----------- |
6
7
|     | def forward(self, | question): |     |     |     |     |     |
| --- | ----------------- | ---------- | --- | --- | --- | --- | --- |
8
|     | context | = self.retrieve(question).passages |     |     |     |     |     |
| --- | ------- | ---------------------------------- | --- | --- | --- | --- | --- |
9
| 10  | return | self.generate_answer(context=context, |     |     | question=question) |     |     |
| --- | ------ | ------------------------------------- | --- | --- | ------------------ | --- | --- |
To highlight modularity, we use ChainOfThought as a drop-in replacement of the basic Predict.
One can now simply write RAG()("Where is Guaran´ı spoken?") to use it. Notice that, if we
useasignature"context, question -> search query", wegetasystemthatgeneratessearch
queriesratherthananswers.
3.3 TELEPROMPTERSCANAUTOMATEPROMPTINGFORARBITRARYPIPELINES
WhencompilingaDSPyprogram, wegenerallyinvokeateleprompter, whichisanoptimizerthat
takes the program, a training set, and a metric—and returns a new optimized program. Different
teleprompters(Sec4)applydifferentstrategiesforoptimization.
5

Preprint
InDSPy,trainingsetsmaybesmall,potentiallyahandfulofexamples,thoughlargerdataenables
morepowerfuloptimization. Trainingexamplesmaybeincomplete,i.e.,onlyinputvaluesarenec-
essary. Labelsforthepipelinestepsarenotrequired,unlesstheyneedtobeusedinthemetric. In
practice,wetypicallyassumelabelsonlyfor(atmost)theprogram’sfinaloutput,nottheintermedi-
atesteps. Thislabel-efficiencyiscriticalformodularity: buildinganewpipelineinDSPyrequires
simplyrecompilingthenewpipeline’scode,notannotatingdataspecifictothenewpipeline.
Metricscanbesimplenotionslikeexactmatch(EM)orF1,buttheycanbeentireDSPyprograms
that balance multiple concerns. For example, we may compile the RAG module above against a
datasetofquestion–answerpairsqa trainsetandthemetricEM.Thegoalofoptimizationhereis
toeffectivelybootstrapfew-shotdemonstrations. Thefollowingcodeachievesthis:
1# Small training set with only questions and final answers.
2qa_trainset = [dspy.Example(question="What is the capital of France?", answer="Paris")]
3
4# The teleprompter will bootstrap missing labels: reasoning chains and retrieval contexts.
5teleprompter = dspy.BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
6compiled_rag = teleprompter.compile(RAG(), trainset=qa_trainset)
Inthisexample, theBootstrapFewShotteleprompter(Sec4, AppendixE.1)simulatesRAGonthe
trainingexample(s).Itwillcollectdemonstrationsofeachmodule(i.e.,examplesofitsinput–output
behavior)thatcollectivelyleadtovalidoutput(i.e.,respectingthesignaturesandthemetric).
Ifonewantedtopushthecompiledprogramtobeextractivegivenitsretrievedcontexts,onecould
defineacustommetrictouseinplaceofdspy.evaluate.answer exact match:
1def answer_and_context_match(example, pred, trace=None):
2 answer_match = dspy.evaluate.answer_exact_match(example, pred)
3
4 # Is the prediction a substring of some passage?
5 context_match = any((pred.answer.lower() in c) for c in pred.context)
6
7 return answer_match and context_match
Notice that behavior like this might be more accurately checked by another DSPy program that
checksforfaithfulgroundingofanswers.SuchmetricsarefullysupportedandencouragedinDSPy.
Teleprompterscanbecomposedbyspecifyingateacherprogram. DSPywillsampledemonstra-
tionsfromthisprogramforpromptoptimization. Thiscompositioncanenableveryrichpipelines,
where expensive programs (e.g., complex expensive ensembles using large LMs) supervise cheap
programs(e.g.,simplepipelinesusingsmallerLMs). Onemaystartwithcompiled ragfromabove
(say, compiled to use a large Llama2-13b-chat LM) but now fine-tune Flan-T5-large to create an
efficientprogram:
1# Larger set of questions with *no labels*. Labels for all steps will be bootstrapped.
2unlabeled_questions = [dspy.Example(question="What is the capital of Germany?"), ...]
3
4# As we assumes no answer, we use ‘answer_passage_match‘ to filter ungrounded answers.
5finetuning_teleprompter = BootstrapFinetune(metric=dspy.evaluate.answer_passage_match)
6
7# We set ‘teacher=compiled_rag‘ to compose. Bootstrapping will now use ‘compiled_rag‘.
8compiled_rag_via_finetune = finetuning_teleprompter.compile(RAG(), teacher=compiled_rag,
trainset=unlabeled_questions, target=’google/flan-t5-large’)
4 THE DSPY COMPILER
AkeysourceofDSPy’sexpressivepowerisitsabilitytocompile—orautomaticallyoptimize—any
programinthisprogrammingmodel. Compilingreliesonateleprompter,whichisanoptimizerfor
DSPyprogramsthatimprovesthequality(orcost)ofmodulesviapromptingorfinetuning, which
are unified in DSPy. While DSPy does not enforce this when creating new teleprompters, typical
telepromptersgothroughthreestages.
Stage1:CandidateGeneration Thecompilerfirst(recursively)findsalluniquePredictmodules
(predictors) in a program, including those nested under other modules. For each unique predictor
p, the teleprompter may generate candidate values for the parameters of p: the instructions, field
descriptions,or—mostimportantly—demonstrations(i.e.,exampleinput–outputpairs). Inthisiter-
6

Preprint
ationofDSPy,wefocusondemonstrationsandfindthatsimplerejection-sampling-likeapproaches
canhelpbootstraphighlyeffectivemulti-stagesystems.
Considerthesimplestnon-trivialteleprompterinDSPy,BootstrapFewShot(simplifiedpseudocode
in Appendix E.1). This teleprompter will simulate a teacher program (or, if unset, the zero-shot
version of the program being compiled) on some training inputs, possibly one or more times with
a high temperature. When running in compile mode, multi-stage traces are tracked transparently
andinathread-safefashionthroughoutexecution. Theprogram’smetricisusedtofilterformulti-
stage traces that together help the pipeline pass the metric. We thus obtain potential labels for all
signatures in the program by throwing away the bad examples and using the good examples as
potentialdemonstrations,thoughthesedesigndecisionsareunderusercontrol.
While LMs can be highly unreliable, we find they can be rather efficient at searching the space
ofsolutionsformulti-stagedesigns. Awell-decomposedprogramcantypicallyfindatleastafew
training examples where the LM can pass the constraints enforced by the signatures and metrics,
allowingustobootstrapiterativelyifneeded.
Stage2: ParameterOptimization Noweachparameterhasadiscretesetofcandidates: demon-
strations, instructions, etc. Many hyperparameter tuning algorithms (e.g., random search or Tree-
structuredParzenEstimatorsasinHyperOpt(Bergstraetal.,2013)andOptuna(Akibaetal.,2019))
can be applied for selection among candidates. We report simplified implementations of DSPy’s
BootstrapFewShotWithRandomSearchandBootstrapFewShotWithOptunainAppendixE.2and
AppendixE.3.
AnothertypeofoptimizationisfinetuningwithBootstrapFinetune,wherethedemonstrationsare
usedtoupdatetheLM’sweightsforeachpredictor. Whenthisisapplied,theLMparameterofeach
moduleisupdatedtothenewLMweights. Typically,weareoptimizingaveragequalityusingthe
metricwithcross-validationoverthetrainingsetoravalidationset. Thisisapplicableevenwithno
labelsforanystages,dependingonthenatureofmetric.
Stage 3: Higher-Order Program Optimization A different type of optimization that the DSPy
compiler supports is modifying the control flow of the program. One of the simplest forms of
these is ensembles, which we use in the case studies in this work. An ensemble will bootstrap
multiplecopiesofthesameprogram,andthenreplacetheprogramwithanewonethatrunsthem
allinparallelandreducestheirpredictionsintoonewithacustomfunction(e.g.,majorityvoting).
In future work, this stage can easily accommodate techniques for more dynamic (i.e., test-time)
bootstrappingaswellasautomaticbacktracking-likelogic.
5 GOALS OF EVALUATION
Programmingframeworkscanbeevaluatedalongmanydimensions: computationalefficiency, de-
veloperefficiency, intuitivenessofthecodeandconcepts, andsoforth. Inthispaper, wefocuson
perhaps the most pressing issue for current LM pipelines: the role of hand-written, task-specific
promptsinachievingperformantsystems. Ourevaluationsseektotestthefollowinghypotheses:
H1 With DSPy, we can replace hand-crafted prompt strings with concise and well-defined
modules,withoutreducingqualityorexpressivepower.
H2 Parameterizing the modules and treating prompting as an optimization problem makes
DSPybetteratadaptingtodifferentLMs,anditmayoutperformexpert-writtenprompts.
H3 Theresultingmodularitymakesitpossibletomorethoroughlyexplorecomplexpipelines
thathaveusefulperformancecharacteristicsorthatfitnuancedmetrics.
Ourevaluationwillexplorethesehypothesesusingdiversetask–programpairs. Wehopethisbegins
ashiftfromunderspecifiedquestionslike“howdodifferentLMscompareonGSM8K”toward“how
theycompareonGSM8KwithprogramPwhencompiledwithstrategyS”,whichisawell-defined
and reproducible run. Ultimately, our goal is to reduce the role of artful prompt construction in
modernAIinfavorofthedevelopmentofnewmodular,composableprogramsandoptimizers.
7

Preprint
Table 1: Results with in-context learning on GSM8K math word problems. Each row represents
a separate pipeline: the module in the Program column is compiled against the examples in the
Trainingset. Theprograms,compilers,and(small)trainingsetsaredefinedinSection6. Rowswith
ensemblebuildontheimmediatelyprecedingrow.
Notably,allprogramsinthistableareexpressed
bycomposingtwotofourDSPymodulesandteleprompters.Compilingthecorrectmodules,instead
ofstringprompts,improvesdifferentLMsfrom4–20%accuracyto49–88%accuracy.
|     |      |             |             |          |           |      | GPT-3.5 Llama2-13b-chat |      |
| --- | ---- | ----------- | ----------- | -------- | --------- | ---- | ----------------------- | ---- |
|     |      | Program     | Compilation |          | Training  | Dev  | Test Dev                | Test |
|     |      |             | none        |          | n/a       | 24.0 | 25.2 7.0                | 9.4  |
|     |      |             | fewshot     |          | trainset  | 33.1 | – 4.3                   | –    |
|     |      | vanilla     | bootstrap   |          | trainset  | 44.0 | – 28.0                  | –    |
|     |      |             | bootstrap×2 |          | trainset  | 64.7 | 61.7 37.3               | 36.5 |
|     |      |             | +ensemble   |          | trainset  |      |                         |      |
|     |      |             |             |          |           | 62.7 | 61.9 39.0               | 34.6 |
|     |      |             | none        |          | n/a       | 50.0 | – 26.7                  | –    |
|     |      |             | fewshot     |          | trainset  | 63.0 | – 27.3                  | –    |
|     |      | CoT         | fewshot     |          | +humanCoT | 78.6 | 72.4 34.3               | 33.7 |
|     |      |             | bootstrap   |          | trainset  |      |                         |      |
|     |      |             |             |          |           | 80.3 | 72.9 43.3               | –    |
|     |      |             | +ensemble   |          | trainset  | 88.3 | 81.6 43.7               | –    |
|     |      |             | none        |          | n/a       | 65.0 | – 36.7                  | –    |
|     |      |             | fewshot     |          | trainset  |      |                         |      |
|     |      | reflection  |             |          |           | 71.7 | – 36.3                  | –    |
|     |      |             | bootstrap   |          | trainset  |      |                         |      |
|     |      |             |             |          |           | 83.0 | 76.0 44.3               | 40.2 |
|     |      |             | +ensemble   |          | trainset  | 86.7 | – 49.0                  | 46.9 |
| 6   | CASE | STUDY: MATH | WORD        | PROBLEMS |           |      |                         |      |
WeevaluateonthepopularGSM8Kdatasetwithgradeschoolmathquestions(Cobbeetal.,2021).
Wesample200and300question–answerpairsfromtheofficialtrainingsetfortraininganddevelop-
ment,respectively. Ourfinalevaluationsusethe1.3kofficialtestsetexamples. Wereportextensive
comparisonsonthedevelopmentsettoavoidoverfittingontest. FollowingpriorworkonGSM8K,
weevaluatetheaccuracyofthefinalnumericalvaluethatappearsintheLMoutput.
Programs Considered For this task, we consider three simple DSPy programs: a one-step Pre-
dictmodule(vanilla),atwo-stepChainOfThoughtmodule(CoT),andfinallyamulti-stageCom-
parerOfThoughtsmodule(ThoughtReflection). Thesearefullydefinedbythefollowingcode:
| 1vanilla | = dspy.Predict("question |     | -> answer") |     | # GSM8K | Program | ‘vanilla‘ |     |
| -------- | ------------------------ | --- | ----------- | --- | ------- | ------- | --------- | --- |
2
| 3CoT | = dspy.ChainOfThought("question |     | ->  | answer") | # GSM8K | Program | ‘CoT‘ |     |
| ---- | ------------------------------- | --- | --- | -------- | ------- | ------- | ----- | --- |
1class ThoughtReflection(dspy.Module):
| 2   | def __init__(self, | num_attempts):                  |     |     |     |          |                 |     |
| --- | ------------------ | ------------------------------- | --- | --- | --- | -------- | --------------- | --- |
|     | self.predict       | = dspy.ChainOfThought("question |     |     | ->  | answer", | n=num_attempts) |     |
3
| 4   | self.compare | = dspy.MultiChainComparison(’question |     |     |     | ->  | answer’, M=num_attempts) |     |
| --- | ------------ | ------------------------------------- | --- | --- | --- | --- | ------------------------ | --- |
5
| 6   | def forward(self, | question):                                    |     |     |                          |     |     |     |
| --- | ----------------- | --------------------------------------------- | --- | --- | ------------------------ | --- | --- | --- |
| 7   | completions       | = self.predict(question=question).completions |     |     |                          |     |     |     |
|     | return            | self.compare(question=question,               |     |     | completions=completions) |     |     |     |
8
9
| 10reflection | =   | ThoughtReflection(num_attempts=5) |     |     | # GSM8K | Program | ‘reflection‘ |     |
| ------------ | --- | --------------------------------- | --- | --- | ------- | ------- | ------------ | --- |
Inreflection,fivereasoningchainsaresampledfromtheLM(alongsidetheiranswers)andthey
MultiChainComparison
are compared in parallel by a built-in module, which generalizes Yoran
etal.(2023). Thisgeneratesanewanswertakingintoaccountthepatternsfromthefiveattempts.
Critically,themodulesusedareallgeneric,noneisspecificmathproblemsorparticularLM.
Compiling As we discussed in Section 4, DSPy programs can be compiled into new, optimized
programs. In our experiments, we evaluate the programs zero-shot (no compiling) as well as a
| numberofstrategiesforcompiling. |     |                                           | OursimplestcompilerisLabeledFewShot: |     |     |                    |     |     |
| ------------------------------- | --- | ----------------------------------------- | ------------------------------------ | --- | --- | ------------------ | --- | --- |
| 1fewshot                        | =   | dspy.LabeledFewShot(k=8).compile(program, |                                      |     |     | trainset=trainset) |     |     |
Here,programcanbeanyDSPymodule.Thissimplysamplesk=8randomdemonstrationsfromthe
trainsetforthefieldscommontothetrainingexamplesandthesignature(s),inthiscase,question
andanswer,butnotthereasoningforinstance. Wereporttheaverageof3–5runs(dependingonthe
setting)whenapplyingsuchrandomsampling.
8

Preprint
Next,wealsoconsiderbootstrappingfew-shotexampleswithrandomsearch:
1tp = BootstrapFewShotWithRandomSearch(metric=gsm8k_accuracy)
2bootstrap = tp.compile(program, trainset=trainset, valset=devset)
Thiswillgeneratedemonstrationchainsforexamplesinthetrainingsetandoptimizetheselection
ofdemonstrations(fromthisset)toself-improvetheprogram’smodules.Asthenameindicates,this
isdonewithrandomsearch,treatingtheselectionofdemonstrationsasaparametertooptimize.
Next, if desired, this bootstrapping process can be nested in DSPy. In particular, we can use the
optimized bootstrap program itself to further bootstrap another program. This is relevant, for
example,whenevertheoriginalzero-shotprogramperformsrelativelypoorly.
1bootstrap2 = tp.compile(program, teacher=bootstrap, trainset=trainset, valset=devset)
Andlastly,weconsiderensemblingthesebootstraps:
1# A program that ensembles the top-7 candidate programs from a bootstrapping compiler run
(in particular ‘bootstrap‘ or, when applicable, ‘bootstrap2‘) with majority voting.
2ensemble = Ensemble(reduce_fn=dspy.majority).compile(bootstrap.programs[:7])
GSM8K includes human reasoning chains. Above, trainset does not include these reasoning
chains. Wealsoevaluatewithtrainset human CoT,whichextendstheexamplesintrainsetwith
the human reasoning string. These two datasets can be used interchangeably as the value for the
trainset parameter above. We note here that compiling generally runs on the order of minutes
(or tens of minutes) as even the more expensive settings only require running the program a few
thousandtimes(e.g.,10–20trialsover150–300validationexamples)andtheycanoccurinparallel.
Results OurresultsaresummarizedinTable1,whichincludesdevresultsaswellasourevaluation
of promising representatives of each approach on the test set. First, the vanilla program results
show that GPT-3.5 and llama2-13b-chat struggle with math word problems when they have to
predicttheanswersdirectly,thatis,withoutusingareasoningchainfirst. Thisismostpronounced
in the absence of good demonstrations, which can be seen in the none compilation setting (i.e.,
zero-shot instruction) and the fewshot setting (i.e., sampling random question–answer pairs). In-
terestingly,however,vanillaishelpedsubstantiallybycompilingwithbootstrapandbyiterating
thisprocessintobootstrap×2. Oninspectingthepromptsbootstrapped(AppendixF),weseethat
thepromptallowstheLMtoleveragetheanswerfieldforreasoningfirst,whichispermittedasthe
metricextractsthefinalnumericalvalueforevaluation.
Next,weconsidertheCoTprogram.Whiletheexperthumanreasoningchains(+human CoT)provide
a large boost when available, we can match or surpass this using bootstrap, substantiating our
hypothesis that DSPy can cut the need for hand-crafted prompts. Beyond this, we see that the
reflectionprogram,whileonlyafewlineslongerthantheothers,isaclearwinner,thoughCoTis
quiteeffectivewithensemble. Overall,thebootstrapcompilationprocedureleadstolargegains
foreveryprogram,acrossbothLMs. Indeed,allprogramsinthistableareexpressedbycomposing
two to four DSPy modules and teleprompters, and they reveal overall that—in the new paradigm
prescribed by DSPy—it’s composing the right generic modules, rather than manipulating string
prompts,thatimprovesdifferentLMsfrom4–20%accuracyto49–88%accuracy.
We can informally compare with the following. Zhang et al. (2022) reports 48% for
text-davinci-002, which aligns closely with our llama2-13b-chat results, and reports 59.4%
with codex when employing a manual CoT approach and 62.8% with an automatic CoT method.
Wang et al. (2022b) report 57% for CoT prompting with PaLM 540-B, which becomes 74% upon
addingself-consistency.TheLlama2authors(Touvronetal.,2023)presents28.7%forllama2-13b,
42.2%forllama2-34b,and56.8%forllama2-70b. Intriguingly,ourprogramwiththe13bvariant
ofthemodeliscompetitivewiththeir34b-basedresultseventhoughwedon’tusehumanreasoning
chainsinourprogram. Zhaoetal.(2023b)reports80.8%forCoTwithgpt-3.5-turbofromApril
2023. The GPT-4 authors (OpenAI, 2023) reports that GPT-3.5 scores 57.1% and GPT-4 elevates
thisto92%buttheynotethatGPT-4wasinfactpre-trainedonasubsetofGSM8K’strainingset.
9

Preprint
| 7   | CASE | STUDY: | COMPLEX | QUESTION |     | ANSWERING |     |     |
| --- | ---- | ------ | ------- | -------- | --- | --------- | --- | --- |
Inthiscasestudy,weexplorethemulti-hopquestionansweringtaskwiththeHotPotQA(Yangetal.,
2018)datasetintheopen-domain“fullwiki”setting. Forretrieval,weuseasearchindexoftheof-
ficialWikipedia2017“abstracts”dumpofHotPotQA.SearchisconductedbyaColBERTv2(San-
thanametal.,2021)retriever. TheHotPotQAtestsetishidden,sowereservetheofficialvalidation
setforourtesting,andsample1000examplesforthat. Wesub-dividethetrainingsetinto70%/30%
train/validationsplits. Inthetraining(andthusvalidation)split,wekeeponlyexamplesmarkedas
“hard”intheoriginaldataset,whichmatchesthedesignationoftheofficialvalidationandtestsets.
Fortrainingandforreportingdevelopmentresults,wesample200and300examplesrespectively.
Programs Considered Our simplest baseline is the vanilla program used in the previous case
study on GSM8K (Sec 6); the "question -> answer" signature is universal enough that it will
workforthistask(andmanyothers)whencompiledappropriately.
Our baseline RAG program is the one given in Section 3.2 as a simple example of RAG with a
dspy.ChainOfThoughtlayer.
WewillseethatthisprogramdoesnotexcelatHotPotQA,andthis
motivatesustoevaluatetwomulti-hopprograms.
Tothatend, wefirsttestReAct(Yaoetal.,2022), amulti-stepagentfortooluse, whichisimple-
mentedasabuilt-inmoduleinDSPy.Inthesimplestcase,aReActmoduleforaparticularsignature
canbedeclaredasfollowsinDSPy:
1react = dspy.ReAct("question -> answer", tools=[dspy.Retrieve(k=1)], max_iters=5)
Wealsotestthefollowingcustomprogram,whichsimulatestheinformationflowinBaleen(Khattab
etal.,2021a)andIRRR(Qietal.,2020)andhassimilaritiestoIRCoT(Trivedietal.,2022).
1class BasicMultiHop(dspy.Module):
| 2   | def __init__(self,  |     | passages_per_hop):                  |                                 |     |          |                   |     |
| --- | ------------------- | --- | ----------------------------------- | ------------------------------- | --- | -------- | ----------------- | --- |
| 3   | self.retrieve       |     | = dspy.Retrieve(k=passages_per_hop) |                                 |     |          |                   |     |
|     | self.generate_query |     |                                     | = dspy.ChainOfThought("context, |     | question | -> search_query") |     |
4
| 5   | self.generate_answer |     |     | = dspy.ChainOfThought("context, |     | question | -> answer") |     |
| --- | -------------------- | --- | --- | ------------------------------- | --- | -------- | ----------- | --- |
6
| 7   | def forward(self, |      | question): |     |     |     |     |     |
| --- | ----------------- | ---- | ---------- | --- | --- | --- | --- | --- |
| 8   | context           | = [] |            |     |     |     |     |     |
9
| 10  | for | hop in  | range(2):                            |     |     |                                 |     |     |
| --- | --- | ------- | ------------------------------------ | --- | --- | ------------------------------- | --- | --- |
| 11  |     | query = | self.generate_query(context=context, |     |     | question=question).search_query |     |     |
| 12  |     | context | += self.retrieve(query).passages     |     |     |                                 |     |     |
13
|     | return | self.generate_answer(context=context, |     |     |     | question=question) |     |     |
| --- | ------ | ------------------------------------- | --- | --- | --- | ------------------ | --- | --- |
14
15
| 16multihop |     | = BasicMultiHop(passages_per_hop=3) |     |     |     |     |     |     |
| ---------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Compiling Forcompilers, wecontinuetousetheonesthatweusedforGSM8K(seeSec6). We
also consider two compositions of our teleprompters. For ReAct, we consider bootstrapping with
BootstrapFewShotWithRandomSearch starting from an earlier bootstrap of the ReAct program.
|     |     | multihop |     |     |     |     | T5-Large |     |
| --- | --- | -------- | --- | --- | --- | --- | -------- | --- |
For the simple program, we also consider fine-tuning with starting from the
earlierbootstrapofthatprogram.
1multihop_t5 = dspy.BootstrapFinetune(metric=answer_exact_match).compile(program,
|     | teacher=bootstrap, |     |     | trainset=trainset, |     | target=’t5-large’) |     |     |
| --- | ------------------ | --- | --- | ------------------ | --- | ------------------ | --- | --- |
Results Table2summarizesourresults. Comparedwiththevanillafew-shotprompting,achain-
of-thought and retrieval-augmented generation (CoT RAG) program can self-bootstrap in DSPy to
increaseanswerEMsubstantially. However,thisreliesentirelyontheColBERTv2retrievertofind
relevantpassagesdirectlyfromtheoriginalquestions,limitingitspassagerecall. Thisistackledin
thereactandmultihopprograms,whichwillgeneratequeriesfortheretrieverinmultipleiterative
“hops”. Indeed,overall,asimplemultihopprogramperformsthebest,andingeneralbootstrap
againprovestobeveryeffectiveatraisingitsqualityrelativetoitsfewshotvariantforbothLMs.
|     |             |     |         | bootstrap |         | bootstrap×2) |                | fewshot |
| --- | ----------- | --- | ------- | --------- | ------- | ------------ | -------------- | ------- |
| In  | particular, | we  | can see | that      | (and/or |              | can outperform | both    |
prompting(formultihop)andexperthumanreasoning(forreact;adaptedslightlyfromYaoetal.
(2022)toourretrievalsetting). Perhapsmostimportantly,wecanmakellama2-13b-chatcompet-
itivewithGPT-3.5bysimplycompilingourprograms.
|     |     |     |     |     |     |     | multihop | t5  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
To assess the finetuning capacity of DSPy, we also evaluated the compiler defined
T5-Large
above which produces a (770M parameter) model. This program scores 39.3% answer
EM and 46.0% passage accuracy on the dev set, using only 200 labeled inputs and 800 unlabeled
10

Preprint
Table2: Resultswithin-contextlearningonHotPotQAmulti-hopretrievalquestionanswering. We
reportanswerexactmatch(Ans)andpair-retrievalaccuracy(Psg). Eachrowrepresentsaseparate
pipeline: themoduleintheProgramcolumniscompiledagainsttheexamplesintheTrainingset.
Theprograms,compilers,and(small)trainingsetsaredefinedinthemaintext. ForHotPotQA,we
usethetrainingset(andnotdev)directlyforcross-validation. ∗Themarkedresultisevaluatedon
50%ofourtestsetduetocost.
|         |           |           | GPT-3.5 |      | Llama2-13b-chat |      |      |
| ------- | --------- | --------- | ------- | ---- | --------------- | ---- | ---- |
| Program | Compiler  | Dev       |         | Test | Dev             |      | Test |
|         |           | Ans Psg   | Ans     | Psg  | Ans Psg         | Ans  | Psg  |
| vanilla | fewshot   | 34.3 n/a  | 31.5    | n/a  | 27.5 n/a        | 21.8 | n/a  |
| CoT RAG | fewshot   | 36.4 36.0 | 29.8    | 34.4 | 34.5 36.0       | 28.0 | 34.4 |
|         | bootstrap | 42.3 36.0 | –       | –    | 38.3 36.0       | 32.9 | 34.4 |
|         | none      | 20.3 –    | –       | –    | 20.0            | – –  | –    |
|         | +human r  | 33.0 –    | –       | –    | 28.3            | – –  | –    |
react
|          | bootstrap   | 31.0 –    | –     | –    | 24.7      | – –    | –    |
| -------- | ----------- | --------- | ----- | ---- | --------- | ------ | ---- |
|          | bootstrap×2 | 39.0 –    | –     | –    | 40.0      | – –    | –    |
|          | fewshot     | 36.9 38.3 | 31.2  | 40.8 | 34.7 32.0 | 31.3   | 30.8 |
| multihop | bootstrap   | 48.7 47.0 | 39.6  | 43.8 | 42.0 48.3 | 36.4   | 43.5 |
|          | ensemble    | 54.7 –    | 45.6∗ | –    | 50.0      | – 41.0 | –    |
questions. For compiling, we use a teacher program consisting of an ensemble (union) of two
multihopwithllama2-13b-chat. Consideringitsextremelysmallsizeandlocalavailability,this
compiledprogramwithT5-Largewouldimposeordersofmagnitudelowercostsforinferencethan
aproprietaryLMlikeGPT-3.5.
OurresultsmaybepeggedagainsttheevaluationonHotPotQAinanumberofrecentpapers,though
there is significant variation in evaluation methodology and test set samples across studies in this
space. UsingCoTprompting,Sietal.(2022)achieve25.2%EM.Witha“recite-and-answer”tech-
niquethatusesPaLM-62B(Chowdheryetal.,2022)toreciteevidencepassages, Sunetal.(2022)
achieve 26.5% EM. Wang et al. (2022a) achieve 33.8% EM and 44.6% F1 when applying self-
consistency for PaLM-540B. Yao et al. (2022) achieve 27.4% EM using ReAct with PaLM-540B
and 30.8 with text-davinci-002, with a tool giving it the ability for search using a Wikipedia
API. They push their PaLM results to 35.1% EM by applying an additional CoT step with self-
whichmayresembleourensembleapproachinthesenseofaggregatingmultiplean-
consistency,
swers. Trivedietal.(2022)reports49%usingapipelinewithcode-davinci-002LMonasample
of500HotPotQAquestions.
8 CONCLUSION
ThispaperintroducedDSPy, anewprogrammingmodelfordesigningAIsystemsusingpipelines
ofpretrainedLMsandothertools. Wepresentedthreenewconceptsintroducedinthisabstraction
(DSPysignatures,modules,andteleprompters),andshowedintwoverydifferentcasestudiesthat
it supports rapid development of highly effective systems that use relatively small LMs. We have
maintainedopen-sourceversionsofthisframeworkforclosetoayear. Inthisperiod,wehaveseen
andcreatedalargenumberofprogramsthatwerecompiledtohigh-qualitysystemsbyDSPy,span-
ningtasksfrominformationextractiontolow-resourcesyntheticdatageneration. Intheinterestof
spaceandtomaintainreasonablescopeinthispaper, weleavereportingonsuchtasksundercon-
trolledexperimentalconditionstofuturework. Whilein-contextlearninghasprovedtransformative
over the past 2–3 years of LM research, we argue that the true expressive power in this emerging
paradigmisinbuildingsophisticatedtexttransformationgraphsinwhichcomposablemodulesand
optimizers(teleprompters)cometogethertoleverageLMsinmoresystematicandreliableways.
ACKNOWLEDGMENTS
WethankJoshPurtellforsuggestingtheaptname“texttransformationgraph”forthecomputational
graph abstraction of DSPy. We thank Rick Battle, Igor Kotenkov, Lisa Li, David Hall, Ashwin
Paranjape, Chris Manning, Percy Liang, and many researchers, developers, and users for valuable
11

Preprint
discussionsandfeedback. WethankGiuseppeAttanasioforhispublicLATEXGitHub-stylePython
codeformattinggist.6
This work was partially supported by IBM as a founding member of the Stanford Institute for
Human-Centered Artificial Intelligence (HAI), Oracle, Virtusa, and Cigna Healthcare. It was also
partiallysupportedbyanHAIAzurecomputegrant. Thisresearchwassupportedinpartbyaffiliate
membersandothersupportersoftheStanfordDAWNproject–Facebook,Google,andVMware—as
wellastheNSFunderCAREERgrantCNS-1651570. Anyopinions, findings, andconclusionsor
recommendationsexpressedinthismaterial arethoseoftheauthorsanddonot necessarilyreflect
theviewsoftheNationalScienceFoundation. OmarKhattabissupportedbytheAppleScholarsin
AI/MLfellowship.
\usepackage[pdftex]{graphicx} ...
\includegraphics[width=0.8\linewidth]{myfile.pdf}
REFERENCES
Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama. Optuna:
A next-generation hyperparameter optimization framework. In Proceedings of the 25th ACM
SIGKDDinternationalconferenceonknowledgediscovery&datamining,pp.2623–2631,2019.
Rami Al-Rfou, Guillaume Alain, Amjad Almahairi, Christof Angermueller, Dzmitry Bahdanau,
Nicolas Ballas, Fre´de´ric Bastien, Justin Bayer, Anatoly Belikov, Alexander Belopolsky, et al.
Theano: APythonframeworkforfastcomputationofmathematicalexpressions. arXive-prints,
pp.arXiv–1605,2016.
James Bergstra, Olivier Breuleux, Fre´de´ric Bastien, Pascal Lamblin, Razvan Pascanu, Guillaume
Desjardins,JosephTurian,DavidWarde-Farley,andYoshuaBengio. Theano: ACPUandGPU
mathcompilerinPython. InProc.9thpythoninscienceconf,volume1,pp.3–10,2010.
James Bergstra, Fre´de´ric Bastien, Olivier Breuleux, Pascal Lamblin, Razvan Pascanu, Olivier De-
lalleau, Guillaume Desjardins, David Warde-Farley, Ian Goodfellow, Arnaud Bergeron, et al.
Theano: Deep learning on gpus with Python. In NIPS 2011, BigLearning Workshop, Granada,
Spain,volume3.Citeseer,2011.
JamesBergstra,DanielYamins,andDavidCox.Makingascienceofmodelsearch:Hyperparameter
optimizationinhundredsofdimensionsforvisionarchitectures. InInternationalconferenceon
machinelearning,pp.115–123.PMLR,2013.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx,
MichaelSBernstein,JeannetteBohg,AntoineBosselut,EmmaBrunskill,etal. Ontheopportu-
nitiesandrisksoffoundationmodels. arXivpreprintarXiv:2108.07258,2021.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
ArvindNeelakantan,PranavShyam,GirishSastry,AmandaAskell,etal. Languagemodelsare
few-shotlearners. Advancesinneuralinformationprocessingsystems,33:1877–1901,2020.
Harrison Chase. Hwchase17/langchain. 2022. URL https://github.com/hwchase17/
langchain.
Danqi Chen, Adam Fisch, Jason Weston, and Antoine Bordes. Reading Wikipedia to answer
open-domain questions. In Proceedings of the 55th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pp. 1870–1879, Vancouver, Canada, July
2017. Association for Computational Linguistics. doi: 10.18653/v1/P17-1171. URL https:
//aclanthology.org/P17-1171.
LingjiaoChen,MateiZaharia,andJamesZou. Frugalgpt: Howtouselargelanguagemodelswhile
reducingcostandimprovingperformance. arXivpreprintarXiv:2305.05176,2023.
6https://gist.github.com/g8a9/07c2be12ae02cfad4aa430d77dc940cb
12

Preprint
Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W Cohen. Program of thoughts prompt-
ing: Disentangling computation from reasoning for numerical reasoning tasks. arXiv preprint
arXiv:2211.12588,2022.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm:
Scalinglanguagemodelingwithpathways. arXivpreprintarXiv:2204.02311,2022.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to
solvemathwordproblems. arXivpreprintarXiv:2110.14168,2021.
RonanCollobert,SamyBengio,andJohnnyMarie´thoz.Torch:amodularmachinelearningsoftware
library. Technicalreport,Idiap,2002.
DavidDohan,WinnieXu,AitorLewkowycz,JacobAustin,DavidBieber,RaphaelGontijoLopes,
YuhuaiWu,HenrykMichalewski,RifASaurous,JaschaSohl-Dickstein,etal. Languagemodel
cascades. arXivpreprintarXiv:2207.10342,2022.
Luyu Gao, Zhuyun Dai, Panupong Pasupat, Anthony Chen, Arun Tejasvi Chaganty, Yicheng Fan,
VincentZhao,NiLao,HongraeLee,Da-ChengJuan,etal. Rarr: Researchingandrevisingwhat
languagemodelssay,usinglanguagemodels. InProceedingsofthe61stAnnualMeetingofthe
AssociationforComputationalLinguistics(Volume1: LongPapers),pp.16477–16508,2023a.
LuyuGao, AmanMadaan, ShuyanZhou, UriAlon, PengfeiLiu, YimingYang, JamieCallan, and
GrahamNeubig. Pal: Program-aidedlanguagemodels. InInternationalConferenceonMachine
Learning,pp.10764–10799.PMLR,2023b.
Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao Song, Xu Tan, Guoqing Liu, Jiang Bian,
andYujiuYang. Connectinglargelanguagemodelswithevolutionaryalgorithmsyieldspowerful
promptoptimizers. arXivpreprintarXiv:2309.08532,2023.
KelvinGuu,KentonLee,ZoraTung,PanupongPasupat,andMing-WeiChang. Realm: Retrieval-
augmentedlanguagemodelpre-training. arXivpreprintarXiv:2002.08909,2020. URLhttps:
//arxiv.org/abs/2002.08909.
BradenHancock,ParomaVarma,StephanieWang,MartinBringmann,PercyLiang,andChristopher
Re´. Training classifiers with natural language explanations. In Proceedings of the 56th Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1884–
1895.AssociationforComputationalLinguistics,2018. URLhttp://aclweb.org/anthology/
P18-1175.
Bin Hu, Chenyang Zhao, Pu Zhang, Zihao Zhou, Yuanhang Yang, Zenglin Xu, and Bin Liu. En-
ablingintelligentinteractionsbetweenanagentandanLLM:Areinforcementlearningapproach.
arXivpreprintarXiv:2306.03604,2023. URLhttps://arxiv.org/abs/2306.03604.
Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei
Han. Largelanguagemodelscanself-improve. arXivpreprintarXiv:2210.11610,2022.
Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane
Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and Edouard Grave. Few-shot learning with re-
trievalaugmentedlanguagemodels. arXivpreprintarXiv:2208.03299,2022.
EhudKarpas,OmriAbend,YonatanBelinkov,BarakLenz,OpherLieber,NirRatner,YoavShoham,
HofitBata,YoavLevine,KevinLeyton-Brown,etal. Mrklsystems: Amodular,neuro-symbolic
architecturethatcombineslargelanguagemodels, externalknowledgesourcesanddiscreterea-
soning. arXivpreprintarXiv:2205.00445,2022.
OmarKhattab,ChristopherPotts,andMateiZaharia.Baleen:RobustMulti-HopReasoningatScale
viaCondensedRetrieval. InThirty-FifthConferenceonNeuralInformationProcessingSystems,
2021a.
OmarKhattab,ChristopherPotts,andMateiZaharia.Relevance-guidedsupervisionforopenqawith
ColBERT. TransactionsoftheAssociationforComputationalLinguistics,9:929–944,2021b.
13

Preprint
Omar Khattab, Keshav Santhanam, Xiang Lisa Li, David Hall, Percy Liang, Christopher Potts,
and Matei Zaharia. Demonstrate-search-predict: Composing retrieval and language models for
knowledge-intensivenlp. arXivpreprintarXiv:2212.14024,2022.
TusharKhot,HarshTrivedi,MatthewFinlayson,YaoFu,KyleRichardson,PeterClark,andAshish
Sabharwal. Decomposed prompting: A modular approach for solving complex tasks. arXiv
preprintarXiv:2210.02406,2022.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large
languagemodelsarezero-shotreasoners. arXivpreprintarXiv:2205.11916,2022.
Angeliki Lazaridou, Elena Gribovskaya, Wojciech Stokowiec, and Nikolai Grigorev. Internet-
augmented language models through few-shot prompting for open-domain question answering.
arXivpreprintarXiv:2203.05115,2022.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Na-
man Goyal, Heinrich Ku¨ttler, Mike Lewis, Wen-tau Yih, Tim Rockta¨schel, Sebastian
Riedel, and Douwe Kiela. Retrieval-augmented generation for knowledge-intensive nlp
tasks. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Ad-
vances in Neural Information Processing Systems, volume 33, pp. 9459–9474. Curran Asso-
ciates,Inc.,2020.URLhttps://proceedings.neurips.cc/paper files/paper/2020/file/
6b493230205f780e1bc26945df7481e5-Paper.pdf.
JerryLiu. LlamaIndex,112022. URLhttps://github.com/jerryjliu/llama index.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri
Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement
withself-feedback. arXivpreprintarXiv:2303.17651,2023.
BryanMcCann,NitishShirishKeskar,CaimingXiong,andRichardSocher. Thenaturallanguage
decathlon: Multitask learning as question answering. arXiv:1806.08730, 2018. URL https:
//arxiv.org/abs/1806.08730.
Microsoft. Semantickernel. 2023. URLhttps://learn.microsoft.com/semantic-kernel/.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christo-
pher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna
Eloundou,GretchenKrueger,KevinButton,MatthewKnight,BenjaminChess,andJohnSchul-
man. WebGPT:Browser-assistedquestion-answeringwithhumanfeedback,2021. URLhttps:
//arxiv.org/abs/2112.09332.
OpenAI. Gpt-4technicalreport,2023.
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,CarrollLWainwright,PamelaMishkin,Chong
Zhang,SandhiniAgarwal,KatarinaSlama,AlexRay,etal. Traininglanguagemodelstofollow
instructionswithhumanfeedback. arXivpreprintarXiv:2203.02155,2022.
AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,GregoryChanan,Trevor
Killeen,ZemingLin,NataliaGimelshein,LucaAntiga,AlbanDesmaison,AndreasKopf,Edward
Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner,
Lu Fang, Junjie Bai, and Soumith Chintala. PyTorch: An imperative style, high-performance
deep learning library. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alche´-Buc, E. Fox,
and R. Garnett (eds.), Advances in Neural Information Processing Systems, volume 32. Curran
Associates,Inc.,2019. URLhttps://proceedings.neurips.cc/paper files/paper/2019/
file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf.
MohammadrezaPourrezaandDavoodRafiei. Din-sql: Decomposedin-contextlearningoftext-to-
sqlwithself-correction. arXivpreprintarXiv:2304.11015,2023.
OfirPress,MuruZhang,SewonMin,LudwigSchmidt,NoahASmith,andMikeLewis. Measuring
and narrowing the compositionality gap in language models. arXiv preprint arXiv:2210.03350,
2022.
14

Preprint
ReidPryzant,DanIter,JerryLi,YinTatLee,ChenguangZhu,andMichaelZeng.Automaticprompt
optimizationwith”gradientdescent”andbeamsearch. arXivpreprintarXiv:2305.03495,2023.
PengQi,XiaowenLin,LeoMehr,ZijianWang,andChristopherD.Manning. Answeringcomplex
open-domain questions through iterative query generation. In Proceedings of the 2019 Con-
ference on Empirical Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP), pp. 2590–2602, Hong Kong,
China, 2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1261. URL
https://aclanthology.org/D19-1261.
Peng Qi, Haejun Lee, Oghenetegiri Sido, Christopher D Manning, et al. Retrieve, rerank, read,
theniterate: Answeringopen-domainquestionsofarbitrarycomplexityfromtext. arXivpreprint
arXiv:2010.12527,2020. URLhttps://arxiv.org/abs/2010.12527.
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language un-
derstandingbygenerativepre-training. Ms,OpenAI,2018. URLhttps://openai.com/blog/
language-unsupervised/.
Alexander J Ratner, Christopher M De Sa, Sen Wu, Daniel Selsam, and Christopher Re´. Data
programming: Creating large training sets, quickly. In D. D. Lee, M. Sugiyama, U. V.
Luxburg, I. Guyon, and R. Garnett (eds.), Advances in Neural Information Processing Systems
29, pp. 3567–3575. Curran Associates, Inc., 2016. URL https://papers.nips.cc/paper/
6523-data-programming-creating-large-training-sets-quickly.
Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, and Matei Zaharia. Col-
BERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction. arXiv preprint
arXiv:2112.01488,2021.
TimoSchick,JaneDwivedi-Yu,RobertoDess`ı,RobertaRaileanu,MariaLomeli,LukeZettlemoyer,
NicolaCancedda,andThomasScialom. Toolformer: Languagemodelscanteachthemselvesto
usetools. arXivpreprintarXiv:2302.04761,2023.
Zhihong Shao, Yeyun Gong, Yelong Shen, Minlie Huang, Nan Duan, and Weizhu Chen. Syn-
theticprompting: Generatingchain-of-thoughtdemonstrationsforlargelanguagemodels. arXiv
preprintarXiv:2302.00618,2023.
NoahShinn, BeckLabash, andAshwinGopinath. Reflexion: anautonomousagentwithdynamic
memoryandself-reflection. arXivpreprintarXiv:2303.11366,2023.
ChengleiSi,ZheGan,ZhengyuanYang,ShuohangWang,JianfengWang,JordanBoyd-Graber,and
LijuanWang. Promptinggpt-3tobereliable. arXivpreprintarXiv:2210.09150,2022.
ZhiqingSun,XuezhiWang,YiTay,YimingYang,andDennyZhou.Recitation-augmentedlanguage
models. arXivpreprintarXiv:2210.01296,2022.
SeiyaTokui,KentaOono,ShoheiHido,andJustinClayton. Chainer: anext-generationopensource
frameworkfordeeplearning. InProceedingsofworkshoponmachinelearningsystems(Learn-
ingSys)inthetwenty-ninthannualconferenceonneuralinformationprocessingsystems(NIPS),
volume5,pp.1–6,2015.
HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,Niko-
layBashlykov,SoumyaBatra,PrajjwalBhargava,ShrutiBhosale,etal. Llama2: Openfounda-
tionandfine-tunedchatmodels. arXivpreprintarXiv:2307.09288,2023.
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Interleaving re-
trieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. arXiv
preprintarXiv:2212.10509,2022.
Fei Wang, James Decker, Xilun Wu, Gregory Essertel, and Tiark Rompf. Backpropaga-
tion with callbacks: Foundations for efficient and expressive differentiable programming.
In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Gar-
nett (eds.), Advances in Neural Information Processing Systems, volume 31. Curran Asso-
ciates,Inc.,2018.URLhttps://proceedings.neurips.cc/paper files/paper/2018/file/
34e157766f31db3d2099831d348a7933-Paper.pdf.
15

Preprint
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, and Denny Zhou. Rationale-
augmentedensemblesinlanguagemodels. arXivpreprintarXiv:2207.00747,2022a.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,EdChi,andDennyZhou. Self-consistency
improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171,
2022b.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny
Zhou. Chain of thought prompting elicits reasoning in large language models. arXiv preprint
arXiv:2201.11903,2022.
ThomasWolf, LysandreDebut, VictorSanh, JulienChaumond, ClementDelangue, AnthonyMoi,
Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick
von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gug-
ger, Mariama Drame, Quentin Lhoest, and Alexander Rush. Transformers: State-of-the-art
natural language processing. In Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing: System Demonstrations, pp. 38–45, Online, 2020. Associ-
ation for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-demos.6. URL https:
//aclanthology.org/2020.emnlp-demos.6.
Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun
Chen. Largelanguagemodelsasoptimizers. arXivpreprintarXiv:2309.03409,2023.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamWCohen,RuslanSalakhutdinov,
and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question
answering. arXivpreprintarXiv:1809.09600,2018.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
React: Synergizingreasoningandactinginlanguagemodels. arXivpreprintarXiv:2210.03629,
2022.
OriYoran,TomerWolfson,BenBogin,UriKatz,DanielDeutch,andJonathanBerant. Answering
questionsbymeta-reasoningovermultiplechainsofthought. arXivpreprintarXiv:2304.13007,
2023.
EricZelikman,YuhuaiWu,andNoahDGoodman. Star: Bootstrappingreasoningwithreasoning.
arXivpreprintarXiv:2203.14465,2022.
ZhuoshengZhang,AstonZhang,MuLi,andAlexSmola. Automaticchainofthoughtpromptingin
largelanguagemodels. arXivpreprintarXiv:2210.03493,2022.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. ExpeL:
LLM agents are experiential learners. arXiv preprint arXiv:2308.10144, 2023a. URL https:
//arxiv.org/pdf/2308.10144.
XuZhao,YuxiXie,KenjiKawaguchi,JunxianHe,andQizheXie. Automaticmodelselectionwith
largelanguagemodelsforreasoning. arXivpreprintarXiv:2305.14333,2023b.
16

Preprint
A ADVANCED SIGNATURES
When more control is desired, one can express signatures as Python classes to provide explicit
instructions of the transformation and describe the format or role of each field more directly. For
instance,thefollowingsignaturegeneratessearchqueriesusingcontextandanoptionalquestion:
1class GenerateSearchQuery(dspy.Signature):
2 """Write a simple search query that will help answer a complex question."""
3
4 context = dspy.InputField(desc="may contain relevant facts")
5 question = dspy.InputField()
6 query = dspy.OutputField(dtype=dspy.SearchQuery)
Usingtheabove,wecanspecifyacompletesystemforthegenerationofasyntheticIRdatasetwhere
thequeriesaremediatedbyaquestiongeneratedbytheLM:
1query_gen = dspy.Predict(GenerateSearchQuery)
2query_gen(context="Language typology")
3# Out: Prediction(question=’What are the main types of language classification?’,
query=’"language classification" OR "language typology" -wikipedia’)
If questions are available, they can be supplied as shown: query gen(context="Language
typology", question="What are the primary language families of South America?").
Asaworkinprogressfeature,userscanoptionallyspecifythetypeofoutputfieldsasbool, int,
float, list,ordictinsteadofthedefaultfree-formstringtype,asincontexts, question ->
answer found: bool.
B COMPARISON WITH EXISTING LIBRARIES LIKE LANGCHAIN AND
LLAMAINDEX
LangChainandLlamaIndexareperhapsthemostpopularlibraryinthegeneralspaceofprompting
LMs. TheselibrarieshaveadifferentfocuscomparedtoDSPyandtheysufferinternallyfromthe
promptengineeringchallengesthatDSPyaimstoresolve. Inparticular,whereasthegoalofDSPy
istotacklethefundamentalchallengesofpromptengineeringforbuildingnewLMcomputational
graphs, LangChainandLlamaIndexgenerallyhelpapplicationdeveloperswhoneedpre-packaged
components and chains, e.g., implementations of popular and reusable pipelines (e.g., particular
agentsandspecificretrievalpipelines)andtools(e.g.,connectionstovariousdatabasesandimple-
mentationsoflong-andshort-termmemoryforagents).
These off-the-shelf higher-level abstractions contrast with DSPy’s focus on introducing core com-
posable operators. In particular, DSPy introduces signatures (to abstract prompts), modules (to
abstractpromptingtechniques),andteleprompterstoactasoptimizersforarbitraryimperativecode
(DSPy programs) that chain modules together. Its goal is to help researchers and practitioners
buildnewLMpipelinesquicklyandachieveveryhighqualitythroughautomaticcompilation(self-
improvement)insteadofmanualpromptengineering.
In contrast, typical existing research implementations and existing libraries like LangChain and
LlamaIndexareimplementedusingmanualpromptengineering,whichisthekeyproblemthatDSPy
tackles. We conducted an informal study to highlight this. In late September 2023, we found
that the LangChain codebase contains 50 strings exceeding 1000 characters, which are generally
prompts, compared to none at all in DSPy. Indeed, a substantial number of LangChain’s Python
filesaresingularlydedicatedtotask-relatedtemplatingandpromptengineeringwith12prompts.py
files and and 42 prompt.py files. DSPy, on the other hand, provides a structured framework that
automaticallybootstrapsprompts. Thelibraryitselfdoesnotcontainasinglehand-writtenprompt
demonstrationforanytasksatthetimeofwriting,despitetheveryhighqualitywithvariousLMs.
To review the typical forms of prompt engineering in existing libraries, we consider the follow-
inginLangChain. TheLangChainProgram-AidedLanguageModelGaoetal.(2023a)chainpro-
gram uses few-shot learning, leveraging a template that is 3982 characters long with 8 math word
problems(Prompt2)andcorrespondingoutputtedprogramsaslearningexamplesforthelanguage
model. LangChain also contains a prompt for SQL query tasks for each of the databases like Or-
acle, GoogleSQL,DuckDB,Crate, andMySQL,withtheaveragelengthofthesepromptsat1058
characters. OthertaskareassuchasQAwithsources(PromptB)andGraph QAalsohavesignif-
17

Preprint
icantly lengthy prompt templates, with averages of 1337 and 722 characters, respectively. While
expert-writtenpromptscanbeuseful,webelievethatLM-andtask-adaptivepromptsbootstrapped
automaticallycanofferfarmorepower(andarefarmoremodular)thanhard-codingapromptper
database provider inside the code base. The next appendix section contains a number of prompts
copiedfromrelatedresearchpapersandexistinglibraries.
C SAMPLE LARGE PROMPTS
This section highlights a few popular existing frameworks that structure prompts with extensive
promptengineeringtemplates. Theprimaryobjectiveistocapturehowmanywordsandcharacters
are used for such large multi-line prompts defined for tasks or tools and present these example
prompts retrieved from open-sourced papers and repositories. The formatting of these example
promptsisadaptedfromGaoetal.(2023a).
| Task/ToolPrompt               | Source          | Words Characters |
| ----------------------------- | --------------- | ---------------- |
| Prompt1: Text-evidencechecker | Gaoetal.(2023a) | 818 4964         |
Prompt2: Mathwordproblems(PAL) LangChain&Gaoetal.(2023b) 566 3957
| Prompt3: ReAct                 | Yaoetal.(2022) | 593 3889 |
| ------------------------------ | -------------- | -------- |
| Prompt4: Zero-shotReAct        | LangChain      | 101 600  |
| Prompt5: QAwithsources         | LangChain      | 992 6197 |
| Prompt6: SQLMyScalequerying    | LangChain      | 343 2239 |
| Prompt7: Relevantdocsretrieval | LlamaIndex     | 129 719  |
| Prompt8: IRSchatbot            | LlamaIndex     | 389 2258 |
18

Preprint
1 [web]Iwillchecksomethingsyousaid.
2
3 (1)Yousaid:Yournoseswitchesbackandforthbetweennostrils.Whenyousleep,youswitchaboutevery45minutes.This
istopreventabuildupofmucus.It’scalledthenasalcycle.
4 Ichecked:Howoftendoyournostrilsswitch?
5 I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus
contributeslesstoairflow,whiletheotherbecomesdecongested.Onaverage,thecongestionpatternswitchesaboutevery
2hours,accordingtoasmall2016studypublishedinthejournalPLOSOne.
6 Yournose’sswitchingtimeisaboutevery2hours,not45minutes.
7 Thisdisagreeswithwhatyousaid.
8
9 (2)Yousaid:TheLittleHousebookswerewrittenbyLauraIngallsWilder.ThebookswerepublishedbyHarperCollins.
10 Ichecked:WhopublishedtheLittleHousebooks?
11 Ifoundthisarticle:Thesearethebooksthatstarteditall--thestoriesthatcapturedtheheartsandimaginationsof
children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books
remainafavoritetothisday.
12 TheLittleHousebookswerepublishedbyHarperCollins.
13 Thisagreeswithwhatyousaid.
14
15 (3)Yousaid:TheStanfordPrisonExperimentwasconductedinthebasementofJordanHall,Stanford’spsychologybuilding.
16 Ichecked:WherewasStanfordPrisonExperimentconducted?
17 I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set
outtoexaminethepsychologicaleffectsofauthorityandpowerlessnessinaprisonenvironment.
18 TheStanfordPrisonExperimentwasconductedinJordanHall.
19 Thisagreeswithwhatyousaid.
20
21 (4)Yousaid:Socialworkisaprofessionthatisbasedinthephilosophicaltraditionofhumanism.Itisanintellectual
disciplinethathasitsrootsinthe1800s.
22 Ichecked:Whendidsocialworkhaveitsroots?
23 I found this article: The Emergence and Growth of the Social work Profession<br><br> Social work’s roots were planted in
the1880s,whencharityorganizationsocieties(COS)werecreatedtoorganizemunicipalvoluntaryreliefassociationsand
settlementhouseswereestablished.
24 Socialworkhasitsrootsinthe1880s,not1800s.
25 Thisdisagreeswithwhatyousaid.
26
27 (5)Yousaid:TheHavel-Hakimialgorithmisanalgorithmforconvertingtheadjacencymatrixofagraphintoitsadjacency
list.ItisnamedafterVaclavHavelandSamihHakimi.
28 Ichecked:WhatistheHavel-Hakimialgorithm?
29 I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree
sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm.
ThealgorithmwaspublishedbyHavel(1955),andlaterbyHakimi(1962).
30 Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists, or
provingthatonecannotfindapositiveanswer,notconvertingtheadjacencymatrixofagraphintoitsadjacencylist.
31 Thisdisagreeswithwhatyousaid.
32
33 (6) You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film
DirtyDancing.ThesongwasproducedbyMichaelLloyd.
34 Ichecked:Whowastheproducerof"(I’veHad)TheTimeofMyLife"?
35 Ifoundthisarticle:OnSeptember8,2010,theoriginaldemoofthissong,alongwitharemixbyproducerMichaelLloyd,
was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at
StanfordUniversity.
36 "TimeofMyLife"wasproducedbyMichaelLloyd.
37 Thisagreeswithwhatyousaid.
38
39 (7) You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved
inappropriatelytowardsaLabourPartyactivist,AvaEtemadzadeh.
40 Ichecked:WhywasKelvinHopinssuspenededfromtheLaborParty?
41 I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against
himwasabletobeconcluded,thepartyhasconfirmed.KelvinHopkinswasaccusedin2017ofinappropriatephysicalcontact
andwassuspendedbytheLabourpartypendinganinvestigation.Thisagreeswithwhatyousaid.
42 KelvinHopinswassuspendedbecausehehadallegedlysexuallyharassedandbehavedinappropriatelytowardsaLabourParty
activist,AvaEtemadzadeh.
43 Thisagreeswithwhatyousaid.
44
45 (8)Yousaid:InthebattlesofLexingtonandConcord,theBritishsidewasledbyGeneralThomasSmith.
46 Ichecked:WholedtheBritishsideinthebattleofLexingtonandConcord?
47 I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant
ColonelFrancisSmith.Therewere700Britishregulars.
48 TheBritishsidewasledbyLieutenantColonelFrancisSmith,notGeneralThomasHall.
49 Thisdisagreeswithwhatyousaid.
50
51 (9)Yousaid:{text}
52 Ichecked:{query}
53 Ifoundthisarticle:{evidence}
54
Figure 1: Example few-shot prompt using a reasoning chain for agreement model that identifies
inconsistenciesbetweentextandevidence(Gaoetal.,2023a).
19

Preprint
1 Q:Oliviahas$23.Sheboughtfivebagelsfor$3each.Howmuchmoneydoesshehaveleft?
2
3 #solutioninPython:
4
5
6 defsolution():
7 """Oliviahas$23.Sheboughtfivebagelsfor$3each.Howmuchmoneydoesshehaveleft?"""
8 moneyinitial=23
9 bagels=5
10 bagelcost=3
11 moneyspent=bagels*bagelcost
12 moneyleft=moneyinitial-moneyspent
13 result=moneyleft
14 returnresult
15
16
17
18
19
20 Q:Michaelhad58golfballs.Ontuesday,helost23golfballs.Onwednesday,helost2more.Howmanygolfballsdidhe
haveattheendofwednesday?
21
22 #solutioninPython:
23
24
25 defsolution():
26 """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls
didhehaveattheendofwednesday?"""
27 golfballsinitial=58
28 golfballslosttuesday=23
29 golfballslostwednesday=2
30 golfballsleft=golfballsinitial-golfballslosttuesday-golfballslostwednesday
31 result=golfballsleft
32 returnresult
33
34
35
36
37
38 Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday.
Howmanycomputersarenowintheserverroom?
39
40 #solutioninPython:
41
42
43 defsolution():
44 """Therewereninecomputersintheserverroom.Fivemorecomputerswereinstalledeachday,frommondaytothursday.
Howmanycomputersarenowintheserverroom?"""
45 computersinitial=9
46 computersperday=5
47 numdays=4
48 computersadded=computersperday*numdays
49 computerstotal=computersinitial+computersadded
50 result=computerstotal
51 returnresult
52
53
54
55
56
57 Q:Shawnhasfivetoys.ForChristmas,hegottwotoyseachfromhismomanddad.Howmanytoysdoeshehavenow?
58
59 #solutioninPython:
60
61
62 defsolution():
63 """Shawnhasfivetoys.ForChristmas,hegottwotoyseachfromhismomanddad.Howmanytoysdoeshehavenow?"""
64 toysinitial=5
65 momtoys=2
66 dadtoys=2
67 totalreceived=momtoys+dadtoys
68 totaltoys=toysinitial+totalreceived
69 result=totaltoys
70 returnresult
71
72
73
74
75
76 Q:Jasonhad20lollipops.HegaveDennysomelollipops.NowJasonhas12lollipops.HowmanylollipopsdidJasongiveto
Denny?
77
78 #solutioninPython:
79 20
80
81

Preprint
1
2
3
4 defsolution():
5 """Jasonhad20lollipops.HegaveDennysomelollipops.NowJasonhas12lollipops.HowmanylollipopsdidJasongive
toDenny?"""
6 jasonlollipopsinitial=20
7 jasonlollipopsafter=12
8 dennylollipops=jasonlollipopsinitial-jasonlollipopsafter
9 result=dennylollipops
10 returnresult
11
12
13
14
15
16 Q:Leahhad32chocolatesandhersisterhad42.Iftheyate35,howmanypiecesdotheyhaveleftintotal?
17
18 #solutioninPython:
19
20 defsolution():
21 """Leahhad32chocolatesandhersisterhad42.Iftheyate35,howmanypiecesdotheyhaveleftintotal?"""
22 leahchocolates=32
23 sisterchocolates=42
24 totalchocolates=leahchocolates+sisterchocolates
25 chocolateseaten=35
26 chocolatesleft=totalchocolates-chocolateseaten
27 result=chocolatesleft
28 returnresult
29
30
31
32
33
34 Q:Ifthereare3carsintheparkinglotand2morecarsarrive,howmanycarsareintheparkinglot?
35
36 #solutioninPython:
37
38
39 defsolution():
40 """Ifthereare3carsintheparkinglotand2morecarsarrive,howmanycarsareintheparkinglot?"""
41 carsinitial=3
42 carsarrived=2
43 totalcars=carsinitial+carsarrived
44 result=totalcars
45 returnresult
46
47
48
49
50
51 Q:Thereare15treesinthegrove.Groveworkerswillplanttreesinthegrovetoday.Aftertheyaredone,therewillbe
21trees.Howmanytreesdidthegroveworkersplanttoday?
52
53 #solutioninPython:
54
55
56 defsolution():
57 """Thereare15treesinthegrove.Groveworkerswillplanttreesinthegrovetoday.Aftertheyaredone,therewill
be21trees.Howmanytreesdidthegroveworkersplanttoday?"""
58 treesinitial=15
59 treesafter=21
60 treesadded=treesafter-treesinitial
61 result=treesadded
62 returnresult
63
64
65
66
67
68 Q:{question}
69
70 #solutioninPython:
Figure2: PALexamplefew-shotpromptforsolvingmathquestionsbygeneratingcode.
21

Preprint
1 SolveaquestionansweringtaskwithinterleavingThought,Action,Observationsteps.Thoughtcanreasonaboutthecurrent
situation,andActioncanbethreetypes:
2 (1)Search[entity],whichsearchestheexactentityonWikipediaandreturnsthefirstparagraphifitexists.Ifnot,it
willreturnsomesimilarentitiestosearch.
3 (2)Lookup[keyword],whichreturnsthenextsentencecontainingkeywordinthecurrentpassage.
4 (3)Finish[answer],whichreturnstheanswerandfinishesthetask.
5 Herearesomeexamples.
6 Question:WhatistheelevationrangefortheareathattheeasternsectoroftheColoradoorogenyextendsinto?
7 Action1:Search[Coloradoorogeny]
8 Observation1:TheColoradoorogenywasanepisodeofmountainbuilding(anorogeny)inColoradoandsurroundingareas.
9 Action2:Lookup[easternsector]
10 Observation2:(Result1/1)TheeasternsectorextendsintotheHighPlainsandiscalledtheCentralPlainsorogeny.
11 Action3:Search[HighPlains]
12 Observation3:HighPlainsreferstooneoftwodistinctlandregions:
13 Action4:Search[HighPlains(UnitedStates)]
14 Observation 4: The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation
fromaround1,800to7,000ft(550to2,130m).[3]
15 Action5:Finish[1,800to7,000ft]
16 Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening
namedafterwho?
17 Action1:Search[Milhouse]
18 Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons
voicedbyPamelaHaydenandcreatedbyMattGroening.
19 Action2:Lookup[namedafter]
20 Observation2:(Result1/1)MilhousewasnamedafterU.S.presidentRichardNixon,whosemiddlenamewasMilhous.
21 Action3:Finish[RichardNixon]
22 Question:WhichdocumentaryisaboutFinnishrockgroups,AdamClaytonPowellorTheSaimaaGesture?
23 Action1:Search[AdamClaytonPowell]
24 Observation 1: Could not find [Adam Clayton Powell]. Similar: [’Adam Clayton Powell III’, ’Seventh Avenue (Manhattan)’,
’AdamClaytonPowellJr.StateOfficeBuilding’,’IsabelWashingtonPowell’,’AdamPowell’,’AdamClaytonPowell(film)’,
’GiancarloEsposito’].
25 Action2:Search[AdamClaytonPowell(film)]
26 Observation2:AdamClaytonPowellisa1989AmericandocumentaryfilmdirectedbyRichardKilberg.Thefilmisaboutthe
rise and fall of influential African-American politician Adam Clayton Powell Jr.[3][4] It was later aired as part of the
PBSseriesTheAmericanExperience.
27 Action3:Finish[TheSaimaaGesture]
28 Question:WhatprofessiondoesNicholasRayandEliaKazanhaveincommon?
29 Action1:Search[NicholasRay]
30 Observation 1: Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 { June 16, 1979) was an American film
director,screenwriter,andactorbestknownforthe1955filmRebelWithoutaCause.
31 Action2:Search[EliaKazan]
32 Observation2:EliaKazanwasanAmericanfilmandtheatredirector,producer,screenwriterandactor.
33 Action3:Finish[director,screenwriter,actor]
34 Question:WhichmagazinewasstartedfirstArthur’sMagazineorFirstforWomen?
35 Action1:Search[Arthur’sMagazine]
36 Observation 1: Arthur’s Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th
century.
37 Action2:Search[FirstforWomen]
38 Observation2:FirstforWomenisawoman’smagazinepublishedbyBauerMediaGroupintheUSA.[1]Themagazinewasstarted
in1989.
39 Action3:Finish[Arthur’sMagazine]
40 Question:WerePavelUrysohnandLeonidLevinknownforthesametypeofwork?
41 Action1:Search[PavelUrysohn]
42 Observation1:PavelSamuilovichUrysohn(February3,1898ˆaAugust17,1924)wasaSovietmathematicianwhoisbestknown
forhiscontributionsindimensiontheory.
43 Action2:Search[LeonidLevin]
44 Observation2:LeonidAnatolievichLevinisaSoviet-Americanmathematicianandcomputerscientist.
45 Action3:Finish[yes]
Figure3: ReActexamplepromptforinterleavingThought,Action,Observationsteps.
22

Preprint
1 Answerthefollowingquestionsasbestyoucan.Youhaveaccesstothefollowingtools:
2 Search:usefulforwhenyouneedtoanswerquestionsabouttheworld
3 Usethefollowingformat:
4 Question:theinputquestionyoumustanswer
5 Thought:youshouldalwaysthinkaboutwhattodo
6 Action:theactiontotake,shouldbeoneof[Search]
7 ActionInput:theinputtotheaction
8 Observation:theresultoftheaction
9 ...(thisThought/Action/ActionInput/ObservationcanrepeatNtimes)
10 Thought:Inowknowthefinalanswer
11 FinalAnswer:thefinalanswertotheoriginalinputquestion
12 Begin!
13 Question:{question}
14 Thought:
Figure4: LangchainReActexamplepromptforinterleavingThought,Action,Observationsteps.
23

Preprint
1 Giventhefollowingextractedpartsofalongdocumentandaquestion,createafinalanswerwithreferences("SOURCES").
2 Ifyoudon’tknowtheanswer,justsaythatyoudon’tknow.Don’ttrytomakeupananswer.
3 ALWAYSreturna"SOURCES"partinyouranswer.
4
5 QUESTION:Whichstate/country’slawgovernstheinterpretationofthecontract?
6 =========
7 Content: This Agreement is governed by English law and the parties submit to the exclusive jurisdiction of the English
courts in relation to any dispute (contractual or non-contractual) concerning this Agreement save that either party may
applytoanycourtforaninjunctionorotherrelieftoprotectitsIntellectualPropertyRights.
8 Source:28-pl
9 Content:NoWaiver.FailureordelayinexercisinganyrightorremedyunderthisAgreementshallnotconstituteawaiver
ofsuch(oranyother)rightorremedy.
10 11.7Severability.Theinvalidity,illegalityorunenforceabilityofanyterm(orpartofaterm)ofthisAgreementshall
notaffectthecontinuationinforceoftheremainderoftheterm(ifany)andthisAgreement.
11 11.8 No Agency. Except as expressly stated otherwise, nothing in this Agreement shall create an agency, partnership or
jointventureofanykindbetweentheparties.
12 11.9NoThird-PartyBeneficiaries.
13 Source:30-pl
14 Content: (b) if Google believes, in good faith, that the Distributor has violated or caused Google to violate any
Anti-BriberyLaws(asdefinedinClause8.5)orthatsuchaviolationisreasonablylikelytooccur,
15 Source:4-pl
16 =========
17 FINALANSWER:ThisAgreementisgovernedbyEnglishlaw.
18 SOURCES:28-pl
19
20 QUESTION:WhatdidthepresidentsayaboutMichaelJackson?
21 =========
22 Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet.
JusticesoftheSupremeCourt.MyfellowAmericans.
23 LastyearCOVID-19keptusapart.Thisyearwearefinallytogetheragain.
24 Tonight,wemeetasDemocratsRepublicansandIndependents.ButmostimportantlyasAmericans.
25 WithadutytooneanothertotheAmericanpeopletotheConstitution.
26 Andwithanunwaveringresolvethatfreedomwillalwaystriumphovertyranny.
27 Sixdaysago,Russia’sVladimirPutinsoughttoshakethefoundationsofthefreeworldthinkinghecouldmakeitbendto
hismenacingways.Buthebadlymiscalculated.
28 HethoughthecouldrollintoUkraineandtheworldwouldrollover.Insteadhemetawallofstrengthheneverimagined.
29 HemettheUkrainianpeople.
30 FromPresidentZelenskyytoeveryUkrainian,theirfearlessness,theircourage,theirdetermination,inspirestheworld.
31 Groupsofcitizensblockingtankswiththeirbodies.Everyonefromstudentstoretireesteachersturnedsoldiersdefending
theirhomeland.
32 Source:0-pl
33 Content:Andwewon’tstop.
34 WehavelostsomuchtoCOVID-19.Timewithoneanother.Andworstofall,somuchlossoflife.
35 Let’s use this moment to reset. Let’s stop looking at COVID-19 as a partisan dividing line and see it for what it is: A
God-awfuldisease.
36 Let’sstopseeingeachotherasenemies,andstartseeingeachotherforwhowereallyare:FellowAmericans.
37 We can’t change how divided we’ve been. But we can change how we move forward|on COVID-19 and other issues we must face
together.
38 I recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner,
OfficerJasonRivera.
39 Theywererespondingtoa9-1-1callwhenamanshotandkilledthemwithastolengun.
40 OfficerMorawas27yearsold.
41 OfficerRiverawas22.
42 BothDominicanAmericanswho’dgrownuponthesamestreetstheylaterchosetopatrolaspoliceofficers.
43 I spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their
missiontorestorethetrustandsafetyeverycommunitydeserves.
44 Source:24-pl
45 Content: And a proud Ukrainian people, who have known 30 years of independence, have repeatedly shown that they will not
tolerateanyonewhotriestotaketheircountrybackwards.
46 ToallAmericans,Iwillbehonestwithyou,asI’vealwayspromised.ARussiandictator,invadingaforeigncountry,has
costsaroundtheworld.
47 AndI’mtakingrobustactiontomakesurethepainofoursanctionsistargetedatRussia’seconomy.AndIwilluseevery
toolatourdisposaltoprotectAmericanbusinessesandconsumers.
48 Tonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil
fromreservesaroundtheworld.
49 America will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready
todomoreifnecessary,unifiedwithourallies.
50 Thesestepswillhelpbluntgaspriceshereathome.AndIknowthenewsaboutwhat’shappeningcanseemalarming.
51 ButIwantyoutoknowthatwearegoingtobeokay.
52 Source:5-pl
53 Content:Moresupportforpatientsandfamilies.
54 Togetthere,IcallonCongresstofundARPA-H,theAdvancedResearchProjectsAgencyforHealth.
55 It’sbasedonDARPA|theDefenseDepartmentprojectthatledtotheInternet,GPS,andsomuchmore.
56 ARPA-Hwillhaveasingularpurpose|todrivebreakthroughsincancer,Alzheimer’s,diabetes,andmore.
24

Preprint
1 Aunityagendaforthenation.
2 Wecandothis.
3 MyfellowAmericans|tonight,wehavegatheredinasacredspace|thecitadelofourdemocracy.
4 In this Capitol, generation after generation, Americans have debated great questions amid great strife, and have done
greatthings.
5 Wehavefoughtforfreedom,expandedliberty,defeatedtotalitarianismandterror.
6 Andbuiltthestrongest,freest,andmostprosperousnationtheworldhaseverknown.
7 Nowisthehour.
8 Ourmomentofresponsibility.
9 Ourtestofresolveandconscience,ofhistoryitself.
10 Itisinthismomentthatourcharacterisformed.Ourpurposeisfound.Ourfutureisforged.
11 WellIknowthisnation.
12 Source:34-pl
13 =========
14 FINALANSWER:ThepresidentdidnotmentionMichaelJackson.
15 SOURCES:
16
17 QUESTION:{question}
18 =========
19 {summaries}
20 =========
21 FINALANSWER:
Figure5: LangchainexamplepromptforQAwithsources.
1 You are a MyScale expert. Given an input question, first create a syntactically correct MyScale query to run, then look
attheresultsofthequeryandreturntheanswertotheinputquestion.
2 MyScalequerieshasavectordistancefunctioncalledDISTANCE(column,array)tocomputerelevancetotheuser’squestion
andsortthefeaturearraycolumnbytherelevance.
3 Whenthequeryisaskingfor{topk}closestrow,youhavetousethisdistancefunctiontocalculatedistancetoentity’s
arrayonvectorcolumnandorderbythedistancetoretrieverelevantrows.
4 *NOTICE*:DISTANCE(column,array)onlyacceptanarraycolumnasitsfirstargumentandaNeuralArray(entity)asitssecond
argument.YoualsoneedauserdefinedfunctioncalledNeuralArray(entity)toretrievetheentity’sarray.
5 Unlesstheuserspecifiesinthequestionaspecificnumberofexamplestoobtain,queryforatmost{topk}resultsusing
theLIMITclauseasperMyScale.Youshouldonlyorderaccordingtothedistancefunction.
6 Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap
eachcolumnnameindoublequotes(")todenotethemasdelimitedidentifiers.
7 Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do
notexist.Also,payattentiontowhichcolumnisinwhichtable.
8 Pay attention to use today() function to get the current date, if the question involves "today". ORDER BY clause should
alwaysbeafterWHEREclause.DONOTaddsemicolontotheendofSQL.Payattentiontothecommentintableschema.
9
10 Usethefollowingformat:
11 ========tableinfo========
12 {tableinfo}
13 Question:{input}
14 SQLQuery:
15
16 Herearesomeexamples:
17 ========tableinfo========
18 CREATETABLE"ChatPaper"(
19 abstractString,
20 idString,
21 vectorArray(Float32),
22 )ENGINE=ReplicatedReplacingMergeTree()
23 ORDERBYid
24 PRIMARYKEYid
25 Question:WhatisFeaturePyramidNetwork?
26 SQLQuery: SELECT ChatPaper.title, ChatPaper.id, ChatPaper.authors FROM ChatPaper ORDER BY DISTANCE(vector,
NeuralArray(PaperRankcontribution))LIMIT{topk}
27
28 Let’sbegin:
29 ========tableinfo========
30 {tableinfo}
31 Question:{input}
32 SQLQuery:
Figure6: LangchainexamplepromptforSQLqueryingusingMyScale.
25

Preprint
1 Alistofdocumentsisshownbelow.Eachdocumenthasanumbernexttoitalongwithasummaryofthedocument.Aquestion
isalsoprovided.
2 Respondwiththenumbersofthedocumentsyoushouldconsulttoanswerthequestion,inorderofrelevance,aswellasthe
relevancescore.
3 Therelevancescoreisanumberfrom1-10basedonhowrelevantyouthinkthedocumentistothequestion.
4 Donotincludeanydocumentsthatarenotrelevanttothequestion.
5
6 Exampleformat:
7 Document1:
8 <summaryofdocument1>
9
10 Document2:
11 <summaryofdocument2>
12
13 ...
14
15 Document10:
16 <summaryofdocument10>
17
18 Question:<question>
19 Answer:
20 Doc:9,Relevance:7
21 Doc:3,Relevance:4
22 Doc:7,Relevance:3
23
24 Let’strythisnow:
25 {contextstr}
26 Question:{querystr}
27 Answer:
Figure 7: LlamaIndex example prompt for returning relevant documents and corresponding sum-
maries.
1 YouareanIRSchatbotwhoseprimarygoalistohelpuserswithfilingtheirtaxreturnsforthe2022year.
2 Provideconciserepliesthatarepoliteandprofessional.
3 Answer questions truthfully based on official government information, with consideration to context provided below on
changesfor2022thatcanaffecttaxrefund.
4 Do not answer questions that are not related to United States tax procedures and respond with "I can only help with any
tax-relatedquestionsyoumayhave.".
5 Ifyoudonotknowtheanswertoaquestion,respondbysaying\Idonotknowtheanswertoyourquestion.Youmaybeable
tofindyouransweratwww.irs.gov/faqs"
6
7 Changesfor2022thatcanaffecttaxrefund:
8 Changes in the number of dependents, employment or self-employment income and divorce, among other factors, may affect
your tax-filing status and refund. No additional stimulus payments. Unlike 2020 and 2021, there were no new stimulus
paymentsfor2022sotaxpayersshouldnotexpecttogetanadditionalpayment.
9 Some tax credits return to 2019 levels. This means that taxpayers will likely receive a significantly smaller refund
comparedwiththeprevioustaxyear.ChangesincludeamountsfortheChildTaxCredit(CTC),theEarnedIncomeTaxCredit
(EITC)andtheChildandDependentCareCreditwillreverttopre-COVIDlevels.
10 For 2022, the CTC is worth $2,000 for each qualifying child. A child must be under age 17 at the end of 2022 to be a
qualifying child. For the EITC, eligible taxpayers with no children will get $560 for the 2022 tax year. The Child and
DependentCareCreditreturnstoamaximumof$2,100in2022.
11 No above-the-line charitable deductions. During COVID, taxpayers were able to take up to a $600 charitable donation tax
deductionontheirtaxreturns.However,fortaxyear2022,taxpayerswhodon’titemizeandwhotakethestandarddeduction,
won’tbeabletodeducttheircharitablecontributions.
12 MorepeoplemaybeeligibleforthePremiumTaxCredit.Fortaxyear2022,taxpayersmayqualifyfortemporarilyexpanded
eligibilityforthepremiumtaxcredit.
13 Eligibility rules changed to claim a tax credit for clean vehicles. Review the changes under the Inflation Reduction Act
of2022toqualifyforaCleanVehicleCredit.
Figure8: LlamaIndexexamplepromptforIRSchatbotguidelines.
26

Preprint
D MODULES
D.1 PREDICT
1class Predict(dspy.Module):
| 2   | def __init__(self, |     | signature,                  | **config): |     |     |     |     |
| --- | ------------------ | --- | --------------------------- | ---------- | --- | --- | --- | --- |
|     | self.signature     |     | = dspy.Signature(signature) |            |     |     |     |     |
3
| 4   | self.config |     | = config |     |     |     |     |     |
| --- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
5
| 6   | # Module            | Parameters.              |     |                                  |       |             |     |     |
| --- | ------------------- | ------------------------ | --- | -------------------------------- | ----- | ----------- | --- | --- |
| 7   | self.lm             | = dspy.ParameterLM(None) |     |                                  | # use | the default | LM  |     |
|     | self.demonstrations |                          | =   | dspy.ParameterDemonstrations([]) |       |             |     |     |
8
9
|     | def forward(self, |     | **kwargs): |     |     |     |     |     |
| --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- |
10
| 11  | lm =           | get_the_right_lm(self.lm, |                                                     |     | kwargs) |     |         |         |
| --- | -------------- | ------------------------- | --------------------------------------------------- | --- | ------- | --- | ------- | ------- |
| 12  | signature      | =                         | get_the_right_signature(self.signature,             |     |         |     | kwargs) |         |
|     | demonstrations |                           | = get_the_right_demonstrations(self.demonstrations, |     |         |     |         | kwargs) |
13
14
|     | prompt | = signature(demos=self.demos, |     |     |     | **kwargs) |     |     |
| --- | ------ | ----------------------------- | --- | --- | --- | --------- | --- | --- |
15
| 16  | completions |     | = lm.generate(prompt, |     | **self.config) |     |     |     |
| --- | ----------- | --- | --------------------- | --- | -------------- | --- | --- | --- |
17 prediction = Prediction.from_completions(completions, signature=signature)
18
| 19  | if dsp.settings.compiling |         |                      | is  | not None:      |     |                     |     |
| --- | ------------------------- | ------- | -------------------- | --- | -------------- | --- | ------------------- | --- |
|     |                           | trace = | dict(predictor=self, |     | inputs=kwargs, |     | outputs=prediction) |     |
20
| 21  |     | dspy.settings.traces.append(trace) |     |     |     |     |     |     |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
22
return prediction
23
D.2 CHAINOFTHOUGHT
1class ChainOfThought(dspy.Module):
| 2   | def __init__(self, |     | signature): |     |     |     |     |     |
| --- | ------------------ | --- | ----------- | --- | --- | --- | --- | --- |
3
4 # Modify signature from ‘*inputs -> *outputs‘ to ‘*inputs -> rationale, *outputs‘.
rationale_field = dspy.OutputField(prefix="Reasoning: Let’s think step by step.")
5
|     | signature | =   | dspy.Signature(signature).prepend_output_field(rationale_field) |     |     |     |     |     |
| --- | --------- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
6
7
|     | # Declare | a   | sub-module | with the | modified | signature. |     |     |
| --- | --------- | --- | ---------- | -------- | -------- | ---------- | --- | --- |
8
| 9   | self.predict |     | = dspy.Predict(self.signature) |     |     |     |     |     |
| --- | ------------ | --- | ------------------------------ | --- | --- | --- | --- | --- |
10
| 11  | def forward(self, |         | **kwargs): |     |                 |     |     |     |
| --- | ----------------- | ------- | ---------- | --- | --------------- | --- | --- | --- |
| 12  | # Just            | forward | the inputs | to  | the sub-module. |     |     |     |
return self.predict(**kwargs)
13
27

Preprint
E TELEPROMPTERS
E.1 BOOTSTRAPFEWSHOT
1class SimplifiedBootstrapFewShot(Teleprompter):
2 def __init__(self, metric=None):
3 self.metric = metric
4
5 def compile(self, student, trainset, teacher=None):
6 teacher = teacher if teacher is not None else student
7 compiled_program = student.deepcopy()
8
9 # Step 1. Prepare mappings between student and teacher Predict modules.
10 # Note: other modules will rely on Predict internally.
11 assert student_and_teacher_have_compatible_predict_modules(student, teacher)
12 name2predictor, predictor2name = map_predictors_recursively(student, teacher)
13
14 # Step 2. Bootstrap traces for each Predict module.
15 # We’ll loop over the training set. We’ll try each example once for simplicity.
16 for example in trainset:
17 if we_found_enough_bootstrapped_demos(): break
18
19 # turn on compiling mode which will allow us to keep track of the traces
20 with dspy.setting.context(compiling=True):
21 # run the teacher program on the example, and get its final prediction
22 # note that compiling=True may affect the internal behavior here
23 prediction = teacher(**example.inputs())
24
25 # get the trace of the all interal Predict calls from teacher program
26 predicted_traces = dspy.settings.trace
27
28 # if the prediction is valid, add the example to the traces
29 if self.metric(example, prediction, predicted_traces):
30 for predictor, inputs, outputs in predicted_traces:
31 d = dspy.Example(automated=True, **inputs, **outputs)
32 predictor_name = self.predictor2name[id(predictor)]
33 compiled_program[predictor_name].demonstrations.append(d)
34
35
36 return compiled_program
E.2 BOOTSTRAPFEWSHOTWITHRANDOMSEARCH
1class SimplifiedBootstrapFewShotWithRandomSearch(Teleprompter):
2 def __init__(self, metric = None, trials=16):
3 self.metric = metric
4 self.trials = trials
5
6 def compile(self, student, *, teacher=None, trainset, valset=None):
7 # we can do forms of cross-validation if valset is unset.
8 valset = trainset if valset is None else valset
9
10 candidates = []
11 for seed in range(self.trials):
12 # Create a new basic bootstrap few-shot program.
13 shuffled_trainset = shuffle(trainset, seed=seed)
14 tp = BootstrapFewShot(metric=metric, max_bootstrap_demos=random_size())
15 candidate_program = tp.compile(student, shuffled_trainset, teacher)
16
17 # Step 2: Evaluate the generated candidate program.
18 score = evaluate_program(candidate_program, self.metric, valset)
19 candidates.append((score, candidate_program))
20
21 # return the best candidate program.
22 return max(candidates, key=lambda x: x[0])[1]
28

Preprint
E.3 BOOTSTRAPFEWSHOTWITHOPTUNA
1class SimplifiedBootstrapFewShotWithOptuna(Teleprompter):
2 def __init__(self, metric, trials=16):
3 self.metric = metric
4 self.trials = trials
5
6 def objective(self, trial):
7 pool = self.pool
8
9 # Step 1: Create copy of student program.
10 candidate_program = self.student.reset_copy()
11
12 # Step 2: Based on trial, select demos for each predictor in program.
13 # Note. For simplicity, we can just select a single demo for each predictor.
14 # But we can easily tune the number of demonstrations to select here.
15 for (name, predictor1), (_, predictor2) in \
16 zip(pool.named_predictors(), candidate_program.named_predictors()):
17 all_demos = predictor1.demos
18 demo_index = trial.suggest_int(f"demo_index_for_{name}", 0, len(all_demos) - 1)
19 predictor2.demos = [all_demos[demo_index]]
20
21 # Step 3: Evaluate the modified candidate program.
22 score = evaluate_program(candidate_program, self.metric, self.valset)
23
24 # Step 4: Store the candidate for Optuna to select highest-scoring program.
25 trial.set_user_attr("program", candidate_program)
26 return score
27
28 def compile(self, student, trainset, teacher=None, valset=None):
29 self.trainset = trainset
30 self.valset = trainset if valset is None else valset
31
32 self.student = student.deepcopy()
33 self.teacher = teacher.deepcopy() if teacher else student.deepcopy()
34
35 # Leverage BootstrapFewshot to create a large number of potential demonstrations.
36 tp = BootstrapFewShot()
37 self.pool = tp.compile(self.student, self.teacher, self.trainset, self.metric)
38
39 # Use Optuna to find the best program by optimizing the objective function.
40 best_program = optimize_with_optuna(self.objective)
41
42 print(’Best score:’, best_program.score)
43 print(’Best program:’, best_program)
44 return best_program
29

Preprint
F EXAMPLES OF THE PROMPTS AUTOMATICALLY GENERATED BY DSPY
ForGSM8K,weincludethepromptbootstrappedbyDSPyforGSM8Kllama2-13b-chatforthe
vanillaprogramcompiledwithbootstrap×2inFigure9.
WealsoincludeaCoTpromptforGSM8Kandagenerate querypromptfromthemultihoppro-
gram for HotPotQA. All of these, particularly their demonstrations’ labels and their selection, are
generatedbyDSPyautomaticallyusingllama2-13b-chat.
30

Preprint
1 Giventhefields‘question‘,producethefields‘answer‘.
2
3 ---
4
5 Followthefollowingformat.
6
7 Question:${question}
8 Answer:${answer}
9
10 ---
11
12 Question:JimmyandIrenegoshoppingforclothesonaTuesday,whereseniorcitizensgeta10%discountontheirpurchases.
Jimmy picks out 3 shorts from the $15 rack. Irene grabs 5 shirts from the $17 rack. How much money do they give to the
cashier?
13 Answer:Jimmypicksout3shortsat$15each=$45.Irenegrabs5shirtsat$17each=$85.Totalcost=$45+$85=$130.
Since senior citizens get a 10% discount, they will pay 10% of $130 = $13. So, they will give the cashier $130 - $13 =
$117.---
14
15 ---
16
17 Question:
Figure 9: Copy of the prompt automatically generated by DSPy for GSM8K Llama2-13b-chat
vanillaprogramcompiledwithbootstrap×2.
1 Giventhefields‘question‘,producethefields‘answer‘.
2
3 ---
4
5 Followthefollowingformat.
6
7 Question:${question}
8 Reasoning:Let’sthinkstepbystepinorderto$producetheanswer.We...
9 Answer:${answer}
10
11 ---
12
13 Question: Mark is baking bread. He has to let it rise for 120 minutes twice. He also needs to spend 10 minutes kneading
itand30minutesbakingit.HowmanyminutesdoesittakeMarktofinishmakingthebread?
14 Reasoning:Let’sthinkstepbystepinordertofindouthowmanyminutesittakesMarktofinishmakingthebread.Weknow
thatheneedstoletitrisefor120minutestwice,sothat’s240minutes.Then,heneedstospend10minuteskneadingit
and30minutesbakingit.So,intotal,itwilltakeMark240+10+30=280minutestofinishmakingthebread.
15 Answer:280---
16
17 ---
18
19 Question:Benhas$2000forhisbusinessoperationscosts.Heordersgoodsfromhissupplierandwritesthemachequefor
$600.Hisdebtorpayshim$800fromthepurchasestheyhadmadeoncredit.Mr.Benthendecidestodoequipmentmaintenance
andspends$1200onthewholeoperation.HowmuchmoneyisMr.Benremainingwith?
20 Reasoning: Let’s think step by step in order to find out how much money Mr. Ben is remaining with. We know that he had
$2000 to begin with, and he spent $600 on goods from his supplier, so he has $2000 - $600 = $1400 left. Then, his debtor
paid him $800, so he has $1400 + $800 = $2200. Finally, he spent $1200 on equipment maintenance, so he has $2200 - $1200
=$1000left.
21 Answer:$1000---
22
23 ---
24
25 ...severalotherdemonstrationshere...
26
27 ---
28
29 Question:
Figure 10: Shortened copy of the prompt automatically generated by DSPy for GSM8K Llama2-
13b-chatCoTprogramcompiledwithbootstrap.
31

Preprint
1 Giventhefields‘context‘,‘question‘,producethefields‘searchquery‘.
2
3 ---
4
5 Followthefollowingformat.
6
7 Context:${context}
8 Question:${question}
9 Reasoning:Let’sthinkstepbystepinorderto${producethesearchquery}.We...
10 SearchQuery:${searchquery}
11
12 ---
13
14 Context:
15 [1] Twilight (novel series) | Twilight is a series of four vampire-themed fantasy romance novels by American author
StephenieMeyer....
16 [2] Harper Connelly Mysteries | The Harper Connelly Mysteries is a series of fantasy mystery novels written by Charlaine
Harris,andfirstpublishedin2005....
17 [3] The Dark Heroine | The Dark Heroine is a series of vampire-themed fantasy romance novels written by English author
AbigailGibbs,publishedbyHarperCollinsin2012....
18
19 Question: In which year was the first of the vampire-themed fantasy romance novels for which The Twilight Saga: The
OfficialIllustratedGuideservesasaspin-offencyclopedicreferencebookfirstpublished?
20
21 Reasoning:Let’sthinkstepbystepinordertodeterminetheyearthefirstofthevampire-themedfantasyromancenovels
wasfirstpublished....
22
23 SearchQuery:Whenwasthefirstofthevampire-themedfantasyromancenovelspublished?
24
25 ---
26
27 Context:
28 [1] The Victorians | The Victorians - Their Story In Pictures is a 2009 British documentary series which focuses on
Victorianartandculture....
29 [2]TheCaxtons|TheCaxtons:AFamilyPictureisan1849VictoriannovelbyEdwardBulwer-Lyttonthatwaspopularinits
time.
30 [3] Victorian (comics) | The Victorian is a 25-issue comic book series published by Penny-Farthing Press and starting in
1999....
31
32 Question:TheVictorians-TheirStoryInPicturesisadocumentaryserieswrittenbyanauthorborninwhatyear?
33
34 Reasoning: Let’s think step by step in order to produce the search query. We know that the documentary series is about
Victorianartandculture,anditwaswrittenandpresentedbyJeremyPaxman.Therefore,weneedtofindtheyearinwhich
JeremyPaxmanwasborn.
35
36 SearchQuery:JeremyPaxmanbirthyear
37
38 ---
39
40
41 Context:
Figure11: ShortenedcopyofthepromptautomaticallygeneratedbyDSPyforHotPotQALlama2-
13b-chatmulti-hopprogram(generatingsecondhopquery)compiledwithbootstrap.
32
