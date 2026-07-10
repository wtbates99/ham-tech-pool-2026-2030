# Technician Pool 2026–2030 Study Tool

A self-contained study app for the FCC Amateur Radio Technician (Element 2)
license exam, built from the **official 2026–2030 question pool** published
by the [NCVEC Question Pool Committee](https://ncvec.org/index.php/2026-2030-technician-question-pool)
(released Dec 18, 2025; revised Feb 19, 2026; effective 7/1/2026–6/30/2030).

All 409 questions, all four answer choices, correct answers, FCC rule
citations, and the 3 schematic figures (T-1, T-2, T-3) used in the
component-identification questions are included verbatim from the NCVEC PDF.

## Use it

Open `index.html` in a browser — no build step, no server, no dependencies.
It also works fine served from GitHub Pages.

Modes:

- **Learn** — browse all 10 subelements / 35 question groups, expand any
  question to reveal the answer and rule citation.
- **Flashcards** — filter by subelement, starred items, or previously-missed
  questions; flip/shuffle; keyboard shortcuts (space to flip, arrows to move).
- **Quiz** — including an "Exam simulation" mode that draws exactly 35
  questions, one per group, mirroring the real VE test, and reports whether
  you'd pass (26/35, 74%).
- **Missed** — questions you've gotten wrong on a quiz collect here for
  targeted review.
- **Progress** — per-subelement mastery bars.

Progress is stored in the browser's `localStorage`, so it's per-device and
persists across sessions.

## Repo layout

```
index.html            generated, self-contained app (open this)
data/questions.json    the 409 parsed questions
data/meta.json          subelement/group titles and descriptions
data/figs/              the 3 schematic figures (T-1, T-2, T-3) as PNGs
scripts/parse_pool.py   parses the NCVEC PDF's extracted text into questions.json
scripts/build_meta.py   writes meta.json (subelement/group titles)
scripts/template.html   app shell with a __DATA__ placeholder
scripts/build.py        embeds data/*.json + data/figs/*.png into index.html
```

To rebuild `index.html` after editing the data or template:

```
python3 scripts/build.py
```

## Source

Question text, answers, and figures are taken directly from the NCVEC's
public-domain release PDF:
`ncvec.org/downloads/TECH_2026/2026-2030 Technician Pool and Syllabus Public Release Dec 18 2025.pdf`

This is a study aid, not an official NCVEC or ARRL product.
