"""Computer Networks (DI03000051) - Unit 5 extras: solved examples (computed), formulas, viva, exam questions."""
import hashlib
import ipaddress
from content_DI03000011_u1_extras import N, E, V, X
from content_DI03000041_u1_notes import tbl


# n1: Caesar cipher
def caesar(s, k):
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s.upper())


P1, K1, C2 = "NETWORK", 3, "KHOOR"
enc = caesar(P1, K1)
dec = caesar(C2, -K1)


def n1_body(lang):
    rows = [(p, str(ord(p) - 65), f"({ord(p) - 65} + 3) mod 26 = {(ord(p) - 65 + 3) % 26}", c) for p, c in zip(P1, enc)]
    head = ["Plain", "Position", "Shift by key 3", "Cipher"] if lang == "en" else ["Plain", "સ્થાન", "Key 3 થી shift", "Cipher"]
    s = ("<p>Number letters A = 0 ... Z = 25. Encryption: C = (P + k) mod 26. Decryption: P = (C - k) mod 26.</p>" if lang == "en" else
         "<p>અક્ષરોને ક્રમાંક આપો A = 0 ... Z = 25. Encryption: C = (P + k) mod 26. Decryption: P = (C - k) mod 26.</p>")
    s += tbl(head, rows)
    s += f"<p>(a) {P1} → <b>{enc}</b></p>"
    s += f"<p>(b) {C2}: " + ", ".join(f"{c}→{p}" for c, p in zip(C2, dec)) + f" → <b>{dec}</b></p>"
    s += ("<p>Only someone who knows the key (3) can read it: this is <b>confidentiality</b>. The Caesar cipher is weak because only 25 keys exist (brute force); modern systems use AES with 128-256 bit keys.</p>" if lang == "en" else
          "<p>ફક્ત key (3) જાણનાર જ વાંચી શકે: આ <b>confidentiality</b> છે. Caesar cipher નબળો છે કારણ કે ફક્ત 25 keys છે (brute force); આધુનિક systems 128-256 bit keys વાળું AES વાપરે.</p>")
    return s


n1 = N("cn5n1", f"Using the Caesar cipher with key = {K1}, (a) encrypt the plaintext {P1}, (b) decrypt the ciphertext {C2}.",
       f"Key = {K1} સાથે Caesar cipher વાપરી, (a) plaintext {P1} ને encrypt કરો, (b) ciphertext {C2} ને decrypt કરો.",
       n1_body("en"), n1_body("gu"))

# n2: hash integrity
m_a, m_b = "Pay Rs 100", "Pay Rs 900"
h_a = hashlib.sha256(m_a.encode()).hexdigest()
h_b = hashlib.sha256(m_b.encode()).hexdigest()
diff = sum(1 for x, y in zip(h_a, h_b) if x != y)


def n2_body(lang):
    s = (f"<p>SHA-256 gives a 256-bit (64 hex digit) digest. First 16 hex digits:</p><ul>"
         f"<li>SHA-256(\"{m_a}\") = <b>{h_a[:16]}...</b></li><li>SHA-256(\"{m_b}\") = <b>{h_b[:16]}...</b></li></ul>")
    if lang == "en":
        s += (f"<p>Only one character of the message changed, but <b>{diff} of the 64</b> hex digits of the hash are different (avalanche effect).</p>"
              f"<p>The receiver recomputes the hash of the message received. If an attacker changed 100 to 900, the new hash will not match the hash sent, so the change is <b>detected</b>: integrity is checked. To stop the attacker from also replacing the hash, a keyed hash (HMAC) or digital signature is used.</p>")
    else:
        s += (f"<p>Message નો ફક્ત એક અક્ષર બદલાયો, પણ hash ના 64 માંથી <b>{diff}</b> hex અંકો અલગ છે (avalanche effect).</p>"
              f"<p>Receiver મળેલા message નો hash ફરી ગણે. જો attacker એ 100 ને 900 કર્યું હોય, તો નવો hash મોકલેલા hash સાથે મેળ નહીં ખાય, તેથી ફેરફાર <b>પકડાય</b>: integrity તપાસાય. Attacker hash પણ ન બદલી શકે તે માટે keyed hash (HMAC) કે digital signature વપરાય.</p>")
    return s


n2 = N("cn5n2", f"Show how a hash function detects a change in a message: compare the SHA-256 hashes of \"{m_a}\" and \"{m_b}\".",
       f"Hash function message માં ફેરફાર કેવી રીતે પકડે તે બતાવો: \"{m_a}\" અને \"{m_b}\" ના SHA-256 hashes સરખાવો.",
       n2_body("en"), n2_body("gu"))

