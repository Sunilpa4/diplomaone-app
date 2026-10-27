"""Computer Networks (DI03000051) - Unit 4 extras: IP addressing numericals (all computed with cn_ip), equations, viva, exam questions."""
from content_DI03000011_u1_extras import N, E, V, X
from content_DI03000041_u1_notes import tbl
import cn_ip as ip

PV = [128, 64, 32, 16, 8, 4, 2, 1]


def pv_sum(bits):
    vals = [str(p) for p, b in zip(PV, bits) if b == "1"]
    return (" + ".join(vals) if vals else "0") + f" = {int(bits, 2)}"


# n1: conversions
a1 = "192.168.10.5"
b1 = "10000001 00001011 00001011 11101111"
c1 = "11000001 10000011 00011011 11111111"


def conv_body(lang):
    t = {"en": ("Decimal to binary", "Binary to decimal (add place values 128 64 32 16 8 4 2 1)"),
         "gu": ("Decimal થી binary", "Binary થી decimal (place values 128 64 32 16 8 4 2 1 ઉમેરો)")}[lang]
    s = f"<p><b>(a) {t[0]}:</b></p><ul>"
    for o in ip.octets(a1):
        s += f"<li>{o} = {pv_sum(f'{o:08b}').split(' = ')[0]} = {o:08b}</li>"
    s += f"</ul><p>{a1} = <b>{ip.to_bin(a1)}</b></p>"
    for tag, b in (("b", b1), ("c", c1)):
        s += f"<p><b>({tag}) {t[1]}:</b></p><ul>"
        for o in b.split():
            s += f"<li>{o} = {pv_sum(o)}</li>"
        s += f"</ul><p>{b} = <b>{ip.bin_to_ip(b)}</b></p>"
    return s


n1 = N("cn4n1", f"(a) Convert {a1} to binary notation. Convert to dotted-decimal: (b) {b1}  (c) {c1}",
       f"(a) {a1} ને binary notation માં ફેરવો. Dotted-decimal માં ફેરવો: (b) {b1}  (c) {c1}",
       conv_body("en"), conv_body("gu"))

# n2: find the class
cls_in = ["00000001 00001011 00001011 11101111", "11000001 10000011 00011011 11111111", "14.23.120.8", "252.5.15.111",
          "134.11.78.56", "227.12.14.87"]


def cls_body(lang):
    rows = []
    for s in cls_in:
        if " " in s:
            c = ip.ip_class(ip.bin_to_ip(s))
            lead = ip.CLASS_INFO[c][1]
            how = (f"first bits {lead}" if lang == "en" else f"પ્રથમ bits {lead}")
        else:
            c = ip.ip_class(s)
            how = (f"first octet {s.split('.')[0]}" if lang == "en" else f"પ્રથમ octet {s.split('.')[0]}")
        rows.append((s, how, c))
    head = ["Address", "Reason", "Class"] if lang == "en" else ["Address", "કારણ", "Class"]
    return tbl(head, rows)


n2 = N("cn4n2", "Find the class of each address: " + ";  ".join(cls_in),
       "દરેક address નો class શોધો: " + ";  ".join(cls_in), cls_body("en"), cls_body("gu"))

# n3: Practical 5 validity
p5 = ["298.27.5.6", "1.4.5.5", "11100010.23.14.67", "192.226.12.11.9"]


def p5_body(lang):
    s = ""
    for i, a in enumerate(p5):
        ok, ren, rgu = ip.v4_check(a)
        tag = "abcd"[i]
        if ok:
            c = ip.classful(a)
            if lang == "en":
                s += (f"<p><b>({tag}) {a}</b> → <b>Valid.</b> First octet {a.split('.')[0]} is in 0-127, so <b>class {c['class']}</b>. "
                      f"Network ID = <b>{c['net_id']}</b> (network address {c['network']}), Host ID = <b>{c['host_id']}</b>.</p>")
            else:
                s += (f"<p><b>({tag}) {a}</b> → <b>Valid.</b> પ્રથમ octet {a.split('.')[0]} એ 0-127 માં છે, તેથી <b>class {c['class']}</b>. "
                      f"Network ID = <b>{c['net_id']}</b> (network address {c['network']}), Host ID = <b>{c['host_id']}</b>.</p>")
        else:
            s += f"<p><b>({tag}) {a}</b> → <b>Invalid.</b> {ren if lang == 'en' else rgu}</p>"
    return s


