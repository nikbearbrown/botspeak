# The Claude Project — Reader Setup Reference

*A single reference for what the reader's Claude Project looks like across the book. Set up once in Chapter 0. Returned to every chapter. Survives the book to become the traveling kit that holds the portfolio together.*

This is the reference the chapter LLM exercises assume but never give in one place. Read it the day you start Chapter 0. Return to it whenever you want to know what should be in the Project at a given point.

---

## What the Claude Project actually is

A Claude Project (the feature inside `claude.ai`) is a persistent context for a long-running working relationship. You set it up once. You add reference files to it. You set a system prompt that governs how Claude responds inside that Project. Every conversation you start inside the Project inherits the context.

For Botspeak, the Project does three things:

1. **Holds your Role Dossier.** The Project always knows who you are professionally, what you do, and what kind of work the chapter exercises should adapt to. You do not re-explain your role every chapter.
2. **Holds your governing files.** Your `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` template live in the Project as attached files. Every chapter exercise can reference them. When a chapter adds a rule to `CLAUDE.md`, you replace the attached file.
3. **Holds your portfolio artifacts as they accrete.** The artifacts you produce in each chapter's LLM exercise live in a `portfolio/` folder on your computer and (selectively) attached to the Project so Claude has context on what you have already built.

When the book is done, the Project does not retire. It becomes the working environment in which you keep the portfolio alive — adding case studies, refreshing the audits, drafting the next 90-day plan.

---

## Setting it up — at Chapter 0

**Step 1.** Open `claude.ai` → Projects → New Project. Name it: **AI Fluency for [Your Role]**.

**Step 2.** Paste this into the Project's Custom Instructions field:

```
I am working through the textbook BOTSPEAK by Nik Bear Brown. Across the
book I am building a portfolio of AI-fluency artifacts in my own field.

You are my collaborator on this work. Your job, in every conversation
inside this Project:

1. Read the attached Role Dossier first. Adapt every response to my
   actual role, my actual tasks, my actual stakeholders. Do not give
   generic advice; give advice grounded in my context.

2. Read the attached CLAUDE.md before producing any output. Honor the
   rules in it. If I am asking for something the CLAUDE.md says I
   should not delegate, say so and explain why.

3. Read the attached DESIGN.md when the work involves a visible
   deliverable. Match the voice, register, and quality standards the
   DESIGN.md names for my domain.

4. Push back. If my framing of a task is sycophantic-drift-shaped, if
   my self-assessments are too generous, if I am asking you to handle
   something the book says belongs in the human layer, name it. The
   Ownership Test applies: I should be able to defend every paragraph
   of any output to a hostile reviewer. Help me get there, not past it.

5. When a chapter exercise produces an artifact, save it to my
   portfolio with the filename the exercise specifies. Use the exact
   structure the book lays out for that artifact.

OPERATING RULES across the book:

- I do not open the tool until I have written the five specification
  components down somewhere I can see them (Chapter 3 rule).
- Before any consequential delegation, I run the four delegation
  questions (Chapter 4 rule).
- I do not ship work I have been building in conversation for more
  than twenty minutes without running, at minimum, the steelman
  (Chapter 5 rule).
- On any external-tier output, I run all four verification layers
  before shipping. The omission layer is the one I most often skip
  and the one most expensive to miss (Chapter 6 rule).
- No recurring AI-assisted process I am part of runs without a
  documented spec, a scheduled drift check, an outcome audit, and a
  named accountable human (Chapter 7 rule).
- I do not own a running automation without sampling, adversarial
  test cases, and outcome auditing on my calendar (Chapter 9 rule).
- Any automation I am responsible for has a specification three
  times the length of the equivalent Augmentation spec, addresses
  all six ambiguity types, and has a diligence design on someone's
  calendar (Chapter 10 rule).
- Any Human Decision Node I am part of, or am designing, gets the
  four-condition test before any deployment and a recurring audit
  during (Chapter 12 rule).

These rules will be in the attached CLAUDE.md as I build it. They are
listed here so you carry them even before the file is complete.

When I do not yet have all of these in CLAUDE.md, work with what is
there. As I add rules across chapters, I will replace the attached
file. Read the most recent attached version.
```

