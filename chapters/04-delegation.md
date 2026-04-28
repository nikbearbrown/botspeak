# Chapter 4 — Delegation
*What to Give the AI, What to Keep, and Why the Difference Matters*

*The tool doesn't take the skill from you. You hand it over voluntarily, in small increments, each of which makes complete sense in the moment.*

---

Here is a strange thing that happens with tools.

When you first get a good one, you use it for everything. A sharp knife, you cut bread with it, open packages with it, scrape the cutting board. A new phone, you use it to read, to navigate, to play music in the shower. The tool is interesting and the novelty of it makes you reach for it past the point where reaching makes sense. That is fine. That is how you learn what the tool actually does.

But then something subtler happens, and this is the part worth paying attention to. You stop doing some things *by hand* that you used to do by hand. Not because the tool does them better — though it often does — but because the tool is *there*, and using it feels like the obviously correct move, and doing it by hand starts to feel like a waste. The navigation app is open, so you follow it even on a route you've driven a hundred times. The synthesis tool is running, so you let it pull the sources even when you know this territory cold.

The tool doesn't take the skill from you. You hand it over voluntarily, in small increments, each of which makes complete sense in the moment.

---

There's a name for this in cognitive psychology: *cognitive offloading*. You move mental work from your head to a system outside your head. Scratch paper is cognitive offloading. A to-do list is cognitive offloading. A calculator is cognitive offloading. None of these are inherently bad. In fact, they are mostly good — they extend what you can do, free working memory for harder problems, and let you take on work that would otherwise exceed your capacity.

AI tools are cognitive offloading on a scale that is qualitatively different from anything before. A calculator offloads arithmetic. An AI research-synthesis tool offloads source-gathering, reading, pattern-recognition across dozens of documents, summarizing, and the initial structuring of an argument. That is not a bigger calculator. That is a different kind of thing.

And so the question you have to ask — which nobody was asking about scratch paper — is this: *what capacity does this offloading build in me, and what does it erode?*

Some cognitive offloading *amplifies* you. You use the tool, and in the process of working with its output, your judgment gets more reps, not fewer. A senior analyst who delegates source-gathering to an AI tool but does her own pattern-recognition and synthesis is getting stronger, not weaker. She is doing more analysis at higher quality, and the analytical muscle is being exercised through the work.

Other cognitive offloading *atrophies* you. You hand off something that was, until now, teaching you. The output is fine. The work gets done. But the feedback loop that was building your skill is gone, and three months later you know less than you would have if you had kept doing it by hand — not because the AI failed, but because it succeeded too completely.

The hard thing is that you cannot feel this happening. Each individual case looks correct. The synthesis tool ran, the output is good, you shipped it. That is not a mistake. It looks like efficiency. It *is* efficiency. And then, six months later, a CFO asks you about a trade-press story you didn't catch, and you realize you stopped reading trade press when the synthesis tool started doing it for you, and the synthesis tool sources from major outlets, not the trades, and now you are standing in a client meeting with a hole in your analysis where your domain intuition used to be.

This is what I mean when I call it the *performance paradox*. Your daily output got faster and more polished. Your judgment — the thing the senior people on your team have, the thing the client pays for — got quieter without your noticing.

---

The paradox is not new. Pilots who fly on autopilot for every flight produce aviators who are excellent at managing the autopilot and have degraded manual flying skills — which is the skill they need precisely on the day the autopilot fails. Radiologists who use AI screening tools for every routine case produce, on the rare complex case, slower and worse calls than the colleague who never adopted the tool. The phenomenon is general. The interesting question is not whether it happens. It is which skills erode and how fast.

There is a rough heuristic I find useful. Ask yourself: *if I hand this task to an AI for six months, what skill of mine will weaken, and is that skill one I will need exactly on the day the AI fails?*

If the answer is "a skill I won't miss" — a task that was mechanical, high-volume, low-judgment — delegate freely and don't look back. Reformatting data. Converting file formats. Spell-checking. These tasks do not build judgment you would ever miss. Outsource them completely.

