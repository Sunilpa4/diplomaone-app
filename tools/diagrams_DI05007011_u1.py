"""Eleven original mobile hardware schematics, NOT photos or electrical pinouts."""
from flowchart_lib import svg,text,arr,rbox,P
from diagrams_DI05007021_u1 import heading,foot,row,BLUE,BF,GREEN,GF,ORANGE,OF,PF,RED,RF
from subject_DI05007011 import DIAG_DIR
TITLES={'hw1_types':'Computer Categories Are Different Axes','hw1_block':'Conceptual PC Functional Blocks',
 'hw1_cpu':'CPU Functional Roles','hw1_board':'Generic Motherboard Role Map',
 'hw1_layers':'Hardware,Software and Firmware','hw1_firmware':'Firmware,OS and Settings Distinctions',
 'hw1_laptop':'Laptop Groups and Integration','hw1_ports':'External Port Recognition Schematics',
 'hw1_usb':'Same Shape,Check Actual Capability','hw1_specs':'A Defensible Dated Specification',
 'hw1_safety':'Safe Identification and Evidence'}

def chain(title,items,height,footer=()):
 b=heading(title)
 for i,(n,d) in enumerate(items):
  y=72+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=foot(height-45,*footer)
 return svg(360,height,b)

def types():
 b=heading('Categories overlap; not one size ladder')
 data=[('Microcomputer','Personal desktop/laptop context'),('Minicomputer','Historical midrange/multiuser category'),
 ('Mainframe','Enterprise transaction/reliability workloads'),('Supercomputer','Suitable large-scale parallel computation'),
 ('Workstation','Professional/technical personal-use role'),('Cloud','Remote access/service/deployment model'),
 ('Embedded','Computing integrated for a device function')]
 for i,(n,d) in enumerate(data):b+=row(63+71*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,58)
 b+=foot(628,'A modern miniPC is not a historical minicomputer.')
 return svg(360,661,b)

def block():
 b=heading('PC functional relationships','Conceptual roles,not literal wiring/pinout')
 b+=rbox(180,89,324,54,'INPUT: keyboard / mouse / other devices',BF,BLUE,11.2)
 b+=arr([(180,116),(180,148)],P)
 b+=rbox(180,182,240,68,'PROCESSING: CPU\nALU + control + internal state',PF,P,12)
 b+=arr([(125,216),(125,242),(75,242),(75,275)],P)
 b+=arr([(105,275),(105,257),(155,257),(155,216)],P)
 b+=arr([(235,216),(235,242),(285,242),(285,275)],P)
 b+=arr([(255,275),(255,257),(205,257),(205,216)],P)
 b+=rbox(90,310,144,70,'RAM\nActive working state',GF,GREEN,11)
 b+=rbox(270,310,144,70,'STORAGE\nPersistent programs/files',OF,ORANGE,10.4)
 b+=arr([(300,182),(350,182),(350,397),(180,397),(180,412)],P)
 b+=rbox(180,444,324,64,'OUTPUT: display / other devices\nSoftware/controllers participate throughout',BF,BLUE,10.8)
 b+=foot(523,'Motherboard/interconnects support communication.',
              'Power supports the system;it is not the data path.')
 return svg(360,571,b)

def cpu():
 b=heading('CPU: simplified functional roles')
 for i,(n,d) in enumerate([('ALU','Arithmetic and logical operations'),('CONTROL UNIT','Instruction/control sequencing'),('REGISTERS / INTERNAL STATE','Fast state used during execution')]):
  b+=row(75+101*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,76)
 b+=foot(409,'Not separate student-removable chip components.',
              'Cores / GHz alone are not a universal speed score.')
 return svg(360,458,b)

