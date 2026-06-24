PublishedasaconferencepaperatICLR2023
SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT
REASONING IN LANGUAGE MODELS
XuezhiWang†‡ JasonWei† DaleSchuurmans† QuocLe† EdH.Chi†
SharanNarang† AakankshaChowdhery† DennyZhou†§
†GoogleResearch,BrainTeam
‡xuezhiw@google.com,§dennyzhou@google.com
ABSTRACT
Chain-of-thoughtpromptingcombinedwithpre-trainedlargelanguagemodelshas
achievedencouragingresultsoncomplexreasoningtasks.Inthispaper,wepropose
anewdecodingstrategy,self-consistency,toreplacethenaivegreedydecoding
usedinchain-of-thoughtprompting. Itfirstsamplesadiversesetofreasoningpaths
insteadofonlytakingthegreedyone,andthenselectsthemostconsistentanswer
bymarginalizingoutthesampledreasoningpaths. Self-consistencyleveragesthe
intuitionthatacomplexreasoningproblemtypicallyadmitsmultipledifferentways
ofthinkingleadingtoitsuniquecorrectanswer. Ourextensiveempiricalevaluation
showsthatself-consistencybooststheperformanceofchain-of-thoughtprompting
withastrikingmarginonarangeofpopulararithmeticandcommonsensereasoning
benchmarks,includingGSM8K(+17.9%),SVAMP(+11.0%),AQuA(+12.2%),
StrategyQA(+6.4%)andARC-challenge(+3.9%).
1 INTRODUCTION
AlthoughlanguagemodelshavedemonstratedremarkablesuccessacrossarangeofNLPtasks,their
abilitytodemonstratereasoningisoftenseenasalimitation,whichcannotbeovercomesolelyby
increasingmodelscale(Raeetal.,2021;BIG-benchcollaboration,2021,interalia). Inaneffort
toaddressthisshortcoming, Weietal.(2022)haveproposedchain-of-thoughtprompting, where
a language model is prompted to generate a series of short sentences that mimic the reasoning
processapersonmightemployinsolvingatask. Forexample,giventhequestion“Ifthereare3
cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?”, instead
ofdirectlyrespondingwith“5”,alanguagemodelwouldbepromptedtorespondwiththeentire
chain-of-thought: “Thereare3carsintheparkinglotalready. 2morearrive. Nowthereare3+
2=5cars. Theansweris5.”. Ithasbeenobservedthatchain-of-thoughtpromptingsignificantly
improvesmodelperformanceacrossavarietyofmulti-stepreasoningtasks(Weietal.,2022).
Inthispaper,weintroduceanoveldecodingstrategycalledself-consistencytoreplacethegreedy
decoding strategy used in chain-of-thought prompting (Wei et al., 2022), that further improves
languagemodels’reasoningperformancebyasignificantmargin. Self-consistencyleveragesthe
intuitionthatcomplexreasoningtaskstypicallyadmitmultiplereasoningpathsthatreachacorrect
answer(Stanovich&West,2000). Themorethatdeliberatethinkingandanalysisisrequiredfora
problem(Evans,2010),thegreaterthediversityofreasoningpathsthatcanrecovertheanswer.
Figure1illustratestheself-consistencymethodwithanexample. Wefirstpromptthelanguagemodel
withchain-of-thoughtprompting,theninsteadofgreedilydecodingtheoptimalreasoningpath,we
proposea“sample-and-marginalize”decodingprocedure: wefirstsamplefromthelanguagemodel’s
decodertogenerateadiversesetofreasoningpaths;eachreasoningpathmightleadtoadifferent
finalanswer,sowedeterminetheoptimalanswerbymarginalizingoutthesampledreasoningpaths
to find the most consistent answer in the final answer set. Such an approach is analogous to the
humanexperiencethatifmultipledifferentwaysofthinkingleadtothesameanswer,onehasgreater
confidencethatthefinalansweriscorrect. Comparedtootherdecodingmethods,self-consistency
avoids the repetitiveness and local-optimality that plague greedy decoding, while mitigating the
stochasticityofasinglesampledgeneration.
1
3202
raM
7
]LC.sc[
4v17111.3022:viXra

PublishedasaconferencepaperatICLR2023
Greedy decode
This means she uses 3 + 4 = 7 eggs every day.
|     |     | Language  | She sells the remainder for $2 per egg, so in  |     |
| --- | --- | --------- | ---------------------------------------------- | --- |
total she sells 7 * $2 = $14 per day.  The answer is $14.
model
The answer is $14.
Marginalize out reasoning paths
Sample a diverse set of
|                                        |     |     | reasoning paths              | to aggregate final answers |
| -------------------------------------- | --- | --- | ---------------------------- | -------------------------- |
| Q: If there are 3 cars in the parking  |     |     | She has 16 - 3 - 4 = 9 eggs  |                            |
| lot and 2 more cars arrive, how many   |     |     | left. So she makes $2 * 9 =  | The answer is $18.         |
| cars are in the parking lot?           |     |     | $18 per day.                 |                            |
A: There are 3 cars in the parking lot
already. 2 more arrive. Now there are
| 3 + 2 = 5 cars. The answer is 5. |                                              |                | This means she she sells the     |                    |
| -------------------------------- | -------------------------------------------- | -------------- | -------------------------------- | ------------------ |
|                                  |                                              |                | remainder for $2 * (16 - 4 - 3)  | The answer is $26. |
| …                                |                                              |                | = $26 per day.                   |                    |
| Q :  J a n e t’ s  d u           | c k s  l a y  1 6   e g g s   p e r  d a y.  | La ng u a g e  |                                  |                    |
Sh e   e a ts   th r e e  f o r  b r e a k f a s t  e v e r y   The answer is $18.
m o d e l
| morning and bakes muffins for her       |     |     | She eats 3 for breakfast, so    |     |
| --------------------------------------- | --- | --- | ------------------------------- | --- |
| friends every day with four. She sells  |     |     | she has 16 - 3 = 13 left. Then  |     |
the remainder for $2 per egg. How
|                               |     |     | she bakes muffins, so she     | The answer is $18. |
| ----------------------------- | --- | --- | ----------------------------- | ------------------ |
| much does she make every day? |     |     | has 13 - 4 = 9 eggs left. So  |                    |
A:
she has 9 eggs * $2 = $18.
Figure 1: The self-consistency method contains three steps: (1) prompt a language model using
chain-of-thought(CoT)prompting;(2)replacethe“greedydecode”inCoTpromptingbysampling
fromthelanguagemodel’sdecodertogenerateadiversesetofreasoningpaths;and(3)marginalize
outthereasoningpathsandaggregatebychoosingthemostconsistentanswerinthefinalanswerset.
Self-consistencyisfarsimplerthanpriorapproachesthateithertrainanadditionalverifier(Cobbe
etal.,2021)ortrainare-rankergivenadditionalhumanannotationstoimprovegenerationquality
(Thoppilanetal.,2022). Instead,self-consistencyisentirelyunsupervised,worksoff-the-shelfwith
pre-trainedlanguagemodels,requiresnoadditionalhumanannotation,andavoidsanyadditional
training, auxiliary models or fine-tuning. Self-consistency also differs from a typical ensemble
approachwheremultiplemodelsaretrainedandtheoutputsfromeachmodelareaggregated,itacts
morelikea“self-ensemble”thatworksontopofasinglelanguagemodel.
Weevaluateself-consistencyonawiderangeofarithmeticandcommonsensereasoningtasksover
fourlanguagemodelswithvaryingscales: thepublicUL2-20B(Tayetal.,2022)andGPT-3-175B
(Brown et al., 2020), and two densely-activated decoder-only language models: LaMDA-137B
(Thoppilanetal.,2022)andPaLM-540B(Chowdheryetal.,2022). Onallfourlanguagemodels,
self-consistencyimprovesoverchain-of-thoughtpromptingbyastrikingmarginacrossalltasks. In
particular,whenusedwithPaLM-540BorGPT-3,self-consistencyachievesnewstate-of-the-artlevels
ofperformanceacrossarithmeticreasoningtasks,includingGSM8K(Cobbeetal.,2021)(+17.9%
absoluteaccuracygains),SVAMP(Pateletal.,2021)(+11.0%),AQuA(Lingetal.,2017)(+12.2%),
andacrosscommonsensereasoningtaskssuchasStrategyQA(Gevaetal.,2021)(+6.4%)andARC-
challenge(Clark etal., 2018)(+3.9%). Inadditional experiments, we show self-consistencycan
robustlyboostperformanceonNLPtaskswhereaddingachain-of-thoughtmighthurtperformance
comparedtostandardprompting(Ye&Durrett,2022). Wealsoshowself-consistencysignificantly
outperformssample-and-rank,beamsearch,ensemble-basedapproaches,andisrobusttosampling
strategiesandimperfectprompts.
| 2 SELF-CONSISTENCY |     | DIVERSE | REASONING | PATHS |
| ------------------ | --- | ------- | --------- | ----- |
OVER
Asalientaspectofhumanityisthatpeoplethinkdifferently. Itisnaturaltosupposethatintasks
requiringdeliberatethinking,therearelikelyseveralwaystoattacktheproblem. Weproposethat
suchaprocesscanbesimulatedinlanguagemodelsviasamplingfromthelanguagemodel’sdecoder.
For instance, as shown in Figure 1, a model can generate several plausible responses to a math
questionthatallarriveatthesamecorrectanswer(Outputs1and3). Sincelanguagemodelsarenot
perfectreasoners,themodelmightalsoproduceanincorrectreasoningpathormakeamistakein
oneofthereasoningsteps(e.g.,inOutput2),butsuchsolutionsarelesslikelytoarriveatthesame
answer. Thatis,wehypothesizethatcorrectreasoningprocesses,eveniftheyarediverse,tendto
havegreateragreementintheirfinalanswerthanincorrectprocesses.
Weleveragethisintuition byproposing thefollowing self-consistency method. First, alanguage
modelispromptedwithasetofmanuallywrittenchain-of-thoughtexemplars(Weietal.,2022). Next,
2

PublishedasaconferencepaperatICLR2023
GSM8K MultiArith AQuA SVAMP CSQA ARC-c
Greedydecode 56.5 94.7 35.8 79.0 79.0 85.2
Weightedavg(unnormalized) 56.3±0.0 90.5±0.0 35.8±0.0 73.0±0.0 74.8±0.0 82.3±0.0
Weightedavg(normalized) 22.1±0.0 59.7±0.0 15.7±0.0 40.5±0.0 52.1±0.0 51.7±0.0
Weightedsum(unnormalized) 59.9±0.0 92.2±0.0 38.2±0.0 76.2±0.0 76.2±0.0 83.5±0.0
Weightedsum(normalized) 74.1±0.0 99.3±0.0 48.0±0.0 86.8±0.0 80.7±0.0 88.7±0.0
Unweightedsum(majorityvote) 74.4±0.1 99.3±0.0 48.3±0.5 86.6±0.1 80.7±0.1 88.7±0.1
Table1: AccuracycomparisonofdifferentansweraggregationstrategiesonPaLM-540B.
wesampleasetofcandidateoutputsfromthelanguagemodel’sdecoder,generatingadiversesetof
candidatereasoningpaths. Self-consistencyiscompatiblewithmostexistingsamplingalgorithms,
includingtemperaturesampling(Ackleyetal.,1985;Ficler&Goldberg,2017),top-ksampling(Fan
etal.,2018;Holtzmanetal.,2018;Radfordetal.,2019),andnucleussampling(Holtzmanetal.,
2020). Finally, we aggregate the answers by marginalizing out the sampled reasoning paths and
choosingtheanswerthatisthemostconsistentamongthegeneratedanswers.
In more detail, assume the generated answers a are from a fixed answer set, a ∈ A, where
i i
i = 1,...,mindexesthemcandidateoutputssampledfromthedecoder. Givenapromptanda
question,self-consistencyintroducesanadditionallatentvariabler ,whichisasequenceoftokens
i
representing the reasoning path in the i-th output, then couples the generation of (r ,a ) where
i i
r →a ,i.e.,generatingareasoningpathr isoptionalandonlyusedtoreachthefinalanswera . As
i i i i
anexample,considerOutput3fromFigure1: thefirstfewsentences“Sheeats3forbreakfast...So
shehas9eggs*$2=$18.” constitutesr ,whiletheanswer18fromthelastsentence,“Theanswer
i
is$18”,isparsedasa .1 Aftersamplingmultiple(r ,a )fromthemodel’sdecoder,self-consistency
i i i
appliesamarginalizationoverr bytakingamajorityvoteovera ,i.e.,argmax (cid:80)m 1(a =a),
i i a i=1 i
oraswedefinedasthemost“consistent”answeramongthefinalanswerset.
In Table 1, we show the test accuracy over a set of reasoning tasks by using different answer
aggregationstrategies. Inadditiontomajorityvote,onecanalsoweighteach(r ,a )byP(r ,a |
i i i i
prompt,question)whenaggregatingtheanswers. NotetocomputeP(r ,a |prompt,question),we
i i
caneithertaketheunnormalizedprobabilityofthemodelgenerating(r ,a )given(prompt,question),
i i
orwecannormalizetheconditionalprobabilitybytheoutputlength(Brownetal.,2020),i.e.,
P(r i ,a i |prompt,question)=expK 1 (cid:80)K k=1 logP(tk|prompt,question,t1,...,tk−1), (1)
wherelogP(t |prompt,question,t ,...,t )isthelogprobabilityofgeneratingthek-thtoken
k 1 k−1
t in (r ,a ) conditioned on the previous tokens, and K is the total number of tokens in (r ,a ).
k i i i i
InTable1,weshowthattakingthe“unweightedsum”,i.e.,takingamajorityvotedirectlyovera
i
yieldsaverysimilaraccuracyasaggregatingusingthe“normalizedweightedsum”. Wetookacloser
lookatthemodel’soutputprobabilitiesandfoundthisisbecauseforeach(r ,a ),thenormalized
i i
conditionalprobabilitiesP(r ,a |prompt,question)arequiteclosetoeachother,i.e.,thelanguage
i i
modelregardsthosegenerationsas“similarlylikely”.2 Additionally,whenaggregatingtheanswers,
the results in Table 1 show that the “normalized” weighted sum (i.e., Equation 1) yields a much
higheraccuracycomparedtoitsunnormalizedcounterpart. Forcompleteness,inTable1wealso
reporttheresultsbytakinga“weightedaverage”,i.e.,eachagetsascoreofitsweightedsumdivided
by (cid:80)m 1(a =a),whichresultsinamuchworseperformance.
i=1 i
Self-consistency explores an interesting space between open-ended text generation and optimal
textgenerationwithafixedanswer. Reasoningtaskstypicallyhavefixedanswers, whichiswhy
researchershavegenerallyconsideredgreedydecodingapproaches(Radfordetal.,2019;Weietal.,
2022;Chowdheryetal.,2022). However,wehavefoundthatevenwhenthedesiredanswerisfixed,
introducing diversity in the reasoning processes can be highly beneficial; therefore we leverage
1Theparseristaskdependent.Forarithmeticreasoning,weparsethefirstnumericalpartasthefinalanswer
afterthemodelgenerates“Theansweris”.Forcommonsensereasoning,weparsethefullstringanswerasthe
finalanswerafterthemodelgenerates“Theansweris”. Mostgeneratedoutputshaveaconsistentformatof
“{Reasoningpaths}.TheanswerisX.”ifwepromptthelanguagemodelinthisformat.
2Thisalsomeansthatthelanguagemodelisnotwellcalibratedandthuscannotdistinguishwellbetween
correctsolutionsandwrongsolutions,whichalsoexplainswhyadditionalre-rankersweretrainedtobetterjudge
thequalityofthesolutionsinpreviouswork(Cobbeetal.,2021;Thoppilanetal.,2022).
3

PublishedasaconferencepaperatICLR2023
sampling,ascommonlyusedforopen-endedtextgeneration(Radfordetal.,2019;Brownetal.,2020;
Thoppilanetal.,2022),toachievethisgoal. Oneshouldnotethatself-consistencycanbeapplied
onlytoproblemswherethefinalanswerisfromafixedanswerset,butinprinciplethisapproachcan
beextendedtoopen-textgenerationproblemsifagoodmetricofconsistencycanbedefinedbetween
multiplegenerations,e.g.,whethertwoanswersagreeorcontradicteachother.
3 EXPERIMENTS
Weconductedaseriesofexperimentstocomparetheproposedself-consistencymethodwithexisting
approachesonarangeofreasoningbenchmarks. Wefindthatself-consistencyrobustlyimproves
reasoningaccuracyforeverylanguagemodelconsidered,spanningawiderangeofmodelscales.
3.1 EXPERIMENTSETUP
Tasksanddatasets. Weevaluateself-consistencyonthefollowingreasoningbenchmarks.3
• Arithmeticreasoning. Forthesetasks,weusedtheMathWordProblemRepository(Koncel-
Kedziorskietal.,2016), includingAddSub(Hosseinietal.,2014), MultiArith(Roy&Roth,
2015), and ASDiv (Miao et al., 2020). We also included AQUA-RAT (Ling et al., 2017), a
recentlypublishedbenchmarkofgrade-school-mathproblems(GSM8K;Cobbeetal.,2021),
andachallengedatasetovermathwordproblems(SVAMP;Pateletal.,2021).
• Commonsensereasoning. Forthesetasks, weusedCommonsenseQA(Talmoretal.,2019),
StrategyQA(Gevaetal.,2021),andtheAI2ReasoningChallenge(ARC)(Clarketal.,2018).
• SymbolicReasoning. Weevaluatetwosymbolicreasoningtasks: lastletterconcatenation(e.g.,
theinputis“ElonMusk”andtheoutputshouldbe“nk”),andCoinflip(e.g.,acoinisheads-up,
afterafewflipsisthecoinstillheads-up?) fromWeietal.(2022).
Languagemodelsandprompts. Weevaluateself-consistencyoverfourtransformer-basedlan-
guagemodelswithvaryingscales:
• UL2(Tayetal.,2022)isanencoder-decodermodeltrainedonamixtureofdenoiserswith20-
billionparameters. UL2iscompletelyopen-sourced4 andhassimilarorbetterperformancethan
GPT-3onzero-shotSuperGLUE,withonly20Bparametersandthusismorecompute-friendly;
• GPT-3(Brownetal.,2020)with175-billionparameters.Weusetwopublicenginescode-davinci-
001andcode-davinci-002fromtheCodexseries(Chenetal.,2021)toaidreproducibility;5
• LaMDA-137B(Thoppilanetal.,2022)isadenseleft-to-right,decoder-onlylanguagemodelwith
137-billionparameters,pre-trainedonamixtureofwebdocuments,dialogdataandWikipedia;
• PaLM-540B(Chowdheryetal.,2022)isadenseleft-to-right,decoder-onlylanguagemodelwith
540-billionparameters,pre-trainedonahighqualitycorpusof780billiontokenswithfiltered
webpages,books,Wikipedia,newsarticles,sourcecode,andsocialmediaconversations.
We perform all experiments in the few-shot setting, without training or fine-tuning the language
models. ForafaircomparisonweusethesamepromptsasinWeietal.(2022): forallarithmetic
reasoning tasks we use the same set of 8 manually written exemplars; for each commonsense
reasoningtask,4-7exemplarsarerandomlychosenfromthetrainingsetwithmanuallycomposed
chain-of-thoughtprompts.6 FulldetailsonthepromptsusedaregiveninAppendixA.3.
Sampling scheme. To sample diverse reasoning paths, we followed similar settings to those
suggestedinRadfordetal.(2019);Holtzmanetal.(2020)foropen-textgeneration. Inparticular,for
UL2-20BandLaMDA-137BweappliedtemperaturesamplingwithT =0.5andtruncatedatthe
top-k(k =40)tokenswiththehighestprobability,forPaLM-540BweappliedT =0.7,k =40,and
forGPT-3weuseT =0.7withouttop-ktruncation. WeprovideanablationstudyinSection3.5to
showthatself-consistencyisgenerallyrobusttosamplingstrategiesandparameters.
3Bydefaultweusethetestsplitforalldatasetsifthelabelsareavailableforevaluation.ForCommonsenseQA
we use the dev split; for StrategyQA we use the question-only set from BIG-bench collaboration (2021):
https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/strategyqa.
4Modelcheckpointsathttps://github.com/google-research/google-research/tree/master/ul2.
5PublicAPIavailableathttps://openai.com/api/.
6Self-consistencyisrobusttodifferentsetsofpromptsandweprovideastudyinAppendixA.1.2.
4

PublishedasaconferencepaperatICLR2023
3.2 MAINRESULTS
We report the results of self-consistency averaged over 10 runs, where we sampled 40 outputs
independently from the decoder in each run. The baseline we compare to is chain-of-thought
promptingwithgreedydecoding(Weietal.,2022),referredtoasCoT-prompting,whichhasbeen
previouslyusedfordecodinginlargelanguagemodels(Chowdheryetal.,2022).
ArithmeticReasoning TheresultsareshowninTable2.7 Self-consistencyimprovesthearithmetic
reasoningperformanceoverallfourlanguagemodelssignificantlyoverchain-of-thoughtprompting.
Moresurprisingly,thegainsbecomemoresignificantwhenthelanguagemodel’sscaleincreases,
e.g., wesee+3%-6%absoluteaccuracyimprovementoverUL2-20Bbut+9%-23%forLaMDA-
137BandGPT-3. Forlargermodelsthatalreadyachievehighaccuracyonmosttasks(e.g.,GPT-3
and PaLM-540B), self-consistency still contributes significant additional gains with +12%-18%
absoluteaccuracyontaskslikeAQuAandGSM8K,and+7%-11%onSVAMPandASDiv. With
self-consistency,weachievenewstate-of-the-artresultsonalmostalltasks: despitethefactthatself-
consistencyisunsupervisedandtask-agnostic,theseresultscomparefavorablytoexistingapproaches
thatrequiretask-specifictraining,orfine-tuningwiththousandsofexamples(e.g.,onGSM8K).
| Method | AddSub MultiArith | ASDiv AQuA  | SVAMP GSM8K   |
| ------ | ----------------- | ----------- | ------------- |
|        | 94.9a 60.5a       | 75.3b 37.9c | 57.4d 35e/55g |
PreviousSoTA
| CoT-prompting | 18.2 10.7 | 16.9 23.6 | 12.6 4.1 |
| ------------- | --------- | --------- | -------- |
UL2-20B
| Self-consistency | 24.8(+6.6) 15.0(+4.3) | 21.5(+4.6) 26.9(+3.3) | 19.4(+6.8) 7.3(+3.2) |
| ---------------- | --------------------- | --------------------- | -------------------- |
| CoT-prompting    | 52.9 51.8             | 49.0 17.7             | 38.9 17.1            |
LaMDA-137B
| Self-consistency | 63.5(+10.6) 75.7(+23.9) | 58.2(+9.2) 26.8(+9.1) | 53.3(+14.4) 27.7(+10.6) |
| ---------------- | ----------------------- | --------------------- | ----------------------- |
| CoT-prompting    | 91.9 94.7               | 74.0 35.8             | 79.0 56.5               |
PaLM-540B
| Self-consistency    | 93.7(+1.8) 99.3(+4.6) | 81.9(+7.9) 48.3(+12.5) | 86.6(+7.6) 74.4(+17.9) |
| ------------------- | --------------------- | ---------------------- | ---------------------- |
| GPT-3 CoT-prompting | 57.2 59.5             | 52.7 18.9              | 39.8 14.6              |
Code-davinci-001 Self-consistency 67.8(+10.6) 82.7(+23.2) 61.9(+9.2) 25.6(+6.7) 54.5(+14.7) 23.4(+8.8)
| GPT-3 CoT-prompting | 89.4 96.2 | 80.1 39.8 | 75.8 60.1 |
| ------------------- | --------- | --------- | --------- |
Code-davinci-002 Self-consistency 91.6(+2.2) 100.0(+3.8) 87.8(+7.6) 52.0(+12.2) 86.8(+11.0) 78.0(+17.9)
Table2: Arithmeticreasoningaccuracybyself-consistencycomparedtochain-of-thoughtprompting
(Weietal.,2022). ThepreviousSoTAbaselinesareobtainedfrom: a: RelevanceandLCAoperation
classifier (Roy & Roth, 2015), b: Lan et al. (2021), c: Amini et al. (2019), d: Pi et al. (2022), e:
GPT-3175Bfinetunedwith7.5kexamples(Cobbeetal.,2021),g: GPT-3175Bfinetunedplusan
additional175Bverifier(Cobbeetal.,2021). Thebestperformanceforeachtaskisshowninbold.
| Method        | CSQA StrategyQA | ARC-e ARC-c | Letter(4) Coinflip(4) |
| ------------- | --------------- | ----------- | --------------------- |
| PreviousSoTA  | 91.2a 73.9b     | 86.4c 75.0c | N/A N/A               |
| CoT-prompting | 51.4 53.3       | 61.6 42.9   | 0.0 50.4              |
UL2-20B Self-consistency 55.7(+4.3) 54.9(+1.6) 69.8(+8.2) 49.5(+6.8) 0.0(+0.0) 50.5(+0.1)
| CoT-prompting | 57.9 65.4 | 75.3 55.1 | 8.2 72.4 |
| ------------- | --------- | --------- | -------- |
LaMDA-137B
| Self-consistency | 63.1(+5.2) 67.8(+2.4) | 79.3(+4.0) 59.8(+4.7) | 8.2(+0.0) 73.5(+1.1) |
| ---------------- | --------------------- | --------------------- | -------------------- |
| CoT-prompting    | 79.0 75.3             | 95.3 85.2             | 65.8 88.2            |
PaLM-540B
| Self-consistency    | 80.7(+1.7) 81.6(+6.3) | 96.4(+1.1) 88.7(+3.5) | 70.8(+5.0) 91.2(+3.0) |
| ------------------- | --------------------- | --------------------- | --------------------- |
| GPT-3 CoT-prompting | 46.6 56.7             | 63.1 43.1             | 7.8 71.4              |
Code-davinci-001 Self-consistency 54.9(+8.3) 61.7(+5.0) 72.1(+9.0) 53.7(+10.6) 10.0(+2.2) 75.9(+4.5)
| GPT-3 CoT-prompting | 79.0 73.4 | 94.0 83.6 | 70.4 99.0 |
| ------------------- | --------- | --------- | --------- |
Code-davinci-002 Self-consistency 81.5(+2.5) 79.8(+6.4) 96.0(+2.0) 87.5(+3.9) 73.4(+3.0) 99.5(+0.5)
Table3: Commonsenseandsymbolicreasoningaccuracybyself-consistencycomparedtochain-
of-thought prompting (Wei et al., 2022). The previous SoTA baselines are obtained from: a:
DeBERTaV3-large + KEAR (Xu et al., 2021b), b: Chowdhery et al. (2022), c: UnifiedQA-FT
| (Khashabietal.,2020). Thebestperformanceforeachtaskisshowninbold. |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- |
7Thestandarddeviationofself-consistencyis≤0.5foralltasksandisthusomittedinthetable.Pleaserefer
toFigure2,Figure7and8forthestandarddeviationsundervaryingnumbersofsampledpaths.
5

PublishedasaconferencepaperatICLR2023
CommonsenseandSymbolicReasoning Table3showstheresultsoncommonsenseandsymbolic
reasoningtasks. Similarly,self-consistencyyieldslargegainsacrossallfourlanguagemodels,and
obtainedSoTAresultson5outof6tasks. Forsymbolicreasoning,wetesttheout-of-distribution
(OOD)settingwheretheinputpromptcontainsexamplesof2-lettersor2-flipsbutwetestexamples
of4-lettersand4-flips(thissettingismorechallengingasPaLM-540BorGPT-3canalreadyachieve
perfectin-distributionaccuracy). InthischallengingOODsetting,thegainofself-consistencyisstill
quitesignificantcomparedtoCoT-promptingwithsufficientmodelsizes.
To show the effect of the number of sampled reasoning paths, we plot the accuracy (mean and
standarddeviationover10runs)withrespecttovaryingnumbersofsampledpaths(1,5,10,20,40)
inFigure2. Theresultsshowthatsamplingahighernumber(e.g.,40)ofreasoningpathsleadstoa
consistentlybetterperformance,furtheremphasizingtheimportanceofintroducingdiversityinthe
reasoningpaths. InTable4,weshowself-consistencyyieldsarichersetofreasoningpathscompared
togreedydecodingwithafewexamplequestionsfromtwotasks.
|              | MultiArith |     | SVAMP |     | Commonsense QA |     | ARC (Challenge)      |                                 |
| ------------ | ---------- | --- | ----- | --- | -------------- | --- | -------------------- | ------------------------------- |
| 75           |            | 54  |       |     |                | 60  |                      |                                 |
| )%( ycaruccA |            | 51  |       | 62  |                |     |                      |                                 |
| 70           |            | 48  |       |     |                | 58  |                      |                                 |
| 65           |            | 45  |       | 60  |                | 56  |                      |                                 |
| 60           |            | 42  |       | 58  |                | 54  |                      |                                 |
| 55           |            | 3 9 |       |     |                | 5 2 | G re e d y  D e c    | o d e  ( S in g l e - p a t h ) |
| 50           |            | 3 6 |       | 56  |                |     | Se lf  C o n si s te | n c y   (M u l t i- p a t h )   |
|              |            | 33  |       |     |                | 5 0 |                      |                                 |
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths
Figure2: Self-consistency(blue)significantlyimprovesaccuracyoverCoT-promptingwithgreedy
decoding(orange)acrossarithmeticandcommonsensereasoningtasks,overLaMDA-137B.Sampling
ahighernumberofdiversereasoningpathsconsistentlyimprovesreasoningaccuracy.
|     | GSM8K |     |     |     |     | StrategyQA |     |     |
| --- | ----- | --- | --- | --- | --- | ---------- | --- | --- |
Question Henrymadetwostopsduringhis60-milebiketrip. Hefirststoppedafter20 Yesorno:IsAlbany,Georgiathemostpopulous
|     | miles.Hissecondstopwas15milesbeforetheendofthetrip.Howmanymiles |     |     |     |     | USAlbany? |     |     |
| --- | --------------------------------------------------------------- | --- | --- | --- | --- | --------- | --- | --- |
didhetravelbetweenhisfirstandsecondstops?
Greedy Hetraveled60milesintotal.Hestoppedafter20miles,sohetraveled60-20 Albany, GeorgiaisthemostpopulousUSAl-
Decode =40milesbetweenthefirstandsecondstops.Theansweris40. bany.Thus,theanswerisyes.
Sampled Henrytravelledatotalof60miles. Hisfirststopwas20milesin, andhis ThemostpopulousUSAlbanyisAlbany,New
Path1 secondstopwas15milesbeforetheend.Sobetweenhisfirstandsecondstops York. Thus, Albany, Georgiaisnotthemost
hetravelled60-20-15=25miles.Theansweris25. populousUSAlbany.Sotheanswerisno.
Sampled Hemadetwostopsduringa60-miletrip. Thefirstwas20milesintothetrip. Albany, Georgia has a population of about
Path2 Thesecondwas15milesbeforetheendofthetrip.Thismeansthesecondstop 88,000. Albany,NewYorkhasapopulationof
was60-15=45milesintothetrip.Sincehemadethestopsinorder,thesecond about95,000.Thus,Albany,Georgiaisnotthe
stopmusthavebeen45-20=25milesafterthefirststop.Theansweris25. mostpopulousUSAlbany.Sotheanswerisno.
Table4: Exampleswhereself-consistencyhelpsrepairtheerrorsovergreedydecode,onPaLM-540B.
Twosampledreasoningpathsthatareconsistentwiththegroundtruthareshown.
3.3 SELF-CONSISTENCYHELPSWHENCHAIN-OF-THOUGHTHURTSPERFORMANCE
Ye & Durrett (2022) show that sometimes chain-of-thought prompting could hurt performance
comparedtostandardpromptinginfew-shotin-contextlearning. Hereweperformastudyusing
self-consistencytoseeifitcanhelpfillinthegap,overasetofcommonNLPtasks,including(1)
Closed-BookQuestionAnswering: BoolQ(Clarketal.,2019),HotpotQA(Yangetal.,2018),and
(2)NaturalLanguageInference: e-SNLI(Camburuetal.,2018),ANLI(Nieetal.,2020)andRTE
(Daganetal.,2005;Bar-Haimetal.,2006;Giampiccoloetal.,2007;Bentivoglietal.,2009).
TheresultsoverPaLM-540BareshowninTable5. Forsometasks(e.g.,ANLI-R1,e-SNLI,RTE),
addingchain-of-thoughtdoeshurtperformancecomparedtostandardprompting(Brownetal.,2020),
butself-consistencyisabletorobustlyboosttheperformanceandoutperformstandardprompting,
makingitareliablewaytoaddrationalesinfew-shotin-contextlearningforcommonNLPtasks.
|     |     |     | ANLIR1/R2/R3 |     | e-SNLI RTE | BoolQ | HotpotQA(EM/F1) |     |
| --- | --- | --- | ------------ | --- | ---------- | ----- | --------------- | --- |
Standard-prompting(no-rationale) 69.1/55.8/55.8 85.8 84.8 71.3 27.1/36.8
CoT-prompting(Weietal.,2022) 68.8/58.9/60.6 81.0 79.1 74.2 28.9/39.8
|     | Self-consistency |     | 78.5/64.5/63.4 |     | 88.4 86.3 | 78.4 | 33.8/44.6 |     |
| --- | ---------------- | --- | -------------- | --- | --------- | ---- | --------- | --- |
Table5: CompareStandard/CoTpromptingwithself-consistencyoncommonNLPtasks.
6

PublishedasaconferencepaperatICLR2023
3.4 COMPARETOOTHEREXISTINGAPPROACHES
We conduct a set of additional studies and show that self-consistency significantly outperforms
existingmethodsincludingsample-and-rank,beamsearch,andensemble-basedapproaches.
ComparisontoSample-and-Rank Onecommonlyusedapproachtoimprovegenerationqualityis
sample-and-rank,wheremultiplesequencesaresampledfromthedecoderandthenrankedaccording
toeachsequence’slogprobability(Adiwardanaetal.,2020). Wecompareself-consistencywith
sample-and-rankonGPT-3code-davinci-001,bysamplingthesamenumberofsequencesfromthe
decoderasself-consistencyandtakingthefinalanswerfromthetop-rankedsequence. Theresultsare
showninFigure3. Whilesample-and-rankdoesimprovetheaccuracywithadditionallysampled
sequencesandranking,thegainismuchsmallercomparedtoself-consistency.
|              | GSM8K |                 |     | MultiArith |              |     | ARC (Challenge) |     |
| ------------ | ----- | --------------- | --- | ---------- | ------------ | --- | --------------- | --- |
| 24           |       |                 |     |            |              | 55  |                 |     |
| )%( ycaruccA |       | )%( ycaruccA 80 |     |            | )%( ycaruccA |     |                 |     |
| 22           |       |                 |     |            |              | 50  |                 |     |
| 20           |       | 75              |     |            |              |     |                 |     |
|              |       | 70              |     |            |              | 45  |                 |     |
18
|     |     | 65  |     |     |     | 40  |                               |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- |
| 16  |     | 60  |     |     |     |     | Self Consistency (Multi-path) |     |
| 14  |     | 55  |     |     |     | 35  | Sample & Rank (Multi-path)    |     |
| 12  |     | 50  |     |     |     |     | Greedy Decode (Single-path)   |     |
30
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths
Figure3: Self-consistencysignificantlyoutperformssample-and-rankwiththesame#ofsamples.
ComparisontoBeamSearch InTable6,wecompareself-consistencywithbeamsearchdecoding
ontheUL2-20Bmodel. Forafaircomparisonwereporttheaccuracyunderthesamenumberof
beamsandreasoningpaths. Onbothtasksself-consistencyoutperformsbeamsearchsignificantly.
Noteself-consistencycanalsoadoptbeamsearchtodecodeeachreasoningpath(resultsareshown
as“Self-consistencyusingbeamsearch”),butitsperformanceisworsecomparedtoself-consistency
withsampling. Thereasonisthatbeamsearchyieldsalowerdiversityintheoutputs(Li&Jurafsky,
2016),whileinself-consistencythediversityofthereasoningpathsisthekeytoabetterperformance.
|     | Beamsize/Self-consistencypaths |     |     | 1    | 5    | 10   | 20   | 40   |
| --- | ------------------------------ | --- | --- | ---- | ---- | ---- | ---- | ---- |
|     | Beamsearchdecoding(topbeam)    |     |     | 23.6 | 19.3 | 16.1 | 15.0 | 10.2 |
AQuA Self-consistencyusingbeamsearch 23.6 19.8±0.3 21.2±0.7 24.6±0.4 24.2±0.5
|     | Self-consistencyusingsampling |     |     | 19.7±2.5 24.9±2.6 |      | 25.3±1.8 | 26.7±1.0 | 26.9±0.5 |
| --- | ----------------------------- | --- | --- | ----------------- | ---- | -------- | -------- | -------- |
|     | Beamsearchdecoding(topbeam)   |     |     | 10.7              | 12.0 | 11.3     | 11.0     | 10.5     |
MultiArith Self-consistencyusingbeamsearch 10.7 11.8±0.0 11.4±0.1 12.3±0.1 10.8±0.1
|     | Self-consistencyusingsampling |     |     | 9.5±1.2 11.3±1.2 |     | 12.3±0.8 | 13.7±0.9 | 14.7±0.3 |
| --- | ----------------------------- | --- | --- | ---------------- | --- | -------- | -------- | -------- |
Table6: Compareself-consistencywithbeamsearchdecodingontheUL2-20Bmodel.
ComparisontoEnsemble-basedApproaches Wefurthercompareself-consistencytoensemble-
basedmethodsforfew-shotlearning. Inparticular,weconsiderensemblingby: (1)promptorder
permutation: we randomly permute the exemplars in the prompt 40 times to mitigate model’s
sensitivity to prompt order (Zhao et al., 2021; Lu et al., 2021); and (2) multiple sets of prompts
(Gao et al., 2021): we manually write 3 different sets of prompts. We took majority vote of the
answersfromgreedydecodinginbothapproachesasanensemble. Table7showsthatcomparedto
self-consistency,existingensemble-basedapproachesachieveamuchsmallergain.8 Inaddition,note
thatself-consistencyisdifferentfromatypicalmodel-ensembleapproach,wheremultiplemodels
aretrainedandtheiroutputsareaggregated. Self-consistencyactsmorelikea“self-ensemble”on
topofasinglelanguagemodel. Weadditionallyshowtheresultsofensemblingmultiplemodelsin
AppendixA.1.3wherethemodel-ensemblesperformmuchworsecomparedtoself-consistency.
|                    |     |     | GSM8K | MultiArith | SVAMP |      | ARC-e | ARC-c |
| ------------------ | --- | --- | ----- | ---------- | ----- | ---- | ----- | ----- |
| CoT(Weietal.,2022) |     |     | 17.1  | 51.8       |       | 38.9 | 75.3  | 55.1  |
Ensemble(3setsofprompts) 18.6±0.5 57.1±0.7 42.1±0.6 76.6±0.1 57.0±0.2
Ensemble(40promptpermutations) 19.2±0.1 60.9±0.2 42.7±0.1 76.9±0.1 57.0±0.1
Self-Consistency(40sampledpaths) 27.7±0.2 75.7±0.3 53.3±0.2 79.3±0.3 59.8±0.2
Table7: Self-consistencyoutperformsprompt-orderandmulti-promptensemblesonLaMDA-137B.
8Self-consistencyiscompatiblewithbothensembleapproachesandweshowtheresultsinAppendixA.1.4.
7

PublishedasaconferencepaperatICLR2023
3.5 ADDITIONALSTUDIES
Weconductedanumberofadditionalexperimentstoanalyzedifferentaspectsoftheself-consistency
method, including its robustness to sampling strategies and parameters, and how it works with
imperfectpromptsandnon-natural-languagereasoningpaths.
Self-Consistency is Robust to Sampling Strategies and Scaling We show self-consistency is
robusttosamplingstrategiesandparameters,byvaryingT intemperaturesampling(Ackleyetal.,
1985;Ficler&Goldberg,2017),kintop-ksampling(Fanetal.,2018;Holtzmanetal.,2018;Radford
etal.,2019),andpinnucleussampling(Holtzmanetal.,2020),overPaLM-540BinFigure4(left).
Figure4(right)showsthatself-consistencyrobustlyimprovesperformanceacrossallscalesforthe
LaMDA-137Bmodelseries. Thegainisrelativelylowerforsmallermodelsduetocertainabilities
(e.g.,arithmetic)onlyemergewhenthemodelreachesasufficientscale(Brownetal.,2020).
76
|              |     |     |     | T=0.7, k=40 |     |                 | Self Consistency |     |     |
| ------------ | --- | --- | --- | ----------- | --- | --------------- | ---------------- | --- | --- |
| )%( ycaruccA | 72  |     |     |             |     | )%( ycaruccA 25 |                  |     |     |
|              | 68  |     |     | T=0.5, k=40 |     |                 | Greedy Decode    |     |     |
20
|     | 64  |     |     | T=0.3, k=40 |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
60
|     |     |     |     | T=0.7, k=20 |     | 15  |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
56
|     | 52  |     |     | T=0.7, no top k |     | 10  |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
p=0.95
48
|     | 44  |     |     | p=0.9 |     | 5   |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Greedy Decode
|     | 0                        | 5 10 15 | 20 25 30 35 40 |     |     |                                 | 1 2 | 5 10 20 | 50 100200 |
| --- | ------------------------ | ------- | -------------- | --- | --- | ------------------------------- | --- | ------- | --------- |
|     | #Sampled Reasoning Paths |         |                |     |     | Model size (#param in billions) |     |         |           |
Figure 4: GSM8Kaccuracy. (Left) Self-consistency isrobust to various sampling strategies and
parameters. (Right)Self-consistencyimprovesperformanceacrosslanguagemodelscales.
Self-ConsistencyImprovesRobustnesstoImperfectPrompts Forfew-shotlearningwithman-
uallyconstructedprompts,humanannotatorssometimesmakeminormistakeswhencreatingthe
prompts. Wefurtherstudyifself-consistencycanhelpimprovealanguagemodel’srobustnessto
imperfectprompts.9 WeshowtheresultsinTable8: whileimperfectpromptsdecreaseaccuracywith
greedydecoding(17.1→14.9),self-consistencycanfillinthegapsandrobustlyimprovetheresults.
Additionally, we found that the consistency (in terms of % of decodes agreeing with the final
aggregatedanswer)ishighlycorrelatedwithaccuracy(Figure5,overGSM8K).Thissuggeststhat
onecanuseself-consistencytoprovideanuncertaintyestimateofthemodelinitsgeneratedsolutions.
Inotherwords,onecanuselowconsistencyasanindicatorthatthemodelhaslowconfidence;i.e.,
self-consistencyconferssomeabilityforthemodelto“knowwhenitdoesn’tknow”.
|     |     | Promptwithcorrectchain-of-thought |     |     | 17.1 |     | 100 |     |     |
| --- | --- | --------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
)%( ycaruccA
80
|     |     | Promptwithimperfectchain-of-thought |     |     | 14.9 |     |     |     |     |
| --- | --- | ----------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
LaMDA-137B
|     |     | +Self-consistency(40paths) |     |     | 23.4 |     | 60  |     |     |
| --- | --- | -------------------------- | --- | --- | ---- | --- | --- | --- | --- |
40
|     |     | Promptwithequations        |     |     | 5.0 |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | +Self-consistency(40paths) |     |     | 6.5 |     | 20  |     |     |
0
|           |     | Zero-shotCoT(Kojimaetal.,2022) |     |     | 43.0 |     |     |                 |              |
| --------- | --- | ------------------------------ | --- | --- | ---- | --- | --- | --------------- | ------------ |
| PaLM-540B |     |                                |     |     |      |     |     | 0 20            | 40 60 80 100 |
|           |     | +Self-consistency(40paths)     |     |     | 69.2 |     |     | Consistency (%) |              |
Table8:Self-consistencyworksunderimperfectprompts,equa- Figure5: Theconsistencyiscor-
tionpromptsandzero-shotchain-of-thoughtforGSM8K. relatedwithmodel’saccuracy.
Self-ConsistencyWorksforNon-Natural-LanguageReasoningPathsandZero-shotCoT We
alsotestedthegeneralityoftheself-consistencyconcepttoalternativeformsofintermediatereasoning
likeequations(e.g.,from“Thereare3carsintheparkinglotalready. 2morearrive. Nowthere
are3+2=5cars.” to“3+2=5”). TheresultsareshowninTable8(“Promptwithequations”):
self-consistencystillimprovesaccuracybygeneratingintermediateequations;however,comparedto
generatingnaturallanguagereasoningpaths,thegainissmallersincetheequationsaremuchshorter
andlessopportunityremainsforgeneratingdiversityinthedecodingprocess. Inaddition,wetested
self-consistencywithzero-shotchain-of-thought(Kojimaetal.,2022)andshowthatself-consistency
worksforzero-shotCoTaswellandimprovestheresultssignificantly(+26.2%)inTable8.
9Weusethesamepromptsasbefore,butswapallthenumbersinthereasoningpathswithrandomnumbers
exceptthefinalanswer,e.g.,from“Thereare3carsintheparkinglotalready.2morearrive.Nowthereare3+
2=5cars.”to“Thereare7carsintheparkinglotalready.6morearrive.Nowthereare7+6=5cars.”.
8

PublishedasaconferencepaperatICLR2023
4 RELATED WORK
Reasoninginlanguagemodels. LanguagemodelsareknowntostruggleinType2tasks,suchas
arithmetic,logicalandcommonsensereasoning(Evans,2010). Previousworkhasprimarilyfocused
onspecializedapproachesforimprovingreasoning(Andoretal.,2019;Ranetal.,2019;Gevaetal.,
2020;Pie˛kosetal.,2021). Comparedtopriorwork,self-consistencyisapplicabletoawiderangeof
reasoningtaskswithoutanyadditionalsupervisionorfine-tuning,whilestillsubstantiallyimproving
theperformanceofthechain-of-thoughtpromptingapproachproposedinWeietal.(2022).
Samplingandre-rankinginlanguagemodels. Multipledecodingstrategiesforlanguagemodels
have been proposed in the literature, e.g., temperature sampling (Ackley et al., 1985; Ficler &
Goldberg, 2017), top-k sampling (Fan et al., 2018; Holtzman et al., 2018; Radford et al., 2019),
nucleussampling(Holtzmanetal.,2020),minimumBayesriskdecoding(Eikema&Aziz,2020;Shi
etal.,2022),andtypicaldecoding(Meisteretal.,2022). Otherworkhassoughttoexplicitlypromote
diversityinthedecodingprocess(Batraetal.,2012;Lietal.,2016;Vijayakumaretal.,2018).
Re-rankingisanothercommonapproachtoimprovegenerationqualityinlanguagemodels(Adiwar-
danaetal.,2020;Shenetal.,2021). Thoppilanetal.(2022)collectadditionalhumanannotations
totrainare-rankerforresponsefiltering. Cobbeetal.(2021)traina“verifier”tore-rankgenerated
solutions,whichsubstantiallyimprovesthesolverateonmathtaskscomparedtojustfine-tuningthe
languagemodel. Elazaretal.(2021)improvetheconsistencyoffactualknowledgeextractionby
extendingpre-trainingwithanadditionalconsistencyloss. Allthesemethodsrequireeithertraining
anadditionalre-rankerorcollectingadditionalhumanannotation,whileself-consistencyrequiresno
additionaltraining,fine-tuning,norextradatacollection.
Extractreasoningpaths. Somepreviousworkhasconsideredtask-specificapproachesforiden-
tifyingreasoningpaths,suchasconstructingsemanticgraphs(Xuetal.,2021a),learninganRNN
to retrieve reasoning paths over the Wikipedia graph (Asai et al., 2020), fine-tuning with human
annotated reasoning paths on math problems (Cobbe et al., 2021), or training an extractor with
heuristic-based pseudo reasoning paths (Chen et al., 2019). More recently, the importance of di-
versityinthereasoningprocesseshasbeennoticed, butonlyleveragedviatask-specifictraining,
eitherthroughanadditionalQAmodeloverextractedreasoningpaths(Chenetal.,2019),orbythe
introductionoflatentvariablesinacommonsenseknowledgegraph(Yuetal.,2022). Comparedto
theseapproaches,self-consistencyisfarsimplerandrequiresnoadditionaltraining. Theapproach
weproposesimplycouplesthegenerationofreasoningpathsandafinalanswerbysamplingfrom
thedecoder,usingaggregationtorecoverthemostconsistentanswerwithoutadditionalmodules.
Consistencyinlanguagemodels. Somepriorworkhasshownthatlanguagemodelscansuffer
frominconsistencyinconversation(Adiwardanaetal.,2020),explanationgeneration(Camburuetal.,
2020),andfactualknowledgeextraction(Elazaretal.,2021). Wellecketal.(2020)use“consistency”
torefertogeneratinganinfinite-lengthsequenceinrecurrentlanguagemodels. Nyeetal.(2021)
improvethelogicalconsistencyofsamplesfromaSystem1modelbyaddingaSystem2-inspired
logicalreasoningmodule. Inthispaperwefocusonaslightlydifferentnotionof“consistency”,i.e.,
utilizinganswerconsistencyamongdiversereasoningpathstoimproveaccuracy.
5 CONCLUSION AND DISCUSSION
Weintroducedasimpleyeteffectivemethodcalledself-consistency,andobservedthatitsignificantly
improves accuracy in a range of arithmetic and commonsense reasoning tasks, across four large
language models with varying scales. Beyond accuracy gains, self-consistency is also useful for
collecting rationales when performing reasoning tasks with language models, and for providing
uncertaintyestimatesandimprovedcalibrationoflanguagemodeloutputs.
Onelimitationofself-consistencyisthatitincursmorecomputationcost. Inpracticepeoplecantrya
smallnumberofpaths(e.g.,5or10)asastartingpointtorealizemostofthegainswhilenotincurring
toomuchcost,asinmostcasestheperformancesaturatesquickly(Figure2). Aspartoffuturework,
onecoulduseself-consistencytogeneratebettersuperviseddatatofine-tunethemodel,suchthatthe
modelcangivemoreaccuratepredictionsinasingleinferencerunafterfine-tuning. Inaddition,we
observedthatlanguagemodelscansometimesgenerateincorrectornonsensicalreasoningpaths(e.g.,
theStrategyQAexampleinTable4,thetwopopulationnumbersarenotexactlycorrect),andfurther
workisneededtobettergroundmodels’rationalegenerations.
9

PublishedasaconferencepaperatICLR2023
REPRODUCIBILITY STATEMENT
Inexperiments,weincludedfourdifferentlanguagemodelswithvaryingscales.Twoofthemarepub-
licmodels:UL2isacompletelyopen-sourcedmodelwithmodelcheckpointsavailableathttps://
github.com/google-research/google-research/tree/master/ul2; GPT-3 is
also a public model with public API available at https://openai.com/api/. For GPT-3,
wehaveincludedtwopublicengines(“code-davinci-001”and“code-davinci-002”)tofurtheraid
reproducibility,asCodexiscurrentlyfreesoanyonecanreproducetheresults. Inaddition,asour
resultsmakeuseofLaMDA-137BandPaLM-540Bthatarenotpubliclyavailable,weprovidethe
exactinputpromptsforalltasksinAppendixA.3(andnotethatwedonotperformanyfinetuning
andonlyapplypromptingtooff-the-shelflanguagemodels).
ETHICS STATEMENT
Aswestatedinthediscussion,languagemodelscansometimesgeneratenonsensicalornon-factual
reasoning paths, so one should use language models’ outputs with extra caution. We deal with
reasoningtasksmostlyandthegeneratedrationalesareonlyusedforinspectinghowamodelreaches
itsanswer. Onecouldpotentiallyusethegeneratedrationalestofurthercheckwhythemodelmakes
certain mistakes or whether the model contains any biases when performing a certain task. For
languagemodelinreal-worlduse,furtherworkisneededtobettergroundmodels’predictionsand
improvemodel’sfactualityandsafety,toensurethemodelsdonotcauseharmstousers.
REFERENCES
DavidH.Ackley,GeoffreyE.Hinton,andTerrenceJ.Sejnowski. Alearningalgorithmforboltzmann
machines. Cognitive Science, 9(1):147–169, 1985. ISSN 0364-0213. URL https://www.
sciencedirect.com/science/article/pii/S0364021385800124.
DanielAdiwardana,Minh-ThangLuong,DavidR.So,JamieHall,NoahFiedel,RomalThoppilan,
ZiYang,ApoorvKulshreshtha,GauravNemade,YifengLu,andQuocV.Le.Towardsahuman-like
open-domainchatbot,2020.
AidaAmini, SaadiaGabriel, ShanchuanLin, RikKoncel-Kedziorski, YejinChoi, andHannaneh
Hajishirzi. MathQA: Towards interpretable math word problem solving with operation-based
formalisms. In Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long
andShortPapers),pp.2357–2367.AssociationforComputationalLinguistics,June2019. URL
https://aclanthology.org/N19-1245.
Daniel Andor, Luheng He, Kenton Lee, and Emily Pitler. Giving BERT a calculator: Finding
operationsandargumentswithreadingcomprehension. InProceedingsofthe2019Conferenceon
EmpiricalMethodsinNaturalLanguageProcessingandthe9thInternationalJointConference
onNaturalLanguageProcessing(EMNLP-IJCNLP),2019. URLhttps://aclanthology.
org/D19-1609.
AkariAsai,KazumaHashimoto,HannanehHajishirzi,RichardSocher,andCaimingXiong. Learn-
ing to retrieve reasoning paths over wikipedia graph for question answering. In International
ConferenceonLearningRepresentations,2020. URLhttps://openreview.net/forum?
id=SJgVHkrYDH.
Roy Bar-Haim, IdoDagan, Bill Dolan, Lisa Ferro, DaniloGiampiccolo, BernardoMagnini, and
IdanSzpektor. Thesecondpascalrecognisingtextualentailmentchallenge. InProceedingsofthe
secondPASCALchallengesworkshoponrecognisingtextualentailment,2006.
DhruvBatra,PaymanYadollahpour,AbnerGuzman-Rivera,andGregoryShakhnarovich. Diverse
m-bestsolutionsinmarkovrandomfields. InProceedingsofthe12thEuropeanConferenceon
ComputerVision-VolumePartV,ECCV’12,pp.1–16,Berlin,Heidelberg,2012.Springer-Verlag.
ISBN9783642337147. URLhttps://doi.org/10.1007/978-3-642-33715-4_1.
10

