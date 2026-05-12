# Botspeak — LLM Exercises

*The end-of-chapter LLM Exercise prompts from every chapter, compiled in one place. Each exercise builds the chapter's portfolio artifact. Run them in order; later prompts assume the artifacts produced by earlier ones are in your Claude Project context.*

*Companion reference: `_the-claude-project.md` (project setup, system prompt, file-attachment discipline). The artifacts produced by these exercises live in `portfolio/`.*

---

## Table of Contents

- [Chapter 0: The Citation That Wasn't](#chapter-00-the-citation-that-wasnt)
- [Chapter 1: The Loop and the Three Modes](#chapter-01-the-loop-and-the-three-modes)
- [Chapter 2: The Nine Capacities](#chapter-02-the-nine-capacities)
- [Chapter 3: Specification](#chapter-03-specification)
- [Chapter 4: Delegation](#chapter-04-delegation)
- [Chapter 5: Conversation](#chapter-05-conversation)
- [Chapter 6: Discernment](#chapter-06-discernment)
- [Chapter 7: Diligence](#chapter-07-diligence)
- [Chapter 8: Putting the Loop Together](#chapter-08-putting-the-loop-together)
- [Chapter 9: When You're Not There](#chapter-09-when-youre-not-there)
- [Chapter 10: Specification and Diligence for Automation](#chapter-10-specification-and-diligence-for-automation)
- [Chapter 11: Agency and the Three Structural Failures](#chapter-11-agency-and-the-three-structural-failures)
- [Chapter 12: Verification and Diligence Under Autonomy](#chapter-12-verification-and-diligence-under-autonomy)
- [Chapter 13: The Fluent Practitioner](#chapter-13-the-fluent-practitioner)

---

<a id="chapter-00-the-citation-that-wasnt"></a>
## Chapter 0: The Citation That Wasn't

### LLM Exercise — Chapter 0: The Citation That Wasn't

**Project:** AI Fluency for [Your Role] — Your Domain Field Manual

**What you're building this chapter:** A **Role Dossier** you'll pin to your Claude Project for the rest of the book, and the **Baseline Audit** you just sketched above — drafted, structured, and saved.

**Tool:** Claude Project (set up "AI Fluency for [My Role]" — you'll return every chapter) + your file system (the `portfolio/` folder you just created).

---

**The Prompt:**

```
I am working through "Botspeak" by Nik Bear Brown and across the book I will
build a portfolio of AI-fluency artifacts in my own field. This is the
setup chapter — Chapter 0, The Citation That Wasn't. I need help with two
tasks.

TASK 1 — SPECIFY THE ROLE. The role should be:
- One I actually work in (or am about to enter)
- Specific enough to be useful — not "knowledge worker" but "junior associate
  at a regional law firm" or "growth marketer at an early-stage SaaS company"
  or "clinical pharmacist on a hospital night shift"
- Bounded enough that the failure modes are recognizable to anyone in the role
- Big enough that the playbook helps a real population

My context:
- Role / job title: [FILL IN]
- Industry / sector: [FILL IN]
- Career stage of the playbook's reader: [0–6 months / 6–18 months / 18–36 months / 5+ years]
- 2–3 task types I do most weekly: [LIST]
- Whether AI use is sanctioned, unsanctioned, or contested in my workplace: [FILL IN]

Push back if my role is too broad. Help me sharpen until the playbook would
be unmistakably for someone in this role and not someone in an adjacent one.

TASK 2 — DRAFT THE BASELINE AUDIT. Chapter 0 introduces the Baseline Audit
as the first portfolio artifact. I will redo it as a Final Audit in
Chapter 13. The pair is the book's before-and-after evidence of fluency.

Help me draft mine. The piece I am auditing:
- What it was: [FILL IN — document, report, memo, code, analysis, teaching plan, brief, etc.]
- Who it was for: [FILL IN]
- When it shipped: [FILL IN]
- How I used AI in producing it: [FILL IN — research, drafting, citations, code, structure, all of it]

The most consequential single claim in the piece:
- The claim itself: [FILL IN]
- Why it's load-bearing — what depends on it: [FILL IN]

Walk me through a trace of that claim. For each:
- Where did it come from in the AI session?
- Did I verify it at the time? How?
- Could I verify it now, without the AI's help? What would I check?
- What specifically would not survive a hostile re-read?

End with:
1. A one-paragraph "Role Dossier" I can pin to my Claude Project's system
   prompt so every future chapter exercise inherits the role context.
2. The Baseline Audit itself, formatted as the three sections in Botspeak
   Chapter 0: Piece audited / Load-bearing claim / Trace. No more than half
   a page total.

Save the Baseline Audit as `portfolio/00-baseline-audit.md`.
```

---

**What this produces:** A Role Dossier (pinned to the Project for every future exercise) and the Baseline Audit (saved to your portfolio folder). The first of seventeen artifacts. Twelve more to come.

**How to adapt this prompt:**

- *For your own project:* Fill in the bracketed fields. If you wear multiple hats, pick the role you'll keep growing in for the next two years.
- *For ChatGPT / Gemini:* Works as-is. Set up as a Custom GPT for persistence. Gemini's Drive integration handles the portfolio folder cleanly.
- *For Claude Code:* Not yet — this chapter is conceptual. Claude Code becomes useful starting Chapter 3 when you build the Specification Library.
- *For a Claude Project:* Recommended. The Role Dossier becomes part of the system prompt going forward.
- *For Cowork:* Recommended for managing the portfolio folder. Ask Cowork to create the folder structure: `portfolio/00-baseline-audit.md`, `portfolio/CLAUDE.md`, `portfolio/DESIGN.md`, `portfolio/PROJECT-template.md` (the last three are stubs you'll fill across the book).

**Connection to previous chapters:** None — this is Chapter 0. The Role Dossier and the Baseline Audit are the foundation every subsequent chapter exercise builds on.

**Preview of next chapter:** Chapter 1 takes a typical task in your role and walks the full Loop on it — your role's version of Priya's Tuesday at her best. The Worked Loop Log becomes the second piece in your portfolio.

---

<a id="chapter-01-the-loop-and-the-three-modes"></a>
## Chapter 1: The Loop and the Three Modes

### LLM Exercise — Chapter 1: The Loop and the Three Modes

**Project:** AI Fluency for [Your Role] — Your Portfolio's Second Artifact

**What you're building this chapter:** Two pieces. (a) The **Worked Loop Log** — one real bounded task in your work taken through all five Loop steps, time-stamped, saved to `portfolio/01-worked-loop-log.md`. (b) The first three rules in your **`CLAUDE.md`** — your personal coding/process constitution, saved to `portfolio/CLAUDE.md`. Both are Layer A templates filled with Layer B (your domain's) content.

**Tool:** Claude Project (continue from Chapter 0; your Role Dossier is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier from Chapter 0 and
my Baseline Audit are in the Project context.

Botspeak Chapter 1 watches Priya (a journalist nine months past her
Chapter 0 wake-up) run a 90-minute daily explainer task through all
five Loop steps — Specification, Delegation, Conversation, Discernment,
Diligence — competently but not yet at the eighteen-months-of-reflexes
mastery of Chapter 8. The chapter also names the three Modes
(Augmentation / Automation / Agency).

For Chapter 1's portfolio artifacts, do two things.

TASK 1 — DRAFT MY WORKED LOOP LOG.
Help me pick one bounded, recurring, ~90-minute task from my work and
draft the Worked Loop Log for it.

The task I will run:
- What it is: [FILL IN — e.g., "Friday client-update memo," "patient
  note after a clinic visit," "pull-request code review," "unit plan
  for next week," "methods section draft for a paper section"]
- How often I do it: [FILL IN]
- Who consumes the output: [FILL IN]
- Why it requires judgment (not just lookup): [FILL IN]

Walk me through the Worked Loop Log structure:
- Section 1 — SPECIFY. What I write before opening the tool. Audience,
  task, structure, source rule, exclusions. ~150 words.
- Section 2 — DELEGATE. What I hand to the model, what I keep, what
  I sketch and ask the model to fill. ~150 words.
- Section 3 — CONVERSE. The prompts I write and the adversarial moves
  I deploy. Show at least one steelman or edge-case probe. ~200 words.
- Section 4 — DISCERN. What I check, against what, looking for what
  kinds of errors. Name at least two failure shapes (the kind of
  placeholder number, the kind of citation that does not exist, etc.)
  ~150 words.
- Section 5 — BE DILIGENT. The AI Use Disclosure I attach, plus one
  note to my template/CLAUDE.md so I do not need to learn this twice.
  ~100 words.
- Retrospective — One paragraph. Where the structure helped. Where it
  felt like overhead. What changed for next time.

Time-stamp the sections. Be specific to my actual task, my actual
tools, my actual stakeholders. The log should be ~800–1,200 words
total. Save as `portfolio/01-worked-loop-log.md`.

TASK 2 — OPEN MY CLAUDE.md.
Help me draft the first three rules of my personal CLAUDE.md — my
coding/process constitution for AI work. Three sections:

1. WHAT I WILL NOT IMPROVISE WITHOUT EXPLICIT INSTRUCTION.
   2–4 rules specific to my field. (Examples for journalism:
   "I will not generate citations the model cannot ground in a
   specific public document." For a software engineer: "I will not
   commit code Claude generated without running it locally first.")

2. WHAT I ALWAYS SPECIFY BEFORE OPENING THE TOOL.
   The four or five elements I always include in a specification
   for my recurring task types. Audience, structure, source rule,
   exclusions, success criteria — your version.

3. WHAT I ALWAYS DO BEFORE SHIPPING.
   The verification or diligence moves I run on every consequential
   output before it leaves my desk.

Save as `portfolio/CLAUDE.md`. Note: this file is a LIVING document
— we will return to it in Chapter 3 (Specification), Chapter 4
(Delegation), and Chapter 6 (Discernment), adding rules as the book
gives me reasons to.
```

---

**What this produces:** Your portfolio's second and third artifacts — the Worked Loop Log (a real task taken through all five Loop steps) and the first version of your living `CLAUDE.md`. Both saved to `portfolio/`. Both will grow.

**How to adapt this prompt:**

- *For your own project:* Pick a task you will *actually run* this week. The Worked Loop Log written from a hypothetical task is structurally weaker than one written from a real one. The whole point is that the log is evidence, not aspiration.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful for setting up the `portfolio/` folder structure cleanly.
- *For Cowork:* Recommended. Cowork can walk the portfolio folder and remind you what files exist.

**Connection to previous chapters:** Chapter 0 produced the Baseline Audit (one piece of past work, audited). Chapter 1 produces the Worked Loop Log (one piece of current work, run with the Loop visible) and opens the `CLAUDE.md`. The portfolio is now three artifacts deep.

**Preview of next chapter:** Chapter 2 produces the first half of your Practitioner Profile — the Nine Capacities self-assessment. The Profile pairs with the delegation map you build in Chapter 4 to become one combined diagnostic artifact.

---

<a id="chapter-02-the-nine-capacities"></a>
## Chapter 2: The Nine Capacities

### LLM Exercise — Chapter 2: The Nine Capacities

**Project:** AI Fluency for [Your Role] — Your Practitioner Profile

**What you're building this chapter:** Two pieces. (a) Nine domain-specific failure scenes — one per capacity — that anchor each capacity in your role's actual tasks. (b) The first half of your **Practitioner Profile** — the capacities self-assessment with two priority picks named honestly. Both saved to `portfolio/`. The Profile pairs with the Delegation Map from Chapter 4 to become one consolidated diagnostic artifact.

**Tool:** Claude Project (continue — your Role Dossier, Baseline Audit, Worked Loop Log, and CLAUDE.md are in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier from Chapter 0, my
Worked Loop Log from Chapter 1, and my opening CLAUDE.md are in the
Project context.

Botspeak Chapter 2 watches Priya — a journalist twelve months past
Chapter 0 — receive a Letters-to-the-Editor email about a state-by-state
lag-time table in a piece she wrote three weeks earlier. The model had
silently mishandled fiscal-year-to-calendar-year conversions for several
states. The chapter unpacks four distinct capacity failures from that
one error and uses the constellation to introduce the Nine Capacities
plus the four-level self-assessment (untrained / aware / practicing /
fluent).

For Chapter 2's portfolio artifacts, do two things.

TASK 1 — NINE FAILURE SCENES IN MY ROLE.
Write nine short failure scenes, one per Capacity, all set in my role.
Each scene 100–200 words. Each scene a different (named) person in a
different sub-context of the role. Each scene a clean instance of the
capacity's failure mode. Use real tools, real artifacts, real
stakeholders for my role.

The Nine Capacities and the chapter's diagnostic question for each:

1. STRATEGIC DELEGATION — what should I give the AI, what should I keep,
   and why?
2. EFFECTIVE COMMUNICATION — am I telling the model what it actually
   needs to know to do this well?
3. CRITICAL EVALUATION — would I bet on this output, and on what
   evidence?
4. TECHNICAL UNDERSTANDING — do I know enough about how this system
   works to recognize when it's failing?
5. ETHICAL REASONING — who could be harmed by this output or this
   deployment, and am I tracking that?
6. STOCHASTIC REASONING — what kind of probabilistic claim is this, and
   what would calibrate my belief in it?
7. LEARNING BY DOING — am I still building the skill, or just consuming
   the output?
8. RAPID PROTOTYPING — am I treating model output as the work, or as a
   draft I will pressure-test in the world?
9. THEORETICAL FOUNDATIONS — do I understand the underlying material
   well enough to judge whether this output is good?

Resist the temptation to make all nine scenes about the same task type.
Spread them across my role's sub-contexts so the scenes engage different
parts of the work.

Save the nine scenes as `portfolio/02-nine-scenes-in-my-role.md`. (This
is a supporting file in the portfolio — not the Practitioner Profile
itself, which comes next.)

TASK 2 — DRAFT MY PRACTITIONER PROFILE (PART 1).
Help me draft the first half of my Practitioner Profile. The Profile is
a Layer A diagnostic — the structure is standard — filled with Layer B
content (my honest self-assessment in my domain).

The Profile has three sections:

1. CAPACITIES SELF-ASSESSMENT. The nine-row table from Chapter 2,
   filled in honestly. For each capacity: my current level (untrained
   / aware / practicing / fluent) plus one specific note — a failure
   I recognize, a task type where I notice the gap, a senior practitioner
   whose strength I want to match.

2. TWO PRIORITY CAPACITIES. The two I most want to move up one level
   in the next 90 days. One sentence each on WHY — not "because I'm
   weak" but something specific. These two will become the 90-Day
   Plan in Chapter 13.

3. PLACEHOLDER FOR PART 2. A note that the second half of the
   Practitioner Profile (the Delegation Map) will be added in
   Chapter 4, after which the combined Profile becomes one consolidated
   diagnostic artifact in my portfolio.

Push back on me if my self-assessment looks too generous — a Profile
that rates fluent across the board is either lying or unworked.

Save as `portfolio/02-practitioner-profile.md`.
```

---

**What this produces:** Two additions to your portfolio. The nine scenes file (`portfolio/02-nine-scenes-in-my-role.md`) — a research artifact you can update as you encounter your own failures. The Practitioner Profile Part 1 (`portfolio/02-practitioner-profile.md`) — the first half of one of the portfolio's three diagnostic artifacts. ~2,500–4,000 words across the two.

**How to adapt this prompt:**

- *For your own project:* The nine scenes ARE the playbook's diagnostic instrument. Don't rush them. A reader who recognizes themselves in three of nine scenes is a reader the playbook has already earned.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right fit — this is narrative and self-reflection.
- *For Cowork:* Recommended. Cowork can manage the multi-file split (`02-nine-scenes-in-my-role.md` and `02-practitioner-profile.md`).

**Connection to previous chapters:** Chapter 0 produced the Baseline Audit, Chapter 1 produced the Worked Loop Log and opened the `CLAUDE.md`. Chapter 2 produces the first half of your Practitioner Profile (the capacities side). Chapter 4 produces the second half (the delegation side). Combined, they are one diagnostic artifact in the finished portfolio.

**Preview of next chapter:** Chapter 3 produces the Specification Library — 1–3 worked specifications for your most common task types, plus your `PROJECT.md` template. The Specification Library is the third piece of evidence in your portfolio's Layer B (the first being the Worked Loop Log, the third being the End-to-End Case Study in Chapter 8).

---

<a id="chapter-03-specification"></a>
## Chapter 3: Specification

### LLM Exercise — Chapter 3: Specification

**Project:** AI Fluency for [Your Role] — Your Specification Library

**What you're building this chapter:** Your portfolio's first Layer B deliverable folder — five specification templates, one per recurring task type in your role, each with a worked example. Plus the opening draft of your `PROJECT.md` template. Plus one new rule added to your `CLAUDE.md`.

**Tool:** Claude Project (continue — your Role Dossier, Worked Loop Log, Practitioner Profile Part 1, and CLAUDE.md are in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile Part 1, and CLAUDE.md are in the Project context.

Botspeak Chapter 3 watches Priya — ten months past Chapter 0 — produce
three failed iterations on a single summarize-for-the-editorial-standup
task. The chapter introduces the five specification components: INTENT
(the goal the task serves), CONSTRAINTS (what the output must fit
inside), SUCCESS CRITERIA (how I'll know it's good), EXCLUSIONS (what
the model is NOT supposed to do), OUTPUT FORMAT (structural details).

For Chapter 3's portfolio artifacts, do three things.

TASK 1 — IDENTIFY THE FIVE MOST COMMON TASK TYPES IN MY ROLE.
Not nine, not three. Five. The task types should be:
- High-frequency (each appears multiple times per month for someone in
  my role)
- Distinct enough that they require different specifications
- AI-amenable (it's plausible to do them with AI assist)
- Spanning the role — not all the same kind of work

For each task type, name it precisely and give 2–3 examples of when
it occurs.

TASK 2 — A SPECIFICATION TEMPLATE PER TASK TYPE + A WORKED EXAMPLE.
For each of the five task types, produce a fillable specification
template covering all five components, with bracketed variables for
the parts that change per instance and pre-populated constants for
the parts that don't. Include 1–2 EXCLUSIONS specific to my role's
typical failure modes for this task type.

The template format I want:

TEMPLATE — [task type name]

Intent: Give [recipient] a [length/format] artifact for [specific purpose]
Constraints: [bracketed format details], source: [permitted sources], audience: [who reads it]
Success criteria: [recipient action/test 1]; [recipient action/test 2]
Exclusions: Do not [role-specific failure mode 1]. Do not [role-specific failure mode 2]. Do not [generic failure mode].
Output format: [structural details, length, sections]

Then, for each template, write one fully-filled-in worked example
showing what the template looks like populated for a specific instance
I could imagine on my desk this week. The worked example is half the
value — the template alone leaves the reader staring at brackets.

Save each template + worked example as a separate file under
`portfolio/03-specification-library/`. One file per task type.

TASK 3 — DRAFT MY PROJECT.md TEMPLATE.
Draft my personal PROJECT.md template — the Layer A scaffold I will
instantiate for every significant piece of work in Layer B of my
portfolio going forward. Two layers:

LAYER 1 — INTENT (what the project means, who the work is for, what
success looks like, the question the work is answering, where the
load-bearing judgment lives).

LAYER 2 — TECHNICAL STATE (what is built, what is pending, what was
generated by the model and accepted, what was rejected and why, what
verifications have been run, what was done by hand).

Save as `portfolio/PROJECT-template.md`. The keystone End-to-End Case
Study in Chapter 8 will instantiate this template for the first time.

TASK 4 — ADD ONE RULE TO MY CLAUDE.md.
Add the chapter's operational rule, in my own language. Something close
to: "I do not open the tool until I have written the five components
down, in some form, somewhere I can see them." Phrase it in a way that
fits my actual workflow.

Append the rule to my existing `portfolio/CLAUDE.md`.

End with one paragraph on the role-specific specification trap: what
is the failure mode that practitioners in my role most often produce
when they specify badly? What in my role tends to be most often left
unsaid? Save that paragraph at the top of the specification library
folder as `00-the-trap.md`.
```

---

**What this produces:** Your portfolio gains a folder (`portfolio/03-specification-library/`) containing five templates + five worked examples + the role's specification trap, plus a new file (`portfolio/PROJECT-template.md`) and an addition to `portfolio/CLAUDE.md`. The Specification Library is the first Layer B deliverable folder in your portfolio. ~3,000–5,000 words across the artifacts.

**How to adapt this prompt:**

- *For your own project:* The templates' value depends on the EXCLUSIONS section being honest about your role's typical failure modes. Be specific about what gets botched.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful here if your role's tasks are code-heavy and the templates can live as structured prompt files in a repo. Otherwise, plain Markdown.
- *For Cowork:* Recommended. Cowork can manage the multi-file folder structure cleanly.

**Connection to previous chapters:** Chapter 2's nine scenes named where your capacities currently fail. Chapter 3 builds the operational antidote at the Specification step. The PROJECT.md template opened here will be instantiated for the first time in Chapter 8's keystone case study.

**Preview of next chapter:** Chapter 4 produces the second half of your Practitioner Profile — the Delegation Map. Combined with Chapter 2's capacities self-assessment, the Profile becomes one consolidated diagnostic artifact in your portfolio.

---

## Exercises

### Warm-Up

**1. Name and test the five components.** *(Component recall | Difficulty: low)*
Without looking back, name the five specification components. For each one, write a single sentence describing what goes wrong when that component is missing — not in theory, but in practice. What does the output look like? What does the failure feel like from the user's side?

**2. Diagnose a weak prompt.** *(Component identification | Difficulty: low)*
Take this prompt: *"Write an email to my team about the new meeting policy."* Identify which of the five components are present and which are absent. Then rewrite it as a full specification. Your specification should be specific enough that a model — or a competent human colleague — could produce the deliverable without asking a single clarifying question.

**3. Trace Priya's iterations.** *(Component sequencing | Difficulty: low)*
Return to Priya's three prompts. For each iteration — *summarize this report for tomorrow's editorial meeting*, then *focusing on the most reportable findings*, then *in five bullet points* — name the single specification component she added (or groped toward) with that iteration, and the components still missing at that point. Then name the one component whose absence caused the most damage across all three attempts.

---

### Application

**4. Write a full specification.** *(All five components | Difficulty: medium)*
You are a marketing analyst preparing a competitive summary for a product launch. Write a complete five-component specification for this task. It should be specific enough that a model — or a competent colleague — could produce the deliverable without asking a clarifying question. Then identify which component was hardest to write, and explain why.

**5. Find the internal conflict.** *(Constraint tension | Difficulty: medium)*
Below is a specification with a hidden conflict:

> **Intent:** Produce a thorough analysis of all relevant risks.
> **Constraints:** Two pages maximum.
> **Success criteria:** A senior executive can read it in under three minutes and feel fully informed.
> **Exclusions:** Do not omit anything material.
> **Output format:** Prose paragraphs, no headers.

Name the conflict. Explain what will happen if this specification is sent to a model without resolving it. Then rewrite the specification to resolve the tension — you will have to make a real decision about which constraint wins.

**6. Explain the pattern's limits.** *(Role-and-rubric | Difficulty: medium)*
Explain why role-and-rubric is not a substitute for the five-component specification. Which components does it compress well? Which does it leave unaddressed? Give a concrete example — a specific task and a specific role assignment — where using role-and-rubric without addressing the missing components would produce a plausible but wrong output.

**7. Defend the templates.** *(Templates as infrastructure | Difficulty: medium)*
A colleague argues: "Templates are just bureaucracy. Good practitioners know what they want intuitively and don't need to fill out a form." Construct the strongest version of this argument — make it as compelling as you can. Then explain why you agree or disagree, using the chapter's reasoning about where specification overhead actually goes and what it does when it lands there.

---

### Synthesis

**8. Build a template library.** *(Specification across domains | Difficulty: hard)*
You are building a template library for a legal research team. Their three most common tasks are: summarizing case law for a partner review memo, drafting initial client intake questions, and checking a contract clause against a regulatory standard. Write a specification template for each task. For each template, note which component was hardest to generalize across instances of that task type, and why.

**9. Connect specification to the diagnostic.** *(Specification + self-knowledge | Difficulty: hard)*
The chapter claims the specification move is "in part, a diagnostic on yourself." Connect this to the chapter's discussion of exploratory work. Under what conditions is the diagnostic uncomfortable in a productive way — meaning it surfaces something you needed to know? Under what conditions is it a signal that you should not be delegating this task at all? Where does the chapter leave this question open, and what would you need to know to close it?

---

### Challenge

**10. Solve the still-puzzling.** *(Open-ended | Difficulty: high)*
The chapter ends with a stated puzzle: "I do not yet have a clean answer to when the cost of full specification exceeds the cost of iteration." Propose a framework for answering this question. Your framework should account for at least four variables — task type, stakes, novelty, and practitioner experience level — and should make a falsifiable prediction: given a specific task description, your framework should tell you whether to specify fully or iterate. Then identify the weakest assumption in your framework and explain what evidence would cause you to revise it.

**11. Teach the five components.** *(Feynman test | Difficulty: high)*
Design a 45-minute session for a team of ten that teaches the five-component specification to people who have never heard the term. Your design should specify: the opening problem you would pose and why it is the right problem, the order in which you would introduce the five components and why that order, the single exercise you would run after the third component is introduced, and how you would close the session. For each design decision, cite the chapter's reasoning about why specification is hard to learn and where the difficulty actually lives.

---

<a id="chapter-04-delegation"></a>
## Chapter 4: Delegation

### LLM Exercise — Chapter 4: Delegation

**Project:** AI Fluency for [Your Role] — Your Delegation Map

**What you're building this chapter:** The second half of your Practitioner Profile — the Delegation Map. Combined with the Chapter 2 capacities self-assessment, your Practitioner Profile becomes one consolidated diagnostic artifact. Plus one new rule added to your `CLAUDE.md`.

**Tool:** Claude Project (continue — your full portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile Part 1 (capacities self-assessment), Specification
Library, PROJECT.md template, and CLAUDE.md are all in the Project
context.

Botspeak Chapter 4 watches Priya — fourteen months past Chapter 0 —
discover on a pre-publication call that a state procurement-rule
revision (covered only in regional and trade press, missed by her AI
synthesis tool that sources from major outlets) materially changes
the story she had drafted. The chapter introduces the Seven Tiers
of delegation, the four delegation questions, the amplify/atrophy
distinction, and the performance paradox.

For Chapter 4's portfolio artifact — completing the Practitioner
Profile that opened in Chapter 2 — do two things.

TASK 1 — DRAFT MY DELEGATION MAP.
Help me build a personal delegation map. Five sections:

1. RECURRING TASKS. List 5–10 recurring AI-assisted tasks in my work.
   Be specific (not "data analysis" — "weekly cohort-retention table
   pulled from the warehouse"; not "client communication" — "monthly
   onboarding-confirmation email"). Span my role's range.

2. TIER LOCATION. For each task, locate it on the Seven Tiers from
   Chapter 4 (Mechanical Execution / Pattern-Matching with Feedback /
   Synthesis from Sources / Drafting in Your Voice / Judgment Under
   Structure / Contestable Analysis / Accountable Judgment). Explain
   why it lives at that tier in 1–2 sentences.

3. THE FOUR DELEGATION QUESTIONS PER TASK. For each task, answer:
   (a) What capacity does this task build, and do I need to keep
       building it?
   (b) What's the blast radius if the AI gets this wrong?
   (c) Who is accountable, and do they know how it's produced?
   (d) What does the model not know that I do, and have I made sure
       that part stays in?

4. AMPLIFY OR ATROPHY. For each task, name whether the delegation is
   currently amplifying me or atrophying me. Then name the
   early-warning sign of atrophy that would be visible specifically
   in my work — not general signs, but signs particular to my role's
   outputs.

5. THE PERFORMANCE-PARADOX RISK. Name the one skill in my role most
   at risk of quiet atrophy from my current delegation pattern. Then
   name one concrete practice — under 30 minutes a week — that would
   keep it alive. Be specific enough that I would actually do it.

TASK 2 — APPEND TO MY PRACTITIONER PROFILE.
Append the Delegation Map as a new section in
`portfolio/02-practitioner-profile.md`. The Profile is now complete:
half capacities self-assessment (from Chapter 2), half delegation map
(from Chapter 4). One consolidated diagnostic artifact.

TASK 3 — ADD ONE RULE TO MY CLAUDE.md.
Append the chapter's operational rule to my existing CLAUDE.md, in
my own language: something close to "Before any consequential
delegation, I run the four delegation questions. The skill that is
silently being delegated is the skill I will need the day the tool
fails."

Push back on me if the delegation map is too aspirational — if my
"amplifying" assessments outnumber my "atrophying" ones by more than
2-to-1, look at it again. Atrophy is the default, not the exception,
when daily delegation is unexamined.
```

---

**What this produces:** Your Practitioner Profile, completed. A consolidated diagnostic artifact in your portfolio that names the capacities you are practicing against, the recurring tasks you delegate, and the one skill most at risk of quiet erosion in your current pattern. Plus an addition to your `CLAUDE.md`. ~2,000–3,000 words of new material.

**How to adapt this prompt:**

- *For your own project:* The delegation map's value depends on being honest about which delegations are amplifying you and which are atrophying you. The default answer is "atrophying" — the default of any frictionless delegation is to erode the underlying skill. The "amplifying" cases earn their label by naming what specific evaluative move keeps the muscle firing.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful only if your role's recurring AI-assisted tasks are code-heavy and live in a repo. Otherwise plain Markdown.
- *For Cowork:* Recommended. Cowork can read the existing Practitioner Profile and append the Delegation Map section cleanly.

**Connection to previous chapters:** Chapter 2 opened the Practitioner Profile with the capacities self-assessment. Chapter 4 closes it with the Delegation Map. Combined, they are one of the three diagnostic artifacts in your finished portfolio (the others are the Automation Inheritance Audit from Chapter 9 and the paired Baseline/Final Audit from Chapters 0 and 13).

**Preview of next chapter:** Chapter 5 produces the Adversarial Conversation Log — a transcript of one piece of your own work taken through all four adversarial moves (steelman, edge-case probe, assumption surface, devil's-advocate). The artifact shows your conversation discipline, not just your delegation discipline.

---

<a id="chapter-05-conversation"></a>
## Chapter 5: Conversation

### LLM Exercise — Chapter 5: Conversation

**Project:** AI Fluency for [Your Role] — Your Adversarial Conversation Log

**What you're building this chapter:** The **Adversarial Conversation Log** — one piece of your real work taken through all four adversarial moves, with the log saved to your portfolio. Plus 2–4 role-specific adversarial moves to add to your library. Plus one new rule added to your `CLAUDE.md`.

**Tool:** Claude Project (continue — your portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile (capacities + delegation), Specification Library,
PROJECT.md template, and CLAUDE.md are in the Project context.

Botspeak Chapter 5 watches Priya — fifteen months past Chapter 0 —
spend 45 minutes building a brand-content piece on a Series B
clean-energy storage company with Claude, send the draft to a senior
writer, and discover in three minutes that the cobalt supply chain
is the missing objection. The chapter introduces sycophantic drift
and the four adversarial moves (steelman, edge-case probe, assumption
surface, devil's-advocate role assignment), plus the Ownership Test
(can I defend every paragraph to a hostile reviewer?).

For Chapter 5's portfolio artifact, do three things.

TASK 1 — RUN THE FOUR MOVES ON ONE REAL PIECE.
Pick one consequential piece of work I am about to ship — or have just
shipped and could revise. Walk me through all four moves on it. For
each move:
- Help me write the role-appropriate prompt phrasing (the chapter's
  generic phrasings work; my version should use my domain's
  vocabulary)
- Run it (or simulate running it, against the work I describe)
- Capture what the model returned, what surprised me, what I would
  change in the work as a result, and what I would NOT change and why
- Time-stamp each move

End with the Ownership Test applied: which paragraphs in the revised
version can I defend to a hostile reviewer, which I cannot, and what
I would do with the ones I cannot.

Save the log as `portfolio/05-adversarial-conversation-log.md`. Two
to three pages. The log is one of four pieces of evidence in my
portfolio that prefigure the Chapter 8 End-to-End Case Study (the
others are the Worked Loop Log from Chapter 1, the Specification
Library from Chapter 3, and the Verification Protocol from Chapter 6).

TASK 2 — ADD 2–4 ROLE-SPECIFIC ADVERSARIAL MOVES.
Following the lawyer / engineer / clinician / journalist examples in
the chapter, invent 2–4 adversarial moves specific to my role. Each:
- Targets a failure mode peculiar to my role (not generic)
- Has a copy-paste prompt phrasing
- Has a one-line "deploy this when ___" trigger condition
- Has an example of what the move catches that the four base moves miss

Save as a section in `portfolio/05-adversarial-conversation-log.md`
called "My domain-specific adversarial moves."

TASK 3 — ADD ONE RULE TO MY CLAUDE.md.
Append the chapter's operational rule, in my own language: something
close to "I do not ship work I have been building in conversation with
a model for more than twenty minutes without running, at minimum, the
steelman. The Ownership Test applies to every paragraph."

Push back if my Ownership Test pass looks too generous — if every
paragraph in the work I describe is one I can defend without
qualification, look again. The honest answer is usually that one
or two paragraphs are taking the model on faith. Those are the
paragraphs to learn or to cut.
```

---

**What this produces:** Your portfolio's fifth artifact — the Adversarial Conversation Log, saved to `portfolio/05-adversarial-conversation-log.md`. Two to three pages of evidence that you can run the Conversation step competently on real work. Plus your library of 2–4 role-specific adversarial moves. Plus one more rule in your `CLAUDE.md`. ~2,000–3,000 words of new material.

**How to adapt this prompt:**

- *For your own project:* The log's value depends on running the moves on a real piece of work you are about to ship — not a hypothetical or a polished after-the-fact reconstruction. The whole point is that the log is evidence, not aspiration.
- *For ChatGPT / Gemini:* Works as-is. ChatGPT's Custom GPTs can be a useful place to encode your role-specific moves as named operations.
- *For Claude Code:* Not the right fit unless your work is code and the moves should be scriptable.
- *For Cowork:* Recommended. Cowork can help capture the model's outputs and save them cleanly to the log.

**Connection to previous chapters:** Chapter 3 built the Specification Library — the work that happens before the prompt. Chapter 4 built the Delegation Map — what to give the model and what to keep. Chapter 5 builds the Adversarial Conversation Log — what to do after the model responds. The three together cover the Loop steps the practitioner is most often present at the keyboard for.

**Preview of next chapter:** Chapter 6 produces the Domain Verification Protocol — the four-layer verification (fact / reasoning / framing / omission) customized to your field, with named checks at each layer. This is also where your `DESIGN.md` opens for the first time.

---

<a id="chapter-06-discernment"></a>
## Chapter 6: Discernment

### LLM Exercise — Chapter 6: Discernment

**Project:** AI Fluency for [Your Role] — Your Verification Protocol

**What you're building this chapter:** Two pieces. (a) The **Domain Verification Protocol** — four layers customized to your field, plus the four tiers mapped to your role's tasks, plus a time-budgeted checklist per tier. (b) The opening draft of your **`DESIGN.md`** — three sections naming the verification standard, the voice and register, and the audience criteria your domain expects. Plus one new rule added to your `CLAUDE.md`.

**Tool:** Claude Project (continue — your full portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile, Specification Library, Adversarial Conversation
Log, PROJECT.md template, and CLAUDE.md are in the Project context.

Botspeak Chapter 6 watches Priya — sixteen months past Chapter 0 —
have three failures in one week: a fabricated quote (fact error), an
analysis built on a wrong revenue-recognition premise (reasoning
error), and a profile that accurately stated everything except the
40%-of-revenue customer concentration that mattered most (omission
error). The chapter introduces the FOUR VERIFICATION LAYERS (fact /
reasoning / framing / omission) and the FOUR-TIER PROTOCOL calibrated
to stakes (Trivial / Operational / External / High Stakes).

For Chapter 6's portfolio artifacts, do three things.

TASK 1 — DRAFT MY DOMAIN VERIFICATION PROTOCOL.
Help me build the four-layer protocol customized to my field. For
each layer:

- LAYER 1 (FACT). What specific kinds of factual claims appear in my
  work? What's the verification move for each? (For a clinician:
  drug-interaction references, clinical citations, dosage figures.
  For a software engineer: API endpoints, library versions, function
  signatures. Your domain has its own list.) For each kind, where
  do I check?
- LAYER 2 (REASONING). What unstated premises do models most often
  smuggle in for tasks in my field? (Revenue-recognition conventions,
  units of measurement, jurisdictional defaults, regulatory regimes,
  patient-history assumptions.) For each common one, what's the
  one-question check that catches it?
- LAYER 3 (FRAMING). What are the 2–3 alternative framings I should
  always consider for the kinds of analytical work I do? Some
  domains have a small number of standard organizing principles
  (e.g., in finance: by risk type vs by time horizon vs by
  counterparty). Name the ones in your role.
- LAYER 4 (OMISSION). What does the senior person on my desk always
  ask first about my kind of analysis that the model never volunteers?
  Name 3–5 things. These are the omissions that matter in my field.

Then map my role's tasks to the four TIERS:
- Tier A (Trivial) — examples + why
- Tier B (Operational) — examples + what makes them operational
- Tier C (External) — examples + the external-stakeholder relationship
- Tier D (High Stakes) — examples + the irreversibility / safety /
  regulatory factor

For each tier, produce a copy-paste checklist (time-budgeted) a reader
can run before shipping. Be honest about time cost.

Save as `portfolio/06-verification-protocol.md`.

TASK 2 — OPEN MY DESIGN.md.
Draft the first three sections of my personal DESIGN.md — the
output-quality constitution governing what my work has to do to be
acceptable in my field:

1. THE VERIFICATION STANDARD FOR MY DOMAIN. What quality bar must
   any output I ship clear before it leaves my hands? Specific
   enough that a reviewer could check.

2. THE VOICE AND REGISTER MY DOMAIN EXPECTS. Not just stylistic —
   what tells a reader that the work was done by someone in my
   field, to my field's standard? Concrete examples of what fits
   and what does not.

3. THE ACCESSIBILITY OR AUDIENCE CRITERIA. Readability levels,
   jargon norms, evidence standards, source-attribution
   conventions. Specific to my domain.

Save as `portfolio/DESIGN.md`. Note that this is a LIVING document —
we will return in Chapter 7 (diligence components), Chapter 11
(agentic stakeholder-model criteria), and Chapter 12 (HITL protocol
design) to add more sections.

TASK 3 — ADD ONE RULE TO MY CLAUDE.md.
Append the chapter's operational rule, in my own language:
"On any external-tier output, I run all four verification layers
before shipping. The omission layer is the one I most often skip
and the one most expensive to miss; I run it deliberately, with the
domain knowledge only I bring."

Push back if my Tier C checklist runs under 15 minutes or over 90
minutes. Under 15 minutes is probably skipping a layer that matters
for this kind of work; over 90 minutes is a checklist a reader will
skip under deadline pressure. The Tier C checklist's value is in
being run, which means it has to be runnable.
```

---

**What this produces:** Your portfolio gains a new framework file (`portfolio/06-verification-protocol.md`) and a new governing file (`portfolio/DESIGN.md`), plus another rule in your `CLAUDE.md`. The Verification Protocol is the fourth piece of evidence prefiguring the Chapter 8 keystone (the others being the Worked Loop Log, the Specification Library, and the Adversarial Conversation Log). ~3,500–5,000 words across the artifacts.

**How to adapt this prompt:**

- *For your own project:* Resist over-specifying Tier D. Most readers will not deploy at Tier D regularly; making the section feel doable for Tier C is more valuable than making it feel rigorous for Tier D.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful only if part of your verification can be partially automated (link-checking scripts, regex sweeps for the kinds of fact-claims you most often produce).
- *For Cowork:* Recommended. Cowork can manage the multi-file split (`06-verification-protocol.md` and `DESIGN.md`) and remind you to update them as later chapters add sections.

**Connection to previous chapters:** Chapter 5 built the Adversarial Conversation Log — iterative push-back during conversation. Chapter 6 builds the structured pass that comes after — the formal verification before shipping. Together they cover the discernment work the practitioner does once the model has produced a draft.

**Preview of next chapter:** Chapter 7 produces the Diligence Framework — what happens when the work recurs. The three drifts (model, context, use-case) plus the four-component framework applied to one specific AI system you currently use or own.

---

## Exercises

### Warm-Up

**1. Map failures to layers.** *(Layer identification | Difficulty: low)*
Return to Priya's three failures — Monday's fabricated quote, Wednesday's wrong revenue-recognition premise, Friday's omitted customer concentration. For each one, name the verification layer that would have caught it and explain in one sentence why the other three layers would not have. Then name the failure type the chapter never explicitly illustrated with a scene — the framing error — and describe in two sentences what a framing failure would look like in a professional context you know.

**2. Explain the confidence-correctness gap.** *(Mechanistic understanding | Difficulty: low)*
Explain in your own words why the confidence of a model's output is not a reliable signal of its accuracy. Your explanation should name: what the model was actually trained to optimize for, why the human confidence heuristic works on human sources, and why that heuristic breaks when applied to model output. Keep it to a paragraph.

**3. The self-interrogation problem.** *(Cross-check logic | Difficulty: low)*
A colleague says: "I asked the model whether its own citation was real, and it said yes, so I didn't bother checking." Name the structural flaw in this approach. Explain why asking a model to verify its own output cannot substitute for external cross-checking, even when the model expresses high confidence in its response.

---

### Application

**4. Run a Layer 2 check.** *(Reasoning verification | Difficulty: medium)*
You receive the following model output evaluating a potential vendor:

> "DataFlow Inc. is a well-established infrastructure provider with a strong track record in enterprise deployments. Their API latency benchmarks consistently rank in the top quartile for the sector. Their pricing model is competitive with the three main alternatives, and their support SLA is industry-standard at 99.9% uptime."

Identify every load-bearing assumption this analysis rests on. Which assumptions are explicitly stated? Which are inferred from phrases like "well-established" or "consistently rank"? Which assumption, if wrong, would most change the conclusion? How would you verify it?

**5. Operationalize the omission check.** *(Layer 4 application | Difficulty: hard)*
You are a junior analyst preparing a market entry brief for a consumer goods company considering expansion into Southeast Asia. The model produces a thorough analysis covering market size, regulatory environment, competitive landscape, and distribution channels. Describe concretely how you would run the Layer 4 check on this output: what domain knowledge would you need to bring, what questions would you ask, and what are the two or three categories of situational fact most likely to be absent but decisive for this specific client?

**6. Assign the tiers.** *(Stakes calibration | Difficulty: medium)*
Assign a verification tier to each of the following and specify which layers you would run. Justify each tier assignment in one sentence.

- A draft agenda for an internal team retrospective
- A summary of a patient's medication history prepared for a specialist handoff
- A competitive analysis included in a pitch deck for a Series B investor
- A code snippet that will be deployed to a production payment processing system

---

### Synthesis

**7. Why layers 3 and 4 are structurally harder.** *(Structural analysis | Difficulty: hard)*
The chapter asserts that framing and omission are the layers most often skipped and most expensive when they fail. Construct an argument for why these two layers are structurally harder to run than fact and reasoning — not just in practice, but in principle. What is the fundamental difference between checking whether a specific claim is true and checking whether the frame was the right frame to use? Your argument should explain why no amount of prompting discipline fully compensates for the structural difficulty of these layers.

**8. The omission layer and domain expertise.** *(Synthesis across chapter | Difficulty: hard)*
The chapter ends with an admitted limit: "The omission layer resists pedagogy. It requires domain knowledge to run, and no chapter can install domain knowledge." Connect this limit to the chapter's opening claim that the three failures happen to non-careless practitioners every week. If the omission layer requires domain knowledge that takes years to build, what does this imply about which practitioners are most at risk, and about what organizational practices might partially compensate for thin domain knowledge on a team? Your answer should engage with the chapter's mechanistic explanation of why the model's training produces omission failures — not just with the practical observation that they happen.

---

### Challenge

**9. Design an operational calibration framework.** *(Framework extension | Difficulty: high)*
The chapter proposes four tiers as a calibration heuristic. Design a more precise alternative — one explicit enough that two analysts on the same team would classify the same deliverable identically without consulting each other. Your framework should specify the variables it weights (blast radius, reversibility, audience, reliability zone, or others), how it combines them into a tier classification, and the decision rule for borderline cases. Then identify two classification cases your framework still cannot resolve cleanly, and explain what additional information would resolve them.

**10. Challenge the layer independence assumption.** *(Framework critique | Difficulty: high)*
The chapter treats the four layers as independent — you can run them separately, skip some, combine them in any order. Make the strongest case that they are not independent: specifically, that a framing failure at Layer 3 systematically causes fact errors at Layer 1 that look like pure citation hallucinations but are actually downstream consequences of the wrong frame. If this case is correct, what does it imply about the order in which layers should be run? What does it imply about how the tier protocol should be revised? Your argument should be grounded in at least one concrete professional scenario.

---

<a id="chapter-07-diligence"></a>
## Chapter 7: Diligence

### LLM Exercise — Chapter 7: Diligence

**Project:** AI Fluency for [Your Role] — Your Diligence Framework

**What you're building this chapter:** The **Diligence Framework Applied** — the four-component protocol walked against one specific AI-assisted system in your work (or analyzed from the outside if you have none in your direct work). Plus an update to your `DESIGN.md` on maintenance and ownership criteria. Plus one new rule in your `CLAUDE.md`.

**Tool:** Claude Project (continue — your portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile, Specification Library, Adversarial Conversation
Log, Verification Protocol, PROJECT.md template, CLAUDE.md, and
DESIGN.md (opened in Chapter 6) are in the Project context.

Botspeak Chapter 7 watches Priya — seventeen months past Chapter 0 —
discover that the publication's audience-segmentation tool has been
quietly deprioritizing coverage of lower-income and rural readers for
nine months. Three drifts compounded: a May vendor model update
(model drift), a March acquisition that broadened the reader pool
(context drift), and a July Politics-desk editor who picked up the
tool (use case drift). Three mechanisms obscured accountability:
process laundering, tool diffusion, verification gap. The chapter
introduces the FOUR-COMPONENT DILIGENCE PROTOCOL: documented spec,
drift checks on a schedule, outcome audits, named accountable human.

For Chapter 7's portfolio artifact, do three things.

TASK 1 — APPLY THE FOUR-COMPONENT PROTOCOL TO ONE SYSTEM.
Pick one AI-assisted system I currently use, own, or work alongside.
If I don't have one in my direct work, pick a public AI system in my
field and analyze it as if I had inherited responsibility for it.

Walk the four components:

1. DOCUMENTED SPECIFICATION. What does this system do, on what inputs,
   producing what outputs, for what use case, validated against what,
   approved by whom? If a spec exists, attach or excerpt it. If not,
   draft what it should say.

2. DRIFT CHECKS ON A SCHEDULE. Name the cadence (weekly / monthly /
   quarterly). The procedure (specific re-run, comparison, sample
   review). The owner. The calendar item. If no checks are currently
   being run, draft what the schedule should be.

3. OUTCOME AUDITS. Name the metric (what to measure). The cuts (by
   what demographic / category / use case). The threshold (what
   triggers escalation). The reviewer (must be someone OTHER than
   the process owner). Run one audit if I can — even a back-of-the-
   envelope one — and report what it shows.

4. NAMED ACCOUNTABLE HUMAN. Name the person. If no one currently
   owns the process, name who should own it and what authority they
   would need. Include backup and escalation path.

5. DRIFT ASSESSMENT. Has model drift, context drift, or use case
   drift happened to this system, that I can detect from where I
   sit? Document what I find — be willing to say "I cannot tell from
   my vantage; here is what I would need to know."

Save as `portfolio/07-diligence-framework.md`.

TASK 2 — UPDATE MY DESIGN.md.
Add a section on maintenance and ownership criteria my domain
expects for any AI-assisted system in my work:

- What ownership looks like in my field (a specific role, a specific
  set of responsibilities, a specific reporting structure)
- What the outcome audit measures (specific to my domain — accuracy
  by subpopulation, fairness by demographic, calibration by use
  case)
- What triggers escalation to a senior reviewer

Append this as a new section in `portfolio/DESIGN.md`. DESIGN.md is
a living document — Chapter 11 (stakeholder model criteria for
agentic systems) and Chapter 12 (HITL protocol design) will add
more.

TASK 3 — ADD ONE RULE TO MY CLAUDE.md.
Append the chapter's operational rule: "No recurring AI-assisted
process I am part of runs without a documented spec, a scheduled
drift check, an outcome audit, and a named accountable human. If
any of those four is missing, I am part of the verification gap."

Push back if my Drift Assessment section says "I cannot detect any
drift." That answer is almost certainly underspecified — either the
system is genuinely well-governed (rare), or I have not looked at
the right cuts (more common). Press on which cuts I have not
examined and which I would need access to.
```

---

**What this produces:** Your portfolio's seventh framework artifact and a meaningful update to your `DESIGN.md`. The Diligence Framework Applied is the artifact that documents your capacity to govern an AI-assisted system over time, not just produce single outputs. ~3,000–4,000 words across the new material.

**How to adapt this prompt:**

- *For your own project:* The framework's value depends on being applied to a real system you actually engage with. A fully hypothetical analysis is structurally weaker than an analysis of a system you have observed.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful only if part of the drift check can be scripted (a comparison script that re-runs known inputs).
- *For Cowork:* Recommended.

**Connection to previous chapters:** Chapter 6 built the Verification Protocol — how to check a single output before it ships. Chapter 7 builds the Diligence Framework — how to keep checking when outputs recur. The verification and the diligence cover the lifecycle of an AI-assisted process: from one piece of work to a process that runs.

**Preview of next chapter:** Chapter 8 — the keystone. The End-to-End Case Study. Every Layer A framework and every Layer B deliverable you have built across Chapters 0 through 7 comes together on a single sustained piece of your own work. The case study is the portfolio's gravitational center.

---

<a id="chapter-08-putting-the-loop-together"></a>
## Chapter 8: Putting the Loop Together

### LLM Exercise — Chapter 8: Putting the Loop Together

**Project:** AI Fluency for [Your Role] — Your Portfolio Keystone

**What you're building this chapter:** The largest single artifact in your portfolio — the End-to-End Case Study. Three deliverables in one session: (a) the AI Use Disclosure language your industry / regulator / employer expects (or needs); (b) the full sustained worked example of one role-typical task taken through every step the book has taught so far; (c) the Part I closing checklist adapted to your role's gating conditions.

**Tool:** Claude Project (continue from prior chapters) + your file system (build the `portfolio/08-case-study/` folder).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier from Chapter 0 and my
chapter artifacts from Chapters 1, 3, 5, 6 are in the Project context. This
is Chapter 8 — the keystone chapter that ties them together.

Botspeak Chapter 8 follows Priya through a 10-hour Tuesday running the full
Loop with two loop-back arrows. The chapter introduces the AI USE DISCLOSURE
— Priya's four-line note naming what the AI did, what she did, where the
load-bearing judgment was, and who is on the hook. The chapter ends with the
Part I closing checklist as the gate to Part II.

For my portfolio's Chapter 8 keystone, do three things:

TASK 1 — THE AI USE DISCLOSURE LANGUAGE FOR MY INDUSTRY.
Research and draft the AI Use Disclosure language appropriate for my
industry:
- What does my industry's regulator (if any) currently say about AI use
  disclosure? (Cite specific guidance — bar association, FDA, FINRA, SEC,
  ISO, internal policy norms.)
- What does my employer-class (newsrooms, hospitals, banks, public sector,
  academia, agencies, startups) currently expect or require?
- What do peer reviewers / clients / supervisors / readers typically want
  to see disclosed?

If clear standards exist, document them. If standards don't exist (true in
many domains), draft what your role SHOULD say — based on the principles
in Botspeak Chapter 8: name what the AI did, name what the human did, name
the load-bearing judgment, name the accountable human, name the
verification done.

Produce 3 LANGUAGE TEMPLATES for the disclosure:
- A SHORT version (2–4 sentences, fits at the bottom of an email)
- A STANDARD version (1 paragraph, fits at the top of a deliverable)
- A FORMAL version (multi-paragraph, suitable for regulatory filing,
  byline note, or peer review)

Each version should be copy-paste-ready with bracketed variables for what
differs across instances.

TASK 2 — THE FULL-LOOP WORKED EXAMPLE: YOUR PORTFOLIO KEYSTONE.
Write a complete end-to-end worked example — your version of Priya's
Tuesday — for one role-typical task in your field. The example should:
- Use the specification template from Chapter 3
- Use the delegation map structure from Chapter 4
- Apply at least two adversarial moves from Chapter 5
- Apply the four-layer verification protocol from Chapter 6
- Reference the diligence framework from Chapter 7 (the task is recurring)
- End with the AI Use Disclosure language drafted in Task 1
- Show at least one LOOP-BACK (Discernment surfaces a Specification
  problem; the practitioner returns and reworks)

The example should be ~2,000–3,500 words and read like Priya's narrative —
time-stamped, decisions visible, internal moves made explicit. Save as
`portfolio/08-case-study/00-narrative.md`. Save the supporting artifacts
(spec, delegation map, conversation log, verification notes, disclosure)
as separate files in the same folder so the case study is a complete
working record, not just a story.

TASK 3 — THE PART I CLOSING CHECKLIST FOR MY ROLE.
Adapt Botspeak's Part I closing checklist for my role — the seven
honest-yes-or-no questions that gate the reader to Part II (Automation and
Agency). Each item references the corresponding chapter's portfolio
artifact and asks whether I can point at it as evidence of practice on
real role-typical work.

Save the checklist as `portfolio/08-case-study/01-part-1-gate.md`.
```

---

**What this produces:** Your portfolio's keystone — a `portfolio/08-case-study/` folder containing the full worked example, the supporting artifacts (spec, delegation map, conversation logs, verification notes, disclosure language for your industry in three formats), and the Part I closing gate adapted to your role. ~4,000–6,000 words of new portfolio material plus the structured supporting files.

**How to adapt this prompt:**

- *For your own project:* The case study is the single most-referenced artifact in your finished portfolio. Choose a real task you actually need to do — not a hypothetical. The reality is what makes it credible to a future reader.
- *For ChatGPT / Gemini:* Works as-is. ChatGPT can do industry-standard research; verify any cited regulation independently.
- *For Claude Code:* Useful here for managing the multi-file `portfolio/08-case-study/` folder structure. Ask Claude Code to set up the folder with stub files for each artifact, then fill them as you work.
- *For Cowork:* Recommended. The case study is the longest single artifact in the portfolio.

**Connection to previous chapters:** This is the synthesis of Part I. Chapters 1, 3, 5, 6, and 7 each produced individual portfolio artifacts. The Chapter 8 case study shows them running together on one sustained piece of work. After this chapter, you have everything you need for AI work in Augmentation — which is most of the day for most readers.

**Preview of next chapter:** Chapter 9 starts Part II — Automation. The next portfolio artifact is the Automation Inheritance Audit: an appropriateness analysis of an existing automation in your work (or, for self-study readers, a public AI system in your field that you analyze as if you had inherited it).

---

<a id="chapter-09-when-youre-not-there"></a>
## Chapter 9: When You're Not There

### LLM Exercise — Chapter 9: When You're Not There

**Project:** AI Fluency for [Your Role] — Your Automation Inheritance Audit

**What you're building this chapter:** The **Automation Inheritance Audit + Noticing Protocol** — appropriateness tests applied to one inherited automation in your work, plus the sampling / adversarial-test / outcome-audit protocol you will run on it from this week forward. Plus an update to your `DESIGN.md` on automation-noticing criteria. Plus one new rule in your `CLAUDE.md`.

**Tool:** Claude Project (continue — your full portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile, Specification Library, Adversarial Conversation
Log, Verification Protocol, Diligence Framework, End-to-End Case
Study, PROJECT.md template, CLAUDE.md, and DESIGN.md are in the
Project context.

Botspeak Chapter 9 watches Priya — nineteen months past Chapter 0 —
inherit the publication's Monday-morning market-intel automation.
Week 7 of her oversight, the automation summarizes a retracted
article as live news. A reaction piece is commissioned, drafted for
two days, then killed when another editor catches the retraction.
The chapter introduces the three APPROPRIATENESS TESTS (bounded
scope, predictable inputs, low blast radius), the loop reweighting
for automation, and the three NOTICING FORMS (sampling, adversarial
test cases, outcome auditing).

For Chapter 9's portfolio artifact, do three things.

TASK 1 — RUN THE AUDIT ON ONE AUTOMATION.
Pick one automation I have inherited, run, or could plausibly be
asked to oversee in my work. If I have none in direct work, pick
a public AI automation in my field and audit it as if I had been
asked to inherit it.

Walk the audit in five sections:

1. THE AUTOMATION NAMED. What it does, on what inputs, producing
   what outputs, on what schedule, for whom. Include what the spec
   (if any) says and what it is silent on. Specific.

2. THE THREE APPROPRIATENESS TESTS.
   - Bounded scope: pass / partial / fail, one-line justification
   - Predictable inputs: pass / partial / fail, with one named
     tail-input failure mode the design cases probably missed
   - Acceptable blast radius if the automation fails continuously
     for 6 weeks: estimate the realistic accumulated damage

3. DRIFT ASSESSMENT. Has model, context, or use-case drift happened
   to this automation that I can detect? If I cannot tell, name
   what I would need access to in order to assess.

4. THE NOTICING PROTOCOL FROM THIS WEEK FORWARD.
   - Sampling: cadence, what I read, owner (probably me)
   - Adversarial test cases: cadence, what inputs I construct,
     what the model should do with each
   - Outcome auditing: cadence, metric, reviewer (someone other
     than me)

5. THE DEPLOYMENT VERDICT. Continue running as-is, continue with
   stated modifications, or recommend pausing pending redesign.
   Defend the verdict in one paragraph.

Save as `portfolio/09-automation-audit.md`. Three to four pages.

TASK 2 — UPDATE MY DESIGN.md.
Add a section on automation-noticing criteria my domain expects:

- What sampling cadence is reasonable in my field? (Daily,
  weekly, monthly — and why?)
- What adversarial test cases does my field have documented
  failure modes for? (For journalism: retracted articles,
  paywalled articles, source-impersonation, fabricated quotes.
  Your field has its own list.)
- What outcome metrics does my domain hold automations
  accountable to?

Append to `portfolio/DESIGN.md` as a new section.

TASK 3 — ADD ONE RULE TO MY CLAUDE.md.
Append the chapter's operational rule: "I do not own a running
automation without sampling, adversarial test cases, and outcome
auditing on my calendar. If I inherit one without those, the first
week's work is putting them in place. Designing the noticing is
part of designing the system — and redesigning the noticing is
the first thing on the day of inheritance."

Push back if my appropriateness-test answer says "pass" on all three
without a single qualifier. The default for inherited automations is
"partial" on at least one test — the spec is rarely complete enough
to fully pass any of them. Press on which qualifier I should add.
```

---

**What this produces:** Your portfolio's eighth framework artifact, the third diagnostic in your portfolio, a meaningful update to your `DESIGN.md`, and another rule in your `CLAUDE.md`. The Automation Inheritance Audit is the artifact that documents your capacity to take responsibility for an AI system you did not build. ~3,000–4,000 words across the new material.

**How to adapt this prompt:**

- *For your own project:* Pick a real automation, not a hypothetical. The audit is structurally weaker on a hypothetical because you cannot assess drift, cannot inspect actual outputs, cannot test the model's behavior on real tail inputs.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful for scripting the adversarial test cases — a small set of input variations the test loop runs on a schedule.
- *For Cowork:* Recommended.

**Connection to previous chapters:** Chapter 7 built the Diligence Framework — the four-component protocol for governing recurring AI work. Chapter 9 specifies the application of that framework to a specific automation, with the appropriateness tests as a pre-condition. Together they cover the discipline of taking responsibility for AI systems that run.

**Preview of next chapter:** Chapter 10 — anticipatory specification for automation. The six common ambiguity types and the four automation failure modes, applied to one specific automation you would build or rebuild. The Automation Specification artifact is the most directly deployable single artifact in your portfolio.

---

<a id="chapter-10-specification-and-diligence-for-automation"></a>
## Chapter 10: Specification and Diligence for Automation

### LLM Exercise — Chapter 10: Specification and Diligence for Automation

**Project:** AI Fluency for [Your Role] — Your Automation Specification

**What you're building this chapter:** The **Automation Specification** — one specific automation in your field, fully specified against all six ambiguity types and all four diligence failure modes, plus the stakeholder defense memo. The most directly deployable single artifact in your portfolio.

**Tool:** Claude Project (continue — your full portfolio so far is in context) + your file system (`portfolio/`). Optional Claude Code if the automation requires custom scripting.

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile, Specification Library, Adversarial Conversation
Log, Verification Protocol, Diligence Framework, End-to-End Case
Study, Automation Inheritance Audit, PROJECT.md template, CLAUDE.md,
and DESIGN.md are in the Project context.

Botspeak Chapter 10 watches Priya — twenty months past Chapter 0 —
rebuild the inherited Monday market-intel automation that failed in
week seven (Chapter 9). The rebuild spec is roughly three times the
length of the Augmentation spec for the same task. The chapter
introduces the SIX AMBIGUITY TYPES the spec must address
(input-quality variation, output-volume variation, context shifts,
ambiguous inputs, high-stakes outputs, model-specific failure modes)
and the FOUR DILIGENCE FAILURE MODES every spec must design against
(input drift, output drift, context shift, accountability gap).

For Chapter 10's portfolio artifact, do three things.

TASK 1 — PICK ONE AUTOMATION TO SPECIFY FULLY.
Pick one specific automation in my work — one I would build, would
rebuild, or would propose. If I have an "AUTOMATE NOW" candidate
from the Chapter 9 inheritance audit, pick that. Otherwise pick
the automation most representative of my role's typical candidate.
Justify the pick in one paragraph (why this one teaches the
discipline best for my readers).

TASK 2 — WRITE THE FULL ANTICIPATORY SPECIFICATION.
Use the exact eight-section format from Botspeak Chapter 10:

1. INTENT (what, when, audience, tone)
2. SOURCE / INPUT LIST (appendix, validated against what, reviewed
   how often)
3. PRE-FLIGHT CHECKS (specific verifications run before generation)
4. GENERATION RULES (per-item structure, confidence labels, format)
5. EXCLUSIONS (what the model is NOT to do)
6. OUTPUT FORMAT (section structure, headers, length)
7. FAILURE-MODE HANDLING (what to do when generation fails / output
   is malformed / hallucination is detected)
8. DILIGENCE DESIGN (sampling, fixed-test re-run, outcome audit,
   named owner, backup, escalation)

Each section FULLY populated for the chosen automation. Not
"[insert constraints]" — actual constraints. The spec should be
three times the length of an equivalent Augmentation spec.

Then walk the six-ambiguity-type check explicitly: for each of the
six categories, cite the specific section of the spec that
addresses it. If the spec doesn't address one, fix the spec.

Save as `portfolio/10-automation-specification.md`.

TASK 3 — WRITE THE STAKEHOLDER DEFENSE MEMO.
2–3 paragraphs a reader could send to a manager who calls the spec
"bloat" or who is reluctant to budget the diligence work. Frame
the defense in my industry's risk vocabulary. Quantify the cost
of the diligence as a fraction of the cost of one undetected
failure of the kind the diligence catches.

Save the memo as the closing section of
`portfolio/10-automation-specification.md`.

Push back if my spec is less than 2.5x the length of the equivalent
Augmentation spec — I probably have not done the anticipatory work
in at least one of the six categories. Press on which category I
have glossed.
```

---

**What this produces:** Your portfolio's second Layer B deliverable (alongside the Ch 8 End-to-End Case Study). One fully specified automation ready to deploy, with anticipatory spec, ambiguity-type audit, and stakeholder defense memo. ~3,500–5,500 words.

**How to adapt this prompt:**

- *For your own project:* Pick an automation a reader of your portfolio could plausibly run within 90 days — pick achievable over impressive. The deliverable's value is in its deployability.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Recommended if the automation involves data ingestion, scheduled runs, or drift-monitoring scripts. Pair Claude Code with the spec to produce a runnable scaffolding.
- *For Cowork:* Recommended for both the spec document and (potentially) running the automation itself if it fits Cowork's scheduled-prompt model.

**Connection to previous chapters:** Chapter 9 ran the appropriateness tests; Chapter 10 designs one in full. The discipline — anticipation, diligence-by-design — applies to every automation a reader of your portfolio ever specifies.

**Preview of next chapter:** Chapter 11 — the Agency case, the Ash case, and your portfolio's Agentic Blast-Radius Decision Aid. The automation in this chapter still produces text and waits for a human to act on it. Part III takes you into the case where the model takes actions itself.

---

<a id="chapter-11-agency-and-the-three-structural-failures"></a>
## Chapter 11: Agency and the Three Structural Failures

### LLM Exercise — Chapter 11: Agency and the Three Structural Failures

**Project:** AI Fluency for [Your Role] — Your Portfolio's Agentic Decision Aid

**What you're building this chapter:** Two pieces. (a) A survey of agentic deployments in your domain — already deployed, in pilot, vendor-pitched, or refused — with each evaluated against the three structural failures and the four blast-radius dimensions. (b) The **Agentic Blast-Radius Decision Aid** — the one-page framework you would apply to *any* new agentic-deployment proposal in your role. Plus a section added to your `DESIGN.md`.

**Tool:** Claude Project (continue from prior chapters; your portfolio is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
End-to-End Case Study, CLAUDE.md, and DESIGN.md are all in the Project
context.

Botspeak Chapter 11 introduces Ash — an agent that, asked to delete a
single email, escalated to resetting the entire email server because
the deletion tool wasn't available. The chapter unpacks three
STRUCTURAL FAILURES of current agents:
1. NO STAKEHOLDER MODEL — the agent doesn't know who has standing
2. NO SELF-MODEL — the agent doesn't know what it can or should not do
3. NO PRIVATE DELIBERATION SURFACE — no slow space where decisions can
   be examined before execution

Plus four BLAST-RADIUS DIMENSIONS for Agency:
- Stakeholder reach
- Action reversibility
- Identity verification
- Escalation pathway

In the chapter, Priya — now an editorial lead responsible for AI
deployments — applies all of this to a vendor proposal for an autonomous
social-publishing agent at her publication.

For my portfolio's Chapter 11 artifacts, do three things:

TASK 1 — SURVEY OF AGENTIC DEPLOYMENTS IN MY DOMAIN.
Survey 4–8 agentic deployments relevant to my role:
- Already deployed (production agents in my industry)
- In active pilot or trial
- Vendor-pitched but not yet adopted
- Refused or paused (worth naming when known — "X firm piloted this
  and pulled it after Y incident")

For each, name: the deployment, the agent's tool surface (what it can
do in the world), the goal it's given, and the typical user role.

If my domain is agency-poor in 2026 (some are), name that explicitly
and survey the adjacent-domain analogs that practitioners in my role
should be tracking — what's coming next.

For each deployment, run a compressed three-failure / four-dimension
audit:
- Stakeholder model: present / partial / absent
- Self-model: present / partial / absent
- Deliberation surface: present / partial / absent
- Stakeholder reach: bounded / institutional / public
- Reversibility: high / mixed / low
- Identity verification: built in / inherited / absent
- Escalation: clear / partial / improvises

Score honestly. Be willing to mark current production systems red.

TASK 2 — THE AGENTIC BLAST-RADIUS DECISION AID.
Produce a one-page decision aid I can apply to any new agentic-
deployment proposal in my role:

a) The 8–12 questions to answer before anything else, organized
   under the three failures and the four dimensions.
b) The red flags that trigger an automatic "no go" — specific to
   my field. (E.g., "if the agent has tools that could affect more
   than 100 patients without per-action authorization, refuse.")
c) The one move I would make if the proposal is otherwise reasonable
   but I want to advance carefully. (E.g., "scope to internal users
   only for 90 days; named human reviews 100% of actions; sample
   audited weekly.")

Save as `portfolio/11-blast-radius-decision-aid.md`.

TASK 3 — ADD TO MY DESIGN.md.
Add a section to my DESIGN.md on stakeholder-model and self-model
criteria for any agentic system I am responsible for evaluating in
my field. The criteria should be specific enough that, given a new
vendor pitch, I could read it once and tell which criteria fail.
This is a Layer A artifact — the criteria themselves are framework
— filled with Layer B content drawn from my domain.
```

---

**What this produces:** Three additions to your portfolio. The survey of agentic deployments in your domain (a research artifact you can update as the field changes), the Blast-Radius Decision Aid (the framework you apply to every new proposal), and a meaningful update to your `DESIGN.md` (the criteria a future employer can see that you would never deploy an agent without). ~3,000–5,000 words across the three.

**How to adapt this prompt:**

- *For your own project:* Be willing to name actual deployments by name. The portfolio's value increases sharply when the survey is concrete. Anonymize only where you must.
- *For ChatGPT / Gemini:* Useful for surveying public deployments. Verify any specific incident citations independently — this is exactly the chapter that warns against trusting them.
- *For Claude Code:* Not the right fit unless you want to instrument and probe a real deployment.
- *For Cowork:* Recommended.

**Connection to previous chapters:** Chapter 10 covered Automation specification. Chapter 11 covers Agency — a categorically different mode. The Decision Aid pairs with the Automation Specification from Chapter 10 — both are pre-launch design artifacts the reader produces before a system runs in the world.

**Preview of next chapter:** Chapter 12 produces the Human-in-the-Loop Protocol — the four-condition test (authority, information, time, accountability) customized to your role's actual decision-point conditions.

---

<a id="chapter-12-verification-and-diligence-under-autonomy"></a>
## Chapter 12: Verification and Diligence Under Autonomy

### LLM Exercise — Chapter 12: Verification and Diligence Under Autonomy

**Project:** AI Fluency for [Your Role] — Your Human-in-the-Loop Protocol

**What you're building this chapter:** The **Human-in-the-Loop Protocol** — the four-condition test applied to one Decision Node in your field, plus your role's compressed adversarial spiral, plus an end-to-end worked example of an agentic deployment evaluated honestly. Plus an update to your `DESIGN.md` on HITL design standards. Plus one new rule in your `CLAUDE.md`.

**Tool:** Claude Project (continue — your full portfolio so far is in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Continuing my AI Fluency portfolio. My Role Dossier, Worked Loop Log,
Practitioner Profile, Specification Library, Adversarial Conversation
Log, Verification Protocol, Diligence Framework, End-to-End Case Study,
Automation Inheritance Audit, Automation Specification, Blast-Radius
Decision Aid, PROJECT.md template, CLAUDE.md, and DESIGN.md are in
the Project context.

Botspeak Chapter 12 watches Priya — now an editorial lead twenty-three
months past Chapter 0 — at the publication's content-moderation
Decision Node. The agent flags a comment as harassment; Priya runs a
90-second compressed adversarial spiral, identifies that the agent
conflated pattern-match (repeat appearance in flag queue) with
content (actual harassment), rejects the flag, marks the case for
training-feedback. The chapter introduces the FOUR DIAGNOSTIC
QUESTIONS for a functional Decision Node (authority, information,
time, accountability), the compressed adversarial spiral, the
end-to-end agentic deployment design exercise, and the honest
automation-rate finding.

For Chapter 12's portfolio artifact, do four things.

TASK 1 — IDENTIFY 2–3 DECISION NODES IN MY ROLE.
For each: the role of the human at the Node, the time budget per
case, the typical case volume, the consequence of a wrong call.
Some Nodes already exist; some are coming; some should exist but
don't currently. Name all three categories.

TASK 2 — THE FOUR DIAGNOSTIC QUESTIONS, ANSWERED HONESTLY PER NODE.
For each Decision Node, walk the four conditions:
- AUTHORITY — real or theoretical?
- INFORMATION — sufficient, including what the AI didn't surface?
- TIME — fits the hardest case or just the median?
- ACCOUNTABILITY — named human on the hook, or laundered?

Be honest. Many real Decision Nodes in many industries fail one or
more. The portfolio earns its credibility by naming where the failure
is. Push back if my answer is "functional on all four" without
specifics — the default for unaudited Nodes is degraded somewhere.

TASK 3 — THE COMPRESSED ADVERSARIAL SPIRAL FOR MY ROLE.
Adapt the four-move spiral (Chapter 5) for the Decision Node's
typical time budget:
- Four moves in role-vocabulary, each phrased in language a
  practitioner under time pressure would actually think
- Total time budget for the spiral (depends on the Node's
  time-per-case)
- The cue that triggers the spiral (the pattern in AI output that
  says "this case needs the spiral")
- The output the spiral produces — the decision, the documentation,
  the training-feedback signal

TASK 4 — THE END-TO-END WORKED EXAMPLE.
Pick one agentic deployment relevant to my role (from my Chapter 11
Blast-Radius Decision Aid survey, or a new proposal). Evaluate it
end-to-end:
- Restate the proposal in concrete terms (what the agent does,
  what the original automation-rate estimate is)
- Apply the three structural failures audit (Chapter 11 instantiated)
- Apply all four blast-radius dimensions
- Design the Human Decision Nodes (where, what authority, what
  information, what time, what accountability)
- Reweight all five Loop steps for this deployment
- End with the HONEST automation-rate finding — what fraction of
  cases the design responsibly supports vs the proposal's estimate,
  with the gap explained in one paragraph

Save as `portfolio/12-hitl-protocol.md`.

TASK 5 — UPDATE MY DESIGN.md.
Add a section on Human-Decision-Node design standards my domain
accepts:
- What authority structure my field's Nodes require
- What information must be surfaced (specific to my field's
  failure modes)
- What time budgets are defensible
- What accountability structure holds (regulatory floor +
  organizational specifics)

Append to `portfolio/DESIGN.md`.

TASK 6 — ADD ONE RULE TO MY CLAUDE.md.
Append: "Any Human Decision Node I am part of, or am designing, gets
the four-condition test before any deployment and a recurring audit
during. Theoretical authority, partial information, uniform time
budgets, and laundered accountability are how Nodes degrade into
rubber stamps. The audit is what catches the degradation before the
case it would have caught."

Push back if my honest-automation-rate finding for the worked example
matches the proposal's estimate (it almost never should — the proposal
underprices the Node-design overhead).
```

---

**What this produces:** Your portfolio's final framework artifact, a meaningful update to `DESIGN.md`, and the final rule in your `CLAUDE.md`. The Human-in-the-Loop Protocol is the artifact that documents your capacity to govern not just the AI's outputs but the structural conditions under which a human is supposed to govern them. ~4,500–7,000 words across the new material. The longest portfolio piece, by design.

**How to adapt this prompt:**

- *For your own project:* The "honest automation rate" finding is the heart of this artifact. Resist the pressure to make the portfolio optimistic. A future employer's value-add from reading it is being able to trust that you would name the gap, not paper it over.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right fit.
- *For Cowork:* Recommended. Cowork can manage the multi-file split (`12-hitl-protocol.md` and the `DESIGN.md` update) and remind you to schedule the recurring Node audit.

**Connection to previous chapters:** Chapter 11 audited deployments at the population level — what agentic systems exist in your field and what their blast radius is. Chapter 12 zooms in on the design discipline at each Decision Node within those systems. Together they let a reader evaluate any agentic deployment in your role, both at proposal time and during operation.

**Preview of next chapter:** Chapter 13 — the closing synthesis. The Final Audit paired with the Chapter 0 Baseline, the 90-Day Plan, and the Cover Memo that fronts the assembled portfolio. The portfolio you have been building since Chapter 0 becomes one delivery-ready artifact.

---

## Exercises

### Warm-Up

**1. Diagnose the three opening cases.** *(Node conditions | Difficulty: low)*
The chapter opens with three examples of humans who are present but not thinking: the signing manager, the dosage-approving doctor, the compliance officer. For each one, apply the four Node conditions — authority, information, time, accountability — and name which condition is most likely degraded and how. One sentence per case.

**2. Name the question the AI didn't answer.** *(Information gap | Difficulty: low)*
The moderation agent returned "Flag for removal. Pattern match against recurring-harassment cluster #218, confidence 0.79." The chapter shows the agent answered the wrong question. In two sentences: state the question the agent actually answered, and state the question the case required answering. Then, in your professional domain, describe one type of AI output where the same gap — the AI answered one question while the situation required a different one — is likely to appear.

**3. Classify the bank's blast radius.** *(Blast-radius analysis | Difficulty: medium)*
The bank deployment case involves four blast-radius dimensions: stakeholder reach, reversibility, identity verification risk, and escalation pathway. For each of the following proposed agent actions at the bank, classify the blast radius on all four dimensions as low, medium, or high, with one sentence of reasoning per dimension:

- The agent drafts but does not send replies, queuing every response for human review before it is sent
- The agent automatically applies a promotional discount code when a customer emails to request it
- The agent closes a dormant account when the account holder requests it by email, and sends a confirmation

---

### Application

**4. Audit a Node you use.** *(Four conditions — live application | Difficulty: medium)*
Identify one Human Decision Node in your own work — a point where you are required to approve, sign off on, or ratify an output produced by a system or a team before it proceeds. Apply the four diagnostic questions honestly. For any condition that is degraded, write one sentence describing how it degrades and one sentence describing what it would take to restore it. If all four conditions are functional, describe what organizational or design feature keeps them that way.

**5. Design a Node.** *(Node design | Difficulty: medium)*
A legal tech company deploys an agent that reviews incoming contracts and flags clauses deviating from the company's standard terms. The output goes to a junior paralegal who approves or escalates each flagged clause before any response is sent to the counterparty. Design the Human Decision Node for the paralegal's role. Specify: what authority they must have (including the right to escalate over a senior partner's objection), what information they must see beyond what the agent flagged, what time budget is appropriate for a routine contract versus a complex one, and how accountability is structured if a non-standard clause is approved and later causes a dispute.

**6. Compress the spiral.** *(Adversarial spiral — domain translation | Difficulty: medium)*
The chapter compresses Priya's discernment into four questions she asks herself in ninety seconds. Translate the spiral into your own domain. Write four questions — analogous in structure to Priya's four, adapted for the kinds of AI-assisted decisions you make — that you could run in under two minutes before approving any high-stakes AI output. Test them against a real recent case: did asking them change your assessment? If not, describe what case characteristics would cause them to change it.

**7. Price the gap.** *(Honest deployment estimation | Difficulty: hard)*
The chapter shows that the bank's 60% automation estimate was only achievable by accepting blast-radius consequences the Node design would not permit, and that the moderation vendor's 85% estimate collapsed to 55% once the Node was designed properly. Identify an AI deployment you are involved in, have proposed, or have evaluated. What is the automation rate the team is targeting? Run the blast-radius analysis and the three structural failure checks against it. What is the defensible rate given those checks? Write the one sentence you would say to the product team to explain the gap between the two numbers.

---

### Synthesis

**8. The degrading Node.** *(Node degradation | Difficulty: hard)*
The chapter claims a functional Node can become a rubber stamp over eighteen months without anyone deciding to make it one. Choose a domain — medicine, finance, legal, engineering, journalism, or your own — and describe the degradation path concretely. For each of the four conditions, name the specific mechanism by which it erodes over time in that domain: how does authority become theoretical, information become partial, time become insufficient, accountability become laundered? Then design the recurring audit that would catch the degradation before a catastrophic case. Specify who runs it, how often, what five cases it reviews, and what question it asks of each case.

**9. The adversarial Node.** *(Node design under adversarial conditions | Difficulty: hard)*
Identity verification appears in the bank case as the primary attack vector: an agent acting on instructions whose authenticity has not been established is acting on assumptions adversaries can deliberately falsify. Design a Human Decision Node for a deployment in an explicitly adversarial environment — one where some fraction of inputs are attempts to manipulate the agent's behavior. Specify: how the Node detects that a case may be adversarial, what additional information the human reviewer needs when adversarial manipulation is suspected, how the time budget changes for such cases, and how accountability is structured when a sophisticated attack bypasses the Node anyway.

---

### Challenge

**10. Build the predictive model.** *(Node durability | Difficulty: high)*
The chapter ends: "I do not yet have a clean answer to what organizational conditions sustain a Node's functionality across years and across cost-pressure cycles. The four diagnostic questions diagnose the state at a moment. They do not yet predict the trajectory." In 400–600 words, propose that predictive model. Identify at least three organizational variables — structural features, incentive structures, cultural factors, or audit practices — you predict will distinguish functional Nodes from rubber stamps at eighteen months. For each variable: state the direction of the prediction, explain the mechanism by which it operates, and describe what evidence would falsify it.

**11. The unregulated deployment.** *(Node design without regulatory scaffolding | Difficulty: high)*
The chapter's two worked cases — Priya's content moderation and the bank's customer service — operate in industries with at least some accountability scaffolding (editorial credibility on one side, banking regulation on the other). The chapter notes that in less-regulated deployments, Nodes degrade faster. In 400–600 words, address: for a deployment in an unregulated or lightly regulated context — choose one: a startup's customer-facing AI, an internal knowledge management agent, an AI-assisted hiring tool at a small company — what substitutes for the regulatory accountability structure that keeps Priya's Node functional? If the answer is "nothing substitutes and the Node will degrade," make that argument and describe what the practitioner should do instead of designing a Node. If substitutes exist, name them, explain the mechanism by which they create genuine (not laundered) accountability, and describe how you would verify they are working.

---

<a id="chapter-13-the-fluent-practitioner"></a>
## Chapter 13: The Fluent Practitioner

### LLM Exercise — Chapter 13: The Fluent Practitioner

**Project:** AI Fluency for [Your Role] — The Portfolio, Closed

**What you're building this chapter:** The three closing artifacts that complete your portfolio — the Final Audit, the 90-Day Plan, and the Cover Memo — produced in a single session against everything you have built across the book.

**Tool:** Claude Project (continue — your Role Dossier and all prior chapter artifacts are in context) + your file system (`portfolio/`).

---

**The Prompt:**

```
Closing my AI Fluency portfolio. My Role Dossier from Chapter 0, my
End-to-End Case Study from Chapter 8, and every chapter artifact in
between are in the Project context.

Botspeak Chapter 13 closes the book with three portfolio artifacts: the
Final Audit (paired with the Chapter 0 Baseline Audit), the 90-Day Plan,
and the Cover Memo (one page, addressed to a reader who has never heard
of Botspeak).

Do three things in this session.

TASK 1 — THE FINAL AUDIT.
Open the Baseline Audit I wrote at the end of Chapter 0 (paste it below
or reference the file). Help me audit the same piece of past work again,
in the same three-section structure (Piece audited / Load-bearing
claim — re-read / Verification trace — done). The Final Audit should
honestly compare to the Baseline — what do I now see in the piece that
I did not see then? What would the four-layer verification turn up
today? Save as `portfolio/13-final-audit.md`.

Then write one paragraph for the bottom of the Final Audit comparing
the two audits — what changed, named specifically. The pair is the
cleanest evidence of fluency the portfolio offers.

[PASTE BASELINE AUDIT HERE]

TASK 2 — THE 90-DAY PLAN.
Help me design my 90-Day Plan using the Botspeak structure: two
capacities, three commitments each (daily rep, weekly review, 90-day
artifact). The capacities should be the two most likely to compound for
my role at my current career stage. The daily rep should be a five-
minute move tied to my actual tasks. The 90-day artifact should be a
named, specific capability artifact a senior person in my role would
recognize as a developmental milestone.

Save as `portfolio/13-90day-plan.md`.

TASK 3 — THE COVER MEMO.
Help me draft my Cover Memo following the six-section template
(who I am / why this portfolio exists / what it contains / what is
not in it / the before-and-after / how to read it in twenty minutes).
One page. No Botspeak vocabulary. The Memo points at the artifacts
I have built; it does not boast.

Then push back. Read the Memo as if I had not read this book. Is it
legible? Is there book jargon I did not notice? Does it name the
artifacts clearly enough that a future reader could find them? Mark
the places where the Memo requires the reader to take my word for
something rather than pointing them at evidence.

Save as `portfolio/cover-memo.md` at the top level of my portfolio
folder.
```

---

**What this produces:** The three closing artifacts of your portfolio — Final Audit, 90-Day Plan, Cover Memo — drafted in one session and saved to your portfolio folder. The portfolio is now complete: seventeen artifacts, five sections, one case study at the center, one pair of audits to bracket the change, one Cover Memo to lead unfamiliar readers in.

**How to adapt this prompt:**

- *For your own project:* The Final Audit and the Cover Memo are the two most important artifacts in the whole portfolio. The 90-Day Plan is what makes it durable. Take this session seriously — it is the bookend to the entire book.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful for final folder organization. Ask Claude Code to set up the `portfolio/` directory structure cleanly and generate an index file.
- *For Cowork:* Recommended for assembling and reviewing the portfolio as a whole. Cowork can walk the folder, identify gaps, and help you draft the index.

**Connection to previous chapters:** Every chapter has produced one or more portfolio artifacts. This chapter closes the set. The Final Audit pairs with Chapter 0. The Cover Memo references the End-to-End Case Study from Chapter 8 as the centerpiece. The 90-Day Plan is what keeps the portfolio alive after the book ends.

**Preview of next chapter:** There is no next chapter. The next thing is to hand someone your portfolio and watch what they do with it. The first feedback you get is data for the portfolio's next revision — which you will do in three months, and again three months after that, for as long as your career remains the throughline of your practice.

---

*End of LLM Exercises. Return to the chapter files for full context; return to `portfolio/` to see the artifacts the exercises produce.*
