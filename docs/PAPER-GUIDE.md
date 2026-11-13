# How a DiplomaOne solved paper is built (and how its cards differ from notes cards)

Working spec of the **solved-paper** product, read out of the 17 sets already in
`papers-upload/`, the publisher (`tools/publish_solved_papers.py`), the convertor
(`tools/prepare_computer_papers.js`) and the website reader (`website/app.js`, `website/styles.css`).
Read this before writing or converting a paper, the same way `docs/NOTES-GUIDE.md` is read before a unit.

---

## 0. The 30-second version

```
papers-upload/originals/<CODE>/english.html      supplied original, never edited
papers-upload/originals/<CODE>/gujarati.html     only when a Gujarati original was supplied
tools/prepare_computer_papers.js                 -> reader copy (bilingual merge / en-only mark / SVG->PNG)
papers-upload/papers/<CODE>/<session>.html|.pdf  the files that get published
tools/publish_solved_papers.py                   gates + copies into the public checkout
.github/workflows/publish-solved-papers.yml      runs the gates on PR, publishes on push to main
website/app.js  sanitizePaper()                  second, stricter gate, inside the browser
```

Public URL shape: `.../papers/<CODE>/<session>.html` and `.../<session>.pdf`,
`<session>` = `summer-2026`, i.e. `^[a-z][a-z0-9]*-[0-9]{4}$`.

---

## 1. The two families of paper we already ship

| | **Owner-supplied family** | **Computer-engineering family** |
|---|---|---|
| Example | 4351902, 4351903, DI04000241, DI04000251, DI04019011 | DI01000131, DI01000151, DI02000101, DI03000011/21/31/41/51, DI04000011/21 |
| Language | one file, `.en`/`.gu` wrappers around every block | English-only, plus `<meta name="paper-language" content="en-only">` and a bilingual notice paragraph |
| Question line | `Q1(a) · full question` | `Q.1 (a) Define …` exactly as printed |
| Answer opens with | `<h3>Answer</h3>` / `<h3>જવાબ</h3>` | `<p><strong>Question as printed:</strong> …</p>` |
| Diagrams | live inline `<svg>` (360 wide) | inert `<img src="data:image/png;base64,…">` |
| Typical size | 80–290 KB | 1.1–2.0 MB |
| Why this split | they were authored in-repo, already sanitizer-safe | they came from Drive with SVG features the old reader dropped |

Both families must pass the same gates (§5). The reader copy is the only file that differs from the
original; `originals/` is kept byte-identical so a paper can always be re-converted.

---

## 2. Document skeleton (exactly seven blocks)

```html
<!doctype html>
<html lang="en">                      <!-- "gu" for a Gujarati original -->
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="paper-language" content="en-only">   <!-- English-only copies only -->
  <title><CODE> · Summer 2026 solved paper</title>
  <style> … one inline stylesheet, no external CSS … </style>
</head>
<body><main class="page">

  <header class="hero">
    <div class="eyebrow">Solved question paper · English only · full question wording</div>
    <h1>Relational Database Management System</h1>
    <div class="meta">GTU Diploma Engineering · Computer Engineering · Semester III ·
                      Summer 2026 · DI03000031 · 18 May 2026 · 70 marks</div>
    <div class="note">
      <p><b>Question wording:</b> …</p>          <!-- how faithfully the questions are reproduced -->
      <p><b>Exam instructions:</b> …</p>         <!-- attempt all, calculators, figures = marks -->
      <p><b>Assumptions:</b> …</p>               <!-- e.g. Oracle syntax, assumed VARCHAR2 widths -->
      <p><b>Coverage:</b> …</p>                  <!-- all 28 parts included, what the answers contain -->
    </div>
  </header>

  <section class="group"><h2>Q1 · Database terminology and SELECT queries</h2> … 4 cards … </section>
  <section class="group"><h2>Q2 · SQL commands and operators</h2>              … 6 cards … </section>
  <section class="group"><h2>Q3 · SQL functions, grouping and joins</h2>       … 6 cards … </section>
  <section class="group"><h2>Q4 · Keys, constraints and normalization</h2>     … 6 cards … </section>
  <section class="group"><h2>Q5 · PL/SQL and triggers</h2>                     … 6 cards … </section>

  <footer>Source: … (which paper, whose upload, which language is authentic, syllabus caveat)</footer>
</main></body></html>
```

