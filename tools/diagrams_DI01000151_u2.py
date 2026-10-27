"""SVG diagrams for Basics of Electronics - Unit 2 (Semiconductors). Mobile-first, no markers/CSS."""
import os, math, sys
sys.path.insert(0, os.path.dirname(__file__))
from diagrams_DI01000151_u1 import svg, text, box, arrow, arrowhead, P, INK

OUT = os.path.join(os.path.dirname(__file__), "..", "content", "computer", "sem1", "DI01000151", "diagrams")
RED, BLUE, GREEN = "#C62828", "#1565C0", "#2E7D32"


def electron(x, y, color=BLUE, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'


def hole(x, y, r=5.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" stroke="{RED}" stroke-width="2"/>'

# ------------------------------------------------------------ 1. Bohr model of silicon


def bohr_si():
    cx, cy = 180, 165
    b = text(180, 20, "Silicon Atom (Z = 14)", 15, weight="bold", color=P)
    radii = [42, 78, 114]
    counts = [2, 8, 4]
    names = ["K (2)", "L (8)", "M (4)"]
    for r, n, nm in zip(radii, counts, names):
        col = RED if n == 4 else "#9E8DB5"
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{2.2 if n==4 else 1.5}" stroke-dasharray="{"" if n==4 else "4 3"}"/>'
        for i in range(n):
            a = 2 * math.pi * i / n - math.pi / 2 + (0.4 if n == 4 else 0)
            b += electron(cx + r * math.cos(a), cy + r * math.sin(a), RED if n == 4 else BLUE, 6 if n == 4 else 5)
        b += text(cx + r * 0.72 + 6, cy + r * 0.72 + 8, nm, 11, color="#555", anchor="start")
    b += f'<circle cx="{cx}" cy="{cy}" r="24" fill="#EADDF7" stroke="{P}" stroke-width="2"/>'
    b += text(cx, cy, "14 p\n14 n", 10.5, weight="bold", color=P)
    b += electron(40, 312, BLUE) + text(52, 312, "Inner electrons", 11, anchor="start")
    b += electron(190, 312, RED, 6) + text(202, 312, "Valence electrons (4)", 11, anchor="start")
    return svg(360, 330, b)

# ------------------------------------------------------------ 2. tri / tetra / penta valent


def valence_atoms():
    b = text(180, 20, "Valence Electrons", 15, weight="bold", color=P)
    data = [(62, "B", "Boron", 3, "Trivalent", "#FFF3E0"), (180, "Si", "Silicon", 4, "Tetravalent", "#EADDF7"),
            (298, "P", "Phosphorus", 5, "Pentavalent", "#E3F2FD")]
    for x, sym, name, n, kind, fill in data:
        y = 95
        b += f'<circle cx="{x}" cy="{y}" r="44" fill="none" stroke="{RED}" stroke-width="1.8"/>'
        b += f'<circle cx="{x}" cy="{y}" r="22" fill="{fill}" stroke="{P}" stroke-width="2"/>'
        b += text(x, y, sym, 15, weight="bold", color=P)
        for i in range(n):
            a = 2 * math.pi * i / n - math.pi / 2
            b += electron(x + 44 * math.cos(a), y + 44 * math.sin(a), RED, 6)
        b += text(x, 160, name, 12, weight="bold")
        b += text(x, 178, kind, 12, color=P, weight="bold")
        b += text(x, 196, f"{n} valence e⁻", 11, color="#555")
    b += '<rect x="10" y="215" width="340" height="62" rx="10" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 233, "Trivalent → acceptor impurity → P-type", 11.5, color="#9A5B00", weight="bold")
    b += text(180, 255, "Pentavalent → donor impurity → N-type", 11.5, color=BLUE, weight="bold")
    return svg(360, 290, b)

# ------------------------------------------------------------ 3. energy bands


def energy_bands():
    b = text(180, 18, "Energy Band Diagrams", 15, weight="bold", color=P)
    cols = [(62, "Insulator", "Eg > 5 eV", 60), (180, "Semiconductor", "Eg ≈ 1 eV", 26), (298, "Conductor", "Overlap", -14)]
    top = 50
    for x, name, eg, gap in cols:
        w = 96
        cb_h, vb_h = 48, 48
        if gap >= 0:
            cb_y = top
            vb_y = top + cb_h + gap
        else:
            cb_y = top + 20
            vb_y = cb_y + cb_h + gap
        b += f'<rect x="{x-w/2}" y="{vb_y}" width="{w}" height="{vb_h}" fill="#C5CAE9" stroke="#3949AB" stroke-width="1.5" opacity="0.9"/>'
        b += f'<rect x="{x-w/2}" y="{cb_y}" width="{w}" height="{cb_h}" fill="#FFCDD2" stroke="{RED}" stroke-width="1.5" opacity="0.85"/>'
        b += text(x, cb_y + 16, "Conduction", 10, weight="bold", color=RED) + text(x, cb_y + 30, "Band", 10, weight="bold", color=RED)
        b += text(x, vb_y + vb_h - 26, "Valence", 10, weight="bold", color="#283593") + text(x, vb_y + vb_h - 12, "Band", 10, weight="bold", color="#283593")
        if gap > 0:
            b += f'<line x1="{x+w/2-10}" y1="{cb_y+cb_h}" x2="{x+w/2-10}" y2="{vb_y}" stroke="{INK}" stroke-width="1.3"/>'
            b += arrowhead(x + w / 2 - 10, cb_y + cb_h, -90, 6) + arrowhead(x + w / 2 - 10, vb_y, 90, 6)
            b += text(x - 6, cb_y + cb_h + gap / 2, "Eg", 11, weight="bold")
        b += text(x, 222, name, 12.5, weight="bold")
        b += text(x, 240, eg, 11.5, color=P, weight="bold")
    b += f'<line x1="12" y1="200" x2="12" y2="50" stroke="{INK}" stroke-width="1.3"/>' + arrowhead(12, 48, -90, 7)
    b += text(22, 44, "Energy", 10, anchor="start", color="#555")
    b += '<rect x="10" y="256" width="340" height="58" rx="10" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 274, "Si: Eg = 1.1 eV   |   Ge: Eg = 0.7 eV", 12, weight="bold")
    b += text(180, 296, "Eg = Forbidden energy gap", 11, color="#555")
    return svg(360, 324, b)

# ------------------------------------------------------------ 4-7. crystal lattices


def lattice(title, centre="Si", centre_fill="#EADDF7", mode="pure", caption=""):
    """3x3 lattice, spacing 100. mode: pure | intrinsic | ntype | ptype"""
    xs = [80, 180, 280]
    ys = [80, 180, 280]
    b = text(180, 22, title, 15, weight="bold", color=P)
    bonds = []
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if i < 2:
                bonds.append(((x, y), (xs[i + 1], y)))
            if j < 2:
                bonds.append(((x, y), (x, ys[j + 1])))
    # dangling bonds to edge
    for x in xs:
        bonds.append(((x, ys[0]), (x, ys[0] - 45)))
        bonds.append(((x, ys[2]), (x, ys[2] + 45)))
    for y in ys:
        bonds.append(((xs[0], y), (xs[0] - 55, y)))
        bonds.append(((xs[2], y), (xs[2] + 55, y)))
    body = ""
    for (x1, y1), (x2, y2) in bonds:
        body += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#B9A7D6" stroke-width="2"/>'
    # electrons on bonds
    special_bond = ((180, 180), (280, 180))  # bond to the right of centre
    for (x1, y1), (x2, y2) in bonds:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if (x2 - x1, y2 - y1) in [(0, -45), (0, 45), (-55, 0), (55, 0)]:
            mx, my = x1 + (x2 - x1) * 0.62, y1 + (y2 - y1) * 0.62
        horiz = y1 == y2
        o = 6
        p1 = (mx, my - o) if horiz else (mx - o, my)
        p2 = (mx, my + o) if horiz else (mx + o, my)
        is_special = ((x1, y1), (x2, y2)) == special_bond
        if is_special and mode == "intrinsic":
            body += electron(*p1) + hole(*p2)
        elif is_special and mode == "ptype":
            body += electron(*p1) + hole(*p2)
        else:
            body += electron(*p1) + electron(*p2)
    # atoms
    for x in xs:
        for y in ys:
            c = (x == 180 and y == 180)
            lab = centre if c else "Si"
            fill = centre_fill if c else "#F3ECFA"
            body += f'<circle cx="{x}" cy="{y}" r="22" fill="{fill}" stroke="{P}" stroke-width="2"/>'
            body += text(x, y, lab, 13 if len(lab) < 3 else 11, weight="bold", color=P)
            if c and mode in ("ntype", "ptype"):
                body += text(x + 17, y - 17, "+" if mode == "ntype" else "−", 13, weight="bold",
                             color=RED if mode == "ntype" else BLUE)
    b += body
    if mode == "intrinsic":
        b += electron(250, 132, BLUE, 6)
        b += f'<path d="M232 174 Q238 150 246 138" fill="none" stroke="{GREEN}" stroke-width="1.6" stroke-dasharray="4 3"/>'
        b += text(262, 120, "Free electron", 11, anchor="start", color=BLUE, weight="bold")
        b += text(232, 214, "Hole", 11, color=RED, weight="bold")
    if mode == "ntype":
        b += electron(212, 214, RED, 6.5)
        b += text(250, 236, "Free\nelectron", 10.5, color=RED, weight="bold")
    if mode == "ptype":
        b += text(232, 214, "Hole", 11, color=RED, weight="bold")
    # legend
    ly = 345
    b += electron(28, ly) + text(38, ly, "Electron", 11, anchor="start")
    if mode in ("intrinsic", "ptype"):
        b += hole(118, ly) + text(128, ly, "Hole", 11, anchor="start")
    if caption:
        b += f'<rect x="10" y="{ly+16}" width="340" height="30" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
        b += text(180, ly + 31, caption, 11.5, weight="bold", color=P)
    return svg(360, ly + (52 if caption else 16), b)


DIAGRAMS = {
    "u2_bohr_silicon": bohr_si,
    "u2_valence_atoms": valence_atoms,
    "u2_energy_bands": energy_bands,
    "u2_covalent_si": lambda: lattice("Covalent Bonds in Silicon Crystal", caption="Each Si atom shares 4 electrons → 8 in outer shell"),
    "u2_intrinsic": lambda: lattice("Intrinsic Semiconductor (Room Temp.)", mode="intrinsic",
                                    caption="Broken bond → one free electron + one hole"),
    "u2_ntype": lambda: lattice("N-type Semiconductor", centre="P", centre_fill="#E3F2FD", mode="ntype",
                                caption="Pentavalent donor → extra free electron"),
    "u2_ptype": lambda: lattice("P-type Semiconductor", centre="B", centre_fill="#FFF3E0", mode="ptype",
                                caption="Trivalent acceptor → one hole created"),
}

if __name__ == "__main__":
    for name, fn in DIAGRAMS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(DIAGRAMS))
