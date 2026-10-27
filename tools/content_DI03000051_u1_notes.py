"""Computer Networks (DI03000051) - Unit 1 notes part A: 1.1 Network basics, 1.2 Types of computer networks.
Part B (topology, standards / protocols, servers) is in content_DI03000051_u1_notes_b."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

CONN_EN = tbl(["Point to Point", "Multipoint"], [
    ("Dedicated link between exactly two devices", "One link shared by three or more devices"),
    ("Entire capacity reserved for the two devices", "Capacity shared spatially or by time-sharing"),
    ("No addressing needed on the link", "Addresses needed to identify the receiver"),
    ("More cables when many devices are connected", "Fewer cables, cheaper"),
    ("High security and speed", "Lower security; collisions possible"),
    ("e.g. PC-printer cable, TV remote, leased line, mesh link", "e.g. bus LAN, Wi-Fi, cable TV")])
CONN_GU = tbl(["Point to Point", "Multipoint"], [
    ("બરાબર બે devices વચ્ચે dedicated link", "ત્રણ કે વધુ devices વચ્ચે એક જ shared link"),
    ("આખી capacity બે devices માટે અનામત", "Capacity જગ્યા કે સમય પ્રમાણે વહેંચાય"),
    ("Link પર addressing ની જરૂર નથી", "Receiver ઓળખવા addresses જરૂરી"),
    ("ઘણા devices જોડવા વધુ cables", "ઓછા cables, સસ્તું"),
    ("વધુ security અને speed", "ઓછી security; collisions શક્ય"),
    ("દા.ત. PC-printer cable, TV remote, leased line, mesh link", "દા.ત. bus LAN, Wi-Fi, cable TV")])

CMP_EN = tbl(["Point", "LAN", "MAN", "WAN"], [
    ("Full form", "Local Area Network", "Metropolitan Area Network", "Wide Area Network"),
    ("Area", "Room, building, campus (up to ~1 km)", "City (5-50 km)", "Country, continent, world"),
    ("Ownership", "Private (one organisation)", "Private or public", "Mostly public / many owners"),
    ("Speed", "Very high (100 Mbps-10 Gbps)", "High (10 Mbps-1 Gbps)", "Lower (Kbps-Mbps per user link)"),
    ("Error rate / delay", "Lowest", "Medium", "Highest"),
    ("Cost", "Low", "Medium", "Very high"),
    ("Media / devices", "UTP, Wi-Fi, switch", "Fiber, routers", "Fiber, satellite, microwave, routers"),
    ("Example", "College computer lab", "Cable TV / city network", "Internet, bank network")])
CMP_GU = tbl(["મુદ્દો", "LAN", "MAN", "WAN"], [
    ("Full form", "Local Area Network", "Metropolitan Area Network", "Wide Area Network"),
    ("વિસ્તાર", "રૂમ, building, campus (~1 km સુધી)", "શહેર (5-50 km)", "દેશ, ખંડ, દુનિયા"),
    ("માલિકી", "Private (એક સંસ્થા)", "Private કે public", "મોટે ભાગે public / ઘણા માલિક"),
    ("Speed", "ખૂબ વધુ (100 Mbps-10 Gbps)", "વધુ (10 Mbps-1 Gbps)", "ઓછી (user link પર Kbps-Mbps)"),
    ("Error rate / delay", "સૌથી ઓછો", "મધ્યમ", "સૌથી વધુ"),
    ("ખર્ચ", "ઓછો", "મધ્યમ", "ખૂબ વધુ"),
    ("Media / devices", "UTP, Wi-Fi, switch", "Fiber, routers", "Fiber, satellite, microwave, routers"),
    ("ઉદાહરણ", "College computer lab", "Cable TV / city network", "Internet, bank network")])

SEC_1_1 = {
    "title": {"en": "1.1 Basics of Computer Network", "gu": "1.1 Computer Network ની મૂળભૂત બાબતો"},
    "items": [
        T("1.1.1 Definition and Need of Computer Network", "1.1.1 Computer Network ની વ્યાખ્યા અને જરૂરિયાત",
          """<p>A <b>computer network</b> is a collection of two or more <b>autonomous (independent) computers and devices</b> interconnected by a <b>transmission medium</b> (cable or wireless) so that they can <b>exchange data and share resources</b>, following a set of rules called <b>protocols</b>.</p>
