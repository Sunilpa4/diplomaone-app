"""Computer Networks (DI03000051) - Unit 4 notes part B: 4.2 IPv6, 4.3 IPv4 vs IPv6."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

SPEC_EN = tbl(["Address", "Name", "Use"], [
    ("::/128", "Unspecified", "All zeros; used as source when a host does not yet know its address (like 0.0.0.0)"),
    ("::1/128", "Loopback", "Testing own stack (like 127.0.0.1)"),
    ("::ffff:0:0/96", "IPv4-mapped", "Represents an IPv4 address inside IPv6, e.g. ::ffff:192.168.1.5"),
    ("fe80::/10", "Link-local", "Automatically configured on every interface; valid on one link only; never routed"),
    ("fc00::/7 (fd00::/8)", "Unique local", "Private addresses inside an organisation (like 10.x / 192.168.x)"),
    ("ff02::1 / ff02::2", "All-nodes / all-routers multicast", "Replace broadcast on the local link"),
    ("2001:db8::/32", "Documentation", "Used only in books and examples"),
    ("2002::/16, 2001::/32", "6to4, Teredo", "Transition (tunnelling) mechanisms")])
SPEC_GU = tbl(["Address", "નામ", "ઉપયોગ"], [
    ("::/128", "Unspecified", "બધા zeros; host ને હજી પોતાનું address ખબર ન હોય ત્યારે source તરીકે વપરાય (0.0.0.0 જેવું)"),
    ("::1/128", "Loopback", "પોતાના stack નું testing (127.0.0.1 જેવું)"),
    ("::ffff:0:0/96", "IPv4-mapped", "IPv6 ની અંદર IPv4 address દર્શાવે, દા.ત. ::ffff:192.168.1.5"),
    ("fe80::/10", "Link-local", "દરેક interface પર આપમેળે configure; ફક્ત એક link પર માન્ય; ક્યારેય route ન થાય"),
    ("fc00::/7 (fd00::/8)", "Unique local", "સંસ્થાની અંદર private addresses (10.x / 192.168.x જેવા)"),
    ("ff02::1 / ff02::2", "All-nodes / all-routers multicast", "Local link પર broadcast ની જગ્યા લે"),
    ("2001:db8::/32", "Documentation", "ફક્ત પુસ્તકો અને ઉદાહરણોમાં વપરાય"),
    ("2002::/16, 2001::/32", "6to4, Teredo", "Transition (tunnelling) mechanisms")])

CMP_EN = tbl(["Point", "IPv4", "IPv6"], [
    ("Address size", "32 bits", "128 bits"), ("Address space", "2^32 ≈ 4.3 × 10⁹", "2^128 ≈ 3.4 × 10³⁸"),
    ("Notation", "Dotted decimal: 192.168.1.1", "Colon hexadecimal: 2001:db8::1"),
    ("Groups", "4 octets of 8 bits", "8 groups of 16 bits"), ("Header", "Variable, 20-60 bytes, 12+ fields", "Fixed 40 bytes, 8 fields"),
    ("Checksum", "Header checksum present", "No header checksum"), ("Options", "In header (options field)", "Extension headers"),
    ("Fragmentation", "By sender and routers", "By sender only"), ("Broadcast", "Yes", "No; multicast and anycast"),
    ("Configuration", "Manual or DHCP", "SLAAC (auto) or DHCPv6"), ("Security", "IPsec optional", "IPsec designed in"),
    ("NAT", "Widely needed", "Not needed (enough addresses)"), ("Address resolution", "ARP (broadcast)", "Neighbor Discovery (ICMPv6 multicast)"),
    ("QoS", "Type of service field", "Traffic class + flow label"), ("Loopback", "127.0.0.1", "::1"),
    ("DNS record", "A record", "AAAA record")])
CMP_GU = tbl(["મુદ્દો", "IPv4", "IPv6"], [
    ("Address size", "32 bits", "128 bits"), ("Address space", "2^32 ≈ 4.3 × 10⁹", "2^128 ≈ 3.4 × 10³⁸"),
    ("Notation", "Dotted decimal: 192.168.1.1", "Colon hexadecimal: 2001:db8::1"),
    ("Groups", "8 bits ના 4 octets", "16 bits ના 8 groups"), ("Header", "Variable, 20-60 bytes, 12+ fields", "Fixed 40 bytes, 8 fields"),
    ("Checksum", "Header checksum છે", "Header checksum નથી"), ("Options", "Header માં (options field)", "Extension headers"),
    ("Fragmentation", "Sender અને routers દ્વારા", "ફક્ત sender દ્વારા"), ("Broadcast", "હા", "ના; multicast અને anycast"),
    ("Configuration", "Manual કે DHCP", "SLAAC (auto) કે DHCPv6"), ("Security", "IPsec વૈકલ્પિક", "IPsec design માં જ"),
    ("NAT", "વ્યાપક રીતે જોઈએ", "જરૂર નથી (પૂરતા addresses)"), ("Address resolution", "ARP (broadcast)", "Neighbor Discovery (ICMPv6 multicast)"),
    ("QoS", "Type of service field", "Traffic class + flow label"), ("Loopback", "127.0.0.1", "::1"),
    ("DNS record", "A record", "AAAA record")])

V6_AD = adv(["Practically unlimited addresses: every device can have a public address; no NAT needed.", "Simpler, fixed header: faster processing by routers.",
             "Auto-configuration (SLAAC): plug and play.", "Built-in security (IPsec) and better QoS with flow labels.", "Efficient routing: hierarchical addressing, smaller routing tables; better multicast, mobility."],
            ["Not directly compatible with IPv4: needs dual stack, tunnelling or translation during transition.", "Long hexadecimal addresses are hard to remember and type.",
             "Older devices and software may not support it; staff need retraining.", "Larger header (40 bytes) adds overhead for small packets."],
            ["વ્યવહારમાં અમર્યાદિત addresses: દરેક device ને public address મળે; NAT ની જરૂર નહીં.", "સરળ, fixed header: routers દ્વારા ઝડપી processing.",
             "Auto-configuration (SLAAC): plug and play.", "Built-in security (IPsec) અને flow labels સાથે વધુ સારી QoS.", "કાર્યક્ષમ routing: hierarchical addressing, નાનાં routing tables; વધુ સારું multicast, mobility."],
            ["IPv4 સાથે સીધું compatible નથી: transition દરમિયાન dual stack, tunnelling કે translation જોઈએ.", "લાંબા hexadecimal addresses યાદ રાખવા અને લખવા મુશ્કેલ.",
             "જૂનાં devices અને software support ન કરે; staff ને ફરી તાલીમ જોઈએ.", "મોટું header (40 bytes) નાના packets માટે overhead વધારે."])

SEC_4_2 = {
    "title": {"en": "4.2 IPv6", "gu": "4.2 IPv6"},
    "items": [
        T("4.2.1 IPv6: Need and Characteristics", "4.2.1 IPv6: જરૂરિયાત અને લાક્ષણિકતાઓ",
          """<p><b>IPv6</b> (Internet Protocol version 6, also called IPng, next generation) was developed by the IETF (RFC 2460, now RFC 8200) to replace IPv4.</p>
