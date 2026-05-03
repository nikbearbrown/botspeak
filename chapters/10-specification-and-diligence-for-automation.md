# Chapter 10 — Specification and Diligence for Automation
*Doing the Work the Live Human Won't Be There to Do*

*The implicit checks you run without naming them don't disappear when you automate. They have to go somewhere. This chapter is about making them explicit before the automation falls into the gap you left.*

---

There is a deceptively simple question hiding inside every automation decision, and almost nobody asks it before they ship.

The question is: *what work are you currently doing by hand that you are about to stop doing?*

Not the work the automation does — you have thought about that. The invisible work. The implicit checks you run without naming them. The judgment calls you make so fast you have forgotten they are judgment calls. When you do a task by hand, you handle exceptions as they arise. You notice when a source looks unreliable. You hedge when two pieces of information conflict. You ping a colleague when something feels too consequential to pass along without a second set of eyes. None of that is in your prompt. All of it is in your head, running continuously, as you work.

When you automate a task, that work does not disappear. It has to go somewhere. Either you design it into the automation explicitly — specifying what to do when reality does not match the design case — or you leave it as a gap, and the automation runs forward into that gap until it falls in.

This chapter is about designing the work in. And the first thing to know is that doing so changes the shape of the specification considerably.

---

Let me make this concrete with a comparison. Suppose you are producing a weekly competitive intelligence summary — a one-page document that lands in your team's Slack channel every Monday morning, covering the past week's moves by your top competitors. You have done this by hand. It works. Now you want to automate it.

Here is the specification you would write if you were doing this task by hand one time, with you at the keyboard:

> Produce a one-page competitive intelligence summary for the team's Slack channel, drawn from the past week's news in our source list, focused on the top six competitors and on segment-level developments. Audience: the team, read in five minutes. Tone: declarative; flag confidence on each item. Format: bulleted, grouped by competitor, then a "segment trends" section. Every claim hyperlinked to its source.

That is a good Augmentation specification. It is one paragraph. It is complete for the case where a skilled person is doing the work in real time, handling exceptions as they arise.

Here is what the Automation specification looks like for the same task:

> Produce a one-page competitive intelligence summary, generated automatically every Monday at 6 AM, posted to the team Slack channel. Audience: the team, read between 8 and 9 AM. Tone: declarative; explicit confidence label on each item.
>
> Source list: see appendix. Each source has been validated for the prior six weeks against retraction history; sources with retraction frequency over 1% are excluded. Source list is reviewed monthly.
>
> Pre-flight checks, run before generation: for each article in the input set, query the publication's retraction page; exclude any article flagged within the past 14 days. For each article older than five days, include a freshness flag in the output. If more than 20% of input articles are flagged or excluded, do not generate the report; instead post to the channel: "Pre-flight check failed; report manually triggered."
>
> Generation rules: one bullet per item, maximum 30 words. Each bullet hyperlinked to source. Confidence label on each bullet: HIGH (multiple independent sources, recent), MEDIUM (single reliable source, recent), LOW (single source, contested, or older than five days). Bullets labeled LOW are grouped at the bottom under "Provisional — verify before citing."
>
> Exclusions: do not summarize opinion pieces unless flagged as analysis. Do not produce forecasts. Do not synthesize across competitors in ways that imply correlation; report each separately. Do not include claims that cannot be sourced to an article in the input set.
>
> Output format: top section "Competitor moves," six headers in fixed order even if a competitor had no news. Middle section "Segment trends." Bottom section "Provisional." Always end with: "Source list version [N], generated [date], by [system identifier]. For corrections, contact [owner]."
>
> Failure-mode handling: if the model returns no output, post "Generation failed; manual report by EOD." If the output exceeds 800 words, truncate to the top ten items by recency and post with note. If the model produces a citation that does not match an article in the input set, drop that bullet and log the event.
>
> Diligence design, runs separately: each week, the named owner reads the full report and spot-checks two random bullets to source. Once a month, run a fixed test set — ten articles from a held-out validation pool — against the current automation and compare against the locked baseline. Any deviation from baseline categorization is reviewed. Once a quarter, compare the prior quarter's reports against ground-truth events and compute hit rate and false-positive rate.
>
> Named accountable human: [owner]. Backup: [name]. Escalation: [manager] if any failure-mode trigger fires two weeks in a row.

