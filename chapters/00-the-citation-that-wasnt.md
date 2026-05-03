# Chapter 0 — The Citation That Wasn't

*What the literate user doesn't know they don't know.*

It is 9:42 on a Tuesday morning in Boston, and Diego Alvarez is staring at an email he did not expect.

He had sent the deliverable on Friday — sixteen pages on the home-medical-equipment sector, prepared on a one-week turnaround for a private equity client considering an acquisition. Clean exhibits. Tight language. The recommendation hedged in the right places. Eleven footnotes, including a 2024 industry report from a research firm whose name looked respectable.

The client's in-house researcher had spent the weekend pulling the sources. Ten checked out. The eleventh did not. The eleventh source — the one cited for the most consequential single number in the deliverable, the projected 8.4% compound annual growth rate of the durable medical equipment segment through 2028 — did not exist. Not the report. Not the firm. Not the analyst whose name appeared in the footnote. The 8.4% figure, the researcher's email said politely, "appears to be without basis," and could Diego help them understand how this happened before the 3 PM call?

Diego knows what happened. He had asked Claude for a market analysis with sources. Claude had given him a market analysis with sources. He had pasted the relevant sections into his memo, polished the language, and shipped it. He had not, at any point, opened a browser and tried to find the eleventh report. He had not asked the model whether the sources were real. He had not treated the output as something that still required pricing.

I want you to sit with that for a moment before we go further, because the failure here is not the one most people will name. Most people who hear this story will say Diego was lazy, or careless, or used the wrong tool. None of those things is true. Diego is twenty-six years old with a master's degree from a good school. He prepared meticulously for the case interviews that landed him this job. He has used Claude through grad school, through job hunting, through the mock deliverables he practiced during onboarding, and in all of those contexts the model gave him useful work. His firm's onboarding included three slides on AI use. The most important slide said: *Always verify AI outputs before client delivery.* Diego nodded along. He did not know what verifying actually meant.

That gap — between hearing an instruction and knowing what it actually requires — is the subject of this book.

---

<!-- → [INFOGRAPHIC: Two-column split — "AI Literacy" vs "AI Fluency" — each column lists 4–5 concrete observable behaviors (e.g., literacy: opens chatbot, reads output, copies and pastes; fluency: spots citation-risk zones, runs verification moves, treats output as raw material). Purpose: make the distinction tangible before the prose defines it.] -->

Let me name two things that look identical from the outside and are not.

The first is AI literacy. Diego has this. He can open a chatbot, type a prompt, read the output, copy and paste. He can, at a taste level, tell polished output from rough output. He has gotten useful work out of these tools many times. Nearly every recent graduate has AI literacy now, even when they think they don't, even when their parents worry that they don't. The bar is low and the world has largely cleared it.

AI literacy is necessary. It is not sufficient. It is not sufficient, in particular, when you have a job and the deliverables go to clients. Walking into that situation with only AI literacy is Diego's situation on Tuesday morning. The output looked polished. The output read competent. The output was wrong in a way the literate user cannot detect, because the failure mode is exactly the kind a literate user does not yet know to look for.

The second thing is AI fluency. Diego does not have this. Three years from now, the senior people on his team will have it. It is the actual difference between Diego's memo on Friday and a memo from a senior consultant given the same brief.

A senior consultant — call her Maya, three years ahead of Diego — would not have shipped that memo. Not because Maya is smarter. Not because Maya is more careful in some vague, unspecifiable way. Not because she has read more books about AI safety. She would not have shipped it because she has a workflow Diego does not have. She runs the AI through five steps where Diego ran it through one. When a chatbot hands her eleven citations, she has a habit — a learned reflex — of asking: *which of these are the ones I'd bet a client relationship on?* She knows that the citation step is exactly the place a model hallucinates, and she has a verification move calibrated to that risk. She is not surprised when the model fabricates a source. By Tuesday morning, she is only surprised when it doesn't.

That difference is teachable. It has structure. It is not a personality trait, not a function of native carefulness, not something you absorb from another year of undirected experience with the tools. It is a discipline. It is what this book is for.

---

Here is the metaphor I keep coming back to.

