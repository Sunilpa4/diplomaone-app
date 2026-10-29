"""Ten self-contained mobile Network Security SVGs; all scenario labels explicit."""
from flowchart_lib import svg,text,arr,rbox,P
from diagrams_DI05007021_u1 import heading,foot,row,BLUE,BF,GREEN,GF,ORANGE,OF,PF,RED,RF
from subject_DI05007021 import DIAG_DIR
TITLES={'sec4_zones':'Zones and Controlled Boundaries','sec4_dmz':'Logical DMZ Flow Policy',
 'sec4_vlan':'VLAN Access, Trunk and Routing','sec4_tunnel':'Private TLS Relay Scope',
 'sec4_firewall':'Packet-Filter Policy Evaluation','sec4_stateful':'Small Stateful Teaching Model',
 'sec4_types':'Five Firewall Types','sec4_ids':'IDS Components and Evidence',
 'sec4_hids_nids':'Host and Network Observation','sec4_analysis':'Synthetic PCAP Analysis Provenance'}

def chain(title,items,height,sub=None,footer=()):
 b=heading(title,sub)
 for i,(n,d) in enumerate(items):
  y=72+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=foot(height-45,*footer)
 return svg(360,height,b)

def zones():
 b=heading('Zones are roles, not automatic trust')
 for y,n,d,fill,color in [(72,'Outside / Internet','Treat untrusted communication appropriately',BF,BLUE),
  (184,'DMZ','Separately controlled exposed services',OF,ORANGE),
  (296,'Inside / Intranet','Internal is not automatically safe',GF,GREEN)]:
  b+=row(y,n,d,fill,color,70)
 b+=arr([(180,142),(180,184)],P);b+=arr([(180,254),(180,296)],P)
 b+=foot(420,'Define, enforce and verify boundary policy.',
              'Private addressing is not authentication.')
 return svg(360,470,b)

def dmz():
 b=heading('Logical example: explicit narrow flows','Python policy model, not a configured firewall')
 data=[('Outside -> designated DMZ web','TCP80 allowed in this teaching policy',GF,GREEN),
       ('Outside -> internal assets','Default deny',RF,RED),
       ('DMZ app -> one approved DB','Only exact host/service dependency allowed',BF,BLUE),
       ('DMZ app -> other inside host','Denied; no blanket internal trust',RF,RED)]
 for i,(n,d,f,c) in enumerate(data):b+=row(77+88*i,n,d,f,c,68)
 b+=foot(466,'No packets are sent to the documentation addresses.',
              'The Packet Tracer guides use a separate lab plan.')
 return svg(360,513,b)

def vlan():
 b=heading('VLANs: separate L2 broadcast domains')
 b+=rbox(94,112,152,104,'VLAN10\nHost A / Host B\nSame assigned domain',BF,BLUE,11)
 b+=rbox(266,112,152,104,'VLAN20\nHost C / Host D\nDifferent domain',PF,P,11)
 b+=arr([(94,164),(94,203),(180,203),(180,233)],P)
 b+=arr([(266,164),(266,203),(180,203)],P)
 b+=row(233,'Trunk: selected VLANs10 and20','Tagging does not route or encrypt',OF,ORANGE,71)
 b+=row(342,'Cross-VLAN communication','Needs appropriate L3 path and policy',GF,GREEN,70)
 b+=foot(455,'Membership model / tag bytes are not switch proof.',
              'Packet Tracer configuration remains guided only.')
 return svg(360,505,b)

def tunnel():
 return chain('Actual private application TLS relay',[
  ('Owned client','Requires lab certificate and correct .test name'),
  ('TLS1.3 protected segment','Client -> relay; real handshake'),
  ('Relay terminates TLS','Reads one bounded teaching message'),
  ('Owned plaintext loopback echo','Outside the TLS segment; sockets close')],505,
  footer=('Not IPsec, a system VPN or Packet Tracer tunnel.',
          'No interface, route or trust-store changes.'))

