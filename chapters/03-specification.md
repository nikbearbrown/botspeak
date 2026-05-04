# Chapter 3 — Specification
*Doing the Thinking the Model Cannot Do for You.*

It is 4:11 PM on a Wednesday and Aisha Okonkwo is having her third bad day in a row with Claude.

Her manager has asked her to summarize a 47-page government report on rural broadband subsidies for a stakeholder meeting tomorrow. Aisha is two months into her first job at a policy nonprofit. She uploads the PDF, types *summarize this report for my manager*, and gets back a clean 600-word summary. It is fine. It is not what her manager wants. Her manager wants the parts most relevant to their coalition's specific position, not a neutral summary. Aisha types: *summarize this report for my manager focusing on the parts most relevant to our coalition.* She gets another 600-word summary, slightly differently weighted, still not it. Her manager wants something that fits in five bullet points on a slide. Aisha types: *summarize this report in five bullet points.* She gets five bullets, each three sentences long, and her manager wants each bullet to be one short clause readable from twenty feet away.

By the third iteration Aisha has spent forty minutes and produced something her manager will rewrite anyway. She closes the laptop. She concludes that Claude is not very good at this.

Claude is not good at this because Aisha has not told Claude what *this* is.

This is the thing I want to understand with you, because it is not a prompting failure in any deep sense. It is a failure of *specification*, which is different from prompting, and which most people who pick up an AI tool never learn to do because nobody has named it separately.

The difference is this: a prompt is what you type. A specification is what you know before you type it.

Language models are, among other things, fluency machines. They are extraordinarily good at producing coherent, plausible-sounding output in whatever direction you point them. The catch is that if the direction is unclear, the fluency just makes the wrong output look convincing. You get something that reads well and misses the point, which is in some ways worse than something that obviously fails — at least the obvious failure tells you immediately to try again. When Aisha got three different polished summaries that were each not quite right, the polish was making it harder to see the problem, not easier.

When people say "the AI didn't give me what I wanted," they usually mean one of two things. Either the model genuinely misunderstood a clear request — this happens, but less often than people think. Or they didn't yet know what they wanted with enough precision for anyone — model or human — to give it to them. The second failure is much more common, and much less visible, because the model's fluency produces output that looks like the problem was almost solved, which creates the impression of a near-miss rather than a specification failure.

The specification move is, in part, a diagnostic on yourself. That is exactly why it is hard.

---

Here is what a working specification contains. I am going to name five components, and the list is not glamorous. It is infrastructure — the kind of thing that sounds boring because it holds something up rather than being the thing held.

<!-- → [INFOGRAPHIC: A five-part diagram — radial or stacked vertical — showing the five specification components (Intent, Constraints, Success Criteria, Exclusions, Output Format) with a one-line definition for each. Each component visually suggests that removing it leaves the specification incomplete. Placed here to anchor the five-component framework before the prose walks through each one.] -->

![Figure 3.1 — A five-part diagram](images/03-specification-fig-01.jpg)

The first is **intent**: not the immediate task, but the goal the task serves. Aisha's intent was not *produce a summary*. Her intent was *give my manager a five-bullet artifact she can paste onto a slide and use to argue our coalition's position in tomorrow's stakeholder meeting.* Those are not the same thing, and the model had no way to know which one she meant. The intent statement is what tells the model — and you — what counts as success.

The second is **constraints**: what the output has to fit inside. Format constraints: five bullets, one clause each, no sub-bullets. Length constraints: under a hundred words total. Source constraints: only claims that appear in the report, not the model's outside knowledge. Audience constraints: people who have not read the document. Constraints are the parts of the specification the model would otherwise guess at — and guess wrong — while producing output that looks like it could be right.

The third is **success criteria**: how you will know, after the fact, that the output is good. *My manager uses it without rewriting* is a real success criterion. *Each bullet would survive a hostile reviewer asking "show me where in the report this comes from"* is a real success criterion. Without success criteria, every output looks plausibly fine, and you are left with a vague dissatisfaction you cannot diagnose.

The fourth is **exclusions**: what the model is not supposed to do. Do not invent sources. Do not pad bullets to make them feel substantive. Do not include the executive summary verbatim. This sounds like a strange thing to have to specify. But language models fill in blanks. If you leave a blank, they will fill it with their best guess at what looks complete. Exclusions are the specification saying: *please leave that blank blank.*

