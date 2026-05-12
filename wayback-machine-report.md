# AI Wayback Machine — Insertion Report

**Status:** All 14 botspeak chapters updated. Block appended at end-of-file in each.

---

## Chapter → Figure Map

| # | Chapter | Figure | Anchor Concept |
|---|---|---|---|
| 00 | The Citation That Wasn't | Henriette Avram | MARC / machine-readable cataloging |
| 01 | The Loop and the Three Modes | W. Ross Ashby | Law of Requisite Variety |
| 02 | The Nine Capacities | Reuven Feuerstein | Mediated Learning Experience |
| 03 | Specification | Nancy Leveson | STAMP / system-theoretic specs |
| 04 | Delegation | Mary Parker Follett | Law of the Situation |
| 05 | Conversation | Gordon Pask | Conversation Theory |
| 06 | Discernment | Joy Buolamwini | Algorithmic auditing (Gender Shades) |
| 07 | Diligence | Genichi Taguchi | Robust design / loss function |
| 08 | Putting the Loop Together | Donella Meadows | Feedback loops & leverage points |
| 09 | When You're Not There | Clarence "Skip" Ellis | Operational Transformation / CSCW |
| 10 | Specification & Diligence for Automation | Jeannette Wing | Computational Thinking / Liskov-Wing |
| 11 | Agency & Three Structural Failures | Charles Perrow | Normal Accidents |
| 12 | Verification & Diligence Under Autonomy | Shafi Goldwasser | Zero-knowledge proofs |
| 13 | The Fluent Practitioner | Yuen Ren Chao | Linguistic fluency / competence vs performance |

---

## Diversity Summary

**Figures included:** Henriette Avram, W. Ross Ashby, Reuven Feuerstein, Nancy Leveson, Mary Parker Follett, Gordon Pask, Joy Buolamwini, Genichi Taguchi, Donella Meadows, Clarence "Skip" Ellis, Jeannette Wing, Charles Perrow, Shafi Goldwasser, Yuen Ren Chao.

**Gender breakdown:** 8 women, 6 men.

**Geographic / national breakdown:**
- US-born or US-based: Leveson, Follett, Meadows, Ellis, Perrow (Perrow worked in US, born US)
- UK: Ashby, Pask
- Romanian-American (Jewish): Avram
- Romanian-Israeli (Jewish): Feuerstein
- Israeli-American (Jewish): Goldwasser
- Japanese: Taguchi
- Ghanaian-American (Black): Buolamwini
- Chinese-American: Wing, Chao
- Black American: Ellis

**Era breakdown (active period of cited work):**
- Pre-1950: 1 (Follett — peaked 1920s)
- 1950–1990: 8 (Avram, Ashby, Feuerstein, Pask, Taguchi, Meadows, Ellis, Perrow, Chao — Chao straddles, peak 1940s–60s; counted here)
- Post-1990: 5 (Leveson active across 80s-present, Buolamwini, Wing, Goldwasser — Goldwasser's foundational 1985 work technically pre-1990 but career extends; counted post-1990 for impact period)

Counted Chao in 1950-1990 (his Mandarin Primer is 1948 — borderline; his career extends through 1970s) and Leveson and Goldwasser in post-1990.

**Disciplines represented:**
- Library / information science: Avram
- Cybernetics: Ashby, Pask, Meadows
- Cognitive psychology / educational science: Feuerstein
- Software safety engineering: Leveson
- Management / organization theory: Follett
- Algorithmic auditing / AI ethics: Buolamwini
- Quality engineering / industrial statistics: Taguchi
- CSCW / collaborative computing: Ellis
- Theoretical computer science: Wing, Goldwasser
- Sociology of organizations & accidents: Perrow
- Linguistics: Chao

**Race / ethnicity (separate axis):**
- 6 white European/American: Ashby, Leveson, Follett, Pask, Meadows, Perrow
- 3 Jewish: Avram, Feuerstein, Goldwasser
- 2 Black: Buolamwini, Ellis
- 3 East Asian: Taguchi, Wing, Chao

**Flags:**
- The set is heavy on 1950–1990 (8 of 14). Pre-1950 is thin (Follett alone). If you want more pre-1950 representation, swap candidates: Suzanne Briet for ch. 0 (documentation theory, pre-1950 French librarian), or Frank Ramsey / Émilie du Châtelet are conceivable but the connection is weaker. I weighted era against fit-to-chapter.
- Latin America, the Arab world, sub-Saharan Africa (beyond Buolamwini's Ghanaian heritage), and Indigenous traditions are unrepresented. None of the swap candidates I considered for those regions had genuine connections to the specific chapter topics. If you want one, the candidate I'd most consider is **S.R. Ranganathan** (Indian, faceted classification) for ch. 0 — but Avram's connection is tighter.
- 8 women is intentional — the historical record badly under-credits women in computing-adjacent fields, and the figures here all earned the slot on substance.

---

## One Caveat About Insertion Location

Your prompt said *"immediately after the LLM Exercise block."* In some chapters (02, 03, 06, 09, 12), the LLM Exercise block sits in the middle of the file with the regular `## Exercises` (the 10-question set) coming after it. I appended at the **end of file** in all 14 chapters, treating "at the bottom of each chapter file" as the operative phrase. This means in those five chapters, the AI Wayback Machine block is positioned after the regular exercises, not immediately after the LLM Exercise block.

If you want it inserted strictly after the `### LLM Exercise` block in those five (which would put it ahead of the `## Exercises` section), say the word and I'll relocate.

---

## Verification Suggestions

Before signing off:

1. Spot-check 2–3 figures against Wikipedia to confirm the framing-sentence claims aren't off. The riskiest framings are the chapter-concept connections in chapters 8 (Meadows) and 13 (Chao) — both connections work but are looser than the others.
2. Run the chapter-3 prompt (Leveson) yourself — it's a useful sanity check on whether the "Run this" prompts produce something the learner can use.
3. Confirm Yuen Ren Chao's Wikipedia page name. Some sources hyphenate ("Yuen-ren Chao"); the page title is **Yuen Ren Chao**.

Logged at: `books/botspeak/wayback-machine-report.md`