n3 = N("cn4n3", "Practical 5: Determine whether the following IPv4 addresses are valid or invalid. If valid, find the class, Network ID and Host ID; if invalid, write the reason. (a) 298.27.5.6 (b) 1.4.5.5 (c) 11100010.23.14.67 (d) 192.226.12.11.9",
       "Practical 5: નીચેના IPv4 addresses valid છે કે invalid તે નક્કી કરો. Valid હોય તો class, Network ID અને Host ID શોધો; invalid હોય તો કારણ લખો. (a) 298.27.5.6 (b) 1.4.5.5 (c) 11100010.23.14.67 (d) 192.226.12.11.9",
       p5_body("en"), p5_body("gu"))

# n4: Practical 6 class and network address
p6 = [("172.16.2.10", "255.255.255.0"), ("10.6.24.20", "255.255.240.0"), ("10.30.36.12", "255.255.255.0")]


def p6_body(lang):
    rows, extra = [], ""
    for a, m in p6:
        net = ip.to_ip(ip.to_int(a) & ip.to_int(m))
        rows.append((a, m, ip.ip_class(a), f"{net} (/{ip.mask_prefix(m)})"))
        for k, (ao, mo) in enumerate(zip(ip.octets(a), ip.octets(m))):
            if mo not in (0, 255):
                extra += (f"<p>{a}: octet {k + 1}: {ao} AND {mo} = {ao:08b} AND {mo:08b} = {ao & mo:08b} = <b>{ao & mo}</b></p>")
    head = ["IPv4 address", "Subnet mask", "Class", "Network (subnet) address"] if lang == "en" else \
        ["IPv4 address", "Subnet mask", "Class", "Network (subnet) address"]
    rule = ("<p>Network address = IP AND mask. Octets with mask 255 are copied, mask 0 gives 0.</p>" if lang == "en" else
            "<p>Network address = IP AND mask. Mask 255 વાળા octets copy થાય, mask 0 થી 0 મળે.</p>")
    return rule + extra + tbl(head, rows)


n4 = N("cn4n4", "Practical 6: Determine the class and network address for: 172.16.2.10 / 255.255.255.0;  10.6.24.20 / 255.255.240.0;  10.30.36.12 / 255.255.255.0",
       "Practical 6: Class અને network address શોધો: 172.16.2.10 / 255.255.255.0;  10.6.24.20 / 255.255.240.0;  10.30.36.12 / 255.255.255.0",
       p6_body("en"), p6_body("gu"))

# n5: Practical 7 subnetting
r7 = ip.subnet_for_hosts("216.21.5.0", 24, 30)


def sub_table(r, lang):
    head = ["Subnet", "Network", "Host range", "Broadcast"] if lang == "en" else ["Subnet", "Network", "Host range", "Broadcast"]
    return tbl(head, [(str(i + 1), net, f"{fh} - {lh}", bc) for i, (net, fh, lh, bc) in enumerate(r["subnets"])])


def p7_body(lang):
    if lang == "en":
        s = (f"<p>Given /24 (class C), 8 host bits. Hosts needed = 30: 2^h - 2 ≥ 30 → h = {r7['h']} (2^5 - 2 = 30).</p>"
             f"<p>Bits borrowed = 8 - {r7['h']} = {r7['borrowed']}; subnets = 2^{r7['borrowed']} = <b>{r7['count']}</b></p>"
             f"<p>New mask = /{r7['prefix']} = <b>{r7['mask']}</b>; block size = 256 - 224 = {r7['size']}; usable hosts = {r7['usable']}</p>")
    else:
        s = (f"<p>આપેલ /24 (class C), 8 host bits. જરૂરી hosts = 30: 2^h - 2 ≥ 30 → h = {r7['h']} (2^5 - 2 = 30).</p>"
             f"<p>ઉછીના bits = 8 - {r7['h']} = {r7['borrowed']}; subnets = 2^{r7['borrowed']} = <b>{r7['count']}</b></p>"
             f"<p>નવો mask = /{r7['prefix']} = <b>{r7['mask']}</b>; block size = 256 - 224 = {r7['size']}; usable hosts = {r7['usable']}</p>")
    return s + sub_table(r7, lang)