PublishedasaconferencepaperatICLR2023
LuisaBentivogli,PeterClark,IdoDagan,andDaniloGiampiccolo. Thefifthpascalrecognizing
textualentailmentchallenge. InTAC,2009.
BIG-bench collaboration. Beyond the imitation game: Measuring and extrapolating the capabil-
ities of language models. In preparation, 2021. URL https://github.com/google/
BIG-bench/.
TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan,PrafullaDhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss,GretchenKrueger,TomHenighan,RewonChild,AdityaRamesh,DanielZiegler,
JeffreyWu,ClemensWinter,ChrisHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,
BenjaminChess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,IlyaSutskever,
andDarioAmodei. Languagemodelsarefew-shotlearners. InAdvancesinNeuralInformation
ProcessingSystems, 2020. URLhttps://proceedings.neurips.cc/paper/2020/
file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
Oana-Maria Camburu, Tim Rocktäschel, Thomas Lukasiewicz, and Phil Blunsom. e-
snli: Natural language inference with natural language explanations. In S. Ben-
gio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett
(eds.), Advances in Neural Information Processing Systems 31, pp. 9539–9549.
Curran Associates, Inc., 2018. URL http://papers.nips.cc/paper/
8163-e-snli-natural-language-inference-with-natural-language-explanations.
pdf.
Oana-MariaCamburu,BrendanShillingford,PasqualeMinervini,ThomasLukasiewicz,andPhil
Blunsom.Makeupyourmind!adversarialgenerationofinconsistentnaturallanguageexplanations.
InProceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,pp.
4157–4165,Online,July2020.AssociationforComputationalLinguistics. doi: 10.18653/v1/2020.
acl-main.382. URLhttps://aclanthology.org/2020.acl-main.382.
JifanChen,Shih-TingLin,andGregDurrett. Multi-hopquestionansweringviareasoningchains.
CoRR,abs/1910.02610,2019. URLhttp://arxiv.org/abs/1910.02610.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared
Kaplan,HarriEdwards, YuriBurda, NicholasJoseph, GregBrockman, etal. Evaluatinglarge
languagemodelstrainedoncode. arXivpreprintarXiv:2107.03374,2021.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts,PaulBarham,HyungWonChung,CharlesSutton,SebastianGehrmann,ParkerSchuh,
KensenShi,SashaTsvyashchenko,JoshuaMaynez,AbhishekRao,ParkerBarnes,YiTay,Noam
Shazeer,VinodkumarPrabhakaran,EmilyReif,NanDu,BenHutchinson,ReinerPope,James
Bradbury,JacobAustin,MichaelIsard,GuyGur-Ari,PengchengYin,TojuDuke,AnselmLev-
skaya,SanjayGhemawat,SunipaDev,HenrykMichalewski,XavierGarcia,VedantMisra,Kevin
Robinson,LiamFedus,DennyZhou,DaphneIppolito,DavidLuan,HyeontaekLim,BarretZoph,
AlexanderSpiridonov,RyanSepassi,DavidDohan,ShivaniAgrawal,MarkOmernick,AndrewM.
Dai,ThanumalayanSankaranarayanaPillai,MariePellat,AitorLewkowycz,EricaMoreira,Rewon
Child,OleksandrPolozov,KatherineLee,ZongweiZhou,XuezhiWang,BrennanSaeta,Mark
Diaz,OrhanFirat,MicheleCatasta,JasonWei,KathyMeier-Hellstern,DouglasEck,JeffDean,
Slav Petrov, and Noah Fiedel. Palm: Scaling language modeling with pathways, 2022. URL
https://arxiv.org/abs/2204.02311.
ChristopherClark,KentonLee,Ming-WeiChang,TomKwiatkowski,MichaelCollins,andKristina
Toutanova. Boolq: Exploringthesurprisingdifficultyofnaturalyes/noquestions. InNAACL,
2019.
PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,AshishSabharwal,CarissaSchoenick,and
OyvindTafjord. Thinkyouhavesolvedquestionanswering? tryarc,theai2reasoningchallenge.
ArXiv,abs/1803.05457,2018.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
MatthiasPlappert,JerryTworek,JacobHilton,ReiichiroNakano,ChristopherHesse,andJohn
Schulman. Trainingverifierstosolvemathwordproblems,2021.
11