<p>Devices on a network are called <b>nodes</b> (computers, printers, mobiles, servers, routers). The connection between two nodes is a <b>link</b>.</p>
<h4>Components of data communication</h4>
<ol><li><b>Message:</b> the information to be sent (text, numbers, image, audio, video).</li><li><b>Sender:</b> the device that sends the message (computer, phone, camera).</li><li><b>Receiver:</b> the device that receives the message.</li><li><b>Transmission medium:</b> the physical path from sender to receiver (twisted pair, coaxial, fiber, radio waves).</li><li><b>Protocol:</b> the set of rules that governs communication; without a common protocol two devices can be connected but cannot communicate.</li></ol>
<h4>Need (goals) of computer networks</h4>
<ul>
<li><b>Resource sharing:</b> printers, scanners, storage and the Internet connection are shared by many users, which reduces cost.</li>
<li><b>Information / data sharing:</b> files and databases stored on a server can be accessed from any computer.</li>
<li><b>Communication:</b> e-mail, chat, video conferencing and VoIP allow fast and cheap communication.</li>
<li><b>Reliability and backup:</b> data can be copied on several computers; if one fails, another copy is available.</li>
<li><b>Cost reduction:</b> many cheap PCs sharing one powerful server is cheaper than giving everybody a big computer.</li>
<li><b>Centralised management:</b> software updates, security and backup are controlled from one place.</li>
<li><b>Scalability:</b> new computers and users can be added easily as the organisation grows.</li>
<li><b>Remote access:</b> work from home, online banking, accessing data from anywhere.</li>
</ul>
<h4>Characteristics of an effective network</h4>
<p><b>Delivery</b> (to the correct receiver), <b>accuracy</b> (without errors), <b>timeliness</b> (in time, e.g. live video), and low <b>jitter</b> (uniform delay between packets). Performance is measured by throughput and delay; reliability and security are also important.</p>""",
          """<p><b>Computer network</b> એ બે કે વધુ <b>સ્વતંત્ર (autonomous) computers અને devices</b> નો સમૂહ છે, જે <b>transmission medium</b> (cable કે wireless) થી જોડાયેલા હોય છે જેથી તેઓ <b>protocols</b> નામના નિયમોને અનુસરીને <b>data ની આપ-લે અને resources ની વહેંચણી</b> કરી શકે.</p>
