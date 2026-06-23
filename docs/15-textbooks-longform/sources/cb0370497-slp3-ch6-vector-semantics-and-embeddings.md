Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2026. All
| rights reserved. | Draft | of January | 6,  | 2026. |     |     |     |     |     |     |     |
| ---------------- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
CHAPTER
| 6   | Neural |     |     | Networks |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
“[M]achinesofthischaractercanbehaveinaverycomplicatedmannerwhen
thenumberofunitsislarge.”
AlanTuring(1948)“IntelligentMachines”,page6
|     | Neural          | networks |        | are a fundamental |     | computational |        | tool    | for          | language | process-   |
| --- | --------------- | -------- | ------ | ----------------- | --- | ------------- | ------ | ------- | ------------ | -------- | ---------- |
|     | ing, and        | a very   | old    | one. They         | are | called        | neural | because | their        | origins  | lie in the |
|     | McCulloch-Pitts |          | neuron | (McCulloch        |     | and           | Pitts, | 1943),  | a simplified | model    | of the     |
biologicalneuronasakindofcomputingelementthatcouldbedescribedinterms
|     | ofpropositionallogic. |     |     | Butthemodernuseinlanguageprocessingnolongerdraws |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
ontheseearlybiologicalinspirations.
|     | Instead,                                                       | a modern     |     | neural     | network | is a    | network            | of small | computing |              | units, each |
| --- | -------------------------------------------------------------- | ------------ | --- | ---------- | ------- | ------- | ------------------ | -------- | --------- | ------------ | ----------- |
|     | ofwhichtakesavectorofinputvaluesandproducesasingleoutputvalue. |              |     |            |         |         |                    |          |           |              | Inthis      |
|     | chapter                                                        | we introduce |     | the neural | net     | applied | to classification. |          | The       | architecture | we          |
feedforward introduceiscalledafeedforwardnetworkbecausethecomputationproceedsiter-
|     | atively from | one | layer | of units | to the | next. | The | use of modern | neural | nets | is often |
| --- | ------------ | --- | ----- | -------- | ------ | ----- | --- | ------------- | ------ | ---- | -------- |
deeplearning calleddeeplearning,becausemodernnetworksareoftendeep(havemanylayers).
Neuralnetworkssharemuchofthesamemathematicsaslogisticregression.But
neuralnetworksareamorepowerfulclassifierthanlogisticregression,andindeeda
minimalneuralnetwork(technicallyonewithasingle‘hiddenlayer’)canbeshown
tolearnanyfunction.
|     | Neuralnetclassifiersaredifferentfromlogisticregressioninanotherway. |             |     |         |     |            |            |     |      |           | With     |
| --- | ------------------------------------------------------------------- | ----------- | --- | ------- | --- | ---------- | ---------- | --- | ---- | --------- | -------- |
|     | logistic                                                            | regression, | we  | applied | the | regression | classifier | to  | many | different | tasks by |
developingmanyrichkindsoffeaturetemplatesbasedondomainknowledge.When
workingwithneuralnetworks,itismorecommontoavoidmostusesofrichhand-
|     | derived                                                            | features, | instead  | building          |         | neural   | networks       | that           | take raw  | tokens     | as inputs   |
| --- | ------------------------------------------------------------------ | --------- | -------- | ----------------- | ------- | -------- | -------------- | -------------- | --------- | ---------- | ----------- |
|     | and learn                                                          | to induce | features |                   | as part | of the   | process        | of learning    | to        | classify.  | We saw      |
|     | examples                                                           | of this   | kind     | of representation |         | learning |                | for embeddings |           | in Chapter | 5, and      |
|     | we’llseelotsofexamplesoncewestartstudyingdeeptransformersnetworks. |           |          |                   |         |          |                |                |           |            | Nets        |
|     | that are                                                           | very deep | are      | particularly      |         | good at  | representation |                | learning. | For        | that reason |
deepneuralnetsaretherighttoolfortasksthatoffersufficientdatatolearnfeatures
automatically.
|     | In this       | chapter   | we’ll    | introduce |           | feedforward    |       | networks | as classifiers, |         | first with |
| --- | ------------- | --------- | -------- | --------- | --------- | -------------- | ----- | -------- | --------------- | ------- | ---------- |
|     | hand-built    | features, | and      | then      | using     | the embeddings |       | that     | we studied      | in      | Chapter 5. |
|     | In subsequent |           | chapters | we’ll     | introduce | many           | other | kinds    | of neural       | models, | most       |
importantlythetransformerandattention,(Chapter8),butalsorecurrentneural
|     | networks | (Chapter | 13) | and | convolutional |     | neural | networks | (Chapter | 15). | And in |
| --- | -------- | -------- | --- | --- | ------------- | --- | ------ | -------- | -------- | ---- | ------ |
thenextchapterwe’llintroducetheparadigmofneurallargelanguagemodels.

2 CHAPTER6 • NEURALNETWORKS
6.1 Units
| Thebuildingblockofaneuralnetworkisasinglecomputationalunit. |                     |           |          |                  | Aunittakes |     |
| ----------------------------------------------------------- | ------------------- | --------- | -------- | ---------------- | ---------- | --- |
| a set of                                                    | real valued numbers | as input, | performs | some computation | on them,   | and |
producesanoutput.
Atitsheart,aneuralunitistakingaweightedsumofitsinputs,withoneaddi-
biasterm tional term in the sum called a bias term. Given a set of inputs x ...x , a unit has
1 n
| asetofcorrespondingweightsw |     | ...w | andabiasb, | sotheweightedsumzcanbe |     |     |
| --------------------------- | --- | ---- | ---------- | ---------------------- | --- | --- |
1 n
representedas:
(cid:88)
|     |     | z=b+ | wx  |     |     | (6.1) |
| --- | --- | ---- | --- | --- | --- | ----- |
i i
i
Oftenit’smoreconvenienttoexpressthisweightedsumusingvectornotation;recall
vector from linear algebra that a vector is, at heart, just a list or array of numbers. Thus
we’lltalkaboutzintermsofaweightvectorw,ascalarbiasb,andaninputvector
x,andwe’llreplacethesumwiththeconvenientdotproduct:
|     |     | z=w·x+b |     |     |     | (6.2) |
| --- | --- | ------- | --- | --- | --- | ----- |
AsdefinedinEq.6.2,zisjustarealvaluednumber.
| Finally,           | instead of using | z, a linear        | function   | of x, as      | the output, neural | units     |
| ------------------ | ---------------- | ------------------ | ---------- | ------------- | ------------------ | --------- |
| apply a non-linear | function         | f to z. We         | will refer | to the output | of this function   | as        |
| the activation     | value for        | the unit, a. Since | we are     | just modeling | a single           | unit, the |
activation
activationforthenodeisinfactthefinaloutputofthenetwork,whichwe’llgenerally
cally. Sothevalueyisdefinedas:
|                                             |     | y=a= | f(z) |                                |     |     |
| ------------------------------------------- | --- | ---- | ---- | ------------------------------ | --- | --- |
| We’lldiscussthreepopularnon-linearfunctions |     |      |      | f below(thesigmoid,thetanh,and |     |     |
therectifiedlinearunitorReLU)butit’spedagogicallyconvenienttostartwiththe
sigmoid sigmoidfunctionsincewesawitinChapter4:
1
|     |     | y=σ(z)= |     |     |     | (6.3) |
| --- | --- | ------- | --- | --- | --- | ----- |
1+e−z
Thesigmoid(showninFig.6.1)hasanumberofadvantages;itmapstheoutput
| into the | range (0,1), which | is useful in | squashing | outliers | toward 0 or 1. | And it’s |
| -------- | ------------------ | ------------ | --------- | -------- | -------------- | -------- |
differentiable,whichaswesawinSection??willbehandyforlearning.
| Figure6.1 | The sigmoid | function takes a | real value | and maps | it to the range (0,1). | It is |
| --------- | ----------- | ---------------- | ---------- | -------- | ---------------------- | ----- |
nearlylineararound0butoutliervaluesgetsquashedtoward0or1.
SubstitutingEq.6.2intoEq.6.3givesustheoutputofaneuralunit:
1
|     | y=σ(w·x+b)= |     |     |     |     | (6.4) |
| --- | ----------- | --- | --- | --- | --- | ----- |
1+exp(−(w·x+b))

|                                                |     |              |                                             |     |     |                      | 6.1 | • UNITS | 3   |
| ---------------------------------------------- | --- | ------------ | ------------------------------------------- | --- | --- | -------------------- | --- | ------- | --- |
| Fig.6.2showsafinalschematicofabasicneuralunit. |     |              |                                             |     |     | Inthisexampletheunit |     |         |     |
| takes3inputvaluesx                             |     | 1 ,x 2 ,andx | 3 ,andcomputesaweightedsum,multiplyingeach  |     |     |                      |     |         |     |
| valuebyaweight(w                               |     | ,w ,andw     | ,respectively),addsthemtoabiastermb,andthen |     |     |                      |     |         |     |
|                                                |     | 1 2          | 3                                           |     |     |                      |     |         |     |
passestheresultingsumthroughasigmoidfunctiontoresultinanumberbetween0
and1.
x
|     |     | 1   | w   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | w 2 |     | z   | a   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | x   |     | ∑   | σ   | y   |     |     |     |
2
w 3
|     |     | x   | b   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
+1
| Figure6.2 Aneuralunit,taking3inputsx               |     |                                                       |     | ,x  | ,andx (andabiasbthatwerepresentasa |                         |     |     |     |
| -------------------------------------------------- | --- | ----------------------------------------------------- | --- | --- | ---------------------------------- | ----------------------- | --- | --- | --- |
|                                                    |     |                                                       |     | 1   | 2 3                                |                         |     |     |     |
| weightforaninputclampedat+1)andproducinganoutputy. |     |                                                       |     |     |                                    | Weincludesomeconvenient |     |     |     |
| intermediatevariables:                             |     | theoutputofthesummation,z,andtheoutputofthesigmoid,a. |     |     |                                    |                         |     |     | In  |
thiscasetheoutputoftheunityisthesameasa,butindeepernetworkswe’llreserveyto
meanthefinaloutputoftheentirenetwork,leavingaastheactivationofanindividualnode.
| Let’swalkthroughanexamplejusttogetanintuition. |     |     |     |     |     | Let’ssupposewehavea |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
unitwiththefollowingweightvectorandbias:
|     |     |     | w   | = [0.2,0.3,0.9] |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
|     |     |     | b   | = 0.5           |     |     |     |     |     |
Whatwouldthisunitdowiththefollowinginputvector:
|     |     |     | x   | = [0.5,0.6,0.1] |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
Theresultingoutputywouldbe:
|                                                               |     | 1           |     |                            | 1   |     |          | 1         |     |
| ------------------------------------------------------------- | --- | ----------- | --- | -------------------------- | --- | --- | -------- | --------- | --- |
| y=σ(w·x+b)=                                                   |     |             | =   |                            |     |     | =        | =.70      |     |
|                                                               |     | 1+e−(w·x+b) |     | 1+e−(.5∗.2+.6∗.3+.1∗.9+.5) |     |     | 1+e−0.87 |           |     |
| Inpractice,thesigmoidisnotcommonlyusedasanactivationfunction. |     |             |     |                            |     |     |          | Afunction |     |
tanh thatisverysimilarbutalmostalwaysbetteristhetanhfunctionshowninFig.6.3a;
tanhisavariantofthesigmoidthatrangesfrom-1to+1:
ez−e−z
|     |     |     | y=tanh(z)= |     |     |     |     |     | (6.5) |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ----- |
ez+e−z
| Thesimplestactivationfunction, |      |        | andperhapsthemostcommonlyused, |       |         |       |           | istherec- |      |
| ------------------------------ | ---- | ------ | ------------------------------ | ----- | ------- | ----- | --------- | --------- | ---- |
| tified linear unit,            | also | called | the ReLU,                      | shown | in Fig. | 6.3b. | It’s just | the same  | as z |
ReLU
whenzispositive,and0otherwise:
|     |     |     | y=ReLU(z)=max(z,0) |     |     |     |     |     | (6.6) |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ----- |
Theseactivationfunctionshavedifferentpropertiesthatmakethemusefulfordiffer-
| entlanguageapplicationsornetworkarchitectures. |     |     |     |     | Forexample,thetanhfunction |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
hasthenicepropertiesofbeingsmoothlydifferentiableandmappingoutliervalues
| towardthemean. | Therectifierfunction,ontheotherhand,hasnicepropertiesthat |     |     |     |     |     |     |     |     |
| -------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

