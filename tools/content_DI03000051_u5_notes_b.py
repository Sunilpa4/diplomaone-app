"""Computer Networks (DI03000051) - Unit 5 notes part B: 5.3 Firewalls."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

TYPES_EN = tbl(["Type", "OSI layer", "What it checks", "Example"], [
    ("Packet filter (stateless)", "3-4", "IP addresses, protocol, ports of each packet", "Router ACL"),
    ("Stateful inspection", "3-4", "Packet + connection state table", "Windows Defender Firewall"),
    ("Circuit-level gateway", "5", "TCP handshake / session validity", "SOCKS proxy"),
    ("Application proxy", "7", "Full content, commands, users", "Squid web proxy"),
    ("Next-generation (NGFW)", "3-7", "All above + IPS, app awareness", "FortiGate, Palo Alto")])
TYPES_GU = tbl(["પ્રકાર", "OSI layer", "શું તપાસે", "ઉદાહરણ"], [
    ("Packet filter (stateless)", "3-4", "દરેક packet ના IP addresses, protocol, ports", "Router ACL"),
    ("Stateful inspection", "3-4", "Packet + connection state table", "Windows Defender Firewall"),
    ("Circuit-level gateway", "5", "TCP handshake / session ની માન્યતા", "SOCKS proxy"),
    ("Application proxy", "7", "સંપૂર્ણ content, commands, users", "Squid web proxy"),
    ("Next-generation (NGFW)", "3-7", "ઉપરનાં બધાં + IPS, app awareness", "FortiGate, Palo Alto")])

CMP_EN = tbl(["Packet filter firewall", "Proxy firewall"], [
    ("Works at network / transport layer (3-4)", "Works at application layer (7)"),
    ("Checks only header: IP, port, protocol", "Checks full content and application commands"),
    ("Direct connection between client and server", "Two separate connections via the proxy"),
    ("Fast, low cost, transparent to users", "Slower, costlier, may need client settings"),
    ("Cannot authenticate users or filter content", "Can authenticate users, filter URLs and viruses"),
    ("Vulnerable to IP spoofing; less logging", "Hides internal addresses; detailed logs, caching"),
    ("One device protects all services", "Separate proxy needed for each service")])
CMP_GU = tbl(["Packet filter firewall", "Proxy firewall"], [
    ("Network / transport layer (3-4) પર કામ કરે", "Application layer (7) પર કામ કરે"),
    ("ફક્ત header તપાસે: IP, port, protocol", "સંપૂર્ણ content અને application commands તપાસે"),
    ("Client અને server વચ્ચે સીધું connection", "Proxy મારફતે બે અલગ connections"),
    ("ઝડપી, ઓછો ખર્ચ, users માટે transparent", "ધીમું, મોંઘું, client settings જોઈ શકે"),
    ("Users authenticate કે content filter ન કરી શકે", "Users authenticate, URLs અને viruses filter કરી શકે"),
    ("IP spoofing સામે નબળું; ઓછું logging", "અંદરના addresses છુપાવે; વિગતવાર logs, caching"),
    ("એક device બધી services બચાવે", "દરેક service માટે અલગ proxy જોઈએ")])

PF_AD = adv(["Simple and fast; little effect on network performance.", "Low cost: built into most routers and operating systems.", "Transparent to users; no client configuration.", "One filter can protect a whole network."],
            ["Cannot inspect data (payload): viruses and malicious commands pass through allowed ports.", "No user authentication; decisions only on addresses and ports.",
             "Vulnerable to IP address spoofing and fragmentation attacks.", "Large rule sets are hard to write and test; a wrong rule order opens holes. Limited logging."],
            ["સરળ અને ઝડપી; network performance પર ઓછી અસર.", "ઓછો ખર્ચ: મોટા ભાગનાં routers અને operating systems માં built in.", "Users માટે transparent; client configuration નહીં.", "એક filter આખું network બચાવી શકે."],
            ["Data (payload) તપાસી ન શકે: viruses અને દુષ્ટ commands મંજૂર ports માંથી પસાર થાય.", "User authentication નહીં; નિર્ણયો ફક્ત addresses અને ports પર.",
             "IP address spoofing અને fragmentation attacks સામે નબળું.", "મોટા rule sets લખવા અને ચકાસવા મુશ્કેલ; ખોટો rule ક્રમ છિદ્રો ખોલે. મર્યાદિત logging."])
PX_AD = adv(["Highest security: understands the application protocol and inspects content.", "Can authenticate users and apply per-user rules.",
             "Hides internal network addresses; no direct outside connection to internal hosts.", "Detailed logging and auditing; caching speeds up repeated web requests."],
            ["Slower: every connection is handled twice and content is processed.", "A separate proxy program is needed for each service (HTTP, FTP, SMTP).",
             "Higher cost and processing power; may need client configuration.", "Single point of failure / bottleneck if overloaded."],
            ["સૌથી વધુ security: application protocol સમજે અને content તપાસે.", "Users authenticate કરી શકે અને user દીઠ rules લાગુ કરી શકે.",
             "અંદરના network addresses છુપાવે; અંદરના hosts સાથે બહારનું સીધું connection નહીં.", "વિગતવાર logging અને auditing; caching વારંવારની web requests ઝડપી બનાવે."],
            ["ધીમું: દરેક connection બે વાર સંભાળાય અને content process થાય.", "દરેક service (HTTP, FTP, SMTP) માટે અલગ proxy program જોઈએ.",
             "વધુ ખર્ચ અને processing power; client configuration જોઈ શકે.", "Overload થાય તો single point of failure / bottleneck."])

SEC_5_3 = {
    "title": {"en": "5.3 Firewalls", "gu": "5.3 Firewalls"},
    "items": [
        T("5.3.1 Firewall: Introduction and Working", "5.3.1 Firewall: પરિચય અને કાર્યપદ્ધતિ",
          """<p>A <b>firewall</b> is a hardware device or software program placed between a trusted internal network (LAN) and an untrusted external network (the Internet) that <b>monitors and controls incoming and outgoing traffic according to a set of security rules</b>. Like a fire wall in a building that stops fire from spreading, it stops unwanted traffic.</p>