<p>Network પરના devices ને <b>nodes</b> કહે છે (computers, printers, mobiles, servers, routers). બે nodes વચ્ચેનું જોડાણ <b>link</b> છે.</p>
<h4>Data communication ના ઘટકો</h4>
<ol><li><b>Message:</b> મોકલવાની માહિતી (text, numbers, image, audio, video).</li><li><b>Sender:</b> message મોકલનાર device (computer, phone, camera).</li><li><b>Receiver:</b> message મેળવનાર device.</li><li><b>Transmission medium:</b> sender થી receiver સુધીનો physical માર્ગ (twisted pair, coaxial, fiber, radio waves).</li><li><b>Protocol:</b> communication નિયંત્રિત કરતા નિયમોનો સમૂહ; સામાન્ય protocol વગર બે devices જોડાયેલા હોય તો પણ વાતચીત કરી શકતા નથી.</li></ol>
<h4>Computer networks ની જરૂરિયાત (goals)</h4>
<ul>
<li><b>Resource sharing:</b> printers, scanners, storage અને Internet connection ઘણા users વહેંચે છે, જેથી ખર્ચ ઘટે.</li>
<li><b>Information / data sharing:</b> server પર રાખેલી files અને databases કોઈ પણ computer પરથી વાપરી શકાય.</li>
<li><b>Communication:</b> e-mail, chat, video conferencing અને VoIP ઝડપી અને સસ્તો સંદેશાવ્યવહાર આપે.</li>
<li><b>Reliability અને backup:</b> data ઘણા computers પર copy રાખી શકાય; એક બગડે તો બીજી copy મળે.</li>
<li><b>ખર્ચમાં ઘટાડો:</b> એક શક્તિશાળી server વહેંચતા ઘણા સસ્તા PCs, દરેકને મોટું computer આપવા કરતાં સસ્તા છે.</li>
<li><b>Centralised management:</b> software updates, security અને backup એક જગ્યાએથી નિયંત્રિત થાય.</li>
<li><b>Scalability:</b> સંસ્થા વધે તેમ નવા computers અને users સહેલાઈથી ઉમેરી શકાય.</li>
<li><b>Remote access:</b> ઘરેથી કામ, online banking, ગમે ત્યાંથી data વાપરવો.</li>
</ul>
<h4>અસરકારક network ની લાક્ષણિકતાઓ</h4>
<p><b>Delivery</b> (સાચા receiver ને), <b>accuracy</b> (errors વગર), <b>timeliness</b> (સમયસર, દા.ત. live video), અને ઓછો <b>jitter</b> (packets વચ્ચે એકસરખો delay). Performance throughput અને delay થી મપાય; reliability અને security પણ મહત્વના છે.</p>""",
          diagram="cn1_basic"),
        T("1.1.2 Computer Network Applications", "1.1.2 Computer Network ના ઉપયોગો",
          """<p>Computer networks are used in almost every field today.</p>
<ul>
<li><b>Business applications:</b> resource sharing (printers, servers), client-server databases, e-mail, video conferencing (Zoom, Google Meet), e-commerce (Amazon, Flipkart), ERP systems linking offices and branches.</li>
<li><b>Banking and finance:</b> ATMs, core banking, online banking, UPI payments, stock market trading.</li>
<li><b>Home applications:</b> access to remote information (WWW, news, online learning), person-to-person communication (WhatsApp, e-mail, social media), interactive entertainment (OTT video streaming, online games), e-shopping.</li>
<li><b>Mobile users:</b> smartphones and laptops on Wi-Fi and 4G/5G networks: navigation (maps), mobile banking, m-commerce, cab booking.</li>
<li><b>Education:</b> e-learning (SWAYAM, NPTEL), online exams, digital libraries, smart classrooms.</li>
<li><b>Healthcare:</b> telemedicine, online reports, hospital information systems.</li>
<li><b>Government (e-governance):</b> online forms, DigiLocker, Aadhaar services, railway / bus reservation.</li>
<li><b>Cloud computing:</b> Google Drive, online office tools and servers rented over the Internet.</li>
<li><b>Internet of Things (IoT):</b> smart homes, CCTV cameras, smart meters and sensors connected to the network.</li>
</ul>""",
          """<p>આજે computer networks લગભગ દરેક ક્ષેત્રમાં વપરાય છે.</p>
<ul>
<li><b>Business ઉપયોગો:</b> resource sharing (printers, servers), client-server databases, e-mail, video conferencing (Zoom, Google Meet), e-commerce (Amazon, Flipkart), offices અને branches ને જોડતી ERP systems.</li>
<li><b>Banking અને finance:</b> ATMs, core banking, online banking, UPI payments, stock market trading.</li>
<li><b>ઘરના ઉપયોગો:</b> દૂરની માહિતી (WWW, news, online learning), વ્યક્તિ-થી-વ્યક્તિ communication (WhatsApp, e-mail, social media), interactive entertainment (OTT video streaming, online games), e-shopping.</li>
<li><b>Mobile users:</b> Wi-Fi અને 4G/5G networks પર smartphones અને laptops: navigation (maps), mobile banking, m-commerce, cab booking.</li>
<li><b>શિક્ષણ:</b> e-learning (SWAYAM, NPTEL), online exams, digital libraries, smart classrooms.</li>
<li><b>આરોગ્ય:</b> telemedicine, online reports, hospital information systems.</li>
<li><b>સરકાર (e-governance):</b> online forms, DigiLocker, Aadhaar services, railway / bus reservation.</li>
<li><b>Cloud computing:</b> Google Drive, online office tools અને Internet પર ભાડે મળતા servers.</li>
<li><b>Internet of Things (IoT):</b> network સાથે જોડાયેલા smart homes, CCTV cameras, smart meters અને sensors.</li>
</ul>"""),
        T("1.1.3 Types of Connection: Point to Point and Multipoint", "1.1.3 Connection ના પ્રકાર: Point to Point અને Multipoint",
          """<p>The <b>type of connection (line configuration)</b> tells how two or more devices are attached to a link. For communication, devices must be connected to the same link at the same time.</p>
