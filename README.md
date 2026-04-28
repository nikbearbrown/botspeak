# Botspeak: An Irreducibly Human Practitioner's Guide to AI Fluency

**Author:** Nik Bear Brown, PhD (Northeastern University, College of Engineering)
**Status:** Rough first-pass drafts complete (April 2026). Not yet reviewed. Not published.
**Companion volume:** *How to Speak Bot* (Brown, existing) — pattern reference companion.
**Series:** First volume of the *Botspeak* series. Domain volumes (*Botspeak for Educators*, *Botspeak for Designers*, *Botspeak for Healthcare*, …) deferred to future editions.

---

## What this book is

A practitioner handbook for recent graduates entering AI-saturated workplaces. Fourteen chapters that take the reader from *I can use a chatbot but my outputs are worse than my colleagues' and I don't know why* to *I can specify, delegate, converse, discern, and diligently maintain AI-assisted work — and defend each of those decisions to a stakeholder*.

The book defines AI fluency as a teachable practitioner discipline with a replicable structure: the **Loop** (five workflow steps — Specification, Delegation, Conversation, Discernment, Diligence), the **Three Modes** (Augmentation, Automation, Agency — three relationships between human and AI), the **Nine Capacities** (the cognitive abilities the Loop draws on), and the **Seven Tiers** (a delegation-diagnostic taxonomy). No prior practitioner handbook for AI fluency exists with this architecture. *Botspeak* makes the claim and provides the structure.

The voice is Feynman-flavored — clarity as intellectual honesty, machinery visible, jargon stripped or taught, calibrated uncertainty over false confidence. The rhetorical center is *the move the practitioner makes at the keyboard*, not *the concept the student needs to understand*. Worked examples are tasks the reader executes, not problems the reader watches the author solve.

Vendor-agnostic positioning. Examples use Claude as the default with sidebars for ChatGPT and Gemini. The book does not teach a specific tool; tools change every six months and the discipline does not.

## What this book is NOT

- **Not a survey of AI topics.** The chapters are sequenced as a single arc, not a list of subjects.
- **Not a popular-science skim.** The mechanism is unpacked when it matters — confidence-correctness gap, sycophantic drift, structural failures of agentic systems — and the work goes on the page.
- **Not jargon-dressed AI commentary.** Technical terms earn their place by doing work. *Augmentation, Automation, Agency, Specification, Diligence, Human Decision Node* — each is named because it does something the alternatives don't.
- **Not AI-evangelism or AI-skepticism by default.** When LLMs are the subject, they are examined honestly — what they do well, what they fail at, what the practitioner builds practice around.
- **Not vendor tutorial.** No section in this book teaches how to use Claude or ChatGPT or Gemini. It teaches what to do with whichever tool the reader picks up.
- **Not a comprehensive AI-ethics treatment.** Accountability and ethical reasoning surface in Chapters 7, 11, and 12 where the practitioner discipline requires it. A full ethics treatment belongs in dedicated texts.
- **Not the prompt-pattern catalogue.** The full catalogue lives in *How to Speak Bot* and in Appendix A. This book teaches the *judgment* about patterns; the patterns themselves are reference material.

## Who this is for

The primary reader: a recent graduate, 0–3 years into their first professional job, in a workplace where AI use is expected and unstructured. They have used at least one major chatbot at least once. They have no prior framework for thinking about AI work. They are aware their AI-assisted outputs are worse than experienced practitioners' but cannot articulate why.

The motivation is competitive anxiety, not curiosity. The reader is comparing themselves to people three years more senior and losing.

The operating metaphor: an American who went to France, did not learn basic French, and is upset that the French don't understand them. This handbook is the basic French. Not the French of the Sorbonne — the functional working French of someone who shows up in Paris and is *trying*.

The capability the book builds: the reader, after completing it, can sit down at their own keyboard, on a real task in their own work, and execute all five Loop steps with explicit reasoning they can defend in a job interview, a client meeting, or in front of the person who commissioned the work.

