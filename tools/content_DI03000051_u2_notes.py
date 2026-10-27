"""Computer Networks (DI03000051) - Unit 2 notes part A: 2.1 OSI reference model.
Part B (TCP/IP model, comparison) is in content_DI03000051_u2_notes_b."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

SUM_EN = tbl(["Layer", "Main functions", "PDU / device", "Protocols"], [
    ("7 Application", "Network services to the user: web, mail, file transfer", "Data / gateway", "HTTP, FTP, SMTP, DNS, Telnet"),
    ("6 Presentation", "Translation, encryption, compression", "Data", "JPEG, MPEG, SSL/TLS, ASCII"),
    ("5 Session", "Dialog control, synchronisation, session management", "Data", "NetBIOS, RPC, PPTP"),
    ("4 Transport", "Process-to-process delivery, ports, segmentation, flow and error control", "Segment", "TCP, UDP, SCTP"),
    ("3 Network", "Logical (IP) addressing, routing, source-to-destination delivery", "Packet / router", "IP, ICMP, ARP, OSPF"),
    ("2 Data Link", "Framing, MAC addressing, hop-to-hop delivery, flow, error, access control", "Frame / switch, bridge", "Ethernet, PPP, HDLC"),
    ("1 Physical", "Transmission of bits, signals, data rate, transmission mode, topology", "Bits / hub, repeater", "RS-232, DSL, 10BaseT")])
SUM_GU = tbl(["Layer", "મુખ્ય કાર્યો", "PDU / device", "Protocols"], [
    ("7 Application", "User ને network services: web, mail, file transfer", "Data / gateway", "HTTP, FTP, SMTP, DNS, Telnet"),
    ("6 Presentation", "Translation, encryption, compression", "Data", "JPEG, MPEG, SSL/TLS, ASCII"),
    ("5 Session", "Dialog control, synchronisation, session management", "Data", "NetBIOS, RPC, PPTP"),
    ("4 Transport", "Process-to-process delivery, ports, segmentation, flow અને error control", "Segment", "TCP, UDP, SCTP"),
    ("3 Network", "Logical (IP) addressing, routing, source-to-destination delivery", "Packet / router", "IP, ICMP, ARP, OSPF"),
    ("2 Data Link", "Framing, MAC addressing, hop-to-hop delivery, flow, error, access control", "Frame / switch, bridge", "Ethernet, PPP, HDLC"),
    ("1 Physical", "Bits નું transmission, signals, data rate, transmission mode, topology", "Bits / hub, repeater", "RS-232, DSL, 10BaseT")])

SEC_2_1 = {
    "title": {"en": "2.1 OSI Reference Model", "gu": "2.1 OSI Reference Model"},
    "items": [
        T("2.1.1 Layered Architecture and the OSI Model", "2.1.1 Layered Architecture અને OSI Model",
          """<p>Network communication is a complex task. To reduce the complexity, network software is organised as a <b>stack of layers</b>, each built on the one below it. Each layer performs a well-defined set of functions, <b>offers services to the layer above</b> and uses the services of the layer below, hiding the details of how they are implemented. This is called a <b>layered architecture</b>; the set of layers and protocols is the <b>network architecture</b>.</p>
