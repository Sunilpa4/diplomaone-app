"""Build final approved unit: safe defensive examples and explicit Kali limits."""
import copy,hashlib,json,platform,sqlite3,subprocess,sys
from subject_DI05007021 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007021_u5_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES
from content_DI05007021_u5_programs import execute_all,HELPERS,FIXTURES
from infosec_u5_manifest import verify_manifest
from infosec_u3_lab import openssl_version
from diagrams_DI05007021_u5 import TITLES,main as draw
from preview_builder import build_preview

def main():
 programs=execute_all();metadata=verify_manifest(FIXTURES);draw()
 gpg=subprocess.run(['gpg','--version'],check=True,text=True,capture_output=True,timeout=5).stdout.splitlines()[0]
 provenance=json.loads((FIXTURES/'provenance.json').read_text())
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'programs_executed':len(programs),'sqlite':sqlite3.sqlite_version,
  'openssl':openssl_version(),'gpg':gpg,'external_python_packages_required':False,
  'helper_sha256':{n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},
  'metadata_file_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(FIXTURES.iterdir()) if p.is_file()},
  'safe_actual_operations':['In-memory SQLite binding/authorizer','offline URL/email parsing','owned benign file checks/recovery','owned TLS identity check','isolated GPG signed-metadata verification'],
  'logical_models':['fictional IP/MAC comparison','synthetic-clock token bucket'],
  'malware_or_attack_payload_executed':False,'phishing_email_or_form_delivered':False,
  'public_network_targets_used':False,'forged_packets_or_ARP_cache_writes':False,'flood_or_load_test_performed':False,
  'botnet_C2_backdoor_or_persistence_created':False,'real_user_data_or_credentials_used':False,
  'TLS_scope':'Owned IPv4 loopback only, correct certificate versus wrong hostname; not an actual MITM or mutual-TLS test',
  'system_trust_or_network_policy_changed':False,'real_private_keys_published':False,
  'temporary_files_keys_keyrings_sockets_workers_cleaned':True,
  'Kali_OS_downloaded_installed_or_booted':False,'Kali_tools_executed':False,'ISO_or_VM_image_downloaded':False,
  'actual_ISO_hash_verified':False,'signed_Kali_metadata_verified':True,
  'GPG_user_or_system_keyrings_modified':False,'GPG_automatic_key_retrieval_used':False,
  'Kali_metadata_result':metadata,'metadata_retrieval_provenance':provenance,
  'production_malware_detection_or_resilience_claim':False,'legal_finding_or_response_guarantee':False,
  'normalization':'Actual fixture results and verification outcomes; no real secrets or arbitrary target traffic'}
 unit={'subject':'DI05007021','unit':5,'format':'notes','title':tr('Introduction to Cyber Security'),
  'hours':8,'weightage':15,'tabs':TABS[:],
  'intro_text':tr('English-only Unit 5: threats/vulnerabilities/actors; viruses, worms, adware, spyware, Trojans, DoS/DDoS, MITM, IP/ARP spoofing, SQL injection, phishing, botnets and backdoors; cyberspace/cybercrime and safe response. Ten bounded defensive examples support study Practicals 11/12. Kali OS/VM work is guided only: actual GPG checks signed metadata, NOT an ISO or booted Kali system. Practice marks are suggested, not official GTU allocations.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':n,'title':tr(t),'file':'diagrams/'+n+'.svg'} for n,t in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':16,'answered_practice_count':16,
  'learning_outcomes':[tr('CO5: Describe the basics of cyber security, cyber-attacks and cybercrime.')],
  'practical_numbers':[11,12],'content_kind':'introductory_cybersecurity_with_safe_defensive_and_signed_metadata_support',
  'assessment_note':tr('Official course: theory ESE 70 + PA 30; practical PA 20 + ESE 30 = 150. Unit 5 is 8h/15%, not a guaranteed paper allocation. Original suggested practice sizes are not official GTU questions; answers are in Notes section 6.'),
  'question_provenance':'Original answered revision exercises; not official past papers','question_marks_are_suggested':True,
  'runtime_evidence':runtime,'sources':[{'title':n,'url':u} for n,u in SOURCES]}
 path=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007021_unit5_preview.html'))
 from export_DI05007021_u5_practicals import export
 export()
 print('Unit 5: 16 topics / 10 safe executed examples / 8 SVGs / 12 cards / 32 viva / 16 answered practice')
 print('All five units prepared. Kali evidence: signed metadata ONLY; no ISO/VM/OS boot. Unit:',path)

if __name__=='__main__':main()