PublishedasaconferencepaperatICLR2023
Ido Dagan, Oren Glickman, and Bernardo Magnini. The pascal recognising textual entailment
challenge. InMachineLearningChallengesWorkshop,pp.177–190.Springer,2005.
BryanEikemaandWilkerAziz. IsMAPdecodingallyouneed?theinadequacyofthemodeinneural
machinetranslation. InProceedingsofthe28thInternationalConferenceonComputationalLin-
guistics,pp.4506–4520,Barcelona,Spain(Online),December2020.InternationalCommitteeon
ComputationalLinguistics. URLhttps://aclanthology.org/2020.coling-main.
398.
Yanai Elazar, Nora Kassner, Shauli Ravfogel, Abhilasha Ravichander, Eduard Hovy, Hinrich
Schütze, and Yoav Goldberg. Measuring and improving consistency in pretrained language
models. TransactionsoftheAssociationforComputationalLinguistics,9:1012–1031,2021. doi:
10.1162/tacl_a_00410. URLhttps://aclanthology.org/2021.tacl-1.60.
JonathanStBTEvans. Intuitionandreasoning: Adual-processperspective. PsychologicalInquiry,
21(4):313–326,2010.
AngelaFan,MikeLewis,andYannDauphin. Hierarchicalneuralstorygeneration. InProceedings
ofthe56thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1: Long
Papers),pp.889–898,Melbourne,Australia,July2018.AssociationforComputationalLinguistics.
doi: 10.18653/v1/P18-1082. URLhttps://aclanthology.org/P18-1082.
JessicaFiclerandYoavGoldberg.Controllinglinguisticstyleaspectsinneurallanguagegeneration.In
ProceedingsoftheWorkshoponStylisticVariation,pp.94–104,Copenhagen,Denmark,September
2017.AssociationforComputationalLinguistics. doi: 10.18653/v1/W17-4912. URLhttps:
//aclanthology.org/W17-4912.
TianyuGao,AdamFisch,andDanqiChen. Makingpre-trainedlanguagemodelsbetterfew-shot
learners. InProceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguis-
ticsandthe11thInternationalJointConferenceonNaturalLanguageProcessing(Volume1: Long
Papers),pp.3816–3830,Online,August2021.AssociationforComputationalLinguistics. doi:
10.18653/v1/2021.acl-long.295. URLhttps://aclanthology.org/2021.acl-long.
295.
MorGeva,AnkitGupta,andJonathanBerant. Injectingnumericalreasoningskillsintolanguage
models. InProceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguis-
tics,2020. doi: 10.18653/v1/2020.acl-main.89. URLhttps://aclanthology.org/2020.
acl-main.89.
MorGeva,DanielKhashabi,EladSegal,TusharKhot,DanRoth,andJonathanBerant. Didaristotle
usealaptop? Aquestionansweringbenchmarkwithimplicitreasoningstrategies. Transactionsof
theAssociationforComputationalLinguistics,2021. URLhttps://aclanthology.org/
2021.tacl-1.21.
DaniloGiampiccolo,BernardoMagnini,IdoDagan,andBillDolan. Thethirdpascalrecognizing
textualentailmentchallenge. InProceedingsoftheACL-PASCALworkshopontextualentailment
andparaphrasing,pp.1–9.AssociationforComputationalLinguistics,2007.
AriHoltzman,JanBuys,MaxwellForbes,AntoineBosselut,DavidGolub,andYejinChoi. Learning
to write with cooperative discriminators. In Proceedings of the 56th Annual Meeting of the
AssociationforComputationalLinguistics(Volume1: LongPapers),pp.1638–1649,Melbourne,
Australia, July 2018. Association for Computational Linguistics. doi: 10.18653/v1/P18-1152.
URLhttps://aclanthology.org/P18-1152.
AriHoltzman,JanBuys,LiDu,MaxwellForbes,andYejinChoi. Thecuriouscaseofneuraltext
degeneration. InInternationalConferenceonLearningRepresentations, 2020. URLhttps:
//openreview.net/forum?id=rygGQyrFvH.
MohammadJavadHosseini,HannanehHajishirzi,OrenEtzioni,andNateKushman. Learningto
solvearithmeticwordproblemswithverbcategorization.InProceedingsofthe2014Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing(EMNLP),2014. doi: 10.3115/v1/D14-1058.
URLhttps://aclanthology.org/D14-1058.
12

