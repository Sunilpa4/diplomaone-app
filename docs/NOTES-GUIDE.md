# How a DiplomaOne unit of notes is made

This is the working specification for note content in this repo: the data model, the writing
style per section type, the diagram rules, the numerical/derivation conventions, and the gates
a unit must pass before it is published. It is derived from the 293 units already in `content/`,
the Flutter readers in `app/lib/`, and the validators in `tools/`.

Read this before writing a new unit. Everything below is enforced by code somewhere.

---

## 0. The 30-second version

```
tools/syllabus_<CODE>.txt            official syllabus text (no PDFs in the repo)
tools/subject_<CODE>.py              subject metadata + UNITS + write_unit()
tools/content_<CODE>_uN_notes.py     NOTES, SYNTAX/ALGORITHMS, VIVA, EXAM, ANSWERED, SOURCES
tools/content_<CODE>_uN_programs.py  EXAMPLES + execute_all()   (real, executed code)
tools/diagrams_<CODE>_uN.py          TITLES + main()  -> 360-wide SVGs
tools/build_<CODE>_uN.py             assembles + writes content/.../unitN.json + preview HTML
tools/test_<CODE>_uN.py              validation groups (this is the definition of "done")
python3 tools/export_app_content.py  -> build/data/  (catalog + subjects + units with svgs)
cd app && flutter test test/all_content_test.dart      -> must print "0 bad" for every unit
python3 tools/publish.py "Added <CODE> Unit N"          -> live for the app
```

The app never bundles units: it downloads `data/units/<CODE>_uN.json` on demand using the hash
list in `data/catalog.json`. So **notes changes ship without a new APK**.

---

## 1. Where content lives

| Path | Meaning |
|---|---|
| `content/<branch>/sem<N>/<CODE>/subject.json` | subject: teaching scheme, exam marks, units list, COs, practicals, books |
| `content/<branch>/sem<N>/<CODE>/unit<N>.json` | one unit of notes (the thing students read) |
| `content/<branch>/sem<N>/<CODE>/diagrams/*.svg` | hand-built SVG diagrams, 360 wide |
| `preview/<CODE>_unit<N>_preview.html` | local phone-shaped preview of that unit |
| `preview/<CODE>_unit<N>_diagrams_*.png` | contact sheets used for visual review |
| `tools/baseline_before_<CODE>.json` | sha256 of every pre-existing content file (no-regression gate) |

`content/` is the source of truth. `build/data/` and `app/assets/content/` are generated.

---

## 2. The unit JSON data model

Every unit is one JSON object. Fields marked ● are always present; the rest depend on the subject type.

```jsonc
{
  "subject": "DI05007021",          // ● subject code, must match folder + subject.json
  "unit": 1,                         // ● int
  "format": "notes",                 // ● always "notes"
  "title":  { "en": "Introduction to Information Security" },   // ● must equal subject.json units[n].title
  "hours": 6, "weightage": 15,       // ● copied from the official syllabus, never invented
  "languages": ["en"],               // ● ["en"] or ["en","gu"]
  "tabs": ["notes","programs","diagrams","syntax","viva","exam"],// ● render order, see below
  "tab_labels": { "programs": { "en": "Practical" } },           //  legacy only - see the note below
  "intro_text": { "en": "…" },       // ● the purple hero paragraph under the title

  "notes":      [ { "title": {...}, "items": [ … ] } ],          // ● main content
  "programs":   [ { "id","title","code","out","expl", … } ],     //  code/practical tab
  "diagrams":   [ { "id","title","file" } ],                     // ● every SVG must be listed here
  "numericals": [ { "id","q","a" } ],                            //  solved numerical tab
  "equations":  [ { "title", "items":[ {"name","f","terms"} ] } ],//  formula tab
  "syntax":     [ { "title", "items":[ {"name","f","terms"} ] } ],//  syntax/algorithm-reference tab
  "algorithms": [ { "title", "items":[ {"name","f","terms"} ] } ],//  alternative to syntax
  "viva":       [ { "title", "items":[ {"q","a"} ] } ],           // ● grouped viva questions
  "exam_questions": [ { "q": {...}, "marks": 4 } ],               // ● practice paper list
  "practicals":    [ { "number","title","body" } ],               //  lab guide cards
  "project_plans": [ { "number","title","body" } ],               //  micro-project cards

  "learning_outcomes": [ { "en": "CO1: …" } ],                    // ● mapped from subject COs
  "practical_numbers": [1],                                        //  syllabus practicals covered here
  "content_kind": "theory_with_safe_practical_support",
  "assessment_note": { "en": "…" },          // official marks split + "practice marks are suggested"
  "question_provenance": "Original answered revision questions; not official past papers",
  "question_marks_are_suggested": true,
  "lesson_count": 14, "answered_practice_count": 12,
  "runtime_evidence": { … },                 // only when programs/tools were really executed
  "sources": [ { "title": "…", "url": "https://…" } ]             // ● real, fetched references
}
```

