# Solved-paper upload batches

## Original seven Summer 2026 HTML sets

These files came from the owner's `papers-manual-upload.zip` in Google Drive. The original GTU question PDFs are unchanged. The supplied solution HTML is retained, except that the primary Q1(c) in DI04000241 and DI04000251 was incorrectly labelled “OR”; the English and Gujarati labels were corrected against the original PDFs (including the Gujarati alternative marker in DI04000251). No other answer changes were made.

Each file pair is published under the same `papers/<subject-code>/summer-2026` path by `.github/workflows/publish-solved-papers.yml`. The publisher validates the supplied bilingual HTML, pairs it with its PDF, and refuses to overwrite a different existing public file. It runs on relevant pushes to main, not on a schedule. The seven-digit codes `4351902` and `4351903` are legacy GTU codes; they are separate from DI codes and are not silently mapped to new-scheme subjects.

Checks confirmed PDF subject codes and the first questions match the respective solution files, and that every solution has 28 question sections in each language. This is not an independent verification of every answer or diagram; educational content should be reviewed against the original question papers.

## Computer Engineering Summer 2026 papers

Ten sets from the owner's `Computer Engineering Paper Solutions` Drive folder cover DI01000131, DI01000151, DI02000101, DI03000011, DI03000021, DI03000031, DI03000041, DI03000051, DI04000011 and DI04000021. The supplied HTML originals are retained under `originals/<code>/`; all ten original PDFs are unchanged and the 21 individual HTML/PDF files matched the corresponding Drive checksums. All PDF subject codes were checked in extracted text. These structural and identity checks do not independently verify every solution, formula or diagram.

Basics of Electronics (DI01000151) was supplied as separate English and Gujarati files. The reader copy combines the matching question parts so the website language toggle chooses the respective original text. The other nine solutions were supplied only in English: both website language settings show the English answer and an explicit English-only notice rather than presenting it as a Gujarati translation. The publisher requires either the existing bilingual structure or an explicitly marked English-only document with 28 question parts.

The existing deployed reader cannot preserve every SVG feature in these papers, so the reader copies contain inert PNG renderings of the original diagrams. Text and code examples remain selectable. The original vector diagrams and original full HTML are preserved in `originals/`. The reader compatibility test compares every answer's text with its original and checks all 28 parts and diagrams in each website language mode. To regenerate these ten reader copies, install `jsdom@26` and `@resvg/resvg-js` in a local Node environment and run `node tools/prepare_computer_papers.js`; the original HTML files are the input. Raster output may vary with fonts or library versions, so review changes before publishing. The publisher refuses to overwrite any differing existing public file.

## Mechanical Engineering 2025 papers

The owner's combined `DI01000181` (English and Gujarati) and `DI01000191` (English only) Winter 2025 / Summer 2025 HTML files are stored unchanged in `originals/`. The four reader copies separate the two exam sessions and convert the original embedded SVGs to inert images for the current reader. The reader retains the original questions, answers, diagrams, and mathematical fractions; the original text/diagrams can be inspected in the saved source HTML. These are unofficial model answers and have not been independently verified. The 2025 original question PDFs were not found in the supplied folder and are not invented or linked; the copies explicitly say so. `missing-originals.json` lists these four reviewed exceptions and the publisher refuses a missing or stale exception. Other papers still require their matching original PDF. The existing Summer 2026 papers are distinct exams and are unchanged. The Summer 2026 PDFs in Drive are described as exports of those existing solutions, not new answers.

## Common-subject PDF study solutions

The owner's `Common Subjects - Solved Question Papers` Drive folder contains Mathematics-I (DI01000021, semester 1, all branches) and Applied Physics (DI01000121, semesters 1 and 2). This upload adds both supplied exam sessions—Winter 2025 and Summer 2026—for each subject: four matched original/solution pairs (eight PDFs). `common-subject-pdf-provenance.json` records the original Drive filenames, Drive MD5 values and local SHA-256 values. Every PDF was checksum-verified against Drive and retained byte-for-byte; original question papers are separate from the supplied solutions.

Mathematics-I solutions are English only. Applied Physics solutions provide English and easy Gujarati explanations, worked calculations and labelled schematics. The supplied solutions state that they cover all 14 MCQs and all choices in the eight “attempt any two” sections; students should still follow the printed exam instructions. Source notes flag ambiguities and assumptions, including the Mathematics-I Summer 2026 wording issues and Applied Physics numerical conventions. These are unofficial study materials, not GTU answer keys, and answers, OR-choice completeness and diagrams were not independently verified. Graphs, diagrams and fractions are rendered as images in the PDFs, so some content may not be searchable; Gujarati text extraction may also be imperfect.

## Civil and Chemical PDF study solutions

The 33 Civil and Chemical exam sets are listed with original source names, Drive MD5 checksums and SHA-256 checksums in `pdf-batch-provenance.json`. Each `papers/<code>/<session>.solution.pdf` is the owner's **unofficial solution**, and `<session>.pdf` is the separate original question paper. They are byte-for-byte the Drive files, not a conversion. Checks compared subject code and session in both PDFs, verified all 66 Drive checksums, and found all 15 question-number/part labels in each solution; this is not independent verification of answers, alternative choices or diagrams. Source PDF languages appear together; their accessibility and text selection depend on the PDF and PDF viewer, and Gujarati text extraction can be imperfect.