<!-- → [IMAGE: Illustrated split-scene — left panel: confident American pointing at a Paris brasserie menu while the waiter looks on coolly; right panel: same brasserie, different traveler leaning in, waiter smiling. No text needed. Visual anchor for the literacy/fluency/illiteracy triad before the prose walks through it.] -->

A young American goes to Paris on his first business trip. He has, at some point, learned about French in the way Americans learn about French. He knows there is a French language. He knows *bonjour* means hello. He knows you order *un café* for coffee and ask for *l'addition* when you want the bill. He has eaten at a creperie in Brooklyn. He thinks of himself as someone who is okay with French.

He arrives in Paris and is surprised to find that the French expect him to do things in French. The waiter at the brasserie does not warm to him when he points at the menu. His hotel concierge gives crisp answers but does not volunteer context. The man at the *tabac* is contemptuous in a way the American cannot quite name. He flies home and tells his friends the French are rude.

The French are not rude. The American does not speak French.

What he has is French *literacy* — the bare awareness that French exists and that some of its words map onto some of his needs. What he lacks is French *fluency* — the basic competence to ask a question, hear an answer, follow up, navigate a misunderstanding, or recognize when his interlocutor is being polite in a way he should match.

The fluent traveler goes to Paris and watches the same brasseries warm up over the course of dinner. The American who knows no French at all is annoyed too, but he at least *knows* he doesn't speak the language, so he doesn't put himself in situations his lack of French will cost him. He is not surprised when things go badly. The literate traveler is the one in the worst position. He has enough to feel confident going in and not enough to handle what he encounters. He is the only one who walks into situations he cannot manage and then blames the situation.

Diego, at 9:42 in the morning, is the literate traveler. He has enough AI capability to feel confident. He does not have enough to know what he is shipping. The deliverable looked like work. It read like research. The polish was real. The underlying judgment — the judgment that should have caught the eleventh citation — was not there.

This book is not the French of the Sorbonne. It is the working French of someone who shows up in Paris *trying* — how do I order food, how do I ask where the bathroom is, how do I tell the doctor where it hurts. The functional, daily-use competence that gets the brasseries to warm up.

---

There is one specific failure mode worth naming now, because it is the one Diego fell into and because most fluent practitioners had to climb out of it themselves before they could see it clearly.

A literate user asked to produce a deliverable gets four pages of output from the chatbot. Four pages, with headings and transitions and bulleted exhibits. The output *looks* like work. It looks, in the way a novice perceives work, exactly the way work is supposed to look. The literate user reads it, lightly polishes it, and ships it. The output is polished. The judgment that should have shaped it is invisible — because the polish is doing the job that judgment used to do.

A fluent practitioner, handed the same four pages, immediately becomes suspicious of them. She knows, because she has been burned, that a language model can fill four pages with confident, structured, citation-bearing prose that is nonetheless wrong in places that matter. To her, the four pages are not work. They are raw material. The work — the part she has to do, the part the model cannot do for her, the part her job actually depends on — has not yet started.

Here is what is strange about this. In almost every other domain, volume is a reasonable proxy for quality. A long memo took someone longer than a short memo. A thick report required more research than a thin one. The world we grew up in trained our intuitions on this correlation, and those intuitions are right nearly everywhere — except here.

<!-- → [CHART: Simple two-panel contrast — left: pre-LLM world, upward-sloping line showing output volume correlating with effort/quality; right: post-LLM world, flat line showing output volume decoupled from effort, with "verification cost" marked as a separate unlabeled bar. Student should notice the correlation breaks and ask where the quality signal went.] -->

Language models broke the correlation. They produce volume at constant cost. The four pages took the same effort to generate as the four sentences. Volume in the post-LLM world is not evidence of effort and not evidence of quality. To the literate eye, it still looks like both. To the fluent eye, it looks like raw material that has not yet been priced.

This is why recent graduates ship deliverables their managers wouldn't, and why those deliverables read polished and read wrong. It is not the only reason. It is the easiest one to name on the first page.

---

I want to be honest about what this book can and cannot do.

It will give you a workflow — five steps, run as a cycle. Specification, Delegation, Conversation, Discernment, Diligence. We will spend a chapter on each. By Chapter 8 you will have run the full cycle on a real task with yourself in the loop. By Chapter 10 you will have learned to run it without yourself in the loop. By Chapter 12 you will have learned to run it when the AI is taking actions in the world on your behalf and not just producing text.