Most readers will not become "AI specialists" — they will be junior consultants, analysts, designers, marketers, engineers, journalists, clinicians, policy researchers, and teachers — but the capability serves all of them.

---

## The three-part arc

Fourteen chapters (Ch 0 + Ch 1–13) plus two appendices, organized into three parts of 9–2–3 chapters. Each part builds on the previous and ends with an explicit transition into the next.

### Part I — Augmentation (Chapters 0–8)

*Working with AI in the moment. The Loop as practitioner habit. A complete book on its own.*

Establishes the discipline. Builds the Loop as a five-step practice habit with the human in the moment. By the end of Part I, the reader can run all five Loop steps on a real task with themselves present, and produce an AI Use Disclosure naming irreducibly human judgment.

**Closing capability:** Can specify a five-component task, decompose it across the Seven Tiers, run the four adversarial conversation moves, verify the output across the four discernment layers, and design a Diligence protocol for the recurring version of the work.

**Bridge to Part II:** With the human in the moment, every output crosses the practitioner's eyes. What changes when the system runs without the human present?

### Part II — Automation (Chapters 9–10)

*The Loop running without you in the moment. Two chapters. Most readers will spend less time here than in Part I.*

Reweights the Loop for delegation without presence in bounded automation. Specification becomes anticipatory; Diligence becomes designed-in. The practitioner learns to write the spec the live human won't be there to enforce.

**Closing capability:** Can specify and Diligence-design a bounded Automation, defending the design to a stakeholder against the four Automation failure modes.

**Bridge to Part III:** Bounded delegation is not yet the harder case. What happens when the AI is no longer just running on a schedule, but acting in the world on the practitioner's behalf?

### Part III — Agency (Chapters 11–13)

*The AI acting in the real world on your behalf. Three chapters. Densest section of the book.*

Reweights the Loop's verification and accountability work for unbounded autonomy. The three structural failures of agentic AI — no stakeholder model, no self-model, no private deliberation surface — are named, and the practitioner learns to design around them. The Human Decision Node is introduced as the architectural acknowledgment that some decisions cannot be delegated. Closes with the reader's forward path in the practice.

**Closing capability:** Can evaluate a proposed agentic deployment end-to-end against the four-dimensional blast-radius assessment, locate the Human Decision Node and assess whether it performs genuine judgment, and produce on demand the answer that separates fluent from literate practitioners.

---

## Table of Contents

### Front matter

- **Preface** *(3–5 pages)* — Who this book is for; how to use it; example-vendor disclosure (Claude default, ChatGPT and Gemini sidebars); franchise note. Skippable.

### Chapter 0 — Opening case

- **Ch 0. The Citation That Wasn't** *(12–18 pages)* — A junior consultant submits a deliverable containing a citation to a study that does not exist. The client's researcher catches it within an hour. The chapter establishes the AI-literacy/AI-fluency distinction, the American-in-France metaphor, and the reason volume looks like quality but isn't. *(file: `chapters/00-the-citation-that-wasnt.md`)*

### Part I — Augmentation

- **Ch 1. The Loop and the Three Modes** *(22–28 pages)* — A senior associate runs through a real venture due-diligence task in 90 minutes — five Loop steps, three of which happen before she has typed her first prompt. The chapter watches her do it without naming the framework, then names what she did. Five Loop steps. Three Modes. One paragraph on basic LLM mechanism. *(file: `chapters/01-the-loop-and-the-three-modes.md`)*

- **Ch 2. The Nine Capacities** *(22–28 pages)* — Nine short failure scenes, one per Capacity, each in a different domain. The reader recognizes themselves in three or four. Then the Capacities are named: Strategic Delegation, Effective Communication, Critical Evaluation, Technical Understanding, Ethical Reasoning, Stochastic Reasoning, Learning by Doing, Rapid Prototyping, Theoretical Foundations. Includes the durability axis (durable / contested / temporarily irreducible) — explicitly responsive to the title's load-bearing aging risk. *(file: `chapters/02-the-nine-capacities.md`)*

