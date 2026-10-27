"""Computer Networks (DI03000051) - Unit 1 notes part B: 1.3 Network topology, 1.4 Standard organizations and
protocols, 1.5 Types of servers."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl


def adv(a_en, d_en, a_gu, d_gu):
    """Advantages / disadvantages lists (EN, GU)."""
    li = lambda xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    return ("<h4>Advantages</h4>" + li(a_en) + "<h4>Disadvantages</h4>" + li(d_en),
            "<h4>ફાયદા</h4>" + li(a_gu) + "<h4>ગેરફાયદા</h4>" + li(d_gu))


TOPO_CMP_EN = tbl(["Topology", "Links for n devices", "Ports per device", "Main drawback"], [
    ("Bus", "1 backbone + n drop lines", "1", "Backbone fault stops all"),
    ("Star", "n (to hub)", "1 (hub needs n)", "Hub failure stops all"),
    ("Ring", "n", "2", "One break can stop ring"),
    ("Mesh", "n(n-1)/2", "n-1", "Very high cost"),
    ("Tree", "n-1 links in hierarchy", "1 (hubs more)", "Root failure"),
    ("Hybrid", "Depends on parts", "Depends", "Complex, costly")])
TOPO_CMP_GU = tbl(["Topology", "n devices માટે links", "Device દીઠ ports", "મુખ્ય ખામી"], [
    ("Bus", "1 backbone + n drop lines", "1", "Backbone fault થી બધું બંધ"),
    ("Star", "n (hub સુધી)", "1 (hub ને n)", "Hub બગડે તો બધું બંધ"),
    ("Ring", "n", "2", "એક break થી ring બંધ"),
    ("Mesh", "n(n-1)/2", "n-1", "ખૂબ વધુ ખર્ચ"),
    ("Tree", "Hierarchy માં n-1 links", "1 (hubs ને વધુ)", "Root બગડે"),
    ("Hybrid", "ભાગો પર આધાર", "આધાર", "જટિલ, ખર્ચાળ")])

ORG_EN = tbl(["Organisation", "Full form and role"], [
    ("IEEE", "<b>Institute of Electrical and Electronics Engineers</b> (USA, 1963). Largest professional engineering society; develops standards for LANs and wireless: <b>IEEE 802 project</b>: 802.3 Ethernet, 802.11 Wi-Fi, 802.15 Bluetooth/PAN, 802.16 WiMAX."),
    ("ISO", "<b>International Organization for Standardization</b> (Geneva, 1947). Body of national standard organisations of about 165 countries; created the <b>OSI reference model</b> (ISO 7498) for open systems interconnection."),
    ("ISOC", "<b>Internet Society</b> (1992). Non-profit body that promotes the open development, evolution and use of the Internet; provides the organisational home and funding for IETF, IAB and IRTF."),
    ("IETF", "<b>Internet Engineering Task Force</b>. Open community of network designers that develops and publishes <b>Internet standards</b> as <b>RFCs</b> (Request for Comments): TCP, IP, HTTP, SMTP. Works in working groups organised by area."),
    ("IRTF", "<b>Internet Research Task Force</b>. Works on <b>long-term research</b> problems of the Internet (future protocols, applications, architecture, technology) through research groups; results may later become IETF standards.")])
ORG_GU = tbl(["Organisation", "Full form અને ભૂમિકા"], [
    ("IEEE", "<b>Institute of Electrical and Electronics Engineers</b> (USA, 1963). સૌથી મોટી professional engineering society; LANs અને wireless માટે standards બનાવે: <b>IEEE 802 project</b>: 802.3 Ethernet, 802.11 Wi-Fi, 802.15 Bluetooth/PAN, 802.16 WiMAX."),
    ("ISO", "<b>International Organization for Standardization</b> (Geneva, 1947). લગભગ 165 દેશોની national standard organisations નો સમૂહ; open systems interconnection માટે <b>OSI reference model</b> (ISO 7498) બનાવ્યું."),
    ("ISOC", "<b>Internet Society</b> (1992). Internet ના ખુલ્લા વિકાસ, પ્રગતિ અને ઉપયોગને પ્રોત્સાહન આપતી non-profit સંસ્થા; IETF, IAB અને IRTF ને સંસ્થાકીય આધાર અને funding આપે."),
    ("IETF", "<b>Internet Engineering Task Force</b>. Network designers નો ખુલ્લો સમુદાય જે <b>Internet standards</b> ને <b>RFCs</b> (Request for Comments) તરીકે બનાવે અને પ્રકાશિત કરે: TCP, IP, HTTP, SMTP. વિસ્તાર પ્રમાણે working groups માં કામ કરે."),
    ("IRTF", "<b>Internet Research Task Force</b>. Research groups દ્વારા Internet ની <b>લાંબા ગાળાની research</b> સમસ્યાઓ (ભાવિ protocols, applications, architecture, technology) પર કામ કરે; પરિણામો પછી IETF standards બની શકે.")])

PROTO_EN = tbl(["Protocol", "Use"], [
    ("HTTP / HTTPS", "Transfer web pages (HTTPS = secure, encrypted)"), ("FTP", "Transfer files between computers"),
    ("SMTP", "Send e-mail"), ("POP3 / IMAP", "Receive / read e-mail from a mail server"),
    ("TCP", "Reliable, connection-oriented delivery of data"), ("UDP", "Fast, connectionless delivery (video, DNS)"),
    ("IP", "Addressing and routing of packets"), ("DNS", "Converts domain names to IP addresses"),
    ("DHCP", "Gives IP addresses automatically to computers"), ("Telnet / SSH", "Remote login (SSH is secure)")])
PROTO_GU = tbl(["Protocol", "ઉપયોગ"], [
    ("HTTP / HTTPS", "Web pages transfer (HTTPS = secure, encrypted)"), ("FTP", "Computers વચ્ચે files transfer"),
    ("SMTP", "E-mail મોકલવા"), ("POP3 / IMAP", "Mail server પરથી e-mail મેળવવા / વાંચવા"),
    ("TCP", "વિશ્વસનીય, connection-oriented data delivery"), ("UDP", "ઝડપી, connectionless delivery (video, DNS)"),
    ("IP", "Packets નું addressing અને routing"), ("DNS", "Domain names ને IP addresses માં ફેરવે"),
    ("DHCP", "Computers ને આપમેળે IP addresses આપે"), ("Telnet / SSH", "Remote login (SSH secure છે)")])

SRV_EN = tbl(["Server", "Main protocols / software", "Example"], [
    ("File server", "SMB/CIFS, NFS, FTP", "Windows Server shared folder, NAS"),
    ("Print server", "IPP, LPD", "Lab printer shared by 40 PCs"),
    ("Mail server", "SMTP, POP3, IMAP", "Gmail, Microsoft Exchange, Postfix"),
    ("Web server", "HTTP, HTTPS", "Apache, Nginx, Microsoft IIS"),
    ("Proxy server", "HTTP proxy, SOCKS", "Squid in a college network")])
SRV_GU = tbl(["Server", "મુખ્ય protocols / software", "ઉદાહરણ"], [
    ("File server", "SMB/CIFS, NFS, FTP", "Windows Server shared folder, NAS"),
    ("Print server", "IPP, LPD", "40 PCs વહેંચતા lab printer"),
    ("Mail server", "SMTP, POP3, IMAP", "Gmail, Microsoft Exchange, Postfix"),
    ("Web server", "HTTP, HTTPS", "Apache, Nginx, Microsoft IIS"),
    ("Proxy server", "HTTP proxy, SOCKS", "College network માં Squid")])

BUS = adv(["Easy to install; least cable of all topologies, so cheap.", "Easy to add a device by tapping the backbone.", "Good for small, temporary networks."],
          ["A break in the backbone stops the whole network.", "Only one device can send at a time; collisions increase with more devices; slow under heavy traffic.",
           "Fault isolation is difficult; limited cable length and number of devices.", "Terminators are needed at both ends to prevent signal reflection."],
          ["Install કરવું સહેલું; બધી topologies માં સૌથી ઓછો cable, તેથી સસ્તું.", "Backbone પર tap કરી device ઉમેરવું સહેલું.", "નાના, કામચલાઉ networks માટે સારું."],
          ["Backbone માં break આખું network બંધ કરે.", "એક સમયે એક જ device મોકલી શકે; devices વધતાં collisions વધે; વધુ traffic માં ધીમું.",
           "Fault શોધવો મુશ્કેલ; cable ની લંબાઈ અને devices ની સંખ્યા મર્યાદિત.", "Signal reflection અટકાવવા બંને છેડે terminators જરૂરી."])
STAR = adv(["Easy to install, configure, add or remove devices.", "Failure of one link or device affects only that device.",
            "Easy fault detection and isolation from the hub.", "Less cable than mesh; each device needs only one port.", "Good performance with a switch."],
           ["The whole network depends on the hub / switch; if it fails, all devices stop.", "More cable than bus or ring.",
            "Cost of the hub / switch; number of devices limited by hub ports."],
           ["Install, configure, device ઉમેરવું કે કાઢવું સહેલું.", "એક link કે device બગડે તો માત્ર તે device પર અસર.",
            "Hub પરથી fault શોધવો અને અલગ કરવો સહેલો.", "Mesh કરતાં ઓછો cable; દરેક device ને એક જ port જોઈએ.", "Switch સાથે સારી performance."],
           ["આખું network hub / switch પર આધારિત; તે બગડે તો બધા devices બંધ.", "Bus કે ring કરતાં વધુ cable.",
            "Hub / switch નો ખર્ચ; devices ની સંખ્યા hub ports થી મર્યાદિત."])
RING = adv(["Equal access for all devices (token); no collisions.", "Easy to install and reconfigure: adding a device changes only two links.",
            "Each device acts as a repeater, so signal is regenerated; good for long distance.", "Fault isolation is simple (a device can raise an alarm if no signal is received)."],
           ["A break in the ring or failure of one device can stop the whole network (unidirectional ring).", "Adding or removing a device disturbs the network.",
            "Delay increases with the number of devices since data passes through every device."],
           ["બધા devices ને સરખો access (token); collisions નહીં.", "Install અને reconfigure સહેલું: device ઉમેરવાથી માત્ર બે links બદલાય.",
            "દરેક device repeater તરીકે કામ કરે, signal ફરી મજબૂત થાય; લાંબા અંતર માટે સારું.", "Fault શોધવો સરળ (signal ન મળે તો device alarm આપે)."],
           ["Ring માં break કે એક device બગડે તો આખું network બંધ થઈ શકે (unidirectional ring).", "Device ઉમેરવા કે કાઢવાથી network ખોરવાય.",
            "Data દરેક device માંથી પસાર થતો હોવાથી devices વધતાં delay વધે."])
MESH = adv(["Dedicated links: no traffic problem, high speed.", "Robust: if one link fails, others still work (alternate paths).",
            "Privacy and security: data travels only on the dedicated link.", "Easy fault identification and isolation."],
           ["Very costly: large amount of cable and many I/O ports.", "Installation and reconnection are difficult.", "Bulk of wiring may need more space than available."],
           ["Dedicated links: traffic સમસ્યા નહીં, વધુ speed.", "Robust: એક link બગડે તો બીજા કામ કરે (વૈકલ્પિક માર્ગો).",
            "Privacy અને security: data માત્ર dedicated link પર જાય.", "Fault ઓળખવો અને અલગ કરવો સહેલો."],
           ["ખૂબ ખર્ચાળ: ઘણો cable અને ઘણા I/O ports.", "Installation અને ફરી જોડાણ મુશ્કેલ.", "વધુ wiring માટે ઉપલબ્ધ કરતાં વધુ જગ્યા જોઈએ."])
TREE = adv(["Easy to expand by adding new branches (scalable).", "Fault in one branch does not affect other branches.",
            "Point-to-point wiring for each segment; easy management in hierarchy.", "Supported by many hardware vendors."],
           ["If the root (central) hub or backbone fails, the network below it stops.", "More cable than bus; difficult to configure as it grows.", "Costly hubs."],
           ["નવી branches ઉમેરી વિસ્તારવું સહેલું (scalable).", "એક branch નો fault બીજી branches ને અસર ન કરે.",
            "દરેક segment માટે point-to-point wiring; hierarchy માં સહેલું સંચાલન.", "ઘણા hardware vendors support કરે."],
           ["Root (central) hub કે backbone બગડે તો તેની નીચેનું network બંધ.", "Bus કરતાં વધુ cable; મોટું થાય તેમ configure કરવું મુશ્કેલ.", "Hubs ખર્ચાળ."])
HYB = adv(["Flexible: the best topology can be used for each part.", "Reliable: faults are limited to one part and easy to detect.", "Scalable: easy to add new networks."],
          ["Complex design and management.", "Costly: needs intelligent hubs and more cabling."],
          ["Flexible: દરેક ભાગ માટે શ્રેષ્ઠ topology વાપરી શકાય.", "Reliable: faults એક ભાગ પૂરતા રહે અને શોધવા સહેલા.", "Scalable: નવા networks ઉમેરવા સહેલા."],
          ["જટિલ design અને સંચાલન.", "ખર્ચાળ: intelligent hubs અને વધુ cabling જોઈએ."])


SEC_1_3 = {
    "title": {"en": "1.3 Network Topology", "gu": "1.3 Network Topology"},
    "items": [
        T("1.3.1 Network Topology and Bus Topology", "1.3.1 Network Topology અને Bus Topology",
          """<p><b>Network topology</b> is the <b>geometric arrangement</b> of devices (nodes) and the links connecting them in a network. <b>Physical topology</b> is the actual layout of cables and devices; <b>logical topology</b> is the way data flows between devices.</p>
