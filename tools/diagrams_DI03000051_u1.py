"""DI03000051 Computer Networks - Unit 1 diagrams: data-communication components, connection types, LAN/MAN/WAN/Internet,
six topologies, client-server and proxy server."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000051", "diagrams")
PF = "#F1E8FC"
GREY = "#666"


def pc(cx, cy, label=None, color=BLUE, fill=BLUEF, size=8.4):
    """Small computer icon (monitor + stand) centred at cx, cy; label below."""
    b = box(cx - 13, cy - 11, 26, 18, fill, color, 2.5, 1.4)
    b += box(cx - 9.5, cy - 7.5, 19, 11, "#fff", color, 1, 0.7)
    b += line(f"M{cx},{cy + 7} L{cx},{cy + 11}", color, 1.4)
    b += line(f"M{cx - 7},{cy + 11.5} L{cx + 7},{cy + 11.5}", color, 1.6)
    if label:
        b += text(cx, cy + 23, label, size, color=INK)
    return b


def dev(cx, cy, label, w=54, h=22, fill=ORANGEF, stroke=ORANGE, size=9):
    return rbox(cx, cy, w, h, label, fill=fill, stroke=stroke, size=size, weight="bold")


def cable(x1, y1, x2, y2, color=GREY, w=1.5, dash=None):
    return line(f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}", color, w, dash)


def term(x, y):
    return box(x - 3, y - 7, 6, 14, RED, RED, 1, 1)


# ------------------------------------------------------------------ 1.1
def basic():
    b = title("Components of Data Communication")
    y = 92
    b += cable(76, y, 284, y, TEAL, 2.4)
    b += pc(50, y, None, BLUE, BLUEF)
    b += pc(310, y, None, GREEN, GREENF)
    b += text(50, y + 26, "Sender", 10, weight="bold", color=BLUE)
    b += text(310, y + 26, "Receiver", 10, weight="bold", color=GREEN)
    b += box(158, y - 34, 44, 26, "#FFF8E1", ORANGE, 3, 1.3)
    b += line(f"M158,{y - 34} L180,{y - 18} L202,{y - 34}", ORANGE, 1.2)
    b += text(180, y - 42, "Message", 10, weight="bold", color=ORANGE)
    b += text(180, y + 15, "Transmission medium", 9.4, color=TEAL, weight="bold")
    b += arr([(214, y - 21), (262, y - 21)], ORANGE)
    for cx, c, f in ((50, BLUE, BLUEF), (310, GREEN, GREENF)):
        b += box(cx - 42, y + 38, 84, 54, f, c, 5, 1.2)
        b += text(cx, y + 52, "Protocol", 9.4, weight="bold", color=c)
        b += text(cx, y + 66, "Rule 1, Rule 2", 8.4)
        b += text(cx, y + 80, "... Rule n", 8.4)
    b += note(12, 202, 336, ["1. Message: data to be sent (text, image, audio, video).",
                             "2. Sender: device that sends the message.",
                             "3. Receiver: device that receives the message.",
                             "4. Medium: physical path (cable, radio waves).",
                             "5. Protocol: rules both sides must follow."])
    return svg(360, 292, b)


# ------------------------------------------------------------------ 1.2
def conn():
    b = title("Types of Connection")
    b += text(180, 46, "(a) Point to Point: dedicated link", 10.5, weight="bold", color=BLUE)
    b += cable(84, 78, 276, 78, BLUE, 2.4)
    b += pc(60, 78, "Station A")
    b += pc(300, 78, "Station B")
    b += text(180, 72, "whole capacity for A and B", 8.6, color=GREY)
    b += text(180, 132, "(b) Multipoint: one shared link", 10.5, weight="bold", color=GREEN)
    ly = 160
    b += cable(30, ly, 330, ly, GREEN, 2.4)
    for i, x in enumerate((60, 140, 220, 300)):
        b += cable(x, ly, x, ly + 18, GREEN, 1.5)
        b += pc(x, ly + 30, f"Station {'ABCD'[i]}", GREEN, GREENF)
    b += text(180, ly - 7, "link capacity shared (spatially / by time)", 8.6, color=GREY)
    b += note(12, 222, 336, ["Point to point: e.g. TV remote, PC to printer cable.",
                             "Multipoint (multidrop): e.g. bus LAN, Wi-Fi."])
    return svg(360, 264, b)


# ------------------------------------------------------------------ 1.3
def lan():
    b = title("Local Area Network (LAN)")
    b += box(14, 38, 332, 150, "#FAFAFA", GREY, 8, 1)
    b += text(26, 54, "One room / building / campus (up to ~1 km)", 9, anchor="start", color=GREY)
    b += cable(90, 96, 290, 96, GREY)
    b += dev(180, 96, "Switch", 64, 24, TEALF, TEAL)
    b += dev(66, 96, "Server", 56, 22, PF, P, 8.8)
    b += dev(294, 96, "Printer", 58, 22, GREENF, GREEN, 8.8)
    xs = [50, 130, 230, 310]
    for x in xs:
        b += cable(x, 142, 180, 108, GREY)
    for i, x in enumerate(xs):
        b += pc(x, 152, f"PC {i + 1}")
    b += note(12, 198, 336, ["Owned by one organisation; high speed 100 Mbps-10 Gbps.",
                             "Low error rate; Ethernet (IEEE 802.3), Wi-Fi (802.11).",
                             "Use: share files, printers, Internet in lab / office."])
    return svg(360, 258, b)


def man():
    b = title("Metropolitan Area Network (MAN)")
    cx, cy, r = 180, 120, 62
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{TEAL}" stroke-width="2.4"/>'
    b += text(cx, cy - 4, "City backbone", 9.4, weight="bold", color=TEAL)
    b += text(cx, cy + 10, "(fiber ring)", 8.6, color=TEAL)
    names = ["College LAN", "Bank LAN", "Office LAN", "Hospital LAN"]
    for i, n in enumerate(names):
        a = math.radians(-135 + i * 90)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ORANGE}"/>'
        lx = x + (-46 if x < cx else 46)
        ly = y + (-14 if y < cy else 14)
        b += cable(x, y, lx, ly, GREY, 1.2)
        b += rbox(lx, ly, 82, 22, n, fill=BLUEF, stroke=BLUE, size=8.8, weight="bold")
    b += text(180, 216, "Covers a city: about 5-50 km", 9.4, color=GREY)
    b += note(12, 228, 336, ["Connects many LANs of one city; owned by a company",
                             "or government. e.g. cable TV network, city Wi-Fi."])
    return svg(360, 270, b)


def wan():
    b = title("Wide Area Network (WAN)")
    cities = [(60, 80, "Surat"), (300, 80, "Delhi"), (60, 190, "Mumbai"), (300, 190, "Chennai")]
    links = [(0, 1), (0, 2), (1, 3), (2, 3), (0, 3)]
    for a, c in links:
        x1, y1, _ = cities[a]; x2, y2, _ = cities[c]
        b += cable(x1, y1, x2, y2, TEAL, 2)
    for x, y, n in cities:
        b += f'<circle cx="{x}" cy="{y}" r="15" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.5"/>'
        b += text(x, y + 3.5, "R", 10, weight="bold", color=ORANGE)
        b += text(x, y + (-22 if y < 130 else 30), n + " LAN", 9.4, weight="bold", color=BLUE)
    b += text(180, 70, "leased line / fiber", 8.6, color=TEAL)
    b += text(180, 226, "R = router", 8.6, color=GREY)
    b += box(150, 112, 60, 24, "#FFF8E1", ORANGE, 12, 1.2)
    b += text(180, 128, "satellite", 8.6, color=ORANGE)
    b += note(12, 238, 336, ["Covers a country / continent (100s-1000s of km).",
                             "Uses routers, leased lines, fiber, satellite links.",
                             "Lower speed, higher cost and delay than LAN."])
    return svg(360, 298, b)


def internet():
    b = title("The Internet: Network of Networks")
    b += box(110, 46, 140, 34, PF, P, 17, 1.6)
    b += text(180, 60, "Internet backbone", 10, weight="bold", color=P)
    b += text(180, 73, "(Tier-1 ISPs)", 8.6, color=P)
    isps = [(60, 130, "ISP: Jio"), (180, 130, "ISP: Airtel"), (300, 130, "ISP: BSNL")]
    for x, y, n in isps:
        b += cable(x, y - 12, 180 + (x - 180) * 0.3, 80, GREY, 1.6)
        b += dev(x, y, n, 78, 24, TEALF, TEAL, 8.8)
    users = [(30, "Home"), (90, "Mobile"), (150, "College"), (210, "Office"), (270, "Server"), (330, "Cafe")]
    for i, (x, n) in enumerate(users):
        px = isps[i // 2][0]
        b += cable(x, 178, px, 142, GREY, 1.2)
        b += pc(x, 186, n, BLUE, BLUEF, 8)
    b += note(12, 222, 336, ["Worldwide network of millions of networks using TCP/IP.",
                             "Services: WWW, e-mail, FTP, video calls, cloud."])
    return svg(360, 264, b)


# ------------------------------------------------------------------ 1.4 topologies
def bus():
    b = title("Bus Topology")
    y = 112
    b += cable(28, y, 332, y, TEAL, 3)
    b += term(26, y); b += term(334, y)
    b += text(30, y + 22, "terminator", 8, anchor="start", color=RED)
    b += text(330, y + 22, "terminator", 8, anchor="end", color=RED)
    for i, x in enumerate((84, 164, 244, 316)):
        b += cable(x, y, x, 76, GREY)
        b += f'<circle cx="{x}" cy="{y}" r="3" fill="{INK}"/>'
        b += pc(x, 64, None)
    for i, x in enumerate((124, 204, 284)):
        b += cable(x, y, x, 148, GREY)
        b += f'<circle cx="{x}" cy="{y}" r="3" fill="{INK}"/>'
        b += pc(x, 160, None)
    b += text(30, y - 8, "backbone", 8.6, anchor="start", color=TEAL, weight="bold")
    b += text(24, 180, "drop line + tap", 8, anchor="start", color=GREY)
    b += note(12, 196, 336, ["All devices share one backbone cable (multipoint).",
                             "+ Easy to install, least cable, cheap.",
                             ("- Backbone fault stops the whole network;", RED),
                             ("  collisions; difficult fault isolation.", RED)])
    return svg(360, 268, b)


def star():
    b = title("Star Topology")
    cx, cy, r = 180, 116, 72
    for i in range(6):
        a = math.radians(-90 + i * 60)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        b += cable(cx, cy, x, y, GREY)
    b += dev(cx, cy, "Hub / Switch", 84, 26, TEALF, TEAL, 9)
    for i in range(6):
        a = math.radians(-90 + i * 60)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        b += pc(x, y, None)
    b += note(12, 206, 336, ["Each device has a dedicated link to a central hub.",
                             "+ Easy to install, add, remove; one link fault",
                             "  affects only that device; easy fault detection.",
                             ("- Hub failure stops all; more cable than bus.", RED)])
    return svg(360, 278, b)


def ring():
    b = title("Ring Topology")
    cx, cy, r = 180, 114, 70
    pts = [(cx + r * math.cos(math.radians(-90 + i * 60)), cy + r * math.sin(math.radians(-90 + i * 60))) for i in range(6)]
    for i in range(6):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 6]
        b += cable(x1, y1, x2, y2, TEAL, 2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ang = math.atan2(y2 - y1, x2 - x1)
        b += arrowhead(mx + 4 * math.cos(ang), my + 4 * math.sin(ang), math.degrees(ang), 7, TEAL)
    for i, (x, y) in enumerate(pts):
        b += pc(x, y, None)
    b += text(cx, cy - 4, "token passes", 9, color=TEAL, weight="bold")
    b += text(cx, cy + 10, "in one direction", 9, color=TEAL)
    b += note(12, 202, 336, ["Each device connects to its two neighbours; data",
                             "passes from device to device (repeaters).",
                             "+ No collisions (token), equal access, easy to add.",
                             ("- One break can stop the ring; slow for many nodes.", RED)])
    return svg(360, 274, b)


def mesh():
    b = title("Mesh Topology (6 devices)")
    cx, cy, r = 180, 124, 70
    pts = [(cx + r * math.cos(math.radians(-90 + i * 60)), cy + r * math.sin(math.radians(-90 + i * 60))) for i in range(6)]
    for i in range(6):
        for j in range(i + 1, 6):
            b += cable(*pts[i], *pts[j], GREY, 1.2)
    for i, (x, y) in enumerate(pts):
        b += pc(x, y, None)
        if abs(x - cx) > 1:
            b += text(x + (20 if x > cx else -20), y + 4, "5 ports", 7.8, color=ORANGE, anchor="start" if x > cx else "end")
    b += note(12, 212, 336, ["Every device has a dedicated link to every other.",
                             ("Links = n(n-1)/2 = 6x5/2 = 15;  ports/device = n-1 = 5", P),
                             "+ Robust, private, no traffic problem, easy fault find.",
                             ("- Very costly: much cable and many ports.", RED)])
    return svg(360, 284, b)


def tree():
    b = title("Tree Topology")
    b += dev(180, 54, "Central hub", 90, 24, TEALF, TEAL)
    subs = [(90, 112), (270, 112)]
    for x, y in subs:
        b += cable(180, 66, x, y - 12, GREY, 1.8)
        b += dev(x, y, "Secondary hub", 98, 22, ORANGEF, ORANGE, 8.6)
    for x, y in subs:
        for dx in (-50, 0, 50):
            b += cable(x, y + 11, x + dx, 160, GREY)
            b += pc(x + dx, 168, None)
    b += note(12, 196, 336, ["Hierarchy of star networks: secondary hubs connect",
                             "to a central (root) hub. Used in colleges, offices.",
                             "+ Easy to expand; fault isolation per branch.",
                             ("- Root hub / backbone failure affects all below.", RED)])
    return svg(360, 268, b)


def hybrid():
    b = title("Hybrid Topology (star + ring + bus)")
    y = 64
    b += cable(28, y, 332, y, TEAL, 3)
    b += term(26, y); b += term(334, y)
    b += text(130, y - 8, "bus backbone", 8.6, color=TEAL, weight="bold")
    # star part
    b += cable(90, y, 90, 104, GREY, 1.8)
    b += dev(90, 112, "Hub", 44, 20, TEALF, TEAL)
    for dx in (-55, 0, 55):
        b += cable(90, 122, 90 + dx, 152, GREY)
        b += pc(90 + dx, 160, None)
    b += text(90, 192, "Star", 9.6, weight="bold", color=BLUE)
    # ring part
    cx, cy, r = 268, 136, 36
    pts = [(cx + r * math.cos(math.radians(-90 + i * 90)), cy + r * math.sin(math.radians(-90 + i * 90))) for i in range(4)]
    b += cable(268, y, *pts[0], GREY, 1.8)
    for i in range(4):
        b += cable(*pts[i], *pts[(i + 1) % 4], TEAL, 1.8)
    for x, yy in pts:
        b += pc(x, yy, None)
    b += text(cx, cy + 4, "Ring", 9.6, weight="bold", color=BLUE)
    b += note(12, 206, 336, ["Combination of two or more topologies.",
                             "+ Flexible, reliable, scalable for big networks.",
                             ("- Complex design; costly to install and manage.", RED)])
    return svg(360, 262, b)


# ------------------------------------------------------------------ 1.6 servers
def client_server():
    b = title("Client-Server Network and Servers")
    for i, x in enumerate((50, 130, 210, 290)):
        b += cable(x, 88, 180, 104, GREY, 1.3)
        b += pc(x, 60, f"Client {i + 1}", BLUE, BLUEF, 8)
    b += dev(180, 116, "Network (LAN / Internet)", 170, 24, TEALF, TEAL, 9)
    servers = [(44, "File"), (112, "Print"), (180, "Mail"), (248, "Web"), (316, "Proxy")]
    for x, n in servers:
        b += cable(180, 128, x, 160, GREY, 1.3)
        b += box(x - 26, 160, 52, 44, PF, P, 4, 1.4)
        for k in range(3):
            b += line(f"M{x - 18},{170 + k * 10} L{x + 18},{170 + k * 10}", P, 1)
        b += text(x, 218, n, 9, weight="bold", color=P)
        b += text(x, 230, "server", 8, color=GREY)
    b += note(12, 240, 336, ["Client requests a service; server provides it.",
                             "Server: powerful computer + server software that",
                             "serves many clients at the same time."])
    return svg(360, 300, b)


def proxy():
    b = title("Proxy Server")
    for i, y in enumerate((70, 120, 170)):
        b += pc(40, y, f"Client {i + 1}", BLUE, BLUEF, 8)
        b += arr([(58, y - 2), (126, 120 - 2 + (y - 120) * 0.25)], BLUE)
    b += box(130, 84, 92, 72, PF, P, 6, 1.6)
    b += text(176, 104, "Proxy server", 9.6, weight="bold", color=P)
    b += box(144, 112, 64, 34, "#FFF8E1", ORANGE, 4, 1.1)
    b += text(176, 126, "cache", 8.8, weight="bold", color=ORANGE)
    b += text(176, 139, "+ filter, log", 8, color=ORANGE)
    b += arr([(224, 112), (266, 112)], P, )
    b += arr([(266, 130), (224, 130)], GREEN)
    b += text(245, 104, "request", 8, color=P)
    b += text(245, 146, "reply", 8, color=GREEN)
    b += f'<ellipse cx="310" cy="121" rx="40" ry="26" fill="{TEALF}" stroke="{TEAL}" stroke-width="1.5"/>'
    b += text(310, 118, "Internet", 9.4, weight="bold", color=TEAL)
    b += text(310, 131, "web servers", 8, color=TEAL)
    b += note(12, 200, 336, ["Intermediary between clients and the Internet.",
                             "Cache hit: page served from cache (faster, saves",
                             "bandwidth). Hides client IP; blocks bad sites."])
    return svg(360, 258, b)


DIAGRAMS = {"cn1_basic": basic, "cn1_conn": conn, "cn1_lan": lan, "cn1_man": man, "cn1_wan": wan, "cn1_internet": internet,
            "cn1_bus": bus, "cn1_star": star, "cn1_ring": ring, "cn1_mesh": mesh, "cn1_tree": tree, "cn1_hybrid": hybrid,
            "cn1_client_server": client_server, "cn1_proxy": proxy}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
