"""GTU Hardware Architecture/System Maintenance — approved English units only."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
SUBJ_DIR=ROOT/'content/computer/sem5/DI05007011';DIAG_DIR=SUBJ_DIR/'diagrams'
TABS=['notes','programs','diagrams','syntax','viva','exam']
def tr(s):return {'en':s}
UNITS=[
 (1,'Core Components of PC/Laptop',7,16,[
  'Computer systems/PC development; micro, mini, mainframe, supercomputer, workstation, cloud and embedded systems',
  'PC block diagram; CPU(ALU/CU), motherboard, RAM, ROM, HDD/SSD, keyboard, mouse, LCD/LED monitor and SMPS',
  'Hardware, software, firmware; BIOS, UEFI and CMOS',
  'Laptop CPU/RAM/expansion, battery, video controller/display, removable/internal storage, input, ports, cooling, speakers/webcam and Wi-Fi/Bluetooth',
  'Front/back ports/connectors: USB, HDMI, RJ45,3.5mm audio,VGA,Thunderbolt',
  'Prepare dated PC/laptop specifications: CPU,RAM,storage,GPU,display,ports,connectivity,OS']),
 (2,'Processor Architecture & Motherboard',11,25,[
  'Microprocessor introduction;8085 features, architecture/registers/ALU/CU/buses and pin diagram',
  'RISC/CISC;dual/quad-core concept and advantages',
  'Motherboard block/components/layout;AT/ATX/Micro-ATX/Mini-ITX;historical northbridge/southbridge',
  'ISA,PCI,PCI-E,PCI-X,AGP,USB,VESA local bus;SMPS working/connectors',
  'SATA,NVMe,RAID (distinguish protocol/interface/array concepts)']),
 (3,'Memory Organization',8,18,[
  'Memory hierarchy/classification;primary RAM/ROM;SRAM/DRAM/DDR generations',
  'PROM,EPROM,EEPROM,Flash;secondary storage;HDD structure/working/performance',
  'Seek,rotation,access and transfer rates;SSD concept/types/working;HDD vs SSD;DVD/USB',
  'Cache L1/L2/L3;associative memory;virtual memory,paging and segmentation']),
 (4,'Input, Output & Peripheral Devices',12,25,[
  'Keyboard types/list;working,construction and operation:mechanical/membrane/wireless',
  'Mouse types/list;working:optical/wireless Bluetooth',
  'Scanner types/list;working:flatbed/sheet-fed',
  'Monitor types/list;LCD/LED working,construction and operation',
  'Printer types/list;laser/inkjet/thermal working,construction,operation and applications']),
 (5,'PC Troubleshooting & Preventive Maintenance',7,16,[
  'POST functions,IPL hardware,test sequences,error messages/codes;visual and layman checks',
  'Systematic motherboard,keyboard,mouse,printer,HDD,monitor,RAM and SMPS troubleshooting',
  'Preventive maintenance/safety;DMM,oscilloscope,logic analyzer/probe/pulser,current tracer',
  'Memtest,CCleaner,HDD scan,defraggler,CPU-Z,CrystalDiskInfo as syllabus-listed tools with safe/contextual use',
  'PC assembly/disassembly with safety and ESD precautions'])]
SUBJECT={'code':'DI05007011','name':tr('Computer Hardware Architecture and System Maintenance'),
 'branch':'computer','semester':5,'syllabus_year':'2026-27','category':'PCC','type':'theory',
 'languages':['en'],'code_lang':'python','teaching':{'lecture':3,'tutorial':0,'practical':2},
 'exam':{'theory_ese':70,'theory_pa':30,'practical_pa':20,'practical_ese':30,'total':150,'credits':4},
 'prerequisites':['Computer/OS fundamentals','Basic electronics:power,voltage,connectors','Peripherals and use','Safe handling of electrical equipment'],
 'theory_rbt_percent':{'remember':30,'understand':40,'apply':30,'analyze':0,'evaluate':0,'create':0},
 'units':[{'no':n,'title':tr(t),'hours':h,'weightage':w,'topics':topics,'file':None} for n,t,h,w,topics in UNITS],
 'course_outcomes':[
  'CO1: Identify and elaborate components of PC/laptop and overall system architecture.',
  'CO2: Examine the processor,motherboard and system buses.',
  'CO3: Identify memory hierarchy and differentiate memory types.',
  'CO4: Demonstrate working principles of I/O devices and peripherals.',
  'CO5: Diagnose hardware faults and perform preventive maintenance.'],
 'practicals':[
  'Identify internal desktop components and observe their functions.',
  'Study and compare CISC and RISC architecture.',
  'Identify motherboard CPU socket,RAM slots,chipset,expansion slots and connectors.',
  'Observe front/back panel ports and list their functions.',
  'Study SMPS connectors and measure output voltages using a digital multimeter.',
  'Install/remove RAM and verify detection in BIOS/UEFI.',
  'Install HDD/SSD and connect the appropriate SATA/NVMe interface (model/form-factor dependent).',
  'Configure BIOS/UEFI and observe hardware detection parameters.',
  'Identify memory modules and storage devices.',
  'Connect/test keyboard,mouse and scanner.',
  'Install/configure a printer and perform a test print.',
  'Identify monitor ports and configure display settings.',
  'Perform POST and interpret model-specific beep/startup error codes.',
  'Troubleshoot no-display,boot-failure,RAM and other common faults.',
  'Assemble/disassemble a PC with safety/ESD precautions.'],
 'books':[
  'Craig Zacker and John Rourke — PC Hardware:The Complete Reference',
  'Scott Mueller — Upgrading and Repairing PCs',
  'William Stallings — Computer Organization and Architecture',
  'K.L.James — Computer Hardware Installation and Interfacing',
  'Stephen J.Bigelow — Troubleshooting,Maintaining and Repairing PCs',
  'Mark Minasi — The Complete PC Upgrade and Maintenance Guide',
  'Mike Meyers — CompTIA A+ Certification All-in-One Exam Guide',
  'Morris Mano — Computer System Architecture']}

def write_subject():
 SUBJ_DIR.mkdir(parents=True,exist_ok=True);DIAG_DIR.mkdir(exist_ok=True)
 for spec in SUBJECT['units']:
  name=f"unit{spec['no']}.json";spec['file']=name if (SUBJ_DIR/name).is_file() else None
 (SUBJ_DIR/'subject.json').write_text(json.dumps(SUBJECT,ensure_ascii=False,indent=1)+'\n')

def write_unit(unit):
 SUBJ_DIR.mkdir(parents=True,exist_ok=True);DIAG_DIR.mkdir(exist_ok=True)
 spec=SUBJECT['units'][unit['unit']-1]
 assert unit['title']==spec['title'] and (unit['hours'],unit['weightage'])==(spec['hours'],spec['weightage'])
 def check(o):
  if isinstance(o,dict):
   assert 'gu' not in o and 'key' not in o
   for v in o.values():check(v)
  elif isinstance(o,list):
   for v in o:check(v)
  elif isinstance(o,str):assert not re.search(r'[\u0a80-\u0aff]',o)
 check(unit)
 path=SUBJ_DIR/f"unit{unit['unit']}.json";path.write_text(json.dumps(unit,ensure_ascii=False,indent=1)+'\n')
 write_subject();return path