# n3: availability downtime
HOURS = 365 * 24
levels = [99.0, 99.9, 99.99, 99.999]


def fmt_time(h, lang):
    if h >= 1:
        return f"{h:.2f} h" + (f" ({h / 24:.2f} days)" if h >= 24 else "")
    m = h * 60
    return f"{m:.2f} min" if m >= 1 else f"{m * 60:.1f} s"


def n3_body(lang):
    head = ["Availability", "Downtime fraction", "Downtime per year"] if lang == "en" else ["Availability", "Downtime ભાગ", "વર્ષ દીઠ downtime"]
    rows = [(f"{a:g}%", f"{(100 - a) / 100:.5f}".rstrip("0"), fmt_time(HOURS * (100 - a) / 100, lang)) for a in levels]
    s = ("<p>Hours in a year = 365 × 24 = 8,760 h. Downtime = (1 - availability) × 8,760 h.</p>" if lang == "en" else
         "<p>વર્ષમાં કલાકો = 365 × 24 = 8,760 h. Downtime = (1 - availability) × 8,760 h.</p>")
    s += f"<p>e.g. 99.9%: (1 - 0.999) × 8,760 = 0.001 × 8,760 = <b>{HOURS * 0.001:.2f} h</b></p>"
    s += tbl(head, rows)
    s += ("<p>Each extra \"nine\" cuts downtime by 10 times; achieving it needs redundancy, backups and DoS protection.</p>" if lang == "en" else
          "<p>દરેક વધારાનો \"nine\" downtime 10 ગણો ઘટાડે; તે મેળવવા redundancy, backups અને DoS protection જોઈએ.</p>")
    return s


n3 = N("cn5n3", "A server must be available 99%, 99.9%, 99.99% and 99.999% of the time. Find the maximum allowed downtime per year in each case.",
       "Server 99%, 99.9%, 99.99% અને 99.999% સમય ઉપલબ્ધ હોવું જોઈએ. દરેક કિસ્સામાં વર્ષ દીઠ મહત્તમ માન્ય downtime શોધો.",
       n3_body("en"), n3_body("gu"))

# n4: packet filter rule evaluation (same rule table as diagram cn5_pfilter)
RULES = [("1", "any", "192.168.1.10", "tcp", {80, 443}, "Allow"), ("2", "any", "192.168.1.11", "tcp", {25}, "Allow"),
         ("3", "192.168.1.0/24", "any", "any", None, "Allow"), ("4", "any", "any", "tcp", {23}, "Deny"), ("5", "any", "any", "any", None, "Deny")]
PKTS = [("45.10.2.7", "192.168.1.10", "tcp", 443), ("45.10.2.7", "192.168.1.10", "tcp", 23), ("192.168.1.25", "142.250.1.1", "tcp", 23),
        ("103.5.6.7", "192.168.1.11", "tcp", 25), ("103.5.6.7", "192.168.1.20", "udp", 53)]


def m_ip(rule, a):
    return rule == "any" or ipaddress.ip_address(a) in ipaddress.ip_network(rule, strict=False)


def decide(p, rules=RULES):
    src, dst, proto, port = p
    for num, rs, rd, rp, ports, act in rules:
        if m_ip(rs, src) and m_ip(rd, dst) and (rp == "any" or rp == proto) and (ports is None or port in ports):
            return num, act


def n4_body(lang):
    rt = tbl(["#", "Source", "Destination", "Protocol / port", "Action"],
             [(n, s, d, (p.upper() + " " + ", ".join(map(str, sorted(pt)))) if pt else "any", a) for n, s, d, p, pt, a in RULES])
    head = ["Packet", "Src → Dst, port", "First match", "Result"] if lang == "en" else ["Packet", "Src → Dst, port", "પ્રથમ match", "પરિણામ"]
    rows = []
    for i, p in enumerate(PKTS):
        num, act = decide(p)
        rows.append((f"P{i + 1}", f"{p[0]} → {p[1]}, {p[2].upper()} {p[3]}", f"Rule {num}", act))
    swapped = [RULES[0], RULES[1], RULES[3], RULES[2], RULES[4]]
    n3_, a3 = decide(PKTS[2], swapped)
    if lang == "en":
        s = "<p>Rule table (checked top to bottom, first match wins):</p>" + rt + tbl(head, rows)
        s += (f"<p><b>Note on P3:</b> an inside host using Telnet (port 23) is <b>allowed</b> because rule 3 (allow inside hosts) matches before rule 4. "
              f"If rules 3 and 4 are swapped, P3 matches rule 4 first and is <b>{'denied' if a3 == 'Deny' else 'allowed'}</b>. Rule order matters.</p>")
    else:
        s = "<p>Rule table (ઉપરથી નીચે તપાસાય, પ્રથમ match જીતે):</p>" + rt + tbl(head, rows)
        s += (f"<p><b>P3 પર નોંધ:</b> Telnet (port 23) વાપરતો અંદરનો host <b>allowed</b> છે કારણ કે rule 3 (અંદરના hosts ને મંજૂરી) rule 4 પહેલાં match થાય. "
              f"Rules 3 અને 4 અદલબદલ કરો, તો P3 પહેલાં rule 4 સાથે match થઈ <b>{a3.lower()}</b> થાય. Rules નો ક્રમ મહત્વનો છે.</p>")
    return s