<h4>1. Point-to-point connection</h4>
<p>Provides a <b>dedicated link between two devices</b>. The entire capacity of the link is reserved for transmission between those two devices only. It can use a cable or wireless media (microwave, satellite, infrared). Example: a computer connected to a printer by a cable; changing TV channels with an infrared remote.</p>
<h4>2. Multipoint (multidrop) connection</h4>
<p>More than two devices <b>share a single link</b>. The capacity of the channel is shared:</p>
<ul><li><b>Spatially shared:</b> several devices use the link at the same time.</li><li><b>Time shared:</b> devices take turns using the link.</li></ul>
<p>Example: computers on a bus topology LAN, devices on a Wi-Fi access point.</p>
<h4>Difference</h4>
""" + CONN_EN,
          """<p><b>Connection નો પ્રકાર (line configuration)</b> બતાવે છે કે બે કે વધુ devices link સાથે કેવી રીતે જોડાયેલા છે. Communication માટે devices એક જ સમયે એક જ link સાથે જોડાયેલા હોવા જોઈએ.</p>
<h4>1. Point-to-point connection</h4>
<p><b>બે devices વચ્ચે dedicated link</b> આપે છે. Link ની આખી capacity ફક્ત એ બે devices વચ્ચેના transmission માટે અનામત હોય છે. તે cable કે wireless media (microwave, satellite, infrared) વાપરી શકે. ઉદાહરણ: cable થી printer સાથે જોડાયેલું computer; infrared remote થી TV channels બદલવા.</p>
<h4>2. Multipoint (multidrop) connection</h4>
<p>બે થી વધુ devices <b>એક જ link વહેંચે</b> છે. Channel ની capacity વહેંચાય છે:</p>
<ul><li><b>Spatially shared:</b> ઘણા devices એક જ સમયે link વાપરે.</li><li><b>Time shared:</b> devices વારાફરતી link વાપરે.</li></ul>
<p>ઉદાહરણ: bus topology LAN પરના computers, Wi-Fi access point પરના devices.</p>
<h4>તફાવત</h4>
""" + CONN_GU,
          diagram="cn1_conn"),
    ]}

SEC_1_2 = {
    "title": {"en": "1.2 Types of Computer Networks", "gu": "1.2 Computer Networks ના પ્રકારો"},
    "items": [
        T("1.2.1 Local Area Network (LAN)", "1.2.1 Local Area Network (LAN)",
          """<p>A <b>LAN</b> is a privately owned network that connects computers and devices within a <b>small geographical area</b> such as a room, a building or a campus (up to about 1 km).</p>
<h4>Characteristics</h4>
<ul><li>Owned, used and managed by a single person or organisation.</li><li>High data rate: 100 Mbps, 1 Gbps or 10 Gbps; very low delay and error rate.</li><li>Uses UTP cables, switches and Wi-Fi access points; common standards are <b>Ethernet (IEEE 802.3)</b> and <b>Wi-Fi (IEEE 802.11)</b>.</li><li>Common topologies: star (most used), bus, ring.</li></ul>
<h4>Uses</h4>
<p>Sharing files, printers, scanners and one Internet connection in a computer lab, office, school, hotel or home; running client-server applications in an office.</p>
<h4>Advantages</h4>
<ul><li>Resource sharing reduces cost; fast and reliable data transfer.</li><li>Centralised data and easy backup; easy communication between users.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Covers only a limited area.</li><li>Setting up a server and cabling has an initial cost; a virus can spread to all computers.</li><li>Needs an administrator for security and maintenance.</li></ul>
<p>A <b>wireless LAN (WLAN)</b> uses Wi-Fi instead of cables. A <b>PAN (Personal Area Network)</b> is even smaller (about 10 m): e.g. a mobile connected to Bluetooth earbuds.</p>""",
          """<p><b>LAN</b> એ privately owned network છે જે રૂમ, building કે campus જેવા <b>નાના ભૌગોલિક વિસ્તાર</b> (લગભગ 1 km સુધી) માં computers અને devices ને જોડે છે.</p>
