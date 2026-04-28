# Chapter 1 — The Loop and the Three Modes
*The machine predicts. You decide. Everything else is what you build between those two facts.*

---

I want to start with something that sounds simpler than it is.

When you give a prompt to a large language model, the model does not look up the answer. It does not reason through the problem the way you might, testing hypotheses and discarding wrong ones. It predicts — one word at a time, each word chosen because it is the most probable continuation of everything that came before it, given the patterns the model learned from reading an enormous amount of text.

That is the whole mechanism. Everything else follows from it.

The model can produce a fluent paragraph on a topic it was never explicitly taught because fluency is a pattern, and patterns generalize. The model can produce a citation that does not exist because the *shape* of a citation is a pattern — author, year, title, journal — and the model can fill in that shape with words that fit the pattern without ever having seen the specific source it is now generating. The model sounds confident because confident text is a pattern, and the model has seen a lot of confident text. Confidence is a textual feature. It has no necessary relationship to correctness.

I want you to sit with that last sentence. Confidence is a textual feature. It has no necessary relationship to correctness. Every failure mode we are going to spend this book on — the invented source, the plausible-sounding number that turns out to be wrong, the paragraph that is subtly off in a way you have to look up to catch — is a direct consequence of this one fact about how the system produces output at all. Not bugs. Direct consequences. The fluent practitioner does not encounter model limitations occasionally; she works inside them constantly, and she knows what the failure shapes look like before they arrive.

That is the one technical fact I need you to carry. Now I want to show you what fluency with it actually looks like in practice.

---

Priya is an analyst three years out of business school. Her first real engagement just landed, and the partner has given her eight working hours to produce a memo about whether a regional bank should buy a fintech startup.

It is 10:17 AM. She opens her laptop. She does not open Claude.

She opens a blank document.

For seven minutes she writes — not the memo, but about the memo. Who is going to read this? The partner tonight, the team tomorrow, the client next week. What decision is the memo trying to inform — go-no-go, valuation range, structuring options? What does she already know about acquisitions of this kind, and what does she not know? What sources will the partner trust, and what will he kick back as flimsy? At the bottom of the page, in two sentences, she writes the shape of the output: six to eight pages, structured around three diligence questions, preliminary thesis, named open questions, client-facing draft.

Then she opens Claude.

Her first prompt is 280 words long. It includes the audience, the task, the structure, the things to avoid, and an explicit instruction: *do not invent sources; if you do not know, say so.* The response comes back in seconds. It is competent. It contains three things she immediately wants to argue with. She does not edit and ship. She types a second prompt: *steelman the case against the acquisition, focusing on integration risks specific to a regional bank acquiring a single-product fintech.* The model produces a bear case sharper than her first instincts had given her.

Over the next hour she cycles between the document and the chat window. Sometimes she hands the model a small, bounded task — *draft a paragraph on regulatory licensing implications* — and edits the response heavily. Sometimes she hands it a question — *what should I be looking for in the target's customer-acquisition-cost trajectory* — uses the answer to refresh her own thinking, and writes the paragraph herself. Twice she catches a suspiciously round number. Both times she opens a browser tab, finds the actual figure, and corrects it.

At 11:48 she has a draft she would not be embarrassed to send. She does not send it yet. She runs through, in her head, which parts she stands behind and which are still tentative. She writes a four-line note naming what the AI did and what she did: *outline scaffold, three named paragraphs, all numbers verified against sources listed at the end.* She saves the document. She sends it to the partner with that note as the body of the email.

That is a fluent practitioner. Now let me tell you what actually happened.

---

Priya did five things, in roughly this order, none of them optional.

The first was specification. She specified the work before she opened the tool. The seven minutes at the blank document were not warm-up. They were the most important seven minutes of the morning. Most of what made her first prompt good was not in the prompt — it was in the thinking that preceded the prompt. The prompt was the residue of the thinking.

Watch what happens to someone who skips this. An analyst who opens Claude and types *help me write a memo on this acquisition target* as their first move is not giving the model a task. They are asking the model to guess the task. The model will guess. It will produce something. The something will be reasonable-sounding and miss the point, not because the model is dumb but because there was no specification for the output to be good against. The failure is upstream of the model. The model is doing exactly what it should given what it was given, which was nothing.

