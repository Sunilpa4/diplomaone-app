"""Computer Networks (DI03000051) - Unit 4 notes part A: 4.1 IPv4.
Part B (4.2 IPv6, 4.3 IPv4 vs IPv6) is in content_DI03000051_u4_notes_b."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

CLS_EN = tbl(["Class", "Leading bits", "1st octet", "Default mask"], [
    ("A", "0", "0 - 127", "255.0.0.0 (/8)"), ("B", "10", "128 - 191", "255.255.0.0 (/16)"),
    ("C", "110", "192 - 223", "255.255.255.0 (/24)"), ("D", "1110", "224 - 239", "-"),
    ("E", "1111", "240 - 255", "-")])
CLS_GU = tbl(["Class", "આગળના bits", "1st octet", "Default mask"], [
    ("A", "0", "0 - 127", "255.0.0.0 (/8)"), ("B", "10", "128 - 191", "255.255.0.0 (/16)"),
    ("C", "110", "192 - 223", "255.255.255.0 (/24)"), ("D", "1110", "224 - 239", "-"),
    ("E", "1111", "240 - 255", "-")])

CNT_EN = tbl(["Class", "Number of networks", "Hosts per network", "Typical user"], [
    ("A", "2^7 = 128 (126 usable)", "2^24 - 2 = 16,777,214", "Very large organisations"),
    ("B", "2^14 = 16,384", "2^16 - 2 = 65,534", "Medium / large organisations"),
    ("C", "2^21 = 2,097,152", "2^8 - 2 = 254", "Small organisations")])
CNT_GU = tbl(["Class", "Networks ની સંખ્યા", "Network દીઠ hosts", "સામાન્ય user"], [
    ("A", "2^7 = 128 (126 usable)", "2^24 - 2 = 16,777,214", "ખૂબ મોટી સંસ્થાઓ"),
    ("B", "2^14 = 16,384", "2^16 - 2 = 65,534", "મધ્યમ / મોટી સંસ્થાઓ"),
    ("C", "2^21 = 2,097,152", "2^8 - 2 = 254", "નાની સંસ્થાઓ")])

MASKS_EN = tbl(["Prefix", "Mask", "Block size", "Usable hosts"], [
    ("/24", "255.255.255.0", "256", "254"), ("/25", "255.255.255.128", "128", "126"), ("/26", "255.255.255.192", "64", "62"),
    ("/27", "255.255.255.224", "32", "30"), ("/28", "255.255.255.240", "16", "14"), ("/29", "255.255.255.248", "8", "6"),
    ("/30", "255.255.255.252", "4", "2")])
MASKS_GU = tbl(["Prefix", "Mask", "Block size", "Usable hosts"], [
    ("/24", "255.255.255.0", "256", "254"), ("/25", "255.255.255.128", "128", "126"), ("/26", "255.255.255.192", "64", "62"),
    ("/27", "255.255.255.224", "32", "30"), ("/28", "255.255.255.240", "16", "14"), ("/29", "255.255.255.248", "8", "6"),
    ("/30", "255.255.255.252", "4", "2")])

CFCL_EN = tbl(["Classful", "Classless (CIDR)"], [
    ("Network size fixed by class (/8, /16, /24)", "Any prefix length /n"),
    ("Class found from the first octet", "Prefix length must be given (a.b.c.d/n)"),
    ("Wastes many addresses", "Efficient allocation, saves addresses"),
    ("Large routing tables", "Route aggregation (supernetting) reduces tables"),
    ("Obsolete (old method)", "Used on the Internet today")])
CFCL_GU = tbl(["Classful", "Classless (CIDR)"], [
    ("Network size class થી નક્કી (/8, /16, /24)", "કોઈ પણ prefix length /n"),
    ("Class પ્રથમ octet થી મળે", "Prefix length આપવી પડે (a.b.c.d/n)"),
    ("ઘણા addresses વેડફાય", "કાર્યક્ષમ ફાળવણી, addresses બચાવે"),
    ("મોટાં routing tables", "Route aggregation (supernetting) tables ઘટાડે"),
    ("જૂની પદ્ધતિ", "આજે Internet પર વપરાય")])

RES_EN = tbl(["Address / block", "Purpose"], [
    ("10.0.0.0 - 10.255.255.255 (10/8)", "Private, class A"), ("172.16.0.0 - 172.31.255.255 (172.16/12)", "Private, class B"),
    ("192.168.0.0 - 192.168.255.255 (192.168/16)", "Private, class C"), ("127.0.0.0/8 (127.0.0.1)", "Loopback: testing own TCP/IP stack"),
    ("169.254.0.0/16", "APIPA / link-local: self-assigned when DHCP fails"), ("0.0.0.0", "This host (at start-up) / default route"),
    ("255.255.255.255", "Limited broadcast (local network only)"), ("Host bits all 0", "Network address"),
    ("Host bits all 1", "Directed broadcast of that network"), ("224.0.0.0 - 239.255.255.255", "Multicast (class D)"),
    ("240.0.0.0 - 255.255.255.254", "Reserved for future / research (class E)")])
RES_GU = tbl(["Address / block", "હેતુ"], [
    ("10.0.0.0 - 10.255.255.255 (10/8)", "Private, class A"), ("172.16.0.0 - 172.31.255.255 (172.16/12)", "Private, class B"),
    ("192.168.0.0 - 192.168.255.255 (192.168/16)", "Private, class C"), ("127.0.0.0/8 (127.0.0.1)", "Loopback: પોતાના TCP/IP stack નું testing"),
    ("169.254.0.0/16", "APIPA / link-local: DHCP નિષ્ફળ જાય ત્યારે જાતે આપેલું"), ("0.0.0.0", "This host (start-up વખતે) / default route"),
    ("255.255.255.255", "Limited broadcast (ફક્ત local network)"), ("Host bits બધા 0", "Network address"),
    ("Host bits બધા 1", "તે network નો directed broadcast"), ("224.0.0.0 - 239.255.255.255", "Multicast (class D)"),
    ("240.0.0.0 - 255.255.255.254", "ભવિષ્ય / સંશોધન માટે reserved (class E)")])

V4_AD = adv(["Simple, well understood, supported by every device and operating system.", "Small 32-bit address and 20-byte header: low overhead.",
             "Subnetting, CIDR and NAT allow efficient use and sharing of addresses.", "Huge base of tools, routers and trained administrators."],
            ["Address space exhausted: only about 4.3 billion addresses for many more devices.", "Needs NAT, which breaks end-to-end connectivity and adds complexity.",
             "Security (IPsec) is optional, not built in.", "Manual or DHCP configuration needed; variable header and checksum slow routers; large routing tables."],
            ["સરળ, સારી રીતે સમજાયેલું, દરેક device અને operating system દ્વારા supported.", "નાનું 32-bit address અને 20-byte header: ઓછો overhead.",
             "Subnetting, CIDR અને NAT addresses નો કાર્યક્ષમ ઉપયોગ અને વહેંચણી શક્ય બનાવે.", "Tools, routers અને તાલીમ પામેલા administrators નો મોટો આધાર."],
            ["Address space ખલાસ: ઘણાં વધુ devices માટે ફક્ત લગભગ 4.3 billion addresses.", "NAT જોઈએ, જે end-to-end connectivity તોડે અને જટિલતા વધારે.",
             "Security (IPsec) વૈકલ્પિક છે, built in નથી.", "Manual કે DHCP configuration જોઈએ; variable header અને checksum routers ને ધીમા કરે; મોટાં routing tables."])

SEC_4_1 = {
    "title": {"en": "4.1 IPv4", "gu": "4.1 IPv4"},
    "items": [
        T("4.1.1 IP Protocol and IPv4 Address", "4.1.1 IP Protocol અને IPv4 Address",
          """<p>The <b>Internet Protocol (IP)</b> is the network-layer protocol of the TCP/IP suite. It moves packets (<b>datagrams</b>) from the source host to the destination host across many networks, using <b>logical addresses</b> called <b>IP addresses</b>. IP version 4 (<b>IPv4</b>) is the most widely used version; <b>IPv6</b> is its successor.</p>
