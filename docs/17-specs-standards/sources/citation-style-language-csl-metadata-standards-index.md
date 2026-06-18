# Citation Style Language (CSL) — Metadata Standards Index

Source: https://msi.dublincore.org/standards/csl/

[Skip to main content](https://msi.dublincore.org/standards/csl/#main-content)
**Draft preview** — This site is an early-stage preview of the Metadata Standards Index. Content, URLs, and design are subject to change without notice.
[![Metadata Standards Index](https://msi.dublincore.org/logo.svg)](https://msi.dublincore.org/)
[Browse](https://msi.dublincore.org/standards)[Organizations](https://msi.dublincore.org/organizations)[Search](https://msi.dublincore.org/search)[About](https://msi.dublincore.org/about)
[Home](https://msi.dublincore.org/) [Standards](https://msi.dublincore.org/standards) CSL [ Back to Standards](https://msi.dublincore.org/standards)
![Citation Style Language logo](https://msi.dublincore.org/standards/csl/logo.png)
# Citation Style Language
CSL
[Technical Specification](https://msi.dublincore.org/types/specification) Active [Libraries & Library Science](https://msi.dublincore.org/subjects/libraries)[Scientific Data & Research](https://msi.dublincore.org/subjects/scientific-data)
An open XML-based language for describing the formatting of in-text citations, notes, and bibliographies. CSL provides a standardized way to encode the rules of thousands of citation styles — from APA and Chicago to journal-specific formats — so that reference management software can automatically format citations. It is used by Zotero, Mendeley, Papers, and many other tools, with a community-maintained repository of over 10,000 citation styles. 
##  Overview
The Citation Style Language (CSL) is an open, XML-based language for describing the formatting of citations, notes, and bibliographies. It provides the engine behind automatic citation formatting in reference managers like Zotero, Mendeley, and Papers, with a community-maintained repository of over 10,000 styles covering journals, publishers, and academic style guides worldwide.
## Background
CSL was created in 2004 by Bruce D'Arcus, a geographer at Miami University, who recognized the need for a standardized, open way to express citation formatting rules. At the time, reference managers each used proprietary style definitions, making it difficult to share citation styles or switch between tools. D'Arcus designed CSL as an XML schema that could encode the rules of any citation style in a portable, machine-readable format. Frank Bennett later contributed significant work on CSL processing, developing the citeproc-js processor. CSL 1.0 was released in 2010 as the first stable version, with CSL 1.0.1 (2012) and CSL 1.0.2 (2015) adding incremental improvements.
## Purpose & Scope
CSL defines how individual references should be formatted — where to place the author name, how to abbreviate journal titles, whether to use footnotes or in-text parenthetical citations, how to sort bibliography entries, and hundreds of other formatting details that vary across the thousands of citation styles in use. A single CSL style file encodes all these rules for one citation style, while CSL locale files handle language-specific terms and date formats.
## Key Concepts  
| Concept  | Description  |  
| --- | --- |  
| Style  | A CSL XML file defining formatting rules for one citation style  |  
| Locale  | Language-specific terms, date formats, and punctuation conventions  |  
| Citation  | The in-text marker (parenthetical, numeric, or note)  |  
| Bibliography  | The formatted list of references at the end of a document  |  
| Macro  | Reusable formatting blocks within a style definition  |  
| cs:info  | Metadata about the style (title, author, license, parent style)  |  
## Serializations & Technical Formats
CSL styles are XML documents conforming to the CSL schema, with the file extension `.csl`. Each style file is self-contained and can be validated against the CSL schema (RELAX NG). Styles can be either "independent" (defining all formatting rules directly) or "dependent" (inheriting rules from a parent style with only metadata differences). CSL locale files use a similar XML structure. The processing model is defined informally in the specification, with multiple implementations (citeproc-js, citeproc-py, citeproc-rs) providing the rendering logic.
## Governance & Maintenance
CSL is maintained as a community project with development coordinated on GitHub. The CSL schema, specification, and style repository are all openly governed. Style contributions undergo review before acceptance into the official repository. The project has no formal standards body affiliation; governance is informal, with core maintainers guiding development. CSL 1.0.2 is the current stable release. Work on CSL 1.1 has introduced features like custom variable types and improved name handling, though it has not yet reached final release.
## Notable Implementations
Zotero, the open-source reference manager, was an early and influential adopter of CSL, and its style repository serves as the canonical collection of CSL styles. Mendeley (Elsevier) and Papers (ReadCube) also use CSL for citation formatting. Pandoc, the universal document converter, uses citeproc for processing citations in Markdown. Many academic publishers accept or recommend CSL-formatted bibliographies. The CSL style repository on GitHub contains styles for over 10,000 journals and style guides, making it one of the largest open collections of bibliographic formatting rules.
## Related Standards
No directly related standards are currently indexed.
## Further Reading
  * [CSL Specification](https://docs.citationstyles.org/en/stable/specification.html)
  * [CSL Documentation](https://docs.citationstyles.org/)
  * [CSL Styles Repository — GitHub](https://github.com/citation-style-language/styles)
  * [CSL Validator](https://validator.citationstyles.org/)


##  Resources & Links
### Specification
  * [CSL Specification ](https://docs.citationstyles.org/en/stable/specification.html)


### Documentation
  * [CSL Documentation ](https://docs.citationstyles.org/)


### Repository
  * [GitHub — CSL Styles Repository ](https://github.com/citation-style-language/styles)
  * [GitHub — CSL Schema ](https://github.com/citation-style-language/schema)


### Validator
  * [CSL Validator ](https://validator.citationstyles.org/)


### Other
  * [Zotero Style Repository — Visual CSL Browser ](https://www.zotero.org/styles)


## Details Publisher
     [CSL Community](https://citationstyles.org/) Version
    1.0.2 Created
    2004 Last Updated
    October 1, 2015 License
     [Creative Commons Attribution Share Alike 3.0 Unported](https://spdx.org/licenses/CC-BY-SA-3.0.html) CC-BY-SA-3.0 Serializations
     XML
## External
[ Official Page](https://citationstyles.org/) [ Wikipedia](https://en.wikipedia.org/wiki/Citation_Style_Language) [ Wikidata (Q824708)](https://www.wikidata.org/wiki/Q824708)
Data Quality Medium
Editorial Status Unreviewed
Indexed 2026-03-29
[![Dublin Core Metadata Initiative](https://msi.dublincore.org/dcmi-logo.svg)](https://dublincore.org)
DCMI is an organization supporting innovation in metadata design and best practices across the metadata ecology.
[![DCMI Education Committee](https://msi.dublincore.org/dcmi-education-logo.svg)](https://education.dublincore.org)
The DCMI Education Committee coordinates activities and publications that teach and inform users about current developments and technologies for metadata.
### Browse
  * [All Standards](https://msi.dublincore.org/standards)
  * [Search](https://msi.dublincore.org/search)
  * [Recently Updated](https://msi.dublincore.org/standards?sort=updated)
  * [Recently Indexed](https://msi.dublincore.org/standards?sort=indexed)


### Types
  * [Element Sets](https://msi.dublincore.org/types/element-set)
  * [Ontologies](https://msi.dublincore.org/types/ontology)
  * [Vocabularies](https://msi.dublincore.org/types/vocabulary)
  * [Data Models](https://msi.dublincore.org/types/data-model)
  * [Exchange Formats](https://msi.dublincore.org/types/exchange-format)


### Subjects
  * [Libraries](https://msi.dublincore.org/subjects/libraries)
  * [Cultural Heritage](https://msi.dublincore.org/subjects/cultural-heritage)
  * [Web & Linked Data](https://msi.dublincore.org/subjects/web)
  * [Scientific Data](https://msi.dublincore.org/subjects/scientific-data)
  * [Government](https://msi.dublincore.org/subjects/government)


### About
  * [About MSI](https://msi.dublincore.org/about)
  * [DCMI Education(opens in new tab)](https://education.dublincore.org/)
  * [DCMI(opens in new tab)](https://dublincore.org)
  * [GitHub(opens in new tab)](https://github.com/dcmi/metadata-standards-index)


Maintained by the [DCMI Education Committee](https://education.dublincore.org/).
[![Creative Commons Attribution 4.0 International License](https://msi.dublincore.org/cc-by.svg)](https://creativecommons.org/licenses/by/4.0/)
Unless indicated otherwise, DCMI documents are licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Please see the [DCMI Document Notice](https://www.dublincore.org/about/copyright/#documentnotice) for further instructions. [Copyright](https://www.dublincore.org/about/copyright/#copyright) © 1995-2026 [DCMI](https://education.dublincore.org/). All Rights Reserved. DCMI [liability](https://www.dublincore.org/about/copyright/#liability), [trademark/service mark](https://www.dublincore.org/about/copyright/#trademark), [document use rules](https://www.dublincore.org/about/copyright/#documentnotice) apply. Your interactions with this site are in accordance with our [privacy](https://www.dublincore.org/about/privacy/) statements.