n5 = N("cn4n5", "Practical 7: Subnet the IP address 216.21.5.0/24 into subnets of 30 hosts each. Find the subnet mask, number of subnets and the range of each subnet.",
       "Practical 7: IP address 216.21.5.0/24 ને દરેક 30 hosts ના subnets માં વહેંચો. Subnet mask, subnets ની સંખ્યા અને દરેક subnet ની range શોધો.",
       p7_body("en"), p7_body("gu"))

# n6: 4 subnets
r6 = ip.subnet_for_count("192.168.1.0", 24, 4)


def n6_body(lang):
    if lang == "en":
        s = (f"<p>Subnets needed = 4: 2^s ≥ 4 → s = {r6['borrowed']} bits borrowed.</p>"
             f"<p>New prefix = 24 + {r6['borrowed']} = /{r6['prefix']}; mask = <b>{r6['mask']}</b></p>"
             f"<p>Host bits = {32 - r6['prefix']}; block size = {r6['size']}; usable hosts per subnet = 2^{32 - r6['prefix']} - 2 = <b>{r6['usable']}</b></p>")
    else:
        s = (f"<p>જરૂરી subnets = 4: 2^s ≥ 4 → s = {r6['borrowed']} bits ઉછીના.</p>"
             f"<p>નવો prefix = 24 + {r6['borrowed']} = /{r6['prefix']}; mask = <b>{r6['mask']}</b></p>"
             f"<p>Host bits = {32 - r6['prefix']}; block size = {r6['size']}; subnet દીઠ usable hosts = 2^{32 - r6['prefix']} - 2 = <b>{r6['usable']}</b></p>")
    return s + sub_table(r6, lang)


n6 = N("cn4n6", "Divide the network 192.168.1.0/24 into 4 equal subnets. Find the new subnet mask, hosts per subnet and the address range of each subnet.",
       "Network 192.168.1.0/24 ને 4 સરખા subnets માં વહેંચો. નવો subnet mask, subnet દીઠ hosts અને દરેક subnet ની address range શોધો.",
       n6_body("en"), n6_body("gu"))

# n7: CIDR blocks
c7 = [("205.16.37.39", 28), ("167.199.170.82", 27)]


def n7_body(lang):
    s = ""
    for i, (a, p) in enumerate(c7):
        bl = ip.block(a, p)
        h = 32 - p
        o4 = ip.octets(a)[3]
        b4 = f"{o4:08b}"
        net4 = ip.octets(bl["network"])[3]
        bc4 = ip.octets(bl["broadcast"])[3]
        lab = "host bits"
        s += (f"<p><b>({'ab'[i]}) {a}/{p}</b>: {lab} = 32 - {p} = {h}; last octet {o4} = {b4[:8 - h]} {b4[8 - h:]}</p><ul>"
              f"<li>First address: {b4[:8 - h]} {'0' * h} = {net4} → <b>{bl['network']}</b></li>"
              f"<li>Last address: {b4[:8 - h]} {'1' * h} = {bc4} → <b>{bl['broadcast']}</b></li>"
              + (f"<li>Number of addresses = 2^{h} = <b>{bl['count']}</b> (usable {bl['hosts']}); mask {bl['mask']}</li></ul>" if lang == "en" else
               f"<li>Addresses ની સંખ્યા = 2^{h} = <b>{bl['count']}</b> (usable {bl['hosts']}); mask {bl['mask']}</li></ul>"))
    return s


n7 = N("cn4n7", "In classless addressing, find the first address, last address and number of addresses in the block for: (a) 205.16.37.39/28 (b) 167.199.170.82/27",
       "Classless addressing માં block નું first address, last address અને addresses ની સંખ્યા શોધો: (a) 205.16.37.39/28 (b) 167.199.170.82/27",
       n7_body("en"), n7_body("gu"))