The second specification is roughly three times the length of the first. Most people, when they first see this, assume something has gone wrong — that the specification has been over-engineered, that the extra length is bureaucratic cover for a simple task. It is not. The extra length is honest accounting for the work a human would have done implicitly if she had been at the keyboard. The implicit work did not disappear when you decided to automate. You wrote it down.

<!-- → [IMAGE: Side-by-side annotated comparison — left column: the Augmentation spec (one paragraph, no section headers), right column: the Automation spec with callout labels pointing to each structural addition: "pre-flight checks = input-quality anticipation", "confidence labels = output-quality signaling", "exclusions = model-failure prevention", "failure-mode handling = six ambiguity types addressed", "diligence design = four failure modes addressed", "named accountable human = accountability gap closed"; student should see at a glance that the extra length is structured, not random, and maps directly to implicit work the human would have done at the keyboard] -->

That is the core discipline of Automation specification: make the implicit explicit, in advance, because nothing about the execution will be in person.

---

The additional length in an Automation specification is not random. It clusters into six categories of anticipated deviation — six ways reality can fail to match the design case, which the specification has to address because no one will be present to address them in the moment.

The first is input-quality variation. What does the system do when an input is degraded, missing, or formatted differently than expected? For the competitive intelligence report, this means retractions, paywalls, and articles older than expected. For other automations, it means missing fields in a submitted form, a corrupted file, an upstream API that returned an error code instead of data. The specification should answer: what behavior do we want, and how does the system detect when input quality has degraded below the threshold where we trust the output?

The second is output-volume variation. What does the system do when the output is substantially longer or shorter than the design case? The 800-word truncation rule in the automation spec above is an answer to this. If a model is left unconstrained on volume, it will, in some fraction of runs, produce outputs that violate the format the downstream consumer expects — a five-paragraph analysis when someone expected three bullets, a one-line summary when someone expected a full page. The automation needs to handle this without halting.

The third is context shifts the model cannot detect. What does the system do when the world has changed in a way the model has no access to? The model does not know that a new competitor entered the market last Thursday, or that a regulatory change last month made certain claims non-compliant, or that the segment you have been tracking just got redefined by the trade press. For slowly-changing context, the monthly source-list review addresses this. For fast-changing context, the pre-flight check and the weekly spot-check are what surface it. The key design question is: what kinds of context change would break this automation's validity, and how would we know that happened?

The fourth is ambiguous inputs. What does the system do when the input is internally contradictory or unclear? For the competitive intelligence task, this is two sources reporting different versions of the same event. For other automations, it is a data row that violates an expected constraint, a customer message that spans multiple issue types, a document with conflicting version numbers. The model will produce output regardless; the question is whether the output it produces in ambiguous cases will be handled correctly by the downstream consumer, or whether ambiguity should trigger a flag that surfaces the conflict to a human.

The fifth is high-stakes outputs. Some outputs, as special cases, are more consequential than the design baseline. A major competitor acquisition in the week's news changes how everything else in the report should be interpreted — it is not just another item. A risk flag in a financial summary warrants different handling than a routine variance. The automation spec should describe what high-stakes looks like, how to detect it, and what the system should do differently when it detects it. Often the right answer is not to handle high-stakes outputs within the automation at all — it is to detect them, halt, and surface them to a human.

The sixth is model-specific failure modes. What does the system do when the model hallucinates, refuses, or produces output that does not pass the format specification? The citation-verification step in the automation spec above is designed to catch one specific form of hallucination: a confident-looking citation that does not correspond to any article in the input set. Other failure modes include output in the wrong language, output that exceeds or falls below format constraints, output that contains a refused section without flagging it, output that looks syntactically correct but carries a semantic error only detectable by checking against the source. Each of these needs a detection step and a handling rule.

Run through these six categories before you ship any automation. For each one, ask: have I addressed this? If the answer is no, the specification is incomplete. The six categories are not exhaustive — there are failure modes specific to your domain that are not on this list — but addressing all six gets you through the common cases.

<!-- → [TABLE: The six anticipatory categories as a pre-ship checklist — columns: Category, What it addresses, Detection mechanism, Handling rule, Example from the competitive intelligence spec; rows: Input-quality variation / Output-volume variation / Context shifts the model cannot detect / Ambiguous inputs / High-stakes outputs / Model-specific failure modes; student should print this and run through it before shipping any automation] -->

