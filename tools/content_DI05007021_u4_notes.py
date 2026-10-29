"""Network Security: English syllabus notes with explicit evidence boundaries."""
from subject_DI05007021 import tr
from content_DI05007021_u1_notes import ul,table,topic
SOURCES=[
 ('GTU DI05007021 syllabus, 2026–27','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf'),
 ('NIST SP800-41r1: firewall technologies/policy (2009 fundamentals)','https://csrc.nist.gov/pubs/sp/800/41/r1/final'),
 ('NIST SP800-94: IDPS principles/components (2007; later draft retired)','https://csrc.nist.gov/pubs/sp/800/94/final'),
 ('Cisco: IEEE802.1Q frame format (historical format reference)','https://www.cisco.com/c/en/us/support/docs/lan-switching/8021q/17056-741-4.html'),
 ('Cisco: NGFW feature overview (vendor description, not a performance guarantee)','https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-next-generation-firewall.html'),
 ('RFC1928: SOCKS5 connection/relay framework','https://www.rfc-editor.org/rfc/rfc1928.html'),
 ('RFC2003: IP encapsulation and tunnel endpoints','https://www.rfc-editor.org/rfc/rfc2003.html'),
 ('Wireshark user guide: introduction and limits','https://www.wireshark.org/docs/wsug_html_chunked/ChapterIntroduction.html'),
 ('TShark command reference','https://www.wireshark.org/docs/man-pages/tshark.html'),
 ('Wireshark display-filter expressions','https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html'),
 ('Cisco Networking Academy: Packet Tracer','https://www.netacad.com/cisco-packet-tracer'),
 ('RFC8446: TLS1.3','https://www.rfc-editor.org/rfc/rfc8446.html')]
