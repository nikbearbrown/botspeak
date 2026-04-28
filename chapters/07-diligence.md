# Chapter 7 — Diligence
*What Happens When the Work Recurs*

*A process does not hold still. The model changes. The world changes. The use case expands. Any of these, unmonitored, can turn a well-designed workflow into a broken one while every individual actor in the system behaves exactly as they did on day one.*

---

Here is a question worth sitting with before we get into the machinery.

When a process goes wrong — not spectacularly, not all at once, but slowly, over months, in ways nobody noticed — who is responsible?

The answer, in most organizations that have added AI to a recurring workflow, is: everyone and no one. Everyone had a role. No one owned the outcome. And the reason that answer keeps occurring is not bad luck, and not malice, and not negligence in any particular person's individual actions. It is a structural problem — a predictable consequence of how AI gets introduced into ongoing work — and it has a tractable fix that almost nobody has put in place.

That fix is what this chapter is about. But I want to start with the mechanism, because you cannot defend against what you cannot name.

---

## Things that drift

Here is the concrete case. A midsize software company spends February setting up an AI tool to do first-pass screening of engineering résumés. The setup team tests it against a sample. The results, on that sample, look indistinguishable from what the recruiting team would have done — a little faster, a little more consistent. The team approves it. The tool goes into the daily workflow.

Nine months later, an audit finds that the tool has been under-scoring résumés from community college applicants, and that the under-scoring correlates with demographic patterns the team had explicitly decided to avoid.

The HR lead wants to know who introduced the bias. The investigation finds that nobody did. Nobody changed the tool. Nobody changed the rubric. Nobody changed the workflow. What actually happened was *all of the following*, simultaneously, slowly:

In May, the model vendor pushed an update. The update changed the way the model weighted certain résumé features. The change was small. It was not announced in any detail. The new weighting happened to be more sensitive to a signal that, in this company's particular applicant pool, correlated with community college attendance. Nobody chose this. Nobody noticed it. The model just got slightly different, and the difference accumulated. That is **model drift**.

In March, the company had pivoted to recruit more aggressively from non-traditional engineering pipelines. The pool of applicants hitting the screening tool in October looked structurally different from the pool in February. The rubric had been designed and validated against February's pool. Nobody re-validated it against October's. The assumptions baked into the specification no longer matched the world the specification was operating in. That is **context drift**.

In July, a recruiter who had not been part of the original setup started using the tool to screen for junior engineering roles. The original tool had been designed for senior roles. The criteria for junior roles are different — you are not supposed to penalize a candidate for missing experience that nobody expects them to have yet. The tool was applying senior-role criteria to junior-role candidates, and the junior-role candidates were getting scored down for the wrong reasons. Nobody had re-spec'd the tool for the new use case. Nobody had told the July recruiter that the tool was not designed for this. That is **use case drift**.

<!-- → [INFOGRAPHIC: Timeline of the screening tool case — horizontal axis showing February through November; three labeled drift events marked at their month of origin (model drift: May, context drift: March, use case drift: July) with arrows showing how each accumulates silently until the audit in November; student should see that no single event caused the failure — the compounding did] -->

Three drifts. Each one, on its own, might have been small enough to miss. Together, and compounding over nine months, they broke the process in a way that harmed real applicants. And not one of them required anyone to make a wrong decision.

This is the important structural fact about recurring AI-assisted work: the process does not hold still. The model changes. The world changes. The use case expands. Any of these, unmonitored, can turn a well-designed workflow into a broken one while every individual actor in the system behaves exactly as they did on day one.

---

## Why nobody is accountable

The HR lead, faced with the audit, has a second problem on top of the first. Not only did the process fail — she cannot find the locus of the failure in any single person's decision. And when she tries to change the process going forward, she discovers she cannot find who owns it.

This is not an accident. There are three mechanisms that routinely obscure accountability when AI is in a recurring workflow, and understanding them is what makes it possible to design against them.

The first is **process laundering**. When an AI produces an output and a human approves it, accountability for the output distributes in a way that lets everyone tell a true and exculpatory story. The human approver says: the AI produced it; I just reviewed it. The AI vendor says: we provide a tool; the customer is responsible for appropriate use. The original setup team says: we set it up correctly in February; what happened after wasn't our responsibility. Every statement is accurate. Together, they produce a situation in which no one is accountable, even though every output had a human signature somewhere in its chain.

