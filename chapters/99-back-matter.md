# Back Matter

## Acknowledgements

A book like this is mostly other people's thinking, used in ways the original thinkers cannot all be asked about. Where I cite by name, I have tried to do so in the chapter rather than in a list at the back, because a list at the back is the kind of acknowledgement that lets the reader skip noticing whose idea is doing the work.

The voices that are explicit, in the AI Wayback Machine sections at the close of each chapter, are the ones whose work the practitioner can pick up and use directly: Henriette Avram, W. Ross Ashby, Lev Vygotsky, W. Edwards Deming, Mary Parker Follett, Gordon Pask, Abraham Wald, Walter Shewhart, Donella Meadows, Norbert Wiener, Grace Hopper, Barry Turner, Kurt Gödel, Yuen Ren Chao. Read one for every chapter you finish. The book is partly a map for them.

The reading I owe to working practitioners — the engineers, analysts, managers, and graduate students whose composite cases anchor the book's worked examples — cannot be cited individually without violating the trust under which the cases were observed. The patterns are real. The names have been changed, the details composited. Every example is something I watched happen. If a working colleague reading this thinks I am writing about them, I probably am, and I am grateful.

The companion volume *How to Speak Bot* (Brown, existing) provided the pattern library this book points back to in the appendices. The two are designed to be read together — *Botspeak* for the workflow, *How to Speak Bot* for the moves inside it.

---

## Glossary

*The book accretes vocabulary on purpose. Most of these terms are named in the chapter where they earn their place. This is the look-up table — the place the reader returns when a term shows up two chapters after it was defined. Chapter references at the end of each entry point to where the term is unpacked.*

**Accountability gap.** The Automation failure mode in which no human is actively monitoring and no human is on the hook. The failure mode that makes the other three (input drift, output drift, context shift) invisible until something fails loudly. (Ch 10)

**Accountability-obscuring mechanisms, three.** Process laundering, tool diffusion, and the verification gap. The three structural ways accountability disappears in a recurring AI-assisted process even though every individual actor behaves correctly. (Ch 7)

**Accountable Judgment.** Tier 7, the top of the Seven Tiers. Decisions where, if they go wrong, a human has to answer for them. The model can inform; the decision belongs entirely to the human. *See also: Seven Tiers.* (Ch 4)

**Adversarial Conversation Log.** The Chapter 5 portfolio artifact — one real piece of work taken through all four adversarial moves, with time-stamps and findings. (Ch 5)

**Adversarial moves, four.** The four prompts that defeat sycophantic drift: the steelman, the edge-case probe, the assumption surface, and the devil's advocate role assignment. (Ch 5)

**Adversarial test cases.** The second of the three Automation noticing forms — inputs constructed to probe known failure modes, run on a schedule. *See also: Noticing forms, three.* (Ch 9)

**Agency.** The third Mode. The configuration in which the AI takes actions in the world on the practitioner's behalf — sending email, posting, calling APIs, modifying records — not just producing text for a human to act on. The blast radius grows in ways text-only mistakes cannot. *See also: Three structural failures of agentic AI.* (Ch 1, Ch 11)

**Agentic Blast-Radius Decision Aid.** The Chapter 11 portfolio artifact — the four-dimension analysis applied to one specific agentic deployment in the reader's field. (Ch 11)

**AI Fluency.** The discipline of running the Loop on real work with deliberate attention to each step, against a domain in which the practitioner can verify, defend, and own the output. The capacity the book teaches. *See also: AI Literacy, Fluency trap, Ownership Test.* (Ch 0)

**AI Literacy.** The capacity to open a chatbot, type a prompt, read the output, copy and paste. Necessary, not sufficient. The bar most readers have already cleared. (Ch 0)

**AI Use Disclosure.** The four-sentence note the practitioner attaches to AI-assisted work naming what the AI did, what the human did, where the load-bearing judgment was, and who is on the hook. Introduced in Chapter 8 as the artifact that closes the Loop. (Ch 8)

**Ambiguity types, six.** Input-quality variation, output-volume variation, context shifts the model cannot detect, ambiguous inputs, high-stakes outputs, and model-specific failure modes. The six categories of anticipated deviation an Automation specification must address. (Ch 10)

**Ambiguous inputs.** One of the six ambiguity types — the case where the input is internally contradictory and the model will produce output regardless. The handling rule is usually: surface the conflict to a human rather than let the model paper over it. (Ch 10)

