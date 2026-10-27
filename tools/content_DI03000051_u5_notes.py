"""Computer Networks (DI03000051) - Unit 5 notes part A: 5.1 Security basics, 5.2 Threats.
Part B (5.3 Firewalls) is in content_DI03000051_u5_notes_b."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

PA_EN = tbl(["Passive attack", "Active attack"], [
    ("Attacker only observes / copies data", "Attacker modifies, blocks or creates data"),
    ("Threat to confidentiality", "Threat to integrity, availability, authenticity"),
    ("Hard to detect (no change in data)", "Easier to detect, harder to prevent"),
    ("Prevented mainly by encryption", "Handled by detection and recovery"),
    ("e.g. eavesdropping, traffic analysis", "e.g. DoS, man-in-the-middle, replay, spoofing")])
PA_GU = tbl(["Passive attack", "Active attack"], [
    ("Attacker ફક્ત data જુએ / copy કરે", "Attacker data બદલે, અટકાવે કે બનાવે"),
    ("Confidentiality ને ખતરો", "Integrity, availability, authenticity ને ખતરો"),
    ("શોધવો મુશ્કેલ (data માં ફેરફાર નહીં)", "શોધવો સહેલો, અટકાવવો મુશ્કેલ"),
    ("મુખ્યત્વે encryption થી અટકાવાય", "Detection અને recovery થી સંભાળાય"),
    ("દા.ત. eavesdropping, traffic analysis", "દા.ત. DoS, man-in-the-middle, replay, spoofing")])

VW_EN = tbl(["Virus", "Worm"], [
    ("Attaches itself to a host file or program", "Standalone program; needs no host"),
    ("Spreads when the user runs the infected file / shares it", "Spreads automatically over the network"),
    ("Needs human action", "No human action needed"),
    ("Mainly damages files and programs on a computer", "Mainly consumes bandwidth and spreads to many computers"),
    ("Spreads slower", "Spreads very fast"),
    ("e.g. CIH, Melissa (macro virus)", "e.g. Morris worm, WannaCry, ILOVEYOU")])
VW_GU = tbl(["Virus", "Worm"], [
    ("પોતાને host file કે program સાથે જોડે", "સ્વતંત્ર program; host ની જરૂર નહીં"),
    ("User infected file ચલાવે / share કરે ત્યારે ફેલાય", "Network પર આપમેળે ફેલાય"),
    ("માનવ ક્રિયા જોઈએ", "માનવ ક્રિયાની જરૂર નહીં"),
    ("મુખ્યત્વે computer પરની files અને programs ને નુકસાન", "મુખ્યત્વે bandwidth વાપરે અને ઘણાં computers માં ફેલાય"),
    ("ધીમો ફેલાય", "ખૂબ ઝડપથી ફેલાય"),
    ("દા.ત. CIH, Melissa (macro virus)", "દા.ત. Morris worm, WannaCry, ILOVEYOU")])

SEC_5_1 = {
    "title": {"en": "5.1 Security Basics", "gu": "5.1 Security Basics"},
    "items": [
        T("5.1.1 Introduction to Network Security", "5.1.1 Network Security નો પરિચય",
          """<p><b>Network security</b> is the set of policies, practices and technologies used to protect a network and the data travelling over it from <b>unauthorised access, misuse, modification, theft or destruction</b>. It covers hardware, software, users and procedures.</p>
<h4>Need for network security</h4>
<ul><li>Organisations store valuable data: bank accounts, student results, medical records, trade secrets.</li>
<li>Networks are open: the Internet connects billions of devices, so attackers anywhere can try to break in.</li>
<li>Attacks cause financial loss, loss of reputation and legal problems (e.g. the IT Act 2000 in India).</li>
<li>Online banking, UPI payments and e-governance depend on trust.</li></ul>
<h4>Basic terms</h4>
<ul><li><b>Asset:</b> anything of value (data, hardware, service).</li>
<li><b>Vulnerability:</b> a weakness that can be exploited (unpatched software, weak password).</li>
<li><b>Threat:</b> a possible danger that may exploit a vulnerability (a hacker, a virus).</li>
<li><b>Attack:</b> an actual attempt to exploit a vulnerability.</li>
<li><b>Risk:</b> the chance of a threat exploiting a vulnerability and the damage that would result.</li></ul>
<h4>Security attacks</h4>
<ul><li><b>Interruption:</b> the message or service is destroyed or made unavailable (attack on availability, e.g. DoS, cutting a cable).</li>
<li><b>Interception:</b> an unauthorised party reads the message (attack on confidentiality, e.g. wire-tapping, packet sniffing).</li>
<li><b>Modification:</b> the message is altered in transit (attack on integrity, e.g. man-in-the-middle).</li>
<li><b>Fabrication:</b> a fake message is inserted as if from a genuine sender (attack on authenticity, e.g. spoofing, phishing email).</li></ul>
""" + PA_EN,
          """<p><b>Network security</b> એ network અને તેના પર જતા data ને <b>અનધિકૃત access, દુરુપયોગ, ફેરફાર, ચોરી કે નાશ</b> થી બચાવવા વપરાતી નીતિઓ, પદ્ધતિઓ અને technologies નો સમૂહ છે. તેમાં hardware, software, users અને કાર્યપદ્ધતિઓ આવે.</p>