<h4>Need for IPv6</h4>
<ul><li><b>Address depletion:</b> IPv4's 4.3 billion addresses are exhausted, while phones, IoT devices and cloud servers keep growing.</li>
<li>NAT and other workarounds add complexity and break end-to-end communication.</li>
<li>Need for built-in security, better real-time (audio / video) support and simpler router processing.</li></ul>
<h4>Characteristics</h4>
<ul>
<li><b>128-bit address</b> written in colon-hexadecimal notation: 2^128 ≈ 3.4 × 10³⁸ addresses.</li>
<li><b>Simplified, fixed 40-byte base header</b> with only 8 fields; no header checksum; fragmentation only by the source.</li>
<li><b>Extension headers</b> for optional features (routing, fragmentation, authentication, encryption), chained with the <b>next header</b> field.</li>
<li><b>Auto-configuration:</b> stateless address auto-configuration (<b>SLAAC</b>) lets a host build its own address from the router's prefix; DHCPv6 is also available.</li>
<li><b>No broadcast:</b> uses unicast, multicast and the new <b>anycast</b>.</li>
<li><b>Built-in security:</b> IPsec authentication and encryption support.</li>
<li><b>Quality of service:</b> traffic class and <b>flow label</b> fields identify real-time flows.</li>
<li><b>Hierarchical addressing</b> and route aggregation keep routing tables small; better support for mobility.</li>
<li><b>Neighbor Discovery</b> (ICMPv6) replaces ARP.</li>
</ul>
""" + V6_AD[0],
          """<p><b>IPv6</b> (Internet Protocol version 6, જેને IPng, next generation પણ કહે) IETF દ્વારા IPv4 ની જગ્યા લેવા વિકસાવાયો (RFC 2460, હવે RFC 8200).</p>