**American-in-India metaphor.** The book's operating metaphor for the literacy/fluency gap. The tourist who reads no Hindi at all asks for help and gets on the right train. The tourist who reads some Hindi misreads the board and ends up on the wrong platform. The fluent speaker buys chai. (Ch 0)

**Amplifying offload.** Cognitive offloading that strengthens the practitioner over time — the evaluative role survives the delegation; the judgment muscle keeps firing. *See also: Atrophying offload.* (Ch 4)

**Anticipatory specification.** The discipline of writing an Automation spec before the system runs, explicitly handling the six ambiguity types and the four failure modes — the implicit checks a human would have run in real time, made explicit on the page. (Ch 10)

**Appropriateness tests, three.** Bounded scope; predictable inputs; low blast radius. The five-minute screen before deciding whether a task should be automated at all — or, for an inherited automation, whether it should continue running in current form. (Ch 9)

**Assumption surface.** The third of the four adversarial moves. The prompt that asks the model to list the unstated assumptions an argument is making, label each one (factual, methodological, value-based), and name what would be needed to defend each. Catches invisible premises. (Ch 5)

**Atrophying offload.** Cognitive offloading that weakens the practitioner over time — the evaluative role does not survive the delegation; the muscle goes dormant; three months later the practitioner knows less than they would have working by hand. The default for unexamined daily delegation. *See also: Performance paradox.* (Ch 4)

**Audience criteria.** The DESIGN.md section naming the readability, jargon, evidence, and source-attribution standards the reader's domain demands. *See also: DESIGN.md.* (Ch 6)

**Augmentation.** The first Mode. The configuration in which the human is at the keyboard while the AI runs — every output crosses human eyes before use. The Loop's most forgiving configuration; the configuration in which most of a practitioner's day still happens. (Ch 1)

**Authority.** The first of the four conditions of a functional Human Decision Node. Does the human at the Node have genuine authority to override the AI's output, including by saying no? Theoretical authority does not produce judgment. (Ch 12)

**Automation.** The second Mode. The configuration in which the AI runs without the human present at execution time. The Loop's steps reweight: specification becomes anticipatory, diligence becomes designed-in, discernment becomes sampling + adversarial tests + outcome audits. (Ch 1, Chs 9–10)

**Automation failure modes, four.** Input drift, output drift, context shift, accountability gap. The four failure modes every Automation's Diligence design must address. (Ch 10)

**Automation Inheritance Audit.** The Chapter 9 portfolio artifact — appropriateness tests + drift assessment + noticing protocol + deployment verdict for one automation the reader has inherited or proposes to oversee. (Ch 9)

**Automation Specification.** The Chapter 10 portfolio artifact — one specific automation fully specified, three times the length of the Augmentation equivalent, with the six-ambiguity-type check and the stakeholder defense memo. The most directly deployable single artifact in the portfolio. (Ch 10)

**Baseline Audit.** The Chapter 0 portfolio artifact — an audit of one of the reader's past AI-assisted pieces, applying the four-layer verification frame informally. Paired with the Final Audit at Chapter 13 as before-and-after evidence of fluency. (Chs 0, 13)

**Be Diligent.** The fifth Loop step. Naming what the AI did, what the human did, where the load-bearing judgment was, and who is on the hook. In Augmentation mode, the AI Use Disclosure. In Automation, the four-component Diligence protocol. (Ch 1, Ch 7)

**Blast radius.** The reach of an error if the AI gets the work wrong. In Augmentation, bounded by what the practitioner reviews and approves. In Automation, scales with time-to-detection. In Agency, has four dimensions: stakeholder reach, reversibility, identity verification, and escalation pathway. *See also: Blast-radius dimensions, four.* (Chs 1, 9, 11)

**Blast-radius dimensions, four.** The four axes used to assess any agentic deployment: stakeholder reach (whose interests are affected if the agent acts incorrectly), reversibility (can the action be undone), identity verification (does the agent know whose authority it acts on), escalation pathway (what does the agent do when uncertain). (Ch 11)

**Bounded scope.** The first appropriateness test. Can the task be described in one paragraph that the practitioner would defend to a manager? If the task is not bounded, the model will be making scope decisions in real time it has not been authorized to make. (Ch 9)

**Capacities, Nine.** Strategic Delegation, Effective Communication, Critical Evaluation, Technical Understanding, Ethical Reasoning, Stochastic Reasoning, Learning by Doing, Rapid Prototyping, Theoretical Foundations. The cognitive abilities the Loop draws on, each named by diagnostic question and located on a durability spectrum. (Ch 2)