### Tab ids the readers understand

`notes · programs · diagrams · flowcharts · algorithms · syntax · equations · numericals · viva · exam`

`tab_labels` is written by some older generators but the Flutter readers ignore it - the tab caption
comes from the app's own `l10n.dart` table (`syntax` → "Syntax", `equations` → "Equations"). Do not
rely on it to rename a tab; choose the tab id whose built-in caption fits.

`exam_questions` is normalised to `exam` on export. Unknown tab ids are silently dropped so old
APKs never crash, but a dropped tab means students never see that section — always pick from the list.

Practical defaults:

| Unit type | `tabs` |
|---|---|
| programming subject (C/Python) | `notes, programs, diagrams, algorithms, numericals, viva, exam` |
| theory with formulas (electronics, electrical, civil…) | `notes, diagrams, equations, numericals, viva, exam` |
| theory, non-numeric (security, management…) | `notes, programs, diagrams, syntax, viva, exam` |

### Notes tab: the only two card shapes

`notes` is a list of **sections** (lavender headers). Each section holds **items**, and an item is
either a *topic card* or a *Q&A card*:

```jsonc
// topic card  -> numbered? no; heading bold; tap to open
{ "h": {"en":"1.2 The CIA triad"},
  "body": {"en":"<p>…</p><table>…</table>"},
  "diagram": "sec1_cia",            // optional, id from diagrams[]
  "programs": ["sec1p01"],          // optional, ids from programs[]
  "examples": ["u2n1"],             // optional, ids from numericals[]  (renders as gold EX box)
  "syllabus_item": "1.2" }          // optional provenance tag, e.g. "2.3", "Practical.1", "Project.4"

// Q&A card  -> numbered by the reader
{ "q": {"en":"What is a passive attack?"}, "a": {"en":"…"} }
```

Rendering rules that constrain writing:

* The **first card of the notes tab is open** on entry; everything else is collapsed. Order
  sections by exam importance, not alphabetically.
* Section headers get expand-all / collapse-all buttons; keep sections homogeneous.
* `diagram` renders inline under the body with a `📐 title · tap to zoom` caption.
* `examples` render as a gold "EX" box; `programs` as a teal "PROG" box. Both are lookups — a
  dangling id renders as nothing, so link only ids that exist.
* Items are auto-numbered when the card has `q/a` (exam, viva). Topic cards keep their
  hand-written numbering inside `h` (`1.1`, `8.10`, `Practical.1`).

---

## 3. Design language (the part that decides how much you can write)

The app is a phone layout: 412 dp logical width, purple `#7B2CD9` bar, lavender `#EADDF7`
section headers, white cards, 10 dp gutters.

| Element | Behaviour | What it means for the writer |
|---|---|---|
| Card body | HTML rendered at 15 px / 1.6 line height | 2–4 short paragraphs per card; long walls of text are unreadable |
| `<h4>` | purple 700, 12/6 margins | the only in-card sub-heading — use it as a signpost, not decoration |
| tables | ≤3 columns fill the width; **4+ columns scroll sideways** | comparison tables: 3 columns max; put lists of 6+ properties in bullets instead |
| `<pre>` | monospace code block, horizontal scroll | algorithms and C/Python go in `<pre>`, never in prose |
| `<code>` | purple pill, mono | inline identifiers only (`STACK[MAX]`, `top = -1`) |
| `<details class="self-check">` | collapsible "check yourself" | one per concept card at most |
| `<img>` | not part of the supported tag set (§4.4) | new units use the `diagram` field; the base64 images in some 2025-era files are legacy and are not copied |
| priority stars / `key: true` | stripped on export (explicit user request) | do not mark "important" items |

Bold (`<b>`) is for the term being defined and for numbers in a result — not for whole sentences.

---

## 4. The notes tab: detailed writing standard

### 4.1 Structure of a unit

1. **One section per syllabus unit-part / topic cluster** — typically 5–9 sections.
2. Inside a section, one card per *examinable* idea, in syllabus order.
3. The final notes section is always **answered practice** (see §10.3).
4. Practicals/projects get their own sections (`Practical.1 …`, `Project.1 …`) when the syllabus
   has them.

