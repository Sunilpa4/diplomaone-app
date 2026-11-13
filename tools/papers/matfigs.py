"""Diagrams for the Material Science and Technology papers (DI01005021).

Same rules as chemfigs.py: 360 px canvas, only rect/line/circle/path/text, and all
text is wrapped so nothing leaves its box or the canvas.
"""
from svgdiag import (svg, box, label, arrow, line, circle, path, notes, wrap,
                     PURPLE, BLUE, GREEN, ORANGE, RED, GREY,
                     PURPLE_F, BLUE_F, GREEN_F, ORANGE_F, RED_F, GREY_F)

CANVAS = 356


def tree(title, root, children, note_lines=(), child_fs=7.2, root_fs=9.0,
         child_h=44, title_gap=0):
    """Root box with a row of child boxes below it, joined by elbow connectors."""
    b = []
    y0 = 18 + title_gap
    b.append(label(180, y0, title, fs=9.4, anchor='middle', bold=True, color=PURPLE))
    ry = y0 + 14
    rw = min(210, max(120, int(len(root) * root_fs * 0.56) + 18))
    b.append(box(180 - rw / 2, ry, rw, 26, root, stroke=PURPLE, fill=PURPLE_F, fs=root_fs, bold=True))
    n = len(children)
    gap = 6
    cw = (CANVAS - 8 - gap * (n - 1)) / n
    cy = ry + 26 + 34
    centers = [4 + cw / 2 + i * (cw + gap) for i in range(n)]
    bus = ry + 26 + 17
    b.append(line(180, ry + 26, 180, bus, color=GREY))
    b.append(line(centers[0], bus, centers[-1], bus, color=GREY))
    for c, x in zip(children, centers):
        b.append(line(x, bus, x, cy, color=GREY))
        b.append(box(x - cw / 2, cy, cw, child_h, c, stroke=BLUE, fill=BLUE_F, fs=child_fs))
    bottom = cy + child_h + 12
    if note_lines:
        nn = notes(14, bottom + 4, *note_lines)
        b.append(nn)
        bottom = nn.bottom
    return svg(''.join(b), bottom, None)


def crystal_solids():
    return tree('Crystalline solids — classification',
                'Crystalline solid',
                [['Ionic', 'NaCl, CaF2'], ['Covalent', 'diamond, SiC'],
                 ['Molecular', 'ice, solid CO2'], ['Metallic', 'Cu, Fe, Al']],
                ['Particles are arranged in a fixed repeating lattice, so every crystal',
                 'has a sharp melting point and a definite cleavage plane.'],
                child_fs=7.0, child_h=42)


