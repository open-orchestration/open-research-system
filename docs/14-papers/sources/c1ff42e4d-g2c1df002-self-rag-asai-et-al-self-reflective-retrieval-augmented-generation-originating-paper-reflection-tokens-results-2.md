[**OpenReview**.net](https://openreview.net/)
[**OpenReview**.net](https://openreview.net/)
[Login](https://openreview.net/login)
[**OpenReview**.net](https://openreview.net/)
[Login](https://openreview.net/login)
×
### BibTeX Record
_Click anywhere on the box above to highlight complete record_
Done
[![back arrow](https://openreview.net/images/arrow_left.svg)Go to **NeurIPS 2023 Workshop Instruction** homepage](https://openreview.net/group?id=NeurIPS.cc/2023/Workshop/Instruction "Venue Homepage")
## Self-RAG: Self-reflective Retrieval Augmented Generation
[![Download PDF](https://openreview.net/images/pdf_icon_blue.svg)](https://openreview.net/pdf?id=jbNjgmE0OP "Download PDF")
### [Akari Asai](https://openreview.net/profile?id=~Akari_Asai2 "~Akari_Asai2"), [Zeqiu Wu](https://openreview.net/profile?id=~Zeqiu_Wu1 "~Zeqiu_Wu1"), [Yizhong Wang](https://openreview.net/profile?id=~Yizhong_Wang2 "~Yizhong_Wang2"), [Avirup Sil](https://openreview.net/profile?id=~Avirup_Sil1 "~Avirup_Sil1"), [Hannaneh Hajishirzi](https://openreview.net/profile?id=~Hannaneh_Hajishirzi1 "~Hannaneh_Hajishirzi1")
Published: 28 Oct 2023, Last Modified: 25 Nov 2023Instruction Workshop @ NeurIPS 2023Everyone[Revisions](https://openreview.net/revisions?id=jbNjgmE0OP)[BibTeX](https://openreview.net/forum?id=jbNjgmE0OP)
**Keywords:** Language Models, Retrieval-augmented Language Models, Retrieval Augmentation, Factuality
**TL;DR:** Our new framework Self-RAG enhances the quality and factuality of instruction-tuned LLMs with on-demand retrieval and self-reflection.
**Abstract:**
Scaling up language models (LMs) or instruction tuning has shown limited effects on improving factuality of LM outputs. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments Language Models (LMs) with retrieval, decreases hallucination issues of large LMs. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes instruction-following LM versatility or can lead to unhelpful response generation. In this work, we introduce a new framework called **Self-Reflective Retrieval-Augmented Generation (Self-RAG)** that enhances an LM's quality and factuality through retrieval and self-reflection. Our framework trains a single arbitrary LM to learn to adaptively retrieve passages on-demand, and generate and reflect on retrieved passages and its own generations using special tokens, called _reflection_ tokens, on diverse instruction-tuning data with interleaving retrieved passages and reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art pre-trained and instruction-follwing LLMs and retrieval-augmented models on a diverse set of tasks. Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, fact verification and reasoning tasks, and it shows significant gains in factuality scores and citation accuracy for long-form generations relative to these models.
**Submission Number:** 66
Loading
[About OpenReview](https://openreview.net/about)
[Contact](https://openreview.net/contact)
[FAQ](https://docs.openreview.net/getting-started/frequently-asked-questions)
[Hosting a Venue](https://openreview.net/group?id=OpenReview.net/Support)
[Sponsors](https://openreview.net/sponsors)
[Terms of Use](https://openreview.net/legal/terms) / [Privacy Policy](https://openreview.net/legal/privacy)
[All Venues](https://openreview.net/venues)
[**Donate**](https://openreview.net/donate)
[News](https://openreview.net/group?id=OpenReview.net/News&referrer=\[Homepage\]\(/\))
[OpenReview](https://openreview.net/about) is a long-term project to advance science through improved peer review with legal nonprofit status. We gratefully acknowledge the support of the [OpenReview Sponsors](https://openreview.net/sponsors). © 2026 OpenReview

