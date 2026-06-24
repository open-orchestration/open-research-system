---
id: d59d1279b
topic: 17-specs-standards
title: "Citation interchange formats: CSL-JSON type enum + required fields, BibTeX entry-type field tables, schema.org citation/ScholarlyArticle"
status: draft
---

This finding grounds the FORMAT SPECIFICS of the engine's three citation interchange
targets — CSL-JSON, BibTeX, and schema.org — directly on their official primary
specifications: the citation-style-language/schema `csl-data.json` JSON Schema
[c914e0136], Oren Patashnik's BibTeX documentation (btxdoc) §3.1 [cb94aa1ff], and the
schema.org `ScholarlyArticle` type page [c9537702a] and `citation` property page
[c4cc2cbe7]. It complements `d75f0cdee` (which establishes at a high level that
CSL-JSON, MADR, and MCP are the engine's interop seams) and `d3c246500` (MCP spec
internals) by NOT restating which formats are chosen, and instead supplying the exact
item-type enumerations, required-vs-optional field tables, host/value types, and a
cross-format concordance the engine's import/export adapters must be built against.

## 1. CSL-JSON: a closed item-type enumeration with only two required fields per item

The CSL-JSON input schema fixes a **closed enumeration of exactly 45 item types** on the
`type` property [c914e0136]. The full set is: `article`, `article-journal`,
`article-magazine`, `article-newspaper`, `bill`, `book`, `broadcast`, `chapter`,
`classic`, `collection`, `dataset`, `document`, `entry`, `entry-dictionary`,
`entry-encyclopedia`, `event`, `figure`, `graphic`, `hearing`, `interview`,
`legal_case`, `legislation`, `manuscript`, `map`, `motion_picture`, `musical_score`,
`pamphlet`, `paper-conference`, `patent`, `performance`, `periodical`,
`personal_communication`, `post`, `post-weblog`, `regulation`, `report`, `review`,
`review-book`, `software`, `song`, `speech`, `standard`, `thesis`, `treaty`, and
`webpage` [c914e0136]. Representative bibliographic types for a research engine include
`article-journal`, `book`, `chapter`, `paper-conference`, `dataset`, `webpage`, `report`,
`software`, and `thesis` [c914e0136].

Per item, the schema's `required` array lists exactly two members: `["type", "id"]`
[c914e0136]. Every other variable — the standard string variables and the structured
sub-objects below — is optional, so the minimal valid CSL-JSON item carries only a type
drawn from the 45-type enum and an identifier [c914e0136].

The variable system has two structured sub-object shapes beyond plain string variables.
Name variables (e.g. `author`) are objects carrying parts such as `family` and `given`
[c914e0136]. Date variables are objects whose canonical representation uses a
`date-parts` array [c914e0136]. The schema defines these as the reusable `name-variable`
and `date-variable` types referenced by the corresponding properties [c914e0136].

## 2. BibTeX: the standard entry types and their required/optional fields (btxdoc §3.1)

btxdoc §3.1 divides each entry type's fields into three classes — **required** (omitting
produces a warning and, rarely, a badly formatted entry; if the required information is
not meaningful, you are using the wrong entry type), **optional** (used if present, can
be omitted without formatting problems), and **ignored** (any field that is neither
required nor optional) [cb94aa1ff]. The standard entry types and their fields, verbatim
from §3.1 [cb94aa1ff]:

- **`article`** — required: author, title, journal, year. optional: volume, number,
  pages, month, note. [cb94aa1ff]
- **`book`** — required: author or editor, title, publisher, year. optional: volume or
  number, series, address, edition, month, note. [cb94aa1ff]
- **`booklet`** — required: title. optional: author, howpublished, address, month, year,
  note. [cb94aa1ff]
- **`conference`** — the same as `inproceedings`, included for Scribe compatibility.
  [cb94aa1ff]
- **`inbook`** — required: author or editor, title, chapter and/or pages, publisher,
  year. optional: volume or number, series, type, address, edition, month, note.
  [cb94aa1ff]
- **`incollection`** — required: author, title, booktitle, publisher, year. optional:
  editor, volume or number, series, type, chapter, pages, address, edition, month, note.
  [cb94aa1ff]
- **`inproceedings`** — required: author, title, booktitle, year. optional: editor,
  volume or number, series, pages, address, month, organization, publisher, note.
  [cb94aa1ff]
- **`manual`** — required: title. optional: author, organization, address, edition,
  month, year, note. [cb94aa1ff]
- **`mastersthesis`** — required: author, title, school, year. optional: type, address,
  month, note. [cb94aa1ff]
- **`misc`** — required: none. optional: author, title, howpublished, month, year, note.
  [cb94aa1ff]