PublishedasaconferencepaperatICLR2023
DanielKhashabi,SewonMin,TusharKhot,AshishSabharwal,OyvindTafjord,PeterClark,andHan-
nanehHajishirzi. UNIFIEDQA:CrossingformatboundarieswithasingleQAsystem. InFindings
oftheAssociationforComputationalLinguistics: EMNLP2020,pp.1896–1907,Online,Novem-
ber2020.AssociationforComputationalLinguistics. doi: 10.18653/v1/2020.findings-emnlp.171.
URLhttps://aclanthology.org/2020.findings-emnlp.171.
TakeshiKojima,ShixiangShaneGu,MachelReid,YutakaMatsuo,andYusukeIwasawa. Large
language models are zero-shot reasoners. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave,
and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems, 2022. URL
https://openreview.net/forum?id=e2TBb5y0yFf.
RikKoncel-Kedziorski,SubhroRoy,AidaAmini,NateKushman,andHannanehHajishirzi.MAWPS:
Amathwordproblemrepository. InProceedingsofthe2016ConferenceoftheNorthAmerican
ChapteroftheAssociationforComputationalLinguistics: HumanLanguageTechnologies,2016.
doi: 10.18653/v1/N16-1136. URLhttps://aclanthology.org/N16-1136.
YihuaiLan,LeiWang,QiyuanZhang,YunshiLan,BingTianDai,YanWang,DongxiangZhang,
andEe-PengLim. MWPToolkit: Anopen-sourceframeworkfordeeplearning-basedmathword
problemsolvers. arXivpreprintarXiv:2109.00799,2021. URLhttps://arxiv.org/abs/
2109.00799.
Jiwei Li and Dan Jurafsky. Mutual information and diverse decoding improve neural machine
translation,2016. URLhttps://arxiv.org/abs/1601.00372.
Jiwei Li, Will Monroe, and Dan Jurafsky. A simple, fast diverse decoding algorithm for neural
generation. CoRR,abs/1611.08562,2016. URLhttp://arxiv.org/abs/1611.08562.
WangLing,DaniYogatama,ChrisDyer,andPhilBlunsom. Programinductionbyrationalegenera-
tion: Learningtosolveandexplainalgebraicwordproblems. InProceedingsofthe55thAnnual
MeetingoftheAssociationforComputationalLinguistics(Volume1: LongPapers),2017. doi:
10.18653/v1/P17-1015. URLhttps://aclanthology.org/P17-1015.
Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp. Fantastically
orderedpromptsandwheretofindthem: Overcomingfew-shotpromptordersensitivity. ArXiv,
abs/2104.08786,2021.
ClaraMeister,TiagoPimentel,GianWiher,andRyanCotterell.Typicaldecodingfornaturallanguage
generation. arXivpreprintarXiv:2202.00666,2022.
ShenYunMiao,ChaoChunLiang,andKehYihSu. Adiversecorpusforevaluatinganddeveloping
English math word problem solvers. In Proceedings of the 58th Annual Meeting of the Asso-
ciationforComputationalLinguistics,2020. URLhttps://aclanthology.org/2020.
acl-main.92.
YixinNie,AdinaWilliams,EmilyDinan,MohitBansal,JasonWeston,andDouweKiela. Adver-
sarialNLI:Anewbenchmarkfornaturallanguageunderstanding. InProceedingsofthe58th
AnnualMeetingoftheAssociationforComputationalLinguistics.AssociationforComputational
Linguistics,2020.
MaxwellNye, MichaelHenryTessler, JoshuaB.Tenenbaum, andBrendenM.Lake. Improving
coherenceandconsistencyinneuralsequencemodelswithdual-system,neuro-symbolicreasoning.
InA.Beygelzimer,Y.Dauphin,P.Liang,andJ.WortmanVaughan(eds.),AdvancesinNeural
Information Processing Systems, 2021. URL https://openreview.net/forum?id=
uyKk_avJ-p4.
ArkilPatel,SatwikBhattamishra,andNavinGoyal. AreNLPmodelsreallyabletosolvesimple
mathwordproblems? InProceedingsofthe2021ConferenceoftheNorthAmericanChapterof
theAssociationforComputationalLinguistics: HumanLanguageTechnologies,pp.2080–2094,
Online,June2021.AssociationforComputationalLinguistics. doi: 10.18653/v1/2021.naacl-main.
168. URLhttps://aclanthology.org/2021.naacl-main.168.
XinyuPi,QianLiu,BeiChen,MortezaZiyadi,ZeqiLin,YanGao,QiangFu,Jian-GuangLou,and
WeizhuChen. Reasoninglikeprogramexecutors,2022.
13