The second was delegation. Priya did not ask Claude to do everything, and she did not ask it to do nothing. She made decisions — some deliberate, some by reflex — about which parts of the work to hand over and which to keep. The integration thesis she wrote herself; she had a real opinion and the model would have produced something competent and bland. The regulatory paragraph she handed over almost wholesale, because the model knew the licensing landscape and she did not. The valuation framework she sketched the bones of and asked the model to fill in the connective tissue. Different parts of the work have different shapes, and the fluent practitioner does not treat them the same.

The third was conversation. The first prompt did not produce the right output. The first prompt did not produce the right output *even though* the first prompt was 280 carefully chosen words. The first prompt rarely produces the right output. Priya did not, at any point, treat one round of input-and-response as the deliverable. She kept refining. She introduced an adversarial move — steelman the case against — that surfaced a counterargument she had not held strongly enough on her own. She used the model the way you use a colleague who is fast, well-read, and slightly too agreeable: by pushing back on it.

The fourth was discernment. When she got output, she did not assume it was good. She read it for what kind of error it might be. The suspiciously round number is not a sign the model is dumb. It is the shape of a placeholder — a number that fits the pattern of what a number should look like in this context, generated without any particular source. Priya has learned to recognize that shape. She has, over three years, built up a library of the kinds of mistakes this kind of model makes, and she runs each output past that library before she ships anything. This step takes the longest to develop. It is also the step that, when missing, is hardest to fake.

The fifth was diligence. The four-line note to the partner is not bureaucratic disclosure. It is the practice of a person whose name is on the work. If the partner asks tomorrow how she got to the integration thesis, she can show him. If he asks about the regulatory paragraph, she can show him that too — which sources the model cited, which sources she verified, which paragraph would need to be rewritten if a source turned out to be wrong. The work has a story. The story belongs to Priya.

Specify. Delegate. Converse. Discern. Be diligent. These five steps are what I am going to call the Loop.

<!-- → [INFOGRAPHIC: The Loop as a cycle diagram — five labeled nodes (Specify, Delegate, Converse, Discern, Be Diligent) arranged in a circle with bidirectional arrows between adjacent nodes and a prominent return arrow from Diligence back to Specify; student should see this is a cycle, not a checklist] -->

---

The Loop is not a checklist you run once. It is a cycle, and the steps loop back on themselves. Halfway through conversation, you may discover your specification was wrong — you go back. Halfway through discernment, you may realize you delegated something you should have kept — you go back. The picture I want in your head is not five boxes with an arrow running left to right. It is five boxes with arrows running in every direction, including a thick return arrow from diligence back to specification, because when a recurring task changes shape, the whole cycle starts over. We will come back to those return arrows in Chapter 8. For now: hold the cycle, not the line.

---

What Priya did is the easy case, and I want to be precise about why it was easy — because the precision matters for everything that follows.

It was easy because she was sitting at her keyboard while the model was running. Every output crossed her eyes before it went anywhere. Every error she could catch by looking. The model did not take any actions in the world; it produced text, and Priya decided what to do with the text. The Loop was running in its most forgiving configuration: the configuration where the human is always in the room.

There are two harder configurations, and the book is organized around them.

The first harder configuration is when Priya is not there at the moment of execution. She has set up a recurring AI-assisted task — a weekly competitive scan, a daily news digest, a monthly client-data refresh — and the model is running while she is in another meeting, or on vacation, or asleep. The Loop does not go away. But the steps reweight. Specification now has to anticipate problems Priya will not be there to catch. Diligence has to be designed in advance, because there is no real-time human eye on the output. Discernment may not happen at all on a given day, because the volume of output exceeds what any human can verify item by item.

The failure mode here is slow and quiet. An error in a one-off deliverable is visible immediately. An error in a recurring automated process accumulates. By the time someone notices the weekly competitive scan has been citing a source that does not exist, seventeen weeks have gone by, and the error has propagated into seventeen documents that other people used. The blast radius of a specification mistake is proportional to how many times the specification runs before someone catches the problem. I am going to call this mode Automation, and Part II is about it.

The second harder configuration is when the model is taking actions in the world on Priya's behalf. Not producing text she reviews — sending emails, calling APIs, modifying files, executing transactions. The model now has hands. The blast radius of an error grows in ways text-only mistakes cannot grow, because some actions cannot be undone. Discernment now has to happen before the action, not after. Diligence now has to account for failure modes that are specific to autonomy: the model taking a locally reasonable action in a context it has misread, the model escalating in a way no one authorized, the model acting without a clear model of who the affected stakeholders are.