<h4>IPv6 ની જરૂરિયાત</h4>
<ul><li><b>Address depletion:</b> IPv4 ના 4.3 billion addresses ખલાસ થયા છે, જ્યારે phones, IoT devices અને cloud servers વધતા જાય છે.</li>
<li>NAT અને બીજા ઉપાયો જટિલતા વધારે અને end-to-end communication તોડે.</li>
<li>Built-in security, વધુ સારો real-time (audio / video) support અને સરળ router processing ની જરૂર.</li></ul>
<h4>લાક્ષણિકતાઓ</h4>
<ul>
<li>Colon-hexadecimal notation માં લખાતું <b>128-bit address</b>: 2^128 ≈ 3.4 × 10³⁸ addresses.</li>
<li>ફક્ત 8 fields વાળું <b>સરળ, fixed 40-byte base header</b>; header checksum નહીં; fragmentation ફક્ત source દ્વારા.</li>
<li>વૈકલ્પિક features (routing, fragmentation, authentication, encryption) માટે <b>extension headers</b>, <b>next header</b> field થી સાંકળમાં જોડાયેલા.</li>
<li><b>Auto-configuration:</b> stateless address auto-configuration (<b>SLAAC</b>) થી host router ના prefix પરથી પોતાનું address બનાવે; DHCPv6 પણ ઉપલબ્ધ.</li>
<li><b>Broadcast નહીં:</b> unicast, multicast અને નવું <b>anycast</b> વાપરે.</li>
<li><b>Built-in security:</b> IPsec authentication અને encryption support.</li>
<li><b>Quality of service:</b> traffic class અને <b>flow label</b> fields real-time flows ઓળખે.</li>
<li><b>Hierarchical addressing</b> અને route aggregation routing tables નાના રાખે; mobility માટે વધુ સારો support.</li>
<li><b>Neighbor Discovery</b> (ICMPv6) ARP ની જગ્યા લે.</li>
</ul>
""" + V6_AD[1],
          diagram="cn4_v6hdr"),
        T("4.2.2 IPv6 Address Notation and Abbreviation", "4.2.2 IPv6 Address Notation અને Abbreviation",
          """<p>An IPv6 address is <b>128 bits</b> long. It is written in <b>colon-hexadecimal notation</b>: 8 groups, each of <b>4 hexadecimal digits (16 bits)</b>, separated by colons.</p>