**CLAUDE.md.** The reader's living coding/process constitution. Accretes rules across chapters as the book gives the reader reasons to add them. Travels to every new role and every new AI tool. *See also: Governing files, three.* (Chs 1, 3, 4, 5, 6, 7, 9, 10, 12)

**Cognitive offloading.** Moving mental work from inside the head to a system outside the head. Scratch paper is offloading; a to-do list is offloading; a calculator is offloading. AI tools offload at a scale qualitatively different from anything before. *See also: Amplifying offload, Atrophying offload.* (Ch 4)

**Confidence-correctness gap.** The distance between how confident an AI output sounds and how likely it is to be correct. The model's tone reflects how typical the output looks; it does not reflect accuracy. The heuristic that works on human sources does not transfer. (Ch 6)

**Constraints.** The second of the five Specification components. The format, length, source, and audience limits the output has to fit inside. The parts of the specification the model would otherwise guess at. (Ch 3)

**Contestable Analysis.** Tier 6 of the Seven Tiers. Problems where reasonable practitioners would genuinely disagree. The model can assemble components; the call belongs to the human. *See also: Seven Tiers.* (Ch 4)

**Context drift.** One of the three drift forms. The world the recurring process operates in has changed in ways the system has no access to — new entrants, new regulations, new audience composition. Caught by outcome audits, not by benchmark re-runs. (Ch 7)

**Context shift.** Two uses. (1) One of the six ambiguity types — what the system does when the world has changed in ways the model cannot detect. (2) One of the four Automation failure modes — the recurring version of the same problem. (Chs 10, 7)

**Converse.** The third Loop step. The iterative refinement that turns a first draft into something the practitioner can stand behind, including the four adversarial moves. The Conversation chapter teaches this step. *See also: Adversarial moves, four.* (Chs 1, 5)

**Cover Memo.** The single most important artifact in the finished portfolio — the one-page cover letter at the front of the portfolio addressed to a reader who has never heard of *Botspeak*. Drafted at Chapter 13. (Ch 13)

**Critical Evaluation.** One of the Nine Capacities. Reading AI output for what kind of error it might contain, not just whether it sounds right. Contested in durability — models are improving at calibrated self-doubt. (Ch 2)

**Decision Node.** *See: Human Decision Node.*

**Delegate.** The second Loop step. Deciding what the model will do and what the human will do, before the work begins. *See also: Seven Tiers, Delegation Map.* (Chs 1, 4)

**Delegation Map.** The second half of the Practitioner Profile — the reader's tasks located on the Seven Tiers, the four delegation questions answered per task, the amplify/atrophy assessment, the named-skill at quiet-atrophy risk. (Ch 4)

**Delegation questions, four.** What capacity does this task build, and do I need to keep building it? What is the blast radius if the AI gets this wrong? Who is accountable, and do they know how the work was produced? What does the model not know that I do, and have I made sure that part stays in? (Ch 4)

**DESIGN.md.** The reader's living output-quality constitution. Names the verification standard, the voice and register the domain expects, the audience criteria, the maintenance and ownership criteria, the agentic stakeholder-model criteria, and the HITL design standards. *See also: Governing files, three.* (Chs 6, 7, 11, 12)

**Devil's advocate role assignment.** The fourth of the four adversarial moves. The instruction that puts the model into a sustained oppositional persona rather than asking for discrete pushback. Catches integration failures the discrete probes miss. (Ch 5)

**Diligence.** The fifth Loop step, expanded in Chapter 7. What happens between executions of recurring work: the documented spec, the scheduled drift check, the outcome audit, the named accountable human. Diligence is primarily about defensibility — the practice that makes a failure auditable when it eventually happens. (Ch 7)

**Diligence components, four.** Documented specification; drift checks on a schedule; outcome audits; named accountable human. The protocol that defeats the three accountability-obscuring mechanisms. (Ch 7)

**Diligence Framework Applied.** The Chapter 7 portfolio artifact — the four-component protocol walked against one specific AI-assisted system the reader uses, owns, or works alongside. (Ch 7)

**Discern.** The fourth Loop step. Reading the output for what kind of error it might contain, calibrating verification effort to stakes. The Discernment chapter teaches this step. *See also: Verification layers, four; Verification tiers, four.* (Chs 1, 6)

**Documented specification.** The first of the four diligence components. The document that answers what the process does, on what inputs, producing what outputs, for what use case, validated against what, approved by whom. Without it, there is no baseline to check drift against. (Ch 7)

