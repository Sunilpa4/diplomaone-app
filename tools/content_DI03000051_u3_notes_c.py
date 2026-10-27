"""Computer Networks (DI03000051) - Unit 3 notes part C: 3.3 Network devices."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

HS_EN = tbl(["Hub", "Switch"], [
    ("Physical layer (layer 1) device", "Data link layer (layer 2) device"),
    ("Works with electrical signals / bits", "Works with frames and MAC addresses"),
    ("Broadcasts data to all ports", "Sends data only to the destination port (unicast)"),
    ("One collision domain for all ports", "Each port is a separate collision domain"),
    ("Half duplex; bandwidth shared", "Full duplex; dedicated bandwidth per port"),
    ("No memory / table", "Stores a MAC address table (CAM table)"),
    ("Less secure, cheap, now obsolete", "More secure, faster, used in all LANs")])
HS_GU = tbl(["Hub", "Switch"], [
    ("Physical layer (layer 1) device", "Data link layer (layer 2) device"),
    ("Electrical signals / bits સાથે કામ કરે", "Frames અને MAC addresses સાથે કામ કરે"),
    ("Data બધા ports પર broadcast કરે", "Data ફક્ત destination port પર મોકલે (unicast)"),
    ("બધા ports માટે એક collision domain", "દરેક port અલગ collision domain"),
    ("Half duplex; bandwidth વહેંચાય", "Full duplex; port દીઠ dedicated bandwidth"),
    ("Memory / table નહીં", "MAC address table (CAM table) રાખે"),
    ("ઓછું secure, સસ્તું, હવે જૂનું", "વધુ secure, ઝડપી, બધા LANs માં વપરાય")])

SR_EN = tbl(["Switch", "Router"], [
    ("Layer 2 (data link)", "Layer 3 (network)"), ("Uses MAC address", "Uses IP address"),
    ("Connects devices within one LAN", "Connects different networks (LAN to LAN / WAN / Internet)"),
    ("MAC address table", "Routing table"), ("One broadcast domain", "Each interface is a separate broadcast domain"),
    ("Cannot do NAT or choose paths", "Performs NAT, best path selection, firewall / DHCP")])
SR_GU = tbl(["Switch", "Router"], [
    ("Layer 2 (data link)", "Layer 3 (network)"), ("MAC address વાપરે", "IP address વાપરે"),
    ("એક LAN ની અંદર devices જોડે", "જુદા networks જોડે (LAN થી LAN / WAN / Internet)"),
    ("MAC address table", "Routing table"), ("એક broadcast domain", "દરેક interface અલગ broadcast domain"),
    ("NAT કે paths પસંદ ન કરી શકે", "NAT, best path selection, firewall / DHCP કરે")])

L23_EN = tbl(["Layer 2 switch", "Layer 3 switch"], [
    ("Works at data link layer", "Works at data link + network layer"),
    ("Forwards frames using MAC addresses", "Forwards using MAC and routes using IP addresses"),
    ("Cannot route between VLANs; needs an external router", "Inter-VLAN routing inside the switch"),
    ("One broadcast domain (unless VLANs)", "Breaks broadcast domains"),
    ("Cheaper, simple", "Costlier, more features (routing protocols, ACL)"),
    ("Used at access layer (connect PCs)", "Used at distribution / core layer of campus networks")])
L23_GU = tbl(["Layer 2 switch", "Layer 3 switch"], [
    ("Data link layer પર કામ કરે", "Data link + network layer પર કામ કરે"),
    ("MAC addresses વાપરી frames forward કરે", "MAC થી forward અને IP addresses થી route કરે"),
    ("VLANs વચ્ચે route ન કરી શકે; બહારનું router જોઈએ", "Switch ની અંદર inter-VLAN routing"),
    ("એક broadcast domain (VLANs સિવાય)", "Broadcast domains તોડે"),
    ("સસ્તું, સરળ", "મોંઘું, વધુ features (routing protocols, ACL)"),
    ("Access layer પર વપરાય (PCs જોડવા)", "Campus networks ના distribution / core layer પર વપરાય")])

DEV_EN = tbl(["Device", "OSI layer", "Address used", "Domains"], [
    ("Repeater, Hub", "1 Physical", "None", "1 collision, 1 broadcast"),
    ("NIC", "1 + 2", "MAC (burned in)", "-"),
    ("Bridge, Switch, AP", "2 Data link", "MAC", "Separate collision, 1 broadcast"),
    ("Router, L3 switch", "3 Network", "IP", "Separate collision and broadcast"),
    ("Gateway", "4 to 7 (all)", "Protocol conversion", "-")])
DEV_GU = tbl(["Device", "OSI layer", "વપરાતું address", "Domains"], [
    ("Repeater, Hub", "1 Physical", "કોઈ નહીં", "1 collision, 1 broadcast"),
    ("NIC", "1 + 2", "MAC (burned in)", "-"),
    ("Bridge, Switch, AP", "2 Data link", "MAC", "અલગ collision, 1 broadcast"),
    ("Router, L3 switch", "3 Network", "IP", "અલગ collision અને broadcast"),
    ("Gateway", "4 થી 7 (બધા)", "Protocol conversion", "-")])

RTR_AD = adv(["Connects different networks and the Internet; chooses the best path.", "Separates broadcast domains, reducing traffic.", "Provides security features: NAT, firewall, access lists."],
             ["Costlier than switches and hubs.", "Slower: must examine IP headers and look up the routing table.", "Needs configuration by a skilled administrator."],
             ["જુદા networks અને Internet જોડે; best path પસંદ કરે.", "Broadcast domains અલગ કરે, traffic ઘટાડે.", "Security features આપે: NAT, firewall, access lists."],
             ["Switches અને hubs કરતાં મોંઘું.", "ધીમું: IP headers તપાસી routing table જોવું પડે.", "કુશળ administrator દ્વારા configuration જોઈએ."])

SEC_3_3 = {
    "title": {"en": "3.3 Network Devices", "gu": "3.3 Network Devices"},
    "items": [
        T("3.3.1 Repeater", "3.3.1 Repeater",
          """<p>A <b>repeater</b> is a <b>physical layer</b> device that receives a signal, and before it becomes too weak or corrupted, <b>regenerates</b> the original bit pattern and sends the refreshed copy onward. It extends the physical length of a LAN (e.g. a UTP segment is limited to 100 m).</p>
