"""36 Unit 4 validation groups: real Neo4j, official driver and Cypher Shell.

No mock engine. Verifies all 16 current/ZIP scripts, exact fixtures/errors,
authentication and atomic ownership, safe HTML/SVG/preview/catalog integration,
DB-independent deterministic export and preservation of published Units 1–3.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

import resvg_py
from PIL import Image,ImageDraw,ImageFont

from subject_DI04000031 import ROOT,SUBJ_DIR,DIAG_DIR
from neo4j_content import (assert_runtime,authentication_rejections,open_driver,DATABASE,URI,
    credentials,CREDENTIALS,run_script,source_for,scratch_artifacts,shell)
from neo4j_lab_runner import statements,safe_scope,run_source,scope_count,scope_constraints,normalize
from content_DI04000031_u4_shared import PEOPLE,FRIENDSHIPS,FIXTURE_JSON
from content_DI04000031_u4_notes import NOTES,SOURCES
from content_DI04000031_u4_extras import PRACTICE_QS
from diagrams_DI04000031_u4 import TITLES
from export_DI04000031_u4_practicals import OUT as ZIP_PATH,REQUIREMENTS
from export_app_content import clean_svg
from test_DI04000031_u1 import Fragment,execute_preview

ROOT=Path(ROOT);SUBJ_DIR=Path(SUBJ_DIR);DIAG_DIR=Path(DIAG_DIR)
PREVIEW=ROOT/'preview/DI04000031_unit4_preview.html'
EMPTY={'scope_labels':[],'constraints':[]}
PRIOR_SOURCE_SHA={
 1:'275a0d08e5b134c8ad8cfd19084130020a99c13ac5a90b946854585d37587b5f',
 2:'a7a61cfd843284fc6d2d88262fd03ca8a73ef3cdea9ac97d8f3f9914b16004fe',
 3:'0c24ae5ab9e8f534987d042465e467e026b2187b6138c4ad965fed01537da694',
}
PRIOR_PUBLIC_SHA={
 1:'9dad2b0c9a9122cc31ca1cccb5d92013cd92ca4a142418be86b7d57589624df2',
 2:'eeeb83bb993f5a3e91ee46710927519d4c5b0afd9fe8d9c1988ee45da38a8a37',
 3:'19dfcd387ac094233d438ece6c508dcf9496389a6ed9ad305de583cabd39f06e',
}


class Unit4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u=json.loads((SUBJ_DIR/'unit4.json').read_text())
        cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
        cls.by_id={p['id']:p for p in cls.u['programs']}
        # Import executes all exact current Cypher sources against the REAL server.
        from content_DI04000031_u4_programs import PROGRAMS
        cls.fresh={p['id']:p for p in PROGRAMS}

    def output(self,n):return self.by_id[f'ns4p{n:02d}']['out']

    def value(self,n,label):
        lines=[s[len(label)+2:] for s in self.output(n).splitlines() if s.startswith(label+': ')]
        self.assertEqual(len(lines),1,(n,label));return json.loads(lines[0])

    def test_01_real_authenticated_versions_protocol_and_cli(self):
        runtime=assert_runtime()
        self.assertEqual((runtime['server'],runtime['shell'],runtime['driver']),('5.26.32','5.26.32','5.28.8'))
        self.assertEqual(runtime['java'],'Temurin 21.0.13+9');self.assertEqual(runtime['edition'],'community')
        self.assertEqual(runtime['bolt_protocol'],'5.8');self.assertTrue(runtime['authenticated'])
        self.assertFalse(runtime['server_usage_reporting']);self.assertFalse(runtime['graph_algorithm_library_installed'])
        self.assertEqual(shell('RETURN 1 AS connected;'),'connected\n1')

    def test_02_official_scope_counts_and_subject_metadata(self):
        u=self.u
        self.assertEqual((u['unit'],u['hours'],u['weightage']),(4,12,20))
        self.assertEqual(u['title'],{'en':'Graph Databases: Neo4j'})
        self.assertEqual(u['practical_numbers'],[7,8]);self.assertEqual(u['exam_questions'],[])
        self.assertEqual(sum(len(g['items']) for g in NOTES),20)
        self.assertEqual(sum(len(g['items']) for g in u['notes']),38)
        self.assertEqual(len(u['notes'][-1]['items']),18)
        self.assertEqual((len(u['programs']),len(u['diagrams'])),(16,14))
        self.assertEqual(sum(len(g['items']) for g in u['syntax']),16)
        self.assertEqual(sum(len(g['items']) for g in u['viva']),56)
        self.assertEqual(self.s['exam'],{'theory_ese':0,'theory_pa':0,'practical_pa':20,'practical_ese':30,'total':50,'credits':3})
        self.assertEqual([s['file'] for s in self.s['units']],['unit1.json','unit2.json','unit3.json','unit4.json',None])
        self.assertIn('Utilize Neo4j to solve relationship-based problems',u['learning_outcomes'][0]['en'])

    def test_03_exact_current_sources_and_fresh_real_outputs(self):
        self.assertEqual(self.by_id,self.fresh)
        for p in self.u['programs']:
            scope,claim,parsed=safe_scope(p['code']['en'])
            self.assertEqual(scope,'NS4_'+p['id']);self.assertTrue(claim.endswith('_owner'))
            self.assertGreater(len(parsed),4)
            self.assertTrue(p['out'].endswith('Scoped graph and constraints removed: true'))
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_04_server_components_and_real_committed_probe(self):
        self.assertEqual(self.value(1,'server_components'),[{'name':'Neo4j Kernel','versions':['5.26.32'],'edition':'community'}])
        self.assertEqual(self.value(1,'created_probe'),[{'id':1,'message':'Graph connected'}])
        self.assertEqual(self.value(1,'stored_roundtrip'),[{'message':'Graph connected'}])
        counters=self.value(1,'created_probe_counters')
        self.assertEqual(counters['nodes_created'],1);self.assertEqual(counters['properties_set'],2)
        self.assertEqual(counters['relationships_created'],0)

    def test_05_multiple_labels_and_stored_typed_properties(self):
        self.assertEqual(self.value(2,'typed_person'),[{'name':'Asha','age':20,'active':True,'score':85.5,
            'skills':['Python','Cypher'],'joined':'2026-10-29','observed_at':'2026-10-29T09:00:00.000Z','student_label':True}])

    def test_06_directed_typed_relationship_and_its_property(self):
        self.assertEqual(self.value(3,'stored_relationship'),[{'source':'Asha','relationship':'KNOWS','target':'Ravi','since':2024}])

    def test_07_match_filters_projection_and_typed_equality(self):
        self.assertEqual(self.value(4,'surat_adults'),[{'id':'P01','name':'Asha','age':20},{'id':'P05','name':'Imran','age':20}])
        self.assertEqual(self.value(4,'selected_ages'),[{'id':'P03','name':'Neha'},{'id':'P06','name':'Dev'}])
        self.assertEqual(self.value(4,'either_condition'),[{'id':'P02','name':'Ravi'},{'id':'P06','name':'Dev'}])
        self.assertEqual(self.value(4,'string_is_not_integer'),[])

    def test_08_outgoing_incoming_and_either_direction(self):
        for label,expected in [('asha_outgoing',['P02','P03']),('ravi_incoming',['P01']),('ravi_either_direction',['P01','P04','P05'])]:
            self.assertEqual([row['id'] for row in self.value(5,label)],expected)

    def test_09_order_limit_distinct_and_city_counts(self):
        self.assertEqual(self.value(6,'oldest_three'),[{'id':'P06','name':'Dev','age':23},{'id':'P04','name':'Meera','age':22},{'id':'P02','name':'Ravi','age':21}])
        self.assertEqual(self.value(6,'distinct_cities'),[{'city':c} for c in ('Bharuch','Rajkot','Surat','Vadodara')])
        self.assertEqual(self.value(6,'people_per_city'),[{'city':c,'people':n} for c,n in [('Bharuch',1),('Rajkot',1),('Surat',3),('Vadodara',1)]])
        self.assertEqual(self.value(6,'surat_count'),[{'people':3}])

    def test_10_merge_create_match_branches_and_single_identity(self):
        self.assertEqual(self.value(7,'first_merge'),[{'id':'P09','name':'Jai','visits':1}])
        self.assertEqual(self.value(7,'second_merge'),[{'id':'P09','name':'Jai','visits':2}])
        self.assertEqual(self.value(7,'one_business_node'),[{'people':1}])

    def test_11_property_label_updates_and_missing_match_no_upsert(self):
        self.assertEqual(self.value(8,'updated_ravi'),[{'name':'Ravi','city':'Surat','age':22}])
        self.assertEqual(self.value(8,'removed_city'),[{'name':'Ravi','city':None,'age':22}])
        self.assertEqual(self.value(8,'label_added'),[{'name':'Ravi','graduate':True}])
        self.assertEqual(self.value(8,'label_removed'),[{'name':'Ravi','graduate':False}])
        self.assertEqual(self.value(8,'missing_update'),[]);self.assertEqual(self.value(8,'people_unchanged'),[{'people':6}])

    def test_12_connected_delete_rejection_and_real_delete_counters(self):
        self.assertIn('connected_node_rejected: Neo.ClientError.Schema.ConstraintValidationFailed (server rejection)',self.output(9))
        self.assertEqual(self.value(9,'asha_still_present'),[{'people':1}])
        self.assertEqual(self.value(9,'delete_relationship_counters')['relationships_deleted'],1)
        self.assertEqual(self.value(9,'delete_now_isolated_asha_counters')['nodes_deleted'],1)
        counter=self.value(9,'detach_ravi_counters')
        self.assertEqual((counter['nodes_deleted'],counter['relationships_deleted']),(1,1))
        self.assertEqual(self.value(9,'remaining_people'),[{'id':'P03','name':'Neha'}])

    def test_13_optional_match_nulls_and_row_vs_expression_counts(self):
        self.assertEqual(self.value(10,'optional_mentees'),[{'id':p['person_id'],'mentee':'Ravi' if i==0 else None} for i,p in enumerate(PEOPLE)])
        self.assertEqual(self.value(10,'row_vs_linked_count'),[{'rows':6,'linked':1}])
        self.assertEqual(self.value(10,'only_linked_people'),[{'mentor':'Asha','mentee':'Ravi'}])

    def test_14_business_uniqueness_index_and_failed_statement_rollback(self):
        self.assertEqual(self.value(11,'business_constraint'),[{'name':'di04000031_u4_ns4p11_person_id','type':'UNIQUENESS','properties':['person_id']}])
        self.assertEqual(self.value(11,'backing_index'),[{'state':'ONLINE','owningConstraint':'di04000031_u4_ns4p11_person_id'}])
        self.assertIn('duplicate_rejected: Neo.ClientError.Schema.ConstraintValidationFailed (server rejection)',self.output(11))
        self.assertEqual(self.value(11,'failed_statement_rolled_back'),[{'people':0}])
        self.assertEqual(self.value(11,'missing_id_is_allowed_by_uniqueness_only'),[{'id':'P01','name':'Asha'},{'id':None,'name':'No ID'}])

    def test_15_real_parameter_binding_and_literal_selector_shaped_text(self):
        self.assertEqual(self.value(12,'parameter_match'),[{'id':'P01','name':'Asha','city':'Surat'}])
        self.assertEqual(self.value(12,'selector_shaped_text_is_not_query_code'),[])
        self.assertEqual(self.value(12,'missing_parameter_value'),[])
        params=[s['params'] for s in statements(self.by_id['ns4p12']['code']['en']) if 'params' in s]
        self.assertEqual(params,[{'name':'Asha'},{'name':"Asha' OR true //"},{'name':'Nobody'}])

    def test_16_exact_social_and_movie_candidate_queries(self):
        self.assertEqual(self.value(13,'friend_candidates'),[{'id':'P04','name':'Meera'},{'id':'P05','name':'Imran'}])
        self.assertEqual(self.value(13,'unseen_movies_liked_by_known_people'),[{'id':'M02','title':'Database Stories'},{'id':'M03','title':'Space Signals'}])
        self.assertNotIn('P06',[r['id'] for r in self.value(13,'friend_candidates')])

    def test_17_shared_device_counts_and_three_distinct_review_pairs(self):
        self.assertEqual(self.value(14,'accounts_per_device'),[{'device':'D01','accounts':3},{'device':'D02','accounts':1}])
        self.assertEqual(self.value(14,'shared_device_pairs'),[{'device':'D01','account_a':a,'account_b':b} for a,b in [('A01','A02'),('A01','A04'),('A02','A04')]])

    def test_18_actual_json_import_all_six_people_edges_and_properties(self):
        self.assertEqual(self.value(15,'verify_every_person'),[{'id':p['person_id'],'name':p['name'],'city':p['city'],'age':p['age']} for p in PEOPLE])
        wanted=sorted([{'source':e['from'],'target':e['to'],'since':e['since']} for e in FRIENDSHIPS],key=lambda x:(x['source'],x['target']))
        self.assertEqual(self.value(15,'verify_every_relationship'),wanted)
        self.assertEqual(self.value(15,'imported_people_counters')['nodes_created'],6)
        self.assertEqual(self.value(15,'imported_friendships_counters')['relationships_created'],6)
        self.assertEqual(self.value(15,'imported_people_counters')['properties_set'],24)

    def test_19_real_type_syntax_semantic_errors_and_unchanged_graph(self):
        for label,kind in [('nested_property_map_rejected','TypeError'),('unknown_variable_rejected','SyntaxError'),
                           ('null_merge_key_rejected','SemanticError'),('bad_pattern_syntax','SyntaxError')]:
            self.assertIn(label+': Neo.ClientError.Statement.'+kind+' (server rejection)',self.output(16))
        self.assertEqual(self.value(16,'valid_people_unchanged'),[{'people':6}])
        self.assertEqual(self.value(16,'missing_person'),[])

    def test_20_anonymous_and_old_default_password_rejected_by_real_server(self):
        denials=authentication_rejections()
        self.assertEqual(denials,{'anonymous':'Neo.ClientError.Security.Unauthorized','factory_password':'Neo.ClientError.Security.Unauthorized'})
        self.assertEqual(self.u['runtime_evidence']['anonymous_rejection'],denials['anonymous'])
        self.assertEqual(self.u['runtime_evidence']['factory_password_rejection'],denials['factory_password'])

    def test_21_actual_matching_cypher_shell_runs_full_positive_scripts(self):
        self.assertEqual(scratch_artifacts(),EMPTY)
        first=shell(self.by_id['ns4p01']['code']['en'])
        self.assertIn('5.26.32',first);self.assertIn('Graph connected',first)
        social=shell(self.by_id['ns4p13']['code']['en'])
        for text in ('Meera','Imran','Database Stories','Space Signals'):self.assertIn(text,social)
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_22_preexisting_nodes_and_constraint_only_scope_are_preserved(self):
        source=source_for('collision_test',"CREATE (:@@L@@:Probe {value:'ours'});")
        scope,claim,parsed=safe_scope(source)
        with open_driver() as driver,driver.session(database=DATABASE) as session:
            self.assertEqual(scope_count(session,scope),0);self.assertEqual(scope_constraints(session,scope),[])
            session.run('CREATE (:'+scope+" {value:'preserve'})").consume()
            try:
                with self.assertRaisesRegex(RuntimeError,'Refusing pre-existing'):
                    run_source(source,session)
                self.assertEqual(session.run('MATCH (n:'+scope+') RETURN n.value AS value').single()['value'],'preserve')
            finally:session.run('MATCH (n:'+scope+') DETACH DELETE n').consume()
            session.run(parsed[0]['sql']).consume()
            try:
                with self.assertRaisesRegex(RuntimeError,'Refusing pre-existing'):
                    run_source(source,session)
                self.assertEqual(scope_constraints(session,scope),[claim])
            finally:session.run('DROP CONSTRAINT '+claim).consume()
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_23_real_atomic_claim_interleaving_and_unexpected_failure_cleanup(self):
        source=source_for('claim_race',"CREATE (:@@L@@:Probe {value:'ours'});")
        scope,claim,parsed=safe_scope(source);interposed=False
        with open_driver() as driver,driver.session(database=DATABASE) as real:
            class InterleavedSession:
                def run(inner,sql,*args,**kwargs):
                    nonlocal interposed
                    if sql==parsed[0]['sql'] and not interposed:
                        real.run(sql).consume();interposed=True
                        real.run('CREATE (:'+scope+" {value:'other creator'})").consume()
                    return real.run(sql,*args,**kwargs)
            try:
                with self.assertRaises(Exception) as caught:run_source(source,InterleavedSession())
                self.assertTrue(interposed)
                self.assertIn(getattr(caught.exception,'code',None),[
                    'Neo.ClientError.Schema.ConstraintAlreadyExists','Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists'])
                self.assertEqual(real.run('MATCH (n:'+scope+') RETURN n.value AS value').single()['value'],'other creator')
                self.assertEqual(scope_constraints(real,scope),[claim])
            finally:
                if interposed:
                    real.run('MATCH (n:'+scope+') DETACH DELETE n').consume()
                    real.run('DROP CONSTRAINT '+claim).consume()
        source=source_for('failed_run','MATCH (p:@@L@@) RETURN unknown.name;')
        with self.assertRaises(Exception) as caught:run_script(source)
        self.assertEqual(getattr(caught.exception,'code',None),'Neo.ClientError.Statement.SyntaxError')
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_24_lexer_directives_context_guards_and_fixture_failures(self):
        parsed=statements("// @result literal\nRETURN 'a; // b' AS value;")
        self.assertEqual(parsed,[{'sql':"RETURN 'a; // b' AS value",'result':'literal'}])
        escaped=r"RETURN 'A\'sha; // still string' AS name;"
        self.assertEqual(len(statements(escaped)),1)
        with self.assertRaises(ValueError):statements("RETURN 'unterminated;")
        for body in ('CREATE USER dangerous SET PASSWORD \'not-real\';',
                     'DROP DATABASE neo4j;', 'MATCH (n) DETACH DELETE n;',
                     'CALL apoc.help(\'x\');',
                     'CREATE CONSTRAINT outside FOR (n:@@L@@) REQUIRE n.x IS UNIQUE;'):
            with self.assertRaises(ValueError):safe_scope(source_for('guard_test',body))
        source=source_for('bad_fixture',"// @params_file ../../credentials.json\nUNWIND $people AS p CREATE (:@@L@@:Person {name:p.name});")
        with self.assertRaisesRegex(ValueError,'Only the supplied'):run_script(source)
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_25_english_safe_html_sources_all_links_and_answered_tasks(self):
        def english(obj):
            if isinstance(obj,dict):
                self.assertNotIn('gu',obj);self.assertNotIn('key',obj)
                for value in obj.values():english(value)
            elif isinstance(obj,list):
                for value in obj:english(value)
            elif isinstance(obj,str):self.assertIsNone(re.search(r'[\u0a80-\u0aff]',obj))
        english(self.u);self.assertEqual(self.s['languages'],['en']);self.assertEqual(self.s['code_lang'],'nosql')
        linked=set()
        for group in self.u['notes']:
            for item in group['items']:
                Fragment().finish(item['body']['en']);self.assertNotIn('@@',item['body']['en'])
                linked.update(item.get('programs',[]))
        self.assertEqual(linked,set(self.by_id))
        for p in self.u['programs']:Fragment().finish(p['expl']['en'])
        for group in self.u['viva']:
            for item in group['items']:Fragment().finish(item['a']['en'])
        self.assertEqual(len(self.u['sources']),len(SOURCES))
        for q,item in zip(PRACTICE_QS,self.u['notes'][-1]['items']):
            self.assertEqual((q['q'],q['a']),(item['h'],item['body']));self.assertNotIn('marks',q)

    def test_26_svg_integrity_rasterization_and_contact_sheets(self):
        self.assertEqual({d['id'] for d in self.u['diagrams']},set(TITLES))
        self.assertEqual({i['diagram'] for g in self.u['notes'] for i in g['items'] if 'diagram' in i},set(TITLES))
        folder=ROOT/'preview/nosql_u4_checks';folder.mkdir(exist_ok=True);images=[]
        for d in self.u['diagrams']:
            file=SUBJ_DIR/d['file'];raw=file.read_text();root=ET.fromstring(raw)
            self.assertEqual(root.get('viewBox').split()[2],'360')
            for bad in ('<marker','<image','<foreignObject','<script','<style','href=','url('):self.assertNotIn(bad,raw)
            image=Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_path=str(file),zoom=1.4,
                font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',
                sans_serif_family='DejaVu Sans',skip_system_fonts=True)))).convert('RGB')
            self.assertGreater(image.height,400);image.save(folder/(d['id']+'.png'));images.append((d['id'],image))
        for batch,label in [(images[:4],'a'),(images[4:8],'b'),(images[8:],'c')]:
            w,h=530,790;sheet=Image.new('RGB',(w*2,h*((len(batch)+1)//2)),'#EAE4F1');draw=ImageDraw.Draw(sheet)
            for i,(id_,image) in enumerate(batch):
                x=i%2*w+12;y=i//2*h+29;self.assertLessEqual(image.height+29,h)
                draw.text((x,y-22),id_,fill='#4C1C85');sheet.paste(image,(x,y))
            sheet.save(ROOT/f'preview/DI04000031_unit4_diagrams_{label}.png')

    def test_27_svg_text_viewport_bounds(self):
        for id_ in TITLES:
            root=ET.parse(DIAG_DIR/(id_+'.svg')).getroot();_,_,width,height=map(float,root.get('viewBox').split())
            for node in root.iter('{http://www.w3.org/2000/svg}text'):
                size=float(node.get('font-size','12'))
                file='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
                font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+file,round(size*10))
                text_width=font.getlength(''.join(node.itertext()))/10;x=float(node.get('x'));y=float(node.get('y'))
                anchor=node.get('text-anchor','start');left=x-text_width/2 if anchor=='middle' else x-text_width if anchor=='end' else x
                self.assertGreaterEqual(left,1,(id_,node.text,left));self.assertLessEqual(left+text_width,width-1,(id_,node.text,left+text_width))
                self.assertGreater(y-size,-1);self.assertLess(y+size/3,height+1)

    def test_28_complete_scoped_source_readability_and_real_negative_codes(self):
        for p in self.u['programs']:
            scope,claim,parsed=safe_scope(p['code']['en'])
            self.assertNotIn('@@',p['code']['en'])
            self.assertEqual(parsed[-2]['sql'],'MATCH (n:'+scope+') DETACH DELETE n')
            self.assertEqual(parsed[-1]['sql'],'DROP CONSTRAINT '+claim)
            self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])
        codes=[s['expect'] for p in self.u['programs'] for s in statements(p['code']['en']) if 'expect' in s]
        self.assertEqual(len(codes),6)
        self.assertEqual(codes.count('Neo.ClientError.Schema.ConstraintValidationFailed'),2)
        self.assertEqual(codes.count('Neo.ClientError.Statement.SyntaxError'),2)

    def test_29_zip_exact_37_files_sources_outputs_fixture_runtime(self):
        with zipfile.ZipFile(ZIP_PATH) as z:
            self.assertEqual(len(z.namelist()),37)
            self.assertEqual(z.read('run_lab.py'),(ROOT/'tools/neo4j_lab_runner.py').read_bytes())
            self.assertEqual(z.read('requirements.txt').decode(),REQUIREMENTS)
            self.assertEqual(z.read('graph_fixture.json').decode(),FIXTURE_JSON)
            self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
            for p in self.u['programs']:
                self.assertEqual(z.read('examples/'+p['id']+'.cypher').decode(),p['code']['en']+'\n')
                self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out']+'\n')
            self.assertEqual(hashlib.sha256(z.read('graph_fixture.json')).hexdigest(),self.u['runtime_evidence']['fixture']['sha256'])

    def test_30_public_zip_runner_reexecutes_all_sixteen_exact_scripts(self):
        private=credentials();env=os.environ.copy();env.update({'NEO4J_URI':URI,
            'NEO4J_USERNAME':private['username'],'NEO4J_PASSWORD':private['password'],'NEO4J_DATABASE':DATABASE})
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ZIP_PATH) as z:z.extractall(tmp)
            for p in self.u['programs']:
                result=subprocess.run([sys.executable,'run_lab.py','examples/'+p['id']+'.cypher'],
                    cwd=tmp,env=env,text=True,capture_output=True,timeout=60)
                self.assertEqual(result.returncode,0,(p['id'],result.stderr))
                self.assertEqual(result.stdout.rstrip('\n'),p['out'],p['id']);self.assertEqual(result.stderr,'',p['id'])
        self.assertEqual(scratch_artifacts(),EMPTY)

    def test_31_preview_five_views_diagram_heading_and_neutral_code(self):
        result=execute_preview(PREVIEW)
        self.assertEqual(set(result['views']),{'notes','programs','diagrams','syntax','viva'})
        self.assertEqual(result['languageHidden'],'none');self.assertEqual(result['neutral'],'a &lt; b &amp;&amp; c &gt; d')
        self.assertIn('<span>Diagrams</span>',result['views']['diagrams'])
        self.assertNotIn('<span>Flowcharts</span>',result['views']['diagrams'])
        self.assertEqual(result['views']['diagrams'].count('class="dcard"'),14)
        self.assertIn(self.u['intro_text']['en'],result['views']['notes'])
        self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')
        for p in self.u['programs']:self.assertIn(p['title']['en'],result['views']['programs'])

    def test_32_export_catalog_app_svgs_and_prior_published_units_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=subprocess.run([sys.executable,'tools/export_app_content.py','--out',tmp],cwd=ROOT,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            subject=json.loads(Path(tmp,'subjects/DI04000031.json').read_text())
            unit=json.loads(Path(tmp,'units/DI04000031_u4.json').read_text())
            catalog=json.loads(Path(tmp,'catalog.json').read_text())
            self.assertEqual(subject['available_units'],[1,2,3,4]);self.assertEqual(len(subject['units']),5)
            self.assertEqual(unit['programs'],self.u['programs']);self.assertEqual(set(unit['svgs']),set(TITLES))
            for d in self.u['diagrams']:
                self.assertEqual(unit['svgs'][d['id']],clean_svg((SUBJ_DIR/d['file']).read_text()))
            for rel in ['subjects/DI04000031.json']+[f'units/DI04000031_u{n}.json' for n in (1,2,3,4)]:
                self.assertEqual(catalog['files'][rel],hashlib.sha1(Path(tmp,rel).read_bytes()).hexdigest()[:12])
            for n in (1,2,3):
                self.assertEqual(hashlib.sha256((SUBJ_DIR/f'unit{n}.json').read_bytes()).hexdigest(),PRIOR_SOURCE_SHA[n])
                self.assertEqual(hashlib.sha256(Path(tmp,f'units/DI04000031_u{n}.json').read_bytes()).hexdigest(),PRIOR_PUBLIC_SHA[n])
            self.assertFalse(Path(tmp,'units/DI04000031_u5.json').exists())

    def test_33_deterministic_rebuild_json_svg_preview_and_zip(self):
        files=[SUBJ_DIR/'unit4.json',SUBJ_DIR/'subject.json',PREVIEW,Path(ZIP_PATH)]
        files+=[DIAG_DIR/(id_+'.svg') for id_ in TITLES]
        before={str(p):p.read_bytes() for p in files}
        result=subprocess.run([sys.executable,'tools/build_DI04000031_u4.py'],cwd=ROOT,text=True,capture_output=True,timeout=90)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(before,{str(p):p.read_bytes() for p in files})

    def test_34_zip_export_is_database_and_network_independent(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp,'offline.zip')
            script="""import socket,sys