4 CHAPTER6 • NEURALNETWORKS
(a) (b)
Figure6.3 ThetanhandReLUactivationfunctions.
resultfromitbeingveryclosetolinear. Inthesigmoidortanhfunctions,veryhigh
saturated valuesofzresultinvaluesofythataresaturated,i.e.,extremelycloseto1,andhave
derivativesverycloseto0. Zeroderivativescauseproblemsforlearning,becauseas
we’ll see in Section 6.6, we’ll train networks by propagating an error signal back-
wards, multiplying gradients (partial derivatives) from each layer of the network;
gradientsthatarealmost0causetheerrorsignaltogetsmallerandsmalleruntilitis
vanishing toosmalltobeusedfortraining,aproblemcalledthevanishinggradientproblem.
gradient
Rectifiersdon’thavethisproblem,sincethederivativeofReLUforhighvaluesofz
is1ratherthanverycloseto0.
6.2 The XOR problem
Earlyinthehistoryofneuralnetworksitwasrealizedthatthepowerofneuralnet-
works, as with the real neurons that inspired them, comes from combining these
unitsintolargernetworks.
Oneofthemostcleverdemonstrationsoftheneedformulti-layernetworkswas
the proof by Minsky and Papert (1969) that a single neural unit cannot compute
someverysimplefunctionsofitsinput. Considerthetaskofcomputingelementary
logical functions of two inputs, like AND, OR, and XOR. As a reminder, here are
thetruthtablesforthosefunctions:
AND OR XOR
x1 x2 y x1 x2 y x1 x2 y
0 0 0 0 0 0 0 0 0
0 1 0 0 1 1 0 1 1
1 0 0 1 0 1 1 0 1
1 1 1 1 1 1 1 1 0
perceptron Thisexamplewasfirstshownfortheperceptron,whichisaverysimpleneural
unit that has a binary output and has a very simple step function as its non-linear
activation function. The output y of a perceptron is 0 or 1, and is computed as
follows(usingthesameweightw,inputx,andbiasbasinEq.6.2):
(cid:26)
0, ifw·x+b≤0
y= (6.7)
1, ifw·x+b>0

6.2 • THEXORPROBLEM 5
It’s very easy to build a perceptron that can compute the logical AND and OR
functionsofitsbinaryinputs;Fig.6.4showsthenecessaryweights.
x x
1 1
1 1
x 1 x 1
2 2
-1 0
+1 +1
(a) (b)
Figure6.4 Theweightswandbiasbforperceptronsforcomputinglogicalfunctions. The
inputsareshownasx andx andthebiasasaspecialnodewithvalue+1whichismultiplied
1 2
withthebiasweightb. (a)logicalAND,withweightsw =1andw =1andbiasweight
1 2
b=−1. (b) logical OR, with weights w =1 and w =1 and bias weight b=0. These
1 2
weights/biasesarejustonefromaninfinitenumberofpossiblesetsofweightsandbiasesthat
wouldimplementthefunctions.
It turns out, however, that it’s not possible to build a perceptron to compute
logicalXOR!(It’sworthspendingamomenttogiveitatry!)
Theintuitionbehindthisimportantresultreliesonunderstandingthatapercep-
tron is a linear classifier. For a two-dimensional input x and x , the perceptron
1 2
equation,w x +w x +b=0istheequationofaline. (Wecanseethisbyputting
1 1 2 2
it in the standard linear format: x =(−w /w )x +(−b/w ).) This line acts as a
2 1 2 1 2
decision decisionboundaryintwo-dimensionalspaceinwhichtheoutput0isassignedtoall
boundary
inputslyingononesideoftheline,andtheoutput1toallinputpointslyingonthe
othersideoftheline. Ifwehadmorethan2inputs,thedecisionboundarybecomes
ahyperplaneinsteadofaline,buttheideaisthesame,separatingthespaceintotwo
categories.
Fig.6.5showsthepossiblelogicalinputs(00,01,10,and11)andthelinedrawn
byonepossiblesetofparametersforanANDandanORclassifier.Noticethatthere
issimplynowaytodrawalinethatseparatesthepositivecasesofXOR(01and10)
linearly fromthenegativecases(00and11). WesaythatXORisnotalinearlyseparable
separable
function. Ofcoursewecoulddrawaboundarywithacurve,orsomeotherfunction,
butnotasingleline.
6.2.1 Thesolution: neuralnetworks
WhiletheXORfunctioncannotbecalculatedbyasingleperceptron,itcanbecal-
culatedbyalayerednetworkofperceptronunits. Ratherthanseethiswithnetworks
ofsimpleperceptrons,however,let’sseehowtocomputeXORusingtwolayersof
ReLU-basedunitsfollowingGoodfellowetal.(2016). Fig.6.6showsafigurewith
the input being processed by two layers of neural units. The middle layer (called
h)hastwounits,andtheoutputlayer(calledy)hasoneunit. Asetofweightsand
biasesareshownthatallowsthenetworktocorrectlycomputetheXORfunction.
Let’swalkthroughwhathappenswiththeinputx=[0,0]. Ifwemultiplyeach
inputvaluebytheappropriateweight,sum,andthenaddthebiasb,wegetthevector
[0,-1],andwethenapplytherectifiedlineartransformationtogivetheoutputofthe
h layer as [0, 0]. Now we once again multiply by the weights, sum, and add the
bias (0 in this case) resulting in the value 0. The reader should work through the
computationoftheremaining3possibleinputpairstoseethattheresultingyvalues
are1fortheinputs[0,1]and[1,0]and0for[0,0]and[1,1].

6 CHAPTER6 • NEURALNETWORKS
x x x
2 2 2
1 1 1
?
0 0 0
x x x
1 1 1
0 1 0 1 0 1
a) x AND x b) x OR x c) x XOR x
1 2 1 2 1 2
Figure6.5 ThefunctionsAND,OR,andXOR,representedwithinputx onthex-axisandinputx onthe
1 2
y-axis. Filledcirclesrepresentperceptronoutputsof1,andwhitecirclesperceptronoutputsof0. Thereisno
waytodrawalinethatcorrectlyseparatesthetwocategoriesforXOR.FigurestyledafterRussellandNorvig
(2002).
x 1 h
1 1
1
1
y
1
1
-2
x
2 1 h 2 0
0
-1
+1 +1
Figure6.6 XORsolutionafterGoodfellowetal.(2016). TherearethreeReLUunits, in
twolayers;we’vecalledthemh ,h (hfor“hiddenlayer”)andy . Asbefore,thenumbers
1 2 1
onthearrowsrepresenttheweightswforeachunit,andwerepresentthebiasbasaweight
onaunitclampedto+1,withthebiasweights/unitsingray.
It’s also instructive to look at the intermediate results, the outputs of the two
hiddennodesh andh . Weshowedinthepreviousparagraphthatthehvectorfor
1 2
the inputs x = [0, 0] was [0, 0]. Fig. 6.7b shows the values of the h layer for all
4 inputs. Notice that hidden representations of the two input points x = [0, 1] and
x=[1, 0](thetwocaseswithXORoutput=1)aremergedtothesinglepointh=
[1,0]. Themergermakesiteasytolinearlyseparatethepositiveandnegativecases
ofXOR.Inotherwords,wecanviewthehiddenlayerofthenetworkasforminga
representationoftheinput.
InthisexamplewejuststipulatedtheweightsinFig.6.6. Butforrealexamples
theweightsforneuralnetworksarelearnedautomaticallyusingtheerrorbackprop-
agationalgorithmtobeintroducedinSection6.6. Thatmeansthehiddenlayerswill
learntoformusefulrepresentations. Thisintuition, thatneuralnetworkscanauto-
matically learn useful representations of the input, is one of their key advantages,
andonethatwewillreturntoagainandagaininlaterchapters.

|     |     |     |     | 6.3 | • FEEDFORWARDNEURALNETWORKS |     |     |     |     | 7   |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
x
|     | 2   |     |     |     | h   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     | 1   |     |     |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   |     |     |     | 0   |     |     |     |     |     |
x
|     |                         |            |       | 1       |                                         |                |     |            |     | h         |
| --- | ----------------------- | ---------- | ----- | ------- | --------------------------------------- | -------------- | --- | ---------- | --- | --------- |
|     | 0                       |            | 1     |         |                                         | 0              | 1   |            | 2   | 1         |
|     | a) The original x space |            |       |         | b) The new (linearly separable) h space |                |     |            |     |           |
|     | Figure6.7               | The hidden | layer | forming | a new                                   | representation | of  | the input. | (b) | shows the |
representationofthehiddenlayer,h,comparedtotheoriginalinputrepresentationxin(a).
|     | Notice that | the input point | [0, | 1] has been | collapsed |     | with the input | point | [1, 0], | making it |
| --- | ----------- | --------------- | --- | ----------- | --------- | --- | -------------- | ----- | ------- | --------- |
possibletolinearlyseparatethepositiveandnegativecasesofXOR.AfterGoodfellowetal.
(2016).
| 6.3 Feedforward |     | Neural |     | Networks |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- |
Let’snowwalkthroughaslightlymoreformalpresentationofthesimplestkindof
feedforward neuralnetwork,thefeedforwardnetwork. Afeedforwardnetworkisamultilayer
network
|     | networkinwhichtheunitsareconnectedwithnocycles; |            |          |            |       |           |            | theoutputsfromunitsin |         |        |
| --- | ----------------------------------------------- | ---------- | -------- | ---------- | ----- | --------- | ---------- | --------------------- | ------- | ------ |
|     | each layer                                      | are passed | to units | in the     | next  | higher    | layer, and | no outputs            | are     | passed |
|     | back to lower                                   | layers.    | (In      | Chapter 13 | we’ll | introduce | networks   | with                  | cycles, | called |
recurrentneuralnetworks.)
Forhistoricalreasonsmultilayernetworks,especiallyfeedforwardnetworks,are
multi-layer
perceptrons sometimescalledmulti-layerperceptrons(orMLPs);thisisatechnicalmisnomer,
MLP sincetheunitsinmodernmultilayernetworksaren’tperceptrons(perceptronshavea
simplestep-functionastheiractivationfunction,butmodernnetworksaremadeup
|     | ofunitswithmanykindsofnon-linearitieslikeReLUsandsigmoids), |     |     |     |     |     |     |     | butatsome |     |
| --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
pointthenamestuck.
|     | Simple | feedforward | networks | have | three | kinds | of nodes: | input | units, | hidden |
| --- | ------ | ----------- | -------- | ---- | ----- | ----- | --------- | ----- | ------ | ------ |
units,andoutputunits.
Fig.6.8showsapicture.Theinputlayerxisavectorofsimplescalarvaluesjust
aswesawinFig.6.2.
hiddenlayer Thecoreoftheneuralnetworkisthehiddenlayerhformedofhiddenunitsh ,
i
eachofwhichisaneuralunitasdescribedinSection6.1,takingaweightedsumof
|     | itsinputsandthenapplyinganon-linearity. |     |                                                      |     |     | Inthestandardarchitecture,eachlayer |     |     |     |     |
| --- | --------------------------------------- | --- | ---------------------------------------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
|     | isfully-connected,                      |     | meaningthateachunitineachlayertakesasinputtheoutputs |     |     |                                     |     |     |     |     |
fully-connected
fromalltheunitsinthepreviouslayer,andthereisalinkbetweeneverypairofunits
|     | fromtwoadjacentlayers.                                           |     | Thuseachhiddenunitsumsoveralltheinputunits. |     |     |     |     |     |     |     |
| --- | ---------------------------------------------------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | Recallthatasinglehiddenunithasasparametersaweightvectorandabias. |     |                                             |     |     |     |     |     |     | We  |
representtheparametersfortheentirehiddenlayerbycombiningtheweightvector
andbiasforeachunitiintoasingleweightmatrixWandasinglebiasvectorbfor
|     | thewholelayer(seeFig.6.8).                   |     |     | EachelementW |     | ji                              | oftheweightmatrixWrepresents |                |     |     |
| --- | -------------------------------------------- | --- | --- | ------------ | --- | ------------------------------- | ---------------------------- | -------------- | --- | --- |
|     | theweightoftheconnectionfromtheithinputunitx |     |     |              |     |                                 | tothe                        | jthhiddenunith |     | .   |
|     |                                              |     |     |              |     |                                 | i                            |                |     | j   |
|     | TheadvantageofusingasinglematrixW            |     |     |              |     | fortheweightsoftheentirelayeris |                              |                |     |     |
thatnowthehiddenlayercomputationforafeedforwardnetworkcanbedonevery

