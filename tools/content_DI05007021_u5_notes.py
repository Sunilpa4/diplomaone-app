"""English-only introductory cyber security: all named threats/crimes, safe study."""
from subject_DI05007021 import tr
from content_DI05007021_u1_notes import ul,table,topic
SOURCES=[
 ('GTU DI05007021 syllabus, 2026–27','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf'),
 ('NIST glossary: threat','https://csrc.nist.gov/glossary/term/threat'),
 ('NIST glossary: vulnerability','https://csrc.nist.gov/glossary/term/vulnerability'),
 ('NIST SP800-83r1: malware prevention/handling (2013 fundamentals)','https://csrc.nist.gov/pubs/sp/800/83/r1/final'),
 ('CISA phishing awareness (archived educational page)','https://www.cisa.gov/secure-our-world/recognize-and-report-phishing'),
 ('CISA DoS/DDoS explanation (archived 2021 article)','https://www.cisa.gov/news-events/news/understanding-denial-service-attacks'),
 ('OWASP: SQL Injection Prevention Cheat Sheet','https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html'),
 ('Python sqlite3 parameter/authorizer documentation','https://docs.python.org/3/library/sqlite3.html'),
 ('Kali official role and suitability','https://www.kali.org/docs/introduction/should-i-use-kali-linux/'),
 ('Kali official image/signature verification guidance','https://www.kali.org/docs/introduction/download-official-kali-linux-images/'),
 ('Kali official download page','https://www.kali.org/get-kali/'),
 ('Kali 2026.3 versioned signed-manifest source','https://cdimage.kali.org/kali-2026.3/SHA256SUMS'),
 ('CERT-In official advisories/contact information','https://www.cert-in.org.in/')]