Typical sizes actually shipped (median per unit):

| Reference subject | Sections | Topic cards | Diagrams | Programs | Viva | Exam Qs |
|---|---|---|---|---|---|---|
| DI03000021 Data Structures | 4 | 17 | 11 | 14 | 28 | 18 |
| DI01000151 Basics of Electronics | 5 | 28 | 8 | – | 31 | 17 |
| DI05007021 Information Security | 6 | 32 | 10 | 10 | 36 | 16 |
| DI03000091 Electrical Instrumentation | 14 | 19 | 9 | 4 | 5 | 6 |

A unit JSON is normally **55–140 KB**. Under ~40 KB usually means the topics got summarised
instead of explained.

### 4.2 The standard body skeleton

Every card is built from the same ordered blocks. Use the `<h4>` names consistently — they are
what students scan for, and the unit tests assert on the key phrases inside them.

**Concept / definition card**

```
<h4>Definition</h4>                  one-sentence definition, term in <b>
<h4>Explanation and application</h4> 3–6 bullets: how it works, where it is used
<h4>Common mistake / conditions</h4> the trap, stated as a rule
<details class="self-check">…</details>
```

**Classification card**

```
<h4>Classification / representative type</h4>  a 3-column table: Type | Meaning | Example
<h4>Comparison</h4>                            another table or bullets
```

**Construction / working card** (machines, instruments, hardware)

```
<h4>Construction — part and purpose</h4>   ordered list, one part per step
<h4>Working — sequence and reason</h4>     ordered list: what happens, and why
<h4>Limitations and safety</h4>            bullets
```

**Procedure / practical card**

```
<h4>Aim and apparatus</h4>
<h4>Connections and instruments</h4>
<h4>Qualified-supervised procedure</h4>    <ol> numbered steps with a stop criterion
<h4>Precautions</h4>
<h4>Observations and result</h4>           table with blank/"actual" cells only
```

**Numerical card** — see §5. **Derivation card** — see §6.

### 4.3 Sentence rules

* First sentence of every card answers the heading. No wind-ups ("In this topic we will…").
* One idea per bullet, ≤ ~25 words. If a bullet needs a semicolon chain, split it.
* Define the symbol before using it; state units at first use.
* Prefer concrete college examples (result portal, hostel attendance, a lab trainer) over abstractions.
* State limits explicitly: "this is a calculation, not a wiring instruction", "this assumes ideal
  conditions". The shipped units do this consistently and it reads well, not pedantically.
* Contractions are fine; slang, emojis and exclamation marks are not.
* No real credentials, phone numbers, hostnames, or "attack this service" instructions.

### 4.4 HTML you may use

`p b strong i ul ol li h4 table thead tbody tr th td code pre sub sup br details summary span div`

Not allowed: `script`, `style`, `link`, `img` with a file or remote `src`, `iframe`, `svg` inside
body, inline `on…=` handlers, external `href` in content (links live in `sources`). Older units from
the chemical/electrical series contain big inline base64 `<img>` figures; that is legacy baggage —
new units use SVG files instead.

Superscripts/subscripts are Unicode or `sub`/`sup`: `10⁻⁶`, `V<sub>rms</sub>`, `x²`.
Math is plain text with `× ÷ ≈ ≤ ≥ → √ π Φ ω` — there is no MathJax in the app.

---

## 5. Numericals: the four-block convention

Numericals live in **two places** and both use the same voice:

* `numericals: [{id, q, a}]` — the dedicated tab (numbered cards in the app), linked from a theory
  card with `"examples": ["u2n1"]`.
* inside a notes card, as a worked example in `<h4>` blocks.

Block order (this is the convention every recent unit follows):

```html
<h4>Given and assumptions</h4>
  every quantity with its unit; state the model/assumption (uniform wire, ideal diode, 50 Hz…)
<h4>Formula</h4>            (or "Conversion" when a unit change is the step)
  the equation, then the same equation with numbers substituted
<h4>Step-by-step solution</h4>   <ol>
  one arithmetic step per <li>, keep units in every line
<h4>Interpretation and check</h4>
  bold final answer with unit, then one line of sanity: magnitude, sign, order-of-magnitude
```

Rules:

1. **Never invent data.** If the syllabus gives no reference value, pick realistic values and say
   "illustrative".
