# Enrichment + Cleanup Log

Run: 2026-05-04 — botspeak

## What changed (most recent → earliest)

### Build pipeline now works end-to-end

`bash build.sh` produces both `output/botspeak.epub` and `output/botspeak.html` from the 16-file chapter set, with metadata, two stylesheets, and a TOC. EPUB chapter splits land cleanly on the 16 H1s (frontmatter, intro, 13 chapters, back matter). The only remaining build warnings are 10 missing portrait .jpg files — see Action Items below.

Files added:

- `metadata.yaml` — pandoc-format book metadata (title, author, language, subjects, keywords)
- `chapters/00-frontmatter.md` — title page, copyright, dedication, "How to read this book"
- `chapters/99-back-matter.md` — acknowledgements, about-the-author, colophon, note on revision
- `styles/kindle.css` — baseline editorial / serif / monochrome stylesheet
- `styles/kindle-book.css` — Botspeak-specific overrides on top of `kindle.css`
- `build.sh` — pandoc → EPUB + HTML build script (executable)

### Inconsistencies fixed

- **Wayback Machine headers** — chapters 0–9 used `## AI Wayback Machine`; chapters 10–13 used `## 🕰️ AI Wayback Machine`. Now all 14 use the emoji form.
- **Portrait image paths** — chapters 0–9 used `../images/...` for portrait stubs; chapters 10–13 used the same. Now all 14 use `images/...` (consistent with chapter-figure paths and with how pandoc resolves resources from the book root).
- **Chapter 02 — Reuven Feuerstein → Lev Vygotsky.** Feuerstein died 2014 with active post-2000 work; Vygotsky (1896–1934) is pre-2001 clean and a stronger conceptual fit for the Nine Capacities chapter (the capacities are made through *mediated* practice — ZPD).
- **Chapter 06 — Wald block reconstructed.** The previous edit had replaced Buolamwini with Abraham Wald in the contextualizing paragraph but left the prompt block empty and the "Now make the prompt better" bullets still referencing Buolamwini. Rebuilt the full block.
- **Chapter 07 — orphan code fence at EOF removed.** A stale ` ``` ` was sitting after the Wayback block, breaking parsing of subsequent chapters.
- **Chapter 08 — duplicated Wayback block removed.** The full Donella Meadows block had been pasted twice; deleted the second copy.
- **Chapter 09 — missing opening fence on the Run-this prompt restored.** The closing ` ``` ` was orphaned without an opener.
- **Boundary `---` / `## ` adjacency in ch 06.** Pandoc was reading `---\n## 🕰️ AI Wayback Machine\n` as a single-column markdown table that swallowed everything from the section header through the start of chapter 7. Inserted a blank line between the rule and the H2.
- **Trailing whitespace.** Every chapter file now ends with `\n\n` so concatenation in the build pipeline doesn't fuse a paragraph with the next chapter's H1.

### Per-chapter Wayback subjects (final state)

| Ch | Subject | Status |
|---|---|---|
| 00 | Henriette Avram (1919–2006) | kept (retired 1992; no significant post-2000 work) |
| 01 | W. Ross Ashby (1903–1972) | kept (clean) |
| 02 | **Lev Vygotsky** (1896–1934) | replaced from Feuerstein |
| 03 | W. Edwards Deming (1900–1993) | kept (already replaced from Leveson before this run) |
| 04 | Mary Parker Follett (1868–1933) | kept (clean) |
| 05 | Gordon Pask (1928–1996) | kept (clean) |
| 06 | Abraham Wald (1902–1950) | kept; section reconstructed (had been replaced from Buolamwini before this run, incompletely) |
| 07 | Walter Shewhart (1891–1967) | kept (already replaced from Taguchi before this run) |
| 08 | Donella Meadows (1941–Feb 2001) | kept (borderline — died Feb 2001 of meningitis; no significant post-2000 work in the 7 weeks) |
| 09 | Norbert Wiener (1894–1964) | kept (clean) |
| 10 | **Grace Hopper** (1906–1992) | replaced from Wing |
| 11 | **Barry Turner** (1937–1995) | replaced from Perrow |
| 12 | **Kurt Gödel** (1906–1978) | replaced from Goldwasser |
| 13 | Yuen Ren Chao (1892–1982) | kept (clean) |

### Tables, figures, and TABLE/FIGURE/IMAGE/DIAGRAM comments

- 9 TABLE comments rendered into populated GitHub-flavored markdown tables (chapters 02, 06, 10×2, 11, 12×2, 13×2). One Ch 10 comment was already fulfilled by an existing populated table — comment removed, table preserved.
- 3 SVG/PNG figure pairs generated in the editorial / monochrome warm-grayscale style: `03-specification-fig-03`, `08-putting-the-loop-together-fig-01`, `10-specification-and-diligence-for-automation-fig-01`. PNGs at 2× the SVG viewBox.
- 25 INFOGRAPHIC/CHART comments left in place as documentation; they are HTML comments and do not render.

## Action items the build pass cannot complete on its own

### Generate 10 portrait .jpg files

The Wayback Machine stubs reference these 10 files (existing chapters 0, 1, 4, 5 already have their portraits on disk; the other 10 do not):

- `images/lev-vygotsky.jpg` (Ch 2) — c. 1930, Soviet psychologist, monochrome portrait
- `images/w-edwards-deming.jpg` (Ch 3) — c. 1980s, statistician, monochrome portrait
- `images/abraham-wald.jpg` (Ch 6) — c. 1940s, Hungarian-American statistician, monochrome portrait
- `images/walter-shewhart.jpg` (Ch 7) — c. 1930s, Bell Labs quality engineer, monochrome portrait
- `images/donella-meadows.jpg` (Ch 8) — c. 1990s, environmental scientist, monochrome portrait
- `images/norbert-wiener.jpg` (Ch 9) — c. 1950s, MIT mathematician, monochrome portrait
- `images/grace-hopper.jpg` (Ch 10) — c. 1960, naval officer in uniform, monochrome portrait
- `images/barry-turner.jpg` (Ch 11) — c. 1980s, British sociologist, monochrome portrait
- `images/kurt-godel.jpg` (Ch 12) — c. 1940s, IAS portrait, monochrome
- `images/yuen-ren-chao.jpg` (Ch 13) — c. 1950s, Berkeley-era portrait, monochrome

Until those files exist, the EPUB references them but cannot embed them. The HTML proof shows them as broken images.

### Add a cover image

`build.sh` looks for `cover.jpg` at the book root. KDP wants 1600×2560 JPEG, RGB, ≤50 MB. The EPUB builds without it; cover is required only for KDP upload.

### Voice flag

This book has no per-book `style/` voice samples yet, so drafts here remain `voice-unanchored` per `book.md` §Voice. Chapter 0 (the Citation That Wasn't) is the voice-setting exercise per `book.md`.

## Build commands

```
cd books/botspeak
./build.sh
```

Outputs land in `output/`: `botspeak.epub` (KDP-ready), `botspeak.html` (proofing mirror), and `combined.md` (archival concatenated source).
