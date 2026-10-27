"""Computer Networks (DI03000051) - Unit 2 extras: header-overhead numericals (computed), equations, viva, exam questions."""
from content_DI03000011_u1_extras import N, E, V, X


def pct(a, b):
    return f"{100 * a / b:.2f}%"


# n1: Tanenbaum-style n-layer overhead
n_, h_, M_ = 7, 20, 500
H = n_ * h_
n1 = N("cn2n1", f"A system has a {n_}-layer protocol hierarchy. Each layer adds a {h_}-byte header. An application generates a message of {M_} bytes. What fraction of the network bandwidth is filled with headers?",
       f"એક system માં {n_}-layer protocol hierarchy છે. દરેક layer {h_}-byte header ઉમેરે છે. Application {M_} bytes નો message બનાવે છે. Network bandwidth નો કેટલો ભાગ headers થી ભરાય?",
       f"<p>Total header = n × h = {n_} × {h_} = {H} bytes</p><p>Total transmitted = M + nh = {M_} + {H} = {M_ + H} bytes</p>"
       f"<p>Fraction of headers = nh / (M + nh) = {H} / {M_ + H} = <b>{H / (M_ + H):.4f} = {pct(H, M_ + H)}</b></p>"
       f"<p>Efficiency = M / (M + nh) = {M_} / {M_ + H} = {pct(M_, M_ + H)}</p>",
       f"<p>કુલ header = n × h = {n_} × {h_} = {H} bytes</p><p>કુલ મોકલાતા = M + nh = {M_} + {H} = {M_ + H} bytes</p>"
       f"<p>Headers નો ભાગ = nh / (M + nh) = {H} / {M_ + H} = <b>{H / (M_ + H):.4f} = {pct(H, M_ + H)}</b></p>"
       f"<p>Efficiency = M / (M + nh) = {M_} / {M_ + H} = {pct(M_, M_ + H)}</p>")

# n2: OSI 6 headers + trailer
M2, h2, t2 = 1000, 20, 4
F2 = M2 + 6 * h2 + t2
n2 = N("cn2n2", f"In the OSI model, a {M2}-byte message is sent. Layers 7 to 2 each add a {h2}-byte header and the data link layer also adds a {t2}-byte trailer. Find the frame size and the efficiency.",
       f"OSI model માં {M2}-byte message મોકલાય છે. Layers 7 થી 2 દરેક {h2}-byte header ઉમેરે અને data link layer {t2}-byte trailer પણ ઉમેરે. Frame size અને efficiency શોધો.",
       f"<p>Headers: 6 layers (7, 6, 5, 4, 3, 2) × {h2} = {6 * h2} bytes; trailer = {t2} bytes</p>"
       f"<p>Frame size = {M2} + {6 * h2} + {t2} = <b>{F2} bytes</b></p>"
       f"<p>Efficiency = data / frame = {M2} / {F2} = <b>{pct(M2, F2)}</b>; overhead = {pct(F2 - M2, F2)}</p>",
       f"<p>Headers: 6 layers (7, 6, 5, 4, 3, 2) × {h2} = {6 * h2} bytes; trailer = {t2} bytes</p>"
       f"<p>Frame size = {M2} + {6 * h2} + {t2} = <b>{F2} bytes</b></p>"
       f"<p>Efficiency = data / frame = {M2} / {F2} = <b>{pct(M2, F2)}</b>; overhead = {pct(F2 - M2, F2)}</p>")

