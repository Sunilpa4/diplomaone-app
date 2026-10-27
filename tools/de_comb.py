"""Combinational-circuit drawing helpers for Digital Electronics (DI03000011) Units 4-5.
bus_circuit: vertical input buses (+ automatic NOT buses) feeding gates in levels; block: labelled block diagram."""
from flowchart_lib import text, P, INK
from de_gates import gate, wire, dot, lab, bexpr, GS

LONG = lambda nm: len(nm) > 1


def bar(nm):
    """'!'-syntax for a complemented name; multi-letter names get one bar over the whole name"""
    return "!(" + nm + ")" if LONG(nm) else "!" + nm


def term(lits):
    """['!A', 'B', '!Cin'] -> bexpr string"""
    out = []
    for l in lits:
        out.append(bar(l[1:]) if l.startswith("!") else l)
    return "·".join(out) if any(LONG(l.lstrip("!")) for l in lits) else "".join(out)


def bus_circuit(names, gates, x0=24, y0=40, pitch=16, lvl_gap=78, out_pad=18, top_gap=10, label_size=10.5):
    """gates: list of dict(k=kind, i=[literals], y=offset, l=level(1..), o=output label or None).
    A literal is a name, '!name' (complement bus), or 'g<j>' (output of gate j).
    Returns (svg, bottom_y, outputs{label: (x, y)})."""
    comps = []
    for g in gates:
        for l in g["i"]:
            if l.startswith("!") and l[1:] not in comps:
                comps.append(l[1:])
    comps.sort(key=names.index)
    bx = {nm: x0 + i * pitch for i, nm in enumerate(names)}
    nx0 = x0 + len(names) * pitch + 4
    cbx = {nm: nx0 + 34 + k * pitch for k, nm in enumerate(comps)}
    last = max(list(bx.values()) + list(cbx.values()))
    lvl_x = {lv: last + 24 + (lv - 1) * lvl_gap for lv in range(1, 5)}
    b = ""
    for nm in names:
        b += lab(bx[nm], y0 - 4, nm, "middle", size=label_size)
    ynot = {}
    for k, nm in enumerate(comps):
        yy = y0 + 12 + k * 24
        ynot[nm] = yy
        g, (ox, _), _ = gate("NOT", nx0, yy, s=0.62)
        b += g + dot(bx[nm], yy) + wire([(bx[nm], yy), (nx0, yy)]) + wire([(ox, yy), (cbx[nm], yy)])
        b += bexpr(cbx[nm], y0 - 4, bar(nm), label_size - 0.5, color="#555")
    top = y0 + 14 + len(comps) * 24 + top_gap
    outs, svg_g = {}, []
    for j, g in enumerate(gates):
        y = top + g["y"]
        x = lvl_x[g.get("l", 1)]
        n = len(g["i"])
        if g["k"] == "WIRE":
            outs[j] = (x + 45, y)
            svg_g.append((x, y, [(x + 45, y)], (x + 45, y)))
            continue
        s, (ox, oy), ins = gate(g["k"], x, y, n=n)
        b += s
        outs[j] = (ox, oy)
        svg_g.append((x, y, ins, (ox, oy)))
    bottom = max(top + g["y"] for g in gates) + 30
    for nm in names:
        b += wire([(bx[nm], y0 + 2), (bx[nm], bottom)])
    for nm in comps:
        b += wire([(cbx[nm], ynot[nm]), (cbx[nm], bottom)])
    for j, g in enumerate(gates):
        x, y, ins, _ = svg_g[j]
        n = len(ins)
        xmin = min(ix for ix, _ in ins)
        maxd = (n - 1) / 2
        for k, ((ix, iy), l) in enumerate(zip(ins, g["i"])):
            if l.startswith("g") and l[1:].isdigit():
                sx, sy = outs[int(l[1:])]
                if abs(sy - iy) < 0.5:
                    b += wire([(sx, sy), (ix, iy)])
                else:
                    d = abs(k - maxd)
                    mx = xmin - 8 - 9 * (maxd - d)
                    b += wire([(sx, sy), (mx, sy), (mx, iy), (ix, iy)])
            else:
                src = cbx[l[1:]] if l.startswith("!") else bx[l]
                b += dot(src, iy) + wire([(src, iy), (ix, iy)])
    named = [(j, g) for j, g in enumerate(gates) if g.get("o")]
    out_x = max(outs[j][0] for j, _ in named) + out_pad if named else 0
    res = {}
    for j, g in named:
        ox, oy = outs[j]
        b += wire([(ox, oy), (out_x, oy)]) + _nlab(out_x + 4, oy + 4, g["o"], "start", label_size)
        res[g["o"]] = (out_x, oy)
    return b, bottom, res


def block(x, y, w, h, title, ins=(), outs=(), lead=26, size=11, fill="#F1E8FC", stroke=P, bottom=(), sub=None):
    """Block diagram box. ins/outs: names spread on left/right; bottom: control inputs entering from below."""
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>'
    lines = title.split("\n")
    for i, t in enumerate(lines):
        b += text(x + w / 2, y + h / 2 + (i - (len(lines) - 1) / 2) * 14 - (6 if sub else 0), t, size + 1, weight="bold", color=GS)
    if sub:
        b += text(x + w / 2, y + h / 2 + 8 + (len(lines) - 1) * 7, sub, 9, color="#666")
    pts = {}
    for side, names in (("L", ins), ("R", outs)):
        for i, nm in enumerate(names):
            yy = y + h * (i + 1) / (len(names) + 1)
            if side == "L":
                b += wire([(x - lead, yy), (x, yy)]) + _arrow(x, yy) + _nlab(x - lead - 4, yy + 4, nm, "end", size)
                pts[nm] = (x - lead, yy)
            else:
                b += wire([(x + w, yy), (x + w + lead, yy)]) + _arrow(x + w + lead, yy) + _nlab(x + w + lead + 4, yy + 4, nm, "start", size)
                pts[nm] = (x + w + lead, yy)
    for i, nm in enumerate(bottom):
        xx = x + w * (i + 1) / (len(bottom) + 1)
        b += wire([(xx, y + h + lead - 6), (xx, y + h)]) + _arrow_up(xx, y + h) + _nlab(xx, y + h + lead + 6, nm, "middle", size)
        pts[nm] = (xx, y + h + lead - 6)
    return b, pts


def _nlab(x, y, nm, anchor, size):
    if "!" in nm:
        return bexpr(x, y, nm, size, anchor=anchor)
    return lab(x, y, nm, anchor, size=size)


def _arrow(x, y, c="#222"):
    return f'<path d="M{x - 6} {y - 3.5} L{x} {y} L{x - 6} {y + 3.5} Z" fill="{c}"/>'


def _arrow_up(x, y, c="#222"):
    return f'<path d="M{x - 3.5} {y + 6} L{x} {y} L{x + 3.5} {y + 6} Z" fill="{c}"/>'


def eq_box(x, y, w, lines, size=11.5, lh=22, fill="#FCFAFF", stroke="#D9C8F0", color=P):
    """box of bexpr lines (overline syntax)"""
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{12 + lh * len(lines)}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
    for i, s in enumerate(lines):
        c = color
        if isinstance(s, tuple):
            s, c = s
        b += bexpr(x + w / 2, y + 6 + lh * (i + 0.5) + size * 0.35, s, size, color=c)
    return b