<ul>
<li>A repeater <b>regenerates</b>, it does not simply amplify: an amplifier boosts noise along with the signal, while a repeater recreates a clean signal.</li>
<li>It has <b>no filtering</b> capability and does not understand addresses; it forwards every bit.</li>
<li>It connects two segments of the <b>same</b> network; both segments form one collision domain.</li>
<li>Placement matters: it must be placed before the signal becomes so weak that bits cannot be recognised.</li>
</ul>
<p><b>Examples:</b> Ethernet repeaters, Wi-Fi range extenders, optical repeaters in long fiber links, microwave relay towers.</p>""",
          """<p><b>Repeater</b> એ <b>physical layer</b> device છે જે signal મેળવે, અને તે ખૂબ નબળું કે બગડેલું થાય તે પહેલાં મૂળ bit pattern <b>ફરી બનાવે (regenerate)</b> અને તાજી copy આગળ મોકલે. તે LAN ની physical લંબાઈ વધારે (દા.ત. UTP segment 100 m સુધી મર્યાદિત).</p>
<ul>
<li>Repeater <b>regenerate</b> કરે, ફક્ત amplify નહીં: amplifier signal સાથે noise પણ વધારે, જ્યારે repeater સ્વચ્છ signal ફરી બનાવે.</li>
<li>તેમાં <b>filtering</b> ક્ષમતા નથી અને addresses સમજતું નથી; દરેક bit forward કરે.</li>
<li>તે <b>એક જ</b> network ના બે segments જોડે; બંને segments એક collision domain બને.</li>
<li>સ્થાન મહત્વનું: bits ઓળખી ન શકાય તેટલું signal નબળું થાય તે પહેલાં મૂકવું જોઈએ.</li>
</ul>
<p><b>ઉદાહરણો:</b> Ethernet repeaters, Wi-Fi range extenders, લાંબા fiber links માં optical repeaters, microwave relay towers.</p>""",
          diagram="cn3_repeater"),
        T("3.3.2 Hub (Active and Passive)", "3.3.2 Hub (Active અને Passive)",
          """<p>A <b>hub</b> is a central connecting device in a <b>star topology</b> LAN. It works at the <b>physical layer</b>. When a signal arrives at one port, the hub sends it out on <b>all other ports</b> (broadcast), so every connected computer receives it and only the addressed one accepts it.</p>
