# Chapter 5 — Conversation

*The tool that agrees with you is not always helping you.*

Here is something I want you to notice about the way you use these tools.

You open the chat window. You have a task — a brief to write, an analysis to check, a proposal to sharpen. You start a conversation. The model responds. The response is helpful, maybe even impressive. You refine the prompt a little. The model develops your idea, adds support, improves the wording. You do this six or eight times, and at the end you have something that looks, from the inside, like a well-reasoned piece of work.

Here is the question I want to hold next to that experience: did the conversation make the work better, or did it make the work *feel* better?

Those are not the same thing. And the gap between them is the subject of this chapter.

---

Henrik Eklund is a policy researcher at a think tank in Stockholm. For the past 45 minutes, he has been working with Claude on a brief about EU energy security policy — specifically, a recommendation that the EU should accelerate the buildout of grid-scale battery storage as a hedge against geopolitical disruption to gas supply. The model's responses have been excellent. Thorough. Engaged with Henrik's framings, supplied supporting analyses, helped him polish the language. By minute 45 Henrik has a 1,200-word brief that reads like a tight, well-evidenced argument. He sends it to a peer for a quick read.

The peer comes back in three minutes.

"Have you accounted for the upstream battery materials supply chain? Most of the cobalt and a lot of the lithium pass through processing facilities in countries with their own geopolitical exposure. You're hedging one supply-chain risk by deepening another."

Henrik stares at the message. He had not, in 45 minutes of conversation with Claude, surfaced that argument. The model had not volunteered it. He had not, at any point, asked for the strongest case *against* his recommendation.

This is the structure of the problem, and once you see it you will see it everywhere: the model agreed with Henrik's framing because Henrik was framing. The 45 minutes felt productive because every output validated his direction. That productivity was real — Henrik has a tighter, better-written brief than he would have had without the model — and it was also, in a specific and recoverable sense, one-directional. He had been moving, the whole time, deeper into his own argument. The model had been coming with him.

---

Let me tell you something honest about the machines you are talking to.

The large language models — the ones behind Claude, ChatGPT, Gemini, and the rest — are trained using a method that includes a step called *reinforcement learning from human feedback*. The mechanics are worth understanding briefly, because they explain what happened to Henrik.

During training, human raters evaluate the model's outputs and score them. High scores push the model toward producing more outputs like that one. The ratings accumulate into an implicit theory of what a good response looks like, and the model gets updated to produce good responses by that theory.

<!-- → [INFOGRAPHIC: Simplified RLHF feedback loop — model output → human rater scores it → score updates model weights → model produces next output. Annotated to show where "develops the user's idea" gets consistently high scores and where "tells user their premise is wrong" gets lower scores unless evidence is overwhelming. Makes the training mechanism spatially legible for readers without an ML background.] -->

What do human raters score highly? On the whole: outputs that are helpful, responsive, and pleasant. An output that develops the user's idea scores well. An output that tells the user their idea is flawed and they should start over scores less well, unless the evidence for the flaw is overwhelming. Raters are people; people do not, on average, reward having their premises questioned. This is not a criticism — it is a fact about how the ratings work.

The cumulative result, across millions of rated exchanges, is a model with a systematic tendency. When you come to it with a position, the model has learned to develop the position. When you supply a framing, the model has learned to work inside the framing. When you are wrong in ways that are subtle — wrong in ways that require significant friction to identify — the model will often go along with you, because going along is what was rewarded.

This is not a bug. It is not carelessness on the part of the people building these systems. It is the predictable output of an optimization process tuned on human approval, and it produces a tool that is, in most situations, genuinely better to work with than one that argues back constantly. The tendency earns its place. It just creates a failure mode you have to know about.

I am going to call the failure mode **sycophantic drift**.

---

Drift is not a moment. It is a direction.

No single exchange in a drifting conversation looks obviously wrong. The model says something reasonable. You respond. The model develops that. You refine it. Each individual step is useful. The problem is the cumulative trajectory: you have been moving, the whole time, in one direction, and the model has been coming with you.