**Drafting in Your Voice.** Tier 4 of the Seven Tiers. The model produces a draft; the practitioner revises. The Tier-specific risk is voice drift over months — the practitioner's writing migrating toward the model's defaults. *See also: Seven Tiers.* (Ch 4)

**Drift forms, three.** Model drift (the model changed), context drift (the world changed), use case drift (the task changed). The three ways recurring AI-assisted work degrades quietly. (Ch 7)

**Edge-case probe.** The second of the four adversarial moves. The prompt that asks the model to construct three specific scenarios in which an argument or recommendation fails. Catches scope error. (Ch 5)

**Effective Communication.** One of the Nine Capacities. Telling the model what it actually needs to know — intent, constraints, audience, success criteria. When this fails, the model fills in blanks with its best guess. (Ch 2)

**End-to-End Case Study.** The Chapter 8 keystone portfolio artifact. One complete piece of the reader's own work taken from intent through delivery, every Loop step documented, every adversarial move logged, every verification layer applied, every disclosure attached. The gravitational center of Layer B. (Ch 8)

**Escalation pathway.** The fourth blast-radius dimension. When the agent encounters a situation outside the scope of its explicit instructions, what does it do — guess and act, or surface to a human and wait? If the answer is the former, the blast radius is whatever the agent can reach with its tools. (Ch 11)

**Ethical Reasoning.** One of the Nine Capacities. Noticing when a use case has stakeholders other than the practitioner and the AI, and acting on that noticing. Durably the human's responsibility — accountability cannot be delegated to a model. (Ch 2)

**Exclusions.** The fourth of the five Specification components. What the model is not supposed to do. The specification saying: please leave that blank blank. (Ch 3)

**External.** Tier C of the four-tier verification protocol. Work going to a client, a regulator, a public audience, a senior stakeholder — anything that publishes. Run all four verification layers. The tier most consequential to most practitioners. *See also: Verification tiers, four.* (Ch 6)

**Fact.** The first of the four verification layers. Are the specific factual claims true — citations real, numbers accurate, attributions correct, quotes actually said? Most users vaguely understand they should run this layer. Execution is what gets skipped under time pressure. (Ch 6)

**Failure-mode handling.** The Automation specification section naming what the system does when generation fails, when output exceeds format constraints, when hallucinated citations are detected. (Ch 10)

**Final Audit.** The Chapter 13 portfolio artifact paired with the Chapter 0 Baseline Audit. The same piece of past work, audited again, by the same person, separated by the book. The cleanest single comparison the portfolio offers. (Chs 13, 0)

**Five-component specification.** *See: Specification components, five.*

**Fluency.** *See: AI Fluency.*

**Fluency trap.** The academic term for what happens when fluent output triggers an evaluation booster — readers trust well-written prose more than the evidence warrants. The fabricated citation is the visible symptom; the trust-in-fluency is the mechanism. (Ch 0)

**Four-layer verification.** *See: Verification layers, four.*

**Four-tier verification protocol.** *See: Verification tiers, four.*

**Framing.** The third of the four verification layers. Even when the facts are right and the reasoning is sound, the model made a choice about how to organize the analysis. Was it the right frame? Would a thoughtful expert in the domain have reached for a different one? (Ch 6)

**Generation rules.** The Automation specification section naming the per-item structure, confidence labels, format constraints, and quality criteria the model must produce against. (Ch 10)

**Governing files, three.** `CLAUDE.md`, `DESIGN.md`, and the `PROJECT.md` template. The three living files at the spine of the portfolio. Accrete across the book; travel to every new role. *See also: Portfolio.* (Chs 1, 3, 6, plus updates across most chapters)

**Hindi-tourist metaphor.** *See: American-in-India metaphor.*

**High-stakes outputs.** One of the six ambiguity types. Some outputs, as special cases, are more consequential than the design baseline. The right response is usually to detect them and halt, not handle them within the automation. (Ch 10)

**High Stakes / Irreversible.** Tier D of the four-tier verification protocol. Medical, legal, and financial decisions of real consequence. Anything where being wrong harms someone. At this tier, the verification is not a check on the output; it is the practice that makes the decision defensible. *See also: Verification tiers, four.* (Ch 6, Ch 12)

**Human Decision Node.** A designed point in an autonomous workflow where a human is required to take responsibility for the action about to happen. The architectural acknowledgment that some decisions cannot be delegated. Functional only when all four conditions (authority, information, time, accountability) are real. *See also: Human Decision Node, four conditions of.* (Ch 12)