<h4>Types of hub</h4>
<ul>
<li><b>Passive hub:</b> just a connector; it joins wires from different branches without regenerating the signal. It needs no power. Part of the media.</li>
<li><b>Active hub:</b> a <b>multiport repeater</b>; it regenerates and amplifies signals before broadcasting. It needs electric power and can extend the distance.</li>
<li><b>Intelligent (smart) hub:</b> an active hub with management features like monitoring traffic and configuring ports.</li>
</ul>
<h4>Limitations</h4>
<p>All ports share one <b>collision domain</b> and the bandwidth; more computers means more collisions and lower speed. Broadcasting every frame also gives poor security. Hubs have been replaced by switches.</p>""",
          """<p><b>Hub</b> એ <b>star topology</b> LAN માં મધ્યસ્થ જોડાણ device છે. તે <b>physical layer</b> પર કામ કરે. જ્યારે એક port પર signal આવે, hub તેને <b>બાકીના બધા ports</b> પર મોકલે (broadcast), તેથી દરેક જોડાયેલું computer તે મેળવે અને ફક્ત જેને address કર્યું હોય તે સ્વીકારે.</p>
<h4>Hub ના પ્રકારો</h4>
<ul>
<li><b>Passive hub:</b> ફક્ત connector; signal regenerate કર્યા વગર જુદી શાખાઓના વાયર જોડે. Power ની જરૂર નહીં. Media નો ભાગ.</li>
<li><b>Active hub:</b> <b>multiport repeater</b>; broadcast કરતાં પહેલાં signals regenerate અને amplify કરે. Electric power જોઈએ અને અંતર વધારી શકે.</li>
<li><b>Intelligent (smart) hub:</b> traffic monitoring અને ports configure કરવા જેવા management features વાળું active hub.</li>
</ul>
<h4>મર્યાદાઓ</h4>
<p>બધા ports એક <b>collision domain</b> અને bandwidth વહેંચે; વધુ computers એટલે વધુ collisions અને ઓછી ઝડપ. દરેક frame broadcast કરવાથી security પણ નબળી. Hubs ની જગ્યા switches એ લીધી છે.</p>""",
          diagram="cn3_hub_switch"),
        T("3.3.3 Switch", "3.3.3 Switch",
          """<p>A <b>switch</b> is a <b>data link layer</b> (layer 2) device that connects multiple devices in a LAN. It is a <b>multiport bridge</b>. A switch reads the <b>destination MAC address</b> of each frame and forwards the frame <b>only to the port</b> where that device is connected.</p>
<h4>Working</h4>
<ol>
<li><b>Learning:</b> when a frame arrives, the switch records the source MAC address and the incoming port in its <b>MAC address table</b> (CAM table).</li>
<li><b>Forwarding:</b> if the destination MAC is in the table, the frame goes out only on that port.</li>
<li><b>Flooding:</b> if the destination is unknown (or a broadcast), the frame is sent out on all ports except the incoming one.</li>
<li><b>Filtering:</b> if the destination is on the same port as the source, the frame is dropped.</li>
</ol>
<p>Each port is a separate <b>collision domain</b> and works in <b>full duplex</b>, giving every device dedicated bandwidth. Switching methods: <b>store-and-forward</b> (checks the whole frame for errors), <b>cut-through</b> (forwards after reading the destination address, faster), <b>fragment-free</b>.</p>
<h4>Hub vs switch</h4>
""" + HS_EN,
          """<p><b>Switch</b> એ <b>data link layer</b> (layer 2) device છે જે LAN માં અનેક devices જોડે. તે <b>multiport bridge</b> છે. Switch દરેક frame નું <b>destination MAC address</b> વાંચે અને frame <b>ફક્ત તે port</b> પર forward કરે જ્યાં તે device જોડાયેલું છે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ol>