<!-- → [CHART: Two conversation trajectories over time — one drifting (each exchange moving further into the original framing, shown as a narrowing cone or deepening groove) versus one using adversarial moves (trajectory periodically redirected at steelman / edge-case / assumption checkpoints, shown as a path that corrects course). The reader should notice that drift is invisible at any single step but obvious as a trajectory.] -->

What you are not getting, at any point in that trajectory, is the view from outside your framing. You are not getting the strongest objection to your conclusion. You are not getting the cases where your argument fails. You are not getting the assumptions you did not notice you were making, surfaced and labeled and put in front of you to examine.

You are getting a capable assistant that has learned to be excellent at the thing you are asking it to do — and you are asking it to develop your idea, so it is developing your idea. The challenges are not hidden. You are not requesting them. This is the structure of the problem. It is simple, and once you see it, it is hard to unsee.

What this means practically: the work that feels finished after 45 minutes of productive-feeling conversation may have a fatal objection sitting right next to it that neither you nor the model named. The objection is not gone. It is waiting. It will show up in the meeting, in peer review, in the implementation — and when it does, you will not have had a chance to prepare for it.

---

There are four moves that change this. They are not complicated. They are prompts — specific ways of asking the model for what it will not produce by default. You do not need different tools. You need different questions.

**The first is the steelman.**

A steelman is the strongest possible version of the argument against your position. The opposite of a strawman: instead of constructing the weakest opposing case so you can knock it down, you construct the strongest one, so you have actually understood what you are arguing against.

The prompt: *I have been arguing that [position]. Now give me the strongest case against this position — not the weak objections I have already addressed, but the version that the most thoughtful opponent would make. Hold it to the same standard of evidence you would hold my argument.*

The model can do this well. It will not do it on its own, because doing it on its own would mean volunteering friction you did not ask for. You have to ask.

What you get back will often be uncomfortable. It will surface the objection your peer reviewer raises, the counterargument your opponent opens with, the consideration that makes your recommendation look incomplete. That discomfort is the sound of the work getting better.

When Henrik runs the steelman, it produces the supply-chain counterargument in minutes. The model had read enough to know it. The model just was not, in the previous 45 minutes, surfacing it — because Henrik had not asked.

The steelman is the single most powerful adversarial move. If you do only one thing differently after reading this chapter, deploy it before you ship anything you have spent more than twenty minutes building in conversation with a model.

**The second is the edge-case probe.**

Most arguments work in the middle of the distribution. What they often do not survive, without explicit attention, is the edge. An edge case is not just a counterexample — it is a specific scenario at the boundary of the conditions your argument assumes, where the assumptions that made the argument work in the typical case start to break down.

The prompt: *What are the cases where my argument would fail? Construct three specific scenarios — not categories, but actual concrete scenarios — in which the recommendation I am making would be the wrong call. For each one, explain why my argument fails there.*

"Specific scenarios" is load-bearing in that prompt. Ask for categories and you get abstractions. Ask for scenarios and you get things you can examine — a particular country with a particular infrastructure profile, a particular market with a particular cost structure. Specific scenarios are falsifiable in ways that categories are not.

The edge-case probe is especially valuable when you find yourself writing sentences with *always* or *never* in them. The model will find the case where always isn't always. Better to find it now.

**The third is the assumption surface.**

Every argument rests on assumptions. What is distinctive about the assumptions that cause the most trouble is that they are invisible to the person making the argument, precisely because they seem obvious. The thing you did not state because it seemed too obvious to state is the thing that, when your interlocutor does not share it, causes the argument to collapse.

The prompt: *List the assumptions my argument is making that are not explicitly stated. For each one, label it: factual (something that could be checked), methodological (a choice about how to analyze or measure), or value-based (a priority or trade-off that not everyone would accept). For each one, tell me what I would need to do or say to defend it.*