You will recognize process laundering in any post-incident conversation where every participant can give a complete, accurate account of their own role and still leave the cause of the problem unexplained. The fix is not to assign blame retroactively. The fix is to name, *in advance*, a single accountable human for each significant recurring AI-assisted process — the person whose job includes monitoring whether the process is still working, not just using it.

The second mechanism is **tool diffusion**. When a tool works, it spreads. The recruiter in July picked up the screening tool because it seemed useful and nobody told her not to. This is a rational thing for an individual to do. The aggregate effect, across a team or an organization, is that the original specification loses authority. New users are operating with partial, possibly garbled, possibly outdated understandings of what the tool was designed for. The original setup team may not know who is using the tool now. The use case has evolved without the specification evolving with it.

The fix is not to lock down tools or require formal approval for every extension. The fix is to maintain a *living document* for each significant AI-assisted process: who set it up, what it was designed for, what it was explicitly *not* designed for, who is currently using it, and who to talk to before extending it to a new use case. The document is cheap to maintain and expensive not to have.

The third mechanism is **the verification gap**. In most workflows, checking whether the process is still working is someone's responsibility in general and no one's in particular. The recruiter assumes the setup team is monitoring for problems. The setup team assumes the recruiters would say something if they noticed an issue. The result is that systematic verification doesn't happen — only reactive verification, after something goes wrong loudly enough to force attention.

The verification gap closes only one way: scheduled checks, with dates and owners, on someone's calendar. Not an aspiration. Not a norm. A calendar entry that recurs and has a name attached to it.

---

## The four components

There is a protocol that defeats all three mechanisms. I want to give it to you in the most concrete terms I can, because the value is not in the theory but in actually running it.

**A documented specification.** The first component is a document that answers: What does this process do? On what inputs? Producing what outputs? For what use case? Validated against what? Approved by whom? The document is accessible to everyone who uses or manages the process. When a new colleague joins and starts using the tool, she reads the spec first. When the use case changes — when someone wants to extend the tool from senior-role screening to junior-role screening — the spec is updated formally, not silently, and the update triggers re-validation.

Without the documented specification, you do not know what the process was supposed to do, which means you have no baseline to check drift against. The spec is the foundation.

**Drift checks on a schedule.** The second component is a set of known inputs — a test set, a benchmark, a sample of historical cases where you know what the right output is — that you re-run against the process on a fixed schedule. Once a month, once a quarter, calibrated to the stakes and the pace of change.

The drift check answers: has the process changed? Are outputs still meeting the criteria the workflow depends on? If the outputs have changed, what changed — the model, the data, the use case? The answers get documented. If the drift is small and benign, you note it and continue. If the drift is significant, you investigate before the accumulation turns into an audit finding.

**Outcome audits.** The third component is a periodic look at the *downstream consequences* of the process — not just the immediate outputs, but the outcomes those outputs produce — broken down by whatever attributes matter for fairness, accuracy, and quality.

For the screening tool, this meant: look at the screening outcomes by applicant demographics, by education type, by application channel. Are some groups systematically scoring differently than you would expect? Is the distribution shifting over time? The outcome audit is the check that model-drift-on-test-sets can miss: a model might produce the right outputs on your benchmark while producing different outputs on the actual distribution it operates on. The outcome audit catches that.

The screening company should have been running this audit monthly. They were not. When the audit eventually happened, it was forced by an unrelated complaint — which is the worst time for an audit.

**A named accountable human.** The fourth component is the one that holds the other three together. One person whose job description includes maintaining this process — not just using it. The person whose name is in the spec as the process owner. The person who has the drift checks and outcome audits on their calendar. The person who is on the hook when the process fails, and who therefore has a personal incentive to make sure it does not.

The named owner does not have to be the most senior person in the room. She has to be someone with the time, the access, and the authority to actually do the work. She has to know she owns it. And the organizational structure has to treat ownership as a real accountability, not a nominal one.

<!-- → [TABLE: The four diligence components — columns: Component, What it answers, What it prevents, How often, Who owns it; rows: Documented specification, Drift checks, Outcome audits, Named accountable human — student should be able to use this as a setup checklist when deploying any recurring AI-assisted workflow] -->