Rules that follow from the gates:

* Every shipped set has **5 `<section class="group">` and 28 `<details class="card">`** (4 + 6 + 6 + 6 + 6).
  New papers follow the pattern the actual paper prints — the publisher checks completeness and
  part↔summary pairing, not a fixed number.
* `h2` is a *topic summary* of the group, not the paper's own phrase: `Q2 · SQL commands and operators`.
  Gujarati originals use `પ્ર.2 · …`.
* Every group is followed by its cards directly — no wrapper `<div>` around a `details`.
* Total paper marks = 70; parts are 3 / 4 / 7 and split a(3) b(4) c(7) inside each question.
  Q1(c) carries the OR; Q2–Q5 carry a-OR, b-OR, c-OR.
* The hero `meta` line is a fixed 7-field sequence: board · programme · branch · semester · session ·
  code · exam date · marks.

---

## 3. Card anatomy

```html
<details class="card">
  <summary>
    <strong>Q.1 (c) Write SQL queries for the following, Table Name: Customer …</strong>
    <small>7 marks</small>
  </summary>
  <div class="answer">
    <p><strong>Question as printed:</strong> …</p>   <!-- verbatim, line breaks normalised -->
    … 2–5 short paragraphs, the term under discussion in <b> …
    <div class="program"><div class="program-label">Oracle SQL / PL/SQL</div>
      <p class="program-lines">CREATE OR REPLACE VIEW …<br>SELECT … FROM …;</p></div>
    <table>…</table>
    <figure><svg role="img" aria-label="…" viewBox="0 0 360 288">…</svg>
      <figcaption>…</figcaption></figure>
  </div>
</details>
```

* `summary` = question + marks chip. It is the whole table of contents; a student reading only the
  summaries must be able to see the paper.
* OR alternatives are their own card, in paper order, directly after the primary part:
  `Q.4 (c) OR Define Normalization, Explain 2NF with Example.`
* Bilingual cards wrap *each* element: `<span class="en"><strong>…</strong><small>3 marks</small></span>`
  in the summary, then `<div class="en"><div class="answer">…</div></div><div class="gu">…`.
  The reader keeps one language at a time and expects `Q1(a)` / `Q1(a) OR` keys to match on both sides.
* Answers are 60–400 words (median 57 in DI02000101 up to 402 in DI01000181); a 3-mark part is
  definition + one example, a 7-mark part is definition + classification/steps + table or diagram +
  worked example.
* Code never goes in `<pre><code>` for these papers; it goes in `.program` / `.program-lines` with `<br>`
  (the sanitizer drops `<pre>` styling but the class survives, so both work — keep the existing style).
* Every `<figure>` needs `role="img"` and an `aria-label`; the label becomes the `alt` text.

---

## 4. Diagrams inside papers

Same authoring rules as notes (§7 of `NOTES-GUIDE.md`): canvas **360 wide**, `<rect … fill="#ffffff">`
first, `font-family="Arial, Helvetica, sans-serif"`, bold title at `y≈23` in `#7B2CD9`,
subtitle `#666`, labels 9–12 px, palette purple/blue/green/orange/red on pale fills, no `<script>`,
`<style>`, `<foreignObject>`, `<image>` or `href`.

What the *browser* actually keeps is narrower — `paperDiagram()` whitelists only
`svg, defs, marker, path, line, rect, circle, text` and a fixed attribute list. So `ellipse`,
`polygon`, `pattern`, `class`, `font-weight`, `font-family` are dropped. Two consequences:

* use rect/path instead of ellipse/polygon if you want the diagram to survive natively;
* anything richer must be rasterised (`prepare_computer_papers.js` uses resvg at 640 px wide,
  `data:image/png;base64`) — that is why those ten papers are 1–2 MB. PNG payloads are capped at
  1.2 MB each and 3 MB per document.

