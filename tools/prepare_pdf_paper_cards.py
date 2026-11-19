#!/usr/bin/env python3
"""Make real question cards from the 37 checksum-reviewed Drive solution PDFs.

Requires PyMuPDF==1.26.7 and Pillow==12.0.0. No OCR, generated answers or PDF
iframes: English prose reflows as HTML; equations/tables/figures and Gujarati
(which has broken PDF Unicode mappings) retain their original rendered pixels.
This importer is intentionally limited to the reviewed layout and fails closed
on changed inputs, missing language boundaries or unexpected question labels.
"""
from collections import OrderedDict
from hashlib import md5, sha256
from html import escape
from io import BytesIO
from pathlib import Path
import argparse
import json
import math
import re

import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
UPLOAD = ROOT / 'papers-upload'
PAPERS = UPLOAD / 'papers'
QUESTION = re.compile(r'^Q\.\s*([1-5])\s*\((\d+|[abcABC])\)(?:\s+([123]))?')
GROUP = re.compile(r'^Q([1-5])(?:\s*\(([AB])\))?\s*·')
MARKER = '<meta name="paper-layout" content="source-pdf-cards-v1">'
SCALE = 2.0


def block_text(block):
    return ' '.join(''.join(s['text'] for s in line['spans']) for line in block.get('lines', []))


def expected_labels(common=False):
    if common:
        return ([f'Q.1 ({i})' for i in range(1, 15)] +
                [f'Q.{q} ({part}) {i}' for q in range(2, 6) for part in 'AB' for i in range(1, 4)])
    return [f'Q.{q} ({part})' + (' OR' if alternative else '')
            for q in range(1, 6)
            for alternative, part in ([(False, 'a'), (False, 'b'), (False, 'c'), (True, 'c')]
                                       if q == 1 else
                                      [(False, 'a'), (False, 'b'), (False, 'c'),
                                       (True, 'a'), (True, 'b'), (True, 'c')])]


def label_for(text, common=False):
    match = QUESTION.match(text)
    if not match:
        raise ValueError('Not a question heading: ' + text)
    q, part, choice = match.groups()
    label = f'Q.{q} ({part})' + (f' {choice}' if choice else '')
    if not common and re.search(r'·\s*OR\s*·', text):
        label += ' OR'
    return label


def native_block(block):
    """Keep sub/superscripts, rather than flattening log bases or powers."""
    lines = []
    for line in block['lines']:
        spans = line['spans']
        size = max(s['size'] for s in spans)
        baseline = max(s['origin'][1] for s in spans if s['size'] >= size * .95)
        content = []
        for span in spans:
            text = escape(span['text'])
            delta = span['origin'][1] - baseline
            if span['flags'] & 1 or (span['size'] < size * .94 and delta < -.8):
                text = '<sup>' + text + '</sup>'
            elif span['size'] < size * .94 and delta > .8:
                text = '<sub>' + text + '</sub>'
            content.append(text)
        lines.append(''.join(content))
    return ' '.join(lines)


