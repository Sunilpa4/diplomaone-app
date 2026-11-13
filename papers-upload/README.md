# Seven Summer 2026 solved-paper sets

These files came from the owner's `papers-manual-upload.zip` in Google Drive. The original GTU question PDFs are unchanged. The supplied solution HTML is retained, except that the primary Q1(c) in DI04000241 and DI04000251 was incorrectly labelled “OR”; the English and Gujarati labels were corrected against the original PDFs (including the Gujarati alternative marker in DI04000251). No other answer changes were made.

Each file pair is published under the same `papers/<subject-code>/summer-2026` path by `.github/workflows/publish-solved-papers.yml`. The publisher validates the supplied bilingual HTML, pairs it with its PDF, and refuses to overwrite a different existing public file. It runs on relevant pushes to main, not on a schedule. The seven-digit codes `4351902` and `4351903` are legacy GTU codes; they are separate from DI codes and are not silently mapped to new-scheme subjects.

Checks confirmed PDF subject codes and the first questions match the respective solution files, and that every solution has 28 question sections in each language. This is not an independent verification of every answer or diagram; educational content should be reviewed against the original question papers.

## Computer Engineering Summer 2026 papers

Ten sets from the owner's `Computer Engineering Paper Solutions` Drive folder cover DI01000131, DI01000151, DI02000101, DI03000011, DI03000021, DI03000031, DI03000041, DI03000051, DI04000011 and DI04000021. The supplied HTML originals are retained under `originals/<code>/`; all ten original PDFs are unchanged and the 21 individual HTML/PDF files matched the corresponding Drive checksums. All PDF subject codes were checked in extracted text. These structural and identity checks do not independently verify every solution, formula or diagram.

Basics of Electronics (DI01000151) was supplied as separate English and Gujarati files. The reader copy combines the matching question parts so the website language toggle chooses the respective original text. The other nine solutions were supplied only in English: both website language settings show the English answer and an explicit English-only notice rather than presenting it as a Gujarati translation. The publisher requires either the existing bilingual structure or an explicitly marked English-only document with 28 question parts.

The existing deployed reader cannot preserve every SVG feature in these papers, so the reader copies contain inert PNG renderings of the original diagrams. Text and code examples remain selectable. The original vector diagrams and original full HTML are preserved in `originals/`. The reader compatibility test compares every answer's text with its original and checks all 28 parts and diagrams in each website language mode. To regenerate these ten reader copies, install `jsdom@26` and `@resvg/resvg-js` in a local Node environment and run `node tools/prepare_computer_papers.js`; the original HTML files are the input. Raster output may vary with fonts or library versions, so review changes before publishing. The publisher refuses to overwrite any differing existing public file.

## Chemical Engineering Semester 1 papers

Four new sets are built with the repository's own generators rather than supplied as finished HTML:

- `papers/DI01005011/winter-2025` — Plant Utilities, Winter 2025 (exam 29-01-2026), 28 answer parts.
- `papers/DI01005011/summer-2026` — Plant Utilities, Summer 2026 (exam 04-07-2026), 28 answer parts.
- `papers/DI01005021/summer-2026` — Material Science and Technology, Summer 2026 (exam 07-07-2026), 28 answer parts.
- `papers/DI01005021/winter-2025` — Material Science and Technology, Winter 2025 (exam 31-01-2026), 28 answer parts.

Each is fully bilingual: the printed English question is repeated in both language modes and only the answer body is translated. The answer modules live in `tools/papers/` (`paperkit.py` for the markup, `svgdiag.py` plus `chemfigs.py`, `utilfigs.py`, `matfigs.py` and `matfigs2.py` for the diagrams) and are rebuilt with `python3 tools/papers/make_<CODE>_<session>.py`. Every diagram is drawn as inline SVG with wrapped labels, so it stays inside the 360 px canvas and survives the reader's SVG whitelist.