8 CHAPTER6 • NEURALNETWORKS
x
1
x
2
x
n
0
…
…
b
+1
…
W U
y
1
h
1
h
2 y
2
h
3
h
n
1
y
n
2
input layer hidden layer output layer
Figure6.8 Asimple2-layerfeedforwardnetwork,withonehiddenlayer,oneoutputlayer,
andoneinputlayer(theinputlayerisusuallynotcountedwhenenumeratinglayers).
efficiently with simple matrix operations. In fact, the computation only has three
steps: multiplyingtheweightmatrixbytheinputvectorx,addingthebiasvectorb,
andapplyingtheactivationfunctiong(suchasthesigmoid,tanh,orReLUactivation
functiondefinedabove).
Theoutputofthehiddenlayer,thevectorh,isthusthefollowing(forthisexam-
plewe’llusethesigmoidfunctionσ asouractivationfunction):
h=σ(Wx+b) (6.8)
Notice that we’re applying the σ function here to a vector, while in Eq. 6.3 it was
applied to a scalar. We’re thus allowing σ(·), and indeed any activation function
g(·),toapplytoavectorelement-wise,sog[z ,z ,z ]=[g(z ),g(z ),g(z )].
1 2 3 1 2 3
Let’sintroducesomeconstantstorepresentthedimensionalitiesofthesevectors
and matrices. We’ll refer to the input layer as layer 0 of the network, and have
n represent the number of inputs, so x is a vector of real numbers of dimension
0
n
0
, or more formally x∈Rn0, a column vector of dimensionality [n
0
×1]. Let’s
call the hidden layer layer 1 and the output layer layer 2. The hidden layer has
dimensionality n
1
, so h∈Rn1 and also b∈Rn1 (since each hidden unitcan take a
differentbiasvalue). AndtheweightmatrixWhasdimensionalityW∈Rn1×n0,i.e.
[n ×n ].
1 0
TakeamomenttoconvinceyourselfthatthematrixmultiplicationinEq.6.8will
computethevalueofeachh asσ
(cid:0)(cid:80)n0
W x +b
(cid:1)
.
j i=1 ji i j
AswesawinSection6.2,theresultingvalueh(forhiddenbutalsoforhypoth-
esis) forms a representation of the input. The role of the output layer is to take
this new representation h and compute a final output. This output could be a real-
valued number, but in many cases the goal of the network is to make some sort of
classificationdecision,andsowewillfocusonthecaseofclassification.
Ifwearedoingabinarytasklikesentimentclassification,wemighthaveasin-
gleoutputnode,anditsscalarvalueyistheprobabilityofpositiveversusnegative
sentiment. If we are doing multinomial classification, such as assigning a part-of-
speechtag,wemighthaveoneoutputnodeforeachpotentialpart-of-speech,whose
outputvalueistheprobabilityofthatpart-of-speech,andthevaluesofalltheoutput
nodesmustsumtoone. Theoutputlayeristhusavectory thatgivesaprobability
distributionacrosstheoutputnodes.

|                         |     |     | 6.3                                         | •   | FEEDFORWARDNEURALNETWORKS |     |     |     | 9   |
| ----------------------- | --- | --- | ------------------------------------------- | --- | ------------------------- | --- | --- | --- | --- |
| Let’sseehowthishappens. |     |     | Likethehiddenlayer,theoutputlayerhasaweight |     |                           |     |     |     |     |
matrix(let’scallitU),butsomemodelsdon’tincludeabiasvectorbintheoutput
| layer, sowe’llsimplifybyeliminatingthebiasvectorinthisexample. |     |     |     |     |     |     |     | Theweight |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
matrixismultipliedbyitsinputvector(h)toproducetheintermediateoutputz:
z=Uh
| There are | n output | nodes, | so z∈Rn2, |     | weight | matrix U | has dimensionality |     | U∈  |
| --------- | -------- | ------ | --------- | --- | ------ | -------- | ------------------ | --- | --- |
2
Rn2×n1,andelementU
|     |     | ij  | istheweightfromunit |     |     | jinthehiddenlayertounitiinthe |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | ----------------------------- | --- | --- | --- |
outputlayer.
However,zcan’tbetheoutputoftheclassifier,sinceit’savectorofreal-valued
| numbers,whilewhatweneedforclassificationisavectorofprobabilities. |          |     |             |     |          |                 |          | Thereis |      |
| ----------------------------------------------------------------- | -------- | --- | ----------- | --- | -------- | --------------- | -------- | ------- | ---- |
| a convenient                                                      | function | for | normalizing |     | a vector | of real values, | by which | we      | mean |
normalizing
convertingittoavectorthatencodesaprobabilitydistribution(allthenumberslie
softmax between 0 and 1 and sum to 1): the softmax function that we saw on page ?? of
| Chapter | 4. More | generally | for | any vector | z   | of dimensionality | d, the | softmax | is  |
| ------- | ------- | --------- | --- | ---------- | --- | ----------------- | ------ | ------- | --- |
definedas:
exp(z) i
|     |     | softmax(z | )   | =   |     | 1≤i≤d |     |     | (6.9) |
| --- | --- | --------- | --- | --- | --- | ----- | --- | --- | ----- |
i (cid:80)d
|     |     |     |     |     | exp(z | j ) |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
j=1
Thusforexamplegivenavector
|     |     | z=[0.6,1.1,−1.5,1.2,3.2,−1.1], |     |     |     |     |     |     | (6.10) |
| --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | ------ |
thesoftmaxfunctionwillnormalizeittoaprobabilitydistribution(shownrounded):
|         | softmax(z)=[0.055,0.090,0.0067,0.10,0.74,0.010] |         |              |     |           |               |              |      | (6.11) |
| ------- | ----------------------------------------------- | ------- | ------------ | --- | --------- | ------------- | ------------ | ---- | ------ |
| You may | recall                                          | that we | used softmax |     | to create | a probability | distribution | from | a      |
vectorofreal-valuednumbers(computedfromsummingweightstimesfeatures)in
themultinomialversionoflogisticregressioninChapter4.
| That | means | we can | think of | a neural | network | classifier | with one | hidden | layer |
| ---- | ----- | ------ | -------- | -------- | ------- | ---------- | -------- | ------ | ----- |
asbuildingavectorhwhichisahiddenlayerrepresentationoftheinput,andthen
| running      | standard                                                 | multinomial | logistic | regression |     | on the features  | that     | the network |     |
| ------------ | -------------------------------------------------------- | ----------- | -------- | ---------- | --- | ---------------- | -------- | ----------- | --- |
| developsinh. | Bycontrast,inChapter4thefeaturesweremainlydesignedbyhand |             |          |            |     |                  |          |             |     |
| via feature  | templates.                                               | So          | a neural | network    | is  | like multinomial | logistic | regression, |     |
but(a)withmanylayers,sinceadeepneuralnetworkislikelayerafterlayeroflo-
gisticregressionclassifiers;(b)withthoseintermediatelayershavingmanypossible
| activation     | functions | (tanh,                                                   | ReLU, | sigmoid) | instead | of just | sigmoid (although |     | we’ll |
| -------------- | --------- | -------------------------------------------------------- | ----- | -------- | ------- | ------- | ----------------- | --- | ----- |
| continuetouseσ |           | forconveniencetomeananyactivationfunction);(c)ratherthan |       |          |         |         |                   |     |       |
formingthefeaturesbyfeaturetemplates,thepriorlayersofthenetworkinducethe
featurerepresentationsthemselves.
Herearethefinalequationsforafeedforwardnetworkwithasinglehiddenlayer,
whichtakesaninputvectorx,outputsaprobabilitydistributiony,andisparameter-
izedbyweightmatricesWandUandabiasvectorb:
|          |             |     |        | h = σ(Wx+b)    |                |        |        |        |        |
| -------- | ----------- | --- | ------ | -------------- | -------------- | ------ | ------ | ------ | ------ |
|          |             |     |        | z = Uh         |                |        |        |        |        |
|          |             |     |        | y = softmax(z) |                |        |        |        | (6.12) |
| And just | to remember | the | shapes | of all         | our variables, | x∈Rn0, | h∈Rn1, | b∈Rn1, |        |
W∈Rn1×n0,U∈Rn2×n1,andtheoutputvectory∈Rn2.We’llcallthisnetworka2-
layernetwork(wetraditionallydon’tcounttheinputlayerwhennumberinglayers,
butdocounttheoutputlayer).Sobythisterminologylogisticregressionisa1-layer
network.

10 CHAPTER6 • NEURALNETWORKS
6.3.1 Moredetailsonfeedforwardnetworks
| Let’s now  | set up some | notation  | to           | make it | easier    | to talk  | about | deeper networks | of         |
| ---------- | ----------- | --------- | ------------ | ------- | --------- | -------- | ----- | --------------- | ---------- |
| depth more | than 2.     | We’ll use | superscripts |         | in square | brackets |       | to mean         | layer num- |
W[1]
| bers, starting             | at 0 for | the input | layer.                                         | So  | will | mean | the weight | matrix | for the |
| -------------------------- | -------- | --------- | ---------------------------------------------- | --- | ---- | ---- | ---------- | ------ | ------- |
| (first)hiddenlayer,andb[1] |          |           | willmeanthebiasvectorforthe(first)hiddenlayer. |     |      |      |            |        | n       |
j
| willmeanthenumberof |              | unitsatlayer |                                   | j.      | We’ll useg(·)tostandfortheactivation |              |     |            |           |
| ------------------- | ------------ | ------------ | --------------------------------- | ------- | ------------------------------------ | ------------ | --- | ---------- | --------- |
| function,           | which will   | tend to      | be ReLU                           | or tanh | for                                  | intermediate |     | layers and | softmax   |
| foroutputlayers.    | We’llusea[i] |              | tomeantheoutputfromlayeri,andz[i] |         |                                      |              |     |            | tomeanthe |
weightsandbiasesW[i]a[i−1]+b[i].
| combinationofpreviouslayeroutput, |     |     |     |     |     |     |     |     | The0th |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
layerisforinputs,sowe’llrefertotheinputsxmoregenerallyasa[0].
Thuswecanre-representour2-layernetfromEq.6.12asfollows:
|     |     |     | z[1] | W[1]a[0]+b[1] |     |     |     |     |     |
| --- | --- | --- | ---- | ------------- | --- | --- | --- | --- | --- |
=
|     |     |     | a[1] | g[1](z[1]) |     |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
=
|     |     |     | z[2] | W[2]a[1]+b[2] |     |     |     |     |     |
| --- | --- | --- | ---- | ------------- | --- | --- | --- | --- | --- |
=
|     |     |     | a[2] | g[2](z[2]) |     |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
=
|     |     |     | yˆ  | = a[2] |     |     |     |     | (6.13) |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ |
Notethatwiththisnotation,theequationsforthecomputationdoneateachlayerare
| thesame. | Thealgorithmforcomputingtheforwardstepinann-layerfeedforward |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
network,giventheinputvectora[0]isthussimply:
foriin1,...,n
| z[i] | = W[i]a[i−1] | + b[i] |     |     |     |     |     |     |     |
| ---- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| a[i] | g[i](z[i])   |        |     |     |     |     |     |     |     |
=
a[n]
yˆ =
It’softenusefultohaveanameforthefinalsetofactivationsrightbeforethefinal
| softmax. | So however | many | layers | we have, | we’ll | generally | call | the unnormalized |     |
| -------- | ---------- | ---- | ------ | -------- | ----- | --------- | ---- | ---------------- | --- |
valuesinthefinalvectorz[n],thevectorofscoresrightbeforethefinalsoftmax,the
logits logits(seeEq.??).
| The need | for non-linear | activation |     | functions |     | One of | the reasons | we  | use non- |
| -------- | -------------- | ---------- | --- | --------- | --- | ------ | ----------- | --- | -------- |
linearactivationfunctionsforeachlayerinaneuralnetworkisthatifwedidnot,the
| resultingnetworkisexactlyequivalenttoasingle-layernetwork. |     |     |     |     |     |     |     | Let’sseewhythis |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
istrue. Imaginethefirsttwolayersofsuchanetworkofpurelylinearlayers:
|     |     |     | z[1] | W[1]x+b[1] |     |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
=
|     |     |     | z[2] | W[2]z[1]+b[2] |     |     |     |     |     |
| --- | --- | --- | ---- | ------------- | --- | --- | --- | --- | --- |
=
Wecanrewritethefunctionthatthenetworkiscomputingas:
z[2] = W[2]z[1]+b[2]
= W[2](W[1]x+b[1])+b[2]
= W[2]W[1]x+W[2]b[1]+b[2]
= W(cid:48)x+b(cid:48)
(6.14)
Thisgeneralizestoanynumberoflayers.Sowithoutnon-linearactivationfunctions,
| a multilayer | network         | is just | a notational |     | variant of           | a single | layer | network  | with a     |
| ------------ | --------------- | ------- | ------------ | --- | -------------------- | -------- | ----- | -------- | ---------- |
| different    | set of weights, | and     | we lose      | all | the representational |          |       | power of | multilayer |
networks.