<h4>OSI model</h4>
<p>The <b>Open Systems Interconnection (OSI) model</b> was developed by the <b>ISO (International Organization for Standardization)</b> and published in 1984 (ISO 7498). An <b>open system</b> is a set of protocols that allows any two different systems to communicate regardless of their underlying architecture. OSI is a <b>reference model</b> (a framework for understanding and designing networks), not a protocol itself.</p>
<p>It has <b>seven layers</b>: (7) Application, (6) Presentation, (5) Session, (4) Transport, (3) Network, (2) Data Link and (1) Physical.</p>
<ul><li><b>Layers 1-3 (network support layers):</b> physical aspects of moving data from one device to another (electrical specifications, physical connections, physical addressing, timing and reliability).</li><li><b>Layer 4 (transport):</b> links the two groups; ensures reliable end-to-end transmission.</li><li><b>Layers 5-7 (user support layers):</b> allow interoperability among unrelated software systems.</li></ul>
<h4>Principles used to design the layers</h4>
<ul><li>A layer is created where a different abstraction is needed; each layer performs a well-defined function.</li><li>Layer boundaries are chosen to minimise information flow across the interfaces.</li><li>The number of layers is large enough to separate functions but small enough to keep the architecture manageable.</li></ul>
<h4>Advantages of layering</h4>
<ul><li>Divides a complex task into smaller, manageable parts; easy to understand and teach.</li><li>A change in one layer does not affect the other layers (modularity).</li><li>Standard interfaces allow products of different vendors to work together (interoperability).</li><li>Easy troubleshooting layer by layer.</li></ul>""",
          """<p>Network communication એ જટિલ કાર્ય છે. જટિલતા ઘટાડવા network software ને <b>layers ના stack</b> તરીકે ગોઠવવામાં આવે છે, દરેક તેની નીચેના layer પર બનેલું હોય છે. દરેક layer નિશ્ચિત કાર્યો કરે, <b>ઉપરના layer ને services આપે</b> અને નીચેના layer ની services વાપરે, અને તે કેવી રીતે અમલમાં છે તેની વિગતો છુપાવે. તેને <b>layered architecture</b> કહે છે; layers અને protocols નો સમૂહ એ <b>network architecture</b> છે.</p>
<h4>OSI model</h4>
<p><b>Open Systems Interconnection (OSI) model</b> <b>ISO (International Organization for Standardization)</b> એ બનાવ્યું અને 1984 માં પ્રકાશિત કર્યું (ISO 7498). <b>Open system</b> એ protocols નો સમૂહ છે જે કોઈ પણ બે જુદી systems ને તેમના અંદરના architecture ની પરવા વગર communicate કરવા દે છે. OSI એ <b>reference model</b> (networks સમજવા અને design કરવા માટેનું માળખું) છે, પોતે protocol નથી.</p>
<p>તેમાં <b>સાત layers</b> છે: (7) Application, (6) Presentation, (5) Session, (4) Transport, (3) Network, (2) Data Link અને (1) Physical.</p>
<ul><li><b>Layers 1-3 (network support layers):</b> એક device થી બીજા device સુધી data લઈ જવાના physical પાસાં (electrical specifications, physical connections, physical addressing, timing અને reliability).</li><li><b>Layer 4 (transport):</b> બંને જૂથોને જોડે; વિશ્વસનીય end-to-end transmission સુનિશ્ચિત કરે.</li><li><b>Layers 5-7 (user support layers):</b> અસંબંધિત software systems વચ્ચે interoperability આપે.</li></ul>
<h4>Layers design કરવાના સિદ્ધાંતો</h4>
<ul><li>જ્યાં જુદા abstraction ની જરૂર હોય ત્યાં layer બને; દરેક layer નિશ્ચિત કાર્ય કરે.</li><li>Interfaces પર માહિતીનો પ્રવાહ ઓછો રહે તે રીતે layer boundaries પસંદ થાય.</li><li>Layers ની સંખ્યા કાર્યો અલગ કરવા પૂરતી મોટી પણ architecture સંભાળી શકાય તેટલી નાની.</li></ul>
<h4>Layering ના ફાયદા</h4>
<ul><li>જટિલ કાર્યને નાના, સંભાળી શકાય તેવા ભાગોમાં વહેંચે; સમજવું અને શીખવવું સહેલું.</li><li>એક layer માં ફેરફાર બીજા layers ને અસર ન કરે (modularity).</li><li>Standard interfaces જુદા vendors ના products ને સાથે કામ કરાવે (interoperability).</li><li>Layer પ્રમાણે troubleshooting સહેલું.</li></ul>""",
          diagram="cn2_osi"),
        T("2.1.2 Peer-to-Peer Processes and Interfaces", "2.1.2 Peer-to-Peer Processes અને Interfaces",
          """<p>When device A sends a message to device B, the message moves <b>down</b> through the layers of A, travels over the physical medium, passes through intermediate nodes (routers use only layers 1-3), and moves <b>up</b> through the layers of B.</p>