<h4>Network security ની જરૂરિયાત</h4>
<ul><li>સંસ્થાઓ કિંમતી data રાખે: bank accounts, student results, medical records, trade secrets.</li>
<li>Networks ખુલ્લા છે: Internet અબજો devices જોડે, તેથી ગમે ત્યાંથી attackers ઘૂસવાનો પ્રયાસ કરી શકે.</li>
<li>Attacks થી આર્થિક નુકસાન, પ્રતિષ્ઠા ગુમાવવી અને કાનૂની સમસ્યાઓ થાય (દા.ત. ભારતમાં IT Act 2000).</li>
<li>Online banking, UPI payments અને e-governance વિશ્વાસ પર આધારિત છે.</li></ul>
<h4>મૂળભૂત શબ્દો</h4>
<ul><li><b>Asset:</b> કિંમત ધરાવતી કોઈ પણ વસ્તુ (data, hardware, service).</li>
<li><b>Vulnerability:</b> exploit કરી શકાય તેવી નબળાઈ (unpatched software, નબળો password).</li>
<li><b>Threat:</b> vulnerability નો લાભ લઈ શકે તેવો સંભવિત ખતરો (hacker, virus).</li>
<li><b>Attack:</b> vulnerability નો લાભ લેવાનો વાસ્તવિક પ્રયાસ.</li>
<li><b>Risk:</b> threat દ્વારા vulnerability નો લાભ લેવાની શક્યતા અને તેનાથી થતું નુકસાન.</li></ul>
<h4>Security attacks</h4>
<ul><li><b>Interruption:</b> message કે service નાશ પામે કે અનુપલબ્ધ બને (availability પર attack, દા.ત. DoS, cable કાપવો).</li>
<li><b>Interception:</b> અનધિકૃત વ્યક્તિ message વાંચે (confidentiality પર attack, દા.ત. wire-tapping, packet sniffing).</li>
<li><b>Modification:</b> રસ્તામાં message બદલાય (integrity પર attack, દા.ત. man-in-the-middle).</li>
<li><b>Fabrication:</b> સાચા sender તરફથી હોય તેમ નકલી message ઉમેરાય (authenticity પર attack, દા.ત. spoofing, phishing email).</li></ul>
""" + PA_GU,
          diagram="cn5_attacks"),
        T("5.1.2 CIA Triad", "5.1.2 CIA Triad",
          """<p>The three basic goals of information security are known as the <b>CIA triad</b>: <b>Confidentiality, Integrity and Availability</b>. Every security mechanism (password, encryption, firewall, backup) supports one or more of these goals.</p>
<ul>
<li><b>Confidentiality:</b> information is disclosed only to authorised people. Threat: <b>disclosure</b> (snooping, sniffing).</li>
<li><b>Integrity:</b> information is accurate and is changed only by authorised people in authorised ways. Threat: <b>alteration</b> (modification, tampering).</li>
<li><b>Availability:</b> information and services are accessible to authorised users <b>whenever needed</b>. Threat: <b>denial</b> (DoS, hardware failure, disaster).</li>
</ul>
<p>The goals must be balanced: making data extremely confidential (many locks) can reduce availability, and vice versa.</p>
<h4>Related security services</h4>
<ul><li><b>Authentication:</b> verifying the identity of a user or device (password, OTP, fingerprint).</li>
<li><b>Authorisation / access control:</b> deciding what an authenticated user may do.</li>
<li><b>Non-repudiation:</b> a sender cannot later deny sending a message (digital signature).</li></ul>""",
          """<p>Information security ના ત્રણ મૂળભૂત ધ્યેયો <b>CIA triad</b> તરીકે ઓળખાય: <b>Confidentiality, Integrity અને Availability</b>. દરેક security mechanism (password, encryption, firewall, backup) આમાંના એક કે વધુ ધ્યેયોને ટેકો આપે.</p>
<ul>
<li><b>Confidentiality:</b> માહિતી ફક્ત અધિકૃત લોકોને જ જાહેર થાય. ખતરો: <b>disclosure</b> (snooping, sniffing).</li>
<li><b>Integrity:</b> માહિતી સચોટ હોય અને ફક્ત અધિકૃત લોકો દ્વારા અધિકૃત રીતે જ બદલાય. ખતરો: <b>alteration</b> (modification, tampering).</li>
<li><b>Availability:</b> માહિતી અને services અધિકૃત users ને <b>જરૂર પડે ત્યારે</b> ઉપલબ્ધ હોય. ખતરો: <b>denial</b> (DoS, hardware failure, આપત્તિ).</li>
</ul>
<p>ધ્યેયો વચ્ચે સંતુલન જરૂરી: data ને અતિશય confidential બનાવવાથી (ઘણાં તાળાં) availability ઘટી શકે, અને ઊલટું.</p>
<h4>સંબંધિત security services</h4>
<ul><li><b>Authentication:</b> user કે device ની ઓળખ ચકાસવી (password, OTP, fingerprint).</li>
<li><b>Authorisation / access control:</b> authenticated user શું કરી શકે તે નક્કી કરવું.</li>
<li><b>Non-repudiation:</b> sender પછીથી message મોકલ્યાનો ઇનકાર ન કરી શકે (digital signature).</li></ul>""",
          diagram="cn5_cia"),
        T("5.1.3 Confidentiality", "5.1.3 Confidentiality",
          """<p><b>Confidentiality</b> means protecting information from <b>unauthorised disclosure</b>. Only the intended, authorised people should be able to read it, both while it is <b>stored</b> (data at rest) and while it is <b>transmitted</b> (data in transit).</p>
