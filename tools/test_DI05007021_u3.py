"""36 groups: actual RSA/OAEP/PSS/CSR/X.509/CRL, rendering and preservation."""
import ast,calendar,csv,datetime,hashlib,html,io,json,math,os,re,stat,subprocess,sys,tempfile,unittest,zipfile
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
import infosec_u3_math as m
from infosec_u3_lab import Lab,HOST,openssl_version
from subject_DI05007021 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007021_u3_programs import EXAMPLES,execute_all,HELPERS
from content_DI05007021_u3_notes import NOTES,PRACTICE
from diagrams_DI05007021_u3 import TITLES
from export_app_content import clean_svg
from export_DI05007021_u3_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007021_unit3_preview.html';ZIP=ROOT/'preview/DI05007021_unit3_practicals.zip'
BASE=Path('/opt/repos/diplomaone-content/data')

def error_codes(result):return [int(x) for x in re.findall(rb'error (\d+) at ',result.stdout+result.stderr)]

class Unit3Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit3.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.text=' '.join(strings(cls.u)).lower()
  cls.plain=html.unescape(re.sub(r'<[^>]*>','',cls.text))
  cls.lab=Lab();cls.lab.__enter__();cls.addClassCleanup(cls.lab.__exit__,None,None,None);cls.lab.pki()
  cls.system={p:p.read_bytes() for p in [Path('/etc/ssl/openssl.cnf'),Path('/etc/ssl/certs/ca-certificates.crt')] if p.is_file()}

 def rejected(self,result,code):
  self.assertNotEqual(result.returncode,0);self.assertIn(code,error_codes(result))

 def test_01_official_unit_scheme_and_practical(self):
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage'],self.u['practical_numbers']),(3,10,25,[6]))
  self.assertIn('CO3',self.u['learning_outcomes'][0]['en'])
  self.assertEqual((self.s['semester'],self.s['syllabus_year']),(5,'2026-27'))
  self.assertEqual(self.s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})

 def test_02_only_approved_first_three_units(self):
  self.assertEqual([x['file'] for x in self.s['units']],['unit1.json','unit2.json','unit3.json',None,None])
  self.assertEqual(sorted(p.name for p in SUBJ_DIR.glob('unit*.json')),['unit1.json','unit2.json','unit3.json'])
  self.assertEqual(self.u['tabs'],TABS)

 def test_03_english_only_no_priority_flags(self):
  def walk(o):
   if isinstance(o,dict):
    self.assertNotIn('gu',o);self.assertNotIn('key',o)
    for v in o.values():walk(v)
   elif isinstance(o,list):
    for v in o:walk(v)
   elif isinstance(o,str):self.assertNotRegex(o,r'[\u0a80-\u0aff]')
  walk(self.u);walk(self.s);self.assertEqual(self.s['languages'],['en'])

 def test_04_counts_and_every_syllabus_topic(self):
  self.assertEqual(sum(len(g['items']) for g in NOTES),16)
  self.assertEqual(sum(len(g['items']) for g in self.u['notes']),32)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams']),len(self.u['exam_questions'])),(10,10,16))
  self.assertEqual(sum(len(g['items']) for g in self.u['syntax']),14)
  self.assertEqual(sum(len(g['items']) for g in self.u['viva']),36)
  for term in ['public-key','applications','rsa','computational','security','digital signature','certificate','registration authority','certificate authority','obtaining','authenticity','integrity']:
   self.assertTrue(term in self.plain,term)

 def test_05_correct_boundary_and_trust_statements(self):
  for term in ['tls 1.3 does not use rsa key transport','not proof that a statement is true','not automatically an authentic key','not a production enrollment service','not a revocation-status assertion']:
   self.assertTrue(term in self.plain,term)
  self.assertTrue('private-key encryption' in self.plain)

 def test_06_real_small_number_key_and_phi_lambda_relations(self):
  pair=m.toy_keypair(61,53,17)
  self.assertEqual(pair,{'p':61,'q':53,'n':3233,'phi':3120,'e':17,'d':2753,'lambda_n':780})
  self.assertEqual(pair['e']*pair['d']%pair['phi'],1)
  self.assertEqual(pair['e']*pair['d']%pair['lambda_n'],1)
  self.assertEqual(pair,self.u['worked_data']['public_toy_parameters'])

 def test_07_invalid_primes_keys_types_and_composite_e(self):
  for p,q,e in [(61,61,17),(9,53,17),(2,53,17),(-3,53,17),(65537,53,17),(61,53,1),(61,53,12),(61,53,3120)]:
   with self.assertRaises(ValueError):m.toy_keypair(p,q,e)
  with self.assertRaises(TypeError):m.toy_keypair(True,53,17)
  with self.assertRaises(TypeError):m.toy_keypair(61.0,53,17)
  pair=m.toy_keypair(7,11,49)
  self.assertEqual(m.rsa_decrypt(m.rsa_encrypt(8,pair),pair),8)

 def test_08_all_3233_representatives_roundtrip_including_non_coprime(self):
  pair=m.toy_keypair(61,53,17)
  for value in range(pair['n']):self.assertEqual(m.rsa_decrypt(m.rsa_encrypt(value,pair),pair),value)
  self.assertEqual(m.rsa_encrypt(65,pair),2790)
  for value in [0,53,61,3232]:self.assertEqual(m.rsa_decrypt(m.rsa_encrypt(value,pair),pair),value)

 def test_09_representative_bounds_not_silent_reduction(self):
  pair=m.toy_keypair(61,53,17)
  for value in [-1,3233,9999]:
   with self.assertRaises(ValueError):m.rsa_encrypt(value,pair)
   with self.assertRaises(ValueError):m.rsa_decrypt(value,pair)
  for value in [True,65.0,'65']:
   with self.assertRaises(TypeError):m.rsa_encrypt(value,pair)

 def test_10_actual_square_and_multiply_trace_and_edge_cases(self):
  result,rows=m.power_trace(65,17,3233)
  self.assertEqual(result,2790);self.assertEqual([r['power'] for r in rows],[65,992,1232,1547,789])
  self.assertEqual([r['bit'] for r in rows],[1,0,0,0,1]);self.assertEqual(rows,self.u['worked_data']['modexp_trace'])
  for exponent in [0,1,2,17,2753]:self.assertEqual(m.power_trace(65,exponent,3233)[0],pow(65,exponent,3233))
  for exponent in [-1,1<<64]:
   with self.assertRaises(ValueError):m.power_trace(65,exponent,3233)

 def test_11_actual_raw_rsa_determinism_and_algebra_only_fixed_data(self):
  p=m.toy_keypair(61,53,17)
  self.assertEqual(m.rsa_encrypt(65,p),m.rsa_encrypt(65,p))
  self.assertEqual(m.rsa_encrypt(2,p)*m.rsa_encrypt(3,p)%p['n'],m.rsa_encrypt(6,p))
  self.assertTrue('fixed tiny public classroom values' in self.p['sec3p03']['expl']['en'])

 def test_12_fresh_real_rsa_bits_exponent_modes_and_distinct_keys(self):
  lab=self.lab
  self.assertEqual(lab.public_facts('recipient'),{'bits':2048,'public_exponent':65537})
  self.assertEqual(stat.S_IMODE(lab.folder.stat().st_mode),0o700)
  self.assertEqual(stat.S_IMODE(lab.rsa('recipient').stat().st_mode),0o600)
  self.assertFalse(lab.public('recipient').read_bytes()==lab.public('other').read_bytes())

 def test_13_actual_oaep_sha256_boundary_and_randomized_recovery(self):
  lab=self.lab;message=b'A'*190
  first=lab.oaep_encrypt(message);second=lab.oaep_encrypt(message)
  self.assertEqual(first.returncode,0);self.assertEqual(len(first.stdout),256)
  self.assertFalse(first.stdout==second.stdout)
  recovered=lab.oaep_decrypt(first.stdout);self.assertEqual((recovered.returncode,recovered.stdout),(0,message))
  too_long=lab.oaep_encrypt(b'A'*191)
  self.assertNotEqual(too_long.returncode,0);self.assertIn(b'data too large',too_long.stderr.lower())
  empty=lab.oaep_encrypt(b'');self.assertEqual(lab.oaep_decrypt(empty.stdout).stdout,b'')

 def test_14_actual_oaep_tamper_wrong_key_and_digest_mismatch(self):
  lab=self.lab;encrypted=lab.oaep_encrypt(b'Only fixed course data')
  changed=bytearray(encrypted.stdout);changed[-1]^=1
  for result in [lab.oaep_decrypt(bytes(changed)),lab.oaep_decrypt(encrypted.stdout,'wrong')]:
   self.assertNotEqual(result.returncode,0);self.assertIn(b'oaep',result.stderr.lower())
  lab.write('cipher.bin',encrypted.stdout)
  wrong=lab.run('pkeyutl','-decrypt','-inkey',lab.rsa('recipient'),'-in',lab.path('cipher.bin'),
   '-pkeyopt','rsa_padding_mode:oaep','-pkeyopt','rsa_oaep_md:sha384','-pkeyopt','rsa_mgf1_md:sha256',check=False)
  self.assertNotEqual(wrong.returncode,0)

 def test_15_actual_pss_original_tampered_wrong_key_and_parameters(self):
  lab=self.lab;message=b'Fixed course document';signature=lab.pss_sign(message)
  self.assertEqual(len(signature),256);self.assertTrue(lab.pss_verify(message,signature))
  self.assertFalse(lab.pss_verify(message+b'!',signature));self.assertFalse(lab.pss_verify(message,signature,'other'))
  lab.write('verify.bin',message);lab.write('signature.bin',signature)
  wrong=lab.run('dgst','-sha256','-verify',lab.public('signer'),'-signature',lab.path('signature.bin'),
   '-sigopt','rsa_padding_mode:pss','-sigopt','rsa_pss_saltlen:0',lab.path('verify.bin'),check=False)
  self.assertNotEqual(wrong.returncode,0)

 def test_16_actual_csr_signature_and_modified_signature_rejected(self):
  lab=self.lab;request=lab.request('learner','Course Learner S01',HOST)
  self.assertTrue(lab.request_valid(request))
  der=lab.run('req','-in',request,'-outform','DER').stdout
  changed=bytearray(der);changed[-1]^=1
  self.assertFalse(lab.request_valid(lab.write('modified.csr.der',bytes(changed)),True))
  view=lab.run('req','-in',request,'-text','-noout').stdout
  self.assertIn(HOST.encode(),view)
  self.assertFalse(self.u['runtime_evidence']['real_RA_identity_vetting_performed'])

 def test_17_actual_three_certificate_chain_and_public_fields(self):
  lab=self.lab;result=lab.verify()
  self.assertEqual(result.returncode,0)
  for name,expect in [('root',b'CA:TRUE'),('intermediate',b'CA:TRUE'),('leaf',b'CA:FALSE')]:
   output=lab.run('x509','-in',lab.path(name+'.cert.pem'),'-noout','-ext','basicConstraints').stdout
   self.assertIn(expect,output)
  text=lab.run('x509','-in',lab.path('leaf.cert.pem'),'-noout','-ext','subjectAltName').stdout
  self.assertIn(b'DNS:'+HOST.encode(),text)

 def test_18_unrelated_trust_and_missing_issuer_rejected(self):
  self.rejected(self.lab.verify(root=self.lab.unrelated_root()),20)
  self.rejected(self.lab.verify(intermediate=False),20)

 def test_19_wrong_hostname_and_purpose_rejected(self):
  self.rejected(self.lab.verify(hostname='wrong.diploma.test'),62)
  self.rejected(self.lab.verify(purpose='sslclient'),26)
  self.assertEqual(self.lab.verify().returncode,0)

 def test_20_expiry_and_not_yet_valid_with_evaluation_time_only(self):
  lab=self.lab
  self.rejected(lab.verify(attime=lab.expiry_epoch()+1),10)
  start=lab.run('x509','-in',lab.path('leaf.cert.pem'),'-noout','-startdate').stdout.decode().strip().split('=',1)[1]
  epoch=calendar.timegm(datetime.datetime.strptime(start,'%b %d %H:%M:%S %Y %Z').timetuple())
  self.rejected(lab.verify(attime=epoch-2),9)
  self.assertEqual(lab.verify().returncode,0)

 def test_21_actual_modified_certificate_signature_fails(self):
  lab=self.lab;der=lab.run('x509','-in',lab.path('leaf.cert.pem'),'-outform','DER').stdout
  changed=bytearray(der);changed[-1]^=1
  self.rejected(lab.verify(certificate=lab.write('modified.cert.der',bytes(changed))),7)

 def test_22_cryptographically_signed_but_invalid_ca_constraints_rejected(self):
  lab=self.lab
  ext=lab.write('badissuer.ext','[bad]\nbasicConstraints=critical,CA:FALSE\nkeyUsage=critical,digitalSignature\nsubjectKeyIdentifier=hash\nauthorityKeyIdentifier=keyid,issuer\n')
  lab.run('x509','-req','-sha256','-in',lab.path('intermediate.csr.pem'),'-CA',lab.path('root.cert.pem'),
   '-CAkey',lab.rsa('root'),'-set_serial','9','-days','30','-extfile',ext,'-extensions','bad','-out',lab.path('badissuer.cert.pem'))
  result=lab.run('verify','-CAfile',lab.path('root.cert.pem'),'-no-CApath','-no-CAstore','-x509_strict',
   '-untrusted',lab.path('badissuer.cert.pem'),lab.path('leaf.cert.pem'),check=False)
  self.assertNotEqual(result.returncode,0);self.assertTrue(set(error_codes(result))&{24,32,79})

 def test_23_unknown_critical_extension_rejected(self):
  lab=self.lab
  ext=lab.write('critical.ext','[bad]\nbasicConstraints=critical,CA:FALSE\nkeyUsage=critical,digitalSignature,keyEncipherment\nextendedKeyUsage=serverAuth\nsubjectAltName=DNS:'+HOST+'\nsubjectKeyIdentifier=hash\nauthorityKeyIdentifier=keyid,issuer\n1.2.3.4=critical,DER:05:00\n')
  lab.run('x509','-req','-sha256','-in',lab.path('leaf.csr.pem'),'-CA',lab.path('intermediate.cert.pem'),
   '-CAkey',lab.rsa('intermediate'),'-set_serial','4097','-days','7','-extfile',ext,'-extensions','bad','-out',lab.path('critical.cert.pem'))
  self.rejected(lab.verify(certificate=lab.path('critical.cert.pem')),34)

 def test_24_real_leaf_crl_before_and_after_revocation(self):
  with Lab() as lab:
   self.assertEqual(lab.verify(crl=lab.crl()).returncode,0)
   self.rejected(lab.verify(crl=lab.crl(revoke=True)),23)
   self.assertEqual(lab.verify().returncode,0)
  evidence=self.u['runtime_evidence']
  self.assertTrue(evidence['leaf_CRL_check_performed']);self.assertFalse(evidence['full_chain_revocation_checked'])
  self.assertFalse(evidence['live_CRL_or_OCSP_performed'])

 def test_25_crl_signature_and_freshness_failures_are_real(self):
  lab=self.lab;crl=lab.crl();self.assertEqual(lab.verify(crl=crl).returncode,0)
  der=lab.run('crl','-in',crl,'-outform','DER').stdout
  changed=bytearray(der);changed[-1]^=1
  self.rejected(lab.verify(crl=lab.write('bad.crl.der',bytes(changed))),8)
  end=lab.run('crl','-in',crl,'-noout','-nextupdate').stdout.decode().strip().split('=',1)[1]
  epoch=calendar.timegm(datetime.datetime.strptime(end,'%b %d %H:%M:%S %Y %Z').timetuple())
  self.rejected(lab.verify(crl=crl,attime=epoch+1),12)

 def test_26_private_modes_context_and_exception_cleanup(self):
  with Lab() as lab:
   private=lab.rsa('shortlife');folder=lab.folder
   self.assertEqual(stat.S_IMODE(folder.stat().st_mode),0o700)
   self.assertEqual(stat.S_IMODE(private.stat().st_mode),0o600)
  self.assertFalse(folder.exists())
  with self.assertRaisesRegex(RuntimeError,'deliberate'):
   with Lab() as lab:
    lab.rsa('shortlife');folder=lab.folder;raise RuntimeError('deliberate')
  self.assertFalse(folder.exists())

 def test_27_all_ten_fresh_real_outputs_and_helper_hashes(self):
  self.assertEqual(execute_all(),self.u['programs'])
  self.assertEqual({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},self.u['runtime_evidence']['helper_sha256'])
  self.assertEqual(openssl_version(),self.u['runtime_evidence']['openssl'])
  for p in EXAMPLES:
   compile(p['code']['en'],p['id'],'exec')
   self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])

 def test_28_system_config_trust_and_environment_unchanged(self):
  for p,raw in self.system.items():self.assertEqual(p.read_bytes(),raw)
  self.assertTrue(self.lab.environment['OPENSSL_CONF'].startswith(str(self.lab.folder)))
  self.assertEqual(self.lab.environment['TZ'],'UTC')
  source=HELPERS['pki_lab.py'].read_text()
  for bad in ['shell=True','crl_download','s_server','s_client','no_check_time','update-ca-certificates','legacy']:
   self.assertNotIn(bad,source)
  for arg in ['-no-CApath','-no-CAstore','-x509_strict','-verify_hostname','-purpose']:
   self.assertIn(arg,source)

 def test_29_safe_html_and_all_linked_ids(self):
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

 def test_30_ten_svgs_font_bounds_raster_and_review_sheets(self):
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
  for start in [0,4,8]:
   group=images[start:start+4];height=max(im.height for n,im in group)+42
   sheet=Image.new('RGB',(960,height*((len(group)+1)//2)+16),'#EAE4F1');draw=ImageDraw.Draw(sheet)
   for i,(name,image) in enumerate(group):
    x=i%2*480+15;y=i//2*height+30;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(image,(x,y))
   sheet.save(ROOT/f'preview/DI05007021_unit3_diagrams_{start//4+1}.png')

 def test_31_all_six_preview_views_real_explanations_hidden_gu(self):
  result=execute_preview(PREVIEW);self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),10);self.assertEqual(result['views']['exam'].count('class="mk"'),16)
  for p in self.u['programs']:self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_32_26_file_zip_and_all_ten_actual_extracted_runs(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),26)
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    for name,path in HELPERS.items():self.assertEqual(z.read(name),path.read_bytes())
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
    rows=list(csv.DictReader(io.StringIO(z.read('rsa_trace.csv').decode())))
    self.assertEqual(len(rows),5);self.assertEqual(rows[-1]['Accumulator_mod3233'],'2790')
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en']);self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
    z.extractall(td)
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-E',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=60)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_33_offline_archive_and_rebuild_determinism_with_fresh_keys(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('Offline export')),patch('socket.socket',side_effect=AssertionError('Offline export')):
    out=export(Path(td)/'kit.zip')
   self.assertEqual(Path(out).read_bytes(),ZIP.read_bytes())
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit3.json',PREVIEW,ZIP]+[DIAG_DIR/(n+'.svg') for n in TITLES]
  before={p:p.read_bytes() for p in paths}
  r=subprocess.run([sys.executable,'tools/build_DI05007021_u3.py'],cwd=ROOT,text=True,capture_output=True,timeout=90)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,raw in before.items():self.assertEqual(p.read_bytes(),raw,str(p))

 def test_34_all_prior_787_source_files_and_all_exported_units_preserved(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007021_u3.json').read_text());self.assertEqual(len(baseline),787)
  for rel,wanted in baseline.items():
   raw=(ROOT/rel).read_bytes()
   if rel=='content/computer/sem5/DI05007021/subject.json':
    restored=json.loads(raw);self.assertEqual(restored['units'][2]['file'],'unit3.json');restored['units'][2]['file']=None
    raw=(json.dumps(restored,ensure_ascii=False,indent=1)+'\n').encode()
   self.assertEqual(hashlib.sha256(raw).hexdigest(),wanted,rel)
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr);self.assertEqual((len(list((out/'subjects').glob('*.json'))),len(list((out/'units').glob('*.json')))),(14,67))
   for p in BASE.rglob('*.json'):
    rel=p.relative_to(BASE).as_posix()
    if rel=='catalog.json':continue
    if rel=='subjects/DI05007021.json':
     expected=json.loads(p.read_bytes());expected['available_units']=[1,2,3];expected['units'][2]['file']='unit3.json'
     self.assertEqual(json.loads((out/rel).read_bytes()),expected)
    else:self.assertEqual((out/rel).read_bytes(),p.read_bytes(),rel)
   old=json.loads((BASE/'catalog.json').read_bytes());new=json.loads((out/'catalog.json').read_bytes())
   self.assertEqual(new['subjects'],old['subjects']);self.assertEqual(new['branches'],old['branches'])
   for rel,wanted in new['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)
   for n,wanted in {1:'8848c814de7659bb4210ddea155e8c87642a0d66cd203c4261390c1c44c8c5b5',2:'756ceb376b312cc9da930ab5bd6f4567e661c5a36e37f56764a7c3dceb962e17'}.items():
    self.assertEqual(hashlib.sha256((out/f'units/DI05007021_u{n}.json').read_bytes()).hexdigest(),wanted)

 def test_35_original_answered_practice_not_official_paper(self):
  self.assertTrue(self.u['question_marks_are_suggested']);self.assertIn('not official past papers',self.u['question_provenance'])
  for i,((q,marks,a),item,question) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(question,{'q':{'en':'Practice: '+q},'marks':marks});self.assertIn(marks,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')

 def test_36_no_real_keys_secrets_binaries_or_unclaimed_network_activity(self):
  evidence=self.u['runtime_evidence']
  for field in ['ephemeral_real_private_keys_published','network_access_used','tls_handshake_performed','public_CA_enrollment','real_RA_identity_vetting_performed','browser_or_system_trust_modified','global_crypto_configuration_changed','production_CA_or_protocol_claim','full_PKIX_conformance_claim','fips_validation_claim','full_chain_revocation_checked','live_CRL_or_OCSP_performed']:
   self.assertFalse(evidence[field],field)
  payload=PREVIEW.read_bytes()+(SUBJ_DIR/'unit3.json').read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for name in z.namelist():
    self.assertNotRegex(name,r'\.(pem|der|exe|so|dll|deb|tar|gz)$');payload+=z.read(name)
  self.assertNotIn(b'-----BEGIN PRIVATE KEY-----',payload)
  self.assertNotIn(b'-----BEGIN RSA PRIVATE KEY-----',payload)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'Private credential leaked')
  for p in EXAMPLES:
   ast.parse(p['code']['en'])
   for bad in ['requests','urllib','socket','shell=True','os.system','https://','http://']:self.assertNotIn(bad,p['code']['en'])
  self.assertLess(ZIP.stat().st_size,25000)
  self.assertFalse((ROOT.parent/'php_root').exists())

if __name__=='__main__':unittest.main(verbosity=2)
