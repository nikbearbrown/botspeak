# Chapter 3 — Specification
*Doing the Thinking the Model Cannot Do for You.*

Here is a thing that keeps happening.

Someone sits down with a language model, types a sentence, reads the output, types a slightly different sentence, reads another output, and after three or four rounds closes the laptop and concludes that AI is not very good at this. What they rarely suspect is that the problem was not in the AI and not in the sentences. The problem was upstream of both — it was in the thinking that the sentences were supposed to be expressing.

I want to talk about that upstream problem, because it is the one that actually matters, and because most writing about AI tools skips straight to the sentences.

---

## The thing the sentence is not

There is a distinction between a *specification* and a *prompt* that almost nobody makes explicitly, and that I think is load-bearing for everything that follows in this book.

A prompt is what you type. A specification is what you know before you type it.

The difference matters because language models are, among other things, fluency machines. They are extraordinarily good at producing coherent, plausible-sounding output in whatever direction you give them. The catch is that if the direction is unclear, the fluency just makes the wrong output look convincing. You get something that reads well and misses the point, which is in some ways worse than something that reads badly and obviously fails — at least the obvious failure tells you immediately that you need to try again.

When people say "the AI didn't give me what I wanted," they usually mean one of two things. Either the model genuinely misunderstood a clear request, which happens but is less common than people think. Or they didn't yet know what they wanted with enough precision for anyone — model or human — to give it to them.

The specification move is, in part, a diagnostic on yourself. And that is exactly why it is hard.

---

## Five components

Let me get concrete. Every working specification has five things in it, and most failing specifications are missing at least two.

<!-- → [INFOGRAPHIC: A five-part radial or vertical diagram showing the five components — Intent, Constraints, Success Criteria, Exclusions, Output Format — with a one-line definition for each. Each node should visually suggest that removing any one of them leaves the specification incomplete. Place here to anchor the section before the prose walks through each one.] -->

The first is **intent** — not the immediate task, but the goal the task serves. Suppose you are a junior researcher and your director has asked you to summarize a government report for a stakeholder presentation tomorrow. You upload the report and type: *summarize this report.* You get a summary. It is fine. It is not what your director wanted, because what your director wanted was not a neutral summary — she wanted the five points most relevant to your organization's policy position, formatted so they fit on a single slide, readable from twenty feet away. The immediate task was *summarize.* The intent was *give my director something she can paste onto a slide and use to make an argument tomorrow morning.*

Those are not the same thing, and the model had no way to know which one you meant.

The second component is **constraints** — what the output has to fit inside. Format constraints: five bullets, each one clause, no sub-bullets. Length constraints: under a hundred words total. Source constraints: only claims that appear in the report, not the model's outside knowledge. Audience constraints: read by people who have not seen the document. Constraints are the parts of the specification that the model would otherwise guess at — and would guess wrong — while producing output that looks like it could be right.

The third component is **success criteria** — how you will know, after the fact, that the output is good. *My director would use it without rewriting* is a real success criterion. *Each bullet would survive a hostile reviewer asking "show me where in the report this comes from"* is a real success criterion. Without success criteria, every output looks plausibly fine, and you are left with a vague feeling of dissatisfaction that you cannot diagnose.

The fourth component is **exclusions** — what the model is not supposed to do. Do not invent sources. Do not pad bullets to make them feel substantive. Do not include the executive summary verbatim. This sounds like a strange thing to have to specify. But language models fill in blanks. If you leave them a blank, they will fill it with their best guess at what looks complete. Exclusions are the specification saying: *please leave that blank blank.*

The fifth component is **output format** — what the deliverable looks like structurally. Markdown headings or plain text? Bullet list or prose? JSON or narrative? This feels like a detail. It is not a detail. The format constrains the kind of thinking the model has to do. A bullet list and a paragraph on the same intent will produce different content, not just different presentation.

---

## Why this is hard

I want to be honest about something.

Most people, when they first try to specify before prompting, discover that they do not fully know what they want. They thought they did. They sit down to write the intent statement and find they have not yet decided what the goal is. They sit down to write the success criteria and find they have none. They sit down to write the exclusions and realize they had been counting on the model to make those decisions for them — even though they would never have described it that way.

