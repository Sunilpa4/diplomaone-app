"""DI03000051 Computer Networks - Unit 2 diagrams: OSI model, peer-to-peer communication, encapsulation, transmission modes,
frame format, hop-to-hop vs end-to-end, port addressing, session checkpoints, presentation functions, TCP/IP suite,
OSI vs TCP/IP mapping, addressing levels."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000051_u1 import pc, dev, cable

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000051", "diagrams")
PF = "#F1E8FC"
GREY = "#666"
LAYERS = ["Application", "Presentation", "Session", "Transport", "Network", "Data Link", "Physical"]
LC = [("#FCE4EC", "#C2185B"), (PF, P), (BLUEF, BLUE), (TEALF, TEAL), (GREENF, GREEN), (ORANGEF, ORANGE), ("#EFEBE9", "#6D4C41")]


def harr(x1, x2, y, color=INK, both=False, dash=None):
    b = line(f"M{x1},{y} L{x2},{y}", color, 1.3, dash)
    b += arrowhead(x2, y, 0 if x2 > x1 else 180, 6, color)
    if both:
        b += arrowhead(x1, y, 180 if x2 > x1 else 0, 6, color)
    return b


def varr(x, y1, y2, color=INK):
    return line(f"M{x},{y1} L{x},{y2}", color, 1.4) + arrowhead(x, y2, 90 if y2 > y1 else -90, 6, color)


# ------------------------------------------------------------------ 2.1 OSI
def osi():
    b = title("OSI Reference Model: 7 Layers")
    pdu = ["Data (message)", "Data", "Data", "Segment", "Packet", "Frame", "Bits"]
    job = ["services: HTTP, FTP, mail", "translate, encrypt, compress", "dialog control, sync points",
           "process to process, ports", "logical address (IP), routing", "frames, MAC address, errors", "bits on the medium"]
    y0, h = 44, 33
    b += text(70, y0 - 4, "Layer", 9, weight="bold", color=GREY)
    b += text(180, y0 - 4, "PDU", 9, weight="bold", color=GREY)
    b += text(286, y0 - 4, "Main job", 9, weight="bold", color=GREY)
    for i, n in enumerate(LAYERS):
        y = y0 + i * h
        f, s = LC[i]
        b += box(12, y + 2, 116, h - 4, f, s, 5, 1.4)
        b += text(22, y + h / 2 + 4, str(7 - i), 11, anchor="start", weight="bold", color=s)
        b += text(76, y + h / 2 + 4, n, 10.2, weight="bold", color=s)
        b += text(180, y + h / 2 + 4, pdu[i], 8.8, color=INK)
        b += text(234, y + h / 2 + 4, job[i], 8, anchor="start", color=GREY)
    y = y0 + 7 * h + 6
    b += note(12, y, 336, ["Mnemonic (top to bottom): All People Seem To Need",
                           "Data Processing. Layers 7-5: user support; layer 4:",
                           "end to end; layers 3-1: network support."])
    return svg(360, y + 60, b)


def peer():
    b = title("Peer-to-Peer Communication in OSI")
    xa, xr, xb, w, h, y0 = 12, 135, 258, 90, 24, 44
    short = ["7 Application", "6 Presentation", "5 Session", "4 Transport", "3 Network", "2 Data Link", "1 Physical"]
    for i, n in enumerate(short):
        y = y0 + i * (h + 4)
        f, s = LC[i]
        for x in (xa, xb):
            b += box(x, y, w, h, f, s, 4, 1.2)
            b += text(x + w / 2, y + 16, n, 8.8, weight="bold", color=s)
        if i >= 4:
            b += box(xr, y, w, h, f, s, 4, 1.2)
            b += text(xr + w / 2, y + 16, n, 8.8, weight="bold", color=s)
            b += harr(xa + w + 3, xr - 3, y + h / 2, GREY, True, "3,3")
            b += harr(xr + w + 3, xb - 3, y + h / 2, GREY, True, "3,3")
        else:
            b += harr(xa + w + 3, xb - 3, y + h / 2, GREY, True, "3,3")
    b += text(57, y0 - 6, "Host A", 9.6, weight="bold", color=BLUE)
    b += text(303, y0 - 6, "Host B", 9.6, weight="bold", color=BLUE)
    b += text(180, y0 + 4 * (h + 4) - 8, "Router", 9.6, weight="bold", color=ORANGE)
    yb = y0 + 7 * (h + 4) + 6
    b += line(f"M{xa + w / 2},{y0 + 6 * (h + 4) + h} L{xa + w / 2},{yb} L{xb + w / 2},{yb} L{xb + w / 2},{y0 + 6 * (h + 4) + h}", RED, 2)
    b += text(180, yb + 13, "physical communication (medium)", 8.6, color=RED)
    b += note(12, yb + 22, 336, ["Dashed: peer-to-peer (logical) communication between",
                                 "the same layers using protocols. Data actually flows",
                                 "down at A, over the medium, and up at B. A router",
                                 "uses only layers 1-3."])
    return svg(360, yb + 92, b)


def encap():
    b = title("Encapsulation and Decapsulation")
    rows = [("7-5 Upper", "Message", []), ("4 Transport", "Segment", ["H4"]), ("3 Network", "Packet", ["H3", "H4"]),
            ("2 Data Link", "Frame", ["H2", "H3", "H4"])]
    cols = {"H4": TEAL, "H3": GREEN, "H2": ORANGE}
    y0, rh = 50, 40
    for i, (lay, pdu, hs) in enumerate(rows):
        y = y0 + i * rh
        b += text(14, y + 15, lay, 9, anchor="start", weight="bold", color=INK)
        b += text(14, y + 27, pdu, 8.2, anchor="start", color=GREY)
        x = 112 + (3 - len(hs)) * 0
        for hname in hs:
            b += box(x, y + 3, 26, 24, "#fff", cols[hname], 2, 1.4)
            b += text(x + 13, y + 19, hname, 8.6, weight="bold", color=cols[hname])
            x += 26
        b += box(x, y + 3, 70, 24, BLUEF, BLUE, 2, 1.4)
        b += text(x + 35, y + 19, "Data", 9, weight="bold", color=BLUE)
        x += 70
        if lay.startswith("2"):
            b += box(x, y + 3, 26, 24, "#fff", ORANGE, 2, 1.4)
            b += text(x + 13, y + 19, "T2", 8.6, weight="bold", color=ORANGE)
    y = y0 + 4 * rh
    b += text(14, y + 15, "1 Physical", 9, anchor="start", weight="bold", color=INK)
    b += text(14, y + 27, "Bits", 8.2, anchor="start", color=GREY)
    b += text(112, y + 20, "0110101110010101...", 10, anchor="start", mono=True, color="#6D4C41", weight="bold")
    b += varr(326, y0 + 6, y + 22, BLUE)
    b += varr(344, y + 22, y0 + 6, GREEN)
    b += text(320, y0 - 4, "send", 8, color=BLUE)
    b += text(346, y0 - 4, "recv", 8, color=GREEN)
    b += note(12, y + 40, 336, ["Sender: each layer adds its header (H); data link also",
                                "adds a trailer (T2 = error check). Receiver: each layer",
                                "removes its own header and passes data up."])
    return svg(360, y + 100, b)


def modes():
    b = title("Transmission Modes (Physical Layer)")
    rows = [("Simplex", "one direction only", "keyboard, TV, radio", "one"),
            ("Half duplex", "both directions, one at a time", "walkie-talkie", "half"),
            ("Full duplex", "both directions at the same time", "telephone, mobile", "full")]
    for i, (n, d, ex, k) in enumerate(rows):
        y = 64 + i * 72
        b += pc(40, y)
        b += pc(320, y)
        b += text(180, y - 22, n, 10.4, weight="bold", color=P)
        if k == "one":
            b += harr(64, 296, y, BLUE)
        elif k == "half":
            b += harr(64, 296, y - 5, BLUE)
            b += harr(296, 64, y + 5, GREEN, False, "5,4")
        else:
            b += harr(64, 296, y - 5, BLUE)
            b += harr(296, 64, y + 5, GREEN)
        b += text(180, y + 20, d, 8.6, color=INK)
        b += text(180, y + 32, "e.g. " + ex, 8.2, color=GREY)
    b += note(12, 268, 336, ["Physical layer also defines: bit representation and",
                             "data rate, bit synchronisation, line configuration",
                             "(point-to-point / multipoint) and physical topology."])
    return svg(360, 328, b)


def frame():
    b = title("Data Link Layer: Frame Format")
    fields = [("Flag", 30, GREY), ("Dest MAC", 52, ORANGE), ("Src MAC", 50, ORANGE), ("Ctrl", 30, ORANGE),
              ("Data (packet)", 84, BLUE), ("FCS", 34, RED), ("Flag", 30, GREY)]
    x, y = 25, 70
    for n, w, c in fields:
        b += box(x, y, w, 34, "#fff", c, 2, 1.5)
        b += text(x + w / 2, y + 21, n, 8.6, weight="bold", color=c)
        x += w
    b += line(f"M55,{y - 8} L187,{y - 8}", ORANGE, 1.2)
    b += text(121, y - 13, "Header (added by DLL)", 8.6, color=ORANGE)
    b += line(f"M271,{y - 8} L305,{y - 8}", RED, 1.2)
    b += text(288, y - 13, "Trailer", 8.6, color=RED)
    b += text(180, y + 52, "FCS = Frame Check Sequence (CRC) for error detection", 8.4, color=RED)
    b += text(180, y + 66, "MAC example: 3C:52:82:1A:9F:04 (48 bits)", 8.4, color=GREY)
    b += note(12, 158, 336, ["Functions: framing, physical (MAC) addressing,",
                             "flow control, error control, access control.",
                             "Sublayers: LLC (logical link) and MAC (media access).",
                             "Devices: switch, bridge, NIC."])
    return svg(360, 234, b)


def hop():
    b = title("Network Layer vs Data Link Layer")
    nodes = [(36, "A", "host"), (136, "R1", "router"), (226, "R2", "router"), (324, "B", "host")]
    y = 128
    for i in range(3):
        b += cable(nodes[i][0] + 18, y, nodes[i + 1][0] - 18, y, GREY, 2)
    for x, n, k in nodes:
        if k == "host":
            b += pc(x, y)
            b += text(x, y + 26, "Host " + n, 8.8, weight="bold", color=BLUE)
        else:
            b += f'<circle cx="{x}" cy="{y}" r="15" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.5"/>'
            b += text(x, y + 4, n, 9.4, weight="bold", color=ORANGE)
    b += harr(36, 324, 72, GREEN)
    b += text(180, 64, "Network layer: source to destination (IP A to IP B)", 8.8, weight="bold", color=GREEN)
    for i in range(3):
        x1, x2 = nodes[i][0] + 4, nodes[i + 1][0] - 4
        b += harr(x1, x2, 96, ORANGE)
    b += text(180, 182, "Data link layer: hop to hop (node to node), MAC", 8.8, weight="bold", color=ORANGE)
    b += text(86, 90, "hop 1", 8, color=ORANGE)
    b += text(181, 90, "hop 2", 8, color=ORANGE)
    b += text(275, 90, "hop 3", 8, color=ORANGE)
    b += note(12, 196, 336, ["Network layer: logical (IP) addressing, routing (best",
                             "path), packet forwarding, fragmentation. Device: router."])
    return svg(360, 238, b)


def ports():
    b = title("Transport Layer: Process to Process")
    for x, name, ip, procs in ((70, "Client", "IP 192.168.1.5", [("Browser", "52000"), ("Mail app", "52100")]),
                               (290, "Server", "IP 142.250.1.10", [("Web server", "80 / 443"), ("Mail server", "25")])):
        b += box(x - 62, 50, 124, 132, "#FAFAFA", GREY, 8, 1.2)
        b += text(x, 66, name, 10, weight="bold", color=BLUE)
        b += text(x, 80, ip, 8.4, color=GREEN)
        for i, (p, port) in enumerate(procs):
            yy = 96 + i * 40
            b += box(x - 52, yy, 104, 32, PF, P, 5, 1.2)
            b += text(x, yy + 13, p, 8.8, weight="bold", color=P)
            b += text(x, yy + 26, "port " + port, 8.2, color=TEAL)
    b += harr(124, 236, 112, TEAL)
    b += harr(124, 236, 152, TEAL)
    b += text(180, 106, "TCP / UDP", 8.4, color=TEAL)
    b += note(12, 194, 336, ["IP address delivers to the right host; port number",
                             "delivers to the right process. Functions: segmentation",
                             "and reassembly, connection control, flow and error",
                             "control end to end (TCP reliable, UDP fast)."])
    return svg(360, 266, b)


def session():
    b = title("Session Layer: Synchronisation Points")
    x0, x1, y = 22, 338, 66
    W = x1 - x0
    b += text(180, 52, "Sending a 2000-page file (checkpoint every 100 pages)", 8.8, weight="bold", color=BLUE)
    b += box(x0, y, W, 20, BLUEF, BLUE, 3, 1.3)
    for i in range(1, 20):
        xx = x0 + W * i / 20
        b += line(f"M{xx:.1f},{y} L{xx:.1f},{y + 20}", BLUE, 0.8 if i % 5 else 1.6)
    for pg in (0, 500, 1500, 2000):
        b += text(x0 + W * pg / 2000, y + 32, str(pg), 8, color=BLUE)
    za, zb = x0 + W * 400 / 2000, x0 + W * 600 / 2000
    b += box(za, y - 2, zb - za, 24, "none", ORANGE, 2, 1.6)
    zy = y + 66
    b += line(f"M{za:.1f},{y + 22} L{x0},{zy}", ORANGE, 0.9, "3,3")
    b += line(f"M{zb:.1f},{y + 22} L{x1},{zy}", ORANGE, 0.9, "3,3")
    b += box(x0, zy, W, 22, "#fff", ORANGE, 3, 1.3)
    X = lambda pg: x0 + W * (pg - 400) / 200
    for pg in range(410, 600, 10):
        b += line(f"M{X(pg):.1f},{zy} L{X(pg):.1f},{zy + 6}", GREY, 0.7)
    for pg in (400, 500, 600):
        b += line(f"M{X(pg):.1f},{zy} L{X(pg):.1f},{zy + 22}", GREEN, 2)
        b += text(X(pg), zy + 34, f"checkpoint {pg}", 8, color=GREEN, anchor="start" if pg == 400 else "end" if pg == 600 else "middle")
    xc = X(523)
    b += line(f"M{xc:.1f},{zy - 6} L{xc:.1f},{zy + 26}", RED, 2)
    b += text(xc + 4, zy - 8, "crash at page 523", 8.4, color=RED, anchor="start")
    b += line(f"M{xc:.1f},{zy + 48} L{X(500) + 2:.1f},{zy + 48}", GREEN, 1.6) + arrowhead(X(500), zy + 48, 180, 6, GREEN)
    b += text(xc + 6, zy + 52, "resume from 500, not page 1", 8.4, color=GREEN, anchor="start")
    b += note(12, zy + 64, 336, ["Only pages 501-523 are re-sent after the crash.",
                                 "Other jobs: dialog control (simplex / half / full",
                                 "duplex), session setup, maintenance and release."])
    return svg(360, zy + 124, b)


def present():
    b = title("Presentation Layer Functions")
    rows = [("Translation", "ASCII / EBCDIC", "common format", BLUE, BLUEF),
            ("Encryption", "plain text: HELLO", "cipher text: KHOOR", RED, REDF),
            ("Compression", "photo 4 MB", "JPEG 400 KB", GREEN, GREENF)]
    for i, (n, a, c, s, f) in enumerate(rows):
        y = 50 + i * 58
        b += rbox(56, y + 20, 92, 34, n, fill=f, stroke=s, size=9.6, weight="bold")
        b += box(118, y + 6, 92, 28, "#fff", GREY, 4, 1)
        b += text(164, y + 24, a, 8.4)
        b += harr(212, 244, y + 20, s)
        b += box(246, y + 6, 100, 28, "#fff", GREY, 4, 1)
        b += text(296, y + 24, c, 8.4)
    b += note(12, 226, 336, ["Concerned with syntax and semantics of information.",
                             "Reverse at receiver: decrypt, decompress, translate.",
                             "Examples: JPEG, MPEG, MP3, SSL/TLS, ASCII, Unicode."])
    return svg(360, 286, b)


# ------------------------------------------------------------------ 2.2 TCP/IP
def tcpip():
    b = title("TCP/IP Model and Protocol Suite")
    rows = [("Application", ["HTTP", "FTP", "SMTP", "DNS", "Telnet", "SNMP", "DHCP"], LC[0]),
            ("Transport", ["TCP", "UDP", "SCTP"], LC[3]),
            ("Internet", ["IP", "ICMP", "ARP", "RARP", "IGMP"], LC[4]),
            ("Network Access", ["Ethernet", "Wi-Fi", "PPP", "drivers"], LC[5])]
    y0, h = 46, 52
    for i, (n, ps, (f, s)) in enumerate(rows):
        y = y0 + i * h
        b += box(12, y, 96, h - 6, f, s, 5, 1.5)
        b += text(60, y + h / 2, n, 9.6, weight="bold", color=s)
        b += text(22, y + 12, str(4 - i), 8.4, color=s, weight="bold")
        b += box(114, y, 234, h - 6, "#fff", s, 5, 1.1)
        x = 122
        for p in ps:
            w = 7 + len(p) * 5.8
            if x + w > 344:
                break
            b += box(x, y + 12, w, 20, f, s, 3, 0.9)
            b += text(x + w / 2, y + 26, p, 8.4, weight="bold", color=s)
            x += w + 4
    y = y0 + 4 * h + 4
    b += note(12, y, 336, ["Developed by US DoD (ARPANET) before OSI; the",
                           "Internet runs on it. Some books show 5 layers by",
                           "splitting network access into data link + physical."])
    return svg(360, y + 60, b)


def mapping():
    b = title("OSI vs TCP/IP: Layer Mapping")
    y0, h = 46, 30
    for i, n in enumerate(LAYERS):
        f, s = LC[i]
        y = y0 + i * h
        b += box(20, y + 2, 120, h - 4, f, s, 4, 1.3)
        b += text(80, y + h / 2 + 4, f"{7 - i}  {n}", 9.4, weight="bold", color=s)
    groups = [(0, 3, "Application", LC[0]), (3, 4, "Transport", LC[3]), (4, 5, "Internet", LC[4]), (5, 7, "Network Access", LC[5])]
    for a, c, n, (f, s) in groups:
        ya, yc = y0 + a * h + 2, y0 + c * h - 2
        b += box(220, ya, 120, yc - ya, f, s, 4, 1.5)
        b += text(280, (ya + yc) / 2 + 4, n, 9.8, weight="bold", color=s)
        b += line(f"M144,{ya} L216,{ya}", GREY, 0.8, "3,3")
        b += line(f"M144,{yc} L216,{yc}", GREY, 0.8, "3,3")
    b += text(80, y0 - 6, "OSI (7)", 10, weight="bold", color=P)
    b += text(280, y0 - 6, "TCP/IP (4)", 10, weight="bold", color=P)
    y = y0 + 7 * h + 8
    b += note(12, y, 336, ["Application layer of TCP/IP = OSI session +",
                           "presentation + application. Network access =",
                           "OSI data link + physical."])
    return svg(360, y + 60, b)


def addr():
    b = title("Addresses Used in TCP/IP")
    rows = [("Specific address", "URL, e-mail: www.gtu.ac.in", "Application", LC[0]),
            ("Port address", "16-bit: 80 (HTTP), 25 (SMTP)", "Transport", LC[3]),
            ("Logical address", "IPv4 32-bit: 192.168.1.5", "Internet / Network", LC[4]),
            ("Physical address", "MAC 48-bit: 3C:52:82:1A:9F:04", "Data link", LC[5])]
    for i, (n, ex, lay, (f, s)) in enumerate(rows):
        y = 46 + i * 50
        b += box(12, y, 336, 42, f, s, 6, 1.4)
        b += text(22, y + 17, n, 10, anchor="start", weight="bold", color=s)
        b += text(338, y + 17, lay + " layer", 8.4, anchor="end", color=s)
        b += text(22, y + 33, ex, 8.8, anchor="start", mono=True)
    b += note(12, 252, 336, ["MAC: changes at every hop. IP: same from source to",
                             "destination. Port: identifies the process."])
    return svg(360, 296, b)


DIAGRAMS = {"cn2_osi": osi, "cn2_peer": peer, "cn2_encap": encap, "cn2_modes": modes, "cn2_frame": frame, "cn2_hop": hop,
            "cn2_ports": ports, "cn2_session": session, "cn2_present": present, "cn2_tcpip": tcpip, "cn2_map": mapping,
            "cn2_addr": addr}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