<p>Example: <b>2001:0db8:0000:0000:0000:ff00:0042:8329</b></p>
<h4>Abbreviation rules</h4>
<ol>
<li><b>Leading zeros</b> in any group can be omitted: 0db8 → db8, 0042 → 42, 0000 → 0. (Trailing zeros cannot be removed: ff00 stays ff00.)</li>
<li><b>Zero compression:</b> one run of consecutive all-zero groups can be replaced by a double colon <b>::</b>. It can be used <b>only once</b>, otherwise the number of omitted groups would be ambiguous.</li>
</ol>
<p>2001:0db8:0000:0000:0000:ff00:0042:8329 → 2001:db8:0:0:0:ff00:42:8329 → <b>2001:db8::ff00:42:8329</b></p>
<p><b>Expanding:</b> count the groups present, and replace :: with enough zero groups to make 8; then pad each group to 4 digits.</p>
<p><b>CIDR notation</b> is used for prefixes: 2001:db8:abcd::/48. A URL with an IPv6 address uses brackets: http://[2001:db8::1]:8080/.</p>
<h4>Checking validity (Practical 8)</h4>
<ul><li>Hex digits 0-9, a-f only; at most 4 digits per group.</li><li>Exactly 8 groups, or fewer with exactly one ::.</li><li>:: at most once; dotted decimal alone is IPv4, not IPv6.</li></ul>""",
          """<p>IPv6 address <b>128 bits</b> લાંબું છે. તે <b>colon-hexadecimal notation</b> માં લખાય: 8 groups, દરેક <b>4 hexadecimal અંકો (16 bits)</b> નો, colons થી અલગ.</p>
<p>ઉદાહરણ: <b>2001:0db8:0000:0000:0000:ff00:0042:8329</b></p>
<h4>Abbreviation ના નિયમો</h4>
<ol>
<li>કોઈ પણ group ના <b>આગળના zeros</b> છોડી શકાય: 0db8 → db8, 0042 → 42, 0000 → 0. (પાછળના zeros કાઢી ન શકાય: ff00 એ ff00 જ રહે.)</li>
<li><b>Zero compression:</b> સળંગ all-zero groups ની એક શ્રેણી double colon <b>::</b> થી બદલી શકાય. તે <b>ફક્ત એક જ વાર</b> વાપરી શકાય, નહીં તો છોડેલા groups ની સંખ્યા અસ્પષ્ટ બને.</li>
</ol>
<p>2001:0db8:0000:0000:0000:ff00:0042:8329 → 2001:db8:0:0:0:ff00:42:8329 → <b>2001:db8::ff00:42:8329</b></p>
<p><b>Expand કરવું:</b> હાજર groups ગણો, અને 8 થાય તેટલા zero groups થી :: બદલો; પછી દરેક group ને 4 અંકો સુધી pad કરો.</p>
<p>Prefixes માટે <b>CIDR notation</b> વપરાય: 2001:db8:abcd::/48. IPv6 address વાળા URL માં brackets વપરાય: http://[2001:db8::1]:8080/.</p>
<h4>Validity તપાસવી (Practical 8)</h4>
<ul><li>ફક્ત hex અંકો 0-9, a-f; group દીઠ વધુમાં વધુ 4 અંકો.</li><li>બરાબર 8 groups, અથવા બરાબર એક :: સાથે ઓછા.</li><li>:: વધુમાં વધુ એક વાર; ફક્ત dotted decimal એ IPv4 છે, IPv6 નહીં.</li></ul>""",
          diagram="cn4_v6fmt", examples=["cn4n8", "cn4n9"]),
        T("4.2.3 IPv6 Addressing Modes", "4.2.3 IPv6 Addressing Modes",
          """<p>IPv6 defines three addressing modes (ways a packet is delivered). There is <b>no broadcast</b> in IPv6.</p>
<ol>
<li><b>Unicast (one-to-one):</b> the address identifies a <b>single interface</b>. A packet sent to a unicast address is delivered to that one interface. Example: global unicast 2001:db8::10, link-local fe80::1.</li>
<li><b>Multicast (one-to-many):</b> the address identifies a <b>group of interfaces</b>, possibly on different nodes. A packet is delivered to <b>every member</b> of the group. Multicast addresses start with <b>ff</b> (ff00::/8). Examples: ff02::1 all nodes on the link (replaces broadcast), ff02::2 all routers, ff02::1:2 all DHCP servers.</li>
<li><b>Anycast (one-to-nearest):</b> the same address is assigned to a group of interfaces (usually on different nodes). A packet is delivered to <b>only one</b> of them, the <b>nearest</b> according to the routing protocol. Anycast addresses come from the unicast space and look the same. Used for DNS root servers, CDNs and load balancing.</li>
</ol>
<p>Broadcast is removed because it disturbs every host on the network; its jobs are done by multicast groups (e.g. Neighbor Discovery uses solicited-node multicast instead of ARP broadcasts).</p>""",
          """<p>IPv6 ત્રણ addressing modes (packet પહોંચાડવાની રીતો) વ્યાખ્યાયિત કરે. IPv6 માં <b>broadcast નથી</b>.</p>