This is uncomfortable. It is also exactly why specification is the skill it is.

Think about what happens in a well-run organization when someone delegates a task to another person. The good manager does not walk up to a colleague and say *"can you write something about the broadband report?"* and walk away. She says: *I need five slide-ready bullets from the rural broadband report — one clause each, no longer than fifteen words, only claims that are in the document, by tomorrow at noon, because we are using them to argue for the coalition's position at the Thursday meeting.* The colleague now has enough to do the work. The manager had to do that thinking before she opened her mouth, and the doing of that thinking is most of the work of delegation.

Language models are not different. They are, in a certain mechanical sense, colleagues who have read a great deal and who will attempt, in good faith, to do what you ask. What they cannot do is want things on your behalf. They cannot supply the goal you forgot to specify. And because they are fluency machines, when the goal is missing, they will produce something that sounds like a goal was present — something plausible, coherent, and wrong.

The specification move forces you to do the thinking the delegation requires. This is why experienced practitioners, when they work well with these tools, produce better output not primarily because they know magic phrases, but because they have learned to specify before they prompt. The specification is the work. The prompt is the document recording it.

---

## A worked example

Watch what the specification looks like when written out:

> **Intent:** Give my director five slide-ready bullets she can paste into tomorrow's stakeholder presentation to argue for the coalition's position on rural broadband subsidies.
>
> **Constraints:** Five bullets, one clause each, ≤15 words per bullet, source only the attached report, audience has not read the report.
>
> **Success criteria:** Director uses it without rewriting. Each bullet survives a reviewer asking "show me where in the report this is."
>
> **Exclusions:** Do not editorialize beyond what the report supports. Do not pad. Do not include the executive summary verbatim.
>
> **Output format:** Five bullets, each on its own line, no sub-bullets, no preamble, no closing sentence.

<!-- → [TABLE: Side-by-side comparison of the original prompt ("summarize this report") vs. this specification — columns: Component, Original Prompt, Full Specification. Rows for each of the five components plus a final row showing the output difference. Student should see exactly which components were missing in the original and what that omission cost.] -->

That is not a prompt. It is the thinking a prompt needs to encode. The actual prompt may be two or three sentences — but those sentences will carry all five components because the writer now knows what they are.

Notice what this specification does that the original *summarize this report* did not: it gives the model a person to write for, a purpose that person has, a deadline that purpose is tied to, a format that purpose requires, and criteria the output has to survive. The model is not being asked to produce a good generic summary. It is being asked to solve a specific problem.

---

## Templates

The five components feel like overhead the first time. They feel like overhead the fifth time. By the twentieth time you do the same kind of task, the overhead is gone — because you have a template.

A template is a specification you wrote once for a category of recurring work, with the variable parts marked, that you fill in rather than invent from scratch. The broadband-summary specification, captured as a template, becomes:

> **Intent:** Give [recipient] a [length] artifact for [specific purpose].
>
> **Constraints:** [format details], source: only [permitted sources], audience: [who reads it].
>
> **Success criteria:** [recipient] uses it without rewriting; each [unit] survives reviewer asking "show me where."
>
> **Exclusions:** Do not editorialize. Do not pad. Do not include [common over-include item].
>
> **Output format:** [structural details].

The next time you summarize a long document for a high-stakes deliverable, you fill in the brackets. The thinking you did the first time is now infrastructure. The template does not do the thinking for you — you still have to know your intent, your constraints, your success criteria. But it reminds you to have them, and it gives you a form to put them in.

Build templates for the five tasks you do most often this quarter. Refine them as you discover what was missing. The fluent practitioner has a small library of templates and rarely starts a specification from scratch. The literate user invents the wheel every time, and every time runs into the same missing components they forgot last time.

<!-- → [IMAGE: A visual of a template card — a physical notecard or document with the five component fields and bracket placeholders visible. Should feel like a working artifact, not a polished infographic. The design should suggest "this is a tool you actually use," not "this is a diagram from a textbook."] -->

---

## Patterns

There is a level of practice above templates, which is the use of *patterns*. A pattern is a compressed structure for part of the specification — a shorthand that the model handles especially well.

One pattern worth knowing is called **role-and-rubric**. It has two pieces.