Four components. None of them is technically sophisticated. Each of them is, in most organizations, missing for most AI-assisted processes.

---

## What diligence is actually for

I want to make a stronger claim than "diligence helps you catch problems early," because while that is true, it undersells what the four components actually do.

Diligence is primarily about defensibility.

Here is what I mean. When a process fails — and processes fail; the question is when, not whether — the consequential question is not who to blame. The consequential question is: what do we change, and how quickly, and how do we address the harm that already happened? Getting good answers to those questions requires knowing what the process was supposed to do, how it deviated, when the deviation started, and why nobody caught it.

A process running the four diligence components can answer all of those questions. Here is the spec. Here is the scheduled check that should have caught the drift in June. Here is what we found when we ran it — and here is why we did not flag it, which is a solvable problem. Here is the named owner who will lead the remediation.

A process without the four components produces the screening company's situation: an audit that cannot identify the mechanism, a team that cannot distribute accountability cleanly, and a HR head who either fires someone for a structural problem or fires nobody and leaves the organization with the impression that nothing was wrong.

The four components make the process accountable in a way that protects the people in it. Diligence is not a safeguard against failure. It is a safeguard against organizational confusion when failure happens — and confusion, in my experience, causes more lasting damage than the failure itself.

---

## A note on where you sit in the organization

Most of what I have described assumes you have some authority over the process — that you are the person setting it up, or managing it, or in a position to propose how it should be maintained.

You may not be. You may be one of many users of a process you did not design and do not officially own.

The four components are still available to you, partially. You can document your own use of the tool — what you use it for, what you have learned about its limits, what cases you have found where it performs unexpectedly. You can escalate that documentation to whoever does own the process. You can decline to extend a tool to use cases you know it was not designed for, and explain why.

What you cannot do is force accountability on a process that the organization has not structured to receive it. This is a real constraint. The chapter is not pretending otherwise. What I would say is that the political moment for proposing the four-component protocol is usually after a near-miss, not after everything is running smoothly. Small failures are good opportunities. Large failures are bad opportunities. Get the protocol in place during a small failure, if you can.

And make sure that your own name on a process is on a process you are diligently maintaining. The accountability cuts both ways: the four components protect you as well as holding you to account.

---

## What this chapter does not cover

The three drifts I named — model drift, context drift, use case drift — are not exhaustive. There are others. *Data drift*, where the data the process ingests changes character over time, is related to context drift but distinct; a workflow processing customer feedback will behave differently in a quarter when sentiment is unusually polarized than in a normal quarter. *Regulatory drift*, where the legal environment shifts in ways that change what the process is permitted to do, is real and consequential in domains like hiring, lending, and healthcare.

The four-component protocol handles all of these, because the protocol is not tuned to any specific drift type. The documented specification records what the process was designed for. The drift check detects when outputs are changing. The outcome audit detects when consequences are changing. The named owner decides what to do about it. The mechanism does not care which drift triggered the check.

The next chapter assembles everything from the first half of the book — specification, delegation, verification, diligence — into a single narrated workflow. You will see how the pieces fit together in real time, and where the feedback loops are that the chapter sequence made look linear.

---

*What would change my mind:* If a high-quality empirical study showed that organizations running the four diligence components for a year produced no fewer audit findings than organizations that did not — that the components are decorative rather than functional — the chapter is wrong about the mechanism, and the chapter is wrong. The pattern I have observed runs the other direction. Organizations with the components catch problems earlier, including problems they had no prior reason to anticipate. But the observation is informal.

*Still puzzling:* I do not have a clean answer to who pays for diligence work in organizational terms. The work is real. It takes time. Most organizational budgets do not have a line item for it. The fluent practitioner often ends up doing the diligence work on top of her assigned role rather than as a recognized component of it. I do not have a fix for that.

---

## Exercises

### Warm-up

**1. Name the drift.** For each scenario below, identify which drift type is operating (model drift, context drift, use case drift, data drift, or regulatory drift) and write one sentence explaining the mechanism. *(Tests: ability to distinguish drift types in context.)*

- A company uses an AI tool to flag potentially fraudulent transactions. Six months in, the tool's false-positive rate doubles. Investigation reveals the vendor silently updated the underlying model in the prior quarter.
- A legal team deploys an AI contract-review tool trained on US contracts. A new analyst begins running European vendor agreements through it without telling anyone.
- An AI customer-sentiment tool was validated against reviews from a normal business quarter. It is now running during a product recall, when customer sentiment is structurally angrier than the validation set.

