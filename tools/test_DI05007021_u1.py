"""26 validation groups: real safe examples, curriculum, rendering and preservation."""
import ast,contextlib,hashlib,hmac,io,json,os,re,socket,subprocess,sys,tempfile,unittest,zipfile
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
from subject_DI05007021 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007021_u1_programs import EXAMPLES,execute_all
from content_DI05007021_u1_notes import NOTES,SPECIFIC,PERVASIVE,PRACTICE
from diagrams_DI05007021_u1 import TITLES
from export_app_content import clean_svg
from export_DI05007021_u1_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007021_unit1_preview.html';ZIP=ROOT/'preview/DI05007021_unit1_practicals.zip'
BASE=Path('/opt/repos/diplomaone-content/data')

def exec_example(p):
 namespace={};output=io.StringIO()
 with contextlib.redirect_stdout(output):exec(compile(p['code']['en'],p['id'],'exec'),namespace)
 return namespace,output.getvalue()

class InfoSecUnit1Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit1.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.text=' '.join(strings(cls.u)).lower()

 def test_01_syllabus_identity_and_actual_official_scheme(self):
  s=self.s
  self.assertEqual((s['code'],s['semester'],s['syllabus_year'],s['category']),('DI05007021',5,'2026-27','PCC-13'))
  self.assertEqual(s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})
  self.assertEqual(s['teaching'],{'lecture':3,'tutorial':0,'practical':2})
  self.assertEqual([x['hours'] for x in s['units']],[6,12,10,9,8])
  self.assertEqual([x['weightage'] for x in s['units']],[15,25,25,20,15])
  self.assertEqual(sum(x['hours'] for x in s['units']),45)
  self.assertEqual(len(s['course_outcomes']),5);self.assertEqual(len(s['practicals']),12)
  self.assertEqual(s['theory_rbt_percent'],{'remember':25,'understand':50,'apply':25,'analyze':0,'evaluate':0,'create':0})
  self.assertIn('ae1602e5b6a1ee6b8e523a832e4908141ea4a79c8fb89208d987f17f6e3b05aa',(ROOT/'tools/syllabus_DI05007021.txt').read_text())

 def test_02_only_approved_unit_one_available(self):
  self.assertEqual([x['file'] for x in self.s['units']],['unit1.json',None,None,None,None])
  self.assertEqual(sorted(p.name for p in SUBJ_DIR.glob('unit*.json')),['unit1.json'])
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage']),(1,6,15))
  self.assertEqual(self.u['practical_numbers'],[1]);self.assertIn('CO1',self.u['learning_outcomes'][0]['en'])

 def test_03_english_only_no_priority_stars_or_language_switch(self):
  def check(o):
   if isinstance(o,dict):
    self.assertNotIn('gu',o);self.assertNotIn('key',o)
    for v in o.values():check(v)
   elif isinstance(o,list):
    for v in o:check(v)
   elif isinstance(o,str):self.assertNotRegex(o,r'[\u0a80-\u0aff]')
  check(self.s);check(self.u);self.assertEqual(self.s['languages'],['en'])

 def test_04_complete_focused_lesson_counts(self):
  self.assertEqual(sum(len(s['items']) for s in NOTES),14)
  self.assertEqual(sum(len(s['items']) for s in self.u['notes']),26)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams']),len(self.u['exam_questions'])),(6,8,12))
  self.assertEqual(sum(len(s['items']) for s in self.u['syntax']),12)
  self.assertEqual(sum(len(s['items']) for s in self.u['viva']),28)
  self.assertEqual(self.u['tabs'],TABS)

 def test_05_cia_goals_and_no_single_control_guarantees(self):
  for word in ['confidentiality','integrity','availability','authorized','timely','reliable','improper','physical','procedures']:
   self.assertIn(word,self.text)
  self.assertIn('encryption does not keep a failed server online',self.text)
  self.assertIn('one incident can affect several goals',self.text)

 def test_06_passive_active_and_four_active_attack_types(self):
  for word in ['traffic analysis','message contents','masquerade','replay','modification','denial of service']:
   self.assertIn(word,self.text)
  self.assertIn('passive does not mean harmless',self.text)
  self.assertIn('freshness',self.text)

 def test_07_services_identity_permissions_and_nonrepudiation(self):
  for word in ['origin','receipt','least privilege','authorization','access control','private-key control']:
   self.assertIn(word,self.text)
  self.assertIn('hmac is not a digital signature',self.text)
  self.assertIn('does not automatically prove which human',self.text)
  self.assertIn('does not authorize every operation',self.text)

 def test_08_all_eight_specific_mechanisms(self):
  expected=['Encipherment','Digital signature','Access control','Data integrity','Authentication exchange','Traffic padding','Routing control','Notarization']
  self.assertEqual([x[0] for x in SPECIFIC],expected)
  for word in expected:self.assertIn(word.lower(),self.text)

 def test_09_all_five_pervasive_mechanisms(self):
  self.assertEqual([x[0] for x in PERVASIVE],['Trusted functionality','Security labels','Event detection','Security audit trail','Security recovery'])
  for n,d in PERVASIVE:self.assertIn(n.lower(),self.text)
  self.assertIn('labels alone do not enforce permissions',self.text)
  self.assertIn('editable logs are not conclusive proof',self.text)

 def test_10_answered_original_practice_not_official_paper(self):
  self.assertTrue(self.u['question_marks_are_suggested'])
  self.assertIn('not official past papers',self.u['question_provenance'])
  self.assertEqual(len(self.u['notes'][-1]['items']),12)
  for i,((q,m,a),item,exam) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(exam,{'q':{'en':'Practice: '+q},'marks':m});self.assertIn(m,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')
  self.assertIn('not a guaranteed number of questions or marks',self.text)

 def test_11_all_six_examples_reexecute_exactly(self):
  self.assertEqual(execute_all(),self.u['programs'])
  for p in self.u['programs']:
   compile(p['code']['en'],p['id'],'exec')
   self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])
   self.assertIn('expl',p);self.assertNotIn('explain',p)

 def test_12_real_sha256_and_all_single_byte_changes(self):
  n,out=exec_example(self.p['sec1p01']);self.assertEqual(out,self.p['sec1p01']['out'])
  self.assertEqual(n['trusted_digest'],hashlib.sha256(n['original']).digest())
  for i in range(len(n['original'])):
   changed=bytearray(n['original']);changed[i]^=1
   self.assertFalse(n['matches_reference'](changed))
  self.assertTrue(n['matches_reference'](n['original']))

 def test_13_real_hmac_wrong_key_tamper_and_no_replay_claim(self):
  n,out=exec_example(self.p['sec1p02']);n2,_=exec_example(self.p['sec1p02'])
  self.assertEqual(out,self.p['sec1p02']['out']);self.assertFalse(n['secret']==n2['secret'])
  self.assertEqual(n['tag'],hmac.new(n['secret'],n['message'],hashlib.sha256).digest())
  wrong=hmac.new(b'wrong-only-for-negative-test',n['message'],hashlib.sha256).digest()
  self.assertFalse(hmac.compare_digest(wrong,n['tag']));self.assertFalse(n['verifies'](n['changed']))
  self.assertTrue(n['verifies'](n['message']));self.assertTrue(n['verifies'](n['message']))
  self.assertNotIn(n['secret'].hex(),out);self.assertIn('not confidentiality, replay protection',self.p['sec1p02']['expl']['en'])

 def test_14_real_tcp_framing_worker_and_listener_cleanup(self):
  n,out=exec_example(self.p['sec1p03']);self.assertEqual(out,self.p['sec1p03']['out'])
  self.assertEqual(n['address'][0],'127.0.0.1');self.assertFalse(n['worker'].is_alive())
  self.assertEqual(n['listener'].fileno(),-1);self.assertEqual(n['client'].fileno(),-1)
  class SplitBytes:
   def __init__(self,parts):self.parts=iter(parts)
   def recv(self,count):return next(self.parts,b'')
  self.assertEqual(n['receive_exact'](SplitBytes([b'U',b'NI',b'T1']),5),b'UNIT1')
  with self.assertRaises(ConnectionError):n['receive_exact'](SplitBytes([b'U']),5)

 def test_15_actual_read_only_loopback_interface_and_route(self):
  n,out=exec_example(self.p['sec1p04']);self.assertEqual(out,self.p['sec1p04']['out'])
  self.assertEqual(n['interface']['ifname'],'lo');self.assertEqual(n['ipv4'],['127.0.0.1'])
  self.assertIn('UP',n['interface']['flags']);self.assertEqual(n['route']['dev'],'lo');self.assertEqual(n['neighbors'],[])

 def test_16_actual_ping_denial_or_single_reply_never_invented(self):
  n,out=exec_example(self.p['sec1p05']);self.assertEqual(out,self.p['sec1p05']['out'])
  self.assertEqual(n['status'],self.u['runtime_evidence']['ping_observed_status'])
  if n['result'].returncode==0:self.assertEqual(n['status'],'one_local_echo_reply')
  else:
   self.assertIn('operation not permitted',n['result'].stderr.lower())
   self.assertEqual(n['status'],'blocked_by_lab_permissions')
  self.assertIn('no icmp success claimed',self.text)

 def test_17_actual_name_resolution_owned_ss_row_and_closed_socket(self):
  n,out=exec_example(self.p['sec1p06']);self.assertEqual(out,self.p['sec1p06']['out'])
  self.assertEqual(n['addresses'],['127.0.0.1']);self.assertTrue(n['found']);self.assertEqual(n['listener'].fileno(),-1)
  rows=subprocess.run(['ss','-ltnH',f'sport = :{n["port"]}'],check=True,text=True,capture_output=True,timeout=3).stdout
  self.assertNotIn(f'127.0.0.1:{n["port"]}',rows)

 def test_18_safe_scope_and_guided_commands_not_false_execution(self):
  evidence=self.u['runtime_evidence']
  for k in ['external_network_targets','persistent_service','dos_traffic_generated','privileged_host_changes','packet_capture_executed','windows_commands_executed','simulator_or_kali_executed']:
   self.assertIs(evidence[k],False)
  for p in EXAMPLES:
   source=p['code']['en'];ast.parse(source)
   for bad in ['shell=True','0.0.0.0','https://','http://','sudo','os.system','-flood']:
    self.assertNotIn(bad,source)
  for tool in ['ipconfig','tracert','arp','tcpdump','whois','host','netstat','nslookup','ftp','telnet']:
   self.assertIn(tool,self.text)
  self.assertIn('not necessarily dns',self.p['sec1p06']['expl']['en'].lower())
  self.assertIn('not claimed as executed',self.text)

 def test_19_balanced_safe_html_and_all_linked_programs_diagrams(self):
  linked=set();diagrams=set()
  for section in self.u['notes']:
   for item in section['items']:
    Fragment().finish(item['body']['en']);self.assertNotIn('@@',item['body']['en'])
    linked.update(item.get('programs',[]))
    if item.get('diagram'):diagrams.add(item['diagram'])
  self.assertEqual(linked,set(self.p));self.assertEqual(diagrams,set(TITLES))
  for p in self.u['programs']:Fragment().finish(p['expl']['en'])
  for g in self.u['syntax']:
   for e in g['items']:Fragment().finish(e['terms']['en'])
  for g in self.u['viva']:
   for e in g['items']:Fragment().finish(e['a']['en'])

 def test_20_eight_svgs_real_font_bounds_raster_and_contact_sheets(self):
  images=[]
  for d in self.u['diagrams']:
   raw=(SUBJ_DIR/d['file']).read_text();root=ET.fromstring(raw)
   w,h=map(float,root.get('viewBox').split()[2:]);self.assertEqual(w,360)
   for bad in ['<script','<style','<marker','<foreignObject','<image','href=']:self.assertNotIn(bad,raw)
   for node in root.iter('{http://www.w3.org/2000/svg}text'):
    size=float(node.get('font-size','12'));font_name='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+font_name,round(size*10))
    pieces=list(node) or [node]
    for piece in pieces:
     txt=''.join(piece.itertext());length=font.getlength(txt)/10;x=float(piece.get('x',node.get('x')))
     anchor=piece.get('text-anchor',node.get('text-anchor','start'))
     left=x-length/2 if anchor=='middle' else x-length if anchor=='end' else x
     self.assertGreaterEqual(left,1,(d['id'],txt));self.assertLessEqual(left+length,w-1,(d['id'],txt))
     y=float(piece.get('y',node.get('y','0')))
     self.assertGreaterEqual(y-size,-1,(d['id'],txt));self.assertLessEqual(y+size/3,h+1,(d['id'],txt))
   png=resvg_py.svg_to_bytes(svg_string=clean_svg(raw),zoom=1.25,font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',sans_serif_family='DejaVu Sans',skip_system_fonts=True)
   image=Image.open(io.BytesIO(bytes(png))).convert('RGB');self.assertGreater(len(image.getcolors(image.width*image.height)),20)
   images.append((d['id'],image))
  for start in [0,4]:
   group=images[start:start+4];height=max(image.height for name,image in group)+42
   sheet=Image.new('RGB',(960,height*2+16),'#EAE4F1');draw=ImageDraw.Draw(sheet)
   for i,(name,image) in enumerate(group):
    x=i%2*480+15;y=i//2*height+30;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(image,(x,y))
   sheet.save(ROOT/f'preview/DI05007021_unit1_diagrams_{start//4+1}.png')

 def test_21_all_six_preview_views_outputs_explanations_and_hidden_gu(self):
  result=execute_preview(PREVIEW)
  self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),8)
  for p in self.u['programs']:
   self.assertIn(p['title']['en'],result['views']['programs']);self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertEqual(result['views']['exam'].count('class="mk"'),12)
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_22_fifteen_file_public_zip_and_all_six_extracted_reruns(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),15)
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence']);z.extractall(td)
    self.assertIn('No pip dependencies',z.read('README.md').decode())
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en'])
     self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-I',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=12)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_23_offline_zip_export_and_reproducibility(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('No commands during export')),patch('socket.socket',side_effect=AssertionError('No sockets during export')):
    path=export(Path(td)/'kit.zip')
   self.assertEqual(Path(path).read_bytes(),ZIP.read_bytes())

 def test_24_deterministic_rebuild(self):
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit1.json',PREVIEW,ZIP]+list(DIAG_DIR.glob('*.svg'))
  before={p:p.read_bytes() for p in paths}
  r=subprocess.run([sys.executable,'tools/build_DI05007021_u1.py'],cwd=ROOT,text=True,capture_output=True,timeout=25)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,raw in before.items():self.assertEqual(p.read_bytes(),raw,str(p))

 def test_25_entire_prior_content_and_public_exports_preserved(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007021.json').read_text())
  self.assertEqual(len(baseline),766)
  for rel,wanted in baseline.items():self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),wanted,rel)
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertEqual((len(list((out/'subjects').glob('*.json'))),len(list((out/'units').glob('*.json')))),(14,65))
   for p in BASE.rglob('*.json'):
    if p.name!='catalog.json':self.assertEqual((out/p.relative_to(BASE)).read_bytes(),p.read_bytes(),str(p))
   old=json.loads((BASE/'catalog.json').read_bytes());new=json.loads((out/'catalog.json').read_bytes())
   for code,value in old['subjects'].items():self.assertEqual(new['subjects'][code],value)
   for branch in old['branches']:
    actual=next(x for x in new['branches'] if x['key']==branch['key'])
    expected=json.loads(json.dumps(branch))
    if branch['key']=='computer':expected['semesters']['5']=['DI05007021']
    self.assertEqual(actual,expected)
   self.assertEqual(new['subjects']['DI05007021']['name'],{'en':'Information Security'})
   self.assertEqual(new['subjects']['DI05007021']['languages'],['en'])
   subject=json.loads((out/'subjects/DI05007021.json').read_text());self.assertEqual(subject['available_units'],[1])
   unit=json.loads((out/'units/DI05007021_u1.json').read_text())
   self.assertEqual(unit['svgs'],{n:clean_svg((DIAG_DIR/(n+'.svg')).read_text()) for n in TITLES})
   for rel,wanted in new['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)

 def test_26_no_credentials_or_unwanted_binaries_in_new_deliverables(self):
  payload=(SUBJ_DIR/'unit1.json').read_bytes()+PREVIEW.read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for n in z.namelist():
    self.assertNotRegex(n,r'\.(exe|so|deb|dll|tar|gz)$');payload+=z.read(n)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'A private credential leaked')
  self.assertLess(ZIP.stat().st_size,15000)
  self.assertFalse((ROOT.parent/'php_root').exists())
  self.assertFalse((ROOT.parent/'.cache/diplomaone-redis-u5').exists())
  self.assertFalse((ROOT.parent/'.cache/diplomaone-neo4j-u4').exists())

if __name__=='__main__':unittest.main(verbosity=2)