**Step 3.** Attach the first reference file: your **Role Dossier**, drafted in the Chapter 0 LLM exercise. One paragraph: who you are professionally, what you do weekly, who you serve, where AI is in your workflow today, what kind of work the portfolio should ladder into.

**Step 4.** Start a new conversation inside the Project. Run the Chapter 0 LLM exercise prompt. The session produces your Baseline Audit. Save it to your `portfolio/` folder on disk.

That is everything for the Chapter 0 setup. You return to the Project at Chapter 1.

---

## What the Project looks like at each stage of the book

The Project evolves across the book. Here is what is attached and what is in the system prompt at each Part-boundary.

### After Chapter 0 — the setup

**Attached files:**
- `Role-Dossier.md`

**Portfolio on disk:**
- `portfolio/`
  - `00-baseline-audit.md`

**System prompt:** as pasted above.

You have a Project that knows who you are and one audit of your past work.

### After Chapter 8 — end of Part I, the keystone

**Attached files:**
- `Role-Dossier.md`
- `CLAUDE.md` (six rules accreted across Chs 1, 3, 4, 5, 6)
- `DESIGN.md` (three sections: verification standard, voice/register, audience criteria)
- `PROJECT-template.md`
- `02-practitioner-profile.md` (the consolidated Profile)
- `06-verification-protocol.md`
- `08-case-study-summary.md` (a one-page index pointing at the case-study folder)

**Portfolio on disk:**

```
portfolio/
├── CLAUDE.md
├── DESIGN.md
├── PROJECT-template.md
├── Role-Dossier.md
├── 00-baseline-audit.md
├── 01-worked-loop-log.md
├── 02-practitioner-profile.md
├── 02-nine-scenes-in-my-role.md          (supporting)
├── 03-specification-library/
│   ├── 00-the-trap.md
│   ├── 01-[task-type].md
│   ├── 02-[task-type].md
│   ├── 03-[task-type].md
│   ├── 04-[task-type].md
│   └── 05-[task-type].md
├── 05-adversarial-conversation-log.md
├── 06-verification-protocol.md
├── 07-diligence-framework.md
└── 08-case-study/
    ├── 00-narrative.md
    ├── 01-spec.md
    ├── 02-delegation-map.md
    ├── 03-conversation-log.md
    ├── 04-verification-notes.md
    ├── 05-final-deliverable.md
    ├── 06-ai-use-disclosure.md
    └── 07-part-1-gate.md
```

You have everything Part I produces: a method (governing files + customized frameworks), evidence the method survives contact with real work (the case study), and self-knowledge (the Profile, the Baseline Audit).

The Project has the load-bearing files attached. The portfolio folder on disk has the full set including the case-study sub-folder, which is too large for the Project's attachment limit; you reference it by path in conversation when needed.

### After Chapter 12 — end of Part III, before synthesis

**Attached files (updated versions):**
- `Role-Dossier.md`
- `CLAUDE.md` (now nine rules — Chs 1, 3, 4, 5, 6, 7, 9, 10, 12)
- `DESIGN.md` (now six sections — verification standard, voice/register, audience criteria, maintenance/ownership, agentic stakeholder-model criteria, HITL design standards)
- `PROJECT-template.md`
- `02-practitioner-profile.md`
- `06-verification-protocol.md`
- `09-automation-audit.md`
- `11-blast-radius-decision-aid.md`
- `12-hitl-protocol.md`

**Portfolio on disk:** everything above plus —

```
portfolio/
├── ...
├── 09-automation-audit.md
├── 10-automation-specification.md
├── 11-blast-radius-decision-aid.md
└── 12-hitl-protocol.md
```

You have the full method (15 governing-and-framework artifacts) and the keystone deliverable. You have not yet drafted the Final Audit, the 90-Day Plan, or the Cover Memo. That is Chapter 13's work.

### After Chapter 13 — the finished portfolio

**Attached files:** same as Chapter 12, plus —
- `13-final-audit.md`
- `13-90day-plan.md`
- `cover-memo.md` (at the top level — the first thing a future reader sees)

