# Chapter 9 — When You're Not There
*The Loop Without You in the Moment.*

Here is a question worth sitting with before we go any further.

When you use an AI tool in the ordinary way — you type a prompt, you read the output, you decide whether to keep it or revise it — there is a human in the loop at every step. You are that human. The human is there not because anyone designed the system that way; the human is there because the system is just a chat window and you are sitting in front of it. The quality control is structural. It costs you nothing to achieve, because the act of reading the output before doing anything with it is the quality control.

Now suppose you automate something. Suppose you set up a process where the model runs on a schedule — every Monday morning, say, pulling last week's news, generating a summary, posting it to a Slack channel before anyone arrives. The process runs. The model generates output. The output goes somewhere and acts in the world. And you are not there.

The question is: where did the quality control go?

This is not rhetorical. The quality control did not disappear. It has to exist somewhere, in some form, or the automation is a reliability time-bomb waiting for its trigger. The work of this chapter is to show you exactly where the quality control has to go, and why designing it in deliberately is the difference between an automation that serves you and one that eventually produces the call from your manager asking how something like this happened.

---

Let me make this concrete with the kind of failure that actually occurs.

A junior analyst — Tessa — builds a small automation. Every Monday morning it pulls the past week's news from a curated set of trade publications, hands the articles to a language model with a structured prompt, and posts a one-page competitive intelligence summary to her team's Slack channel. For six weeks the automation runs cleanly. The team reads it. People cite it in meetings. Tessa puts it in her self-review.

In week seven, one of the source articles turns out to be wrong. A trade publication ran a story about a competitor's product launch; two days later the publication retracted it. The retraction did not make it into Tessa's curated source list. The model, working only from the original article, summarized the product launch as current fact. The summary posted Monday morning. The CFO, heading into a board call, cited it. The board chairman, who had seen the retraction in his own news feed, asked whether the CFO was sure. The CFO was not sure. A three-million-dollar strategic decision was paused for the analysis to be redone.

Notice the shape of this failure. The model did not hallucinate. It did not fabricate. It faithfully summarized a real article from a real publication. The article was simply no longer true by the time the model read it, and the model had no way to know that, and the spec had not anticipated the possibility. This is not a model failure. It is a design failure — specifically, the failure you get when you remove the human from the loop and do not replace the human with anything.