<h4>Threats</h4>
<ul><li>Eavesdropping / packet sniffing on a network (e.g. on open public Wi-Fi).</li><li>Stolen passwords, shoulder surfing, social engineering.</li><li>Lost or stolen laptops and pen drives; insiders leaking data.</li></ul>
<h4>Mechanisms</h4>
<ul>
<li><b>Encryption:</b> converts readable <b>plaintext</b> into unreadable <b>ciphertext</b> using a <b>key</b>; only someone with the right key can decrypt it.
<ul><li><b>Symmetric (secret key):</b> the same key encrypts and decrypts (AES, DES). Fast.</li><li><b>Asymmetric (public key):</b> a public key encrypts and the matching private key decrypts (RSA). Solves key distribution.</li></ul></li>
<li><b>Access control:</b> user IDs, passwords, permissions, multi-factor authentication.</li>
<li>Secure protocols: <b>HTTPS (TLS)</b>, SSH, VPN, WPA2 / WPA3 on Wi-Fi.</li>
<li>Data classification and physical security (locked server rooms).</li>
</ul>""",
          """<p><b>Confidentiality</b> એટલે માહિતીને <b>અનધિકૃત disclosure</b> થી બચાવવી. માહિતી <b>સંગ્રહિત</b> હોય (data at rest) અને <b>મોકલાતી</b> હોય (data in transit) ત્યારે ફક્ત ઇચ્છિત, અધિકૃત લોકો જ તે વાંચી શકે.</p>
<h4>ખતરા</h4>
<ul><li>Network પર eavesdropping / packet sniffing (દા.ત. ખુલ્લા public Wi-Fi પર).</li><li>ચોરાયેલા passwords, shoulder surfing, social engineering.</li><li>ખોવાયેલા કે ચોરાયેલા laptops અને pen drives; insiders દ્વારા data leak.</li></ul>
<h4>Mechanisms</h4>
<ul>
<li><b>Encryption:</b> વાંચી શકાય તેવા <b>plaintext</b> ને <b>key</b> વાપરીને ન વાંચી શકાય તેવા <b>ciphertext</b> માં ફેરવે; સાચી key ધરાવનાર જ decrypt કરી શકે.
<ul><li><b>Symmetric (secret key):</b> સરખી key encrypt અને decrypt કરે (AES, DES). ઝડપી.</li><li><b>Asymmetric (public key):</b> public key encrypt કરે અને મેળ ખાતી private key decrypt કરે (RSA). Key distribution ની સમસ્યા ઉકેલે.</li></ul></li>
<li><b>Access control:</b> user IDs, passwords, permissions, multi-factor authentication.</li>
<li>Secure protocols: <b>HTTPS (TLS)</b>, SSH, VPN, Wi-Fi પર WPA2 / WPA3.</li>
<li>Data classification અને physical security (તાળાબંધ server rooms).</li>
</ul>""",
          diagram="cn5_encrypt", examples=["cn5n1"]),
        T("5.1.4 Integrity", "5.1.4 Integrity",
          """<p><b>Integrity</b> means that data is <b>accurate, complete and unchanged</b> except by authorised people through authorised processes. The receiver must be able to detect if a message was altered, accidentally (noise, errors) or deliberately (attack).</p>
<h4>Threats</h4>
<ul><li>Man-in-the-middle attack changing data in transit (e.g. changing the amount or account number in a payment).</li><li>Viruses corrupting files; unauthorised database updates (changing marks).</li><li>Transmission errors and hardware faults.</li></ul>
<h4>Mechanisms</h4>
<ul>
<li><b>Hash functions</b> (MD5, SHA-256): produce a fixed-size <b>message digest</b> (fingerprint). The receiver recomputes the hash; if it differs, the data was changed. Even a 1-character change gives a completely different hash.</li>
<li><b>Message Authentication Code (MAC / HMAC):</b> hash combined with a secret key, so an attacker cannot recompute it.</li>
<li><b>Digital signatures:</b> hash encrypted with the sender's private key; give integrity, authentication and non-repudiation.</li>
<li>Checksums and CRC for accidental errors; access permissions, version control, audit logs and backups.</li>
</ul>""",
          """<p><b>Integrity</b> એટલે data <b>સચોટ, સંપૂર્ણ અને બદલાયા વગરનો</b> રહે, સિવાય કે અધિકૃત લોકો અધિકૃત પ્રક્રિયાઓ દ્વારા બદલે. Message આકસ્મિક (noise, errors) કે ઇરાદાપૂર્વક (attack) બદલાયો હોય તો receiver તે શોધી શકવો જોઈએ.</p>
<h4>ખતરા</h4>
<ul><li>રસ્તામાં data બદલતો man-in-the-middle attack (દા.ત. payment માં રકમ કે account number બદલવો).</li><li>Files બગાડતા viruses; અનધિકૃત database updates (marks બદલવા).</li><li>Transmission errors અને hardware faults.</li></ul>
<h4>Mechanisms</h4>
<ul>
<li><b>Hash functions</b> (MD5, SHA-256): fixed-size <b>message digest</b> (fingerprint) બનાવે. Receiver ફરી hash ગણે; જો અલગ હોય, તો data બદલાયો છે. 1 અક્ષરનો ફેરફાર પણ સંપૂર્ણ અલગ hash આપે.</li>
<li><b>Message Authentication Code (MAC / HMAC):</b> secret key સાથે જોડેલો hash, જેથી attacker તે ફરી ગણી ન શકે.</li>
<li><b>Digital signatures:</b> sender ની private key થી encrypt કરેલો hash; integrity, authentication અને non-repudiation આપે.</li>
<li>આકસ્મિક errors માટે checksums અને CRC; access permissions, version control, audit logs અને backups.</li>
</ul>""",
          diagram="cn5_hash", examples=["cn5n2"]),
        T("5.1.5 Availability", "5.1.5 Availability",
          """<p><b>Availability</b> means that systems, networks and data are <b>accessible and usable by authorised users whenever they need them</b>. A perfectly confidential and accurate system is useless if it cannot be reached (e.g. a results website that crashes on result day).</p>