The fifth is **output format**: what the deliverable looks like structurally. Markdown or plain text. Bullet list or prose. Five items on their own lines or a flowing paragraph. This feels like a detail. It is not a detail. The format constrains the kind of thinking the model has to do, and a bullet list and a paragraph on the same intent will produce different content, not just different presentation.

Now watch what Aisha would have sent if she had specified before prompting:

> **Intent:** Give my manager a five-bullet artifact she can paste onto a slide for tomorrow's stakeholder meeting on rural broadband subsidies.
>
> **Constraints:** Five bullets total, one clause each, ≤15 words per bullet, source only the attached report, audience has not read the report.
>
> **Success criteria:** Manager uses it without rewriting; each bullet survives a reviewer asking "show me where in the report."
>
> **Exclusions:** Do not editorialize beyond what the report supports. Do not pad. Do not include the executive summary verbatim.
>
> **Output format:** Five bullets, each on its own line, no sub-bullets, no preamble, no closing sentence.

| Prompt as sent | Component groping toward — but never stated | What the omission cost |
|---|---|---|
| *"Summarize this report for my manager."* | Nothing. No component is present. | Model guessed the task. Produced a neutral 600-word summary — polished, directionless, unusable. |
| *"Summarize this report for my manager, focusing on the parts most relevant to our coalition."* | **Intent** — partially. Adds audience and a hint of purpose, but the actual goal (slide artifact, stakeholder meeting, coalition position) remains unstated. | Model reweighted the summary slightly. Still 600 words, still not slide-ready. The polish made the near-miss hard to name. |
| *"Summarize this report in five bullet points."* | **Output Format** — partially. Adds bullet structure but omits length per bullet, preamble rules, and hierarchy constraints. | Model produced five bullets, each three sentences long. Format was closer; content was still unfit for a slide readable from twenty feet. |
| **Complete specification:** Intent (coalition slide for tomorrow's meeting) + Constraints (≤15 words per bullet, report only, unread audience) + Success Criteria (manager uses without rewriting; each bullet survives hostile review) + Exclusions (no editorializing, no padding, no verbatim executive summary) + Output Format (five bullets, own lines, no sub-bullets, no preamble) | **All five components present.** | Manager uses it without rewriting. |

That is not a prompt. It is the thinking a prompt needs to encode. The actual prompt Aisha types may be two or three sentences long — but those sentences will carry all five components because she now knows what they are.

---

I want to admit something about why this is hard, because the difficulty is not what most people expect.

Most people, when they first try to specify before prompting, discover that they do not fully know what they want. They thought they did. They sit down to write the intent statement and find they have not yet decided what the goal is. They sit down to write the success criteria and find they have none. They sit down to write the exclusions and realize they had been counting on the model to make those decisions for them — even though they would never have described it that way.

This is uncomfortable. It is also the specification doing its job.

Think about what happens in a well-run organization when someone delegates a task. The good manager does not walk up to a colleague and say *can you write something about the broadband report?* and walk away. She says: *I need five slide-ready bullets from the rural broadband report — one clause each, no longer than fifteen words, only claims that are in the document, by tomorrow at noon, because we are using them to argue for the coalition's position at the Thursday meeting.* The colleague now has enough to do the work. The manager had to do that thinking before she opened her mouth.

Language models are not different. They are, in a certain mechanical sense, colleagues who have read a great deal and who will attempt in good faith to do what you ask. What they cannot do is want things on your behalf. They cannot supply the goal you forgot to specify. And because they are fluency machines, when the goal is missing, they will produce something that sounds like a goal was present — something plausible, coherent, and wrong in a way that is difficult to name.

The specification move forces you to do the thinking the delegation requires. This is why experienced practitioners produce better output not primarily because they know better phrases, but because they have learned to specify before they prompt. The specification is the work. The prompt is the document recording it.

---

Let me say something about templates, because this is where the specification stops being slow.

The five components feel like overhead the first time. They feel like overhead the fifth time. By the twentieth time you do the same kind of task, the overhead is gone — because you have a template.

A template is a specification you wrote once for a category of recurring work, with the variable parts marked, that you fill in rather than invent from scratch. Aisha's broadband-summary specification, captured as a template, becomes:

> **Intent:** Give [recipient] a [length] artifact for [specific purpose].
>
> **Constraints:** [format details], source: only [permitted sources], audience: [who reads it].
>
> **Success criteria:** [recipient] uses it without rewriting; each [unit] survives reviewer asking "show me where."
>
> **Exclusions:** Do not editorialize. Do not pad. Do not include [common over-include item].
>
> **Output format:** [structural details].

<!-- → [IMAGE: A visual of a filled-in template card — a physical notecard or document with the five fields completed for a real task instance. Should feel like a working artifact, not a polished infographic. The design should convey "this is a tool you actually use at your desk," not "this is a diagram from a textbook."] -->

![Figure 3.3 — A visual of a filled-in template card](images/03-specification-fig-03.jpg)

The next time she summarizes a long document for a high-stakes deliverable, she fills in the brackets. The thinking she did the first time is now infrastructure. The template does not do the thinking for her — she still has to know her intent, her constraints, her success criteria. But it reminds her to have them, and it gives her a form to put them in.

Build templates for the five tasks you do most often this quarter. Refine them as you discover what was missing. The fluent practitioner has a small library of templates and rarely starts a specification from scratch. The literate user invents the wheel every time, and every time runs into the same missing components she forgot last time.

---

There is a level of practice above templates, which is the use of *patterns*. A pattern is a compressed structure for part of the specification — a shorthand that the model handles especially well. I want to introduce one pattern here, not because it is magic, but because seeing one will help you understand what all patterns are.

The pattern is called **role-and-rubric**, and it has two pieces.

The role piece assigns the model a specific professional persona: not *act like a friendly assistant* but *act as a senior policy researcher with a decade of rural infrastructure experience preparing a one-page brief for a coalition.* The role compresses a great deal of constraint and tone into a single phrase the model can hold in mind while generating. The model does not have that experience in any meaningful sense. But it has read enough text produced by people in that role that the assignment shifts the statistical weight of its output toward what such a person would actually write.

The rubric piece supplies explicit criteria the output will be judged against: *each bullet must be defensible against a hostile reviewer asking "where in the report is this"; no claim that goes beyond what the report supports; tone declarative, not hedged; total under a hundred words.* The rubric is the success criteria and exclusions components, made explicit in a form the model can self-check against.

| Specification component | How role-and-rubric handles it |
|---|---|
| **Intent** | Partially. The role assignment implies a purpose ("senior policy researcher preparing a one-page brief") but does not state the goal the task serves. Still needs an explicit statement of what success looks like for this specific output. |
| **Constraints** | Poorly. Role implies tone and register but says nothing about length, permitted sources, or audience. These must still be stated explicitly. |
| **Success Criteria** | Well — this is what the rubric does. Explicit, testable criteria ("each bullet must be defensible against a hostile reviewer") are the rubric's native function. |
| **Exclusions** | Well — also rubric territory. "No claim that goes beyond what the report supports" is a clean exclusion the rubric encodes directly. |
| **Output Format** | Not addressed. Neither the role nor the rubric specifies markdown vs. plain text, bullet vs. prose, or structural details. Must still be stated separately. |

Role-and-rubric is one pattern. There are others — chain-of-thought, few-shot examples, constraint stacking. Each compresses different parts of the five components into a structure the model handles well. They are scaffolds for the same five components, not alternatives to them. The mistake I see most often is reaching for a pattern before specifying. Someone reads about chain-of-thought and starts adding *think step by step* to every prompt, regardless of whether step-by-step reasoning is what the task requires. Patterns serve the specification. The specification does not serve the pattern. If you do not yet know your intent, adding *think step by step* will give you a fluent, step-by-step, wrong answer.

---

I want to address something the chapter so far has left implicit.

When you force yourself to write down the intent, you will sometimes discover that you have not decided what success looks like. When you write down the constraints, you will sometimes discover that two of them are in tension — you want it short and you want it comprehensive, and you have not yet decided which one wins. When you write down the exclusions, you will sometimes discover that what you were actually planning to ask the model to do is make a judgment call you should be making yourself.

These discoveries are not a sign that specification is too much work. They are the specification doing its job, which is to surface the parts of the task you had not yet thought through. A language model is a fluency amplifier. Give it half-formed intent, and it produces fluent half-formed output. Give it well-formed intent, and it produces fluent well-formed output. The fluency amplifies whatever you brought. This is not a flaw in the technology. It is a property of all powerful delegation: the quality of the output is bounded by the quality of the brief.

Sometimes, even with discipline, you do not yet know what you want. You are at the beginning of a problem, feeling around its edges. This is fine. *Exploratory* is itself a specifiable intent: *surface three to five distinct framings of this question without committing to one; optimize for variety over polish; do not produce a finished artifact.* That is a specification for uncertainty. It tells the model you are not looking for a polished output you will feel committed to — you are looking for raw material you can think with. Specification under uncertainty is not a contradiction. It is honesty about what stage of work you are in. The mistake is skipping the specification because the task feels unclear, which usually produces polished output that answers a question you were not actually asking, which you then feel oddly obligated to accept.

---

There is a prior question this chapter has been deliberately avoiding: whether to pass the task to the model at all.

Some tasks should not be delegated. Some should be delegated in pieces, with strong human judgment at the joins. Some should never leave your hands entirely. The specification move is how you get good output when you have decided to delegate. The question of *whether* to delegate — and what it costs when you do — is what the next chapter takes up.

Specification gets you a well-formed task to hand off. Delegation asks whether you should hand it off in the first place, and if so, how much of it. Those are different questions, and the order matters. You cannot ask the delegation question well until you have specified the task clearly enough to see what the task actually is. Which is one more reason the specification move comes first.

---

*What would change my mind on this chapter.* If careful empirical work showed that experienced practitioners produce equivalent-quality output from one-sentence prompts and from full five-component specifications — that the specification is decorative for people who have done it enough times that it lives in muscle memory — I would have to revise the claim that specification is the load-bearing skill. What I observe is the opposite: experienced practitioners specify more, not less, and the specification gets tighter, not looser, as the task gets harder. But the observation is informal, and I hold it accordingly.

*Still puzzling.* I do not yet have a clean answer to when the cost of full specification exceeds the cost of iteration. For very small tasks — reword this sentence, fix this heading — it almost certainly does. The break-even point is task-dependent, and I have not found a rule that generalizes cleanly.

---

> **Going deeper — *Computational Skepticism for AI***
>
> Specification, formalized at the level engineers use when they validate datasets and deployments, is called **reconstructing the epistemic frame**. The advanced book makes the point that every dataset and every prompt embeds a frame — what it claims to represent, what it actually represents, what it excludes — and that the most consequential failures live in assumptions the practitioner never wrote down: scope, sampling, definition, time, access. The five components in this chapter are the practitioner-grade version. The six-step epistemic-frame reconstruction in the advanced book is the engineering-grade version, with an explicit prediction-lock you do before you see any output, so the gap between expectation and observation can teach you.
>
> Reaching for the deeper version pays off when you specify automations (Chapter 10 of this book) or design AI deployments other people will rely on.
>
> See *Computational Skepticism for AI*, **Chapter 5 — Data Validation: Reconstructing the Epistemic Frame Behind a Dataset**.

---

### LLM Exercise — Chapter 3: Specification

**Project:** AI Fluency for [Your Role] — The Domain Field Manual

**What you're building this chapter:** Section 4 of the playbook — five specification templates for the five most common task types in your role. Each template is a fillable scaffold that captures the five components (intent, constraints, success criteria, exclusions, output format) and is ready for the reader to drop their own brackets into and use immediately.

**Tool:** Claude Project (continue) + Cowork (write Section 4).

---

**The Prompt:**

```
Continuing my Domain Field Manual playbook. My Role Dossier and Sections 1–3 are in the Project context.

Botspeak Chapter 3 teaches that specification is the work the prompt documents. Five components: INTENT (the goal the task serves), CONSTRAINTS (what the output must fit inside), SUCCESS CRITERIA (how I'll know it's good), EXCLUSIONS (what the model is NOT supposed to do), OUTPUT FORMAT (structural details). Aisha's "summarize this report for my manager" failed because four of the five components were never specified.

For my playbook's Section 4, do three things:

TASK 1 — IDENTIFY THE FIVE MOST COMMON TASK TYPES IN MY ROLE.
Not nine, not three. Five. The task types should be:
- High-frequency (each appears multiple times per month for someone in my role)
- Distinct enough that they require different specifications
- AI-amenable (it's plausible to do them with AI assist)
- Spanning the role — not all the same kind of work

For each task type, name it precisely and give 2–3 examples of when it occurs.

TASK 2 — A SPECIFICATION TEMPLATE PER TASK TYPE.
For each of the five task types, produce a fillable specification template. The template should:
- Cover all five components in the chapter (intent, constraints, success criteria, exclusions, output format)
- Have BRACKETED VARIABLES the reader fills in for their specific instance
- Pre-populate the constants — the things every instance of this task type shares (audience, format, tone, source rules common to the type)
- Include 1–2 EXCLUSIONS specific to my role's typical failure modes for this task type (the "do not invent industry comparables" / "do not hedge in both directions" kind)
- Specify the output format with the precision Aisha's third iteration finally reached

The template format I want:

TEMPLATE — [task type name]

Intent: Give [recipient] a [length/format] artifact for [specific purpose]
Constraints: [bracketed format details], source: [permitted sources], audience: [who reads it]
Success criteria: [recipient action/test 1]; [recipient action/test 2]
Exclusions: Do not [role-specific failure mode 1]. Do not [role-specific failure mode 2]. Do not [generic failure mode].
Output format: [structural details, length, sections]

TASK 3 — ONE WORKED EXAMPLE PER TEMPLATE.
For each template, write one fully-filled-in example showing what the template looks like populated for a specific instance the reader could imagine on their own desk this week. The worked example is half the value — the template alone leaves the reader staring at brackets.

End with one paragraph on the role-specific specification trap: what is the failure mode that recent practitioners in my role most often produce when they specify badly? What in my role tends to be most often left unsaid?

Save as `04-specification-templates.md` in my playbook folder.
```

---

**What this produces:** Section 4 of the playbook — five fillable specification templates plus five worked examples plus one role-specific specification trap, ~2,500–4,000 words. The first directly-usable artifacts in the playbook.

**How to adapt this prompt:**
- *For your own project:* The templates' value depends on the EXCLUSIONS section being honest about your role's typical failure modes. Be specific about what gets botched.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right fit unless your role's tasks are code-heavy and you want the templates as structured prompt files in a repo.
- *For Cowork:* Recommended.

**Connection to previous chapters:** Section 3's nine failure scenes told you which capacities most fail in your role. The templates here are the operational antidote at the Specification step.

**Preview of next chapter:** Chapter 4 produces Section 5 — the Seven Tiers of delegation calibrated to your work. Each Tier gets domain-specific examples; the chapter ends with a Tier-classification worksheet the reader can apply to any task they're considering.

---

## Exercises

### Warm-Up

**1. Name and test the five components.** *(Component recall | Difficulty: low)*
Without looking back, name the five specification components. For each one, write a single sentence describing what goes wrong when that component is missing — not in theory, but in practice. What does the output look like? What does the failure feel like from the user's side?

**2. Diagnose a weak prompt.** *(Component identification | Difficulty: low)*
Take this prompt: *"Write an email to my team about the new meeting policy."* Identify which of the five components are present and which are absent. Then rewrite it as a full specification. Your specification should be specific enough that a model — or a competent human colleague — could produce the deliverable without asking a single clarifying question.

**3. Trace Aisha's iterations.** *(Component sequencing | Difficulty: low)*
Return to Aisha's three prompts. For each iteration — *summarize this report for my manager*, then *focusing on parts most relevant to our coalition*, then *in five bullet points* — name the single specification component she added (or groped toward) with that iteration, and the components still missing at that point. Then name the one component whose absence caused the most damage across all three attempts.

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

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Nancy Leveson** was arguing that most failures come from incomplete specifications rather than component breakdown decades before anyone said "prompt engineering." Here's a prompt to find out more — and then make it better.

![Nancy Leveson, c. 2000s. AI-generated portrait based on a public domain photograph.](../images/nancy-leveson.jpg)
*Nancy Leveson, c. 2000s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who is Nancy Leveson, and how does her work on STAMP and System-Theoretic Process Analysis connect to the idea that careful specification is the main defense against AI failure? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Nancy Leveson"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain STAMP in plain language, as if you've never heard the words "control structure"
- Ask it to compare Leveson's safety-spec components to the five-component prompt template in this chapter
- Add a constraint: "Answer as if you're writing a memo to a manager who calls specification 'bloat'"

What changes? What gets better? What gets worse?