def solids_compare():
    b = []
    b.append(label(180, 18, 'Crystalline and amorphous solids', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(12, 30, 160, 30, 'Crystalline solid', stroke=BLUE, fill=BLUE_F, fs=8.6, bold=True))
    b.append(box(186, 30, 160, 30, 'Amorphous solid', stroke=ORANGE, fill=ORANGE_F, fs=8.6, bold=True))
    # ordered lattice on the left, random chain on the right
    for r in range(4):
        for c in range(5):
            b.append(circle(34 + c * 22, 84 + r * 20, 4, stroke=BLUE, fill=BLUE_F, width=1))
    import random
    random.seed(11)
    for r in range(4):
        for c in range(5):
            if random.random() < 0.15:
                continue
            b.append(circle(205 + c * 22 + random.randint(-5, 5),
                            84 + r * 20 + random.randint(-5, 5), 4,
                            stroke=ORANGE, fill=ORANGE_F, width=1))
    b.append(label(92, 178, 'long-range order', fs=7.4, anchor='middle', color=BLUE))
    b.append(label(266, 178, 'short-range order only', fs=7.4, anchor='middle', color=ORANGE))
    b.append(line(180, 34, 180, 176, color='#ddd6e2', width=1.2, dash='4 4'))
    n = notes(14, 196, 'Crystalline: sharp melting point, anisotropic, cleaves along planes.',
              'Amorphous: softens over a range, isotropic, breaks like glass.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def unit_cells():
    b = []
    b.append(label(180, 18, 'Crystal lattice and unit cell', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    specs = [('Simple cubic', '1 atom', 'corners only'),
             ('BCC', '2 atoms', 'corners + body centre'),
             ('FCC', '4 atoms', 'corners + face centres')]
    for i, (name, count, desc) in enumerate(specs):
        x = 10 + i * 117
        b.append(box(x, 28, 108, 22, name, stroke=BLUE, fill=BLUE_F, fs=8.2, bold=True))
        bx, by, sz, d = x + 26, 74, 50, 14
        b.append(f'<rect x="{bx}" y="{by + d}" width="{sz}" height="{sz}" fill="#FBFDFF" stroke="{BLUE}" stroke-width="1.1"/>')
        b.append(f'<rect x="{bx + d}" y="{by}" width="{sz}" height="{sz}" fill="none" stroke="{BLUE}" stroke-width="1.1"/>')
        for ax in (bx, bx + sz):
            b.append(line(ax, by + d, ax + d, by, color=BLUE))
        b.append(line(bx, by + d + sz, bx + d, by + sz, color=BLUE))
        b.append(line(bx + sz, by + d + sz, bx + sz + d, by + sz, color=BLUE))
        corners = [(bx + d, by), (bx + sz + d, by), (bx, by + d), (bx + sz, by + d),
                   (bx, by + d + sz), (bx + sz, by + d + sz),
                   (bx + d, by + sz), (bx + sz + d, by + sz)]
        for cx, cy in corners:
            b.append(circle(cx, cy, 3.2, stroke=PURPLE, fill=PURPLE_F, width=1))
        if i == 1:
            b.append(circle(bx + sz / 2 + d / 2, by + d / 2 + sz / 2, 3.4,
                            stroke=PURPLE, fill=PURPLE_F, width=1))
        if i == 2:
            for fx, fy in ((bx + sz / 2, by + d), (bx + sz / 2 + d, by),
                           (bx, by + d + sz / 2), (bx + sz, by + d + sz / 2),
                           (bx + d, by + sz), (bx + sz + d, by + sz),
                           (bx + sz / 2, by + d + sz), (bx + sz / 2 + d, by + sz)):
                b.append(circle(fx, fy, 3.2, stroke=PURPLE, fill=PURPLE_F, width=1))
        b.append(label(x + 54, 178, count + ' per cell', fs=7.4, anchor='middle', bold=True, color=PURPLE))
        b.append(label(x + 54, 190, desc, fs=6.6, anchor='middle', color=GREY))
    n = notes(14, 206, 'The lattice is the regular 3-D set of points; the unit cell is the smallest block',
              'that repeats to build the crystal. Corner atoms are shared by 8 cells, so the count is',
              '1, 2 and 4. Packing fraction: 52 % (SC), 68 % (BCC), 74 % (FCC).')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def testing_tree():
    return tree('Testing of materials',
                'Material testing',
                [['Destructive', 'tensile, hardness, impact'], ['Non-destructive', 'DPT, UT, RT, MPI']],
                ['Destructive tests spoil the sample, so a test piece is cut from the lot.',
                 'Non-destructive tests scan the finished part and keep it fit for service.'],
                child_h=46)


def rolling_forging():
    b = []
    b.append(label(180, 18, 'Rolling and forging', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(10, 28, 156, 22, 'Rolling — continuous', stroke=BLUE, fill=BLUE_F, fs=8.2, bold=True))
    b.append(box(190, 28, 156, 22, 'Forging — discrete', stroke=ORANGE, fill=ORANGE_F, fs=8.2, bold=True))
    # rolling: two rolls and a plate through them
    b.append(circle(64, 76, 17, stroke=BLUE, fill='#fff', width=1.4))
    b.append(circle(64, 122, 17, stroke=BLUE, fill='#fff', width=1.4))
    b.append(f'<rect x="14" y="90" width="52" height="12" fill="#D9E7F4" stroke="{BLUE}" stroke-width="1"/>')
    b.append(f'<rect x="64" y="93" width="94" height="7" fill="#D9E7F4" stroke="{BLUE}" stroke-width="1"/>')
    b.append(arrow(120, 78, 152, 78, color=BLUE))
    b.append(label(64, 72, 'rolls', fs=6.8, anchor='middle', color=GREY))
    b.append(label(88, 152, 'slab in, thin strip out', fs=7.2, anchor='middle', color=GREY))
    # forging: hammer and anvil
    b.append(f'<rect x="226" y="56" width="60" height="22" fill="{ORANGE_F}" stroke="{ORANGE}" stroke-width="1.2"/>')
    b.append(label(256, 71, 'hammer', fs=7.4, anchor='middle', color=ORANGE))
    b.append(arrow(256, 82, 256, 98, color=ORANGE))
    b.append(f'<rect x="216" y="98" width="80" height="16" rx="4" fill="#EFE6DA" stroke="{ORANGE}" stroke-width="1.2"/>')
    b.append(label(256, 110, 'hot billet', fs=6.8, anchor='middle', color=ORANGE))
    b.append(f'<rect x="232" y="126" width="48" height="12" fill="{GREY_F}" stroke="{GREY}" stroke-width="1"/>')
    b.append(label(256, 152, 'anvil', fs=7.2, anchor='middle', color=GREY))
    n = notes(14, 166, 'Rolling pushes the hot slab between rotating rolls: long, uniform sections.',
              'Forging squeezes the hot billet between a hammer and an anvil: stronger, grain follows shape.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def dye_penetrant():
    b = []
    b.append(label(180, 18, 'Dye penetration test (DPT)', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    steps = ['1 Clean surface', '2 Apply red dye', '3 Dwell 10 min', '4 Remove excess',
             '5 Apply developer', '6 Read indication']
    for i, s in enumerate(steps):
        row, col = divmod(i, 2)
        x = 14 + col * 176
        y = 34 + row * 46
        b.append(box(x, y, 166, 34, s, stroke=BLUE, fill=BLUE_F, fs=7.8))
        if col == 0:
            b.append(arrow(x + 166, y + 17, x + 176, y + 17, color=GREY))
        elif i < 5:
            b.append(arrow(x + 83, y + 34, x + 83 - 176 + 176, y + 34 + 12, color=GREY, head=0))
    # zig-zag down arrows between the rows
    b.append(arrow(97, 68, 97, 80, color=GREY))
    b.append(arrow(273, 114, 273, 126, color=GREY))
    # crack close-up
    b.append(f'<rect x="14" y="192" width="150" height="62" rx="5" fill="#FDFDFD" stroke="{GREY}" stroke-width="1.1"/>')
    b.append(path('M30 236 L60 214 L70 224 L96 206 L120 228 L146 210', stroke=GREY, width=3))
    b.append(path('M60 214 L74 226', stroke=RED, width=2.4))
    b.append(label(89, 202, 'surface-breaking crack', fs=7, anchor='middle', color=GREY))
    b.append(box(184, 196, 162, 54, ['Red dye is trapped in the crack;', 'developer draws it out as a bright line'],
                 stroke=RED, fill=RED_F, fs=7.6))
    n = notes(14, 268, 'Only surface defects are found, and the surface must be clean and dry before the test.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def hydrostatic():
    b = []
    b.append(label(180, 18, 'Hydrostatic test of a vessel', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # vessel body
    b.append(f'<rect x="96" y="66" width="130" height="92" rx="26" fill="#F7F9FC" stroke="{BLUE}" stroke-width="1.6"/>')
    b.append(label(161, 116, 'vessel filled', fs=7.8, anchor='middle', color=BLUE))
    b.append(label(161, 128, 'with water', fs=7.8, anchor='middle', color=BLUE))
    b.append(f'<rect x="88" y="150" width="146" height="7" fill="#DCE9F5" stroke="{BLUE}" stroke-width="1"/>')
    # pressure gauge
    b.append(circle(161, 46, 15, stroke=ORANGE, fill='#fff', width=1.4))
    b.append(line(161, 46, 169, 38, color=ORANGE, width=1.6))
    b.append(label(186, 44, 'pressure gauge', fs=7.2, color=ORANGE))
    b.append(line(161, 61, 161, 66, color=ORANGE))
    # pump to the left
    b.append(box(14, 108, 62, 30, 'hand pump', stroke=GREY, fill=GREY_F, fs=7.6))
    b.append(arrow(76, 123, 96, 130, color=GREY))
    b.append(label(30, 100, 'water in', fs=6.8, color=GREY))
    # valve on top right
    b.append(f'<rect x="216" y="60" width="12" height="10" fill="{GREY_F}" stroke="{GREY}" stroke-width="1"/>')
    b.append(line(222, 50, 222, 60, color=GREY, width=1.6))
    b.append(label(232, 54, 'air vent', fs=7, color=GREY))
    # gauge glass level
    b.append(f'<rect x="248" y="84" width="9" height="70" fill="#EAF3FA" stroke="{GREY}" stroke-width="1"/>')
    b.append(line(248, 104, 257, 104, color=BLUE, width=1.4))
    b.append(label(262, 100, 'level', fs=6.8, color=GREY))
    b.append(label(262, 110, 'glass', fs=6.8, color=GREY))
    n = notes(14, 172, 'Water is pumped in until the pressure reaches 1.5 times the design pressure',
              'and held for 30 minutes. Water is almost incompressible, so a burst releases',
              'very little energy; any leak, weep or permanent bulge fails the test.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def insulation_wall():
    b = []
    b.append(label(180, 18, 'Thermal insulation on a hot wall', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(f'<rect x="40" y="40" width="34" height="140" fill="#E8D6C6" stroke="{ORANGE}" stroke-width="1.2"/>')
    b.append(label(57, 116, 'wall', fs=7.4, anchor='middle', color=ORANGE))
    b.append(f'<rect x="74" y="40" width="70" height="140" fill="{PURPLE_F}" stroke="{PURPLE}" stroke-width="1.3"/>')
    b.append(label(109, 110, 'insulation', fs=7.4, anchor='middle', color=PURPLE))
    b.append(label(109, 122, 'mineral wool', fs=7, anchor='middle', color=PURPLE))
    b.append(f'<rect x="144" y="40" width="22" height="140" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(label(178, 116, 'steel', fs=7, color=GREY))
    b.append(label(178, 126, 'cladding', fs=7, color=GREY))
    b.append(label(57, 34, 'T hot', fs=7.6, anchor='middle', color=RED))
    b.append(label(250, 34, 'T cold', fs=7.6, anchor='middle', color=BLUE))
    for y in (62, 86, 156, 180):
        b.append(arrow(196, y, 296, y, color=RED, head=4))
    b.append(label(246, 190, 'heat flow q', fs=7.2, anchor='middle', color=RED))
    n = notes(14, 204, 'q = k·A·(T hot − T cold) / t. A low-conductivity, dry, closed-cell layer',
              'cuts q; if the insulation gets wet its k rises and the saving is lost.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def fibre_tree():
    return tree('Fibres — classification',
                'Fibre',
                [['Natural', 'cotton, wool, silk'], ['Synthetic', 'nylon, PET, acrylic']],
                ['Natural fibres come from plants, animals or minerals.',
                 'Synthetic fibres are spun from polymers; they are stronger but melt and hold static.'],
                child_h=46)


def paint_layers():
    b = []
    b.append(label(180, 18, 'Paint system — layer by layer', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    layers = [('Top coat', 'colour + gloss, weather resistance', GREEN),
              ('Under coat', 'fills, gives opacity, bonds to primer', BLUE),
              ('Primer', 'adhesion + rust inhibition', ORANGE),
              ('Metal surface', 'cleaned, degreased, dry', GREY)]
    y = 34
    for i, (name, why, col) in enumerate(layers):
        h = 40 if i < 3 else 26
        b.append(f'<rect x="24" y="{y}" width="{176}" height="{h}" fill="#fff" stroke="{col}" stroke-width="1.3"/>')
        b.append(label(112, y + h / 2 + 3, name, fs=8.2, anchor='middle', bold=True, color=col))
        b.append(label(208, y + h / 2 + 2, why, fs=7.2, color=GREY))
        y += h
    b.append(label(112, y + 18, 'each coat dries before the next is applied', fs=7, anchor='middle', color=GREY))
    n = notes(14, y + 36, 'Solvent, pigment, binder and additives are the four ingredients of a paint.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def materials_tree():
    return tree('Engineering materials',
                'Materials',
                [['Metals', 'ferrous / non-ferrous'], ['Ceramics', 'glass, porcelain'],
                 ['Polymers', 'plastic, rubber'], ['Composites', 'FRP, cermet']],
                ['Properties come from structure: metallic bonding gives ductility, ionic and',
                 'covalent bonding gives hardness and brittleness, long chains give flexibility.'],
                child_fs=6.8, child_h=44)
