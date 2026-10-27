"""Generates mobile-friendly SVG diagrams for Basics of Electronics - Unit 1.
No <marker> / CSS used, so files render in flutter_svg as well as browsers."""
import os, math

OUT = os.path.join(os.path.dirname(__file__), "..", "content", "computer", "sem1", "DI01000151", "diagrams")
P = "#7B2CD9"      # brand purple
INK = "#222"
FONT = 'font-family="Arial, Helvetica, sans-serif"'


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT}>'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>')


def text(x, y, s, size=12, anchor="middle", color=INK, weight="normal"):
    lines = s.split("\n")
    out = ""
    for i, ln in enumerate(lines):
        dy = (i - (len(lines) - 1) / 2) * (size + 2)
        out += (f'<text x="{x}" y="{y + dy + size * 0.35:.1f}" font-size="{size}" text-anchor="{anchor}" '
                f'fill="{color}" font-weight="{weight}">{ln}</text>')
    return out


def arrowhead(x, y, ang_deg, size=7, color=INK):
    a = math.radians(ang_deg)
    p1 = (x - size * math.cos(a) + size * 0.5 * math.sin(a), y - size * math.sin(a) - size * 0.5 * math.cos(a))
    p2 = (x - size * math.cos(a) - size * 0.5 * math.sin(a), y - size * math.sin(a) + size * 0.5 * math.cos(a))
    return f'<polygon points="{x:.1f},{y:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>'


def arrow(x1, y1, x2, y2, color=INK, w=2):
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>'
            + arrowhead(x2, y2, ang, color=color))