<li><b>Learning:</b> frame આવે ત્યારે switch source MAC address અને incoming port તેના <b>MAC address table</b> (CAM table) માં નોંધે.</li>
<li><b>Forwarding:</b> જો destination MAC table માં હોય, તો frame ફક્ત તે port પર જાય.</li>
<li><b>Flooding:</b> જો destination અજાણ્યું (કે broadcast) હોય, તો frame incoming સિવાયના બધા ports પર મોકલાય.</li>
<li><b>Filtering:</b> જો destination અને source એક જ port પર હોય, તો frame drop થાય.</li>
</ol>
<p>દરેક port અલગ <b>collision domain</b> છે અને <b>full duplex</b> માં કામ કરે, જેથી દરેક device ને dedicated bandwidth મળે. Switching પદ્ધતિઓ: <b>store-and-forward</b> (આખી frame ની errors તપાસે), <b>cut-through</b> (destination address વાંચીને forward કરે, ઝડપી), <b>fragment-free</b>.</p>
<h4>Hub vs switch</h4>
""" + HS_GU),
        T("3.3.4 Bridge", "3.3.4 Bridge",
          """<p>A <b>bridge</b> operates in both the physical and the <b>data link layer</b>. It connects <b>two LAN segments</b> and can <b>filter</b> traffic: it checks the destination MAC address of a frame and decides whether to forward it or drop it.</p>
<ul>
<li>A bridge keeps a <b>bridge (forwarding) table</b> that maps MAC addresses to ports.</li>
<li>If the source and destination are on the same segment, the frame is <b>filtered</b> (not forwarded), which reduces traffic on the other segment.</li>
<li>It divides a LAN into separate <b>collision domains</b> but keeps one broadcast domain.</li>
<li>A bridge does not change the frame's physical (MAC) addresses.</li>
</ul>
<h4>Types</h4>
<ul>
<li><b>Transparent bridge:</b> stations are unaware of the bridge; it builds its table automatically by learning. Uses the Spanning Tree Protocol to prevent loops.</li>
<li><b>Source routing bridge:</b> the sending station decides the path and puts it in the frame (used in Token Ring).</li>
<li><b>Translational bridge:</b> connects LANs of different types (e.g. Ethernet and Token Ring).</li>
</ul>""",
          """<p><b>Bridge</b> physical અને <b>data link layer</b> બંનેમાં કામ કરે. તે <b>બે LAN segments</b> જોડે અને traffic <b>filter</b> કરી શકે: frame નું destination MAC address તપાસી forward કરવું કે drop કરવું તે નક્કી કરે.</p>
<ul>
<li>Bridge MAC addresses ને ports સાથે જોડતું <b>bridge (forwarding) table</b> રાખે.</li>
<li>જો source અને destination એક જ segment પર હોય, તો frame <b>filter</b> થાય (forward નહીં), જે બીજા segment પરનો traffic ઘટાડે.</li>
<li>તે LAN ને અલગ <b>collision domains</b> માં વહેંચે પણ એક broadcast domain રાખે.</li>
<li>Bridge frame ના physical (MAC) addresses બદલતું નથી.</li>
</ul>
<h4>પ્રકારો</h4>
<ul>
<li><b>Transparent bridge:</b> stations ને bridge ની જાણ નથી; learning દ્વારા આપમેળે table બનાવે. Loops અટકાવવા Spanning Tree Protocol વાપરે.</li>
<li><b>Source routing bridge:</b> મોકલનાર station path નક્કી કરી frame માં મૂકે (Token Ring માં વપરાય).</li>
<li><b>Translational bridge:</b> જુદા પ્રકારના LANs જોડે (દા.ત. Ethernet અને Token Ring).</li>
</ul>""",
          diagram="cn3_bridge"),
        T("3.3.5 Router", "3.3.5 Router",
          """<p>A <b>router</b> is a <b>network layer</b> (layer 3) device that connects <b>two or more different networks</b> (e.g. a LAN to another LAN, or a LAN to the Internet). It forwards packets based on the <b>destination IP address</b> using a <b>routing table</b>.</p>