<ol>
<li><b>Unicast (એક-થી-એક):</b> address <b>એક interface</b> ઓળખે. Unicast address ને મોકલેલું packet તે એક interface ને પહોંચાડાય. ઉદાહરણ: global unicast 2001:db8::10, link-local fe80::1.</li>
<li><b>Multicast (એક-થી-ઘણા):</b> address <b>interfaces નો group</b> ઓળખે, કદાચ જુદા nodes પર. Packet group ના <b>દરેક સભ્ય</b> ને પહોંચાડાય. Multicast addresses <b>ff</b> થી શરૂ થાય (ff00::/8). ઉદાહરણો: ff02::1 link પરના બધા nodes (broadcast ની જગ્યા), ff02::2 બધા routers, ff02::1:2 બધા DHCP servers.</li>
<li><b>Anycast (એક-થી-નજીકના):</b> સરખું address interfaces ના group (સામાન્ય રીતે જુદા nodes) ને અપાય. Packet તેમાંથી <b>ફક્ત એક</b>, routing protocol મુજબ <b>સૌથી નજીકના</b> ને પહોંચાડાય. Anycast addresses unicast space માંથી આવે અને સરખા દેખાય. DNS root servers, CDNs અને load balancing માં વપરાય.</li>
</ol>
<p>Broadcast દૂર કરાયું કારણ કે તે network ના દરેક host ને ખલેલ પહોંચાડે; તેનાં કામ multicast groups કરે (દા.ત. Neighbor Discovery, ARP broadcasts ને બદલે solicited-node multicast વાપરે).</p>""",
          diagram="cn4_v6modes"),
        T("4.2.4 IPv6 Address Types", "4.2.4 IPv6 Address Types",
          """<p>IPv6 addresses are identified by their leading bits (the <b>type prefix</b>).</p>
<ul>
<li><b>Global unicast (2000::/3):</b> public, globally routable addresses (like public IPv4). Structure: <b>48-bit global routing prefix</b> (assigned by ISP / registry) + <b>16-bit subnet ID</b> (up to 65,536 subnets for a site) + <b>64-bit interface ID</b> (the host part).</li>
<li><b>Link-local (fe80::/10):</b> automatically created on every IPv6 interface; used for communication on the same link (Neighbor Discovery, routing protocols). Routers never forward them.</li>
<li><b>Unique local (fc00::/7, in practice fd00::/8):</b> private addresses for use inside a site, not routed on the Internet (like 10.0.0.0/8).</li>
<li><b>Multicast (ff00::/8):</b> group addresses; the next bits give flags and the <b>scope</b> (ff02 = link, ff05 = site, ff0e = global).</li>
<li><b>Anycast:</b> taken from the unicast space and assigned to several interfaces.</li>
<li><b>Special:</b> loopback ::1, unspecified ::, IPv4-mapped ::ffff:a.b.c.d (see 4.2.5).</li>
</ul>
<h4>Interface ID</h4>
<p>The 64-bit interface ID can be formed from the 48-bit MAC address using <b>modified EUI-64</b> (insert ff:fe in the middle and flip the 7th bit), generated randomly for privacy, or assigned by DHCPv6.</p>""",
          """<p>IPv6 addresses તેમના આગળના bits (<b>type prefix</b>) થી ઓળખાય.</p>
