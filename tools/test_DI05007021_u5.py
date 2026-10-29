"""36 groups: safe defence, actual local I/O/signed metadata, preservation and UI."""
import ast,contextlib,csv,hashlib,html,io,json,math,os,re,shutil,socket,sqlite3,ssl,subprocess,sys,tempfile,threading,unittest,zipfile
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
import infosec_u3_lab
sys.modules.setdefault('pki_lab',infosec_u3_lab)
import infosec_u4_localnet as localnet
import infosec_u5_defence as defence
from infosec_u5_manifest import verify_manifest,PRIMARY,INSTALLER
from subject_DI05007021 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007021_u5_programs import EXAMPLES,execute_all,HELPERS,FIXTURES
from content_DI05007021_u5_notes import NOTES,PRACTICE
from content_DI05007021_u5_guides import GUIDES,CASES
from diagrams_DI05007021_u5 import TITLES
from export_app_content import clean_svg
from export_DI05007021_u5_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007021_unit5_preview.html';ZIP=ROOT/'preview/DI05007021_unit5_practicals.zip'
BASE=Path('/opt/repos/diplomaone-content/data')

def execute_in_process(example):
 namespace={};out=io.StringIO()
 with contextlib.redirect_stdout(out):exec(compile(example['code']['en'],example['id'],'exec'),namespace)
 return namespace,out.getvalue()