<p>An <b>IPv4 address</b> is a <b>32-bit</b> address that <b>uniquely and universally</b> defines the connection of a device (host or router interface) to the Internet. Two devices on the Internet can never have the same public address at the same time. A device with two connections (e.g. a router) has two IP addresses.</p>
<h4>Notations</h4>
<ul>
<li><b>Binary notation:</b> 32 bits, usually with a space between each octet (8 bits): <b>11000000 10101000 00001010 00000101</b></li>
<li><b>Dotted-decimal notation:</b> each octet written as a decimal number 0-255, separated by dots: <b>192.168.10.5</b></li>
<li>Hexadecimal notation is sometimes used in programming: C0A80A05.</li>
</ul>
<h4>Conversion</h4>
<p>Each octet uses place values <b>128 64 32 16 8 4 2 1</b>. Binary to decimal: add the place values of the 1 bits. Decimal to binary: subtract the largest place values that fit (192 = 128 + 64 = 11000000).</p>
<p><b>Address space:</b> 2^32 = 4,294,967,296 addresses (about 4.3 billion), less those reserved for special use.</p>""",
          """<p><b>Internet Protocol (IP)</b> એ TCP/IP suite નો network-layer protocol છે. તે <b>IP addresses</b> તરીકે ઓળખાતા <b>logical addresses</b> વાપરીને ઘણા networks પાર source host થી destination host સુધી packets (<b>datagrams</b>) લઈ જાય છે. IP version 4 (<b>IPv4</b>) સૌથી વધુ વપરાતું version છે; <b>IPv6</b> તેનું અનુગામી છે.</p>