2. Significant figures match the given data (3 s.f. is the house default).
3. Bold the answer: `<p><b>R = 0.17 Ω</b></p>`.
4. Add the check — students lose marks for unsupported numbers, and the check is what makes a
   numerical a *teaching* example.
5. Traces (stack/queue/expression conversion, register tables, titration rows) go in a
   `<table>` with one column for step/state, not prose.
6. Where a numerical could be misread as an operating instruction, close with a scope line.

---

## 6. Derivations: moderate length, five required parts

`"derivation": true` marks the item. The body then follows:

```
<h4>Definition</h4>                       what the quantity is, in one sentence
<h4>Detailed explanation and application</h4>  bullets: when it holds, what it ignores
<h4>Assumptions and ordered derivation</h4>    <ol>, one line per step, symbols defined as they appear
<h4>Final relation</h4>                   bold equation (+ the rearranged form students must memorise)
<h4>Worked example / interpretation</h4>   one substitution, then units/validity limits
```

Owner's standing instruction (recorded in the electrical subjects as `derivation_policy`):

> moderate-length derivations with defined symbols, assumptions, necessary steps, final equation and
> units/validity.

So: **no 20-step mathematical marathons, and no "it can be shown that".** Each step must be a
statement a diploma student could reproduce in a 4-mark answer. If a derivation needs more than
~6 steps, split it: state the result, derive the practical consequence, and put the long algebra in
a numbered appendix card.

---

## 7. Diagrams: hand-built SVG, 360 px wide

Diagrams are authored as SVG strings in `tools/diagrams_<CODE>_uN.py` using the shared primitives
(`flowchart_lib.py`: `svg text arr rbox decision terminal process io row ...`, built on
`diagrams_DI01000151_u1.py`). No external assets, no CSS, no `<marker>`.

Hard rules (enforced by `test_<CODE>_uN.py`):

| Rule | Value |
|---|---|
| Canvas width | exactly **360**; height whatever the content needs (usually 300–700) |
| Background | `<rect … fill="#ffffff"/>` filling the canvas |
| Fonts | declare `font-family="Arial, Helvetica, sans-serif"` (export rewrites it to **DejaVu Sans**) or `DejaVu Sans` directly; bold = `font-weight="bold"` |
| Forbidden | `<script>`, `<style>`, `<marker>`, `<foreignObject>`, `<image>`, any `href=` |
| Text bounds | every text must sit inside 1 px of the canvas — checked with real DejaVu metrics, so measure with the same font the app uses |
| Raster check | rendered with resvg + DejaVu at 1.25×; must not be blank (≥20 distinct colours) |
| Structure | `title` at y≈18 (`size 14–14.5`, bold, purple `#7B2CD9`), optional subtitle y≈48 (`10.5`, `#666`), footer notes at the bottom (`10.2`, `#666`) |
| Content width | content boxes 324 wide, centred at x=180, 18 px margins |
| Text size | labels 10.2–12; multi-line via `\n` (the library offsets lines by size+2) |
| Palette | purple `#7B2CD9`, blue `#1565C0`, green `#2E7D32`, orange `#B66A00`/`#E07B00`, red `#BD2543`; fills are pale versions of the stroke |

Practical limits: at 11 px in a 324 px box, keep a line to **~45–50 characters**; a 3-line footer at
10.2 px fits in the last ~60 px of the canvas; leave ~20 px between a box and the next arrow head.
Two-column layouts work (x≈95 and x≈265, width ~150 each); three columns get cramped below 11 px.

Naming and wiring:

* id = lowercase snake, subject-scoped: `sec1_cia`, `ds2_stack_array`, `inst3_bridge`.
* `TITLES = {id: "Human title"}` in the diagrams module; the same id goes in `unit["diagrams"]`
  as `{"id","title","file": "diagrams/<id>.svg"}`, and a notes card references it by id.
* Every diagram must be referenced by at least one card, and every referenced id must exist —
  both directions are tested.
* Caption + zoom come free: `📐 <title> · tap to zoom`, pinch/zoom 1–5× in a full-screen viewer.
* Contact sheets (`preview/<CODE>_unit<N>_diagrams_1.png`) are generated for visual review; check
  that no label is clipped and that arrows do not cross text (add a white backing rect if they do).

Content rule: **one idea per diagram**. A diagram that needs a paragraph of explanation inside it
should be two diagrams.

---

## 8. Programs tab (code subjects and "show me" theory subjects)

