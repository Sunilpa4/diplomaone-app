"""Build Unit 4: explicit models, actual offline analysis/local I/O, guided PT."""
import copy,hashlib,platform,ssl,sys
from subject_DI05007021 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007021_u4_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES
from content_DI05007021_u4_programs import execute_all,HELPERS
from infosec_u4_packets import pcap_bytes,dissect,tshark_version
from infosec_u3_lab import openssl_version
from diagrams_DI05007021_u4 import TITLES,main as draw
from preview_builder import build_preview
MANIFEST=['frame.number','_ws.col.Protocol','ip.src','ip.dst','tcp.srcport','tcp.dstport',
          'vlan.id','ip.checksum.status','tcp.checksum.status','udp.checksum.status']

def main():
 programs=execute_all();draw();raw=pcap_bytes()
 fixture=ROOT/'tools/fixtures_DI05007021_u4/synthetic.pcap';fixture.parent.mkdir(parents=True,exist_ok=True);fixture.write_bytes(raw)
 manifest=dissect(MANIFEST)
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'programs_executed':len(programs),'tshark':tshark_version(),
  'openssl_cli':openssl_version(),'python_ssl':ssl.OPENSSL_VERSION,
  'helper_sha256':{n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},
  'external_python_packages_required':False,'TShark_offline_executed':True,'Wireshark_GUI_executed':False,
  'live_packet_capture_performed':False,'Packet_Tracer_executed':False,'Snort_Suricata_or_NGFW_executed':False,
  'kernel_firewall_changed':False,'switch_VLAN_or_router_configured':False,'network_namespace_created':False,
  'public_network_targets_used':False,'persistent_service':False,'host_capture_privileges_enabled':False,
  'logical_models':['DMZ flow policy','rule order/default deny','tiny TCP direction/phase/TTL','same-VLAN membership','invented NIDS rule/label fixtures'],
  'real_local_operations':['TShark offline dissection/filter/checksum validation','owned loopback HTTP allow-list','owned private TLS1.3 byte relay','owned temporary-file hash changes'],
  'network_scope':'Owned IPv4 loopback only for actual sockets; documentation IPs exist only in models/synthetic PCAP',
  'TLS_handshake_performed':True,'mutual_TLS_performed':False,'TLS_scope':'One client-to-relay TLS1.3 segment, then owned plaintext loopback backend; not VPN/IPsec',
  'system_trust_store_changed':False,'real_private_keys_published':False,'temporary_keys_sockets_workers_cleaned':True,
  'synthetic_pcap_sha256':hashlib.sha256(raw).hexdigest(),'synthetic_pcap_bytes':len(raw),'synthetic_frame_count':len(manifest),
  'pcap_origin':'Constructed benign protocol fixture; NOT live capture or Packet Tracer output',
  'checksum_status_reference':{'Good':1,'Bad':0,'Unverified':2},
  'IDS_deployment_or_production_accuracy_claim':False,'production_firewall_or_gateway_claim':False,
  'practical_execution_scope':{'7':'Actual TShark offline synthetic-file analysis; Wireshark GUI/live capture guided only',
   '8':'Packet Tracer guided only; Python VLAN model/tag dissection are separate illustrations',
   '9':'Packet Tracer guided only; logical DMZ policy is not enforcement',
   '10':'Packet Tracer router-ACL guide only; models/owned application allow-list are not a deployed kernel firewall'}}
 unit={'subject':'DI05007021','unit':4,'format':'notes','title':tr('Network Security'),'hours':9,'weightage':20,'tabs':TABS[:],
  'intro_text':tr('English-only Unit 4: zones/DMZ/Internet/Intranet/VLAN/tunneling; packet, stateful, application, circuit and next-generation firewalls; intruders/IDS/components/HIDS/NIDS. Includes twelve executed logical/offline/private-local examples and clearly guided-only Packet Tracer/Wireshark GUI exercises for Practicals 7–10. Synthetic PCAP is not live capture; models are not deployed protection. Practice marks are suggested, not official allocations.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':n,'title':tr(t),'file':'diagrams/'+n+'.svg'} for n,t in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':18,'answered_practice_count':16,
  'learning_outcomes':[tr('CO4: Apply measures to protect network communication using firewalls and intrusion detection systems.')],
  'practical_numbers':[7,8,9,10],'content_kind':'network_theory_with_explicit_model_offline_local_and_guided_evidence',
  'assessment_note':tr('Official course: theory ESE 70 + PA 30; practical PA 20 + ESE 30 = 150. Unit 4 is 9h/20%, not a guaranteed paper allocation. Original suggested practice sizes are not official GTU questions; answers are in Notes section 5.'),
  'question_provenance':'Original answered revision exercises; not official past papers','question_marks_are_suggested':True,
  'runtime_evidence':runtime,'worked_data':{'manifest_fields':MANIFEST,'manifest_rows':manifest},
  'sources':[{'title':n,'url':u} for n,u in SOURCES]}
 path=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007021_unit4_preview.html'))
 from export_DI05007021_u4_practicals import export
 export()
 print('Unit 4: 18 lessons / 12 executed illustrations / 10 SVGs / 14 cards / 36 viva / 16 answered practice')
 print('Actual TShark:',runtime['tshark'],'/ synthetic frames:',len(manifest));print('Unit:',path)

if __name__=='__main__':main()