<p><b>Use of topology:</b> it decides the cost, the amount of cable, the speed, the reliability, the ease of installation and fault detection, and how easily the network can grow. The basic topologies are bus, star, ring and mesh; tree and hybrid are combinations.</p>
<h4>Bus topology</h4>
<p>All devices are connected to a <b>single main cable called the backbone (bus)</b>. Each device is attached to the backbone by a <b>drop line</b> and a <b>tap</b> (connector). It is a <b>multipoint</b> configuration. A signal sent by one device travels along the backbone in both directions and is received by all devices; only the addressed device accepts it. <b>Terminators</b> at both ends absorb the signal to stop reflection.</p>
<p><b>Use:</b> early Ethernet LANs (10Base2 / 10Base5 coaxial), small temporary networks, cable TV distribution.</p>
""" + BUS[0],
          """<p><b>Network topology</b> એ network માં devices (nodes) અને તેમને જોડતા links ની <b>ભૌમિતિક ગોઠવણી</b> છે. <b>Physical topology</b> એ cables અને devices ની ખરેખર ગોઠવણી છે; <b>logical topology</b> એ devices વચ્ચે data કેવી રીતે વહે છે તે છે.</p>
<p><b>Topology નો ઉપયોગ:</b> તે ખર્ચ, cable નું પ્રમાણ, speed, reliability, installation અને fault detection ની સરળતા, અને network કેટલું સહેલાઈથી વધી શકે તે નક્કી કરે છે. મૂળભૂત topologies bus, star, ring અને mesh છે; tree અને hybrid તેમનાં સંયોજનો છે.</p>
<h4>Bus topology</h4>
<p>બધા devices <b>backbone (bus) નામના એક મુખ્ય cable</b> સાથે જોડાયેલા હોય છે. દરેક device <b>drop line</b> અને <b>tap</b> (connector) વડે backbone સાથે જોડાય છે. તે <b>multipoint</b> configuration છે. એક device નો signal backbone પર બંને દિશામાં જાય છે અને બધા devices ને મળે છે; માત્ર જેનું address હોય તે device સ્વીકારે છે. બંને છેડે <b>terminators</b> reflection અટકાવવા signal શોષી લે છે.</p>
<p><b>ઉપયોગ:</b> શરૂઆતના Ethernet LANs (10Base2 / 10Base5 coaxial), નાના કામચલાઉ networks, cable TV distribution.</p>
""" + BUS[1],
          diagram="cn1_bus"),
        T("1.3.2 Star Topology", "1.3.2 Star Topology",
          """<p>In a star topology each device has a <b>dedicated point-to-point link only to a central device</b>, a <b>hub or switch</b>. Devices are not directly linked to each other; all traffic passes through the central device. If one device wants to send data to another, it sends it to the hub, which forwards it to the destination (a switch sends it only to the destination port).</p>