```jsonc
{ "id": "sec1p01",
  "title": { "en": "Integrity check against a trusted reference" },
  "code":  { "en": "…" },      // real source, ≤ 78 chars per line
  "out":   "…",                // the actual captured stdout, byte for byte
  "expl":  { "en": "…" },      // what to notice; key name is exactly "expl"
  "plot":  "diag_id",          // optional: render a diagram as the output figure
  "run":   "html" }            // optional: web subjects get a ▶ Run button
```

* Output is **captured, never typed**. `execute_all()` runs the code each build and the test
  re-executes it and compares (`self.assertEqual(execute_all(), unit['programs'])`).
* Code must be deterministic: no random values, no timings, no ephemeral ports, no timestamps.
  If a run must show live data (ports, addresses), print a stable field, not the whole row.
* Hidden secrets stay out: if a key/token is needed, generate it in RAM and never print it.
* ≤ 12 programs per unit; each program gets a card in the notes by `programs: ["id"]` and appears in
  the Programs tab list.
* Web/CSS/HTML subjects: set `run: "html"` and verify with `tools/web_check.py` (screenshots at
  390 px and 1100 px, no JS errors).

---

## 9. Syntax, algorithms and equations tabs

Three variants of the same structure — grouped reference cards:

```jsonc
{ "title": {"en":"Expression conversion"},
  "items": [ { "name": {"en":"Infix to postfix"},
               "f": "operator stack; operands -> output",     // mono chip / code line
               "terms": {"en":"Pop while precedence is higher; stop at '('."} } ] }
```

* `syntax` — language constructs (C/Python): `f` is the syntax skeleton, `terms` the rules.
  For code subjects `f` is drawn as a code block.
* `algorithms` — pseudocode blocks, one algorithm per item (PUSH/POP, traversals…). These are the
  same algorithms printed in the notes `<pre>` blocks.
* `equations` — formula sheet: `f` is the equation (rendered big, purple), `terms` defines each
  symbol with its unit. Grouped by theme; 3–14 items per unit.

Keep this tab a *revision sheet*: no explanation paragraphs, one line of meaning per entry.

---

## 10. Viva, exam questions and answered practice

### 10.1 Viva

Grouped: `[{ "title":{"en":"Stack"}, "items":[{"q":…,"a":…}] }]`.
26–36 questions per unit, grouped 6–10 per topic, answer in **one sentence** (two if a formula is
needed). Questions must be answerable from the notes, in the order a viva would ask them.

### 10.2 Exam questions

```jsonc
{ "q": {"en":"Practice: Define information security and explain why a college needs it."}, "marks": 3 }
```