<!-- → [INFOGRAPHIC: A seven-week timeline of Tessa's automation. Weeks 1–6 marked "clean runs / trust accumulates." Week 7 marked with three annotated events in sequence: retraction published → wrong summary posted → CFO cites it at board call → strategic decision paused. A callout should highlight the gap between "model ran correctly" and "output was wrong," making the design failure — not the model — visible as the locus of error.] -->

![Figure 9.1 — A seven-week timeline of Tessa's automation. Weeks 1–6 marked "clean runs / trust accumulates." Week 7 marked with three annotated events in sequence: retraction published → wrong summary posted → CFO cites it at board call → strategic decision paused. A callout should highlight the gap between "model ran correctly" and "output was wrong," making the design failure](images/09-when-youre-not-there-fig-01.jpg)

In ordinary augmentation work, this error never happens. Tessa would have read the source article herself, or at minimum read the model's summary before it went anywhere, and would likely have checked the publication before forwarding claims about a competitor to her CFO. The error is impossible when a human is actively in the loop. Given enough recurrences, it is nearly inevitable when the human has been systematically removed.

---

Every chapter up to this one has described a loop: you specify the task, you delegate some portion to the model, you have a conversation that refines the output, you apply the verification layers from Chapter 6, and you maintain the practice over time. That loop runs with you at the keyboard. You conduct it in real time.

When you automate something, the loop does not disappear. It runs. But you do not. Every step still has to happen — specification, delegation, conversation, discernment, maintenance — but some steps that were reflexive in person become impossible without explicit design. The automation changes where the weight falls.

<!-- → [TABLE: The loop reweighting — rows for each loop step (Specification, Delegation, Conversation, Discernment, Maintenance), columns for "In augmentation" vs. "In automation." Each cell describes how the step works in each mode and what design work the shift requires. The reader should be able to see at a glance which steps become load-bearing in automation and why.] -->

*Figure 9.2*

**Specification** becomes harder, not easier. When you write a one-off task, your spec covers one set of inputs you have in front of you. You know the context because you are in it. When you specify an automation, you are specifying a class of tasks the system will run against inputs you have not yet seen, in conditions that will change over time. Tessa's spec was correct for the normal case — articles from her curated list that were currently accurate. It was silent on what to do when an article had been retracted. A good spec for automation has to anticipate the ways the inputs will deviate from the design case, and has to specify what the system should do when they deviate. The silence in the spec is where the failures live.

**Delegation** shifts from a real-time decision to a design-time commitment. In ordinary work, you decide in the moment which parts to delegate, and you can walk that decision back if the output looks wrong. In automation, you have already delegated, in advance, to a system that will run the same delegation every recurrence. The commitment is much harder to walk back, because the system runs without you. The question of what to delegate has to be answered more carefully, at design time, before any of the specific inputs have arrived.

**Conversation** gets frozen. When you are at the keyboard, the conversation with the model is iterative — you push back, you add context, you run the adversarial moves from Chapter 5. In automation, the conversation is whatever prompt you wrote at setup time, run exactly that way every recurrence. There is no one to push back on week seven's output. Whatever corrective moves you want the system to make, you have to bake them in as standing instructions. The model does not have a peer reviewer. You are not there to be one.

**Discernment** is where Tessa's automation failed. In ordinary work, discernment is what you do before the output leaves your desk — the four verification layers applied to the specific thing you just built. In automation, discernment cannot happen in real time on every output, because the volume is too high and you are not there. Discernment has to shift to a different schedule: periodic sampling, adversarial test cases run at intervals, retrospective audits. These are approximations, with gaps. The gaps are where the failure happens in week seven.

**Maintenance** becomes the most important step, not a nice-to-have afterthought. In ordinary work, maintenance is the practice of keeping a process healthy over time — checking for drift, auditing outcomes, naming who is accountable. In automation, maintenance is the only mechanism by which you learn that the system is failing. Without explicit maintenance design, the automation runs until someone notices a bad output — which means the failure has already propagated some number of times before it was detected.

The reweighting is worth sitting with. Specification and maintenance become load-bearing in ways they are not in ordinary work. Discernment has to be redesigned around the absence of a real-time human. The conversation has to be preloaded with the corrections the model would need in advance. None of this is obvious when you set the automation up, because setting it up feels like any other task: write a prompt, test it on a few examples, confirm it works. The testing does not reveal the reweighting. The reweighting only becomes visible when the failure arrives.

---

There is something about automation failures that is not obvious until you think it through carefully.

When a model produces a wrong output in ordinary augmentation work, the blast radius is bounded. One piece of work. You catch the error, you correct it, you ship the corrected version. The damage is proportional to the rework.

When a model produces a wrong output in an automation, the blast radius is proportional to *how long the failure goes undetected multiplied by the downstream consequences of each wrong output*. If Tessa's automation produces a wrong output every Monday for six weeks before anyone notices — six weeks, not one — there are six wrong reports in the team's history, and six weeks of decisions made partly on their basis, and the task of auditing the damage is much harder than correcting a single piece of work.

The scaling can be worse than linear if wrong outputs compound. A wrong competitive analysis in week three shapes how someone frames a conversation in week four. The wrong frame shapes a decision in week five. The decision structures a commitment in week six. By week seven, the wrong output from week three has influenced a chain of things that cannot be easily unwound. This is not a worst case. It is a realistic case for any automation where the outputs feed into a running process.

<!-- → [CHART: Two line graphs side by side — left: blast radius in augmentation (flat, single point of damage, bounded); right: blast radius in automation over time (grows from first wrong output, potentially compounding nonlinearly when outputs feed downstream decisions). The visual should make the scaling difference visceral, not just stated.] -->

*Figure 9.3*

The design implication is stark: you cannot rely on accidentally noticing that an automation is failing. In ordinary work, you notice because you are reading the output. In automation, you have deliberately arranged not to read the output in real time. Noticing has to be designed. It has to be a scheduled, explicit, accountable activity, built in at setup time, because if it is not built in, it does not happen — and the blast radius grows from the moment the first wrong output appears until the moment someone happens to look.

---

Before automating any task, three tests. If the task fails one of them, do not automate it — at least, not without explicit additional safeguards. If it passes all three, automation is appropriate; the next chapter will show how to specify and design the maintenance around it.

**Is the scope bounded?** Can you describe, in a single paragraph, exactly what the task does and what it does not do, in terms you would defend to your manager? Tessa's task was: summarize the past week's articles from this curated list of sources, in this format, at this time. That is bounded. The edges are clear. Compare to: automate market intelligence. That is not bounded. The surface area is too large for any spec to be tight, which means the model will be making scope decisions in real time that you have not authorized it to make. If the task is not bounded, you cannot specify it well, and if you cannot specify it well, you cannot design the discernment and maintenance around its failure modes.

**Are the inputs predictable?** Are the inputs the system will receive within a known range that your design cases actually represented? Tessa's inputs were mostly predictable — trade publication articles in a known format from a curated source list. Two failure modes were invisible during setup: retracted articles, and behind-paywall articles the model could not fully read. These were rare but possible. The model had never encountered them during testing. They were waiting in the tail of the input distribution.

The question to ask is not whether the typical input is predictable. The typical input is almost always predictable. The question is whether the *atypical* inputs — the ones that are rare but real — are represented in your design cases, and whether the spec tells the model what to do when it encounters them. If the spec is silent on the atypical inputs, the atypical inputs are where the failures will be.

**Is the blast radius acceptable if the system fails continuously for weeks?** This is the test most often skipped because failure feels hypothetical during setup. It does not feel hypothetical after the CFO's call. The right way to run this test is to assume the failure will happen — not as a possible outcome, but as a scheduled event — and to ask what the accumulated damage will be when you finally notice. If the damage is manageable and the outputs are low-stakes enough that continuous failure would be caught and corrected without lasting consequences, then automating is appropriate. If six weeks of wrong outputs would have already propagated into decisions that are hard to reverse, either do not automate, or build in explicit human checkpoints that catch each output before it acts in the world.

These three tests take five minutes. They prevent most of the cases where automation should not have been deployed in the first place.

---

The phrase Tessa writes down, after her conversation with the CFO, is: *designing the noticing is part of designing the system.* That sentence names the thing that distinguishes a well-designed automation from one that is waiting to fail.

Designing the noticing means deciding, at setup time, how you will learn that the system is producing wrong outputs before those outputs have been acting in the world for weeks. There are three forms this takes.

*Sampling* is the simplest: commit, at setup time, to reading a fraction of the outputs in full on a scheduled basis. Not spot-checking whenever it occurs to you, but a regular, accountable practice — Tessa reads the full automation output every Friday and spot-checks one source. Sampling does not catch every failure. It catches failures that are persistent enough to appear in the sample, which is most of the failures that matter.

*Adversarial test cases* are inputs you construct to probe the failure modes you identified during the bounded-scope and predictable-inputs tests. In Tessa's case, an adversarial test case might be a retracted article inserted into the source list to see whether the model flags it or silently summarizes it. You run these test cases periodically, not just at setup, because the model's behavior can shift when the inputs shift. Adversarial testing is how you find the failure mode before it finds you.

*Outcome auditing* is periodic review of what the automation produced against what actually turned out to be true. Once a quarter, Tessa reviews the past quarter's competitive summaries against what the competitors actually did. The audit catches systematic bias or systematic omission that sampling might miss because each individual output looked plausible. Outcome auditing is the slowest of the three forms but the one that catches the failures that are structurally correct and substantively wrong — the ones that look fine on the day and turn out to have been quietly misleading.

<!-- → [INFOGRAPHIC: A three-panel reference card for the noticing forms — Sampling, Adversarial Test Cases, Outcome Auditing. Each panel: what it catches, what it misses, suggested cadence. The design should make this feel like a quick-reference tool the practitioner returns to when designing any new automation, not a one-time read.] -->

![Figure 9.4 — A three-panel reference card for the noticing forms](images/09-when-youre-not-there-fig-04.jpg)

Building these three practices in at design time is not optional infrastructure. They are the quality control that replaces the human who is no longer there.

---

The two things this chapter has established are the conditions for appropriate automation and the shape of the noticing design. Chapter 10 takes both into depth: what anticipatory specification looks like when done carefully — the kind of spec that prepares the system for inputs it has not yet seen — and how to build the discernment and maintenance practices into the automation's design from the first day. By the end of that chapter you will be able to specify a small automation with the failure modes addressed in writing and the noticing built in.

---

*What would change my mind.* If automation infrastructure evolved to include retraction-detection, drift-detection, and outcome-monitoring as default turnkey capabilities — things you configure rather than design from scratch — the manual design work I describe here would shift. Some platforms are beginning to move in this direction. The discipline would remain the practitioner's even then; what changes is how much of the implementation is handed to you. As of early 2026, the implementation is mostly yours.

*Still puzzling.* I do not have a clean estimate of what fraction of currently deployed AI automations would fail an honest run of the three appropriateness tests. My sense, from watching organizations adopt these tools, is that it is high — most were built without the tests being run, because the tests feel like friction during the excitement of setup. I would like data on this. I do not have it.

---

> **Going deeper — *Computational Skepticism for AI***
>
> Tessa's retraction failure is, in the language of the advanced volume, a **hidden assumption that failed silently** — the system was built on the assumption that sources are durable, the assumption was never written down, and the model had no way to know when the assumption had broken. The deeper book argues that procedural data validation (distributions, missingness, correlation checks) is necessary but not sufficient — that the failures that actually break deployments live in structural assumptions invisible to standard checks. The cure is the **six-step epistemic-frame reconstruction** that explicitly enumerates what the data is claimed to represent, what it actually represents, and what it excludes — including a prediction-lock about the failure pattern you would expect if a particular assumption broke.
>
> The advanced book also distinguishes prediction systems (where the worst output is wrong information) from **consequence systems** (where the worst output is wrong action in the world). Tessa's automation sits in between: it produces information, but the information drives consequential action by the CFO. This in-between zone is where most current automations sit — and where the loop reweighting in this chapter is most urgent.
>
> See *Computational Skepticism for AI*, **Chapter 5 — Data Validation** and **Chapter 9 — Validating Agentic AI**.

---

### LLM Exercise — Chapter 9: When You're Not There

**Project:** AI Fluency for [Your Role] — The Domain Field Manual

**What you're building this chapter:** Section 10 of the playbook — the appropriateness-test screen applied to typical automation candidates in your role. A ranked list of which tasks should be automated, which shouldn't, and which require specific modification before they can be — calibrated to your industry's risk tolerance.

**Tool:** Claude Project (continue) + Cowork (write Section 10).

---

**The Prompt:**

```
Continuing my Domain Field Manual playbook. My Role Dossier and Sections 1–9 are in the Project context.

Botspeak Chapter 9 introduces three APPROPRIATENESS TESTS that gate whether to automate at all:
1. BOUNDED SCOPE — can the task be described in one paragraph that you'd defend to your manager?
2. PREDICTABLE INPUTS — are the inputs within a known distribution the model has handled successfully?
3. LOW BLAST RADIUS — if the system produces wrong output every Monday for 6 weeks before anyone notices, what damage has been done?

Plus the principle: BLAST RADIUS SCALES WITH TIME-TO-DETECTION, not with per-output severity. And the design rule: DESIGNING THE NOTICING IS PART OF DESIGNING THE SYSTEM.

For my playbook's Section 10, do four things:

TASK 1 — INVENTORY OF AUTOMATION CANDIDATES IN MY ROLE.
List 6–10 tasks in my role that are CURRENTLY automated, plausibly will be in the next 12 months, or have been proposed to automate. For each:
- What the task is
- The current state (manual, partially automated, fully automated)
- Who would benefit from automation (the practitioner, the team, customers, the organization)
- Why it has not been fully automated (if it hasn't)

TASK 2 — APPROPRIATENESS-TEST APPLICATION.
For each candidate from Task 1, run the three appropriateness tests:
- BOUNDED SCOPE — pass / fail / partial, with one-line justification
- PREDICTABLE INPUTS — pass / fail / partial, with one-line justification
- LOW BLAST RADIUS — calibrated to my industry: estimate the cumulative damage of 6 weeks of undetected wrong output

Sort the candidates into three buckets:
- AUTOMATE NOW (passes all three; ready to design)
- AUTOMATE WITH MODIFICATION (passes 1–2; specify the modification needed)
- DO NOT AUTOMATE (fails 2–3; or the blast-radius answer is too high regardless)

TASK 3 — INDUSTRY-CALIBRATED BLAST-RADIUS GUIDANCE.
Different industries have different tolerance for the kinds of error that automated AI produces. A marketing automation that produces a wrong tagline is recoverable; a legal automation that misfiles a court date is much less so; a clinical automation that mis-screens a patient is critical. Calibrate the blast-radius test for my industry:
- What constitutes LOW blast radius in my industry? (Recoverable, single-instance errors)
- What constitutes MEDIUM blast radius? (Affects many customers; affects regulatory standing)
- What constitutes HIGH blast radius? (Affects safety; affects irreversible decisions; affects systemic trust)
- What is my industry's historical AI-automation failure that exemplifies "shouldn't have been automated"?

TASK 4 — THE ROLE-SPECIFIC LOOP REWEIGHTING.
The chapter notes that the loop reweights for automation — Specification, Discernment, Maintenance become heavier; Conversation freezes; Delegation moves to design-time. For my role, identify:
- Which loop step is my role's biggest weakness when designing automations? (Most roles drop the Maintenance design; some drop anticipatory Specification.)
- The role-specific antidote for that weakness
- A "before you ship an automation" checklist (5–8 items) that protects against the role's typical automation failure mode

Save as `10-when-to-automate.md` in my playbook folder.
```

---

**What this produces:** Section 10 of the playbook — an inventory of automation candidates with appropriateness-test verdicts, industry-calibrated blast-radius guidance, and a "before you ship an automation" checklist. ~3,000–4,500 words.

**How to adapt this prompt:**
- *For your own project:* The "DO NOT AUTOMATE" bucket is the section's most valuable bucket. Be unflinching about which currently-running automations in your industry shouldn't be.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful only if you want to script the appropriateness test as a structured form.
- *For Cowork:* Recommended.

**Connection to previous chapters:** Sections 1–9 covered work in Augmentation. Section 10 transitions to Automation — the loop without a human in the moment.

**Preview of next chapter:** Chapter 10 produces Section 11 — a complete anticipatory specification for ONE specific automation in your role, fully populated for the six ambiguity types and the four failure modes. The most directly deployable artifact in the playbook.

---

## Exercises

### Warm-Up

**1. Locate the quality control.** *(Conceptual | Difficulty: low)*
In ordinary augmentation work, the human is "in the loop" without any deliberate design effort. Explain in two or three sentences why this is the case, and why removing the human from the loop in automation does not remove the quality-control requirement — it only relocates it. Where, specifically, does the quality control have to go when the human is no longer there?

**2. Name the failure type.** *(Failure analysis | Difficulty: low)*
The chapter describes Tessa's failure as a design failure, not a model failure. Explain the distinction. The model behaved correctly by its own logic — so what, precisely, failed? Describe what the design would have needed to include to prevent the failure, in one specific sentence.

**3. Walk the reweighting.** *(Loop comprehension | Difficulty: medium)*
For each of the five loop steps — Specification, Delegation, Conversation, Discernment, Maintenance — write one sentence describing how it works differently in automation compared to ordinary augmentation. Then name the single step whose reweighting is both least obvious at setup time and most expensive when overlooked. Explain why.

---

### Application

**4. Run the three tests.** *(Appropriateness testing | Difficulty: medium)*
A marketing team wants to automate a weekly email to 40,000 subscribers summarizing the company's new content. The model pulls from an internal content feed, generates the email body, and sends it. Run all three appropriateness tests on this automation. For each test: state whether it passes, identify the most significant risk the test exposes, and name what the spec or design would need to say to address that risk.

**5. Design the noticing layer.** *(Noticing design | Difficulty: medium)*
Using the three noticing forms — sampling, adversarial test cases, outcome auditing — design a noticing layer for Tessa's competitive intelligence automation as it should have existed from day one. For each form: specify the cadence, describe exactly what would be checked or tested, and name the failure type it is designed to catch that the other two forms would miss.

**6. Find the tail inputs.** *(Predictable-inputs test | Difficulty: hard)*
The chapter states: "The question is not whether the typical input is predictable. The question is whether the atypical inputs are represented in your design cases." Choose one of the following automations and identify three atypical input conditions its design cases are most likely to have missed. For each condition, describe what the model would probably do if it encountered it, and what the spec would need to say to handle it correctly:

- An automation that categorizes incoming customer support tickets by topic and routes them to the appropriate team
- An automation that generates a daily cash-flow summary from a company's transaction data
- An automation that summarizes new scientific papers in a research area and flags ones relevant to a team's current project

---

### Synthesis

**7. Compound blast radius and the verification layers.** *(Cross-chapter synthesis | Difficulty: hard)*
The chapter introduces a compound failure mode: wrong outputs that feed into a running process can cause downstream decisions to grow the blast radius nonlinearly. Connect this to the four verification layers from Chapter 6. Which layers become structurally impossible to run in real time on automated outputs? Which could be approximated through the three noticing forms, and how closely? Which layer is most likely to go permanently unaddressed in a typical automation deployment, and what is the practical consequence of that gap?

**8. Stress-test the three tests.** *(Framework critique | Difficulty: hard)*
The three appropriateness tests are framed as a five-minute check that prevents most inappropriate deployments. Construct the case that they are insufficient: describe a specific automation that would pass all three tests and still produce a compounding failure of the kind the chapter describes. What condition or failure mode does your example exploit? Propose a fourth test that would catch it, and explain why the chapter's three tests do not.

---

### Challenge

**9. Design a team automation governance policy.** *(Feynman test | Difficulty: high)*
Design an automation governance policy for a twelve-person analyst team that uses AI automations regularly. The policy must specify: how new automations are approved before deployment, what noticing design is required as a condition of deployment, how failures are reported and escalated, and how automations are retired when they degrade. The policy must fit on one page and be specific enough that two team members would make the same classification decision about the same automation without consulting each other. Identify the two points in your policy that require the most judgment, and explain why you could not make them more explicit without creating rules that would be gamed or ignored.

**10. Operationalize the open puzzle.** *(Research design | Difficulty: high)*
The chapter ends: "I do not have a clean estimate of what fraction of currently deployed AI automations would fail an honest run of the three appropriateness tests." Propose a study design that would produce that estimate. Specify the population you would sample from, how you would operationalize "fails a test" so that two independent raters would agree, what confounds your design would need to control for, and what you would conclude if the fraction turned out to be very high (above 70%) versus very low (below 20%). Your conclusions should engage with the chapter's prescriptive claims — not just describe what the number would mean in the abstract.

---

## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Clarence "Skip" Ellis** was figuring out how systems behave correctly when multiple actors touch the same artifact at different times — decades before anyone thought about "AI automations running while you sleep." Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Clarence "Skip" Ellis, and how does his work on Operational Transformation and groupware connect to designing AI automations that act on shared resources when no human is in the chair? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Clarence Ellis (computer scientist)"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain Operational Transformation in plain language, as if you've never thought about concurrent edits
- Ask it to compare Ellis's groupware concerns to the three appropriateness tests in this chapter
- Add a constraint: "Answer as if you're sketching a noticing layer for a Tessa-style automation"

What changes? What gets better? What gets worse?