Figures are decorative-inert on purpose: text stays selectable, diagrams are not interactive.

---

## 5. Hard gates (both must pass, in this order)

`tools/publish_solved_papers.py` — fails the whole set on any of:

| Gate | Value |
|---|---|
| Path shape | `papers/<CODE>/<session>.html` + `.pdf`, exactly two parts |
| Codes | `DI[0-9]{8}` or legacy `[0-9]{7}`; never silently mapped to a new-scheme subject |
| Sections / parts | **read from the paper**: ≥1 `<section>`, ≥1 `<details>` inside `<main>`, every section holds at least one part, every part has its own `<summary>`. No fixed count — the shipped sets are 28 parts, new papers may be 15 or 5×6. |
| Language | bilingual: `.en` blocks and `.gu` blocks equal in number and ≥1, no `en-only` marker — or `en-only` + `lang="en"` + zero `.en/.gu` |
| Size | HTML ≤ 3,000,000 bytes |
| PDF | starts `%PDF-`, `%%EOF` inside the last 2 KB, one PDF per solution |
| Filesystem | no symlinks, no path escaping the site checkout |
| Overwrite | identical file = preserved; **different existing public file = hard error** |

`website/app.js sanitizePaper()` — the runtime gate:

* Only presentational tags survive; `SCRIPT/STYLE/IFRAME/OBJECT/EMBED/FORM/INPUT/BUTTON/LINK/META/VIDEO/AUDIO` are removed whole, unknown tags are unwrapped, all attributes except a class whitelist are stripped.
* Class whitelist: `card answer note eq frac num den result paper-figure`.
* `<a href>` is **not** kept — the Original-PDF link comes from the index, not from the document body.
* `<img>` only `data:image/(png|jpeg|gif|webp);base64` under 1.2 MB.
* Fetch is `redirect:'error'`, cached per `code/session`, and the cached source is reused when the
  student flips language.

Discovery is filename-based only: the site reads the public repo tree, keeps
`papers/<code>/<session>.html`, and attaches `pdf` only when `<session>.pdf` exists (or a legacy
`Question_Paper.pdf` is referenced). No manifest, no schedule, no background polling.

---

## 6. How it looks on the site

`solved-paper` is styled to sit inside the normal reader card: purple serif `h2` per group, the
lavender `.note` box for the hero notes, white `.card`s with an `+ / −` marker, `1.8` line-height
answers, green `.result` boxes, `.frac/.num/.den` for stacked fractions, `.eq` for display maths.
Breadcrumb: `Solved papers / <subject> / Solved question paper`; toolbar: back + `Original question
paper (PDF) ↗`. Language toggle re-renders the same cached HTML in `.en` or `.gu`.

The Flutter app does **not** read papers yet: `app/lib/screens/subject_screen.dart` shows the
`Paper Solutions` section with the placeholder `paper_soon` string. Papers are a website-only feature
today.

---

## 7. Paper cards vs notes cards — the differences that matter when writing

| | Notes (`content/<branch>/semN/<CODE>/unitN.json`) | Solved paper (`papers/…`) |
|---|---|---|
| Container | JSON unit, rendered by Flutter/JS card widgets | one self-contained HTML file, inline CSS |
| Card unit | `items[]` — topic card `{h,body}` or Q&A card `{q,a}` | `<details class="card">` with `summary` + `.answer` |
| Numbering | hand-written in `h` (`1.1`, `Practical.1`) or reader-auto for `q/a` | paper numbering `Q.4 (c)` / `Q.4 (c) OR` — never renumbered |
| Structure inside | fixed `<h4>` skeleton: Definition → Explanation → Common mistake → self-check | free prose: question-as-printed → explanation → table/program/diagram |
| Marks | suggested (`question_marks_are_suggested: true`) | **official**, printed on the paper |
| Provenance | "original revision questions, not past papers" | the real paper: code + exam date + source footer |
| Language | one JSON, `languages:["en"]` or `["en","gu"]`, both in one file | `.en`/`.gu` wrappers, or explicit en-only marker |
| Diagrams | `unit.svgs[id]` referenced by `diagram` field, 360 wide | inline `<svg>` or base64 `<img>` inside the answer |
| First card | first notes card opens by default | all cards closed by default |
| Edit safety | regenerated by `build_*.py`, guarded by tests | published files are append-only; a differing file is never overwritten |
| Delivery | downloaded per unit at runtime, no APK needed | static file on Pages, fetched per paper |

