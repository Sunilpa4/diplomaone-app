"""36 groups: honest models, real offline/loopback evidence, preservation and UI."""
import ast,collections,csv,hashlib,html,io,json,math,os,re,socket,ssl,stat,struct,subprocess,sys,tempfile,threading,unittest,zipfile
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import resvg_py
# Maintainer import name differs from the public ZIP's pki_lab.py.
import infosec_u3_lab
sys.modules.setdefault('pki_lab',infosec_u3_lab)
import infosec_u4_models as model
import infosec_u4_packets as packets
import infosec_u4_localnet as localnet
from subject_DI05007021 import ROOT,SUBJ_DIR,DIAG_DIR,TABS
from content_DI05007021_u4_notes import NOTES,PRACTICE
from content_DI05007021_u4_programs import EXAMPLES,execute_all,HELPERS
from content_DI05007021_u4_guides import GUIDES
from diagrams_DI05007021_u4 import TITLES
from export_app_content import clean_svg
from export_DI05007021_u4_practicals import export
from test_DI04000031_u1 import Fragment,execute_preview,strings
PREVIEW=ROOT/'preview/DI05007021_unit4_preview.html';ZIP=ROOT/'preview/DI05007021_unit4_practicals.zip'
FIXTURE=ROOT/'tools/fixtures_DI05007021_u4/synthetic.pcap';BASE=Path('/opt/repos/diplomaone-content/data')

def unpack_pcap(raw):
 header=struct.unpack('<IHHIIII',raw[:24]);rows=[];offset=24
 while offset<len(raw):
  sec,usec,length,original=struct.unpack('<IIII',raw[offset:offset+16]);offset+=16
  frame=raw[offset:offset+length];offset+=length
  assert len(frame)==length==original
  rows.append((sec,usec,frame))
 assert offset==len(raw)
 return header,rows

def assemble(rows):
 raw=bytearray(FIXTURE.read_bytes()[:24])
 for sec,usec,frame in rows:raw+=struct.pack('<IIII',sec,usec,len(frame),len(frame))+frame
 return bytes(raw)

def ones_sum(data):
 if len(data)%2:data+=b'\0'
 total=0
 for i in range(0,len(data),2):total+=(data[i]<<8)|data[i+1]
 while total>65535:total=(total&65535)+(total>>16)
 return total