**Human Decision Node, four conditions of.** Authority, information, time, accountability. All four must be real, or the Node — regardless of its form — is a signature waiting to happen. (Ch 12)

**Human-in-the-Loop Protocol.** The Chapter 12 portfolio artifact — the four-condition test applied to one Decision Node in the reader's work, plus the compressed adversarial spiral, plus an end-to-end worked example of an agentic deployment with the honest automation-rate finding. (Ch 12)

**Identity verification.** The third blast-radius dimension. Does the agent know whose authority it is acting on, and is that authority legitimate? The primary attack vector in adversarial environments. (Ch 11)

**Information.** The second of the four conditions of a functional Human Decision Node. Does the human at the Node have enough information to make a judgment, including information the AI did not surface? If the human can only see what the AI showed, they are approving the AI's framing, not judging. (Ch 12)

**Input drift.** One of the four Automation failure modes. The inputs to the system are no longer representative of the inputs it was designed for. Sources reliable in February less reliable in October. (Ch 10)

**Input-quality variation.** The first of the six ambiguity types. What the system does when an input is degraded, missing, or formatted differently than expected. (Ch 10)

**Intent.** The first of the five Specification components. Not the immediate task but the goal the task serves. What the practitioner is trying to do, named in advance, so the model and the practitioner share a definition of success. (Ch 3)

**Judgment Under Structure.** Tier 5 of the Seven Tiers. The practitioner authors the framework; the model applies it. Delegate the application; keep the authorship. *See also: Seven Tiers.* (Ch 4)

**Layer A.** Field-agnostic infrastructure. The three governing files and the customized framework templates. Same structure for every reader regardless of domain. *See also: Layer B, Portfolio.* (Throughout)

**Layer B.** Field-specific deliverables. The reader's actual work, annotated with the prompts that generated drafts and the verifications that approved them. The keystone Case Study is the largest Layer B artifact. *See also: Layer A, Portfolio.* (Throughout)

**Learning by Doing.** One of the Nine Capacities. Using AI in ways that amplify skills rather than replace them. Durably the human's responsibility — the practitioner has a body and a daily routine; the model does not. (Ch 2)

**Literacy.** *See: AI Literacy.*

**Loop, the.** Specify → Delegate → Converse → Discern → Be Diligent. Five steps, run as a cycle, with loop-back arrows where Discernment surfaces a problem with Specification. The book's central practitioner workflow. (Ch 1; runs through every chapter)

**Loop-back.** The return arrow from a later Loop step to an earlier one — usually Discernment back to Specification — when the work itself reveals that the earlier decision was wrong. The structural feature that distinguishes running the Loop from following it. (Ch 8)

**Low blast radius.** The third of the three appropriateness tests. If the system fails continuously for weeks before anyone notices, is the accumulated damage manageable? If not, either do not automate or design explicit human checkpoints in. (Ch 9)

**Mechanical Execution.** Tier 1 of the Seven Tiers. Tasks where the right answer is fully determined and doing it by hand builds no judgment worth keeping. Delegate freely. *See also: Seven Tiers.* (Ch 4)

**Meet Priya.** The one-page front-matter page that introduces the protagonist and names the broader audience. *See also: Priya Banksy.*

**Model drift.** One of the three drift forms. The model the recurring process runs on has changed — vendor update, fine-tuning, capability shift — producing different outputs on matching inputs. Caught by monthly fixed-test re-runs. (Ch 7)

**Model-specific failure modes.** One of the six ambiguity types. What the system does when the model hallucinates, refuses, or produces output that breaks the format spec. (Ch 10)

**Modes, Three.** Augmentation, Automation, Agency. The three relationships between human and AI. The Loop runs in each mode, and the steps reweight as the mode changes. *See also: Augmentation, Automation, Agency.* (Ch 1)

**Named accountable human.** The fourth of the four diligence components. One person whose job description includes maintaining the process — not just using it — with recurring review on their calendar. The fix for process laundering and the verification gap. (Ch 7)

**Nine Capacities.** *See: Capacities, Nine.*

**90-Day Plan.** The Chapter 13 portfolio artifact — two capacities, three commitments per capacity (daily rep, weekly review, 90-day artifact). The forward-looking piece of the portfolio. Scheduled on the calendar before the chapter closes. (Ch 13)

**No deliberation surface.** The third of the three structural failures of agentic AI. The agent has no social or temporal slowdown between deciding and executing — no thinking out loud, no colleague check, no sleeping on it. *See also: Three structural failures of agentic AI.* (Ch 11)

