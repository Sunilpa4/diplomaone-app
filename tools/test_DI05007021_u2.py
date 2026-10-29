"""34 validation groups: real ciphers, independent DES, safe content and preservation."""
import ast,copy,csv,hashlib,io,json,math,random,re,socket,subprocess,sys,tempfile,unittest,zipfile
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
import infosec_u2_ciphers as c
from infosec_u2_evidence import check_des
from subject_DI05007021 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007021_u2_programs import EXAMPLES,execute_all,HELPER
from content_DI05007021_u2_notes import NOTES,PRACTICE
from diagrams_DI05007021_u2 import TITLES
from export_app_content import clean_svg
from export_DI05007021_u2_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007021_unit2_preview.html';ZIP=ROOT/'preview/DI05007021_unit2_practicals.zip'
BASE=Path('/opt/repos/diplomaone-content/data')

class Unit2Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit2.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.text=' '.join(strings(cls.u)).lower()

 def test_01_official_curriculum_scope(self):
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage']),(2,12,25))
  self.assertEqual(self.u['practical_numbers'],[2,3,4,5]);self.assertIn('CO2',self.u['learning_outcomes'][0]['en'])
  self.assertEqual((self.s['semester'],self.s['syllabus_year']),(5,'2026-27'))
  self.assertEqual(self.s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})
  self.assertEqual([x['hours'] for x in self.s['units']],[6,12,10,9,8])
  self.assertEqual([x['weightage'] for x in self.s['units']],[15,25,25,20,15])

 def test_02_units_one_two_and_other_installed_approved_units(self):
  installed=[i for i in range(1,6) if (SUBJ_DIR/f'unit{i}.json').is_file()]
  self.assertTrue({1,2}.issubset(installed))
  self.assertEqual([x['file'] for x in self.s['units']],[f'unit{i}.json' if i in installed else None for i in range(1,6)])
  self.assertEqual(self.u['tabs'],TABS)

 def test_03_english_only_and_no_priority_flags(self):
  def walk(o):
   if isinstance(o,dict):
    self.assertNotIn('gu',o);self.assertNotIn('key',o)
    for v in o.values():walk(v)
   elif isinstance(o,list):
    for v in o:walk(v)
   elif isinstance(o,str):self.assertNotRegex(o,r'[\u0a80-\u0aff]')
  walk(self.u);walk(self.s);self.assertEqual(self.s['languages'],['en'])

 def test_04_counts_and_complete_syllabus_terms(self):
  self.assertEqual(sum(len(g['items']) for g in NOTES),18)
  self.assertEqual(sum(len(g['items']) for g in self.u['notes']),34)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams'])),(12,10))
  self.assertEqual(sum(len(g['items']) for g in self.u['syntax']),14)
  self.assertEqual(sum(len(g['items']) for g in self.u['viva']),36)
  self.assertEqual(len(self.u['exam_questions']),16)
  for term in ['plaintext','ciphertext','cryptanalysis','cryptology','monoalphabetic','caesar','polyalphabetic','playfair','hill','one-time pad','rail fence','steganography','des']:
   self.assertIn(term,self.text)

 def test_05_classifications_and_security_boundaries(self):
  self.assertIn('polygraphic and polyalphabetic are different classifications',self.text)
  self.assertIn('not suitable choices for protecting real data today',self.text)
  self.assertIn('19 may 2005',self.text);self.assertIn('not a nist/fips validation',re.sub(r'<[^>]*>','',self.text))
  self.assertIn('does not by itself encrypt or authenticate',self.text)

 def test_06_normalization_is_explicit_and_rejects_other_characters(self):
  self.assertEqual(c.letters(' aB c\tD\r\n'),'ABCD');self.assertEqual(c.letters(''),'')
  for bad in ['A1','HELLO!','café','A'+chr(0x0a95),'a_b']:
   with self.assertRaises(ValueError):c.letters(bad)
  with self.assertRaises(TypeError):c.letters(b'ABC')
  with self.assertRaises(TypeError):c.caesar('ABC',True)

 def test_07_caesar_known_vectors_wrap_and_all_shifts(self):
  self.assertEqual(c.caesar('ATTACKATDAWN',3),'DWWDFNDWGDZQ')
  self.assertEqual(c.caesar('XYZ',3),'ABC');self.assertEqual(c.caesar('ABC',-3),'XYZ')
  for k in range(-30,55):
   plain='HELLOWORLDXYZ';self.assertEqual(c.caesar(c.caesar(plain,k),-k),plain)
  self.assertEqual(c.caesar('ABC',26),'ABC')

 def test_08_fixed_sample_caesar_analysis_only(self):
  candidates=[c.caesar('KHOOR',-k) for k in range(26)]
  self.assertEqual(len(candidates),26);self.assertEqual(candidates[3],'HELLO')
  self.assertEqual(candidates.count('HELLO'),1)
  self.assertIn('fixed sample KHOOR',self.p['sec2p02']['expl']['en'])

 def test_09_monoalphabetic_permutation_inverse_and_pattern(self):
  key='QWERTYUIOPASDFGHJKLZXCVBNM'
  self.assertEqual(c.substitution('HELLO',key),'ITSSG')
  self.assertEqual(c.substitution(c.ALPHABET,key),key)
  rng=random.Random(29)
  for _ in range(30):
   key=''.join(rng.sample(c.ALPHABET,26));plain=''.join(rng.choices(c.ALPHABET,k=80))
   self.assertEqual(c.substitution(c.substitution(plain,key),key,True),plain)
  for key in ['A'*26,c.ALPHABET[:-1],'']:
   with self.assertRaises(ValueError):c.substitution('HELLO',key)

 def test_10_vigenere_known_vector_and_empty_key_rejection(self):
  self.assertEqual(c.vigenere('ATTACKATDAWN','LEMON'),'LXFOPVEFRNHR')
  self.assertEqual(c.vigenere('LXFOPVEFRNHR','LEMON',True),'ATTACKATDAWN')
  with self.assertRaises(ValueError):c.vigenere('HELLO','')
  self.assertEqual(c.vigenere('','LEMON'),'')

 def test_11_playfair_square_has_25_unique_no_j(self):
  square=c.playfair_square('PLAYFAIREXAMPLE')
  self.assertEqual(square,'PLAYFIREXMBCDGHKNOQSTUVWZ')
  self.assertEqual((len(square),len(set(square))),(25,25));self.assertNotIn('J',square)
  self.assertEqual(c.playfair_square('JIG'),c.playfair_square('IIG'))
  with self.assertRaises(ValueError):c.playfair_square('')

 def test_12_playfair_preparation_repeat_x_ij_and_preserved_fillers(self):
  for text,prepared in [('BALLOON','BALXLOON'),('XX','XQXQ'),('X','XQ'),('JIG','IXIG'),('','')]:
   self.assertEqual(c.playfair_prepare(text),prepared)
  for text in ['XXXXX','JIG','BALLOON','HELLOX','XQX','AXAX']:
   cipher,prepared=c.playfair_encrypt(text,'PLAYFAIREXAMPLE')
   self.assertEqual(c.playfair_decrypt(cipher,'PLAYFAIREXAMPLE'),prepared)
   self.assertEqual(len(prepared)%2,0)
   self.assertTrue(all(prepared[i]!=prepared[i+1] for i in range(0,len(prepared),2)))

 def test_13_playfair_all_three_rules_and_published_vector(self):
  key='PLAYFAIREXAMPLE'
  for plain,cipher in [('PL','LA'),('PI','IB'),('HI','BM')]:
   self.assertEqual(c.playfair_encrypt(plain,key)[0],cipher)
   self.assertEqual(c.playfair_decrypt(cipher,key),plain)
  cipher,prepared=c.playfair_encrypt('HIDETHEGOLDINTHETREESTUMP',key)
  self.assertEqual(cipher,'BMODZBXDNABEKUDMUIXMMOUVIF')
  self.assertEqual(prepared,'HIDETHEGOLDINTHETREXESTUMP')
  self.assertEqual(c.playfair_decrypt(cipher,key),prepared)
  with self.assertRaises(ValueError):c.playfair_decrypt('ABC',key)

 def test_14_hill_validity_and_real_modular_inverse(self):
  key=[[3,3],[2,5]];inverse=c.hill_inverse(key)
  self.assertEqual(inverse,[[15,17],[20,9]])
  self.assertEqual([[sum(key[r][j]*inverse[j][col] for j in range(2))%26 for col in range(2)] for r in range(2)],[[1,0],[0,1]])
  for bad in [[[2,0],[0,1]],[[13,0],[0,1]],[[1,2],[2,4]],[[1,2,3],[4,5]],[[1]],None]:
   with self.assertRaises(ValueError):c.hill_encrypt('AB',bad)
  with self.assertRaises(TypeError):c.hill_encrypt('AB',[[1.0,0],[0,1]])

 def test_15_hill_two_by_two_worked_values(self):
  key=[[3,3],[2,5]]
  self.assertEqual(c.hill_encrypt('HELP',key),('HIAT','HELP'))
  self.assertEqual(c.hill_decrypt('HIAT',key),'HELP')
  self.assertEqual([3*7+3*4,2*7+5*4],[33,34])
  self.assertEqual(c.hill_encrypt('HELP',[[29,29],[28,31]])[0],'HIAT')

 def test_16_hill_three_by_three_and_random_inverse_properties(self):
  key=[[6,24,1],[13,16,10],[20,17,15]]
  self.assertEqual(c.determinant(key),441)
  self.assertEqual(c.hill_encrypt('ACT',key),('POH','ACT'));self.assertEqual(c.hill_encrypt('CAT',key)[0],'FIN')
  self.assertEqual(c.hill_inverse(key),[[8,5,10],[21,8,21],[21,12,8]])
  rng=random.Random(2026)
  for n in [2,3]:
   count=0
   while count<30:
    matrix=[[rng.randrange(26) for _ in range(n)] for _ in range(n)]
    if math.gcd(c.determinant(matrix),26)!=1:continue
    inverse=c.hill_inverse(matrix)
    identity=[[sum(matrix[r][j]*inverse[j][col] for j in range(n))%26 for col in range(n)] for r in range(n)]
    self.assertEqual(identity,[[int(r==col) for col in range(n)] for r in range(n)])
    cipher,prepared=c.hill_encrypt('TESTWITHENDINGX',matrix)
    self.assertEqual(c.hill_decrypt(cipher,matrix),prepared);count+=1

 def test_17_hill_padding_is_explicit_not_guessed_away(self):
  key=[[6,24,1],[13,16,10],[20,17,15]]
  cipher,prepared=c.hill_encrypt('HI',key)
  self.assertEqual(prepared,'HIX');self.assertEqual(c.hill_decrypt(cipher,key),'HIX')
  cipher,prepared=c.hill_encrypt('HELLOX',key)
  self.assertEqual(prepared,'HELLOX');self.assertEqual(c.hill_decrypt(cipher,key),'HELLOX')
  with self.assertRaises(ValueError):c.hill_decrypt('A',key)
  self.assertEqual(c.hill_encrypt('',key),('',''))

 def test_18_rail_fence_known_vector_unequal_rows_and_identity(self):
  plain='WEAREDISCOVEREDRUNATONCE';cipher='WECRUOERDSOEERNTNEAIVDAC'
  self.assertEqual(c.rail_encrypt(plain,3),cipher);self.assertEqual(c.rail_decrypt(cipher,3),plain)
  self.assertEqual(sorted(plain),sorted(cipher));self.assertEqual(c.rail_encrypt('ABC',1),'ABC')
  rng=random.Random(19)
  for length in range(2,50):
   text=''.join(rng.choices(c.ALPHABET,k=length))
   for rails in range(1,min(7,length)+1):self.assertEqual(c.rail_decrypt(c.rail_encrypt(text,rails),rails),text)
  for rails in [0,4]:
   with self.assertRaises(ValueError):c.rail_encrypt('ABC',rails)
  self.assertEqual(c.rail_encrypt('',1),'')

 def test_19_letter_pad_vector_lengths_and_each_symbol_bijection(self):
  self.assertEqual(c.pad_letters('HELLO','XMCKL'),'EQNVZ')
  self.assertEqual(c.pad_letters('EQNVZ','XMCKL',True),'HELLO')
  with self.assertRaises(ValueError):c.pad_letters('HELLO','KEY')
  for symbol in c.ALPHABET:
   self.assertEqual(set(c.pad_letters(symbol,k) for k in c.ALPHABET),set(c.ALPHABET))
  self.assertIn('public fixed classroom data',self.text);self.assertIn('not a proof of ideal',self.text)

 def test_20_xor_roundtrip_reuse_relation_and_bad_lengths(self):
  rng=random.Random(13)
  for n in range(1,65):
   p1=rng.randbytes(n);p2=rng.randbytes(n);key=rng.randbytes(n)
   c1=c.xor_bytes(p1,key);c2=c.xor_bytes(p2,key)
   self.assertEqual(c.xor_bytes(c1,key),p1)
   self.assertEqual(c.xor_bytes(c1,c2),c.xor_bytes(p1,p2))
  with self.assertRaises(ValueError):c.xor_bytes(b'ABC',b'A')
  with self.assertRaises(TypeError):c.xor_bytes('ABC',b'ABC')
  self.assertIn('does not stop active modification',self.text)

 def test_21_des_known_answer_trace_and_zero_vector(self):
  key=bytes.fromhex('133457799BBCDFF1');plain=bytes.fromhex('0123456789ABCDEF')
  trace=c.des_trace(plain,key)
  self.assertEqual(trace['result'].hex().upper(),'85E813540F0AB405')
  self.assertEqual(c.des_block(trace['result'],key,True),plain)
  self.assertEqual(trace['initial'],'CC00CCFFF0AAF0AA')
  self.assertEqual(trace['rounds'][1],{'round':1,'left':'F0AAF0AA','right':'EF4A6544','subkey':'1B02EFFC7072'})
  self.assertEqual(len(trace['rounds']),17)
  self.assertEqual(trace['rounds'],self.u['worked_data']['des_rounds'])
  self.assertEqual(c.des_block(bytes(8),bytes(8)).hex().upper(),'8CA64DE9C1B123A7')

 def test_22_actual_independent_openssl_66_blocks_both_directions(self):
  config=Path('/etc/ssl/openssl.cnf');before=config.read_bytes()
  reference=check_des();self.assertEqual(reference,self.u['runtime_evidence']['independent_des_reference'])
  self.assertEqual(reference['compared_blocks'],66);self.assertEqual(reference['directions'],['encrypt','decrypt'])
  self.assertEqual(config.read_bytes(),before);self.assertFalse(reference['certification_claim'])

 def test_23_des_tables_inverse_permutations_parity_and_key_widths(self):
  self.assertEqual(sorted(c.IP),list(range(1,65)));self.assertEqual(sorted(c.FP),list(range(1,65)))
  for i in range(64):self.assertEqual(c.permute(c.permute(1<<i,c.IP,64),c.FP,64),1<<i)
  self.assertEqual(sorted(c.P),list(range(1,33)))
  self.assertEqual(set(c.PC1),set(range(1,65))-set(range(8,65,8)))
  self.assertEqual((len(c.PC1),len(c.PC2),len(c.SHIFTS)),(56,48,16));self.assertEqual(sum(c.SHIFTS),28)
  for box in c.SBOXES:
   self.assertEqual(len(box),4)
   for row in box:self.assertEqual(sorted(row),list(range(16)))
  key=bytes.fromhex('133457799BBCDFF1');toggle=bytes(b^1 for b in key)
  self.assertEqual(c.des_round_keys(key),c.des_round_keys(toggle))
  self.assertTrue(all(k.bit_length()<=48 for k in c.des_round_keys(key)))

 def test_24_des_roundtrip_complement_property_and_invalid_blocks(self):
  rng=random.Random(46)
  for _ in range(20):
   key=rng.randbytes(8);plain=rng.randbytes(8);cipher=c.des_block(plain,key)
   self.assertEqual(c.des_block(cipher,key,True),plain)
   complement=lambda b:bytes(x^255 for x in b)
   self.assertEqual(c.des_block(complement(plain),complement(key)),complement(cipher))
  for block,key in [(b'123',b'12345678'),(b'12345678',b'123'),('12345678',b'12345678')]:
   with self.assertRaises(ValueError):c.des_block(block,key)

 def test_25_lsb_real_pixel_fixture_capacity_and_corrupt_header(self):
  cover=bytes([120,96,180])*64;stego=c.lsb_embed(cover,b'GTU')
  self.assertEqual(c.lsb_extract(stego),b'GTU')
  self.assertEqual(sum(a!=b for a,b in zip(cover,stego)),13)
  self.assertEqual(max(abs(a-b) for a,b in zip(cover,stego)),1)
  self.assertEqual(c.lsb_extract(c.lsb_embed(bytes(16),b'')),b'')
  with self.assertRaises(ValueError):c.lsb_embed(bytes(39),b'GTU')
  with self.assertRaises(ValueError):c.lsb_extract(bytes([1])*16)
  with self.assertRaises(ValueError):c.lsb_extract(stego[:39])
  altered=bytearray(stego);altered[16]^=1
  self.assertNotEqual(c.lsb_extract(bytes(altered)),b'GTU')

 def test_26_all_twelve_real_outputs_and_public_helper_hash(self):
  self.assertEqual(execute_all(),self.u['programs'])
  self.assertEqual(hashlib.sha256(HELPER.read_bytes()).hexdigest(),self.u['runtime_evidence']['helper_sha256'])
  for p in self.u['programs']:
   compile(p['code']['en'],p['id'],'exec');ast.parse(p['code']['en'])
   self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])
   self.assertIn('expl',p)

 def test_27_safe_html_and_all_program_diagram_links(self):
  linked=set();diagrams=set()
  for section in self.u['notes']:
   for item in section['items']:
    Fragment().finish(item['body']['en']);linked.update(item.get('programs',[]))
    if item.get('diagram'):diagrams.add(item['diagram'])
    self.assertNotIn('@@',item['body']['en'])
  self.assertEqual(linked,set(self.p));self.assertEqual(diagrams,set(TITLES))
  for p in self.u['programs']:Fragment().finish(p['expl']['en'])
  for g in self.u['syntax']:
   for e in g['items']:Fragment().finish(e['terms']['en'])
  for g in self.u['viva']:
   for e in g['items']:Fragment().finish(e['a']['en'])

 def test_28_ten_self_contained_svg_font_bounds_raster_and_review_sheets(self):
  images=[]
  for d in self.u['diagrams']:
   raw=(SUBJ_DIR/d['file']).read_text();root=ET.fromstring(raw);w,h=map(float,root.get('viewBox').split()[2:])
   self.assertEqual(w,360)
   for bad in ['<script','<style','<marker','<foreignObject','<image','href=']:self.assertNotIn(bad,raw)
   for node in root.iter('{http://www.w3.org/2000/svg}text'):
    size=float(node.get('font-size','12'))
    font_name='DejaVuSansMono.ttf' if 'Mono' in node.get('font-family','') else 'DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+font_name,round(size*10))
    for piece in list(node) or [node]:
     txt=''.join(piece.itertext());length=font.getlength(txt)/10;x=float(piece.get('x',node.get('x')))
     anchor=piece.get('text-anchor',node.get('text-anchor','start'))
     left=x-length/2 if anchor=='middle' else x-length if anchor=='end' else x
     self.assertGreaterEqual(left,1,(d['id'],txt));self.assertLessEqual(left+length,w-1,(d['id'],txt))
     y=float(piece.get('y',node.get('y','0')));self.assertGreaterEqual(y-size,-1,(d['id'],txt));self.assertLessEqual(y+size/3,h+1,(d['id'],txt))
   png=resvg_py.svg_to_bytes(svg_string=clean_svg(raw),zoom=1.25,font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',sans_serif_family='DejaVu Sans',monospace_family='DejaVu Sans Mono',skip_system_fonts=True)
   image=Image.open(io.BytesIO(bytes(png))).convert('RGB');self.assertGreater(len(image.getcolors(image.width*image.height)),20);images.append((d['id'],image))
  for start in [0,4,8]:
   group=images[start:start+4];height=max(im.height for name,im in group)+42
   sheet=Image.new('RGB',(960,height*((len(group)+1)//2)+16),'#EAE4F1');draw=ImageDraw.Draw(sheet)
   for i,(name,image) in enumerate(group):
    x=i%2*480+15;y=i//2*height+30;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(image,(x,y))
   sheet.save(ROOT/f'preview/DI05007021_unit2_diagrams_{start//4+1}.png')

 def test_29_six_preview_views_real_explanations_and_hidden_gu(self):
  result=execute_preview(PREVIEW);self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),10)
  self.assertEqual(result['views']['exam'].count('class="mk"'),16)
  for p in self.u['programs']:self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_30_exact_29_file_zip_and_twelve_extracted_example_runs(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),29);self.assertEqual(z.read('ciphers.py'),HELPER.read_bytes())
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
    trace=list(csv.DictReader(io.StringIO(z.read('des_trace.csv').decode())))
    self.assertEqual(len(trace),17);self.assertEqual(trace[-1]['Right32_hex'],'0A4CD995')
    z.extractall(td)
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en'])
     self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-E',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=12)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_31_offline_export_and_deterministic_complete_rebuild(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('Offline export')),patch('socket.socket',side_effect=AssertionError('Offline export')):
    out=export(Path(td)/'kit.zip')
   self.assertEqual(Path(out).read_bytes(),ZIP.read_bytes())
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit2.json',PREVIEW,ZIP]+[DIAG_DIR/(n+'.svg') for n in TITLES]
  before={p:p.read_bytes() for p in paths}
  r=subprocess.run([sys.executable,'tools/build_DI05007021_u2.py'],cwd=ROOT,text=True,capture_output=True,timeout=30)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,wanted in before.items():self.assertEqual(p.read_bytes(),wanted,str(p))

 def test_32_all_prior_776_content_files_and_public_units_preserved(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007021_u2.json').read_text());self.assertEqual(len(baseline),776)
  subject_rel='content/computer/sem5/DI05007021/subject.json'
  for rel,wanted in baseline.items():
   raw=(ROOT/rel).read_bytes()
   if rel==subject_rel:
    restored=json.loads(raw);self.assertEqual(restored['units'][1]['file'],'unit2.json')
    for spec in restored['units'][1:]:spec['file']=None
    raw=(json.dumps(restored,ensure_ascii=False,indent=1)+'\n').encode()
   self.assertEqual(hashlib.sha256(raw).hexdigest(),wanted,rel)
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertGreaterEqual(len(list((out/'subjects').glob('*.json'))),14)
   self.assertGreaterEqual(len(list((out/'units').glob('*.json'))),66)
   installed=[i for i in range(1,6) if (SUBJ_DIR/f'unit{i}.json').is_file()]
   for p in BASE.rglob('*.json'):
    rel=p.relative_to(BASE).as_posix()
    if rel=='catalog.json':continue
    if rel=='subjects/DI05007021.json':
     expected=json.loads(p.read_bytes());expected['available_units']=installed
     for spec in expected['units']:spec['file']=f"unit{spec['no']}.json" if spec['no'] in installed else None
     self.assertEqual(json.loads((out/rel).read_bytes()),expected)
    else:self.assertEqual((out/rel).read_bytes(),p.read_bytes(),rel)
   cat=json.loads((out/'catalog.json').read_bytes())
   old=json.loads((BASE/'catalog.json').read_bytes())
   self.assertEqual(cat['subjects'],old['subjects']);self.assertEqual(cat['branches'],old['branches'])
   for rel,wanted in cat['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)
   self.assertEqual(hashlib.sha256((out/'units/DI05007021_u1.json').read_bytes()).hexdigest(),'8848c814de7659bb4210ddea155e8c87642a0d66cd203c4261390c1c44c8c5b5')

 def test_33_original_suggested_practice_questions_and_answers(self):
  self.assertTrue(self.u['question_marks_are_suggested']);self.assertIn('not official past papers',self.u['question_provenance'])
  for i,((q,m,a),item,question) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(question,{'q':{'en':'Practice: '+q},'marks':m});self.assertIn(m,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')
  self.assertIn('not a guaranteed paper allocation',self.u['assessment_note']['en'])

 def test_34_no_secrets_binaries_network_or_production_claim(self):
  evidence=self.u['runtime_evidence']
  for name in ['external_packages_required','network_access_used','persistent_service','real_user_data_used','production_security_claim','fips_validation_claim','global_crypto_configuration_changed','fresh_pad_material_published']:
   self.assertFalse(evidence[name])
  for p in EXAMPLES:
   for bad in ['urllib','requests','socket','shell=True','os.system','https://','http://']:
    self.assertNotIn(bad,p['code']['en'])
  payload=PREVIEW.read_bytes()+(SUBJ_DIR/'unit2.json').read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for name in z.namelist():
    self.assertNotRegex(name,r'\.(exe|so|deb|dll|tar|gz)$');payload+=z.read(name)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'Private credential leaked')
  self.assertLess(ZIP.stat().st_size,25000)
  self.assertFalse((ROOT.parent/'php_root').exists())

if __name__=='__main__':unittest.main(verbosity=2)
