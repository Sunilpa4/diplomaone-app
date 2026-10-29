"""Build approved English Unit 3 with real RSA/CSR/PKI evidence and no private keys."""
import copy,hashlib,platform,sys
from subject_DI05007021 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007021_u3_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES
from content_DI05007021_u3_programs import execute_all,HELPERS
from diagrams_DI05007021_u3 import TITLES,main as draw
from infosec_u3_math import toy_keypair,power_trace
from infosec_u3_lab import openssl_version
from preview_builder import build_preview

def main():
 programs=execute_all();draw();pair=toy_keypair(61,53,17);value,trace=power_trace(65,17,3233)
 assert value==2790
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'openssl':openssl_version(),'programs_executed':len(programs),
  'helper_sha256':{n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in HELPERS.items()},
  'external_python_packages_required':False,'openssl_cli_required':True,
  'real_rsa_bits':2048,'public_exponent':65537,
  'encryption_profile':'RSA-OAEP; SHA-256; MGF1-SHA-256; empty label',
  'signature_profile':'RSA-PSS; SHA-256; MGF1-SHA-256; digest-length salt',
  'private_key_files_mode':'0600','temporary_directory_mode':'0700',
  'ephemeral_real_private_keys_published':False,'temporary_fixtures_removed':True,
  'network_access_used':False,'tls_handshake_performed':False,'public_CA_enrollment':False,
  'real_RA_identity_vetting_performed':False,'browser_or_system_trust_modified':False,
  'global_crypto_configuration_changed':False,'production_CA_or_protocol_claim':False,
  'full_PKIX_conformance_claim':False,'fips_validation_claim':False,
  'certificate_scope':'Fresh local root/intermediate/leaf; explicitly supplied lab root; reserved .test identity',
  'certificate_negative_cases':['wrong hostname','wrong purpose','missing intermediate','expired evaluation time','unrelated root','modified signature'],
  'leaf_CRL_check_performed':True,'full_chain_revocation_checked':False,'live_CRL_or_OCSP_performed':False,
  'normalization':'Actual math, sizes, fixed fictional names and verification outcomes; random bytes/keys/paths/dates not published as fixed values'}
 unit={'subject':'DI05007021','unit':3,'format':'notes','title':tr('Public-Key Cryptography'),
  'hours':10,'weightage':25,'tabs':TABS[:],
  'intro_text':tr('English-only Unit 3: public-key principles/applications; worked RSA algorithm, modular computation and security; digital signatures, certificates, CA/RA, enrollment and validation. Includes Practical 6 and ten actually executed arithmetic/OpenSSL examples. Toy RSA is not secure encryption; local PKI fixtures are not public enrollment or a live TLS service. Suggested practice marks are not official GTU allocations.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':n,'title':tr(t),'file':'diagrams/'+n+'.svg'} for n,t in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':16,'answered_practice_count':16,
  'learning_outcomes':[tr('CO3: Demonstrate public-key encryption with public-key cryptography.')],
  'practical_numbers':[6],'content_kind':'theory_with_executed_RSA_and_local_PKI_support',
  'assessment_note':tr('Official course: theory ESE 70 + PA 30; practical PA 20 + ESE 30 = 150. Unit 3 is 10h/25%, not a guaranteed paper allocation. Original practice sizes are suggested only; model answers are in Notes section 6.'),
  'question_provenance':'Original answered revision exercises; not official past papers','question_marks_are_suggested':True,
  'runtime_evidence':runtime,'worked_data':{'public_toy_parameters':pair,'modexp_trace':trace},
  'sources':[{'title':n,'url':u} for n,u in SOURCES]}
 path=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007021_unit3_preview.html'))
 from export_DI05007021_u3_practicals import export
 export()
 print('Unit 3: 16 lessons / 10 executed examples / 10 SVGs / 14 cards / 36 viva / 16 answered practice')
 print('Unit:',path)

if __name__=='__main__':main()