**Portfolio on disk:**

```
portfolio/
├── cover-memo.md                          ← the front door
├── CLAUDE.md                              ← my method, coding side
├── DESIGN.md                              ← my method, output side
├── PROJECT-template.md                    ← my method, project side
├── Role-Dossier.md                        ← who I am
│
├── 00-baseline-audit.md                   ← before
├── 13-final-audit.md                      ← after
├── 13-90day-plan.md                       ← what's next
│
├── 01-worked-loop-log.md                  ← I can run the Loop
├── 03-specification-library/              ← I can specify
├── 05-adversarial-conversation-log.md     ← I can converse adversarially
├── 06-verification-protocol.md            ← I can verify
├── 08-case-study/                         ← I have done all of it on real work
├── 10-automation-specification.md         ← I can spec an automation
│
├── 02-practitioner-profile.md             ← I know my strengths and gaps
├── 02-nine-scenes-in-my-role.md           ← (supporting)
├── 07-diligence-framework.md              ← I govern systems over time
├── 09-automation-audit.md                 ← I take responsibility for inherited systems
├── 11-blast-radius-decision-aid.md        ← I evaluate agentic deployments
└── 12-hitl-protocol.md                    ← I design human decision nodes
```

Seventeen artifacts, five sections, anchored by one case study. The Cover Memo is the front door. The before-and-after audit pair is the cleanest single piece of evidence the portfolio offers. Everything else supports.

---

## Why the Project survives the book

When the book ends, you do not retire the Project. You keep it as the working environment in which you keep the portfolio alive.

- When you take on a new agentic deployment to evaluate, you open the Project, attach the proposal, and Claude has your `DESIGN.md` criteria, your blast-radius decision aid, and your HITL protocol already in context. The evaluation takes thirty minutes, not three days.
- When you build a new automation, you open the Project, share the Augmentation version, and Claude helps you expand to the Automation spec against your existing six-ambiguity-types template.
- When you start a new role, you update the Role Dossier, run a new Baseline Audit against work from the new role, and the portfolio refreshes around the new context. The method travels. The artifacts get updated. The Cover Memo gets re-drafted.

The Project is the operating environment for the practice the book teaches. It is also, when you need to hand the portfolio to a future reader, the place you generate the package — pulling the latest artifacts, refreshing the Cover Memo, producing the share-ready zip or folder.

---

## Variants — ChatGPT, Gemini, Cowork

The same setup works in adjacent tools with minor adaptation.

- **ChatGPT.** Create a Custom GPT named "AI Fluency for [Your Role]." Paste the system prompt into the instructions field. Attach files via the GPT's knowledge files. The Custom GPT becomes structurally equivalent to the Claude Project.
- **Gemini.** Use a Gem with the same instructions; attach files via Drive integration. Gemini's Drive sync makes the portfolio folder updates flow automatically into the Gem's knowledge.
- **Cowork.** Set up a Cowork session pointed at the `portfolio/` folder. The system prompt above becomes the session's persistent context. Cowork can actually read and write the artifact files directly, which is operationally cleaner than attached-file management.

Pick the surface that fits how you work. The portfolio folder on disk is the source of truth in any case; the Project / Custom GPT / Gem / Cowork session is the working interface.

---

## The single most important practice

Update the Project's attached files when the disk files change. The Project's value collapses if `CLAUDE.md` in the Project lags four chapters behind the `CLAUDE.md` on disk. The portfolio is a living artifact. The Project is the live working surface on top of it. Both have to stay in sync.

A two-minute discipline at the end of each chapter's exercise: detach the old version of the file, attach the new version, confirm the system prompt still references the file by name. Most chapters update one file. The discipline takes longer to describe than to do.

If the practice slips, the symptom appears as Claude giving advice that contradicts a rule you have already written into `CLAUDE.md`. When you see that, do not argue with Claude. Update the attached file. The rule is in the wrong place, not wrong.

---

*Companion to the chapter LLM exercises. Read at Chapter 0 setup. Refer back when the chapter exercise references "the Project" and you want to know what is supposed to be in it.*
