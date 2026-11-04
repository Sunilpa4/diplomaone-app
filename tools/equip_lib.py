# -*- coding: utf-8 -*-
"""Equipment-style SVG primitives for DI04005071 real-type diagrams (360 px wide)."""
INK = "#272134"
STEEL, STEEL_F = "#2F5D8A", "#DCE9F5"
HOT, HOT_F = "#B66A00", "#FDEBD7"
CAT, CAT_F = "#2E7D32", "#E8F5E9"
GAS, GAS_F = "#BD2543", "#FCE4EC"
WAT, WAT_F = "#1565C0", "#E3F2FD"
PUR, PUR_F = "#7B2CD9", "#F3E5F5"
GRAY = "#5A5A5A"

_DEFS = ('<defs>'
 '<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#444444"/></marker>'
 '<marker id="ahB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#1565C0"/></marker>'
 '<marker id="ahG" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2E7D32"/></marker>'
 '<marker id="ahR" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#BD2543"/></marker>'
 '<marker id="ahO" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#B66A00"/></marker>'
 '</defs>')

def svg_doc(title, sub, height, body):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" '
         f'viewBox="0 0 360 {height}" font-family="DejaVu Sans, Arial, sans-serif">'
         f'<rect width="360" height="{height}" fill="#ffffff"/>' + _DEFS
         + f'<text x="180" y="19" font-size="12.5" fill="#7B2CD9" text-anchor="middle" font-weight="bold">{title}</text>')
    if sub:
        s += f'<text x="180" y="34" font-size="9" fill="#666666" text-anchor="middle">{sub}</text>'
    return s + body + "</svg>"

def t(x, y, s, size=9, fill=INK, bold=False, anchor="middle", italic=False):
    w = ' font-weight="bold"' if bold else ""
    i = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}{i}>{s}</text>'