<p><b>IPv4 address</b> એ <b>32-bit</b> address છે જે device (host કે router interface) ના Internet સાથેના જોડાણને <b>અનન્ય અને સાર્વત્રિક</b> રીતે ઓળખે છે. Internet પર બે devices એક જ સમયે ક્યારેય સરખું public address ધરાવી ન શકે. બે જોડાણ ધરાવતા device (દા.ત. router) ને બે IP addresses હોય.</p>
<h4>Notations</h4>
<ul>
<li><b>Binary notation:</b> 32 bits, સામાન્ય રીતે દરેક octet (8 bits) વચ્ચે space: <b>11000000 10101000 00001010 00000101</b></li>
<li><b>Dotted-decimal notation:</b> દરેક octet 0-255 ની decimal સંખ્યા તરીકે, dots થી અલગ: <b>192.168.10.5</b></li>
<li>Programming માં ક્યારેક hexadecimal notation વપરાય: C0A80A05.</li>
</ul>
<h4>રૂપાંતર</h4>
<p>દરેક octet place values <b>128 64 32 16 8 4 2 1</b> વાપરે. Binary થી decimal: 1 bits ની place values ઉમેરો. Decimal થી binary: બંધબેસતી સૌથી મોટી place values બાદ કરો (192 = 128 + 64 = 11000000).</p>
<p><b>Address space:</b> 2^32 = 4,294,967,296 addresses (લગભગ 4.3 billion), ખાસ ઉપયોગ માટે reserved હોય તે બાદ.</p>""",
          diagram="cn4_v4fmt", examples=["cn4n1"]),
        T("4.1.2 Characteristics of IPv4", "4.1.2 IPv4 ની લાક્ષણિકતાઓ",
          """<ul>
<li><b>32-bit addressing:</b> about 4.3 billion addresses, written in dotted decimal.</li>
<li><b>Connectionless:</b> each datagram is handled independently; no connection is set up, and datagrams of one message may take different routes and arrive out of order.</li>
<li><b>Best-effort, unreliable delivery:</b> IP does not guarantee delivery, order or freedom from duplicates. Error and flow control are left to upper layers (TCP).</li>
<li><b>Header of 20-60 bytes</b> with a <b>header checksum</b> (checks the header only, not the data).</li>
<li><b>Fragmentation:</b> a datagram larger than the network's MTU can be divided into fragments by the sender or routers; the identification, flags and fragment offset fields reassemble them.</li>
<li><b>TTL (time to live):</b> decremented by each router; the datagram is discarded at 0, preventing endless loops.</li>
<li><b>Protocol field:</b> tells which upper-layer protocol the data belongs to (1 = ICMP, 6 = TCP, 17 = UDP).</li>
<li>Supports <b>unicast, broadcast and multicast</b>; uses classful or classless (CIDR) addressing with subnet masks.</li>
<li>Works with helper protocols: <b>ARP</b> (IP to MAC), <b>ICMP</b> (errors, ping), <b>DHCP</b> (automatic configuration), <b>IGMP</b> (multicast).</li>
</ul>""",
          """<ul>