<p><b>Use:</b> the most common topology in modern LANs: college labs, offices and homes (Ethernet with UTP cables and a switch, Wi-Fi with an access point).</p>
""" + STAR[0],
          """<p>Star topology માં દરેક device પાસે <b>માત્ર central device</b>, એટલે કે <b>hub કે switch</b> સુધી <b>dedicated point-to-point link</b> હોય છે. Devices એકબીજા સાથે સીધા જોડાયેલા નથી; બધો traffic central device માંથી પસાર થાય છે. એક device બીજાને data મોકલવા ઇચ્છે તો તે hub ને મોકલે, જે destination ને forward કરે (switch માત્ર destination port પર મોકલે).</p>
<p><b>ઉપયોગ:</b> આધુનિક LANs માં સૌથી સામાન્ય topology: college labs, offices અને ઘરો (UTP cables અને switch સાથે Ethernet, access point સાથે Wi-Fi).</p>
""" + STAR[1],
          diagram="cn1_star"),
        T("1.3.3 Ring Topology", "1.3.3 Ring Topology",
          """<p>In a ring topology each device has a dedicated point-to-point connection with <b>only the two devices on either side</b> of it, forming a closed loop (ring). A signal travels around the ring in <b>one direction</b>, from device to device, until it reaches its destination. Each device contains a <b>repeater</b> that regenerates the signal and passes it on.</p>