This batch contains Civil DI01006021, DI03006011, DI03006021, DI03006031, DI03006041 and DI03006051, and Chemical DI01005011, DI01005021, DI02005011, DI02005021, DI03005011, DI03005021, DI03005031, DI03005061, DI04005021, DI04005041, DI04005071, 4350501 and 4360501. The seven-digit codes are older-scheme subjects, not renamed to DI codes. Cross-listing by name warns that the syllabuses can differ. Missing years have not been invented.

The browser discovers uploaded papers on demand, without scheduled scanning. When a matching `<session>.html` is present, it takes precedence over `<session>.solution.pdf`; the two do not create duplicate exam entries. Solved papers remain grouped under their catalog subject's actual branch and semester. Linked older-scheme papers follow the matching subject but retain a scheme warning, rather than being relabelled with a DI code. Future PDF-only uploads receive an honest conversion-needed notice and optional links, **not an embedded PDF viewer**. A PDF is an archive/download, not question-card content.

## Individual-question card refresh

All **37 formerly PDF-only sets** above now have actual HTML `<details class="card">` question/answer readers alongside their unchanged original/solution PDFs. There are **1,076 cards and 3,129 lossless WebP excerpts**. The 33 Civil/Chemical engineering sets have 28 parts, including OR alternatives. Each Mathematics-I and Applied Physics paper has **38 items**: 14 MCQs plus all three choices in the eight remaining groups. Maths stays English-only and says so in either website language mode; no Gujarati translation has been invented.

`tools/prepare_pdf_paper_cards.py` segments the original solution by question number and language. English prose is selectable HTML; equations, fractions, diagrams, tables and all Gujarati content use cropped original pixels inside the matching question's summary/answer. They are not whole-PDF frames or full-page scans. Small source print can be enlarged in a keyboard-accessible dialog with fit/original-size controls. Source notes and assumptions remain available in a separate expandable block, not ahead of every question.

`pdf-card-sources.json` records the verified Drive solution IDs. `pdf-card-manifest.json` records source/HTML/image SHA-256 hashes, all ordered question labels, language coverage, PDF coordinates, fixed-origin raster crop boxes and source-block coverage. Conversion fails on missing question boundaries or unaccounted content blocks. Checksums prove identity and retained content, **not correctness of the supplied educational answers**.

For reproducible conversion/auditing:

```sh
python3 -m venv .venv
.venv/bin/pip install -r tools/paper-card-requirements.txt
.venv/bin/python tools/prepare_pdf_paper_cards.py
python3 tools/test_paper_card_files.py
.venv/bin/python tools/verify_pdf_card_rendering.py
```

### Electrical Engineering Summer 2026

Twelve verified ZIP bundles supplied actual HTML, so these were **not re-created from PDFs**. The subject codes are DI01000081, DI01009011, DI02000161, DI02000171, DI03000081, DI03000091, DI03000101, DI03009011, DI03009021, DI04000171, DI04000321 and DI04009011. Their matching originals remain separate PDFs. All 15 supplied HTML files are unmodified in `originals/`; bundled font licences are retained. `electrical-paper-provenance.json` records Drive bundle/extracted-file identities and checksums.

`tools/prepare_electrical_papers.js` combines the separate English/Gujarati files for the first two subjects, preserves all supplied worked text, makes inherited OR labels explicit, and rasterizes complete source SVGs to scoped PNGs. `electrical-card-manifest.json` audits **336 bilingual cards and 271 distinct PNG diagrams**, including source SVG and image hashes. Two known Digital Electronics (DI02000161) issues have explicit bilingual review/correction notices at Q1(c) OR and Q2(c) OR; the supplied original answer is retained underneath, not silently edited. This is not a full independent answer audit.

Install `jsdom@26.1.0` and `@resvg/resvg-js@2.6.2`, then run `node tools/prepare_electrical_papers.js`. On a reviewed regeneration only, `--update-reader-copies` permits replacing a local generated reader whose hash still matches its prior manifest; it does not authorize overwriting published public files.

### Mechanical and the second Chemical location

Existing Mechanical Summer 2026 HTML cards and the four 2025 readers remain unchanged. The two combined 2025 Drive sources still match their verified checksums. Summer 2026 Drive PDFs are exports of existing card solutions, not grounds for replacing confirmed, distinct exams.

The second Chemical shortcut points to an older **2017 Batch** archive with diploma/degree material, legacy-scheme references, handwritten scans and mixed-session documents. Its six diploma semesters and named solution folders were inspected separately. Unidentified scans and combined sessions have **not** been uploaded as current solved papers; for example 3360501 is Fertilizer, not 4360501 Chemical Reaction Engineering. Scope and unresolved source identities are recorded in `drive-card-refresh-audit.json`. Do not silently merge these schemes or label an OCR-free scan as a verified solution.

### Publishing and deployment

The publisher validates every staged file before copying, refuses symlinks/unsafe paths and differing existing public files, requires matching original PDFs (except the four documented 2025 exceptions), and permits only referenced PNG/WebP assets in the current paper's own `<session>.assets/` directory. Common papers must explicitly declare their 38-item layout. Website CSP trusts only the public paper image path and forbids PDF frames. No scheduled background job was added.

Reader, source-preservation, manifest, source-pixel and optional real-Chromium desktop/mobile tests are in `website/test_card_refresh.js`, `tools/test_electrical_papers.js`, `tools/test_paper_card_files.py`, `tools/verify_pdf_card_rendering.py` and `tools/test_paper_cards_browser.js`. Publish the content **and redeploy the rebuilt `DiplomaOne-Netlify.zip`** to update a manually deployed custom domain; a successful GitHub Pages content upload alone does not update an older Netlify frontend.