n4 = N("cn5n4", "A packet filter firewall has the rule table shown (rules 1-5). Decide whether each packet is allowed or denied: P1 45.10.2.7 → 192.168.1.10 TCP 443; P2 45.10.2.7 → 192.168.1.10 TCP 23; P3 192.168.1.25 → 142.250.1.1 TCP 23; P4 103.5.6.7 → 192.168.1.11 TCP 25; P5 103.5.6.7 → 192.168.1.20 UDP 53.",
       "Packet filter firewall નું rule table (rules 1-5) આપેલું છે. દરેક packet allowed છે કે denied તે નક્કી કરો: P1 45.10.2.7 → 192.168.1.10 TCP 443; P2 45.10.2.7 → 192.168.1.10 TCP 23; P3 192.168.1.25 → 142.250.1.1 TCP 23; P4 103.5.6.7 → 192.168.1.11 TCP 25; P5 103.5.6.7 → 192.168.1.20 UDP 53.",
       n4_body("en"), n4_body("gu"))

NUMERICALS = [n1, n2, n3, n4]

EQUATIONS = [
    {"title": {"en": "Security formulas", "gu": "Security formulas"}, "items": [
        E("Caesar cipher", "Caesar cipher", "C = (P + k) mod 26,   P = (C - k) mod 26", "A = 0 ... Z = 25; k = key (shift)", "A = 0 ... Z = 25; k = key (shift)"),
        E("Availability", "Availability", "A = uptime / (uptime + downtime) × 100%", "Also MTBF / (MTBF + MTTR)", "MTBF / (MTBF + MTTR) પણ"),
        E("Downtime per year", "વર્ષ દીઠ downtime", "Downtime = (1 - A) × 8,760 h", "99.9% → 8.76 h per year", "99.9% → વર્ષે 8.76 h"),
        E("Brute-force key space", "Brute-force key space", "Keys = 2^n  (n-bit key)", "AES-128: 2^128 keys; Caesar: only 25", "AES-128: 2^128 keys; Caesar: ફક્ત 25"),
        E("Hash output sizes", "Hash output sizes", "MD5 = 128 bits,  SHA-1 = 160 bits,  SHA-256 = 256 bits", "Fixed size for any input length", "કોઈ પણ input length માટે fixed size"),
    ]},
    {"title": {"en": "Common ports for firewall rules", "gu": "Firewall rules માટે સામાન્ય ports"}, "items": [
        E("Well-known ports", "Well-known ports", "FTP 20/21,  SSH 22,  Telnet 23,  SMTP 25,  DNS 53,  HTTP 80,  HTTPS 443", "Rules block or allow services by port number", "Rules port number થી services block કે allow કરે"),
    ]},
]