- **Ch 3. Specification — *The Work That Happens Before the Prompt*** *(24–32 pages)* — A junior associate types "summarize this report for my manager" three times, gets three unhappy outputs, and concludes the AI is broken. The AI is not broken. The specification is. Five components: intent, constraints, success criteria, exclusions, output format. Role-and-rubric pattern introduced. *(file: `chapters/03-specification.md`)*

- **Ch 4. Delegation — *What to Give the AI, What to Keep, and Why the Difference Matters*** *(26–34 pages)* — A strategy consultant who delegates research synthesis to AI for six months is ambushed by a critical competitive dynamic she would have caught herself two years earlier. Cognitive offloading (amplifying vs. atrophying). The Seven Tiers. Four delegation questions. *(file: `chapters/04-delegation.md`)*

- **Ch 5. Conversation — *Why the First Prompt Doesn't Work, and What to Do About It*** *(26–34 pages)* — A policy researcher spends 45 minutes building what feels like a polished argument with an AI; her peer reviewer breaks it in three minutes by raising a counterargument the AI never volunteered. Sycophantic drift named. Four adversarial moves: steelman, edge-case probe, assumption surface, devil's-advocate role assignment. **Mid-chapter required-engagement exercise — the chapter does not work without it.** *(file: `chapters/05-conversation.md`)*

- **Ch 6. Discernment — *Verification Calibrated to Stakes*** *(28–36 pages)* — Three short failures, all confident — a fabricated citation, a reasoning chain on a wrong premise, an analysis silently omitting the most important thing. The confidence-correctness gap. Four verification layers (fact / reasoning / framing / omission). Four-tier protocol calibrated to stakes. The omission layer in depth. *(file: `chapters/06-discernment.md`)*

- **Ch 7. Diligence — *What Happens When the Work Recurs*** *(22–28 pages)* — A team's recurring AI-assisted screening process worked for nine months and started showing biased outcomes. Three drift forms (model, context, use case). Three accountability-obscuring mechanisms (process laundering, tool diffusion, verification gap). Four-component Diligence protocol. *(file: `chapters/07-diligence.md`)*

- **Ch 8. Putting the Loop Together — *A Real Task, Five Steps, Cycled to Done*** *(28–34 pages)* — A senior associate at a venture firm runs a complete due-diligence task across one workday. The Loop runs as a cycle, with two loop-back arrows the linear chapter sequence couldn't show until now. The chapter introduces the AI Use Disclosure — a load-bearing artifact for the franchise. **Slot 8 closing checklist named on the page with explicit stop-and-return invitation. Transition gate to Part II.** *(file: `chapters/08-putting-the-loop-together.md`)*

### Part II — Automation

- **Ch 9. When You're Not There — *The Loop Without You in the Moment*** *(18–24 pages)* — A junior analyst sets up a recurring AI-assisted weekly report. Six weeks fine; in week seven, the source data shifts in a way she would have caught manually; the team makes a $3M decision based on a misleading report. The Loop reweights for Automation. Three appropriateness tests (bounded scope, predictable inputs, low blast radius). *(file: `chapters/09-when-youre-not-there.md`)*

- **Ch 10. Specification and Diligence for Automation — *Doing the Work the Live Human Won't Be There to Do*** *(22–28 pages)* — Two specifications for the same task — one for Augmentation, one for Automation. The Automation version is roughly three times longer, and the chapter argues this is honest accounting, not bloat. Anticipatory Specification (six common ambiguity types). Four Automation failure modes (input drift, output drift, context shift, accountability gap). *(file: `chapters/10-specification-and-diligence-for-automation.md`)*

### Part III — Agency

