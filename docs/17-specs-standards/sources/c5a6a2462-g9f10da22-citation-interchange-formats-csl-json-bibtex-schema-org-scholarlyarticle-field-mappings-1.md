[📄 GROBID Tools](https://grobid.org/)
  * [Extractor](https://grobid.org/)
  * [Guides](https://grobid.org/guides/)
  * [Formats](https://grobid.org/formats/)
  * [About](https://grobid.org/about.html)
  * [Contact](https://grobid.org/contact.html)


# CSL-JSON as an interchange format
Last reviewed on April 24, 2026
CSL-JSON is the input format used by Citation Style Language processors. It is a JSON document — strictly, an array of items — that any CSL-compliant engine can render into a formatted citation according to a chosen style. It is also the most structured of the formats produced by the extractor and the easiest one to consume programmatically.
## Anatomy of an item

```
[
  {
    "id": "smith2023something",
    "type": "article-journal",
    "title": "Something about pdf extraction",
    "author": [
      {"family": "Smith", "given": "Jane"},
      {"family": "Doe",   "given": "John"}
    ],
    "container-title": "Journal of Document Engineering",
    "volume": "12",
    "issue": "3",
    "page": "101-120",
    "issued": {"date-parts": [[2023, 5, 14]]},
    "DOI": "10.1234/jde.2023.0012"
  }
]
```

Each object has an `id` (the equivalent of a BibTeX citation key), a `type` drawn from a fixed list, and a set of variables. The schema is published by the CSL project and is stable enough that records produced today will continue to render correctly with future style files.
## Item types
CSL has a richer type vocabulary than BibTeX. The frequently used members:
  * `article-journal` — a journal article.
  * `article-magazine`, `article-newspaper` — non-academic articles.
  * `book` and `chapter` — whole books and parts of edited collections.
  * `paper-conference` — a conference paper.
  * `thesis` — with a `genre` variable to distinguish PhD, master's, and so on.
  * `report` — institutional or technical reports.
  * `dataset`, `software` — increasingly common; supported by modern styles.
  * `webpage` — material that does not have a print equivalent.
  * `manuscript`, `personal-communication` — for unpublished or private sources.


## Names
Names are objects with `family` and `given`, and optional `suffix`, `non-dropping-particle`, and `dropping-particle` fields. For institutions, use a single-string `literal` form to stop a CSL processor from trying to split it into a personal name. Two examples:

```
{"family": "van der Waals", "given": "Johannes"}
{"literal": "World Health Organization"}
```

## Dates
Dates are objects too. The `date-parts` array can hold a single date — `[[2023, 5, 14]]` — or a range with two arrays. Year-only and year-month dates are valid. There is also a `literal` form for dates that cannot be parsed into a year, month, day structure: `{"literal": "Spring 2023"}`.
## Why CSL-JSON tends to win for interchange
  * It is JSON. Every modern programming language has first-class support for parsing it; you can pipe it through scripts without writing a custom tokenizer.
  * Its variables are typed (string, number, name, date) and named consistently. There is no ambiguity about which tag means "journal".
  * It is the format Zotero and many other tools use internally, so importing and exporting between them rarely loses information.
  * The CSL ecosystem includes a large library of style files, so once you have CSL-JSON you can render in almost any citation style without converting your data.


## Where it is less natural
  * LaTeX users usually want a `.bib` file. Going from CSL-JSON to BibTeX is straightforward but is one extra step.
  * Older reference managers and some publisher submission portals do not accept CSL-JSON yet; they expect BibTeX or RIS.
  * The schema does not natively encode every field a particular publisher might need (production codes, internal identifiers); for those, a custom layer on top is required.


## Validating output
The CSL project publishes a JSON Schema for CSL-JSON. Running the extractor's output through a validator is a cheap way to catch format-level mistakes before they reach a citation processor. Most failures come from putting a value in the wrong shape — a string where an array of name objects is expected, for instance — and the schema flags those clearly.
## Related
  * [BibTeX](https://grobid.org/formats/bibtex.html)
  * [RIS](https://grobid.org/formats/ris.html)
  * [DOIs, ArXiv IDs, and friends](https://grobid.org/guides/doi-and-identifiers.html)


[About](https://grobid.org/about.html) [Contact](https://grobid.org/contact.html) [Privacy](https://grobid.org/privacy.html) [Terms](https://grobid.org/terms.html) [Cookies](https://grobid.org/cookies.html) [Disclaimer](https://grobid.org/disclaimer.html)
© 2026 GROBID Tools. Built with PDF.js and pdf-lib running in your browser.