The role piece assigns the model a specific professional persona: not *act like a friendly assistant* but *act as a senior policy researcher with a decade of rural infrastructure experience preparing a one-page brief for a coalition.* The role compresses a great deal of constraint and tone into a single phrase the model can hold in mind while generating. The model does not, of course, have that experience in any meaningful sense. But it has read enough text produced by people in that role that the role assignment shifts the statistical weight of its output toward what such a person would actually write.

The rubric piece supplies explicit criteria the output will be judged against: *each bullet must be defensible against a hostile reviewer asking "where in the report is this"; no claim that goes beyond what the report supports; tone declarative, not hedged; total under a hundred words.* The rubric is the success criteria and exclusions components, made explicit in a form the model can self-check against during generation.

<!-- → [TABLE: A two-column breakdown of the role-and-rubric pattern — left column: specification component (Intent, Constraints, Success Criteria, Exclusions, Output Format), right column: how role-and-rubric encodes or leaves unaddressed each component. Student should see which components the pattern compresses well and which ones still need explicit treatment.] -->

Role-and-rubric is a pattern that compresses two of the five specification components into a structure the model handles well. The other patterns — chain-of-thought, few-shot examples, constraint stacking — each compress different parts. They are scaffolds for the same five components, not alternatives to them.

The mistake I see most often with patterns is reaching for one before specifying. Someone reads about chain-of-thought prompting — *think step by step before answering* — and starts adding it to every prompt, regardless of whether step-by-step reasoning is what the task requires. Patterns serve the specification. The specification does not serve the pattern. If you do not yet know your intent, adding *think step by step* to the prompt will give you a fluent, step-by-step wrong answer.

---

## What specification reveals

I said earlier that the specification move is a diagnostic on yourself, and I want to come back to that because I think it is the thing most worth understanding.

When you force yourself to write down the intent, you will sometimes discover that you have not decided what success looks like. When you write down the constraints, you will sometimes discover that two of them are in tension — you want it short and you want it comprehensive, and you have not yet decided which one wins. When you write down the exclusions, you will sometimes discover that what you were actually planning to ask the model to do is make a judgment call you should be making yourself.

These discoveries are valuable. They are not a sign that specification is too much work. They are the specification doing its job, which is to surface the parts of the task you had not yet thought through.

A language model is a fluency amplifier. Give it half-formed intent, and it produces fluent half-formed output. Give it well-formed intent, and it produces fluent well-formed output. The fluency amplifies whatever you brought. This is not a flaw in the technology. It is a property of all powerful delegation: the quality of the output is bounded by the quality of the brief.

The specification move is how you write a brief worth giving.

---

## A note on exploratory work

Sometimes, even with discipline, you do not yet know what you want. You are at the beginning of a problem, feeling around its edges, not yet ready to specify a goal because you do not know what the goal should be.

This is fine. *Exploratory* is itself a specifiable intent.

*Intent: surface three to five distinct framings of this question without committing to one; optimize for variety over polish; do not produce a finished artifact.* That is a specification for uncertainty. It tells the model you are not looking for a polished output you will feel committed to — you are looking for raw material you can think with.

Specification under uncertainty is not a contradiction. It is honesty about what stage of work you are in. The mistake is skipping the specification because the task feels unclear, which usually produces polished output that answers a question you were not actually asking, which you then feel oddly obligated to accept.

---

## What this chapter does not cover

I have described the specification move as though the only question is how to pass a task to a model. But there is a prior question I have been avoiding: whether to pass it at all.

Some tasks should not be delegated. Some should be delegated in pieces, with strong human judgment at the joins. Some should never leave your hands entirely. The specification move is how you get good output when you have decided to delegate. The question of *whether* to delegate — and what it costs when you do — is what the next chapter takes up.

---

*What would change my mind on this chapter:* If careful empirical work showed that experienced practitioners produce equivalent-quality output from one-sentence prompts and from full five-component specifications — that the specification is decorative for people who have done it enough times that it lives in muscle memory — I would have to revise the claim that specification is the load-bearing skill. What I observe is the opposite: experienced practitioners specify more, not less, and the specification gets tighter, not looser, as the task gets harder. But the observation is informal, and I hold it accordingly.