<p>Access is usually controlled by a <b>token</b>: a special frame that circulates around the ring; only the device holding the token can send data. A <b>dual ring</b> (two rings in opposite directions, e.g. FDDI) keeps working even if one ring breaks.</p>
<p><b>Use:</b> IBM Token Ring LAN, FDDI, SONET fiber rings in MAN / telecom backbones.</p>
""" + RING[0],
          """<p>Ring topology માં દરેક device પાસે <b>તેની બંને બાજુના માત્ર બે devices</b> સાથે dedicated point-to-point જોડાણ હોય છે, જે બંધ loop (ring) બનાવે છે. Signal ring પર <b>એક દિશામાં</b> device થી device જાય છે, destination સુધી પહોંચે ત્યાં સુધી. દરેક device માં <b>repeater</b> હોય છે જે signal ફરી મજબૂત બનાવી આગળ મોકલે.</p>
<p>Access સામાન્ય રીતે <b>token</b> થી નિયંત્રિત થાય છે: ring પર ફરતો ખાસ frame; token ધરાવતું device જ data મોકલી શકે. <b>Dual ring</b> (વિરુદ્ધ દિશામાં બે rings, દા.ત. FDDI) એક ring તૂટે તો પણ કામ ચાલુ રાખે.</p>
<p><b>ઉપયોગ:</b> IBM Token Ring LAN, FDDI, MAN / telecom backbones માં SONET fiber rings.</p>
""" + RING[1],
          diagram="cn1_ring"),
        T("1.3.4 Mesh Topology", "1.3.4 Mesh Topology",
          """<p>In a (fully connected) mesh topology <b>every device has a dedicated point-to-point link to every other device</b>. A link carries traffic only between the two devices it connects.</p>
