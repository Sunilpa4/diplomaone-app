"""DI03000051 Computer Networks - Unit 3 diagrams: media classification, twisted pair, RJ-45 colour codes, coaxial, fiber,
fiber modes, propagation, spectrum, microwave, satellite, repeater, hub vs switch, bridge, router, access point, NIC,
devices vs OSI layers."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000051_u1 import pc, dev, cable
from diagrams_DI03000051_u2 import harr, varr, LC

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000051", "diagrams")
PF = "#F1E8FC"
GREY = "#666"
BROWN = "#795548"
WCOL = {"orange": "#F57C00", "green": "#2E7D32", "blue": "#1565C0", "brown": "#6D4C41"}


def poly(pts, color=INK, w=1.6, dash=None):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return line(d, color, w, dash)


def leader(x1, y1, x2, y2, label, anchor="middle", color=INK, size=8.6):
    b = line(f"M{x1},{y1} L{x2},{y2}", GREY, 0.9)
    b += f'<circle cx="{x1}" cy="{y1}" r="2" fill="{GREY}"/>'
    b += text(x2, y2 - 4, label, size, anchor=anchor, color=color, weight="bold")
    return b


# ------------------------------------------------------------------ 3.1 guided
def classify():
    b = title("Classification of Transmission Media")
    b += rbox(180, 52, 150, 26, "Transmission media", fill=PF, stroke=P, size=10, weight="bold")
    for x, n, s, f in ((92, "Guided (wired)", BLUE, BLUEF), (268, "Unguided (wireless)", GREEN, GREENF)):
        b += line(f"M180,65 L180,80 L{x},80 L{x},92", GREY, 1.3)
        b += rbox(x, 104, 140, 24, n, fill=f, stroke=s, size=9.6, weight="bold")
    g = [("Twisted pair", "UTP, STP"), ("Coaxial cable", "RG-59, RG-58"), ("Fiber optic", "single / multimode")]
    u = [("Radio waves", "3 kHz-1 GHz"), ("Microwaves", "1-300 GHz"), ("Infrared", "300 GHz-400 THz")]
    for col, items, s, f in ((92, g, BLUE, BLUEF), (268, u, GREEN, GREENF)):
        b += line(f"M{col - 66},116 L{col - 66},{140 + 2 * 38 + 14}", GREY, 1.1)
        for i, (n, sub) in enumerate(items):
            y = 140 + i * 38
            b += line(f"M{col - 66},{y + 14} L{col - 56},{y + 14}", GREY, 1.1)
            b += box(col - 56, y, 128, 30, "#fff", s, 4, 1.2)
            b += text(col + 8, y + 13, n, 9, weight="bold", color=s)
            b += text(col + 8, y + 25, sub, 7.8, color=GREY)
    b += note(12, 262, 336, ["Guided: signal travels in a physical path (copper or glass).",
                             "Unguided: electromagnetic waves through air / vacuum,",
                             "no physical conductor (also called wireless)."])
    return svg(360, 322, b)


def twisted():
    b = title("Twisted Pair Cable: UTP and STP")
    # twisted wires
    x0, x1, yc = 30, 330, 62
    pa = [(x, yc + 9 * math.sin((x - x0) / 14)) for x in range(x0, x1 + 1, 3)]
    pb = [(x, yc - 9 * math.sin((x - x0) / 14)) for x in range(x0, x1 + 1, 3)]
    b += poly(pa, WCOL["orange"], 2.6) + poly(pb, "#BBB", 2.6)
    b += text(180, 90, "two insulated copper wires twisted together (cancels noise)", 8.4, color=GREY)
    pairs = ["orange", "green", "blue", "brown"]
    for cx, name, stp in ((95, "UTP (unshielded)", False), (265, "STP (shielded)", True)):
        cy = 168
        b += f'<circle cx="{cx}" cy="{cy}" r="52" fill="#ECEFF1" stroke="{GREY}" stroke-width="2"/>'
        if stp:
            b += f'<circle cx="{cx}" cy="{cy}" r="46" fill="none" stroke="#9E9E9E" stroke-width="3" stroke-dasharray="2,2"/>'
        for k, c in enumerate(pairs):
            a = math.radians(45 + k * 90)
            px, py = cx + 22 * math.cos(a), cy + 22 * math.sin(a)
            if stp:
                b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="15" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="1.6"/>'
            for j, col in enumerate((WCOL[c], "#fff")):
                ox = 6 * math.cos(a + math.pi / 2) * (1 if j == 0 else -1)
                oy = 6 * math.sin(a + math.pi / 2) * (1 if j == 0 else -1)
                b += f'<circle cx="{px + ox:.1f}" cy="{py + oy:.1f}" r="5.5" fill="{col}" stroke="{WCOL[c]}" stroke-width="1.4"/>'
        b += text(cx, cy + 68, name, 9.6, weight="bold", color=BLUE)
    b += text(265, 108, "foil around each pair + braid", 7.8, color=GREY)
    b += note(12, 254, 336, ["4 pairs, 8 wires; colour codes orange, green, blue, brown.",
                             "UTP: cheap, flexible, used in LANs (Cat5e, Cat6).",
                             "STP: metal shield reduces noise and crosstalk; costly."])
    return svg(360, 314, b)


def rj45():
    b = title("RJ-45 Colour Codes (Practical 3)")
    A = [("white", "green"), ("green", None), ("white", "orange"), ("blue", None), ("white", "blue"), ("orange", None),
         ("white", "brown"), ("brown", None)]
    B = [("white", "orange"), ("orange", None), ("white", "green"), ("blue", None), ("white", "blue"), ("green", None),
         ("white", "brown"), ("brown", None)]
    for x0, name, std in ((22, "T568A", A), (196, "T568B", B)):
        b += box(x0, 46, 142, 118, "#F5F5F5", GREY, 6, 1.4)
        b += text(x0 + 71, 62, name, 10.5, weight="bold", color=P)
        for i, (c1, c2) in enumerate(std):
            x = x0 + 13 + i * 15.5
            if c2 is None:
                b += box(x, 70, 11, 64, WCOL[c1], WCOL[c1], 1, 1)
            else:
                b += box(x, 70, 11, 64, "#fff", WCOL[c2], 1, 1)
                b += box(x + 3.5, 70, 4, 64, WCOL[c2], WCOL[c2], 0, 0.5)
            b += text(x + 5.5, 148, str(i + 1), 8.6, weight="bold")
        b += text(x0 + 71, 160, "pin 1 to 8 (clip down)", 7.8, color=GREY)
    b += box(12, 176, 336, 44, BLUEF, BLUE, 6, 1.2)
    b += text(22, 193, "Straight-through: B to B (or A to A)", 9.4, anchor="start", weight="bold", color=BLUE)
    b += text(22, 209, "different devices: PC to switch, switch to router", 8.6, anchor="start")
    b += box(12, 228, 336, 44, ORANGEF, ORANGE, 6, 1.2)
    b += text(22, 245, "Crossover: A at one end, B at the other", 9.4, anchor="start", weight="bold", color=ORANGE)
    b += text(22, 261, "same devices: PC to PC, switch to switch", 8.6, anchor="start")
    b += note(12, 280, 336, ["Cross swaps pairs: 1-3 and 2-6 (transmit to receive).",
                             "Tools: crimping tool, RJ-45 connectors, LAN tester."])
    return svg(360, 326, b)


def coax():
    b = title("Coaxial Cable")
    layers = [(20, 330, 30, "#455A64", "Outer jacket (PVC)"), (90, 330, 24, "#B0BEC5", "Braided outer conductor (shield)"),
              (170, 330, 16, "#FFFFFF", "Insulator (dielectric)"), (250, 330, 5, "#E65100", "Inner copper conductor")]
    yc = 104
    for x, xe, r, f, n in layers:
        b += box(x, yc - r, xe - x, 2 * r, f, "#37474F", 3 if r > 6 else 1, 1.2)
    labels = [(55, yc - 30, 40, 54, "Outer jacket"), (130, yc - 24, 120, 66, "Braided shield"),
              (210, yc - 16, 220, 54, "Insulator"), (290, yc - 5, 300, 66, "Copper core")]
    for x1, y1, x2, y2, n in labels:
        b += leader(x1, y1, x2, y2, n)
    # cross-section
    cx, cy = 70, 196
    for r, f in ((30, "#455A64"), (24, "#B0BEC5"), (16, "#fff"), (5, "#E65100")):
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="#37474F" stroke-width="1.2"/>'
    b += text(cx, cy + 44, "cross-section", 8.4, color=GREY)
    b += note(120, 160, 228, ["Connectors: BNC, BNC-T,", "BNC terminator, F-type (TV).",
                              "Types: RG-59 (cable TV),", "RG-58 (thin Ethernet),", "RG-11 (thick Ethernet)."], size=9)
    b += note(12, 252, 336, ["Uses: cable TV, CCTV, old 10Base2 / 10Base5 Ethernet,",
                             "long-distance telephone lines, broadband Internet."])
    return svg(360, 296, b)


def fiber():
    b = title("Fiber Optic Cable: Structure")
    yc = 84
    layers = [(20, 330, 26, "#FFB300", "Jacket"), (90, 330, 20, "#E0E0E0", "Buffer coating"),
              (160, 330, 13, "#B3E5FC", "Cladding (glass, lower n)"), (240, 330, 6, "#E1F5FE", "Core")]
    for x, xe, r, f, n in layers:
        b += box(x, yc - r, xe - x, 2 * r, f, "#546E7A", 3 if r > 6 else 1, 1.2)
    for x1, y1, x2, y2, n in [(55, yc - 26, 46, 48, "Jacket"), (125, yc - 20, 125, 60, "Buffer"),
                              (200, yc - 13, 196, 48, "Cladding"), (285, yc - 6, 296, 60, "Core")]:
        b += leader(x1, y1, x2, y2, n)
    # TIR
    y1, y2 = 150, 200
    b += box(20, y1 - 14, 320, 14, "#B3E5FC", "#546E7A", 0, 1)
    b += box(20, y2, 320, 14, "#B3E5FC", "#546E7A", 0, 1)
    b += box(20, y1, 320, y2 - y1, "#E1F5FE", "#546E7A", 0, 1)
    b += text(330, y1 - 4, "cladding n2", 8, anchor="end", color=GREY)
    b += text(330, y2 + 11, "cladding n2", 8, anchor="end", color=GREY)
    pts, x, up = [(20, 186)], 20, True
    while x < 320:
        x += 46
        pts.append((min(x, 340), y1 if up else y2))
        up = not up
    b += poly(pts, RED, 1.8)
    b += arrowhead(pts[-1][0], pts[-1][1], math.degrees(math.atan2(pts[-1][1] - pts[-2][1], pts[-1][0] - pts[-2][0])), 7, RED)
    b += text(180, y2 + 30, "core n1 > cladding n2: total internal reflection", 8.8, color=RED, weight="bold")
    b += note(12, 240, 336, ["Carries data as pulses of light (LED / laser).",
                             "Angle > critical angle, so light stays in the core.",
                             "Connectors: SC, ST, LC, MT-RJ."])
    return svg(360, 300, b)


def fiber_modes():
    b = title("Fiber Optic Propagation Modes")
    rows = [("Multimode step-index", 26, "step"), ("Multimode graded-index", 26, "graded"), ("Single mode", 7, "single")]
    for i, (n, half, kind) in enumerate(rows):
        yc = 84 + i * 86
        b += text(180, yc - 37, n, 9.8, weight="bold", color=P)
        b += box(70, yc - half - 6, 220, 2 * half + 12, "#B3E5FC", "#546E7A", 2, 1)
        b += box(70, yc - half, 220, 2 * half, "#E1F5FE", "#546E7A", 0, 0.8)
        if kind == "step":
            for k, c in ((0, RED), (1, ORANGE), (2, GREEN)):
                if k == 0:
                    b += poly([(70, yc), (290, yc)], c, 1.4)
                else:
                    seg = 220 / (2 * k + 1)
                    pts, x, s = [(70, yc)], 70, 1
                    x += seg / 2
                    pts.append((x, yc - s * half)); s = -s
                    while x + seg <= 290.5:
                        x += seg
                        pts.append((x, yc - s * half)); s = -s
                    pts.append((290, yc))
                    b += poly(pts, c, 1.3)
        elif kind == "graded":
            for amp, c in ((0, RED), (12, ORANGE), (22, GREEN)):
                pts = [(x, yc - amp * math.sin((x - 70) / 220 * 4 * math.pi)) for x in range(70, 291, 4)]
                b += poly(pts, c, 1.3)
        else:
            b += poly([(70, yc), (290, yc)], RED, 1.8)
        # pulses
        w_in, w_out = 6, (24 if kind == "step" else 16 if kind == "graded" else 10)
        b += poly([(20, yc + 10), (36 - w_in / 2, yc + 10), (36 - w_in / 2, yc - 10), (36 + w_in / 2, yc - 10), (36 + w_in / 2, yc + 10), (56, yc + 10)], BLUE, 1.5)
        top = max(w_out - 8, 2)
        hgt = 18 if kind == "single" else 14 if kind == "graded" else 10
        b += poly([(300, yc + 10), (322 - w_out / 2, yc + 10), (322 - top / 2, yc + 10 - hgt), (322 + top / 2, yc + 10 - hgt),
                   (322 + w_out / 2, yc + 10), (344, yc + 10)], BLUE, 1.5)
    b += text(36, 306, "input pulse", 8, color=BLUE)
    b += text(322, 306, "output pulse", 8, color=BLUE)
    b += note(12, 316, 336, ["Step-index: many paths, pulse spreads (short links).",
                             "Graded-index: core n decreases outward, less spread.",
                             "Single mode: thin core (8-10 µm), one path, laser,",
                             "longest distance and highest bandwidth."])
    return svg(360, 390, b)


# ------------------------------------------------------------------ 3.2 unguided
def earth(y, x0=12, x1=348, sag=10):
    return f'<path d="M{x0},{y} Q180,{y - sag * 2} {x1},{y} L{x1},{y + 10} L{x0},{y + 10} Z" fill="#C8E6C9" stroke="{GREEN}" stroke-width="1.2"/>'


def tower(x, y, h=26, color=GREY):
    b = line(f"M{x - 6},{y} L{x},{y - h} L{x + 6},{y}", color, 1.5)
    b += line(f"M{x - 4},{y - h * 0.4} L{x + 4},{y - h * 0.4}", color, 1)
    b += f'<circle cx="{x}" cy="{y - h}" r="2.6" fill="{RED}"/>'
    return b


def prop():
    b = title("Propagation Methods")
    # ground
    y = 104
    b += text(180, 46, "Ground propagation (below 2 MHz): follows the earth", 8.8, weight="bold", color=BLUE)
    b += earth(y, sag=10)
    b += tower(40, y - 6)
    b += tower(320, y - 6)
    pts = [(x, (y - 14) - 20 * (1 - ((x - 180) / 168) ** 2) * 0.5 - 2 * math.sin(x / 5)) for x in range(46, 316, 3)]
    b += poly(pts, BLUE, 1.5)
    # sky
    y = 204
    b += text(180, 124, "Sky propagation (2-30 MHz): reflected by ionosphere", 8.8, weight="bold", color=ORANGE)
    b += f'<path d="M12,142 Q180,128 348,142" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-opacity="0.35"/>'
    b += text(300, 152, "ionosphere", 8, color=ORANGE)
    b += earth(y, sag=10)
    b += tower(40, y - 6)
    b += tower(320, y - 6)
    b += poly([(40, y - 32), (110, 140), (180, y - 18)], ORANGE, 1.5)
    b += poly([(180, y - 18), (250, 140), (320, y - 32)], ORANGE, 1.5)
    # LOS
    y = 290
    b += text(180, 226, "Line-of-sight (above 30 MHz): straight line, antennas", 8.8, weight="bold", color=RED)
    b += text(180, 238, "must face each other", 8.8, weight="bold", color=RED)
    b += earth(y, sag=6)
    b += tower(40, y - 4, 40)
    b += tower(320, y - 4, 40)
    b += line(f"M44,{y - 44} L316,{y - 44}", RED, 1.6) + arrowhead(316, y - 44, 0, 7, RED)
    b += note(12, 306, 336, ["Ground: AM radio. Sky: amateur radio, long-distance",
                             "broadcast. Line-of-sight: FM, TV, microwave, satellite."])
    return svg(360, 350, b)


def spectrum():
    b = title("Electromagnetic Spectrum")
    segs = [("Radio", 64, "#E3F2FD", BLUE), ("Micro-\nwave", 52, "#E0F2F1", TEAL), ("Infra-\nred", 48, "#FFEBEE", RED),
            ("Visible", 40, "#FFF8E1", ORANGE), ("UV", 34, "#F3E5F5", P), ("X-ray", 44, "#ECEFF1", GREY), ("Gamma", 54, "#EFEBE9", BROWN)]
    x, y = 12, 70
    for n, w, f, s in segs:
        b += box(x, y, w, 40, f, s, 2, 1.2)
        parts = n.split("\n")
        for k, ptxt in enumerate(parts):
            b += text(x + w / 2, y + 24 - 6 * (len(parts) - 1) + k * 12, ptxt, 8.6, weight="bold", color=s)
        x += w
    b += line(f"M12,{y + 50} L176,{y + 50}", GREEN, 2)
    b += text(94, y + 64, "used for communication", 8.6, color=GREEN, weight="bold")
    freqs = [(12, "3 kHz"), (76, "1 GHz"), (128, "300 GHz"), (176, "400 THz")]
    for fx, ft in freqs:
        b += line(f"M{fx},{y - 2} L{fx},{y - 8}", GREY, 1)
        b += text(fx, y - 12, ft, 7.6, color=GREY, anchor="start" if fx == 12 else "middle")
    b += harr(20, 340, 150, P)
    b += text(180, 144, "frequency increases →", 8.8, color=P)
    b += harr(340, 20, 172, TEAL)
    b += text(180, 166, "wavelength increases ←", 8.8, color=TEAL)
    b += note(12, 186, 336, ["Radio waves: 3 kHz-1 GHz, omnidirectional.",
                             "Microwaves: 1-300 GHz, unidirectional (line of sight).",
                             "Infrared: 300 GHz-400 THz, short range, no walls.",
                             "λ = c / f   (c = 3 × 10⁸ m/s)"])
    return svg(360, 262, b)


def microwave():
    b = title("Terrestrial Microwave Transmission")
    y = 170
    b += earth(y, sag=12)
    for x, lab in ((40, "Tower A"), (180, "Repeater"), (320, "Tower B")):
        yy = y - (12 if x == 180 else 2)
        b += line(f"M{x - 8},{yy} L{x},{yy - 70} L{x + 8},{yy}", GREY, 1.8)
        b += line(f"M{x - 6},{yy - 30} L{x + 6},{yy - 30}", GREY, 1)
        b += text(x, yy + 22, lab, 8.6, weight="bold", color=BLUE)
    dishes = [(46, 104, 0), (174, 94, 180), (186, 94, 0), (314, 104, 180)]
    for dx, dy, a in dishes:
        sgn = 1 if a == 0 else -1
        b += f'<path d="M{dx},{dy - 9} Q{dx + 8 * sgn},{dy} {dx},{dy + 9}" fill="none" stroke="{TEAL}" stroke-width="3"/>'
    b += harr(52, 168, 100, RED)
    b += harr(192, 308, 100, RED)
    b += text(110, 90, "line of sight", 8.4, color=RED)
    b += text(250, 90, "about 50 km", 8.4, color=RED)
    b += note(12, 200, 336, ["Parabolic dish antennas face each other on tall towers.",
                             "Repeaters needed because of earth's curvature.",
                             "Uses: mobile towers, TV links, long-distance telephone."])
    return svg(360, 260, b)


def satellite():
    b = title("Satellite Transmission")
    y = 210
    b += f'<path d="M12,{y} Q180,{y - 34} 348,{y} L348,{y + 12} L12,{y + 12} Z" fill="#C8E6C9" stroke="{GREEN}" stroke-width="1.2"/>'
    sx, sy = 180, 62
    b += box(sx - 12, sy - 10, 24, 20, "#ECEFF1", GREY, 3, 1.4)
    b += box(sx - 48, sy - 6, 32, 12, BLUEF, BLUE, 1, 1)
    b += box(sx + 16, sy - 6, 32, 12, BLUEF, BLUE, 1, 1)
    b += text(sx, sy - 18, "Satellite (transponder)", 9, weight="bold", color=P)
    for gx, lab in ((60, "Earth station A"), (300, "Earth station B")):
        gy = y - 14
        b += f'<path d="M{gx - 12},{gy - 10} Q{gx},{gy + 4} {gx + 12},{gy - 10}" fill="none" stroke="{TEAL}" stroke-width="3"/>'
        b += line(f"M{gx},{gy - 4} L{gx},{gy + 6}", GREY, 2)
        b += text(gx, y + 26, lab, 8.6, weight="bold", color=BLUE)
    b += line(f"M64,{y - 28} L{sx - 14},{sy + 12}", RED, 1.6) + arrowhead(sx - 14, sy + 12, math.degrees(math.atan2(sy + 12 - (y - 28), sx - 14 - 64)), 7, RED)
    b += line(f"M{sx + 14},{sy + 12} L296,{y - 28}", GREEN, 1.6) + arrowhead(296, y - 28, math.degrees(math.atan2(y - 28 - sy - 12, 296 - sx - 14)), 7, GREEN)
    b += text(92, 120, "uplink", 9, weight="bold", color=RED)
    b += text(270, 120, "downlink", 9, weight="bold", color=GREEN)
    b += text(180, 140, "GEO: 35,786 km", 8.6, color=GREY)
    b += note(12, 246, 336, ["Satellite receives on the uplink frequency, amplifies,",
                             "and retransmits on a different downlink frequency.",
                             "Orbits: GEO (TV, VSAT), MEO (GPS), LEO (Starlink).",
                             "Uses: DTH TV, GPS, weather, remote Internet."])
    return svg(360, 320, b)


# ------------------------------------------------------------------ 3.3 devices
def repeater():
    b = title("Repeater: Regenerates the Signal")
    y = 96
    # weak noisy signal
    import random
    random.seed(4)
    bits = [1, 0, 1, 1, 0, 1]
    pts, x = [], 16
    for bt in bits:
        for k in range(8):
            pts.append((x, y - (10 if bt else -2) + random.uniform(-4, 4)))
            x += 2.6
    b += poly(pts, GREY, 1.3)
    b += text(80, y + 30, "weak, noisy signal", 8.6, color=GREY)
    b += rbox(180, y, 64, 34, "Repeater", fill=ORANGEF, stroke=ORANGE, size=9.6, weight="bold")
    b += harr(144, 146, y, GREY)
    pts, x = [], 216
    prev = None
    for bt in bits:
        yy = y - 14 if bt else y + 10
        if prev is not None:
            pts.append((x, yy))
        else:
            pts.append((x, yy))
        pts.append((x + 21, yy))
        x += 21
        prev = yy
    b += poly(pts, BLUE, 2)
    b += text(280, y + 30, "regenerated: same bits", 8.6, color=BLUE)
    b += text(80, y - 26, "1 0 1 1 0 1", 9, mono=True, color=GREY)
    b += text(280, y - 26, "1 0 1 1 0 1", 9, mono=True, color=BLUE)
    b += note(12, 140, 336, ["Physical layer device. Regenerates (not just amplifies)",
                             "the original bit pattern and extends cable length",
                             "(Ethernet UTP: 100 m per segment). No filtering."])
    return svg(360, 200, b)


def hub_switch():
    b = title("Hub (broadcast) vs Switch (unicast)")

    def seg(cx, cy, px, py, f0, f1, color):
        x0, y0 = cx + (px - cx) * f0, cy + (py - cy) * f0
        x1, y1 = cx + (px - cx) * f1, cy + (py - cy) * f1
        return line(f"M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}", color, 2.4) + \
            arrowhead(x1, y1, math.degrees(math.atan2(y1 - y0, x1 - x0)), 7, color)

    for cx, n, sw in ((92, "Hub", False), (268, "Switch", True)):
        cy = 116
        pcs = [(cx - 60, 66, "A"), (cx + 60, 66, "B"), (cx - 60, 170, "C"), (cx + 60, 170, "D")]
        for px, py, lab in pcs:
            b += cable(cx, cy, px, py, GREY, 1.3)
        b += seg(cx, cy, cx - 60, 66, 0.75, 0.38, BLUE)
        targets = [pcs[3]] if sw else pcs[1:]
        for px, py, lab in targets:
            b += seg(cx, cy, px, py, 0.4, 0.78, GREEN if sw else RED)
        b += dev(cx, cy, n, 60, 24, TEALF if sw else ORANGEF, TEAL if sw else ORANGE)
        for px, py, lab in pcs:
            b += pc(px, py)
            b += text(px + (20 if px > cx else -20), py + 4, lab, 9.4, weight="bold", color=BLUE)
        b += text(cx, 204, "A sends to D:", 8.6, weight="bold")
        b += text(cx, 216, "goes to D only (MAC table)" if sw else "copied to B, C and D", 8.4, color=GREEN if sw else RED)
    b += note(12, 228, 336, ["Hub: layer 1, multiport repeater, one collision domain,",
                             "half duplex, shares bandwidth.",
                             "Switch: layer 2, learns MAC addresses, full duplex,",
                             "each port its own collision domain."])
    return svg(360, 302, b)


def bridge():
    b = title("Bridge: Connects Two LAN Segments")
    y = 100
    b += cable(16, y, 150, y, TEAL, 3)
    b += cable(210, y, 344, y, TEAL, 3)
    b += dev(180, y, "Bridge", 56, 26, ORANGEF, ORANGE)
    b += text(150, y - 8, "port 1", 8, color=ORANGE, anchor="end")
    b += text(210, y - 8, "port 2", 8, color=ORANGE, anchor="start")
    for x, lab in ((44, "A"), (110, "B"), (250, "C"), (316, "D")):
        b += cable(x, y, x, y - 26, GREY)
        b += pc(x, y - 38)
        b += text(x, y + 16, lab, 9.4, weight="bold", color=BLUE)
    b += text(83, y + 34, "LAN segment 1", 8.8, color=TEAL, weight="bold")
    b += text(277, y + 34, "LAN segment 2", 8.8, color=TEAL, weight="bold")
    b += box(110, 146, 140, 56, "#fff", ORANGE, 4, 1.2)
    b += text(180, 160, "Bridge table", 9, weight="bold", color=ORANGE)
    b += text(124, 176, "MAC of A, B → port 1", 8.4, anchor="start", mono=True)
    b += text(124, 192, "MAC of C, D → port 2", 8.4, anchor="start", mono=True)
    b += note(12, 212, 336, ["A to B: same side, frame filtered (not forwarded).",
                             "A to C: forwarded to port 2. Layer 2 device; divides",
                             "collision domains, reduces traffic."])
    return svg(360, 272, b)


def router():
    b = title("Router: Connects Different Networks")
    b += f'<circle cx="180" cy="108" r="22" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.8"/>'
    b += text(180, 112, "Router", 9, weight="bold", color=ORANGE)
    nets = [(60, 70, "LAN 1", "192.168.1.0/24", "eth0"), (60, 156, "LAN 2", "10.0.0.0/8", "eth1"), (300, 108, "Internet", "ISP", "wan0")]
    for x, y, n, ip, port in nets:
        b += cable(180 + (-20 if x < 180 else 22), 108, x + (40 if x < 180 else -38), y, GREY, 1.8)
        b += f'<ellipse cx="{x}" cy="{y}" rx="44" ry="22" fill="{TEALF if n != "Internet" else BLUEF}" stroke="{TEAL if n != "Internet" else BLUE}" stroke-width="1.4"/>'
        b += text(x, y - 3, n, 9.4, weight="bold", color=TEAL if n != "Internet" else BLUE)
        b += text(x, y + 10, ip, 7.8, color=GREY)
    b += box(60, 190, 240, 76, "#fff", ORANGE, 4, 1.2)
    b += text(180, 205, "Routing table", 9, weight="bold", color=ORANGE)
    rows = [("192.168.1.0/24", "eth0"), ("10.0.0.0/8", "eth1"), ("0.0.0.0/0 (default)", "wan0")]
    for i, (a, c) in enumerate(rows):
        b += text(72, 222 + i * 15, a, 8.4, anchor="start", mono=True)
        b += text(288, 222 + i * 15, c, 8.4, anchor="end", mono=True, color=ORANGE)
    b += note(12, 276, 336, ["Layer 3 device: reads the destination IP address and",
                             "forwards the packet on the best path. Separates",
                             "broadcast domains; uses NAT, firewall, DHCP."])
    return svg(360, 336, b)


def ap():
    b = title("Wireless Access Point (Wi-Fi)")
    b += dev(60, 70, "Switch", 64, 24, TEALF, TEAL)
    b += cable(92, 70, 154, 98, GREY, 1.8)
    b += text(118, 76, "UTP", 8, color=GREY)
    b += box(158, 90, 44, 18, BLUEF, BLUE, 4, 1.5)
    b += line("M170,90 L166,74", BLUE, 1.6) + line("M190,90 L194,74", BLUE, 1.6)
    b += text(180, 124, "Access point", 9, weight="bold", color=BLUE)
    for r in (20, 32, 44):
        b += f'<path d="M{180 - r * 0.8},{99 + r * 0.6 + 30} A{r},{r} 0 0 0 {180 + r * 0.8},{99 + r * 0.6 + 30}" fill="none" stroke="{GREEN}" stroke-width="1.3"/>'
    for x, lab in ((60, "Laptop"), (180, "Phone"), (300, "Tablet")):
        b += pc(x, 200, lab, GREEN, GREENF)
    for r in (14, 22):
        for x in (60, 300):
            b += f'<path d="M{x - r * 0.7},{184 - r * 0.5} A{r},{r} 0 0 1 {x + r * 0.7},{184 - r * 0.5}" fill="none" stroke="{GREEN}" stroke-width="1.1"/>'
    b += note(12, 232, 336, ["Connects wireless devices to a wired LAN (IEEE 802.11).",
                             "Range about 30-100 m; 2.4 / 5 / 6 GHz bands.",
                             "Security: WPA2 / WPA3; identified by SSID."])
    return svg(360, 292, b)


def nic():
    b = title("Network Interface Card (NIC)")
    b += box(40, 50, 280, 120, "#C8E6C9", GREEN, 6, 1.6)
    b += box(40, 170, 160, 14, "#FFD54F", "#F9A825", 1, 1.2)
    for k in range(18):
        b += line(f"M{46 + k * 8.6},{172} L{46 + k * 8.6},{182}", "#F9A825", 2)
    b += text(120, 198, "Bus connector (PCIe / USB)", 8.6, weight="bold", color="#F57F17")
    b += box(320, 76, 26, 34, "#B0BEC5", "#455A64", 2, 1.4)
    b += box(326, 84, 14, 16, "#263238", "#263238", 1, 1)
    b += text(346, 126, "RJ-45", 8, anchor="end", weight="bold", color="#37474F")
    b += f'<circle cx="326" cy="70" r="3" fill="{GREEN}"/><circle cx="338" cy="70" r="3" fill="#FFB300"/>'
    b += text(316, 62, "LEDs", 7.6, anchor="end", color=GREY)
    parts = [(120, 92, 70, 40, "Controller", "(MAC chip)"), (222, 72, 52, 26, "ROM", "MAC addr"),
             (222, 116, 52, 26, "Buffer", "RAM"), (288, 92, 30, 40, "PHY", "")]
    for x, y, w, h, a, c in parts:
        b += box(x - w / 2, y - h / 2, w, h, "#263238", "#000", 3, 1)
        b += text(x, y - 1 if c else y + 4, a, 8.2, weight="bold", color="#fff")
        if c:
            b += text(x, y + 11, c, 7.4, color="#CFD8DC")
    b += text(60, 152, "transceiver / magnetics", 7.8, anchor="start", color="#1B5E20")
    b += note(12, 208, 336, ["Gives a computer a network connection and a unique",
                             "48-bit MAC address. Works at layers 1 and 2.",
                             "Types: Ethernet (wired, RJ-45) and Wi-Fi (wireless,",
                             "antenna); internal (PCIe) or external (USB)."])
    return svg(360, 282, b)


def dev_osi():
    b = title("Network Devices and OSI Layers")
    rows = [("7-4 Upper layers", "Gateway (protocol converter)", LC[0]),
            ("3 Network", "Router, Layer-3 switch", LC[4]),
            ("2 Data Link", "Switch, Bridge, NIC, Access point", LC[5]),
            ("1 Physical", "Hub, Repeater, cables, connectors", LC[6])]
    for i, (lay, devs, (f, s)) in enumerate(rows):
        y = 46 + i * 46
        b += box(12, y, 120, 38, f, s, 5, 1.4)
        b += text(72, y + 23, lay, 9.6, weight="bold", color=s)
        b += box(138, y, 210, 38, "#fff", s, 5, 1.2)
        b += text(243, y + 23, devs, 9, color=INK)
    b += note(12, 236, 336, ["Higher-layer devices also perform lower-layer jobs",
                             "(a router also works at layers 1 and 2).",
                             "Gateway can work at all seven layers."])
    return svg(360, 296, b)


DIAGRAMS = {"cn3_class": classify, "cn3_tp": twisted, "cn3_rj45": rj45, "cn3_coax": coax, "cn3_fiber": fiber,
            "cn3_fiber_modes": fiber_modes, "cn3_prop": prop, "cn3_spectrum": spectrum, "cn3_microwave": microwave,
            "cn3_satellite": satellite, "cn3_repeater": repeater, "cn3_hub_switch": hub_switch, "cn3_bridge": bridge,
            "cn3_router": router, "cn3_ap": ap, "cn3_nic": nic, "cn3_dev_osi": dev_osi}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