# n8: IPv6 abbreviate / expand
comp_in = ["2001:0db8:0000:0000:0000:ff00:0042:8329", "fe80:0000:0000:0000:0202:b3ff:fe1e:8329", "2001:0db8:0001:0000:0000:0ab9:c0a8:0102"]
exp_in = ["2001:db8::1", "fe80::1:2", "::1"]


def n8_body(lang):
    t = ("Abbreviate", "Expand") if lang == "en" else ("ટૂંકું કરો", "Expand કરો")
    s = f"<p><b>{t[0]}</b> (remove leading zeros, then :: once for the longest zero run):</p><ul>"
    for a in comp_in:
        step = ":".join(g.lstrip("0") or "0" for g in a.split(":"))
        s += f"<li>{a} → {step} → <b>{ip.v6_compress(a)}</b></li>"
    s += f"</ul><p><b>{t[1]}</b> (fill :: with zero groups to make 8, pad each group to 4 digits):</p><ul>"
    for a in exp_in:
        present = len([g for g in a.replace("::", ":").split(":") if g])
        s += f"<li>{a}: {present} group(s) present, :: = {8 - present} zero groups → <b>{ip.v6_expand(a)}</b></li>"
    return s + "</ul>"


n8 = N("cn4n8", "Write in shortest form: " + ";  ".join(comp_in) + ".  Write in full form: " + ";  ".join(exp_in),
       "ટૂંકા સ્વરૂપમાં લખો: " + ";  ".join(comp_in) + ".  પૂર્ણ સ્વરૂપમાં લખો: " + ";  ".join(exp_in),
       n8_body("en"), n8_body("gu"))

# n9: Practical 8 IPv6 validity
p8 = ["2001:db8:3333:4444:5555:6666:7777:8888", "2001:0db8:0001:0000:0000:0ab9:C0A8:0102", "225.1.4.2", "::", "fe80:2030:31:24"]
P8_NOTE = {"2001:db8:3333:4444:5555:6666:7777:8888": ("8 groups of hex digits; leading zero of 0db8 omitted.", "Hex અંકોના 8 groups; 0db8 નો આગળનો zero છોડેલો."),
           "2001:0db8:0001:0000:0000:0ab9:C0A8:0102": ("8 full groups; uppercase hex is allowed. Short form: ", "8 પૂર્ણ groups; uppercase hex માન્ય છે. ટૂંકું સ્વરૂપ: "),
           "::": ("The unspecified address (all 128 bits zero).", "Unspecified address (બધા 128 bits zero).")}


def p8_body(lang):
    s = ("<p>(The syllabus prints some addresses with spaces after the colons; spaces are not part of an address and are ignored here.)</p>" if lang == "en" else
         "<p>(Syllabus માં કેટલાક addresses colons પછી spaces સાથે છપાયા છે; spaces address નો ભાગ નથી અને અહીં અવગણ્યા છે.)</p>")
    for i, a in enumerate(p8):
        ok, ren, rgu = ip.v6_check(a)
        tag = "abcde"[i]
        if ok:
            nt = P8_NOTE[a][0 if lang == "en" else 1]
            if nt.endswith(": "):
                nt += ip.v6_compress(a)
            s += f"<p><b>({tag}) {a}</b> → <b>Valid.</b> {nt}</p>"
        else:
            s += f"<p><b>({tag}) {a}</b> → <b>Invalid.</b> {ren if lang == 'en' else rgu}</p>"
    return s


n9 = N("cn4n9", "Practical 8: Identify valid IPv6 addresses; for invalid ones write the reason: (a) 2001:db8:3333:4444:5555:6666:7777:8888 (b) 2001:0db8:0001:0000:0000:0ab9:C0A8:0102 (c) 225.1.4.2 (d) :: (e) fe80:2030:31:24",
       "Practical 8: Valid IPv6 addresses ઓળખો; invalid માટે કારણ લખો: (a) 2001:db8:3333:4444:5555:6666:7777:8888 (b) 2001:0db8:0001:0000:0000:0ab9:C0A8:0102 (c) 225.1.4.2 (d) :: (e) fe80:2030:31:24",
       p8_body("en"), p8_body("gu"))

