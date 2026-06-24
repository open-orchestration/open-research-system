---
id: d6432467b
topic: 10-context-prompt-engineering
title: "Chain of Draft: Primary-Source Numbers for Token-Budget Reasoning (Upgrading a Blog-Relayed Claim)"
status: draft
---

# Chain of Draft: Primary-Source Numbers for Token-Budget Reasoning (Upgrading a Blog-Relayed Claim)

## Why this finding exists

The promoted prompting-ladder finding [d0cce1cec] lists Chain-of-Draft as a cheaper
middle rung but only blog-relayed: "Chain-of-Draft is reported to match CoT accuracy at
75-80% fewer tokens … (blog-relayed; benchmark before committing)" [d0cce1cec]. This
finding upgrades that single claim to its **primary source** — Xu, Xie, Zhao & He (Zoom
Communications), "Chain of Draft: Thinking Faster by Writing Less" (arXiv:2502.18600)
[c810db9f5] — replacing the relayed range with the paper's actual GSM8K table, its real
prompt mechanism, and the honest accuracy/token tradeoff that the blog framing flattened.

## 1. What Chain of Draft is, and how the prompt differs from CoT

Chain of Draft (CoD) is a prompting paradigm in which the LLM generates *minimalistic yet
informative* intermediate reasoning steps instead of the verbose step-by-step narration of
Chain-of-Thought (CoT) [c810db9f5]. The design is inspired by how humans jot down concise
drafts — capturing only the essential intermediate result of each step — rather than
writing out fully-formed sentences [c810db9f5].

The prompt mechanism is a single added instruction: keep a **minimum draft for each
thinking step, with five words at most** [c810db9f5]. Critically, the paper states this
word limit is **NOT enforced** — it is only a general guideline to promote brevity, not a
hard constraint the decoder checks [c810db9f5]. So CoD is a pure prompting technique: same
model, same single forward pass as CoT, only the reasoning-format instruction changes
[c810db9f5].

## 2. What the GSM8K table actually shows (Table 1, verified clean)

On GSM8K the paper reports, for two frontier models, accuracy / tokens / latency under CoT
vs CoD [c810db9f5]:

| Model | Method | Accuracy | Tokens | Latency |
| --- | --- | --- | --- | --- |
| GPT-4o | CoT | 95.4% | 205.1 | 4.2s |
| GPT-4o | CoD | 91.1% | 43.9 | 1.0s |
| Claude 3.5 Sonnet | CoT | 95.8% | 190.0 | 3.1s |
| Claude 3.5 Sonnet | CoD | 91.4% | 39.8 | 1.6s |

All eight values were byte-confirmed whitespace-insensitively in the source (each appears
exactly once) [c810db9f5].

The honest reading: **on GSM8K, CoD is slightly *below* CoT, not above.** Accuracy drops
about 4 percentage points (GPT-4o 95.4% → 91.1%; Claude 3.5 Sonnet 95.8% → 91.4%) in
exchange for an ~79–81% cut in output tokens (205.1 → 43.9 ≈ 79% fewer; 190.0 → 39.8 ≈ 79%
fewer) and a large latency reduction (GPT-4o 4.2s → 1.0s; Claude 3.5 Sonnet 3.1s → 1.6s)
[c810db9f5]. This is a token/latency-for-accuracy trade on this benchmark, not a free lunch
— which sharpens the vaguer blog-relayed "match CoT accuracy at 75-80% fewer tokens" of
[d0cce1cec].

## 3. The "7.6% of tokens" figure is an across-task minimum, not a GSM8K number

The abstract's headline is that CoD matches or surpasses CoT in accuracy "while using as
little as only 7.6% of the tokens, significantly reducing cost and latency" [c810db9f5].
The phrase "as little as" marks this as the paper's **minimum token usage observed across
its evaluated tasks**, not the GSM8K result — on GSM8K the reduction is ~79% (i.e., ~21% of
tokens remain), well above 7.6% [c810db9f5]. Attribute 7.6% only as the across-task floor,
never as the GSM8K figure.

The "matches or surpasses" in the abstract is likewise an across-benchmark claim: CoD
trails CoT by ~4pp on GSM8K but the paper reports it surpassing CoT on some other tasks
[c810db9f5]. The paper evaluates additional task families — commonsense reasoning
(BIG-bench date understanding and sports understanding) and other arithmetic/symbolic
reasoning — but their per-task result tables did not survive the PDF→markdown conversion
cleanly, so their specific numbers are not transcribed here (see Gaps) [c810db9f5].

## 4. How this upgrades the blog-relayed claim in d0cce1cec

[d0cce1cec] correctly flagged its CoD claim as blog-relayed via [cc90d07d5] and told the
reader to "benchmark before committing" [d0cce1cec]. This finding discharges that caveat for
the GSM8K case with primary numbers:

- **Token reduction:** the blog's "75-80% fewer tokens" is consistent with the primary
  GSM8K result (~79%) [c810db9f5][d0cce1cec].
- **Accuracy:** the blog's "match CoT accuracy" is too generous for GSM8K specifically — the
  primary table shows a ~4pp drop, with parity-or-better being an across-task abstract claim,
  not the GSM8K outcome [c810db9f5].
- **Mechanism:** the operative prompt is the unenforced "five words at most per step" draft
  instruction — a detail the ladder finding did not carry [c810db9f5].

## 5. When CoD is the right rung of the prompting ladder

CoD sits where you want most of CoT's reasoning benefit at a fraction of CoT's output cost
and latency, and can absorb a small accuracy hit — e.g. interactive or latency-bound
reasoning where CoT's full chain is too slow or too expensive [c810db9f5]. Where a ~4pp
accuracy difference on hard arithmetic is unacceptable, full CoT (or a higher rung) remains
the choice [c810db9f5]. This complements the ladder's escalation logic in [d0cce1cec]:
default low, and reach for CoD as the cost-aware variant of CoT before escalating to
self-consistency or tree-of-thoughts [d0cce1cec].

## Gaps found

- **Per-task numbers beyond GSM8K are not transcribed.** The commonsense (BIG-bench date /
  sports understanding) and other arithmetic/symbolic result tables are garbled in the
  PDF→markdown source; their cells fragment across markdown pipes and could not be read
  whitespace-insensitively with confidence, so no values from them are quoted [c810db9f5].
- **Which task hits the 7.6% floor is not isolated here.** The abstract gives 7.6% as the
  across-task minimum but the per-task token table that would pin it to a specific benchmark
  is among the garbled tables [c810db9f5].
- **Reported limitations not transcribed.** The paper's discussion of where CoD degrades
  (e.g. on smaller models or in zero-shot settings, as widely summarized) could not be
  cleanly re-grepped from the converted bytes and is therefore omitted rather than
  paraphrased [c810db9f5].
