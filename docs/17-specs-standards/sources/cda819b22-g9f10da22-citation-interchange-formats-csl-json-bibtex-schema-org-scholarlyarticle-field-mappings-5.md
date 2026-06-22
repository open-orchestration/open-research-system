  * [Zotero](https://www.zotero.org/)
  * [Groups](https://www.zotero.org/groups/)
  * [Documentation](https://www.zotero.org/support/)
  * [Forums](https://www.zotero.org/support/kb/field_mappings)
  * [Get Involved](https://www.zotero.org/getinvolved)
  * [Log In](https://www.zotero.org/user/login/)
  * [Sign Up](https://www.zotero.org/user/register/)
  * [Upgrade Storage](https://www.zotero.org/storage)


[ ![Zotero](https://www.zotero.org/static/images/bs4theme/zotero-logo.1775160902.svg) ](https://www.zotero.org/)
  * [Groups](https://www.zotero.org/groups/)
  * [Documentation](https://www.zotero.org/support/)
  * [Forums](https://forums.zotero.org/discussions)
  * [Get Involved](https://www.zotero.org/getinvolved)
  * [Log In](https://www.zotero.org/user/login/)
  * [Upgrade Storage](https://www.zotero.org/storage)


  * [Home](https://www.zotero.org/support/)
  * Getting Started
    * [Installation](https://www.zotero.org/support/installation)
    * [Quick Start Guide](https://www.zotero.org/support/quick_start_guide)
    * [System Requirements](https://www.zotero.org/support/system_requirements)
    * [Frequently Asked Questions](https://www.zotero.org/support/frequently_asked_questions)
    * [Version History](https://www.zotero.org/support/changelog)
  * Adding to Your Library
    * [Adding Items](https://www.zotero.org/support/adding_items_to_zotero)
    * [Adding Files](https://www.zotero.org/support/attaching_files)
    * [Feeds](https://www.zotero.org/support/feeds)
    * [Retrieve PDF Metadata](https://www.zotero.org/support/retrieve_pdf_metadata)
    * [Importing from Other Tools](https://www.zotero.org/support/moving_to_zotero)
  * Organizing & Taking Notes
    * [Collections and Tags](https://www.zotero.org/support/collections_and_tags)
    * [Searching](https://www.zotero.org/support/searching)
    * [Sorting](https://www.zotero.org/support/sorting)
    * [PDF Reader](https://www.zotero.org/support/pdf_reader)
    * [Notes](https://www.zotero.org/support/notes)
    * [Related Items](https://www.zotero.org/support/related)
    * [Duplicate Detection](https://www.zotero.org/support/duplicate_detection)
  * Citations & Bibliographies
    * [Creating Bibliographies](https://www.zotero.org/support/creating_bibliographies)
    * [Word Processor Integration](https://www.zotero.org/support/word_processor_integration)
    * [Citation Styles](https://www.zotero.org/support/styles)
    * [Reports](https://www.zotero.org/support/reports)
  * Syncing & Collaboration
    * [Data and File Syncing](https://www.zotero.org/support/sync)
    * [Groups](https://www.zotero.org/support/groups)
    * [My Publications](https://www.zotero.org/support/my_publications)
  * Preferences
    * [Preferences](https://www.zotero.org/support/preferences)
    * [Connector Preferences](https://www.zotero.org/support/connector_preferences)
    * [Languages](https://www.zotero.org/support/supported_languages)
  * [Knowledge Base](https://www.zotero.org/support/kb)
  * Troubleshooting
    * [Getting Help](https://www.zotero.org/support/getting_help)
    * [Library Data Issues](https://www.zotero.org/support/zotero_data)
    * [Web Saving Issues](https://www.zotero.org/support/troubleshooting_translator_issues)
    * [Word Processor Plugin Issues](https://www.zotero.org/support/word_processor_plugin_troubleshooting)
    * [Data Sync Issues](https://www.zotero.org/support/kb/changes_not_syncing)
    * [File Sync Issues](https://www.zotero.org/support/kb/files_not_syncing)
    * [File Handling Issues](https://www.zotero.org/support/kb/file_handling_issues)
  * [Developers](https://www.zotero.org/support/dev)


## Import/Export Field Mappings[#](https://www.zotero.org/support/kb/field_mappings#importexport_field_mappings "Permanent link")
Zotero can import and export data in various bibliographic standards. This page links to mappings between Zotero fields and various standards.
**Please note:** Import/export is not recommended for [transferring entire Zotero libraries](https://www.zotero.org/support/kb/transferring_a_library) between systems, and, if you use Zotero’s word processor plugins, links to Zotero items from existing word processor documents will be lost after an export/import.
Also note that Zotero and most of the formats listed on this page are in active development, which may mean that linked information becomes outdated from time to time. You can always test current field mappings by exporting the sample items from the [devTesting Group Library](https://www.zotero.org/groups/183462/devtesting/items/collectionKey/97FH6RRU). You can also see the relevant translator files at the [Zotero Translators GitHub repo](https://github.com/zotero/translators/).
#### Data loss during import/export[#](https://www.zotero.org/support/kb/field_mappings#data_loss_during_importexport "Permanent link")
Different standards vary in the degree to which they are compatible with Zotero. Zotero RDF is in general the least lossy export format. (books, articles, journals, etc.). It is the only format that preserves information about item collections, attachment files, and notes. RIS or MODS will import/export notes (but not attachment files or collections). Other colelctions will only include data about Zoterotem metadata fields (not collections, attachment files, or notes).
#### Export format field mappings and documentation[#](https://www.zotero.org/support/kb/field_mappings#export_format_field_mappings_and_documentation "Permanent link")
Field mappings for most Zotero export types are listed [here](https://github.com/aurimasv/zotero-import-export-formats).
Mappings between Zotero types/fields and Citation Style Language (CSL) types/fields are also listed [here](https://aurimasv.github.io/z2csl/typeMap.xml).
Documentation is available for the [RIS](https://en.wikipedia.org/wiki/RIS_\(file_format\)), [MODS](http://www.loc.gov/standards/mods//mods-outline.html), [ReferBibIX](http://sti15.com/bib/formats/refer.html), [Unqualified Dublic Core RDF](http://dublincore.org/documents/dcmi-terms/), [BibTeX](http://www.bibtex.org/Format/), [BibLaTeX](http://ctan.math.washington.edu/tex-archive/macros/latex/contrib/biblatex/doc/biblatex.pdf), [Bibliontology RDF](http://bibliontology.com/), [COinS](https://www.google.be/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwjxoc68vNLXAhUMthoKHai3BusQFgg_MAM&url=https%3A%2F%2Farchive.is%2FdGBd&usg=AOvVaw06rReD7TcTdcTFIoPsiGUu), [RefWorks](https://www.refworks.com/refworks/help/refworks_tagged_format.htm), and [Wikipedia Citation](http://en.wikipedia.org/wiki/Citation_templates) formats.
On this page
  * [Import/Export Field Mappings](https://www.zotero.org/support/kb/field_mappings#importexport_field_mappings)
    * [Data loss during import/export](https://www.zotero.org/support/kb/field_mappings#data_loss_during_importexport)
    * [Export format field mappings and documentation](https://www.zotero.org/support/kb/field_mappings#export_format_field_mappings_and_documentation)


Last updated 2017-11-22
[ Edit on GitHub ](https://github.com/zotero/zotero-docs/edit/main/content/kb/field_mappings.md)
  * [Documentation](https://www.zotero.org/support/)
  * [Forums](https://forums.zotero.org/)
  * [Blog](https://www.zotero.org/blog/)
  * [Privacy](https://www.zotero.org/support/privacy)
  * [Terms of Service](https://www.zotero.org/support/terms/terms_of_service)
  * [Get Involved](https://www.zotero.org/getinvolved/)
  * [Developers](https://www.zotero.org/support/dev/start)
  * [Jobs](https://www.zotero.org/jobs)


  * Follow us
  * [![Mastodon icon](https://www.zotero.org/static/images/icons/mastodon-logo-white.svg)](https://fosstodon.org/@zotero/)


Zotero is a project of [Digital Scholar](http://digitalscholar.org/), a nonprofit organization dedicated to the development of software and services for researchers and cultural heritage institutions, and is developed by a [global community](https://www.zotero.org/support/credits_and_acknowledgments).