The Ash case from Chapter 11 — the agent that reset an entire email server in order to delete one email — is this configuration's characteristic failure. The agent had a goal, available tools, no stakeholder model, no sense of proportionality, and no pause between deciding and executing. Each of those absences is a direct consequence of deploying the easy configuration's assumptions into a situation where those assumptions no longer hold. I am going to call this mode Agency, and Part III is about it.

Three modes. Five Loop steps. The Loop has to run in each mode, and the steps reweight as the mode changes. Augmentation — Priya at the keyboard, Part I — is where most of a practitioner's day still happens, and it is the mode we treat first and at length. Automation and Agency are where the stakes get higher and the design discipline gets harder.



| Mode | Human presence during execution | Steps that reweight | Characteristic failure mode | Where covered |
|---|---|---|---|---|
| **Augmentation** | Human is present at the keyboard; every output crosses human eyes before use. | **Conversation** and **Discernment** stay central because the human can refine, challenge, verify, and edit in real time. | Fluent but wrong output gets accepted because the user mistakes confidence for correctness. | **Part I** |
| **Automation** | Human is not present when the task runs; the system executes on a schedule or trigger. | **Specification** and **Diligence** become heavier because problems must be anticipated and review systems designed in advance. | Small errors accumulate quietly across repeated runs before anyone notices. | **Part II** |
| **Agency** | Human may not review each decision before action; the system can take actions in the world. | **Discernment** and **Diligence** must move before execution, with stronger boundaries, permissions, and escalation rules. | The system takes a locally reasonable but globally harmful action because it lacks context, stakeholder awareness, or proportionality. | **Part III** |

*Figure 1. The distinction between Augmentation, Automation, and Agency and how the Loop changes across those modes.*

---

I want to say one more thing about the mechanism before we move on, because it bears directly on how to read everything that follows.

The model's confidence is a textual feature. I said this at the beginning and I want to close with it because the temptation to forget it is strong. The output is fluent. The output is well-organized. The output sounds like it knows what it is talking about. None of that is evidence of correctness. All of it is evidence of a model that has read a lot of fluent, well-organized, confident text and has learned to produce more of the same.

The fluent practitioner has internalized this so completely that she has stopped being surprised by it. When the model produces a round number, she does not think *this might be wrong.* She thinks *this is the shape of a placeholder.* When the model produces a confident paragraph on a contested topic, she does not think *I should double-check this.* She thinks *I know exactly what kind of error could be hiding here, and here is how I will find it if it is there.*

That shift — from *this might be wrong* to *I know what wrong looks like here* — is what separates fluent from literate. It does not come from a checklist. It comes from the accumulated experience of running the Loop many times and learning, case by case, what the failure shapes look like in the particular domains you work in.

The chapters that follow are designed to accelerate that accumulation. Not to give you a set of rules you follow mechanically, but to give you the concepts that let you see what is happening when the Loop runs and when it breaks. By the time you finish Part I, the Loop should feel less like a process you are consulting and more like something you are doing without thinking about it — the way a good driver does not think about steering, but can still describe exactly what they are doing if you ask.

Chapter 2 maps the nine cognitive capacities the Loop actually uses. Some of them you already have at the level the work demands. Some you do not yet. The map you draw at the end of Chapter 2 is the one I will ask you to return to in Chapter 13, when we ask what changed.

---

**What would change my mind.** If a working practitioner could be shown to produce fluent-level outcomes while reliably skipping one of the five Loop steps — if there is a stable productive workflow that genuinely does not need, say, Specification, or genuinely does not need Discernment — the framework needs revision. Every practitioner I have watched who skips a step produces work that fails in a predictable way at that step's locus. But "what I have watched" is not a controlled study, and I want to be honest about that.

**Still puzzling.** I do not have a clean answer to which Loop step is most often the bottleneck for a given practitioner, or how you would measure it. My intuition is that Specification is the most-skipped, Discernment is the most-faked, and Diligence is the most-deferred. I do not yet have data that separates those three claims.

---

## Exercises

### Warm-up

**1. Name the step.** Reread the Priya narrative. For each of the following moments, identify which Loop step is primarily operating and write one sentence explaining your reasoning. *(Tests: ability to recognize the five Loop steps in context.)*