|     |                      | 6.4 | • FEEDFORWARDNETWORKSFORNLP:CLASSIFICATION |                                                  |     |     |     |     |     |     | 11  |
| --- | -------------------- | --- | ------------------------------------------ | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | Replacingthebiasunit |     |                                            | Indescribingnetworks,wewillsometimesuseaslightly |     |     |     |     |     |     |     |
simplifiednotationthatrepresentsexactlythesamefunctionwithoutreferringtoan
|     | explicitbiasnode |     | b.  | Instead, | weaddadummynode |     |     | a   | toeachlayer | whosevalue |     |
| --- | ---------------- | --- | --- | -------- | --------------- | --- | --- | --- | ----------- | ---------- | --- |
0
[0]
|     | will always | be  | 1. Thus | layer | 0, the | input | layer, will | have | a dummy | node | a =1, |
| --- | ----------- | --- | ------- | ----- | ------ | ----- | ----------- | ---- | ------- | ---- | ----- |
0
[1]
|     | layer1willhavea |     | =1,andsoon.Thisdummynodestillhasanassociatedweight, |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     | andthatweightrepresentsthebiasvalueb. |     |     |     |           |     | Forexampleinsteadofanequationlike |     |     |     |        |
| --- | ------------------------------------- | --- | --- | --- | --------- | --- | --------------------------------- | --- | --- | --- | ------ |
|     |                                       |     |     |     | h=σ(Wx+b) |     |                                   |     |     |     | (6.15) |
we’lluse:
|     |                                  |      |       |           | h=σ(Wx) |         |         |       |           |              | (6.16)     |
| --- | -------------------------------- | ---- | ----- | --------- | ------- | ------- | ------- | ----- | --------- | ------------ | ---------- |
|     | Butnowinsteadofourvectorxhavingn |      |       |           |         | 0       | values: | x=x 1 | ,...,x n0 | ,itwillhaven | 0 +        |
|     | 1 values,                        | with | a new | 0th dummy |         | value x | =1:     | x=x   | ,...,x    | . And        | instead of |
|     |                                  |      |       |           |         |         | 0       | 0     | n0        |              |            |
computingeachh
j asfollows:
|     |     |     |     |     | (cid:32) |     |     | (cid:33) |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- |
n0
(cid:88)
|     |     |     |     | h   | =σ  | W   | x +b | ,   |     |     | (6.17) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------ |
|     |     |     |     | j   |     |     | ji i | j   |     |     |        |
i=1
we’llinsteaduse:
|     |     |     |     |     |     | (cid:32) n0 | (cid:33) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | --- | --- | --- |
(cid:88)
|     |     |     |     |     | h =σ |     | W x  | ,   |     |     |        |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | ------ |
|     |     |     |     |     | j    |     | ji i |     |     |     | (6.18) |
i=0
|     | wherethevalueW |     | replaceswhathadbeenb |     |     |     | . Fig.6.9showsavisualization. |     |     |     |     |
| --- | -------------- | --- | -------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
|     |                |     | j0                   |     |     |     | j                             |     |     |     |     |
|     |                | W   |                      | U   |     |     |                               | W   |     | U   |     |
h
|     | x   |     |     | 1   |     | y   | x =1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     | 1   |     |     |     |     | 1   | 0    |     |     |     | y   |
|     |     |     |     |     |     |     |      |     | h   |     | 1   |
1
h
2
|     | x   |     |     |     |     | y   | x   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2   |     |     |     |     | 2   | 1   |     | h   |     | y   |
2
|     |     |     | h   |     |     |     |     |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | …   |     |     | 3   |     |     |     |     |     |     |     |
|     |     |     |     |     |     | …   | x   |     | h   |     |     |
|     |     |     | …   |     |     |     | 2   |     | 3   |     |     |
…
|     | x   |     |     |     |     |     |     |     | …   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | n   |     | h   |     |     |     |     |     |     |     |     |
|     | 0   |     | n   |     |     |     | …   |     |     |     |     |
1
|     |           |                                     |     |     |     | y   |     |      | h   |     |     |
| --- | --------- | ----------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |           | b                                   |     |     |     | n   | x   |      | n   |     | y   |
|     | +1        |                                     |     |     |     | 2   | n   |      |     | 1   | n   |
|     |           |                                     |     |     |     |     | 0   |      |     |     | 2   |
|     |           |                                     | (a) |     |     |     |     |      | (b) |     |     |
|     | Figure6.9 | Replacingthebiasnode(shownina)withx |     |     |     |     |     | (b). |     |     |     |
0
|     | We’ll | continue | showing |     | the bias | as b | when we | go over | the | learning | algorithm |
| --- | ----- | -------- | ------- | --- | -------- | ---- | ------- | ------- | --- | -------- | --------- |
inSection6.6,butgoingforwardinthebook,formostfiguresandsomeequations
we’llusethissimplifiednotationwithoutexplicitbiasterms.
| 6.4 Feedforward |     |     | networks |     | for | NLP: |     | Classification |     |     |     |
| --------------- | --- | --- | -------- | --- | --- | ---- | --- | -------------- | --- | --- | --- |
Let’sseehowtoapplyfeedforwardnetworkstoNLPclassificationtasks.Inpractice,
simplefeedforwardnetworksaren’tthewaywedotextclassification;forrealappli-
cationswewouldusemoresophisticatedarchitecturesliketheBERTtransformers

12 CHAPTER6 • NEURALNETWORKS
of Chapter 9. Nonetheless seeing a feedforward network text classifier will let us
introduce key ideas that will play a role throughout the rest of the book, includ-
ingtheideasoftheembeddingmatrix,representationpooling,andrepresentation
learning.
Butbeforeintroducinganyoftheseideas,let’sstartwithaclassifierbymaking
onlyminimalchangefromthesentimentclassifierswesawinChapter4.Likethem,
we’ll take hand-built features, pass them through a classifier, and produce a class
probability. Theonlydifferenceisthatwe’lluseaneuralnetworkinsteadoflogistic
regressionastheclassifier.
6.4.1 Neuralnetclassifierswithhand-builtfeatures
Let’sbeginwithasimple2-layersentimentclassifierbytakingourlogisticregres-
sion classifier from Chapter 4, which corresponds to a 1-layer network, and just
adding a hidden layer. The input element x can be scalar features like those in
i
Fig. ??, e.g., x = count(words ∈ doc), x = count(positive lexicon words ∈ doc),
1 2
x = 1 if “no” ∈ doc, and so on, for a total of d features. And the output layer
3
yˆ could have two nodes (one each for positive and negative), or 3 nodes (positive,
negative, neutral), in which case yˆ would be the estimated probability of positive
1
sentiment, yˆ theprobability ofnegative andyˆ theprobability ofneutral. The re-
2 3
sultingequationswouldbejustwhatwesawabovefora2-layernetwork(asalways,
we’llcontinuetousetheσ tostandforanynon-linearity, whethersigmoid, ReLU
orother).
x = [x ,x ,...x ] (eachx isahand-designedfeature)
1 2 d i
h = σ(Wx+b)
z = Uh
yˆ = softmax(z) (6.19)
Fig.6.10showsasketchofthisarchitecture. Aswementionedearlier, addingthis
hiddenlayertoourlogisticregressionclassifierallowsthenetworktorepresentthe
non-linearinteractionsbetweenfeatures.Thisalonemightgiveusabettersentiment
classifier.
h1
p(+)
h2
h3
h
dh
Input words W U
[d⨉1] [d ⨉d] [3⨉d ]
h [d ⨉1] h
h
Hidden layer Output layer
softmax
…
dessert wordcount x
=3 1 y^
1
was pos w it o iv r e d s l e = x i 1 con x 2 y^ 2 p(-)
great count of “no” x y^ 3 p(neut)
3
= 0
x y
h
[3⨉1]
Input layer
d=3 features
Figure6.10 Feedforwardnetworksentimentanalysisusingtraditionalhand-builtfeatures
oftheinputtext.

|     | 6.5 | •   | EMBEDDINGSASTHEINPUTTONEURALNETCLASSIFIERS |     |     |     |     |     |     |     | 13  |
| --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
6.4.2 Vectorizingforparallelizinginference
|     | While Eq.   | 6.19     | shows  | how    | to classify | a single       | example | x,    | in practice | we          | want to |
| --- | ----------- | -------- | ------ | ------ | ----------- | -------------- | ------- | ----- | ----------- | ----------- | ------- |
|     | efficiently | classify | an     | entire | test set    | of m examples. |         | We do | this by     | vectorizing | the     |
|     | process,    | just as  | we saw | with   | logistic    | regression;    | instead |       | of using    | for-loops   | to go   |
througheachexample,we’llusematrixmultiplicationtodotheentirecomputation
ofanentiretestsetatonce.First,wepackalltheinputfeaturevectorsforeachinput
xintoasingleinputmatrixX,witheachrowiarowvectorconsistingofthefeatures
|     | forinputexamplex(i)(i.e.,thevectorx(i)). |     |     |     |     | Ifthedimensionalityofourinputfeature |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
vectorisd,Xwillbeamatrixofshape[m×d].
Becausewearenowmodelingeachinputasarowvectorratherthanacolumn
|     | vector,wealsoneedtoslightlymodifyEq.6.19. |     |     |     |     |     | Xisofshape[m×d]andWisof |     |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
shape[d ×d],sowe’llreorderhowwemultiplyXandWandtransposeWsothey
h
|     | correctlymultiplytoyieldamatrixHofshape[m×d |     |     |     |     |     |     | ]. 1 |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
h
|     | ThebiasvectorbfromEq.6.19ofshape[1×d |     |       |      |          |      |              | h ]willnowhavetobereplicated |     |          |          |
| --- | ------------------------------------ | --- | ----- | ---- | -------- | ---- | ------------ | ---------------------------- | --- | -------- | -------- |
|     | into a matrix                        | of  | shape | [m×d | ]. We’ll | need | to similarly | reorder                      |     | the next | step and |
h
|     | transpose      | U. Finally, |                                   | our output | matrix     | Yˆ  | will be | of shape                    | [m×3] | (or more | gen-     |
| --- | -------------- | ----------- | --------------------------------- | ---------- | ---------- | --- | ------- | --------------------------- | ----- | -------- | -------- |
|     | erally [m×d    | o ],        | where                             | d o is     | the number | of  | output  | classes),                   | with  | each row | i of our |
|     | outputmatrixYˆ |             | consistingoftheoutputvectoryˆ(i). |            |            |     |         | Herearethefinalequationsfor |       |          |          |
computingtheoutputclassdistributionforanentiretestset:
(cid:124)
|     |     |     |     |     | H = | σ(XW | +b) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(cid:124)
|     |     |     |     |     | Z =  | HU         |     |     |     |     |        |
| --- | --- | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | ------ |
|     |     |     |     |     | Yˆ = | softmax(Z) |     |     |     |     | (6.20) |
Inthisbook,we’llsometimesseeorderingslikeWX+bandsometimesXW+b.
|     | That’s why | it’s | always | important | to  | be very | aware | of the | shapes | of your | weight |
| --- | ---------- | ---- | ------ | --------- | --- | ------- | ----- | ------ | ------ | ------- | ------ |
matricesparticipatinginanygivenequation.
| 6.5 Embeddings |                  |     | as the   | input |               | to neural |     | net    | classifiers  |      |          |
| -------------- | ---------------- | --- | -------- | ----- | ------------- | --------- | --- | ------ | ------------ | ---- | -------- |
|                | While hand-built |     | features | are   | a traditional | way       | to  | design | classifiers, | most | applica- |
tionsofneuralnetworksforNLPdon’tusehand-builthuman-engineeredfeaturesas
inputs. Instead,wedrawondeeplearning’sabilitytolearnfeaturesfromthedataby
|     | representing | tokens | as  | embeddings. |     | For this | section | we’ll | represent | each token | by  |
| --- | ------------ | ------ | --- | ----------- | --- | -------- | ------- | ----- | --------- | ---------- | --- |
itsstaticword2vecorGloVeembeddingsthatwesawhowtocomputeinChapter5.
Bystaticembedding,wemeanthateachtokenisrepresentedbyafixedvectorthat
|     | wetrainonce,andthenjustputintoabigdictionary. |     |     |     |     |     |     | Whenwewanttorefertothat |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
token,wegrabitsembeddingoutofthedictionary.
|     | However | when | we  | apply | neural | models | to the | task of | language | modeling | (as |
| --- | ------- | ---- | --- | ----- | ------ | ------ | ------ | ------- | -------- | -------- | --- |
we’llseeinChapter8)thesituationismorecomplex,andwe’lluseamorepower-
|     | ful kind                                            | of embedding |     | called | a contextual | embedding. |     | Contextual |                       | embeddings | are |
| --- | --------------------------------------------------- | ------------ | --- | ------ | ------------ | ---------- | --- | ---------- | --------------------- | ---------- | --- |
|     | differentforeachtimeawordoccursinadifferentcontext. |              |     |        |              |            |     |            | Furthermore,we’llhave |            |     |
thenetworklearntheseembeddingsaspartofthetaskofwordprediction.
Solet’sexplorethetextclassificationdomainabove,butusingstaticembeddings
|     | asfeaturesinsteadofthehand-designedfeatures. |     |     |     |     |     | Let’sfocusontheinferencestage, |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
1 Notethatwecouldhavekepttheoriginalorderofourproductsifwehadinsteadmadeourinput
matrixXrepresenteachinputasacolumnvectorinsteadofarowvector,makingitofshape[d×m].But
representinginputsasrowvectorsisconvenientandcommoninneuralnetworkmodels.