NOTES=[
 {'title':tr('1. Cyber Security Foundations'),'items':[
  topic('1.1 Cyber security, cyberspace and what is being protected',
   '<p><b>Cyber security</b> protects digital systems, communications, services and information from relevant threats and attacks. <b>Cyberspace</b> is the interconnected digital environment in which systems, services, data and online activities interact; harm can affect real people and organizations.</p>'+ul(
    'Confidentiality concerns unauthorized disclosure; integrity concerns improper change/destruction; availability concerns useful, timely access.',
    'Assets include accounts, devices, documents, services, money/reputation and personal privacy/safety. Controls must fit the asset and consequences.',
    'Cyber security is not just installing a tool. People, procedures, configuration, access control, updates, monitoring and recovery all matter.',
    'Every exercise in this unit uses fictional/public or owned fixtures. No malware, phishing delivery, botnet, flood, spoofed network path or attack against an external system is performed.') ),
  topic('1.2 Threat, vulnerability, attack, intruder and hacker',
   table(['Term','Meaning','Example / distinction'],[
    ('Threat','A circumstance/event/source with potential for harm.','Possible credential theft or malicious disruption; not necessarily a successful event.'),
    ('Vulnerability','An exploitable/triggerable weakness in a system, implementation, procedure or control.','An unpatched flaw or improperly restricted access; a weakness is not itself proof of compromise.'),
    ('Cyber-attack','An attempted/actual malicious or unauthorized action against a security objective.','A harmful access/disclosure/modification/disruption attempt.'),
    ('Intruder','An actor attempting or causing unauthorized policy violations.','May be an outsider or an insider misusing rights.'),
    ('Hacker','A broad contextual term, not automatically a criminal label.','Authorized security research/testing differs from unauthorized access or harm.')])+
   '<p>Assess likely harm and exposure, but do not label an outage, alert or person an attacker from one ambiguous symptom. Permission must cover the target, method and scope; having Kali or another tool is not authorization.</p>','sec5_risk')]},
 {'title':tr('2. Malware and Related Capabilities'),'items':[
  topic('2.1 Viruses, worms and Trojans',
   table(['Type','Defining idea','Defensive focus'],[
    ('Virus','Malicious code associated with a host file/program; spread involves infection/execution mechanisms.','Trusted software, controlled execution, appropriate detection and update/recovery procedures.'),
    ('Worm','Self-propagating malware that can spread between systems without depending on the same host-file model.','Reduce exposed weaknesses, patch, restrict unnecessary paths and respond across affected systems.'),
    ('Trojan','Malicious functionality presented as something legitimate/useful.','Verify sources, avoid untrusted installers/attachments and apply least privilege.')])+
   '<p>These are conceptual distinctions, not exclusive boxes: a Trojan may install a backdoor, spyware or bot component. No real sample is needed for this introduction. The file example handles only harmless text as data and compares hashes; it is not an antivirus or a malware-family classifier.</p>','sec5_malware',programs=['sec5p07']),
  topic('2.2 Adware and spyware',
   '<p><b>Adware</b> involves advertising-related behaviour and may be unwanted, intrusive or bundled deceptively; advertising software is not automatically criminal in every context. <b>Spyware</b> covertly collects/monitors information contrary to the user’s awareness or authorization.</p>'+ul(
    'Potential effects include privacy loss, unwanted changes and resource use. Symptoms such as pop-ups or slow performance are not conclusive attribution.',
    'Use trusted installation sources, deliberate permission/consent choices, updates and appropriate endpoint controls. Avoid installing unverified “cleanup” tools from alarming pop-ups.',
    'Authorized, transparent monitoring under appropriate policy is not the same factual situation as covert abusive surveillance. Definitions, intent and legal context matter.') ),
  topic('2.3 Botnets and backdoors',
   '<p>A <b>botnet</b> is a collection of compromised/controlled devices that can be coordinated for harmful activity such as abuse or disruption. The compromised device owner may also be a victim. A <b>backdoor</b> is a concealed or unauthorized access mechanism that bypasses intended access controls; such access can enable persistence or later misuse.</p>'+ul(
    'The concepts describe control/access capability, not one specific propagation method. A Trojan or other compromise can help establish it.',
    'Restrict exposure/privileges, patch, use appropriate monitoring and investigate suspicious access. Respond using trusted procedures rather than trying to operate a suspected bot/backdoor yourself.',
    'No remote-control service, command-and-control channel, persistence, backdoor or malware distribution is created in this course material.') )]},
 {'title':tr('3. Cyber Threats and Attacks'),'items':[
  topic('3.1 DoS and DDoS: availability and mitigation limits',
   '<p><b>Denial of service (DoS)</b> is malicious denial/disruption of legitimate resource use. <b>Distributed DoS (DDoS)</b> uses multiple participating systems. Availability is the main goal affected, but ordinary faults, maintenance or permissions can also cause access failures.</p>'+ul(
    'Defensive measures may include appropriate service design, resource limits, monitoring, recovery and coordinated upstream/provider response. One local setting is not a universal solution.',
    'Our token-bucket code performs six synthetic-clock admission decisions: four allowed and two limited. It sends <b>no requests or flood traffic</b>.',
    'This model is not deployed mitigation, a stress test or a bandwidth/resilience benchmark. A local limiter cannot by itself save an already saturated upstream link.',
    'Investigate evidence and follow authorized response procedures; do not attack a service to demonstrate the definition.') ,'sec5_attacks',programs=['sec5p05']),
  topic('3.2 Man-in-the-middle / on-path interference',
   '<p>A <b>man-in-the-middle (MITM)</b> or on-path attacker interposes in a communication path, potentially relaying, reading or altering exchanges. Merely forwarding traffic as an authorized service is not automatically malicious.</p>'+ul(
    'Use appropriate authenticated encryption/protocols, authentic key/certificate trust and correct identity validation. Do not ignore failed certificate checks.',
    'The actual private TLS example succeeds for its owned server name and rejects a wrong hostname. It is a control demonstration, not a real MITM attack or a detector for all on-path threats.',
    'A correctly validated certificate for an attacker’s own lookalike site does not make that site honest. TLS does not cure compromised endpoints, wrongly trusted roots or all application flaws.',
    'Only owned loopback endpoints and fresh temporary keys are used; no foreign network, capture or public target is involved.') ,programs=['sec5p08']),
  topic('3.3 IP spoofing and ARP spoofing are different claims',
   table(['Concept','What is misrepresented?','Limits and suitable defence'],[
    ('IP spoofing','Source IP information in packets.','An address alone is not identity; appropriate ingress/egress validation and authenticated protocols help, but routing/transport context still matters.'),
    ('ARP spoofing','An IPv4-address-to-link-address mapping on a relevant local network.','Consider suitable switch/host safeguards and trusted monitoring; a mapping change can also be legitimate replacement/failover.')])+
   '<p>The example compares only two <b>fictional dictionaries</b>. It flags a changed gateway mapping but does not confirm an attack, read/change an ARP cache or transmit forged IP/ARP packets. No poisoning, impersonation path or network reconfiguration is performed.</p>',programs=['sec5p04']),
  topic('3.4 SQL injection: separate query structure from data',
   '<p><b>SQL injection</b> occurs when untrusted input becomes part of query syntax rather than remaining data. The defensive example uses a real <b>in-memory SQLite</b> database with two fictional course records and a fixed parameterized query.</p>'+ul(
    'Define the query structure in application code and bind values through the database API. The fixed SQL-like input is treated as one literal value and returns no match; no vulnerable concatenated query is executed.',
    'Parameter placeholders normally represent data values, not table names, column names or SQL keywords. Keep structure fixed or choose it from a small application-owned allow-list.',
    'Validation is useful but does not make concatenation safe. Stored procedures/ORMs are not automatically immune when they construct dynamic SQL unsafely.',
    'Use suitable least privilege and application authorization too. The second actual SQLite example allows reads and denies a DELETE on its own connection; it is not a complete database-role or row-authorization design.',
    'No real account, deployed database, external target or credential-bypass experiment is used.') ,'sec5_sqli',programs=['sec5p01','sec5p02']),
  topic('3.5 Phishing: recognizable hints versus proof',
   '<p><b>Phishing</b> uses deceptive messages/sites or other communication to trick a person into harmful disclosure or action. It may appear through email, messages, social platforms or calls. Urgency, an unexpected request, a mismatched address or an unfamiliar link can be warning signs—not an infallible classifier.</p>'+ul(
    'Pause and verify through an independently known trusted route. Do not use the suspicious message’s link/number to verify itself, send passwords/passcodes or open unexpected attachments.',
    'Display names and From-header parsing are not sender authentication; headers may be forged. Correct grammar or HTTPS alone is not proof of legitimacy.',
    'The URL exercise parses reserved .test strings offline: a familiar prefix or userinfo before @ is not the hostname. It never opens a link or supplies a safe-site verdict.',
    'The email exercise parses neutral training headers only; no message, lure, credential form, attachment or campaign is sent. SPF/DKIM/DMARC validation is not performed.',
    '<b>Terminology:</b> a login OTP means a one-time passcode, not the one-time-pad cipher from Unit 2. Do not disclose authentication codes in response to unexpected requests.') ,'sec5_phishing',programs=['sec5p03','sec5p06'])]},
 {'title':tr('4. Cybercrime, Privacy and Personal Safety'),'items':[
  topic('4.1 Cybercrime, identity theft, information theft and hacking',
   '<p><b>Cybercrime</b> concerns criminal conduct involving digital systems/data or cyberspace, subject to applicable facts/law. An educational category or suspicious observation is not itself a legal finding.</p>'+table(['Category','Core distinction','Defensive response'],[
    ('Identity theft','Misuse of identifying/account information to impersonate or abuse another identity.','Protect accounts/identity data, use appropriate authentication, review/report unauthorized activity through trusted channels.'),
    ('Information theft','Unauthorized acquisition/disclosure of protected data.','Least privilege, appropriate encryption/access controls, monitoring and careful evidence/incident handling.'),
    ('Hacking in the crime context','Unauthorized access/exploitation or harmful misuse, not every authorized security activity.','Obtain explicit scope/permission for testing and follow responsible institutional procedures.')])+
   '<p>Stolen information may enable identity abuse, but the two terms are not interchangeable. Intruders may be insiders as well as outsiders. This unit does not invent statute sections, mandatory reporting deadlines or guaranteed remedies; use current appropriate official advice for the jurisdiction.</p>','sec5_crime'),
  topic('4.2 Cyberstalking, malware distribution and safe reporting',
   '<p><b>Cyberstalking</b> concerns abusive persistent online monitoring/contact/threatening conduct in its factual/legal context. <b>Malware distribution</b> involves spreading malicious code; discussing a category does not authorize obtaining, forwarding or executing dangerous samples.</p>'+ul(
    'Protect personal information, use appropriate platform safety/block/report controls and seek trusted support. For a student, trusted staff/guardians may help. If there is immediate danger, seek local emergency assistance.',
    'Preserve appropriate evidence safely under the relevant procedure; do not expose someone’s private details publicly, confront suspects or conduct unauthorized tracing/investigation.',
    'For suspected malicious files or account abuse, follow the organization’s incident channel and qualified responder instructions. Do not run suspicious material or forward harmful attachments merely to prove a point.',
    'Use current verified official channels for the place/incident. CERT-In’s official site is linked for Indian advisories/contact information; it is not presented as a substitute for every appropriate reporting authority.') )]},
 {'title':tr('5. Safe Study and Defensive Practice'),'items':[
  topic('5.1 Practical 11: prevention, detection, response and recovery',
   table(['Stage','Examples','Important limitation'],[
    ('Prevent','Appropriate updates, trusted sources, least privilege, suitable MFA, parameterized input handling and controlled exposure.','No one control guarantees prevention; protection must fit the use and threat.'),
    ('Detect','Relevant logs/alerts, trusted integrity checks and investigation of context.','A changed hash, address or pattern is a clue, not automatic attribution or malware proof.'),
    ('Respond','Use authorized procedures, contain appropriately and preserve/report relevant evidence safely.','Unplanned actions may damage evidence or services; do not conduct unauthorized counterattacks.'),
    ('Recover','Restore known-good data/services under an appropriate plan and verify the result.','Recovery of one file does not prove the host is clean or that the incident is resolved.')])+
   '<p>The real recovery exercise changes and restores one harmless temporary file and verifies its digest. Its same-folder copy is <b>not</b> an offline/immutable backup design or a ransomware experiment. Real backups need appropriate separation, access protection, consistency and tested restoration. The case sheet and reporting guide are fictional study work, not actual incident investigations.</p>','sec5_defence',programs=['sec5p09']),
  topic('5.2 Practical 12: what Kali Linux is—and what is only guided',
   '<p><b>Kali Linux</b> is a specialized distribution/toolkit for professional security assessment and auditing. Its official documentation warns that it is not the default general-purpose beginner desktop. Tool access does not grant permission to test other people’s systems.</p>'+ul(
    'The optional VM/OS guide uses official sources, appropriate isolation/snapshots, deliberate shared-folder/network choices and an instructor-approved lab scope.',
    'Read-only OS/user/file/interface observations in a learner’s own Kali VM are suggested, but <b>Kali is not downloaded, installed or booted here</b>. The reference host is Debian 13, not Kali.',
    'No malware, offensive toolkit, persistence, credential harvesting, scanning of public systems or multi-gigabyte ISO/VM is included.',
    'A VM is not a guarantee that executing malware is safe. This introductory study does not require real malware execution or bridging an experiment onto an unapproved network.') ),
  topic('5.3 Actual Kali signed-metadata check: distinguish three stages',
   '<p>The small reference fixture contains the official <b>Kali 2026.3</b> SHA256SUMS file, detached signature, public archive signing key and provenance record. It uses the primary fingerprint checked against official Kali documentation on 29 October 2026:</p><p><code>827C8569F2518CC677FECA1AED65462EC8D5E4C5</code></p>'+table(['Stage','Reference status','What it establishes'],[
    ('Verify manifest signature under the pinned public key.','Actually executed with GPG 2.4.7 in an isolated temporary keyring.','The signed metadata verifies under the explicitly pinned key; no automatic global ownertrust is asserted.'),
    ('Hash the actual downloaded ISO and compare its filename/digest.','NOT performed: no ISO bytes were downloaded.','Required before claiming those image bytes match the signed entry.'),
    ('Install/boot/study an appropriate isolated Kali VM.','Guided only; NOT performed.','A separate learner/instructor activity, not proof supplied by the metadata signature.')])+
   '<p>The frozen published entry is <code>kali-linux-2026.3-installer-amd64.iso</code>. Its <b>published manifest digest</b> matches the separately checked official download-page value; it is not a digest computed from an ISO we possess. The example disables automatic key retrieval, checks VALIDSIG under the pin and deletes its keyring. A tampered manifest/signature or wrong pin is rejected in tests.</p><p>Before a new real download, check current official version/key/status through a trusted channel. A public key from an unexpected message or an untrusted checksum page is not automatically authentic. Hash/signature checks have different trust assumptions; neither a historical valid manifest nor this lab guarantees that a future installed OS is secure.</p>','sec5_kali',programs=['sec5p10']),
  topic('5.4 Evidence boundaries, journal and official assessment',
   '<p>The ten supporting scripts use actual in-memory SQL protections, offline URL/email parsing, fictional ARP/rate models, benign owned files/recovery, an owned TLS identity check and frozen signed-metadata verification. They do not perform the attacks whose names appear in the syllabus.</p>'+ul(
    'Python standard library handles the local models/files/SQLite; the TLS example needs OpenSSL 3 and the metadata check needs GPG. Provided helpers/data sit beside the root scripts; no pip package or PYTHONPATH setup is required.',
    'No real identities/accounts/messages, malware samples, user credentials, public target, spoofed traffic, botnet/C2, flood or Kali OS is used. Only the TLS example briefly opens owned loopback sockets; workers/temporary keys/keyrings/files are removed.',
    'Practicals 11/12 are study-oriented. The case/VM guides distinguish expected learner steps from the actual reference observations; a generic Debian output is not relabelled as Kali.',
    'The official course remains 70+30 theory and 20+30 practical=150. Unit 5 is 8 hours/15% syllabus weight, not a guaranteed question allocation. The sixteen original answered questions have suggested 3/4/7-mark practice sizes, not official GTU papers or predictions.')+
   '<p><b>References:</b> '+', '.join('<a href="'+u+'">'+n+'</a>' for n,u in SOURCES)+'. NIST2013 and archived CISA pages support educational fundamentals, not current legal or vendor-performance claims. Explanations/examples are original and all case identities are fictional.</p>')]}]