# n3: TCP/IP over Ethernet
D3, F3 = 1460, 1460 + 20 + 20 + 14 + 4
n3 = N("cn2n3", "An application sends 1460 bytes of data using TCP over IPv4 and Ethernet. TCP header = 20 bytes, IP header = 20 bytes, Ethernet header = 14 bytes and Ethernet trailer (FCS) = 4 bytes. Find the frame size and the efficiency.",
       "Application TCP, IPv4 અને Ethernet વાપરીને 1460 bytes data મોકલે છે. TCP header = 20 bytes, IP header = 20 bytes, Ethernet header = 14 bytes અને Ethernet trailer (FCS) = 4 bytes. Frame size અને efficiency શોધો.",
       f"<p>Segment = 1460 + 20 = 1480 bytes; packet = 1480 + 20 = 1500 bytes; frame = 1500 + 14 + 4 = <b>{F3} bytes</b></p>"
       f"<p>Efficiency = 1460 / {F3} = <b>{pct(D3, F3)}</b></p><p>(1500 bytes is the maximum IP packet size on Ethernet, called the MTU.)</p>",
       f"<p>Segment = 1460 + 20 = 1480 bytes; packet = 1480 + 20 = 1500 bytes; frame = 1500 + 14 + 4 = <b>{F3} bytes</b></p>"
       f"<p>Efficiency = 1460 / {F3} = <b>{pct(D3, F3)}</b></p><p>(Ethernet પર મહત્તમ IP packet size 1500 bytes છે, જેને MTU કહે છે.)</p>")

# n4: small UDP packet (voice)
D4, F4 = 160, 160 + 12 + 8 + 20 + 18
n4 = N("cn2n4", "A voice call sends 160 bytes of audio per packet using RTP (12-byte header) over UDP (8 bytes), IPv4 (20 bytes) and Ethernet (18 bytes header + trailer). Find the efficiency. What happens if TCP (20 bytes) is used instead of UDP?",
       "Voice call દરેક packet માં 160 bytes audio RTP (12-byte header), UDP (8 bytes), IPv4 (20 bytes) અને Ethernet (18 bytes header + trailer) પર મોકલે છે. Efficiency શોધો. UDP ના બદલે TCP (20 bytes) વાપરીએ તો શું થાય?",
       f"<p>Frame = 160 + 12 + 8 + 20 + 18 = <b>{F4} bytes</b>; efficiency = 160 / {F4} = <b>{pct(D4, F4)}</b></p>"
       f"<p>With TCP: frame = {F4 + 12} bytes; efficiency = 160 / {F4 + 12} = {pct(D4, F4 + 12)}. TCP also retransmits late packets, which adds delay. So <b>UDP is preferred</b> for real-time voice and video: small header and no retransmission delay.</p>",
       f"<p>Frame = 160 + 12 + 8 + 20 + 18 = <b>{F4} bytes</b>; efficiency = 160 / {F4} = <b>{pct(D4, F4)}</b></p>"
       f"<p>TCP સાથે: frame = {F4 + 12} bytes; efficiency = 160 / {F4 + 12} = {pct(D4, F4 + 12)}. TCP મોડા packets ફરી મોકલે, જે delay વધારે. તેથી real-time voice અને video માટે <b>UDP પસંદ થાય</b>: નાનું header અને retransmission delay નહીં.</p>")

NUMERICALS = [n1, n2, n3, n4]

EQUATIONS = [
    {"title": {"en": "Header overhead", "gu": "Header overhead"}, "items": [
        E("Total size sent", "કુલ મોકલાતી size", "Total = M + n × h", "M = message, n = layers, h = header per layer", "M = message, n = layers, h = layer દીઠ header"),
        E("Fraction of headers", "Headers નો ભાગ", "Overhead = nh / (M + nh)", "Larger headers or smaller messages → more overhead", "મોટાં headers કે નાના messages → વધુ overhead"),
        E("Efficiency", "Efficiency", "Efficiency = M / (M + nh) × 100%", "Also = data / frame size", "= data / frame size પણ"),
        E("TCP/IP over Ethernet", "Ethernet પર TCP/IP", "Frame = data + 20 (TCP) + 20 (IP) + 18 (Ethernet)", "Max: 1460 + 20 + 20 + 18 = 1518 bytes", "મહત્તમ: 1460 + 20 + 20 + 18 = 1518 bytes"),
    ]},
    {"title": {"en": "Address sizes", "gu": "Address sizes"}, "items": [
        E("Address sizes", "Address sizes", "MAC = 48 bits,  IPv4 = 32 bits,  IPv6 = 128 bits,  port = 16 bits", "Port range 0-65535; well-known 0-1023", "Port range 0-65535; well-known 0-1023"),
    ]},
]