class Unit4Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.u=json.loads((SUBJ_DIR/'unit4.json').read_text());cls.s=json.loads((SUBJ_DIR/'subject.json').read_text())
  cls.p={p['id']:p for p in cls.u['programs']};cls.text=' '.join(strings(cls.u)).lower();cls.plain=html.unescape(re.sub(r'<[^>]*>','',cls.text))
  cls.system={p:p.read_bytes() for p in [Path('/etc/ssl/openssl.cnf'),Path('/etc/ssl/certs/ca-certificates.crt')] if p.is_file()}
  cls.addresses=subprocess.run(['ip','-j','address'],check=True,capture_output=True).stdout
  cls.routes=subprocess.run(['ip','-j','route'],check=True,capture_output=True).stdout

 def test_01_official_scheme_co4_and_practicals(self):
  self.assertEqual((self.u['unit'],self.u['hours'],self.u['weightage'],self.u['practical_numbers']),(4,9,20,[7,8,9,10]))
  self.assertIn('CO4',self.u['learning_outcomes'][0]['en'])
  self.assertEqual((self.s['semester'],self.s['syllabus_year']),(5,'2026-27'))
  self.assertEqual(self.s['exam'],{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4})

 def test_02_first_four_and_other_installed_approved_units(self):
  installed=[i for i in range(1,6) if (SUBJ_DIR/f'unit{i}.json').is_file()]
  self.assertTrue({1,2,3,4}.issubset(installed))
  self.assertEqual([x['file'] for x in self.s['units']],[f'unit{i}.json' if i in installed else None for i in range(1,6)])
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

 def test_04_all_topics_and_counts(self):
  self.assertEqual(sum(len(g['items']) for g in NOTES),18);self.assertEqual(sum(len(g['items']) for g in self.u['notes']),34)
  self.assertEqual((len(self.u['programs']),len(self.u['diagrams']),len(self.u['exam_questions'])),(12,10,16))
  self.assertEqual(sum(len(g['items']) for g in self.u['syntax']),14);self.assertEqual(sum(len(g['items']) for g in self.u['viva']),36)
  for term in ['security zone','dmz','internet','intranet','vlan','tunneling','packet filtering','stateful inspection','application-level gateway','circuit-level gateway','next-generation firewall','intruder','components','hids','nids','advantages','disadvantages']:
   self.assertTrue(term in self.plain,term)

 def test_05_evidence_classes_not_false_product_execution(self):
  e=self.u['runtime_evidence'];self.assertTrue(e['TShark_offline_executed']);self.assertTrue(e['TLS_handshake_performed'])
  for name in ['Wireshark_GUI_executed','live_packet_capture_performed','Packet_Tracer_executed','Snort_Suricata_or_NGFW_executed','kernel_firewall_changed','switch_VLAN_or_router_configured','network_namespace_created','public_network_targets_used','persistent_service','host_capture_privileges_enabled','mutual_TLS_performed']:
   self.assertIs(e[name],False,name)
  self.assertEqual(set(e['practical_execution_scope']),{'7','8','9','10'})
  self.assertTrue('not substitutes represented as successful packet tracer execution' in self.plain)

 def test_06_logical_dmz_exact_allow_deny_matrix(self):
  cases=[(model.Flow('192.0.2.10','198.51.100.10',50000,80),True),
   (model.Flow('192.0.2.10','203.0.113.20',50000,80),False),
   (model.Flow('198.51.100.10','203.0.113.20',45000,5432),True),
   (model.Flow('198.51.100.10','203.0.113.21',45000,5432),False)]
  for flow,wanted in cases:self.assertEqual(model.decide(flow)[0],wanted)
  self.assertFalse(model.decide(model.Flow('192.0.2.10','198.51.100.10',50000,22))[0])

 def test_07_order_default_deny_and_invalid_policy_inputs(self):
  flow=model.Flow('192.0.2.10','198.51.100.10',50000,80)
  allow=model.Rule('allow','0.0.0.0/0','198.51.100.0/24','TCP',80,'allow')
  deny=model.Rule('deny','192.0.2.10/32','198.51.100.10/32','TCP',80,'deny')
  self.assertFalse(model.decide(flow,[deny,allow])[0]);self.assertTrue(model.decide(flow,[allow,deny])[0]);self.assertFalse(model.decide(flow,[])[0])
  for port in [0,65536,True]:
   with self.assertRaises(ValueError):model.Flow('192.0.2.10','198.51.100.10',port,80)
  with self.assertRaises(ValueError):model.Rule('x','0.0.0.0/0','0.0.0.0/0','TCP',80,'permit-all')
  with self.assertRaises(ValueError):model.Flow('::1','198.51.100.10',50000,80)

 def test_08_stateful_direction_handshake_expiry_reset_and_clock(self):
  flow=model.Flow('192.0.2.10','198.51.100.10',50000,80);s=model.StatefulModel(ttl=5)
  self.assertFalse(s.observe(flow.reverse(),'DATA',0));self.assertTrue(s.observe(flow,'SYN',1))
  self.assertFalse(s.observe(flow,'SYNACK',2));self.assertFalse(s.observe(flow.reverse(),'DATA',2))
  self.assertTrue(s.observe(flow.reverse(),'SYNACK',3));self.assertFalse(s.observe(flow.reverse(),'ACK',3))
  self.assertTrue(s.observe(flow,'ACK',4));self.assertTrue(s.observe(flow.reverse(),'DATA',5))
  self.assertFalse(s.observe(flow.reverse(),'DATA',11));self.assertFalse(s.sessions)
  self.assertTrue(s.observe(flow,'SYN',12));self.assertTrue(s.observe(flow.reverse(),'RST',13));self.assertFalse(s.sessions)
  for event in ['ESTABLISHED','ANY']:
   with self.assertRaises(ValueError):s.observe(flow,event,14)
  for now in [float('nan'),float('inf'),-1,1]:
   with self.assertRaises(ValueError):s.observe(flow,'SYN',now)

 def test_09_vlan_membership_and_reserved_ids_not_real_forwarding(self):
  self.assertTrue(model.vlan_l2_allowed(10,10));self.assertFalse(model.vlan_l2_allowed(10,20))
  for bad in [0,4095,-1,True,'10']:
   with self.assertRaises(ValueError):model.vlan_l2_allowed(bad,10)
  self.assertTrue('tag bytes in a file do not prove a switch enforced segmentation' in self.plain)

 def test_10_frozen_pcap_header_records_origin_and_sha(self):
  raw=FIXTURE.read_bytes();self.assertEqual(raw,packets.pcap_bytes())
  header,rows=unpack_pcap(raw);self.assertEqual(header,(0xa1b2c3d4,2,4,0,0,65535,1))
  self.assertEqual(len(rows),16);self.assertEqual(len(raw),1373)
  self.assertEqual([r[1] for r in rows],[i*20000 for i in range(16)])
  self.assertEqual(hashlib.sha256(raw).hexdigest(),self.u['runtime_evidence']['synthetic_pcap_sha256'])
  self.assertTrue('NOT live capture' in self.u['runtime_evidence']['pcap_origin'])

 def test_11_independent_ip_tcp_udp_checksum_arithmetic(self):
  _,rows=unpack_pcap(FIXTURE.read_bytes());counts=collections.Counter()
  for sec,usec,frame in rows:
   kind=struct.unpack('!H',frame[12:14])[0];offset=18 if kind==0x8100 else 14
   if kind==0x0806:continue
   ip=frame[offset:];length=struct.unpack('!H',ip[2:4])[0];ip=ip[:length]
   self.assertEqual(ones_sum(ip[:20]),65535)
   proto=ip[9];segment=ip[20:];pseudo=ip[12:20]+struct.pack('!BBH',0,proto,len(segment))
   self.assertEqual(ones_sum(pseudo+segment),65535)
   counts[proto]+=1
  self.assertEqual(counts,{6:10,17:4})

 def test_12_actual_tshark_version_and_checksum_enumeration(self):
  self.assertEqual(packets.tshark_version(),self.u['runtime_evidence']['tshark'])
  r=subprocess.run(['tshark','-G','values'],check=True,text=True,capture_output=True,timeout=15)
  for field in ['ip.checksum.status','tcp.checksum.status','udp.checksum.status']:
   self.assertIn('V\t'+field+'\t1\tGood',r.stdout)
  self.assertEqual(self.u['runtime_evidence']['checksum_status_reference'],{'Good':1,'Bad':0,'Unverified':2})

 def test_13_actual_offline_protocol_counts_and_no_malformed_packets(self):
  rows=packets.dissect(['frame.number','_ws.col.Protocol'])
  self.assertEqual(len(rows),16)
  self.assertEqual(dict(collections.Counter(r[1] for r in rows)),{'ARP':2,'DNS':2,'TCP':8,'HTTP':2,'UDP':2})
  for filt,count in [('arp',2),('dns',2),('tcp',10),('http',2),('udp',4),('vlan',2)]:self.assertEqual(len(packets.dissect(['frame.number'],filt)),count)
  self.assertEqual(packets.dissect(['frame.number'],'_ws.malformed'),[])

 def test_14_actual_tcp_handshake_sequence_and_endpoints(self):
  rows=packets.dissect(['frame.number','tcp.seq_raw','tcp.ack_raw','tcp.flags'],'tcp')
  self.assertEqual(rows[:3],[['5','1000','0','0x0002'],['6','2000','1001','0x0012'],['7','1001','2001','0x0010']])
  self.assertEqual(rows[3][0],'8');self.assertEqual(rows[-1][0],'14')
  self.assertEqual(packets.dissect(['frame.number'],'tcp.analysis.retransmission'),[])
  self.assertEqual(packets.dissect(['frame.number'],'tcp.analysis.lost_segment'),[])

 def test_15_actual_dns_http_and_real_8021q_tag_bytes(self):
  dns=packets.dissect(['dns.qry.name','dns.a'],'dns')
  self.assertEqual(dns,[['portal.diploma.test',''],['portal.diploma.test','198.51.100.10']])
  self.assertEqual(packets.dissect(['http.request.method','http.request.uri'],'http.request'),[['GET','/course']])
  self.assertEqual(packets.dissect(['http.response.code'],'http.response'),[['200']])
  self.assertEqual(packets.dissect(['frame.number','vlan.id'],'vlan'),[['15','10'],['16','20']])
  _,rows=unpack_pcap(FIXTURE.read_bytes())
  for index,vid in [(14,10),(15,20)]:self.assertEqual(struct.unpack('!HHH',rows[index][2][12:18]),(0x8100,vid,0x0800))

 def test_16_actual_good_checksums_and_detected_corruption(self):
  rows=packets.dissect(['ip.checksum.status','tcp.checksum.status','udp.checksum.status'],'ip')
  self.assertEqual(len(rows),14);self.assertTrue(all(v=='1' for row in rows for v in row if v))
  _,frames=unpack_pcap(FIXTURE.read_bytes())
  for index,byteoffset,field in [(4,14+8,'ip.checksum.status'),(7,14+20+20,'tcp.checksum.status'),(2,14+20+8,'udp.checksum.status')]:
   altered=list(frames);sec,usec,raw=altered[index];changed=bytearray(raw);changed[byteoffset]^=1
   altered[index]=(sec,usec,bytes(changed));values=packets.dissect([field],f'frame.number == {index+1}',assemble(altered))
   self.assertEqual(values,[['0']],field)

 def test_17_real_filter_mismatch_rejection_not_live_capture(self):
  self.assertEqual(len(packets.dissect(['frame.number'],'tcp.port == 80')),10)
  self.assertEqual(len(packets.dissect(['frame.number'],'http')),2)
  with self.assertRaises(subprocess.CalledProcessError) as caught:packets.dissect(['frame.number'],'tcp port 80')
  self.assertIn('was unexpected',caught.exception.stderr);self.assertIn('capture filter',caught.exception.stderr)
  self.assertIn('BPF_form_rejected_as_display_filter: True',self.p['sec4p12']['out'])

 def test_18_actual_owned_http_allow_and_deny_cleanup(self):
  for path,code in [('/course',200),('/admin',403)]:
   result=localnet.private_http(path);self.assertEqual(result['status'],code)
   for name in ['loopback_only','listener_closed','worker_stopped']:self.assertTrue(result[name])
  with self.assertRaises(ValueError):localnet.private_http('/unprepared')

 def test_19_actual_tls13_verified_server_relay_and_key_cleanup(self):
  result=localnet.private_tls_relay()
  self.assertEqual(result['tls_version'],'TLSv1.3');self.assertEqual(result['checked_hostname'],'portal.diploma.test')
  for name in ['echo_matches','certificate_required','loopback_only','listeners_closed','workers_stopped','temporary_keys_removed']:self.assertTrue(result[name])
  self.assertEqual(ssl.OPENSSL_VERSION,self.u['runtime_evidence']['python_ssl'])
  self.assertFalse(self.u['runtime_evidence']['mutual_TLS_performed'])

 def test_20_readonly_network_crypto_config_and_capture_privileges(self):
  self.assertEqual(subprocess.run(['ip','-j','address'],check=True,capture_output=True).stdout,self.addresses)
  self.assertEqual(subprocess.run(['ip','-j','route'],check=True,capture_output=True).stdout,self.routes)
  for p,raw in self.system.items():self.assertEqual(p.read_bytes(),raw)
  cap=next(l.split()[1] for l in Path('/proc/self/status').read_text().splitlines() if l.startswith('CapEff:'))
  self.assertEqual(int(cap,16),0)
  dump=Path('/usr/bin/dumpcap');self.assertFalse(dump.stat().st_mode&stat.S_ISUID)
  try:value=os.getxattr(dump,'security.capability')
  except OSError:value=b''
  self.assertFalse(value)

 def test_21_hids_owned_file_real_changes_and_baseline_limitation(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'own.conf';p.write_bytes(b'role=student\n');baseline=hashlib.sha256(p.read_bytes()).hexdigest()
   self.assertFalse(model.hids_check(p,baseline));p.write_bytes(b'role=staff\n');self.assertTrue(model.hids_check(p,baseline))
   p.write_bytes(b'role=student\n');self.assertFalse(model.hids_check(p,baseline))
  self.assertTrue('legitimate administrator update can also alert' in self.plain)

 def test_22_nids_rule_fixture_is_not_intrusion_confirmation(self):
  rows=[{'zone':'outside','destination_port':22},{'zone':'inside','destination_port':22},{'zone':'outside','destination_port':80}]
  self.assertEqual([model.nids_fixture_alert(r) for r in rows],[True,False,False])
  self.assertTrue(model.nids_fixture_alert({'zone':'outside','destination_port':22,'authorized_admin':True}))
  self.assertTrue('does not run snort/suricata' in self.plain)

 def test_23_real_confusion_matrix_arithmetic_not_product_benchmark(self):
  c=model.confusion_counts([True,True,False,True,False,False],[True,True,True,False,False,False])
  self.assertEqual(c,{'TP':2,'FP':1,'FN':1,'TN':2})
  self.assertEqual(round(c['TP']/(c['TP']+c['FP']),4),0.6667)
  self.assertEqual(round(c['FP']/(c['FP']+c['TN']),4),0.3333)
  self.assertEqual(model.confusion_counts([],[]),{'TP':0,'FP':0,'FN':0,'TN':0})
  with self.assertRaises(ValueError):model.confusion_counts([1],[True])
  with self.assertRaises(ValueError):model.confusion_counts([True],[])

 def test_24_all_twelve_fresh_outputs_and_helper_source_hashes(self):
  self.assertEqual(execute_all(),self.u['programs'])
  self.assertEqual({n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},self.u['runtime_evidence']['helper_sha256'])
  for p in EXAMPLES:
   compile(p['code']['en'],p['id'],'exec');ast.parse(p['code']['en'])
   self.assertLessEqual(max(map(len,p['code']['en'].splitlines())),78,p['id'])

 def test_25_four_guides_have_honest_provenance_and_expected_tests(self):
  self.assertEqual(len(GUIDES),4)
  for name,text in GUIDES.items():
   self.assertIn('NOT',text,name)
   self.assertNotRegex(name,r'\.(pkt|pka)$')
  self.assertIn('GUIDED ONLY',GUIDES['guides/packet_tracer_vlan.md'])
  self.assertIn('NOT executed',GUIDES['guides/packet_tracer_firewall.md'])
  self.assertIn('not observed results',GUIDES['guides/packet_tracer_firewall.md'])
  self.assertIn('not a replacement for a real state table',GUIDES['guides/packet_tracer_firewall.md'])

 def test_26_balanced_html_and_all_diagram_program_links(self):
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

 def test_27_ten_svg_bounds_raster_and_contact_sheets(self):
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
   sheet.save(ROOT/f'preview/DI05007021_unit4_diagrams_{start//4+1}.png')

 def test_28_all_six_preview_views_real_explanations_hidden_gu(self):
  result=execute_preview(PREVIEW);self.assertEqual(set(result['views']),set(TABS));self.assertEqual(result['languageHidden'],'none')
  self.assertEqual(result['views']['diagrams'].count('class="dcard"'),10);self.assertEqual(result['views']['exam'].count('class="mk"'),16)
  for p in self.u['programs']:self.assertIn(p['expl']['en'],result['views']['programs'])
  self.assertNotRegex(PREVIEW.read_text(),r'<(?:script|link|img)[^>]+(?:src|href)=')

 def test_29_exact_37_file_zip_pcap_manifest_and_twelve_extracted_runs(self):
  with tempfile.TemporaryDirectory() as td:
   with zipfile.ZipFile(ZIP) as z:
    self.assertEqual(len(z.namelist()),37)
    self.assertTrue(all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist()))
    for name,path in HELPERS.items():self.assertEqual(z.read(name),path.read_bytes())
    self.assertEqual(z.read('synthetic.pcap'),FIXTURE.read_bytes())
    self.assertEqual(json.loads(z.read('runtime.json')),self.u['runtime_evidence'])
    rows=list(csv.reader(io.StringIO(z.read('packet_manifest.csv').decode())))
    self.assertEqual(rows[0],self.u['worked_data']['manifest_fields']);self.assertEqual(rows[1:],self.u['worked_data']['manifest_rows'])
    for name,text in GUIDES.items():self.assertEqual(z.read(name).decode(),text)
    for p in self.u['programs']:
     self.assertEqual(z.read(p['id']+'.py').decode(),p['code']['en'])
     self.assertEqual(z.read('expected/'+p['id']+'.txt').decode(),p['out'])
    z.extractall(td)
   for p in self.u['programs']:
    r=subprocess.run([sys.executable,'-E',p['id']+'.py'],cwd=td,text=True,capture_output=True,timeout=60)
    self.assertEqual((r.returncode,r.stdout,r.stderr),(0,p['out'],''))

 def test_30_offline_export_needs_no_commands_network_or_packet_generation(self):
  with tempfile.TemporaryDirectory() as td:
   with patch('subprocess.run',side_effect=AssertionError('Offline export')),patch('socket.socket',side_effect=AssertionError('Offline export')),patch('infosec_u4_packets.pcap_bytes',side_effect=AssertionError('Read frozen file only')):
    out=export(Path(td)/'kit.zip')
   self.assertEqual(Path(out).read_bytes(),ZIP.read_bytes())

 def test_31_byte_identical_complete_rebuild_with_fresh_tls_keys(self):
  paths=[SUBJ_DIR/'subject.json',SUBJ_DIR/'unit4.json',PREVIEW,ZIP,FIXTURE]+[DIAG_DIR/(n+'.svg') for n in TITLES]
  before={p:p.read_bytes() for p in paths}
  r=subprocess.run([sys.executable,'tools/build_DI05007021_u4.py'],cwd=ROOT,text=True,capture_output=True,timeout=90)
  self.assertEqual(r.returncode,0,r.stderr)
  for p,raw in before.items():self.assertEqual(p.read_bytes(),raw,str(p))

 def test_32_all_798_prior_content_files_and_exported_units_preserved(self):
  baseline=json.loads((ROOT/'tools/baseline_before_DI05007021_u4.json').read_text());self.assertEqual(len(baseline),798)
  for rel,wanted in baseline.items():
   raw=(ROOT/rel).read_bytes()
   if rel=='content/computer/sem5/DI05007021/subject.json':
    old=json.loads(raw);self.assertEqual(old['units'][3]['file'],'unit4.json')
    for spec in old['units'][3:]:spec['file']=None
    raw=(json.dumps(old,ensure_ascii=False,indent=1)+'\n').encode()
   self.assertEqual(hashlib.sha256(raw).hexdigest(),wanted,rel)
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'data';r=subprocess.run([sys.executable,'tools/export_app_content.py','--out',str(out)],cwd=ROOT,text=True,capture_output=True,timeout=20)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertGreaterEqual(len(list((out/'subjects').glob('*.json'))),14)
   self.assertGreaterEqual(len(list((out/'units').glob('*.json'))),68)
   installed=[i for i in range(1,6) if (SUBJ_DIR/f'unit{i}.json').is_file()]
   for p in BASE.rglob('*.json'):
    rel=p.relative_to(BASE).as_posix()
    if rel=='catalog.json':continue
    if rel=='subjects/DI05007021.json':
     expected=json.loads(p.read_bytes());expected['available_units']=installed
     for spec in expected['units']:spec['file']=f"unit{spec['no']}.json" if spec['no'] in installed else None
     self.assertEqual(json.loads((out/rel).read_bytes()),expected)
    else:self.assertEqual((out/rel).read_bytes(),p.read_bytes(),rel)
   old=json.loads((BASE/'catalog.json').read_bytes());new=json.loads((out/'catalog.json').read_bytes())
   self.assertEqual(new['subjects'],old['subjects']);self.assertEqual(new['branches'],old['branches'])
   for rel,wanted in new['files'].items():self.assertEqual(hashlib.sha1((out/rel).read_bytes()).hexdigest()[:12],wanted)
   for n,wanted in {1:'8848c814de7659bb4210ddea155e8c87642a0d66cd203c4261390c1c44c8c5b5',2:'756ceb376b312cc9da930ab5bd6f4567e661c5a36e37f56764a7c3dceb962e17',3:'6cef3afbe321215279969584edc05d238cbc2ea1ef555775fb2356b19a7446b3'}.items():
    self.assertEqual(hashlib.sha256((out/f'units/DI05007021_u{n}.json').read_bytes()).hexdigest(),wanted)

 def test_33_original_answered_questions_suggested_marks_only(self):
  self.assertTrue(self.u['question_marks_are_suggested']);self.assertIn('not official past papers',self.u['question_provenance'])
  for i,((q,marks,a),item,question) in enumerate(zip(PRACTICE,self.u['notes'][-1]['items'],self.u['exam_questions']),1):
   self.assertEqual(question,{'q':{'en':'Practice: '+q},'marks':marks});self.assertIn(marks,[3,4,7])
   self.assertEqual(item['body']['en'],a);self.assertEqual(item['h']['en'],f'Practice {i}. {q}')

 def test_34_no_false_production_ids_benchmark_or_vpn_claim(self):
  e=self.u['runtime_evidence']
  for name in ['system_trust_store_changed','real_private_keys_published','IDS_deployment_or_production_accuracy_claim','production_firewall_or_gateway_claim']:
   self.assertIs(e[name],False)
  self.assertTrue('not measured production ids accuracy' in self.plain)
  self.assertTrue('not ipsec' in self.plain);self.assertTrue('not a full http parser' in self.plain)
  self.assertIn('not RFC-complete TCP',HELPERS['models.py'].read_text())

 def test_35_no_secrets_private_keys_binaries_or_fake_pkt_files(self):
  payload=PREVIEW.read_bytes()+(SUBJ_DIR/'unit4.json').read_bytes()
  with zipfile.ZipFile(ZIP) as z:
   for name in z.namelist():
    self.assertNotRegex(name,r'\.(pem|der|exe|so|dll|deb|tar|gz|pkt|pka)$');payload+=z.read(name)
  self.assertNotIn(b'-----BEGIN PRIVATE KEY-----',payload);self.assertNotIn(b'-----BEGIN RSA PRIVATE KEY-----',payload)
  for p in (ROOT/'.secrets').glob('*'):
   if p.is_file():
    secret=p.read_bytes().strip()
    if len(secret)>12:self.assertFalse(secret in payload,'Private credential leaked')
  self.assertLess(ZIP.stat().st_size,50000);self.assertFalse((ROOT.parent/'php_root').exists())

 def test_36_real_failure_cleanup_hostname_validation_and_bounded_framing(self):
  before=set(threading.enumerate());temps=set(Path('/tmp').glob('infosec-u3-*'))
  with patch('socket.create_connection',side_effect=ConnectionRefusedError('deliberate local client failure')):
   with self.assertRaises(ConnectionRefusedError):localnet.private_http('/course')
  self.assertEqual(set(threading.enumerate()),before)
  with patch('infosec_u4_localnet.HOST','wrong.diploma.test'):
   with self.assertRaises(ssl.SSLCertVerificationError):localnet.private_tls_relay()
  self.assertEqual(set(threading.enumerate()),before);self.assertEqual(set(Path('/tmp').glob('infosec-u3-*')),temps)
  class Fragmented:
   def __init__(self,parts):self.parts=iter(parts)
   def recv(self,count):return next(self.parts,b'')
  self.assertEqual(localnet.exact(Fragmented([b'N',b'ET']),3),b'NET')
  with self.assertRaises(ConnectionError):localnet.exact(Fragmented([b'N']),3)
  with self.assertRaises(ValueError):localnet.exact(Fragmented([]),1025)

if __name__=='__main__':unittest.main(verbosity=2)
