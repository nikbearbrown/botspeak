# Chapter 8 — Putting the Loop Together

*A Real Task, Five Steps, Cycled to Done*

---

There is something you cannot learn from a list of steps.

You can read a recipe and understand, individually, what each instruction means. Dice the onion. Reduce the heat. Deglaze with wine. Each step is comprehensible. What the recipe cannot tell you — what no recipe can tell you — is what it actually feels like to cook. The moment where you realize the onion went in too early. The adjustment you make halfway through because the pan is running hot. The part where the whole thing looks wrong for thirty seconds before it comes together.

That gap between reading the steps and doing the thing is where most skill actually lives.

We have spent seven chapters on the steps. This one is about doing the thing.

---

It is 8:47 on a Tuesday morning and Maya Park is opening her laptop in a coffee shop in San Francisco. She is a senior associate at a venture firm. Her partner has asked her to produce a first-look due-diligence brief on a Series B candidate by end of day. The candidate is a small B2B software company in supply-chain analytics. The brief will land at the partner meeting Wednesday morning, where the firm decides whether to pursue real diligence.

Ten hours from now, she will send it.

What happens in between is not a demonstration of a framework. It is a person doing work. The framework is inside it, the way the recipe is inside the dish — present, but not the thing you're actually tasting.

---

Maya does not open Claude at 8:47. She opens a blank document.

For twelve minutes she writes about the brief. Audience: her partner, who will read it on his phone between six and eight tonight and use it Wednesday morning to argue for or against advancing the candidate. Length: four pages plus a source appendix. Structure: company snapshot, market, team, traction, risks, recommendation, open questions. Source rule: no claim without a footnote linking to a primary source or a specific conversation from this week.

Then she writes the success criteria. Her partner reads it in five minutes on his phone, gets the picture, shows up Wednesday with one or two specific questions to ask the founder. He does not feel the need to rewrite it.

Then she writes the exclusions. Do not invent industry comparables. Do not produce confident financial projections without explicit assumptions. Do not bury risks inside qualifying paragraphs. Do not produce a recommendation that hedges in both directions.

Twelve minutes. Everything that follows runs on top of those twelve minutes.

The reason to write the specification before opening the tool is not procedural. It is that the tool will answer whatever question you actually ask, and if you do not know what question you are actually asking, you will not notice when the answer drifts. Maya does not need the specification document. She needs the act of writing it — the forcing function that makes her discover, before she has spent four hours working, what she is actually trying to produce.

<!-- → [IMAGE: A photo or illustration of a handwritten or typed specification document — audience, success criteria, exclusions — sitting next to a closed laptop. The visual cue is that the spec precedes the tool. Works as a chapter opener image if the publisher wants one.] -->

---

Now she decomposes the brief.

The company snapshot — pulling product description, founding date, prior round sizes — is mechanical. The model will do this accurately and quickly and Maya doing it herself would teach her nothing she doesn't already know. She hands it over entirely.

The market sizing is synthesis. The model will gather, combine, and present numbers from multiple sources. Maya will evaluate the output, but more importantly she will check what the synthesis is not telling her — which sources weren't included, which framing wasn't considered, what a skeptic would reach for that the synthesis missed. This is the Nora trap from Chapter 4: synthesis tools tell you what the sources say. They cannot tell you what the sources don't say. She handles this by asking the model, explicitly, to steelman the bear case on the market after producing the main estimate.

The team analysis is synthesis of a different kind — public records, prior exits, named-investor signals. Same handling as market sizing: model generates, Maya verifies against primary sources, Maya checks for omissions.

The traction analysis is mixed. Public claims are mechanical, pull-and-verify. The operational reality — actual revenue trajectory, actual retention — lives in the founder's data room and her partner's call notes, which are not in the model's reach. Those parts are hers alone.

The risks section is contestable analysis. Reasonable practitioners would disagree about which risks are load-bearing in this segment at this stage. The model can surface candidates she should consider. The judgment about which risks actually matter — and how to weigh them against each other — is hers.

The recommendation is accountable judgment. Fully hers. The model will not be on the hook if the firm advances, spends two weeks on real diligence, and finds the candidate wanting. Maya will. The decision belongs to the person who carries the consequence.

She writes a six-line delegation map at the top of her notes file. Not for anyone else. For herself — so that when she is three hours in and the work is flowing, she does not accidentally start handing over the parts she meant to keep.