VIVA = [
    {"title": {"en": "OSI model", "gu": "OSI model"}, "items": [
        V("What is the full form of OSI? Who developed it?", "OSI નું full form શું છે? કોણે બનાવ્યું?", "Open Systems Interconnection; developed by ISO.", "Open Systems Interconnection; ISO એ બનાવ્યું."),
        V("How many layers are in the OSI model? Name them.", "OSI model માં કેટલા layers છે? નામ આપો.", "Seven: physical, data link, network, transport, session, presentation, application.", "સાત: physical, data link, network, transport, session, presentation, application."),
        V("What is encapsulation?", "Encapsulation શું છે?", "Adding a header (and trailer at layer 2) to data as it moves down the layers at the sender.", "Sender પર data layers માં નીચે જાય ત્યારે header (અને layer 2 પર trailer) ઉમેરવું."),
        V("Name the PDU of each layer.", "દરેક layer નો PDU જણાવો.", "Data (upper layers), segment (transport), packet (network), frame (data link), bits (physical).", "Data (ઉપરના layers), segment (transport), packet (network), frame (data link), bits (physical)."),
        V("Which layer is responsible for hop-to-hop delivery?", "Hop-to-hop delivery માટે કયું layer જવાબદાર છે?", "Data link layer.", "Data link layer."),
        V("Which layer does routing?", "Routing કયું layer કરે?", "Network layer (device: router).", "Network layer (device: router)."),
        V("Which layer provides process-to-process delivery?", "Process-to-process delivery કયું layer આપે?", "Transport layer, using port numbers.", "Transport layer, port numbers વાપરીને."),
        V("What are synchronisation points?", "Synchronisation points શું છે?", "Checkpoints added by the session layer so that after a crash only data after the last checkpoint is resent.", "Session layer ઉમેરે તે checkpoints જેથી crash પછી માત્ર છેલ્લા checkpoint પછીનો data ફરી મોકલાય."),
        V("Which layer does encryption and compression?", "Encryption અને compression કયું layer કરે?", "Presentation layer.", "Presentation layer."),
        V("What are the sublayers of the data link layer?", "Data link layer ના sublayers કયા છે?", "LLC (Logical Link Control) and MAC (Media Access Control).", "LLC (Logical Link Control) અને MAC (Media Access Control)."),
        V("Name the devices working at layers 1, 2 and 3.", "Layers 1, 2 અને 3 પર કામ કરતા devices જણાવો.", "Layer 1: hub, repeater; layer 2: switch, bridge; layer 3: router.", "Layer 1: hub, repeater; layer 2: switch, bridge; layer 3: router."),
        V("What are the three transmission modes?", "ત્રણ transmission modes કયા છે?", "Simplex, half duplex and full duplex.", "Simplex, half duplex અને full duplex."),
    ]},
    {"title": {"en": "TCP/IP model and comparison", "gu": "TCP/IP model અને સરખામણી"}, "items": [
        V("Name the layers of the TCP/IP model.", "TCP/IP model ના layers જણાવો.", "Network access, internet, transport and application.", "Network access, internet, transport અને application."),
        V("Who developed TCP/IP?", "TCP/IP કોણે બનાવ્યું?", "The US Department of Defense (DoD) for ARPANET.", "US Department of Defense (DoD) એ ARPANET માટે."),
        V("What is the use of ARP?", "ARP નો ઉપયોગ શું છે?", "It finds the MAC address of a host from its IP address.", "IP address પરથી host નું MAC address શોધે."),
        V("Which protocol is used by ping?", "Ping કયો protocol વાપરે?", "ICMP.", "ICMP."),
        V("Give two differences between TCP and UDP.", "TCP અને UDP વચ્ચે બે તફાવત આપો.", "TCP is connection-oriented and reliable; UDP is connectionless and unreliable but faster with an 8-byte header.", "TCP connection-oriented અને વિશ્વસનીય; UDP connectionless અને અવિશ્વસનીય પણ 8-byte header સાથે ઝડપી."),
        V("What is the three-way handshake?", "Three-way handshake શું છે?", "TCP connection setup using SYN, SYN-ACK and ACK.", "SYN, SYN-ACK અને ACK વાપરી TCP connection setup."),
        V("Give the port numbers of HTTP, HTTPS, FTP, SMTP and DNS.", "HTTP, HTTPS, FTP, SMTP અને DNS ના port numbers આપો.", "HTTP 80, HTTPS 443, FTP 20/21, SMTP 25, DNS 53.", "HTTP 80, HTTPS 443, FTP 20/21, SMTP 25, DNS 53."),
        V("Name the four levels of addresses in TCP/IP.", "TCP/IP માં addresses ના ચાર સ્તર જણાવો.", "Physical (MAC), logical (IP), port and specific (URL / e-mail) addresses.", "Physical (MAC), logical (IP), port અને specific (URL / e-mail) addresses."),
        V("Which OSI layers are combined in the TCP/IP application layer?", "TCP/IP application layer માં કયા OSI layers જોડાયેલા છે?", "Session, presentation and application.", "Session, presentation અને application."),
        V("Which model is used on the Internet?", "Internet પર કયું model વપરાય?", "TCP/IP model.", "TCP/IP model."),
    ]},
]