<li><b>32-bit addressing:</b> લગભગ 4.3 billion addresses, dotted decimal માં લખાય.</li>
<li><b>Connectionless:</b> દરેક datagram સ્વતંત્ર રીતે સંભાળાય; connection set up થતું નથી, અને એક message ના datagrams જુદા routes લઈ ક્રમ બહાર પહોંચી શકે.</li>
<li><b>Best-effort, unreliable delivery:</b> IP delivery, ક્રમ કે duplicates ન હોવાની ખાતરી આપતું નથી. Error અને flow control ઉપરના layers (TCP) પર છોડાય.</li>
<li><b>20-60 bytes નું header</b>, <b>header checksum</b> સાથે (ફક્ત header તપાસે, data નહીં).</li>
<li><b>Fragmentation:</b> network ના MTU કરતાં મોટું datagram sender કે routers દ્વારા fragments માં વહેંચાઈ શકે; identification, flags અને fragment offset fields તેમને ફરી જોડે.</li>
<li><b>TTL (time to live):</b> દરેક router તેને ઘટાડે; 0 થાય ત્યારે datagram કાઢી નખાય, જે અનંત loops અટકાવે.</li>
<li><b>Protocol field:</b> data કયા upper-layer protocol નો છે તે કહે (1 = ICMP, 6 = TCP, 17 = UDP).</li>
<li><b>Unicast, broadcast અને multicast</b> support કરે; subnet masks સાથે classful કે classless (CIDR) addressing વાપરે.</li>
<li>સહાયક protocols સાથે કામ કરે: <b>ARP</b> (IP થી MAC), <b>ICMP</b> (errors, ping), <b>DHCP</b> (automatic configuration), <b>IGMP</b> (multicast).</li>
</ul>""",
          diagram="cn4_v4hdr"),
        T("4.1.3 Advantages and Disadvantages of IPv4", "4.1.3 IPv4 ના ફાયદા અને ગેરફાયદા",
          V4_AD[0] + """<p>The shortage of IPv4 addresses was delayed by <b>CIDR</b>, <b>private addresses with NAT</b> and <b>DHCP</b>, but the permanent solution is <b>IPv6</b>. IANA allocated its last free IPv4 blocks in 2011.</p>""",
          V4_AD[1] + """<p>IPv4 addresses ની અછત <b>CIDR</b>, <b>NAT સાથે private addresses</b> અને <b>DHCP</b> દ્વારા મોડી થઈ, પણ કાયમી ઉકેલ <b>IPv6</b> છે. IANA એ તેના છેલ્લા મુક્ત IPv4 blocks 2011 માં ફાળવ્યા.</p>"""),
        T("4.1.4 Classful Addressing Scheme", "4.1.4 Classful Addressing Scheme",
          """<p>In <b>classful addressing</b> (the original IPv4 scheme), the address space is divided into five classes: <b>A, B, C, D and E</b>. The class decides how many bits are used for the network and how many for the host.</p>
""" + CLS_EN + """
<h4>Finding the class</h4>
<ul><li><b>Binary notation:</b> look at the leading bits: 0 = A, 10 = B, 110 = C, 1110 = D, 1111 = E.</li>
<li><b>Dotted-decimal notation:</b> look at the first octet: 0-127 A, 128-191 B, 192-223 C, 224-239 D, 240-255 E.</li></ul>
<p>Class A, B and C addresses are for unicast (one host); the address is split into a network ID and a host ID (see 4.1.6).</p>""",
          """<p><b>Classful addressing</b> (મૂળ IPv4 પદ્ધતિ) માં address space પાંચ classes માં વહેંચાય છે: <b>A, B, C, D અને E</b>. Class નક્કી કરે કે network માટે કેટલા bits અને host માટે કેટલા bits વપરાય.</p>