If the answer is "a skill I'll need precisely when something goes wrong" — and wrong means missing the Sysco pilot, wrong means the client asking a question you can't answer, wrong means the edge case the model doesn't know to flag — then you have a choice to make consciously. You can still delegate. But you need to build the practice in by other means. The surgeon who uses robotic tools still practices on the simulator. The navigator who relies on GPS still runs chart exercises. You keep the skill alive artificially, because the natural opportunity to practice it has been removed by the tool.

---

Let me be more precise about this, because the intuition about "mechanical versus judgment" can mislead you if you don't push on it.

There is a spectrum. At one end: tasks where the right answer is fully determined, the model will get it right reliably, and doing it yourself would not teach you anything you don't already know. These are genuinely mechanical. Delegate them.

Move along the spectrum and you get to tasks where the right answer is well-defined but *recognizing wrong answers* requires domain knowledge you have. The model generates a draft; you check it. The model suggests category labels; you verify them. Here the skill you are practicing is *the check* — the evaluative judgment that distinguishes correct from close-but-wrong. That skill is worth keeping. Delegate the generation; keep the evaluation.

A little further and you're in synthesis territory. The model is gathering and combining information from multiple sources and producing a unified output. This is Nora's territory. Two risks live here that don't live at the mechanical end. First, the sources might contain errors the model won't catch because it doesn't know what you know about this specific client, this specific moment, these specific operating conditions. Second — and this is the Sysco problem — *the omissions are often where the insight lives*. A synthesis tool tells you what the sources say. It cannot tell you what the sources don't say. The practitioner who knows the domain can smell the absence. The practitioner who has been delegating synthesis for six months has lost that smell.

Go further still and you reach what I'd call contestable analysis: problems where reasonable practitioners would genuinely disagree about the answer. Strategic recommendations. Investment theses on non-consensus positions. Diagnostic calls in ambiguous cases. Models produce confident output here with no reliable signal about where the confidence is warranted and where it is guesswork dressed as synthesis. A model asked "should our client enter this market" will not answer "I don't know." It will reason its way to a position. The position may be excellent or terrible, and the model cannot tell the difference. You have to. Which means you have to keep the analytical work here even if you use the model to assemble components of it.

And at the far end of the spectrum: decisions where, if they go wrong, a human has to answer for them. Hiring. Firing. Safety. Care decisions. These are not analyzable into components where the model takes some and you take others. The accountability is whole and cannot be distributed. You can use the model to inform the decision. The decision belongs to you.

<!-- → [INFOGRAPHIC: The delegation spectrum as a horizontal gradient — seven labeled regions from left (Mechanical Execution) to right (Accountable Judgment), with a color shift from green to amber to red indicating increasing practitioner ownership required; each region shows a one-line delegation rule and a one-line example task; student should see that delegation is not binary but a continuous judgment call] -->

---

You can think of these as tiers. Not because the world divides cleanly — it doesn't — but because having a name for each region helps you locate yourself when you're deciding what to hand off.

Tier one is mechanical execution: fully determined, model reliably correct, no judgment being built by doing it yourself. Delegate freely.

Tier two is pattern-matching with feedback: right answer is defined, but you need to check. Keep the check.

Tier three is synthesis from sources: model gathers and combines, you evaluate. The danger is the Nora trap — stay alert to what the synthesis is not telling you, not just what it is.

Tier four is drafting in your voice: the model produces, you revise. Real risk here is long-term voice drift — your writing migrates toward the model's defaults over months. Keep some work done without the model just to keep your own register alive.

Tier five is judgment under structure: you author the framework, the model applies it. Delegate the application; keep the authorship.

Tier six is contestable analysis. Don't delegate the call. You can delegate the inputs.

Tier seven is accountable judgment. The model can inform it. You own it entirely.

A delegation map for any non-trivial task is: decompose it, locate each component on the tiers, hand over the bottom, partner on the middle, keep the top. The map is something you can defend. It is the artifact that proves you thought about what you were doing.

<!-- → [TABLE: The seven delegation tiers — columns: Tier, Name, Delegation rule, Example task, Skill-atrophy risk (Low / Medium / High); student should be able to use this as a quick reference when building a delegation map for a real task] -->