<ul>
<li><b>Peer-to-peer process:</b> layer <i>x</i> on one machine communicates logically with layer <i>x</i> on the other machine using a <b>protocol</b>. The processes in corresponding layers are called <b>peers</b>. This communication is <b>virtual (logical)</b>; only the physical layer communicates directly.</li>
<li><b>Interface:</b> between each pair of adjacent layers there is an interface that defines the information and <b>services</b> a layer provides to the layer above it. Well-defined interfaces allow a layer's implementation to be changed without affecting the others.</li>
<li><b>Service Access Point (SAP):</b> the point at which an upper layer accesses the services of a lower layer (e.g. a port number is a transport-layer SAP).</li>
<li><b>Protocol vs service:</b> a <b>service</b> is what a layer provides to the layer above (vertical); a <b>protocol</b> is the set of rules between peer layers (horizontal).</li>
</ul>""",
          """<p>Device A device B ને message મોકલે ત્યારે message A ના layers માંથી <b>નીચે</b> જાય, physical medium પર જાય, વચ્ચેના nodes માંથી પસાર થાય (routers માત્ર layers 1-3 વાપરે), અને B ના layers માંથી <b>ઉપર</b> જાય.</p>
<ul>
<li><b>Peer-to-peer process:</b> એક machine પરનું layer <i>x</i> બીજા machine પરના layer <i>x</i> સાથે <b>protocol</b> વાપરીને logical રીતે communicate કરે. અનુરૂપ layers ની processes ને <b>peers</b> કહે છે. આ communication <b>virtual (logical)</b> છે; માત્ર physical layer સીધું communicate કરે.</li>
<li><b>Interface:</b> દરેક બાજુ-બાજુના layers ની જોડી વચ્ચે interface હોય છે જે layer ઉપરના layer ને કઈ માહિતી અને <b>services</b> આપે તે નક્કી કરે. સ્પષ્ટ interfaces layer નો અમલ બીજાને અસર કર્યા વગર બદલવા દે.</li>
<li><b>Service Access Point (SAP):</b> જ્યાંથી ઉપરનું layer નીચેના layer ની services વાપરે તે બિંદુ (દા.ત. port number એ transport-layer SAP છે).</li>
<li><b>Protocol vs service:</b> <b>service</b> એ layer ઉપરના layer ને જે આપે તે (vertical); <b>protocol</b> એ peer layers વચ્ચેના નિયમો (horizontal).</li>
</ul>""",
          diagram="cn2_peer"),
        T("2.1.3 Encapsulation and Decapsulation", "2.1.3 Encapsulation અને Decapsulation",
          """<p><b>Encapsulation</b> is the process in which each layer at the sender <b>adds its own control information (header)</b> to the data received from the layer above, and passes the whole unit down. The data link layer also adds a <b>trailer</b> (error-detection bits). At the physical layer the frame is converted into a stream of <b>bits / signals</b>.</p>
<p><b>Decapsulation</b> is the reverse process at the receiver: each layer reads and <b>removes its peer's header</b>, performs its function, and passes the remaining data up.</p>
<h4>Protocol Data Units (PDUs)</h4>
<ul><li>Application, presentation, session: <b>data / message</b></li><li>Transport: <b>segment</b> (TCP) or <b>datagram</b> (UDP)</li><li>Network: <b>packet</b> (IP datagram)</li><li>Data link: <b>frame</b></li><li>Physical: <b>bits</b></li></ul>
<p>Headers carry information such as addresses, sequence numbers and error-checking codes. They add <b>overhead</b>: the larger the headers compared to the data, the lower the efficiency (see the solved numericals).</p>""",
          """<p><b>Encapsulation</b> એ પ્રક્રિયા છે જેમાં sender પરનું દરેક layer ઉપરના layer પાસેથી મળેલા data માં <b>પોતાની control માહિતી (header) ઉમેરે</b> છે, અને આખું એકમ નીચે મોકલે. Data link layer <b>trailer</b> (error-detection bits) પણ ઉમેરે. Physical layer પર frame <b>bits / signals</b> ના પ્રવાહમાં ફેરવાય.</p>