**2. Process laundering, identified.** Reread the description of process laundering. Write the three exculpatory statements — one each from the human approver, the AI vendor, and the original setup team — that together produce the accountability gap. Then write one sentence explaining why each statement is both true and insufficient on its own. *(Tests: retention of the process laundering mechanism and its structural character.)*

**3. The four components, applied.** You are setting up a recurring AI-assisted process: a weekly summary of customer support tickets, delivered every Monday to the product team. For each of the four diligence components, write two to three sentences describing concretely what it looks like for this specific process — not a restatement of the general definition, but the actual artifact, schedule, or role you would create. *(Tests: ability to instantiate abstract components into a specific workflow.)*

---

### Application

**4. Diagnose the screening case.** The screening company was running the four-component protocol incompletely — some components were present in weakened or implicit form, others were absent entirely. For each of the four components, describe whether it was present, absent, or present in a degraded form in the screening company's workflow as described in the chapter. For each absent or degraded component, describe specifically what having it in place would have changed about the outcome. *(Tests: ability to apply the four-component framework as a diagnostic tool, not just a setup checklist.)*

**5. Write a living document.** You are the process owner for an AI tool that generates first-draft project status reports from a shared project-management database, used by eight project managers across two teams. Write the living document for this process. It should include: what the process does and does not do, who set it up and when, who is currently using it, what the process was validated against, what the explicit not-designed-for cases are, who to contact before extending it, and the name and calendar cadence of the scheduled drift check. Aim for one page. *(Tests: ability to produce the actual artifact, not just describe it.)*

**6. Blast radius by drift type.** The chapter claims that "the blast radius of a specification mistake is proportional to how many times the specification runs before someone catches the problem." Apply this claim specifically to context drift. Describe a scenario in which context drift accumulates silently for six months in a high-stakes domain (healthcare, lending, hiring, or safety — your choice), estimate the blast radius using the chapter's framing, and identify the specific diligence component that would have caught the drift earliest if it had been in place. *(Tests: integration of the blast-radius concept from Chapter 1 with the drift mechanics introduced here.)*

---

### Synthesis

**7. The defensibility argument.** The chapter's central claim is that diligence is primarily about defensibility, not early detection. Explain the difference between those two purposes. Then construct a scenario in which the four components catch no problems for a year — the process runs cleanly — but their presence still produces a meaningful organizational benefit. Your scenario should make the defensibility argument concrete rather than abstract. *(Tests: ability to hold the chapter's strongest claim and reason from it rather than from the more obvious early-detection framing.)*

**8. Accountability without authority.** The chapter acknowledges a real constraint: a practitioner who is one of many users of a process she did not design cannot force accountability on a process the organization has not structured to receive it. Describe a specific situation in which this constraint is in play. What can the practitioner actually do within the constraint? What should she escalate, to whom, and when? What should she refuse to do even if instructed? *(Tests: integration of the accountability argument with the organizational-reality section — reasoning about what diligence looks like when you do not own the process.)*

---

### Challenge

**9. The verification gap as a design problem.** The chapter says the verification gap closes only one way: scheduled checks with dates and owners on a calendar. Make the strongest possible argument against this claim — identify a scenario in which calendar-based verification would fail to catch a drift that a different detection mechanism would have caught earlier. Then explain what that scenario implies about how the four-component protocol should be designed, without abandoning the protocol's core logic. *(Tests: ability to stress-test the chapter's claims and reason about their limits — the Feynman move of pushing on what you think you understand.)*

**10. Regulatory drift and the four components.** The chapter names regulatory drift as a real risk in hiring, lending, and healthcare, but does not fully develop it. Choose one of those three domains. Describe a plausible scenario in which regulatory drift — a change in the legal environment — turns a compliant AI-assisted process into a non-compliant one. Identify which of the four diligence components is best positioned to catch this drift, explain what it would need to look like in practice to actually catch it (not the generic version, the domain-specific version), and name what organizational role or function would need to be involved that might not currently be part of a typical AI process-ownership structure. *(Tests: ability to extend the framework into a domain-specific context where the standard instantiation of the components is insufficient.)*