14 CHAPTER6 • NEURALNETWORKS
inwhichwehavealreadylearnedembeddingsforalltheinputtokens. Anembed-
ding is a vector of dimension d that represents the input token. The dictionary of
embedding static embeddings in which we store these embeddings is the embedding matrix
matrix
E. Each row of the embedding matrix represents each token of the vocabularyV
as a (row) vector of dimensionality d. Since E has a row for each of the |V| to-
kensinthevocabulary,Ehasshape[|V|×d]. ThisembeddingmatrixEplaysarole
wheneverweareusingembeddingsasinputtoneuralNLPsystems,includinginthe
transformer-basedlargelanguagemodelswewillintroduceoverthenextchapters.
Givenaninputtokenstringlikedessert was greatwefirstconvertthetokens
intovocabularyindices(thesewerecreatedwhenwefirsttokenizedtheinputusing
BPE or SentencePiece). So the representation of dessert was great might be
w=[3,9824,226]. NextweuseindexingtoselectthecorrespondingrowsfromE
(row3,row9824,row226).
Another way to think about selecting token embeddings from the embedding
matrix is to represent input tokens as one-hot vectors of shape [1×|V|], i.e., with
one-hotvector onedimensionforeachwordinthevocabulary. Recallthatinaone-hotvectorall
the elements are 0 except one, the element whose dimension is the word’s index
in the vocabulary, which has value 1. So if the word “dessert” has index 3 in the
vocabulary,x =1,andx =0 ∀i(cid:54)=3,asshownhere:
3 i
[0 0 1 0 0 0 0 ... 0 0 0 0]
1 2 3 4 5 6 7 ... ... |V|
Multiplyingbyaone-hotvectorthathasonlyonenon-zeroelementx =1simply
i
selectsouttherelevantrowvectorforwordi,resultingintheembeddingforwordi,
asdepictedinFig.6.11.
d
3
3 |V| d
1 0 0 1 0 0 0 0 … 0 0 0 0 ✕ E = 1
|V|
Figure6.11 Selecting the embedding vector for wordV by multiplying the embedding
3
matrixEwithaone-hotvectorwitha1inindex3.
Wecanextendthisideatorepresenttheentireinputtokensequenceasamatrix
ofone-hotvectors,oneforeachoftheN inputpositionsasshowninFig.6.12.
d
|V| d
0 0 1 0 0 0 0 … 0 0 0 0
0 0 0 0 0 0 0 … 0 0 1 0 ✕ E =
1 0 0 0 0 0 0 … 0 0 0 0
… N
N 0 0 0 0 1 0 0 … 0 0 0 0 |V|
Figure6.12 SelectingtheembeddingmatrixfortheinputsequenceoftokenidsW bymul-
tiplyingaone-hotmatrixcorrespondingtoW bytheembeddingmatrixE.
WenowneedtoclassifythisinputofN [1×d]embeddings,representingawin-
dowofN tokens,intoasingleclass(likepositiveornegative).
Therearetwocommonwaystopassembeddingstoaclassifier: concatenation
and pooling. First, we can take this input of shape [N×d] and reshape it by con-
catenatingalltheinputvectorsintooneverylongvectorofshape[1×dN]. Then

6.5 • EMBEDDINGSASTHEINPUTTONEURALNETCLASSIFIERS 15
wepassthisinputtoourclassifierandletitmakeitsdecision. Thisgivesuslotsof
pool information, at the cost of using a pretty large network. Second, we can pool the
N embeddingsintoasingleembeddingandthenpassthatsinglepooledembedding
to the classifier. Pooling gives us less information than would have been present
in all the original embeddings, but has the advantage of being small and efficient
and is especially useful in tasks for which we don’t care as much about the origi-
nalwordorder. Let’sgiveanexampleofeach: poolingforthesentimenttask,and
concatenationforthelanguagemodelingtask.
Poolinginputembeddingsforsentiment Solet’sbeginwithseeinghowpooling
can work for the sentiment classification task. The intuition of pooling is that for
sentiment, theexactpositionoftheinput(issomewordlikegreatthefirstword?
thesecondword?) islessimportantthantheidentityoftheworditself.
Apoolingfunctionisawaytoturnasetofembeddingsintoasingleembedding.
For example, for a text with N input words/tokens w ,...,w , we want to turn
1 N
the N row embeddings e(w ),...,e(w ) (each of dimensionality d) into a single
1 N
embeddingalsoofdimensionalityd.
mean-pooling Therearevariouswaystopool. Thesimplestismean-pooling: takingthemean
bysummingtheembeddingsandthendividingbyN:
N
1 (cid:88)
x mean = e(w i ) (6.21)
N
i=1
Herearetheequationsforthisclassifierassumingmeanpooling:
x = mean(e(w ),e(w ),...,e(w ))
1 2 n
h = σ(xW+b)
z = hU
yˆ = softmax(z) (6.22)
ThearchitectureissketchedinFig.6.13, wherewealsogivetheshapesforallthe
relevantmatrices.
max-pooling Therearemanyotheroptionsforpooling,likemax-pooling,inwhichcasefor
eachdimensionwetaketheelement-wisemaxoveralltheinputs. Theelement-wise
max of a set of N vectors is a new vector whose kth element is the max of the kth
elementsofalltheN vectors.
Concatenatinginputembeddingsforlanguagemodeling Forsentimentanaly-
sis we saw how to generate an output vector with probabilities over three classes:
positive, negative, or neutral, given as input a window of N input tokens, by first
poolingthosetokenembeddingsintoasingleembeddingvector.
Nowlet’sconsiderlanguagemodeling: predictingupcomingwordsfromprior
words. In this task we are given the same window of N input tokens, but our task
now is to predict the next token that should follow the window. We’ll sketch a
simplefeedforwardneurallanguagemodel,drawingonanalgorithmfirstintroduced
by Bengio et al. (2003). The feedforward language model introduces many of the
important concepts of large language modeling that we will return to in Chapter 7
andChapter8.
Neurallanguagemodelshavemanyadvantagesoverthen-gramlanguagemod-
els of Chapter 3. Neural language models can handle much longer histories, can
generalizebetterovercontextsofsimilarwords,andarefarmoreaccurateatword-

16 CHAPTER6 • NEURALNETWORKS
p(+) p(-) p(neut) Output probabilities
y^ ^y y^ y
1 2 3 [1⨉3] Output layer softmax
U [d h ⨉3] weights
h 1 h 2 h 3 … h dh h [1⨉d h ] Hidden layer
W[d⨉d h ] weights
x
[1⨉d] Input layer
pooled embedding
+ pooling
embedding for “dessert”
embedding for “was” N⨉d embeddings
embedding for “great”
E E E |V|⨉d E matrix
shared across words
1 3 |V|
1 524 |V|
1 902 |V| N⨉|V| one-hot vectors
00 1 00
00 01 00
“dessert” = V 3 “was” = V 524 “ 0 g 0 rea 0 t” 1 = V 00
902
dessert was great Input words
Figure6.13 Feedforwardnetworksentimentanalysisusingapooledembeddingoftheinputwords. Ateach
timestepthenetworkcomputesad-dimensionalembeddingforeachcontextword(bymultiplyingaone-hot
vector by the embedding matrix E), and pools the resulting N embeddings to get a single embedding that
representsthecontextwindowasthelayere.
prediction. On the other hand, neural net language models are slower, more com-
plex, need vast amounts of energy to train, and are less interpretable than n-gram
models,soforsomesmallertasksann-gramlanguagemodelisstilltherighttool.
A feedforward neural language model is a feedforward network that takes as
inputattimet arepresentationofsomenumberofpreviouswords(w ,w ,etc.)
t−1 t−2
and outputs a probability distribution over possible next words. Thus—like the n-
gramLM—thefeedforwardneuralLMapproximatestheprobabilityofawordgiven
theentirepriorcontextP(w|w )byapproximatingbasedontheN−1previous
t 1:t−1
words:
P(w t |w 1 ,...,w t−1 )≈P(w t |w t−N+1 ,...,w t−1 ) (6.23)
Inthefollowingexampleswe’llusea4-gramexample,sowe’llshowaneuralnetto
estimatetheprobabilityP(w =i|w ,w ,w ).
t t−3 t−2 t−1
Neural language models represent words in this prior context by their embed-
dings, rather than just by their word identity as used in n-gram language models.
Using embeddings allows neural language models to generalize better to unseen
data. Forexample,supposewe’veseenthissentenceintraining:
Ihavetomakesurethatthecatgetsfed.
buthaveneverseenthewords“getsfed”aftertheword“dog”. Ourtestsethasthe

6.5 • EMBEDDINGSASTHEINPUTTONEURALNETCLASSIFIERS 17
prefix“Iforgottomakesurethatthedoggets”. What’sthenextword? Ann-gram
languagemodelwillpredict“fed”after“thatthecatgets”,butnotafter“thatthedog
gets”.ButaneuralLM,knowingthat“cat”and“dog”havesimilarembeddings,will
beabletogeneralizefromthe“cat”contexttoassignahighenoughprobabilityto
“fed”evenafterseeing“dog”.
p(w=aardvark|w ,w ,w ) p(w=do|…) p(w=fish|…) p(w=zebra|…)
t t-3 t-2 t-1 t t t
output layer y y^ 1 … y^ 34 … y^ 42 … ^y 35102 … y^ |V| 1⨉|V|
softmax
U
d ⨉|V|
h
hidden layer h h 1 h 2 h 3 … h dh 1⨉d h
W Nd⨉d h
embedding layer e 1⨉Nd
E is shared E E E
across words
|V|⨉d
1 35 |V| 1 992 |V| 1 451 |V|
Input layer N⨉|V|
one-hot 00 1 00 00 01 00 00 0 1 00
vectors “for” = V 35 “all” = V 992 “the” = V 451
...
… and thanks for all the ? …
wt-3 wt-2 wt-1 wt
Figure6.14 Forwardinferenceinafeedforwardneurallanguagemodel. Ateachtimestep
tthenetworkcomputesad-dimensionalembeddingforeachoftheN=3contexttokens(by
multiplyingaone-hotvectorbytheembeddingmatrixE),andconcatenatesthethreetoget
theembeddinge.ThisembeddingeismultipliedbyweightmatrixWandthenanactivation
functionisappliedelement-wisetoproducethehiddenlayerh,whichisthenmultipliedby
anotherweightmatrixU. Asoftmaxlayerpredictsateachoutputnodeitheprobabilitythat
thenextwordwt willbevocabularywordV i.WeshowthecontextwindowsizeNas3justto
fitonthepage,butinpracticelanguagemodelingrequiresamuchlongercontext.
This prediction task requires an output vector that expresses |V| probabilities:
one probability value for each possible next token. We might have a vocabulary
between 60,000 and 300,000 tokens, so the output vector for the task of language
modelingismuchlongerthan3. Anotherdifferenceforlanguagemodelingisthat
insteadofpoolingtheembeddingsoftheN inputtokenstocreateasingleembed-
ding,weconcatenatetheinputsintooneverylonginputvector. Topredictthenext
token,ithelpstoknoweachoftheprecedingtokensandwhatordertheywerein.
Fig.6.14showsthelanguagemodelingtask,sketchedwithaveryshortcontext
windowofN=3justtofitonthepage.These3embeddingvectorsareconcatenated
toproducee,theembeddinglayer. ThisismultipliedbyaweightmatrixWtopro-
duceahiddenlayer,andanotherweightmatrixUtoproduceanoutputlayerwhose
softmax gives a probability distribution over words. For example y , the value of
42
outputnode42,istheprobabilityofthenextwordw beingV ,thevocabularyword
t 42
withindex42(whichistheword‘fish’inourexample).
The equations for a simple feedforward neural language model with a window