NOTES=[
 {'title':tr('1. Security Topologies and Boundaries'),'items':[
  topic('1.1 Security zones, Internet and Intranet',
   '<p>A <b>security zone</b> groups systems with an intended security posture or role. A boundary controls communication between zones; merely naming a zone does not enforce a policy.</p>'+table(['Term','Meaning','Security implication'],[
    ('Internet','Interconnected external networks and public services.','Treat untrusted traffic appropriately; a reachable address does not establish identity.'),
    ('Intranet','An organization’s internal network/services.','Internal does not mean automatically safe; insiders and compromised endpoints can still cause harm.'),
    ('Security boundary','A point or set of controls separating roles/postures.','Define allowed flows, enforce them, monitor and verify both permitted and denied cases.')])+
   '<p>Addressing, physical layout and security trust are different concepts. A private IP address is not authentication. Apply least privilege, suitable ingress/egress controls, source validation and appropriate IPv4/IPv6 policy; the classroom policy code is IPv4-only and not real network enforcement.</p>','sec4_zones'),
  topic('1.2 DMZ placement and an explicit flow policy',
   '<p>A <b>DMZ</b> is a separately controlled network segment for services that need exposure beyond the internal network. It reduces uncontrolled direct access to internal assets; it is not automatically a trusted or secure zone.</p>'+table(['Logical example flow','Intended decision','Reason'],[
    ('Outside → designated DMZ web server TCP80','Allow the named service.','Only a required published service, not all DMZ ports.'),
    ('Outside → internal network','Deny by default.','Do not expose internal assets directly.'),
    ('DMZ app → one approved internal DB TCP5432','Allow only that exact backend in this model.','An explicit narrow business dependency, not unrestricted DMZ-to-LAN access.'),
    ('DMZ app → other internal host/service','Deny.','A compromised exposed service should not gain blanket internal reachability.')])+
   '<p>The executed model uses RFC5737 documentation ranges: outside 192.0.2.0/24, DMZ 198.51.100.0/24 and inside 203.0.113.0/24. It sends no traffic there. Packet Tracer guides use a separate simulated IP plan and a different minimal policy, clearly labelled; they were not executed. The teaching HTTP port80 policy is not a confidentiality mechanism.</p>','sec4_dmz',programs=['sec4p01']),
  topic('1.3 VLANs, access ports, trunks and inter-VLAN routing',
   '<p>A <b>VLAN</b> separates a Layer-2 broadcast domain logically. An access port typically carries one assigned VLAN for its endpoint. A trunk can carry selected VLANs between devices; IEEE802.1Q inserts a four-byte tag with a 12-bit VLAN identifier.</p>'+ul(
    'Ordinary VLAN IDs are 1–4094; ID0 has priority-tag meaning and 4095 is reserved. This lab uses 10 and 20.',
    'Hosts in different VLANs need an appropriate Layer-3 path to communicate. A trunk is not itself a router or permission to connect all VLANs.',
    'VLANs do not encrypt frames and are not VPNs. Correct port/trunk configuration, allowed VLAN lists, controlled routing and policy still matter.',
    'The Python same-VLAN rule is only a logical model. Actual TShark dissects two constructed802.1Q frames; tag bytes in a file do not prove a switch enforced segmentation.',
    'A failed ping alone may reflect addressing, gateways, links or ACLs; verify the setup before claiming isolation.') ,'sec4_vlan',programs=['sec4p04']),
  topic('1.4 Tunneling, encapsulation and the actual TLS byte relay',
   '<p><b>Tunneling</b> carries one communication representation inside another between tunnel endpoints. Encapsulation alone is not encryption: IP-in-IP is an example of carrying an IP datagram within an outer IP packet. Confidentiality/authentication require the relevant protection scheme and trust model.</p>'+ul(
    'Distinguish original endpoints, encapsulator/entry and decapsulator/exit. Policy must account for what is visible before, within and after a tunnel.',
    'An encrypted tunnel can limit an intermediate sensor’s payload visibility; its endpoints and the decrypted segment still need protection.',
    '<b>Actual example:</b> one framed teaching message crosses a real private TLS1.3 client-to-relay connection, then an owned plaintext loopback connection to an echo endpoint. The client requires the correct lab server certificate/hostname under an explicitly supplied lab root; client-certificate authentication (mutual TLS) is not performed.',
    'This is a bounded application-byte relay, not IPsec, a system-wide VPN, a SOCKS implementation or a Packet Tracer tunnel. No routes, interfaces or system trust stores change; all sockets, workers and temporary keys close.') ,'sec4_tunnel',programs=['sec4p08'])]},
 {'title':tr('2. Firewalls and Their Types'),'items':[
  topic('2.1 Why firewalls are needed; packet filtering and rule policy',
   '<p>A <b>firewall</b> controls network/host traffic according to policy. Place enforcement at the relevant boundary and define direction, addresses, protocols, services and exceptions. Prefer justified minimal permissions, verify expected denies/allows, and protect configuration/logs.</p>'+ul(
    '<b>Packet filtering:</b> examines header information such as source/destination IP, protocol and ports. A basic stateless filter evaluates packets without a full connection-state context.',
    'The executed Python model uses explicit <b>first match</b>, then default deny. An earlier broad allow can shadow a later specific deny; real products’ semantics must be checked.',
    'Rules do not establish that source addresses are authentic. Consider anti-spoofing, asymmetric paths, IPv6, fragmentation and other platform behaviour; these are not implemented by the small model.',
    'A firewall is not a complete security program or a guarantee against endpoint compromise, allowed-channel attacks or application vulnerabilities. No kernel firewall is installed/configured by these examples.') ,'sec4_firewall',programs=['sec4p02']),
  topic('2.2 Stateful inspection and controlled return traffic',
   '<p>A <b>stateful inspection firewall</b> associates packets with tracked connection/flow state and policy, rather than treating a return packet’s TCP flag alone as proof that it belongs to an approved session.</p>'+ul(
    'For a permitted TCP initiation, track the relevant addresses, ports, protocol, direction and lifecycle. Match appropriate return traffic against that stored state.',
    'State needs timeouts and resource management. Expired or unsolicited traffic must not automatically inherit an old permission.',
    'A router ACL keyword such as established, when available, may only test ACK/RST flags; it is not the same as a real state table.',
    'The executed model tracks a declared SYN → matching SYNACK → ACK sequence, return data and TTL on a synthetic clock. It is not RFC-complete TCP: no sequence validation, retransmission, NAT, fragmentation or kernel filtering is claimed.') ,'sec4_stateful',programs=['sec4p03']),
  topic('2.3 Application-level gateway',
   '<p>An <b>application-level gateway / application proxy</b> mediates supported application communication and may inspect protocol-specific operations, content or authorization according to its design. It can distinguish requests sharing the same TCP port, unlike a header-only rule.</p>'+ul(
    'Example goal: allow an approved HTTP course request but reject a disallowed path. This is application policy, not just “TCP80 allowed.”',
    'Advantages can include protocol-aware control and useful application logs; limitations include supported-protocol scope, resource demands, configuration complexity and the need for a correct parser.',
    'Encrypted payload is not automatically visible. Authorized termination/inspection has trust, privacy and operational implications.',
    'Our real owned loopback example returns 200 for GET /course and 403 for /admin, then closes. Its tiny bounded allow-list is NOT a complete HTTP parser, WAF, deployed firewall or production proxy.') ,programs=['sec4p07']),
  topic('2.4 Circuit-level gateway',
   '<p>A <b>circuit-level gateway</b> controls establishment/relay of communication sessions according to its policy, rather than necessarily understanding each application command/content item. SOCKS provides a useful connection/relay framework example; RFC1928 describes a shim between application and transport, not a network-layer ICMP gateway.</p>'+ul(
    'It may control which clients can establish which connections and may use an authentication method, depending on the scheme/configuration.',
    'Relaying a permitted byte stream does not by itself identify harmful application content or encrypt it.',
    'Do not confuse connection mediation, full application inspection, encryption and IP-level routing; products may combine functions.',
    'No SOCKS protocol or circuit-gateway product is implemented/tested here. The separate TLS byte-relay example illustrates only its explicitly stated local transport scope.') ),
  topic('2.5 Next-generation firewalls and comparison',
   '<p>A <b>next-generation firewall (NGFW)</b> combines state-aware network control with additional application/user context and capabilities such as integrated intrusion prevention, depending on the product and enabled features. Feature labels do not guarantee complete prevention or visibility into encrypted payloads.</p>'+table(['Syllabus type','Primary decision context','Important limitation'],[
    ('Packet filtering','Packet headers and rule policy.','Limited application/session context in a basic stateless design.'),
    ('Stateful inspection','Tracked flow/session state plus policy.','State handling, resource use, paths and implementation correctness matter.'),
    ('Application-level gateway','Supported application/protocol semantics.','Parser/protocol support, trust/privacy and resource trade-offs.'),
    ('Circuit-level gateway','Session establishment and byte relay.','Does not necessarily inspect application commands/content.'),
    ('NGFW','Combined state/application/context and additional protections.','Capabilities/configuration/licensing vary; no universal encrypted-traffic or malware guarantee.')])+
   '<p>The unit does not run an NGFW, ASA, Snort/Suricata appliance or a commercial benchmark. Cisco’s feature overview is used as a vendor description, not evidence of measured performance.</p>','sec4_types')]},
 {'title':tr('3. Intrusion Detection Systems'),'items':[
  topic('3.1 Intruders, intrusion detection and prevention',
   '<p>An <b>intrusion</b> involves attempted or actual violation of a security policy. An intruder may be an outsider, a masquerader using someone else’s identity or an insider misusing authorized access. Unusual behaviour is a reason to investigate, not automatic proof of malicious intent.</p>'+ul(
    '<b>IDS:</b> observes relevant events, analyzes them and generates records/alerts. <b>IPS:</b> may actively block/prevent traffic or actions when deployed for that purpose. Detection alone is not blocking.',
    'Signature/pattern matching, anomaly detection and stateful protocol analysis are detection approaches. HIDS/NIDS describe where observations are collected; these are different classification axes.',
    'False positives are benign activity flagged as suspicious. False negatives are relevant malicious/violating activity that is missed.',
    'An attacker can try to avoid sensors, exploit visibility gaps or overload analysis. Correct placement, tuning, updates, evidence and response processes matter.') ),
  topic('3.2 IDS components and the evidence pipeline',
   table(['Component','Purpose'],[
    ('Sensors / host agents','Collect selected packets, logs, file/process or other host/network events.'),
    ('Analysis engine','Apply appropriate rules, baselines or protocol analysis to observations.'),
    ('Configuration / knowledge base','Maintain policies, signatures/baselines and tuning information.'),
    ('Event / alert storage','Keep relevant protected records with useful context and time information.'),
    ('Management console / response integration','Present alerts, manage health/configuration and support authorized investigation/response.')])+
   '<p>Protect the monitoring system itself. Sensor health, packet/event loss, clock consistency, protected logs, appropriate access control and an investigation workflow affect the usefulness of results. A dashboard or isolated rule does not prove that every network path was observed.</p>','sec4_ids'),
  topic('3.3 Host-based IDS: strengths and limitations',
   '<p><b>HIDS</b> collects evidence at a host, such as relevant logs, file-integrity observations, processes or configuration changes.</p>'+table(['Advantages','Disadvantages / conditions'],[
    ('Detailed local context and visibility of selected host activity.','Requires appropriate host deployment, permissions, maintenance and resources.'),
    ('May inspect application-level information available at the endpoint, including data after authorized decryption.','This visibility is not automatic for all apps/data and raises access/privacy concerns.'),
    ('Can detect selected file/configuration changes.','Baseline trust and legitimate updates matter; a compromised host may tamper with the agent or evidence.')])+
   '<p>The executed file-hash fixture really changes/restores an owned temporary file. It demonstrates change detection only, not who acted, maliciousness, prevention or a deployed HIDS/EDR product.</p>',programs=['sec4p09']),
  topic('3.4 Network-based IDS: strengths and limitations',
   '<p><b>NIDS</b> analyzes network observations at suitable monitoring points, such as an authorized TAP/mirror feed or an appropriate sensor position.</p>'+table(['Advantages','Disadvantages / conditions'],[
    ('Can observe multiple hosts/flows on the monitored path.','Unobserved VLANs, routes or switched traffic are not magically visible; placement and feed configuration matter.'),
    ('Can identify selected network patterns and correlate traffic context.','Encryption limits payload inspection without appropriate authorized visibility; packet loss and throughput can affect analysis.'),
    ('Can be deployed without an agent on every endpoint.','It may lack host/process/user context and still requires maintenance, tuning and investigation.')])+
   '<p>Wireshark/TShark is a packet analyzer, <b>not automatically an IDS</b>. The executed NIDS-style rule uses three invented records; it does not run Snort/Suricata, observe a live network or confirm an intruder.</p>',programs=['sec4p10']),
  topic('3.5 Combine HIDS/NIDS evidence and interpret alert quality',
   '<p>Host and network observations can complement one another. Choose sensors for the asset/threat, confirm coverage and correlate protected evidence rather than expecting a single tool to see everything.</p>'+table(['Outcome','Meaning'],[
    ('True positive (TP)','Relevant ground-truth event correctly flagged.'),('False positive (FP)','Benign ground-truth event flagged.'),
    ('False negative (FN)','Relevant ground-truth event missed.'),('True negative (TN)','Benign ground-truth event not flagged.')])+
   '<p>The actual six-case teaching fixture gives TP 2, FP 1, FN 1, TN 2. Precision=TP/(TP+FP)=2/3; recall=TP/(TP+FN)=2/3; false-positive rate=FP/(FP+TN)=1/3. These are hand-labelled fixture calculations, <b>not measured production IDS accuracy, an AI model or a performance benchmark</b>.</p>','sec4_hids_nids',programs=['sec4p11'])]},
 {'title':tr('4. Honest Practical Evidence and Guided Simulation'),'items':[
  topic('4.1 Practical 7: actual offline TShark protocol analysis',
   '<p>The kit supplies <code>synthetic.pcap</code>, a code-constructed 16-frame Ethernet fixture with fake local MACs, documentation-only IPv4 addresses and reserved .test names. It is <b>not a live capture or Packet Tracer output</b>.</p>'+ul(
    'Actual TShark 4.4.19 dissects ARP, DNS, a complete small TCP/HTTP exchange and two tagged UDP frames. The protocol-column labels are ARP2,DNS2,HTTP2,TCP8,UDP2; filter counts overlap because HTTP runs over TCP and DNS over UDP.',
    'The DNS response maps portal.diploma.test to 198.51.100.10; the HTTP request is GET /course and response 200. Frames 15/16 carry VLAN IDs 10/20.',
    'Use <code>tshark -n -r synthetic.pcap -Y dns</code> for authorized offline inspection; -n disables name resolution. No interface capture or remote lookup is required.',
    'Wireshark GUI opening/filter/follow-stream steps are supplied as guidance, not claimed as executed. No actual TLS traffic appears in this PCAP; the separate live loopback TLS example is not a recorded capture.',
    'Fixed teaching timestamps and correct synthetic packets are not evidence of real network timing, ownership, attack detection or deployment security.') ,'sec4_analysis',programs=['sec4p05']),
  topic('4.2 Filters, checksums and limits of packet evidence',
   '<p><b>Capture filters</b> use capture/BPF syntax, for example <code>tcp port 80</code>. <b>Display filters</b> use Wireshark syntax, for example <code>tcp.port == 80</code>. Do not substitute one for the other.</p>'+ul(
    'Actual offline filtering finds 10 TCP-port80 frames and 2 HTTP frames. Passing the BPF form as a -Y display expression is actually rejected with an unexpected-token diagnostic; no capture-filter execution is claimed.',
    'The DNS, HTTP and VLAN fields are actually extracted. With explicit checksum preferences, all present IP/TCP/UDP checksums validate as Good. In the tested 4.4.19 enumeration, Good=1, Bad=0 and Unverified=2.',
    'A correct checksum is not cryptographic authentication, a firewall rule or a proof of a trusted sender. In other real captures, checksum offload and capture conditions can also affect interpretation.',
    'Use only owned/instructor-authorized traffic and avoid sharing sensitive payloads/addresses/credentials. Do not grant extra capture privileges or disable security just to force a lab result.') ,programs=['sec4p06','sec4p12']),
  topic('4.3 Practicals 8–10: Packet Tracer guides, not fabricated runs',
   table(['Official practical','Included guided activity','Honest boundary'],[
    ('8: VLAN simulation','Two-switch access/trunk/VLAN10/20 setup, IP plan and same/cross-VLAN checks.','No Packet Tracer/switch run or .pkt/.pka file is claimed.'),
    ('9: DMZ simulation','Separate simulated WAN/DMZ/inside segments and a three-interface router plan.','Zone labels alone do not enforce isolation; inspect routing before/after policy.'),
    ('10: firewall simulation','Illustrative router extended-ACL packet-filter policy with one permitted HTTP path and denied internal paths.','Guided device-dependent syntax, not tested ASA/stateful/NGFW commands or production policy.')])+
   '<p>The supplied Markdown guides distinguish suggested expected results from observations. Build/save your own authorized simulator project and record actual outcomes. Interface names/features vary by model/version. Source-port or ACK/RST matching in an ACL is not genuine connection-state tracking. A ping failure alone does not establish the intended security policy.</p>'+ '<p>Python logical models, TShark dissection and the private application examples are supporting evidence, <b>not substitutes represented as successful Packet Tracer execution</b>. No host VLAN/router/firewall configuration is changed.</p>'),
  topic('4.4 Evidence classes, practical journal and assessment',
   table(['Evidence class','What actually runs'],[
    ('Logical models','DMZ flow policy, ordering/default deny, tiny state table, VLAN membership and an invented NIDS-style rule.'),
    ('Real local operations','Offline TShark dissection/checksums/filter rejection; owned loopback HTTP200/403; a private TLS1.3 byte relay; owned file-change hashing.'),
    ('Guided only','Wireshark GUI/live capture; Packet Tracer VLAN/DMZ/firewall; circuit/NGFW appliances; Snort/Suricata deployment.')])+
   '<p>The twelve scripts use provided helpers at the extracted ZIP root. Python standard library is sufficient for models; analysis requires TShark, and the private TLS example requires OpenSSL 3. No pip packages, binaries or real private keys are shipped. Live listeners/workers/temporary keys close at the end of each example.</p>'+ul(
    'Record tool/version, actual command or fixture, outcome, interpretation and limits. Do not replace a failed/guided task with invented output.',
    'The course remains 70+30 theory and 20+30 practical=150. Unit 4 is 9 hours/20% syllabus weight, not a guaranteed paper allocation.',
    'The sixteen answered questions are original revision exercises with suggested 3/4/7-mark sizes, not official GTU papers, marks or a predicted pattern.')+
   '<p><b>References:</b> '+', '.join('<a href="'+u+'">'+n+'</a>' for n,u in SOURCES)+'. Historical NIST/Cisco documents support fundamentals/format facts, not current vendor benchmarks. The NIST800-94 revision draft never became a final publication and was retired.</p>')]}]