VIVA = [
    {"title": {"en": "Security basics", "gu": "Security basics"}, "items": [
        V("What is the CIA triad?", "CIA triad એટલે શું?", "Confidentiality, Integrity and Availability: the three basic goals of information security.", "Confidentiality, Integrity અને Availability: information security ના ત્રણ મૂળભૂત ધ્યેયો."),
        V("Which mechanism provides confidentiality?", "કયું mechanism confidentiality આપે?", "Encryption, along with access control (passwords, permissions).", "Encryption, access control (passwords, permissions) સાથે."),
        V("How is integrity checked?", "Integrity કેવી રીતે તપાસાય?", "With hash functions (SHA-256), MAC or digital signatures; a changed message gives a different hash.", "Hash functions (SHA-256), MAC કે digital signatures થી; બદલાયેલો message અલગ hash આપે."),
        V("Give an example of an attack on availability.", "Availability પરના attack નું ઉદાહરણ આપો.", "Denial of Service (DoS / DDoS) flooding a server so genuine users cannot use it.", "Denial of Service (DoS / DDoS) server ને ભરી દે જેથી સાચા users તેને વાપરી ન શકે."),
        V("Difference between passive and active attack?", "Passive અને active attack વચ્ચે તફાવત?", "Passive only reads data (eavesdropping); active modifies, blocks or fakes data (DoS, spoofing).", "Passive ફક્ત data વાંચે (eavesdropping); active data બદલે, અટકાવે કે નકલી બનાવે (DoS, spoofing)."),
        V("What is the difference between a threat and a vulnerability?", "Threat અને vulnerability વચ્ચે તફાવત?", "A vulnerability is a weakness; a threat is something that may exploit that weakness.", "Vulnerability એ નબળાઈ છે; threat એ તે નબળાઈનો લાભ લઈ શકે તેવી વસ્તુ છે."),
    ]},
    {"title": {"en": "Threats", "gu": "Threats"}, "items": [
        V("Difference between a virus and a worm?", "Virus અને worm વચ્ચે તફાવત?", "A virus attaches to a host file and needs user action; a worm is standalone and spreads over the network by itself.", "Virus host file સાથે જોડાય અને user ક્રિયા માગે; worm સ્વતંત્ર છે અને network પર જાતે ફેલાય."),
        V("What is a Trojan horse?", "Trojan horse એટલે શું?", "A program that looks useful but secretly performs malicious actions; it does not replicate.", "ઉપયોગી દેખાતો પણ ગુપ્ત રીતે દુષ્ટ ક્રિયા કરતો program; તે નકલો બનાવતો નથી."),
        V("Who is an intruder?", "Intruder કોણ છે?", "A person, usually an outsider, who gains unauthorised access to a system, e.g. a hacker or masquerader.", "System માં અનધિકૃત access મેળવનાર વ્યક્તિ, સામાન્ય રીતે outsider, દા.ત. hacker કે masquerader."),
        V("Why are insiders dangerous?", "Insiders શા માટે ખતરનાક છે?", "They already have trusted access and know the systems, and their actions look like normal work.", "તેમની પાસે પહેલેથી વિશ્વાસપાત્ર access છે અને systems જાણે છે, અને તેમની ક્રિયાઓ સામાન્ય કામ જેવી દેખાય."),
        V("What is the main motive of criminal organisations?", "Criminal organisations નો મુખ્ય હેતુ શું?", "Financial profit: fraud, ransomware, selling stolen data.", "આર્થિક નફો: fraud, ransomware, ચોરાયેલો data વેચવો."),
        V("What is information warfare?", "Information warfare એટલે શું?", "Use of cyber attacks and information by nations against other nations, e.g. espionage and attacks on infrastructure (Stuxnet).", "દેશો દ્વારા બીજા દેશો સામે cyber attacks અને માહિતીનો ઉપયોગ, દા.ત. espionage અને infrastructure પર attacks (Stuxnet)."),
        V("What is a script kiddie?", "Script kiddie એટલે શું?", "An unskilled attacker who uses ready-made hacking tools without understanding them.", "તૈયાર hacking tools સમજ્યા વગર વાપરતો અકુશળ attacker."),
    ]},
    {"title": {"en": "Firewalls", "gu": "Firewalls"}, "items": [
        V("What is a firewall?", "Firewall એટલે શું?", "A hardware or software system that filters traffic between a trusted and an untrusted network according to rules.", "Rules મુજબ trusted અને untrusted network વચ્ચે traffic filter કરતી hardware કે software system."),
        V("What does a packet filter check?", "Packet filter શું તપાસે?", "Header fields: source / destination IP, protocol and source / destination port.", "Header fields: source / destination IP, protocol અને source / destination port."),
        V("At which layer does a proxy firewall work?", "Proxy firewall કયા layer પર કામ કરે?", "The application layer (layer 7).", "Application layer (layer 7)."),
        V("What is a DMZ?", "DMZ એટલે શું?", "A separate network zone between two firewalls for public servers such as web and mail servers.", "Web અને mail servers જેવા public servers માટે બે firewalls વચ્ચેનો અલગ network zone."),
        V("What is the default deny policy?", "Default deny policy એટલે શું?", "Everything is blocked unless a rule explicitly allows it.", "Rule સ્પષ્ટ રીતે મંજૂર ન કરે ત્યાં સુધી બધું block."),
        V("What is a stateful firewall?", "Stateful firewall એટલે શું?", "A firewall that tracks active connections in a state table and allows only packets belonging to valid connections.", "સક્રિય connections ને state table માં track કરી ફક્ત માન્ય connections નાં packets મંજૂર કરતું firewall."),
    ]},
    {"title": {"en": "Network commands (Practicals 10, 11)", "gu": "Network commands (Practicals 10, 11)"}, "items": [
        V("What does ipconfig show?", "ipconfig શું બતાવે?", "IP address, subnet mask and default gateway of each adapter; ipconfig /all also shows MAC address, DHCP and DNS servers.", "દરેક adapter નું IP address, subnet mask અને default gateway; ipconfig /all MAC address, DHCP અને DNS servers પણ બતાવે."),
        V("What is ping used for?", "ping શા માટે વપરાય?", "To test reachability of a host using ICMP echo request / reply, and measure round-trip time.", "ICMP echo request / reply વાપરી host સુધી પહોંચી શકાય છે કે નહીં તે ચકાસવા અને round-trip time માપવા."),
        V("What does tracert do?", "tracert શું કરે?", "Shows the list of routers (hops) a packet passes through to reach the destination, using increasing TTL values.", "વધતા TTL values વાપરી destination સુધી પહોંચતાં packet જે routers (hops) માંથી પસાર થાય તેની યાદી બતાવે."),
        V("What does netstat show?", "netstat શું બતાવે?", "Active TCP connections, listening ports and network statistics (netstat -an).", "સક્રિય TCP connections, listening ports અને network statistics (netstat -an)."),
        V("What is pathping?", "pathping એટલે શું?", "A Windows command that combines ping and tracert, showing packet loss at each hop.", "ping અને tracert ને જોડતો Windows command, દરેક hop પર packet loss બતાવે."),
        V("What does route print show?", "route print શું બતાવે?", "The computer's IP routing table, including the default route 0.0.0.0.", "Computer નું IP routing table, default route 0.0.0.0 સહિત."),
        V("How do you set a static IP in Windows?", "Windows માં static IP કેવી રીતે set કરાય?", "Network Connections (ncpa.cpl) → adapter Properties → IPv4 → Use the following IP address: enter IP, mask, gateway and DNS.", "Network Connections (ncpa.cpl) → adapter Properties → IPv4 → Use the following IP address: IP, mask, gateway અને DNS લખો."),
    ]},
]