| 18 CHAPTER6 | •   | NEURALNETWORKS |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sizeof3,givenone-hotinputvectorsforeachinputcontextword,are:
|     |     |     |     | e = | [Ex | t−3 ;Ex | t−2 ;Ex | t−1 ] |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | --- | --- | --- |
h = σ(We+b)
z = Uh
|     |      |        |                   | yˆ = | softmax(z) |               |     |     |          |       | (6.24)   |
| --- | ---- | ------ | ----------------- | ---- | ---------- | ------------- | --- | --- | -------- | ----- | -------- |
|     | Note | thatwe | we use semicolons |      | to mean    | concatenation |     | of  | vectors, | so we | form the |
embeddinglayerebyconcatenatingthe3embeddingsforthethreecontextvectors.
|     | We’ll | return | to this | idea of | using | neural | networks | to  | do language | modeling | in  |
| --- | ----- | ------ | ------- | ------- | ----- | ------ | -------- | --- | ----------- | -------- | --- |
Chapter7andChapter8whenweintroducetransformerlanguagemodels.
| 6.6 Training |     | Neural | Nets |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Afeedforwardneuralnetisaninstanceofsupervisedmachinelearninginwhichwe
|     | know                                        | the correct      | output | y for each | observation |      | x.                            | What   | the system | produces, | via      |
| --- | ------------------------------------------- | ---------------- | ------ | ---------- | ----------- | ---- | ----------------------------- | ------ | ---------- | --------- | -------- |
|     | Eq.6.13,isyˆ,thesystem’sestimateofthetruey. |                  |        |            |             |      | Thegoalofthetrainingprocedure |        |            |           |          |
|     |                                             |                  |        | W[i]       | b[i]        |      |                               |        |            |           |          |
|     | is to                                       | learn parameters |        | and        | for         | each | layer                         | i that | make yˆ    | for each  | training |
observationascloseaspossibletothetruey.
Ingeneral,wedoallthisbydrawingonthemethodsweintroducedinChapter4
forlogisticregression,sothereadershouldbecomfortablewiththatchapterbefore
|     | proceeding. |     | We’ll explore | the | algorithm | on  | simple | generic | networks |     | rather than |
| --- | ----------- | --- | ------------- | --- | --------- | --- | ------ | ------- | -------- | --- | ----------- |
networksdesignedforsentimentorlanguagemodeling.
|     | First, | we’ll | need a | loss function |     | that models | the | distance | between |     | the system |
| --- | ------ | ----- | ------ | ------------- | --- | ----------- | --- | -------- | ------- | --- | ---------- |
outputandthegoldoutput,andit’scommontousethelossfunctionusedforlogistic
regression,thecross-entropyloss.
|     | Second, |     | to find the | parameters | that | minimize | this | loss | function, | we’ll | use the |
| --- | ------- | --- | ----------- | ---------- | ---- | -------- | ---- | ---- | --------- | ----- | ------- |
gradientdescentoptimizationalgorithmintroducedinChapter4.
|     | Third,                                                              | gradientdescentrequiresknowingthegradientofthelossfunction, |     |          |             |     |          |             |      |          | the      |
| --- | ------------------------------------------------------------------- | ----------------------------------------------------------- | --- | -------- | ----------- | --- | -------- | ----------- | ---- | -------- | -------- |
|     | vector                                                              | that contains                                               | the | partial  | derivative  | of  | the loss | function    | with | respect  | to each  |
|     | of the                                                              | parameters.                                                 | In  | logistic | regression, | for | each     | observation |      | we could | directly |
|     | computethederivativeofthelossfunctionwithrespecttoanindividualworb. |                                                             |     |          |             |     |          |             |      |          | But      |
forneuralnetworks,withmillionsofparametersinmanylayers,it’smuchharderto
|     | see how                         | to compute | the                                                 | partial | derivative | of                                   | some weight |     | in layer | 1 when | the loss |
| --- | ------------------------------- | ---------- | --------------------------------------------------- | ------- | ---------- | ------------------------------------ | ----------- | --- | -------- | ------ | -------- |
|     | isattachedtosomemuchlaterlayer. |            |                                                     |         |            | Howdowepartialoutthelossoverallthose |             |     |          |        |          |
|     | intermediatelayers?             |            | Theansweristhealgorithmcallederrorbackpropagationor |         |            |                                      |             |     |          |        |          |
backwarddifferentiation.
6.6.1 Lossfunction
cross-entropy Thecross-entropylossthatisusedinneuralnetworksisthesameonewesawfor
loss
|     | logistic    | regression. | If the       | neural     | network | is       | being used | as   | a binary | classifier, | with |
| --- | ----------- | ----------- | ------------ | ---------- | ------- | -------- | ---------- | ---- | -------- | ----------- | ---- |
|     | the sigmoid |             | at the final | layer, the | loss    | function | is the     | same | logistic | regression  | loss |
wesawinEq.??:
|     |     |     | L (yˆ,y)=−logp(y|x) |     |     | = −[ylogyˆ+(1−y)log(1−yˆ)] |     |     |     |     | (6.25) |
| --- | --- | --- | ------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | ------ |
CE
Ifweareusingthenetworktoclassifyinto3ormoreclasses,thelossfunctionis
exactlythesameasthelossformultinomialregressionthatwesawinChapter4on

6.6 • TRAININGNEURALNETS 19
page??. Let’sbrieflysummarizetheexplanationhereforconvenience. First,when
wehavemorethan2classeswe’llneedtorepresentbothy andyˆ asvectors. Let’s
assume we’re doing hard classification, where only one class is the correct one.
The true label y is then a vector with K elements, each corresponding to a class,
withy =1ifthecorrectclassisc,withallotherelementsofybeing0. Recallthat
c
avectorlikethis,withonevalueequalto1andtherest0,iscalledaone-hotvector.
AndourclassifierwillproduceanestimatevectorwithK elementsyˆ,eachelement
yˆ ofwhichrepresentstheestimatedprobability p(y =1|x).
k k
ThelossfunctionforasingleexamplexisthenegativesumofthelogsoftheK
outputclasses,eachweightedbytheirprobabilityy :
k
K
(cid:88)
L CE (yˆ,y)=− y k logyˆ k (6.26)
k=1
Wecansimplifythisequationfurther;let’sfirstrewritetheequationusingthefunc-
tion 1{} which evaluates to 1 if the condition in the brackets is true and to 0 oth-
erwise. ThismakesitmoreobviousthatthetermsinthesuminEq.6.26willbe0
exceptforthetermcorrespondingtothetrueclassforwhichy =1:
k
K
(cid:88)
L (yˆ,y) = − 1{y =1}logyˆ
CE k k
k=1
Inotherwords,thecross-entropylossissimplythenegativelogoftheoutputproba-
bilitycorrespondingtothecorrectclass,andwethereforealsocallthisthenegative
negativelog loglikelihoodloss:
likelihoodloss
L CE (yˆ,y) = −logyˆ c (wherecisthecorrectclass) (6.27)
PlugginginthesoftmaxformulafromEq.6.9,andwithK thenumberofclasses:
exp(z )
c
L CE (yˆ,y) = −log (cid:80)K
exp(z )
(wherecisthecorrectclass) (6.28)
j=1 j
Let’sthinkaboutthenegativelogprobabilityasalossfunction. Aperfectclas-
sifierwouldassignthecorrectclassiprobability1andalltheincorrectclassesprob-
ability0. Thatmeansthehigher p(yˆ)(thecloseritisto1),thebettertheclassifier;
i
p(yˆ)is(thecloseritisto0),theworsetheclassifier. Thenegativelogofthisprob-
i
ability is a beautiful loss metric since it goes from 0 (negative log of 1, no loss)
to infinity (negative log of 0, infinite loss). This loss function also insures that as
probability of the correct answer is maximized, the probability of all the incorrect
answersisminimized; sincetheyallsumtoone, anyincreaseintheprobabilityof
thecorrectansweriscomingattheexpenseoftheincorrectanswers.
The number K of classes of the output vector yˆcan be small or large. Perhaps
our task is 3-way sentiment, and then the classes might be positive, negative, and
neutral. Orifourtaskisdecidingthepartofspeechofaword(i.e.,whetheritisa
nounorverboradjective,etc.),thenKissetofpossiblepartsofspeechinourtagset
(of whichthere are 17in the tagset wewill define inChapter 17). And ifour task
islanguagemodeling,andourclassifieristryingtopredictwhichwordisnext,then
oursetofclassesisthesetofwords,whichmightbe50,000or100,000.

20 CHAPTER6 • NEURALNETWORKS
6.6.2 ComputingtheGradient
How do we compute the gradient of this loss function? Computing the gradient
requires the partial derivative of the loss function with respect to each parameter.
For a network with one weight layer and sigmoid output (which is what logistic
regressionis),wecouldsimplyusethederivativeofthelossthatweusedforlogistic
regressioninEq.6.29(andderivedinSection??):
∂L (yˆ,y)
CE
= (yˆ−y)x
j
∂w
j
= (σ(w·x+b)−y)x j (6.29)
Orforanetworkwithoneweightlayerandsoftmaxoutput(=multinomiallogistic
regression),wecouldusethederivativeofthesoftmaxlossfromEq.??,shownfor
aparticularweightw andinputx
k i
∂L (yˆ,y)
CE = −(y −yˆ )x
k k i
∂w
k,i
= −(y −p(y =1|x))x
k k i
(cid:32) (cid:33)
exp(w ·x+b )
k k
= − y k − (cid:80)K
exp(w ·x+b )
x i (6.30)
j=1 j j
Butthesederivativesonlygivecorrectupdatesforoneweightlayer:thelastone!
Fordeepnetworks,computingthegradientsforeachweightismuchmorecomplex,
sincewearecomputingthederivativewithrespecttoweightparametersthatappear
all the way back in the very early layers of the network, even though the loss is
computedonlyattheveryendofthenetwork.
Thesolutiontocomputingthisgradientisanalgorithmcallederrorbackprop-
errorback- agation or backprop (Rumelhart et al., 1986). While backprop was invented spe-
propagation
ciallyforneuralnetworks, itturnsouttobethesameasamoregeneralprocedure
called backward differentiation, which depends on the notion of computation
graphs. Let’sseehowthatworksinthenextsubsection.
6.6.3 ComputationGraphs
Acomputationgraphisarepresentationoftheprocessofcomputingamathematical
expression,inwhichthecomputationisbrokendownintoseparateoperations,each
ofwhichismodeledasanodeinagraph.
ConsidercomputingthefunctionL(a,b,c)=c(a+2b). Ifwemakeeachofthe
componentadditionandmultiplicationoperationsexplicit,andaddnames(dande)
fortheintermediateoutputs,theresultingseriesofcomputationsis:
d = 2∗b
e = a+d
L = c∗e
We can now represent this as a graph, with nodes for each operation, and di-
rected edges showing the outputs from each operation as the inputs to the next, as
in Fig. 6.15. The simplest use of computation graphs is to compute the value of
thefunctionwithsomegiveninputs. Inthefigure,we’veassumedtheinputsa=3,
b=1,c=−2,andwe’veshowntheresultoftheforwardpasstocomputethere-
sultL(3,1,−2)=−10. Intheforwardpassofacomputationgraph,weapplyeach

|           |                |         |             | 6.6 | • TRAININGNEURALNETS |     |     |           | 21     |
| --------- | -------------- | ------- | ----------- | --- | -------------------- | --- | --- | --------- | ------ |
| operation | left to right, | passing | the outputs |     | of each computation  |     | as  | the input | to the |
nextnode.
forward pass
a=3
a
e=5
e=a+d
d=2
b=1
|     |     | d = 2b |     |     |     | L=ce | L=-10 |     |     |
| --- | --- | ------ | --- | --- | --- | ---- | ----- | --- | --- |
b
c=-2
c
| Figure6.15 | ComputationgraphforthefunctionL(a,b,c)=c(a+2b),withvaluesforinput |     |     |     |     |     |     |     |     |
| ---------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
nodesa=3,b=1,c=−2,showingtheforwardpasscomputationofL.
6.6.4 Backwarddifferentiationoncomputationgraphs
| The importance | of      | the computation |      | graph comes | from | the backward |        | pass,   | which   |
| -------------- | ------- | --------------- | ---- | ----------- | ---- | ------------ | ------ | ------- | ------- |
| is used to     | compute | the derivatives | that | we’ll       | need | for the      | weight | update. | In this |
exampleourgoalistocomputethederivativeoftheoutputfunctionLwithrespect
| to eachof | the input | variables, | i.e., ∂L, | ∂L, | and ∂L. | The derivative |     | ∂L tells | ushow |
| --------- | --------- | ---------- | --------- | --- | ------- | -------------- | --- | -------- | ----- |
|           |           |            | ∂a        | ∂b  | ∂c      |                |     | ∂a       |       |
muchasmallchangeinaaffectsL.
| Backwards | differentiation |     | makes | use of | the chain | rule | in calculus, |     | so let’s re- |
| --------- | --------------- | --- | ----- | ------ | --------- | ---- | ------------ | --- | ------------ |
chainrule
| mind ourselves         | of  | that. Suppose   | we  | are computing                        |     | the derivative |     | of a | composite |
| ---------------------- | --- | --------------- | --- | ------------------------------------ | --- | -------------- | --- | ---- | --------- |
| function f(x)=u(v(x)). |     | Thederivativeof |     | f(x)isthederivativeofu(x)withrespect |     |                |     |      |           |
tov(x)timesthederivativeofv(x)withrespecttox:
|     |     |     | df  | du  | dv  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | =   | ·   |     |     |     |     |
(6.31)
|                                            |     |                                 | dx  | dv  | dx                          |         |     |     |     |
| ------------------------------------------ | --- | ------------------------------- | --- | --- | --------------------------- | ------- | --- | --- | --- |
| Thechainruleextendstomorethantwofunctions. |     |                                 |     |     | Ifcomputingthederivativeofa |         |     |     |     |
|                                            |     | f(x)=u(v(w(x))),thederivativeof |     |     |                             | f(x)is: |     |     |     |
compositefunction
|     |     |     | df  | du  | dv dw |     |     |     |        |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | ------ |
|     |     |     | =   | ·   | ·     |     |     |     | (6.32) |
|     |     |     | dx  | dv  | dw dx |     |     |     |        |
Theintuitionofbackwarddifferentiationistopassgradientsbackfromthefinal
nodetoallthenodesinthegraph.Fig.6.16showspartofthebackwardcomputation
| atonenodee. | Eachnodetakesanupstreamgradientthatispassedinfromitsparent |     |     |     |     |     |     |     |     |
| ----------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
nodetotheright,andforeachofitsinputscomputesalocalgradient(thegradient
ofitsoutputwithrespecttoitsinput),andusesthechainruletomultiplythesetwo
tocomputeadownstreamgradienttobepassedontothenextearliernode.
| Let’s                                  | now compute | the | 3 derivatives | we  | need. Since | in  | the computation |     | graph |
| -------------------------------------- | ----------- | --- | ------------- | --- | ----------- | --- | --------------- | --- | ----- |
| L=ce,wecandirectlycomputethederivative |             |     |               |     | ∂L:         |     |                 |     |       |
∂c
∂L
|     |     |     |     | =e  |     |     |     |     | (6.33) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
∂c
Fortheothertwo,we’llneedtousethechainrule:
|     |     |     | ∂L  | ∂L∂e |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
=
|     |     |     | ∂a  | ∂e∂a   |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     | ∂L  | ∂L∂e∂d |     |     |     |     |     |
=
(6.34)
|     |     |     | ∂b  | ∂e∂d | ∂b  |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |

