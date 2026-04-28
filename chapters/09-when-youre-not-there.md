# Chapter 9 — When You're Not There

*The Loop Without You in the Moment*

---

Here is a question worth sitting with before we go any further.

When you use an AI tool in the ordinary way — you type a prompt, you read the output, you decide whether to keep it or revise it — there is a human in the loop at every step. You are that human. The human is there not because anyone designed the system that way; the human is there because the system is just a chat window and you are sitting in front of it. The quality control is structural. It costs you nothing to achieve it, because the act of reading the output before doing anything with it is the quality control.

Now suppose you automate something. Suppose you set up a process where the model runs on a schedule — every Monday morning, say, pulling last week's news, generating a summary, posting it to a Slack channel before anyone arrives. The process runs. The model generates output. The output goes somewhere and acts in the world. And you are not there. You are asleep, or in a meeting, or unaware that anything ran.

The question is: where did the quality control go?

This is not a rhetorical question. The quality control did not disappear. It has to exist somewhere, in some form, or the automation is a reliability-time-bomb waiting for its trigger. The work of this chapter is to show you exactly where the quality control has to go, and why designing it in deliberately is the difference between an automation that serves you and one that eventually produces the call from your manager asking how something like this happened.

---

## What a failure looks like at scale

Let me make this concrete with the kind of failure that actually occurs.

A junior analyst — call her Tessa — builds a small automation. Every Monday morning it pulls the past week's news from a curated set of trade publications, hands the articles to a language model with a structured prompt, and posts a one-page competitive intelligence summary to her team's Slack channel. For six weeks the automation runs cleanly. The team reads it. People cite it in meetings. Tessa puts it in her self-review.

In week seven, one of the source articles turns out to be wrong. A trade publication ran a story about a competitor's product launch; two days later the publication retracted it. The retraction did not make it into Tessa's curated source list. The model, working only from the original article, summarized the product launch as current fact. The summary posted Monday morning. The CFO, who was heading into a board call and wanted to sound current on competitive developments, cited it. The board chairman, who had seen the retraction in his own news feed, asked whether the CFO was sure. The CFO was not sure. A three-million-dollar strategic decision that depended in part on the competitive picture was paused for the analysis to be redone.

Notice the shape of this failure. The model did not hallucinate. It did not fabricate. It faithfully summarized a real article from a real publication. The article was simply no longer true by the time the model read it, and the model had no way to know that, and the spec had not anticipated the possibility. The failure is not a model failure — it is a design failure. Specifically, it is the failure you get when you remove the human from the loop and do not replace the human with anything.

