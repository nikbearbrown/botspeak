
# Chapter 0 — The Citation That Wasn't

It's Tuesday, 9:42 in the morning, in an open-plan office in Boston, and a young consultant named Diego Alvarez is reading an email he didn't expect.

The email is from his client. Diego sent the deliverable on Friday — a sixteen-page market analysis on the home-medical-equipment industry, prepared on a one-week turnaround for a private equity firm thinking about an acquisition. It was, Diego thought, a good memo. The exhibits were clean. The language was tight. The recommendation was hedged in the right places. It cited eleven sources, including a 2024 industry report from a research firm whose name appeared respectable.

The client's in-house researcher had spent the weekend pulling those sources to verify them. Ten checked out. The eleventh did not. The eleventh source — the one Diego's memo cited for the most consequential single number in the deliverable, the projected 8.4% compound annual growth rate of the durable medical equipment segment through 2028 — did not exist. Not the report. Not the firm. Not the analyst whose name appeared in the footnote. The 8.4% number, the researcher's email said politely, "appears to be without basis," and the researcher would like to understand how this happened before the team's call at 3 PM today.

Diego stares at his monitor. He knows, more or less, what happened.

He had asked Claude for a market analysis with sources, and Claude had given him a market analysis with sources. He had pasted the relevant sections into his memo, polishing the language and tightening the structure. He hadn't, at any point, opened a browser and tried to find the eleventh report. He hadn't asked the model whether any of the cited sources were ones it had invented. He hadn't, at any point, treated the output as raw material that still needed pricing.

Now I want you to sit with that for a moment, because the thing that happened to Diego is not what most people think it is. Most people, hearing this story, will say Diego was lazy, or careless, or unprofessional, or used the wrong tool. None of those things are true. Diego is none of those things. He's twenty-six years old, he has a master's degree from a good school, he prepared meticulously for the case interviews that landed him this job, and he had used Claude through grad school and through the job hunt with what felt like consistent success. His firm's onboarding included three slides about AI use, and the most important slide said: "Always verify AI outputs before client delivery." Diego had nodded along. He didn't know what verifying actually meant.

This is what I want to talk about in this chapter. I want to talk about why Diego sent that memo. Because if I can convince you that it wasn't laziness or carelessness — that it was, instead, a *predictable* gap between two skills that look the same and aren't — then we have something to work with. Then the rest of this book is about closing the gap.

## Two things that look the same and are not

Let me name two things, because we don't have a vocabulary for them yet, and the absence of the vocabulary is part of the problem.

The first is *AI literacy*. AI literacy is what Diego has. He can open a chatbot. He can type a prompt. He can read the answer. He can copy and paste. He can, at a kind of taste-level, tell whether the output reads polished or reads rough. He has used these tools on graded assignments, on cover letters, on the case prep he did before this job, and he has gotten useful work out of them most of the time. Nearly every recent graduate has AI literacy now, even when they think they don't, even when their parents at Thanksgiving worry that they don't. The bar is low and the world has cleared it.

AI literacy is necessary. It is not sufficient. It is, in particular, not sufficient when you have a job and the deliverables matter. Holding only AI literacy and walking into the situation Diego walked into on Friday is the situation Diego is in on Tuesday at 9:42 in the morning. The output looks polished. The output reads competent. The output is wrong in a way the literate user is not equipped to detect, because the failure mode is *exactly* the kind of failure a literate user does not yet know to look for.

The second thing is *AI fluency*. AI fluency is what Diego doesn't have. It is, three years from now, what the senior people on his team will have. It is the difference between Diego's memo on Friday and a memo from a senior consultant given the same brief.

