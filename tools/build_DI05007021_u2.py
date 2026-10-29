"""Build approved English Unit 2 with actual cipher outputs and independent DES proof."""
import copy,hashlib,platform,sys
from subject_DI05007021 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007021_u2_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES
from content_DI05007021_u2_programs import execute_all,HELPER
from diagrams_DI05007021_u2 import TITLES,main as draw
from infosec_u2_ciphers import des_trace
from infosec_u2_evidence import check_des
from preview_builder import build_preview

def main():
 programs=execute_all();reference=check_des();draw()
 trace=des_trace(bytes.fromhex('0123456789ABCDEF'),bytes.fromhex('133457799BBCDFF1'))
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'programs_executed':len(programs),
  'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),
  'external_packages_required':False,'network_access_used':False,'persistent_service':False,
  'real_user_data_used':False,'production_security_claim':False,'fips_validation_claim':False,
  'global_crypto_configuration_changed':False,'cipher_keys_are_public_teaching_data':True,
  'fresh_pad_material_published':False,'otp_randomness_claim':'OS-backed CSPRNG demonstration, not proof of ideal information-theoretic randomness',
  'normalization':'Classical ASCII letters uppercased, whitespace removed; Playfair I/J merged; fillers/padding preserved',
  'steganography_scope':'In-memory synthetic RGB channel bytes only; no real images/files or network channel',
  'des_status':'Historical withdrawn DES, not modern data protection',
  'independent_des_reference':reference}
 unit={'subject':'DI05007021','unit':2,'format':'notes',
  'title':tr('Conventional and Symmetric Cryptography'),'hours':12,'weightage':25,'tabs':TABS[:],
  'intro_text':tr('English-only Unit 2: cryptographic terms; monoalphabetic, Caesar, polyalphabetic/Vigenere, Playfair, Hill, one-time pad and rail fence; steganography types; historical DES structure and trade-offs. Includes worked calculations and twelve actually executed examples for Practicals 2–5 and supporting study. Classical methods and DES are not production protection. Suggested practice marks are not official GTU allocations.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':n,'title':tr(t),'file':'diagrams/'+n+'.svg'} for n,t in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':18,'answered_practice_count':16,
  'learning_outcomes':[tr('CO2: Demonstrate substitution, transposition techniques and symmetric cryptography algorithms.')],
  'practical_numbers':[2,3,4,5],'content_kind':'theory_with_executed_classical_cipher_practicals',
  'assessment_note':tr('Official course: theory ESE70 + PA30; practical PA20 + ESE30 =150. Unit 2 weight25% is not a guaranteed paper allocation. Practice question sizes are suggested only; model answers are in Notes section7.'),
  'question_provenance':'Original answered revision exercises; not official past papers',
  'question_marks_are_suggested':True,'runtime_evidence':runtime,
  'worked_data':{'des_public_master_key_hex':'133457799BBCDFF1','des_public_plaintext_hex':'0123456789ABCDEF',
   'des_ciphertext_hex':trace['result'].hex().upper(),'des_rounds':trace['rounds']},
  'sources':[{'title':n,'url':u} for n,u in SOURCES]}
 path=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007021_unit2_preview.html'))
 from export_DI05007021_u2_practicals import export
 export()
 print('Unit 2: 18 lessons / 12 executed examples / 10 SVGs / 14 cards / 36 viva / 16 answered practice')
 print('Independent DES:',reference['compared_blocks'],'blocks, both directions; unit:',path)

if __name__=='__main__':main()
