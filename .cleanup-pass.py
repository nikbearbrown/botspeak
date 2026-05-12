#!/usr/bin/env python3
"""Cleanup pass — make the book buildable with the user's pandoc pipeline.

Operations:
  1) Replace Ch 02 Feuerstein → Vygotsky (last subject failing the post-2000 rule)
  2) Fix Ch 06 — add Wald run-this prompt block; replace Buolamwini-leftover bullets
  3) Normalize all Wayback section headers from `## AI Wayback Machine` to `## 🕰️ AI Wayback Machine`
  4) Normalize all portrait paths from `../images/...` to `images/...`
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"


# ---------------------------------------------------------------------------
# 1) Ch 02 — Replace Feuerstein → Vygotsky
# ---------------------------------------------------------------------------
CH02_NEW_BLOCK = """## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Lev Vygotsky** was working out how cognitive capacities form — that they live first in the joint activity between a learner, the world, and a tool, and only later become individual reflexes — decades before anyone worried about AI-mediated skill atrophy. The capacities in this chapter are not innate traits the reader either has or doesn't. They are made and unmade through the company a learner keeps with their tools. Here's a prompt to find out more — and then make it better.

![Lev Vygotsky, c. 1930. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/lev-vygotsky.jpg)
*Lev Vygotsky, c. 1930. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Lev Vygotsky, and how does his concept of the Zone of Proximal Development connect to the idea that the Nine Capacities are built through mediated practice with tools — including AI — rather than learned in the abstract? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Lev Vygotsky"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "Zone of Proximal Development" in plain language, as if you've never taken a psychology course
- Ask it to compare Vygotsky's account of mediated tool use to the early-warning signs of a capacity going slack from AI use
- Add a constraint: "Answer as if you're writing a footnote in a chapter called The Nine Capacities"

What changes? What gets better? What gets worse?
"""


# ---------------------------------------------------------------------------
# 2) Ch 06 — Reconstruct the Wald block (it lost its prompt and kept Buolamwini bullets)
# ---------------------------------------------------------------------------
CH06_NEW_BLOCK = """## 🕰️ AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Abraham Wald** solved one of the Second World War's most consequential omission problems before most statisticians had named the error type: when the U.S. military asked him where to add armor to its bombers, he pointed to the parts with *no* bullet holes — the planes with holes in those spots never made it back to be counted. The thing missing from the data was exactly the thing that mattered. Here's a prompt to find out more — and then make it better.

![Abraham Wald, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/abraham-wald.jpg)
*Abraham Wald, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Abraham Wald, and how does his bombers-with-no-holes argument connect to Layer 4 of verification — the omission layer — where the most consequential failures hide in what the model did not say? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Abraham Wald"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "survivorship bias" in plain language, as if you've never seen the term
- Ask it to compare Wald's missing-bullet-hole reasoning to running Layers 3 and 4 (framing, omission) on a market-entry brief
- Add a constraint: "Answer as if you're writing a verification-tier example for a chapter on Discernment"

What changes? What gets better? What gets worse?
"""


def replace_block(filename, new_block):
    """Replace the entire `## AI Wayback Machine` (with or without 🕰️) section."""
    path = CH / filename
    text = path.read_text()
    # Locate the section start.
    m = re.search(r'^## (?:🕰️ )?AI Wayback Machine\s*$', text, re.MULTILINE)
    if not m:
        print(f"!!! no AI Wayback Machine section in {filename}")
        return False
    sec_start = m.start()
    # Find the next H2 boundary, or EOF.
    next_h2 = re.search(r'\n## ', text[sec_start + 1:])
    if next_h2:
        sec_end = sec_start + 1 + next_h2.start() + 1
        path.write_text(text[:sec_start] + new_block.rstrip() + "\n" + text[sec_end:])
    else:
        path.write_text(text[:sec_start] + new_block.rstrip() + "\n")
    return True


# ---------------------------------------------------------------------------
# 3) Normalize headers + 4) Normalize image paths
# ---------------------------------------------------------------------------
def normalize_all():
    fixes = []
    for f in sorted(CH.glob("*.md")):
        text = f.read_text()
        original = text
        # Header normalization (only touch header lines that lack the emoji).
        text = re.sub(
            r'^## AI Wayback Machine\s*$',
            '## 🕰️ AI Wayback Machine',
            text,
            flags=re.MULTILINE,
        )
        # Image path normalization — only inside this book's chapter files.
        text = text.replace('](../images/', '](images/')
        if text != original:
            f.write_text(text)
            fixes.append(f.name)
    return fixes


def main():
    print("[1] Ch 02 Feuerstein → Vygotsky")
    replace_block("02-the-nine-capacities.md", CH02_NEW_BLOCK)

    print("[2] Ch 06 Wald block reconstruction")
    replace_block("06-discernment.md", CH06_NEW_BLOCK)

    print("[3+4] Normalize headers and image paths across all chapters")
    fixes = normalize_all()
    for n in fixes:
        print(f"   normalized: {n}")

    # Sanity checks
    print("\n--- post-checks ---")
    plain_count = 0
    bad_path_count = 0
    for f in sorted(CH.glob("*.md")):
        t = f.read_text()
        if re.search(r'^## AI Wayback Machine\s*$', t, re.MULTILINE):
            plain_count += 1
            print(f"  STILL PLAIN: {f.name}")
        if '](../images/' in t:
            bad_path_count += 1
            print(f"  STILL ../images/: {f.name}")
    print(f"plain headers remaining: {plain_count}")
    print(f"../images/ refs remaining: {bad_path_count}")


if __name__ == "__main__":
    main()