*Still puzzling:* I do not yet have a clean answer to when the cost of full specification exceeds the cost of iteration. For very small tasks — reword this sentence, fix this heading — it almost certainly does. The break-even point is task-dependent, and I have not found a rule that generalizes cleanly.

---

## Exercises

### Warm-up

**1.** Name the five components of a working specification. For each one, write a single sentence explaining what goes wrong when that component is missing. *(Tests: recall and functional understanding of all five components.)*

**2.** Take this prompt: *"Write an email to my team about the new meeting policy."* Identify which of the five specification components are present and which are missing. Then rewrite it as a full specification. *(Tests: ability to diagnose a weak prompt and translate it into specification form.)*

**3.** A colleague says, "I tried the five-component thing but it still didn't work — the output missed the point." Name two failure modes that could produce this result even with a complete-looking specification. *(Tests: understanding of intent precision and success criteria specificity.)* — *Warm-up / Medium*

---

### Application

**4.** You are a marketing analyst asked to prepare a competitive summary for a product launch. Write a full five-component specification for this task. Your specification should be specific enough that a model — or a competent human colleague — could produce the deliverable without asking a single clarifying question. *(Tests: ability to apply all five components to a novel professional context.)* — *Application / Medium*

**5.** Below is a specification with a hidden internal conflict:

> **Intent:** Produce a thorough analysis of all relevant risks.
> **Constraints:** Two pages maximum.
> **Success criteria:** A senior executive can read it in under three minutes and feel fully informed.
> **Exclusions:** Do not omit anything material.
> **Output format:** Prose paragraphs, no headers.

Identify the conflict. Explain what will happen if you send this specification to a model without resolving it first. Then rewrite it to resolve the tension. *(Tests: ability to spot constraint conflicts and apply the principle that specifications surface unresolved thinking.)* — *Application / Medium-Hard*

**6.** Explain why the *role-and-rubric* pattern is not a substitute for the five-component specification. Which components does it compress well? Which does it leave unaddressed? Give a concrete example where using role-and-rubric without a full specification would produce a plausible but wrong output. *(Tests: understanding of patterns as scaffolds for components, not replacements for them.)* — *Application / Medium*

**7.** A friend argues: "Templates are just bureaucracy. Good practitioners know what they want intuitively and don't need to fill out a form." Construct the strongest version of this argument, then explain why you agree or disagree based on the chapter's claims about where specification overhead actually goes. *(Tests: ability to engage with the chapter's core argument critically.)* — *Application / Hard*

---

### Synthesis

**8.** You are building a template library for a legal research team. Their three most common tasks are: (a) summarizing case law for a partner review memo, (b) drafting initial client intake questions, and (c) checking a contract clause against a regulatory standard. Write a template for each task. For each template, note which component was hardest to generalize and why. *(Tests: ability to apply specification across domains and identify where specification effort concentrates.)* — *Synthesis / Hard*

**9.** The chapter claims: "The specification move is, in part, a diagnostic on yourself." Connect this claim to the chapter's discussion of exploratory work. Under what conditions is the diagnostic *uncomfortable in a productive way* versus *a signal that you should not be delegating this task at all*? Where does the chapter leave this question open, and what would you need to know to answer it? *(Tests: ability to synthesize across multiple sections of the chapter and connect to the question the chapter explicitly defers to the next chapter.)* — *Synthesis / Hard*

---

### Challenge

**10.** The chapter ends with a stated puzzle: "I do not yet have a clean answer to when the cost of full specification exceeds the cost of iteration." Propose a framework for answering this question. Your framework should account for task type, stakes, novelty, and the practitioner's experience level. It should make a falsifiable prediction. Then identify the weakest assumption in your framework. *(Tests: ability to extend chapter reasoning into territory it explicitly leaves open, and to evaluate one's own reasoning honestly.)* — *Challenge / Open-ended*

**11.** Design a one-hour workshop for a team of twelve that teaches the five-component specification to people who have never heard of it. Specify: the opening problem you would pose, the order you would introduce the components, the exercise you would use after the third component, and how you would close. Justify each design decision using the chapter's reasoning about why specification is hard to learn. *(Tests: Feynman test — can the student teach it? Also tests whether the student understands *why* the components are ordered as they are and where the difficulty actually lives.)* — *Challenge / Open-ended*