<h4>Working</h4>
<ol>
<li>A packet arrives at an interface; the router reads the destination IP address.</li>
<li>It looks up the routing table to find the best matching network and the outgoing interface / next hop.</li>
<li>It changes the frame's MAC addresses for the next link and forwards the packet. If no route matches, the default route is used or the packet is dropped.</li>
</ol>
<ul>
<li>The routing table can be <b>static</b> (configured manually) or <b>dynamic</b> (learned through routing protocols such as RIP, OSPF, BGP).</li>
<li>Each router interface has its own IP address and is a separate <b>broadcast domain</b>.</li>
<li>Home Wi-Fi routers combine a router, switch, access point, DHCP server, NAT and firewall in one box.</li>
</ul>
""" + RTR_AD[0] + """
<h4>Switch vs router</h4>
""" + SR_EN,
          """<p><b>Router</b> એ <b>network layer</b> (layer 3) device છે જે <b>બે કે વધુ જુદા networks</b> જોડે (દા.ત. LAN ને બીજા LAN સાથે, કે LAN ને Internet સાથે). તે <b>routing table</b> વાપરી <b>destination IP address</b> ના આધારે packets forward કરે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ol>
<li>Packet interface પર આવે; router destination IP address વાંચે.</li>
<li>Best matching network અને outgoing interface / next hop શોધવા routing table જુએ.</li>
<li>આગળની link માટે frame ના MAC addresses બદલી packet forward કરે. જો કોઈ route ન મળે, તો default route વપરાય કે packet drop થાય.</li>
</ol>
<ul>
<li>Routing table <b>static</b> (હાથથી configure) કે <b>dynamic</b> (RIP, OSPF, BGP જેવા routing protocols દ્વારા શીખેલું) હોઈ શકે.</li>
<li>દરેક router interface નું પોતાનું IP address છે અને તે અલગ <b>broadcast domain</b> છે.</li>
<li>ઘરના Wi-Fi routers એક box માં router, switch, access point, DHCP server, NAT અને firewall ભેગા કરે.</li>
</ul>
""" + RTR_AD[1] + """
<h4>Switch vs router</h4>
""" + SR_GU,
          diagram="cn3_router"),
        T("3.3.6 Gateway", "3.3.6 Gateway",
          """<p>A <b>gateway</b> is a device (or software on a computer) that connects <b>two networks that use different protocols</b>. It can work at <b>all seven layers</b> of the OSI model, though it usually operates at the upper layers (transport to application). A gateway is also called a <b>protocol converter</b>.</p>
<ul>
<li>It receives a message in one format, <b>translates</b> it into the format understood by the other network, and forwards it.</li>
<li>It can also provide security (filtering) and act as the entry / exit point of a network.</li>
<li>In TCP/IP terminology, the router that connects a LAN to outside networks is called the <b>default gateway</b>; a PC sends all packets for other networks to it.</li>
</ul>
<h4>Examples</h4>
<ul>
<li><b>Email gateway:</b> converts between different mail systems.</li>
<li><b>VoIP gateway:</b> connects the IP phone network to the traditional telephone network.</li>
<li><b>IoT gateway:</b> converts Zigbee / Bluetooth sensor data to IP for the cloud.</li>
<li><b>Payment gateway</b>, <b>cloud storage gateway</b>, and the <b>print server</b> that lets network users share a printer.</li>
</ul>
<p><b>Router vs gateway:</b> a router connects networks using the <b>same</b> protocol (IP) and selects paths; a gateway connects networks using <b>different</b> protocols and converts between them.</p>""",
          """<p><b>Gateway</b> એ device (કે computer પરનું software) છે જે <b>જુદા protocols વાપરતા બે networks</b> જોડે. તે OSI model ના <b>બધા સાત layers</b> પર કામ કરી શકે, જોકે સામાન્ય રીતે ઉપરના layers (transport થી application) પર કામ કરે. Gateway ને <b>protocol converter</b> પણ કહે છે.</p>