A fluent practitioner — let's call her Maya, three years ahead of Diego on the same team — would not have shipped Diego's memo. Not because Maya is smarter. Not because Maya is more careful in some fuzzy diligent way. Not because Maya has read more books about AI ethics. Maya wouldn't have shipped that memo because she has a workflow Diego doesn't have. Because she runs the AI through five steps where Diego ran it through one. Because when a chatbot hands her eleven citations, she has a habit — a learned reflex — of asking which of these are the ones I'd bet a client relationship on. Because she knows that the citation step is exactly the kind of place a model fabricates, and she has a specific verification move calibrated to that risk. Because she's not surprised when the model produces a fabrication. By 9:42 AM, she's only surprised when it doesn't.

That difference — between Diego and Maya — is teachable. I want you to notice that it has structure. It is not a personality trait. It is not a function of how careful you are by nature. It is not something you'll absorb from another year of generic experience with the tools. It is a discipline, and the discipline is this book.

## The young American in Paris

Now I want to give you a metaphor, because I think it's the right one, and I want to make sure you have it before we go any further.

A young American flies to Paris on his first business trip. He has, at some point in high school or college, learned about French in the way Americans learn about French. He knows there is a French language. He knows it has accents on some of the letters. He knows that *bonjour* means hello and that you order *un café* if you want a coffee and *l'addition* if you want the bill. He has watched a few films. He has eaten at a creperie in Brooklyn. He thinks of himself as someone who is okay with French.

He arrives in Paris and is surprised to find that the French expect him to do things in French. He is surprised that the waiter at the brasserie does not warm to him when he points at items on the menu. He is surprised that his hotel concierge gives crisp answers to direct questions but does not volunteer the kind of context an American concierge would. He is surprised that the man at the *tabac* is, somehow, contemptuous in a way the American can't quite name. He flies home and tells his friends the French are rude.

The French are not rude. The American doesn't speak French. He has French *literacy* — the bare awareness that French exists and that some of the words map to some of his needs. He doesn't have French *fluency* — the basic competence to ask a question, hear an answer, follow up, navigate a misunderstanding, or recognize when his interlocutor is being polite in a way he should match.

The fluent traveler goes to Paris and watches the same brasseries warm up to him over the course of dinner. The illiterate traveler is annoyed at the French. The literate traveler is the one who has half the situation and doesn't know it.

And here is the part I want you to feel, not just understand: the literate traveler is in the worst position of the three. The illiterate traveler at least *knows* he doesn't speak French, so he doesn't try, so he doesn't put himself in situations where his lack of French costs him anything. The fluent traveler doesn't lose anything either, because she's fluent. The literate traveler is the only one who walks confidently into situations he cannot handle and is then surprised when they go badly. He is the only one who, by Wednesday of his trip, is genuinely angry at people who have been polite to him.

Diego, on Tuesday at 9:42 in the morning, is the literate traveler. He's not the person who refused to use AI. He's not the senior consultant on his team. He's the one in the middle, the one with enough capability to ship something to a client and not enough capability to know what he's shipping.

This book is not the French of the Sorbonne. It's not the French you'd need to read Camus in the original or argue philosophy at a dinner party. It's the working French of someone who shows up in Paris and is *trying* — how do I order food, how do I ask where the bathroom is, how do I get a taxi, how do I tell the doctor where it hurts. It's the basic competence that gets the brasseries to warm up.

## Why volume looks like quality

There's one specific failure mode worth naming on this opening page, because it's the one Diego fell into, and most fluent practitioners I've talked to had to climb out of it themselves before they noticed it.

A literate user, asked to produce a deliverable, gets four pages of output from the chatbot. Four pages. With headings, transitions, bulleted lists, exhibits. The output looks like work. It looks, in the way a novice can perceive, *exactly the way work is supposed to look*. The literate user reads it, lightly edits it, and ships it. The output looks polished and the underlying judgment that should have shaped it is invisible — because the polish is doing the job that judgment used to do.

A fluent practitioner, given the same four pages, immediately becomes suspicious of them. She knows, because she has been burned, that an LLM can fill four pages with confident, structured, citation-bearing prose that is nonetheless wrong in places that matter. The four pages, to her, are not work. They're raw material. The work — the part she has to do, the part the model cannot do for her, the part her job actually depends on — has not yet started.

