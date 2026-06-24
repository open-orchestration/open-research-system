ColBERT: Efficient and Effective Passage Search via
Contextualized Late Interaction over BERT
OmarKhattab MateiZaharia
StanfordUniversity StanfordUniversity
okhattab@stanford.edu matei@cs.stanford.edu
ABSTRACT
105
RecentprogressinNaturalLanguageUnderstanding(NLU)isdriv-
ingfast-pacedadvancesinInformationRetrieval(IR),largelyowed 104
tofine-tuningdeeplanguagemodels(LMs)fordocumentranking.
Whileremarkablyeffective,therankingmodelsbasedontheseLMs 103
increasecomputationalcostbyordersofmagnitudeoverpriorap-
proaches,particularlyastheymustfeedeachquery–documentpair 102
throughamassiveneuralnetworktocomputeasinglerelevance
score.Totacklethis,wepresentColBERT,anovelrankingmodel 101
thatadaptsdeepLMs(inparticular,BERT)forefficientretrieval. 0.15 0.20 0.25 0.30 0.35 0.40
MRR@10
ColBERTintroducesalateinteractionarchitecturethatindepen-
dentlyencodesthequeryandthedocumentusingBERTandthen
employsacheapyetpowerfulinteractionstepthatmodelstheir
fine-grained similarity. By delaying and yet retaining this fine-
granularinteraction,ColBERTcanleveragetheexpressivenessof
deepLMswhilesimultaneouslygainingtheabilitytopre-compute
documentrepresentationsoffline,considerablyspeedingupquery
processing.Beyondreducingthecostofre-rankingthedocuments
retrievedbyatraditionalmodel,ColBERT’spruning-friendly in-
teractionmechanismenablesleveragingvector-similarityindexes
forend-to-endretrievaldirectlyfromalargedocumentcollection.
WeextensivelyevaluateColBERTusingtworecentpassagesearch
datasets.ResultsshowthatColBERT’seffectivenessiscompetitive
with existing BERT-based models (and outperforms every non-
BERTbaseline),whileexecutingtwoorders-of-magnitudefaster
andrequiringfourorders-of-magnitudefewerFLOPsperquery.
ACMReferenceformat:
OmarKhattabandMateiZaharia.2020.ColBERT:EfficientandEffectivePas-
sageSearchviaContextualizedLateInteractionoverBERT.InProceedings
ofProceedingsofthe43rdInternationalACMSIGIRConferenceonResearch
andDevelopmentinInformationRetrieval,VirtualEvent,China,July25–30,
2020(SIGIR’20),10pages.
DOI:10.1145/3397271.3401075
1 INTRODUCTION
Overthepastfewyears,theInformationRetrieval(IR)community
haswitnessedtheintroductionofahostofneuralrankingmodels,
includingDRMM[7],KNRM[4,36],andDuet[20,22].Incontrast
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org.
SIGIR’20,VirtualEvent,China
©2020Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
978-1-4503-8016-4/20/07...$15.00
DOI:10.1145/3397271.3401075
)sm(
ycnetaL
yreuQ
Bag-of-Words (BoW) Model
BoW Model with NLU Augmentation
Neural Matching Model BERT-large
Deep Language Model
BERT-base ColBERT (ours)
ColBERT (full retrieval)
Duet fT+ConvKNRM
BM25 KNRMdoc2queryDeepC do T cTTTTTquery ColBERT (re-rank)
Figure 1: Effectiveness (MRR@10) versus Mean Query La-
tency (log-scale) for a number of representative ranking
modelsonMSMARCORanking[24].Thefigurealsoshows
ColBERT.Neuralre-rankersrunontopoftheofficialBM25
top-1000resultsanduseaTeslaV100GPU.Methodologyand
detailedresultsarein§4.
topriorlearning-to-rankmethodsthatrelyonhand-craftedfea-
tures,thesemodelsemployembedding-basedrepresentationsof
queriesanddocumentsanddirectlymodellocalinteractions(i.e.,
fine-granularrelationships)betweentheircontents.Amongthem,
arecentapproachhasemergedthatfine-tunes deeppre-trained
languagemodels(LMs)likeELMo[29]andBERT[5]forestimating
relevance. Bycomputingdeeply-contextualizedsemanticrepre-
sentationsofquery–documentpairs,theseLMshelpbridgethe
pervasivevocabularymismatch[21,42]betweendocumentsand
queries[30]. Indeed,inthespanofjustafewmonths,anumber
ofrankingmodelsbasedonBERThaveachievedstate-of-the-art
resultsonvariousretrievalbenchmarks[3,18,25,39]andhave
beenproprietarilyadaptedfordeploymentbyGoogle1andBing2.
However,theremarkablegainsdeliveredbytheseLMscome
atasteepincreaseincomputationalcost.Hofsta¨tteretal.[9]and
MacAvaneyetal.[18]observethatBERT-basedmodelsinthelit-
eratureare100-1000×morecomputationallyexpensivethanprior
models—someofwhicharearguablynotinexpensivetobeginwith
[13].Thisquality–costtradeoffissummarizedbyFigure1,which
comparestwoBERT-basedrankers[25,27]againstarepresentative
setofrankingmodels.ThefigureusesMSMARCORanking[24],
a recent collection of 9M passages and 1M queries from Bing’s
logs. Itreportsretrievaleffectiveness(MRR@10)ontheofficial
validationsetaswellasaveragequerylatency(log-scale)usinga
high-endserverthatdedicatesoneTeslaV100GPUperqueryfor
neuralre-rankers.Followingthere-rankingsetupofMSMARCO,
ColBERT(re-rank),theNeuralMatchingModels,andtheDeepLMs
re-ranktheMSMARCO’sofficialtop-1000documentsperquery.
1https://blog.google/products/search/search-language-understanding-bert/
2https://azure.microsoft.com/en-us/blog/bing-delivers-its-largest-improvement-
in-search-experience-using-azure-gpus/
0202
nuJ
4
]RI.sc[
2v23821.4002:viXra

s s
MLP ∑
CNN / Match Kernels / MLP
CNN / Match Kernels
MaxSim MaxSim MaxSim
Query Query Document
tnemucoD
s s
Query Document Query Document
(a) Representation-based Similarity (b) Query-Document Interaction (c) All-to-all Interaction (d) Late Interaction
(e.g., DSSM, SNRM) (e.g., DRMM, KNRM, Conv-KNRM) (e.g., BERT) (i.e., the proposed ColBERT)
Figure2: Schematicdiagramsillustratingquery–documentmatchingparadigmsinneuralIR.Thefigurecontrastsexisting
approaches(sub-figures(a),(b),and(c))withtheproposedlateinteractionparadigm(sub-figure(d)).
Othermethods,includingColBERT(fullretrieval),directlyretrieve Theseincreasinglyexpressivearchitecturesareintension.While
thetop-1000resultsfromtheentirecollection. interaction-basedmodels(i.e.,Figure2(b)and(c))tendtobesu-
Asthefigureshows,BERTconsiderablyimprovessearchpreci- periorforIRtasks[8,21],arepresentation-focusedmodel—byiso-
sion,raisingMRR@10byalmost7%againstthebestpreviousmeth- latingthecomputationsamongqandd—makesitpossibletopre-
ods;simultaneously,itincreaseslatencybyuptotensofthousands computedocumentrepresentationsoffline[41],greatlyreducing
ofmillisecondsevenwithahigh-endGPU.Thisposesachallenging thecomputationalloadperquery. Inthiswork,weobservethat
tradeoffsinceraisingqueryresponsetimesbyaslittleas100msis thefine-grainedmatchingofinteraction-basedmodelsandthepre-
knowntoimpactuserexperienceandevenmeasurablydiminish computationofdocumentrepresentationsofrepresentation-based
revenue[17].Totacklethisproblem,recentworkhasstartedex- modelscanbecombinedbyretainingyetjudiciouslydelayingthe
ploringusingNaturalLanguageUnderstanding(NLU)techniques query–documentinteraction. Figure2(d)illustratesanarchitec-
toaugmenttraditionalretrievalmodelslikeBM25[32].Forexam- turethatpreciselydoesso.Asillustrated,everyqueryembedding
ple,Nogueiraetal.[26,28]expanddocumentswithNLU-generated interactswithalldocumentembeddingsviaaMaxSimoperator,
queriesbeforeindexingwithBM25scoresandDai&Callan[2]re- whichcomputesmaximumsimilarity(e.g.,cosinesimilarity),and
placeBM25’stermfrequencywithNLU-estimatedtermimportance. the scalar outputs of these operators are summed across query
Despitesuccessfullyreducinglatency,theseapproachesgenerally terms. ThisparadigmallowsColBERTtoexploitdeepLM-based
reduceprecisionsubstantiallyrelativetoBERT. representationswhileshiftingthecostofencodingdocumentsof-
ToreconcileefficiencyandcontextualizationinIR,wepropose flineandamortizingthecostofencodingthequeryonceacross
ColBERT,arankingmodelbasedoncontextualizedlateinterac- allrankeddocuments.Additionally,itenablesColBERTtolever-
tionoverBERT.Asthenamesuggests,ColBERTproposesanovel agevector-similaritysearchindexes(e.g.,[1,15])toretrievethe
lateinteractionparadigmforestimatingrelevancebetweenaquery top-k resultsdirectlyfromalargedocumentcollection,substan-
qandadocumentd.Underlateinteraction,qanddareseparately tiallyimprovingrecallovermodelsthatonlyre-ranktheoutputof
encodedintotwosetsofcontextualembeddings,andrelevanceis term-basedretrieval.
evaluatedusingcheapandpruning-friendlycomputationsbetween AsFigure1illustrates, ColBERTcanservequeriesintensor
bothsets—thatis,fastcomputationsthatenablerankingwithout few hundreds of milliseconds. For instance, when used for re-
exhaustivelyevaluatingeverypossiblecandidate. rankingasin“ColBERT(re-rank)”,itdeliversover170×speedup
Figure2contrastsourproposedlateinteractionapproachwith (andrequires14,000×fewerFLOPs)relativetoexistingBERT-based
existingneuralmatchingparadigms.Ontheleft,Figure2(a)illus- models,whilebeingmoreeffectivethaneverynon-BERTbaseline
tratesrepresentation-focusedrankers,whichindependentlycompute (§4.2&4.3). ColBERT’sindexing—theonlytimeitneedstofeed
anembeddingforqandanotherford andestimaterelevanceas documentsthroughBERT—isalsopractical: itcanindextheMS
asinglesimilarityscorebetweentwovectors[12,41].Movingto MARCOcollectionof9Mpassagesinabout3hoursusingasingle
theright,Figure2(b)visualizestypicalinteraction-focusedrankers. serverwithfourGPUs(§4.5),retainingitseffectivenesswithaspace
Insteadofsummarizingqanddintoindividualembeddings,these footprintofaslittleasfewtensofGiBs. Ourextensiveablation
rankersmodelword-andphrase-levelrelationshipsacrossqandd study (§4.4) shows that late interaction, its implementation via
andmatchthemusingadeepneuralnetwork(e.g.,withCNNs/MLPs MaxSimoperations,andcrucialdesignchoiceswithinourBERT-
[22]orkernels[36]).Inthesimplestcase,theyfeedtheneuralnet- basedencodersareallessentialtoColBERT’seffectiveness.
work an interaction matrix that reflects the similiarity between Ourmaincontributionsareasfollows.
everypairofwordsacrossqandd.Furtherright,Figure2(c)illus-
(1) Weproposelateinteraction(§3.1)asaparadigmforefficient
tratesamorepowerfulinteraction-basedparadigm,whichmodels
andeffectiveneuralranking.
theinteractionsbetweenwordswithinaswellasacrossqanddat
(2) WepresentColBERT(§3.2&3.3),ahighly-effectivemodel
thesametime,asinBERT’stransformerarchitecture[25].
thatemploysnovelBERT-basedqueryanddocumenten-
coderswithinthelateinteractionparadigm.

(3) WeshowhowtoleverageColBERTbothforre-rankingon
score
topofaterm-basedretrievalmodel(§3.5)andforsearching
afullcollectionusingvectorsimilarityindexes(§3.6).
(4) WeevaluateColBERTonMSMARCOandTRECCAR,two
MaxSim MaxSim MaxSim
recentpassagesearchcollections.
Query Encoder, f Document Encoder, f
2 RELATEDWORK Q D
NeuralMatchingModels.Overthepastfewyears,IRresearchers
haveintroducednumerousneuralarchitecturesforranking. In
Query Document
thiswork,wecompareagainstKNRM[4,36],Duet[20,22],Con-
vKNRM [4], and fastText+ConvKNRM [10]. KNRM proposes a
differentiablekernel-poolingtechniqueforextractingmatching
signalsfromaninteractionmatrix,whileDuetcombinessignals
fromexact-match-basedaswellasembedding-basedsimilarities
forranking. Introducedin2018,ConvKNRMlearnstomatchn-
gramsinthequeryandthedocument.Lastly,fastText+ConvKNRM
(abbreviatedfT+ConvKNRM)tacklestheabsenceofrarewords
fromtypicalwordembeddingslistsbyadoptingsub-wordtoken
embeddings.
In2018,Zamanietal.[41]introducedSNRM,arepresentation-
focusedIRmodelthatencodeseachqueryandeachdocumentas
asingle,sparsehigh-dimensionalvectorof“latentterms”.Bypro-
ducingasparse-vectorrepresentationforeachdocument,SNRM
isabletouseatraditionalIRinvertedindexforrepresentingdocu-
ments,allowingfastend-to-endretrieval.Despitehighlypromising
resultsandinsights,SNRM’seffectivenessissubstantiallyoutper-
formedbythestateoftheartonthedatasetswithwhichitwas
evaluated(e.g.,see[18,38]).WhileSNRMemployssparsitytoal-
lowusinginvertedindexes,werelaxthisassumptionandcompare
a(dense)BERT-basedrepresentation-focusedmodelagainstour
late-interactionColBERTinourablationexperimentsin§4.4.Fora
detailedoverviewofexistingneuralrankingmodels,wereferthe
readerstotworecentsurveysoftheliterature[8,21].
Language Model Pretraining for IR. Recent work in NLU
emphasizestheimportancepre-traininglanguagerepresentation
modelsinanunsupervisedfashionbeforesubsequentlyfine-tuning
themondownstreamtasks.AnotableexampleisBERT[5],abi-
directionaltransformer-basedlanguagemodelwhosefine-tuning
advancedthestateoftheartonvariousNLUbenchmarks.Nogueiraet
al.[25],MacAvaneyetal.[18],andDai&Callan[3]investigate
incorporatingsuchLMs(mainlyBERT,butalsoELMo[29])ondif-
ferentrankingdatasets.AsillustratedinFigure2(c),thecommon
approach(andtheoneadoptedbyNogueiraetal.onMSMARCO
andTRECCAR)istofeedthequery–documentpairthroughBERT
anduseanMLPontopofBERT’s[CLS]outputtokentoproducea
relevancescore.SubsequentworkbyNogueiraetal.[27]introduced
duoBERT,whichfine-tunesBERTtocomparetherelevanceofa
pairofdocumentsgivenaquery.Relativetotheirsingle-document
BERT,thisgivesduoBERTa1%MRR@10advantageonMSMARCO
whileincreasingthecostbyatleast1.4×.
BERT Optimizations. As discussed in §1, these LM-based
rankerscanbehighlyexpensiveinpractice. Whileongoingef-
fortsintheNLUliteraturefordistilling[14,33],compressing[40],
andpruning[19]BERTcanbeinstrumentalinnarrowingthisgap,
gnixednI
enilffO
Figure3:ThegeneralarchitectureofColBERTgivenaquery
qandadocumentd.
theygenerallyachievesignificantlysmallerspeedupsthanourre-
designedarchitectureforIR,duetotheirgenericnature,andmore
aggressiveoptimizationsoftencomeatthecostoflowerquality.
EfficientNLU-basedModels. Recently,adirectionemerged
thatemploysexpensiveNLUcomputationoffline. Thisincludes
doc2query[28]andDeepCT[2]. Thedoc2querymodelexpands
eachdocumentwithapre-definednumberofsyntheticqueries
queriesgeneratedbyaseq2seqtransformermodelthatistrainedto
generatequeriesgivenadocument.ItthenreliesonaBM25index
forretrievalfromthe(expanded)documents.DeepCTusesBERT
toproducethetermfrequencycomponentofBM25inacontext-
awaremanner,essentiallyrepresentingafeasiblerealizationofthe
term-independenceassumptionwithneuralnetworks[23].Lastly,
docTTTTTquery[26]isidenticaltodoc2queryexceptthatitfine-
tunes a pre-trained model (namely, T5 [31]) for generating the
predictedqueries.
Concurrentlywithourdraftingofthispaper,Hofsta¨tteretal.[11]
publishedtheirTransformer-Kernel(TK)model.Atahighlevel,TK
improvestheKNRMarchitecturedescribedearlier:whileKNRM
employskernelpoolingontopofword-embedding-basedinter-
action,TKusesaTransformer[34]componentforcontextually
encodingqueriesanddocumentsbeforekernelpooling.TKestab-
lishesanewstate-of-the-artfornon-BERTmodelsonMSMARCO
(Dev);however,thebestnon-ensembleMRR@10itachievesis31%
whileColBERTreachesupto36%.Moreover,duetoindexingdocu-
mentrepresentationsofflineandemployingaMaxSim-basedlate
interactionmechanism,ColBERTismuchmorescalable,enabling
end-to-endretrievalwhichisnotsupportedbyTK.
3 COLBERT
ColBERTprescribesasimpleframeworkforbalancingthequality
andcostofneuralIR,particularlydeeplanguagemodelslikeBERT.
Asintroducedearlier,delayingthequery–documentinteractioncan
facilitatecheapneuralre-ranking(i.e.,throughpre-computation)
andevensupportpracticalend-to-endneuralretrieval(i.e.,through
pruningviavector-similaritysearch).ColBERTaddresseshowto
do so while still preserving the effectiveness of state-of-the-art
models, whichconditionthebulkoftheircomputationsonthe
jointquery–documentpair.

EventhoughColBERT’slate-interactionframeworkcanbeap- deeptransformerarchitecture,whichcomputesacontextualized
pliedtoawidevarietyofarchitectures(e.g.,CNNs,RNNs,trans- representationofeachtoken.
formers,etc.),wechoosetofocusthisworkonbi-directionaltransformer- Wedenotethepaddingwithmaskedtokensasqueryaugmen-
basedencoders(i.e.,BERT)owingtotheirstate-of-the-arteffective- tation,astepthatallowsBERTtoproducequery-basedembeddings
nessyetveryhighcomputationalcost. atthepositionscorrespondingtothesemasks.Queryaugmentation
isintendedtoserveasasoft,differentiablemechanismforlearning
toexpandquerieswithnewtermsortore-weighexistingterms
3.1 Architecture
basedontheirimportanceformatchingthequery.Asweshowin
Figure3depictsthegeneralarchitectureofColBERT,whichcom- §4.4,thisoperationisessentialforColBERT’seffectiveness.
prises:(a)aqueryencoderfQ ,(b)adocumentencoderfD ,and(c) GivenBERT’srepresentationofeachtoken,ourencoderpasses
thelateinteractionmechanism.Givenaqueryqanddocumentd, thecontextualizedoutputrepresentationsthroughalinearlayer
fQ encodesqintoabagoffixed-sizeembeddingsEq whilefD en- withnoactivations. Thislayerservestocontrolthedimension
codesdintoanotherbagE
d
.Crucially,eachembeddingsinEq and ofColBERT’sembeddings,producingm-dimensionalembeddings
E iscontextualizedbasedontheothertermsinqord,respectively. forthelayer’soutputsizem. Aswediscusslaterinmoredetail,
d
WedescribeourBERT-basedencodersin§3.2. wetypicallyfixmtobemuchsmallerthanBERT’sfixedhidden
UsingEq andE
d
, ColBERTcomputestherelevancescorebe- dimension.
tweenqanddvialateinteraction,whichwedefineasasummation WhileColBERT’sembeddingdimensionhaslimitedimpacton
ofmaximumsimilarity(MaxSim)operators.Inparticular,wefind theefficiencyofqueryencoding,thisstepiscrucialforcontrolling
themaximumcosinesimilarityofeachv ∈Eq withvectorsinE
d
, thespacefootprintofdocuments,asweshowin§4.5.Inaddition,it
andcombinetheoutputsviasummation.Besidescosine,wealso canhaveasignificantimpactonqueryexecutiontime,particularly
evaluatesquaredL2distanceasameasureofvectorsimilarity.In- thetimetakenfortransferringthedocumentrepresentationsonto
tuitively,thisinteractionmechanismsoftlysearchesforeachquery theGPUfromsystemmemory(wheretheyresidebeforeprocessing
termtq —inamannerthatreflectsitscontextinthequery—against a query). In fact, as we show in §4.2, gathering, stacking, and
thedocument’sembeddings,quantifyingthestrengthofthe“match” transferringtheembeddingsfromCPUtoGPUcanbethemost
viathelargestsimilarityscorebetweentq andadocumenttermt
d
. expensivestepinre-rankingwithColBERT.Finally, theoutput
Giventhesetermscores,itthenestimatesthedocumentrelevance embeddings are normalized so each has L2 norm equal to one.
bysummingthematchingevidenceacrossallqueryterms. Theresultisthatthedot-productofanytwoembeddingsbecomes
Whilemoresophisticatedmatchingispossiblewithotherchoices equivalenttotheircosinesimilarity,fallinginthe[−1,1]range.
suchasdeepconvolutionandattentionlayers(i.e.,asintypical DocumentEncoder.Ourdocumentencoderhasaverysimilar
interaction-focusedmodels),asummationofmaximumsimilarity architecture.Wefirstsegmentadocumentdintoitsconstituentto-
computationshastwodistinctivecharacteristics. First,itstands kensd1d2...dm ,towhichweprependBERT’sstarttoken[CLS]fol-
outasaparticularlycheapinteractionmechanism,asweexamine lowedbyourspecialtoken[D]thatindicatesadocumentsequence.
itsFLOPsin§4.2. Second,andmoreimportantly,itisamenable Unlikequeries,wedonotappend[mask]tokenstodocuments.Af-
tohighly-efficientpruningfortop-k retrieval,asweevaluatein terpassingthisinputsequencethroughBERTandthesubsequent
§4.3.Thisenablesusingvector-similarityalgorithmsforskipping linearlayer,thedocumentencoderfiltersouttheembeddingscorre-
documentswithoutmaterializingthefullinteractionmatrixoreven spondingtopunctuationsymbols,determinedviaapre-definedlist.
consideringeachdocumentinisolation.Othercheapchoices(e.g., Thisfilteringismeanttoreducethenumberofembeddingsperdoc-
asummationofaveragesimilarityscores,insteadofmaximum)are ument,aswehypothesizethat(evencontextualized)embeddings
possible;however,manyarelessamenabletopruning.In§4.4,we ofpunctuationareunnecessaryforeffectiveness.
conductanextensiveablationstudythatempiricallyverifiesthead- Insummary,givenq=q0q1...q
l
andd =d0d1...dn ,wecompute
vantageofourMaxSim-basedlateinteractionagainstalternatives. thebagsofembeddingsEq andE
d
inthefollowingmanner,where
#referstothe[mask]tokens:
3.2 Query&DocumentEncoders
Priortolateinteraction,ColBERTencodeseachqueryordocument
intoabagofembeddings,employingBERT-basedencoders. We
Eq :=Normalize(CNN(BERT(“[Q]q0q1...q
l
##...#”))) (1)
shareasingleBERTmodelamongourqueryanddocumenten- E d :=Filter(Normalize(CNN(BERT(“[D]d0d1...dn ”)))) (2)
codersbutdistinguishinputsequencesthatcorrespondtoqueries
anddocumentsbyprependingaspecialtoken[Q]toqueriesand
3.3 LateInteraction
anothertoken[D]todocuments.
QueryEncoder.Givenatextualqueryq,wetokenizeitintoits Giventherepresentationofaqueryqandadocumentd,therel-
BERT-basedWordPiece[35]tokensq1q2...q
l
.Weprependthetoken evancescoreofd toq, denotedasS
q,d
, isestimatedvialatein-
[Q]tothequery.WeplacethistokenrightafterBERT’ssequence- teractionbetweentheirbagsofcontextualizedembeddings. As
starttoken[CLS].Ifthequeryhasfewerthanapre-definednumber mentionedbefore, thisisconductedasasumofmaximumsim-
of tokens Nq , we pad it with BERT’s special [mask] tokens up ilarity computations, namely cosine similarity (implemented as
to length Nq (otherwise, we truncate it to the first Nq tokens). dot-productsduetotheembeddingnormalization)orsquaredL2
ThispaddedsequenceofinputtokensisthenpassedintoBERT’s distance.

(unlikeourapproachin§3.6).Tobeginwith,ourqueryservingsub-
systemloadstheindexeddocumentsrepresentationsintomemory,
|     |     | :=  | (cid:213) | m a x | ·ET |     | (3) |     |     |     |     |     |     |
| --- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S q,d Eqi rep re se n ti n g e a c h d o c um e nt a s a m a tr i x o f e m b e d d in g s .
|     |     |     |     | j∈ [| E | |] dj |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
i∈[|Eq |] d G iv e n a q u e r y , w e co m p u te i ts b a g o f c o n te x t u al i z edembed-
q
ColBERTisdifferentiableend-to-end. Wefine-tunetheBERT dingsEq (Equation1)and,concurrently,gatherthedocumentrepre-
encodersandtrainfromscratchtheadditionalparameters(i.e.,the sentationsintoa3-dimensionaltensorDconsistingofkdocument
linearlayerandthe[Q]and[D]markers’embeddings)usingthe matrices. Wepadthek documentstotheirmaximumlengthto
facilitatebatchedoperations,andmovethetensorDtotheGPU’s
Adam[16]optimizer.Noticethatourinteractionmechanismhas
|                        |     |     |                          |     | +                       |     |     | memory.OntheGPU,wecomputeabatchdot-productofEq |     |     |     |     | and |
| ---------------------- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| notrainableparameters. |     |     | Givenatriple(cid:104)q,d |     | ,d−(cid:105)withqueryq, |     |     |                                                |     |     |     |     |     |
D,possiblyovermultiplemini-batches.Theoutputmaterializesa
| positivedocumentd |     | +andnegativedocumentd−,ColBERTisused |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toproduceascoreforeachdocumentindividuallyandisoptimized 3-dimensionaltensorthatisacollectionofcross-matchmatrices
viapairwisesoftmaxcross-entropylossoverthecomputedscores betweenqandeachdocument.Tocomputethescoreofeachdocu-
ofd +andd−. ment,wereduceitsmatrixacrossdocumenttermsviaamax-pool
(i.e.,representinganexhaustiveimplementationofourMaxSim
computation)andreduceacrossquerytermsviaasummation.Fi-
| 3.4 OfflineIndexing: |     |     |     | Computing&Storing |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DocumentEmbeddings nally,wesortthekdocumentsbytheirtotalscores.
|     |     |     |     |     |     |     |     | Relative | to existing | neural | rankers | (especially, | but not exclu- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ------- | ------------ | -------------- |
Bydesign,ColBERTisolatesalmostallofthecomputationsbetween
sively,BERT-basedones),thiscomputationisverycheapthat,in
queriesanddocuments,largelytoenablepre-computingdocument fact,itscostisdominatedbythecostofgatheringandtransferring
representationsoffline.Atahighlevel,ourindexingprocedureis thepre-computedembeddings.Toillustrate,rankingkdocuments
straight-forward:weproceedoverthedocumentsinthecollection
viatypicalBERTrankersrequiresfeedingBERTkdifferentinputs
| i n b a tc h e | s ,r u n n | in g ou  | r d o c u m  | e n t e n c | o d e r o n         | e a c h b a | t ch a n d |               |          |                          |     |     |        |
| -------------- | ---------- | -------- | ------------ | ----------- | ------------------- | ----------- | ---------- | ------------- | -------- | ------------------------ | --- | --- | ------ |
|                |            |          |              |             | f D                 |             |            | eachoflengthl | =|q|+|di | |forqueryqanddocumentsdi |     |     | ,where |
| s to r in g t  | h e o u tp | u t em b | ed d i n g s | p e r d o   | c u m e n t .A l th | o u g h i n | d ex i n g |               |          |                          |     |     |        |
attentionhasquadraticcostinthelengthofthesequence.Incon-
| a set of | documents | is  | an offline | process, | we incorporate |     | a few |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | -------- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
trast,ColBERTfeedsBERTonlyasingle,muchshortersequenceof
simpleoptimizationsforenhancingthethroughputofindexing.As lengthl =|q|.Consequently,ColBERTisnotonlycheaper,italso
weshowin§4.5,theseoptimizationscanconsiderablyreducethe
scalesmuchbetterwithkasweexaminein§4.2.
offlinecostofindexing.
Tobeginwith,weexploitmultipleGPUs,ifavailable,forfaster
|     |     |     |     |     |     |     |     | 3.6 End-to-endTop-k |     |     | RetrievalwithColBERT |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------------------- | --- | --- |
encodingofbatchesofdocumentsinparallel.Whenbatching,we
Asmentionedbefore,ColBERT’slate-interactionoperatorisspecifi-
padalldocumentstothemaximumlengthofadocumentwithin
thebatch.3 callydesignedtoenableend-to-endretrievalfromalargecollection,
Tomakecappingthesequencelengthonaper-batch
largelytoimproverecallrelativetoterm-basedretrievalapproaches.
basismoreeffective,ourindexerproceedsthroughdocumentsin
Thissectionisconcernedwithcaseswherethenumberofdocu-
groupsofB(e.g.,B=100,000)documents.Itsortsthesedocuments
mentstoberankedistoolargeforexhaustiveevaluationofeach
| bylengthandthenfeedsbatchesofb(e.g.,b |     |     |     |     | =128)documentsof |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
possiblecandidatedocument,particularlywhenweareonlyinter-
comparablelengththroughourencoder.Thislength-basedbucket-
|     |     |     |     |     |     |     |     | estedinthehighestscoringones. |     |     | Concretely,wefocushereon |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ------------------------ | --- | --- |
ingissometimesreferedtoasaBucketIteratorinsomelibraries
retrievingthetop-kresultsdirectlyfromalargedocumentcollec-
(e.g.,allenNLP).Lastly,whilemostcomputationsoccurontheGPU,
|     |     |     |     |     |     |     |     | tionwithN | (e.g.,N | =10,000,000)documents,wherek |     |     | (cid:28)N. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------------------------- | --- | --- | ---------- |
wefoundthatanon-trivialportionoftheindexingtimeisspenton
Todoso,weleveragethepruning-friendlynatureoftheMaxSim
pre-processingthetextsequences,primarilyBERT’sWordPieceto-
|     |     |     |     |     |     |     |     | operationsatthebackboneoflateinteraction. |     |     |     | Insteadofapply- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --------------- | --- |
kenization.Exploitingthattheseoperationsareindependentacross
ingMaxSimbetweenoneofthequeryembeddingsandallofone
documentsinabatch,weparallelizethepre-processingacrossthe
|     |     |     |     |     |     |     |     | document’s | embeddings, | we  | can use | fast vector-similarity | data |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------- | ---------------------- | ---- |
availableCPUcores.
|     |     |     |     |     |     |     |     | structures | to efficiently | conduct | this | search between | the query |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------- | ---- | -------------- | --------- |
Oncethedocumentrepresentationsareproduced,theyaresaved
|     |     |     |     |     |     |     |     | embeddingandall |     | documentembeddingsacrossthefullcollec- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------------------------------- | --- | --- | --- |
todiskusing32-bitor16-bitvaluestorepresenteachdimension.
Aswedescribein§3.5and3.6, theserepresentationsareeither tion. Forthis,weemployanoff-the-shelflibraryforlarge-scale
vector-similaritysearch,namelyfaiss[15]fromFacebook.4Inpar-
simplyloadedfromdiskforrankingoraresubsequentlyindexed
ticular,attheendofofflineindexing(§3.4),wemaintainamapping
forvector-similaritysearch,respectively.
fromeachembeddingtoitsdocumentoforiginandthenindexall
documentembeddingsintofaiss.
| 3.5 Top-k | Re-rankingwithColBERT |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Subsequently,whenservingqueries,weuseatwo-stagepro-
RecallthatColBERTcanbeusedforre-rankingtheoutputofan-
ceduretoretrievethetop-kdocumentsfromtheentirecollection.
| otherretrievalmodel, |     |     | typicallyaterm-basedmodel, |     |     | ordirectly |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
BothstagesrelyonColBERT’sscoring:thefirstisanapproximate
forend-to-endretrievalfromadocumentcollection. Inthissec- stageaimedatfilteringwhilethesecondisarefinementstage.For
tion,wediscusshowweuseColBERTforrankingasmallsetof thefirststage,weconcurrentlyissueNq vector-similarityqueries
k(e.g.,k =1000)documentsgivenaqueryq.Sincekissmall,we (correspondingtoeachoftheembeddingsinEq )ontoourfaissin-
relyonbatchcomputationstoexhaustivelyscoreeachdocument
dex.Thisretrievesthetop-k(cid:48)(e.g.,k(cid:48)=k/2)matchesforthatvector
3ThepublicBERTimplementationswesawsimplypadtoapre-definedlength. 4https://github.com/facebookresearch/faiss

overalldocumentembeddings.Wemapeachofthosetoitsdocu- sets)asa“local”evaluationset. Alongwiththeofficialdevelop-
mentoforigin,producingNq ×k(cid:48)documentIDs,onlyK ≤Nq ×k(cid:48) mentset,weusethisheld-outsetfortestingourmodelsaswellas
ofwhichareunique.TheseKdocumentslikelycontainoneormore baselinesin§4.3.Wedosotoavoidsubmittingmultiplevariants
embeddingsthatarehighlysimilartothequeryembeddings.For ofthesamemodelatonce,astheorganizersdiscouragetoomany
thesecondstage,werefinethissetbyexhaustivelyre-rankingonly submissionsbythesameteam.
thoseK documentsintheusualmannerdescribedin§3.5. TRECCAR.IntroducedbyDietz[6]etal.in2017,TRECCAR
Inourfaiss-basedimplementation,weuseanIVFPQindex(“in- isasyntheticdatasetbasedonWikipediathatconsistsofabout
vertedfilewithproductquantization”). Thisindexpartitionsthe 29Mpassages.Similartorelatedwork[25],weusethefirstfourof
embeddingspaceintoP(e.g.,P =1000)cellsbasedonk-meansclus- fivepre-definedfoldsfortrainingandthefifthforvalidation.This
teringandthenassignseachdocumentembeddingtoitsnearestcell amountstoroughly3Mqueriesgeneratedbyconcatenatingthe
basedontheselectedvector-similaritymetric.Forservingqueries, titleofaWikipediapagewiththeheadingofoneofitssections.
whensearchingforthetop-k(cid:48)matchesforasinglequeryembed- Thatsection’spassagesaremarkedasrelevanttothecorresponding
ding,onlythenearestp(e.g.,p =10)partitionsaresearched. To query.OurevaluationisconductedonthetestsetusedinTREC
improvememoryefficiency,everyembeddingisdividedintos(e.g., 2017CAR,whichcontains2,254queries.
s = 16)sub-vectors,eachrepresentedusingonebyte. Moreover,
theindexconductsthesimilaritycomputationsinthiscompressed 4.1.2 Implementation. OurColBERTmodelsareimplemented
domain,leadingtocheapercomputationsandthusfastersearch. usingPython3andPyTorch1.Weusethepopulartransformers 5
libraryforthepre-trainedBERTmodel.Similarto[25],wefine-tune
allColBERTmodelswithlearningrate3×10−6withabatchsize
4 EXPERIMENTALEVALUATION 32.WefixthenumberofembeddingsperqueryatNq =32.Weset
WenowturnourattentiontoempiricallytestingColBERT,address-
ourColBERTembeddingdimensionmtobe128;§4.5demonstrates
ColBERT’srobustnesstoawiderangeofembeddingdimensions.
ingthefollowingresearchquestions.
ForMSMARCO,weinitializetheBERTcomponentsoftheCol-
RQ :Inatypicalre-rankingsetup,howwellcanColBERTbridge
1
BERTqueryanddocumentencodersusingGoogle’sofficialpre-
theexistinggap(highlightedin§1)betweenhighly-efficientand
trainedBERT model.Further,wetrainallmodelsfor200kitera-
highly-effectiveneuralmodels?(§4.2) base
tions.ForTRECCAR,wefollowrelatedwork[2,25]anduseadif-
RQ :Beyondre-ranking,canColBERTeffectivelysupportend-
2
ferentpre-trainedmodeltotheofficialones.Toexplain,theofficial
to-endretrievaldirectlyfromalargecollection?(§4.3)
BERTmodelswerepre-trainedonWikipedia,whichisthesource
RQ :WhatdoeseachcomponentofColBERT(e.g.,lateinterac-
3
ofTRECCAR’strainingandtestsets. Toavoidleakingtestdata
tion,queryaugmentation)contributetoitsquality?(§4.4)
intotrain,NogueiraandCho’s[25]pre-trainarandomly-initialized
RQ : WhatareColBERT’sindexing-relatedcostsintermsof
4
BERTmodelontheWikipagescorrespondingtotrainingsubsetof
offlinecomputationandmemoryoverhead?(§4.5)
TRECCAR.TheyreleasetheirBERT pre-trainedmodel,which
large
wefine-tuneforColBERT’sexperimentsonTRECCAR.Sincefine-
4.1 Methodology tuningthismodelissignificantlyslowerthanBERT ,wetrain
base
onTRECCARforonly125kiterations.
4.1.1 Datasets&Metrics. Similartorelatedwork[2,27,28],
Inourre-rankingresults,unlessstatedotherwise,weuse4bytes
we conduct our experiments on the MS MARCO Ranking [24]
perdimensioninourembeddingsandemploycosineasourvector-
(henceforth,MSMARCO)andTRECComplexAnswerRetrieval
similarityfunction.Forend-to-endranking,weuse(squared)L2
(TREC-CAR)[6]datasets. Bothoftheserecentdatasetsprovide
largetrainingdataofthescalethatfacilitatestrainingandevaluat-
distance,aswefoundourfaissindexwasfasteratL2-basedre-
ingdeepneuralnetworks.Wedescribebothindetailbelow.
trieval. Forourfaissindex,wesetthenumberofpartitionsto
MSMARCO.MSMARCOisadataset(andacorresponding P =2,000,andsearchthenearestp=10toeachqueryembeddingto
competition)introducedbyMicrosoftin2016forreadingcompre-
retrievek(cid:48)=k =1000documentvectorsperqueryembedding.We
hensionandadaptedin2018forretrieval.Itisacollectionof8.8M
divideeachembeddingintos =16sub-vectors,eachencodedusing
onebyte.Torepresenttheindexusedforthesecondstageofour
passagesfromWebpages,whichweregatheredfromBing’sresults
end-to-endretrievalprocedure,weuse16-bitvaluesperdimension.
to 1M real-world queries. Each query is associated with sparse
relevancejudgementsofone(orveryfew)documentsmarkedas
4.1.3 Hardware&TimeMeasurements. Toevaluatethelatency
relevantandnodocumentsexplicitlyindicatedasirrelevant.Per
ofneuralre-rankingmodelsin§4.2,weuseasingleTeslaV100GPU
theofficialevaluation,weuseMRR@10tomeasureeffectiveness.
thathas32GiBsofmemoryonaserverwithtwoIntelXeonGold
Weusethreesetsofqueriesforevaluation. Theofficialdevel-
6132CPUs,eachwith14physicalcores(24hyperthreads),and469
opmentandevaluationsetscontainroughly7kqueries.However,
GiBsofRAM.ForthemostlyCPU-basedretrievalexperimentsin
therelevancejudgementsoftheevaluationsetareheld-outbyMi-
§4.3andtheindexingexperimentsin§4.5,weuseanotherserver
crosoftandeffectivenessresultscanonlybeobtainedbysubmitting
withthesameCPUandsystemmemoryspecificationsbutwhich
tothecompetition’sorganizers.Wesubmittedourmainre-ranking
hasfourTitanVGPUsattached, eachwith12GiBsofmemory.
ColBERTmodelfortheresultsin§4.2.Inaddition,thecollection
Acrossallexperiments,onlyoneGPUisdedicatedperqueryfor
includesroughly55kqueries(withlabels)thatareprovidedasad-
ditionalvalidationdata. Were-purposearandomsampleof5k
queriesamongthose(i.e.,onesnotinourdevelopmentortraining 5https://github.com/huggingface/transformers

Method MRR@10(Dev) MRR@10(Eval) Re-rankingLatency(ms) FLOPs/query
| BM25(official) |     |     | 16.7 |     | 16.5 |     | -   | -            |     |
| -------------- | --- | --- | ---- | --- | ---- | --- | --- | ------------ | --- |
| KNRM           |     |     | 19.8 |     | 19.8 |     | 3   | 592M(0.085×) |     |
| Duet           |     |     | 24.3 |     | 24.5 |     | 22  | 159B(23×)    |     |
|                |     |     | 29.0 |     | 27.7 |     | 28  | 78B(11×)     |     |
fastText+ConvKNRM
| BERT [25] |     |     | 34.7 |     | -   |     | 10,700 | 97T(13,900×) |     |
| --------- | --- | --- | ---- | --- | --- | --- | ------ | ------------ | --- |
base
| BERT (ourtraining) |     |     | 36.0 |     | -   |     | 10,700 | 97T(13,900×) |     |
| ------------------ | --- | --- | ---- | --- | --- | --- | ------ | ------------ | --- |
base
| BERT [25] |     |     | 36.5 |     | 35.9 |     | 32,900 | 340T(48,600×) |     |
| --------- | --- | --- | ---- | --- | ---- | --- | ------ | ------------- | --- |
large
| ColBERT(overBERT | )   |     | 34.9 |     | 34.9 |     | 61  | 7B(1×) |     |
| ---------------- | --- | --- | ---- | --- | ---- | --- | --- | ------ | --- |
base
Table 1: “Re-ranking” results on MS MARCO. Each neural model re-ranks the official top-1000 results produced by BM25.
Latencyisreportedforre-rankingonly.Toobtaintheend-to-endlatencyinFigure1,weaddtheBM25latencyfromTable2.
Method MRR@10(Dev) MRR@10(LocalEval) Latency(ms) Recall@50 Recall@200 Recall@1000
| BM25(official)    |     | 16.7 |     |     | -    | -        | -     | -     | 81.4  |
| ----------------- | --- | ---- | --- | --- | ---- | -------- | ----- | ----- | ----- |
| BM25(Anserini)    |     | 18.7 |     |     | 19.5 | 62       | 59.2  | 73.8  | 85.7  |
| doc2query         |     | 21.5 |     |     | 22.8 | 85       | 64.4  | 77.9  | 89.1  |
| DeepCT            |     | 24.3 |     |     | -    | 62(est.) | 69[2] | 82[2] | 91[2] |
| docTTTTTquery     |     | 27.7 |     |     | 28.4 | 87       | 75.6  | 86.9  | 94.7  |
| ColBERT (re-rank) |     | 34.8 |     |     | 36.4 | -        | 75.3  | 80.5  | 81.4  |
L2
| ColBERT (end-to-end) |     | 36.0 |     |     | 36.7 | 458 | 82.9 | 92.3 | 96.8 |
| -------------------- | --- | ---- | --- | --- | ---- | --- | ---- | ---- | ---- |
L2
Table2:End-to-endretrievalresultsonMSMARCO.Eachmodelretrievesthetop-1000documentsperquerydirectlyfromthe
entire8.8Mdocumentcollection.
retrieval(i.e.,formethodswithneuralcomputations)butweuse documentsonline,leavingonlyanegligiblecost.Weestimatethe
uptoallfourGPUsduringindexing. FLOPsperqueryofeachmodelusingthetorchprofile6library.
Wenowproceedtostudytheresults,whicharereportedinTa-
|     |     |     |     |     |     | ble1. Tobeginwith,wenoticethefastprogressfromKNRMin |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
2017totheBERT-basedmodelsin2019,manifestingitselfinover
| 4.2 Quality–CostTradeoff: |     | Top-k | Re-ranking |     |     |                      |     |                                 |     |
| ------------------------- | --- | ----- | ---------- | --- | --- | -------------------- | --- | ------------------------------- | --- |
|                           |     |       |            |     |     | 16%increaseinMRR@10. |     | Asdescribedin§1,thesimultaneous |     |
Inthissection,weexamineColBERT’sefficiencyandeffectiveness increaseincomputationalcostisdifficulttomiss.Judgingbytheir
atre-rankingthetop-kresultsextractedbyabag-of-wordsretrieval
rathermonotonicpatternofincreasinglylargercostandhigheref-
model,whichisthemosttypicalsettingfortestinganddeploying
fectiveness,theseresultsappeartopaintapicturewhereexpensive
neuralrankingmodels.WebeginwiththeMSMARCOdataset.We modelsarenecessaryforhigh-qualityranking.
compareagainstKNRM,Duet,andfastText+ConvKNRM,arepre- Incontrastwiththistrend,ColBERT(whichemployslateinter-
sentativesetofneuralmatchingmodelsthathavebeenpreviously actionoverBERT )performsnoworsethantheoriginaladap-
base
testedonMSMARCO.Inaddition,wecompareagainstthenat-
|     |     |     |     |     |     | tationofBERT | base forrankingbyNogueiraandCho[25,27]and |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ----------------------------------------- | --- | --- |
uraladaptationofBERTforrankingbyNogueiraandCho[25],
|     |     |     |     |     |     | isonlymarginallylesseffectivethanBERT |     |     | large andourtraining |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | -------------------- |
inparticular,BERT base anditsdeepercounterpartBERT large .We ofBERT (describedabove).Whilehighlycompetitiveineffec-
base
alsoreportresultsfor“BERT (ourtraining)”,whichisbasedon tiveness,ColBERTisordersofmagnitudecheaperthanBERT ,
base base
NogueiraandCho’sbasemodel(includinghyperparameters)but inparticular,byover170×inlatencyand13,900×inFLOPs.This
istrainedwiththesamelossfunctionasColBERT(§3.3)for200k highlightstheexpressivenessofourproposedlateinteractionmech-
iterations,allowingforamoredirectcomparisonoftheresults.
anism,particularlywhencoupledwithapowerfulpre-trainedLM
Wereportthecompetition’sofficialmetric,namelyMRR@10, likeBERT.WhileColBERT’sre-rankinglatencyisslightlyhigher
onthevalidationset(Dev)andtheevaluationset(Eval).Wealso thanthenon-BERTre-rankingmodelsshown(i.e.,by10sofmil-
reportthere-rankinglatency,whichwemeasureusingasingle liseconds),thisdifferenceisexplainedbythetimeittakestogather,
TeslaV100GPU,andtheFLOPsperqueryforeachneuralranking stack,andtransferthedocumentembeddingstotheGPU.Inpartic-
model. ForColBERT,ourreportedlatencysubsumestheentire
ular,thequeryencodingandinteractioninColBERTconsumeonly
computationfromgatheringthedocumentrepresentations,moving 13millisecondsofitstotalexecutiontime.WenotethatColBERT’s
themtotheGPU,tokenizingthenencodingthequery,andapplying latencyandFLOPscanbeconsiderablyreducedbypaddingqueries
lateinteractiontocomputedocumentscores. Forthebaselines, toashorterlength,usingsmallervectordimensions(theMRR@10
wemeasurethescoringcomputationsontheGPUandexclude ofwhichistestedin§4.5),employingquantizationofthedocument
| the CPU-based | text preprocessing | (similar | to [9]). | In principle, |     |     |     |     |     |
| ------------- | ------------------ | -------- | -------- | ------------- | --- | --- | --- | --- | --- |
thebaselinescanpre-computethemajorityofthispreprocessing
(e.g.,documenttokenization)offlineandparallelizetherestacross 6https://github.com/mit-han-lab/torchprofile

vectors,andstoringtheembeddingsonGPUifsufficientmemory havebeentestedonthisdataset.Theseresultsdirectlymirrorthose
| exists.Weleavethesedirectionsforfuturework. |     |     |     | withMSMARCO.        |     |           |     |
| ------------------------------------------- | --- | --- | --- | ------------------- | --- | --------- | --- |
|                                             |     |     |     | 4.3 End-to-endTop-k |     | Retrieval |     |
)elacs-gol( sPOLF noilliM
109 BERTbase (our training) Beyondcheapre-ranking,ColBERTisamenabletotop-kretrievaldi-
2000
108 ColBERT rectlyfromafullcollection.Table2considersfullretrieval,wherein
500 1000
|     |     |     |         | each model retrieves                               | the top-1000 | documents directly | from MS |
| --- | --- | --- | ------- | -------------------------------------------------- | ------------ | ------------------ | ------- |
| 107 |     |     | 100 200 |                                                    |              |                    |         |
|     |     | 50  |         | MARCO’s8.8Mdocumentsperquery.InadditiontoMRR@10and |              |                    |         |
20
106 k=10 latencyinmilliseconds,thetablereportsRecall@50,Recall@200,
andRecall@1000,importantmetricsforafull-retrievalmodelthat
105
essentiallyfiltersdownalargecollectiononaper-querybasis.
| 104 |      |           | 5002000 |                                                    |     |     |     |
| --- | ---- | --------- | ------- | -------------------------------------------------- | --- | --- | --- |
|     | k=10 | 20 50 100 |         |                                                    |     |     |     |
|     |      |           | 1000    | WecompareagainstBM25,inparticularMSMARCO’sofficial |     |     |     |
| 103 |      |           | 200     |                                                    |     |     |     |
BM25rankingaswellasawell-tunedbaselinebasedontheAnserini
|     | 0.27 0.29 | 0.31 0.33 | 0.35 0.37 |     |     |     |     |
| --- | --------- | --------- | --------- | --- | --- | --- | --- |
toolkit.7 Whilemanyothertraditionalmodelsexist,wearenot
MRR@10 awareofanythatsubstantiallyoutperformAnserini’sBM25im-
plementation(e.g.,seeRM3in[28],LMDirin[2],orMicrosoft’s
| Figure 4: | FLOPs (in millions) | and MRR@10 | as functions |     |     |     |     |
| --------- | ------------------- | ---------- | ------------ | --- | --- | --- | --- |
ofthere-rankingdepthk. SincetheofficialBM25ranking proprietaryfeature-basedRankSVMontheleaderboard).
isnotordered,theinitialtop-k retrievalisconductedwith Wealsocompareagainstdoc2query, DeepCT,anddocTTTT-
Anserini’sBM25. Tquery. Allthreerelyonatraditionalbag-of-wordsmodel(pri-
marilyBM25)forretrieval.Crucially,however,theyre-weighthe
Divingdeeperintothequality–costtradeoffbetweenBERTand frequencyoftermsperdocumentand/orexpandthesetofterms
ColBERT,Figure4demonstratestherelationshipsbetweenFLOPs
|     |     |     |     | ineachdocumentbeforebuildingtheBM25index. |     |     | Inparticular, |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | ------------- |
andeffectiveness(MRR@10)asafunctionofthere-rankingdepth
|     |     |     |     | doc2query expands | each document | with a pre-defined | number |
| --- | --- | --- | --- | ----------------- | ------------- | ------------------ | ------ |
kwhenre-rankingthetop-kresultsbyBM25,comparingColBERT
|     |     |     |     | of synthetic | queries generated | by a seq2seq transformer | model |
| --- | --- | --- | --- | ------------ | ----------------- | ------------------------ | ----- |
andBERT base (ourtraining).WeconductthisexperimentonMS (whichdocTTTTqueryreplacedwithapre-trainedlanguagemodel,
MARCO(Dev).Wenoteherethatastheofficialtop-1000ranking T5[31]).Incontrast,DeepCTusesBERTtoproducethetermfre-
doesnotprovidetheBM25order(andalsolacksdocumentsbeyond
quencycomponentofBM25inacontext-awaremanner.
thetop-1000perquery),themodelsinthisexperimentre-rankthe
ForthelatencyofAnserini’sBM25,doc2query,anddocTTTT-
Anserini[37]toolkit’sBM25output.Consequently,bothMRR@10
query,weusetheauthors’[26,28]Anserini-basedimplementation.
valuesatk =1000areslightlyhigherfromthosereportedinTable1. Whilethisimplementationsupportsmulti-threading,itonlyutilizes
StudyingtheresultsinFigure4,wenoticethatnotonlyisCol- parallelismacrossdifferentqueries.Wethusreportsingle-threaded
BERTmuchcheaperthanBERTforthesamemodelsize(i.e.,12-
|                                 |     |                           |     | latency for these | models, noting | that simply parallelizing | their |
| ------------------------------- | --- | ------------------------- | --- | ----------------- | -------------- | ------------------------- | ----- |
| layer“base”transformerencoder), |     | italsoscalesbetterwiththe |     |                   |                |                           |       |
computationovershardsoftheindexcansubstantiallydecrease
| numberofrankeddocuments. |     | Inpart,thisisbecauseColBERT |     |     |     |     |     |
| ------------------------ | --- | --------------------------- | --- | --- | --- | --- | --- |
theiralready-lowlatency.ForDeepCT,weonlyestimateitslatency
onlyneedstoprocessthequeryonce,irrespectiveofthenumberof usingthatofBM25(asdenotedby(est.)inthetable),sinceDeepCT
documentsevaluated.Forinstance,atk =10,BERTrequiresnearly re-weighsBM25’stermfrequencywithoutmodifyingtheindex
180×moreFLOPsthanColBERT;atk = 1000,BERT’soverhead otherwise.8 Asdiscussedin§4.1,weuseColBERT forend-to-
L2
| jumpsto13,900×.Itthenreaches23,000×atk |     |     | =2000.Infact,our |     |     |     |     |
| -------------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- |
endretrieval,whichemploysnegativesquaredL2distanceasits
informalexperimentationshowsthatthisorders-of-magnitudegap
vector-similarityfunction.Foritslatency,wemeasurethetimefor
inFLOPsmakesitpracticaltorunColBERTentirelyontheCPU, faiss-basedcandidatefilteringandthesubsequentre-ranking.In
althoughCPU-basedre-rankingliesoutsideourscope. thisexperiment,faissusesallavailableCPUcores.
LookingatTable2,wefirstseeAnserini’sBM25baselineat18.7
Method MAP MRR@10 MRR@10,noticingitsverylowlatencyasimplementedinAnserini
|                |     |      |     | (whichextendsthewell-knownLucenesystem), |     | owingtoboth |     |
| -------------- | --- | ---- | --- | ---------------------------------------- | --- | ----------- | --- |
| BM25(Anserini) |     | 15.3 | -   |                                          |     |             |     |
verycheapoperationsanddecadesofbag-of-wordstop-kretrieval
| doc2query |     | 18.1 | -   |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- | --- |
optimizations.Thethreesubsequentbaselines,namelydoc2query,
| DeepCT |     | 24.6 | 33.2 |     |     |     |     |
| ------ | --- | ---- | ---- | --- | --- | --- | --- |
DeepCT,anddocTTTTquery,eachbringsadecisiveenhancement
| BM25+BERT | base | 31.0 | -   |     |     |     |     |
| --------- | ---- | ---- | --- | --- | --- | --- | --- |
toeffectiveness.Theseimprovementscomeatnegligibleoverheads
| BM25+BERT    | large | 33.5 | -    |                                                          |     |     |     |
| ------------ | ----- | ---- | ---- | -------------------------------------------------------- | --- | --- | --- |
|              |       |      |      | inlatency, sincethesebaselinesultimatelyrelyonBM25-based |     |     |     |
| BM25+ColBERT |       | 31.3 | 44.3 |                                                          |     |     |     |
retrieval. Themosteffectiveamongthesethree,docTTTTquery,
Table3:ResultsonTRECCAR. demonstratesamassive9%gainovervanillaBM25byfine-tuning
therecentlanguagemodelT5.
HavingstudiedourresultsonMSMARCO,wenowconsider
| TRECCAR,whoseofficialmetricisMAP.Resultsaresummarized |     |     |     | 7http://anserini.io/ |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
inTable3,whichincludesanumberofimportantbaselines(BM25, 8Inpractice,amyriadofreasonscouldstillcauseDeepCT’slatencytodiffer
slightlyfromBM25’s.Forinstance,thetop-kpruningstrategyemployed,ifany,could
doc2query,andDeepCT)inadditiontore-rankingbaselinesthat interactdifferentlywithachangeddistributionofscores.

ShiftingourattentiontoColBERT’send-to-endretrievaleffec-
Basic ColBERT Indexing
tiveness,weseeitsmajorgainsinMRR@10overalloftheseend-to-
+multi-GPU document processing
endmodels.Infact,usingColBERTintheend-to-endsetupissupe- +per-batch maximum sequence length
riorintermsofMRR@10tore-rankingwiththesamemodeldue +length-based bucketing
totheimprovedrecall.MovingbeyondMRR@10,wealsoseelarge +multi-core pre-processing
gainsinRecall@kforkequalsto50,200,and1000.Forinstance, 0 10000 20000 30000 40000 50000
Throughput (documents/minute)
itsRecall@50actuallyexceedstheofficialBM25’sRecall@1000and
Figure6:EffectofColBERT’sindexingoptimizationsonthe
evenallbutdocTTTTTquery’sRecall@200,emphasizingthevalue
offlineindexingthroughput.
ofend-to-endretrieval(insteadofjustre-ranking)withColBERT.
4.5 IndexingThroughput&Footprint
4.4 AblationStudies
Lastly,weexaminetheindexingthroughputandspacefootprint
ofColBERT.Figure6reportsindexingthroughputonMSMARCO
documentswithColBERTandfourotherablationsettings,which
BERT [CLS]-based dot-product (5-layer) [A] individuallyenableoptimizationsdescribedin§3.4ontopofbasic
ColBERT via average similarity (5-layer) [B] batchedindexing.Basedonthesethroughputs,ColBERTcanindex
ColBERT without query augmentation (5-layer) [C] MSMARCOinaboutthreehours.NotethatanyBERT-basedmodel
ColBERT (5-layer) [D] mustincurthecomputationalcostofprocessingeachdocument
ColBERT (12-layer) [E]
atleastonce.WhileColBERTencodeseachdocumentwithBERT
ColBERT + e2e retrieval (12-layer) [F]
exactlyonce,existingBERT-basedrankerswouldrepeatsimilar
0.22 0.24 0.26 0.28 0.30 0.32 0.34 0.36
MRR@10 computationsonpossiblyhundredsofdocumentsforeachquery.
Figure 5: Ablation results on MS MARCO (Dev). Between
bracketsisthenumberofBERTlayersusedineachmodel.
Setting Dimension(m) Bytes/Dim Space(GiBs) MRR@10
Re-rankCosine 128 4 286 34.9
End-to-endL2 128 2 154 36.0
Theresultsfrom§4.2indicatethatColBERTishighlyeffective
Re-rankL2 128 2 143 34.8
despitethelowcostandsimplicityofitslateinteractionmechanism.
Re-rankCosine 48 4 54 34.4
Tobetterunderstandthesourceofthiseffectiveness,weexaminea
Re-rankCosine 24 2 27 33.9
numberofimportantdetailsinColBERT’sinteractionandencoder
Table4:SpaceFootprintvsMRR@10(Dev)onMSMARCO.
architecture.Forthisablation,wereportMRR@10onthevalidation
setofMSMARCOinFigure5,whichshowsourmainre-ranking
ColBERTmodel[E],withMRR@10of34.9%. Table4reportsthespacefootprintofColBERTundervarious
Duetothecostoftrainingallmodels,wetrainacopyofour settingsaswereducetheembeddingsdimensionand/orthebytes
mainmodelthatretainsonlythefirst5layersofBERToutof12 perdimension.Interestingly,themostspace-efficientsetting,that
(i.e.,model[D])andsimilarlytrainallourablationmodelsfor200k is,re-rankingwithcosinesimilaritywith24-dimensionalvectors
iterationswithfiveBERTlayers.Tobeginwith,weaskifthefine- storedas2-bytefloats,isonly1%worseinMRR@10thanthemost
granular interaction in late interaction is necessary. Model [A] space-consumingone,whiletheformerrequiresonly27GiBsto
tacklesthisquestion:itusesBERTtoproduceasingleembedding representtheMSMARCOcollection.
vectorforthequeryandanotherforthedocument,extractedfrom
5 CONCLUSIONS
BERT’s[CLS]contextualizedembeddingandexpandedthrougha
linearlayertodimension4096(whichequalsNq ×128=32×128). Inthispaper,weintroducedColBERT,anovelrankingmodelthat
Relevanceisestimatedastheinnerproductofthequery’sandthe employscontextualizedlateinteractionoverdeepLMs(inparticular,
document’sembeddings,whichwefoundtoperformbetterthan BERT)forefficientretrieval.Byindependentlyencodingqueries
cosinesimilarityforsingle-vectorre-ranking.Astheresultsshow, anddocumentsintofine-grainedrepresentationsthatinteractvia
thismodelisconsiderablylesseffectivethanColBERT,reinforcing cheapandpruning-friendlycomputations,ColBERTcanleverage
theimportanceoflateinteraction. theexpressivenessofdeepLMswhilegreatlyspeedingupquery
Subsequently,weaskifourMaxSim-basedlateinteractionisbet- processing.Inaddition,doingsoallowsusingColBERTforend-to-
terthanothersimplealternatives.Wetestamodel[B]thatreplaces endneuralretrievaldirectlyfromalargedocumentcollection.Our
ColBERT’smaximumsimilaritywithaveragesimilarity.Theresults resultsshowthatColBERTismorethan170×fasterandrequires
suggesttheimportanceofindividualtermsinthequerypaying 14,000×fewerFLOPs/querythanexistingBERT-basedmodels,all
specialattentiontoparticulartermsinthedocument. Similarly, whileonlyminimallyimpactingqualityandwhileoutperforming
thefigureemphasizestheimportanceofourqueryaugmentation everynon-BERTbaseline.
mechanism:withoutqueryaugmentation[C],ColBERThasano- Acknowledgments.OKwassupportedbytheEltoukhyFamily
ticeablylowerMRR@10.Lastly,weseetheimpactofend-to-end GraduateFellowshipattheStanfordSchoolofEngineering.This
retrievalnotonlyonrecallbutalsoonMRR@10. Byretrieving research was supported in part by affiliate members and other
directlyfromthefullcollection,ColBERTisabletoretrievetothe supportersoftheStanfordDAWNproject—AntFinancial,Facebook,
top-10documentsmissedentirelyfromBM25’stop-1000. Google,Infosys,NEC,andVMware—aswellasCisco,SAP,andthe

NSFunderCAREERgrantCNS-1651570.Anyopinions,findings, [25] RodrigoNogueiraandKyunghyunCho.2019.PassageRe-rankingwithBERT.
andconclusionsorrecommendationsexpressedinthismaterialare arXivpreprintarXiv:1901.04085(2019).
[26] RodrigoNogueira,JimmyLin,andAIEpistemic.2019. Fromdoc2queryto
thoseoftheauthorsanddonotnecessarilyreflecttheviewsofthe
docTTTTTquery.(2019).
NationalScienceFoundation. [27] RodrigoNogueira,WeiYang,KyunghyunCho,andJimmyLin.2019.Multi-Stage
DocumentRankingwithBERT.arXivpreprintarXiv:1910.14424(2019).
REFERENCES [28] RodrigoNogueira,WeiYang,JimmyLin,andKyunghyunCho.2019.Document
ExpansionbyQueryPrediction.arXivpreprintarXiv:1904.08375(2019).
[1] FirasAbuzaid,GeetSethi,PeterBailis,andMateiZaharia.2019.ToIndexorNot [29] MatthewEPeters,MarkNeumann,MohitIyyer,MattGardner,Christopher
toIndex:OptimizingExactMaximumInnerProductSearch.In2019IEEE35th Clark,KentonLee,andLukeZettlemoyer.2018. Deepcontextualizedword
InternationalConferenceonDataEngineering(ICDE).IEEE,1250–1261. representations.arXivpreprintarXiv:1802.05365(2018).
[2] ZhuyunDaiandJamieCallan.2019. Context-AwareSentence/PassageTerm [30] YifanQiao,ChenyanXiong,ZhenghaoLiu,andZhiyuanLiu.2019. Under-
ImportanceEstimationForFirstStageRetrieval.arXivpreprintarXiv:1910.10687 standingtheBehaviorsofBERTinRanking. arXivpreprintarXiv:1904.07531
(2019). (2019).
[3] ZhuyunDaiandJamieCallan.2019. DeeperTextUnderstandingforIRwith [31] ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,
ContextualNeuralLanguageModeling.arXivpreprintarXiv:1905.09217(2019). MichaelMatena,YanqiZhou,WeiLi,andPeterJLiu.2019. Exploringthe
[4] ZhuyunDai,ChenyanXiong,JamieCallan,andZhiyuanLiu.2018.Convolutional limitsoftransferlearningwithaunifiedtext-to-texttransformer.arXivpreprint
neuralnetworksforsoft-matchingn-gramsinad-hocsearch.InProceedingsofthe arXiv:1910.10683(2019).
eleventhACMinternationalconferenceonwebsearchanddatamining.126–134. [32] StephenERobertson,SteveWalker,SusanJones,MichelineMHancock-Beaulieu,
[5] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2018.Bert: MikeGatford,etal.1995.OkapiatTREC-3.NISTSpecialPublication(1995).
Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding. [33] RaphaelTang,YaoLu,LinqingLiu,LiliMou,OlgaVechtomova,andJimmyLin.
arXivpreprintarXiv:1810.04805(2018). 2019.Distillingtask-specificknowledgefromBERTintosimpleneuralnetworks.
[6] LauraDietz,ManishaVerma,FilipRadlinski,andNickCraswell.2017. TREC arXivpreprintarXiv:1903.12136(2019).
ComplexAnswerRetrievalOverview..InTREC. [34] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,
[7] JiafengGuo,YixingFan,QingyaoAi,andWBruceCroft.2016.Adeeprelevance AidanNGomez, LukaszKaiser,andIlliaPolosukhin.2017. Attentionisall
matchingmodelforad-hocretrieval.InProceedingsofthe25thACMInternational youneed.InAdvancesinneuralinformationprocessingsystems.5998–6008.
onConferenceonInformationandKnowledgeManagement.ACM,55–64. [35] YonghuiWu,MikeSchuster,ZhifengChen,QuocVLe,MohammadNorouzi,
[8] JiafengGuo,YixingFan,LiangPang,LiuYang,QingyaoAi,HamedZamani, WolfgangMacherey,MaximKrikun,YuanCao,QinGao,KlausMacherey,etal.
ChenWu,WBruceCroft,andXueqiCheng.2019. Adeeplookintoneural 2016.Google’sneuralmachinetranslationsystem:Bridgingthegapbetween
rankingmodelsforinformationretrieval.arXivpreprintarXiv:1903.06902(2019). humanandmachinetranslation.arXivpreprintarXiv:1609.08144(2016).
[9] SebastianHofsta¨tterandAllanHanbury.2019.Let’smeasureruntime!Extending [36] ChenyanXiong,ZhuyunDai,JamieCallan,ZhiyuanLiu,andRussellPower.
theIRreplicabilityinfrastructuretoincludeperformanceaspects.arXivpreprint 2017. End-to-endneuralad-hocrankingwithkernelpooling.InProceedings
arXiv:1907.04614(2019). ofthe40thInternationalACMSIGIRconferenceonresearchanddevelopmentin
[10] SebastianHofsta¨tter,NavidRekabsaz,CarstenEickhoff,andAllanHanbury. informationretrieval.55–64.
2019.Ontheeffectoflow-frequencytermsonneural-IRmodels.InProceedings [37] PeilinYang,HuiFang,andJimmyLin.2018. Anserini:Reproducibleranking
ofthe42ndInternationalACMSIGIRConferenceonResearchandDevelopmentin baselinesusingLucene. JournalofDataandInformationQuality(JDIQ)10,4
InformationRetrieval.1137–1140. (2018),1–20.
[11] SebastianHofsta¨tter,MarkusZlabinger,andAllanHanbury.2019.TUWien@ [38] WeiYang,KuangLu,PeilinYang,andJimmyLin.2019.CriticallyExamining
TRECDeepLearning’19–SimpleContextualizationforRe-ranking.arXivpreprint the”NeuralHype”WeakBaselinesandtheAdditivityofEffectivenessGains
arXiv:1912.01385(2019). fromNeuralRankingModels.InProceedingsofthe42ndInternationalACMSIGIR
[12] Po-SenHuang,XiaodongHe,JianfengGao,LiDeng,AlexAcero,andLarry ConferenceonResearchandDevelopmentinInformationRetrieval.1129–1132.
Heck.2013. Learningdeepstructuredsemanticmodelsforwebsearchusing [39] ZeynepAkkalyoncuYilmaz,WeiYang,HaotianZhang,andJimmyLin.2019.
clickthroughdata.InProceedingsofthe22ndACMinternationalconferenceon Cross-domainmodelingofsentence-levelevidencefordocumentretrieval.In
Information&KnowledgeManagement.2333–2338. Proceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguagePro-
[13] ShiyuJi,JinjinShao,andTaoYang.2019. EfficientInteraction-basedNeural cessingandthe9thInternationalJointConferenceonNaturalLanguageProcessing
RankingwithLocalitySensitiveHashing.InTheWorldWideWebConference. (EMNLP-IJCNLP).3481–3487.
ACM,2858–2864. [40] OfirZafrir,GuyBoudoukh,PeterIzsak,andMosheWasserblat.2019.Q8bert:
[14] XiaoqiJiao,YichunYin,LifengShang,XinJiang,XiaoChen,LinlinLi,FangWang, Quantized8bitbert.arXivpreprintarXiv:1910.06188(2019).
andQunLiu.2019.Tinybert:Distillingbertfornaturallanguageunderstanding. [41] HamedZamani,MostafaDehghani,WBruceCroft,ErikLearned-Miller,and
arXivpreprintarXiv:1909.10351(2019). JaapKamps.2018.Fromneuralre-rankingtoneuralranking:Learningasparse
[15] JeffJohnson,MatthijsDouze,andHerve´Je´gou.2017. Billion-scalesimilarity representationforinvertedindexing.InProceedingsofthe27thACMInternational
searchwithGPUs.arXivpreprintarXiv:1702.08734(2017). ConferenceonInformationandKnowledgeManagement.ACM,497–506.
[16] DiederikPKingmaandJimmyBa.2014.Adam:Amethodforstochasticopti- [42] LeZhao.2012.Modelingandsolvingtermmismatchforfull-textretrieval.Ph.D.
mization.arXivpreprintarXiv:1412.6980(2014). Dissertation.CarnegieMellonUniversity.
[17] RonKohavi,AlexDeng,BrianFrasca,TobyWalker,YaXu,andNilsPohlmann.
2013.Onlinecontrolledexperimentsatlargescale.InSIGKDD.
[18] SeanMacAvaney,AndrewYates,ArmanCohan,andNazliGoharian.2019.Cedr:
Contextualizedembeddingsfordocumentranking.InProceedingsofthe42nd
InternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
Retrieval.ACM,1101–1104.
[19] PaulMichel,OmerLevy,andGrahamNeubig.2019.AreSixteenHeadsReally
BetterthanOne?.InAdvancesinNeuralInformationProcessingSystems.14014–
14024.
[20] BhaskarMitraandNickCraswell.2019.AnUpdatedDuetModelforPassage
Re-ranking.arXivpreprintarXiv:1903.07666(2019).
[21] BhaskarMitra,NickCraswell,etal.2018.Anintroductiontoneuralinformation
retrieval.FoundationsandTrends®inInformationRetrieval13,1(2018),1–126.
[22] BhaskarMitra,FernandoDiaz,andNickCraswell.2017.Learningtomatchusing
localanddistributedrepresentationsoftextforwebsearch.InProceedingsof
the26thInternationalConferenceonWorldWideWeb.InternationalWorldWide
WebConferencesSteeringCommittee,1291–1299.
[23] BhaskarMitra,CorbyRosset,DavidHawking,NickCraswell,FernandoDiaz,
andEmineYilmaz.2019.Incorporatingquerytermindependenceassumption
forefficientretrievalandrankingusingdeepneuralnetworks.arXivpreprint
arXiv:1907.03693(2019).
[24] TriNguyen,MirRosenberg,XiaSong,JianfengGao,SaurabhTiwary,Rangan
Majumder,andLiDeng.2016. MSMARCO:AHuman-GeneratedMAchine
ReadingCOmprehensionDataset.(2016).
