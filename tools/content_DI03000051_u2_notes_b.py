"""Computer Networks (DI03000051) - Unit 2 notes part B: 2.2 TCP/IP model, 2.3 Comparison of OSI and TCP/IP."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

TCPUDP_EN = tbl(["TCP", "UDP"], [
    ("Transmission Control Protocol", "User Datagram Protocol"),
    ("Connection-oriented (3-way handshake)", "Connectionless"),
    ("Reliable: acknowledgement, retransmission", "Unreliable: no acknowledgement"),
    ("Data arrives in order (sequence numbers)", "No ordering guarantee"),
    ("Flow and congestion control", "No flow control"),
    ("Header 20-60 bytes; slower", "Header 8 bytes; faster"),
    ("HTTP, FTP, SMTP, SSH", "DNS, DHCP, VoIP, video streaming, online games")])
TCPUDP_GU = tbl(["TCP", "UDP"], [
    ("Transmission Control Protocol", "User Datagram Protocol"),
    ("Connection-oriented (3-way handshake)", "Connectionless"),
    ("વિશ્વસનીય: acknowledgement, retransmission", "અવિશ્વસનીય: acknowledgement નહીં"),
    ("Data ક્રમમાં પહોંચે (sequence numbers)", "ક્રમની ખાતરી નહીં"),
    ("Flow અને congestion control", "Flow control નહીં"),
    ("Header 20-60 bytes; ધીમું", "Header 8 bytes; ઝડપી"),
    ("HTTP, FTP, SMTP, SSH", "DNS, DHCP, VoIP, video streaming, online games")])

APP_EN = tbl(["Protocol", "Port", "Use"], [
    ("HTTP / HTTPS", "80 / 443", "Web pages (HTTPS secure)"), ("FTP", "20, 21", "File transfer"),
    ("SMTP", "25", "Send e-mail"), ("POP3 / IMAP", "110 / 143", "Receive e-mail"),
    ("DNS", "53", "Domain name to IP address"), ("Telnet / SSH", "23 / 22", "Remote login"),
    ("DHCP", "67, 68", "Automatic IP configuration"), ("SNMP", "161", "Network management")])
APP_GU = tbl(["Protocol", "Port", "ઉપયોગ"], [
    ("HTTP / HTTPS", "80 / 443", "Web pages (HTTPS secure)"), ("FTP", "20, 21", "File transfer"),
    ("SMTP", "25", "E-mail મોકલવા"), ("POP3 / IMAP", "110 / 143", "E-mail મેળવવા"),
    ("DNS", "53", "Domain name થી IP address"), ("Telnet / SSH", "23 / 22", "Remote login"),
    ("DHCP", "67, 68", "આપમેળે IP configuration"), ("SNMP", "161", "Network management")])

CMP_EN = tbl(["OSI model", "TCP/IP model"], [
    ("Open Systems Interconnection", "Transmission Control Protocol / Internet Protocol"),
    ("Developed by ISO (1984)", "Developed by US DoD for ARPANET (1970s)"),
    ("7 layers", "4 layers (5 in some books)"),
    ("Reference / conceptual model; generic", "Practical model; the Internet is based on it"),
    ("Model defined first, protocols later", "Protocols came first, model described them"),
    ("Clear distinction between services, interfaces and protocols", "No clear distinction"),
    ("Separate session and presentation layers", "Included in the application layer"),
    ("Network layer: connectionless and connection-oriented", "Internet layer: connectionless only (IP)"),
    ("Transport layer: connection-oriented only", "Transport: both (TCP and UDP)"),
    ("Protocols are hidden, easily replaced", "Protocols are not easily replaced"),
    ("Vertical approach", "Horizontal approach"),
    ("Used mainly for teaching and troubleshooting", "Used in real networks and the Internet")])
CMP_GU = tbl(["OSI model", "TCP/IP model"], [
    ("Open Systems Interconnection", "Transmission Control Protocol / Internet Protocol"),
    ("ISO એ બનાવ્યું (1984)", "US DoD એ ARPANET માટે બનાવ્યું (1970s)"),
    ("7 layers", "4 layers (કેટલાંક પુસ્તકોમાં 5)"),
    ("Reference / conceptual model; generic", "Practical model; Internet તેના પર આધારિત"),
    ("પહેલાં model, પછી protocols", "પહેલાં protocols, model એ તેમનું વર્ણન કર્યું"),
    ("Services, interfaces અને protocols વચ્ચે સ્પષ્ટ ભેદ", "સ્પષ્ટ ભેદ નથી"),
    ("અલગ session અને presentation layers", "Application layer માં સમાવેશ"),
    ("Network layer: connectionless અને connection-oriented", "Internet layer: માત્ર connectionless (IP)"),
    ("Transport layer: માત્ર connection-oriented", "Transport: બંને (TCP અને UDP)"),
    ("Protocols છુપાયેલા, સહેલાઈથી બદલાય", "Protocols સહેલાઈથી બદલાતા નથી"),
    ("Vertical approach", "Horizontal approach"),
    ("મુખ્યત્વે શીખવવા અને troubleshooting માટે", "ખરા networks અને Internet માં વપરાય")])

SEC_2_2 = {
    "title": {"en": "2.2 TCP/IP Model", "gu": "2.2 TCP/IP Model"},
    "items": [
        T("2.2.1 Introduction to the TCP/IP Model", "2.2.1 TCP/IP Model નો પરિચય",
          """<p>The <b>TCP/IP model</b> (Internet model) is named after its two main protocols: <b>Transmission Control Protocol</b> and <b>Internet Protocol</b>. It was developed in the 1970s by the <b>US Department of Defense (DoD)</b> for <b>ARPANET</b>, before the OSI model, and became the standard of the Internet in 1983.</p>