<h4>Threats</h4>
<ul><li><b>Denial of Service (DoS):</b> an attacker floods a server with requests so genuine users cannot be served. <b>Distributed DoS (DDoS)</b> uses thousands of infected computers (a <b>botnet</b>).</li>
<li><b>Ransomware</b> encrypting files and demanding payment.</li><li>Hardware / power failure, software bugs, natural disasters (flood, fire), accidental deletion.</li></ul>
<h4>Mechanisms</h4>
<ul><li><b>Redundancy:</b> backup servers, RAID disks, multiple network links, clustering, load balancers.</li>
<li><b>Regular backups</b> and a disaster recovery plan (off-site / cloud copies).</li>
<li>UPS and generators; regular maintenance and patching.</li>
<li>Firewalls, intrusion prevention, rate limiting and anti-DDoS / CDN services.</li></ul>
<p>Availability is measured as <b>uptime %</b>: 99.9% ("three nines") still allows about 8.8 hours of downtime per year.</p>""",
          """<p><b>Availability</b> એટલે systems, networks અને data <b>અધિકૃત users ને જરૂર પડે ત્યારે ઉપલબ્ધ અને વાપરી શકાય તેવા</b> હોય. સંપૂર્ણ confidential અને સચોટ system પણ જો પહોંચી ન શકાય તો નકામું છે (દા.ત. result ના દિવસે crash થતી results website).</p>
<h4>ખતરા</h4>
<ul><li><b>Denial of Service (DoS):</b> attacker server ને requests થી ભરી દે જેથી સાચા users ને service ન મળે. <b>Distributed DoS (DDoS)</b> હજારો infected computers (<b>botnet</b>) વાપરે.</li>
<li>Files encrypt કરી પૈસા માગતું <b>ransomware</b>.</li><li>Hardware / power failure, software bugs, કુદરતી આપત્તિઓ (પૂર, આગ), આકસ્મિક deletion.</li></ul>
<h4>Mechanisms</h4>
<ul><li><b>Redundancy:</b> backup servers, RAID disks, અનેક network links, clustering, load balancers.</li>
<li><b>નિયમિત backups</b> અને disaster recovery plan (off-site / cloud copies).</li>
<li>UPS અને generators; નિયમિત maintenance અને patching.</li>
<li>Firewalls, intrusion prevention, rate limiting અને anti-DDoS / CDN services.</li></ul>
<p>Availability <b>uptime %</b> તરીકે મપાય: 99.9% ("three nines") પણ વર્ષે લગભગ 8.8 કલાક downtime આપે.</p>""",
          diagram="cn5_dos", examples=["cn5n3"]),
    ]}

SEC_5_2 = {
    "title": {"en": "5.2 Threats to Security", "gu": "5.2 Threats to Security"},
    "items": [
        T("5.2.1 Threats to Security: Overview", "5.2.1 Threats to Security: ઝાંખી",
          """<p>A <b>threat</b> is any person, program or event that can cause harm to a computer system or network. Threats come from <b>outside</b> (hackers, criminals) and <b>inside</b> (employees), and can be <b>intentional</b> or <b>accidental</b>.</p>
<p>Threats are often arranged by <b>sophistication</b> (skill, money and time available):</p>
<ul>
<li><b>Unstructured threats:</b> individuals or small groups with little money and skill, often using ready-made tools found on the Internet (<b>script kiddies</b>), and self-spreading malware like viruses and worms. Many in number, but usually detected by basic security.</li>
<li><b>Structured threats:</b> skilled, organised attackers with time and money, who plan carefully, e.g. <b>criminal organisations</b>, skilled intruders and malicious <b>insiders</b>.</li>
<li><b>Highly structured threats:</b> very large, well-funded groups that can work for years, e.g. <b>terrorist groups</b> and nations conducting <b>information warfare</b>.</li>
</ul>
<p>The syllabus threats are: <b>viruses and worms, intruders, insiders, criminal organisations, terrorists and information warfare</b>.</p>
<h4>Common types of malicious software (malware)</h4>
<ul><li><b>Virus, worm</b> (5.2.2); <b>Trojan horse:</b> looks useful but hides malicious code; <b>ransomware</b>; <b>spyware / keylogger</b>; <b>adware</b>; <b>rootkit</b>; <b>logic bomb</b>: triggers on a date or event; <b>backdoor</b>.</li></ul>""",
          """<p><b>Threat</b> એ કોઈ પણ વ્યક્તિ, program કે ઘટના છે જે computer system કે network ને નુકસાન કરી શકે. Threats <b>બહારથી</b> (hackers, criminals) અને <b>અંદરથી</b> (employees) આવે, અને <b>ઇરાદાપૂર્વક</b> કે <b>આકસ્મિક</b> હોઈ શકે.</p>