<ul>
<li>તે એક format માં message મેળવે, બીજું network સમજે તે format માં <b>અનુવાદ</b> કરે અને forward કરે.</li>
<li>તે security (filtering) પણ આપી શકે અને network ના પ્રવેશ / નિકાસ બિંદુ તરીકે કામ કરે.</li>
<li>TCP/IP પરિભાષામાં, LAN ને બહારના networks સાથે જોડતા router ને <b>default gateway</b> કહે છે; PC બીજા networks માટેના બધા packets તેને મોકલે.</li>
</ul>
<h4>ઉદાહરણો</h4>
<ul>
<li><b>Email gateway:</b> જુદી mail systems વચ્ચે રૂપાંતર કરે.</li>
<li><b>VoIP gateway:</b> IP phone network ને પરંપરાગત telephone network સાથે જોડે.</li>
<li><b>IoT gateway:</b> Zigbee / Bluetooth sensor data ને cloud માટે IP માં ફેરવે.</li>
<li><b>Payment gateway</b>, <b>cloud storage gateway</b>, અને network users ને printer વહેંચવા દેતું <b>print server</b>.</li>
</ul>
<p><b>Router vs gateway:</b> router <b>સરખા</b> protocol (IP) વાપરતા networks જોડે અને paths પસંદ કરે; gateway <b>જુદા</b> protocols વાપરતા networks જોડે અને તેમની વચ્ચે રૂપાંતર કરે.</p>"""),
        T("3.3.7 Wireless Access Point", "3.3.7 Wireless Access Point",
          """<p>A <b>wireless access point (AP / WAP)</b> is a <b>data link layer</b> device that allows wireless devices (laptops, phones, tablets) to connect to a <b>wired LAN</b> using Wi-Fi (<b>IEEE 802.11</b>). It is connected to a switch or router by a UTP cable and acts as a bridge between wireless and wired networks.</p>
<ul>
<li>It broadcasts a network name called the <b>SSID</b> (Service Set Identifier).</li>
<li>It uses the 2.4 GHz and 5 GHz bands (6 GHz for Wi-Fi 6E / 7); the typical indoor range is about 30-50 m.</li>
<li>It provides security through <b>WPA2 / WPA3</b> encryption and password authentication.</li>
<li>Several APs with the same SSID give coverage across a building or campus; users can roam between them.</li>
<li>Many APs are powered over the Ethernet cable (<b>PoE</b>).</li>
</ul>
<p><b>Modes:</b> root (normal AP), repeater / range extender, bridge (point-to-point link between buildings), client.</p>
<p><b>AP vs Wi-Fi router:</b> an AP only gives wireless access to an existing network, while a Wi-Fi router also performs routing, NAT and DHCP for Internet sharing.</p>""",
          """<p><b>Wireless access point (AP / WAP)</b> એ <b>data link layer</b> device છે જે wireless devices (laptops, phones, tablets) ને Wi-Fi (<b>IEEE 802.11</b>) વાપરીને <b>wired LAN</b> સાથે જોડાવા દે. તે UTP cable થી switch કે router સાથે જોડાય અને wireless અને wired networks વચ્ચે bridge તરીકે કામ કરે.</p>
<ul>
<li>તે <b>SSID</b> (Service Set Identifier) નામનું network નામ broadcast કરે.</li>
<li>તે 2.4 GHz અને 5 GHz bands (Wi-Fi 6E / 7 માટે 6 GHz) વાપરે; સામાન્ય indoor range લગભગ 30-50 m.</li>
<li>તે <b>WPA2 / WPA3</b> encryption અને password authentication દ્વારા security આપે.</li>
<li>સરખા SSID વાળા અનેક APs building કે campus માં coverage આપે; users તેમની વચ્ચે roam કરી શકે.</li>
<li>ઘણા APs ને Ethernet cable દ્વારા power મળે (<b>PoE</b>).</li>
</ul>
<p><b>Modes:</b> root (સામાન્ય AP), repeater / range extender, bridge (buildings વચ્ચે point-to-point link), client.</p>
<p><b>AP vs Wi-Fi router:</b> AP ફક્ત હાલના network ને wireless access આપે, જ્યારે Wi-Fi router Internet sharing માટે routing, NAT અને DHCP પણ કરે.</p>""",
          diagram="cn3_ap"),
        T("3.3.8 Network Interface Card (NIC)", "3.3.8 Network Interface Card (NIC)",
          """<p>A <b>Network Interface Card (NIC)</b>, also called a network adapter or LAN card, is the hardware that connects a computer to a network. It works at the <b>physical and data link layers</b>.</p>
