"""Extra Material Science diagrams for the DI01005021 Winter-2025 paper.

Every builder returns a standalone SVG string on the 360 px canvas used by the reader.
"""
from svgdiag import (svg, box, label, arrow, line, circle, path, notes, wrap,
                     PURPLE, BLUE, GREEN, ORANGE, RED, GREY,
                     PURPLE_F, BLUE_F, GREEN_F, ORANGE_F, RED_F, GREY_F)
CANVAS = 360


def tree(title, root, children, note_lines=(), child_fs=7.2, root_fs=9.0,
         child_h=44, max_w=118):
    """Root box with a row of child boxes below it (child width capped so 2 boxes do not sprawl)."""
    b = []
    y0 = 18
    b.append(label(180, y0, title, fs=9.4, anchor='middle', bold=True, color=PURPLE))
    ry = y0 + 14
    rw = min(210, max(120, int(len(root) * root_fs * 0.56) + 18))
    b.append(box(180 - rw / 2, ry, rw, 26, root, stroke=PURPLE, fill=PURPLE_F, fs=root_fs, bold=True))
    n = len(children)
    gap = 10
    cw = min(max_w, (CANVAS - 8 - gap * (n - 1)) / n)
    cy = ry + 26 + 34
    span = n * cw + gap * (n - 1)
    left = (CANVAS - span) / 2
    centers = [left + cw / 2 + i * (cw + gap) for i in range(n)]
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


