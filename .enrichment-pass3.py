#!/usr/bin/env python3
"""Pass 3 — Validate Wayback Machine subjects against the 'no post-2000' rule
and insert AI-generated portrait stubs.

Decisions per chapter:
  10 — Jeannette Wing  (b.1956, alive, post-2000 work) → REPLACE with Grace Hopper
  11 — Charles Perrow  (1925-2019, post-2000 book)     → REPLACE with Barry Turner
  12 — Shafi Goldwasser(b.1958, alive, post-2000 work) → REPLACE with Kurt Gödel
  13 — Yuen Ren Chao   (1892-1982, all pre-2000)       → KEEP (just insert stub)
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"


# Each entry: a complete replacement of the AI Wayback Machine block
# from the section header through the closing "What changes? ..." line.
# We keep the block's structural shape identical to the existing chapters' style.

SECTIONS = {
    "10-specification-and-diligence-for-automation.md": {
        "old_subject": "Jeannette Wing",
        "new_subject": "Grace Hopper",
        "stub_caption": "Grace Hopper, c. 1960. AI-generated portrait based on a public domain photograph.",
        "stub_filename": "grace-hopper.jpg",
        "stub_alt": "Grace Hopper, c. 1960. AI-generated portrait based on a public domain photograph (Wikimedia Commons).",
        "block": """## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Grace Hopper** was working out how to specify a computation precisely enough that a machine could execute it without a human at the keyboard — compilers, machine-independent languages, COBOL — decades before "AI automation" was a job description. Here's a prompt to find out more — and then make it better.

{STUB}

**Run this:**

```
Who was Grace Hopper, and how does her work on compilers and machine-independent specification connect to writing automation specs against the six ambiguity types in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Grace Hopper"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "machine independence" in plain language, as if you've never written a line of COBOL
- Ask it to compare Hopper's compiler discipline to anticipating model swaps in a deployed automation
- Add a constraint: "Answer as if you're writing the rationale for a Section 11 automation spec"

What changes? What gets better? What gets worse?
""",
    },

    "11-agency-and-the-three-structural-failures.md": {
        "old_subject": "Charles Perrow",
        "new_subject": "Barry Turner",
        "stub_caption": "Barry Turner, c. 1980s. AI-generated portrait based on a public domain photograph.",
        "stub_filename": "barry-turner.jpg",
        "stub_alt": "Barry Turner, c. 1980s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).",
        "block": """## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Barry Turner** was arguing in *Man-Made Disasters* that catastrophic failures incubate quietly inside the structure of an organization — not as anyone's operator error, but as accumulated small omissions waiting on a trigger — decades before agentic AI deployments existed. Here's a prompt to find out more — and then make it better.

{STUB}

**Run this:**

```
Who was Barry Turner, and how does his theory of disaster incubation connect to the three structural failures of agentic AI — overreach, identity-verification gap, and missing escalation? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Barry Turner sociologist"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "incubation period" and "decoy phenomena" in plain language, as if you've never read the sociology of accidents
- Ask it to compare Turner's analysis of the Aberfan disaster to a hypothetical agentic-tool failure in your role
- Add a constraint: "Answer as if you're writing red-flag entries for a 'no go' agentic-deployment decision aid"

What changes? What gets better? What gets worse?
""",
    },

    "12-verification-and-diligence-under-autonomy.md": {
        "old_subject": "Shafi Goldwasser",
        "new_subject": "Kurt Gödel",
        "stub_caption": "Kurt Gödel, c. 1940s. AI-generated portrait based on a public domain photograph.",
        "stub_filename": "kurt-godel.jpg",
        "stub_alt": "Kurt Gödel, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).",
        "block": """## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Kurt Gödel** proved that any verification system powerful enough to be useful has true claims it cannot decide from inside itself — the formal limit on automated checking — decades before "Human Decision Node" entered anyone's vocabulary. Here's a prompt to find out more — and then make it better.

{STUB}

**Run this:**

```
Who was Kurt Gödel, and how do his incompleteness theorems connect to designing a Human Decision Node that has to verify an agentic action without re-running the agent's reasoning? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Kurt Gödel"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "incompleteness" in plain language, as if you've never seen a logic textbook
- Ask it to compare Gödel's limit-theorem framing to the four diagnostic questions for a functional Node
- Add a constraint: "Answer as if you're sketching the audit cadence that catches Node degradation"

What changes? What gets better? What gets worse?
""",
    },

    "13-the-fluent-practitioner.md": {
        # Keep Yuen Ren Chao — died 1982, foundational work all pre-2000.
        "old_subject": "Yuen Ren Chao",
        "new_subject": "Yuen Ren Chao",
        "stub_caption": "Yuen Ren Chao, c. 1950s. AI-generated portrait based on a public domain photograph.",
        "stub_filename": "yuen-ren-chao.jpg",
        "stub_alt": "Yuen Ren Chao, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).",
        "block": None,  # signals "keep existing block; just insert stub"
    },
}


PORTRAIT_STUB_TEMPLATE = (
    "![{alt}](../images/{filename})\n*{caption}*"
)


def process_chapter(filename, info):
    path = CH / filename
    text = path.read_text()
    section_marker = "## 🕰️ AI Wayback Machine"
    if section_marker not in text:
        print(f"!!! no section in {filename}")
        return None

    stub = PORTRAIT_STUB_TEMPLATE.format(
        alt=info["stub_alt"],
        filename=info["stub_filename"],
        caption=info["stub_caption"],
    )

    if info["block"] is None:
        # Keep mode — insert stub between the opening paragraph and "Run this:".
        # Locate the opening paragraph (the one that names the person).
        # Find the section, then insert before "**Run this:**".
        sec_idx = text.index(section_marker)
        run_idx = text.index("**Run this:**", sec_idx)
        # Walk back from run_idx to the previous double-newline (paragraph break).
        # We want to insert immediately after the contextualizing paragraph
        # and before any preceding blank line that leads into "Run this:".
        # Insert "\n\n{stub}\n" right before "**Run this:**" with surrounding blank lines.
        before = text[:run_idx]
        after = text[run_idx:]
        # Trim any trailing blank lines after the contextualizing paragraph
        before = before.rstrip() + "\n\n" + stub + "\n\n"
        new_text = before + after
        path.write_text(new_text)
        action = "kept"
    else:
        # Replace mode — swap the entire AI Wayback Machine block.
        # Find start (the section header) and end (next ## header or EOF).
        sec_idx = text.index(section_marker)
        # Look for the next H2 after sec_idx; if none, take to EOF.
        next_h2 = re.search(r'\n## ', text[sec_idx + 1:])
        if next_h2:
            end_idx = sec_idx + 1 + next_h2.start() + 1  # keep the leading \n
        else:
            end_idx = len(text)
        new_block = info["block"].format(STUB=stub).rstrip() + "\n"
        # Preserve the trailing \n if there was one.
        new_text = text[:sec_idx] + new_block
        if end_idx < len(text):
            new_text += text[end_idx:]
        path.write_text(new_text)
        action = "replaced"

    return action, info["old_subject"], info["new_subject"]


def main():
    results = {}
    for filename, info in SECTIONS.items():
        result = process_chapter(filename, info)
        results[filename] = result
        print(f"  {filename}: {result}")
    return results


if __name__ == "__main__":
    main()