<ul>
<li>Every NIC has a unique 48-bit <b>MAC (physical) address</b> burned into its ROM by the manufacturer, written as 12 hexadecimal digits, e.g. <b>00:1A:2B:3C:4D:5E</b>. The first 24 bits (OUI) identify the manufacturer.</li>
<li>It converts data from the computer (parallel) into signals for the cable or radio (serial), and back.</li>
<li>It frames data, checks errors and controls access to the medium (e.g. CSMA/CD for Ethernet).</li>
<li>It connects to the motherboard through PCIe or USB; today most NICs are built into the motherboard.</li>
</ul>
<h4>Types</h4>
<ul>
<li><b>Wired (Ethernet) NIC:</b> RJ-45 port; 100 Mbps / 1 Gbps / 10 Gbps. LEDs show link and activity.</li>
<li><b>Wireless NIC:</b> Wi-Fi adapter with antenna (internal card or USB dongle).</li>
<li><b>Fiber NIC:</b> SFP port for fiber in servers.</li>
</ul>
<p>The MAC address can be seen with <b>ipconfig /all</b> (Windows) or <b>ip link</b> (Linux).</p>""",
          """<p><b>Network Interface Card (NIC)</b>, જેને network adapter કે LAN card પણ કહે છે, તે computer ને network સાથે જોડતું hardware છે. તે <b>physical અને data link layers</b> પર કામ કરે.</p>
<ul>
<li>દરેક NIC માં manufacturer દ્વારા ROM માં લખેલું અનન્ય 48-bit <b>MAC (physical) address</b> હોય, 12 hexadecimal અંકોમાં લખાય, દા.ત. <b>00:1A:2B:3C:4D:5E</b>. પ્રથમ 24 bits (OUI) manufacturer ઓળખે.</li>
<li>તે computer ના data (parallel) ને cable કે radio માટેના signals (serial) માં અને પાછા ફેરવે.</li>
<li>તે data frame કરે, errors તપાસે અને medium નો access નિયંત્રિત કરે (દા.ત. Ethernet માટે CSMA/CD).</li>
<li>તે PCIe કે USB દ્વારા motherboard સાથે જોડાય; આજે મોટા ભાગના NICs motherboard માં જ હોય.</li>
</ul>
<h4>પ્રકારો</h4>
<ul>
<li><b>Wired (Ethernet) NIC:</b> RJ-45 port; 100 Mbps / 1 Gbps / 10 Gbps. LEDs link અને activity બતાવે.</li>
<li><b>Wireless NIC:</b> antenna વાળું Wi-Fi adapter (internal card કે USB dongle).</li>
<li><b>Fiber NIC:</b> servers માં fiber માટે SFP port.</li>
</ul>
<p>MAC address <b>ipconfig /all</b> (Windows) કે <b>ip link</b> (Linux) થી જોઈ શકાય.</p>""",
          diagram="cn3_nic"),
        T("3.3.9 Layer 2 vs Layer 3 Switch; Devices and OSI Layers", "3.3.9 Layer 2 vs Layer 3 Switch; Devices અને OSI Layers",
          """<p>A <b>layer 2 switch</b> forwards frames using MAC addresses only. A <b>layer 3 switch</b> (multilayer switch) combines a switch and a router: it switches frames within a VLAN using MAC addresses and <b>routes packets between VLANs</b> using IP addresses, in hardware, at wire speed.</p>
""" + L23_EN + """
<h4>Network devices and OSI layers</h4>
<p>A device that works at a higher layer can also perform the jobs of the lower layers (a router also regenerates signals and handles frames).</p>
""" + DEV_EN + """
<p><b>Collision domain:</b> the part of a network where two transmissions at the same time collide. <b>Broadcast domain:</b> the part of a network that receives a broadcast frame. Switches and bridges break collision domains; routers break both.</p>""",
          """<p><b>Layer 2 switch</b> ફક્ત MAC addresses વાપરી frames forward કરે. <b>Layer 3 switch</b> (multilayer switch) switch અને router ભેગા કરે: VLAN ની અંદર MAC addresses વાપરી frames switch કરે અને IP addresses વાપરી <b>VLANs વચ્ચે packets route</b> કરે, hardware માં, wire speed પર.</p>
""" + L23_GU + """
<h4>Network devices અને OSI layers</h4>
<p>ઉપરના layer પર કામ કરતું device નીચેના layers ના કામ પણ કરી શકે (router signals regenerate પણ કરે અને frames સંભાળે).</p>
""" + DEV_GU + """
<p><b>Collision domain:</b> network નો ભાગ જ્યાં એક સાથે થતા બે transmissions અથડાય. <b>Broadcast domain:</b> network નો ભાગ જે broadcast frame મેળવે. Switches અને bridges collision domains તોડે; routers બંને તોડે.</p>""",
          diagram="cn3_dev_osi"),
    ]}