def rect(x, y, w, h, fill="#ffffff", stroke=STEEL, sw=1.5, rx=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def circ(cx, cy, r, fill="#ffffff", stroke=STEEL, sw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def ell(cx, cy, rx, ry, fill="#ffffff", stroke=STEEL, sw=1.5):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1, y1, x2, y2, stroke=GRAY, sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def path(d, fill="none", stroke=GRAY, sw=1.4, dash=None, marker=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}{m}/>'

def pipe(pts, color="#444444", sw=1.6, dash=None, marker="ah", arrow=True):
    """Polyline of <line> segments + explicit polygon arrowhead (renderer-proof)."""
    import math
    col = {"ah": "#444444", "ahB": "#1565C0", "ahG": "#2E7D32", "ahR": "#BD2543", "ahO": "#B66A00"}[marker]
    if color != "#444444":
        col = color
    out = ""
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        out += line(x1, y1, x2, y2, col, sw, dash)
    if arrow and len(pts) >= 2:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - 8 * math.cos(ang), y2 - 8 * math.sin(ang)
        px, py = 3.6 * math.sin(ang), -3.6 * math.cos(ang)
        out += (f'<polygon points="{x2:.1f},{y2:.1f} {bx + px:.1f},{by + py:.1f} '
                f'{bx - px:.1f},{by - py:.1f}" fill="{col}"/>')
    return out

def h_vessel(x, y, w, h, fill=STEEL_F, stroke=STEEL):
    """Horizontal cylindrical vessel with dished ends."""
    r = h / 2
    return (f'<path d="M{x + r},{y} H{x + w - r} A{r},{r} 0 0 1 {x + w - r},{y + h} H{x + r} '
            f'A{r},{r} 0 0 1 {x + r},{y} Z" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')

def column(x, y, w, h, trays=6, fill=STEEL_F, stroke=STEEL, tray_col="#7FA6C9"):
    """Vertical column: domed top, tray lines, skirt."""
    b = f'<path d="M{x},{y + 12} A{w/2},{12} 0 0 1 {x + w},{y + 12} V{y + h} H{x} Z" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    if trays:
        for i in range(trays):
            ty = y + 26 + i * (h - 40) / max(trays - 1, 1)
            b += line(x + 3, ty, x + w - 3, ty, tray_col, 1.1)
    b += rect(x + w * 0.3, y + h, w * 0.4, 7, "#C9D6E4", stroke, 1.1, 1)
    return b

def v_reactor(x, y, w, h, beds=(), fill="#FDF6EC", stroke=HOT):
    """Vertical reactor vessel with catalyst bed bands [(label, frac_centre)]."""
    b = f'<path d="M{x},{y + 10} A{w/2},{10} 0 0 1 {x + w},{y + 10} V{y + h - 10} A{w/2},{10} 0 0 1 {x},{y + h - 10} Z" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    for lab, fy in beds:
        by = y + fy * h
        b += rect(x + 3, by - 9, w - 6, 18, "#F6C98B", HOT, 1.0, 2)
        b += t(x + w / 2, by + 3, lab, 7.5, HOT, True)
    return b

def sphere(cx, cy, r, fill="#FDF6EC", stroke=HOT):
    return circ(cx, cy, r, fill, stroke, 1.6)

def furnace(x, y, w, h):
    """Fired heater cabin with burner flames at floor and tube rows at roof."""
    b = rect(x, y, w, h, "#FDF1E3", HOT, 1.7, 2)
    for i in range(3):  # convection tube rows at top
        ty = y + 10 + i * 8
        b += line(x + 6, ty, x + w - 6, ty, HOT, 2.2)
    n = max(2, int(w // 26))
    for i in range(n):  # burners + flames
        bx = x + 14 + i * (w - 28) / max(n - 1, 1)
        b += f'<path d="M{bx - 5},{y + h} L{bx},{y + h - 16} L{bx + 5},{y + h} Z" fill="#F4A259" stroke="{HOT}" stroke-width="0.8"/>'
        b += rect(bx - 6, y + h - 3, 12, 4, "#8A8A8A", GRAY, 0.7, 1)
    return b

def exch(x, y, w=34, h=20):
    """Shell-and-tube exchanger symbol: box with zigzag."""
    pts = []
    steps = 4
    for i in range(steps * 2 + 1):
        px = x + 3 + i * (w - 6) / (steps * 2)
        py = y + 4 if i % 2 == 0 else y + h - 4
        pts.append((px, py))
    return rect(x, y, w, h, "#EFF6EE", CAT, 1.4, 2) + pipe(pts, CAT, 1.1, None, "ahG", arrow=False)

def pump(cx, cy, r=8, label="P"):
    return circ(cx, cy, r, "#FFFFFF", STEEL, 1.5) + f'<path d="M{cx - r + 2},{cy + r - 2} L{cx + r - 2},{cy} L{cx - r + 2},{cy - r + 2} Z" fill="{STEEL_F}" stroke="{STEEL}" stroke-width="0.9"/>' + t(cx, cy + r + 11, label, 7.5, STEEL, True)

def drum_filter(cx, cy, r=30):
    """Rotary vacuum drum partially in a trough."""
    b = f'<path d="M{cx - r - 10},{cy + 6} H{cx + r + 10} L{cx + r - 2},{cy + r + 10} H{cx - r + 2} Z" fill="{WAT_F}" stroke="{WAT}" stroke-width="1.4"/>'
    b += circ(cx, cy, r, "#FFF8E7", HOT, 1.7)
    b += circ(cx, cy, 5, "#FFFFFF", HOT, 1.2)
    for ang in (40, 90, 140, 220, 270, 320):
        import math
        x2 = cx + (r - 3) * math.cos(math.radians(ang)); y2 = cy + (r - 3) * math.sin(math.radians(ang))
        b += line(cx, cy, x2, y2, "#D8B26A", 0.9)
    return b

def lbl(x, y, s, anchor="start", size=8.5, color=INK, bold=False):
    return t(x, y, s, size, color, bold, anchor)

def leader(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, "#999999", 0.8) + f'<circle cx="{x1}" cy="{y1}" r="1.6" fill="#999999"/>'

def note(x, y, s, anchor="middle"):
    return t(x, y, s, 8, "#666666", False, anchor, True)