<!-- → [TABLE: Maya's delegation map — two columns: Task / Who Handles It. Rows: Company snapshot / Model entirely. Market sizing / Model generates, Maya verifies and checks for omissions. Team analysis / Model generates, Maya verifies against primary sources. Traction (public) / Model generates, Maya verifies. Traction (operational) / Maya alone. Risks / Model surfaces candidates, Maya judges. Recommendation / Maya alone. This table makes the decomposition step concrete and reusable as a template for readers building their own delegation maps.] -->

---

She opens Claude at 9:14. Her first prompt is 320 words.

It includes the audience, the structure, the constraints, the source rule, the exclusions. It asks for only the company snapshot and a first-pass market sizing — not the whole brief. This is important. Commissioning the full brief in one prompt produces output that is structurally complete and substantively thin. Commissioning in pieces produces output you can actually evaluate, section by section, with enough attention on each piece to catch what's wrong.

The model returns a clean snapshot and a market-sizing pass. The snapshot looks right. The market sizing has three numbers Maya does not recognize. She copies them into a verification list.

The second prompt: *steelman the bear case on this market.* The model produces one. It includes a thesis about platform consolidation that, if correct, would cause the candidate's target segment to contract rather than grow. Maya copies the thesis into her open-questions file. She does not know yet whether it is right. She knows it is the kind of argument her partner will make Wednesday morning if she does not address it.

The third prompt: *what assumptions am I implicitly making by treating this as a B2B software opportunity rather than a vertical-software opportunity?* The model surfaces three. One she disagrees with; she notes the disagreement. Two she had not considered; she folds them into her thinking.

By 10:02 she has rough drafts of the company snapshot and market sizing, a risk-candidate list, and — this is the part that justifies the conversation step — two arguments she did not start the morning holding. The model did not give her the conclusion. It gave her the shape of the problem, which is different and more valuable.

---

Now she verifies.

She opens the three primary sources for the market-sizing numbers. One is correct. One is approximately correct but uses 2024 numbers; the model had presented them as current. She updates. One does not exist — the model cited a source that she cannot locate. She finds an actual source for the same underlying claim and replaces the citation.

This is worth pausing on. The model produced a confident-looking citation to a source that was not there. This is not a rare failure mode. It is a common one. The fluent practitioner treats every citation as a hypothesis until verified. The literate user treats them as facts until something breaks.

She traces the market-sizing reasoning chain. The model assumed a particular growth rate to get from a current estimate to a five-year projection. She makes the assumption explicit in the brief with a sentence that names the source. Her partner will be able to poke at it if he wants to.

She asks herself: what other market-sizing frame would change my view? The model offers vertical segmentation versus horizontal. Her framing is horizontal because the candidate's product is sold horizontally. She notes the alternative in the appendix.

She messages her partner on Slack: *anything specific I should look for in this segment that I might miss?* He sends back two pointers. One is a regulatory development she had not considered. She adds a paragraph.

---

Maya gets a sandwich at 12:20. She does not eat at her desk. She sits in the sun and thinks about whether anything she has written is off.

One thing nags. The market-sizing section feels like it is overstating the segment's growth rate. Not by a lot. But her intuition from prior deals in adjacent spaces says the number is aggressive.

This is a real Loop step. Decompression is not a break from work. It is the part of work where your intuition catches up with your output. Most fluent practitioners have a version of this — a walk, a sandwich, a coffee away from the screen — that they take specifically to step outside the model's frame. The model produces output with a particular texture and rhythm, and if you stay inside it for six hours straight, you start taking that texture as given. Stepping out lets you hear the thing that was nagging.

---

At 1:14, Maya loops back to her specification.

The thing that nagged crystallizes. Her specification was wrong.

She had written the brief as if her partner wanted a recommendation *on the candidate*. But what he had actually said on Friday was that he wanted to know whether the candidate was worth real diligence over the next two weeks. That is a different question. In the first framing, the market-sizing section is load-bearing — it determines whether the opportunity is large enough to back. In the second framing, the market-sizing section is supporting context, and the load-bearing piece is something else entirely: *what would real diligence have to answer, and is answering it worth the firm's time*.

The open-questions section is now the most important section in the brief. The recommendation is not *in or out* but *advance to diligence versus pass now*, with a clear bar for what advancing would require.

She writes a new specification. She does not throw out the work. She re-anchors it. The sections that survive the change stay; the parts that don't get rebuilt.

The loop-back costs forty minutes. It is the most valuable forty minutes of the day.

This is what a linear chapter sequence cannot show. The Loop is a cycle. Midway through the work, discernment revealed a problem with specification. Maya went back. She did not start over. She rebuilt from the new spec, pulling forward what survived, rebuilding what didn't. If she had not taken the sandwich, had not let the intuition catch up, she would have sent a polished brief at 6 PM that answered the wrong question. The partner might not have known why it felt off. He would have known it felt off.

<!-- → [CHART: A timeline diagram of Maya's day — horizontal axis is clock time (8:47 AM to 5:52 PM), annotations at each key event: spec writing, delegation map, first Claude session, verification pass, sandwich / decompression, loop-back to specification, second Claude session, final verification, disclosure, send. Arrows showing the loop-back from 1:14 to the specification node. The point is to make the cycle structure visible against a real timeline so it doesn't read as abstract.] -->

---

The third conversation cycle, against the new specification, runs differently. It is faster and more surgical because the spec is sharper. The model produces, against the new brief, a recommendation framework: a list of what would have to be true for a yes-on-real-diligence, framed as testable hypotheses. She and the model spend forty-five minutes refining them, narrowing the open questions, holding each candidate question against the bar of *can the founder answer this in a one-hour call*.

By 2:55 the recommendation section reads: advance to real diligence, scoped to four hypotheses, sixty hours over two weeks.

---

At 3:00 she loops back again — this time not to specification but to a question about the process itself.

She does first-look diligence briefs every two to three weeks. This is not a one-off task. It is a recurring kind of task, which means the thing she learned today — confirm with the partner whether the brief is recommending on the candidate or on the diligence-time decision — should not need to be learned again. She makes a note in her template file. The question is now pre-baked. She will not make this specification mistake on the next brief.

This second loop-back is quieter than the first. Nobody watching her would see it. She just updated a file. But this is how fluent practitioners improve — not through retrospectives scheduled on a calendar, but through small notes made in the moment, folded back into the template, so that the next run of the same task starts from a slightly better place.

---

At 4:30 she runs the full verification pass. Three small fact errors, one reasoning gap, one framing alternative folded into the appendix.

At 5:45 the brief is done to her standard.

At 5:48 she writes four sentences.

*AI use note: Claude was used in research and drafting — primarily for market-sizing synthesis (sources verified independently, footnotes 3, 7, 11), team-background scan (verified via LinkedIn, Crunchbase, and a regulatory filing), and risk-category surfacing (then refined against my own assessment). The recommendation is mine. The verification is mine. Any errors are mine.*

The disclosure does not apologize. It does not pretend the AI did nothing. It does not pretend Maya did everything. It tells the partner exactly what was AI-assisted, exactly what was independently verified, and exactly who is accountable.

This is the AI Use Disclosure. It is the artifact that closes the loop — the moment where the practitioner's name goes on the work, not as a formality but as a genuine claim of ownership over the judgment calls that mattered.

At 5:52 she sends it.

Her partner reads it on the train home and texts at 7:11: *Tight. See you Wednesday.*

---

There is a specific thing that happened today that I want to name precisely, because it is easy to read the story and miss it.

Maya did not follow the Loop. She ran it. Following would mean executing the steps in sequence and stopping when you reach the end. Running means using the steps as a scaffold while staying alert to the places where the work itself tells you to go back. The loop-back to specification at 1:14 was not a failure of the framework. It was the framework working — the discernment step doing what it is supposed to do, which is surface the places where earlier decisions were wrong.

The fluent practitioner is not the one who executes the steps most cleanly. She is the one who notices fastest when a step needs to be revisited, and who does the revisiting without hesitation, without treating the prior work as a sunk cost she has to protect.

That is the difference. Not speed. Not better prompts. Not a more sophisticated delegation map. The willingness to loop back — to let the work teach you what the work actually needs — and the structural habit of creating moments where that teaching can happen.

---

Part II is about what happens when the loop runs faster, or without you in the moment, or across systems you do not fully control. The steps reweight. New failure modes appear. The judgment calls get harder, not easier, because the distance between your decision and its consequence gets longer.

What you just watched Maya do is the foundation. If any of the six things that happened today — the specification, the delegation map, the adversarial conversation, the verification, the loop-back, the disclosure — felt unfamiliar or uncertain, that is the place to go back to before continuing. The loop runs on top of that foundation. It does not replace it.

---

**What would change my mind.** If a careful study of fluent practitioners showed that the loop-back to specification is rare — that most briefs land on the first spec and the cycle is a teacher's overcorrection — the chapter is wrong about what the cycle is doing. What I observe is the opposite: the loop-back is frequent, and it is usually Discernment forcing a return to Specification. I would update on counter-evidence.

**Still puzzling.** The forty-minute cost of Maya's loop-back was obviously worth it. But I do not have a good model for when a loop-back is worth the cost and when it is a form of productive-feeling avoidance — a way of reworking the spec rather than doing the harder thing of committing to an output. That line is real and I do not yet know how to draw it precisely.

---

## Exercises

### Warm-Up

**1. Annotate the loop.** *(Tests: Loop step identification)*
The chapter traces six distinct things Maya does: specification, delegation map, adversarial conversation, verification, loop-back, disclosure. For each one, write one sentence naming what would have gone wrong if she had skipped it. Work through them in order. If you find two where skipping produces the same consequence, look again — the consequences are different.

**2. Classify the delegation.** *(Tests: delegation map construction)*
Maya's delegation map appears implicitly in the chapter and is reconstructed in the table. Below are five tasks drawn from a different kind of work — a graduate student writing a literature review. Classify each task the same way Maya classified hers: model entirely, model generates / human verifies, or human alone.

- Compiling a list of papers published in a given journal between 2018 and 2024 on a named topic
- Summarizing the argument of each paper
- Identifying which papers the field treats as foundational versus peripheral
- Deciding which gaps in the literature the student's own research addresses
- Writing the transition sentences that connect one paper's contribution to the next

For any classification you are uncertain about, write one sentence explaining what makes it contested.

**3. Write the disclosure.** *(Tests: AI Use Disclosure construction)*
Below is a brief description of an AI-assisted work product. Write the four-sentence AI Use Disclosure for it, following the structure of Maya's disclosure: what was AI-assisted, what was independently verified, who is accountable.

> A product manager used an AI tool to generate a competitive landscape analysis for a board presentation. The tool summarized five competitors' public positioning. The PM verified three of the summaries against the competitors' actual websites. The product strategy recommendation in the final slide was written by the PM without AI assistance.

---

### Application

**4. Write your specification.** *(Tests: specification — live application)*
Before your next AI-assisted work task — any task, today or this week — write the specification first, before opening the tool. Include: audience, success criteria, structure, exclusions. Time yourself. Spend no more than fifteen minutes. After you complete the task, look back at the specification and answer: what did writing the spec reveal about the task that you would not have noticed if you had opened the tool first?

**5. Build your delegation map.** *(Tests: delegation map — live application)*
For the same task from Exercise 4, or for any recent AI-assisted project, construct a delegation map using Maya's categories. Then compare it to what actually happened: which parts did you handle as planned? Which parts did you accidentally hand over that you had meant to keep? What caused the drift from the plan?

**6. Catch the hallucinated citation.** *(Tests: verification — targeted application)*
Take any AI-generated output that contains citations, footnotes, or references to named sources — from a recent project, or produced fresh for this exercise. Verify every citation: find the source, confirm the claim it is being used to support appears in the source, and confirm the source is current enough to be relevant. Report: how many citations were accurate? How many were approximately accurate but misrepresented? How many could not be located? What is your revised policy for treating AI-generated citations going forward?

**7. Find the specification error.** *(Tests: loop-back — diagnostic)*
Maya's loop-back at 1:14 was triggered by a gap between what she had specified and what her partner had actually asked for. Think of a recent piece of work you delivered — AI-assisted or not — that landed with some version of "this isn't quite what I needed." Reconstruct the specification you were working from. Then reconstruct the specification you should have been working from. Name the specific moment where you could have caught the gap, and what would have needed to happen for you to catch it.

---

### Synthesis

**8. Run a full loop.** *(Tests: all five Loop steps — integration)*
Choose a consequential task you need to complete in the next two weeks. Run the full Loop on it: write the specification before opening any tool; build the delegation map; use at least two adversarial moves in your AI conversation; run a verification pass on every claim you plan to ship; write the AI Use Disclosure before sending. After completing the task, write a one-page retrospective: where did the loop add the most value? Where did you feel friction against the structure? Did you loop back to specification? What did the loop-back cost, and was it worth it?

**9. Design the template.** *(Tests: Loop as recurring practice — synthesis)*
Maya's second loop-back is a template update — she pre-bakes a question into her brief template so she does not make the same specification mistake twice. Identify a recurring AI-assisted task in your own work. Design a reusable template for it that pre-bakes the specification, the delegation map structure, the adversarial moves you would deploy, the verification checklist, and the disclosure language. The template should be specific enough that the next time you run the task, the setup takes five minutes instead of thirty.

---

### Challenge

**10. The sunk-cost loop-back.** *(Tests: loop-back judgment — open-ended)*
The chapter ends with an unresolved puzzle: "I do not have a good model for when a loop-back is worth the cost and when it is a form of productive-feeling avoidance." Construct that model. In 400–600 words, propose a set of criteria — at least three, testable against real cases — for deciding whether a loop-back to specification is the right move or whether it is a way of avoiding the harder work of committing to an output. Test your criteria against Maya's 1:14 loop-back (should pass) and against at least one case you construct where the loop-back would be avoidance (should fail). Do not just describe the two extremes — find the line between them.

**11. The Loop under time pressure.** *(Tests: Loop adaptation — synthesis and critical stance)*
Maya had ten hours. Most knowledge workers do not always have ten hours for a piece of first-look work. In 400–600 words, address the following: If you had ninety minutes for the task Maya spent ten hours on, which steps compress, which steps are non-negotiable, and which steps change character under time pressure? Defend your choices by reasoning about what each step is doing — which failures it prevents and how costly those failures are relative to the time saved by skipping it. The answer "do fewer steps" is not wrong, but it requires you to name which failures you are accepting and why they are acceptable at that time horizon.