class Paper:
    def __init__(self, path, key, output):
        self.path, self.key, self.output = path, key, output
        self.code, self.session = key.split('/')
        self.common = self.code in ('DI01000021', 'DI01000121')
        self.english_only = self.code == 'DI01000021'
        self.doc = fitz.open(path)
        self.pages = []
        self.questions, self.groups, self.en_labels, self.gu_labels = [], [], [], []
        self.assets, self.covered, self.native = [], set(), set()
        self.raster_cache = OrderedDict()
        self.asset_dir = output / self.code / (self.session + '.assets')
        for pn, page in enumerate(self.doc):
            items = []
            for i, b in enumerate(page.get_text('dict')['blocks']):
                b['id'], b['page'], b['text'] = f'{pn + 1}:{i}', pn, block_text(b)
                b['rect'] = fitz.Rect(b['bbox'])
                # Never import the printed page-number footer.
                if b['text'].startswith('DiplomaOne study material') and b['rect'].y0 > 800:
                    continue
                if b['rect'].y1 > 802:
                    raise ValueError(f'Unexpected content below page body: {key} {pn + 1}')
                items.append(b)
                pos = (pn, b['rect'].y0)
                if QUESTION.match(b['text']):
                    self.questions.append((pos, b))
                if GROUP.match(b['text']):
                    self.groups.append((pos, b))
                if b['text'] == 'English answer':
                    self.en_labels.append((pos, b))
                if b['type'] == 0 and b['text'].endswith('જવાબ') and max(
                        s['size'] for l in b['lines'] for s in l['spans']) < 9.1:
                    self.gu_labels.append((pos, b))
            self.pages.append(items)
        # Inline question fractions can begin above the heading's text box.
        # Include their full extent in this question, never the preceding answer.
        self.questions = [((pos[0], min([pos[1]] + [x['rect'].y0 for x in self.pages[pos[0]]
                           if x['type'] == 1 and x['rect'].y0 < b['rect'].y1 and x['rect'].y1 > b['rect'].y0])), b)
                          for pos, b in self.questions]
        self.questions.sort(key=lambda v: v[0])
        if len(self.questions) != (38 if self.common else 28):
            raise ValueError(f'Unexpected question count: {key}: {len(self.questions)}')
        if not self.english_only and (len(self.en_labels) != len(self.questions) or
                                      len(self.gu_labels) != len(self.questions)):
            raise ValueError(f'Unexpected answer-language boundaries: {key}')

    def selected(self, start, end):
        for pn in range(start[0], min(end[0] + 1, len(self.pages))):
            lo = start[1] if pn == start[0] else 0
            hi = end[1] if pn == end[0] else 802
            items = [b for b in self.pages[pn] if b['rect'].y0 >= lo - .1 and b['rect'].y1 <= hi + .1]
            if items:
                yield pn, items

    def image(self, pn, rect, items, language, label):
        # Constant source column width: mathematical snippets keep their scale
        # instead of stretching a narrow fraction to fill the reader.
        rect = fitz.Rect(51, max(39, rect.y0 - 2), 544, min(801, rect.y1 + 2))
        # Render the whole page at a fixed origin, then crop those pixels.
        # Rendering with a fractional PDF clip can subtly change antialiasing
        # along its edge depending on MuPDF's display-list/font cache state.
        if pn not in self.raster_cache:
            pix = self.doc[pn].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), alpha=False)
            self.raster_cache[pn] = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        page_image = self.raster_cache[pn]
        self.raster_cache.move_to_end(pn)
        while len(self.raster_cache) > 2:
            self.raster_cache.popitem(last=False)
        box = [math.floor(rect.x0*SCALE), math.floor(rect.y0*SCALE),
               math.ceil(rect.x1*SCALE), math.ceil(rect.y1*SCALE)]
        image = page_image.crop(box)
        buffer = BytesIO()
        # Lossless is both smaller for these printed pages and keeps every
        # fraction bar/Gujarati glyph exactly as rendered from the source.
        image.save(buffer, format='WEBP', lossless=True, method=6)
        data = buffer.getvalue()
        name = f'{len(self.assets) + 1:04d}.webp'
        self.asset_dir.mkdir(parents=True, exist_ok=True)
        (self.asset_dir / name).write_bytes(data)
        text = ' '.join(b['text'] for b in sorted(items, key=lambda b: (b['rect'].y0, b['rect'].x0)) if b['type'] == 0)
        self.covered.update(b['id'] for b in items)
        self.assets.append({'path': f'{self.code}/{self.session}.assets/{name}',
                            'sha256': sha256(data).hexdigest(), 'page': pn + 1,
                            'clip': list(rect), 'raster_box': box,
                            'width': image.width, 'height': image.height,
                            'blocks': [b['id'] for b in items], 'language': language})
        if language == 'gu':
            alt = f'{label}: મૂળ ગુજરાતી જવાબ, પાનું {pn + 1}. મોટું કરીને વાંચો.'
            caption = f'મૂળ ગુજરાતી જવાબ · પાનું {pn + 1}'
        else:
            alt = f'{label}: preserved source formula, table or diagram, page {pn + 1}.'
            if text:
                alt += ' Extracted text context (formula notation may be incomplete): ' + text
            caption = ''
        return (f'<figure class="paper-excerpt"><img src="{self.session}.assets/{name}" '
                f'alt="{escape(alt, quote=True)}" loading="lazy" width="{image.width}" height="{image.height}">'
                + (f'<figcaption>{caption}</figcaption>' if caption else '') + '</figure>')

    def render(self, start, end, language, label):
        result = []
        for pn, items in self.selected(start, end):
            if language == 'gu':
                rect = fitz.Rect(items[0]['rect'])
                for item in items[1:]:
                    rect |= item['rect']
                result.append(self.image(pn, rect, items, language, label))
                continue
            # Merge only vertically overlapping blocks. Inline fraction images
            # and their adjoining text must be rendered together, not dropped.
            regions = [dict(rect=fitz.Rect(b['rect']), items=[b], raster=b['type'] == 1) for b in items]
            # PDF table cells have lost their HTML row/column semantics. Keep
            # each source table intact rather than flattening its cell order.
            lo, hi = min(b['rect'].y0 for b in items), max(b['rect'].y1 for b in items)
            for table in self.doc[pn].find_tables().tables:
                rect = fitz.Rect(table.bbox)
                if table.row_count >= 2 and table.col_count >= 2 and rect.y0 >= lo - 4 and rect.y1 <= hi + 4:
                    regions.append(dict(rect=rect, items=[], raster=True))
            regions.sort(key=lambda r: r['rect'].y0)
            merged = []
            for region in regions:
                if merged and region['rect'].y0 < merged[-1]['rect'].y1 - .3:
                    previous = merged[-1]
                    previous['rect'] |= region['rect']
                    previous['items'].extend(region['items'])
                    previous['raster'] |= region['raster']
                else:
                    merged.append(region)
            for region in merged:
                if region['raster']:
                    result.append(self.image(pn, region['rect'], region['items'], language, label))
                else:
                    for block in sorted(region['items'], key=lambda b: (b['rect'].y0, b['rect'].x0)):
                        if re.search(r'[\u0a80-\u0aff\x80-\x9f]', block['text']):
                            raise ValueError(f'Gujarati/invalid glyph in English interval: {self.key} {pn + 1} {block["text"][:100]}')
                        self.covered.add(block['id'])
                        self.native.add(block['id'])
                        result.append('<p>' + native_block(block) + '</p>')
        return '\n'.join(result)

    def build(self):
        end = (len(self.pages), 0)
        boundaries = sorted([pos for pos, _ in self.questions + self.groups] + [end])
        cards, labels = [], []
        actual_sections = set()
        for number, (start, heading) in enumerate(self.questions):
            stop = next(pos for pos in boundaries if pos > start)
            if self.english_only:
                # All question-heading spans share the blue heading colour.
                heads = [b for pn, items in self.selected(start, stop) for b in items
                         if b['type'] == 0 and all(s['color'] == 1527667 for l in b['lines'] for s in l['spans'])]
                head_end = max((b['page'], b['rect'].y1) for b in heads)
                # Include inline question fractions that extend beyond text.
                for pn, items in self.selected(start, stop):
                    if pn == head_end[0]:
                        for b in items:
                            if b['type'] == 1 and b['rect'].y0 < head_end[1] and b['rect'].y1 > head_end[1]:
                                head_end = (pn, b['rect'].y1)
                en_start, en_end, gu_start = head_end, stop, None
            else:
                en_pos, en_label = next((p, b) for p, b in self.en_labels if start < p < stop)
                gu_pos, gu_label = next((p, b) for p, b in self.gu_labels if en_pos < p < stop)
                head_end = en_pos
                en_start, en_end = (en_label['page'], en_label['rect'].y1), gu_pos
                gu_start = (gu_label['page'], gu_label['rect'].y1)
            # Recover complete multi-block headings, including their OR marker.
            heading_items = [b for pn, items in self.selected(start, head_end) for b in items if b['type'] == 0]
            title_text = heading['text'] + ' ' + ' '.join(b['text'] for b in heading_items if b['id'] != heading['id'])
            raw_label = label_for(title_text, self.common)
            label = expected_labels(self.common)[number]
            if raw_label.removesuffix(' OR') != label.removesuffix(' OR') or (raw_label.endswith(' OR') and not label.endswith(' OR')):
                raise ValueError(f'Unexpected question order: {self.key}: {raw_label}, expected {label}')
            # Some supplied papers print OR only on (a), applying to the whole
            # repeated (a,b,c) block. Carry that explicit alternative forward.
            inherited_or = label.endswith(' OR') and not raw_label.endswith(' OR')
            if inherited_or and (not labels or not labels[-1].endswith(' OR')):
                raise ValueError(f'Missing source OR marker: {self.key}: {label}')
            labels.append(label)
            q = int(QUESTION.match(title_text).group(1))
            if q not in actual_sections:
                if actual_sections:
                    cards.append('</section>')
                cards.append(f'<section><h2>Question {q}</h2>')
                actual_sections.add(q)
            nearby_groups = [(pos, b) for pos, b in self.groups if (number == 0 or self.questions[number - 1][0] < pos) and pos < start]
            for _, group in nearby_groups:
                cards.append('<h3>' + escape(group['text']) + '</h3>')
            summary = self.render(start, head_end, 'en', label)
            # p/figure are not phrasing content, so a question with a source
            # fraction gets a plain, useful summary plus its full wording in
            # the answer, instead of invalid block markup in <summary>.
            contains_image = '<figure' in summary
            if contains_image:
                # A useful question preview, never pretend extracted fraction
                # text is a complete mathematical question. Its authentic
                # wording/notation is shown inside the expanded answer.
                title_plain = title_text.split('·', 1)[-1].strip()
                title_plain = re.sub(r'^(?:OR\s*·\s*)?', '', title_plain)
                summary_html = (f'<span>{escape(label)}</span><strong>{escape(title_plain)}'
                                '<small class="paper-question-hint"> · Open for the original formula and worked answer</small></strong>')
            else:
                summary_html = '<strong>' + summary.replace('<p>', '').replace('</p>', ' ') + '</strong>'
            if inherited_or:
                summary_html = '<span>OR</span>' + summary_html
            en = self.render(en_start, en_end, 'en', label)
            if not en.strip():
                raise ValueError(f'Empty English answer: {self.key} {label}')
            if contains_image:
                en = '<h3>Question</h3>' + summary + '<h3>Worked solution</h3>' + en
            if self.english_only:
                answer = en
            else:
                gu = self.render(gu_start, stop, 'gu', label)
                if not gu.strip():
                    raise ValueError(f'Empty Gujarati answer: {self.key} {label}')
                # Keep the authentic question visible in both language modes.
                if contains_image:
                    gu = '<h3>મૂળ પ્રશ્ન</h3>' + summary + '<h3>જવાબ</h3>' + gu
                answer = f'<div class="en">{en}</div><div class="gu">{gu}</div>'
            cards.append(f'<details class="card" data-question="{escape(label)}"><summary>{summary_html}</summary>'
                         f'<div class="answer">{answer}</div></details>')
        cards.append('</section>')
        if labels != expected_labels(self.common):
            raise ValueError(f'Question/OR order mismatch: {self.key}: {labels}')
        intro_end = min(pos for pos, _ in self.groups + self.questions)
        intro = []
        for pn, items in self.selected((0, 0), intro_end):
            for b in items:
                if b['type'] == 0 and b['rect'].x0 >= 60 and not re.search(r'[\u0a80-\u0aff\x80-\x9f]', b['text']):
                    self.covered.add(b['id'])
                    self.native.add(b['id'])
                    intro.append('<p>' + native_block(b) + '</p>')
        notice = ('<p class="note' + ('' if self.english_only else ' en') + '">'
                  'Unofficial study solution; not an official GTU answer key. Answers have not been independently verified. '
                  'English text reflows; source equations, diagrams and Gujarati retain their original appearance. '
                  'Use Enlarge image to inspect them.</p>')
        if self.english_only:
            notice += '<p class="note">This supplied solution is English only; switching the site language does not translate its answers.</p>'
        else:
            notice += ('<p class="note gu">આ બિનસત્તાવાર અભ્યાસ ઉકેલ છે, સત્તાવાર GTU જવાબવહી નથી. '
                       'PDF માંથી ગુજરાતી લખાણ સાચું નીકળતું નથી, તેથી દરેક જવાબ મૂળ ચિત્રરૂપે જાળવ્યો છે. '
                       'વાંચવા માટે ચિત્ર મોટું કરો. મૂળ પ્રશ્ન અને પરીક્ષાના વિકલ્પોની સૂચનાઓ અનુસરો.</p>')
        original_intro = '' if self.english_only else '<div class="gu">' + self.render((0, 0), intro_end, 'gu', 'Source introduction') + '</div>'
        html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">' + MARKER +
                f'<meta name="paper-question-count" content="{len(labels)}">' +
                ('<meta name="paper-language" content="en-only">' if self.english_only else '') +
                f'<title>{escape(self.key)} · Solved question cards</title></head><body><main>' + notice +
                '<div class="paper-source-notes"><div' + ('' if self.english_only else ' class="en"') + '>' + ''.join(intro) + '</div>' +
                original_intro + '</div>' + '\n'.join(cards) + '</main></body></html>\n')
        html = re.sub(r'[ \t]+\n', '\n', html)
        destination = self.output / (self.key + '.html')
        if destination.exists() and MARKER not in destination.read_text():
            raise ValueError('Refusing to replace an unrelated HTML solution: ' + str(destination))
        # Each content block between first question and EOF must appear as
        # native prose or in a source crop; only headings/language labels are
        # deliberately handled separately.
        structural = {b['id'] for _, b in self.groups + self.en_labels + self.gu_labels}
        omitted = [b['id'] for pn, items in self.selected(self.questions[0][0], end) for b in items
                   if b['id'] not in self.covered and b['id'] not in structural
                   and not (b['type'] == 0 and max(s['size'] for l in b['lines'] for s in l['spans']) >= 14)]
        if omitted:
            raise ValueError(f'Uncovered source blocks: {self.key}: {omitted}')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding='utf-8')
        self.doc.close()
        return {'paper': self.key, 'source_sha256': sha256(self.path.read_bytes()).hexdigest(),
                'html_sha256': sha256(html.encode()).hexdigest(), 'questions': labels,
                'languages': ['en'] if self.english_only else ['en', 'gu'],
                'native_blocks': len(self.native),
                'source_blocks_covered': len(self.covered), 'uncovered_blocks': omitted,
                'assets': self.assets}