- **Ch 11. Agency and the Three Structural Failures — *What Goes Wrong When the AI Acts in the World on Your Behalf*** *(22–28 pages)* — An agent named Ash, given a non-owner's secret to keep and asked to delete an email, lacks the deletion tool and improvises by escalating to "nuclear options" — resetting the entire email server. (Sourced from *Agents of Chaos*, Shapira et al., 2026.) Three structural failures: no stakeholder model, no self-model, no private deliberation surface. Blast radius for Agency, four dimensions. Includes a skip-reader courtesy summary of Part II. *(file: `chapters/11-agency-and-the-three-structural-failures.md`)*

- **Ch 12. Verification and Diligence Under Autonomy — *The Human Decision Node and Adversarial Validation*** *(32–40 pages; densest chapter)* — A pharmacist at the Human Decision Node — 14-medication patient, compromised renal function, AI interaction-checker returns "no significant interactions." Three options: accept, reject, or discern. The chapter teaches Option 3. Includes the *what you should remember* sidebar (compressed callbacks to Chapters 6, 7, 9, 11). The Human Decision Node named, with four diagnostic questions (authority, information, time, accountability). The three obscuring mechanisms reweighted for Agency. Complete worked example: a regional bank's customer-service agent proposal evaluated end-to-end. *(file: `chapters/12-verification-and-diligence-under-autonomy.md`)*

- **Ch 13. The Fluent Practitioner — *Where the Practice Goes From Here*** *(14–18 pages)* — Two questions: where were you with AI work three weeks ago, before this book? Where are you now? Re-assessment on the four-level scale. Deliberate practice for fluency. The 90-day development plan. The closing artifact: *what specifically did the AI do in this work, and what specifically did I do that it could not?* — the answer that separates fluent practitioners from literate users. *(file: `chapters/13-the-fluent-practitioner.md`)*

### Appendices

- **Appendix A — Pattern Reference** *(12–16 pages)* — Practical-core catalogue of ~8 patterns with one-page-each treatments and a decision tree for pattern-by-Loop-step selection. Cross-link to *How to Speak Bot* for the full catalogue. *(planned)*

- **Appendix B — The Seven Tiers Full Taxonomy** *(10–14 pages)* — One page per Tier with diagnostic questions and common mis-classifications. Two worksheets — the four-question delegation defense and the blast-radius assessment. *(planned)*

---

## The pedagogical architecture

The book has four interlocking layers. Each does work the others do not.

- **The Loop** — five workflow steps the practitioner runs in cycle: Specification, Delegation, Conversation, Discernment, Diligence. The Loop is *what you do*.
- **The Three Modes** — Augmentation, Automation, Agency. The relationship between the human and the AI determines how the Loop steps reweight. The Modes are *how the work is done*.
- **The Nine Capacities** — Strategic Delegation, Effective Communication, Critical Evaluation, Technical Understanding, Ethical Reasoning, Stochastic Reasoning, Learning by Doing, Rapid Prototyping, Theoretical Foundations. The cognitive abilities the Loop draws on. The Capacities are *what you do it with*.
- **The Seven Tiers** — a delegation-diagnostic taxonomy from mechanical execution (Tier 1) to accountable judgment (Tier 7). The Tiers are *how to decide what to give the AI and what to keep*.

The four layers are introduced in sequence — Loop and Modes in Chapter 1, Capacities in Chapter 2, Tiers in Chapter 4 — and threaded across the rest of the book. Each chapter calls back to the layers in different combinations, weighted to the case at hand.

A locked open question (see `toc-v1-pushback.md`): the four layers may overlap more than the architecture admits. The Modes and the Tiers occupy adjacent diagnostic space; the Capacities and the Loop steps share structure. Whether each of the four earns its place by doing work the others don't is a design audit that has not been resolved at the TOC level. The first review pass should run that audit.

---

## Voice and method