---

The automation specification covers what happens during execution. The Diligence design covers what happens between executions — the monitoring that keeps the automation valid over time.

Chapter 7 introduced three drift forms: model drift, context drift, and use-case drift. Automations are more vulnerable to all three than Augmentation workflows, because the automation runs without a human present to notice when something has gone wrong. A human doing a task by hand will catch drift reflexively; the automation will not catch it unless you design a check that runs separately from the execution.

There are four specific failure modes every Automation's Diligence design should address.

The first is input drift. The inputs to the system are no longer representative of the inputs it was designed for. Sources that were reliable in February are less reliable in October. The data schema that the automation was built to parse has been quietly updated upstream. The customer tickets that used to arrive in English are now arriving in a mix of languages the original prompt was not tested on. For the competitive intelligence automation, input drift is addressed by the monthly source-list review with an explicit retraction-frequency threshold. For other automations, the analogous check is: periodically re-examine whether the inputs that arrive in production still look like the inputs the automation was designed to handle.

The second is output drift. The model is producing different outputs than it did at setup, given matching inputs. This is the model-drift problem from Chapter 7, now embedded in an automation rather than a human-supervised workflow. The check is a fixed test set — a small held-out pool of inputs where you know, from manual evaluation at setup, what the correct output is — re-run against the production automation on a fixed schedule. Any deviation from the locked baseline gets reviewed. Not every deviation is a problem; a model update might improve output quality. But the deviation should be detected and examined, not silently absorbed.

The third is context shift. The world the automation operates in has changed in ways the system does not know about. For the competitive intelligence automation, the quarterly outcome audit — comparing reports against actual events that happened in the sector — is the check for context shift. For other automations, the analogous check is: periodically look at the downstream consequences of the automation's outputs and ask whether the outputs are still correct in the world as it now exists, not the world as it existed at setup.

The fourth is the accountability gap. No human is actively monitoring; no human is on the hook. The automation runs on a schedule, produces outputs on a schedule, and the person who set it up has moved on to other things. This is the failure mode that makes the other three invisible. The fix is the named accountable human — the single person whose job description includes maintaining this automation, not just using it — with a recurring calendar commitment that forces their eyes on the output at a minimum frequency. For the competitive intelligence automation, this is the weekly Friday spot-check: fifteen minutes, two bullets checked to source, the output read in full. Not because the spot-check catches everything; because it creates a human in the loop with a reason to notice when something looks wrong.

The four Diligence moves are not heavy in aggregate. A weekly spot-check is fifteen minutes. A monthly fixed-test re-run is an hour. A quarterly outcome audit is a half-day. Across a year, this is roughly forty hours — the overhead of running the automation responsibly. That cost is real. It is also, in any domain where the automation's failures would be consequential, much smaller than the cost of the audit that follows when no one was watching.

<!-- → [TABLE: The four Diligence failure modes and their monitoring moves — columns: Failure mode, What it looks like when it occurs undetected, Diligence move that catches it, Cadence, Approximate annual time cost; rows: Input drift / Output drift / Context shift / Accountability gap; final row shows total ~40 hours/year; student should use this to cost out the diligence design for any automation they are considering and compare against the blast radius of an undetected failure] -->

---

I want to address the objection directly, because you will hear it.

The Automation specification is long. Someone looking at it will ask why — whether the length reflects over-engineering, whether a simpler spec would work just as well, whether the Diligence design is necessary overhead on a tool that runs without problems most of the time.

The answer is that the length reflects the transfer of work. When you do a task by hand, the implicit checks you run continuously — is this source reliable? does this seem right? should I flag this before passing it along? — are real work. They are not in any specification because they live in your head. When you automate the task, that work has to go somewhere explicit, because the automation has no head. Every item in the longer specification is a check you would have run in person. The choice is between making it explicit in the specification or leaving it as a gap the automation will eventually fall into.

The three-to-one ratio between the Automation specification and the Augmentation specification is not a feature of this particular task. It is a rough constant across task types, because the overhead is not about the content of the task — it is about the absence of a human in the execution loop. Any task complex enough to benefit from automation is complex enough to have implicit checks worth making explicit. The ratio stays roughly constant because the extra length is the transfer cost, and the transfer cost is proportional to the richness of the implicit work, not to the complexity of the domain.