EXAM_QS = [
    X("Explain the CIA triad with a diagram.", "આકૃતિ સાથે CIA triad સમજાવો.", 4),
    X("Explain confidentiality, integrity and availability with mechanisms for each.", "Confidentiality, integrity અને availability દરેકના mechanisms સાથે સમજાવો.", 7),
    X("Explain types of security attacks: interruption, interception, modification and fabrication.", "Security attacks ના પ્રકારો સમજાવો: interruption, interception, modification અને fabrication.", 4),
    X("Differentiate passive and active attacks.", "Passive અને active attacks નો તફાવત આપો.", 3),
    X("Differentiate virus and worm.", "Virus અને worm નો તફાવત આપો.", 3),
    X("Explain viruses and worms with examples.", "ઉદાહરણો સાથે viruses અને worms સમજાવો.", 4),
    X("Write a short note on intruders.", "Intruders પર ટૂંકનોંધ લખો.", 3),
    X("Explain insiders as a threat to security.", "Security માટે ખતરા તરીકે insiders સમજાવો.", 3),
    X("Explain criminal organisations, terrorists and information warfare as security threats.", "Security threats તરીકે criminal organisations, terrorists અને information warfare સમજાવો.", 7),
    X("What is a firewall? Explain its working.", "Firewall એટલે શું? તેની કાર્યપદ્ધતિ સમજાવો.", 4),
    X("Explain the design principles of a firewall.", "Firewall ના design principles સમજાવો.", 4),
    X("Explain the packet filter firewall with its advantages and disadvantages.", "Packet filter firewall તેના ફાયદા અને ગેરફાયદા સાથે સમજાવો.", 4),
    X("Explain the proxy firewall with a diagram.", "આકૃતિ સાથે proxy firewall સમજાવો.", 4),
    X("Differentiate packet filter firewall and proxy firewall.", "Packet filter firewall અને proxy firewall નો તફાવત આપો.", 3),
    X("List types of firewalls and the OSI layer at which each works.", "Firewalls ના પ્રકારો અને દરેક કયા OSI layer પર કામ કરે તેની યાદી આપો.", 3),
]