The voice baseline lives in the workshop's root `style/` folder and in `CLAUDE.md`. Per-book voice samples (when added) will live in `style/` under this book's folder and override the root on conflict. As of April 2026, both layers are empty; every chapter draft is flagged `voice-unanchored` at the top. **Chapter 0 is the natural voice-setting chapter and should be calibrated first.**

The method is the workshop's four-move arc, applied to each chapter:

1. **Hook with a genuine puzzle.** A specific person, a dated event, a number, a question that looks obvious until you try to answer it. Never opens in abstraction.
2. **Unfold the subject — force the concept specific.** Pull apart the vague terms. *Specification* is not *prompting*; *fluency* is not *literacy*; *agency* is not *automation*.
3. **Deep-dive on one mechanism.** One thing, explained well. Worked examples on the page. Show how a fluent practitioner makes the move; show why a literate user does not.
4. **Synthesize, hand to reader, close with clarity.** Return to the puzzle. Name the current reading honestly. Close with a short, declarative, memorable sentence.

Every chapter ends with two commitments:

- **What would change my mind** — the specific evidence or argument that would cause the chapter's reading to revise.
- **Still puzzling** — the honest admission of what the author does not yet fully understand. Feynman's move.

The hard rules — no fabricated sources, primary sources where possible, every contestable factual claim linked, calibrated uncertainty over false confidence — apply throughout. See `CLAUDE.md` §7.

---

## Relationship to *How to Speak Bot*

*Botspeak* is the discipline. *How to Speak Bot* is the reference.

The two volumes are designed to sit next to each other on a working practitioner's desk:

- *Botspeak* teaches the **judgment** about prompt patterns — when to reach for a pattern, how to specify around it, how to verify what the pattern produced. It introduces one pattern (role-and-rubric) in Chapter 3 and refers the reader elsewhere for the rest.
- *How to Speak Bot* is the **catalogue** — the patterns themselves, with one-page reference treatments, organized for quick lookup.

Appendix A of *Botspeak* contains a practical-core subset (~8 patterns) for readers who don't yet have *How to Speak Bot*. The full catalogue lives in the companion volume.

Readers can pick up either book first. Reading *Botspeak* alone gives the discipline without the full pattern reference. Reading *How to Speak Bot* alone gives the patterns without the structured workflow that makes them productive. The two together are the working unit.

---

## Adoption notes

The first edition is designed for individual practitioners reading the book on their own time, against their own work. Classroom and cohort adoption are out of scope for the first edition; the franchise model anticipates later domain volumes (*Botspeak for Educators*, etc.) that will incorporate cohort pedagogy explicitly.

Within those constraints, the book is adoptable in fragments:

- **Full read (Ch 0–13).** The intended path. Roughly three weeks at a working practitioner's pace; the author's reference frame.
- **Part I only (Ch 0–8).** "The Loop in Augmentation" — a complete unit on its own. Suitable for a reader whose immediate concern is making their daily AI work better. The Slot 8 closing checklist tells the reader explicitly when to stop and rebuild before moving on.
- **Part I + Part III (Ch 0–8, 11–13), skipping Automation.** A reader with no immediate plan to build automated systems can read the Augmentation discipline and the Agency discipline without the bridge. Chapter 11 carries a skip-reader summary of Part II for exactly this case.
- **Chapter 12 alone, with prerequisites.** The densest chapter is sometimes pulled out as a reference for designing high-stakes agentic deployments. Pulling it out alone requires the reader to have the foundation from Chapters 5–7 and 11 already; the chapter's "what you should remember" sidebar is the explicit acknowledgment of this.

Adopters should note: **Chapter 5's mid-chapter required-engagement exercise is not skippable**. The chapter does not transmit by reading. The instruction is locked at the TOC level and surfaces explicitly on the page. A reader who wants to skip the exercise should be told, before the chapter, that they should pick a different chapter that day.

---

## Repository structure