<h4>Working</h4>
<ol><li>All traffic between the two networks is forced to pass through the firewall (a <b>choke point</b>).</li>
<li>For each packet or connection, the firewall reads the relevant information (addresses, ports, protocol, connection state, or content).</li>
<li>It compares this with the <b>rule base</b> (security policy), usually from top to bottom.</li>
<li>It takes the action of the first matching rule: <b>allow (accept)</b>, <b>deny (drop silently)</b> or <b>reject (drop and inform the sender)</b>, and may <b>log</b> the event.</li></ol>
<h4>Functions</h4>
<ul><li>Blocks unauthorised access from outside while allowing legitimate traffic.</li><li>Controls which internal users may use which Internet services.</li><li>Hides the internal network structure (often with NAT).</li><li>Logs and alerts on suspicious activity; can provide VPN.</li></ul>
<h4>Hardware and software firewalls</h4>
<ul><li><b>Hardware (network) firewall:</b> a separate device or built into a router; protects the whole network.</li>
<li><b>Software (host-based) firewall:</b> runs on a single computer, e.g. <b>Windows Defender Firewall</b>, Linux iptables / ufw; protects that host.</li></ul>""",
          """<p><b>Firewall</b> એ વિશ્વાસપાત્ર આંતરિક network (LAN) અને અવિશ્વસનીય બાહ્ય network (Internet) વચ્ચે મુકાયેલું hardware device કે software program છે જે <b>security rules ના સમૂહ મુજબ આવતા અને જતા traffic પર નજર રાખે અને નિયંત્રિત કરે</b>. Building માં આગને ફેલાતી અટકાવતી fire wall ની જેમ, તે અનિચ્છનીય traffic અટકાવે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ol><li>બે networks વચ્ચેનો બધો traffic firewall માંથી પસાર થવા ફરજિયાત બને (<b>choke point</b>).</li>