| 22 CHAPTER6 |     | • NEURALNETWORKS |     |     |       |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
|             |     |                  |     |     | d     |     | e   |     |     |     |
|             |     |                  | d   |     |       | e   |     | L   |     |     |
|             |     |                  |     | ∂L  | ∂L ∂e | ∂e  | ∂L  |     |     |     |
=
|     |            |     |                                                                   |            |       | ∂d        | ∂e        |     |     |     |
| --- | ---------- | --- | ----------------------------------------------------------------- | ---------- | ----- | --------- | --------- | --- | --- | --- |
|     |            |     |                                                                   | ∂d         | ∂e ∂d |           |           |     |     |     |
|     |            |     |                                                                   | downstream |       | local     | upstream  |     |     |     |
|     |            |     |                                                                   |  gradient  |       |  gradient |  gradient |     |     |     |
|     | Figure6.16 |     | Eachnode(likeehere)takesanupstreamgradient,multipliesitbythelocal |            |       |           |           |     |     |     |
gradient(thegradientofitsoutputwithrespecttoitsinput),andusesthechainruletocompute
|     | a downstream |     | gradient to | be passed | on  | to a prior | node. A node | may | have multiple | local |
| --- | ------------ | --- | ----------- | --------- | --- | ---------- | ------------ | --- | ------------- | ----- |
gradientsifithasmultipleinputs.
|     |     |     |     |     |     |     |     | ∂L, | ∂L, ∂e, | ∂e,and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ |
Eq.6.34andEq.6.33thusrequirefiveintermediatederivatives:
|     |     |     |     |     |     |     |     | ∂e  | ∂c ∂a | ∂d  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
∂d,whichareasfollows(makinguseofthefactthatthederivativeofasumisthe
∂b
sumofthederivatives):
|     |     |     |     |       |     | ∂L  | ∂L  |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L=ce  | :   | =c, | =e  |     |     |     |
|     |     |     |     |       |     | ∂e  | ∂c  |     |     |     |
|     |     |     |     |       |     | ∂e  | ∂e  |     |     |     |
|     |     |     |     | e=a+d | :   | =1, | =1  |     |     |     |
|     |     |     |     |       |     | ∂a  | ∂d  |     |     |     |
∂d
|     |     |     |     | d=2b | :   | =2  |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
∂b
|     | In the                                                  | backward | pass, | we compute |     | each of these                          | partials | along  | each edge     | of the |
| --- | ------------------------------------------------------- | -------- | ----- | ---------- | --- | -------------------------------------- | -------- | ------ | ------------- | ------ |
|     | graphfromrighttoleft,usingthechainrulejustaswedidabove. |          |       |            |     |                                        |          |        | Thuswebeginby |        |
|     | computingthedownstreamgradientsfromnodeL,whichare       |          |       |            |     |                                        |          | ∂L and | ∂L.Fornodee,  |        |
|     |                                                         |          |       |            |     |                                        |          | ∂e     | ∂c            |        |
|     | wethenmultiplythisupstreamgradient                      |          |       |            |     | ∂L bythelocalgradient(thegradientofthe |          |        |               |        |
∂e
|     |                               |     |     |     | ∂e  |                                  |     |     |     | ∂L. |
| --- | ----------------------------- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- |
|     | outputwithrespecttotheinput), |     |     |     |     | togettheoutputwesendbacktonoded: |     |     |     |     |
|     |                               |     |     |     | ∂d  |                                  |     |     |     | ∂d  |
Andsoon,untilwehaveannotatedthegraphallthewaytoalltheinputvariables.
Theforwardpassconvenientlyalreadywillhavecomputedthevaluesoftheforward
|     | intermediatevariablesweneed(likedande)tocomputethesederivatives. |     |     |     |     |     |     |     | Fig.6.17 |     |
| --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
showsthebackwardpass.
a=3
a
∂L ∂L∂e
|     | =   | =-2 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂a ∂e ∂a
|     |     |     |     |     | e=d+a |     | e=5 |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
d=2
b=1
|         |     |        |         |     | ∂e  | ∂e    | ∂ L |     |      |       |
| ------- | --- | ------ | ------- | --- | --- | ----- | --- | --- | ---- | ----- |
| b       |     | d = 2b |         |     |     | =1 =1 | =-2 |     |      |       |
|         |     |        | ∂L ∂L∂e |     | ∂a  | ∂d    | ∂ e |     | L=ce | L=-10 |
|         |     |        | =       | =-2 |     |       |     |     |      |       |
|         |     |        | ∂d ∂e   | ∂d  |     |       |     |     |      |       |
| ∂L ∂L∂d |     | ∂d     |         |     |     |       |     |     |      |       |
| =       | =-4 | =2     |         |     |     |       |     |     | ∂L   |       |
| ∂b ∂d   | ∂b  | ∂b     |         |     |     |       |     |     | =-2  |       |
∂e
c=-2
∂L
|     |     |     |     |     |     |     |     |     | =5  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂c
∂L
|     |     |     | =5  |     |     | backward pass |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
c
∂c
Figure6.17 ComputationgraphforthefunctionL(a,b,c)=c(a+2b),showingthebackwardpasscomputa-
| ∂L, ∂L,and | ∂L. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionof
| ∂a ∂b | ∂c  |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

6.6 • TRAININGNEURALNETS 23
Backwarddifferentiationforaneuralnetwork
Of course computation graphs for real neural networks are much more complex.
Fig.6.18showsasamplecomputationgraphfora2-layerneuralnetworkwithn =
0
2, n =2, and n =1, assuming binary classification and hence using a sigmoid
1 2
outputunitforsimplicity. Thefunctionthatthecomputationgraphiscomputingis:
z[1] = W[1]x+b[1]
a[1] = ReLU(z[1])
z[2] = W[2]a[1]+b[2]
a[2] = σ(z[2])
yˆ = a[2] (6.35)
Forthebackwardpasswe’llalsoneedtocomputethelossL. Thelossfunction
forbinarysigmoidoutputfromEq.6.25is
L CE (yˆ,y) = −[ylogyˆ+(1−y)log(1−yˆ)] (6.36)
Ouroutputyˆ=a[2],sowecanrephrasethisas
(cid:104) (cid:105)
L CE (a[2],y) = − yloga[2]+(1−y)log(1−a[2]) (6.37)
[1]
w
11 *
[1]
w
12 z [1] = a [1] =
* 1 1
+ ReLU
x
1
*
[1]
b [2]
x 2 1 w 1 [ 1 2] z + = a [2] = σ L (a [2] ,y)
*
*
[1] [2]
w [1] [1] w
21 * z 2 = a 2 = 12
+ ReLU
[1]
w [2]
22 b
1
[1]
b
2
Figure6.18 Samplecomputationgraphforasimple2-layerneuralnet(=1hiddenlayer)withtwoinputunits
and2hiddenunits. We’veadjustedthenotationabittoavoidlongequationsinthenodesbyjustmentioning
[1]
thefunctionthatisbeingcomputed,andtheresultingvariablename.Thusthe*totherightofnodew means
11
thatw [1] istobemultipliedbyx ,andthenodez[1]=+meansthatthevalueofz[1] iscomputedbysumming
11 1
[1]
thethreenodesthatfeedintoit(thetwoproducts,andthebiastermb ).
i
The weights that need updating (those for which we need to know the partial
derivativeofthelossfunction)areshowninteal. Inordertodothebackwardpass,
we’llneedtoknowthederivativesofallthefunctionsinthegraph. Wealreadysaw
inSection??thederivativeofthesigmoidσ:
dσ(z)
=σ(z)(1−σ(z)) (6.38)
dz

24 CHAPTER6 • NEURALNETWORKS
| We’ll also | need | the derivatives | of each | of  | the other | activation | functions. The |
| ---------- | ---- | --------------- | ------- | --- | --------- | ---------- | -------------- |
derivativeoftanhis:
dtanh(z)
=1−tanh2(z)
(6.39)
dz
ThederivativeoftheReLUis2
|     |     | dReLU(z) | (cid:26) | for | z<0 |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- |
0
|     |     |     | =   |       |     |     | (6.40) |
| --- | --- | --- | --- | ----- | --- | --- | ------ |
|     |     |     | dz  | 1 for | z≥0 |     |        |
We’llgivethestartofthecomputation,computingthederivativeofthelossfunction
| Lwithrespecttoz,or |     | ∂L (andleavingtherestofthecomputationasanexercisefor |     |     |     |     |     |
| ------------------ | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
∂z
thereader). Bythechainrule:
|     |     |     | ∂L ∂L | ∂a[2] |     |     |     |
| --- | --- | --- | ----- | ----- | --- | --- | --- |
=
(6.41)
|     |     |     | ∂z ∂a[2] | ∂z  |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- |
∂L
| Solet’sfirstcompute |     | ,takingthederivativeofEq.6.37,repeatedhere: |     |     |     |     |     |
| ------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
∂a[2]
|     |          | (cid:104) |                           |     |     | (cid:105) |     |
| --- | -------- | --------- | ------------------------- | --- | --- | --------- | --- |
| L   | (a[2],y) | = −       | yloga[2]+(1−y)log(1−a[2]) |     |     |           |     |
CE
|     |       | (cid:32)(cid:32) |            | (cid:33) |        |              | (cid:33) |
| --- | ----- | ---------------- | ---------- | -------- | ------ | ------------ | -------- |
|     | ∂L    |                  | ∂log(a[2]) |          |        | ∂log(1−a[2]) |          |
|     |       | = −              | y          |          | +(1−y) |              |          |
|     | ∂a[2] |                  | ∂a[2]      |          |        | ∂a[2]        |          |
|     |       | (cid:18)(cid:18) | (cid:19)   |          |        | (cid:19)     |          |
|     |       |                  | 1          |          | 1      |              |          |
|     |       | = −              | y +(1−y)   |          |        | (−1)         |          |
|     |       |                  | a[2]       |          | 1−a[2] |              |          |
|     |       | (cid:18)         |            | (cid:19) |        |              |          |
|     |       |                  | y y−1      |          |        |              |          |
|     |       | = −              | +          |          |        |              |          |
(6.42)
|     |     |     | a[2] 1−a[2] |     |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- |
Next,bythederivativeofthesigmoid:
∂a[2]
=a[2](1−a[2])
∂z
Finally,wecanusethechainrule:
∂a[2]
|     |     | ∂L  | ∂L  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
=
|     |     | ∂z  | ∂a[2] ∂z |     |          |     |     |
| --- | --- | --- | -------- | --- | -------- | --- | --- |
|     |     |     | (cid:18) |     | (cid:19) |     |     |
y y−1
|     |     | =   | − + |     | a[2](1−a[2]) |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- |
a[2] 1−a[2]
a[2]−y
|     |     | =   |     |     |     |     | (6.43) |
| --- | --- | --- | --- | --- | --- | --- | ------ |
Continuingthebackwardcomputationofthegradients(nextbypassingthegra-
[2]
| dientsoverb | andthetwoproductnodes,andsoon,backtoallthetealnodes),is |     |     |     |     |     |     |
| ----------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
1
leftasanexerciseforthereader.
6.6.5 Moredetailsonlearning
Optimizationinneuralnetworksisanon-convexoptimizationproblem,morecom-
plexthanforlogisticregression,andforthatandotherreasonstherearemanybest
practicesforsuccessfullearning.
2 Thederivativeisactuallyundefinedatthepointz=0,butbyconventionwetreatitas1.

