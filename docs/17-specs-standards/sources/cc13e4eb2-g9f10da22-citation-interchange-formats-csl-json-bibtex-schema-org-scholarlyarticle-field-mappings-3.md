[![](https://twineconvert.com/_next/image?url=%2Flogo.png&w=96&q=75)twineconvert](https://twineconvert.com/)[Tools](https://twineconvert.com/all-tools)[Privacy](https://twineconvert.com/#privacy)[Why in-browser](https://twineconvert.com/#why)[FAQ](https://twineconvert.com/#faq)[Browse all](https://twineconvert.com/all-tools)
  1. [Home](https://twineconvert.com/)
  2. /
  3. [Blog](https://twineconvert.com/blog)


# BibTeX vs RIS vs CSL-JSON: which citation format to use in 2026
Three formats, each dominant in a different ecosystem. The honest comparison and the migration paths between them.
May 26, 2026 · 4 min read
If you do any research writing, you have to pick a bibliography format at some point. The three serious options are BibTeX, RIS, and CSL-JSON. They all carry the same kind of data; they all have a specific cultural home.
## BibTeX
**Created** : 1985 by Oren Patashnik for LaTeX.
**Owned by** : the LaTeX/academic-writing ecosystem.
**Looks like** :

```
@article{smith2024,
  author = {Smith, John and Doe, Jane},
  title  = {A Sample Paper},
  journal = {Nature},
  year   = {2024},
  volume = {123},
  pages  = {45-67},
  doi    = {10.1038/sample.2024.001},
}

```

**Use when** :
  * You write papers in LaTeX
  * Your bibliography manager is JabRef, Zotero (with the Better BibTeX plugin), or any LaTeX-aware tool
  * You collaborate with mathematicians, physicists, computer scientists (who mostly use LaTeX)


**Avoid when** :
  * You collaborate with humanities researchers (who mostly use Word + Zotero + CSL styles)
  * Your target tool is a modern web-based reference manager (CSL-JSON works better there)


## RIS
**Created** : 1980s by Research Information Systems (the company that became ProCite, then bought by ResearchSoft, then by Thomson Reuters).
**Owned by** : the legacy reference-manager ecosystem (EndNote, ProCite, Reference Manager).
**Looks like** :

```
TY  - JOUR
AU  - Smith, John
AU  - Doe, Jane
TI  - A Sample Paper
JO  - Nature
PY  - 2024
VL  - 123
SP  - 45
EP  - 67
DO  - 10.1038/sample.2024.001
ER  - 

```

**Use when** :
  * You use EndNote, ProCite, or Reference Manager
  * You are exporting from PubMed (which exports natively to RIS)
  * You are exchanging citation data with someone in the biomedical or life sciences community (where EndNote remains dominant)


**Avoid when** :
  * You work in LaTeX (BibTeX is the natural home)
  * Your tool offers CSL-JSON as an alternative (it is more modern and structurally cleaner)


## CSL-JSON
**Created** : 2010s by the Citation Style Language project (the same group that makes CSL styles for Zotero/Mendeley/Pandoc).
**Owned by** : the modern web-based ecosystem (Zotero, Pandoc, Mendeley).
**Looks like** :

```
[
  {
    "id": "smith2024",
    "type": "article-journal",
    "title": "A Sample Paper",
    "author": [
      { "family": "Smith", "given": "John" },
      { "family": "Doe", "given": "Jane" }
    ],
    "issued": { "date-parts": [[2024]] },
    "container-title": "Nature",
    "volume": "123",
    "page": "45-67",
    "DOI": "10.1038/sample.2024.001"
  }
]

```

**Use when** :
  * You use Zotero or Pandoc
  * You want to write bibliographies in Markdown documents (Pandoc accepts CSL-JSON as `--bibliography`)
  * You are building anything programmatic that consumes citation data (CSL-JSON is the cleanest structured form)


**Avoid when** :
  * Your tool does not support it (most LaTeX workflows want BibTeX; most EndNote workflows want RIS)
  * You are sending the file to a colleague who has never heard of CSL-JSON (BibTeX or RIS is more recognizable)


## The honest comparison
| Property | BibTeX | RIS | CSL-JSON | |---|---|---|---| | Age | 40 years | 40 years | 12 years | | Encoding | LaTeX-escaped (\'e) | Plain text | JSON (UTF-8) | | Author format | "Last, First and Last, First" | One author per AU line | Structured  objects | | Date format | Year integer + month string | Year integer | date-parts array | | Field richness | ~30 standard fields | ~30 standard tags | 80+ CSL fields | | Comments | Yes (with @comment) | No standard | No (JSON has none) | | Cross-references | Yes (crossref =) | No | No | | Best in | LaTeX | EndNote/ProCite | Zotero/Pandoc/web |
## The migration matrix
Where do you go from where?
  * **From BibTeX** : [BibTeX → CSL-JSON](https://twineconvert.com/bibtex-to-csl-json) is the easiest path; structured cleanly. [BibTeX → RIS](https://twineconvert.com/bibtex-to-ris) loses a little (no crossref support in RIS) but works.
  * **From RIS** : [RIS → BibTeX](https://twineconvert.com/ris-to-bibtex) for LaTeX users. RIS → CSL-JSON is not yet a direct converter we ship (the workaround is RIS → BibTeX → CSL-JSON, which loses minor RIS-specific fields).
  * **From CSL-JSON** : [CSL-JSON → BibTeX](https://twineconvert.com/csl-json-to-bibtex) preserves the core fields. Going to RIS requires the same two-step pivot.


In every conversion, the core fields (title, authors, year, journal, DOI) survive cleanly. The lossage is in metadata that one format supports and another does not. For most users, that loss is acceptable.
## What I would actually pick if starting fresh
For a thesis, a paper, or any long-form academic writing:
  * **If you write in LaTeX** : BibTeX. The whole ecosystem assumes it.
  * **If you write in Word with Zotero** : CSL-JSON internally, export to BibTeX when you need to share with a LaTeX collaborator.
  * **If you write in Markdown with Pandoc** : CSL-JSON natively.
  * **If you write in EndNote** : RIS for exchange, EndNote's native `.enl` library for daily work.


The format you use day-to-day matters less than picking one and being consistent. The conversion tools (ours and others) make migration cheap when you need it; what is expensive is having half your library in one format and half in another, with no clear authoritative source.
## Related converters
  * [BibTeX → CSL-JSON /bibtex-to-csl-json](https://twineconvert.com/bibtex-to-csl-json)
  * [BibTeX → RIS /bibtex-to-ris](https://twineconvert.com/bibtex-to-ris)
  * [RIS → BibTeX /ris-to-bibtex](https://twineconvert.com/ris-to-bibtex)

[← All posts](https://twineconvert.com/blog)
![](https://twineconvert.com/_next/image?url=%2Flogo.png&w=48&q=75)twineconvert
Convert files in your browser. Nothing uploaded. No signup. No file size limit.
[![Buy me a coffee](https://twineconvert.com/buy-me-a-coffee.png)](https://buymeacoffee.com/twineconvert)
### Image
  * [HEIC to JPG](https://twineconvert.com/heic-to-jpg)
  * [PNG to WebP](https://twineconvert.com/png-to-webp)
  * [JPG to PNG](https://twineconvert.com/jpg-to-png)
  * [WebP to PNG](https://twineconvert.com/webp-to-png)
  * [PNG to ICO](https://twineconvert.com/png-to-ico)


### Document
  * [PDF to JPG](https://twineconvert.com/pdf-to-jpg)
  * [JPG to PDF](https://twineconvert.com/jpg-to-pdf)
  * [DOCX to PDF](https://twineconvert.com/docx-to-pdf)
  * [PDF to DOCX](https://twineconvert.com/pdf-to-docx)
  * [Compress PDF](https://twineconvert.com/compress-pdf)


### Audio · Video
  * [MP4 to MP3](https://twineconvert.com/mp4-to-mp3)
  * [MOV to MP4](https://twineconvert.com/mov-to-mp4)
  * [WAV to MP3](https://twineconvert.com/wav-to-mp3)
  * [MP4 to GIF](https://twineconvert.com/mp4-to-gif)
  * [GIF to MP4](https://twineconvert.com/gif-to-mp4)


### Pro · Niche
  * [OFX to CSV](https://twineconvert.com/ofx-to-csv)
  * [Apple Health export](https://twineconvert.com/apple-health-to-csv)
  * [IFC quantity takeoff](https://twineconvert.com/ifc-to-csv)
  * [GEDCOM to CSV](https://twineconvert.com/gedcom-to-csv)
  * [Embroidery DST/PES](https://twineconvert.com/dst-to-pes)


© 2026 twineconvert. Every conversion runs in your browser.
[All tools](https://twineconvert.com/all-tools)[About](https://twineconvert.com/about)[Privacy](https://twineconvert.com/privacy)[Terms](https://twineconvert.com/terms)

