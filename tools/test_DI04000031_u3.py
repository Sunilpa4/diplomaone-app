"""32 Cassandra Unit 3 validation groups, using real authenticated Cassandra.

Includes all current source execution, actual cqlsh CSV import, key/value/time
verification, negative cases, namespace ownership guards, exported runner,
SVG/HTML/preview/native-export checks and a deterministic rebuild.
"""
import hashlib
import io
import json
import logging
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
from cassandra_content import (assert_runtime, open_session, scratch_keyspaces, nodetool_status,
    credentials, CREDENTIALS, HOME, HOST, PORT)
from cassandra_lab_runner import statements, safe_namespace, run_source, normalize, load_driver
from content_DI04000031_u3_shared import CSV, expected_readings
from content_DI04000031_u3_notes import NOTES, SOURCES
from content_DI04000031_u3_extras import PRACTICE_QS
from diagrams_DI04000031_u3 import TITLES
from export_DI04000031_u3_practicals import OUT as ZIP_PATH
from test_DI04000031_u1 import Fragment, execute_preview

ROOT = Path(ROOT); SUBJ_DIR = Path(SUBJ_DIR); DIAG_DIR = Path(DIAG_DIR)
PREVIEW = ROOT / 'preview/DI04000031_unit3_preview.html'


def row_key(row): return tuple(row[k] for k in ('device_id', 'day', 'reading_at', 'temperature_c', 'status'))


