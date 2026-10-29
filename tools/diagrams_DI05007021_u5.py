"""Eight compact self-contained cyber-security concept/evidence SVGs."""
from flowchart_lib import svg,text,arr,rbox,P
from diagrams_DI05007021_u1 import heading,foot,row,BLUE,BF,GREEN,GF,ORANGE,OF,PF,RED,RF
from subject_DI05007021 import DIAG_DIR
TITLES={'sec5_risk':'Threat, Weakness, Action and Impact','sec5_malware':'Malware and Capability Distinctions',
 'sec5_attacks':'Network-Attack Concepts and Limits','sec5_sqli':'SQL Structure versus Bound Data',
 'sec5_phishing':'Pause, Check and Verify','sec5_crime':'Cybercrime, Privacy and Safety',
 'sec5_defence':'Prevent, Detect, Respond, Recover','sec5_kali':'Signed Metadata Is Not an ISO or OS Boot'}

def chain(title,items,height,footer=()):
 b=heading(title)
 for i,(n,d) in enumerate(items):
  y=72+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=foot(height-45,*footer)
 return svg(360,height,b)

def risk():
 return chain('Separate potential, weakness and action',[
  ('Asset and security objective','Data, services, accounts and personal safety'),
  ('Threat / vulnerability','Potential harm versus a relevant weakness'),
  ('Attempt / event and consequences','Investigate what happened and its impact')],422,
  footer=('A symptom alone does not prove an attacker.',
          'Authorization, evidence and context matter.'))

def malware():
 b=heading('Malware categories can overlap')
 data=[('Virus','Host/infection/execution mechanism'),('Worm','Self-propagation between systems'),
       ('Trojan','Malicious function presented as useful'),('Adware / spyware','Advertising behaviour / covert monitoring'),
       ('Botnet / backdoor','Coordinated control / unauthorized access')]
 for i,(n,d) in enumerate(data):b+=row(65+79*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,64)
 b+=foot(494,'No malware, bot/C2 or persistence is created.',
              'Benign file hashes do not classify malware.')
 return svg(360,542,b)

def attacks():
 b=heading('Do not infer an attack from one symptom')
 for i,(n,d) in enumerate([
  ('DoS / DDoS','Malicious availability disruption / distributed'),
  ('MITM / on-path interference','Unauthorized interposition in communication'),
  ('IP spoofing / ARP spoofing','Source-IP claim / local address mapping')]):
  b+=row(76+105*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,76)
 b+=foot(419,'No floods, poisoned caches or forged packets.',
              'Rate/ARP exercises are only logical fixtures.',
              'The TLS identity check uses owned loopback.')
 return svg(360,490,b)

def sqli():
 b=heading('Keep SQL structure separate from values')
 b+=row(68,'Application-owned query structure','SELECT ... WHERE code = ?',BF,BLUE,70)
 b+=row(168,'Bind the input value through the API','Do not concatenate untrusted SQL syntax',PF,P,70)
 b+=arr([(180,138),(180,168)],P);b+=arr([(180,238),(180,272)],P)
 b+=row(272,'Actual own in-memory SQLite results','Normal C01: 1 row; bound SQL-like input: 0',GF,GREEN,72)
 b+=foot(397,'Both fictional records remain intact.',
              'Binding values is not application authorization.',
              'No external database/account is attacked.')
 return svg(360,464,b)

def phishing():
 return chain('Pause and verify through a trusted route',[
  ('Notice the unexpected request','Display names, urgency or links are hints'),
  ('Read the actual address/hostname','A familiar prefix or @ text can mislead'),
  ('Use a separately known trusted channel','Do not verify via the suspicious message'),
  ('Report/handle safely under policy','No password/passcode or private-data reply')],500,
  footer=('HTTPS or perfect grammar is not legitimacy proof.',
          'Only neutral offline strings/headers are parsed.'))

def crime():
 b=heading('Course categories, not legal findings')
 data=[('Identity / information theft','Identity misuse versus unauthorized data theft'),
       ('Unauthorized hacking','Not every authorized security activity'),
       ('Cyberstalking','Protect privacy and seek appropriate support'),
       ('Malware distribution','Do not obtain/run/spread dangerous samples')]
 for i,(n,d) in enumerate(data):b+=row(69+89*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,70)
 b+=foot(457,'Preserve appropriate evidence safely.',
              'Use trusted institutional/official channels.',
              'Immediate danger: seek local emergency help.')
 return svg(360,527,b)

def defence():
 return chain('A coordinated defensive cycle',[
  ('PREVENT','Appropriate updates, access and input controls'),
  ('DETECT','Relevant trusted evidence and investigation'),
  ('RESPOND','Authorized containment/reporting procedures'),
  ('RECOVER','Restore known-good data/services and verify')],493,
  footer=('A changed hash is not an intrusion verdict.',
          'One file copy is not full incident recovery.'))

def kali():
 b=heading('Three evidence stages in Kali study')
 b+=row(76,'1. Signed manifest under a pinned key','ACTUAL GPG check of frozen2026.3 metadata',GF,GREEN,75)
 b+=arr([(180,151),(180,185)],P)
 b+=row(185,'2. Hash and compare actual ISO bytes','NOT DONE: no image bytes downloaded',OF,ORANGE,75)
 b+=arr([(180,260),(180,294)],P)
 b+=row(294,'3. Install/boot/study an isolated VM','GUIDED ONLY: no Kali OS is booted',PF,P,75)
 b+=foot(425,'Metadata authenticity is not missing-image integrity.',
              'No ISO/VM, offensive toolkit or secret key shipped.',
              'Check current authentic versions/keys for new use.')
 return svg(360,496,b)

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for n,draw in zip(TITLES,[risk,malware,attacks,sqli,phishing,crime,defence,kali]):
  (DIAG_DIR/(n+'.svg')).write_text(draw())
 print('Unit 5 diagrams:',len(TITLES))

if __name__=='__main__':main()