def board():
 b=heading('Generic motherboard role map','NOT a model-specific layout or service photograph')
 b+='<rect x="18" y="69" width="324" height="351" rx="8" fill="#EEF6EE" stroke="#2E7D32" stroke-width="2"/>'
 b+=rbox(102,144,128,104,'CPU / SoC\nDesign varies',BF,BLUE,11)
 for x in [195,224,253,282]:b+=f'<rect x="{x}" y="95" width="19" height="126" fill="#EADDF7" stroke="{P}" stroke-width="1.4"/>'
 b+=text(250,240,'Memory / slot area*',11,color=P)
 b+=rbox(101,283,132,58,'Firmware storage\n(nonvolatile content)',PF,P,10.8)
 b+=rbox(253,307,144,62,'I/O / controller\nfunctions*',OF,ORANGE,11)
 b+=rbox(180,380,292,45,'Storage / expansion / power connections*',BF,BLUE,10.6)
 b+=foot(457,'* Locations,integration and removability vary.',
              'Some functions share a package;consult the manual.')
 return svg(360,508,b)

def layers():
 b=heading('Physical carrier is not its program')
 b+=row(76,'HARDWARE','Physical chip / board / device',BF,BLUE,75)
 b+=row(181,'FIRMWARE','Low-level software in suitable storage',PF,P,75)
 b+=row(286,'SOFTWARE','OS / drivers / applications and data',GF,GREEN,75)
 b+=foot(411,'The flash chip is hardware;its contents are code.',
              'Firmware can be updateable;no flashing is done.')
 return svg(360,460,b)

def firmware():
 b=heading('Startup interface is not settings storage')
 data=[('Platform firmware initialization','Applicable hardware / platform state'),
       ('Legacy BIOS OR UEFI boot interfaces','Alternative paths,not two required stages'),
       ('OS loader and operating system','Drivers/apps then use supported hardware')]
 for i,(n,d) in enumerate(data):
  y=68+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=row(330,'SEPARATE: CMOS / RTC / NVRAM','Settings/time context,not an after-OS boot step',OF,ORANGE,70)
 b+=foot(445,'RTC cell is not the laptop operating battery.',
              'No BIOS,CMOS,TPM or security-setting changes.')
 return svg(360,492,b)

def laptop():
 b=heading('Laptop: integration varies by model','Concept silhouette,not a disassembly map')
 b+='<rect x="56" y="79" width="248" height="147" rx="7" fill="#DDEDF9" stroke="#45556A" stroke-width="3"/>'
 b+='<circle cx="180" cy="87" r="3" fill="#333"/>'
 b+=text(180,137,'Display / graphics path',14,color=BLUE,weight='bold')
 b+=text(180,172,'Camera / microphones',11)
 b+='<path d="M42 235 L318 235 L343 342 L17 342 Z" fill="#E4E7EB" stroke="#45556A" stroke-width="2"/>'
 b+='<rect x="67" y="248" width="226" height="44" rx="4" fill="#FAFAFC" stroke="#8D929A"/>'
 b+=text(180,270,'Keyboard / input',12)
 b+='<rect x="139" y="302" width="82" height="28" rx="4" fill="#C3C7D0" stroke="#8D929A"/>'
 b+=row(377,'Core / power / storage','CPU, RAM,board,storage,main battery',PF,P,67)
 b+=row(460,'I/O / thermal / connectivity','Ports,cooling,audio,webcam,Wi-Fi/Bluetooth',BF,BLUE,67)
 b+=foot(565,'Slots,drives,fans and modules are not universal.',
              'No laptop is opened or physically inspected here.')
 return svg(360,615,b)