<li>દરેક packet કે connection માટે firewall સંબંધિત માહિતી (addresses, ports, protocol, connection state, કે content) વાંચે.</li>
<li>તેને <b>rule base</b> (security policy) સાથે સરખાવે, સામાન્ય રીતે ઉપરથી નીચે.</li>
<li>પ્રથમ મેળ ખાતા rule નું action લે: <b>allow (accept)</b>, <b>deny (ચુપચાપ drop)</b> કે <b>reject (drop કરી sender ને જાણ)</b>, અને ઘટના <b>log</b> કરી શકે.</li></ol>
<h4>કાર્યો</h4>
<ul><li>કાયદેસર traffic મંજૂર કરતાં બહારથી અનધિકૃત access અટકાવે.</li><li>કયા આંતરિક users કઈ Internet services વાપરી શકે તે નિયંત્રિત કરે.</li><li>આંતરિક network રચના છુપાવે (ઘણી વાર NAT સાથે).</li><li>શંકાસ્પદ પ્રવૃત્તિ log કરે અને alert આપે; VPN આપી શકે.</li></ul>
<h4>Hardware અને software firewalls</h4>
<ul><li><b>Hardware (network) firewall:</b> અલગ device કે router માં built in; આખું network બચાવે.</li>
<li><b>Software (host-based) firewall:</b> એક computer પર ચાલે, દા.ત. <b>Windows Defender Firewall</b>, Linux iptables / ufw; તે host ને બચાવે.</li></ul>""",
          diagram="cn5_firewall"),
        T("5.3.2 Firewall Design Principles", "5.3.2 Firewall Design Principles",
          """<h4>Design goals</h4>