PublishedasaconferencepaperatICLR2023
PiotrPie˛kos,MateuszMalinowski,andHenrykMichalewski. MeasuringandimprovingBERT’s
mathematicalabilitiesbypredictingtheorderofreasoning.InProceedingsofthe59thAnnualMeet-
ingoftheAssociationforComputationalLinguisticsandthe11thInternationalJointConferenceon
NaturalLanguageProcessing(Volume2:ShortPapers),2021.doi:10.18653/v1/2021.acl-short.49.
URLhttps://aclanthology.org/2021.acl-short.49.
AlecRadford,JeffWu,RewonChild,DavidLuan,DarioAmodei,andIlyaSutskever. Language
modelsareunsupervisedmultitasklearners. 2019.
JackWRae,SebastianBorgeaud,TrevorCai,KatieMillican,JordanHoffmann,FrancisSong,John
Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models:
Methods,analysis&insightsfromtraininggopher. arXivpreprintarXiv:2112.11446,2021.
QiuRan,YankaiLin,PengLi,JieZhou,andZhiyuanLiu. NumNet:Machinereadingcomprehension
withnumericalreasoning.InProceedingsofthe2019ConferenceonEmpiricalMethodsinNatural
LanguageProcessingandthe9thInternationalJointConferenceonNaturalLanguageProcessing
(EMNLP-IJCNLP), 2019. doi: 10.18653/v1/D19-1251. URL https://aclanthology.
org/D19-1251.
SubhroRoyandDanRoth. Solvinggeneralarithmeticwordproblems. InProceedingsofthe2015
Conference on Empirical Methods in Natural Language Processing, 2015. doi: 10.18653/v1/
D15-1202. URLhttps://aclanthology.org/D15-1202.
JianhaoShen,YichunYin,LinLi,LifengShang,XinJiang,MingZhang,andQunLiu. Generate
& rank: A multi-task framework for math word problems. In Findings of the Association for
Computational Linguistics: EMNLP 2021, pp. 2269–2279, Punta Cana, Dominican Republic,
November2021.AssociationforComputationalLinguistics. URLhttps://aclanthology.
org/2021.findings-emnlp.195.
Freda Shi, Daniel Fried, Marjan Ghazvininejad, Luke Zettlemoyer, and Sida I. Wang. Natural
languagetocodetranslationwithexecution. InProceedingsofthe2022ConferenceonEmpirical
MethodsinNaturalLanguageProcessing, pp.3533–3546, AbuDhabi, UnitedArabEmirates,
December2022.AssociationforComputationalLinguistics. URLhttps://aclanthology.
org/2022.emnlp-main.231.
Keith E Stanovich and Richard F West. Individual differences in reasoning: Implications for
the rationality debate? Behavioral and brain sciences, 23(5):645–665, 2000. URL https:
//pubmed.ncbi.nlm.nih.gov/11301544/.
AlonTalmor,JonathanHerzig,NicholasLourie,andJonathanBerant. CommonsenseQA:Aquestion
answeringchallengetargetingcommonsenseknowledge. InProceedingsofthe2019Conferenceof
theNorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguage
Technologies, Volume 1 (Long and Short Papers), 2019. URL https://aclanthology.
org/N19-1421.
YiTay,MostafaDehghani,VinhQ.Tran,XavierGarcia,JasonWei,XuezhiWang,HyungWonChung,
DaraBahri,TalSchuster,StevenZheng,DennyZhou,NeilHoulsby,andDonaldMetzler. Unifying
languagelearningparadigms,2022. URLhttps://arxiv.org/abs/2205.05131.
RomalThoppilan,DanielDeFreitas,JamieHall,NoamShazeer,ApoorvKulshreshtha,Heng-Tze
Cheng,AliciaJin,TaylorBos,LeslieBaker,YuDu,etal. Lamda: Languagemodelsfordialog
applications. arXiv preprint arXiv:2201.08239, 2022. URL https://arxiv.org/abs/
2201.08239.
Ashwin Vijayakumar, Michael Cogswell, Ramprasaath Selvaraju, Qing Sun, Stefan Lee, David
Crandall, andDhruvBatra. Diversebeamsearchforimproveddescriptionofcomplexscenes.
Proceedings of the AAAI Conference on Artificial Intelligence, 32, Apr. 2018. URL https:
//ojs.aaai.org/index.php/AAAI/article/view/12340.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdChi,Quoc
Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models.
ConferenceonNeuralInformationProcessingSystems(NeurIPS),2022. URLhttps://arxiv.
org/pdf/2201.11903.
14