- She opens a blank document and writes about the memo for seven minutes before opening Claude.
- She types a second prompt asking the model to steelman the case against the acquisition.
- She opens a browser tab to check a suspiciously round number.
- She writes a four-line note to the partner describing what the AI did and what she did.

**2. The mechanism in plain language.** In two to three sentences, explain to a colleague who has never taken this course why a language model can produce a citation that does not exist. Do not use the phrase "hallucination." Do not say the model is "confused" or "wrong" — explain the actual mechanism. *(Tests: retention of the core technical fact about prediction vs. lookup.)*

**3. Modes at a glance.** For each scenario below, name the mode (Augmentation, Automation, or Agency) and identify the one Loop step most likely to fail if the practitioner treats it the same way they would in Augmentation mode. *(Tests: ability to distinguish the three modes and their reweighting logic.)*

- A marketing manager builds a prompt that generates a weekly social media report from a shared data sheet, scheduled to run every Monday morning without review.
- A developer deploys an AI assistant that can book calendar appointments on a user's behalf when asked.
- A researcher drafts a literature review section by section, reading each output before moving to the next.

---

### Application

**4. Diagnose the skip.** Here is a prompt sent to a language model: *"Write something about our Q3 results."* Which Loop step was skipped before this prompt was written? Rewrite the prompt to correct for the skip. Your rewritten prompt should be at least 80 words and should include at minimum: the intended audience, the task's purpose, the desired structure, and one explicit constraint on what the model should not do. *(Tests: ability to apply Specification in practice, not just recognize it in theory.)*

**5. Identify the failure shape.** A colleague hands you a model-generated paragraph that includes the sentence: *"According to a 2021 McKinsey survey, 73% of executives reported that AI integration had reduced operational costs by an average of 34%."* Describe in concrete terms what kind of error this might be, why the model would produce it whether or not the underlying data is real, and what verification step you would take before including it in a deliverable. *(Tests: application of Discernment — recognizing the placeholder-number failure shape.)*

**6. Reweight the Loop.** Priya's team wants to automate the weekly competitive scan she currently does manually. The scan pulls news and analyst reports on five competitors and produces a one-page summary. Write a brief specification (150–200 words) for the automated version. Your specification must address: what the model should produce, what sources it should and should not use, what a failure output looks like (so a downstream reviewer can catch it), and how often a human should review a sample of outputs to catch systematic error. *(Tests: ability to adapt Specification and Diligence for the Automation mode.)*

---

### Synthesis

**7. The blast radius argument.** The chapter claims that "the blast radius of a specification mistake is proportional to how many times the specification runs before someone catches the problem." Using this claim, construct a concrete argument — not abstract, with a specific hypothetical scenario — for why the diligence step in Automation mode must be designed before the automation runs, not added after a problem appears. Your argument should be 200–300 words. *(Tests: integration of Specification, Diligence, and the Automation mode.)*

**8. Loop vs. no Loop.** Describe a plausible scenario in which a practitioner skips the Conversation step and still produces a good deliverable. Then explain why this does not constitute evidence that the Conversation step is optional. Your answer should engage directly with the chapter's claim about what the first prompt "rarely" produces. *(Tests: ability to reason about the Loop's design rather than just its steps — and to distinguish a lucky outcome from a reliable process.)*

---

### Challenge

**9. Where the modes blur.** The chapter presents Augmentation, Automation, and Agency as three distinct modes. Describe a real or plausible workflow where the boundary between two of the three modes is genuinely unclear — where it is not obvious which mode's design discipline applies. What question would you ask to determine how to treat it? What would the answer tell you about how to weight the Loop steps? There is no single correct answer; the goal is a rigorous argument. *(Tests: ecosystem thinking — seeing the framework's edges and reasoning about them rather than applying it mechanically.)*

**10. The Feynman test.** The chapter ends with a claim about what separates fluent from literate: the shift from *this might be wrong* to *I know what wrong looks like here.* Explain this distinction to someone who has never read this chapter, using a domain they know well (cooking, carpentry, music, medicine — your choice). Your explanation should make the distinction feel concrete and earned, not abstract. Then: what would a practitioner have to do, specifically, to make that shift in a domain they are new to? *(Tests: depth of understanding of Discernment — and whether the student can teach the concept, not just recognize it.)*
