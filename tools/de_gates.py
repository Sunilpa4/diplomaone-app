"""Logic-gate SVG symbols + Boolean helpers for Digital Electronics (DI03000011), reused by Units 2-5.
gate(kind, x, y) draws a gate whose left edge is at x and centre line at y; it returns (svg, out_point, input_points)."""
from itertools import product
from flowchart_lib import text, line, P, INK

GF = "#F6F0FE"   # gate fill
GS = "#4A148C"   # gate stroke
WIRE = "#222"
HI = "#2E7D32"   # logic-1 colour
LO = "#9E9E9E"


def _bubble(cx, cy, r=4.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{GS}" stroke-width="1.8"/>'


def _and_body(x, y, s):
    h = 20 * s
    return f'<path d="M{x} {y - h} L{x + 25 * s} {y - h} A{h} {h} 0 0 1 {x + 25 * s} {y + h} L{x} {y + h} Z" fill="{GF}" stroke="{GS}" stroke-width="1.8"/>', x + 45 * s


def _or_body(x, y, s):
    h = 20 * s
    d = (f"M{x} {y - h} Q{x + 12 * s} {y} {x} {y + h} Q{x + 30 * s} {y + h} {x + 50 * s} {y} "
         f"Q{x + 30 * s} {y - h} {x} {y - h} Z")
    return f'<path d="{d}" fill="{GF}" stroke="{GS}" stroke-width="1.8"/>', x + 50 * s


def _in_ys(y, n, s):
    if n == 1:
        return [y]
    if n == 2:
        return [y - 10 * s, y + 10 * s]
    if n == 3:
        return [y - 13 * s, y, y + 13 * s]
    return [y - 15 * s, y - 5 * s, y + 5 * s, y + 15 * s]


def _or_curve_x(x, yy, y, s):
    t = ((yy - y) / (20 * s) + 1) / 2
    return x + 2 * t * (1 - t) * 12 * s


def gate(kind, x, y, n=2, s=1.0, label=None):
    """kind: AND OR NOT NAND NOR XOR XNOR BUF. Returns (svg, (ox, oy), [(ix, iy), ...])."""
    kind = kind.upper()
    b = ""
    if kind in ("NOT", "BUF"):
        h = 15 * s
        b += f'<path d="M{x} {y - h} L{x + 30 * s} {y} L{x} {y + h} Z" fill="{GF}" stroke="{GS}" stroke-width="1.8"/>'
        ox = x + 30 * s
        if kind == "NOT":
            b += _bubble(ox + 4.5, y)
            ox += 9
        return b, (ox, y), [(x, y)]
    ys = _in_ys(y, n, s)
    if kind in ("AND", "NAND"):
        body, ox = _and_body(x, y, s)
        ins = [(x, yy) for yy in ys]
        b += body
    elif kind in ("OR", "NOR"):
        body, ox = _or_body(x, y, s)
        ins = [(_or_curve_x(x, yy, y, s), yy) for yy in ys]
        b += body
    elif kind in ("XOR", "XNOR"):
        body, ox = _or_body(x + 8 * s, y, s)
        h = 20 * s
        b += body + f'<path d="M{x} {y - h} Q{x + 12 * s} {y} {x} {y + h}" fill="none" stroke="{GS}" stroke-width="1.8"/>'
        ins = [(_or_curve_x(x, yy, y, s), yy) for yy in ys]
    else:
        raise ValueError(kind)
    if kind in ("NAND", "NOR", "XNOR"):
        b += _bubble(ox + 4.5, y)
        ox += 9
    if label:
        b += text((x + ox) / 2 - 2, y + 4, label, 9, weight="bold", color=GS)
    return b, (ox, y), ins


def wire(pts, color=WIRE, w=1.6):
    d = "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"/>'


def dot(x, y, color=WIRE):
    return f'<circle cx="{x}" cy="{y}" r="2.8" fill="{color}"/>'


def lab(x, y, s, anchor="end", size=11, color=INK, weight="bold"):
    return text(x, y, s, size, anchor=anchor, color=color, weight=weight)


def over(s):
    """complement bar in SVG text: use a combining overline (U+0305) after each char"""
    return "".join(c + "\u0305" for c in s)


def simple_gate(kind, x, y, n=2, names="AB", out="Y", lead=22, tail=24, s=1.0, out_label=None):
    """gate with labelled input leads and output lead; returns svg and output end point"""
    g, (ox, oy), ins = gate(kind, x, y, n, s)
    b = g
    for (ix, iy), nm in zip(ins, names):
        b += wire([(x - lead, iy), (ix, iy)]) + lab(x - lead - 4, iy + 4, nm)
    b += wire([(ox, oy), (ox + tail, oy)]) + lab(ox + tail + 4, oy + 4, out_label or out, "start")
    return b, (ox + tail, oy)


def tt_svg(x, y, head, rows, cw=30, rh=19, out_cols=1, size=10.5):
    """SVG truth table; last out_cols columns are outputs (green header, 1s highlighted)"""
    b = ""
    nc = len(head)
    for i, h in enumerate(head):
        isout = i >= nc - out_cols
        b += f'<rect x="{x + i * cw}" y="{y}" width="{cw}" height="{rh}" fill="{HI if isout else P}" stroke="{P}" stroke-width="1"/>'
        b += text(x + i * cw + cw / 2, y + rh / 2, h, size, color="#fff", weight="bold")
    for r, row in enumerate(rows):
        yy = y + (r + 1) * rh
        for i, v in enumerate(row):
            isout = i >= nc - out_cols
            fill = ("#E3F5E6" if str(v) == "1" else "#fff") if isout else ("#FAF6FF" if r % 2 else "#fff")
            b += f'<rect x="{x + i * cw}" y="{yy}" width="{cw}" height="{rh}" fill="{fill}" stroke="#C9B3EC" stroke-width="1"/>'
            b += text(x + i * cw + cw / 2, yy + rh / 2, str(v), size, mono=True, weight="bold" if isout else "normal")
    return b


# ---------------------------------------------------------------- Boolean helpers (truth tables, verification)
OPS = {
    "AND": lambda *a: int(all(a)), "OR": lambda *a: int(any(a)), "NOT": lambda a: 1 - a,
    "NAND": lambda *a: 1 - int(all(a)), "NOR": lambda *a: 1 - int(any(a)),
    "XOR": lambda *a: sum(a) % 2, "XNOR": lambda *a: 1 - sum(a) % 2,
}


def truth(f, n):
    """rows (bits..., f(bits)) for all 2^n input combinations, MSB first"""
    return [(*bits, int(f(*bits))) for bits in product((0, 1), repeat=n)]


def minterms(f, n):
    return [i for i, bits in enumerate(product((0, 1), repeat=n)) if f(*bits)]


def equiv(f, g, n):
    return all(int(f(*b)) == int(g(*b)) for b in product((0, 1), repeat=n))


def tt_html(head, rows, out_cols=1):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join((f"<td><b>{v}</b></td>" if i >= len(head) - out_cols else f"<td>{v}</td>") for i, v in enumerate(r)) + "</tr>"
    return h + "</table>"


if __name__ == "__main__":
    assert truth(OPS["XOR"], 2) == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    assert minterms(lambda a, b, c: (a and b) or (not b and c), 3) == [1, 5, 6, 7]
    assert equiv(lambda a, b: 1 - (a & b), lambda a, b: (1 - a) | (1 - b), 2)
    print("ok")


# ---------------------------------------------------------------- Boolean expressions with over-bars
def parse_bars(s):
    """'!A' = A with a bar, '!(A+B)' = bar over A+B (brackets not shown). Returns (chars, bars[(start, end, level)])."""
    chars, bars = [], []

    def rec(i, inside):
        lit = 0
        while i < len(s):
            c = s[i]
            if c == "!":
                if s[i + 1] == "(":
                    st = len(chars)
                    i = rec(i + 2, True)
                    en = len(chars)
                else:
                    st = len(chars); chars.append(s[i + 1]); en = st + 1
                    i += 2
                inner = [lv for a, b, lv in bars if a >= st and b <= en]
                bars.append((st, en, 1 + max(inner) if inner else 0))
            elif c == ")" and inside and lit == 0:
                return i + 1
            else:
                lit += (c == "(") - (c == ")")
                chars.append(c); i += 1
        return i
    rec(0, False)
    return chars, bars


def bexpr(x, y, s, size=12, anchor="middle", color=INK, weight="bold"):
    chars, bars = parse_bars(s)
    cw = size * 0.62
    w = len(chars) * cw
    x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
    b = ""
    for i, c in enumerate(chars):
        if c != " ":
            b += text(x0 + i * cw + cw / 2, y, c, size, mono=True, weight=weight, color=color)
    for st, en, lv in bars:
        yy = y - size * 0.62 - lv * 3.2
        b += f'<path d="M{x0 + st * cw + 1.2:.1f} {yy:.1f} L{x0 + en * cw - 1.2:.1f} {yy:.1f}" stroke="{color}" stroke-width="1.3"/>'
    return b


def bh(s):
    """same syntax to HTML (overline spans); nested bars are shown as one bar over the group"""
    chars, bars = parse_bars(s)
    top = [(a, b) for a, b, lv in bars if not any(a2 <= a and b <= b2 and (a2, b2) != (a, b) for a2, b2, _ in bars)]
    out, i = "", 0
    while i < len(chars):
        hit = [t for t in top if t[0] == i]
        if hit:
            a, b = hit[0]
            out += '<span style="text-decoration:overline">' + "".join(chars[a:b]) + "</span>"
            i = b
        else:
            out += chars[i]; i += 1
    return out