PublishedasaconferencepaperatICLR2023
SeanWelleck,IliaKulikov,JaedeokKim,RichardYuanzhePang,andKyunghyunCho. Consistency
ofarecurrentlanguagemodelwithrespecttoincompletedecoding. InProceedingsofthe2020
ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP),pp.5553–5568,
Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.
emnlp-main.448. URLhttps://aclanthology.org/2020.emnlp-main.448.
Weiwen Xu, Yang Deng, Huihui Zhang, Deng Cai, and Wai Lam. Exploiting reasoning chains
for multi-hop science question answering. In Findings of the Association for Computational
Linguistics: EMNLP2021,pp.1143–1156,PuntaCana,DominicanRepublic,November2021a.
Association for Computational Linguistics. URL https://aclanthology.org/2021.
findings-emnlp.99.
Yichong Xu, Chenguang Zhu, Shuohang Wang, Siqi Sun, Hao Cheng, Xiaodong Liu, Jianfeng
Gao, Pengcheng He, Michael Zeng, and Xuedong Huang. Human parity on commonsenseqa:
Augmentingself-attentionwithexternalattention,2021b. URLhttps://arxiv.org/abs/
2112.03254.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamCohen,RuslanSalakhutdinov,and
ChristopherD.Manning. HotpotQA:Adatasetfordiverse,explainablemulti-hopquestionanswer-
ing.InProceedingsofthe2018ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,
pp.2369–2380,Brussels,Belgium,October-November2018.AssociationforComputationalLin-
guistics. doi: 10.18653/v1/D18-1259. URLhttps://aclanthology.org/D18-1259.
XiYeandGregDurrett. Theunreliabilityofexplanationsinfew-shotpromptingfortextualreasoning.
In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in
NeuralInformationProcessingSystems,2022. URLhttps://openreview.net/forum?
id=Bct2f8fRd8S.
WenhaoYu,ChenguangZhu,LianhuiQin,ZhihanZhang,TongZhao,andMengJiang. Diversifying
content generation for commonsense reasoning with mixture of knowledge graph experts. In
FindingsofAnnualMeetingoftheAssociationforComputationalLinguistics(ACL),2022.
ZihaoZhao,EricWallace,ShiFeng,DanKlein,andSameerSingh. Calibratebeforeuse: Improving
few-shot performance of language models. In Marina Meila and Tong Zhang (eds.), Proceed-
ingsofthe38thInternationalConferenceonMachineLearning,volume139ofProceedingsof
Machine Learning Research. PMLR, 2021. URL https://proceedings.mlr.press/
v139/zhao21c.html.
15

PublishedasaconferencepaperatICLR2023
A APPENDIX
A.1 ADDITIONALEXPERIMENTRESULTS
| A.1.1 | ROBUSTNESSTOSAMPLINGSTRATEGIESANDPARAMETERS |     |     |     |     |     |     |     |
| ----- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
In Figure 6 we ablate the results with respect to different sampling strategies and parameters by
|     | T   |     |     | k Top-k |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
varying in temperature sampling and in sampling, on LaMDA-137B. We show that
self-consistencyisrobusttovarioussamplingstrategiesandparameters.
28
|     |     | )%( ycaruccA 26 |     |     | T=0.7, k=40 |     |     |     |
| --- | --- | --------------- | --- | --- | ----------- | --- | --- | --- |
T=0.5, k=40
24
T=0.3, k=40
22
T=0.5, k=20
|     |     | 20  |     |     | T=0.5, no top k |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
|     |     | 18  |     |     | Greedy Decode   |     |     |     |
4 8 1216202428323640
#Sampled Reasoning Paths
Figure6: GSM8KaccuracyoverLaMDA-137B.Self-consistencyworksundervarioussampling
strategiesandsamplingparameters.
InFigure7andFigure8,weshowtheresultsofself-consistencycomparedwithgreedydecodinga
singlepathoverLaMDA-137BandPaLM-540B,respectively. Self-consistencyimprovesovergreedy
decodebyaquitesignificantmarginonbothmodels,ontopofhighaccuracyalreadyachievedby
scalingupmodelsizes.
|                 | MultiArith |     | ASDiv |     | SVAMP |     | GSM8K                         |     |
| --------------- | ---------- | --- | ----- | --- | ----- | --- | ----------------------------- | --- |
|                 |            | 58  |       | 54  |       | 28  |                               |     |
| )%( ycaruccA 75 |            | 56  |       | 51  |       | 26  |                               |     |
| 70              |            | 54  |       | 48  |       | 24  |                               |     |
| 65              |            | 52  |       | 45  |       | 22  | Greedy Decode (Single-path)   |     |
| 60              |            | 50  |       | 42  |       | 20  | Self Consistency (Multi-path) |     |
| 55              |            | 48  |       | 39  |       | 18  |                               |     |
| 50              |            | 46  |       | 36  |       | 16  |                               |     |
|                 |            | 44  |       | 33  |       | 14  |                               |     |
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths
|     | Commonsense QA |     | Strategy QA |     | ARC (Easy) |     | ARC (Challenge) |     |
| --- | -------------- | --- | ----------- | --- | ---------- | --- | --------------- | --- |
60
| )%( ycaruccA |     | 68  |     | 78  |     |     |                      |                               |
| ------------ | --- | --- | --- | --- | --- | --- | -------------------- | ----------------------------- |
| 62           |     | 67  |     |     |     | 58  |                      |                               |
| 60           |     | 66  |     | 76  |     |     |                      |                               |
|              |     |     |     | 7 4 |     | 56  |                      |                               |
| 58           |     | 6 5 |     |     |     | 5 4 |                      |                               |
|              |     | 6 4 |     | 7 2 |     |     | G re e d y  D e c o  | d e  ( S in g l e - p a t h ) |
| 56           |     | 6 3 |     | 7 0 |     | 5 2 |                      |                               |
|              |     |     |     | 6 8 |     | 5 0 | Se lf  C o n si s te | n c y   (M u l t i- p a t h ) |
6 2
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths
Figure 7: Self-consistency (blue) significantly improves accuracy across various arithmetic and
commonsensereasoningtasks,overLaMDA-137B.Samplingahighernumberofdiversereasoning
pathsconsistentlyimprovesreasoningaccuracy.
WefurthershowadditionalsampledreasoningpathsfromtheLaMDA-137BmodelinTable12,and
sampledreasoningpathsfromthePaLM-540BmodelinTable13. Weseethatthediversityinthe
additionallysampledreasoningpathsindeedhelpsthemodelarriveatamorecorrectfinalanswer
afteraggregation.
| A.1.2 | ROBUSTNESSTODIFFERENTSETSOFPROMPTS |     |     |     |     |     |     |     |
| ----- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
InTable9,wefurthershowthatself-consistencyisquiterobusttodifferentsetsofinputprompts.
Wemanuallywrote3differentsetsofchain-of-thoughtaspromptstothemodel. Acrossallsetsof
prompts,self-consistencyyieldsconsistentgainsovertheoriginalCoTapproach.
| A.1.3 | COMPAREDTOMODELENSEMBLES |     |     |     |     |     |     |     |
| ----- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
Additionally,weprovideresultsofdirectlyensemblingtheoutputsfrommultiplelanguagemodels.
TheresultsareshowninTable10, bygreedilydecodingsequencesfrom3languagemodelsand
16

PublishedasaconferencepaperatICLR2023
|     |     | AddSub |     |     |     | ASDiv |     |     |     |
| --- | --- | ------ | --- | --- | --- | ----- | --- | --- | --- |
AQuA
|     | )%( ycaruccA 94 |     |     | )%( ycaruccA 82 |     |     |                 |     |                             |
| --- | --------------- | --- | --- | --------------- | --- | --- | --------------- | --- | --------------------------- |
|     |                 |     |     | 80              |     |     | )%( ycaruccA 48 |     |                             |
|     | 92              |     |     |                 |     |     | 45              |     |                             |
|     |                 |     |     | 78              |     |     | 42              |     | Greedy Decode (Single-path) |
90
|     |     |     |     | 76  |     |     | 39  |     | Self Consistency (Multi-path) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- |
|     | 88  |     |     | 74  |     |     | 36  |     |                               |
|     |     |     |     | 72  |     |     | 33  |     |                               |
|     | 86  |     |     |     |     |     | 30  |     |                               |
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Chains #Sampled Reasoning Chains #Sampled Reasoning Chains
|     | MultiArith   |     |              |      |     | SVAMP |              |     |                               |
| --- | ------------ | --- | ------------ | ---- | --- | ----- | ------------ | --- | ----------------------------- |
|     |              |     |              | 87.5 |     |       |              |     | GSM8K                         |
|     | )%( ycaruccA |     | )%( ycaruccA | 85.0 |     |       | 75           |     |                               |
|     | 98           |     |              |      |     |       | )%( ycaruccA |     |                               |
|     | 96           |     |              | 82.5 |     |       | 70           |     |                               |
|     |              |     |              | 80.0 |     |       | 65           |     |                               |
|     | 94           |     |              |      |     |       |              |     | Greedy Decode (Single-path)   |
|     |              |     |              | 77.5 |     |       | 60           |     | Self Consistency (Multi-path) |
|     | 92           |     |              | 75.0 |     |       |              |     |                               |
|     | 90           |     |              |      |     |       | 55           |     |                               |
72.5
|     | 88        |          |       | 70.0 |         |                | 50  |        |                   |
| --- | --------- | -------- | ----- | ---- | ------- | -------------- | --- | ------ | ----------------- |
|     | 0 5 10 15 | 20 25 30 | 35 40 | 0    | 5 10 15 | 20 25 30 35 40 |     |        |                   |
|     |           |          |       |      |         |                |     | 0 5 10 | 15 20 25 30 35 40 |
#Sampled Reasoning Chains #Sampled Reasoning Chains #Sampled Reasoning Chains
|                 | Commonsense QA |     | Strategy QA |     |     | ARC (Easy) |     |     | ARC (Challenge)               |
| --------------- | -------------- | --- | ----------- | --- | --- | ---------- | --- | --- | ----------------------------- |
| )%( ycaruccA 81 |                | 82  |             |     |     | 96         |     |     |                               |
| 80              |                |     |             |     |     |            |     | 88  |                               |
| 79              |                | 80  |             |     |     | 94         |     | 86  |                               |
| 78              |                |     |             |     |     |            |     | 84  |                               |
| 77              |                | 78  |             |     |     | 92         |     |     |                               |
| 76              |                | 76  |             |     |     |            |     | 82  |                               |
|                 |                |     |             |     |     | 90         |     | 80  | Greedy Decode (Single-path)   |
| 75              |                | 74  |             |     |     |            |     | 78  | Self Consistency (Multi-path) |
| 74              |                |     |             |     |     | 88         |     |     |                               |
0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40 0 5 10 15 20 25 30 35 40
#Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths #Sampled Reasoning Paths
Figure 8: Self-consistency (blue) significantly improves accuracy across various arithmetic and
commonsensereasoningtasks,overPaLM-540B.Samplingahighernumberofdiversereasoning
pathsconsistentlyhelpsreasoningaccuracy.
|     |                    |     | Promptset1(usedinthemaintext) |     |             |     | Promptset2  |      | Promptset3  |
| --- | ------------------ | --- | ----------------------------- | --- | ----------- | --- | ----------- | ---- | ----------- |
|     | CoT(Weietal.,2022) |     |                               |     | 56.5        |     |             | 54.6 | 54.0        |
|     | Self-consistency   |     |                               |     | 74.4(+17.9) |     | 72.1(+17.5) |      | 70.4(+16.4) |
Table9: GSM8KaccuracyoverPaLM-540B.Theresultsshowrobustnessofself-consistencywith
respecttodifferentpromptsintheinput.
takingthemajorityvote(averagedover10runs). Notethisisatypicalensembleapproach(averaging
overthepredictionsovermultiplemodels)anditachievesaperformancesignificantlyworsethan
self-consistency(self-consistencyoverPaLM-540Bgetsanaccuracyof74.4%),aslower-capacity
modelsdragdowntheperformanceofhigher-capacitymodels. Inaddition,thisapproachislimitedin
twoways: 1)Itrequiresmultiplemodelsforanensemblewhichmightnotalwaysbeavailable,while
self-consistencyonlyrequiresonesinglemodelto“self-ensemble”;2)Ifoneofthemodelsismuch
weaker,itcanactuallyhurtthefinalperformance.
|             |     | Method                            |     |     |     |     |     |     | GSM8Kaccuracy |
| ----------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | ------------- |
| Singlemodel |     | PaLM-540B,greedy/self-consistency |     |     |     |     |     |     | 56.5/74.4     |
|             |     | LaMDA-137B+PaLM-540B              |     |     |     |     |     |     | 36.9±0.5      |
Ensembleofmodels PaLM-540B+GPT-3(code-davinci-001,175B) 36.6±0.4
|     |          | LaMDA-137B+GPT-3(code-davinci-001,175B)               |     |     |     |     |     |     | 16.0±0.8 |
| --- | -------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- |
|     |          | LaMDA-137B+PaLM-540B+GPT-3(code-davinci-001,175B)     |     |     |     |     |     |     | 33.3±0.7 |
|     | Table10: | ComparisonofGSM8Kaccuracyovermultiple-modelensembles. |     |     |     |     |     |     |          |
A.1.4 COMBININGSELF-CONSISTENCYWITHOTHERENSEMBLINGSTRATEGIES
Self-consistencyiscompletelycompatiblewithotherensemblestrategies,althoughthegainsachieved
byself-consistencyaresignificantlyhigherthanotherensemblestrategies(andcan“override”the
performancegainsachievedbyotherensemblestrategies). Wefurtherperformedexperimentsand
include the results in Table 11 (for a fair comparison, we use 40 sets of prompts, or 40 prompt
permutationstocomparewithself-consistencywith40paths,allexperimentsarebasedonPaLM-
540B).
17