<p>TCP/IP is a <b>hierarchical protocol suite</b> made of interactive modules, each providing a specific function; the modules are not necessarily interdependent (unlike strict OSI layering).</p>
<h4>Layers</h4>
<ol><li><b>Network access (host-to-network / link) layer</b>: corresponds to OSI physical + data link.</li><li><b>Internet layer</b>: corresponds to OSI network layer.</li><li><b>Transport layer</b>: corresponds to OSI transport layer.</li><li><b>Application layer</b>: corresponds to OSI session + presentation + application.</li></ol>
<p>Many textbooks (Forouzan) describe a <b>five-layer</b> TCP/IP model: physical, data link, network, transport and application.</p>
<h4>Design goals</h4>
<ul><li>Connect different kinds of networks seamlessly (internetworking).</li><li>Survive the loss of network hardware: connections stay up as long as source and destination work (robustness).</li><li>Flexible architecture supporting applications with different needs (file transfer to real-time speech).</li></ul>""",
          """<p><b>TCP/IP model</b> (Internet model) નું નામ તેના બે મુખ્ય protocols: <b>Transmission Control Protocol</b> અને <b>Internet Protocol</b> પરથી પડ્યું છે. તે 1970s માં <b>US Department of Defense (DoD)</b> એ <b>ARPANET</b> માટે, OSI model પહેલાં બનાવ્યું, અને 1983 માં Internet નું standard બન્યું.</p>
<p>TCP/IP એ interactive modules નું બનેલું <b>hierarchical protocol suite</b> છે, દરેક ચોક્કસ કાર્ય આપે; modules જરૂરી નથી કે એકબીજા પર આધારિત હોય (કડક OSI layering થી વિપરીત).</p>
<h4>Layers</h4>
<ol><li><b>Network access (host-to-network / link) layer</b>: OSI physical + data link ને અનુરૂપ.</li><li><b>Internet layer</b>: OSI network layer ને અનુરૂપ.</li><li><b>Transport layer</b>: OSI transport layer ને અનુરૂપ.</li><li><b>Application layer</b>: OSI session + presentation + application ને અનુરૂપ.</li></ol>
<p>ઘણાં પાઠ્યપુસ્તકો (Forouzan) <b>પાંચ-layer</b> TCP/IP model વર્ણવે છે: physical, data link, network, transport અને application.</p>
<h4>Design ના ધ્યેયો</h4>
<ul><li>જુદા પ્રકારના networks ને સરળતાથી જોડવા (internetworking).</li><li>Network hardware ગુમાવવા છતાં ટકી રહેવું: source અને destination ચાલુ હોય ત્યાં સુધી connections ચાલુ રહે (robustness).</li><li>જુદી જરૂરિયાતો (file transfer થી real-time speech) વાળી applications ને support કરતું flexible architecture.</li></ul>""",
          diagram="cn2_tcpip"),
        T("2.2.2 Network Access Layer and Internet Layer", "2.2.2 Network Access Layer અને Internet Layer",
          """<h4>1. Network access (host-to-network) layer</h4>