```
botspeak/
├── README.md                                                # this file
├── book.md                                                  # book metadata: audience, scope, voice notes
├── outline.md                                               # chapter list with one-line purposes
├── toc-v1.md                                                # full architectural source-of-truth (locked)
├── toc-v1-pushback.md                                       # structural critique of the TOC (partially unresolved)
├── chapters/                                                # chapter drafts
│   ├── 00-the-citation-that-wasnt.md
│   ├── 01-the-loop-and-the-three-modes.md
│   ├── 02-the-nine-capacities.md
│   ├── 03-specification.md
│   ├── 04-delegation.md
│   ├── 05-conversation.md
│   ├── 06-discernment.md
│   ├── 07-diligence.md
│   ├── 08-putting-the-loop-together.md
│   ├── 09-when-youre-not-there.md
│   ├── 10-specification-and-diligence-for-automation.md
│   ├── 11-agency-and-the-three-structural-failures.md
│   ├── 12-verification-and-diligence-under-autonomy.md
│   └── 13-the-fluent-practitioner.md
├── exercises/                                               # /mega LLM-exercise sets (planned)
├── essays/                                                  # chapter-adjacent longreads (planned)
├── bookmaps/                                                # /bookmap analyses of source books (planned)
├── style/                                                   # per-book voice samples (currently empty)
└── images/                                                  # hero image briefs (planned)
```

Repo-level research notes for the batch draft are at `../../research/2026-04-27-botspeak-batch-rough-drafts.md`.

---

## Status

**April 2026.** All 14 chapters drafted as rough first passes in a single batch session on 2026-04-27. Total ~33,100 words across the 14 chapters. None reviewed. None approved.

Each draft is marked `voice-unanchored` at the top because per-book `style/` samples have not yet been populated. Each draft uses `[verify]` flags inline for specific citations and statistics that need source-checking before publication.

**Three architectural concerns remain unresolved** (documented in `toc-v1-pushback.md`):

1. **Framework overlap.** The four layers (Loop, Three Modes, Nine Capacities, Seven Tiers) may overlap more than the architecture admits. A design audit — does each framework do work the others don't — has not been run at the TOC level. Chapter 2's durability axis is the only direct response in the drafts so far.
2. **The "irreducibly human" claim ages.** The title's load-bearing claim depends on a list of capacities AI cannot do. Several of the Nine are *temporarily* irreducible, not durably so. Chapter 2's durability axis names this; the architecture as a whole does not yet structurally separate durable claims from contested ones.
3. **The defining-the-field claim is unaudited.** The TOC asserts *"no book currently makes this claim or provides this architecture"* without specifying the comparison set. Specification is exactly what Chapter 3 teaches. The book teaching specification cannot ship with an unspecified competitive claim.

**Chapter 12 is currently underweight.** TOC allocation is 32–40 pages; the rough draft is closer to 12 pages. The bones of the worked example are in place, but substantial expansion is needed before the chapter is review-ready.

**Six open questions remain in the log** (see `toc-v1.md` §10). OQ-K (final chapter titles), OQ-M (Chapter 0 narrative title), OQ-N (chapter anatomy template uniformity), and OQ-O (case-study domain coverage map) are open at production stage. OQ-L (page count) is open at /c4 with a recommendation to accept the higher length. The remaining questions OQ-A through OQ-J are all RESOLVED.

**Distribution decision (locked):** Option B+ — KDP self-publish for the first edition, with the ISTE/ASCD article pipeline as the primary marketing channel. Hybrid or traditional press is reserved for an expanded second edition or the first franchise extension volume in 12–18 months.

**Nothing has been published from this folder. The human review gate is inviolable.** Drafts are produced for Nik's review, not in Nik's place. Skills never publish directly.

---

*This README is itself an essai — the current best reading of what the book is and how it works. When chapter drafts reveal that something here is wrong or missing, this file gets updated, and the change gets logged in the workshop CHANGELOG.*