<p>Threats ઘણી વાર <b>sophistication</b> (ઉપલબ્ધ કુશળતા, પૈસા અને સમય) પ્રમાણે ગોઠવાય:</p>
<ul>
<li><b>Unstructured threats:</b> ઓછા પૈસા અને કુશળતા વાળા વ્યક્તિઓ કે નાના જૂથો, ઘણી વાર Internet પર મળતાં તૈયાર tools વાપરતા (<b>script kiddies</b>), અને viruses તથા worms જેવા જાતે ફેલાતા malware. સંખ્યામાં ઘણા, પણ સામાન્ય રીતે basic security થી પકડાય.</li>
<li><b>Structured threats:</b> સમય અને પૈસા ધરાવતા કુશળ, સંગઠિત attackers, જે કાળજીપૂર્વક યોજના બનાવે, દા.ત. <b>criminal organisations</b>, કુશળ intruders અને દુષ્ટ <b>insiders</b>.</li>
<li><b>Highly structured threats:</b> વર્ષો સુધી કામ કરી શકે તેવાં ખૂબ મોટાં, સારા ભંડોળ વાળાં જૂથો, દા.ત. <b>terrorist groups</b> અને <b>information warfare</b> કરતા દેશો.</li>
</ul>
<p>Syllabus ના threats: <b>viruses અને worms, intruders, insiders, criminal organisations, terrorists અને information warfare</b>.</p>
<h4>Malicious software (malware) ના સામાન્ય પ્રકારો</h4>
<ul><li><b>Virus, worm</b> (5.2.2); <b>Trojan horse:</b> ઉપયોગી દેખાય પણ દુષ્ટ code છુપાવે; <b>ransomware</b>; <b>spyware / keylogger</b>; <b>adware</b>; <b>rootkit</b>; <b>logic bomb</b>: તારીખ કે ઘટના પર સક્રિય થાય; <b>backdoor</b>.</li></ul>""",
          diagram="cn5_pyramid"),
        T("5.2.2 Viruses and Worms", "5.2.2 Viruses અને Worms",
          """<h4>Virus</h4>
<p>A <b>computer virus</b> is a piece of malicious code that <b>attaches itself to a host program or file</b> and <b>replicates</b> when the infected program is run. Like a biological virus, it cannot live on its own; it needs a host and usually <b>human action</b> (opening a file, running a program, inserting a pen drive) to spread.</p>
<ul><li><b>Phases:</b> dormant → propagation (copies itself into other files) → triggering (on a date or event) → execution (payload: delete files, show messages, slow the system).</li>
<li><b>Types:</b> file infector (.exe), boot sector virus, <b>macro virus</b> (Word / Excel documents), polymorphic virus (changes its code to avoid detection), stealth virus.</li></ul>
<h4>Worm</h4>
<p>A <b>worm</b> is a <b>standalone</b> malicious program that <b>copies itself from computer to computer over a network without any user action</b>, by exploiting security holes (unpatched services) or using email contacts. Worms consume huge network bandwidth and may carry payloads such as ransomware.</p>
<ul><li>Examples: <b>Morris worm</b> (1988, first major Internet worm), <b>ILOVEYOU</b> (2000, email), <b>WannaCry</b> (2017, ransomware worm via a Windows SMB flaw).</li></ul>
<h4>Protection</h4>
<p>Antivirus software with updated signatures, regular OS patches, firewalls, not opening unknown attachments or pirated software, scanning pen drives, and regular backups.</p>
""" + VW_EN,
          """<h4>Virus</h4>
<p><b>Computer virus</b> એ દુષ્ટ code નો ટુકડો છે જે <b>પોતાને host program કે file સાથે જોડે</b> અને infected program ચલાવાય ત્યારે <b>પોતાની નકલો</b> બનાવે. જૈવિક virus ની જેમ, તે જાતે જીવી ન શકે; ફેલાવા માટે host અને સામાન્ય રીતે <b>માનવ ક્રિયા</b> (file ખોલવી, program ચલાવવો, pen drive લગાવવી) જોઈએ.</p>
<ul><li><b>Phases:</b> dormant → propagation (બીજી files માં નકલ) → triggering (તારીખ કે ઘટના પર) → execution (payload: files delete કરવી, messages બતાવવા, system ધીમું કરવું).</li>
<li><b>પ્રકારો:</b> file infector (.exe), boot sector virus, <b>macro virus</b> (Word / Excel documents), polymorphic virus (પકડાવાથી બચવા code બદલે), stealth virus.</li></ul>
<h4>Worm</h4>
<p><b>Worm</b> એ <b>સ્વતંત્ર</b> દુષ્ટ program છે જે security છિદ્રો (unpatched services) નો લાભ લઈને કે email contacts વાપરીને <b>કોઈ user ક્રિયા વગર network પર computer થી computer પોતાની નકલ કરે</b>. Worms ખૂબ network bandwidth વાપરે અને ransomware જેવા payloads લઈ જઈ શકે.</p>
<ul><li>ઉદાહરણો: <b>Morris worm</b> (1988, પ્રથમ મોટો Internet worm), <b>ILOVEYOU</b> (2000, email), <b>WannaCry</b> (2017, Windows SMB ખામી દ્વારા ransomware worm).</li></ul>
<h4>રક્ષણ</h4>
<p>Updated signatures વાળું antivirus software, નિયમિત OS patches, firewalls, અજાણ્યાં attachments કે pirated software ન ખોલવા, pen drives scan કરવી, અને નિયમિત backups.</p>
""" + VW_GU,
          diagram="cn5_virus_worm"),
        T("5.2.3 Intruders", "5.2.3 Intruders",
          """<p>An <b>intruder</b> is a person who gains or tries to gain <b>unauthorised access</b> to a system or network, generally called a <b>hacker</b> (or cracker when malicious). Intruders are mostly <b>outsiders</b>.</p>