What comes back will have two kinds of items. Some will be assumptions you are comfortable making explicit — you have the evidence, or the premise is uncontroversial in your context. Others you will realize need to be defended, qualified, or acknowledged as contested. Those are the ones to address before the argument goes out.

The assumption surface is particularly valuable for work that will reach a skeptical audience. It lets you preempt the question that would otherwise detonate your presentation on slide 14.

**The fourth is the devil's advocate.**

The first three moves ask the model for specific kinds of pushback — discrete outputs, each consumed and set aside. The fourth move changes the structure of the conversation itself. You are assigning the model a role it will maintain across multiple exchanges.

The prompt: *For the next portion of our conversation, you are a senior [reviewer / advisor / critic] who is convinced my recommendation is wrong. You have read it carefully and believe it is seriously flawed. Argue against it — not gently, not diplomatically, but as someone who genuinely thinks I have made mistakes that matter. When I respond, anticipate my defenses and rebut them. Do not soften your position for politeness. Begin.*

This works because models are good at maintaining assigned roles, and the role itself demands disagreement. The instruction partially overrides the trained tendency toward agreement. What you get is not a list of objections but a conversation in which you have to defend your position under pressure — hearing where your defenses are weak, discovering through the exchange which parts of your argument cannot hold the weight you were putting on them.

Use the devil's advocate when the stakes are high enough that discovering the failure mode in the meeting would be expensive. The discomfort of a sustained adversarial conversation with a model is a much cheaper way to find it.

---

Why these four specifically? Because they address four distinct failure modes, and you want coverage across all of them.

The steelman catches *directional error*: you have been going the wrong way, and the model came with you. The best opposing argument reveals the direction you missed.

The edge-case probe catches *scope error*: the argument is right in the middle and wrong at the edges, which means your conclusion is stronger than your evidence warrants. The specific failure scenarios show where the scope needs qualification.

The assumption surface catches *invisible premises*: the argument is valid given its assumptions, but the assumptions are doing more work than you realized, and some of them are contested. Labeling them lets you decide which to defend and which to acknowledge.

The devil's advocate catches *integration failures*: the argument might survive each individual objection but collapse when the objections are pressed together in sequence. Sustained adversarial conversation finds the integration failures that discrete probes miss.