class Unit3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = json.loads((SUBJ_DIR / 'unit3.json').read_text())
        cls.s = json.loads((SUBJ_DIR / 'subject.json').read_text())
        cls.by_id = {p['id']: p for p in cls.u['programs']}
        # Executes all 14 current sources against real Cassandra once, not a mock.
        from content_DI04000031_u3_programs import PROGRAMS
        cls.fresh = {p['id']: p for p in PROGRAMS}

    def output(self, n): return self.by_id[f'ns3p{n:02d}']['out']

    def value(self, n, prefix):
        values = [line[len(prefix) + 2:] for line in self.output(n).splitlines() if line.startswith(prefix + ': ')]
        self.assertEqual(len(values), 1, (n, prefix))
        return json.loads(values[0])

    def test_01_real_runtime_versions_and_read_only_health(self):
        r = assert_runtime()
        self.assertEqual((r['server'], r['cqlsh'], r['cql'], r['driver']), ('5.0.9', '6.2.0', '3.4.7', '3.29.0'))
        self.assertEqual(r['java'], 'Temurin 17.0.21+9')
        self.assertEqual(r['physical_nodes'], 1); self.assertTrue(r['authenticated'])
        self.assertTrue(r['factory_login_disabled'])
        self.assertEqual(r['data_center'], 'datacenter1')
        self.assertRegex(nodetool_status(), r'(?m)^UN\s+127\.0\.0\.1\s')

    def test_02_official_scope_schema_and_content_counts(self):
        u = self.u
        self.assertEqual((u['unit'], u['hours'], u['weightage']), (3, 12, 20))
        self.assertEqual(u['practical_numbers'], [4, 5, 6])
        self.assertEqual(sum(len(g['items']) for g in NOTES), 18)
        self.assertEqual(sum(len(g['items']) for g in u['notes']), 34)
        self.assertEqual(len(u['notes'][-1]['items']), 16)
        self.assertEqual((len(u['programs']), len(u['diagrams'])), (14, 13))
        self.assertEqual(sum(len(g['items']) for g in u['syntax']), 14)
        self.assertEqual(sum(len(g['items']) for g in u['viva']), 52)
        self.assertEqual(u['exam_questions'], [])
        self.assertEqual(self.s['exam'], {'theory_ese':0, 'theory_pa':0, 'practical_pa':20,
                                         'practical_ese':30, 'total':50, 'credits':3})
        expected_files=['unit1.json','unit2.json','unit3.json']+[f'unit{n}.json' if (SUBJ_DIR/f'unit{n}.json').is_file() else None for n in (4,5)]
        self.assertEqual([v['file'] for v in self.s['units']],expected_files)
        self.assertIn('Cassandra’s data model and CQL', u['learning_outcomes'][0]['en'])

    def test_03_exact_current_cql_and_fresh_real_outputs(self):
        self.assertEqual(self.by_id, self.fresh)
        for p in self.u['programs']:
            name, parsed = safe_namespace(p['code']['en'])
            self.assertEqual(name, 'di04000031_u3_' + p['id'])
            self.assertTrue(parsed); self.assertTrue(p['out'].endswith('Scratch keyspace removed: true'))
        self.assertEqual(scratch_keyspaces(), [])

    def test_04_keyspace_lifecycle_versions_and_stored_roundtrip(self):
        self.assertEqual(self.value(1, 'server_versions'), [{'release_version':'5.0.9','cql_version':'3.4.7'}])
        self.assertEqual(self.value(1, 'local_datacenter'), [{'data_center':'datacenter1'}])
        settings = self.value(1, 'keyspace_options')[0]
        self.assertTrue(settings['durable_writes'])
        self.assertEqual(settings['replication']['datacenter1'], '1')
        self.assertIn('NetworkTopologyStrategy', settings['replication']['class'])
        self.assertEqual(self.value(1, 'stored_roundtrip'), [{'id':1,'message':'Cassandra connected'}])
        self.assertEqual(self.value(1, 'tables_after_drop'), [])

    def test_05_real_typed_record_and_fixed_utc_date_uuid(self):
        self.assertEqual(self.value(2, 'typed_profile'), [{
            'learner_id':1, 'name':'Asha', 'active':True, 'joined_at':'2026-10-29T09:00:00.000Z',
            'exam_day':'2026-10-29', 'score':85.5, 'profile_id':'11111111-1111-4111-8111-111111111111'}])

    def test_06_four_logical_partitions_and_descending_rows(self):
        parts = {(r['device_id'], r['day']) for r in self.value(3, 'logical_partitions')}
        self.assertEqual(parts, {('S01','2026-10-29'),('S02','2026-10-29'),('S01','2026-10-30'),('S03','2026-10-29')})
        for label, temps in [('s01_day29',[32.,31.,30.]),('s01_day30',[34.,33.]),('s02_day29',[29.,28.])]:
            self.assertEqual([r['temperature_c'] for r in self.value(3, label)], temps)

    def test_07_insert_upsert_retains_omitted_existing_columns(self):
        self.assertEqual(self.value(4, 'same_primary_key'), [{'learner_id':1,'name':'Asha Patel','city':'Surat','marks':82}])
        self.assertEqual(self.value(4, 'new_primary_key'), [{'learner_id':4,'name':'Imran','city':None,'marks':None}])
        self.assertEqual(self.value(4, 'one_row_for_id1'), [{'n':1}])

    def test_08_where_in_projection_and_missing_empty_result(self):
        self.assertEqual(self.value(5, 'exact_id'), [{'name':'Ravi','city':'Bharuch'}])
        self.assertEqual({(r['learner_id'],r['name']) for r in self.value(5, 'two_known_ids')}, {(1,'Asha'),(3,'Neha')})
        self.assertEqual(self.value(5, 'missing_id'), [])

    def test_09_clustering_order_range_and_limit(self):
        for label, temps in [('latest_two',[32.,31.]),('earliest_two',[30.,31.]),('bounded_range',[31.,30.])]:
            self.assertEqual([r['temperature_c'] for r in self.value(6, label)], temps)
        self.assertEqual([r['reading_at'][11:16] for r in self.value(6, 'bounded_range')], ['09:01','09:00'])

    def test_10_update_existing_and_missing_key_upsert(self):
        self.assertEqual(self.value(7, 'ravi_after_update'), [{'name':'Ravi','city':'Surat','marks':75}])
        self.assertEqual(self.value(7, 'missing_key_created'), [{'learner_id':99,'name':'Jai','city':None,'marks':68}])

    def test_11_cell_row_and_partition_deletion(self):
        self.assertEqual(self.value(8, 'city_cell_deleted'), [{'learner_id':1,'name':'Asha','city':None,'marks':82}])
        self.assertEqual(self.value(8, 'learner_row_deleted'), [])
        self.assertEqual(self.value(8, 'one_sensor_row_deleted'), [{'n':2}])
        self.assertEqual(self.value(8, 'whole_partition_deleted'), [{'n':0}])

    def test_12_schema_add_write_drop_and_table_removal(self):
        self.assertEqual(self.value(9, 'added_column_initially_null'), [{'learner_id':1,'name':'Asha','city':None}])
        self.assertEqual(self.value(9, 'added_column_written'), [{'name':'Asha','city':'Surat'}])
        self.assertEqual(self.value(9, 'table_comment'), [{'comment':'Small schema-change lab'}])
        self.assertEqual(self.value(9, 'columns_after_drop'), [
            {'column_name':'learner_id','kind':'partition_key','type':'int'},
            {'column_name':'name','kind':'regular','type':'text'}])
        self.assertEqual(self.value(9, 'table_removed'), [])

    def test_13_query_table_denormalization_staleness_and_correction(self):
        self.assertEqual(self.value(10, 'high_day29')[0]['temperature_c'], 32.)
        for label, temp in [('base_corrected',35.),('second_table_still_old',32.),('second_table_corrected',35.)]:
            self.assertEqual(self.value(10, label), [{'temperature_c':temp}])

    def test_14_actual_filter_rejection_and_bounded_allow_filtering(self):
        self.assertIn('non_key_filter_rejected: InvalidRequest (server rejection)', self.output(11))
        self.assertIn('limit_does_not_legalize_filter: InvalidRequest (server rejection)', self.output(11))
        self.assertEqual([r['temperature_c'] for r in self.value(11, 'bounded_partition_filter')], [32.,31.])

    def test_15_actual_cqlsh_csv_import_all_eight_keys_values_and_times(self):
        self.assertIn('csv_import: cqlsh COPY FROM completed (8 rows imported)', self.output(12))
        self.assertEqual(self.value(12, 'imported_row_count'), [{'n':8}])
        rows = self.value(12, 'imported_rows')
        self.assertEqual(sorted(map(row_key, rows)), sorted(map(row_key, expected_readings())))
        self.assertEqual(len({(r['device_id'],r['day'],r['reading_at']) for r in rows}), 8)
        self.assertEqual(len(self.value(12, 'imported_partitions')), 4)
        self.assertEqual(self.value(12, 'latest_imported_reading'), [
            {'reading_at':'2026-10-29T09:02:00.000Z','temperature_c':32.}])
        self.assertIn("DATETIMEFORMAT='%Y-%m-%dT%H:%M:%S%z'", self.by_id['ns3p12']['code']['en'])

    def test_16_real_per_partition_analytical_features(self):
        self.assertEqual(self.value(13, 's01_day29_features'), [
            {'samples':3,'total':93.,'mean':31.,'minimum':30.,'maximum':32.}])
        for label, count, mean in [('s02_day29_features',2,28.5),('s01_day30_features',2,33.5),('s03_day29_features',1,27.)]:
            self.assertEqual(self.value(13, label), [{'samples':count,'mean':mean}])

    def test_17_real_negative_type_null_key_order_mutation_and_syntax(self):
        for label in ('wrong_int_type','null_primary_key','regular_column_ordering','primary_key_set_rejected'):
            self.assertIn(label + ': InvalidRequest (server rejection)', self.output(14))
        self.assertIn('bad_cql_syntax: SyntaxException (server rejection)', self.output(14))
        self.assertEqual(self.value(14, 'valid_rows_unchanged'), [{'n':3}])
        self.assertEqual(self.value(14, 'missing_is_empty'), [])

    def test_18_unauthenticated_and_factory_connections_rejected(self):
        _, Cluster, Auth, Policy, _ = load_driver(HOME)
        logger = logging.getLogger('cassandra'); old = logger.level; logger.setLevel(logging.CRITICAL)
        try:
            for auth in (None, Auth(username='cassandra',password='cassandra')):
                cluster = Cluster([HOST], port=PORT, protocol_version=4, auth_provider=auth,
                                  load_balancing_policy=Policy(local_dc='datacenter1'), connect_timeout=5)
                try:
                    with self.assertRaises(Exception) as caught: cluster.connect()
                    # Real native-protocol authentication failed, not just a timed-out absent service.
                    self.assertIn('AuthenticationFailed', str(caught.exception))
                finally: cluster.shutdown()
        finally: logger.setLevel(old)

    def test_19_existing_namespace_is_preserved_and_failed_run_cleans_only_own(self):
        private = credentials(); cluster, session = open_session()
        name = 'di04000031_u3_ownership_test'
        create = "CREATE KEYSPACE " + name + " WITH replication={'class':'NetworkTopologyStrategy','datacenter1':1}"
        created = False
        try:
            self.assertIsNone(session.execute('SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name=%s',(name,)).one())
            session.execute(create); created = True
            session.execute('CREATE TABLE ' + name + '.sentinel (id int PRIMARY KEY, value text)')
            session.execute('INSERT INTO ' + name + ".sentinel (id,value) VALUES (1,'preserve')")
            with self.assertRaisesRegex(RuntimeError, 'Refusing pre-existing keyspace'):
                run_source(create + '; USE ' + name + '; DROP KEYSPACE ' + name + ';', session,
                           private['username'],private['password'],HOME,HOST,PORT)
            self.assertEqual(session.execute('SELECT value FROM ' + name + '.sentinel WHERE id=1').one()['value'], 'preserve')
        finally:
            if created: session.execute('DROP KEYSPACE ' + name)
            cluster.shutdown()
        # Deterministic CREATE interleaving, with REAL server DDL/errors: another
        # creator appears after the preflight read. A failed CREATE must NOT own it.
        name = 'di04000031_u3_create_race'
        create = "CREATE KEYSPACE " + name + " WITH replication={'class':'NetworkTopologyStrategy','datacenter1':1}"
        cluster, real = open_session(); interposed = False
        class InterleavedSession:
            def execute(inner, sql, *args):
                nonlocal interposed
                if sql == create and not interposed:
                    real.execute(create); interposed = True
                    real.execute('CREATE TABLE ' + name + '.sentinel (id int PRIMARY KEY, value text)')
                    real.execute('INSERT INTO ' + name + ".sentinel (id,value) VALUES (1,'other creator')")
                return real.execute(sql, *args)
        try:
            with self.assertRaises(Exception) as caught:
                run_source(create + '; USE ' + name + '; DROP KEYSPACE ' + name + ';',
                           InterleavedSession(), private['username'],private['password'],HOME,HOST,PORT)
            self.assertEqual(type(caught.exception).__name__, 'AlreadyExists')
            self.assertTrue(interposed)
            self.assertEqual(real.execute('SELECT value FROM ' + name + '.sentinel WHERE id=1').one()['value'], 'other creator')
        finally:
            if interposed: real.execute('DROP KEYSPACE ' + name)
            cluster.shutdown()
        # Unexpected data failure after successful CREATE invokes owned cleanup.
        name = 'di04000031_u3_failed_run'
        source = "CREATE KEYSPACE " + name + " WITH replication={'class':'NetworkTopologyStrategy','datacenter1':1}; USE " + name + '; SELECT * FROM absent_table;'
        cluster, session = open_session()
        try:
            with self.assertRaises(Exception):
                run_source(source,session,private['username'],private['password'],HOME,HOST,PORT)
            self.assertIsNone(session.execute('SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name=%s',(name,)).one())
        finally: cluster.shutdown()
        self.assertEqual(scratch_keyspaces(), [])

    def test_20_lexer_comments_quotes_and_context_guards(self):
        sql = "-- @result value\nSELECT 'a;--b''c' FROM probe; -- trailing\n"
        self.assertEqual(statements(sql), [("SELECT 'a;--b''c' FROM probe",'value',None)])
        with self.assertRaises(ValueError): statements("SELECT 'unterminated;")
        for source in ("CREATE KEYSPACE production WITH replication={};",
                       "CREATE KEYSPACE di04000031_u3_bad WITH replication={}; USE production;",
                       "CREATE KEYSPACE di04000031_u3_bad WITH replication={}; DROP KEYSPACE system;",
                       "CREATE KEYSPACE di04000031_u3_bad WITH replication={}; CREATE ROLE unsafe WITH LOGIN=true;"):
            with self.assertRaises(ValueError): safe_namespace(source)
        from cassandra_lab_runner import copy_from
        with self.assertRaisesRegex(RuntimeError, 'Set CASSANDRA_HOME'):
            copy_from("COPY t FROM 'sensors.csv'", 'di04000031_u3_demo', 'unused', 'unused', None, HOST, PORT, '.')
        self.assertEqual(statements('-- @result rejected\n-- @expect InvalidRequest\nSELECT bad FROM t;')[0][1:],
                         ('rejected','InvalidRequest'))

    def test_21_english_safe_html_references_and_all_program_links(self):
        def english(obj):
            if isinstance(obj,dict):
                self.assertNotIn('gu',obj); self.assertNotIn('key',obj)
                for val in obj.values(): english(val)
            elif isinstance(obj,list):
                for val in obj: english(val)
            elif isinstance(obj,str): self.assertIsNone(re.search(r'[\u0a80-\u0aff]',obj))
        english(self.u); self.assertEqual(self.s['languages'], ['en'])
        self.assertEqual(self.s['code_lang'], 'nosql')
        linked = set()
        for group in self.u['notes']:
            for item in group['items']:
                Fragment().finish(item['body']['en']); self.assertNotIn('@@',item['body']['en'])
                linked.update(item.get('programs',[]))
        self.assertEqual(linked,set(self.by_id))
        for p in self.u['programs']: Fragment().finish(p['expl']['en'])
        for g in self.u['viva']:
            for q in g['items']: Fragment().finish(q['a']['en'])
        self.assertEqual(len(self.u['sources']),len(SOURCES))
        for q,item in zip(PRACTICE_QS,self.u['notes'][-1]['items']):
            self.assertEqual((q['q'],q['a']),(item['h'],item['body'])); self.assertNotIn('marks',q)

    def test_22_svg_integrity_raster_and_contact_sheets(self):
        self.assertEqual({d['id'] for d in self.u['diagrams']},set(TITLES))
        used={i['diagram'] for s in self.u['notes'] for i in s['items'] if 'diagram' in i}
        self.assertEqual(used,set(TITLES))
        checks=ROOT/'preview/nosql_u3_checks';checks.mkdir(exist_ok=True)
        images=[]
        for d in self.u['diagrams']:
            file=SUBJ_DIR/d['file'];raw=file.read_text();root=ET.fromstring(raw)
            self.assertEqual(root.get('viewBox').split()[2],'360')
            for bad in ('<marker','<image','<foreignObject','<script','<style','href=','url('): self.assertNotIn(bad,raw)
            image=Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_path=str(file),zoom=1.4,
                font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',
                sans_serif_family='DejaVu Sans',skip_system_fonts=True)))).convert('RGB')
            image.save(checks/(d['id']+'.png'));images.append((d['id'],image))
        for batch,label in [(images[:4],'a'),(images[4:8],'b'),(images[8:],'c')]:
            w,h=530,770;sheet=Image.new('RGB',(w*2,h*((len(batch)+1)//2)),'#EAE4F1');draw=ImageDraw.Draw(sheet)
            for i,(id_,image) in enumerate(batch):
                x=i%2*w+12;y=i//2*h+29
                self.assertLessEqual(image.height+29,h)
                draw.text((x,y-22),id_,fill='#4C1C85');sheet.paste(image,(x,y))
            sheet.save(ROOT/f'preview/DI04000031_unit3_diagrams_{label}.png')

    def test_23_svg_text_viewport_bounds(self):
        for id_ in TITLES:
            root=ET.parse(DIAG_DIR/(id_+'.svg')).getroot();_,_,width,height=map(float,root.get('viewBox').split())
            for node in root.iter('{http://www.w3.org/2000/svg}text'):
                size=float(node.get('font-size','12'))
                file='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
                font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+file,round(size*10))
                tw=font.getlength(''.join(node.itertext()))/10;x=float(node.get('x'));y=float(node.get('y'))
                anchor=node.get('text-anchor','start');left=x-tw/2 if anchor=='middle' else x-tw if anchor=='end' else x
                self.assertGreaterEqual(left,1,(id_,node.text,left));self.assertLessEqual(left+tw,width-1,(id_,node.text,left+tw))
                self.assertGreater(y-size,-1);self.assertLess(y+size/3,height+1)

    def test_24_cql_source_completeness_readability_and_expected_failures(self):
        for p in self.u['programs']:
            source=p['code']['en'];name,parsed=safe_namespace(source)
            self.assertNotIn('@@',source)
            self.assertEqual(parsed[-2][0],'USE system');self.assertEqual(parsed[-1][0],'DROP KEYSPACE '+name)
            self.assertLessEqual(max(map(len,source.splitlines())),78)
        failures=[expect for p in self.u['programs'] for _,_,expect in statements(p['code']['en']) if expect]
        self.assertEqual(failures.count('InvalidRequest'),6);self.assertEqual(failures.count('SyntaxException'),1)

    def test_25_zip_exact_sources_outputs_csv_and_runtime(self):
        with zipfile.ZipFile(ZIP_PATH) as z:
            self.assertEqual(len(z.namelist()),32)
            self.assertEqual(z.read('sensors.csv').decode(),CSV)
            self.assertEqual(z.read('run_lab.py'),(ROOT/'tools/cassandra_lab_runner.py').read_bytes())
            self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
            for p in self.u['programs']:
                self.assertEqual(z.read('examples/'+p['id']+'.cql').decode(),p['code']['en']+'\n')
                self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out']+'\n')
            self.assertEqual(hashlib.sha256(z.read('sensors.csv')).hexdigest(),self.u['runtime_evidence']['fixture']['sha256'])

    def public_runner(self,only=None,tz=None):
        private=credentials();env=os.environ.copy();env.update({'CASSANDRA_HOME':str(HOME),
            'CASSANDRA_USERNAME':private['username'],'CASSANDRA_PASSWORD':private['password']})
        if tz:env['TZ']=tz
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ZIP_PATH) as z:z.extractall(tmp)
            for p in self.u['programs']:
                if only and p['id']!=only:continue
                r=subprocess.run(['python3','run_lab.py','examples/'+p['id']+'.cql','--port',str(PORT)],
                    cwd=tmp,env=env,text=True,capture_output=True,timeout=100)
                self.assertEqual(r.returncode,0,(p['id'],r.stderr))
                self.assertEqual(r.stdout.rstrip('\n'),p['out'],p['id']);self.assertEqual(r.stderr,'',p['id'])

    def test_26_public_zip_runner_reexecutes_all_fourteen_real_scripts(self):
        self.public_runner();self.assertEqual(scratch_keyspaces(),[])

    def test_27_preview_all_five_views_neutral_code_and_diagram_heading(self):
        result=execute_preview(PREVIEW)
        self.assertEqual(set(result['views']),{'notes','programs','diagrams','syntax','viva'})
        self.assertEqual(result['languageHidden'],'none');self.assertEqual(result['neutral'],'a &lt; b &amp;&amp; c &gt; d')
        self.assertIn('<span>Diagrams</span>',result['views']['diagrams'])
        self.assertNotIn('<span>Flowcharts</span>',result['views']['diagrams'])
        self.assertEqual(result['views']['diagrams'].count('class="dcard"'),13)
        self.assertIn(self.u['intro_text']['en'],result['views']['notes'])
        self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')
        for p in self.u['programs']:self.assertIn(p['title']['en'],result['views']['programs'])

    def test_28_export_availability_hashes_embedded_svgs_and_prior_units(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=subprocess.run(['python3','tools/export_app_content.py','--out',tmp],cwd=ROOT,text=True,capture_output=True)
            self.assertEqual(r.returncode,0,r.stdout+r.stderr)
            s=json.loads(Path(tmp,'subjects/DI04000031.json').read_text())
            u=json.loads(Path(tmp,'units/DI04000031_u3.json').read_text())
            catalog=json.loads(Path(tmp,'catalog.json').read_text())
            expected_available=[1,2,3]+[n for n in (4,5) if (SUBJ_DIR/f'unit{n}.json').is_file()]
            self.assertEqual(s['available_units'],expected_available);self.assertEqual(len(s['units']),5)
            self.assertEqual(u['programs'],self.u['programs']);self.assertEqual(set(u['svgs']),set(TITLES))
            for rel in ('subjects/DI04000031.json','units/DI04000031_u1.json','units/DI04000031_u2.json','units/DI04000031_u3.json'):
                self.assertEqual(catalog['files'][rel],hashlib.sha1(Path(tmp,rel).read_bytes()).hexdigest()[:12])
            for n in (1,2):
                prior=json.loads(Path(tmp,f'units/DI04000031_u{n}.json').read_text());prior.pop('svgs')
                self.assertEqual(prior,json.loads((SUBJ_DIR/f'unit{n}.json').read_text()))
            for n in (4,5):
                self.assertEqual(Path(tmp,f'units/DI04000031_u{n}.json').exists(),(SUBJ_DIR/f'unit{n}.json').is_file())

    def test_29_deterministic_rebuild_json_svg_preview_and_zip(self):
        files=[SUBJ_DIR/'unit3.json',SUBJ_DIR/'subject.json',PREVIEW,Path(ZIP_PATH)]
        files += [DIAG_DIR/(id_+'.svg') for id_ in TITLES]
        before={str(p):p.read_bytes() for p in files}
        r=subprocess.run(['python3','tools/build_DI04000031_u3.py'],cwd=ROOT,text=True,capture_output=True,timeout=100)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        self.assertEqual(before,{str(p):p.read_bytes() for p in files})

    def test_30_csv_runner_is_timezone_portable_and_preserves_every_time(self):
        self.public_runner(only='ns3p12',tz='Asia/Kolkata')
        self.assertEqual(sorted(map(row_key,self.value(12,'imported_rows'))),sorted(map(row_key,expected_readings())))
        self.assertEqual(scratch_keyspaces(),[])

    def test_31_no_private_secrets_or_runtime_data_in_deliverables(self):
        secret=credentials()['password'].encode()
        blobs=[PREVIEW.read_bytes(),(SUBJ_DIR/'unit3.json').read_bytes(),(SUBJ_DIR/'subject.json').read_bytes()]
        with zipfile.ZipFile(ZIP_PATH) as z:
            self.assertFalse(any('credential' in name or name.endswith('.db') for name in z.namelist()))
            blobs += [z.read(name) for name in z.namelist()]
        self.assertFalse(any(secret in b for b in blobs),'Unexpected private credential in a deliverable')
        self.assertFalse(CREDENTIALS.is_relative_to(ROOT));self.assertFalse((ROOT/'.cache/diplomaone-cassandra-u3').exists())

    def test_32_single_node_health_awareness_scope_and_complete_cleanup(self):
        r=self.u['runtime_evidence']
        self.assertEqual(r['physical_nodes'],1);self.assertEqual(r['lab_replication_factor'],1)
        for key in ('multi_node_distribution_tested','failover_tested','cluster_operations_performed','public_database_endpoint'):
            self.assertFalse(r[key])
        self.assertEqual(r['fixture']['stored_rows'],8);self.assertEqual(r['fixture']['logical_partitions'],4)
        self.assertTrue(r['fixture']['all_keys_values_times_match']);self.assertFalse(r['fixture']['live_ingestion'])
        notes=' '.join(i['body']['en'] for g in self.u['notes'] for i in g['items'])
        self.assertIn('awareness level only',notes);self.assertIn('one physical node',notes)
        self.assertIn('not a trained',notes.lower())
        for p in self.u['programs']:
            for forbidden in ('nodetool repair','nodetool decommission','ALTER SYSTEM','CREATE ROLE'):
                self.assertNotIn(forbidden,p['code']['en'])
        self.assertEqual(scratch_keyspaces(),[])


if __name__=='__main__':unittest.main(verbosity=2)