<h4>Classes of intruders</h4>
<ul><li><b>Masquerader:</b> an outsider who uses a legitimate user's account (stolen password) to get in.</li>
<li><b>Misfeasor:</b> a legitimate user who accesses data or resources he is not authorised for, or misuses his privileges (often an insider).</li>
<li><b>Clandestine user:</b> someone who seizes supervisory (administrator) control to avoid auditing and access controls.</li></ul>
<h4>By skill and intent</h4>
<ul><li><b>Script kiddies:</b> low skill; use readily available tools without understanding them. Largest group (unstructured threat).</li>
<li><b>Skilled hackers / elite:</b> can find new vulnerabilities and write their own exploits.</li>
<li><b>White hat</b> (ethical hackers, authorised penetration testers), <b>black hat</b> (malicious), <b>grey hat</b> (in between), <b>hacktivists</b> (political or social motives).</li></ul>
<h4>Typical steps of an intrusion</h4>
<p>Reconnaissance (gathering information) → scanning (ping sweeps, port scans) → gaining access (exploiting a vulnerability, password cracking) → maintaining access (backdoor) → covering tracks (deleting logs).</p>
<p><b>Defence:</b> strong passwords and MFA, firewalls, <b>Intrusion Detection / Prevention Systems (IDS / IPS)</b>, patching, monitoring logs, and honeypots.</p>""",
          """<p><b>Intruder</b> એ system કે network માં <b>અનધિકૃત access</b> મેળવનાર કે મેળવવાનો પ્રયાસ કરનાર વ્યક્તિ છે, જેને સામાન્ય રીતે <b>hacker</b> (દુષ્ટ હોય ત્યારે cracker) કહે છે. Intruders મોટે ભાગે <b>outsiders</b> હોય છે.</p>
<h4>Intruders ના વર્ગો</h4>
<ul><li><b>Masquerader:</b> અંદર આવવા કાયદેસર user ના account (ચોરાયેલો password) નો ઉપયોગ કરતો outsider.</li>
<li><b>Misfeasor:</b> કાયદેસર user જે અધિકાર ન હોય તેવા data કે resources વાપરે, કે પોતાના privileges નો દુરુપયોગ કરે (ઘણી વાર insider).</li>
<li><b>Clandestine user:</b> auditing અને access controls થી બચવા supervisory (administrator) control કબજે કરનાર.</li></ul>
<h4>કુશળતા અને ઇરાદા પ્રમાણે</h4>
<ul><li><b>Script kiddies:</b> ઓછી કુશળતા; સમજ્યા વગર સહેલાઈથી મળતાં tools વાપરે. સૌથી મોટું જૂથ (unstructured threat).</li>
<li><b>Skilled hackers / elite:</b> નવી vulnerabilities શોધી અને પોતાના exploits લખી શકે.</li>
<li><b>White hat</b> (ethical hackers, અધિકૃત penetration testers), <b>black hat</b> (દુષ્ટ), <b>grey hat</b> (વચ્ચે), <b>hacktivists</b> (રાજકીય કે સામાજિક હેતુ).</li></ul>
<h4>Intrusion નાં સામાન્ય પગલાં</h4>
<p>Reconnaissance (માહિતી ભેગી કરવી) → scanning (ping sweeps, port scans) → access મેળવવો (vulnerability નો લાભ, password cracking) → access જાળવવો (backdoor) → નિશાન ભૂંસવાં (logs delete કરવા).</p>
<p><b>બચાવ:</b> મજબૂત passwords અને MFA, firewalls, <b>Intrusion Detection / Prevention Systems (IDS / IPS)</b>, patching, logs પર નજર, અને honeypots.</p>"""),
        T("5.2.4 Insiders", "5.2.4 Insiders",
          """<p>An <b>insider</b> is a person who has <b>authorised access</b> to an organisation's systems, such as an employee, contractor, former employee or business partner, and misuses it. Insiders are often considered <b>more dangerous than outside intruders</b> because:</p>
<ul><li>They already have access and are trusted; firewalls facing the Internet do not stop them.</li>
<li>They know where valuable data is kept and what security controls exist.</li>
<li>Their actions look like normal work, so they are hard to detect.</li></ul>
<h4>Types and motives</h4>
<ul><li><b>Malicious insider:</b> deliberately steals data, sabotages systems or plants logic bombs, out of revenge (a fired employee), greed (selling data to competitors) or ideology.</li>
<li><b>Negligent / accidental insider:</b> causes harm by mistake: falling for phishing, weak passwords, losing a laptop, misconfiguring a server.</li>
<li><b>Compromised insider:</b> a genuine user whose account has been taken over by an outsider.</li></ul>
<h4>Controls</h4>
<ul><li><b>Least privilege</b> and need-to-know access; separation of duties (no single person controls a whole process).</li>
<li>Prompt removal of access when employees leave; background checks.</li>
<li>Monitoring and audit logs, data loss prevention (DLP), security awareness training.</li></ul>""",
          """<p><b>Insider</b> એ સંસ્થાની systems માં <b>અધિકૃત access</b> ધરાવતી વ્યક્તિ છે, જેમ કે employee, contractor, ભૂતપૂર્વ employee કે business partner, જે તેનો દુરુપયોગ કરે. Insiders ને ઘણી વાર <b>બહારના intruders કરતાં વધુ ખતરનાક</b> ગણાય છે કારણ કે:</p>
