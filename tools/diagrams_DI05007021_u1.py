"""Eight compact mobile SVGs; no external assets, CSS, markers or fonts."""
from flowchart_lib import svg,text,arr,rbox,decision,P
from subject_DI05007021 import DIAG_DIR
BLUE='#1565C0';BF='#EAF3FD';GREEN='#2E7D32';GF='#EAF6EC'
ORANGE='#B66A00';OF='#FFF4DF';PF='#F2EBFA';RED='#BD2543';RF='#FDECF0'
TITLES={'sec1_cia':'CIA Security Goals','sec1_attacks':'Passive and Active Attacks',
 'sec1_dos':'DoS, DDoS and Ordinary Outages','sec1_services':'Five Syllabus Security Services',
 'sec1_authz':'Authentication, Authorization and Enforcement',
 'sec1_specific':'Eight Specific Security Mechanisms',
 'sec1_pervasive':'Five Pervasive Security Mechanisms',
 'sec1_diagnose':'Safe Layer-by-Layer Diagnosis'}

def heading(title,sub=None):
 b=text(180,24,title,14,weight='bold',color=P)
 if sub:b+=text(180,48,sub,10.5,color='#666')
 return b

def foot(y,*lines):
 return ''.join(text(180,y+17*i,s,10.2,color='#666') for i,s in enumerate(lines))

def row(y,name,detail,fill=PF,color=P,h=62):
 return (f'<rect x="18" y="{y}" width="324" height="{h}" rx="8" fill="{fill}" stroke="{color}" stroke-width="1.6"/>'
  +text(180,y+23,name,12,weight='bold',color=color)+text(180,y+45,detail,10.7))

def cia():
 b=heading('CIA: three core security goals','Example asset: a college result portal')
 b+=row(76,'CONFIDENTIALITY','Authorized access and disclosure',BF,BLUE,70)
 b+=row(164,'INTEGRITY','No improper change or destruction',PF,P,70)
 b+=row(252,'AVAILABILITY','Timely, reliable access and use',GF,GREEN,70)
 b+=foot(359,'One event can harm more than one goal.',
              'No single mechanism guarantees all three.')
 return svg(360,404,b)

def attacks():
 b=heading('Attacks: observe or interfere?')
 b+=rbox(180,113,324,112,'PASSIVE\nObserve without changing data/system\nMessage contents; traffic analysis',BF,BLUE,11.6)
 b+=rbox(180,278,324,146,'ACTIVE\nAlter, impersonate, replay or disrupt\nMasquerade; replay; modification; DoS',OF,ORANGE,11.2)
 b+=foot(394,'Passive does not mean harmless.',
              'Encrypted content can still expose traffic patterns.')
 return svg(360,443,b)

def dos():
 b=heading('An outage is not always an attack')
 b+=rbox(180,89,324,56,'Legitimate users need a service',BF,BLUE,12)
 b+=arr([(180,117),(180,151)],P)
 b+=rbox(180,184,324,66,'Service access is unavailable',RF,RED,12)
 b+=arr([(180,217),(180,251)],P)
 b+=rbox(180,290,324,78,'Investigate the cause\nAttack? Fault? Maintenance? Permissions?',OF,ORANGE,11)
 b+=row(353,'DoS / DDoS','Malicious denial / distributed participation',PF,P,67)
 b+=foot(455,'Availability is the primary goal affected.',
              'No flood or exhaustion experiment is needed.')
 return svg(360,500,b)

def services():
 b=heading('Services: what protection is supplied?')
 rows=[('Confidentiality','Restrict unauthorized disclosure',BF,BLUE),
  ('Integrity','Protect against improper change/destruction',PF,P),
  ('Authentication','Establish a claimed identity or data origin',GF,GREEN),
  ('Access control','Prevent unauthorized use/operations',OF,ORANGE),
  ('Non-repudiation','Evidence against false denial',RF,RED)]
 for i,(n,d,f,c) in enumerate(rows):b+=row(63+80*i,n,d,f,c,65)
 b+=foot(496,'Mechanisms are the means of supplying services.',
              'Availability remains an essential security goal.')
 return svg(360,542,b)

def authz():
 b=heading('A valid identity is not every permission')
 b+=rbox(180,98,324,66,'AUTHENTICATION\nVerify the claimed identity',BF,BLUE,12)
 b+=arr([(180,131),(180,188)],P)
 b+='<rect x="44" y="145" width="272" height="27" fill="white"/>'
 b+=text(180,160,'Continue only after identity verification',10.2,color='#555')
 b+=rbox(180,222,324,68,'AUTHORIZATION\nCheck this subject, operation and resource',PF,P,11.3)
 b+=arr([(180,256),(180,291)],P)
 b+=decision(180,322,'Allowed?',132,62,12)
 b+=arr([(114,322),(90,322),(90,384)],GREEN,label='Yes',lpos=(82,350))
 b+=arr([(246,322),(270,322),(270,384)],RED,label='No',lpos=(283,350))
 b+=rbox(90,411,144,54,'Enforce: allow',GF,GREEN,11.5)
 b+=rbox(270,411,144,54,'Enforce: deny',RF,RED,11.5)
 b+=foot(473,'Failed identity verification is rejected earlier.',
              'Least privilege limits the allowed operations.')
 return svg(360,520,b)

def specific():
 b=heading('Specific security mechanisms (X.800)')
 data=[('Encipherment','Cryptographic transformation'),('Digital signature','Verifiable signing under trust assumptions'),
  ('Access control','Enforce permitted use'),('Data integrity','Protected change / sequence checking'),
  ('Authentication exchange','Establish the claimed identity or origin'),('Traffic padding','Reduce traffic-pattern inference'),
  ('Routing control','Constrain communication paths'),('Notarization','Trusted third-party evidence')]
 for i,(n,d) in enumerate(data):b+=row(62+67*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,56)
 b+=foot(637,'A mechanism can support more than one service.')
 return svg(360,665,b)

def pervasive():
 b=heading('Pervasive security mechanisms (X.800)')
 data=[('Trusted functionality','Trustworthy security-critical functions'),
  ('Security labels','Policy-interpreted security attributes'),('Event detection','Recognize security-relevant events'),
  ('Security audit trail','Protected records for examination'),('Security recovery','Restore an acceptable secure state')]
 for i,(n,d) in enumerate(data):b+=row(62+78*i,n,d,GF if i%2==0 else PF,GREEN if i%2==0 else P,64)
 b+=foot(461,'Support is not confined to one particular service.',
              'Labels and editable logs alone do not enforce security.')
 return svg(360,510,b)

def diagnose():
 b=heading('Diagnose one layer at a time','Only your own system or an authorized lab')
 data=[('1. Local setup','Loopback address and interface'),('2. Name resolution','localhost through the OS resolver'),
  ('3. Path and permissions','Route decision; interpret denied ping honestly'),('4. Service and policy','Owned listening socket; permitted operation')]
 for i,(n,d) in enumerate(data):
  y=80+91*i
  if i:b+=arr([(180,y-27),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,64)
 b+=foot(463,'Loopback success does not prove Internet access.',
              'A failed ping alone does not prove DoS.',
              'A working service is not automatically secure.')
 return svg(360,530,b)

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for name,draw in zip(TITLES,[cia,attacks,dos,services,authz,specific,pervasive,diagnose]):
  (DIAG_DIR/(name+'.svg')).write_text(draw())
 print('Information Security Unit 1 diagrams:',len(TITLES))

if __name__=='__main__':main()
