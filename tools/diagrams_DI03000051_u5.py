"""SVG diagrams for DI03000051 Computer Networks Unit 5: Network Security Aspects."""
import os
import hashlib
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000051_u1 import pc, dev
from diagrams_DI03000051_u2 import harr, varr, LC
from diagrams_DI03000051_u3 import poly
from diagrams_DI03000051_u4 import cell

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000051", "diagrams")
PF = "#F1E8FC"
GREY = "#666"


def server(cx, cy, label=None, color=TEAL, fill=TEALF, size=8.4):
    b = box(cx - 13, cy - 16, 26, 30, fill, color, 2.5, 1.4)
    for k in range(3):
        y = cy - 11 + k * 8
        b += line(f"M{cx - 9},{y + 3} L{cx + 4},{y + 3}", color, 1.2)
        b += f'<circle cx="{cx + 8}" cy="{y + 3}" r="1.5" fill="{color}"/>'
    if label:
        b += text(cx, cy + 26, label, size, color=color, weight="bold")
    return b


def wall(x, y, w, h, label="Firewall"):
    b = box(x, y, w, h, "#FFCCBC", "#BF360C", 2, 1.4)
    rows = int(h // 10)
    for r in range(1, rows):
        b += line(f"M{x},{y + r * 10} L{x + w},{y + r * 10}", "#BF360C", 0.7)
    for r in range(rows):
        off = 0 if r % 2 else w / 2
        xx = x + off if off else x + w / 2
        b += line(f"M{xx},{y + r * 10} L{xx},{y + min((r + 1) * 10, h)}", "#BF360C", 0.7)
    if label:
        b += text(x + w / 2, y - 6, label, 8.6, weight="bold", color="#BF360C")
    return b


def cross(x, y, color=RED, s=6):
    return line(f"M{x - s},{y - s} L{x + s},{y + s} M{x - s},{y + s} L{x + s},{y - s}", color, 2.4)


def tick(x, y, color=GREEN):
    return line(f"M{x - 6},{y} L{x - 2},{y + 5} L{x + 7},{y - 6}", color, 2.4)


# ------------------------------------------------------------------ 5.1 basics
def cia():
    b = title("CIA Triad of Security")
    A, B_, C_ = (180, 56), (60, 236), (300, 236)
    b += f'<polygon points="{A[0]},{A[1]} {B_[0]},{B_[1]} {C_[0]},{C_[1]}" fill="{PF}" stroke="{P}" stroke-width="2"/>'
    b += text(180, 182, "Information", 11, weight="bold", color=P)
    b += text(180, 197, "security", 11, weight="bold", color=P)
    for (x, y), name, sub, (f, s) in [((180, 56), "Confidentiality", "only authorised can read", (BLUEF, BLUE)),
                                      ((60, 236), "Integrity", "data not altered", (GREENF, GREEN)),
                                      ((300, 236), "Availability", "accessible when needed", (ORANGEF, ORANGE))]:
        b += box(x - 54, y - 16, 108, 32, f, s, 6, 1.6)
        b += text(x, y - 1, name, 10, weight="bold", color=s)
        b += text(x, y + 11, sub, 7.4, color=GREY)
    b += text(110, 140, "encryption,", 8, color=BLUE, anchor="end")
    b += text(110, 152, "access control", 8, color=BLUE, anchor="end")
    b += text(250, 140, "hashing,", 8, color=GREEN, anchor="start")
    b += text(250, 152, "digital signature", 8, color=GREEN, anchor="start")
    b += text(300, 266, "backup, redundancy, anti-DoS", 7.6, color=ORANGE)
    b += note(12, 284, 336, ["Attacks: disclosure (C), alteration (I), denial (A).",
                             "A secure system must protect all three."])
    return svg(360, 328, b)


def attacks():
    b = title("Security Attacks on a Message")
    panels = [("Interruption", "availability", "cut"), ("Interception", "confidentiality", "tap"),
              ("Modification", "integrity", "mod"), ("Fabrication", "authenticity", "fab")]
    for i, (name, goal, kind) in enumerate(panels):
        x0 = 12 + (i % 2) * 172
        y0 = 40 + (i // 2) * 116
        b += box(x0, y0, 164, 108, "#fff", P, 6, 1.1)
        b += text(x0 + 82, y0 + 15, name, 10, weight="bold", color=P)
        b += text(x0 + 82, y0 + 27, f"attack on {goal}", 7.6, color=GREY)
        sx, dx, yy = x0 + 26, x0 + 138, y0 + 56
        b += pc(sx, yy, "A", BLUE, BLUEF, 7.6)
        b += pc(dx, yy, "B", BLUE, BLUEF, 7.6)
        ax, ay = x0 + 82, y0 + 92
        b += pc(ax, ay - 4, None, RED, REDF)
        b += text(ax + 18, ay + 2, "attacker", 7.4, color=RED, anchor="start")
        if kind == "cut":
            b += line(f"M{sx + 16},{yy} L{ax - 8},{yy}", BLUE, 1.6)
            b += cross(ax, yy)
        elif kind == "tap":
            b += line(f"M{sx + 16},{yy} L{dx - 22},{yy}", BLUE, 1.6) + arrowhead(dx - 16, yy, 0, 6, BLUE)
            b += line(f"M{ax},{yy} L{ax},{ay - 20}", RED, 1.4, "3,2") + arrowhead(ax, ay - 16, 90, 6, RED)
        elif kind == "mod":
            b += line(f"M{sx + 16},{yy} L{ax - 4},{ay - 18}", BLUE, 1.6) + arrowhead(ax - 2, ay - 16, 50, 6, BLUE)
            b += line(f"M{ax + 4},{ay - 18} L{dx - 18},{yy + 2}", RED, 1.6) + arrowhead(dx - 16, yy, -45, 6, RED)
        else:
            b += line(f"M{ax + 4},{ay - 18} L{dx - 18},{yy + 2}", RED, 1.6) + arrowhead(dx - 16, yy, -45, 6, RED)
            b += text(x0 + 6, yy + 38, "(A sent nothing)", 7, color=GREY, anchor="start")
    b += note(12, 276, 336, ["Passive attack: interception (only reading, hard to detect).",
                             "Active attacks: interruption, modification, fabrication."])
    return svg(360, 320, b)


def encrypt():
    b = title("Confidentiality: Encryption")
    y = 92
    b += cell(12, y - 14, 70, 28, "HELLO", BLUEF, BLUE, 10, BLUE, "bold", True)
    b += text(47, y - 20, "plaintext", 8, color=BLUE)
    b += rbox(127, y, 62, 30, "Encrypt", fill=GREENF, stroke=GREEN, size=9, weight="bold", color=GREEN)
    b += cell(180, y - 14, 70, 28, "KHOOR", REDF, RED, 10, RED, "bold", True)
    b += text(215, y - 20, "ciphertext", 8, color=RED)
    b += rbox(298, y, 62, 30, "Decrypt", fill=GREENF, stroke=GREEN, size=9, weight="bold", color=GREEN)
    b += harr(82, 96, y) + harr(158, 180, y) + harr(250, 267, y)
    b += cell(268, y + 34, 70, 26, "HELLO", BLUEF, BLUE, 10, BLUE, "bold", True)
    b += varr(298, y + 15, y + 33, BLUE)
    for x in (127, 298):
        b += text(x, y - 26, "key", 8, color=ORANGE, weight="bold")
        b += varr(x, y - 22, y - 16, ORANGE)
    b += text(215, y + 48, "sent over the network", 7.6, color=GREY)
    b += pc(215, 186, None, RED, REDF)
    b += line(f"M215,{y + 15} L215,170", RED, 1.3, "3,2")
    b += text(240, 186, "eavesdropper sees only", 8, color=RED, anchor="start")
    b += text(240, 198, "KHOOR (meaningless)", 8, color=RED, anchor="start", weight="bold")
    b += note(12, 214, 336, ["Example: Caesar cipher, key = 3 (each letter shifted by 3).",
                             "Symmetric: same secret key (AES). Asymmetric: public /",
                             "private key pair (RSA). HTTPS, VPN, Wi-Fi WPA3 use it."])
    return svg(360, 274, b)


def hashv():
    HX = hashlib.sha256(b"Pay Rs 100").hexdigest()[:6] + "..."
    b = title("Integrity: Hash Check")
    b += text(75, 50, "Sender", 9.6, weight="bold", color=BLUE)
    b += text(277, 50, "Receiver", 9.6, weight="bold", color=GREEN)
    b += cell(20, 60, 110, 24, "Pay Rs 100", BLUEF, BLUE, 9.4, INK, mono=True)
    b += rbox(75, 112, 84, 24, "Hash (SHA-256)", fill=PF, stroke=P, size=8.2, weight="bold", color=P)
    b += varr(75, 84, 99, P) + varr(75, 124, 135, P)
    b += cell(25, 136, 100, 22, HX, PF, P, 9, P, "bold", True)
    b += line("M125,147 L160,147 L160,76", P, 1.3)
    b += harr(130, 204, 72, BLUE)
    b += text(167, 64, "message + hash", 7.6, color=GREY)
    b += cell(206, 60, 90, 24, "Pay Rs 100", GREENF, GREEN, 9.4, INK, mono=True)
    b += cell(296, 60, 52, 24, HX, PF, P, 8.4, P, "bold", True)
    b += rbox(251, 112, 80, 24, "Hash again", fill=PF, stroke=P, size=8.2, weight="bold", color=P)
    b += varr(251, 84, 99, P) + varr(251, 124, 135, P)
    b += cell(211, 136, 80, 22, "new hash", PF, P, 8.4, P)
    b += varr(251, 158, 183, ORANGE)
    b += varr(322, 84, 183, P)
    b += text(326, 130, "received", 7.4, color=P, anchor="start")
    b += text(326, 140, "hash", 7.4, color=P, anchor="start")
    b += rbox(280, 196, 110, 26, "Compare", fill=ORANGEF, stroke=ORANGE, size=9, weight="bold", color=ORANGE)
    b += text(280, 224, "equal: not changed", 8, color=GREEN, weight="bold")
    b += text(280, 236, "different: tampered", 8, color=RED, weight="bold")
    b += text(20, 190, "Changing even one character", 8, anchor="start", color=GREY)
    b += text(20, 202, "(100 to 900) gives a totally", 8, anchor="start", color=GREY)
    b += text(20, 214, "different hash.", 8, anchor="start", color=GREY)
    b += note(12, 246, 336, ["Hash = fixed-size fingerprint of data (MD5, SHA-256).",
                             "Digital signature = hash encrypted with sender's private key."])
    return svg(360, 290, b)


def dos():
    b = title("Availability Attack: DDoS")
    b += server(296, 120, "Server", RED, REDF)
    for i in range(5):
        y = 52 + i * 34
        b += pc(40, y, None, RED, REDF)
        b += line(f"M56,{y} L272,{116 + (i - 2) * 3}", RED, 1.1)
        b += arrowhead(276, 116 + (i - 2) * 3, 0, 5, RED)
    b += text(12, 230, "botnet (infected PCs)", 8, color=RED, weight="bold", anchor="start")
    b += text(170, 52, "flood of fake requests", 8, color=RED, weight="bold")
    b += pc(160, 214, "Genuine user", BLUE, BLUEF, 8)
    b += line(f"M176,212 L248,180", BLUE, 1.4, "4,3")
    b += cross(256, 176)
    b += text(296, 156, "overloaded,", 8, color=RED)
    b += text(296, 168, "cannot reply", 8, color=RED)
    b += note(12, 246, 336, ["DoS: one attacker; DDoS: thousands of zombie PCs.",
                             "Defence: firewall rules, rate limiting, redundant servers,",
                             "load balancers, CDN, backups and UPS for availability."])
    return svg(360, 306, b)


# ------------------------------------------------------------------ 5.2 threats
def pyramid():
    b = title("Threat Sophistication Levels")
    levels = [("Information warfare (nation states)", "highly structured", RED, REDF),
              ("Terrorists, criminal orgs", "structured", ORANGE, ORANGEF),
              ("Skilled intruders, insiders", "structured / unstructured", TEAL, TEALF),
              ("Script kiddies, viruses, worms", "unstructured", BLUE, BLUEF)]
    top, base, h = 46, 236, 47.5
    for i, (name, sub, s, f) in enumerate(levels):
        y1, y2 = top + i * h, top + (i + 1) * h
        w1 = 30 + i * 74
        w2 = 30 + (i + 1) * 74
        pts = f"{180 - w1 / 2 + 0},{y1} {180 + w1 / 2},{y1} {180 + w2 / 2},{y2} {180 - w2 / 2},{y2}"
        if i == 0:
            pts = f"180,{y1} 180,{y1} {180 + w2 / 2},{y2} {180 - w2 / 2},{y2}"
        b += f'<polygon points="{pts}" fill="{f}" stroke="{s}" stroke-width="1.4"/>'
        if i == 0:
            b += text(12, y1 + 26, "Information warfare", 8.4, weight="bold", color=s, anchor="start")
            b += text(12, y1 + 38, "(nation states)", 7.6, color=s, anchor="start")
            b += text(12, y1 + 49, "highly structured", 7.4, color=GREY, anchor="start")
        else:
            b += text(180, y1 + h / 2 + 2, name, 8.4, weight="bold", color=s)
        if i:
            b += text(180, y1 + h / 2 + 13, sub, 7.4, color=GREY)
    b += line("M350,130 L350,52", GREY, 1.2) + arrowhead(350, 50, -90, 6, GREY)
    b += text(342, 62, "skill, money, time", 7.6, color=GREY, anchor="end")
    b += text(342, 74, "increase upward", 7.6, color=GREY, anchor="end")
    b += note(12, 246, 336, ["Lower levels: many attacks, low skill, known tools.",
                             "Top: few attackers but very well funded and dangerous."])
    return svg(360, 290, b)


def virus_worm():
    b = title("Virus vs Worm")
    b += box(12, 40, 336, 96, BLUEF, BLUE, 6, 1.2)
    b += text(22, 56, "Virus: attaches to a host file", 9.6, anchor="start", weight="bold", color=BLUE)
    b += box(24, 70, 84, 34, "#fff", GREY, 3, 1.2)
    b += text(55, 90, "game.exe", 8.6)
    b += box(90, 72, 16, 30, REDF, RED, 2, 1.2)
    b += text(98, 114, "virus code", 7.4, color=RED)
    b += text(118, 84, "user runs", 8, anchor="start", color=GREY)
    b += text(118, 96, "the file", 8, anchor="start", color=GREY)
    b += harr(162, 190, 87, RED)
    for j in range(3):
        x = 196 + j * 48
        b += box(x, 70, 46, 34, "#fff", GREY, 3, 1.2)
        b += text(x + 19, 90, ["a.doc", "b.exe", "c.exe"][j], 7.6)
        b += box(x + 36, 72, 8, 30, REDF, RED, 1.5, 1)
    b += text(272, 118, "infects other files", 7.8, color=RED)
    b += box(12, 146, 336, 104, GREENF, GREEN, 6, 1.2)
    b += text(22, 162, "Worm: standalone, spreads by itself over network", 9.6, anchor="start", weight="bold", color=GREEN)
    pts = [(46, 206), (130, 186), (130, 230), (220, 196), (306, 186), (306, 230)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5)]
    for a, c in edges:
        (x1, y1), (x2, y2) = pts[a], pts[c]
        b += line(f"M{x1 + 14},{y1} L{x2 - 16},{y2}", RED, 1.3) + arrowhead(x2 - 14, y2, 0 if abs(y2 - y1) < 2 else (15 if y2 > y1 else -15) if x2 > x1 else 180, 5, RED)
    for i, (x, y) in enumerate(pts):
        b += pc(x, y, None, RED if True else BLUE, REDF)
    b += text(46, 230, "first victim", 7.4, color=RED)
    b += note(12, 260, 336, ["Virus needs a host program and user action to spread.",
                             "Worm copies itself through network flaws automatically,",
                             "eating bandwidth (e.g. WannaCry 2017, ILOVEYOU 2000)."])
    return svg(360, 320, b)


# ------------------------------------------------------------------ 5.3 firewalls
def firewall():
    b = title("Firewall: Working")
    b += box(12, 44, 124, 172, BLUEF, BLUE, 8, 1.2)
    b += text(74, 60, "Trusted network", 9, weight="bold", color=BLUE)
    for k, y in enumerate((90, 140, 190)):
        b += pc(46, y, None)
    b += server(100, 140, None)
    b += wall(160, 54, 34, 156)
    b += box(222, 44, 126, 172, "#F5F5F5", GREY, 8, 1.2)
    b += text(285, 60, "Internet (untrusted)", 9, weight="bold", color=GREY)
    b += pc(300, 100, "user", GREY, "#fff", 7.6)
    b += pc(300, 186, "hacker", RED, REDF, 7.6)
    # allowed
    b += line("M284,96 L140,96", GREEN, 1.6) + arrowhead(138, 96, 180, 6, GREEN)
    b += text(250, 88, "HTTPS reply", 7.4, color=GREEN, weight="bold")
    b += tick(250, 110)
    # blocked
    b += line("M282,182 L198,182", RED, 1.6) + arrowhead(196, 182, 180, 6, RED)
    b += cross(178, 182)
    b += text(240, 172, "telnet / scan", 7.4, color=RED, weight="bold")
    b += note(12, 226, 336, ["Every packet in or out passes the firewall; it compares",
                             "the packet with the rule base (policy): allow or deny.",
                             "Placed between the LAN and the Internet (choke point)."])
    return svg(360, 286, b)


def dmz():
    b = title("Firewall Design: DMZ")
    b += box(12, 70, 66, 90, "#F5F5F5", GREY, 6, 1.1)
    b += text(45, 86, "Internet", 9, weight="bold", color=GREY)
    b += pc(45, 120, None, GREY, "#fff")
    b += wall(90, 66, 22, 100, "")
    b += text(101, 182, "outer", 7.6, color="#BF360C", weight="bold")
    b += text(101, 192, "firewall", 7.6, color="#BF360C", weight="bold")
    b += box(124, 56, 108, 120, ORANGEF, ORANGE, 6, 1.2)
    b += text(178, 72, "DMZ", 10, weight="bold", color=ORANGE)
    b += server(150, 112, "Web", ORANGE, "#fff", 7.6)
    b += server(206, 112, "Mail", ORANGE, "#fff", 7.6)
    b += wall(244, 66, 22, 100, "")
    b += text(255, 182, "inner", 7.6, color="#BF360C", weight="bold")
    b += text(255, 192, "firewall", 7.6, color="#BF360C", weight="bold")
    b += box(278, 56, 70, 120, BLUEF, BLUE, 6, 1.2)
    b += text(313, 72, "LAN", 10, weight="bold", color=BLUE)
    b += pc(313, 100, None)
    b += pc(313, 146, None)
    b += line("M60,200 L60,210 L170,210", GREEN, 1.3) + arrowhead(172, 210, 0, 5, GREEN)
    b += text(116, 222, "public may reach DMZ", 7.6, color=GREEN)
    b += line("M300,200 L300,210 L200,210", BLUE, 1.3) + arrowhead(198, 210, 180, 5, BLUE)
    b += text(250, 222, "LAN users go out", 7.6, color=BLUE)
    b += note(12, 234, 336, ["Public servers sit in the DMZ (demilitarised zone).",
                             "Internet cannot reach the LAN directly: two layers of",
                             "defence (defence in depth). Default policy: deny all."])
    return svg(360, 294, b)


def pfilter():
    b = title("Packet Filter Firewall")
    b += text(12, 50, "Checks header fields only:", 9, anchor="start", weight="bold", color=P)
    fields = [("Src IP", BLUEF, BLUE), ("Dst IP", BLUEF, BLUE), ("Protocol", TEALF, TEAL), ("Src port", GREENF, GREEN),
              ("Dst port", GREENF, GREEN), ("Data", "#F5F5F5", GREY)]
    x = 12
    for i, (n, f, s) in enumerate(fields):
        w = 52 if i < 5 else 76
        b += cell(x, 58, w, 22, n, f, s, 8.2, s, "bold")
        x += w + 0
    b += text(320, 92, "not inspected", 7.4, color=GREY)
    b += text(110, 96, "IP header (L3)   |   TCP/UDP header (L4)", 7.6, color=GREY)
    cols = [20, 52, 138, 220, 300]
    b += box(12, 104, 336, 20, PF, P, 3, 1.1)
    for c, h in zip(cols, ["#", "Source", "Destination", "Dst port", "Action"]):
        b += text(c, 118, h, 8.4, anchor="start", weight="bold", color=P)
    rules = [("1", "any", "192.168.1.10", "80, 443", "Allow"), ("2", "any", "192.168.1.11", "25", "Allow"),
             ("3", "192.168.1.0/24", "any", "any", "Allow"), ("4", "any", "any", "23", "Deny"), ("5", "any", "any", "any", "Deny")]
    for i, r in enumerate(rules):
        y = 124 + i * 20
        b += box(12, y, 336, 20, "#fff" if i % 2 else "#FAFAFA", "#DDD", 0, 0.6)
        for j, (c, v) in enumerate(zip(cols, r)):
            col = (GREEN if v == "Allow" else RED) if j == 4 else INK
            b += text(c, y + 14, v, 8.2, anchor="start", color=col, weight="bold" if j == 4 else "normal", mono=j in (1, 2, 3))
    b += text(180, 238, "Rules are checked top to bottom; first match wins.", 8.2, color=GREY)
    b += note(12, 248, 336, ["Last rule = default deny. Works at network / transport layer.",
                             "Fast and cheap (often built into routers) but cannot",
                             "see the content, users or application commands."])
    return svg(360, 308, b)


def proxy():
    b = title("Proxy Firewall (Application Gateway)")
    b += pc(40, 96, "Client", BLUE, BLUEF)
    b += box(126, 60, 108, 96, ORANGEF, ORANGE, 8, 1.4)
    b += text(180, 78, "Proxy", 10, weight="bold", color=ORANGE)
    for k, s in enumerate(["checks URL, user,", "commands, content", "(HTTP, FTP, SMTP)", "logs and caches"]):
        b += text(180, 96 + k * 13, s, 7.8, color=INK)
    b += server(320, 98, "Server", TEAL, TEALF)
    b += harr(58, 124, 88, BLUE) + harr(124, 58, 106, BLUE)
    b += harr(236, 302, 88, TEAL) + harr(302, 236, 106, TEAL)
    b += text(91, 82, "conn. 1", 7.6, color=BLUE, weight="bold")
    b += text(269, 82, "conn. 2", 7.6, color=TEAL, weight="bold")
    b += text(180, 178, "No direct connection between client and server:", 8.4, color=P, weight="bold")
    b += text(180, 191, "the server sees only the proxy's address.", 8.4, color=P)
    b += cell(30, 202, 130, 22, "GET /notes.html", GREENF, GREEN, 8.4, GREEN, mono=True)
    b += tick(172, 213)
    b += cell(200, 202, 130, 22, "GET /virus.exe", REDF, RED, 8.4, RED, mono=True)
    b += cross(342, 213)
    b += note(12, 236, 336, ["Works at the application layer (layer 7); understands",
                             "the protocol, so it can filter content and authenticate",
                             "users. More secure but slower; one proxy per service."])
    return svg(360, 296, b)


def fw_osi():
    b = title("Firewall Types and OSI Layers")
    rows = [("7 Application", "Proxy / application gateway", LC[0]), ("6 Presentation", "", LC[1]), ("5 Session", "Circuit-level gateway", LC[2]),
            ("4 Transport", "Stateful inspection, packet filter", LC[3]), ("3 Network", "Packet filter", LC[4]),
            ("2 Data Link", "", LC[5]), ("1 Physical", "", LC[6])]
    for i, (lay, fw, (f, s)) in enumerate(rows):
        y = 42 + i * 30
        b += box(12, y, 112, 26, f, s, 4, 1.2)
        b += text(68, y + 17, lay, 9, weight="bold", color=s)
        if fw:
            b += box(132, y, 216, 26, "#fff", s, 4, 1.2)
            b += text(240, y + 17, fw, 8.8, color=INK, weight="bold")
    b += note(12, 256, 336, ["Higher layer = more checking (content, users), more security,",
                             "but slower. NGFW combines all, plus intrusion prevention."], size=9.2)
    return svg(360, 300, b)


DIAGRAMS = {"cn5_cia": cia, "cn5_attacks": attacks, "cn5_encrypt": encrypt, "cn5_hash": hashv, "cn5_dos": dos,
            "cn5_pyramid": pyramid, "cn5_virus_worm": virus_worm, "cn5_firewall": firewall, "cn5_dmz": dmz,
            "cn5_pfilter": pfilter, "cn5_proxy": proxy, "cn5_fw_osi": fw_osi}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