<p>The lowest layer. TCP/IP does not define a specific protocol here; it supports all standard and proprietary protocols. It handles the <b>physical transmission</b> of bits and <b>framing</b>, MAC addressing and media access on the local network.</p>
<ul><li>Functions: send IP packets over the physical network, framing, MAC addressing, error detection, mapping IP to physical addresses.</li><li>Technologies: Ethernet, Wi-Fi, PPP, DSL, token ring, device drivers and NICs.</li></ul>
<h4>2. Internet layer</h4>
<p>The key layer that holds the architecture together. It permits hosts to <b>inject packets into any network</b> and have them travel independently to the destination, possibly by different routes and arriving out of order.</p>
<ul>
<li><b>IP (Internet Protocol):</b> an <b>unreliable, connectionless</b>, best-effort protocol; provides logical addressing and routing. Data units are called <b>datagrams</b>. Versions: IPv4 (32-bit address) and IPv6 (128-bit).</li>
<li><b>ARP (Address Resolution Protocol):</b> finds the <b>physical (MAC) address</b> of a host when its IP address is known.</li>
<li><b>RARP (Reverse ARP):</b> finds the IP address when the physical address is known (replaced by DHCP).</li>
<li><b>ICMP (Internet Control Message Protocol):</b> sends error and query messages (destination unreachable, time exceeded); used by <code>ping</code> and <code>tracert</code>.</li>
<li><b>IGMP (Internet Group Management Protocol):</b> manages <b>multicast</b> group membership (one message to a group of receivers).</li>
</ul>""",
          """<h4>1. Network access (host-to-network) layer</h4>
<p>સૌથી નીચેનું layer. TCP/IP અહીં ચોક્કસ protocol નક્કી કરતું નથી; તે બધા standard અને proprietary protocols ને support કરે. તે local network પર bits નું <b>physical transmission</b> અને <b>framing</b>, MAC addressing અને media access સંભાળે.</p>
<ul><li>કાર્યો: physical network પર IP packets મોકલવા, framing, MAC addressing, error detection, IP ને physical addresses સાથે જોડવા.</li><li>Technologies: Ethernet, Wi-Fi, PPP, DSL, token ring, device drivers અને NICs.</li></ul>
<h4>2. Internet layer</h4>
<p>Architecture ને જોડી રાખતું મુખ્ય layer. તે hosts ને <b>કોઈ પણ network માં packets મોકલવા</b> દે અને તે destination સુધી સ્વતંત્ર રીતે, કદાચ જુદા માર્ગે અને ક્રમ બહાર પહોંચે.</p>
<ul>
<li><b>IP (Internet Protocol):</b> <b>અવિશ્વસનીય, connectionless</b>, best-effort protocol; logical addressing અને routing આપે. Data units ને <b>datagrams</b> કહે છે. Versions: IPv4 (32-bit address) અને IPv6 (128-bit).</li>
<li><b>ARP (Address Resolution Protocol):</b> IP address ખબર હોય ત્યારે host નું <b>physical (MAC) address</b> શોધે.</li>
<li><b>RARP (Reverse ARP):</b> physical address ખબર હોય ત્યારે IP address શોધે (DHCP એ સ્થાન લીધું).</li>
<li><b>ICMP (Internet Control Message Protocol):</b> error અને query messages મોકલે (destination unreachable, time exceeded); <code>ping</code> અને <code>tracert</code> વાપરે.</li>
<li><b>IGMP (Internet Group Management Protocol):</b> <b>multicast</b> group membership સંભાળે (receivers ના જૂથને એક message).</li>
</ul>"""),
        T("2.2.3 Transport Layer: TCP, UDP, SCTP", "2.2.3 Transport Layer: TCP, UDP, SCTP",
          """<p>The transport layer of TCP/IP provides <b>process-to-process</b> communication using <b>port numbers</b>. It allows peer entities on the source and destination hosts to carry on a conversation.</p>
