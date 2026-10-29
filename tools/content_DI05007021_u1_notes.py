"""English-only Unit 1: syllabus topics, safe Practical 1 and answered practice."""
from subject_DI05007021 import tr

def ul(*items):return '<ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
def table(head,rows):
 return '<table><tr>'+''.join('<th>'+s+'</th>' for s in head)+'</tr>'+''.join('<tr>'+''.join('<td>'+s+'</td>' for s in r)+'</tr>' for r in rows)+'</table>'
def topic(title,body,diagram=None,programs=None):
 out={'h':tr(title),'body':tr(body)}
 if diagram:out['diagram']=diagram
 if programs:out['programs']=programs
 return out

SOURCES=[
 ('GTU DI05007021, Information Security, 2026–27 (uploaded syllabus)', 'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf'),
 ('NIST glossary: confidentiality','https://csrc.nist.gov/glossary/term/confidentiality'),
 ('NIST glossary: integrity','https://csrc.nist.gov/glossary/term/integrity'),
 ('NIST glossary: availability','https://csrc.nist.gov/glossary/term/availability'),
 ('NIST glossary: passive attack','https://csrc.nist.gov/glossary/term/passive_attack'),
 ('ITU-T X.800: security services and specific/pervasive mechanisms','https://www.itu.int/rec/T-REC-X.800-199103-I/en'),
 ('CISA: Understanding Denial-of-Service Attacks (archived educational article, 2021)','https://www.cisa.gov/news-events/news/understanding-denial-service-attacks'),
 ('Python: hashlib','https://docs.python.org/3/library/hashlib.html'),
 ('Python: hmac','https://docs.python.org/3/library/hmac.html')]

SPECIFIC=[
 ('Encipherment','Transforms data using a cryptographic scheme to help protect confidentiality. Key management matters; encryption alone does not guarantee integrity or availability.'),
 ('Digital signature','Creates a verifiable signature with a private signing key. Supports integrity, origin authentication and evidence for non-repudiation under suitable trust and key-control assumptions.'),
 ('Access control','Enforces which subjects may perform which operations on which resources; e.g. a reader cannot change a protected record.'),
 ('Data integrity','Detects unauthorized changes. Depending on scope, mechanisms may also check ordering, insertion, deletion or replay; a bare message digest alone does not provide all these properties.'),
 ('Authentication exchange','Uses an appropriate protocol to establish a claimed identity or origin, e.g. a protected challenge-response exchange. Freshness checks can resist replay.'),
 ('Traffic padding','Adds protected cover/padding traffic to reduce what an observer can infer from traffic patterns. It does not mean renaming or merely compressing a file.'),
 ('Routing control','Selects or constrains communication paths according to security policy; not a claim that any alternative route is automatically secure.'),
 ('Notarization','Uses a trusted third party to provide evidence about properties of a communication, such as origin or time, under an agreed procedure.')]
PERVASIVE=[
 ('Trusted functionality','Security-critical functions must behave as intended; e.g. a trustworthy reference monitor. Trusted is an assumption requiring assurance, not a claim of infallibility.'),
 ('Security labels','Associate resources with security attributes such as Public or Restricted so policy can interpret them. Labels alone do not enforce permissions.'),
 ('Event detection','Recognizes selected security-relevant events, such as repeated failed access attempts, and may trigger an alert or response. A detected event is not automatically a confirmed attack.'),
 ('Security audit trail','Records relevant events for examination and accountability. Logs need access protection and integrity controls; plain editable logs are not conclusive proof.'),
 ('Security recovery','Restores an acceptable secure state after a failure or incident, e.g. verified restoration and credential replacement when appropriate. A backup is useful only if recovery works.')]

