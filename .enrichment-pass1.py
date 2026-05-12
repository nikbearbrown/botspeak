#!/usr/bin/env python3
"""Pass 1 — Render TABLE comments to markdown tables. In-place edit."""
import re, os, sys
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# (filename, comment_substring_to_match, replacement_block)
# A comment_substring_to_match is a unique fragment of the [TABLE: ...] comment
# that distinguishes it from any other in the same file.

REPLACEMENTS = []

# === Ch 02 — Self-assessment grid ===
ch02_table = """| Capacity | Untrained | Aware | Practicing | Fluent | Notes |
|---|:---:|:---:|:---:|:---:|---|
| **Strategic Delegation** | ☐ | ☐ | ☐ | ☐ |  |
| **Effective Communication** | ☐ | ☐ | ☐ | ☐ |  |
| **Critical Evaluation** | ☐ | ☐ | ☐ | ☐ |  |
| **Technical Understanding** | ☐ | ☐ | ☐ | ☐ |  |
| **Ethical Reasoning** | ☐ | ☐ | ☐ | ☐ |  |
| **Stochastic Reasoning** | ☐ | ☐ | ☐ | ☐ |  |
| **Learning by Doing** | ☐ | ☐ | ☐ | ☐ |  |
| **Rapid Prototyping** | ☐ | ☐ | ☐ | ☐ |  |
| **Theoretical Foundations** | ☐ | ☐ | ☐ | ☐ |  |"""
REPLACEMENTS.append((
    "02-the-nine-capacities.md",
    "Self-assessment grid",
    ch02_table,
))

# === Ch 06 — Verification tier matrix ===
ch06_table = """| Tier | Layer 1 — Fact | Layer 2 — Reasoning | Layer 3 — Framing | Layer 4 — Omission | Approx. time |
|---|:---:|:---:|:---:|:---:|---|
| **Trivial** (drafts you'll edit, brainstorms, throwaway code) | Optional (spot-check) | Skip | Skip | Skip | < 1 min |
| **Operational** (internal memos, non-prod code, personal decisions) | Required | Required | Optional | Skip | 5–15 min |
| **External** (client work, regulator-facing, public, senior stakeholder) | Required | Required | Required | Required | 30–60 min |
| **High Stakes / Irreversible** (medical, legal, financial, named harm) | Required | Required | Required | Required (deepest) | 1+ hr — verification *is* the work |"""
REPLACEMENTS.append((
    "06-discernment.md",
    "Verification tier matrix",
    ch06_table,
))

# === Ch 10 first comment (line 74) — existing table fulfills it; just remove the comment ===
REPLACEMENTS.append((
    "10-specification-and-diligence-for-automation.md",
    "The six anticipatory categories as a pre-ship checklist",
    "",  # empty replacement = comment removed; existing table below stays
))

# === Ch 10 second comment (line 105) — Four Diligence failure modes ===
ch10b_table = """| Failure mode | What it looks like undetected | Diligence move that catches it | Cadence | Approx. annual time cost |
|---|---|---|---|---|
| **Input drift** | Sources that were reliable degrade silently; sample no longer represents the design case | Weekly spot-check on a recent batch — read what came in, not just what came out | Weekly, 15 min | ~13 hr |
| **Output drift** | Same inputs now produce subtly different outputs (model swap, tuning change, vendor update) | Monthly fixed-test re-run against a frozen input set | Monthly, ~1 hr | ~12 hr |
| **Context shift** | The world the automation operates on has changed in ways the model has no signal for | Quarterly outcome audit — sample real-world impact, refresh sources and prompts | Quarterly, ~half day | ~16 hr |
| **Accountability gap** | Outputs flow to consumers without anyone on the hook; no one is reading the failures when they occur | Named owner with explicit review duty in the runbook; failure-flag triage in the weekly check | Continuous (folded into above) | folded in |
| **Total** |  |  |  | **~40 hr / year** |"""
REPLACEMENTS.append((
    "10-specification-and-diligence-for-automation.md",
    "The four Diligence failure modes",
    ch10b_table,
))

# === Ch 11 — Agent blast-radius assessment matrix ===
# Existing table below stays; new comparison matrix replaces the comment.
ch11_table = """| Dimension | Calendar scheduling agent | Code deployment agent | Agent with financial transaction authority | The Ash case (reference) |
|---|---|---|---|---|
| **Stakeholder reach** | Caller, callee, your team's calendars — bounded and known | Engineering team, on-call rotation, downstream consumers of the deploy | Customers, counterparties, the institution's regulators | Entire user population of a shared server who never consented |
| **Reversibility** | High — meetings can be moved, invites resent | Mixed — rollback exists for code; not for data migrations or external side effects | Low to none — wires, trades, and disclosures cannot be unsent | Effectively none — server reset against unknown backup state |
| **Identity verification** | Auth handled by the calendar host; low risk if scoped to your account | Required: signed commits, deploy keys, 2FA on the agent's runner | Required and audited: customer auth, transaction-level approval, segregation of duties | Absent — acted on instructions from a user not authorized to issue them |
| **Escalation pathway** | Obvious — surface conflicts and ambiguous times to the user | Required — fail-stop on tests, page on-call on production drift | Required and rehearsed — hard halt on threshold breaches, named escalation duty | None working — goal in hand, tools blocked, alternative tools used without escalation |"""
REPLACEMENTS.append((
    "11-agency-and-the-three-structural-failures.md",
    "Agent blast-radius assessment matrix",
    ch11_table,
))