def firewall():
 b=heading('Policy model: first match, then default')
 b+=row(72,'Packet/flow attributes','Addresses, protocol, ports and direction',BF,BLUE,65)
 b+=arr([(180,137),(180,175)],P)
 b+=row(175,'Evaluate ordered rules','First matching action in THIS model',PF,P,65)
 b+=arr([(180,240),(180,274),(90,274),(90,314)],GREEN)
 b+=arr([(180,274),(270,274),(270,314)],RED)
 b+=rbox(90,350,144,72,'Matching allow:\npermitted',GF,GREEN,11.5)
 b+=rbox(270,350,144,72,'Deny / no match:\nrejected',RF,RED,11.5)
 b+=foot(434,'A broad earlier allow can shadow a later deny.',
              'No kernel or router rules are configured.')
 return svg(360,485,b)

def stateful():
 return chain('Small logical state table, not full TCP',[
  ('Permitted initiation: SYN','Store the original tuple/direction'),
  ('Matching reverse SYNACK','Move to the model handshake phase'),
  ('Original-direction ACK','Establish the model session'),
  ('Matching data before TTL expiry','Return path needs stored state'),
  ('Expiry / reset','Old permission is not retained indefinitely')],579,
  footer=('Unsolicited return data is denied.',
          'No sequence validation, NAT or kernel enforcement.'))

def types():
 b=heading('Five firewall types: different context')
 data=[('Packet filtering','Relevant packet headers and rules'),('Stateful inspection','Tracked session/flow context'),
  ('Application-level gateway','Supported application semantics'),('Circuit-level gateway','Session establishment and byte relay'),
  ('Next-generation firewall','Additional application/context/protection')]
 for i,(n,d) in enumerate(data):b+=row(65+80*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,65)
 b+=foot(496,'Products/configuration may combine capabilities.',
              'No type guarantees complete prevention/visibility.')
 return svg(360,543,b)

def ids():
 return chain('IDS: observation -> analysis -> evidence',[
  ('Sensors / host agents','Collect selected relevant observations'),('Analysis and rules/baselines','Evaluate appropriate detection logic'),
  ('Protected alert / event store','Keep context, times and useful records'),('Management / investigation','Check health, tune and respond appropriately')],497,
  footer=('An alert is not confirmed maliciousness.',
          'IDS detection is not automatic IPS blocking.'))

def hostnetwork():
 b=heading('Complementary views, not all-seeing tools')
 b+=rbox(180,143,324,145,'HIDS: selected host context\nFiles / logs / processes\nNeeds agent access, trusted baseline and upkeep\nA compromised host may tamper with evidence',BF,BLUE,10.8)
 b+=rbox(180,330,324,145,'NIDS: monitored network paths\nPackets / flows at appropriate sensors\nPlacement, encryption and packet loss matter\nOff-path traffic is not automatically visible',PF,P,10.8)
 b+=foot(454,'False positives and false negatives both matter.',
              'The six-case metrics are not a product benchmark.')
 return svg(360,503,b)

def analysis():
 return chain('Actual offline analysis; honest origin',[
  ('Construct 16 harmless synthetic frames','Fake/local MACs; documentation IPs; .test'),
  ('Owned synthetic.pcap','Not live capture or Packet Tracer output'),
  ('Actual TShark -n -r dissection','ARP / DNS / TCP / HTTP / VLAN tags'),
  ('Interpret fields, checksums and filters','Correct bytes are not deployment security')],506,
  footer=('Wireshark GUI and Packet Tracer are guided.',
          'No foreign traffic or live capture is used.'))

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for n,draw in zip(TITLES,[zones,dmz,vlan,tunnel,firewall,stateful,types,ids,hostnetwork,analysis]):
  (DIAG_DIR/(n+'.svg')).write_text(draw())
 print('Unit 4 diagrams:',len(TITLES))

if __name__=='__main__':main()
