# Chapter 2 — The Nine Capacities
*The gap between two equally smart people isn't skill — it's a constellation you can learn to see.*

I want to start with something I have been turning over for the last two years, because it is going to organize everything that follows.

When I watch two equally smart people use an AI tool — say, two software engineers, or two analysts, or two graduate students — and one of them gets dramatically better results than the other, the difference between them is almost never what you would predict. It is not that one of them knows more about machine learning. It is not that one of them is better at writing prompts. It is not that one of them is more familiar with the particular tool. Sometimes those things matter at the margin. But the bulk of the gap — the gap that makes one of them ship good work in a third of the time and the other ship mediocre work and not notice — that gap comes from somewhere else.

I want to find out where.

Let me show you what I mean by way of a single example. I will come back to it many times in this chapter, and I will refer to the person as Devin, because that is what I have always called him in my head. Devin is a real composite — that is, the things I am going to describe really happened, but they happened to several different engineers I have worked with, and I have rolled them into one person to keep the story clean. There are no invented quotes. There is only the pattern.

Devin is a software engineer, two years out of school. Sharp. Writes clean code. Trusted by his team. He gets a ticket: a customer is complaining that some date-related calculation in the product is occasionally wrong. Specifically, it sometimes returns the wrong number of days between two dates near the end of February. Devin has done date arithmetic before, but not this kind, and he reaches for an LLM. He explains the problem in a paragraph. He gets back a function that, on first read, looks correct. The function compiles. Devin writes a test. The test passes. Devin commits the code.

Three weeks later the same customer reports the same bug. The function fails on the last day of February in a leap year, in a way Devin's test did not exercise. Devin, when he looks back at the code, sees the failure mode immediately. The model had handled February 28 correctly. It had handled February 29 in a leap year correctly *as the start date*. It had not handled the case where February 29 was the *end* date and the calculation crossed it. Devin had not noticed because he had not generated the case in his test. He had not generated the case in his test because, when he read the function, he stopped reading at the place where it looked plausible.

Now here is the question I want you to sit with for a moment: *what, exactly, did Devin do wrong?*

Notice that it is not one thing. He did not fail at one cognitive task. He failed at several at once, and they are not the same kind of failure. Let me try to pull them apart, because the pulling-apart is the move I want you to learn in this chapter.

He failed, first, at *deciding what to delegate*. He gave the model the whole problem — including the part that required holding in his head a working model of the edge cases in the Gregorian calendar, which is exactly the kind of thing a human checking a model's output is supposed to do. He treated the model as a function that returns an answer. He should have treated it as a draftsman that returns a draft.

He failed, second, at *evaluating the output*. He read the function. He did not stress-test the function. He did not, before committing, ask himself: *what would have to be true for this to be wrong?* That question — *what would have to be true for this to be wrong* — is a different cognitive move from *does this look right?* The first asks you to imagine the world in which the code fails. The second asks you whether the code matches a vague mental picture of what correct code looks like. They feel similar. They are not. Devin made the second move when the situation called for the first.

He failed, third, at *handling uncertainty honestly*. The model had not told him, "I am 95% confident this handles all leap-year edge cases." Models do not, in general, tell you that. They produce confident-looking output and you have to import the uncertainty yourself. Devin did not import it. The output looked confident, so he treated it as confident. That is a sleight of hand the model is performing on him, and the cure for it is not in the model. It is in him.

And he failed, fourth — this one is subtle, but it matters more than the other three combined over the long run — at *staying in the practice*. Devin used to write date arithmetic by hand. He used to think carefully about edge cases because he had to. The model has, over the last year, taken that careful thinking out of his daily practice. Not out of his abilities — he could still do it if he sat down and tried. But out of his daily practice. And here is what is curious: what falls out of daily practice gets *slow* before it gets *weak*. A muscle you do not use gets slow before it atrophies. Devin's was getting slow. He could not feel it getting slow. People rarely can. They notice the day the muscle fails to do what they need it to do, and by then the gap they have to close is months wide instead of days.