If your Automation specification is the same length as your Augmentation specification, you have not yet done the anticipatory work. Either the task is genuinely so simple that the work is small — rare — or you are about to ship an automation you have not fully diligence-designed. Run through the six ambiguity types and the four failure modes, and see which ones you have addressed. If any are missing, finish the spec before you ship.

---

At some point, you will have to explain this to someone who did not read this book. A manager who wants to know why the spec is three pages for a task that took one paragraph last year. A budget conversation about the forty hours of annual monitoring. A compliance review that asks why the automation has a failure-mode handling section at all.

The case to make is not technical. It is about the transfer of work. When the task ran by hand, those forty hours happened implicitly, distributed across the person doing the task — in the pauses when she checked a citation, the moments when she flagged a conflicting source, the weekly rhythm of reading her own output before sending it. The automation does not eliminate that work. It makes it optional in the short run and necessary in the long run, because what is optional in the short run tends not to happen, and what does not happen in the long run produces the audits.

The Diligence design is what makes the automation defensible. Not defensible in the sense of immune to failure — automations fail — but defensible in the sense that when something goes wrong, you know what happened, you know when it started, and you can change the specific thing that broke without having to redesign the whole process. That is a different outcome than discovering, six months after the fact, that the automation has been running on drift and no one knows which outputs to trust.

The next chapter begins Part III. The automation in this chapter still runs on a schedule, produces text, and waits for a human to act on it. Part III takes you into the case where the model is not producing text for a human to act on — it is taking actions itself, in the world, on your behalf. The Loop will reweight again. The blast radius will expand again. The structural failure modes will be different from anything we have seen so far.

---

**What would change my mind.** If empirical practice showed that automations could run with Augmentation-grade specifications — that the anticipatory work adds overhead without reducing failure rates — the chapter is over-prescribed. The opposite is what I see: automations without explicit failure-mode handling and Diligence design fail in predictable ways at predictable cadence.

**Still puzzling.** I do not have a clean rule for how much anticipatory work is enough. The specification can always be longer. The cost of additional anticipation eventually exceeds the benefit. I cannot give you a general rule for where that point sits. Address each of the six ambiguity types and each of the four failure modes; depth within each is judgment informed by the stakes of the domain.

---

---

## Exercises

### Warm-up

**1. Identify the category.** For each gap in the specification below, name which of the six anticipatory categories it belongs to and write one sentence explaining your reasoning. *(Tests: ability to classify specification gaps against the six categories.)*

An automated system summarizes customer support tickets each morning and posts a digest to the support team's channel. The specification states: "Summarize the top ten tickets by volume, grouped by issue type. Tone: professional. Post by 8 AM."

- The specification does not say what to do if the upstream ticketing system returns no data that morning.
- The specification does not say what to do if two tickets report contradictory information about the same product issue.
- The specification does not say what to do if the digest runs to fifteen hundred words instead of the expected two hundred.
- The specification does not define what constitutes a high-stakes ticket — for example, a report involving a safety issue — or how it should be handled differently.

**2. The implicit-work question.** Choose a task you currently do by hand that involves judgment calls you make quickly and without naming them. List three implicit checks you run during that task — things you do that are not in any written specification, that you would stop doing if you handed the task to an automation. For each, write one sentence describing what would happen, over time, if the automation ran without that check. *(Tests: ability to identify implicit work before automating — the foundational skill the chapter teaches.)*

**3. Diligence design, named.** For each element of the competitive intelligence automation's Diligence design, name which of the four Diligence failure modes it addresses and explain the match in one sentence. *(Tests: ability to map specific monitoring mechanisms to the failure modes they address.)*

- Weekly Friday spot-check: owner reads the full report, spot-checks two bullets to source.
- Monthly fixed-test re-run against the locked baseline.
- Quarterly outcome audit comparing reports against ground-truth events.
- Named accountable human with backup and escalation path.

---

### Application

