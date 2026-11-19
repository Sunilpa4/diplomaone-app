# Question-card refresh — validation record

Reviewed 2026-10-30. This is an artifact/source-preservation record, not a claim that a manually deployed custom domain has been updated or that every educational answer is correct.

## Scope

| Supplied location | Reader result |
| --- | --- |
| Current Chemical | 23 PDF-only exams → individual question cards |
| Civil | 10 PDF-only exams → individual question cards |
| Mathematics-I | 2 exams, 38 cards each; English-only as supplied |
| Applied Physics | 2 exams, 38 bilingual cards each |
| Electrical | 12 Summer 2026 HTML sets reused; 336 bilingual cards |
| Mechanical | Existing 7 Summer 2026 + 4 2025 readers preserved, not overwritten |
| Second Chemical / 2017 Batch archive | Separately inventoried; unresolved legacy scans **not yet uploaded** |

The refresh adds **49 readers / 1,412 question parts / 3,400 scoped images**. The 37 PDF-derived readers account for 1,076 parts and 3,129 lossless WebP excerpts. Electrical accounts for 336 parts and 271 PNG diagrams. Source exam code/session, OR order, Maths/Physics 38-item layouts and unchanged source identities are recorded in the two card manifests and three provenance files. Archive exclusions and exact Drive identities are in `drive-card-refresh-audit.json`.

## Successful checks

- `tools/test_paper_card_files.py`: source/HTML/image checksums, 49 subject/session identities, ordered question labels, language declarations, source-block coverage, no orphan images, and mathematical truth-table checks for the two explicitly labelled Digital Electronics errata.
- `tools/verify_pdf_card_rendering.py`: **all 3,129 excerpts match fixed-origin original PDF rendering pixel for pixel**, using the pinned PyMuPDF/Pillow versions. A draft fractional-clip rendering discrepancy was corrected before this final verification.
- `website/test_card_refresh.js`: all 49 readers preserve every supplied visible text node, question count, collapsed question/answer structure and image in **both** website language modes. HTML beats matching PDF discovery, without duplicate exams.
- `tools/test_electrical_papers.js`: all 336 worked answers match the unchanged original HTML, all original summaries are retained, and all source figure counts survive. Only explicit OR/question labels and the two labelled bilingual errata are additional annotations.
- Existing Computer and Mechanical source-preservation tests pass; existing public paper bytes are unchanged.
- Reader/discovery/uploaded-paper/link/security tests and the five website ad-declaration tests pass. Optional PDF links replace PDF frames; scoped images pass the production CSP.
- `tools/test_netlify_package.py` passes, including the real 49-reader test against packaged JavaScript and a file-by-file check that the committed ZIP is fresh.
- Publisher's 13 unit tests pass. Preflight validates all **3,573 staged files** before copying. All 112 previously published staged files match public Git blob hashes exactly; 3,461 files are additive (49 HTML readers, 12 Electrical question PDFs, 3,400 images).
- **20 real Chromium checks**: ten representative paper/language combinations at 1365×960 and 390×844. Civil, current/legacy Chemical, both Common subjects, Electrical (including split-language sources and errata), and existing Mechanical readers were covered. Checked expansion/collapse, decoded images, production CSP, no PDF frames, image-dialog fit/original-size, keyboard dismissal/focus return and no horizontal page overflow. Review screenshots are ignored under `build/card-browser/`, not published.

For a local preview, run `python3 tools/preview_paper_cards.py` (binds 0.0.0.0:4173). For the optional browser audit, install `playwright@1.56.1`, `@sparticuz/chromium@153.0.0` and `jsdom@26.1.0`, then run `node tools/test_paper_cards_browser.js` while that preview runs. A system Chromium can be provided with `CHROMIUM_EXECUTABLE_PATH`. The test intercepts the **production trusted URLs**, supplies CORS headers and uses the production CSP; it does not disable web security. No external page request is needed.

## Repository-wide limits, not hidden successes

The broad `python3 -m unittest discover -s tools -p 'test_*.py'` run executed 817 tests: 802 passed, two failed and 13 modules could not load in the system-Python environment. The two failures were reproduced unchanged on an isolated archive of base commit `f91fd1ec5a907e274aea89a48db377599072c652`:

- `test_DI04000041_u1.CloudUnit1.test_14_export_carries_the_unit`: expects five published Cloud units; exporter currently reports one.
- `test_maths_coverage.MathsCoverage.test_09_exporter_satisfies_the_publisher_contract`: existing Engineering Graphics common-subject metadata is not listed under all 27 branches.

The 13 module-load errors require unrelated Pillow/resvg_py/Redis or a preconfigured PHP/MySQL runtime (`/tmp/phproot/usr/bin/php8.4`). Neither those source modules nor note content/exporter code was changed in this refresh. The paper-specific, website, package, pixel and browser checks above completed successfully; the full repository suite is **not** reported as green. Flutter remains unavailable locally and is handled by the existing GitHub workflows.

## Deployment boundary

Publishing content to GitHub Pages and updating a Netlify frontend are separate operations. The rebuilt root `DiplomaOne-Netlify.zip` contains the updated question reader/CSP/styles and live-data redirects, not a stale copy of note or paper data. A manual Netlify deployment must still receive this ZIP to update that frontend. Do not infer `www.diplomaone.in` freshness from a content-publisher success alone. No scheduled scan or background publishing loop was added, and no Drive original was modified.