NUMERICALS = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

EQUATIONS = [
    {"title": {"en": "IPv4 counting", "gu": "IPv4 ગણતરી"}, "items": [
        E("Total IPv4 addresses", "કુલ IPv4 addresses", "2^32 = 4,294,967,296", "32-bit address", "32-bit address"),
        E("Usable hosts", "Usable hosts", "Hosts = 2^h - 2", "h = host bits; minus network and broadcast address", "h = host bits; network અને broadcast address બાદ"),
        E("Number of subnets", "Subnets ની સંખ્યા", "Subnets = 2^s", "s = bits borrowed from the host part", "s = host ભાગમાંથી ઉછીના bits"),
        E("Addresses in a block", "Block માં addresses", "N = 2^(32 - n)", "n = prefix length in a.b.c.d/n", "a.b.c.d/n માં n = prefix length"),
        E("Block size", "Block size", "Block = 256 - mask octet", "e.g. /27: 256 - 224 = 32", "દા.ત. /27: 256 - 224 = 32"),
    ]},
    {"title": {"en": "Masking", "gu": "Masking"}, "items": [
        E("Network address", "Network address", "Network = IP AND mask", "Host bits set to 0", "Host bits 0 કરાય"),
        E("Broadcast address", "Broadcast address", "Broadcast = network OR (NOT mask)", "Host bits set to 1", "Host bits 1 કરાય"),
        E("Host range", "Host range", "First = network + 1,  Last = broadcast - 1", "Usable addresses lie between network and broadcast", "Usable addresses network અને broadcast ની વચ્ચે"),
        E("Default masks", "Default masks", "A /8 = 255.0.0.0,  B /16 = 255.255.0.0,  C /24 = 255.255.255.0", "Number after / = count of 1 bits in the mask", "/ પછીની સંખ્યા = mask માં 1 bits ની સંખ્યા"),
        E("Class from first octet", "First octet પરથી class", "A 0-127,  B 128-191,  C 192-223,  D 224-239,  E 240-255", "Leading bits 0, 10, 110, 1110, 1111", "આગળના bits 0, 10, 110, 1110, 1111"),
    ]},
    {"title": {"en": "IPv6", "gu": "IPv6"}, "items": [
        E("IPv6 address space", "IPv6 address space", "2^128 ≈ 3.4 × 10³⁸", "8 groups × 16 bits", "8 groups × 16 bits"),
        E("Global unicast structure", "Global unicast રચના", "48-bit prefix + 16-bit subnet + 64-bit interface ID", "Prefix from ISP; 2^16 subnets per site", "Prefix ISP પાસેથી; site દીઠ 2^16 subnets"),
    ]},
]

