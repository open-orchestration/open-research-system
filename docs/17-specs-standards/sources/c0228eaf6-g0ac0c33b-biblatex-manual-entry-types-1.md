|     |     |     | The |     |     | Package |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
biblatex
ProgrammableBibliographiesandCitations
| PhilipKime,MoritzWemheuer, |     |     |               |     |     | Version3.21 |     |     |     |     |
| -------------------------- | --- | --- | ------------- | --- | --- | ----------- | --- | --- | --- | --- |
|                            |     |     | PhilippLehman |     |     | July10,2025 |     |     |     |     |
Contents
| ListofTables    |                     |     |         |       | 1    | 4 AuthorGuide |                     |        |         | 156   |
| --------------- | ------------------- | --- | ------- | ----- | ---- | ------------- | ------------------- | ------ | ------- | ----- |
|                 |                     |     |         |       |      | 4.1           | Overview            | . . .  | . . . . | . 156 |
| 1 Introduction  |                     |     |         |       | 2    | 4.2           | BibliographyStyles  |        | .       | . 159 |
| 1.1             | About               | . . | . . . . | . . . | . 2  |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.3           | CitationStyles      |        | . . . . | . 182 |
| 1.2             | License             | .   | . . . . | . . . | . 2  |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.4           | DataInterface       |        | . . . . | . 185 |
| 1.3             | Feedback            |     | . . . . | . . . | . 2  |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.5           | Customization       |        | . . . . | . 195 |
| 1.4             | Acknowledgements    |     |         | .     | . 2  |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.6           | AuxiliaryCommands   |        |         | . 243 |
| 1.5             | Prerequisites       |     | . .     | . . . | . 3  |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.7           | Punctuation         | .      | . . . . | . 272 |
|                 |                     |     |         |       |      | 4.8           | LocalizationStrings |        | .       | . 278 |
| 2 DatabaseGuide |                     |     |         |       | 7    |               |                     |        |         |       |
|                 |                     |     |         |       |      | 4.9           | LocalizationModules |        |         | . 281 |
| 2.1             | EntryTypes          |     | . .     | . . . | . 7  |               |                     |        |         |       |
| 2.2             | EntryFields         |     | . .     | . . . | . 15 | 4.10          | FormattingCommands  |        |         | 297   |
| 2.3             | UsageNotes          |     | . .     | . . . | . 33 | 4.11          | HintsandCaveats     |        | . .     | . 317 |
| 2.4             | HintsandCaveats     |     |         | . .   | . 42 |               |                     |        |         |       |
|                 |                     |     |         |       |      | Appendix      |                     |        |         | 335   |
| 3 UserGuide     |                     |     |         |       | 46   |               |                     |        |         |       |
| 3.1             | PackageOptions      |     |         | . . . | . 46 | A Default     |                     | Driver | Source  |       |
| 3.2             | GlobalCustomization |     |         |       | . 74 | Mappings      |                     |        |         | 335   |
3.3 StandardStyles . . . . 74 A.1 bibtex . . . . . . . . . 335
| 3.4 | ExtendedNameFormat |     |     |     | 80  |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.5 RelatedEntries . . . . . 81 B DefaultInheritanceSetup 336
| 3.6 | SortingOptions       |     |     | . . . | . 82  |                           |             |     |         |       |
| --- | -------------------- | --- | --- | ----- | ----- | ------------------------- | ----------- | --- | ------- | ----- |
|     |                      |     |     |       |       | C DefaultSortingTemplates |             |     |         | 338   |
| 3.7 | DataAnnotations      |     |     | . .   | . 83  |                           |             |     |         |       |
| 3.8 | BibliographyCommands |     |     |       | 89    | C.1                       | Alphabetic1 | .   | . . . . | . 338 |
| 3.9 | CitationCommands     |     |     | .     | . 108 | C.2                       | Alphabetic2 | .   | . . . . | . 338 |
3.10 LocalizationCommands 120 C.3 Chronological . . . . . 338
| 3.11 | Entry              | Querying |         | Com-  |       |              |        |         |         |       |
| ---- | ------------------ | -------- | ------- | ----- | ----- | ------------ | ------ | ------- | ------- | ----- |
|      | mands              | .        | . . . . | . . . | . 121 | D biblatexml |        |         |         | 339   |
| 3.12 | FormattingCommands |          |         |       | 121   | D.1          | Header | . . . . | . . . . | . 339 |
3.13 Languagenotes . . . . 136 D.2 Body . . . . . . . . . . 340
| 3.14             | UsageNotes      |     | . .         | . . . | . 139 |                         |     |     |     |      |
| ---------------- | --------------- | --- | ----------- | ----- | ----- | ----------------------- | --- | --- | --- | ---- |
| 3.15             | HintsandCaveats |     |             | . .   | . 149 | E OptionScope           |     |     |     | 343  |
| 3.16             | Using           | the | fallback    |       |       |                         |     |     |     |      |
|                  | BibTeXbackend   |     |             | . . . | . 155 | F RevisionHistory       |     |     |     | 346  |
| List             | of Tables       |     |             |       |       |                         |     |     |     |      |
| 1 biber/biblatex |                 |     | compatibil- |       |       | 6 WorkUniquenessoptions |     |     | .   | . 69 |
itymatrix . . . . . . . . . . . 8 7 Disambiguationcounters . . 71
2 SupportedLanguages . . . . 29 8 mcite-likecommands . . . . 119
3 DateSpecifications . . . . . . 39 9 mcite-likesyntax. . . . . . . 120
4 ISO8601-2 4.3 Unspecified 10 DateInterface . . . . . . . . 173
DateParsing . . . . . . . . . 40 11 Validtransliterationpairs . . 232
5 EnhancedDateSpecifications 41 12 \mkcomprangesetup . . . . . 265
1

1 Introduction
Thisdocumentisasystematicreferencemanualforthebiblatexpackage. Lookat
thesampledocumentswhichcomewithbiblatextogetafirstimpression.1 Fora
quickstartguide,browse§§1.1,2.1,2.2,2.3,3.1,3.3,3.8,3.9,3.14.
1.1 Aboutbiblatex
ThispackageprovidesadvancedbibliographicfacilitiesforusewithLaTeX.Thepack-
ageisacompletereimplementationofthebibliographicfacilitiesprovidedbyLaTeX.
Thebiblatexpackageworkswiththe“backend”(program)biber,whichisusedto
processBibTeXformatdatafilesandthenperformsallsorting,labelgeneration(anda
greatdealmore). FormattingofthebibliographyisentirelycontrolledbyTeXmacros.
GoodworkingknowledgeinLaTeXshouldbesufficienttodesignnewbibliography
andcitationstyles. Thispackagealsosupportssubdividedbibliographies,multiple
bibliographieswithinonedocument,andseparatelistsofbibliographicinformation
suchasabbreviationsofvariousfields. Bibliographiesmaybesubdividedintoparts
and/orsegmentedbytopics. Justlikethebibliographystyles,allcitationcommands
maybefreelydefined. FeaturessuchasfullUnicodesupportforbibliographydata,
customisablesorting,multiplebibliographieswithdifferentsorting,customisable
labelsanddynamicdatamodificationareavailable. Pleasereferto§1.5.6forinforma-
tiononbiber/biblatexversioncompatibility. Thepackageiscompletelylocalised
andcaninterfacewiththebabelandpolyglossiapackages. Pleaserefertotable2
foralistoflanguagescurrentlysupportedbythispackage.
1.2 License
Copyright©2006–2012PhilippLehman,2012–2017PhilipKime,AudreyBoruvka,
JosephWright,2018–PhilipKimeandMoritzWemheuer. Permissionisgrantedto
copy,distributeand/ormodifythissoftwareunderthetermsoftheLaTeXProject
PublicLicense,version1.3.2
1.3 Feedback
PleaseusethebiblatexprojectpageonGitHubtoreportbugsandsubmitfeature
requests.3 Beforemakingafeaturerequest,pleaseensurethatyouhavethoroughly
studiedthismanual. Ifyoudonotwanttoreportabugorrequestafeaturebutare
simplyinneedofassistance,youmightwanttoconsiderpostingyourquestionon
thecomp.text.texnewsgrouporTeX-LaTeXStackExchange.4
1.4 Acknowledgements
ThepackagewasoriginallywrittenbyPhilippLehmanandmuchofhisexcellent
originalcoderemainsinthecore. PhilipKimetookoverthepackagein2012with
MoritzWemheuermakingregularandvaluablecontributionsfrom2017. Themain
authorswouldliketoacknowledgethevaluablehelpofAudreyBoruvkaandJoseph
Wrightwhohelpedwiththetransitionofownershipin2012andfollowingyears.
Thelanguagemodulesofthispackagearemadepossiblethankstothefollowing
contributors:
1https://ctan.org/tex-archive/macros/latex/contrib/biblatex/doc/examples
2https://www.latex-project.org/lppl.txt
3https://github.com/plk/biblatex
4https://tex.stackexchange.com/questions/tagged/biblatex
2

Ander Zarketa-Astigarraga (Basque); Augusto Ritter Stoffel, Mateus Araújo, Gus-
tavoBarros(Brazilian);KaloyanGanev(Bulgarian);SebastiàVila-Marta(Catalan);
IvoPletikosić(Croatian);MichalHoftich(Czech);ChristianMondrup,JonasNyrup
(Danish);JohannesWilm(Danish/Norwegian);AlexandervanLoon,PieterBelmans,
Hendrik Maryns (Dutch); Kristian Kankainen, Benson Muite, Artjom Jemeljanov
(Estonian); Hannu Väisänen, Janne Kujanpää (Finnish); Denis Bitouzé (French);
ApostolosSyropoulos,Prokopis(Greek);MártonMarczell,BenceFerdinandy(Hun-
garian); Baldur Kristinsson (Icelandic); Enrico Gregorio, Andrea Marchitelli (Ital-
ian);RihardsSkuja(Latvian);ValdemarasKlumbys(Lithuanian); (Marathi);
�नरंजन
HåkonMalmedal,HansFredrikNordhaug(Norwegian);AnastasiaKandulina,Yuriy
Chernyshov, Sebastian Wasiuta (Polish); José Carlos Santos (Portuguese); Patrick
Danilevici(Romanian);OlegDomanov(Russian);AndrejRadović(Serbian);Martin
Vrábel,DávidLupták(Slovak);TeaTušar,BogdanFilipič(Slovene);IgnacioFernán-
dez Galván (Spanish); Per Starbäck, Carl-Gustav Werner, Filip Åsblom (Swedish);
AbdulkerimGok(Turkish);SergiyM.Ponomarenko(Ukrainian).
1.5 Prerequisites
Thissectiongivesanoverviewofallresourcesrequiredbythispackageanddiscusses
compatibilityissues.
1.5.1 Requirements
The resources listed in this section are strictly required for biblatex to function.
Thepackagewillnotworkiftheyarenotavailable.
e-TeX Thebiblatexpackagerequirese-TeX. TeXdistributionshavebeenprovidinge-TeX
binariesforquitesometime,thepopulardistributionsusethembydefaultthesedays.
Thebiblatexpackagechecksifitisrunningundere-TeX. Simplytrycompilingyour
documentsasyouusuallydo,thechancesarethatitjustworks. Ifyougetanerror
message, trycompilingthedocumentwithelatexinsteadoflatexorpdfelatex
insteadofpdflatex,respectively.
biber biber is the backend of biblatex used to transfer data from source files to the
LaTeXcode. bibercomeswithTeXLiveandisalsoavailablefromSourceForge.5
biber uses the btparse C library for BibTeX format file parsing which aimed to
be compatible with BibTeX’s parsing rules but also aimed at correcting some of
thecommonproblems. Fordetails,seethemanualpageforthePerlText::BibTeX
module.6
etoolbox ThisLaTeXpackage,whichisloadedautomatically,providesgenericprogramming
facilitiesrequiredbybiblatex. Itisavailablefromctan.7
kvoptions ThisLaTeXpackage,whichisalsoloadedautomatically,isusedforinternaloption
handling. Itisavailablefromctan.8
logreq This LaTeX package, which is also loaded automatically, provides a frontend for
writing machine-readable messages to an auxiliary log file. It is available from
ctan.9
5https://biblatex-biber.sourceforge.net/
6https://metacpan.org/release/Text-BibTeX
7https://ctan.org/pkg/etoolbox
8https://ctan.org/pkg/kvoptions
9https://ctan.org/pkg/logreq/
3

pdftexcmds ThisLaTeXpackage,whichisloadedautomatically,implementspdfTeXprimitives
forLuaTeX,italsooffersaunifiedinterfacefortheseprimitivesacrossengines. Itis
availablefromctan.10
biblatexusespdftexcmdstoaccesstheMD5hashprimitives,soversion0.27(2018/01/30)
oraboveisstronglyrecommended.
Apartfromtheaboveresources,biblatexalsorequiresthestandardLaTeXpack-
ageskeyvalandifthenaswellastheurlpackage. Thesepackagesareincludedin
allcommonTeXdistributionsandwillbeloadedautomatically.
1.5.2 RecommendedPackages
Thepackageslistedinthissectionarenotstrictlyrequiredforbiblatextofunction,
buttheyproviderecommendedadditionalfunctionsorenhanceexistingfeatures.
babel/polyglossia Thebabelandpolyglossiapackagesprovidethecorearchitectureformultilingual
typesetting. IfyouarewritinginalanguageotherthanAmericanEnglish,usingone
ofthesepackagesisstronglyrecommended. Youshouldloadbabelorpolyglossia
beforebiblatexandthenbiblatexwilldetectbabelorpolyglossiaautomatically.
(Whilebabelmaybeloadedafterbiblatexifsodesired,polyglossiamustalways
beloadedbeforebiblatex.)
biblatexhasonlylimitedsupportforpolyglossiaversionspriortov1.45(2019/10/27).
Additionalusefulfeaturesforbiblatexwereaddedinversion1.49. Ifpolyglossia
isused,itshouldbeupdatedtoversion1.49(2020/04/08)orabove.
Theminimumsupportedbabelversionisv3.9r(2016/04/23).
csquotes Ifthispackageisavailable,biblatexwilluseitslanguagesensitivequotationfacilities
toenclosecertaintitlesinquotationmarks. Ifnot,biblatexusesquotessuitablefor
AmericanEnglishasafallback. WhenwritinginalanguageotherthanAmerican
English,loadingcsquotesisstronglyrecommended.11
1.5.3 AdditionalUsefulPackages
The packages listed in this section are not required for biblatex to function, but
provideadditionalspecialistfunctionsorenhanceexistingfeatures. Thesepackages
generally only need to be loaded if their functionality is explicitly desired. The
packageloadingorderusuallydoesnotmatter.
xpatch Thexpatchpackageextendsthepatchingcommandsofetoolboxtobiblatexbiblio-
graphymacros,driversandformattingdirectives.12 Itscommandsareusefultoapply
surgical-precisionchangestobibliographymacros,driversorformattingdirectives
withouthavingtorestatethewholedefinitiontochangeit. Thebiblatexcoredoes
notneedorusethesepatchingcommandsandstylesthatmakeuseofthemshould
loadthepackagethemselves.
1.5.4 CompatibleClassesandPackages
The biblatex package provides dedicated compatibility code for the classes and
packageslistedinthissection.
10https://ctan.org/pkg/pdftexcmds/
11https://ctan.org/pkg/csquotes/
12https://ctan.org/pkg/xpatch/
4

hyperref Thehyperrefpackagetransformscitationsintohyperlinks. Seethehyperrefand
backrefpackageoptionsin§3.1.2.1forfurtherdetails. Whenusingthehyperref
package,itispreferabletoloaditafterbiblatex.
showkeys Theshowkeyspackageprintstheinternalkeysof,amongotherthings,citationsin
thetextanditemsinthebibliography. Thepackageloadingorderdoesnotmatter.
memoir Whenusingthememoirclass,thedefaultbibliographyheadingsareadaptedsuch
that they blend well with the default layout of this class. See § 3.15.2 for further
usagehints.
KOMA-Script Whenusinganyofthescrartcl,scrbook,orscrreprtclasses,thedefaultbiblio-
graphyheadingsareadaptedsuchthattheyblendwellwiththedefaultlayoutof
theseclasses. See§3.15.1forfurtherusagehints.
Ifavailablebiblatexmakesuseofsomeofthemorerecentofkoma-Script’sdo-hooks.
The relevant hooks are present from version 3.27 (2019/10/12) onwards, which is
thereforetheminimumversionrecommendation.
1.5.5 IncompatiblePackages
Thepackageslistedinthissectionarenotcompatiblewithbiblatex. Sinceitreimple-
mentsthebibliographicfacilitiesofLaTeXfromthegroundup,biblatexnaturally
conflicts with all packages modifying the same facilities. This is not specific to
biblatex. Someofthepackageslistedbelowarealsoincompatiblewitheachother
forthesamereason.
babelbib The babelbib package provides support for multilingual bibliographies. This is a
standardfeatureofbiblatex. Usethelangidfieldandthepackageoptionautolang
for similar functionality. Note that biblatex automatically adjusts to the main
document language if babel or polyglossia is loaded. You only need the above
mentionedfeaturesifyouwanttoswitchlanguagesonaper-entrybasiswithinthe
bibliography. See§§2.2.3and3.1.2.1fordetails. Alsosee§3.10.
backref Thebackrefpackagecreatesbackreferencesinthebibliography. Seethepackage
optionshyperrefandbackrefin§3.1.2.1forcomparablefunctionality.
bibtopic Thebibtopicpackageprovidessupportforbibliographiessubdividedbytopic,type,
orothercriteria. Forbibliographiessubdividedbytopic, seethecategoryfeature
in § 3.8.6 and the corresponding filters in § 3.8.2. Alternatively, you may use the
keywordsfieldinconjunctionwiththekeywordandnotkeywordfiltersforcompara-
blefunctionality,see§§2.2.3and3.8.2fordetails. Forbibliographiessubdividedby
type,usethetypeandnottypefilters. Alsosee§3.14.4forexamples.
bibunits Thebibunitspackageprovidessupportformultiplepartial(e.g.,perchapter)bibli-
ographies. Seechapterbib.
chapterbib Thechapterbibpackageprovidessupportformultiplepartialbibliographies. Use
the refsection environment and the section filter for comparable functionality.
Alternatively, you might also want to use the refsegment environment and the
segmentfilter. See§§3.8.4,3.8.5,3.8.2fordetails. Alsosee§3.14.3forexamples.
cite Thecitepackageautomaticallysortsnumericcitationsandcancompressalistof
consecutivenumberstoarange. Italsomakesthepunctuationusedincitationscon-
figurable. Forsortedandcompressednumericcitations,seethesortcitespackage
5

optionin§3.1.2.1andthenumeric-compcitationstylein§3.3.1. Forconfigurable
punctuation,see§3.12.
citeref Anotherpackageforcreatingbackreferencesinthebibliography. Seebackref.
inlinebib Theinlinebibpackageisdesignedfortraditionalcitationsgiveninfootnotes. For
comparablefunctionality,seetheverbosecitationstylesin§3.3.1.
jurabib Originallydesignedforcitationsinlawstudiesand(mostlyGerman)judicialdocu-
ments,thejurabibpackagealsoprovidesfeaturesaimedatusersinthehumanities.
Intermsofthefeaturesprovided,therearesomesimilaritiesbetweenjurabiband
biblatex but the approaches taken by both packages are quite different. Since
both jurabib and biblatex are full-featured packages, the list of similarities and
differencesistoolongtobediscussedhere.
mcite Themcitepackageprovidessupportforgroupedcitations,i.e.,multipleitemscan
becitedasasinglereferenceandlistedasasingleblockinthebibliography. The
citationgroupsaredefinedastheitemsarecited. Thisonlyworkswithunsorted
bibliographies. Thebiblatexpackagealsosupportsgroupedcitations,whichare
called‘entrysets’or‘referencesets’inthismanual. See§§3.14.5,3.8.11,3.9.10for
details.
mciteplus Asignificantlyenhancedreimplementationofthemcitepackagewhichsupports
groupinginsortedbibliographies. Seemcite.
multibib Themultibibpackageprovidessupportforbibliographiessubdividedbytopicor
othercriteria. Seebibtopic.
natbib Thenatbibpackagesupportsnumericandauthor-yearcitationschemes,incorpo-
rating sorting and compression code found in the cite package. It also provides
additionalcitationcommandsandseveralconfigurationoptions. Seethenumeric
andauthor-yearcitationstylesandtheirvariantsin§3.3.1,thesortcitespackage
option in § 3.1.2.1, the citation commands in § 3.9, and the facilities discussed in
§§3.8.7,3.8.8,3.12forcomparablefunctionality. Alsosee§3.9.9.
splitbib Thesplitbibpackageprovidessupportforbibliographiessubdividedbytopic. See
bibtopic.
titlesec Thetitlesecpackageredefinesuser-leveldocumentdivisioncommandssuchas
\chapter or \section. This approach is not compatible with internal command
changes applied by the biblatex refsection, refsegment and citereset option
settingsdescribedin§3.1.2.1.
ucs Theucspackageprovidessupportforutf-8encodedinput,butitdoessoinaway
incompatiblewithbiblatex.
If you get an error about ucs being loaded, but you don’t load it explic-
itly in your preamble, check that you don’t load inputenc’s utf8x module:
\usepackage[utf8x]{inputenc}willalsoloaducs.
Insteadofucs/utf8xuseaUnicodeenginesuchasXeTeXorLuaTeXifyouwantfull
Unicodesupport. IfyouusepdfTeXorTeX,theUnicodecharacterspredefinedbythe
LaTeXformatareusuallyenoughformanyusecases(thisistrueforLaTeXfromApril
2018orlater, in olderversionsload inputencwiththeutf8module)andmissing
characterscanbedefinedusing\DeclareUnicodeCharacterornewunicodechar’s
\newunicodechar.
6

etextools Theetextoolspackageprovidesenhancementstolistmacrosdefinedbyetoolbox
andafewothertoolsforcommanddefinitions. Thepackageredefineslisthandling
macrosinawayincompatiblewithbiblatex.
If you must load the etextools package at all costs, define the control sequence
\blx@noerroretextools before you load biblatex. If \blx@noerroretextools is
defined,noerrorwillbeissuedifetextoolsisloaded,themessageisdegradedtoa
warninginstead. Inthatcaseyouneedtomakesurethatallredefinedmacrosused
bybiblatex(currentlyonly\forlistloop)havetheiroriginaletoolboxdefinitions
whenbiblatexisloaded.
1.5.6 CompatibilityMatrixforbiber
biberversionsarecloselycoupledwithbiblatexversions. Youneedtohavethe
rightcombinationofthetwo. biberwillthrowafatalerrorduringprocessingifit
encountersinformationwhichcomesfromabiblatexversionwhichisincompatible.
Table1showsacompatibilitymatrixfortherecentversions.
2 Database Guide
Thissectiondescribesthedefaultdatamodeldefinedintheblx-dm.deffilewhich
is part of biblatex. The data model is defined using the macros documented in
§ 4.5.4. It is possible to redefine the data model which both biblatex and biber
usesothatdatasourcescancontainnewentrytypesandfields(whichofcoursewill
needstylesupport). Thedatamodelspecificationalsoallowsforconstraintstobe
definedsothatdatasourcescanbevalidatedagainstthedatamodel(usingbiber’s
--validate-datamodeloption). Userswhowanttocustomisethedatamodelneed
tolookattheblx-dm.deffileandtoread§4.5.4.
Allentrytypesandfieldnamesaregiveninall-lowercaseformhere. Thisishow
theentrytypesandfieldnamesaregiveninthedatamodel. Whilethebiber/BibTeX
input side is case insensitive, the LaTeX side is case sensitive and uses the exact
capitalisation from the data model. This means that the input in the bib file may
useanycapitalisationofentrytypesandfieldnames,butwhenthefieldsareused
intheLaTeXdocument—forexamplein\citefield—thecapitalisationmustmatch
thecapitalisationinthedatamodel,forstandardtypesandfieldsthatwouldbeall
lowercase.
2.1 EntryTypes
Thissectiongivesanoverviewoftheentrytypessupportedbythedefaultbiblatex
datamodelalongwiththefieldssupportedbyeachtype.
2.1.1 RegularTypes
The lists below indicate the fields supported by each entry type. Note that the
mappingoffieldstoanentrytypeisultimatelyatthediscretionofthebibliography
style. Thelistsbelowthereforeservetwopurposes. Theyindicatethefieldssupported
bythestandardstyleswhichcomewiththispackageandtheyalsoserveasamodel
forcustomstyles. Notethatthe‘required’fieldsarenotstrictlyrequiredinallcases,
see§2.3.2fordetails. Thefieldsmarkedas‘optional’areoptionalinatechnicalsense.
Bibliographicalformattingrulesusuallyrequiremorethanjustthe‘required’fields.
Thedefaultdatamodeldefinedafewconstraintsfortheformatofdatefields,ISBNs
andsomespecialfieldslikegenderbuttheconstraintsareonlyusedifvalidating
7

Table1:biber/biblatexcompatibilitymatrix
Biberversion biblatexversion
2.21 3.21
2.20 3.20
2.19 3.19
2.18 3.18
2.17 3.17
2.16 3.16
2.15 3.15
2.14 3.14
2.13 3.13
2.12 3.12
2.11 3.11
2.10 3.10
2.9 3.9
2.8 3.8
2.7 3.7
2.6 3.5,3.6
2.5 3.4
2.4 3.3
2.3 3.2
2.2 3.1
2.1 3.0
2.0 3.0
1.9 2.9
1.8 2.8
1.7 2.7
1.6 2.6
1.5 2.5
1.4 2.4
1.3 2.3
1.2 2.1,2.2
1.1 2.1
1.0 2.0
0.9.9 1.7x
0.9.8 1.7x
0.9.7 1.7x
0.9.6 1.7x
0.9.5 1.6x
0.9.4 1.5x
0.9.3 1.5x
0.9.2 1.4x
0.9.1 1.4x
0.9 1.4x
8

againstthedatamodelwithbiber’s--validate-datamodeloption. Genericfields
likeabstractandannotationorlabelandshorthandarenotincludedinthelists
belowbecausetheyareindependentoftheentrytype. Thespecialfieldsdiscussed
in§2.2.3,whicharealsoindependentoftheentrytype,arenotincludedinthelists
either. Seethedefaultdatamodelspecificationinthefileblx-dm.defwhichcomes
withbiblatexforacompletespecification.
The ‘alias’ relation referred to in this subsection is the ‘soft alias’ defined with
\DeclareBibliographyAlias. Thatmeansthatthealiaswillusethesamebibliogra-
phy driver as the type it is aliased to, but that its type-specific formatting is still
handledindependentlyofthealiasedtype.
article An article in a journal, magazine, newspaper, or other periodical which forms a
self-contained unit with its own title. The title of the periodical is given in the
journaltitlefield. Iftheissuehasitsowntitleinadditiontothemaintitleofthe
periodical,itgoesintheissuetitlefield. Notethateditorandrelatedfieldsrefer
tothejournalwhiletranslatorandrelatedfieldsrefertothearticle.
Requiredfields: author,title,journaltitle,year/date
Optionalfields: translator,annotator,commentator,subtitle,titleaddon,
editor,editora,editorb,editorc,journalsubtitle,journaltitleaddon,
issuetitle,issuesubtitle,issuetitleaddon,language,origlanguage,series,
volume,number,eid,issue,month,pages,version,note,issn,addendum,
pubstate,doi,eprint,eprintclass,eprinttype,url,urldate
book Asingle-volumebookwithoneormoreauthorswheretheauthorssharecreditfor
theworkasawhole. Thisentrytypealsocoversthefunctionofthe@inbooktypeof
traditionalBibTeX,see§2.3.1fordetails.
Requiredfields: author,title,year/date
Optionalfields: editor,editora,editorb,editorc,translator,annotator,
commentator,introduction,foreword,afterword,subtitle,titleaddon,
maintitle,mainsubtitle,maintitleaddon,language,origlanguage,volume,
part,edition,volumes,series,number,note,publisher,location,isbn,eid,
chapter,pages,pagetotal,addendum,pubstate,doi,eprint,eprintclass,
eprinttype,url,urldate
mvbook Amulti-volume@book. Forbackwardscompatibility,multi-volumebooksarealso
supported by the entry type @book. However, it is advisable to make use of the
dedicatedentrytype@mvbook.
Requiredfields: author,title,year/date
Optionalfields: editor,editora,editorb,editorc,translator,annotator,
commentator,introduction,foreword,afterword,subtitle,titleaddon,
language,origlanguage,edition,volumes,series,number,note,publisher,
location,isbn,pagetotal,addendum,pubstate,doi,eprint,eprintclass,
eprinttype,url,urldate
inbook Apartofabookwhichformsaself-containedunitwithitsowntitle. Notethatthe
profileofthisentrytypeisdifferentfromstandardBibTeX,see§2.3.1.
Requiredfields: author,title,booktitle,year/date
9

Optionalfields: bookauthor,editor,editora,editorb,editorc,translator,
annotator,commentator,introduction,foreword,afterword,subtitle,
titleaddon,maintitle,mainsubtitle,maintitleaddon,booksubtitle,
booktitleaddon,language,origlanguage,volume,part,edition,volumes,
series,number,note,publisher,location,isbn,eid,chapter,pages,addendum,
pubstate,doi,eprint,eprintclass,eprinttype,url,urldate
bookinbook This type is similar to @inbook but intended for works originally published as a
stand-alonebook. Atypicalexamplearebooksreprintedinthecollectedworksof
anauthor.
suppbook Supplementalmaterialina@book. Thistypeiscloselyrelatedtothe@inbookentry
type. While@inbookisprimarilyintendedforapartofabookwithitsowntitle(e.g.,
a single essay in a collection of essays by the same author), this type is provided
for elements such as prefaces, introductions, forewords, afterwords, etc. which
oftenhaveagenerictitleonly. Styleguidesmayrequiresuchitemstobeformatted
differentlyfromother@inbookitems. Thestandardstyleswilltreatthisentrytype
asanaliasfor@inbook.
booklet Abook-likeworkwithoutaformalpublisherorsponsoringinstitution. Usethefield
howpublished to supply publishing information in free format, if applicable. The
fieldtypemaybeusefulaswell.
Requiredfields: author/editor,title,year/date
Optionalfields: subtitle,titleaddon,language,howpublished,type,note,
location,eid,chapter,pages,pagetotal,addendum,pubstate,doi,eprint,
eprintclass,eprinttype,url,urldate
collection Asingle-volumecollectionwithmultiple,self-containedcontributionsbydistinct
authorswhichhavetheirowntitle. Theworkasawholehasnooverallauthorbutit
willusuallyhaveaneditor.
Requiredfields: editor,title,year/date
Optionalfields: editora,editorb,editorc,translator,annotator,commentator,
introduction,foreword,afterword,subtitle,titleaddon,maintitle,
mainsubtitle,maintitleaddon,language,origlanguage,volume,part,edition,
volumes,series,number,note,publisher,location,isbn,eid,chapter,pages,
pagetotal,addendum,pubstate,doi,eprint,eprintclass,eprinttype,url,
urldate
mvcollection Amulti-volume@collection. Forbackwardscompatibility,multi-volumecollections
arealsosupportedbytheentrytype@collection. However,itisadvisabletomake
useofthededicatedentrytype@mvcollection.
Requiredfields: editor,title,year/date
Optionalfields: editora,editorb,editorc,translator,annotator,commentator,
introduction,foreword,afterword,subtitle,titleaddon,language,
origlanguage,edition,volumes,series,number,note,publisher,location,
isbn,pagetotal,addendum,pubstate,doi,eprint,eprintclass,eprinttype,url,
urldate
incollection Acontributiontoacollectionwhichformsaself-containedunitwithadistinctauthor
andtitle. Theauthorreferstothetitle,theeditortothebooktitle,i.e.,thetitle
ofthecollection.
10

Requiredfields: author,title,editor,booktitle,year/date
Optionalfields: editor,editora,editorb,editorc,translator,annotator,
commentator,introduction,foreword,afterword,subtitle,titleaddon,
maintitle,mainsubtitle,maintitleaddon,booksubtitle,booktitleaddon,
language,origlanguage,volume,part,edition,volumes,series,number,note,
publisher,location,isbn,eid,chapter,pages,addendum,pubstate,doi,eprint,
eprintclass,eprinttype,url,urldate
suppcollection Supplemental material in a @collection. This type is similar to @suppbook but
relatedtothe@collectionentrytype. Thestandardstyleswilltreatthisentrytype
asanaliasfor@incollection.
dataset Adatasetorasimilarcollectionof(mostly)rawdata.
Requiredfields: author/editor,title,year/date
Optionalfields: subtitle,titleaddon,language,edition,type,series,number,
version,note,organization,publisher,location,addendum,pubstate,doi,
eprint,eprintclass,eprinttype,url,urldate
manual Technicalorotherdocumentation,notnecessarilyinprintedform. Theauthoror
editorisomissibleintermsof§2.3.2.
Requiredfields: author/editor,title,year/date
Optionalfields: subtitle,titleaddon,language,edition,type,series,number,
version,note,organization,publisher,location,isbn,eid,chapter,pages,
pagetotal,addendum,pubstate,doi,eprint,eprintclass,eprinttype,url,
urldate
misc Afallbacktypeforentrieswhichdonotfitintoanyothercategory. Usethefield
howpublished to supply publishing information in free format, if applicable. The
fieldtypemaybeusefulaswell. author,editor,andyearareomissibleintermsof
§2.3.2.
Requiredfields: author/editor,title,year/date
Optionalfields: subtitle,titleaddon,language,howpublished,type,version,
note,organization,location,month,addendum,pubstate,doi,eprint,
eprintclass,eprinttype,url,urldate
online Anonlineresource. author,editor,andyearareomissibleintermsof§2.3.2. This
entrytypeisintendedforsourcessuchaswebsiteswhichareintrinsicallyonline
resources. Notethatallentrytypessupporttheurlfield. Forexample,whenadding
anarticlefromanonlinejournal,itmaybepreferabletousethe@articletypeand
itsurlfield.
Requiredfields: author/editor,title,year/date,doi/eprint/url
Optionalfields: subtitle,titleaddon,language,version,note,organization,
month,addendum,pubstate,eprintclass,eprinttype,urldate
patent Apatentorpatentrequest. Thenumberorrecordtokenisgiveninthenumberfield.
Usethetypefieldtospecifythetypeandthelocationfieldtoindicatethescopeof
thepatent,ifdifferentfromthescopeimpliedbythetype. Notethatthelocation
fieldistreatedasakeylistwiththisentrytype,see§2.2.1fordetails.
Requiredfields: author,title,number,year/date
11

Optionalfields: holder,subtitle,titleaddon,type,version,location,note,
month,addendum,pubstate,doi,eprint,eprintclass,eprinttype,url,urldate
periodical Ancompleteissueofaperiodical,suchasaspecialissueofajournal. Thetitleofthe
periodicalisgiveninthetitlefield. Iftheissuehasitsowntitleinadditiontothe
maintitleoftheperiodical,itgoesintheissuetitlefield. Theeditorisomissible
intermsof§2.3.2.
Requiredfields: editor,title,year/date
Optionalfields: editora,editorb,editorc,subtitle,titleaddon,issuetitle,
issuesubtitle,issuetitleaddon,language,series,volume,number,issue,
month,note,issn,addendum,pubstate,doi,eprint,eprintclass,eprinttype,
url,urldate
suppperiodical Supplementalmaterialina@periodical. Thistypeissimilarto@suppbookbutrelated
tothe@periodicalentrytype. Theroleofthisentrytypemaybemoreobviousif
youbearinmindthatthe@articletypecouldalsobecalled@inperiodical. This
type may be useful when referring to items such as regular columns, obituaries,
letterstotheeditor,etc. whichonlyhaveagenerictitle. Styleguidesmayrequire
suchitemstobeformatteddifferentlyfromarticlesinthestrictsenseoftheword.
Thestandardstyleswilltreatthisentrytypeasanaliasfor@article.
proceedings Asingle-volumeconferenceproceedings. Thistypeisverysimilarto@collection.
Itsupportsanoptionalorganizationfieldwhichholdsthesponsoringinstitution.
Theeditorisomissibleintermsof§2.3.2.
Requiredfields: title,year/date
Optionalfields: editor,subtitle,titleaddon,maintitle,mainsubtitle,
maintitleaddon,eventtitle,eventtitleaddon,eventdate,venue,language,
volume,part,volumes,series,number,note,organization,publisher,location,
month,isbn,eid,chapter,pages,pagetotal,addendum,pubstate,doi,eprint,
eprintclass,eprinttype,url,urldate
mvproceedings A multi-volume @proceedings entry. For backwards compatibility, multi-volume
proceedings are also supported by the entry type @proceedings. However, it is
advisabletomakeuseofthededicatedentrytype@mvproceedings
Requiredfields: title,year/date
Optionalfields: editor,subtitle,titleaddon,eventtitle,eventtitleaddon,
eventdate,venue,language,volumes,series,number,note,organization,
publisher,location,month,isbn,pagetotal,addendum,pubstate,doi,eprint,
eprintclass,eprinttype,url,urldate
inproceedings An article in a conference proceedings. This type is similar to @incollection. It
supportsanoptionalorganizationfield.
Requiredfields: author,title,booktitle,year/date
Optionalfields: editor,subtitle,titleaddon,maintitle,mainsubtitle,
maintitleaddon,booksubtitle,booktitleaddon,eventtitle,eventtitleaddon,
eventdate,venue,language,volume,part,volumes,series,number,note,
organization,publisher,location,month,isbn,eid,chapter,pages,addendum,
pubstate,doi,eprint,eprintclass,eprinttype,url,urldate
12

reference Asingle-volumeworkofreferencesuchasanencyclopediaoradictionary. Thisis
amorespecificvariantofthegeneric@collectionentrytype. Thestandardstyles
willtreatthisentrytypeasanaliasfor@collection.
mvreference Amulti-volume@referenceentry. Thestandardstyleswilltreatthisentrytypeas
analiasfor@mvcollection. Forbackwardscompatibility,multi-volumereferences
arealsosupportedbytheentrytype@reference. However,itisadvisabletomake
useofthededicatedentrytype@mvreference.
inreference An article in a work of reference. This is a more specific variant of the generic
@incollectionentrytype. Thestandardstyleswilltreatthisentrytypeasanalias
for@incollection.
report Atechnicalreport,researchreport,orwhitepaperpublishedbyauniversityorsome
otherinstitution. Usethetypefieldtospecifythetypeofreport. Thesponsoring
institutiongoesintheinstitutionfield.
Requiredfields: author,title,type,institution,year/date
Optionalfields: subtitle,titleaddon,language,number,version,note,
location,month,isrn,eid,chapter,pages,pagetotal,addendum,pubstate,doi,
eprint,eprintclass,eprinttype,url,urldate
set Anentryset. Thisentrytypeisspecial,see§3.14.5fordetails.
software Computer software. The standard styles will treat this entry type as an alias for
@misc.
thesis Athesiswrittenforaneducationalinstitutiontosatisfytherequirementsforadegree.
Usethetypefieldtospecifythetypeofthesis.
Requiredfields: author,title,type,institution,year/date
Optionalfields: subtitle,titleaddon,language,note,location,month,isbn,
eid,chapter,pages,pagetotal,addendum,pubstate,doi,eprint,eprintclass,
eprinttype,url,urldate
unpublished Aworkwithanauthorandatitlewhichhasnotbeenformallypublished,suchasa
manuscriptorthescriptofatalk. Usethefieldshowpublishedandnotetosupply
additionalinformationinfreeformat,ifapplicable.
Requiredfields: author,title,year/date
Optionalfields: subtitle,titleaddon,type,eventtitle,eventtitleaddon,
eventdate,venue,language,howpublished,note,location,isbn,month,
addendum,pubstate,doi,eprint,eprintclass,eprinttype,url,urldate
xdata Thisentrytypeisspecial. @xdataentriesholddatawhichmaybeinheritedbyother
entriesusingthexdatafield. Entriesofthistypeonlyserveasdatacontainers;they
maynotbecitedoraddedtothebibliography. See§3.14.6fordetails.
custom[a–f] Customtypesforspecialbibliographystyles. Thestandardstylesdefinednobiblio-
graphydriversforthesetypesandwillfallbacktousingthedriverfor@misc.
13

2.1.2 TypeAliases
Theentrytypeslistedinthissectionareprovidedforbackwardscompatibilitywith
traditionalBibTeXstyles. Thesealiasesareresolvedbythebackendasthedatais
processed. biblatexandthestyleswillseeonlytheentrytypethealiaspointsto
(thetarget), notthealiasname(thesource). Inparticularbiblatex-sideper-type
operationsliketype-specificformattingandfilteringonlyworkforthetargettype,
notthesourcetype. This‘hardalias’isunlikethe‘softalias’relationintheprevious
subsection. Therelevantmappingsforthebibtexdrivercanbefoundin§A.1.
conference Alegacyaliasfor@inproceedings.
electronic Analiasfor@online.
mastersthesis Similarto@thesisexceptthatthetypefieldisoptionalanddefaultstothelocalised
term‘Master’sthesis’. Youmaystillusethetypefieldtooverridethat.
phdthesis Similarto@thesisexceptthatthetypefieldisoptionalanddefaultstothelocalised
term‘PhDthesis’. Youmaystillusethetypefieldtooverridethat.
techreport Similarto@reportexceptthatthetypefieldisoptionalanddefaultstothelocalised
term‘technicalreport’. Youmaystillusethetypefieldtooverridethat.
www Analiasfor@online,providedforjurabibcompatibility.
2.1.3 Non-standardTypes
The types in this section are similar to the custom types @custom[a--f], i.e., the
standardbibliographystylesprovidenobibliographydriversforthesetypes. Inthe
standardstylestheywillusethebibliographydriverfor@miscentries—exceptions
tothisrulearenotedinthedescriptionsbelow. Thetypesareknowntothedefault
datamodelandwillbehappilyacceptedbybiber.
artwork Worksofthevisualartssuchaspaintings,sculpture,andinstallations.
audio Audiorecordings,typicallyonaudiocd,dvd,audiocassette,orsimilarmedia. See
also@music.
bibnote This special entry type is not meant to be used in the bib file like other types. It
is provided for third-party packages like notes2bib which merge notes into the
bibliography. Thenotesshouldgointothenotefield. Beadvisedthatthe@bibnote
type is not related to the \defbibnote command in any way. \defbibnote is for
adding comments at the beginning or the end of the bibliography, whereas the
@bibnotetypeismeantforpackageswhichrenderendnotesasbibliographyentries.
commentary Commentarieswhichhaveastatusdifferentfromregularbooks,suchaslegalcom-
mentaries.
image Images,pictures,photographs,andsimilarmedia.
jurisdiction Courtdecisions,courtrecordings,andsimilarthings.
legislation Laws,bills,legislativeproposals,andsimilarthings.
legal Legaldocumentssuchastreaties.
letter Personalcorrespondencesuchasletters,emails,memoranda,etc.
14

movie Motionpictures. Seealso@video.
music Musicalrecordings. Thisisamorespecificvariantof@audio.
performance Musicalandtheatricalperformancesaswellasotherworksoftheperformingarts.
Thistypereferstotheeventasopposedtoarecording,ascore,oraprintedplay.
review Reviewsofsomeotherwork. Thisisamorespecificvariantofthe@articletype.
Thestandardstyleswilltreatthisentrytypeasanaliasfor@article.
standard NationalandinternationalstandardsissuedbyastandardsbodysuchastheInterna-
tionalOrganizationforStandardization.
video Audiovisualrecordings,typicallyondvd,vhscassette,orsimilarmedia. Seealso
@movie.
2.2 EntryFields
Thissectiongivesanoverviewofthefieldssupportedbythebiblatexdefaultdata
model. See § 2.2.1 for an introduction to the data types used by the data model
specificationand§§2.2.2and2.2.3fortheactualfieldlistings.
2.2.1 DataTypes
Indatasourcessuchasabibfile,allbibliographicdataisspecifiedinfields. Some
ofthosefields,forexampleauthorandeditor,maycontainalistofitems. Thislist
structureisimplementedbytheBibTeXfileformatviathekeyword‘and’,whichis
usedtoseparatetheindividualitemsinthelist. Thebiblatexpackageimplements
threedistinctdatatypestohandlebibliographicdata: namelists,literallists,and
fields. Therearealsoseverallistandfieldsubtypesandacontenttypewhichcanbe
usedtosemanticallydistinguishfieldswhichareotherwisenotdistinguishableon
thebasisofonlytheirdatatype(see§4.5.4). Thissectiongivesanoverviewofthe
datatypessupportedbythispackage. See§§2.2.2and2.2.3forinformationabout
themappingoftheBibTeXfileformatfieldstobiblatex’sdatatypes.
Namelists are parsed and split up into the individual items at the and delimiter.
Each item in the list is then dissected into the name part components: by
default the given name, the name prefix (von, van, of, da, de, della, …), the
family name, and the name suffix (junior, senior, …). The valid name parts
canbecustomisedbychangingthedatamodeldefinitiondescribedin§4.2.3.
Namelistsmaybetruncatedinthebibfilewiththekeyword‘and others’.
Typicalexamplesofnamelistsareauthorandeditor.
Namelistfieldsautomaticallyhavean\ifuse*testcreatedasperthename
listsinthedefaultdatamodel(see§4.6.2). Theyalsoautomaticallyhavean
ifuse* option created which controls labelling and sorting behaviour with
thename(see§3.1.3.1). bibersupportsacustomisablesetofnamepartsbut
currentlythisisdefinedtobethesamesetofpartsassupportedbytraditional
BibTeX:
• Familyname(alsoknownas‘last’part)
• Givenname(alsoknownas‘first’part)
• Nameprefix(alsoknownas‘von’part)
• Namesuffix(alsoknownas‘Jr’part)
15

The supported list of name parts is defined as a constant list in the de-
faultdatamodelusingthe\DeclareDatamodelConstantcommand(see4.5.4).
However, it is not enough to simply add to this list in order to add sup-
port for another name part as name parts typically have to be hard coded
into bibliography drivers and the backend processing. See the example file
93-nameparts.tex fordetails on howto define and use custom name parts.
Alsosee\DeclareUniquenameTemplatein§4.11.4forinformationonhowto
customisenamedisambiguationusingcustomnameparts.
Literallists areparsedandsplitupintotheindividualitemsattheanddelimiter
butnotdissectedfurther. Literallistsmaybetruncatedinthebibfilewiththe
| keyword‘and | others’. | Therearetwosubtypes: |     |     |     |     |     |     |     |
| ----------- | -------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
Literallists inthestrictsensearehandledasdescribedabove. Theindividual
| itemsaresimplyprintedasis. |     |     |     | Typicalexamplesofsuchliterallistsare |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
publisherandlocation.
Keylists areavariantofliterallistswhichmayholdprintabledataorlocal-
| isation | keys. | For each | item in | the list, | styles | should | perform | a   | test to |
| ------- | ----- | -------- | ------- | --------- | ------ | ------ | ------- | --- | ------- |
determinewhetheritisaknownlocalisationkey(thelocalisationkeys
| definedbydefaultarelistedin§4.9.2). |                                   |         |                |     | Ifso,thelocalisedstringshould |           |                   |        |     |
| ----------------------------------- | --------------------------------- | ------- | -------------- | --- | ----------------------------- | --------- | ----------------- | ------ | --- |
| beprinted.                          | Ifnot,theitemshouldbeprintedasis. |         |                |     |                               |           | Thestandardstyles |        |     |
| are set                             | up to                             | exhibit | this behaviour |     | for all                       | key lists | listed            | below. | New |
keylistsdonotautomaticallyperformthistest,ithastobeimplemented
| explicitlyviathelistformat.       |     |     | Atypicalexampleofakeylistislanguage. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| Fields areusuallyprintedasawhole. |     |     | Thereareseveralsubtypes:             |     |     |     |     |     |     |
Literalfields areprintedasis. Typicalexamplesofliteralfieldsaretitle
andnote.
Rangefields consist of one or more ranges where all dashes are normal-
| ized and                                    | replaced                                       | by       | the command |                                   | \bibrangedash. |        | A range           | is       | some- |
| ------------------------------------------- | ---------------------------------------------- | -------- | ----------- | --------------------------------- | -------------- | ------ | ----------------- | -------- | ----- |
| thing optionally                            |                                                | followed | by          | one or                            | more           | dashes | optionally        | followed |       |
| bysomenon-dash(e.g.                         |                                                |          | 5--7).      | Anynumberofconsecutivedasheswill  |                |        |                   |          |       |
| onlyyieldasinglerangedash.                  |                                                |          |             | Atypicalexampleofarangefieldisthe |                |        |                   |          |       |
| pagesfield.                                 | Seealsothe\bibrangessepcommandwhichcanbeusedto |          |             |                                   |                |        |                   |          |       |
| customisetheseparatorbetweenmultipleranges. |                                                |          |             |                                   |                |        | Rangefieldswillbe |          |       |
skippedandwillgenerateawarningiftheydonotconsistofoneormore
| ranges. | You | can normalise | messy | range |     | fields before | they | are parsed |     |
| ------- | --- | ------------- | ----- | ----- | --- | ------------- | ---- | ---------- | --- |
using\DeclareSourcemap(see§4.5.3).
Integerfields holdintegerswhichmaybeconvertedtoordinalsorstrings
| astheyareprinted.              |            | Atypicalexampleistheextradateorvolumefield. |     |                                   |                              |          |              |          |     |
| ------------------------------ | ---------- | ------------------------------------------- | --- | --------------------------------- | ---------------------------- | -------- | ------------ | -------- | --- |
| Suchfieldsaresortedasintegers. |            |                                             |     | bibermakesa(quiteserious)effort   |                              |          |              |          |     |
| to map                         | non-arabic | representations                             |     |                                   | (roman                       | numerals | for          | example) | to  |
| integersforsortingpurposes.    |            |                                             |     | Seethenoromanoptionwhichcanbeused |                              |          |              |          |     |
| tosuppressromannumeralparsing. |            |                                             |     |                                   | Thiscanhelpincaseswherethere |          |              |          |     |
| isan ambiguity                 |            | betweenparsing                              |     | as                                | romannumeralsor              |          | alphanumeric |          |     |
(e.g. ‘C’),see§3.1.2.3.
Datepartfields hold unformatted integers which may be converted
| to ordinals |                 | or strings | as they            | are   | printed. |          | A typical        | example   |       |
| ----------- | --------------- | ---------- | ------------------ | ----- | -------- | -------- | ---------------- | --------- | ----- |
| is the      | month           | field.     | For every          | field | of       | datatype | date             | in the    | data- |
| model,      | datepart        | fields     | are automatically  |       |          | created  | with the         | following |       |
| names:      | <datetype>year, |            | <datetype>endyear, |       |          |          | <datetype>month, |           |       |
16

<datetype>endmonth, <datetype>day, <datetype>endday,
<datetype>hour, <datetype>endhour, <datetype>minute,
<datetype>endminute, <datetype>second, <datetype>endsecond,
<datetype>timezone, <datetype>endtimezone. <datetype> is the
string preceding ‘date’ for any datamodel field of datatype=date. For
example, in the default datamodel, ‘event’, ‘orig’, ‘url’ and the empty
string‘’forthedatefielddate.
Datefields holdadatespecificationinyyyy-mm-ddThh:nn[+-][hh[:nn]Z]
format or a date range in yyyy-mm-ddThh:nn[+-][hh[:nn]Z]/yyyy-
mm-ddThh:nn[+-][hh[:nn]Z] format and other formats permitted by
iso8601-2 Clause 4, level 1, see § 2.3.8. Date fields are special in that
thedateisparsedandsplitupintoitsdateparttypecomponents. The
datepartcomponents(seeabove)areautomaticallydefinedandrecog-
nisedwhenafieldofdatatypedateisdefinedinthedatamodel. Atypical
exampleisthedatefield.
Verbatimfields are processed in verbatim mode and may contain special
characters. Typicalexamplesofverbatimfieldsarefileanddoi.
URIfields areprocessedinverbatimmodeandmaycontainspecialcharac-
ters. TheyarealsoURL-escapediftheydon’tlookliketheyalreadyare.
Thetypicalexampleofaurifieldisurl.
Separatedvaluefields Aseparatedlistofliteralvalues. Examplesarethe
keywordsandoptionsfields. Theseparatorcanbeconfiguredtobeany
Perlregularexpressionviathexsvsepoptionwhichdefaultstotheusual
BibTeXcommasurroundedbyoptionalwhitespace.
Patternfields A literal field which must match a particular pattern. An
exampleisthegenderfieldfrom§2.2.3.
Keyfields Mayholdprintabledataorlocalisationkeys. Stylesshouldperform
atesttodeterminewhetherthevalueofthefieldisaknownlocalisation
key(thelocalisationkeysdefinedbydefaultarelistedin§4.9.2). Ifso,
thelocalisedstringshouldbeprinted. Ifnot,thevalueshouldbeprinted
asis. Thestandardstylesaresetuptohandleallkeyfieldslistedbelow
inthatway. Newkeyfieldsdonotautomaticallyperformthetest,ithas
tobeenabledexplicitlyinthefieldformat. Atypicalexampleisthetype
field.
Codefields HoldsTeXcode.
2.2.2 DataFields
The fields listed in this section are the regular ones holding printable data in the
defaultdatamodel. Thenameontheleftisthedefaultdatamodelnameofthefield
asusedbybiblatexanditsbackend. Thebiblatexdatatypeisgiventotherightof
thename. See§2.2.1forexplanationofthevariousdatatypes.
Somefieldsaremarkedas‘label’fieldswhichmeansthattheyareoftenusedas
abbreviationlabelswhenprintingbibliographylistsinthesenseofsection§3.8.3.
biblatexautomaticallycreatessupportingmacrosforsuchfields. See§3.8.3.
abstract field(literal)
Thisfieldisintendedforrecordingabstractsinabibfile,tobeprintedbyaspecial
bibliographystyle. Itisnotusedbyallstandardbibliographystyles.
17

addendum field(literal)
Miscellaneousbibliographicdatatobeprintedattheendoftheentry. Thisissimilar
tothenotefieldexceptthatitisprintedattheendofthebibliographyentry.
afterword list(name)
Theauthor(s)ofanafterwordtothework. Iftheauthoroftheafterwordisidentical
totheeditorand/ortranslator,thestandardstyleswillautomaticallyconcatenate
thesefieldsinthebibliography. Seealsointroductionandforeword.
annotation field(literal)
Thisfieldmaybeusefulwhenimplementingastyleforannotatedbibliographies.
Itisnotusedbyallstandardbibliographystyles. Notethatthisfieldiscompletely
unrelatedtoannotator. Theannotatoristheauthorofannotationswhicharepart
oftheworkcited.
annotator list(name)
Theauthor(s)ofannotationstothework. Iftheannotatorisidenticaltotheeditor
and/ortranslator,thestandardstyleswillautomaticallyconcatenatethesefields
inthebibliography. Seealsocommentator.
author list(name)
Theauthor(s)ofthetitle.
authortype field(key)
The type of author. This field will affect the string (if any) used to introduce the
author.
bookauthor list(name)
Theauthor(s)ofthebooktitle.
bookpagination field(key)
Iftheworkispublishedaspartofanotherone,thisisthepaginationschemeofthe
enclosingwork,i.e.,bookpaginationrelatestopaginationlikebooktitletotitle.
Thevalueofthisfieldwillaffecttheformattingofthepagesandpagetotalfields.
Thekeyshouldbegiveninthesingularform. Possiblekeysarepage,column,line,
verse,section,andparagraph. Seealsopaginationaswellas§2.3.12.
booksubtitle field(literal)
Thesubtitlerelatedtothebooktitle. Ifthesubtitlefieldreferstoaworkwhichis
partofalargerpublication,apossiblesubtitleofthemainworkisgiveninthisfield.
Seealsosubtitle.
booktitle field(literal)
Ifthetitlefieldindicatesthetitleofaworkwhichispartofalargerpublication,
thetitleofthemainworkisgiveninthisfield. Seealsotitle.
booktitleaddon field(literal)
Anannextothebooktitle,tobeprintedinadifferentfont.
18

chapter field(literal)
Achapterorsectionoranyotherunitofawork.
commentator list(name)
The author(s) of a commentary to the work. Note that this field is intended for
commentededitionswhichhaveacommentatorinadditiontotheauthor. Ifthework
isastand-alonecommentary,thecommentatorshouldbegivenintheauthorfield.
Ifthecommentatorisidenticaltotheeditorand/ortranslator,thestandardstyles
willautomaticallyconcatenatethesefieldsinthebibliography. Seealsoannotator.
date field(date)
Thepublicationdate. Seealsomonthandyearaswellas§§2.3.8and2.3.9.
doi field(verbatim)
TheDigitalObjectIdentifierofthework.
edition field(integerorliteral)
Theeditionofaprintedpublication. Thismustbeaninteger,notanordinal. Don’t
say edition={First} or edition={1st} but edition={1}. The bibliography style
convertsthistoalanguagedependentordinal. Itisalsopossibletogivetheedition
asaliteralstring,forexample“Third,revisedandexpandededition”.
editor list(name)
Theeditor(s)ofthetitle,booktitle,ormaintitle,dependingontheentrytype.
Usetheeditortypefieldtospecifytheroleifitisdifferentfrom‘editor’. See§2.3.6
forfurtherhints.
editora list(name)
Asecondaryeditorperformingadifferenteditorialrole,suchascompiling,redacting,
etc. Usetheeditoratypefieldtospecifytherole. See§2.3.6forfurtherhints.
editorb list(name)
Anothersecondaryeditorperformingadifferentrole. Usetheeditorbtypefieldto
specifytherole. See§2.3.6forfurtherhints.
editorc list(name)
Anothersecondaryeditorperformingadifferentrole. Usetheeditorctypefieldto
specifytherole. See§2.3.6forfurtherhints.
editortype field(key)
The type of editorial role performed by the editor. Roles supported by default
are editor, compiler, founder, continuator, redactor, reviser, collaborator,
organizer. Therole‘editor’isthedefault. Inthiscase,thefieldisomissible. See
§2.3.6forfurtherhints.
editoratype field(key)
Similartoeditortypebutreferringtotheeditorafield. See§2.3.6forfurtherhints.
19

editorbtype field(key)
Similartoeditortypebutreferringtotheeditorbfield. See§2.3.6forfurtherhints.
editorctype field(key)
Similartoeditortypebutreferringtotheeditorcfield. See§2.3.6forfurtherhints.
eid field(literal)
Theelectronicidentifierofan@articleorchapter-likesectionofalargerworkoften
called‘articlenumber’,‘papernumber’orthelike. Thisfieldmayreplacethepages
fieldforjournalsdeviatingfromtheclassicpaginationschemeofprintedjournalsby
onlyenumeratingarticlesorpapersandnotpages.
Nottobeconfusedwithnumber,whichfor@articlessubdividesthevolume.
entrysubtype field(literal)
Thisfield,whichisnotusedbythestandardstyles,maybeusedtospecifyasubtype
ofanentrytype. Thismaybeusefulforbibliographystyleswhichsupportafiner-
grainedsetofentrytypes.
eprint field(verbatim)
Theelectronicidentifierofanonlinepublication. Thisisroughlycomparabletoa
doibutspecifictoacertainarchive,repository,service,orsystem. See§3.14.7for
details. Alsoseeeprinttypeandeprintclass.
eprintclass field(literal)
Additional information related to the resource indicated by the eprinttype field.
Thiscouldbeasectionofanarchive,apathindicatingaservice,aclassificationof
somesort,etc. See§3.14.7fordetails. Alsoseeeprintandeprinttype.
eprinttype field(literal)
Thetypeofeprintidentifier,e.g.,thenameofthearchive,repository,service,or
system the eprint field refers to. See § 3.14.7 for details. Also see eprint and
eprintclass.
eventdate field(date)
Thedateofaconference,asymposium,orsomeothereventin@proceedingsand
@inproceedingsentries. Thisfieldmayalsobeusefulforthecustomtypeslistedin
§2.1.3. Seealsoeventtitleandvenueaswellas§2.3.8.
eventtitle field(literal)
Thetitleofaconference,asymposium,orsomeothereventin@proceedingsand
@inproceedingsentries. Thisfieldmayalsobeusefulforthecustomtypeslistedin
§2.1.3. Notethatthisfieldholdstheplaintitleoftheevent. Thingslike“Proceed-
ingsoftheFifthXYZConference”gointothetitleaddonorbooktitleaddonfield,
respectively. Seealsoeventdateandvenue.
eventtitleaddon field(literal)
An annex to the eventtitle field. Can be used for known event acronyms, for
example.
20

file field(verbatim)
Alocallinktoapdforotherversionofthework. Notusedbythestandardbiblio-
graphystyles.
foreword list(name)
Theauthor(s)ofaforewordtothework. Iftheauthoroftheforewordisidenticalto
theeditorand/ortranslator,thestandardstyleswillautomaticallyconcatenate
thesefieldsinthebibliography. Seealsointroductionandafterword.
holder list(name)
Theholder(s)ofa@patent,ifdifferentfromtheauthor. Notethatcorporateholders
needtobewrappedinanadditionalsetofbraces,see§2.3.3fordetails. Thislistmay
alsobeusefulforthecustomtypeslistedin§2.1.3.
howpublished field(literal)
Apublicationnoticeforunusualpublicationswhichdonotfitintoanyofthecommon
categories.
indextitle field(literal)
Atitletouseforindexinginsteadoftheregulartitlefield. Thisfieldmaybeuseful
ifyouhaveanentrywithatitlelike“AnIntroductionto…”andwantthatindexed
as“Introductionto…,An”. Styleauthorsshouldnotethatbiblatexautomatically
copiesthevalueofthetitlefieldtoindextitleifthelatterfieldisundefined.
institution list(literal)
The name of a university or some other institution, depending on the entry type.
TraditionalBibTeXusesthefieldnameschoolfortheses,whichissupportedasan
alias. Seealso§§2.2.5and2.3.4.
introduction list(name)
The author(s) of an introduction to the work. If the author of the introduction is
identical to the editor and/or translator, the standard styles will automatically
concatenatethesefieldsinthebibliography. Seealsoforewordandafterword.
isan field(literal)
TheInternationalStandardAudiovisualNumberofanaudiovisualwork. Notused
bythestandardbibliographystyles.
isbn field(literal)
TheInternationalStandardBookNumberofabook.
ismn field(literal)
TheInternationalStandardMusicNumberforprintedmusicsuchasmusicalscores.
Notusedbythestandardbibliographystyles.
isrn field(literal)
TheInternationalStandardTechnicalReportNumberofatechnicalreport.
21

issn field(literal)
TheInternationalStandardSerialNumberofaperiodical.
issue field(literal)
Theissueofajournal. Thisfieldisintendedforjournalswhoseindividualissuesare
identifiedbyadesignationsuchas‘Spring’or‘Summer’ratherthanthemonthora
number. Theplacementofissueissimilartomonthandnumber. Integerrangesand
shortdesignatorsarebetterwrittentothenumberfield. Seealsomonth,numberand
§§2.3.10and2.3.11.
issuesubtitle field(literal)
Thesubtitleofaspecificissueofajournalorotherperiodical.
issuetitle field(literal)
Thetitleofaspecificissueofajournalorotherperiodical.
issuetitleaddon field(literal)
Anannextotheissuetitle,tobeprintedinadifferentfont.
iswc field(literal)
TheInternationalStandardWorkCodeofamusicalwork. Notusedbythestandard
bibliographystyles.
journalsubtitle field(literal)
Thesubtitleofajournal,anewspaper,orsomeotherperiodical.
journaltitle field(literal)
Thenameofajournal,anewspaper,orsomeotherperiodical.
journaltitleaddon field(literal)
Anannextothejournaltitle,tobeprintedinadifferentfont.
label field(literal)
Adesignationtobeusedbythecitationstyleasasubstitutefortheregularlabelif
anydatarequiredtogeneratetheregularlabelismissing. Forexample, whenan
author-yearcitationstyleisgeneratingacitationforanentrywhichismissingthe
author or the year, it may fall back to label. See § 2.3.2 for details. Note that, in
contrasttoshorthand,labelisonlyusedasafallback. Seealsoshorthand.
language list(key)
Thelanguage(s)ofthework. Languagesmaybespecifiedliterallyoraslocalisation
keys(see§4.9.2,especially§4.9.2.18). Iflocalisationkeysareused,theprefixlang
isomissible: bothlangenglishandenglishcanbeused. Iftheclearlangoption
isset,thecontentofthisfieldmaybeclearedifitmatchesthebabel/polyglossia
languageofthedocument(orthelanguagespecifiedexplicitlywiththelanguage
option),see§3.1.2.1. Seealsooriglanguageandcomparelangidin§2.2.3.
22

library field(literal)
This field may be useful to record information such as a library name and a call
number. Thismaybeprintedbyaspecialbibliographystyleifdesired. Notusedby
thestandardbibliographystyles.
location list(literal)
Theplace(s)ofpublication,i.e.,thelocationofthepublisherorinstitution,de-
pendingontheentrytype. TraditionalBibTeXusesthefieldnameaddress,which
issupportedasanalias. Seealso§§2.2.5and2.3.4. With@patententries,thislist
indicates the scope of a patent. This list may also be useful for the custom types
listedin§2.1.3.
mainsubtitle field(literal)
Thesubtitlerelatedtothemaintitle. Seealsosubtitle.
maintitle field(literal)
The main title of a multi-volume book, such as Collected Works. If the title or
booktitlefieldindicatesthetitleofasinglevolumewhichispartofmulti-volume
book,thetitleofthecompleteworkisgiveninthisfield.
maintitleaddon field(literal)
Anannextothemaintitle,tobeprintedinadifferentfont.
month field(literal)
Thepublicationmonth. Thismustbeaninteger,notanordinalorastring. Don’tsay
month={January}butmonth={1}. Thebibliographystyleconvertsthistoalanguage
dependentstringorordinalwhererequired. Thisfieldisaliteralfieldonlywhen
givenexplicitlyinthedata(forplainBibTeXcompatibilityforexample). Itishowever
bettertousethedatefieldasthissupportsmanymorefeatures. See§§2.3.8and
2.3.9.
nameaddon field(literal)
Anaddontobeprintedimmediatelyaftertheauthornameinthebibliography. Not
usedbythestandardbibliographystyles.
note field(literal)
Miscellaneousbibliographicdatawhichdoesnotfitintoanyotherfield. Thenote
fieldmaybeusedtorecordbibliographicdatainafreeformat. Publicationfactssuch
as“ReprintoftheeditionLondon1831”aretypicalcandidatesforthenotefield. See
alsoaddendum.
number field(literal)
Thenumberofajournalorthevolume/numberofabookinaseries. Seealsoissue
aswellas§§2.3.7,2.3.10,2.3.11. With@patententries,thisisthenumberorrecord
token of a patent or patent request. Normally this field will be an integer or an
integerrange,butitmayalsobeashortdesignatorthatisnotentirelynumericsuch
as“S1”,“Suppl.2”,“3es”. Inthesecasestheoutputshouldbescrutinisedcarefully.
23

Since number is—maybe counterintuitively given its name—a literal field, sorting
templateswillnottreatitscontentsasintegers,butasliteralstrings,whichmeans
that“11”maysortbetween“1”and“2”. Ifintegersortingisdesired,thefieldcanbe
declaredanintegerfieldinacustomdatamodel(see§4.5.4). Butthenthesortingof
non-integervaluesisnotwelldefined.
The ‘article number’ or ‘paper number’, which can be used instead of—or along
with—apagerangetopinpointaspecificarticlewithinanotherwork,goesintothe
eidfield.
organization list(literal)
Theorganization(s)thatpublisheda@manualoran@onlineresource,orsponsored
aconference. Seealso§2.3.4.
origdate field(date)
Iftheworkisatranslation,areprint,orsomethingsimilar,thepublicationdateof
theoriginaledition. Notusedbythestandardbibliographystyles. Seealsodate.
origlanguage list(key)
Iftheworkisatranslation,thelanguage(s)oftheoriginalwork. Seealsolanguage.
origlocation list(literal)
If the work is a translation, a reprint, or something similar, the location of the
originaledition. Notusedbythestandardbibliographystyles. Seealsolocation
and§2.3.4.
origpublisher list(literal)
If the work is a translation, a reprint, or something similar, the publisher of the
originaledition. Notusedbythestandardbibliographystyles. Seealsopublisher
and§2.3.4.
origtitle field(literal)
Iftheworkisatranslation,thetitleoftheoriginalwork. Notusedbythestandard
bibliographystyles. Seealsotitle.
pages field(range)
Oneormorepagenumbersorpageranges. Iftheworkispublishedaspartofanother
one,suchasanarticleinajournaloracollection,thisfieldholdstherelevantpage
rangeinthatotherwork. Itmayalsobeusedtolimitthereferencetoaspecificpart
ofawork(achapterinabook,forexample). Forpapersinelectronicjournalswitha
non-classicalpaginationsetuptheeidfieldmaybemoresuitable.
pagetotal field(literal)
Thetotalnumberofpagesofthework.
pagination field(key)
The pagination of the work. The value of this field will affect the formatting the
hpostnoteiargumenttoacitationcommand. Thekeyshouldbegiveninthesingular
form. Possiblekeysarepage,column,line,verse,section,andparagraph. Seealso
bookpaginationaswellas§§2.3.12and3.15.3.
24

| part | field(literal) |     |     |     |     |     |
| ---- | -------------- | --- | --- | --- | --- | --- |
Thenumberofapartialvolume. Thisfieldappliestobooksonly,nottojournals. It
maybeusedwhenalogicalvolumeconsistsoftwoormorephysicalones. Inthis
casethenumberofthelogicalvolumegoesinthevolumefieldandthenumberof
|           | thepartofthatvolumeinthepartfield. |     | Seealsovolume. |     |     |     |
| --------- | ---------------------------------- | --- | -------------- | --- | --- | --- |
| publisher | list(literal)                      |     |                |     |     |     |
|           | Thename(s)ofthepublisher(s).       |     | Seealso§2.3.4. |     |     |     |
| pubstate  | field(key)                         |     |                |     |     |     |
Thepublicationstateofthework,e.g.,‘inpress’. See§4.9.2.11forknownpublication
states.
| reprinttitle | field(literal)               |     |                             |     |     |     |
| ------------ | ---------------------------- | --- | --------------------------- | --- | --- | --- |
|              | Thetitleofareprintofthework. |     | Notusedbythestandardstyles. |     |     |     |
| series       | field(literal)               |     |                             |     |     |     |
Thenameofapublicationseries,suchas“Studiesin…”,orthenumberofajournal
series. Booksinapublicationseriesareusuallynumbered. Thenumberorvolume
ofabookinaseriesisgiveninthenumberfield. Notethatthe@articleentrytype
makesuseoftheseriesfieldaswell,buthandlesitinaspecialway. See§2.3.7for
details.
| shortauthor | list(name) |     |     |     |     | Labelfield |
| ----------- | ---------- | --- | --- | --- | --- | ---------- |
Theauthor(s)ofthework,giveninanabbreviatedform. Thisfieldismainlyintended
forabbreviatedformsofcorporateauthors,see§2.3.3fordetails.
| shorteditor | list(name) |     |     |     |     | Labelfield |
| ----------- | ---------- | --- | --- | --- | --- | ---------- |
Theeditor(s)ofthework,giveninanabbreviatedform. Thisfieldismainlyintended
forabbreviatedformsofcorporateeditors,see§2.3.3fordetails.
| shorthand | field(literal) |     |     |     |     | Labelfield |
| --------- | -------------- | --- | --- | --- | --- | ---------- |
Aspecialdesignationtobeusedbythecitationstyleinsteadoftheusuallabel. If
|                | defined,itoverridesthedefaultlabel. |     | Seealsolabel. |     |     |     |
| -------------- | ----------------------------------- | --- | ------------- | --- | --- | --- |
| shorthandintro | field(literal)                      |     |               |     |     |     |
Theverbosecitationstyleswhichcomeswiththispackageuseaphraselike“hence-
forth cited as [shorthand]” to introduce shorthands on the first citation. If the
|     |     | field is defined, | it overrides | the standard | phrase. Note | that the |
| --- | --- | ----------------- | ------------ | ------------ | ------------ | -------- |
shorthandintro
alternativephrasemustincludetheshorthand.
| shortjournal | field(literal) |     |     |     |     | Labelfield |
| ------------ | -------------- | --- | --- | --- | --- | ---------- |
A short version or an acronym of the journaltitle. Not used by the standard
bibliographystyles.
| shortseries | field(literal) |     |     |     |     | Labelfield |
| ----------- | -------------- | --- | --- | --- | --- | ---------- |
Ashortversionoranacronymoftheseriesfield. Notusedbythestandardbiblio-
graphystyles.
25

shorttitle field(literal) Labelfield
Thetitleinanabridgedform. Thisfieldisusuallynotincludedinthebibliography.
Itisintendedforcitationsinauthor-titleformat. Ifpresent,theauthor-titlecitation
stylesusethisfieldinsteadoftitle.
subtitle field(literal)
Thesubtitleofthework.
title field(literal)
Thetitleofthework.
titleaddon field(literal)
Anannextothetitle,tobeprintedinadifferentfont.
translator list(name)
Thetranslator(s)ofthetitleorbooktitle,dependingontheentrytype. Ifthetrans-
latorisidenticaltotheeditor,thestandardstyleswillautomaticallyconcatenate
thesefieldsinthebibliography.
type field(key)
Thetypeofamanual,patent,report,orthesis. Thisfieldmayalsobeusefulfor
thecustomtypeslistedin§2.1.3.
url field(uri)
Theurlofanonlinepublication. IfitisnotURL-escaped(no‘%’chars)itwillbe
URI-escaped according to RFC 3987, that is, even Unicode chars will be correctly
escaped.
urldate field(date)
Theaccessdateoftheaddressspecifiedintheurlfield. Seealso§2.3.8.
venue field(literal)
Thelocationofaconference,asymposium,orsomeothereventin@proceedings
and@inproceedingsentries. Thisfieldmayalsobeusefulforthecustomtypeslisted
in § 2.1.3. Note that the location list holds the place of publication. It therefore
corresponds to the publisher and institution lists. The location of the event is
giveninthevenuefield. Seealsoeventdateandeventtitle.
version field(literal)
Therevisionnumberofapieceofsoftware,amanual,etc.
volume field(integer)
Thevolumeofamulti-volumebookoraperiodical. Itisexpectedtobeaninteger,not
necessarilyinarabicnumeralssincebiberwillautomaticallyconvertfromroman
numeralsorarabiclettertointegersinternallyforsortingpurposes. Seealsopart.
Seethenoromanoptionwhichcanbeusedtosuppressromannumeralparsing. This
canhelpincaseswherethereisanambiguitybetweenparsingasromannumerals
oralphanumeric(e.g. ‘C’),see§3.1.2.3.
26

volumes field(integer)
Thetotalnumberofvolumesofamulti-volumework. Dependingontheentrytype,
thisfieldreferstotitleormaintitle. Itisexpectedtobeaninteger,notnecessarily
in arabic numerals since biber will automatically convert from roman numerals
orarabiclettertointegersinternallyforsortingpurposes. Seethenoromanoption
whichcanbeusedtosuppressromannumeralparsing. Thiscanhelpincaseswhere
thereisanambiguitybetweenparsingasromannumeralsoralphanumeric(e.g. ‘C’),
see§3.1.2.3.
year field(literal)
Theyearofpublication. Thisfieldisaliteralfieldonlywhengivenexplicitlyinthe
data(forplainBibTeXcompatibilityforexample). Itishoweverbettertousethedate
fieldasthisiscompatiblewithplainyearstooandsupportsmanymorefeatures. See
§§2.3.8and2.3.9.
2.2.3 SpecialFields
Thefieldslistedinthissectiondonotholdprintabledatabutserveadifferentpurpose.
Theyapplytoallentrytypesinthedefaultdatamodel.
crossref field(entrykey)
Thisfieldholdsanentrykeyforthecross-referencingfeature. Childentrieswitha
crossreffieldinheritdatafromtheparententryspecifiedinthecrossreffield. If
thenumberofchildentriesreferencingaspecificparententryhitsacertainthreshold,
theparententryisautomaticallyaddedtothebibliographyevenifithasnotbeen
cited explicitly. The threshold is settable with the mincrossrefs package option
from§3.1.2.1. Styleauthorsshouldnotethatwhetherornotthecrossreffieldsof
thechildentriesaredefinedonthebiblatexleveldependsontheavailabilityofthe
parententry. Iftheparententryisavailable,thecrossreffieldsofthechildentries
willbedefined. Ifnot,thechildentriesstillinheritthedatafromtheparententry
buttheircrossreffieldswillbeundefined. Whethertheparententryisaddedto
thebibliographyimplicitlybecauseofthethresholdorexplicitlybecauseithasbeen
citeddoesnotmatter. Seealsothexreffieldinthissectionaswellas§2.4.1.
entryset field(separatedvalues)
Thisfieldisspecifictoentrysets. See§3.14.5fordetails. Thisfieldisconsumedby
thebackendprocessinganddoesnotappearinthe.bbl.
execute field(code)
AspecialfieldwhichholdsarbitraryTeXcodetobeexecutedwheneverthedataof
therespectiveentryisaccessed. Thismaybeusefultohandlespecialcases. Con-
ceptually,thisfieldiscomparabletothehooks\AtEveryBibitem,\AtEveryLositem,
and\AtEveryCitekeyfrom§4.10.6,exceptthatitisdefinableonaper-entrybasis
inthebibfile. Anycodeinthisfieldisexecutedautomaticallyimmediatelyafter
thesehooks.
gender field(Patternmatchingoneof: sf,sm,sn,pf,pm,pn,pp)
The gender of the author or the gender of the editor, if there is no author. The
following identifiers are supported: sf (feminine singular, a single female name),
27

sm (masculine singular, a single male name), sn (neuter singular, a single neuter
name),pf(feminineplural,alistoffemalenames),pm(masculineplural,alistofmale
names),pn(neuterplural,alistofneuternames),pp(plural,amixedgenderlistof
names). Thisinformationisonlyrequiredbyspecialbibliographyandcitationstyles
andonlyincertainlanguages. Forexample,acitationstylemayreplacerecurrent
authornameswithatermsuchas‘idem’. IftheLatinwordisused,asiscustomin
EnglishandFrench,thereisnoneedtospecifythegender. InGermanpublications,
however, such key terms are usually given in German and in this case they are
gender-sensitive.
langid field(identifier)
The language id of the bibliography entry. The alias hyphenation is provided for
backwards compatibility. The identifier must be a language name known to the
babel/polyglossiapackages. Thisinformationmaybeusedtoswitchhyphenation
patternsandlocalisestringsinthebibliography. Notethatthelanguagenamesare
casesensitive. Thelanguagescurrentlysupportedbythispackagearegivenintable2.
Note that babel treats the identifier english as an alias for british or american,
dependingonthebabelversion. Thebiblatexpackagealwaystreatsitasanalias
foramerican. Itispreferabletousethelanguageidentifiersamericanandbritish
(babel) or a language specific option to specify a language variant (polyglossia,
usingthelangidoptsfield)toavoidanypossibleconfusion. Comparelanguagein
§2.2.2.
langidopts field(literal)
Forpolyglossiausers,allowsper-entrylanguagespecificoptions. Theliteralvalue
ofthisfieldispassedtopolyglossia’slanguageswitchingfacilitywhenusingthe
packageoptionautolang=langname. Forexample,thefields:
langid = {english},
langidopts = {variant=british},
wouldwrapthebibliographyentryin:
\english[variant=british]
...
\endenglish
ids field(separatedlistofentrykeys)
Citationkeyaliasesforthemaincitationkey. Anentrymaybecitedbyanyofits
aliasesandbiblatexwilltreatthecitationasifithadusedtheprimarycitationkey.
Thisistoaiduserswhochangetheircitationkeysbuthavelegacydocumentswhich
useolderkeysforthesameentry. Thisfieldisconsumedbythebackendprocessing
anddoesnotappearinthe.bbl.
indexsorttitle field(literal)
Thetitleusedwhensortingtheindex. Incontrasttoindextitle,thisfieldisused
forsortingonly. Theprintedtitleintheindexistheindextitleorthetitlefield.
Thisfieldmaybeusefulifthetitlecontainsspecialcharactersorcommandswhich
interferewiththesortingoftheindex. Considerthisexample:
28

Table2:SupportedLanguages
| Language  | Region/Dialect                      | Identifiers |
| --------- | ----------------------------------- | ----------- |
| Basque    | France,Spain                        | basque      |
| Bulgarian | Bulgaria                            | bulgarian   |
| Catalan   | Spain,France,Andorra,Italy          | catalan     |
| Croatian  | Croatia,BosniaandHerzegovina,Serbia | croatian    |
| Czech     | CzechRepublic                       |             |
czech
| Danish  | Denmark       | danish                     |
| ------- | ------------- | -------------------------- |
| Dutch   | Netherlands   | dutch                      |
| English | USA           | american,USenglish,english |
|         | UnitedKingdom | british,UKenglish          |
Canada
canadian
|          | Australia     | australian |
| -------- | ------------- | ---------- |
|          | NewZealand    | newzealand |
| Estonian | Estonia       | estonian   |
| Finnish  | Finland       | finnish    |
| French   | France,Canada |            |
french
| German | Germany |     |
| ------ | ------- | --- |
german
|             | Austria     | austrian    |
| ----------- | ----------- | ----------- |
|             | Switzerland | swissgerman |
| German(new) | Germany     | ngerman     |
|             | Austria     | naustrian   |
Switzerland
nswissgerman
| Greek     | Greece  | greek            |
| --------- | ------- | ---------------- |
| Hungarian | Hungary | magyar,hungarian |
| Icelandic | Iceland | icelandic        |
| Italian   | Italy   | italian          |
| Latvian   | Latvia  |                  |
latvian
| Lithuanian         | Lithuania | lithuanian |
| ------------------ | --------- | ---------- |
| Marathi            | India     | marathi    |
| Norwegian(Bokmål)  | Norway    | norsk      |
| Norwegian(Nynorsk) | Norway    | nynorsk    |
| Polish             | Poland    |            |
polish
| Portuguese     | Brazil   | brazil              |
| -------------- | -------- | ------------------- |
|                | Portugal | portuguese,portuges |
| Romanian       | Romania  | romanian            |
| Russian        | Russia   | russian             |
| Serbian(Latin) | Serbia   |                     |
serbian
| Serbian(Cyrillic) | Serbia   | serbianc          |
| ----------------- | -------- | ----------------- |
| Slovak            | Slovakia | slovak            |
| Slovene           | Slovenia | slovene,slovenian |
| Spanish           | Spain    | spanish           |
| Swedish           | Sweden   | swedish           |
| Turkish           | Turkey   |                   |
turkish
| Ukrainian | Ukraine | ukrainian |
| --------- | ------- | --------- |
29

title = {The \LaTeX\ Companion},
indextitle = {\LaTeX\ Companion, The},
indexsorttitle = {LATEX Companion},
Styleauthorsshouldnotethatbiblatexautomaticallycopiesthevalueofeitherthe
indextitleorthetitlefieldtoindexsorttitleifthelatterfieldisundefined.
keywords field(separatedvalues)
A separated list of keywords. These keywords are intended for the bibliography
filters(see§§3.8.2and3.14.4),theyareusuallynotprinted. Notethatwiththedefault
separator(comma),spacesaroundtheseparatorareignored.
options field(separatedhkeyi=hvalueioptions)
A separated list of entry options in hkeyi=hvaluei notation. This field is used to
set options on a per-entry basis. See § 3.1.3 for details. Note that citation and
bibliographystylesmaydefineadditionalentryoptions.
presort field(string)
A special field used to modify the sorting order of the bibliography. This field is
thefirstitemthesortingroutineconsiderswhensortingthebibliography,henceit
may be used to arrange the entries in groups. This may be useful when creating
subdivided bibliographies with the bibliography filters. Please refer to § 3.6 for
furtherdetails. Alsosee§4.5.6. Thisfieldisconsumedbythebackendprocessing
anddoesnotappearinthe.bbl.
related field(separatedvalues)
Citationkeysofotherentrieswhichhavearelationshiptothisentry. Therelationship
isspecifiedbytherelatedtypefield. Pleasereferto§3.5forfurtherdetails.
relatedoptions field(separatedvalues)
Per-typeoptionstosetforarelatedentry. Notethatthisdoesnotsettheoptionson
therelatedentryitself,onlythedataonlyclonewhichisusedasadatasourcefor
theparententry.
relatedtype field(identifier)
Anidentifierwhichspecifiedthetypeofrelationshipforthekeyslistedintherelated
field. Theidentifierisalocalisedbibliographystringprintedbeforethedatafromthe
relatedentrylist. Itisalsousedtoidentifytype-specificformattingdirectivesand
bibliographymacrosfortherelatedentries. Pleasereferto§3.5forfurtherdetails.
relatedstring field(literal)
A field used to override the bibliography string specified by relatedtype. Please
referto§3.5forfurtherdetails.
sortkey field(literal)
Afieldusedtomodifythesortingorderofthebibliography. Thinkofthisfieldas
themastersortkey. Ifpresent,biblatexusesthisfieldduringsortingandignores
everythingelse,exceptforthepresortfield. Pleasereferto§3.6forfurtherdetails.
Thisfieldisconsumedbythebackendprocessinganddoesnotappearinthe.bbl.
30

sortname list(name)
Anameoralistofnamesusedtomodifythesortingorderofthebibliography. If
present,thislistisusedinsteadofauthororeditorwhensortingthebibliography.
Please refer to § 3.6 for further details. This field is consumed by the backend
processinganddoesnotappearinthe.bbl.
sortshorthand field(literal)
Similar to sortkey but used in the list of shorthands. If present, biblatex uses
thisfieldinsteadofshorthandwhensortingthelistofshorthands. Thisisusefulif
theshorthandfieldholdsshorthandswithformattingcommandssuchas\emphor
\textbf. Thisfieldisconsumedbythebackendprocessinganddoesnotappearin
the.bbl.
sorttitle field(literal)
A field used to modify the sorting order of the bibliography. If present, this field
is used instead of the title field when sorting the bibliography. The sorttitle
field may come in handy if you have an entry with a title like “An Introduction
to…”andwantthatalphabetizedunder‘I’ratherthan‘A’.Inthiscase,youcouldput
“Introduction to…” in the sorttitle field. Please refer to § 3.6 for further details.
Thisfieldisconsumedbythebackendprocessinganddoesnotappearinthe.bbl.
sortyear field(integer)
Afieldusedtomodifythesortingorderofthebibliography. Inthedefaultsorting
templates,ifthisfieldispresent,itisusedinsteadoftheyearfieldwhensortingthe
bibliography. Pleasereferto§3.6forfurtherdetails. Thisfieldisconsumedbythe
backendprocessinganddoesnotappearinthe.bbl.
xdata field(separatedlistofentrykeys)
Thisfieldinheritsdatafromoneormore@xdataentries. Conceptually,thexdata
field is related to crossref and xref: crossref establishes a logical parent/child
relationandinheritsdata;xrefestablishesaslogicalparent/childrelationwithout
inheritingdata;xdatainheritsdatawithoutestablishingarelation. Thevalueofthe
xdatamaybeasingleentrykeyoraseparatedlistofkeys. See§3.14.6forfurther
details. Thisfieldisconsumedbythebackendprocessinganddoesnotappearinthe
.bbl.
xref field(entrykey)
Thisfieldisanalternativecross-referencingmechanism. Itdiffersfromcrossrefin
thatthechildentrywillnotinheritanydatafromtheparententryspecifiedinthe
xreffield. Ifthenumberofchildentriesreferencingaspecificparententryhitsa
certainthreshold,theparententryisautomaticallyaddedtothebibliographyevenif
ithasnotbeencitedexplicitly. Thethresholdissettablewiththeminxrefspackage
optionfrom§3.1.2.1. Styleauthorsshouldnotethatwhetherornotthexreffields
ofthechildentriesaredefinedonthebiblatexleveldependsontheavailabilityof
theparententry. Iftheparententryisavailable,thexreffieldsofthechildentries
willbedefined. Ifnot,theirxreffieldswillbeundefined. Whethertheparententry
isaddedtothebibliographyimplicitlybecauseofthethresholdorexplicitlybecause
ithasbeenciteddoesnotmatter. Seealsothecrossreffieldinthissectionaswell
as§2.4.1.
31

2.2.4 CustomFields
Thefieldslistedinthissectionareintendedforspecialbibliographystyles. Theyare
notusedbythestandardbibliographystyles.
name[a–c] list(name)
Customlistsforspecialbibliographystyles. Notusedbythestandardbibliography
styles.
name[a–c]type field(key)
Similartoauthortypeandeditortypebutreferringtothefieldsname[a--c]. Not
usedbythestandardbibliographystyles.
list[a–f] list(literal)
Customlistsforspecialbibliographystyles. Notusedbythestandardbibliography
styles.
user[a–f] field(literal)
Customfieldsforspecialbibliographystyles. Notusedbythestandardbibliography
styles.
verb[a–c] field(verbatim)
Similartothecustomfieldsaboveexceptthattheseareverbatimfields. Notusedby
thestandardbibliographystyles.
2.2.5 FieldAliases
Thealiaseslistedinthissectionareprovidedforbackwardscompatibilitywithtradi-
tionalBibTeXandotherapplicationsbasedontraditionalBibTeXstyles. Notethat
thesealiasesareimmediatelyresolvedasthebibfileisprocessed. Allbibliography
andcitationstylesmustusethenamesofthefieldstheypointto,notthealias. Inbib
files,youmayuseeitherthealiasorthefieldnamebutnotbothatthesametime.
address list(literal)
Analiasforlocation,providedforBibTeXcompatibility. TraditionalBibTeXuses
the slightly misleading field name address for the place of publication, i.e., the
locationofthepublisher,whilebiblatexusesthegenericfieldnamelocation. See
§§2.2.2and2.3.4.
annote field(literal)
Analiasforannotation,providedforjurabibcompatibility. See§2.2.2.
archiveprefix field(literal)
Analiasforeprinttype,providedforarXivcompatibility. See§§2.2.2and3.14.7.
journal field(literal)
Analiasforjournaltitle,providedforBibTeXcompatibility. See§2.2.2.
key field(literal)
Analiasforsortkey,providedforBibTeXcompatibility. See§2.2.3.
32

pdf field(verbatim)
Analiasforfile,providedforJabRefcompatibility. See§2.2.2.
primaryclass field(literal)
Analiasforeprintclass,providedforarXivcompatibility. See§§2.2.2and3.14.7.
school list(literal)
Analiasforinstitution,providedforBibTeXcompatibility. Theinstitutionfield
isusedbytraditionalBibTeXfortechnicalreportswhereastheschoolfieldholds
theinstitutionassociatedwiththeses. Thebiblatexpackageemploysthegeneric
fieldnameinstitutioninbothcases. See§§2.2.2and2.3.4.
2.3 UsageNotes
Theentrytypesandfieldssupportedbythispackageshouldforthemostpartbe
intuitivetouseforanyonefamiliarwithBibTeX.However,apartfromtheadditional
typesandfieldsprovidedbythispackage,someofthefamiliaronesarehandledin
awaywhichisinneedofexplanation. Thispackageincludessomecompatibility
code for bib files which were generated with a traditional BibTeX style in mind.
Unfortunately, it is not possible to handle all legacy files automatically because
biblatex’sdatamodelisslightlydifferentfromtraditionalBibTeX.Therefore,such
bibfileswillmostlikelyrequireeditinginordertoworkproperlywiththispackage.
Insum,thefollowingitemsaredifferentfromtraditionalBibTeXstyles:
• Theentrytype@inbook. See§§2.1.1and2.3.1fordetails.
• Thefieldsinstitution,organization,andpublisheraswellasthealiases
addressandschool. See§§2.2.2,2.2.5,2.3.4fordetails.
• Thehandlingofcertaintypesoftitles. See§2.3.5fordetails.
• Thefieldseries. See§§2.2.2and2.3.7fordetails.
• Thefieldsyearandmonth. See§§2.2.2,2.3.8,2.3.9,2.3.10fordetails.
• Thefieldedition. See§2.2.2fordetails.
• Thefieldkey. See§2.3.2fordetails.
Usersofthejurabibpackageshouldnotethattheshortauthorfieldistreatedas
anamelistbybiblatex,see§2.3.3fordetails.
2.3.1 TheEntryType@inbook
Usethe@inbookentrytypeforaself-containedpartofabookwithitsowntitleonly.
It relates to @book just like @incollection relates to @collection. See § 2.3.5 for
examples. Ifyouwanttorefertoachapterorsectionofabook,simplyusethebook
type and add a chapter and/or pages field. Whether a bibliography should at all
includereferencestochaptersorsectionsiscontroversialbecauseachapterisnota
bibliographicentity.
33

2.3.2 MissingandOmissibleData
Thefieldsmarkedas‘required’in§2.1.1arenotstrictlyrequiredinallcases. The
bibliographystyleswhichcomewiththispackagecangetbywithaslittleasatitle
field for most entry types. A book published anonymously, a periodical without
anexpliciteditor,orasoftwaremanualwithoutanexplicitauthorshouldposeno
problem as far as the bibliography is concerned. Citation styles, however, may
havedifferentrequirements. Forexample,anauthor-yearcitationschemeobviously
requiresanauthor/editorandayearfield.
Youmaygenerallyusethelabelfieldtoprovideasubstituteforanymissingdata
requiredforcitations. Howthelabelfieldisemployeddependsonthecitationstyle.
Theauthor-yearcitationstyleswhichcomewiththispackageusethelabelfield
asafallbackifeithertheauthor/editorortheyearismissing. Thenumericstyles,
ontheotherhand,donotuseitatallsincethenumericschemeisindependentof
theavailabledata. Theauthor-titlestylesignoreitaswell,becausethebaretitleis
usuallysufficienttoformauniquecitationandatitleisexpectedtobeavailablein
anycase. Thelabelfieldmayalsobeusedtooverridethenon-numericportionof
theautomaticallygeneratedlabelalphafieldusedbyalphabeticcitationstyles. See
§4.2.4fordetails.
NotethattraditionalBibTeXstylessupportakeyfieldwhichisusedforalphabet-
izingifbothauthorandeditoraremissing. Thebiblatexpackagetreatskeyasan
aliasforsortkey. Inadditiontothat,itoffersveryfine-grainedsortingcontrols,see
§§2.2.3and3.6fordetails. Thenatbibpackageemploysthekeyfieldasafallback
labelforcitations. Usethelabelfieldinstead.
2.3.3 CorporateAuthorsandEditors
Corporateauthorsandeditorsaregivenintheauthororeditorfield,respectively.
Note that they must be wrapped in an extra pair of curly braces to prevent data
parsingfromtreatingthemaspersonalnameswhicharetobedissectedintotheir
components. Usetheshortauthorfieldifyouwanttogiveanabbreviatedformof
thenameoranacronymforuseincitations.
author = {{National Aeronautics and Space Administration}},
shortauthor = {NASA},
Thedefaultcitationstyleswillusetheshortnameinallcitationswhilethefullname
isprintedinthebibliography. Forcorporateeditors,usethecorrespondingfields
editor and shorteditor. Since all of these fields are treated as name lists, it is
possibletomixpersonalnamesandcorporatenames,providedthatthenamesofall
corporationsandinstitutionsarewrappedinbraces.
editor = {{National Aeronautics and Space Administration}
and Doe, John},
shorteditor = {NASA and Doe, John},
Users switching from the jurabib package to biblatex should note that the
shortauthorfieldistreatedasanamelist.
2.3.4 LiteralLists
Thefieldsinstitution,organization,publisher,andlocationareliterallistsin
terms of § 2.2. This also applies to origlocation, origpublisher and to the field
34

aliasesaddressandschool. Allofthesefieldsmaycontainalistofitemsseparated
bythekeyword‘and’. Iftheycontainaliteral‘and’,itmustbewrappedinbraces.
| publisher | = {William | Reid | {and} | Company}, |     |
| --------- | ---------- | ---- | ----- | --------- | --- |
institution = {Office of Information Management {and} Communications
,→
},
organization = {American Society for Photogrammetry {and} Remote
,→ Sensing
and
|     | American | Congress |     | on Surveying | {and} Mapping}, |
| --- | -------- | -------- | --- | ------------ | --------------- |
Notethedifferencebetweenaliteral‘{and}’andthelistseparator‘and’intheabove
| examples. Youmayalsowraptheentirenameinbraces: |             |      |     |            |     |
| ---------------------------------------------- | ----------- | ---- | --- | ---------- | --- |
| publisher                                      | = {{William | Reid | and | Company}}, |     |
institution = {{Office of Information Management and Communications}
,→
},
organization = {{American Society for Photogrammetry and Remote
,→ Sensing}
and
|     | {American |     | Congress | on Surveying | and Mapping}}, |
| --- | --------- | --- | -------- | ------------ | -------------- |
Legacyfileswhichhavenotbeenupdatedforusewithbiblatexwillstillworkif
thesefieldsdonotcontainaliteral‘and’. However,notethatyouwillmissouton
theadditionalfeaturesofliterallistsinthiscase,suchasconfigurableformatting
andautomatictruncation.
2.3.5 Titles
Thefollowingexamplesdemonstratehowtohandledifferenttypesoftitles. Let’s
startwithafive-volumeworkwhichisreferredtoasawhole:
@MvBook{works,
| author  | = {Shakespeare, |     | William}, |     |     |
| ------- | --------------- | --- | --------- | --- | --- |
| title   | = {Collected    |     | Works},   |     |     |
| volumes | = {5},          |     |           |     |     |
...
The individual volumes of a multi-volume work usually have a title of their own.
SupposethefourthvolumeoftheCollectedWorks includesShakespeare’ssonnets
andwearereferringtothisvolumeonly:
@Book{works:4,
| author    | = {Shakespeare, |     | William}, |     |     |
| --------- | --------------- | --- | --------- | --- | --- |
| maintitle | = {Collected    |     | Works},   |     |     |
| title     | = {Sonnets},    |     |           |     |     |
| volume    | = {4},          |     |           |     |     |
...
Iftheindividualvolumesdonothaveatitle,weputthemaintitleinthetitlefield
andincludeavolumenumber:
35

@Book{works:4,
| author | = {Shakespeare, | William}, |     |
| ------ | --------------- | --------- | --- |
| title  | = {Collected    | Works},   |     |
| volume | = {4},          |           |     |
...
Inthenextexample, wearereferringtoapartofavolume, butthispartisaself-
containedworkwithitsowntitle. Therespectivevolumealsohasatitleandthereis
stillthemaintitleoftheentireedition:
@InBook{lear,
| author     | = {Shakespeare, | William}, |     |
| ---------- | --------------- | --------- | --- |
| bookauthor | = {Shakespeare, | William}, |     |
| maintitle  | = {Collected    | Works},   |     |
| booktitle  | = {Tragedies},  |           |     |
| title      | = {King         | Lear},    |     |
| volume     | = {1},          |           |     |
| pages      | = {53-159},     |           |     |
...
SupposethefirstvolumeoftheCollectedWorks includesareprintedessaybyawell-
knownscholar. Thisisnottheusualintroductionbytheeditorbutaself-contained
| work. TheCollectedWorks |     | alsohaveaseparateeditor: |     |
| ----------------------- | --- | ------------------------ | --- |
@InBook{stage,
| author     | = {Expert,      | Edward},            |         |
| ---------- | --------------- | ------------------- | ------- |
| title      | = {Shakespeare  | and the Elizabethan | Stage}, |
| bookauthor | = {Shakespeare, | William},           |         |
| editor     | = {Bookmaker,   | Bernard},           |         |
| maintitle  | = {Collected    | Works},             |         |
| booktitle  | = {Tragedies},  |                     |         |
| volume     | = {1},          |                     |         |
| pages      | = {7-49},       |                     |         |
...
See§2.3.7forfurtherexamples.
2.3.6 EditorialRoles
The type of editorial role performed by an editor in one of the editor fields
(i.e., editor, editora, editorb, editorc) may be specified in the corresponding
editor...typefield. Thefollowingrolesaresupportedbydefault. Therole‘editor’
| isthedefault. | Inthiscase,theeditortypefieldisomissible. |     |     |
| ------------- | ----------------------------------------- | --- | --- |
editor Themaineditor. Thisisthemostgenericeditorialroleandthedefaultvalue.
compiler Similartoeditorbutusedifthetaskoftheeditorismainlycompiling.
founder Thefoundingeditorofaperiodicaloracomprehensivepublicationprojectsuchasa
‘CollectedWorks’editionoralong-runninglegalcommentary.
continuator Aneditorwhocontinuedtheworkofthefoundingeditor(founder)butwassubse-
quentlyreplacedbythecurrenteditor(editor).
36

redactor Asecondaryeditorwhosetaskisredactingthework.
reviser Asecondaryeditorwhosetaskisrevisingthework.
Asecondaryeditororaconsultanttotheeditor.
collaborator
organizer Similartoeditorbutusedifthetaskoftheeditorismainlyorganizing.
For example, if the task of the editor is compiling, you may indicate that in the
correspondingeditortypefield:
@Collection{...,
| editor     | = {Editor,    | Edward}, |
| ---------- | ------------- | -------- |
| editortype | = {compiler}, |          |
...
Theremayalsobesecondaryeditorsinadditiontothemaineditor:
@Book{...,
| author      | = {...},          |            |
| ----------- | ----------------- | ---------- |
| editor      | = {Editor,        | Edward},   |
| editora     | = {Redactor,      | Randolph}, |
| editoratype | = {redactor},     |            |
| editorb     | = {Consultant,    | Conrad},   |
| editorbtype | = {collaborator}, |            |
...
Periodicals or long-running publication projects may see several generations of
editors. For example, there may be a founding editor in addition to the current
editor:
@Book{...,
| author      | = {...},     |            |
| ----------- | ------------ | ---------- |
| editor      | = {Editor,   | Edward},   |
| editora     | = {Founder,  | Frederic}, |
| editoratype | = {founder}, |            |
...
Notethatonlytheeditorisconsideredincitationsandwhensortingthebibliography.
Ifanentryistypicallycitedbythefoundingeditor(andsortedaccordinglyinthe
bibliography),thefoundergoesintotheeditorfieldandthecurrenteditormoves
tooneoftheeditor...fields:
@Collection{...,
| editor     | = {Founder,  | Frederic}, |
| ---------- | ------------ | ---------- |
| editortype | = {founder}, |            |
| editora    | = {Editor,   | Edward},   |
...
Youmayaddmorerolesbyinitializinganddefininganewlocalisationkeywhose
namecorrespondstotheidentifierintheeditor...typefield. See§§3.10and4.9.1
fordetails.
37

2.3.7 PublicationandJournalSeries
TheseriesfieldisusedbytraditionalBibTeXstylesbothforthemaintitleofamulti-
volumeworkandforapublicationseries,i.e.,alooselyrelatedsequenceofbooksby
thesamepublisherwhichdealwiththesamegeneraltopicorbelongtothesame
fieldofresearch. Thismaybeambiguous. Thispackageintroducesamaintitlefield
formulti-volumeworksandemploysseriesforpublicationseriesonly. Thevolume
ornumberofabookintheseriesgoesinthenumberfieldinthiscase:
@Book{...,
| author | = {Expert,     | Edward},   |                 |             |
| ------ | -------------- | ---------- | --------------- | ----------- |
| title  | = {Shakespeare | and        | the Elizabethan | Age},       |
| series | = {Studies     | in English | Literature      | and Drama}, |
| number | = {57},        |            |                 |             |
...
The@articleentrytypemakesuseoftheseriesfieldaswell,buthandlesitina
specialway. First,atestisperformedtodeterminewhetherthevalueofthefieldis
aninteger. Ifso,itwillbeprintedasanordinal. Ifnot,anothertestisperformedto
determinewhetheritisalocalisationkey. Ifso,thelocalisedstringisprinted. Ifnot,
thevalueisprintedasis. Considerthefollowingexampleofajournalpublishedin
numberedseries:
@Article{...,
| journal | = {Journal | Name}, |     |     |
| ------- | ---------- | ------ | --- | --- |
| series  | = {3},     |        |     |     |
| volume  | = {15},    |        |     |     |
| number  | = {7},     |        |     |     |
| year    | = {1995},  |        |     |     |
...
This entry will be printed as “Journal Name. 3rd ser. 15.7 (1995)”. Some journals
use designations such as “old series” and “new series” instead of a number. Such
designationsmaybegivenintheseriesfieldaswell,eitherasaliteralstringorasa
localisationkey. Considerthefollowingexamplewhichmakesuseofthelocalisation
keynewseries:
@Article{...,
| journal | = {Journal     | Name}, |     |     |
| ------- | -------------- | ------ | --- | --- |
| series  | = {newseries}, |        |     |     |
| volume  | = {9},         |        |     |     |
| year    | = {1998},      |        |     |     |
...
Thisentrywillbeprintedas“JournalName. Newser. 9(1998)”. See§4.9.2foralist
oflocalisationkeysdefinedbydefault.
2.3.8 DateandTimeSpecifications
Date fields such as the default data model dates date, origdate, eventdate, and
urldateadheretoiso8601-2ExtendedFormatspecificationlevel1. Inadditionto
theiso8601-2emptydaterangemarkers,youmayalsospecifyanopenended/start
38

Table3:DateSpecifications
| DateSpecification | FormattedDate(Examples) |                    |
| ----------------- | ----------------------- | ------------------ |
|                   | Short/12-hourFormat     | Long/24-hourFormat |
| 1850              | 1850                    | 1850               |
| 1997/             | 1997–                   | 1997–              |
|                   | –1997                   | –1997              |
/1997
| 1997/..    | 1997–      | 1997–           |
| ---------- | ---------- | --------------- |
| ../1997    | –1997      | –1997           |
| 1967-02    | 02/1967    | February1967    |
| 2009-01-31 | 31/01/2009 | 31stJanuary2009 |
|            | 1988–1992  | 1988–1992       |
1988/1992
| 2002-01/2002-02       | 01/2002–02/2002       | January2002–February2002   |
| --------------------- | --------------------- | -------------------------- |
| 1995-03-30/1995-04-05 | 30/03/1995–05/04/1995 | 30thMarch1995–5thApril1995 |
| 2004-04-05T14:34:00   | 05/04/20042:34PM      | 5thApril200414:34:00       |
daterangebygivingtherangeseparatorandomittingtheend/startdate(e.g.,YYYY/,
/YYYY).Seetable3forsomeexamplesofvaliddatespecificationsandtheformatted
datesautomaticallygeneratedbybiblatex. Theformatteddateislanguagespecific
andwillbeadaptedautomatically. Ifthereisnodatefieldinanentry,biblatexwill
alsoconsiderthefieldsyearandmonthforbackwardscompatibilitywithtraditional
BibTeXbutthisisnotencouragedasexplicityearandmontharenotparsedfordate
meta-informationmarkersortimesandareusedas-is. Styleauthorsshouldnote
thatdatefieldslikedateororigdateareonlyavailableinthebibfile. Alldatesare
parsedanddissectedintotheircomponentsasthebibfileisprocessed. Thedateand
timecomponentsaremadeavailabletostylesbywayofthespecialfieldsdiscussed
in§4.2.4.3. Seethissectionandtable10onpage173forfurtherinformation.
iso8601-2ExtendedFormatdatesareastronomicaldatesinwhichyear‘0’exists.
WhenoutputtingdatesinBCEorBCera(seethedateeraoptionbelow),notethat
theywilltypicallybeoneyearearliersinceBCE/BCeradonothaveayear0(year0
| is1BCE/BC).Thisconversionisautomatic. |     | Seeexamplesintable5. |
| ------------------------------------- | --- | -------------------- |
Datefieldnamesmust endwiththestring‘date’,aswiththedefaultdatefields.
Bearthisinmindwhenaddingnewdatefieldstothedatamodel(see§4.5.4).
biblatex
willcheckalldatefieldsafterreadingthedatamodelandwillexitwithanerrorifit
findsadatefieldwhichdoesnotadheretothisnamingconvention.
iso8601-2 supports dates before common era (BCE/BC) by way of a negative
date format and supports ‘approximate’ (circa) and uncertain dates. Such date
formatssetinternalmarkerswhichcanbetestedforsothatappropriatelocalised
markers(suchascircaorbeforecommonera)canbeinserted. Alsosupportedare
‘unspecified’dates(iso8601-24.3)whichareautomaticallyexpandedintoappropriate
datarangesaccompaniedbyafield<datetype>dateunspecifiedwhichdetailsthe
granularity of the unspecified data. Styles may use this information to format
such dates appropriately but the standard styles do not do this. See table 4 on
page40fortheallowediso8601-2‘unspecified’formats,theirrangeexpansionsand
<datetype>dateunspecifiedvalues(see§4.2.4.1).
Table5showsformatswhichuseappropriatetestsandformatting. Seethedate
meta-informationtestsin§4.6.2andthelocalisationstringsin§4.9.2.21. Seealso
the96-dates.texexamplefileforcompleteexamplesofthetestsandlocalisation
stringsuse.
Theoutputof‘circa’,uncertaintyanderainformationinstandardstyles(orcustom
styles not customising the internal \mkdaterange* macros) is controlled by the
39

Table4:ISO8601-24.3UnspecifiedDateParsing
DateSpecification ExpandedRange Meta-information
199X 1990/1999 yearindecade
19XX 1900/1999 yearincentury
1999-XX 1999-01/1999-12 monthinyear
1999-01-XX 1999-01-01/1999-01-31 dayinmonth
1999-XX-XX 1999-01-01/1999-12-31 dayinyear
packageoptionsdatecirca,dateuncertain,dateeraanddateeraauto(see§3.1.2.1).
Seetable5onpage41forexampleswhichassumestheseoptionsareallused.
2.3.9 Year,MonthandDate
The fields year and month are still supported by biblatex, but the full set of date
features(dayandtimeprecision,ranges,…)canonlybeusedwithdate. Itistherefore
recommendedtopreferdateoveryearandmonthunlessbackwardscompatibility
ofthebibfilewithclassicalBibTeXisrequired.
2.3.10 MonthsandJournalIssues
Themonthfieldisanintegerfield. Thebibliographystyleconvertsthemonthtoa
language-dependentstringasrequired. Forbackwardscompatibility,youmayalso
usethefollowingthree-letterabbreviationsinthemonthfield: jan,feb,mar,apr,may,
jun,jul,aug,sep,oct,nov,dec. NotethattheseabbreviationsareBibTeXstrings
which must be given without any braces or quotes. When using them, don’t say
month={jan}ormonth="jan"butmonth=jan. Itisnotpossibletospecifyamonth
suchasmonth={8/9}. Usethedatefieldfordaterangesinstead. Quarterlyjournals
aretypicallyidentifiedbyadesignationsuchas‘Spring’or‘Summer’whichshould
begivenintheissuefield. Theplacementoftheissuefieldin@articleentriesis
similartoandoverridesthemonthfield.
2.3.11 JournalNumbersandIssues
Theterms‘number’,‘issue’andeven‘issuenumber’areoftenusedsynonymouslyby
journalstorefertothesubdvisionofavolume. Thefactthatbiblatex’sdatamodel
hasfieldsofbothnamescansometimesleadtoconfusionaboutwhichfieldshould
beused. Firstandforemostthewordthatthejournalusesforthesubdivsionofa
volumeshouldbeofminorimportance,whatmattersistheroleinthedatamodel.
Asaruleofthumbnumberistherightfieldinmostcircumstances. Inthestandard
stylesnumbermodifiesvolume,whereasissuemodifiesthedate(year)oftheentry.
Numericidentifiersandshortdesignatorsthatarenotnecessarily(entirely)numeric
suchas‘A’,‘S1’,‘C2’,‘Suppl.3’,‘4es’wouldgointothenumberfield,becausethey
usuallymodifythevolume. Theoutputof—especiallylonger—non-numericinputfor
numbershouldbecheckedsinceitcouldpotentiallylookoddwithsomestyles. The
fieldissuecanbeusedfordesignationssuchas‘Spring’,‘Winter’or‘Michaelmas
term’ifthatiscommonlyusedtorefertothejournal.
The‘articlenumber’or‘papernumber’,whichcanbeusedinsteadof—oralong
with—apagerangetopinpointaspecificarticlewithinanotherwork,goesintothe
eidfield,whoseplacementinthestandardstylesissimilartotheanalogouspages
field.
40

Table5:EnhancedDateSpecifications
| DateSpecification | FormattedDate(Examples) |                                                 |
| ----------------- | ----------------------- | ----------------------------------------------- |
|                   | OutputFormat            | OutputFormatNotes                               |
| 0000              | 1BC                     | dateera=christianprintsbeforechristlocalisation |
-0876 877BCE dateera=secular prints beforecommonera localisation
string
-0877/-0866 878BC–867BC using \ifdateera test and beforechrist localisation
string
0768 0768CE usingdateeraautosetto‘1000’andcommoneralocalisation
string
344-02BCE
-0343-02
| 0343-02-03 | 343-02-03CE | withdateeraauto=400                                |
| ---------- | ----------- | -------------------------------------------------- |
| 0343-02-03 | 343-02-02CE | withdateeraauto=400andjulian                       |
| 1723~      | circa1723   | using\ifdatecircatest                              |
| 1723?      | 1723?       | using\ifdateuncertaintest                          |
| 1723%      | circa1723?  | using\ifdateuncertainand\ifdatecircatests          |
|            | 2004        | also,yeardivisionissettothelocalisationstring‘sum- |
2004-22
mer’
2004-24 2004 also,yeardivisionissettothelocalisationstring‘winter’
2.3.12 Pagination
Whenspecifyingapageorpagerange,eitherinthepagesfieldofanentryorinthe
hpostnoteiargumenttoacitationcommand,itisconvenienttohavebiblatexadd
prefixeslike‘p.’ or‘pp.’ automaticallyandthisisindeedwhatthispackagedoesby
default. However,someworksmayuseadifferentpaginationschemeormaynotbe
citedbypagebutratherbyverseorlinenumber. Thisiswhenthepaginationand
bookpaginationfieldscomeintoplay. Asanexample,considerthefollowingentry:
@InBook{key,
| title          | = {...},    |     |
| -------------- | ----------- | --- |
| pagination     | = {verse},  |     |
| booktitle      | = {...},    |     |
| bookpagination | = {page},   |     |
| pages          | = {53--65}, |     |
...
Thebookpaginationfieldaffectstheformattingofthepagesandpagetotalfields
inthelistofreferences. Sincepageisthedefault,thisfieldisomissibleintheabove
example. Inthiscase,thepagerangewillbeformattedas‘pp.53–65’. Supposethat,
whenquotingfromthiswork,itiscustomarytouseversenumbersratherthanpage
numbers in citations. This is reflected by the pagination field, which affects the
formattingofthehpostnoteiargumenttoanycitationcommand. Withacitationlike
\cite[17]{key},thepostnotewillbeformattedas‘v.17’. Settingthepagination
fieldtosectionwouldyield‘§17’. See§3.15.3forfurtherusageinstructions.
Thepaginationandbookpaginationfieldsarekeyfields. Thispackagewilltry
tousetheirvalueasalocalisationkey,providedthatthekeyisdefined. Alwaysuse
thesingularformofthekeynameinbibfiles,thepluralisformedautomatically.
Thekeyspage, column, line, verse, section, andparagrapharepredefined, with
being the default. The string ‘none’ has a special meaning when used in a
page
paginationorbookpaginationfield. Itsuppressestheprefixfortherespectiveentry.
Iftherearenopredefinedlocalisationkeysforthepaginationschemerequiredbya
certainentry,youcansimplyaddthem. Seethecommands\NewBibliographyString
41

and \DefineBibliographyStrings in § 3.10. You need to define two localisation
stringsforeachadditionalpaginationscheme: thesingularform(whoselocalisation
keycorrespondstothevalueofthepaginationfield)andthepluralform(whose
localisationkeymustbethesingularplustheletter‘s’). Seethepredefinedkeysin
§4.9.2forexamples.
2.4 HintsandCaveats
This section provides some additional hints concerning the data interface of this
| package. Italsoaddressessomecommonproblems. |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- |
2.4.1 Cross-referencing
biberfeaturesahighlycustomizablecross-referencingmechanismwithflexibledata
inheritance rules. Duplicating certain fields in the parent entry or adding empty
fieldstothechildentryisnolongerrequired. Entriesarespecifiedinanaturalway:
@Book{book,
| author    | = {Author},       |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- |
| title     | = {Booktitle},    |     |     |     |     |
| subtitle  | = {Booksubtitle}, |     |     |     |     |
| publisher | = {Publisher},    |     |     |     |     |
| location  | = {Location},     |     |     |     |     |
| date      | = {1995},         |     |     |     |     |
}
@InBook{inbook,
| crossref | = {book},  |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- |
| title    | = {Title}, |     |     |     |     |
| pages    | = {5--25}, |     |     |     |     |
}
The title field of the parent will be copied to the booktitle field of the child,
| the      | becomes | the booksubtitle. | The    | of the parent | becomes the |
| -------- | ------- | ----------------- | ------ | ------------- | ----------- |
| subtitle |         |                   | author |               |             |
bookauthorofthechildand,sincethechilddoesnotprovideanauthorfield,itis
alsoduplicatedastheauthorofthechild. Afterdatainheritance,thechildentryis
similartothis:
| author       | = {Author},       |     |     |     |     |
| ------------ | ----------------- | --- | --- | --- | --- |
| bookauthor   | = {Author},       |     |     |     |     |
| title        | = {Title},        |     |     |     |     |
| booktitle    | = {Booktitle},    |     |     |     |     |
| booksubtitle | = {Booksubtitle}, |     |     |     |     |
| publisher    | = {Publisher},    |     |     |     |     |
| location     | = {Location},     |     |     |     |     |
| date         | = {1995},         |     |     |     |     |
| pages        | = {5--25},        |     |     |     |     |
SeeappendixBforalistofmappingrulessetupbydefault. Notethatallofthisis
customizable. See§4.5.12onhowtoconfigurebiber’scross-referencingmechanism.
Seealso§2.2.3.
42

2.4.1.1 Thexreffield
Inadditiontothecrossreffield,biblatexsupportsasimplifiedcross-referencing
mechanismbasedonthexreffield. Thisisusefulifyouwanttoestablishaparent/
childrelationbetweentwoassociatedentriesbutprefertokeepthemindependent
asfarasthedataisconcerned. Thexreffielddiffersfromcrossrefinthatthechild
entrywillnotinheritanydatafromtheparent. Iftheparentisreferencedbyacertain
numberofchildentries,biblatexwillautomaticallyaddittothebibliography. The
threshold is controlled by the minxrefs package option from § 3.1.2.1.u See also
§2.2.3.
2.4.2 SortingandEncodingIssues
biberhandlesus-ascii,8-bitencodingssuchasLatin1,andutf-8. Itfeaturestrue
Unicodesupportandiscapableofreencodingthebibdataontheflyinarobustway.
Forsorting,biberusesaPerlimplementationoftheUnicodeCollationAlgorithm
(uca),asoutlinedinUnicodeTechnicalStandard#10.13 Collationtailoringbasedon
theUnicodeCommonLocaleDataRepository(cldr)isalsosupported.14
SupportingUnicodeimpliesmuchmorethanhandlingutf-8input. Unicodeis
a complex standard covering more than its most well-known parts, the Unicode
character encoding and transport encodings such as utf-8. It also standardizes
aspectssuchasstringcollation,whichisrequiredforlanguage-sensitivesorting. For
example,byusingtheUnicodeCollationAlgorithm,bibercanhandlethecharacter
‘ß’withoutanymanualintervention. Allyouneedtodotogetlocalisedsortingis
specifythelocale:
\usepackage[sortlocale=de]{biblatex}
orifyouareusingGermanasthemaindocumentlanguageviababelorpolyglossia:
\usepackage[sortlocale=auto]{biblatex}
Thiswillmakebiblatexpassthebabel/polyglossiamaindocumentlanguageas
the locale which biber will map into a suitable default locale. biber will not try
togetlocaleinformationfromitsenvironmentasthismakesdocumentprocessing
dependentonsomethingnotinthedocumentwhichisagainstTeX’sspiritofrepro-
ducibility. Thisalsomakessensesincebabel/polyglossiaareinfacttherelevant
environmentforadocument. Notethatthiswillalsoworkwith8-bitencodingssuch
asLatin9,i.e.,youcantakeadvantageofUnicode-basedsortingeventhoughyou
arenotusingutf-8input. See§2.4.2.1onhowtospecifyinputanddataencodings
properly.
2.4.2.1 SpecifyingEncodings
Whenusinganon-us-asciiencodinginthebibfile,itisimportanttounderstand
what biblatex can do for you and what may require manual intervention. The
packagetakescareoftheLaTeXside,i.e.,itensuresthatthedataimportedfromthe
bblfileisinterpretedcorrectly,providedthatthebibencodingpackageoption(orthe
datasourcespecificoverrideforthis,see§3.8.1)issetproperly. Allofthisishandled
13https://unicode.org/reports/tr10/
14http://cldr.unicode.org/
43

automatically and no further steps, apart from setting the bibencoding option in
certaincases(namelywhentheencodingofthebibfilediffersfromtheencodingof
thetexfile),arerequiredprovidedthatyousetupyourdocumentencoding(i.e.,load
inputencorrelatedpackagesifrequired)before biblatexisloaded. Hereareafew
typicalusagescenariosalongwiththerelevantlinesfromthedocumentpreamble:
• us-asciinotationinboththetexandthebibfilewithpdfTeXortraditional
TeX:
\usepackage{biblatex}
• Latin1encoding(iso-8859-1)inthetexfile,us-asciinotationinthebibfile
withpdfTeXortraditionalTeX:
\usepackage[latin1]{inputenc}
\usepackage[bibencoding=ascii]{biblatex}
• Latin9encoding(iso-8859-15)inboththetexandthebibfilewithpdfTeXor
traditional:
\usepackage[latin9]{inputenc}
\usepackage[bibencoding=auto]{biblatex}
Since bibencoding=auto is the default setting, the option is omissible. The
followingsetupwillhavethesameeffect:
\usepackage[latin9]{inputenc}
\usepackage{biblatex}
• utf-8encodinginthetexfile,Latin1(iso-8859-1)inthebibfilewithpdfTeX
ortraditionalTeX:
\usepackage[utf8]{inputenc}
\usepackage[bibencoding=latin1]{biblatex}
ThesamescenariowithLaTeXrelease2018-04-01orabove,XeTeXorLuaTeX
innativeutf-8mode:
\usepackage[bibencoding=latin1]{biblatex}
bibercanhandleus-asciinotation,8-bitencodingssuchasLatin1,andutf-8. It
isalsocapableofreencodingthebibdataonthefly(replacingthelimitedmacro-
levelreencodingfeatureofbiblatex). Thiswillhappenautomaticallyifrequired,
providedthatyouspecifytheencodingofthebibfilesproperly. Inadditiontothe
scenariosdiscussedabove,bibercanalsohandlethefollowingcases:
• Transparentutf-8workflow,i.e.,utf-8encodinginboththetexandthebib
filewithpdfTeXortraditionalTeX:
44

\usepackage[utf8]{inputenc}
\usepackage[bibencoding=auto]{biblatex}
Sincebibencoding=autoisthedefaultsetting,theoptionisomissible:
\usepackage[utf8]{inputenc}
\usepackage{biblatex}
ThesamescenariowithXeTeXorLuaTeXinnativeutf-8mode:
\usepackage{biblatex}
• Itisevenpossibletocombinean8-bitencodedtexfilewithutf-8encoding
inthebibfile,providedthatallcharactersinthebibfilearealsocoveredby
theselected8-bitencoding:
\usepackage[latin1]{inputenc}
\usepackage[bibencoding=utf8]{biblatex}
SomeworkaroundsmayberequiredwhenusingtraditionalTeXorpdfTeXwith
utf-8 encoding because inputenc’s utf8 module does not cover all of Unicode.
Roughlyspeaking,itonlycoverstheWesternEuropeanUnicoderange. Whenloading
inputencwiththeutf8option,biblatexwillnormallyinstructbibertoreencode
thebibdatatoutf-8. Thismayleadtoinputencerrorsifsomeofthecharactersin
thebibfileareoutsidethelimitedUnicoderangesupportedbyinputenc.
• Ifyouareaffectedbythisproblem,trysettingthesafeinputencoption:
\usepackage[utf8]{inputenc}
\usepackage[safeinputenc]{biblatex}
If this option is enabled, biblatex will ignore inputenc’s utf8 option and
use us-ascii. biber will then try to convert the bib data to us-ascii nota-
tion. For example, it will convert S̨ to \k{S}. This option is similar to set-
ting texencoding=ascii but will only take effect in this specific scenario
(inputenc/inputenxwithutf-8). Thisworkaroundtakesadvantageofthefact
thatbothUnicodeandtheutf-8transportencodingarebackwardscompatible
withus-ascii.
Thissolutionmaybeacceptableasaworkaroundifthedatainthebibfileismostly
us-ascii anyway, with only a few strings, such as some authors’ names, causing
problems. However,keepinmindthatitwillnotmagicallymaketraditionalTeXor
pdfTeXsupportUnicode. Itmayhelpiftheoccasionaloddcharacterisnotsupported
by inputenc, but may still be processed by TeX when using an accent command
(e.g.,\d{S}insteadofṢ).IfyouneedfullUnicodesupport,however,switchtoXeTeX
orLuaTeX.
TypicalerrorswheninputenccannothandleacertainUTF-8characterare:
45

| ! Package  | inputenc Error: | Unicode | char <char> | (U+<codepoint>) |     |
| ---------- | --------------- | ------- | ----------- | --------------- | --- |
| (inputenc) |                 | not set | up for use  | with LaTeX.     |     |
butalsolessobviousthingslike:
| ! Argument | of \UTFviii@three@octets |     | has an | extra }. |     |
| ---------- | ------------------------ | --- | ------ | -------- | --- |
| 3 User     | Guide                    |     |        |          |     |
Thispartofthemanualdocumentstheuserinterfaceofthebiblatexpackage. The
userguidecoverseverythingyouneedtoknowinordertousebiblatexwiththe
defaultstylesthatcomewiththispackage. Youshouldreadtheuserguidefirstin
anycase. Ifyouwanttowriteyourowncitationand/orbibliographystyles,continue
withtheauthorguideafterwards.
3.1 PackageOptions
Allpackageoptionsaregiveninhkeyi=hvalueinotation. Thevaluetrueisomissible
withallbooleankeys. Forexample,givingsortciteswithoutavalueisequivalent
tosortcites=true.
3.1.1 Load-timeOptions
The following options must be used as biblatex is loaded, i.e., in the optional
argumentto\usepackage.
| backend=bibtex,bibtex8,biber |     |                                   |     |     | default:biber |
| ---------------------------- | --- | --------------------------------- | --- | --- | ------------- |
| Specifiesthedatabasebackend. |     | Thefollowingbackendsaresupported: |     |     |               |
biber biber,thedefaultbackendofbiblatex,supportsus-ascii,8-biten-
|     | codings,   | utf-8, on-the-fly | reencoding,     | locale-specific         | sorting, and |
| --- | ---------- | ----------------- | --------------- | ----------------------- | ------------ |
|     | many other | features.         | Locale-specific | sorting, case-sensitive | sort-        |
ing,andupper/lowercaseprecedencearecontrolledbytheoptions
sortlocale,sortcase,andsortupper,respectively.
bibtex LegacyBibTeX.TraditionalBibTeXsupportsus-asciiencodingonly.
Sortingisalwayscase-insensitive.
bibtex8,the8-bitimplementationofBibTeX,supportsus-asciiand
bibtex8
8-bitencodingssuchasLatin1.
See§3.16fordetailsofusingBibTeXasabackend.
| style=hfilei |     |     |     |     | default:numeric |
| ------------ | --- | --- | --- | --- | --------------- |
Loadsthebibliographystylehfilei.bbxandthecitationstylehfilei.cbx. See§3.3for
anoverviewofthestandardstyles.
bibstyle=hfilei default:numeric
Loadsthebibliographystylehfilei.bbx. See§3.3.2foranoverviewofthestandard
bibliographystyles.
citestyle=hfilei default:numeric
Loadsthecitationstylehfilei.cbx. See§3.3.1foranoverviewofthestandardcitation
styles.
46

datamodel=hfilei
Loadsthedatamodelhfilei.dbx. Notethat.dbxfilescorrespondingtothestyleor
bibstyle/citestyleareloadedautomaticallyifavailableunlessthisoptionspecifies
anotherfile. See§4.5.4formoredetails.
natbib=true,false default:false
Loadscompatibilitymodulewhichprovidesaliasesforthecitationcommandsofthe
natbibpackage. See§3.9.9fordetails.
mcite=true,false default:false
Loadsacitationmodulewhichprovidesmcite/mciteplus-likecitationcommands.
See§3.9.10fordetails.
casechanger=auto,latex2e,expl3 default:auto
Thisoptionselectstheimplementationofbiblatex’scasechangingfunctions,most
prominently\MakeSentenceCase*. expl3selectsthenewimplementationbasedon
theLaTeX3modulel3text. Notethatthel3textmoduleassumesutf-8inputand
thatyourexpl3versionshouldbenewenough(atleastversion2020-04-06). latex2e
selectstheoriginalimplementation,whichhastrickybraceprotectionbehaviourand
someshortcomingswhendealingwithnon-us-asciicharacters. Thedefaultauto
selectsthecasechangingcodebasedontheavailableexpl3versionanddetected
documentencoding(expl3isselectedifexpl3isatleastversion2020-04-06andthe
documentencodingisdetectedasutf-8).
3.1.2 PreambleOptions
3.1.2.1 General
Thefollowingoptionsmaybeusedintheoptionalargumentto\usepackageaswell
as in the configuration file and the document preamble. The default value listed
totherightisthepackagedefault. Notethatbibliographyandcitationstylesmay
modifythedefaultsettingatloadtime,see§3.3fordetails.
sorting=nty,ntd,nyt,ndt,nyvt,ndvt,anyt,andt,anyvt,andvt,ynt,dnt, default:nty
ydnt,ddnt,none,count,debug,hnamei
Thesortingorderofthebibliography. Unlessstatedotherwise,theentriesaresorted
inascendingorder. Thefollowingchoicesareavailablebydefault:
nty Sortbyname,title,year.
ntd Sortbyname,title,fulldate.
nyt Sortbyname,year,title.
ndt Sortbyname,fulldate,title.
nyvt Sortbyname,year,volume,title.
ndvt Sortbyname,fulldate,volume,title.
anyt Sortbyalphabeticlabel,name,year,title.
andt Sortbyalphabeticlabel,name,fulldate,title.
anyvt Sortbyalphabeticlabel,name,year,volume,title.
andvt Sortbyalphabeticlabel,name,fulldate,volume,title.
47

ynt Sortbyyear,name,title.
dnt Sortbyfulldate,name,title.
ydnt Sortbyyear(descending),name,title.
ddnt Sortbyfulldate(descending),name,title.
none Donotsortatall. Allentriesareprocessedincitationorder.
count Sortindescendingorderofnumberoftimescited
debug Sortbyentrykey. Thisisintendedfordebuggingonly.
hnamei Usehnamei,asdefinedwith\DeclareSortingTemplate(§4.5.6)
Using any of the ‘alphabetic’ sorting templates only makes sense in conjunction
with a bibliography style which prints the corresponding labels. Note that some
bibliographystylesinitializethispackageoptiontoavaluedifferentfromthepackage
default(nty). See§3.3.2fordetails. Pleasereferto§3.6foranin-depthexplanation
oftheabovesortingoptionsaswellasthefieldsconsideredinthesortingprocess.
Seealso§4.5.6onhowtoadaptthepredefinedtemplatesordefinenewones.
sortcase=true,false default:true
Whetherornottosortthebibliographyandthelistofshorthandscase-sensitively.
sortupper=true,false default:true
Thisoptioncorrespondstobiber’s--sortuppercommand-lineoption. Ifenabled,
thebibliographyissortedin‘uppercasebeforelowercase’order. Disablingthisoption
means‘lowercasebeforeuppercase’order.
sortlocale=auto,hlocalei default:auto
This option sets the global sorting locale. Every sorting template inherits this lo-
caleifnoneisspecifiedusingthehlocaleioptionto\printbibliography. Setting
this to auto requests that it be set to the babel/polyglossia main document lan-
guage identifier, if these packages are used and en_US otherwise. biber will map
babel/polyglossialanguageidentifiersintosensiblelocaleidentifiers(seethebiber
documentation). You can therefore specify either a normal locale identifier like
de_DE_phonebook,es_ESoroneofthesupportedbabel/polyglossialanguageiden-
tifiersifthemappingbibermakesofthisisfineforyou.
sortcites=true,false default:false
Whether or not to sort citations if multiple entry keys are passed to a citation
command. If this option is enabled, citations are sorted according to the current
bibliography context sorting template (see § 3.8.10). This feature works with all
citationstyles.
sortsets=true,false default:false
Whetherornottosortsetmembersaccordingtotheactivereferencecontextsorting
scheme. Bydefaultthisisfalseandsetmembersappearintheordergiveninthe
datasource.
pluralothers=true,false default:false
Controlswhetherthelocalised‘andothers’string(e.g. ‘etal’)isforcedtobeplural.
Iftrue,itwillonlybeprintedinplaceoftwoormorenamesandifthereisonlyone
nameitwouldreplace,thenameitselfisprintedinstead. Defaultstofalse.
48

maxnames=hintegeri default:3
Athresholdaffectingalllistsofnames(author,editor,etc.). Ifalistexceedsthis
threshold,i.e.,ifitholdsmorethanhintegerinames,itisautomaticallytruncated
accordingtothesettingoftheminnamesoption. maxnamesisthemasteroptionwhich
setsmaxbibnames,maxcitenamesandmaxsortnames. Notethattheuniquelistfea-
turecanlocallyoverridemaxnames,seethedocumentationoftheuniquelistoption
in§3.1.2.3and§4.11.4.
minnames=hintegeri default:1
A limit affecting all lists of names (author, editor, etc.). If a list holds more
thanhmaxnamesinames,itisautomaticallytruncatedtohminnamesinames. The
hminnamesi value must be smaller than or equal to hmaxnamesi. minnames is the
masteroptionwhichsetsbothminbibnamesandmincitenames. Likemaxnamesthe
valueofminnamescanbeoverriddenbyuniquelist.
maxbibnames=hintegeri default:hmaxnamesi
Similartomaxnamesbutaffectsonlythebibliography.
minbibnames=hintegeri default:hminnamesi
Similartominnamesbutaffectsonlythebibliography.
maxcitenames=hintegeri default:hmaxnamesi
Similartomaxnamesbutaffectsonlythecitationsinthedocumentbody.
mincitenames=hintegeri default:hminnamesi
Similartominnamesbutaffectsonlythecitationsinthedocumentbody.
maxsortnames=hintegeri default:hmaxbibnamesi
Similartomaxnamesbutaffectsonlythenamesvisibletosorting. Sincethisdefaults
tohmaxbibnamesi,youshouldsetthisaftermaxbibnamesifmaxbibnamesisexplicitly
set.
minsortnames=hintegeri default:hminbibnamesi
Similartominnamesbutaffectsonlythenamesvisibletosorting. Sincethisdefaults
tohminbibnamesi,youshouldsetthisafterminbibnamesifminbibnamesisexplicitly
set.
maxitems=hintegeri default:3
Similartomaxnames,butaffectingallliterallists(publisher,location,etc.).
minitems=hintegeri default:1
Similartominnames,butaffectingallliterallists(publisher,location,etc.).
autocite=plain,inline,footnote,superscript,...
Thisoptioncontrolsthebehaviorofthe\autocitecommanddiscussedin§3.9.4.
Theplainoptionmakes\autocitebehavelike\cite,inlinemakesitbehavelike
\parencite, footnote makes it behave like \footcite, and superscript makes
it behave like \supercite. The options plain, inline, and footnote are always
49

available, thesuperscriptoptionisonlyprovidedbythenumericcitationstyles
whichcomewiththispackage. Thecitationstylemayalsodefineadditionaloptions.
Thedefaultsettingofthisoptiondependsontheselectedcitationstyle,see§3.3.1.
autopunct=true,false default:true
This option controls whether the citation commands scan ahead for punctuation
marks. See§3.9and\DeclareAutoPunctuationin§4.7.5fordetails.
language=autobib,autocite,auto,hlanguagei default:autobib
Thisoptioncontrolsmultilingualsupport. Bydefaultbiblatexautomaticallypicks
up the active surrounding language from the babel/polyglossia package15 (and
fall back to English if babel/polyglossia is not available). autobib switches the
languageforeachentryinthebibliographyusingthelangidfieldandthelanguage
environmentspecifiedbytheautolangoption. autociteswitchesthelanguagefor
eachcitationusingthelangidfieldandthelanguageenvironmentspecifiedbythe
autolangoption. autoisashorthandtosetbothautobibandautocite. Itisalso
possibletoselectthepackagelanguagemanually. Inthiscase,thelanguagechosen
willoverridethelangidofentriesandyoushouldstillchoosealanguageswitching
environment with the autolang option to select how the switch to the manually
chosenlanguageishandled. Pleaserefertotable2foralistofsupportedlanguages
andthecorrespondingidentifiers.
clearlang=true,false default:true
If this option is enabled, biblatex will automatically clear the language field of
all entries whose language field matches the babel/polyglossia language of the
document(orthelanguagespecifiedexplicitlywiththelanguageoption)inorderto
omitredundantlanguagespecifications. Thelanguagemappingsrequiredbythis
feature are provided by the \DeclareRedundantLanguages command from § 4.9.1.
Thisoptionisalsosettableonaper-typeandper-entrybasis.
autolang=none,hyphen,other,other*,langname default:none
This option controls which babel language environment16 is used if the
babel/polyglossiapackageisloadedandabibliographyentryincludesalangid
field(see§2.2.3). Notethatregardlessoftheselectedvaluebiblatexautomatically
adjusts to the main document language if babel/polyglossia is loaded. In mul-
tilingual documents, it will also continually adjust to the current language as far
ascitationsandthedefaultlanguageofthebibliographyisconcerned. Theeffect
of additional language adjustment, which can negate the effect of picking up the
surroundinglanguage,dependsonthelanguageenvironmentselectedbythisoption.
Thepossiblechoicesare:
none Donotuseanyadditionalenclosinglanguageenvironmentatall. This
means that citations and the bibliography are set in the currently
activelanguage—thisneednotbethemainlanguage.
hyphen Enclosetheentryinahyphenrulesenvironment. Thiswillloadhy-
phenationpatternsforthelanguagespecifiedinthelangidfieldof
15Notethatbiblatexhasonlylimitedsupportforpolyglossiaversionspriortov1.45.Ifpolyglossia
isused,itshouldbeupdatedtoversion1.45(2019/10/27)orabove.
16polyglossiaunderstandsthebabellanguageenvironmentstooandsothisoptioncontrolsboth
thebabelandpolyglossialanguageenvironments.
50

theentry,ifavailable. Localisationstringsandextralanguagedefi-
nitions are not changed and taken from the surrounding language
environment.
other Enclosetheentryinanotherlanguageenvironment. Thiswillload
hyphenationpatternsforthespecifiedlanguage,enableallextradef-
initionswhichbabel/polyglossiaandbiblatexprovideforthere-
spectivelanguage,andtranslatekeytermssuchas‘editor’and‘vol-
ume’. Theextradefinitionsincludelocalisationsofthedateformat,of
ordinals,andsimilarthings.
other* Enclose the entry in an otherlanguage* environment. Please note
thatbiblatextreatsotherlanguage*likeotherlanguageiflanghook
issettoextras.
langname polyglossiaonly. Enclosetheentryina<languagename>environ-
ment. Thebenefitofthisoptionvalueforpolyglossiausersisthatit
takesnoteofthelangidoptsfieldsothatyoucanaddper-language
optionstoanentry(likeselectingalanguagevariant). Whenusing
babel,thisoptiondoesthesameastheotheroptionvalue.
langhook=captions,extras default:captions
This option controls whether bibliography strings and extras are written to
\captions<language>or\extras<language>. Theexacteffectofthisoptionde-
pendonthelanguagepackage(babel/polyglossia). Broadlyspeaking,thelanguage
switching environments provided by those packages (except hyphenrules) either
switchlanguagecaptionsandextrasoronlylanguageextras. Hence,ifthisoption
issettoextras,alllanguageswitcheswillaffectbiblatex,whereaswithcaptions
onlylanguageswitchesthatalsoswitchotherpartsofthedocumentlanguageaffect
biblatex.
block=none,space,par,nbpar,ragged default:none
This option controls the extra spacing between blocks, i.e., larger segments of a
bibliographyentry. Thepossiblechoicesare:
none Donotaddanythingatall.
space Insertadditionalhorizontalspacebetweenblocks. Thisissimilarto
thedefaultbehaviorofthestandardLaTeXdocumentclasses.
par Startanewparagraphforeveryblock. Thisissimilartotheopenbib
optionofthestandardLaTeXdocumentclasses.
nbpar Similartotheparoption,butdisallowspagebreaksatblockbound-
ariesandwithinanentry.
ragged Inserts a small negative penalty to encourage line breaks at block
boundariesandsetsthebibliographyraggedright.
The\newblockpunctcommandmayalsoberedefineddirectlytoachievedifferent
results,see§3.12.1. Alsosee§4.7.1foradditionalinformation.
locallabelwidth=true,false default:false
Thisoptioncontrolswhether\printbibliographyusesalocallycalculatedvaluefor
\labelnumberwidthand\labelalphawidthortheglobalvaluecalculatedfromall
entries. Thelocalvalueiscalculatedseparatelyforeachbibliographyandtakesinto
51

accountonlytheentriesdisplayedinthatbibliography. Thisoptionisusefulifthere
areseveralbibliographieswithwildlyvaryinglabellengthsinthesamedocument.
notetype=foot+end,footonly,endonly default:foot+end
Thisoptioncontrolsthebehaviorof\mkbibfootnote,\mkbibendnote,andsimilar
wrappersfrom§4.10.4. Thepossiblechoicesare:
foot+end Supportbothfootnotesandendnotes,i.e.,\mkbibfootnotewillgen-
eratefootnotesand\mkbibendnotewillgenerateendnotes.
footonly Forcefootnotes,i.e.,make\mkbibendnotegeneratefootnotes.
endonly Forceendnotes,i.e.,make\mkbibfootnotegenerateendnotes.
hyperref=true,false,auto,manual default:auto
Whether or not to transform citations and back references into clickable hyper-
links. Thisfeaturerequiresthehyperrefpackage. Italsorequiressupportbythe
selected citation style. All standard styles which ship with this package support
hyperlinks. hyperref=autoautomaticallydetectsifthehyperrefpackagehasbeen
loaded. This is the default setting. hyperref=false explicitly disables links even
if hyperref is loaded. hyperref=true enables links when hyperref is loaded, it
cannot explicitly enable links if hyperref is not loaded, as such it works exactly
like hyperref=auto except that it will issue a warning if hyperref is not loaded.
hyperref=manualgivesfullmanualcontroloverhyperrefinteraction,itshouldonly
beneededbypackageauthorsinveryspecialcircumstances. Withthehyperref=
manualsettingyouareresponsibletoenableordisablehyperrefsupportmanually
with\BiblatexManualHyperrefOnor\BiblatexManualHyperrefOffyourself. One
ofthetwocommandsmustbecalledexactlyonce;\BiblatexManualHyperrefOncan
onlybecalledafterhyperrefisloaded.
backref=true,false default:false
Whetherornottoprintbackreferencesinthebibliography. Thebackreferencesare
alistofpagenumbersindicatingthepagesonwhichtherespectivebibliography
entry is cited. If there are refsection environments in the document, the back
references are local to the reference sections. Strictly speaking, this option only
controls whether the biblatex package collects the data required to print such
references. Thisfeaturestillhastobesupportedbytheselectedbibliographystyle.
Allstandardstyleswhichcomewiththispackagedoso.
backrefstyle=none,three,two,two+,three+,all+ default:three
Thisoptioncontrolshowsequencesofconsecutivepagesinthelistofbackreferences
areformatted. Thefollowingstylesareavailable:
none Disablethisfeature,i.e.,donotcompressthepagelist.
three Compressanysequenceofthreeormoreconsecutivepagestoarange,
e.g.,thelist‘1,2,11,12,13,21,22,23,24’iscompressedto‘1,2,11–13,
21–24’.
two Compressanysequenceoftwoormoreconsecutivepagestoarange,
e.g.,theabovelistiscompressedto‘1–2,11–13,21–24’.
two+ Similarinconcepttotwobutasequenceofexactlytwoconsecutive
pages is printed using the starting page and the localisation string
sequens,e.g.,theabovelistiscompressedto‘1sq.,11–13,21–24’.
52

three+ Similarinconcepttotwo+butasequenceofexactlythreeconsecutive
pages is printed using the starting page and the localisation string
sequentes,e.g.,theabovelistiscompressedto‘1sq.,11sqq.,21–24’.
all+ Similarinconcepttothree+butanysequenceofconsecutivepages
isprintedasanopen-endedrange,e.g.,theabovelistiscompressed
to‘1sq.,11sqq.,21sqq.’.
AllstylessupportbothArabicandRomannumerals. Inordertoavoidpotentially
ambiguouslists,differentsetsofnumeralswillnotbemixedwhengeneratingranges,
e.g.,thelist‘iii,iv,v,6,7,8’iscompressedto‘iii–v,6–8’.
backrefsetstyle=setonly,memonly,setormem,setandmem,memandset, default:setonly
setplusmem
This option controls how back references to @set entries and their members are
handled. Thefollowingoptionsareavailable:
setonly Allbackreferencesareaddedtothe@setentry. Thepagereflistsof
setmembersremainblank.
memonly Referencestosetmembersareaddedtotherespectivemember. Ref-
erencestothe@setentryareaddedtoallmembers. Thepagereflist
ofthe@setentryremainsblank.
setormem Referencestothe@setentryareaddedtothe@setentry. References
tosetmembersareaddedtotherespectivemember.
setandmem Referencestothe@setentryareaddedtothe@setentry. References
tosetmembersareaddedtotherespectivememberandtothe@set
entry.
memandset Referencestothe@setentryareaddedtothe@setentryandtoall
members. References to set members are added to the respective
member.
setplusmem Referencestothe@setentryareaddedtothe@setentryandtoall
members. References to set members are added to the respective
memberandtothe@setentry.
backreffloats=true,false default:true
Whethertoenablebackreferencestocitationsinfloats.
indexing=true,false,cite,bib default:false
Thisoptioncontrolsindexingincitationsandinthebibliography. Moreprecisely,
itaffectsthe\ifciteindexand\ifbibindexcommandsfrom§4.6.2. Theoptionis
settableonaglobal,aper-type,oronaper-entrybasis. Thepossiblechoicesare:
true Enableindexingglobally.
false Disableindexingglobally.
cite Enableindexingincitationsonly.
bib Enableindexinginthebibliographyonly.
This feature requires support by the selected citation style. All standard styles
whichcomewiththispackagesupportindexingofbothcitationsandentriesinthe
bibliography. Notethatyoustillneedtoenableindexinggloballywith\makeindex
togetanindex.
53

citepagerange=normalized,2sq,3sqq,allsqq,compressed default:normalized
Thisoptioncontrolshowpagerangesareformattedinthepostnotefieldofcitations.
Thefollowingformatsareavailable:
normalized Thecitedpagesareoutputwithnormalizedrangesandfullstarting
andendingpagesinallcases,e.g.,thelist‘1-2,11-13,21-24’isoutput
as‘1–2,11–13,21–24’.
2sq Arangeofexactlytwoconsecutivepagesisprintedusingthestart-
ing page and the localisation string sequens, e.g., the above list is
compressedto‘1sq.,11–13,21–24’.
3sqq Similarinconceptto2sqbut,additionally,arangeofexactlythree
consecutivepages isprinted using thestarting pageand thelocali-
sation string sequentes, e.g., the above list is compressed to ‘1sq.,
11sqq.,21–24’.
allsqq Similarinconceptto3sqqwiththedifferencethatsequentesisde-
finedas‘anyrangeofmorethantwoconsecutivepages’. Hence,the
abovelistiscompressedto‘1sq.,11sqq.,21sqq.’.
compressed Thepagerangesarecompressedwith\mkcomprange(see§4.6.4),so
theabovelistcomesoutas‘1–2,11–3,21–4’.
Thespacinginsertedbetweenthepagenumberandtherespectivelocalisationstring
maybemodifiedbyredefiningthemacro\sqspace.
Note that this feature is only supported by citation styles that use \mkautorange
or \mkautorange* for formatting page ranges in the postscript field (see § 4.6.4).
Whenusing\mkseqrangeor\mkseqrange*, 2sq, 3ssq, andallsqqareconsidered,
anyothervalueequals3ssq.
loadfiles=true,false default:false
This option controls whether external files requested by way of the \printfile
command are loaded. See also § 3.14.8 and \printfile in § 4.4.1. Note that this
featureisdisabledbydefaultforperformancereasons.
refsection=none,part,chapter,chapter+,section,section+,subsection, default:none
subsection+
Thisoptionautomaticallystartsanewreferencesectionatadocumentdivisionsuch
asachapterorasection. Thisisequivalenttothe\newrefsectioncommand,see
§3.8.4fordetails. Thefollowingchoiceofdocumentdivisionsisavailable:
none Disablethisfeature.
part Startareferencesectionatevery\partcommand.
chapter Startareferencesectionatevery\chaptercommand.
chapter+ Startareferencesectionatevery\chapterandeveryhigherlevelof
sectioning,i.e. \part.
section Startareferencesectionatevery\sectioncommand.
section+ Startareferencesectionatevery\sectionandeveryhigherlevelof
sectioning,i.e. \partand\chapter(ifavailable).
subsection Startareferencesectionatevery\subsectioncommand.
54

subsection+ Startareferencesectionatevery\subsectionandeveryhigherlevel
ofsectioning,i.e. \part,\chapter(ifavailable)and\section.
refsegment=none,part,chapter,chapter+,section,section+,subsection, default:none
subsection+
Similartotherefsectionoptionbutstartsanewreferencesegment. Thisisequiv-
alent to the \newrefsegment command, see § 3.8.5 for details. When using both
options,notethatyoucanonlyapplythisoptiontoalower-leveldocumentdivision
thantheonerefsectionisappliedtoandthatnestedreferencesegmentswillbe
localtotheenclosingreferencesection.
citereset=none,part,chapter,chapter+,section,section+,subsection, default:none
subsection+
Thisoptionautomaticallyexecutesthe\citeresetcommandfrom§3.9.8atadoc-
umentdivisionsuchasachapterora section. The followingchoiceofdocument
divisionsisavailable:
none Disablethisfeature.
part Performaresetatevery\partcommand.
chapter Performaresetatevery\chaptercommand.
chapter+ Performaresetatevery\chapterand\partcommand.
section Performaresetatevery\sectioncommand.
section+ Perform a reset at every \section, hchapteri (if supported by the
class)and\partcommand.
subsection Performaresetatevery\subsectioncommand.
subsection+ Perform a reset at every \subsection, \section, hchapteri (if sup-
portedbytheclass)and\partcommand.
abbreviate=true,false default:true
Whetherornottouselongorabbreviatedstringsincitationsandinthebibliography.
Thisoptionaffectsthelocalisationmodules. Ifthisoptionisenabled,keytermssuch
as‘editor’areabbreviated. Ifnot,theyarewrittenout. Thisoptionisalsosettableon
aper-typeorper-entrybasis.
date=year,short,long,terse,comp,ymd,iso default:comp
Thisoptioncontrolsthebasicformatofprinteddatespecifications. Thefollowing
choicesareavailable:
year Useonlyyears,forexample:
2010
2010–2012
short Usetheshortformatwithverboseranges,forexample:
01/01/2010
21/01/2010–30/01/2010
01/21/2010–01/30/2010
55

long Usethelongformatwithverboseranges,forexample:
1stJanuary2010
21stJanuary2010–30thJanuary2010
January21,2010–January30,2010
terse Usetheshortformatwithcompactranges,forexample:
21–30/01/2010
01/21–01/30/2010
comp Usethelongformatwithcompactranges,forexample:
21st–30thJanuary2010
January21–30,2010
iso UseISO8601ExtendedFormat(yyyy-mm-dd),forexample:
2010-01-01
2010-01-21/2010-01-30
ymd A year-month-day format which can be modified by other options
unlikestrictiso8601-2,forexample:
2010-1-1
2010-1-21/2010-1-30
Note that iso format will enforce dateera=astronomical, datezeros=true,
timezeros=true, seconds=true, <datetype>time=24h and julian=false. ymd
isanEDTF-likeformatbutwhichcanchangethevariousoptionswhichthestrict
isooptiondoesnotallowfor.
Asseenintheaboveexamples,theactualdateformatislanguagespecific. Notethat
themonthnameinalllongformatsisresponsivetothedateabbrevpackageoption.
Theleadingzerosformonthsanddaysinallshortformatsmaybecontrolledsepa-
ratelywiththedatezerospackageoption. Theleadingzerosforhours,minutesand
secondsinallshortformatsmaybecontrolledseparatelywiththetimezerospack-
ageoption. Ifoutputtingtimes,theprintingofsecondsandtimezonesiscontrolled
bythesecondsandtimezonesoptionsrespectively.
The options julian and gregorianstart may be used to control when to output
JulianCalendardates.
labeldate=year,short,long,terse,comp,ymd,iso default:year
Similar to the date option but controls the format of the date field selected with
\DeclareLabeldate.
<datetype>date=year,short,long,terse,comp,ymd,iso default:comp
Similartothedateoptionbutcontrolstheformatofthe<datetype>datefieldin
thedatamodel.
alldates=year,short,long,terse,comp,ymd,iso
Setstheoptionforalldatesinthedatamodeltothesamevalue. Thedatefieldsin
thedefaultdatamodelaredate,origdate,eventdateandurldate.
56

julian=true,false default:false
Thisoptioncontrolswhetherdatesbeforethedatespecifiedinthegregorianstart
option will be converted automatically to the Julian Calendar. Dates so changed
willreturn‘true’forthe\ifdatejulianand\if<datetype>datejuliantests(see
§4.6.2). Pleasebearinmindthatdatesconsistingofjustayearlike‘1565’willnever
beconvertedtoaJulianCalendardatebecauseadatewithoutamonthanddayhas
anambiguousJulianCalendarrepresentation17. Forexample,inthecaseof‘1565’,
thisisJulianyear‘1564’untilaftertheGregoriandate‘10thJanuary1565’whenthe
Julianyearbecomes‘1565’.
gregorianstart=hYYYY-MM-DDi
ThisoptioncontrolsthedatebeforewhichdatesareconvertedtotheJulianCalendar.
Itisastrictformatstring,4-digityear,2-digitmonthandday,separatedbyasingle
dashcharacter(anyvalidUnicodecharacterwiththe‘Dash’property). Thedefault
is’1582-10-15’,thedateoftheinstigationofthestandardGregorianCalendar. This
optiondoesnotnothingunlessjulianissetto‘true’.
datezeros=true,false default:true
This option controls whether short and terse date components are printed with
leadingzerosunlessoverriddenbyspecificformatting.
timezeros=true,false default:true
Thisoptioncontrolswhethertimecomponentsareprintedwithleadingzerosunless
overriddenbyspecificformatting.
timezones=true,false default:false
Thisoptioncontrolswhethertimezonesareprintedwhenprintingtimes.
seconds=true,false default:false
Thisoptioncontrolswhethersecondsareprintedwhenprintingtimes.
dateabbrev=true,false default:true
Thisoptioncontrolswhetherlongandcompdatesareprintedwithlongorabbreviated
month/yeardivisionnames. Theoptionissimilartothegenericabbreviateoption
but specific to the date formatting. This option is also settable on a per-type and
per-entrybasis.
datecirca=true,false default:false
Thisoptioncontrolswhethertooutput‘circa’informationaboutdates. Ifsettotrue,
dateswillbeprecededbytheexpansionofthe\datecircaprintmacro(§3.12.1).
dateuncertain=true,false default:false
Thisoptioncontrolswhethertooutputuncertaintyinformationaboutdates. Ifsetto
true,dateswillbefollowedbytheexpansionofthe\dateuncertainprintmacro
andenddateswillbefollowedbythe\enddateuncertainprintmacro(§3.12.1).
17Thisispotentiallytruefordatesmissingtimestoobutthisisnotrelevantforbibliographicwork.
57

dateera=astronomical,secular,christian default:astronomical
This option controls how date era information is printed. ‘astronomical’ uses
\dateeraprintpre to print era information before start/end dates. ‘secular’ and
‘christian’ uses \dateeraprint to print era information after the start/end/dates.
By default ‘astronomical’ results in a minus sign before BCE/BC dates and ‘secu-
lar’/‘christian’ results in the relevant localisation strings like ‘BCE’ or ‘BC’ after
BCE/BCdates. Seetherelevantcommentsin§3.12.1andthelocalisationstringsin
§4.9.2.21.
dateeraauto=hintegeri default:0
This option sets the astronomical year, below which era localisation strings are
automaticallyadded. Thisoptiondoesnothingwithoutdateerabeingsetto‘secular’
or‘christian’.
time=12h,24h,24hcomp default:24h
Thisoptioncontrolsthebasicformatofprintedtimespecifications. Thefollowing
choicesareavailable:
24h 24-hourformat,forexample:
14:03:23
14:3:23
14:03:23+05:00
14:03:23Z
14:21:23–14:23:45
14:23:23–14:23:45
24hcomp 24-hourformatwithcompressedranges,forexample:
14:21–23(hoursarethesame)
14:23:23–45(hourandminutearethesame)
12h 12-hourformatwith(localised)AM/PMmarkers,forexample:
2:34PM
2:34PM–3:50PM
Asseenintheaboveexamples,theactualtimeformatislanguagespecific. Notethat
theAM/PMstringisresponsivetotheabbreviatepackageoption,ifthismakesa
differenceinthespecificlocale. Theleadingzerosinthe24-hourformatsmaybe
controlledseparatelywiththetimezerospackageoption. Theseparatorbetween
timecomponents(\bibtimesepand\bibtzminsep)andbetweenthetimeandany
timezone(\bibtimezonesep)arealsolanguagespecificandcustomisable,see§3.12.3.
Thereareglobalpackageoptionswhichdeterminewhethersecondsandtimezones
areprinted(secondsandtimezones,respectively,see§3.1.2.1). Timezones,ifpresent,
areeither‘Z’oranumericpositiveornegativeoffset. Nodefaultstylesprinttime
information. Customstylesmayprinttimesbyusingthe\print<datetype>time
commands,see§4.4.1.
labeltime=12h,24h,24hcomp default:24h
Similartothetimeoptionbutcontrolstheformatofthetimepartfieldsobtained
fromthefieldselectedwith\DeclareLabeldate.
58

<datetype>time=12h,24h,24hcomp default:24h
Similartothetimeoptionbutcontrolstheformatofthetimepartfieldsobtained
fromthe<datetype>datefieldinthedatamodel.
alltimes=12h,24h,24hcomp
Setslabeltimeandthe<datetype>timeoptionforalltimesinthedatamodelto
thesamevalue. Thedatefieldssupportingtimepartsinthedefaultdatamodelare
date,origdate,eventdateandurldate.
dateusetime=true,false default:false
Specifieswhethertoprintanytimecomponentofadatefieldafterthedatecomponent.
The separator between the date and time components is \bibdatetimesep from
§3.12.3.
labeldateusetime=true,false default:false
Similartothedateusetimeoptionbutcontrolsthewhethertoprinttimecomponents
forthefieldselectedwith\DeclareLabeldate.
<datetype>dateusetime=true,false default:false
Similartothedateusetimeoptionbutcontrolsthewhethertoprinttimecomponents
forthe<datetype>datefieldinthedatamodel.
alldatesusetime=true,false default:false
Sets labeldateusetime and the <datetype>dateusetime option for all
<datetype>datefieldsinthedatamoel.
defernumbers=true,false default:false
In contrast to standard LaTeX, the numeric labels generated by this package are
normally assigned to the full list of references at the beginning of the document
body. Ifthisoptionisenabled,numericlabels(i.e.,thelabelnumberfielddiscussed
in § 4.2.4) are assigned the first time an entry is printed in any bibliography. See
§3.15.5forfurtherexplanation. ThisoptionrequirestwoLaTeXrunsafterthedata
has been exported to the bbl file by the backend (in addition to any other runs
requiredbypagebreakschangingetc.). Animportantthingtonoteisthatifyou
areusingthisoption,thenchangestooptions,thebibfileorcertaincommandslike
\printbibliographywillusuallyrequirethatyoudeleteyourcurrentauxfileand
re-runLaTeXtoobtainthecorrectnumbering. See§4.1.
punctfont=true,false default:false
This option enables an alternative mechanism for dealing with unit punctuation
after a field printed in a different font (for example, a title printed in italics). See
\setpunctfontin§4.7.1fordetails.
arxiv=abs,ps,pdf,format default:abs
PathselectorforarXivlinks. Ifhyperlinksupportisenabled,thisoptioncontrols
whichversionofthedocumentthearXiveprintlinkswillpointto. Thefollowing
choicesareavailable:
abs Linktotheabstractpage.
59

ps LinktothePostScriptversion.
pdf Linktothepdfversion.
format Linktotheformatselectorpage.
See§3.14.7fordetailsonsupportforarXivandelectronicpublishinginformation.
texencoding=auto,hencodingi default:auto
Specifiestheencodingofthetexfile. Thisoptionaffectsthedatatransferredfrom
thebackendtobiblatex. Thiscorrespondstobiber’s--output-encodingoption.
Thefollowingchoicesareavailable:
auto Try to auto-detect the input encoding. If the inputenc/inputenx/
luainputencpackageisavailable,biblatexwillgetthemainencod-
ingfromthatpackage. Ifnot,itassumesutf-8encodingifaLaTeX
formatusingatleasttheApril2018versionofthekernel,XeTeXor
LuaTeXhasbeendetected,andus-asciiotherwise.
hencodingi Specifies the hencodingi explicitly. This is for odd cases in which
auto-detectionfailsoryouwanttoforceacertainencodingforsome
reason.
Notethatsettingtexencoding=hencodingiwillalsoaffectthebibencodingoptionif
bibencoding=auto.
bibencoding=auto,hencodingi default:auto
Specifies the default encoding of the bib files. This can be overridden on a per-
datasourcebasisusingthebibencodingoptionto\addbibresource,see§3.8.1. This
optioncorrespondstobiber’s--input-encodingoption. Thefollowingchoicesare
available:
auto Usethisoptioniftheworkflowistransparent,i.e.,iftheencodingof
thebibfileisidenticaltotheencodingofthetexfile.
hencodingi Iftheencodingofthebibfileisdifferentfromtheoneofthetexfile,
youneedtospecifyitexplicitly.
Bydefault,biblatexassumesthatthetexfileandthebibfileusethesameencoding
(bibencoding=auto).
safeinputenc=true,false default:false
If this option is enabled, biblatex will automatically force texencoding=ascii if
theinputenc/inputenxpackagehasbeenloadedandtheinputencodingisutf-8,
i.e.,itwillignoreanymacro-basedutf-8supportanduseus-asciionly. biberwill
thentrytoconvertanynon-us-asciidatainthebibfiletous-ascii. Forexample,
itwillconvertṢto\d{S}.See§2.4.2.1foranexplanationofwhyyoumaywantto
enablethisoption.
bibwarn=true,false default:true
By default, biblatex will report warnings issued by the backend concerning the
datainthebibfileasLaTeXwarnings. Usethisoptiontosuppresssuchwarnings.
60

mincrossrefs=hintegeri default:2
Setstheminimumnumberofcrossreferencestohintegeriwhenrequestingabackend
run.18 Thisoptionalsoaffectsthehandlingofthexreffield. Seethefielddescription
in§2.2.3aswellas§2.4.1fordetails.
minxrefs=hintegeri default:2
Asmincrossrefsbutforxreffields.
bibtexcaseprotection=true,false default:true
Thisoptiononlyhasaneffectwhentheexpl3implementationofthecasechanging
functionsisselected. Iftheoptionissettotrue,\MakeSentenceCase*supportsbrace
protectionofwordsfromcasechangeasinclassicalBibTeX.Iftheoptionissetto
false,pairsofbracesnolongerimplycaseprotection,whichcannowbeachieved
bywrappingtherelevantwordin\NoCaseChange—thismakesforalessconfusing,
ifmoreverbose,markupofcaseprotection. Forexamplesoftheeffectofthisoption
refertothedocumentationof\MakeSentenceCase*in§4.6.4.
3.1.2.2 Style-specific
Thefollowingoptionsareprovidedbyallstandardbibliographystyles(asopposed
to the core package). The options are available as preamble options like those in
§3.1.2.1andataper-typeandper-entryscope.
isbn=true,false default:true
Thisoptioncontrolswhetherthefieldsisbn/issn/isrnareprinted.
url=true,false default:true
Thisoptioncontrolswhethertheurlfieldandtheaccessdateisprinted. Theoption
onlyaffectsentrytypeswhoseurlinformationisoptional. Theurlfieldof@online
entriesisalwaysprinted.
doi=true,false default:true
Thisoptioncontrolswhetherthefielddoiisprinted.
eprint=true,false default:true
Thisoptioncontrolswhethereprintinformationisprinted.
related=true,false default:true
Whethertouseinformationfromrelatedentriesornot. See§3.5.
18Ifanentrywhichiscross-referencedbyotherentriesinthebibfilehitsthisthreshold,itisincluded
inthebibliographyevenifithasnotbeencitedexplicitly.ThisisastandardfeatureoftheBibTeX
formatandnotspecifictobiblatex.Seethedescriptionofthecrossreffieldin§2.2.3forfurther
information.
61

alphabetic/numeric Additionally, styles of the alphabetic and numeric family
supportthesubentryoptioninglobal,per-typeandper-entryscope.
subentry=true,false default:false
Thisoptionaffectsthehandlingofcitationstosetmembersandthedisplayofsets
in the bibliography. If the option is enabled, citations to individual set members
featureanadditionalletterthatidentifiesthemember,thatletterisalsoprintedin
the bibliography. If the option is disabled, a citation to the member of a set will
displayjustasacitationtotheentiresetandtherewillbenoadditionallettersin
thebibliographyentriesenumeratingthemembers.
Supposekey1andkey2aremembersofthesetset1. Withsubentrysettotrueina
numericstyleacitationtokey1willshowas‘[1a]’andacitationtokey2as‘[1b]’,
while the entire set set1 will be cited as ‘[1]’. Furthermore ‘(a)’ and ‘(b)’ will be
addedinfrontoftheentrydataforthesetmembersinthebibliographyentryfor
theset. Withsubentrysettofalsecitationstoallthreekeyswillshowas‘[1]’,no
additionalletterwillbeprintedinthebibliography.
numeric-comp Thecitationstylenumeric-compsupportsthesubentrycompoption
inglobal,per-typeandper-entryscope.
subentrycomp=true,false default:true
This option determines whether or not citations to set members are compressed
similartonon-setcitations. Theoptiononlyhasaneffectifsubentryissettotrue.
Supposekey1,key2andkey3aremembersofthesetset1. Withsubentrycompset
totruethethreeentrieswillbecompressedto‘[1a–c]’incitations. Withsubentry
settofalsethecitationwillshowinthemoreverboseform‘[1a,1b,1c]’.
Theoptionisintendedmainlyforbackwardscompatibility,becauseearlierversions
ofbiblatexdidnotcompresssetmembercitations.
authortitle/authoryear All bibliography styles of the authoryear and
authortitlefamilyaswellasallbibliographystylesoftheverbosefamily—whose
bibliographystylesarebasedonauthortitle—supporttheoptiondashedinglobal
scope.
dashed=true,false default:true
Thisoptioncontrolswhetherrecurrentthesameauthor/editorlistinthebibliogra-
phy are replaced by a dash (\bibnamedash, see § 3.12.1). If the option is enabled,
subsequentmentionsofthesamenamelistatthebeginningofanentryarereplaced
by a dash provided the entry is not the first on the current page. If the option is
disabled,namelistsareneverreplacedbyadash.
authoryear Bibliography styles of the authoryear family provide the option
mergedateinglobal,per-typeandper-entryscope.
mergedate=false,minimum,basic,compact,maximum,true default:true
Thisoptioncontrolswhetherandhowthedatespecificationintheentryismerged
withthedatelabelshowndirectlyaftertheauthor/editorlist.
62

false Strictly separate the date specification shown in the entry (styled
withdate)fromthedatelabel(styledwithlabeldate). Thedatewill
alwaysbeshowntwice.
minimum Omitthedatespecificationwheneveritcoincidesexactly—including
extradateinformation—withtheoutputofthedatelabel.
basic Similartominimum,butthedatespecificationwillalsobeomittedifit
differsfromthedatelabelonlybytheabsenceoftheextradateletter.
compact Mergesalldatespecificationswiththedatelabel. Thedateformatof
thatmergeddatelabeliscontrolledbydate,notlabeldate,evenif
it is printed in the position of the date label. The issue field is not
merged.
maximum Likecompact,butifpresenttheissuefieldwillalsobemovedinto
thedatelabelatthebeginningoftheentry.
true Analiasforcompact.
Morein-depthexamplesofthisoptioncanbefoundinthestyleexamples.
‘ibid’ styles Citation styles with ‘ibid.’ function, namely authortitle-
ibid, authortitle-icomp, authoryear-ibid, authoryear-icomp, verbose-ibid,
verbose-inote, verbose-trad1, verbose-trad2 and verbose-trad3 provide the
globalibidpageoption.
ibidpage=true,false default:false
Whetheribidemwithoutpagereferencemeans‘samework’or‘samework+same
page’. Ifsettotrueapagerangepostnotewillbesuppressedinanibidemcitationif
thelastcitationwastothesamepagerange. Withibidpage=falsethepostnoteis
notomitted. Citationstodifferentpagerangesthanthepreviousalwaysproducethe
pagerangeswitheithersetting.
verbose All citation styles of the verbose family provide the global option
citepages.
citepages=permit,suppress,omit,separate default:permit
Thisoptioncontrolstheoutputofthepages/pagetotalfieldinthefullcitationin
combinationwithapostnotecontainingapagerange. Theoptioncanbeusedto
suppressreferencestotwopagerangesinfullcitationslikethefollowing
Author. “Title.” In: Book,pp.100–150,p.125.
Here‘p.125’isthepostnoteargumentand‘pp.100–150’isthevalueofthepages
field.
permit Allow duplication of page specifications, i.e. print both pages/
pagetotalandpostnote.
suppress Unconditionallysuppressthepages/pagetotalfieldsincitations,re-
gardlessofthepostnote.
omit Suppressthepages/pagetotalifthepostnotecontainsapagerange.
Theyarestillprintedifthereisnopostnoteorifthepostnoteisnot
anumberorrange.
63

separate Separatethepages/pagetotalfromthepostnoteifthelattercontains
apagerange. Thestringthisciteisaddedtoseparatethetwopage
ranges.
verbose-trad Thecitationstylesoftheverbose-tradfamilysupporttheglobal
optionstrict.
strict=true,false default:false
Thisoptionallowstorestricttheuseofthescholarlyabbreviations‘ibid.’ and‘op.cit.’
toavoidambiguities. Iftheoptionissettotruethesetermswillonlybeusedifthe
relevantworkwascitedinthesameorpreviousfootnote.
reading Thereadingstylesupportsanumberofadditionaloptions,buttheseare
notofgeneralinterestandcanbefoundinthestyleexample.
3.1.2.3 Internal
Thedefaultsettingsofthefollowingpreambleoptionsarecontrolledbybibliography
andcitationstyles. Apartfromthepagetrackerand<name>initsoptions,which
youmaywanttoadapt,thereisnormallynoneedtosetthemexplicitly.
pagetracker=true,false,page,spread default:false
This option controls the page tracker which is required by the \ifsamepage and
\iffirstonpagetestsfrom§4.6.2. Thepossiblechoicesare:
true Enablethetrackerinautomaticmode. ThisislikespreadifLaTeXis
intwosidemode,andlikepageotherwise.
false Disablethetracker.
page Enablethetrackerinpagemode. Inthismode,trackingworksona
per-pagebasis.
spread Enablethetrackerinspreadmode. Inthismode,trackingworksona
per-spread(doublepage)basis.
Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats,see§4.11.6.
citecounter=true,false,context default:false
This option controls the citation counter which is required by citecounter from
§4.6.2. Thepossiblechoicesare:
true Enablethecitationcounteringlobalmode.
false Disablethecitationcounter.
context Enablethecitationcounterincontext-sensitivemode. Inthismode,
citationsinfootnotesandinthebodytextarecountedindependently.
citetracker=true,false,context,strict,constrict default:false
Thisoptioncontrolsthecitationtrackerwhichisrequiredbythe\ifciteseenand
\ifentryseentestsfrom§4.6.2. Thepossiblechoicesare:
true Enablethetrackeringlobalmode.
64

false Disablethetracker.
context Enablethetrackerincontext-sensitivemode. Inthismode,citations
infootnotesandinthebodytextaretrackedindependently.
strict Enablethetrackerinstrictmode. Inthismode,anitemisonlycon-
sideredbythetrackerifitappearedinastand-alonecitation,i.e.,ifa
singleentrykeywaspassedtothecitationcommand.
constrict Thismodecombinesthefeaturesofcontextandstrict.
Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats, see § 4.11.6. This option is also settable on a per-type or per-entry
basis.
ibidtracker=true,false,context,strict,constrict default:false
Thisoptioncontrolsthe‘ibidem’trackerwhichisrequiredbythe\ifciteibidtest
from§4.6.2. Thepossiblechoicesare:
true Enablethetrackeringlobalmode.
false Disablethetracker.
context Enablethetrackerincontext-sensitivemode. Inthismode,citations
infootnotesandinthebodytextaretrackedseparately.
strict Enablethetrackerinstrictmode. Inthismode,potentiallyambiguous
references are suppressed. A reference is considered ambiguous if
either the current citation (the one including the ‘ibidem’) or the
previouscitation(theonethe‘ibidem’refersto)consistsofalistof
references.19
constrict This mode combines the features of context and strict. It also
keepstrackoffootnotenumbersanddetectspotentiallyambiguous
referencesinfootnotesinastricterwaythanthestrictoption. In
additiontotheconditionsimposedbythestrictoption,areference
inafootnotewillonlybeconsideredasunambiguousifthecurrent
citationandthepreviouscitationaregiveninthesamefootnoteorin
immediatelyconsecutivefootnotes.
Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats, see § 4.11.6. This option is also settable on a per-type or per-entry
basis.
opcittracker=true,false,context,strict,constrict default:false
Thisoptioncontrolsthe‘opcit’trackerwhichisrequiredbythe\ifopcittestfrom
§4.6.2. Thisfeatureissimilartothe‘ibidem’tracker,exceptthatittrackscitations
on a per-author/editor basis, i.e., \ifopcit will yield true if the cited item is the
sameasthelastonebythisauthor/editor. Thepossiblechoicesare:
true Enablethetrackeringlobalmode.
false Disablethetracker.
19Forexample,supposetheinitialcitationis“Jones,Title; Williams,Title”andthefollowingone
“ibidem”. Fromatechnicalpointofview,itisfairlyclearthatthe‘ibidem’refersto‘Williams’
becausethisisthelastreferenceprocessedbythepreviouscitationcommand.Toahumanreader,
however,thismaynotbeobviousbecausethe‘ibidem’mayalsorefertobothtitles.Thestrictmode
avoidssuchambiguousreferences.
65

context Enablethetrackerincontext-sensitivemode. Inthismode,citations
infootnotesandinthebodytextaretrackedseparately.
strict Enablethetrackerinstrictmode. Inthismode,potentiallyambiguous
referencesaresuppressed. Seeibidtracker=strictfordetails.
constrict This mode combines the features of context and strict. See the
explanationofibidtracker=constrictfordetails.
Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats, see § 4.11.6. This option is also settable on a per-type or per-entry
basis.
loccittracker=true,false,context,strict,constrict default:false
Thisoptioncontrolsthe‘loccit’trackerwhichisrequiredbythe\ifloccittestfrom
§4.6.2. Thisfeatureissimilartothe‘opcit’trackerexceptthatitalsocheckswhether
thehpostnoteiargumentsmatch,i.e.,\ifloccitwillyieldtrueifthecitationrefers
tothesamepagecitedbefore. Thepossiblechoicesare:
true Enablethetrackeringlobalmode.
false Disablethetracker.
context Enablethetrackerincontext-sensitivemode. Inthismode,citations
infootnotesandinthebodytextaretrackedseparately.
strict Enablethetrackerinstrictmode. Inthismode,potentiallyambiguous
references are suppressed. See ibidtracker=strict for details. In
additiontothat,thismodealsochecksifthehpostnoteiargumentis
numerical(basedon\ifnumeralsfrom§4.6.2).
constrict This mode combines the features of context and strict. See the
explanation of ibidtracker=constrict for details. In addition to
that,thismodealsochecksifthehpostnoteiargumentisnumerical
(basedon\ifnumeralsfrom§4.6.2).
Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats, see § 4.11.6. This option is also settable on a per-type or per-entry
basis.
idemtracker=true,false,context,strict,constrict default:false
Thisoptioncontrolsthe‘idem’trackerwhichisrequiredbythe\ifciteidemtest
from§4.6.2. Thepossiblechoicesare:
true Enablethetrackeringlobalmode.
false Disablethetracker.
context Enablethetrackerincontext-sensitivemode. Inthismode,citations
infootnotesandinthebodytextaretrackedseparately.
strict Thisisanaliasfortrue,providedonlyforconsistencywiththeother
trackers. Since‘idem’replacementsdonotgetambiguousinthesame
wayas‘ibidem’or‘op.cit.’,thestricttrackingmodedoesnotapply
tothem.
constrict This mode is similar to context with one additional condition: a
reference in a footnote will only be considered as unambiguous if
thecurrentcitationandthepreviouscitationaregiveninthesame
footnoteorinimmediatelyconsecutivefootnotes.
66

Note that this tracker is disabled in all floats unless explicitly requested with
trackfloats, see § 4.11.6. This option is also settable on a per-type or per-entry
basis.
trackfloats=true,false default:false
Whethertoenablecitationtrackinginfloats. Citationtrackinginfloatscanbetricky,
sothisoptionshouldonlybeenabledifabsolutelynecessaryandtheoutputshould
bescrutinisedcarefully,seealso§4.11.6.
parentracker=true,false default:true
This option controls the parenthesis tracker which keeps track of nested paren-
theses and brackets. This information is used by \parentext and \brackettext
from§3.9.5,\mkbibparensand\mkbibbracketsfrom§4.10.4and\bibopenparen,
\bibcloseparen,\bibopenbracket,\bibclosebracket(also§4.10.4).
maxparens=hintegeri default:3
Themaximumpermittednestinglevelofparenthesesandbrackets. Ifparentheses
andbracketsarenesteddeeperthanthisvalue,biblatexwillissueerrors.
<namepart>inits=true,false default:false
The option sets the \if<namepart>inits test from § 4.6.2. <namepart> is any
validnamepartasdefinedinthedatamodelbythe\DeclareDatamodelConstant
command(§4.2.3). Forthegivenname,forexample,theoptionbecomesgiveninits.
Thisoptionisalsosettableonaper-type,per-entry,per-namelistandper-namebasis.
If giveninits is set to true, the default name formats will only render the given
name initials and not the full given name. The standard styles only use the test
\ifgiveninitsandhenceonlyrespondtotheoptiongiveninits. Settingtheoption
foranamepartdifferentfromgivenhasnoeffectonthedefaultnameformats.
Notethatsortingandnameuniquenessarenotautomaticallyaffectedbythisoption,
thesehavetoberequestedexplicitlyvia\DeclareSortingNamekeyTemplateandthe
uniquenameoption(or\DeclareUniquenameTemplate),respectively. Awarningwill
be issued if giveninits is used together with uniquename set to one of the full
valuesanduniquenameisautomaticallysettothecorrespondinginitvalue.
terseinits=true,false default:false
This option controls the format of all initials generated by biblatex. If enabled,
initialsarerenderedusingaterseformatwithoutdotsandspaces. Forexample,the
initialsofDonaldErvinKnuthwouldberenderedas‘D.E.’bydefault,andas‘DE’
ifthisoptionisenabled. Theoptionwillaffectthe\ifterseinitstestfrom§4.6.2.
Theoptionworksbyredefiningsomemacroswhichcontroltheformatofinitials.
See§3.15.4fordetails. Thisoptionisalsosettableonaper-type,per-entry,per-name
andper-namelistbasis.
labelalpha=true,false default:false
Whetherornottoprovidethespecialfieldslabelalphaandextraalpha,see§4.2.4
for details. This option is also settable on a per-type and per-entry basis. See
also maxalphanames and minalphanames. Table 7 summarises the various extra*
disambiguationcountersandwhattheytrack.
67

maxalphanames=hintegeri default:3
Similartothemaxnamesoptionbutcustomizestheformatofthelabelalphafield.
minalphanames=hintegeri default:1
Similartotheminnamesoptionbutcustomizestheformatofthelabelalphafield.
labelnumber=true,false default:false
Whetherornottoprovidethespecialfieldlabelnumber,see§4.2.4fordetails. This
optionisalsosettableonaper-typeandper-entrybasis.
noroman=true,false default:false
Whether or not to try to parse roman numerals encountered in integer fields for
sortingpurposes. Sincebiberalsotriestoparsealphanumericvalueswhensorting
integerfields,thisromannumeralparsingcanbeaproblemwhen,forexample,‘C’
isencounteredasthiscouldbearomannumeralorasimplealphanumericstring
whichwouldhaveadifferentintegervaluedependingonhowitwasparsed. Itis
likelythatthisismostusefulonaper-entrybasisforentriesthathave,forexample,
a volume field with values such as ‘A’, ‘B’, ‘C’, ‘D’ which should not be parsed as
romannumeralssincethiswouldgiveincorrectintegervaluesfor‘C’and‘D’.
Thisoptionisalsosettableonaper-typeandper-entrybasis.
labeltitle=true,false default:false
Whetherornottoprovidethespecialfieldextratitle,see§4.2.4fordetails. Note
thatthespecialfieldlabeltitleisalwaysprovidedandthisoptioncontrolsrather
whetherlabeltitleisusedtogenerateextratitleinformation. Thisoptionisalso
settableonaper-typeandper-entrybasis. Table7summarisesthevariousextra*
disambiguationcountersandwhattheytrack.
labeltitleyear=true,false default:false
Whetherornottoprovidethespecialfieldextratitleyear,see§4.2.4fordetails.
Notethatthespecialfieldlabeltitleyearisalwaysprovidedandthisoptioncontrols
rather whether labeltitleyear is used to generate extratitleyear information.
Thisoptionisalsosettableonaper-typeandper-entrybasis. Table7summarises
thevariousextra*disambiguationcountersandwhattheytrack.
labeldateparts=true,false default:false
Whether or not to provide the special fields labelyear, labelmonth,
labelday, labelendyear, labelendmonth, labelendday, labelhour,
labelendhour, labelminute, labelendminute, labelsecond, labelendsecond,
labelyeardivision, labelendyeardivision, labeltimezone, labelendtimeone
andextradate,see§4.2.4fordetails. Thisoptionisalsosettableonaper-typeand
per-entrybasis. Table7summarisesthevariousextra*disambiguationcounters
andwhattheytrack.
singletitle=true,false default:false
Whetherornottoprovidethedatarequiredbythe\ifsingletitletest,see§4.6.2
for details. See table 6 for details on what determines the data for this test. This
optionisalsosettableonaper-typeandper-entrybasis.
68

Table6:WorkUniquenessoptions
Option Test Tracks
singletitle \ifsingletitle labelname
uniquetitle \ifuniquetitle labeltitle
uniquebaretitle \ifuniquebaretitle labeltitle when labelname
isnull
uniquework \ifuniquework labelname+labeltitle
uniquetitle=true,false default:false
Whetherornottoprovidethedatarequiredbythe\ifuniquetitletest,see§4.6.2
for details. See table 6 for details on what determines the data for this test. This
optionisalsosettableonaper-typeandper-entrybasis.
uniquebaretitle=true,false default:false
Whetherornottoprovidethedatarequiredbythe\ifuniquebaretitletest,see
§4.6.2fordetails. Seetable6fordetailsonwhatdeterminesthedataforthistest.
Thisoptionisalsosettableonaper-typeandper-entrybasis.
uniquework=true,false default:false
Whetherornottoprovidethedatarequiredbythe\ifuniqueworktest,see§4.6.2
for details. See table 6 for details on what determines the data for this test. This
optionisalsosettableonaper-typeandper-entrybasis.
uniqueprimaryauthor=true,false default:false
Whetherornottoprovidethedatarequiredbythe\ifuniqueprimaryauthortest,
see§4.6.2fordetails. Thisoptionisalsosettableonaper-typeandper-entrybasis.
uniquename=true,false,init,full,allinit,allfull,mininit,minfull, default:false
minyearinit,minyearfull
Whetherornottoupdatetheuniquenamecounter,see§4.6.2fordetails. Thisfeature
willdisambiguateindividualnamesinthelabelnamelist. Thisoptionisalsosettable
onaper-type,per-entry,per-namelistandper-namebasis. Thepossiblechoicesare:
true Analiasforfull.
false Disablethisfeature.
init Disambiguateusinginitialsonly.
full Disambiguateusinginitialsorfullnames,asrequired.
allinit Similar to init but disambiguates all names in the labelname list,
beyondmaxnames/minnames/uniquelist.
allfull Similar to full but disambiguates all names in the labelname list,
beyondmaxnames/minnames/uniquelist.
mininit Avariantofinitwhichonlydisambiguatesnamesinidenticallists
ofbasenameparts(bydefault,listsoffamilynames).
minfull Avariantoffullwhichonlydisambiguatesnamesinidenticallists
ofbasenameparts(bydefault,listsoffamilynames).
minyearinit Avariantofmininitwhichonlydisambiguatesnamesinidentical
listsofbasenamepartspluslabelyear.
69

minyearfull Avariantofminfullwhichonlydisambiguatesnamesinidentical
listsofbasenamepartspluslabelyear.
Notethattheuniquenameoptionwillalsoaffectuniquelist, the\ifsingletitle
test, and the extradate and extraname fields. See § 4.11.4 for further details and
practicalexamples.
uniquelist=true,false,minyear default:false
Whetherornottoupdatetheuniquelistcounter,see§4.6.2fordetails. Thisfeature
will disambiguate the labelname list if it has become ambiguous after maxnames/
minnames truncation. Essentially, it overrides maxnames/minnames on a per-field
basis. Thisoptionisalsosettableonaper-type, per-entryandper-namelistbasis.
Thepossiblechoicesare:
true Disambiguatethelabelnamelist.
false Disablethisfeature.
minyear Disambiguatethelabelnamelistonlyifthetruncatedlistisidentical
toanotheronewiththesamelabelyear. Thismodeofoperationis
usefulforauthor-yearstylesandrequireslabeldateparts=true.
Note that the uniquelist option will also affect the \ifsingletitle test and the
extradateandextranamefields. See§4.11.4forfurtherdetailsandpracticalexam-
ples.
nohashothers=true,false default:false
By default, name lists which are truncated with ‘et al’–either explicitly by ‘and
others’ in the data source or the uniquelist and min/maxnames options–result in
differentnamelisthashes(andthereforedifferentextranameandextradatevalues)
anddifferentsorting. Thisoptionallowsthisbehaviourtobetuned. Whensetto
htruei, biber ignores ‘et al’ truncations for the purposes of generating name list
hashes. Consider:
Jones 1972
Jones/and others 1972
Smith 2000
Smith/Vogel/Beast/Tremble 2000
Withmaxnames=3,minnames=1,nohashothers=false,theresultwouldbe:
Jones 1972
Jones et al. 1972
Smith 2000
Smith et al. 2000
Whereaswithmaxnames=3,minnames=1,nohashothers=true,theresultwouldbe:
Jones 1972a
Jones et al. 1972b
Smith 2000a
Smith et al. 2000b
70

Table7:Disambiguationcounters
| Option         | Enabledfield(s) | Enabledcounter | Countertracks |
| -------------- | --------------- | -------------- | ------------- |
| labelalpha     | labelalpha      | extraalpha     | label         |
| labeldateparts | labelyear       | extradate      | extradate     |
context+labelyear
labelmonth
labelday
labelendyear
labelendmonth
labelendday
labelhour
labelminute
labelsecond
labelendhour
labelendminute
labelendsecond
labelyeardivision
labelendyeardivision
labeltimezone
labelendtimezone
| labeltitle | —   | extratitle | labelname+labeltitle |
| ---------- | --- | ---------- | -------------------- |
—
| labeltitleyear |     | extratitleyear | labeltitle+labelyear |
| -------------- | --- | -------------- | -------------------- |
| —              | —   | extraname      | labelname            |
Ifdesired,thiscouldbefurthersimplifiedbyremovingthe‘etal.’toobtain:
Jones 1972a
Jones 1972b
Smith 2000a
Smith 2000b
Notethatthenohashothersoptionwillaffecttheextradateandextranamefields.
Thisoptionisalsosettableonaper-type,per-entryandper-namelistbasis.
nosortothers=true,false default:false
Theoptionhasarelatedtoeffecttonohashothersbutappliestosorting–thevisible
listofnames(whichistheminsortnamesvalue)usedtodeterminesortingwillignore
| anytruncation. Thismeansthatwithnosortothers=true,thenamelists: |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- |
Jones, Smith
| Jones, Smith et | al  |     |     |
| --------------- | --- | --- | --- |
willsortexactlythesame. Thedefaultsettingofnosortothersalwayssortsinthe
ordershownintheexample,thatis,bydefault,truncatednameslistsalwayssort
afteranynamelistsidenticaltothepointoftruncation.
Thisoptionisalsosettableonaper-type,per-entryandper-namelistbasis.
3.1.3 EntryOptions
Entryoptionsarepackageoptionswhichdeterminehowbibliographydataentries
| arehandled. Theymaybesetatvariousscopesdefinedbelow. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- |
71

3.1.3.1 Preamble/Type/EntryOptions
The following options are settable on a per-type basis or on a per-entry in the
optionsfield. Inadditiontothat,theymayalsobeusedintheoptionalargumentto
\usepackageaswellasintheconfigurationfileandthedocumentpreamble. Thisis
usefulifyouwanttochangethedefaultbehaviourglobally.
useauthor=true,false default:true
Whethertheauthorisusedinlabelsandconsideredduringsorting. Thismaybe
useful if an entry includes an author field but is usually not cited by author for
some reason. Setting useauthor=false does not meanthat the author isignored
completely. Itmeansthattheauthorisnotusedinlabelsandignoredduringsorting.
Theentrywillthenbealphabetizedbyeditorortitle. Withthestandardstyles,
theauthorisprintedafterthetitleinthiscase. Seealso§3.6. Thisoptionisalso
settableonaper-typeandper-entrybasis.
useeditor=true,false default:true
Whether the editor replaces a missing author in labels and during sorting. This
maybeusefulifanentryincludesaneditorfieldbutisusuallynotcitedbyeditor.
Settinguseeditor=falsedoesnotmeanthattheeditorisignoredcompletely. It
meansthattheeditordoesnotreplaceamissingauthorinlabelsandduringsorting.
Theentrywillthenbealphabetizedbytitle. Withthestandardstyles,theeditor
isprintedafterthetitleinthiscase. Seealso§3.6. Thisoptionisalsosettableona
per-typeandper-entrybasis.
usetranslator=true,false default:false
Whether the translator replaces a missing author/editor in labels and during
sorting. Settingusetranslator=truedoesnotmeanthatthetranslatoroverrides
theauthor/editor. Itmeansthatthetranslatorisconsideredasafallbackifthe
author/editorismissingorifuseauthoranduseeditoraresettofalse. Inother
words,inordertociteabookbytranslatorratherthanbyauthor,youneedtoset
thefollowingoptions: Thisoptionisalsosettableonaper-typeandper-entrybasis.
@Book{...,
options = {useauthor=false,usetranslator=true},
author = {...},
translator = {...},
...
Withthestandardstyles,thetranslatorisprintedafterthetitlebydefault. Seealso
§3.6.
use<name>=true,false default:true
Asperuseauthor,useeditorandusetranslator,allnamelistsdefinedinthedata
model have an option controlling their behaviour in sorting and labelling auto-
maticallydefined. Global,per-typeandper-entryoptionscalled‘use<name>’are
automaticallycreated.
useprefix=true,false default:false
Whetherthedefaultdatamodelnamepart‘prefix’(von,van,of,da,de,della,etc.) is
consideredwhen:
72

• Printingthefamilynameincitations
• Sorting
• Generationofcertaintypesoflabels
• Generatingnameuniquenessinformation
• Formattingaspectsofthebibliography
Forexample,ifthisoptionisenabled,biblatexprecedesthefamilynamewiththe
prefix—LudwigvanBeethovenwouldbecitedas“vanBeethoven”andalphabetized
as “Van Beethoven, Ludwig”. If this option is disabled (the default), he is cited as
“Beethoven”andalphabetizedas“Beethoven,Ludwigvan”instead. Thisoptionisalso
settableonaper-typescope. WithbiblatexmldatasourcesandtheBibTeXextended
nameformatsupportedbybiber(see§3.4),thisisalsosettableonper-namelistand
per-namescopes.
indexing=true,false,cite,bib
The indexing option is also settable per-type or per-entry basis. See § 3.1.2.1 for
details.
skipbib=true,false default:false
Ifthisoptionisenabled,theentryisexcludedfromthebibliographybutitmaystill
becited. Thisoptionisalsosettableonaper-typebasis.
skipbiblist=true,false default:false
If this option is enabled, the entry is excluded from bibliography lists. It is still
includedinthebibliographyanditmayalsobecitedbyshorthandetc. Thisoption
isalsosettableonaper-typebasis.
skiplab=true,false default:false
If this option is enabled, biblatex will not assign any labels to the entry. It is
notrequiredfornormaloperation. Useitwithcare. Ifenabled,biblatexcannot
guaranteeuniquecitationsfortherespectiveentryandcitationsstyleswhichrequire
labelsmayfailtocreatevalidcitationsfortheentry. Thisoptionisalsosettableona
per-typebasis.
dataonly=true,false default:false
Settingthisoptionisequivalenttouniquename=false,uniquelist=false, skipbib,
skipbiblist,andskiplab. Itisnotrequiredfornormaloperation. Useitwithcare.
Thisoptionisalsosettableonaper-typebasis.
3.1.3.2 EntryOnlyOptions
Thefollowingoptionsaresettableonlyonaper-entryintheoptionsfield. Theyare
notavailablegloballyorper-type.
labelnamefield=hfieldnamei
Specifies the field to consider first when looking for a labelname candidate. It is
essentiallyprependedtothesearchlistcreatedby\DeclareLabelnameforjustthis
entry.
73

labeltitlefield=hfieldnamei
Specifiesthefieldtoconsiderfirstwhenlookingforalabeltitlecandidate. Itis
essentiallyprependedtothesearchlistcreatedby\DeclareLabeltitleforjustthis
entry.
3.1.4 LegacyOptions
The following legacy option may be used globally in the optional argument to
\documentclassorlocallyintheoptionalargumentto\usepackage:
openbib ThisoptionisprovidedforbackwardscompatibilitywiththestandardLaTeXdocu- Deprecated
mentclasses. openbibissimilartoblock=par.
3.2 GlobalCustomization
Apartfromwritingnewcitationandbibliographystyles,therearenumerouswaysto
customizethestyleswhichcomewiththispackage. Customizationwillusuallytake
placeinthepreamble,butthereisalsoaconfigurationfileforpermanentadaptions.
Theconfigurationfilemayalsobeusedtoinitializethepackageoptionstoavalue
differentfromthepackagedefault.
3.2.1 ConfigurationFile
Ifavailable,thispackagewillloadtheconfigurationfilebiblatex.cfg. Thisfileis
readattheendofthepackage,immediatelyafterthecitationandbibliographystyles
havebeenloaded.
3.2.2 SettingPackageOptions
Theload-timepackageoptionsin§3.1.1mustbegivenintheoptionalargumentto
\usepackage. Thepackageoptionsin§3.1.2mayalsobegiveninthepreamble. The
optionsareexecutedwiththefollowingcommand:
\ExecuteBibliographyOptions[hentrytype,…i]{hkey=value,…i}
Thiscommandmayalsobeusedintheconfigurationfiletomodifythedefaultsetting
ofapackageoption. Certainoptionsarealsosettableonaper-typebasis. Inthis
case, the optional hentrytypei argument specifies the entry type. The hentrytypei
argumentmaybeacomma-separatedlistofvalues.
3.3 StandardStyles
Thissectionprovidesashortdescriptionofallbibliographyandcitationstyleswhich
comewiththebiblatexpackage. Eachstyleisfurtherillustratedinastyleexample
which is linked in the right margin. The local link may not be available if this
documentdoesnotresideintheexpectedfolderstructure. Ifyouwanttowriteyour
ownstyles,see§4.
3.3.1 CitationStyles
Thecitationstyleswhichcomewiththispackageimplementseveralcommoncitation
schemes. Allstandardstylescaterfortheshorthandfieldandsupporthyperlinksas
wellasindexing.
74

numeric Thisstyleimplementsanumericcitationschemesimilartothestandardbibliographic Styleexample:
facilitiesofLaTeX.Itshouldbeemployedinconjunctionwithanumericbibliography local,online.
stylewhichprintsthecorrespondinglabelsinthebibliography. Itisintendedforin-
textcitations. Thestylewillsetthefollowingpackageoptionsatloadtime: autocite=
inline,labelnumber=true. Thisstylealsoprovidesanadditionalpreambleoption
calledsubentrywhichaffectsthehandlingofentrysets. Ifthisoptionisdisabled,
citationsreferringtoamemberofasetwillpointtotheentireset. Ifitisenabled,
thestylesupportscitationslike“[5c]”whichpointtoasubentryinaset(thethird
oneinthisexample). Seethestyleexamplefordetails.
numeric-comp A compact variant of the numeric style which prints a list of more than two con- Styleexample:
secutive numbers as a range. This style is similar to the cite package and the local,online.
sort&compressoptionofthenatbibpackageinnumericalmode. Forexample,in-
steadof“[8,3,1,7,2]”thisstylewouldprint“[1–3,7,8]”. Itisintendedforin-text
citations. Thestylewillsetthefollowingpackageoptionsatloadtime: autocite=
inline, sortcites=true, labelnumber=true. It also provides the subentry and
subentrycompoptions.
numeric-verb Averbosevariantofthenumericstyle. Thedifferenceaffectsthehandlingofalist Styleexample:
of citations and is only apparent when multiple entry keys are passed to a single local,online.
citation command. For example, instead of “[2, 5, 6]” this style would print “[2];
[5];[6]”. Itisintendedforin-textcitations. Thestylewillsetthefollowingpackage
options at load time: autocite=inline, labelnumber=true. It also provides the
subentryoption.
alphabetic Thisstyleimplementsanalphabeticcitationschemesimilartothealpha.bststyle Styleexample:
oftraditionalBibTeX.Thealphabeticlabelsresembleacompactauthor-yearstyleto local,online.
someextent,butthewaytheyareemployedissimilartoanumericcitationscheme.
Forexample,insteadof“Jones1995”thisstylewouldusethelabel“[Jon95]”. “Jones
andWilliams1986”wouldberenderedas“[JW86]”. Thisstyleshouldbeemployed
inconjunctionwithanalphabeticbibliographystylewhichprintsthecorresponding
labelsinthebibliography. Itisintendedforin-textcitations. Thestylewillsetthe
followingpackageoptionsatloadtime: autocite=inline,labelalpha=true. This
stylealsoprovidesanadditionalpreambleoptioncalledsubentrywhichaffectsthe
handling of entry sets. If this option is disabled, citations referring to a member
ofasetwillpointtotheentireset. Ifitisenabled,thestylesupportscitationslike
“[SGW(c)]”whichpointtoasubentryinaset(thethirdoneinthisexample). Seethe
styleexamplefordetails.
alphabetic-verb Averbosevariantofthealphabeticstyle. Thedifferenceaffectsthehandlingofa Styleexample:
listofcitationsandisonlyapparentwhenmultipleentrykeysarepassedtoasingle local,online.
citationcommand. Forexample,insteadof“[Doe92;Doe95;Jon98]”thisstylewould
print“[Doe92];[Doe95];[Jon98]”. Itisintendedforin-textcitations. Thestylewill
setthefollowingpackageoptionsatloadtime: autocite=inline,labelalpha=true.
Italsoprovidesthesubentryoption.
authoryear Thisstyleimplementsanauthor-yearcitationscheme. Ifthebibliographycontains Styleexample:
twoormoreworksbythesameauthorwhichwereallpublishedinthesameyear,a local,online.
letterisappendedtotheyear. Forexample,thisstylewouldprintcitationssuchas
“Doe1995a;Doe1995b;Jones1998”. Thisstyleshouldbeemployedinconjunction
with an author-year bibliography style which prints the corresponding labels in
thebibliography. Itisprimarilyintendedforin-textcitations,butitcouldalsobe
used with citations given in footnotes. The style will set the following package
75

options at load time: autocite=inline, labeldateparts=true, uniquename=full,
uniquelist=true.
authoryear-comp A compact variant of the authoryear style which prints the author only once if Styleexample:
subsequentreferencespassedtoasinglecitationcommandsharethesameauthor. If local,online.
theysharethesameyearaswell,theyearisalsoprintedonlyonce. Forexample,
instead of “Doe 1995b; Doe 1992; Jones 1998; Doe 1995a” this style would print
“Doe1992,1995a,b;Jones1998”. Itisprimarilyintendedforin-textcitations,butit
couldalsobeusedwithcitationsgiveninfootnotes. Thestylewillsetthefollowing
packageoptionsatloadtime: autocite=inline,sortcites=true,labeldateparts=
true,uniquename=full,uniquelist=true.
authoryear-ibid Avariantoftheauthoryearstylewhichreplacesrepeatedcitationsbytheabbre- Styleexample:
viation ibidem unless the citation is the first one on the current page or double- local,online.
pagespread,ortheibidemwouldbeambiguousinthesenseofthepackageoption
ibidtracker=constrict. Thestylewillsetthefollowingpackageoptionsatload
time: autocite=inline, labeldateparts=true, uniquename=full, uniquelist=
true,ibidtracker=constrict,pagetracker=true. Thisstylealsoprovidesanaddi-
tionalpreambleoptioncalledibidpage. Seethestyleexamplefordetails.
authoryear-icomp A style combining authoryear-comp and authoryear-ibid. The style will set the Styleexample:
followingpackageoptionsatloadtime: autocite=inline,labeldateparts=true, local,online.
uniquename=full,uniquelist=true,ibidtracker=constrict,pagetracker=true,
sortcites=true. This style also provides an additional preamble option called
ibidpage. Seethestyleexamplefordetails.
authortitle This style implements a simple author-title citation scheme. It will make use of Styleexample:
the shorttitle field, if available. It is intended for citations given in footnotes. local,online.
Thestylewillsetthefollowingpackageoptionsatloadtime: autocite=footnote,
uniquename=full,uniquelist=true.
authortitle-comp A compact variant of the authortitle style which prints the author only once if Styleexample:
subsequentreferencespassedtoasinglecitationcommandsharethesameauthor. local,online.
Forexample,insteadof“Doe,Firsttitle;Doe,Secondtitle”thisstylewouldprint“Doe,
Firsttitle,Secondtitle”. Itisintendedforcitationsgiveninfootnotes. Thestylewillset
thefollowingpackageoptionsatloadtime: autocite=footnote,sortcites=true,
uniquename=full,uniquelist=true.
authortitle-ibid Avariantoftheauthortitlestylewhichreplacesrepeatedcitationsbytheabbre- Styleexample:
viation ibidem unless the citation is the first one on the current page or double- local,online.
pagespread,ortheibidemwouldbeambiguousinthesenseofthepackageoption
ibidtracker=constrict. Itisintendedforcitationsgiveninfootnotes. Thestylewill
setthefollowingpackageoptionsatloadtime: autocite=footnote,uniquename=
full, uniquelist=true, ibidtracker=constrict, pagetracker=true. This style
alsoprovidesanadditionalpreambleoptioncalledibidpage. Seethestyleexample
fordetails.
authortitle-icomp Astylecombiningthefeaturesofauthortitle-compandauthortitle-ibid. The Styleexample:
style will set the following package options at load time: autocite=footnote, local,online.
uniquename=full,uniquelist=true,ibidtracker=constrict,pagetracker=true,
sortcites=true. This style also provides an additional preamble option called
ibidpage. Seethestyleexamplefordetails.
authortitle-terse Atersevariantoftheauthortitlestylewhichonlyprintsthetitleifthebibliography Styleexample:
local,online.
76

containsmorethanoneworkbytherespectiveauthor/editor. Thisstylewillmake
useoftheshorttitlefield,ifavailable. Itissuitableforin-textcitationsaswellas
citationsgiveninfootnotes. Thestylewillsetthefollowingpackageoptionsatload
time: autocite=inline,singletitle=true,uniquename=full,uniquelist=true.
authortitle-tcomp Astylecombiningthefeaturesofauthortitle-compandauthortitle-terse. This Styleexample:
style will make use of the shorttitle field, if available. It is suitable for in-text local,online.
citations as well as citations given in footnotes. The style will set the following
package options at load time: autocite=inline, sortcites=true, singletitle=
true,uniquename=full,uniquelist=true.
authortitle-ticomp Astylecombiningthefeaturesofauthortitle-icompandauthortitle-terse. In Styleexample:
otherwords: avariantoftheauthortitle-tcompstylewithanibidemfeature. This local,online.
styleissuitableforin-textcitationsaswellascitationsgiveninfootnotes. Itwill
set the following package options at load time: autocite=inline, ibidtracker=
constrict,pagetracker=true,sortcites=true,singletitle=true,uniquename=
full,uniquelist=true. Thisstylealsoprovidesanadditionalpreambleoptioncalled
ibidpage. Seethestyleexamplefordetails.
verbose Averbosecitationstylewhichprintsafullcitationsimilartoabibliographyentry Styleexample:
whenanentryiscitedforthefirsttime,andashortcitationafterwards. Ifavailable, local,online.
theshorttitlefieldisusedinallshortcitations. Iftheshorthandfieldisdefined,
the shorthand is introduced on the first citation and used as the short citation
thereafter. Thisstylemaybeusedwithoutalistofreferencesandshorthandssince
all bibliographic data is provided on the first citation. It is intended for citations
given in footnotes. The style will set the following package options at load time:
autocite=footnote,citetracker=context. Thisstylealsoprovidesanadditional
preambleoptioncalledcitepages. Seethestyleexamplefordetails.
verbose-ibid Avariantoftheverbosestylewhichreplacesrepeatedcitationsbytheabbreviation Styleexample:
ibidemunlessthecitationisthefirstoneonthecurrentpageordouble-pagespread, local,online.
ortheibidemwouldbeambiguousinthesenseofibidtracker=strict. Thisstyle
isintendedforcitationsgiveninfootnotes. Thestylewillsetthefollowingpackage
options at load time: autocite=footnote, citetracker=context, ibidtracker=
constrict,pagetracker=true. Thisstylealsoprovidesadditionalpreambleoptions
calledibidpageandcitepages. Seethestyleexamplefordetails.
verbose-note This style is similar to the verbose style in that it prints a full citation similar to Styleexample:
abibliographyentrywhenanentryiscitedforthefirsttime,andashortcitation local,online.
afterwards. In contrast to the verbose style, the short citation is a pointer to the
footnote with the full citation. If the bibliography contains more than one work
bytherespectiveauthor/editor,thepointeralsoincludesthetitle. Ifavailable,the
shorttitle field is used in all short citations. If the shorthand field is defined,
it is handled as with the verbose style. This style may be used without a list of
referencesandshorthandssinceallbibliographicdataisprovidedonthefirstcitation.
It is exclusively intended for citations given in footnotes. The style will set the
followingpackageoptionsatloadtime: autocite=footnote,citetracker=context,
singletitle=true. This style also provides additional preamble options called
pagerefandcitepages. Seethestyleexamplefordetails.
verbose-inote Avariantoftheverbose-notestylewhichreplacesrepeatedcitationsbytheabbre- Styleexample:
viationibidemunlessthecitationisthefirstoneonthecurrentpageordouble-page local,online.
spread, or the ibidem would be ambiguous in the sense of ibidtracker=strict.
This style is exclusively intended for citations given in footnotes. It will set the
77

followingpackageoptionsatloadtime: autocite=footnote,citetracker=context,
ibidtracker=constrict, singletitle=true, pagetracker=true. This style also
providesadditionalpreambleoptionscalledibidpage,pageref,andcitepages. See
thestyleexamplefordetails.
verbose-trad1 This style implements a traditional citation scheme. It is similar to the verbose Styleexample:
style in that it prints a full citation similar to a bibliography entry when an item local,online.
iscitedforthefirsttime,andashortcitationafterwards. Apartfromthat,ituses
thescholarlyabbreviationsibidem, idem, op.cit., andloc.cit. toreplacerecurrent
authors, titles, and page numbers in repeated citations in a special way. If the
shorthandfieldisdefined,theshorthandisintroducedonthefirstcitationandused
astheshortcitationthereafter. Thisstylemaybeusedwithoutalistofreferences
and shorthands since all bibliographic data is provided on the first citation. It is
intendedforcitationsgiveninfootnotes. Thestylewillsetthefollowingpackage
options at load time: autocite=footnote, citetracker=context, ibidtracker=
constrict, idemtracker=constrict, opcittracker=context, loccittracker=
context. This style also provides additional preamble options called ibidpage,
strict,andcitepages. Seethestyleexamplefordetails.
verbose-trad2 Anothertraditionalcitationscheme. Itisalsosimilartotheverbosestylebutuses Styleexample:
scholarlyabbreviationslikeibidemandideminrepeatedcitations. Incontrasttothe local,online.
verbose-trad1style,thelogicoftheop.cit. abbreviationsisdifferentinthisstyle
andloc.cit. isnotusedatall. Itisinfactmoresimilartoverbose-ibidandverbose-
inotethantoverbose-trad1. Thestylewillsetthefollowingpackageoptionsat
load time: autocite=footnote, citetracker=context, ibidtracker=constrict,
idemtracker=constrict. Thisstylealsoprovidesadditionalpreambleoptionscalled
ibidpage,strict,andcitepages. Seethestyleexamplefordetails.
verbose-trad3 Yet another traditional citation scheme. It is similar to the verbose-trad2 style Styleexample:
butusesthescholarlyabbreviationsibidem andop.cit. inaslightlydifferentway. local,online.
Thestylewillsetthefollowingpackageoptionsatloadtime: autocite=footnote,
citetracker=context, ibidtracker=constrict, loccittracker=constrict. This
stylealsoprovidesadditionalpreambleoptionscalledstrictandcitepages. See
thestyleexamplefordetails.
reading Acitationstylewhichgoeswiththebibliographystylebythesamename. Itsimply Styleexample:
loadstheauthortitlestyle. local,online.
Thefollowingcitationstylesarespecialpurposestyles. Theyarenotintendedfor
thefinalversionofadocument:
draft Adraftstylewhichusestheentrykeysincitations. Thestylewillsetthefollowing Styleexample:
packageoptionsatloadtime: autocite=plain. local,online.
debug This style prints the entry key rather than some kind of label. It is intended for Styleexample:
debuggingonlyandwillsetthefollowingpackageoptionsatloadtime: autocite= local,online.
plain.
3.3.2 BibliographyStyles
All bibliography styles which come with this package use the same basic format
fortheindividualbibliographyentries. Theyonlydifferinthekindoflabelprinted
inthebibliographyandtheoverallformattingofthelistofreferences. Thereisa
matchingbibliographystyleforeverycitationstyle. Notethatsomebibliography
78

stylesarenotmentionedbelowbecausetheysimplyloadamoregenericstyle. For
example,thebibliographystyleauthortitle-compwillloadtheauthortitlestyle.
numeric Thisstyleprintsanumericlabelsimilartothestandardbibliographicfacilitiesof Styleexample:
LaTeX.Itisintendedforuseinconjunctionwithanumericcitationstyle. Notethatthe local,online.
shorthandfieldoverridesthedefaultlabel. Thestylewillsetthefollowingpackage
options at load time: labelnumber=true. This style also provides an additional
preambleoptioncalledsubentrywhichaffectstheformattingofentrysets. Ifthis
optionisenabled,allmembersofasetaremarkedwithaletterwhichmaybeusedin
citationsreferringtoasetmemberratherthantheentireset. Seethestyleexample
fordetails.
alphabetic This style prints an alphabetic label similar to the alpha.bst style of traditional Styleexample:
BibTeX.Itisintendedforuseinconjunctionwithanalphabeticcitationstyle. Note local,online.
thattheshorthandfieldoverridesthedefaultlabel. Thestylewillsetthefollowing
packageoptionsatloadtime: labelalpha=true,sorting=anyt.
authoryear This style differs from the other styles in that the publication date is not printed Styleexample:
towards the end of the entry but rather after the author/editor. It is intended for local,online.
useinconjunctionwithanauthor-yearcitationstyle. Recurringauthorandeditor
namesarereplacedbyadashunlesstheentryisthefirstoneonthecurrentpageor
double-pagespread. Thisstyleprovidesanadditionalpreambleoptioncalleddashed
whichcontrolsthisfeature. Italsoprovidedapreambleoptioncalledmergedate. See
thestyleexamplefordetails. Thestylewillsetthefollowingpackageoptionsatload
time: labeldateparts=true,sorting=nyt,pagetracker=true,mergedate=true.
authortitle Thisstyledoesnotprintanylabelatall. Itisintendedforuseinconjunctionwith Styleexample:
anauthor-titlecitationstyle. Recurringauthorandeditornamesarereplacedbya local,online.
dashunlesstheentryisthefirstoneonthecurrentpageordouble-pagespread. This
stylealsoprovidesanadditionalpreambleoptioncalleddashedwhichcontrolsthis
feature. Seethestyleexamplefordetails. Thestylewillsetthefollowingpackage
optionsatloadtime: pagetracker=true.
verbose Thisstyleissimilartotheauthortitlestyle. Italsoprovidesanadditionalpreamble Styleexample:
optioncalleddashed. Seethestyleexamplefordetails. Thestylewillsetthefollowing local,online.
packageoptionsatloadtime: pagetracker=true.
reading This special bibliography style is designed for personal reading lists, annotated Styleexample:
bibliographies,andsimilarapplications. Itoptionallyincludesthefieldsannotation, local,online.
abstract, library, and file in the bibliography. If desired, it also adds various
kindsofshortheaderstothebibliography. Thisstylealsoprovidestheadditional
preambleoptionsentryhead,entrykey,annotation,abstract,library,andfile
whichcontrolwhetherornotthecorrespondingitemsareprintedinthebibliography.
Seethestyleexamplefordetails. Seealso§3.14.8. Thestylewillsetthefollowing
package options at load time: loadfiles=true, entryhead=true, entrykey=true,
annotation=true,abstract=true,library=true,file=true.
Thefollowingbibliographystylesarespecialpurposestyles. Theyarenotintended
forthefinalversionofadocument:
draft Thisdraftstyleincludestheentrykeysinthebibliography. Thebibliographywillbe Styleexample:
sortedbyentrykey. Thestylewillsetthefollowingpackageoptionsatloadtime: local,online.
sorting=debug.
debug Thisstyleprintsallbibliographicdataintabularformat. Itisintendedfordebugging Styleexample:
onlyandwillsetthefollowingpackageoptionsatloadtime: sorting=debug. local,online.
79

3.4 ExtendedNameFormat
The parsing rules for BibTeX names are rather archaic and not suited to many
internationalnameformats. bibersupportsanextendednameformatwhichallows
explicitspecificationofthepartsofnames. Thisallowstheuseofcustomnameparts
apartfromthefourstandardBibTeXparts. Extendednameformatsaresupportedin
allnamefieldsandcanbeusedalongwiththeusualBibTeXnameformat. Recognition
ofextendednameformatcanbedisabledwiththebiberoption--noxnameincase
youdonotneedtheextendedformatandtheauto-detectioncausesproblemswith
normalnameparsing. Theseparator=whichcomesbetweenthenamepartnames
andvaluesiscustomisablewiththebiberoption--xnamesep. Hereisanexample:
| AUTHOR | = {Hans | Harman | and | Simon de | Beumont} |     |     |
| ------ | ------- | ------ | --- | -------- | -------- | --- | --- |
AUTHOR = {given=Hans, family=Harman and given=Simon, prefix=de, family
,→
=Beumont}
These two name specifications are equivalent but the extended format explicitly
namestheparts. Thesupportedpartsarethosespecifiedbythebiblatexdatamode
constantnameparts,see§4.2.3. AswithtraditionalBibTeXnameparsing,initials
areautomaticallygeneratedbutitisalsopossibletospecifytheseexplicitly:
| AUTHOR | = {given=Jean, |     | prefix=de | la,     | prefix-i=d,  |     | family=Rousse} |
| ------ | -------------- | --- | --------- | ------- | ------------ | --- | -------------- |
| AUTHOR | = {given={Jean |     | Pierre    | Simon}, | given-i=JPS} |     |                |
Initialsarespecifiedbyaddingthesuffix-itothenamepartname. Compoundparts
maybeprotectedwithbraces:
| AUTHOR | = {given={Jean |     | Pierre}} |     |     |     |     |
| ------ | -------------- | --- | -------- | --- | --- | --- | --- |
If a namepart contains a comma, the whole namepart should be protected with
quotes:
| AUTHOR | = {"family={Robert |     |     | and Sons, | Inc.}"} |     |     |
| ------ | ------------------ | --- | --- | --------- | ------- | --- | --- |
TraditionalBibTeXnameformatsandtheextendedformmaybeusedtogether:
AUTHOR = {Hans Harman and given=Simon, prefix=de, family=Beumont}
Per-namelistandper-nameoptionsmaybespecifiedintheextendednameformat,
see§3.1.3.1:
| AUTHOR | = {nosortothers=true |     |                 | and Hans | Harman     | and |                 |
| ------ | -------------------- | --- | --------------- | -------- | ---------- | --- | --------------- |
|        | given=Simon,         |     | family=Beumont, |          | prefix=de, |     | useprefix=true} |
hidi
A special parameter may also be used for any name and this will be used to
overridethehashusedtodetectidenticalnames,forexample,agenderchangecould
behandledlikethis(seealso§4.11.5):
| AUTHOR | = {id=person1, |     | given=Simon,  |     | family=Beumont} |     |     |
| ------ | -------------- | --- | ------------- | --- | --------------- | --- | --- |
| AUTHOR | = {id=person1, |     | given=Simone, |     | family=Beumont} |     |     |
80

3.5 RelatedEntries
Almostallbibliographystylesrequireauthorstospecifycertaintypesofrelationship
betweenentriessuchas“Reprintof”,“Reprintedin”etc. Itisimpossibletoprovide
data fields to cover all of these relationships and so biblatex provides a general
mechanismforthisusingtheentryfieldsrelated,relatedtypeandrelatedstring.
Arelatedentrydoesnotneedtobecitedanddoesnotappearinthebibliography
itself(unlessofcourseitisalsociteditselfindependently)asacloneistakenofthe
relatedentrytobeusedasadatasource. Therelatedtypefieldspecifiesthetype
ofrelationbetweenthecurrentandtherelatedentry. Itcanselectatype-specific
bibliographymacrotoprinttherelatedentriesandwilloftenalsobealocalisation
stringwhichwillbeprintedbeforetheinformationfromtherelatedentriesisprinted,
forexample“Orig. Pub. as”. Therelatedstringfieldcanbeusedtooverridethe
stringdeterminedviarelatedtype. Someexamples:
@Book{key1,
...
related = {key2},
relatedtype = {reprintof},
...
}
@Book{key2,
...
}
Herewespecifythatentrykey1isareprintofentrykey2. Inthebibliographydriver
forBookentries,when\usebibmacro{related}iscalledforentrykey1:
• If the localisation string “reprintof” is defined, it is printed in the
relatedstring:reprintofformat. Ifthisformattingdirectiveisundefined,
thestringisprintedintherelatedstring:defaultformat.
• Iftherelated:reprintofmacroisdefined,itisusedtoformattheinformation
containedinentrykey2,otherwisetherelated:defaultmacroisused
• If the related:reprintof format is defined, it is used to format both the
localisation string and data. If this format is not defined, then the related
formatisusedinstead.
Itisalsosupportedtohavecascadingand/orcircularrelations:
@Book{key1,
...
related = {key2},
relatedtype = {reprintof},
...
}
@Book{key2,
...
related = {key3},
relatedtype = {translationof},
81

...
}
@Book{key3,
...
related = {key2},
relatedtype = {translationas},
...
}
Multiplerelationstothesameentryarealsopossible:
@MVBook{key1,
...
related = {key2,key3},
relatedtype = {multivolume},
...
}
@Book{key2,
...
}
@Book{key3,
...
}
Notetheorderofthekeysinlistsofmultiplerelatedentriesisimportant. Thedata
frommultiplerelatedentriesisprintedintheorderofthekeyslistedinthisfield.
See§4.5.1foramoredetailsonthemechanismsbehindthisfeature. Youcanturn
thisfeatureoffusingthepackageoptionrelatedfrom§3.1.2.1.
You can use the relatedoptions to set options on the related entry data clone.
This is useful if you need to override the dataonly option which is set by de-
fault on all related entry clones. For example, if you will expose some of the
names in the related clone in your document, you may want to have them dis-
ambiguatedfromnamesinotherentriesbutnormallythiswon’thappenasrelated
clones have the per-entry dataonly option set and this in turn sets uniquename=
falseanduniquelist=false. Insuchacase, youcansetrelatedoptionstojust
skiplab, skipbib, skipbiblist.
3.6 SortingOptions
Thispackagesupportsfullycustomisablesortingtemplatesforthebibliography. The
default global sorting template is selected with the sorting package option from
§3.1.2.1. Apartfromtheregulardatafieldstherearealsosomespecialfieldswhich
maybeusedtooptimizethesortingofthebibliography. AppendicesC.1andC.2
giveanoutlineofthedefaultalphabeticsortingtemplatessupportedbybiblatex.
Chronological sorting templates are listed in appendix C.3. A few explanations
concerningthedefaulttemplatesareinorder.
The first item considered in the sorting process is always the presort field of
the entry. If this field is undefined, biblatex will use the default value ‘mm’ as a
presortstring. Thenextitemconsideredisthesortkeyfield. Ifthisfieldisdefined,
82

it serves as the master sort key. Apart from the presort field, no further data is
consideredinthiscase. Ifthesortkeyfieldisundefined,sortingcontinueswiththe
name. The package will try using the sortname, author, editor, and translator
fields,inthisorder. Whichfieldsareconsideredalsodependsonthesettingofthe
use<name>options. Ifallsuchoptionsaredisabled,thesortnamefieldisignored
as well. Note that all name fields are responsive to maxnames and minnames. If
nonamefieldisavailable,eitherbecauseallofthemareundefinedorbecauseall
use<name>optionsaredisabled,biblatexwillfallbacktothesorttitleandtitle
fieldsasalastresort. Theremainingitemsare,invariousorder: thesortyearfield,
if defined, or the first four digits of the year field otherwise; the sorttitle field,
if defined, or the title field otherwise; the volume field. Note that the sorting
templatesshowninappendixC.2includeanadditionalitem: labelalphaisthelabel
usedby‘alphabetic’bibliographystyles. Strictlyspeaking,thestringusedforsorting
islabelalpha+extraalpha. ThesortingtemplatesinappendixC.2areintendedto
beusedinconjunctionwithalphabeticstylesonly.
ThechronologicalsortingtemplatespresentedinappendixC.3alsomakeuseof
thepresortandsortkeyfields,ifdefined. Thenextitemconsideredisthesortyear
ortheyearfield,dependingonavailability. Theynttemplateextractsthefirstfour
Arabicfiguresfromthefield. Ifbothfieldsareundefined,thestring9999isusedasa
fallbackvalue. Thismeansthatallentrieswithoutayearwillbemovedtotheendof
thelist. Theydnttemplateissimilarinconceptbutsortstheyearindescendingorder.
Aswiththeynttemplate,thestring9999isusedasafallbackvalue. Theremaining
itemsaresimilartothealphabeticsortingtemplatesdiscussedabove. Notethatthe
ydntsortingtemplatewillonlysortthedateindescendingorder. Allotheritems
aresortedinascendingorderasusual.
Mostbuilt-insortingtemplateshaveavariantwhichsortsonalloftheavailable
partsofafullISO8601daterightdowntosecondsinsteadofonlytheyear,see§3.1.2.
Using special fields such as sortkey, sortname, or sorttitle is usually not re-
quired. Thebiblatexpackageisquitecapableofworkingoutthedesiredsorting
orderbyusingthedatafoundintheregularfieldsofanentry. Youwillonlyneed
themifyouwanttomanuallymodifythesortingorderofthebibliographyorifany
datarequiredforsortingismissing. Pleaserefertothefielddescriptionsin§2.2.3
fordetailsonpossibleusesofthespecialfields.
3.7 DataAnnotations
Ideally,thereshouldbenoformattinginformationinabibliographydatafile,how-
ever, sometimes such questionable practice seems to the only way in which the
desiredresultscanbeachieved. Dataannotationsareawayofaddressingthisby
allowinguserstoattachsemanticinformation(ratherthantypographicalmarkup)
toinformationinabibliographydatasourcesothattheinformationcanbeusedat
markuptimebyastyle. Forexample,ifyouwantedtohighlightcertainnamesina
workdependingonwhethertheywereastudentauthor(indicatedbyasuperscript
asteriskinthereferences)oracorrespondingauthor(indicatedbyboldface),then
youmightbetemptedtotry:
@MISC{Article1,
AUTHOR = {Last1\textsuperscript{*}, First1 and \textbf{Last2}, \
,→ textbf{First2} and Last3, First3}
}
83

There are several problems with this. Firstly, it will break BibTeX’s fragile name
parsingroutinesandprobablywon’tcompileatall. Secondly,itisnotonlymixing
updatawithmarkup,itdoessoinahard-codedway: thisdatacan’teasilybeshared
and used with other styles. While it is possible to achieve this formatting using
biblatexinternalsinastyleordocument,thisisacomplexandunreliablemethod
whichmanyuserswillnotwishtouse.
Inordertoaddresstheseissues,biblatexhasageneraldataannotationfacility
whichallowsyoutoattachanynumberofacomma-separatedlistofannotationsto
datafields,itemswithindatafieldlists(likenames)andevenpartsofspecificitems
suchaspartsofnames(givenname,familynameetc.). Therearemacrosprovidedto
checkforannotationswhichcanbeusedinformattingdirectives.
Therearethree“scopes”fordataannotations,inorderofincreasingspecificity:
• field—appliedtotop-levelfieldsinadatasourceentry
• item—appliedtoitemswithinalistfieldinadatasourceentry
• part—appliedtopartswithinitemswithinalistfieldinadatasourceentry
DataannotationsaresupportedforBibTeXandbiblatexmldatasources.
@MISC{ann1,
| AUTHOR | = {Last1, | First1 and | Last2, First2 | and Last3, |
| ------ | --------- | ---------- | ------------- | ---------- |
,→ First3},
| AUTHOR+an        | = {1:family=student;2=corresponding}, |          |     |     |
| ---------------- | ------------------------------------- | -------- | --- | --- |
| TITLE            | = {The                                | Title},  |     |     |
| TITLE+an:default | = {=titleannotation},                 |          |     |     |
| TITLE+an:french  | = {="Le                               | titre"}, |     |     |
| TITLE+an:german  | = {="Der                              | Titel"}, |     |     |
}
Herethefieldnamesuffix+anisauser-definable20 suffixwhichmarksadatafield
asanannotationoftheunsuffixedfield. Multipleannotationscanbeprovidedfor
the same field since all annotations are named. After the annotation marker is
the optional named annotation marker 21 and an optional annotation name. The
annotationnameis‘default’ifnotspecifiedandsointheaboveexamplethefollowing
twoareequivalent:
| TITLE+an         | = {=titleannotation}, |     |     |     |
| ---------------- | --------------------- | --- | --- | --- |
| TITLE+an:default | = {=titleannotation}, |     |     |     |
TheformatofannotationfieldsinBibTeXdatasourcesisisasfollows:
<annotationspecs> ::= <annotationspec> [ ";" <annotationspec> ]
<annotationspec> ::= [ <itemcount> [ ":" <part> ] ] "=" <annotations>
| <annotations> | ::= <annotation> | [            | "," <annotation> | ]   |
| ------------- | ---------------- | ------------ | ---------------- | --- |
| <annotation>  | ::= ["]          | (string) ["] |                  |     |
Thatis,oneormorespecificationsseparatedbysemicolons. Eachspecificationisan
equalssignfollowedbyacomma-separatedlistofannotationkeywordsorastring
20Seebiber’s--annotation-markeroption.
21Seebiber’s--named-annotation-markeroption.
84

enclosedindouble-quotes(a‘literal’annotation,seebelow). Toannotateaspecific
iteminalist,putthenumberofthelistitembeforetheequalssign(listsstartat1). If
youneedtoannotateaspecificpartofthelistitem,giveitsnameafterthelistitem
number,precededbyacolon. Namepartnamesaredefinedinthedatamodel,see
§4.2.3. Somefurtherexamples:
AUTHOR = {Last1, First1 and Last2, First2 and Last3, First3},
| AUTHOR+an   |     | = {3:given=annotation1, |             |                | annotation2}, |              |
| ----------- | --- | ----------------------- | ----------- | -------------- | ------------- | ------------ |
| TITLE       |     | = {A title},            |             |                |               |              |
| TITLE+an    |     | = {=a title             | annotation, |                | another title | annotation}, |
| LANGUAGE    |     | = {english              | and         | french},       |               |              |
| LANGUAGE+an |     | = {1=annotation3;       |             | 2=annotation4} |               |              |
}
Attaching annotations to data is similar in data sources. Using the
biblatexml
exampleabove,wewouldhave:
<bltx:entries xmlns:bltx="http://biblatex-biber.sourceforge.net/
,→
biblatexml">
| <bltx:entry |     | id="test"      | entrytype="misc"> |     |     |     |
| ----------- | --- | -------------- | ----------------- | --- | --- | --- |
| <bltx:names |     | type="author"> |                   |     |     |     |
<bltx:name>
|     | <bltx:namepart |     | type="given"  |     | initial="F">First1</bltx:namepart> |     |
| --- | -------------- | --- | ------------- | --- | ---------------------------------- | --- |
|     | <bltx:namepart |     | type="family" |     | initial="L">Last1</bltx:namepart>  |     |
</bltx:name>
<bltx:name>
|     | <bltx:namepart |     | type="given"  |     | initial="F">First2</bltx:namepart> |     |
| --- | -------------- | --- | ------------- | --- | ---------------------------------- | --- |
|     | <bltx:namepart |     | type="family" |     | initial="L">Last2</bltx:namepart>  |     |
</bltx:name>
<bltx:name>
|     | <bltx:namepart |     | type="given"  |     | initial="F">First3</bltx:namepart> |     |
| --- | -------------- | --- | ------------- | --- | ---------------------------------- | --- |
|     | <bltx:namepart |     | type="family" |     | initial="L">Last3</bltx:namepart>  |     |
</bltx:name>
</bltx:names>
</bltx:annotation field="author" item="1" part="family">student</
,→
bltx:annotation>
| </bltx:annotation |     |     | field="author" |     | item="2">corresponding</ |     |
| ----------------- | --- | --- | -------------- | --- | ------------------------ | --- |
,→ bltx:annotation>
</bltx:entry>
</bltx:entries>
Toaccesstheannotationinformationwhenformattingbibliographydata,macros
areprovided,correspondingtothethreeannotationscopes:
\iffieldannotation[hfieldi][hannotationnamei]{hannotationi}{htruei}{hfalsei}
Executes htruei if the data field hfieldi has an annotation hannotationi for the an-
notation called hannotationnamei and false otherwise. If hannotationnamei is not
given, then the annotation named ‘default’ is assumed (this is the name given to
annotationsdefinedwithoutanexplicitname). Ifhfieldiisnotgiven,thecurrentdata
fieldasindicatedby\currentfield,\currentlistor\currentname(see§4.4.2)is
assumed. Of course, this is only possible if these commands are defined, that is,
insideformattingdirectives.
85

\ifitemannotation[hfieldi][hannotationnamei][hitemi]{hannotationi}{htruei}{hfalsei}
Executes htruei if the item hitemi in the data field hfieldi has an annotation
hannotationi and false otherwise. If hannotationnamei is not given, then the an-
notationnamed‘default’isassumed(thisisthenamegiventoannotationsdefined
without an explicit name). The optional argument hfieldi can be inferred if not
providedaswith\iffieldannotation. Ifhitemiisnotgiven,thenumberoftheitem
currentlybeingprocessedasgivenbylistcountisused.
\ifpartannotation[hfieldi][hannotationnamei][hitemi]{hparti}{hannotationi}{htruei}{hfalsei}
Executeshtrueiifthepartnamedhpartiinitemhitemiinthedatafieldhfieldihasan
annotationhannotationiandfalseotherwise. Ifhannotationnameiisnotgiven,then
theannotationnamed‘default’isassumed(thisisthenamegiventoannotations
definedwithoutanexplicitname). Thetwooptionalargumentshfieldiandhitemican
beinferredasin\ifitemannotation. Theparameterhparticanneverbeinferred
andisthereforeamandatoryargument.
Datefieldsarespecialandhandledinacontextwhere\currentfieldisnotaccessible.
Thusthereisafourthcommandtotestannotationsfordates.
\ifdateannotation[hannotationnamei]{hdatetypei}{hannotationi}{htruei}{hfalsei}
Executeshtrueiifthedatefieldhdatetypeihasanannotationhannotationiandfalse
otherwise. Ifhannotationnameiisnotgiven,thentheannotationnamed‘default’is
assumed(thisisthenamegiventoannotationsdefinedwithoutanexplicitname).
Thehdatetypeiargumentismandatory,becauseitcannotbeinferredinmostcontexts
where\ifdateannotationwillbeused.
\hasfieldannotation[hfieldi][hannotationnamei]{htruei}{hfalsei}
Executes htruei if the data field hfieldi has a literal annotation hannotationnamei
definedandfalseotherwise. Ifhannotationnameiisnotgiven,thentheannotation
named ‘default’ is assumed (this is the name given to annotations defined with-
outanexplicitname). Ifhfieldiisnotgiven,thecurrentdatafieldasindicatedby
\currentfield,\currentlistor\currentname(see§4.4.2)isassumed. Ofcourse,
thisisonlypossibleifthesecommandsaredefined,thatis,insideformattingdirec-
tives.
\hasitemannotation[hfieldi][hannotationnamei][hitemi]{htruei}{hfalsei}
Executes htruei if the item hitemi in the data field hfieldi has a literal annotation
hannotationnameidefinedandfalseotherwise. Ifhannotationnameiisnotgiven,then
theannotationnamed‘default’isassumed(thisisthenamegiventoannotations
definedwithoutanexplicitname). Theoptionalargumenthfieldicanbeinferredif
notprovidedaswith\iffieldannotation. Ifhitemiisnotgiven,thenumberofthe
itemcurrentlybeingprocessedasgivenbylistcountisused.
\haspartannotation[hfieldi][hannotationnamei][hitemi]{hparti}{htruei}{hfalsei}
Executes htruei if the part named hparti in the item hitemi in the data field
hfieldi has a literal annotation hannotationnamei defined and false otherwise. If
hannotationnameiisnotgiven,thentheannotationnamed‘default’isassumed(this
is the name given to annotations defined without an explicit name). The two op-
tionalargumentshfieldiandhitemicanbeinferredasin\ifitemannotation. The
parameterhparticanneverbeinferredandisthereforeamandatoryargument.
86

Datefieldsarespecialandhandledinacontextwhere\currentfieldisnotaccessible.
Thusthereisafourthcommandtotesttheexistenceofannotationsfordates.
\hasdateannotation[hannotationnamei]{hdatetypei}{htruei}{hfalsei}
Executes htruei if the date field hdatetypei has any annotation hannotationnamei
definedandfalseotherwise. Ifhannotationnameiisnotgiven,thentheannotation
named‘default’isassumed(thisisthenamegiventoannotationsdefinedwithoutan
explicitname). Thehdatetypeiargumentismandatory,becauseitcannotbeinferred
inmostcontextswhere\ifdateannotationwillbeused.
As an example of how to use the annotation information to solve the problem
originally presented in this section, this could be used in the name formatting
directivestoputanasteriskafterallfamilynamesannotatedas“student”:
\ifpartannotation{family}{student}
{\textsuperscript{*}}
{}%
Toputthegivenandfamilynamesofnamelistitemsannotatedas“corresponding”
inboldface:
\renewcommand*{\mkbibnamegiven}[1]{%
\ifitemannotation{corresponding}
{\textbf{#1}}
{#1}}
\renewcommand*{\mkbibnamefamily}[1]{%
\ifitemannotation{corresponding}
{\textbf{#1}}
{#1}}
3.7.1 LiteralAnnotations
Iftheannotationisastringenclosedindouble-quotes,theannotationisa‘literal’
annotation. Inthiscasetheannotationcanberetrievedandusedasastringrather
thanasmeta-informationusedtodetermineformatting. Thisisusefulinorderto
beabletoattachedspecificannotationstodatawhicharetobeprintedas-is. For
example:
AUTHOR = {{American Educational Research Association} and {American
,→ Psychological Association}
and {National Council on Measurement in Education}},
AUTHOR+an = {1:family="AERA"; 2:family="APA"; 3:family="NCME"}
}
Suchannotationsarenotkeyswhosepresencecanbetestedforbutareratherliteral
informationattachedtothedata. Thevaluesareretrievedbythefollowingmacros
\getfieldannotation[hfieldi][hannotationnamei]
Retrieves any literal annotation for the field hfieldi. If hannotationnamei is not
given, then the annotation named ‘default’ is assumed (this is the name given to
87

annotationsdefinedwithoutanexplicitname). Ifhfieldiisnotgiven,thecurrentdata
fieldasindicatedby\currentfield,\currentlistor\currentname(see§4.4.2)is
assumed. Of course, this is only possible if these commands are defined, that is,
insideformattingdirectives.
\getitemannotation[hfieldi][hannotationnamei][hitemi]
Retrieves any literal annotation for the item hitemi in the field hfieldi. If
hannotationnameiisnotgiven,thentheannotationnamed‘default’isassumed(this
isthenamegiventoannotationsdefinedwithoutanexplicitname). Theoptional
argumenthfieldicanbeinferredifnotprovidedaswith\getfieldannotation. If
hitemiisnotgiven,thenumberoftheitemcurrentlybeingprocessedasgivenby
listcountisused.
\getpartannotation[hfieldi][hannotationnamei][hitemi]{hparti}
Retrievesanyliteralannotationfortheparthparti. Ifhannotationnameiisnotgiven,
thentheannotationnamed‘default’isassumed(thisisthenamegiventoannotations
definedwithoutanexplicitname). Thetwooptionalargumentshfieldiandhitemican
beinferredasin\getitemannotation. Theparameterhparticanneverbeinferred
andisthereforeamandatoryargument.
Datefieldsarespecialandhandledinacontextwhere\currentfieldisnotaccessible.
Thusthereisafourthcommandtoaccessliteralannotationsfordates.
\getdateannotation[hannotationnamei]{hdatetypei}
Retrievealiteralannotationforthedatefieldhdatetypei. Ifhannotationnameiisnot
given,thentheannotationnamed‘default’isassumed(thisisthenamegiventoan-
notationsdefinedwithoutanexplicitname). Thehdatetypeiargumentismandatory,
becauseitcannotbeinferredinmostcontextswhere\getdateannotationwillbe
used.
So,forexample,giventhebibliographyentryabove,wecouldputthefollowingin
thepreamble:
\renewcommand*{\mkbibnamefamily}[1]{%
#1\space\mkbibparens{\getpartannotation{family}}}
Inordertogetsomethinglikethisinthebibliographywhenformattingnames:
American Educational Research Association (AERA) and
American Psychological Association (APA), and
National Council on Measurement in Education (NCME)
}
Naturallytherearesemanticallymoreelegantwaysofdealingwithcorporateauthors
withoutusingthe‘family’namepart(see§4.2.3)butthisexampledemonstratesclearly
auseforliteralannotations.
88

3.8 BibliographyCommands
3.8.1 Resources
\addbibresource[hoptionsi]{hresourcei}
Addsahresourcei,suchasa.bibfile,tothedefaultresourcelist. Thiscommandis
onlyavailableinthepreamble. Itreplacesthe\bibliographylegacycommand. Note
thatfilesmustbespecifiedwiththeirfullname,includingtheextension. Withbiber,
the resource name can be a BSD-style glob pattern. This only makes sense when
resourcesrefertofileswithanabsoluteorrelativepathanddoesnotworkwhen
looking for data resources in biber s input/output directories or with resources
located by hkpsewhichi etc. When running on Windows, biber will switch to a
Windows compatible globbing mode where backslashes are also usable as path
separators and case does not matter. If the resources contain duplicate entries
(that is, duplicate entrykeys), it is backend dependent what then happens. For
example, by default biber will ignore further occurrence of entrykeys unless its
--noskipduplicatesoptionsisused. Invoke\addbibresourcemultipletimestoadd
moreresources,forexample:
\addbibresource{bibfile1.bib}
\addbibresource{bibfile2.bib}
\addbibresource[glob]{bibfiles/bibfile*.bib}
\addbibresource[glob]{bibfile-num?.bib}
\addbibresource[glob]{bibfile{1,2,3}.bib}
\addbibresource[location=remote]{https://raw.githubusercontent.com/
,→ plk/biblatex/master/bibtex/bib/biblatex/biblatex-examples.bib}
\addbibresource[location=remote,label=lan]{ftp://192.168.1.57/~user/
,→ file.bib}
Sincethehresourceistringisreadinaverbatim-likemode,itmaycontainarbitrary
characters. The only restriction is that any curly braces must be balanced. The
followinghoptionsiareavailable:
bibencoding=hbibencodingi
Thisoptioncanbeusedtooverridetheglobalbibencodingoptionforaparticular
hresourcei.
label=hidentifieri
Assignsalabeltoaresource. Thehidentifierimaybeusedinplaceofthefullresource
name in the optional argument of refsection (see § 3.8.4). The label is a unique
identifierforthehresourcei,soeachlabelshouldonlybeusedonce.
location=hlocationi default:local
Thelocationoftheresource. Thehlocationimaybeeitherlocalforlocalresources
orremoteforurls. Remoteresourcesrequirebiber. Theprotocolshttp/httpsand
ftparesupported. Theremoteurlmustbeafullyqualifiedpathtoabibfileora
urlwhichreturnsabibfile.
type=htypei default:file
Thetypeofresource. Currently,theonlysupportedtypeisfile.
datatype=hdatatypei default:bibtex
Thedatatype(format)oftheresource. Thefollowingformatsarecurrentlysupported:
89

bibtex BibTeXformat.
biblatexml ExperimentalXMLformatforbiblatex. See§D.
glob=true,false
Whetherbibershouldglob(expandaccordingtopattern)thedatasourcename. There
isaglobalsettingforthisinbiber(falsebydefaultandsettabletotrueusingthe
--glob-datasourcesoption). Thisoptionallowsoverridingthebiberdefaultona
per-resourcebasis.
\addglobalbib[hoptionsi]{hresourcei}
Thiscommanddiffersfrom\addbibresourceinthatthehresourceiisaddedtothe
globalresourcelist. Thedifferencebetweendefaultresourcesandglobalresources
is only relevant if there are reference sections in the document and the optional
argument of refsection (§ 3.8.4) is used to specify alternative resources which
replace the default resource list. Any global resources are added to all reference
sections.
\addsectionbib[hoptionsi]{hresourcei}
Thiscommanddiffersfrom\addbibresourceinthattheresourcehoptionsiarereg-
istered but the hresourcei not added to any resourcelist. This is only required for
resourceswhich 1)aregivenexclusivelyin theoptional argumentof refsection
(§ 3.8.4) and 2) require options different from the default settings. In this case,
\addsectionbibisemployedtoqualifythehresourceipriortousingitbysettingthe
appropriatehoptionsiinthepreamble. Thelabeloptionmaybeusefultoassigna
shortnametotheresource.
\bibliography{hbibfile,…i}
Deprecated
Thelegacycommandforaddingbibliographicresources,supportedforbackwards
compatibility. Like\addbibresource,thiscommandisonlyavailableinthepreamble
andaddsresourcestothedefaultresourcelist. Itsargumentisacomma-separated
list of bib files. The .bib extension may be omitted from the filename. Invoking
this command multiple times to add more files is permissible. This command is
deprecated. Pleaseconsiderusing\addbibresourceinstead.
3.8.2 TheBibliography
\printbibliography[hkey=value,…i]
Thiscommandprintsthebibliography. Ittakesoneoptionalargument,whichisa
listofoptionsgiveninhkeyi=hvalueinotation. Thefollowingoptionsareavailable:
env=hnamei default:bibliography/shorthands
The‘high-level’layoutofthebibliographyandthelistofshorthandsiscontrolled
byenvironmentsdefinedwith\defbibenvironment. Thisoptionselectsanenviron-
ment. Thehnameicorrespondstotheidentifierusedwhendefiningtheenvironment
with\defbibenvironment. Bydefault,the\printbibliographycommandusesthe
identifierbibliography;\printbiblistusesshorthands. Seealso§§3.8.3and3.8.7.
90

heading=hnamei default:bibliography/shorthands
Thebibliographyandthelistofshorthandstypicallyhaveachapterorsectionheading.
Thisoptionselectstheheadinghnamei,asdefinedwith\defbibheading. Bydefault,
the\printbibliographycommandusestheheadingbibliography;\printbiblist
usesshorthands. Seealso§§3.8.3and3.8.7.
title=htexti
This option overrides the default title provided by the heading selected with the
headingoption,ifsupportedbytheheadingdefinition. See§3.8.7fordetails.
label=hlabeli
Ifhlabeliisnonempty,issue\label{hlabeli}aftertypesettingtheheading. Nosanity
checkingisdonewhetherornotitisusefultosetalabelaftertheheading(e.g.,if
theheadingisnotnumbereda\reftothelabelmightnotresultinusefuloutput).
block=none,space,par,nbpar,ragged default:globalsetting (none)
This option overrides the global block option (see § 3.1.2.1, the meaning of the
settingsisexplainedthereaswell).
prenote=hnamei
The prenote is an arbitrary piece of text to be printed after the heading but be-
forethelistofreferences. Thisoptionselectstheprenotehnamei,asdefinedwith
\defbibnote. Bydefault,noprenoteisprinted. Thenoteisprintedinthestandard
textfont. Itisnotaffectedby\bibsetupand\bibfontbutitmaycontainitsown
fontdeclarations. See§3.8.8fordetails.
postnote=hnamei
The postnote is an arbitrary piece of textto be printed after the list of references.
Thisoptionselectsthepostnotehnamei,asdefinedwith\defbibnote. Bydefault,
nopostnoteisprinted. Thenoteisprintedinthestandardtextfont. Itisnotaffected
by\bibsetupand\bibfontbutitmaycontainitsownfontdeclarations. See§3.8.8
fordetails.
Thefollowingoptionscanbeusedto‘filter’theentriesprintedinthebibliography.
Ifseveral‘filteringoptions’areused—includingcaseswherethesameoptionisused
multipletimeswithdifferentvalues—,anentrywillonlybeprintedifitsatisfiesall
filteringconditions. Inotherwords,‘filteringoptions’areconnectedviaalogicand.
section=hintegeri default:currentsection
Print only entries cited in reference section hintegeri. The reference sections are
numberedstartingat1. Allcitationsgivenoutsidearefsectionenvironmentare
assignedtosection0. See§3.8.4fordetailsand§3.14.3forusageexamples.
segment=hintegeri
Print only entries cited in reference segment hintegeri. The reference segments
arenumberedstartingat1. Allcitationsgivenoutsidearefsegmentenvironment
are assigned to segment 0. See § 3.8.5 for details and § 3.14.3 for usage examples.
Rememberthatsegmentswithinasectionarenumberedlocaltothesectionsothe
segmentyourequestwillbethenthsegmentintherequested(orcurrentlyactive
enclosing)section.
91

type=hentrytypei
Printonlyentrieswhoseentrytypeishentrytypei.
nottype=hentrytypei
Print only entries whose entry type is not hentrytypei. This option may be used
multipletimes.
subtype=hsubtypei
Printonlyentrieswhoseentrysubtypeisdefinedandhsubtypei.
notsubtype=hsubtypei
Printonlyentrieswhoseentrysubtypeisundefinedornothsubtypei. Thisoption
maybeusedmultipletimes.
keyword=hkeywordi
Print only entries whose keywords field includes hkeywordi. This option may be
usedmultipletimes.
notkeyword=hkeywordi
Print only entries whose keywords field does not include hkeywordi. This option
maybeusedmultipletimes.
category=hcategoryi
Printonlyentriesassignedtocategoryhcategoryi. Thisoptionmaybeusedmultiple
times.
notcategory=hcategoryi
Print only entries not assigned to category hcategoryi. This option may be used
multipletimes.
filter=hnamei
Filtertheentrieswithfilterhnamei,asdefinedwith\defbibfilter. See§3.8.9for
details.
check=hnamei
Filtertheentrieswithcheckhnamei,asdefinedwith\defbibcheck. See§3.8.9for
details.
The following options are useful in ‘split bibliography’ setups, where several
bibliographies(withdifferentfilteringoptions)areprintedinthesamedocument.
resetnumbers=htrue,false,numberi
Thisoptionappliestonumericalcitation/bibliographystylesonlyandrequiresthat
thedefernumbersoptionfrom§3.1.2.1beenabledglobally. Ifenabled,itwillreset
thenumericallabelsassignedtotheentriesintherespectivebibliography,i.e.,the
numberingwillrestartat1. Youcanalsopassanumbertothisoption,forexample:
resetnumbers=10toresetnumberingtothespecifiednumbertoaidnumberingcon-
tinuityacrossdocuments. Usethisoptionwithcareasbiblatexcannotguarantee
uniquelabelsgloballyiftheyareresetmanually.
92

omitnumbers=true,false
Thisoptionappliestonumericalcitation/bibliographystylesonlyandrequiresthat
the defernumbers option from § 3.1.2.1 be enabled globally. If enabled, biblatex
willnotassignanumericallabeltotheentriesintherespectivebibliography. Thisis
usefulwhenmixinganumericalsubbibliographywithoneormoresubbibliographies
usingadifferentscheme(e.g.,author-titleorauthor-year).
locallabelwidth=true,false default:false
Calculate\labelnumberwidth,\labelalphawidthandsimilarlengthslocallyforthe
presentbibliographyandnotgloballyforallentries. Seealsolabelnumberwidthin
§3.1.2.1.
\bibbysection[hkey=value,…i]
This command automatically loops over all reference sections. This is equivalent
to giving one \printbibliography command for every section but has the addi-
tional benefit of automatically skipping sections without references. Note that
\bibbysectionstartslookingforreferencesinsection1. Itwillignorereferences
given outside of refsection environments since they are assigned to section 0.
See § 3.14.3 for usage examples. The options are a subset of those supported by
\printbibliography. Validoptionsareenv,heading,prenote,postnote. Thecur-
rentbibliographycontextsortingtemplateisusedforallsections(see§3.8.10).
\bibbysegment[hkey=value,…i]
This command automatically loops over all reference segments. This is equiva-
lenttogivingone\printbibliographycommandforeverysegmentinthecurrent
refsectionbuthastheadditionalbenefitofautomaticallyskippingsegmentswith-
outreferences. Notethat\bibbysegmentstartslookingforreferencesinsegment1.
Itwillignorereferencesgivenoutsideofrefsegmentenvironmentssincetheyare
assignedtosegment0. See§3.14.3forusageexamples. Theoptionsareasubsetof
thosesupportedby\printbibliography. Validoptionsareenv,heading,prenote,
postnote. Thecurrentbibliographycontextsortingtemplateisusedforallsegments
(see§3.8.10).
\bibbycategory[hkey=value,…i]
Thiscommandloopsoverallbibliographycategories. Thisisequivalenttogivingone
\printbibliographycommandforeverycategorybuthastheadditionalbenefitof
automaticallyskippingemptycategories. Thecategoriesareprocessedintheorderin
whichtheyweredeclared. See§3.14.3forusageexamples. Theoptionsareasubsetof
thosesupportedby\printbibliography. Validoptionsareenv,prenote,postnote,
section. Notethatheadingisnotavailablewiththiscommand. Thenameofthe
currentcategoryisautomaticallyusedastheheadingname. Thisisequivalentto
passingheading=hcategoryito\printbibliographyandimpliesthattheremustbe
amatchingheadingdefinitionforeverycategory. Thecurrentbibliographycontext
sortingtemplateisusedforallcategories(see§3.8.10).
\printbibheading[hkey=value,…i]
Thiscommandprintsabibliographyheadingdefinedwith\defbibheading. Ittakes
oneoptionalargument,whichisalistofoptionsgiveninhkeyi=hvalueinotation. The
optionsareasmallsubsetofthosesupportedby\printbibliography. Validoptions
93

areheading,title,label,prenoteandpostnote. Notethatboththeprenoteand
postnoteargumentareprintedaftertheheading. Theirbehaviourexactlymirrors
thatof\printbibliography,exceptthatnobibliographyiscreatedinbetweenthe
twonotes. Bydefault,thiscommandusestheheadingbibliography. See§3.8.7for
details. Alsosee§§3.14.3and3.14.4forusageexamples.
\DeclarePrintbibliographyDefaults{hkey=value,…i}
This command can be used to globally set defaults for some options
to \printbibliography, the \bibby... bibliography commands and
\printbibheading. Thesupportedkeysare
• env
• heading
• title
• prenote
• postnote
• filter
To print a bibliography with a different sorting template than the global sorting
template,usethebibliographycontextswitchingcommandsfrom§3.8.10.
3.8.3 BibliographyLists
biblatex can, in addition to printing normal bibliographies, also print arbitrary
listsofinformationderivedfromthebibliographydatasuchasalistofshorthand
abbreviationsforparticularentriesoralistofabbreviationsofjournaltitles.
Abibliographylistdiffersfromanormalbibliographyinthatthesamebibliography
driverisusedtoprintallentriesratherthanaspecificdriverbeingusedforeach
entrydependingontheentrytype.
\printbiblist[hkey=value,…i]{hbiblistnamei}
This command prints a bibliography list. It takes an optional argument, which
is a list of options given in hkeyi=hvaluei notation. Valid options are all options
supportedby\printbibliography(§3.8.2)exceptresetnumbersandomitnumbers.
Additionally,thetwooptionsdriverandbiblistfilterareavailable. Ifthereare
anyrefsectionenvironmentsinthedocument,thebibliographylistwillbelocal
to these environments; see § 3.8.4 for details. By default, this command uses the
headingbiblist. See§3.8.7fordetails.
Thehbiblistnameiisamandatoryargumentwhichnamesthebibliographylist. This
nameisusedtoidentify:
• Thedefaultbibliographydriverusedtoprintthelistentries
• A default bibliography list filter declared with \DeclareBiblistFilter (see
§4.5.7)usedtofiltertheentriesreturnedbybiberinthe.bbl
• Adefaultcheckdeclaredwith\defbibcheck(see§3.8.9)usedtopost-process
thelistentries
• Thedefaultbibenvironmenttouse
• Thedefaultsortingtemplatetouse
94

Thetwoadditionaloptionscanbeusedtochangesomeofthedefaultssetbythe
mandatoryargument.
driver=hdriveri default:hbiblistnamei
Changethebibliographydriverusedtoprintthelistentries.
biblistfilter=hbiblistfilteri default:hbiblistnamei
Changethebibliographylistfilterusedtofiltertheentries. hbiblistfilterimustbea
validbibliographylistfilterdefinedwith\DeclareBiblistFilter(see§4.5.7).
Intermsofsortingthelist,thedefaultistosortusingthesortingtemplatenamed
afterthebibliographylist(ifitexists)andonlythentofallbacktothecurrentcontext
sortingtemplateifthisisnotdefined(see§3.8.10).
Themostcommonbibliographylistisalistofshorthandabbreviationsforcertain
entries and so this has a convenience alias \printshorthands[…] for backwards
compatibilitywhichisdefinedas:
\printbiblist[...]{shorthand}
biblatexprovidesautomaticsupportfordatasourcefieldsinthedefaultdatamodel
markedas‘Labelfields’(See§2.2.2). Suchfieldsautomaticallyhavedefinedforthem:
• Adefaultbibenvironment(See§3.8.7)
• Abibliographylistfilter(See§4.5.7)
• Somesupportingformatsandlengths(See§4.10.5and§4.10.4)
Thereforeonlyaminimalsetupisrequiredtoprintbibliographylistswithsuchfields.
Forexample,toprintalistofjournaltitleabbreviations,youcanminimallyputthis
inyourpreamble:
\DeclareBibliographyDriver{shortjournal}{%
\printfield{journaltitle}}
Thenyoucanputthisinyourdocumentwhereyouwanttoprintthelist:
\printbiblist[title={Journal Shorthands}]{shortjournal}
Sinceshortjournalisdefinedinthedefaultdatamodelasa‘Labelfield’,thisexample:
• Usestheautomaticallycreated‘shortjournal’bibenvironment
• Usestheautomaticallycreated‘shortjournal’bibliographylistfiltertoreturn
onlyentrieswithashortjournalfieldinthe.bbl
• Usesthedefined‘shortjournal’bibliographydrivertoprinttheentries
• Uses the default ‘biblist’ heading but overrides the title with ‘Journal Short-
hands’
• Usesthecurrentbibliographycontextsortingtemplateifnotemplateexists
withthenameshortjournal
Often,youwillwanttosortonthelabelfieldofthelistandsinceasortingtemplate
isautomaticallypickedupifitisnamedafterthelist,inthiscaseyoucouldsimply
do:
95

\DeclareSortingTemplate{shortjournal}{
\sort{
\field{shortjournal}
}
}
Naturallyalldefaultscanbeoverriddenbyoptionsto\printbiblistanddefinitions
oftheenvironments,filtersetc. andinthiswayarbitrarytypesofbibliographylists
canbeprintedcontainingavarietyofinformationfromthebibliographydata.
Bibliographylistsareoftenusedtoprintlistsofvariouskindsofshorthandsand
thiscanresultinduplicateentriesifmorethanonebibliographyentryhasthesame
shorthand. Forexample,severaljournalarticlesinthesamejournalwouldresultin
duplicateentriesinalistofjournalshorthands. Youcanusethefactthatsuchlists
automaticallypickupa\bibcheckwiththesamenameasthelisttodefineacheck
toremoveduplicates. Ifyouaredefiningalisttoprintallofthejournalshorthands
usingtheshortjournalfield,youcoulddefinea\bibchecklikethis:
\defbibcheck{shortjournal}{%
\iffieldundef{shortjournal}
{\skipentry}
{\iffieldundef{journaltitle}
{\skipentry}
{\ifcsdef{sjcheck@\therefsection
-\strfield{shortjournal}=\strfield{journaltitle}}
{\skipentry}
{\savefieldcs{journaltitle}{sjcheck@\therefsection
-\strfield{shortjournal}=\strfield{journaltitle}}}}}}
3.8.4 BibliographySections
The refsection environment is used in the document body to mark a reference
section. Thisenvironmentisusefulifyouwantseparate,independentbibliographies
and bibliography lists in each chapter, section, or any other part of a document.
Within a reference section, all cited works are assigned labels which are local to
theenvironment. Technically,referencesectionsarecompletelyindependentfrom
document divisions such as \chapter and \section even though they will most
likelybeusedperchapterorsection. Seetherefsectionpackageoptionin§3.1.2.1
forawaytoautomatethis. Alsosee§3.14.3forusageexamples.
\begin{refsection}[hresource,…i]
\end{refsection}
Theoptionalargumentisacomma-separatedlistofresourcesspecifictothereference
section. Iftheargumentisomitted,thereferencesectionwillusethedefaultresource
list,asspecifiedwith\addbibresourceinthepreamble. Iftheargumentisprovided,
itreplacesthedefaultresourcelist. Globalresourcesspecifiedwith\addglobalbib
arealwaysconsidered. refsectionenvironmentsmaynotbenested,butyoumay
use refsegment environments within a refsection to subdivide it into segments.
Use the section option of \printbibliography to select a section when printing
the bibliography, and the corresponding option of \printbiblist when printing
96

bibliographylists. Bibliographysectionsarenumberedstartingat1. Thenumberof
thecurrentsectionisalsowrittentothetranscriptfile. Allcitationsgivenoutsidea
refsectionenvironmentareassignedtosection0. If\printbibliographyisused
withinarefsection,itwillautomaticallyselectthecurrentsection. Thesection
optionisnotrequiredinthiscase. Thisalsoappliesto\printbiblist. Beginninga
newreferencesectionautomaticallyendstheactivereferencecontext(see§3.8.10).
\newrefsection[hresource,…i]
Thiscommandissimilartotherefsectionenvironmentexceptthatitisastand-
alone command rather than an environment. It automatically ends the previous
referencesection(ifany)andimmediatelystartsanewone. Notethatthereference
sectionstartedbythelast\newrefsectioncommandinthedocumentwillextend
totheveryendofthedocument. Use\endrefsectionifyouwanttoterminateit
earlier.
3.8.5 BibliographySegments
The refsegment environment is used in the document body to mark a reference
segment. This environment is useful if you want one global bibliography which
issubdividedbychapter,section,oranyotherpartofthedocument. Technically,
referencesegmentsarecompletelyindependentfromdocumentdivisionssuchas
\chapterand\sectioneventhoughtheywilltypicallybeusedperchapterorsection.
Seetherefsegmentpackageoptionin§3.1.2.1forawaytoautomatethis. Alsosee
§3.14.3forusageexamples.
\begin{refsegment}
\end{refsegment}
The difference between a refsection and a refsegment environment is that the
formercreateslabelswhicharelocaltotheenvironmentwhereasthelatterprovides
atargetforthesegmentfilterof\printbibliographywithoutaffectingthelabels.
Theywillbeuniqueacrosstheentiredocument. refsegmentenvironmentsmaynot
be nested, but you may use them in conjunction with refsection to subdivide a
referencesectionintosegments. Inthiscase,thesegmentsarelocaltotheenclosing
refsectionenvironment. Usethesegmentoptionof\printbibliographytoselecta
segmentwhenprintingthebibliography. Withinasection,thereferencesegmentsare
numberedstartingat1andthenumberofthecurrentsegmentwillbewrittentothe
transcriptfile. Allcitationsgivenoutsidearefsegmentenvironmentareassigned
to segment 0. In contrast to the refsection environment, the current segment
is not selected automatically if \printbibliography is used within a refsegment
environment.
\newrefsegment Thiscommandissimilartotherefsegmentenvironmentexceptthatitisastand-
alone command rather than an environment. It automatically ends the previous
referencesegment(ifany)andimmediatelystartsanewone. Notethatthereference
segmentstartedbythelast\newrefsegmentcommandwillextendtotheendofthe
document. Use\endrefsegmentifyouwanttoterminateitearlier.
3.8.6 BibliographyCategories
Bibliographycategoriesallowyoutosplitthebibliographyintomultiplepartsdedi-
catedtodifferenttopicsordifferenttypesofreferences,forexampleprimaryand
secondarysources. See§3.14.4forusageexamples.
97

\DeclareBibliographyCategory{hcategoryi}
Declaresanewhcategoryi,tobeusedinconjunctionwith\addtocategoryandthe
category and notcategory filtersof \printbibliography. Thiscommand is used
inthedocumentpreamble.
\addtocategory{hcategoryi}{hkeyi}
Assigns a hkeyi to a hcategoryi, to be used in conjunction with the category and
notcategory filters of \printbibliography. This command may be used in the
preamble and in the document body. The hkeyi may be a single entry key or a
comma-separatedlistofkeys. Theassignmentisglobal.
3.8.7 BibliographyHeadingsandEnvironments
\defbibenvironment{hnamei}{hbegincodei}{hendcodei}{hitemcodei}
Thiscommanddefinesbibliographyenvironments. Thehnameiisanidentifierpassed
to the env option of \printbibliography and \printbiblist when selecting the
environment. The hbegincodei is LaTeX code to be executed at the beginning of
the environment; the hendcodei is executed at the end of the environment; the
hitemcodeiiscodetobeexecutedatthebeginningofeachentryinthebibliography
orabibliographylist. HereisanexampleofadefinitionbasedonthestandardLaTeX
listenvironment:
\defbibenvironment{bibliography}
{\list{}
{\setlength{\leftmargin}{\bibhang}%
\setlength{\itemindent}{-\leftmargin}%
\setlength{\itemsep}{\bibitemsep}%
\setlength{\parsep}{\bibparsep}}}
{\endlist}
{\item}
Asseenintheaboveexample,usageof\defbibenvironmentisroughlysimilarto
\newenvironment except that there is an additional mandatory argument for the
hitemcodei.
\defbibheading{hnamei}[htitlei]{hcodei}
This command defines bibliography headings. The hnamei is an identifier to be
passed to the heading option of \printbibliography or \printbibheading and
\printbiblistwhenselectingtheheading. ThehcodeishouldbeLaTeXcodegener-
atingafully-fledgedheading,includingpageheadersandanentryinthetableof
contents,ifdesired. If\printbibliographyor\printbiblistareinvokedwitha
titleoption,thetitlewillbepassedtotheheadingdefinitionas#1. Ifnot,thedefault
title specified by the optional htitlei argument is passed as #1 instead. The htitlei
argumentwilltypicallybe\bibname,\refname,or\biblistname(see§4.9.2.1). This
commandisoftenneededafterchangestodocumentheadersinthepreamble. Here
isanexampleofasimpleheadingdefinition:
\defbibheading{bibliography}[\bibname]{%
\chapter*{#1}%
98

\markboth{#1}{#1}}
The following headings, which are intended for use with \printbibliography
and\printbibheading,arepredefined:
bibliography
Thisisthedefaultheadingusedby\printbibliographyiftheheadingoptionisnot
given. Its default definition depends on the document class. If the class provides
a \chapter command, the heading is similar to the bibliography heading of the
standardLaTeXbookclass,i.e.,ituses\chapter*tocreateanunnumberedchapter
heading which is not included in the table of contents. If there is no \chapter
command,itissimilartothebibliographyheadingofthestandardLaTeXarticle
class,i.e.,ituses\section*tocreateanunnumberedsectionheadingwhichisnot
includedinthetableofcontents. Thestringusedintheheadingalsodependson
thedocumentclass. Withbook-likeclassesthelocalisationstringbibliographyis
used,withotherclassesitisreferences(see§4.9.2). Seealso§§3.15.1and3.15.2
forclass-specifichints.
subbibliography
Similartobibliographybutonesectioninglevellower. Thisheadingdefinitionuses
\section*insteadof\chapter*withabook-likeclassand\subsection*insteadof
\section*otherwise.
bibintoc
Similartobibliographyabovebutaddsanentrytothetableofcontents.
subbibintoc
Similartosubbibliographyabovebutaddsanentrytothetableofcontents.
bibnumbered
Similartobibliographyabovebutuses\chapteror\sectiontocreateanumbered
headingwhichisalsoaddedtothetableofcontents.
subbibnumbered
Similar to subbibliography above but uses \section or \subsection to create a
numberedheadingwhichisalsoaddedtothetableofcontents.
none
Ablankheadingdefinition. Usethistosuppresstheheading.
Thefollowingheadingsintendedforusewith\printbiblistarepredefined:
biblist
This is the default heading used by \printbiblist if the heading option is not
given. Itissimilartobibliographyaboveexceptthatitusesthelocalisationstring
shorthandsinsteadofbibliographyorreferences(see§4.9.2). Seealso§§3.15.1
and3.15.2forclass-specifichints.
99

biblistintoc
Similartobiblistabovebutaddsanentrytothetableofcontents.
biblistnumbered
Similar to biblist above but uses \chapter or \section to create a numbered
headingwhichisalsoaddedtothetableofcontents.
3.8.8 BibliographyNotes
\defbibnote{hnamei}{htexti}
Defines the bibliography note hnamei, to be used via the prenote and postnote
optionsof\printbibliographyand\printbiblist. Thehtextimaybeanyarbitrary
pieceoftext,possiblyspanningseveralparagraphsandcontainingfontdeclarations.
Alsosee§3.15.6.
3.8.9 BibliographyFiltersandChecks
\defbibfilter{hnamei}{hexpressioni}
Defines the custom bibliography filter hnamei, to be used via the filter option
of \printbibliography. The hexpressioni is a complex test based on the logical
operatorsand,or,not,thegroupseparator(...),andthefollowingatomictests:
segment=hintegeri
Matchesallentriescitedinreferencesegmenthintegeri.
type=hentrytypei
Matchesallentrieswhoseentrytypeishentrytypei.
subtype=hsubtypei
Matchesallentrieswhoseentrysubtypeishsubtypei.
keyword=hkeywordi
Matches all entries whose keywords field includes hkeywordi. If the hkeywordi
containsspaces,itneedstobewrappedinbraces.
category=hcategoryi
Matchesallentriesassignedtohcategoryiwith\addtocategory.
Hereisanexampleofafilterexpression:
\defbibfilter{example}{%
( type=book or type=inbook )
and keyword=abc
and not keyword={x y z}
}
100

This filter will match all entries whose entry type is either @book or @inbook and
whose keywords field includes the keyword ‘abc’ but not ‘x y z’. As seen in the
aboveexample,allelements—including(and)—areseparatedbywhitespace(spaces,
tabs,orlineendings)oneitherside. Thereisnospacingaroundtheequalsign. The
logicaloperatorsareevaluatedwiththe\ifboolexprcommandfromtheetoolbox
package. Seetheetoolboxmanualfordetailsaboutthesyntax. Thesyntaxofthe
\ifthenelsecommandfromtheifthenpackage,whichhasbeenemployedinolder
versions of biblatex, is still supported. This is the same test using ifthen-like
syntax:
\defbibfilter{example}{%
\( \type{book} \or \type{inbook} \)
\and \keyword{abc}
\and \not \keyword{x y z}
}
Note that custom filters are local to the reference section in which they are used.
Usethesectionfilterof\printbibliographytoselectadifferentsection. Thisis
notpossiblefromwithinacustomfilter.
\defbibcheck{hnamei}{hcodei}
Definesthecustombibliographyfilterhnamei, tobeusedviathecheckoptionof
\printbibliography. \defbibcheck is similar in concept to \defbibfilter but
muchmorelow-level. Ratherthanahigh-levelexpression,thehcodeiisLaTeXcode,
much like the code used in driver definitions, which may perform arbitrary tests
todecidewhetherornotagivenentryistobeprinted. Thebibliographicdataof
therespectiveentryisavailablewhenthehcodeiisexecuted. Issuingthecommand
\skipentryinthehcodeiwillcausethecurrententrytobeskipped. Forexample,
thefollowingfilterwillonlyoutputentrieswithanabstractfield:
\defbibcheck{abstract}{%
\iffieldundef{abstract}{\skipentry}{}}
...
\printbibliography[check=abstract]
Thefollowingcheckwillexcludeallentriespublishedbeforetheyear2000:
\defbibcheck{recent}{%
\iffieldint{year}
{\ifnumless{\thefield{year}}{2000}
{\skipentry}
{}}
{\skipentry}}
Seetheauthorguide,inparticular§§4.6.2and4.6.3,forfurtherdetails.
3.8.10 ReferenceContexts
Referencesinabibliographyarecitedandprintedina‘context’. Thecontextdeter-
mines the data which is actually used to cite or provide bibliographic data for an
entry. Acontextconsistsofthefollowinginformation:
101

• Asortingtemplate
• Atemplateforconstructingthesortingkeysfornames
• Astringprefixforcitationschemeswhichusealphabeticornumericlabels
• Atemplateforcalculatingnameuniquenessinformation
• Atemplateforconstructingalphabeticlabelsfornames
Thepurposeofbibliographycontextsistwofold. Firstly,theyareusedtosetoptions
whichinfluenceaprintedbibliographyandsecondlytoinfluencethedataprintedby
citationcommands. Theformeruseisthemostcommonwhenoneneedstoprint
morethanonebibliographylistwithdifferent,forexample,sorting.
\usepackage[sorting=nyt]{biblatex}
\begin{document}
\cite{one}
\cite{two}
\printbibliography
\newrefcontext[sorting=ydnt]
\printbibliography
Hereweprinttwobibliographies,onewiththedefault‘nyt’sortingtemplateand
onewiththe‘ydnt’sortingtemplate.
To demonstrate the second type of use of bibliography contexts, we have to
understandthattheactualdataforanentrycanvarydependingonthecontext. This
ismostobviousinthecaseoftheextra*fieldslikeextradatewhicharegeneratedby
thebackendaccordingtotheorderofentriesafter sortingsothattheycomeoutinthe
expected‘a,b,c’order. Thisclearlyshowsthatthedata inanentrycanbedifferent
betweensortingtemplates. Ifadocumentcontainsmorethanonebibliographylist
withdifferentsortingtemplates,itcanhappenthenthatthe.bblcontainssorting
listswiththesameentrybutcontainingdifferentdata(adifferentvalueforextradate,
forexample). Thepurposeofbibliographycontextsistoencapsulatethingsinsidea
contextsothatbiblatexcanusethecorrectentrydata. Anexampleisprintinga
bibliographylistwithadifferentsortingordertotheglobalsortingorderwherethe
extra*fieldsaredifferentforthesameentrybetweensortinglists:
\usepackage[sorting=nyt,style=authoryear]{biblatex}
\DeclareSortingTemplate{yntd}{
\sort{
\field[strside=left,strwidth=4]{sortyear}
\field[strside=left,strwidth=4]{year}
\literal{9999}
}
\sort{
\field{sortname}
\field{author}
\field{editor}
}
\sort[direction=descending]{
\field{sorttitle}
102

\field{title}
}
}
\begin{document}
\cite{one}
\cite{two}
\printbibliography
\newrefcontext[sorting=yntd]
\cite{one}
\cite{two}
\printbibliography
Here,theseconduseofthecitations,alongwiththe\printbibliographycommand
willusedatafromthecontextofthecustom‘yntd’sortingtemplatewhichmaywell
be different from the data associated with the default ‘nyt’ template. That is, the
citationlabels(inanauthoryearstylewhichusesextradate)maybedifferentfor
theexactsameentries betweendifferentbibliographycontextsandsothecitations
themselvesmaylookdifferent.
Referencecontextscanbedeclaredwith\DeclareRefcontextandreferredtoby
name,seebelow.
By default, data for a citation is drawn from the reference context of the last
bibliographyinwhichitwasprinted. Forexample:
\DeclareRefcontext{ap}{labelprefix=A}
\begin{document}
\cite{book, article, misc}
\printbibliography[type=book]
\newrefcontext{ap}
\printbibliography[type=article]
\newrefcontext[sorting=ydnt]
\printbibliography[type=misc]
\end{document}
This example also shows the declaration and use of a named reference context.
Assumingtheentrykeysareindicativeoftheirentrytypes,thisisthedefaultsituation
forthecitationswhichcorrespondstowhatusersnormallyexpect:
• Thecitationofentrybookwoulddrawitsdatafromtheglobalreferencecontext,
becausethelastbibliographyinwhichitwasprintedwastheoneintheglobal
referencecontext.
• Thecitationofentryarticlewoulddrawitsdatafromreferencecontextwith
labelprefix=Aandwouldthereforehavea‘A’prefixwhencited.
• Thecitationofentrymiscwoulddrawitsdatafromthereferencecontextwith
sorting=ydnt
103

Incaseswheretheuserhasentrieswhichoccurinmultiplebibliographiesindiffer-
entformsorwithpotentiallydifferentlabels(inanumericschemewithdifferent
labelprefixvaluesforexample),itmaybenecessarytotellbiblatexfromwhich
referencecontextyouwishtodrawthecitationinformation. Asshownabovethiscan
bedonebyexplicitlyputtingcitationsinsidereferencecontexts. Thiscanbeonerous
inalargedocumentandsothereisspecificfunctionalityforassigningcitationsto
referencecontextsprogrammatically,seethe\assignrefcontext*macrosbelow.
\DeclareRefcontext{hnamei}{hkey=value,…i}
Declares a named reference context with name hnamei. The hkey=valuei options
definethecontextattributes. Allcontextattributesareoptionalanddefaulttothe
globalsettingsifabsent. Thevalidoptionsare:
sorting=hnamei
Specifyasortingtemplatedefinedpreviouslywith\DeclareSortingTemplate. This
templateisusedtodeterminewhichdatatoretrieveand/orprintforanentryinthe
commandsinsidethecontext.
sortingnamekeytemplatename=hnamei
Specify a sorting name key template defined previously with
\DeclareSortingNamekeyTemplate. This template is used to construct sort-
ingkeysfornamesinsidethecontext. Thetemplatenamecanalsobespecified(in
increasingorderofpreference)per-entry,per-namelistandper-name. See§Efor
informationonsettingper-option,per-namelistandper-nameoptions.
uniquenametemplatename=hnamei
Specify a uniquename template defined previously with
\DeclareUniquenameTemplate (see § 4.11.4). This template is used to calcu-
lateuniquenessinformationfornamesinsidethecontext. Thetemplatenamecan
alsobespecified(inincreasingorderofpreference)per-entry,per-namelistandper-
name. See § E for information on setting per-option, per-namelist and per-name
options.
labelalphanametemplatename=hnamei
Specifyatemplatedefinedpreviouslywith\DeclareLabelalphaNameTemplate(see
§4.5.5). Thistemplateisusedtoconstructnamepartsofalphabeticlabelsfornames
insidethecontext. Thetemplatenamecanalsobespecified(inincreasingorderof
preference)per-entry,per-namelistandper-name. See§Eforinformationonsetting
per-option,per-namelistandper-nameoptions.
namehashtemplatename=hnamei
Specifyatemplatedefinedpreviouslywith\DeclareNamehashTemplate(see§4.11.5).
Thistemplateisusedtoconstructnamehashesusedtodeterminewhethernames
refer to the same person. The template name can also be specified (in increasing
orderofpreference)per-entry,per-namelistandper-name. See§Eforinformation
onsettingper-option,per-namelistandper-nameoptions.
nametemplates=hnamei
A convenience meta-option which sets sortingnamekeytemplate,
uniquenametemplate, labelalphanametemplate and namehashtemplate to
the same template name. This option can also be specified (in increasing order
ofpreference)per-entry, per-namelistandper-name. See§Eforinformationon
settingper-option,per-namelistandper-nameoptions.
104

labelprefix=hstringi
Thisoptionappliestonumericalcitation/bibliographystylesonlyandrequiresthat
thedefernumbersoptionfrom§3.1.2.1beenabledglobally. Settingthisoptionwill
implicitlyenableresetnumbersfortheany\printbibliographyinthescopeofthe
context(unlessoverriddenbyauser-specifiedvalueforresetnumbers). Theoption
assignsthehstringiasaprefixtoallentriesinthereferencecontext. Forexample,
ifthe hstringi is A,the numerical labels printed will be [A1], [A2], [A3], etc. This
isusefulforsubdividednumericalbibliographieswhereeachsubbibliographyuses
adifferentprefix. Thehstringiisavailabletostylesinthelabelprefixfieldofall
affectedentries. Notethatthehstringiisfullyexpanded,whichmeansthatyoucan
usecontext-dependentmacroslike\thechapter,butnotunexpandablecommands
such as \dag. If you need to pass unexpandable code to hstringi, protect it from
expansionwith\detokenize. See§4.2.4.2fordetails.
\begin{refcontext}[hkey=value,…i]{hnamei}
\end{refcontext}
Wraps a reference context environment. The possible hkey=valuei optional argu-
ments are as for \DeclareRefcontext and override options given for the named
referencecontexthnamei. hnameicanalsobeomittedas{}orbyomittingeventhe
emptybraces22.
Therefcontextenvironmentcannotbenestedandbiblatexwillgenerateanerror
ifyoutrytodoso.
\newrefcontext[hkey=value,…i]{hnamei}
Thiscommandissimilartotherefcontextenvironmentexceptthatitisastand-
alone command rather than an environment. It automatically ends any previous
reference context section begun with \newrefcontext (if any) and immediately
startsanewone. Notethatthecontextsectionstartedbythelast\newrefcontext
command in the document will extend to the end of the current refsection. Use
\endrefcontextifyouwanttoterminateitearlier.
\localrefcontext[hkey=value,…i]{hnamei}
Thiscommandissimilartothenewrefcontextcommandexceptthatitsetsupthe
reference context only locally. This is useful if the reference context needs to be
changedwithinagroup. Thereisnoneedtoendalocalreferencecontext,itwill
automaticallyberesetoncethegroupends.
Atthebeginningofthedocument,thereisalwaysaglobalcontextcontainingglobal
settingsforeachofthereferencecontextoptions. Hereisanexamplesummarising
thereferencecontextswithvarioussettings:
\usepackage[sorting=nty]{biblatex}
\DeclareRefcontext{testrc}{sorting=nyt}
% Global reference context:
% sorting=nty
% sortingnamekeytemplate=global
22Thisslightlyoddsyntaxpossibilityisaresultofbackwardscompatibilitywithbiblatex<3.5
105

% labelprefix=
\begin{document}
\begin{refcontext}{testrc}
% reference context:
% sorting=nyt
% sortingnamekeytemplate=global
% labelprefix=
\end{refcontext}
\begin{refcontext}[labelprefix=A]{testrc}
% reference context:
% sorting=nyt
% sortingnamekeytemplate=global
% labelprefix=A
\end{refcontext}
\begin{refcontext}[sorting=ydnt,labelprefix=A]
% reference context:
% sorting=ydnt
% sortingnamekeytemplate=global
% labelprefix=A
\end{refcontext}
\newrefcontext}[labelprefix=B]
% reference context:
% sorting=nty
% sortingnamekeytemplate=global
% labelprefix=B
\endrefcontext
\newrefcontext}[sorting=ynt,labelprefix=C]{testrc}
% reference context:
% sorting=ynt
% sortingnamekeytemplate=global
% labelprefix=C
\endrefcontext
\assignrefcontextkeyws[hkey=value,…i]{hkeyword1,keyword2,…i}
\assignrefcontextkeyws*[hkey=value,…i]{hkeyword1,keyword2,…i}
\assignrefcontextcats[hkey=value,…i]{hcategory1,category2,…i}
\assignrefcontextcats*[hkey=value,…i]{hcategory1,category2,…i}
\assignrefcontextentries[hkey=value,…i]{hentrykey1,entrykey2,…i}
\assignrefcontextentries*[hkey=value,…i]{hentrykey1,entrykey2,…i}
\assignrefcontextentries[hkey=value,…i]{h*i}
\assignrefcontextentries*[hkey=value,…i]{h*i}
Thesecommandsautomateputtingcitationsintorefcontextswhenthedefaultbe-
haviour is not sufficient. The hkey=valuei options are as for \DeclareRefcontext
106

withtheadditionofthename=refcontextnameoptionwhichsetsalloptionsfrom
thosedefinedforthenamedrefcontexthrefcontextnamei. Usename=defaulttouse
theglobaldefaultrefcontextoptions. Thespecifichkeyi=hvalueioptionsoverride
thosesetbyanynamedhrefcontextnamei. Thedefaultbehaviouristhatthedatafor
acitationisdrawnfromtherefcontextofthemostrecentlyprocessedbibliography
inwhichitwasprinted23. Forcitationsthatareusedinsomewaybutnotprinted
inabibliographyorbibliographylist,theydefaulttodrawingtheirdatafromthe
global refcontext established at the beginning of the document. To override this
behaviour,insteadofmanuallywrappingcitationcommandsinrefcontextenviron-
ments,whichmightbeerror-proneandtedious,youcanregisteracomma-separated
listofhkeywordsi,hcategoriesiorhentrykeysiwhich,respectively,maketheentries
withanyofthespecifiedkeywords,entriesinanyofthespecifiedcategories(see
§ 3.14.4) or entries with any of the specified citation keys draw their data from a
particularnamedrefcontextand/orspecifiedhrefcontextkey/valuesi. Suchrefcontext
auto-assignmentsarespecifictothecurrentrefsection. Youmayspecifythesame
citationkeyinanyofthesecommandsbutbeawarethatassignmentisdoneinthe
orderhkeywordsi,hcategoriesi,hentrykeysiwiththelaterspecificationsoverriding
theearlier. \assignrefcontextentriesacceptsasingleasteriskinsteadofalistof
entrykeys which allows the assignment of all keys in a refsection to a refcontext
withhavingtoexplicitlylistthem. Anexample:
\assignrefcontextentries[labelprefix=A]{key2}
\cite{key1}
\begin{refcontext}[labelprefix=B]
\cite{key2}
\end{refcontext}
Here,thedataforthecitationofkey2willbedrawnfromrefcontextlabelprefix=A
andnotlabelprefix=B(resultinginalabelwithprefix‘A’andnot‘B’).Thestarred
versionsdonotoverridealocalrefcontextandsowith:
\assignrefcontextentries*[labelprefix=A]{key2}
\cite{key1}
\begin{refcontext}[labelprefix=B]
\cite{key2}
\end{refcontext}
thedataforthecitationofkey2willbedrawnfromrefcontextlabelprefix=B. Note
thatthesecommandsarerarelynecessaryunlessyouhavemultiplebibliographies
inwhichthesamecitationsoccurandbiblatexcannotbydefaulttellwhichbiblio-
graphylistacitationshouldreferto. Seetheexamplefile94-labelprefix.texfor
moredetails.
\DeclareRefcontext{testrc}{labelprefix=A}
\assignrefcontextentries[name=testrc]{key2}
\cite{key1}
\begin{refcontext}[labelprefix=B]
23Thisdoesnotalwaysmeanwhatonemightthink.Inadocumentcontainingmultiplebibliographies,
thelastbibliographywillbethecontextforanycitationsbeforethefirstbibliographybecauseall
bibliographiesareprocessedwhenthe.bblisread.
107

\cite{key2}
\end{refcontext}
Here, the data for the citation of key2 will be drawn from the refcontext named
‘testrc’whichhaslabelprefix=Aandnotlabelprefix=B(resultinginalabelwith
prefix‘A’andnot‘B’).
\DeclareRefcontext{testrc}{labelprefix=A}
\assignrefcontextentries[name=testrc,labelprefix=C]{key2}
\cite{key1}
\begin{refcontext}[labelprefix=B]
\cite{key2}
\end{refcontext}
Here, the data for the citation of key2 will be drawn from refcontext with
labelprefix=Candnotlabelprefix=Asincetheexplicitoptionsoverridethenamed
refcontext(resultinginalabelwithprefix‘C’andnot‘A’or‘B’).
\GenRefcontextData{hkey=value,…i}
Thiscommandtakesthesamekey/valueoptionsas\DeclareRefcontext. Itforces
the currently active refcontext, optionally modified by the key/value options, to
bewrittentothe.bcfsothatbiberwillcreateasorteddatalistforthespecified
refcontext. Normallythisisautomaticwhen\printbibliography/\prinbiblistis
usedinareferencecontextbuttherearesituationswherethedataforarefcontextwill
beneededbutnoreferencelistisgeneratedinthatcontexte.g. tosortcitationswith
thesortcitesoptionwhenthesortingofcitationsrequiresadifferentrefcontextto
thatusedfortheactualreferencelist.
3.8.11 DynamicEntrySets
Inadditiontothe@setentrytype,biblatexalsosupportsdynamicentrysetsdefined
on a per-document/per-refsection basis. The following command, which may be
usedinthedocumentpreambleorthedocumentbody,definesthesethkeyi:
\defbibentryset{hkeyi}{hkey1,key2,key3,…i}
Thehkeyiistheentrykeyoftheset,whichisusedlikeanyotherentrykeywhen
referringtotheset. Thehkeyimustbeuniqueanditmustnotconflictwithanyother
entrykey. Thesecondargumentisacomma-separatedlistoftheentrykeyswhich
makeuptheset. \defbibentrysetimpliestheequivalentofa\nocitecommand,
i.e.,allsetswhicharedeclaredarealsoaddedtothebibliography. Whendeclaring
the same set more than once, only the first invocation of \defbibentryset will
definetheset. Subsequentdefinitionsofthesamehkeyiareignoredandworklike
\nocitehkeyi. Dynamic entry sets defined in the document body are local to the
enclosingrefsectionenvironment,ifany. Otherwise,theyareassignedtoreference
section 0. Those defined in the preamble are assigned to reference section 0. See
§3.14.5forfurtherdetails.
3.9 CitationCommands
Allcitationcommandsgenerallytakeonemandatoryandtwooptionalarguments.
Thehprenoteiistexttobeprintedatthebeginningofthecitation. Thisisusually
108

anoticesuchas‘see’or‘compare’. Thehpostnoteiistexttobeprintedatthevery
endofthecitation. Thisisusuallyapagenumber. Ifonlyoneoftheseargumentsis
given,itistakenasapostnote. Ifyouwanttospecifyaprenotebutnopostnote,you
needtoleavethesecondoptionalargumentempty,asin\cite[see][]{key}. The
hkeyiargumenttoallcitationcommandsismandatory. Thisistheentrykeyora
comma-separatedlistofkeyscorrespondingtotheentrykeysinthebibfile. Insum,
allbasiccitationscommandslistedfurtherdownhavethefollowingsyntax:
\command[hprenotei][hpostnotei]{hkeysi}hpunctuationi
If the autopunct package option from § 3.1.2.1 is enabled, they will scan ahead
foranyhpunctuationiimmediatelyfollowingtheirlastargument. Thisisusefulto
avoidspuriouspunctuation marksafter citations. This featureis configuredwith
\DeclareAutoPunctuation,see§4.7.5fordetails.
3.9.1 StandardCommands
The following commands are defined by the citation style. Citation styles may
provideanyarbitrarynumberofspecializedcommands,butthesearethestandard
commandstypicallyprovidedbygeneral-purposestyles.
\cite[hprenotei][hpostnotei]{hkeyi}
\Cite[hprenotei][hpostnotei]{hkeyi}
Thesearethebarecitationcommands. Theyprintthecitationwithoutanyadditions
suchasparentheses. Thenumericandalphabeticstylesstillwrapthelabelinsquare
bracketssincethereferencemaybeambiguousotherwise. \Citeissimilarto\cite
but capitalizes the name prefix of the first name in the citation if the useprefix
optionisenabled,providedthatthereisanameprefixandthecitationstyleprints
anynameatall.
\parencite[hprenotei][hpostnotei]{hkeyi}
\Parencite[hprenotei][hpostnotei]{hkeyi}
Thesecommandsuseaformatsimilarto\citebutenclosetheentirecitationinparen-
theses. Thenumericandalphabeticstylesusesquarebracketsinstead. \Parenciteis
similarto\parencitebutcapitalizesthenameprefixofthefirstnameinthecitation
if the useprefix option is enabled, provided that there is a name prefix and the
citationstyleprintsanynameatall.
\footcite[hprenotei][hpostnotei]{hkeyi}
\footcitetext[hprenotei][hpostnotei]{hkeyi}
Thesecommanduseaformatsimilarto\citebutputtheentirecitationinafootnote
andaddaperiodattheend. Inthefootnote,theyautomaticallycapitalizethename
prefix of the first name if the useprefix option is enabled, provided that there is
anameprefixandthecitationstyleprintsanynameatall. \footcitetextdiffers
from\footciteinthatituses\footnotetextinsteadof\footnote.
3.9.2 Style-specificCommands
Thefollowingadditionalcitationcommandsareonlyprovidedbysomeofthecitation
styleswhichcomewiththispackage.
109

\textcite[hprenotei][hpostnotei]{hkeyi}
\Textcite[hprenotei][hpostnotei]{hkeyi}
Thesecitationcommandsareprovidedbyallstylesthatcomewiththispackage. They
areintendedforuseintheflowoftext,replacingthesubjectofasentence. Theyprint
theauthorsoreditorsfollowedbyacitationlabelwhichisenclosedinparentheses.
Dependingonthecitationstyle,thelabelmaybeanumber,theyearofpublication,
anabridgedversionofthetitle,orsomethingelse. Thenumericandalphabeticstyles
usesquarebracketsinsteadofparentheses. Intheverbosestyles,thelabelisprovided
inafootnote. Trailingpunctuationismovedbetweentheauthororeditornames
andthefootnotemark. \Textciteissimilarto\textcitebutcapitalizesthename
prefixofthefirstnameinthecitationiftheuseprefixoptionisenabled,provided
thatthereisanameprefix.
\smartcite[hprenotei][hpostnotei]{hkeyi}
\Smartcite[hprenotei][hpostnotei]{hkeyi}
Like\parenciteinafootnoteandlike\footciteinthebody.
\cite*[hprenotei][hpostnotei]{hkeyi}
Thiscommandisprovidedbyallauthor-yearandauthor-titlestyles. Itissimilarto
theregular\citecommandbutmerelyprintstheyearorthetitle,respectively.
\parencite*[hprenotei][hpostnotei]{hkeyi}
Thiscommandisprovidedbyallauthor-yearandauthor-titlestyles. Itissimilarto
theregular\parencitecommandbutmerelyprintstheyearorthetitle,respectively.
\supercite{hkeyi}
This command, which is only provided by the numeric styles, prints numeric
citations as superscripts without brackets. It uses \supercitedelim instead of
\multicitedelim as citation delimiter. Note that any hprenotei and hpostnotei ar-
gumentsareignored. Iftheyaregiven, \supercitewilldiscardthemandissuea
warningmessage.
3.9.3 QualifiedCitationLists
Thispackagesupportsaclassofspecialcitationcommandscalled‘multicite’com-
mands. The point of these commands is that their argument is a list of citations
whereeachitemformsafullyqualifiedcitationwithapre-and/orpostnote. This
isparticularlyusefulwithparentheticalcitationsandcitationsgiveninfootnotes.
Itisalsopossibletoassignapre-and/orpostnotetotheentirelist. Themulticite
commandsarebuiltontopofbackendcommandslike\parenciteand\footcite.
Thecitationstyleprovidesamulticitedefinitionwith\DeclareMultiCiteCommand
(see§4.3.1). Thefollowingexampleillustratesthesyntaxofmulticitecommands:
\parencites[35]{key1}[88--120]{key2}[23]{key3}
The format of the arguments is similar to that of the regular citation commands,
exceptthatonlyonecitationcommandisgiven. Ifonlyoneoptionalargumentis
givenforaniteminthelist,itistakenasapostnote. Ifyouwanttospecifyaprenote
butnopostnote,youneedtoleavethesecondoptionalargumentoftherespective
itemempty:
110

\parencites[35]{key1}[chapter 2 in][]{key2}[23]{key3}
Inadditiontothat,theentirecitationlistmayalsohaveapre-and/orpostnote. The
syntaxoftheseglobalnotesdiffersfromotheroptionalargumentsinthattheyare
giveninparenthesesratherthantheusualbrackets:
\parencites(and chapter 3)[35]{key1}[78]{key2}[23]{key3}
\parencites(Compare)()[35]{key1}[78]{key2}[23]{key3}
\parencites(See)(and the introduction)[35]{key1}[78]{key2}[23]{key3}
Notethatthemulticitecommandskeeponscanningforargumentsuntiltheyen-
counteratokenthatisnotthestartofanoptionalormandatoryargument. Ifaleft
braceorbracketfollowsamulticitecommand,youneedtomaskitbyadding\relax
or a control space (a backslash followed by a space) after the last valid argument.
Thiswillcausethescannertostop.
\parencites[35]{key1}[78]{key2}\relax[...]
\parencites[35]{key1}[78]{key2}\(cid:32){...}
Bydefault,thispackageprovidesthefollowingmulticitecommandswhichcorre-
spondtoregularcommandsfrom§§3.9.1and3.9.2:
\cites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\Cites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\citeand\Cite,respectively.
\parencites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\Parencites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\parenciteand\Parencite,respectively.
\footcites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\footcitetexts(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\footciteand\footcitetext,respectively.
\smartcites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\Smartcites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\smartciteand\Smartcite,respectively.
\textcites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\Textcites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\textciteand\Textcite,respectively.
\supercites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Themulticiteversionof\supercite. Thiscommandisonlyprovidedbythenumeric
styles.
111

3.9.4 Style-independentCommands
Sometimesitisdesirabletogivethecitationsinthesourcefileinaformatthatis
not tied to a specific citation style and can be modified globally in the preamble.
The format of the citations is easily changed by loading a different citation style.
However, when using commands such as \parencite or \footcite, the way the
citationsareintegratedwiththetextisstilleffectivelyhard-coded. Theideabehind
the\autocitecommandistoprovidehigher-levelcitationmarkupwhichmakes
globalswitchingfrominlinecitationstocitationsgiveninfootnotes(orassuper-
scripts) possible. The \autocite command is built on top of backend commands
like\parenciteand\footcite. Thecitationstyleprovidesan\autocitedefinition
with\DeclareAutoCiteCommand(see§4.3.1). Thisdefinitionmaybeactivatedwith
theautocitepackageoptionfrom§3.1.2.1. Thecitationstylewillusuallyinitialize
thispackageoptiontoavaluewhichissuitableforthestyle,see§3.3.1fordetails.
Notethattherearecertainlimitstohigh-levelcitationmarkup. Forexample,inline
author-yearcitationschemesoftenintegratecitationssotightlywiththetextthatit
isvirtuallyimpossibletoautomaticallyconvertthemtofootnotes. The\autocite
commandisonlyapplicableincasesinwhichyouwouldnormallyuse\parencite
or\footcite(or\supercite,withanumericstyle). Thecitationsshouldbegiven
attheendofasentenceorapartialsentence,immediatelyprecedingtheterminal
punctuationmark,andtheyshouldnotbeapartofthesentenceinagrammatical
sense(like\textcite,forexample).
\autocite[hprenotei][hpostnotei]{hkeyi}
\Autocite[hprenotei][hpostnotei]{hkeyi}
Incontrasttoothercitationcommands,the\autocitecommanddoesnotonlyscan
aheadforpunctuationmarksfollowingitslastargumenttoavoiddoublepunctuation
marks, it actually moves them around if required. For example, with autocite=
footnote,atrailingpunctuationmarkwillbemovedsuchthatthefootnotemark
isprintedafterthepunctuation. \Autociteissimilarto\autocitebutcapitalizes
thenameprefixofthefirstnameinthecitationiftheuseprefixoptionisenabled,
providedthatthereisanameprefixandthecitationstyleprintsanynameatall.
\autocite*[hprenotei][hpostnotei]{hkeyi}
\Autocite*[hprenotei][hpostnotei]{hkeyi}
Thestarredvariantsof\autocitedonotbehavedifferentlyfromtheregularones.
Theasteriskissimplypassedontothebackendcommand. Forexample,if\autocite
isconfiguredtouse\parencite,then\autocite*willexecute\parencite*.
\autocites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
\Autocites(hmultiprenotei)(hmultipostnotei)[hprenotei][hpostnotei]{hkeyi}...[hprenotei][hpostnotei]{hkeyi}
Thisisthemulticiteversionof\autocite. Italsodetectsandmovespunctuationif
required. Notethatthereisnostarredvariant. \Autocitesissimilarto\autocites
but capitalizes the name prefix of the first name in the citation if the useprefix
optionisenabled,providedthatthereisanameprefixandthecitationstyleprints
anynameatall.
112

3.9.5 TextCommands
Thefollowingcommandsareprovidedbythecoreofbiblatex. Theyareintended
foruseintheflowoftext. Notethatalltextcommandsareexcludedfromcitation
tracking.
\citeauthor[hprenotei][hpostnotei]{hkeyi}
\citeauthor*[hprenotei][hpostnotei]{hkeyi}
\Citeauthor[hprenotei][hpostnotei]{hkeyi}
\Citeauthor*[hprenotei][hpostnotei]{hkeyi}
Thesecommandsprinttheauthors. Strictlyspeaking,itprintsthelabelnamelist,
which may be the author, the editor, or the translator. \Citeauthor is similar
to \citeauthor but capitalizes the name prefix of the first name in the citation if
theuseprefixoptionisenabled,providedthatthereisanameprefix. Thestarred
variantseffectivelyforcemaxcitenamesto1forjustthiscommandonsoonlyprint
thefirstnameinthelabelnamelist(potentiallyfollowedbythe“etal”stringifthere
aremorenames). Thisallowsmorenaturaltextualflowwhenreferringtoapaperin
thesingularwhenotherwise\citeauthorwouldgeneratea(naturallyplural)listof
names.
\citetitle[hprenotei][hpostnotei]{hkeyi}
\citetitle*[hprenotei][hpostnotei]{hkeyi}
Thiscommandprintsthetitle. Itwillusetheabridgedtitleintheshorttitlefield,if
available. Otherwiseitfallsbacktothefulltitlefoundinthetitlefield. Thestarred
variantalwaysprintsthefulltitle.
\citeyear[hprenotei][hpostnotei]{hkeyi}
\citeyear*[hprenotei][hpostnotei]{hkeyi}
Thiscommandprintstheyear(yearfieldoryearcomponentofdate). Thestarred
variantincludestheextradateinformation,ifany.
\citedate[hprenotei][hpostnotei]{hkeyi}
\citedate*[hprenotei][hpostnotei]{hkeyi}
Thiscommandprintsthefulldate(dateoryear). Thestarredvariantincludesthe
extradateinformation,ifany.
\citeurl[hprenotei][hpostnotei]{hkeyi}
Thiscommandprintstheurlfield.
\parentext{htexti}
Thiscommandwrapsthehtextiincontextsensitiveparentheses.
\brackettext{htexti}
Thiscommandwrapsthehtextiincontextsensitivebrackets.
113

3.9.6 SpecialCommands
Thefollowingspecialcommandsarealsoprovidedbythecoreofbiblatex.
\nocite{hkeyi}
\nocite{*}
ThiscommandissimilartothestandardLaTeX\nocitecommand. Itaddsthehkeyi
tothebibliographywithoutprintingacitation. Ifthehkeyiisanasterisk,allentries
availableinthein-scopebibliographydatasource(s)areaddedtothebibliography.
Like all other citation commands, \nocite commands in the document body are
localtotheenclosingrefsectionenvironment,ifany. IncontrasttostandardLaTeX,
\nocitemayalsobeusedinthedocumentpreamble. Inthiscase,thereferencesare
assignedtoreferencesection0. Forthepurposesoforderingcitationsbyappearance
\nocitewillbehavelikeallothercitecommands,withtheaddedrulethata\nocite
issuedinthepreambleistreatedascomingbeforeallexplicitcitationsinreference
section0fromthedocumentbody.
\fullcite[hprenotei][hpostnotei]{hkeyi}
Thiscommandusesthebibliographydriverfortherespectiveentrytypetocreatea
fullcitationsimilartothebibliographyentry. Itisthusrelatedtothebibliography
styleratherthanthecitationstyle.
\footfullcite[hprenotei][hpostnotei]{hkeyi}
Similarto\fullcitebutputstheentirecitationinafootnoteandaddsaperiodat
theend.
\volcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Volcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Thesecommandsaresimilarto\citeand\Citebutintendedforreferencestomulti-
volumeworkswhicharecitedbyvolumeandpagenumber. Insteadofthehpostnotei,
theytakeamandatoryhvolumeiandanoptionalhpagesiargument. Sincetheymerely
composethepostnoteandpassittothe\citecommandprovidedbythecitation
styleasahpostnoteiargument,thesecommandsarestyleindependent. Thevolume
and pages/text portion are formatted with the macro \mkvolcitenote when they
arepassedontothecitationcommand. Additionallytheyaremadeavailableinthe
specialfieldsvolcitevolumeandvolcitepages(§4.3.2)Theformatofthevolume
portioniscontrolledbythefieldformattingdirectivevolcitevolume,theformatof
thepages/textportioniscontrolledbythefieldformattingdirectivevolcitepages
(§ 4.10.4). The delimiter printed between the volume portion and the pages/text
portionmaybemodifiedbyredefiningthemacro\volcitedelim(§4.10.1).
\volcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Volcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\volciteand\Volcite,respectively.
\pvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Pvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Similarto\volcitebutbasedon\parencite.
114

\pvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Pvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\pvolciteand\Pvolcite,respectively.
\fvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Fvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\ftvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Ftvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Similarto\volcitebutbasedon\footciteand\footcitetext,respectively.
\fvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Fvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\ftvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Ftvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\fvolciteand\ftvolcite,respectively.
\svolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Svolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Similarto\volcitebutbasedon\smartcite.
\svolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Svolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\svolciteand\Svolcite,respectively.
\tvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Tvolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Similarto\volcitebutbasedon\textcite.
\tvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Tvolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\tvolciteand\Tvolcite,respectively.
\avolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Avolcite[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Similarto\volcitebutbasedon\autocite.
115

\avolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
\Avolcites(hmultiprenotei)(hmultipostnotei)[hprenotei]{hvolumei}[hpagesi]{hkeyi}
...[hprenotei]{hvolumei}[hpagesi]{hkeyi}
Themulticiteversionof\avolciteand\Avolcite,respectively.
\notecite[hprenotei][hpostnotei]{hkeyi}
\Notecite[hprenotei][hpostnotei]{hkeyi}
Thesecommandsprintthehprenoteiandhpostnoteiargumentsbutnocitation. This
maybeusefulforauthorswhoincorporateimplicitcitationsintheirwriting,only
givinginformationnotmentionedbeforeintherunningtext,butwhostillwantto
takeadvantageoftheautomatichpostnoteiformattingandcitationtracking. Thisis
ageneric,style-independentcitationcommand. Specialcitationstylesmayprovide
smarterfacilitiesforthesamepurpose. Thecapitalizedversionforcescapitalization
(notethatthisisonlyapplicableifthenotestartswithacommandwhichissensitive
tobiblatex’spunctuationtracker).
\pnotecite[hprenotei][hpostnotei]{hkeyi}
\Pnotecite[hprenotei][hpostnotei]{hkeyi}
Similarto\notecitebutthenotesareprintedinparentheses.
\fnotecite[hprenotei][hpostnotei]{hkeyi}
Similarto\notecitebutthenotesareprintedinafootnote.
3.9.7 Low-levelCommands
The following commands are also provided by the core of biblatex. They grant
accesstoalllistsandfieldsatalowerlevel.
\citename[hprenotei][hpostnotei]{hkeyi}[hformati]{hnamelisti}
Thehformatiisaformattingdirectivedefinedwith\DeclareNameFormat. Formatting
directivesarediscussedin§4.4.2. Ifthisoptionalargumentisomitted,thiscommand
fallsbacktotheformatcitename. Thelastargumentisthenameofahnamelisti,in
thesenseexplainedin§2.2.
\citelist[hprenotei][hpostnotei]{hkeyi}[hformati]{hliterallisti}
Thehformatiisaformattingdirectivedefinedwith\DeclareListFormat. Formatting
directivesarediscussedin§4.4.2. Ifthisoptionalargumentisomitted,thiscommand
fallsbacktotheformatcitelist. Thelastargumentisthenameofahliterallisti,in
thesenseexplainedin§2.2.
\citefield[hprenotei][hpostnotei]{hkeyi}[hformati]{hfieldi}
Thehformatiisaformattingdirectivedefinedwith\DeclareFieldFormat. Format-
ting directives are discussed in § 4.4.2. If this optional argument is omitted, this
commandfallsbacktotheformatcitefield. Thelastargumentisthenameofa
hfieldi,inthesenseexplainedin§2.2.
116

3.9.8 MiscellaneousCommands
Thecommandsinthissectionarelittlehelpersrelatedtocitations.
\citereset This command resets the citation style. This may be useful if the style replaces
repeatedcitationswithabbreviationslikeibidem,idem,op. cit.,etc. andyouwant
to force a full citation at the beginning of a new chapter, section, or some other
location. Thecommandexecutesastylespecificinitializationhookdefinedwiththe
\InitializeCitationStylecommandfrom§4.3.1. Italsoresetstheinternalcita-
tiontrackersofthispackage. Theresetwillaffectthe\ifciteseen,\ifentryseen,
\ifciteibid, and \ifciteidem tests discussed in § 4.6.2. When used inside a
refsection environment, the reset of the citation tracker is local to the current
refsectionenvironment. Alsoseetheciteresetpackageoptionin§3.1.2.1.
\citereset* Similar to \citereset but only executes the style’s initialization hook, without
resettingtheinternalcitationtrackers.
\mancite Use this command to mark manually inserted citations if you mix automatically
generatedandmanualcitations. Thisisparticularlyusefulifthecitationstylere-
placesrepeatedcitationsbyanabbreviationlikeibidemwhichmaygetambiguous
ormisleadingotherwise. Alwaysuse\manciteinthesamecontextasthemanual
citation, e.g., if the citation is given in a footnote, include \mancite in the foot-
note. The \mancite command executes a style specific reset hook defined with
the\OnManualCitationcommandfrom§4.3.1. Italsoresetstheinternal‘ibidem’
and ‘idem’ trackers of this package. The reset will affect the \ifciteibid and
\ifciteidemtestsdiscussedin§4.6.2.
\pno Thiscommandforcesasinglepageprefixinthehpostnoteiargumenttoacitation
command. See § 3.15.3 for further details and usage instructions. Note that this
commandisonlyavailablelocallyincitationsandthebibliography.
\ppno Similarto\pnobutforcesarangeprefix. See§3.15.3forfurtherdetailsandusage
instructions. Notethatthiscommandisonlyavailablelocallyincitationsandthe
bibliography.
\nopp Similarto\pnobutsuppressesallprefixes. See§3.15.3forfurtherdetailsandusage
instructions. Notethatthiscommandisonlyavailablelocallyincitationsandthe
bibliography.
\psq Inthehpostnoteiargumenttoacitationcommand,thiscommandindicatesarangeof
twopageswhereonlythestartingpageisgiven. See§3.15.3forfurtherdetailsand
usageinstructions. Thesuffixprintedisthelocalisationstringsequens,see§4.9.2.
Thespacinginsertedbetweenthesuffixandthepagenumbermaybemodifiedby
redefiningthemacro\sqspace. Thedefaultisanunbreakableinterwordspace. Note
thatthiscommandisonlyavailablelocallyincitationsandthebibliography.
Note also that you might want to use the option citepagerange (see § 3.1.2.1) to
automatizetheuseofthiscommandratherthanenteringitmanually.
\psqq Similarto\psqbut,dependingontheconvention,indicateseitherarangeofthree
pagesoranopen-endedpagerangegreaterthantwopages. See§3.15.3forfurther
detailsandusageinstructions. Thesuffixprintedisthelocalisationstringsequentes,
see§4.9.2. Thiscommandisonlyavailablelocallyincitationsandthebibliography.
Note also that you might want to use the option citepagerange (see § 3.1.2.1) to
automatizetheuseofthiscommandratherthanenteringitmanually.
117

\pnfmt{htexti}
This command formats its argument htexti in the same format as postnote. The
commandcanbeusedtoformatapagerangewhileaddingadditionaltextinthe
postnoteargumentofacitecommand.
\autocite[\pnfmt{378-381, 383} and more]{sigfridsson}
\RN{hintegeri}
ThiscommandprintsanintegerasanuppercaseRomannumeral. Theformatting
appliedtothenumeralmaybemodifiedbyredefiningthemacro\RNfont.
\Rn{hintegeri}
Similarto\RNbutprintsalowercaseRomannumeral. Theformattingappliedtothe
numeralmaybemodifiedbyredefiningthemacro\Rnfont.
3.9.9 natbibCompatibilityCommands
Thenatbibpackageoptionloadsa natbibcompatibilitymodule. Themodulede-
fines aliases for the citation commands provided by the natbib package. This in-
cludes aliases for the core citation commands \citet and \citep as well as the
variants \citealt and \citealp. The starred variants of these commands, which
print the full author list, are also supported. The \cite command, which is han-
dled in a particular way by natbib, is not treated in a special way. The text com-
mands (\citeauthor, \citeyear, etc.) are also supported, as are all commands
whichcapitalizethenameprefix(\Citet,\Citep,\Citeauthor,etc.). Aliasingwith
\defcitealias, \citetalias, and \citepalias is possible as well. Note that the
compatibilitycommandswillnotemulatethecitationformatofthenatbibpackage.
They merely alias natbib’s commands to functionally equivalent facilities of the
biblatexpackage. Thecitationformatdependsonthemaincitationstyle. However,
thecompatibilitystylewilladapt\nameyeardelimtomatchthedefaultstyleofthe
natbibpackage.
3.9.10 mcite-likeCitationCommands
The mcite package option loads a special citation module which provides mcite/
mciteplus-likecitationcommands. Strictlyspeaking,whatthemoduleprovidesare
wrappersforthecommandsofthemaincitationstyle. Forexample,thefollowing
command:
\mcite{key1,setA,*keyA1,*keyA2,*keyA3,key2,setB,*keyB1,*keyB2,*keyB3}
isessentiallyequivalenttothis:
\defbibentryset{setA}{keyA1,keyA2,keyA3}%
\defbibentryset{setB}{keyB1,keyB2,keyB3}%
\cite{key1,setA,key2,setB}
118

Table8:mcite-likecommands
StandardCommand mcite-likeCommand
\cite \mcite
\Cite \Mcite
\parencite \mparencite
\Parencite \Mparencite
\footcite \mfootcite
\footcitetext \mfootcitetext
\textcite \mtextcite
\Textcite \Mtextcite
\supercite \msupercite
\autocite \mautocite
\Autocite \Mautocite
The\mcitecommandwillworkwithanystylesincethe\citebackendcommandis
controlledbythemaincitationstyleasusual. Themcitemoduleprovideswrappers
forthestandardcommandsin§§3.9.1and3.9.2. Seetable9foranoverview. Pre
andpostnotesaswellasstarredvariantsofallcommandsarealsosupported. The
parameterswillbepassedtothebackendcommand. Forexample:
\mcite*[pre][post]{setA,*keyA1,*keyA2,*keyA3}
willexecute:
\defbibentryset{setA}{keyA1,keyA2,keyA3}%
\cite*[pre][post]{setA}
Notethatthemcitemoduleisnotacompatibilitymodule. Itprovidescommands
whichareverysimilarbutnotidenticalinsyntaxandfunctiontomcite’scommands.
Whenmigratingfrommcite/mciteplustobiblatex,legacyfilesmustbeupdated.
Withmcite,thefirstmemberofthecitationgroupisalsotheidentifierofthegroup
asawhole. Borrowinganexamplefromthemcitemanual,thisgroup:
\cite{glashow,*salam,*weinberg}
consistsofthreeentriesandtheentrykeyofthefirstonealsoservesasidentifier
oftheentiregroup. Incontrasttothat,abiblatexentrysetisanentityinitsown
right. Therefore,itrequiresauniqueentrykeywhichisassignedtothesetasitis
defined:
\mcite{set1,*glashow,*salam,*weinberg}
Oncedefined,anentrysetishandledlikeanyregularentryinabibfile. Whenusing
one of the numeric styles which come with biblatex and activating its subentry
option,itisevenpossibletorefertosetmembers. Seetable9forsomeexamples.
Restatingtheoriginaldefinitionofthesetisredundant,butpermissible. Incontrast
tomciteplus,however,restatingapartoftheoriginaldefinitionisinvalid. Usethe
entrykeyofthesetinstead.
119

Table9:mcite-likesyntax(sampleoutputwithstyle=numericandsubentry
option)
Input Output Comment
\mcite{set1,*glashow,*salam,*weinberg} [1] Definingandcitingtheset
\mcite{set1} [1] Subsequentcitationoftheset
\cite{set1} [1] Regular\citeworksasusual
\mcite{set1,*glashow,*salam,*weinberg} [1] Redundant,butpermissible
\mcite{glashow} [1a] Citingasetmember
\cite{weinberg} [1c] Regular\citeworksaswell
3.10 LocalizationCommands
Thebiblatexpackageprovidestranslationsforkeytermssuchas‘edition’or‘vol-
ume’ as well as definitions for language specific features such as the date format
andordinals. Thesedefinitions,whichareloadedautomatically,maybemodifiedor
extendedinthedocumentpreambleortheconfigurationfilewiththecommands
introducedinthissection.
\DefineBibliographyStrings{hlanguagei}{hdefinitionsi}
This command is used to define localisation strings. The hlanguagei must be a
languagenameknowntothebabel/polyglossiapackages,i.e.,oneoftheidentifiers
listedintable2onpage29. Thehdefinitionsiarehkeyi=hvalueipairswhichassign
anexpressiontoanidentifier:
\DefineBibliographyStrings{american}{%
bibliography = {Bibliography},
shorthands = {Abbreviations},
editor = {editor},
editors = {editors},
}
A complete list of all keys supported by default is given is § 4.9.2. Note that all
expressions should be capitalized as they usually are when used in the middle
of a sentence. The biblatex package will automatically capitalize the first word
when required at the beginning of a sentence. Expressions intended for use in
headings should be capitalized in a way that is suitable for titling. In contrast to
\DeclareBibliographyStrings,\DefineBibliographyStringsoverridesboththe
fullandtheabbreviatedversionofthestring. See§4.9.1forfurtherdetails.
\DefineBibliographyExtras{hlanguagei}{hcodei}
Thiscommandisusedtoadaptlanguagespecificfeaturessuchasthedateformatand
ordinals. Thehlanguageimustbealanguagenameknowntothebabel/polyglossia
packages. Thehcodei,whichmaybearbitraryLaTeXcode,willusuallyconsistof
redefinitionsoftheformattingcommandsfrom§3.12.3.
\UndefineBibliographyExtras{hlanguagei}{hcodei}
Thiscommandisusedtorestoretheoriginaldefinitionofanycommandsmodified
with\DefineBibliographyExtras. Ifaredefinedcommandisincludedin§3.12.3,
thereisnoneedtorestoreitspreviousdefinitionsincethesecommandsareadapted
byalllanguagemodulesanyway.
120

\DefineHyphenationExceptions{hlanguagei}{htexti}
This is a LaTeX frontend to TeX’s \hyphenation command which defines hy-
phenation exceptions. The hlanguagei must be a language name known to the
babel/polyglossia packages. The htexti is a whitespace-separated list of words.
Hyphenationpointsaremarkedwithadash:
\DefineHyphenationExceptions{american}{%
hy-phen-ation ex-cep-tion
}
\NewBibliographyString{hkeyi}
Thiscommanddeclaresnewlocalisationstrings,i.e.,itinitializesanewhkeyitobe
usedinthehdefinitionsiof\DefineBibliographyStrings. Thehkeyiargumentmay
alsobeacomma-separatedlistofkeynames. Thekeyslistedin§4.9.2aredefined
bydefault.
3.11 EntryQueryingCommands
Thecommandsinthissectionareuser-facingequivalentsoftheidentically-named
commandsinsection§4.6.2. Theycanbeusedtotestforthepresenceandattributes
ofspecificbibliographyentries. Seesection§4.6.2forusage.
\ifentryseen{hentrykeyi}{htruei}{hfalsei}
\ifentryinbib{hentrykeyi}{htruei}{hfalsei}
\ifentrycategory{hentrykeyi}{hcategoryi}{htruei}{hfalsei}
\ifentrykeyword{hentrykeyi}{hkeywordi}{htruei}{hfalsei}
3.12 FormattingCommands
The commands and facilities presented in this section may be used to adapt the
formatofcitationsandthebibliography.
3.12.1 GenericCommandsandHooks
Thecommandsinthissectionmayberedefinedwith\renewcommandinthedocument
preamble. Thosemarkedas‘ContextSensitive’inthemargincanalso(andgenerally
should)becustomisedwith\DeclareDelimFormatandareprintedwith\printdelim
(§3.12.2). Notethatallcommandsstartingwith\mk…takeoneargument. Allofthese
commandsaredefinedinbiblatex.def.
\bibsetup Arbitrary code to be executed at the beginning of the bibliography, intended for
commandswhichaffectthelayoutofthebibliography.
\bibfont Arbitrary code setting the font used in the bibliography. This is very similar to
\bibsetupbutintendedforswitchingfonts.
\citesetup Arbitrarycodetobeexecutedatthebeginningofeachcitationcommand.
\newblockpunct Theseparatorinsertedbetween‘blocks’inthesenseexplainedin§4.7.1. Thedefault
definitioniscontrolledbythepackageoptionblock(see§3.1.2.1).
121

\newunitpunct Theseparatorinsertedbetween‘units’inthesenseexplainedin§4.7.1. Thiswill
usuallybeaperiodoracommaplusaninterwordspace. Thedefaultdefinitionisa
periodandaspace.
\finentrypunct Thepunctuationprintedattheveryendofeverybibliographyentry,usuallyaperiod.
Thedefaultdefinitionisaperiod.
\entrysetpunct Thepunctuationprintedbetweenbibliographysubentriesofanentryset. Thedefault
definitionisasemicolonandaspace.
\bibnamedelima Thisdelimitercontrolsthespacingbetweentheelementswhichmakeupanamepart.
Itisinsertedautomaticallybythebackendafterthefirstnameelementiftheelement
islessthanthreecharacterslongandbeforethelastelement. Thedefaultdefinition
is\addhighpenspace, i.e., aspacepenalizedbythevalueofthehighnamepenalty
counter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimb Thisdelimitercontrolsthespacingbetweentheelementswhichmakeupaname
part. Itisinsertedautomaticallybythebackendbetweenallnameelementswhere
\bibnamedelimadoesnotapply. Thedefaultdefinitionis\addlowpenspace,i.e.,a
spacepenalizedbythevalueofthelownamepenaltycounter(§3.12.4). Pleaserefer
to§3.15.4forfurtherdetails.
\bibnamedelimc Thisdelimitercontrolsthespacingbetweennameparts. Thedefaultnameformats
use it between the name prefix and the family name if useprefix=true. The de-
fault definition is \addhighpenspace, i.e., a space penalized by the value of the
highnamepenaltycounter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimd Thisdelimitercontrolsthespacingbetweennameparts. Thedefaultnameformatsuse
itbetweenallnamepartswhere\bibnamedelimcdoesnotapply. Thedefaultdefini-
tionis\addlowpenspace,i.e.,aspacepenalizedbythevalueofthelownamepenalty
counter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimi Thisdelimiterreplaces\bibnamedelima/bafterinitials. Notethatthisonlyapplies
toinitialsgivenassuchinthebibfile,nottotheinitialsautomaticallygeneratedby
biblatexwhichusetheirownsetofdelimiters.
\bibinitperiod The punctuation inserted automatically by the backend after all initials unless
\bibinithyphendelimapplies. Thedefaultdefinitionisaperiod(\adddot). Please
referto§3.15.4forfurtherdetails.
\bibinitdelim Thespacinginsertedautomaticallybythebackendbetweenmultipleinitialsunless
\bibinithyphendelimapplies. Thedefaultdefinitionisanunbreakableinterword
space. Pleasereferto§3.15.4forfurtherdetails.
\bibinithyphendelim Thepunctuationinsertedautomaticallybythebackendbetweentheinitialsof
hyphenatednameparts,replacing\bibinitperiodand\bibinitdelim. Thedefault
definitionisaperiodfollowedbyanunbreakablehyphen. Pleasereferto§3.15.4for
furtherdetails.
\bibindexnamedelima Replaces\bibnamedelimaintheindex.
\bibindexnamedelimb Replaces\bibnamedelimbintheindex.
\bibindexnamedelimc Replaces\bibnamedelimcintheindex.
\bibindexnamedelimd Replaces\bibnamedelimdintheindex.
122

\bibindexnamedelimi Replaces\bibnamedelimiintheindex.
\bibindexinitperiod Replaces\bibinitperiodintheindex.
\bibindexinitdelim Replaces\bibinitdelimintheindex.
\bibindexinithyphendelim Replaces\bibinithyphendelimintheindex.
\revsdnamepunct The punctuation to be printed between the given and family name parts when a
nameisreversed. Thedefaultisacomma. Hereisanexampleshowinganamewith
thedefaultcommaas\revsdnamedelim:
Jones, Edward
Thiscommandshouldbeusedwith\bibnamedelimdasareversed-nameseparator
informattingdirectivesfornamelists. Pleasereferto§3.15.4forfurtherdetails.
\bibnamedash Thedashtobeusedasareplacementforrecurrentauthorsoreditorsinthebiblio-
graphy. Thedefaultisan‘em’oran‘en’dash,dependingontheindentationofthe
listofreferences.
\labelnamepunct A separator to be printed after the name used for alphabetizing in the bibliogra- Deprecated
phy(authororeditor,iftheauthorfieldisundefined)insteadof\newunitpunct.
The default is \newunitpunct, i.e., it is not handled differently from regular unit
punctuationbutpermitsconvenientreconfiguration. Thispunctuationcommand
isdeprecatedandhasbeensupersededbythecontext-sensitive\nametitledelim
(see§3.12.2). Forbackwardscompatibilityreasons,however,\nametitledelimstill
defaults to \labelnamepunct in the bib and biblist contexts. Style authors may
want to consider replacing \labelnampunct with \printdelim{nametitledelim}
andusersmaywanttoprefermodifyingthecontext-sensitivenametitledelimin
thebibcontextwith\DeclareDelimFormatoverredefining\labelnamepunct,e.g.,
\DeclareDelimFormat[bib]{nametitledelim}{%
\addcolon\space}
\subtitlepunct The separator printed between the fields title and subtitle, booktitle and
booksubtitle, as well as maintitle and mainsubtitle. With the default styles,
this separator replaces \newunitpunct at this location. The default definition is
\newunitpunct,i.e.,itisnothandleddifferentlyfromregularunitpunctuation.
\intitlepunct Theseparatorbetweentheword“in”andthefollowingtitleinentrytypessuchas
@article, @inbook, @incollection, etc. The default definition is a colon plus an
interwordspace(e.g.,“Article,in: Journal”or“Title,in: Book”). Notethatthisisthe
separatorstring,notonlythepunctuationmark. Ifyoudon’twantacolonafter“in”,
\intitlepunctshouldstillinsertaspace.
\bibpagespunct Theseparatorprintedbeforethepagesfield. Thedefaultisacommaplusaninterword
space.
\bibpagerefpunct Theseparatorprintedbeforethepagereffield. Thedefaultisaninterwordspace.
\bibeidpunct Theseparatorprintedbeforetheeidfield(similarto\bibpagespunct). Thedefault
isacommaplusaninterwordspace.
123

\multinamedelim Thedelimiterprintedbetweenmultipleitemsinanamelistlikeauthororeditorif ContextSensitive
therearemorethantwonamesinthelist. Thedefaultisacommaplusaninterword
space. See\finalnamedelimforanexample.24
\finalnamedelim Thedelimiterprintedinsteadof\multinamedelimbeforethefinalnameinaname ContextSensitive
list. Thedefaultisthelocalisedterm‘and’,separatedbyinterwordspaces. Hereis
anexample:
Michel Goossens, Frank Mittelbach and Alexander Samarin
Edward Jones and Joe Williams
Thecommainthefirstexampleisthe\multinamedelimwhereasthestring‘and’in
bothexamplesisthe\finalnamedelim. Seealso\finalandcommain§3.12.3.
\revsdnamedelim An extra delimiter printed after the first name in a name list if the first name is ContextSensitive
reversed(onlyinlistswithtwonames). Thedefaultisanemptystring,i.e.,noextra
delimiterwillbeprinted. Hereisanexampleshowinganamelistwithacommaas
\revsdnamedelim:
Jones, Edward, and Joe Williams
In this example, the comma after ‘Edward’ is the \revsdnamedelim whereas the
string‘and’isthe\finalnamedelim,printedinadditiontotheformer.
\andothersdelim The delimiter printed before the localisation string ‘andothers’ if a name list like ContextSensitive
authororeditoristruncated. Thedefaultisaninterwordspace.
\multilistdelim The delimiter printed between multiple items in a literal list like publisher or ContextSensitive
location if there are more than two items in the list. The default is a comma
plusaninterwordspace. See\multinamedelimforfurtherexplanation.
\finallistdelim Thedelimiterprintedinsteadof\multilistdelimbeforethefinaliteminaliteral ContextSensitive
list. The default is the localised term ‘and’, separated by interword spaces. See
\finalnamedelimforfurtherexplanation.
\andmoredelim The delimiter printed before the localisation string ‘andmore’ if a literal list like ContextSensitive
publisherorlocationistruncated. Thedefaultisaninterwordspace.
\multicitedelim Thedelimiterprintedbetweencitationsifmultipleentrykeysarepassedtoasingle
citationcommand. Thedefaultisasemicolonplusaninterwordspace.
\multiciterangedelim Thedelimiterprintedbetweentwocitationsiftheyarecompressedtoarange.
Thedefaultis\bibrangedash.
\multicitesubentrydelim Thedelimiterprintedbetweensubentrycitationsofthesameset. Thisde-
limiterisonlyusedincitationstylesthatreducecitationsofthesamesettoamore
compactform(subentryofnumeric-comp). Thedefaultisacomma.
\multicitesubentryrangedelim Thedelimiterprintedbetweentwocitationsofthesamesetiftheyare
compressedtoarange. Thedefaultis\multiciterangedelim.
24Notethat\multinamedelimisnotusedatallifthereareonlytwonamesinthelist. Inthiscase,the
defaultstylesusethe\finalnamedelim.
124

\supercitedelim Similarto\multicitedelim,butusedbythe\supercitecommandonly. Thedefault
isacomma.
\superciterangedelim Analogue of \multiciterangedelim for \supercite. The default is
\bibrangedash.
\supercitesubentrydelim Analogue of \multicitesubentrydelim for \supercite. The default is
\supercitedelim.
\supercitesubentryrangedelim Analogueof\multicitesubentryrangedelimfor\supercite. Thede-
faultis\superciterangedelim.
\compcitedelim Similarto\multicitedelim,butusedbycertaincitationstyleswhen‘compressing’
multiplecitations. Thedefaultdefinitionisacommaplusaninterwordspace.
\textcitedelim Similarto\multicitedelim,butusedby\textciteandrelatedcommands(§3.9.2).
The default is a comma plus an interword space. The standard styles modify this
provisional definition to ensure that the delimiter before the final citation is the
localisedterm‘and’,separatedbyinterwordspaces. Seealso\finalandcommaand
\finalandsemicolonin§3.12.3.
\nametitledelim The delimiter printed between the author/editor and the title by author-title and ContextSensitive
someverbosecitationstylesandinthebibliography. Inauthor-yearbibliography
stylesthisdelimiterisplacedaftertheauthor/editorandyearandbeforethetitle.
Thedefaultdefinitioninsidebibliographiesisthenowdeprecated\labelnamepunct
andisacommaplusaninterwordspaceotherwise.
\nameyeardelim Thedelimiterprintedbetweentheauthor/editorandtheyearbyauthor-yearcitation ContextSensitive
andbibliographystyles. Thedefaultdefinitionisaninterwordspace.
\namelabeldelim Thedelimiterprintedbetweenthename/titleandthelabelbyalphabeticandnumeric ContextSensitive
citationstyles. Thedefaultdefinitionisaninterwordspace.
\nonameyeardelim The delimiter printed between the substitute for the labelname when it does not ContextSensitive
exist(usuallythelabelortitleinstandardstyles)andtheyearinauthor-yearcitation
andbibliographystyles. Thisisonlyusedwhenthereisnolabelnamesincewhen
thelabelnameexists,\nameyeardelimisused. Thedefaultdefinitionisaninterword
space.
\authortypedelim The delimiter printed between the author and the authortype. The default is a ContextSensitive
commafollowedbyaspace.
\editortypedelim Thedelimiterprintedbetweentheeditorandtheeditororeditortypestring. The ContextSensitive
defaultisacommafollowedbyaspace.
\translatortypedelim The delimiter printed between the translator and the translator string. The ContextSensitive
defaultisacommafollowedbyaspace.
\labelalphaothers Astringtobeappendedtothenon-numericportionofthelabelalphafield(i.e.,
thefieldholdingthecitationlabelusedbyalphabeticcitationstyles)ifthenumber
ofauthors/editorsexceedsthemaxalphanamesthresholdortheauthor/editorlist
wastruncatedinthebibfilewiththekeyword‘and others’. Thiswilltypicallybea
singlecharactersuchasaplussignoranasterisk. Thedefaultisaplussign. This
commandmayalsoberedefinedtoanemptystringtodisablethisfeature. Inany
case,itmustberedefinedinthepreamble.
125

\sortalphaothers Similarto\labelalphaothersbutusedinthesortingprocess. Settingittoadifferent
valueisadvisableifthelattercontainsformattingcommands,forexample:
\renewcommand*{\labelalphaothers}{\textbf{+}}
\renewcommand*{\sortalphaothers}{+}
If\sortalphaothersisnotredefined,itdefaultsto\labelalphaothers.
\volcitedelim The delimiter printed between the volume portion and the page/text portion of
\volciteandrelatedcommands(§3.9.6).
\mkvolcitenote{hvolumei}{hpagesi}
This macro formats the hvolumei and hpagesi arguments of \volcite and related
commands(§3.9.6)whentheyarepassedontotheunderlyingcitationcommand.
\prenotedelim Thedelimiterprintedafterthehprenoteiargumentofacitationcommand. See§3.9 ContextSensitive
fordetails. Thedefaultisaninterwordspace.
\postnotedelim The delimiter printed before the hpostnotei argument of a citation command. See ContextSensitive
§3.9fordetails. Thedefaultisacommaplusaninterwordspace.
\extpostnotedelim Thedelimiterprintedbetweenthecitationandtheparentheticalhpostnoteiargument ContextSensitive
ofacitationcommandwhenthepostnoteoccursoutsideofthecitationparentheses.
Inthestandardstyles,thisoccurswhenthecitationusestheshorthandfieldofthe
entry. See§3.9fordetails. Thedefaultisaninterwordspace.
\multiprenotedelim The delimiter printed after the hmultiprenotei argument of a citation command. ContextSensitive
See§3.9fordetails. Thedefaultis\prenotedelim.
\multipostnotedelim Thedelimiterprintedbeforethehmultipostnoteiargumentofacitationcommand. ContextSensitive
See§3.9fordetails. Thedefaultis\postnotedelim.
\mkbibname‘namepart’{htexti}Thiscommand,whichtakesoneargument,isusedtoformatthenamepart
‘namepart’ofnamelistfields. Thedefaultdatamodeldefinesthenameparts‘family’,
‘given’, ‘prefix’ and ‘suffix’ and therefore the following macros are automatically
defined:
\mkbibnamefamily
\mkbibnamegiven
\mkbibnameprefix
\mkbibnamesuffix
ForbackwardscompatibilitywiththelegacyBibTeXnameparts,thefollowingare
alsodefined,willgeneratewarningsandwillsetthecorrectmacro:
\mkbibnamelast
\mkbibnamefirst
\mkbibnameaffix
\mkbibcompletenamefamily{htexti}This command, which takes one argument, is used to format the
completenameinfamilyformatorder.
126

\mkbibcompletenamefamilygiven{htexti}This command, which takes one argument, is used to format
thecompletenameinfamily-givenformatorder.
\mkbibcompletenamegivenfamily{htexti}This command, which takes one argument, is used to format
thecompletenameingiven-familyformatorder.
\mkbibcompletename{htexti}The initial value of all default formatting hooks
\mkbibcompletename‘formatorder’.
\datecircadelim When formatting dates with the global option datecirca enabled, the delimiter ContextSensitive
printedafteranylocalised‘circa’term. Defaultstointerwordspace.
\dateeradelim When formatting dates with the global option dateera set, the delimiter printed ContextSensitive
beforethelocalisationeraterm. Defaultstointerwordspace.
\dateuncertainprint Prints date uncertainty information when the global option dateuncertain is
enabled and the \ifdateuncertain test is true. By default, prints the language
specific\bibdateuncertainstring(§3.12.3).
\enddateuncertainprint Printsdateuncertaintyinformationwhentheglobaloptiondateuncertainis
enabledandthe\ifenddateuncertaintestistrue. Bydefault,printsthelanguage
specific\bibdateuncertainstring(§3.12.3).
\datecircaprint Printsdatecircainformationwhentheglobaloptiondatecircaisenabledandthe
\ifdatecircatestistrue. Bydefault,printsthe‘circa’localisedterm(§4.9.2.21)and
thedatecircadelimdelimiter.
\enddatecircaprint Printsdatecircainformationwhentheglobaloptiondatecircaisenabledandthe
\ifenddatecircatestistrue. Bydefault,printsthe‘circa’localisedterm(§4.9.2.21)
andthedatecircadelimdelimiter.
\datecircaprintiso Printsiso8601-2formatdatecircainformationwhentheglobaloptiondatecirca
isenabledandthe\ifdatecircatestistrue. Prints\textasciitilde.
\enddatecircaprintiso Prints iso8601-2 format date circa information when the global option
datecircaisenabledandthe\ifenddatecircatestistrue. Prints\textasciitilde.
\dateeraprint{hyearfieldi}Prints date era information when the global option dateera is set to
‘secular’or‘christian’. Bydefault,printsthedateeradelimdelimiterandtheappro-
priatelocalisederaterm(§4.9.2.21). Ifthedateeraautooptionisset,thenthepassed
hyearfieldi(whichisthenameofayearfieldsuchas‘year’,‘origyear’,‘endeventyear’
etc.) istestedtoseeifitsvalueisearlierthanthedateeraautothresholdandifso,
thentheBCE/CElocalisationwillbeoutputtoo. Thedefaultsettingfordateeraauto
is 0 and so only BCE/BC localisation strings are candidates for output. Detects
whether the start or end year era information is to be printed by looking at the
hyearfieldinamepassedtoit.
\dateeraprintpre Printsdateerainformationwhentheglobaloptiondateeraissetto‘astronomical’.
By default, prints bibdataeraprefix. Detects whether the start or end year era
informationistobeprintedbylookingatthehyearfieldinamepassedtoit.
\relatedpunct Theseparatorbetweentherelatedtypebibliographylocalisationstringandthedata
fromthefirstrelatedentry. Hereisanexamplewith\relatedpunctsettoadash:
A. Smith. Title. 2000, (Orig. pub. as-Origtitle)
127

\relateddelim The generic separator between the data of multiple related entries. The default
definitionisanoptionaldotpluslinebreak. HereisanexamplewherevolumesA-E
arerelatedentriesofthe5volumemainwork:
Donald E. Knuth. Computers & Typesetting. 5 vols. Reading, Mass.:
,→ Addison-Wesley, 1984-1986.
Vol. A: The TEXbook. 1984.
Vol. B: TEX: The Program. 1986.
Vol. C: The METAFONTbook. By. 1986.
Vol. D: METAFONT: The Program. 1986.
Vol. E: Computer Modern Typefaces. 1986.
\relateddelim<relatedtype> Theseparatorbetweenthedataofmultiplerelatedentriesinsiderelated
entries of type ‘relatedtype’. There is no default, if such a type-specific delimiter
doesnotexist,\relateddelimisused.
\begrelateddelim Thegenericseparatorbeforetheblockofrelatedentries. Thedefaultdefinitionis
\newunitpunct.
\begrelateddelim<relatedtype> The separator between the block of related entries of type ‘re-
latedtype’. There is no default, if such a type-specific delimiter does not exist,
\relateddelimisused.
3.12.2 Context-sensitiveDelimiters
Manydelimitersdescribedin§3.12.1aregloballydefined. Thatis,nomatterwhere
you use them, they print the same thing. This is not necessarily desirable for de-
limiterswhichyoumightwanttoprintdifferentthingsindifferentcontexts. Here
‘context’ means things like ‘inside a text citation’ or ‘inside a bibliography item’.
Forthisreason,biblatexprovidesamoresophisticateddelimiterspecificationand
user interface alongside the standard one based on normal macros defined with
\newcommand.
Forbackwardscompatibilityreasonsallcontext-sensitivedelimiters(i.e.,alldelim-
itersmarkedas‘contextsensitive’in§3.12.1)canberedefinedwith\renewcommand
intheglobalcontext. Itis,however,stronglyrecommendedtousetheinterfacedoc-
umentedbelow(primarily\DeclareDelimFormat)toredefinethesedelimiters—even
if\renewcommandwouldsufficeforthejobathand.
\DeclareDelimFormat[hcontext,…i]{hnamei}{hcodei}
\DeclareDelimFormat*[hcontext,…i]{hnamei}{hcodei}
Declaresthedelimitermacrohnameiwiththereplacementtexthcodei. Iftheoptional
comma-separatedlistofhcontextsiisgiven,declarehnameionlyforthosecontexts.
hnameidefinedwithoutanyhcontextsibehavesjustliketheglobaldelimiterdefini-
tionswhich\newcommandgives—justaplainmacrowithareplacementwhichcanbe
usedas\name. However,youcanalsocalldelimitermacrosdefinedinthiswayby
using\printdelim,whichiscontext-aware. Thestarredversionclearsallhcontexti
specificdeclarationsforallhnamesifirst.
128

\DeclareDelimAlias[haliascontext,…i]{haliasi}[hdelimcontexti]{hdelimi}
Declares haliasi to be an alias for the delimiter hdelimi. If the optional
haliascontext,…i nor hdelimcontexti are given, the assignment is performed for
allexistingcontextsofthetargethdelimiseparately,sothathaliasibecomesanexact
copyofhdelimiinallcontexts. Ifonlythesecondoptionalargumenthdelimcontexti
isgiven,allexistingcontextsofhaliasiwillbeclearedandtheglobal/emptycontext
becomesanaliasofhdelimiinthecontexthdelimcontexti. Thefirstoptionalargu-
menthaliascontext,…imayholdalistofcontextsforwhichthealiasisassigned. In
thatcasethesecondoptionalargumenthdelimcontextispecifiesthecontextofthe
targetdelimiter. Thisargumentmaynotbealist,itcanonlyholdonecontext. Ifitis
missing,thehaliascontextiisassumed(ifhaliascontextiisalist,theassignmentis
performedseparatelyforeachlistitem),ifitisemptytheglobalcontextisused.
\DeclareDelimAlias[bib,biblist]{finalnamedelim}[]{multinamedelim}
Defines the bib and biblist contexts of \finalnamedelim as aliases of
\multinamedeliminglobalcontext. Ontheotherhand
\DeclareDelimAlias[bib,biblist]{finalnamedelim}{multinamedelim}
defines \finalnamedelim in the context bib to be an alias of \multinamedelim in
thebibcontextanddefines\finalnamedeliminbiblistcontexttobeanaliasof
\multinamedeliminbiblist.
\DeclareDelimAlias*[haliascontext,…i]{haliasi}[hdelimcontexti]{hdelimi}
Deprecated
Thestarredversionof\DeclareDelimAliasisdeprecatedinfavourofusingunstarred
\DeclareDelimAliaswithoptionalarguments.
It assigns the delimiter alias for specific contexts only. The first optional argu-
ment haliascontexti holds a list of contexts for which the assignment is going to
beperformed. Ifitisemptyormissingtheglobal/emptycontextisassumed. The
secondoptionalargumenthdelimcontextispecifiesthecontextofthetargetdelimiter.
This argument may not be a list, it can only hold one context. If it is missing the
haliascontexti is assumed (if haliascontexti is a list, the assignment is performed
separatelyforeachlistitem),ifitisemptytheglobalcontextisused.
\printdelim[hcontexti]{hnamei}
Printsadelimiterwithnamehnamei,locallyestablishingaoptionalhcontextifirst.
Without the optional hcontexti, \printdelim uses the currently active delimiter
context.
Delimiter contexts are simply a string, the value of the internal macro
\blx@delimcontextwhichcanbesetmanuallybythecommand\delimcontext
\delimcontext{hcontexti}
Set the delimiter context to hcontexti. This setting is not global so that delimiter
contextscanbenestedusingtheusualLaTeXgroupmethod.
129

\DeclareDelimcontextAlias{haliasi}{hnamei}
Thecontext-sensitivedelimitersystemcreatesdelimitercontextsbasedonthename
ofcitationcommands(‘parencite’,‘textcite’etc.) passedto\DeclareCiteCommand.
In certain cases where there are nested definitions of citation commands
where \DeclareCiteCommand calls itself (see the definition of \textcite in
authoryear-icompforexample). Thedelimitercontextisthenusuallyincorrectand
thedelimiterspecificationsdonotwork. Forexample,thedefinitionof\textcite
in fact defines and uses \cbx@textcite and so the context is automatically set to
cbx@textcitewhenprintingthecitation. Delimiterdefinitionsexpectingtoseethe
contexttextcitethereforedonotwork. Thereforethiscommandisprovidedfor
styleauthorswhichaliasesthecontexthaliasitothecontexthnamei. Forexample:
\DeclareDelimcontextAlias{cbx@textcite}{textcite}
This (which is a default setting), makes sure that when inside the \cbx@textcite
citationcommand,thecontextisinfacttextciteasexpected.
\UndeclareDelimcontextAlias{haliasi}
Removesthedelimitercontextaliasdeclaredforhaliasi.
biblatexhasseveraldefaultcontextswhichareestablishedautomaticallyinvarious
places:
none Atbegindocument
bib Insideabibliographybegunwith\printbibliographyorinsidea\usedriver
biblist Insideabibliographylistbegunwith\printbiblist
‘citecommand’ Inside a citation command \citecommand defined with
\DeclareCiteCommand
Forexample,thedefaultsfor\nametitledelimare:
\DeclareDelimFormat{nametitledelim}{\addcomma\space}
\DeclareDelimFormat[bib,biblist]{nametitledelim}{\labelnamepunct}
\DeclareDelimFormat[textcite]{nametitledelim}{\addspace}
Thismeansthat\nametitledelimisdefinedgloballyas‘\addcomma\space’asperthe
standarddelimiterinterface. However,inaddition,thedelimitercanbeprintedusing
\printdelimwhichwouldprintthesameas\nametitledelimapartfrominsidea
\textcite,inwhichitwouldprint\addspacewhichismoresuitableforrunning
text,andinabibliography(list)inwhichittakesthevalueof\labelnamepunctfor
compatibilityreasons. Ifdesired,acontextcanbeforcedwiththeoptionalargument
to\printdelim,so
\printdelim[textcite]{nametitledelim}
wouldprint\addspaceregardlessofthesurroundingcontextofthe\printdelim.
Contextsarejustarbitrarystringsandsoyoucanestablishthematanytime,using
\delimcontext. If \printdelim finds no special value for the delimiter hnamei
130

in the current context, it simply prints \name. This means that style authors can
use\printdelimandusersexpectingtobeabletouse\renewcommandtoredefine
delimiterscandosowithonecaveat—suchadefinitionwon’tchangeanycontext-
specificdelimiterswhicharedefined:
\DeclareDelimFormat{delima}{X}
\DeclareDelimFormat[textcite]{delima}{Y}
\renewcommand*{\delima}{Z}
Here, \delima always prints ‘Z’. \printdelim{delima} in any context other than
‘textcite’alsoprints\delimaandhence‘Z’butina‘textcite’contextprints‘Y’.Seethe
04-delimiters.texexamplefilethatcomeswithbiblatexformoreinformation.
3.12.3 Language-specificCommands
The commands in this section are language specific. When redefining them, you
needtowrapthenewdefinitionina\DeclareBibliographyExtrascommand(inan
.lbxfile)ora\DefineBibliographyExtrascommand(userdocuments),see§3.10
fordetails. Notethatallcommandsstartingwith\mk…takeoneormorearguments.
\bibrangedash The language specific dash to be used for ranges of numbers. Defaults to
\textendash.
\bibrangessep Thelanguagespecificseparatortobeusedbetweenmultipleranges. Defaultstoa
commafollowedbyaspace.
\bibdatesep Thelanguagespecificseparatorusedbetweendatecomponentsinterse/shortdate
formats. Defaultsto\hyphen.
\bibdatendsep Thelanguagespecificseparatorusedbetweendatecomponentsinterse/shortdate
formatswhenthereisnodaypartofthedate(usuallymeaningmonthandyearonly).
Defaultsto\hyphen.
\bibdaterangesep Thelanguagespecificseparatortobeusedfordateranges. Defaultsto\textendash
for all date formats apart from ymd which defaults to a \slash. The date format
optionisoishard-codedto\slashsincethisisastandardscompliantformat.
\mkbibdatelong Takesthenamesofthreefieldasargumentswhichcorrespondtothreedatecompo-
nents(intheorderyear/month/day)andusestheirvaluestoprintthedateinthe
languagespecificlongdateformat.
\mkbibdateshort Similarto\mkbibdatelongbutusingthelanguagespecificshortdateformat.
\mkbibtimezone Modifiesatimezonestringpassedinastheonlyargument. Bydefaultthischanges
‘Z’tothevalueof\bibtimezone.
\bibdateuncertain Thelanguagespecificmarkertobeusedafteruncertaindateswhentheglobaloption
dateuncertainisenabled. Defaultstoaspacefollowedbyaquestionmark.
\bibdateeraprefix The language specific marker which is printed as a prefix to beginning BCE/BC
datesinadaterangewhentheoptiondateeraissetto‘astronomical’. Defaultsto
\textminus,ifdefinedand\textendashotherwise.
131

\bibdateeraendprefix ThelanguagespecificmarkerwhichisprintedasaprefixtoendBCE/BCdates
inadaterangewhentheoptiondateeraissetto‘astronomical’. Defaultstoathin
spacefollowedby\bibdateeraprefixwhen\bibdaterangesepissettoadashand
to\bibdateeraprefixotherwise. Thisisaseparatemacrosothatyoumayaddextra
spacebeforeanegativedatemarkerwhich,forexamplefollowsadashdaterange
markerasthiscanlookalittleodd.
\bibtimesep Thelanguagespecificmarkerwhichseparatestimecomponents. Defaultstoacolon.
\bibutctimezone ThelanguagespecificstringprintedfortheUTCtimezone. Defaultsto‘Z’.
\bibtimezonesep The language specific marker which separates an optional time zone component
fromatime. Emptybydefault.
\bibtzminsep Thelanguagespecificmarkerwhichseparateshourandminutecomponentofoffset
timezones. Defaultstoa\bibtimesep.
\bibdatetimesep The language specific separator printed between date and time compo-
nents when printing time components along with date components (see the
<datetype>dateusetimeoptionin§3.1.2.1). Defaultstoaspacefornon-iso8601-2
outputformats,and’T’foriso8601-2outputformat.
\finalandcomma Printsthecommatobeinsertedbeforethefinal‘and’inalist,ifapplicableinthe
respectivelanguage. Hereisanexample:
Michel Goossens, Frank Mittelbach, and Alexander Samarin
\finalandcomma is the comma before the word ‘and’. See also \multinamedelim,
\finalnamedelim,\textcitedelim,and\revsdnamedelimin§3.12.1.
\finalandsemicolon Printsthesemicolontobeinsertedbeforethefinal‘and’inalistoflists,ifapplicable
intherespectivelanguage. Hereisanexample:
Goossens, Mittelbach, and Samarin; Bertram and Wenworth; and Knuth
\finalandsemicolon is the semicolon before the word ‘and’. See also
\textcitedelimin§3.12.1.
\mkbibordinal{hintegeri}
Thiscommand,whichtakesanintegerasitsargument,printsanordinalnumber.
\mkbibmascord{hintegeri}
Similarto\mkbibordinal,butprintsamasculineordinal,ifapplicableintherespec-
tivelanguage.
\mkbibfemord{hintegeri}
Similarto\mkbibordinal,butprintsafeminineordinal,ifapplicableintherespective
language.
\mkbibneutord{hintegeri}
Similarto\mkbibordinal,butprintsaneuterordinal,ifapplicableintherespective
language.
132

\mkbibordedition{hintegeri}
Similarto\mkbibordinal,butintendedforusewiththeterm‘edition’.
\mkbibordseries{hintegeri}
Similarto\mkbibordinal,butintendedforusewiththeterm‘series’.
3.12.4 LengthsandCounters
Thelengthregistersandcountersinthissectionmaybechangedinthedocument
preamblewith\setlengthand\setcounter,respectively.
\bibhang Thehangingindentationofthebibliography,ifapplicable. Thislengthisinitialized
to\parindentatload-time. If\parindentiszerolengthforsomereason,\bibhang
willdefaultto1em.
\biblabelsep Thehorizontalspacebetweenentriesandtheircorrespondinglabelsinthebibliogra-
phy. Thisonlyappliestobibliographystyleswhichprintlabels,suchasthenumeric
andalphabeticstyles. Thislengthisinitializedtotwicethevalueof\labelsepat
load-time.
\bibitemsep Theverticalspacebetweentheindividualentriesinthebibliography. Thislength
is initialized to \itemsep at load-time. Note that \bibitemsep, \bibnamesep, and
\bibinitsepobeytherulesfor\addvspace,thatis,whenverticalspaceintroduced
byanyofthesecommandsimmediatelyfollowsonfromspaceintroducedbyanother
ofthem,theresultingtotalspaceisequaltothelargestofthem.
\bibnamesep Verticalspacetobeinsertedbetweentwoentriesinthebibliographywheneveran
entry starts with a name which is different from the initial name of the previous
entry. The default value is zero. Setting this length to a positive value greater
than \bibitemsep will group the bibliography by author/editor name. Note that
\bibitemsep,\bibnamesep,and\bibinitsepobeytherulesfor\addvspace,thatis,
whenverticalspaceintroducedbyanyofthesecommandsimmediatelyfollowson
fromspaceintroducedbyanotherofthem,theresultingtotalspaceisequaltothe
largestofthem.
\bibinitsep Verticalspacetobeinsertedbetweentwoentriesinthebibliographywheneveran
entry starts with a letter which is different from the initial letter of the previous
entry. Thedefaultvalueiszero. Settingthislengthtoapositivevaluegreaterthan
\bibitemsep will group the bibliography alphabetically. Note that \bibitemsep,
\bibnamesep,and\bibinitsepobeytherulesfor\addvspace,thatis,whenvertical
space introduced by any of these commands immediately follows on from space
introduced by another of them, the resulting total space is equal to the largest of
them.
\bibparsep The vertical space between paragraphs within an entry in the bibliography. The
defaultvalueiszero.
abbrvpenalty Thiscounter,whichisusedbythelocalisationmodules,holdsthepenaltyusedin
short or abbreviated localisation strings. For example, a linebreak in expressions
such as “et al.” or “ed. by” is unfortunate, but should still be possible to prevent
overfullboxes. Thiscounterisinitializedto\hyphenpenaltyatload-time. Theidea
ismakingTeXtreatthewholeexpressionasifitwereasingle,hyphenatablewordas
farasline-breakingisconcerned. Ifyoudislikesuchlinebreaks,useahighervalue.
133

Ifyoudonotmindthematall,setthiscountertozero. Ifyouwanttosuppressthem
unconditionally,setitto‘infinite’(10000orhigher).25
highnamepenalty Thiscounterholdsapenaltyaffectingline-breakinginnames. Pleasereferto§§3.15.4
and3.12.1forexplanation. Thecounterisinitializedto\hyphenpenaltyatload-time.
Useahighervalueifyoudisliketherespectivelinebreaks. Ifyoudonotmindthem
at all, set this counter to zero. If you prefer the traditional BibTeX behavior (no
linebreaksathighnamepenaltybreakpoints),setitto‘infinite’(10000orhigher).
lownamepenalty Similartohighnamepenalty. Pleasereferto§§3.15.4and3.12.1forexplanation. The
counterisinitializedtohalfthe\hyphenpenaltyatload-time. Useahighervalueif
youdisliketherespectivelinebreaks. Ifyoudonotmindthematall,setthiscounter
tozero.
biburlnumpenalty Ifthiscounterissettoavaluegreaterthanzero,biblatexwillpermitlinebreaks
afternumbersinallstringsformattedwiththe\urlcommandfromtheurlpackage.
Thiswillaffecturlsanddoisinthebibliography. Thebreakpointswillbepenalized
by the value of this counter. If urls and/or dois in the bibliography run into the
margin,trysettingthiscountertoavaluegreaterthanzerobutlessthan10000(you
normallywanttouseahighvaluelike9000). Settingthecountertozerodisables
thisfeature. Thisisthedefaultsetting.
biburlucpenalty Similartobiburlnumpenalty,exceptthatitwilladdabreakpointafteralluppercase
letters.
biburllcpenalty Similartobiburlnumpenalty,exceptthatitwilladdabreakpointafteralllowercase
letters.
biburlbigbreakpenalty Thebiblatexversionofurl’s\UrlBigBreakPenalty. Thedefaultvalueis100.
biburlbreakpenalty Thebiblatexversionofurl’s\UrlBreakPenalty. Thedefaultvalueis200.
\biburlbigskip Thebiblatexversionof\Urlmuskip. Thislengthholdstheadditional(stretchable)
space inserted around breakable characters in the \url command from the url
package. Thedefaultvalueis0mu plus 3mu.
\biburlnumskip The additional space inserted after numbers in strings formatted with the \url
commandfromtheurlpackage. Thiswillaffecturlsanddoisinthebibliography.
Ifurlsand/ordoisinthebibliographyrunintothemargin,itmayhelptosetthis
lengthtoaddsomesmallstretchablespace,forexample0mu plus 1mu. Thedefault
settingis0mu. Thisvalueisonlyusedifbiburlnumpenaltyissettoavaluedifferent
fromzero.
\biburlucskip Similartobiburlnumskip,exceptthatitwilladdspaceafteralluppercaseletters.
25Thedefaultvaluesassignedtoabbrvpenalty,lownamepenalty,andhighnamepenaltyaredeliber-
atelyverylowtopreventoverfullboxes. Thisimpliesthatyouwillhardlynoticeanyeffecton
line-breakingifthetextissetjustified.Ifyousetthesecountersto10000tosuppresstherespective
breakpoints,youwillnoticetheireffectbutyoumayalsobeconfrontedwithoverfullboxes.Keep
inmindthatline-breakinginthebibliographyisoftenmoredifficultthaninthebodytextand
thatyoucannotresorttorephrasingasentence. Insomecasesitmaybepreferabletosetthe
entirebibliography\raggedrighttopreventsuboptimallinebreaks. Inthiscase,eventhefairly
lowdefaultpenaltieswillmakeavisibledifference.
134

\biburllcskip Similartobiburlnumskip,exceptthatitwilladdspaceafteralllowercaseletters.
3.12.5 All-purposeCommands
Thecommandsinthissectionareall-purposetextcommandswhicharegenerally
available,notonlyincitationsandthebibliography.
\bibellipsis Anellipsissymbolwithbrackets: ‘[…]’.
\noligature Disablesligaturesatthispositionandaddssomespace. Usethiscommandtobreak
upstandardligatureslike‘fi’and‘fl’. Itissimilartothe"|shorthandprovidedby
somelanguagemodulesofthebabel/polyglossiapackages.
\hyphenate A conditional hyphen. In contrast to the standard \- command, this one allows
hyphenationintherestoftheword. Itissimilartothe"-shorthandprovidedby
somelanguagemodulesofthebabel/polyglossiapackages.
\hyphen Anexplicit,breakablehyphenintendedforcompoundwords. Incontrasttoaliteral
‘-’,thiscommandallowshyphenationintherestoftheword. Itissimilartothe"=
shorthandprovidedbysomelanguagemodulesofthebabel/polyglossiapackages.
\nbhyphen Anexplicit,non-breakablehyphenintendedforcompoundwords. Incontrasttoa
literal‘-’,thiscommanddoesnotpermitlinebreaksatthehyphenbutstillallows
hyphenationintherestoftheword. Itissimilartothe"~shorthandprovidedby
somelanguagemodulesofthebabel/polyglossiapackages.
\nohyphenation Agenericswitchwhichsuppresseshyphenationlocally. Itsscopeshouldnormally
beconfinedtoagroup. Thecommandusesalanguagewithouthyphenationpatterns
tosuppresshyphenation. TheideawastakenfromPeterWilson’shyphenatpackage.
Notethatthiscommandshouldonlybeusedforsmallportionsoftextandthatits
effectsarenegatedifbabel/polyglossiaisusedtoswitchthelanguagewhileitis
active.
\textnohyphenation{htexti}
Similarto\nohyphenationbutrestrictedtothehtextiargument.
\mknumalph{hintegeri}
Takesanintegerintherange1–702asitsargumentandconvertsittoastringas
follows: 1=a, …, 26=z, 27=aa, …, 702=zz. This is intended for use in formatting
directivesfortheextradate,extranameandextraalphafields.
\mkbibacro{htexti}
Genericcommandwhichtypesetsanacronymusingthesmallcapsvariantofthe
current font, if available, and as-is otherwise. The acronym should be given in
uppercaseletters.
\autocap{hcharacteri}
Automatically converts the hcharacteri to its uppercase form if biblatex’s punc-
tuationtrackerwouldcapitalizealocalisationstringatthecurrentlocation. This
commandisrobust. Itisusefulforconditionalcapitalizationofcertainstringsinan
entry. Notethatthehcharacteriargumentisasinglecharactergiveninlowercase.
Forexample:
135

\autocap{s}pecial issue
willyield‘Specialissue’or‘specialissue’,asappropriate. Ifthestringtobecapitalized
starts with an inflected character given in us-ascii notation, include the accent
commandinthehcharacteriargumentasfollows:
\autocap{\'e}dition sp\'eciale
Thiswillyield‘Éditionspéciale’or‘éditionspéciale’. Ifthestringtobecapitalized
startswithacommandwhichprintsacharacter,suchas\aeor\oe,simplyputthe
commandinthehcharacteriargument:
\autocap{\oe}uvres
Thiswillyield‘Œuvres’or‘œuvres’.
3.13 Language-specificNotes
Thefacilitiesdiscussedinthissectionarespecifictocertainlocalisationmodules.
3.13.1 American
The American localisation module uses \uspunctuation from § 4.7.5 to enable
‘American-style’ punctuation. If this feature is enabled, all trailing commas and
periodsafter\mkbibquotewillbemovedinsidethequotes. Ifyouwanttodisable
thisfeature,use\stdpunctuationasfollows:
\DefineBibliographyExtras{american}{%
\stdpunctuation
}
Bydefault,the‘Americanpunctuation’featureisenabledbytheamericanlocalisation
module only. The above code is only required if you want American localisation
withoutAmericanpunctuation. Sincestandardpunctuationisthepackagedefault,it
wouldberedundantwithanyotherlanguage.
Itishighlyadvisabletoalwaysspecifyamerican,british,australian,etc. rather
thanenglishwhenloadingthebabel/polyglossiapackagestoavoidanypossible
confusion. Olderversionsofthebabelpackageusedtotreatenglishasanaliasfor
british;morerecentonestreatitasanaliasforamerican. Thebiblatexpackage
essentially treats english as an alias for american, except for the above feature
whichisonlyenabledifamericanisrequestedexplicitly.
3.13.2 Bulgarian
LiketheGreeklocalisationmodule,theBulgarianmodulealsorequiresutf-8support.
Itwillnotworkwithanyotherencoding.
136

3.13.3 Greek
The Greek localisation module requires utf-8 support. It will not work with any
otherencoding. Generallyspeaking,thebiblatexpackageiscompatiblewiththe
inputencpackageandwiththeUnicodeenginesLuaLaTeXandXeLaTeX.Theucs
packagewillnotwork. Notethatyoumayneedtoloadadditionalpackageswhichset
upGreekfonts. Asaruleofthumb,asetupwhichworksforregularGreekdocuments
shouldalsoworkwithbiblatex. However,thereisonefundamentallimitation. As
ofthiswriting,biblatexhasnosupportforswitchingscripts. Greektitlesinthe
bibliographyshouldworkfine,butEnglishandothertitlesinthebibliographymay
berenderedinGreekletters. Ifyouneedmulti-scriptbibliographies,usingaUnicode
engineistheonlysensiblechoice.
3.13.4 Hungarian
TheHungarianlocalisationmoduleneedstoredefinecertainfieldformatstoobtain
the grammatically correct word order. This means that these field formats are
overwrittenwhenevertheHungarianlocalisationisactive,nomatterwhetherthey
weredefinedinthepreambleorbyacustomstyle. Sopleasebeawarethatusing
the Hungarian localisation module may cause the bibliography output to deviate
fromtheformatdictatedbytheloadedstyleandpreambledefinitions. Changesto
thisbehaviourneedtobemadeusing\DefineBibliographyExtras. Inparticular
\mkpageprefixisredefinedtooutputthe‘page’or‘pages’stringasasuffixafterthe
pagenumberfollowingHungarianconventions,andallformatsoffieldsinvolving
pages,chaptersandvolumesweremodifiedsothatnumbersareprintedasordinals.
3.13.5 Latvian
TheLatvianlocalisationmodule,liketheHungarianlanguagemodule,needstorede-
finecertainfieldformatstoobtainthegrammaticallycorrectwordorder. Thismeans
thatthesefieldformatsareoverwrittenwhenevertheLatvianlocalisationisactive,no
matterwhethertheyweredefinedinthepreambleorbyacustomstyle. Sopleasebe
awarethatusingtheLatvianlocalisationmodulemaycausethebibliographyoutput
to deviate from the format dictated by the loaded style and preamble definitions.
Changestothisbehaviourneedtobemadeusing\DefineBibliographyExtras. In
particular \mkpageprefix is redefined to output the ‘page’ or ‘pages’ string as a
suffixafterthepagenumberfollowingLatvianconventions,andallformatsoffields
involvingpages,chaptersandvolumesweremodifiedsothatnumbersareprintedas
ordinals.
3.13.6 Lithuanian
TheLithuanianlocalisationmoduleneedsutf-8supportandwillonlyworkwith
thisencoding.
3.13.7 Marathi
TheMarathilocalisationmoduleneedsutf-8supportandwillonlyworkwiththis
encoding,butuserstypesettingsignificantportionsofMarathiwillprobablybeusing
aUnicodeengineanyway.
LiketheHungarianlanguagemodule,theMarathilocalisationneedstoredefine
certain field formats and internal formatting macros to obtain acceptable output.
137

This means that these field formats are overwritten whenever the Marathi local-
isation is active, no matter whether they were defined in the preamble or by a
customstyle. SopleasebeawarethatusingtheMarathilocalisationmodulemay
cause the bibliography output to deviate from the format dictated by the loaded
styleandpreambledefinitions. Changestothisbehaviourneedtobemadeusing
\DefineBibliographyExtras.
Thereissomelimitedsupportfornumericoperationswithnon-us-asciiDevana-
garinumerals. Duetothelimitationsofarithmeticoperationstous-asciinumerals
and backwards compatibility reasons additional work may be needed to support
Devanagarinumeralsinplaceswheretheydonotworkatthemoment.
3.13.8 Romanian
TheRomanianlocalisationmoduleneedsutf-8supportandwillonlyworkwiththis
encoding.
LiketheHungarianandLatvianlocalisationmodules,theRomanianlbxfileapplies
somechangestomacrosthatareusuallynotaffectedbylocalisation. \newunitpunct
is set to produce a comma followed by a space. \intitlepunct only produces a
space.
3.13.9 Russian
LiketheGreekandLithuanianlocalisationmodule,theRussianmodulealsorequires
utf-8support. Itwillnotworkwithanyotherencoding.
3.13.10 Spanish
Handling the word ‘and’ is more difficult in Spanish than in the other languages
supportedbythispackagebecauseitmaybe‘y’or‘e’,dependingontheinitialsound
ofthefollowingword. Therefore,theSpanishlocalisationmoduledoesnotusethe
localisationstring‘and’butaspecialinternal‘smartand’command. Thebehaviorof
thiscommandiscontrolledbythesmartandcounter.
smartand Thiscountercontrolsthebehavioroftheinternal‘smartand’command. Whenset
to1,itprints‘y’or‘e’,dependingonthecontext. Whensetto2,italwaysprints‘y’.
Whensetto3,italwaysprints‘e’. Whensetto0,the‘smartand’featureisdisabled.
This counter is initialized to 1 at load-time and may be changed in the preamble.
NotethatsettingthiscountertoapositivevalueimpliesthattheSpanishlocalisation
moduleignores\finalnamedelimand\finallistdelim.
\forceE Usethiscommandinbibfilesifbiblatexgetsthe‘and’beforeacertainnamewrong.
Asitsnamesuggests,itwillenforce‘e’. Thiscommandmustbeusedinaspecialway
tobecorrectBibTeXdatafileformat. Hereisanexample:
author = {Edward Jones and Eoin Maguire},
author = {Edward Jones and {\forceE{E}}oin Maguire},
Notethattheinitialletteroftherespectivenamecomponentisgivenasanargument
to\forceEandthattheentireconstructiswrappedinanadditionalpairofcurly
braces.
138

\forceY Similarto\forceEbutenforces‘y’.
3.13.11 Turkish
Bydefaultbabel’sTurkishlocalisationmodulemakes‘=’a‘shorthand’,whichbreaks
thehkeyi=hvalueiparserusesbybiblatex. Thisproblemcanberesolvedbytelling
babelnottomake‘=’ashorthand(forexamplebyloadingbabelwiththeoption
shorthands=:!) or by loading a hkeyi=hvaluei package that can deal with active
characters(kvsetkeysandxkeyval)26.
3.14 UsageNotes
Thefollowingsectionsgiveabasicoverviewofthebiblatexpackageanddiscuss
sometypicalusagescenarios.
3.14.1 Overview
UsingthebiblatexpackageisslightlydifferentfromusingtraditionalBibTeXstyles
andrelatedpackages. Beforewegettospecificusagescenarios,wewilltherefore
havealookatthestructureofatypicaldocumentfirst:
\documentclass{...}
\usepackage[...]{biblatex}
\addbibresource{bibfile.bib}
\begin{document}
\cite{...}
...
\printbibliography
\end{document}
With traditional BibTeX, the \bibliography command serves two purposes. It
marksthelocationofthebibliographyanditalsospecifiesthebibfile(s). Thefile
extensionisomitted. Withbiblatex,resourcesarespecifiedinthepreamblewith
\addbibresourceusingthefullnamewith.bibsuffix. Thebibliographyisprinted
using the \printbibliography command which may be used multiple times (see
§3.8fordetails). Thedocumentbodymaycontainanynumberofcitationcommands
(§3.9). Processingthisexamplefilerequiresthatacertainprocedurebefollowed.
Suppose our example file is called example.tex and our bibliographic data is in
bibfile.bib. Theprocedure,then,isasfollows:
1. Runlatexonexample.tex. Ifthefilecontainsanycitations, biblatexwill
requesttherespectivedatafrombiberbywritingcommandstotheauxiliary
fileexample.bcf.
2. Runbiberonexample.bcf. biberwillretrievethedatafrombibfile.biband
writeittotheauxiliaryfileexample.bblinaformatwhichcanbeprocessed
bybiblatex.
3. Run latex on example.tex. biblatex will read the data from example.bbl
andprintallcitationsaswellasthebibliography.
26https://tex.stackexchange.com/a/160428/35864
139

3.14.2 AuxiliaryFiles
The biblatex package uses one auxiliary bcf file only. Even if there are citation
commandsinafileincludedvia\include,youonlyneedtorunbiberonthemain
bcffile. Allinformationbiberneedsisinthebcffile,includinginformationabout
allrefsectionsifusingmultiplerefsectionenvironments(see§3.14.3).
3.14.3 MultipleBibliographies
In a collection of articles by different authors, such as a conference proceedings
volume for example, it is very common to have one bibliography for each article
ratherthanaglobalonefortheentirebook. Intheexamplebelow,eacharticlewould
bepresentedasaseparate\chapterwithitsownbibliography.
\documentclass{...}
\usepackage{biblatex}
\addbibresource{...}
\begin{document}
\chapter{...}
\begin{refsection}
...
\printbibliography[heading=subbibliography]
\end{refsection}
\chapter{...}
\begin{refsection}
...
\printbibliography[heading=subbibliography]
\end{refsection}
\end{document}
If\printbibliographyisusedinsidearefsectionenvironment,itautomatically
restrictsthescopeofthelistofreferencestotheenclosingrefsectionenvironment.
Foracumulativebibliographywhichissubdividedbychapterbutprintedattheend
of the book, use the section option of \printbibliography to select a reference
section,asshowninthenextexample.
\documentclass{...}
\usepackage{biblatex}
\defbibheading{subbibliography}{%
\section*{References for Chapter \ref{refsection:\therefsection}}}
\addbibresource{...}
\begin{document}
\chapter{...}
\begin{refsection}
...
\end{refsection}
\chapter{...}
\begin{refsection}
...
\end{refsection}
\printbibheading
\printbibliography[section=1,heading=subbibliography]
140

\printbibliography[section=2,heading=subbibliography]
\end{document}
Notethedefinitionofthebibliographyheadingintheaboveexample. Thisisthe
definition taking care of the subheadings in the bibliography. The main heading
is generated with a plain \chapter command in this case. The biblatex package
automaticallysetsalabelatthebeginningofeveryrefsectionenvironment,using
the standard \label command. The identifier used is the string refsection: fol-
lowedbythenumberoftherespectiverefsectionenvironment. Thenumberofthe
currentsectionisaccessibleviatherefsectioncounter. Whenusingthesection
optionof\printbibliography,thiscounterisalsosetlocally. Thismeansthatyou
mayusethecounterinheadingdefinitionstoprintsubheadingslike“Referencesfor
Chapter3”,asshownabove. Youcouldalsousethetitleoftherespectivechapteras
asubheadingbyloadingthenamerefpackageandusing\namerefinsteadof\ref:
\usepackage{nameref}
\defbibheading{subbibliography}{%
\section*{\nameref{refsection:\therefsection}}}
Sincegivingone\printbibliographycommandforeachpartofasubdividedbib-
liographyistedious,biblatexprovidesashorthand. The\bibbysectioncommand
automatically loops over all reference sections. This is equivalent to giving one
\printbibliographycommandforeverysectionbuthastheadditionalbenefitof
automaticallyskippingsectionswithoutreferences. Intheexampleabove,thebiblio-
graphywouldthenbegeneratedasfollows:
\printbibheading
\bibbysection[heading=subbibliography]
Whenusingaformatwithonecumulativebibliographysubdividedbychapter(or
anyotherdocumentdivision)itmaybemoreappropriatetouserefsegmentrather
thanrefsectionenvironments. Thedifferenceisthattherefsectionenvironment
generates labels local to the environment while refsegment does not affect the
generation of labels, hence they will be unique across the entire document. The
nextexamplecouldalsobegivenin§3.14.4because,visually,itcreatesoneglobal
bibliographysubdividedintomultiplesegments.
\documentclass{...}
\usepackage{biblatex}
\defbibheading{subbibliography}{%
\section*{References for Chapter \ref{refsegment:
,→ \therefsection\therefsegment}}}
\addbibresource{...}
\begin{document}
\chapter{...}
\begin{refsegment}
...
\end{refsegment}
\chapter{...}
\begin{refsegment}
141

...
\end{refsegment}
\printbibheading
\printbibliography[segment=1,heading=subbibliography]
\printbibliography[segment=2,heading=subbibliography]
\end{document}
Theuseof refsegmentissimilartorefsectionandthereisalsoacorresponding
segmentoptionfor\printbibliography. Thebiblatexpackageautomaticallysetsa
labelatthebeginningofeveryrefsegmentenvironmentusingthestringrefsegment:
followedbythenumberoftherespectiverefsegmentenvironmentasanidentifier.
Thereisamatchingrefsegmentcounterwhichmaybeusedinheadingdefinitions,
as shown above. As with reference sections, there is also a shorthand command
whichautomaticallyloopsoverallreferencesegments:
\printbibheading
\bibbysegment[heading=subbibliography]
Thisisequivalenttogivingone\printbibliographycommandforeverysegment
inthecurrentrefsection.
3.14.4 SubdividedBibliographies
It is very common to subdivide a bibliography by certain criteria. For example,
you may want to list printed and online resources separately or divide a biblio-
graphy into primary and secondary sources. The former case is straightforward
becauseyoucanusetheentrytypeasacriterionforthetypeandnottypefiltersof
\printbibliography. Thenextexamplealsodemonstrateshowtogeneratematching
subheadingsforthetwopartsofthebibliography.
\documentclass{...}
\usepackage{biblatex}
\addbibresource{...}
\begin{document}
...
\printbibheading
\printbibliography[nottype=online,heading=subbibliography,
title={Printed Sources}]
\printbibliography[type=online,heading=subbibliography,
title={Online Sources}]
\end{document}
Youmayalsousemorethantwosubdivisions:
\printbibliography[type=article,...]
\printbibliography[type=book,...]
\printbibliography[nottype=article,nottype=book,...]
Itisevenpossibletogiveachainofdifferenttypesoffilters:
142

\printbibliography[section=2,type=book,keyword=abc,notkeyword=xyz]
Thiswouldprint allworkscited inreferencesection 2whose entrytypeis @book
and whose keywords field includes the keyword ‘abc’ but not ‘xyz’. When using
bibliography filters inconjunction with a numeric style, see § 3.15.5. If youneed
complexfilterswithconditionalexpressions,usethefilteroptioninconjunction
withacustomfilterdefinedwith\defbibfilter. See§3.8.9fordetailsoncustom
filters.
\documentclass{...}
\usepackage{biblatex}
\addbibresource{...}
\begin{document}
...
\printbibheading
\printbibliography[keyword=primary,heading=subbibliography,%
title={Primary Sources}]
\printbibliography[keyword=secondary,heading=subbibliography,%
title={Secondary Sources}]
\end{document}
Dividing a bibliography into primary and secondary sources is possible with a
keywordfilter,asshownintheaboveexample. Inthiscase,withonlytwosubdivi-
sions,itwouldbesufficienttouseonekeywordasfiltercriterion:
\printbibliography[keyword=primary,...]
\printbibliography[notkeyword=primary,...]
Sincebiblatexhasnowayofknowingifaniteminthebibliographyisconsidered
tobeprimaryorsecondaryliterature,weneedtosupplythebibliographyfilterwith
the required data by adding a keywords field to each entry in the bib file. These
keywords may then be used as targets for the keyword and notkeyword filters, as
shownabove. Itmaybeagoodideatoaddsuchkeywordsrightawaywhilebuilding
abibfile.
@Book{key,
keywords = {primary,some,other,keywords},
...
Analternativewayofsubdividingthelistofreferencesarebibliographycategories.
Theydifferfromthekeywords-basedapproachshownintheexampleaboveinthat
theyworkonthedocumentlevelanddonotrequireanychangestothebibfile.
\documentclass{...}
\usepackage{biblatex}
\DeclareBibliographyCategory{primary}
\DeclareBibliographyCategory{secondary}
\addtocategory{primary}{key1,key3,key6}
\addtocategory{secondary}{key2,key4,key5}
143

\addbibresource{...}
\begin{document}
...
\printbibheading
\printbibliography[category=primary,heading=subbibliography,%
title={Primary Sources}]
\printbibliography[category=secondary,heading=subbibliography,%
title={Secondary Sources}]
\end{document}
Inthiscaseitwouldalsobesufficienttouseonecategoryonly:
\printbibliography[category=primary,...]
\printbibliography[notcategory=primary,...]
It is still a good idea to declare all categories used in the bibliography explicitly
because there is a \bibbycategory command which automatically loops over all
categories. Thisisequivalenttogivingone\printbibliographycommandforevery
category,intheorderinwhichtheyweredeclared.
\documentclass{...}
\usepackage{biblatex}
\DeclareBibliographyCategory{primary}
\DeclareBibliographyCategory{secondary}
\addtocategory{primary}{key1,key3,key6}
\addtocategory{secondary}{key2,key4,key5}
\defbibheading{primary}{\section*{Primary Sources}}
\defbibheading{secondary}{\section*{Secondary Sources}}
\addbibresource{...}
\begin{document}
...
\printbibheading
\bibbycategory
\end{document}
Thehandlingoftheheadingsisdifferentfrom\bibbysectionand\bibbysegment
in this case. \bibbycategory uses the name of the current category as a heading
name. Thisisequivalenttopassingheading=hcategoryito\printbibliographyand
impliesthatyouneedtoprovideamatchingheadingforeverycategory.
3.14.5 EntrySets
An entry set is a group of entries which are cited as a single reference and listed
asasingleiteminthebibliography. Theindividualentriesinthesetareseparated
by\entrysetpunct(§4.10.1). Thebiblatexpackagesupportstwotypesofentry
sets. Staticentrysetsaredefinedinthebibfilelikeanyotherentry. Dynamicentry
setsaredefinedwith\defbibentryset(§3.8.11)onaper-document/per-refsection
basisinthedocumentpreambleorthedocumentbody. Thissectiondealswiththe
definitionofentrysets;styleauthorsshouldalsosee§4.11.1forfurtherinformation.
Pleasenotethatentrysetsonlymakesenseforstyleswhichrefertoentriesbylabels
suchastheprovidednumericandalphabeticstyles. Styleswhichrefertoentries
144

via names, titles etc. (authoryear, authortitle, verbose etc.) rarely employ sets
anddonotsupportthembydefaultwhentheyareciteddirectly. Customstylesmay
ofcoursechoosetoimplementsomemannerofsetcitationsupportinanymanner
theychoose.
| 3.14.5.1 Staticentrysets |     |     |     |     |
| ------------------------ | --- | --- | --- | --- |
Staticentrysetsaredefinedinthebibfilelikeanyotherentry. Defininganentry
set is as simple as adding an entry of type @set. The entry has an entryset field
definingthemembersofthesetasaseparatedlistofentrykeys:
@Set{set1,
| entryset | = {key1,key2,key3}, |     |     |     |
| -------- | ------------------- | --- | --- | --- |
}
Entriesmaybepartofasetinonedocument/refsectionandstand-alonereferencesin
anotherone,dependingonthepresenceofthe@setentry. Ifthe@setentryiscited,
thesetmembersaregroupedautomatically. Ifnot,theywillworklikeanyregular
entry. NotethatwithBibTeXasthebackend,theremustalsobeanentrysetfieldin
thesetmemberswhichpointtothesetparent. Withbiber,thisisnotnecessary.
| 3.14.5.2 Dynamicentrysets |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
Dynamicentrysetsaresetupandworkmuchlikestaticones. Themaindifferenceis
thattheyaredefinedinthedocumentpreambleorontheflyinthedocumentbody
usingthe\defbibentrysetcommandfrom§3.8.11:
\defbibentryset{set1}{key1,key2,key3}
| Dynamic entry | sets in | the document | body are local | to the enclosing |
| ------------- | ------- | ------------ | -------------- | ---------------- |
refsection
environment, if any. Otherwise, they are assigned to reference section 0. Those
definedinthepreambleareassignedtoreferencesection0.
3.14.6 DataContainers
The@xdataentrytypeservesasadatacontainerholdingoneormorefields. Data
in@xdataentriesmaybereferencedandusedbyotherentries. @xdataentriesmay
notbecitedoraddedtothebibliography,theyonlyserveasadatasourceforother
entries(includingother@xdataentries). Thisdatainheritancemechanismisuseful
forfixedfieldcombinationssuchaspublisher/locationandforotherfrequently
useddata:
@XData{hup,
| publisher | = {Harvard    | University | Press}, |     |
| --------- | ------------- | ---------- | ------- | --- |
| location  | = {Cambridge, | Mass.},    |         |     |
}
@Book{...,
| author | = {...}, |     |     |     |
| ------ | -------- | --- | --- | --- |
| title  | = {...}, |     |     |     |
| date   | = {...}, |     |     |     |
| xdata  | = {hup}, |     |     |     |
}
145

Usingaseparatedlistofkeysinitsxdatafield,anentrymayinheritdatafromseveral
@xdataentries. Cascading@xdataentriesaresupportedaswell,i.e.,an@xdataentry
mayreferenceoneormoreother@xdataentries:
@XData{macmillan:name,
| publisher | = {Macmillan}, |     |     |     |
| --------- | -------------- | --- | --- | --- |
}
@XData{macmillan:place,
| location | = {New York | and London}, |     |     |
| -------- | ----------- | ------------ | --- | --- |
}
@XData{macmillan,
| xdata | = {macmillan:name,macmillan:place}, |     |     |     |
| ----- | ----------------------------------- | --- | --- | --- |
}
@Book{...,
| author | = {...},       |     |     |     |
| ------ | -------------- | --- | --- | --- |
| title  | = {...},       |     |     |     |
| date   | = {...},       |     |     |     |
| xdata  | = {macmillan}, |     |     |     |
}
Moregranular@xdataentrydatamaybereferenced. Itisnotnecessarytoreference
| onlyentirefields. | Forexample: |     |     |     |
| ----------------- | ----------- | --- | --- | --- |
@XData{someauthors,
| author | = {John | Smith and Brian | Brown} |     |
| ------ | ------- | --------------- | ------ | --- |
}
@XData{somelocations,
| location | = {Location1 | and Location2} |     |     |
| -------- | ------------ | -------------- | --- | --- |
}
@XData{somenotes,
| note = | {A note} |     |     |     |
| ------ | -------- | --- | --- | --- |
}
@Book{...,
| author   | = {Alan                           | Drudge and xdata=someauthors-author-2}, |     |                 |
| -------- | --------------------------------- | --------------------------------------- | --- | --------------- |
| editor   | = {xdata=someauthors-author       |                                         | and | Ann Editor},    |
| location | = {xdata=somelocations-location-1 |                                         |     | and Location3}, |
| note     | = {xdata=somenotes-note}          |                                         |     |                 |
}
Theformatofgranular@xdatareferencesareasfollows:
xdata=<key>-<field>-<index>
| 1 2 3 | 4 5 | 6 7 |     |     |
| ----- | --- | --- | --- | --- |
1. Thevalueofthebiberoption--xdatamarker(bydefault’xdata’)
2. Thevalueofthebiberoption--xnamesep(bydefault’=’)
3. Avalidentrykeyofan@xdataentry
4. Thevalueofthebiberoption--xdatasep(bydefault’-’)
5. Avalidentryfieldinthesource@xdataentry
6. (Optional)Thevalueofthebiberoption--xdatasep(bydefault’-’)
146

7. (Optional)Avalid1-basedindexintoalist/namefieldinthesource@xdata
entry
Thereare--output-*variantsoftheaboveoptionsforbibertoolmodeoutputso
that these separators and markers can be programmatically changed. Taking the
exampleabove,this@bookwouldresolveto:
@Book{...,
author = {Alan Drudge and Brian Brown},
editor = {John Smith and Brian Brown and Ann Editor},
location = {Location1 and Location3},
note = {A note}
}
Thingstonotewithgranular@xdatareferences:
• Referencesmustbemadeonlyto@xdatafields. Awarningwillbegenerated
otherwiseandthereferencewillnotberesolved
• References must be made only to @xdata fields of the same type (list/name
anddatatype)asthereferencingfield. Awarningwillbegeneratedotherwise
andthereferencewillnotberesolved
• Referencestofieldsofdatatype’date’arenotpossible. Referencestolegacy
yearandmonthfieldsarepossible
• Referencestomissingentries,fieldsorlist/nameindiceswillgenerateawarn-
ingandthereferencewillnotberesolved
• If an index is missing for a reference to a list/name field, the entire xdata
name/listfieldwillbesplicedintothereferencingfieldatthedesiredposition.
Seealso§§2.1.1and2.2.3.
3.14.7 ElectronicPublishingInformation
Thebiblatexpackageprovidesthreefieldsforelectronicpublishinginformation:
eprint,eprinttype,andeprintclass. Theeprintfieldisaverbatimfieldsimilarto
doiwhichholdstheidentifieroftheitem. Theeprinttypefieldholdstheresource
name, i.e., the name of the site or electronic archive. The optional eprintclass
fieldisintendedforadditionalinformationspecifictotheresourceindicatedbythe
eprinttypefield. Thiscouldbeasection,apath,classificationinformation,etc. If
theeprinttypefieldisavailable,thestandardstyleswilluseitasaliterallabel. Inthe
followingexample,theywouldprint“Resource: identifier”ratherthanthegeneric
“eprint: identifier”:
eprint = {identifier},
eprinttype = {Resource},
Thestandardstylesfeaturededicatedsupportforafewonlinearchives. ForarXivref-
erences,puttheidentifierintheeprintfieldandthestringarxivintheeprinttype
field:
147

eprint = {math/0307200v3},
eprinttype = {arxiv},
Forpaperswhichusethenewidentifierscheme(April2007andlater)addtheprimary
classificationintheeprintclassfield:
eprint = {1008.2849v1},
eprinttype = {arxiv},
eprintclass = {cs.DS},
TherearetwoaliaseswhicheasetheintegrationofarXiventries. archiveprefix
is treated as an alias for eprinttype; primaryclass is an alias for eprintclass.
If hyperlinks are enabled, the eprint identifier will be transformed into a link to
arxiv.org. Seethepackageoptionarxivin§3.1.2.1forfurtherdetails.
For jstor references, put the stable jstor number in the eprint field and the
stringjstorintheeprinttypefield:
eprint = {number},
eprinttype = {jstor},
Whenusingjstor’sexportfeaturetoexportcitationsinBibTeXformat,jstoruses
theurlfieldbydefault(wherethehnumberiisauniqueandstableidentifier):
url = {http://www.jstor.org/stable/number},
Whilethiswillworkasexpected,fullurlstendtoclutterthebibliography. With
theeprintfields,thestandardstyleswillusethemorereadable“jstor: hnumberi”
formatwhichalsosupportshyperlinks. Thehnumberibecomesaclickablelinkif
hyperrefsupportisenabled.
ForPubMedreferences,putthestablePubMedidentifierintheeprintfieldand
thestringpubmedintheeprinttypefield. Thismeansthat:
url = {http://www.ncbi.nlm.nih.gov/pubmed/pmid},
becomes:
eprint = {pmid},
eprinttype = {pubmed},
and the standard styles will print “pmid: hpmidi” instead of the lengthy url. If
hyperrefsupportisenabled,thehpmidiwillbeaclickablelinktoPubMed.
Forhandles(hdls), putthehandleintheeprintfieldandthestringhdlinthe
eprinttypefield:
eprint = {handle},
eprinttype = {hdl},
For Google Books references, put Google’s identifier in the eprint field and the
stringgooglebooksintheeprinttypefield. Thismeansthat,forexample:
url = {http://books.google.com/books?id=XXu4AkRVBBoC},
148

wouldbecome:
eprint = {XXu4AkRVBBoC},
eprinttype = {googlebooks},
andthestandardstyleswouldprint“GoogleBooks: XXu4AkRVBBoC”insteadofthefull
url. Ifhyperrefsupportisenabled,theidentifierwillbeaclickablelinktoGoogle
Books.27
Notethateprintisaverbatimfield. Alwaysgivetheidentifierinitsunmodified
form. Forexample,thereisnoneedtoreplace_with\_. Alsosee§4.11.2onhowto
adddedicatedsupportforothereprintresources.
3.14.8 ExternalAbstractsandAnnotations
Styleswhichprintthefieldsabstractand/orannotationmaysupportanalternative
way of adding abstracts or annotations to the bibliography. Instead of including
thetextinthebibfile,itmayalsobestoredinanexternalLaTeXfile. Forexample,
insteadofsaying
@Article{key1,
...
abstract = {This is an abstract of entry `key1'.}
}
in the bib file, you may create a file named bibabstract-key1.tex and put the
abstractinthisfile:
This is an abstract of entry `key1'.
\endinput
The name of the external file must be the entry key prefixed with bibabstract-
or bibannotation-, respectively. You can change these prefixes by redefining
\bibabstractprefix and \bibannotationprefix. Note that this feature needs to
beenabledexplicitlybysettingthepackageoptionloadfilesfrom§3.1.2.1. The
optionisdisabledbydefaultforperformancereasons. Alsonotethatanyabstract
andannotationfieldsinthebibfiletakeprecedenceovertheexternalfiles. Using
externalfilesisstronglyrecommendedifyouhavelongabstractsoralotofanno-
tationssincethismayincreasememoryrequirementssignificantly. Itisalsomore
convenienttoeditthetextinadedicatedLaTeXfile. Styleauthorsshouldsee§4.11.3
forfurtherinformation.
3.15 HintsandCaveats
Thissectionprovidesadditionalusagehintsandaddressessomecommonproblems
andpotentialmisconceptions.
27NotethattheGoogleBooksidseemstobeabitofan‘internal’value.Asofthiswriting,theredoes
notseemtobeanywaytosearchforanidonGoogleBooks.Youmayprefertousetheurlinthis
case.
149

3.15.1 UsagewithKOMA-ScriptClasses
Whenusedinconjunctionwitharecentversion28 oneofthescrbook,scrreprt,or
scrartclclasses,biblatexpassescontroloverthe(default)headingsbibliography
andbiblistfrom§3.8.7totheclass. Hence,bibliography-heading-relatedclassop-
tionscanbeusedasusual. Youcanoverridethedefaultheadingsbyusingtheheading
optionof\printbibliography,\printbibheadingand\printbiblist. See§§3.8.2,
3.8.3,3.8.7fordetails.
biblatexalsotriestodetectbibliography-relatedclassoptionsandsettingsitself.29
Thiswasrequiredtobeabletoadaptthebibliographyheadingstotheclasssettings
inolderversionsofkoma-Script. Ifoneoftheaboveclassesisdetected,biblatex
willprovidethefollowingadditionaltestswhichmaybeusefulincustomheading
definitions. Since these tests rely on the error-prone external detection of koma-
Scriptsettingsandarenolongerusedwithnewerkoma-Scriptversions,thesetests
aredeprecatedandshouldnolongerbeused.
\ifkomabibtotoc{htruei}{hfalsei}
Deprecated
Expandstohtrueiiftheclasswouldaddthebibliographytothetableofcontents,
andtohfalseiotherwise. Thistestisdeprecated.
\ifkomabibtotocnumbered{htruei}{hfalsei}
Deprecated
Expands to htruei if the class would add the bibliography to the table of con-
tents as a numbered section, and to hfalsei otherwise. If this test yields htruei,
\ifkomabibtotoc will always yield htruei as well, but not vice versa. This test is
deprecated.
3.15.2 UsagewiththeMemoirClass
Whenusingbiblatexwiththememoirclass,mostclassfacilitiesforadaptingthe
bibliography have no effect. Use the corresponding facilities of this package in-
stead (§§ 3.8.2, 3.8.7, 3.8.8). Instead of redefining memoir’s \bibsection, use the
heading option of \printbibliography and \defbibheading (§§ 3.8.2 and 3.8.7).
Insteadof\prebibhookand\postbibhook,usetheprenoteandpostnoteoptions
of\printbibliographyand\defbibnote(§§3.8.2and3.8.8). Alldefaultheadings
areadapted at load-time such thattheyblend wellwith thedefault layoutof this
class. Thedefaultheadingsbibliographyandbiblist(§3.8.7)arealsoresponsive
tomemoir’s\bibintocand\nobibintocswitches. Thelengthregister\bibitemsep
is used by biblatex in a way similar to memoir (§ 3.12.4). This section also intro-
ducessomeadditionallengthregisterswhichcorrespondtomemoir’s\biblistextra.
Lastly,\setbiblabeldoesnotmaptoasinglefacilityofthebiblatexpackagesince
thestyleofalllabelsinthebibliographyiscontrolledbythebibliographystyle. See
§4.2.2intheauthorsectionofthismanualfordetails. Ifthememoirclassisdetected,
biblatex will also provide the following additional test which may be useful in
customheadingdefinitions:
28Atleastkoma-Script3.25(2018/03/30).
29Thisappliestothetraditionalsyntaxoftheseoptions(bibtotocandbibtotocnumbered)aswell
astothehkeyi=hvalueisyntaxintroducedinkoma-Script3.x,i.e.,tobibliography=nottotoc,
bibliography=totoc,andbibliography=totocnumbered.Theglobaltoc=bibliographyandtoc=
bibliographynumberedoptionsaswellastheiraliasesaredetectedaswell.Inanycase,theoptions
mustbesetgloballyintheoptionalargumentto\documentclass.
150

\ifmemoirbibintoc{htruei}{hfalsei}
Expands to htruei or hfalsei, depending on memoir’s \bibintoc and \nobibintoc
switches. ThisisaLaTeXfrontendtomemoir’s\ifnobibintoctest. Notethatthe
logicofthetestisreversed.
3.15.3 PageNumbersinCitations
Ifthehpostnoteiargumenttoacitationcommandisapagenumberorpagerange,
biblatexwillautomaticallyprefixitwith‘p.’ or‘pp.’ bydefault. Thisworksreliably
intypicalcases,butsometimesmanualinterventionmayberequired. Inthiscase,it
isimportanttounderstandhowthisargumentishandledindetail. First,biblatex
checksifthepostnoteisanArabicorRomannumeral(caseinsensitive). Ifthistest
succeeds, thepostnoteisconsideredasasinglepageorothernumberwhichwill
beprefixedwith‘p.’ orsomeotherstringwhichdependsonthepaginationfield
(see § 2.3.12). If it fails, a second test is performed to find out if the postnote is a
rangeoralistofArabicorRomannumerals. Ifthistestsucceeds,thepostnotewill
beprefixedwith‘pp.’ orsomeotherstringinthepluralform. Ifitfailsaswell,the
postnoteisprintedasis. Notethatbothtestsexpandthehpostnotei. Allcommands
used in this argument must therefore be robust or prefixed with \protect. Here
areafewexamplesofhpostnoteiargumentswhichwillbecorrectlyrecognizedasa
singlenumber,arangeofnumbers,oralistofnumbers,respectively:
\cite[25]{key}
\cite[vii]{key}
\cite[XIV]{key}
\cite[34--38]{key}
\cite[iv--x]{key}
\cite[185/86]{key}
\cite[XI \& XV]{key}
\cite[3, 5, 7]{key}
\cite[vii--x; 5, 7]{key}
Insomeothercases,however,thetestsmaygetitwrongandyouneedtoresortto
theauxiliarycommands\pnfmt,\pno,\ppno,and\noppfrom§3.9.8. Forexample,
supposeaworkiscitedbyaspecialpaginationschemeconsistingofnumbersand
letters. Inthisscheme,thestring‘27a’wouldmean‘page27,parta’. Sincethisstring
doesnotlooklikeanumberorarangetobiblatex,youneedtoforcetheprefixfor
asinglenumbermanually:
\cite[\pno~27a]{key}
There is also a \ppno command which forces a range prefix as well as a \nopp
commandwhichsuppressesallprefixes:
\cite[\ppno~27a--28c]{key}
\cite[\nopp 25]{key}
Thesecommandsmaybeusedanywhereinthehpostnoteiargument. Theymayalso
beusedmultipletimes. Forexample,whencitingbyvolumeandpagenumber,you
maywanttosuppresstheprefixatthebeginningofthepostnoteandadditinthe
middleofthestring:
151

\cite[VII, \pno~5]{key}
\cite[VII, \pno~3, \ppno~40--45]{key}
\cite[see][\ppno~37--46, in particular \pno~40]{key}
The command \pnfmt can be used for hpostnoteis consisting of a page range and
some additional text. \pnfmt prints its argument in the format specified for the
postnoteandcanbeusedtoformatthepagerangeautomaticallywithouttheneed
for\pnoand\ppno.
\cite[\pnfmt{37-46}, in particular \pnfmt{40}]{key}
Therearealsotwoauxiliarycommandforsuffixeslike‘thefollowingpage(s)’. Instead
ofinsertingsuchsuffixesliterally(whichwouldrequire\ppnotoforceaprefix):
\cite[\ppno~27~sq.]{key}
\cite[\ppno~55~sqq.]{key}
usetheauxiliarycommands\psqand\psqq. Notethatthereisnospacebetween
thenumberandthecommand. Thisspacewillbeinsertedautomaticallyandmaybe
modifiedbyredefiningthemacro\sqspace.
\cite[27\psq]{key}
\cite[55\psqq]{key}
Sincethepostnoteisprintedwithoutanyprefixifitincludesanycharacterwhichis
notanArabicorRomannumeral,youmayalsotypetheprefixmanually—though
thisisdiscouraged:
\cite[p.~5]{key}
Itispossibletosuppresstheprefixonaper-entrybasisbysettingthepagination
fieldofanentryto‘none’,see§2.3.12fordetails. Ifyoudonotwantanyprefixesat
allorprefertotypethemmanually,youcanalsodisabletheentiremechanismin
thedocumentpreambleortheconfigurationfileasfollows:
\DeclareFieldFormat{postnote}{#1}
The hpostnotei argument is handled as a field and the formatting of this field is
controlledbyafieldformattingdirectivewhichmaybefreelyredefined. Theabove
definitionwillsimplyprintthepostnoteasis. See§§4.3.2and4.4.2intheauthor
guideforfurtherdetails.
3.15.4 NamePartsandNameSpacing
The biblatex package gives users and style authors very fine-grained control of
namespacingandtheline-breakingbehaviorofnames. Thecommandsdiscussedin
thefollowingaredocumentedin§§3.12.1and4.10.1. Thissectionismeanttogive
anoverviewofhowtheyareputtogether. Anoteonterminology: anamepart is
abasicpartofthename,forexamplethegivenorthefamilyname. Eachpartofa
152

namemaybeasinglenameoritmaybecomposedofmultiplenames. Forexample,
thenamepart‘givenname’maybecomposedofagivenandamiddlename. The
latterarereferredtoasnameelements inthissection. Let’sconsiderasimplename
| first: “JohnEdwardDoe”. | Thisnameiscomposedofthefollowingparts: |     |     |     |
| ----------------------- | -------------------------------------- | --- | --- | --- |
| Given JohnEdward        |                                        |     |     |     |
| Prefix —                |                                        |     |     |     |
| Family Doe              |                                        |     |     |     |
| Suffix —                |                                        |     |     |     |
Thespacing,punctuationandline-breakingbehaviorofnamesiscontrolledbysix
macros:
a=\bibnamedelima Insertedbythebackendafterthefirstelementofeveryname
partifthatelementislessthanthreecharacterslongand
beforethelastelementofeverynamepart.
b=\bibnamedelimb Insertedbythebackendbetweenallelementsofanamepart
where\bibnamedelimadoesnotapply.
c=\bibnamedelimc Insertedbyaformattingdirectivebetweenthenameprefix
|     | andthefamilynameifuseprefix=true. |     |     | If  |
| --- | --------------------------------- | --- | --- | --- |
useprefix=false,\bibnamedelimdisusedinstead.
d=\bibnamedelimd Insertedbyaformattingdirectivebetweennamepartswhere
\bibnamedelimcdoesnotapply.
| i=\bibnamedelimi | Replaces\bibnamedelima/bafterinitials |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | --- |
p=\revsdnamepunct Insertedbyaformattingdirectiveafterthefamilyname
whenthenamepartsarereversed.
Thisishowthedelimitersareemployed:
| John Edward | Doe    |     |     |     |
| ----------- | ------ | --- | --- | --- |
| a           | d      |     |     |     |
| Doe, John   | Edward |     |     |     |
| pd          | a      |     |     |     |
Initialsinthebibfilegetaspecialdelimiter:
| J. Edward | Doe |     |     |     |
| --------- | --- | --- | --- | --- |
| i         | d   |     |     |     |
Let’sconsideramorecomplexname: “Charles-JeanÉtienneGustaveNicolasdeLa
| ValléePoussin”.                         | Thisnameiscomposedofthefollowingparts: |     |     |     |
| --------------------------------------- | -------------------------------------- | --- | --- | --- |
| Given Charles-JeanÉtienneGustaveNicolas |                                        |     |     |     |
| Prefix de                               |                                        |     |     |     |
| Family LaValléePoussin                  |                                        |     |     |     |
| Suffix —                                |                                        |     |     |     |
Thedelimiters:
| Charles-Jean | Étienne Gustave | Nicolas | de La Vallée | Poussin |
| ------------ | --------------- | ------- | ------------ | ------- |
|              | b b             | a       | d c a        | a       |
Notethat\bibnamedelima/b/iareinsertedbythebackend. Thebackendprocesses
thenamepartsandtakescareofthedelimitersbetweentheelementsthatmakeup
a name part, processing each part individually. In contrast to that, the delimiters
between the parts of the complete name (\bibnamedelimc/d) are added by name
formatting directives at a later point in the processing chain. The spacing and
punctuation of initials is also handled by the backend and may be customized by
redefiningthefollowingthreemacros:
153

a=\bibinitperiod Insertedbythebackendafterinitials.
b=\bibinitdelim Insertedbythebackendbetweenmultipleinitials.
c=\bibinithyphendelim Insertedbythebackendbetweentheinitialsof
hyphenatednameparts,replacing\bibinitperiodand
\bibinitdelim.
Thisishowtheyareemployed:
J. E. Doe
ab a
K.-H. Mustermann
c a
3.15.5 SplitBibliographiesandCitationLabels
Thecitationlabelsgeneratedbythispackageareassignedtothefulllistofreferences
beforeitissplitupbyanybibliographyfilters. Theyareguaranteedtobeunique
acrosstheentiredocument(orarefsectionenvironment), nomatterhowmany
bibliographyfiltersyouareusing. Whenusinganumericcitationscheme,however,
thiswillmostlikelyleadtodiscontinuousnumberinginsplitbibliographies. Use
thedefernumberspackageoptiontoavoidthisproblem. Ifthisoptionisenabled,
numericlabelsareassignedthefirsttimeanentryisprintedinanybibliography.
Compare the output of the following example with defernumbers=true and
defernumbers=false.
\documentclass{article}
\usepackage[defernumbers=true]{biblatex}
\addbibresource{biblatex-examples.bib}
\begin{document}
Lorem \autocite{worman} ipsum \autocite{sigfridsson}
dolor \autocite{nussbaum} sit \autocite{aksin}
\printbibheading[title={Bibliography}]
\printbibliography[heading=subbibliography,
type=book, title={Books}]
\printbibliography[heading=subbibliography,
type=article, title={Articles}]
\end{document}
There are pathological cases where neither defernumbers=true nor
defernumbers=false produce fully desirable output. This may be the case
when entries can end up in several of the split bibliographies—or if there is an
additional global bibliography. But in most cases with non-overlapping split
bibliographiesdefernumbers=trueproducesbetterresults. biblatexwilltherefore
suggestsettingdefernumberstotrueinawarningwhenasplitbibliographysetup
isdetected. Thatwarningcanbesuppressedincasesettingdefernumberstotrueis
notdesirable.
3.15.6 ActiveCharactersinBibliographyHeadings
Packages using active characters, such as babel, polyglossia, csquotes, or
underscore,usuallydonotmakethemactiveuntilthebeginningofthedocument
154

bodytoavoidinterferencewithotherpackages. Atypicalexampleofsuchanactive
character is the us-ascii quote ", which is used by various language modules of
thebabel/polyglossiapackages. Ifshorthandssuchas"<and"aareusedinthe
argumentto\defbibheadingandtheheadingsaredefinedinthedocumentpream-
ble,thenon-activeformofthecharactersissavedintheheadingdefinition. When
theheadingistypeset,theydonotfunctionasacommandbutaresimplyprinted
literally. The most straightforward solution consists in moving \defbibheading
after \begin{document}. Alternatively, you may use babel’s \shorthandon and
\shorthandoffcommandstotemporarilymaketheshorthandsactiveinthepream-
ble. Theabovealsoappliestobibliographynotesandthe\defbibnotecommand.
3.15.7 GroupinginReferenceSectionsandSegments
AllLaTeXenvironmentsenclosedin\beginand\endformagroup. Thismayhave
undesirablesideeffectsiftheenvironmentcontainsanythingthatdoesnotexpect
tobeusedwithinagroup. Thisissueisnotspecifictorefsectionandrefsegment
environments,butitobviouslyappliestothemaswell. Sincetheseenvironments
willusuallyenclosemuchlargerportionsofthedocumentthanatypicalitemize
orsimilarenvironment,theyaresimplymorelikelytotriggerproblemsrelatedto
grouping. Ifyouobserveanymalfunctionsafteraddingrefsectionenvironmentsto
adocument(forexample,ifanythingseemstobe‘trapped’insidetheenvironment),
trythefollowingsyntaxinstead:
\chapter{...}
\refsection
...
\endrefsection
Thiswillnotformagroup,butotherwiseworksasusual. Asfarasbiblatexiscon-
cerned,itdoesnotmatterwhichsyntaxyouuse. Thealternativesyntaxisalsosup-
portedbytherefsegmentenvironment. Notethatthecommands\newrefsection
and\newrefsegmentdonotformagroup. See§§3.8.4and3.8.5fordetails.
3.16 UsingthefallbackBibTeXbackend
Toutiliseallofthefeaturesdescribedhere,biblatexmustbeusedwiththebiber
programasabackend. Indeed,thedocumentationingeneralassumesthis. However,
for a limited subset of use cases it is possible to use the long-established BibTeX
program(eitherthe7-bitbibtexor8-bitbibtex8)asthesupportingbackend. This
worksinmuchthesamewayasforbiberwiththeonlyprovisobeingthatBibTeX
ismuchmorelimitedasabackend.
Using BibTeX as the backend requires that the option backend=bibtex or
backend=bibtex8isgivenatloadtime. Thebiblatexpackagewillthenwriteap-
propriate data for use by BibTeX into the auxiliary file(s) and a special data file
(automatically included in those to be read by BibTeX). The BibTeX (8) program
shouldthenberunoneachauxiliaryfile: biblatexwilllistalloftherequiredfiles
inthelog.
KeylimitationsoftheBibTeXbackendare:
• Sortingisglobalandislimitedtous-asciiordering
• Nore-encodingispossibleandthusdatabaseentriesmustbeinLICRformto
workreliably
155

• Thedatamodelisfixed
• Cross-referencingismorelimitedandentrysetsmustbewrittenintothe.bib
file
• Fixedmemorycapacity(usingthe--wolfgangoptionwithbibtex8isstrongly
recommendedtominimizethelikelihoodofanissuehere)
4 Author Guide
This part of the manual documents the author interface of the biblatex package.
Theauthorguidecoverseverythingyouneedtoknowinordertowritenewcitation
andbibliographystylesorlocalisationmodules. Youshouldreadtheuserguidefirst
beforecontinuingwiththispartofthemanual.
4.1 Overview
Beforewegettothecommandsandfacilitiesprovidedbybiblatex,wewillhave
alookatsomeofitsfundamentalconcepts. Thebiblatexpackageusesauxiliary
filesinaspecialway. Mostnotably,thebblfileisuseddifferentlyandthereisno
conceptofastyle-dependentbstfile. WithLaTeX’sstandardbibliographicfacilities,
adocumentincludesanynumberofcitationcommandsinthedocumentbodyplus
\bibliographystyleand\bibliography,usuallytowardstheendofthedocument.
The location of the former is arbitrary, the latter marks the spot wherethe list of
referencesistobeprinted:
\documentclass{...}
\begin{document}
\cite{...}
...
\bibliographystyle{...}
\bibliography{...}
\end{document}
Processingthisfilesrequiresthatacertainprocedurebefollowed. Thisprocedureis
asfollows:
1. Runlatex: Onthefirstrun,\bibstyleand\bibdatacommandsarewritten
totheauxfile,alongwith\citationcommandsforallcitations. Atthispoint,
thereferencesareundefinedbecauseLaTeXiswaitingforBibTeXtosupply
therequireddata. Thereisalsonobibliographyyet.
2. Run bibtex: BibTeXwrites a thebibliography environmentto the bbl file,
supplyingallentriesfromthebibfilewhichwererequestedbythe\citation
commandsintheauxfile.
3. Run latex: Starting with the second run, the \bibitem commands in the
thebibliographyenvironmentwriteone\bibcitecommandforeachbiblio-
graphy entry to the aux file. These \bibcite commands define the citation
labelsusedby\cite. However,thereferencesarestillundefinedbecausethe
labelsarenotavailableuntiltheendofthisrun.
156

4. Runlatex: Startingwiththethirdrun,thecitationlabelsaredefinedasthe
auxfileisreadinattheendofthepreamble. Allcitationscannowbeprinted.
Notethatallbibliographicdataiswrittentothebblfileinthefinalformat. The
bbl file is read in and processed like any printable section of the document. For
example,considerthefollowingentryinabibfile:
@Book{companion,
| author | =   | {Michel | Goossens and | Frank | Mittelbach | and Alexander |
| ------ | --- | ------- | ------------ | ----- | ---------- | ------------- |
,→
Samarin},
| title     | =   | {The LaTeX        | Companion}, |     |     |     |
| --------- | --- | ----------------- | ----------- | --- | --- | --- |
| publisher | =   | {Addison-Wesley}, |             |     |     |     |
| address   | =   | {Reading,         | Mass.},     |     |     |     |
| year      | =   | {1994},           |             |     |     |     |
}
Withtheplain.bststyle,BibTeXexportsthisentrytothebblfileasfollows:
\bibitem{companion}
| Michel    | Goossens,       | Frank     | Mittelbach, | and    | Alexander | Samarin. |
| --------- | --------------- | --------- | ----------- | ------ | --------- | -------- |
| \newblock | {\em            | The LaTeX | Companion}. |        |           |          |
| \newblock | Addison-Wesley, |           | Reading,    | Mass., | 1994.     |          |
By default, LaTeX generates numeric citation labels, hence \bibitem writes lines
suchasthefollowingtotheauxfile:
\bibcite{companion}{1}
Implementingadifferentcitationstyleimpliesthatmoredatahastobetransferred
viatheauxfile. Withthenatbibpackage, forexample, theauxfilecontainslines
likethisone:
| \bibcite{companion}{{1}{1994}{{Goossens |     |     |     |     | et~al.}}{{Goossens, |     |
| --------------------------------------- | --- | --- | --- | --- | ------------------- | --- |
,→ Mittelbach,
and Samarin}}}
The biblatex package supports citations in any arbitrary format, hence citation
commandsneedaccesstoallbibliographicdata. Whatthiswouldmeanwithinthe
scopeoftheprocedureoutlinedabovebecomesobviouswhenlookingattheoutput
ofthejurabibpackagewhichalsomakesallbibliographicdataavailableincitations:
\bibcite{companion}{{Goossens\jbbfsasep Mittelbach\jbbstasep Samarin
,→ }%
| {}{{0}{}{book}{1994}{}{}{}{}{Reading, |     |     |     |     | Mass.\bpubaddr{}Addison- |     |
| ------------------------------------- | --- | --- | --- | --- | ------------------------ | --- |
,→ Wesley%
\bibbdsep{} 1994}}{{The LaTeX Companion}{}{}{2}{}{}{}{}{}}{\bibnf
{Goossens}{Michel}{M.}{}{}\Bibbfsasep\bibnf{Mittelbach}{Frank}{F.}%
{}{}\Bibbstasep\bibnf{Samarin}{Alexander}{A.}{}{}}{\bibtfont{The
| LaTeX                     | Companion}.\ |     | \apyformat{Reading, |     | Mass.\bpubaddr{} |     |
| ------------------------- | ------------ | --- | ------------------- | --- | ---------------- | --- |
| Addison-Wesley\bibbdsep{} |              |     | 1994}}}             |     |                  |     |
157

Inthiscase,thecontentsoftheentirethebibliographyenvironmentareeffectively
transferred via the aux file. The data is read from the bbl file, written to the aux
file,readbackfromtheauxfileandthenkeptinmemory. Thebibliographyitselfis
stillgeneratedasthebblfileisreadin. Thebiblatexpackagewouldalsobeforced
tocyclealldatathroughtheauxfile. Thisimpliesprocessingoverheadandisalso
redundantbecausethedatahastobekeptinmemoryanyway.
Thetraditionalprocedureisbasedontheassumptionthatthefullbibliographicdata
ofanentryisonlyrequiredinthebibliographyandthatallcitationsuseshortlabels.
Thismakesitveryeffectiveintermsofmemoryrequirements,butitalsoimpliesthat
itdoesnotscalewell. Thatiswhybiblatextakesadifferentapproach. Firstofall,
thedocumentstructureisslightlydifferent. Insteadofusing\bibliographyinthe
documentbody,databasefilesarespecifiedinthepreamblewith\addbibresource,
\bibliographystyleisomittedentirely(allfeaturesarecontrolledbypackageop-
tions),andthebibliographyisprintedusing\printbibliography:
\documentclass{...}
\usepackage[...]{biblatex}
\addbibresource{...}
\begin{document}
\cite{...}
...
\printbibliography
\end{document}
Inordertostreamlinethewholeprocedure,biblatexessentiallyemploysthebblfile
likeanauxfile,rendering\bibciteobsolete. Wethengetthefollowingprocedure:
1. Run latex: The first step is similar to the traditional procedure described
above: \bibstyleand\bibdatacommandsarewrittentothbcffile, along
with\citationcommandsforallcitations. Wethenwaitforthebackendto
supplytherequireddata.
2. Runbiber: Thebackendsuppliesthoseentriesfromthebibfilewhichwere
requestedbythe\citationcommandsintheauxiliaryfile. However,itdoes
not write a printable bibliography to the bbl file, but rather a structured
representationofthebibliographicdata. Justlikeanauxfile,thisbblfiledoes
notprintanythingwhenreadin. Itmerelyputsdatainmemory.
3. Runlatex: Startingwiththesecondrun,thebblfileisprocessedrightatthe
beginningofthedocumentbody,justlikeanauxfile. Fromthispointon,all
bibliographicdataisavailableinmemorysothatallcitationscanbeprinted
rightaway.30 Thecitationcommandshaveaccesstothecompletebibliographic
data,notonlytoapredefinedlabel. Thebibliographyisgeneratedfrommemory
usingthesamedataandmaybefilteredorsplitasrequired.
Let’sconsiderthesampleentrygivenaboveoncemore:
@Book{companion,
30Ifthedefernumberspackageoptionisenabledbiblatexusesanalgorithmsimilartothetraditional
proceduretogeneratenumericlabels. Inthiscase,thenumbersareassignedasthebibliographyis
printedandthencycledthroughthebackendauxiliaryfile. ItwilltakeanadditionalLaTeXrunfor
themtobepickedupincitations.
158

author = {Michel Goossens and Frank Mittelbach and Alexander
,→ Samarin},
title = {The LaTeX Companion},
publisher = {Addison-Wesley},
address = {Reading, Mass.},
year = {1994},
}
Thisentryisessentiallyexportedinthefollowingformat:
\entry{companion}{book}{}
\labelname{author}{3}{}{%
{{uniquename=0,hash=...}{Goossens}{G.}{Michel}{M.}{}{}{}{}}%
{{uniquename=0,hash=...}{Mittelbach}{M.}{Frank}{F.}{}{}{}{}}%
{{uniquename=0,hash=...}{Samarin}{S.}{Alexander}{A.}{}{}{}{}}%
}
\name{author}{3}{}{%
{{uniquename=0,hash=...}{Goossens}{G.}{Michel}{M.}{}{}{}{}}%
{{uniquename=0,hash=...}{Mittelbach}{M.}{Frank}{F.}{}{}{}{}}%
{{uniquename=0,hash=...}{Samarin}{S.}{Alexander}{A.}{}{}{}{}}%
}
\list{publisher}{1}{%
{Addison-Wesley}%
}
\list{location}{1}{%
{Reading, Mass.}%
}
\field{title}{The LaTeX Companion}
\field{year}{1994}
\endentry
Asseeninthisexample,thedataispresentedinastructuredformatthatresembles
the structure of a bib file to some extent. At this point, no decision concerning
the final format of the bibliography entry has been made. The formatting of the
bibliographyandallcitationsiscontrolledbyLaTeXmacros,whicharedefinedin
bibliographyandcitationstylefiles.
4.2 BibliographyStyles
Abibliographystyleisasetofmacroswhichprinttheentriesinthebibliography.
Suchstylesaredefinedinfileswiththesuffixbbx. Thebiblatexpackageloadsthe
selectedbibliographystylefileattheendofthepackage. Notethatasmallrepertory
offrequentlyusedmacrossharedbyseveralofthestandardbibliographystylesis
includedinbiblatex.def. Thisfileisloadedattheendofthepackageaswell,prior
totheselectedbibliographystyle.
4.2.1 BibliographyStyleFiles
Beforewegoovertheindividualcomponentsofabibliographystyle,considerthis
exampleoftheoverallstructureofatypicalbbxfile:
159

\ProvidesFile{example.bbx}[2006/03/15 v1.0 biblatex bibliography
,→ style]
\defbibenvironment{bibliography}
{...}
{...}
{...}
\defbibenvironment{shorthand}
{...}
{...}
{...}
\InitializeBibliographyStyle{...}
\DeclareBibliographyDriver{article}{...}
\DeclareBibliographyDriver{book}{...}
\DeclareBibliographyDriver{inbook}{...}
...
\DeclareBibliographyDriver{shorthand}{...}
\endinput
Themainstructureofabibliographystylefileconsistsofthefollowingcommands:
\RequireBibliographyStyle{hstylei}
Thiscommandisoptionalandintendedforspecializedbibliographystylesbuilton
topofamoregenericstyle. Itloadsthebibliographystylestyle.bbx.
\InitializeBibliographyStyle{hcodei}
Specifies arbitrary hcodei to be inserted at the beginning of the bibliography, but
insidethegroupformedbythebibliography. Thiscommandisoptional. Itmaybe
usefulfordefinitionswhicharesharedbyseveralbibliographydriversbutnotused
outsidethebibliography. Keepinmindthattheremaybeseveralbibliographiesina
document. Ifthebibliographydriversmakeanyglobalassignments,theyshouldbe
resetatthebeginningofthenextbibliography.
\DeclareBibliographyDriver{hentrytypei}{hcodei}
Definesabibliographydriver. A‘driver’isamacrowhichhandlesaspecificentry
type(whenprintingbibliographylists)oraspecificnamedbibliographylist(when
printingbibliographylists). Thehentrytypeicorrespondstotheentrytypeusedin
bib files, specified in lowercase letters (see § 2.1). The hentrytypei argument may
alsobeanasterisk. Inthiscase,thedriverservesasafallbackwhichisusedifno
specific driver for the entry type has been defined. The hcodei is arbitrary code
whichtypesetsallbibliographyentriesoftherespectivehentrytypei. Thiscommand
ismandatory. Everybibliographystyleshouldprovideadriverforeachentrytype.
\DeclareBibliographyAlias{haliasi}{hentrytypei}
Ifabibliographydrivercoversmorethanoneentrytype,thiscommandmaybeused
todefineanaliaswherehentrytypeiisthenameofadefineddriver. Thiscommandis
optional. Thehaliasiargumentmayalsobeanasterisk. Inthiscase,thehentrytypei
driverservesasafallbackwhichisusedifnospecificdriverforanentryhasbeen
defined.
160

Note that an alias declared with \DeclareBibliographyAlias only ‘reroutes’ the
bibliographydriverfromhaliasitohentrytypei. Type-specificformattingdirectives
stilloperatewiththeoldhaliasiname. \DeclareBibliographyAliasthusprovides
onlya‘soft’alias. Ifacompletealiasisdesiredsothathaliasiandhentrytypeiare
completelyindistinguishableandusethesametype-specificformatting,anapproach
with source mapping would be more appropriate (cf. the mappings for § 2.1.2 in
§A.1,thiswouldgivea‘hard’alias).
\DeclareBibliographyOption[hdatatypei]{hkeyi}[hvaluei]{hcodei}
This command defines additional preamble options in hkeyi=hvaluei format. The
hkeyiistheoptionkey. ThehcodeiisarbitraryTeXcodetobeexecutedwhenever
theoptionisused. Thevaluepassedtotheoptionispassedontothehcodeias#1.
Theoptionalhvalueiisadefaultvaluetobeusedifthebarekeyisgivenwithoutany
value. Thisisusefulforbooleanswitches. Thehdatatypeiisathedatatypeforthe
option. Ifomitted,itdefaultsto‘boolean’. Forexample,withadefinitionlikethe
following:
\DeclareBibliographyOption[boolean]{somekey}[true]{...}
giving‘somekey’withoutavalueisequivalentto‘somekey=true’. Validhdatatypei
valuesaredefinedinthedefaultbiberDatamodelas:
\DeclareDatamodelConstant[type=list]{optiondatatypes}{boolean,integer
,→ ,string,xml}
\DeclareTypeOption[hdatatypei]{hkeyi}[hvaluei]{hcodei}
Similarto\DeclareBibliographyOptionbutdefinesoptionswhicharesettableona
per-typebasisusingtheoptionalargumentof\ExecuteBibliographyOptions(see
§ 3.2.2). The hcodei is executed whenever biblatex prepares the data of an entry
ofthe type forwhich the option hasbeen set for useby a citationcommand or a
bibliographydriver.
\DeclareEntryOption[hdatatypei]{hkeyi}[hvaluei]{hcodei}
Similarto\DeclareBibliographyOptionbutdefinesoptionswhicharesettableon
a per-entry basis in the options field from § 2.2.3. The hcodei is executed when-
ever biblatex prepares the data of the entry for use by a citation command or a
bibliographydriver.
\DeclareBiblatexOption{hscope,…i}[hdatatypei]{hkeyi}[hvaluei]{hcodei}
Thiscommandisaconvenientinterfacetodeclareanoptionforseveralscopesat
once. Thehscopeiargumentmaybeacomma-separatedlistofscopesforwhichthe
option will be declared. Currently the scopes global, type, entry, namelist and
namearesupported,thefirstthreeofwhichareequivalenttodefiningtheoptionwith
\DeclareBibliographyOption,\DeclareTypeOptionand\DeclareEntryOption,re-
spectively.
161

4.2.2 BibliographyEnvironments
Apartfromdefiningbibliographydrivers,thebibliographystyleisalsoresponsible
for the environments which control the layout of the bibliography and bibliogra-
phy lists. These environments are defined with \defbibenvironment. By default,
\printbibliographyusestheenvironmentbibliography. Hereisadefinitionsuit-
ableforabibliographystylewhichdoesnotprintanylabelsinthebibliography:
\defbibenvironment{bibliography}
{\list
{}
{\setlength{\leftmargin}{\bibhang}%
\setlength{\itemindent}{-\leftmargin}%
\setlength{\itemsep}{\bibitemsep}%
\setlength{\parsep}{\bibparsep}}}
{\endlist}
{\item}
This definition employs a list environment with hanging indentation, using the
\bibhang length register provided by biblatex. It allows for a certain degree of
configurabilitybyusing\bibitemsepand\bibparsep,twolengthregistersprovided
bybiblatexforthisverypurpose(see§4.10.3). Theauthoryearandauthortitle
bibliographystylesuseadefinitionsimilartothisexample.
\defbibenvironment{bibliography}
{\list
{\printfield[labelnumberwidth]{labelnumber}}
{\setlength{\labelwidth}{\labelnumberwidth}%
\setlength{\leftmargin}{\labelwidth}%
\setlength{\labelsep}{\biblabelsep}%
\addtolength{\leftmargin}{\labelsep}%
\setlength{\itemsep}{\bibitemsep}%
\setlength{\parsep}{\bibparsep}}%
\renewcommand*{\makelabel}[1]{\hss##1}}
{\endlist}
{\item}
Somebibliographystylesprintlabelsinthebibliography. Forexample,abibliography
styledesignedforanumericcitationschemewillprintthenumberofeveryentry
suchthatthebibliographylookslikeanumberedlist. Inthefirstexample,thefirst
argument to \list was empty. In this example, we need it to insert the number,
which is provided by biblatex in the labelnumber field. We also employ several
lengthregistersandotherfacilitiesprovidedbybiblatex,see§§4.10.4and4.10.5
for details. The numeric bibliography style uses the definition given above. The
alphabeticstyleissimilar,exceptthatlabelnumberisreplacedbylabelalphaand
labelnumberwidthbylabelalphawidth.
Bibliographylistsarehandledinasimilarway. \printbiblistusestheenviron-
mentnamedafterthebibliographylistbydefault. Atypicalexampleisgivenbelow.
See§§4.10.4and4.10.5fordetailsonthelengthregistersandfacilitiesusedinthis
example.
162

\defbibenvironment{shorthand}
{\list
{\printfield[shorthandwidth]{shorthand}}
{\setlength{\labelwidth}{\shorthandwidth}%
\setlength{\leftmargin}{\labelwidth}%
\setlength{\labelsep}{\biblabelsep}%
\addtolength{\leftmargin}{\labelsep}%
\setlength{\itemsep}{\bibitemsep}%
\setlength{\parsep}{\bibparsep}%
\renewcommand*{\makelabel}[1]{##1\hss}}}
{\endlist}
{\item}
4.2.3 BibliographyDrivers
Before we go over the commands which form the data interface of the biblatex
package,itmaybeinstructivetohavealookatthestructureofabibliographydriver.
Notethattheexamplegivenbelowisgreatlysimplified,butstillfunctional. Forthe
sakeofreadability,weomitseveralfieldswhichmaybepartofa@bookentryand
alsosimplifythehandlingofthosewhichareconsidered. Themainpointistogive
youanideaofhowadriverisstructured. Forinformationaboutthemappingofthe
BibTeXfileformatfieldstobiblatex’sdatatypes,see§2.2.
\DeclareBibliographyDriver{book}{%
\printnames{author}%
\newunit\newblock
\printfield{title}%
\newunit\newblock
\printlist{publisher}%
\newunit
\printlist{location}%
\newunit
\printfield{year}%
\finentry}
The standard bibliography styles employ two bibliography macros begentry and
finentry:
\DeclareBibliographyDriver{entrytype}{%
\usebibmacro{begentry}
...
\usebibmacro{finentry}}
withthedefaultdefinitions
\newbibmacro*{begentry}{}
\newbibmacro*{finentry}{\finentry}
163

Useofthesemacrosisrecommendedforeasyhooksintothebeginningandendof
thedriver.
Returningtothedriverforthebookentrytypeabove,thereisstillonepiecemissing:
theformattingdirectivesusedby\printnames,\printlist,and\printfield. To
giveyouanideaofwhataformattingdirectivelookslike,herearesomefictional
onesusedbyoursampledriver. Fieldformatsarestraightforward,thevalueofthe
fieldispassedtotheformattingdirectiveasanargumentwhichmaybeformattedas
desired. Thefollowingdirectivewillsimplywrapitsargumentinan\emphcommand:
\DeclareFieldFormat{title}{\emph{#1}}
List formats are slightly more complex. After splitting up the list into individual
items,biblatexwillexecutetheformattingdirectiveonceforeveryiteminthelist.
The item is passed to the directive as an argument. The separator to be inserted
betweentheindividualitemsinthelistisalsohandledbythecorrespondingdirective,
hencewehavetocheckwhetherweareinthemiddleofthelistorattheendwhen
insertingit.
\DeclareListFormat{location}{%
#1%
\ifthenelse{\value{listcount}<\value{liststop}}
{\addcomma\space}
{}}
Formattingdirectivesfornamesaresimilartothoseforliterallists.
Names depend on the datamodel constant ‘nameparts’ which has the default
definition:
\DeclareDatamodelConstant[type=list]{nameparts}
{prefix,family,suffix,given}
Thiscanbecustomisedtoaddmorenamepartstodealwiththingslikepatronymics
(seetheexamplefile93-nameparts.tex). Thisneedsanextendednameformatfor
data sources since the standard BibTeX name format is very limited. biblatexml
(§D)handlesthisnativelyandthereisanextendednameformatwhichcanhandle
customnamepartswhenusingbiber(see§3.4).
Insidenameformats,the‘nameparts’constantdeclarationmakesavailabletwoor
threemacrosforeachnamepartdefinedinthedatamodel:
\namepart<namepart> \% The full <namepart>
\namepart<namepart>i \% The initials of the <namepart>
\namepart<namepart>un \% Numeric value indicating uniqueness level
,→ for <namepart>
\namepart‘namepart’unonlyexistsifthepackageoptionuniquenameisnotsetto
‘false’andcantakethefollowingvalues.
0 ‘namepart’ was not used in disambiguating the name (because
disambiguation=nonewassetin\DeclareUniquenameTemplate,see§4.11.4).
Inthiscasethestyleshoulddecidewhattoprintforthis‘namepart’
164

1 Initialsonlyshouldbeprintedfor‘namepart’toensureuniquenessaccording
totheuniquenamepackageoptionsetting
2 The full ‘namepart’ should be printed to ensure uniqueness according to the
uniquenamepackageoptionsetting
Note these per-namepart uniqueness macros are essentially an override of the
uniquename value (see § 4.6.2) for the name as a whole. Styles can choose to use
eitherthelessgranularuniquenamevalueorthemoredetailedper-namepartvalues.
UsuallythegeneraluniquenamevalueisenoughforordinaryWesternnamesbutthe
moregranularinformationper-namepartisprovidedtoallowsophisticatedname
uniquenessprocessingformorecomplexnameschemata.
Thenameformattingdirectiveisexecutedonceforeachnameinthenamelist.
Hereisasimplifiedexample—thestandardnameformatsaremoreintricate:
\DeclareNameFormat{author}{%
\ifthenelse{\value{listcount}=1}
{\namepartfamily%
\ifdefvoid{\namepartgiven}{}{\addcomma\space\namepartgiven}}
{\ifdefvoid{\namepartgiven}{}{\namepartgiven\space}%
\namepartfamily}%
\ifthenelse{\value{listcount}<\value{liststop}}
{\addcomma\space}
{}}
Theabovedirectivereversesthenameofthefirstauthor(“Family,Given”)andprints
theremainingnamesintheirregularsequence(“GivenFamily”). Notethattheonly
componentwhichisguaranteedtobeavailableisthefamilyname,hencewehave
to check which parts of the name are actually present. If a certain name part is
notavailable,thecorrespondingmacrowillbeempty. Aswithdirectivesforliteral
lists, theseparatortobeinsertedbetweentheindividualitemsinthenamelistis
alsohandledbytheformattingdirective,hencewehavetocheckwhetherweare
in the middle of the list or at the end when inserting it. This is what the second
\ifthenelsetestdoes. Seealso§4.4.2.
A similar output that also respects the \multinamedelim and \finalnamedelim
commandsaswellasthe‘prefix’and‘suffix’namepartscanbeachievedwith
\DeclareNameAlias{author}{family-given/given-family}
4.2.4 SpecialFields
Thefollowinglistsandfieldsareusedbybiblatextopassdatatobibliographydrivers
andcitationcommands. Theyarenotusedinbibfilesbutdefinedautomaticallyby
thepackage. Fromtheperspectiveofabibliographyorcitationstyle,theyarenot
differentfromthefieldsinabibfile.
4.2.4.1 GenericFields
<datetype>dateunspecified field(string)
If<datetype>dateheldaniso8601-24.3‘unspecified’,thisfieldwillbesettooneof
yearindecade,yearincentury,monthinyear,dayinmonthordayinyearwhichspec-
ifiesthegranularityoftheunspecifiedinformation. Thesestringscanbetestedfor
165

andalongwiththedaterangeswhichareautomaticallycreatedforsuch‘unspecified’
dates,astylemaychoosetoformatthedateinaspecialway. See§2.3.8. Forexample,
anentrywithdatessuchas:
@book{key,
date = {19uu},
origdate = {199u}
}
wouldresultinthesameinformationinthe.bblas:
@book{key,
date = {1900/1999},
origdate = {1990/1999}
}
butwouldadditionallyhavethefielddateunspecifiedsetto‘yearincentury’and
origdateunspecifiedsetto‘yearindecade’. Thisinformationcouldbeusedtorender
thedateasperhaps‘20thcentury’andorigdateas‘The1990s’,informationwhich
cannot be derived from the date ranges alone. Since such auto-generated ranges
haveknownvalues,giventhe‘unspecified’meta-information,itisrelativelyeasyto
usetherangevaluestoformatspecialcases. Whilethestandardstylesdonotdo
this,examplesaregiveninthefile96-dates.tex.
entrykey field(string)
Theentrykeyofaniteminthebibfile. Thisisthestringusedbybiblatexandthe
backendtoidentifyanentryinthebibfile.
Notethatthesetofcharactersallowedandusableinthestringforentrykeydepends
onthebackend(biber,BibTeX)aswellastheLaTeXengine(pdfLaTeX,LuaLaTeX,
XeLaTeX).Generally,us-ascii-letters(a-z,A-Z)andnumbers(0-9)aresafe,soare
the punctuation characters full stop (.) and solidus (/). The punctuation charac-
ters-_:;!? arealsosafeeveniftheyaremadeactivebybabel/polyglossia. Ifa
Unicodeengineisused,non-us-asciicharactersarealsoacceptable. Curlybraces
({}),commas,spaces,backslashes(\),hashes(#),percentcharacters(%)andtildes
(~)arealwaysforbidden. biberadditionallyforbidsroundbrackets(()),quotation
marks (", '), and the equals sign (=). The entrykey is case sensitive, but it is not
recommended to exploit that fact too much by introducing two different entries
whosekeydiffersonlyincapitalisation(e.g.,sigfridssonandSigfridsson). For
fullportabilityitisadvisabletosticktoaschemeoflowercase(andifsodesiredupper-
case)us-ascii-letters,numbersandasmallsetofacceptablepunctuationcharacters,
say.:-.
childentrykey field(string)
Thisfieldisnolongernecessaryorrecommended.Forbackwardscompatibility,itis Deprecated
merelyacopyoftheentrykeyfieldinanysetchildren.
labelnamesource field(literal)
Holds the name of the field used to populate labelname, determined by
\DeclareLabelname.
166

labeltitlesource field(literal)
Holds the name of the field used to populate labeltitle, determined by
\DeclareLabeltitle.
labeldatesource field(literal)
Holdsoneof:
• The prefix coming before ‘date’ of the date field name chosen by
\DeclareLabeldate
• Thenameofafield
• Aliteralorlocalisationstring
Normally holds the prefix coming before ‘date’ of the date field name chosen
by \DeclareLabeldate. For example, if the labeldate field is eventdate, then
labeldatesourcewillbe‘event’. Incase\DeclareLabeldateselectsthedatefield,
then labeldatesource will be defined but will be an empty string as the prefix
coming before ‘date’ in the date label name is empty. This is so that the con-
tentsoflabeldatesourcecanbeusedinconstructingreferencestothefieldwhich
\DeclareLabeldatechooses. Since\DeclareLabeldatecanalsoselectliteralstrings
forfallbacks,labeldatesourcemaynotrefertoafieldormaybeundefined. Bearin
mindthat\DeclareLabeldatecanalsobeusedtoselectnon-datefieldsasafallback
andsolabeldatesourcemightcontainafieldname. So,insummary,therulesare
\iffieldundef{labeldatesource}
{}% labeldate package option is not set
{\iffieldundef{\thefield{labeldatesource}year}
% \DeclareLabeldate resolved to either a literal/localisation
% string or a non-date field since
% if a date is defined by a date field, there is
% at least a year
{\iffieldundef{\thefield{labeldatesource}}
{}% \DeclareLabeldate resolved to a literal/localisation
,→ string
{}% \DeclareLabeldate resolved to a non-date field
}
{} % \DeclareLabeldate resolved a date field name prefix like ""
,→ or "orig"
}
entrytype field(string)
Theentrytype(@book,@inbook,etc.),giveninlowercaseletters.
childentrytype field(string)
Thisfieldisnolongernecessaryorrecommended.Forbackwardscompatibility,itis Deprecated
merelyacopyoftheentrytypefieldinanysetchildren.
entrysetcount field(integer)
Thisfieldholdsanintegerindicatingthepositionofasetmemberintheentryset
(startingat1). Thisfieldisonlyavailableinthesubentriesofanentryset.
167

hash field(string)
Thisfieldisspecialinthatitisonlyavailablelocallyinnameformattingdirectives.
It holds a hash string which uniquely identifies individual names in a name list.
Thisinformationisavailableforallnamesinallnamelists. Seealsonamehashand
fullhash. Sensitivetothehashcustomisationsdescribedin§4.11.5.
namehash field(string)
Ahashstringwhichuniquelyidentifiesthelabelnamelist. Thisisusefulforrecur-
rencechecks. Forexample,acitationstylewhichreplacesrecurrentauthorsoreditors
withastringlike‘idem’couldsavethenamehashfieldwith\savefieldanduseit
inacomparisonwith\iffieldequalslater(see§§4.6.1and4.6.2). Thenamehashis
derivedfromthetruncatedlabelnamelist,i.e.,itisresponsivetomaxcitenamesand
mincitenames. See also hash and fullhash. Sensitive to the hash customisations
describedin§4.11.5.
bibnamehash field(string)
Asnamehashbutresponsivetomaxbibnamesandminbibnames. Thisisnotusedin
standardstylesbutmaybeusedtomaketestsinbibliographylists(suchasthoseused
todeterminewhetherdashesshouldreplacerepeatedauthors)behavedifferently.
Sensitivetothehashcustomisationsdescribedin§4.11.5.
<namelist>namehash field(string)
Asnamehashforthenamelistcalled‘namelist’.
<namelist>bibnamehash field(string)
Asbibnamehashforthenamelistcalled‘namelist’.
fullhash field(string)
Ahashstringwhichuniquelyidentifiesthelabelnamelist. Thisfieldsdiffersfrom
namehashintwodetails: 1)Theshortauthorandshorteditorlistsareignoredwhen
generating the hash. 2) The hash always refers to the full list, ignoring maxnames
and minnames. See also hash and namehash. Sensitive to the hash customisations
describedin§4.11.5.
fullhashraw field(string)
As fullhash but not sensitive to the hash customisations described in § 4.11.5.
Basicallyahashofallofthefullnamepartsofanameasitappearsinthedata. Not
usedinthedefaultstylesbutcouldbeusedtodiscriminatebetweentheliteralgiven
glyphsofanameandthenameasitisdesiredtobeidentifiedfornamematching
purposes.
<namelist>fullhash field(string)
Asfullhashforthenamelistcalled‘namelist’.
<namelist>fullhashraw field(string)
Asfullhashrawforthenamelistcalled‘namelist’.
168

pageref list(literal)
If the backref package option is enabled, this list holds the page numbers of the
pagesonwhichtherespectivebibliographyentryiscited. Iftherearerefsection
environmentsinthedocument,thebackreferencesarelocaltothereferencesections.
sortinit field(literal)
Thisfieldholdstheinitialcharacteroftheinformationusedduringsorting.
sortinithash field(string)
Thisfieldholdsahashofthe(locale-specific)UnicodeCollationAlgorithmprimary
weight of the first extended grapheme cluster (essentially the first character) of
the string used during sorting. This is useful when subdividing the bibliography
alphabeticallyandisusedinternallyby\bibinitsep(see§3.12.4).
clonesourcekey field(string)
Thisfieldholdstheentrykeyoftheentryfromwhichanentrywascloned. Clones
arecreatedforentrieswhicharementionedinrelatedfieldsaspartofrelatedentry
processing,forexample.
urlraw field(verbatim)
Thisistheunencoded, rawversionofanyurl. Thisisintendedforusewhenthe
displayversionandclickablelinkversionofaURLaredifferent. Thiscanbethecase
whentheURLcontainsspecialorUnicodecharacters. Inthecasewherenosuch
charactersoccur,maybeidenticaltotheurl.
4.2.4.2 FieldsforUseinCitationLabels
labelalpha field(literal)
Alabelsimilartothelabelsgeneratedbythealpha.bststyleoftraditionalBibTeX.
Thisdefaultlabelconsistsofinitialsdrawnfromthelabelnamelistplusthelasttwo
digitsofthepublicationyear. Thelabelfieldmaybeusedtooverrideitsnon-numeric
portion. Ifthelabelfieldisdefined,biblatexwilluseitsvalueandappendthelast
twodigitsofthepublicationyearwhengeneratinglabelalpha. Theshorthandfield
may be used to override the entire label. If defined, labelalpha is the shorthand
rather than an automatically generated label. Users can specify a template used
toconstructthealphabeticlabel(see§4.5.5)andthedefaulttemplatemirrorsthe
formatmentionedforbibtexabove. Acomplete‘alphabetic’labelconsistsofthefields
labelalphaplusextraalpha. Notethatthelabelalphaandextraalphafieldsneed
toberequestedwiththepackageoptionlabelalpha(§3.1.2.3). Seealsoextraalpha
aswellas\labelalphaothersin§3.12.1.
extraalpha field(integer)
The‘alphabetic’citationschemeusuallyrequiresalettertobeappendedtothelabelif
thebibliographycontainstwoormoreworksbythesameauthorwhichwereallpub-
lishedinthesameyear. Inthiscase,theextraalphafieldholdsanintegerwhichmay
beconvertedtoaletterwith\mknumalphorformattedinsomeotherway. Thisfieldis
similartotheroleofextradateintheauthor-yearscheme. Acomplete‘alphabetic’
labelconsistsofthefieldslabelalphaplusextraalpha. Notethatthelabelalpha
andextraalphafieldsneedtoberequestedwiththepackageoptionlabelalpha,see
169

§3.1.2.3fordetails. Seealsolabelalphaaswellas\labelalphaothersin§3.12.1.
Table7summarisesthevariousextra*disambiguationcountersandwhattheytrack.
labelname list(name)
Thenametobeprintedincitations. Thislistisacopyofeithertheshortauthor,the
author, the shorteditor, the editor, or the translator list, which are normally
checkedforinthisorder. Ifnoauthorsandeditorsareavailable,thislistisundefined.
Notethatthislistisalsoresponsivetotheuse<name>,options,see§3.1.3. Citation
stylesshouldusethislistwhenprintingthenameinacitation. Thislistisprovided
forconvenienceonlyanddoesnotcarryanyadditionalmeaning. Thisfieldmaybe
customized. See§4.5.11fordetails.
extraname field(integer)
Holdsacountofthenumberofbibliographyentrieswithinarefsectionwhichderive
fromthesamelabelnamelist. Thiscountertakesaccountofuniquenamesettings(see
§3.1.2.3). Whilenotusedbyanystandardstyles,thisfieldisusefulinstyleswhich
wishtonumberbibliographyentriesonaper-labelnamebasis. Thisfieldwillonly
existifthereisalabelname. Theextranamecounterisrelatedto,butconceptually
differentfrom\ifsingletitle(see§3.1.2.3and§4.6.2).
labelnumber field(literal)
Thenumberofthebibliographyentry,asrequiredbynumericcitationschemes. If
theshorthandfieldisdefined,biblatexdoesnotassignanumbertotherespective
entry. In this case labelnumber is the shorthand rather than a number. Numeric
stylesmustusethevalueofthisfieldinsteadofacounter. Notethatthisfieldneeds
toberequestedwiththepackageoptionlabelnumber,see§3.1.2.3fordetails. Also
seethepackageoptiondefernumbersin§3.1.2.1.
labelprefix field(literal)
Ifthelabelprefixoptionof\newrefcontexthasbeensetinordertoprefixallentries
inasubbibliographywithafixedstring,thisstringisavailableinthelabelprefix
field of all affected entries. If no prefix has been set, the labelprefix field of the
respective entry is undefined. See the labelprefix option of \newrefcontext in
§3.8.10fordetails. Iftheshorthandfieldisdefined,biblatexdoesnotassignthe
prefixtothelabelprefixfieldoftherespectiveentry. Inthiscase,thelabelprefix
fieldisundefined.
labeltitle field(literal)
Theprintabletitleofawork. Insomecircumstances,astylemightneedtochoosea
titlefromalistofapossibletitlefields. Forexample,citationstylesprintingshort
titles may want to print the shorttitle field if it exists but otherwise print the
titlefield. Thelistoffieldstobeconsideredwhenconstructinglabeltitlemay
becustomized. See§4.5.11fordetails. Notethattheextratitlefieldneedstobe
requested with the package option labeltitle, see § 3.1.2.3 for details. See also
extratitle. Notealsothattheextratitleyearfieldneedstoberequestedwiththe
packageoptionlabeltitleyear. Seealsoextratitleyear.
extratitle field(integer)
It is sometimes useful, for example in author-title citation schemes, to be able to
disambiguateworkswiththesametitle. Forworksbythesamelabelnamewiththe
170

samelabeltitle,theextratitlefieldholdsanintegerwhichmaybeconvertedto
aletterwith\mknumalphorformattedinsomeotherway(oritcanbemerelyusedas
aflagtosaythatsomeotherfieldsuchasadateshouldbeusedinconjunctionwith
thelabeltitlefield). Thisfieldisundefinedifthereisonlyoneworkwiththesame
labeltitlebythesamelabelnameinthebibliography. Notethattheextratitle
field needs to be requested with the package option labeltitle, see § 3.1.2.3 for
details. Seealsolabeltitle. Table7summarisesthevariousextra*disambiguation
countersandwhattheytrack.
extratitleyear field(integer)
Itissometimesuseful,forexampleinauthor-titlecitationschemes,tobeabletodis-
ambiguateworkswiththesametitleinthesameyearbutwithnoauthor. Forworks
withthesamelabeltitleandwiththesamelabelyear,theextratitleyearfield
holdsanintegerwhichmaybeconvertedtoaletterwith\mknumalphorformattedin
someotherway(oritcanbemerelyusedasaflagtosaythatsomeotherfieldsuch
asapublishershouldbeusedinconjunctionwiththelabelyearfield). Thisfield
isundefinedifthereisonlyoneworkwiththesamelabeltitleandlabelyearin
thebibliography. Notethattheextratitleyearfieldneedstoberequestedwiththe
packageoptionlabeltitleyear,see§3.1.2.3fordetails. Seealsolabeltitleyear.
Table7summarisesthevariousextra*disambiguationcountersandwhattheytrack.
labelyear field(literal)
Theyearofthedatefieldselectedby\DeclareLabeldate(§4.5.11)ortheyearfield,
for use in author-year labels. A complete author-year label consists of the fields
labelyearplusextradate. Notethatthelabelyearandextradatefieldsneedto
berequestedwiththepackageoptionlabeldateparts,see§3.1.2.3fordetails. See
alsoextradate.
labelendyear field(literal)
Theendyearofthedatefieldselectedby\DeclareLabeldate(§4.5.11)iftheselected
dateisarange.
labelmonth field(datepart)
Themonthofthedatefieldselectedby\DeclareLabeldate(§4.5.11),orthemonth
field for use in author-year labels. Note that the labelmonth field needs to be
requestedwiththepackageoptionlabeldateparts,see§3.1.2.3fordetails.
labelendmonth field(datepart)
The end month of the date field selected by \DeclareLabeldate (§ 4.5.11) if the
selecteddateisarange.
labelday field(datepart)
The month of the date field selected by \DeclareLabeldate (§ 4.5.11) for use in
author-year labels. Note that the labelday field needs to be requested with the
packageoptionlabeldateparts,see§3.1.2.3fordetails.
labelendday field(datepart)
Theenddayofthedatefieldselectedby\DeclareLabeldate(§4.5.11)iftheselected
dateisarange.
171

extradate field(integer)
Theauthor-yearcitationschemeusuallyrequiresalettertobeappendedtotheyear
if the bibliography contains two or more works by the same author (actually the
labelname, which is usually the author by default but which need not be) which
were all published in the same year. In this case, the extradate field holds an in-
teger which may be converted to a letter with \mknumalph or formatted in some
other way. This field is undefined if there is only one work by the author in the
bibliographyorifallworksbytheauthorhavedifferentpublicationyears. Acom-
pleteauthor-yearlabelconsistsofthefieldslabelyearplusextradate. Notethat
thelabelyearandextradatefieldsneedtoberequestedwiththepackageoption
labeldateparts,see§3.1.2.3fordetails. Seealsolabelyear. Table7summarisesthe
variousextra*disambiguationcountersandwhattheytrack. Notethatbiblatex
allowsageneralisationofthisbehaviourandthedefaultcontextforextradatedis-
ambiguationcanbechangedtoallowothercontextsthantheauthor. Thedefaultwill
fallbacktothelabeltitleifthereisnolabelname(whichisusuallytheauthor).
See\DeclareExtradateContextin§4.5.11tocustomisetheextradatecontext.
extradatescope field(literal)
Thisfieldcontainsthenameofthemostspecificdatepartwhichdeterminedthevalue
ofextradate. Itisnotusedbythestandardstylesbutmaybeusefulincontrolling
theplacementoftheextradatefieldvalue. Forexample,iftwoworksbythesame
authorwithdates‘2020-05-04’and‘2020-06-04’weredisambiguatedbyextradate,
thenextradatascopewouldcontain‘labelyear’forbothentriesasthemostspecific
difference is the (label)year. If the dates were ‘2020-05-04’ and ‘2020-05-02’, then
extradatascopewouldcontain‘labelmonth’. Seealso\DeclareExtradate(§4.5.11)
whichdescribeshowtochangethescopeusedtotrackdates.
4.2.4.3 DateComponentFields
Note that it is possible to define new date fields in the datamodel which behave
exactlylikethedefaultdatamodeldatefieldsdescribedinthissection.
Seetable10foranoverviewofhowthedatefieldsinbibfilesarerelatedtothe
datefieldsprovidedbythestyleinterface. Whentestingforafieldlikeorigdatein
astyle,usecodelike:
\iffieldundef{origyear}{...}{...}
Thiswilltellyouifthecorrespondingdateisdefinedatall. Thistest:
\iffieldundef{origendyear}{...}{...}
willtellyouifthecorrespondingdateisdefinedanda(fullyspecified)range. This
test:
\iffieldequalstr{origendyear}{}{...}{...}
willtellyouifthecorrespondingdateisdefinedandanopen-endedrange. Open-
ended ranges are indicated by an empty endyear component (as opposed to an
undefined endyear component). See § 2.3.8 and table 3 on page 39 for further
examples.
172

Table10:DateInterface
| bibFile |                      | DataInterface      |                |
| ------- | -------------------- | ------------------ | -------------- |
| Field   | Value(Example)       | Field              | Value(Example) |
| date    | 1988                 | day                | undefined      |
|         |                      | month              | undefined      |
|         |                      | year               | 1988           |
|         |                      | yeardivision       | undefined      |
|         |                      | endday             | undefined      |
|         |                      | endmonth           | undefined      |
|         |                      | endyear            | undefined      |
|         |                      | endyeardivision    | undefined      |
|         |                      | hour               | undefined      |
|         |                      | minute             | undefined      |
|         |                      | second             | undefined      |
|         |                      | timezone           | undefined      |
|         |                      | endhour            | undefined      |
|         |                      | endminute          | undefined      |
|         |                      | endsecond          | undefined      |
|         |                      | endtimezone        | undefined      |
| date    | 1997/                | day                | undefined      |
|         |                      | month              | undefined      |
|         |                      | year               | 1997           |
|         |                      | yeardivision       | undefined      |
|         |                      | endday             | undefined      |
|         |                      | endmonth           | undefined      |
|         |                      | endyear            | empty          |
|         |                      | endyeardivision    | undefined      |
|         |                      | hour               | undefined      |
|         |                      | minute             | undefined      |
|         |                      | second             | undefined      |
|         |                      | timezone           | undefined      |
|         |                      | endhour            | undefined      |
|         |                      | endminute          | undefined      |
|         |                      | endsecond          | undefined      |
|         |                      | endtimezone        | undefined      |
| urldate | 2009-01-31           | urlday             | 31             |
|         |                      | urlmonth           | 01             |
|         |                      | urlyear            | 2009           |
|         |                      | urlyeardivision    | undefined      |
|         |                      | urlendday          | undefined      |
|         |                      | urlendmonth        | undefined      |
|         |                      | urlendyear         | undefined      |
|         |                      | urlendyeardivision | undefined      |
|         |                      | urlhour            | undefined      |
|         |                      | urlminute          | undefined      |
|         |                      | urlsecond          | undefined      |
|         |                      | urltimezone        | undefined      |
|         |                      | urlendhour         | undefined      |
|         |                      | urlendminute       | undefined      |
|         |                      | urlendsecond       | undefined      |
|         |                      | urlendtimezone     | undefined      |
| urldate | 2009-01-31T15:34:04Z | urlday             | 31             |
|         |                      | urlmonth           | 01             |
|         |                      | urlyear            | 2009           |
|         |                      | urlyeardivision    | undefined      |
|         |                      | urlendday          | undefined      |
|         |                      | urlendmonth        | undefined      |
|         |                      | urlendyear         | undefined      |
|         |                      | urlendyeardivision | undefined      |
|         |                      | urlhour            | 15             |
|         |                      | urlminute          | 34             |
173

Table10:DateInterface(cont’d)
|         |                           | urlsecond          | 04        |
| ------- | ------------------------- | ------------------ | --------- |
|         |                           | urltimezone        | Z         |
|         |                           | urlendhour         | undefined |
|         |                           | urlendminute       | undefined |
|         |                           | urlendsecond       | undefined |
|         |                           | urlendtimezone     | undefined |
| urldate | 2009-01-31T15:34:04+05:00 | urlday             | 31        |
|         |                           | urlmonth           | 01        |
|         |                           | urlyear            | 2009      |
|         |                           | urlyeardivision    | undefined |
|         |                           | urlendday          | undefined |
|         |                           | urlendmonth        | undefined |
|         |                           | urlendyear         | undefined |
|         |                           | urlendyeardivision | undefined |
|         |                           | urlhour            | 15        |
|         |                           | urlminute          | 34        |
|         |                           | urlsecond          | 04        |
|         |                           | urltimezone        | +0500     |
|         |                           | urlendhour         | undefined |
|         |                           | urlendminute       | undefined |
|         |                           | urlendsecond       | undefined |
|         |                           | urlendtimezone     | undefined |
| urldate | 2009-01-31T15:34:04/      | urlday             | 31        |
2009-01-31T16:04:34
|           |                       | urlmonth            | 1         |
| --------- | --------------------- | ------------------- | --------- |
|           |                       | urlyear             | 2009      |
|           |                       | urlyeardivision     | undefined |
|           |                       | urlendday           | 31        |
|           |                       | urlendmonth         | 1         |
|           |                       | urlendyear          | 2009      |
|           |                       | urlendyeardivision  | undefined |
|           |                       | urlhour             | 15        |
|           |                       | urlminute           | 34        |
|           |                       | urlsecond           | 4         |
|           |                       | urltimezone         | floating  |
|           |                       | urlendhour          | 16        |
|           |                       | urlendminute        | 4         |
|           |                       | urlendsecond        | 34        |
|           |                       | urlendtimezone      | floating  |
| origdate  | 2002-21/2002-23       | origday             | undefined |
|           |                       | origmonth           | 01        |
|           |                       | origyear            | 2002      |
|           |                       | origyeardivision    | spring    |
|           |                       | origendday          | undefined |
|           |                       | origendmonth        | 02        |
|           |                       | origendyear         | 2002      |
|           |                       | origendyeardivision | autumn    |
|           |                       | orighour            | undefined |
|           |                       | origminute          | undefined |
|           |                       | origsecond          | undefined |
|           |                       | origtimezone        | undefined |
|           |                       | origendhour         | undefined |
|           |                       | origendminute       | undefined |
|           |                       | origendsecond       | undefined |
|           |                       | origendtimezone     | undefined |
| eventdate | 1995-01-31/1995-02-05 | eventday            | 31        |
|           |                       | eventmonth          | 01        |
|           |                       | eventyear           | 1995      |
|           |                       | eventyeardivision   | undefined |
|           |                       | eventendday         | 05        |
|           |                       | eventendmonth       | 02        |
|           |                       | eventendyear        | 1995      |
174

Table10:DateInterface(cont’d)
eventendyeardivision undefined
eventhour undefined
eventminute undefined
eventsecond undefined
eventtimezone undefined
eventendhour undefined
eventendminute undefined
eventendsecond undefined
eventendtimezone undefined
hour field(datepart)
Thisfieldholdsthehourcomponentofthedatefield. Ifthedateisarange,itholds
thehourcomponentofthestartdate.
minute field(datepart)
This field holds the minute component of the date field. If the date is a range, it
holdstheminutecomponentofthestartdate.
second field(datepart)
Thisfieldholdsthesecondcomponentofthedatefield. Ifthedateisarange,itholds
thesecondcomponentofthestartdate.
timezone field(datepart)
Thisfieldholdsthetimezonecomponentofthedatefield. Ifthedateisarange,it
holdsthetimezonecomponentofthestartdate.
day field(datepart)
Thisfieldholdsthedaycomponentofthedatefield. Ifthedateisarange,itholds
thedaycomponentofthestartdate.
month field(datepart)
Thisfieldisthemonthasgiveninthedatabasefileoritholdsthemonthcomponent
ofthedatefield. Ifthedateisarange,itholdsthemonthcomponentofthestart
date.
year field(datepart)
Thisfieldistheyearasgiveninthedatabasefileoritholdstheyearcomponentof
thedatefield. Ifthedateisarange,itholdstheyearcomponentofthestartdate.
yeardivision field(datepart)
Thisfieldholdstheyeardivision(season,quarter,quadrimesteretc.) componentof
thedatefieldasspecifiedbyiso8601-24.8(§2.3.8). Itcontainsalocalisationstring
(§4.9.2.21). Ifthedateisarange,itholdstheyeardivisioncomponentofthestart
date.
season field(datepart)
Deprecated
Thisfieldholdstheseasoncomponentofthedatefieldasspecifiedbyiso8601-24.8
(§2.3.8). Itcontainsaseasonlocalisationstring(§4.9.2.21). Ifthedateisarange,
175

it holds the season component of the start date. This is deprecated in favour of
yeardivisionwhichismoregeneralised.
endhour field(datepart)
Ifthedatespecificationinthedatefieldisarange,thisfieldholdsthehourcomponent
oftheenddate.
endminute field(datepart)
If the date specification in the date field is a range, this field holds the minute
componentoftheenddate.
endsecond field(datepart)
If the date specification in the date field is a range, this field holds the second
componentoftheenddate.
endtimezone field(datepart)
If the date specification in the date field is a range, this field holds the timezone
componentoftheenddate.
endday field(datepart)
Ifthedatespecificationinthedatefieldisarange,thisfieldholdsthedaycomponent
oftheenddate.
endmonth field(datepart)
If the date specification in the date field is a range, this field holds the month
componentoftheenddate.
endyear field(datepart)
Ifthedatespecificationinthedatefieldisarange,thisfieldholdstheyearcomponent
oftheenddate. Ablank(butdefined)endyearcomponentindicatesanopenended
daterange.
endyeardivision field(datepart)
Ifthedatespecificationinthedatefieldisarange,thisfieldholdstheyeardivision
(season, quarter, quadrimester etc.) component of the end date as specified by
iso8601-2 4.8 (§ 2.3.8). It contains a year division localisation string (§ 4.9.2.21).
Ablank(butdefined)endyeardivisioncomponentindicatesanopenendeddate
range.
endseason field(datepart)
Deprecated
If the date specification in the date field is a range, this field holds the season
componentoftheenddateasspecifiedbyiso8601-24.8(§2.3.8). Itcontainsaseason
localisationstring(§4.9.2.21). Ablank(butdefined)endseasoncomponentindicates
anopenendeddaterange. Thisisdeprecatedinfavourofendyeardivisionwhich
ismoregeneralised.
176

orighour field(datepart)
Thisfieldholdsthehourcomponentoftheorigdatefield. Ifthedateisarange,it
holdsthehourcomponentofthestartdate.
origminute field(datepart)
Thisfieldholdstheminutecomponentoftheorigdatefield. Ifthedateisarange,it
holdstheminutecomponentofthestartdate.
origsecond field(datepart)
Thisfieldholdsthesecondcomponentoftheorigdatefield. Ifthedateisarange,it
holdsthesecondcomponentofthestartdate.
origtimezone field(datepart)
Thisfieldholdsthetimezonecomponentoftheorigdatefield. Ifthedateisarange,
itholdsthetimezonecomponentofthestartdate.
origday field(datepart)
Thisfieldholdsthedaycomponentoftheorigdatefield. Ifthedateisarange,it
holdsthedaycomponentofthestartdate.
origmonth field(datepart)
Thisfieldholdsthemonthcomponentoftheorigdatefield. Ifthedateisarange,it
holdsthemonthcomponentofthestartdate.
origyear field(datepart)
Thisfieldholdstheyearcomponentoftheorigdatefield. Ifthedateisarange,it
holdstheyearcomponentofthestartdate.
origyeardivision field(datepart)
Thisfieldholdstheyeardivision(season,quarter,quadrimesteretc.) componentof
theorigdatefieldasspecifiedbyiso8601-24.7(§2.3.8). Itcontainsayeardivision
localisation string (§ 4.9.2.21). If the date is a range, it holds the year division
component of the start date. This is deprecated in favour of origyeardivision
whichismoregeneralised.
origseason field(datepart)
Deprecated
Thisfieldholdstheseasoncomponentoftheorigdatefieldasspecifiedbyiso8601-2
4.7(§2.3.8). Itcontainsaseasonlocalisationstring(§4.9.2.21). Ifthedateisarange,
it holds the season component of the start date. This is deprecated in favour of
origyeardivisionwhichismoregeneralised.
origendhour field(datepart)
If the date specification in the origdate field is a range, this field holds the hour
componentoftheenddate.
177

origendminute field(datepart)
Ifthedatespecificationintheorigdatefieldisarange,thisfieldholdstheminute
componentoftheenddate.
origendsecond field(datepart)
Ifthedatespecificationintheorigdatefieldisarange,thisfieldholdsthesecond
componentoftheenddate.
origendtimezone field(datepart)
Ifthedatespecificationintheorigdatefieldisarange,thisfieldholdsthetimezone
componentoftheenddate.
origendday field(datepart)
If the date specification in the origdate field is a range, this field holds the day
componentoftheenddate.
origendmonth field(datepart)
Ifthedatespecificationintheorigdatefieldisarange,thisfieldholdsthemonth
componentoftheenddate.
origendyear field(datepart)
If the date specification in the origdate field is a range, this field holds the year
componentoftheenddate. Ablank(butdefined)origendyearcomponentindicates
anopenendedorigdaterange.
origendyeardivision field(datepart)
If the date specification in the origdate field is a range, this field holds the year
division(season,quarter,quadrimesteretc.) componentoftheenddateasspecified
byiso8601-24.8(§2.3.8). Itcontainsayeardivisionlocalisationstring(§4.9.2.21).
A blank (but defined) origendyeardivision component indicates an open ended
origdaterange.
origendseason field(datepart)
Deprecated
If the date specification in the origdate field is a range, this field holds the sea-
son component of the end date as specified by iso8601-2 4.8 (§ 2.3.8). It contains
aseasonlocalisationstring(§4.9.2.21). Ablank(butdefined)origendseasoncom-
ponent indicates an open ended origdate range. This is deprecated in favour of
origendyeardivisionwhichismoregeneralised.
eventhour field(datepart)
Thisfieldholdsthehourcomponentoftheeventdatefield. Ifthedateisarange,it
holdsthehourcomponentofthestartdate.
eventminute field(datepart)
Thisfieldholdstheminutecomponentoftheeventdatefield. Ifthedateisarange,
itholdstheminutecomponentofthestartdate.
178

eventsecond field(datepart)
Thisfieldholdsthesecondcomponentoftheeventdatefield. Ifthedateisarange,
itholdsthesecondcomponentofthestartdate.
eventtimezone field(datepart)
Thisfieldholdsthetimezonecomponentoftheeventdatefield. Ifthedateisarange,
itholdsthetimezonecomponentofthestartdate.
eventday field(datepart)
Thisfieldholdsthedaycomponentoftheeventdatefield. Ifthedateisarange,it
holdsthedaycomponentofthestartdate.
eventmonth field(datepart)
Thisfieldholdsthemonthcomponentoftheeventdatefield. Ifthedateisarange,
itholdsthemonthcomponentofthestartdate.
eventyear field(datepart)
Thisfieldholdstheyearcomponentoftheeventdatefield. Ifthedateisarange,it
holdstheyearcomponentofthestartdate.
eventyeardivision field(datepart)
This field holds the year division (season, quarter, quadrimester etc.) component
of the eventdate field as specified by iso8601-2 4.8 (§ 2.3.8). It contains a year
divisionlocalisationstring(§4.9.2.21). Ifthedateisarange,itholdstheyeardivision
componentofthestartdate.
eventseason field(datepart)
Deprecated
Thisfieldholdstheseasoncomponentoftheeventdatefieldasspecifiedbyiso8601-2
4.8(§2.3.8). Itcontainsaseasonlocalisationstring(§4.9.2.21). Ifthedateisarange,
it holds the season component of the start date. This is deprecated in favour of
eventyeardivisionwhichismoregeneralised.
eventendhour field(datepart)
Ifthedatespecificationintheeventdatefieldisarange,thisfieldholdsthehour
componentoftheenddate.
eventendminute field(datepart)
Ifthedatespecificationintheeventdatefieldisarange,thisfieldholdstheminute
componentoftheenddate.
eventendsecond field(datepart)
Ifthedatespecificationintheeventdatefieldisarange,thisfieldholdsthesecond
componentoftheenddate.
eventendtimezone field(datepart)
Ifthedatespecificationintheeventdatefieldisarange,thisfieldholdsthetimezone
componentoftheenddate.
179

eventendday field(datepart)
If the date specification in the eventdate field is a range, this field holds the day
componentoftheenddate.
eventendmonth field(datepart)
Ifthedatespecificationintheeventdatefieldisarange,thisfieldholdsthemonth
componentoftheenddate.
eventendyear field(datepart)
Ifthedatespecificationintheeventdatefieldisarange, thisfieldholdstheyear
componentoftheenddate. Ablank(butdefined)eventendyearcomponentindicates
anopenendedeventdaterange.
eventendyeardivision field(datepart)
Ifthedatespecificationintheeventdatefieldisarange, thisfieldholdstheyear
division(season,quarter,quadrimesteretc.) componentoftheenddateasspecified
byiso8601-24.8(§2.3.8). Itcontainsayeardivisionlocalisationstring(§4.9.2.21).
Ablank(butdefined)eventendyeardivisioncomponentindicatesanopenended
eventdaterange.
eventendseason field(datepart)
Deprecated
If the date specification in the eventdate field is a range, this field holds the sea-
soncomponentoftheenddateasspecifiedbyiso8601-24.8(§2.3.8). Itcontainsa
seasonlocalisationstring(§4.9.2.21). Ablank(butdefined)eventendseasoncom-
ponentindicatesanopenendedeventdaterange. Thisisdeprecatedinfavourof
eventendyeardivisionwhichismoregeneralised.
urlhour field(datepart)
Thisfieldholdsthehourcomponentoftheurldatefield. Ifthedateisarange,it
holdsthehourcomponentofthestartdate.
urlminute field(datepart)
Thisfieldholdstheminutecomponentoftheurldatefield. Ifthedateisarange,it
holdstheminutecomponentofthestartdate.
urlsecond field(datepart)
Thisfieldholdsthesecondcomponentoftheurldatefield. Ifthedateisarange,it
holdsthesecondcomponentofthestartdate.
timezone field(urldatepart)
Thisfieldholdsthetimezonecomponentoftheurldatefield. Ifthedateisarange,
itholdsthetimezonecomponentofthestartdate.
urlday field(datepart)
Thisfieldholdsthedaycomponentoftheurldatefield.
180

urlmonth field(datepart)
Thisfieldholdsthemonthcomponentoftheurldatefield.
urlyear field(datepart)
Thisfieldholdstheyearcomponentoftheurldatefield.
urlyeardivision field(datepart)
Thisfieldholdstheyeardivision(season,quarter,quadrimesteretc.) componentof
theurldatefieldasspecifiedbyiso8601-24.8(§2.3.8). Itcontainsayeardivision
localisation string (§ 4.9.2.21). If the date is a range, it holds the year division
componentofthestartdate.
urlseason field(datepart)
Deprecated
Thisfieldholdstheseasoncomponentoftheurldatefieldasspecifiedbyiso8601-2
4.8(§2.3.8). Itcontainsaseasonlocalisationstring(§4.9.2.21). Ifthedateisarange,
it holds the season component of the start date. This is deprecated in favour of
urlyeardivisionwhichismoregeneralised.
urlendhour field(datepart)
If the date specification in the urldate field is a range, this field holds the hour
componentoftheenddate.
urlendminute field(datepart)
Ifthedatespecificationintheurldatefieldisarange,thisfieldholdstheminute
componentoftheenddate.
urlendsecond field(datepart)
Ifthedatespecificationintheurldatefieldisarange,thisfieldholdsthesecond
componentoftheenddate.
urlendtimezone field(datepart)
Ifthedatespecificationintheurldatefieldisarange,thisfieldholdsthetimezone
componentoftheenddate.
urlendday field(datepart)
If the date specification in the urldate field is a range, this field holds the day
componentoftheenddate.
urlendmonth field(datepart)
Ifthedatespecificationintheurldatefieldisarange, thisfieldholdsthemonth
componentoftheenddate.
urlendyear field(datepart)
If the date specification in the urldate field is a range, this field holds the year
componentoftheenddate. Ablank(butdefined)urlendyearcomponentindicates
anopenendedurldaterange.
181

urlendyeardivision field(datepart)
If the date specification in the urldate field is a range, this field holds the year
division(season,quarter,quadrimesteretc.) componentoftheenddateasspecified
byiso8601-24.8(§2.3.8). Itcontainsayeardivisionlocalisationstring(§4.9.2.21).
A blank (but defined) urlendyeardivision component indicates an open ended
urldaterange.
urlendseason field(datepart)
Deprecated
Ifthedatespecificationintheurldatefieldisarange, thisfieldholdstheseason
component of the end date as specified by iso8601-2 4.8 (§ 2.3.8). It contains a
season localisation string (§ 4.9.2.21). A blank (but defined) urlendseason com-
ponent indicates an open ended urldate range. This is deprecated in favour of
urlendyeardivisionwhichismoregeneralised.
4.3 CitationStyles
Acitationstyleisasetofcommandssuchas\citewhichprintdifferenttypesof
citations. Suchstylesaredefinedinfileswiththesuffixcbx. Thebiblatexpackage
loads the selected citation style file at the end of the package. Note that a small
repertoryoffrequentlyusedmacrossharedbyseveralofthestandardcitationstyles
isalsoincludedinbiblatex.def. Thisfileisloadedattheendofthepackageaswell,
priortotheselectedcitationstyle. Italsocontainsthedefinitionsofthecommands
from§3.9.5.
4.3.1 CitationStyleFiles
Beforewegoovertheindividualcommandsavailableincitationstylefiles,consider
thisexampleoftheoverallstructureofatypicalcbxfile:
\ProvidesFile{example.cbx}[2006/03/15 v1.0 biblatex citation style]
\DeclareCiteCommand{\cite}{...}{...}{...}{...}
\DeclareCiteCommand{\parencite}[\mkbibparens]{...}{...}{...}{...}
\DeclareCiteCommand{\footcite}[\mkbibfootnote]{...}{...}{...}{...}
\DeclareCiteCommand{\textcite}{...}{...}{...}{...}
\endinput
\RequireCitationStyle{hstylei}
Thiscommandisoptionalandintendedforspecializedcitationstylesbuiltontopof
amoregenericstyle. Itloadsthecitationstylestyle.cbx.
\InitializeCitationStyle{hcodei}
Specifiesarbitraryhcodeirequiredtoinitializeorresetthecitationstyle. Thishook
will be executed once at package load-time and every time the \citereset com-
mandfrom§3.9.8isused. The\citeresetcommandalsoresetstheinternalcita-
tiontrackersofthispackage. Theresetwillaffectthe\ifciteseen,\ifentryseen,
\ifciteibid,and\ifciteidemtestsdiscussedin§4.6.2. Whenusedinarefsection
environment,theresetofthecitationtrackerislocaltothecurrentrefsectionen-
vironment.
182

\OnManualCitation{hcodei}
Specifies arbitrary hcodei required for a partial reset of the citation style. This
hookwillbeexecutedeverytimethe\mancitecommandfrom§3.9.8isused. Itis
particularlyusefulincitationstyleswhichreplacerepeatedcitationsbyabbreviations
like‘ibidem’or‘op. cit.’ whichmaygetambiguousifautomaticallygeneratedand
manualcitationsaremixed. The\mancitecommandalsoresetstheinternal‘ibidem’
and ‘idem’ trackers of this package. The reset will affect the \ifciteibid and
\ifciteidemtestsdiscussedin§4.6.2.
\DeclareCiteCommand{hcommandi}[hwrapperi]{hprecodei}{hloopcodei}{hsepcodei}{hpostcodei}
\DeclareCiteCommand*{hcommandi}[hwrapperi]{hprecodei}{hloopcodei}{hsepcodei}{hpostcodei}
Thisisthecorecommandusedtodefineallcitationcommands. Ittakesoneoptional
andfivemandatoryarguments. Thehcommandiisthecommandtobedefined,for
example\cite. Iftheoptionalhwrapperiargumentisgiven,theentirecitationwill
bepassedtothehwrapperiasanargument,i.e.,thewrappercommandmusttake
one mandatory argument.31 The hprecodei is arbitrary code to be executed at the
beginningofthecitation. Itwilltypicallyhandlethehprenoteiargumentwhichis
availableintheprenotefield. Itmayalsobeusedtoinitializemacrosrequiredby
thehloopcodei. Thehloopcodeiisarbitrarycodetobeexecutedforeachentrykey
passedtothehcommandi. Thisisthecorecodewhichprintsthecitationlabelsor
anyotherdata. Thehsepcodeiisarbitrarycodetobeexecutedaftereachiteration
of the hloopcodei. It will only be executed if a list of entry keys is passed to the
hcommandi. The hsepcodei will usually insert some kind of separator, such as a
commaorasemicolon. Thehpostcodeiisarbitrarycodetobeexecutedattheend
ofthecitation. Thehpostcodeiwilltypicallyhandlethehpostnoteiargumentwhich
is available in the postnote field.32 The starred variant of \DeclareCiteCommand
definesastarredhcommandi. Forexample,\DeclareCiteCommand*{\cite}would
define\cite*.33
\DeclareMultiCiteCommand{hcommandi}[hwrapperi]{hcitei}{hdelimiteri}
Thiscommanddefines‘multicite’commands(§3.9.3). Thehcommandiisthemul-
ticite command to be defined, for example \cites. It is automatically made ro-
bust. Multicite commands are built on top of backend commands defined with
\DeclareCiteCommand and the hcitei argument specifies the name of the backend
command to be used. Note that the wrapper of the backend command (i.e., the
hwrapperiargumentpassedto\DeclareCiteCommand)isignored. Usetheoptional
hwrapperiargumenttospecifyanalternativewrapper. Thehdelimiteriisthestring
to be printed as a separator between the individual citations in the list. This will
typically be \multicitedelim. The following examples are real definitions taken
frombiblatex.def:
\DeclareMultiCiteCommand{\cites}%
31Typicalexamplesofwrappercommandsare\mkbibparensand\mkbibfootnote.
32Thebibliographicdataavailabletothehloopcodeiisthedataoftheentrycurrentlybeingprocessed.
Inadditiontothat,thedataofthefirstentryisavailabletothehprecodeiandthedataofthelastone
isavailabletothehpostcodei. ‘First’and‘last’refertotheorderinwhichthecitationsareprinted.
Ifthesortcitespackageoptionisactive,thisistheorderofthelistaftersorting. Notethatno
bibliographicdataisavailabletothehsepcodei.
33Notethattheregularvariantof\DeclareCiteCommanddefinesastarredversionofthehcommandi
implicitly,unlessthestarredversionhasbeendefinedbefore.Thisisintendedasafallback.The
implicitdefinitionisanaliasfortheregularvariant.
183

{\cite}{\multicitedelim}
\DeclareMultiCiteCommand{\parencites}[\mkbibparens]%
{\parencite}{\multicitedelim}
\DeclareMultiCiteCommand{\footcites}[\mkbibfootnote]%
{\footcite}{\multicitedelim}
\DeclareAutoCiteCommand{hnamei}[hpositioni]{hcitei}{hmulticitei}
Thiscommandprovidesdefinitionsforthe\autociteand\autocitescommands
from § 3.9.4. The definitions are enabled with the autocite package option from
§3.1.2.1. Thehnameiisanidentifierwhichservesasthevaluepassedtothepack-
age option. The autocite commands are built on top of backend commands like
\parenciteand\parencites. Theargumentshciteiandhmulticiteispecifytheback-
endcommandstouse. Thehciteiargumentrefersto\autociteandhmulticiteirefers
to\autocites. Thehpositioniargumentcontrolsthehandlingofanypunctuation
marksafterthecitation. Possiblevaluesarel,r,f. rmeansthatthepunctuationis
placedtotherightofthecitation, i.e.,itwillnotbemovedaround. lmeansthat
anypunctuationafterthecitationismovedtotheleftofthecitation. fislikerina
footnoteandlikelotherwise. Thisargumentisoptionalanddefaultstor. Seealso
\DeclareAutoPunctuationin§4.7.5andtheautopunctpackageoptionin§3.1.2.1.
Thefollowingexamplesarerealdefinitionstakenfrombiblatex.def:
\DeclareAutoCiteCommand{plain}{\cite}{\cites}
\DeclareAutoCiteCommand{inline}{\parencite}{\parencites}
\DeclareAutoCiteCommand{footnote}[l]{\footcite}{\footcites}
\DeclareAutoCiteCommand{footnote}[f]{\smartcite}{\smartcites}
Adefinitionprovidedinthedocumentpreamblecanbesubsequentlyadoptedwith
thefollowing: (see§3.2.2).
\ExecuteBibliographyOptions{autocite=name}
\DeclareCitePunctuationPosition{hcommandi}{hpositioni}
Setupthecitecommandhcommanditomovepunctuationmarksafterthecitation
like\autocite. Thehpositioniargumentcantakethevaluesr,l,f,c,oandd. Ifan
unknownhpositioniidentifierisused,itdefaultstoo.
r Thepunctuationmarkisnotmovedandremainstotherightofthe
citation.
l The punctuation mark is moved to the left of the citation and thus
appearsbeforeit.
f Likerinfootnotesandlikelotherwise.
c Passthepunctuationontotheinternalimplementationofthecitation
commands. Itwillthenbeexecutedwithinthehwrappericommand
ifgiven.
o Retainthedefaultsetupofcforcitationdefinedcommandswithout
hwrapperi command and l for citation commands defined with a
hwrappericommand.
184

d Droptheexplicitpunctuationmark. Itwillonlybeavailableasthe
fieldpostpunct.
Thiscommandcannotbeusedfor\autocite,toconfigure\autociteusetheop-
tionalhpositioniargumentfor\DeclareAutoCiteCommand.
4.3.2 SpecialFields
Thefollowingfieldsareusedbybiblatextopassdatatocitationcommands. Theyare
notusedinbibfilesbutdefinedautomaticallybythepackage. Fromtheperspective
ofacitationstyle,theyarenotdifferentfromthefieldsinabibfile. Seealso§4.2.4.
prenote field(literal)
The hprenotei argument passed to a citation command. This field is specific to
citationsandnotavailableinthebibliography. Ifthehprenoteiargumentismissing
orempty,thisfieldisundefined.
postnote field(literal)
The hpostnotei argument passed to a citation command. This field is specific to
citationsandnotavailableinthebibliography. Ifthehpostnoteiargumentismissing
orempty,thisfieldisundefined.
multiprenote field(literal)
Thehmultiprenoteiargumentpassedtoamulticitecommand. Thisfieldisspecific
tocitationsandnotavailableinthebibliography. Ifthehmultiprenoteiargumentis
missingorempty,thisfieldisundefined.
multipostnote field(literal)
Thehmultipostnoteiargumentpassedtoamulticitecommand. Thisfieldisspecific
tocitationsandnotavailableinthebibliography. Ifthehmultipostnoteiargumentis
missingorempty,thisfieldisundefined.
volcitevolume field(literal)
Thehvolumeiargumentpassedto\volciteorarelatedcitationcommand(§3.9.6).
Thisfieldisspecificto\volcitecitationsandnotavailableinthebibliographyor
othercitations.
volcitepages field(literal)
Thehpagesiargumentpassedto\volciteorarelatedcitationcommand(§3.9.6).
Thisfieldisspecificto\volcitecitationsandnotavailableinthebibliographyor
othercitations. Ifthehpagesiargumentismissingorempty,thisfieldisundefined.
postpunct field(punctuationcommand)
Thetrailingpunctuationargumentimplicitlypassedtoacitationcommand. This
field is specific to citations and not available in the bibliography. If the character
followingagivencitationcommandisnotspecifiedin\DeclareAutoPunctuation
(§4.7.5),thisfieldisundefined.
4.4 DataInterface
Thedatainterfacearethefacilitiesusedtoformatandprintallbibliographicdata.
Thesefacilitiesareavailableinbothbibliographyandcitationstyles.
185

4.4.1 DataCommands
Thissectionintroducesthemaindatainterfaceofthebiblatexpackage. Theseare
thecommandsdoingmostofthework,i.e.,theyactuallyprintthedataprovidedin
listsandfields.
\DeprecateField{hfieldi}{hmessagei}
\DeprecateList{hlisti}{hmessagei}
\DeprecateName{hnamei}{hmessagei}
Whenanattemptismadetoprinthfieldi,hlisti,hnamei,adeprecationwarningis
issuedwiththeadditionalhmessagei. Thisaidsstyleauthorswhoarechangingfield
namesintheirstyle. Notethatthedeprecateditemmustnolongerbedefinedinthe
datamodelforthistowork;hfieldi,hlistiorhnameicannotbelistedanywhereasan
argumentto\DeclareDatamodelFields.
\DeprecateFieldWithReplacement{hfieldi}{hreplacementi}
\DeprecateListWithReplacement{hlisti}{hreplacementi}
\DeprecateNameWithReplacement{hnamei}{hreplacementi}
Similarto\DeprecateField,\DeprecateListand\DeprecateName. Thecommands
donotonlyissueadeprecationwarning,theytrytodefineareplacementforthe
deprecatedfieldthatisprintedinitsstead. The\replacementmustbeofthesame
typeasthedeprecatedhfieldi,hlistiorhnamei. Iftheformattingofhreplacementi
shouldbeappliedwhenprintingthedeprecatedfield,thatneedstoberequestedwith
\DeclareFieldAlias (see § 4.4.2). Note that the deprecated item must no longer
bedefinedinthedatamodelforthiswork;hfieldi,hlistiorhnameicannotbelisted
anywhereasanargumentto\DeclareDatamodelFields.
\printfield[hformati]{hfieldi}
This command prints a hfieldi using the formatting directive hformati, as defined
with\DeclareFieldFormat. Ifatype-specifichformatihasbeendeclared,thetype-
specificformattingdirectivetakesprecedenceoverthegenericone. Ifthehfieldiis
undefined,nothingisprinted. Ifthehformatiisomitted,\printfieldtriesusingthe
nameofthefieldasaformatname. Forexample,ifthetitlefieldistobeprinted
andthehformatiisnotspecified,itwilltrytousethefieldformattitle.34 Inthis
case,anytype-specificformattingdirectivewillalsotakeprecedenceoverthegeneric
one. If all of these formats are undefined, it falls back to default as a last resort.
Notethat\printfieldprovidesthenameofthefieldcurrentlybeingprocessedin
\currentfieldforuseinfieldformattingdirectives.
\printlist[hformati][hstarti–hstopi]{hliterallisti}
Thiscommandloopsoverallitemsinahliterallisti,startingatitemnumberhstarti
andstoppingatitemnumberhstopi,includinghstartiandhstopi(alllistsarenum-
bered starting at 1). Each item is printed using the formatting directive hformati,
asdefinedwith\DeclareListFormat. Ifatype-specifichformatihasbeendeclared,
thetype-specificformattingdirectivetakesprecedenceoverthegenericone. Ifthe
hliterallistiisundefined,nothingisprinted. Ifthehformatiisomitted,\printlist
tries using the name of the list as a format name. In this case, any type-specific
formattingdirectivewillalsotakeprecedenceoverthegenericone. Ifallofthese
34Inotherwords,\printfield{title}isequivalentto\printfield[title]{title}.
186

formats are undefined, it falls back to default as a last resort. The hstarti argu-
ment defaults to 1; hstopi defaults to the total number of items in the list. If the
totalnumberisgreaterthanhmaxitemsi,hstopidefaultstohminitemsi(see§3.1.2.1).
See \printnames for further details. Note that \printlist provides the name of
theliterallistcurrentlybeingprocessedin\currentlistforuseinlistformatting
directives.
\printnames[hformati][hstarti–hstopi]{hnamelisti}
Thiscommandloopsoverallitemsinahnamelisti,startingatitemnumberhstarti
andstoppingatitemnumberhstopi,includinghstartiandhstopi(alllistsarenum-
bered starting at 1). Each item is printed using the formatting directive hformati,
asdefinedwith\DeclareNameFormat. Ifatype-specifichformatihasbeendeclared,
thetype-specificformattingdirectivetakesprecedenceoverthegenericone. Ifthe
hnamelistiisundefined,nothingisprinted. Ifthehformatiisomitted,\printnames
tries using the name of the list as a format name. In this case, any type-specific
formattingdirectivewillalsotakeprecedenceoverthegenericone. Ifallofthese
formatsareundefined,itfallsbacktodefaultasalastresort. Thehstartiargument
defaults to 1; hstopi defaults to the total number of items in the list. If the total
numberisgreaterthanhmaxnamesi,hstopidefaultstohminnamesi(see§3.1.2.1). If
youwanttoselectarangebutusethedefaultlistformat,thefirstoptionalargument
muststillbegiven,butisleftempty:
\printnames[][1-3]{...}
One of hstarti and hstopi may be omitted, hence the following arguments are all
valid:
\printnames[...][-1]{...}
\printnames[...][2-]{...}
\printnames[...][1-3]{...}
Ifyouwanttooverridehmaxnamesiandhminnamesiandforceprintingoftheentire
list,youmayrefertothelisttotalcounterinthesecondoptionalargument:
\printnames[...][-\value{listtotal}]{...}
Whenever\printnamesand\printlistprocessalist,informationconcerningthe
currentstateisaccessiblebywayoffourcounters: thelisttotalcounterholdsthe
totalnumberofitemsinthecurrentlist,listcountholdsthenumberoftheitem
currentlybeingprocessed,liststartisthehstartiargumentpassedto\printnames
or \printlist, liststop is the hstopi argument. These counters are intended for
useinlistformattingdirectives. listtotalmayalsobeusedinthesecondoptional
argumentto\printnamesand\printlist. Notethatthesecountersarelocaltolist
formattingdirectivesanddonotholdmeaningfulvalueswhenusedanywhereelse.
Foreverylist,thereisalsoacounterbythesamenamewhichholdsthetotalnumber
ofitemsinthecorrespondinglist. Forexample,theauthorcounterholdsthetotal
numberofitemsintheauthorlist. Thesecountersaresimilartolisttotalexcept
that they may also be used independently of list formatting directives. There are
alsomaxnamesandminnamesaswellasmaxitemsandminitemscounterswhichhold
187

thevaluesofthecorrespondingpackageoptions. See§4.10.5foracompletelistof
suchinternalcounters. Notethat\printnamesprovidesthenameofthenamelist
currentlybeingprocessedin\currentnameforuseinnameformattingdirectives.
\printtext[hformati]{htexti}
Thiscommandprintshtexti,whichmaybeprintabletextorarbitrarycodegenerating
printabletext. Itclearsthepunctuationbufferbeforeinsertinghtextiandinforms
biblatexthatprintabletexthasbeeninserted. Thisensuresthatallprecedingand
following\newblockand\newunitcommandshavethedesiredeffect. \printfield
and\printnamesaswellas\bibstringanditscompanioncommands(see§4.8)do
thatautomatically. Usingthiscommandisrequiredifabibliographystylesinserts
literal text (including the commands from §§ 4.7.3 and 4.7.4) to ensure that block
andunitpunctuationworksasadvertisedin§4.7.1. Theoptionalhformatiargument
specifiesafieldformattingdirectivetobeusedtoformathtexti. Thismayalsobe
usefulwhenseveralfieldsaretobeprintedasonechunk,forexample,byenclosing
the entire chunk in parentheses or quotation marks. If a type-specific hformati
hasbeendeclared,thetype-specificformattingdirectivetakesprecedenceoverthe
genericone. Ifthehformatiisomitted,thehtextiisprintedasis. Seealso§4.11.8
forsomepracticalhints.
\printfile[hformati]{hfilei}
This command is similar to \printtext except that the second argument is a file
nameratherthanliteraltext. ThehfileiargumentmustbethenameofavalidLaTeX
file found in TeX’s search path. \printfile will use \input to load this hfilei. If
there is no such file, \printfile does nothing. The optional hformati argument
specifies a field formatting directive to be applied to the hfilei. If a type-specific
hformatihasbeendeclared,thetype-specificformattingdirectivetakesprecedence
overthegenericone. Ifthehformatiisomitted,thehfileiisprintedasis. Notethat
thisfeatureneedstobeenabledexplicitlybysettingthepackageoptionloadfiles
from§3.1.2.1. Bydefault,\printfilewillnotinputanyfiles.
\printdate Thiscommandprintsthedateoftheentry,asspecifiedinthefieldsdateormonth/
year. The date format is controlled by the package option date from § 3.1.2.1.
Additionalformatting(fontsetc.) maybeappliedbyadjustingthefieldformatdate
(§4.10.4). Notethatthiscommandinterfaceswiththepunctuationtracker. Thereis
noneedtowrapitina\printtextcommand.
\printdateextra Similarto\printdatebutincorporatestheextradatefieldinthedatespecification.
Thisisusefulforbibliographystylesdesignedforauthor-yearcitations.
\printlabeldate Similarto\printdatebutprintsthedatefielddeterminedby\DeclareLabeldate.
Thedateformatiscontrolledbythepackageoptionlabeldatefrom§3.1.2.1. Addi-
tionalformattingmaybeappliedbyadjustingthefieldformatlabeldate(§4.10.4).
\printlabeldateextra Similar to \printlabeldate but incorporates the extradate field in the date
specification. Thisisusefulforbibliographystylesdesignedforauthor-yearcitations.
\print<datetype>date As\printdatebutprintsthe<datetype>dateoftheentry. Thedateformat
is controlled by the package option <datetype>date from § 3.1.2.1. Additional
formattingmaybeappliedbyadjustingthefieldformat<datetype>date(§4.10.4).
The <datetype>s in the default data model are ‘’ (for the main date field), ‘orig’,
‘event’and‘url’.
188

\printtime Thiscommandprintsthetimerangeoftheentry,asspecifiedinthedatefield(see
§ 2.3.8). The time format is controlled by the package option time from § 3.1.2.1.
Additionalformatting(fontsetc.) maybeappliedbyadjustingthefieldformattime
(§4.10.4). Relevanttotimeformattingarethetimezerosoptionandthe\bibtimesep
and\bibtimezonesepmacros(§3.12.3). Notethatthiscommandinterfaceswiththe
punctuationtracker. Thereisnoneedtowrapitina\printtextcommand. Note
that this command prints a stand-alone time range apart from the date elements.
With the <datepart>dateusetime option, you can have the printed along with
a date when printing a date range instead of printing the time range completely
separately,whichiswhatthiscommandallowsfor.
\print<datetype>time As\printtimebutprintsthe<datetype>timeoftheentry. Thetimeformat
is controlled by the package option <datetype>time from § 3.1.2.1. Additional
formattingmaybeappliedbyadjustingthefieldformat<datetype>time(§4.10.4).
The <datetype>s in the default data model are ‘’ (for the main date field), ‘orig’,
‘event’and‘url’.
\indexfield[hformati]{hfieldi}
This command is similar to \printfield except that the hfieldi is not printed
but added to the index using the formatting directive hformati, as defined with
\DeclareIndexFieldFormat. Ifatype-specifichformatihasbeendeclared,ittakes
precedence over the generic one. If the hfieldi is undefined, this command does
nothing. If the hformati isomitted, \indexfield triesusing the name of the field
asaformatname. Inthiscase,anytype-specificformattingdirectivewillalsotake
precedenceoverthegenericone. Ifalloftheseformatsareundefined,itfallsbackto
defaultasalastresort.
\indexlist[hformati][hstarti–hstopi]{hliterallisti}
This command is similar to \printlist except that the items in the list are not
printedbutaddedtotheindexusingtheformattingdirectivehformati,asdefined
with\DeclareIndexListFormat. Ifatype-specifichformatihasbeendeclared,the
type-specific formatting directive takes precedence over the generic one. If the
hliterallisti is undefined, this command does nothing. If the hformati is omitted,
\indexlisttriesusingthenameofthelistasaformatname. Inthiscase,anytype-
specificformattingdirectivewillalsotakeprecedenceoverthegenericone. Ifallof
theseformatsareundefined,itfallsbacktodefaultasalastresort.
\indexnames[hformati][hstarti–hstopi]{hnamelisti}
This command is similar to \printnames except that the items in the list are not
printedbutaddedtotheindexusingtheformattingdirectivehformati,asdefined
with\DeclareIndexNameFormat. Ifatype-specifichformatihasbeendeclared,the
type-specific formatting directive takes precedence over the generic one. If the
hnamelisti is undefined, this command does nothing. If the hformati is omitted,
\indexnamestriesusingthenameofthelistasaformatname. Inthiscase,anytype-
specificformattingdirectivewillalsotakeprecedenceoverthegenericone. Ifallof
theseformatsareundefined,itfallsbacktodefaultasalastresort.
\entrydata{hkeyi}{hcodei}
\entrydata*{hkeyi}{hcodei}
Datacommandslike\printfieldnormallyusethedataoftheentrycurrentlybeing
processed. Youmayuse\entrydatatoswitchcontextslocally. Thehkeyiistheentry
189

keyoftheentrytouselocally. Thehcodeiisarbitrarycodetobeexecutedinthis
context. Thiscodewillbeexecutedinagroup. See§4.11.7foranexample. Notethat
thiscommandwillautomaticallyswitchlanguagesiftheautolangpackageoptionis
enabled. Thestarredversion\entrydata*willcloneallfieldsoftheenclosingentry,
usingfield,counter,andotherresourcenamesprefixedwiththestring‘saved’. This
isusefulwhencomparingtwodatasets. Forexample,insidethehcodeiargument,
the author field holds the author of entry hkeyi and the author of the enclosing
entryisavailableassavedauthor. Theauthorcounterholdsthenumberofnames
intheauthorfieldofhkeyi;thesavedauthorcounterreferstotheauthorcountof
theenclosingentry.
\entryset{hprecodei}{hpostcodei}
Thiscommandisintendedforuseinbibliographydrivershandling@setentries. It
willloopoverallmembersoftheset,asindicatedbytheentrysetfield,andexecute
theappropriatedriverfortherespectivesetmember. Thisissimilartoexecutingthe
\usedrivercommandfrom§4.6.4foreachsetmember. Thehprecodeiisarbitrary
codetobeexecutedpriortoprocessingeachitemintheset. Thehpostcodeiisarbitrary
codetobeexecutedimmediatelyafterprocessingeachitem. Bothargumentsare
mandatory in terms of the syntax but may be left empty. See § 4.11.1 for usage
examples.
\DeclareFieldInputHandler{hfieldi}{hcodei}
Thiscommandcanbeusedtodefineadatainputhandlerforhfieldiwhenitisread
from the .bbl. The hcodei is passed one argument (#1), which contains the input
fieldvalue,itshouldthenredefinethecommand\NewValue,whichholdsthedesired
outputfieldvalue. Forexample, toignorethevolumesfieldwhenitappears, you
coulddo
\DeclareFieldInputHandler{volumes}{\def\NewValue{}}
Generally,youwouldwanttouse\DeclareSourcemap(see§4.5.3)toremoveand
modifyfieldsbutthisalternativemethodmaybeusefulinsomecircumstanceswhen
the emphasis is on appearance rather than data since the hcodei can be arbitrary
TeX.
Ingeneral,\DeclareFieldInputHandlershouldnotbeusedtoapplyformattingto
afield,sincethatshouldhappenwith\DeclareFieldFormat,sothefollowingisjust
atoyexamplethatshowshow\DeclareFieldInputHandlerworks.
\DeclareFieldInputHandler{volumes}{\def\NewValue{\textbf{#1}}}
\DeclareListInputHandler{hlisti}{hcodei}
As \DeclareFieldInputHandler but for lists. Within the hcodei, the macro
\NewValue contains the value of the list and \NewCount contains the number of
items in the list. Note that \NewValue as well as the single argument to hcodei
containtheinternalrepresentationofthelist.
190

\DeclareNameInputHandler{hnamei}{hcodei}
As \DeclareFieldInputHandler but for names. Within the hcodei, the macro
\NewValuecontainsthevalueofthename,\NewCountcontainsthenumberofindi-
vidualnamesinthenameand\NewOptioncontainsanyper-nameoptionspassedin
the.bbl. Notethat\NewValueaswellasthesingleargumenttohcodeicontainthe
internalrepresentationofthenamelist.
4.4.2 FormattingDirectives
Thissectionintroducesthecommandsusedtodefinetheformattingdirectivesre-
quiredbythedatacommandsfrom§4.4.1. Notethatallstandardformatsaredefined
inbiblatex.def.
\DeclareFieldFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareFieldFormat*{hformati}{hcodei}
Definesthefieldformathformati. Thisformattingdirectiveisarbitraryhcodeitobe
executedby\printfield. Thevalueofthefieldwillbepassedtothehcodeiasits
firstandonlyargument. Thenameofthefieldcurrentlybeingprocessedisavailable
tothehcodeias\currentfield. Ifanhentrytypeiisspecified,theformatisspecific
to that type. The hentrytypei argument may be a comma-separated list of values.
Thestarredvariantofthiscommandissimilartotheregularversion,exceptthatall
type-specificformatsarecleared.
\DeclareListFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareListFormat*{hformati}{hcodei}
Definestheliterallistformathformati. Thisformattingdirectiveisarbitraryhcodei
tobeexecutedforeveryiteminalistprocessedby\printlist. Thecurrentitem
willbepassedtothehcodeiasitsfirstandonlyargument. Thenameoftheliteral
list currently being processed is available to the hcodei as \currentlist. If an
hentrytypeiisspecified,theformatisspecifictothattype. Thehentrytypeiargument
may be a comma-separated list of values. Note that the formatting directive also
handlesthepunctuationtobeinsertedbetweentheindividualitemsinthelist. You
needtocheckwhetheryouareinthemiddleoforattheendofthelist,i.e.,whether
listcountissmallerthanorequaltoliststop. Thestarredvariantofthiscommand
issimilartotheregularversion,exceptthatalltype-specificformatsarecleared.
\DeclareNameFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareNameFormat*{hformati}{hcodei}
Definesthenamelistformathformati. Thisformattingdirectiveisarbitraryhcodei
tobeexecutedforeverynameinalistprocessedby\printnames. Ifanhentrytypei
isspecified,theformatisspecifictothattype. Thehentrytypeiargumentmaybea
comma-separatedlistofvalues. Theindividualpartsofanamewillbeavailablein
automaticallycreatedmacros(seebelow). Thedefaultdatamodedefinesfourname
partwhichcorrespondtothestandardBibTeXnamepartsarguments:
family Thefamilyname(s),knowas‘last’inBibTeX.Ifanameconsistsofasingle
partonly(forexample,‘Aristotle’),thispartwillbetreatedasthefamilyname.
given Thegivenname(s). Notethatgivennamesarereferredtoasthe‘first’names
intheBibTeXfileformatdocumentation.
191

prefix Anynameprefices,forexamplevon,van,of,da,de,del,della,etc. Note
thatnamepreficesarereferredtoasthe‘von’partofthenameintheBibTeX
fileformatdocumentation.
suffix Anynamesuffices,forexampleJr,Sr. Notethatnamesufficesarereferred
toasthe‘Jr’partofthenameintheBibTeXfileformatdocumentation.
Thevalueofthedatamodel‘nameparts’constant(see§4.2.3)createstwomacrosfor
eachnamepartinthedatamodelforthename. So,forexample,inthedefaultdata
model,nameformatswillhavedefinedthefollowingmacros:
\namepartprefix
\namepartprefixi
\namepartfamily
\namepartfamilyi
\namepartsuffix
\namepartsuffixi
\namepartgiven
\namepartgiveni
Ifacertainpartofanameisnotavailable,thecorrespondingmacrowillbeempty,
hence you may use, for example, the etoolbox tests like \ifdefvoid to check for
theindividualpartsofaname. Thenameofthenamelistcurrentlybeingprocessed
isavailabletothehcodeias\currentname. Notethattheformattingdirectivealso
handlesthepunctuationtobeinsertedbetweenseparatenamesandbetweenthe
individualpartsofaname. Youneedtocheckwhetheryouareinthemiddleoforat
theendofthelist,i.e.,whetherlistcountissmallerthanorequaltoliststop. See
also§3.15.4. Thestarredvariantofthiscommandissimilartotheregularversion,
exceptthatalltype-specificformatsarecleared.
\DeclareListWrapperFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareListWrapperFormat*{hformati}{hcodei}
Definesthelistwrapperformathformati. Thisformattingdirectiveisarbitraryhcodei
to be executed once for the entirelist processed by \printlist. The name of the
literallistcurrentlybeingprocessedisavailabletothehcodeias\currentlist. Ifan
hentrytypeiisspecified,theformatisspecifictothattype. Thehentrytypeiargument
maybeacomma-separatedlistofvalues. Thestarredvariantofthiscommandis
similartotheregularversion,exceptthatalltype-specificformatsarecleared.
\DeclareNameWrapperFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareNameWrapperFormat*{hformati}{hcodei}
Definesthelistwrapperformathformati. Thisformattingdirectiveisarbitraryhcodei
tobeexecutedoncefortheentirenamelistprocessedby\printnames. Thenameof
theliterallistcurrentlybeingprocessedisavailabletothehcodeias\currentname.
If an hentrytypei is specified, the format is specific to that type. The hentrytypei
argument may be a comma-separated list of values. The starred variant of this
commandissimilartotheregularversion,exceptthatalltype-specificformatsare
cleared.
192

\DeclareIndexFieldFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareIndexFieldFormat*{hformati}{hcodei}
Defines the field format hformati. This formatting directive is arbitrary hcodei to
be executed by \indexfield. The value of the field will be passed to the hcodei
asitsfirstandonlyargument. Thenameofthefieldcurrentlybeingprocessedis
availabletothehcodeias\currentfield. Ifanhentrytypeiisspecified,theformat
isspecifictothattype. Thehentrytypeiargumentmaybeacomma-separatedlist
of values. This command is similar to \DeclareFieldFormat except that the data
handledbythehcodeiisnotintendedtobeprintedbutwrittentotheindex. Note
that\indexfieldwillexecutethehcodeiasis,i.e.,thehcodeimustinclude\index
orasimilarcommand. Thestarredvariantofthiscommandissimilartotheregular
version,exceptthatalltype-specificformatsarecleared.
\DeclareIndexListFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareIndexListFormat*{hformati}{hcodei}
Definestheliterallistformathformati. Thisformattingdirectiveisarbitraryhcodei
tobeexecutedforeveryiteminalistprocessedby\indexlist. Thecurrentitem
willbepassedtothehcodeiasitsonlyargument. Thenameoftheliterallistcurrently
being processed is available to the hcodei as \currentlist. If an hentrytypei is
specified, the format is specific to that type. The hentrytypei argument may be a
comma-separatedlistofvalues. Thiscommandissimilarto\DeclareListFormat
exceptthatthedatahandledbythehcodeiisnotintendedtobeprintedbutwritten
totheindex. Notethat\indexlistwillexecutethehcodeiasis,i.e.,thehcodeimust
include\indexorasimilarcommand. Thestarredvariantofthiscommandissimilar
totheregularversion,exceptthatalltype-specificformatsarecleared.
\DeclareIndexNameFormat[hentrytype,…i]{hformati}{hcodei}
\DeclareIndexNameFormat*{hformati}{hcodei}
Definesthenamelistformathformati. Thisformattingdirectiveisarbitraryhcodei
tobeexecutedforeverynameinalistprocessedby\indexnames. Thenameofthe
namelistcurrentlybeingprocessedisavailabletothehcodeias\currentname. Ifan
hentrytypeiisspecified,theformatisspecifictothattype. Thehentrytypeiargument
maybeacomma-separatedlistofvalues. Thepartsofthenamewillbepassedtothe
hcodeiasseparatearguments. Thiscommandisverysimilarto\DeclareNameFormat
exceptthatthedatahandledbythehcodeiisnotintendedtobeprintedbutwritten
to the index. Note that \indexnames will execute the hcodei as is, i.e., the hcodei
mustinclude\indexorasimilarcommand. Thestarredvariantofthiscommandis
similartotheregularversion,exceptthatalltype-specificformatsarecleared.
\DeclareFieldAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declares haliasi to be an alias for the field format hformati. If an hentrytypei is
specified,thealiasisspecifictothattype. Thehformatentrytypeiistheentrytype
of the backend format. This is only required when declaring an alias for a type-
specificformattingdirective.
\DeclareListAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasfortheliterallistformathformati. Ifanhentrytypei
is specified, the alias is specific to that type. The hformatentrytypei is the entry
typeofthebackendformat. Thisisonlyrequiredwhendeclaringanaliasforatype-
specificformattingdirective.
193

\DeclareNameAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasforthenamelistformathformati. Ifanhentrytypei
is specified, the alias is specific to that type. The hformatentrytypei is the entry
typeofthebackendformat. Thisisonlyrequiredwhendeclaringanaliasforatype-
specificformattingdirective.
\DeclareListWrapperAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasfortheouterlistformathformati. Ifanhentrytypei
is specified, the alias is specific to that type. The hformatentrytypei is the entry
typeofthebackendformat. Thisisonlyrequiredwhendeclaringanaliasforatype-
specificformattingdirective.
\DeclareNameWrapperAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declares haliasi to be an alias for the outer name list format hformati. If an
hentrytypei is specified, the alias is specific to that type. The hformatentrytypei
is the entry type of the backend format. This is only required when declaring an
aliasforatype-specificformattingdirective.
\DeclareIndexFieldAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declares haliasi to be an alias for the field format hformati. If an hentrytypei is
specified,thealiasisspecifictothattype. Thehformatentrytypeiistheentrytype
of the backend format. This is only required when declaring an alias for a type-
specificformattingdirective.
\DeclareIndexListAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasfortheliterallistformathformati. Ifanhentrytypei
is specified, the alias is specific to that type. The hformatentrytypei is the entry
typeofthebackendformat. Thisisonlyrequiredwhendeclaringanaliasforatype-
specificformattingdirective.
\DeclareIndexNameAlias[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasforthenamelistformathformati. Ifanhentrytypei
is specified, the alias is specific to that type. The hformatentrytypei is the entry
typeofthebackendformat. Thisisonlyrequiredwhendeclaringanaliasforatype-
specificformattingdirective.
\DeprecateFieldFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Declareshaliasitobeanaliasforthenamelistformathformatiandissueadepre-
cationwarning. Ifanhentrytypeiisspecified,thealiasisspecifictothattype. The
hformatentrytypei isthe entry type of the backend format. This is only required
whendeclaringanaliasforatype-specificformattingdirective.
\DeprecateListFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforlistformats.
\DeprecateNameFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutfornameformats.
194

\DeprecateListWrapperFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforouterlistformats.
\DeprecateNameWrapperFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforouternameformats.
\DeprecateIndexFieldFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforindexfieldformats.
\DeprecateIndexListFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforindexlistformats.
\DeprecateIndexNameFormatWithReplacement[hentrytypei]{haliasi}[hformatentrytypei]{hformati}
Similarto\DeprecateFieldFormatWithReplacementbutforindexnameformats.
4.5 Customization
4.5.1 RelatedEntries
Therelatedentriesfeaturecomprisesthefollowingcomponents:
• Specialfieldsinanentrytosetupanddescriberelationships
• Optionally,localisationstringstoprefixtherelateddata
• Macrostoextractandprinttherelateddata
• Formatstoformatthelocalisationstringandrelateddata
Thespecialfieldsarerelated,relatedtype,relatedstringandrelatedoptions:
related Aseparatedlistofkeysofentrieswhicharerelatedtothisentryinsomeway. Note
theorderofthekeysisimportant. Thedatafrommultiplerelatedentriesisprinted
intheorderofthekeyslistedinthisfield.
relatedtype Thetypeofrelationship. Thisservesthreepurposes. Ifthevalueofthisfield
resolvestoalocalisationstringidentifier,thentheresultinglocalisedstringis
printedbeforethedatafromtherelatedentries. Secondly,ifthereisamacrocalled
related:hrelatedtypei,thisisusedtoformatthedatafromtherelatedentries. Ifno
suchmacroexists,thenthemacrorelated:defaultisused. Lastly,ifthereisa
formatnamedrelated:hrelatedtypei,thenitisusedtoformatboththelocalised
stringandrelatedentrydata. Ifthereisnorelatedtypespecificformat,therelated
formatisused.
relatedstring Ifanentrycontainsthisfield,thenifvalueofthefieldresolvestoalocalisation
stringidentifier,thelocalisationkeyvaluespecifiedisprintedbeforedatafromthe
relatedentries. Ifthefielddoesnotspecifyalocalisationkey,itsvalueisprinted
literally. Ifbothrelatedtypeandrelatedstringarepresentinanentry,
relatedstringisusedforthepre-datastring(butrelatedtypeisstillusedto
determinethemacroandformattousewhenprintingthedata).
relatedoptions Alistofper-entryoptionstosetontherelatedentry(actuallyonthecloneofthe
relatedentrywhichisusedasadatasource—theactualrelatedentryisnotmodified
becauseitmightbeciteddirectlyitself).
195

The related entry feature is enabled by default by the package option related
from§3.1.2.1. Therelatedinformationentrydatafromtherelatedentriesisincluded
via a \usebibmacro{related} call. Standard styles call this macro towards the
end of each driver. Style authors should ensure the existence of (or take note of
existing)localisationstringswhichareusefulasvaluesfortherelatedtypefield,
suchastranslationoforperhapstranslationas. Apluralvariantcanbeidentified
withthelocalisationkeyhrelatedtypeis. Thiskey’scorrespondingstringisprinted
whenever more than one entry is specified in related. Bibliography macros and
formattingdirectivesforprintingentriesrelatedbyhrelatedtypeishouldbedefined
usingthenamerelated:hrelatedtypei. Thefilebiblatex.defcontainsmacrosand
formatsforsomecommonrelationtypeswhichcanbeusedastemplates. Inparticular,
the\entrydata*commandisessentialinsuchmacrosinordertomakethedataof
therelatedentriesavailable. Examplesofentriesusingthisfeaturecanbefoundin
the biblatex distribution examples file biblatex-examples.bib. There are some
specificformattingmacrosforthisfeaturewhichcontroldelimitersandseparators
inrelatedentryinformation,see§4.10.1.
4.5.2 DatasourceSets
Itisusefultobeabletodefinenamedsetsofdatasourcefieldnamesforuseinloops
etc. In addition, biber can use such sets in order to apply options and perform
operationsonparticularsetsofdatasourcefields. Thefollowingmacrosallowthe
usertodefinearbitrarysetsofdatasourcefields,exposedtobiblatexasetoolbox
listsandtobiberinthe.bcf.
\DeclareDatafieldSet{hnamei}{hspecificationi}
Declareasetofdatasourcefieldswithnamehnamei.
name=hsetnamei
Thenameoftheset.
Thehspecificationiisoneormore\memberitems:
\member
fieldtype=hfieldtypei
datatype=hdatatypei
field=hfieldnamei
A\memberspecificationappendsfieldstotheset. Fieldscanbespecifiedbydatamodel
hfieldtypeiand/orhdatatypei(see§4.5.4). Alternatively,fieldscanbeexplicitlyadded
bynameusingthehfieldioption. Oncedefined,thesetisavailableasanetoolbox
listcalled\datafieldset‘setname’andisalsopassedviathe.bcftobiber.
Forexample,herearethedefaultsetsdefinedbybiblatexfornamefieldsandtitle
fields:
\DeclareDatafieldSet{setnames}{
\member[datatype=name, fieldtype=list]
}
\DeclareDatafieldSet{settitles}{
196

\member[field=title]
\member[field=booktitle]
\member[field=eventtitle]
\member[field=issuetitle]
\member[field=journaltitle]
\member[field=maintitle]
\member[field=origtitle]
}
Thisdefinesthemacros\datafieldsetsetnamesand\datafieldsetsettitlesas
etoolboxlistscontainingthenamesofthememberdatasourcefieldsspecified.
4.5.3 DynamicModificationofData
Bibliographicdatasourceswhichareautomaticallygeneratedorwhichyouhaveno
controlovercanbeaproblemifyouneedtoedittheminsomeway. Forthisreason,
biberhastheabilitytomodifydataasitisreadsothatyoucanapplymodifications
to the source data stream without actually changing it. The modification can be
definedinbiber’sconfigfile(seebiberdocs),orviabiblatexmacrosinwhichcase
youcanapplythemodificationonlyforspecificdocuments,stylesorglobally.
Source mapping happens during data parsing and therefore before any other
operationsuchasinheritanceandsorting.
Sourcemappingscanbedefinedatdifferent“levels”whichareappliedinadefined
order. Seethebiblatexmanualregardingthesemacros:
user-levelmapsdefinedwith\DeclareSourcemap→
user-levelmapsdefinedinthebiberconfigfile(seebiberdocs)→
style-levelmapsdefinedwith\DeclareStyleSourcemap→
driver-levelmapsdefinedwith\DeclareDriverSourcemap
\DeclareSourcemap{hspecificationi}
Definessourcedatamodification(mapping)ruleswhichcanbeusedtoperformany
combinationofthefollowingtasks:
• Mapdatasourceentrytypestodifferententrytypes
• Mapdatasourcefieldstodifferentfields
• Addnewfieldstoanentry
• Removefieldsfromanentry
• Modifythe contents of afield using standardPerl regularexpressionmatch
andreplace35
• Restrict any of the above operations to entries coming from particular data-
sourceswhichyoudefinedin\addresourcemacros
• Restrictanyoftheaboveoperationstoentriesonlyofacertainentrytype
• Restrictanyoftheaboveoperationstoentriesinaparticularreferencesection
35See for example https://perldoc.perl.org/perlretut.html, https://perldoc.perl.org/
perlrequick.htmlandhttps://perldoc.perl.org/perlre.html.Therearemanymoreresources
availableaboutregularexpessionsinPerl.
197

Thehspecificationiisanundelimitedlistof\mapsdirectiveswhichspecifycontainers
formappingsrulesapplyingtoaparticulardatasourcetype(§3.8.1). Spaces,tabs,
andlineendingsmaybeusedfreelytovisuallyarrangethehspecificationi. Blank
linesarenotpermissible. Thiscommandmayonlybeusedinthepreambleandcan
beusedmultipletimes,themapsbeingruninorderofdefinition.
\maps[hoptionsi]{helementsi}
Containsanorderedsetof\mapelementseachofwhichisalogicallyrelatedsetof
mappingstepstoapplytothedatasource. Thehoptionsiare:
datatype=bibtex,biblatexml default:bibtex
Datasourcetypetowhichthecontained\mapdirectivesapply(§3.8.1).
overwrite=true,false default:false
Specifywhetheramappingruleisallowedtooverwritealreadyexistingdatainan
entry. Ifthisoptionisnotspecified,thedefaultisfalse. Theshortformoverwrite
isequivalenttooverwrite=true.
\map[hoptionsi]{hrestrictions,stepsi}
A container for an ordered set of map \steps, optionally restricted to particular
entrytypes or data sources. This is a grouping element to allow a set of mapping
stepstoapplyonlytospecificentrytypesordatasources. Mappingstepsmustalways
becontainedwithina\mapelement. Thehoptionsiare:
overwrite=true,false
Asthesameoptionontheparent\mapselement. Thisoptionallowsanoverrideon
aper-mapgroupbasis. Ifthisoptionisnotspecified,thedefaultistheparent\maps
elementoptionvalue. Theshortformoverwriteisequivalenttooverwrite=true.
foreach=hloopvali
Loopoverall\stepsinthis\map,settingthespecialvariable$MAPLOOPtoeachofthe
comma-separatedvaluescontainedinhloopvali. hloopvalicaneitherbethenameof
adatafieldsetdefinedwith\DeclareDatafieldSet(see§4.5.2),adatasourcefield
whichisfetchedandparsedasacomma-separatedvalueslistoranexplicitcomma-
separatedvalueslist. hloopvaliisdeterminedinthisorder. Thisallowstheuserto
repeatagroupof\stepsforeachvaluehloopvali. Usingregexpmaps,itispossible
tocreateaCSVfieldforusewiththisfunctionality. Thespecialvariable$MAPUNIQ
may also be used in the \steps to generate a random unique string. This can be
usefulwhencreatingkeysfornewentries. Anexample:
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map[overwrite, foreach={author,editor, translator}]{
\step[fieldsource=\regexp{$MAPLOOP}, match={Smith}, replace={
,→ Jones}]
}
}
}
refsection=hintegeri
Onlyapplythecontained\stepcommandstoentriesinthereferencesectionwith
numberhrefsectioni.
198

\perdatasource{hdatasourcei}
Restrictsall\stepsinthis\mapelementtoentriesfromthenamedhdatasourcei. The
hdatasourceinameshouldbeexactlyasgivenina\addresourcemacrodefininga
data source for the document. Multiple \perdatasource restrictions are allowed
withina\mapelement.
\pertype{hentrytypei}
Restrictsall\stepsinthis\mapelementtoentriesofthenamedhentrytypei. Multiple
\pertyperestrictionsareallowedwithina\mapelement.
\pernottype{hentrytypei}
Restricts all \steps in this \map element to entries not of the named hentrytypei.
Multiple\pernottyperestrictionsareallowedwithina\mapelement.
\step[hoptionsi]
A mapping step. Each step is applied sequentially to every relevant entry where
‘relevant’meansthoseentrieswhichcorrespondtothedatasourcetype,entrytype
anddatasourcenamerestrictionsmentionedabove. Eachstepisappliedtotheentry
asitappearsaftertheapplicationofallprevioussteps. Themappingperformedby
thestepisdeterminedbythefollowinghoptionis:
typesource=hentrytypei
typetarget=hentrytypei
fieldsource=hentryfieldi
notfield=hentryfieldi
fieldtarget=hentryfieldi
match=hregexpi
matchi=hregexpi
notmatch=hregexpi
notmatchi=hregexpi
matches=hregexpi
matchesi=hregexpi
replace=hregexpi
fieldset=hentryfieldi
fieldvalue=hstringi
entryclone=hclonekeyi
entrynew=hentrynewkeyi
entrynewtype=hstringi
entrytarget=hstringi
cited=true,false default:false
nocited=true,false default:false
citedornocited=true,false default:false
allnocited=true,false default:false
199

starnocited=true,false default:false
entrynocite=true,false default:false
entrynull=true,false default:false
append=true,false default:false
appendstrict=true,false default:false
final=true,false default:false
null=true,false default:false
origfield=true,false default:false
origfieldval=true,false default:false
origentrytype=true,false default:false
Forallboolean\stepoptions,theshortformoptionisequivalenttooption=true.
Thefollowingrulesforamappingstepapply:
Note that the options cited, nocited, citedornocited, allnocited and
starnocited are unique in that they can make the results of a sourcemap differ
dependingontherefsection. Thisisbecauseadatasourcetowhichsourcemapping
appliesmaybeusedinseveralrefsectionsandsourcemappingsareappliedwhen
fetching the data from the datasources for a refsection. Citation commands are
local to a refsection and therefore may differ for the same entry from refsection
to refsection. For example, the same entry may be \cited in one refsection but
\nocited in another, resulting in different source map results and therefore data
betweentherefsections. Thiscanbeavoidedifdesired,bylimitingsourcemapsto
specificrefsectionsonly(seerefsectionoptiontothe\mapcommandabove).
• Iffinalistrueforastepthennomorestepsafterthisonearerunwithinthe
currentmapforthecurrententryiftheconditionsforthestepsofararenot
satisfied. Examplesaregiveninthedescriptionsforspecificstepsastowhat
thismeansfortheirparticularsemantics.
• Ifentrynewisset,anewentryiscreatedwiththeentrykeyentrynewkeyandthe
entrytypegivenintheoptionentrynewtype. Thisentryisonlyin-scopeduring
theprocessingofthecurrententryandcanbereferencedbyentrytarget. In
entrynewkey,youmayusestandardPerlregularexpressionbackreferencesto
capturesfromapreviousmatchstep.
• Whenafieldsetstephasentrytargetsettotheentrykeyofanentrycreated
by entrynew, the target forthe field setwill bethe entrytargetentryrather
thantheentrybeingcurrentlyprocessed. Thisallowsuserstocreatenewentries
andsetfieldsinthem.
• Ifentrynociteisusedinaentryneworentryclonestep,thenew/cloneentry
will be included in the .bbl as if the entry/clone had been \nociteed in the
document.
• If entrynull is set, processing of the \map immediately terminates and the
currententryisnotcreated. Itisasifitdidnotexistinthedatasource. Obviously,
youshouldselecttheentrieswhichyouwanttoapplythistousingpriormapping
steps.
• Ifentrycloneisset,acloneoftheentryiscreatedwithanentrykeyclonekey.
Obviously this may cause labelling problems in author/year styles etc. and
should be used with care. The cloned entry is in-scope during the process-
ing of the current entry and can be modified by passing its key as the value
200

to entrytarget. In clonekey, you may use standard Perl regular expression
backreferencestocapturesfromapreviousmatchstep.
• If cited is used then only apply the step if the entry key of an entry was
specificallycitedvia\cite.
• If nocited is used then only apply the step if the entry key of an entry was
specificallynocitedvia\nociteorwasincludedvia\nocite{*}.
• Ifcitedornocitedisusedthenonlyapplythestepiftheentrykeyofanentry
wasspecificallycitedvia\citeorspecificallynocitedvia\nocite.
• Ifallnocitedisusedthenonlyapplythestepiftheentrykeyofanentrywas
includedvia\nocite{*}.
• Ifstarnocitedisusedthenonlyapplythestepiftheentrykeyofanentrywas
includedsolelybecauseof\nocite{*}. Thisimpliesthattheentrywasneither
explicitly\citeednorexplicitly\nociteed.
• Changethetypesourcehentrytypeitothetypetargethentrytypei,ifdefined. If
finalistruethenifthehentrytypeioftheentryisnottypesource,processing
oftheparent\mapimmediatelyterminates.
• Change the fieldsource hentryfieldi to fieldtarget, if defined. If final is
truethenifthereisnofieldsourcehentryfieldiintheentry,processingofthe
parent\mapimmediatelyterminates.
• If notfield is true only if the hentryfieldi does not exist. Usually used with
finalsothatifanentrydoescontainhentryfieldi,themapterminates.
• Ifmatchisdefinedbutreplaceisnot,onlyapplythestepifthefieldsource
hentryfieldimatchesthematchregularexpression(logicisreversedifyouuse
notmatchandcase-insensitiveifyouusetheversionsendingin‘i’)36. Youmay
usecaptureparenthesisasusualandrefertothese($1…$9)inlaterfieldvalue
specifications. This allows you to pull out parts of some fields and put these
partsinotherfields.
• Performaregularexpressionmatchandreplaceonthevalueofthefieldsource
hentryfieldiifmatchandreplacearedefined.
• Ifmatchesisdefined,itshouldbeacomma-separatedlistofliteralstringswhich
arereplacedbycorrespondinglocationsinacomma-separatedlistprovidedin
replace. Thelistsmusthavethesamenumberofelementsorthestepwillbe
skipped. matchesiisthesamebutcase-insensitive.
• Iffieldsetisdefined,thenitsvalueishentryfieldiwhichwillbesettoavalue
specifiedbyfurtheroptions. Ifoverwriteisfalseforthisstepandthefieldto
setalreadyexiststhenthemapstepisignoredandiffinalisalsotrue, then
processing of the parent map stops at this point. If append is true, then the
valuetosetisappendedtothecurrentvalueofhentryfieldi. appendstrictonly
appendstohentryfieldiifhentryfieldiisnotempty. Thevaluetosetisspecified
byamandatoryoneandonlyoneofthefollowingoptions:
◦ fieldvalue—Thefieldsethentryfieldiissettothefieldvaluehstringi
◦ null — The fieldset hentryfieldi is ignored, as if it did not exist in the
datasource
◦ origentrytype — The fieldset hentryfieldi is set to the most recently
mentionedtypesourcehentrytypeiname
36RegularexpressionsarefullPerl5.16regularexpressions.Thismeansyoumayneedtodealwith
specialcharacters,seeexamples.
201

◦ origfield — The fieldset hentryfieldi is set to the most recently men-
tionedfieldsourcehentryfieldiname
◦ origfieldval—Thefieldsethentryfieldiissettothemostrecentlymen-
tionedfieldsourcevalue
With BibTeX datasources, you may specify the pseudo-field entrykey for
fieldsourcewhichisthecitationkeyoftheentry. Withbiblatexmltheentrykeyis
anormalattributeandcanbereferencelikeanyotherattribute. Naturally,this‘field’
cannotbechanged(usedasfieldset,fieldtargetorchangedusingreplace).
Macrosusedin\stepareexpanded. Unexpandablecontentsshouldbeprotected
with\detokenize,regularexpressionscanbeescapedusingthededicated\regexp
command(seetheexamplesbelow).
\DeclareStyleSourcemap{hspecificationi}
Thiscommandsetsthesourcemappingsusedbyastyle. Suchmappingsareconceptu-
allyseparatefromusermappingsdefinedwith\DeclareSourcemapandareapplieddi-
rectlyafterusermaps. Thesyntaxisidenticalto\DeclareSourcemap. Thiscommand
isprovidedforstyleauthorssothatanymapsdefinedforthestyledonotinterfere
withusermapsorthedefaultdrivermapsdefinedwith\DeclareDriverSourcemap.
Thiscommandisforuseinstylefilesandcanbeusedmultipletimes,themapsbeing
runinorderofdefinition.
\DeclareDriverSourcemap[hdatatype=driveri]{hspecificationi}
This command sets the driver default source mappings for the specified hdriveri.
Such mappings are conceptually separate from user mappings defined with
\DeclareSourcemap and style mapping defined with \DeclareStyleSourcemap.
They consist of mappings which are part of the driver setup. Users should not
normallyneedtochangethese. Driverdefaultmappingareappliedafterusermap-
pings(\DeclareSourcemap)andstylemappings(\DeclareStyleSourcemap). These
defaults are described in Appendix § A. The hspecificationi is identical to that for
\DeclareSourcemapbutwithoutthe\mapselements: thehspecificationiisjustalist
of\mapelementssinceeach\DeclareDriverSourcemaponlyappliestoonedatatype
driver. SeethedefaultdefinitionsinAppendix§Aforexamples.
\regexp{hPCREi}
Thiscommandcanbeusedwithanycommandacceptingaregularexpressionkeyto
protectaregularexpressionfrombeinginterpretedbyTEXsothatitispassedthrough
tobibercorrectly. Regularexpressionsoftencontainsequencesofcharactersthat
are also valid TEX commands but which should not be interpreted as such. The
argument is a normal PCRE (Perl Compatible Regular Expression37). Perl escape
sequenceslike\tforatab,\nforanewline,\Aforthestartofastringor\dfora
digitcanbeused,withoutTEXtryingtoexecutethemascommands,ascanbespecial
characterslike^,_or{..}and#. Onlythe%mustbeprotected: tomatchasingle%
inthebib,use\%intheregularexpression,a\%ismatchedby\\%.
Herearesomedatasourcemappingexamples:
37https://perldoc.perl.org/perlre
202

\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\perdatasource{example1.bib}
\perdatasource{example2.bib}
\step[fieldset=keywords, fieldvalue={keyw1, keyw2}]
\step[fieldsource=entrykey]
\step[fieldset=note, origfieldval]
}
}
}
Thiswouldaddakeywordsfieldwithvalue‘keyw1,keyw2’andsetthenotefield
to the entry key to all entries which are found in either the examples1.bib or
examples2.bibfiles.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=title]
\step[fieldset=note, origfieldval]
}
}
}
Copythetitlefieldtothenotefieldunlessthenotefieldalreadyexists.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[typesource=chat, typetarget=customa, final]
\step[fieldset=type, origentrytype]
}
}
}
Anychatentrytypeswouldbecomecustomaentrytypesandwouldautomatically
haveatypefieldsetto‘chat’unlessthetypefieldalreadyexistsintheentry(because
overwriteisfalsebydefault). Thismappingappliesonlytoentriesoftype@chat
sincethefirststephasfinalsetandsoifthetypesourcedoesnotmatchtheentry
entrytype,processingofthis\mapimmediatelyterminates.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\perdatasource{examples.bib}
\pertype{article}
\pertype{book}
\step[fieldset=abstract, null]
\step[fieldset=note, fieldvalue={Auto-created this field}]
203

}
}
}
Any entries of entrytype @article or @book from the examples.bib datasource
wouldhavetheirabstractfieldsremovedandanotefieldaddedwithvalue‘Auto-
createdthisfield’.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldset=abstract, null]
\step[fieldsource=conductor, fieldtarget=namea]
\step[fieldsource=gps, fieldtarget=usera]
}
}
}
This removes abstract fields from any entry, changes conductor fields to namea
fieldsandchangesgpsfieldstouserafields.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=pubmedid, fieldtarget=eprint, final]
\step[fieldset=eprinttype, origfield]
\step[fieldset=userd, fieldvalue={Some string of things}]
}
}
}
Appliesonlytoentrieswithpubmedfieldsandmapspubmedidfieldstoeprintfields,
setstheeprinttypefieldto‘pubmedid’andalsosets theuserdfieldtothestring
‘Somestringofthings’.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=series,
match=\regexp{\A\d*(.+)},
replace=\regexp{\L$1}]
}
}
}
Here,thecontentsoftheseriesfieldhaveleadingnumbersstrippedandtheremain-
derofthecontentslowercased. Sinceregularexpressionsusuallycontainallsort
of special characters, it is best to enclose them in the provided \regexp macro as
shown—thiswillpasstheexpressionthroughtobibercorrectly.
204

\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=maintitle,
match=\regexp{Collected\s+Works.+Freud},
final]
\step[fieldset=keywords, fieldvalue=freud]
}
}
}
Here, if for an entry, the maintitle field matches a particular regular expression,
wesetaspecialkeywordsowecan,forexample,makeareferencessectionjustfor
certainitems.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=lista, match=\regexp{regexp}, final]
\step[fieldset=lista, null]
}
}
}
Ifanentryhasalistafieldwhichmatchesregularexpression‘regexp’,thenitis
removed.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map[overwrite=false]{
\step[fieldsource=author]
\step[fieldset=editor, origfieldval, final]
\step[fieldsource=editor, match=\regexp{\A(.+?)\s+and.*},
,→ replace={$1}]
}
}
}
Foranyentrywithanauthorfield,trytoseteditortothesameasauthor. Ifthis
failsbecauseeditoralreadyexists,stop,otherwisetruncateeditortojustthefirst
nameinthenamelist.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=author,
match={Smith, Bill},
replace={Smith, William}]
\step[fieldsource=author,
match={Jones, Baz},
205

replace={Jones, Barry}]
}
}
}
Here,weusemultiplematch/replaceforthesamefieldtoregularisesomeinconstant
namevariants. Bearinmindthat\stepprocessingwithinamapelementissequential
and so the changes from a previous \steps are already committed. Note that we
don’t need the \regexp macro to protect the regular expressions in this example
astheycontainnocharacterswhichneedspecialescaping. Pleasenotethatdueto
thedifficultyofprotectingregularexpressionsinLaTeX,thereshouldbenoliteral
spacesintheargumentto\regexp. Pleaseuseescapecodeequivalentsifspacesare
needed. Forexample,thisexample,ifusing\regexp,shouldbe:
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=author,
match=\regexp{Smith,\s+Bill},
replace=\regexp{Smith,\x20William}]
\step[fieldsource=author,
match=\regexp{Jones,\s+Baz},
replace=\regexp{Jones,\x20Barry}]
}
}
}
Here,wehaveusedthehexadecimalescapesequence‘\x20’inplaceofliteralspaces
inthereplacementstrings.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map[overwrite]{
\step[fieldsource=author, match={Doe,}, final]
\step[fieldset=shortauthor, origfieldval]
\step[fieldset=sortname, origfieldval]
\step[fieldsource=shortauthor,
match=\regexp{Doe,\s*(?:\.|ohn)(?:[-]*)(?:P\.|Paul)*},
replace={Doe, John Paul}]
\step[fieldsource=sortname,
match=\regexp{Doe,\s*(?:\.|ohn)(?:[-]*)(?:P\.|Paul)*},
replace={Doe, John Paul}]
}
}
}
Onlyappliestoentrieswithanauthorfieldmatching‘Doe,’. Firsttheauthorfield
is copied to both the shortauthor and sortname fields, overwriting them if they
alreadyexist. Then,thesetwonewfieldsaremodifiedtocanonicaliseaparticular
name,whichpresumablyhassomevariantsinthedatasource.
206

\DeclareSourcemap{
\maps[datatype=bibtex]{
\map[overwrite]{
| \step[fieldsource=verba, | final]        |         |     |
| ------------------------ | ------------- | ------- | --- |
| \step[fieldset=verbb,    | fieldvalue=/, | append] |     |
| \step[fieldset=verbb,    | origfieldval, | append] |     |
| \step[fieldsource=verbb, | final]        |         |     |
| \step[fieldset=verbc,    | fieldvalue=/, | append] |     |
| \step[fieldset=verbc,    | origfieldval, | append] |     |
}
}
}
This example demonstrates the sequential nature of the step processing and the
appendoption. Ifanentryhasaverbafieldthenfirst,aforwardslashisappended
totheverbbfield. Then,thecontentsofverbaareappendedtotheverbbfield. A
slashisthenappendedtotheverbcfieldandthecontentsofverbbareappendedto
theverbcfield.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map[overwrite]{
| \step[fieldset=autourl, | fieldvalue={http://scholar.google.com/ |     |     |
| ----------------------- | -------------------------------------- | --- | --- |
,→ scholar?q="}]
\step[fieldsource=title]
| \step[fieldset=autourl,   | origfieldval,                 | append] |         |
| ------------------------- | ----------------------------- | ------- | ------- |
| \step[fieldset=autourl,   | fieldvalue={"+author:},       |         | append] |
| \step[fieldsource=author, | match=\regexp{\A([^,]+)\s*,}] |         |         |
| \step[fieldset=autourl,   | fieldvalue={$1},              | append] |         |
| \step[fieldset=autourl,   | fieldvalue={&as_ylo=},        |         | append] |
\step[fieldsource=year]
| \step[fieldset=autourl, | origfieldval,          | append] |         |
| ----------------------- | ---------------------- | ------- | ------- |
| \step[fieldset=autourl, | fieldvalue={&as_yhi=}, |         | append] |
| \step[fieldset=autourl, | origfieldval,          | append] |         |
}
}
}
Thisexampleassumesyouhavecreatedafieldcalledautourlusingthedatamodel
macrosfrom§4.5.4inordertohold,forexample,aGoogleScholarqueryURLauto-
createdfromelementsoftheentry. Theexampleprogressivelyextractsinformation
fromtheentry,constructingtheURLasitgoes. Itdemonstratesthatitispossible
to refer to parenthetical matches from the most recent match in any following
fieldvaluewhichallowsextractingthefamilynamefromtheauthor,assuminga
‘family,given’format. Theresultingfieldcouldthenbeusedasahyperlinkfrom,for
example,thetitleoftheworkinthebibliography.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
207

\step[fieldsource=title, match={A Title}, final]
\step[entrynull]
}
}
}
Anyentrywithatitlefieldmatching‘ATitle’willbecompletelyignored.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\pernottype{book}
\pernottype{article}
\step[entrynull]
}
}
}
Anyentrywhichisnota@bookor@articlewillbeignored.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\perdatasource{biblatex-examples.bib}
\step[entryclone={rel-}]
}
}
}
Here,acloneofanentryfromthespecifieddatasourcewillbecreated. Theentry
key of the clone will be the same as the original but prefixed by the value of the
entrycloneparameter. Theclonedentrywouldstillneedtobecitedinthedocument
usingitsnewentrykey. Thistypeofmappingstepshouldbeusedwithcareasitmay
producelabellingproblemsinauthoryearstyleswhichuse,forexample,extradate.
Oneusecaseisfornumericstyleswhichcontainmultiplebibliographiescontaining
thesameentry. Inthiscase,youmayneeddifferentbibliographynumberlabelsfor
the same entry and this is very tricky when there is only one entry which needs
differentlabels. Creatingcloneswithdifferententrykeyssolvesthisproblem.
\DeclareSourcemap{
\maps[datatype=bibtex]{
\map{
\step[fieldsource=note]
\step[fieldset=usera, origfieldval]
\step[fieldsource=usera, matchesi={string1,string2,StriNg3},
,→ replace={1,2,3}]
}
}
}
208

Here, any note field is copied to usera and then ‘string1’, ‘string2’ and ‘string3’
arematchedcase-insensitivelyintheuserafieldandreplacedwith‘1’,‘2’and‘3’
respectively. Thevalueofmatchesandmatchesiarenotregularexpressions,they
areCSVlistsofliteralstrings,asisthevalueofreplacewheneitherofmatchesor
matchesi are used. The lengths of the match/replace CSV lists must be the same.
Thisisusefulwhencreatinganewfieldtosortbyinacustomsortingschemewhen
thefieldyouwishtosortbyhasadefinedorderwhichisnotalphabeticalornumeric,
such as when sorting by level of court in legal bibliographies. Using matches is
simplymoreefficientthanusingmanyindividualmatchmapsinserial.
biblatexml datasources are more structured than BibTeX since they are XML.
Sourcemappingispossiblewithbiblatexmltoobutthespecificationsofsourceand
targetfieldsetc. alsosupportXPath1.0pathsinordertobeabletoworkwiththe
structureddata. FieldscanbespecifiedaspertheBibTeXexamplesaboveandthese
areconvertedintoXPath1.0queriesinternallyasnecessary. Forexample:
\DeclareSourcemap{
\maps[datatype=biblatexml]{
\map{
\step[fieldsource=\regexp{./bltx:names[@type='author']/bltx:name
,→ [2]/bltx:namepart[@type='family']},
match=\regexp{\ASmith},
replace={Jones}]
}
\map{
\step[fieldsource=editor, fieldtarget=translator]
}
\map{
\step[fieldsource=\regexp{./bltx:names[@type='editor']},
fieldtarget=\regexp{./bltx:names[@type='translator']}]
}
\map{
\step[fieldset=\regexp{./bltx:names[@type='author']/bltx:name
,→ [2]/@useprefix},
fieldvalue={false}]
}
}
}
Thesemaps,respectively,
• Replacethefamilyname‘Smith’ofthesecondauthornamewith‘Jones’
• Movetheeditortotranslator
• MovetheeditortotranslatorbutwithexplicitXPaths
• Settheper-namelistuseprefixoptionontheauthornamelistto‘false’
4.5.4 DataModelSpecification
Thedatamodelwhichbiblatexusesconsistsoffourmainelements:
• Specificationofconstantstringsandlistsofstrings
209

• SpecificationofvalidEntrytypes
• SpecificationofvalidFieldsalongwiththeirtype,datatypeandanyspecial
flags
• SpecificationofwhichFieldsarevalidinwhichEntrytypes
• Specificationofconstraintswhichcanbeusedtovalidatedataagainstthedata
model
Thedefaultdatamodelisdefinedinthecorebiblatexfileblx-dm.defusingthe
macrosdescribedinthissection. Thedefaultdatamodelisdescribedindetailin§2.
Thedatamodelisusedinternallybybiblatexandalsobythebackend. Inpractice,
changing the data model means that you can define the entrytypes and fields for
yourdatasourcesandvalidateyourdataagainstthedatamodel. Naturally,thisisnot
muchuseunlessyourstylesupportsanynewentrytypesorfieldsanditraisesissues
ofportabilitybetweenstyles(althoughthiscanbemitigatedbyusingthedynamic
datamodificationfunctionalitydescribedin§4.5.3).
Notethatwhilethebiber/BibTeXinputsiteisnotcasesensitivewhenitcomes
to entry types and field names (Perl’s Unicode case folding is used to normalise
field names and entry types), the LaTeX side is case sensitive and uses the exact
capitalisationfromthedatamodel.
Validation against the data model means that after mapping your data sources
intothedatamodel,biber(usingits--validate_datamodeloption)cancheck:
• Whetherallentrytypesarevalidentrytypes
• Whetherallfieldsarevalidfieldsfortheirentrytype
• Whetherthefieldsobeyvariousconstraintsontheirformatwhichyouspecify
Redefiningthedatamodelcanbedoneinseveralplaces. Styleauthorscancreatea
.dbx file which contains the data model macros required and this will be loaded
automaticallywhenusingthebiblatexpackagestyleoptionbylookingforafile
named after the style with a .dbx extension (just like the .cbx and .bbx files for
a style). If the style option is not used but rather the citestyle and bibstyle
options, then the package will try to load .dbx files called <citestyle>.dbx
and <bibstyle>.dbx. Alternatively, the name of the data model file can be
differentfromanyofthestyleoptionnamesbyspecifyingthename(without.dbx
extension) to the package datamodel option. After loading the style data model
file,biblatexthenloads,ifpresent,ausersbiblatex-dm.cfgwhichshouldbeput
somewherebiblatexcanfindit,justlikethemainconfigurationfilebiblatex.cfg.
Tosummarise,thedatamodelisdeterminedbyaddingtothedatamodelfromeach
oftheselocations,inorder:
blx-dm.def→
<datamodel option>.dbx→
<style option>.dbx→
<citestyle option>.dbxand<bibstyle option>.dbx→
biblatex-dm.cfg
Itisnotpossibletoaddtoaloadeddatamodelbyusingthemacrosbelowinyour
preambleasthepreambleisreadafterbiblatexhasdefinedcriticalinternalmacros
based on the data model. If any data model macro is used in a document, it will
210

be ignored and a warning will be generated. The data model is defined using the
followingmacros:
\DeclareDatamodelConstant[hoptionsi]{hnamei}{hconstantdefi}
Declares the hnamei as a datamodel constant with definition hconstantdefi. Such
constantsaretypicallyusedinternallybybiber.
type=string,list default:string
Aconstantcanbeasimplestring(defaultifthehtypeioptionisomitted)oracomma-
separatedlistofstrings.
\DeclareDatamodelEntrytypes[hoptionsi]{hentrytypesi}
Declaresthecomma-separatedlistofhentrytypesitobevalidentrytypesinthedata
model. AsusualinTeXcsvlists,makesureeachelementisimmediatelyfollowedby
acommaortheclosingbrace—noextraneouswhitespace.
skipout=true,false default:false
Thisentrytypeisnotoutputtothe.bbl. Typicallyusedforspecialentrytypeswhich
areprocessedandconsumedbythebackendsuchas@xdata.
\DeclareDatamodelFields[hoptionsi]{hfieldsi}
Declares the comma-separated list of hfieldsi to be valid fields in the data model
withassociatedcomma-separatedhoptionsi. Thehtypeiandhdatatypeioptionsare
mandatory. Allvalidhoptionsiare:
type=hfieldtypei
Setthetypeofthefieldasdescribedin§2.2.1,typically‘field’or‘list’.
format=hfieldformati
Anyspecialformatofthefield. Normallyunspecifiedbutcantakethevalue‘xsv’
whichtellsbiberthatthisfieldhasaseparatedvaluesformat. Theexactseparator
canbecontrolledwiththebiberoptionxsvsepanddefaultstotheexpectedcomma
surroundedbyoptionalwhitespace.
datatype=hfielddatatypei
Setthedatatypeofthefieldasdescribedin§2.2.1. Forexample,‘name’or‘literal’.
nullok=true,false default:false
Thefieldisallowedtobedefinedbutempty.
skipout=true,false default:false
The field is not output to the .bbl and is therefore not present during biblatex
styleprocessing. AsusualinTeXcsvlists,makesureeachelementisimmediately
followedbyacommaortheclosingbrace—noextraneouswhitespace.
label=true,false default:false
Thefieldcanbeusedasalabelinabibliographyorbibliographylist. Specifyingthis
causesbiblatextocreateseveralhelpermacrosforthefieldsothattherearesome
internallengthsandheadingsetc. defined.
211

\DeclareDatamodelEntryfields[hentrytypesi]{hfieldsi}
Declaresthatthecomma-separatedlistofhfieldsiisvalidforthecomma-separated
listofhentrytypesi. Ifhentrytypesiisnotgiven,thefieldsarevalidforallentrytypes.
As usual in TeX csv lists, make sure each element is immediately followed by a
commaortheclosingbrace—noextraneouswhitespace.
\DeclareDatamodelConstraints[hentrytypesi]{hspecificationi}
Ifacomma-separatedlistofhentrytypesiisgiven,theconstraintsapplyonlytothose
entrytypes. Thehspecificationiisanundelimitedlistof\constraintdirectiveswhich
specifyaconstraint. Spaces,tabs,andlineendingsmaybeusedfreelytovisually
arrangethehspecificationi. Blanklinesarenotpermissible.
\constraint[htype=constrainttypei]{helementsi}
Specifiesaconstraintoftypehconstrainttypei. Validconstrainttypesare:
type=data,mandatory,conditional
Constraintsoftype‘data’putrestrictionsonthevalueofafield. Constraintsoftype
‘mandatory’specifywhichfieldsorcombinationsoffieldsanentrytypeshouldhave.
Constraintsoftype‘conditional’allowmoresophisticatedconditionalandquantified
fieldconstraints.
datatype=integer,isbn,issn,ismn,datepart,pattern
Forconstraintsoftypehdatai,constrainfieldvaluestobethegivendatatype.
rangemin=hnumi
Forconstraintsofhtypei‘data’andhdatatypei‘integer’,constrainfieldvaluestobe
atleasthnumi.
rangemax=hnumi
Forconstraintsofhtypei‘data’andhdatatypei‘integer’,constrainfieldvaluestobe
atmosthnumi.
pattern=hpatti
For constraints of htypei ‘data’ and hdatatypei ‘pattern’, constrain field values to
matchregularexpressionpatternhpatti. Itisbesttowrapanyregularexpressionin
themacro\regexp,see§4.5.3.
A\constraintmacromaycontainanyofthefollowing:
\constraintfieldsor{hfieldsi}
Forconstraintsofhtypei‘mandatory’,specifiesthatanentrymustcontainaboolean
ORofthe\constraintfields.
\constraintfieldsxor{hfieldsi}
Forconstraintsofhtypei‘mandatory’,specifiesthatanentrymustcontainaboolean
XORofthe\constraintfields.
212

\antecedent[hquantifier=quantspeci]{hfieldsi}
For constraints of htypei ‘conditional’, specifies a quantified set of
\constraintfields which must be satisfied before the \consequent of the
constraintischecked. hquantspecishouldhaveoneofthefollowingvalues:
quantifier=all,one,none
Specifies how many of the \constrainfield’s inside the \antecedent have to be
presenttosatisfytheantecedentoftheconditionalconstraint.
\consequent[hquantifier=quantspeci]{hfieldsi}
For constraints of htypei ‘conditional’, specifies a quantified set of
\constraintfields which must be satisfied if the preceding \antecedent of
theconstraintwassatisfied. hquantspecishouldhaveoneofthefollowingvalues:
quantifier=all,one,none
Specifieshowmanyofthe\constraintfield’sinsidethe\consequenthavetobe
presenttosatisfytheconsequentoftheconditionalconstraint.
\constraintfield{hfieldi}
Forconstraintsofhtypei‘data’,theconstraintappliestothishfieldi. Forconstraints
ofhtypei‘mandatory’,theentrymustcontainthishfieldi.
Thedatamodeldeclarationmacrosmaybeusedmultipletimesastheyappendtothe
previousdefinitions. Inordertoreplace,changeorremoveexistingdefinitions(such
as the default model which is loaded with biblatex), you should reset (clear) the
currentdefinitionandthensetwhatyouwantusingthefollowingmacros. Typically,
thesemacroswillbethefirstthingsinanybiblatex-dm.cfgfile:
\ResetDatamodelEntrytypes
Clearalldatamodelentrytypeinformation.
\ResetDatamodelFields
Clearalldatamodelfieldinformation.
\ResetDatamodelEntryfields
Clearalldatamodelfieldsforentrytypesinformation.
\ResetDatamodelConstraints
ClearalldatamodelfieldsConstraintsinformation.
Here is an example of a simple data model. Refer to the core biblatex file
blx-dm.defforthedefaultdatamodelspecification.
\ResetDatamodelEntrytypes
\ResetDatamodelFields
\ResetDatamodelEntryfields
\ResetDatamodelConstraints
\DeclareDatamodelEntrytypes{entrytype1, entrytype2}
213

\DeclareDatamodelFields[type=field, datatype=literal]{field1,field2,
,→ field3,field4}
\DeclareDatamodelEntryfields{field1}
\DeclareDatamodelEntryfields[entrytype1]{field2,field3}
\DeclareDatamodelEntryfields[entrytype2]{field2,field3,field4}
\DeclareDatamodelConstraints[entrytype1]{
\constraint[type=data, datatype=integer, rangemin=3, rangemax=10]{
\constraintfield{field1}
}
\constraint[type=mandatory]{
\constraintfield{field1}
\constraintfieldsxor{
\constraintfield{field2}
\constraintfield{field3}
}
}
}
\DeclareDatamodelConstraints{
\constraint[type=conditional]{
\antecedent[quantifier=none]{
\constraintfield{field2}
}
\consequent[quantifier=all]{
\constraintfield{field3}
\constraintfield{field4}
}
}
}
Thismodelspecifies:
• Clearthedefaultdatamodelcompletely
• Twovalidentrytypes@entrytype1and@entrytype2
• Fourvalidliteralfieldfields
• field1isvalidforallentrytypes
• field2andfield3arevalidforentrytype1
• field2,field3andfield4arevalidfor@entrytype2
• For@entrytype1:
– field1mustbeanintegerbetween3and10
– field1mustbepresent
– Oneandonlyoneoffield2orfield3mustbepresent
• Foranyentrytype,iffield2isnotpresent,field3andfield4mustbepresent
214

4.5.5 Labels
Alphabeticstylesusealabeltoidentifybibliographyentries. Thislabelisconstructed
fromcomponentsoftheentryusingatemplatewhichdescribeshowtobuildthe
label. The template can be customised on a global or per-type basis. A separate
templateisusedtospecifyhowtoextractpartsofnamefieldsforlabels,sincenames
canbequitecomplexfields.
\DeclareLabelalphaTemplate[]{hspecificationi}
Defines the alphabetic label template for the given entrytypes. If no entrytypes
are specified in the first argument, then the global label template is defined. The
hspecificationiisanundelimitedlistof\labelelementdirectiveswhichspecifythe
elementsusedtobuildthelabel. Spaces,tabs,andlineendingsmaybeusedfreelyto
visuallyarrangethehspecificationi. Blanklinesarenotpermissible. Thiscommand
mayonlybeusedinthepreamble.
\labelelement{helementsi}
Specifiestheelementsusedtobuildthelabel. Thehelementsiareanundelimitedlist
of\fieldor\literalcommandswhichareevaluatedintheorderinwhichtheyare
given. Thefirst\fieldor\literalwhichexpandstoanon-emptystringisusedas
the\labelelementexpansionandthenext\labelelement,ifany,isthenprocessed.
\field[hoptionsi]{hfieldi}
If hfieldi is non-empty, use it as the current label \labelelement, subject to the
options below. Useful values for hfieldi are typically the name list type fields,
date fields, and title fields. You may also use the ‘citekey’ or ‘entrykey‘ pseudo-
fields to specify the citation/entry key as part of the label. Name list fields are
treatedspeciallyandwhenanamelistfieldisspecified,thetemplatedefinedwith
\DeclareLabelalphaNameTemplate is used to extract parts from the name which
thenreturnsthestringthatthe\fieldoptionuses.
final=true,false default:false
This option marks a \field directive as the final one in the hspecificationi. If the
hfieldi isnon-empty, then thisfield is usedfor the labeland the remainderof the
hspecificationiwillbeignored. Theshortformfinalisequivalenttofinal=true.
lowercase=true,false default:false
Forcesthelabelpartderivedfromthefieldtolowercase. Bydefault,thecaseistaken
fromthefieldsourceandnotmodified.
strwidth=hintegeri default:1
The number of characters of the hfieldi to use. This setting may be overrid-
den by an individual name part when extracting characters from a name. See
\DeclareLabelalphaNameTemplatebelow.
strside=left,right default:left
Thesideofthestringfromwhichtotakethestrwidthnumberofcharacters. This
settingmaybeoverriddenbyanindividualnamepartwhenextractingcharacters
fromaname. See\DeclareLabelalphaNameTemplatebelow.
padside=left,right default:right
Sidetopadthelabelpartwhenusingthepadcharoption. Onlyforusewithfixed-
widthlabelstrings(strwidth).
215

padchar=hcharacteri
Ifpresent,padsthelabelpartonthepadsidesidewiththespecifiedcharactertothe
lengthofstrwidth. Onlyforusewithfixed-widthlabelstrings(strwidth).
uppercase=true,false default:false
Forcesthelabelpartderivedfromthefieldtouppercase. Bydefault,thecaseistaken
fromthefieldsourceandnotmodified.
varwidth=true,false default:false
Useavariablewidth,left-sidesubstringofcharactersfromthestringreturnedfor
hfieldi. The length of the string is determined by the minimum length needed to
disambiguatethesubstringfromallotherhfieldielementsinthesamepositionin
thelabel. Fornamelistfields,thismeansthateachnamesubstringisdisambiguated
fromallothernamesubstringswhichoccurinthesamepositioninthenamelist(see
examplesbelow). Thisoptionoverridesstrwidthifbothareused. Theshortform
varwidthisequivalenttovarwidth=true. Fornamelistfields,the\namepartswith
thepreoptionsetareprependedtothestringreturnedfromthisdisambiguation.
varwidthnorm=true,false default:false
As varwidth but will force the disambiguated substrings for the hfieldi to be the
samelengthasthelongestdisambiguatedsubstring. Thiscanbeusedtoregularise
theformatofthelabelsifdesired. Thisoptionoverridesstrwidthifbothareused.
Theshortformvarwidthnormisequivalenttovarwidthnorm=true.
varwidthlist=true,false default:false
Alternativemethodofautomaticlabeldisambiguationwherethefieldasawhole
is disambiguated from all other fields in the same label position. For non-name
listfields,thisisequivalenttovarwidth. Fornamelistfields,namesinanamelist
are not disambiguated from other names in the same position in their name lists
butinsteadtheentirenamelistisdisambiguatedasawholefromothernamelists
(seeexamplesbelow). Thisoptionoverridesstrwidthifbothareused. Theshort
form varwidthlist is equivalent to varwidthlist=true. For name list fields, the
\namepartswiththepreoptionsetareprependedtothestringreturnedfromthis
disambiguation.
strwidthmax=hintegeri
Whenusingvarwidth,thisoptionsetsalimit(innumberofcharacters)onthelength
ofvariablewidthsubstrings. Thisoptioncanbeusedtoregularisethelabel.
strfixedcount=hintegeri default:1
When using varwidthnorm, there must be at least strfixedcount disambiguated
substringswiththesame,maximallengthtotriggertheforcingofalldisambiguated
substringstothissamemaximallength.
ifnames=hrangei
Onlyusethis\fieldspecificationifitisanamelistfieldwithanumberofnames
matchingtheifnamesrangevalue. Thisallowsa\labelelementtobeconditionalised
onnamelength(seebelow). Therangecanspecifiedasinthefollowingexamples:
ifnames=3 -> Only apply to name lists containing exactly 3 names
ifnames={2-4} -> Only apply to name lists containing minimum 2 and
,→ maximum 4 names
ifnames={-3} -> Only apply to name lists containing at most 3 names
ifnames={2-} -> Only apply to name lists containing at least 2 names
216

names=hrangei
By default, for name list fields, the names used range from the first name to the
maxalphanames/minalphanamestruncation. Thisoptioncanbeusedtooverridethis
withanexplicitrangeofnamestoconsider. Theplus‘+’signisaspecialendofrange
markerdenotingthetruncationpointofmax/minalphanames. Therangeseparator
canbeanynumberofcharacterswiththeUnicodeDashproperty. Forexample:
| names=3     | -> Use first  | 3 names    | in the name list |     |     |
| ----------- | ------------- | ---------- | ---------------- | --- | --- |
| names={2-3} | -> Use second | and thirds | names only       |     |     |
| names={-3}  | -> Same       | as 1-3     |                  |     |     |
names={2-} -> Use all names starting with the second name (ignoring
,→
| max/minalphanames |     | truncation) |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- |
names={2-+} -> Use all names starting with the second name (respecting
| ,→ max/minalphanames |     | truncation) |     |               |     |
| -------------------- | --- | ----------- | --- | ------------- | --- |
| namessep=hstringi    |     |             |     | default:empty |     |
Anarbitrarystringseparatortoputbetweennamesinanamelist.
| noalphaothers=true,false |     |     |     | default:false |     |
| ------------------------ | --- | --- | --- | ------------- | --- |
Bydefault,\labelalphaothersisappendedtolabelpartsderivedfromnamelistsif
therearemorenamesinthelistthanareshowninthelabelpart. Thisoptioncanbe
usedtodisablethedefaultbehaviour.
\literal{hcharactersi}
Inserttheliteralhcharactersiintothelabelatthispoint.
Whenanamelist\fieldisspecified,themethodofextractingthestringisspecified
byaseparatetemplatespecifiedbythefollowingcommand:
\DeclareLabelalphaNameTemplate[hnamei]{hspecificationi}
Definesthelabelalphanametemplatehnamei. Thehnameiisoptionalanddefaults
toh‘global’i.
Suchtemplatesspecifyhowtoextractalabelstringfromanamelistwhena\field
specificationin\DeclareLabelalphaTemplatecontainsanamelist.
\namepart[hoptionsi]{hnameparti}
hnameparti
|                                              | is one | of the datamodel | nameparts        | defined with  | the |
| -------------------------------------------- | ------ | ---------------- | ---------------- | ------------- | --- |
| \DeclareDatamodelConstantcommand(see§4.2.3). |        |                  | Thehoptionsiare: |               |     |
| use=true,false                               |        |                  |                  | default:false |     |
Only use the hnameparti in constructing the label information if there is a corre-
spondingoptionuse‘namepart’andthatoptionistrue.
| pre=true,false |     |     |     | default:false |     |
| -------------- | --- | --- | --- | ------------- | --- |
Whenconstructinglabelstringsfromnames,the\namepartwithout apreoption
will be used to construct label string, passing through disambiguation, substring
etc. operationsasspecifiedbythe\fieldoptionsin\DeclareLabelalpaTemplate.
Then the \namepart options with the pre option set will be prepended to the
result, (in the order given, if there are more than one such \nameparts). This
allows to unconditionally prepend certain namepart information to name label
217

strings, like name prefices. Note that the uppercase and lowercase options of
\field in \DeclareLabelalphaTemplate are applied to the entire label returned
from\DeclareLabelalphaTemplate,bothprepartsandnonpre.
compound=true,false default:false
For static (non-varwidth) disambiguation in \DeclareLabelalphaTemplate, treat
namepartsseparatedbywhitespaceorhyphens(compoundnames)asseparatenames
forlabelgeneration. Thismeansthatwhenformingalabeloutof,forexamplethe
surname‘BallamForsyth’witha1character,left-sidesubstring,thisnamewouldgive
‘BF’withcompound=trueand‘B’withcompound=false. Theshortformcompoundis
equivalenttocompound=true.
strwidth=hintegeri default:1
Thenumberofcharactersofthehnamepartitouse.
strside=left,right default:left
Thesideofthestringfromwhichtotakethestrwidthnumberofcharacters.
Notethatthetemplatesforlabelscanbedefinedper-typeandyoushouldbeaware
ofthiswhenusingtheautomaticallydisambiguatedlabelfunctionality. Disambigua-
tionisnotper-typeasthismightleadtoambiguityduetodifferentlabelformatsfor
differenttypesbeingisolatedfromeachothersdisambiguationprocess. Normally,
youwillwanttouseverydifferentlabelformatsfordifferenttypestomakethetype
obviousbythelabel.
Herearesomeexamples. Thedefaultglobalbiblatexalphabeticlabeltemplate
isdefinedbelow. Firstly,shorthandhasfinal=trueandsoifthereisashorthand
field,itisusedasthelabelandnothingmoreofthetemplateisconsidered. Next,
the label field is used as the first label element if it exists. Otherwise, if there is
onlyonename(ifnames=1)inthelabelnamelist,thenthreecharactersfromtheleft
sideofthefamilynameinthelabelnameareusedasthefirstlabelelement. Ifthe
labelnamehasmorethanonenameinit, onecharacterfromtheleftsideofeach
familynameisusedasthefirstlabelelement. Thesecondlabelelementconsistsof2
charactersfromtherightsideoftheyearfield.
The default template for constructing labels from names is also shown. This
prependsthefirstcharacterfromtheleftsideofanyprefix(iftheuseprefixoption
istrue)toalabelextractedfromthefamilyname(accordingtotheoptionsonthe
calling\fieldoptionfrom\DeclareLabelalphaTemplate),allowingforcompound
familynames.
\DeclareLabelalphaTemplate{
\labelelement{
\field[final]{shorthand}
\field{label}
\field[strwidth=3,strside=left,ifnames=1]{labelname}
\field[strwidth=1,strside=left]{labelname}
}
\labelelement{
\field[strwidth=2,strside=right]{year}
}
}
\DeclareLabelalphaNameTemplate{
218

\namepart[use=true, pre=true, strwidth=1, compound=true]{prefix}
\namepart{family}
}
Togetanideaofhowthelabelautomaticdisambiguationworks,considerthefol-
lowingauthorlists:
Agassi, Chang, Laver (2000)
Agassi, Connors, Lendl (2001)
Agassi, Courier, Laver (2002)
Borg, Connors, Edberg (2003)
Borg, Connors, Emerson (2004)
Assumingatemplatedeclarationsuchas:
\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidth]{labelname}
}
}
Thenthelabelswouldbe:
Agassi, Chang, Laver [AChLa]
Agassi, Connors, Lendl [AConLe]
Agassi, Courier, Laver [ACouLa]
Borg, Connors, Edberg [BConEd]
Borg, Connors, Emerson [BConEm]
Withnormalisedvariablewidthlabelsdefined:
\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidthnorm]{labelname}
}
}
Youwouldgetthefollowingasthesubstringsofnamesineachpositionareextended
tothelengthofthelongestsubstringinthatsameposition:
Agassi, Chang, Laver [AChaLa]
Agassi, Connors, Lendl [AConLe]
Agassi, Courier, Laver [ACouLa]
Borg, Connors, Edberg [BConEd]
Borg, Connors, Emerson [BConEm]
Witharestrictiontotwocharactersforthenamecomponentsofthelabelelement
definedlikethis:
219

\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidthnorm,strwidthmax=2]{labelname}
}
}
This would be the result (note that the individual family name label parts are no
longerunambiguous):
Agassi, Chang, Laver [AChLa]
Agassi, Connors, Lendl [ACoLe]
Agassi, Courier, Laver [ACoLa]
Borg, Connors, Edberg [BCoEd]
Borg, Connors, Emerson [BCoEm]
Alternatively,youcouldchoosetodisambiguatethenamelistsasawholewith:
\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidthlist]{labelname}
}
}
Whichwouldresultin:
Agassi, Chang, Laver [AChL]
Agassi, Connors, Lendl [ACoL]
Agassi, Courier, Laver [ACL]
Borg, Connors, Edberg [BCEd]
Borg, Connors, Emerson [BCE]
Perhaps you only want to consider at most two names for label generation but
disambiguateatthewholenamelistlevel:
\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidthlist,names=2]{labelname}
}
}
Whichwouldresultin:
Agassi, Chang, Laver [ACh+]
Agassi, Connors, Lendl [ACo+]
Agassi, Courier, Laver [AC+]
Borg, Connors, Edberg [BC+a]
Borg, Connors, Emerson [BC+b]
Inthislastexample, youcansee\labelalphaothershasbeenappendedtoshow
that there are more names. The last two labels now require disambiguating with
220

\extraalphaasthereisnowayofdisambiguatingthislabelnamelistwithonlytwo
names.
Finally,hereisanexampleusingmultiplelabelelements:
\DeclareLabelalphaTemplate{
\labelelement{
\field[varwidthlist]{labelname}
}
\labelelement{
\literal{-}
}
\labelelement{
\field[strwidth=3,strside=right]{labelyear}
}
}
Whichwouldresultin:
| Agassi, Chang,   | Laver   | [AChL-000]  |     |
| ---------------- | ------- | ----------- | --- |
| Agassi, Connors, | Lendl   | [AConL-001] |     |
| Agassi, Courier, | Laver   | [ACouL-002] |     |
| Borg, Connors,   | Edberg  | [BCEd-003]  |     |
| Borg, Connors,   | Emerson | [BCEm-004]  |     |
Hereisanotherrathercontrivedexampleshowingthatyoudon’tneedtospecially
quoteLaTeXspecialcharacters(apartfrom‘%’,obviously)whenspecifyingpadding
charactersandliterals:
\DeclareLabelalphaTemplate{
\labelelement{
\literal{>}
}
\labelelement{
\literal{\%}
}
\labelelement{
| \field[namessep={/}, |     | strwidth=4, | padchar=_]{labelname} |
| -------------------- | --- | ----------- | --------------------- |
}
\labelelement{
| \field[strwidth=3, |     | padchar=&, | padside=left]{title} |
| ------------------ | --- | ---------- | -------------------- |
}
\labelelement{
\field[strwidth=2,strside=right]{year}
}
}
whichgiven:
@Book{test,
| author | = {XXX | YY and WWW ZZ}, |     |
| ------ | ------ | --------------- | --- |
| title  | = {T}, |                 |     |
221

year = {2007},
}
wouldresultingalabellookinglikethis:
[>%YY/ZZ__&&T07]
Generatinglabelsfromfieldsmayinvolvesomedifficultieswhenyouhavefields
containing diacritics, hyphens, spaces etc. Often, you want to ignore things like
separator characters or spaces when generating labels. An option is provided to
customise the regular expression(s) to strip from a field before it is passed to the
labelgenerationsystem.
\DeclareNolabel{hspecificationi}
Definesregularexpressionstostripfromanyfieldbeforegeneratingalabelpartfor
thefield. Thehspecificationiisanundelimitedlistof\nolabeldirectiveswhichspec-
ifytheregularexpressionstoremovefromfields. Spaces,tabsandlineendingsmay
beusedfreelytovisuallyarrangethehspecificationi. Blanklinesarenotpermissible.
Thiscommandmayonlybeusedinthepreamble.
\nolabel{hregexpi}
Anynumberof\nolabelcommandscanbegiveneachofwhichspecifiestoremove
thehregexpifromthecopyofthefieldwhichthelabelgenerationsystemsees. Since
regular expressions usually contain special characters, it is best to enclose them
intheprovided\regexpmacroasshown—thiswillpasstheexpressionthroughto
bibercorrectly.
Ifthereisno\DeclareNolabelspecification,biberwilldefaultto:
\DeclareNolabel{
% strip punctuation, symbols, separator and control characters
\nolabel{\regexp{[\p{P}\p{S}\p{C}]+}}
}
Thisbiberdefaultstripspunctuation,symbol,separatorandcontrolcharactersfrom
fieldsbeforepassingthefieldstringtothelabelgenerationsystem.
\DeclareNolabelwidthcount{hspecificationi}
Defines regular expressions to ignore from any field when counting charac-
ters in fixed-width substrings. The hspecificationi is an undelimited list of
\nolabelwidthcount directives which specify the regular expressions to ignore
when counting characters for fixed-width substrings. Spaces, tabs and line end-
ingsmaybeusedfreelytovisuallyarrangethehspecificationi. Blanklinesarenot
permissible. Thiscommandmayonlybeusedinthepreamble.
\nolabelwidthcount{hregexpi}
Anynumberof\nolabelwidthcountcommandscanbegiveneachofwhichspec-
ifies to ignore the hregexpi when generating fixed-width substrings during label
generation. Sinceregularexpressionsusuallycontainspecialcharacters,itisbestto
enclosethemintheprovided\regexpmacroasshown—thiswillpasstheexpression
throughtobibercorrectly.
222

There is no default \DeclareNolabelwidthcount specification. Note that this
settingisonlytakenintoaccountwhenusingfixed-widthsubstrings(non-varwidth)
duringlabelpartgeneration. See§4.5.5.
4.5.6 Sorting
Inadditiontothepredefinedsortingtemplatesdiscussedin§3.6, itispossibleto
define new ones or modify the default definitions. The sorting process may be
customizedfurtherbyexcludingcertainfieldsfromsortingonaper-typebasisand
byautomaticallypopulatingthepresortfieldonaper-typebasis.
\DeclareSortingTemplate[hoptionsi]{hnamei}{hspecificationi}
Defines the sorting template hnamei. The hnamei is the identifier passed
to the sorting option (§ 3.1.2.1) when selecting the sorting template. The
\DeclareSortingTemplatecommandsupportsthefollowingoptionalarguments:
locale=hlocalei
Thelocaleforthesortingtemplatewhichthenoverridestheglobalsortinglocalein
thesortlocaleoptiondiscussedin§3.1.2.1.
Thehspecificationiisanundelimitedlistof\sortdirectiveswhichspecifytheele-
mentstobeconsideredinthesortingprocess. Spaces,tabs,andlineendingsmaybe
usedfreelytovisuallyarrangethehspecificationi. Blanklinesarenotpermissible.
Thiscommandmayonlybeusedinthepreamble.
\sort{helementsi}
Specifies the elements considered in the sorting process. The helementsi are an
undelimitedlistof\field,\literal,\citecount,\intciteorderand\citeorder
commandswhichareevaluatedintheorderinwhichtheyaregiven. Ifanelement
isdefined,itisaddedtothesortkeyandthesortingroutineskipstothenext\sort
directive. Ifitisundefined,thenextelementisevaluated. Sinceliteralstringsare
always defined, any \literal commands should be the sole or the last element
in a \sort directive. All helementsi should be the same datatype as described in
§2.2.2sincetheywillbepotentiallycomparedtoanyoftheotherhelementsiinother
entries.. The\sortcommandsupportsthefollowingoptionalarguments:
locale=hlocalei
Override the locale used for sorting at the level of a particular set of sort-
ing elements. If specified, the locale overrides the locale set at the level of
\DeclareSortingTemplateandalsotheglobalsetting. Seealsothediscussionofthe
globalsortinglocaleoptionsortlocalein§3.1.2.1.
direction=ascending,descending default:ascending
The sort direction, which may be either ascending or descending. The default is
ascendingorder.
final=true,false default:false
Thisoptionmarksa\sortdirectiveasthefinaloneinthehspecificationi. Ifoneof
thehelementsiisavailable,theremainderofthehspecificationiwillbeignored. The
shortformfinalisequivalenttofinal=true.
sortcase=true,false
Whetherornottosortcase-sensitively. Thedefaultsettingdependsontheglobal
sortcaseoption.
223

sortupper=true,false
Whetherornottosortin‘uppercasebeforelowercase’(true)or‘lowercasebefore
uppercase’order(false). Thedefaultsettingdependsontheglobalsortupperoption.
\field[hkey=value,…i]{hfieldi}
The\fieldelementaddsahfielditothesortingspecification. Ifthehfieldiisunde-
fined,theelementisskipped. The\fieldcommandsupportsthefollowingoptional
arguments:
padside=left,right default:left
Padsafieldontheleftorrightsideusingpadcharsothatitswidthispadwidth. If
nopaddingoptionisset,nopaddingisdoneatall. Ifanypaddingoptionisspecified,
then padding is performed and the missing options are assigned built-in default
values. Ifpaddingandsubstringmatchingarebothspecified,thesubstringmatchis
performedfirst.
padwidth=hintegeri default:4
Thetargetwidthincharacters.
padchar=hcharacteri default:0
Thecharactertobeusedwhenpaddingthefield.
strside=left,right default:left
Performs a substring match on the left or right side of the field. The number
of characters to match is specified by the corresponding strwidth option. If no
substringoptionisset,nosubstringmatchingisperformedatall. Ifanysubstring
optionisspecified,thensubstringmatchingisperformedandthemissingoptions
are assigned built-in default values. If padding and substring matching are both
specified,thesubstringmatchisperformedfirst.
strwidth=hintegeri default:4
Thenumberofcharacterstomatch.
\literal{hstringi}
The \literal element adds a literal hstringi to the sorting specification. This is
usefulasafallbackifsomefieldsarenotavailable.
\citecount The \citecount element has a special meaning. It requests a sort based on the
numberoftimesanitemwascited. Thestandardcountsortingtemplateusesthis
toprovideasortindescendingorderofnumberofcitations. Notethattheoption
citecountermustalsobeenabledforthistowork. Inaddition,anadditionalbiber
runisrequiredinordertocalculatethedataforthisoptioncorrectlyandsothetypical
invocationsequenceforthisoptionislatex→biber→latex→latex→biber→latex.
\citeorder The\citeorderelementhasaspecialmeaning. Itrequestsasortbasedonthelexical
orderoftheactualcitations. Forentriescitedwithinthesamecitationcommand
like:
\cite{one,two}
224

thereisadistinctionbetweenthelexicalorderandthesemanticorder. Here“one”
and“two”havethesamesemanticorderbutauniquelexicalorder. Thesemantic
orderonlymattersifyouspecifyfurthersortingtodisambiguateentrieswiththe
samesemanticorder. Forexample,thisisthedefinitionofthenonesortingtemplate:
\DeclareSortingTemplate{lexical}{
\sort{\citeorder}
}
Thissortsthebibliographypurelylexicallybytheorderofthekeysinthecitation
commands. Intheexampleabove,itsorts“one”before“two”. However,supposethat
youconsider“one”and“two”tohavethesameorder(semanticorder)sincetheyare
citedatthesametimeandwanttofurthersortthesebyyear. Suppose“two”hasan
earlieryearthan“one”:
\DeclareSortingTemplate{lexicalyear}{
\sort{\citeorder}
\sort{year}
}
Thissorts“two”before“one”,eventhoughlexically,“one”wouldsortbefore“two”.
This is possible because the semantic order can be disambiguated by the further
sorting on year. With the standard none sorting template, the lexical order and
semanticorderareidenticalbecausethereisnothingfurthertodisambiguatethem.
This means that you can use \citeorder just like any other sorting specification
element,choosinghowtofurthersortentriescitedatthesametime(inthesame
citationcommand).
Seealso\intciteorderbelow.
\intciteorder The\intciteorderelementhasaspecialmeaning. Itrequestsasortbasedonthe
lexicalorderinternaltothesamecitationcommand. Forexample:
\cite{one,two}
Here both citations have the same \citeorder but different \intciteorder. This
sortingcommandisbasicallyamoregranularformof\citeordersothatordercan
bedistinguishedforcitationswithinthesamecitationcommand. So,forexample,
withtheaboveexample,thiswillguaranteesortingof‘one’before‘two’:
\DeclareSortingTemplate{fulllexical}{
\sort{\citeorder}
\sort{\intciteorder}
}
\DeclareSortingNamekeyTemplate[hnamei]{hspecificationi}
Defineshowthesortingkeysfornamesareconstructed. Thiscanchangethesorting
orderofnamesarbitrarilybecauseyoucanchoosehowtoputtogetherthenameparts
225

whenconstructingthestringtocomparewhensorting. Thesortingkeyconstruction
template so defined is called hnamei which defaults to “global” if this optional
parameterisabsent. Whenconstructingthesortingkeyforaname,asortingkeyfor
eachnamepartisconstructedandthekeyforeachnameisformedintoanordered
keylistwithaspecialinternalseparator. Thepointofthisoptionistoaccommodate
languagesorsituationswheresortingofnamesneedstobecustomised(forexample,
Icelandicnamesaresometimessortedbygivennamesratherthanbyfamilynames).
This macro may be used multiple times to define templates with different names
whichcanthenbereferredtolater. Sortingnamekeytemplatescanbespecifiedat
thefollowingscopes,inorderofincreasingprecedence:
• Thedefaulttemplatedefinedwithouttheoptionalnameargument
• Given as the sortingnamekeytemplate option to a reference context (see
§3.8.10)
• Givenasaper-entryoptionsortnamekeytemplateinabibliographydatasource
entry
• Givenasaper-namelistoptionsortnamekeytemplate
• Givenasaper-nameoptionsortnamekeytemplate
Bydefaultthereisonlyaglobaltemplatewhichhasthefollowinghspecificationi:
\DeclareSortingNamekeyTemplate{
\keypart{
\namepart[use=true]{prefix}
\namepart{family}
}
\keypart{
\namepart{given}
}
\keypart{
\namepart{suffix}
}
\keypart{
\namepart[use=false]{prefix}
}
}
Thismeansthatthekeyisconstructedbyconcatenating,inorder,thenameprefix
(onlyiftheuseprefixoptionistrue)withthefamilyname(s),thegivennames(s),
thenamesuffixandthenthenameprefix(onlyiftheuseprefixoptionisfalse). The
visible number of names in the name list used to construct the key is the default
sortingvisibility,seebelow.
\visibility{hvisibilityscopei}
hvisibilityscopeidetermineswhichvisibilitysettingstouseforthenamelist. This
determineshowmanynamesinthenamelistarevisibletothesortingalgorithm. This
isbydefaultsetto‘sort’,whichisthestandardvisibilityforsortingdeterminedbythe
max*/min*names and uniquelist options. \visibility can be omitted entirely if
thisdefaultisdesired. Theonlyotherscopeis‘cite’whichforcesthesortingalgorithm
tousethenamelistvisibilityofthecitationsratherthanthatofthereferencelist
226

sorting. Thisisusefulwhenusingthesortcitesoptioninthesituationwhenastyle
hasdifferentnamelisttruncationrulesforcitationsthanithasforthereferencelist.
Citationscanthenbeforcedtosortusingadifferentreferencecontextthatusesa
modifiedsortingnamekeytemplatethatenforcesthecorrectnamelisttruncation
forcitationsortingwith:
\DeclareSortingNamekeyTemplate[mycitesorttemplate]{
\visibilty{cite}
.
.
.
andthenforcethistobeusedwithe.g.:
\newrefcontext[sortingnamekeytemplate=mycitesorttemplate]
\cite{a,b,c}
Onething tonote isthat areferencecontextwill notbe written tothe .bcfifno
\printbibliographyor\printbiblistoccurswithinitwhichwillmeanthatbiber
willnotgenerateanysorteddatafortherefcontext. Thereforeiftherequirement
is to just correctly sort citations using this refcontext, you will need to force the
writingoftherefcontextusing\GenRefcontextData(see§3.8.10):
| % make      | sure sorting      | data                             | using this | template |     | is  |
| ----------- | ----------------- | -------------------------------- | ---------- | -------- | --- | --- |
| % generated | since no          | \printbibliography/\printbiblist |            |          |     |     |
| % occurs    | in the refcontext |                                  | with       |          |     |     |
% sortingnamekeytemplatename=mycitesorttemplate,
| % this | won't happen | by default |     |     |     |     |
| ------ | ------------ | ---------- | --- | --- | --- | --- |
\GenRefcontextData{sortingnamekeytemplatename=mycitesorttemplate}
| % Switch | to this refcontext |            | to use       | the | correct  |       |
| -------- | ------------------ | ---------- | ------------ | --- | -------- | ----- |
| % sorted | data using         | the        | sorting name | key | template |       |
| % which  | uses "cite"        | visibility | for          | the | name     | lists |
\newrefcontext[sortingnamekeytemplate=mycitesorttemplate]
| % citations | are correctly |     | sorted |     |     |     |
| ----------- | ------------- | --- | ------ | --- | --- | --- |
\cite{a,b,c}
| % Switch  | to the default     |     | sorting name | key      | template |     |
| --------- | ------------------ | --- | ------------ | -------- | -------- | --- |
| % for the | actual list        | of  | references   | which    | uses     | the |
| % default | sorting visibility |     | for          | the name | lists    |     |
\newrefcontext[sortingnamekeytemplate=global]
| % references | are correctly |     | sorted |     |     |     |
| ------------ | ------------- | --- | ------ | --- | --- | --- |
\printbibliography
\keypart{hparti}
hpartiisanorderedlistofof\namepartand\literalspecificationswhicharecon-
catenatedtogetherwhenconstructingapartofthenamesortingkey. The\keyparts
arethenconcatenatedtogetherwithterminalpaddingtoensurecorrectsorting.
\literal{hstringi}
Aliteralstringtoinsertintothenamesortingkey.
227

\namepart{hnamei}
Specifiesthehnameiofanameparttouseinconstructingthenamesortingkey.
use=true,false default:true
Indicatesthatthenameparthnameiisonlytobeusedinthisconcatenationposition
ifthecorrespondinguse‘name’optionissettothespecifiedbooleanvalue.
inits=true,false default:true
Indicatesthatonlytheinitialsofnameparthnameiaretobeusedinconstructing
thesortingspecification.
Asanexample,supposeyouwantedtobeabletosortnamesbygivennamerather
thanfamilyname,youcoulddefineasortingnamekeytemplatelikethis:
\DeclareNamekeyTemplate[givenfirst]{
\keypart{
\namepart{given}
}
\keypart{
\namepart[use=true]{prefix}
}
\keypart{
\namepart{family}
}
\keypart{
\namepart[use=false]{prefix}
}
}
Youcanthenusethenamegivenfirstattheappropriatescopeinordertomake
biber use this template when constructing sorting name keys. For example, you
couldenablethisforonebibliographylistlikethis:
\begin{refcontext}[sortnamekeytemplate=givenfirst]
\printbibliography
\end{refcontext}
orperhapsyouonlywanttodothisforaparticularentry:
@BOOK{key,
OPTIONS = {sortnamekeytemplate=givenfirst},
AUTHOR = {Arnar Vigfusson}
}
orjustanamelistbyusingtheoptionasapseudo-namewhichwillbeignored:
@BOOK{key,
AUTHOR = {sortnamekeytemplate=givenfirst and Arnar Vigfusson}
}
228

orjustasinglenamebypassingtheoptionaspartoftheextendednameinformation
formatwhichbibersupports(see§3.4):
@BOOK{key,
AUTHOR = {given=Arnar, family=Vigfusson, sortnamekeytemplate=
,→ givenfirst}
}
Nowwegivesomeexamplesofsortingtemplates. Inthefirstexample,wedefinea
simplename/title/yeartemplate. Thenameelementmaybeeithertheauthor,the
editor,orthetranslator. Giventhisspecification,thesortingroutinewillusethe
firstelementwhichisavailableandcontinuewiththetitle. Notethattheoptions
use<name>optionsareconsideredautomaticallyinthesortingprocess:
\DeclareSortingTemplate{sample}{
\sort{
\field{author}
\field{editor}
\field{translator}
}
\sort{
\field{title}
}
\sort{
\field{year}
}
}
Inthenextexample,wedefinethesametemplateinamoreelaborateway,considering
special fields such as presort, sortkey, sortname, etc. Since the sortkey field
specifies the master sort key, it needs to override all other elements except for
presort. This is indicated by the final option. If the sortkey field is available,
processingwillstopatthispoint. Ifnot,thesortingroutinecontinueswiththenext
\sortdirective. Thissetupcorrespondstothedefaultdefinitionofthentytemplate:
\DeclareSortingTemplate{nty}{
\sort{
\field{presort}
}
\sort[final]{
\field{sortkey}
}
\sort{
\field{sortname}
\field{author}
\field{editor}
\field{translator}
\field{sorttitle}
\field{title}
}
\sort{
229

\field{sorttitle}
\field{title}
}
\sort{
\field{sortyear}
\field{year}
}
}
Finally,hereisanexampleofasortingtemplatewhichoverridestheglobalsorting
localeandadditionallyoverridesagainwhensortingbytheorigtitlefield. Note
theuseinthetemplate-leveloverrideofababel/polyglossialanguagenameinstead
ofareallocaleidentifier. biberwillmapthistoasuitable,reallocaleidentifier(in
thiscase,sv_SE):
\DeclareSortingTemplate[locale=swedish]{custom}{
\sort{
\field{sortname}
\field{author}
\field{editor}
\field{translator}
\field{sorttitle}
\field{title}
}
\sort[locale=de_DE_phonebook]{
\field{origtitle}
}
}
\DeclareSortExclusion{hentrytype,…i}{hfield,…i}
Specifies fields to be excluded from sorting on a per-type basis. The hentrytypei
argument and the hfieldi argument may be a comma-separated list of values. A
blank hfieldi argument will clear all exclusions for this hentrytypei. A value of
‘*’for hentrytypei willexcludehfield,…iforevery entrytype. This isequivalent to
simplydeletingthefieldfromthesortingspecificationandisonlynormallyused
in combination with \DeclareSortInclusion when one wishes to exclude a field
forallbutexplicitlyincludedentrytypes. Seeexamplein\DeclareSortInclusion
below. Thiscommandmayonlybeusedinthepreamble.
\DeclareSortInclusion{hentrytype,…i}{hfield,…i}
Only used along with \DeclareSortExclusion. Specifies fields to be included in
sortingonaper-typebasis. Thisallowstheusertoexcludeafieldfromsortingforall
entrytypesandthentooverridethisforcertainentrytypes. Thisiseasiersometimes
than using \DeclareSortExclusion to list exclusions for many entrytypes. The
hentrytypeiargumentandthehfieldiargumentmaybeacomma-separatedlistof
values. Thiscommandmayonlybeusedinthepreamble. Forexample,thiswould
usetitleduringsortingonlyfor@articles:
\DeclareSortExclusion{*}{title}
230

\DeclareSortInclusion{article}{title}
\DeclarePresort[hentrytype,…i]{hstringi}
Specifiesastringtobeusedtoautomaticallypopulatethepresortfieldofentries
withoutapresortfield. Thepresortmaybedefinedgloballyoronaper-typebasis.
Iftheoptionalhentrytypeiargumentisgiven,thehstringiappliestotherespective
entrytype. Ifnot,itservesastheglobaldefaultvalue. Specifyinganhentrytypeiin
conjunctionwithablankhstringiwillclearthetype-specificsetting. Thehentrytypei
argumentmaybeacomma-separatedlistofvalues. Thiscommandmayonlybeused
inthepreamble.
\DeclareSortTranslit[hentrytypei]{hspecificationi}
Languages which can be written in different scripts or alphabets often only have
CLDRsortingtailoringforonescriptanditisexpectedthatyoutransliterateinto
thesupportedscriptforsortingpurposes. AcommonexampleisSanskritwhichis
oftenwritteninacademiccontextsinIASTromanisedscriptbutwhichneedstobe
sortedinthe‘sa’localewhichexpectstheDevanāgarīscript. Anothercommoncase
istransliterationofRussianCyrillicintoLatinasdefinedbytheALA-LCstandard.
Suchrequirementmeansthatitisnecessarytotransliterateintothesortingscript
internally. \DeclareSortTranslit declares which parts of an entry you would
like to transliterate for sorting purposes. Without the hentrytypei parameter, the
hspecificationiappliestoallentrytypes. Thehspecificationiisoneormore\translit
commands:
\translit[hlangidsi]{hfieldorfieldseti}{hfromi}{htoi}
Specifiesthatthedatafieldfieldorallfieldsinafieldsethfieldsetideclaredwith
\DeclareDatafieldSet(see§4.5.2)shouldbetransliteratedfromscript hfromito
scripthtoiforsortingpurposes. Thefield/setargumentshouldbe‘*’toapplytranslit-
eration to all fields. The valid hfromi and htoi values are given in table 11. The
optional hlangidsi parameter is a comma-separated list of langid fields and the
transliterationwillapplyonlytobibliographyentriescontainingoneofthelangids
inthelist. Notethatbiblatexdoesnotaimtosupportgeneraltransliteration,only
thosewhichareusefulforsortingpurposes. PleaseopenaGitHubticketforbiblatex
ifyouthinkyouneedadditionaltransliterations.
An example of transliterating titles so that they sort correctly in Sanskrit. This
exampleassumesthatentriesthatshouldhavetheirtitlefieldstransliteratedhavea
langidfieldsetto‘sanskrit’.
\DeclareDatafieldSet{settitles}{
\member[field=title]
\member[field=booktitle]
\member[field=eventtitle]
\member[field=issuetitle]
\member[field=journaltitle]
\member[field=maintitle]
\member[field=origtitle]
}
\DeclareSortTranslit{
231

Table11:Validtransliterationpairs
From To Description
iast devanagari SanskritIASTtoDevanāgarī
russian ala-lc ALA-LCromanisationforRussian
russian bgn/pcgn-standard BGN/PCGN:1947(StandardVariant),CyrillictoLatin,Russian
\translit[sanskrit]{settitles}{iast}{devanagari}
}
4.5.7 BibliographyListFilters
Whenusingcustomisablebibliographylists(See§3.8.3),usuallyonewantstoreturn
inthe.bblonlythoseentrieswhichhavetheparticularfieldswhichthebibliography
listissummarising. Forexample, whenprintinganormallistofshorthands, you
wantthelistreturnedbybiberinthe.bbltocontainonlythoseentrieswhichhave
ashorthandfield. Thisisaccomplishedbydefiningabibliographylistfilterusing
the \DeclareBiblistFilter command. This differs fromthe filters defined using
\defbibfilter (see § 3.8.9) since the filters defined by \defbibfilter run inside
biblatexafterthe.bblhasbeengenerated.
\DeclareBiblistFilter{hnamei}{hspecificationi}
Definesabibliographylistfilterwithhnamei. Thehspecificationiconsistsofoneor
more\filteror\filterormacros,allofwhichmustbesatisfiedfortheentryto
passthefilter:
\filter[hfilterspeci]
Filterentriesaccordingtothehfilterspeci. hfilterspecicanbeoneof:
type=type/nottype,filter=hentrytypei Entryis/isnotofentrytype
type=subtype/notsubtype,filter=hsubtypei Entryis/isnotofsubtype
type=keyword/notkeyword,filter=hkeywordi Entryhas/doesnothavekeyword
type=field/notfield,filter=hfieldi Entryhas/doesnothaveafieldcalledfield
\filteror{htypei}{hfiltersi}
A wrapper around one or more \filter commands specifying that they form a
disjunctiveset,i.e. anyoneofthehfiltersimustbesatisfied.
Fieldsinthedatamodelwhicharemarkedas‘Labelfields’(see§4.5.4)automatically
haveafilterdefinedforthemwiththesamenameandwhichfiltersoutanyentries
whichdonocontainthefield. Forexample,biblatexautomaticallygeneratesafilter
fortheshorthandfield:
\DeclareBiblistFilter{shorthand}{
\filter[type=field,filter=shorthand]
}
232

4.5.8 ControllingNameInitialsGeneration
Generatinginitialsfornamepartsfromagivennameinvolvessomedifficultieswhen
youhavenameswithprefixes, diacritics, hyphensetc. Often, youwanttoignore
thingslikeprefixeswhengeneratinginitialssothattheinitialsfor“al-Hasan”isjust
“H”insteadof“a-H”.Thisistrickywhenyoualsohavenameslike“Ho-Pun”where
youwanttheinitialstobe“H-P”,forexample.
\DeclareNoinit{hspecificationi}
Defines regular expressions to strip from names before generating initials. The
hspecificationiisanundelimitedlistof\noinitdirectiveswhichspecifytheregular
expressionstoremovefromthename. Spaces,tabsandlineendingsmaybeused
freelytovisuallyarrangethehspecificationi. Blanklinesarenotpermissible. This
commandmayonlybeusedinthepreamble.
\noinit{hregexpi}
Anynumberof\noinitcommandscanbegiveneachofwhichspecifiestoremove
thehregexpifromthecopyofthenamewhichtheinitialsgenerationsystemsees.
Sinceregularexpressionsusuallycontainspecialcharacters,itisbesttoenclosethem
intheprovided\regexpmacroasshown—thiswillpasstheexpressionthroughto
bibercorrectly.
Ifthereisno\DeclareNoinitspecification,biberwilldefaultto:
\DeclareNoinit{
% strip lowercase prefixes like 'al-' when generating initials from
,→ names
\noinit{\regexp{\b\p{Ll}{2}\p{Pd}}}
% strip some common diacritics when generating initials from names
\noinit{\regexp{[\x{2bf}\x{2018}]}}
}
Thisbiberdefaultstripsacoupleofdiacriticsandalsostripslowercaseprefixesfrom
namesbeforegeneratinginitials.
4.5.9 FineTuningSorting
Itcanbeusefultofinetunesortingsothatitignorescertainpartsofparticularfields.
\DeclareNosort{hspecificationi}
Definesregularexpressionstostripfromparticularfieldsortypesoffieldswhen
sorting. Thehspecificationiisanundelimitedlistof\nosortdirectiveswhichspecify
theregularexpressionstoremovefromparticularfieldsortypeoffield. Spaces,tabs
andlineendingsmaybeusedfreelytovisuallyarrangethehspecificationi. Blank
linesarenotpermissible. Thiscommandmayonlybeusedinthepreamble.
233

\nosort{hfieldordatafieldseti}{hregexpi}
Anynumberof\nosortcommandscanbegiveneachofwhichspecifiestoremovethe
hregexpifromthehfieldiorhdatafieldseti. Ahdatafieldsetiissimplyaconvenience
grouping of semantically similar fields from which you might want to remove a
regexp. See§4.5.2fortheavailablesets,theirmembersandcustomisation. Since
regular expressions usually contain special characters, it is best to enclose them
intheprovided\regexpmacroasshown—thiswillpasstheexpressionthroughto
bibercorrectly.
Thedefaultis:
\DeclareNosort{
% strip prefixes like 'al-' when sorting names
\nosort{setnames}{\regexp{\A\p{L}{2}\p{Pd}}}
% strip some diacritics when sorting names
\nosort{setnames}{\regexp{[\x{2bf}\x{2018}]}}
}
This biber default strips a couple of diacritics and also strips two-letter prefixes
(like“Al-”)fromnameswhensorting. Supposeyouwantedtoignore“The”atthe
beginningofthetitlefieldwhensorting:
\DeclareNosort{
\nosort{title}{\regexp{\AThe\s+}}
}
Orifyouwantedtoignore“The”atthebeginningofanytitlefield:
\DeclareNosort{
\nosort{settitles}{\regexp{\AThe\s+}}
}
4.5.10 FineTuninghashinganduniquename
\DeclareNonamestring{hspecificationi}
Defines regular expressions to strip from name fields when generating fullhash,
fullhashraw and uniquename. The hspecificationi is an undelimited list of
\nonamestring directives which specify the regular expressions to remove from
particularnamefields. Spaces,tabsandlineendingsmaybeusedfreelytovisually
arrangethehspecificationi. Blanklinesarenotpermissible. Thiscommandmayonly
beusedinthepreamble.
\nonamestring{hnamefieldordatafieldnameseti}{hregexpi}
Any number of \nonamestring commands can be given each of which spec-
ifies to remove the hregexpi from the hnamefieldi or hdatafieldnameseti. A
hdatafieldnamesetiissimplyaconveniencegroupingofsemanticallysimilarfields
fromwhichyoumightwanttoremovearegexp. See§4.5.2fortheavailablesets,their
membersandcustomisation. Onlysetofnamelistsarerelevanttothiscommand.
234

Sinceregularexpressionsusuallycontainspecialcharacters,itisbesttoenclosethem
intheprovided\regexpmacroasshown—thiswillpasstheexpressionthroughto
bibercorrectly.
Supposeyouwantedtoignoresquarebracketsinnamesintheauthornamefield
and treat ‘D[onald] Knuth’ the same as ‘Donald Knuth’ for purposes uniquename
andhashingsothatbothvariantsappearedtogetherinadashedbibliographystyle
andwerealsotreatedthesamewhencalculatinguniquename:
\DeclareNonamestring{
\nonamestring{author}{\regexp{[\[\]]}}
}
Forconsistency,itisoftendesirabletousethesameregexpin\DeclareNosort.
4.5.11 SpecialFields
Someoftheautomaticallygeneratedfieldsfrom§4.2.4.2maybecustomized.
\DeclareLabelname[hentrytype,…i]{hspecificationi}
Defines the fields to consider when generating the labelname field (see § 4.2.4.2).
Thehspecificationiisanorderedlistof\fieldcommands. Thefieldsarecheckedin
theorderlistedandthefirstfieldwhichisavailablewillbeusedaslabelname. This
isthedefaultdefinition:
\DeclareLabelname{%
\field{shortauthor}
\field{author}
\field{shorteditor}
\field{editor}
\field{translator}
}
Thelabelnamefieldmaybecustomizedgloballyoronaper-typebasis. Iftheoptional
hentrytypeiargumentisgiven,thespecificationappliestotherespectiveentrytype.
Ifnot,itisappliedglobally. Thehentrytypeiargumentmaybeacomma-separated
listofvalues. Thiscommandmayonlybeusedinthepreamble.
\DeclareLabeldate[hentrytype,…i]{hspecificationi}
Definesthedatecomponentstoconsiderwhengeneratinglabelyear,labelmonth,
labelday,labelendyear,labelendmonthandlabelenddayfields(see§4.2.4.2). The
hspecificationi is an ordered list of \field or \literal commands. The items are
checkedintheorderlistedandthefirstitemwhichisavailablewillbeusedtopopluate
thementionedfields. Notethatthe\fielditemsdonothavetobedatetype‘date’in
thedatamodelsothatyoucancreatepseudo-yearlabelsby,forexample,usinga
pubstatefieldcontents,ifavailable,astheyearlabelbydefining\DeclareLabeldate
suitably. Notealsothata\literalcommandwillalwaysbeusedwhenfoundandso
thisshouldalwaysbethelastthinginthelist. Ifthevalueofa\literalcommandisa
validlocalisationstring,thenthiswillberesolvedinthecurrentlanguage,otherwise
thevalueisusedasaliteralstringas-is. Thisisthedefaultdefinition:
235

\DeclareLabeldate{%
\field{date}
\field{year}
\field{eventdate}
\field{origdate}
\field{urldate}
\literal{nodate}
}
Notethatthedatefieldissplitbythebackendintoyear,monthwhicharealsovalid
fieldsinthedefaultdatamodel. Inordertosupportlegacydatawhichdirectlysets
yearand/ormonth,thespecification‘date’in\DeclareLabeldatewillalsomatch
yearandmonthfields,ifpresent. Thelabel*fieldsmaybecustomizedgloballyor
onaper-typebasis. Iftheoptionalhentrytypeiargumentisgiven,thespecification
applies to the respective entry type. If not, it is applied globally. The hentrytypei
argumentmaybeacomma-separatedlistofvalues. Thiscommandmayonlybeused
inthepreamble. Seealso§4.2.4.3.
\DeclareExtradate{hspecificationi}
Defineswhichdateinformationisusedtoconstructtheextradatefield. Withthe
default setting for \DeclareExtradateContext, this field (see § 4.2.4.2) is printed
todisambiguateworksbythesamelabelname(usuallytheauthor)orlabeltitle
(usually the main title) which occur in the same date scope. By default, the date
scopeistheyearandsotwoworksbythesameauthor/titlewithinthesameyear
willhavedifferentextradatevalueswhichareusedtodisambiguatetheworksin
the bibliography in the usual manner seen in many authoryear type styles. The
hspecificationiisoneormore\scopespecificationswhichcancontainoneormore
\fieldspecifications. Withina\scope,theexistenceofeach\fieldwillbechecked
andiffound,thefirst\fieldisusedandtherestareignored. Thisallowsafallback
incasecertainfieldsarenotavailableinallentries. All\scopesareusedtotrack
informationand\scopesshouldbespecifiedindecreasingorderofgenerality(e.g.
yearthenmonththendayetc)Thedefaultdefinitionis:
\DeclareExtradate{%
\scope{
\field{labelyear}
\field{year}
}
}
Thismeansthatthelabelyearfieldonly(oryearifthisdoesnotexist)willbeused
totrackworksbythesameauthor. Withthefollowingdatasourceentries:
@BOOK{extra1,
AUTHOR = {John Doe},
DATE = {2001-01}
}
@BOOK{extra2,
236

AUTHOR = {John Doe},
DATE = {2001-02}
}
Thedefaultdefinitionwouldresultin:
Doe 2001a
Doe 2001b
Here,extradateonlyconsidersthe((label)year)informationandsincethisisiden-
tical,disambiguationisrequired. However,considerthefollowingdefinition:
\DeclareExtradate{%
\scope{
\field{labelyear}
\field{year}
}
\scope{
\field{labelmonth}
}
}
Theresultwouldbe:
Doe 2001
Doe 2001
Ifonlyyearswereprinted,thiswouldbeambiguousbecauseextradatenowconsid-
erslabelmonthandsincethisdiffers,nodisambiguationisnecessary. Careshould
thereforebetakentosynchronisetheprintedinformationwiththeextradatedis-
ambiguationsettings. Noticethattheseconddefinitionis‘month-in-year’disam-
biguationandquitedifferentfrom:
\DeclareExtradate{%
\scope{
\field{labelmonth}
}
}
whichisjustplain‘month’disambiguationwhichisveryunlikelytobewhatyou
everwanttodosincethisdisambiguationonlybasedonmonthandignorestheyear
entirely. extradatecalculationshouldalmostalwaysbebasedonallinformation
downtotheresolutionyourequire. Forexample,ifyouwishtodisambiguateright
downtothehourlevel(perhapsusefulinlargebibliographiesofrapidlychanging
onlinematerial),youwouldspecifysomethinglikethis:
\DeclareExtradate{%
\scope{
237

\field{labelyear}
\field{year}
}
\scope{
\field{labelmonth}
}
\scope{
\field{labelday}
}
\scope{
\field{labelhour}
}
}
Entries without the specified granularity of information will disambiguate at the
lowestgranularitytheycontain,so,forexample,with:
\DeclareExtradate{%
\scope{
\field{labelyear}
\field{year}
}
\scope{
\field{labelmonth}
}
}
@BOOK{extra1,
AUTHOR = {John Doe},
DATE = {2001}
}
@BOOK{extra2,
AUTHOR = {John Doe},
DATE = {2001}
}
Theresultwouldstillbe:
Doe 2001a
Doe 2001b
Thiscommandmayonlybeusedinthepreamble.
\DeclareExtradateContext[hentrytype,…i]{hspecificationi}
Definesthecontextinwhichidenticaldates(asdeterminedby\DeclareExtradate)
aretrackedsothatextradatecanbeappendedfordisambiguationpurposes. Nor-
mallythiscontextistheauthornamesothatworksofthesamedatebythesame
author can be disambiguated in authoryear type styles. Often, when there is no
author,thetitleappearsintheauthorpositionandthetitleisusedasthecontextto
disambiguateinstead. Therefore,thedefaultdefinitionis:
238

\DeclareExtradateContext{%
\field{labelname}
\field{labeltitle}
}
Itisunlikelythatthiswillneedtobecustomisedfornormalusecases.
\DeclareLabeltitle[hentrytype,…i]{hspecificationi}
Definesthefieldstoconsiderwhengeneratingthelabeltitlefield(see§4.2.4.2).
Thehspecificationiisanorderedlistof\fieldcommands. Thefieldsarecheckedin
theorderlistedandthefirstfieldwhichisavailablewillbeusedaslabeltitle. This
isthedefaultdefinition:
\DeclareLabeltitle{%
\field{shorttitle}
\field{title}
}
The labeltitle field may be customized globally or on a per-type basis. If the
optionalhentrytypeiargumentisgiven,thespecificationappliestotherespective
entrytype. Ifnot,itisappliedglobally. Thehentrytypeiargumentmaybeacomma-
separatedlistofvalues. Thiscommandmayonlybeusedinthepreamble.
4.5.12 DataInheritance(crossref)
biber features a highly customizable cross-referencing mechanism with flexible
data inheritance rules. This sections deals with the configuration interface. See
appendixBforthedefaultconfiguration. Anoteonterminology: thechild ortarget
istheentrywiththecrossreffield,theparent orsource istheentrythecrossref
fieldpointsto. Thechildinheritsdatafromtheparent.
\DefaultInheritance[hexceptionsi]{hoptionsi}
Configures the default inheritance behavior. This command may only be used in
the preamble. The default behavior may be customized be setting the following
hoptionsi:
all=true,false default:true
Whetherornottoinheritallfieldsfromtheparentbydefault.
all=true means that the child entry inherits all fields from the parent, unless a
morespecificinheritancerulehasbeensetupwith\DeclareDataInheritance. Ifan
inheritanceruleisdefinedforafield,datainheritanceiscontrolledbythatrule. all=
falsemeansthatnodataisinheritedfromtheparentbydefaultandeachfieldtobe
inheritedrequiresanexplicitinheritancerulesetupwith\DeclareDataInheritance.
Thepackagedefaultisall=true.
override=true,false default:false
Whetherornottooverwritetargetfieldswithsourcefieldsifbotharedefined. This
appliesbothtoautomaticinheritanceandtoexplicitinheritancerules. Thepackage
defaultisoverride=false,i.e.,existingfieldsofthechildentryarenotoverwritten.
239

ignore=hcsvlistofuniquenessoptionsi
Thisoptiontakesacomma-separatedlistofoneofmoreof‘singletitle’,‘uniquetitle’,
‘uniquebaretitle’and/or‘uniquework’. Thepurposeofthisoptionistoignoretracking
informationforthesethreeoptionswhenthefieldwhichwouldtriggerthetracking
(table 6) is inherited. An example—Suppose that you have several @book entries
which all crossref a @mvbook from which they get their author field. You might
reasonablywantthe\ifsingletitletesttoreturn‘true’forthisauthorastheironly
‘work’ is the @mvbook. Similar comments would apply to situations involving the
\ifuniquetitle,\ifuniquebaretitleand\ifuniqueworktests. Theignoreoption
listswhichoftheseshouldhavetheirtrackinginformationignoredwhenthefields
whichwouldtriggerthemareinherited. Theideaisthatthepresenceofaninherited
fielddoesnotcontributetowardsthedeterminationofwhethersomecombination
ofname/titleisuniqueinthebibliographicdata. Forexample,thismodifieddefault
settingwouldignoresingletitleanduniquetitletracking:
\DefaultInheritance{ignore={singletitle,uniquetitle}, all=true,
,→ override=false}
Ofcourse,theignoringoftrackingdoesnothingifthefieldsinheriteddonotplaya
roleintracking. Onlythefieldslistedintable6arerelevanttothisoption.
Theoptionalhexceptionsiareanundelimitedlistof\exceptdirectives. Spaces,tabs,
andlineendingsmaybeusedfreelytovisuallyarrangethehexceptionsi. Blanklines
arenotpermissible.
\except{hsourcei}{htargeti}{hoptionsi}
Definesanexceptiontothedefaultinheritancerules.
\DeclareDataInheritancesetstheinheritancehoptionsiforaspecifichsourceiand
htargeticombination. Thehsourceiandhtargetiargumentsspecifytheparentand
the child entry type. The asterisk matches all types and is permissible in either
argument.
\DeclareDataInheritance[hoptionsi]{hsource,…i}{htarget,…i}{hrulesi}
Declaresinheritancerules. Thehsourceiandhtargetiargumentsspecifytheparent
and the child entry type. Either argument may be a single entry type, a comma-
separated list of types, or an asterisk. The asterisk matches all entry types. The
hrulesi are an undelimited list of \inherit and/or \noinherit directives. Spaces,
tabs,andlineendingsmaybeusedfreelytovisuallyarrangethehrulesi. Blanklines
arenotpermissible. Thiscommandmayonlybeusedinthepreamble. Theoptions
are:
ignore=hcsvlistofuniquenessoptionsi
As the ignore option on \DefaultInheritance explained above. When set here,
it takes precedence over any global options set with \DefaultInheritance. For
example, this would ignore singletitle and uniquetitle tracking for a @book
inheritingfroma@mvbook.
\DeclareDataInheritance[ignore={singletitle,uniquetitle}]{mvbook}{
,→ book}{...}
240

\inherit[hoptioni]{hsourcei}{htargeti}
Definesaninheritancerulebymappingahsourceifieldtoahtargetifield. hoptioni
canbeoneof
override=true,false default:false
Astheoverrideoptionfor\DefaultInheritanceexplainedabove. Whensethere,
ittakesprecedenceoveranyglobaloptionssetwith\DefaultInheritance.
\noinherit{hsourcei}
Unconditionallypreventsinheritanceofthehsourceifield.
\ResetDataInheritance Clearsallinheritancerulesdefinedwith\DeclareDataInheritance. Thiscom-
mandmayonlybeusedinthepreamble.
Herearesomepracticalexamples:
\DefaultInheritance{all=true,override=false}
Thisexampleshowshowtoconfigurethedefaultinheritancebehavior. Theabove
settingsarethepackagedefaults.
\DefaultInheritance[
\except{*}{online}{all=false}
]{all=true,override=false}
This example is similar to the one above but adds one exception: entries of type
@onlinewill,bydefault,notinheritanydatafromanyparent.
\DeclareDataInheritance{collection}{incollection}{
\inherit{title}{booktitle}
\inherit{subtitle}{booksubtitle}
\inherit{titleaddon}{booktitleaddon}
}
Sofar wehavelooked atsetting up standardinheritance. For example, all=true
means that the publisher field of a source entry is copied to the publisher field
of the target entry. In some cases, however, asymmetric mappings are required.
Theyaredefinedwith\DeclareDataInheritance. Theaboveexamplesetsupthree
typical rules for @incollection entries referencing a @collection. We map the
titleandrelatedfieldsofthesourcetothecorrespondingbooktitlefieldsofthe
target.
\DeclareDataInheritance{mvbook,book}{inbook,bookinbook}{
\inherit{author}{author}
\inherit{author}{bookauthor}
}
This rule is an example of one-to-many mapping: it maps the author field of the
sourcetoboththeauthorandthebookauthorfieldsofthetargetinordertoallow
forcompactinbook/bookinbookentries. Thesourcemaybeeithera@mvbookora
@bookentry,thetargeteitheran@inbookora@bookinbookentry.
241

\DeclareDataInheritance{*}{inbook,incollection}{
\noinherit{introduction}
}
Thisrulepreventsinheritanceoftheintroductionfield. Itappliestoalltargetsof
type@inbookor@incollection,regardlessofthesourceentrytype.
\DeclareDataInheritance{*}{*}{
\noinherit{abstract}
}
Thisrule,whichappliestoallentries,regardlessofthesourceandtargetentrytypes,
preventsinheritanceoftheabstractfield.
\DefaultInheritance{all=true,override=false}
\ResetDataInheritance
ThisexampledemonstrateshowtoemulatetraditionalBibTeX’scross-referencing
mechanism. Itenablesinheritancebydefault, disablesoverwriting, andclearsall
otherinheritancerulesandmappings.
Inabibliographyentry,youcangiveanoption‘noinherit’wherethevalueisa
datafieldsetdefinedwith\DeclareDatafieldSet(§4.5.2). Thiswillblockinheritance
ofthefieldsinthesetonaper-entrybasis. Forexample:
\DeclareDatafieldSet{nobtitle}{
\member[field=booktitle]
}
@INBOOK{s1,
OPTIONS = {noinherit=nobtitle},
TITLE = {Subtitle},
CROSSREF = {s2}
}
@BOOK{s2,
TITLE = {Title}
}
Here, s1 will not inherit the TITLE of s2 as BOOKTITLE as this is blocked by the
datafield set given as the value to the noinherit option. One important thing to
noteisthatchildrenwillneverinheritanydatepartsofagiventypeiftheyalready
containadatepartofthattype. So,forexample:
@INBOOK{b1,
DATE = {2004-03-03},
ORIGDATE = {2004-03},
CROSSREF = {b2}
}
242

@BOOK{b2,
DATE = {2004-03-03/2005-08-09},
ORIGDATE = {2004-03/2005-08},
EVENTDATE = {2004-03/2005-08},
}
Here, b1 will not inherit any of endyear, endmonth, endday, origendyear or
origendmonth as this would make a mess of its own dates. It will, given the in-
heritancedefaults,inheritalloftheevent*dateparts.
4.6 AuxiliaryCommands
Thefacilitiesinthissectionareintendedforanalyzingandsavingbibliographicdata
ratherthanformattingandprintingit.
4.6.1 DataCommands
Thecommandsinthissectiongrantlow-levelaccesstotheunformattedbibliographic
data. Theyarenotintendedfortypesettingbutratherforthingslikesavingdatatoa
temporarymacrosothatitmaybeusedinacomparisonlater.
\thefield{hfieldi}
Expandstotheunformattedhfieldi. Ifthehfieldiisundefined,thiscommandexpands
toanemptystring.
\strfield{hfieldi}
Similarto \thefield, exceptthat the field is automatically sanitizedsuch that its
valuemaysafelybeusedintheformationofacontrolsequencename.
\csfield{hfieldi}
Similarto\thefield,butpreventsexpansion.
\usefield{hcommandi}{hfieldi}
Executeshcommandiusingtheunformattedhfieldiasitsargument.
\thelist{hliterallisti}
Expands to the unformatted hliterallisti. If the list is undefined, this command
expandstoanemptystring. Notethatthiscommandwilldumpthehliterallistiin
theinternalformatusedbythispackage. Thisformatisnotsuitableforprinting.
\strlist{hliterallisti}
Similar to \thelist, except that the list internal representation is automatically
sanitizedsuchthatitsvaluemaysafelybeusedintheformationofacontrolsequence
name.
\thefirstlistitem{hliterallisti}
Expandstotheunformattedfirstiteminhliterallisti. Ifthehliterallistiisundefined,
thiscommandexpandstoanemptystring.
243

\strfirstlistitem{hliterallisti}
Similarto\thefirstlistitem,exceptthattheitemisautomaticallysanitizedsuch
thatitsvaluemaysafelybeusedintheformationofacontrolsequencename.
\usefirstlistitem{hcommandi}{hliterallisti}
Executeshcommandiusingtheunformattedfirstitemofhliterallistiasitsargument.
\thename{hnamelisti}
Expands to the unformatted hnamelisti. If the list is undefined, this command
expandstoanemptystring. Notethatthiscommandwilldumpthehnamelistiin
theinternalformatusedbythispackage. Thisformatisnotsuitableforprinting.
\strname{hnamelisti}
Similarto\thename,exceptthatthenameinternalrepresentationisautomatically
sanitizedsuchthatitsvaluemaysafelybeusedintheformationofacontrolsequence
name.
\savefield{hfieldi}{hmacroi}
\savefield*{hfieldi}{hmacroi}
Copiesanunformattedhfielditoa hmacroi. Theregularvariantofthiscommand
definesthehmacroiglobally,thestarredoneworkslocally.
\savelist{hliterallisti}{hmacroi}
\savelist*{hliterallisti}{hmacroi}
Copiesanunformattedhliterallistitoahmacroi. Theregularvariantofthiscommand
definesthehmacroiglobally,thestarredoneworkslocally.
\savename{hnamelisti}{hmacroi}
\savename*{hnamelisti}{hmacroi}
Copiesanunformattedhnamelistitoahmacroi. Theregularvariantofthiscommand
definesthehmacroiglobally,thestarredoneworkslocally.
\savefieldcs{hfieldi}{hcsnamei}
\savefieldcs*{hfieldi}{hcsnamei}
Similar to \savefield, but takes the control sequence name hcsnamei (without a
leadingbackslash)asanargument,ratherthanamacroname.
\savelistcs{hliterallisti}{hcsnamei}
\savelistcs*{hliterallisti}{hcsnamei}
Similar to \savelist, but takes the control sequence name hcsnamei (without a
leadingbackslash)asanargument,ratherthanamacroname.
\savenamecs{hnamelisti}{hcsnamei}
\savenamecs*{hnamelisti}{hcsnamei}
Similar to \savename, but takes the control sequence name hcsnamei (without a
leadingbackslash)asanargument,ratherthanamacroname.
244

\restorefield{hfieldi}{hmacroi}
Restores a hfieldi from a hmacroi defined with \savefield before. The field is re-
storedwithinalocalscope.
\restorelist{hliterallisti}{hmacroi}
Restores a hliterallisti from a hmacroi defined with \savelist before. The list is
restoredwithinalocalscope.
\restorename{hnamelisti}{hmacroi}
Restores a hnamelisti from a hmacroi defined with \savename before. The list is
restoredwithinalocalscope.
\clearfield{hfieldi}
Clearsthehfieldiwithinalocalscope. Afieldclearedthiswayistreatedasundefined
bysubsequentdatacommands.
\clearlist{hliterallisti}
Clears the hliterallisti within a local scope. A list cleared this way is treated as
undefinedbysubsequentdatacommands.
\clearname{hnamelisti}
Clears the hnamelisti within a local scope. A list cleared this way is treated as
undefinedbysubsequentdatacommands.
4.6.2 Stand-aloneTests
The commands in this section are various kinds of stand-alone tests for use in
bibliographyandcitationstyles.
\if<datetype>julian{htruei}{hfalsei}
Expands to htruei if the date ‘datetype’date (date, urldate, eventdate etc.) Was
convertedtotheJulianCalendarduetothesettingsofthejulianandgregorianstart
options.
\ifdatejulian{htruei}{hfalsei}
As \if<datetype>julian but for use in \mkbibdate* formatting commands
(§4.10.2)insidewhichtheappropriate\if<datetype>juliancommandisaliased
tothiscommand.
\if<datetype>dateera{herai}{htruei}{hfalsei}
Expandstohtrueiifthedate‘datetype’date(date,urldate,eventdateetc.) hasan
eraspecificationequaltoheraiandhfalseiotherwise. Thesupportedheraistrings
whichbiberdeterminesandpassesinthe.bblare:
bceBCE/BCera
ceCE/ADera
This command is useful for determining whether to print the location strings in
§4.9.2.21.
245

\ifdateera{herai}{htruei}{hfalsei}
As \if<datetype>dateera but for use in \mkbibdate* formatting commands
(§4.10.2)insidewhichtheappropriate\if<datetype>dateeracommandisaliased
tothiscommand.
\if<datetype>datecirca{htruei}{hfalsei}
Expandstohtrueiifthedate‘datetype’date(date, urldate, eventdateetc.) hada
‘circa’ marker in the source and hfalsei otherwise. See § 2.3.8. This command is
usefulfordeterminingwhethertoprintthelocationstringsin§4.9.2.21.
\ifdatecirca{htruei}{hfalsei}
As \if<datetype>datecirca but for use in \mkbibdate* formatting commands
(§ 4.10.2) inside which the appropriate \if<datetype>datecirca command is
aliasedtothiscommand.
\if<datetype>dateuncertain{htruei}{hfalsei}
Expandstohtrueiifthedate‘datetype’date(date,urldate,eventdateetc.) hadan
uncertaintymarkerinthesourceandhfalseiotherwise. See§2.3.8. Thiscommand
isusefulfordeterminingwhethertoprint,forexample,aquestionmarkafterayear.
\ifdateuncertain{htruei}{hfalsei}
As \if<datetype>dateuncertain but for use in \mkbibdate* formatting com-
mands(§4.10.2)insidewhichtheappropriate\if<datetype>dateuncertaincom-
mandisaliasedtothiscommand.
\ifenddateuncertain{htruei}{hfalsei}
As\ifend<datetype>dateuncertainbutforusein\mkbibdate*formattingcom-
mands(§4.10.2)insidewhichtheappropriate\ifend<datetype>dateuncertain
commandisaliasedtothiscommand.
\if<datetype>dateunknown{htruei}{hfalsei}
Expandstohtrueiifthedate‘datetype’date(date,urldate,eventdateetc.) ismarked
asunknown(asopposedtoopen)inthesourceandhfalseiotherwise. See§2.3.8.
\ifdateunknown{htruei}{hfalsei}
As\if<datetype>dateunknownbutforusein\mkbibdate*formattingcommands
(§ 4.10.2) inside which the appropriate \if<datetype>dateunknown command is
aliasedtothiscommand.
\ifenddateunknown{htruei}{hfalsei}
As \ifend<datetype>dateunknown but for use in \mkbibdate* formatting com-
mands(§4.10.2)insidewhichtheappropriate\ifend<datetype>dateunknowncom-
mandisaliasedtothiscommand.
\iflabeldateisdate{htruei}{hfalsei}
Expandstohtrueiiflabeldateisdefinedandwasobtainedfromdate,andtohfalsei
otherwise.
246

\ifdatehasyearonlyprecision{hdatetypei}{htruei}{hfalsei}
Expands to htruei if the hdatetypeidate is defined and would be shown with year
precision\print<datetype>date,andtofalseotherwise.
\ifdatehastime{hdatetypei}{htruei}{hfalsei}
Expands to htruei if the hdatetypeidate is defined, has a time component and
<datetype>dateusetimeistrue,andtofalseotherwise.
\ifdateshavedifferentprecision{hdatetype1i}{hdatetype2i}{htruei}{hfalsei}
Expands to htruei if the two dates hdatetype1i and hdatetype2i would
show in different precision when printed with \print<datetype1>date and
\print<datetype2>daterespectively,andtohfalseiotherwise.
\ifdateyearsequal{hdatetype1i}{hdatetype2i}{htruei}{hfalsei}
Expandstohtrueiifthetwodateshdatetype1iandhdatetype2ihavethesameyear
andera. Sincethesignofthedateissavedintheerafield,yearsshouldbecompared
usingthiscommandtoavoidconfusionwhenthetwoyearshaveoppositesigns
\ifdatesequal{hdatetype1i}{hdatetype2i}{htruei}{hfalsei}
Expandstohtrueiifthetwodateshdatetype1iandhdatetype2iarethesame. Here
hdatetype2imaybethe‘end’bitofhdatetype1i(orviceversa).
\ifdaterangesequal{hdatetype1i}{hdatetype2i}{htruei}{hfalsei}
Expands to htruei if the two date ranges—that is the start and the end
date—hdatetype1iandhdatetype2iarethesame.
\ifcaselang[hlanguagei]{htruei}{hfalsei}
Expands to htruei if the optional hlanguagei is one of those declared by
\DeclareCaseLangs (see § 4.6.4) and to hfalsei otherwise. Without the optional
argument,checksthecurrentvalueof\currentlang.
\ifsortingnamekeytemplatename{hstringi}{htruei}{hfalsei}
Expandstohtrueiifthehstringiisequaltothecurrentinscopesortingnamekey
templatename(see4.5.6),andtohfalseiotherwise.
\ifuniquenametemplatename{hstringi}{htruei}{hfalsei}
Expandstohtrueiifthehstringiisequaltothecurrentinscopeuniquenessname
keytemplatename(see4.5.6),andtohfalseiotherwise.
\iflabelalphanametemplatename{hstringi}{htruei}{hfalsei}
Expandstohtrueiifthehstringiisequaltothecurrentinscopealphabeticlabelname
templatename(see4.5.6),andtohfalseiotherwise.
\ifnamehashtemplatename{hstringi}{htruei}{hfalsei}
Expandstohtrueiifthehstringiisequaltothecurrentinscopenamehashtemplate
name(see4.11.5),andtohfalseiotherwise.
247

\iffieldundef{hfieldi}{htruei}{hfalsei}
Expandstohtrueiifthehfieldiisundefined,andtohfalseiotherwise.
\iflistundef{hliterallisti}{htruei}{hfalsei}
Expandstohtrueiifthehliterallistiisundefined,andtohfalseiotherwise.
\ifnameundef{hnamelisti}{htruei}{hfalsei}
Expandstohtrueiifthehnamelistiisundefined,andtohfalseiotherwise.
\iffieldsequal{hfield1i}{hfield2i}{htruei}{hfalsei}
Expands to htruei if the values of hfield1i and hfield2i are equal, and to hfalsei
otherwise.
\iflistsequal{hliterallist1i}{hliterallist2i}{htruei}{hfalsei}
Expandstohtrueiifthevaluesofhliterallist1iandhliterallist2iareequal,andto
hfalseiotherwise.
\ifnamesequal{hnamelist1i}{hnamelist2i}{htruei}{hfalsei}
Expands to htruei if the values of hnamelist1i and hnamelist2i are equal, and to
hfalseiotherwise.
\iffieldequals{hfieldi}{hmacroi}{htruei}{hfalsei}
Expandstohtrueiifthevalueofthehfieldiisequaltothedefinitionofhmacroi,and
tohfalseiotherwise.
\iflistequals{hliterallisti}{hmacroi}{htruei}{hfalsei}
Expandstohtrueiifthevalueofthehliterallistiisequaltothedefinitionofhmacroi,
andtohfalseiotherwise.
\ifnameequals{hnamelisti}{hmacroi}{htruei}{hfalsei}
Expandstohtrueiifthevalueofthehnamelistiisequaltothedefinitionofhmacroi,
andtohfalseiotherwise.
\iffieldequalcs{hfieldi}{hcsnamei}{htruei}{hfalsei}
Similarto\iffieldequalsbuttakesthecontrolsequencenamehcsnamei(without
aleadingbackslash)asanargument,ratherthanamacroname.
\iflistequalcs{hliterallisti}{hcsnamei}{htruei}{hfalsei}
Similarto\iflistequalsbuttakesthecontrolsequencenamehcsnamei(withouta
leadingbackslash)asanargument,ratherthanamacroname.
\ifnameequalcs{hnamelisti}{hcsnamei}{htruei}{hfalsei}
Similarto\ifnameequalsbuttakesthecontrolsequencenamehcsnamei(withouta
leadingbackslash)asanargument,ratherthanamacroname.
\iffieldequalstr{hfieldi}{hstringi}{htruei}{hfalsei}
Executeshtrueiifthevalueofthehfieldiisequaltohstringi,andhfalseiotherwise.
Thiscommandisrobust.
248

\iffieldxref{hfieldi}{htruei}{hfalsei}
Ifthecrossref/xreffieldofanentryisdefined,thiscommandchecksifthehfieldi
is related to the cross-referenced parent entry. It executes htruei if the hfieldi of
thechildentryisequaltothecorrespondinghfieldioftheparententry,andhfalsei
otherwise. Ifthecrossref/xreffieldisundefined,italwaysexecuteshfalsei. This
commandisrobust. Seethedescriptionofthecrossrefandxreffieldsin§2.2.3as
wellas§2.4.1forfurtherinformationconcerningcross-referencing.
\iflistxref{hliterallisti}{htruei}{hfalsei}
Similarto\iffieldxrefbutchecksifahliterallistiisrelatedtothecross-referenced
parententry. Seethedescriptionofthecrossrefandxreffieldsin§2.2.3aswellas
§2.4.1forfurtherinformationconcerningcross-referencing.
\ifnamexref{hnamelisti}{htruei}{hfalsei}
Similarto\iffieldxrefbutchecksifahnamelistiisrelatedtothecross-referenced
parententry. Seethedescriptionofthecrossrefandxreffieldsin§2.2.3aswellas
§2.4.1forfurtherinformationconcerningcross-referencing.
\ifcurrentfield{hfieldi}{htruei}{hfalsei}
Executeshtrueiifthecurrentfieldishfieldi,andhfalseiotherwise. Thiscommand
isrobust. Itisintendedforuseinfieldformattingdirectivesandalwaysexecutes
hfalseiwhenusedinanyothercontext.
\ifcurrentlist{hliterallisti}{htruei}{hfalsei}
Executeshtrueiifthecurrentlistishliterallisti,andhfalseiotherwise. Thiscommand
is robust. It is intended for use in list formatting directives and always executes
hfalseiwhenusedinanyothercontext.
\ifcurrentname{hnamelisti}{htruei}{hfalsei}
Executeshtrueiifthecurrentlistishnamelisti,andhfalseiotherwise. Thiscommand
is robust. It is intended for use in list formatting directives and always executes
hfalseiwhenusedinanyothercontext.
\ifuseprefix{htruei}{hfalsei}
Expandstohtrueiiftheuseprefixoptionisenabled(eithergloballyorforthecurrent
entry),andhfalseiotherwise. See§3.1.3fordetailsonthisoption.
\ifuseauthor{htruei}{hfalsei}
Thisisjustaparticularcaseofthe\ifuse<name>macrobelowbutismentioned
hereasauthorispartofthedefaultdatamodel. Expandstohtrueiiftheuseauthor
optionisenabled(eithergloballyorforthecurrententry),andhfalseiotherwise. See
§3.1.3fordetailsonthisoption.
\ifuseeditor{htruei}{hfalsei}
Thisisjustaparticularcaseofthe\ifuse<name>macrobelowbutismentioned
hereaseditorispartofthedefaultdatamodel. Expandstohtrueiiftheuseeditor
optionisenabled(eithergloballyorforthecurrententry),andhfalseiotherwise. See
§3.1.3fordetailsonthisoption.
249

\ifusetranslator{htruei}{hfalsei}
Thisisjustaparticularcaseofthe\ifuse<name>macrobelowbutismentioned
here as translator is part of the default data model. Expands to htruei if the
usetranslator option is enabled (either globally or for the current entry), and
hfalseiotherwise. See§3.1.3fordetailsonthisoption.
\ifuse<name>{htruei}{hfalsei}
Expands to htruei if the use<name> option is enabled (either globally or for the
currententry),andhfalseiotherwise. See§3.1.3fordetailsonthisoption.
\ifcrossrefsource{htruei}{hfalsei}
Expandstohtrueiiftheentrywasincludedinthe.bblduetobeingreferencedmore
thanmincrossrefstimesandfalseotherwise. See§3.1.2.1. Alsoexpandstofalseif
theentrywasdirectlycited.
\ifxrefsource{htruei}{hfalsei}
Expandstohtrueiiftheentrywasincludedinthe.bblduetobeingreferencedmore
thanminxrefstimesandfalseotherwise. See§3.1.2.1. Alsoexpandstofalseifthe
entrywasdirectlycited.
\ifsingletitle{htruei}{hfalsei}
Expandstohtrueiifthereisonlyoneworkbythelabelnamenameinthebibliography,
andtohfalseiotherwise. Iflabelnameisnotsetforanentry,thiswillalwaysexpand
to hfalsei. Note that this feature needs to be enabled explicitly with the package
optionsingletitle.
\ifnocite{htruei}{hfalsei}
Expandstohtrueiiftheentrywas only includedinthe .bblvia\nocite. Thatis,
returnshfalseiifanentrywasboth\nocite’dand\cite’d.
\ifuniquetitle{htruei}{hfalsei}
Expandstohtrueiifthereisonlyoneworkwiththetitlelabeltitleandtohfalsei
otherwise. Iflabeltitleisnotsetforanentry,thiswillalwaysexpandtohfalsei.
Note that this feature needs to be enabled explicitly with the package option
uniquetitle.
\ifuniquebaretitle{htruei}{hfalsei}
Expandstohtrueiiflabelnameisemptyandthereisonlyoneworkwiththetitle
labeltitleandtohfalseiotherwise. Iflabeltitleisnotsetforanentry,thiswill
alwaysexpandtohfalsei. Notethatthisfeatureneedstobeenabledexplicitlywith
thepackageoptionuniquebaretitle.
\ifuniquework{htruei}{hfalsei}
Expands to htruei if there is only one work by the labelname name with the
labeltitletitleinthebibliography,andtohfalseiotherwise. Ifneitherlabelname
norlabeltitlearesetforanentry,thiswillalwaysexpandtohfalsei. Notethatthis
featureneedstobeenabledexplicitlywiththepackageoptionuniquework. Ifboth
singletitle and uniquetitle are false for the same entry, this could be because
250

anotherentryhasthesamelabdlnameandyetanother,different,entryhasthesame
labeltitle. uniqueworkwouldletyouknowthatthereisanotherentrythathas
both thesamelabelnameand thesamelabeltitle. Thiscouldbehelpfulincases
wheremultiplepeoplemaintainbibliographydatasourcesandthereisariskofadding
thesameworkwithdifferentkeyswithoutotherpartiesrealisingthis. Thistestcould
helptofindsuchduplicates.
\ifuniqueprimaryauthor{htruei}{hfalsei}
Expandstohtrueiiftheprimary(first)authornameoflabelnameisuniqueinthe
bibliography list and to hfalsei otherwise. This effectively answers the question
‘is there more than one author with the same base name’. The base name parts
aredefinedby\DeclareUniquenameTemplatesee§4.11.4. Thisisrequiredbysome
styles(e.g. APA)whichmandatesprimaryauthordisambiguationonlyandonlyif
thereare(different)primaryauthorswiththesamefamilyname. Iflabelnameisnot
setforanentry,thiswillalwaysexpandtohfalsei. Notethatthisfeatureneedstobe
enabledexplicitlywiththepackageoptionuniqueprimaryauthor.
\ifandothers{hlisti}{htruei}{hfalsei}
Expandstohtrueiifthehlistiisdefinedandhasbeentruncatedinthebibfilewith
thekeyword‘and others’,andtohfalseiotherwise. Thehlistimaybealiterallist
oranamelist.
\ifmorenames{htruei}{hfalsei}
Expandstohtrueiifthecurrentnamelisthasbeenorwillbetruncated,andtohfalsei
otherwise. Thiscommandisintendedforuseinformattingdirectivesfornamelists.
Itwillalwaysexpandtohfalseiwhenusedelsewhere. Thiscommandperformsthe
equivalentofan\ifandotherstestforthecurrentlist. Ifthistestisnegative,italso
checks if the listtotal counter is larger than liststop. This command may be
usedinaformattingdirectivetodecideifanotesuchas“andothers”or“etal.” isto
beprintedattheendofthelist. Notethatyoustillneedtocheckwhetheryouarein
themiddleorattheendofthelist,i.e.,whetherlistcountissmallerthanorequal
toliststop,see§4.4.1fordetails.
\ifmoreitems{htruei}{hfalsei}
This command is similar to \ifmorenames but checks the current literal list. It is
intended for use in formatting directives for literal lists. It will always expand to
hfalseiwhenusedelsewhere.
\if<namepart>inits{htruei}{hfalsei}
Expandstohtrueiorhfalsei,dependingonthestateofthe<namepart>initspack-
ageoption(see§3.1.2.3). Thiscommandisintendedforuseinformattingdirectives
fornamelists.
\ifterseinits{htruei}{hfalsei}
Expands to htruei or hfalsei, depending on the state of the terseinits package
option(see§3.1.2.3). Thiscommandisintendedforuseinformattingdirectivesfor
namelists.
251

\ifentrytype{htypei}{htruei}{hfalsei}
Executes htruei if the entry type of the entry currently being processed is htypei,
andhfalseiotherwise.
\ifkeyword{hkeywordi}{htruei}{hfalsei}
Executeshtrueiifthehkeywordiisfoundinthekeywordsfieldoftheentrycurrently
beingprocessed,andhfalseiotherwise.
\ifentrykeyword{hentrykeyi}{hkeywordi}{htruei}{hfalsei}
Avariantof\ifkeywordwhichtakesanentrykeyasitsfirstargument. Thisisuseful
fortestinganentryotherthantheonecurrentlyprocessed. Auser-facingversionof
thiscommandisavailableforuseindocumentssee§3.11.
\ifcategory{hcategoryi}{htruei}{hfalsei}
Executes htruei if the entry currently being processed has been assigned to a
hcategoryiwith\addtocategory,andhfalseiotherwise.
\ifentrycategory{hentrykeyi}{hcategoryi}{htruei}{hfalsei}
A variant of \ifcategory which takes an entry key as its first argument. This is
usefulfor testing anentry other than theone currentlyprocessed. A user-facing
versionofthiscommandisavailableforuseindocumentssee§3.11
\ifciteseen{htruei}{hfalsei}
Executes htruei if the entry currently being processed has been cited before, and
hfalseiotherwise. Thiscommandisrobustandintendedforuseincitationstyles.
If there are any refsection environments in the document, the citation tracking
islocaltotheseenvironments. Notethatthecitationtrackerneedstobeenabled
explicitlywiththepackageoptioncitetracker. Thebehaviorofthistestdepends
onthemodethecitationtrackerisoperatingin,see§3.1.2.3fordetails. Ifthecitation
tracker is disabled, the test always yields hfalsei. Also see the \citetrackertrue
and\citetrackerfalseswitchesin§4.6.4.
\ifentryseen{hentrykeyi}{htruei}{hfalsei}
Avariantof\ifciteseenwhichtakesanentrykeyasitsfirstargument. Sincethe
hentrykeyiisexpandedpriortoperformingthetest,itispossibletotestforentry
keysinafieldsuchasxref:
\ifentryseen{\thefield{xref}}{true}{false}
Apart from the additional argument, \ifentryseen behaves like \ifciteseen. A
user-facingversionofthiscommandisavailableforuseindocumentssee§3.11.
\ifentryinbib{hentrykeyi}{htruei}{hfalsei}
Executes htruei if the entry hentrykeyi appears in the current bibliography, and
hfalsei otherwise. A user-facing version of this command is available for use in
documentssee§3.11.
252

\iffirstcitekey{htruei}{hfalsei}
Executes htruei if the entry currently being processed is the first one in the cita-
tionlist,andhfalseiotherwise. Thiscommandreliesonthecitecount,citetotal,
multicitecountandmulticitetotalcounters(§4.10.5)andthusisintendedforuse
onlyinthehloopcodeiofacitationcommanddefinedwith\DeclareCiteCommand.
\iflastcitekey{htruei}{hfalsei}
Similar\iffirstcitekey,butexecuteshtrueiiftheentrycurrentlybeingprocessed
isthelastoneinthecitationlist,andhfalseiotherwise.
\ifciteibid{htruei}{hfalsei}
Expandstohtrueiiftheentrycurrentlybeingprocessedisthesameasthelastone,
andtohfalseiotherwise. Thiscommandisintendedforuseincitationstyles. Ifthere
are any refsection environments in the document, the tracking is local to these
environments. Note that the ‘ibidem’ tracker needs to be enabled explicitly with
the package option ibidtracker. The behavior of this test depends on the mode
the tracker is operating in, see § 3.1.2.3 for details. If the tracker is disabled, the
testalwaysyieldshfalsei. Alsoseethe\citetrackertrueand\citetrackerfalse
switchesin§4.6.4.
\ifciteidem{htruei}{hfalsei}
Expandstohtrueiiftheprimaryname(i.e.,theauthororeditor)intheentrycurrently
beingprocessedisthesameasthelastone,andtohfalseiotherwise. Thiscommand
isintendedforuseincitationstyles. Ifthereareanyrefsectionenvironmentsinthe
document,thetrackingislocaltotheseenvironments. Notethatthe‘idem’tracker
needstobeenabledexplicitlywiththepackageoptionidemtracker. Thebehavior
ofthistestdependsonthemodethetrackerisoperatingin,see§3.1.2.3fordetails.
Ifthetrackerisdisabled,thetestalwaysyieldshfalsei. Alsosee\citetrackertrue
and\citetrackerfalsein§4.6.4.
\ifopcit{htruei}{hfalsei}
This command is similar to \ifciteibid except that it expands to htruei if the
entrycurrentlybeingprocessedisthesameasthelastonebythisauthororeditor.
Notethatthe‘opcit’trackerneedstobeenabledexplicitlywiththepackageoption
opcittracker. Thebehaviorofthistestdependsonthemodethetrackerisoperating
in,see§3.1.2.3fordetails. Ifthetrackerisdisabled,thetestalwaysyieldshfalsei.
Alsoseethe\citetrackertrueand\citetrackerfalseswitchesin§4.6.4.
\ifloccit{htruei}{hfalsei}
This command is similar to \ifopcit except that it also compares the hpostnotei
argumentsandexpandstohtrueionlyiftheymatchandarenumerical(inthesenseof
\ifnumeralsfrom§4.6.2),i.e.,\ifloccitwillyieldtrueifthecitationreferstothe
samepagecitedbefore. Notethatthe‘loccit’trackerneedstobeenabledexplicitly
withthepackageoptionloccittracker. Thebehaviorofthistestdependsonthe
modethetrackerisoperatingin,see§3.1.2.3fordetails. Ifthetrackerisdisabled,the
testalwaysyieldshfalsei. Alsoseethe\citetrackertrueand\citetrackerfalse
switchesin§4.6.4.
253

\iffirstonpage{htruei}{hfalsei}
Thebehaviorofthiscommandisresponsivetothepackageoptionpagetracker. If
theoptionissettopage,itexpandstohtrueiifthecurrentitemisthefirstoneonthe
page,andtohfalseiotherwise. Iftheoptionissettospread,itexpandstohtrueiif
thecurrentitemisthefirstoneonthedouble-pagespread,andtohfalseiotherwise.
If the page tracker is disabled, this test always yields hfalsei. Depending on the
context,the‘item’maybeacitationoranentryinthebibliographyorabibliography
list. Notethatthistestdistinguishesbetweenbodytextandfootnotes. Forexample,
if used in the first footnote on a page, it will expand to htruei even if there is a
citationinthebodytextpriortothefootnote. Alsoseethe\pagetrackertrueand
\pagetrackerfalseswitchesin§4.6.4.
\ifsamepage{hinstance1i}{hinstance2i}{htruei}{hfalsei}
This command expands to htruei if two instances of a reference are located on
the same page or double-page spread, and to hfalsei otherwise. An instance of a
reference may be a citation or an entry in the bibliography or a bibliography list.
Theseinstancesareidentifiedbythevalueoftheinstcountcounter,see§4.10.5. The
behaviorofthiscommandisresponsivetothepackageoptionpagetracker. Ifthis
optionissettospread,\ifsamepageisinfactan‘ifsamespread’test. Ifthepage
trackerisdisabled,thistestalwaysyieldshfalsei. Theargumentshinstance1iand
hinstance2iaretreatedasintegerexpressionsinthesenseofe-TeX’s\numexpr. This
impliesthatitispossibletomakecalculationswithinthesearguments,forexample:
\ifsamepage{\value{instcount}}{\value{instcount}-1}{true}{false}
Note that \value is not prefixed by \the and that the subtraction is included in
the second argument in the above example. If hinstance1i or hinstance2i is an
invalid number (for example, a negative one), the test yields hfalsei. Also note
that this test does not distinguish between body text and footnotes. Also see the
\pagetrackertrueand\pagetrackerfalseswitchesin§4.6.4.
\ifinteger{hstringi}{htruei}{hfalsei}
Executes htruei if the hstringi is a positive integer, and hfalsei otherwise. This
commandisrobust.
\hascomputableequivalent{hstringi}{htruei}{hfalsei}
ExecuteshtrueiifthehstringicanbetransformedintoaLaTeX-computableinteger
consisting only of us-ascii characters via \getcomputableequivalent and hfalsei
otherwise. The mapping from non-us-ascii to us-ascii numerals will usually be
giveninthelbxfile.
\ifiscomputable{hstringi}{htruei}{hfalsei}
Returns htruei if \ifinteger or \hascomputableequivalent retrurns htruei on
hstringiandhfalseiotherwise.
\getcomputableequivalent{hstringi}{hmacroi}
Savestheus-asciirepresentationofthenumbergivenashstringiinhmacroi.
254

\ifnumeral{hstringi}{htruei}{hfalsei}
ExecuteshtrueiifthehstringiisanArabicorRomannumeral,andhfalseiotherwise.
Thiscommandisrobust. Seealso\DeclareNumCharsand\NumCheckSetupin§4.6.4.
\ifnumerals{hstringi}{htruei}{hfalsei}
Executes htruei if the hstringi is a range or a list of Arabic or Roman numerals,
and hfalsei otherwise. This command is robust. In contrast to \ifnumeral, it
will also execute htruei with arguments like “52–58”, “14/15”, “1, 3, 5”, and so
on. See also \DeclareNumChars, \DeclareRangeChars, \DeclareRangeCommands,
\NumCheckSetup,and\NumsCheckSetupin§4.6.4.
\ifpages{hstringi}{htruei}{hfalsei}
Similar to \ifnumerals, but also considers \DeclarePageCommands and
\PagesCheckSetupfrom§4.6.4.
\iffieldint{hfieldi}{htruei}{hfalsei}
Similarto\ifinteger,butusesthevalueofahfieldiratherthanaliteralstringin
thetest. Ifthehfieldiisundefined,itexecuteshfalsei.
\fieldhascomputableequivalent{hfieldi}{htruei}{hfalsei}
Similarto\hascomputableequivalent,butusesthevalueofahfieldiratherthana
literalstringinthetest. Ifthehfieldiisundefined,itexecuteshfalsei.
\iffieldiscomputable{hfieldi}{htruei}{hfalsei}
Similarto\ifiscomputable,butusesthevalueofahfieldiratherthanaliteralstring
inthetest. Ifthehfieldiisundefined,itexecuteshfalsei.
\iffieldnum{hfieldi}{htruei}{hfalsei}
Similarto\ifnumeral,butusesthevalueofahfieldiratherthanaliteralstringin
thetest. Ifthehfieldiisundefined,itexecuteshfalsei.
\iffieldnums{hfieldi}{htruei}{hfalsei}
Similarto\ifnumerals,butusesthevalueofahfieldiratherthanaliteralstringin
thetest. Ifthehfieldiisundefined,itexecuteshfalsei.
\iffieldpages{hfieldi}{htruei}{hfalsei}
Similarto\ifpages,butusesthevalueofahfieldiratherthanaliteralstringinthe
test. Ifthehfieldiisundefined,itexecuteshfalsei.
\ifbibstring{hstringi}{htruei}{hfalsei}
Expandstohtrueiifthehstringiisaknownlocalisationkey,andtohfalseiotherwise.
Thelocalisationkeysdefinedbydefaultarelistedin§4.9.2. Newonesmaybedefined
with\NewBibliographyString.
\ifbibxstring{hstringi}{htruei}{hfalsei}
Similarto\ifbibstring,butthehstringiisexpanded.
255

\iffieldbibstring{hfieldi}{htruei}{hfalsei}
Similarto\ifbibstring,butusesthevalueofahfieldiratherthanaliteralstringin
thetest. Ifthehfieldiisundefined,itexpandstohfalsei.
\iffieldplusstringbibstring{hfieldi}{hstringi}{htruei}{hfalsei}
Similarto\iffieldbibstring,butappendshstringitothevalueofhfieldiandchecks
if the resulting string is a known localisation key. Expands to hfalsei if hfieldi is
undefined.
\ifdriver{hentrytypei}{htruei}{hfalsei}
Expandstohtrueiifadriverforthehentrytypeiisavailable,andtohfalseiotherwise.
\ifcapital{htruei}{hfalsei}
Executes htruei if biblatex’s punctuation tracker would capitalize a localisation
stringatthecurrentlocation,andhfalseiotherwise. Thiscommandisrobust. Itmay
be useful for conditional capitalization of certain parts of a name in a formatting
directive.
\ifcitation{htruei}{hfalsei}
Expandstohtrueiwhenlocatedinacitation,andtohfalseiotherwise. Notethatthis
commandisresponsivetotheoutermostcontextinwhichitisused. Forexample,if
acitationcommanddefinedwith\DeclareCiteCommandexecutesadriverdefined
with\DeclareBibliographyDriver,any\ifcitationtestsinthedrivercodewill
yieldhtruei. See§4.11.7forapracticalexample.
\ifvolcite{htruei}{hfalsei}
Expandstohtrueiwhenlocatedin\volciteorarelatedcitationcommand(§3.9.6),
andtohfalseiotherwise.
\ifbibliography{htruei}{hfalsei}
Expands to htruei when located in a bibliography, and to hfalsei otherwise. Note
thatthiscommandisresponsivetotheoutermostcontextinwhichitisused. For
example,ifadriverdefinedwith\DeclareBibliographyDriverexecutesacitation
command defined with \DeclareCiteCommand, any \ifbibliography tests in the
citationcodewillyieldhtruei. See§4.11.7forapracticalexample.
\ifnatbibmode{htruei}{hfalsei}
Expandstohtrueiorhfalseidependingonthenatbiboptionfrom§3.1.1.
\ifciteindex{htruei}{hfalsei}
Expandstohtrueiorhfalseidependingontheindexingoptionfrom§3.1.2.1.
\ifbibindex{htruei}{hfalsei}
Expandstohtrueiorhfalseidependingontheindexingoptionfrom§3.1.2.1.
\iffootnote{htruei}{hfalsei}
Expandstohtrueiwhenlocatedinafootnote, andtohfalseiotherwise. Notethat
footnotesinminipageenvironmentsareconsideredtobepartofthebodytext. This
commandwillonlyexpandtohtrueiinfootnotesathebottomofthepageandin
endnotesasprovidedbytheendnotespackage.
256

citecounter Thiscounterindicateshowmanytimestheentrycurrentlybeingprocessediscited
inthecurrentreferencesection. Notethatthisfeatureneedstobeenabledexplicitly
withthepackageoptioncitecounter. Iftheoptionissettocontext, citationsin
thebodytextandinfootnotesarecountedseparately. Inthiscase,citecounterwill
holdthevalueofthecontextitisusedin.
maxcitecounter This counter holds the maximum value of citecounter across all entries in the
currentreferencesection. Likecitecounteritisonlyavailableifthecitecounter
option is enabled and tracks footnotes and text separately if the option is set to
context.
uniquename Thiscounterreferstothelabelnamelist. Itissetonaper-namebasis. Itsvalueis0if
thebasepartsofthename(bydefaultjustthe‘family’partofthename)areunique,1if
addingtheothernon-basepartsofthename(asspecifiedintheuniquenametemplate
defined by \DeclareUniquenameTemplate) as initials will make it unique, and 2 if
addingthefullformofthenon-basepartsofthenamearerequiredtodisambiguatethe
name. Thisinformationisrequiredbyauthor-yearandauthor-titlecitationschemes
which add additional parts of the name when citing different authors with the
samefamilyname. Forexample,(giventhedefault\DeclareUniquenameTemplate
definition)ifthereisone‘JohnDoe’andone‘EdwardDoe’inthelistofreferences,
thiscounterwillbesetto1. Ifthereisone‘JohnDoe’andone‘JaneDoe’,thevalue
ofthecounterwillbe2. Iftheoptionissettoinit/allinit/mininit/minyearinit,
thecounterwillbelimitedto1. Thisisusefulforcitationsstyleswhichuseinitials
to disambiguate names but never print the full name in citations. If adding the
initialsisnotsufficienttodisambiguatethename,uniquenamewillalsobesetto0
forthatname. Thisfeatureneedstobeenabledexplicitlywiththepackageoption
uniquename. Note that the uniquename counter is local to \printnames and that
itisonlysetforthelabelnamelistandforthenamelistthatlabelnamehasbeen
derived from (typically author or editor). Its value is zero in any other context,
i.e.,itmustbeevaluatedinthenameformattingdirectiveshandlingnamelists. See
§4.11.4forfurtherdetailsandpracticalexamples. Thiscountercanbeoverridden
onaper-namepartbasisbyconsultingthe\namepart‘namepart’unmacrosduring
nameformatting,see§4.2.3.
uniquelist This counter refers to the labelname list. It is set on a per-field basis. Its value
indicatesthenumberofnamesrequiredtodisambiguatethenamelistifautomatic
maxnames/minnames truncation would lead to ambiguous citations. For example,
if there is one work by ‘Doe/Smith/Johnson’ and another one by ‘Doe/Edwards/
Williams’,settingmaxnames=1wouldleadto‘Doeetal.’ inbothcases. Inthiscase,
uniquelistwouldbesetto2onthelabelnamelistsofbothentriesbecauseatleast
thefirsttwonamesarerequiredtodisambiguatethem. Notethattheuniquelist
counterislocalto\printnamesandthatitisonlysetforthelabelnamelistandto
the name list labelname has been derived from (typically author or editor). Its
valueiszeroinanyothercontext. Ifavailable,theuniquelistvaluewillbeusedau-
tomaticallyby\printnameswhenprocessingthenamelist,i.e.,itwillautomatically
override maxnames/minnames. This feature needs to be enabled explicitly with the
packageoptionuniquelist. See§4.11.4forfurtherdetailsandpracticalexamples.
parenlevel Thecurrentnestinglevelofparenthesesand/orbrackets. Thisinformationisonly
availableiftheparentrackerfrom§3.1.2.3isenabled.
257

4.6.3 Testswith\ifboolexprand\ifthenelse
The tests introduced in § 4.6.2 may also be used with the \ifboolexpr command
providedbytheetoolboxpackageandthe\ifthenelsecommandprovidedbythe
ifthenpackage. Thesyntaxofthetestsisslightlydifferentinthiscase: thehtruei
andhfalseiargumentsareomittedfromthetestitselfandpassedtothe\ifboolexpr
or \ifthenelse command instead. Note that the use of these commands implies
some processing overhead. If you do not need any boolean operators, it is more
efficienttousethestand-alonetestsfrom§4.6.2.
\ifboolexpr{hexpressioni}{htruei}{hfalsei}
etoolbox command which allows for complex tests with boolean operators and
grouping:
\ifboolexpr{ (
test {\ifnameundef{editor}}
and
not test {\iflistundef{location}}
)
or test {\iffieldundef{year}}
}
{...}
{...}
\ifthenelse{htestsi}{htruei}{hfalsei}
ifthencommandwhichallowsforcomplextestswithbooleanoperatorsandgroup-
ing:
\ifthenelse{ \(
\ifnameundef{editor}
\and
\not \iflistundef{location}
\)
\or \iffieldundef{year}
}
{...}
{...}
Theadditionaltestsprovidedbybiblatexareonlyavailablewhen\ifboolexpror
\ifthenelseareusedincitationcommandsandinthebibliography.
4.6.4 MiscellaneousCommands
Thesectionintroducedmiscellaneouscommandsandlittlehelpersforuseinbiblio-
graphyandcitationstyles.
\newbibmacro{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
\newbibmacro*{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
Definesamacrotobeexecutedvia\usebibmacrolater. Thesyntaxofthiscommand
isverysimilarto\newcommandexceptthathnameimaycontaincharacterssuchas
258

numbersandpunctuationmarksanddoesnotstartwithabackslash. Theoptional
argumenthargumentsiisanintegerspecifyingthenumberofargumentstakenby
themacro. Ifhoptionaliisgiven,itspecifiesadefaultvalueforthefirstargument
of the macro, which automatically becomes an optional argument. In contrast to
\newcommand,\newbibmacroissuesawarningmessageifthemacroisalreadydefined,
andautomaticallyfallsbackto\renewbibmacro. Aswith\newcommand,theregular
variantofthiscommandusesthe\longprefixinthedefinitionwhilethestarredone
doesnot. Ifamacrohasbeendeclaredtobelong,itmaytakeargumentscontaining
\partokens. \newbibmacroand\renewbibmacroareprovidedforconvenience. Style
authorsarefreetouse\newcommandor\definstead. However,notethatmostshared
definitionsfoundinbiblatex.defaredefinedwith\newbibmacro,hencetheymust
beusedandmodifiedaccordingly.
\renewbibmacro{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
\renewbibmacro*{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
Similar to \newbibmacro but redefines hnamei. In contrast to \renewcommand,
\renewbibmacro issues a warning message if the macro is undefined, and auto-
maticallyfallsbackto\newbibmacro.
\providebibmacro{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
\providebibmacro*{hnamei}[hargumentsi][hoptionali]{hdefinitioni}
Similarto\newbibmacrobutonlydefineshnameiifitisundefined. Thiscommand
issimilarinconceptto\providecommand.
\letbibmacro{haliasi}{hnamei}
\letbibmacro*{haliasi}{hnamei}
This command defines the macro haliasi to be an alias of the macro hnamei. The
definitionisperformedby\csletcs. Anerrorisissuedifhnameiisundefined. The
regularvariantofthiscommandsanitizeshnameiwhilethestarredvariantdoesnot.
\usebibmacro{hnamei}
\usebibmacro*{hnamei}
This command executes the macro hnamei, as defined with \newbibmacro. If the
macro takes any arguments, they are simply appended after hnamei. The regular
variantofthiscommandsanitizeshnameiwhilethestarredvariantdoesnot.
\savecommand{hcommandi}
\restorecommand{hcommandi}
Thesecommandssaveandrestoreanyhcommandi,whichmustbeacommandname
starting with a backslash. Both commands work within a local scope. They are
mainlyprovidedforuseinlocalisationfiles.
\savebibmacro{hnamei}
\restorebibmacro{hnamei}
Thesecommandssaveandrestorethemacrohnamei,wherehnameiistheidentifier
ofamacrodefinedwith\newbibmacro. Bothcommandsworkwithinalocalscope.
Theyaremainlyprovidedforuseinlocalisationfiles.
259

\savefieldformat[hentrytypei]{hformati}
\restorefieldformat[hentrytypei]{hformati}
Thesecommandssaveandrestoretheformattingdirectivehformati,asdefinedwith
\DeclareFieldFormat. Bothcommandsworkwithinalocalscope. Theyaremainly
providedforuseinlocalisationfiles.
\savelistformat[hentrytypei]{hformati}
\restorelistformat[hentrytypei]{hformati}
Thesecommandssaveandrestoretheformattingdirectivehformati,asdefinedwith
\DeclareListFormat. Bothcommandsworkwithinalocalscope. Theyaremainly
providedforuseinlocalisationfiles.
\savenameformat[hentrytypei]{hformati}
\restorenameformat[hentrytypei]{hformati}
Thesecommandssaveandrestoretheformattingdirectivehformati,asdefinedwith
\DeclareNameFormat. Bothcommandsworkwithinalocalscope. Theyaremainly
providedforuseinlocalisationfiles.
\savelistwrapperformat[hentrytypei]{hformati}
\restorelistwrapperformat[hentrytypei]{hformati}
Thesecommandssaveandrestoretheformattingdirectivehformati,asdefinedwith
\DeclareListWrapperFormat. Bothcommandsworkwithinalocalscope. Theyare
mainlyprovidedforuseinlocalisationfiles.
\savenamewrapperformat[hentrytypei]{hformati}
\restorenamewrapperformat[hentrytypei]{hformati}
Thesecommandssaveandrestoretheformattingdirectivehformati,asdefinedwith
\DeclareNameWrapperFormat. Bothcommandsworkwithinalocalscope. Theyare
mainlyprovidedforuseinlocalisationfiles.
\ifbibmacroundef{hnamei}{htruei}{hfalsei}
Expands to htruei if the bibliography macro hnamei is undefined, and to hfalsei
otherwise.
Thisbibliographymacrocanbeusedinthefollowingidiomtomakeabibliography
macromoretypespecific.
\letbibmacro{cite:*}{cite}
\newbibmacro{cite:patent}{%
\printtext{\color{red}%
Some citation format specific to patents}}
\renewbibmacro*{cite}{%
\ifbibmacroundef{cite:\thefield{entrytype}}
{\usebibmacro{cite:*}}
{\usebibmacro*{cite:\thefield{entrytype}}}%
}
260

\iffieldformatundef[hentrytypei]{hnamei}{htruei}{hfalsei}
\iflistformatundef[hentrytypei]{hnamei}{htruei}{hfalsei}
\ifnameformatundef[hentrytypei]{hnamei}{htruei}{hfalsei}
\iflistwrapperformatundef[hentrytypei]{hnamei}{htruei}{hfalsei}
\ifnamewrapperformatundef[hentrytypei]{hnamei}{htruei}{hfalsei}
Expands to htruei if the formatting directive hformati is undefined, and to hfalsei
otherwise.
\usedriver{hcodei}{hentrytypei}
Executesthebibliographydriverforanhentrytypei. Callingthiscommandinthe
hloopcodeiofacitationcommanddefinedwith\DeclareCiteCommandisasimpleway
toprintfullcitationssimilartoabibliographyentry. Commandssuchas\newblock,
which are not applicable in a citation, are disabled automatically by default. The
globalinitializationcanbechangedwith\AtUsedriver,see§4.10.6. Additionallocal
initializationcommandsmaybepassedasthehcodeiargument. Thisargumentis
executedinsidethegroupinwhich\usedriverrunstherespectivedriver. Notethat
it is mandatory in terms of the syntax but may be left empty. Also note that this
command will automatically switch languages if the autolang package option is
enabled.
\bibhypertarget{hnamei}{htexti}
Awrapperforhyperref’s\hypertargetcommand. Thehnameiisthenameofthe
anchor,thehtextiisarbitraryprintabletextorcodewhichservesasananchor. If
thereareanyrefsectionenvironmentsinthedocument,thehnameiislocaltothe
currentenvironment. Ifthehyperrefpackageoptionisdisabledorthehyperref
packagehasnotbeenloaded,thiscommandwillsimplypassonitshtextiargument.
Seealsotheformattingdirectivebibhypertargetin§4.10.4.
\bibhyperlink{hnamei}{htexti}
A wrapper for hyperref’s \hyperlink command. The hnamei is the name of an
anchordefinedwith\bibhypertarget,thehtextiisarbitraryprintabletextorcode
to be transformed into a link. If there are any refsection environments in the
document,thehnameiislocaltothecurrentenvironment. Ifthehyperrefpackage
optionisdisabledorthehyperrefpackagehasnotbeenloaded,thiscommandwill
simplypassonitshtextiargument. Seealsotheformattingdirectivebibhyperlink
in§4.10.4.
\bibhyperref[hentrykeyi]{htexti}
Transformshtextiintoaninternallinkpointingtohentrykeyiinthebibliography.
If hentrykeyi is omitted, this command uses the key of the entry currently being
processed. This command is employed to transform citations into clickable links
pointingtothecorrespondingentryinthebibliography. Thelinktargetismarked
automaticallybybiblatex. Iftherearemultiplebibliographiesinadocument,the
targetwillbethefirstoccurenceofhentrykeyiinoneofthebibliographies. Ifthere
arerefsectionenvironments,thelinksarelocaltotheenvironment. Seealsothe
formattingdirectivebibhyperrefin§4.10.4.
\ifhyperref{htruei}{hfalsei}
Expandstohtrueiifthehyperrefpackageoptionisenabled(whichimpliesthatthe
hyperrefpackagehasbeenloaded),andtohfalseiotherwise.
261

\docsvfield{hfieldi}
Similartothe\docsvlistcommandfromtheetoolboxpackage,exceptthatittakes
afieldnameasitsargument. Thevalueofthisfieldisparsedasacomma-separated
list. Ifthehfieldiisundefined,thiscommandexpandstoanemptystring.
\forcsvfield{hhandleri}{hfieldi}
Similar to the \forcsvlist command from the etoolbox package, except that it
takes a field name as its argument. The value of this field is parsed as a comma-
separatedlist. Ifthehfieldiisundefined,thiscommandexpandstoanemptystring.
\MakeCapital{htexti}
Similarto\MakeUppercasebutonlyconvertsthefirstprintablecharacterinhtextito
uppercase. Notethattherestrictionsthatapplyto\MakeUppercasealsoapplytothis
command. Namely,allcommandsinhtextimusteitherberobustorprefixedwith
\protect since the htexti is expanded during capitalization. Apart from us-ascii
charactersandthestandardaccentcommands,thiscommandalsohandlestheactive
charactersoftheinputencpackageaswellastheshorthandsofthebabelpackage.
Ifthehtextistartswithacontrolsequence,nothingiscapitalized. Thiscommandis
robust.
\MakeSentenceCase{htexti}
\MakeSentenceCase*{htexti}
Convertsitshtextiargumenttosentencecase,i.e.,thefirstwordiscapitalizedand
theremainderofthestringisconvertedtolowercase. Thiscommandisrobust. The
starredvariantdiffersfromtheregularversioninthatitconsidersthelanguageof
theentry,asspecifiedinthelangidfield. Ifthelangidfieldisdefinedandholdsa
language declared with \DeclareCaseLangs (see below)38, then the sentence case
conversion is performed. If the langid field is undefined, then the language list
declaredwith\DeclareCaseLangsischeckedforthepresenceofthemaindocument
languagederivedfromthelanguageoption. Iffound,sentencecaseconversionis
performed, if not, the htexti is not altered in any way. It is recommended to use
\MakeSentenceCase*ratherthantheregularvariantinformattingdirectives.
Dependingontheoptioncasechanger\MakeCaseChangeand\MakeCaseChange*are
eitherimplementedusingtheexpl3modulel3textororiginalLATEX2εcode.
BothvariantssupportthetraditionalBibTeXconventionforbibfilesthatanything
wrapped in a pair of curly braces is not modified when changing the case. For
example:
\MakeSentenceCase{an Introduction to LaTeX}
\MakeSentenceCase{an Introduction to {LaTeX}}
wouldyield:
An introduction to latex
An introduction to LaTeX
38Bydefault,convertingtosentencecaseisenabledforthefollowinglanguageidentifiers:american,
british, canadian, english, australian, newzealand as well as the aliases USenglish and
UKenglish.Use\DeclareCaseLangstoextendorchangethislist.
262

InbibfilesdesignedwithtraditionalBibTeXinmind,ithasbeenfairlycommonto
onlywrapsinglelettersinbracestopreventcase-changing:
title = {An Introduction to {L}a{T}e{X}}
Theproblemwiththisconventionisthatthebraceswillsuppressthekerningon
bothsidesoftheenclosedletter. Itispreferabletowraptheentirewordinbracesas
showninthefirstexample. Macrosintitlesmustalsobeprotectedwithbraces
title = {The {\TeX book}},
Thebehaviourof\MakeSentenceCasediffersslightlybetweenthelatex2eandexpl3
implementation. Generallyspeaking,theexpl3codeisclosertotheBibTeXbehaviour
of change.case$. It is also better equipped to deal with non-us-ascii input and
macrosthanthelatex2eimplementation. \MakeSentenceCasebehavesasfollows.
• The first letter of its argument is capitalised with \MakeUppercase. This is
differentfromBibTeX’schange.case$,whichdoesnottouchthefirstletterof
itsargument.
Note that with the latex2e code a pair of braces that starts with a control
sequencewillbetreatedasasinglecharacterforcapitalisationpurposes. This
meansthattheentireargumentofacommandprotectedwithasinglepairof
bracesiscapitalised.
• Withthelatex2ecodeexpandablecommandsareexpandedbeforethecase
change, which means that the case change applies to the replacement text.
Unexpandablecommandsarenottouched.
BibTeXdoesnotinterpretmacrosandthereforepassescommandsthroughun-
changed(thisdoesnotnecessarilyapplytothearguments ofthosecommands).
Theexpl3implementationalsodoesnotexpandcommandsandonlyapplies
casechangetothearguments.
• Textwrappedinoneormorepairsofbracesisprotectedfromcasechangeunless
itstartswithacontrolsequence. ThisisthesamebehaviouraswithBibTeX.
Notethatthebracescouldeitherbeexplicitgroupsorargumentdelimiters.
• Textin asingle pairof bracesthat starts witha controlsequence isnot pro-
tected and will be subject to case changes. Note that this need not apply to
braces that are argument delimiters, in fact the latex2e implementation of
\MakeSentenceCase may in some cases produce an error or otherwise unde-
sirableoutputiftheargumentofacommandstartswithacontrolsequence.
BibTeX’scasechangefunctiondoesnotdifferentiatebetweenargumentdelim-
itersandbracegroupsandalwayssubjectstextatbracelevel1tocasechange
ifitstartswithacontrolsequence.
Formostintentsandpurposesthefollowingrulesshouldgiveasensibleresult.
• Protectallwordswhosecaseshouldnotbechangedbywrappingtheminone
pairofbraces.
• Ifwordsarealreadyinthebracedargumentofacommandsuchas\mkbibquote
or\emph,theyareautomaticallyprotected.
– Toundo thisprotectionwrapthecommandinbracesagain.
263

– Itisnotpossibletoselectivelyre-applyprotectionifithasbeenundone
withanadditionalpairofbraces. Ifamorefine-grainedcontrolisneeded,
work-aroundslikesplittingtheargumentcouldbetried.
• Whileitispossibletoprotectwordsfromcasechangeatthebeginningofa
fieldwithapairofbraces,itisnotpossibletoundothecaseprotectionthata
commandautomaticallyimpliesbywrappingitinbracesinthatposition. In
thatcasework-aroundsarenecessary.
title = {The Story of {HMS} \emph{Erebus}
in {\emph{Really}} Strong Wind},
wouldbeconvertedtosentencecaseby\MakeSentenceCaseas
ThestoryofHMSErebus inreally strongwind
Iftheexpl3implementationofthecasechangingfunctionsisselected,theBibTeX
caseprotectionbehaviourcanbeexchangedforaslightlysimplerversion. When
bibtexcaseprotection set to false, braces no longer automatically imply case
protection. Insteadwordscanbeprotectedfromcasechangewith\NoCaseChange.
Theexamplesfromabovewouldthenread
title = {An Introduction to \NoCaseChange{LaTeX}},
title = {The Story of \NoCaseChange{HMS \emph{Erebus}}
in \emph{Really} Strong Wind},
Generally,thisoptionshouldallowforasanercaseprotectioninput,becausecurly
braces are no longer overloaded with different levels of meaning, but it is a big
departure from the standard case protection input that has been with the LaTeX
worldforalongtime.
Due to its complex implementation \MakeSentenceCase can not accept arbitrary
input,itonlysafelyoperatesonrawtextorfielddata. Inthestandardstylesthetitle
andothertitle-likefieldformatsdonotworktogetherwith\MakeSentenceCasebe-
causeoftheirargumentstructure,sothestandardstylesofferadedicatedtitlecase
fieldformattoapplythiscommand. Toenablesentencecasinginstandardstylesfor
languagesthatsupportityouwoulduse:
\DeclareFieldFormat{titlecase}{\MakeSentenceCase*{#1}}
Sentencecasingcanthenbedisabledbyresettingthatfieldformatto
\DeclareFieldFormat{titlecase}{#1}
Customstylesmayfollowadifferentapproach,butstyleauthorsareencouragedto
applythesamegeneralideastotheirstyles.
\mkpageprefix[hpaginationi][hpostproi]{htexti}
Thiscommandisintendedforuseinfieldformattingdirectiveswhichformatthe
pagenumbersinthehpostnoteiargumentofcitationcommandsandthepagesfield
of bibliography entries. It will parse its htexti argument and prefix it with ‘p.’ or
‘pp.’ by default. The optional hpaginationi argument holds the name of a field
264

Table12:\mkcomprangesetup
| Input    | Output          |                  |                   |
| -------- | --------------- | ---------------- | ----------------- |
|          | mincomprange=10 | mincomprange=100 | mincomprange=1000 |
| 11--15   | 11–5            | 11–15            | 11–15             |
| 111--115 | 111–5           | 111–5            | 111–115           |
|          | 1111–5          | 1111–5           | 1111–5            |
1111--1115
|            | maxcomprange=1000 | maxcomprange=100 | maxcomprange=10  |
| ---------- | ----------------- | ---------------- | ---------------- |
| 1111--1115 | 1111–5            | 1111–5           | 1111–5           |
| 1111--1155 | 1111–55           | 1111–55          | 1111–1155        |
| 1111--1555 | 1111–555          | 1111–1555        | 1111–1555        |
|            | mincompwidth=1    | mincompwidth=10  | mincompwidth=100 |
| 1111--1115 | 1111–5            | 1111–15          | 1111–115         |
| 1111--1155 | 1111–55           | 1111–55          | 1111–155         |
| 1111--1555 | 1111–555          | 1111–555         | 1111–555         |
indicatingthepaginationtype. Thismaybeeitherpaginationorbookpagination,
withpaginationbeingthedefault. Thespacingbetweentheprefixandthehtexti
maybemodifiedbyredefining\ppspace. Thedefaultisanunbreakableinterword
space. See §§ 2.3.12 and 3.15.3 for further details. See also \DeclareNumChars,
\DeclareRangeChars,\DeclareRangeCommands,and\NumCheckSetup. Theoptional
hpostproi argument specifies a macroto be used for post-processing the htexti. If
onlyoneoptionalargumentisgiven,itistakenashpaginationi. Herearetwotypical
examples:
\DeclareFieldFormat{postnote}{\mkpageprefix[pagination][\mknormrange
,→ ]{#1}}
\DeclareFieldFormat{pages}{\mkpageprefix[bookpagination]{#1}}
\mkpagetotal[hpaginationi][hpostproi]{htexti}
This command is similar to \mkpageprefix except that it is intended for the
pagetotal field of bibliography entries, i.e., it will print “123 pages” rather than
“page 123”. The optional hpaginationi argument defaults to bookpagination. The
spacinginsertedbetweenthepaginationsuffixandthehtextimaybemodifiedby
redefiningthemacro\ppspace. Theoptionalhpostproiargumentspecifiesamacro
tobeusedforpost-processingthehtexti.
Ifonlyoneoptionalargumentisgiven,it
| istakenashpaginationi. | Hereisatypicalexample: |     |     |
| ---------------------- | ---------------------- | --- | --- |
\DeclareFieldFormat{pagetotal}{\mkpagetotal[bookpagination]{#1}}
The optional argument is omissible in this case. The pagination
bookpagination
stringsaretakenfrom<pagination>totaland<pagination>totals.
\mkcomprange[hpostproi][hitempostproi]{htexti}
\mkcomprange*[hpostproi][hitempostproi]{htexti}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,willparseits
htextiargumentforpagerangesandcompressthem.
Forexample,“125–129”maybe
formattedas“125–9”. Youmayconfigurethebehaviorof\mkcomprangebyadjusting
265

theLaTeXcountersmincomprange,maxcomprange,andmincompwidth,asillustrated
intable12. Thedefaultsettingsare10,100000,and1,respectively. Thismeansthat
the command tries to compress as much as possible by default. Use \setcounter
toadjust theparameters. The scannerrecognises \bibrangedashandhyphens as
rangedashes. Itwillnormalizethedashbyreplacinganynumberofconsecutive
hyphens with \bibrangedash. Lists of ranges delimited with \bibrangessep are
alsosupported. Thescannerwillnormaliseanycommaorsemicolonssurrounded
by optional space by replacing them with \bibrangessep. If you want to hide a
character from the list/range scanner for some reason, wrap the character or the
entirestringincurlybraces. Theoptionalhpostproiargumentspecifiesamacroto
be used for post-processing the htexti. This is important if you want to combine
\mkcomprangewithotherformattingmacroswhichalsoneedtoparsetheirhtexti
argument,suchas\mkpageprefix. Simplynestingthesecommandswillnotwork
asexpected. Usethehpostproiargumenttosetuptheprocessingchainasfollows:
\DeclareFieldFormat{postnote}{\mkcomprange[{\mkpageprefix[pagination]
,→ }]{#1}}
Note that \mkcomprange is executed first, using \mkpageprefix as post-processor.
Also note that the hpostproi argument is wrapped in an additional pair of braces.
ThisisonlyrequiredinthisparticularcasetopreventLaTeX’soptionalargument
scannerfromgettingconfusedbythenestedbrackets. Thestarredversionofthis
commanddiffersfromtheregularoneinthewaythehpostproiargumentisapplied
toalistofvalues. Forexample:
\mkcomprange[\mkpageprefix]{5, 123-129, 423-439}
\mkcomprange*[\mkpageprefix]{5, 123-129, 423-439}
willoutput:
pp. 5, 123-9, 423-39
p. 5, pp. 123-9, pp. 423-39
Thesecondoptionalargumenthitempostproiisusedtopost-processeachindividual
numberitemintheformattedlist. Itcanbeusedtoconvertnumbersfromcardinals
toordinals. Ifonlyoneoptionalargumentispresent,itistreatedashpostproi.
\mknormrange[hpostproi][hitempostproi]{htexti}
\mknormrange*[hpostproi][hitempostproi]{htexti}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,willparse
its htexti argument for page ranges and will normalise them. The command is
similarto\mkcomprangeexceptthatthepagerangeswillnotbecompressed. The
scannerrecognises\bibrangedashandhyphensasrangedashes. Itwillnormalize
the dash by replacing any number of consecutive hyphens with \bibrangedash.
Listsofrangesdelimitedwith\bibrangesseparealsosupported. Thescannerwill
normaliseanycommaorsemicolonssurroundedbyoptionalspacebyreplacingthem
with\bibrangessep. Ifyouwanttohideacharacterfromthelist/rangescannerfor
somereason,wrapthecharacterortheentirestringincurlybraces. Theoptional
hpostproiargumentspecifiesamacrotobeusedforpost-processingthehtexti. See
266

\mkcomprangeonhowtousethisargument. Thestarredversionofthiscommand
differsfromtheregularoneinthewaythehpostproiargumentisappliedtoalist
ofvalues. Thesecondoptionalargumenthitempostproiisusedtopost-processeach
individual number item in the formatted list. It can be used to convert numbers
fromcardinalstoordinals. Ifonlyoneoptionalargumentispresent,itistreatedas
hpostproi.
\mkseqrange[hpostproi][hitempostproi]{htexti}
\mkseqrange*[hpostproi][hitempostproi]{htexti}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,willparseits
htextiargumentforpagerangesandwillnormalisethemsimilarto\mknormrange.
Thedifferenceisthatthecommandwilloutputonlythefirstpageandthelocalisation
stringsequensorsequentes, respectively, ifapplicable(dependingonthesetting
ofthecitepagerangeoption;see§3.1.2.1). Thescannerrecognises\bibrangedash
and hyphens as range dashes. It will normalize the dash by replacing any num-
ber of consecutive hyphens with \bibrangedash. Lists of ranges delimited with
\bibrangesseparealsosupported. Thescannerwillnormaliseanycommaorsemi-
colonssurroundedbyoptionalspacebyreplacingthemwith\bibrangessep. Ifyou
wanttohideacharacterfromthelist/rangescannerforsomereason,wrapthechar-
acterortheentirestringincurlybraces. Theoptionalhpostproiargumentspecifiesa
macrotobeusedforpost-processingthehtexti. See\mkcomprangeonhowtouse
thisargument. Thestarredversionofthiscommanddiffersfromtheregularonein
thewaythehpostproiargumentisappliedtoalistofvalues. Thesecondoptional
argumenthitempostproiisusedtopost-processeachindividualnumberiteminthe
formattedlist. Itcanbeusedtoconvertnumbersfromcardinalstoordinals. Ifonly
oneoptionalargumentispresent,itistreatedashpostproi. Forexample,withdefault
citepagerangesettings:
\mkseqrange[\mkpageprefix]{5, 123-124, 423-439, 522-524}
\mkseqrange*[\mkpageprefix]{5, 123-124, 423-439, 522-524}
willoutput:
pp. 5, 123 sq., 423-439, 522 sqq.
p. 5, pp. 123 sq., pp. 423-439, pp. 522 sqq.
\mkautorange[hpostproi][hitempostproi]{htexti}
\mkautorange*[hpostproi][hitempostproi]{htexti}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,isaportman-
teaucommandwhichisequalto\mkseqrangeor\mkseqrange*,respectively,ifthe
citepagerangeoption(see§3.1.2.1)issetto2sq,3sqq,orallsqq,to\mkcomprange
or \mkcomprange*, respectively, if the citepagerange option is set to compressed,
andto\mknormrangeor\mknormrange*withnormalizedandbydefault. Usethisif
youwanttogivetheusersofyourstylethechoicetotogglecitepagerange.
\mkfirstpage[hpostproi][hitempostproi]{htexti}
\mkfirstpage*[hpostproi][hitempostproi]{htexti}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,willparse
itshtextiargumentforpagerangesandprintthestartpageoftherangeonly. The
267

scanner recognizes \bibrangedash and hyphens as range dashes. Lists of ranges
delimitedwith\bibrangesseparealsosupported. Ifyouwanttohideacharacter
fromthelist/rangescannerforsomereason,wrapthecharacterortheentirestring
in curly braces. The optional hpostproi argument specifies a macro to be used for
post-processing the htexti. See \mkcomprange on how to use this argument. The
starredversionofthiscommanddiffersfromtheregularoneinthewaythehpostproi
argumentisappliedtoalistofvalues. Thesecondoptionalargumenthitempostproi
isusedtopost-processeachindividualnumberitemintheformattedlist. Itcanbe
usedtoconvertnumbersfromcardinalstoordinals. Ifonlyoneoptionalargument
ispresent,itistreatedashpostproi. Forexample:
\mkfirstpage[\mkpageprefix]{5, 123-129, 423-439}
\mkfirstpage*[\mkpageprefix]{5, 123-129, 423-439}
willoutput:
pp. 5, 123, 423
p. 5, p. 123, p. 423
\rangelen{hrangefieldi}
Takesthenameofabibfielddeclaredasarangefieldinthedatamodelandreturns
the length of the range. This is calculated by biber and can handle many special
cases. Itwillreturn−1foropenendedranges. Specifically\rangelencan:
• Calculatethetotalofmultiplerangesinthesamefieldsuchas‘1-10,20-30’
• Handleimplicitrangessuchas‘22-4’and‘130-33’
• Handleromannumeralrangesinupperandlowercaseandconsistingofboth
us-asciiandUnicoderomannumeralrepresentations.
Herearesomeexamples:
pages=‘10’ \rangelen{pages}returns’1’
pages=‘10-15’ \rangelen{pages}returns’6’
pages=‘10-15,47-53’ \rangelen{pages}returns’13’
pages=‘10-’ \rangelen{pages}returns’-1’
pages=‘-10’ \rangelen{pages}returns’-1’
pages=‘48-9’ \rangelen{pages}returns’2’
pages=‘172-77’ \rangelen{pages}returns’6’
pages=‘i-vi’ \rangelen{pages}returns’6’
pages=‘X-XX’ \rangelen{pages}returns’11’
pages=‘ⅥⅠ-ⅻ’ \rangelen{pages}returns’6’
pages=‘ⅥⅠ-ⅻ,145-7,135-39’ \rangelen{pages}returns’14’
The\rangelencommandcanbeusedintests:
\ifnumcomp{\rangelen{pages}}{=}{1}{add 'f'}{do nothing}
268

\DeclareNumChars{hcharactersi}
\DeclareNumChars*{hcharactersi}
Thiscommandconfiguresthe\ifnumeral, \ifnumerals, and\ifpagestestsfrom
§4.6.2. Thesetupwillalsoaffect\iffieldnum,\iffieldnums,\iffieldpagesaswell
as\mkpageprefixand\mkpagetotal. Thehcharactersiargumentisanundelimited
listofcharacterswhicharetobeconsideredasbeingpartofanumber. Theregular
versionofthiscommandreplacesthecurrentsetting,thestarredversionappendsits
argumenttothecurrentlist. Thedefaultsettingis:
\DeclareNumChars{.}
Thismeansthata(sectionorother)numberlike‘3.4.5’willbeconsideredasanumber.
NotethatArabicandRomannumeralsaredetectedbydefault,thereisnoneedto
declarethemexplicitly.
\DeclareRangeChars{hcharactersi}
\DeclareRangeChars*{hcharactersi}
This command configures the \ifnumerals and \ifpages tests from § 4.6.2. The
setup will also affect \iffieldnums and \iffieldpages as well as \mkpageprefix
and\mkpagetotal. Thehcharactersiargumentisanundelimitedlistofcharacters
whicharetobeconsideredasrangeindicators. Theregularversionofthiscommand
replacesthecurrentsetting,thestarredversionappendsitsargumenttothecurrent
list. Thedefaultsettingis:
\DeclareRangeChars{~,;-+/}
ForenginesthatfullysupportUnicodethesedefaultsareextendedwith
\DeclareRangeChars*{–—}
Thismeansthatstringslike‘3–5’,‘35+’,‘8/9’andsoonwillbeconsideredasarange
by\ifnumeralsand\ifpages. Non-rangecharactersinsuchstringsarerecognized
asnumbers. Sostringslike‘3a–5a’and‘35b+’arenotdeemedtoberangesbydefault.
Seealso§§2.3.12and3.15.3forfurtherdetails.
\DeclareRangeCommands{hcommandsi}
\DeclareRangeCommands*{hcommandsi}
This command is similar to \DeclareRangeChars, except that the hcommandsi ar-
gument is an undelimited list of commands which are to be considered as range
indicators. The regular version of this command replaces the current setting, the
starred versionappends its argument to the currentlist. The default list is rather
longandshouldcoverallcommoncases;hereisashorterexample:
\DeclareRangeCommands{\&\bibrangedash\textendash\textemdash\psq\psqq}
Seealso§§2.3.12and3.15.3forfurtherdetails.
269

\DeclarePageCommands{hcommandsi}
\DeclarePageCommands*{hcommandsi}
Thiscommandissimilarto\DeclareRangeCommands,exceptthatitonlyaffectsthe
\ifpages and \iffieldpages tests but not \ifnumerals and \iffieldnums. The
defaultsettingis:
\DeclarePageCommands{\pno\ppno}
\NumCheckSetup{hcodei}
Use this command to temporarily redefine any commands which interfere with
the tests performed by \ifnumeral, \ifnumerals, and \ifpages from § 4.6.2.
The setup will also affect \iffieldnum, \iffieldnums, \iffieldpages as well as
\mkpageprefixand\mkpagetotal. Thehcodeiwillbeexecutedinagroupbythese
commands. Since the above mentioned commands will expand the string to be
analyzed,itispossibletoremovecommandstobeignoredbythetestsbymaking
themexpandtoanemptystring. Seealso§§2.3.12and3.15.3forfurtherdetails.
\NumsCheckSetup{hcodei}
Like \NumCheckSetup but only applies to \ifnumerals and \ifpages from § 4.6.2
andtheirderivativetests.
\PagesCheckSetup{hcodei}
Like \NumCheckSetup but only applies to \ifpages from § 4.6.2 and its derivative
tests. Thedefaultsettingismakes\pnfmttransparenttothetest:
\PagesCheckSetup{\let\pnfmt\@firstofone}
\DeclareBabelToExplLanguageMapping{hbabellanguagei}{hexpllanguagei}
Thiscommandisonlyavailableiftheexpl3casechangingcodeisused.
Usehexpllanguageiashlanguageiargumentforthel3textcasechangingfunctions
whenbabel languageisactive. Thiscommandisonlyrequiredifhbabellanguagei
should correspond to a language for which l3text has special rules set up. The
defaultinvocationsofthiscommandare
\DeclareBabelToExplLanguageMapping{dutch}{nl}
\DeclareBabelToExplLanguageMapping{greek}{el}
\DeclareBabelToExplLanguageMapping{turkish}{tr}
\UndeclareBabelToExplLanguageMapping{hbabellanguagei}
Thiscommandisonlyavailableiftheexpl3casechangingcodeisused.
Removes the babel-to-expl3 language mapping for hbabellanguagei. If the argu-
mentisanasterisk*,alllanguagemappingsareremoved.
270

\DeclareCaseLangs{hlanguagesi}
\DeclareCaseLangs*{hlanguagesi}
Definesthelistoflanguageswhichareconsideredbythe\MakeSentenceCase*com-
mandasitconvertsastringtosentencecase. Thehlanguagesiargumentisacomma-
separatedlistofbabel/polyglossialanguageidentifiers. Theregularversionofthis
commandreplacesthecurrentsetting,thestarredversionappendsitsargumentto
thecurrentlist. Thedefaultsettingis:
\DeclareCaseLangs{%
american,british,canadian,english,australian,newzealand,USenglish,
,→ UKenglish}
Seethebabel/polyglossiamanualsandtable2foralistoflanguagesidentifiers.
\BibliographyWarning{hmessagei}
Thiscommandissimilarto\PackageWarningbutprintstheentrykeyoftheentry
currentlybeingprocessedinadditiontotheinputlinenumber. Itmaybeusedin
the bibliography as well as in citation commands. If the hmessagei is fairly long,
use\MessageBreaktoincludelinebreaks. Notethatthestandard\PackageWarning
commanddoesnotprovideameaningfulcluewhenusedinthebibliographysince
theinputlinenumberisthelineonwhichthe\printbibliographycommandwas
given.
\pagetrackertrue
\pagetrackerfalse
These commands activate or deactivate the page tracker locally (this will affect
the\iffirstonpageand\ifsamepagetestfrom§4.6.2). Theyareintendedforuse
in the definition of citation commands or anywhere in the document body. If a
citationcommandistobeexcludedfrompagetracking,use\pagetrackerfalsein
thehprecodeiargumentof\DeclareCiteCommand. See§4.3.1fordetails. Notethat
thesecommandshavenoeffectifpagetrackinghasbeendisabledglobally.
\citetrackertrue
\citetrackerfalse
Thesecommandsactivateordeactivateallcitationtrackerslocally(thiswillaffect
the\ifciteseen,\ifentryseen,\ifciteibid,and\ifciteidemtestsfrom§4.6.2).
They are intended for use in the definition of citation commands or anywhere in
the document body. If a citation command is to be excluded from tracking, use
\citetrackerfalseinthehprecodeiargumentof\DeclareCiteCommand. See§4.3.1
fordetails. Notethatthesecommandshavenoeffectiftrackinghasbeendisabled
globally.
\backtrackertrue
\backtrackerfalse
Thesecommandsactivateordeactivatethebackreftrackerlocally. Theyareintended
foruseinthedefinitionofcitationcommandsoranywhereinthedocumentbody. If
acitationcommandistobeexcludedfrombacktracking,use\backtrackerfalsein
thehprecodeiargumentof\DeclareCiteCommand. Notethatthesecommandshave
noeffectifthebackrefoptionhasbeennotbeensetglobally.
271

4.7 PunctuationandSpacing
Thebiblatexpackageprovideselaboratefacilitiesdesignedtomanageandtrack
punctuationandspacinginthebibliographyandincitations. Thesefacilitieswork
ontwolevels. Thehigh-levelcommandsdiscussedin§4.7.1dealwithpunctuation
andwhitespaceinsertedbythebibliographystylebetweentheindividualsegments
ofabibliographyentry. Thecommandsin§§4.7.2,4.7.3,4.7.4workatalowerlevel.
TheyuseTeX’sspacefactorandmodifiedspacefactorcodestotrackpunctuation
in a robust and efficient way. This way it is possible to detect trailing punctua-
tion marks within fields, not only those explicitly inserted between fields. The
sametechniqueisalsousedforautomaticcapitalizationoflocalisationstrings,see
\DeclareCapitalPunctuationin§4.7.5aswellas§4.8fordetails. Notethatthese
facilitiesareonlymadeavailablelocallyincitationsandbibliographies. Theywill
notaffectanyotherpartofadocument.
4.7.1 BlockandUnitPunctuation
Themajorsegmentsofabibliographyentryare‘blocks’and‘units’. Ablockisthe
largersegmentofthetwo,aunitisshorteroratmostequalinlength. Forexample,
the values of fields such as title or note usually form a unit which is separated
fromsubsequentdatabyaperiodoracomma. Ablockmaycompriseseveralfields
whicharetreatedasseparateunits,forexamplepublisher,location,andyear. The
segmentationofanentryintoblocksandunitsisatthediscretionofthebibliography
style. An entry is segmented by inserting \newblock and \newunit commands at
suitableplacesand\finentryattheveryend(see§4.2.3foranexample). Seealso
§4.11.8forsomepracticalhints.
\newblock Recordstheendofablock. Thiscommanddoesnotprintanything,itmerelymarks
the end of the block. The block delimiter \newblockpunct will be inserted by a
subsequent \printtext, \printfield, \printlist, \printnames, or \bibstring
command. Youmayuse\newblockatsuitableplaceswithouthavingtoworryabout
spurious blocks. A new block will only be started by the next \printfield (or
similar)commandifthiscommandprintsanything. See§4.11.8forfurtherdetails.
\newunit Recordstheendofaunitandputsthedefaultdelimiter\newunitpunctinthepunc-
tuationbuffer. Thiscommanddoesnotprintanything,itmerelymarkstheendofthe
unit. Thepunctuationbufferwillbeinsertedbythenext\printtext,\printfield,
\printlist, \printnames, or \bibstring command. You may use \newunit after
commandslike\printfieldwithouthavingtoworryaboutspuriouspunctuation
andwhitespace. Thebufferwillonlybeinsertedbythenext\printfieldorsimilar
commandifboth fieldsarenon-empty. Thisalsoappliesto\printtext,\printlist,
\printnames,and\bibstring. See§4.11.8forfurtherdetails.
\finentry Inserts \finentrypunct. This command should be used at the very end of every
bibliographyentry.
\setunit{hpunctuationi}
\setunit*{hpunctuationi}
The \setunit command is similar to \newunit except that it uses hpunctuationi
instead of \newunitpunct. The starred variant differs from the regular version in
that it checks if the last \printtext, \printfield, \printlist, \printnames, or
\bibstringcommanddidactuallyprintanything. Ifnot,itdoesnothing.
272

\printunit{hpunctuationi}
\printunit*{hpunctuationi}
The\printunitcommandissimilarto\setunitexceptthathpunctuationipersistsin
thebuffer. Thisensuresthathpunctuationiisinsertedbeforethenextnon-emptyfield
printedbythe\printtext,\printfield,\printlist,\printnames,or\bibstring
commands—regardlessofanyintermediatecallsto\newunitor\setunit.
\setpunctfont{hcommandi}
Thiscommand,whichisintendedforuseinfieldformattingdirectives,providesan
alternativewayofdealingwithunitpunctuationafterafieldprintedinadifferent
font(forexample,atitleprintedinitalics). ThestandardLaTeXwayofdealingwith
thisisaddingasmallamountofspace,theso-calleditaliccorrection. Thiscommand
allowsadaptingthepunctuationtothefontoftheprecedingfield. Thehcommandi
shouldbeatextfontcommandwhichtakesoneargument,suchas\emphor\textbf.
Thiscommandwillonlyaffectpunctuationmarksinsertedbyoneofthecommands
from § 4.7.3. The font adaption is applied to the nextpunctuation mark only and
willberesetautomaticallythereafter. Ifyouwanttoresetitmanuallybeforeittakes
effect, issue \resetpunctfont. If the punctfont package option is disabled, this
commanddoesnothing. Notethatthe\mkbibemph,\mkbibitalicand\mkbibbold
wrappersfrom§4.10.4incorporatethisfeaturebydefault.
\resetpunctfont Thiscommandresetstheunitpunctuationfontdefinedwith\setpunctfontbeforeit
takeseffect. Ifthepunctfontpackageoptionisdisabled,thiscommanddoesnothing.
4.7.2 PunctuationTests
Thefollowingcommandsmaybeusedtotestforprecedingpunctuationmarksat
anypointincitationsandthebibliography.
\ifpunct{htruei}{hfalsei}
Executeshtrueiifprecededbyanypunctuationmarkexceptforanabbreviationdot,
andhfalseiotherwise.
\ifterm{htruei}{hfalsei}
Executeshtrueiifprecededbyaterminalpunctuationmark,andhfalseiotherwise.
Aterminalpunctuationmarkisanypunctuationmarkwhichhasbeenregisteredfor
automatic capitalization, either with \DeclareCapitalPunctuation or by default,
see § 4.7.5 for details. By default, this applies to periods, exclamation marks, and
questionmarks.
\ifpunctmark{hcharacteri}{htruei}{hfalsei}
Executeshtrueiifprecededbythepunctuationmarkhcharacteri,andhfalseiother-
wise. Thehcharacterimaybeacomma,asemicolon,acolon,aperiod,anexclama-
tion mark, a question mark, or an asterisk. Note that a period denotes an end-of-
sentence period. Use the asterisk to test for the dot after an abbreviation. If this
commandisusedinaformattingdirectivefornamelists,i.e.,intheargumentto
\DeclareNameFormat,thehcharacterimayalsobeanapostrophe.
273

\ifprefchar{htruei}{hfalsei}
Executeshtrueiifprecededbyanyprefixcharacterdeclaredby\DeclarePrefChars.
4.7.3 AddingPunctuation
Thefollowingcommandsaredesignedtopreventdoublepunctuationmarks. Biblio-
graphyandcitationstylesshouldalwaysusethesecommandsinsteadofliteralpunc-
tuationmarks. All\add...commandsinthissectionautomaticallyremovepreceding
whitespacewith\unspace(see§4.7.4). Notethatthebehaviorofall\add...com-
mandsdiscussedbelowisthepackagedefault,whichisrestoredwheneverbiblatex
switcheslanguages. Thisbehaviormaybeadjustedwith\DeclarePunctuationPairs
from§4.7.5.
\adddot Addsaperiodunlessitisprecededbyanypunctuationmark. Thepurposeofthis
command is inserting the dot after an abbreviation. Any dot inserted this way is
recognizedassuchbytheotherpunctuationcommands. Thiscommandmayalsobe
usedtoturnapreviouslyinsertedliteralperiodintoanabbreviationdot.
\addcomma Addsacommaunlessitisprecededbyanothercomma,asemicolon,acolon,ora
period.
\addsemicolon Addsasemicolonunlessitisprecededbyacomma,anothersemicolon,acolon,ora
period.
\addcolon Adds a colon unless it is preceded by a comma, a semicolon, another colon, or a
period.
\addperiod Addsaperiodunlessitisprecededbyanabbreviationdotoranyotherpunctuation
mark. Thiscommandmayalsobeusedtoturnapreviouslyinsertedabbreviation
dotintoaperiod,forexampleattheendofasentence.
\addexclam Addsanexclamationmarkunlessitisprecededbyanypunctuationmarkexceptfor
anabbreviationdot.
\addquestion Addsaquestionmarkunlessitisprecededbyanypunctuationmarkexceptforan
abbreviationdot.
\addslash Adds a breakable slash. This command differs from the \slash command in the
LaTeXkernelinthatalinebreakaftertheslashisnotpenalizedatall.
\isdot Turns a previously inserted literal period into an abbreviation dot. In contrast to
\adddot,nothingisinsertedifthiscommandisnotprecededbyaperiod.
\nopunct Addsaninternalmarkerwhichwillcausethenextpunctuationcommandtoprint
nothing.
4.7.4 AddingWhitespace
Thefollowingcommandsaredesignedtopreventspuriouswhitespace. Bibliography
andcitationstylesshouldalwaysusethesecommandsinsteadofliteralwhitespace.
Incontrasttothecommandsin§§4.7.2and4.7.3,theyarenotrestrictedtocitations
andthebibliographybutavailableglobally.
\unspace Removesprecedingwhitespace,i.e.,removesallskipsandpenaltiesfromtheend
of the current horizontal list. This command is implicitly executed by all of the
followingcommands.
274

\addspace Addsabreakableinterwordspace.
\addnbspace Addsanon-breakableinterwordspace.
\addthinspace Addsabreakable thinspace.
\addnbthinspace Addsanon-breakablethinspace. Thisissimilarto\,and\thinspace.
\addlowpenspace Addsaspacepenalizedbythevalueofthelownamepenaltycounter,see§§3.12.4
and4.10.3fordetails.
\addhighpenspace Addsaspacepenalizedbythevalueofthehighnamepenaltycounter,see§§3.12.4
and4.10.3fordetails.
\addlpthinspace Similarto\addlowpenspacebutaddsabreakablethinspace.
\addhpthinspace Similarto\addhighpenspacebutaddsabreakablethinspace.
\addabbrvspace Addsaspacepenalizedbythevalueoftheabbrvpenaltycounter,see§§3.12.4and
4.10.3fordetails.
\addabthinspace Similarto\addabbrvspacebutusingathinspace.
\adddotspace Executes \adddot and adds a space penalized by the value of the abbrvpenalty
counter,see§§3.12.4and4.10.3fordetails.
Note that the commands in this section implicitly execute \unspace to remove
spuriouswhitespace,hencetheymaybeusedtooverrideeachother. Forexample,
youmayuse\addnbspacetotransformapreviouslyinsertedinterwordspaceintoa
non-breakableoneand\addspacetoturnanon-breakablespaceintoabreakable
one.
4.7.5 ConfiguringPunctuationandCapitalization
The following commands configure various features related to punctuation and
automaticcapitalization.
\DeclarePrefChars{hcharactersi}
\DeclarePrefChars*{hcharactersi}
Thiscommanddeclarescharactersthataretobetreatedspeciallywhentestingto
seeif\bibnamedelimcistobeinsertedbetweenanameprefixandafamilyname. If
acharacterisinthelistofhcharactersi,\bibnamedelimcisnotinserted. Itisusedto
allowabbreviatednamepreficeslike‘d’Argent’wherenospaceshouldbeinserted
aftertheapostrophe. Thestarredversionappendsitsargumenttothelistofprefix
characters,theunstarredversionreplacesthecurrentsetting. Thedefaultsettingis:
\DeclarePrefChars{'-}
ForenginesthatfullysupportUnicodethesedefaultsareextendedwith
\DeclarePrefChars*{’}
275

\DeclareAutoPunctuation{hcharactersi}
Thiscommanddefinesthepunctuationmarkstobeconsideredbythecitationcom-
mandsastheyscanaheadforpunctuation. Notethathcharactersiisanundelimited
listofcharacters. Validhcharactersiareperiod,comma,semicolon,colon,exclama-
tionandquestionmark. Thedefaultsettingis:
\DeclareAutoPunctuation{.,;:!?}
Thisdefinitionisrestoredautomaticallywhenevertheautopunctpackageoption
is set to true. Executing \DeclareAutoPunctuation{} is equivalent to setting
autopunct=false,i.e.,itdisablesthisfeature.
\DeclareCapitalPunctuation{hcharactersi}
Whenbiblatexinsertslocalisationstrings,i.e.,keytermssuchas‘edition’or‘vol-
ume’,itautomaticallycapitalizesthemafterterminalpunctuationmarks. Thiscom-
mand defines the punctuation marks which will cause localisation strings to be
capitalizedifoneofthemprecedesastring. Notethathcharactersiisanundelimited
listofcharacters. Validhcharactersiareperiod,comma,semicolon,colon,exclama-
tionandquestionmark. Thepackagedefaultis:
\DeclareCapitalPunctuation{.!?}
Using\DeclareCapitalPunctuationwithanemptyargumentisequivalenttodis-
ablingautomaticcapitalization. Sincethisfeatureislanguagespecific,thiscommand
must be used in the argument to \DefineBibliographyExtras (when used in the
preamble)or\DeclareBibliographyExtras(whenusedinalocalisationmodule).
See§§3.10and4.9fordetails. Bydefault,stringsarecapitalizedafterperiods,ex-
clamationmarks, andquestionmarks. Allstringsaregenerallycapitalizedatthe
beginningofaparagraph(infactwheneverTeXisinverticalmode).
\DeclarePunctuationPairs{hidentifieri}{hcharactersi}
Use this command to declare valid pairs of punctuation marks. This will affect
the punctuation commands discussed in § 4.7.3. For example, the description of
\addcommastatesthatthiscommandaddsacommaunlessitisprecededbyanother
comma,asemicolon,acolon,oraperiod. Inotherwords,commasafterabbreviation
dots,exclamationmarks,andquestionmarksarepermitted. Thesevalidpairsare
declaredasfollows:
\DeclarePunctuationPairs{comma}{*!?}
Thehidentifieriselectsthecommandtobeconfigured. Theidentifierscorrespond
to the names of the punctuation commands from § 4.7.3 without the \add pre-
fix,i.e.,validhidentifieristringsaredot,comma,semicolon,colon,period,exclam,
question. Thehcharactersiargumentisanundelimitedlistofpunctuationmarks.
Validhcharactersiarecomma,semicolon,colon,period,exclamationmark,question
mark, andasterisk. Aperiodinthehcharactersiargumentdenotesanend-of-sen-
tenceperiod,anasteriskthedotafteranabbreviation. Thisisthedefaultsetup,which
isautomaticallyrestoredwheneverbiblatexswitcheslanguagesandcorresponds
tothebehaviordescribedin§4.7.3:
276

\DeclarePunctuationPairs{dot}{}
\DeclarePunctuationPairs{comma}{*!?}
\DeclarePunctuationPairs{semicolon}{*!?}
\DeclarePunctuationPairs{colon}{*!?}
\DeclarePunctuationPairs{period}{}
\DeclarePunctuationPairs{exclam}{*}
\DeclarePunctuationPairs{question}{*}
Since this feature is language specific, \DeclarePunctuationPairs must be used
in the argument to \DefineBibliographyExtras (when used in the preamble) or
\DeclareBibliographyExtras (when used in a localisation module). See §§ 3.10
and4.9fordetails. Notethatsomelocalisationmodulesmayuseasetupwhichis
differentfromthepackagedefault.39
\DeclareQuotePunctuation{hcharactersi}
This command controls ‘American-style’ punctuation. The \mkbibquote wrapper
from§4.10.4caninteractwiththepunctuationfacilitiesdiscussedin§§4.7.1,4.7.3,
4.7.4. Punctuationmarksafter\mkbibquotewillbemovedinsidethequotesifthey
have been registered with \DeclareQuotePunctuation. Note that hcharactersi is
anundelimitedlistofcharacters. Validhcharactersiareperiod,comma,semicolon,
colon,exclamationandquestionmark. Hereisanexample:
\DeclareQuotePunctuation{.,}
Executing\DeclareQuotePunctuation{}isequivalenttodisablingthisfeature. This
isthepackagedefault. Sincethisfeatureislanguagespecific,thiscommandmustbe
usedintheargumentto\DefineBibliographyExtras(whenusedinthepreamble)
or\DeclareBibliographyExtras(whenusedinalocalisationmodule). See§§3.10
and4.9fordetails. Seealso§3.13.1.
\uspunctuation A shorthand using the lower-level commands \DeclareQuotePunctuation and
\DeclarePunctuationPairstoactivate‘American-style’punctuation. See§3.13.1
fordetails. Thisshorthandisprovidedforconvenienceonly. Theeffectivesettings
areappliedbythelower-levelcommands.
\stdpunctuation Undoesthesettingsappliedby\uspunctuation,restoringstandardpunctuation. As
standardpunctuationisthedefaultsetting,youonlyneedthiscommandtooverride
apreviouslyexecuted\uspunctuationcommand. See§3.13.1fordetails.
4.7.6 CorrectingPunctuationTracking
Thefacilitiesforpunctuationtrackingandautomaticcapitalizationareveryreliable
undernormalcircumstances,buttherearealwaysmarginalcaseswhichmayrequire
manualintervention. Typicalcasesarelocalisationstringsprintedasthefirstwordin
afootnote(whichisusuallytreatedasthebeginningofaparagraphasfarascapital-
izationisconcerned,butTeXisnotinverticalmodeatthispoint)orpunctuationafter
periodswhicharenotreallyend-of-sentenceperiods(forexample,afteranellipsis
like“[…]”acommandsuchas\addperiodwoulddonothingsinceparenthesesand
bracketsaretransparenttothepunctuationtracker). Insuchcases,usethefollowing
39Asofthiswriting,theamericanmoduleusesdifferentsettingsfor‘American-style’punctuation.
277

commandsinbibliographyandcitationstylestomarkthebeginningormiddleofa
sentenceifandwhererequired:
\bibsentence Thiscommandmarksthebeginningofasentence. Alocalisationstringimmediately
afterthiscommandwillbecapitalizedandthepunctuationtrackerisreset,i.e.,this
commandhidesallprecedingpunctuationmarksfromthepunctuationtrackerand
enforcescapitalization.
\midsentence Thiscommandmarksthemiddleofasentence. Alocalisationstringimmediately
afterthiscommandwillnotbecapitalizedandthepunctuationtrackerisreset,i.e.,
thiscommandhidesallprecedingpunctuationmarksfromthepunctuationtracker
andsuppressescapitalization.
\midsentence* Thestarredvariantof\midsentencediffersfromtheregularoneinthatapreceding
abbreviation dot is not hidden from the punctuation tracker, i.e., any code after
\midsentence*willseeaprecedingabbreviationdot. Allotherpunctuationmarks
arehiddenfromthepunctuationtrackerandcapitalizationissuppressed.
4.8 LocalizationStrings
Localizationstringsarekeytermssuchas‘edition’or‘volume’whichareautomati-
callytranslatedbybiblatex’slocalisationmodules. See§4.9foranoverviewand
§4.9.2foralistofallstringssupportedbydefault. Thecommandsinthissectionare
usedtoprintthelocalisedterm.
\bibstring[hwrapperi]{hkeyi}
Printsthelocalisationstringhkeyi,wherehkeyiisanidentifierinlowercaseletters
(see§4.9.2). Thestringwillbecapitalizedasrequired,see§4.7.5fordetails. Depend-
ingontheabbreviatepackageoptionfrom§3.1.2.1,\bibstringprintstheshortor
thelongversionofthestring. Iflocalisationstringsarenested,i.e.,if\bibstringis
usedinanotherstring,itwillbehavelike\bibxstring. Ifthehwrapperiargument
isgiven, thestringispassedtothehwrapperiforformatting. Thisisintendedfor
fontcommandssuchas\emph.
\biblstring[hwrapperi]{hkeyi}
Similarto\bibstringbutalwaysprintsthelongstring,ignoringtheabbreviate
option.
\bibsstring[hwrapperi]{hkeyi}
Similarto\bibstringbutalwaysprintstheshortstring,ignoringtheabbreviate
option.
\bibncpstring[hwrapperi]{hkeyi}
Similarto\bibstringbutthetermisnevercapitalized.
\bibncplstring[hwrapperi]{hkeyi}
Similarto\biblstringbutthetermisnevercapitalized.
\bibncpsstring[hwrapperi]{hkeyi}
Similarto\bibsstringbutthetermisnevercapitalized.
278

\bibcpstring[hwrapperi]{hkeyi}
Similarto\bibstringbutthetermisalwayscapitalized.
\bibcplstring[hwrapperi]{hkeyi}
Similarto\biblstringbutthetermisalwayscapitalized.
\bibcpsstring[hwrapperi]{hkeyi}
Similarto\bibsstringbutthetermisalwayscapitalized.
\bibucstring[hwrapperi]{hkeyi}
Similarto\bibstringbutthewholetermisuppercased.
\bibuclstring[hwrapperi]{hkeyi}
Similarto\biblstringbutthewholetermisuppercased.
\bibucsstring[hwrapperi]{hkeyi}
Similarto\bibsstringbutthewholetermisuppercased.
\biblcstring[hwrapperi]{hkeyi}
Similarto\bibstringbutthewholetermislowercased.
\biblclstring[hwrapperi]{hkeyi}
Similarto\biblstringbutthewholetermislowercased.
\biblcsstring[hwrapperi]{hkeyi}
Similarto\bibsstringbutthewholetermislowercased.
\bibxstring{hkeyi}
Asimplifiedbutexpandableversionof\bibstring. Notethatthisvariantdoesnot
capitalizeautomatically,nordoesithookintothepunctuationtracker. Itisintended
forspecialcasesinwhichstringsarenestedoranexpandedlocalisationstringis
requiredinatest.
\bibxlstring[hwrapperi]{hkeyi}
Similar to \bibxstring but always uses the long string, ignoring the abbreviate
option.
\bibxsstring[hwrapperi]{hkeyi}
Similarto\bibxstringbutalwaysusestheshortstring,ignoringtheabbreviate
option.
\mainlang
Deprecated
Switchesfromthecurrentlanguagetothemaindocumentlanguage. Thiscommand
isdeprecated. Usethetext-macro\textmainlanginstead. Withbabelthiscommand
willneedtobewrappedintotwo groupstohavepurelylocaleffect.
279

\textmainlang{htexti}
Locallyswitchesfromthecurrentlanguagetothemaindocumentlanguagetotypeset
htexti. Thiscanbeusedthehwrapperiargumentinthelocalisationstringcommands
above.
\texouterlang{htexti}
Locallyswitchesfromthecurrentlanguagetothesurroundinglanguage(whichwas
notselectedbybiblatex)totypesethtexti. Thiscanbeusedthehwrapperiargument
inthelocalisationstringcommandsabove.
It is possible to add bibliography strings to a bibliography string set to apply
additionalformatting.
\DeclareBibstringSet{hsetnamei}{hkey,…i}
Thiscommandsassignsallhkeyistothebibliographystringsethsetnamei.
\UndeclareBibstringSet{hsetnamei}
Removethebibliographystringsethsetnamei. Anyformattingdefinitionswillalso
becleared.
\UndeclareBibstringSets
Removeallexistingbibliographystringsetswith\UndeclareBibstringSet.
\DeclareBibstringSetFormat{hsetnamei}{hcodei}
Defines the bibliography string format for hsetnamei. The format works exactly
likeanadditionalhwrapperiformatfor\bibstring. hcodeiisexecutedwhenevera
bibliography string of hsetnamei is printed. The text of the bibliography string is
passedtohcodeiasfirstandonlyargument.
\UndeclareBibstringSetFormat{hsetnamei}
Removeanybibliographystringsetformatdefinedforhsetnamei.
Bibliographystringsetscanbeusefultoapplyadditionalformattingtoanumber
ofbibliographystringsatthesametime. Thesecommandsareintendedforusein
language modules. For example in French typography it is customary to italicise
Latinterms. TheFrenchlanguagemodulecandefineanewbibliographystringset
calledlatinforallLatinstringsandapplyadditionalformattingonlytothesestrings.
Itisnotrecommendedtoapplytheformattingdirectlyinthebibliographystring
definitions,sincethatcaninterferewiththecapitalisationfunction. Assumingthat
theFrenchlanguage.lbxfileonlydefinestwoLatinstrings,andothersandibidem,
the.lbxfilewouldcontainthefollowing.
\DeclareBibliographyExtras{%
…
\DeclareBibstringSet{latin}{andothers,ibidem}%
\DeclareBibstringSetFormat{latin}{\mkbibemph{#1}}%
…
}
280

\UndeclareBibliographyExtras{%
…
\UndeclareBibstringSet{latin}%
…
}
Note that the defined sets should be undeclared after use to avoid side effects for
otherlanguages.
4.9 LocalizationModules
Alocalisationmoduleprovidestranslationsforkeytermssuchas‘edition’or‘volume’
as well as definitions for language specific features such as the date format and
ordinals. Thesedefinitionsareprovidedinfileswiththesuffixlbx. Thebasename
of the file must be a language name known to the babel/polyglossia packages.
Thelbxfilesmayalsobeusedtomapbabel/polyglossialanguagenamestothe
backendmodulesofthebiblatexpackage. Alllocalisationmodulesareloadedon
demandinthedocumentbody. Notethatthecontentsofthefileareprocessedina
groupandthatthecategorycodeofthecharacter@istemporarilysetto‘letter’.
4.9.1 LocalizationCommands
The user-level versions of the localisation commands were already introduced in
§ 3.10. When used in lbx files, however, the syntax of localisation commands is
differentfromtheusersyntaxinthepreambleandtheconfigurationfile. Whenused
inlocalisationfiles,thereisnoneedtospecifythehlanguageibecausethemapping
ofstringstoalanguageisalreadyprovidedbythenameofthelbxfile.
\DeclareBibliographyStrings{hdefinitionsi}
Thiscommandisonlyavailableinlbxfiles. Itisusedtodefinelocalisationstrings.
The hdefinitionsi consist of hkeyi=hvaluei pairs which assign an expression to an
identifier. Acompletelistofallkeyssupportedbydefaultisgivenis§4.9.2. Notethat
thesyntaxofthevalueisdifferentinlbxfiles. Thevalueassignedtoakeyconsists
oftwoexpressions,eachofwhichiswrappedinanadditionalpairofbrackets. This
isbestshownbyexample:
\DeclareBibliographyStrings{%
bibliography = {{Bibliography}{Bibliography}},
shorthands = {{List of Abbreviations}{Abbreviations}},
editor = {{editor}{ed.}},
editors = {{editors}{eds.}},
}
Thefirstvalueisthelong,writtenoutexpression,thesecondoneisanabbreviated
orshortform. Bothstringsmustalwaysbegiveneventhoughtheymaybeidentical
ifanexpressionisalways(ornever)abbreviated. Dependingonthesettingofthe
abbreviate package option (see § 3.1.2.1), biblatex selects one expression when
loading the lbx file. There is also a special key named inherit which copies the
stringsfromadifferentlanguage. Thisisintendedforlanguageswhichonlydifferin
afewexpressions,suchasGermanandAustrianorAmericanandBritishEnglish.
Forexample,herearethecompletedefinitionsforAustrian:
281

\DeclareBibliographyStrings{%
| inherit | = {german},             |     |     |     |     |     |
| ------- | ----------------------- | --- | --- | --- | --- | --- |
| january | = {{J\"anner}{J\"an.}}, |     |     |     |     |     |
}
The above examples are slightly simplified. Real localisation files should use the
punctuationandformattingcommandsdiscussedin§§4.7.3and3.12insteadofliteral
| punctuation. | Hereisanexcerptfromareallocalisationfile: |                                 |                                    |       |           |     |
| ------------ | ----------------------------------------- | ------------------------------- | ---------------------------------- | ----- | --------- | --- |
| bibliography | =                                         | {{Bibliography}{Bibliography}}, |                                    |       |           |     |
| shorthands   | =                                         | {{List                          | of Abbreviations}{Abbreviations}}, |       |           |     |
| editor       | =                                         | {{editor}{ed\adddot}},          |                                    |       |           |     |
| editors      | =                                         | {{editors}{eds\adddot}},        |                                    |       |           |     |
| byeditor     | =                                         | {{edited                        | by}{ed\adddotspace                 | by}}, |           |     |
| mathesis     | =                                         | {{Master's                      | thesis}{MA\addabbrvspace           |       | thesis}}, |     |
Notethehandlingofabbreviationdots,thespacinginabbreviatedexpressions,and
the capitalization in the example above. All expressions should be capitalized as
theyusuallyarewhenusedinthemiddleofasentence. Thebiblatexpackagewill
automaticallycapitalizethefirstwordwhenrequiredatthebeginningofasentence,
see \DeclareCapitalPunctuation in § 4.7.5 for details. Expressions intended for
useinheadingsarespecial. Theyshouldbecapitalizedinawaythatissuitablefor
titlingandshouldnotbeabbreviated(buttheymayhaveashortform).
\InheritBibliographyStrings{hlanguagei}
This command is only available in lbx files. It copies the localisation strings for
hlanguageitothecurrentlanguage,asspecifiedbythenameofthelbxfile.
\DeclareBibliographyExtras{hcodei}
This command is only available in files. It is used to adapt language specific
lbx
featuressuchasthedateformatandordinals. Thehcodei,whichmaybearbitrary
LaTeXcode,willusuallyconsistofredefinitionsoftheformattingcommandsfrom
§4.10.2.
\UndeclareBibliographyExtras{hcodei}
This command is only available in lbx files. It is used to restore any formatting
commandsmodifiedwith\DeclareBibliographyExtras. Ifaredefinedcommandis
includedin§4.10.2, thereisnoneedtorestoreitspreviousdefinitionsincethese
commandsarelocalisedbyalllanguagemodulesanyway.
\InheritBibliographyExtras{hlanguagei}
This command is only available in lbx files. It copies the bibliography extras for
hlanguageitothecurrentlanguage,asspecifiedbythenameofthelbxfile.
\DeclareHyphenationExceptions{htexti}
| This command | corresponds | to  |     |     | from § 3.10. | The |
| ------------ | ----------- | --- | --- | --- | ------------ | --- |
\DefineHyphenationExceptions
differenceisthatitisonlyavailableinlbxfilesandthatthehlanguageiargumentis
omitted. Thehyphenationexceptionswillaffectthelanguageofthelbxfilecurrently
beingprocessed.
282

\DeclareRedundantLanguages{hlanguage,language,…i}{hlangid,langid,…i}
Thiscommandprovidesthelanguagemappingsrequiredbytheclearlangoption
from § 3.1.2.1. The hlanguagei is the string given in the language field (without
the optional lang prefix); hlangidi is babel/polyglossia’s language identifier, as
givenintheoptionalargumentof\usepackagewhenloadingbabelortheargument
of \setdefaultlanguage or \setotherlanguages when using polyglossia. This
command may be used in lbx files or in the document preamble. Here are some
examples:
\DeclareRedundantLanguages{french}{french}
\DeclareRedundantLanguages{german}{german,ngerman,austrian,naustrian,
nswissgerman,swissgerman}
\DeclareRedundantLanguages{english,american}{english,american,british
,→ ,
canadian,australian,newzealand,USenglish,UKenglish}
Notethatthisfeatureneedstobeenabledgloballywiththeclearlangoptionfrom
§3.1.2.1. Ifitisdisabled,allmappingswillbeignored. Ifthehlangidiparameteris
blank,biblatexwillclearthemappingsforthecorrespondinghlanguagei,i.e.,the
featurewillbedisabledforthishlanguageionly.
\DeclareLanguageMapping{hlanguagei}{hfilei}
This command maps a babel/polyglossia language identifier to an lbx file. The
hlanguagei must be a language name known to the babel/polyglossia package,
i.e., one of the identifiers listed in table 2. The hfilei argument is the name of an
alternativelbxfilewithoutthe.lbxsuffix. Declaringthesamemappingmorethan
onceispossible. Subsequentdeclarationswillsimplyoverwriteanypreviousones.
Thiscommandmayonlybeusedinthepreamble. See§4.11.9forfurtherdetails.
\DeclareLanguageMappingSuffix{hsuffixi}
Thiscommanddefinesalanguagefilesuffixwhichwillbeaddedwhenlookingfor
.lbxlanguagestringdefinitionfiles. Thisisintendedforstyleswhichprovidetheir
own.lbxfilessothattheywillbeusedautomatically. Forexample,theAPAstyle
defines:
\DeclareLanguageMappingSuffix{-apa}
When the document language is ‘german’, biblatex will look for the file
german-apa.lbx which defines some APA specific strings and in turn loads
german.lbx. If\DeclareLanguageMappingisdefinedforalanguage,thisoverrides
\DeclareLanguageMappingSuffix.
Thesuffixwillbeappliedtootherlanguagefilesloadedrecursivelybytheloadingof
alanguagefile. Forexample,giventhesuffixdefinedabove,whenloading‘ngerman’,
biblatexwilllookforthefilengerman-apa.lbxandifthisrecursivelyloads‘german’,
thenbiblatexwilllookforgerman-apa.lbx. Infiniterecursionisofcourseavoided.
283

\NewBibliographyString{hkeyi}
This command, which may be used in the preamble (including cbx and bbx
files) as well as in lbx files, declares new localisation strings, i.e., it initializes
a new hkeyi to be used in the hdefinitionsi of \DefineBibliographyStrings or
\DeclareBibliographyStrings. The hkeyi argument may also be a comma-sep-
aratedlistofkeynames. Whenusedinanlbx,thehkeyiisinitializedonlyforthe
languagespecifiedbythenameofthelbxfile. Thekeyslistedin§4.9.2aredefined
bydefault.
4.9.2 LocalizationKeys
The localisation keys in this section are defined by default and covered by the
localisationfileswhichcomewithbiblatex. Notethatthesestringsareonlyavailable
in citations, the bibliography and bibliography lists. All expressions should be
capitalizedastheyusuallyarewhenusedinthemiddleofasentence. biblatexwill
capitalizethemautomaticallyatthebeginningofasentence. Theonlyexceptionsto
theserulesarethethreestringsintendedforuseinheadings.
4.9.2.1 Headings
Thefollowingstringsarespecialbecausetheyareintendedforuseinheadingsand
madeavailablegloballyviamacros. Forthisreason,theyshouldbecapitalizedfor
useinheadingsandtheymustnotincludeanylocalcommandswhicharepartof
biblatex’sauthorinterface.
bibliography Theterm‘bibliography’,alsoavailableas\bibname.
references Theterm‘references’,alsoavailableas\refname.
shorthands Theterm‘listofshorthands’or‘listofabbreviations’,alsoavailableas
\biblistname.
4.9.2.2 Roles,ExpressedasFunctions
Thefollowingkeysrefertoroleswhichareexpressedasafunction(‘editor’,‘transla-
tor’)ratherthanasanaction(‘editedby’,‘translatedby’).
editor Theterm‘editor’,referringtothemaineditor. Thisisthemostgenericeditorialrole.
editors Thepluralformofeditor.
compiler Theterm‘compiler’,referringtoaneditorwhosetaskistocompileawork.
compilers Thepluralformofcompiler.
founder Theterm‘founder’,referringtoafoundingeditor.
founders Thepluralformoffounder.
continuator Anexpressionlike‘continuator’,‘continuation’,or‘continued’,referringtoapast
editorwhocontinuedtheworkofthefoundingeditorbutwassubsequently
replacedbythecurrenteditor.
continuators Thepluralformofcontinuator.
redactor Theterm‘redactor’,referringtoasecondaryeditor.
redactors Thepluralformofredactor.
reviser Theterm‘reviser’,referringtoasecondaryeditor.
284

revisers Thepluralformofreviser.
collaborator Atermlike‘collaborator’,‘collaboration’,‘cooperator’,or‘cooperation’,referringto
asecondaryeditor.
collaborators Thepluralformofcollaborator.
translator Theterm‘translator’.
translators Thepluralformoftranslator.
commentator Theterm‘commentator’,referringtotheauthorofacommentarytoawork.
commentators Thepluralformofcommentators.
annotator Theterm‘annotator’,referringtotheauthorofannotationstoawork.
annotators Thepluralformofannotators.
organizer Theterm‘organizer’,referringtotheorganizerofaneventorwork.
organizers Thepluralformoforganizer.
4.9.2.3 ConcatenatedEditorRoles,ExpressedasFunctions
Thefollowingkeysaresimilarinfunctiontoeditor,translator,etc. Theyareused
to indicate additional roles of the editor, e.g., ‘editor and translator’, ‘editor and
foreword’.
editortr Usedifeditor/translatorareidentical.
editorstr Thepluralformofeditortr.
editorco Usedifeditor/commentatorareidentical.
editorsco Thepluralformofeditorco.
editoran Usedifeditor/annotatorareidentical.
editorsan Thepluralformofeditoran.
editorin Usedifeditor/introductionareidentical.
editorsin Thepluralformofeditorin.
editorfo Usedifeditor/forewordareidentical.
editorsfo Thepluralformofeditorfo.
editoraf Usedifeditor/aftwordareidentical.
editorsaf Thepluralformofeditoraf.
Keysforeditor/translator/hroleicombinations:
editortrco Usedifeditor/translator/commentatorareidentical.
editorstrco Thepluralformofeditortrco.
editortran Usedifeditor/translator/annotatorareidentical.
editorstran Thepluralformofeditortran.
editortrin Usedifeditor/translator/introductionareidentical.
editorstrin Thepluralformofeditortrin.
editortrfo Usedifeditor/translator/forewordareidentical.
editorstrfo Thepluralformofeditortrfo.
editortraf Usedifeditor/translator/aftwordareidentical.
285

editorstraf Thepluralformofeditortraf.
Keysforeditor/commentator/hroleicombinations:
editorcoin Usedifeditor/commentator/introductionareidentical.
editorscoin Thepluralformofeditorcoin.
editorcofo Usedifeditor/commentator/forewordareidentical.
editorscofo Thepluralformofeditorcofo.
editorcoaf Usedifeditor/commentator/aftwordareidentical.
editorscoaf Thepluralformofeditorcoaf.
Keysforeditor/annotator/hroleicombinations:
editoranin Usedifeditor/annotator/introductionareidentical.
editorsanin Thepluralformofeditoranin.
editoranfo Usedifeditor/annotator/forewordareidentical.
editorsanfo Thepluralformofeditoranfo.
editoranaf Usedifeditor/annotator/aftwordareidentical.
editorsanaf Thepluralformofeditoranaf.
Keysforeditor/translator/commentator/hroleicombinations:
editortrcoin Usedifeditor/translator/commentator/introductionareidentical.
editorstrcoin Thepluralformofeditortrcoin.
editortrcofo Usedifeditor/translator/commentator/forewordareidentical.
editorstrcofo Thepluralformofeditortrcofo.
editortrcoaf Usedifeditor/translator/commentator/aftwordareidentical.
editorstrcoaf Thepluralformofeditortrcoaf.
Keysforeditor/annotator/commentator/hroleicombinations:
editortranin Usedifeditor/annotator/commentator/introductionareidentical.
editorstranin Thepluralformofeditortranin.
editortranfo Usedifeditor/annotator/commentator/forewordareidentical.
editorstranfo Thepluralformofeditortranfo.
editortranaf Usedifeditor/annotator/commentator/aftwordareidentical.
editorstranaf Thepluralformofeditortranaf.
4.9.2.4 ConcatenatedTranslatorRoles,ExpressedasFunctions
Thefollowingkeysaresimilarinfunctiontotranslator. Theyareusedtoindicate
additionalrolesofthetranslator,e.g.,‘translatorandcommentator’,‘translatorand
introduction’.
translatorco Usediftranslator/commentatorareidentical.
translatorsco Thepluralformoftranslatorco.
286

translatoran Usediftranslator/annotatorareidentical.
translatorsan Thepluralformoftranslatoran.
translatorin Usediftranslator/introductionareidentical.
translatorsin Thepluralformoftranslatorin.
translatorfo Usediftranslator/forewordareidentical.
translatorsfo Thepluralformoftranslatorfo.
translatoraf Usediftranslator/aftwordareidentical.
translatorsaf Thepluralformoftranslatoraf.
Keysfortranslator/commentator/hroleicombinations:
translatorcoin Usediftranslator/commentator/introductionareidentical.
translatorscoin Thepluralformoftranslatorcoin.
translatorcofo Usediftranslator/commentator/forewordareidentical.
translatorscofo Thepluralformoftranslatorcofo.
translatorcoaf Usediftranslator/commentator/aftwordareidentical.
translatorscoaf Thepluralformoftranslatorcoaf.
Keysfortranslator/annotator/hroleicombinations:
translatoranin Usediftranslator/annotator/introductionareidentical.
translatorsanin Thepluralformoftranslatoranin.
translatoranfo Usediftranslator/annotator/forewordareidentical.
translatorsanfo Thepluralformoftranslatoranfo.
translatoranaf Usediftranslator/annotator/aftwordareidentical.
translatorsanaf Thepluralformoftranslatoranaf.
4.9.2.5 Roles,ExpressedasActions
The following keys refer to roles which are expressed as an action (‘edited by’,
‘translatedby’)ratherthanasafunction(‘editor’,‘translator’).
byauthor Theexpression‘[created]byhnamei’.
byeditor Theexpression‘editedbyhnamei’.
bycompiler Theexpression‘compiledbyhnamei’.
byfounder Theexpression‘foundedbyhnamei’.
bycontinuator Theexpression‘continuedbyhnamei’.
byredactor Theexpression‘redactedbyhnamei’.
byreviser Theexpression‘revisedbyhnamei’.
byreviewer Theexpression‘reviewedbyhnamei’.
bycollaborator Anexpressionlike‘incollaborationwithhnamei’or‘incooperationwithhnamei’.
bytranslator Theexpression‘translatedbyhnamei’or‘translatedfromhlanguageibyhnamei’.
bycommentator Theexpression‘commentedbyhnamei’.
byannotator Theexpression‘annotatedbyhnamei’.
byorganizer Theexpression‘[organized]byhnamei’.
287

4.9.2.6 ConcatenatedEditorRoles,ExpressedasActions
Thefollowingkeysaresimilarinfunctiontobyeditor,bytranslator,etc. Theyare
usedtoindicateadditionalrolesoftheeditor,e.g.,‘editedandtranslatedby’,‘edited
andfurnishedwithanintroductionby’,‘edited,withaforeword,by’.
byeditortr Usedifeditor/translatorareidentical.
byeditorco Usedifeditor/commentatorareidentical.
byeditoran Usedifeditor/annotatorareidentical.
byeditorin Usedifeditor/introductionareidentical.
byeditorfo Usedifeditor/forewordareidentical.
byeditoraf Usedifeditor/aftwordareidentical.
Keysforeditor/translator/hroleicombinations:
byeditortrco Usedifeditor/translator/commentatorareidentical.
byeditortran Usedifeditor/translator/annotatorareidentical.
byeditortrin Usedifeditor/translator/introductionareidentical.
byeditortrfo Usedifeditor/translator/forewordareidentical.
byeditortraf Usedifeditor/translator/aftwordareidentical.
Keysforeditor/commentator/hroleicombinations:
byeditorcoin Usedifeditor/commentator/introductionareidentical.
byeditorcofo Usedifeditor/commentator/forewordareidentical.
byeditorcoaf Usedifeditor/commentator/aftwordareidentical.
Keysforeditor/annotator/hroleicombinations:
byeditoranin Usedifeditor/annotator/introductionareidentical.
byeditoranfo Usedifeditor/annotator/forewordareidentical.
byeditoranaf Usedifeditor/annotator/aftwordareidentical.
Keysforeditor/translator/commentator/hroleicombinations:
byeditortrcoin Usedifeditor/translator/commentator/introductionareidentical.
byeditortrcofo Usedifeditor/translator/commentator/forewordareidentical.
byeditortrcoaf Usedifeditor/translator/commentator/aftwordareidentical.
Keysforeditor/translator/annotator/hroleicombinations:
byeditortranin Usedifeditor/annotator/commentator/introductionareidentical.
byeditortranfo Usedifeditor/annotator/commentator/forewordareidentical.
byeditortranaf Usedifeditor/annotator/commentator/aftwordareidentical.
288

4.9.2.7 ConcatenatedTranslatorRoles,ExpressedasActions
Thefollowingkeysaresimilarinfunctiontobytranslator. Theyareusedtoindicate
additionalrolesofthetranslator,e.g.,‘translatedandcommentedby’,‘translated
andfurnishedwithanintroductionby’,‘translated,withaforeword,by’.
bytranslatorco Usediftranslator/commentatorareidentical.
bytranslatoran Usediftranslator/annotatorareidentical.
bytranslatorin Usediftranslator/introductionareidentical.
bytranslatorfo Usediftranslator/forewordareidentical.
bytranslatoraf Usediftranslator/aftwordareidentical.
Keysfortranslator/commentator/hroleicombinations:
bytranslatorcoin Usediftranslator/commentator/introductionareidentical.
bytranslatorcofo Usediftranslator/commentator/forewordareidentical.
bytranslatorcoaf Usediftranslator/commentator/aftwordareidentical.
Keysfortranslator/annotator/hroleicombinations:
bytranslatoranin Usediftranslator/annotator/introductionareidentical.
bytranslatoranfo Usediftranslator/annotator/forewordareidentical.
bytranslatoranaf Usediftranslator/annotator/aftwordareidentical.
4.9.2.8 Roles,ExpressedasObjects
Roleswhicharerelatedtosupplementarymaterialmayalsobeexpressedasobjects
(‘with a commentary by’) rather than as functions (‘commentator’) or as actions
(‘commentedby’).
withcommentator Theexpression‘withacommentarybyhnamei’.
withannotator Theexpression‘withannotationsbyhnamei’.
withintroduction Theexpression‘withanintroductionbyhnamei’.
withforeword Theexpression‘withaforewordbyhnamei’.
withafterword Theexpression‘withanafterwordbyhnamei’.
4.9.2.9 SupplementaryMaterial
commentary Theterm‘commentary’.
annotations Theterm‘annotations’.
introduction Theterm‘introduction’.
foreword Theterm‘foreword’.
afterword Theterm‘afterword’.
289

4.9.2.10 PublicationDetails
volume Theterm‘volume’,referringtoabook.
volumes Thepluralformofvolume.
involumes Theterm‘in’,asusedinexpressionslike‘inhnumberofvolumesivolumes’.
jourvol Theterm‘volume’,referringtoajournal.
jourser Theterm‘series’,referringtoajournal.
book Theterm‘book’,referringtoadocumentdivision.
part Theterm‘part’,referringtoapartofabookoraperiodical.
issue Theterm‘issue’,referringtoaperiodical.
newseries Theexpression‘newseries’,referringtoajournal.
oldseries Theexpression‘oldseries’,referringtoajournal.
edition Theterm‘edition’.
in Theterm‘in’,referringtothetitleofaworkpublishedaspartofanotherone,e.g.,
‘htitleofarticleiinhtitleofjournali’.
inseries Theterm‘in’,asusedinexpressionslike‘volumehnumberiinhnameofseriesi’.
ofseries Theterm‘of’,asusedinexpressionslike‘volumehnumberiofhnameofseriesi’.
number Theterm‘number’,referringtoanissueofajournal.
chapter Theterm‘chapter’,referringtoachapterinabook.
version Theterm‘version’,referringtoarevisionnumber.
reprint Theterm‘reprint’.
reprintof Theexpression‘reprintofhtitlei’.
reprintas Theexpression‘reprintedashtitlei’.
reprintfrom Theexpression‘reprintedfromhtitlei’.
translationof Theexpression‘translationofhtitlei’.
translationas Theexpression‘translatedashtitlei’.
translationfrom Theexpression‘translatedfrom[the]hlanguagei’.
reviewof Theexpression‘reviewofhtitlei’.
origpubas Theexpression‘originallypublishedashtitlei’.
origpubin Theexpression‘originallypublishedinhyeari’.
astitle Theterm‘as’,asusedinexpressionslike‘publishedbyhpublisheriashtitlei’.
bypublisher Theterm‘by’,asusedinexpressionslike‘publishedbyhpublisheri’.
4.9.2.11 PublicationState
inpreparation Theexpression‘inpreparation’(themanuscriptisbeingpreparedforpublication).
submitted Theexpression‘submitted’(themanuscripthasbeensubmittedtoajournalor
conference).
forthcoming Theexpression‘forthcoming’(themanuscripthasbeenacceptedbyapressor
journal).
inpress Theexpression‘inpress’(themanuscriptisfullycopyeditedandoutoftheauthor’s
hands;itisinthefinalstagesoftheproductionprocess).
prepublished Theexpression‘pre-published’(themanuscriptispublishedinapreliminaryformor
location,suchasonlineversioninadvanceofprintpublication).
290

4.9.2.12 Pagination
page Theterm‘page’.
pages Thepluralformofpage.
column Theterm‘column’,referringtoacolumnonapage.
columns Thepluralformofcolumn.
section Theterm‘section’,referringtoadocumentdivision(usuallyabbreviatedas§).
sections Thepluralformofsection(usuallyabbreviatedas§§).
paragraph Theterm‘paragraph’(i.e.,ablockoftext,nottobeconfusedwithsection).
paragraphs Thepluralformofparagraph.
verse Theterm‘verse’asusedwhenreferringtoaworkwhichiscitedbyversenumbers.
verses Thepluralformofverse.
line Theterm‘line’asusedwhenreferringtoaworkwhichiscitedbylinenumbers.
lines Thepluralformofline.
pagetotal Theterm‘page’asusedin\mkpageprefix.
pagetotals Thepluralformofpagetotal.
columntotal Theterm‘column’,referringtoacolumnonapage,asusedin\mkpageprefix.
columntotals Thepluralformofcolumntotal.
sectiontotal Theterm‘section’,referringtoadocumentdivision(usuallyabbreviatedas§),as
usedin\mkpageprefix.
sectiontotals Thepluralformofsectiontotal(usuallyabbreviatedas§§).
paragraphtotal Theterm‘paragraph’(i.e.,ablockoftext,nottobeconfusedwithsection)asused
in\mkpageprefix.
paragraphtotals Thepluralformofparagraphtotal.
versetotal Theterm‘verse’asusedwhenreferringtoaworkwhichiscitedbyversenumbers
whenusedin\mkpageprefix.
versetotals Thepluralformofversetotal.
linetotal Theterm‘line’asusedwhenreferringtoaworkwhichiscitedbylinenumbers
whenusedin\mkpageprefix.
linetotals Thepluralformoflinetotal.
4.9.2.13 Types
Thefollowingkeysaretypicallyusedinthetypefieldof@thesis,@report,@misc,
andotherentries:
bathesis Anexpressionequivalenttotheterm‘Bachelor’sthesis’.
mathesis Anexpressionequivalenttotheterm‘Master’sthesis’.
phdthesis Theterm‘PhDthesis’,‘PhDdissertation’,‘doctoralthesis’,etc.
candthesis Anexpressionequivalenttotheterm‘Candidatethesis’. Usedfor‘Candidate’
degreesthathavenoclearequivalenttotheMaster’sordoctorallevel.
techreport Theterm‘technicalreport’.
resreport Theterm‘researchreport’.
291

software Theterm‘computersoftware’.
datacd Theterm‘datacd’or‘cd-rom’.
audiocd Theterm‘audiocd’.
4.9.2.14 Miscellaneous
nodate Thetermtouseinplaceofadatewhenthereisnodateforanentrye.g.,‘n.d.’
and Theterm‘and’,asusedinalistofauthorsoreditors,forexample.
andothers Theexpression‘andothers’or‘etalii’,usedtomarkthetruncationofanamelist.
andmore Likeandothersbutusedtomarkthetruncationofaliterallist.
4.9.2.15 Labels
Thefollowingstringsareintendedforuseaslabels,e.g.,‘Address: hurli’or‘Abstract:
habstracti’.
url Theterm‘address’inthesenseofaninternetaddress. Thisstringisnotusedbythe
standardstyles.
urlfrom Anexpressionlike‘availablefromhurli’or‘availableathurli’. Thisstringisnot
usedbythestandardstyles.
urlseen Anexpressionlike‘accessedonhdatei’,‘retrievedonhdatei’,‘visitedonhdatei’,
referringtotheaccessdateofanonlineresource.
file Theterm‘file’.
library Theterm‘library’.
abstract Theterm‘abstract’.
annotation Theterm‘annotations’.
4.9.2.16 Citations
Traditionalscholarlyexpressionsusedincitations:
idem ThetermequivalenttotheLatin‘idem’(‘thesame[person]’).
idemsf Thefemininesingularformofidem.
idemsm Themasculinesingularformofidem.
idemsn Theneutersingularformofidem.
idempf Thefemininepluralformofidem.
idempm Themasculinepluralformofidem.
idempn Theneuterpluralformofidem.
idempp Thepluralformofidemsuitableforamixedgenderlistofnames.
ibidem ThetermequivalenttotheLatin‘ibidem’(‘inthesameplace’).
opcit ThetermequivalenttotheLatinterm‘operecitato’(‘[in]thework[already]cited’).
loccit ThetermequivalenttotheLatinterm‘lococitato’(‘[at]theplace[already]cited’).
confer ThetermequivalenttotheLatin‘confer’(‘compare’).
sequens ThetermequivalenttotheLatin‘sequens’(‘[and]thefollowing[page]’),asusedto
indicatearangeoftwopageswhenonlythestartingpageisprovided(e.g.,‘25sq.’
or‘25f.’ insteadof‘25–26’).
292

sequentes ThetermequivalenttotheLatin‘sequentes’(‘[and]thefollowing[pages]’),asused
toindicate,dependingonconvention,eitherarangeofexactlythreepagesoran
open-endedrangeofpages(>2)whenonlythestartingpageisprovided(e.g.,
‘25sqq.’ or‘25ff.’).
passim ThetermequivalenttotheLatin‘passim’(‘throughout’,‘hereandthere’,
‘scatteredly’).
Otherexpressionsfrequentlyusedincitations:
see Theterm‘see’.
seealso Theexpression‘seealso’.
seenote Anexpressionlike‘seenotehfootnotei’or‘asinhfootnotei’,usedtorefertoa
previousfootnoteinacitation.
backrefpage Anexpressionlike‘seepagehpagei’or‘citedonpagehpagei’,usedtointroduce
backreferencesinthebibliography.
backrefpages Thepluralformofbackrefpage,e.g.,‘seepageshpagesi’or‘citedonpageshpagesi’.
quotedin Anexpressionlike‘quotedinhcitationi’,usedwhenquotingapassagewhichwas
alreadyaquotationinthecitedwork.
citedas Anexpressionlike‘henceforthcitedashshorthandi’,usedtointroduceashorthand
inacitation.
thiscite Theexpressionusedinsomeverbosecitationstylestodifferentiatebetweenthe
pagerangeoftheciteditem(typicallyanarticleinajournal,collection,or
conferenceproceedings)andthepagenumberthecitationrefersto. Forexample:
“Author,Title,in: Book,pp. 45–61,thiscitep. 52.”
4.9.2.17 MonthNames
january Thename‘January’.
february Thename‘February’.
march Thename‘March’.
april Thename‘April’.
may Thename‘May’.
june Thename‘June’.
july Thename‘July’.
august Thename‘August’.
september Thename‘September’.
october Thename‘October’.
november Thename‘November’.
december Thename‘December’.
4.9.2.18 LanguageNames
langamerican Thelanguage‘American’or‘AmericanEnglish’.
langbasque Thelanguage‘Basque’.
langbrazilian Thelanguage‘Brazilian’or‘BrazilianPortuguese’.
293

langbulgarian Thelanguage‘Bulgarian’.
langcatalan Thelanguage‘Catalan’.
langcroatian Thelanguage‘Croatian’.
langczech Thelanguage‘Czech’.
langdanish Thelanguage‘Danish’.
langdutch Thelanguage‘Dutch’.
langenglish Thelanguage‘English’.
langestonian Thelanguage‘Estonian’.
langfinnish Thelanguage‘Finnish’.
langfrench Thelanguage‘French’.
langgerman Thelanguage‘German’.
langgreek Thelanguage‘Greek’.
langhungarian Thelanguage‘Hungarian’.
langitalian Thelanguage‘Italian’.
langjapanese Thelanguage‘Japanese’.
langlatin Thelanguage‘Latin’.
langlatvian Thelanguage‘Latvian’.
langlithuanian Thelanguage‘Lithuanian’.
langmarathi Thelanguage‘Marathi’.
langnorwegian Thelanguage‘Norwegian’.
langpolish Thelanguage‘Polish’.
langportuguese Thelanguage‘Portuguese’.
langromanian Thelanguage‘Romanian’.
langrussian Thelanguage‘Russian’.
langserbian Thelanguage‘Serbian’.
langslovak Thelanguage‘Slovak’.
langslovene Thelanguage‘Slovene’.
langspanish Thelanguage‘Spanish’.
langswedish Thelanguage‘Swedish’.
langturkish Thelanguage‘Turkish’.
langukrainian Thelanguage‘Ukrainian’.
The following strings are intended for use in phrases like ‘translated from [the]
Englishbyhtranslatori’:
fromamerican Theexpression‘from[the]American’or‘from[the]AmericanEnglish’.
frombasque Theexpression‘from[the]Basque’.
frombrazilian Theexpression‘from[the]Brazilian’or‘from[the]BrazilianPortuguese’.
frombulgarian Theexpression‘from[the]Bulgarian’.
fromcatalan Theexpression‘from[the]Catalan’.
294

fromcroatian Theexpression‘from[the]Croatian’.
fromczech Theexpression‘from[the]Czech’.
fromdanish Theexpression‘from[the]Danish’.
fromdutch Theexpression‘from[the]Dutch’.
fromenglish Theexpression‘from[the]English’.
fromestonian Theexpression‘from[the]Estonian’.
fromfinnish Theexpression‘from[the]Finnish’.
fromfrench Theexpression‘from[the]French’.
fromgerman Theexpression‘from[the]German’.
fromgreek Theexpression‘from[the]Greek’.
fromhungarian Thelanguage‘from[the]Hungarian’.
fromitalian Theexpression‘from[the]Italian’.
fromjapanese Theexpression‘from[the]Japanese’.
fromlatin Theexpression‘from[the]Latin’.
fromlatvian Theexpression‘from[the]Latvian’.
fromlithuanian Thelanguage‘from[the]Lithuanian’.
frommarathi Theexpression‘from[the]Marathi’.
fromnorwegian Theexpression‘from[the]Norwegian’.
frompolish Theexpression‘from[the]Polish’.
fromportuguese Theexpression‘from[the]Portuguese’.
fromromanian Theexpression‘from[the]Romanian’.
fromrussian Theexpression‘from[the]Russian’.
fromserbian Theexpression‘from[the]Serbian’.
fromslovak Theexpression‘from[the]Slovak’.
fromslovene Theexpression‘from[the]Slovene’.
fromspanish Theexpression‘from[the]Spanish’.
fromswedish Theexpression‘from[the]Swedish’.
fromturkish Theexpression‘from[the]Turkish’.
fromukrainian Theexpression‘from[the]Ukrainian’.
4.9.2.19 CountryNames
Countrynamesarelocalisedbyusingthestringcountryplustheiso-3166country
codeasthekey. Theshortversionofthetranslationshouldbetheiso-3166country
code. Notethatonlyasmallnumberofcountrynamesisdefinedbydefault,mainly
toillustratethisscheme. Thesekeysareusedinthelocationlistof@patententries
buttheymaybeusefulforotherpurposesaswell.
countryde Thename‘Germany’,abbreviatedasDE.
countryeu Thename‘EuropeanUnion’,abbreviatedasEU.
countryep SimilartocountryeubutabbreviatedasEP.Thisisintendedforpatententries.
countryfr Thename‘France’,abbreviatedasFR.
countryuk Thename‘UnitedKingdom’,abbreviated(accordingtoiso-3166)asGB.
countryus Thename‘UnitedStatesofAmerica’,abbreviatedasUS.
295

4.9.2.20 PatentsandPatentRequests
Stringsrelatedtopatentsarelocalisedbyusingthetermpatentplustheiso-3166
countrycodeasthekey. Notethatonlyasmallnumberofpatentkeysisdefined
bydefault,mainlytoillustratethisscheme. Thesekeysareusedinthetypefieldof
@patententries.
patent Thegenericterm‘patent’.
patentde Theexpression‘Germanpatent’.
patenteu Theexpression‘Europeanpatent’.
patentfr Theexpression‘Frenchpatent’.
patentuk Theexpression‘Britishpatent’.
patentus Theexpression‘U.S.patent’.
Patent requests are handled in a similar way, using the string patreq as the base
nameofthekey:
patreq Thegenericterm‘patentrequest’.
patreqde Theexpression‘Germanpatentrequest’.
patreqeu Theexpression‘Europeanpatentrequest’.
patreqfr Theexpression‘Frenchpatentrequest’.
patrequk Theexpression‘Britishpatentrequest’.
patrequs Theexpression‘U.S.patentrequest’.
4.9.2.21 DatesandTimes
Abbreviation strings for standard eras. Both secular and Christian variants are
supported.
commonera Theera‘CE’
beforecommonera Theera‘BCE’
annodomini Theera‘AD’
beforechrist Theera‘BC’
Abbreviationstringsfor‘circa’dates:
circa Thestring‘circa’
Abbreviationstringsforyeardivisionsparsedfromiso8601-2ExtendedFormat
dates:
spring Thestring‘spring’
summer Thestring‘summer’
autumn Thestring‘autumn’
winter Thestring‘winter’
springN Thestring‘spring(NorthernHemisphere)’
summerN Thestring‘summer(NorthernHemisphere)’
autumnN Thestring‘autumn(NorthernHemisphere)’
296

winterN Thestring‘winter(NorthernHemisphere)’
springS Thestring‘spring(SouthernHemisphere)’
summerS Thestring‘summer(SouthernHemisphere)’
autumnS Thestring‘autumn(SouthernHemisphere)’
winterS Thestring‘winter(SouthernHemisphere)’
Q1 Thestring‘Quarter1’
Q2 Thestring‘Quarter2’
Q3 Thestring‘Quarter3’
Q4 Thestring‘Quarter3’
QD1 Thestring‘Quadrimester1’
QD2 Thestring‘Quadrimester2’
QD3 Thestring‘Quadrimester3’
S1 Thestring‘Semestral1’
S2 Thestring‘Semestral2’
AbbreviationstringsforAM/PM:
am Thestring‘AM’
pm Thestring‘PM’
4.10 FormattingCommands
This section corresponds to § 3.12 in the user part of this manual. Bibliography
andcitationstylesshouldincorporatethecommandsandfacilitiesdiscussedinthis
sectioninordertoprovideacertaindegreeofhigh-levelconfigurability. Usersshould
notbeforcedtowritenewstylesifalltheywanttodoismodifythespacinginthe
bibliographyorthepunctuationusedincitations.
4.10.1 User-definableCommandsandHooks
Thissectioncorrespondsto§3.12.1intheuserpartofthemanual. Thecommands
andhooksdiscussedherearemeanttoberedefinedbyusers,butbibliographyand
citationstylesmayprovideadefaultdefinitionwhichisdifferentfromthepackage
default. These commands are defined in biblatex.def. Note that all commands
startingwith\mk…takeonemandatoryargument.
\bibsetup Arbitrary code to be executed at the beginning of the bibliography, intended for
commandswhichaffectthelayoutofthebibliography.
\bibfont Arbitrary code setting the font used in the bibliography. This is very similar to
\bibsetupbutintendedforswitchingfonts.
\citesetup Arbitrarycodetobeexecutedatthebeginningofeachcitationcommand.
\newblockpunct Theseparatorinsertedbetween‘blocks’inthesenseexplainedin§4.7.1. Thedefault
definitioniscontrolledbythepackageoptionblock(see§3.1.2.1).
\newunitpunct Theseparatorinsertedbetween‘units’inthesenseexplainedin§4.7.1. Thiswill
usuallybeaperiodoracommaplusaninterwordspace. Thedefaultdefinitionisa
periodandaspace.
297

\finentrypunct Thepunctuationprintedattheveryendofeverybibliographyentry,usuallyaperiod.
Thedefaultdefinitionisaperiod.
\entrysetpunct Thepunctuationprintedbetweenbibliographysubentriesofanentryset. Thedefault
definitionisasemicolonandaspace.
\bibnamedelima Thisdelimitercontrolsthespacingbetweentheelementswhichmakeupanamepart.
Itisinsertedautomaticallybythebackendafterthefirstnameelementiftheelement
islessthanthreecharacterslongandbeforethelastelement. Thedefaultdefinition
is\addhighpenspace, i.e., aspacepenalizedbythevalueofthehighnamepenalty
counter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimb Thisdelimitercontrolsthespacingbetweentheelementswhichmakeupaname
part. Itisinsertedautomaticallybythebackendbetweenallnameelementswhere
\bibnamedelimadoesnotapply. Thedefaultdefinitionis\addlowpenspace,i.e.,a
spacepenalizedbythevalueofthelownamepenaltycounter(§3.12.4). Pleaserefer
to§3.15.4forfurtherdetails.
\bibnamedelimc Thisdelimitercontrolsthespacingbetweennameparts. Thedefaultnameformats
use it between the name prefix and the family name if useprefix=true. The de-
fault definition is \addhighpenspace, i.e., a space penalized by the value of the
highnamepenaltycounter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimd Thisdelimitercontrolsthespacingbetweennameparts. Thedefaultnameformatsuse
itbetweenallnamepartswhere\bibnamedelimcdoesnotapply. Thedefaultdefini-
tionis\addlowpenspace,i.e.,aspacepenalizedbythevalueofthelownamepenalty
counter(§3.12.4). Pleasereferto§3.15.4forfurtherdetails.
\bibnamedelimi Thisdelimiterreplaces\bibnamedelima/bafterinitials. Notethatthisonlyapplies
toinitialsgivenassuchinthebibfile,nottotheinitialsautomaticallygeneratedby
biblatexwhichusetheirownsetofdelimiters.
\bibinitperiod The punctuation inserted automatically by the backend after all initials unless
\bibinithyphendelimapplies. Thedefaultdefinitionisaperiod(\adddot). Please
referto§3.15.4forfurtherdetails.
\bibinitdelim Thespacinginsertedautomaticallybythebackendbetweenmultipleinitialsunless
\bibinithyphendelimapplies. Thedefaultdefinitionisanunbreakableinterword
space. Pleasereferto§3.15.4forfurtherdetails.
\bibinithyphendelim Thepunctuationinsertedautomaticallybythebackendbetweentheinitialsof
hyphenatednameparts,replacing\bibinitperiodand\bibinitdelim. Thedefault
definitionisaperiodfollowedbyanunbreakablehyphen. Pleasereferto§3.15.4for
furtherdetails.
\bibindexnamedelima Replaces\bibnamedelimaintheindex.
\bibindexnamedelimb Replaces\bibnamedelimbintheindex.
\bibindexnamedelimc Replaces\bibnamedelimcintheindex.
\bibindexnamedelimd Replaces\bibnamedelimdintheindex.
\bibindexnamedelimi Replaces\bibnamedelimiintheindex.
\bibindexinitperiod Replaces\bibinitperiodintheindex.
298

\bibindexinitdelim Replaces\bibinitdelimintheindex.
\bibindexinithyphendelim Replaces\bibinithyphendelimintheindex.
\revsdnamepunct The punctuation to be printed between the given and family name parts when a
nameisreversed. Thedefaultisacomma. Thiscommandshouldbeincorporatedin
formattingdirectivesfornamelists. Pleasereferto§3.15.4forfurtherdetails.
\bibnamedash Thedashtobeusedasareplacementforrecurrentauthorsoreditorsinthebiblio-
graphy. Thedefaultisan‘em’oran‘en’dash,dependingontheindentationofthe
listofreferences.
\labelnamepunct A separator to be printed after the name used for alphabetizing in the bibliogra- Deprecated
phy(authororeditor,iftheauthorfieldisundefined)insteadof\newunitpunct.
The default is \newunitpunct, i.e., it is not handled differently from regular unit
punctuationbutpermitsconvenientreconfiguration. Thispunctuationcommand
isdeprecatedandhasbeensupersededbythecontext-sensitive\nametitledelim
(see§3.12.2). Forbackwardscompatibilityreasons,however,\nametitledelimstill
defaults to \labelnamepunct in the bib and biblist contexts. Style authors may
want to consider replacing \labelnampunct with \printdelim{nametitledelim}
andusersmaywanttoprefermodifyingthecontext-sensitivenametitledelimwith
\DeclareDelimFormatoverredefining\labelnamepunct,e.g.,
\DeclareDelimFormat[bib]{nametitledelim}{%
\addcolon\space}
\subtitlepunct Theseparatortobeprintedbetweenthefieldstitleandsubtitle,booktitleand
booksubtitle,aswellasmaintitleandmainsubtitle. Usethisseparatorinsteadof
\newunitpunctatthislocation. Thedefaultis\newunitpunct,i.e.,itisnothandled
differentlyfromregularunitpunctuationbutpermitsconvenientreconfiguration.
\intitlepunct Theseparatortobeprintedbetweentheword“in”andthefollowingtitleinentry
typessuchas@article,@inbook,@incollection,etc. Usethisseparatorinsteadof
\newunitpunctatthislocation. Thedefaultdefinitionisacolonplusaninterword
space.
\bibpagespunct The separator to be printed before the pages field. Use this separator instead of
\newunitpunctatthislocation. Thedefaultisacommaplusaninterwordspace.
\bibpagerefpunct Theseparatortobeprintedbeforethepagereffield. Usethisseparatorinsteadof
\newunitpunctatthislocation. Thedefaultisaninterwordspace.
\bibeidpunct Theseparatorprintedbeforetheeidfield(similarto\bibpagespunct). Thedefault
isacommaplusaninterwordspace.
\multinamedelim The delimiter to be printed between multiple items in a name list like author or ContextSensitive
editoriftherearemorethantwonamesinthelist. Ifthereareonlytwonamesin
thelist, usethe \finalnamedeliminstead. Thiscommandshouldbeincorporated
inallformattingdirectivesfornamelists. Thedefaultisacommafollowedbyan
interwordspace.
\finalnamedelim Usethiscommandinsteadof\multinamedelimbeforethefinalnameinanamelist. ContextSensitive
Thedefaultisthelocalisedterm‘and’,separatedbyinterwordspaces.
299

\revsdnamedelim Theextradelimitertobeprintedafterthefirstnameinanamelistconsistingoftwo ContextSensitive
names(inadditionto\finalnamedelim)ifthefirstnameisreversed. Thiscommand
shouldbeincorporatedinallformattingdirectivesfornamelists.
\andothersdelim Thedelimitertobeprintedbeforethelocalisationstring‘andothers’ifanamelist ContextSensitive
like author or editor is truncated. This command should be incorporated in all
formattingdirectivesfornamelists. Thedefaultisaninterwordspace.
\multilistdelim Thedelimitertobeprintedbetweenmultipleitemsinaliterallistlikepublisheror ContextSensitive
locationiftherearemorethantwonamesinthelist. Ifthereareonlytwoitemsin
thelist,usethe\finallistdeliminstead. Thiscommandshouldbeincorporatedin
allformattingdirectivesforliterallists. Thedefaultisacommaplusaninterword
space.
\finallistdelim Usethiscommandinsteadof\multilistdelimbeforethefinaliteminaliterallist. ContextSensitive
Thedefaultisthelocalisedterm‘and’,separatedbyinterwordspaces.
\andmoredelim Thedelimitertobeprintedbeforethelocalisationstring‘andmore’ifaliterallistlike ContextSensitive
publisherorlocationistruncated. Thiscommandshouldbeincorporatedinall
formattingdirectivesforliterallists. Thedefaultisaninterwordspace.
\multicitedelim Thedelimiterprintedbetweencitationsifmultipleentrykeysarepassedtoasingleci-
tationcommand. Thiscommandshouldbeincorporatedinthedefinitionofallcitation
commands,forexampleinthehsepcodeiargumentpassedto\DeclareCiteCommand.
See§4.3.1fordetails. Thedefaultisasemicolonplusaninterwordspace.
\multiciterangedelim Thedelimiterprintedbetweentwocitationsiftheyarecompressedtoarange.
Thedefaultis\bibrangedash.
\multicitesubentrydelim Thedelimiterprintedbetweensubentrycitationsofthesameset. Thisde-
limiterisonlyusedincitationstylesthatreducecitationsofthesamesettoamore
compactform(subentryofnumeric-comp). Thedefaultisacomma.
\multicitesubentryrangedelim Thedelimiterprintedbetweentwocitationsofthesamesetiftheyare
compressedtoarange. Thedefaultis\multiciterangedelim.
\supercitedelim Similarto\multinamedelim,butintendedforthe\supercitecommandonly. The
defaultisacomma.
\superciterangedelim Analogue of \multiciterangedelim for \supercite. The default is
\bibrangedash.
\supercitesubentrydelim Analogue of \multicitesubentrydelim for \supercite. The default is
\supercitedelim.
\supercitesubentryrangedelim Analogueof\multicitesubentryrangedelimfor\supercite. Thede-
faultis\superciterangedelim.
\compcitedelim Similarto\multicitedelim,butintendedforcitationstylesthat‘compress’multiple
citations, i.e., print the author only once if subsequent citations share the same
authoretc. Thedefaultdefinitionisacommaplusaninterwordspace.
\textcitedelim Similar to \multicitedelim, but intended for \textcite and related commands
(§3.9.2). Thedefaultisacommaplusaninterwordspace. Thestandardstylesmodify
thisprovisionaldefinitiontoensurethatthedelimiterbeforethefinalcitationisthe
localisedterm‘and’,separatedbyinterwordspaces.
300

\nametitledelim Thedelimitertobeprintedbetweentheauthor/editorandthetitle. Thiscommand ContextSensitive
should be incorporated in the definition of all citation commands of author-title
and some verbose citation styles and in the bibliography drivers—in author-year
bibliographies \nametitledelim may be printed between the author/editor-year
blockandthetitle. Thedefaultdefinitioninsidebibliographies(i.e.,inthebiband
biblistcontexts)isthenowdeprecated\labelnamepunct(forbackwardscompati-
bilityreasons),intextcitecontextitisaspaceanditisacommaplusaninterword
spaceotherwise.
\nameyeardelim Thedelimitertobeprintedbetweentheauthor/editorandtheyear. Thiscommand ContextSensitive
should be incorporated in the definition of all citation commands of author-year
citationstylesandinthebibliographydrivers. Thedefaultdefinitionisaninterword
space. Forbackwardscompatibilityreasonsthereareseparatedefinitionsinthebib,
biblist,textciteandglobalcontext.
\namelabeldelim Thedelimiterprintedbetweenthename/titleandthelabel. Thiscommandshouldbe ContextSensitive
incorporatedinthedefinitionofallcitationcommandsofalphabeticandnumeric
citationstyles. Thedefaultdefinitionisaninterwordspace.
\nonameyeardelim The delimiter printed between the substitute for the labelname when it does not ContextSensitive
exist(usuallythelabelortitleinstandardstyles)andtheyearcitationstylesand
thebibliographydrivers. Thiscommandshouldbeincorporatedinthedefinitionof
allcitationcommandsofauthor-yearcitationstylesandinthebibliographydrivers.
Thedefaultdefinitionisaninterwordspace. Forbackwardscompatibilityreasons
thereareseparatedefinitionsinthebib,biblist,textciteandglobalcontext.
\authortypedelim The delimiter printed between the author and the authortype. The default is a ContextSensitive
commafollowedbyaspace.
\editortypedelim Thedelimiterprintedbetweentheeditorandtheeditororeditortypestring. The ContextSensitive
defaultisacommafollowedbyaspace.
\translatortypedelim The delimiter printed between the translator and the translator string. The ContextSensitive
defaultisacommafollowedbyaspace.
\labelalphaothers Astringtobeappendedtothenon-numericportionofthelabelalphafield(i.e.,
thefieldholdingthecitationlabelusedbyalphabeticcitationstyles)ifthenumber
ofauthors/editorsexceedsthemaxalphanamesthresholdortheauthor/editorlist
wastruncatedinthebibfilewiththekeyword‘and others’. Thiswilltypicallybea
singlecharactersuchasaplussignoranasterisk. Thedefaultisaplussign. This
commandmayalsoberedefinedtoanemptystringtodisablethisfeature. Inany
case,itmustberedefinedinthepreamble.
\sortalphaothers Similarto\labelalphaothersbutusedinthesortingprocess. Settingittoadifferent
valueisadvisableifthelattercontainsformattingcommands. If\sortalphaothers
isnotredefined,itdefaultsto\labelalphaothers.
\volcitedelim Thedelimitertobeprintedbetweenthevolumeportionandthepage/textportionof
\volciteandrelatedcommands(§3.9.6).
\prenotedelim Thedelimitertobeprintedafterthehprenoteiargumentofacitationcommand. The ContextSensitive
defaultisaninterwordspace.
\postnotedelim Thedelimitertobeprintedbeforethehpostnoteiargumentofacitationcommand. ContextSensitive
Thedefaultisacommaplusaninterwordspace.
301

\extpostnotedelim Thedelimiterprintedbetweenthecitationandtheparentheticalhpostnoteiargument ContextSensitive
ofacitationcommandwhenthepostnoteoccursoutsideofthecitationparentheses.
Inthestandardstyles,thisoccurswhenthecitationusestheshorthandfieldofthe
entry. Thedefaultisaninterwordspace.
\multiprenotedelim Thedelimitertobeprintedafterthehmultiprenoteiargumentofacitationcommand. ContextSensitive
\multipostnotedelim The delimiter to be printed before the hmultipostnotei argument of a citation ContextSensitive
command.
\mkbibname‘namepart’{htexti}Formattinghookforthenamepart‘namepart’,tobeusedinallformatting
directives for name lists. The default datamodel defines the name parts ‘family’,
‘given’, ‘prefix’ and ‘suffix’ and therefore the following macros are automatically
defined:
\mkbibnamefamily
\mkbibnamegiven
\mkbibnameprefix
\mkbibnamesuffix
\mkbibcompletename‘formatorder’{htexti}Formattinghookforthecompletenameinformatorder‘for-
matorder’. Thedefaultstylesusethenameformatorders‘family’,‘family-given’and
‘given-family’,thereforethefollowingmacrosareautomaticallydefined:
\mkbibcompletenamefamily
\mkbibcompletenamefamilygiven
\mkbibcompletenamegivenfamily
Theseformattinghooksshouldenclosethecompletenameinthebibliographymacro
\name:‘formatorder’. Initiallyallhooksexpandto\mkbibcompletename.
\mkbibcompletename{htexti}The initial value of all default formatting hooks
\mkbibcompletename‘formatorder’.
\datecircadelim When formatting dates with the global option datecirca enabled, the delimiter ContextSensitive
printedafteranylocalised‘circa’term. Defaultstointerwordspace.
\dateeradelim When formatting dates with the global option dateera set, the delimiter printed ContextSensitive
beforethelocalisationeraterm. Defaultstointerwordspace.
\dateuncertainprint Prints date uncertainty information when the global option dateuncertain is
enabled and the \ifdateuncertain test is true. By default, prints the language
specific\bibdateuncertainstring(§3.12.3).
\enddateuncertainprint Printsdateuncertaintyinformationwhentheglobaloptiondateuncertainis
enabledandthe\ifenddateuncertaintestistrue. Bydefault,printsthelanguage
specific\bibdateuncertainstring(§3.12.3).
\datecircaprint Printsdatecircainformationwhentheglobaloptiondatecircaisenabledandthe
\ifdatecircatestistrue. Bydefault,printsthe‘circa’localisedterm(§4.9.2.21)and
thedatecircadelimdelimiter.
302

\enddatecircaprint Printsdatecircainformationwhentheglobaloptiondatecircaisenabledandthe
\ifenddatecircatestistrue. Bydefault,printsthe‘circa’localisedterm(§4.9.2.21)
andthedatecircadelimdelimiter.
\datecircaprintiso Printsiso8601-2formatdatecircainformationwhentheglobaloptiondatecirca
isenabledandthe\ifdatecircatestistrue. Prints\textasciitilde.
\enddatecircaprintiso Prints iso8601-2 format date circa information when the global option
datecircaisenabledandthe\ifenddatecircatestistrue. Prints\textasciitilde.
\dateeraprint yearfieldPrintsdateerainformationwhentheglobaloptiondateeraissetto‘secular’
or ‘christian’. By default, prints the dateeradelim delimiter and the appropriate
localised era term (§ 4.9.2.21). If the dateeraauto option is set, then the passed
hyearfieldi(whichisthenameofayearfieldsuchas‘year’,‘origyear’,‘endeventyear’
etc.) istestedtoseeifitsvalueisearlierthanthedateeraautothresholdandifso,
thentheBCE/CElocalisationwillbeoutputtoo. Thedefaultsettingfordateeraauto
is 0 and so only BCE/BC localisation strings are candidates for output. Detects
whether the start or end year era information is to be printed by looking at the
hyearfieldinamepassedtoit.
\dateeraprintpre Printsdateerainformationwhentheglobaloptiondateeraissetto‘astronomical’.
By default, prints bibdataeraprefix. Detects whether the start or end year era
informationistobeprintedbylookingatthehyearfieldinamepassedtoit.
\relatedpunct Theseparatorbetweentherelatedtypebibliographylocalisationstringandthedata
fromthefirstrelatedentry.
\relateddelim The generic separator between the data of multiple related entries. The default
definitionisanoptionaldotpluslinebreak.
\relateddelim<relatedtype> Theseparatorbetweenthedataofmultiplerelatedentriesinsiderelated
entries of type ‘relatedtype’. There is no default, if such a type-specific delimiter
doesnotexist,\relateddelimisused.
\begrelateddelim Thegenericseparatorbeforetheblockofrelatedentries. Thedefaultdefinitionis
\newunitpunct.
\begrelateddelim<relatedtype> The separator between the block of related entries of type ‘re-
latedtype’. There is no default, if such a type-specific delimiter does not exist,
\relateddelimisused.
4.10.2 Language-specificCommands
Thissectioncorrespondsto§3.12.3intheuserpartofthemanual. Thecommands
discussed here are usually handled by the localisation modules, but may also be
redefinedbyusersonaper-languagebasis. Notethatallcommandsstartingwith
\mk…takeoneormoremandatoryarguments.
\bibrangedash The language specific dash to be used for ranges of numbers. Defaults to
\textendash.
\bibrangessep Thelanguagespecificseparatortobeusedbetweenmultipleranges. Defaultstoa
commafollowedbyaspace.
\bibdatesep Thelanguagespecificseparatorusedbetweendatecomponentsintersedateformats.
Defaultsto\hyphen.
303

\bibdaterangesep Thelanguagespecificseparatortobeusedfordateranges. Defaultsto\textendash
for all date formats apart from ymd which defaults to a \slash. The date format
optionisoishard-codedto\slashsincethisisastandardscompliantformat.
\mkbibdatelong Takesthenamesofthreefieldasargumentswhichcorrespondtothreedatecompo-
nents(intheorderyear/month/day)andusestheirvaluestoprintthedateinthe
languagespecificlongdateformat.
\mkbibdateshort Similarto\mkbibdatelongbutusingthelanguagespecificshortdateformat.
\mkbibtimezone Modifiesatimezonestringpassedinastheonlyargument. Bydefaultthischanges
‘Z’tothevalueof\bibtimezone.
\bibdateuncertain Thelanguagespecificmarkertobeusedafteruncertaindateswhentheglobaloption
dateuncertainisenabled. Defaultstoaspacefollowedbyaquestionmark.
\bibdateeraprefix The language specific marker which is printed as a prefix to beginning BCE/BC
datesinadaterangewhentheoptiondateeraissetto‘astronomical’. Defaultsto
\textminus,ifdefinedand\textendashotherwise.
\bibdateeraendprefix ThelanguagespecificmarkerwhichisprintedasaprefixtoendBCE/BCdates
inadaterangewhentheoptiondateeraissetto‘astronomical’. Defaultstoathin
spacefollowedby\bibdateeraprefixwhen\bibdaterangesepissettoadashand
to\bibdateeraprefixotherwise. Thisisaseparatemacrosothatyoumayaddextra
spacebeforeanegativedatemarkerwhich,forexamplefollowsadashdaterange
markerasthiscanlookalittleodd.
\bibtimesep Thelanguagespecificmarkerwhichseparatestimecomponents. Defaulttoacolon.
\bibutctimezone ThelanguagespecificstringprintedfortheUTCtimezone. Defaultsto‘Z’.
\bibtimezonesep The language specific marker which separates an optional time zone component
fromatime. Emptybydefault.
\bibtzminsep Thelanguagespecificmarkerwhichseparateshourandminutecomponentofoffset
timezones. Defaultstoa\bibtimesep.
\bibdatetimesep The language specific separator printed between date and time compo-
nents when printing time components along with date components (see the
<datetype>dateusetimeoptionin§3.1.2.1). Defaultstoaspacefornon-iso8601-2
outputformats,and’T’foriso8601-2outputformat.
\finalandcomma Printsthecommatobeinsertedbeforethefinal‘and’inanenumeration,ifapplicable
intherespectivelanguage.
\finalandsemicolon Prints the semicolon to be inserted before the final ‘and’ in an enumeration, if
applicableintherespectivelanguage.
\mkbibordinal{hintegeri}
Takesanintegerargumentandprintsitasanordinalnumber.
\mkbibmascord{hintegeri}
Similarto\mkbibordinal,butprintsamasculineordinal,ifapplicableintherespec-
tivelanguage.
304

\mkbibfemord{hintegeri}
Similarto\mkbibordinal,butprintsafeminineordinal,ifapplicableintherespective
language.
\mkbibneutord{hintegeri}
Similarto\mkbibordinal,butprintsaneuterordinal,ifapplicableintherespective
language.
\mkbibordedition{hintegeri}
Similarto\mkbibordinal,butintendedforusewiththeterm‘edition’.
\mkbibordseries{hintegeri}
Similarto\mkbibordinal,butintendedforusewiththeterm‘series’.
4.10.3 User-definableLengthsandCounters
This section corresponds to § 3.12.4 in the user part of the manual. The length
registersandcountersdiscussedherearemeanttobealteredbyusers. Bibliography
andcitationstylesshouldincorporatethemwhereapplicableandmayalsoprovide
adefaultsettingwhichisdifferentfromthepackagedefault.
\bibhang Thehangingindentationofthebibliography,ifapplicable. Thislengthisinitialized
to\parindentatload-time. If\parindentiszerolengthforsomereason,\bibhang
willdefaultto1em.
\biblabelsep The horizontal space between entries and their corresponding labels. Bibliogra-
phy styles which use list environments and print a label should set \labelsep
to \biblabelsep in the definition of the respective environment. This length is
initializedtotwicethevalueof\labelsepatload-time.
\bibitemsep Theverticalspacebetweentheindividualentriesinthebibliography. Bibliography
stylesusinglistenvironmentsshouldset\itemsepto\bibitemsepinthedefinition
oftherespectiveenvironment. Thislengthisinitializedto\itemsepatload-time.
\bibnamesep Verticalspacetobeinsertedbetweentwoentriesinthebibliographywheneveran
entry starts with a name which is different from the initial name of the previous
entry. The default value is zero. Setting this length to a positive value greater
than \bibitemsep will group the bibliography by author/editor name. Note that
\bibitemsep,\bibnamesep,and\bibinitsepobeytherulesfor\addvspace,thatis,
whenverticalspaceintroducedbyanyofthesecommandsimmediatelyfollowson
fromspaceintroducedbyanotherofthem,theresultingtotalspaceisequaltothe
largestofthem.
\bibinitsep Verticalspacetobeinsertedbetweentwoentriesinthebibliographywheneveran
entry starts with a letter which is different from the initial letter of the previous
entry. Thedefaultvalueiszero. Settingthislengthtoapositivevaluegreaterthan
\bibitemsep will group the bibliography alphabetically. Note that \bibitemsep,
\bibnamesep,and\bibinitsepobeytherulesfor\addvspace,thatis,whenvertical
space introduced by any of these commands immediately follows on from space
introduced by another of them, the resulting total space is equal to the largest of
them.
305

\bibparsep The vertical space between paragraphs within an entry in the bibliography. Bib-
liographystylesusinglistenvironmentsshouldset\parsepto\bibparsepinthe
definitionoftherespectiveenvironment. Thedefaultvalueiszero.
abbrvpenalty The penalty used by \addabbrvspace, \addabthinspace, and \adddotspace, see
§4.7.4fordetails. Thiscounterisinitializedto\hyphenpenaltyatload-time.
highnamepenalty Thepenaltyusedby\addhighpenspaceand\addhpthinspace,see§4.7.4fordetails.
Thecounterisinitializedto\hyphenpenaltyatload-time.
lownamepenalty Thepenaltyusedby\addlowpenspaceand\addlpthinspace,see§4.7.4fordetails.
Thecounterisinitializedtohalfthe\hyphenpenaltyatload-time.
biburlbigbreakpenalty Thebiblatexversionofurl’s\UrlBigBreakPenalty. Thedefaultvalueis100.
biburlbreakpenalty Thebiblatexversionofurl’s\UrlBreakPenalty. Thedefaultvalueis200.
biburlnumpenalty Ifthiscounterissettoavaluegreaterthanzero,biblatexwillpermitlinebreaks
afternumbersinallstringsformattedwiththe\urlcommandfromtheurlpackage.
Thiswillaffecturlsanddoisinthebibliography. Thebreakpointswillbepenalized
by the value of this counter. If urls and/or dois in the bibliography run into the
margin,trysettingthiscountertoavaluegreaterthanzerobutlessthan10000(you
normallywanttouseahighvaluelike9000). Settingthecountertozerodisables
thisfeature. Thisisthedefaultsetting.
biburlucpenalty Similartobiburlnumpenalty,exceptthatitwilladdabreakpointafteralluppercase
letters.
biburllcpenalty Similartobiburlnumpenalty,exceptthatitwilladdabreakpointafteralllowercase
letters.
\biburlbigskip Thebiblatexversionof\Urlmuskip. Thislengthholdstheadditional(stretchable)
space inserted around breakable characters in the \url command from the url
package. Thedefaultvalueis0mu plus 3mu.
\biburlnumskip The additional space inserted after numbers in strings formatted with the \url
commandfromtheurlpackage. Thiswillaffecturlsanddoisinthebibliography.
Ifurlsand/ordoisinthebibliographyrunintothemargin,itmayhelptosetthis
lengthtoaddsomesmallstretchablespace,forexample0mu plus 1mu. Thedefault
settingis0mu. Thisvalueisonlyusedifbiburlnumpenaltyissettoavaluedifferent
fromzero.
\biburlucskip Similartobiburlnumskip,exceptthatitwilladdspaceafteralluppercaseletters.
\biburllcskip Similartobiburlnumskip,exceptthatitwilladdspaceafteralluppercaseletters.
4.10.4 AuxiliaryCommandsandHooks
Theauxiliarycommandsandfacilitiesinthissectionserveaspecialpurpose. Some
ofthemareusedbybiblatextocommunicatewithbibliographyandcitationstyles
insomewayorother.
\mkbibemph{htexti}
A generic command which prints its argument as emphasized text. This is a
simple wrapper around the standard \emph command. Apart from that, it uses
306

\setpunctfontfrom§4.7.1toadaptthefontofthenextpunctuationmarkfollowing
the text set in italics. If the punctfont package option is disabled, this command
behaveslike\emph.
\mkbibitalic{htexti}
Similarinconceptto\mkbibemphbutprintsitalicizedtext. Thisisasimplewrapper
aroundthestandard\textitcommandwhichincorporates\setpunctfont. Ifthe
punctfontpackageoptionisdisabled,thiscommandbehaveslike\textit.
\mkbibbold{htexti}
Similar in concept to \mkbibemph but prints bold text. This is a simple wrapper
aroundthestandard\textbfcommandwhichincorporates\setpunctfont. Ifthe
punctfontpackageoptionisdisabled,thiscommandbehaveslike\textbf.
\mkbibquote{htexti}
Agenericcommandwhichwrapsitsargumentinquotationmarks. Ifthecsquotes
packageisloaded,thiscommandusesthelanguagesensitivequotationmarkspro-
videdbythatpackage. \mkbibquotealsosupports‘American-style’punctuation,see
\DeclareQuotePunctuationin§4.7.5fordetails.
\mkbibparens{htexti}
A generic command which wraps its argument in parentheses. This command is
nestable. Whennested,itwillalternatebetweenparenthesesandbrackets,depending
onthenestinglevel.
\mkbibbrackets{htexti}
Agenericcommandwhichwrapsitsargumentinsquarebrackets. Thiscommandis
nestable. Whennested,itwillalternatebetweenbracketsandparentheses,depending
onthenestinglevel.
\bibopenparenhtexti\bibcloseparen
Alternativesyntaxfor\mkbibparens. Thiswillalsoworkacrossgroups. Notethat
\bibopenparenand\bibcloseparenmustalwaysbebalanced.
\bibopenbrackethtexti\bibclosebracket
Alternativesyntaxfor\mkbibbrackets. Thiswillalsoworkacrossgroups. Notethat
\bibopenbracketand\bibclosebracketmustalwaysbebalanced.
\mkbibfootnote{htexti}
Agenericcommandwhichprintsitsargumentasafootnote. Thisisawrapperaround
thestandardLaTeX\footnotecommandwhichremovesspuriouswhitespacepre-
cedingthefootnotemarkandpreventsnestedfootnotes. Bydefault,\mkbibfootnote
requestscapitalizationatthebeginningofthenoteandautomaticallyaddsaperiod
attheend. Youmaychangethisbehaviorbyredefiningthe\bibfootnotewrapper
macrointroducedbelow.
\mkbibfootnotetext{htexti}
Similarto\mkbibfootnotebutusesthe\footnotetextcommand.
307

\mkbibendnote{htexti}
Similarinconceptto\mkbibfootnoteexceptthatitprintsitsargumentasanend-
note. \mkbibendnoteremovesspuriouswhitespaceprecedingtheendnotemarkand
preventsnestednotes. Itsupportsthe\endnotecommandprovidedbytheendnotes
packageaswellasthe\pagenotecommandprovidedbythepagenotepackageand
the memoir class. If both commands are available, \endnote takes precedence. If
no endnote support is available, \mkbibendnote issues an error and falls back to
\footnote. Bydefault, \mkbibendnoterequestscapitalizationatthebeginningof
thenoteandautomaticallyaddsaperiodattheend. Youmaychangethisbehavior
byredefiningthe\bibendnotewrappermacrointroducedbelow.
\mkbibendnotetext{htexti}
Similar to \mkbibendnote but uses the \endnotetext command. Please note that
as of this writing, neither the pagenote package nor the memoir class provide a
corresponding\pagenotetextcommand. Inthiscase,\mkbibendnotewillissuean
errorandfallbackto\footnotetext.
\bibfootnotewrapper{htexti}
An inner wrapper which encloses the htexti argument of \mkbibfootnote and
\mkbibfootnotetext. Forexample,\mkbibfootnoteeventuallyboilsdowntothis:
\footnote{\bibfootnotewrapper{text}}
Thewrapperensurescapitalizationatthebeginningofthenoteandaddsaperiodat
theend. Thedefaultdefinitionis:
\newcommand{\bibfootnotewrapper}[1]{\bibsentence #1\addperiod}
Ifyoudon’twantcapitalizationatthebeginningoraperiodattheendofthenote,
donotmodify\mkbibfootnotebutredefine\bibfootnotewrapperinstead.
\bibendnotewrapper{htexti}
Similarinconceptto\bibfootnotewrapperbutrelatedtothe\mkbibendnoteand
\mkbibendnotetextcommands.
\mkbibsuperscript{htexti}
Agenericcommandwhichprintsitsargumentassuperscriptedtext. Thisisasimple
wrapperaroundthestandardLaTeX\textsuperscriptcommandwhichremoves
spuriouswhitespaceandallowshyphenationoftheprecedingword.
\mkbibmonth{hintegeri}
This command takes an integer argument and prints it as a month name. Even
thoughtheoutputofthiscommandislanguagespecific,itsdefinitionisnot,henceit
isnormallynotredefinedinlocalisationmodules.
\mkbibyeardivision{hstringi}
Deprecated
Thiscommandtakesayeardivisionlocalisationstringandprintstheversionofthe
stringcorrespondingtothesettingofthedateabbrevpackageoption. Eventhough
the output of this command is language specific, its definition is not, hence it is
normallynotredefinedinlocalisationmodules.
308

\mkbibseason{hstringi}
Deprecated
Thiscommandtakesaseasonlocalisationstringandprintstheversionofthestring
correspondingtothesettingofthedateabbrevpackageoption. Eventhoughthe
outputofthiscommandislanguagespecific,itsdefinitionisnot,henceitisnormally
notredefinedinlocalisationmodules.
\mkyearzeros{hintegeri}
Thiscommandstripsleadingzerosfromayearorenforcesthem,dependingonthe
datezerospackageoption(§3.1.2.1). Itisintendedforuseinthedefinitionofdate
formattingmacros. Ifzerosareenforced,thiscommandcalls\forcezerosyandthus
expandsitsargumentwith\protected@edef.
\mkmonthzeros{hintegeri}
Thiscommandstripsleadingzerosfromamonthorenforcesthem,dependingon
thedatezerospackageoption(§3.1.2.1). Itisintendedforuseinthedefinitionof
dateformattingmacros. Ifzerosareenforced,thiscommandcalls\forcezerosmdt
andthusexpandsitsargumentwith\protected@edef.
\mkdayzeros{hintegeri}
Thiscommandstripsleadingzerosfromadayorenforcesthem,dependingonthe
datezerospackageoption(§3.1.2.1). Itisintendedforuseinthedefinitionofdate
formattingmacros. Ifzerosareenforced,thiscommandcalls\forcezerosmdtand
thusexpandsitsargumentwith\protected@edef.
\mktimezeros{hintegeri}
Thiscommandstripsleadingzerosfromanumberorpreservesthem,dependingon
thetimezerospackageoption(§3.1.2.1). Itisintendedforuseinthedefinitionof
timeformattingmacros. Ifzerosareenforced,thiscommandcalls\forcezerosmdt
andthusexpandsitsargumentwith\protected@edef.
\forcezerosy{hintegeri}
This command adds zeros to a year (or any number supposed to be 4-digits). It
is intended for date formatting and ordinals. The argument is expanded with
\protected@edefbeforeitisprocessed.
\forcezerosmdt{hintegeri}
Thiscommandaddszerostoamonth,dayortimepart(oranynumbersupposedto
be2-digits). Itisintendedfordate/timeformattingandordinals. Theargumentis
expandedwith\protected@edefbeforeitisprocessed.
\stripzeros{hintegeri}
Thiscommandstripsleadingzerosfromanumber. Itisintendedfordateformatting
andordinals.
<labelfield>width Foreveryfieldmarkedasa‘Labelfield’inthedatamodel,aformattingdirectiveis
createdaspershorthandwidthabove. Sinceshorthandissomarkedinthedefault
datamodel,thisfunctionalityisasupersetofthatdescribedforshorthandwidth.
309

labelnumberwidth Similar to shorthandwidth, but referring to the labelnumber field and the length
register\labelnumberwidth. Numericstylesshouldadjustthisdirectivesuchthatit
correspondstotheformatusedinthebibliography.
labelalphawidth Similar to shorthandwidth, but referring to the labelalpha field and the length
register\labelalphawidth. Alphabeticstylesshouldadjustthisdirectivesuchthat
itcorrespondstotheformatusedinthebibliography.
bibhyperref A special formatting directive for use with \printfield and \printtext. This
directivewrapsitsargumentina\bibhyperrefcommand,see§4.6.4fordetails.
bibhyperlink Aspecialformattingdirectiveforusewith\printfieldand\printtext. Itwrapsits
argumentina\bibhyperlinkcommand,see§4.6.4fordetails. Thehnameiargument
passedto\bibhyperlinkisthevalueoftheentrykeyfield.
bibhypertarget Aspecialformattingdirectiveforusewith\printfieldand\printtext. Itwraps
its argument in a \bibhypertarget command, see § 4.6.4 for details. The hnamei
argumentpassedto\bibhypertargetisthevalueoftheentrykeyfield.
volcitepages Aspecialformattingdirectivewhichcontrolstheformatofthepage/textportionin
theargumentofcitationcommandslike\volcite.
volcitevolume Aspecialformattingdirectivewhichcontrolstheformatofthevolumeportionin
theargumentofcitationcommandslike\volcite.
date A special formatting directive which controls the format of \printdate (§ 4.4.1).
Notethatthedateformat(long/shortetc.) iscontrolledbythepackageoptiondate
from§3.1.2.1. Thisformattingdirectiveonlycontrolsadditionalformattingsuchas
fontsetc.
labeldate Asdatebutcontrolstheformatof\printlabeldate.
<datetype>date Asdatebutcontrolstheformatof\print<datetype>date.
time A special formatting directive which controls the format of \printtime (§ 4.4.1).
Notethatthetimeformat(24h/12hetc.) iscontrolledbythepackageoptiontime
from§3.1.2.1. Thisformattingdirectiveonlycontrolsadditionalformattingsuchas
fontsetc.
labeltime Astimebutcontrolstheformatof\printlabeltime.
<datetype>time Astimebutcontrolstheformatof\print<datetype>time.
4.10.5 AuxiliaryLengths,Counters,andOtherFeatures
The length registers and counters discussed here are used by biblatex to pass
informationtobibliographyandcitationstyles. Thinkofthemasread-onlyregisters.
Note that all counters are LaTeX counters. Use \value{counter} to read out the
currentvalue.
\<labelfield>width For every field marked as a ‘label’ field in the data model, a length register is
createdaspershorthandwidthabove. Sinceshorthandissomarkedinthedefault
datamodel,thisfunctionalityisasupersetofthatdescribedforshorthandwidth.
\labelnumberwidth Thislengthregisterindicatesthewidthofthewidestlabelnumber. Numericbib-
liographystylesshouldincorporatethislengthinthedefinitionofthebibliography
environment.
310

\labelalphawidth Thislengthregisterindicatesthewidthofthewidestlabelalpha. Alphabeticbib-
liographystylesshouldincorporatethislengthinthedefinitionofthebibliography
environment.
maxextraalpha Thiscounterholdsthehighestnumberfoundinanyextraalphafield.
maxextradate Thiscounterholdsthehighestnumberfoundinanyextradatefield.
maxextraname Thiscounterholdsthehighestnumberfoundinanyextranamefield.
maxextratitle Thiscounterholdsthehighestnumberfoundinanyextratitlefield.
maxextratitleyear Thiscounterholdsthehighestnumberfoundinanyextratitleyearfield.
refsection This counter indicates the current refsection environment. When queried in a
bibliographyheading,thecounterreturnsthevalueoftherefsectionoptionpassed
to\printbibliography.
refsegment This counter indicates the current refsegment environment. When queried in a
bibliographyheading,thiscounterreturnsthevalueoftherefsegmentoptionpassed
to\printbibliography.
maxnames Thiscounterholdsthesettingofthemaxnamespackageoption.
minnames Thiscounterholdsthesettingoftheminnamespackageoption.
maxitems Thiscounterholdsthesettingofthemaxitemspackageoption.
minitems Thiscounterholdsthesettingoftheminitemspackageoption.
instcount This counter is incremented by biblatex for every citation as well as for every
entryinthebibliographyandbibliographylists. Thevalueofthiscounteruniquely
identifiesasingleinstanceofareferenceinthedocument.
citetotal Thiscounter,whichisonlyavailableinthehloopcodeiofacitationcommanddefined
with\DeclareCiteCommand,holdsthetotalnumberofvalidentrykeyspassedtothe
citationcommand.
citecount Thiscounter,whichisonlyavailableinthehloopcodeiofacitationcommanddefined
with \DeclareCiteCommand, holds the number of the entry key currently being
processedbythehloopcodei.
multicitetotal Thiscounterissimilartocitetotalbutonlyavailableinmulticitecommands. It
holds the total number of citations passed to the multicite command. Note that
eachofthesecitationsmayconsistofmorethanoneentrykey. Thisinformationis
providedbythecitetotalcounter.
multicitecount Thiscounterissimilartocitecountbutonlyavailableinmulticitecommands. It
holds the number of the citation currently being processed. Note that this cita-
tionmayconsistofmorethanoneentrykey. Thisinformationisprovidedbythe
citetotalandcitecountcounters.
311

listtotal Thiscounterholdsthetotalnumberofitemsinthecurrentlist. Itisintendedfor
useinlistformattingdirectivesanddoesnotholdameaningfulvaluewhenused
anywhereelse. Asanexception,itmayalsobeusedinthesecondoptionalargument
to\printnamesand\printlist,see§4.4.1fordetails. Foreverylist,thereisalsoa
counterbythesamenamewhichholdsthetotalnumberofitemsinthecorresponding
list. Forexample,theauthorcounterholdsthetotalnumberofitemsintheauthor
list. This applies to both name lists and literal lists. These counters are similar
to listtotal except that they may also be used independently of list formatting
directives. For example, a bibliography style might check the editor counter to
decideWhetherornottoprinttheterm“editor”orratheritspluralform“editors”
afterthelistofeditors.
listcount This counter holds the number of the list item currently being processed. It is
intendedforuseinlistformattingdirectivesanddoesnotholdameaningfulvalue
whenusedanywhereelse.
liststart Thiscounterholdsthehstartiargumentpassedto\printnamesor\printlist. Itis
intendedforuseinlistformattingdirectivesanddoesnotholdameaningfulvalue
whenusedanywhereelse.
liststop Thiscounterholdsthehstopiargumentpassedto\printnamesor\printlist. Itis
intendedforuseinlistformattingdirectivesanddoesnotholdameaningfulvalue
whenusedanywhereelse.
\currentlang The name of the currently active language for biblatex. Can be used anywhere
anddefaultstothemaindocumentlanguage. Thisisautomaticallyswitchedinside
entrieswhichdefinelangid,givensuitablesettingsoftheautolangandlanguage
options. Note that this does not track all document language changes, only the
currentbiblatexsetting.
\currentfield Thenameofthefieldcurrentlybeingprocessedby\printfield. Thisinformation
isonlyavailablelocallyinfieldformattingdirectives.
\currentlist Thenameoftheliterallistcurrentlybeingprocessedby\printlist. Thisinformation
isonlyavailablelocallyinlistformattingdirectives.
\currentname Thenameofthenamelistcurrentlybeingprocessedby\printnames. Thisinforma-
tionisonlyavailablelocallyinnameformattingdirectives.
4.10.6 GeneralPurposeHooks
\AtBeginRefsection{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofeveryreference
section. Thehcodeiisexecutedjustaftersettingthereferencesectionnumber. This
commandmayonlybeusedinthepreamble.
\AtNextRefsection{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofthenextrefer-
encesection. Thehcodeiisexecutedjustaftersettingthereferencesectionnumber.
\AtFollowingRefsections{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofallreferencesec-
tionsfollowingthiscommand. Thehcodeiisexecutedjustaftersettingthereference
sectionnumberandjustbeforeanycodeexecutedvia\AtNextRefsection.
312

\AtBeginBibliography{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofthebibliography.
Thehcodeiisexecutedatthebeginningofthelistofreferences,immediatelyafter
the hbegincodei of \defbibenvironment. This command may only be used in the
preamble.
\AtBeginShorthands{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofthelistofshort-
hands. Thehcodeiisexecutedatthebeginningofthelistofshorthands,immediately
afterthehbegincodeiof\defbibenvironment. Thiscommandmayonlybeusedin
thepreamble.
Thisisjustanaliasfor:
\AtBeginBiblist{shorthand}{code}
\AtBeginBiblist{hbiblistnamei}{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofthebibliography
listhbiblistnamei. Thehcodeiisexecutedatthebeginningofthebibliographylist,
immediatelyafterthehbegincodeiof\defbibenvironment. Thiscommandmayonly
beusedinthepreamble.
\AtEveryBibitem{hcodei}
Appends the hcodei to an internal hook executed at the beginning of every item
in the bibliography. The hcodei is executed immediately after the hitemcodei of
\defbibenvironment. Thebibliographicdataoftherespectiveentryisavailableat
thispoint. Thiscommandmayonlybeusedinthepreamble.
\AtEveryLositem{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofeveryitemin
thelistofshorthands. Thehcodeiisexecutedimmediatelyafterthehitemcodeiof
\defbibenvironment. Thebibliographicdataoftherespectiveentryisavailableat
thispoint. Thiscommandmayonlybeusedinthepreamble.
Thisisjustanaliasfor:
\AtEveryBiblistitem{shorthand}{code}
\AtEveryBiblistitem{hbiblistnamei}{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofeveryitemin
thebibliographylistnamedhbiblistnamei. Thehcodeiisexecutedimmediatelyafter
the hitemcodei of \defbibenvironment. The bibliographic data of the respective
entryisavailableatthispoint. Thiscommandmayonlybeusedinthepreamble.
\AtNextBibliography{hcodei}
Similarto\AtBeginBibliographybutonlyaffectingthenext\printbibliography.
Theinternalhookisclearedafterbeingexecutedonce. Thiscommandmaybeused
inthedocumentbody.
313

\AtUsedriver{hcodei}
\AtUsedriver*{hcodei}
Appendsthehcodeitoaninternalhookexecutedwheninitializing\usedriver. The
starredvariantofthecommandclearstheinitialisationhook,sothedefaultscanbe
overwritten. Thiscommandmayonlybeusedinthepreamble. Thedefaultsettingis:
\AtUsedriver{%
\delimcontext{bib}%
\let\finentry\blx@finentry@usedrv
\let\newblock\relax
\let\abx@macro@bibindex\@empty
\let\abx@macro@pageref\@empty}
\AtEveryCite{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofeverycitation
command. Thehcodeiisexecutedimmediatelybeforethehprecodeiofthecommand
(see§4.3.1). Nobibliographicdataisavailableatthispoint. Thiscommandmayonly
beusedinthepreamble.
\AtEveryCitekey{hcodei}
Appendsthehcodeitoaninternalhookexecutedonceforeveryentrykeypassed
toacitationcommand. Thehcodeiisexecutedimmediatelybeforethehloopcodeiof
thecommand(see§4.3.1). Thebibliographicdataoftherespectiveentryisavailable
atthispoint. Thiscommandmayonlybeusedinthepreamble.
\AtEveryMultiCite{hcodei}
Appendsthehcodeitoaninternalhookexecutedatthebeginningofeverymulticite
command. Thehcodeiisexecutedimmediatelybeforethemultiprenotefield(§4.3.2)
isprinted. Nobibliographicdataisavailableatthispoint. Thiscommandmayonly
beusedinthepreamble.
\AtNextCite{hcodei}
Similarto\AtEveryCitebutonlyaffectingthenextcitationcommand. Theinter-
nalhookiscleared afterbeingexecuted once. Thiscommand maybeused inthe
documentbody.
\AtEachCitekey{hcodei}
Similarto\AtEveryCitekeybutonlyaffectingthecurrentcitationcommand. This
commandmaybeusedinthedocumentbody. Thehcodeiisappendedtotheinternal
hooklocallywhenlocatedinacitation,asdeterminedby\ifcitation.
\AtNextCitekey{hcodei}
Similarto\AtEveryCitekeybutonlyaffectingthenextentrykey. Theinternalhook
isclearedafterbeingexecutedonce. Thiscommandmaybeusedinthedocument
body.
314

\AtNextMultiCite{hcodei}
Similarto\AtEveryMultiCitebutonlyaffectingthenextmulticitecommand. The
internalhookisclearedafterbeingexecutedonce. Thiscommandmaybeusedin
thedocumentbody.
\AtVolcite{hcodei}
\AtVolcite*{hcodei}
Appendsthehcodeitoaninternalhookexecutedwheninitializing\volcite. The
starredvariantofthecommandclearstheinitialisationhook,sothedefaultscanbe
overwritten. Thiscommandmayonlybeusedinthepreamble. Thedefaultsettingis:
\AtVolcite{%
\DeclareFieldAlias{postnote}{volcitenote}}
\AtDataInput[hentrytypei]{hcodei}
Appendsthehcodeitoaninternalhookexecutedonceforeveryentryasthebibli-
ographic data is imported from the bbl file. The hentrytypei is the entry type the
hcodeiappliesto. Ifitappliestoallentrytypes, omittheoptionalargument. The
hcodeiisexecutedimmediatelyaftertheentryhasbeenimported. Thiscommand
mayonlybeusedinthepreamble. Notethathcodeimaybeexecutedmultipletimes
foranentry. Thisoccurswhenthesameentryiscitedindifferentrefsectionenvi-
ronmentsorthesortingoptionsettingsincorporatemorethanonesortingtemplate.
Therefsectioncounterholdsthenumberoftherespectivereferencesectionwhile
thedataisimported.
\UseBibitemHook
Executestheinternalhookcorrespondingto\AtEveryBibitem.
\UseUsedriverHook
Executestheinternalhookcorrespondingto\AtUsedriver.
\UseEveryCiteHook
Executestheinternalhookcorrespondingto\AtEveryCite.
\UseEveryCitekeyHook
Executestheinternalhookcorrespondingto\AtEveryCitekey.
\UseEveryMultiCiteHook
Executestheinternalhookcorrespondingto\AtMultiEveryCite.
\UseNextCiteHook
Executesandclearstheinternalhookcorrespondingto\AtNextCite.
\UseNextCitekeyHook
Executesandclearstheinternalhookcorrespondingto\AtNextCitekey.
315

\UseNextMultiCiteHook
Executesandclearstheinternalhookcorrespondingto\AtNextMultiCite.
\UseVolciteHook
Executestheinternalhookcorrespondingto\AtVolcite.
\DeferNextCitekeyHook
Locallyun-definestheinternalhookspecifiedby\AtNextCitekey. Thisessentially
defers the hook to the next entry key in the citation list, when executed in the
hprecodeiargumentof\DeclareCiteCommand(§4.3.1).
\AtEveryEntrykey{hcodei}{hsuccessi}{hfailurei}
Appendshcodeitoaninternalhookexecutedeverytimeanentrykeyisprocessed
foracitationcommandor\nocite. Thehcodeiispassedoneargument(#1),which
containstheentrykey. Ifthecodecanbeappendedtothehookhsuccessiisexecuted,
otherwisehfailureiisexecuted. Unlike\AtEveryCitekeytheentrydataofthecurrent
entrykey is not available when hcodei is processed, indeed it is not even known
whetherornotthereisanyentrydataatall.
4.10.7 Filehooks
biblatexhasrudimentarysupportforinjectingarbitrarycodebeforeandafterafile
isloadedviafilehooks. Forfilesthatareloadedusingbiblatex’sfileinterface—that
includesallbibliographyandcitationstyles—thefollowingthreehooksareavailable
\blx@filehook@preload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedbeforeitisloaded.
\blx@filehook@postload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedafteritisloaded.
\blx@filehook@failure@<filename with extension>
Thishookisexecutedif<filename with extension>cannotbefound.
biblatex generally only loads files once even if they were requested multiple
times,sothehookswillonlybeexecutedonce. Naturally,thefilehooksneedtobe
populatedbeforethefilesareloaded,sothesafestwouldbetopopulatethembefore
biblatexisloaded. Itisadvisabletoonlyappendcodetoavoidoverwritingprevious
hookcontents. Sincethenameofthefilehookincludethedotandthefileextension
theywillusuallyhavetobedefinedwithacommandlike\csapptofrometoolbox.
The.lbxfilesarespecialandmayhavetobeloadedseveraltimesinsomesituations.
Theirfilehooksare
\blx@lbxfilehook@once@preload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedbeforeitisloaded
inasituationwherethe.lbxfilesareloadedonlyonce.
\blx@lbxfilehook@once@postload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedafteritisloadedin
asituationwherethe.lbxfilesareloadedonlyonce.
316

\blx@lbxfilehook@once@failure@<filename with extension>
Thishookisexecutedif<filename with extension>cannotbefoundinasitua-
tionwherethe.lbxfilesareloadedonlyonce.
\blx@lbxfilehook@simple@preload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedbeforeitisloaded
inasituationwherethe.lbxfilesmaybeloadedmultipletimes.
\blx@lbxfilehook@simple@postload@<filename with extension>
If<filename with extension>isfound,thishookisexecutedafteritisloadedin
asituationwherethe.lbxfilesmaybeloadedmultipletimes.
\blx@lbxfilehook@simple@failure@<filename with extension>
Thishookisexecutedif<filename with extension>cannotbefoundinasitua-
tionwherethe.lbxfilesmaybeloadedmultipletimes.
Thefollowingcodesetsupbeamertoprintthebibliographylabelsinsteadofits
bibliographyiconswhennumeric.bbxafterisloaded
\csappto{blx@filehook@postload@numeric.bbx}{%
\mode<presentation>{%
\setbeamertemplate{bibliography item}{%
\insertbiblabel}}}
4.11 HintsandCaveats
Thissectionprovidessomeadditionalhintsconcerningtheauthorinterfaceofthis
package. Italsoaddressescommonproblemsandpotentialmisconceptions.
4.11.1 EntrySets
Entrysetshavealreadybeenintroducedin§3.14.5. Thissectiondiscusseshowto
processentrysetsinabibliographystyle. Fromtheperspectiveofthedriver,there
isnodifferencebetweenstaticanddynamicentrysets. Bothtypesarehandledin
thesameway. Youwillnormallyusethe\entrysetcommandfrom§4.4.1toloop
over all set members (in the order in which they are listed in the entryset field
ofthe@setentry, orintheorderinwhichtheywerepassedto\defbibentryset,
respectively)andappend\finentryattheend. That’sit. Theformattingishandled
bythedriversfortheentrytypesoftheindividualsetmembers:
\DeclareBibliographyDriver{set}{%
\entryset{}{}%
\finentry}
Youmayhavenoticedthatthenumericstyleswhichcomewiththispackagesupport
subdividedentrysets,i.e.,themembersofthesetaremarkedwithaletterorsome
othermarkersuchthatcitationsmayeitherrefertotheentiresetortoaspecificset
member. Themarkersaregeneratedasfollowsbythebibliographystyle:
317

\DeclareBibliographyDriver{set}{%
\entryset
{\printfield{entrysetcount}%
\setunit*{\addnbspace}}
{}%
\finentry}
Theentrysetcountfieldholdsanintegerindicatingthepositionofasetmember
intheentryset. Theconversionofthisnumbertoaletterorsomeothermarkeris
handledbytheformattingdirectiveoftheentrysetcountfield. Allthedriverneeds
todoisprintthefieldandaddsomewhitespace(orstartanewline). Printingthe
markersincitationsworksinasimilarway. Whereanumericstylenormallysays
\printfield{labelnumber},yousimplyappendtheentrysetcountfield:
\printfield{labelnumber}\printfield{entrysetcount}
Sincethisfieldisonlydefinedwhenprocessingcitationsreferringtoasetmember,
thereisnoneedtoaddanyadditionaltests.
Citing entry sets directly requires that a meaningful way of identifying sets is
availableinthestyle. Thisisobviousforstylesbasedonnumericoralphabeticlabels
butnotobvious(andrarelyrequired)instyleswhichconstructcitationsbasedon
textualnames/titles/datesetc. Thedefaultprovidedstyleswhichnonotconstruct
citationsbasedonlabels(authoryear,authortitle,verboseetc.) thereforedonot
supportcitingsetsdirectlyasthereisnoobviousdefaultidentifiertouseinsuch
cases and such styles rarely, if ever, employ sets anyway. Custom styles may of
coursechoosetodefineandprintacitationidentifierfordirectlycitedsets.
4.11.2 ElectronicPublishingInformation
ThestandardstylesfeaturededicatedsupportforarXivreferences. Supportforother
resourcesiseasilyadded. Thestandardstyleshandletheeprintfieldasfollows:
\iffieldundef{eprinttype}
{\printfield{eprint}}
{\printfield[eprint:\strfield{eprinttype}]{eprint}}
If an eprinttype field is available, the above code tries to use the field format
eprint:heprinttypei. If this format is undefined, \printfield automatically falls
back to the field format eprint. Therearetwopredefined field formats, the type-
specificformateprint:arxivandthefallbackformateprint:
\DeclareFieldFormat{eprint}{...}
\DeclareFieldFormat{eprint:arxiv}{...}
Inotherwords,addingsupportforadditionalresourcesisaseasyasdefiningafield
formatnamedeprint:hresourceiwherehresourceiisanidentifiertobeusedinthe
eprinttypefield.
318

4.11.3 ExternalAbstractsandAnnotations
External abstracts and annotations have been discussed in § 3.14.8. This section
provides some more background for style authors. The standard styles use the
followingmacros(frombiblatex.def)tohandleabstractsandannotations:
\newbibmacro*{annotation}{%
\iffieldundef{annotation}
{\printfile[annotation]{\bibannotationprefix\thefield{entrykey}.
,→ tex}}%
{\printfield{annotation}}}
\newcommand*{\bibannotationprefix}{bibannotation-}
\newbibmacro*{abstract}{%
\iffieldundef{abstract}
{\printfile[abstract]{\bibabstractprefix\thefield{entrykey}.tex
,→ }}%
{\printfield{abstract}}}
\newcommand*{\bibabstractprefix}{bibabstract-}
Iftheabstract/annotationfieldisundefined,theabovecodetriestoloadtheab-
stracts/annotationsfromanexternalfile. The\printfilecommandsalsoincorporate
file name prefixes which may be redefined by users. Note that you must enable
\printfileexplicitlybysettingtheloadfilespackageoptionfrom§3.1.2.1. This
featureisdisabledbydefaultforperformancereasons.
4.11.4 NameDisambiguation
The uniquename and uniquelist options introduced in § 3.1.2.3 support various
modesofoperation. Thissectionexplainsthedifferencesbetweenthesemodesby
way of example. The uniquename option disambiguates individual names in the
labelname list. The uniquelist option disambiguates the labelname list if it has
becomeambiguousaftermaxnames/minnamestruncation. Youcanuseeitheroption
stand-aloneorcombineboth.
Namedisambiguationworksbytakinga‘base’whichiscomposedofoneormore
namepartsandthendeterminingwhatneedstobeadded,ifanything,tothis‘base’to
makethenameuniqueinthecurrentrefsection. Namedisambiguationiscontrolled
bytheuniquenametemplatedeclaredwiththefollowingcommand:
\DeclareUniquenameTemplate[hnamei]{hspecificationi}
Defines the uniquename template hnamei. The hnamei is optional and defaults to
‘global’.
The hspecificationi is an ordered list of \namepart commands which define the
namepartstouseindeterminingtheuniquenameinformation.
\namepart[hoptionsi]{hnameparti}
hnameparti is one of the datamodel nameparts defined with the
\DeclareDatamodelConstantcommand(see§4.2.3). Thehoptionsiare:
use=true,false default:false
Onlyusethehnamepartiinconstructingtheuniquenameinformationifthereisa
correspondingoptionuse‘namepart’andthatoptionistrue.
319

base=true,false default:false
Thehnamepartiispartofthe‘base’whichisthemainpieceofnamepart(s)informa-
tionwhichisbeingdisambiguatedbyuniquenessinformation. Forexample,afamily
name which may be disambiguated by further given names. ‘base’ hnamepartis
must occur before any non-‘base’ hnamepartsi. There must be at least one ‘base’
hnamepartiandbiberwillreportanerrorifthisisnotthecase.
disambiguation=none,init,initorfull,full
Thehnamepartiwillbedisambiguatedatmostbyinformationatthegivenvalue. If
thisoptionisnotpresentthenthedefaultisinferredfromtheuniquenamepackage
optionsetting(see§6). The‘disambiguation’optionisignoredforhnamepartiswhich
havethe‘base’optionsetto‘true’sinceitisthesenamepartswhicharebeingdisam-
biguatedbythevalueofthenon-basehnamepartisandtherefore‘disambiguation’
doesnotapply.
noneDonotusethehnamepartitoperformanynamedisambiguation
initUseonlytheinitialsofthehnamepartitoperformnamedisambiguation
initorfullUseinitialsandifnecessarythefullhnamepartitoperformnamedisam-
biguation
fullUseonlythefullhnamepartitoperformnamedisambiguationevenifinitials
wouldsuffice
Thedefaultuniquenametemplateis:
\DeclareUniquenameTemplate{
\namepart[use=true, base=true]{prefix}
\namepart[base=true]{family}
\namepart{given}
}
Thismeansthatthe‘base’tobedisambiguatedconsistsofthe‘family’namepart,along
withanyprefix,iftheuseprefixoptionistrue. Thedisambiguationisperformed
by adding anything up to the full namepart of any non ‘base’ nameparts in the
specification,herejustthe‘given’namepart.
4.11.4.1 IndividualNames(uniquename)
Let’sstartoffwithsomeuniquenameexamples. Considerthefollowingdata:
John Doe 2008
Edward Doe 2008
John Smith 2008
Jane Smith 2008
Let’s assume we’re using an author-year style and set uniquename=false. In this
case,wewouldgetthefollowingcitations:
Doe 2008a
Doe 2008b
Smith 2008a
Smith 2008b
320

Sincethefamilynamesareambiguousandallworkshavebeenpublishedinthesame
year,anextraletterisappendedtotheyeartodisambiguatethecitations. Manystyle
guides,however,mandatethattheextraletterbeusedtodisambiguateworksbythe
sameauthorsonly,notworksbydifferentauthorswiththesamefamilyname. In
ordertodisambiguatetheauthor’sfamilyname,youareexpectedtoaddadditional
partsofthename,eitherasinitialsorinfull. Thisrequirementisaddressedbythe
uniquenameoption. Herearethesamecitationswithuniquename=init:
J. Doe 2008
E. Doe 2008
Smith 2008a
Smith 2008b
uniquename=initrestrictsnamedisambiguationtoinitials. Since‘J.Smith’would
still be ambiguous, no additional name parts are added for the ‘Smiths’. With
uniquename=full,namesareprintedinfullwhererequired:
J. Doe 2008
E. Doe 2008
John Smith 2008
Jane Smith 2008
Inordertoillustratethedifferencebetweenuniquename=init/fullandallinit/
allfull, we need to introduce the notion of a ‘visible’ name. In the following,
‘visible’namesareallnamesatapositionbeforethemaxnames/minnames/uniquelist
truncationpoint. Forexample,giventhisdata:
William Jones/Edward Doe/Jane Smith
John Doe
John Smith
andmaxnames=1,minnames=1,uniquename=init/full,wewouldgetthefollowing
namesincitations:
Jones et al.
Doe
Smith
When disambiguating names, uniquename=init/full only consider the visible
names. Sinceallvisiblefamilynamesaredistinctinthisexample,nofurthername
partsareadded. Let’scomparethattotheoutputofuniquename=allinit:
Jones et al.
J. Doe
Smith
allinitconsidersallnamesinalllabelnamelists,includingthosewhicharehidden
and replaced by ‘et al.’ as the list is truncated. In this example, ‘John Doe’ is
disambiguatedfrom‘EdwardDoe’. Sincetheambiguityofthetwo‘Smiths’can’tbe
resolvedbyaddinginitials,noinitialsareaddedinthiscase. Nowlet’scomparethat
totheoutputofuniquename=allfullwhichalsodisambiguates‘JohnSmith’from
‘JaneSmith’:
321

Jones et al.
J. Doe
John Smith
The options uniquename = mininit/minfull are similar to init/full in that
they only consider visible names, but they perform minimal disambigua-
tion. That is, they will disambiguate individual names only if they occur
in identical lists of base nameparts (for the concept of ‘base’ nameparts, see
\DeclareUniquenameTemplate in § 4.11.4). Considerthefollowingdata:
John Doe/William Jones
Edward Doe/William Jones
John Smith/William Edwards
Edward Smith/Allan Johnson
Withuniquename=init/full,wewouldget:
J. Doe and Jones
E. Doe and Jones
J. Smith and Edwards
E. Smith and Johnson
Withuniquename=mininit/minfull:
J. Doe and Jones
E. Doe and Jones
Smith and Edwards
Smith and Johnson
The‘Smiths’arenotdisambiguatedbecausethevisiblenamelistsarenotambiguous
andthemininit/minfulloptionsservetodisambiguatenamesoccurringiniden-
ticalbasenamepartlistsonly. Anotherwayoflookingatthisisthattheyglobally
disambiguate base namepart lists. When it comes to ambiguous lists, note that a
truncatedlistisconsideredtobedistinctfromanuntruncatedoneevenifthevisible
namesareidentical. Forexample,considerthefollowingdata:
John Doe/William Jones
Edward Doe
Withmaxnames=1,uniquename=init/full,wewouldget:
J. Doe et al.
E. Doe
Withuniquename=mininit/minfull:
Doe et al.
Doe
Becausethelistsdifferinthe‘etal.’,thenamesarenotdisambiguated.
The options uniquename=minyearinit/minyearfull are similar to mininit/
minfull but they will disambiguate individual names only if they occur in iden-
ticallistsofbasenamepartsandlabelyear. Considerthefollowingdata:
322

John Smith 2000
John Smith 2001
Ian Smith 2020
Brian Smith 2020
Withuniquename=init/full/mininit/minfullor,wewouldget:
J. Smith 2000
J. Smith 2001
I. Smith 2020
B. Smith 2020
Withuniquename=minyearinit/minyearfull:
Smith 2000
Smith 2001
I. Smith 2020
B. Smith 2020
Here, as with uniquelist=minyear, the emphasis is on unique references to the
bibliographyitemsratherthanuniquename/personrepresentationsinthecitations
themselves. Thetwo‘JohnSmith’citationsareuniquewithinthelistofbasename+la-
belyearcombinationsandsoneednoinitials. Theothertwocitationsarenotunique
insuchalistandsohaveinitialsadded.
4.11.4.2 ListsofNames(uniquelist)
Ambiguityisalsoanissuewithnamelists. Ifthelabelnamelististruncatedbythe
maxnames/minnamesoptions,itmaybecomeambiguous. Thistypeofambiguityis
addressedbytheuniquelistoption. Considerthefollowingdata:
Doe/Jones/Smith 2005
Smith/Johnson/Doe 2005
Smith/Doe/Edwards 2005
Smith/Doe/Jones 2005
Manyauthor-yearstylestruncatelongauthor/editorlistsincitations. Forexample,
withmaxnames=1wewouldget:
Doe et al. 2005
Smith et al. 2005a
Smith et al. 2005b
Smith et al. 2005c
Since the authors are ambiguous after truncation, the extra letter is added to the
year to ensure unique citations. Here again, many style guides mandate that the
extra letter be used to disambiguate works by the same authors only. In order to
disambiguateauthorlists,youareusuallyrequiredtoaddmorenames,exceeding
the maxnames/minnames truncation point. The uniquelist feature addresses this
requirement. Withuniquelist=true,wewouldget:
323

Doe et al. 2005
Smith, Johnson et al. 2005
Smith, Doe and Edwards 2005
Smith, Doe and Jones 2005
Theuniquelistoptionoverridesmaxnames/minnamesonaper-entrybasis. Essen-
tially,whathappensisthatthe‘etal.’ partofthecitationisexpandedtothepoint
ofnoambiguity—butnofurtherthanthat. uniquelistmayalsobecombinedwith
uniquename. Considerthefollowingdata:
John Doe/Allan Johnson/William Jones 2009
John Doe/Edward Johnson/William Jones 2009
John Doe/Jane Smith/William Jones 2009
John Doe/John Smith/William Jones 2009
John Doe/John Edwards/William Jones 2009
John Doe/John Edwards/Jack Johnson 2009
Withmaxnames=1:
Doe et al. 2009a
Doe et al. 2009b
Doe et al. 2009c
Doe et al. 2009d
Doe et al. 2009e
Doe et al. 2009f
Withmaxnames=1,uniquename=full,uniquelist=true:
Doe, A. Johnson et al. 2009
Doe, E. Johnson et al. 2009
Doe, Jane Smith et al. 2009
Doe, John Smith et al. 2009
Doe, Edwards and Jones 2009
Doe, Edwards and Johnson 2009
With uniquelist=minyear, list disambiguation only happens if the visible list is
identicaltoanothervisiblelistwiththesamelabelyear. Thisisusefulforauthor-year
styleswhichonlyrequirethatthecitationasawholebeunique,butdonotguarantee
unambiguousauthorshipinformationincitations. Thismodeisconceptuallyrelated
touniquename=mininit/minfull. Considerthisexample:
Smith/Jones 2000
Smith/Johnson 2001
Withmaxnames=1anduniquelist=true,wewouldget:
Smith and Jones 2000
Smith and Johnson 2001
Withuniquelist=minyear:
324

| Smith et al. | 2000 |     |
| ------------ | ---- | --- |
| Smith et al. | 2001 |     |
Withuniquelist=minyear,itisnotclearthattheauthorsaredifferentforthetwo
worksbutthecitationsasawholearestillunambiguoussincetheyearisdifferent.
In contrast to that, uniquelist=true disambiguates the authorship even if this
informationisnotrequiredtouniquelylocatetheworksinthebibliography. Let’s
consideranotherexample:
| Vogel/Beast/Garble/Rook  |     | 2000 |
| ------------------------ | --- | ---- |
| Vogel/Beast/Tremble/Bite |     | 2000 |
| Vogel/Beast/Acid/Squeeze |     | 2001 |
Withmaxnames=3,minnames=1,uniquelist=true,wewouldget:
| Vogel, Beast, | Garble  | et al. 2000 |
| ------------- | ------- | ----------- |
| Vogel, Beast, | Tremble | et al. 2000 |
| Vogel, Beast, | Acid et | al. 2001    |
Withuniquelist=minyear:
| Vogel, Beast, | Garble  | et al. 2000 |
| ------------- | ------- | ----------- |
| Vogel, Beast, | Tremble | et al. 2000 |
| Vogel et al.  | 2001    |             |
Inthelastcitation, uniquelist=minyeardoesnotoverridemaxnames/minnamesas
thecitationdoesnotneeddisambiguatingfromtheothertwobecausetheyearis
different.
4.11.5 NameIdentity
Alotdependsonwhetherseveralnamesinabibliographyrefertothesameperson
ornot. Bydefault,thisisdeterminedpurelysyntacticallybywhetherornotallof
thefullpartsofanameareidentical. Thiscanbechangedhoweverbyalteringthe
algorithmthatbiberusestocalculatevarioushashesfornamesviathefollowing
command:
\DeclareNamehashTemplate[hnamei]{hspecificationi}
Definesthetemplatehnameiusedtoconstructthehashesfromthepartsofaname.
Thehnameiisoptionalanddefaultsto‘global’.
hspecificationi
The is an ordered list of \namepart commands which define the
namepartstouseinconstructingnamehashes.
\namepart[hoptionsi]{hnameparti}
hnameparti is one of the datamodel nameparts defined with the
\DeclareDatamodelConstantcommand(see§4.2.3). Thehoptionsiare:
hashscope=init,full
Thehnamepartiwillbeusedintheconstructionofthehashforthenameandthe
datausedfromthenameparttodothisisoneof:
325

initUseonlytheinitialsofthehnamepartiinthehashconstruction
fullUsethefullhnamepartiinthehashconstruction
Thedefaultnamehashtemplateis:
\DeclareNamehashTemplate{
\namepart[hashscope=full]{family}
\namepart[hashscope=full]{given}
\namepart[hashscope=full]{prefix}
\namepart[hashscope=full]{suffix}
}
This means that these nameparts (which all must be valid datamodel nameparts
declared by \DeclareDatamodelConstant) will be used in the order specified to
constructnamehashes. Thefullnamepartwillbeusedforallnameparts.
Iftherewasabibliographyincluding,forexample,severalsyntacticvariationsof
anamewheresometimesthefullgivennamewaspresentandsometimesonlythe
initialbutthesereferredtothesameperson,youcouldset:
\DeclareNamehashTemplate{
\namepart[hashscope=full]{family}
\namepart[hashscope=init]{given}
\namepart[hashscope=full]{prefix}
\namepart[hashscope=full]{suffix}
}
Whichwouldgeneratehashesusingonlytheinitialsofthegivenname,thustreating
‘John Smith’ and ‘J. Smith’ as the same person for hashing purposes. This would
prevent biblatex from treating these as different people even though based on
syntaxalone(whichisthedefault),theywouldbe.
4.11.5.1 Customnamehashesviatheextendednameformat
Anotherwayofcustomisingnamehashgenerationisbyoverridingcompletelythe
namehashconstructionalgorithmbypassinganidentifierstringforthenameusing
the extended name format (§ 3.4). This string will be turned into a hash as given
andanynamehashtemplatewillbeignoredforthisname. Forexample, tohave
‘JohnSmith’and‘J.Smith’seenasthesamepersonfornameidentitypurposes,an
alternativetotheabovewouldbe:
AUTHOR = {id=jshash, family=Smith, given=J. and id=jshash, family=
,→ Smith, given=John}
Here, the identical hidi parameters of the extended name format ensure that the
hashesforthetwonameswillbethesame. Thishasthesameeffectastheabove
example using \DeclareNamehashTemplate and is intended for trickier situations
where people change names and there is therefore no mere syntactic difference
betweendifferentnameformsforthesameperson.
326

4.11.6 TrackersinFloatsandTOC/LOT/LOF
If a citation is given in a float (typically in the caption of a figure or table), schol-
arlybackreferenceslike‘ibidem’orbackreferencesbasedonthepagetrackerget
ambiguous because floats are objects which are (physically and logically) placed
outsidetheflowoftext,hencethelogicofsuchreferencesappliespoorlytothem. To
avoidanysuchambiguities,thecitationandpagetrackersaretemporarilydisabled
inallfloatsunlessexplicitlyrequestedwithtrackfloats. Inadditiontothat,these
trackersplusthebackreferencetracker(backref)aretemporarilydisabledinthe
tableofcontents,thelistoffigures,andthelistoftables.
4.11.7 MixingProgrammingInterfaces
Thebiblatexpackageprovidestwomainprogramminginterfacesforstyleauthors.
The\DeclareBibliographyDrivercommand,whichdefinesahandlerforanentry
type,istypicallyusedinbbxfiles. \DeclareCiteCommand,whichdefinesanewcita-
tioncommand,istypicallyusedincbxfiles. However,insomecasesitisconvenient
tomixthesetwointerfaces. Forexample,the\fullcitecommandprintsaverbose
citationsimilartothefullbibliographyentry. Itisessentiallydefinedasfollows:
\DeclareCiteCommand{\fullcite}
{...}
{\usedriver{...}{\thefield{entrytype}}}
{...}
{...}
As you can see, the core code which prints the citations simply executes the bib-
liography driver defined with \DeclareBibliographyDriver for the type of the
currententry. Whenwritingacitationstyleforaverbosecitationscheme,itisoften
convenienttousethefollowingstructure:
\ProvidesFile{example.cbx}[2007/06/09 v1.0 biblatex citation style]
\DeclareCiteCommand{\cite}
{...}
{\usedriver{...}{cite:\thefield{entrytype}}}
{...}
{...}
\DeclareBibliographyDriver{cite:article}{...}
\DeclareBibliographyDriver{cite:book}{...}
\DeclareBibliographyDriver{cite:inbook}{...}
...
Anothercaseinwhichmixinginterfacesishelpfularestylesusingcross-references
withinthebibliography. Forexample,whenprintingan@incollectionentry,the
data inherited from the @collection parent entry would be replaced by a short
pointertotherespectiveparententry:
[1] AudreyAuthor: Titleofarticle. In: [2],pp.134–165.
[2] EdwardEditor,ed.: Titleofcollection. Publisher: Location,1995.
327

Onewaytoimplementsuchcross-referenceswithinthebibliographyistothink
ofthemascitationswhichusethevalueofthexreforcrossreffieldastheentry
key. Hereisanexample:
\ProvidesFile{example.bbx}[2007/06/09 v1.0 biblatex bibliography
,→ style]
\DeclareCiteCommand{\bbx@xref}
{}
{...}% code for cross-references
{}
{}
\DeclareBibliographyDriver{incollection}{%
...
\iffieldundef{xref}
{...}% code if no cross-reference
{\bbx@xref{\thefield{xref}}}%
...
}
When defining \bbx@xref, the hprecodei, hpostcodei, and hsepcodei arguments of
\DeclareCiteCommandareleftemptyintheaboveexamplebecausetheywillnotbe
used anyway. The cross-reference is printed by the hloopcodei of \bbx@xref. For
furtherdetailsonthexreffield,referto§2.2.3andtothehintsin§2.4.1. Alsosee
the\iffieldxref,\iflistxref,and\ifnamexreftestsin§4.6.2. Theabovecould
alsobeimplementedusingthe\entrydatacommandfrom§4.4.1:
\ProvidesFile{example.bbx}[2007/06/09 v1.0 biblatex bibliography
,→ style]
\DeclareBibliographyDriver{incollection}{%
...
\iffieldundef{xref}
{...}% code if no cross-reference
{\entrydata{\thefield{xref}}{%
% code for cross-references
...
}}%
...
}
4.11.8 UsingthePunctuationTracker
4.11.8.1 TheBasics
Thereisonefundamentalprinciplestyleauthorsshouldkeepinmindwhendesigning
abibliographydriver: blockandunitpunctuationishandledasynchronously. Thisis
bestexplainedbywayofexample. Considerthefollowingcodesnippet:
328

\printfield{title}%
\newunit
\printfield{edition}%
\newunit
\printfield{note}%
Ifthereisnoeditionfield,thispieceofcodewillnotprint:
Title. . Note
butrather:
Title. Note
because the unit punctuation tracker works asynchronously. \newunit will not
printtheunitpunctuationimmediately. Itmerelyrecordsaunitboundaryandputs
\newunitpunctonthepunctuationbuffer. Thisbufferwillbehandledbysubsequent
\printfield,\printlist,orsimilarcommandsbutonlyiftherespectivefieldorlist
isdefined. Commandslike\printfieldwillconsiderthreefactorspriortoinserting
anyblockorunitpunctuation:
• Hasanewunit/blockbeenrequestedatall?
=Isthereanypreceding\newunitor\newblockcommand?
• Didtheprecedingcommandsprintanything?
=Isthereanypreceding\printfieldorsimilarcommand?
=Didthiscommandactuallyprintanything?
• Areweabouttoprintanythingnow?
=Isthefield/listtobeprocessednowdefined?
Blockandunitpunctuationwillonlybeinsertedifall oftheseconditionsapply. Let’s
reconsidertheaboveexample:
\printfield{title}%
\newunit
\printfield{edition}%
\newunit
\printfield{note}%
Here’swhathappensiftheeditionfieldisundefined. Thefirst\printfieldcom-
mand prints the title and sets an internal ‘new text’ flag. The first \newunit sets
an internal ‘new unit’ flag. No punctuation has been printed at this point. The
second\printfielddoesnothingbecausetheeditionfieldisundefined. Thenext
\newunitcommandsetstheinternalflag‘newunit’again. Stillnopunctuationhas
beenprinted. Thethird\printfieldchecksifthenotefieldisdefined. Ifso,itlooks
atthe‘newtext’and‘newunit’flags. Ifbothareset,itinsertsthepunctuationbuffer
beforeprintingthenote. Itthenclearsthe‘newunit’flagandsetsthe‘newtext’flag
again.
329

This may all sound more complicated than it is. In practice, it means that it is
possibletowritelargepartsofabibliographydriverinasequentialway. Theadvan-
tageofthisapproachbecomesobviouswhentryingtowritetheabovecodewithout
usingthepunctuationtracker. Suchanattemptwillleadtoaratherconvolutedset
of\iffieldundeftestsrequiredtocheckforallpossiblefieldcombinations(note
thatthecodebelowhandlesthreefields;atypicaldrivermayneedtocaterforsome
twodozenfields):
\iffieldundef{title}%
{\iffieldundef{edition}
{\printfield{note}}
{\printfield{edition}%
\iffieldundef{note}%
{}
{. \printfield{note}}}}
{\printfield{title}%
\iffieldundef{edition}
{}
{. \printfield{edition}}%
\iffieldundef{note}
{}
{. \printfield{note}}}%
4.11.8.2 CommonMistakes
Itisafairlycommonmisconceptiontothinkoftheunitpunctuationassomething
thatishandledsynchronously. Thistypicallycausesproblemsifthedriverincludes
anyliteraltext. Considerthiserroneouscodesnippetwhichwillgeneratemisplaced
unitpunctuation:
\printfield{title}%
\newunit
(\printfield{series} \printfield{number})%
Thiscodewillyieldthefollowingresult:
Title (. Series Number)
Here’swhathappens. Thefirst\printfieldprintsthetitle. Then\newunitmarksa
unitboundarybutdoesnotprintanything. Theunitpunctuationisprintedbythenext
\printfieldcommand. That’stheasynchronouspartmentionedbefore. However,
theopeningparenthesisisprintedimmediatelybeforethenext\printfieldinserts
theunitpunctuation,leadingtoamisplacedperiod. Wheninsertingany literaltext
suchasparentheses(includingthoseprintedbycommandssuchas\bibopenparen
and\mkbibparens),alwayswrapthetextina\printtextcommand. Forthepunc-
tuationtrackertoworkasexpected,itneedstoknowaboutallliteraltextinserted
by a driver. This is what \printtext is all about. \printtext interfaces with the
punctuationtrackerandensuresthatthepunctuationbufferisinsertedbeforethe
literaltextgetsprinted. Italsosetstheinternal‘newtext’flag. Notethereisinfacta
thirdpieceofliteraltextinthisexample: thespaceafter\printfield{series}. In
thecorrectedexample,wewillusethepunctuationtrackertohandlethatspace.
330

\printfield{title}%
\newunit
\printtext{(}%
\printfield{series}%
\setunit*{\addspace}%
\printfield{number}%
\printtext{)}%
While the above code will work as expected, the recommended way to handle
parentheses,quotes,andotherthingswhichenclosemorethanonefield,istodefine
afieldformat:
\DeclareFieldFormat{parens}{\mkbibparens{#1}}
Fieldformatsmaybeusedwithboth\printfieldand\printtext,hencewecan
usethemtoencloseseveralfieldsinasinglepairofparentheses:
\printtext[parens]{%
\printfield{series}%
\setunit*{\addspace}%
\printfield{number}%
}%
Westillneedtohandlecasesinwhichthereisnoseriesinformationatall,solet’s
improvethecodesomemore:
\iffieldundef{series}
{}
{\printtext[parens]{%
\printfield{series}%
\setunit*{\addspace}%
\printfield{number}}}%
One final hint: localisation strings are not literal text as far as the punctuation
trackerisconcerned. Since\bibstringandsimilarcommandsinterfacewiththe
punctuationtracker,thereisnoneedtowrapthemina\printtextcommand.
4.11.8.3 AdvancedUsage
Thepunctuationtrackermayalsobeusedtohandlemorecomplexscenarios. For
example, suppose that we want the fields location, publisher, and year to be
renderedinoneofthefollowingformats,dependingontheavailabledata:
...text. Location: Publisher, Year. Text...
...text. Location: Publisher. Text...
...text. Location: Year. Text...
...text. Publisher, Year. Text...
...text. Location. Text...
...text. Publisher. Text...
...text. Year. Text...
331

This problem can be solved with a rather convoluted set of \iflistundef and
\iffieldundeftestswhichcheckforallpossiblefieldcombinations:
\iflistundef{location}
{\iflistundef{publisher}
{\printfield{year}}
{\printlist{publisher}%
\iffieldundef{year}
{}
{, \printfield{year}}}}
{\printlist{location}%
\iflistundef{publisher}%
{\iffieldundef{year}
{}
{: \printfield{year}}}
{: \printlist{publisher}%
\iffieldundef{year}
{}
{, \printfield{year}}}}%
The above could be written in a somewhat more readable way by employing
\ifthenelseandthebooleanoperatorsdiscussedin§4.6.3. Theapproachwould
stillbeessentiallythesame. However,itmayalsobewrittensequentially:
\newunit
\printlist{location}%
\setunit*{\addcolon\space}%
\printlist{publisher}%
\setunit*{\addcomma\space}%
\printfield{year}%
\newunit
Inpractice,youwilloftenuseacombinationofexplicittestsandtheimplicittests
performedbythepunctuationtracker. Forexample,considerthefollowingformat
(notethepunctuationafterthelocationifthereisnopublisher):
...text. Location: Publisher, Year. Text...
...text. Location: Publisher. Text...
...text. Location, Year. Text...
...text. Publisher, Year. Text...
...text. Location. Text...
...text. Publisher. Text...
...text. Year. Text...
Thiscanbehandledbythefollowingcode:
\newunit
\printlist{location}%
\iflistundef{publisher}
{\setunit*{\addcomma\space}}
332

{\setunit*{\addcolon\space}}%
\printlist{publisher}%
\setunit*{\addcomma\space}%
\printfield{year}%
\newunit
Sincethepunctuationafterthelocationisspecialifthereisnopublisher,weneedone
\iflistundeftesttocatchthiscase. Everythingelseishandledbythepunctuation
tracker.
4.11.9 CustomLocalizationModules
Styleguidesmayincludeprovisionsastohowstringslike‘edition’shouldbeabbre-
viatedortheymaymandatecertainfixedexpressions. Forexample,themlastyle
guiderequiresauthorstousetheterm‘WorksCited’ratherthan‘Bibliography’or
‘References’ in the heading of the bibliography. Localization commands such as
\DefineBibliographyStringsfrom§3.10mayindeedbeusedincbxandbbxfiles
to handle such cases. However, overloading style files with translations is rather
inconvenient. Thisiswhere\DeclareLanguageMappingfrom§4.9.1comesintoplay.
Thiscommandmapsanlbxfilewithalternativetranslationstoababel/polyglossia
language. Forexample,youcouldcreateafilenamedfrench-humanities.lbxwhich
provides French translations adapted for use in the humanities and map it to the
babel/polyglossialanguagefrenchinthepreambleorintheconfigurationfile:
\DeclareLanguageMapping{french}{french-humanities}
If the document language is set to french, french-humanities.lbx will replace
french.lbx. Comingbacktothemlaexamplementionedabove,anmlastylemay
comewithanamerican-mla.lbxfiletoprovidestringswhichcomplywiththemla
styleguide. Itwoulddeclarethefollowingmappinginthecbxand/orbbxfile:
\DeclareLanguageMapping{american}{american-mla}
Use\DeclareLanguageMappingSuffix(see§4.9.1)todefinesuchamappingforall
languages.
Sincethealternativelbxfilecaninheritstringsfromthestandardamerican.lbx
module,american-mla.lbxmaybeasshortasthis:
\ProvidesFile{american-mla.lbx}[2008/10/01 v1.0 biblatex localization
,→ ]
\InheritBibliographyExtras{american}
\DeclareBibliographyStrings{%
inherit = {american},
bibliography = {{Works Cited}{Works Cited}},
references = {{Works Cited}{Works Cited}},
}
\endinput
Alternative lbx files must ensure that the localisation module is complete. They
should do so by inheriting data from the corresponding standard module. If
333

the language american is mapped to american-mla.lbx, biblatex will not load
american.lbx unless this module is requested explicitly. In the above example,
inheriting ‘strings’ and ‘extras’ will cause biblatex to load american.lbx before
applyingthemodificationsinamerican-mla.lbx.
Note that \DeclareLanguageMapping is not intended to handle language vari-
ants (e.g., American English vs. British English) or babel/polyglossia language
aliases(e.g.,USenglishvs. american). Forexample,babel/polyglossiaoffersthe
USenglish option which is similar to american. Therefore, biblatex comes with
an USenglish.lbx file which simply inherits all data from american.lbx (which
in turn gets the ‘strings’ from english.lbx). In other words, the mapping of lan-
guagevariantsandbabel/polyglossialanguagealiaseshappensonthefilelevel,
thepointbeingthatbiblatex’slanguagesupportcanbeextendedsimplybyadding
additional lbx files. There is no need for centralized mapping. If you need sup-
port for, say, Portuguese (babel/polyglossia: portuges), you create a file named
portuges.lbx. If babel/polyglossia offered an alias named brasil, you would
createbrasil.lbxandinheritthedatafromportuges.lbx. Incontrasttothat,the
pointof\DeclareLanguageMappingishandlingstylistic variantslike‘humanitiesvs.
naturalsciences’or‘mlavs. apa’etc. whichwilltypicallybebuiltontopofexisting
lbxfiles.
4.11.10 Grouping
Inacitationorbibliographystyle,youmayneedtosetflagsorstorecertainvalues
for later use. In this case, it is crucial to understand the basic grouping structure
imposed by this package. As a rule of thumb, you are working in a large group
wheneverauthorcommandssuchasthosediscussedin§4.6areavailablebecause
theauthorinterfaceofthispackageisonlyenabledlocally. Ifanybibliographicdata
isavailable,thereisatleastoneadditionalgroup. Herearesomegeneralrules:
• Theentirelistofreferencesprintedby\printbibliographyandsimilarcom-
mands is processed in a group. Each entry in the list is processed in an
additional group which encloses the hitemcodei of \defbibenvironment as
wellasalldrivercode.
• Theentirebibliographylistprintedby\printbiblistisprocessedinagroup.
Eachentryinthelistisprocessedinanadditionalgroupwhichenclosesthe
hitemcodeiof\defbibenvironmentaswellasalldrivercode.
• Allcitationcommandsdefinedwith\DeclareCiteCommandareprocessedina
groupholdingthecompletecitationcodeconsistingofthehprecodei,hsepcodei,
hloopcodei,andhpostcodeiarguments. Thehloopcodeiisenclosedinanaddi-
tionalgroupeverytimeitisexecuted. Ifanyhwrappericodehasbeenspecified,
theentireunitconsistingofthewrappercodeandthecitationcodeiswrapped
inanadditionalgroup.
• Inadditiontothegroupingimposedbyallbackendcommandsdefinedwith
\DeclareCiteCommand,all‘autocite’and‘multicite’definitionsimplyanaddi-
tionalgroup.
• \printfile, \printtext, \printfield, \printlist, and \printnames form
groups. Thisimpliesthatallformattingdirectiveswillbeprocessedwithina
groupoftheirown.
334

• Alllbxfilesareloadedandprocessedinagroup. Ifanlbxfilecontainsany
codewhichisnotpartof\DeclareBibliographyExtras,thedefinitionsmust
beglobal.
Note that using \aftergroup in citation and bibliography styles is unreliable
becausetheprecisenumberofgroupsemployedinacertaincontextmaychangein
futureversionsofthispackage. Iftheaboveliststatesthatsomethingisprocessedin
agroup,thismeansthatthereisatleastone group. Theremayalsobeseveralnested
ones.
4.11.11 Namespaces
Inordertominimizetheriskofnameclashes,LaTeXpackagestypicallyprefixthe
namesofinternalmacroswithashortstringspecifictothepackage. Forexample,if
thefoobarpackagerequiresamacroforinternaluse,itwouldtypicallybecalled
\FB@macroor\foo@macroratherthan\macroor\@macro. Hereisalistoftheprefixes
usedorrecommendedbybiblatex:
blx All macros with names like \blx@name are strictly reserved for internal use. This
alsoappliestocounternames,lengthregisters,booleanswitches,andsoon. These
macrosmaybealteredinbackwards-incompatibleways,theymayberenamedor
even removed at any time without further notice. Such changes will not even be
mentionedintherevisionhistoryorthereleasenotes. Inshort: neveruseanymacros
withthestringblxintheirnameinanystyles.
abx Macros prefixed with abx are also internal macros but they are fairly stable. It is
alwayspreferabletousethefacilitiesprovidedbytheofficialauthorinterface,but
theremaybecasesinwhichusinganabxmacroisconvenient.
bbx Thisistherecommendedprefixforinternalmacrosdefinedinbibliographystyles.
cbx Thisistherecommendedprefixforinternalmacrosdefinedincitationstyles.
lbx This is the recommended base prefix for internal macros defined in localisation
modules. Thelocalisationmoduleshouldaddasecondprefixtospecifythelanguage.
Forexample,aninternalmacrodefinedbytheSpanishlocalisationmodulewouldbe
named\lbx@es@macro.
Appendix
A Default Driver Source Mappings
Thesearethedriverdefaultsourcemappings.
A.1 bibtex
The bibtex driver is of course the most comprehensive and mature of the
biblatex/bibersupporteddataformats. Thesesourcemappingdefaultsarehowthe
aliasesfromsections§2.1.2and§2.2.5areimplemented.
\DeclareDriverSourcemap[datatype=bibtex]{
\map{
\step[typesource=conference, typetarget=inproceedings]
335

| \step[typesource=electronic, |     |     | typetarget=online] |     |     |
| ---------------------------- | --- | --- | ------------------ | --- | --- |
| \step[typesource=www,        |     |     | typetarget=online] |     |     |
}
\map{
| \step[typesource=mastersthesis, |     |     | typetarget=thesis,   | final] |     |
| ------------------------------- | --- | --- | -------------------- | ------ | --- |
| \step[fieldset=type,            |     |     | fieldvalue=mathesis] |        |     |
}
\map{
| \step[typesource=phdthesis, |     | typetarget=thesis,    |     | final] |     |
| --------------------------- | --- | --------------------- | --- | ------ | --- |
| \step[fieldset=type,        |     | fieldvalue=phdthesis] |     |        |     |
}
\map{
| \step[typesource=techreport, |     |     | typetarget=report,     | final] |     |
| ---------------------------- | --- | --- | ---------------------- | ------ | --- |
| \step[fieldset=type,         |     |     | fieldvalue=techreport] |        |     |
}
\map{
| \step[fieldsource=address,       |     |     | fieldtarget=location]     |     |     |
| -------------------------------- | --- | --- | ------------------------- | --- | --- |
| \step[fieldsource=school,        |     |     | fieldtarget=institution]  |     |     |
| \step[fieldsource=annote,        |     |     | fieldtarget=annotation]   |     |     |
| \step[fieldsource=archiveprefix, |     |     | fieldtarget=eprinttype]   |     |     |
| \step[fieldsource=journal,       |     |     | fieldtarget=journaltitle] |     |     |
| \step[fieldsource=primaryclass,  |     |     | fieldtarget=eprintclass]  |     |     |
| \step[fieldsource=key,           |     |     | fieldtarget=sortkey]      |     |     |
| \step[fieldsource=pdf,           |     |     | fieldtarget=file]         |     |     |
}
}
| B Default | Inheritance | Setup |     |     |     |
| --------- | ----------- | ----- | --- | --- | --- |
The following table shows the biber cross-referencing rules defined by default.
Pleasereferto§§2.4.1and4.5.12forexplanation.
| Types  |        |     | Fields   |     |        |
| ------ | ------ | --- | -------- | --- | ------ |
| Source | Target |     | Source   |     | Target |
| *      | *      |     | ids      |     | –      |
|        |        |     | crossref |     | –      |
|        |        |     | xref     |     | –      |
|        |        |     | entryset |     | –      |
–
entrysubtype
|     |     |     | execute |     | –   |
| --- | --- | --- | ------- | --- | --- |
|     |     |     | label   |     | –   |
|     |     |     | options |     | –   |
|     |     |     | presort |     | –   |
|     |     |     | related |     | –   |
–
relatedoptions
|     |     |     | relatedstring  |     | –   |
| --- | --- | --- | -------------- | --- | --- |
|     |     |     | relatedtype    |     | –   |
|     |     |     | shorthand      |     | –   |
|     |     |     | shorthandintro |     | –   |
–
sortkey
| mvbook,book | inbook,bookinbook,suppbook |     | author |     | author     |
| ----------- | -------------------------- | --- | ------ | --- | ---------- |
|             |                            |     | author |     | bookauthor |
336

| Types  |                                 | Fields     |                |
| ------ | ------------------------------- | ---------- | -------------- |
| Source | Target                          | Source     | Target         |
| mvbook | book,inbook,bookinbook,suppbook | title      | maintitle      |
|        |                                 | subtitle   | mainsubtitle   |
|        |                                 | titleaddon | maintitleaddon |
|        |                                 | shorttitle | –              |
|        |                                 | sorttitle  | –              |
|        |                                 | indextitle | –              |
–
indexsorttitle
mvcollection, collection,reference,incollection, title maintitle
| mvreference | inreference,suppcollection | subtitle   | mainsubtitle   |
| ----------- | -------------------------- | ---------- | -------------- |
|             |                            | titleaddon | maintitleaddon |
|             |                            | shorttitle | –              |
–
sorttitle
|               |                           | indextitle     | –              |
| ------------- | ------------------------- | -------------- | -------------- |
|               |                           | indexsorttitle | –              |
| mvproceedings | proceedings,inproceedings | title          | maintitle      |
|               |                           | subtitle       | mainsubtitle   |
|               |                           | titleaddon     | maintitleaddon |
|               |                           | shorttitle     | –              |
|               |                           | sorttitle      | –              |
|               |                           | indextitle     | –              |
|               |                           | indexsorttitle | –              |
inbook,bookinbook,suppbook
| book |     | title      | booktitle      |
| ---- | --- | ---------- | -------------- |
|      |     | subtitle   | booksubtitle   |
|      |     | titleaddon | booktitleaddon |
|      |     | shorttitle | –              |
|      |     | sorttitle  | –              |
–
indextitle
|             |                           | indexsorttitle | –              |
| ----------- | ------------------------- | -------------- | -------------- |
| collection, | incollection,inreference, | title          | booktitle      |
| reference   | suppcollection            | subtitle       | booksubtitle   |
|             |                           | titleaddon     | booktitleaddon |
–
shorttitle
|             |               | sorttitle      | –              |
| ----------- | ------------- | -------------- | -------------- |
|             |               | indextitle     | –              |
|             |               | indexsorttitle | –              |
| proceedings | inproceedings | title          | booktitle      |
|             |               | subtitle       | booksubtitle   |
|             |               | titleaddon     | booktitleaddon |
|             |               | shorttitle     | –              |
|             |               | sorttitle      | –              |
|             |               | indextitle     | –              |
–
indexsorttitle
| periodical | article,suppperiodical | title      | journaltitle    |
| ---------- | ---------------------- | ---------- | --------------- |
|            |                        | subtitle   | journalsubtitle |
|            |                        | shorttitle | –               |
–
sorttitle
|     |     | indextitle     | –   |
| --- | --- | -------------- | --- |
|     |     | indexsorttitle | –   |
| *   | *   | *              | *   |
337

| C Default | Sorting | Templates |     |     |     |
| --------- | ------- | --------- | --- | --- | --- |
C.1 AlphabeticTemplates1
The following table shows the standard alphabetic sorting templates defined by
default. Pleasereferto§3.6forexplanation.
Option Templatename
| nty presort | →sortname | →sorttitle | →sortyear | →volume |     |
| ----------- | --------- | ---------- | --------- | ------- | --- |
| ,→mm        | ,→author  | ,→title    | ,→year    |         |     |
,→editor
,→translator
,→sorttitle
,→title
| nyt presort | →sortname | →sortyear | →sorttitle | →volume |     |
| ----------- | --------- | --------- | ---------- | ------- | --- |
| ,→mm        | ,→author  | ,→year    | ,→title    |         |     |
,→editor
,→translator
,→sorttitle
,→title
| nyvt presort | →sortname | →sortyear | →volume | →sorttitle |     |
| ------------ | --------- | --------- | ------- | ---------- | --- |
| ,→mm         | ,→author  | ,→year    |         | ,→title    |     |
,→editor
,→translator
,→sorttitle
,→title
| all presort | →sortkey |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
,→mm
C.2 AlphabeticTemplates2
Thefollowingtableshowsthealphabeticsortingtemplatesforalphabeticstyles
| definedbydefault. | Pleasereferto§3.6forexplanation. |     |     |     |     |
| ----------------- | -------------------------------- | --- | --- | --- | --- |
Option Templatename
anyt presort →labelalpha →sortname →sortyear →sorttitle →volume
| ,→mm |     | ,→author | ,→year | ,→title |     |
| ---- | --- | -------- | ------ | ------- | --- |
,→editor
,→translator
,→sorttitle
,→title
anyvt presort →labelalpha →sortname →sortyear →volume →sorttitle
| ,→mm |     | ,→author | ,→year |     | ,→title |
| ---- | --- | -------- | ------ | --- | ------- |
,→editor
,→translator
,→sorttitle
,→title
| all presort | →labelalpha | →sortkey |     |     |     |
| ----------- | ----------- | -------- | --- | --- | --- |
,→mm
C.3 ChronologicalTemplates
Thefollowingtableshowsthechronologicalsortingtemplatesdefinedbydefault.
Pleasereferto§3.6forexplanation.
338

Option Templatename
ynt presort →sortyear →sortname →sorttitle
,→mm ,→year ,→author ,→title
,→9999 ,→editor
,→translator
,→sorttitle
,→title
ydnt presort →sortyear(desc.) →sortname →sorttitle
,→mm ,→year(desc.) ,→author ,→title
,→9999 ,→editor
,→translator
,→sorttitle
,→title
all presort →sortkey
,→mm
D biblatexml
ThebiblatexmlXMLdatasourceformatisdesignedtobeanextensibleandmodern
data source format for biblatex users. There are limitations with BibTeX format
.bibfiles,inparticularonemightmentionUTF-8supportandnameformats. biber
goes some way to addressing the UTF-8 limitations by using a modified version
ofthebtparseClibrarybuttheratherarchaicnameparsingrulesforBibTeXare
hard-codedandspecifictosimpleWesternnames.
biblatexml isan XMLformat forbibliographic data. When biber eitherreads
orwritesbiblatexmlformatdatasources,itautomaticallywritesaRelaXNGXML
schemaforthedatasourceswhichisdynamicallygeneratedfromtheactivebiblatex
datamodel. Thereisnostaticschemaforbiblatexmldatasourcesbecausetheallow-
ablefieldsetc. dependonthedatamodel. Theformatofbiblatexmldatasourcesis
relativelyself-explanatory—itisusuallyonlynecessarytogenerateabiblatexml
datasourcefromexistingBibTeXformatdatasources(usingbiber’s‘tool’mode)in
order to understand the format. biber also allows users to validate biblatexml
datasourcesagainstthedatamodelgeneratedschema.
SincethebiblatexmlformatisXMLanddependsonthedatamodelandthedata
modelisextensiblebytheuser(see§4.5.4),thebiblatexmlformatcandealwith
extensionsthatBibTeXformatdatasourcescannot,e.g. newnameparts,optionsat
sub-entryscope. SinceitisanXMLformat,itisrelativelyeasytotransformitinto
otherXMLformatsorHTMLusingstandardXMLprocessinglibrariesandtools.
Hereisanexplanationoftheformatwithexamples. Byconvention,biblatexml
fileshavea.bltxmlextensionandkpsewhichunderstandsthisfileextension.
D.1 Header
biblatexmlfilesbeginwiththestandardXMLheader:
<?xml version="1.0" encoding="UTF-8"?>
Theschemamodel,typeandschematypenamespacearegiveninthefollowingline:
<?xml-model href="biblatexml.rng"
type="application/xml"
schematypens="http://relaxng.org/ns/structure/1.0"?>
339

Whenbibergeneratesbiblatexmldatasources,itautomaticallyaddsthislineand
pointstheschemamodel(href)attributeattheautomaticallygeneratedRelaXNG
XMLschemaforeaseofvalidation.
D.2 Body
Thebodyofabiblatexmldatasourcelookslike:
<bltx:entries
xmlns:bltx="http://biblatex-biber.sourceforge.net/biblatexml">
<bltx:entry id="" entrytype="">
</bltx:entry>
.
.
.
<bltx:entry id="" entrytype="">
</bltx:entry>
</bltx:entries>
Thebodyisoneormoreentryelementsinsidethetop-levelentrieselementand
everythingisinthebltxnamespace. Anentryhasanidattributecorrespondingto
aBibTeXentrykeyandaentrytypeattributecorrespondingtoaBibTeXentrytype.
Forexample,thebiblatexml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="biblatexml.rng"
type="application/xml"
schematypens="http://relaxng.org/ns/structure/1.0"?>
<bltx:entries
xmlns:bltx="http://biblatex-biber.sourceforge.net/biblatexml">
<bltx:entry id="key1" entrytype="book">
</bltx:entry>
</bltx:entries>
CorrespondstotheBibTeX.bib
@book{key1,
}
Ingeneral,theXMLelementsinabiblatexmlformatdatasourcefilehavenames
correspondingtothefieldsinthedatamodel,justlikeBibTeXformatdatasources. So
forexample,theBibTeXformatsource
@book{key1,
TITLE = {...},
ISSUE = {...},
NOTE = {...}
}
wouldbe,inbiblatexml
340

| <bltx:entry | id="key1" | entrytype="book"> |     |
| ----------- | --------- | ----------------- | --- |
<bltx:title>...</bltx:title>
<bltx:issue>...</bltx:issue>
<bltx:note>...</bltx:note>
</bltx:entry>
Thefollowingexceptionstothissimplemappingaretobenoted
D.2.1 Keyaliases
Citationkeyaliasesarespecifiedlikethis:
<bltx:ids>
<bltx:key>alias1</bltx:key>
<bltx:key>alias2</bltx:key>
</bltx:ids>
thiscorrespondstotheBibTeXformat
@book{key1,
IDS = {alias1,alias2}
}
D.2.2 Names
Namespecificationsinbiblatexmlaresomewhatmorecomplexinordertogeneralise
thenamehandlingabilitiesofbiblatex. Theuserhastobemoreexplicitaboutthe
namepartsandthisallowsamuchgreatscopeforthehandlingofdifferenttypesof
| namesandnameparts. |               | Anameinbiblatexmlformatlookslikethis |                   |
| ------------------ | ------------- | ------------------------------------ | ----------------- |
| <bltx:names        | type="author" | morenames="1"                        | useprefix="true"> |
| <bltx:name         | gender="sm">  |                                      |                   |
| <bltx:namepart     |               | type="given">                        |                   |
| <bltx:namepart     |               | initial="J">John</bltx:namepart>     |                   |
| <bltx:namepart     |               | initial="A">Arthur</bltx:namepart>   |                   |
</bltx:namepart>
| <bltx:namepart |     | type="family">Smith</bltx:namepart> |                                 |
| -------------- | --- | ----------------------------------- | ------------------------------- |
| <bltx:namepart |     | type="prefix"                       | initial="v">von</bltx:namepart> |
</bltx:name>
| <bltx:name     | useprefix="false"> |               |     |
| -------------- | ------------------ | ------------- | --- |
| <bltx:namepart |                    | type="given"> |     |
<bltx:namepart>Raymond</bltx:namepart>
</bltx:namepart>
| <bltx:namepart |     | type="family">Brown</bltx:namepart> |     |
| -------------- | --- | ----------------------------------- | --- |
</bltx:name>
</bltx:names>
Anamelistfieldiscontainedinthenameselementwiththemandatorytypeattribute
| givingthenameofthenamelist. |     | Thingstonote: |     |
| --------------------------- | --- | ------------- | --- |
341

• TheoptionalmorenamesattributeperformsthesametaskastheBibTeXdata-
sourceformat‘andothers’stringattheendofaname.
• Notethatoptionaluseprefixoptioncanbespecifiedatthelevelofaname
list or an individual name in the name list. This is impossible with BibTeX
datasources.
• Individualnamesmayhaveanoptionalgenderattributewhichmustbeone
ofthosedefinedinthedatamodel‘gender’constantlist. Thisiscurrentlynot
usedbystandardstylesbutisavailableinbiblatexnameformatsifnecessary.
• Anamelistiscomposedofoneormorenameelements.
• Each name is composed of name parts of a type defined by the data model
‘nameparts’constant.
• Eachnamepartmayhaveanoptioninitialattributewhichmakesexplicitthe
initialofthenamepart. Ifthisisnotpresent,biberattemptstoautomatically
determinetheinitialfromthenamepart.
• Namepartsmayhavenamepartssothatcompoundnamescanbehandled.
Ignoringthebiblatexml-onlyfeatures,acorrespondingBibTeXformatdatasource
wouldlooklikethis:
AUTHOR = {von Smith, John Arthur and Brown, Raymond and others}
D.2.3 Lists
Datasource list fields (see § 2.2.1) can be represented in two ways, depending on
whetherthereismorethanoneelementinthelist:
<bltx:publisher>London</bltx:publisher>
<bltx:location>
<bltx:item>London</bltx:item>
<bltx:item>Moscow</bltx:item>
</bltx:location>
D.2.4 Ranges
Datasourcerangefields(see§2.2.1)arerepresentedlikethis:
<bltx:pages>
<bltx:item>
<bltx:start>1</bltx:start>
<bltx:end>10</bltx:end>
</bltx:item>
<bltx:item>
<bltx:start>30</bltx:start>
<bltx:end>34</bltx:end>
</bltx:item>
</bltx:pages>
Arangefieldisalistofranges,eachwithitsownitem. Arangeitemhasastart
elementandanoptionalendelement,sincerangescanbeopen-ended.
342

D.2.5 Dates
Datasourcedatefields(see§2.2.1)canberepresentedintwoways,dependingon
whethertheyconstituteadaterange:
<bltx:date>1985-04-02</bltx:date>
<bltx:date type="event">
<bltx:start>1990-05-16</bltx:start>
<bltx:end>1990-05-17</bltx:end>
</bltx:date>
Thetypeattributeonadateelementcorrespondstoaparticulartypeofdatedefined
inthedatamodel.
D.2.6 RelatedEntries
Relatedentriesarespecifiedasfollows:
<bltx:related>
<bltx:item type="reprint"
ids="rel1,rel2"
string="Somestring"
options="skipbiblist"/>
</bltx:related>
ThiscorrespondstotheBibTeXformat:
@book{key1,
RELATED = {rel2,rel2},
RELATEDTYPE = {reprint},
RELATEDSTRING = {Somestring},
RELATEDOPTIONS = {skipbiblist}
}
Asper§4.5.1,thestringandoptionsattributesareoptional.
E Option Scope
Thefollowingtableprovidesanoverviewofthescopeofvariousoptions.
Per-entry,per-namelistandper-nameoptionsaresetinthedatasource,forexample,
ina.bibfile. Seethebiberdocumentationfordetailsbuthereareafewexamples.
Per-entry:
@BOOK{key,
OPTIONS = {sortingnamekeytemplatename=template1},
}
Per-namelistandper-nameoptionsrequireeitherthebiblatexmldatasourceformat
ortheextendBibTeXnameformatsupportedbybiber(seethebiberdocumentation
fordetails). Per-namelist:
343

@BOOK{key,
AUTHOR = {sortingnamekeytemplatename=template1 and Arthur Smith and
,→
Bill Brown},
}
Per-name:
@BOOK{key,
AUTHOR = {sortingnamekeytemplatename=template1, family=Smith, given=
| ,→ Arthur and Bill | Brown}, |     |     |     |     |
| ------------------ | ------- | --- | --- | --- | --- |
}
| Option | Scope |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Load-time Global Per-refcontext Per-type Per-entry Per-namelist Per-name
| abbreviate      | • • | –   | • • | –   | –   |
| --------------- | --- | --- | --- | --- | --- |
| alldates        | • • | –   | – – | –   | –   |
| alldatesusetime | • • | –   | – – | –   | –   |
|                 | • • | –   | – – | –   | –   |
alltimes
| arxiv     | • • | –   | – – | –   | –   |
| --------- | --- | --- | --- | --- | --- |
| autocite  | • • | –   | – – | –   | –   |
| autopunct | • • | –   | – – | –   | –   |
| autolang  | • • | –   | – – | –   | –   |
|           | • – | –   | – – | –   | –   |
backend
|                 | • • |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
| backref         |     | –   | – – | –   | –   |
| backrefsetstyle | • • | –   | – – | –   | –   |
| backrefstyle    | • • | –   | – – | –   | –   |
| bibencoding     | • • | –   | – – | –   | –   |
| bibstyle        | • – | –   | – – | –   | –   |
|                 | • • | –   | • • | –   | –   |
bibtexcaseprotection
| bibwarn     | • • | –   | – – | –   | –   |
| ----------- | --- | --- | --- | --- | --- |
| block       | • • | –   | – – | –   | –   |
| casechanger | • – | –   | – – | –   | –   |
| citecounter | • • | –   | – – | –   | –   |
|             | • • | –   | – – | –   | –   |
citereset
| citestyle   | • – | –   | – – | –   | –   |
| ----------- | --- | --- | --- | --- | --- |
| citetracker | • • | –   | • • | –   | –   |
| clearlang   | • • | –   | • • | –   | –   |
| datamodel   | • – | –   | – – | –   | –   |
|             | • • | –   | • • | –   | –   |
dataonly
| date           | • • | –   | – – | –   | –   |
| -------------- | --- | --- | --- | --- | --- |
| labeldate      | • • | –   | – – | –   | –   |
| <datetype>date | • • | –   | – – | –   | –   |
| dateabbrev     | • • | –   | • • | –   | –   |
|                | • • | –   | – – | –   | –   |
datecirca
|               | • • |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
| dateera       |     | –   | – – | –   | –   |
| dateerauto    | • • | –   | – – | –   | –   |
| dateuncertain | • • | –   | – – | –   | –   |
| datezeros     | • • | –   | – – | –   | –   |
|               | • • | –   | – – | –   | –   |
defernumbers
|     | • • | –   | • • | –   | –   |
| --- | --- | --- | --- | --- | --- |
doi
| eprint          | • • | –   | • • | –   | –   |
| --------------- | --- | --- | --- | --- | --- |
| <namepart>inits | • • | –   | • • | •   | •   |
| gregorianstart  | • • | –   | – – | –   | –   |
| hyperref        | • • | –   | – – | –   | –   |
|                 | • • | –   | • • | –   | –   |
ibidtracker
| idemtracker | • • | –   | • • | –   | –   |
| ----------- | --- | --- | --- | --- | --- |
| indexing    | • • | –   | • • | –   | –   |
344

| Option | Scope |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Load-time Global Per-refcontext Per-type Per-entry Per-namelist Per-name
| isbn   | • • | –   | • • | –   | –   |
| ------ | --- | --- | --- | --- | --- |
| julian | • • | –   | – – | –   | –   |
|        | • • | –   | • • | –   | –   |
labelalpha
| labelalphanametemplatename | – – | •   | – • | •   | •   |
| -------------------------- | --- | --- | --- | --- | --- |
| labelnamefield             | – – | –   | – • | –   | –   |
| labelnumber                | • • | –   | • • | –   | –   |
| labeltitle                 | • • | –   | • • | –   | –   |
|                            | – – | –   | – • | –   | –   |
labeltitlefield
| labeltitleyear   | • • | –   | • • | –   | –   |
| ---------------- | --- | --- | --- | --- | --- |
| labeldateparts   | • • | –   | • • | –   | –   |
| labeltime        | • • | –   | – – | –   | –   |
| labeldateusetime | • • | –   | – – | –   | –   |
|                  | – – | •   | – – | –   | –   |
labelprefix
<datetype>time
|                       | • • | –   | – – | –   | –   |
| --------------------- | --- | --- | --- | --- | --- |
| <datetype>dateusetime | • • | –   | – – | –   | –   |
| language              | • • | –   | – – | –   | –   |
| loadfiles             | • • | –   | – – | –   | –   |
|                       | • • | –   | • • | –   | –   |
loccittracker
|               | • • |     | • • |     |     |
| ------------- | --- | --- | --- | --- | --- |
| maxalphanames |     | –   |     | –   | –   |
| maxbibnames   | • • | –   | • • | –   | –   |
| maxcitenames  | • • | –   | • • | –   | –   |
| maxsortnames  | • • | –   | • • | –   | –   |
|               | • • | –   | • • | –   | –   |
maxitems
|     | • • | –   | • • | –   | –   |
| --- | --- | --- | --- | --- | --- |
maxnames
| maxparens     | • • | –   | – – | –   | –   |
| ------------- | --- | --- | --- | --- | --- |
| mcite         | • – | –   | – – | –   | –   |
| minalphanames | • • | –   | • • | –   | –   |
| minbibnames   | • • | –   | • • | –   | –   |
|               | • • | –   | • • | –   | –   |
mincitenames
| minsortnames | • • | –   | • • | –   | –   |
| ------------ | --- | --- | --- | --- | --- |
| mincrossrefs | • • | –   | – – | –   | –   |
| minxrefs     | • • | –   | – – | –   | –   |
| minitems     | • • | –   | • • | –   | –   |
|              | • • | –   | • • | –   | –   |
minnames
| namehashtemplatename | – – | •   | – • | •   | •   |
| -------------------- | --- | --- | --- | --- | --- |
| nametemplates        | – – | •   | – • | •   | •   |
| natbib               | • – | –   | – – | –   | –   |
| nohashothers         | • • | –   | • • | •   | –   |
|                      | • • | –   | • • | •   | –   |
nosortothers
| noinherit    | – – | –   | – • | –   | –   |
| ------------ | --- | --- | --- | --- | --- |
| notetype     | • • | –   | – – | –   | –   |
| opcittracker | • • | –   | • • | –   | –   |
| openbib      | • • | –   | – – | –   | –   |
|              | • • | –   | – – | –   | –   |
pagetracker
|              | • • |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
| parentracker |     | –   | – – | –   | –   |
| punctfont    | • • | –   | – – | –   | –   |
| refsection   | • • | –   | – – | –   | –   |
| refsegment   | • • | –   | – – | –   | –   |
| related      | • • | –   | • • | –   | –   |
|              | • • | –   | – – | –   | –   |
safeinputenc
| seconds     | • • | –   | – – | –   | –   |
| ----------- | --- | --- | --- | --- | --- |
| singletitle | • • | –   | • • | –   | –   |
| skipbib     | • • | –   | • • | –   | –   |
| skipbiblist | • • | –   | • • | –   | –   |
|             | • • | –   | • • | –   | –   |
skiplab
| sortcase                   | • • | –   | – – | –   | –   |
| -------------------------- | --- | --- | --- | --- | --- |
| sortcites                  | • • | –   | – – | –   | –   |
| sorting                    | • • | –   | – – | –   | –   |
| sortingnamekeytemplatename | – – | •   | – • | •   | •   |
|                            | • • | –   | – – | –   | –   |
sortlocale
345

| Option | Scope |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Load-time Global Per-refcontext Per-type Per-entry Per-namelist Per-name
| sortlos   | • • | –   | – – | –   | –   |
| --------- | --- | --- | --- | --- | --- |
| sortupper | • • | –   | – – | –   | –   |
|           | • – | –   | – – | –   | –   |
style
| terseinits  | • • | –   | • • | •   | •   |
| ----------- | --- | --- | --- | --- | --- |
| texencoding | • • | –   | – – | –   | –   |
| timezeros   | • • | –   | – – | –   | –   |
| timezones   | • • | –   | – – | –   | –   |
|             | • • | –   | • • | •   | –   |
uniquelist
| uniquename             | • • | –   | • • | •   | •   |
| ---------------------- | --- | --- | --- | --- | --- |
| uniquenametemplatename | – – | •   | – • | •   | •   |
| uniquetitle            | • • | –   | • • | –   | –   |
| uniquebaretitle        | • • | –   | • • | –   | –   |
|                        | • • | –   | • • | –   | –   |
uniquework
| uniqueprimaryauthor | • • | –   | • • | –   | –   |
| ------------------- | --- | --- | --- | --- | --- |
| url                 | • • | –   | • • | –   | –   |
| useprefix           | • • | –   | • • | •   | •   |
| use<name>           | • • | –   | • • | –   | –   |
F Revision History
Thisrevisionhistoryisalistofchangesrelevanttousersofthispackage. Changes
ofamoretechnicalnaturewhichdonotaffecttheuserinterfaceorthebehaviorof
thepackagearenotincludedinthelist. Moretechnicaldetailsaretobefoundin
theCHANGES.mdfile. Thenumbersontherightindicatetherelevantsectionofthis
manual.
3.21 2025-07-10
Added\mkseqrangeand\mkseqrange*toformatpagesincitationsusingthe
bibliographystringssequensandsequentesifapplicable . . . . . . . 4.6.4
Addedoptioncitepagerangetocustomizetheformatofpageranges . . 3.1.2.1
Added\mkautorangeand\mkautorange*whichforwardsto\mknormrange,
\mkcomprangeor\mkseqrange(ortheirstarredcounterpart,respectively)
dependingonthecitepagerangevalue . . . . . . . . . . . . . . . . . 4.6.4
Use\mkautorangeinstandardstyles.
Fix\DeclareHyphenationExceptionswithpolyglossiaandlanguagevariants.
3.20 2024-03-22
Addednewuniquenameoptions . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.3
Addeddefaultfulldatesortingtemplates . . . . . . . . . . . . . . . . . . 3.1.2
Addedbibdatendsep . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.3
Added\AtFollowingRefsections . . . . . . . . . . . . . . . . . . . . . . 4.10.6
Added\DeclareNamehashTemplate . . . . . . . . . . . . . . . . . . . . . . 4.11.5
Addedfullhashraw . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.1
AugmentedExtendedNameFormattoenableoverrideofnamehashes . . 3.4
3.19 2023-03-05
Added\AtNextRefsection . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
346

Added\DeclareExtradateContextoption. . . . . . . . . . . . . . . . . . 4.5.11
Modifiedwarningforusingbibtexbackend
Enhancedextradatetrackingtofallbackonlabeltitlewhenthereisnoauthor
3.18b 2022-07-12
Reenable\MakeUppercase/\MakeLowercase‘patches’basedon\CaseSwitch
3.18a 2022-07-02
Disable\MakeUppercase/\MakeLowercasepatchesasemergencyfixforLaTeX
2022-06-01-PL4compatibility.
3.18 2022-06-22
Addedsortingoption\intciteorder . . . . . . . . . . . . . . . . . . . . 4.5.6
Addedglobaloptionpluralothers . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Added\localrefcontext . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.8.10
Added\visibilityoptionto\DeclareSortingNamekeyTemplate . . . . 4.5.6
Added\GenRefcontextData . . . . . . . . . . . . . . . . . . . . . . . . . . 3.8.10
Added\AtBeginRefsection . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
3.17 2022-01-25
Changedbehaviourofindex-lessgranularXDATAreferences . . . . . . . 3.14.6
Added\DeclareNonamestring . . . . . . . . . . . . . . . . . . . . . . . . 4.5.10
Addednew\citecountsortoptionandassociateddefaultsortingscheme 4.5.6
and . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addednewsourcemapverbsmatchesandmatchesi . . . . . . . . . . . . 4.5.3
Deprecatedseasonfieldsandmacrosinfavourofgeneralisedyeardivisions4.2.4.3
Added\textouterlang . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.8
Added\UndeclareDelimcontextAlias . . . . . . . . . . . . . . . . . . . . 3.12.2
Added\DeclareBibstringSet,\DeclareBibstringSetFormatetc. . . . . 4.8
AddedMarathilocalisation( )
�नरंजन
AddedRomanianlocalisation(PatrickDanilevici)
Addedsomesupportforcalculatingwithnon-us-asciinumerals . . . . . 4.6.2
Removedlistsupportforhnameiargumentof\DeclareDelimFormat . . . 3.12.2
3.16 2020-12-31
Addednamedrefcontextsupportto\assignrefcontext* . . . . . . . . . 3.8.10
Fixedinfiniteloopwithvolcitepagesfieldformat
AddedExtendedNameFormatdocumentation . . . . . . . . . . . . . . . 3.4
Addedlabeloptionto\printbibliography . . . . . . . . . . . . . . . . 3.8.2
Deprecate\mainlanginfavourof\textmainlang . . . . . . . . . . . . . 4.8
AddedBasquelocalisation(AnderZarketa-Astigarraga)
3.15a 2020-08-23
Fixedbugwithlongargumentsin\DeclareFieldFormatandfriends
347

3.15 2020-08-16
Addedstarnocitedoptiontosourcemaps . . . . . . . . . . . . . . . . . . 4.5.3
Addedthegloboptionto\addbibresource . . . . . . . . . . . . . . . . . 3.8.1
Addedeidtomoreentrytypes . . . . . . . . . . . . . . . . . . . . . . . . 2.1.1
Added\bibeidpunct . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.1
Addedissuetitleaddonandjournaltitleaddon . . . . . . . . . . . . . 2.2.2
numeric-compcompressessubentrysetreferencesnow . . . . . . . . . . 3.1.2.2
Addedsubentrycomptonumeric-compstyle . . . . . . . . . . . . . . . . . 3.1.2.2
Added\multiciterangedelim,\multicitesubentrydelim,
\multicitesubentryrangedelim,\superciterangedelim,
\supercitesubentrydelim,\supercitesubentryrangedelim . . . . . 3.12.1
Implementedexpl3casechangingfunctions . . . . . . . . . . . . . . . . 4.6.4
Addedcasechangeroption . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1
Addedbibtexcaseprotectionoption . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Added\mautociteand\Mautocite . . . . . . . . . . . . . . . . . . . . . 3.9.10
Addedtrackfloatsandbackreffloats . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addedblockoptionto\printbibliographyandfriends . . . . . . . . . . 3.8.2
Added\NumsCheckSetupand\PagesCheckSetup . . . . . . . . . . . . . . 4.6.4
Added\AtEveryEntrykey . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
Added\ifdatesequaland\ifdaterangesequal . . . . . . . . . . . . . . 4.6.2
Clarified\ifuniqueprimaryauthorsemantics . . . . . . . . . . . . . . . . 4.6.2
Added\bibncpstring,\bibncplstringand\bibncpsstring . . . . . . . 4.8
AddedLithuanianlocalisation(ValdemarasKlumbys)
AddedSerbianlocalisation(AndrejRadović)
AddedTurkishlocalisation(AbdulkerimGok)
Addedfilehooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.7
Deprecated\ifkomabibtotocand\ifkomabibtotocnumbered . . . . . . . 3.15.1
3.14 2019-12-01
Addednewmappingverbsforcitationsources . . . . . . . . . . . . . . . 4.5.3
Addeddocumentationfornewbibergranular@xdatafunctionality . . . 3.14.6
Enhancedpolyglossiasupport
3.13a 2019-08-31
Bugfixrelease
3.13 2019-08-17
Addednew@datasetentrytype . . . . . . . . . . . . . . . . . . . . . . . 2.1.1
Promoted@softwaretoregularentrytype. . . . . . . . . . . . . . . . . . 2.1.1
Addedentrykeyaliasforentrykeysinlabels . . . . . . . . . . . . . . . . 4.5.5
Addedappendstrictsourcemappingoption . . . . . . . . . . . . . . . . 4.5.3
348

Addednohashothersandnosortothers . . . . . . . . . . . . . . . . . . . 3.1.2.3
Enhanced\addbibresourcewithglobbing . . . . . . . . . . . . . . . . . 3.8.1
Added\DeclareBiblatexOption . . . . . . . . . . . . . . . . . . . . . . . 4.2.1
Expandedscopepossibilitiesforseveraloptions . . . . . . . . . . . . . . . E
Added\ifvolcitetest . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Addedspecialfieldsvolcitevolumeandvolcitepages. . . . . . . . . . . 4.3.2
Added\AtVolcitehook . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
Added\pnfmt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.9.8
Added\mkbibcompletenameand\mkbibcompletename‘formatorder’ . . 3.12.1
Made\postnotedelimandfriendscontextsensitive . . . . . . . . . . . . 3.12.1
Added\multipostnotedelimand\multiprenotedelim . . . . . . . . . . 3.12.1
Added\thefirstlistitemandfriends . . . . . . . . . . . . . . . . . . . 4.6.1
Addedhitempostproiargumentto\mkcomprange,\mknormrangeand\mkfirstpage
4.6.4
Added\biburlbigskipandfriends . . . . . . . . . . . . . . . . . . . . . 3.12.4
Addedbiburlbigbreakpenaltyandbiburlbreakpenaltyandfriends . . 3.12.4
Added\DeclarePrintbibliographyDefaults . . . . . . . . . . . . . . . . 3.8.2
Addeddoito@online . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1.1
3.12 2018-10-30
Addedliteralandnamedannotationfunctionality . . . . . . . . . . . . . 3.7
Added\ifnocite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Addedcase-insensitiveversionsofmatchingoperators . . . . . . . . . . . 4.5.3
Addedlangidsoptionalargumentto\DeclareSortTranslit . . . . . . . 4.5.6
Addednoromanoption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.3
Changedsortyeartoanintegerfield . . . . . . . . . . . . . . . . . . . . 2.2.3
Addedextraname . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.2
Addedbibencodingoptionto\addbibresource . . . . . . . . . . . . . . 3.8.1
Changedtypeofnumberfromintegertoliteral . . . . . . . . . . . . . . . 2.2.2
Removednoerroretextoolsoption . . . . . . . . . . . . . . . . . . . . . 1.5.5
Addedmaxsortnamesandminsortnames . . . . . . . . . . . . . . . . . . . 3.1.2.1
Added\DeprecateFieldFormatWithReplacementandfriends . . . . . . . 4.4.2
Addedlistandnamewrappers . . . . . . . . . . . . . . . . . . . . . . . . 4.4.2
Added\ifdateyearsequal . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Added‘andhigher’sectioningvaluesforcitereset,refsectionandrefsegment
options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
AddedHungarianlocalisation . . . . . . . . . . . . . . . . . . . . . . . . . 3.13.4
Added\DeclareCitePunctuationPosition . . . . . . . . . . . . . . . . . 4.3.1
349

3.11 2018-02-20
Addedentrynociteoptiontosourcemapping . . . . . . . . . . . . . . . . 4.5.3
Addeddriverandbiblistfilteroptionsto\printbiblist . . . . . . . 3.8.3
Added\mknormrange . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.4
Added\ifdateannotation . . . . . . . . . . . . . . . . . . . . . . . . . . 3.7
Extended\iffieldannotationandfriends . . . . . . . . . . . . . . . . . 3.7
Changed\DeclareSourcemapsothatitcanbeusedmultipletimes . . . . 4.5.3
AddedLatvianlocalisation(RihardsSkuja)
Addedlocallabelwidthoption. . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
3.10 2017-12-19
Changededtftoiso . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addednoerroretextoolsoption . . . . . . . . . . . . . . . . . . . . . . . 1.5.5
3.9 2017-11-21
Added\iffieldplusstringbibstring . . . . . . . . . . . . . . . . . . . . 4.6.2
Fixed\mkpagetotal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.4
3.8 2017-11-04
Addedhyperref=manualoption. . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addedfieldextradatescope . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.2
Added\DeclareExtradate . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.11
Added\DeprecateFieldWithReplacement,\DeprecateListWithReplacementand
\DeprecateNameWithReplacement . . . . . . . . . . . . . . . . . . . . 4.4.1
Added\letbibmacro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.4
Renamedextrayeartoextradate . . . . . . . . . . . . . . . . . . . . . . 4.2.4.2
Addedsortsetsglobaloption . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Added\iflabelalphanametemplatenameand\uniquenametemplatename 4.6.2
Renamed\ifsortingnameschemeto\ifsortingnamekeytemplatename . 4.6.2
Renamedsortingnamekeyschemetosortingnamekeytemplate . . . . . . 3.8.10
Renamed\DeclareSortingNamekeySchemeto\DeclareSortingNamekeyTemplate
4.5.6
Renamed\DeclareSortingSchemeto\DeclareSortingTemplate . . . . . 4.5.6
Changesto\DeclareUniquenameTemplateand\DeclareLabelalphaNameTemplate
scopes . . . . . . . . . . . . . . 4.11.4 and . . . . . . . . . . . . . . 4.5.5
Addednewdisambiguationoptionto\DeclareUniquenameTemplate . . 4.11.4
Addednewuser-facingversionsofsomeentry-queryingcommands . . . 3.11
Changedoriglanguagetoalistinlinewithlanguage . . . . . . . . . . . 2.2.2
Deprecatedchildentrykeyandchildentrytype . . . . . . . . . . . . . . 4.2.4.1
Addedbibnamehashandnamelistspecificvariants . . . . . . . . . . . . . 4.2.4.1
AddedALA-LCRussianromanisationtransliterationsupport . . . . . . . 4.5.6
Addedurlraw . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.1
350

Added\AtUsedriver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
AddedBulgarianlocalisation(KaloyanGanev)
sortyearisnowaliteral,notaninteger . . . . . . . . . . . . . . . . . . . 2.2.3
Added\DeclareLanguageMappingSuffix . . . . . . . . . . . . . . . . . . 4.9.1
Changeddefaultfor\DeclarePrefChars . . . . . . . . . . . . . . . . . . . 4.7.5
Added\authortypedelim,\editortypedelimand\translatortypedelim 3.12.1
Added\DeclareDelimAlias . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.2
AddedslovenianasaliasforsloveneduetoPolyglossianameforthelanguage
2.2.3
AddedUkrainianlocalisation(SergiyM.Ponomarenko)
3.7 2016-12-08
Correcteddefaultfor\bibdateeraprefix . . . . . . . . . . . . . . . . . . 4.10.2
Added\DeclareSortInclusion . . . . . . . . . . . . . . . . . . . . . . . . 4.5.6
Added\relateddelim<relatedtype> . . . . . . . . . . . . . . . . . . . 3.12.1
3.6 2016-09-15
Correctedsomedocumentationandfixedabugwithlabeldatelocalisationstrings.
3.5 2016-09-10
Added\ifuniquebaretitletest . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Documented\labelnamesourceand\labeltitlesource . . . . . . . . . 4.2.4.1
Added\bibdaterangesep . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.3
Addedrefsectionoptionto\DeclareSourcemap . . . . . . . . . . . . . . 4.5.3
Addedsuppressoptiontoinheritancespecifications . . . . . . . . . . . . 4.5.12
Added\ifuniquework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Changed\DeclareStyleSourcemapsothatitcanbeusedmultipletimes . 4.5.3
Added\forcezerosyand\forcezerosmdt . . . . . . . . . . . . . . . . . 4.10.4
Changed\mkdatezerosto\mkyearzeros,\mkmonthszerosand\mkdayzeros
4.10.4
Addednamehashandfullhashforallnamelistfields. . . . . . . . . . . . 4.2.4.1
Generalisedgiveninitsoptiontoallnameparts . . . . . . . . . . . . . . 3.1.2.3
Addedinitsoptionto\DeclareSortingNamekeyScheme . . . . . . . . . . 4.5.6
Removedoptionsortgiveninits. Usetheoptioninitsto
\DeclareSortingNamekeySchemeinstead
Added\DeclareLabelalphaNameTemplate . . . . . . . . . . . . . . . . . . 4.5.5
AddedfulledtfLevels0and1complianceforparsingandprintingtimes 2.3.8
ChangeddatestobefullyedtfLevels0and1compliant. Associatedtestsand
localisationstrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.8
Addedtimezeros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addedmktimezeros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.4
Changediso8601toedtf . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
351

Added\DeclareUniquenameTemplate . . . . . . . . . . . . . . . . . . . . 4.11.4
RemovedexperimentalRISsupport
sortnamekeyschemeanduseprefixcanbenowbesetper-namelistandper-name
forBibTeXdatasources . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.6
Added\DeclareDelimcontextAlias . . . . . . . . . . . . . . . . . . . . . 3.12.2
AddedEstonianlocalisation(BensonMuite)
Referencecontextsmaynowbenamed . . . . . . . . . . . . . . . . . . . 3.8.10
AddednotfieldstepinSourcemaps . . . . . . . . . . . . . . . . . . . . . 4.5.3
3.4 2016-05-10
Added\ifcrossrefsourceand\ifxrefsource . . . . . . . . . . . . . . . 4.6.2
Addeddataannotationfeature . . . . . . . . . . . . . . . . . . . . . . . . 3.7
Addedpackageoptionminxrefs . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Added\ifuniqueprimaryauthorandassociatedglobaloption . . . . . . 4.6.2
Added\DeprecateField,\DeprecateListand\DeprecateName . . . . . 4.4.1
Added\ifcaselang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Added\DeclareSortTranslit . . . . . . . . . . . . . . . . . . . . . . . . 4.5.6
Addeduniquetitletest . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
Added\namelabeldelim . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.1
Newstarredvariantsofthe\assignrefcontext*macros . . . . . . . . . 3.8.10
Newcontext-sensitivedelimiterinterface . . . . . . . . . . . . . . . . . . 3.12.2
Movedprefixnumbersoptionto\newrefcontextandrenamedtolabelprefix
3.8.10
Added\DeclareDatafieldSet . . . . . . . . . . . . . . . . . . . . . . . . 4.5.2
3.3 2016-03-01
Newmacrosforauto-assignmentofrefcontexts . . . . . . . . . . . . . . . 3.8.10
Schemadocumentationforbiblatexml . . . . . . . . . . . . . . . . . . . D
Sourcemappingdocumentationandexamplesforbiblatexml . . . . . . 4.5.3
Changesfornameformatstogeneraliseavailablenameparts . . . . . . . 4.4.2
useprefixcannowbespecifiedper-namelistandper-nameinbiblatexml
datasources
Newsourcemappingoptionsforcreatingnewentriesdynamicallyandloopingover
mapsteps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.3
Addednoalphaothersandenhancednamerangeselectionin
\DeclareLabelalphaTemplate . . . . . . . . . . . . . . . . . . . . . . 4.5.5
Added\DeclareDatamodelConstant . . . . . . . . . . . . . . . . . . . . . 4.5.4
Renamedfirstinitstogiveninitsandsortfirstinitstosortgiveninits
3.1.2.3
Added\DeclareSortingNamekeyScheme . . . . . . . . . . . . . . . . . . . 4.5.6
Removedmessyexperimentalendnoteandzoterordfsupportforbiber
Added\nonameyeardelim . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.1
Added\extpostnotedelim . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.1
352

3.2 2015-12-28
Addedpstrwidthandpcompoundto\DeclareLabelalphaTemplate . . . . 4.5.5
Added\AtEachCitekey . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
3.1 2015-09
Added\DeclareNolabel . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.5
Added\DeclareNolabelwidthcount . . . . . . . . . . . . . . . . . . . . . 4.5.5
3.0 2015-04-20
ImprovedDanish(JonasNyrup)andSpanish(ludenticus)translations
labelnameandlabeltitlearenowresolvedbybiblatexinsteadofbiberfor
moreflexibilityandfutureextensibility
New\entryclonesourcemapverbforcloningentriesduringsourcemapping4.5.3
New\pernottypenegatedper-typesourcemapverb . . . . . . . . . . . . 4.5.3
Newrangecalculationcommand\frangelen . . . . . . . . . . . . . . . . 4.6.4
Newbibliographycontextfunctionality . . . . . . . . . . . . . . . . . . . 3.8.10
Namelistsinthedatamodelnowautomaticallycreateinternalsfor\ifuse<name>
testsandbooleans . . . . . . . . . . . 3.1.3.1 and . . . . . . . . . . 4.6.2
2.9a 2014-06-25
resetnumbersnowallowspassinganumbertoresetto . . . . . . . . . . 3.8.2
2.9 2014-02-25
Generalisedshorthandsfacility . . . . . . . . . . . . . . . . . . . . . . . . 3.8.3
Sortinglocalescannowbedefinedaspartofasortingscheme . . . . . . 4.5.6
Addedsortinithash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.1
AddedSlovenelocalisation(TeaTušarandBogdanFilipič)
Added\mkbibitalic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.4
Recommendbegentryandfinentrybibliographymacros . . . . . . . . . 4.2.3
2.8a 2013-11-25
Splitoptionlanguage=autointolanguage=autociteandlanguage=autobib
3.1.2.1
2.8 2013-10-21
Newlangidopts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.3
hyphenationfieldrenamedtolangid . . . . . . . . . . . . . . . . . . . . 2.2.3
polyglossiasupport
Renamedbabeloptiontoautolang . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
CorrectedDutchlocalisation
Addeddatelabel=yearoption . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.1
Addeddatelabelsourcefield . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.1
353

2.7a 2013-07-14
Bugfix-respectmaxnamesanduniquelistin\finalandsemicolon
CorrectedFrenchlocalisation
2.7 2013-07-07
Addedfieldeventtitleaddontodefaultdatamodelandstyles . . . . . . . 2.2.2
Added\ifentryinbib,\iffirstcitekeyand\iflastcitekey . . . . . . 4.6.2
Addedpostpunctspecialfield,documentedmultiprenoteandmultipostnote
specialfields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2
Added\UseBibitemHook,\AtEveryMultiCite,\AtNextMultiCite,
\UseEveryCiteHook,\UseEveryCitekeyHook,\UseEveryMultiCiteHook,
\UseNextCiteHook,\UseNextCitekeyHook,\UseNextMultiCiteHook,
\DeferNextCitekeyHook . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
Fixed\textciteandrelatedcommandsinthenumericandverbosestyles 3.9.2
Addedmulticitevariantsof\volciteandrelatedcommands . . . . . . . 3.9.6
Added\finalandsemicolon . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.3
Addedcitationdelimiter\textcitedelimfor\textciteandrelatedcommandsto
styles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.1
UpdatedRussianlocalisation(OlegDomanov)
FixedBrazilianandFinnishlocalisation
2.6 2013-04-30
Added\printunit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.7.1
Addedfieldclonesourcekey . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4.1
Newoptionsfor\DeclareLabelalphaTemplate . . . . . . . . . . . . . . . 4.5.5
Added\DeclareLabeldateandretired\DeclareLabelyear . . . . . . . . 4.5.11
Addednodatelocalisationstring . . . . . . . . . . . . . . . . . . . . . . . 4.9.2.14
Added\rangelen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.4
Addedstarredvariantsof\citeauthorand\Citeauthor . . . . . . . . . 3.9.5
Restoredoriginalurlformat. Addedurlfromlocalisationkey . . . . . . . 4.9.2.15
Added\AtNextBibliography . . . . . . . . . . . . . . . . . . . . . . . . . 4.10.6
Fixedrelatedentryprocessingtoallownestedandcyclicrelatedentries
AddedCroatianlocalisation(IvoPletikosić)
AddedPolishlocalisation(AnastasiaKandulina,YuriyChernyshov)
FixedCatalanlocalisation
Addedsmart“of”fortitlestoCatalanandFrenchlocalisation
Miscbugfixes
2.5 2013-01-10
Madeurlworkasalocalisationstring,defaultingtopreviouslyhard-codedvalue
‘URL’.
Changedsomebiberoptionnamestocoherewithbiber1.5.
354

Newsourcemapstepforconditionallyremovingentireentries . . . . . . 4.5.3
UpdatedCatalanlocalisation(SebastiàVila-Marta)
2.4 2012-11-28
Addedrelatedoptionsfield . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.1
Added\DeclareStyleSourcemap . . . . . . . . . . . . . . . . . . . . . . . 4.5.3
Renamed\DeclareDefaultSourcemapto\DeclareDriverSourcemap . . . 4.5.3
Documented\DeclareFieldInputHandler,\DeclareListInputHandlerand
\DeclareNameInputHandler.
AddedCzechlocalisation(MichalHoftich)
UpdatedCatalanlocalisation(SebastiàVila-Marta)
2.3 2012-11-01
BetterdetectionofsituationswhichrequireabiberorLATEXre-run
Newappendmodefor\DeclareSourcemapsothatfieldscanbecombined 4.5.3
Extendedauxiliaryindexingmacros
Addedsupportforplurallocalisationstringswithrelatedtype . . . . . . 4.5.1
Added\csfieldand\usefield . . . . . . . . . . . . . . . . . . . . . . . 4.6.1
Addedstarredvariantof\usebibmacro . . . . . . . . . . . . . . . . . . . 4.6.4
Added\ifbibmacroundef,\iffieldformatundef,\iflistformatundefand
\ifnameformatundef . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.4
AddedCatalanlocalisation(SebastiàVila-Marta)
Miscbugfixes
2.2 2012-08-17
Miscbugfixes
Added\revsdnamepunct . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.12.1
Added\ifterseinits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2
2.1 2012-08-01
Miscbugfixes
UpdatedNorwegianlocalisation(HåkonMalmedal)
Increaseddatamodelauto-loadingpossibilities . . . . . . . . . . . . . . . 4.5.4
2.0 2012-07-01
Miscbugfixes
Generalisedsingletitletestalittle . . . . . . . . . . . . . . . . . . . . . 4.6.2
Addednewspecialfieldextratitleyear . . . . . . . . . . . . . . . . . . 4.2.4
Customisabledatamodel . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.4
Added\DeclareDefaultSourcemap . . . . . . . . . . . . . . . . . . . . . . 4.5.3
Addedlabeltitleoption . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.3
Addednewspecialfieldextratitle . . . . . . . . . . . . . . . . . . . . . 4.2.4
Madespecialfieldlabeltitlecustomisable . . . . . . . . . . . . . . . . . 4.2.4
355

Removedfieldreprinttitle . . . . . . . . . . . . . . . . . . . . . . . . . 3.5
Addedrelatedentryfeature . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5
Added\DeclareNoinit . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.8
Added\DeclareNosort . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.9
Addedsortingoptionfor\printbibliographyand\printshorthands . 3.8.2
Addedidsfieldforcitekeyaliasing . . . . . . . . . . . . . . . . . . . . . . 2.2
Addedsortfirstinitsoption . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2.3
Addeddatastreammodificationfeature . . . . . . . . . . . . . . . . . . . 4.5.3
Addedcustomisablelabelsfeature . . . . . . . . . . . . . . . . . . . . . . 4.5.5
Added\citeyear*and\citedate* . . . . . . . . . . . . . . . . . . . . . 3.9.5
356