""" + CLS_GU + """
<h4>Class શોધવો</h4>
<ul><li><b>Binary notation:</b> આગળના bits જુઓ: 0 = A, 10 = B, 110 = C, 1110 = D, 1111 = E.</li>
<li><b>Dotted-decimal notation:</b> પ્રથમ octet જુઓ: 0-127 A, 128-191 B, 192-223 C, 224-239 D, 240-255 E.</li></ul>
<p>Class A, B અને C addresses unicast (એક host) માટે છે; address network ID અને host ID માં વહેંચાય (જુઓ 4.1.6).</p>""",
          diagram="cn4_classes", examples=["cn4n2"]),
        T("4.1.5 Networks and Hosts in Each Class", "4.1.5 દરેક Class માં Networks અને Hosts",
          """<p>The number of network bits and host bits fixes how many networks a class has and how many hosts each network can hold. The leading class bits are not counted as free network bits.</p>
""" + CNT_EN + """
<ul><li>Class A: 8 network bits - 1 fixed bit = 7 bits → 2^7 networks; 24 host bits.</li>
<li>Class B: 16 - 2 = 14 bits → 2^14 networks; 16 host bits.</li>
<li>Class C: 24 - 3 = 21 bits → 2^21 networks; 8 host bits.</li></ul>
<p>Class D addresses are used for <b>multicasting</b> (one source to a group) and class E is <b>reserved</b>.</p>
<h4>Problem of classful addressing</h4>
<p>Blocks are too large or too small: a class A block (16 million addresses) is far too big for any one organisation, while a class C block (254 hosts) is too small for most. Many addresses were wasted, and the scheme led to early address depletion. It was replaced by <b>classless addressing</b> in 1993.</p>""",
          """<p>Network bits અને host bits ની સંખ્યા નક્કી કરે કે class માં કેટલા networks છે અને દરેક network માં કેટલા hosts રહી શકે. આગળના class bits મુક્ત network bits તરીકે ગણાતા નથી.</p>
""" + CNT_GU + """
<ul><li>Class A: 8 network bits - 1 fixed bit = 7 bits → 2^7 networks; 24 host bits.</li>
<li>Class B: 16 - 2 = 14 bits → 2^14 networks; 16 host bits.</li>
<li>Class C: 24 - 3 = 21 bits → 2^21 networks; 8 host bits.</li></ul>""" + """
<p>Class D addresses <b>multicasting</b> (એક source થી group) માટે વપરાય અને class E <b>reserved</b> છે.</p>
<h4>Classful addressing ની સમસ્યા</h4>
<p>Blocks ખૂબ મોટા કે ખૂબ નાના છે: class A block (16 million addresses) કોઈ એક સંસ્થા માટે ઘણો મોટો, જ્યારે class C block (254 hosts) મોટા ભાગની માટે નાનો. ઘણા addresses વેડફાયા, અને આ પદ્ધતિથી addresses વહેલા ખલાસ થયા. 1993 માં તેની જગ્યા <b>classless addressing</b> એ લીધી.</p>""",
          diagram="cn4_space"),
        T("4.1.6 Network ID, Host ID and Special Addresses of a Block", "4.1.6 Network ID, Host ID અને Block ના ખાસ Addresses",
          """<p>In classes A, B and C, an IP address is divided into two parts:</p>
<ul><li><b>Network ID (netid):</b> identifies the network; all hosts on one network share it.</li>
<li><b>Host ID (hostid):</b> identifies a particular host (interface) on that network.</li></ul>
<p>Class A: netid = 1st octet, hostid = last 3 octets. Class B: netid = first 2 octets, hostid = last 2. Class C: netid = first 3 octets, hostid = last octet.</p>
<h4>Two special addresses in every network</h4>
<ul><li><b>Network address:</b> all host bits = 0 (e.g. 172.16.0.0). It names the network itself and is used in routing tables; it is not assigned to any host.</li>
<li><b>Directed broadcast address:</b> all host bits = 1 (e.g. 172.16.255.255). A packet sent to it reaches every host on that network.</li></ul>
<p>So the number of <b>usable hosts = 2^(host bits) - 2</b>.</p>
<h4>Checking validity (Practical 5)</h4>
<ul><li>Exactly <b>4 octets</b> separated by dots.</li><li>Each octet a decimal number from <b>0 to 255</b>.</li><li>No leading zeros (045) and no mixing of binary and decimal notation.</li></ul>""",
          """<p>Classes A, B અને C માં IP address બે ભાગમાં વહેંચાય:</p>