<h4>લાક્ષણિકતાઓ</h4>
<ul><li>એક જ વ્યક્તિ કે સંસ્થાની માલિકી, ઉપયોગ અને સંચાલન.</li><li>વધુ data rate: 100 Mbps, 1 Gbps કે 10 Gbps; ખૂબ ઓછો delay અને error rate.</li><li>UTP cables, switches અને Wi-Fi access points વાપરે; સામાન્ય standards <b>Ethernet (IEEE 802.3)</b> અને <b>Wi-Fi (IEEE 802.11)</b> છે.</li><li>સામાન્ય topologies: star (સૌથી વધુ વપરાતી), bus, ring.</li></ul>
<h4>ઉપયોગો</h4>
<p>Computer lab, office, school, hotel કે ઘરમાં files, printers, scanners અને એક Internet connection વહેંચવા; office માં client-server applications ચલાવવા.</p>
<h4>ફાયદા</h4>
<ul><li>Resource sharing થી ખર્ચ ઘટે; ઝડપી અને વિશ્વસનીય data transfer.</li><li>Centralised data અને સહેલું backup; users વચ્ચે સરળ communication.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>માત્ર મર્યાદિત વિસ્તાર આવરી લે.</li><li>Server અને cabling માટે શરૂઆતી ખર્ચ; virus બધા computers માં ફેલાઈ શકે.</li><li>Security અને maintenance માટે administrator જોઈએ.</li></ul>
<p><b>Wireless LAN (WLAN)</b> cables ના બદલે Wi-Fi વાપરે. <b>PAN (Personal Area Network)</b> તેનાથી પણ નાનું (લગભગ 10 m) છે: દા.ત. Bluetooth earbuds સાથે જોડાયેલો mobile.</p>""",
          diagram="cn1_lan"),
        T("1.2.2 Metropolitan Area Network (MAN)", "1.2.2 Metropolitan Area Network (MAN)",
          """<p>A <b>MAN</b> is a network that covers a <b>city or a large town</b> (about 5 to 50 km). It is larger than a LAN and smaller than a WAN, and usually interconnects several LANs of a city using a high-speed backbone (generally optical fiber).</p>
<h4>Characteristics</h4>
<ul><li>Owned by a single large organisation, a group of organisations, a telephone / cable company or the government.</li><li>Data rate is high (10 Mbps to 1 Gbps or more), slightly lower than a LAN.</li><li>Uses fiber optic cables, routers and switches; earlier standard: DQDB (IEEE 802.6); wireless MAN: WiMAX (IEEE 802.16).</li></ul>
<h4>Uses / examples</h4>
<p>Cable TV network of a city, connecting all branches of a bank or all colleges of a university in one city, city-wide Wi-Fi, CCTV surveillance network of a smart city.</p>
<h4>Advantages</h4>
<ul><li>Connects many LANs of a city at high speed; sharing of a common Internet connection.</li><li>Cheaper than a WAN for city-level communication.</li></ul>
<h4>Disadvantages</h4>
<ul><li>More costly and complex than a LAN; difficult to manage and secure.</li><li>Needs skilled staff; fiber laying is expensive.</li></ul>""",
          """<p><b>MAN</b> એ <b>શહેર કે મોટા નગર</b> (લગભગ 5 થી 50 km) ને આવરી લેતું network છે. તે LAN થી મોટું અને WAN થી નાનું છે, અને સામાન્ય રીતે high-speed backbone (મોટે ભાગે optical fiber) વડે શહેરના ઘણા LANs ને જોડે છે.</p>