<p><b>Decapsulation</b> એ receiver પરની વિરુદ્ધ પ્રક્રિયા છે: દરેક layer પોતાના peer નું header વાંચી <b>દૂર કરે</b>, પોતાનું કાર્ય કરે, અને બાકીનો data ઉપર મોકલે.</p>
<h4>Protocol Data Units (PDUs)</h4>
<ul><li>Application, presentation, session: <b>data / message</b></li><li>Transport: <b>segment</b> (TCP) અથવા <b>datagram</b> (UDP)</li><li>Network: <b>packet</b> (IP datagram)</li><li>Data link: <b>frame</b></li><li>Physical: <b>bits</b></li></ul>
<p>Headers માં addresses, sequence numbers અને error-checking codes જેવી માહિતી હોય છે. તે <b>overhead</b> ઉમેરે છે: data ની સરખામણીમાં headers જેટલા મોટા, તેટલી efficiency ઓછી (ઉકેલેલા દાખલા જુઓ).</p>""",
          diagram="cn2_encap", examples=["cn2n1", "cn2n2"]),
        T("2.1.4 Physical Layer (Layer 1)", "2.1.4 Physical Layer (Layer 1)",
          """<p>The physical layer coordinates the functions required to <b>carry a bit stream over a physical medium</b>. It deals with the mechanical and electrical specifications of the interface and the transmission medium.</p>
<h4>Functions</h4>
<ul>
<li><b>Physical characteristics of interfaces and media:</b> type of medium, connectors (RJ-45), pins, cables.</li>
<li><b>Representation of bits:</b> bits (0 and 1) are encoded into electrical or optical signals; the layer defines the encoding.</li>
<li><b>Data rate:</b> the number of bits sent per second (transmission rate), i.e. the duration of a bit.</li>
<li><b>Synchronisation of bits:</b> sender and receiver clocks must be synchronised at the bit level.</li>
<li><b>Line configuration:</b> point-to-point or multipoint connection.</li>
<li><b>Physical topology:</b> bus, star, ring, mesh, hybrid.</li>
<li><b>Transmission mode:</b> <b>simplex</b> (one direction only: keyboard, TV broadcast), <b>half duplex</b> (both directions but one at a time: walkie-talkie) or <b>full duplex</b> (both directions simultaneously: telephone).</li>
</ul>
<p><b>Devices:</b> hub, repeater, cables, connectors, modem. <b>Standards:</b> RS-232, 10BaseT, 100BaseTX, DSL, IEEE 802.11 physical layer.</p>""",
          """<p>Physical layer <b>physical medium પર bit stream લઈ જવા</b> માટેનાં કાર્યોનું સંકલન કરે છે. તે interface અને transmission medium ના mechanical અને electrical specifications સાથે સંબંધિત છે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Interfaces અને media ની physical લાક્ષણિકતાઓ:</b> medium નો પ્રકાર, connectors (RJ-45), pins, cables.</li>
<li><b>Bits નું representation:</b> bits (0 અને 1) electrical કે optical signals માં encode થાય; layer encoding નક્કી કરે.</li>
<li><b>Data rate:</b> પ્રતિ second મોકલાતા bits ની સંખ્યા (transmission rate), એટલે કે bit નો સમયગાળો.</li>
<li><b>Bits નું synchronisation:</b> sender અને receiver ની clocks bit સ્તરે synchronise હોવી જોઈએ.</li>
<li><b>Line configuration:</b> point-to-point કે multipoint connection.</li>
<li><b>Physical topology:</b> bus, star, ring, mesh, hybrid.</li>
<li><b>Transmission mode:</b> <b>simplex</b> (માત્ર એક દિશા: keyboard, TV broadcast), <b>half duplex</b> (બંને દિશા પણ એક સમયે એક: walkie-talkie) અથવા <b>full duplex</b> (બંને દિશા એક સાથે: telephone).</li>
</ul>
<p><b>Devices:</b> hub, repeater, cables, connectors, modem. <b>Standards:</b> RS-232, 10BaseT, 100BaseTX, DSL, IEEE 802.11 physical layer.</p>""",
          diagram="cn2_modes"),
        T("2.1.5 Data Link Layer (Layer 2)", "2.1.5 Data Link Layer (Layer 2)",
          """<p>The data link layer transforms the raw physical layer into a <b>reliable link</b>. It makes the physical layer appear error-free to the network layer and is responsible for <b>hop-to-hop (node-to-node) delivery</b>.</p>