<ul><li><b>Network ID (netid):</b> network ઓળખે; એક network ના બધા hosts તે વહેંચે.</li>
<li><b>Host ID (hostid):</b> તે network પરના ચોક્કસ host (interface) ને ઓળખે.</li></ul>
<p>Class A: netid = 1st octet, hostid = છેલ્લા 3 octets. Class B: netid = પ્રથમ 2 octets, hostid = છેલ્લા 2. Class C: netid = પ્રથમ 3 octets, hostid = છેલ્લો octet.</p>
<h4>દરેક network ના બે ખાસ addresses</h4>
<ul><li><b>Network address:</b> બધા host bits = 0 (દા.ત. 172.16.0.0). તે network ને જ નામ આપે અને routing tables માં વપરાય; કોઈ host ને અપાતું નથી.</li>
<li><b>Directed broadcast address:</b> બધા host bits = 1 (દા.ત. 172.16.255.255). તેને મોકલેલું packet તે network ના દરેક host સુધી પહોંચે.</li></ul>
<p>તેથી <b>usable hosts = 2^(host bits) - 2</b>.</p>
<h4>Validity તપાસવી (Practical 5)</h4>
<ul><li>Dots થી અલગ બરાબર <b>4 octets</b>.</li><li>દરેક octet <b>0 થી 255</b> ની decimal સંખ્યા.</li><li>આગળ શૂન્ય (045) નહીં અને binary તથા decimal notation નું મિશ્રણ નહીં.</li></ul>""",
          diagram="cn4_netid", examples=["cn4n3"]),
        T("4.1.7 Subnet Mask and Masking", "4.1.7 Subnet Mask અને Masking",
          """<p>A <b>mask</b> (subnet mask) is a 32-bit number in which the <b>1 bits mark the network (and subnet) part</b> and the <b>0 bits mark the host part</b> of an address. The ones are always contiguous from the left.</p>
<ul><li><b>Default masks:</b> class A 255.0.0.0 (/8), class B 255.255.0.0 (/16), class C 255.255.255.0 (/24).</li>
<li><b>Slash (CIDR) notation:</b> /n gives the number of 1 bits; 255.255.240.0 = 11111111.11111111.11110000.00000000 = <b>/20</b>.</li></ul>
<h4>Masking: finding the network address</h4>
<p>The router performs a bit-wise <b>AND</b> of the IP address and the mask: <b>Network address = IP address AND mask</b>. Shortcut: where the mask octet is 255, copy the address octet; where it is 0, write 0; for any other value, AND that octet in binary.</p>
<p>Broadcast address = network address with all host bits set to 1 (IP OR inverted mask).</p>
<p>A host uses its mask to decide whether a destination is on its <b>own network</b> (deliver directly) or on another network (send to the <b>default gateway</b>).</p>
""" + MASKS_EN,
          """<p><b>Mask</b> (subnet mask) એ 32-bit સંખ્યા છે જેમાં <b>1 bits address નો network (અને subnet) ભાગ</b> અને <b>0 bits host ભાગ</b> દર્શાવે. Ones હંમેશા ડાબેથી સળંગ હોય.</p>
<ul><li><b>Default masks:</b> class A 255.0.0.0 (/8), class B 255.255.0.0 (/16), class C 255.255.255.0 (/24).</li>
<li><b>Slash (CIDR) notation:</b> /n એ 1 bits ની સંખ્યા આપે; 255.255.240.0 = 11111111.11111111.11110000.00000000 = <b>/20</b>.</li></ul>
<h4>Masking: network address શોધવું</h4>
<p>Router IP address અને mask નું bit-wise <b>AND</b> કરે: <b>Network address = IP address AND mask</b>. ટૂંકી રીત: જ્યાં mask octet 255 હોય, ત્યાં address octet copy કરો; જ્યાં 0 હોય, 0 લખો; બીજી કોઈ value માટે, તે octet નું binary માં AND કરો.</p>
<p>Broadcast address = બધા host bits 1 કરેલું network address (IP OR inverted mask).</p>
<p>Host તેના mask વાપરીને નક્કી કરે કે destination તેના <b>પોતાના network</b> પર છે (સીધું પહોંચાડો) કે બીજા network પર (<b>default gateway</b> ને મોકલો).</p>
""" + MASKS_GU,
          diagram="cn4_mask", examples=["cn4n4"]),
        T("4.1.8 Subnetting", "4.1.8 Subnetting",
          """<p><b>Subnetting</b> divides one large network into several smaller networks called <b>subnets</b>, by <b>borrowing bits from the host part</b> to form a subnet ID. Address = network ID + subnet ID + host ID.</p>