<h4>Formulas for n devices</h4>
<ul><li>Number of links (cables) = <b>n(n-1)/2</b> (duplex links)</li><li>Ports (I/O) per device = <b>n-1</b></li><li>Total ports in the network = <b>n(n-1)</b></li></ul>
<p>Example: for 6 devices, links = 6×5/2 = <b>15</b>, ports per device = <b>5</b>, total ports = <b>30</b>. In a <b>partial mesh</b>, only important devices are fully connected.</p>
<p><b>Use:</b> Internet backbone between routers, connecting the main offices of a bank, WAN links between telephone exchanges, wireless mesh networks.</p>
""" + MESH[0],
          """<p>(Fully connected) mesh topology માં <b>દરેક device પાસે બીજા દરેક device સુધી dedicated point-to-point link</b> હોય છે. Link માત્ર તે જોડતા બે devices વચ્ચેનો traffic લઈ જાય છે.</p>
<h4>n devices માટેનાં સૂત્રો</h4>
<ul><li>Links (cables) ની સંખ્યા = <b>n(n-1)/2</b> (duplex links)</li><li>Device દીઠ ports (I/O) = <b>n-1</b></li><li>Network માં કુલ ports = <b>n(n-1)</b></li></ul>
<p>ઉદાહરણ: 6 devices માટે, links = 6×5/2 = <b>15</b>, device દીઠ ports = <b>5</b>, કુલ ports = <b>30</b>. <b>Partial mesh</b> માં માત્ર મહત્વના devices જ fully connected હોય છે.</p>
<p><b>ઉપયોગ:</b> routers વચ્ચે Internet backbone, bank ની મુખ્ય offices જોડવી, telephone exchanges વચ્ચે WAN links, wireless mesh networks.</p>
""" + MESH[1],
          diagram="cn1_mesh", examples=["cn1n2", "cn1n3"]),
        T("1.3.5 Tree Topology", "1.3.5 Tree Topology",
          """<p>A tree topology is a <b>hierarchical</b> arrangement and a variation of star. Devices are connected to <b>secondary hubs</b>, and the secondary hubs are connected to a <b>central (root) hub</b>. It can also be seen as several star networks connected by a bus backbone. The central hub is active (repeats the signal); secondary hubs may be active or passive.</p>
<p><b>Use:</b> large organisations and campuses: each department / floor has its own hub (star), and all are connected to the main hub; cable TV networks.</p>
""" + TREE[0],
          """<p>Tree topology એ <b>hierarchical</b> ગોઠવણી અને star નો પ્રકાર છે. Devices <b>secondary hubs</b> સાથે જોડાય, અને secondary hubs <b>central (root) hub</b> સાથે જોડાય. તેને bus backbone થી જોડાયેલા ઘણા star networks તરીકે પણ જોઈ શકાય. Central hub active (signal repeat કરે) હોય; secondary hubs active કે passive હોઈ શકે.</p>
<p><b>ઉપયોગ:</b> મોટી સંસ્થાઓ અને campuses: દરેક department / floor નું પોતાનું hub (star), અને બધા મુખ્ય hub સાથે જોડાયેલા; cable TV networks.</p>
""" + TREE[1],
          diagram="cn1_tree"),
        T("1.3.6 Hybrid Topology", "1.3.6 Hybrid Topology",
          """<p>A hybrid topology is a <b>combination of two or more different basic topologies</b> (e.g. star + ring, star + bus). The resulting network does not follow any single standard topology. Example: each department of a college uses a star LAN, and the department switches are connected by a bus or ring backbone.</p>
<p><b>Use:</b> large organisations, universities, the Internet itself (mixture of all topologies).</p>
""" + HYB[0],
          """<p>Hybrid topology એ <b>બે કે વધુ જુદી મૂળભૂત topologies નું સંયોજન</b> છે (દા.ત. star + ring, star + bus). પરિણામી network કોઈ એક standard topology ને અનુસરતું નથી. ઉદાહરણ: college ના દરેક department માં star LAN, અને department switches bus કે ring backbone થી જોડાયેલા.</p>
<p><b>ઉપયોગ:</b> મોટી સંસ્થાઓ, universities, Internet પોતે (બધી topologies નું મિશ્રણ).</p>
""" + HYB[1],
          diagram="cn1_hybrid"),
        T("1.3.7 Comparison of Topologies (Practical 1)", "1.3.7 Topologies ની સરખામણી (Practical 1)",
          """<p>The number of cables (links) and ports depends on the topology. For <b>n</b> devices:</p>
""" + TOPO_CMP_EN + """
<h4>Practical 1: six devices</h4>
<ul><li><b>Bus:</b> 1 backbone + 6 drop lines; 1 port per device; total 6 ports.</li><li><b>Ring:</b> 6 cables; 2 ports per device; total 12 ports.</li><li><b>Star:</b> 6 cables; 1 port per device + 6 ports on the hub; total 12 ports.</li><li><b>Mesh:</b> 15 cables; 5 ports per device; total 30 ports.</li></ul>
<h4>Choosing a topology</h4>
<p>Small lab or office → <b>star</b> (easy, reliable). Very reliable backbone → <b>mesh</b> (partial). Big campus → <b>tree / hybrid</b>. Low-cost temporary network → <b>bus</b>.</p>""",
          """<p>Cables (links) અને ports ની સંખ્યા topology પર આધાર રાખે છે. <b>n</b> devices માટે:</p>