- **`phdthesis`** — required: author, title, school, year. optional: type, address,
  month, note. [cb94aa1ff]
- **`proceedings`** — required: title, year. optional: editor, volume or number, series,
  address, month, organization, publisher, note. [cb94aa1ff]
- **`techreport`** — required: author, title, institution, year. optional: type, number,
  address, month, note. [cb94aa1ff]
- **`unpublished`** — required: author, title, note. optional: month, year. [cb94aa1ff]

(Conversion note: the markitdown rendering of btxdoc ran several field words together —
e.g. "Requiredfields:" and the `inproceedings`/`proceedings`/`techreport` field lists
were split across fragmented table cells. The field memberships listed above are the
canonical de-spaced forms recovered from those cells, not paraphrases — `techreport`'s
"Requiredfields: author,title,institution,year" is rendered here as the four fields
author/title/institution/year [cb94aa1ff].)

In addition to the fields above, every entry type also accepts an optional `key` field,
used in some styles for alphabetizing, cross referencing, or forming a `\bibitem` label;
this `key` field is distinct from the citation key in the `\cite` command [cb94aa1ff].

**crossref field inheritance.** The standard styles support a cross-referencing feature:
a cross-referencing entry `\cite`s the cross-referenced entry (named via its `crossref`
field, whose value is the database key of the entry being cross referenced) and omits
fields that appear in the cross-referenced entry, which the cross-referenced entry then
supplies [cb94aa1ff]. §3.1 enumerates five such inheritance situations: (1) an
`inproceedings` (or `conference`) cross-referencing a `proceedings`; (2) a `book`, (3) an
`inbook`, or (4) an `incollection` cross-referencing a `book` (the cross-referencing
entry being a single volume of a multi-volume work); and (5) an `article`
cross-referencing an `article` — there being no `journal` entry type [cb94aa1ff].

## 3. schema.org: the `citation` property and the ScholarlyArticle type

The schema.org `citation` property is defined as "A citation or reference to another
creative work, such as another publication, web page, scholarly article, etc." [c4cc2cbe7].
Its values are expected to be one of two types — `CreativeWork` or `Text` — and it is
used on the `CreativeWork` type [c4cc2cbe7].

`ScholarlyArticle` sits in the type hierarchy
`Thing > CreativeWork > Article > ScholarlyArticle` and is defined simply as "A scholarly
article" [c9537702a]. Because it descends from `CreativeWork` (via `Article`), it inherits
the bibliographically relevant properties defined higher in the chain — including
`citation`, `author`, `datePublished`, `publisher`, `isPartOf`, `pagination`, `pageStart`,
`pageEnd`, `identifier`, `sameAs`, `url`, `abstract`, and `name`, alongside `Article`'s own
`headline` — exposed on its page under the "Properties from Thing", "Properties from
CreativeWork", and "Properties from Article" sections [c9537702a].

## 4. Cross-format concordance

The same bibliographic concept maps across the three formats, which is what lets a cited
source round-trip between them:

| Concept | BibTeX entry type | CSL-JSON `type` | schema.org type |
| --- | --- | --- | --- |
| Journal article | `@article` [cb94aa1ff] | `article-journal` [c914e0136] | `ScholarlyArticle` (Thing > CreativeWork > Article > ScholarlyArticle) [c9537702a] |
| Conference paper | `@inproceedings` / `@conference` [cb94aa1ff] | `paper-conference` [c914e0136] | `Article` / `CreativeWork` [c9537702a] |
| Doctoral thesis | `@phdthesis` [cb94aa1ff] | `thesis` [c914e0136] | `CreativeWork` [c9537702a] |
| Book | `@book` [cb94aa1ff] | `book` [c914e0136] | `CreativeWork` [c9537702a] |
| Technical report | `@techreport` [cb94aa1ff] | `report` [c914e0136] | `CreativeWork` [c9537702a] |

The identifier semantics also align: BibTeX's citation key, CSL-JSON's required `id`
[c914e0136], and schema.org's `identifier` on `CreativeWork` [c9537702a] all anchor a
reference, and a reference-to-another-work relation is carried by schema.org's `citation`
property whose value is itself a `CreativeWork` or `Text` [c4cc2cbe7].

**Why this matters for a citation-gated engine.** Because every finding is gated on cited
sources, the engine's stored citations must survive export and re-import without losing
the type distinction or required identity. CSL-JSON pins this hardest — a closed 45-type
enum and a two-field `["type","id"]` floor [c914e0136] — so it is the natural canonical
store, while BibTeX's per-entry required-field tables [cb94aa1ff] and schema.org's
`CreativeWork`/`citation` graph [c4cc2cbe7][c9537702a] define what a faithful round-trip to
each external format must preserve.