Notice what's strange about this. In almost every other domain we know, volume *is* a reasonable proxy for quality. A long memo took someone longer than a short memo. A thick report involved more research than a thin one. A 200-page novel represents more work than a 20-page short story. The world we grew up in built our intuitions on this correlation, and our intuitions are right almost everywhere except here.

LLMs broke the correlation. An LLM produces volume at constant cost. The four pages took the same work to generate as the four sentences. Volume, in the post-LLM world, is not evidence of effort, and it is not evidence of quality. To the literate eye, it still looks like both. To the fluent eye, it looks like raw material that has not yet been priced.

This is one of the reasons recent graduates ship deliverables their managers don't, and one of the reasons recent graduates' deliverables read polished and read wrong. It's not the only reason. It's the easiest one to name on the first page.

## What this book will and won't do

I want to be honest with you about what this book can and cannot do.

It's going to give you a workflow. Five steps, run as a cycle. We'll spend a chapter on each one. By Chapter 8 you'll have run the full cycle on a real task with yourself in the loop. By Chapter 10 you'll have learned to run it without yourself in the loop. By Chapter 12 you'll have learned to run it when the AI is taking actions in the world on your behalf and not just producing text.

It's going to give you a vocabulary. Names for the moves Maya makes that Diego doesn't, so you can recognize them when you make them, and notice when you skip them.

It's not going to teach you a specific AI tool. The examples use Claude, with sidebars for ChatGPT and Gemini, but the tools change every six months and the discipline does not. It's not going to teach you AI ethics in the comprehensive sense — that's a different book, an important one, but a different one. It's not going to teach you the inner workings of large language models. There is one paragraph, in Chapter 1, on how an LLM produces its output, because that paragraph does work. The rest of that literature is a field you can study afterward if it interests you.

It is going to teach you AI fluency. AI fluency is what Diego does not yet have. AI fluency is what Maya has. AI fluency is the difference between the practitioner who uses AI to do their job better and the practitioner who uses AI and does their job worse.

---

It is now 9:58 AM on a Tuesday in Boston. Diego has six hours until the 3 PM call. The next thirteen chapters are going to be about how he should have spent the previous five days, and what — between now and 3 PM — he can salvage.

I'll tell you now what I think is the most interesting thing about Diego's situation. It's not that he's in trouble. He is, but it's recoverable; junior consultants make this kind of mistake and survive, and Diego is going to survive this one. The interesting thing is that the firm hired Diego specifically *because* he was AI-literate. They valued the literacy. They counted on it. They gave him a one-week turnaround on a deliverable that, ten years ago, would have been a four-week project for a team of three. The firm bet on AI as a productivity multiplier, and they were right to bet on it, and they staffed the project assuming the multiplier would hold.

The multiplier did hold. Diego produced sixteen pages in five days. The pages looked like sixteen pages of work. The pages cost less time and money than sixteen pages of pre-AI work would have cost. Everything about the economics of the situation worked the way it was supposed to.

And then one of the citations was wrong, and the whole memo is now in question, and the client's confidence in the firm has taken a hit they will need months to repair.

This is what I mean when I say AI literacy is not sufficient. It's not that the literate user can't produce work. The literate user produces a *lot* of work. The problem is that the work is unpriced — that the literate user cannot tell, looking at his own output, where the value is and where the rot is. The firm bet on a productivity multiplier and got one. They did not yet know that the multiplier comes with a verification cost, and that someone has to pay it, and that if Diego doesn't pay it, the client will, and the cost the client pays is denominated in trust.

The fluent practitioner pays the verification cost on her own time, in her own workflow, before the work leaves her desk. That is most of what fluency *is*. That is most of what this book teaches.

Open Chapter 1. We'll start with the first step.