""" + TOPO_CMP_GU + """
<h4>Practical 1: છ devices</h4>
<ul><li><b>Bus:</b> 1 backbone + 6 drop lines; device દીઠ 1 port; કુલ 6 ports.</li><li><b>Ring:</b> 6 cables; device દીઠ 2 ports; કુલ 12 ports.</li><li><b>Star:</b> 6 cables; device દીઠ 1 port + hub પર 6 ports; કુલ 12 ports.</li><li><b>Mesh:</b> 15 cables; device દીઠ 5 ports; કુલ 30 ports.</li></ul>
<h4>Topology ની પસંદગી</h4>
<p>નાની lab કે office → <b>star</b> (સહેલું, વિશ્વસનીય). ખૂબ વિશ્વસનીય backbone → <b>mesh</b> (partial). મોટું campus → <b>tree / hybrid</b>. ઓછા ખર્ચનું કામચલાઉ network → <b>bus</b>.</p>""",
          examples=["cn1n1", "cn1n4", "cn1n5", "cn1n6"]),
    ]}

SEC_1_4 = {
    "title": {"en": "1.4 Standard Organizations and Protocols", "gu": "1.4 Standard Organizations અને Protocols"},
    "items": [
        T("1.4.1 Protocols", "1.4.1 Protocols",
          """<p>A <b>protocol</b> is a <b>set of rules</b> that governs data communication: it defines <b>what</b> is communicated, <b>how</b> it is communicated and <b>when</b> it is communicated. Two devices may be connected, but they can communicate only if they follow the same protocol (like two people need a common language).</p>
<h4>Key elements of a protocol</h4>
<ol><li><b>Syntax:</b> the structure or format of the data: the order of fields. e.g. first 8 bits = sender address, next 8 bits = receiver address, rest = message.</li><li><b>Semantics:</b> the meaning of each section of bits: how a pattern is interpreted and what action is taken (e.g. does an address identify the route or the final destination?).</li><li><b>Timing:</b> <b>when</b> data should be sent and <b>how fast</b>; e.g. if the sender sends at 100 Mbps and the receiver can handle only 1 Mbps, data will be lost.</li></ol>
<h4>Standards</h4>
<p>A <b>standard</b> is an agreed specification that makes equipment of different manufacturers work together (<b>interoperability</b>). <b>De facto</b> standards are adopted through wide use without formal approval (e.g. early TCP/IP); <b>de jure</b> standards are approved by an official body (e.g. IEEE 802.3).</p>
<h4>Common protocols</h4>
""" + PROTO_EN,
          """<p><b>Protocol</b> એ data communication નિયંત્રિત કરતા <b>નિયમોનો સમૂહ</b> છે: તે નક્કી કરે છે કે <b>શું</b> communicate થાય, <b>કેવી રીતે</b> થાય અને <b>ક્યારે</b> થાય. બે devices જોડાયેલા હોય, પરંતુ એક જ protocol અનુસરે ત્યારે જ વાતચીત કરી શકે (જેમ બે વ્યક્તિઓને સામાન્ય ભાષા જોઈએ).</p>
<h4>Protocol ના મુખ્ય તત્વો</h4>
<ol><li><b>Syntax:</b> data નું structure કે format: fields નો ક્રમ. દા.ત. પહેલા 8 bits = sender address, પછીના 8 bits = receiver address, બાકી = message.</li><li><b>Semantics:</b> bits ના દરેક ભાગનો અર્થ: pattern નું અર્થઘટન કેવી રીતે થાય અને કઈ ક્રિયા થાય (દા.ત. address route ઓળખે છે કે અંતિમ destination?).</li><li><b>Timing:</b> data <b>ક્યારે</b> મોકલવો અને <b>કેટલી ઝડપે</b>; દા.ત. sender 100 Mbps પર મોકલે અને receiver માત્ર 1 Mbps સંભાળી શકે તો data ખોવાય.</li></ol>
<h4>Standards</h4>
<p><b>Standard</b> એ સંમત specification છે જે જુદા manufacturers ના સાધનોને સાથે કામ કરાવે છે (<b>interoperability</b>). <b>De facto</b> standards formal મંજૂરી વગર વ્યાપક ઉપયોગથી અપનાવાય (દા.ત. શરૂઆતનું TCP/IP); <b>de jure</b> standards સત્તાવાર સંસ્થા મંજૂર કરે (દા.ત. IEEE 802.3).</p>
<h4>સામાન્ય protocols</h4>
""" + PROTO_GU),
        T("1.4.2 Standard Organizations: IEEE, ISOC, IETF, ISO, IRTF", "1.4.2 Standard Organizations: IEEE, ISOC, IETF, ISO, IRTF",
          """<p>Standards are developed by <b>standard creation committees</b>, <b>forums</b> and <b>regulatory agencies</b>. The important organisations for computer networks are:</p>
