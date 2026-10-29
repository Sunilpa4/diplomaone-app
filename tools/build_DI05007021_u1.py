"""Build approved Unit 1 only; execute the safe examples before storing outputs."""
import copy,json,platform,subprocess,sys
from pathlib import Path
from subject_DI05007021 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007021_u1_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES
from content_DI05007021_u1_programs import execute_all
from diagrams_DI05007021_u1 import TITLES,main as draw
from preview_builder import build_preview

def version(*cmd):
 r=subprocess.run(cmd,check=True,text=True,capture_output=True,timeout=3)
 return r.stdout.splitlines()[0]

def main():
 programs=execute_all();draw()
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'iproute2':version('ip','-V'),'ss':version('ss','-V'),'ping':version('ping','-V'),
  'programs_executed':len(programs),'network_scope':'Owned IPv4 loopback only; OS-assigned TCP ports',
  'external_network_targets':False,'persistent_service':False,'dos_traffic_generated':False,
  'privileged_host_changes':False,'packet_capture_executed':False,'windows_commands_executed':False,
  'simulator_or_kali_executed':False,'ping_attempted':True,
  'ping_observed_status':programs[4]['out'].split('observed_status: ',1)[1].strip(),
  'normalization':'Actual result fields; no fixed dynamic ports or packet timings; HMAC key never published',
  'crypto_scope':'SHA-256 with trusted reference and HMAC-SHA256 illustration, not a cipher practical or production protocol'}
 unit={'subject':'DI05007021','unit':1,'format':'notes',
  'title':tr('Introduction to Information Security'),'hours':6,'weightage':15,'tabs':TABS[:],
  'intro_text':tr('English-only Unit 1: need for security; CIA goals; active/passive attacks and DoS; five security services; specific and pervasive mechanisms. Includes safe Practical 1 guidance, six executed supporting examples, diagrams, viva and answered revision. Suggested practice-question marks are not official GTU paper marks. Actual ping permission denial is reported honestly.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':id_,'title':tr(title),'file':'diagrams/'+id_+'.svg'} for id_,title in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':14,'answered_practice_count':12,
  'learning_outcomes':[tr('CO1: Describe the fundamentals of information security.')],
  'practical_numbers':[1],'content_kind':'theory_with_safe_practical_support',
  'assessment_note':tr('Official course: theory ESE 70 + PA 30; practical PA 20 + ESE 30 = 150. Practice sizes are suggested, not official GTU questions, paper patterns or guaranteed unit marks. Model answers are in Notes section 6.'),
  'question_provenance':'Original answered revision questions; not official past papers',
  'question_marks_are_suggested':True,'runtime_evidence':runtime,
  'sources':[{'title':name,'url':url} for name,url in SOURCES]}
 out=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007021_unit1_preview.html'))
 from export_DI05007021_u1_practicals import export
 export()
 print('Information Security Unit 1: 14 lessons / 6 executed examples / 8 SVGs / 12 cards / 28 viva / 12 answered practice')
 print('Ping observation:',runtime['ping_observed_status']);print('Unit:',out)

if __name__=='__main__':main()