---

In practice, four questions get you to the map quickly. You can run them in two minutes before any consequential delegation.

*What capacity does this task build, and do I need to keep building it?* This is the Nora question, asked in advance. If the task has been building one of your skills, delegating it stops the building. That might be fine. It might not. Decide consciously.

*What is the blast radius if the AI gets this wrong?* A misformatted table is one blast radius. An error in a strategic recommendation is another. A wrong medical call is a third. Match your verification effort to the blast radius. At high blast radius, the verification is more important than the generation.

*Who is accountable if this is wrong, and does that person know how it was produced?* If your name is on the work, your accountability is on the work. The threshold for disclosure is lower than most practitioners currently assume. If a stakeholder would feel deceived to learn the work was AI-assisted, that is information you need to act on before the work ships, not after.

*What does the model not know that I do, and have I made sure that part stays in?* The model has broad reading and no domain intuition specific to this client, this moment, these relationships. If you are not actively folding in what you know that the model cannot, the output will be polished and missing the thing a senior practitioner would catch. The Sysco pilot is always somewhere in the analysis.

Four questions. Run them. After you have run them a few hundred times they will be reflex, and you will have them before you open the tool rather than after you have already shipped.

---

Here is something true about the fluent practitioner that is easy to underestimate. She is not faster than the literate user because she uses the tool more aggressively. She is faster *and more reliable* because she knows exactly which parts of the work she is handing off and which parts she is keeping — and she has kept alive the judgment that makes the output trustworthy.

The literate user thinks about the tool. The fluent practitioner thinks about the work. The tool is somewhere in the background, doing the parts the tool should do, while the practitioner is doing the parts that are actually hard and actually hers.

Nora got faster. Her work looked better. The forty-page analysis was, in fact, the best-organized work she had produced on a tight timeline. And standing in front of the CFO, the thing she learned was that best-organized is not the same as right, and that the senior consultant she was becoming before the tool is not the same as the consultant she was becoming with it.

The lesson is not to use the tool less. The lesson is to use it with clear eyes about what the bargain is.

---

*Next chapter: The first prompt rarely produces what you want. Even with a clean specification and a deliberate delegation map, there is a gap between what you asked for and what you need — and closing that gap is a skill. Chapter 5 is about that conversation: the four adversarial moves that separate a fluent practitioner's iterative refinement from a literate user's one-shot hope.*

---

**What would change my mind.** If longitudinal evidence showed that aggressive delegation at the contestable-analysis tier does not degrade practitioner judgment over time — that the model catches what the practitioner would have caught, and sometimes more — the keep-the-skill argument here is weaker. The radiologist evidence, and the pattern behind Nora's story, suggests otherwise. I would update on counter-evidence.

**Still puzzling.** I do not have a sharp answer to how long atrophy takes for a given skill. Six months was clearly enough in Nora's case. Some skills probably go faster; some take years. That time-constant matters enormously for how carefully you need to manage the practice-by-other-means requirement, and it is not yet well-characterized empirically.

---

## Exercises

### Warm-up

**1. Tier identification.** For each task below, name the delegation tier and write one sentence explaining your reasoning. *(Tests: ability to locate tasks on the seven-tier framework.)*

- An analyst asks an AI to reformat a data table from wide to long format for a statistical analysis.
- A consultant asks an AI to synthesize analyst reports on a target company's competitive position ahead of a client meeting.
- A hiring manager asks an AI to recommend which of three finalists to hire based on interview notes.
- A writer asks an AI to generate a first draft of a strategy memo, which she then revises heavily.

**2. The paradox in plain language.** Explain the performance paradox — in two to three sentences, without using the word "paradox" — to a colleague who is proud that her team's output quality has measurably improved since adopting AI tools six months ago. Your explanation should not be dismissive of the improvement. It should name what is true about the improvement and what might also be true alongside it. *(Tests: retention of the performance paradox concept and ability to hold both sides of it.)*