def port_icon(kind,x,y):
 if kind in ['USB-A','USB-C','Thunderbolt']:
  rx=0 if kind=='USB-A' else 12
  out=f'<rect x="{x}" y="{y}" width="61" height="26" rx="{rx}" fill="#E9EDF2" stroke="#35465C" stroke-width="2"/>'
  if kind=='USB-A':out+=f'<rect x="{x+7}" y="{y+8}" width="47" height="9" fill="#62778B"/>'
  else:out+=f'<rect x="{x+9}" y="{y+9}" width="43" height="8" rx="4" fill="#62778B"/>'
  return out
 if kind=='HDMI':return f'<path d="M{x} {y} L{x+61} {y} L{x+51} {y+26} L{x+10} {y+26} Z" fill="#E9EDF2" stroke="#35465C" stroke-width="2"/>'
 if kind=='Ethernet':
  out=f'<path d="M{x} {y} H{x+61} V{y+24} H{x+43} V{y+31} H{x+18} V{y+24} H{x} Z" fill="#E9EDF2" stroke="#35465C" stroke-width="2"/>'
  for i in range(8):out+=f'<rect x="{x+9+i*6}" y="{y+4}" width="3" height="9" fill="#BB8B31"/>'
  return out
 if kind=='Audio':return f'<circle cx="{x+30}" cy="{y+13}" r="15" fill="#E9EDF2" stroke="#35465C" stroke-width="2"/><circle cx="{x+30}" cy="{y+13}" r="6" fill="#35465C"/>'
 out=f'<path d="M{x} {y} H{x+61} L{x+55} {y+29} H{x+6} Z" fill="#E9EDF2" stroke="#35465C" stroke-width="2"/>'
 for r in range(3):
  for c in range(5):out+=f'<circle cx="{x+11+c*9.5}" cy="{y+7+r*7}" r="1.7" fill="#35465C"/>'
 return out

def ports():
 b=heading('Port shapes: recognition only','Simplified schematics,not exact electrical pinouts')
 data=[('USB-A','USB-A','Check implemented USB capabilities'),('USB-C','USB-C','Oval shape;features need documentation'),
       ('HDMI','HDMI','Digital display/audio where supported'),('Ethernet','8P8C Ethernet / RJ45-style','Not a telephone/RJ11 jack'),
       ('Audio','3.5mm analog audio','Headphone/mic roles vary'),('VGA','VGA (DE-15)','Traditional analog video'),
       ('Thunderbolt','Thunderbolt3/4/5 shape','Same USB-C outline;check marks/manual')]
 for i,(kind,n,d) in enumerate(data):
  y=79+76*i;b+=port_icon(kind,37,y)
  b+=text(126,y+8,n,11.2,anchor='start',weight='bold',color=P)
  b+=text(126,y+30,d,9.7,anchor='start')
 b+=foot(638,'Older Thunderbolt1/2 used MiniDP-style connectors.',
              'Position/appearance alone does not prove capability.')
 return svg(360,685,b)

def usb():
 b=heading('Same USB-C shape:check the function')
 b+=port_icon('USB-C',150,74)
 b+=row(135,'Connector form','Not a protocol / speed / charging guarantee',BF,BLUE,70)
 b+=row(236,'Actual implementation and cable','USB data,video modes,PD and/or Thunderbolt',PF,P,70)
 b+=row(337,'Verify model-specific documentation','Mac mini front USB3 differs from rear TB4',GF,GREEN,70)
 b+=foot(452,'No hardware probe or PD negotiation is performed.',
              'Published rates are not measured file-transfer speed.')
 return svg(360,500,b)

def specs():
 return chain('Defensible current specification method',[
  ('Exact model / selected configuration','Do not mix base and upgrade columns'),
  ('CPU / memory / storage / GPU / display','Record actual documented/observed values'),
  ('Ports / connectivity / OS','Shape alone is not complete capability'),
  ('Source + date + evidence scope','Mark unknown;do not claim worldwide newest')],500,
  footer=('References checked29Oct2026;no device benchmark.',
          'Apple Silicon examples are not Windows servicing.'))

def safety():
 return chain('Identification is not hazardous repair',[
  ('Authorized device + exact service manual','Use suitable instructor/trained supervision'),
  ('Specified power isolation / approved ESD','No improvised mains/grounding connections'),
  ('Observe only permitted components/ports','Do not force plugs or touch exposed contacts'),
  ('Record actual evidence / unknowns','No physical/electrical results are fabricated')],502,
  footer=('Never open PSU/charger/monitor enclosures.',
          'No voltage probes,firmware clear or battery work.'))

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for n,draw in zip(TITLES,[types,block,cpu,board,layers,firmware,laptop,ports,usb,specs,safety]):
  (DIAG_DIR/(n+'.svg')).write_text(draw())
 print('Hardware Unit 1 diagrams:',len(TITLES))

if __name__=='__main__':main()