**No self-model.** The second of the three structural failures of agentic AI. The agent has no reliable internal signal for when an action is categorically out of proportion to the task it was given. *See also: Three structural failures of agentic AI.* (Ch 11)

**No stakeholder model.** The first of the three structural failures of agentic AI. The agent has no implicit map of whose interests matter in any given action. The explicit list of stakeholders the practitioner writes in will always be incomplete. *See also: Three structural failures of agentic AI.* (Ch 11)

**Noticing forms, three.** Sampling; adversarial test cases; outcome auditing. The three practices that replace real-time discernment when the human is not present at execution. (Ch 9)

**Omission.** The fourth and hardest of the four verification layers. Of all the things that are true about the topic, the model said some of them and not others — which unsaid things matter? Requires domain knowledge the output doesn't contain. The layer most often skipped and the one most expensive to fail at. (Ch 6)

**Operational.** Tier B of the four-tier verification protocol. Internal memos, non-production code, personal decisions. Run Layer 1 on specific claims; run Layer 2 on the main reasoning; take a quick pass at Layer 4. *See also: Verification tiers, four.* (Ch 6)

**Outcome auditing.** The third of the three Automation noticing forms — and the third of the four diligence components. Periodic review of what the system produced against what actually turned out to be true, broken down by the attributes that matter. (Chs 7, 9)

**Output drift.** One of the four Automation failure modes. The model is producing different outputs than it did at setup, given matching inputs. Caught by a fixed test set re-run on schedule. (Ch 10)

**Output format.** The fifth of the five Specification components. The structural shape of the deliverable — markdown or plain text, bullets or prose, sections and headers. Not a detail. The format constrains the kind of thinking the model does. (Ch 3)

**Output-volume variation.** One of the six ambiguity types. What the system does when the output is substantially longer or shorter than the design case. (Ch 10)

**Ownership Test.** The closing test the practitioner runs on themselves after the four adversarial moves and the verification pass: can I defend every paragraph to a hostile reviewer asking where it came from and why I stand behind it? If not, either learn the paragraph or cut it. (Ch 5)

**Pattern-Matching with Feedback.** Tier 2 of the Seven Tiers. Tasks where the right answer is well-defined but recognizing wrong answers requires domain knowledge. Delegate the generation; keep the evaluation. *See also: Seven Tiers.* (Ch 4)

**Performance paradox.** The phenomenon where a practitioner's daily output gets faster and more polished after adopting AI tools while their underlying judgment quietly atrophies. Visible only when something happens that the model has no signal for. *See also: Atrophying offload.* (Ch 4)

**Portfolio.** The reader's accreted record of fluency, assembled across the book. Three governing files plus customized frameworks plus field-specific deliverables plus diagnostics, fronted by the Cover Memo. Seventeen artifacts in five sections. The thing the practitioner hands to a future reader instead of arguing for their fluency. *See also: Cover Memo, Layer A, Layer B.* (Throughout; structurally named in Ch 0 and Ch 13)

**Practitioner Profile.** The Chapter 2 + Chapter 4 portfolio artifact (consolidated). Half capacities self-assessment, half delegation map. One of the three diagnostic artifacts in the finished portfolio. (Chs 2, 4)

**Pre-flight checks.** The Automation specification section naming what the system verifies before generation — for example, querying retraction pages, flagging articles older than the freshness window, refusing to generate when input quality drops below threshold. (Ch 10)

**Predictable inputs.** The second of the three appropriateness tests. Are the inputs the system will receive within a known range the design cases represented? The question is not whether the typical input is predictable; the question is whether the atypical inputs are represented. (Ch 9)

**Priya Banksy.** The book's single protagonist — 29 years old, BA Mass Communication from Symbiosis Institute of Media & Communication (Pune), AI Content Strategist at a US digital publication on her first year of OPT. Her arc runs from six months in (Chapter 0) to three years in (Chapter 13). Worked example, not template. The reader's field is the actual subject.

**Process laundering.** The first of the three accountability-obscuring mechanisms. When an AI produces an output and a human approves it, accountability distributes such that every participant can give an accurate exculpatory account and the cause of failure goes unexplained. Fixed by the named accountable human. (Ch 7)

**PROJECT.md.** The per-project state file with two layers — intent (what the project means, who it serves, what success looks like) and technical (what is built, what is generated and accepted versus rejected, what is verified). Instantiated for every significant Layer B deliverable. *See also: Governing files, three.* (Ch 3, instantiated at Ch 8)