Shared DNA: purple `#7B2CD9` accent, white cards on a pale page, `summary` = the scannable question,
360-wide hand-built SVG, `mark`/`b` for the key term only, no external assets, no inline handlers.

---

## 8. Definition of done for a new paper

1. `originals/<CODE>/english.html` (+ `gujarati.html`) present and untouched.
2. Reader copy in `papers/<CODE>/<session>.html`, same session name as the PDF.
3. `node tools/test_computer_papers.js` passes (bilingual structure, 28 parts, 28 texts equal to the originals, diagrams present in both language modes).
4. `python3 tools/test_publish_solved_papers.py` passes.
5. `python3 tools/publish_solved_papers.py papers-upload/papers <empty-dir>` dry run reports every file as added.
6. Visual check at 390 px and 1100 px: no clipped diagram label, no sideways-scrolling table, question text intact.
7. Only then push to `main`; the workflow publishes additively and refuses overwrites.

---

## 9. Owner's answer style (standing instruction, 2026-11-13)

Applies to **every new paper** solve. Recorded here so it survives between sessions.

**Language** — one file, both languages, *same content* in each, switched by the site's language
button. Use the established shape: `<span class="en">` / `<span class="gu">` in the summary, and
`<div class="en"><div class="answer">…</div></div>` + `<div class="gu"><div class="answer">…</div></div>`
for the body. Never mix a Gujarati sentence into the English block or vice versa. No en-only
fallback for a paper solved under this rule.

**Gujarati voice** — easy, friendly, spoken Gujarati a student can revise from (not heavy
Sanskritised textbook Gujarati). **Technical keywords stay in English inside the Gujarati sentence**:
"રેઝિસ્ટરનું **tolerance** બેન્ડ …", "**primary key** ક્યારેય NULL ન હોઈ શકે". Numbers, units,
symbols, code and question numbers are never translated.

**Depth follows the printed marks, nothing else**

| Part | Must contain |
|---|---|
| 3 marks | one-sentence definition (term in `<b>`) + 2–4 key points/classification bullets + one concrete example. No derivation, no padding. |
| 4 marks | definition + how it works / where it is used (ordered or bulleted) + a small worked example or a ≤3-column comparison table + one limitation. |
| 7 marks | definition and why it matters → **construction part-by-part** → **working step-and-reason** → classification/comparison table → one labelled diagram → worked example/numerical → 2–3 limitations/applications. |

**Construction / working questions** — always two named blocks:
`<h4>Construction — part and purpose</h4>` (ordered list, one part per step) then
`<h4>Working — step and reason</h4>` (ordered list: what happens, then why it happens). Close with
limitations/safety. This is where diploma papers award the marks.

**Numericals and derivations** — stepwise and reproducible:
1. Given/assume, every quantity with its unit ("illustrative" when the paper supplies no data);
2. formula written, then the same formula with the numbers substituted;
3. one arithmetic step per numbered line, units carried in every line;
4. bold final answer, then a one-line sanity check (magnitude/sign/units);
5. derivation: definition → assumptions → numbered steps → final relation in bold → validity limits.
   No skipped algebra, no "it can be shown that".

**Maths formatting** — real vertical fractions, owner's decision of 2026-11-13 (supersedes the
earlier plain-text choice). Any division, ratio, rate or unit conversion is written as a **stacked
fraction**, numerator on top, a rule, denominator at the bottom — never `x/5` on one line:

```html
<span class="frac"><span class="num">V</span><span class="den">R</span></span>
```

`V = IR` style products, sums, powers (`10⁻⁶`) and roots stay inline; `10⁻⁶`, `V<sub>rms</sub>`,
`× ÷ ≈ ≤ ≥ → √ π ω` are unchanged. `.frac` is whitelisted by the reader and styled in
`solved-paper` CSS (`num` gets the underline/rule, `den` sits below).