<ul><li>તેમની પાસે પહેલેથી access છે અને તેઓ વિશ્વાસપાત્ર છે; Internet તરફના firewalls તેમને અટકાવતા નથી.</li>
<li>કિંમતી data ક્યાં રાખેલો છે અને કયાં security controls છે તે તેઓ જાણે છે.</li>
<li>તેમની ક્રિયાઓ સામાન્ય કામ જેવી દેખાય, તેથી પકડવી મુશ્કેલ.</li></ul>
<h4>પ્રકારો અને હેતુઓ</h4>
<ul><li><b>Malicious insider:</b> બદલો (છૂટો કરાયેલો employee), લોભ (competitors ને data વેચવો) કે વિચારધારાને કારણે ઇરાદાપૂર્વક data ચોરે, systems ને નુકસાન કરે કે logic bombs મૂકે.</li>
<li><b>Negligent / accidental insider:</b> ભૂલથી નુકસાન કરે: phishing માં ફસાવું, નબળા passwords, laptop ખોવો, server ખોટી રીતે configure કરવું.</li>
<li><b>Compromised insider:</b> સાચો user જેનું account outsider એ કબજે કર્યું હોય.</li></ul>
<h4>Controls</h4>
<ul><li><b>Least privilege</b> અને need-to-know access; separation of duties (એક જ વ્યક્તિ આખી પ્રક્રિયા નિયંત્રિત ન કરે).</li>
<li>Employees છોડે ત્યારે તરત access દૂર કરવો; background checks.</li>
<li>Monitoring અને audit logs, data loss prevention (DLP), security awareness training.</li></ul>"""),
        T("5.2.5 Criminal Organizations", "5.2.5 Criminal Organizations",
          """<p>As business and banking moved online, <b>organised crime groups</b> moved into cybercrime because it is profitable, low-risk and can be done from anywhere in the world. They are a <b>structured threat</b>: they have money to hire skilled hackers, buy tools and spend months on an attack.</p>
<h4>Activities</h4>
<ul><li><b>Financial fraud:</b> stealing card details and banking passwords, fake UPI / KYC calls, online shopping scams.</li>
<li><b>Ransomware</b> attacks on companies and hospitals, demanding payment in cryptocurrency.</li>
<li><b>Phishing</b> campaigns and fake websites; identity theft.</li>
<li>Running <b>botnets</b> and renting them out for DDoS or spam; selling stolen data on the dark web.</li>
<li>Extortion: threatening DDoS or publishing stolen data unless paid.</li></ul>
<h4>Characteristics</h4>
<p>Profit is the main motive. Groups are well organised like businesses (developers, distributors, money-launderers), often cross international borders, and use encryption and cryptocurrency to hide.</p>
<p><b>Defence:</b> strong authentication (OTP, MFA), user awareness, fraud monitoring by banks, backups against ransomware, and reporting to the cyber-crime cell (cybercrime.gov.in, helpline 1930 in India).</p>""",
          """<p>વ્યવસાય અને banking online થતાં, <b>organised crime groups</b> cybercrime તરફ વળ્યાં કારણ કે તે નફાકારક, ઓછું જોખમી અને દુનિયામાં ગમે ત્યાંથી થઈ શકે છે. તેઓ <b>structured threat</b> છે: કુશળ hackers રાખવા, tools ખરીદવા અને attack પર મહિનાઓ ખર્ચવા તેમની પાસે પૈસા છે.</p>
<h4>પ્રવૃત્તિઓ</h4>
<ul><li><b>Financial fraud:</b> card details અને banking passwords ચોરવા, નકલી UPI / KYC calls, online shopping scams.</li>
<li>Companies અને hospitals પર <b>ransomware</b> attacks, cryptocurrency માં ચુકવણી માગવી.</li>
<li><b>Phishing</b> campaigns અને નકલી websites; identity theft.</li>
<li><b>Botnets</b> ચલાવવાં અને DDoS કે spam માટે ભાડે આપવાં; ચોરાયેલો data dark web પર વેચવો.</li>
<li>Extortion: પૈસા ન મળે તો DDoS કે ચોરાયેલો data જાહેર કરવાની ધમકી.</li></ul>
<h4>લાક્ષણિકતાઓ</h4>
<p>નફો મુખ્ય હેતુ છે. જૂથો વ્યવસાયની જેમ સુવ્યવસ્થિત હોય (developers, distributors, money-launderers), ઘણી વાર આંતરરાષ્ટ્રીય સરહદો પાર કરે, અને છુપાવા encryption અને cryptocurrency વાપરે.</p>
<p><b>બચાવ:</b> મજબૂત authentication (OTP, MFA), user જાગૃતિ, banks દ્વારા fraud monitoring, ransomware સામે backups, અને cyber-crime cell ને report કરવું (ભારતમાં cybercrime.gov.in, helpline 1930).</p>"""),
        T("5.2.6 Terrorists", "5.2.6 Terrorists",
          """<p><b>Terrorist groups</b> may use computers and networks to cause fear, disruption and damage for political or ideological goals. Attacks on computer systems by terrorists are called <b>cyber terrorism</b>. They are a <b>highly structured threat</b> when well funded.</p>
<h4>How terrorists use networks</h4>
<ul><li><b>Attacking critical infrastructure:</b> power grids, water supply, transport, telecommunication, banking and hospital systems controlled by computers (SCADA / industrial control systems). Disabling them can harm many people.</li>
<li><b>Propaganda and recruitment</b> through websites and social media; spreading fake news and panic.</li>
<li><b>Communication and planning</b> using encrypted messaging; raising funds through cybercrime.</li>
<li>Defacing government websites and stealing sensitive data.</li></ul>
<p>Unlike criminals, the main motive is not money but <b>publicity, fear and disruption</b>.</p>
<p><b>Defence:</b> strong protection and isolation of critical infrastructure networks, national agencies (CERT-In, NCIIPC in India), monitoring, cooperation between countries, and laws such as Section 66F of the IT Act (cyber terrorism).</p>""",
          """<p><b>Terrorist groups</b> રાજકીય કે વૈચારિક ધ્યેયો માટે ભય, વિક્ષેપ અને નુકસાન ફેલાવવા computers અને networks વાપરી શકે. Terrorists દ્વારા computer systems પરના attacks ને <b>cyber terrorism</b> કહે છે. સારું ભંડોળ હોય ત્યારે તેઓ <b>highly structured threat</b> છે.</p>