VIVA = [
    {"title": {"en": "IPv4 basics", "gu": "IPv4 basics"}, "items": [
        V("What is an IP address?", "IP address એટલે શું?", "A 32-bit (IPv4) logical address that uniquely identifies a device's connection on a network or the Internet.", "Network કે Internet પર device ના જોડાણને અનન્ય રીતે ઓળખતું 32-bit (IPv4) logical address."),
        V("Why is IP called connectionless and unreliable?", "IP ને connectionless અને unreliable કેમ કહે?", "Each datagram is sent independently without setting up a connection, and IP does not guarantee delivery or order (best effort).", "દરેક datagram connection set up કર્યા વગર સ્વતંત્ર રીતે મોકલાય, અને IP delivery કે ક્રમની ખાતરી આપતું નથી (best effort)."),
        V("What is the use of TTL?", "TTL નો ઉપયોગ શું?", "Time to live limits the number of hops; each router reduces it by 1 and the packet is discarded at 0, preventing loops.", "Time to live hops ની સંખ્યા મર્યાદિત કરે; દરેક router તેને 1 ઘટાડે અને 0 થતાં packet કાઢી નખાય, જે loops અટકાવે."),
        V("Which class does 172.16.2.10 belong to?", "172.16.2.10 કયા class નું છે?", "Class B, because the first octet 172 lies in 128-191.", "Class B, કારણ કે પ્રથમ octet 172 એ 128-191 માં છે."),
        V("Why do we subtract 2 when counting hosts?", "Hosts ગણતાં 2 શા માટે બાદ કરીએ?", "The all-0s host address is the network address and the all-1s is the broadcast address; neither can be assigned.", "All-0s host address એ network address અને all-1s એ broadcast address છે; બેમાંથી એક પણ આપી શકાતું નથી."),
        V("What is the loopback address?", "Loopback address કયું છે?", "127.0.0.1 (127.0.0.0/8) in IPv4 and ::1 in IPv6; used to test the local TCP/IP stack.", "IPv4 માં 127.0.0.1 (127.0.0.0/8) અને IPv6 માં ::1; local TCP/IP stack તપાસવા વપરાય."),
        V("List the private IPv4 ranges.", "Private IPv4 ranges ની યાદી આપો.", "10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16.", "10.0.0.0/8, 172.16.0.0/12 અને 192.168.0.0/16."),
        V("What is APIPA?", "APIPA એટલે શું?", "Automatic Private IP Addressing: a 169.254.x.x address a PC gives itself when no DHCP server answers.", "Automatic Private IP Addressing: કોઈ DHCP server જવાબ ન આપે ત્યારે PC પોતાને આપતું 169.254.x.x address."),
    ]},
    {"title": {"en": "Masks, subnets and CIDR", "gu": "Masks, subnets અને CIDR"}, "items": [
        V("What is a subnet mask?", "Subnet mask એટલે શું?", "A 32-bit value whose 1 bits mark the network part and 0 bits the host part; IP AND mask gives the network address.", "32-bit value જેના 1 bits network ભાગ અને 0 bits host ભાગ દર્શાવે; IP AND mask થી network address મળે."),
        V("What does /26 mean?", "/26 નો અર્થ શું?", "The first 26 bits are the network part: mask 255.255.255.192, 64 addresses, 62 usable hosts.", "પ્રથમ 26 bits network ભાગ છે: mask 255.255.255.192, 64 addresses, 62 usable hosts."),
        V("Why is subnetting done?", "Subnetting શા માટે કરાય?", "To divide a large network into smaller ones: less broadcast traffic, better security and management, efficient use of addresses.", "મોટા network ને નાનામાં વહેંચવા: ઓછો broadcast traffic, વધુ સારી security અને management, addresses નો કાર્યક્ષમ ઉપયોગ."),
        V("What is CIDR?", "CIDR એટલે શું?", "Classless Inter-Domain Routing: addresses allocated in blocks of any power-of-2 size, written a.b.c.d/n.", "Classless Inter-Domain Routing: 2 ની કોઈ પણ ઘાત જેટલા blocks માં addresses ફાળવાય, a.b.c.d/n તરીકે લખાય."),
        V("What is supernetting?", "Supernetting એટલે શું?", "Combining several contiguous networks into one larger block (route aggregation) to reduce routing table size.", "Routing table નું કદ ઘટાડવા ઘણા સળંગ networks ને એક મોટા block માં ભેગા કરવા (route aggregation)."),
        V("What is NAT?", "NAT એટલે શું?", "Network Address Translation: a router replaces private addresses with its public address, so many devices share one public IP.", "Network Address Translation: router private addresses ને તેના public address થી બદલે, જેથી ઘણા devices એક public IP વહેંચે."),
    ]},
    {"title": {"en": "IPv6", "gu": "IPv6"}, "items": [
        V("What is the size of an IPv6 address?", "IPv6 address નું કદ કેટલું?", "128 bits, written as 8 groups of 4 hex digits separated by colons.", "128 bits, colons થી અલગ 4 hex અંકોના 8 groups તરીકે લખાય."),
        V("Why is :: allowed only once?", ":: ફક્ત એક જ વાર કેમ માન્ય?", "If used twice, it would be impossible to know how many zero groups each :: stands for.", "બે વાર વપરાય તો દરેક :: કેટલા zero groups દર્શાવે છે તે જાણવું અશક્ય બને."),
        V("Name the IPv6 addressing modes.", "IPv6 addressing modes ના નામ આપો.", "Unicast (one-to-one), multicast (one-to-many) and anycast (one-to-nearest). There is no broadcast.", "Unicast (એક-થી-એક), multicast (એક-થી-ઘણા) અને anycast (એક-થી-નજીકના). Broadcast નથી."),
        V("What is a link-local address?", "Link-local address એટલે શું?", "An automatically configured fe80::/10 address valid only on the local link; routers do not forward it.", "આપમેળે configure થતું fe80::/10 address ફક્ત local link પર માન્ય; routers તેને forward કરતા નથી."),
        V("What is the size of the IPv6 base header?", "IPv6 base header નું કદ?", "Fixed 40 bytes, with extension headers for options.", "Fixed 40 bytes, options માટે extension headers સાથે."),
        V("What is SLAAC?", "SLAAC એટલે શું?", "Stateless Address Auto-Configuration: a host forms its IPv6 address from the router's prefix and its interface ID, without DHCP.", "Stateless Address Auto-Configuration: host DHCP વગર router ના prefix અને પોતાના interface ID પરથી IPv6 address બનાવે."),
        V("Which DNS record stores an IPv6 address?", "IPv6 address કયા DNS record માં રહે?", "The AAAA (quad-A) record; IPv4 uses the A record.", "AAAA (quad-A) record; IPv4 A record વાપરે."),
        V("Name the IPv4-to-IPv6 transition methods.", "IPv4-થી-IPv6 transition પદ્ધતિઓના નામ આપો.", "Dual stack, tunnelling and header translation (NAT64).", "Dual stack, tunnelling અને header translation (NAT64)."),
    ]},
]