""" + ORG_EN + """
<h4>Internet standards process</h4>
<p>A specification starts as an <b>Internet Draft</b> (working document, valid for 6 months). If recommended, it is published as an <b>RFC</b>. An RFC moves through maturity levels: <b>Proposed Standard</b> → <b>Internet Standard</b>. The <b>IAB (Internet Architecture Board)</b> gives technical oversight; <b>ICANN</b> manages domain names and IP address allocation.</p>
<p>Other bodies: <b>ITU-T</b> (telecommunication standards), <b>ANSI</b> (American National Standards Institute), <b>EIA/TIA</b> (cabling standards such as the T568A / T568B colour codes for UTP).</p>""",
          """<p>Standards <b>standard creation committees</b>, <b>forums</b> અને <b>regulatory agencies</b> બનાવે છે. Computer networks માટે મહત્વની organisations:</p>
""" + ORG_GU + """
<h4>Internet standards ની પ્રક્રિયા</h4>
<p>Specification <b>Internet Draft</b> (કામચલાઉ document, 6 મહિના માન્ય) તરીકે શરૂ થાય. ભલામણ થાય તો <b>RFC</b> તરીકે પ્રકાશિત થાય. RFC maturity levels માંથી પસાર થાય: <b>Proposed Standard</b> → <b>Internet Standard</b>. <b>IAB (Internet Architecture Board)</b> technical દેખરેખ રાખે; <b>ICANN</b> domain names અને IP address ફાળવણી સંભાળે.</p>
<p>બીજી સંસ્થાઓ: <b>ITU-T</b> (telecommunication standards), <b>ANSI</b> (American National Standards Institute), <b>EIA/TIA</b> (UTP માટે T568A / T568B colour codes જેવા cabling standards).</p>"""),
    ]}

SEC_1_5 = {
    "title": {"en": "1.5 Types of Servers", "gu": "1.5 Servers ના પ્રકારો"},
    "items": [
        T("1.5.1 Servers: File Server, Print Server, Mail Server", "1.5.1 Servers: File Server, Print Server, Mail Server",
          """<p>In a <b>client-server network</b>, a <b>server</b> is a powerful computer (or software) that <b>provides services</b> to other computers called <b>clients</b>. Clients send requests; the server processes them and sends replies. A server has a fast processor, large RAM and storage, a reliable power supply and a server operating system (Windows Server, Linux). (In a <b>peer-to-peer</b> network, every computer is both client and server.)</p>
<h4>1. File server</h4>
<p>Stores files centrally and lets authorised clients <b>store, retrieve, share and update files</b> over the network.</p>
<ul><li><b>Features:</b> central storage, user accounts and access permissions (read / write), file locking for shared files, quotas, regular backup, RAID disks for reliability.</li><li><b>Applications:</b> shared folders in an office or lab, project files of a team, home directories of students.</li></ul>
<h4>2. Print server</h4>
<p>Manages one or more printers and lets many clients <b>share them</b>. Print jobs are received, stored in a <b>print queue (spooling)</b> and sent to the printer one by one.</p>
<ul><li><b>Features:</b> print queue management (pause, cancel, priority), sharing costly printers, user-wise accounting and limits, status reporting (paper out, error).</li><li><b>Applications:</b> one laser printer shared by all PCs in a lab or office.</li></ul>
<h4>3. Mail server</h4>
<p>Stores, sends and receives <b>e-mail</b> for users. It works like a post office: an <b>outgoing (SMTP) server</b> sends mail to the receiver's mail server, and the receiver reads it from the <b>incoming server</b> using <b>POP3</b> (download) or <b>IMAP</b> (keep on server, sync on all devices).</p>
<ul><li><b>Features:</b> user mailboxes, spam and virus filtering, attachments, address books, auto-reply.</li><li><b>Applications:</b> Gmail, Outlook / Microsoft Exchange, college and company e-mail.</li></ul>""",
          """<p><b>Client-server network</b> માં <b>server</b> એ શક્તિશાળી computer (કે software) છે જે <b>clients</b> નામના બીજા computers ને <b>સેવાઓ આપે</b> છે. Clients requests મોકલે; server તેની પ્રક્રિયા કરી જવાબ મોકલે. Server માં ઝડપી processor, મોટી RAM અને storage, વિશ્વસનીય power supply અને server operating system (Windows Server, Linux) હોય છે. (<b>Peer-to-peer</b> network માં દરેક computer client અને server બંને હોય.)</p>