<!-- → [INFOGRAPHIC: A timeline of Tessa's automation failure — seven weeks on a horizontal axis. Weeks 1–6 marked as "clean runs / trust accumulates." Week 7 marked with the retraction event, the wrong output, and the downstream chain: CFO cites it → board call → strategic decision paused. Annotate the gap between "model ran correctly" and "output was wrong" to make the design failure visible. The student should see that the model did nothing unusual; the system did.] -->

In ordinary augmentation work, this error never happens. Tessa would have read the source article herself, or at minimum read the model's summary before it went anywhere, and would likely have checked the publication before forwarding claims about a competitor to her CFO. The error is impossible when a human is actively in the loop. The error is nearly inevitable, given enough recurrences, when the human has been systematically removed.

---

## How the Loop reweights

In every chapter up to this one, I have been describing a loop: you specify the task, you delegate some portion of it to the model, you have a conversation that refines the output, you apply the four verification layers, and you maintain the practice over time. That loop runs with you at the keyboard. You conduct it in real time.

When you automate something, the loop does not disappear. It runs. But you do not. Every step of the loop still has to happen — specification, delegation, conversation, discernment, maintenance — but some steps that were reflexive in person become impossible without explicit design. The automation changes where the weight falls.

<!-- → [TABLE: The loop reweighting table — rows for each loop step (Specification, Delegation, Conversation, Discernment, Maintenance), columns for "In ordinary augmentation" vs. "In automation." Each cell describes how that step works in each mode and what design work the shift requires. The student should be able to see at a glance which steps become load-bearing in automation and why.] -->

**Specification** becomes harder, not easier. When you are writing a one-off task, your spec covers one set of inputs you have in front of you. You know the context because you are in it. When you are specifying an automation, you are specifying a class of tasks the system will run against inputs you have not yet seen, in conditions that will change over time. Tessa's spec was correct for the normal case — articles from her curated list that were currently accurate. It was silent on what to do when an article had been retracted. A good spec for automation has to anticipate the ways the inputs will deviate from the design case, and it has to specify what the system should do when they deviate. The silence in the spec is where the failures live.

**Delegation** shifts from a real-time decision to a design-time commitment. In ordinary work, you decide in the moment which parts to delegate, and you can walk that decision back if the output looks wrong. In automation, you have already delegated, in advance, to a system that will run the same delegation every recurrence. The commitment is much harder to walk back, because the system is running without you. The question of what to delegate has to be answered more carefully, at design time, before any of the specific inputs have arrived.

**Conversation** gets frozen. When you are at the keyboard, the conversation between you and the model is iterative — you push back, you add context, you run the adversarial moves from Chapter 5. In automation, the conversation is whatever prompt you wrote at setup time, run exactly that way every recurrence. There is no one to push back on week seven's output. Whatever corrective moves you want the system to make, you have to bake them in as standing instructions. The model does not have a peer reviewer. You are not there to be one.

**Discernment** is where Tessa's automation failed. In ordinary work, discernment is what you do before the output leaves your desk — the four verification layers applied to the specific thing you just built. In automation, discernment cannot happen in real time on every output, because the volume is too high and you are not there. Discernment has to shift to a different schedule: periodic sampling, adversarial test cases run at intervals, retrospective audits. These are not equivalents of real-time verification — they are approximations, with gaps. The gaps are where the failure happens in week seven.

**Maintenance** becomes the most important step, not a nice-to-have afterthought. In ordinary work, maintenance is the practice of keeping a process healthy over time — checking for drift, auditing outcomes, naming who is accountable. In automation, maintenance is the only mechanism by which you learn that the system is failing. Without explicit maintenance design, the automation runs until someone notices a bad output — which means the failure has already propagated some number of times before it was detected.

This is the shape of the reweighting. Specification and maintenance become load-bearing in ways they are not in ordinary work. Discernment has to be redesigned around the absence of a real-time human. The conversation has to be preloaded with the corrections the model would need in advance. These reweightings are not obvious when you set the automation up, because setting it up feels like any other task: write a prompt, test it on a few examples, confirm it works. The testing does not reveal the reweighting. The reweighting only becomes visible when the failure arrives.

---

## The blast radius scales differently

There is something about automation failures that is not obvious until you think it through carefully.

When a model produces a wrong output in ordinary augmentation work, the blast radius is bounded. It is one piece of work. You catch the error, you correct it, you ship the corrected version. The damage is proportional to the time you spend on rework.

When a model produces a wrong output in an automation, the blast radius is proportional to *how long the failure goes undetected multiplied by the downstream consequences of each wrong output*. If Tessa's automation produces a wrong output every Monday for six weeks before anyone notices — not six weeks in our story, but a plausible duration — then there are six wrong reports in the team's history, and there are six weeks of decisions made partly on the basis of those reports, and the task of auditing the damage is much harder than the task of correcting a single piece of work.

The scaling is not linear if the wrong outputs compound. A wrong competitive analysis in week three shapes how someone frames a conversation in week four. The wrong frame shapes a decision in week five. The decision structures a commitment in week six. By week seven, the wrong output from week three has influenced a chain of things that cannot be easily unwound. This is not a worst case. It is a realistic case for any automation where the outputs feed into a running process.

<!-- → [CHART: Two line graphs side by side — left shows blast radius in ordinary augmentation (flat, bounded, single point of damage); right shows blast radius in automation over time (grows from first wrong output, potentially compounds nonlinearly if outputs feed downstream decisions). The visual should make the scaling difference visceral, not just stated.] -->

The design implication is stark: *you cannot rely on accidentally noticing that an automation is failing*. In ordinary work, you notice because you are reading the output. In automation, you have deliberately arranged not to read the output in real time. Noticing has to be designed. It has to be a scheduled, explicit, accountable activity, built in at setup time, because if it is not built in, it does not happen — and the blast radius grows from the moment the first wrong output appears until the moment someone happens to look.

---

## Three tests before you automate

There is a set of conditions under which automating a task is appropriate. If the task does not meet those conditions, automation will produce the kind of failure I have been describing — maybe not in week seven, maybe not for months, but eventually, when the inputs drift into territory the spec did not anticipate.

The tests are not complicated. They take five minutes. Run them before you commit to automating anything consequential.

**Is the scope bounded?** Can you describe, in a single paragraph, exactly what the task does and what it does not do, in terms you would defend to your manager? Tessa's task was: summarize the past week's articles from this curated list of sources, in this format, at this time. That is bounded. The edges are clear. Compare to: automate market intelligence. That is not bounded. The surface area is too large for any spec to be tight, which means the model will be making scope decisions in real time that you have not authorized it to make. If the task is not bounded, you cannot specify it well, and if you cannot specify it well, you cannot design the discernment and maintenance around its failure modes.

**Are the inputs predictable?** Are the inputs the system will receive within a known range that your design cases actually represented? Tessa's inputs were mostly predictable — trade publication articles in a known format from a curated source list. Two failure modes were invisible during setup: retracted articles, and behind-paywall articles the model could not fully read. These were rare but possible. The model had never encountered them during testing. They were waiting in the tail of the input distribution.

The question to ask is not whether the typical input is predictable. The typical input is almost always predictable. The question is whether the *atypical* inputs — the ones that are rare but real — are represented in your design cases, and whether the spec tells the model what to do when it encounters them. If the spec is silent on the atypical inputs, the atypical inputs are where the failures will be.

**Is the blast radius acceptable if the system fails continuously for weeks?** This is the test most often skipped because failure feels hypothetical during setup. It does not feel hypothetical after the CFO's call. The right way to run this test is to assume the failure will happen — not as a possible outcome, but as a scheduled event — and to ask what the accumulated damage will be when you finally notice. If the answer is that the damage is manageable, that the outputs are low-stakes enough that continuous failure would be caught and corrected without lasting consequences, then automating is appropriate. If the answer is that six weeks of wrong outputs would have already propagated into decisions that are hard to reverse, then either do not automate, or build in explicit human checkpoints that catch each output before it acts in the world.

These three tests do not eliminate risk. Nothing does. What they do is force you to think about the failure mode before the failure rather than after it. Most automation deployments that go wrong were built by people who never asked whether the blast radius was acceptable, because the failure felt so remote at setup time that the question seemed unnecessary. The question is most necessary exactly when it seems unnecessary.

---

## Designing the noticing

The phrase Tessa writes down, after her conversation with her CFO, is this: *designing the noticing is part of designing the system*. That sentence is worth holding onto, because it names the thing that distinguishes a well-designed automation from one that is waiting to fail.

Designing the noticing means deciding, at setup time, how you will learn that the system is producing wrong outputs before those outputs have been acting in the world for weeks. There are three forms this can take.

*Sampling* is the simplest: commit, at setup time, to reading a fraction of the outputs in full. Not spot-checking every Monday at random, but a scheduled, accountable practice — Tessa reads the full automation output every Friday and spot-checks one source. Sampling does not catch every failure. It catches failures that are persistent enough to appear in the sample, which is most of the failures that matter.

*Adversarial test cases* are inputs you construct to probe the failure modes you identified during the bounded-scope and predictable-inputs tests. In Tessa's case, an adversarial test case might be a retracted article inserted into the source list to see whether the model flags it or silently summarizes it. You run these test cases periodically, not just at setup, because the model's behavior can shift when the inputs shift. Adversarial testing is how you find the failure mode before it finds you.

*Outcome auditing* is periodic review of what the automation produced against what actually turned out to be true. Once a quarter, Tessa reviews the past quarter's competitive summaries against what the competitors actually did. The audit catches systematic bias, systematic omission, or systematic mischaracterization that sampling might miss because each individual output looked plausible. Outcome auditing is the slowest of the three forms but the one that catches the failures that are structurally correct and substantively wrong — the ones that look fine on the day and turn out to have been quietly misleading.

<!-- → [INFOGRAPHIC: A three-panel diagram showing the three noticing forms (Sampling, Adversarial Test Cases, Outcome Auditing) — for each: what it catches, what it misses, and suggested cadence. Should function as a quick-reference card for designing the noticing layer of any automation. Place here immediately after the three forms are introduced.] -->

Building these three practices into the automation at design time is not optional infrastructure. They are the quality control that replaces the human who is no longer there.

---

## What the next chapter covers

The two things this chapter has established are the conditions for appropriate automation and the shape of the noticing design. Chapter 10 takes both of them into depth: what anticipatory specification looks like when it is done carefully — the kind of spec that prepares the system for inputs it has not yet seen — and how to build the discernment and maintenance practices into the automation's design from the first day. By the end of that chapter, you will be able to specify a small automation with the failure modes addressed in writing and the noticing built in.

---

*What would change my mind.* If automation infrastructure evolved to include retraction-detection, drift-detection, and outcome-monitoring as default turnkey capabilities — things you configure rather than design from scratch — the manual design work I describe here would shift. Some platforms are beginning to move in this direction. The discipline would remain the practitioner's even then; what changes is how much of the implementation is handed to you. As of early 2026, the implementation is mostly yours.

*Still puzzling.* I do not have a clean estimate of what fraction of currently deployed AI automations would fail an honest run of the three appropriateness tests. My sense, from watching organizations adopt these tools, is that it is high — most were built without the tests being run, because the tests feel like friction during the excitement of setup. I would like data on this. I do not have it.

---

## Exercises

### Warm-up

**1.** In ordinary augmentation work, the human is "in the loop" without any deliberate design effort. Explain why this is the case, and why removing the human from the loop in automation does not remove the quality control requirement — it only relocates it. Where does the quality control have to go? *(Tests: core conceptual understanding of why automation changes the design problem.)* — *Warm-up / Easy*

**2.** The chapter describes Tessa's failure as a design failure, not a model failure. Explain what this distinction means. The model behaved correctly by its own logic — so what, specifically, failed? *(Tests: ability to locate the failure at the right level of analysis: spec design, not model behavior.)* — *Warm-up / Easy*

**3.** Name the five loop steps described in the chapter (Specification, Delegation, Conversation, Discernment, Maintenance). For each one, write a single sentence describing how it works differently in automation compared to ordinary augmentation. *(Tests: recall and functional understanding of the loop reweighting.)* — *Warm-up / Medium*

---

### Application

**4.** A marketing team wants to automate a weekly email to 40,000 subscribers that summarizes the company's new content. The model pulls from an internal content feed, generates the email body, and sends it. Run the three appropriateness tests (bounded scope, predictable inputs, acceptable blast radius) on this automation. For each test, state whether it passes and identify the most significant risk that the test exposes. *(Tests: ability to apply the three pre-automation tests to a specific case and reason about the failure modes each test surfaces.)* — *Application / Medium*

**5.** Tessa's automation had no designed noticing. Using the three noticing forms (sampling, adversarial test cases, outcome auditing), design a noticing layer for her competitive intelligence automation. For each form: specify the cadence, describe exactly what would be checked, and name the failure type it is designed to catch. *(Tests: ability to operationalize the noticing design for a concrete automation.)* — *Application / Medium*

**6.** The chapter states: "The question to ask is not whether the typical input is predictable. The question is whether the *atypical* inputs are represented in your design cases." Choose one of the following automations and identify three atypical input conditions its design cases are most likely to have missed. For each condition, describe what the model would probably do, and what the spec would need to say to handle it:

- An automation that categorizes incoming customer support tickets by topic and routes them to the appropriate team
- An automation that generates a daily cash-flow summary from a company's transaction data
- An automation that summarizes new scientific papers in a research area and flags ones relevant to a team's current project

*(Tests: ability to reason about tail inputs and their implications for spec design.)* — *Application / Hard*

---

### Synthesis

**7.** The chapter introduces a compound failure mode: wrong outputs that feed into a running process can cause downstream decisions to compound the original error, so that the blast radius grows nonlinearly. Connect this to the four verification layers from Chapter 6. Which layers become structurally impossible to run in real time on automated outputs? Which layers could be approximated through the three noticing forms, and how? Which layer is most likely to go permanently unaddressed in a typical automation deployment, and what is the consequence? *(Tests: ability to synthesize across Chapter 6 and Chapter 9 and reason about which verification work can and cannot survive the removal of a real-time human.)* — *Synthesis / Hard*

**8.** The chapter's three appropriateness tests (bounded scope, predictable inputs, acceptable blast radius) are framed as a five-minute check before automating. Construct the case that these tests are insufficient on their own — that there are automation deployments that pass all three tests and still produce the kind of compounding failure the chapter describes. What condition or failure mode would such a deployment exploit? What fourth test, if added, would catch it? *(Tests: ability to stress-test the chapter's own framework and extend it.)* — *Synthesis / Hard*

---

### Challenge

**9.** Design an automation governance policy for a twelve-person analyst team that uses AI automations regularly. The policy should specify: how new automations are approved before deployment, what noticing design is required, how failures are reported and escalated, and how automations are retired when they degrade. The policy should be short enough to actually be used (one page or less) and specific enough that two team members would make the same decision about whether a given automation is compliant. Identify the two places where your policy requires the most judgment and explain why you could not make them more explicit without creating rules that would be gamed or ignored. *(Tests: Feynman test — can the student design a system that operationalizes the chapter's principles at team scale? Also tests honest reasoning about the limits of policy.)* — *Challenge / Open-ended*

**10.** The chapter ends with an open puzzle: "I do not have a clean estimate of what fraction of currently deployed AI automations would fail an honest run of the three appropriateness tests." Propose a study design that would produce that estimate. Specify: what population you would sample from, how you would operationalize "fails a test" so that two independent raters would agree, what confounds your design would need to control for, and what you would conclude if the fraction turned out to be very high (say, above 70%) versus very low (say, below 20%). *(Tests: ability to translate a practical puzzle into a researchable question, and to reason about what different answers would imply for the chapter's prescriptive claims.)* — *Challenge / Open-ended*