6.7 • SUMMARY 25
Forlogisticregressionwecaninitializegradientdescentwithalltheweightsand
biaseshavingthevalue0. Inneuralnetworks,bycontrast,weneedtoinitializethe
weightswithsmallrandomnumbers. It’salsohelpfultonormalizetheinputvalues
tohave0meanandunitvariance.
Variousformsofregularizationareusedtopreventoverfitting. Oneofthemost
dropout important is dropout: randomly dropping some units and their connections from
the network during training (Hinton et al. 2012, Srivastava et al. 2014). At each
iterationoftraining(wheneverweupdateparameters,i.e. eachmini-batchifweare
using mini-batch gradient descent), we repeatedly choose a probability p and for
each unit we replace its output with zero with probability p (and renormalize the
restoftheoutputsfromthatlayer).
hyperparameter Tuningofhyperparametersisalsoimportant. Theparametersofaneuralnet-
work are the weights W and biases b; those are learned by gradient descent. The
hyperparametersarethingsthatarechosenbythealgorithmdesigner; optimalval-
ues are tuned on a devset rather than by gradient descent learning on the training
set. Hyperparameters include the learning rate η, the mini-batch size, the model
architecture(thenumberoflayers,thenumberofhiddennodesperlayer,thechoice
of activation functions), how to regularize, and so on. Gradient descent itself also
hasmanyarchitecturalvariantssuchasAdam(KingmaandBa,2015).
Finally, most modern neural networks are built using computation graph for-
malismsthatmakeiteasyandnaturaltodogradientcomputationandparallelization
on vector-based GPUs (Graphic Processing Units). PyTorch (Paszke et al., 2017)
and TensorFlow (Abadi et al., 2015) are two of the most popular. The interested
reader should consult a neural network textbook for further details; some sugges-
tionsareattheendofthechapter.
6.7 Summary
• Neuralnetworksarebuiltoutofneuralunits. Originallyinspiredbybiologi-
calneurons,neuralnetworksarenowanabstractcomputationaldevicerather
thanabiologicalmodel.
• Eachneuralunitmultipliesinputvaluesbyaweightvector, addsabias, and
then applies a non-linear activation function like sigmoid, tanh, or rectified
linearunit.
• Inafully-connected,feedforwardnetwork,eachunitinlayeriisconnected
toeachunitinlayeri+1,andtherearenocycles.
• Thepowerofneuralnetworkscomesfromtheabilityofearlylayerstolearn
representationsthatcanbeutilizedbylaterlayersinthenetwork.
• Neural networks are trained by optimization algorithms like gradient de-
scent.
• Errorbackpropagation,backwarddifferentiationonacomputationgraph,
isusedtocomputethegradientsofthelossfunctionforanetwork.
• Neurallanguagemodelsuseaneuralnetworkasaprobabilisticclassifier,to
computetheprobabilityofthenextwordgiventhepreviousnwords.
• Neurallanguagemodelscanusepretrainedembeddings,orcanlearnembed-
dingsfromscratchintheprocessoflanguagemodeling.

26 CHAPTER6 • NEURALNETWORKS
Historical Notes
Theoriginsofneuralnetworkslieinthe1940sMcCulloch-Pittsneuron(McCul-
lochandPitts,1943),asimplifiedmodelofthebiologicalneuronasakindofcom-
| putingelementthatcouldbedescribedintermsofpropositionallogic. |     |     |     |     |     |     |     | Bythelate |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
1950sandearly1960s,anumberoflabs(includingFrankRosenblattatCornelland
| Bernard Widrow      |     | at Stanford) | developed      |     | research     | into neural | networks; |                    | this phase |
| ------------------- | --- | ------------ | -------------- | --- | ------------ | ----------- | --------- | ------------------ | ---------- |
| saw the development |     | of           | the perceptron |     | (Rosenblatt, | 1958),      | and       | the transformation |            |
ofthethresholdintoabias,anotationwestilluse(WidrowandHoff,1960).
Thefieldofneuralnetworksdeclinedafteritwasshownthatasingleperceptron
| unit was unable | to  | model | functions | as  | simple | as XOR (Minsky |     | and Papert, | 1969). |
| --------------- | --- | ----- | --------- | --- | ------ | -------------- | --- | ----------- | ------ |
Whilesomesmallamountofworkcontinuedduringthenexttwodecades,amajor
| revival for     | the field | didn’t     | come            | until   | the 1980s, | when practical    |     | tools for  | building  |
| --------------- | --------- | ---------- | --------------- | ------- | ---------- | ----------------- | --- | ---------- | --------- |
| deeper networks |           | like error | backpropagation |         |            | became widespread |     | (Rumelhart | et al.,   |
| 1986). During   | the       | 1980s      | a wide          | variety | of         | neural network    | and | related    | architec- |
turesweredeveloped,particularlyforapplicationsinpsychologyandcognitivesci-
| ence (Rumelhart |     | and McClelland |     | 1986b, | McClelland | and | Elman | 1986, Rumelhart |     |
| --------------- | --- | -------------- | --- | ------ | ---------- | --- | ----- | --------------- | --- |
connectionist and McClelland 1986a, Elman 1990), for which the term connectionist or paral-
leldistributedprocessingwasoftenused(FeldmanandBallard1982,Smolensky
| 1988). Many | of  | the principles |     | and techniques |     | developed | in this | period | are foun- |
| ----------- | --- | -------------- | --- | -------------- | --- | --------- | ------- | ------ | --------- |
dationaltomodernwork,includingtheideasofdistributedrepresentations(Hinton,
1986),recurrentnetworks(Elman,1990),andtheuseoftensorsforcompositionality
(Smolensky,1990).
Bythe1990slargerneuralnetworksbegantobeappliedtomanypracticallan-
guageprocessingtasksaswell,likehandwritingrecognition(LeCunetal.1989)and
| speechrecognition(MorganandBourlard1990). |     |     |     |     |     | Bytheearly2000s,improvements |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
incomputerhardwareandadvancesinoptimizationandtrainingtechniquesmadeit
possibletotrainevenlargeranddeepernetworks,leadingtothemoderntermdeep
| learning(Hintonetal.2006,Bengioetal.2007). |     |     |     |     |     | Wecovermorerelatedhistoryin |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- |
Chapter13andChapter15.
Thereareanumberofexcellentbooksonneuralnetworks,includingGoodfellow
etal.(2016)andNielsen(2015).

|     |     |     |     |     |     |     | HistoricalNotes | 27  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
Abadi, M., A. Agarwal, P. Barham, E. Brevdo, Z. Chen, Rumelhart,D.E.andJ.L.McClelland.1986a. Onlearning
C. Citro, G. S. Corrado, A. Davis, J. Dean, M. Devin, thepasttenseofEnglishverbs. InD.E.Rumelhartand
S.Ghemawat,I.Goodfellow,A.Harp,G.Irving,M.Is- J. L. McClelland, eds, Parallel Distributed Processing,
| ard,Y.Jia,R.Jozefowicz,L.Kaiser,M.Kudlur,J.Leven- |     |     |     |     |     | volume2,216–271.MITPress. |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
berg,D.Mane´,R.Monga,S.Moore,D.Murray,C.Olah,
Rumelhart,D.E.andJ.L.McClelland,eds.1986b.Parallel
| M.Schuster, | J.Shlens, | B.Steiner, | I.Sutskever, |     | K.Tal- |     |     |     |
| ----------- | --------- | ---------- | ------------ | --- | ------ | --- | --- | --- |
DistributedProcessing.MITPress.
war,P.Tucker,V.Vanhoucke,V.Vasudevan,F.Vie´gas,
|     |     |     |     |     |     | Russell, S.andP.Norvig.2002. | ArtificialIntelligence: | A   |
| --- | --- | --- | --- | --- | --- | ---------------------------- | ----------------------- | --- |
O.Vinyals,P.Warden,M.Wattenberg,M.Wicke,Y.Yu,
ModernApproach,2ndedition.PrenticeHall.
| andX.Zheng.2015. |     | TensorFlow: | Large-scalemachine |     |     |     |     |     |
| ---------------- | --- | ----------- | ------------------ | --- | --- | --- | --- | --- |
learningonheterogeneoussystems. Softwareavailable Smolensky,P.1988.Onthepropertreatmentofconnection-
ism.Behavioralandbrainsciences,11(1):1–23.
fromtensorflow.org.
Bengio,Y.,R.Ducharme,P.Vincent,andC.Jauvin.2003. Smolensky, P. 1990. Tensor product variable binding and
Aneuralprobabilisticlanguagemodel. JMLR,3:1137– therepresentationofsymbolicstructuresinconnectionist
| 1155. |     |     |     |     |     | systems.Artificialintelligence,46(1-2):159–216. |     |     |
| ----- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
Bengio, Y., P. Lamblin, D. Popovici, and H. Larochelle. Srivastava, N., G. E. Hinton, A. Krizhevsky, I. Sutskever,
2007. Greedy layer-wise training of deep networks. and R. R. Salakhutdinov. 2014. Dropout: a simple
| NeurIPS.        |                         |     |     |               |     | waytopreventneuralnetworksfromoverfitting. |     | JMLR, |
| --------------- | ----------------------- | --- | --- | ------------- | --- | ------------------------------------------ | --- | ----- |
| Elman,J.L.1990. | Findingstructureintime. |     |     | Cognitivesci- |     | 15(1):1929–1958.                           |     |       |
ence,14(2):179–211. Widrow,B.andM.E.Hoff.1960. Adaptiveswitchingcir-
cuits.IREWESCONConventionRecord,volume4.
Feldman,J.A.andD.H.Ballard.1982.Connectionistmod-
elsandtheirproperties.CognitiveScience,6:205–254.
| Goodfellow, | I., Y. Bengio, | and | A. Courville. | 2016. | Deep |     |     |     |
| ----------- | -------------- | --- | ------------- | ----- | ---- | --- | --- | --- |
Learning.MITPress.
| Hinton,G.E.1986. | Learningdistributedrepresentationsof |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
concepts.COGSCI.
| Hinton, G. | E., S. Osindero, | and | Y.-W. | Teh. 2006. | A fast |     |     |     |
| ---------- | ---------------- | --- | ----- | ---------- | ------ | --- | --- | --- |
Neuralcomputa-
learningalgorithmfordeepbeliefnets.
tion,18(7):1527–1554.
Hinton,G.E.,N.Srivastava,A.Krizhevsky,I.Sutskever,and
| R.R.Salakhutdinov.2012.                      |     |     | Improvingneuralnetworks |     |       |     |     |     |
| -------------------------------------------- | --- | --- | ----------------------- | --- | ----- | --- | --- | --- |
| bypreventingco-adaptationoffeaturedetectors. |     |     |                         |     | ArXiv |     |     |     |
preprintarXiv:1207.0580.
Kingma,D.andJ.Ba.2015.Adam:Amethodforstochastic
optimization.ICLR2015.
| LeCun, Y., | B. Boser, | J. S. Denker, | D.  | Henderson, | R. E. |     |     |     |
| ---------- | --------- | ------------- | --- | ---------- | ----- | --- | --- | --- |
Howard,W.Hubbard,andL.D.Jackel.1989.Backprop-
agationappliedtohandwrittenzipcoderecognition.Neu-
ralcomputation,1(4):541–551.
McClelland,J.L.andJ.L.Elman.1986.TheTRACEmodel
ofspeechperception.CognitivePsychology,18:1–86.
| McCulloch,W.S.andW.Pitts.1943.  |     |     | Alogicalcalculusof |                  |     |     |     |     |
| ------------------------------- | --- | --- | ------------------ | ---------------- | --- | --- | --- | --- |
| ideasimmanentinnervousactivity. |     |     |                    | BulletinofMathe- |     |     |     |     |
maticalBiophysics,5:115–133.
Minsky,M.andS.Papert.1969.Perceptrons.MITPress.
| Morgan,     | N. and H. | Bourlard.  | 1990.       | Continuous | speech |     |     |     |
| ----------- | --------- | ---------- | ----------- | ---------- | ------ | --- | --- | --- |
| recognition | using     | multilayer | perceptrons | with       | hidden |     |     |     |
markovmodels.ICASSP.
| Nielsen,M.A.2015. |     | NeuralnetworksandDeeplearning. |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
DeterminationPressUSA.
Paszke,A.,S.Gross,S.Chintala,G.Chanan,E.Yang,Z.De-
| Vito, Z. | Lin, A. Desmaison, |     | L. Antiga, | and | A. Lerer. |     |     |     |
| -------- | ------------------ | --- | ---------- | --- | --------- | --- | --- | --- |
2017.Automaticdifferentiationinpytorch.NIPS-W.
| Rosenblatt,F.1958. | Theperceptron:Aprobabilisticmodel |     |     |     |     |     |     |     |
| ------------------ | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
forinformationstorageandorganizationinthebrain.Psy-
chologicalreview,65(6):386–408.
Rumelhart,D.E.,G.E.Hinton,andR.J.Williams.1986.
Learninginternalrepresentationsbyerrorpropagation.In
D.E.RumelhartandJ.L.McClelland,eds,ParallelDis-
tributedProcessing,volume2,318–362.MITPress.