<h4>Functions</h4>
<ul>
<li><b>Framing:</b> divides the stream of bits from the network layer into manageable units called <b>frames</b>, marking their start and end (flags).</li>
<li><b>Physical addressing:</b> adds a header with the <b>physical (MAC) address</b> of the sender and of the receiver (next hop) on the same network.</li>
<li><b>Flow control:</b> prevents a fast sender from overwhelming a slow receiver.</li>
<li><b>Error control:</b> detects and retransmits damaged or lost frames, and recognises duplicate frames; a <b>trailer (FCS / CRC)</b> is added at the end of the frame.</li>
<li><b>Access control:</b> when two or more devices share one link, decides which device has control of the link at a given time (CSMA/CD, token passing).</li>
</ul>
<p><b>Sublayers (IEEE 802):</b> <b>LLC</b> (Logical Link Control: flow and error control) and <b>MAC</b> (Media Access Control: addressing and access to the medium).</p>
<p><b>Devices:</b> switch, bridge, NIC. <b>Protocols:</b> Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC.</p>""",
          """<p>Data link layer કાચા physical layer ને <b>વિશ્વસનીય link</b> માં ફેરવે છે. તે network layer ને physical layer error-free દેખાડે અને <b>hop-to-hop (node-to-node) delivery</b> માટે જવાબદાર છે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Framing:</b> network layer પાસેથી આવતા bits ના પ્રવાહને <b>frames</b> નામના સંભાળી શકાય તેવા એકમોમાં વહેંચે, તેમની શરૂઆત અને અંત (flags) દર્શાવે.</li>
<li><b>Physical addressing:</b> એક જ network પરના sender અને receiver (next hop) ના <b>physical (MAC) address</b> વાળું header ઉમેરે.</li>
<li><b>Flow control:</b> ઝડપી sender ધીમા receiver ને ડુબાડી ન દે તે અટકાવે.</li>
<li><b>Error control:</b> બગડેલા કે ખોવાયેલા frames શોધી ફરી મોકલે, અને duplicate frames ઓળખે; frame ના અંતે <b>trailer (FCS / CRC)</b> ઉમેરાય.</li>
<li><b>Access control:</b> બે કે વધુ devices એક link વહેંચે ત્યારે કોઈ સમયે link પર કયા device નું નિયંત્રણ તે નક્કી કરે (CSMA/CD, token passing).</li>
</ul>
<p><b>Sublayers (IEEE 802):</b> <b>LLC</b> (Logical Link Control: flow અને error control) અને <b>MAC</b> (Media Access Control: addressing અને medium access).</p>
<p><b>Devices:</b> switch, bridge, NIC. <b>Protocols:</b> Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC.</p>""",
          diagram="cn2_frame"),
        T("2.1.6 Network Layer (Layer 3)", "2.1.6 Network Layer (Layer 3)",
          """<p>The network layer is responsible for the <b>source-to-destination delivery of a packet</b>, possibly across multiple networks (links). The data link layer delivers between two systems on the same network; the network layer ensures that each packet gets from its point of origin to its final destination.</p>
