**Note** : You are viewing the development version of [Schema.org](https://schema.org). See [how we work](https://schema.org/docs/howwework.html) for more details. 
[Schema.org](https://schema.org/)
  * [Docs](https://schema.org/docs/documents.html)
  * [Schemas](https://schema.org/docs/schemas.html)
  * [Validate](https://validator.schema.org)
  * [About](https://schema.org/docs/about.html)


[ ](javascript:void\(0\);)
# ScholarlyArticle
A Schema.org Type
Usage: [ 10K - 100K Domains Based on monthly aggregations from Google's web index. ](https://schema.org/docs/usage_stats.html) (Google - May 2026) 
[Thing](https://schema.org/Thing "Thing") > [CreativeWork](https://schema.org/CreativeWork "CreativeWork") > [Article](https://schema.org/Article "Article") > [ScholarlyArticle](https://schema.org/ScholarlyArticle "ScholarlyArticle")   

**[more...]**
  * Canonical URL: https://schema.org/ScholarlyArticle
  * [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ScholarlyArticle)


A scholarly article.  
| Property  | Expected Type  | Description  |  
| --- | --- | --- |  
| Properties from [Article](https://schema.org/Article "Article")  |  
| `               articleBody[](https://schema.org/articleBody "articleBody")`  |  [Text](https://schema.org/Text "Text")  | The actual body of the article.   |  
| `               articleSection[](https://schema.org/articleSection "articleSection")`  |  [Text](https://schema.org/Text "Text")  | Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.   |  
| `               backstory[](https://schema.org/backstory "backstory")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Text](https://schema.org/Text "Text")  | For an [Article](https://schema.org/Article), typically a [NewsArticle](https://schema.org/NewsArticle), the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.   |  
| `               pageEnd[](https://schema.org/pageEnd "pageEnd")`  |  [Integer](https://schema.org/Integer "Integer") or   
[Text](https://schema.org/Text "Text")  | The page on which the work ends; for example "138" or "xvi".   |  
| `               pageStart[](https://schema.org/pageStart "pageStart")`  |  [Integer](https://schema.org/Integer "Integer") or   
[Text](https://schema.org/Text "Text")  | The page on which the work starts; for example "135" or "xiii".   |  
| `               pagination[](https://schema.org/pagination "pagination")`  |  [Text](https://schema.org/Text "Text")  | Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".   |  
| `               speakable[](https://schema.org/speakable "speakable")`  |  [SpeakableSpecification](https://schema.org/SpeakableSpecification "SpeakableSpecification") or   
[URL](https://schema.org/URL "URL")  | Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.  
  
The _speakable_ property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:  
  
1.) _id-value_ URL references - uses _id-value_ of an element in the page being annotated. The simplest use of _speakable_ has (potentially relative) URL values, referencing identified sections of the document concerned.  
  
2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [cssSelector](https://schema.org/cssSelector) property.  
  
3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [xpath](https://schema.org/xpath) property.  
  
For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type, [SpeakableSpecification](https://schema.org/SpeakableSpecification) which is defined to be a possible value of the _speakable_ property.   |  
| `               wordCount[](https://schema.org/wordCount "wordCount")`  |  [Integer](https://schema.org/Integer "Integer")  | The number of words in the text of the CreativeWork such as an Article, Book, etc.   |  
| Properties from [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  |  
| `               about[](https://schema.org/about "about")`  |  [Thing](https://schema.org/Thing "Thing")  | The subject matter of an object.   
Inverse property: [subjectOf](https://schema.org/subjectOf "subjectOf")  |  
| `               abstract[](https://schema.org/abstract "abstract")`  |  [Text](https://schema.org/Text "Text")  | An abstract is a short description that summarizes a [CreativeWork](https://schema.org/CreativeWork).   |  
| `               accessMode[](https://schema.org/accessMode "accessMode")`  |  [Text](https://schema.org/Text "Text")  | The human sensory perceptual system or cognitive faculty through which a person may process or perceive the intellectual content of a resource, not including any adaptations of the content (e.g., text alternatives for images). Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).   |  
| `               accessModeSufficient[](https://schema.org/accessModeSufficient "accessModeSufficient")`  |  [ItemList](https://schema.org/ItemList "ItemList")  | A list of single or combined access modes that are sufficient to understand all the intellectual content of a resource, including any adaptations. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).   |  
| `               accessibilityAPI[](https://schema.org/accessibilityAPI "accessibilityAPI")`  |  [Text](https://schema.org/Text "Text")  | Indicates that the resource is compatible with the referenced accessibility API. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).   |  
| `               accessibilityControl[](https://schema.org/accessibilityControl "accessibilityControl")`  |  [Text](https://schema.org/Text "Text")  | Identifies input methods that are sufficient to fully control the described resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).   |  
| `               accessibilityFeature[](https://schema.org/accessibilityFeature "accessibilityFeature")`  |  [Text](https://schema.org/Text "Text")  | Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).   |  
| `               accessibilityHazard[](https://schema.org/accessibilityHazard "accessibilityHazard")`  |  [Text](https://schema.org/Text "Text")  | A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).   |  
| `               accessibilitySummary[](https://schema.org/accessibilitySummary "accessibilitySummary")`  |  [Text](https://schema.org/Text "Text")  | A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed".   |  
| `               accountablePerson[](https://schema.org/accountablePerson "accountablePerson")`  |  [Person](https://schema.org/Person "Person")  | Specifies the Person that is legally accountable for the CreativeWork.   |  
| `               acquireLicensePage[](https://schema.org/acquireLicensePage "acquireLicensePage")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item.   |  
| `               aggregateRating[](https://schema.org/aggregateRating "aggregateRating")`  |  [AggregateRating](https://schema.org/AggregateRating "AggregateRating")  | The overall rating, based on a collection of reviews or ratings, of the item.   |  
| `               alternativeHeadline[](https://schema.org/alternativeHeadline "alternativeHeadline")`  |  [Text](https://schema.org/Text "Text")  | A secondary title of the CreativeWork.   |  
| `               archivedAt[](https://schema.org/archivedAt "archivedAt")`  |  [URL](https://schema.org/URL "URL") or   
[WebPage](https://schema.org/WebPage "WebPage")  | Indicates a page or other link involved in archival of a [CreativeWork](https://schema.org/CreativeWork). In the case of [MediaReview](https://schema.org/MediaReview), the items in a [MediaReviewItem](https://schema.org/MediaReviewItem) may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.   |  
| `               assesses[](https://schema.org/assesses "assesses")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | The item being described is intended to assess the competency or learning outcome defined by the referenced term.   |  
| `               associatedMedia[](https://schema.org/associatedMedia "associatedMedia")`  |  [MediaObject](https://schema.org/MediaObject "MediaObject")  | A media object that encodes this CreativeWork. This property is a synonym for encoding.   |  
| `               audience[](https://schema.org/audience "audience")`  |  [Audience](https://schema.org/Audience "Audience")  | An intended audience, i.e. a group for whom something was created. Supersedes [serviceAudience](https://schema.org/serviceAudience "serviceAudience").   |  
| `               audio[](https://schema.org/audio "audio")`  |  [AudioObject](https://schema.org/AudioObject "AudioObject") or   
[Clip](https://schema.org/Clip "Clip") or   
[MusicRecording](https://schema.org/MusicRecording "MusicRecording")  | An embedded audio object.   |  
| `               author[](https://schema.org/author "author")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.   |  
| `               award[](https://schema.org/award "award")`  |  [Text](https://schema.org/Text "Text")  | An award won by or for this item. Supersedes [awards](https://schema.org/awards "awards").   |  
| `               character[](https://schema.org/character "character")`  |  [Person](https://schema.org/Person "Person")  | Fictional person connected with a creative work.   |  
| `               citation[](https://schema.org/citation "citation")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Text](https://schema.org/Text "Text")  | A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.   |  
| `               comment[](https://schema.org/comment "comment")`  |  [Comment](https://schema.org/Comment "Comment")  | Comments, typically from users.   |  
| `               commentCount[](https://schema.org/commentCount "commentCount")`  |  [Integer](https://schema.org/Integer "Integer")  | The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.   |  
| `               conditionsOfAccess[](https://schema.org/conditionsOfAccess "conditionsOfAccess")`  |  [Text](https://schema.org/Text "Text")  | Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [ArchiveComponent](https://schema.org/ArchiveComponent) held by an [ArchiveOrganization](https://schema.org/ArchiveOrganization). This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.  
  
For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ".   |  
| `               contentLocation[](https://schema.org/contentLocation "contentLocation")`  |  [Place](https://schema.org/Place "Place")  | The location depicted or described in the content. For example, the location in a photograph or painting.   |  
| `               contentRating[](https://schema.org/contentRating "contentRating")`  |  [Rating](https://schema.org/Rating "Rating") or   
[Text](https://schema.org/Text "Text")  | Official rating of a piece of content—for example, 'MPAA PG-13'.   |  
| `               contentReferenceTime[](https://schema.org/contentReferenceTime "contentReferenceTime")`  |  [DateTime](https://schema.org/DateTime "DateTime")  | The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.   |  
| `               contributor[](https://schema.org/contributor "contributor")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A secondary contributor to the CreativeWork or Event.   |  
| `               copyrightHolder[](https://schema.org/copyrightHolder "copyrightHolder")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The party holding the legal copyright to the CreativeWork.   |  
| `               copyrightNotice[](https://schema.org/copyrightNotice "copyrightNotice")`  |  [Text](https://schema.org/Text "Text")  | Text of a notice appropriate for describing the copyright aspects of this Creative Work, ideally indicating the owner of the copyright for the Work.   |  
| `               copyrightYear[](https://schema.org/copyrightYear "copyrightYear")`  |  [Number](https://schema.org/Number "Number")  | The year during which the claimed copyright for the CreativeWork was first asserted.   |  
| `               correction[](https://schema.org/correction "correction")`  |  [CorrectionComment](https://schema.org/CorrectionComment "CorrectionComment") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | Indicates a correction to a [CreativeWork](https://schema.org/CreativeWork), either via a [CorrectionComment](https://schema.org/CorrectionComment), textually or in another document.   |  
| `               countryOfOrigin[](https://schema.org/countryOfOrigin "countryOfOrigin")`  |  [Country](https://schema.org/Country "Country")  | The country of origin of something, including products as well as creative works such as movie and TV content.  
  
In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [CreativeWork](https://schema.org/CreativeWork) it is difficult to provide fully general guidance, and properties such as [contentLocation](https://schema.org/contentLocation) and [locationCreated](https://schema.org/locationCreated) may be more applicable.  
  
In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.   |  
| `               creativeWorkStatus[](https://schema.org/creativeWorkStatus "creativeWorkStatus")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.   |  
| `               creator[](https://schema.org/creator "creator")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.   |  
| `               creditText[](https://schema.org/creditText "creditText")`  |  [Text](https://schema.org/Text "Text")  | Text that can be used to credit person(s) and/or organization(s) associated with a published Creative Work.   |  
| `               dateCreated[](https://schema.org/dateCreated "dateCreated")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | The date on which the CreativeWork was created or the item was added to a DataFeed.   |  
| `               dateModified[](https://schema.org/dateModified "dateModified")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.   |  
| `               datePublished[](https://schema.org/datePublished "datePublished")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | Date of first publication or broadcast. For example the date a [CreativeWork](https://schema.org/CreativeWork) was broadcast or a [Certification](https://schema.org/Certification) was issued.   |  
| `               digitalSourceType[](https://schema.org/digitalSourceType "digitalSourceType")`  |  [IPTCDigitalSourceEnumeration](https://schema.org/IPTCDigitalSourceEnumeration "IPTCDigitalSourceEnumeration")  | Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some [CreativeWork](https://schema.org/CreativeWork).   |  
| `               discussionUrl[](https://schema.org/discussionUrl "discussionUrl")`  |  [URL](https://schema.org/URL "URL")  | A link to the page containing the comments of the CreativeWork.   |  
| `               displayLocation[](https://schema.org/displayLocation "displayLocation")`  |  [Place](https://schema.org/Place "Place")  | The location at which an item can be viewed or experienced in-person.   |  
| `               editEIDR[](https://schema.org/editEIDR "editEIDR")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [identifier](https://schema.org/identifier) representing a specific edit / edition for a work of film or television.  
  
For example, the motion picture known as "Ghostbusters" whose [titleEIDR](https://schema.org/titleEIDR) is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".  
  
Since schema.org types like [Movie](https://schema.org/Movie) and [TVEpisode](https://schema.org/TVEpisode) can be used for both works and their multiple expressions, it is possible to use [titleEIDR](https://schema.org/titleEIDR) alone (for a general description), or alongside [editEIDR](https://schema.org/editEIDR) for a more edit-specific description.   |  
| `               editor[](https://schema.org/editor "editor")`  |  [Person](https://schema.org/Person "Person")  | Specifies the Person who edited the CreativeWork.   |  
| `               educationalAlignment[](https://schema.org/educationalAlignment "educationalAlignment")`  |  [AlignmentObject](https://schema.org/AlignmentObject "AlignmentObject")  | An alignment to an established educational framework.  
  
This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [teaches](https://schema.org/teaches) or [assesses](https://schema.org/assesses) a competency.   |  
| `               educationalLevel[](https://schema.org/educationalLevel "educationalLevel")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.   |  
| `               educationalUse[](https://schema.org/educationalUse "educationalUse")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | The purpose of a work in the context of education; for example, 'assignment', 'group work'.   |  
| `               encoding[](https://schema.org/encoding "encoding")`  |  [MediaObject](https://schema.org/MediaObject "MediaObject")  | A media object that encodes this CreativeWork. This property is a synonym for associatedMedia. Supersedes [encodings](https://schema.org/encodings "encodings").   
Inverse property: [encodesCreativeWork](https://schema.org/encodesCreativeWork "encodesCreativeWork")  |  
| `               encodingFormat[](https://schema.org/encodingFormat "encodingFormat")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.  
  
In cases where a [CreativeWork](https://schema.org/CreativeWork) has several media type representations, [encoding](https://schema.org/encoding) can be used to indicate each [MediaObject](https://schema.org/MediaObject) alongside particular [encodingFormat](https://schema.org/encodingFormat) information.  
  
Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry. Supersedes [fileFormat](https://schema.org/fileFormat "fileFormat").   |  
| `               exampleOfWork[](https://schema.org/exampleOfWork "exampleOfWork")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  | A creative work that this work is an example/instance/realization/derivation of.   
Inverse property: [workExample](https://schema.org/workExample "workExample")  |  
| `               expires[](https://schema.org/expires "expires")`  |  [Date](https://schema.org/Date "Date") or   
[DateTime](https://schema.org/DateTime "DateTime")  | Date the content expires and is no longer useful or available. For example a [VideoObject](https://schema.org/VideoObject) or [NewsArticle](https://schema.org/NewsArticle) whose availability or relevance is time-limited, a [ClaimReview](https://schema.org/ClaimReview) fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a [Certification](https://schema.org/Certification) the validity has expired.   |  
| `               funder[](https://schema.org/funder "funder")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A person or organization that supports (sponsors) something through some kind of financial contribution.   |  
| `               funding[](https://schema.org/funding "funding")`  |  [Grant](https://schema.org/Grant "Grant")  | A [Grant](https://schema.org/Grant) that directly or indirectly provide funding or sponsorship for this item. See also [ownershipFundingInfo](https://schema.org/ownershipFundingInfo).   
Inverse property: [fundedItem](https://schema.org/fundedItem "fundedItem")  |  
| `               genre[](https://schema.org/genre "genre")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | Genre of the creative work, broadcast channel or group.   |  
| `               hasPart[](https://schema.org/hasPart "hasPart")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  | Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).   
Inverse property: [isPartOf](https://schema.org/isPartOf "isPartOf")  |  
| `               headline[](https://schema.org/headline "headline")`  |  [Text](https://schema.org/Text "Text")  | Headline of the article.   |  
| `               inLanguage[](https://schema.org/inLanguage "inLanguage")`  |  [Language](https://schema.org/Language "Language") or   
[Text](https://schema.org/Text "Text")  | The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [availableLanguage](https://schema.org/availableLanguage). Supersedes [language](https://schema.org/language "language").   |  
| `               interactionStatistic[](https://schema.org/interactionStatistic "interactionStatistic")`  |  [InteractionCounter](https://schema.org/InteractionCounter "InteractionCounter")  | The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used. Supersedes [interactionCount](https://schema.org/interactionCount "interactionCount").   |  
| `               interactivityType[](https://schema.org/interactivityType "interactivityType")`  |  [Text](https://schema.org/Text "Text")  | The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.   |  
| `               interpretedAsClaim[](https://schema.org/interpretedAsClaim "interpretedAsClaim")`  |  [Claim](https://schema.org/Claim "Claim")  | Used to indicate a specific claim contained, implied, translated or refined from the content of a [MediaObject](https://schema.org/MediaObject) or other [CreativeWork](https://schema.org/CreativeWork). The interpreting party can be indicated using [claimInterpreter](https://schema.org/claimInterpreter).   |  
| `               isAccessibleForFree[](https://schema.org/isAccessibleForFree "isAccessibleForFree")`  |  [Boolean](https://schema.org/Boolean "Boolean")  | A flag to signal that the item, event, or place is accessible for free. Supersedes [free](https://schema.org/free "free").   |  
| `               isBasedOn[](https://schema.org/isBasedOn "isBasedOn")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Product](https://schema.org/Product "Product") or   
[URL](https://schema.org/URL "URL")  | A resource from which this work is derived or from which it is a modification or adaptation. Supersedes [isBasedOnUrl](https://schema.org/isBasedOnUrl "isBasedOnUrl").   |  
| `               isFamilyFriendly[](https://schema.org/isFamilyFriendly "isFamilyFriendly")`  |  [Boolean](https://schema.org/Boolean "Boolean")  | Indicates whether this content is family friendly.   |  
| `               isPartOf[](https://schema.org/isPartOf "isPartOf")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.   
Inverse property: [hasPart](https://schema.org/hasPart "hasPart")  |  
| `               keywords[](https://schema.org/keywords "keywords")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.   |  
| `               learningResourceType[](https://schema.org/learningResourceType "learningResourceType")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.   |  
| `               license[](https://schema.org/license "license")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | A license document that applies to this content, typically indicated by URL.   |  
| `               locationCreated[](https://schema.org/locationCreated "locationCreated")`  |  [Place](https://schema.org/Place "Place")  | The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.   |  
| `               mainEntity[](https://schema.org/mainEntity "mainEntity")`  |  [Thing](https://schema.org/Thing "Thing")  | Indicates the primary entity described in some page or other CreativeWork.   
Inverse property: [mainEntityOfPage](https://schema.org/mainEntityOfPage "mainEntityOfPage")  |  
| `               maintainer[](https://schema.org/maintainer "maintainer")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A maintainer of a [Dataset](https://schema.org/Dataset), software package ([SoftwareApplication](https://schema.org/SoftwareApplication)), or other [Project](https://schema.org/Project). A maintainer is a [Person](https://schema.org/Person) or [Organization](https://schema.org/Organization) that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When [maintainer](https://schema.org/maintainer) is applied to a specific version of something e.g. a particular version or packaging of a [Dataset](https://schema.org/Dataset), it is always possible that the upstream source has a different maintainer. The [isBasedOn](https://schema.org/isBasedOn) property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.   |  
| `               material[](https://schema.org/material "material")`  |  [Product](https://schema.org/Product "Product") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | A material that something is made from, e.g. leather, wool, cotton, paper.   |  
| `               materialExtent[](https://schema.org/materialExtent "materialExtent")`  |  [QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue") or   
[Text](https://schema.org/Text "Text")  | The quantity of the materials being described or an expression of the physical space they occupy.   |  
| `               mentions[](https://schema.org/mentions "mentions")`  |  [Thing](https://schema.org/Thing "Thing")  | Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.   |  
| `               offers[](https://schema.org/offers "offers")`  |  [Demand](https://schema.org/Demand "Demand") or   
[Offer](https://schema.org/Offer "Offer")  | An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [businessFunction](https://schema.org/businessFunction) to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [Demand](https://schema.org/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.   
Inverse property: [itemOffered](https://schema.org/itemOffered "itemOffered")  |  
| `               pattern[](https://schema.org/pattern "pattern")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.   |  
| `               position[](https://schema.org/position "position")`  |  [Integer](https://schema.org/Integer "Integer") or   
[Text](https://schema.org/Text "Text")  | The position of an item in a series or sequence of items.   |  
| `               producer[](https://schema.org/producer "producer")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The person or organization who produced the work (e.g. music album, movie, TV/radio series etc.).   |  
| `               provider[](https://schema.org/provider "provider")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes [carrier](https://schema.org/carrier "carrier").   |  
| `               publication[](https://schema.org/publication "publication")`  |  [PublicationEvent](https://schema.org/PublicationEvent "PublicationEvent")  | A publication event associated with the item.   |  
| `               publisher[](https://schema.org/publisher "publisher")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | The publisher of the article in question.   |  
| `               publisherImprint[](https://schema.org/publisherImprint "publisherImprint")`  |  [Organization](https://schema.org/Organization "Organization")  | The publishing division which published the comic.   |  
| `               publishingPrinciples[](https://schema.org/publishingPrinciples "publishingPrinciples")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | The publishingPrinciples property indicates (typically via [URL](https://schema.org/URL)) a document describing the editorial principles of an [Organization](https://schema.org/Organization) (or individual, e.g. a [Person](https://schema.org/Person) writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [CreativeWork](https://schema.org/CreativeWork) (e.g. [NewsArticle](https://schema.org/NewsArticle)) the principles are those of the party primarily responsible for the creation of the [CreativeWork](https://schema.org/CreativeWork).  
  
While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [funder](https://schema.org/funder)) can be expressed using schema.org terminology.   |  
| `               recordedAt[](https://schema.org/recordedAt "recordedAt")`  |  [Event](https://schema.org/Event "Event")  | The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.   
Inverse property: [recordedIn](https://schema.org/recordedIn "recordedIn")  |  
| `               releasedEvent[](https://schema.org/releasedEvent "releasedEvent")`  |  [PublicationEvent](https://schema.org/PublicationEvent "PublicationEvent")  | The place and time the release was issued, expressed as a PublicationEvent.   |  
| `               review[](https://schema.org/review "review")`  |  [Review](https://schema.org/Review "Review")  | A review of the item. Supersedes [reviews](https://schema.org/reviews "reviews").   |  
| `               schemaVersion[](https://schema.org/schemaVersion "schemaVersion")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to indicate the use of a specific schema.org release, e.g. `10.0` as a simple string, or more explicitly via URL, `https://schema.org/docs/releases.html#v10.0`. There may be situations in which other schemas might usefully be referenced this way, e.g. `http://dublincore.org/specifications/dublin-core/dces/1999-07-02/` but this has not been carefully explored in the community.   |  
| `               sdDatePublished[](https://schema.org/sdDatePublished "sdDatePublished")`  |  [Date](https://schema.org/Date "Date")  | Indicates the date on which the current structured data was generated / published. Typically used alongside [sdPublisher](https://schema.org/sdPublisher).   |  
| `               sdLicense[](https://schema.org/sdLicense "sdLicense")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | A license document that applies to this structured data, typically indicated by URL.   |  
| `               sdPublisher[](https://schema.org/sdPublisher "sdPublisher")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | Indicates the party responsible for generating and publishing the current structured data markup, typically in cases where the structured data is derived automatically from existing published content but published on a different site. For example, student projects and open data initiatives often re-publish existing content with more explicitly structured metadata. The [sdPublisher](https://schema.org/sdPublisher) property helps make such practices more explicit.   |  
| `               size[](https://schema.org/size "size")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[QuantitativeValue](https://schema.org/QuantitativeValue "QuantitativeValue") or   
[SizeSpecification](https://schema.org/SizeSpecification "SizeSpecification") or   
[Text](https://schema.org/Text "Text")  | A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode, or a comprehensive and structured [SizeSpecification](https://schema.org/SizeSpecification); in other cases, the [width](https://schema.org/width), [height](https://schema.org/height), [depth](https://schema.org/depth) and [weight](https://schema.org/weight) properties may be more applicable.   |  
| `               sourceOrganization[](https://schema.org/sourceOrganization "sourceOrganization")`  |  [Organization](https://schema.org/Organization "Organization")  | The Organization on whose behalf the creator was working.   |  
| `               spatial[](https://schema.org/spatial "spatial")`  |  [Place](https://schema.org/Place "Place")  | The "spatial" property can be used in cases when more specific properties (e.g. [locationCreated](https://schema.org/locationCreated), [spatialCoverage](https://schema.org/spatialCoverage), [contentLocation](https://schema.org/contentLocation)) are not known to be appropriate.   |  
| `               spatialCoverage[](https://schema.org/spatialCoverage "spatialCoverage")`  |  [Place](https://schema.org/Place "Place")  | The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York.   |  
| `               sponsor[](https://schema.org/sponsor "sponsor")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.   |  
| `               teaches[](https://schema.org/teaches "teaches")`  |  [DefinedTerm](https://schema.org/DefinedTerm "DefinedTerm") or   
[Text](https://schema.org/Text "Text")  | The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.   |  
| `               temporal[](https://schema.org/temporal "temporal")`  |  [DateTime](https://schema.org/DateTime "DateTime") or   
[Text](https://schema.org/Text "Text")  | The "temporal" property can be used in cases where more specific properties (e.g. [temporalCoverage](https://schema.org/temporalCoverage), [dateCreated](https://schema.org/dateCreated), [dateModified](https://schema.org/dateModified), [datePublished](https://schema.org/datePublished)) are not known to be appropriate.   |  
| `               temporalCoverage[](https://schema.org/temporalCoverage "temporalCoverage")`  |  [DateTime](https://schema.org/DateTime "DateTime") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | The temporalCoverage of a CreativeWork indicates the period that the content applies to, i.e. that it describes, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL. Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".  
  
Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated. Supersedes [datasetTimeInterval](https://schema.org/datasetTimeInterval "datasetTimeInterval").   |  
| `               text[](https://schema.org/text "text")`  |  [Text](https://schema.org/Text "Text")  | The textual content of this CreativeWork.   |  
| `               thumbnail[](https://schema.org/thumbnail "thumbnail")`  |  [ImageObject](https://schema.org/ImageObject "ImageObject")  | Thumbnail image for an image or video.   |  
| `               thumbnailUrl[](https://schema.org/thumbnailUrl "thumbnailUrl")`  |  [URL](https://schema.org/URL "URL")  | A thumbnail image relevant to the Thing.   |  
| `               timeRequired[](https://schema.org/timeRequired "timeRequired")`  |  [Duration](https://schema.org/Duration "Duration")  | Approximate or typical time it usually takes to work with or through the content of this work for the typical or target audience.   |  
| `               translationOfWork[](https://schema.org/translationOfWork "translationOfWork")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  | The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the Origin of Species”.   
Inverse property: [workTranslation](https://schema.org/workTranslation "workTranslation")  |  
| `               translator[](https://schema.org/translator "translator")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.   |  
| `               typicalAgeRange[](https://schema.org/typicalAgeRange "typicalAgeRange")`  |  [Text](https://schema.org/Text "Text")  | The typical expected age range, e.g. '7-9', '11-'.   |  
| `               usageInfo[](https://schema.org/usageInfo "usageInfo")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | The schema.org [usageInfo](https://schema.org/usageInfo) property indicates further information about a [CreativeWork](https://schema.org/CreativeWork). This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.  
  
This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.   |  
| `               version[](https://schema.org/version "version")`  |  [Number](https://schema.org/Number "Number") or   
[Text](https://schema.org/Text "Text")  | The version of the CreativeWork embodied by a specified resource.   |  
| `               video[](https://schema.org/video "video")`  |  [Clip](https://schema.org/Clip "Clip") or   
[VideoObject](https://schema.org/VideoObject "VideoObject")  | An embedded video object.   |  
| `               wordCount[](https://schema.org/wordCount "wordCount")`  |  [Integer](https://schema.org/Integer "Integer")  | The number of words in the text of the CreativeWork such as an Article, Book, etc.   |  
| `               workExample[](https://schema.org/workExample "workExample")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  | Example/instance/realization/derivation of the concept of this creative work. E.g. the paperback edition, first edition, or e-book.   
Inverse property: [exampleOfWork](https://schema.org/exampleOfWork "exampleOfWork")  |  
| `               workTranslation[](https://schema.org/workTranslation "workTranslation")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork")  | A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation “Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese translation Tây du ký bình khảo.   
Inverse property: [translationOfWork](https://schema.org/translationOfWork "translationOfWork")  |  
| Properties from [Thing](https://schema.org/Thing "Thing")  |  
| `               additionalType[](https://schema.org/additionalType "additionalType")`  |  [Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org [style guide](https://schema.org/docs/styleguide.html).   |  
| `               alternateName[](https://schema.org/alternateName "alternateName")`  |  [Text](https://schema.org/Text "Text")  | An alias for the item.   |  
| `               description[](https://schema.org/description "description")`  |  [Text](https://schema.org/Text "Text") or   
[TextObject](https://schema.org/TextObject "TextObject")  | A description of the item.   |  
| `               disambiguatingDescription[](https://schema.org/disambiguatingDescription "disambiguatingDescription")`  |  [Text](https://schema.org/Text "Text")  | A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.   |  
| `               identifier[](https://schema.org/identifier "identifier")`  |  [PropertyValue](https://schema.org/PropertyValue "PropertyValue") or   
[Text](https://schema.org/Text "Text") or   
[URL](https://schema.org/URL "URL")  | The identifier property represents any kind of identifier for any kind of [Thing](https://schema.org/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](https://schema.org/docs/datamodel.html#identifierBg) for more details.   |  
| `               image[](https://schema.org/image "image")`  |  [ImageObject](https://schema.org/ImageObject "ImageObject") or   
[URL](https://schema.org/URL "URL")  | An image of the item. This can be a [URL](https://schema.org/URL) or a fully described [ImageObject](https://schema.org/ImageObject).   |  
| `               mainEntityOfPage[](https://schema.org/mainEntityOfPage "mainEntityOfPage")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[URL](https://schema.org/URL "URL")  | Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](https://schema.org/docs/datamodel.html#mainEntityBackground) for details.   
Inverse property: [mainEntity](https://schema.org/mainEntity "mainEntity")  |  
| `               name[](https://schema.org/name "name")`  |  [Text](https://schema.org/Text "Text")  | The name of the item.   |  
| `               owner[](https://schema.org/owner "owner")`  |  [Organization](https://schema.org/Organization "Organization") or   
[Person](https://schema.org/Person "Person")  | A person or organization who owns this Thing.   
Inverse property: [owns](https://schema.org/owns "owns")  |  
| `               potentialAction[](https://schema.org/potentialAction "potentialAction")`  |  [Action](https://schema.org/Action "Action")  | Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.   |  
| `               sameAs[](https://schema.org/sameAs "sameAs")`  |  [URL](https://schema.org/URL "URL")  | URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.   |  
| `               subjectOf[](https://schema.org/subjectOf "subjectOf")`  |  [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or   
[Event](https://schema.org/Event "Event")  | A CreativeWork or Event about this Thing.   
Inverse property: [about](https://schema.org/about "about")  |  
| `               url[](https://schema.org/url "url")`  |  [URL](https://schema.org/URL "URL")  | URL of the item.   |  
  

#### More specific Types
  * [MedicalScholarlyArticle](https://schema.org/MedicalScholarlyArticle "MedicalScholarlyArticle")


### Examples
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 1](https://schema.org/ScholarlyArticle#eg-0398 "Link: #eg-0398")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<!-- A list of the issues for a single volume of a given periodical. -->  




  2. 
<div>  




  3. 
 <h1>The Lancet</h1>  




  4. 
 <p>Volume 376, July 2010-December 2010</p>  




  5. 
 <p>Published by Elsevier  




  6. 
 <ul>  




  7. 
   <li>ISSN 0140-6736</li>  




  8. 
 </ul>  




  9. 
 <h3>Issues:</h3>  




  10. 
 <ul>  




  11. 
   <li>No. 9734 Jul 3, 2010 p 1-68</li>  




  12. 
   <li>No. 9735 Jul 10, 2010 p 69-140</li>  




  13. 
 </ul>  




  14. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<!-- A list of the issues for a single volume of a given periodical. -->  




  2. 
<div itemscope itemtype="https://schema.org/Periodical">  




  3. 
  <h1 itemprop="name">The Lancet</h1>  




  4. 
  <p>Volume 376, July 2010-December 2010</p>  




  5. 
  <p>Published by <span itemprop="publisher">Elsevier</span>  




  6. 
  <ul>  




  7. 
    <li>ISSN <span itemprop="issn">0140-6736</span></li>  




  8. 
  </ul>  




  9. 
  <h3>Issues:</h3>  




  10. 
  <div itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationVolume" itemid="#vol376">  




  11. 
    <meta itemprop="volumeNumber" content="376">  




  12. 
    <ul>  




  13. 
      <li itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#iss9734">No.  




  14. 
        <span itemprop="issueNumber">9734</span>  




  15. 
        <time datetime="2010-07-03" itemprop="datePublished">Jul 3, 2010</time>  




  16. 
        p <span itemprop="pageStart">1</span>-<span itemprop="pageEnd">68</span>  




  17. 
      </li>  




  18. 
      <li itemprop="hasPart" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#iss9735">No.  




  19. 
        <span itemprop="issueNumber">9735</span>  




  20. 
        <time datetime="2010-07-03" itemprop="datePublished">Jul 10, 2010</time>  




  21. 
        p <span itemprop="pageStart">69</span>-<span itemprop="pageEnd">140</span>  




  22. 
      </li>  




  23. 
    </ul>  




  24. 
  </div>  




  25. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<!-- A list of the issues for a single volume of a given periodical. -->  




  2. 
<div vocab="https://schema.org/" typeof="Periodical">  




  3. 
  <h1 property="name">The Lancet</h1>  




  4. 
  <p>Volume 376, July 2010-December 2010</p>  




  5. 
  <p>Published by <span property="publisher">Elsevier</span>  




  6. 
  <ul>  




  7. 
    <li>ISSN <span property="issn">0140-6736</span></li>  




  8. 
  </ul>  




  9. 
  <h3>Issues:</h3>  




  10. 
  <div property="hasPart" typeof="PublicationVolume" resource="#vol376">  




  11. 
    <meta property="volumeNumber" content="376">  




  12. 
    <ul>  




  13. 
      <li property="hasPart" typeof="PublicationIssue" resource="#issue9734">No.  




  14. 
        <span property="issueNumber">9734</span>  




  15. 
        <time datetime="2010-07-03" property="datePublished">Jul 3, 2010</time>  




  16. 
        p <span property="pageStart">1</span>-<span property="pageEnd">68</span>  




  17. 
      </li>  




  18. 
      <li property="hasPart" typeof="PublicationIssue" resource="#issue9735">No.  




  19. 
        <span property="issueNumber">9735</span>  




  20. 
        <time datetime="2010-07-03" property="datePublished">Jul 10, 2010</time>  




  21. 
        p <span property="pageStart">69</span>-<span property="pageEnd">140</span>  




  22. 
      </li>  




  23. 
    </ul>  




  24. 
  </div>  




  25. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Periodical",  




  5. 
  "issn": "0140-6736",  




  6. 
  "hasPart": {  




  7. 
    "@id": "vol376",  




  8. 
    "@type": "PublicationVolume",  




  9. 
    "volumeNumber": "376",  




  10. 
    "hasPart": [  




  11. 
      {  




  12. 
        "@id": "issue9735",  




  13. 
        "@type": "PublicationIssue",  




  14. 
        "datePublished": "2010-07-03",  




  15. 
        "pageEnd": "140",  




  16. 
        "pageStart": "69",  




  17. 
        "issueNumber": "9735"  




  18. 
      },  




  19. 
      {  




  20. 
        "@id": "issue9734",  




  21. 
        "@type": "PublicationIssue",  




  22. 
        "datePublished": "2010-07-03",  




  23. 
        "pageEnd": "68",  




  24. 
        "pageStart": "1",  




  25. 
        "issueNumber": "9734"  




  26. 
      }  




  27. 
    ]  




  28. 
  },  




  29. 
  "name": "The Lancet",  




  30. 
  "publisher": "Elsevier"  




  31. 
}  




  32. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Periodical", "issn": "0140-6736", "hasPart": { "@id": "vol376", "@type": "PublicationVolume", "volumeNumber": "376", "hasPart": [ { "@id": "issue9735", "@type": "PublicationIssue", "datePublished": "2010-07-03", "pageEnd": "140", "pageStart": "69", "issueNumber": "9735" }, { "@id": "issue9734", "@type": "PublicationIssue", "datePublished": "2010-07-03", "pageEnd": "68", "pageStart": "1", "issueNumber": "9734" } ] }, "name": "The Lancet", "publisher": "Elsevier" }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 2](https://schema.org/ScholarlyArticle#eg-0399 "Link: #eg-0399")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<!-- An article, fully linked to the issue, volume, and periodical in which it was published -->  




  2. 
<div>  




  3. 
  <strong>Title:</strong> Be Careful What You Wish For: FRBR, Some Lacunae, A Review<br />  




  4. 
  <strong>Author:</strong> Smiraglia, Richard P.<br />  




  5. 
  <strong>Subjects:</strong> Catalog ; Works <br />  




  6. 
  <strong>Is Part Of:</strong>  




  7. 
  <div>Cataloging &amp;amp; Classification Quarterly, 2012, Vol. 50 (5),</div>  




  8. 
  <div>p.360-368 [Peer Reviewed Journal]<br />  




  9. 
    <strong>Description:</strong>  




  10. 
      The library catalog as a catalog of works  




  11. 
      was an infectious idea, which together with research led to  




  12. 
      reconceptualization in the form of the FRBR conceptual model. Two  




  13. 
      categories of lacunae emerge—the expression entity, and gaps in the  




  14. 
      model such as aggregates and dynamic documents. Evidence needed to  




  15. 
      extend the FRBR model is available in contemporary research on  




  16. 
      instantiation. The challenge for the bibliographic community is to  




  17. 
      begin to think of FRBR as a form of knowledge organization system,  




  18. 
      adding a final dimension to classification. The articles in the present  




  19. 
      special issue offer a compendium of the promise of the FRBR  




  20. 
      model.  




  21. 
  </div>  




  22. 
  <strong>Publisher:</strong> Taylor &amp;amp; Francis Group<br />  




  23. 
  <strong>Source:</strong> Routledge, Taylor &amp;amp; Francis Group<br />  




  24. 
  <strong>ISSN</strong> 0163-9374 ;<br />  




  25. 
  <strong>E-ISSN</strong> 1544-4554;<br />  




  26. 
  <strong>DOI:</strong>  




  27. 
  <a href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a>  




  28. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<!-- An article, fully linked to the issue, volume, and periodical in which it was published -->  




  2. 
<div itemscope itemtype="https://schema.org/ScholarlyArticle">  




  3. 
  <strong>Title:</strong> <span itemprop="name">Be Careful What You Wish For: FRBR, Some Lacunae, A Review</span><br />  




  4. 
  <strong>Author:</strong> <span itemprop="author">Smiraglia, Richard P.</span><br />  




  5. 
  <strong>Subjects:</strong> <span itemprop="about">Catalog</span> ; <span itemprop="about">Works</span> <br />  




  6. 
  <strong>Is Part Of:</strong>  




  7. 
  <div itemprop="isPartOf" itemscope itemtype="https://schema.org/PublicationIssue" itemid="#issue">  




  8. 
    <span itemscope itemtype="https://schema.org/Periodical" itemid="#periodical">  




  9. 
      <span itemprop="name">Cataloging &amp;amp; Classification Quarterly</span>,  




  10. 
    </span>  




  11. 
    <span itemprop="datePublished">2012</span>,  




  12. 
    Vol.<span itemprop="isPartOf" itemscope  




  13. 
              itemtype="https://schema.org/PublicationVolume"><link  




  14. 
              itemprop="isPartOf" href="#periodical" /><span  




  15. 
              itemprop="volumeNumber">50</span></span>(<span  




  16. 
          itemprop="issueNumber">5</span>),  




  17. 
  </div>  




  18. 
  <div>  




  19. 
    p.<span itemprop="pageStart">360</span>-<span itemprop="pageEnd">368</span> [Peer Reviewed Journal]<br />  




  20. 
    <strong>Description:</strong>  




  21. 
    <span itemprop="description">The library catalog as a catalog of works  




  22. 
      was an infectious idea, which together with research led to  




  23. 
      reconceptualization in the form of the FRBR conceptual model. Two  




  24. 
      categories of lacunae emerge—the expression entity, and gaps in the  




  25. 
      model such as aggregates and dynamic documents. Evidence needed to  




  26. 
      extend the FRBR model is available in contemporary research on  




  27. 
      instantiation. The challenge for the bibliographic community is to  




  28. 
      begin to think of FRBR as a form of knowledge organization system,  




  29. 
      adding a final dimension to classification. The articles in the present  




  30. 
      special issue offer a compendium of the promise of the FRBR  




  31. 
      model.</span>  




  32. 
  </div>  




  33. 
  <span itemscope itemtype="https://schema.org/Periodical" itemid="#periodical">  




  34. 
    <strong>Publisher:</strong>  




  35. 
    <span itemprop="publisher">Taylor &amp;amp; Francis Group</span><br />  




  36. 
    <strong>Source:</strong> Routledge, Taylor &amp;amp; Francis Group<br />  




  37. 
    <strong>ISSN</strong> <span itemprop="issn">0163-9374</span> ;<br />  




  38. 
    <strong>E-ISSN</strong> <span itemprop="issn">1544-4554</span> ;<br />  




  39. 
  </span>  




  40. 
  <strong>DOI:</strong>  




  41. 
  <a itemprop="sameAs" href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a>  




  42. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<!-- An article, fully linked to the issue, volume, and periodical in which it was published -->  




  2. 
<div vocab="https://schema.org/" typeof="ScholarlyArticle" resource="#article">  




  3. 
  <strong>Title:</strong> <span property="name">Be Careful What You Wish For: FRBR, Some Lacunae, A Review</span><br />  




  4. 
  <strong>Author:</strong> <span property="author">Smiraglia, Richard P.</span><br />  




  5. 
  <strong>Subjects:</strong> <span property="about">Catalog</span> ; <span property="about">Works</span> <br />  




  6. 
  <strong>Is Part Of:</strong>  




  7. 
  <div property="isPartOf" typeof="PublicationIssue" resource="#issue">  




  8. 
    <span typeof="Periodical" resource="#periodical">  




  9. 
      <span property="name">Cataloging &amp;amp; Classification Quarterly</span>,  




  10. 
    </span>  




  11. 
    <span property="datePublished">2012</span>,  




  12. 
    Vol.<span property="isPartOf" typeof="PublicationVolume" resource="#periodical"><span  




  13. 
              property="volumeNumber">50</span></span>(<span  




  14. 
          property="issueNumber">5</span>),  




  15. 
  </div>  




  16. 
  <div>  




  17. 
    p.<span property="pageStart">360</span>-<span property="pageEnd">368</span> [Peer Reviewed Journal]<br />  




  18. 
    <strong>Description:</strong>  




  19. 
    <span property="description">The library catalog as a catalog of works  




  20. 
      was an infectious idea, which together with research led to  




  21. 
      reconceptualization in the form of the FRBR conceptual model. Two  




  22. 
      categories of lacunae emerge—the expression entity, and gaps in the  




  23. 
      model such as aggregates and dynamic documents. Evidence needed to  




  24. 
      extend the FRBR model is available in contemporary research on  




  25. 
      instantiation. The challenge for the bibliographic community is to  




  26. 
      begin to think of FRBR as a form of knowledge organization system,  




  27. 
      adding a final dimension to classification. The articles in the present  




  28. 
      special issue offer a compendium of the promise of the FRBR  




  29. 
      model.</span>  




  30. 
  </div>  




  31. 
  <span resource="#periodical">  




  32. 
    <strong>Publisher:</strong>  




  33. 
    <span property="publisher">Taylor &amp;amp; Francis Group</span><br />  




  34. 
    <strong>Source:</strong> Routledge, Taylor &amp;amp; Francis Group<br />  




  35. 
    <strong>ISSN</strong> <span property="issn">0163-9374</span> ;<br />  




  36. 
    <strong>E-ISSN</strong> <span property="issn">1544-4554</span> ;<br />  




  37. 
  </span>  




  38. 
  <strong>DOI:</strong>  




  39. 
  <a property="sameAs" href="https://doi.org/10.1080/01639374.2012.682254">10.1080/01639374.2012.682254</a>  




  40. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@graph": [  




  5. 
    {  




  6. 
        "@id": "#issue",  




  7. 
        "@type": "PublicationIssue",  




  8. 
        "issueNumber": "5",  




  9. 
        "datePublished": "2012",  




  10. 
        "isPartOf": {  




  11. 
            "@id": "#periodical",  




  12. 
            "@type": [  




  13. 
                "PublicationVolume",  




  14. 
                "Periodical"  




  15. 
            ],  




  16. 
            "name": "Cataloging & Classification Quarterly",  




  17. 
            "issn": [  




  18. 
                "1544-4554",  




  19. 
                "0163-9374"  




  20. 
            ],  




  21. 
            "volumeNumber": "50",  




  22. 
            "publisher": "Taylor & Francis Group"  




  23. 
        }  




  24. 
    },  




  25. 
    {  




  26. 
        "@type": "ScholarlyArticle",  




  27. 
        "isPartOf": "#issue",  




  28. 
        "description": "The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge--the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.",  




  29. 
        "sameAs": "https://doi.org/10.1080/01639374.2012.682254",  




  30. 
        "about": [  




  31. 
            "Works",  




  32. 
            "Catalog"  




  33. 
        ],  




  34. 
        "pageEnd": "368",  




  35. 
        "pageStart": "360",  




  36. 
        "name": "Be Careful What You Wish For: FRBR, Some Lacunae, A Review",  




  37. 
        "author": "Smiraglia, Richard P."  




  38. 
    }  




  39. 
  ]  




  40. 
}  




  41. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@graph": [ { "@id": "#issue", "@type": "PublicationIssue", "issueNumber": "5", "datePublished": "2012", "isPartOf": { "@id": "#periodical", "@type": [ "PublicationVolume", "Periodical" ], "name": "Cataloging & Classification Quarterly", "issn": [ "1544-4554", "0163-9374" ], "volumeNumber": "50", "publisher": "Taylor & Francis Group" } }, { "@type": "ScholarlyArticle", "isPartOf": "#issue", "description": "The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge--the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.", "sameAs": "https://doi.org/10.1080/01639374.2012.682254", "about": [ "Works", "Catalog" ], "pageEnd": "368", "pageStart": "360", "name": "Be Careful What You Wish For: FRBR, Some Lacunae, A Review", "author": "Smiraglia, Richard P." } ] }
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 3](https://schema.org/ScholarlyArticle#eg-0401 "Link: #eg-0401")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<!-- An article citation in MLA format, using a 'flat' approach that simplifies  




  2. 
  markup by not specifying an explicit relationship between the periodical,  




  3. 
  volume, and issue -->  




  4. 
<div>  




  5. 
  Carlyle, Allyson. &quot;Understanding FRBR as a Conceptual Model: FRBR  




  6. 
    and the Bibliographic Universe.&quot;  




  7. 
  <em>Library Resources and Technical Services</em>,  




  8. 
  v. 50, no. 4 (October 2006): 264-273. Print.  




  9. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<!-- An article citation in MLA format, using a 'flat' approach that simplifies  




  2. 
  markup by not specifying an explicit relationship between the periodical,  




  3. 
  volume, and issue -->  




  4. 
<div itemscope itemtype="https://schema.org/ScholarlyArticle">  




  5. 
  <span itemprop="author">Carlyle, Allyson.</span>  




  6. 
  &quot;<span itemprop="name">Understanding FRBR as a Conceptual Model: FRBR  




  7. 
    and the Bibliographic Universe</span>&quot;  




  8. 
  <div itemprop="isPartOf" itemscope itemtype="https://schema.org/Periodical">  




  9. 
    <em><span itemprop="name">Library Resources and Technical Services</span></em>  




  10. 
  </div>  




  11. 
  <span itemprop="isPartOf" itemscope itemtype="https://schema.org/PublicationVolume">  




  12. 
    v. <span itemprop="volumeNumber">50</span>  




  13. 
  </span>,  




  14. 
  <span itemprop="isPartOf" itemscope itemtype="https://schema.org/PublicationIssue">  




  15. 
    no. <span itemprop="issueNumber">4</span>  




  16. 
    (<time datetime="2006-10" itemprop="datePublished">October 2006</time>):  




  17. 
  </span>  




  18. 
  <span itemprop="pageStart">264</span>-<span itemprop="pageEnd">273</span>  




  19. 
Print.</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<!-- An article citation in MLA format, using a 'flat' approach that simplifies  




  2. 
  markup by not specifying an explicit relationship between the periodical,  




  3. 
  volume, and issue -->  




  4. 
<div vocab="https://schema.org/" typeof="ScholarlyArticle">  




  5. 
  <span property="author">Carlyle, Allyson.</span>  




  6. 
  &quot;<span property="name">Understanding FRBR as a Conceptual Model: FRBR  




  7. 
    and the Bibliographic Universe</span>&quot;  




  8. 
  <div property="isPartOf" typeof="Periodical">  




  9. 
    <em><span property="name">Library Resources and Technical Services</span></em>  




  10. 
  </div>  




  11. 
  <span property="isPartOf" typeof="PublicationVolume">  




  12. 
    v. <span property ="volumeNumber">50</span>  




  13. 
  </span>,  




  14. 
  <span property="isPartOf" typeof="PublicationIssue">  




  15. 
    no. <span property="issueNumber">4</span>  




  16. 
    (<time datetime="2006-10" property="datePublished">October 2006</time>):  




  17. 
  </span>  




  18. 
  <span property="pageStart">264</span>-<span property="pageEnd">273</span>  




  19. 
Print.</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@graph": [  




  5. 
    {  




  6. 
      "@id": "#issue4",  




  7. 
      "@type": "PublicationIssue",  




  8. 
      "datePublished": "2006-10",  




  9. 
      "issueNumber": "4"  




  10. 
    },  




  11. 
    {  




  12. 
      "@id": "#volume50",  




  13. 
      "@type": "PublicationVolume",  




  14. 
      "volumeNumber": "50"  




  15. 
    },  




  16. 
    {  




  17. 
      "@id": "#periodical",  




  18. 
      "@type": "Periodical",  




  19. 
      "name": "Library Resources and Technical Services"  




  20. 
    },  




  21. 
    {  




  22. 
      "@id": "#article",  




  23. 
      "@type": "ScholarlyArticle",  




  24. 
      "author": "Carlyle, Allyson.",  




  25. 
      "isPartOf": [  




  26. 
        {  




  27. 
          "@id": "#periodical"  




  28. 
        },  




  29. 
        {  




  30. 
          "@id": "#volume50"  




  31. 
        },  




  32. 
        {  




  33. 
          "@id": "#issue4"  




  34. 
        }  




  35. 
      ],  




  36. 
      "name": "Understanding FRBR as a Conceptual Model: FRBR and the Bibliographic Universe",  




  37. 
      "pageEnd": "273",  




  38. 
      "pageStart": "264"  




  39. 
    }  




  40. 
  ]  




  41. 
}  




  42. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@graph": [ { "@id": "#issue4", "@type": "PublicationIssue", "datePublished": "2006-10", "issueNumber": "4" }, { "@id": "#volume50", "@type": "PublicationVolume", "volumeNumber": "50" }, { "@id": "#periodical", "@type": "Periodical", "name": "Library Resources and Technical Services" }, { "@id": "#article", "@type": "ScholarlyArticle", "author": "Carlyle, Allyson.", "isPartOf": [ { "@id": "#periodical" }, { "@id": "#volume50" }, { "@id": "#issue4" } ], "name": "Understanding FRBR as a Conceptual Model: FRBR and the Bibliographic Universe", "pageEnd": "273", "pageStart": "264" } ] }
[Terms and conditions](https://schema.org/docs/terms.html)
• Schema.org • V30.0 | 2026-03-19 