So we have four different things, all happening at once, in one apparently simple failure. And if I told you a similar story about a marketing associate writing taglines, or a hiring manager screening résumés, or a graduate student writing a literature review — I will mention each of them briefly in a moment — you would find a different combination of similar failures each time. But you would always find a combination. Never just one.

This is what I have been turning over. People who use AI well are not doing one thing right. They are doing a constellation of things right, and the constellation has a shape.

I am going to claim the shape has nine points. I will not pretend the number is sacred. I will say that I have looked, over the last two years, at a lot of working practitioners, and the same nine kinds of cognitive move keep showing up. They are not exhaustive. They may, with more data, prove to be eight, or eleven. For now, nine fits the cases I have seen, and the cost of changing the count later is small. The capacities are what matter; the count is bookkeeping.

Here is the whole shape at once, sketched briefly, before I go through them in any depth. I will not work through all of them carefully here — that is what the rest of the book is for — but I want you to see the constellation in one glance, because each point only makes sense in relation to the others.

<!-- → [INFOGRAPHIC: A "constellation" diagram with nine labeled nodes arranged in a loose circular or organic cluster — each node is a capacity name with its one-line diagnostic question. Nodes are connected by light lines to suggest interdependence rather than hierarchy. This is the chapter's organizing image; it should be visually memorable and referenceable throughout the book.] -->

The first is **strategic delegation**: deciding, before you begin, what the model should do and what you should do, and why. This was Devin's first failure. The diagnostic question is: *what should I give the AI, what should I keep, and why?* The fluent practitioner can answer this question in seconds. The novice cannot answer it at all and so just hands the model the whole task, which is the same as not deciding.

The second is **effective communication**: telling the model — or your colleague, or the document you are writing — what it actually needs to know. The diagnostic question is: *am I specifying intent, constraints, audience, success criteria?* When this fails, the model fills in the blanks with its best guess at what you meant, and the best guess will be a slightly different one each time, which is how you get the experience of "the model is inconsistent" when actually you have been inconsistent and the model has been faithfully reflecting your inconsistency back at you. I find this the funniest of the nine, because the failure looks like the model's failure and is in fact yours.

The third is **critical evaluation**: reading the output for what kind of error it might contain. This was Devin's second failure, and it is, I think, the most under-practiced of the nine. Most people read AI output for whether it sounds right. Reading AI output for whether it *is* right is a different cognitive activity, and it requires you to hold, in your head, a model of the kinds of failure this kind of system produces. Without that internal model of failure, you have nothing to check against, and so the only thing you can check against is plausibility. Plausibility is a very low bar.

The fourth is **technical understanding**: knowing enough about how the system works under the hood to predict where it will fail. Not at a research depth. At a practitioner's depth. Enough to know that a language model will hallucinate citations because of how it was trained, and so you should always check citations. Enough to know that an image model will produce six fingers because of the structure of its training data, and so you should always count fingers. The diagnostic question is: *do I have a working model of why this thing succeeds and fails?* This is the capacity I find most often missing in otherwise sophisticated users. They use the tool well in the cases where it happens to work and have no theory of when it will not.

The fifth is **ethical reasoning**: noticing when the use case has stakeholders other than yourself and the AI, and acting on that noticing. The hiring manager who runs résumés through a tool he has not audited has failed at this. So has the marketing team that ships an ad campaign without asking who might be hurt by it. The diagnostic question: *who could be harmed by this output, and am I tracking that?* I want to flag, because it matters: this is not a soft skill. This is the capacity that keeps you from shipping a thing that gets you sued, or fired, or — more importantly — hurts somebody.

The sixth is **stochastic reasoning**: handling uncertainty honestly. Yours, the model's, the world's. This was Devin's third failure. The diagnostic question is: *what kind of probabilistic claim is this, and what would calibrate my belief in it?* I want to be honest with you that this is one of the harder capacities, because we are all bad at probability and the model produces output that looks deterministic when it is anything but. The model will give you a number — say, "65% probability the Fed cuts rates" — and the number will look like a number, and you will use it as if it were a number, and it may in fact be the model's best guess at last week's market-implied probability with no fresh information at all. The capacity is not "be good at probability." The capacity is "ask, every time, what kind of probabilistic claim is in front of me."

The seventh is **learning by doing**. This was Devin's fourth failure, the slow one. The diagnostic question is: *am I using the AI in a way that builds my skill, or in a way that consumes my skill?* These are different. AI use can be the most powerful learning multiplier you have ever encountered, and it can also be the fastest skill atrophier. Whether it is one or the other depends almost entirely on how you use it — not whether you use it. I am going to have a lot to say about this later, and I am going to keep coming back to it, because I think most people who think they are using AI to learn are using it in a way that prevents learning, and most people who think AI is making them dumber have simply not noticed the few specific moves that turn AI use into accelerated practice.

The eighth is **rapid prototyping**: treating model output as a draft to be tested in the world, rather than as the work itself. The product manager who hands four AI-generated feature ideas to engineering without prototyping or user-testing has failed at this. The model produced options. The model did not produce validation. The diagnostic question is: *am I testing this against reality, or just against my own approval?* Approval is cheap. Reality is the only thing that talks back.

The ninth is **theoretical foundations**: keeping enough domain knowledge in your own head that the AI is amplifying your understanding rather than substituting for it. The graduate student who has the AI write his literature review without reading the foundational papers has failed at this. He has the prose. He does not have the foundation, which means he cannot tell good prose from prose with subtly wrong framing. The diagnostic question: *do I understand the underlying material well enough to judge whether this output is good?* Without that, you are not collaborating with the model. You are taking dictation from it.

<!-- → [TABLE: The Nine Capacities reference table — columns: Capacity Name, Diagnostic Question, Which Kind of Failure (delegation / evaluation / uncertainty / practice), Durability (durable / contested / temporary). One row per capacity. This table should be formatted for easy scanning and positioned here so readers have the full picture before the durability discussion that follows.] -->

Nine. Each one a different cognitive capacity. Each one a place where I have watched real working practitioners fail. And — this is the part that took me longest to see — each one separable enough to practice on its own.

That last claim is the one I am least sure of, and I want to be honest about it. It is possible that the nine capacities correlate so strongly with general professional judgment that "develop the nine capacities" reduces, empirically, to "get better at your job." If that is true, the architecture in this book is decorative — it gets you the right behavior, but the decomposition into nine is not actually doing work. I have looked at this carefully and I believe the decomposition is doing work, in the sense that I can identify practitioners strong in some capacities and weak in others, and the patterns are not random. But I do not have the longitudinal data to be sure. If a careful empirical study showed that fluent practitioners share four or five of these and the rest are decorative, I would update. The list comes from observation, not theory, and observation can be wrong.

There is a second thing I want to be honest about, which is the question of *durability*. Some of these capacities are durably the human's responsibility, in any future I can foresee. Some are temporarily the human's responsibility, in 2026, and may not be in 2028 or 2030.

Strategic delegation is durable. Someone has to be accountable for the work, and accountability cannot be delegated to a model. Your name on the work is your name on the work, and the question of what to delegate is an accountability question, not a capability question. Ethical reasoning is durable in the same way. Someone has to be on the hook. Models cannot be on the hook in the relevant sense — when the lawsuit is filed, when the patient is harmed, when the algorithm denies the loan, the model is not the defendant. You are.

Learning by doing is durable in a different way: you have a body and the model does not, and the skills you build in your body — including the cognitive skills that live in the way you reach for tools — are yours regardless of what the model can do at any given moment.

Critical evaluation and stochastic reasoning are *contested*. Models are getting better at calibrated self-doubt and at uncertainty quantification. In some narrow domains a well-tuned model may already produce better-calibrated probabilistic claims than a well-trained human. The fluent practitioner of 2028 may have to update which parts of these capacities she still owns and which she has reasonable grounds to lean on the model for. I cannot tell you yet which parts those are. You will be able to tell, when the time comes, by the practice you have built.

The remaining four — effective communication, technical understanding, rapid prototyping, theoretical foundations — are temporarily irreducible at varying timelines. Models will erode parts of each. The judgment of what is a good prototype, what is a load-bearing foundation, what level of technical understanding is sufficient — that is going to remain yours longer than the production of those things.

<!-- → [CHART: A horizontal timeline or spectrum diagram showing the nine capacities arranged by durability — left axis "Durable (human always responsible)" through center "Contested (timeline unclear)" to right "Temporarily irreducible (eroding)". Each capacity placed at its approximate position based on the text's analysis. The goal is to make the durability gradient spatially legible.] -->

I am telling you this because I want the book to age well in your hands. The capacities that are durable, you are investing in for the whole career. The capacities that are temporary, you are still going to need for now, and the book will still try to teach them. When the timeline closes on any of them, you will be among the first to notice, because the practice you have built will tell you. That is one of the hidden benefits of practicing a capacity rather than reading about it: the practice gives you the sensors to know when the capacity is or is not still load-bearing.

I want to end with a thing I would do if I were sitting with you in a room. Take the nine capacities and ask yourself, on each one, where you are. Not in a precise way. In a four-level way. *Untrained* means you have not knowingly practiced this; you may not even know what it would feel like to practice it. *Aware* means you can name the capacity and recognize when it is at issue, but you do not yet have a routine for it. *Practicing* means you have a routine and you execute it imperfectly. *Fluent* means it is reflex, you do it without thinking, and you can teach it to somebody else.

<!-- → [TABLE: A self-assessment grid — rows are the nine capacities, columns are the four levels (Untrained / Aware / Practicing / Fluent) with a checkbox or blank cell at each intersection. Designed as a fill-in tool for readers, ideally formatted so it can be printed or used digitally. Include a small notes column or margin.] -->

Don't agonize about which level. Pick the one that is closer to true than the alternatives, and move on. The rough answer is what you need.

When you have nine answers, look at them and pick the two capacities you most want to move up one level in the next ninety days. Those are the two the rest of the book is going to be most useful for you on. Do not pick the ones you are already strongest in. That is comfortable and unproductive, and I have watched a lot of smart people make exactly that mistake — they invest in their already-strong capacities because the practice feels rewarding, and they leave the weak ones weak. The weak ones are where the next ninety days of deliberate practice will buy you the most working capability. Pick the ones that are slightly painful to look at honestly. Those.

Write them down somewhere you will find again. You are going to come back to them at the end of the book, and the comparison — what you said you would work on, what you actually got better at — is going to teach you something about yourself that I cannot teach you here.

That is what the nine capacities are. We will spend the rest of the book on them, one and two at a time, with the Loop as the workflow that draws on them. The Loop is what you do. The capacities are what you do it with. Hold both in your head as we go.

---

## Exercises

### Warm-Up

**1. Name the failure.** *(Tests: capacity identification)*
Return to the Devin story. For each of the four failures described — delegation, evaluation, uncertainty, practice — write one sentence that names what Devin should have done differently at exactly that moment. Keep each sentence to the action, not the theory.

**2. Map the diagnostic questions.** *(Tests: capacity recall)*
Without looking back at the chapter, write the diagnostic question for any five of the nine capacities. Then check your answers. For any you got wrong or couldn't recall: why did that one not stick? What would make the diagnostic question more memorable to you?

**3. Spot the missing capacity.** *(Tests: capacity recognition in context)*
A marketing associate uses an AI tool to generate five tagline options for a product launch. She picks her favorite, sends it to the client, and the client approves it. Six months later the tagline turns out to echo the slogan of a competitor from a decade ago — not copyrighted, but embarrassing. Name every capacity she failed to exercise, in the order she failed to exercise them.

---

### Application

**4. Classify a real task.** *(Tests: strategic delegation)*
Take a task you actually did in the last week — with AI or without. Break it into its component subtasks. For each subtask, apply the strategic delegation diagnostic: *what should I give the AI, what should I keep, and why?* Write out your reasoning for at least three of the subtasks. Then ask: did you actually split the work this way? If not, what would have changed if you had?

**5. Rewrite the prompt.** *(Tests: effective communication)*
Below is a real prompt that produces inconsistent output from a language model:

> "Summarize this article for me."

Rewrite it to specify intent, constraints, audience, and success criteria. Your rewrite should be no longer than 80 words. Then explain, in two or three sentences, what gap between the original and the rewrite the model was previously filling with guesswork.

**6. Import the uncertainty.** *(Tests: stochastic reasoning)*
A model returns the following output in response to a question about a business decision:

> "Based on current trends, there is approximately a 70% chance that the new feature will increase retention."

Write three questions you would ask — or investigations you would run — before using this number in a decision. For each question, name what kind of uncertainty it is checking: the model's training data, the model's reasoning, or the underlying world.

**7. Durability classification.** *(Tests: technical understanding + theoretical foundations)*
The chapter places the nine capacities on a rough durability spectrum. Pick one capacity the chapter calls "durable" and one it calls "contested." For each: write a one-paragraph argument for why a practitioner in 2030 might reasonably disagree with the chapter's classification. You don't have to believe the argument — just make it honestly.

---

### Synthesis

**8. The hiring manager case.** *(Tests: ethical reasoning + strategic delegation + critical evaluation)*
A hiring manager at a mid-size company is screening 200 résumés for an engineering role. She passes all 200 through an AI tool that ranks them by predicted job fit and returns the top 20 for human review. She does not audit the tool, does not examine how it was trained, and does not review any résumé outside the top 20.

Identify every capacity the hiring manager failed to exercise. For the two you consider most consequential: explain not just what she failed to do but what specific harm or error could result. Then describe the minimum practice — one action per capacity — that would have meaningfully reduced that risk.

**9. The slow failure.** *(Tests: learning by doing)*
The chapter describes a kind of failure that is "slow" — a capacity that atrophies before it visibly fails. Choose a professional skill from your own domain (not date arithmetic) that you believe is currently in your daily practice. Describe, concretely, what it would look like if that skill were being quietly eroded by AI use — the early warning signs, the first visible failure, the gap that would have accumulated by the time you noticed. Then design one specific practice routine — something you could do in under 20 minutes per week — that would keep the skill load-bearing regardless of how much AI you use.

---

### Challenge

**10. The ninth capacity stress test.** *(Tests: theoretical foundations — open-ended)*
The chapter argues that theoretical foundations are "temporarily irreducible" — that a practitioner needs enough domain knowledge to judge whether model output is good, even if models are getting better at producing it. Find a domain where you have genuine expertise. Design a test — a specific prompt, task, or question — that you believe would reveal the difference between a practitioner who has that domain foundation and one who does not, using only the outputs they produce or accept from an AI tool. Your test should be concrete enough that someone could actually run it.

**11. Update the architecture.** *(Tests: all nine — synthesis and critical stance)*
The chapter admits: "I do not have the longitudinal data to be sure" the decomposition into nine is doing work. Treat this as an invitation. Based on your own experience using AI tools professionally, make one of the following arguments in 400–600 words:

- One of the nine capacities should be split into two distinct capacities (they are not the same kind of failure).
- Two of the nine capacities should be merged (they reliably co-occur and cannot be meaningfully separated in practice).
- A tenth capacity is missing from the list (name it, give its diagnostic question, give a real case where its absence caused a failure).

You are not required to be right. You are required to argue from evidence — cases, observations, or your own experience — rather than from theory alone.