EXAM_QS = [
    X("What is a layered architecture? Give its advantages.", "Layered architecture શું છે? તેના ફાયદા આપો.", 3),
    X("Draw the OSI reference model and explain the function of each layer.", "OSI reference model દોરો અને દરેક layer નું કાર્ય સમજાવો.", 7),
    X("Explain encapsulation and decapsulation with a diagram.", "આકૃતિ સાથે encapsulation અને decapsulation સમજાવો.", 4),
    X("Explain peer-to-peer processes and interfaces in the OSI model.", "OSI model માં peer-to-peer processes અને interfaces સમજાવો.", 3),
    X("Explain the functions of the physical and data link layers.", "Physical અને data link layers નાં કાર્યો સમજાવો.", 4),
    X("Explain the functions of the network and transport layers.", "Network અને transport layers નાં કાર્યો સમજાવો.", 4),
    X("Explain the session and presentation layers.", "Session અને presentation layers સમજાવો.", 4),
    X("Differentiate hop-to-hop and source-to-destination delivery.", "Hop-to-hop અને source-to-destination delivery નો તફાવત આપો.", 3),
    X("Explain the simplex, half duplex and full duplex transmission modes.", "Simplex, half duplex અને full duplex transmission modes સમજાવો.", 3),
    X("Draw the TCP/IP model and explain the function of each layer with protocols.", "TCP/IP model દોરો અને protocols સાથે દરેક layer નું કાર્ય સમજાવો.", 7),
    X("Explain the protocols of the internet layer: IP, ARP, RARP, ICMP, IGMP.", "Internet layer ના protocols: IP, ARP, RARP, ICMP, IGMP સમજાવો.", 4),
    X("Differentiate TCP and UDP.", "TCP અને UDP નો તફાવત આપો.", 4),
    X("Explain the four levels of addresses used in TCP/IP.", "TCP/IP માં વપરાતા addresses ના ચાર સ્તર સમજાવો.", 4),
    X("Compare the OSI and TCP/IP models.", "OSI અને TCP/IP models ની સરખામણી કરો.", 7),
    X("Map the layers of the OSI model to the TCP/IP model with a diagram.", "આકૃતિ સાથે OSI model ના layers ને TCP/IP model સાથે સરખાવો.", 3),
]
