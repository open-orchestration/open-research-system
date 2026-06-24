DataMinKnowlDisc(2009)18:140–181
DOI10.1007/s10618-008-0114-1
Controlled experiments on the web:
survey and practical guide
RonKohavi · RogerLongbotham ·
DanSommerfield · RandalM.Henne
Received:14February2008/Accepted:30June2008/Publishedonline:30July2008
SpringerScience+BusinessMedia,LLC2008
Abstract Thewebprovidesanunprecedentedopportunitytoevaluateideasquickly
usingcontrolledexperiments,alsocalledrandomizedexperiments,A/Btests(andtheir
generalizations),splittests,Control/Treatmenttests,MultiVariableTests(MVT)and
parallel flights. Controlled experiments embody the best scientific design for estab-
lishingacausalrelationshipbetweenchangesandtheirinfluenceonuser-observable
behavior.Weprovideapracticalguidetoconductingonlineexperiments,whereend-
userscanhelpguidethedevelopmentoffeatures.Ourexperienceindicatesthatsig-
nificant learning and return-on-investment (ROI) are seen when development teams
listentotheircustomers,nottotheHighestPaidPerson’sOpinion(HiPPO).Wepro-
vide several examples of controlled experiments with surprising results. We review
theimportantingredientsofrunningcontrolledexperiments,anddiscusstheirlimita-
tions (both technical and organizational). We focus on several areas that are critical
toexperimentation,includingstatisticalpower,samplesize,andtechniquesforvari-
ancereduction.Wedescribecommonarchitecturesforexperimentationsystemsand
analyzetheiradvantagesanddisadvantages.Weevaluaterandomizationandhashing
techniques,whichweshowarenotassimpleinpracticeasisoftenassumed.Controlled
Responsibleeditor:R.Bayardo.
B
R.Kohavi( )·R.Longbotham·D.Sommerfield·R.M.Henne
Microsoft,OneMicrosoftWay,Redmond,WA98052,USA
e-mail:ronnyk@microsoft.com
R.Longbotham
e-mail:rogerlon@microsoft.com
D.Sommerfield
e-mail:dans@microsoft.com
R.M.Henne
e-mail:rhenne@microsoft.com
123

Controlledexperimentsontheweb 141
experiments typically generate large amounts of data, which can be analyzed using
dataminingtechniquestogaindeeperunderstandingofthefactorsinfluencingtheout-
comeofinterest,leadingtonewhypothesesandcreatingavirtuouscycleofimprove-
ments.Organizationsthatembracecontrolledexperimentswithclearevaluationcri-
teriacan evolve theirsystems withautomated optimizations and real-timeanalyses.
Basedonourextensivepracticalexperiencewithmultiplesystemsandorganizations,
we share key lessons that will help practitioners in running trustworthy controlled
experiments.
Keywords Controlledexperiments·A/Btesting·e-commerce·
Websiteoptimization·MultiVariableTesting·MVT
1 Introduction
Oneaccuratemeasurementisworthmorethanathousandexpertopinions
–AdmiralGraceHopper
Inthe1700s,aBritishship’scaptainobservedthelackofscurvyamongsailorsserv-
ingonthenavalshipsofMediterraneancountries,wherecitrusfruitwaspartoftheir
rations.Hethengavehalfhiscrewlimes(theTreatmentgroup)whiletheotherhalf(the
Controlgroup)continuedwiththeirregulardiet.Despitemuchgrumblingamongthe
crewintheTreatmentgroup,theexperimentwasasuccess,showingthatconsuming
limespreventedscurvy.Whilethecaptaindidnotrealizethatscurvyisaconsequence
ofvitaminCdeficiency,andthatlimesarerichinvitaminC,theinterventionworked.
Britishsailorseventuallywerecompelledtoconsumecitrusfruitregularly,apractice
thatgaverisetothestill-popularlabellimeys(Rossietal.2003;Marks2000).
Some 300years later, Greg Linden at Amazon created a prototype to show
personalizedrecommendationsbasedonitemsintheshoppingcart(Linden2006a,b).
Youaddanitem,recommendationsshowup;addanotheritem,differentrecommenda-
tionsshowup.Lindennotesthatwhiletheprototypelookedpromising,“amarketing
senior vice-president was dead set against it,” claiming it will distract people from
checking out. Greg was “forbidden to work on this any further.” Nonetheless, Greg
ran a controlled experiment, and the “feature won by such a wide margin that not
havingitlivewascostingAmazonanoticeablechunkofchange.Withnewurgency,
shoppingcartrecommendationslaunched.”Sincethen,multiplesiteshavecopiedcart
recommendations.
TheauthorsofthispaperwereinvolvedinmanyexperimentsatAmazon,Microsoft,
Dupont, and NASA. The culture of experimentation at Amazon, where data trumps
intuition (Kohavi et al. 2004), and a system that made running experiments easy,
allowedAmazontoinnovatequicklyandeffectively.AtMicrosoft,therearemultiple
systemsforrunningcontrolledexperiments.Wedescribeseveralarchitecturesinthis
paper with their advantages and disadvantages. A unifying theme is that controlled
experimentshavegreatreturn-on-investment(ROI)andthatbuildingtheappropriate
infrastructure can accelerate innovation. Stefan Thomke’s book title is well suited
here:ExperimentationMatters(Thomke2003).
123

142 R.Kohavietal.
The web provides an unprecedented opportunity to evaluate ideas quickly using
controlled experiments, also called randomized experiments (single-factor or facto-
rialdesigns),A/Btests(andtheirgeneralizations),splittests,Control/Treatment,and
parallelflights.Inthesimplestmanifestationofsuchexperiments,liveusersareran-
domlyassignedtooneoftwovariants:(i)theControl,whichiscommonlythe“exist-
ing”version,and(ii)theTreatment,whichisusuallyanewversionbeingevaluated.
Metrics of interest, ranging from runtime performance to implicit and explicit user
behaviors and survey data, are collected. Statistical tests are then conducted on the
collecteddatatoevaluatewhetherthereisastatisticallysignificantdifferencebetween
thetwovariantsonmetricsofinterest,thuspermittingustoretainorrejectthe(null)
hypothesis that there is no difference between the versions. In many cases, drilling
downtosegmentsofusersusingmanual(e.g.,OLAP)ormachinelearninganddata
mining techniques, allows us to understand which subpopulations show significant
differences, thus helping improve our understanding and progress forward with an
idea.
Controlledexperimentsprovideamethodologytoreliablyevaluateideas.Unlike
othermethodologies,suchaspost-hocanalysisorinterruptedtimeseries(quasiexper-
imentation)(CharlesandMelvin2004),thisexperimentaldesignmethodologytests
forcausalrelationships(Keppeletal.1992,pp.5–6).Mostorganizationshavemany
ideas, but the return-on-investment (ROI) for many may be unclear and the evalua-
tionitselfmaybeexpensive.Asshowninthenextsection,evenminorchangescan
makeabigdifference,andofteninunexpectedways.Aliveexperimentgoesalong
wayinprovidingguidanceastothevalueoftheidea.Ourcontributionsincludethe
following.
• In Sect. 3 we review controlled experiments in a web environment and provide a
richsetofreferences,includinganimportantreviewofstatisticalpowerandsample
size,whichareoftenmissinginprimers.Wethenlookattechniquesforreducing
variancethatwefoundusefulinpractice.Wealsodiscussextensionsandlimitations
sothatpractitionerscanavoidpitfalls.
• In Sect. 4, we present several alternatives to MultiVariable Tests (MVTs) in an
online setting. In the software world, there are sometimes good reasons to prefer
concurrentuni-variatetestsovertraditionalMVTs.
• InSect.5,wepresentgeneralizedarchitecturesthatunifymultipleexperimentation
systems we have seen, and we discuss their pros and cons. We show that some
randomization and hashing schemes fail conditional independence tests required
forstatisticalvalidity.
• InSect.6weprovideimportantpracticallessons.
When a company builds a system for experimentation, the cost of testing and
experimentalfailurebecomessmall,thusencouraginginnovationthroughexperimen-
tation.Failingfastandknowingthatanideaisnotasgreataswaspreviouslythought
helps provide necessary course adjustments so that other more successful ideas can
beproposedandimplemented.
123

Controlledexperimentsontheweb 143
2 Motivatingexamples
Thefewerthefacts,thestrongertheopinion
–ArnoldGlasow
Thefollowingexamplespresentsurprisingresultsinmultipleareas.Thefirsttwo
deal with small UI changes that result in dramatic differences. The third example
showshowcontrolledexperimentscanbeusedtomakeatradeoffbetweenshort-term
revenue from ads and the degradation in the user experience. The fourth example
showstheuseofcontrolledexperimentsinbackendalgorithms,inthiscasesearchat
Amazon.
2.1 CheckoutpageatDoctorFootCare
Theconversionrateofane-commercesiteisthepercentageofvisitstothewebsite
thatincludeapurchase.ThefollowingexamplecomesfromBryanEisenberg’sarticles
(Eisenberg2003a,b).
Canyouguesswhichonehasahigherconversionrateandwhetherthedifference
issignificant?
ThereareninedifferencesbetweenthetwovariantsoftheDoctorFootCarecheck-
outpageshowninFig.1.Ifadesignershowedyoutheseandaskedwhichoneshould
be deployed, could you tell which one results in a higher conversion rate? Could
you estimate what the difference is between the conversion rates and whether that
differenceissignificant?
We encourage you, the reader, to think about this experiment before reading the
answer.Canyouestimatewhichvariantisbetterandbyhowmuch?Itisveryhumbling
toseehowharditistocorrectlypredicttheanswer.
Please,challengeyourself!
Fig.1 VariantAonleft,VariantBonright
123

