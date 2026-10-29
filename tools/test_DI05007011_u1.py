"""30 groups: hardware content, actual software, honest scope, UI and all-old-data regression."""
import ast,contextlib,csv,hashlib,html,io,json,os,re,socket,subprocess,sys,tempfile,unittest,zipfile
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
import hardware_u1_helper as lab
from subject_DI05007011 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007011_u1_notes import NOTES,PRACTICE,REFERENCE
from content_DI05007011_u1_programs import EXAMPLES,execute_all,HELPER,REFERENCE as REF_PATH
from content_DI05007011_u1_guides import GUIDES,COMPONENTS,PORTS
from diagrams_DI05007011_u1 import TITLES,port_icon
from export_app_content import clean_svg
from export_DI05007011_u1_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007011_unit1_preview.html';ZIP=ROOT/'preview/DI05007011_unit1_practicals.zip'
BASE=Path('/opt/repos/diplomaone-content/data')

class HardwareUnit1Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit1.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.plain=html.unescape(re.sub(r'<[^>]*>','',' '.join(strings(cls.u)))).lower()

 def test_01_pdf_provenance_and_official_scheme(self):
  self.assertIn('f53c78bc1058c42708ad909ca94f111c2757e1c3ac2d7a8a48784507c2b55915',(ROOT/'tools/syllabus_DI05007011.txt').read_text())
  self.assertEqual((self.s['code'],self.s['semester'],self.s['syllabus_year'],self.s['category']),('DI05007011',5,'2026-27','PCC'))
  self.assertEqual(self.s['teaching'],{'lecture':3,'tutorial':0,'practical':2})
  self.assertEqual(self.s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})
  self.assertEqual(len(self.s['practicals']),15)
  self.assertEqual(self.s['theory_rbt_percent'],{'remember':30,'understand':40,'apply':30,'analyze':0,'evaluate':0,'create':0})

 def test_02_only_approved_unit_one_and_correct_full_plan(self):
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage'],self.u['practical_numbers']),(1,7,16,[1,4]))
  self.assertEqual([u['hours'] for u in self.s['units']],[7,11,8,12,7]);self.assertEqual([u['weightage'] for u in self.s['units']],[16,25,18,25,16])
  self.assertEqual([u['file'] for u in self.s['units']],['unit1.json',None,None,None,None])
  self.assertEqual(sorted(p.name for p in SUBJ_DIR.glob('unit*.json')),['unit1.json'])
  self.assertIn('CO1',self.u['learning_outcomes'][0]['en']);self.assertEqual(self.u['tabs'],TABS)

 def test_03_english_only_no_priority_markers(self):
  def walk(o):
   if isinstance(o,dict):
    self.assertNotIn('gu',o);self.assertNotIn('key',o)
    for v in o.values():walk(v)
   elif isinstance(o,list):
    for v in o:walk(v)
   elif isinstance(o,str):self.assertNotRegex(o,r'[\u0a80-\u0aff]')
  walk(self.u);walk(self.s);self.assertEqual(self.s['languages'],['en'])

 def test_04_all_syllabus_terms_and_counts(self):
  self.assertEqual(sum(len(g['items']) for g in NOTES),18);self.assertEqual(sum(len(g['items']) for g in self.u['notes']),34)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams']),len(self.u['exam_questions'])),(4,11,16))
  self.assertEqual(sum(len(g['items']) for g in self.u['syntax']),14);self.assertEqual(sum(len(g['items']) for g in self.u['viva']),32)
  for term in ['microcomputer','minicomputer','mainframe','supercomputer','workstation','cloud','embedded','alu','control unit','motherboard','ram','rom','hdd','ssd','keyboard','mouse','monitor','smps','firmware','bios','uefi','cmos','battery','expansion','removable','cooling','speakers','webcam','wi-fi','bluetooth','usb','hdmi','rj45','vga','thunderbolt','specification']:
   self.assertTrue(term in self.plain,term)

 def test_05_taxonomy_and_pc_history_not_misleading(self):
  for term in ['not the first personal computer ever','not the same as a modern small-form-factor','do not arrange every row','deployment model','categories may overlap']:
   self.assertTrue(term in self.plain,term)
  self.assertTrue('august 1981' in self.plain)

 def test_06_cpu_roles_and_no_clock_core_speed_guarantee(self):
  for term in ['arithmetic','logical operations','instruction/control','registers','not a universal','not parts a student removes']:
   self.assertTrue(term in self.plain,term)

 def test_07_ram_firmware_cmos_rtc_distinctions(self):
  for term in ['volatile','updateable flash','chip is hardware','not the bios/uefi program itself','not the laptop’s main operating battery','modern settings may use nvram']:
   self.assertTrue(term in self.plain,term)
  self.assertTrue('raid describes a storage arrangement' in self.plain)
  self.assertTrue('m.2 is a form-factor/connector family' in self.plain)

 def test_08_connector_display_and_thunderbolt_distinctions(self):
  for term in ['led-backlit lcd','usb-c is a connector form','thunderbolt 1/2','mini displayport-style','3/4/5 use usb-c','traditional analog video','8p8c','trs/trrs','power delivery is negotiated']:
   self.assertTrue(term in self.plain,term)

 def test_09_physical_electrical_and_firmware_work_honestly_unperformed(self):
  e=self.u['runtime_evidence']
  for name in ['physical_PC_or_laptop_inspected','physical_components_or_ports_handled_tested','physical_practicals_1_4_completed','hardware_photographs_taken','electrical_voltage_measurements','SMPS_charger_monitor_opened','battery_or_component_insertion_removal','BIOS_UEFI_GUI_accessed','firmware_CMOS_TPM_or_security_settings_changed','drivers_or_OS_settings_changed']:
   self.assertIs(e[name],False,name)
  self.assertTrue('never open an smps/charger/monitor enclosure' in self.plain)
  self.assertTrue('do not improvise' in self.plain)

 def test_10_actual_readonly_inventory_matches_current_kernel_view(self):
  observed=lab.environment_inventory();self.assertEqual(observed,json.loads(self.p['hw1p01']['out']))
  self.assertEqual(observed,self.u['runtime_evidence']['sandbox_inventory'])
  self.assertEqual(observed['reported_logical_cpus'],os.cpu_count())
  mem=next(l for l in Path('/proc/meminfo').read_text().splitlines() if l.startswith('MemTotal:'))
  self.assertEqual(observed['kernel_MemTotal_bytes'],int(mem.split()[1])*1024)

 def test_11_no_physical_bios_or_private_identifier_inference(self):
  observed=lab.environment_inventory()
  self.assertFalse(observed['physical_components_inspected']);self.assertFalse(observed['BIOS_UEFI_or_CMOS_probed'])
  self.assertTrue('not physical' in observed['scope'])
  for forbidden in ['hostname','serial','mac_address','BIOS_version','battery_health']:self.assertNotIn(forbidden,observed)
  source=HELPER.read_text()
  for forbidden in ['platform.node(', 'socket.gethostname(', '/sys/class/dmi', 'dmidecode', 'subprocess.run(']:self.assertNotIn(forbidden,source)

 def test_12_real_capacity_arithmetic_and_invalid_values(self):
  self.assertEqual(16*2**30,17179869184)
  self.assertEqual(lab.decimal_gb_to_gib(512),Decimal('476.837158203125'))
  self.assertEqual(round(lab.decimal_gb_to_gib(512),3),Decimal('476.837'))
  for bad in [-1,'nan','Infinity','not a number',True]:
   with self.assertRaises(ValueError):lab.decimal_gb_to_gib(bad)
  self.assertEqual(lab.decimal_gb_to_gib(0),0)

 def test_13_explicit_connector_fixture_known_unknown_and_bad_rows(self):
  rows=[{'connector':'USB-C','video_documented':False},{'connector':'USB-C','video_documented':True}]
  result=lab.connector_fixture(rows)
  self.assertEqual(result,{'same_connector':True,'video_capability_varies_in_fixture':True,'charging_unspecified_count':2,'actual_ports_or_PD_negotiation_tested':False})
  for bad in [[],[{'connector':'USB-A','video_documented':True}],[{'connector':'USB-C'}],[{'connector':'USB-C','video_documented':1}]]:
   with self.assertRaises(ValueError):lab.connector_fixture(bad)

 def test_14_spec_fields_completeness_is_not_compatibility(self):
  for p in REFERENCE['profiles']:self.assertEqual(lab.missing_spec_fields(p),[])
  self.assertEqual(len(lab.missing_spec_fields({'processor':'Model only'})),9)
  invalid=dict(REFERENCE['profiles'][0]);invalid['source_url']='http://not-approved.test';invalid['checked_on']='not a date'
  self.assertEqual(set(lab.missing_spec_fields(invalid)),{'source_url','checked_on'})
  self.assertTrue('completeness is not accuracy,compatibility or benchmark proof' in self.plain)

 def test_15_dated_selected_manufacturer_profiles_no_variant_mixing(self):
  self.assertEqual(REFERENCE['checked_on'],'2026-10-29');self.assertFalse(REFERENCE['physical_devices_tested'])
  air,mini=REFERENCE['profiles'];self.assertEqual([air['id'],mini['id']],['air_m5_base','mini_m6_base'])
  self.assertIn('M5',air['processor']);self.assertIn('10-core',air['processor']);self.assertEqual(air['gpu'],'8-core integrated GPU')
  self.assertEqual(air['storage'],'512GB SSD');self.assertIn('13.6',air['display']);self.assertIn('2560x1664',air['display'])
  self.assertIn('M6',mini['processor']);self.assertIn('12-core',mini['processor']);self.assertEqual(mini['gpu'],'12-core integrated GPU')
  self.assertEqual(mini['storage'],'256GB SSD');self.assertIn('no built-in panel',mini['display'])
  self.assertTrue(all(p['os']=='macOS' and '16GB unified' in p['memory'] for p in [air,mini]))

 def test_16_source_checks_and_dated_platform_limit_not_latest_guarantee(self):
  self.assertEqual(len(REFERENCE['source_checks']),2)
  for check in REFERENCE['source_checks']:
   self.assertRegex(check['html_sha256'],r'^[0-9a-f]{64}$');self.assertTrue(check['selected_first_column_reviewed'])
   self.assertFalse(check['raw_page_copied_into_kit']);self.assertEqual(check['checked_on'],'2026-10-29')
   self.assertTrue(check['url'].startswith('https://www.apple.com/'))
  self.assertTrue('not a claim of globally newest hardware' in self.plain)
  self.assertTrue('not a windows x86 bios/assembly guide' in self.plain)
  self.assertTrue('illustrative sample' in self.plain)

 def test_17_four_fresh_actual_outputs_and_source_hashes(self):
  self.assertEqual(execute_all(),self.u['programs'])
  e=self.u['runtime_evidence'];self.assertEqual(hashlib.sha256(HELPER.read_bytes()).hexdigest(),e['helper_sha256'])
  self.assertEqual(hashlib.sha256(REF_PATH.read_bytes()).hexdigest(),e['reference_json_sha256'])
  for p in EXAMPLES:
   compile(p['code']['en'],p['id'],'exec');self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78)

 def test_18_safe_html_and_all_linked_ids(self):
  programs=set();diagrams=set()
  for group in self.u['notes']:
   for item in group['items']:
    Fragment().finish(item['body']['en']);programs.update(item.get('programs',[]))
    if item.get('diagram'):diagrams.add(item['diagram'])
    self.assertNotIn('@@',item['body']['en'])
  self.assertEqual(programs,set(self.p));self.assertEqual(diagrams,set(TITLES))
  for p in self.u['programs']:Fragment().finish(p['expl']['en'])
  for g in self.u['syntax']:
   for item in g['items']:Fragment().finish(item['terms']['en'])
  for g in self.u['viva']:
   for item in g['items']:Fragment().finish(item['a']['en'])

 def test_19_eleven_svgs_real_font_bounds_raster_and_sheets(self):
  images=[]
  for d in self.u['diagrams']:
   raw=(SUBJ_DIR/d['file']).read_text();root=ET.fromstring(raw);w,h=map(float,root.get('viewBox').split()[2:]);self.assertEqual(w,360)
   for bad in ['<image','<script','<style','<marker','<foreignObject','href=']:self.assertNotIn(bad,raw)
   for node in root.iter('{http://www.w3.org/2000/svg}text'):
    size=float(node.get('font-size','12'));name='DejaVuSans-Bold.ttf' if node.get('font-weight')=='bold' else 'DejaVuSans.ttf'
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name,round(size*10))
    for piece in list(node) or [node]:
     txt=''.join(piece.itertext());length=font.getlength(txt)/10;x=float(piece.get('x',node.get('x')))
     anchor=piece.get('text-anchor',node.get('text-anchor','start'));left=x-length/2 if anchor=='middle' else x-length if anchor=='end' else x
     self.assertGreaterEqual(left,1,(d['id'],txt));self.assertLessEqual(left+length,w-1,(d['id'],txt))
     y=float(piece.get('y',node.get('y','0')));self.assertGreaterEqual(y-size,-1,(d['id'],txt));self.assertLessEqual(y+size/3,h+1,(d['id'],txt))
   png=resvg_py.svg_to_bytes(svg_string=clean_svg(raw),zoom=1.25,font_dirs=['/usr/share/fonts/truetype/dejavu'],font_family='DejaVu Sans',sans_serif_family='DejaVu Sans',skip_system_fonts=True)
   im=Image.open(io.BytesIO(bytes(png))).convert('RGB');self.assertGreater(len(im.getcolors(im.width*im.height)),20);images.append((d['id'],im))
  for start in [0,4,8]:
   group=images[start:start+4];height=max(im.height for name,im in group)+42
   sheet=Image.new('RGB',(960,height*((len(group)+1)//2)+16),'#EAE4F1');draw=ImageDraw.Draw(sheet)
   for i,(name,im) in enumerate(group):
    x=i%2*480+15;y=i//2*height+30;draw.text((x,y-22),name,fill='#4C1C85');sheet.paste(im,(x,y))
   sheet.save(ROOT/f'preview/DI05007011_unit1_diagrams_{start//4+1}.png')

 def test_20_schematic_recognition_not_photos_or_pinouts(self):
  self.assertEqual(port_icon('VGA',0,0).count('<circle'),15)
  self.assertEqual(port_icon('Ethernet',0,0).count('<rect'),8)
  self.assertTrue('not electrical pinouts' in self.plain)
  self.assertTrue('not a photograph,service manual' in self.plain)

 def test_21_six_preview_views_outputs_explanations_and_hidden_gu(self):
  result=execute_preview(PREVIEW);self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),11);self.assertEqual(result['views']['exam'].count('class="mk"'),16)
  for p in self.u['programs']:self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_22_seventeen_file_kit_and_all_four_extracted_actual_runs(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),17)
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    self.assertEqual(z.read('hardware_lab.py'),HELPER.read_bytes());self.assertEqual(z.read('reference_specs.json'),REF_PATH.read_bytes())
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
    for name,expected in [('components.csv',len(COMPONENTS)+1),('ports.csv',len(PORTS)+1),('specification.csv',13)]:
     rows=list(csv.reader(io.StringIO(z.read(name).decode())));self.assertEqual(len(rows),expected)
     self.assertTrue(all(all(not x for x in row[1:]) for row in rows[1:]))
    for name,text in GUIDES.items():self.assertEqual(z.read(name).decode(),text)
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en']);self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
    z.extractall(td)
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-E',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=10)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_23_offline_kit_export_does_not_probe_or_execute(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('Offline export')),patch('socket.socket',side_effect=AssertionError('Offline export')),patch('hardware_u1_helper.environment_inventory',side_effect=AssertionError('Use stored output only')):
    out=export(Path(td)/'kit.zip')
   self.assertEqual(Path(out).read_bytes(),ZIP.read_bytes())

 def test_24_byte_identical_complete_rebuild(self):
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit1.json',PREVIEW,ZIP,REF_PATH]+[DIAG_DIR/(n+'.svg') for n in TITLES]
  before={p:p.read_bytes() for p in paths}
  r=subprocess.run([sys.executable,'tools/build_DI05007011_u1.py'],cwd=ROOT,text=True,capture_output=True,timeout=20)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,raw in before.items():self.assertEqual(p.read_bytes(),raw,str(p))

 def test_25_all_818_prior_source_files_byte_identical(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007011.json').read_text());self.assertEqual(len(baseline),818)
  for rel,wanted in baseline.items():self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),wanted,rel)

 def test_26_all_69_old_public_units_and_14_subjects_preserved(self):
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr);self.assertEqual((len(list((out/'subjects').glob('*.json'))),len(list((out/'units').glob('*.json')))),(15,70))
   for p in BASE.rglob('*.json'):
    if p.name!='catalog.json':self.assertEqual((out/p.relative_to(BASE)).read_bytes(),p.read_bytes(),str(p))
   old=json.loads((BASE/'catalog.json').read_bytes());new=json.loads((out/'catalog.json').read_bytes())
   for code,value in old['subjects'].items():self.assertEqual(new['subjects'][code],value)
   for branch in old['branches']:
    actual=next(x for x in new['branches'] if x['key']==branch['key']);expected=json.loads(json.dumps(branch))
    if branch['key']=='computer':expected['semesters']['5']=['DI05007011','DI05007021']
    self.assertEqual(actual,expected)
   self.assertEqual(new['subjects']['DI05007011']['name'],{'en':'Computer Hardware Architecture and System Maintenance'})
   self.assertEqual(new['subjects']['DI05007011']['languages'],['en'])
   subject=json.loads((out/'subjects/DI05007011.json').read_text());self.assertEqual(subject['available_units'],[1])
   for rel,wanted in new['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)
   unit=json.loads((out/'units/DI05007011_u1.json').read_bytes())
   self.assertEqual(unit['svgs'],{n:clean_svg((DIAG_DIR/(n+'.svg')).read_text()) for n in TITLES})

 def test_27_original_answered_practice_suggested_marks_only(self):
  self.assertTrue(self.u['question_marks_are_suggested']);self.assertIn('not official past papers',self.u['question_provenance'])
  for i,((q,marks,a),item,question) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(question,{'q':{'en':'Practice: '+q},'marks':marks});self.assertIn(marks,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')

 def test_28_no_credentials_binaries_or_raw_manufacturer_images(self):
  payload=PREVIEW.read_bytes()+(SUBJ_DIR/'unit1.json').read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for name in z.namelist():
    self.assertNotRegex(name,r'\.(exe|so|dll|deb|tar|gz|iso|img|pem|der|jpg|png|webp)$');payload+=z.read(name)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'Credential leaked')
  self.assertLess(ZIP.stat().st_size,25000)

 def test_29_no_unrelated_previous_material_or_app_code_changed(self):
  import sys
  sys.path.insert(0,str(ROOT/'tools'));from sync_code import skip
  clone=Path('/opt/repos/diplomaone-app')
  for base in [ROOT/'app',ROOT/'content']:
   for p in base.rglob('*'):
    if not p.is_file():continue
    rel=str(p.relative_to(ROOT))
    if skip(rel) or rel.startswith('content/computer/sem5/DI05007011/'):continue
    if (clone/rel).is_file():self.assertEqual(p.read_bytes(),(clone/rel).read_bytes(),rel)

 def test_30_guided_scope_and_no_privileged_network_physical_operations(self):
  self.assertEqual(len(GUIDES),2)
  self.assertTrue('NOT executed here' in GUIDES['guides/component_and_port_identification.md'])
  self.assertTrue('No voltage values' in GUIDES['guides/component_and_port_identification.md'])
  self.assertTrue('not a full assembly/repair guide' in GUIDES['guides/component_and_port_identification.md'])
  for p in EXAMPLES:
   ast.parse(p['code']['en'])
   for bad in ['requests','urllib.request','socket','shell=True','sudo','dmidecode','os.system','subprocess.Popen']:
    self.assertNotIn(bad,p['code']['en'])
  self.assertFalse((ROOT.parent/'php_root').exists())

if __name__=='__main__':unittest.main(verbosity=2)