<!-- → [INFOGRAPHIC: The Loop as a circular five-step diagram — Specify → Delegate → Converse → Discern → Be Diligent → back to Specify. Minimal labels only; no descriptions. First appearance of the book's central framework; the visual should feel like a preview, not a full explanation.] -->

It will give you a vocabulary — names for the moves Maya makes that Diego does not, so you can recognize them when you are making them and notice when you are skipping them.

It will not teach you a specific AI tool. The examples use Claude, with sidebars for ChatGPT and Gemini, but the tools change every six months and the discipline does not. It will not teach AI ethics in the comprehensive sense. It will not teach you the inner workings of language models. There is one paragraph, in Chapter 1, on how an LLM produces its output, because that paragraph does work. The rest of the model-internals literature is a field you can visit afterward.

What it will teach is AI fluency. The difference between Diego on Friday and Maya on the same brief. The difference between the practitioner who uses AI to do their job better and the practitioner who uses AI and does their job worse.

---

I will tell you now what I think is the most interesting thing about Diego's situation, because it is easy to miss if you are focused on the mistake.

His firm hired him specifically because he was AI-literate. They valued the literacy. They counted on it. They gave him a one-week turnaround on a deliverable that, ten years ago, would have been a four-week project for a team of three. The firm bet on AI as a productivity multiplier, and they were right to bet on it, and they staffed the project assuming the multiplier would hold.

The multiplier did hold. Diego produced sixteen pages in five days. The pages looked like sixteen pages of work. The pages cost less time and money than sixteen pre-AI pages would have cost. Everything about the economics worked the way it was supposed to.

And then one citation was wrong, and the whole memo was now in question, and the client's confidence in the firm had taken a hit they would need months to repair.

This is what I mean when I say AI literacy is not sufficient. The literate user produces *a lot* of work. The problem is that the work is unpriced — the literate user cannot look at his own output and tell where the value is and where the rot is. The firm bet on a productivity multiplier and got one. What they did not know is that the multiplier comes with a verification cost, and that someone has to pay it. If Diego does not pay it before the deliverable leaves his desk, the client pays it afterward, and the cost the client pays is denominated in trust.

<!-- → [TABLE: "Who pays the verification cost" — three rows: (1) Fluent practitioner pays before delivery — cost: her time; consequence: clean deliverable; (2) Literate practitioner skips it — cost: none upfront; consequence: client discovers the error; (3) Client pays — cost: trust, relationship, repair time. Columns: Who pays | When | In what currency | Consequence. Anchors the economics argument the paragraph is making.] -->

The fluent practitioner pays the verification cost in her own workflow, before the work leaves her desk. That is most of what fluency *is*. That is most of what this book teaches.

It is now 9:58 AM on a Tuesday in Boston. Diego has six hours until the 3 PM call. The next thirteen chapters are about how he should have spent the previous five days, and what — between now and 3 PM — he can salvage.

Open Chapter 1. We'll start at the beginning.

---

**What would change my mind.** If a serious longitudinal study of recent-graduate AI use showed that the literate-fluent gap closes within a year of normal job exposure, without any structured framework — that practitioners self-teach fluency from sheer reps — the book's central premise weakens. I have not seen such a study. The closest evidence I am aware of points the other way: literacy plateaus, and the fluency gap persists or widens.

**Still puzzling.** I do not yet have a clean way to distinguish "fluency" from "good judgment shaped by enough painful experience." It is plausible that what I am calling fluency is simply what painful experience teaches anyway, and that naming the moves and rehearsing them just compresses the timeline. I have not yet seen the experiment that would prove it.

---

> **Going deeper — *Computational Skepticism for AI***
>
> Diego's failure has a name in the academic literature: the **fluency trap**. Fluent output triggers an evaluation booster — readers trust well-written prose more than the evidence warrants. The trap doesn't only fool literate users; it amplifies whatever evaluation the reader was going to make, including the wrong ones. The fabricated citation is the visible symptom; the trust-in-the-fluency is the mechanism.
>
> The companion advanced volume *Computational Skepticism for AI* opens by naming this directly and gives you four philosophical moves to interrupt it before it does damage — Cartesian doubt, Hume's induction limit, Popperian falsifiability, and the Plato's Cave move — plus the Five Supervisory Capacities the deeper book is organized around.
>
> See *Computational Skepticism for AI*, **Chapter 1 — The Skeptic's Toolkit**.

---

### LLM Exercise — Chapter 0: The Citation That Wasn't

**Project:** AI Fluency for [Your Role] — The Domain Field Manual

**What you're building this chapter:** The role you'll write the playbook for, a Role Dossier you'll pin to your Claude Project for the rest of the book, and the playbook's opening case — a domain-specific Citation-That-Wasn't drawn from a real or plausible AI failure in your field.

**Tool:** Claude Project (set up "AI Fluency for [My Role]" and return every chapter) + Cowork (create the playbook folder and the first section file).

---

**The Prompt:**

```
I am working through "Botspeak" and across the book I will translate the framework into a domain-specific playbook — "AI Fluency for [MY ROLE]" — that another junior in the same role could pick up and use. This is the setup chapter. I need help with two tasks.

TASK 1 — SPECIFY THE ROLE. The role should be:
- One I actually work in (or am about to enter)
- Specific enough to be useful — not "knowledge worker" but "junior associate at a regional law firm" or "growth marketer at an early-stage SaaS company" or "clinical pharmacist on hospital night shift"
- Bounded enough that the failure modes are recognizable to anyone in the role
- Big enough that the playbook helps a real population

My context:
- Role / job title: [FILL IN]
- Industry / sector: [FILL IN]
- Career stage of the playbook's reader: [0–6 months / 6–18 months / 18–36 months]
- 2–3 task types I do most weekly: [LIST]
- Whether AI use is sanctioned, unsanctioned, or contested in my workplace: [FILL IN]

Push back if my role is too broad. Help me sharpen until the playbook would be unmistakably for someone in this role and not someone in an adjacent one.

TASK 2 — FIND THE OPENING CASE. Botspeak Chapter 0 opens with Diego, a junior consultant who shipped a fabricated citation. The Citation-That-Wasn't IS the chapter — the case carries the argument. My playbook needs its own version. The case should be:
- An AI failure someone in my role has actually had, or could plausibly have, in the next year
- Specific enough that the reader recognizes themselves in it (named tools, named tasks, specific stakes)
- Recoverable — the case opens the playbook; the playbook teaches what would have caught it
- True or labeled-illustrative; if invented, name the invention

Walk me through 2–3 candidate cases drawn from my role. For each: the task that triggered it, the AI move that failed, the type of failure (fabrication / wrong-premise reasoning / dangerous omission / sycophantic drift), the cost when it surfaced, who paid that cost, and the literate-user pattern that made it possible. Help me pick the strongest one — the one where the failure mode generalizes.

End with:
1. A one-paragraph "Role Dossier" I can pin to my Claude Project's system prompt so every future chapter exercise inherits the role context.
2. The playbook's opening section in 800–1,500 words, in the voice of Botspeak Chapter 0, drawing on my chosen case.

Save as `01-the-[your-failure-slug].md` in my playbook folder.
```

---

**What this produces:** A Role Dossier (pinned to the Project), the playbook folder structure, and Section 1 of the playbook — your role's Citation-That-Wasn't. Twelve more sections to follow.

**How to adapt this prompt:**
- *For your own project:* Fill in the bracketed fields. If you wear multiple hats, pick the role you'll keep growing in.
- *For ChatGPT / Gemini:* Works as-is. Set up as a Custom GPT for persistence. Gemini's Drive integration handles the playbook folder cleanly.
- *For Claude Code:* Not yet — this chapter is conceptual.
- *For a Claude Project:* Recommended. The Role Dossier becomes part of the system prompt going forward.
- *For Cowork:* Recommended for managing the playbook folder. Ask Cowork to create the folder structure: `playbook/01-opening-case.md`, `playbook/02-the-loop.md`, etc.

**Connection to previous chapters:** This is the foundation. Without the role specified and the dossier pinned, every subsequent chapter exercise produces generic content.

**Preview of next chapter:** Chapter 1 takes a typical task in your role and walks the full Loop on it — your role's version of Priya's Tuesday. The walkthrough becomes Section 2 of the playbook.