**4. Write the Automation specification.** You currently produce a monthly regulatory-change summary by hand: you scan three government agency websites and two trade publications for any rule changes or enforcement actions relevant to your industry, produce a one-page summary, and email it to the compliance team. Now you want to automate this. Write the full Automation specification. Your specification must address all six anticipatory categories. For each category, write the relevant rule, handling instruction, or detection step explicitly — not a placeholder, an actual rule. *(Tests: ability to produce the artifact, not just describe it.)*

**5. Diagnose the gap.** Here is a partial Automation specification for a system that generates weekly sales-performance summaries from a CRM database: *"Every Friday at 5 PM, query the CRM for closed deals in the prior seven days. Produce a summary with total revenue, deal count, and top five reps by revenue. Post to the sales channel."* Identify which of the six anticipatory categories are unaddressed. For each unaddressed category, write the specific rule, handling instruction, or detection step that would close the gap for this particular automation. *(Tests: ability to use the six-category framework as a diagnostic tool on a real spec.)*

**6. The forty-hour argument.** A manager reviewing your Automation proposal objects: "This says we'll spend forty hours a year monitoring a tool we built because it saves us forty hours a year. That's a zero-sum trade." Write a two-hundred-word response that makes the case for the forty hours without using the word "defensibility" or the phrase "the audit." Your argument should be specific to what the monitoring actually does — not a general claim about diligence being good. *(Tests: ability to articulate the chapter's core argument in a form that persuades someone who has not read it.)*

---

### Synthesis

**7. Specification versus Diligence design.** The chapter separates the Automation specification (what happens during execution) from the Diligence design (what happens between executions). Explain why these are two distinct things rather than one longer document — what work does each one do that the other cannot? Use the competitive intelligence automation as your reference case. Your answer should be 150–200 words and should make the distinction feel necessary rather than organizational. *(Tests: ability to articulate the structural logic of the chapter, not just its contents.)*

**8. Connect to Chapter 7.** Chapter 7 introduced model drift, context drift, and use-case drift in the context of a recurring human-supervised workflow. This chapter applies the same framework to automations running without human supervision. Identify the one way in which context drift is *harder* to catch in an automation than in a human-supervised workflow, and explain the specific Diligence mechanism this chapter provides to compensate. *(Tests: integration across chapters — ability to see how the same failure mode changes shape when the execution context changes.)*

---

### Challenge

**9. The three-to-one ratio.** The chapter claims the Automation specification will be roughly three times the length of the Augmentation specification for the same task, because the ratio is determined by the absence of a human in the execution loop rather than by the content of the task. Test this claim: choose a task substantially simpler than the competitive intelligence summary — a task where the Augmentation specification is three or four sentences — and write both the Augmentation specification and the full Automation specification for it. Does the ratio hold? If it does, explain what the extra length consists of. If it does not, explain what feature of the simpler task breaks the ratio and what this implies about the chapter's claim. *(Tests: ability to stress-test the chapter's generalizations rather than accept them.)*