EXAM_QS = [
    X("Explain the IPv4 address with its notations. Convert 192.168.10.5 to binary.", "IPv4 address તેની notations સાથે સમજાવો. 192.168.10.5 ને binary માં ફેરવો.", 3),
    X("List the characteristics of IPv4.", "IPv4 ની લાક્ષણિકતાઓની યાદી આપો.", 3),
    X("Write the advantages and disadvantages of IPv4.", "IPv4 ના ફાયદા અને ગેરફાયદા લખો.", 3),
    X("Explain the classful addressing scheme with a diagram.", "આકૃતિ સાથે classful addressing scheme સમજાવો.", 4),
    X("Determine whether the given IPv4 addresses are valid. If valid, find class, network ID and host ID.", "આપેલા IPv4 addresses valid છે કે નહીં તે નક્કી કરો. Valid હોય તો class, network ID અને host ID શોધો.", 4),
    X("What is a subnet mask? Find the network address of 10.6.24.20 with mask 255.255.240.0.", "Subnet mask એટલે શું? Mask 255.255.240.0 સાથે 10.6.24.20 નું network address શોધો.", 4),
    X("Subnet 216.21.5.0/24 into subnets of 30 hosts each.", "216.21.5.0/24 ને દરેક 30 hosts ના subnets માં વહેંચો.", 7),
    X("Explain classless addressing. Find the first and last address of the block 205.16.37.39/28.", "Classless addressing સમજાવો. Block 205.16.37.39/28 નું first અને last address શોધો.", 4),
    X("Differentiate classful and classless addressing.", "Classful અને classless addressing નો તફાવત આપો.", 3),
    X("Explain reserved (special) IPv4 addresses.", "Reserved (special) IPv4 addresses સમજાવો.", 3),
    X("Explain the characteristics of IPv6.", "IPv6 ની લાક્ષણિકતાઓ સમજાવો.", 4),
    X("Explain IPv6 address notation and abbreviation rules with an example.", "ઉદાહરણ સાથે IPv6 address notation અને abbreviation ના નિયમો સમજાવો.", 3),
    X("Explain IPv6 addressing modes.", "IPv6 addressing modes સમજાવો.", 3),
    X("Explain IPv6 address types and special addresses.", "IPv6 address types અને special addresses સમજાવો.", 4),
    X("Identify valid IPv6 addresses and give reasons for invalid ones.", "Valid IPv6 addresses ઓળખો અને invalid માટે કારણો આપો.", 3),
    X("Differentiate IPv4 and IPv6.", "IPv4 અને IPv6 નો તફાવત આપો.", 7),
]