sys.path.insert(0,'tools')
def blocked(*args,**kwargs):raise AssertionError('Network is forbidden during archive export')
socket.socket.connect=blocked
sys.modules['neo4j']=None
from export_DI04000031_u4_practicals import export
export(sys.argv[1])
"""
            result=subprocess.run([sys.executable,'-c',script,str(path)],cwd=ROOT,text=True,capture_output=True,timeout=20)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertEqual(path.read_bytes(),Path(ZIP_PATH).read_bytes())

    def test_35_no_private_secrets_or_runtime_data_in_deliverables(self):
        secret=credentials()['password'].encode()
        blobs=[PREVIEW.read_bytes(),(SUBJ_DIR/'unit4.json').read_bytes(),(SUBJ_DIR/'subject.json').read_bytes()]
        with zipfile.ZipFile(ZIP_PATH) as z:
            self.assertFalse(any('credential' in n or n.endswith('.db') for n in z.namelist()))
            blobs += [z.read(name) for name in z.namelist()]
        self.assertFalse(any(secret in data for data in blobs),'Unexpected private credential in a deliverable')
        self.assertFalse(CREDENTIALS.is_relative_to(ROOT));self.assertEqual(CREDENTIALS.stat().st_mode & 0o777,0o600)
        self.assertFalse((ROOT/'.cache/diplomaone-neo4j-u4').exists())
        self.assertFalse(any(re.search(rb'(?:neo4j|bolt)(?:\+s)?://[^\s/]+:[^\s/]+@',data) for data in blobs))

    def test_36_scope_gui_ai_algorithm_company_boundaries_and_cleanup(self):
        evidence=self.u['runtime_evidence']
        self.assertEqual(evidence['physical_instances'],1);self.assertEqual(evidence['programs_executed'],16)
        for key in ('desktop_installed','aura_provisioned','browser_ui_automated','public_database_endpoint',
                    'graph_algorithm_library_installed','graph_algorithms_implemented','model_trained',
                    'company_deployments_verified','cluster_failover_tested','performance_benchmarked'):
            self.assertFalse(evidence[key],key)
        for p in self.u['programs']:
            for forbidden in ('gds.','apoc.','CREATE DATABASE','DROP DATABASE','MATCH (n) DETACH DELETE n'):
                self.assertNotIn(forbidden,p['code']['en'])
        notes=' '.join(i['body']['en'] for g in self.u['notes'] for i in g['items']).lower()
        notes=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',notes))
        for phrase in ('not verified claims','not a fraud verdict','not implementations','not one atomic transaction'):
            self.assertIn(phrase,notes)
        self.assertEqual(scratch_artifacts(),EMPTY)


if __name__=='__main__':unittest.main(verbosity=2)