* 12–18 per unit; marks are **3 / 4 / 7** (across the shipped units: 4-mark ≈ 43 %, 7-mark ≈ 41 %,
  3-mark ≈ 13 %, the odd 6 where a subject's paper uses it).
* Always prefixed `Practice:` when they are original compositions.
* `question_provenance` and `question_marks_are_suggested: true` must be set, and the assessment
  note must say the marks are suggested, not an official paper/weightage.
* Never present them as GTU past-paper questions, never claim a guaranteed paper pattern.

### 10.3 Answered practice (last notes section)

Every practice question gets a model answer in the final notes section, matched 1:1:

```
item.h    = "Practice 4. <the question>"
item.body = the model answer, in the same h4 skeleton as a theory card
unit.answered_practice_count = len(practice)
```

The test zips `PRACTICE`, `exam_questions` and the last notes section together and asserts they
correspond exactly, so question text and answer cannot drift apart.

---

## 11. Practicals, projects and the lab kit

Syllabus practicals become cards tagged `"syllabus_item": "Practical.3"` and
`"practical_number": 3`, plus an entry in `unit["practicals"]`:

```jsonc
{ "number": 3, "title": {"en":"Implement PUSH and POP"},
  "body": {"en":"<h4>Aim and apparatus</h4>…"} }
```

Honesty rules (these are the difference between a usable lab guide and a fake one):

* State what was **actually** executed, in `runtime_evidence` (python version, OS, arch, which
  programs ran, what was *not* attempted).
* Anything not run is labelled **guided**, never "performed": `Windows ipconfig`, `traceroute`,
  `tcpdump`, `Kali` demos, Packet Tracer simulations, hardware experiments.
* If a command was denied (e.g. ping without sockets), report the denial rather than inventing
  success.
* Safety line for hardware/electrical: energised work only under qualified supervision; numericals
  are calculations, not wiring instructions.
* Where a kit is exported (`export_<CODE>_uN_practicals.py`), it is a deterministic ZIP with:
  programs + `expected/*.txt` + `runtime.json` + `README.md` + a blank journal CSV (15 files in the
  reference implementation), no pip dependencies, no binaries, and the build must work offline
  (the test patches `subprocess.run` and `socket` to fail during export).

---

## 12. Subject file and registering a new subject

`subject.json` drives the subject page (exam scheme strip, unit list with available/unavailable
badges, practicals, books):

*(Values below are illustrative — hours, weightage, category and year must come from the syllabus.)*

```jsonc
{ "code":"DI04000041", "name":{"en":"Cloud Computing"}, "branch":"computer", "semester":4,
  "syllabus_year":"2024-25", "category":"PCC", "type":"theory",
  "languages":["en"], "code_lang":null,
  "teaching":{"lecture":3,"tutorial":0,"practical":2},
  "exam":{"theory_ese":70,"theory_pa":30,"practical_pa":20,"practical_ese":30,"total":150,"credits":4},
  "prerequisites":[…],
  "units":[{"no":1,"title":{"en":…},"hours":…,"weightage":…,"topics":[…],"file":null}],
  "course_outcomes":[…], "theory_rbt_percent":{…}, "practicals":[…], "books":[…] }
```

`write_subject()` sets `"file": "unitN.json"` only when that file already exists — that is what makes
a unit appear in the app (`available_units`). Never fake it.

New subject must also be registered in `tools/export_app_content.py`:

1. `SUBJECTS[code] = (english, gujarati_or_None, category, credits, type, alt_code)`
2. `BRANCH_SEMS[branch][semester] = [codes…]` in display order.

Otherwise it exports but never shows in Browse.

---

## 13. Language policy

* `languages: ["en"]` → **English only**: no `gu` keys anywhere, no Devanagari/Gujarati codepoints
  (the IS validator asserts this over the whole unit and subject).
* `languages: ["en","gu"]` → every user-visible string gets both `en` and `gu`; `tr()` picks the
  active language and falls back to `en` when `gu` is missing, so a missing translation silently
  shows English — point parity is checked by test where it matters.
* Technical symbols, code, and units stay in Latin script in both versions.
* 44 of 55 shipped subjects are bilingual; the newest Computer Sem 5 subjects are English-only by
  explicit owner decision.

---

## 13b. Review workshop (HTML previews for what was written now)

`preview/` already contains hundreds of committed previews, so a reviewer cannot tell which
units are new. `tools/notes_workshop.py` keeps a separate **shelf** that only lists units
explicitly added while working on them.

```bash
python3 tools/notes_workshop.py add DI04000041 1     # render preview + put it on the shelf
python3 tools/notes_workshop.py render --all         # re-render after editing content
python3 tools/notes_workshop.py check --all          # link integrity + SVG text-bounds audit
python3 tools/notes_workshop.py list                 # shelf, with fresh/stale state
python3 tools/notes_workshop.py serve --port 8800    # live review over HTTP (0.0.0.0)
python3 tools/notes_workshop.py clear                # empty the shelf
```

| File | Meaning |
|---|---|
| `preview/workshop/index.html` | shelf page - only the units added here, with counts and a review checklist |
| `preview/workshop/<CODE>_u<N>.html` | self-contained phone-shaped preview (same renderer as the app) |
| `preview/workshop/manifest.json` | the shelf: code, unit, build time, source sha1, stats |

Notes:

* The preview is byte-identical to what the app draws: purple bar, lavender section headers,
  tap-to-open cards, inline SVG diagrams with a tap-to-zoom viewer, gold EX boxes for numericals.
* Each preview carries a **DRAFT** badge linking back to the shelf; nothing here is published.
* `check` is the fastest quality gate before asking for a human review: it resolves every
  diagram/program/numerical link in both directions and measures every SVG label with the real
  DejaVu advance widths (the app's bundled font), so a clipped label is caught before it ships.
* Building a unit with `build_<CODE>_uN.py` calls the workshop automatically, so the shelf is
  always current after a rebuild.

## 13c. Foundation chapters (unit 0) and "Branch: All" subjects

Some subjects assume school-level tools that a first-semester diploma student may not have. For
Mathematics-I (`DI01000021`) we author one extra chapter ourselves: **Unit 0, "Start Mathematics
From Zero"**. It is *not* GTU content, so the data says so explicitly.

```python
# subject.json (tools/subject_DI01000021.py)
{"no": 0, "title": tr("Start Mathematics From Zero (Foundation)"),
 "hours": 0, "weightage": 0, "official": False, ...}
"foundation_unit": {"no": 0, "official": False, "why": "..."}
# unit0.json
{"unit": 0, "hours": 0, "weightage": 0, "official": False, "foundation": True, ...}
```

Rules:

* A foundation unit is **unit 0**, always with `hours = 0` and `weightage = 0` (`write_unit`
  refuses anything else), `official = false` and `foundation = true`. Never add it to
  `theory_marks_by_unit`, never claim GTU marks for it, and say so in `assessment_note`.
* The app prints `L('own_chapter')` - "Foundation chapter · our own, not in the GTU syllabus" -
  instead of the hours/weightage line whenever a unit has `official: false` (subject list and
  the unit hero card).
* It is written like any other unit (cards, diagrams, formula sheet, numericals, viva, practice
  with model answers) but with more repetition and checks, because the reader is starting from
  zero. Unit 0 of Mathematics-I has 31 taught cards, 22 solved numericals and 14 answered practice
  questions, all linked two ways.
* **Common subjects** live in `content/common/sem<N>/<CODE>/` and carry
  `"branch": "common"`, `"common_to_all_branches": true`. `tools/export_app_content.py` inserts a
  common code into semester *N* of **every** branch, so "Branch: All" really means all branches -
  the test asserts that the catalog lists it under all 27 branches.

## 14. Build → review → verify → publish

```bash
# 1. build one unit (writes content JSON, SVGs, preview HTML, practical ZIP)
python3 tools/build_DI05007021_u1.py

# 2. validation groups for that unit
python3 -m unittest tools.test_DI05007021_u1.py -v

# 3. visual review
#    open preview/DI05007021_unit1_preview.html  (phone-shaped, same cards as the app)
#    preview/DI05007021_unit1_diagrams_1.png      (contact sheet)

# 4. full export (all subjects, ~2 s)
python3 tools/export_app_content.py                 # -> build/data
python3 tools/export_app_content.py --app-assets    # also refresh the bundled offline fallback
                                                    # (only before an app build – it is small on purpose)

# 5. renderer check for every unit (needs Flutter)
cd app && flutter pub get && flutter test test/all_content_test.dart   # expect "0 bad" per unit

# 6. compatibility of the export shapes with older readers
python3 tools/test_export_compatibility.py

# 7. publish notes (no APK needed)
python3 tools/publish.py "Added DI04000041 Unit 1"
```

`tools/publish.py` clones `diplomaone-content`, regenerates `data/`, commits and pushes; GitHub Pages
serves it. `tools/sync_code.py "msg"` is for app/tool changes and triggers the APK/web build.

Current export baseline: **55 subjects / 293 units / 348 hashed files**. The bundled
`app/assets/content` fallback intentionally holds only 4 subjects (it exists so a fresh install can
paint Browse offline) — refresh it with `--app-assets` only when shipping an app build.

---

## 15. Definition of done — the gate list

A unit is publishable only when all of these hold (all are real assertions from
`test_<CODE>_uN.py`; copy that file as the template):

**Curriculum**
- [ ] code/semester/syllabus_year/category match the official document; hours + weightage sum to the
      official total (e.g. 45 h / 100 %)
- [ ] exam and teaching schemes copied exactly; COs mapped; practicals count matches the syllabus
- [ ] every syllabus topic appears in a unit card (coverage asserted by keyword or `syllabus_item`)
- [ ] `tools/syllabus_<CODE>.txt` stores the source text and its sha256

**Content**
- [ ] section/card counts in the expected band; no card without a heading
- [ ] every diagram id and program id linked from a card, and every link resolves
- [ ] HTML balanced (`Fragment().finish()`), no unsupported tags, no `data:` images
- [ ] English-only units contain no Gujarati codepoints and no `gu` keys
- [ ] practice questions ↔ answered practice ↔ `exam_questions` correspond 1:1
- [ ] no priority stars / `key` flags

**Rendering**
- [ ] `flutter test test/all_content_test.dart`: **0 bad** for every unit, at 412×880
- [ ] every SVG: width 360, no forbidden elements, text inside bounds (DejaVu metrics), rasterises
      to a real picture
- [ ] preview HTML: all tabs present, expected card counts, no external `src`/`href`

**Reproducibility and safety**
- [ ] rebuild is byte-identical (`build_*.py` run twice → same hashes)
- [ ] every program re-executes to its stored `out` on a clean interpreter
- [ ] `baseline_before_<CODE>.json` sha256s of all pre-existing content still match (no collateral edits)
- [ ] exported older units are byte-identical to what is live
- [ ] no credentials, binaries, or generated junk in the deliverables

---

## 16. Do / Don't

**Do**
* Write from the syllabus outward: one official topic line → one card → one exam answer.
* Keep the h4 vocabulary stable (`Definition`, `Explanation and application`, `Construction — part and purpose`,
  `Working — sequence and reason`, `Assumptions and ordered derivation`, `Given`, `Find`,
  `Step-by-step solution`, `Interpretation and check`, `Common mistake / conditions`, `Precautions`).
* Give every numerical a check line and every derivation a validity line.
* Reuse the shared SVG primitives; a new shape added to `flowchart_lib.py` is fine, a copied third
  variant is not.
* Run the build and the tests before saying a unit is finished.

**Don't**
* Hand-edit `content/**.json` (they are generated by the build script; the next rebuild wipes edits).
* Edit `build/data` or `app/assets/content` by hand.
* Add Gujarati to an English-only subject, or "key/important" stars anywhere.
* Claim a practical was performed, or a question is an official GTU paper question.
* Put screenshots/PNGs inside note bodies — diagrams are SVG files listed in `diagrams[]`.
* Commit `.secrets/`, keystores, `build/`, or generated previews that are gitignored.

---

## Appendix A — minimal unit skeleton

```python
# tools/subject_<CODE>.py
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / 'content/computer/sem4/DI04000041'
DIAG_DIR = SUBJ_DIR / 'diagrams'
TABS = ['notes','diagrams','equations','numericals','viva','exam']
def tr(s): return {'en': s}

UNITS = [(1, 'Unit One Title', 8, 20, ['topic a', 'topic b']), ...]
SUBJECT = {...}   # as in §12

def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True); DIAG_DIR.mkdir(exist_ok=True)
    spec = SUBJECT['units'][unit['unit'] - 1]
    assert unit['title'] == spec['title']
    assert (unit['hours'], unit['weightage']) == (spec['hours'], spec['weightage'])
    (SUBJ_DIR / f"unit{unit['unit']}.json").write_text(json.dumps(unit, ensure_ascii=False, indent=1) + '\n')
    write_subject()
```

```python
# tools/build_<CODE>_uN.py
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
from subject_<CODE> import SUBJECT, DIAG_DIR, TABS, tr, write_unit
from content_<CODE>_uN_notes import NOTES, EQUATIONS, VIVA, EXAM, ANSWERED, SOURCES
from diagrams_<CODE>_uN import TITLES, main as draw
from preview_builder import build_preview

draw()
unit = {
 'subject':'<CODE>','unit':N,'format':'notes','title':tr('…'),'hours':H,'weightage':W,
 'languages':['en'],'tabs':TABS,'intro_text':tr('…'),
 'notes': NOTES + [ANSWERED],
 'diagrams':[{'id':i,'title':tr(t),'file':f'diagrams/{i}.svg'} for i,t in TITLES.items()],
 'equations':EQUATIONS,'viva':VIVA,'exam_questions':EXAM,
 'learning_outcomes':[tr('CO1: …')],
 'question_provenance':'Original answered revision questions; not official past papers',
 'question_marks_are_suggested':True,
 'assessment_note':tr('… official marks … practice marks are suggested …'),
 'sources':[{'title':n,'url':u} for n,u in SOURCES],
}
write_unit(unit)
build_preview(unit, SUBJECT, str(DIAG_DIR), str(ROOT/f'preview/<CODE>_unitN_preview.html'))
```

## Appendix B — file naming

| Kind | Pattern | Example |
|---|---|---|
| syllabus text | `tools/syllabus_<CODE>.txt` | `syllabus_DI04000041.txt` |
| subject module | `tools/subject_<CODE>.py` | `subject_DI04000041.py` |
| notes / programs / diagrams | `tools/content_<CODE>_u<N>_*.py`, `tools/diagrams_<CODE>_u<N>.py` | `diagrams_DI04000041_u2.py` |
| build / test / practical export | `tools/build_…_u<N>.py`, `tools/test_…_u<N>.py`, `tools/export_…_u<N>_practicals.py` | |
| unit data | `content/<branch>/sem<N>/<CODE>/unit<N>.json` | `content/computer/sem4/DI04000041/unit2.json` |
| common subject unit | `content/common/sem<N>/<CODE>/unit<N>.json` | `content/common/sem1/DI01000021/unit0.json` |
| diagram | `content/<branch>/sem<N>/<CODE>/diagrams/<id>.svg` | `cc2_vm_layers.svg` |
| preview | `preview/<CODE>_unit<N>_preview.html` | |