<h4>લાક્ષણિકતાઓ</h4>
<ul><li>એક મોટી સંસ્થા, સંસ્થાઓનો સમૂહ, telephone / cable company કે સરકારની માલિકી.</li><li>Data rate વધુ (10 Mbps થી 1 Gbps કે વધુ), LAN કરતાં થોડો ઓછો.</li><li>Fiber optic cables, routers અને switches વાપરે; જૂનું standard: DQDB (IEEE 802.6); wireless MAN: WiMAX (IEEE 802.16).</li></ul>
<h4>ઉપયોગો / ઉદાહરણો</h4>
<p>શહેરનું cable TV network, એક શહેરમાં bank ની બધી branches કે university ની બધી colleges ને જોડવી, શહેરવ્યાપી Wi-Fi, smart city નું CCTV surveillance network.</p>
<h4>ફાયદા</h4>
<ul><li>શહેરના ઘણા LANs ને ઝડપથી જોડે; સામાન્ય Internet connection ની વહેંચણી.</li><li>શહેર-સ્તરના communication માટે WAN કરતાં સસ્તું.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>LAN કરતાં વધુ ખર્ચાળ અને જટિલ; સંચાલન અને security મુશ્કેલ.</li><li>કુશળ staff જોઈએ; fiber નાખવું મોંઘું.</li></ul>""",
          diagram="cn1_man"),
        T("1.2.3 Wide Area Network (WAN)", "1.2.3 Wide Area Network (WAN)",
          """<p>A <b>WAN</b> spans a <b>large geographical area</b> such as a state, a country, a continent or the whole world. It connects LANs and MANs that are far apart using <b>routers</b> and long-distance links: leased telephone lines, optical fiber, microwave and satellite.</p>
<h4>Characteristics</h4>
<ul><li>Usually not owned by one organisation; links are leased from telecom companies (ISPs).</li><li>Lower speed per link and higher propagation delay and error rate than LAN / MAN.</li><li>Technologies: leased lines, MPLS, Frame Relay, ATM, 4G/5G, satellite links.</li><li>Two kinds: <b>point-to-point WAN</b> (leased line between two sites) and <b>switched WAN</b> (backbone of the Internet).</li></ul>
<h4>Uses / examples</h4>
<p>The Internet (largest WAN), railway reservation network, network connecting all branches of a bank across India, ATM network, multinational company networks.</p>
<h4>Advantages</h4>
<ul><li>Covers a very large area; people in different cities and countries can communicate and share data.</li><li>Centralised data for all branches; supports business everywhere.</li></ul>
<h4>Disadvantages</h4>
<ul><li>High setup and maintenance cost; complex to manage.</li><li>More security problems (hacking, viruses); needs firewalls.</li><li>Slower and higher delay than a LAN.</li></ul>""",
          """<p><b>WAN</b> રાજ્ય, દેશ, ખંડ કે આખી દુનિયા જેવા <b>મોટા ભૌગોલિક વિસ્તાર</b> માં ફેલાયેલું હોય છે. તે <b>routers</b> અને લાંબા અંતરના links: leased telephone lines, optical fiber, microwave અને satellite વડે દૂર આવેલા LANs અને MANs ને જોડે છે.</p>