PublishedasaconferencepaperatICLR2023
GSM8Kaccuracy
Differentsetsofprompts(x40) 58.9
Prompt-permutation(x40) 59.6
Self-consistency(x40) 74.4
Self-consistency+differentsetsofprompts(x40) 75.4
Self-consistency+prompt-permutation(x40) 73.8
Table11: Combiningself-consistencywithotherensemblingstrategies.
A.2 DETAILSONRESOURCESANDINFERENCE
Forallfourlanguagemodelsweperformprompting-basedinferenceonly. ForUL2weuseTPUv3
(2x2configuration,4chips,8cores). ForGPT-3modelstheexperimentsaredonethoughthepublic
API.10ForLaMDA-137BweuseTPUv3(8x8configuration,64chips,128cores). ForPaLM-540B
weuseTPUv4(4x4x12configuration,192chips,384cores). Mostinferencejobstake1to4hours
(overabout1,000examples)foreachtaskonUL2andLaMDA-137B,andabout2to12hourson
PaLM-540B.Sometasks(e.g.,commonsensereasoning)takelongerbutdonotexceed2daysfor
eachtask.
ForGPT-3models,weuse128maxtokensforallmethods,withoutfrequencypenaltyorpresence
penalty. Forallmodels,wetakethegeneratedoutputsuntilthestartofthenext“Q:"toparsethefinal
answers,consistentwithourpromptingformat.
Question GreedyDecode SampledPath1 SampledPath2
[MultiArith]Samhad10socks. Samhad10socks. Hethrew Sam had 10 socks. He Hehad10socks.Hethrewaway
If he threw away 3 old ones away3oldonesthatdidn’tfit. threwaway3oldones.So 3 old ones that didn’t fit. He
thatdidn’tfitandbought36new Hebought36newones. That nowhehas7left.Thenhe bought36newones. Sointotal
ones,howmanysockswouldhe meanshehas10+36-3=41 bought36newones. So hehas10-3+36=43socks.The
have? socks.Theansweris41. nowhehas7+36=43 answeris43.
socks.Theansweris43.
[SVAMP]Inaschoolthereare Thereare697girlsandtherest Thenumberofboysisthe In the beginning there are 697
697girlsandtherestareboys. areboys. Thatmeansthereare difference between 697 girlsandtherestareboys.So,the
Ifthereare228moregirlsthan 697 + 228 = 925 girls. The and228.Thisis697-228 numberofboysmustbe697-228
boys. Howmanyboysarethere restareboys.Sothenumberof =469.Theansweris469. =469boys.Theansweris469.
inthatschool? boysis925-697=228. The
answeris228.
[AQuA]Thereare10orangesin Thereare10orangesinabas- Thereare10orangesina Thereare10orangesinthebas-
abasket.Findtheno.ofwaysin ket. So there are 10 ways basket.Weneedtochoose ket.Ifyouchoose2oranges,you
which2orangesarechosenfrom inwhich2orangesarechosen 2orangesfromthebasket. have10C2=45waysofchoosing
thebasket?(a)45(b)90(c)120 fromthebasket. Sothenumberofwaysare 2oranges.Sotheansweris(a).
(d)150(e)180 10C2.Sotheansweris(a).
[CommonsenseQA] The man Theanswermustbesomething The answer must be Theanswermustbeaplacewhere
laidonthesoftmossandlooked thatissoftandmossy. Ofthe somewhere where moss themanislayingdownandlook-
up at the trees, where was the abovechoices, onlygroundis is found. Of the above ing up at trees. Of the above
man? (a)niagrafalls(b)forest softandmossy. Sotheanswer choices, only forests are choices, only forest is a place
(c)waterfall(d)ground(e)tree is(d). known for having moss. wherepeoplelaydownandlook
Sotheansweris(b). attrees.Sotheansweris(b).
[ARC]Whichofthesewillmost Plantingtreeswillnotharma The answer is (b), water Theansweris(b),waterpollution.
likelyharmahabitat? (a)plant- habitat.Sotheansweris(a). pollution, because it will Treesaregoodforahabitat,rain-
ingtrees.(b)waterpollution.(c) mostlikelyharmthehabi- fallisnecessaryforahabitat,and
rainfall.(d)sunlight. tat.Theotheranswersare sunlightisnecessaryforahabitat.
notlikelytoharmthehabi- Sotheansweris(b).
tat.
[ARC-challenge] Which pro- Theprocessofphotosynthesis Theformationoffossilfu- Theprocessthattakesthelongest
cessinthecarboncycletakesthe in plants takes the longest to elstakesthelongesttime time to complete is the forma-
longesttocomplete? (a)emis- complete.Sotheansweris(c). to complete. So the an- tion of fossil fuels, which hap-
sionofwaste. (b)respirationin sweris(d). pensovermillionsofyears. So
animals. (c) photosynthesis in theansweris(d).
plants.(d)formationoffossilfu-
els.
Table12: Additionalexampleswhereself-consistencyhelpsrepairtheerrorsovergreedydecodeon
LaMDA-137B.Twosampledreasoningpathsthatareconsistentwiththegroundtruthareshown.
10https://beta.openai.com/docs/api-reference/making-requests
18

PublishedasaconferencepaperatICLR2023
Question GreedyDecode SampledPath1 SampledPath2
[GSM8K] Kyle bought last The book was sold for $19.50. Theoriginalpriceofthebook Kyle bought a book that is sold
year’s best-selling book for This is 25% less than the origi- is $19.50. Since it was dis- for$19.50. Witha25%discount,
$19.50.Thisiswitha25%dis- nalprice.Thismeanstheoriginal countedby25%,theoriginal theoriginalpricemustbehigher.
countfromtheoriginalprice. pricewas100%. 25%of100% price was 19.50 / 0.75 = 26. If we call the original price x,
Whatwastheoriginalpriceof is 25%. So the original price Theansweris26. thenthediscountedpriceis0.75x.
thebook? was 100% - 25% = 75%. The Sincethisis$19.50,wecanwrite
originalpricewas75%of$19.50. 0.75x=19.50. Solvingthis, we
75%of$19.50is75%*$19.50= findthattheoriginalpriceisx=
$14.625.Theansweris$14.625. 19.50/0.75=$26. Theansweris
$26.
[AQuA] The capacity of a Thevolumeofthetankis8m* Thevolumeofthetankis8m Thevolumeofthetankis8m*
tank of dimensions (8 m x 6 6m*2.5m=120m3. Sothe *6m*2.5m=120m3. Thisis 6m*2.5m=120m3. Onecu-
mx2.5m)is(a)120litres(b) capacityofthetankis120m3.So equalto120000litres. Sothe bicmetercontains1000litres,so
1200litres(c)12000litres(d) theansweris(c). answeris(d) thetankcontains120m3*1000
120000litres(e)Noneofthese liters/m3=120,000liters. Sothe
answeris(d).
[StrategyQA] Yes or no: The Great Depression was an Prozac is an anti-depressant TheGreatDepressionisatimepe-
CantheGreatDepressionbe economicdepression. Prozacis medication.TheGreatDepres- riod. Prozac is used to treat de-
treatedwithProzac? a drug used to treat depression. sion is not a disease. Thus, pression(thementalillness).Thus,
Thus,theGreatDepressioncould ProzaccannottreattheGreat the Great Depression can not be
betreatedwithProzac.Sothean- Depression. Sotheansweris treatedwithProzac.Sotheanswer
swerisyes. no. isno.
[ARC-easy]Whichsourceof Coal, sunlight, and water are Anonrenewablesourceofen- Coalisafossilfuelandisformed
energyisnonrenewable? (a) all renewable sources of energy. ergyisoneinwhichthesource fromdeadorganismsfromthepast.
coal. (b)sunlight. (c)water. Woodisanonrenewablesourceof is not replenished in a short Coalcannotbeproducedinashort
(d)wood. energy.Sotheansweris(d). amountoftime.Thus,theonly periodoftime,soitisconsidered
optionthatisnonrenewableis anonrenewablesourceofenergy.
coal.Sotheansweris(a). Sotheansweris(a).
[ARC-challenge] Students The Earth is closest to the Sun EarthisclosesttotheSunon Floridaisclosertothesunduring
studiedtherevolutionofEarth inDecember,henceFloridawill June21,thesummersolstice. June,soitwillhavethemostsun-
aroundtheSun.Duringwhich have the most sunlight energy Sotheansweris(b). lightenergyduringthatmonth.So
month will Florida have the availableinDecember.Sothean- theansweris(b).
most sunlight energy avail- sweris(d).
able? (a)March.(b)June.(c)
September.(d)December.
Table13: Additionalexampleswhereself-consistencyhelpsrepairtheerrorsovergreedydecodeon
PaLM-540B.Twosampledreasoningpathsthatareconsistentwiththegroundtruthareshown.
A.3 FULLSETSOFPROMPTS
Welistthefulldetailsofthepromptsusedfortwonewly-introduceddatasets,AQUA-RAT(Ling
etal.,2017)andAI2ReasoningChallenge(ARC)(Clarketal.,2018),wherewemanuallycomposed
theexamplechain-of-thoughtinthispaper,inTable14andTable15,respectively.
Table14: Few-shotexemplarsforAQUA-RAT.
Q:Johnfoundthattheaverageof15numbersis40. If10isaddedtoeachnumberthenthemeanofthe
numbersis?AnswerChoices:(a)50(b)45(c)65(d)78(e)64
A:If10isaddedtoeachnumber,thenthemeanofthenumbersalsoincreasesby10. Sothenewmean
wouldbe50.Theansweris(a).
Q:Ifa/b=3/4and8a+5b=22,thenfindthevalueofa.AnswerChoices:(a)1/2(b)3/2(c)5/2(d)4/2(e)
7/2
A:Ifa/b=3/4,thenb=4a/3.So8a+5(4a/3)=22.Thissimplifiesto8a+20a/3=22,whichmeans
44a/3=22.Soaisequalto3/2.Theansweris(b).
Q:Apersonistravelingat20km/hrandreachedhisdestinyin2.5hrthenfindthedistance?AnswerChoices:
(a)53km(b)55km(c)52km(d)60km(e)50km
A:Thedistancethatthepersontraveledwouldhavebeen20km/hr*2.5hrs=50km.Theansweris(e).
Q:Howmanykeystrokesareneededtotypethenumbersfrom1to500?AnswerChoices:(a)1156(b)1392
(c)1480(d)1562(e)1788
A:Thereare9one-digitnumbersfrom1to9.Thereare90two-digitnumbersfrom10to99.Thereare401
three-digitnumbersfrom100to500.9+90(2)+401(3)=1392.Theansweris(b).
19

