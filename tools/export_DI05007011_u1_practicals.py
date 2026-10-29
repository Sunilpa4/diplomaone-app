"""Offline deterministic hardware identification/support kit; no device probing."""
import csv,io,json,zipfile
from pathlib import Path
from content_DI05007011_u1_guides import GUIDES,COMPONENTS,PORTS
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'preview/DI05007011_unit1_practicals.zip'
README='''# DI05007011 — Unit 1 — Core Components of PC/Laptop (English only)

GTU Semester 5 / effective 2026–27 / 7 hours / 16% / CO1.
Course scheme: 70+30 theory and20+30 practical=150, 4 credits,L3/T0/PR2.
Official Practicals 1 and4 concern physical component/port identification.
Those physical tasks are GUIDED ONLY,not executed/fabricated in this sandbox.

## Actual software examples
Python 3.10+; reference 3.13.16 / Debian 13 x86_64. No pip package/server required.
Keep hardware_lab.py and reference_specs.json beside the four root scripts.
Run: python3 hw1p01.py (then 02–04 separately); no PYTHONPATH setup is needed.
01:actual generic OS/kernel inventory;02:capacity-unit arithmetic;
03:declared fictional USB-C profile comparison;04:spec-field completeness.
expected/*.txt stores actual reference stdout,not invented hardware readings.
Resource values can differ on another sandbox/device;report scope/version.

The inventory reports only exposed OS/kernel architecture,logical CPUs and
Linux MemTotal. It does not prove physical cores,DIMMs,laptop model,ports,
firmware mode or the learner's device. It avoids hostname,DMI serial,MAC and
account collection. The other scripts calculate or validate declared data;
they are not electrical measurements,USB/PD negotiation,certification,
physical compatibility/performance tests or real component handling.

## Dated reference specs
Two manufacturer first/base configurations were reviewed on 29 Oct2026:
MacBook Air 13-inch M5 and Mac mini M6. They are Apple Silicon/macOS examples,
NOT Windows x86 BIOS/assembly instructions. Do not mix configurable upgrades,
15-inch or M5 Pro variants into the selected base profiles. Unified-memory
labels do not promise standard DIMM upgradeability. Only structured facts and
source-check hashes are bundled,not raw manufacturer pages/photos/prices.
They are dated manufacturer-listed educational examples,not worldwide newest,
Indian availability/stock,purchase,upgrade or benchmark guarantees. Recheck
exact model/service documents for new work. The syllabus13th-gen i5 sample is
illustrative,not automatically latest in2026.

## Physical/GUI guidance and safety
Use components.csv,ports.csv and specification.csv for YOUR actual supervised
observations,documentation-only values or UNKNOWN entries. Windows/macOS GUI
and BIOS/UEFI observations are guided,NOT claimed as executed here. The SVGs
are concept/recognition schematics,not photographs,exact pinouts or service
maps. Connector shape alone does not prove capability. USB-C,USB protocols,
Thunderbolt generations,DisplayPort/video and negotiated PD are distinct.

Use only an owned/instructor-authorized device,the exact service manual and
appropriate trained supervision/approved ESD setup. Isolate specified power
sources before permitted internal work;never improvise mains grounding.
NEVER open PSU/SMPS,charger or monitor enclosures or probe hazardous power.
Stored charge can remain after unplugging. Stop for damaged/swollen batteries;
no shorting,puncturing,battery removal,voltage tests or physical repair is done
here. No firmware flashing,CMOS/password clearing,TPM/Secure Boot/boot/security
changes are part of this introduction. Avoid private asset/customer details in
shared journals. Guides are not a universal assembly/repair procedure.

## Study
18 lessons, 11 diagrams, 14 reference cards, 32 viva and 16 original answered
revision questions are in the preview/live unit. Suggested 3/4/7-mark sizes are
practice guidance,NOT official GTU questions/allocations or a predicted paper.
The 16% weight is not a guaranteed question allocation.

17 files: 4 scripts, 4 actual outputs,hardware_lab.py,reference_specs.json,
runtime.json,README, 3 blank learner CSVs and 2 guided-only Markdown documents.
No binaries,driver installs,physical/electrical result claims or heavy runtime.
'''

def csv_text(rows):
 f=io.StringIO();csv.writer(f,lineterminator='\n').writerows(rows);return f.getvalue()

def export(path=OUT):
 unit=json.loads((ROOT/'content/computer/sem5/DI05007011/unit1.json').read_text())
 files={'README.md':README,'hardware_lab.py':(ROOT/'tools/hardware_u1_helper.py').read_text(),
  'reference_specs.json':(ROOT/'tools/fixtures_DI05007011_u1/reference_specs.json').read_bytes(),
  'runtime.json':json.dumps(unit['runtime_evidence'],indent=2)+'\n'}
 files.update(GUIDES)
 files['components.csv']=csv_text([['Component / role','Function','Actual location or documentation','Observed / documented / unknown','Safety / limitation']]+[[x,'','','',''] for x in COMPONENTS])
 files['ports.csv']=csv_text([['Port / connector','Actual position','Documented function/capability','Evidence/source','Unknown/limitation']]+[[x,'','','',''] for x in PORTS])
 fields=['Exact model/configuration','Processor','Memory','Storage','GPU','Display','Ports','Connectivity','Operating system','Source URL','Check date','Evidence scope / unknowns']
 files['specification.csv']=csv_text([['Field','Recorded value','Source / evidence','Limitation']]+[[x,'','',''] for x in fields])
 for p in unit['programs']:
  files[p['id']+'.py']=p['code']['en'];files['expected/'+p['id']+'.txt']=p['out']
 assert len(files)==17
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for name,data in files.items():
   info=zipfile.ZipInfo(name,(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data if isinstance(data,bytes) else data.encode())
 print('Hardware Unit 1 practical kit:',path.stat().st_size,'bytes / 17 files');return str(path)

if __name__=='__main__':export()