**3. The four questions, applied.** A research associate is about to delegate the following task: *summarize the last twelve months of earnings calls for three public competitors and identify recurring themes in management's forward guidance.* Run the four pre-delegation questions on this task. For each question, write two to three sentences — not just the question restated, but your actual answer for this specific task. *(Tests: mechanical application of the four-question framework before it becomes reflex.)*

---

### Application

**4. Build a delegation map.** A strategy consultant is preparing a market-entry recommendation for a client considering expansion into Southeast Asia. The work involves: gathering macro data on five target markets, synthesizing analyst and trade-press coverage, identifying regulatory barriers, structuring the recommendation framework, drafting the written analysis, and making the final go/no-go call for the presentation. Decompose this work into its components, locate each on the seven tiers, and produce a delegation map that specifies what gets handed to the AI, what gets partnered, and what the consultant keeps. Defend each call in one sentence. *(Tests: ability to apply tier logic to a multi-component real task.)*

**5. Diagnose the atrophy.** Nora's failure was not visible in her daily output — it appeared only when a CFO asked a question the synthesis tool had no reason to surface. Describe a plausible scenario in a different domain (medicine, law, engineering, journalism — your choice) where the same structure plays out: a practitioner whose output quality improved after adopting an AI tool, but whose judgment degraded in a way that only became visible under a specific condition. Name the skill that atrophied, the condition that revealed it, and what the practitioner would have needed to do differently to prevent it. *(Tests: ability to generalize the Nora pattern beyond the case as given.)*

**6. The blast radius check.** You are reviewing a colleague's delegation decision before a deliverable ships. The colleague delegated the following to an AI and did not verify the output: a one-paragraph summary of a regulatory approval timeline for a pharmaceutical product, included in a board memo. Using the blast-radius question, explain specifically what the verification step should have been, what failure modes it would have caught, and what the consequence of skipping it could be. *(Tests: application of the blast-radius heuristic to a concrete high-stakes case.)*

---

### Synthesis

**7. Amplify vs. atrophy.** The chapter distinguishes cognitive offloading that amplifies you from cognitive offloading that atrophies you. Using the seven-tier framework, identify the structural feature that separates the two categories — what is it about the nature of a task that determines whether delegating it builds you or diminishes you? Your answer should be a clear, defensible claim in 150–200 words, not a restatement of the tiers. *(Tests: ability to extract the underlying principle from the framework rather than just apply it.)*

**8. The voice drift problem.** Tier four introduces voice drift as a distinct risk for practitioners who delegate drafting consistently. Explain why voice drift is a problem that does not appear in the other tiers — what is different about drafting in your voice, as opposed to synthesis or pattern-matching, that makes the atrophy risk specifically linguistic rather than analytical? Then propose a concrete practice — something a practitioner could do weekly in thirty minutes or less — that would keep the risk manageable without abandoning delegation. *(Tests: integration of the cognitive offloading argument with the specific character of Tier 4.)*

---

### Challenge

**9. The accountability edge case.** The chapter says accountable judgment "cannot be distributed" and the decision belongs to you entirely. But consider a practitioner who uses an AI to surface options, model scenarios, and pressure-test assumptions before making a hiring decision — then makes the call herself. Has she kept the accountability whole, or has she partially distributed it? Construct the strongest argument for each position, then say which you find more convincing and why. There is no clean answer; the goal is a rigorous argument that takes both sides seriously. *(Tests: ability to reason at the edges of the framework where it does not yield a clean answer.)*

**10. Design the counter-practice.** The chapter notes that practitioners who delegate skills they will need when the AI fails must "keep the skill alive artificially, because the natural opportunity to practice it has been removed by the tool." Choose a specific domain and a specific skill that AI tools are now commonly used to offload in that domain. Design a concrete counter-practice — structured, realistic, requiring no more than two hours per month — that would keep the skill genuinely maintained rather than just nominally practiced. Your design should name what the practice measures, how a practitioner would know if the skill is degrading, and what threshold would tell her the practice is no longer sufficient. *(Tests: synthesis of the keep-the-skill argument into actionable design — the Feynman test for whether you understood the problem well enough to solve it.)*
