"""24 validation groups for the concise Redis unit; all DB tests are real."""
import copy,hashlib,io,json,os,re,subprocess,sys,tempfile,time,unittest,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
import redis,resvg_py
from PIL import Image,ImageDraw,ImageFont
from subject_DI04000031 import ROOT,SUBJ_DIR,DIAG_DIR
from redis_content import assert_runtime,client,cli,env,private,remaining,run_program,CREDS
from redis_lab_runner import Lab
from diagrams_DI04000031_u5 import TITLES
from test_DI04000031_u1 import Fragment,execute_preview
from export_app_content import clean_svg
ROOT=Path(ROOT);SUBJ_DIR=Path(SUBJ_DIR);DIAG_DIR=Path(DIAG_DIR)
PREVIEW=ROOT/'preview/DI04000031_unit5_preview.html';ZIP=ROOT/'preview/DI04000031_unit5_practicals.zip'
PRIOR_PUBLIC={1:'9dad2b0c9a9122cc31ca1cccb5d92013cd92ca4a142418be86b7d57589624df2',
 2:'eeeb83bb993f5a3e91ee46710927519d4c5b0afd9fe8d9c1988ee45da38a8a37',
 3:'19dfcd387ac094233d438ece6c508dcf9496389a6ed9ad305de583cabd39f06e'}
PRIOR_SOURCE={1:'275a0d08e5b134c8ad8cfd19084130020a99c13ac5a90b946854585d37587b5f',
 2:'a7a61cfd843284fc6d2d88262fd03ca8a73ef3cdea9ac97d8f3f9914b16004fe',
 3:'0c24ae5ab9e8f534987d042465e467e026b2187b6138c4ad965fed01537da694'}


def restore_old_status(unit):
    """Only three Unit 4 text leaves change: remove obsolete pending status."""
    unit=copy.deepcopy(unit)
    a='Redis is covered separately in Unit 5; this unit focuses on Neo4j.'
    b='Units 1–3 remain preserved and Unit 5 is a separate pending release.'
    body=unit['notes'][-2]['items'][-1]['body']['en'];assert body.count(a)==1
    unit['notes'][-2]['items'][-1]['body']['en']=body.replace(a,b)
    last=unit['viva'][-1]['items'][-1]
    assert last['q']['en']=='What is the official assessment and which unit covers Redis?'
    last['q']['en']='What is the official assessment and what remains pending?'
    a='This is the Neo4j unit; Redis is covered separately in Unit 5.'
    b='This release is Unit 4 only; Redis Unit 5 is still a separate pending unit.'
    assert last['a']['en'].count(a)==1;last['a']['en']=last['a']['en'].replace(a,b)
    return unit