class Unit5Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit5.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.text=' '.join(strings(cls.u)).lower();cls.plain=html.unescape(re.sub(r'<[^>]*>','',cls.text))
  cls.system={p:p.read_bytes() for p in [Path('/etc/ssl/openssl.cnf'),Path('/etc/ssl/certs/ca-certificates.crt')] if p.is_file()}
  cls.addresses=subprocess.run(['ip','-j','address'],check=True,capture_output=True).stdout
  cls.routes=subprocess.run(['ip','-j','route'],check=True,capture_output=True).stdout

 def test_01_official_final_unit_and_study_practicals(self):
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage'],self.u['practical_numbers']),(5,8,15,[11,12]))
  self.assertIn('CO5',self.u['learning_outcomes'][0]['en'])
  self.assertEqual(self.s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})
  self.assertEqual((self.s['semester'],self.s['syllabus_year']),(5,'2026-27'))

 def test_02_all_five_units_and_complete_syllabus_totals(self):
  self.assertEqual([x['file'] for x in self.s['units']],[f'unit{i}.json' for i in range(1,6)])
  self.assertEqual(sum(x['hours'] for x in self.s['units']),45);self.assertEqual(sum(x['weightage'] for x in self.s['units']),100)
  self.assertEqual(sorted(p.name for p in SUBJ_DIR.glob('unit*.json')),[f'unit{i}.json' for i in range(1,6)])
  self.assertEqual(len(self.s['practicals']),12);self.assertEqual(self.u['tabs'],TABS)

 def test_03_english_only_no_priority_flags(self):
  def walk(o):
   if isinstance(o,dict):
    self.assertNotIn('gu',o);self.assertNotIn('key',o)
    for v in o.values():walk(v)
   elif isinstance(o,list):
    for v in o:walk(v)
   elif isinstance(o,str):self.assertNotRegex(o,r'[\u0a80-\u0aff]')
  walk(self.u);walk(self.s);self.assertEqual(self.s['languages'],['en'])

 def test_04_all_named_threats_crimes_and_counts(self):
  self.assertEqual(sum(len(g['items']) for g in NOTES),16);self.assertEqual(sum(len(g['items']) for g in self.u['notes']),32)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams']),len(self.u['exam_questions'])),(10,8,16))
  self.assertEqual(sum(len(g['items']) for g in self.u['syntax']),12);self.assertEqual(sum(len(g['items']) for g in self.u['viva']),32)
  for term in ['threat','vulnerability','intruder','hacker','worm','virus','adware','spyware','trojan','dos','ddos','mitm','ip spoofing','arp spoofing','sql injection','phishing','botnet','backdoor','cyberspace','identity theft','information theft','hacking','cyberstalking','malware distribution']:
   self.assertTrue(term in self.plain,term)

 def test_05_correct_distinctions_and_nonproof_boundaries(self):
  for term in ['not mutually exclusive','not itself a legal finding','not proof of poisoning','not a url-reputation service','not an offline/immutable backup','not a digest computed from an iso we possess']:
   self.assertTrue(term in self.plain,term)
  self.assertTrue('not automatically criminal' in self.plain)
  self.assertTrue('one-time passcode' in self.plain)

 def test_06_actual_parameterized_sql_values_remain_literal_and_connection_closes(self):
  n,out=execute_in_process(self.p['sec5p01']);self.assertEqual(out,self.p['sec5p01']['out'])
  self.assertEqual(n['normal'],[('Networks',)]);self.assertEqual(n['literal'],[]);self.assertEqual(n['count'],2)
  with self.assertRaises(sqlite3.ProgrammingError):n['db'].execute('SELECT 1')
  with contextlib.closing(sqlite3.connect(':memory:')) as db:
   db.execute('CREATE TABLE sample(value TEXT)');db.execute('INSERT INTO sample VALUES (?)',("' OR 1=1 --",))
   self.assertEqual(db.execute('SELECT value FROM sample WHERE value=?',("' OR 1=1 --",)).fetchone()[0],"' OR 1=1 --")

 def test_07_actual_read_authorizer_denies_delete_update_insert_drop(self):
  n,out=execute_in_process(self.p['sec5p02']);self.assertEqual(out,self.p['sec5p02']['out']);self.assertTrue(n['denied'])
  with self.assertRaises(sqlite3.ProgrammingError):n['db'].execute('SELECT 1')
  with contextlib.closing(sqlite3.connect(':memory:')) as db:
   db.execute('CREATE TABLE courses(code TEXT)');db.execute('INSERT INTO courses VALUES (?)',('C01',));db.commit()
   db.set_authorizer(n['authorize'])
   for statement in ['DELETE FROM courses',"UPDATE courses SET code='C02'","INSERT INTO courses VALUES ('C03')",'DROP TABLE courses']:
    with self.assertRaises(sqlite3.DatabaseError) as caught:db.execute(statement)
    self.assertEqual(caught.exception.sqlite_errorcode,sqlite3.SQLITE_AUTH)
   self.assertEqual(db.execute('SELECT code FROM courses').fetchall(),[('C01',)])

 def test_08_actual_url_parsing_prefix_userinfo_and_no_authenticity_verdict(self):
  good=defence.url_signals('https://college.example.test/portal')
  self.assertTrue(good['exact_expected_host']);self.assertTrue(good['https_scheme']);self.assertFalse(good['authenticity_proven'])
  bad=defence.url_signals('https://college.example.test@notice.attacker.test/portal')
  self.assertTrue(bad['userinfo_present']);self.assertFalse(bad['exact_expected_host']);self.assertEqual(bad['hostname'],'notice.attacker.test')
  self.assertFalse(defence.url_signals('https://college.example.test.attacker.test/portal')['exact_expected_host'])
  self.assertFalse(defence.url_signals('http://college.example.test/')['https_scheme'])
  self.assertFalse(defence.url_signals('https://college.example.test:8443/')['expected_port'])

 def test_09_url_malformed_control_unicode_and_port_cases(self):
  for bad in ['https://college.example.test:bad/','https://college.example.test/\n','https://exámple.test/',b'not text']:
   with self.assertRaises(ValueError):defence.url_signals(bad)
  self.assertTrue(defence.url_signals('HTTPS://COLLEGE.EXAMPLE.TEST:443/')['exact_expected_host'])
  self.assertFalse(defence.url_signals('/relative/')['exact_expected_host'])

 def test_10_email_parser_is_real_but_neither_authentication_nor_delivery(self):
  n,out=execute_in_process(self.p['sec5p06']);self.assertEqual(out,self.p['sec5p06']['out'])
  self.assertEqual(n['sender'].display_name,'Campus Desk');self.assertEqual(n['sender'].domain,'notice.attacker.test')
  self.assertTrue('header_parsing_authenticates_sender: False' in out)
  self.assertTrue('email_sent_or_links_opened: False' in out)

 def test_11_arp_dictionary_comparison_and_legitimate_change_ambiguity(self):
  baseline={'192.0.2.1':'02:00:00:00:00:01'}
  self.assertEqual(defence.arp_changes(baseline,dict(baseline)),[])
  self.assertEqual(defence.arp_changes(baseline,{'192.0.2.1':'02:00:00:00:00:99'}),['192.0.2.1'])
  self.assertEqual(defence.arp_changes(baseline,{}),['192.0.2.1'])
  with self.assertRaises(ValueError):defence.arp_changes(baseline,{'192.0.2.1':'not-mac'})
  self.assertTrue('legitimate replacement/failover' in self.plain)

 def test_12_synthetic_limiter_sequence_capacity_and_bad_clock(self):
  model=defence.TokenBucket(2,1)
  self.assertEqual([model.allow(t) for t in [0,0,0,1,1,2]],[True,True,False,True,False,True])
  self.assertLessEqual(model.tokens,2);self.assertGreaterEqual(model.tokens,0)
  for bad in [float('nan'),float('inf'),-1,1,True]:
   with self.assertRaises(ValueError):model.allow(bad)
  for cap,refill in [(0,1),(1,0),(float('inf'),1),(True,1)]:
   with self.assertRaises(ValueError):defence.TokenBucket(cap,refill)

 def test_13_real_benign_file_hashes_not_malware_execution(self):
  n,out=execute_in_process(self.p['sec5p07']);self.assertEqual(out,self.p['sec5p07']['out'])
  self.assertFalse(n['path'].exists());self.assertFalse(Path(n['folder']).exists())
  self.assertIn('original_digest_matches: True',out);self.assertIn('changed_digest_matches: False',out)
  self.assertIn('malware_scanner_or_payload_executed: False',out)

 def test_14_real_single_file_restore_is_not_full_resilience(self):
  n,out=execute_in_process(self.p['sec5p09']);self.assertEqual(out,self.p['sec5p09']['out'])
  self.assertFalse(n['current'].exists());self.assertFalse(n['backup'].exists())
  self.assertIn('restored_digest_matches: True',out)
  self.assertIn('ransomware_or_offline_backup_system_tested: False',out)

 def test_15_real_owned_tls_positive_negative_hostname_and_cleanup(self):
  before=set(threading.enumerate());temps=set(Path('/tmp').glob('infosec-u3-*'))
  valid=localnet.private_tls_relay();self.assertEqual(valid['tls_version'],'TLSv1.3');self.assertTrue(valid['echo_matches'])
  with patch('infosec_u4_localnet.HOST','wrong.diploma.test'):
   with self.assertRaises(ssl.SSLCertVerificationError):localnet.private_tls_relay()
  self.assertEqual(set(threading.enumerate()),before);self.assertEqual(set(Path('/tmp').glob('infosec-u3-*')),temps)

 def test_16_frozen_public_metadata_files_exact_hashes_no_image(self):
  self.assertEqual(sorted(p.name for p in FIXTURES.iterdir()),['SHA256SUMS','SHA256SUMS.gpg','kali-archive-key.asc','provenance.json'])
  provenance=json.loads((FIXTURES/'provenance.json').read_text())
  for name,wanted in provenance['file_sha256'].items():self.assertEqual(hashlib.sha256((FIXTURES/name).read_bytes()).hexdigest(),wanted)
  self.assertEqual(provenance['primary_fingerprint'],PRIMARY)
  self.assertIn(b'BEGIN PGP PUBLIC KEY BLOCK',(FIXTURES/'kali-archive-key.asc').read_bytes())
  self.assertFalse((FIXTURES/INSTALLER).exists());self.assertLess(sum(p.stat().st_size for p in FIXTURES.iterdir()),25000)

 def test_17_actual_gpg_pinned_signature_and_entry_not_iso_verification(self):
  result=verify_manifest(FIXTURES)
  self.assertEqual(result,self.u['runtime_evidence']['Kali_metadata_result'])
  self.assertTrue(result['signature_valid']);self.assertEqual(result['primary_fingerprint'],PRIMARY)
  self.assertEqual(result['installer_filename'],INSTALLER)
  self.assertEqual(result['published_installer_sha256'],'db9cbed33edb45727d16911813c2434fcd1419585007884153be22a03b30ec2f')
  self.assertFalse(result['ISO_downloaded_or_verified']);self.assertFalse(result['Kali_booted']);self.assertTrue(result['isolated_keyring_removed'])

 def test_18_actual_modified_manifest_and_signature_are_rejected(self):
  for name in ['SHA256SUMS','SHA256SUMS.gpg']:
   with tempfile.TemporaryDirectory() as td:
    copy=Path(td)/'metadata';shutil.copytree(FIXTURES,copy)
    if name=='SHA256SUMS':(copy/name).write_bytes((copy/name).read_bytes()+b'\nmodified training copy\n')
    else:
     data=bytearray((copy/name).read_bytes());data[len(data)//2]^=1;(copy/name).write_bytes(data)
    with self.assertRaises(ValueError):verify_manifest(copy)

 def test_19_wrong_or_malformed_primary_pin_rejected(self):
  with self.assertRaisesRegex(ValueError,'primary pin'):verify_manifest(FIXTURES,'0'*40)
  with self.assertRaisesRegex(ValueError,'40-hex'):verify_manifest(FIXTURES,'BAD')

 def test_20_gpg_explicit_isolation_no_auto_retrieval_and_no_ownertrust_override(self):
  real=subprocess.run;calls=[]
  def record(cmd,*args,**kwargs):
   calls.append(cmd);return real(cmd,*args,**kwargs)
  with patch('subprocess.run',side_effect=record):verify_manifest(FIXTURES)
  for cmd in calls:
   self.assertEqual(cmd[0],'gpg');self.assertIn('--homedir',cmd)
   home=cmd[cmd.index('--homedir')+1];self.assertTrue(home.startswith('/tmp/infosec-u5-gpg-'));self.assertFalse(Path(home).exists())
   for flag in ['--no-options','--no-autostart','--no-auto-key-retrieve']:self.assertIn(flag,cmd)
   self.assertNotIn('--keyserver',cmd);self.assertNotIn('--trust-model',cmd)

 def test_21_status_parser_requires_validsig_and_rejects_bad_status(self):
  shown=subprocess.CompletedProcess([],0,'pub:-:4096:1:demo::::::\nfpr:::::::::'+PRIMARY+':\n','')
  imported=subprocess.CompletedProcess([],0,'','')
  for status in ['[GNUPG:] GOODSIG '+PRIMARY+' demo\n','[GNUPG:] VALIDSIG '+PRIMARY+' 2026-10-20 0 0 4 0 1 10 00 '+PRIMARY+'\n[GNUPG:] BADSIG bad\n']:
   verified=subprocess.CompletedProcess([],0,status,'')
   with patch('subprocess.run',side_effect=[shown,imported,verified]):
    with self.assertRaisesRegex(ValueError,'signature verification failed'):verify_manifest(FIXTURES)

 def test_22_gpg_failure_timeout_and_wrong_pin_remove_temporary_home(self):
  before=set(Path('/tmp').glob('infosec-u5-gpg-*'))
  with patch('subprocess.run',side_effect=subprocess.TimeoutExpired('gpg',15)):
   with self.assertRaises(subprocess.TimeoutExpired):verify_manifest(FIXTURES)
  with self.assertRaises(ValueError):verify_manifest(FIXTURES,'0'*40)
  self.assertEqual(set(Path('/tmp').glob('infosec-u5-gpg-*')),before)

 def test_23_kali_is_study_guidance_only_and_signatures_have_distinct_scope(self):
  e=self.u['runtime_evidence']
  for field in ['Kali_OS_downloaded_installed_or_booted','Kali_tools_executed','ISO_or_VM_image_downloaded','actual_ISO_hash_verified','GPG_user_or_system_keyrings_modified','GPG_automatic_key_retrieval_used']:
   self.assertIs(e[field],False,field)
  self.assertTrue(e['signed_Kali_metadata_verified'])
  self.assertTrue('reference host is debian' in self.plain)
  self.assertTrue('not a current-release' in self.p['sec5p10']['expl']['en'].lower())

 def test_24_all_ten_fresh_real_outputs_and_helper_metadata_hashes(self):
  self.assertEqual(execute_all(),self.u['programs'])
  e=self.u['runtime_evidence'];self.assertEqual({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},e['helper_sha256'])
  self.assertEqual({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(FIXTURES.iterdir()) if p.is_file()},e['metadata_file_sha256'])
  self.assertEqual(sqlite3.sqlite_version,e['sqlite'])
  for p in EXAMPLES:
   compile(p['code']['en'],p['id'],'exec');self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])

 def test_25_safe_html_and_all_linked_topics(self):
  linked=set();diagrams=set()
  for group in self.u['notes']:
   for item in group['items']:
    Fragment().finish(item['body']['en']);linked.update(item.get('programs',[]))
    if item.get('diagram'):diagrams.add(item['diagram'])
    self.assertNotIn('@@',item['body']['en'])
  self.assertEqual(linked,set(self.p));self.assertEqual(diagrams,set(TITLES))
  for p in self.u['programs']:Fragment().finish(p['expl']['en'])
  for group in self.u['syntax']:
   for item in group['items']:Fragment().finish(item['terms']['en'])
  for group in self.u['viva']:
   for item in group['items']:Fragment().finish(item['a']['en'])

 def test_26_eight_svg_bounds_raster_and_review_sheets(self):
  images=[]
  for d in self.u['diagrams']:
   raw=(SUBJ_DIR/d['file']).read_text();root=ET.fromstring(raw);w,h=map(float,root.get('viewBox').split()[2:]);self.assertEqual(w,360)
   for bad in ['<script','<style','<marker','<foreignObject','<image','href=']:self.assertNotIn(bad,raw)
   for node in root.iter('{http://www.w3.org/2000/svg}text'):
    size=float(node.get('font-size','12'));name='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name,round(size*10))
    for piece in list(node) or [node]:
     txt=''.join(piece.itertext());length=font.getlength(txt)/10;x=float(piece.get('x',node.get('x')))
     anchor=piece.get('text-anchor',node.get('text-anchor','start'));left=x-length/2 if anchor=='middle' else x-length if anchor=='end' else x
     self.assertGreaterEqual(left,1,(d['id'],txt));self.assertLessEqual(left+length,w-1,(d['id'],txt))
     y=float(piece.get('y',node.get('y','0')));self.assertGreaterEqual(y-size,-1,(d['id'],txt));self.assertLessEqual(y+size/3,h+1,(d['id'],txt))
   png=resvg_py.svg_to_bytes(svg_string=clean_svg(raw),zoom=1.25,font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',sans_serif_family='DejaVu Sans',skip_system_fonts=True)
   image=Image.open(io.BytesIO(bytes(png))).convert('RGB');self.assertGreater(len(image.getcolors(image.width*image.height)),20);images.append((d['id'],image))
  for start in [0,4]:
   group=images[start:start+4];height=max(im.height for n,im in group)+42
   sheet=Image.new('RGB',(960,height*2+16),'#EAE4F1');draw=ImageDraw.Draw(sheet)
   for i,(name,image) in enumerate(group):
    x=i%2*480+15;y=i//2*height+30;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(image,(x,y))
   sheet.save(ROOT/f'preview/DI05007021_unit5_diagrams_{start//4+1}.png')

 def test_27_six_preview_views_true_explanations_and_hidden_gu(self):
  result=execute_preview(PREVIEW);self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),8);self.assertEqual(result['views']['exam'].count('class="mk"'),16)
  for p in self.u['programs']:self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_28_exact_34_file_zip_and_all_ten_extracted_runs(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),34)
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    for name,path in HELPERS.items():self.assertEqual(z.read(name),path.read_bytes())
    for p in FIXTURES.iterdir():self.assertEqual(z.read('kali_metadata/'+p.name),p.read_bytes())
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
    cases=list(csv.reader(io.StringIO(z.read('case_sheet.csv').decode())));self.assertEqual(len(cases),11)
    for name,text in GUIDES.items():self.assertEqual(z.read(name).decode(),text)
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en']);self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
    z.extractall(td)
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-E',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=60)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_29_offline_archive_needs_no_verification_commands_or_network(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('Offline export')),patch('socket.socket',side_effect=AssertionError('Offline export')),patch('infosec_u5_manifest.verify_manifest',side_effect=AssertionError('Read frozen data only')):
    out=export(Path(td)/'kit.zip')
   self.assertEqual(Path(out).read_bytes(),ZIP.read_bytes())

 def test_30_deterministic_rebuild_despite_fresh_tls_and_gpg_homes(self):
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit5.json',PREVIEW,ZIP]+[DIAG_DIR/(n+'.svg') for n in TITLES]+list(FIXTURES.iterdir())
  before={p:p.read_bytes() for p in paths if p.is_file()}
  r=subprocess.run([sys.executable,'tools/build_DI05007021_u5.py'],cwd=ROOT,text=True,capture_output=True,timeout=90)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,raw in before.items():self.assertEqual(p.read_bytes(),raw,str(p))

 def test_31_all_809_prior_source_files_and_all_old_exported_units_preserved(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007021_u5.json').read_text());self.assertEqual(len(baseline),809)
  for rel,wanted in baseline.items():
   raw=(ROOT/rel).read_bytes()
   if rel=='content/computer/sem5/DI05007021/subject.json':
    old=json.loads(raw);self.assertEqual(old['units'][4]['file'],'unit5.json');old['units'][4]['file']=None
    raw=(json.dumps(old,ensure_ascii=False,indent=1)+'\n').encode()
   self.assertEqual(hashlib.sha256(raw).hexdigest(),wanted,rel)
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr);self.assertEqual((len(list((out/'subjects').glob('*.json'))),len(list((out/'units').glob('*.json')))),(14,69))
   for p in BASE.rglob('*.json'):
    rel=p.relative_to(BASE).as_posix()
    if rel=='catalog.json':continue
    if rel=='subjects/DI05007021.json':
     expected=json.loads(p.read_bytes());expected['available_units']=[1,2,3,4,5];expected['units'][4]['file']='unit5.json'
     self.assertEqual(json.loads((out/rel).read_bytes()),expected)
    else:self.assertEqual((out/rel).read_bytes(),p.read_bytes(),rel)
   old=json.loads((BASE/'catalog.json').read_bytes());new=json.loads((out/'catalog.json').read_bytes())
   self.assertEqual(new['subjects'],old['subjects']);self.assertEqual(new['branches'],old['branches'])
   for rel,wanted in new['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)
   for n,wanted in {1:'8848c814de7659bb4210ddea155e8c87642a0d66cd203c4261390c1c44c8c5b5',2:'756ceb376b312cc9da930ab5bd6f4567e661c5a36e37f56764a7c3dceb962e17',3:'6cef3afbe321215279969584edc05d238cbc2ea1ef555775fb2356b19a7446b3',4:'2064f04977028a857029898157cb965491554461ecf5e9d9869109c75adbd46d'}.items():
    self.assertEqual(hashlib.sha256((out/f'units/DI05007021_u{n}.json').read_bytes()).hexdigest(),wanted)

 def test_32_original_answered_practice_not_official_paper(self):
  self.assertTrue(self.u['question_marks_are_suggested']);self.assertIn('not official past papers',self.u['question_provenance'])
  for i,((q,marks,a),item,question) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(question,{'q':{'en':'Practice: '+q},'marks':marks});self.assertIn(marks,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')

 def test_33_guides_and_cases_are_fictional_privacy_preserving_and_not_os_proof(self):
  self.assertEqual((len(GUIDES),len(CASES)),(2,10))
  self.assertTrue('Kali Linux itself is NOT downloaded, installed or booted' in GUIDES['guides/kali_study.md'])
  self.assertTrue('No malware execution is part' in GUIDES['guides/kali_study.md'])
  self.assertTrue('not legal findings' in GUIDES['guides/defensive_case_study.md'])
  self.assertTrue('immediate danger' in self.plain)
  self.assertTrue('does not prescribe legal filing deadlines' in ' '.join(GUIDES['guides/defensive_case_study.md'].split()))

 def test_34_no_private_keys_executables_images_iso_or_credentials(self):
  payload=PREVIEW.read_bytes()+(SUBJ_DIR/'unit5.json').read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for name in z.namelist():
    self.assertNotRegex(name,r'\.(exe|dll|so|deb|tar|gz|iso|img|ova|vmdk|vdi|qcow2|pem|der)$');payload+=z.read(name)
  for marker in [b'-----BEGIN PRIVATE KEY-----',b'-----BEGIN RSA PRIVATE KEY-----',b'-----BEGIN PGP PRIVATE KEY BLOCK-----']:
   self.assertNotIn(marker,payload)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'Private credential leaked')
  self.assertLess(ZIP.stat().st_size,50000);self.assertFalse((ROOT.parent/'php_root').exists())

 def test_35_system_network_crypto_and_environment_unchanged(self):
  for p,raw in self.system.items():self.assertEqual(p.read_bytes(),raw)
  self.assertEqual(subprocess.run(['ip','-j','address'],check=True,capture_output=True).stdout,self.addresses)
  self.assertEqual(subprocess.run(['ip','-j','route'],check=True,capture_output=True).stdout,self.routes)
  cap=next(l.split()[1] for l in Path('/proc/self/status').read_text().splitlines() if l.startswith('CapEff:'))
  self.assertEqual(int(cap,16),0)
  self.assertNotEqual(os.environ.get('GNUPGHOME',''),str(FIXTURES))

 def test_36_attack_and_guarantee_claims_absent_from_executed_scope(self):
  e=self.u['runtime_evidence']
  for name in ['malware_or_attack_payload_executed','phishing_email_or_form_delivered','public_network_targets_used','forged_packets_or_ARP_cache_writes','flood_or_load_test_performed','botnet_C2_backdoor_or_persistence_created','real_user_data_or_credentials_used','system_trust_or_network_policy_changed','real_private_keys_published','production_malware_detection_or_resilience_claim','legal_finding_or_response_guarantee']:
   self.assertIs(e[name],False,name)
  for p in EXAMPLES:
   ast.parse(p['code']['en'])
   for bad in ['smtplib','urllib.request','requests.get','os.system','shell=True','AF_PACKET','subprocess.Popen']:
    self.assertNotIn(bad,p['code']['en'])
  self.assertTrue('No malware' in GUIDES['guides/kali_study.md'])

if __name__=='__main__':unittest.main(verbosity=2)