144 R.Kohavietal.
Fig.2 Microsofthelpratingswidget.Theoriginalwidgetisshownabove.WhenusersclickonYes/No,
thedialoguecontinuesaskingforfree-textinput(two-phase)
VariantAinFig.1outperformedvariantBbyanorderofmagnitude.Inreality,the
site“upgraded”fromtheAtoBandlost90%oftheirrevenue!Mostofthechanges
intheupgradewerepositive,butthecouponcodewasthecriticalone:peoplestarted
tothinktwiceaboutwhethertheywerepayingtoomuchbecausetherearediscount
couponsouttherethattheydonothave.Byremovingthediscountcodefromthenew
version(B),conversion-rateincreased6.5%relativetotheoldversion(A)inFig.2.
2.2 RatingsofMicrosoftOfficehelparticles
UsersofMicrosoftOfficewhorequesthelp(orgothroughtheOfficeOnlinewebsiteat
http://office.microsoft.com)aregivenanopportunitytoratethearticlestheyread.The
initialimplementationpresenteduserswithaYes/Nowidget.Theteamthenmodified
thewidgetandoffereda5-starratings.
Themotivationsforthechangewerethefollowing:
1. The 5-star widget provides finer-grained feedback, which might help better
evaluatecontentwriters.
2. The5-starwidgetimprovesusabilitybyexposinguserstoasinglefeedbackbox
asopposedtotwoseparatepop-ups(oneforYes/NoandanotherforWhy).
Can you estimate which widget had a higher response rate, where response is any
interactionwiththewidget?
The surprise here was that number of ratings plummeted by about 90%, thus
significantly missing on goal #2 above. Based on additional tests, it turned out that
the two-stage model helps in increasing the response rate. Specifically, a controlled
experimentshowedthatthewidgetshowninFig.3,whichwasatwo-stagemodeland
alsoclarifiedthe5-starsdirectionas“Nothelpful”to“Veryhelpful”outperformedthe
oneinFig.4byafactorof2.2,i.e.,theresponseratewas2.2timeshigher.
Evengoal#1wassomewhatofadisappointmentasmostpeoplechosetheextremes
(one or five stars). When faced with a problem for which you need help, the article
eitherhelpsyousolvetheproblemoritdoesnot!
Theteamfinallysettledonayes/no/I-don’t-knowoption,whichhadaslightlylower
responseratethanjustyes/no,buttheadditionalinformationwasconsidereduseful.
123

Controlledexperimentsontheweb 145
Fig.3 Atwo-stagemodelwidget
Fig.4 New5-starratingswidget.Singleratingwidgetwith5stars
2.3 MSNhomepageads
A critical question that many site owners face is how many ads to place. In the
short-term,increasingthereal-estategiventoadscanincreaserevenue,butwhatwill
itdototheuserexperience,especiallyifthesearenon-targetedads?Thetradeoffbe-
tweenincreasedrevenueandthedegradationoftheend-userexperienceisatoughone
toassess,andthat’sexactlythequestionthattheMSNhomepageteamatMicrosoft
facedinlate2007.
TheMSNhomepageisbuiltoutofmodules.TheShoppingmoduleisshownon
therightsideofthepage above thefold.Theproposalwastoaddthreeoffersright
belowit,asshowninFig.5,whichmeantthattheseofferswouldshowupbelowthe
foldformostusers.TheDisplayAdsmarketingteamestimatedtheycouldgenerate
tensofthousandsofdollarsperdayfromtheseadditionaloffers.
Theinterestingchallengehereishowtocomparetheadrevenuewiththe“userexpe-
rience.”InSect.3.1,werefertothisproblemastheOEC,ortheOverallEvaluation
Criterion.Inthiscase,wedecidedtoseeifpageviewsandclicksdecreased,andassigna
123

146 R.Kohavietal.
Fig.5 MSNhomepageproposal.Left:Control,Right:proposedtreatment
monetaryvaluetoeach.(Nostatisticallysignificantchangewasseeninvisitfrequency
forthisexperiment.)PageviewsoftheMSNhomepagehaveanassignedvaluebased
onads;clickstodestinationsfromtheMSNhomepagewereestimatedintwoways:
1. Monetary value that the destination property assigned to a click from the MSN
homepage.ThesedestinationpropertiesareothersitesintheMSNnetwork.Such
aclickgeneratesavisittoanMSNproperty(e.g.,MSNAutosorMSNMoney),
whichresultsinmultiplepageviews.
2. ThecostpaidtosearchenginesforaclickthatbringsausertoanMSNpropertybut
notviatheMSNhomepage(SearchEngineMarketing).Ifthehomepageisdriv-
inglesstraffictotheproperties,whatisthecostofregeneratingthe“lost”traffic?
Asexpected,thenumberfrom#2(SEM)washigher,asadditionalvaluebeyonddirect
monetization is assigned to a click that may represent a new user, but the numbers
werecloseenoughtogetagreementonthemonetizationvaluetouse.
A controlled experiment was run on 5% of the MSN US home page users for
12days.Clickthroughratedecreasedby0.38%(relativechange),andtheresultwas
statisticallysignificant(p-value=0.02).
Translatingthelostclickstotheirmonetaryvalue,itwashigherthantheexpected
adrevenue,sotheideaofaddingmoreadstotheMSNhomepagewasscrapped.
2.4 Behavior-BasedSearchatAmazon
TheexamplesabovechangedUser-Interface(UI)elements.Thisexampledealswitha
backendalgorithmicchange,whichisoftenoverlookedasanareatoapplycontrolled
experiments.
123

Controlledexperimentsontheweb 147
Back in 2004, when several of the authors were in the Data Mining and
Personalization department at Amazon, there already existed a good algorithm for
makingrecommendationsbasedontwosets.ThesignaturefeatureforAmazon’srec-
ommendationis“PeoplewhoboughtitemXboughtitemY,”butthiswasgeneralized
to“PeoplewhovieweditemXboughtitemY”and“PeoplewhovieweditemXviewed
itemY.”Aproposalwasmadetousethesamealgorithmfor“Peoplewhosearched
for X bought item Y.” We called it Behavior-Based Search (BBS). In fact, the idea
wastosurfacethisinsearchresultswithnovisiblechangestotheuserinterface.Ifa
usersearchedforastringthatwascommon,andtherewasastrongsignalthatpeople
whosearchedforthatstringboughtoneofseveralitems,theseitemswouldsurfaceat
thetopofthesearchresults.Notethatthisalgorithmhasnosemanticunderstanding
ofthesearchedphrase,whichwasitsstrengthandweakness.
Proponents of the algorithm gave examples of underspecified searches, such as
“24,” which most humans associated with the TV show starring Kiefer Sutherland.
Amazon’s search was returning poor results, shown in Fig.6, such as CDs with 24
Italian Songs, clothing for 24-month old toddlers, a 24-inch towel bar, etc. (These
resultsarestillvisibleonAmazontodayifyouaddanadvancedsearchqualifierlike
“-foo” to the search phrase since this makes the search phrase unique and no map-
pings will exist from people who searched for it to products.) The BBS algorithm
gavetop-notchresultswiththeDVDsoftheshowandwithrelatedbooks,i.e.,things
that people purchased after searching for “24” as shown in Fig.6. The weakness of
the algorithm was that some items surfaced that did not contain the words in the
searchphrase.Forexample,ifonesearchesfor“SonyHDDVDPlayer”(thisexam-
ple is recent as of January 2008), Toshiba HD DVDs will show up fairly high. The
reasonisthatSonymakesBlu-RayDVDplayers,notHDplayers,andthatmanyusers
who search for Sony HD DVD players end up purchasing a Toshiba player. Given
the pros and cons for the idea of Behavior-Based search, Amazon ran a controlled
experiment.
Fig.6 Amazonsearchfor“24”withandwithoutBBS
123

148 R.Kohavietal.
In a UW iEdge Seminar talk by Amazon in April 2006, it was disclosed that the
featureincreasedAmazon’srevenueby3%,whichtranslatesintoseveralhundredsof
millionsofdollars.
2.5 Otherexamples
While these are extreme examples that are surprising in the magnitude of the
difference, they show how hard it is to predict the success of new designs. Several
moreexamplescanbefoundintheemetricstalkoncontrolledexperiments(Kohavi
2007).
Great examples of experiments are available at Marketing Experiments journal
(McGlaughlin2006),DesignChoicesCanCrippleaWebsite(Usborne2005),Callto
Action(EisenbergandEisenberg2005),andWhichSellsBest(EisenbergandGarcia
2006).Forrester’sPrimeronA/BTesting(Chathametal.2004)mentionsafewgood
examplesofpositiveROI:
• Marriott realized an additional $30 million in bookings with a new online
reservationsform.
• Luxury accessories retailer Coach improved the effectiveness of its site’s search
engine200%—byhavingitsvendorprovethatanewsearchenginewouldproduce
moreeffectiveresultswithanA/Btest.
• Disk-drive maker Iomega needed to know whether its prospects favored limited
freewareortrialversionsoffullsoftwareproducts,andwhichemaillandingpages
wouldproducethebestconversionrate.Theirsolution?Tostructureanexperimen-
taldesigntotestthevariouspermutations—thatultimatelydroveupcampaignyield
by50%.
Spool (2004) quantifies the cost of frustration at Amtrak.com’s web site, by noting
thatitisverydifficulttoregisterandthatonlyoneoutofeveryfourattemptssucceeds.
Obviouslymakingthesitemoreusablewillnotincreaseregistrationsbyafactorof
three or four, but if registrations increased by 20%, he shows that revenues would
increasebyover$15M/year,enoughtogetsomeone’sattention.
A/BtestatInterContinentalHotelsledthefirmtoaddtherangeofavailablerates
to search results, which added $45M–$60M of increased bookings (Manning et al.
2006).
Inshop.com’sTheStateofRetailing(ForresterResearch2005),theauthorswrote
thatintheirsurveyof137USretailers“100%oftheretailersthatemployedusability
testingandA/Btestingofoffersandpromotionsrankthesetacticsaseffectiveorvery
effective.”
Forrester’s Web Analytics Spending Trends 2007 (Burns 2006) wrote that A/B
testing will see the highest percentage of large increases [of web analytics catego-
ries]. A/B testing was one of only two categories [the other is SEO/SEM] in their
surveythatsawanincreaseinthepercentageofrespondentsplanningmajorbudget
growth.
123

Controlledexperimentsontheweb 149
3 Controlledexperiments
Enlightenedtrialanderroroutperformstheplanningofflawlessexecution
–DavidKelly,founderofIdeo
Tohaveagreatidea,havealotofthem
–ThomasA.Edison
In the simplest controlled experiment, often referred to as an A/B test, users are
randomlyexposedtooneoftwovariants:Control(A),orTreatment(B)asshownin
Fig.7(Masonetal.1989;Boxetal.2005;Keppeletal.1992).
Thekeyhereis“random.”Userscannotbedistributed“anyoldwhichway”(Weiss
1997);nofactorcaninfluencethedecision.Basedonobservationscollected,anOverall
EvaluationCriterion(OEC)isderivedforeachvariant(Roy2001).
Forexample,inCheckoutExample(Sect.2.1),theOECcanbetheconversionrate,
unitspurchased,revenue,profit,expectedlifetimevalue,orsomeweightedcombina-
tionofthese.AnalysisisthendonetodetermineifthedifferenceintheOECforthe
variantsisstatisticallysignificant.
Iftheexperimentwasdesignedandexecutedproperly,theonlythingconsistently
differentbetweenthetwovariantsisthechangebetweentheControlandTreatment,
soanydifferencesintheOECareinevitablytheresultofthisassignment,establishing
causality(Weiss1997,p.215).
Thereareseveralprimersonrunningcontrolledexperimentsontheweb(Peterson
2004,pp.76–78;EisenbergandEisenberg2005,pp.283–286;Chathametal.2004;
Eisenberg 2005, 2004; Quarto-vonTivadar 2006; Miller 2007, 2006; Kaushik 2006;
Peterson 2005, pp. 248–253; Tyler and Ledford 2006, pp. 213–219; Sterne 2002,
pp.116–119).
100%
Users
50% 50%
Users Users
Control: Treatment:
Existing System Existing System
with Feature X
Users interactions instrumented,
analyzed & compared
Analyze at the end of the
experiment
Fig.7 High-levelflowforanA/Btest
123

150 R.Kohavietal.
Whiletheconceptiseasytounderstandandbasicideasechothroughmanyrefer-
ences,thereareimportantlessonsthatweshareherethatarerarelydiscussed.These
will help experimenters understand the applicability, limitations, and how to avoid
mistakesthatinvalidatetheresults.
3.1 Terminology
Theterminologyforcontrolledexperimentsvarieswidelyintheliterature.Belowwe
definekeytermsusedinthispaperandnotealternativetermsthatarecommonlyused.
Overall Evaluation Criterion (OEC) (Roy 2001). A quantitative measure of the
experiment’sobjective.InstatisticsthisisoftencalledtheResponseorDependentVari-
able(Masonetal.1989;Boxetal.2005);othersynonymsincludeOutcome,Evaluation
metric,Performancemetric,orFitnessFunction(Quarto-vonTivadar2006).Experi-
mentsmayhavemultipleobjectivesandascorecardapproachmightbetaken(Kaplan
andNorton1996),althoughselectingasinglemetric,possiblyasaweightedcombi-
nation of such objectives is highly desired and recommended (Roy 2001, p. 50). A
singlemetricforcestradeoffstobemadeonceformultipleexperimentsandalignsthe
organizationbehindaclearobjective.AgoodOECshouldnotbeshort-termfocused
(e.g., clicks); to the contrary, it should include factors that predict long-term goals,
such as predicted lifetime value and repeat visits. Ulwick describes some ways to
measurewhatcustomerswant(althoughnotspecificallyfortheweb)(Ulwick2005).
Factor.AcontrollableexperimentalvariablethatisthoughttoinfluencetheOEC.
FactorsareassignedValues,sometimescalledLevelsorVersions.Factorsaresome-
timescalledVariables.InsimpleA/Btests,thereisasinglefactorwithtwovalues:A
andB.
Variant.Auserexperiencebeingtestedbyassigninglevelstothefactors;itiseither
theControloroneoftheTreatments.SometimesreferredtoasTreatment,althoughwe
prefertospecificallydifferentiatebetweentheControl,whichisaspecialvariantthat
designatestheexistingversionbeingcomparedagainstandthenewTreatmentsbeing
tried.Incaseofabug,forexample,theexperimentisabortedandallusersshouldsee
theControlvariant.
Experimentalunit.Theentityoverwhichmetricsarecalculatedbeforeaveraging
overtheentireexperimentforeachvariant.Sometimescalledanitem.Theunitsare
assumed to be independent. On the web, the user is a common experimental unit,
althoughsomemetricsmayhaveuser-day,user-sessionorpageviewsastheexperi-
mentalunits.Foranyoftheserandomizationbyuserispreferred.Itisimportantthat
theuserreceiveaconsistentexperiencethroughouttheexperiment,andthisiscom-
monlyachievedthroughrandomizationbasedonuserIDsstoredincookies.Wewill
assumethatrandomizationisbyuserwithsomesuggestionswhenrandomizationby
userisnotappropriateinAppendix.
Null hypothesis. The hypothesis, often referred to as H , that the OECs for the
0
variantsarenotdifferentandthatanyobserveddifferencesduringtheexperimentare
duetorandomfluctuations.
Confidencelevel.Theprobabilityoffailingtoreject(i.e.,retaining)thenullhypoth-
esiswhenitistrue.
123

Controlledexperimentsontheweb 151
Power. The probability of correctly rejecting the null hypothesis, H , when it is
0
false.Powermeasuresourabilitytodetectadifferencewhenitindeedexists.
A/Atest.SometimescalledaNullTest(Peterson2004).InsteadofanA/Btest,you
exercisetheexperimentationsystem,assigninguserstooneoftwogroups,butexpose
themtoexactlythesameexperience.AnA/Atestcanbeusedto(i)collectdataand
assessitsvariabilityforpowercalculations,and(ii)testtheexperimentationsystem
(theNullhypothesisshouldberejectedabout5%ofthetimewhena95%confidence
levelisused).
Standarddeviation(Std-Dev).Ameasureofvariability,typicallydenotedbyσ.
Standarderror(Std-Err).Forastatistic,itisthestandarddeviationofthesampling
distributionofthesam√plestatistic(Masonetal.1989).Forameanofn independent
observations,itisσˆ/ nwhereσˆ istheestimatedstandarddeviation.
3.2 Hypothesistestingandsamplesize
To evaluate whether one of the treatments is different than the Control, a statistical
testcanbedone.WeacceptaTreatmentasbeingstatisticallysignificantlydifferentif
thetestrejectsthenullhypothesis,whichisthattheOECsarenotdifferent.
Wewillnotreviewthedetailsofthestatisticaltests,astheyaredescribedverywell
inmanystatisticalbooks(Masonetal.1989;Boxetal.2005;Keppeletal.1992).
Whatisimportantistoreviewthefactorsthatimpactthetest:
1. Confidence level. Commonly set to 95%, this level implies that 5% of the time
wewillincorrectlyconcludethatthereisadifferencewhenthereisnone(TypeI
error).Allelsebeingequal,increasingthislevelreducesourpower(below).
2. Power.Commonlydesiredtobearound80–95%,althoughnotdirectlycontrolled.
IftheNullHypothesisisfalse,i.e.,thereisadifferenceintheOECs,thepower
istheprobabilityofdeterminingthatthedifferenceisstatisticallysignificant.(A
TypeIIerrorisonewhereweretaintheNullHypothesiswhenitisfalse.)
3. Standard error. The smaller the Std-Err, the more powerful the test. There are
threeusefulwaystoreducetheStd-Err:
a. TheestimatedOECistypicallyameanoflargesamples.AsshowninSect.3.1,
theStd-Errofameanisinverselyproportionaltothesquarerootofthesample
size,soincreasingthesamplesize,whichusuallyimpliesrunningtheexper-
iment longer, reduces the Std-Err and hence increases the power for most
metrics.Seetheexamplein3.2.1.
b. Use OEC components that have inherently lower variability, i.e., the Std-
Dev,σ,issmaller.Forexample,conversionprobability(0–100%)typically
haslowerStd-Devthannumberofpurchaseunits(typicallysmallintegers),
whichinturnhasalowerStd-Devthanrevenue(real-valued).Seetheexample
in3.2.1.
c. LowerthevariabilityoftheOECbyfilteringoutuserswhowerenotexposed
tothevariants,yetwerestillincludedintheOEC.Forexample,ifyoumake
a change to the checkout page, analyze only users who got to the page, as
everyoneelseaddsnoise,increasingthevariability.Seetheexamplein3.2.3.
123

152 R.Kohavietal.
4. Effect. The difference in OECs for the variants, i.e. the mean of the Treatment
minus the mean of the Control. Larger differences are easier to detect, so great
ideaswillunlikelybemissed.Conversely,TypeIIerrorsaremorelikelywhenthe
effectsaresmall.
Two formulas are useful to share in this context. The first is the t-test, used in A/B
tests(singlefactorhypothesistests):
O −O
t = B A (1)
σ(cid:1)
d
where O and O aretheestimatedOECvalues(e.g.,averages),σ(cid:1) istheestimated
A B d
standard deviation of the difference between the two OECs, and t is the test result.
Basedontheconfidencelevel,athresholdtisestablished(e.g.,1.96forlargesamples
and95%confidence)andiftheabsolutevalueoftislargerthanthethreshold,then
werejecttheNullHypothesis,claimingtheTreatment’sOECisthereforestatistically
significantlydifferentthantheControl’sOEC.Weassumethroughoutthatthesample
sizesarelargeenoughthatitissafetoassumethemeanshaveaNormaldistribution
bytheCentralLimitTheorem(Boxetal.2005,p.29;BoosandHughes-Oliver2000)
eventhoughthepopulationdistributionsmaybequiteskewed.
A second formula is a calculation for the minimum sample size, assuming the
desiredconfidencelevelis95%andthedesiredpoweris80%(vanBelle2002,p.31)
16σ2
n = (2)
(cid:2)2
where n is the number of users in each variant and the variants are assumed to be
ofequalsize,σ2 isthevarianceoftheOEC,and(cid:2)isthesensitivity,ortheamount
ofchangeyouwanttodetect.(Itiswellknownthatonecouldimprovethepowerof
comparisonsofthetreatmentstothecontrolbymakingthesamplesizeofthecontrol
largerthanforthetreatmentswhenthereismorethanonetreatmentandyouareonly
interestedinthecomparisonofeachtreatmenttothecontrol.If,however,aprimary
objectiveistocomparethetreatmentstoeachotherthenallgroupsshouldbeofthe
samesizeasgivenbyFormula2.)Thecoefficientof16intheformulaprovides80%
power,i.e.,ithasan80%probabilityofrejectingthenullhypothesisthatthereisno
differencebetweentheTreatmentandControlifthetruemeanisdifferentthanthetrue
Controlby(cid:2).EvenaroughestimateofstandarddeviationinFormula2canbehelpful
inplanninganexperiment.Replacethe16by21intheformulaabovetoincreasethe
powerto90%.
Amoreconservativeformulaforsamplesize(for90%power)hasbeensuggested
(Wheeler1974):
n =(4rσ/(cid:2))2 (3)
wherer isthenumberofvariants(assumedtobeapproximatelyequalinsize).The
formula is an approximation and intentionally conservative to account for multiple
123

Controlledexperimentsontheweb 153
comparisonissueswhenconductingananalysisofvariancewithmultiplevariantsper
factor(Wheeler1975;vanBelle2002).Theexamplesbelowusethefirstformula.
3.2.1 Example:impactoflower-variabilityOEConthesamplesize
Suppose you have an e-commerce site and 5% of users who visit during the
experiment period end up purchasing. Those purchasing spend about $75. The
average user therefore spends $3.75 (95% spend $0). Assume the standard devia-
tionis$30.IfyouarerunninganA/Btestandwanttodetecta5%changetorevenue,
you will need over 409,000 users to achieve the desired 80% power, based on the
aboveformula:16∗302/(3.75∗0.05)2.
If,however,youwereonlylookingfora5%changeinconversionrate(notrevenue),
alowervariabilityOECbasedonpoint3.bcanbeused.Purchase,aconversionevent,
is modeled as a Bernoulli trial with p = √0.05 being the probability of a purchase.
ThestandarddeviationofaBernoulliis p(1− p)andthusyouwillneedlessthan
122,000userstoachievethedesiredpowerbasedon16∗(0.05·(1−0.05))/(0.05·
0.05)2.
UsingconversionastheOECinsteadofpurchasingspendcanthusreducethesam-
ple size required for the experiment by a factor of 3.3. Because the number of site
visitorsisapproximatelylinearintherunningtimefortheexperiment(thenumberof
distinctusersissublinearduetorepeatvisitors,butalinearapproximationisreason-
ableformostsites),thiscanreducetherunningtimeoftheexperimentfrom6weeks
to2weeks,andthusisworthconsidering.
3.2.2 Example:impactofreducedsensitivityonthesamplesize
Because the sensitivity, (cid:2), is squared in the formula for sample size, if the desired
sensitivityisreducedtosupportdetectinga20%changeinconversioninsteadof5%
(afactorof4),thenumberofusersneededdropsbyafactorof16to7,600.
Aswillbediscussedlateron,thisisthereasonthatdetectingabugintheimplemen-
tationcanbedonequickly.Supposeyouplananexperimentthatwillallowdetecting
a1%changeintheOEC,butabugintheimplementationexposesuserstoabadexpe-
rienceandcausestheOECtodropby20%.Suchabugcanbedetectednotin1/20th
oftheplannedrunningtime,butin1/400thoftherunningtime.Iftheexperimentwas
plannedtorunfortwoweeks,youcandetectanegregiousprobleminthefirsthour!
3.2.3 Example:filteringusersnotimpactedbythechange
If you made a change to the checkout process, you should only analyze users who
started the checkout process (point 3.c), as others could not see any difference and
thereforejustaddnoise.Assumethat10%ofusersinitiatecheckoutandthat50%of
thoseuserscompleteit.ThisusersegmentismorehomogenousandhencetheOEC
haslowervariability.Usingthesamenumbersasbefore,theaverageconversionrateis
0.5,thestd-devis0.5,andthusyouwillneedonly6,400usersgoingthroughcheckout
todetecta5%changebasedon16∗(0.5(1−0.5))/(0.5·0.05)2.Sinceweexcluded
the90%whodonotinitiate,thetotalnumberofuserstothewebsiteshouldbe64,000,
123

154 R.Kohavietal.
whichisalmosthalfthepreviousresultof122,000,thustheexperimentcouldrunfor
halfthetimeandyieldthesamepower.
3.2.4 ThechoiceofOECmustbemadeinadvance
Whenrunningexperiments,itisimportanttodecideinadvanceontheOEC(aplanned
comparison);otherwise,thereisanincreasedriskoffindingwhatappeartobesignif-
icantresultsbychance(familywisetypeIerror)(Keppeletal.1992).Severaladjust-
mentshavebeenproposedintheliterature(e.g.,Fisher’sleast-significant-difference,
Bonferroniadjustment,Duncan’stest,Scheffé’stest,Tukey’stest,andDunnett’stest),
buttheybasicallyequatetoincreasingthe95%confidencelevelandthusreducingthe
statisticalpower(Masonetal.1989;Boxetal.2005;Keppeletal.1992).
3.3 Confidenceintervalsforabsoluteandpercenteffect
ItisusefultogiveaconfidenceintervalforthedifferenceinthemeansoftheTreatment
andControlinadditiontotheresultsofthehypothesistest.Theconfidenceinterval
gives arangeofplausiblevalues forthesizeoftheeffectoftheTreatment whereas
thehypothesistestonlydeterminesifthereisastatisticallysignificantdifferencein
themean.
3.3.1 Confidenceintervalsforabsoluteeffect
The formula for the confidence interval for the difference in two means is fairly
straightforward.Usingthenotationdevelopedpreviously,theupperandlowerbounds
fora95%confidenceintervalare
CILimits= O −O ±1.96∗σ(cid:1) (4)
B A d
One could use the confidence interval for the absolute affect to conduct a hypothe-
sis test—if zero is in the interval you would not reject H , otherwise reject H and
0 0
concludetheTreatmenthasaneffect.
3.3.2 Confidenceintervalsforpercenteffect
Formanyonlinemetrics,thedifferenceinthemeansissosmallthatpercentchange
has much more intuitive meaning than the absolute difference. For example, for a
recent experiment, the treatment effect for specific clickthrough rate was 0.00014.
Thistranslatedtoa12.85%changeduetotheTreatment.Thelatternumberwasmuch
moremeaningfultodecisionmakers.Thepercentdifferenceiscalculatedby
O −O
PctDiff= B A ∗100% (5)
O
A
123

Controlledexperimentsontheweb 155
However,formingaconfidenceintervalaroundthepercentchangeisnotastraightfor-
wardextensionoftheconfidenceintervalfortheabsoluteeffect.Thisisbecausewe
arenowdividingbyarandomvariable.Theinitialderivationofthisintervalisdueto
Fieller(WillanandBriggs2006).Notethatifthedenominatorisstochasticallyclose
tozerooneorbothendpointswillnotexist.Inpractice,youshouldn’tcalculatethis
intervaliftheconfidenceintervalforthedenominatorcontainszero.
Definethecoefficientofvariationofthetwogroupstobe
σ(cid:2)
CV = B
B
O
B
σ(cid:2)
CV = A
B
O
A
Thelowerandupperboundsfora95%confidenceintervalforthepercentdifference
are
CIforPercentEffect=(PctDiff+1)
(cid:3)
1±1.96∗ CV2+CV2−(1.962)∗CV2∗CV2
∗ A B A B −1
1−(1.96)∗CV2
A
(6)
These formulas assume the covariance between the Treatment and Control mean is
zerowhichwillbetrueinacontrolledexperimentwhentherandomizationiscarried
outproperly.
3.4 Effectofrobotsonexperimentalresults
Robotscanintroducesignificantskewintoestimates,enoughtorenderassumptions
invalid.Wehaveseencaseswhererobotscausedmanymetricstobesignificantwhen
theyshouldnothavebeen(e.g.,muchmorethan5%falsepositivesforanA/Atest).
Forthepurposeofexperimentation,itisespeciallyimportanttoremovesometypes
ofrobots,thosethatinteractwiththeuser-id.Forsomewebsitesrobotsarethoughtto
provideuptohalfthepageviewsonthesite(Kohavietal.2004).Sincemanyrobots
havethesamecharacteristicsashumanusersitisdifficulttoclearlydelineatebetween
the two. Benign or simple robots can often be filtered by basic characteristics (e.g.
useragent,IPaddress)butmanymodernrobotsusesophisticatedtechniquestoescape
detectionsandfiltering(TanandKumar2002).
3.4.1 JavaScriptversusserver-sidecall
Itisgenerallythoughtthatveryfewrobotswillbeincludedintheexperimentifthe
treatmentassignmentiscalledbyJavaScriptsothoseexperimentalsetupsshouldn’t
beaffectedasmuchbyrobots.Thisshouldbevalidatedbytheexperimenter.
123

156 R.Kohavietal.
3.4.2 Robotsthatrejectcookies
Werecommendexcludingunidentifiedrequestsfromtheanalysis,sothatrobotsthat
rejectcookieswillnotbepartoftheexperimentalresults.Ifthetreatmentassignment
anddatacollectionisbasedonlyonuserswithauserIDstoredintheuser’scookie,
theserobotswillnotbecountedinthenumberofusersorinthedatathatiscollected
onuserbehavior.
3.4.3 Robotsthatacceptcookies
Ifarobotacceptscookiesanddoesnotdeletethem,theeffectcanbeprofound,espe-
ciallyiftherobothasalargenumberofactionsonthesite.Wehavefoundthatthereare
usuallyarelativelysmallnumberoftheserobotsbuttheirpresenceintheTreatmentor
Controlcanseriouslybiasthecomparison.Forexample,wehavefoundsomerobots
that have up to 7,000 clicks on a page in an hour or more than 3,000 page views in
a day. Any hypothesis test comparing Treatment and Control when these robots are
present can be very misleading. These robots will not only bias the estimate of the
effect, they also increase the standard deviation of many metrics, thus reducing the
power.
Therefore,weneedtoaggressivelyfilteroutrobotsthatdonotdeletecookiesand
havealargenumberofactions(e.g.pageviewsorclickthroughs(triggeredbyonclick
JavaScript handlers)) for a single user-id. Robots that either do not accept cookies
or clear cookies after one or only a few actions will not have much of an effect on
thecomparisonofTreatmenttoControl.Robotfilteringcanbeaccomplishedthrough
a combination of omitting users whose user agent is on a list of known robots and
through the use of heuristics (Kohavi 2003). The heuristics may vary depending on
thewebsite.
3.5 Extensionsforonlinesettings
Several extensions to basic controlled experiments are possible in an online setting
(e.g.,ontheweb).
3.5.1 Treatmentramp-up
AnexperimentcanbeinitiatedwithasmallpercentageofusersassignedtotheTreat-
ment(s),andthenthatpercentagecanbegraduallyincreased.Forexample,ifyouplan
torunanA/Btestat50%/50%,youmightstartwitha99.9%/0.1%split,thenrampup
theTreatmentfrom0.1%to0.5%to2.5%to10%to50%.Ateachstep,whichcould
run for, say, a couple of hours, you can analyze the data to make sure there are no
egregiousproblemswiththeTreatmentbeforeexposingittomoreusers.Thesquare
factorinthepowerformulaimpliesthatsucherrorscouldbecaughtquicklyonsmall
populationsandtheexperimentcanbeabortedbeforemanyusersareexposedtothe
badTreatment.
123

Controlledexperimentsontheweb 157
3.5.2 Automation
OnceanorganizationhasaclearOEC,itcanrunexperimentstooptimizecertainareas
amenabletoautomatedsearch.Forexample,theslotsonthehomepageatAmazon
areautomaticallyoptimized(Kohavietal.2004).Ifdecisionshavetobemadequickly
(e.g., headline optimizations for portal sites), these could be made with lower con-
fidence levels because the cost of mistakes is lower. Multi-armed bandit algorithms
(Wikepedia2008)andHoeffdingRaces(MaronandMoore1994)canbeusedforsuch
optimizations.
3.5.3 Softwaremigrations
Experimentscanbeusedtohelpwithsoftwaremigration.Ifafeatureorasystemis
beingmigratedtoanewbackend,newdatabase,oranewlanguage,butisnotexpected
tochangeuser-visiblefeatures,anA/Btestcanbeexecutedwiththegoalofretaining
theNullHypothesis,whichisthatthevariantsarenotdifferent.Wehaveseenseveral
suchmigrations,wherethemigrationwasdeclaredcomplete,butanA/Btestshowed
significantdifferencesinkeymetrics,helpingidentifybugsintheport.Becausethe
goalhereistoretaintheNullHypothesis,itiscrucialtomakesuretheexperimenthas
enoughstatisticalpowertoactuallyrejecttheNullHypothesisifitfalse.
3.6 Limitations
Despite significant advantages that controlled experiments provide in terms of
causality,theydohavelimitationsthatneedtobeunderstood.Some,whicharenoted
inthePsychologyliteraturearenotrelevanttotheweb(Rossietal.2003,pp.252–262;
Weiss1997),butsomelimitationsweencounteredarecertainlyworthnoting.
1. Quantitativemetrics,butnoexplanations.Itispossibletoknowwhichvariantis
better,andbyhowmuch,butnot“why.”Inuserstudies,forexample,behavioris
oftenaugmentedwithusers’comments,andhenceusabilitylabscanbeusedto
augmentandcomplementcontrolledexperiments(Nielsen2005).
2. Short term versus long term effects. Controlled experiments measure the effect
on the OEC during the experimentation period, typically a few weeks. While
someauthors have criticizedthatfocusing onametricimpliesshort-termfocus
(Quarto-vonTivadar2006;Nielsen2005),wedisagree.Long-termgoalsshouldbe
partoftheOEC.Letustakesearchadsasanexample.IfyourOECisrevenue,you
mightplasteradsoverapage,butweknowthatmanyadshurttheuserexperience,
soagoodOECshouldincludeapenaltytermofusageofreal-estateforadsthat
are not clicked, and/or should directly measure repeat visits and abandonment.
Likewise, it is wise to look at delayed conversion metrics, where there is a lag
from the time a user is exposed to something and take action. These are some-
timescalledlatentconversions(Miller2006;Quarto-vonTivadar2006).Coming
upwithgoodOECsishard,butwhatisthealternative?Thekeypointhereisto
recognizethislimitation,butavoidthrowingthebabyoutwiththebathwater.
123

158 R.Kohavietal.
3. Primacy and newness effects. These are opposite effects that need to be recog-
nized.Ifyouchangethenavigationonawebsite,experiencedusersmaybeless
efficientuntiltheygetusedtothenewnavigation,thusgivinganinherentadvan-
tagetotheControl.Conversely,whenanewdesignorfeatureisintroduced,some
userswillinvestigateit,clickeverywhere,andthusintroducea“newness”bias.
ThisbiasissometimesassociatedwiththeHawthorneeffect(2007).Bothprimacy
andnewnessconcernsimplythatsomeexperimentsneedtoberunformultiple
weeks.OneanalysisthatcanbedoneistocomputetheOEConlyfornewusers
onthedifferentvariants,sincetheyarenotaffectedbyeitherfactor.
4. Featuresmustbeimplemented.Alivecontrolledexperimentneedstoexposesome
userstoaTreatmentdifferentthanthecurrentsite(Control).Thefeaturemaybe
aprototypethatisbeingtestedagainstasmallportion,ormaynotcoveralledge
cases(e.g.,theexperimentmayintentionallyexclude20%ofbrowsertypesthat
wouldrequiresignificanttesting).Nonetheless,thefeaturemustbeimplemented
andbeofsufficientqualitytoexposeuserstoit.Nielsen(2005)correctlypoints
outthatpaperprototypingcanbeusedforqualitativefeedbackandquickrefine-
mentsofdesignsinearlystages.Weagreeandrecommendthatsuchtechniques
complementcontrolledexperiments.
5. Consistency.Usersmaynoticetheyaregettingadifferentvariantthantheirfriends
andfamily.Itisalsopossiblethatthesameuserwillseemultiplevariantswhen
usingdifferentcomputers(withdifferentcookies).Itisrelativelyrarethatusers
willnoticethedifference.
6. Parallelexperiments.Ourexperienceisthatstronginteractionsarerareinpractice
(vanBelle2002),andwebelievethisconcernisoverrated.Raisingawarenessof
thisconcernisenoughforexperimenterstoavoidteststhatcaninteract.Pairwise
statisticaltestscanalsobedonetoflagsuchinteractionsautomatically.
7. LaunchEventsandMediaAnnouncements.Ifthereisabigannouncementmade
aboutanewfeature,suchthatthefeatureisannouncedtothemedia,allusersneed
toseeit.
4 MultiVariableTesting1
AnexperimentthatincludesmorethanonefactorisoftencalledaMultiVariabletest
(MVT)(AltandUsborne2005).Forexample,considertestingfivefactorsontheMSN
homepageinasingleexperiment.AscreenshotoftheMSNhomepageshowingthe
controlforeachofthesefactorsisgiveninFig.8.
1 ThisisalsoknownasMultivariatetesting.WeusethetermMultiVariableTestingfortworeasons.These
testswerefirstcalledMultiVariableTestsin1996inanarticleinForbes(Koselka1996)referringtodesigned
experimentsinareasincludingsalesandmarketing.Inaddition,thesetestsarepartofthestatisticalliterature
intheDesignofExperimentsfield.Thereisaseparatefieldofstatisticsknownasmultivariatestatisticsthat
doesnotdealwiththistopicsousingthetermmultivariatecouldbeasourceofconfusion.
123

Controlledexperimentsontheweb 159
Factor Control Treatment
F1 Shoppingmoduleasabove AddOffersmodulebelow
F2 Shoppingmoduleasabove Redborderandheading
F3 MoneyandQuotesasabove MergeintooneMoneymodule
F4 Staticadshowntoeveryone Adshowndependsonrecentuserbehavior
F5 Videoheadlineschosenbyeditors Orderofheadlineschosenbypopularity/competition
In a single test we can estimate the (main) effects of each factor as well as the
interactive effects between factors. First, we will consider the benefits and limita-
tions of MVT versus one-factor-at-a-time, or A/B tests. Then we will discuss three
approachestoonlineMVTsandhoweachapproachtakesadvantageofthepotential
benefitsandmitigatesthelimitations.
There are two primary benefits of a single MVT versus multiple sequential A/B
teststotestthesamefactors:
1. You can test many factors in a short period of time, accelerating improvement.
Forexample,ifyouwantedtotestfivechangestothewebsiteandyouneedtorun
eachA/Btestfourweekstoachievethepoweryouneed,itwilltakeatleastfive
Fig.8 ScreenshotofMSNHomepagewithcontrolsforthefivefactors
123

160 R.Kohavietal.
monthstocompletetheA/Btests.However,youcouldrunasingleMVTwithall
fivefactorsinonemonthwiththesamepoweraswiththefiveA/Btests.
2. Youcanestimateinteractionsbetweenfactors.Twofactorsinteractiftheircom-
binedeffectisdifferentfromthesumofthetwoindividualeffects.Ifthetwofactors
worktogethertoenhancetheoutcometheinteractionissynergistic.Ifinsteadthey
workagainsteachothertodampentheeffect,theinteractionisantagonistic.
Threecommonlimitationsare:
1. Somecombinationsoffactorsmaygiveapooruserexperience.Forexample,two
factors being tested for an online retailer may be enlarging a product image or
providingadditionalproductdetail.Bothmayimprovesaleswhentestedindivid-
ually, but when both are done at the same time the “buy box” is pushed below
thefoldandsalesdecrease.Thiswouldbealargeantagonisticinteraction.This
interactionshouldbecaughtintheplanningphasesothatthesetwofactorswould
notbetestedatthesametime.
2. Analysisandinterpretationaremoredifficult.Forasinglefactortestyoutypically
havemanymetricsfortheTreatment-Controlcomparison.ForanMVTyouhave
thesamemetricsformanyTreatment-Controlcomparisons(atleastoneforeach
factorbeingtested)plustheanalysisandinterpretationoftheinteractionsbetween
thefactors.Certainly,theinformationsetismuchricherbutitcanmakethetask
ofassessingwhichtreatmentstorolloutmorecomplex.
3. Itcantakelongertobeginthetest.Ifyouhavefivefactorsyouwanttotestand
plantotestthemoneatatimeyoucanstartwithany ofthosethatarereadyto
betestedandtesttheotherslater.WithanMVTyoumusthaveallfivereadyfor
testingatthebeginningofthetest.Ifanyoneisdelayed,thiswoulddelaythestart
ofthetest.
Wedon’tbelieveanyofthelimitationsareseriousonesinmostcases,buttheyshould
berecognizedbeforeconductinganMVT.Generally,webelievethefirstexperiment
onedoesshouldbeanA/Btestmainlyduetothecomplexityoftestingmorethanone
factorinthesametest.
TherearethreeoverarchingphilosophiestoconductingMVTswithonlineproper-
ties.
4.1 TraditionalMVT
Thisapproachusesdesignsthatareusedinmanufacturingandotherofflineapplica-
tions. These designs are most often fractional factorial (Davies and Hay 1950) and
PlackettandBurman(1946)designsthatarespecificsubsetsoffullfactorialdesigns
(allcombinationsoffactorlevels).ThesedesignswerepopularizedbyGenichiTaguchi
andaresometimesknownasTaguchidesigns.Theusermustbecarefultochoosea
designthatwillhavesufficientresolutiontoestimatethemaineffectsandinteractions
thatareofinterest.
ForourMSNexampleweshowdesignsforatestofthesefivefactorswithafull
factorial,afractionalfactorialoraPlackett-Burmandesign.
123

| Controlledexperimentsontheweb |     |     |     | 161 |
| ----------------------------- | --- | --- | --- | --- |
Table1 Fractionalfactorial
|     | Usergroups | Factorlevelsassignedtoeachgroup |     |     |
| --- | ---------- | ------------------------------- | --- | --- |
designtotestfivefactorswith
| eightusergroups |     | F1 F2 | F3 F4 | F5  |
| --------------- | --- | ----- | ----- | --- |
|                 | 1   | −1 −1 | −1 1  | 1   |
|                 |     | −1 −1 |       | −1  |
|                 | 2   |       | 1 1   |     |
|                 |     | −1    | −1 −1 |     |
|                 | 3   | 1     |       | 1   |
|                 |     | −1    | −1    | −1  |
|                 | 4   | 1     | 1     |     |
|                 | 5   | 1 −1  | −1 −1 | −1  |
|                 | 6   | 1 −1  | 1 −1  | 1   |
|                 | 7   | 1 1   | −1 1  | −1  |
|                 | 8   | 1 1   | 1 1   | 1   |
|                 |     |       | 25 =  |     |
Full factorial has all combinations of the factors which would be 32 user
groups.Afractionalfactorialisafractionofthefullfactorialthathas2K usergroups
andeachcolumnisorthogonaltotheotherfourcolumns.Thereareobviouslymany
=3isgiven
suchfractionswith8and16usergroups.Onefractionalfactorialfor K
inTable1where−1denotesthecontroland1denotesthetreatment.
Plackett–Burmandesignscanbeconstructedwherethefactorsareallattwolevels
with the number of user groups being a multiple of 4, so 4, 8, 12, 16, 20, etc. The
number of factors that can be tested for any of these designs is the number of user
groupsminusone.IfthenumberofusergroupsisapoweroftwothePlackett–Burman
designisalsoafractionalfactorial.
Aswiththefractionalfactorials,thereareusuallymanyPlackett–Burmandesigns
thatcouldbeusedforagivennumberofusergroups.
In the statistical field of Design of Experiments, a major research area is to find
designsthatminimizethenumberofusergroupsneededforthetestwhileallowing
you to estimate the main effects and interactions with little or no confounding. The
fractional factorial in Table1 can estimate all five main effects but cannot estimate
interactionswell(Boxetal.2005,pp.235–305).Formanyexperimentersoneofthe
primary reasons for running an MVT is to estimate the interactions among the fac-
tors being tested. You cannot estimate any interactions well with this design since
allinteractionsaretotallyconfoundedwithmaineffectsorothertwo-factorinterac-
tions.Noamountofeffortatanalysisordataminingwillallowyoutoestimatethese
interactionsindividually.Ifyouwanttoestimatealltwofactorinteractionswithfive
factorsyouwillneedafractionalfactorialdesignwith16treatmentcombinations.The
Placket–BurmandesigninTable2hasalltwofactorinteractionspartiallyconfounded
withmaineffectsandothertwofactorinteractions.Thismakestheestimationofthese
twofactorinteractionschallenging.
WerecommendtwoalternativesthatwebelievearebetterthanthetraditionalMVT
approach for online tests. The one you prefer will depend on how highly you value
estimatinginteractions.
4.2 MVTbyrunningconcurrenttests
Fractionsofthefullfactorialareusedinofflinetestingbecausethereisusuallyacost
to using more treatment combinations even when the number of experimental units
123

| 162 |     |     |     |     | R.Kohavietal. |
| --- | --- | --- | --- | --- | ------------- |
Table2 Plackett–Burman
|     | Usergroups | Factorlevelsassignedtoeachgroup |     |     |     |
| --- | ---------- | ------------------------------- | --- | --- | --- |
designtotestfivefactorswith12
| usergroups |     | F1  | F2  | F3  | F4 F5 |
| ---------- | --- | --- | --- | --- | ----- |
|            | 1   | 1   | 1   | 1   | 1 1   |
|            |     | −1  |     | −1  |       |
|            | 2   |     | 1   |     | 1 1   |
|            |     | −1  | −1  |     | −1    |
|            | 3   |     |     | 1   | 1     |
|            |     |     | −1  | −1  | −1    |
|            | 4   | 1   |     |     | 1     |
|            | 5   | −1  | 1   | −1  | −1 1  |
|            | 6   | −1  | −1  | 1   | −1 −1 |
|            | 7   | −1  | −1  | −1  | 1 −1  |
|            | 8   | 1   | −1  | −1  | −1 1  |
|            | 9   | 1   | 1   | −1  | −1 −1 |
|            | 10  | 1   | 1   | 1   | −1 −1 |
|            |     | −1  |     |     | −1    |
|            | 11  |     | 1   | 1   | 1     |
−1
|     | 12  | 1   |     | 1   | 1 1 |
| --- | --- | --- | --- | --- | --- |
does not increase. This does not have to be the case with tests conducted with web
sites.Ifwesetupeachfactortorunasaone-factorexperimentandrunallthesetests
concurrentlywecansimplifyoureffortandgetafullfactorialintheend.Inthismode
westartandstopalltheseone-factortestsatthesametimeonthesamesetofusers
withusersbeingindependentlyrandomlyassignedtoeachexperiment.Theendresult
isyouwillhaveafullfactorialexperimentinallthefactorsyouaretesting.Ofcourse,
with a full factorial you will be able to estimate any interaction you want. A side
benefitofthisapproachisthatyoucanturnoffanyfactoratanytime(forexampleifa
treatmentforafactorisdisastrous)withoutaffectingtheotherfactors.Theexperiment
thatincludestheremainingfactorsisnotaffected.
Itiscommonlythoughtthatthepoweroftheexperimentdecreaseswiththenumber
of treatment combinations (cells). This may be true if the analysis is conducted by
comparingeachindividualcelltotheControlcell.However,iftheanalysisisthemore
traditionaloneofcalculatingmaineffectsandinteractionsusingallthedataforeach
effect, little or no power is lost. (A very slight loss of power could occur if one of
the factors of combination of factors increases the variation of the response. Using
a pooled estimate for experimental error will minimize any loss of power.) If your
samplesize(e.g.numberofusers)isfixed,itdoesn’tmatterifyouaretestingasingle
factorormanyorwhetheryouareconductinganeightrunMVTorafullfactorialthe
powertodetectadifferenceforanymaineffectisthesame(Boxetal.2005).There
aretwothingsthatwilldecreaseyourpower,though.Oneisincreasingthenumber
oflevels(variants)forafactor.Thiswilleffectivelydecreasethesamplesizeforany
comparisonyouwanttomake,whetherthetestisanMVToranA/Btest.Theotheris
toassignlessthan50%ofthetestpopulationtothetreatment(iftherearetwolevels).
ItisespeciallyimportantfortreatmentsinanMVTtohavethesamepercentageofthe
populationastheControl.
4.3 Overlappingexperiments
Thisapproachistosimplytestafactorasaone-factorexperimentwhenthefactoris
readytobetestedwitheachtestbeingindependentlyrandomized.Itisdistinctfromthe
123

Controlledexperimentsontheweb 163
previousSect.(4.2)inthathereeachexperimentturnsonwhenthetreatmentisready
togoratherthanlaunchingallfactorsofafactorialdesignatonce.Inanagilesoftware
developmentworld,therearesignificantbenefitstorunningmoretestsfrequently,as
theyarereadytobedeployed.Thesetestscanbegoingonsimultaneouslyifthereis
noobvioususerexperience issuewiththecombinations thatcouldbeshowntoany
visitor.Thisistheapproachyoushouldtakeifyouwanttomaximizethespeedwith
which ideas are tested and you are not interested in or concerned with interactions.
Largeinteractionsbetweenfactorsareactuallyrarerthanmostpeoplebelieve,unless
they are already known, such as with the buy box example. This is a much better
alternativethanthetraditionalapproachmentionedfirst.Withthetraditionalapproach
youhavethelimitationthatyoucan’ttestuntilallthefactorsarereadytobetested.In
addition,whenyou’redone(withmanytestdesignsthatarerecommended)youwon’t
beabletoestimateinteractionswellifatall.Withoverlappingexperimentsyoutest
thefactorsmorequicklyand,ifthereissufficientoverlapinanytwofactors,youcan
estimatetheinteractionbetweenthosefactors.Ifyouareespeciallyinterestedinthe
interactionbetweentwospecificfactorsyoucanplantotestthosefactorsatthesame
time.
WebelievethetwoalternativespresentedabovearebetterthanthetraditionalMVT
approachforonlineexperiments.Theoneyouusewoulddependonyourpriorities.If
youwanttotestideasasquicklyaspossibleandaren’tconcernedaboutinteractions,
usetheoverlappingexperimentsapproach.Ifitisimportanttoestimateinteractions
run the experiments concurrently with users being independently randomized into
eachtesteffectivelygivingyouafullfactorialexperiment.
5 Implementationarchitecture
Implementing an experiment on a website involves three components. The first
componentistherandomizationalgorithm,whichisafunctionthatmapsendusersto
variants.Thesecondcomponentistheassignmentmethod,whichusestheoutputof
therandomizationalgorithmtodeterminetheexperiencethateachuserwillseeonthe
website.Thethirdcomponentisthedatapath,whichcapturesrawobservationdata
as the users interact with the website, aggregates it, applies statistics, and prepares
reportsoftheexperiment’soutcome.
5.1 Randomizationalgorithm
Findingagoodrandomizationalgorithmiscriticalbecausethestatisticsofcontrolled
experimentsassumethateachvariantofanexperimentisassignedarandomsample
ofendusers.Randomizationalgorithmsmusthavethefollowingthreepropertiesto
supportstatisticallycorrectexperiments(usingthemethodologypresentedabove):
1. Endusersmustbeequallylikelytoseeeachvariantofanexperiment(assuming
a50–50split).Thereshouldbenobiastowardanyparticularvariant.
2. Repeatassignmentsofasingleendusermustbeconsistent;theendusershould
beassignedtothesamevariantoneachsuccessivevisittothesite.
123

164 R.Kohavietal.
3. Whenmultipleexperimentsarerun,theremustbenocorrelationbetweenexper-
iments. An end user’s assignment to a variant in one experiment must have no
effectontheprobabilityofbeingassignedtoavariantinanyotherexperiment.
Randomization algorithms may optionally support the following two desirable
properties:
4. Thealgorithmmaysupportmonotonicramp-up,meaningthatthepercentageof
userswhoseeaTreatmentcanbeslowlyincreasedwithoutchangingtheassign-
mentsofuserswhowerepreviouslyassignedtothatTreatment.Supportingthis
propertyallowstheTreatmentpercentagetobeslowlyincreasedwithoutimpair-
ingtheuserexperienceordamagingthevalidityoftheexperiment.
5. Thealgorithmmaysupportexternalcontrol,meaningthatuserscanbemanually
forced into and out of variants. This property makes it easier to test the experi-
mentalsite.
The remainder of this section will only consider techniques that satisfy at least the
firstthreeproperties.
5.1.1 Pseudorandomwithcaching
A standard pseudorandom number generator can be used as the randomization
algorithmwhencoupledwithaformofcaching.Agoodpseudorandomnumbergen-
erator will, by itself, satisfy the first and third requirements of the randomization
algorithm.
Wetestedseveralpopularrandomnumbergeneratorsontheirabilitytosatisfythe
firstandthirdrequirements.Wetestedfivesimulatedexperimentsagainstonemillion
sequentialuserIDs,runningchi-squareteststolookforinteractions.Wefoundthatthe
randomnumbergeneratorsbuiltintomanypopularlanguages(forexample,C#)work
wellaslongasthegeneratorisseededonlyonceatserverstartup.Seedingtherandom
numbergeneratoroneachrequestmaycauseadjacentrequeststousethesameseed
which may (as it did in our tests) introduce noticeable correlations between exper-
iments. In particular, we found that the technique employed by Eric Peterson using
VisualBasic(Peterson2005)createstwo-wayinteractionsbetweenexperiments.
Tosatisfythesecondrequirement,thealgorithmmustintroducestate:theassign-
mentsofendusersmustbecachedoncetheyvisitthesite.Thecachingcanbeaccom-
plishedeitherontheserverside(bystoringtheassignmentsforallusersinsomeform
ofdatabase),orontheclientside(bystoringauser’sassignmentinacookie).
Thedatabaseapproachisexpensive(inhardware),andhasspacerequirementsthat
increaselinearlywiththenumberofexperimentsandthenumberofusers.However,
it easily satisfies the fifth property by allowing the user assignment database to be
modified. The cookie approach is significantly cheaper, requiring no database and
costingonlyalinearamountofspaceinthenumberofexperiments(thistimewithin
theuser’scookie).Itwillnotworkforuserswithcookiesturnedoff.
Bothformsofthisapproacharedifficulttoscaleuptoalargesystemwithalarge
fleet of servers. The server making the random assignment must communicate its
state to all the other servers (including those used for backend algorithms) in order
123

Controlledexperimentsontheweb 165
tokeepassignmentsconsistent.Thissortofpropagationisexpensiveanddifficultto
implementcorrectly.
The fourth requirement (monotonic ramp-up) is difficult to implement using this
method,andsomanysystemsignoretherequirementaltogether.Regardlessofwhich
approachisusedtomaintainstate,thesystemwouldneedtocarefullyreassignCon-
troluserswhovisitthesiteafteraramp-up.Thedifficultycomesindeterminingthe
percentageTreatmenttoassigntotheseuserssothattheoverallTreatmentpercentage
reachesthedesiredvalue.
5.1.2 Hashandpartition
Thismethodeliminatestheneedforcachingbyreplacingtherandomnumbergenerator
withahashfunction.Unlikearandomnumbergenerator,whichproducesrandomly
distributednumbersindependentofanyinput,a(good)hashfunctionproducesran-
domly distributed numbers as a function of a specific input. The method works as
follows: each user is assigned a single unique identifier which is maintained either
throughadatabaseoracookie.Likewise,eachexperimentisassignedauniqueiden-
tifier. A hash function is applied to the combination of the user identifier and the
experiment identifier (e.g. by concatenating them together) to obtain an integer that
isuniformlydistributedonarangeofvalues.Therangeisthenpartitioned,witheach
variantrepresentedbyapartition.Theuniqueuseridentifiermaybereusedacrossany
numberofexperiments.
Thismethodisverysensitivetothechoiceofhashfunction.Ifthehashfunction
hasanyfunnels(instanceswhereadjacentkeysmaptothesamehashcode)thenthe
first property (uniform distribution) will be violated. And if the hash function has
characteristics(instanceswhereaperturbationofthekeyproducesapredictableper-
turbation of the hash code), then correlations may occur between experiments. Few
hashfunctionsaresoundenoughtobeusedinthistechnique.
Wetestedthistechniqueusingseveralpopularhashfunctionsandamethodology
similartotheoneweusedonthepseudorandomnumbergenerators.Whileanyhash
functionwillsatisfythesecondrequirement(bydefinition),satisfyingthefirstandthird
is more difficult. We tested five simulated experiments against one million sequen-
tial user IDs. We ran chi-square tests to look for violations of the first and third
requirementsofarandomizationalgorithmandfoundthatonlythecryptographichash
functionMD5generatednocorrelationsbetweenexperiments.SHA256(anothercryp-
tographichash)cameclose,requiringafive-wayinteractiontoproduceacorrelation.
Otherhashfunctions(includingthestringhashingalgorithmbuiltinto.net)failedto
passevenatwo-wayinteractiontest.
Therunning-timeperformanceofthehashandpartitionapproachislimitedbythe
running-timeperformanceofthehashfunction,whichcanbeanissuebecausecrypto-
graphichasheslikeMD5areexpensiveandcleverattemptstoimprovetheperformance
throughpartialcachinggenerallyfail.Forexample,onesystemattemptedtocompute
separatehashesofboththeexperimentnameandtheenduserwhichwouldthenbe
XOR’dtogether.TheintentwastoavoidthecostofMD5bycachingthehashedexper-
iment name in the experiment, caching the hashed end user id in the user’s cookie,
andexecutingonlythefinalXORatassignmenttime.Thistechniqueproducessevere
123

166 R.Kohavietal.
correlationsbetweenexperiments:assumingtwoexperimentswithtwovariantseach
runningat50/50,ifthemostsignificantbitofthehashesoftheexperimentnamesfor
twoexperimentsmatched,userswouldalwaysgetthesameassignmentacrossboth
experiments.Iftheydidnotmatch,userswouldgetexactlytheoppositeassignment
between experiments. Either way, the third property is violated and results of both
experimentsareconfounded.
Satisfying the fifth property (external control) is very difficult with a raw hash
and partition approach. The simplest way to satisfy this property is to use a hybrid
approach, combining the hash and partition method with either a small database or
limiteduseofcookies.Becausethesetofuserssubjecttoexternalcontrolistypically
small(e.g.usersdesignedbyatestteam),thishybridapproachshouldnotencounter
thefulldisadvantagesofthepseudorandomwithcachingtechnique.
5.2 Assignmentmethod
Theassignmentmethodisthepieceofsoftwarethatenablestheexperimentingwebsite
toexecuteadifferentcodepathfordifferentendusers.Agoodassignmentmethodcan
manipulate anything from visible website content to backend algorithms. There are
multiplewaystoimplementanassignmentmethod.Intheremainderofthissection,
wecompareseveralcommonassignmentmethodsandrecommendbestpracticesfor
theiruse.
5.2.1 Trafficsplitting
Http Response (Control)
Http Request (Control)
Control
server(s)
Http Request
Client Browser Proxy Server
Treatment
server(s)
Http Request (Treatment)
Http Response (Treatment)
Trafficsplittingreferstoafamilyofassignmentmethodsthatinvolveimplementing
eachvariantofanexperimentonadifferentlogicalfleetofservers.Thesecanbedif-
ferentphysicalservers,differentvirtualservers,oreventdifferentportsonthesame
machine.Thewebsiteuseseitheraloadbalancerorproxyservertosplittrafficbetween
thevariantsandtherandomizationalgorithmmustbeembeddedatthislevel.Traffic
splitting has the advantage of being non-intrusive; no changes to existing code are
required to implement an experiment. However, the approach has significant disad-
vantages:
1. Runningexperimentsonsmallfeaturesisdisproportionatelydifficultbecausethe
entireapplicationmustbereplicatedregardlessofthesizeofthechange.
2. Settingupandconfiguringparallelfleetsistypicallyexpensive.TheControlfleet
must have sufficient capacity to take 100% of the traffic in the event that the
123

Controlledexperimentsontheweb 167
experiment needs to be shut down. The Treatment fleet(s) may be smaller, but
theirsizewilllimitthemaximumpercentagethatmaybeassignedtoeachTreat-
ment.
3. Runningmultipleexperimentsrequiresthefleettosupportonepartitionforeach
combinationofvariantsacrossallexperiments.Thisnumberincreasesasthenum-
beroftestedcombinationsincreases(potentiallyexponentiallyinthenumberof
simultaneousexperiments).
4. Anydifferencesbetweenthefleetsusedforeachvariantmayconfoundtheexper-
imentalresults.Ideally,thehardwareandnetworktopologyofeachfleetwillbe
identicalandA/Atestswillberuntoconfirmtheabsenceoffleet-relatedeffects.
The drawback of traffic splitting is that it is an expensive way to implement an
experiment,eventhoughthemethodappearscheapbecauseitminimizesIT/developer
involvement.Werecommend thismethodfortestingchanges thatintroducesignifi-
cantlydifferentcode,suchasmigrationtoanewwebsiteplatform,theintroduction
ofanewrenderingengine,oracompleteupgradeofawebsite.
5.2.2 Pagerewriting
Http Request
Web Server
Http Request
Client Browser Proxy Server
Original HTML
Modified HTML
Pagerewritingisanassignmentmethodthatincorporatesaspecialtypeofproxy
serverthatmodifiesHTMLcontentbeforeitispresentedtotheenduser.Usingthis
approach,theend-user’sbrowsersendsarequesttotheproxyserver,whichforwardsit
ontotheexperimentingwebsiteafterrecordingsomedata.Then,theHTMLresponse
from the experimenting website passes back through the proxy server on its way
to the end user’s browser. The proxy server applies the randomization algorithm,
selectsvariantsforoneormoreexperiments,andmodifiestheHTMLaccordingtothe
selectedvariants(e.g.byapplyingsubstitutionrulesexpressedasregularexpressionsor
XPathqueries).TheserverthensendsthemodifiedHTMLtotheenduser’sbrowser.
At least one commercial provider (SiteSpect 2008) offers a solution based on this
method.Liketrafficsplitting,thismethodisnon-intrusive.However,itstillincurssome
disadvantages:
1. Pagerendertimeisimpactedbytheactionoftheproxyserver.Rendertimewillbe
affectedbyboththetimerequiredtorewritetheHTMLandthenetworklatency
betweentheproxyserverandthewebserver.
2. Experimentationonlargesitesrequiressignificanthardware.Becausetheproxy
serversbothneedtohandleallpotentialtraffictothesiteandmaybecomeapoint
of failure, a large number of servers may be required to ensure scalability and
availabilityofthewebsite.
123

168 R.Kohavietal.
3. Developmentandtestingofvariantcontentismoredifficultandmoreerror-prone
than with other methods. Each variant must be expressed as a set of rules for
modifyingHTMLcoderatherthanastheHTMLcodeitself.
4. Runningexperimentsonbackendalgorithmsisdifficultbecausetheassignment
decisionismadeafterthepageisrenderedbythewebsite.
5. Runningexperimentsonencryptedtraffic(inparticular,pagesservedviahttps)is
resource-intensivebecausetheproxyservermustdecrypt,modify,andre-encrypt
the content. This represents a significant problem because the most interesting
partsofawebsite(suchasthecheckoutpage)arecommonlyencrypted.
Pagerewritingcanbeacheapmethodforexperimentingonfront-endcontentbecause
itminimizesIT/developerinvolvement.However,itisnotappropriatefortestingback-
endchangesorplatformmigrations.
5.2.3 Client-sideassignment
Ajax Call
Assignment
Server
Variant HTML
Client Browser
HTTP Request Web Server
Initial HTML
Client-side page modification is the most popular assignment method found in
third-partyexperimentationplatforms.Itissupportedbynumerousproductsincluding
Google Website Optimizer (2008), Omniture’s Offermatica (Omniture 2008), Inter-
woven’sOptimost(2008),Widemile(2008),andVerster(2008).
All of these products can run an experiment without making any decisions on
theserver.Adeveloper implementsanexperimentbyinsertingJavaScriptcodethat
instructstheenduser’sbrowsertoinvokeanassignmentserviceatrendertime.The
servicecallreturnstheappropriatevariantfortheenduser,andtriggersaJavaScript
callbackthatinstructsthebrowsertodynamicallyalterthepagebeingpresentedtothe
user,typicallybymodifyingtheDOM.Themodificationmustoccurbeforeanypartof
thepagerenders,soanylatencyintheservicecallwilladdtotheoverallpagerender
time.Thecontentforeachvariantcaneitherbecleverlyembeddedintothepageor
canbeservedbytheassignmentservice.Thismethod,althoughintrusive,canbevery
easytoimplement:allthedeveloperneedstodoisaddasmallsnippetofJavaScript
toapage.However,ithassomekeylimitations:
1. The client-side assignment logic executes after the initial page is served and
therefore delays the end user experience, especially if the assignment service
getsoverloadedoriftheenduserisonaslowconnectionorislocatedfarfrom
theassignmentserver.
2. Themethodisdifficulttoemployoncomplexsitesthatrelyondynamiccontent
becausecomplexcontentcaninteractwiththeJavaScriptcodethatmodifiesthe
page.
123

Controlledexperimentsontheweb 169
3. Enduserscandetermine(viathebrowser’sViewSourcecommand)thatapageis
subjecttoexperimentation,andmayeven(insomeimplementations)beableto
extractthecontentofeachvariant.
Note:someimplementationsofthismethodattempttooptimizerendertimebyavoid
theservicecalliftheenduserisknown(viacookie)tobeintheControl.Thisopti-
mizationisincorrect(andshouldnotbeused)becauseitcausestherendertimedelay
tobecomecorrelatedwithvariantassignment,therebyaddingaconfoundingfactorto
theexperiment.
Thismethodisbestforexperimentsonfront-endcontentthatisprimarilystatic.
5.2.4 Server-sideassignment
Service Call
Http Request
Client Browser Web Server Assignment
Server
Assignment
Final HTML
Server-sideassignmentreferstoafamilyofmethodsthatusecodeembeddedinto
thewebsite’sserverstoproduceadifferentuserexperienceforeachvariant.Thecode
takestheformofanAPIcallplacedatthepointwherethewebsitelogicdiffersbetween
variants. The API invokes the randomization algorithm and returns the identifier of
thevarianttobedisplayedforthecurrentuser.Thecallingcodeusesthisinformation
tobranchtoadifferentcodepathforeachvariant.TheAPIcallcanbeplacedany-
where on the server side, in front-end rendering code, back-end algorithm code, or
eveninthesite’scontent-managementsystem.Acomplexexperimentmaymakeuse
ofmultipleAPIcallsinsertedintothecodeatdifferentplaces.WhiletheAPIcanbe
implementedasalocalfunctioncall,ittypicallyusesanexternalservicetoensurethat
the assignment logic stays consistent across a large server fleet. Server-side assign-
ment is very intrusive; it requires deep changes to the experimenting application’s
code.Nonetheless,server-sideassignmenthasthreedistinctadvantages:
1. It is an extremely general method; it is possible to experiment on virtually any
aspectofapagesimplybymodifyingitscode.
2. Itplacestheexperimentationcodeinthebestlogicalplace—rightwheredecisions
are made about a change. In particular, it is possible to experiment on backend
features (for example, search and personalization algorithms) without touching
thefrontend.
3. Experimentationiscompletelytransparenttoendusers.Endusersexperienceonly
minimaldelayandcannotdiscernthatanexperimentisrunningonthesite.
Server-sideassignmentalsohasanumberofdisadvantages,allofwhicharestemfrom
itsintrusiveness:
123

170 R.Kohavietal.
1. Initial implementation is expensive. Depending on the complexity of the site,
implementingthenecessaryserver-sidecodechangescanbedifficult.
2. Becausethemethodrequiresadevelopertochangecodedeepinthepagelogic
for each experiment, implementing an experiment introduces risk. The risk is
greatest on complex features whose code is spread across many pages and/or
services.
3. Somevariationsofthismethodrequirecodechangestobemanuallyundoneto
completeanexperiment.Specifically,aprogrammermustremovethecodepath
thatimplementsthelosingtreatmentalongwiththeconditionallogicthatreacts
totheenduser’streatmentassignment.Whilethissimplyreferstocodeclean-up,
leavingthelosingtreatmentcodeintherecanyieldaverymessycodebase,while
removingitaddsrisksinceproductioncodewillbemodified.Whilethisprocessis
trivialforasimpleone-pageexperiment,itcanbeapainfulprocessifAPIcallsare
spreadthroughoutthecode,andallsuchcodechangesintroduceadditionalrisk.
Server-sideassignmentcanbeintegratedintoacontentmanagementsystemtogreatly
reducethecostofrunningexperimentsusingthismethod.Whensointegrated,exper-
iments are configured by changing metadata instead of code. The metadata may be
represented by anything from an editable configuration file to a relational database
managedbyagraphicaluserinterface.Themethodisbestillustratedwithanexample
fromarealsystemrunningatAmazon.com.
Amazon’shomepageisbuiltonacontentmanagementsystemthatassemblesthe
pagefromindividualunitscalledslots(Kohavietal.2004).Thesystemreferstopage
metadataatrendertimetodeterminehowtoassemblethepage.Non-technicalcontent
editorsschedulepiecesofcontentineachslotthroughagraphicaluserinterfacethat
edits this page metadata. Content can include anything from an advertisement, to a
productimage,toasnippetoftextfilledwithlinks,toawidgetthatdisplaysdynamic
content (such as personalized recommendations). A typical experiment would be to
try various pieces of content in different locations. For example, do the recommen-
dationsreceivehigherclickthroughontheleftorontheright?Toenablethissortof
experiment, the content management system is extended to allow pieces of content
tobescheduledwithrespecttoaspecificexperiment.Asthepagerequestcomesin,
thesystemexecutestheassignmentlogicforeachscheduledexperimentandsavesthe
resultstopagecontextwherethepageassemblymechanismcanreacttoit.Thecontent
managementsystemonlyneedstobemodifiedonce;fromthenon,experimentscan
bedesigned,implemented,andremovedbymodifyingthepagemetadatathroughthe
userinterface.
5.2.5 Summary
The following table summarizes the relative advantages and disadvantages of all of
theassignmentmethodsdescribedabove.
123

| Controlledexperimentsontheweb |     |     |     |     | 171 |
| ----------------------------- | --- | --- | --- | --- | --- |
Family Intrusive? Implementation Implementation Hardware Flexibility Impacton
|     |     | costoffirst | costof     | cost rendertime |     |
| --- | --- | ----------- | ---------- | --------------- | --- |
|     |     | experiment  | subsequent |                 |     |
experiments
| Traffic       | No  | Moderate | Moderate | High High         | Low  |
| ------------- | --- | -------- | -------- | ----------------- | ---- |
| splitting     |     | tohigh   | tohigh   |                   |      |
| Pagerewriting | No  | Moderate | Moderate | Moderate Moderate | High |
tohigh
| Client-side | Yes          | Moderate | Moderate | Low Low      | High    |
| ----------- | ------------ | -------- | -------- | ------------ | ------- |
| assignment  | (moderately) |          |          |              |         |
| Server-side | Yes(highly)  | High     | Moderate | Low Veryhigh | Verylow |
| assignment  |              |          | tolow    |              |         |
5.3 Datapath
Inordertocomparemetricsacrossexperimentvariants,awebsitemustfirstrecordthe
treatmentassignmentsofallenduserswhovisitthesiteduringanexperiment.Then,
thewebsitemustcollectrawdatasuchaspageviews,clicks,revenue,rendertime,or
customer-feedbackselections.Eachrowofthisrawdatamustbeannotatedwiththe
identifierofthevariantofeachexperimentthattheusersawonthepagerequest.The
systemmustthenconvertthisrawdataintometrics—numericalsummariesthatcan
be compared between variants of an experiment to determine the outcome. Metrics
canrangefromsimpleaggregates(totalpageviews)allthewaytocomplexinferred
measures (customer satisfaction or search relevance). To compute metrics, the sys-
temappliesbasictransformationsandthenaggregatestheobservations,groupingby
experiment, variant, and any other dimensions that the experimenter wishes to ana-
lyze(forexample,demographics oruseragent).Additionaltransformationsmaybe
appliedatthispointtoproducemorecomplexmeasures.Fromhere,wecreateatable
of metric values, broken down by dimensions, experiment, and (most importantly)
variant.Wecannowcomparemetricvaluesbetweenvariantsanddeterminestatistical
significanceusingeitheranyofanumberofstatisticaltests.
Although the basic analysis techniques closely resemble those used in online
analytic processing (OLAP), website experimentation raises some specific data
issues.
5.3.1 Event-triggeredfiltering
Data collected from web traffic on a large site typically has tremendous variability,
therebymakingitdifficulttorunanexperimentwithsufficientpowertodetecteffects
onsmallerfeatures.Onecriticalwaytocontrolthisvariabilityistorestricttheanalysis
to only those users who were impacted by the experiment (see Sect. 3.2.3). We can
further restrict the analysis to the portion of user behavior that was affected by the
experiment.Werefertothesedatarestrictionsasevent-triggeredfiltering.
123

172 R.Kohavietal.
Event-triggered filtering is implemented by tracking the time at which each user
first saw content that was affected by the experiment. This data can be collected
directly(byrecordinganeventwhenauserseesexperimentalcontent)orindirectly
(by identifying experimental content from page views or other parts of the existing
rawdatastream).Itisalsopossibletointegrateevent-triggeredfilteringdirectlyinto
theassignmentmethod.
5.3.2 Rawdatacollection
Collectingtherawobservationsissimilartobasicwebsiteinstrumentation.However,
theneedsofexperimentationmakesomeoptionsmoreattractivethanothers.
5.3.2.1Usingexisting(external)datacollection Manywebsitesalreadyhavesome
datacollectioninplace,eitherthroughanin-housesystemoranexternalmetricspro-
viderlikeOmnitureorWebmetrics.Forthesewebsites,asimpleapproachistopush
thetreatmentassignmentforeachuserintothissystemsothatitbecomesavailablefor
analysis.Whilethisapproachissimpletosetup,mostexistingdatacollectionsystems
arenotdesignedforthestatisticalanalysesthatarerequiredtocorrectlyanalyzethe
resultsofacontrolledexperiment.Therefore,analysisrequiresmanualextractionof
thedatafromtheexternalsystem,whichcanbeexpensiveandalsoprecludesreal-time
analysis. Moreover, the existing code needs to be modified each time a new experi-
ment is run to add the treatment assignment to allof the recorded observations. We
recommendthisapproachonlyinsituationswherenootherapproachcanbeused.
5.3.2.2 Local data collection Using this method, the website records data locally,
eitherthroughalocaldatabaseorlogfiles.Thedataiscollectedlocallyoneachserverin
thefleetandmustbesortedandaggregatedbeforeanalysiscanbegin.Thismethodcan
bemadetoscaleuptoverylargewebsites.However,asthefleetscalesup,collecting
theselogsinnearreal-timewhileminimizingdatalossbecomesextremelydifficult.
Moreover, this method makes it difficult to collect data from sources other than the
webserver (like backend services or even the user’s browser via JavaScript); every
additionalsourceofdataincreasesthecomplexityoftheloggatheringinfrastructure.
5.3.2.3 Service-based collection Under this model, the website implements a ser-
vicespecificallydesignedtorecordandstoreobservationdata.Servicecallsmaybe
placedinanumberoflocations,includingwebservers,applicationservers,backend
algorithmservices,andeventheenduser’sbrowser(calledviaJavaScript).Implemen-
tationsofthismodeltypicallycachesomedatalocallytoavoidmakinganexcessive
numberofphysicalservicecalls.Thisapproachhastheadvantageofcentralizingall
observationdata,makingitavailableforeasyanalysis.Inparticular,itmakesiteasy
tocombineobservationsfrombackendserviceswithclient-sideJavaScriptdatacol-
lectionthatisnecessarytoaccuratecaptureuserbehavioronpagesmakingextensive
use of DHTML and Ajax. This method also makes it easier to experiment on large
websitesbuiltonheterogeneousarchitectures.
123

Controlledexperimentsontheweb 173
Unlike with assignment methods, there is a clear winner among data collection
techniques:service-basedcollectionisthemostflexibleandthereforepreferredwhen
possible.
6 Lessonslearned
Thedifferencebetweentheoryandpracticeislargerinpracticethanthediffer-
encebetweentheoryandpracticeintheory
–JanL.A.vandeSnepscheut
Many theoretical techniques seem well suited for practical use and yet require
significant ingenuity to apply them to messy real world environments. Controlled
experimentsarenoexception.Havingrunalargenumberofonlineexperiments,we
nowshareseveralpracticallessonsinthreeareas:(i)analysis;(ii)trustandexecution;
and(iii)cultureandbusiness.
6.1 Analysis
Theroadtohellispavedwithgoodintentionsandlitteredwithsloppyanalysis
–Anonymous
6.1.1 Minethedata
A controlled experiment provides more than just a single bit of information about
whetherthedifferenceinOECsisstatisticallysignificant.Richdataistypicallycol-
lectedthatcanbeanalyzedusingmachinelearninganddataminingtechniques.For
example,anexperimentshowednosignificantdifferenceoverall,butapopulationof
userswithaspecificbrowserversionwassignificantlyworsefortheTreatment.The
specificTreatmentfeature,whichinvolvedJavaScript,wasbuggyforthatbrowserver-
sionandusersabandoned.Excludingthepopulationfromtheanalysisshowedpositive
results,andoncethebugwasfixed,thefeaturewasindeedretestedandwaspositive.
6.1.2 Speedmatters
A Treatment might provide a worse user experience because of its performance.
Linden (2006b, p. 15), wrote that experiments at Amazon showed a 1% sales
decreaseforanadditional100msec,andthataspecificexperimentatGoogle,which
increasedthetimetodisplaysearchresultsby500msecsreducedrevenuesby20%
(basedonatalkbyMarissaMayeratWeb2.0).RecentexperimentsatMicrosoftLive
Search (Kohavi 2007, p. 12) showed that when the search results page was slowed
downbyonesecond,queriesperuserdeclinedby1%andadclicksperuserdeclinedby
1.5%;whenthesearchresultspagewassloweddownbytwoseconds,thesenumbers
morethandoubledto2.5%and4.4%.
IftimeisnotdirectlypartofyourOEC,makesurethatanewfeaturethatislosing
isnotlosingbecauseitisslower.
123

174 R.Kohavietal.
6.1.3 Testonefactoratatime(ornot)
Severalauthors(Peterson2004,p.76;Eisenberg2005)recommendtestingonefactor
atatime.Webelievetheadvice,interpretednarrowly,istoorestrictiveandcanlead
organizations to focus on small incremental improvements. Conversely, some com-
paniesaretoutingtheirfractionalfactorialdesignsandTaguchimethods,thusintro-
ducingcomplexitywhereitmaynotbeneeded.Whileitisclearthatfactorialdesigns
allow for joint optimization of factors, and are therefore superior in theory (Mason
etal.1989;Boxetal.2005)ourexperiencefromrunningexperimentsinonlineweb
sites is that interactions are less frequent than people assume (van Belle 2002), and
awarenessoftheissueisenoughthatparallelinteractingexperimentsareavoided.Our
recommendationsaretherefore:
• Conduct single-factor experiments for gaining insights and when you make
incrementalchangesthatcouldbedecoupled.
• Trysomeboldbetsandverydifferentdesigns.Forexample,lettwodesignerscome
upwithtwoverydifferentdesignsforanewfeatureandtrythemoneagainstthe
other.Youmightthenstarttoperturbthewinningversiontoimproveitfurther.For
backendalgorithmsitiseveneasiertotryacompletelydifferentalgorithm(e.g.,
anewrecommendationalgorithm).Dataminingcanhelpisolateareaswherethe
newalgorithmissignificantlybetter,leadingtointerestinginsights.
• Use full or fractional factorial designs suitable for estimating interactions when
severalfactorsaresuspectedtointeractstrongly.Limitthenumberofvaluesper
factorandassignthesamepercentagetothetreatmentsastothecontrol.Thisgives
yourexperimentmaximumpowertodetecteffects.
6.2 Trustandexecution
InGodwetrust,allotherspaycash
–JeanShepherd
6.2.1 RuncontinuousA/Atests
RunA/Atests(seeSect.3.1)andvalidatethefollowing.
1. Areuserssplitaccordingtotheplannedpercentages?
2. Isthedatacollectedmatchingthesystemofrecord?
3. Aretheresultsshowingnon-significantresults95%ofthetime?
ContinuouslyrunA/Atestsinparallelwithotherexperiments.
6.2.2 Automateramp-upandabort
As discussed in Sect. 3.3, we recommend that experimenters gradually increase the
percentageofusersassignedtotheTreatment(s).Anexperimentationsystemthatanal-
ysestheexperimentdatainnear-real-timecanautomaticallyshut-downaTreatment
if it is significantly underperforming relative to the Control. An auto-abort simply
123

Controlledexperimentsontheweb 175
reduces the percentage of users assigned to the underperforming Treatment to zero.
Sincethesystemwillautomaticallyreducetheriskofexposingmanyuserstoegre-
giouserrors,theorganizationcanmakeboldbetsandinnovatefaster.Ramp-upisquite
easytodoinonlineenvironments,yethardtodoinofflinestudies.Wehaveseenno
mentionofthesepracticalideasintheliterature,yettheyareextremelyuseful.
6.2.3 Determinetheminimumsamplesize
Decideonthestatisticalpower,theeffectyouwouldliketodetect,andestimatethe
variabilityoftheOECthroughanA/Atest.Basedonthisdatayoucancomputethe
minimumsamplesizeneededfortheexperimentandhencetherunningtimeforyour
website.Acommonmistakeistorunexperimentsthatareunderpowered.Consider
the techniques mentioned in Sect. 3.2 point 3 to reduce the variability of the OEC.
Alsorecognizethatsomemetricshavepoorpowercharacteristicsinthattheirpower
actuallydegradesastheexperimentrunslonger.Forthesemetricsitisimportantthat
yougetanadequatenumberofusersintothetestperdayandthattheTreatmentand
Controlgroupsareofequalsize.
6.2.4 Assign50%ofuserstotreatment
Onecommonpracticeamongnoviceexperimentersistorunnewvariantsforonlya
smallpercentageofusers.Thelogicbehindthatdecisionisthatincaseofanerroronly
fewuserswillseeabadTreatment,whichiswhywerecommendTreatmentramp-up.
Inordertomaximizethepowerofanexperimentandminimizetherunningtime,we
recommend that 50% of users see each of the variants in an A/B test.Assuming all
factorsarefixed,agoodapproximationforthemultiplicativeincreaseinrunningtime
for an A/B test relative to 50%/50% is 1/(4p(1− p) where the Treatment receives
portion p ofthetraffic.Forexample,ifanexperimentisrunat99%/1%,thenitwill
havetorunabout25timeslongerthanifitranat50%/50%.
6.2.5 Bewareofdayofweekeffects
Evenifyouhavealotofusersvisitingthesite,implyingthatyoucouldrunanexperi-
mentforonlyhoursoraday,westronglyrecommendrunningexperimentsforatleast
a week or two, then continuing by multiples of a week so that day-of-week effects
canbeanalyzed.Formanysitestheusersvisitingontheweekendrepresentdifferent
segments,andanalyzingthemseparatelymayleadtointerestinginsights.Thislesson
canbegeneralizedtoothertime-relatedevents,suchasholidaysandseasons,andto
differentgeographies:whatworksintheUSmaynotworkwellinFrance,Germany,
orJapan.
Putting6.2.3,6.2.4,and6.2.5together,supposethatthepowercalculationsimply
thatyouneedtorunanA/Btestforaminimumof5days,iftheexperimentwererun
at50%/50%.Wewouldthenrecommendrunningitforaweektoavoidday-of-week
effectsandtoincreasethepowerovertheminimum.However,iftheexperimentwere
runat95%/5%,therunningtimewouldhavetobeincreasedbyafactorof5–25days,
inwhichcasewewouldrecommendrunningitforfourweeks.Suchanexperiment
123

176 R.Kohavietal.
shouldnotberunat99%/1%becauseitwouldrequireover125days,aperiodwecon-
sider too long for reliable result; factors, such as cookie churn, that have secondary
impactinexperimentsrunningforafewweeksmaystartcontaminatingthedata.
6.3 Cultureandbusiness
Itisdifficulttogetamantounderstandsomethingwhenhissalarydependsupon
hisnotunderstandingit.
–UptonSinclair
6.3.1 AgreeontheOECupfront
One of the powers of controlled experiments is that it can objectively measure the
valueofnewfeaturesforthebusiness.However,itbestservesthispurposewhenthe
interested parties have agreed on how an experiment is to be evaluated before the
experimentisrun.
While this advice may sound obvious, it is infrequently applied because the
evaluationofmanyonlinefeaturesissubjecttoseveral,oftencompetingobjectives.
OECscanbecombinedmeasures,whichtransformmultipleobjectives,intheformof
experimentalobservations,intoasinglemetric.InformulatinganOEC,anorganiza-
tionisforcedtoweighthevalueofvariousinputsanddecidetheirrelativeimportance.
Agoodtechniqueistoassessthelifetimevalueofusersandtheiractions.Forexam-
ple,asearchfromanewusermaybeworthmorethananadditionalsearchfroman
existinguser.Althoughasinglemetricisnotrequiredforrunningexperiments,this
hardup-frontworkcanaligntheorganizationandclarifygoals.
6.3.2 Bewareoflaunchingfeaturesthat“donothurt”users
When an experiment yields no statistically significant difference between variants,
thismaymeanthattheretrulyisnodifferencebetweenthevariantsorthattheexper-
imentdidnothavesufficientpowertodetectthechange.Inthefaceofa“nosignifi-
cantdifference”result,sometimesthedecisionismadetolaunchthechangeanyway
“becauseitdoesnothurtanything.”Itispossiblethattheexperimentisnegativebut
underpowered.
6.3.3 Weighthefeaturemaintenancecosts
An experiment may show a statistically significant difference between variants, but
choosing to launch the new variant may still be unjustified because of maintenance
costs. A small increase in the OEC may not outweigh the cost of maintaining the
feature.
123

Controlledexperimentsontheweb 177
6.3.4 Changetoadata-drivenculture
Runningafewonlineexperimentscanprovidegreatinsightsintohowcustomersare
usingafeature.Runningfrequentexperimentsandusingexperimentalresultsasmajor
inputtocompanydecisionsandproductplanningcanhaveadramaticimpactoncom-
pany culture. As Mike Moran said in his wonderful book “Do it Wrong Quickly”
(Moran2007)“Sometimesyouhavetokissalotoffrogstofindoneprince.Sohow
can you find your prince faster? By finding more frogs and kissing them faster and
faster.”Softwareorganizationsshippingclassicalsoftwaredevelopedaculturewhere
features are completely designed prior to implementation. In a web world, we can
integrate customer feedback directly through prototypes and experimentation. If an
organizationhasdonethehardworktoagreeonanOECandvettedanexperimentation
system,experimentationcanproviderealdataandmovetheculturetowardsattaining
sharedgoalsratherthanbattleoveropinions.
7 Summary
Almostanyquestioncanbeansweredcheaply,quicklyandfinally,byatestcam-
paign. And that’s the way to answer them – not by arguments around a table.
Gotothecourtoflastresort–buyersofyourproducts.
–ClaudeHopkins,ScientificAdvertising,1923
…theabilitytoexperimenteasilyisacriticalfactorforWeb-basedapplications.
The online world is never static. There is a constant flow of new users, new
productsandnewtechnologies.Beingabletofigureoutquicklywhatworksand
whatdoesn’tcanmeanthedifferencebetweensurvivalandextinction.
–HalVarian,2007
Classical knowledge discovery and data mining provide insight, but the patterns
discoveredarecorrelationalandthereforeposechallengesinseparatingusefulaction-
able patterns from those caused by “leaks” (Kohavi et al. 2004). Controlled experi-
ments neutralize confounding variables by distributing them equally over all values
throughrandomassignment(Keppeletal.1992),thusestablishingacausalrelation-
shipbetweenthechangesmadeinthedifferentvariantsandthemeasure(s)ofinterest,
including the Overall Evaluation Criterion (OEC). Using data mining techniques in
thissettingcanthusprovideextremelyvaluableinsights,suchastheidentificationof
segmentsthatbenefitfromafeatureintroducedinacontrolledexperiment,leadingto
avirtuouscycleofimprovementsinfeaturesandbetterpersonalization.
The basic ideas in running controlled experiments are easy to understand, but a
comprehensiveoverviewforthewebwasnotpreviouslyavailable.Inaddition,there
areimportantnewlessonsandinsightsthatwesharedthroughoutthepaper,including
generalizedarchitectures,ramp-upandaborts,thepracticalproblemswithrandomi-
zationandhashingtechniques,andorganizationalissues,especiallyastheyrelateto
OEC.
123

178 R.Kohavietal.
Software features in products today are commonly determined by the same way
medicine was prescribed prior to World War II: by people who were regarded as
experts,notbyusingscientificmethods,suchascontrolledexperiments.Wecando
bettertoday,especiallywithouraccesstocustomerbehavioronline.InTheProgressof
Experiment:ScienceandTherapeuticReformintheUnitedStates,1900–1990(Marks
2000,p.3),theauthorwroteabouttheincreasingimportanceofdesignedexperiments
in the advance of medical knowledge: “Reformers in the second half of the century
abandonedtheirpredecessors’trustinthejudgmentofexperiencedclinicians.Inits
place, they offered an impersonal standard of scientific integrity: the double-blind,
randomized,controlledclinicaltrial.”
Manyorganizationshavestrongmanagerswhohavestrongopinions,butlackdata,
sowestartedtousethetermHiPPO,whichstandsforHighestPaidPerson’sOpinion,as
awaytoremindeveryonethatsuccessreallydependsontheusers’perceptions.Some
authors have called experimentation the “New Imperative for Innovation” (Thomke
2001)andpointoutthat“newtechnologiesaremakingiteasierthanevertoconduct
complexexperimentsquicklyandcheaply.”Weagreeandbelievethatcompaniescan
accelerate innovation through experimentation because it is the customers’ experi-
ence that ultimately matters, and we should listen to them all the time by running
experiments.
Acknowledgements WewouldliketothankmembersoftheExperimentationPlatformteamatMicrosoft.
ThefirstauthorwishestothankAvinashKaushikforagreatconversationonA/Btesting,whereheusedthe
term“HiPO”forHighestPaidOpinion;thisevolvedintoHiPPO(pictureincluded)inourpresentations.We
thankFritzBehr,KeithButler,RodDeyo,DanyelFisher,JamesHamilton,AndrewHesky,RonitHaNegby,
GregLinden,FosterProvost,SaharonRosset,GeoffWebb,andZijianZhengfortheirfeedback.
AppendixA
Whenrandomizationbyuser-IDisnotappropriate
Theapproachwedescribeinthispaperistorandomlyassignuserstoonegroupor
anotherandcomparethesegroupsofuserstodeterminewhichexperience(i.e.Treat-
ment)isbest.Therearesomeexperimentationobjectiveswherethisapproachwillnot
work.Wewilldescribethreeoftheseandalternativeapproachestorandomizationin
anonlineenvironment.
1. ControlmayaffecttheeffectivenessoftheTreatmentandviceversa Biddingon
Ebay.2 Suppose the Treatment is to give an incentive (perhaps a $5 discount or
certainpercentoffthefinalbidprice)forausertobethefirstbidderandnosuch
incentiveexistsfortheControl.Assumethesuccessmetric(OEC)istheratioof
the final sales price to the minimum bid for each item. If some users have this
incentive and others do not, the presence of the Treatment will affect all items
so we cannot get a true measure of the effectiveness of making this change. In
thiscaseyoucanrandomlyassignonegroupofitemsintheauctiontobeinthe
ControlandtheresttobeintheTreatmentandcomparetheOECforthesetwo
groups.i.e.randomlyassigntheitemsintheauction,nottheusers.
2 WewishtothankNeelSundaresanandhisteamateBayforthisexample.
123

Controlledexperimentsontheweb 179
2. Notdesirabletorandomizebasedonuser Priceelasticitystudy.Theusualran-
domizationbasedonuserisnotdesirablebecausebadcustomerrelationscould
resultifit’sexposedthatsomecustomersaregettingadifferentpricethanother
customers (everything else being equal) as Amazon.com discovered when it
ran such a study (Weiss 2000). Here also, the items involved in the study can
be randomly assigned to the Treatment or Control instead of randomizing the
users.
3. Not possible to randomize on user Search Engine Optimization (SEO). Most
robotsdonotsetcookiessotheywouldnotbeinanyexperiment.Ifyouwantedto
conductatestonrobotbehavior(e.g.clickthroughsbyrobotsorother)youcannot
randomizebasedonauserID.Insteadyoucantakegroupsofpagesonyoursite
that are similar and randomly assign pages within each group to Treatment or
Controlandcomparerobotbehaviorforthetwogroupsofpages.
References
AltB,UsborneN(2005)MarketExpJ.[Online]December29,2005.http://www.marketingexperiments.
com/improving-website-conversion/multivariable-testing.html
BoosDD,Hughes-OliverJM(2000)HowlargedoesnhavetobeforZandtintervals?AmStatist54(2):121–
128
BoxGEP,HunterJS,HunterWG(2005)Statisticsforexperimenters:design,innovation,anddiscovery,
2ndedn.Wiley,ISBN:0471718130
BurnsM(2006)Webanalyticsspendingstrends2007.ForresterResearchInc.,Cambridge
CharlesRS,MelvinMM(2004)Quasiexperimentation.[bookauth.]In:WholeyJS,HatryHP,Newcomer
KE(eds)Handbookofpracticalprogramevaluation,2ndedn.Jossey-Bass
ChathamB,TemkinBD,AmatoM(2004)AprimeronA/Btesting.ForresterResearch
DaviesOL,HayWA(1950)Constructionandusesoffractionalfactorialdesignsinindustrialresearch.
Biometrics233(6):121–128
EisenbergB(2003a)HowtoDecreasesalesby90%.ClickZ.[Online]Feb21,2003.http://www.clickz.
com/showPage.html?page=1588161
EisenbergB(2003b)Howtoincreaseconversionrate1,000%.ClickZ.[Online]Feb28,2003.http://www.
clickz.com/showPage.html?page=1756031
EisenbergB(2004)A/Btestingforthemathematicallydisinclined.ClickZ.[Online]May7,2004.http://
www.clickz.com/showPage.html?page=3349901
EisenbergB(2005)HowtoimproveA/Btesting.ClickZNetw.[Online]April29,2005.http://www.clickz.
com/showPage.html?page=3500811
EisenbergB,EisenbergJ(2005)Calltoaction,secretformulastoimproveonlineresults.WizardAcademy
Press,Austin,2005.Makingthedialmovebytesting,introducingA/Btesting
EisenbergB,GarciaA(2006)Whichsellsbest:aquickstartguidetotestingforretailers.Futurenow’s
publications.[Online]2006.http://futurenowinc.com/shop/
ForresterResearch(2005)Thestateofretailingonline.Shop.org
GoogleWebsiteOptimizer(2008)[Online]2008.http://services.google.com/websiteoptimizer
Hawthorneeffect(2007)Wikipedia.[Online]2007.http://en.wikipedia.org/wiki/Hawthorne_experiments
HopkinsC(1923)Scientificadvertising.CrownPublishersInc.,NewYorkCity
KaplanRS,NortonDP(1996)Thebalancedscorecard:translatingstrategyintoaction.HarvardBusiness
SchoolPress,ISBN:0875846513
KaushikA(2006)Experimentationandtesting:aprimer.Occam’sRazorbyAvinashKaushik.[Online]
May22,2006.http://www.kaushik.net/avinash/2006/05/experimentation-and-testing-a-primer.html
KeppelG,SaufleyWH,TokunagaH(1992)Introductiontodesignandanalysis,2ndedn.W.H.Freeman
andCompany
KohaviR(2007)Emetrics2007practicalguidetocontrolledexperimentsontheweb.[Online]October16,
2007.http://exp-platform.com/Documents/2007-10EmetricsExperimenation.pdf
KohaviR,ParekhR(2003)Tensupplementaryanalysestoimprovee-commercewebsites.WebKDD
123

180 R.Kohavietal.
KohaviR,RoundM(2004)In:SterneJ(ed)FrontlineinternetanalyticsatAmazon.com.SantaBarbara,
CA.http://ai.stanford.edu/~ronnyk/emetricsAmazon.pdf
Kohavi R et al (2004) Lessons and challenges from mining retail e-commerce data. Machine Learn
57(1–2):83–113.http://ai.stanford.edu/~ronnyk/lessonsInDM.pdf
KoselkaR(1996)Thenewmantra:MVT.Forbes.March11,1996,pp114–118
LindenG(2006a)EarlyAmazon:shoppingcartrecommendations.GeekingwithGreg.[Online]April25,
2006.http://glinden.blogspot.com/2006/04/early-amazon-shopping-cart.html
Linden G (2006b) Make data useful. [Online] Dec 2006. http://home.blarg.net/~glinden/
StanfordDataMining.2006-11-29.ppt
ManningH,DorseyM,CarneyCL(2006)Don’trationalizebadsitedesign.ForresterResearch,Cambridge
MarksHM(2000)Theprogressofexperiment:scienceandtherapeuticreformintheunitedstates,1900–
1990.CambridgeUniversityPress,ISBN:978-0521785617
MaronO,MooreAW(1994)Hoeffdingraces:acceleratingmodelselectionsearchforclassificationand
functionapproximation.http://citeseer.ist.psu.edu/maron94hoeffding.html
MasonRL,GunstRF,HessJL(1989)Statisticaldesignandanalysisofexperimentswithapplicationsto
engineeringandscience.Wiley,ISBN:047185364X
McGlaughlinFetal(2006)Thepowerofsmallchangestested.MarketExpJ.[Online]March21,2006.
http://www.marketingexperiments.com/improving-website-conversion/power-small-change.html
MillerS(2006)TheConversionLab.com:howtoexperimentyourwaytoincreasedwebsalesusingsplit
testingandTaguchioptimization.http://www.conversionlab.com/
MillerS(2007)Howtodesignasplittest.Webmarketingtoday,conversion/testing.[Online]Jan18,2007.
http://www.wilsonweb.com/conversion/
MoranM(2007)Doitwrongquickly:howthewebchangestheoldmarketingrules.IBMPress,ISBN:
0132255960
NielsenJ(2005)PuttingA/Btestinginitsplace.Useit.comAlertbox.[Online]Aug15,2005.http://www.
useit.com/alertbox/20050815.html
Omniture(2008)[Online]2008.www.omniture.com/products/optimization/offermatica
Optimost(2008)[Online]2008.http://www.optimost.com
PetersonET(2004)Webanalyticsdemystified:amarketer’sguidetounderstandinghowyourwebsite
affectsyourbusiness.CeliloGroupMediaandCafePress,ISBN:0974358428
PetersonET(2005)Websitemeasurementhacks.O’ReillyMedia,ISBN:0596009887
PlackettRL,BurmanJP(1946)Thedesignofoptimummultifactorialexperiments.Biometrika33:305–325
Quarto-vonTivadar J (2006) AB testing: too little, too soon. Future Now. [Online] 2006. http://www.
futurenowinc.com/abtesting.pdf
RossiPH,LipseyMW,FreemanHE(2003)Evaluation:asystematicapproach,7thedn.SagePublications,
Inc.,ISBN:0-7619-0894-3
RoyRK(2001)Designofexperimentsusingthetaguchiapproach:16stepstoproductandprocessimprove-
ment.Wiley,ISBN:0-471-36101-1
SiteSpect(2008)[Online]2008.http://www.sitespect.com
Spool JM (2004) The cost of frustration. WebProNews. [Online] September 20, 2004. http://www.
webpronews.com/topnews/2004/09/20/the-cost-of-frustration
SterneJ(2002)Webmetrics:provenmethodsformeasuringwebsitesuccess.Wiley,ISBN:0-471-22072-8
TanP-N,KumarV(2002)Discoveryofwebrobotsessionsbasedontheirnavigationalpatterns.DataMin
KnowlDis
ThomkeS(2001)Enlightenedexperimentation:thenewimperativeforinnovation,Feb2001
ThomkeSH(2003)Experimentationmatters:unlockingthepotentialofnewtechnologiesforinnovation
TylerME,LedfordJ(2006)Googleanalytics.Wiley,ISBN:0470053852
UlwickA(2005)Whatcustomerswant:usingoutcome-driveninnovationtocreatebreakthroughproducts
andservices.McGraw-Hill,ISBN:0071408673
UsborneN(2005)Designchoicescancrippleawebsite.Alistapart.[Online]Nov8,2005.http://alistapart.
com/articles/designcancripple
vanBelleG(2002)Statisticalrulesofthumb.Wiley,ISBN:0471402273
VarianHR(2007)Kaizen,thatcontinuousimprovementstrategy,findsitsidealenvironment.NewYork
Times. February 8, 2007. Online at http://www.nytimes.com/2007/02/08/business/08scene.html?
fta=y
Verster(2008)[Online]2008.http://www.vertster.com
123

Controlledexperimentsontheweb 181
WeissCH(1997)Evaluation:methodsforstudyingprogramsandpolicies,2ndedn.PrenticeHall,ISBN:
0-13-309725-0
Weiss TR (2000) Amazon apologizes for price-testing program that angered customers. www.
Safecount.net. [Online] September 28, 2000. http://www.infoworld.com/articles/hn/xml/00/09/28/
000928hnamazondvd.html
WheelerRE(1974)Portablepower.Technometrics16:193–201.http://www.bobwheeler.com/stat/Papers/
PortablePower.PDF
WheelerRE(1975)Thevalidityofportablepower.Technometrics17(2):177–179
Widemile(2008)[Online]2008.http://www.widemile.com
Wikepedia (2008) Multi-armed bandit. Wikipedia. [Online] 2008. http://en.wikipedia.org/wiki/
Multi-armed_bandit
WillanAR,BriggsAH(2006)Statisticalanalysisofcost-effectivenessdata(statisticsinpractice).Wiley
123