PRACTICE=[
 ('Define cyber security and cyberspace with CIA and personal-impact examples.',4,
  '<p>Cyber security protects digital systems, communications, services and information against relevant threats. Cyberspace is the interconnected digital environment of systems/data/services/online interaction. Unauthorized disclosure affects confidentiality, improper changes affect integrity, and unusable services affect availability. Harm can also affect privacy, money, reputation and personal safety. Tools alone do not replace people, process, configuration, access and recovery controls.</p>'),
 ('Distinguish threat, vulnerability, attack, intruder and hacker.',4,
  '<p>A threat has potential for harm; a vulnerability is a weakness that can be exploited/triggered; an attack is an attempted/actual malicious or unauthorized action against a security goal. An intruder attempts/causes policy violations and may be an insider or outsider. Hacker is a broader contextual term: authorized testing/research is not automatically criminal. A weakness, unusual event or outage alone does not prove compromise or identify a person.</p>'),
 ('Compare virus, worm and Trojan and explain why categories can overlap.',7,
  '<p>A virus is associated with a host file/program and an infection/execution mechanism; a worm self-propagates between systems without relying on the same host-file model; a Trojan presents malicious functionality as something useful/legitimate. A Trojan may install spyware, a backdoor or bot component, so these are not mutually exclusive labels. Use trusted sources, updates, controlled execution/exposure and appropriate detection/response. No real malware sample is required or executed in the class examples.</p>'),
 ('Explain adware and spyware without treating every advertisement or authorized monitor as crime.',3,
  '<p>Adware relates to advertising behaviour and can be unwanted/intrusive/deceptively bundled, but advertising software is not automatically criminal. Spyware covertly monitors/collects information contrary to awareness or authorization. Consent, transparency, policy and facts distinguish legitimate monitoring from abuse. Symptoms are not conclusive attribution; avoid unverified cleanup tools and use trusted installation/permission/update practices.</p>'),
 ('Define botnet and backdoor with defensive implications.',4,
  '<p>A botnet coordinates controlled/compromised devices for harmful activity; their owners may also be victims. A backdoor provides concealed/unauthorized access bypassing intended controls. These are capabilities and may follow different compromise/propagation routes. Reduce exposure and privileges, patch, monitor appropriate evidence and use trusted response processes. Do not operate suspected infrastructure or create persistence/remote control merely to study the definition.</p>'),
 ('Compare DoS and DDoS and interpret the six-event limiter model.',4,
  '<p>DoS maliciously disrupts legitimate use; DDoS distributes participation across multiple systems. An outage can also be a fault or maintenance/permission issue. The token-bucket fixture at times 0,0,0,1,1,2 with capacity 2/refill 1 allows four and limits two logical admissions. It sends no network requests or flood. Local rate limiting is one possible control concept, not a guarantee against upstream saturation or a resilience benchmark.</p>'),
 ('Explain MITM/on-path interference and the limits of TLS validation.',7,
  '<p>An attacker may interpose in a path to relay/read/alter communication. Appropriate authenticated protocols and authentic key/certificate trust can help; do not ignore failed identity validation. The real owned loopback TLS example succeeds under its correct server name and rejects a wrong hostname, with cleanup. It is not an actual MITM attack/detector, public TLS audit or client-certificate authentication. A phisher can have a valid certificate for their own lookalike name, and compromised endpoints/trust roots remain different risks.</p>'),
 ('Differentiate IP spoofing and ARP spoofing; what does a mapping change prove?',4,
  '<p>IP spoofing misrepresents source IP information; ARP spoofing misrepresents an IPv4-to-link-address mapping on the relevant local network. An address is not identity. A changed fictional mapping is a signal to investigate, not proof of poisoning or attribution; legitimate replacement/failover may explain it. The program only compares dictionaries: it does not read/change a live ARP cache or send forged packets. Use appropriate network safeguards and authenticated protocols under policy.</p>'),
 ('Explain SQL injection and the actual parameterized-query result.',7,
  '<p>Injection occurs when untrusted input changes SQL syntax. Keep query structure fixed and bind data values through the API. In the real in-memory fixture, normal C01 returns one row; the fixed SQL-like value returns zero because it remains a literal, and both rows stay intact. No vulnerable concatenated query or public account attack occurs. Bindings normally cannot select table/column names; choose structure from owned allow-lists. Also enforce least privilege and application authorization; safe values alone do not decide access.</p>'),
 ('Explain the SQLite authorizer example and why it is not complete authorization.',3,
  '<p>The own in-memory connection allows SELECT/READ, denies DELETE with an actual SQLite authorization error and still has two rows. That is a per-connection fixture restriction, not an OS/database-account privilege framework, row-access policy or proof that an application is secure. Appropriate real roles/permissions, API/query design and authorization checks are still needed.</p>'),
 ('Explain phishing hints and why hostname/header parsing or HTTPS is not proof.',7,
  '<p>Deception may use unexpected requests, urgency, display names, misleading links or attachments across email/messages/calls. Pause and verify via a separately known trusted route; do not disclose passwords/login codes or open unexpected material. A familiar URL prefix/userinfo is not the parsed host; From display text is not sender authentication. HTTPS and correct grammar do not establish legitimacy. The examples parse only reserved .test strings and neutral in-memory headers, with no link opening, email delivery, SPF/DKIM/DMARC or automatic phishing verdict.</p>'),
 ('Distinguish identity theft, information theft and hacking in the crime context.',4,
  '<p>Identity theft misuses identifying/account data for impersonation or identity abuse. Information theft concerns unauthorized acquisition/disclosure of protected data; it may enable identity abuse but is not the same term. Hacking in the crime context concerns unauthorized access/exploitation/harm, not every authorized security activity. Protect information/accounts and report through appropriate trusted procedures. Educational labels are not legal findings; facts and jurisdiction matter.</p>'),
 ('Describe a privacy-preserving response to cyberstalking or suspected malware distribution.',4,
  '<p>Use appropriate platform safety/block/report functions and trusted support, preserving relevant evidence safely without publishing victim details or forwarding harmful material. Students may involve trusted staff/guardians; immediate danger calls for local emergency assistance. Follow institutional/appropriate official reporting channels and qualified responder guidance. Do not confront suspects, conduct unauthorized tracking, run malware or assume a legal outcome from one observation. The unit does not invent legal sections or reporting deadlines.</p>'),
 ('Explain prevention, detection, response and recovery using the benign file examples.',7,
  '<p>Prevent with appropriate hardening/trusted sources/access/input controls; detect with relevant trusted evidence; respond under authorized containment/reporting/evidence procedures; recover known-good data/services and verify the outcome. A real changed digest detects one benign file change, not malware identity or attribution. The separate recovery really restores one own file, but its same-folder copy is not an offline/immutable backup architecture, ransomware test or proof that a compromised host is clean.</p>'),
 ('State Kali Linux’s role and a safe guided VM study plan.',4,
  '<p>Kali is a specialized security-assessment/auditing distribution, not a default beginner general-purpose desktop or permission to target others. Use authentic official sources, check current keys/signatures and actual image hashes, then follow an instructor-approved isolated VM plan with deliberate networking/integration/snapshots. A VM does not make malware execution automatically safe. Kali-side read-only observations are guided; no Kali OS/ISO/VM or offensive toolkit is installed/booted/run in this reference.</p>'),
 ('Interpret the signed Kali metadata result and the unperformed ISO/boot stages.',7,
  '<p>Actual GPG verifies frozen official Kali 2026.3 SHA256SUMS under primary 827C8569F2518CC677FECA1AED65462EC8D5E4C5, checked against official documentation, in an isolated temporary keyring with automatic retrieval disabled. The published installer entry is authenticated under that pin; it is not a hash computed from a downloaded ISO. No ISO bytes were obtained/verified and no Kali VM booted. A real new download still needs a current authentic key/version/status, signature validation and local hashing of the actual image before guided installation. Historical metadata validity is not permanent security or global ownertrust.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('6. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}
CARDS=[
 ('Threat versus weakness versus action','Threat: potential harm\nVulnerability: weakness\nAttack: attempted/actual unauthorized action','A weakness or symptom alone is not proof of compromise or attribution.'),
 ('Malware distinctions','Virus: host/infection model\nWorm: self-propagation\nTrojan: deceptive malicious functionality','Adware/spyware/bot/backdoor capabilities can overlap; no samples are executed.'),
 ('Availability and limiting','DoS/DDoS: malicious availability disruption\nSix-case limiter: logical decisions only','No flood/load test; local admission control does not guarantee upstream DDoS resilience.'),
 ('MITM and identity checks','Use appropriate authenticated protocols\nDo not bypass certificate/name failures','Correct TLS to an attacker’s own site does not make that site honest.'),
 ('IP versus ARP spoofing','IP: source IP claim\nARP: local IPv4-to-link-address claim','Only fictional mappings are compared; no spoofed packets/cache writes.'),
 ('Parameterized SQL','SELECT title FROM courses WHERE code = ?\nBind the value separately through the API','Query structure/identifier choices need fixed allow-lists; binding does not authorize the caller.'),
 ('Phishing precautions','Pause -> verify through a known trusted route\nReport appropriately; do not disclose codes','Display names, From parsing, HTTPS or perfect grammar alone do not prove legitimacy.'),
 ('Cybercrime categories','Identity theft; information theft\nUnauthorized hacking; cyberstalking\nMalware distribution','Educational categories are not legal findings. Protect privacy and use current appropriate official channels.'),
 ('Defence cycle','Prevent -> detect -> respond -> recover','A changed hash is not malware proof. One restored file is not full incident recovery.'),
 ('Kali study scope','Specialized assessment/auditing distribution\nVM/OS commands are guided only','No ISO/VM download, Kali boot or offensive-tool execution is performed.'),
 ('Downloaded-image trust stages','1. Verify signed manifest under authentic key\n2. Hash/compare actual downloaded image\n3. Guided safe installation/OS study','Only stage 1 runs here, in an isolated keyring. A checksum and digital signature are different checks.'),
 ('Frozen metadata reference','Kali 2026.3 signed metadata\nPrimary fingerprint pinned from official docs\nNo global keyring or keyserver lookup','Not a perpetual latest-release, key-validity or ISO-security guarantee; no ISO bytes are present.')]
SYNTAX=[{'title':tr('Cyber Security Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]
QA=[
 ('What is cyber security?','Protection of digital systems, communications, services and information against relevant threats/attacks.'),
 ('What is cyberspace?','The interconnected digital environment where systems, data, services and online interactions operate.'),
 ('How does a threat differ from a vulnerability?','Potential harm/source/event versus an exploitable/triggerable weakness.'),
 ('Does a vulnerability prove an attack occurred?','No. A weakness is not itself evidence of compromise or attribution.'),
 ('Is every hacker a criminal intruder?','No. Authorized security work differs from unauthorized access/harm; scope and permission matter.'),
 ('What distinguishes a virus from a worm?','Virus uses a host/infection model; a worm self-propagates between systems without that same dependency.'),
 ('What is a Trojan?','Malicious functionality presented as something legitimate or useful.'),
 ('Can malware categories overlap?','Yes. A Trojan may install spyware, a backdoor or a bot component.'),
 ('Is all advertising software automatically criminal malware?','No. Adware can be unwanted/intrusive/deceptive, but consent, behaviour and legal context matter.'),
 ('What is spyware?','Covert information collection/monitoring contrary to awareness or authorization.'),
 ('What is a botnet?','Coordinated controlled/compromised devices that may be used for harmful activity; owners may also be victims.'),
 ('What is a backdoor?','Concealed/unauthorized access bypassing intended access controls.'),
 ('How do DoS and DDoS differ?','DDoS distributes participation across multiple systems; both maliciously disrupt legitimate availability.'),
 ('Does an outage alone prove DoS?','No. Faults, maintenance, configuration or permissions can also explain it.'),
 ('What is MITM/on-path interference?','An attacker interposes in communication, potentially reading, relaying or altering it.'),
 ('What does IP spoofing misrepresent?','Source IP information, which is not an authenticated identity by itself.'),
 ('What does ARP spoofing misrepresent?','An IPv4-to-link-address mapping on the relevant local network.'),
 ('Does a changed MAC mapping prove poisoning?','No. Legitimate replacement/failover may also explain it; the example only compares fictional dictionaries.'),
 ('What is SQL injection?','Untrusted input becomes part of SQL syntax rather than remaining data.'),
 ('What is the main query defence shown?','Keep structure fixed and bind data values through the database API.'),
 ('Can a value placeholder choose a table/column name safely?','Normally no. Keep structural choices fixed or map them from a small owned allow-list.'),
 ('Does parameter binding decide user authorization?','No. Appropriate application access controls and least privilege are separate requirements.'),
 ('What is phishing?','Deceptive communication/site content intended to trick people into harmful disclosure or action.'),
 ('Do good grammar, a familiar display name or HTTPS prove legitimacy?','No. Verify using a separately known trusted route; parsing is not authentication.'),
 ('Does login OTP mean the same as Unit 2’s OTP cipher?','No. Here it means a one-time passcode; Unit 2 discusses a one-time pad.'),
 ('How do identity theft and information theft differ?','Identity misuse/impersonation versus unauthorized acquisition/disclosure of protected data; one may enable the other.'),
 ('What is a safe cyberstalking response principle?','Protect privacy, preserve appropriate evidence safely and seek trusted support/official channels; do not conduct unauthorized tracing.'),
 ('Does a hash mismatch identify malware or an attacker?','No. It only establishes a difference against the chosen reference under its assumptions.'),
 ('Does one restored same-folder file prove ransomware resilience?','No. The fixture is not an offline/immutable backup system or proof that a host is clean.'),
 ('What is Kali intended for?','Specialized authorized security assessment/auditing, not a default beginner desktop or permission to target others.'),
 ('What Kali activity is actually executed?','Only GPG verification of frozen official signed metadata; no ISO download/verification, installation or OS boot.'),
 ('Why is a valid manifest signature insufficient to verify an absent ISO?','The actual image bytes must still be hashed and compared under an appropriate authentic/current trust process.')]
VIVA=[{'title':tr('Unit 5 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
