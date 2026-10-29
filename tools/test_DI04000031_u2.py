"""Thirty real-MongoDB Unit 2 validation groups; no emulator.

Run after the authenticated private server is started and Unit 2 is built.
Includes exact displayed-source execution, exported ZIP runner re-execution,
negative cases, fixtures, deterministic rebuild, SVG/HTML/preview/export checks.
"""
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

import resvg_py
from PIL import Image, ImageDraw, ImageFont

from subject_DI04000031 import ROOT, SUBJ_DIR, DIAG_DIR
from mongodb_content import GUARD, assert_runtime, shell, run_script, private_uri, scratch_databases, CREDENTIALS
from content_DI04000031_u2_shared import STUDENTS, SEED
from content_DI04000031_u2_notes import NOTES, SOURCES
from content_DI04000031_u2_extras import PRACTICE_QS
from diagrams_DI04000031_u2 import TITLES
from export_DI04000031_u2_practicals import OUT as ZIP_PATH
from test_DI04000031_u1 import Fragment, execute_preview

ROOT = Path(ROOT); SUBJ_DIR = Path(SUBJ_DIR); DIAG_DIR = Path(DIAG_DIR)
PREVIEW = ROOT / 'preview/DI04000031_unit2_preview.html'


class Unit2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = json.loads((SUBJ_DIR / 'unit2.json').read_text())
        cls.s = json.loads((SUBJ_DIR / 'subject.json').read_text())
        cls.by_id = {p['id']: p for p in cls.u['programs']}
        # Import executes every current source on real mongod, once, in fresh DBs.
        from content_DI04000031_u2_programs import PROGRAMS
        cls.fresh = {p['id']: p for p in PROGRAMS}

    def output(self, number): return self.by_id[f'ns2p{number:02d}']['out']

    def json_line(self, number, prefix):
        matches = [line[len(prefix):] for line in self.output(number).splitlines() if line.startswith(prefix)]
        self.assertEqual(len(matches), 1, (number, prefix))
        return json.loads(matches[0])

    def test_01_real_authenticated_standalone_runtime(self):
        r = assert_runtime()
        self.assertEqual((r['server'], r['shell']), ('9.0.4', '2.14.0'))
        self.assertTrue(r['authenticated']); self.assertTrue(r['standalone'])
        self.assertEqual(self.u['runtime_evidence']['server_version'], r['server'])
        self.assertEqual(self.u['runtime_evidence']['shell_version'], r['shell'])
        self.assertFalse(self.u['runtime_evidence']['replication_configured'])
        self.assertFalse(self.u['runtime_evidence']['sharding_configured'])
        self.assertFalse(self.u['runtime_evidence']['public_database_endpoint'])

    def test_02_official_scope_structure_and_counts(self):
        u = self.u
        self.assertEqual((u['unit'], u['hours'], u['weightage']), (2, 18, 30))
        self.assertEqual(u['title'], {'en': 'Document Databases: MongoDB'})
        self.assertEqual(sum(len(s['items']) for s in NOTES), 20)
        self.assertEqual(sum(len(s['items']) for s in u['notes']), 38)
        self.assertEqual(len(u['programs']), 14); self.assertEqual(len(u['diagrams']), 13)
        self.assertEqual(sum(len(g['items']) for g in u['syntax']), 16)
        self.assertEqual(sum(len(g['items']) for g in u['viva']), 56)
        self.assertEqual(len(u['notes'][-1]['items']), 18)
        self.assertEqual(u['practical_numbers'], [2, 3])
        self.assertEqual(u['exam_questions'], [])
        self.assertEqual(self.s['exam']['theory_ese'], 0)
        self.assertEqual(self.s['exam']['theory_pa'], 0)
        self.assertEqual(self.s['exam']['total'], 50)
        self.assertEqual([v['file'] for v in self.s['units']], ['unit1.json', 'unit2.json', None, None, None])

    def test_03_exact_current_sources_and_fresh_real_outputs(self):
        self.assertEqual(self.by_id, self.fresh)
        for p in self.by_id.values():
            self.assertTrue(p['code']['en'].startswith(GUARD))
            self.assertTrue(p['out'])
            self.assertNotIn('mock', p['code']['en'].lower())
        self.assertEqual(scratch_databases(), [])

    def test_04_connection_collection_write_read_drop(self):
        self.assertEqual(self.output(1).splitlines(), [
            'Server: 9.0.4', 'Ping: 1', 'Scratch selected: true',
            'Collection exists: true', 'Stored message: MongoDB connected', 'Collection dropped: true'])

    def test_05_bson_types_objectid_and_date(self):
        out = self.output(2)
        for field, kind in [('_id', 'objectId'), ('name', 'string'), ('age', 'int'),
                            ('skills', 'array'), ('address', 'object'), ('active', 'bool'),
                            ('joined', 'date'), ('score', 'double')]:
            self.assertIn(f'{field} / {kind}: 1', out)
        self.assertIn('String ID matches: 0', out); self.assertIn('ObjectId matches: 1', out)
        self.assertIn('2026-01-15T00:00:00.000Z', out)

    def test_06_inserts_and_real_duplicate_key_rejection(self):
        self.assertEqual(self.output(3).splitlines(), ['insertOne acknowledged: true',
            'insertMany count: 2', 'Duplicate ID error: 11000', 'Stored rows: 3'])

    def test_07_all_syllabus_filter_results(self):
        expected = {'gt80: ': [1, 3, 5], 'lt70: ': [4, 6], 'inCities: ': [1, 2, 3, 5],
                    'and: ': [1, 5], 'or: ': [1, 3, 5, 6], 'implicitAnd: ': [1, 3, 5]}
        for prefix, ids in expected.items(): self.assertEqual(self.json_line(4, prefix), ids)
        for op in ('$gt', '$lt', '$in', '$and', '$or'):
            self.assertIn(op, self.by_id['ns2p04']['code']['en'])

    def test_08_stable_sort_limit_projection_and_cursor(self):
        self.assertEqual(self.json_line(5, 'Top three: '), [
            {'name': 'Neha', 'marks': 92}, {'name': 'Asha', 'marks': 82}, {'name': 'Meera', 'marks': 82}])
        self.assertEqual(self.json_line(5, 'Exclusion: '), {'_id': 2, 'name': 'Ravi', 'city': 'Bharuch', 'marks': 70})
        self.assertIn('find returns cursor: true', self.output(5))
        self.assertIsNone(self.json_line(5, 'Missing findOne: '))

    def test_09_array_membership_and_nested_equality(self):
        for prefix, ids in {'MongoDB skill: ': [1, 3], 'Python or Java: ': [1, 2, 3, 4, 5],
                            'Nested pin: ': [1], 'Whole-object match: ': [], 'Two skills: ': [1]}.items():
            self.assertEqual(self.json_line(6, prefix), ids)

    def test_10_update_real_noop_and_missing_counts(self):
        out = self.output(7)
        for line in ('One: 1/1', 'Many: 2/2', 'No-op: 1/0', 'Missing: 0/0'):
            self.assertIn(line, out)
        self.assertEqual(self.json_line(7, 'Ravi: '), {'name': 'Ravi', 'city': 'Surat', 'marks': 75})

    def test_11_upsert_and_replacement_remove_omitted_fields(self):
        for line in ('Created by upsert: 1', 'Second matched: 1', 'Profiles: 1',
                     'ID retained: 7', 'City removed: true', 'Remaining fields: _id,marks,name'):
            self.assertIn(line, self.output(8))

    def test_12_targeted_deletion_and_missing_record(self):
        self.assertEqual(self.output(9).splitlines(), ['Preview inactive: 2', 'deleteOne: 1',
            'deleteMany: 1', 'Missing delete: 0', 'Remaining IDs: [1,2,3,5]'])

    def test_13_embedding_references_and_absence_are_real(self):
        self.assertEqual(self.output(10).splitlines(), ['Embedded city: Surat',
            'Referenced course: MongoDB Basics', 'Missing reference: true', 'Reference inserted: 1'])

    def test_14_forced_index_counters_and_unique_email(self):
        self.assertEqual(self.output(11).splitlines(), ['Scan returned/examined: 3/6',
            'Index returned/examined: 3/3', 'Index keys examined: 3',
            'Indexes: _id_,city_marks', 'Unique email error: 11000', 'Accounts: 1'])
        code = self.by_id['ns2p11']['code']['en']
        self.assertIn('.hint({$natural: 1})', code); self.assertIn('.hint("city_marks")', code)
        self.assertNotIn('executionTimeMillis', code)

    def test_15_aggregation_totals_averages_and_unchanged_source(self):
        lines = self.output(12).splitlines()
        self.assertEqual(json.loads(lines[0]), [
            {'_id': 'book', 'count': 3, 'total': 600, 'average': 200},
            {'_id': 'tool', 'count': 2, 'total': 1000, 'average': 500}])
        self.assertEqual(lines[1], 'Source documents unchanged: 6')

    def test_16_guarded_single_document_stock_update(self):
        out = self.output(13)
        for line in ('Sale 1 matched: 1', 'Sale 2 matched: 1', 'Sale 3 matched: 0',
                     'Final stock: 0', 'Missing delete: 0'):
            self.assertIn(line, out)
        self.assertEqual(self.json_line(13, 'Books: '), [{'name': 'NoSQL Guide', 'pricePaise': 25000}])
        self.assertIn('stock: {$gte: 1}', self.by_id['ns2p13']['code']['en'])

    def test_17_null_missing_and_rejected_query_update_shapes(self):
        self.assertEqual(self.json_line(14, 'Null equality: '), [1, 2])
        self.assertEqual(self.json_line(14, 'Explicit null: '), [1])
        self.assertEqual(self.json_line(14, 'Missing field: '), [2])
        self.assertEqual(self.json_line(14, 'String ID matches: '), [])
        self.assertIn('Mixed projection rejected: 31254', self.output(14))
        self.assertIn('Non-operator update rejected: MongoInvalidArgumentError', self.output(14))
        self.assertIn('Selector-shaped input rejected: true', self.output(14))

    def test_18_prefix_guard_and_unauthed_write_rejection(self):
        with self.assertRaisesRegex(RuntimeError, 'Select an isolated Unit 2 scratch database'):
            shell(GUARD + 'db.guard_should_not_exist.insertOne({_id:1});', database='admin')
        anon = 'mongodb://127.0.0.1:27027/admin?directConnection=true&serverSelectionTimeoutMS=5000'
        out = shell('''try {
  db.unauthorized_probe.insertOne({_id:1});
  throw new Error("Unexpected unauthenticated write");
} catch(e) {
  if(e.code !== 13) throw e;
  print("Unauthorized write code: " + e.code);
}''', uri=anon, database='di04000031_u2_unauth_probe')
        self.assertEqual(out, 'Unauthorized write code: 13')
        self.assertEqual(scratch_databases(), [])

    def test_19_shared_seed_matches_actual_persisted_json(self):
        out = run_script(GUARD + SEED + 'print(JSON.stringify(db.students.find({}).sort({_id:1}).toArray()));', 'seed_check')
        self.assertEqual(json.loads(out), STUDENTS)
        self.assertEqual(len({r['_id'] for r in STUDENTS}), 6)
        self.assertEqual([r['marks'] for r in STUDENTS if r['city'] == 'Surat'], [82, 92, 82])

    def test_20_links_english_safe_html_and_no_unexpanded_snippets(self):
        def en_only(obj):
            if isinstance(obj, dict):
                self.assertNotIn('gu', obj); self.assertNotIn('key', obj)
                for val in obj.values(): en_only(val)
            elif isinstance(obj, list):
                for val in obj: en_only(val)
            elif isinstance(obj, str): self.assertIsNone(re.search(r'[\u0a80-\u0aff]', obj))
        en_only(self.u)
        self.assertEqual(self.s['languages'], ['en'])
        self.assertEqual(self.s['code_lang'], 'nosql')
        for sec in self.u['notes']:
            for item in sec['items']:
                Fragment().finish(item['body']['en']); self.assertNotIn('@@', item['body']['en'])
        for p in self.u['programs']: Fragment().finish(p['expl']['en'])
        for group in self.u['viva']:
            for q in group['items']: Fragment().finish(q['a']['en'])
        self.assertEqual(len(self.u['sources']), len(SOURCES))
        used_p = {p for s in self.u['notes'] for i in s['items'] for p in i.get('programs', [])}
        self.assertEqual(used_p, set(self.by_id))
        for q, card in zip(PRACTICE_QS, self.u['notes'][-1]['items']):
            self.assertEqual((q['q'], q['a']), (card['h'], card['body']))
            self.assertNotIn('marks', q)

    def test_21_svg_integrity_raster_and_contact_sheets(self):
        self.assertEqual({d['id'] for d in self.u['diagrams']}, set(TITLES))
        used = {i['diagram'] for s in self.u['notes'] for i in s['items'] if 'diagram' in i}
        self.assertEqual(used, set(TITLES))
        checks = ROOT / 'preview/nosql_u2_checks'; checks.mkdir(exist_ok=True)
        images = []
        for d in self.u['diagrams']:
            raw = (SUBJ_DIR / d['file']).read_text()
            root = ET.fromstring(raw)
            self.assertEqual(root.attrib['viewBox'].split()[2], '360')
            for bad in ('<marker', '<image', '<foreignObject', '<script', '<style', 'href=', 'url('):
                self.assertNotIn(bad, raw)
            image = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(
                svg_path=str(SUBJ_DIR / d['file']), zoom=1.4,
                font_dirs=['/usr/share/fonts/truetype/dejavu'],
                font_family='DejaVu Sans', sans_serif_family='DejaVu Sans',
                skip_system_fonts=True)))).convert('RGB')
            self.assertGreater(image.height, 400)
            image.save(checks / (d['id'] + '.png')); images.append((d['id'], image))
        for batch, label in [(images[:4], 'a'), (images[4:8], 'b'), (images[8:], 'c')]:
            w, h = 530, 710
            sheet = Image.new('RGB', (w * 2, h * ((len(batch) + 1) // 2)), '#EAE4F1')
            draw = ImageDraw.Draw(sheet)
            for i, (id_, image) in enumerate(batch):
                x = i % 2 * w + 12; y = i // 2 * h + 29
                draw.text((x, y - 22), id_, fill='#4C1C85'); sheet.paste(image, (x, y))
            sheet.save(ROOT / f'preview/DI04000031_unit2_diagrams_{label}.png')

    def test_22_svg_text_viewport_bounds(self):
        for id_ in TITLES:
            root = ET.parse(DIAG_DIR / (id_ + '.svg')).getroot()
            _, _, width, height = map(float, root.attrib['viewBox'].split())
            for node in root.iter('{http://www.w3.org/2000/svg}text'):
                size = float(node.get('font-size', '12'))
                fontname = 'DejaVuSans-Bold.ttf' if node.get('font-weight') == 'bold' else 'DejaVuSans.ttf'
                font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/' + fontname, round(size * 10))
                tw = font.getlength(''.join(node.itertext())) / 10
                x = float(node.get('x')); y = float(node.get('y')); anchor = node.get('text-anchor', 'start')
                left = x - tw / 2 if anchor == 'middle' else x - tw if anchor == 'end' else x
                self.assertGreaterEqual(left, 1, (id_, node.text, left))
                self.assertLessEqual(left + tw, width - 1, (id_, node.text, left + tw))
                self.assertGreater(y - size, -1); self.assertLess(y + size / 3, height + 1)

    def test_23_every_displayed_script_is_valid_javascript(self):
        for p in self.u['programs']:
            r = subprocess.run(['node', '--check'], input=p['code']['en'], text=True, capture_output=True)
            self.assertEqual(r.returncode, 0, (p['id'], r.stderr))
            self.assertLessEqual(max(map(len, p['code']['en'].splitlines())), 78)

    def test_24_zip_exact_sources_outputs_runtime_and_csv(self):
        with zipfile.ZipFile(ZIP_PATH) as z:
            names = set(z.namelist()); self.assertEqual(len(names), 32)
            self.assertTrue({'README.md', 'run_lab.py', 'students.csv', 'runtime.json'} <= names)
            self.assertEqual(json.loads(z.read('runtime.json')), self.u['runtime_evidence'])
            for p in self.u['programs']:
                self.assertEqual(z.read('examples/' + p['id'] + '.js').decode(), p['code']['en'] + '\n')
                self.assertEqual(z.read('expected/' + p['id'] + '.txt').decode(), p['out'] + '\n')
            rows = list(csv.DictReader(io.StringIO(z.read('students.csv').decode())))
            self.assertEqual([r['name'] for r in rows], [r['name'] for r in STUDENTS])
            self.assertEqual([int(r['marks']) for r in rows], [r['marks'] for r in STUDENTS])
            self.assertFalse(any('secret' in name.lower() or 'credential' in name.lower() for name in names))
            self.assertEqual(z.read('run_lab.py'), (ROOT / 'tools/mongodb_lab_runner.py').read_bytes())

    def test_25_exported_public_runner_reexecutes_all_fourteen(self):
        env = os.environ.copy(); env['MONGODB_URI'] = private_uri()
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ZIP_PATH) as z: z.extractall(tmp)
            for p in self.u['programs']:
                r = subprocess.run(['python3', 'run_lab.py', 'examples/' + p['id'] + '.js'],
                    cwd=tmp, env=env, text=True, capture_output=True, timeout=50)
                self.assertEqual(r.returncode, 0, (p['id'], r.stderr))
                self.assertEqual(r.stdout.rstrip('\n'), p['out'], p['id'])
                self.assertEqual(r.stderr, '', p['id'])
        self.assertEqual(scratch_databases(), [])

    def test_26_preview_all_five_views_and_correct_diagram_heading(self):
        content = PREVIEW.read_text()
        self.assertNotRegex(content, r'<(?:script|link|img)[^>]+(?:src|href)=')
        result = execute_preview(PREVIEW)
        self.assertEqual(set(result['views']), {'notes', 'programs', 'diagrams', 'syntax', 'viva'})
        self.assertEqual(result['languageHidden'], 'none')
        self.assertIn('<span>Diagrams</span>', result['views']['diagrams'])
        self.assertNotIn('<span>Flowcharts</span>', result['views']['diagrams'])
        self.assertEqual(result['views']['diagrams'].count('class="dcard"'), 13)
        self.assertEqual(result['neutral'], 'a &lt; b &amp;&amp; c &gt; d')
        self.assertIn(self.u['intro_text']['en'], result['views']['notes'])
        self.assertNotIn('solved C programs', result['views']['notes'])
        for p in self.u['programs']: self.assertIn(p['title']['en'], result['views']['programs'])

    def test_27_export_metadata_embedded_svgs_catalog_hashes_and_unit1(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(['python3', 'tools/export_app_content.py', '--out', tmp],
                               cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            subject = json.loads(Path(tmp, 'subjects/DI04000031.json').read_text())
            unit = json.loads(Path(tmp, 'units/DI04000031_u2.json').read_text())
            catalog = json.loads(Path(tmp, 'catalog.json').read_text())
            self.assertEqual(subject['available_units'], [1, 2])
            self.assertEqual(catalog['subjects']['DI04000031']['status'], 'available')
            self.assertEqual(set(unit['svgs']), set(TITLES))
            self.assertEqual(unit['programs'], self.u['programs'])
            for rel in ('subjects/DI04000031.json', 'units/DI04000031_u1.json', 'units/DI04000031_u2.json'):
                self.assertEqual(catalog['files'][rel], hashlib.sha1(Path(tmp, rel).read_bytes()).hexdigest()[:12])
            self.assertFalse(Path(tmp, 'units/DI04000031_u3.json').exists())
            u1 = json.loads(Path(tmp, 'units/DI04000031_u1.json').read_text())
            local1 = json.loads((SUBJ_DIR / 'unit1.json').read_text())
            u1.pop('svgs'); self.assertEqual(u1, local1)

    def test_28_deterministic_rebuild_json_svg_preview_and_zip(self):
        files = [SUBJ_DIR / 'unit2.json', SUBJ_DIR / 'subject.json', PREVIEW, Path(ZIP_PATH)]
        files += [DIAG_DIR / (id_ + '.svg') for id_ in TITLES]
        before = {str(p): p.read_bytes() for p in files}
        r = subprocess.run(['python3', 'tools/build_DI04000031_u2.py'], cwd=ROOT,
                           text=True, capture_output=True, timeout=70)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(before, {str(p): p.read_bytes() for p in files})

    def test_29_no_private_credentials_or_runtime_storage_in_deliverables(self):
        secret = json.loads(CREDENTIALS.read_text())['password'].encode()
        blobs = [PREVIEW.read_bytes(), (SUBJ_DIR / 'unit2.json').read_bytes(),
                 (SUBJ_DIR / 'subject.json').read_bytes()]
        with zipfile.ZipFile(ZIP_PATH) as z: blobs += [z.read(n) for n in z.namelist()]
        self.assertFalse(any(secret in blob for blob in blobs), 'A deliverable contains a private credential')
        self.assertFalse((ROOT / '.cache/mongodb-u2').exists())
        self.assertFalse(str(CREDENTIALS).startswith(str(ROOT) + os.sep))
        self.assertFalse(any(re.search(rb'mongodb://[^\s/]+:[^\s/]+@', blob) for blob in blobs),
                         'Unexpected embedded credential-bearing URI')

    def test_30_conceptual_cluster_scope_and_complete_cleanup(self):
        for p in self.u['programs']:
            for forbidden in ('rs.initiate', 'sh.enableSharding', 'sh.shardCollection'):
                self.assertNotIn(forbidden, p['code']['en'])
        lessons = ' '.join(i['body']['en'] for s in self.u['notes'] for i in s['items'])
        self.assertIn('conceptual only', lessons.lower())
        self.assertIn('no failover test is claimed', lessons.lower())
        self.assertIn('No mongos/config-server/shard setup', lessons)
        self.assertEqual(scratch_databases(), [])


if __name__ == '__main__': unittest.main(verbosity=2)