**Rapid Prototyping.** One of the Nine Capacities. Treating model output as a draft to be tested in the world, not as the work itself. (Ch 2)

**Reasoning.** The second of the four verification layers. Given the facts, does the conclusion follow? Is there a skipped step, an unstated premise, a move that would not survive being written out explicitly? Harder than fact because the fault is structural. (Ch 6)

**Reversibility.** The second blast-radius dimension. Can the action be undone? The single most consequential dimension — a reversible mistake is a problem; an irreversible mistake is a catastrophe. (Ch 11)

**Role Dossier.** The one-paragraph file the reader writes at Chapter 0 naming their role, their typical tasks, their stakeholders, and the AI use in their current workflow. Attached to the reader's Claude Project so every future chapter exercise inherits the role context. (Ch 0)

**Role-and-rubric pattern.** The compressed structure introduced in Chapter 3 — assigning the model a specific professional persona plus explicit judgment criteria. A scaffold for the five Specification components, not a substitute. (Ch 3)

**Sampling.** The first of the three Automation noticing forms — reading a fraction of the outputs in full on a scheduled basis. Does not catch every failure; catches the persistent ones, which are most of the failures that matter. (Ch 9)

**Self-model.** *See: No self-model.*

**Seven Tiers.** Mechanical Execution → Pattern-Matching with Feedback → Synthesis from Sources → Drafting in Your Voice → Judgment Under Structure → Contestable Analysis → Accountable Judgment. The delegation-diagnostic taxonomy. Decompose a complex task, locate each component on the Tiers, hand over the bottom, partner on the middle, keep the top. (Ch 4)

**Specification.** Two senses. (1) The first Loop step — the thinking the practitioner does before opening the tool. (2) The five-component artifact that documents the thinking. The prompt is the document recording the specification, not the specification itself. *See also: Specification components, five.* (Ch 3)

**Specification components, five.** Intent, constraints, success criteria, exclusions, output format. The components every working specification carries, made explicit. (Ch 3)

**Specification Library.** The Chapter 3 portfolio artifact — five templates, one per recurring task type in the reader's role, each with a worked example. (Ch 3)

**Specify.** The first Loop step. *See also: Specification, Specification components, five.* (Chs 1, 3)

**Stakeholder model.** *See: No stakeholder model.*

**Stakeholder reach.** The first blast-radius dimension. Whose interests are affected if the agent acts incorrectly — yours, your team's, your customers', people who never heard of you? Constraining the agent's privileges is one of the few reliable blast-radius defenses available before any code runs. (Ch 11)

**Steelman.** The first and most powerful of the four adversarial moves. The prompt that asks the model to construct the strongest possible argument against a position. Catches directional error. The single move to deploy on any work the practitioner has spent more than twenty minutes building in conversation. (Ch 5)

**Still puzzling.** The chapter-end commitment naming what the author does not yet fully understand. Feynman's move. The pair to *What would change my mind.* (Throughout)

**Stochastic Reasoning.** One of the Nine Capacities. Handling uncertainty honestly — the practitioner's, the model's, the world's. Contested in durability — models are improving at calibrated uncertainty quantification in narrow domains. (Ch 2)

**Strategic Delegation.** One of the Nine Capacities. Deciding, before beginning, what the model should do and what the practitioner should do, and why. Durably the human's responsibility — accountability cannot be delegated to a model. (Ch 2)

**Success criteria.** The third of the five Specification components. How the practitioner will know, after the fact, that the output is good — the recipient action or test the output has to pass. (Ch 3)

**Sycophantic drift.** The failure mode in which an AI conversation moves the whole way in one direction because the practitioner is framing and the model has been trained to develop the position the user supplies. Not a moment; a direction. Defeated by the four adversarial moves. (Ch 5)

**Synthesis from Sources.** Tier 3 of the Seven Tiers. The model gathers and combines information from multiple sources; the practitioner evaluates. The Tier-specific risk is omission — the synthesis tells you what the sources say but not what the sources do not say. *See also: Seven Tiers, Performance paradox.* (Ch 4)

**Technical Understanding.** One of the Nine Capacities. Knowing enough about how the system works to predict where it will fail. Practitioner depth, not research depth. (Ch 2)

**Theoretical Foundations.** One of the Nine Capacities. Keeping enough domain knowledge to judge whether AI output is good. Without it, the practitioner is not collaborating with the model — they are taking dictation. (Ch 2)