<ol><li><b>All traffic</b> from inside to outside, and vice versa, must pass through the firewall (physically block all other access).</li>
<li><b>Only authorised traffic</b>, as defined by the local security policy, is allowed to pass.</li>
<li>The firewall itself must be <b>immune to penetration</b>: a hardened, trusted system with a secure operating system and minimal services.</li></ol>
<h4>Access control techniques</h4>
<ul><li><b>Service control:</b> which Internet services (web, email, FTP) may be accessed, by IP address and port.</li>
<li><b>Direction control:</b> in which direction a service request may flow (inbound or outbound).</li>
<li><b>User control:</b> which users may access a service (needs authentication).</li>
<li><b>Behaviour control:</b> how a service is used, e.g. filtering spam email or blocking certain websites.</li></ul>
<h4>Default policy</h4>
<ul><li><b>Default deny</b> ("that which is not expressly permitted is prohibited"): block everything and allow only needed services. More secure; recommended.</li>
<li><b>Default allow</b> ("that which is not expressly prohibited is permitted"): allow everything and block known bad traffic. Easier for users but less secure.</li></ul>
<h4>Other principles</h4>
<ul><li><b>Defence in depth:</b> several layers (outer firewall, <b>DMZ</b>, inner firewall, host firewalls, antivirus).</li>
<li><b>DMZ (demilitarised zone):</b> a separate network segment for public servers (web, mail, DNS), so outsiders never reach the internal LAN directly.</li>
<li><b>Least privilege</b>, simplicity of rules, logging and regular review of rules.</li></ul>
<h4>Limitations of a firewall</h4>
<p>It cannot protect against attacks that bypass it (a user's mobile hotspot), against insiders, against viruses in allowed traffic (unless it inspects content), or against social engineering. It is one part of security, not the whole.</p>""",
          """<h4>Design goals</h4>
<ol><li>અંદરથી બહાર અને બહારથી અંદરનો <b>બધો traffic</b> firewall માંથી પસાર થવો જોઈએ (બાકીના બધા access physically અટકાવો).</li>
<li>Local security policy માં વ્યાખ્યાયિત <b>ફક્ત અધિકૃત traffic</b> ને જ પસાર થવા દેવાય.</li>
<li>Firewall પોતે <b>ભેદી ન શકાય તેવું</b> હોવું જોઈએ: secure operating system અને ઓછામાં ઓછી services વાળું hardened, trusted system.</li></ol>
<h4>Access control techniques</h4>
<ul><li><b>Service control:</b> IP address અને port દ્વારા કઈ Internet services (web, email, FTP) વાપરી શકાય.</li>
<li><b>Direction control:</b> service request કઈ દિશામાં (inbound કે outbound) જઈ શકે.</li>
<li><b>User control:</b> કયા users service વાપરી શકે (authentication જોઈએ).</li>
<li><b>Behaviour control:</b> service કેવી રીતે વપરાય, દા.ત. spam email filter કરવા કે અમુક websites block કરવી.</li></ul>
<h4>Default policy</h4>
<ul><li><b>Default deny</b> ("જે સ્પષ્ટ રીતે મંજૂર નથી તે પ્રતિબંધિત છે"): બધું block કરો અને ફક્ત જરૂરી services મંજૂર કરો. વધુ secure; ભલામણ કરેલું.</li>
<li><b>Default allow</b> ("જે સ્પષ્ટ રીતે પ્રતિબંધિત નથી તે મંજૂર છે"): બધું મંજૂર કરો અને જાણીતો ખરાબ traffic block કરો. Users માટે સહેલું પણ ઓછું secure.</li></ul>
<h4>અન્ય સિદ્ધાંતો</h4>
<ul><li><b>Defence in depth:</b> અનેક સ્તરો (outer firewall, <b>DMZ</b>, inner firewall, host firewalls, antivirus).</li>
<li><b>DMZ (demilitarised zone):</b> public servers (web, mail, DNS) માટે અલગ network segment, જેથી બહારના લોકો આંતરિક LAN સુધી સીધા ક્યારેય ન પહોંચે.</li>
<li><b>Least privilege</b>, rules ની સરળતા, logging અને rules ની નિયમિત સમીક્ષા.</li></ul>
<h4>Firewall ની મર્યાદાઓ</h4>
<p>તેને bypass કરતા attacks (user નો mobile hotspot), insiders, મંજૂર traffic માંના viruses (content તપાસે નહીં ત્યાં સુધી), કે social engineering સામે તે રક્ષણ આપી શકતું નથી. તે security નો એક ભાગ છે, સંપૂર્ણ security નહીં.</p>""",
          diagram="cn5_dmz"),
        T("5.3.3 Types of Firewalls", "5.3.3 Firewalls ના પ્રકારો",
          """<p>Firewalls are classified by the OSI layer at which they examine traffic. Higher layers give more detailed checking but need more processing.</p>
<ul>
<li><b>Packet filtering firewall:</b> checks each packet's header against rules (see 5.3.4).</li>
<li><b>Stateful inspection firewall:</b> a packet filter that also keeps a <b>state table</b> of active connections; replies to connections started from inside are allowed automatically, and packets that do not belong to a valid connection are dropped. Most common today.</li>
<li><b>Circuit-level gateway:</b> works at the session layer; checks that the TCP handshake is legitimate and then relays the connection without examining content.</li>
<li><b>Application-level gateway (proxy firewall):</b> works at the application layer and examines the content (see 5.3.5).</li>
<li><b>Next-generation firewall (NGFW):</b> combines stateful filtering with deep packet inspection, application identification, intrusion prevention and threat intelligence.</li>
</ul>
""" + TYPES_EN,
          """<p>Firewalls traffic તપાસે તે OSI layer પ્રમાણે વર્ગીકૃત થાય. ઉપરના layers વધુ વિગતવાર તપાસ આપે પણ વધુ processing માગે.</p>
<ul>
<li><b>Packet filtering firewall:</b> દરેક packet નું header rules સાથે તપાસે (જુઓ 5.3.4).</li>
<li><b>Stateful inspection firewall:</b> packet filter જે સક્રિય connections નું <b>state table</b> પણ રાખે; અંદરથી શરૂ થયેલાં connections ના replies આપમેળે મંજૂર થાય, અને માન્ય connection ના ન હોય તેવાં packets drop થાય. આજે સૌથી સામાન્ય.</li>
<li><b>Circuit-level gateway:</b> session layer પર કામ કરે; TCP handshake કાયદેસર છે તે ચકાસી પછી content તપાસ્યા વગર connection relay કરે.</li>
<li><b>Application-level gateway (proxy firewall):</b> application layer પર કામ કરે અને content તપાસે (જુઓ 5.3.5).</li>
<li><b>Next-generation firewall (NGFW):</b> stateful filtering ને deep packet inspection, application identification, intrusion prevention અને threat intelligence સાથે જોડે.</li>
</ul>
""" + TYPES_GU,
          diagram="cn5_fw_osi"),
        T("5.3.4 Packet Filter Firewall", "5.3.4 Packet Filter Firewall",
          """<p>A <b>packet filter firewall</b> (screening router) examines <b>each packet independently</b> at the <b>network and transport layers</b> and decides to forward or discard it based on <b>header information only</b>:</p>
<ul><li>Source IP address and destination IP address</li><li>Protocol (TCP, UDP, ICMP)</li><li>Source and destination port numbers (identify the service: 80 HTTP, 443 HTTPS, 25 SMTP, 23 Telnet, 22 SSH)</li><li>Interface and direction (inbound / outbound), TCP flags</li></ul>
<h4>Working</h4>
<p>The administrator writes an ordered <b>rule table</b> (access control list). For every packet, rules are checked from top to bottom; the <b>first matching rule</b> decides allow or deny. If no rule matches, the <b>default rule</b> (normally deny) applies. A <b>stateless</b> packet filter has no memory of earlier packets; a <b>stateful</b> one also tracks connections.</p>
<p><b>Example rules:</b> allow anyone to reach the web server 192.168.1.10 on ports 80 / 443; allow mail to 192.168.1.11 on port 25; allow inside hosts to go out; deny Telnet (23); deny everything else.</p>
""" + PF_AD[0],
          """<p><b>Packet filter firewall</b> (screening router) <b>network અને transport layers</b> પર <b>દરેક packet ને સ્વતંત્ર રીતે</b> તપાસે અને <b>ફક્ત header માહિતી</b> ના આધારે તેને forward કે discard કરવાનું નક્કી કરે:</p>
<ul><li>Source IP address અને destination IP address</li><li>Protocol (TCP, UDP, ICMP)</li><li>Source અને destination port numbers (service ઓળખે: 80 HTTP, 443 HTTPS, 25 SMTP, 23 Telnet, 22 SSH)</li><li>Interface અને દિશા (inbound / outbound), TCP flags</li></ul>
<h4>કાર્યપદ્ધતિ</h4>
<p>Administrator ક્રમબદ્ધ <b>rule table</b> (access control list) લખે. દરેક packet માટે rules ઉપરથી નીચે તપાસાય; <b>પ્રથમ મેળ ખાતો rule</b> allow કે deny નક્કી કરે. કોઈ rule મેળ ન ખાય, તો <b>default rule</b> (સામાન્ય રીતે deny) લાગુ પડે. <b>Stateless</b> packet filter ને અગાઉનાં packets યાદ નથી; <b>stateful</b> connections પણ track કરે.</p>
<p><b>ઉદાહરણ rules:</b> કોઈ પણ ને web server 192.168.1.10 સુધી ports 80 / 443 પર પહોંચવા દો; 192.168.1.11 ને port 25 પર mail મંજૂર; અંદરના hosts ને બહાર જવા દો; Telnet (23) deny; બાકી બધું deny.</p>
""" + PF_AD[1],
          diagram="cn5_pfilter", examples=["cn5n4"]),
        T("5.3.5 Proxy Firewall", "5.3.5 Proxy Firewall",
          """<p>A <b>proxy firewall</b>, also called an <b>application-level gateway</b>, works at the <b>application layer</b>. It acts as an <b>intermediary</b>: the client connects to the proxy, the proxy checks the request and, if allowed, opens a <b>separate connection</b> to the real server on the client's behalf. There is <b>never a direct connection</b> between the inside host and the outside server.</p>
<h4>Working</h4>
<ol><li>The user's browser sends a request (e.g. GET a web page) to the proxy.</li>
<li>The proxy may authenticate the user and examines the request at the application level: URL, commands (FTP put / get), content type, file attachments.</li>
<li>If the request obeys the policy, the proxy sends its own request to the server using its own address.</li>
<li>The server's reply comes back to the proxy, which inspects it (e.g. virus scan) and passes it to the client; it can also <b>cache</b> it for later requests.</li></ol>
<p>Because it understands each protocol, a separate proxy service is needed for HTTP, FTP, SMTP, etc. Example: the <b>Squid</b> web proxy used in many college networks to block sites and save bandwidth.</p>
""" + PX_AD[0] + """
<h4>Packet filter vs proxy firewall</h4>
""" + CMP_EN,
          """<p><b>Proxy firewall</b>, જેને <b>application-level gateway</b> પણ કહે, <b>application layer</b> પર કામ કરે. તે <b>મધ્યસ્થી</b> તરીકે કામ કરે: client proxy સાથે જોડાય, proxy request તપાસે અને મંજૂર હોય તો client વતી સાચા server સાથે <b>અલગ connection</b> ખોલે. અંદરના host અને બહારના server વચ્ચે <b>ક્યારેય સીધું connection</b> હોતું નથી.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ol><li>User નું browser request (દા.ત. web page GET) proxy ને મોકલે.</li>
<li>Proxy user ને authenticate કરી શકે અને application સ્તરે request તપાસે: URL, commands (FTP put / get), content type, file attachments.</li>
<li>Request policy મુજબ હોય, તો proxy પોતાના address થી server ને પોતાની request મોકલે.</li>
<li>Server નો reply proxy પાસે આવે, જે તેને તપાસી (દા.ત. virus scan) client ને આપે; પછીની requests માટે તેને <b>cache</b> પણ કરી શકે.</li></ol>
<p>દરેક protocol સમજતું હોવાથી HTTP, FTP, SMTP વગેરે માટે અલગ proxy service જોઈએ. ઉદાહરણ: sites block કરવા અને bandwidth બચાવવા ઘણાં college networks માં વપરાતું <b>Squid</b> web proxy.</p>
""" + PX_AD[1] + """
<h4>Packet filter vs proxy firewall</h4>
""" + CMP_GU,
          diagram="cn5_proxy"),
        T("5.3.6 Practical 9: Windows Defender Firewall", "5.3.6 Practical 9: Windows Defender Firewall",
          """<p><b>Aim:</b> study how a firewall provides network security, using the built-in host firewall of Windows.</p>
<h4>Steps</h4>
<ol><li>Open <b>Control Panel → System and Security → Windows Defender Firewall</b> (or run <b>wf.msc</b> for Advanced Security).</li>
<li>Observe the network profiles: <b>Domain, Private, Public</b>, and check that the firewall is <b>On</b> for each.</li>
<li><b>Allow an app through the firewall:</b> choose an app and tick Private / Public.</li>
<li>In <b>Advanced settings</b>, view <b>Inbound Rules</b> and <b>Outbound Rules</b>.</li>
<li><b>Create a rule:</b> New Rule → Port → TCP, specific port 23 → Block the connection → apply to all profiles → name it "Block Telnet".</li>
<li><b>Test:</b> create an inbound rule to block <b>ICMPv4 (ping)</b>; ping this PC from another PC and observe "Request timed out"; disable the rule and ping again to see replies.</li>
<li>Enable <b>logging</b> (Properties → Logging → log dropped packets) and view the log file pfirewall.log.</li></ol>
<h4>Observation / conclusion</h4>
<p>The firewall is a stateful host firewall: by default it blocks unsolicited inbound connections and allows outbound traffic. Rules based on program, port, protocol and IP address control which traffic is allowed, protecting the computer from unauthorised access.</p>
<p>On Linux, the same can be done with <b>ufw</b> (e.g. <b>sudo ufw deny 23/tcp</b>) or iptables.</p>""",
          """<p><b>હેતુ:</b> Windows ના built-in host firewall વાપરીને firewall network security કેવી રીતે આપે છે તેનો અભ્યાસ.</p>
<h4>પગલાં</h4>
<ol><li><b>Control Panel → System and Security → Windows Defender Firewall</b> ખોલો (અથવા Advanced Security માટે <b>wf.msc</b> ચલાવો).</li>
<li>Network profiles જુઓ: <b>Domain, Private, Public</b>, અને દરેક માટે firewall <b>On</b> છે તે તપાસો.</li>
<li><b>Firewall માંથી app ને મંજૂરી:</b> app પસંદ કરી Private / Public પર tick કરો.</li>
<li><b>Advanced settings</b> માં <b>Inbound Rules</b> અને <b>Outbound Rules</b> જુઓ.</li>
<li><b>Rule બનાવો:</b> New Rule → Port → TCP, specific port 23 → Block the connection → બધા profiles પર લાગુ → નામ "Block Telnet".</li>
<li><b>Test:</b> <b>ICMPv4 (ping)</b> block કરવા inbound rule બનાવો; બીજા PC પરથી આ PC ને ping કરી "Request timed out" જુઓ; rule disable કરી ફરી ping કરી replies જુઓ.</li>
<li><b>Logging</b> ચાલુ કરો (Properties → Logging → log dropped packets) અને log file pfirewall.log જુઓ.</li></ol>
<h4>અવલોકન / નિષ્કર્ષ</h4>
<p>આ firewall stateful host firewall છે: default રીતે માગ્યા વગરનાં inbound connections block કરે અને outbound traffic મંજૂર કરે. Program, port, protocol અને IP address આધારિત rules કયો traffic મંજૂર છે તે નિયંત્રિત કરી computer ને અનધિકૃત access થી બચાવે.</p>
<p>Linux પર આ જ <b>ufw</b> (દા.ત. <b>sudo ufw deny 23/tcp</b>) કે iptables થી કરી શકાય.</p>"""),
    ]}
