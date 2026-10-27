"""Computer Networks (DI03000051) - Unit 1 extras: topology numericals (computed), equations, viva, exam questions."""
from content_DI03000011_u1_extras import N, E, V, X
from content_DI03000041_u1_notes import tbl


def topo(n):
    return {"bus": (f"1 backbone + {n} drop lines", 1, n), "ring": (n, 2, 2 * n), "star": (n, 1, 2 * n),
            "mesh": (n * (n - 1) // 2, n - 1, n * (n - 1))}


def p1_table(n, lang):
    t = topo(n)
    if lang == "en":
        head = ["Topology", "Cables (links)", "Ports per device", "Total ports"]
        star_tot = f"{n} + {n} (hub) = {2 * n}"
    else:
        head = ["Topology", "Cables (links)", "Device દીઠ ports", "કુલ ports"]
        star_tot = f"{n} + {n} (hub) = {2 * n}"
    return tbl(head, [("Bus", t["bus"][0], "1", f"{n} × 1 = {n}"),
                      ("Ring", str(t["ring"][0]), "2", f"{n} × 2 = {2 * n}"),
                      ("Star", f"{n} (device to hub)", "1", star_tot),
                      ("Mesh", f"{n}({n}-1)/2 = {t['mesh'][0]}", f"{n}-1 = {n - 1}", f"{n} × {n - 1} = {n * (n - 1)}")])


n1 = N("cn1n1", "(Practical 1) Six devices are connected with wired media. Find the number of cables (links), ports needed in each device and the total number of ports in the network for (a) bus (b) ring (c) star (d) mesh topology.",
       "(Practical 1) છ devices wired media થી જોડાયેલા છે. (a) bus (b) ring (c) star (d) mesh topology માટે cables (links) ની સંખ્યા, દરેક device માં જરૂરી ports અને network માં કુલ ports શોધો.",
       """<p>Given n = 6 devices.</p>
<ul><li><b>Bus:</b> one backbone cable; each device is connected by its own drop line, so 6 drop lines; each device needs 1 port.</li>
<li><b>Ring:</b> each device is connected to its two neighbours: links = n = 6; ports per device = 2.</li>
<li><b>Star:</b> each device has one cable to the hub: links = n = 6; 1 port per device, and the hub needs 6 ports.</li>
<li><b>Mesh:</b> links = n(n-1)/2 = 6×5/2 = 15; ports per device = n-1 = 5; total = n(n-1) = 30.</li></ul>""" + p1_table(6, "en") +
       "<p><b>Answer:</b> Bus 6 ports, Ring 12 ports, Star 12 ports (6 devices + 6 hub), Mesh 15 cables and 30 ports.</p>",
       """<p>n = 6 devices આપેલ છે.</p>
<ul><li><b>Bus:</b> એક backbone cable; દરેક device પોતાની drop line થી જોડાય, તેથી 6 drop lines; દરેક device ને 1 port.</li>
<li><b>Ring:</b> દરેક device તેના બે પડોશીઓ સાથે જોડાય: links = n = 6; device દીઠ ports = 2.</li>
<li><b>Star:</b> દરેક device નો hub સુધી એક cable: links = n = 6; device દીઠ 1 port, અને hub ને 6 ports.</li>
<li><b>Mesh:</b> links = n(n-1)/2 = 6×5/2 = 15; device દીઠ ports = n-1 = 5; કુલ = n(n-1) = 30.</li></ul>""" + p1_table(6, "gu") +
       "<p><b>જવાબ:</b> Bus 6 ports, Ring 12 ports, Star 12 ports (6 devices + 6 hub), Mesh 15 cables અને 30 ports.</p>")

n2 = N("cn1n2", "Eight computers are to be connected in a fully connected mesh topology. Find the number of cables, the ports on each computer and the total ports.",
       "આઠ computers ને fully connected mesh topology માં જોડવાના છે. Cables ની સંખ્યા, દરેક computer પરના ports અને કુલ ports શોધો.",
       "<p>n = 8</p><p>Cables = n(n-1)/2 = 8×7/2 = <b>28</b></p><p>Ports per computer = n-1 = <b>7</b></p><p>Total ports = n(n-1) = 8×7 = <b>56</b></p>",
       "<p>n = 8</p><p>Cables = n(n-1)/2 = 8×7/2 = <b>28</b></p><p>Computer દીઠ ports = n-1 = <b>7</b></p><p>કુલ ports = n(n-1) = 8×7 = <b>56</b></p>")

n3 = N("cn1n3", "A fully connected mesh network has 21 links. How many devices are there, and how many ports does each device need?",
       "Fully connected mesh network માં 21 links છે. કેટલા devices છે, અને દરેક device ને કેટલા ports જોઈએ?",
       "<p>n(n-1)/2 = 21 ⇒ n(n-1) = 42 ⇒ n² - n - 42 = 0 ⇒ (n-7)(n+6) = 0</p><p>n = <b>7 devices</b> (n = -6 is not possible)</p><p>Ports per device = n-1 = <b>6</b>; check: 7×6/2 = 21 ✓</p>",
       "<p>n(n-1)/2 = 21 ⇒ n(n-1) = 42 ⇒ n² - n - 42 = 0 ⇒ (n-7)(n+6) = 0</p><p>n = <b>7 devices</b> (n = -6 શક્ય નથી)</p><p>Device દીઠ ports = n-1 = <b>6</b>; ચકાસણી: 7×6/2 = 21 ✓</p>")

n4 = N("cn1n4", "A lab has 10 computers. Compare the number of cables needed for star and mesh topology. Which is suitable for the lab and why?",
       "Lab માં 10 computers છે. Star અને mesh topology માટે જરૂરી cables ની સરખામણી કરો. Lab માટે કઈ યોગ્ય છે અને શા માટે?",
       "<p>n = 10</p><p><b>Star:</b> cables = n = <b>10</b>; 1 port per computer; hub / switch with at least 10 ports.</p><p><b>Mesh:</b> cables = 10×9/2 = <b>45</b>; 9 ports per computer; total 90 ports.</p><p>Mesh needs 4.5 times more cables and 9 network cards in each PC, which is very costly. <b>Star topology is suitable</b>: cheap, easy to install, and a fault in one cable affects only one computer.</p>",
       "<p>n = 10</p><p><b>Star:</b> cables = n = <b>10</b>; computer દીઠ 1 port; ઓછામાં ઓછા 10 ports વાળું hub / switch.</p><p><b>Mesh:</b> cables = 10×9/2 = <b>45</b>; computer દીઠ 9 ports; કુલ 90 ports.</p><p>Mesh ને 4.5 ગણા વધુ cables અને દરેક PC માં 9 network cards જોઈએ, જે ખૂબ ખર્ચાળ છે. <b>Star topology યોગ્ય છે</b>: સસ્તી, install કરવી સહેલી, અને એક cable નો fault માત્ર એક computer ને અસર કરે.</p>")

n5 = N("cn1n5", "Find the number of links and ports per device for 5 devices in ring and mesh topology.",
       "Ring અને mesh topology માં 5 devices માટે links અને device દીઠ ports શોધો.",
       "<p>n = 5</p><p><b>Ring:</b> links = n = <b>5</b>; ports per device = <b>2</b>; total ports = 10.</p><p><b>Mesh:</b> links = 5×4/2 = <b>10</b>; ports per device = <b>4</b>; total ports = 20.</p>",
       "<p>n = 5</p><p><b>Ring:</b> links = n = <b>5</b>; device દીઠ ports = <b>2</b>; કુલ ports = 10.</p><p><b>Mesh:</b> links = 5×4/2 = <b>10</b>; device દીઠ ports = <b>4</b>; કુલ ports = 20.</p>")

n6 = N("cn1n6", "In a star network of 24 computers, one 16-port switch is not enough. How many 16-port switches are needed if the switches are connected to each other in a chain (one port of each switch used for each switch-to-switch link)?",
       "24 computers ના star network માં એક 16-port switch પૂરતું નથી. Switches એકબીજા સાથે chain માં જોડાય (દરેક switch-to-switch link માટે દરેક switch નો એક port વપરાય) તો કેટલા 16-port switches જોઈએ?",
       "<p>With 2 switches: 1 link between them uses 1 port on each, so usable ports = 2×16 - 2 = 30 ≥ 24 ✓ (1 switch gives only 16 &lt; 24).</p><p><b>2 switches</b> are needed; cables = 24 (computers) + 1 (switch to switch) = <b>25</b>. This is an extended star (tree).</p>",
       "<p>2 switches સાથે: તેમની વચ્ચેની 1 link દરેકનો 1 port વાપરે, તેથી વાપરી શકાય તેવા ports = 2×16 - 2 = 30 ≥ 24 ✓ (1 switch માત્ર 16 &lt; 24 આપે).</p><p><b>2 switches</b> જોઈએ; cables = 24 (computers) + 1 (switch to switch) = <b>25</b>. આ extended star (tree) છે.</p>")

NUMERICALS = [n1, n2, n3, n4, n5, n6]

EQUATIONS = [
    {"title": {"en": "Topology formulas (n devices)", "gu": "Topology સૂત્રો (n devices)"}, "items": [
        E("Mesh: number of links", "Mesh: links ની સંખ્યા", "Links = n(n - 1) / 2", "Duplex links; e.g. n = 6 → 15", "Duplex links; દા.ત. n = 6 → 15"),
        E("Mesh: ports per device", "Mesh: device દીઠ ports", "Ports per device = n - 1", "Each device connects to all others", "દરેક device બાકી બધા સાથે જોડાય"),
        E("Mesh: total ports", "Mesh: કુલ ports", "Total ports = n(n - 1)", "e.g. n = 6 → 30", "દા.ત. n = 6 → 30"),
        E("Star", "Star", "Links = n,  ports/device = 1,  hub ports = n", "Total ports = 2n with hub", "Hub સાથે કુલ ports = 2n"),
        E("Ring", "Ring", "Links = n,  ports/device = 2,  total = 2n", "Each device has two neighbours", "દરેક device ના બે પડોશી"),
        E("Bus", "Bus", "1 backbone + n drop lines,  ports/device = 1", "Total ports = n; 2 terminators", "કુલ ports = n; 2 terminators"),
    ]},
]

VIVA = [
    {"title": {"en": "Network basics and types", "gu": "Network basics અને પ્રકારો"}, "items": [
        V("What is a computer network?", "Computer network શું છે?", "A collection of interconnected autonomous computers and devices that share data and resources using protocols.", "Protocols વાપરીને data અને resources વહેંચતા જોડાયેલા સ્વતંત્ર computers અને devices નો સમૂહ."),
        V("Name the five components of data communication.", "Data communication ના પાંચ ઘટકો જણાવો.", "Message, sender, receiver, transmission medium and protocol.", "Message, sender, receiver, transmission medium અને protocol."),
        V("What is a node?", "Node શું છે?", "Any device connected to a network: computer, printer, router, mobile.", "Network સાથે જોડાયેલું કોઈ પણ device: computer, printer, router, mobile."),
        V("Differentiate point-to-point and multipoint connection.", "Point-to-point અને multipoint connection નો તફાવત આપો.", "Point-to-point: dedicated link between two devices. Multipoint: one link shared by more than two devices.", "Point-to-point: બે devices વચ્ચે dedicated link. Multipoint: બે થી વધુ devices વહેંચતી એક link."),
        V("Give the range of LAN, MAN and WAN.", "LAN, MAN અને WAN નો વિસ્તાર આપો.", "LAN up to about 1 km (building / campus), MAN 5-50 km (city), WAN country to world.", "LAN લગભગ 1 km સુધી (building / campus), MAN 5-50 km (શહેર), WAN દેશથી દુનિયા."),
        V("Which is the largest WAN?", "સૌથી મોટું WAN કયું છે?", "The Internet.", "Internet."),
        V("What is PAN?", "PAN શું છે?", "Personal Area Network (about 10 m), e.g. a mobile with Bluetooth earbuds.", "Personal Area Network (લગભગ 10 m), દા.ત. Bluetooth earbuds સાથે mobile."),
        V("What is an intranet?", "Intranet શું છે?", "A private network of an organisation using Internet technologies, accessible only to its members.", "Internet technologies વાપરતું સંસ્થાનું private network, માત્ર તેના સભ્યો વાપરી શકે."),
    ]},
    {"title": {"en": "Topology", "gu": "Topology"}, "items": [
        V("What is network topology?", "Network topology શું છે?", "The geometric arrangement of nodes and links in a network.", "Network માં nodes અને links ની ભૌમિતિક ગોઠવણી."),
        V("Why are terminators used in bus topology?", "Bus topology માં terminators શા માટે વપરાય?", "To absorb the signal at the ends of the backbone and prevent reflection.", "Backbone ના છેડે signal શોષી reflection અટકાવવા."),
        V("Which topology is most used in LANs?", "LANs માં કઈ topology સૌથી વધુ વપરાય?", "Star topology (with a switch).", "Star topology (switch સાથે)."),
        V("What happens if the hub fails in star topology?", "Star topology માં hub બગડે તો શું થાય?", "The whole network stops because all communication passes through the hub.", "આખું network બંધ થાય કારણ કે બધું communication hub માંથી પસાર થાય."),
        V("What is a token in ring topology?", "Ring topology માં token શું છે?", "A special frame circulating in the ring; only the device holding it can transmit.", "Ring માં ફરતો ખાસ frame; તે ધરાવતું device જ transmit કરી શકે."),
        V("How many links are needed for 6 devices in mesh?", "Mesh માં 6 devices માટે કેટલી links જોઈએ?", "n(n-1)/2 = 15 links; 5 ports per device.", "n(n-1)/2 = 15 links; device દીઠ 5 ports."),
        V("What is hybrid topology?", "Hybrid topology શું છે?", "A combination of two or more topologies, e.g. star + bus.", "બે કે વધુ topologies નું સંયોજન, દા.ત. star + bus."),
    ]},
    {"title": {"en": "Standards, protocols and servers", "gu": "Standards, protocols અને servers"}, "items": [
        V("What is a protocol? Give its key elements.", "Protocol શું છે? તેના મુખ્ય તત્વો આપો.", "A set of rules for data communication; key elements: syntax, semantics and timing.", "Data communication માટેના નિયમોનો સમૂહ; મુખ્ય તત્વો: syntax, semantics અને timing."),
        V("Give the full forms of IEEE, ISO, ISOC, IETF and IRTF.", "IEEE, ISO, ISOC, IETF અને IRTF ના full forms આપો.", "Institute of Electrical and Electronics Engineers; International Organization for Standardization; Internet Society; Internet Engineering Task Force; Internet Research Task Force.", "Institute of Electrical and Electronics Engineers; International Organization for Standardization; Internet Society; Internet Engineering Task Force; Internet Research Task Force."),
        V("What is an RFC?", "RFC શું છે?", "Request for Comments: a document in which Internet standards are published by the IETF.", "Request for Comments: IETF દ્વારા Internet standards પ્રકાશિત થતું document."),
        V("Which IEEE standards are used for Ethernet and Wi-Fi?", "Ethernet અને Wi-Fi માટે કયા IEEE standards વપરાય?", "IEEE 802.3 for Ethernet and IEEE 802.11 for Wi-Fi.", "Ethernet માટે IEEE 802.3 અને Wi-Fi માટે IEEE 802.11."),
        V("Which organisation developed the OSI model?", "OSI model કઈ સંસ્થાએ બનાવ્યું?", "ISO (International Organization for Standardization).", "ISO (International Organization for Standardization)."),
        V("What is a server?", "Server શું છે?", "A computer or program that provides services to client computers on a network.", "Network પર client computers ને સેવાઓ આપતું computer કે program."),
        V("Which protocols does a mail server use?", "Mail server કયા protocols વાપરે?", "SMTP to send mail; POP3 or IMAP to receive mail.", "Mail મોકલવા SMTP; મેળવવા POP3 કે IMAP."),
        V("What is the use of caching in a proxy server?", "Proxy server માં caching નો ઉપયોગ શું છે?", "Frequently requested pages are stored and served locally, which is faster and saves bandwidth.", "વારંવાર માંગાતાં pages સંગ્રહાઈ સ્થાનિક રીતે અપાય, જે ઝડપી છે અને bandwidth બચાવે."),
        V("Name two web server software.", "બે web server software નાં નામ આપો.", "Apache and Nginx (also Microsoft IIS).", "Apache અને Nginx (Microsoft IIS પણ)."),
    ]},
]

EXAM_QS = [
    X("Define computer network. Explain the need of computer networks.", "Computer network ની વ્યાખ્યા આપો. Computer networks ની જરૂરિયાત સમજાવો.", 3),
    X("Explain the components of data communication with a diagram.", "આકૃતિ સાથે data communication ના ઘટકો સમજાવો.", 3),
    X("List applications of computer networks.", "Computer networks ના ઉપયોગો જણાવો.", 3),
    X("Differentiate point-to-point and multipoint connection.", "Point-to-point અને multipoint connection નો તફાવત આપો.", 3),
    X("Explain LAN with its advantages and disadvantages.", "LAN તેના ફાયદા અને ગેરફાયદા સાથે સમજાવો.", 4),
    X("Explain MAN and WAN with examples.", "ઉદાહરણો સાથે MAN અને WAN સમજાવો.", 4),
    X("Compare LAN, MAN and WAN.", "LAN, MAN અને WAN ની સરખામણી કરો.", 4),
    X("Define network topology. Explain bus topology with its advantages and disadvantages.", "Network topology ની વ્યાખ્યા આપો. Bus topology તેના ફાયદા અને ગેરફાયદા સાથે સમજાવો.", 4),
    X("Explain star and ring topology with diagrams.", "આકૃતિઓ સાથે star અને ring topology સમજાવો.", 7),
    X("Explain mesh topology. Find the number of links and ports for 6 devices.", "Mesh topology સમજાવો. 6 devices માટે links અને ports શોધો.", 4),
    X("Explain tree and hybrid topology.", "Tree અને hybrid topology સમજાવો.", 4),
    X("Explain any four network topologies with diagrams, advantages and disadvantages.", "કોઈ પણ ચાર network topologies આકૃતિઓ, ફાયદા અને ગેરફાયદા સાથે સમજાવો.", 7),
    X("Define protocol. Explain the key elements of a protocol.", "Protocol ની વ્યાખ્યા આપો. Protocol ના મુખ્ય તત્વો સમજાવો.", 3),
    X("Write a short note on standard organisations: IEEE, ISO, ISOC, IETF, IRTF.", "Standard organisations: IEEE, ISO, ISOC, IETF, IRTF પર ટૂંકનોંધ લખો.", 4),
    X("Explain file server, print server and mail server.", "File server, print server અને mail server સમજાવો.", 4),
    X("Explain web server and proxy server with their applications.", "Web server અને proxy server તેમના ઉપયોગો સાથે સમજાવો.", 4),
]
