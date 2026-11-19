# Mechanical solved-paper recheck

## What was missed

The prior refresh checked the named Mechanical Drive folder (two combined Semester 1 files) and the older seven-paper batch. A wider Drive search found **four newer Semester 3 combined HTML files at the Drive root**. Those contain genuinely updated Summer 2026 worked answers and previously unpublished Winter 2025 answers. Treating all Mechanical Summer files as exports of the old readers was incorrect.

No Drive file was moved, rewritten or deleted. The exact source identities and recovered byte checksums are in `mechanical-refresh-sources.json`. The previous public Summer readers are preserved in `originals/` and the replacement manifest pins both old and new hashes.

## Semester 3 result

| Subject | Code | Winter 2025 | Summer 2026 |
| --- | --- | --- | --- |
| Theory of Machines and Mechanisms | DI03000141 | No solution found in supplied locations | Existing supplied reader preserved byte-for-byte |
| Measurements and Metrology | DI03000151 | No solution found in supplied locations | Existing supplied reader preserved byte-for-byte |
| Manufacturing Engineering-I | DI03000161 | Added from combined Drive HTML | Replaced with newly supplied worked answers |
| Fluid Mechanics and Hydraulic Machinery | DI03000171 | Added from combined Drive HTML | Replaced with newly supplied worked answers |
| Basics of Applied Mechanics | DI03000201 | Added from combined Drive HTML | Replaced with newly supplied worked answers |
| Engineering Thermodynamics | DI03019011 | Added from combined Drive HTML | Replaced with newly supplied worked answers |

This yields **six subjects / ten supplied exam sessions** in Mechanical Semester 3. Existing Semester 1, Semester 4, legacy Semester 5 and Semester 1 Summer/Winter 2025 answers remain unchanged. Newer DI-code and legacy 435-code exams are not silently conflated.

The four updated combined sources are **English-only**, as supplied. Both site language modes show an explicit English-only notice, not an invented Gujarati translation. Four separate Winter original PDFs were not found; the readers disclose this and never link a Summer question PDF as the Winter original. The six Summer originals retain their prior published bytes, with unambiguous per-exam PDF names.

## Card/choice preservation

- Eight prepared readers contain **224 unique question parts**, preserving **all 228 supplied source-card occurrences**, with **109 distinct scoped PNG diagrams**.
- Manufacturing-I and Fluid Mechanics Summer repeat identical common Q1(a) and Q1(b) cards in both Q1(c) branches. The originals print OR only for Q1(c). The importer verifies both copies' text/images are identical, displays the common work once, audits both source IDs and explicitly explains this choice structure. It does not drop a distinct answer or claim the exam has 30 different parts.
- Every supplied worked answer is compared against its source in both site language modes, including equations, tables, marks, assumptions and diagram identities. All source SVGs are preserved in the original HTML and rendered completely to inert PNGs for the site.
- Answers remain unofficial owner-supplied study material, not independently certified GTU marking schemes.

## Listing changes

The solved-paper page now has branch, semester and search filters, with **all available sessions grouped beneath each subject**. The catalog determines placement, not a loose Drive file's parent folder or an inferred name. Single-session subjects explicitly state that only one session is currently uploaded; this notice disappears automatically when more sessions are discovered. Unregistered papers remain available in the all-paper list rather than disappearing.

Direct views: `#/papers/mechanical` and `#/papers/mechanical/3`. Branch and semester pages link to the same filtered view; existing subject/unit note links are preserved.

## Validation completed

- **18 publisher unit tests**: default overwrite refusal, exact opt-in old/new SHA-256 authorization, invalid/stale metadata and paths, protection of original PDFs/images, symlink refusal, preflight-before-write and idempotence.
- Public-tree-based end-to-end simulation: **3,575 existing staged files unchanged; 119 additions; exactly four reviewed HTML replacements; 3,698 staged files verified**. A publication attempt without the review manifest aborts before any write. With the manifest, only the expected paths change; rerunning changes nothing. Unrelated notes and existing generic original PDF paths are preserved.
- All four Drive source MD5s/lengths match. The HTML download transport injected a 190-byte Rocket Loader script/type attribute; removal of only those transport additions recovered bytes matching the exact Drive hashes. No reconstructed source is accepted on approximate matching.
- All six Summer original PDFs verified for subject code, Summer 2026 session, date, Semester III and Q1 OR structure.
- `tools/test_mechanical_refresh.js`: all 228 source occurrences and all diagram identities survive the deployed sanitizer in EN/Gujarati UI modes.
- `website/test_mechanical_listing.js`: all six subjects, ten real sessions, missing-Winter honesty, subject grouping/filtering, note links, older-scheme Semester 5 placement and correct exam-specific PDF links.
- **60 real-Chromium paper/language/viewport checks plus two listing/filter checks passed** (1365×960 and 390×844). This includes all ten Mechanical Semester 3 readers in both UI languages. Checked decoded images, expansion, image-dialog enlargement/scrolling/keyboard focus, production CSP, no PDF frames and no horizontal page overflow. Other branches and Common papers were included as regressions.
- Existing reader/discovery/seven-paper/Computer/Mechanical 2025/Electrical/Common/Civil-Chemical tests pass. All 49 earlier refreshed papers retain their supplied text/images; all **3,129 prior PDF excerpts** again match their original pixels.
- **32 relevant Python tests passed**, plus the JavaScript suites and real-browser checks. The unrelated broad repository content-suite failures documented in `CARD-REFRESH-VALIDATION.md` are outside this change; the content/exporter code was not changed and that broad suite is not claimed green.
- Rebuilt root `DiplomaOne-Netlify.zip`, checked file-by-file for freshness, including both new Mechanical regression suites against the packaged JavaScript.

## Publication boundary

This document records prepared artifacts and tests, not a deployment claim. The GitHub workflows publish reviewed paper changes and the updated Pages reader after merge. An older manually deployed Netlify frontend must separately receive the rebuilt ZIP to use the new grouping/filter controls. No scheduled Drive scan or background polling was added.