<ul>
<li><b>Global unicast (2000::/3):</b> public, વૈશ્વિક રીતે routable addresses (public IPv4 જેવા). રચના: <b>48-bit global routing prefix</b> (ISP / registry દ્વારા અપાય) + <b>16-bit subnet ID</b> (site માટે 65,536 સુધી subnets) + <b>64-bit interface ID</b> (host ભાગ).</li>
<li><b>Link-local (fe80::/10):</b> દરેક IPv6 interface પર આપમેળે બને; સરખી link પર communication (Neighbor Discovery, routing protocols) માટે. Routers તેમને ક્યારેય forward કરતા નથી.</li>
<li><b>Unique local (fc00::/7, વ્યવહારમાં fd00::/8):</b> site ની અંદર વાપરવા private addresses, Internet પર route ન થાય (10.0.0.0/8 જેવા).</li>
<li><b>Multicast (ff00::/8):</b> group addresses; પછીના bits flags અને <b>scope</b> આપે (ff02 = link, ff05 = site, ff0e = global).</li>
<li><b>Anycast:</b> unicast space માંથી લેવાય અને ઘણા interfaces ને અપાય.</li>
<li><b>Special:</b> loopback ::1, unspecified ::, IPv4-mapped ::ffff:a.b.c.d (જુઓ 4.2.5).</li>
</ul>
<h4>Interface ID</h4>
<p>64-bit interface ID 48-bit MAC address પરથી <b>modified EUI-64</b> (વચ્ચે ff:fe ઉમેરો અને 7મો bit ઉલટાવો) વાપરીને બનાવી શકાય, privacy માટે random બનાવી શકાય, કે DHCPv6 દ્વારા અપાય.</p>""",
          diagram="cn4_v6types"),
        T("4.2.5 IPv6 Special Addresses", "4.2.5 IPv6 Special Addresses",
          """<p>Some IPv6 addresses and prefixes are reserved for special purposes:</p>
""" + SPEC_EN + """
<p>Most IPv6 address space is still unassigned and kept for future use.</p>""",
          """<p>કેટલાક IPv6 addresses અને prefixes ખાસ હેતુઓ માટે reserved છે:</p>
""" + SPEC_GU + """
<p>મોટા ભાગનું IPv6 address space હજી ફાળવાયું નથી અને ભવિષ્ય માટે રાખેલું છે.</p>"""),
    ]}

SEC_4_3 = {
    "title": {"en": "4.3 IPv4 vs IPv6", "gu": "4.3 IPv4 vs IPv6"},
    "items": [
        T("4.3.1 Difference between IPv4 and IPv6", "4.3.1 IPv4 અને IPv6 વચ્ચે તફાવત",
          CMP_EN + """
<h4>Transition from IPv4 to IPv6</h4>
<p>Because the two versions are not directly compatible, three strategies are used while both co-exist:</p>
<ul><li><b>Dual stack:</b> devices run both IPv4 and IPv6 and use whichever the destination supports (most common today).</li>
<li><b>Tunnelling:</b> IPv6 packets are carried inside IPv4 packets across IPv4-only networks (6to4, Teredo).</li>
<li><b>Header translation:</b> a translator (NAT64) converts between IPv6 and IPv4 headers when one side supports only one version.</li></ul>""",
          CMP_GU + """
<h4>IPv4 થી IPv6 તરફ transition</h4>
<p>બંને versions સીધા compatible ન હોવાથી, બંને સાથે ચાલે ત્યારે ત્રણ વ્યૂહરચના વપરાય:</p>
<ul><li><b>Dual stack:</b> devices IPv4 અને IPv6 બંને ચલાવે અને destination જે support કરે તે વાપરે (આજે સૌથી સામાન્ય).</li>
<li><b>Tunnelling:</b> IPv4-only networks પાર IPv6 packets IPv4 packets ની અંદર લઈ જવાય (6to4, Teredo).</li>
<li><b>Header translation:</b> એક બાજુ ફક્ત એક version support કરે ત્યારે translator (NAT64) IPv6 અને IPv4 headers વચ્ચે રૂપાંતર કરે.</li></ul>"""),
    ]}