<h4>Functions</h4>
<ul>
<li><b>Logical addressing:</b> adds a header with the <b>logical (IP) addresses</b> of the sender and the receiver, which are unique across the whole Internet. (Physical addresses work only within one network.)</li>
<li><b>Routing:</b> routers find the <b>best path</b> through the interconnected networks using routing tables and routing protocols (RIP, OSPF, BGP).</li>
<li><b>Packet forwarding / switching:</b> moving packets from the input to the correct output of a router.</li>
<li><b>Fragmentation and reassembly:</b> dividing a packet when it is larger than the maximum size allowed on a network.</li>
<li><b>Congestion control</b> and quality of service.</li>
</ul>
<p><b>Device:</b> router (layer-3 switch). <b>Protocols:</b> IPv4, IPv6, ICMP, IGMP, ARP, routing protocols. PDU: <b>packet</b>.</p>""",
          """<p>Network layer ઘણા networks (links) પાર <b>packet ની source-to-destination delivery</b> માટે જવાબદાર છે. Data link layer એક જ network પરની બે systems વચ્ચે delivery કરે; network layer ખાતરી કરે કે દરેક packet તેના મૂળ સ્થાનથી અંતિમ destination સુધી પહોંચે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Logical addressing:</b> sender અને receiver ના <b>logical (IP) addresses</b> વાળું header ઉમેરે, જે આખા Internet પર અનન્ય છે. (Physical addresses માત્ર એક network માં કામ કરે.)</li>
<li><b>Routing:</b> routers routing tables અને routing protocols (RIP, OSPF, BGP) વાપરી જોડાયેલા networks માંથી <b>શ્રેષ્ઠ માર્ગ</b> શોધે.</li>
<li><b>Packet forwarding / switching:</b> router ના input થી સાચા output સુધી packets ખસેડવા.</li>
<li><b>Fragmentation અને reassembly:</b> network પર માન્ય મહત્તમ size કરતાં packet મોટું હોય ત્યારે તેને વહેંચવું.</li>
<li><b>Congestion control</b> અને quality of service.</li>
</ul>
<p><b>Device:</b> router (layer-3 switch). <b>Protocols:</b> IPv4, IPv6, ICMP, IGMP, ARP, routing protocols. PDU: <b>packet</b>.</p>""",
          diagram="cn2_hop"),
        T("2.1.7 Transport Layer (Layer 4)", "2.1.7 Transport Layer (Layer 4)",
          """<p>The transport layer is responsible for <b>process-to-process delivery</b> of the entire message. The network layer delivers packets to the right <b>host</b>; the transport layer delivers the message to the right <b>process (application)</b> on that host, making sure it arrives intact and in order.</p>
<h4>Functions</h4>
<ul>
<li><b>Service-point (port) addressing:</b> the header includes a <b>port number</b> that identifies the application process (e.g. 80 for a web server).</li>
<li><b>Segmentation and reassembly:</b> the message is divided into <b>segments</b>, each with a <b>sequence number</b>, so that the receiver can reassemble them correctly and replace lost ones.</li>
<li><b>Connection control:</b> <b>connection-oriented</b> (TCP: connection set up, data transfer, release) or <b>connectionless</b> (UDP: each segment independent).</li>
<li><b>Flow control:</b> end to end, rather than across a single link.</li>
<li><b>Error control:</b> end to end; ensures the whole message arrives without error, loss or duplication (retransmission).</li>
</ul>
<p><b>Protocols:</b> TCP (reliable), UDP (fast, unreliable), SCTP. PDU: <b>segment</b>. Also called the heart of the OSI model, as it links the network-support and user-support layers.</p>""",
          """<p>Transport layer આખા message ની <b>process-to-process delivery</b> માટે જવાબદાર છે. Network layer packets ને સાચા <b>host</b> સુધી પહોંચાડે; transport layer message ને તે host પરની સાચી <b>process (application)</b> સુધી પહોંચાડે, અને ખાતરી કરે કે તે અખંડ અને ક્રમમાં પહોંચે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Service-point (port) addressing:</b> header માં application process ઓળખતો <b>port number</b> હોય (દા.ત. web server માટે 80).</li>