<h4>1. File server</h4>
<p>Files કેન્દ્રિય રીતે રાખે અને અધિકૃત clients ને network પર <b>files store, retrieve, share અને update</b> કરવા દે.</p>
<ul><li><b>Features:</b> central storage, user accounts અને access permissions (read / write), shared files માટે file locking, quotas, નિયમિત backup, reliability માટે RAID disks.</li><li><b>ઉપયોગો:</b> office કે lab માં shared folders, team ની project files, students ની home directories.</li></ul>
<h4>2. Print server</h4>
<p>એક કે વધુ printers સંભાળે અને ઘણા clients ને <b>તે વહેંચવા</b> દે. Print jobs મેળવી <b>print queue (spooling)</b> માં રાખે અને એક પછી એક printer ને મોકલે.</p>
<ul><li><b>Features:</b> print queue management (pause, cancel, priority), મોંઘા printers ની વહેંચણી, user પ્રમાણે હિસાબ અને મર્યાદા, status reporting (paper out, error).</li><li><b>ઉપયોગો:</b> lab કે office ના બધા PCs વહેંચતા એક laser printer.</li></ul>
<h4>3. Mail server</h4>
<p>Users માટે <b>e-mail</b> store કરે, મોકલે અને મેળવે. તે post office જેવું કામ કરે: <b>outgoing (SMTP) server</b> receiver ના mail server ને mail મોકલે, અને receiver <b>incoming server</b> પરથી <b>POP3</b> (download) કે <b>IMAP</b> (server પર રાખે, બધા devices પર sync) વડે વાંચે.</p>
<ul><li><b>Features:</b> user mailboxes, spam અને virus filtering, attachments, address books, auto-reply.</li><li><b>ઉપયોગો:</b> Gmail, Outlook / Microsoft Exchange, college અને company e-mail.</li></ul>""",
          diagram="cn1_client_server"),
        T("1.5.2 Web Server and Proxy Server", "1.5.2 Web Server અને Proxy Server",
          """<h4>4. Web server</h4>
<p>Stores <b>websites</b> (HTML pages, images, scripts) and delivers them to clients' <b>web browsers</b> using <b>HTTP / HTTPS</b>. The browser sends a request for a URL; the web server finds the page (or generates it using PHP, Java, Python with a database) and sends it back.</p>
<ul><li><b>Features:</b> handles thousands of requests at once, static and dynamic pages, HTTPS security (SSL/TLS certificates), virtual hosting (many websites on one server), logging.</li><li><b>Applications:</b> hosting college, company and e-commerce websites. Software: Apache, Nginx, Microsoft IIS.</li></ul>
<h4>5. Proxy server</h4>
<p>An <b>intermediary</b> between clients and the Internet. The client sends its request to the proxy; the proxy forwards it to the web server on behalf of the client, receives the reply and passes it back.</p>
<ul><li><b>Caching:</b> frequently visited pages are stored; the next request is served from the cache (faster, saves bandwidth).</li><li><b>Filtering / access control:</b> blocks unwanted websites (used in colleges and offices).</li><li><b>Privacy:</b> hides clients' IP addresses from outside servers.</li><li><b>Logging and monitoring</b> of Internet use; <b>sharing</b> one Internet connection.</li><li><b>Applications:</b> college / office Internet gateway (Squid), anonymous browsing, load balancing (reverse proxy in front of web servers).</li></ul>
<h4>Summary of servers</h4>
""" + SRV_EN,
          """<h4>4. Web server</h4>
<p><b>Websites</b> (HTML pages, images, scripts) store કરે અને <b>HTTP / HTTPS</b> વડે clients ના <b>web browsers</b> ને આપે. Browser URL માટે request મોકલે; web server page શોધે (કે database સાથે PHP, Java, Python વડે બનાવે) અને પાછું મોકલે.</p>
<ul><li><b>Features:</b> એક સાથે હજારો requests સંભાળે, static અને dynamic pages, HTTPS security (SSL/TLS certificates), virtual hosting (એક server પર ઘણી websites), logging.</li><li><b>ઉપયોગો:</b> college, company અને e-commerce websites hosting. Software: Apache, Nginx, Microsoft IIS.</li></ul>
<h4>5. Proxy server</h4>
<p>Clients અને Internet વચ્ચેનો <b>મધ્યસ્થી</b>. Client પોતાની request proxy ને મોકલે; proxy client વતી web server ને forward કરે, જવાબ મેળવી પાછો આપે.</p>
<ul><li><b>Caching:</b> વારંવાર જોવાતાં pages સંગ્રહાય; બીજી request cache માંથી પૂરી થાય (ઝડપી, bandwidth બચે).</li><li><b>Filtering / access control:</b> અનિચ્છનીય websites block કરે (colleges અને offices માં વપરાય).</li><li><b>Privacy:</b> બહારના servers થી clients ના IP addresses છુપાવે.</li><li>Internet ઉપયોગનું <b>logging અને monitoring</b>; એક Internet connection ની <b>વહેંચણી</b>.</li><li><b>ઉપયોગો:</b> college / office Internet gateway (Squid), anonymous browsing, load balancing (web servers આગળ reverse proxy).</li></ul>
<h4>Servers નો સારાંશ</h4>
""" + SRV_GU,
          diagram="cn1_proxy"),
    ]}