**Diagrams** — minimal: only when the question is inherently visual (construction, working, block,
circuit, waveform, flowchart, classification tree) or the paper says "with diagram". A definition-only
3-mark part gets no figure. A technical diagram that the answer depends on is drawn properly
(360 wide, palette + rules of §4); decorative figures are not added.

**Provenance** — answer the printed question as printed, at its printed marks; hero `.note` carries the
assumptions; footer keeps the source line; every card refetches nothing and cites nothing external.

### Question line inside each card (owner's decision, 2026-11-13)

The Gujarati block answers in Gujarati but **keeps the printed English question line unchanged**
(`<strong>Q.4 (c) Define Normalization, Explain 3NF with Example.</strong>` in both languages).
Only the answer body is translated, so nothing about the paper's own wording can drift. The marks
chip reads `7 marks` in English and `7 ગુણ` in Gujarati.

### Gate is structure-adaptive (owner's decision, 2026-11-13)

`SolutionParser.check()` in `tools/publish_solved_papers.py` derives the shape from the document:
`<main>` must be closed, at least one `<section>`, at least one `<details>`, every section non-empty,
`<summary>` count equal to `<details>` count, and the language blocks either balanced `.en`/`.gu` or an
explicit `en-only` marker. A paper with 15 parts, or five questions of six parts each, publishes
normally. `tools/test_publish_solved_papers.py` covers those shapes.

---

## 10. Notebook-style layout for numericals and derivations

Owner's instruction (2026-11-13): *"numericals write as we write in notebook — step by step, line by
line."* A numerical or a derivation is therefore never a paragraph. It is a stack of short lines, in
the exact order a student writes them in an answer book. Live sample: `docs/samples/paper-notebook-sample.html`.

**Markup** (classes are whitelisted in `sanitizePaper()`, so this survives on the website):

```html
<h4>Given and assumption</h4>
<div class="work">
  <p>R = 22 Ω</p>
  <p>V = 220 V</p>
  <p>t = 3 h</p>
</div>

<h4>Step-by-step solution</h4>
<ol class="steps">
  <li><span class="step-label">Formula · current</span>I = V / R</li>
  <li><span class="step-label">Substitution</span>I = 220 / 22</li>
  <li><span class="step-label">Calculate</span>I = 10 A</li>
  <li><span class="step-label">Formula · power</span>P = V I</li>
  <li><span class="step-label">Substitution</span>P = 220 × 10</li>
  <li><span class="step-label">Calculate</span>P = 2200 W = 2.2 kW</li>
</ol>
<p class="result"><b>I = 10 A, P = 2.2 kW</b></p>
```

* `.work` = the ruled block (left margin rule, one quantity/statement per line) — use it for
  given data, formula boards and derivation lines.
* `ol.steps` = auto-numbered steps; `.step-label` names the step in purple small caps
  (`Given / Formula / Substitution / Calculate / Answer` — Gujarati: `આપેલું / સૂત્ર / કિંમત મૂકો / ગણો / જવાબ`).
* `.result` = the boxed final answer; one per numerical, bold, with units.
* Math inside a step uses stacked fractions for every division:
  `<span class="frac"><span class="num">220</span><span class="den">22</span></span>` renders as 220 over 22.
  The step text never contains `220 / 22` on one line. Products stay inline: `P = 220 × 10`.
* One statement per line means one `<p>` or one `<li>` — never `a = 1, b = 2, so c = 3` in a sentence.
* Every line carries its unit; the substitution line repeats the formula with numbers in place.

**Order for a numerical:** Given → Formula → Substitution → Calculate → (repeat per quantity) →
boxed answer → Interpretation/check (1–3 bullets: magnitude, sign, unit, real-world sense).

**Order for a derivation:** Statement of what is being derived → Assumptions (bulleted) →
`.work` lines numbered so each one follows from the previous → final relation in bold →
validity/limits line. Six lines or fewer; longer algebra goes to a separate "algebra appendix" card.
