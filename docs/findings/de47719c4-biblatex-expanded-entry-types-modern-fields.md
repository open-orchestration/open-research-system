---
id: de47719c4
topic: 17-specs-standards
title: "biblatex extends legacy BibTeX: web-native/modern entry types (@online, @thesis, @dataset, @software) and modern fields (urldate, eprint, doi, pubstate)"
status: draft
---

This finding grounds the **modern, web-native extensions** the biblatex package adds on top
of the legacy BibTeX entry-type set, directly on the official biblatex package manual
(Philipp Lehman et al., CTAN) [c0228eaf6]. It is the modern complement to **d59d1279b**,
which grounds the *legacy* BibTeX entry types (Patashnik's btxdoc §3.1), CSL-JSON, and
schema.org. Where d59d1279b establishes what the traditional `@article`/`@book`/`@phdthesis`
btxdoc set requires, this finding establishes the entry types and fields a research system
needs to cite **websites, preprints, theses, and datasets** — sources the legacy btxdoc set
cannot model — and the compatibility seam between the two. Cross-link [d59d1279b]. Load-bearing
claims rest on the biblatex manual [c0228eaf6].

## 1. Web-native and modern entry types biblatex adds beyond legacy BibTeX

biblatex defines entry types absent from the traditional btxdoc set, of direct use to a
system that cites online and modern sources [c0228eaf6]:

- **@online** — "An online resource." It is intended for sources such as websites which are
  intrinsically online resources, and `author`, `editor`, and `year` are omissible (in terms
  of §2.3.2) [c0228eaf6]. **@electronic** is an alias for @online, and **@www** is likewise
  an alias for @online [c0228eaf6].
- **@dataset** — "A dataset or a similar collection of (mostly) raw data." [c0228eaf6]
- **@software** — "Computer software. The standard styles will treat this entry type as an
  alias for @misc." [c0228eaf6]
- **@thesis** — "A thesis written for an educational institution to satisfy the requirements
  for a degree," with the `type` field used to specify the kind of thesis [c0228eaf6].

These complement, rather than replace, the legacy types grounded in [d59d1279b]: the engine's
adapters can target a journal `@article` or a `@book` exactly as before, but now also have
first-class types for a cited webpage (@online), a cited preprint dataset (@dataset), a cited
software artifact (@software), and a thesis whose degree kind is explicit (@thesis).

## 2. Required vs. optional fields for the key modern types (verbatim from the manual)

The manual classifies each entry type's fields as **required** vs. **optional** [c0228eaf6].
The field memberships below are the de-spaced forms recovered from the manual's
whitespace-collapsed field lists, not paraphrases [c0228eaf6]:

- **@online** — Required fields: author/editor, title, year/date, doi/eprint/url. Optional
  fields: subtitle, titleaddon, language, version, note, organization, month, addendum,
  pubstate, eprintclass, eprinttype, urldate [c0228eaf6]. The manual notes that **all entry
  types support the `url` field**, and suggests that for an article from an online journal it
  may be preferable to use @article with its `url` field rather than @online [c0228eaf6].
- **@thesis** — Required fields: author, title, type, institution, year/date. Optional fields:
  subtitle, titleaddon, language, note, location, month, isbn, eid, chapter, pages, pagetotal,
  addendum, pubstate, doi, eprint, eprintclass, eprinttype, url, urldate [c0228eaf6].
- **@dataset** — Required fields: author/editor, title, year/date. Optional fields: subtitle,
  titleaddon, language, edition, type, series, number, version, note, organization, publisher,
  location, addendum, pubstate, doi, eprint, eprintclass, eprinttype, url, urldate [c0228eaf6].

Note that @thesis makes `type` and `institution` **required** — unlike legacy btxdoc, where
`@phdthesis`/`@mastersthesis` instead require `school` and treat `type` as optional
([d59d1279b] grounds that legacy shape). biblatex's **@mastersthesis** and **@phdthesis** are
each "Similar to @thesis except that the `type` field is optional and defaults to the localised
term" ('Master's thesis' / 'PhD thesis' respectively), which you may still override via `type`
[c0228eaf6].

## 3. Modern fields for citing preprints, websites, and DOIs

Beyond the legacy field vocabulary, the manual defines fields the traditional BibTeX btxdoc set
lacks, which the entry types above carry [c0228eaf6]:

- **urldate** — an access date for a `url` (appears as an optional field across @online,
  @thesis, @dataset, etc.) [c0228eaf6].
- **eprint** / **eprinttype** / **eprintclass** — for preprint/archive identifiers such as an
  arXiv id, its type, and its class [c0228eaf6].
- **doi** — a Digital Object Identifier [c0228eaf6].
- **pubstate** — publication state (e.g. forthcoming/in press) [c0228eaf6].
- **version** — a version/revision string, used by @online, @dataset, and @software's family
  [c0228eaf6].

For @online specifically, `doi/eprint/url` is part of the **required** set, so a cited online
resource cannot be expressed without at least one resolvable locator [c0228eaf6] — exactly the
identity floor a citation-gated engine wants for web sources.

## 4. Compatibility with legacy .bib files

biblatex's data model is "slightly different from traditional BibTeX"; the manual states that
such (legacy) bib files "will most likely require editing in order to work properly with this
package" [c0228eaf6]. It also defines **legacy aliases** so old types still resolve:
**@conference** is a legacy alias for @inproceedings, and **@electronic** is an alias for
@online [c0228eaf6]. These aliases are resolved by the backend as the data is processed —
biblatex and the styles see only the target type the alias points to, not the alias name, so
per-type formatting and filtering apply to the target only [c0228eaf6]. This means an engine
exporting biblatex can emit legacy aliases for interoperability while relying on the modern
target type's field model.

## 5. How this complements d59d1279b

d59d1279b pins the legacy/canonical layer — btxdoc §3.1's `@article`/`@book`/`@phdthesis`
required-field tables, CSL-JSON's closed 45-type enum, and schema.org's CreativeWork graph
[d59d1279b]. This finding adds the layer those sources do not cover well: native types for
**web pages, datasets, software, and theses with explicit degree kind**, plus the **urldate /
eprint / doi / pubstate / version** fields needed to cite preprints and online sources with
resolvable, dated locators [c0228eaf6]. Together they let the engine's import/export adapters
round-trip both a classic book and a cited arXiv preprint or webpage without losing type or
locator identity. The CSL-JSON↔biblatex type correspondences are visible at the concept level
— biblatex @online ≈ CSL `webpage`, @dataset ≈ CSL `dataset`, @software ≈ CSL `software`,
@thesis ≈ CSL `thesis` ([d59d1279b] enumerates the CSL side) — but the manual does not itself
publish a CSL crosswalk (see Gaps).

## Gaps found

- A field-level **CSL ↔ BibTeX ↔ schema.org crosswalk** (graph node g3518bee2) remains
  ungrounded; this finding is biblatex-only and does not supply that concordance — the
  concept-level type correspondences in §5 are inferred alignment, not a mapping published by
  the manual [c0228eaf6].
- The manual's per-type **optional-field lists are long**; only the entry types named here
  (@online, @thesis, @dataset) have their full required/optional lists transcribed. The PDF→
  markdown conversion **collapsed whitespace** inside these lists (rendering e.g.
  "Requiredfields:author,title,type,institution,year/date" as run-together words), so the
  field memberships above are de-spaced recoveries of those collapsed cells, not paraphrases,
  and a small risk of a dropped/merged token in a long optional list cannot be fully excluded
  without the original PDF [c0228eaf6].