# ---------------------------------------------------------------- Q1
def plastic_tree():
    b = []
    b.append(label(180, 18, 'Plastics — classification', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(105, 30, 150, 26, 'Plastic', stroke=PURPLE, fill=PURPLE_F, fs=9.2, bold=True))
    b.append(line(180, 56, 180, 70, color=GREY))
    b.append(line(96, 70, 264, 70, color=GREY))
    for x in (96, 264):
        b.append(line(x, 70, x, 84, color=GREY))
    b.append(box(16, 84, 160, 30, 'Thermoplastic', stroke=BLUE, fill=BLUE_F, fs=8.6, bold=True))
    b.append(box(184, 84, 160, 30, 'Thermosetting', stroke=ORANGE, fill=ORANGE_F, fs=8.6, bold=True))
    # long separate chains on the left, cross-linked network on the right
    for i in range(3):
        y = 132 + i * 16
        b.append(path(f'M28 {y} q 12 -8 24 0 q 12 8 24 0 q 12 -8 24 0 q 12 8 24 0 q 12 -8 24 0',
                      stroke=BLUE, width=1.3))
    for i in range(3):
        y = 132 + i * 16
        b.append(path(f'M196 {y} q 12 -8 24 0 q 12 8 24 0 q 12 -8 24 0 q 12 8 24 0 q 12 -8 24 0',
                      stroke=ORANGE, width=1.3))
    for x in (216, 246, 276, 306):
        b.append(line(x, 128, x, 168, color=ORANGE, width=1.1, dash='3 2'))
    b.append(label(96, 192, 'softens again on heating', fs=6.8, anchor='middle', color=BLUE))
    b.append(label(96, 202, 'PVC, PE, PP, PS', fs=6.8, anchor='middle', color=BLUE))
    b.append(label(264, 192, 'cross-linked, cannot be re-melted', fs=6.8, anchor='middle', color=ORANGE))
    b.append(label(264, 202, 'bakelite, epoxy, melamine', fs=6.8, anchor='middle', color=ORANGE))
    n = notes(14, 216, 'Thermoplastics have long separate chains held by weak forces, so',
              'they can be re-melted and recycled. Thermosets are cross-linked, so the',
              'first set is permanent and they char instead of melting.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def glass_wool():
    b = []
    b.append(label(180, 18, 'Glass wool as thermal insulation', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(f'<rect x="40" y="40" width="30" height="128" fill="#E8D6C6" stroke="{ORANGE}" stroke-width="1.2"/>')
    b.append(label(55, 34, 'hot wall', fs=7.2, anchor='middle', color=ORANGE))
    b.append(f'<rect x="70" y="40" width="86" height="128" fill="{ORANGE_F}" stroke="{ORANGE}" stroke-width="1.3"/>')
    b.append(label(113, 30, 'glass wool mat', fs=7.2, anchor='middle', color=ORANGE))
    # crimped fibres inside the mat
    for i in range(6):
        y = 50 + i * 20
        b.append(path(f'M74 {y} q 8 -7 16 0 q 8 7 16 0 q 8 -7 16 0 q 8 7 16 0', stroke=GREY, width=1))
    b.append(f'<rect x="156" y="40" width="16" height="128" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(label(180, 128, 'steel cladding', fs=6.8, color=GREY))
    b.append(arrow(180, 96, 320, 96, color=RED, head=4))
    b.append(label(250, 86, 'heat flow q greatly reduced', fs=6.6, anchor='middle', color=RED))
    b.append(label(250, 112, 'the surface stays safe to touch', fs=6.4, anchor='middle', color=GREY))
    n = notes(14, 186, 'Glass wool is spun from soda-lime glass; the trapped air in its crimped',
              'fibres gives k ≈ 0.04 W/m·K, so a 50 mm mat does the work of a much thicker',
              'solid layer. It is non-combustible and does not rot, but it must stay dry.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def ceramic_tree():
    return tree('Ceramic materials',
                'Ceramics',
                [['Traditional', 'clay, porcelain,\nsanitaryware'],
                 ['Refractory', 'firebrick, alumina,\nsilica'],
                 ['Advanced', 'SiC, zirconia,\nPZT']],
                ['Ceramics are inorganic, non-metallic solids with ionic or',
                 'covalent bonds, so they are hard, brittle, heat-resistant',
                 'and electrical insulators.'],
                child_fs=6.8, child_h=46)


# ---------------------------------------------------------------- Q2
def creep_curve():
    b = []
    b.append(label(180, 16, 'Creep curve at constant stress and temperature', fs=9.2, anchor='middle',
                   bold=True, color=PURPLE))
    ax, ay = 46, 34
    base = ay + 108
    b.append(arrow(ax, base, ax, ay, color=GREY, head=4))
    b.append(arrow(ax, base, ax + 292, base, color=GREY, head=4))
    b.append(label(28, ay + 54, 'strain', fs=7.2, anchor='middle', color=GREY))
    b.append(label(ax + 160, base + 16, 'time', fs=7.2, anchor='middle', color=GREY))
    b.append(path(f'M{ax} {base - 8} C {ax + 16} {ay + 58} {ax + 32} {ay + 46} {ax + 60} {ay + 44}',
                  stroke=BLUE, width=1.8))
    b.append(path(f'M{ax + 60} {ay + 44} L {ax + 212} {ay + 24}', stroke=GREEN, width=1.8))
    b.append(path(f'M{ax + 212} {ay + 24} C {ax + 246} {ay + 22} {ax + 264} {ay + 12} '
                  f'{ax + 280} {ay - 6}', stroke=RED, width=1.8))
    b.append(label(ax + 46, ay + 84, 'Stage I', fs=6.8, anchor='middle', color=BLUE))
    b.append(label(ax + 46, ay + 93, 'primary', fs=6.4, anchor='middle', color=BLUE))
    b.append(label(ax + 136, ay + 46, 'Stage II — steady rate', fs=6.8, anchor='middle', color=GREEN))
    b.append(label(ax + 244, ay + 4, 'Stage III', fs=6.8, anchor='middle', color=RED))
    b.append(line(ax + 280, ay - 8, ax + 296, ay - 8, color=RED, width=1.4, dash='3 3'))
    b.append(label(ax + 296, ay - 14, 'fracture', fs=6.4, anchor='end', color=RED))
    n = notes(14, base + 28, 'Stage I: the rate falls as the metal strain-hardens.',
              'Stage II: a steady rate, used to compare materials.',
              'Stage III: the rate rises as voids join, and the part breaks.',
              'A part is designed on its stage-II life, not on the first sign of strain.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def varnish_system():
    b = []
    b.append(label(180, 18, 'Varnish on a wooden surface', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    layers = [('Varnish film', 'resin + oil, clear, glossy', PURPLE),
              ('Second coat', 'fills the grain', BLUE),
              ('First coat (sealer)', 'soaks in and bonds', ORANGE),
              ('Wood surface', 'sanded, dry, clean', GREY)]
    y = 34
    for i, (name, why, col) in enumerate(layers):
        h = 34 if i < 3 else 26
        b.append(f'<rect x="24" y="{y}" width="140" height="{h}" fill="#fff" stroke="{col}" stroke-width="1.3"/>')
        b.append(label(94, y + h / 2 + 3, name, fs=7.8, anchor='middle', bold=True, color=col))
        b.append(label(172, y + h / 2 + 2, why, fs=6.8, color=GREY))
        y += h
    b.append(label(94, y + 18, 'each coat dries hard before the next', fs=6.8, anchor='middle', color=GREY))
    n = notes(14, y + 34, 'The four ingredients are resin, oil, solvent and a drier. The film is clear,',
              'so the grain shows through, and it protects the wood from water and abrasion.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


# ---------------------------------------------------------------- Q3
def metals_tree():
    return tree('Engineering metals',
                'Metals',
                [['Ferrous', 'steel, cast iron'],
                 ['Non-ferrous', 'Cu, Al, Zn, Pb, Ni']],
                ['Ferrous metals are alloys of iron: strong and cheap but they rust.',
                 'Non-ferrous metals resist corrosion, conduct well and are lighter.',
                 'The common five are copper, aluminium, zinc, lead and nickel.'],
                child_fs=7.0, child_h=42)


def cast_iron_tree():
    return tree('Cast iron — types',
                'Cast iron (2–4 % C)',
                [['Grey', 'graphite flakes,\ncasts well'],
                 ['White', 'cementite,\nhard, brittle'],
                 ['Malleable', 'heat treated,\nductile skin'],
                 ['Ductile (SG)', 'nodular graphite,\nstrong']],
                ['Carbon above 2 % makes the metal non-malleable, so it is cast.',
                 'Grey iron damps vibration and is cheap; ductile iron is used',
                 'for pipes and crankshafts where some toughness is needed.'],
                child_fs=6.6, child_h=46)


def band_gaps():
    b = []
    b.append(label(180, 16, 'Electrical behaviour of solids', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(label(180, 30, 'upper band = conduction, lower band = valence', fs=6.6, anchor='middle', color=GREY))
    specs = [('Conductor', 'Cu, Ag, Al', GREEN, 0, 'bands overlap'),
             ('Semiconductor', 'Si, Ge', BLUE, 14, 'gap ≈ 1 eV'),
             ('Insulator', 'glass, rubber', RED, 34, 'gap &gt; 5 eV')]
    for i, (name, ex, col, gap, note) in enumerate(specs):
        x = 16 + i * 114
        b.append(box(x, 44, 100, 22, name, stroke=col, fill='#fff', fs=7.8, bold=True))
        b.append(label(x + 50, 78, ex, fs=6.6, anchor='middle', color=col))
        # valence band sits at a common level so the gaps can be compared by eye
        v_top, v_h = 140, 22
        c_h = 22
        c_bot = v_top - gap
        c_top = c_bot - c_h
        b.append(f'<rect x="{x + 6}" y="{v_top}" width="88" height="{v_h}" fill="{BLUE_F}" stroke="{col}" stroke-width="1.2"/>')
        dash = ' stroke-dasharray="3 2"' if gap else ''
        b.append(f'<rect x="{x + 6}" y="{c_top}" width="88" height="{c_h}" fill="#fff" stroke="{col}" '
                 f'stroke-width="1.2"{dash}/>')
        if gap:
            b.append(f'<path d="M{x + 50} {v_top - 2} L{x + 50} {c_bot + 2}" stroke="{GREY}" stroke-width="1"/>')
        b.append(label(x + 50, 176, note, fs=6.4, anchor='middle', color=GREY))
        if gap == 0:
            b.append(label(x + 50, c_top + 15, 'conduction', fs=6.0, anchor='middle', color=col))
            b.append(label(x + 50, v_top + 15, 'valence', fs=6.0, anchor='middle', color=col))
    n = notes(14, 190, 'A solid conducts when its electrons can reach an empty band. In a metal',
              'the bands overlap; in a semiconductor a gap of about 1 eV is crossed by heat',
              'or by doping; in an insulator the gap is above 5 eV, so no conduction.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def visual_inspection():
    b = []
    b.append(label(180, 16, 'Visual inspection of a butt weld', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # two plates with a welded joint between them
    b.append(f'<rect x="40" y="96" width="118" height="30" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(f'<rect x="158" y="96" width="118" height="30" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(path('M158 126 L158 106 Q 160 90 173 90 Q 186 90 188 106 L188 126 Z',
                  stroke=PURPLE, fill=PURPLE_F, width=1.5))
    b.append(label(173, 84, 'weld bead', fs=6.8, anchor='middle', color=PURPLE))
    # a surface crack marked on the right plate
    b.append(path('M226 96 l 6 6 l -3 6 l 7 5', stroke=RED, width=1.6))
    b.append(arrow(240, 74, 232, 92, color=RED, head=3))
    b.append(label(252, 70, 'crack found', fs=6.6, anchor='middle', color=RED))
    # lamp, eye and magnifier
    b.append(circle(52, 52, 9, stroke=ORANGE, fill=ORANGE_F, width=1.3))
    for a, dx, dy in ((0, 16, 0), (90, 0, 16), (180, -16, 0)):
        pass
    b.append(label(52, 34, 'good light', fs=6.6, anchor='middle', color=ORANGE))
    b.append(circle(300, 52, 14, stroke=BLUE, fill='#fff', width=1.4))
    b.append(line(290, 62, 278, 74, color=BLUE, width=2))
    b.append(label(300, 30, 'magnifier', fs=6.6, anchor='middle', color=BLUE))
    b.append(label(180, 146, 'clean the surface, inspect, then record and mark every defect', fs=6.4,
                   anchor='middle', color=GREY))
    n = notes(14, 160, 'Visual inspection is the cheapest test and always the first.',
              'The trained eye finds cracks, porosity, undercut and corrosion.',
              'It needs good light and a clean surface, and finds surface defects only.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


# ---------------------------------------------------------------- Q5
def alloy_tree():
    return tree('Alloys — classification',
                'Alloy',
                [['Ferrous', 'steel, cast iron,\nstainless'],
                 ['Non-ferrous', 'brass, bronze,\nduralumin'],
                 ['By phase', 'solid solution,\neutectic, intermetallic']],
                ['An alloy is a base metal plus other elements, added to raise',
                 'strength, hardness or corrosion resistance. A solid solution is',
                 'one phase, a eutectic is a fine mixture, an intermetallic a compound.'],
                child_fs=6.6, child_h=46)