**Three structural failures of agentic AI.** No stakeholder model; no self-model; no deliberation surface. Not three separate bugs — three faces of one underlying gap: judgment. (Ch 11)

**Tiers, Seven.** *See: Seven Tiers.*

**Time.** The third of the four conditions of a functional Human Decision Node. Does the human have enough time to actually use the information and authority they have? The most frequently violated and most quietly violated condition. (Ch 12)

**Tool diffusion.** The second of the three accountability-obscuring mechanisms. When a tool works, it spreads — secondary users adopt it with partial understanding of what it was designed for. Fixed by a living document the tool's owner maintains. (Ch 7)

**Translate before you move on.** The chapter-end block in every Botspeak chapter. The explicit prompt asking the reader to name their domain's equivalent of Priya's case and to produce the chapter's portfolio artifact in their own field. The book's "fluency in your field" thesis made operational. (Throughout)

**Trivial.** Tier A of the four-tier verification protocol. Drafts the practitioner will edit, brainstorms, throwaway code. Verify at Layer 1 on specific claims if at all. *See also: Verification tiers, four.* (Ch 6)

**Use case drift.** One of the three drift forms. The task the recurring process is being applied to has expanded beyond what the original spec covered. A tool built for one beat used quietly on another. (Ch 7)

**Verification gap.** The third of the three accountability-obscuring mechanisms. Checking whether the process is still working is someone's responsibility in general and no one's in particular. Closes only one way: scheduled checks with dates and owners on a calendar. (Ch 7)

**Verification layers, four.** Fact, reasoning, framing, omission. The four kinds of error and the four checks that catch them. Roughly increasing in difficulty; most practitioners run only the first. *See also: Verification tiers, four.* (Ch 6)

**Verification tiers, four.** Trivial (drafts), Operational (internal memos), External (anything that publishes), High Stakes / Irreversible (medical, legal, financial, named harm). Verification effort scales with what the practitioner has to lose. *See also: Verification layers, four.* (Ch 6)

**Verification standard.** The DESIGN.md section naming the quality bar any output must clear before it leaves the practitioner's hands. *See also: DESIGN.md.* (Ch 6)

**Voice and register.** The DESIGN.md section naming what the practitioner's domain expects of their outputs — what tells a reader the work was done by someone in this field, to this field's standard. *See also: DESIGN.md.* (Ch 6)

**What would change my mind.** The chapter-end commitment naming the specific evidence or argument that would cause the chapter's reading to revise. The pair to *Still puzzling.* (Throughout)

**Worked Loop Log.** The Chapter 1 portfolio artifact — one recent piece of the reader's work taken through all five Loop steps with time-stamps. The first piece of evidence that prefigures the Chapter 8 keystone. (Ch 1)

---

## About the author

Nik Bear Brown writes textbooks for working professionals in fields where the working consensus is moving faster than the published consensus — AI fluency, computational finance, computational skepticism, the design of agentic systems. The books are written for the practitioner who has to do the work on Monday morning, not the academic researcher who has the year.

The voice across the books is consistent: explanation over assertion, mechanism over name, calibrated uncertainty over false confidence. If a chapter cites an authority by reference rather than as an instrument under test, the chapter is not yet doing the method.

---

## Colophon

*Botspeak* was drafted in markdown using the Feynman-flavored editorial method described in the workshop's `CLAUDE.md`. Source was version-controlled. Chapters were drafted, reviewed against working-practitioner cases, and revised before any chapter shipped. The book is set in the typeface your reader chose for it.

The figures are intentionally austere — monochrome warm grayscale, serif type, no rounded corners, no shadows, no color highlights. The design choice is editorial: the reader's attention should fall on what the figure shows, not on how the figure presents itself.

The AI Wayback Machine sections close each chapter with a contemporary tool — a prompt to a large language model — pointed at a thinker whose foundational work is older than the millennium. The pairing is deliberate. The point is not nostalgia. The point is that the practitioner who can run a useful prompt about Vygotsky has already done part of the practice the book is teaching.

---

## A note on revision

This is a first edition. The field is moving fast enough that some specific tool or technique in this book will be obsolete before many readers finish it. The Loop will not be obsolete. The Capacities will not be obsolete. The ability to separate your contribution from the model's, and stand behind your contribution on your own authority, will not be obsolete — it will become more valuable as the field matures.

If a chapter's reading is wrong, the corrigenda live at the workshop's repository.

— *End of book.*