<li><b>Segmentation અને reassembly:</b> message <b>segments</b> માં વહેંચાય, દરેકને <b>sequence number</b> હોય, જેથી receiver તેમને સાચી રીતે જોડી શકે અને ખોવાયેલા બદલી શકે.</li>
<li><b>Connection control:</b> <b>connection-oriented</b> (TCP: connection setup, data transfer, release) કે <b>connectionless</b> (UDP: દરેક segment સ્વતંત્ર).</li>
<li><b>Flow control:</b> એક link પર નહીં પણ end to end.</li>
<li><b>Error control:</b> end to end; આખો message error, loss કે duplication વગર પહોંચે તેની ખાતરી (retransmission).</li>
</ul>
<p><b>Protocols:</b> TCP (વિશ્વસનીય), UDP (ઝડપી, અવિશ્વસનીય), SCTP. PDU: <b>segment</b>. તે network-support અને user-support layers ને જોડતું હોવાથી OSI model નું હૃદય પણ કહેવાય છે.</p>""",
          diagram="cn2_ports"),
        T("2.1.8 Session Layer (Layer 5)", "2.1.8 Session Layer (Layer 5)",
          """<p>The session layer is the network <b>dialog controller</b>. It establishes, maintains and synchronises the interaction (session) between communicating systems.</p>
<h4>Functions</h4>
<ul>
<li><b>Dialog control:</b> allows two systems to enter into a dialog and decides whose turn it is to send, in half-duplex or full-duplex mode.</li>
<li><b>Synchronisation:</b> adds <b>checkpoints (synchronisation points)</b> into the stream of data. Example: when sending a 2000-page file, a checkpoint is inserted after every 100 pages; if a crash happens at page 523, only pages 501-523 are retransmitted.</li>
<li><b>Session management:</b> session establishment, maintenance and termination; authentication and authorisation of the session.</li>
<li><b>Token management:</b> prevents two sides from attempting the same critical operation at the same time.</li>
</ul>
<p><b>Protocols / examples:</b> NetBIOS, RPC (Remote Procedure Call), PPTP, SQL sessions, login sessions.</p>""",
          """<p>Session layer એ network નો <b>dialog controller</b> છે. તે communicate કરતી systems વચ્ચેની ક્રિયાપ્રતિક્રિયા (session) સ્થાપે, જાળવે અને synchronise કરે છે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Dialog control:</b> બે systems ને dialog માં પ્રવેશવા દે અને half-duplex કે full-duplex mode માં મોકલવાનો વારો કોનો તે નક્કી કરે.</li>
<li><b>Synchronisation:</b> data ના પ્રવાહમાં <b>checkpoints (synchronisation points)</b> ઉમેરે. ઉદાહરણ: 2000-page file મોકલતી વખતે દર 100 pages પછી checkpoint મુકાય; page 523 પર crash થાય તો માત્ર pages 501-523 ફરી મોકલાય.</li>
<li><b>Session management:</b> session સ્થાપના, જાળવણી અને સમાપ્તિ; session નું authentication અને authorisation.</li>
<li><b>Token management:</b> બંને બાજુ એક જ critical operation એક સાથે કરવાનો પ્રયાસ ન કરે તે અટકાવે.</li>
</ul>
<p><b>Protocols / ઉદાહરણો:</b> NetBIOS, RPC (Remote Procedure Call), PPTP, SQL sessions, login sessions.</p>""",
          diagram="cn2_session"),
        T("2.1.9 Presentation Layer (Layer 6)", "2.1.9 Presentation Layer (Layer 6)",
          """<p>The presentation layer is concerned with the <b>syntax and semantics</b> of the information exchanged between two systems. It makes sure that data sent by the application layer of one system can be read by the application layer of the other.</p>
<h4>Functions</h4>
<ul>
<li><b>Translation:</b> different computers use different encoding systems (ASCII, EBCDIC, Unicode). The sender's format is changed into a common format and, at the receiver, into the receiver's format.</li>
<li><b>Encryption and decryption:</b> to carry sensitive information (passwords, bank details) securely, the sender transforms the original information (plain text) into another form (cipher text); the receiver decrypts it. Example: SSL/TLS used by HTTPS.</li>
<li><b>Compression:</b> reduces the number of bits to be transmitted; important for multimedia: text (ZIP), images (JPEG), audio (MP3) and video (MPEG).</li>
</ul>
<p>It is sometimes called the <b>translator</b> of the network.</p>""",
          """<p>Presentation layer બે systems વચ્ચે આપ-લે થતી માહિતીના <b>syntax અને semantics</b> સાથે સંબંધિત છે. તે ખાતરી કરે કે એક system ના application layer એ મોકલેલો data બીજી system નું application layer વાંચી શકે.</p>