PublishedasaconferencepaperatICLR2023
Table15: Few-shotexemplarsforARCeasy/challenge.
Q:Georgewantstowarmhishandsquicklybyrubbingthem. Whichskinsurfacewillproducethemost
heat?(a)drypalms.(b)wetpalms.(c)palmscoveredwithoil.(d)palmscoveredwithlotion.
A:Drysurfaceswillmorelikelycausemorefrictionviarubbingthanothersmoothersurfaces,hencedry
palmswillproducethemostheat.Theansweris(a).
Q:Whichfactorwillmostlikelycauseapersontodevelopafever?(a)alegmusclerelaxingafterexercise.
(b)abacterialpopulationinthebloodstream.(c)severalviralparticlesontheskin.(d)carbohydratesbeing
digestedinthestomach.
A:Option(b),bacterialpopulationisthemostlikelycauseforapersondevelopingfever.Theansweris(b).
Q:Whichchangeinthestateofwaterparticlescausestheparticlestobecomearrangedinafixedposition?
(a)boiling.(b)melting.(c)freezing.(d)evaporating.
A:Whenwaterisfreezed,theparticlesarearrangedinafixedposition;theparticlesarestillmovingforall
otheroptions.Theansweris(c).
Q:Whenaswitchisusedinanelectricalcircuit,theswitchcan(a)causethechargetobuild.(b)increase
anddecreasethevoltage.(c)causethecurrenttochangedirection.(d)stopandstarttheflowofcurrent.
A:Thefunctionofaswitchistostartandstoptheflowofacurrent.Theansweris(d).
Table16: Few-shotexemplarsforHotpotQA(closed-booksetting).
Q:WhichmagazinewasstartedfirstArthur’sMagazineorFirstforWomen?
A:Arthur’sMagazinestartedin1844.FirstforWomenstartedin1989.SoArthur’sMagazinewasstartedfirst.
TheanswerisArthur’sMagazine.
Q:TheOberoifamilyispartofahotelcompanythathasaheadofficeinwhatcity?
A:TheOberoifamilyispartofthehotelcompanycalledTheOberoiGroup. TheOberoiGrouphasitshead
officeinDelhi.TheanswerisDelhi.
Q:WhatnationalitywasJamesHenryMiller’swife?
A:JamesHenryMiller’swifeisJuneMiller.JuneMillerisanAmerican.TheanswerisAmerican.
Q:TheDutch-Belgiantelevisionseriesthat"HouseofAnubis"wasbasedonfirstairedinwhatyear?
A:"HouseofAnubis"isbasedontheDutch–BelgiantelevisionseriesHetHuisAnubis.HetHuisAnubisisfirst
airedinSeptember2006.Theansweris2006.
Asadditionalinformation,wealsolisttheexactsetofpromptsusedforallarithmeticreasoningtasks
inTable17,sincetherearemultiplesetsofpromptsintroducedinWeietal.(2022). Thepromptsfor
CommonsenseQAandStrategyQAarethesameasusedinWeietal.(2022).
WeprovidetheexactpromptsusedforcommonNLPtasksinthefollowingtablesaswell,including
NLI(Table18,Table19,Table20)andClosed-BookQuestion-Answeringtasks(Table16,Table21).
20

PublishedasaconferencepaperatICLR2023
Table17: Few-shotexemplarsforallarithmeticreasoningtasks,fromWeietal.(2022).
Q:Thereare15treesinthegrove.Groveworkerswillplanttreesinthegrovetoday.Aftertheyaredone,
therewillbe21trees.Howmanytreesdidthegroveworkersplanttoday?
A:Westartwith15trees.Laterwehave21trees.Thedifferencemustbethenumberoftreestheyplanted.
So,theymusthaveplanted21-15=6trees.Theansweris6.
Q:Ifthereare3carsintheparkinglotand2morecarsarrive,howmanycarsareintheparkinglot?
A:Thereare3carsintheparkinglotalready.2morearrive.Nowthereare3+2=5cars.Theansweris5.
Q:Leahhad32chocolatesandhersisterhad42.Iftheyate35,howmanypiecesdotheyhaveleftintotal?
A: Leah had 32 chocolates and Leah’s sister had 42. That means there were originally 32 + 42 = 74
chocolates.35havebeeneaten.Sointotaltheystillhave74-35=39chocolates.Theansweris39.
Q:Jasonhad20lollipops.HegaveDennysomelollipops.NowJasonhas12lollipops.Howmanylollipops
didJasongivetoDenny?
A:Jasonhad20lollipops.Sinceheonlyhas12now,hemusthavegiventheresttoDenny.Thenumberof
lollipopshehasgiventoDennymusthavebeen20-12=8lollipops.Theansweris8.
Q:Shawnhasfivetoys.ForChristmas,hegottwotoyseachfromhismomanddad.Howmanytoysdoes
hehavenow?
A:Hehas5toys.Hegot2frommom,soafterthathehas5+2=7toys.Thenhegot2morefromdad,so
intotalhehas7+2=9toys.Theansweris9.
Q:Therewereninecomputersintheserverroom. Fivemorecomputerswereinstalledeachday,from
mondaytothursday.Howmanycomputersarenowintheserverroom?
A:Thereare4daysfrommondaytothursday.5computerswereaddedeachday.Thatmeansintotal4*5=
20computerswereadded.Therewere9computersinthebeginning,sonowthereare9+20=29computers.
Theansweris29.
Q:Michaelhad58golfballs.Ontuesday,helost23golfballs.Onwednesday,helost2more.Howmany
golfballsdidhehaveattheendofwednesday?
A: Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On
Wednesdayhelost2moresonowhehas35-2=33balls.Theansweris33.
Q:Oliviahas$23.Sheboughtfivebagelsfor$3each.Howmuchmoneydoesshehaveleft?
A:Shebought5bagelsfor$3each. Thismeansshespent5*$3=$15onthebagels. Shehad$23in
beginning,sonowshehas$23-$15=$8.Theansweris8.
21

PublishedasaconferencepaperatICLR2023
Table18: Few-shotexemplarsforANLI.
Premise:
"Conceptuallycreamskimminghastwobasicdimensions-productandgeography."
Basedonthispremise,canweconcludethehypothesis"Productandgeographyarewhatmakecreamskimming
work."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Basedon"creamskimminghastwobasicdimensions"wecan’tinferthatthesetwodimensionsarewhat
makecreamskimmingwork.Theanswerisitisnotpossibletotell.
Premise:
"Oneofourmemberwillcarryoutyourinstructionsminutely."
Basedonthispremise,canweconcludethehypothesis"Amemberofmyteamwillexecuteyourorderswith
immenseprecision."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:"oneof"meansthesameas"amemberof","carryout"meansthesameas"execute",and"minutely"means
thesameas"immenseprecision".Theanswerisyes.
Premise:
"Funforadultsandchildren."
Basedonthispremise,canweconcludethehypothesis"Funforonlychildren."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:"adultsandchildren"contradicts"onlychildren".Theanswerisno.
Premise:
"HeturnedandsmiledatVrenna."
Basedonthispremise,canweconcludethehypothesis"HesmiledatVrennawhowaswalkingslowlybehind
himwithhermother."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:thepremisedoesnotsayanythingabout"Vrennawaswalking".Theanswerisitisnotpossibletotell.
Premise:
"wellyouseethatontelevisionalso"
Basedonthispremise,canweconcludethehypothesis"Youcanseethatontelevision,aswell."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:"also"and"aswell"meanthesamething.Theanswerisyes.
Premise:
"VrennaandIbothfoughthimandhenearlytookus."
Basedonthispremise,canweconcludethehypothesis"NeitherVrennanormyselfhaveeverfoughthim."is
true?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:"VrennaandIboth"contradicts"neitherVrennanormyself".Theanswerisno.
22

PublishedasaconferencepaperatICLR2023
Table19: Few-shotexemplarsfore-SNLI(therationalesarecrowd-sourcedannotationsfromthe
originaldataset).
Premise:
"Apersononahorsejumpsoverabrokendownairplane."
Basedonthispremise,canweconcludethehypothesis"Apersonistraininghishorseforacompetition."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Thepersonisnotnecessarilytraininghishorse.Theanswerisitisnotpossibletotell.
Premise:
"Apersononahorsejumpsoverabrokendownairplane."
Basedonthispremise,canweconcludethehypothesis"Apersonisatadiner,orderinganomelette."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Onejumpinghorsecannotbeinadinerorderingfood.Theanswerisno.
Premise:
"Apersononahorsejumpsoverabrokendownairplane."
Basedonthispremise,canweconcludethehypothesis"Apersonisoutdoors,onahorse."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Abrokendownairplaneisoutdoors.Theanswerisyes.
Premise:
"Childrensmilingandwavingatcamera."
Basedonthispremise,canweconcludethehypothesis"Theyaresmilingattheirparents."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Justbecausetheyaresmilingandwavingatacameradoesnotimplytheirparentsoranyoneisanyonebehind
it.Theanswerisitisnotpossibletotell.
Premise:
"Childrensmilingandwavingatcamera."
Basedonthispremise,canweconcludethehypothesis"Thekidsarefrowning."istrue?OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Onecannotbesmilingandfrowningatthesametime.Theanswerisno.
Premise:
"Childrensmilingandwavingatcamera."
Basedonthispremise,canweconcludethehypothesis"Therearechildrenpresent."istrue?
OPTIONS:
-yes
-no
-itisnotpossibletotell
A:Thechildrenmustbepresenttoseethemsmilingandwaving.Theanswerisyes.
23

PublishedasaconferencepaperatICLR2023
Table20: Few-shotexemplarsforRTE.
Premise:
"NoWeaponsofMassDestructionFoundinIraqYet."
Basedonthispremise,canweconcludethehypothesis"WeaponsofMassDestructionFoundinIraq."istrue?
A:"NoWeaponsofMassDestructionFound"contradicts"WeaponsofMassDestructionFound".Theansweris
no.
Premise:
"Aplaceofsorrow,afterPopeJohnPaulIIdied,becameaplaceofcelebration,asRomanCatholicfaithful
gatheredindowntownChicagotomarktheinstallationofnewPopeBenedictXVI."
Basedonthispremise,canweconcludethehypothesis"PopeBenedictXVIisthenewleaderoftheRoman
CatholicChurch."istrue?’
A:"installationofnewPopeBenedictXVI."means"PopeBenedictXVIisthenewleader".Theanswerisyes.
Premise:
"Amanisdueincourtlaterchargedwiththemurder26yearsagoofateenagerwhosecasewasthefirstto
befeaturedonBBCOne’sCrimewatch.ColetteAram,16,waswalkingtoherboyfriend’shouseinKeyworth,
Nottinghamshire,on30October1983whenshedisappeared.Herbodywaslaterfoundinafieldclosetoher
home.PaulStewartHutchinson,50,hasbeenchargedwithmurderandisduebeforeNottinghammagistrates
later."
Basedonthispremise,canweconcludethehypothesis"PaulStewartHutchinsonisaccusedofhavingstabbeda
girl."istrue?
A:ThepremisedoesnotsayPaulStewartHutchinson"stabbed"thisgirl.Theanswerisno.
Premise:
"Herceptinwasalreadyapprovedtotreatthesickestbreastcancerpatients,andthecompanysaid,Monday,it
willdiscusswithfederalregulatorsthepossibilityofprescribingthedrugformorebreastcancerpatients."
Basedonthispremise,canweconcludethehypothesis"Herceptincanbeusedtotreatbreastcancer."istrue?
A:"Herceptinwasapprovedtotreatbreastcancer"impliesthat"Herceptincanbeusedtotreatbreastcancer".
Theanswerisyes.
Table21: Few-shotexemplarsforBoolQ(closed-booksetting).
Q:doessystemofadownhave2singers?
A:SystemofaDowncurrentlyconsistsofSerjTankian,DaronMalakian,ShavoOdadjianandJohnDolmayan.
SerjandDarondovocals,sothebanddoeshavetwosingers.Theanswerisyes.
Q:doiranandafghanistanspeakthesamelanguage?
A:IranandAfghanistanbothspeaktheIndo-EuropeanlanguagePersian.Theanswerisyes.
Q:isacelloandabassthesamething?
A:Thecelloisplayedsittingdownwiththeinstrumentbetweentheknees,whereasthedoublebassisplayed
standingorsittingonastool.Theanswerisno.
Q:canyouuseoystercardatepsomstation?
A:EpsomrailwaystationservesthetownofEpsominSurreyandisnotintheLondonOystercardzone.The
answerisno.
24