**10. Design the high-stakes detection rule.** The chapter identifies high-stakes outputs as one of the six anticipatory categories, notes that the right response is often to detect them and surface them to a human rather than handle them within the automation, but does not give a general method for defining what "high-stakes" looks like or how to detect it algorithmically. For an automation of your choice — in a domain where high-stakes outputs occur — design the high-stakes detection rule: what triggers it, what the system does when triggered, who receives the escalation, and how you would validate at setup that the rule fires when it should and does not fire when it should not. Your design should be concrete enough that a developer could implement it. *(Tests: ability to complete the chapter's most underspecified component — going from principle to implementable design in a domain-specific context.)*

---

### LLM Exercise — Chapter 10: Specification and Diligence for Automation

**Project:** AI Fluency for [Your Role] — The Domain Field Manual

**What you're building this chapter:** Section 11 of the playbook — a complete anticipatory specification for ONE specific Automation in your role, fully populated against all six ambiguity types and all four failure modes, plus the diligence-design appendix it requires. This is the most directly-deployable artifact in the playbook — a reader could hand it to IT or run it themselves.

**Tool:** Claude Project (continue) + Cowork (write Section 11). Optional Claude Code if the Automation requires custom scripting.

---

**The Prompt:**

```
Continuing my Domain Field Manual playbook. My Role Dossier and Sections 1–10 are in the Project context. The "AUTOMATE NOW" bucket from Section 10 contains the candidates ready for design.

Botspeak Chapter 10 teaches:
- The Augmentation specification is one paragraph; the Automation specification is roughly THREE TIMES LONGER, mostly in anticipation work.
- SIX AMBIGUITY TYPES the spec must address: input-quality variation, output-volume variation, context shifts the model can't detect, ambiguous inputs, high-stakes outputs, model-specific failure modes.
- FOUR FAILURE MODES to design against: input drift, output drift, context shift, accountability gap.
- The defense to a stakeholder: "we built this Automation to do work I would otherwise do by hand; the work I do by hand carries implicit checks; the Automation does not run those checks unless we design them in."

For my playbook's Section 11, do four things:

TASK 1 — PICK ONE AUTOMATION TO SPECIFY FULLY.
From Section 10's "AUTOMATE NOW" bucket, pick ONE — the one most representative of my role's typical Automation candidate. Justify the pick (why this one teaches the discipline best for my readers).

TASK 2 — THE COMPLETE ANTICIPATORY SPECIFICATION.
Write the full spec for the chosen Automation, in the exact format Botspeak Chapter 10 uses for the competitive-intelligence rebuild:

INTENT: [what, when, audience, tone]
SOURCE / INPUT LIST: [appendix, validated against what, reviewed how often]
PRE-FLIGHT CHECKS (run before generation): [the specific verifications]
GENERATION RULES: [the per-item structure, confidence labels, format]
EXCLUSIONS: [what the model is NOT to do]
OUTPUT FORMAT: [section structure, headers, length]
FAILURE-MODE HANDLING: [what to do when generation fails / output is malformed / hallucination is detected]
DILIGENCE DESIGN: [Friday spot-check, monthly fixed-test re-run, quarterly outcome audit, named owner, named backup, escalation path]

Each section should be FULLY populated for the chosen Automation in my role. Not "[insert constraints here]" — actual constraints. The spec should be THREE TIMES the length of an equivalent Augmentation spec for the same task. If it isn't, you haven't done the anticipatory work yet.

TASK 3 — THE SIX-AMBIGUITY-TYPE WALK-THROUGH.
For the spec produced in Task 2, walk explicitly through all six ambiguity types and confirm each is addressed:
- INPUT-QUALITY VARIATION — what the system does when an input is degraded, missing, or formatted differently
- OUTPUT-VOLUME VARIATION — what the system does when output is much longer or shorter than the design case
- CONTEXT SHIFTS — what the system does when the world has changed in ways the model can't detect
- AMBIGUOUS INPUTS — what the system does when input is internally contradictory
- HIGH-STAKES OUTPUTS — what the system does when an output looks unusually consequential
- MODEL-SPECIFIC FAILURES — what the system does when the model hallucinates / refuses / produces malformed output

For each: cite the specific section of the spec that addresses it. If the spec doesn't address one, fix the spec.

TASK 4 — THE STAKEHOLDER DEFENSE MEMO.
Write the 2–3 paragraph defense memo a reader could send to a manager who calls the spec "bloat" or who is reluctant to budget the diligence work. Frame the defense in my industry's risk vocabulary; quantify the cost of the diligence as a fraction of the cost of one undetected failure of the kind the diligence catches.

Save as `11-an-automation-fully-specified.md` in my playbook folder.
```

---

**What this produces:** Section 11 of the playbook — one fully specified Automation ready to deploy, with anticipatory spec, ambiguity-type audit, and stakeholder defense memo. ~3,500–5,500 words. The most directly-deployable artifact in the entire playbook.

**How to adapt this prompt:**
- *For your own project:* The Automation you pick should be one a reader of your playbook could ACTUALLY run within 90 days — pick achievable over impressive.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Recommended if the Automation involves data ingestion, scheduled runs, or drift-monitoring scripts. Pair Claude Code with the spec to produce a runnable scaffolding.
- *For Cowork:* Recommended for both the spec document and (potentially) running the Automation itself if it fits Cowork's scheduled-prompt model.

**Connection to previous chapters:** Section 10 screened candidates; Section 11 designs one in full. The discipline — anticipation, diligence-by-design — applies to every Automation a reader of the playbook ever specifies.

**Preview of next chapter:** Chapter 11 starts Part III — Agency. Section 12 of the playbook surveys the agentic deployments your domain is currently weighing or has launched, and applies the three structural failures to each.