class Unit5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u=json.loads((SUBJ_DIR/'unit5.json').read_text())
        cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
        cls.p={p['id']:p for p in cls.u['programs']}
        from content_DI04000031_u5_programs import PROGRAMS
        cls.fresh={p['id']:p for p in PROGRAMS}

    def value(self,n,label):
        return json.loads(next(s[len(label)+2:] for s in self.p[f'ns5p{n:02d}']['out'].splitlines() if s.startswith(label+': ')))

    def test_01_actual_server_cli_and_client(self):
        r=assert_runtime();self.assertEqual((r['server_version'],r['cli_version'],r['driver_version']),('8.10.3','8.10.3','8.1.0'))
        self.assertTrue(r['authenticated']);self.assertFalse(r['persistence_enabled']);self.assertEqual(cli('PING'),'PONG')

    def test_02_concise_syllabus_coverage_and_full_availability(self):
        u=self.u;self.assertEqual((u['hours'],u['weightage'],u['practical_numbers']),(10,17,[9]))
        self.assertEqual(u['content_density'],'concise');self.assertEqual(u['exam_questions'],[])
        self.assertEqual(sum(len(g['items']) for g in u['notes']),13)
        self.assertEqual((len(u['programs']),len(u['diagrams'])),(8,4))
        self.assertEqual(sum(len(g['items']) for g in u['syntax']),8)
        self.assertEqual(sum(len(g['items']) for g in u['viva']),12)
        self.assertLess(len(json.dumps(u)),45000)
        self.assertEqual([g['file'] for g in self.s['units']],[f'unit{n}.json' for n in range(1,6)])
        self.assertEqual(self.s['exam']['theory_ese'],0);self.assertEqual(self.s['exam']['total'],50)

    def test_03_all_current_eight_real_outputs_match(self):
        self.assertEqual(self.p,self.fresh);self.assertEqual(remaining(),[])
        for p in self.u['programs']:
            compile(p['code']['en'],p['id'],'exec')
            self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78)

    def test_04_basic_stored_key_operations(self):
        self.assertIs(self.value(1,'ping'),True);self.assertIs(self.value(1,'set'),True)
        self.assertEqual(self.value(1,'get'),'Sensor Node');self.assertEqual(self.value(1,'type'),'string')
        self.assertEqual(self.value(1,'exists'),1);self.assertEqual(self.value(1,'deleted'),1);self.assertIsNone(self.value(1,'missing'))

    def test_05_string_counter_and_immediate_expiry(self):
        self.assertEqual(self.value(2,'incremented'),11);self.assertEqual(self.value(2,'stored_string'),'11')
        self.assertTrue(self.value(2,'ttl_active'));self.assertIsNone(self.value(2,'after_immediate_expiry'))
        self.assertEqual(self.value(2,'missing_ttl'),-2)

    def test_06_list_order_and_pop(self):
        self.assertEqual(self.value(3,'jobs'),['load','train','evaluate']);self.assertEqual(self.value(3,'removed_left'),'load')
        self.assertEqual(self.value(3,'remaining'),['train','evaluate']);self.assertEqual(self.value(3,'length'),2)

    def test_07_set_uniqueness_membership_and_removal(self):
        self.assertEqual(self.value(4,'added'),2);self.assertEqual(self.value(4,'members'),['Python','Redis'])
        self.assertEqual(self.value(4,'has_python'),1);self.assertEqual(self.value(4,'removed'),1)
        self.assertEqual(self.value(4,'remaining'),['Python'])

    def test_08_hash_fields_and_string_age(self):
        self.assertEqual(self.value(5,'new_fields'),3);self.assertEqual(self.value(5,'name'),'Asha')
        self.assertEqual(self.value(5,'profile'),{'age':'20','city':'Surat','name':'Asha'})
        self.assertEqual(self.value(5,'removed_age'),1);self.assertEqual(self.value(5,'remaining'),{'city':'Surat','name':'Asha'})

    def test_09_real_transactions_do_not_roll_back_runtime_errors(self):
        self.assertEqual(self.value(6,'exec'),[11,'11'])
        self.assertEqual(self.value(6,'exec_with_error'),[{'server_error':'value is not an integer or out of range'},True])
        self.assertEqual(self.value(6,'later_write'),'done')

    def test_10_recommendation_cache_hit_miss_invalidation(self):
        self.assertIsNone(self.value(7,'initial_miss'));self.assertEqual(self.value(7,'cache_hit'),'P101,P102')
        self.assertTrue(self.value(7,'ttl_active'));self.assertIsNone(self.value(7,'after_invalidation'))

    def test_11_python_cache_aside_uses_real_redis_and_local_source(self):
        self.assertEqual(self.value(8,'first'),{'from':'source','value':'Sensor Node'})
        self.assertEqual(self.value(8,'second'),{'from':'cache','value':'Sensor Node'})
        self.assertEqual(self.value(8,'after_update'),{'from':'source','value':'Sensor Node v2'})
        for field in ('ai_model_trained','live_multi_database_integration','performance_benchmark','public_database_endpoint'):
            self.assertFalse(self.u['runtime_evidence'][field])

    def test_12_real_time_expiry_and_wrong_type(self):
        with client() as r,Lab('expiry_test',['temporary','text'],connection=r) as lab:
            key=lab.key('temporary');r.set(key,'short',ex=1);time.sleep(1.2)
            self.assertIsNone(r.get(key));self.assertEqual(r.ttl(key),-2)
            key=lab.key('text');r.set(key,'not a list')
            with self.assertRaises(redis.exceptions.ResponseError) as error:r.lpush(key,'x')
            self.assertIn('WRONGTYPE',str(error.exception))
        self.assertEqual(remaining(),[])

    def test_13_real_cli_four_types_exec_and_discard(self):
        with client() as r,Lab('cli_test',['string','list','set','hash'],connection=r) as lab:
            a,b,c,d=[lab.key(n) for n in ('string','list','set','hash')]
            output=cli(f'SET {a} 1\nGET {a}\nRPUSH {b} x y\nLRANGE {b} 0 -1\nSADD {c} x x\nHSET {d} name Asha\nHGET {d} name\nMULTI\nINCR {a}\nGET {a}\nEXEC\nMULTI\nSET {a} 99\nDISCARD\nGET {a}')
            self.assertEqual(output.splitlines(),['OK','1','2','x','y','1','1','Asha','OK','QUEUED','QUEUED','2','2','OK','QUEUED','OK','2'])
        self.assertEqual(remaining(),[])

    def test_14_anonymous_wrong_password_and_forbidden_commands_denied(self):
        for args in ({},{'username':'u5_lab','password':'not-the-private-password'}):
            with redis.Redis(host='127.0.0.1',port=6385,protocol=2,**args) as r:
                with self.assertRaises(redis.exceptions.AuthenticationError):r.ping()
        with client() as r:
            with self.assertRaises(redis.exceptions.NoPermissionError):r.execute_command('FLUSHDB')
            with self.assertRaises(redis.exceptions.NoPermissionError):r.set('outside_course_scope','x')
            self.assertTrue(r.ping())

    def test_15_existing_scope_and_real_set_nx_race_preserve_foreign_claim(self):
        with client() as r:
            lab=Lab('collision_test',['value'],connection=r,suffix='fixed')
            r.set(lab.key('value'),'preserve')
            try:
                with self.assertRaisesRegex(RuntimeError,'Existing scope'):lab.__enter__()
                self.assertEqual(r.get(lab.key('value')),'preserve')
            finally:r.delete(lab.key('value'),lab.owner)
            class Interleave:
                def __getattr__(self,name):return getattr(r,name)
                def set(self,key,value,**kwargs):
                    r.set(key,'other-creator',nx=True)
                    return r.set(key,value,**kwargs)
            lab=Lab('race_test',['value'],connection=Interleave(),suffix='fixed')
            try:
                with self.assertRaisesRegex(RuntimeError,'claim failed'):lab.__enter__()
                self.assertEqual(r.get(lab.owner),'other-creator');self.assertFalse(lab.owned)
            finally:r.delete(lab.owner)
        self.assertEqual(remaining(),[])

    def test_16_failure_cleanup_and_changed_owner_is_not_deleted(self):
        with client() as r:
            lab=Lab('failure_test',['value'],connection=r)
            with self.assertRaisesRegex(ValueError,'deliberate'):
                with lab:r.set(lab.key('value'),'ours');raise ValueError('deliberate')
            self.assertEqual(r.exists(lab.owner,lab.key('value')),0)
            lab=Lab('owner_changed',['value'],connection=r)
            try:
                with self.assertRaisesRegex(RuntimeError,'ownership changed'):
                    with lab:r.set(lab.key('value'),'preserve');r.set(lab.owner,'different')
                self.assertEqual(r.get(lab.key('value')),'preserve')
            finally:r.delete(lab.owner,lab.key('value'))
        self.assertEqual(remaining(),[])

    def test_17_english_safe_html_linked_topics_and_no_theory_paper(self):
        def walk(obj):
            if isinstance(obj,dict):
                self.assertNotIn('gu',obj);self.assertNotIn('key',obj)
                for value in obj.values():walk(value)
            elif isinstance(obj,list):
                for value in obj:walk(value)
            elif isinstance(obj,str):self.assertNotRegex(obj,r'[\u0a80-\u0aff]')
        walk(self.u);linked=set();diagrams=set()
        for group in self.u['notes']:
            for item in group['items']:
                Fragment().finish(item['body']['en']);self.assertNotIn('@@',item['body']['en'])
                linked.update(item.get('programs',[]))
                if item.get('diagram'):diagrams.add(item['diagram'])
        self.assertEqual(linked,set(self.p));self.assertEqual(diagrams,set(TITLES))
        for p in self.u['programs']:Fragment().finish(p['expl']['en'])
        self.assertEqual(self.u['exam_questions'],[])

    def test_18_four_self_contained_svgs_rasterize_and_fit(self):
        images=[]
        for d in self.u['diagrams']:
            path=SUBJ_DIR/d['file'];raw=path.read_text();root=ET.fromstring(raw)
            self.assertEqual(root.get('viewBox').split()[2],'360')
            for bad in ('<script','<style','<marker','<foreignObject','<image','href='):self.assertNotIn(bad,raw)
            width,height=map(float,root.get('viewBox').split()[2:])
            for node in root.iter('{http://www.w3.org/2000/svg}text'):
                size=float(node.get('font-size','12'));name='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
                font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name,round(size*10))
                length=font.getlength(''.join(node.itertext()))/10;x=float(node.get('x'));y=float(node.get('y'))
                anchor=node.get('text-anchor','start');left=x-length/2 if anchor=='middle' else x-length if anchor=='end' else x
                self.assertGreaterEqual(left,1,(d['id'],node.text));self.assertLessEqual(left+length,width-1,(d['id'],node.text))
                self.assertLess(y+size/3,height+1)
            png=resvg_py.svg_to_bytes(svg_string=clean_svg(raw),zoom=1.4,font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',sans_serif_family='DejaVu Sans',skip_system_fonts=True)
            image=Image.open(io.BytesIO(bytes(png))).convert('RGB');images.append((d['id'],image))
        sheet=Image.new('RGB',(1060,1480),'#EAE4F1');draw=ImageDraw.Draw(sheet)
        for i,(name,image) in enumerate(images):
            x=i%2*530+12;y=i//2*740+29;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(image,(x,y))
        sheet.save(ROOT/'preview/DI04000031_unit5_diagrams.png')

    def test_19_five_preview_views_and_neutral_query_rendering(self):
        result=execute_preview(PREVIEW)
        self.assertEqual(set(result['views']),{'notes','programs','diagrams','syntax','viva'})
        self.assertEqual(result['languageHidden'],'none');self.assertEqual(result['neutral'],'a &lt; b &amp;&amp; c &gt; d')
        self.assertEqual(result['views']['diagrams'].count('class="dcard"'),4)
        self.assertIn(self.u['intro_text']['en'],result['views']['notes'])
        self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

    def test_20_zip_exact_twenty_files_and_all_eight_public_reruns(self):
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ZIP) as z:
                self.assertEqual(len(z.namelist()),20);z.extractall(tmp)
                self.assertEqual(z.read('lab.py'),(ROOT/'tools/redis_lab_runner.py').read_bytes())
                self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
                for p in self.u['programs']:
                    self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en']+'\n')
                    self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out']+'\n')
            for p in self.u['programs']:
                result=subprocess.run([sys.executable,p['id']+'.py'],cwd=tmp,env=env(),text=True,capture_output=True,timeout=20)
                self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(result.stderr,'')
                self.assertEqual(result.stdout.rstrip('\n'),p['out'])
        self.assertEqual(remaining(),[])

    def test_21_export_full_subject_hashes_and_prior_content_only_status_tidy(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=subprocess.run([sys.executable,'tools/export_app_content.py','--out',tmp],cwd=ROOT,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            catalog=json.loads(Path(tmp,'catalog.json').read_text());subject=json.loads(Path(tmp,'subjects/DI04000031.json').read_text())
            self.assertEqual(subject['available_units'],[1,2,3,4,5])
            for n in range(1,6):
                path=Path(tmp,f'units/DI04000031_u{n}.json')
                self.assertEqual(catalog['files'][f'units/DI04000031_u{n}.json'],hashlib.sha1(path.read_bytes()).hexdigest()[:12])
                if n<4:
                    self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),PRIOR_PUBLIC[n])
                    self.assertEqual(hashlib.sha256((SUBJ_DIR/f'unit{n}.json').read_bytes()).hexdigest(),PRIOR_SOURCE[n])
            u4=restore_old_status(json.loads(Path(tmp,'units/DI04000031_u4.json').read_text()))
            self.assertEqual(hashlib.sha256(json.dumps(u4,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'1ab4d2deefc6927c030a897aa6fdd420daa291640e9c906e051f5fca9991f814')
            u4=restore_old_status(json.loads((SUBJ_DIR/'unit4.json').read_text()))
            self.assertEqual(hashlib.sha256(json.dumps(u4,ensure_ascii=False,indent=1).encode()).hexdigest(),'b9cb9fb110c8e60050f5da80f6370066b96f7719f1ee243969e7fce9b7dff7a7')
            u5=json.loads(Path(tmp,'units/DI04000031_u5.json').read_text())
            self.assertEqual(u5['programs'],self.u['programs']);self.assertEqual(len(u5['svgs']),4)
            for d in self.u['diagrams']:self.assertEqual(u5['svgs'][d['id']],clean_svg((SUBJ_DIR/d['file']).read_text()))

    def test_22_deterministic_rebuild(self):
        paths=[SUBJ_DIR/'unit5.json',SUBJ_DIR/'subject.json',PREVIEW,ZIP]+[DIAG_DIR/(d+'.svg') for d in TITLES]
        before={str(p):p.read_bytes() for p in paths}
        result=subprocess.run([sys.executable,'tools/build_DI04000031_u5.py'],cwd=ROOT,text=True,capture_output=True,timeout=45)
        self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(before,{str(p):p.read_bytes() for p in paths})

    def test_23_archive_export_is_network_database_independent(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp,'offline.zip')
            code="""import socket,sys
sys.path.insert(0,'tools')
def blocked(*a,**k):raise AssertionError('Network forbidden')
socket.socket.connect=blocked
sys.modules['redis']=None
from export_DI04000031_u5_practicals import export
export(sys.argv[1])
"""
            result=subprocess.run([sys.executable,'-c',code,str(path)],cwd=ROOT,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(path.read_bytes(),ZIP.read_bytes())

    def test_24_no_secrets_in_deliverables_and_final_scoped_cleanup(self):
        blobs=[PREVIEW.read_bytes(),(SUBJ_DIR/'unit5.json').read_bytes()]
        with zipfile.ZipFile(ZIP) as z:blobs.extend(z.read(n) for n in z.namelist())
        for secret in private().values():self.assertFalse(any(secret.encode() in data for data in blobs))
        self.assertEqual(CREDS.stat().st_mode & 0o777,0o600);self.assertFalse(CREDS.is_relative_to(ROOT))
        self.assertEqual(remaining(),[])


if __name__=='__main__':unittest.main(verbosity=2)