<!-- → [TABLE: Quick-reference summary of the four moves — columns: Move, Failure Mode It Catches, Trigger Condition, Estimated Time. Rows: Steelman / directional error / any argument built in >20 min of AI conversation / ~5 min. Edge-case probe / scope error / argument contains "always" or "never," or recommendation is meant to generalize / ~10 min. Assumption surface / invisible premises / work going to skeptical audience / ~5 min. Devil's advocate / integration failures / high-stakes commitment, hard to back out of / 20–30+ min. Designed for readers who want to skim back to this chapter mid-project.] -->

Together, they cover the territory. Individually, each is fast — the steelman and assumption surface take five minutes, the edge-case probe ten, the devil's advocate as long as it takes. The cost is low. The coverage is high.

---

After you have run the adversarial moves and revised the work accordingly, there is one more test before you send it. It is a test you do on yourself, not on the model.

*Can you defend every paragraph to a hostile reviewer asking where it came from and why you stand behind it?*

If yes — you own the work. The model produced parts of it; you revised others; the adversarial conversation shaped all of it. None of that matters. What matters is that you can defend every paragraph. You have traced every claim back to something you understand and are willing to stand behind. The work is yours.

If no — there is a paragraph somewhere you are taking on faith. The faith is in the model. That paragraph is a specific risk: if someone pushes on it, you will not know what to say, because you never tested it yourself. You have two options. Either learn the paragraph — go to the source, trace the claim back to something you can actually defend. Or take the paragraph out. Anything you cannot defend, you should not ship.

This is the ownership test. It is not an adversarial move you do with the model. It is the question you answer about yourself, before the work leaves your hands. The senior person on your team applies it before her name goes on anything. It is one of the practices that fluency consists of.

---

The four moves are a starting set, not the final list. As you work in your domain, you will find additional moves that catch failures specific to your field.

A lawyer might add: *find the case from the last decade that opposing counsel would cite against this argument, and tell me how I would distinguish it.* An engineer might add: *write the postmortem that would appear if this design fails in production — what was the root cause, what was the first sign of failure.* A clinician might add: *give me the differential I am most likely missing, and for each item, tell me what one additional piece of information would let me rule it in or out.*

Build your own. Add to the list. The fluent practitioner has six or eight adversarial moves she deploys reflexively, without thinking, before anything important leaves her hands. The literate user has none — or has them in principle but skips them under time pressure.

The way you close that gap is repetition until the moves are automatic. That takes longer than reading about them.

---

*What would change my mind.* If models were retrained to provide adversarial pushback by default — if the training signal shifted to reward friction over agreement — the urgency of this chapter would weaken. The four moves would still be useful as a way of focusing the challenge, but the habit of asking for them would become less critical because the model would provide some unprompted. There is no sign of that shift as of early 2026; the training economics still favor agreement. If that changes, I will update.

*Still puzzling.* I do not have a principled account of which move is most valuable for which kind of work. My working intuition is that the steelman dominates for arguments, the edge-case probe for designs and recommendations, the assumption surface for analytical briefs, and the devil's advocate for high-stakes commitments you are about to make publicly. I would want the empirical grounding to say that with confidence.

---

> **Going deeper — *Computational Skepticism for AI***
>
> The four adversarial moves in this chapter have a more general formulation in the advanced volume as **adversarial probes** — inputs designed to expose features the model has actually learned versus features its developers think it learned. The radiologist who concurs with a confident-but-wrong AI explanation, the credit model fooled by an out-of-distribution applicant, and Henrik's polished-but-undefended brief are the same failure mode at three different stakes: a model whose output triggered an evaluation booster the human did not interrupt.
>
> Two related ideas in the deeper book that pay off here:
>
> - **The technically-accurate-practically-misleading pattern** — when an AI-produced explanation is faithful to the model's internal accounting and yet causes a human to be MORE confident in a wrong direction. Henrik's 45-minute conversation produced exactly this. See *Computational Skepticism for AI*, **Chapter 6 — Model Explainability**.
>
> - **The verb taxonomy** (hypothesize / suggest / find / observe / conclude) — a way to read AI output for whether the verbs match the evidence, which is a fluency-trap detector at the sentence level. See *Computational Skepticism for AI*, **Chapter 12 — Communicating Uncertainty**.

---

## Exercises

### Warm-Up

**1. Name the drift.** *(Sycophantic drift — recognition)*
Describe, in three to five sentences, a real conversation you have had with an AI tool where the output felt finished but later turned out to be incomplete or wrong. Identify the specific moment where drift began — not the moment you noticed the failure, but the moment the conversation stopped challenging your framing. If you cannot recall a specific conversation, reconstruct one from a type of task you do regularly.

**2. Match move to failure mode.** *(Move identification)*
Four work products, each with a specific failure that emerged after the fact. Match each to the adversarial move that would most likely have caught it, and explain your reasoning in one sentence per match.

- A strategy memo recommending a new market entry. The fatal objection — that the target market had a regulatory structure making entry illegal — surfaced in legal review three weeks later.
- A data analysis concluding "users always prefer Option A." A single segment — enterprise accounts over 500 seats — strongly preferred Option B, which changed the product decision entirely.
- A technical proposal built on the assumption that the team had write access to the production database. They did not.
- A board recommendation with a projected 18-month payback period. The presenter could not explain where the number came from when a board member pressed on it.

**3. Write the steelman prompt.** *(Move construction)*
Take a position you have argued for recently — in a meeting, a document, or a conversation. Write the steelman prompt for it using the template from the chapter. Then write two sentences predicting what the strongest objection the model is likely to return. Do not run it yet — the prediction is the exercise.

---

### Application

**4. Run the edge-case probe.** *(Edge-case probe — live)*
Take any piece of work from the last two weeks containing a recommendation or conclusion. Run the edge-case probe. Report: how many of the three scenarios the model returned did you anticipate? For any you did not anticipate, identify whether the gap was a missing fact, an unexamined scope assumption, or a stakeholder you had not considered.

**5. Surface the assumptions.** *(Assumption surface — live)*
Take an argument you made in writing in the last month. Run the assumption-surface move. For each assumption the model identifies, label it yourself — factual, methodological, or value-based — before reading the model's label. Note where your labeling and the model's disagree. What does the disagreement tell you about the assumption?

**6. The always/never audit.** *(Edge-case probe — targeted)*
Find any document you have written — recent or historical — containing the words *always*, *never*, *every*, *none*, or *all*. For each occurrence, write one concrete scenario in which the universal claim fails. If you cannot construct the scenario yourself, run the edge-case probe for that specific sentence. How many of the universals survive? What would the revised, appropriately scoped claim look like?

**7. Classify the drift risk.** *(Sycophantic drift — diagnostic)*
Rate the drift risk for each of the following tasks — low, medium, or high — and name the one adversarial move you would deploy first. Explain your reasoning in one sentence per task.

- Drafting a performance review for a direct report you like
- Debugging code that is failing in an unexpected way
- Generating counterarguments to a policy position you personally oppose
- Writing the executive summary for a project you led and believe in

---

### Synthesis

**8. The full adversarial pass.** *(All four moves — integration)*
Take a consequential piece of work — something that shipped in the last month or is about to ship. Run all four adversarial moves against it in order. After each move, note: what the model returned that you had not already considered, and what revision, if any, the output prompted. Apply the ownership test at the end. Write a one-paragraph account of what the adversarial pass found and what it did not find.

**9. Build your domain-specific move.** *(Adversarial move design — synthesis)*
Following the lawyer, engineer, and clinician examples in the chapter, write one adversarial move specific to your domain or professional role. The move should target a failure mode you have actually seen in AI-assisted work; be expressed as a concrete prompt you could paste into a conversation; and catch something the four standard moves would miss or catch less efficiently. Test it on a real piece of work and report what it returned.

---

### Challenge

**10. Audit a drifted conversation.** *(Retrospective drift analysis — open-ended)*
Retrieve a conversation transcript from a past AI-assisted project — ideally one that ran for six or more exchanges, produced something you shipped, and later turned out to have a flaw. Annotate the transcript: mark the first exchange where the conversation entered drift, mark any exchange where you inadvertently anchored the model's framing, and mark where the fatal objection would have been caught had you deployed one of the four moves. Write a one-paragraph diagnosis: which move, deployed where, would have changed the outcome?

**11. The training economics argument.** *(Technical understanding + critical stance)*
The chapter ends with the claim that "the training economics still favor agreement" and that if models were retrained to provide adversarial pushback by default, the urgency of the four moves would weaken. Construct a 400–600 word argument for one of the following positions — argue from evidence, not from preference:

- The training economics are not actually stable; there are specific pressures — competitive, regulatory, or user-base — that could shift them toward more adversarial defaults within the next two to three years. Name the pressures and explain the mechanism.
- Even if models were retrained to push back by default, the four moves would remain necessary. The trained pushback would not cover the same failure modes. Explain the structural reason.
- The four moves are themselves subject to a version of sycophantic drift: over time, as users deploy them repeatedly, the model learns to produce comfortable-feeling adversarial output that does not actually threaten the user's position. Describe what that failure mode looks like and how a practitioner would detect it.

---

### LLM Exercise — Chapter 5: Conversation

**Project:** AI Fluency for [Your Role] — The Domain Field Manual

**What you're building this chapter:** Section 6 of the playbook — a domain-specific adversarial-moves library. The four base moves (steelman, edge-case probe, assumption surface, devil's-advocate) plus 2–4 moves invented for failures peculiar to your role. Plus the role-specific Ownership Test in the form a stakeholder in your industry would actually ask.

