#!/usr/bin/env python3
"""Pass 2 — Generate SVG figures + 2x PNG copies for FIGURE/IMAGE/DIAGRAM comments."""
import re, os
from pathlib import Path
import cairosvg

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

# Shared SVG defs block. Arrow marker, no shadows, no gradients.
DEFS = '''<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#1a1714"/>
  </marker>
</defs>'''

INK = "#1a1714"
GRAY_DARK = "#4a4540"
GRAY_MID = "#8a8480"
GRAY_LIGHT = "#c8c4c0"
CREAM = "#f5f2ee"
WHITE = "#fdfcfb"
SERIF = "Georgia, 'Times New Roman', serif"


# ---------------------------------------------------------------------------
# Figure 3.3 — Filled-in template card (Aisha / rural broadband summary)
# ---------------------------------------------------------------------------
def fig_3_3():
    # 700 x 460 — slightly taller because the card has 5 rows of body text.
    w, h = 700, 460
    # Card geometry (paper notecard look).
    card_x, card_y, card_w, card_h = 60, 56, 580, 348

    # Field rows: y_label, y_text_start, label, body lines
    rows = [
        (
            "INTENT",
            "Give my manager a five-bullet artifact she can paste onto a slide",
            "for tomorrow's stakeholder meeting on rural broadband subsidies.",
        ),
        (
            "CONSTRAINTS",
            "Five bullets, one clause each, ≤15 words per bullet. Source:",
            "only claims in the attached report. Audience: has not read it.",
        ),
        (
            "SUCCESS CRITERIA",
            "Manager can paste the bullets onto her deck without rewriting.",
            "Each bullet is readable from twenty feet away.",
        ),
        (
            "EXCLUSIONS",
            "Do not editorialize. Do not pad with context. Do not include",
            "outside-source claims even if they would strengthen the case.",
        ),
        (
            "OUTPUT FORMAT",
            "Five bullets. One clause each. ≤100 words total.",
            "No sub-bullets. No introduction. No closing summary.",
        ),
    ]
    row_h = 64
    rows_top = card_y + 24
    out = []
    out.append(f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">')
    out.append(DEFS)
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>')
    # Card background (looks like a real notecard)
    out.append(
        f'<rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" '
        f'fill="{CREAM}" stroke="{INK}" stroke-width="1"/>'
    )
    # Title strip
    out.append(
        f'<text x="{card_x + 16}" y="{card_y + 20}" font-family="{SERIF}" '
        f'font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">'
        f'SPECIFICATION TEMPLATE — RURAL BROADBAND SUMMARY</text>'
    )
    # Hairline under title
    out.append(
        f'<line x1="{card_x + 16}" y1="{card_y + 28}" x2="{card_x + card_w - 16}" '
        f'y2="{card_y + 28}" stroke="{GRAY_MID}" stroke-width="0.75"/>'
    )

    for i, (label, l1, l2) in enumerate(rows):
        ry = rows_top + i * row_h
        # Field label (small, bold, all caps, indented)
        out.append(
            f'<text x="{card_x + 16}" y="{ry + 14}" font-family="{SERIF}" '
            f'font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1">'
            f'{label}</text>'
        )
        # Body line 1
        out.append(
            f'<text x="{card_x + 16}" y="{ry + 32}" font-family="{SERIF}" '
            f'font-size="13" fill="{INK}">{l1}</text>'
        )
        # Body line 2
        out.append(
            f'<text x="{card_x + 16}" y="{ry + 48}" font-family="{SERIF}" '
            f'font-size="13" fill="{INK}">{l2}</text>'
        )
        # Hairline rule under each field except the last
        if i < len(rows) - 1:
            out.append(
                f'<line x1="{card_x + 16}" y1="{ry + 56}" x2="{card_x + card_w - 16}" '
                f'y2="{ry + 56}" stroke="{GRAY_LIGHT}" stroke-width="0.75" '
                f'stroke-dasharray="4 3"/>'
            )

    # Caption beneath the card
    out.append(
        f'<text x="{w/2}" y="{card_y + card_h + 32}" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'A working artifact — the specification a fluent practitioner fills in '
        f'before she opens the tool.</text>'
    )
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Figure 8.1 — Spec document next to closed laptop
# ---------------------------------------------------------------------------
def fig_8_1():
    w, h = 700, 420
    out = []
    out.append(f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">')
    out.append(DEFS)
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>')

    # ------ LEFT: paper specification document ------
    px, py, pw, ph = 56, 56, 296, 312
    # Page shadow line (subtle, no fill — flat editorial)
    out.append(
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="{CREAM}" '
        f'stroke="{INK}" stroke-width="1"/>'
    )
    # Top label
    out.append(
        f'<text x="{px + 16}" y="{py + 22}" font-family="{SERIF}" '
        f'font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">'
        f'COMPETITIVE INTELLIGENCE BRIEF — SPECIFICATION</text>'
    )
    out.append(
        f'<line x1="{px + 16}" y1="{py + 30}" x2="{px + pw - 16}" y2="{py + 30}" '
        f'stroke="{GRAY_MID}" stroke-width="0.75"/>'
    )
    # Field rows (audience, success criteria, exclusions visible — the comment said so)
    fields = [
        ("AUDIENCE",
         "Investment committee.",
         "Three partners; will read once; will ask hard questions."),
        ("SUCCESS CRITERIA",
         "Defensible recommendation by Friday 9am.",
         "Each claim must trace to a primary source."),
        ("EXCLUSIONS",
         "No outside-source claims unless flagged.",
         "No model speculation. No padded context."),
        ("OUTPUT FORMAT",
         "Five sections; ≤3 pages; appendix with",
         "filings list; one-sentence executive summary."),
    ]
    fy_start = py + 50
    fy_step = 64
    for i, (lab, l1, l2) in enumerate(fields):
        fy = fy_start + i * fy_step
        out.append(
            f'<text x="{px + 16}" y="{fy}" font-family="{SERIF}" '
            f'font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1">'
            f'{lab}</text>'
        )
        out.append(
            f'<text x="{px + 16}" y="{fy + 16}" font-family="{SERIF}" '
            f'font-size="11" fill="{INK}">{l1}</text>'
        )
        out.append(
            f'<text x="{px + 16}" y="{fy + 32}" font-family="{SERIF}" '
            f'font-size="11" fill="{INK}">{l2}</text>'
        )
        if i < len(fields) - 1:
            out.append(
                f'<line x1="{px + 16}" y1="{fy + 44}" x2="{px + pw - 16}" '
                f'y2="{fy + 44}" stroke="{GRAY_LIGHT}" stroke-width="0.75" '
                f'stroke-dasharray="4 3"/>'
            )
    # Page caption
    out.append(
        f'<text x="{px + pw/2}" y="{py + ph + 22}" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'Written first — on paper, before the tool opens.</text>'
    )

    # ------ RIGHT: closed laptop silhouette ------
    lx, ly = 416, 168
    lw_top, lh_top = 224, 152  # closed lid
    base_h = 14
    # Lid
    out.append(
        f'<rect x="{lx}" y="{ly}" width="{lw_top}" height="{lh_top}" '
        f'fill="{CREAM}" stroke="{INK}" stroke-width="1"/>'
    )
    # Apple-style etched circle (we'll do a plain inset rectangle for an "lid logo" — keep monochrome flat)
    out.append(
        f'<circle cx="{lx + lw_top/2}" cy="{ly + lh_top/2}" r="22" '
        f'fill="none" stroke="{GRAY_MID}" stroke-width="1"/>'
    )
    out.append(
        f'<circle cx="{lx + lw_top/2}" cy="{ly + lh_top/2}" r="6" '
        f'fill="{GRAY_MID}"/>'
    )
    # Base (slightly wider than lid for closed-laptop feel)
    base_x = lx - 12
    base_y = ly + lh_top
    base_w = lw_top + 24
    out.append(
        f'<rect x="{base_x}" y="{base_y}" width="{base_w}" height="{base_h}" '
        f'fill="{GRAY_LIGHT}" stroke="{INK}" stroke-width="1"/>'
    )
    # Hinge line
    out.append(
        f'<line x1="{lx}" y1="{ly + lh_top}" x2="{lx + lw_top}" '
        f'y2="{ly + lh_top}" stroke="{INK}" stroke-width="1"/>'
    )
    # Front lip
    out.append(
        f'<line x1="{base_x + 32}" y1="{base_y + base_h}" x2="{base_x + base_w - 32}" '
        f'y2="{base_y + base_h}" stroke="{GRAY_DARK}" stroke-width="0.75"/>'
    )
    # Caption under laptop
    out.append(
        f'<text x="{lx + lw_top/2}" y="{base_y + base_h + 32}" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'Closed — the tool is the second move, not the first.</text>'
    )

    # Title at top of figure
    out.append(
        f'<text x="{w/2}" y="36" font-family="{SERIF}" '
        f'font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">'
        f'Specification first. Tool second.</text>'
    )

    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Figure 10.1 — Side-by-side annotated comparison: Augmentation vs Automation
# ---------------------------------------------------------------------------
def fig_10_1():
    # Taller canvas — 6 callouts on the right column.
    w, h = 700, 600
    out = []
    out.append(f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">')
    out.append(DEFS)
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>')

    # Title
    out.append(
        f'<text x="{w/2}" y="32" font-family="{SERIF}" '
        f'font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">'
        f'Augmentation specification → Automation specification</text>'
    )
    out.append(
        f'<text x="{w/2}" y="50" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'The extra length is not bureaucracy — it is the implicit work the human '
        f'would have done at the keyboard.</text>'
    )

    # ------ LEFT column: short spec ------
    lx, ly, lw, lh = 56, 80, 220, 470
    out.append(
        f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" fill="{CREAM}" '
        f'stroke="{INK}" stroke-width="1"/>'
    )
    out.append(
        f'<text x="{lx + 12}" y="{ly + 22}" font-family="{SERIF}" '
        f'font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">'
        f'AUGMENTATION SPEC</text>'
    )
    out.append(
        f'<line x1="{lx + 12}" y1="{ly + 30}" x2="{lx + lw - 12}" y2="{ly + 30}" '
        f'stroke="{GRAY_MID}" stroke-width="0.75"/>'
    )
    aug_lines = [
        "Produce a weekly competitive",
        "intelligence brief on the three",
        "named competitors. Cover product,",
        "pricing, and headcount. ≤2",
        "pages, source-cited. Use the",
        "weekly news pull as input.",
        "I’ll review before it ships.",
    ]
    for i, line in enumerate(aug_lines):
        out.append(
            f'<text x="{lx + 12}" y="{ly + 56 + i*22}" font-family="{SERIF}" '
            f'font-size="12" fill="{INK}">{line}</text>'
        )
    out.append(
        f'<text x="{lx + lw/2}" y="{ly + lh - 16}" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'~50 words. One paragraph.</text>'
    )

    # ------ RIGHT column: long spec, with structural section labels ------
    rx, ry, rw, rh = 320, 80, 220, 470
    out.append(
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="{CREAM}" '
        f'stroke="{INK}" stroke-width="1"/>'
    )
    out.append(
        f'<text x="{rx + 12}" y="{ry + 22}" font-family="{SERIF}" '
        f'font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">'
        f'AUTOMATION SPEC</text>'
    )
    out.append(
        f'<line x1="{rx + 12}" y1="{ry + 30}" x2="{rx + rw - 12}" y2="{ry + 30}" '
        f'stroke="{GRAY_MID}" stroke-width="0.75"/>'
    )

    # Six section labels inside the right card. Each one will get a callout.
    # Y positions chosen on the 8px grid.
    sections = [
        ("Pre-flight checks", 56),
        ("Confidence labels", 120),
        ("Exclusions", 184),
        ("Failure-mode handling", 248),
        ("Diligence design", 320),
        ("Named accountable human", 392),
    ]
    for label, dy in sections:
        out.append(
            f'<text x="{rx + 12}" y="{ry + dy}" font-family="{SERIF}" '
            f'font-size="11" font-weight="bold" fill="{INK}">{label}</text>'
        )
        # one line of placeholder body text under each
        out.append(
            f'<text x="{rx + 12}" y="{ry + dy + 16}" font-family="{SERIF}" '
            f'font-size="10" fill="{GRAY_DARK}">— specified in advance —</text>'
        )
        # hairline rule
        out.append(
            f'<line x1="{rx + 12}" y1="{ry + dy + 28}" x2="{rx + rw - 12}" '
            f'y2="{ry + dy + 28}" stroke="{GRAY_LIGHT}" stroke-width="0.75" '
            f'stroke-dasharray="4 3"/>'
        )
    out.append(
        f'<text x="{rx + rw/2}" y="{ry + rh - 16}" font-family="{SERIF}" '
        f'font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">'
        f'~150 words. Section-structured.</text>'
    )

    # ------ Callouts on the right side of the right card ------
    callouts = [
        ("input-quality anticipation", 56),
        ("output-quality signaling", 120),
        ("model-failure prevention", 184),
        ("six ambiguity types addressed", 248),
        ("four failure modes addressed", 320),
        ("accountability gap closed", 392),
    ]
    callout_x = rx + rw + 24
    for text, dy in callouts:
        ty = ry + dy + 4
        # connector line from right edge of card to callout start
        out.append(
            f'<path d="M{rx + rw} {ry + dy} L{callout_x - 8} {ty}" '
            f'fill="none" stroke="{INK}" stroke-width="1" marker-end="url(#arrow)"/>'
        )
        out.append(
            f'<text x="{callout_x}" y="{ty + 4}" font-family="{SERIF}" '
            f'font-size="10" fill="{GRAY_DARK}">{text}</text>'
        )

    # Bottom note: "3:1 ratio"
    out.append(
        f'<line x1="{lx + lw/2}" y1="{ly + lh + 14}" x2="{rx + rw/2}" '
        f'y2="{ry + rh + 14}" stroke="{GRAY_MID}" stroke-width="0.75" '
        f'stroke-dasharray="4 3"/>'
    )
    out.append(
        f'<text x="{(lx + lw/2 + rx + rw/2)/2}" y="{ly + lh + 32}" '
        f'font-family="{SERIF}" font-size="10" font-style="italic" '
        f'fill="{GRAY_DARK}" text-anchor="middle">'
        f'Roughly 3× the length, structurally — every addition does work.</text>'
    )

    out.append('</svg>')
    return "\n".join(out)


FIGURES = [
    {
        "slug": "03-specification-fig-03",
        "svg": fig_3_3(),
        "alt": "A filled-in specification template card — Aisha's rural-broadband-summary task with all five fields completed",
        "title": "A filled-in template card",
        "ch_file": "03-specification.md",
        "fig_label": "Figure 3.3",
        "comment_key": "filled-in template card",
        "old_image_md": "![Figure 3.3 — A visual of a filled-in template card](images/03-specification-fig-03.jpg)",
    },
    {
        "slug": "08-putting-the-loop-together-fig-01",
        "svg": fig_8_1(),
        "alt": "A specification document beside a closed laptop — the visual cue that the spec precedes the tool",
        "title": "Specification first, tool second",
        "ch_file": "08-putting-the-loop-together.md",
        "fig_label": "Figure 8.1",
        "comment_key": "handwritten or typed specification document",
        "old_image_md": "![Figure 8.1 — A handwritten or typed specification document](images/08-putting-the-loop-together-fig-01.jpg)",
    },
    {
        "slug": "10-specification-and-diligence-for-automation-fig-01",
        "svg": fig_10_1(),
        "alt": "Side-by-side comparison: a one-paragraph Augmentation specification and a section-structured Automation specification with six labeled additions",
        "title": "Augmentation specification → Automation specification",
        "ch_file": "10-specification-and-diligence-for-automation.md",
        "fig_label": "Figure 10.1",
        "comment_key": "Side-by-side annotated comparison",
        "old_image_md": "![Figure 10.1 — Side-by-side annotated comparison](images/10-specification-and-diligence-for-automation-fig-01.jpg)",
    },
]


def write_svg_and_png(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    # Render PNG at 2x. Look at viewBox in the svg to determine pixel size.
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(
        bytestring=svg_str.encode("utf-8"),
        output_width=vw * 2,
        output_height=vh * 2,
        write_to=str(png_path),
    )
    return svg_path, png_path


def replace_comment_and_image_tag(ch_file, comment_key, old_image_md, alt, title, slug):
    path = CH / ch_file
    text = path.read_text()
    # Build the new image markdown referencing the .png
    new_md = f"![{alt}](../images/{slug}.png)\n*{title}*"
    # Match the comment with comment_key inside it.
    pat = re.compile(
        r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM):[^\n]*?'
        + re.escape(comment_key)
        + r'[^\n]*?-->',
        re.DOTALL,
    )
    m = pat.search(text)
    if not m:
        print(f"!!! NO MATCH (comment): {ch_file} | key={comment_key!r}")
        return False
    # Replace the comment with the new image markdown
    text = text[:m.start()] + new_md + text[m.end():]
    # Now remove the redundant existing placeholder image tag, if it's still there.
    if old_image_md in text:
        text = text.replace(old_image_md + "\n", "")
        text = text.replace(old_image_md, "")
    path.write_text(text)
    print(f"[ok] {ch_file} | comment + placeholder → {slug}.png")
    return True


def main():
    for fig in FIGURES:
        svg_path, png_path = write_svg_and_png(fig["slug"], fig["svg"])
        size_svg = svg_path.stat().st_size
        size_png = png_path.stat().st_size
        print(f"  wrote {svg_path.name} ({size_svg} bytes) + {png_path.name} ({size_png} bytes)")
        replace_comment_and_image_tag(
            fig["ch_file"], fig["comment_key"], fig["old_image_md"],
            fig["alt"], fig["title"], fig["slug"],
        )


if __name__ == "__main__":
    main()
