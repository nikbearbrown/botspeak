# Botspeak TOC v1 — Pushback

*Written against `toc-v1.md` before any chapter is drafted.*
*Date: 2026-04-27.*
*Posture: critique, not approval. Three load-bearing concerns, ranked by how much trouble they cause if ignored.*

---

## 1. The architecture is four overlapping frameworks for a reader who has none

The TOC tells me the audience has *no prior framework*. Then it asks them to absorb four named structures by Chapter 4:

- **The Loop** — 5 named steps
- **The Three Modes** — 3 named relationships
- **The Nine Capacities** — 9 named cognitive abilities
- **The Seven Tiers** — 7 named delegation levels

That is **24 named entities** before the reader has practiced one. And they are not orthogonal — the Capacities map onto the Loop, the Tiers feed into Delegation (Loop step 2), the Modes reweight every Loop step. The architecture *says* it is layered. Reading it, it feels stacked.

A practitioner handbook earns its load-bearing vocabulary by showing it doing work the reader can't do without it. The current TOC introduces all four frameworks as definitions before the reader has felt the pain each one solves. Chapter 0 establishes one pain (the citation that wasn't). Chapter 1 names the Loop *and* the Three Modes. Chapter 2 names the Nine Capacities. Chapter 4 names the Seven Tiers. By page 80 the reader is carrying 24 names and has executed zero tasks.

**The Feynman test:** for each of the four frameworks, can I show a worked example where removing that framework loses the move, and substituting one of the other three does not recover it? If yes — the framework earns its place. If no — it's vocabulary, not machinery.

Specifically:
- Do the **Three Modes** do work the **Seven Tiers** don't already do? Tiers 1–3 ≈ Augmentation, Tiers 4–6 ≈ Automation, Tier 7 ≈ Agency. If the Tiers and the Modes are saying nearly the same thing at different granularities, one is decoration.
- Do the **Nine Capacities** do work the **Loop** doesn't? If each Capacity maps to one Loop step (the TOC promises a "Capacities-Loop mapping"), the Capacities may be the Loop steps named twice.

**Recommendation:** before /c2, do a one-page exercise where each framework has to defend its own existence against the other three. Cut what doesn't survive. A 350-page book with three frameworks that each do work is more credible than a 450-page book with four frameworks that overlap.

## 2. "Irreducibly human" is the title's load-bearing wall — and it's the most contestable claim

The book is called *The Irreducibly Human Practitioner's Guide to AI Fluency*. The thesis depends on a list of capacities that AI cannot do (the Nine Capacities, several of which sound suspiciously like they could be done by AI within the franchise's stated 12–18 month horizon). The TOC's risk section names the Chapter 12 case studies as the aging risk. That's not the aging risk. The *title* is the aging risk.

Concretely: which of the Nine Capacities are durably irreducibly human, and which are temporarily so?

- **Strategic Delegation** — durable. Requires accountability, which is a social construct AI cannot hold.
- **Effective Communication** — temporary. Already partially eroded.
- **Critical Evaluation** — *contested*. Better self-doubt and uncertainty quantification erodes this.
- **Technical Understanding** — temporary. AI explains AI better every quarter.
- **Ethical Reasoning** — durable in the sense that someone has to be on the hook. Not durable in the sense of generating ethical analysis.
- **Stochastic Reasoning** — temporary. Better calibration tools collapse this.
- **Learning by Doing** — durable. The body is a constraint AI doesn't have.
- **Rapid Prototyping** — temporary, in some domains already collapsed.
- **Theoretical Foundations** — temporary in retrieval, durable in judgment-under-disagreement.

If half the Nine are temporarily irreducible, the book's title is making a 2026 claim that may not survive 2028. That is fine — books date. But the *architecture* should price this in. The structural arguments need to be cleanly separable from the capacity-by-capacity claims, so that when GPT-7 collapses Stochastic Reasoning, the chapter on Stochastic Reasoning gets revised but the Loop survives.

Right now I cannot tell from the TOC whether that separation exists. The Nine Capacities are introduced as the cognitive vocabulary of the discipline. If three of them collapse in the next edition, does the discipline collapse with them?

**Recommendation:** in Chapter 2, classify each Capacity along a *durability axis* (durable / contested / temporarily irreducible). Make the temporarily-irreducible ones explicit. This is honest, it ages well, and it does the Feynman move of naming what we don't yet know. It is also a competitive moat — no other handbook does this and most won't.

## 3. The book is teaching adversarial validation while running an unaudited claim that "no book currently makes this claim"

The TOC asserts: *"No book currently makes this claim or provides this architecture."* That sentence is the entire defining-the-field positioning. It is the marketing claim, the proposal claim, and the franchise claim. It is unsourced.

I can think of, off the top of my head:
- *Co-Intelligence* (Mollick, 2024) — makes a structured-practice claim, names types of AI relationship, gives heuristics. Not a "Loop" but architecturally adjacent.
- *The Coming Wave* (Suleyman, 2023) — different ambition, but stakes a "containment" framework.
- The Anthropic, OpenAI, and DeepMind responsible-use guides — not books, but they have architecture, are widely read, and define vocabulary.
- ISTE's existing AI literacy frameworks for educators — also not books, but the field's existing structure.
- *How to Speak Bot* — Brown's own companion. The TOC explicitly cross-links to it. If *How to Speak Bot* doesn't already make some of *Botspeak*'s claims, the cross-link is doing nothing. If it does, "no book makes this claim" is being asserted against the author's own prior work.

A book that teaches discernment, omission, and adversarial validation cannot ship with an unaudited "no one else does this" claim. The right move is not to delete the claim — the defining-the-field positioning is real and probably correct in some narrow specification. The right move is to *specify* the claim using Chapter 3's own method:

- *No prior practitioner handbook* — what counts as a handbook?
- *for AI fluency* — fluency as defined how?
- *with this architecture* — which architectural feature is novel? The Loop? The Tiers? The Modes? The combination?

Once specified, the claim becomes defensible and the chapter on Specification has just done what it claims to teach. As written, the TOC is teaching the reader a discipline the TOC itself is not yet practicing.

**Recommendation:** before /m1 (market positioning), audit the claim against six to ten plausibly-comparable texts (Mollick, Suleyman, *How to Speak Bot*, ISTE frameworks, *AI Snake Oil*, *The Alignment Problem*, the ARIA practitioner guides, and so on). Specify what *Botspeak* does that none of them do. Make the claim narrow enough to be true.

---

## What is *not* on this pushback list (deliberately)

- **Page count.** The TOC self-flagged at OQ-L. Concur with the recommendation to accept ~400 pp. A practitioner handbook that defines a field can earn 400 pp; a thin one would underprice the work.
- **The Slot 5 live exercise instruction.** Concur. Unusual handbook formatting, defensible at production.
- **The franchise framing.** Suspicious of premature franchising before the first volume is validated, but this is a marketing decision, not an architecture decision, and the architecture survives if the franchise doesn't.

---

*The three concerns above will not be visible until chapters are drafted. By the time they're visible at the chapter level, they're expensive to fix. Worth answering now, while the TOC is still v1.*