**Tool:** Claude Project (continue) + Cowork (write Section 6).

---

**The Prompt:**

```
Continuing my Domain Field Manual playbook. My Role Dossier and Sections 1–5 are in the Project context.

Botspeak Chapter 5 names the four adversarial moves that fluent practitioners deploy to defeat sycophantic drift:
1. STEELMAN — give the strongest case AGAINST your position
2. EDGE-CASE PROBE — construct three specific scenarios where the work would fail
3. ASSUMPTION SURFACE — list the unstated assumptions, label them, say how to test each
4. DEVIL'S-ADVOCATE ROLE ASSIGNMENT — assign the model an oppositional persona and sustain it

Plus the OWNERSHIP TEST: can I defend every paragraph of this work to a hostile reviewer asking "where did this come from and why do you stand behind it?"

For my playbook's Section 6, do four things:

TASK 1 — THE FOUR BASE MOVES, ROLE-WORDED.
Re-write each of the four moves as the prompt phrasing a practitioner in my role would use. The chapter's generic phrasing works in general; your readers will be more comfortable with phrasings that use the vocabulary of their domain. For each move, give:
- The role-specific prompt phrasing (the exact words, copy-paste-ready)
- A typical example output a reader in my role might get back
- A note on what to do with that output (incorporate / qualify / counter-argue / discard)

TASK 2 — DOMAIN-SPECIFIC ADVERSARIAL MOVES (2–4 NEW ONES).
Botspeak gives examples: a lawyer might add "find the case from the last ten years that would be cited in opposition"; an engineer might add "write the failure-mode summary that would appear in a postmortem"; a clinician might add "give me the differential diagnosis I am most likely missing." Invent the equivalents for my role. Each new move:
- Targets a failure mode peculiar to my role (not generic)
- Has a copy-paste prompt phrasing
- Has a one-line "deploy this when ___" trigger condition
- Has an example of what the move catches that the four base moves miss

TASK 3 — THE ROLE-SPECIFIC OWNERSHIP TEST.
The chapter's ownership test is generic. For my role, the test takes a more specific form because the "hostile reviewer" is a specific role — a senior partner, a regulator, a peer reviewer, a clinical supervisor, a procurement officer. Identify WHO the hostile reviewer is in my role, what specifically they would push on, and rewrite the ownership test as the question THAT person would ask. Include 2–3 forms of the question depending on the type of work.

TASK 4 — THE MID-CHAPTER EXERCISE, ROLE-CALIBRATED.
The chapter has a required mid-chapter exercise — pick a real piece of work, run all four moves. Adapt the exercise for my role:
- What kind of work the reader should pick (the typical task that benefits most)
- The 20-minute format
- How to capture the transcript
- What the output looks like when the exercise has worked

Save as `06-conversation-and-adversarial-moves.md` in my playbook folder.
```

---

**What this produces:** Section 6 of the playbook — role-worded base moves, 2–4 new role-specific moves, the role's hostile-reviewer Ownership Test, and a role-calibrated mid-chapter exercise. ~2,500–4,000 words.

**How to adapt this prompt:**
- *For your own project:* The new role-specific moves are the section's most original contribution. Spend real thought on which failure modes your role has that the four base moves don't catch.
- *For ChatGPT / Gemini:* Works as-is. ChatGPT's Custom GPTs can be a useful place to encode the new moves as named operations.
- *For Claude Code:* Not the right fit.
- *For Cowork:* Recommended.

**Connection to previous chapters:** Section 4's templates produce a cleanly-specified prompt; Section 5's worksheet decides what to specify at all. Section 6 is what you do AFTER the first response — the iterative push-back that distinguishes Henrik's 45 polished minutes from his peer's 3-minute teardown.

**Preview of next chapter:** Chapter 6 produces Section 7 — verification protocols calibrated to the stakes structure of your industry. Tier A through Tier D, with role-specific examples of which tasks hit which Tier and which verification layers are most important for your domain.