<h4>લાક્ષણિકતાઓ</h4>
<ul><li>સામાન્ય રીતે એક સંસ્થાની માલિકી નથી; links telecom companies (ISPs) પાસેથી ભાડે લેવાય.</li><li>LAN / MAN કરતાં link દીઠ ઓછી speed અને વધુ propagation delay અને error rate.</li><li>Technologies: leased lines, MPLS, Frame Relay, ATM, 4G/5G, satellite links.</li><li>બે પ્રકાર: <b>point-to-point WAN</b> (બે sites વચ્ચે leased line) અને <b>switched WAN</b> (Internet નું backbone).</li></ul>
<h4>ઉપયોગો / ઉદાહરણો</h4>
<p>Internet (સૌથી મોટું WAN), railway reservation network, ભારતભરમાં bank ની બધી branches ને જોડતું network, ATM network, multinational company networks.</p>
<h4>ફાયદા</h4>
<ul><li>ખૂબ મોટો વિસ્તાર આવરી લે; જુદાં શહેરો અને દેશોના લોકો communication અને data sharing કરી શકે.</li><li>બધી branches માટે centralised data; દરેક જગ્યાએ business ને support.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Setup અને maintenance નો ખર્ચ વધુ; સંચાલન જટિલ.</li><li>વધુ security સમસ્યાઓ (hacking, viruses); firewalls જોઈએ.</li><li>LAN કરતાં ધીમું અને વધુ delay.</li></ul>""",
          diagram="cn1_wan"),
        T("1.2.4 Internet and Comparison of LAN, MAN, WAN", "1.2.4 Internet અને LAN, MAN, WAN ની સરખામણી",
          """<p>The <b>Internet</b> (inter-connected networks) is a <b>worldwide network of networks</b> that connects millions of private, public, academic, business and government networks using the <b>TCP/IP</b> protocol suite. Nobody owns the whole Internet.</p>
<h4>Structure</h4>
<ul><li><b>Backbone:</b> very high-speed fiber networks of large (Tier-1) providers, including undersea cables between countries.</li><li><b>ISPs (Internet Service Providers):</b> regional and local companies (Jio, Airtel, BSNL) that connect to the backbone and give Internet access to users.</li><li><b>End users:</b> homes, mobiles, colleges, offices and servers connected through their ISP by broadband, fiber, DSL, 4G/5G or Wi-Fi.</li></ul>
<h4>Services / uses of the Internet</h4>
<p>World Wide Web (websites), e-mail, file transfer (FTP), search engines, social media, e-commerce, online banking and UPI, video streaming and conferencing, cloud storage, e-learning.</p>
<p><b>Intranet:</b> a private network of an organisation using Internet technology (web pages, e-mail), accessible only to its employees. <b>Extranet:</b> part of an intranet opened to selected outsiders (suppliers, customers).</p>
<h4>Comparison of LAN, MAN and WAN</h4>
""" + CMP_EN,
          """<p><b>Internet</b> (inter-connected networks) એ <b>TCP/IP</b> protocol suite વાપરીને લાખો private, public, academic, business અને government networks ને જોડતું <b>વિશ્વવ્યાપી networks નું network</b> છે. આખા Internet નો કોઈ એક માલિક નથી.</p>
<h4>રચના</h4>
<ul><li><b>Backbone:</b> મોટા (Tier-1) providers ના ખૂબ high-speed fiber networks, દેશો વચ્ચેના દરિયાઈ (undersea) cables સહિત.</li><li><b>ISPs (Internet Service Providers):</b> backbone સાથે જોડાઈને users ને Internet access આપતી પ્રાદેશિક અને સ્થાનિક companies (Jio, Airtel, BSNL).</li><li><b>End users:</b> broadband, fiber, DSL, 4G/5G કે Wi-Fi વડે પોતાના ISP મારફતે જોડાયેલા ઘરો, mobiles, colleges, offices અને servers.</li></ul>
<h4>Internet ની સેવાઓ / ઉપયોગો</h4>
<p>World Wide Web (websites), e-mail, file transfer (FTP), search engines, social media, e-commerce, online banking અને UPI, video streaming અને conferencing, cloud storage, e-learning.</p>
<p><b>Intranet:</b> Internet technology (web pages, e-mail) વાપરતું સંસ્થાનું private network, ફક્ત તેના કર્મચારીઓ વાપરી શકે. <b>Extranet:</b> પસંદગીના બહારના લોકો (suppliers, customers) માટે ખોલેલો intranet નો ભાગ.</p>
<h4>LAN, MAN અને WAN ની સરખામણી</h4>
""" + CMP_GU,
          diagram="cn1_internet"),
    ]}

from content_DI03000051_u1_notes_b import SEC_1_3, SEC_1_4, SEC_1_5  # noqa: E402

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4, SEC_1_5]