<ul>
<li><b>TCP (Transmission Control Protocol):</b> a <b>reliable, connection-oriented</b> stream protocol. A connection is set up with a <b>three-way handshake</b> (SYN, SYN-ACK, ACK) before data is sent. The byte stream is divided into <b>segments</b> with sequence numbers; the receiver acknowledges them; lost segments are retransmitted; flow control and congestion control are provided.</li>
<li><b>UDP (User Datagram Protocol):</b> a simple, <b>unreliable, connectionless</b> protocol. It adds only port addresses, a checksum and length to the data. Used where speed matters more than reliability, or for one-request one-reply applications.</li>
<li><b>SCTP (Stream Control Transmission Protocol):</b> newer protocol combining the best features of TCP and UDP; supports multiple streams; used for telephony signalling over IP.</li>
</ul>
<h4>TCP vs UDP</h4>
""" + TCPUDP_EN,
          """<p>TCP/IP નું transport layer <b>port numbers</b> વાપરીને <b>process-to-process</b> communication આપે છે. તે source અને destination hosts પરની peer entities ને વાતચીત કરવા દે.</p>
<ul>
<li><b>TCP (Transmission Control Protocol):</b> <b>વિશ્વસનીય, connection-oriented</b> stream protocol. Data મોકલતાં પહેલાં <b>three-way handshake</b> (SYN, SYN-ACK, ACK) થી connection બને. Byte stream sequence numbers સાથે <b>segments</b> માં વહેંચાય; receiver acknowledge કરે; ખોવાયેલા segments ફરી મોકલાય; flow control અને congestion control મળે.</li>
<li><b>UDP (User Datagram Protocol):</b> સરળ, <b>અવિશ્વસનીય, connectionless</b> protocol. તે data માં માત્ર port addresses, checksum અને length ઉમેરે. જ્યાં reliability કરતાં speed વધુ મહત્વની હોય, કે એક-request એક-reply applications માટે વપરાય.</li>
<li><b>SCTP (Stream Control Transmission Protocol):</b> TCP અને UDP ની શ્રેષ્ઠ લાક્ષણિકતાઓ જોડતો નવો protocol; ઘણા streams support કરે; IP પર telephony signalling માટે વપરાય.</li>
</ul>
<h4>TCP vs UDP</h4>
""" + TCPUDP_GU,
          examples=["cn2n3", "cn2n4"]),
        T("2.2.4 Application Layer of TCP/IP", "2.2.4 TCP/IP નું Application Layer",
          """<p>The application layer of TCP/IP combines the functions of the OSI <b>session, presentation and application</b> layers. It contains all the higher-level protocols that users and programs use directly. Each application protocol uses TCP or UDP with a <b>well-known port number</b>.</p>
""" + APP_EN + """
<ul><li><b>HTTP:</b> client (browser) requests a web page; server responds. HTTPS adds TLS encryption.</li><li><b>FTP:</b> uses two connections: port 21 for control and port 20 for data.</li><li><b>SMTP:</b> push protocol for sending mail between mail servers; POP3 / IMAP are used by the client to pull mail.</li><li><b>DNS:</b> converts names like www.gtu.ac.in to IP addresses (uses UDP).</li><li><b>Telnet / SSH:</b> remote login; SSH encrypts the session.</li><li><b>SNMP:</b> monitors and manages network devices.</li></ul>""",
          """<p>TCP/IP નું application layer OSI ના <b>session, presentation અને application</b> layers નાં કાર્યો જોડે છે. તેમાં users અને programs સીધા વાપરે તે બધા ઉચ્ચ-સ્તરના protocols છે. દરેક application protocol <b>well-known port number</b> સાથે TCP કે UDP વાપરે.</p>
""" + APP_GU + """
<ul><li><b>HTTP:</b> client (browser) web page માંગે; server જવાબ આપે. HTTPS TLS encryption ઉમેરે.</li><li><b>FTP:</b> બે connections વાપરે: control માટે port 21 અને data માટે port 20.</li><li><b>SMTP:</b> mail servers વચ્ચે mail મોકલવાનો push protocol; client mail ખેંચવા POP3 / IMAP વાપરે.</li><li><b>DNS:</b> www.gtu.ac.in જેવાં નામોને IP addresses માં ફેરવે (UDP વાપરે).</li><li><b>Telnet / SSH:</b> remote login; SSH session encrypt કરે.</li><li><b>SNMP:</b> network devices નું monitoring અને management.</li></ul>"""),
        T("2.2.5 Addressing in TCP/IP", "2.2.5 TCP/IP માં Addressing",
          """<p>Four levels of addresses are used in an internet that uses TCP/IP:</p>
