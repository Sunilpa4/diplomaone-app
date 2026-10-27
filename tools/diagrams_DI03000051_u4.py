"""SVG diagrams for DI03000051 Computer Networks Unit 4: IP Protocol (IPv4, IPv6)."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000051_u1 import pc, dev
from diagrams_DI03000051_u2 import harr, varr
import cn_ip

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000051", "diagrams")
PF = "#F1E8FC"
GREY = "#666"
NB = "\u00a0"


def cell(x, y, w, h, s, fill, stroke, size=9, color=INK, weight="normal", mono=False):
    return box(x, y, w, h, fill, stroke, 3, 1.2) + text(x + w / 2, y + h / 2 + size * 0.36, s, size, color=color, weight=weight, mono=mono)


def brace(x1, x2, y, label, color=GREY, size=8.4, up=False):
    d = -5 if up else 5
    b = line(f"M{x1},{y} L{x1},{y + d} L{x2},{y + d} L{x2},{y}", color, 1)
    b += text((x1 + x2) / 2, y + d + (-4 if up else 12), label, size, color=color, weight="bold")
    return b


# ------------------------------------------------------------------ 4.1 IPv4
def v4fmt():
    b = title("IPv4 Address: 32 Bits, 4 Octets")
    ip = "192.168.10.5"
    o = cn_ip.octets(ip)
    b += text(180, 50, ip, 15, weight="bold", color=P, mono=True)
    for i, v in enumerate(o):
        x = 20 + i * 82
        b += text(x + 37, 70, f"octet {i + 1}", 8.2, color=GREY)
        b += cell(x, 76, 74, 24, str(v), BLUEF, BLUE, 11, BLUE, "bold")
        b += cell(x, 104, 74, 22, f"{v:08b}", GREENF, GREEN, 9.4, GREEN, mono=True)
        if i < 3:
            b += text(x + 78, 96, ".", 14, weight="bold")
    b += brace(20, 340, 132, "32 bits = 4 bytes;  each octet 8 bits (0-255)")
    # place values for 192
    b += text(180, 172, "Converting octet 1:  192 = 128 + 64", 9.6, weight="bold", color=ORANGE)
    pv = [128, 64, 32, 16, 8, 4, 2, 1]
    bits = f"{o[0]:08b}"
    for i, (p, bt) in enumerate(zip(pv, bits)):
        x = 40 + i * 36
        b += cell(x, 180, 32, 20, str(p), "#fff", GREY, 8.6, GREY)
        on = bt == "1"
        b += cell(x, 202, 32, 22, bt, ORANGEF if on else "#fff", ORANGE if on else GREY, 10, ORANGE if on else GREY, "bold", True)
    b += text(26, 194, "value", 7.8, anchor="end", color=GREY)
    b += text(26, 217, "bit", 7.8, anchor="end", color=GREY)
    b += note(12, 236, 336, ["Dotted-decimal notation: 4 decimal numbers separated by dots.",
                             "Binary notation: 32 bits, a space between octets.",
                             "Total addresses = 2^32 = 4,294,967,296 (about 4.3 billion)."])
    return svg(360, 296, b)


def header(rows, ttl, total_note, h_svg, x0=20, bw=10, rh=26, y0=58):
    b = title(ttl)
    for k in (0, 8, 16, 24, 32):
        b += text(x0 + k * bw, y0 - 6, str(k if k < 32 else 31), 7.4, color=GREY)
    y = y0
    for row in rows:
        x = x0
        hh = rh * row[0]
        for name, bits, fill, stroke in row[1]:
            w = bits * bw
            b += box(x, y, w, hh, fill, stroke, 2, 1.1)
            b += text(x + w / 2, y + hh / 2 + 3.2, name, 8.6 if w > 50 else 7.6, color=stroke, weight="bold")
            x += w
        y += hh
    b += note(12, y + 10, 336, total_note)
    return svg(360, y + 10 + 10 + 15 * len(total_note) + 10, b)


def v4hdr():
    B, T, G, O, R = (BLUEF, BLUE), (TEALF, TEAL), (GREENF, GREEN), (ORANGEF, ORANGE), (REDF, RED)
    rows = [(1, [("Ver", 4, *B), ("IHL", 4, *B), ("Service type", 8, *T), ("Total length", 16, *T)]),
            (1, [("Identification", 16, *O), ("Flags", 3, *O), ("Fragment offset", 13, *O)]),
            (1, [("TTL", 8, *R), ("Protocol", 8, *R), ("Header checksum", 16, *R)]),
            (1, [("Source IP address (32 bits)", 32, *G)]),
            (1, [("Destination IP address (32 bits)", 32, *G)]),
            (1, [("Options + padding (0-40 bytes)", 32, "#F5F5F5", GREY)])]
    return header(rows, "IPv4 Datagram Header", ["Header: 20 bytes (no options) to 60 bytes.",
                                                 "Ver = 4, TTL = hop limit, Protocol: 6 = TCP, 17 = UDP.",
                                                 "Identification, flags, offset: used for fragmentation."], 274)


def classes():
    b = title("Classful Addressing: Classes A to E")
    x0, ow = 36, 50
    for k in range(4):
        b += text(x0 + k * ow + ow / 2, 50, f"octet {k + 1}", 8, color=GREY)
    b += text(298, 50, "1st octet", 8, color=GREY, weight="bold")
    rows = [("A", "0xxxxxxx", 1), ("B", "10xxxxxx", 2), ("C", "110xxxxx", 3), ("D", "1110xxxx", 0), ("E", "1111xxxx", -1)]
    for i, (c, lead, k) in enumerate(rows):
        y = 58 + i * 32
        (lo, hi), _, _ = cn_ip.CLASS_INFO[c]
        b += text(20, y + 17, c, 13, weight="bold", color=P)
        b += cell(x0, y, ow, 24, lead, BLUEF if k > 0 else (ORANGEF if k == 0 else "#EEEEEE"), BLUE if k > 0 else (ORANGE if k == 0 else GREY), 8.4, INK, mono=True)
        if k > 0:
            for j in range(1, 4):
                net = j < k
                b += cell(x0 + j * ow, y, ow, 24, "Net" if net else "Host", BLUEF if net else GREENF, BLUE if net else GREEN, 9,
                          BLUE if net else GREEN, "bold")
        else:
            b += cell(x0 + ow, y, 3 * ow, 24, "Multicast group address" if k == 0 else "Reserved (future use)",
                      ORANGEF if k == 0 else "#EEEEEE", ORANGE if k == 0 else GREY, 9, ORANGE if k == 0 else GREY, "bold")
        b += text(298, y + 16, f"{lo} - {hi}", 10, weight="bold", color=INK)
    b += note(12, 222, 336, ["Find the class from the first octet (or leading bits).",
                             "Default masks: A = 255.0.0.0 (/8), B = 255.255.0.0 (/16),",
                             "C = 255.255.255.0 (/24). D and E have no net/host split.",
                             "127.x.x.x (in class A range) is reserved for loopback."])
    return svg(360, 296, b)


def space():
    b = title("Address Space of Each Class")
    segs = [("A", 0, 128, BLUEF, BLUE), ("B", 128, 192, TEALF, TEAL), ("C", 192, 224, GREENF, GREEN),
            ("D", 224, 240, ORANGEF, ORANGE), ("E", 240, 256, "#EEEEEE", GREY)]
    sc = 336 / 256
    for c, lo, hi, f, s in segs:
        x, w = 12 + lo * sc, (hi - lo) * sc
        b += box(x, 50, w, 30, f, s, 0, 1.2)
        pct = 100 * (hi - lo) / 256
        b += text(x + w / 2, 64, c, 11, weight="bold", color=s)
        b += text(x + w / 2, 76, f"{pct:g}%" if w > 30 else "", 7.6, color=s)
        b += text(x, 92, str(lo), 7.6, color=GREY, anchor="start" if lo == 0 else "middle")
    b += text(180, 108, "first-octet value", 8, color=GREY)
    cols = [20, 58, 158, 300]
    heads = ["Class", "Networks", "Hosts / network", "Mask"]
    data = [("A", "2^7 = 128 *", "2^24 - 2 = 16,777,214", "/8"),
            ("B", "2^14 = 16,384", "2^16 - 2 = 65,534", "/16"),
            ("C", "2^21 = 2,097,152", "2^8 - 2 = 254", "/24")]
    b += box(12, 118, 336, 22, PF, P, 3, 1.1)
    for x, h in zip(cols, heads):
        b += text(x, 133, h, 8.6, anchor="start", weight="bold", color=P)
    for i, row in enumerate(data):
        y = 140 + i * 24
        b += box(12, y, 336, 24, "#fff", P, 0, 0.8)
        for j, (x, v) in enumerate(zip(cols, row)):
            b += text(x, y + 16, v, 8.4 if j else 10, anchor="start", weight="bold" if j == 0 else "normal", color=P if j == 0 else INK)
    b += note(12, 222, 336, ["Hosts = 2^(host bits) - 2: the all-0s host (network",
                             "address) and all-1s host (broadcast) cannot be given",
                             "to a device. Classful addressing wastes many addresses.",
                             "* class A: 0 and 127 are reserved, so 126 usable."])
    return svg(360, 296, b)


def netid():
    b = title("Network ID and Host ID (Class B)")
    ip = "172.16.2.10"
    c = cn_ip.classful(ip)
    b += text(180, 48, f"{ip}  :  class {c['class']} (first octet 172 is 128-191)", 9.6, weight="bold", color=P)
    rows = [("Address", ["172", "16", "2", "10"], INK), ("Network address", ["172", "16", "0", "0"], BLUE),
            ("Broadcast", ["172", "16", "255", "255"], RED)]
    for i, (lab, vals, col) in enumerate(rows):
        y = 90 + i * 56
        b += text(12, y - 4, lab, 8.8, anchor="start", weight="bold", color=col)
        for j, v in enumerate(vals):
            net = j < 2
            b += cell(110 + j * 58, y - 18, 54, 26, v, BLUEF if net else GREENF, BLUE if net else GREEN, 11, BLUE if net else GREEN, "bold")
        if i == 0:
            b += brace(110, 222, y + 12, "Network ID (16 bits)", BLUE)
            b += brace(226, 338, y + 12, "Host ID (16 bits)", GREEN)
    b += text(12, 158, "host bits all 0", 7.8, anchor="start", color=GREY)
    b += text(12, 214, "host bits all 1", 7.8, anchor="start", color=GREY)
    b += note(12, 226, 336, [f"Network address {c['network']} identifies the network.",
                             f"Broadcast {c['broadcast']} reaches every host on it.",
                             f"Usable hosts: {c['network'][:-1]}1 to 172.16.255.254 = 2^16 - 2 = {c['hosts']:,}."])
    return svg(360, 286, b)


def mask():
    b = title("Subnet Mask: Network Address (AND)")
    ip, m = "10.6.24.20", "255.255.240.0"
    rows = cn_ip.and_rows(ip, m)
    cols = [(BLUE, BLUEF), (ORANGE, ORANGEF), (GREEN, GREENF)]
    for i, ((lab, dot, bn), (s, f)) in enumerate(zip(rows, cols)):
        y = 50 + i * 46
        if i == 2:
            b += line(f"M12,{y - 6} L348,{y - 6}", INK, 1.4)
        b += box(12, y, 336, 38, f, s, 5, 1.1)
        b += text(20, y + 15, lab, 9, anchor="start", weight="bold", color=s)
        b += text(20, y + 30, dot, 9.6, anchor="start", weight="bold", mono=True)
        octs = bn.split()
        for k, o in enumerate(octs):
            x = 130 + k * 55
            hl = k == 2
            b += text(x + 25, y + 24, o, 8.6, mono=True, weight="bold" if hl else "normal", color=RED if hl else INK)
    b += text(180, 196, "IP AND mask, bit by bit (1 AND 1 = 1, else 0)", 8.4, color=GREY)
    b += text(180, 210, "octet 3: 24 AND 240 = 16 (00010000)", 8.6, color=RED, weight="bold")
    b += note(12, 222, 336, ["Mask 1-bits mark the network part, 0-bits the host part.",
                             f"255.255.240.0 has 20 ones, so it is written /20.",
                             f"Network address = 10.6.16.0 (class A, but subnetted)."])
    return svg(360, 282, b)


def subnet():
    b = title("Subnetting 216.21.5.0/24 (30 Hosts Each)")
    r = cn_ip.subnet_for_hosts("216.21.5.0", 24, 30)
    x0, bw = 20, 10
    for name, bits, f, s in [("Network 24 bits", 24, BLUEF, BLUE), ("Subnet 3", 3, ORANGEF, ORANGE), ("Host 5", 5, GREENF, GREEN)]:
        w = bits * bw
        b += box(x0, 42, w, 24, f, s, 2, 1.2)
        b += text(x0 + w / 2, 58, name, 8.6 if bits > 3 else 7.4, weight="bold", color=s)
        x0 += w
    b += text(180, 82, f"2^5 - 2 = 30 hosts, 2^3 = {r['count']} subnets, mask {r['mask']} (/{r['prefix']})", 8.6, weight="bold", color=P)
    cols = [40, 116, 212, 300]
    b += box(12, 90, 336, 20, PF, P, 3, 1.1)
    for x, h in zip(cols, ["Subnet", "Network", "Usable hosts", "Broadcast"]):
        b += text(x, 104, h, 8.6, weight="bold", color=P)
    for i, (net, fh, lh, bc) in enumerate(r["subnets"]):
        y = 110 + i * 18
        b += box(12, y, 336, 18, "#fff" if i % 2 else "#FAFAFA", "#DDD", 0, 0.6)
        last = lambda a: "." + a.split(".")[-1]
        vals = [str(i + 1), last(net), f"{last(fh)} - {last(lh)}", last(bc)]
        for j, (x, v) in enumerate(zip(cols, vals)):
            b += text(x, y + 13, v, 8.6, mono=j > 0, color=[INK, BLUE, GREEN, RED][j], weight="bold" if j == 0 else "normal")
    b += note(12, 260, 336, ["Values show the last octet of 216.21.5.x.",
                             "Block size = 256 - 224 = 32 addresses per subnet."])
    return svg(360, 304, b)


def cidr():
    b = title("Classless Block: 205.16.37.39/28")
    blk = cn_ip.block("205.16.37.39", 28)
    x0, bw = 20, 10
    for name, bits, f, s in [("Prefix (network) 28 bits", 28, BLUEF, BLUE), ("Host 4", 4, GREENF, GREEN)]:
        w = bits * bw
        b += box(x0, 42, w, 24, f, s, 2, 1.2)
        b += text(x0 + w / 2, 58, name, 8.6, weight="bold", color=s)
        x0 += w
    b += text(180, 84, "last octet 39 = 0010 0111;  keep 28 bits, host bits to 0 / 1", 8.6, color=GREY)
    # block of 16 addresses 32..47
    for i in range(16):
        x = 20 + i * 20
        v = 32 + i
        f, s = (BLUEF, BLUE) if i == 0 else (REDF, RED) if i == 15 else (ORANGEF, ORANGE) if v == 39 else ("#fff", GREY)
        b += cell(x, 100, 20, 24, str(v), f, s, 8.2, s, "bold" if s != GREY else "normal")
    b += text(30, 140, "first", 8, color=BLUE, weight="bold")
    b += text(330, 140, "last", 8, color=RED, weight="bold")
    b += text(170, 140, "given address 39", 8, color=ORANGE, weight="bold")
    b += brace(20, 340, 148, f"block of 2^(32-28) = {blk['count']} addresses")
    b += note(12, 178, 336, [f"First (network) address: {blk['network']}",
                             f"Last (broadcast) address: {blk['broadcast']}",
                             f"Usable hosts: {blk['first_host']} to {blk['last_host']} ({blk['hosts']})",
                             f"Mask /28 = {blk['mask']}"], mono=False)
    return svg(360, 252, b)


def reserved():
    b = title("Reserved and Special IPv4 Addresses")
    rows = [("10.0.0.0/8", "Private (class A)", BLUE, BLUEF), ("172.16.0.0/12", "Private (172.16 - 172.31)", BLUE, BLUEF),
            ("192.168.0.0/16", "Private (class C)", BLUE, BLUEF), ("127.0.0.0/8", "Loopback (127.0.0.1)", GREEN, GREENF),
            ("169.254.0.0/16", "APIPA / link-local", TEAL, TEALF), ("0.0.0.0", "This host / default route", GREY, "#F5F5F5"),
            ("255.255.255.255", "Limited broadcast", RED, REDF), ("224.0.0.0/4", "Multicast (class D)", ORANGE, ORANGEF),
            ("240.0.0.0/4", "Reserved (class E)", GREY, "#F5F5F5")]
    for i, (rng, use, s, f) in enumerate(rows):
        y = 40 + i * 24
        b += box(12, y, 150, 20, f, s, 3, 1.1)
        b += text(87, y + 14, rng, 9, weight="bold", color=s, mono=True)
        b += text(172, y + 14, use, 9, anchor="start", color=INK)
    b += note(12, 262, 336, ["Private addresses are not routed on the Internet;",
                             "NAT in the router translates them to a public IP."])
    return svg(360, 306, b)


# ------------------------------------------------------------------ 4.2 IPv6
def v6fmt():
    b = title("IPv6 Address: 128 Bits, 8 Groups")
    full = "2001:0db8:0000:0000:0000:ff00:0042:8329"
    g = full.split(":")
    for i, v in enumerate(g):
        x = 12 + i * 42
        z = v == "0000"
        b += cell(x, 44, 40, 22, v, "#EEEEEE" if z else BLUEF, GREY if z else BLUE, 8.6, GREY if z else BLUE, "bold", True)
    b += brace(12, 52, 70, "")
    b += text(12, 87, "one group = 16 bits = 4 hex digits", 8.4, anchor="start", color=GREY, weight="bold")
    b += brace(12, 346, 92, "8 groups x 16 bits = 128 bits, separated by colons")
    b += text(180, 132, "Rule 1: drop leading zeros in each group", 9.2, weight="bold", color=ORANGE)
    s1 = ":".join(x.lstrip("0") or "0" for x in g)
    b += text(180, 150, s1, 10, mono=True, weight="bold")
    b += text(180, 178, "Rule 2: replace ONE run of zero groups with ::", 9.2, weight="bold", color=GREEN)
    b += text(180, 196, cn_ip.v6_compress(full), 11, mono=True, weight="bold", color=GREEN)
    b += note(12, 212, 336, ["Hexadecimal digits 0-9, a-f (not case sensitive).",
                             ":: may be used only once in an address.",
                             "Total addresses = 2^128 (about 3.4 x 10^38)."])
    return svg(360, 272, b)


def v6hdr():
    B, T, G, O = (BLUEF, BLUE), (TEALF, TEAL), (GREENF, GREEN), (ORANGEF, ORANGE)
    rows = [(1, [("Ver", 4, *B), ("Traffic class", 8, *T), ("Flow label (20 bits)", 20, *T)]),
            (1, [("Payload length", 16, *O), ("Next header", 8, *O), ("Hop limit", 8, *O)]),
            (2, [("Source address (128 bits)", 32, *G)]),
            (2, [("Destination address (128 bits)", 32, *G)])]
    return header(rows, "IPv6 Base Header (40 Bytes)", ["Fixed 40-byte header; no checksum, no fragmentation",
                                                       "fields; options go in extension headers (Next header).",
                                                       "Hop limit = TTL; flow label for real-time traffic."], 262)


def v6modes():
    b = title("IPv6 Addressing Modes")
    rows = [("Unicast", "one to one", [1, 0, 0], BLUE), ("Multicast", "one to many (group)", [1, 1, 1], ORANGE),
            ("Anycast", "one to nearest of group", [1, 0, 0], GREEN)]
    for i, (name, sub, on, col) in enumerate(rows):
        y = 40 + i * 74
        b += box(12, y, 336, 66, "#fff", col, 6, 1.2)
        b += text(22, y + 16, name, 10, anchor="start", weight="bold", color=col)
        b += text(22, y + 29, sub, 8, anchor="start", color=GREY)
        b += pc(46, y + 46, None, col, "#fff")
        for j in range(3):
            ry = y + 14 + j * 20
            rx = 290
            grp = i > 0
            hit = on[j] == 1
            if hit:
                b += line(f"M64,{y + 44} L{rx - 20},{ry + 2}", col, 1.6)
                b += arrowhead(rx - 20, ry + 2, 0 if j == 0 else (10 if j == 1 else 18), 6, col)
            b += box(rx - 16, ry - 5, 30, 14, (col if hit else "#fff"), col if (grp or hit) else GREY, 3, 1)
            b += text(rx - 1, ry + 5, f"R{j + 1}", 7.6, color="#fff" if hit else GREY, weight="bold")
        if i > 0:
            b += f'<rect x="268" y="{y + 4}" width="44" height="58" rx="5" fill="none" stroke="{col}" stroke-width="1" stroke-dasharray="3,2"/>'
            b += text(330, y + 36, "group", 7.6, color=col, weight="bold")
        if i == 2:
            b += text(200, y + 60, "R1 is the nearest member", 7.6, color=col)
    b += note(12, 266, 336, ["No broadcast in IPv6: multicast ff02::1 (all nodes) is used.",
                             "Anycast: same address on many servers (e.g. DNS)."])
    return svg(360, 310, b)


def v6types():
    b = title("IPv6 Global Unicast and Address Types")
    x0 = 12
    for name, bits, f, s in [("Global routing prefix", 48, BLUEF, BLUE), ("Subnet", 16, ORANGEF, ORANGE),
                             ("Interface ID", 64, GREENF, GREEN)]:
        w = bits * 336 / 128
        b += box(x0, 44, w, 26, f, s, 2, 1.2)
        b += text(x0 + w / 2, 61, name, 8.4 if bits > 16 else 7.8, weight="bold", color=s)
        b += text(x0 + w / 2, 82, f"{bits} bits", 8, color=s, weight="bold")
        x0 += w
    b += text(180, 98, "network part 64 bits (ISP + site)  |  host part 64 bits", 8.2, color=GREY)
    rows = [("2000::/3", "Global unicast (public)", BLUE, BLUEF), ("fe80::/10", "Link-local (auto, one link)", TEAL, TEALF),
            ("fc00::/7", "Unique local (private)", GREEN, GREENF), ("ff00::/8", "Multicast", ORANGE, ORANGEF),
            ("::1/128", "Loopback", RED, REDF), ("::/128", "Unspecified", GREY, "#F5F5F5"),
            ("::ffff:0:0/96", "IPv4-mapped", P, PF)]
    for i, (pre, use, s, f) in enumerate(rows):
        y = 108 + i * 22
        b += box(12, y, 130, 18, f, s, 3, 1.1)
        b += text(77, y + 13, pre, 8.8, weight="bold", color=s, mono=True)
        b += text(152, y + 13, use, 9, anchor="start")
    b += note(12, 268, 336, ["Interface ID can be made from the MAC address (EUI-64)",
                             "or random; documentation prefix is 2001:db8::/32."])
    return svg(360, 312, b)


DIAGRAMS = {"cn4_v4fmt": v4fmt, "cn4_v4hdr": v4hdr, "cn4_classes": classes, "cn4_space": space, "cn4_netid": netid,
            "cn4_mask": mask, "cn4_subnet": subnet, "cn4_cidr": cidr, "cn4_reserved": reserved, "cn4_v6fmt": v6fmt,
            "cn4_v6hdr": v6hdr, "cn4_v6modes": v6modes, "cn4_v6types": v6types}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