# === Ch 12 first comment — Four Node conditions ===
ch12a_table = """| Condition | What "Functional" looks like | What "Degraded" looks like | How degradation typically happens |
|---|---|---|---|
| **Authority** | The human at the Node can override the AI — including by saying *no* — and the override holds | Override is technically permitted but operationally costly: rework, queue penalties, manager escalation | Process design that punishes overrides; KPIs that reward throughput over judgment |
| **Information** | The human sees what the AI saw plus what the AI missed — labs, history, specific facts the model has no access to | The human sees the AI's recommendation and a confidence label, with no surfaced inputs to challenge it | Optimizing the UI for efficiency over judgment; hiding raw inputs behind summaries |
| **Time** | The time budget at the Node fits the hardest case the Node has to handle, not the median | A uniform short budget per case; harder cases get the same minute as easier ones | Queue pressure; SLAs measured in seconds; staffing models that price the median |
| **Accountability** | A specific named human is on the hook if the decision is wrong — license, role, paper trail | "The system" or "the team" is on the hook; the named human can defer to the AI's recommendation as cover | Diffuse accountability; sign-offs that the audit trail treats as advisory; AI cited as the decision-maker |"""
REPLACEMENTS.append((
    "12-verification-and-diligence-under-autonomy.md",
    "The four Node conditions",
    ch12a_table,
))

# === Ch 12 second comment — Bank deployment before/after ===
ch12b_table = """| Element | Before (proposed) | After (defensible) |
|---|---|---|
| **Automation rate** | 60% of incoming cases handled end-to-end by the agent | 30–35% — the residual is what survives once the Node design correctly routes the rest |
| **Identity verification** | Not specified — the agent acted on whatever the email asserted | Required before any account action: customer auth, instruction-level verification, no out-of-band changes |
| **Capability constraints** | Not specified — the agent could touch any field it could see | Explicit: no transfers, no cross-account access, no policy exceptions, no credential changes |
| **Node trigger conditions** | Not specified — the agent decided when to ask | Account closures, credential changes, agent-flagged uncertainty, plus a 5% random audit |
| **Node accountability structure** | Not specified — implied "the team reviews escalations" | Named accountable human, genuine authority to refuse, time budget sized to the hardest case, audit trail per decision |"""
REPLACEMENTS.append((
    "12-verification-and-diligence-under-autonomy.md",
    "The bank deployment",
    ch12b_table,
))

# === Ch 13 first comment — 90-day plan template ===
ch13a_table = """| Slot | Capacity name | Daily rep — what / how long / artifact | Weekly review — day / time / the one question | 90-day artifact (specific enough to evaluate) |
|---|---|---|---|---|
| **Capacity 1** | _________________ | _________________ / _____ min / _________________ | _____ / _____ / _________________ | _________________ |
| **Capacity 2** | _________________ | _________________ / _____ min / _________________ | _____ / _____ / _________________ | _________________ |"""
REPLACEMENTS.append((
    "13-the-fluent-practitioner.md",
    "90-day plan template",
    ch13a_table,
))

# === Ch 13 second comment — Anatomy of the fluent answer ===
ch13b_table = """| Sentence or phrase from the answer | What it does | What the vague literate-user answer omits |
|---|---|---|
| *"I used the model to draft the company-snapshot and market-sizing sections."* | Names what the AI did specifically — which sections, which moves | The literate user says "helped me draft it" without naming which parts |
| *"The source list for those sections was verified independently; the three primary filings I relied on are listed in the appendix."* | Surfaces the verification — what was checked, against what, where it can be audited | The literate user buries or omits verification entirely |
| *"I did the team analysis without the model because the senior signals I was reading require knowing things about how that particular firm operates that are not in any document the model could access."* | Names where domain expertise was load-bearing — and *why* the model could not substitute | The literate user cannot name this — which means she does not know it |
| *"The recommendation at the end is mine. The accountability for the brief is mine."* | Assigns accountability cleanly to a single named person | The literate user leaves accountability ambiguous — "we put it together" |"""
REPLACEMENTS.append((
    "13-the-fluent-practitioner.md",
    "Anatomy of the fluent answer",
    ch13b_table,
))


def apply_replacements():
    counts = {}
    for filename, key, replacement in REPLACEMENTS:
        path = CH / filename
        text = path.read_text()
        # Match the entire comment that contains `key`. Comments are single-line.
        pattern = re.compile(
            r'<!--\s*→\s*\[TABLE:[^\n]*?' + re.escape(key) + r'[^\n]*?-->',
            re.DOTALL,
        )
        m = pattern.search(text)
        if not m:
            print(f"!!! NO MATCH: {filename} | key={key!r}")
            continue
        new_text = text[:m.start()] + replacement + text[m.end():]
        path.write_text(new_text)
        counts[filename] = counts.get(filename, 0) + 1
        print(f"[ok] {filename} | {key!r} → {len(replacement)} chars")
    return counts


if __name__ == "__main__":
    counts = apply_replacements()
    print("\n--- per-file table counts ---")
    for f, n in counts.items():
        print(f"  {f}: {n}")