NOTES=[
 {'title':tr('1. Foundations and Security Goals'),'items':[
  topic('1.1 Information security and the need for protection',
   '<p><b>Information security</b> protects information and the systems that handle it against unauthorized disclosure, improper change or destruction, and loss of useful access. It applies to digital records, paper, devices, people and procedures—not only antivirus software.</p>'+ul(
    '<b>Assets:</b> student records, credentials, business documents, services and reputation.',
    '<b>Threat:</b> a potential cause of harm; <b>vulnerability:</b> a weakness that may be exploited; <b>attack:</b> an attempt to violate security. An accidental fault can also harm an asset without being an attack.',
    '<b>Why security is needed:</b> protect privacy and valuable work, maintain trustworthy records, keep services usable, and reduce operational and financial harm.',
    '<b>Controls:</b> combine technical measures with physical protection and administrative procedures. Choose controls for the asset, threat and consequence; no single product removes all risk.')),
  topic('1.2 The CIA triad',
   '<p>The three core goals are <b>confidentiality, integrity and availability</b>. Consider a college result portal:</p>'+table(
    ['Goal','Meaning','Failure and useful controls'],[
    ('Confidentiality','Only authorized parties can access or receive protected information.','A result file is disclosed to an outsider. Use access restrictions and suitable encryption.'),
    ('Integrity','Information is not improperly modified or destroyed.','A mark is changed without permission. Use authorization, protected integrity checks and audit records.'),
    ('Availability','Authorized users have timely, reliable access to information and services.','Students cannot obtain results when needed. Use capacity planning, recovery procedures and suitable redundancy.')])+
   '<p>One incident can affect several goals. Encryption does not keep a failed server online; a backup does not by itself stop disclosure; a publicly stored hash does not authenticate a sender.</p>','sec1_cia')]},
 {'title':tr('2. Security Attacks'),'items':[
  topic('2.1 Passive attacks: observation without alteration',
   '<p>A <b>passive attack</b> observes information or communication without altering the system or data.</p>'+ul(
    '<b>Release of message contents:</b> unauthorized reading of an unprotected message.',
    '<b>Traffic analysis:</b> learning from endpoints, timing, frequency or volume, even when message contents are encrypted.',
    '<b>Main concern:</b> confidentiality. Observation can leave little visible evidence, so prevention is important. Encryption protects content; it does not automatically hide all metadata.')+
   '<p>Passive does not mean harmless or authorized. Reading someone else’s traffic without permission is not part of this lab.</p>','sec1_attacks'),
  topic('2.2 Active attacks: alteration, impersonation or disruption',
   '<p>An <b>active attack</b> deliberately changes system state, introduces false information, impersonates an entity or disrupts service.</p>'+table(
    ['Type','Classroom example','Relevant protection'],[
    ('Masquerade','An outsider acts as an authorized staff member.','Strong authentication and appropriate access control.'),
    ('Replay','A previously valid message is submitted again without permission.','Authenticated freshness, such as correctly checked nonces or sequence numbers.'),
    ('Modification','An attendance value is changed in transit.','Authenticated integrity plus authorization at the endpoint.'),
    ('Denial of service','A malicious action prevents legitimate service use.','Layered prevention, detection, response and recovery.')])+
   '<p><b>Compare:</b> passive observation mainly seeks information; active attacks alter behaviour, information or access. Detection and recovery are especially important for active attacks. Neither class is always completely preventable.</p>'),
  topic('2.3 Denial of service, distributed DoS and ordinary faults',
   '<p><b>DoS</b> aims to deny legitimate use of a resource. <b>DDoS</b> is a distributed form in which multiple systems participate. The main CIA goal affected is availability, although an incident may cause other harm too.</p>'+ul(
    '<b>Recognize:</b> failed service requests, unusual resource consumption or abnormal traffic can justify investigation. They do not alone prove a malicious attack.',
    '<b>Respond defensively:</b> follow the incident procedure, preserve relevant evidence, involve the administrator/provider, apply appropriate traffic controls and recover the service. Avoid blocking legitimate users unnecessarily.',
    '<b>Important distinction:</b> a broken cable, maintenance, permissions or a configuration error can also cause an outage.',
    '<b>Lab boundary:</b> do not generate floods, exhaust resources or test other people’s hosts. This unit makes no DoS experiment or mitigation-performance claim.')+
   '<p>The cited CISA article is an archived explanation of the concept, not a current policy or a prescribed implementation guide.</p>','sec1_dos')]},
 {'title':tr('3. Security Services'),'items':[
  topic('3.1 What a security service provides',
   '<p>A <b>security service</b> is a protection supplied to users, data or a communicating system. A <b>mechanism</b> is a means used to supply that protection.</p>'+table(
    ['Syllabus service','Protection sought','Example'],[
    ('Confidentiality','Prevent unauthorized disclosure.','Restrict who can read a result file.'),
    ('Integrity','Protect against improper changes or destruction.','Detect an altered attendance message using a trusted integrity mechanism.'),
    ('Authentication','Establish a claimed identity or data origin.','Verify an account holder or the origin of a protected message.'),
    ('Non-repudiation','Provide evidence against false denial of a relevant action.','Evidence of message origin or receipt under an agreed process.'),
    ('Access control','Prevent unauthorized use of a resource or operation.','A student can view their result but cannot edit marks.')])+
   '<p>Availability remains an essential security <b>goal</b>. This syllabus’s service list and the core X.800 categories above should not be confused with a guarantee that a cryptographic mechanism supplies availability.</p>','sec1_services'),
  topic('3.2 Authentication versus authorization and access control',
   '<p><b>Authentication:</b> “Who or what is this?” <b>Authorization:</b> “What is this subject allowed to do?” <b>Access control:</b> enforcement of those permissions.</p>'+ul(
    'A valid student login must not gain the teacher’s permission to change marks. Successful authentication does not authorize every operation.',
    'Apply least privilege: grant only the access needed for the task, then enforce the policy for each protected operation.',
    'Authentication may concern a peer/entity or a message’s origin. Integrity and freshness checks are separate requirements; replaying a valid old message can still be harmful.',
    'Access control helps protect confidentiality and integrity, but a configuration mistake or untrusted enforcement component can defeat it.')+'<p>The diagram is a conceptual decision flow, not a deployed authentication server.</p>','sec1_authz'),
  topic('3.3 Non-repudiation: evidence, not an absolute promise',
   '<p><b>Non-repudiation of origin</b> addresses a sender falsely denying a message. <b>Non-repudiation of delivery/receipt</b> addresses a recipient falsely denying the relevant delivery or receipt.</p>'+ul(
    'Digital signatures and trusted evidence-handling processes can support non-repudiation. Identity binding, private-key control, timestamps and the applicable procedure matter.',
    'A signature verifies a cryptographic relationship under its assumptions; it does not automatically prove which human operated a device, that the signed statement is true, or a particular legal result.',
    '<b>HMAC is not a digital signature:</b> both parties sharing the secret can create valid tags, so it does not supply publicly verifiable proof against the other key holder.',
    'A plain hash is not sender authentication. Encryption alone is not proof of authorship or receipt. Unit 3 covers public keys and certificates in more detail.'))]},
 {'title':tr('4. Security Mechanisms'),'items':[
  topic('4.1 Eight specific mechanisms in X.800',
   '<p><b>Specific mechanisms</b> directly support one or more particular security services. Learn each name with one purpose and example; they are not eight interchangeable security products.</p>'+table(['Specific mechanism','Purpose and limitation'],SPECIFIC)+
   '<p>This is the X.800 classification. It is not a recommendation to deploy old algorithms from the standard. Detailed cipher algorithms belong to later units.</p>','sec1_specific'),
  topic('4.2 Five pervasive mechanisms in X.800',
   '<p><b>Pervasive mechanisms</b> provide supporting security functions that are not confined to a single particular service. They can support several protections across a system.</p>'+table(['Pervasive mechanism','Meaning and classroom example'],PERVASIVE)+
   '<p><b>Contrast:</b> encipherment is a specific protection mechanism; a security audit trail is pervasive support. Both are needed in an appropriate design—pervasive does not mean optional or automatically stronger.</p>','sec1_pervasive'),
  topic('4.3 Relating goals, services, mechanisms and attacks',
   '<p>Use this order in a worked answer: <b>asset → threatened goal → required service → suitable mechanism → remaining limitation</b>.</p>'+table(
    ['Situation','Service / mechanism','Limitation'],[
    ('An outsider reads a private file.','Confidentiality / access control and appropriate encryption.','An authorized recipient may still disclose what they read.'),
    ('A protected message is changed.','Integrity and origin authentication / suitable authenticated integrity checking.','A bare digest is useful only with a trusted reference; a valid tag alone does not prove freshness.'),
    ('A user denies sending an instruction.','Non-repudiation / signature and trusted evidence process.','Key compromise and identity/evidence assumptions must be considered.'),
    ('A server is unavailable.','Availability goal / appropriate capacity, monitoring and recovery controls.','First distinguish attacks from ordinary faults; encryption alone does not repair availability.')])+
   '<p>Relationships are <b>many-to-many</b>: one mechanism can support several services and a service may require several mechanisms. Avoid “one goal, one magic tool” answers.</p>')]},
 {'title':tr('5. Safe Practical 1 and Revision'),'items':[
  topic('5.1 TCP/IP utilities: commands and honest execution labels',
   '<p><b>Practical 1:</b> execute basic TCP/IP utilities. Use only your own computer or an instructor-authorized lab. Start with read-only observations, record the command, result, interpretation and limitation, and omit private addresses or credentials from shared reports.</p>'+table(
    ['Purpose / utility','Bounded example','Status in this reference'],[
    ('Address configuration: ipconfig / ip','Windows: <code>ipconfig /all</code><br>Linux: <code>ip -j address show dev lo</code>','Linux loopback query actually executed; Windows guided only.'),
    ('Reachability: ping','Linux: <code>ping -n -c 1 -W 2 127.0.0.1</code><br>Windows: <code>ping -n 1 127.0.0.1</code>','Linux attempted; sandbox denied socket permission. No ICMP success claimed.'),
    ('Route: tracert / traceroute','Windows: <code>tracert -d 127.0.0.1</code><br>Linux: <code>traceroute -n 127.0.0.1</code>','Guided only. The executed <code>ip route get</code> is a local route decision, not a hop trace.'),
    ('Neighbours: arp / ip neigh','Windows: <code>arp -a</code><br>Linux: <code>ip -j neigh show dev lo</code>','Linux loopback query executed; an empty neighbour table is normal here.'),
    ('Sockets: netstat / ss','Windows: <code>netstat -an</code><br>Linux: <code>ss -ltnH</code> with a lab-owned port filter','Filtered ss actually inspected only the example’s own listening socket.'),
    ('DNS: nslookup / host','<code>nslookup example.org</code><br><code>host example.org</code>','Guided only. Actual <code>getent ahostsv4 localhost</code> is system name resolution, not proof of a DNS query.'),
    ('Registration: whois','<code>whois example.org</code>','Guided public example; not executed. WHOIS is not a host-reachability or ownership-authentication test.'),
    ('Capture: tcpdump','<code>tcpdump -i lo -nn -c 1</code>','Guided only; requires suitable permission and an authorized packet source. No captured traffic is claimed.'),
    ('Legacy clients: ftp / telnet','<code>ftp &lt;lab-host&gt;</code><br><code>telnet &lt;lab-host&gt; &lt;port&gt;</code>','Guided only, using a disposable instructor-provided service. Legacy plaintext FTP/Telnet are unsuitable for real passwords.')])+
   '<p>Utilities and permissions differ by OS. Do not change host security settings merely to force a lab result. A denied or unavailable command should be reported honestly and checked with the instructor.</p>'),
  topic('5.2 Six executed supporting examples and their limits',
   '<p>The downloadable kit contains six small, actually executed Python examples. Python’s standard library handles hashing/HMAC and the private TCP example; the Linux utility examples require existing <code>ip</code>, <code>ss</code>, <code>getent</code> and <code>ping</code>.</p>'+ul(
    '<b>01:</b> compare a SHA-256 digest with a trusted reference. This is change detection, not encryption or identity proof.',
    '<b>02:</b> verify a real HMAC tag with an ephemeral key. This is not a public signature or a replay-prevention protocol.',
    '<b>03:</b> exchange exactly one teaching message over private loopback TCP; all sockets and the worker close.',
    '<b>04:</b> read actual loopback address, route and neighbour information.',
    '<b>05:</b> attempt one local ping and record the actual permission denial in this sandbox.',
    '<b>06:</b> resolve localhost through the OS and inspect an owned listening socket, then close it.')+
   '<p>These illustrations do not implement an enterprise security system. They are not substitutes for the later official cipher, simulator, Wireshark or Kali Linux practicals. Windows GUI/commands and those later tools are not claimed as executed.</p>',programs=[f'sec1p{i:02d}' for i in range(1,7)]),
  topic('5.3 Diagnose carefully and prepare a defensible answer',
   '<p>For a failed connection, inspect <b>local configuration → name resolution → route/reachability → service listening and policy</b>. Interpret each result within its layer; successful ping is neither a secure-login test nor proof that a web application works.</p>'+ul(
    'A loopback connection tests this computer’s local stack/service, not the Internet connection.',
    'A permission-denied ping and a working TCP exchange can occur together. Do not label that observation a DoS attack.',
    'For a theory answer, give a definition, distinguish nearby terms, draw a labelled diagram where useful, and apply one concrete example.',
    '<b>Assessment:</b> theory ESE 70 + PA 30, practical PA 20 + ESE 30 = 150. Unit 1 is 6 hours / 15% syllabus weight; that is not a guaranteed number of questions or marks in a paper.',
    '<b>Practice pool:</b> the following twelve answered questions have suggested 3/4/7-mark practice sizes only. They are original revision questions, not official GTU past-paper questions or a promised paper pattern.')+
   '<p><b>Primary references:</b> '+', '.join('<a href="'+url+'">'+name+'</a>' for name,url in SOURCES)+'. Definitions are paraphrased and examples are fictional.</p>','sec1_diagnose')]}]