<h4>Why subnet?</h4>
<ul><li>Reduces broadcast traffic and congestion (smaller broadcast domains).</li><li>Uses addresses efficiently; less waste.</li><li>Better security and management: departments (labs, office, accounts) on separate subnets.</li><li>Outside routers still see one network, so routing tables stay small.</li></ul>
<h4>Steps</h4>
<ol><li>Find the bits needed: for <b>H hosts</b>, choose host bits h with <b>2^h - 2 ≥ H</b>; for <b>S subnets</b>, borrow s bits with <b>2^s ≥ S</b>.</li>
<li>New prefix = old prefix + borrowed bits; write the new mask.</li>
<li>Block size (addresses per subnet) = 2^h = 256 - (interesting mask octet).</li>
<li>List subnets: network addresses go up in steps of the block size; first host = network + 1, broadcast = next network - 1, last host = broadcast - 1.</li></ol>
<p><b>Example (Practical 7):</b> 216.21.5.0/24 with 30 hosts each: 2^5 - 2 = 30, so h = 5, 3 bits borrowed, new mask 255.255.255.224 (/27), 8 subnets of 32 addresses.</p>""",
          """<p><b>Subnetting</b> એક મોટા network ને <b>subnets</b> નામના ઘણા નાના networks માં વહેંચે, subnet ID બનાવવા <b>host ભાગમાંથી bits ઉછીના લઈને</b>. Address = network ID + subnet ID + host ID.</p>
<h4>Subnet શા માટે?</h4>
<ul><li>Broadcast traffic અને congestion ઘટાડે (નાના broadcast domains).</li><li>Addresses નો કાર્યક્ષમ ઉપયોગ; ઓછો બગાડ.</li><li>વધુ સારી security અને management: વિભાગો (labs, office, accounts) અલગ subnets પર.</li><li>બહારના routers હજી એક network જુએ, તેથી routing tables નાના રહે.</li></ul>
<h4>પગલાં</h4>
<ol><li>જરૂરી bits શોધો: <b>H hosts</b> માટે, <b>2^h - 2 ≥ H</b> થાય તેવા host bits h પસંદ કરો; <b>S subnets</b> માટે, <b>2^s ≥ S</b> થાય તેટલા s bits ઉછીના લો.</li>
<li>નવો prefix = જૂનો prefix + ઉછીના bits; નવો mask લખો.</li>
<li>Block size (subnet દીઠ addresses) = 2^h = 256 - (રસપ્રદ mask octet).</li>
<li>Subnets ની યાદી: network addresses block size ના પગલે વધે; first host = network + 1, broadcast = આગલું network - 1, last host = broadcast - 1.</li></ol>
<p><b>ઉદાહરણ (Practical 7):</b> 216.21.5.0/24 દરેકમાં 30 hosts: 2^5 - 2 = 30, તેથી h = 5, 3 bits ઉછીના, નવો mask 255.255.255.224 (/27), 32 addresses ના 8 subnets.</p>""",
          diagram="cn4_subnet", examples=["cn4n5", "cn4n6"]),
        T("4.1.9 Classless Addressing (CIDR)", "4.1.9 Classless Addressing (CIDR)",
          """<p><b>Classless addressing</b>, or <b>CIDR</b> (Classless Inter-Domain Routing), removes classes. An organisation gets a <b>block</b> of addresses of any size that is a power of 2, written in <b>slash notation a.b.c.d/n</b>, where n (the prefix length) is the number of network bits.</p>