<ol>
<li><b>Physical (link / MAC) address:</b> the address of a node as defined by its LAN or WAN; included in the frame by the data link layer. Ethernet uses a <b>48-bit</b> (6-byte) address written in hexadecimal, e.g. <code>07:01:02:01:2C:4B</code>. It has authority only on the local network and <b>changes at every hop</b>.</li>
<li><b>Logical (IP) address:</b> a universal address independent of the physical network, needed for communication across networks. IPv4 address = <b>32 bits</b>, e.g. <code>192.168.1.5</code>; IPv6 = 128 bits. It stays the <b>same from source to destination</b>.</li>
<li><b>Port address:</b> a <b>16-bit</b> number identifying a process on a host, e.g. 80 for HTTP, 25 for SMTP. Port numbers 0-1023 are well-known ports.</li>
<li><b>Specific address:</b> user-friendly addresses used by applications: e-mail address (student@gtu.ac.in) and URL (www.gtu.ac.in). They are converted to port and logical addresses (by DNS).</li>
</ol>""",
          """<p>TCP/IP વાપરતા internet માં ચાર સ્તરના addresses વપરાય છે:</p>
<ol>
<li><b>Physical (link / MAC) address:</b> LAN કે WAN દ્વારા નક્કી થયેલું node નું address; data link layer frame માં મૂકે. Ethernet hexadecimal માં લખાતું <b>48-bit</b> (6-byte) address વાપરે, દા.ત. <code>07:01:02:01:2C:4B</code>. તે માત્ર local network પર માન્ય છે અને <b>દરેક hop પર બદલાય</b>.</li>
<li><b>Logical (IP) address:</b> physical network થી સ્વતંત્ર વૈશ્વિક address, networks પાર communication માટે જરૂરી. IPv4 address = <b>32 bits</b>, દા.ત. <code>192.168.1.5</code>; IPv6 = 128 bits. તે <b>source થી destination સુધી સરખું</b> રહે.</li>
<li><b>Port address:</b> host પરની process ઓળખતો <b>16-bit</b> number, દા.ત. HTTP માટે 80, SMTP માટે 25. Port numbers 0-1023 well-known ports છે.</li>
<li><b>Specific address:</b> applications વાપરે તેવાં user-friendly addresses: e-mail address (student@gtu.ac.in) અને URL (www.gtu.ac.in). તે (DNS વડે) port અને logical addresses માં ફેરવાય.</li>
</ol>""",
          diagram="cn2_addr"),
    ]}

SEC_2_3 = {
    "title": {"en": "2.3 Comparison of OSI and TCP/IP Models", "gu": "2.3 OSI અને TCP/IP Models ની સરખામણી"},
    "items": [
        T("2.3.1 OSI vs TCP/IP", "2.3.1 OSI vs TCP/IP",
          """<h4>Similarities</h4>
<ul><li>Both are based on the concept of a <b>stack of independent protocols / layers</b>.</li><li>The functionality of the layers is roughly similar: in both, the layers up to transport provide end-to-end, network-independent transport service; layers above transport are application-oriented users of that service.</li><li>Both have network, transport and application layers; both use packet switching.</li></ul>
<h4>Differences</h4>
""" + CMP_EN + """
<h4>Criticism</h4>
<p><b>OSI:</b> bad timing (TCP/IP was already in use), complex, some layers (session, presentation) nearly empty while others (data link, network) are overloaded. <b>TCP/IP:</b> does not clearly separate service, interface and protocol, so it is not a good model for new technologies; the host-to-network layer is not really a layer.</p>""",
          """<h4>સામ્યતાઓ</h4>
<ul><li>બંને <b>સ્વતંત્ર protocols / layers ના stack</b> ના ખ્યાલ પર આધારિત છે.</li><li>Layers ની કાર્યક્ષમતા લગભગ સરખી છે: બંનેમાં transport સુધીના layers end-to-end, network-independent transport service આપે; transport ઉપરના layers એ service ના application-oriented users છે.</li><li>બંનેમાં network, transport અને application layers છે; બંને packet switching વાપરે.</li></ul>
<h4>તફાવતો</h4>
""" + CMP_GU + """
<h4>ટીકા</h4>
<p><b>OSI:</b> ખરાબ સમય (TCP/IP પહેલેથી વપરાતું હતું), જટિલ, કેટલાક layers (session, presentation) લગભગ ખાલી જ્યારે બીજા (data link, network) પર વધુ ભાર. <b>TCP/IP:</b> service, interface અને protocol સ્પષ્ટ અલગ નથી કરતું, તેથી નવી technologies માટે સારું model નથી; host-to-network layer ખરેખર layer નથી.</p>""",
          diagram="cn2_map"),
    ]}