PRACTICE=[
 ('Define information security and explain why a college needs it.',3,
  '<p>Information security protects information and supporting systems against unauthorized disclosure, improper change/destruction and loss of useful access. A college needs it to protect private student records, keep marks accurate and make essential services available. Technical controls, physical protection and procedures work together; antivirus alone is insufficient.</p>'),
 ('Explain the CIA triad using a result-portal example.',7,
  '<p><b>Confidentiality:</b> only authorized users can see protected results; use access restrictions and appropriate encryption. <b>Integrity:</b> marks cannot be improperly changed or destroyed; use authorization, protected integrity checks and audit records. <b>Availability:</b> authorized users can obtain results when needed; use suitable capacity and tested recovery. Draw the three labelled goals and give one failure for each. One event may harm multiple goals; no single control guarantees all three.</p>'),
 ('Differentiate passive and active attacks with examples.',4,
  '<p>A passive attack observes without altering the system or data: unauthorized message reading and traffic analysis are examples. An active attack changes state, inserts/replays information, impersonates a user or disrupts service: modification, masquerade, replay and DoS are examples. Passive attacks mainly threaten confidentiality and may be hard to notice; active attacks make integrity, authentication, availability, detection and recovery particularly important. Passive does not mean harmless.</p>'),
 ('Explain DoS and DDoS and distinguish them from an ordinary outage.',4,
  '<p>DoS is a malicious attempt to prevent legitimate use of a resource. DDoS distributes participation across multiple systems. Both primarily threaten availability. A broken link, planned maintenance or a permission error can also stop access, so an outage alone is not evidence of attack. Investigate, preserve evidence and follow authorized incident-response and recovery procedures. No attack traffic needs to be generated to explain the concept.</p>'),
 ('Explain the five security services listed in this unit.',7,
  '<p><b>Confidentiality</b> protects against unauthorized disclosure; <b>integrity</b> protects against improper change/destruction; <b>authentication</b> establishes a claimed identity or data origin; <b>access control</b> prevents unauthorized operations; <b>non-repudiation</b> supplies evidence against false denial of a relevant action. Use a result system to illustrate restricted reading, protected marks, identity checking, permission enforcement and an appropriately signed/evidenced instruction. A service states the protection; mechanisms implement it.</p>'),
 ('Differentiate authentication, authorization and access control.',3,
  '<p>Authentication establishes who or what is making a claim. Authorization decides the permitted operations on resources. Access control enforces those decisions. A student may authenticate successfully and be authorized to view their own result, but must still be denied permission to edit a teacher’s mark sheet. Apply least privilege rather than treating login as unrestricted access.</p>'),
 ('Explain non-repudiation and why HMAC is not a digital signature.',4,
  '<p>Non-repudiation supplies evidence concerning origin or receipt so a relevant party cannot easily deny the action falsely. A digital signature can support this under identity, key-control and evidence-handling assumptions; it is not an automatic legal or human-identity guarantee. HMAC uses a shared secret, so either holder can generate a valid tag. It therefore does not supply public proof against the other holder. Encryption and a bare hash alone do not provide non-repudiation.</p>'),
 ('List and explain the eight specific security mechanisms.',7,
  '<p><b>Encipherment:</b> cryptographic transformation; <b>digital signature:</b> verifiable signing; <b>access control:</b> enforcement of permitted use; <b>data integrity:</b> protected change detection and, where designed, sequence checks; <b>authentication exchange:</b> establish a claimed identity/origin; <b>traffic padding:</b> reduce inference from traffic patterns; <b>routing control:</b> constrain paths by security policy; <b>notarization:</b> trusted third-party evidence. Explain a purpose, not just an acronym. The mechanisms may support overlapping services.</p>'),
 ('Explain five pervasive security mechanisms with examples.',7,
  '<p><b>Trusted functionality:</b> dependable security-critical enforcement; <b>security labels:</b> security attributes interpreted by policy; <b>event detection:</b> recognize selected security-relevant events; <b>security audit trail:</b> protected records for examination/accountability; <b>security recovery:</b> restore an acceptable secure state. For a result system, use a trustworthy permission check, a Restricted label, a failed-access alert, protected logs and verified restoration. Labels and editable logs alone do not enforce security or conclusively prove an event.</p>'),
 ('Differentiate a security service and a mechanism with two mappings.',4,
  '<p>A service states what protection is supplied; a mechanism describes a means of supplying it. Confidentiality may use suitable encryption together with access restrictions. Integrity and origin authentication may use a suitable authenticated integrity mechanism. A service can need several mechanisms, and one mechanism can support several services. Do not claim that encryption alone guarantees integrity, identity and availability.</p>'),
 ('A message and its plain hash both match after replacement. Is the sender authenticated?',3,
  '<p>No. An attacker who can replace both data and the digest can make a matching pair. A hash comparison is useful only when its reference is trustworthy and does not itself identify a sender. A properly keyed MAC can support authentication among secret holders; public signatures require their own trust assumptions. Neither a matching hash nor a MAC by itself proves freshness or human identity.</p>'),
 ('Ping is denied, but a private TCP exchange succeeds. Interpret the observation.',4,
  '<p>The recorded ping result is a local socket-permission denial, not evidence of an ICMP response and not proof of a network attack. A successful one-message loopback TCP exchange demonstrates that particular local TCP service at that moment. It does not prove Internet access, confidentiality, authenticated login or future availability. Record the command and limitation, and use an authorized alternative rather than disabling security settings.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('6. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}

CARDS=[
 ('CIA','C = confidentiality\nI = integrity\nA = availability','Goals may overlap; a single mechanism does not guarantee all three.'),
 ('Attack classes','Passive: observe\nActive: alter, impersonate, replay or disrupt','Classify by what the action does, not whether it looks harmless.'),
 ('Authentication and access','Authenticate the subject\nAuthorize the operation\nEnforce the policy','A successful login is not permission to do everything.'),
 ('Service versus mechanism','Service: what protection?\nMechanism: how is it supplied?','For example: confidentiality service; appropriate encryption plus access restrictions.'),
 ('Specific mechanisms, part 1','Encipherment; digital signature\nAccess control; data integrity','Four of the eight X.800 specific mechanisms.'),
 ('Specific mechanisms, part 2','Authentication exchange; traffic padding\nRouting control; notarization','The remaining four X.800 specific mechanisms.'),
 ('Pervasive mechanisms','Trusted functionality; security labels\nEvent detection; security audit trail\nSecurity recovery','Supporting mechanisms not confined to a single particular security service.'),
 ('Hash, MAC and signature','Hash + trusted reference: change check\nMAC: shared-secret integrity/authentication\nSignature: public verification under trust','Neither a bare hash nor HMAC supplies public non-repudiation; encryption is a different service.'),
 ('Linux loopback observations','ip -j address show dev lo\nip -j route get 127.0.0.1\nip -j neigh show dev lo','Actually executed read-only queries. Route lookup is not traceroute; loopback usually needs no ARP neighbour.'),
 ('Bounded ping','ping -n -c 1 -W 2 127.0.0.1','Actually attempted, but this reference sandbox denied socket permission. Windows uses different count flags.'),
 ('Local resolver and socket table','getent ahostsv4 localhost\nss -ltnH "sport = :<owned-port>"','Actual examples use only localhost and an OS-assigned owned listener. getent is not necessarily DNS.'),
 ('Practical journal','Command -> observation -> interpretation\n-> limitation -> safe next step','Separate actual results from guided commands; never invent outputs or publish credentials.')]
SYNTAX=[{'title':tr('Security and Utility Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]

QA=[
 ('What is information security?','Protection of information and supporting systems against unauthorized disclosure, improper change/destruction and loss of useful access.'),
 ('Why is security not just antivirus?','It also requires suitable permissions, trustworthy processes, physical protection, recovery and other controls.'),
 ('What does CIA stand for?','Confidentiality, integrity and availability.'),
 ('Does confidentiality mean no one may read the data?','No. It means access and disclosure are restricted to authorized parties.'),
 ('What is integrity?','Protection against improper modification or destruction; a suitable integrity check needs trustworthy assumptions.'),
 ('What is availability?','Timely, reliable access to and use of information and services by authorized users.'),
 ('Can one event violate several CIA goals?','Yes. For example, a destructive data theft incident can involve disclosure, alteration and loss of access.'),
 ('What is a passive attack?','Unauthorized observation without altering the system or data, such as eavesdropping or traffic analysis.'),
 ('Can encrypted communication reveal traffic patterns?','Yes. Content encryption does not automatically hide endpoints, timing or volume.'),
 ('Name four active attack types.','Masquerade, replay, message modification and denial of service.'),
 ('Why can replay be active even if old message bytes are unchanged?','Unauthorized reintroduction changes the communication or system behaviour; integrity alone may not establish freshness.'),
 ('What is DoS?','A malicious attempt to prevent legitimate access to or use of a resource.'),
 ('What makes DDoS distributed?','Multiple participating systems act against the target; a single failure is not automatically DDoS.'),
 ('Does a failed ping prove DoS?','No. Permissions, filtering, a fault or configuration may explain it; investigate within authorized scope.'),
 ('What is a security service?','A protection provided to a user, data or communication; it states the required security property.'),
 ('Name the five listed security services.','Confidentiality, integrity, authentication, non-repudiation and access control.'),
 ('How do authentication and authorization differ?','Authentication checks a claimed identity/origin; authorization determines permitted operations.'),
 ('What is least privilege?','Grant only the access needed for a task and enforce the applicable policy.'),
 ('What is non-repudiation of origin?','Evidence supporting the origin of data against a sender’s false denial, under the relevant trust and evidence assumptions.'),
 ('Does a digital signature prove a statement is true?','No. It verifies a cryptographic relationship under assumptions, not truth or automatic human/legal attribution.'),
 ('Why is HMAC not public non-repudiation?','Each shared-secret holder can create a valid tag, so it cannot provide public proof against the other holder.'),
 ('What is a specific mechanism?','A mechanism that directly supports one or more particular services, such as encipherment or an authentication exchange.'),
 ('What is traffic padding intended to reduce?','Inference from traffic patterns; it requires appropriate protection and is not merely file compression.'),
 ('What is notarization?','Use of a trusted third party to provide evidence about properties of a communication under an agreed process.'),
 ('Name the five pervasive mechanisms.','Trusted functionality, security labels, event detection, security audit trail and security recovery.'),
 ('Does a security label enforce access by itself?','No. A trustworthy policy-enforcement mechanism must interpret and enforce it.'),
 ('Why protect audit logs?','An editable or untrusted record may be changed or misattributed and is not conclusive evidence on its own.'),
 ('What is the limitation of the practical reference?','It runs small standard-library and Linux-loopback examples, records a real denied ping, and does not claim Windows, simulator, packet-capture or DoS execution.')]
VIVA=[{'title':tr('Unit 1 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