<h4>Rules for a block</h4>
<ul><li>The addresses are contiguous.</li><li>The number of addresses is a power of 2: N = 2^(32-n).</li><li>The first address is evenly divisible by N (it is the address with all host bits 0).</li></ul>
<h4>Finding block information from any address a.b.c.d/n</h4>
<ul><li><b>First address</b> = set the rightmost 32-n bits to 0 (AND with the mask).</li><li><b>Last address</b> = set the rightmost 32-n bits to 1.</li><li><b>Number of addresses</b> = 2^(32-n).</li></ul>
<p><b>Supernetting / route aggregation:</b> several contiguous small blocks can be combined and advertised as one larger block (e.g. four /24 blocks as one /22), keeping Internet routing tables small. ISPs and regional registries (APNIC for India) allocate CIDR blocks.</p>
""" + CFCL_EN,
          """<p><b>Classless addressing</b>, અથવા <b>CIDR</b> (Classless Inter-Domain Routing), classes દૂર કરે. સંસ્થાને 2 ની ઘાત હોય તેવા કોઈ પણ કદનો addresses નો <b>block</b> મળે, <b>slash notation a.b.c.d/n</b> માં લખાય, જ્યાં n (prefix length) એ network bits ની સંખ્યા છે.</p>
<h4>Block ના નિયમો</h4>
<ul><li>Addresses સળંગ હોય.</li><li>Addresses ની સંખ્યા 2 ની ઘાત: N = 2^(32-n).</li><li>પ્રથમ address N થી નિઃશેષ ભાગી શકાય (બધા host bits 0 વાળું address).</li></ul>
<h4>કોઈ પણ address a.b.c.d/n પરથી block માહિતી</h4>
<ul><li><b>First address</b> = જમણી બાજુના 32-n bits 0 કરો (mask સાથે AND).</li><li><b>Last address</b> = જમણી બાજુના 32-n bits 1 કરો.</li><li><b>Addresses ની સંખ્યા</b> = 2^(32-n).</li></ul>
<p><b>Supernetting / route aggregation:</b> ઘણા સળંગ નાના blocks ભેગા કરી એક મોટા block તરીકે જાહેર કરી શકાય (દા.ત. ચાર /24 blocks એક /22 તરીકે), જેથી Internet routing tables નાના રહે. ISPs અને regional registries (ભારત માટે APNIC) CIDR blocks ફાળવે.</p>
""" + CFCL_GU,
          diagram="cn4_cidr", examples=["cn4n7"]),
        T("4.1.10 Reserved (Special) IPv4 Addresses", "4.1.10 Reserved (Special) IPv4 Addresses",
          """<p>Some IPv4 addresses are <b>reserved</b> for special purposes and cannot be assigned as normal public host addresses.</p>
""" + RES_EN + """
<h4>Private addresses and NAT</h4>
<p>Private addresses (RFC 1918) can be used freely inside any home, college or company network, but they are <b>not routed on the Internet</b>. Many organisations reuse the same private ranges. A router with <b>NAT</b> (Network Address Translation) replaces the private source address with its single public address when packets go to the Internet, so hundreds of devices can share one public IP.</p>
<p><b>Loopback:</b> <b>ping 127.0.0.1</b> tests the computer's own TCP/IP software; the packet never leaves the machine. <b>APIPA</b> (169.254.x.x) appears in ipconfig when a PC cannot reach a DHCP server, a useful troubleshooting sign.</p>""",
          """<p>કેટલાક IPv4 addresses ખાસ હેતુઓ માટે <b>reserved</b> છે અને સામાન્ય public host addresses તરીકે આપી શકાતા નથી.</p>
""" + RES_GU + """
<h4>Private addresses અને NAT</h4>
<p>Private addresses (RFC 1918) કોઈ પણ ઘર, college કે company network ની અંદર મુક્ત રીતે વાપરી શકાય, પણ તે <b>Internet પર route થતા નથી</b>. ઘણી સંસ્થાઓ સરખી private ranges ફરી વાપરે. <b>NAT</b> (Network Address Translation) વાળું router packets Internet પર જાય ત્યારે private source address ને તેના એક public address થી બદલે, જેથી સેંકડો devices એક public IP વહેંચી શકે.</p>
<p><b>Loopback:</b> <b>ping 127.0.0.1</b> computer નું પોતાનું TCP/IP software તપાસે; packet machine છોડતું નથી. PC DHCP server સુધી ન પહોંચે ત્યારે ipconfig માં <b>APIPA</b> (169.254.x.x) દેખાય, જે troubleshooting માટે ઉપયોગી સંકેત છે.</p>""",
          diagram="cn4_reserved"),
    ]}

from content_DI03000051_u4_notes_b import SEC_4_2, SEC_4_3  # noqa: E402

NOTES = [SEC_4_1, SEC_4_2, SEC_4_3]