def build(keys=None, output=PAPERS, manifest=UPLOAD / 'pdf-card-manifest.json'):
    sources = json.loads((UPLOAD / 'pdf-card-sources.json').read_text())['sources']
    provenance = {e['path']: e for name in ('pdf-batch-provenance.json', 'common-subject-pdf-provenance.json')
                  for e in json.loads((UPLOAD / name).read_text())}
    if set(sources) != {str(p.relative_to(PAPERS)).removesuffix('.solution.pdf') for p in PAPERS.glob('*/*.solution.pdf')}:
        raise ValueError('Drive source audit and solution PDF inventory differ')
    if keys and set(keys) != set(sources) and manifest == UPLOAD / 'pdf-card-manifest.json':
        raise ValueError('Subset reviews need a separate --manifest path; never truncate the complete audit')
    result = []
    for key in sorted(keys or sources):
        source = PAPERS / (key + '.solution.pdf')
        data = source.read_bytes()
        entry = provenance['papers/' + key + '.solution.pdf']
        if md5(data).hexdigest() != entry['drive_md5'] or sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Input differs from the reviewed Drive PDF: ' + key)
        record = Paper(source, key, output).build()
        record['drive_id'] = sources[key]
        record['drive_md5'] = entry['drive_md5']
        result.append(record)
        print(key, len(record['questions']), 'cards;', len(record['assets']), 'source excerpts;', flush=True)
    if manifest:
        manifest.write_text(json.dumps({'format': 'source-pdf-cards-v1', 'papers': result}, indent=2) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('keys', nargs='*', help='Subset for local review; omit to build all 37 sets')
    parser.add_argument('--output', type=Path, default=PAPERS)
    parser.add_argument('--manifest', type=Path, default=UPLOAD / 'pdf-card-manifest.json')
    args = parser.parse_args()
    build(args.keys, args.output, args.manifest)