def box(cx, cy, w, h, label, fill="#EADDF7", stroke=P, size=11, weight="normal", color=INK):
    return (f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="7" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.5"/>' + text(cx, cy, label, size, color=color, weight=weight))


G = f'<g fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'

# ---------------------------------------------------------------- 1. symbols


def resistor(x, y):
    d = f"M{x-45} {y} H{x-30}"
    xs = x - 30
    for i in range(6):
        d += f" L{xs + 5 + i * 10} {y + (-9 if i % 2 == 0 else 9)}"
    d += f" L{x+30} {y} H{x+45}"
    return f'<path d="{d}"/>'


def capacitor(x, y, polar=False):
    s = f'<path d="M{x-45} {y} H{x-6} M{x-6} {y-16} V{y+16} M{x+6} {y} H{x+45}"/>'
    if polar:
        s += f'<path d="M{x+10} {y-16} Q{x+2} {y} {x+10} {y+16}"/>'
        s += f'<path d="M{x-18} {y-16} h8 M{x-14} {y-20} v8" stroke-width="1.6"/>'
    else:
        s += f'<path d="M{x+6} {y-16} V{y+16}"/>'
    return s


def inductor(x, y, core=False):
    d = f"M{x-45} {y} H{x-40}"
    for _ in range(4):
        d += " a10 10 0 0 1 20 0"
    d += f" H{x+45}"
    s = f'<path d="{d}"/>'
    if core:
        s += f'<path d="M{x-40} {y-16} H{x+40} M{x-40} {y-21} H{x+40}"/>'
    return s


def diag_arrow(x, y):
    return (f'<line x1="{x-24}" y1="{y+20}" x2="{x+22}" y2="{y-18}" stroke="{P}" stroke-width="2"/>'
            + arrowhead(x + 24, y - 20, -40, 8, P))


def symbols():
    cols = [95, 265]
    rows = [55, 155, 255, 355]
    items = [
        ("Fixed Resistor", lambda x, y: resistor(x, y)),
        ("Variable Resistor", lambda x, y: resistor(x, y) + "</g>" + diag_arrow(x, y) + G),
        ("Potentiometer", lambda x, y: resistor(x, y) + f'<path d="M{x} {y-34} V{y-14}"/>' + "</g>"
            + arrowhead(x, y - 11, 90, 8) + G),
        ("Capacitor (Non-polar)", lambda x, y: capacitor(x, y)),
        ("Electrolytic Capacitor", lambda x, y: capacitor(x, y, True)),
        ("Variable Capacitor", lambda x, y: capacitor(x, y) + "</g>" + diag_arrow(x, y) + G),
        ("Inductor (Air core)", lambda x, y: inductor(x, y)),
        ("Iron-core Inductor", lambda x, y: inductor(x, y, True)),
    ]
    body = ""
    for i, (label, fn) in enumerate(items):
        x, y = cols[i % 2], rows[i // 2]
        body += f'<rect x="{x-80}" y="{y-40}" width="160" height="90" rx="10" fill="#F7F2FD" stroke="#E0D2F3"/>'
        body += G + fn(x, y) + "</g>" + text(x, y + 34, label, 12, weight="bold")
    return svg(360, 405, body)

# ---------------------------------------------------------------- 2. resistor tree


def resistor_tree():
    b = box(180, 28, 150, 34, "RESISTORS", fill=P, stroke=P, size=13, weight="bold", color="#fff")
    heads = [(62, "Fixed"), (180, "Variable"), (298, "Special\n(Non-linear)")]
    leaves = [
        ["Carbon\nComposition", "Carbon Film", "Metal Film", "Wire Wound"],
        ["Potentiometer", "Rheostat", "Preset /\nTrimmer"],
        ["LDR", "Thermistor\n(NTC / PTC)", "Varistor\n(VDR)"],
    ]
    b += f'<path d="M180 45 V70 M62 70 H298 M62 70 V88 M180 70 V88 M298 70 V88" stroke="{P}" stroke-width="1.6" fill="none"/>'
    for (x, h), lv in zip(heads, leaves):
        b += box(x, 108, 108, 40, h, fill="#D9C2F5", size=12, weight="bold")
        for j, leaf in enumerate(lv):
            y = 175 + j * 56
            b += f'<path d="M{x} {128 + (0 if j == 0 else 0)} V{y-20}" stroke="{P}" stroke-width="1.4" fill="none"/>' if j == 0 else ""
            if j > 0:
                b += f'<path d="M{x} {y-56+20} V{y-20}" stroke="{P}" stroke-width="1.4" fill="none"/>'
            b += box(x, y, 108, 40, leaf, fill="#ffffff", size=11)
    return svg(360, 375, b)

# ---------------------------------------------------------------- 3. colour code


def colour_code():
    b = f'<path d="M10 70 H80 M280 70 H350" stroke="#777" stroke-width="4" stroke-linecap="round"/>'
    b += '<rect x="80" y="42" width="200" height="56" rx="24" fill="#E8C997" stroke="#9C7A45" stroke-width="2"/>'
    bands = [(110, "#F5D90A", "Yellow", "4", "1st digit"), (140, "#7B1FA2", "Violet", "7", "2nd digit"),
             (170, "#D32F2F", "Red", "× 10²", "Multiplier"), (240, "#C9A227", "Gold", "± 5%", "Tolerance")]
    for x, c, *_ in bands:
        b += f'<rect x="{x}" y="42" width="14" height="56" fill="{c}"/>'
    b += text(180, 22, "4-Band Resistor Colour Code", 14, weight="bold", color=P)
    for i, (x, c, name, val, role) in enumerate(bands):
        y = 132 + i * 26
        b += f'<rect x="28" y="{y-9}" width="18" height="18" rx="3" fill="{c}" stroke="#555"/>'
        b += text(56, y, f"Band {i+1}: {name}", 12, anchor="start")
        b += text(200, y, role, 12, anchor="start", color="#555")
        b += text(330, y, val, 13, anchor="end", weight="bold", color=P)
    b += '<rect x="20" y="232" width="320" height="58" rx="10" fill="#EADDF7"/>'
    b += text(180, 250, "R = 47 × 10² Ω = 4700 Ω = 4.7 kΩ ± 5%", 13, weight="bold")
    b += text(180, 274, "Range: 4.465 kΩ to 4.935 kΩ", 12, color="#444")
    return svg(360, 300, b)

# ---------------------------------------------------------------- 4. parallel plate capacitor


def parallel_plate():
    b = '<rect x="104" y="40" width="152" height="150" fill="#EFE6FA"/>'
    b += text(180, 105, "Dielectric", 13, weight="bold", color=P)
    b += text(180, 123, "(εr)", 12, color=P)
    b += '<rect x="90" y="40" width="14" height="150" fill="#9E9E9E" stroke="#555"/>'
    b += '<rect x="256" y="40" width="14" height="150" fill="#9E9E9E" stroke="#555"/>'
    for i in range(6):
        y = 55 + i * 24
        b += text(116, y, "+", 15, weight="bold", color="#C62828")
        b += text(244, y, "−", 15, weight="bold", color="#1565C0")
    b += text(97, 28, "+Q", 13, weight="bold", color="#C62828")
    b += text(263, 28, "−Q", 13, weight="bold", color="#1565C0")
    b += text(48, 60, "Plate 1\n(Area A)", 11, color="#444")
    b += text(312, 60, "Plate 2\n(Area A)", 11, color="#444")
    # distance d
    b += f'<line x1="106" y1="205" x2="254" y2="205" stroke="{INK}" stroke-width="1.5"/>'
    b += arrowhead(106, 205, 180) + arrowhead(254, 205, 0) + text(180, 196, "d", 13, weight="bold")
    # circuit
    b += G + '<path d="M90 115 H40 V245 H168 M184 245 H320 V115 H270"/>'
    b += '<path d="M168 230 V260" stroke-width="2.5"/><path d="M184 237 V253" stroke-width="4"/></g>'
    b += text(160, 225, "+", 12, weight="bold") + text(194, 228, "−", 12, weight="bold")
    b += text(176, 278, "Battery (V)", 11, color="#444")
    return svg(360, 290, b)

# ---------------------------------------------------------------- 5. capacitor tree


def capacitor_tree():
    line = lambda d: f'<path d="{d}" stroke="{P}" stroke-width="1.5" fill="none"/>'
    b = box(180, 26, 150, 32, "CAPACITORS", fill=P, stroke=P, size=13, weight="bold", color="#fff")
    b += line("M180 42 V60 M110 60 H295 M110 60 V78 M295 60 V78")
    b += box(110, 96, 110, 34, "Fixed", fill="#D9C2F5", size=12, weight="bold")
    b += box(295, 96, 100, 34, "Variable", fill="#D9C2F5", size=12, weight="bold")
    b += line("M110 113 V128 M55 128 H165 M55 128 V146 M165 128 V146")
    b += box(55, 164, 100, 34, "Polarized", fill="#EADDF7", size=11, weight="bold")
    b += box(165, 164, 100, 34, "Non-polarized", fill="#EADDF7", size=11, weight="bold")
    b += line("M295 113 V146") + box(295, 164, 100, 34, "Gang\nCapacitor", fill="#fff", size=11)
    b += line("M295 181 V200") + box(295, 218, 100, 34, "Trimmer\nCapacitor", fill="#fff", size=11)
    pol = ["Aluminium\nElectrolytic", "Tantalum\nElectrolytic"]
    non = ["Ceramic", "Mica", "Paper", "Plastic Film\n(Polyester)"]
    for j, s in enumerate(pol):
        y = 218 + j * 52
        b += line(f"M55 {y-52+17} V{y-17}") + box(55, y, 100, 36, s, fill="#fff", size=11)
    for j, s in enumerate(non):
        y = 218 + j * 52
        b += line(f"M165 {y-52+17} V{y-17}") + box(165, y, 100, 36, s, fill="#fff", size=11)
    return svg(360, 395, b)

# ---------------------------------------------------------------- 6. mutual induction


def mutual():
    b = ('<path fill="#D6CDE3" fill-rule="evenodd" stroke="#8E7FA8" stroke-width="1.5" '
         'd="M110 40 H250 V200 H110 Z M140 70 V170 H220 V70 Z"/>')
    b += ('<rect x="125" y="55" width="110" height="130" rx="6" fill="none" stroke="#2E7D32" '
          'stroke-width="1.5" stroke-dasharray="6 4"/>')
    b += arrowhead(185, 55, 0, 8, "#2E7D32") + arrowhead(175, 185, 180, 8, "#2E7D32")
    b += text(180, 30, "Mutual flux Φ", 12, weight="bold", color="#2E7D32")
    coil = ""
    for i in range(7):
        y = 80 + i * 13
        coil += f'<path d="M102 {y} L148 {y+6}" stroke="#C62828" stroke-width="3"/>'
        coil += f'<path d="M212 {y} L258 {y+6}" stroke="#1565C0" stroke-width="3"/>'
    b += coil
    b += G + '<path d="M102 80 H45 V104 M45 140 V164 H102 M258 80 H315 V104 M315 140 V164 H258"/>'
    b += '<circle cx="45" cy="122" r="18"/><path d="M33 122 q6 -12 12 0 t12 0"/>'
    b += '<circle cx="315" cy="122" r="18"/><path d="M302 109 L328 135 M328 109 L302 135"/></g>'
    b += text(45, 184, "AC source", 11) + text(72, 72, "i₁", 13, weight="bold", color="#C62828")
    b += text(350, 122, "e₂", 13, weight="bold", color="#1565C0")
    b += text(315, 184, "Lamp", 11)
    b += text(110, 222, "Primary coil (L₁)", 12, weight="bold", color="#C62828")
    b += text(262, 222, "Secondary coil (L₂)", 12, weight="bold", color="#1565C0")
    b += text(180, 120, "Iron\ncore", 11, color="#555")
    return svg(360, 240, b)

# ---------------------------------------------------------------- 7. DC power supply block diagram


def wave(kind, x, y, w=80, a=14):
    pts = []
    n = 60
    for i in range(n + 1):
        t = i / n
        X = x + t * w
        s = math.sin(t * 4 * math.pi)
        if kind == "big":
            Y = y - a * s
        elif kind == "small":
            Y = y - a * 0.5 * s
        elif kind == "fw":
            Y = y + a * 0.5 - a * abs(s)
        elif kind == "ripple":
            Y = y - a * 0.35 - 2.5 * abs(math.sin(t * 4 * math.pi + 1.2))
        else:
            Y = y - a * 0.4
        pts.append(f"{X:.1f},{Y:.1f}")
    axis = f'<line x1="{x}" y1="{y + (a*0.5 if kind in ("fw","ripple","dc") else 0)}" x2="{x+w}" y2="{y + (a*0.5 if kind in ("fw","ripple","dc") else 0)}" stroke="#bbb" stroke-width="1"/>'
    return axis + f'<polyline points="{" ".join(pts)}" fill="none" stroke="{P}" stroke-width="2"/>'


def dc_supply():
    stages = [("AC Mains\n230 V, 50 Hz", "#FFF3E0", "#EF6C00"), ("Step-down\nTransformer", "#EADDF7", P),
              ("Rectifier", "#EADDF7", P), ("Filter", "#EADDF7", P), ("Voltage\nRegulator", "#EADDF7", P),
              ("Load\n(Regulated DC)", "#E8F5E9", "#2E7D32")]
    waves = [("big", "230 V AC"), ("small", "Low-voltage AC"), ("fw", "Pulsating DC"),
             ("ripple", "DC with ripple"), ("dc", "Pure, steady DC")]
    b = ""
    for i, (lab, fill, st) in enumerate(stages):
        y = 35 + i * 100
        b += box(115, y, 180, 50, lab, fill=fill, stroke=st, size=13, weight="bold")
        if i < 5:
            b += arrow(115, y + 25, 115, y + 73, INK, 2)
            kind, cap = waves[i]
            b += wave(kind, 245, y + 50, 90, 16)
            b += text(290, y + 78, cap, 10, color="#555")
    return svg(360, 580, b)


DIAGRAMS = {
    "u1_symbols": symbols,
    "u1_resistor_tree": resistor_tree,
    "u1_colour_code": colour_code,
    "u1_parallel_plate": parallel_plate,
    "u1_capacitor_tree": capacitor_tree,
    "u1_mutual_induction": mutual,
    "u1_dc_power_supply": dc_supply,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in DIAGRAMS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(DIAGRAMS), "diagrams to", os.path.abspath(OUT))
