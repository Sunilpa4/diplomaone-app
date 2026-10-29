"""Build approved Unit 1 only; physical work guided,software results actual."""
import copy,hashlib,json,platform,sys
from subject_DI05007011 import ROOT,SUBJECT,DIAG_DIR,TABS,tr,write_unit
from content_DI05007011_u1_notes import NOTES,SYNTAX,VIVA,EXAM,ANSWERED,SOURCES,REFERENCE
from content_DI05007011_u1_programs import execute_all,HELPER,REFERENCE as REFERENCE_PATH
from diagrams_DI05007011_u1 import TITLES,main as draw
from preview_builder import build_preview

def main():
 programs=execute_all();draw();inventory=json.loads(programs[0]['out'])
 runtime={'python':sys.version.split()[0],'os':platform.freedesktop_os_release()['PRETTY_NAME'],
  'architecture':platform.machine(),'software_examples_executed':len(programs),
  'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),
  'reference_json_sha256':hashlib.sha256(REFERENCE_PATH.read_bytes()).hexdigest(),
  'external_packages_or_network_required_for_examples':False,
  'sandbox_inventory':inventory,'inventory_is_physical_student_device_spec':False,
  'physical_PC_or_laptop_inspected':False,'physical_components_or_ports_handled_tested':False,
  'physical_practicals_1_4_completed':False,'hardware_photographs_taken':False,
  'electrical_voltage_measurements':False,'SMPS_charger_monitor_opened':False,
  'battery_or_component_insertion_removal':False,'BIOS_UEFI_GUI_accessed':False,
  'firmware_CMOS_TPM_or_security_settings_changed':False,'drivers_or_OS_settings_changed':False,
  'hostnames_serials_MACs_or_credentials_collected':False,
  'connector_profile_scope':'Explicit fictional specification-data comparison;no port/cable/PD test',
  'manufacturer_references_scope':'Dated official-page first/base profiles;not physical tests,worldwide latest,stock,purchase,upgrade or benchmark guarantees',
  'reference_check_date':REFERENCE['checked_on'],'reference_platform_note':REFERENCE['platform_note'],
  'actual_inventory_scope':'Read-only generic OS/kernel resources only;not physical component identification',
  'practical_execution_scope':{'1':'Guided-only supervised physical desktop component identification',
   '4':'Guided-only physical front/back port identification;Windows/macOS/BIOS GUI not executed'}}
 unit={'subject':'DI05007011','unit':1,'format':'notes','title':tr('Core Components of PC/Laptop'),
  'hours':7,'weightage':16,'tabs':TABS[:],
  'intro_text':tr('English-only,diagram-focused Unit 1:computer development/types,PC functional blocks,CPU/board/memory/storage/I/O/power,hardware/software/firmware,BIOS/UEFI/CMOS,laptop components,ports/connectors and dated specifications. Four executed software helpers support worksheets;physical Practicals1/4 are guided only,not fabricated hardware/electrical/BIOS work. Original practice marks are suggested,not official GTU allocations.'),
  'notes':copy.deepcopy(NOTES)+[copy.deepcopy(ANSWERED)],'programs':programs,
  'diagrams':[{'id':n,'title':tr(t),'file':'diagrams/'+n+'.svg'} for n,t in TITLES.items()],
  'syntax':SYNTAX,'viva':VIVA,'exam_questions':EXAM,'lesson_count':18,'answered_practice_count':16,
  'learning_outcomes':[tr('CO1:Identify and elaborate components of PC/laptop and overall system architecture.')],
  'practical_numbers':[1,4],'content_kind':'hardware_theory_with_guided_physical_identification_and_actual_software_support',
  'assessment_note':tr('Official course:theory ESE70+PA30;practical PA20+ESE30=150,4 credits. Unit1 is7h/16%,not guaranteed question marks. Original suggested revision sizes are not official GTU papers;answers are in Notes section6.'),
  'question_provenance':'Original answered revision exercises;not official past papers','question_marks_are_suggested':True,
  'runtime_evidence':runtime,'manufacturer_reference_profiles':REFERENCE['profiles'],
  'sources':[{'title':n,'url':u} for n,u in SOURCES]}
 path=write_unit(unit)
 build_preview(unit,SUBJECT,str(DIAG_DIR),str(ROOT/'preview/DI05007011_unit1_preview.html'))
 from export_DI05007011_u1_practicals import export
 export()
 print('Hardware Unit 1:18 topics /4 executed software examples /11 SVGs /14 cards /32 viva /16 answered practice')
 print('Physical component/port/electrical/BIOS work:guided only. Unit:',path)

if __name__=='__main__':main()