<h4>કાર્યો</h4>
<ul>
<li><b>Translation:</b> જુદાં computers જુદી encoding systems (ASCII, EBCDIC, Unicode) વાપરે. Sender નું format સામાન્ય format માં અને receiver પર receiver ના format માં બદલાય.</li>
<li><b>Encryption અને decryption:</b> સંવેદનશીલ માહિતી (passwords, bank details) સુરક્ષિત રીતે લઈ જવા sender મૂળ માહિતી (plain text) ને બીજા સ્વરૂપ (cipher text) માં ફેરવે; receiver તેને decrypt કરે. ઉદાહરણ: HTTPS વાપરતું SSL/TLS.</li>
<li><b>Compression:</b> મોકલવાના bits ની સંખ્યા ઘટાડે; multimedia માટે મહત્વનું: text (ZIP), images (JPEG), audio (MP3) અને video (MPEG).</li>
</ul>
<p>તેને ક્યારેક network નો <b>translator</b> કહે છે.</p>""",
          diagram="cn2_present"),
        T("2.1.10 Application Layer (Layer 7) and Summary of OSI Layers (Practical 2)", "2.1.10 Application Layer (Layer 7) અને OSI Layers નો સારાંશ (Practical 2)",
          """<p>The application layer enables the <b>user (human or software) to access the network</b>. It provides user interfaces and support for services such as e-mail, remote file access and transfer, and the World Wide Web. It is the layer closest to the user.</p>
<h4>Services / functions</h4>
<ul>
<li><b>Network virtual terminal:</b> a software version of a physical terminal that allows a user to log on to a remote host (Telnet, SSH).</li>
<li><b>File transfer, access and management (FTAM):</b> access, retrieve and manage files on a remote computer (FTP).</li>
<li><b>Mail services:</b> e-mail forwarding and storage (SMTP, POP3, IMAP).</li>
<li><b>Directory services:</b> distributed databases of information about objects and services (DNS, LDAP).</li>
<li><b>Web access:</b> HTTP / HTTPS for browsing.</li>
</ul>
<h4>Summary of the seven layers</h4>
""" + SUM_EN + """
<p>Memory aid (7 to 1): <b>All People Seem To Need Data Processing</b>; (1 to 7): <b>Please Do Not Throw Sausage Pizza Away</b>.</p>""",
          """<p>Application layer <b>user (માણસ કે software) ને network વાપરવા</b> દે છે. તે user interfaces અને e-mail, remote file access અને transfer, અને World Wide Web જેવી services માટે support આપે. તે user ની સૌથી નજીકનું layer છે.</p>
<h4>Services / કાર્યો</h4>
<ul>
<li><b>Network virtual terminal:</b> physical terminal નું software સ્વરૂપ જે user ને remote host પર log on કરવા દે (Telnet, SSH).</li>
<li><b>File transfer, access અને management (FTAM):</b> remote computer પરની files access, retrieve અને manage કરવી (FTP).</li>
<li><b>Mail services:</b> e-mail forwarding અને storage (SMTP, POP3, IMAP).</li>
<li><b>Directory services:</b> objects અને services વિશેની માહિતીના distributed databases (DNS, LDAP).</li>
<li><b>Web access:</b> browsing માટે HTTP / HTTPS.</li>
</ul>
<h4>સાત layers નો સારાંશ</h4>
""" + SUM_GU + """
<p>યાદ રાખવા (7 થી 1): <b>All People Seem To Need Data Processing</b>; (1 થી 7): <b>Please Do Not Throw Sausage Pizza Away</b>.</p>"""),
    ]}

from content_DI03000051_u2_notes_b import SEC_2_2, SEC_2_3  # noqa: E402

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3]