PRACTICE=[
 ('Explain security zones, Internet and Intranet without assuming internal traffic is safe.',4,
  '<p>A zone groups systems by intended role/security posture; a boundary enforces communication policy. Internet refers to external interconnected networks/services; an Intranet is organizational internal networking. Naming a zone or using a private address does not authenticate a user or stop compromise. Define/enforce allowed directions/services, monitor evidence and test denies/allows. Internal systems and insiders can still violate policy.</p>'),
 ('Explain a DMZ topology and four flow-policy decisions.',7,
  '<p>Place exposed services in a separately controlled DMZ between outside access and protected internal assets. In the logical model, outside-to-designated-web TCP80 is allowed, outside-to-inside is denied, one exact app-to-approved-DB TCP5432 dependency is allowed, and other DMZ-to-inside access is denied. These are explicit model decisions, not actual router enforcement. The separate Packet Tracer guide uses a different minimal lab plan/policy and was not executed. A DMZ label alone is not isolation or confidentiality.</p>'),
 ('Differentiate VLAN access/trunk behaviour and inter-VLAN routing.',7,
  '<p>A VLAN separates an L2 broadcast domain. An access port normally serves its assigned VLAN; a trunk carries selected VLANs between devices. An802.1Q tag has a 12-bit VLAN ID in a four-byte tag; ordinary IDs are 1–4094, with 0/4095 special/reserved. Cross-VLAN communication needs an appropriate L3 path and controlled policy. Trunking does not route, encrypt or automatically permit all VLAN traffic. Verify configuration/IP/gateway/link state before interpreting a failed ping.</p>'),
 ('Explain tunneling and why a tunnel does not automatically encrypt.',4,
  '<p>Tunneling carries one representation within another between entry/exit endpoints; IP-in-IP encapsulation itself is not encryption. Separate the original source/destination from tunnel endpoints and consider visibility before/after termination. The actual example negotiates TLS1.3 with a checked owned certificate, relays one framed message, then uses an owned plaintext loopback backend. It is not IPsec, a machine-wide VPN or a Packet Tracer tunnel; protection covers only the TLS segment.</p>'),
 ('Explain packet filtering, rule order and default deny.',4,
  '<p>A basic packet filter evaluates header fields such as addresses, protocol and ports. In the declared first-match Python model, a specific deny before a broad allow rejects the flow; reversing them permits it. With no match, the default is deny. Real product semantics and directions must be checked. Header rules do not authenticate source addresses or fully understand applications. The code models decisions and does not install a host/router firewall.</p>'),
 ('Compare stateless filtering and stateful inspection, including return traffic.',7,
  '<p>Stateless filtering evaluates packets without full stored session context. Stateful inspection tracks relevant flow/session context and policy so matching return traffic can be treated appropriately, with timeouts/lifecycle/resource handling. An unsolicited packet or an ACK/RST flag is not by itself a real established connection. The tiny model checks SYN, matching SYNACK, final ACK, return data and TTL on a synthetic clock, but not sequence validation, NAT, fragments or complete TCP/kernel enforcement.</p>'),
 ('Explain an application-level gateway and the actual200/403 example.',4,
  '<p>An application gateway mediates supported protocol communication and can inspect application operations instead of only ports. It can provide protocol-aware control/logging but depends on parser correctness, protocol support, resources and trust/privacy decisions. The private real loopback example accepts GET /course with200 and rejects /admin with403, then closes all endpoints/workers. Its bounded allow-list is not a full HTTP parser, production WAF, complete proxy or host firewall.</p>'),
 ('Explain a circuit-level gateway and contrast it with application inspection.',4,
  '<p>A circuit-level gateway controls establishment/relay of sessions under its policy, possibly including authentication. It need not inspect each application command/content item. SOCKS is a relevant relay framework between application and transport, not an IP/ICMP forwarding or automatic encryption guarantee. Application gateways can make supported application-semantic decisions. No SOCKS/circuit product is implemented or claimed as tested here.</p>'),
 ('Describe NGFW capabilities and limitations compared with the other four types.',7,
  '<p>Packet filtering uses header/rule context; stateful inspection adds tracked flow state; an application gateway examines supported application semantics; a circuit gateway mediates sessions/relay. An NGFW combines state-aware control with features such as application/user context and integrated prevention depending on product/configuration/licensing. No label guarantees visibility into all encrypted content or prevention of every threat. The unit runs no NGFW appliance or commercial performance benchmark.</p>'),
 ('Define intruder, IDS and IPS and explain why an alert is not proof.',4,
  '<p>An intruder attempts/causes policy violations and may be an outsider, masquerader or insider misusing rights. IDS collects/analyzes observations and alerts; IPS can actively prevent/block when deployed for that role. Unusual or matching activity may be benign, while a real violation may be missed. Investigate protected evidence and context rather than treating an alert as confirmed guilt or assuming detection automatically blocks traffic.</p>'),
 ('Describe IDS components and the evidence pipeline.',7,
  '<p>Sensors/agents collect selected network/host observations; an analysis engine applies relevant methods; rules/baselines/configuration express detection knowledge; protected event/alert storage preserves context; a console/response integration supports health, management and authorized investigation. Sensor placement/health, clock consistency, packet/event loss, protected logs and access control affect reliability. A rule or dashboard alone does not prove full coverage.</p>'),
 ('Compare HIDS and NIDS advantages and disadvantages.',7,
  '<p>HIDS provides selected host/file/process/log context and may observe application data available at its endpoint, but needs agent deployment/permissions/resources, baseline management and protection against tampering. NIDS can observe multiple flows/hosts on the monitored path without agents everywhere, but cannot see off-path/switched traffic automatically, may lack host/user context, and faces encryption/packet-loss/throughput limits. Combine complementary evidence and authorized visibility; neither guarantees complete detection.</p>'),
 ('Explain false positives/negatives and calculate the six-case fixture metrics.',4,
  '<p>TP is a relevant event correctly flagged; FP a benign event flagged; FN a relevant event missed; TN a benign event unflagged. With TP 2, FP 1, FN 1, TN 2, precision=2/(2+1)=0.6667, recall=2/(2+1)=0.6667 and false-positive rate=1/(1+2)=0.3333. These are actual calculations on six hand-labelled teaching cases, not a measured production IDS benchmark or AI accuracy claim.</p>'),
 ('Interpret the synthetic PCAP protocol/filter/checksum evidence.',4,
  '<p>The code constructs16 frames, not a live capture: ARP2,DNS2,HTTP2,TCP8,UDP2 protocol-column labels. Protocol filters overlap: TCP-port80 matches10 and HTTP2. DNS gives portal.diploma.test→198.51.100.10; HTTP GET /course gets200; two UDP frames have VLAN10/20 tags. Present IP/TCP/UDP checksums validate as Good1 under tested TShark 4.4.19. Correct checksums/tag bytes are not authentication, switch-policy enforcement or real network timing evidence.</p>'),
 ('Differentiate capture/display filters and a packet analyzer from IDS.',3,
  '<p>Capture/BPF syntax such as tcp port80 differs from Wireshark display syntax tcp.port==80. The actual offline -Y attempt with BPF form is rejected; no live -f capture is executed. TShark/Wireshark decodes packet data but is not automatically an IDS or a blocking firewall. The displayed subset is not proof that unobserved traffic was absent from the real network.</p>'),
 ('State the execution limits for Practicals 7–10 and a defensible journal.',4,
  '<p>Real TShark offline analysis of a synthetic file, owned TCP/TLS exchanges and file hashing are executed. VLAN/DMZ/rule/state/alert examples are declared Python logical models. Wireshark GUI/live capture and Packet Tracer VLAN/DMZ/firewall commands are guided only; no .pkt result, kernel policy, switch configuration, Snort/Suricata or NGFW deployment is claimed. Record actual commands, tool versions, observations, failures and limitations. Never fabricate output or weaken host protections to force a result.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('5. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}
CARDS=[
 ('Zone policy','Zone label != enforcement\nInternal/private address != trusted identity','Define services/directions, enforce, monitor and verify both positive and negative cases.'),
 ('DMZ model','Outside -> named DMZ web: allow\nOutside -> inside: deny\nApp -> exact approved DB: narrow exception','Logical model only, not a configured firewall or Packet Tracer result.'),
 ('VLANs','Access: assigned VLAN\nTrunk: selected VLANs\nRouting: controlled L3 path','802.1Q ordinary IDs1–4094. Tags do not encrypt or automatically prove switch isolation.'),
 ('Tunneling','Original data -> encapsulation\n-> tunnel endpoints -> decapsulation','Encapsulation alone is not confidentiality. The real demo is a local TLS byte relay, not an IP-level VPN.'),
 ('Packet-filter policy','Check relevant headers/direction\nFirst match in THIS model\nNo match -> deny','Other products may evaluate differently; source addresses alone are not authentication.'),
 ('Stateful model','SYN -> matching SYNACK -> ACK\n-> tracked data -> expiry','Tiny logical model; not sequence-validating TCP, NAT, fragments, a kernel firewall or a packet transmission.'),
 ('Application versus circuit','Application: supported protocol semantics\nCircuit: session establishment/relay','A permitted stream is not automatically safe/encrypted. The tiny local HTTP demo is not production WAF/SOCKS.'),
 ('NGFW','State/context + application awareness\n+ additional enabled capabilities','Vendor/configuration/licensing/visibility matter; no universal malware or encrypted-payload guarantee.'),
 ('IDS pipeline','Sensor/agent -> analysis -> alert/store\n-> management/investigation','Protect health, clocks, evidence and access. Detection is not automatic prevention.'),
 ('HIDS versus NIDS','Host: selected local logs/files/processes\nNetwork: observations on monitored path','Agents/host compromise versus placement/encryption/loss trade-offs; complementary evidence.'),
 ('Alert quality','Precision=TP/(TP+FP)\nRecall=TP/(TP+FN)\nFPR=FP/(FP+TN)','Six-case fixture only, not a production accuracy benchmark. Handle zero denominators appropriately in other datasets.'),
 ('Offline display filters','tshark -n -r synthetic.pcap -Y dns\ntshark -n -r synthetic.pcap -Y http\ntshark -n -r synthetic.pcap -Y "vlan.id == 10"','Actual file dissection. No interface capture; correct filter syntax depends on context.'),
 ('Capture versus display','Capture/BPF: tcp port 80\nDisplay: tcp.port == 80','BPF form was really rejected as a -Y display expression. No live capture is claimed.'),
 ('Evidence boundaries','Synthetic file != live capture\nPython model != switch/firewall deployment\nGuide != observed simulator result','Packet Tracer/Wireshark GUI/IDS appliances are not run. Check actual observations and disclose limitations.')]
SYNTAX=[{'title':tr('Network Security Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]
QA=[
 ('What is a security zone?','A grouping by intended role/security posture; its name alone does not enforce policy.'),
 ('Is an Intranet automatically safe?','No. Insider misuse, compromised endpoints and misconfiguration remain possible.'),
 ('What is the purpose of a DMZ?','Separately control exposed services and their paths to outside/internal assets.'),
 ('Can every DMZ host reach every internal host?','It should not gain blanket access; permit only justified controlled dependencies.'),
 ('What does a VLAN separate?','A logical Layer-2 broadcast domain.'),
 ('What does an access port typically carry?','Traffic for the endpoint’s assigned VLAN under the configured port behaviour.'),
 ('What does a trunk do?','Carries selected VLANs between devices; it does not itself route or encrypt them.'),
 ('What allows inter-VLAN communication?','An appropriate Layer-3 routing path with suitable security policy.'),
 ('What are the ordinary VLAN ID limits?','1–4094;0 is used for priority tagging and 4095 is reserved.'),
 ('Does a failed ping prove segmentation?','No. Addresses, masks, gateways, links or filtering can explain failure; verify the setup.'),
 ('What is tunneling?','Carrying one communication representation within another between entry/exit endpoints.'),
 ('Does encapsulation automatically encrypt?','No. Protection depends on the actual protocol/scheme and endpoint trust.'),
 ('What does the actual TLS example protect?','The owned client-to-relay TLS1.3 segment; the separate backend is owned plaintext loopback.'),
 ('What is packet filtering?','Traffic decision-making using relevant packet headers and rule policy.'),
 ('What is default deny?','Deny traffic unless an applicable rule/policy explicitly permits it.'),
 ('Does rule order always work the same across products?','No. This model is first-match; real evaluation semantics and direction must be checked.'),
 ('What does stateful inspection add?','Stored flow/session context and lifecycle handling for relevant traffic.'),
 ('Is a TCP ACK/RST flag alone genuine stored state?','No. An ACL established keyword may only test flags, not validate an approved connection.'),
 ('What can an application gateway examine?','Supported application/protocol operations, subject to parser, configuration and visibility limits.'),
 ('What is the local application example’s outcome?','GET /course receives 200; /admin receives 403 on owned loopback only.'),
 ('What does a circuit-level gateway control?','Session establishment/relay, not necessarily each application content item.'),
 ('Does SOCKS inherently provide an IP/ICMP gateway or encrypt traffic?','No. Its specific relay/authentication behaviour must not be confused with those properties.'),
 ('What distinguishes an NGFW conceptually?','Additional application/context/inspection or prevention capabilities combined with state-aware control, depending on the product/configuration.'),
 ('Does an IDS automatically block an intruder?','No. Detection/alerting is different from prevention/IPS action.'),
 ('Can an insider be an intruder?','Yes, when attempting/causing unauthorized policy violations or misusing authorized rights.'),
 ('Name typical IDS components.','Sensors/agents, analysis engine, rule/baseline configuration, protected event storage and management/response interface.'),
 ('What are signature/anomaly methods versus HIDS/NIDS?','Detection approach versus observation location; they are different classification axes.'),
 ('What is a HIDS advantage?','Relevant local host/file/process/log context when the deployed sensor has appropriate access.'),
 ('What is a HIDS limitation?','Deployment/resources/maintenance, baseline trust and possible tampering on a compromised host.'),
 ('What is a NIDS advantage?','Observing multiple flows/hosts on an appropriately monitored network path.'),
 ('What limits NIDS visibility?','Off-path/switched traffic, feed placement, encryption, packet loss and available analysis capacity.'),
 ('Is Wireshark automatically an IDS?','No. It is a packet analyzer; a rule/product/investigation system is a separate capability.'),
 ('What is a false positive versus false negative?','Benign activity flagged versus a relevant ground-truth event missed.'),
 ('Why does a good checksum not prove a trusted sender?','Checksums detect certain corruption, not cryptographic identity or authorization.'),
 ('What was actually analyzed in the PCAP?','16 constructed benign frames, not live capture; ARP/DNS/TCP/HTTP and two VLAN-tagged UDP frames.'),
 ('Which practical/tool claims remain guided only?','Wireshark GUI/live capture and Packet Tracer VLAN/DMZ/firewall; no Snort/Suricata, NGFW, host firewall or switch deployment is claimed.')]
VIVA=[{'title':tr('Unit 4 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