<h4>Terrorists networks કેવી રીતે વાપરે</h4>
<ul><li><b>Critical infrastructure પર attack:</b> computers થી નિયંત્રિત power grids, પાણી પુરવઠો, transport, telecommunication, banking અને hospital systems (SCADA / industrial control systems). તેમને બંધ કરવાથી ઘણા લોકોને નુકસાન થઈ શકે.</li>
<li>Websites અને social media દ્વારા <b>propaganda અને recruitment</b>; fake news અને ગભરાટ ફેલાવવો.</li>
<li>Encrypted messaging વાપરી <b>communication અને planning</b>; cybercrime દ્વારા ભંડોળ ભેગું કરવું.</li>
<li>સરકારી websites deface કરવી અને સંવેદનશીલ data ચોરવો.</li></ul>
<p>Criminals થી વિપરીત, મુખ્ય હેતુ પૈસા નહીં પણ <b>પ્રસિદ્ધિ, ભય અને વિક્ષેપ</b> છે.</p>
<p><b>બચાવ:</b> critical infrastructure networks નું મજબૂત રક્ષણ અને અલગીકરણ, રાષ્ટ્રીય agencies (ભારતમાં CERT-In, NCIIPC), monitoring, દેશો વચ્ચે સહકાર, અને IT Act ની Section 66F (cyber terrorism) જેવા કાયદા.</p>"""),
        T("5.2.7 Information Warfare", "5.2.7 Information Warfare",
          """<p><b>Information warfare</b> is the use of information and computer networks by a <b>nation (state)</b> to gain an advantage over an adversary, by attacking the enemy's information systems while defending its own. It is the <b>most highly structured threat</b>: nations have huge budgets, the best experts, and years of time.</p>
<h4>Offensive and defensive sides</h4>
<ul><li><b>Offensive:</b> cyber espionage (stealing military, political and industrial secrets), disabling the enemy's communication, power and financial systems before or during a conflict, planting malware in advance.</li>
<li><b>Defensive:</b> protecting one's own military and civilian critical infrastructure from such attacks.</li></ul>
<h4>Forms</h4>
<ul><li>Attacks on command-and-control and communication networks.</li><li>Sabotage of infrastructure: e.g. the <b>Stuxnet</b> worm (around 2010) damaged uranium centrifuges by attacking industrial controllers; attacks on Ukraine's power grid (2015).</li>
<li><b>Psychological operations:</b> misinformation and propaganda through media and social networks to influence public opinion or elections.</li>
<li><b>Advanced Persistent Threats (APT):</b> long-term, stealthy intrusions sponsored by states.</li></ul>
<p>Modern militaries treat cyberspace as a fifth domain of warfare after land, sea, air and space, and maintain dedicated cyber commands.</p>""",
          """<p><b>Information warfare</b> એટલે <b>દેશ (state)</b> દ્વારા શત્રુ પર લાભ મેળવવા માહિતી અને computer networks નો ઉપયોગ, શત્રુની information systems પર attack કરીને અને પોતાની systems નો બચાવ કરીને. તે <b>સૌથી highly structured threat</b> છે: દેશો પાસે વિશાળ budgets, શ્રેષ્ઠ નિષ્ણાતો અને વર્ષોનો સમય હોય.</p>
<h4>Offensive અને defensive બાજુ</h4>
<ul><li><b>Offensive:</b> cyber espionage (લશ્કરી, રાજકીય અને ઔદ્યોગિક રહસ્યો ચોરવાં), સંઘર્ષ પહેલાં કે દરમિયાન શત્રુની communication, power અને financial systems બંધ કરવી, અગાઉથી malware મૂકવો.</li>
<li><b>Defensive:</b> પોતાના લશ્કરી અને નાગરિક critical infrastructure ને આવા attacks થી બચાવવું.</li></ul>
<h4>સ્વરૂપો</h4>
<ul><li>Command-and-control અને communication networks પર attacks.</li><li>Infrastructure ની તોડફોડ: દા.ત. <b>Stuxnet</b> worm (લગભગ 2010) એ industrial controllers પર attack કરી uranium centrifuges ને નુકસાન કર્યું; Ukraine ના power grid પર attacks (2015).</li>
<li><b>Psychological operations:</b> જાહેર અભિપ્રાય કે ચૂંટણીઓને પ્રભાવિત કરવા media અને social networks દ્વારા ખોટી માહિતી અને propaganda.</li>
<li><b>Advanced Persistent Threats (APT):</b> દેશો દ્વારા પ્રાયોજિત લાંબા ગાળાના, છુપા intrusions.</li></ul>
<p>આધુનિક લશ્કરો cyberspace ને જમીન, સમુદ્ર, હવા અને અવકાશ પછી યુદ્ધનું પાંચમું ક્ષેત્ર ગણે છે અને અલગ cyber commands રાખે છે.</p>"""),
    ]}

from content_DI03000051_u5_notes_b import SEC_5_3  # noqa: E402

NOTES = [SEC_5_1, SEC_5_2, SEC_5_3]
