"""Reusable flowchart / block-diagram primitives for the C-programming subjects (360-wide SVGs, no markers/CSS)."""
import math
from xml.sax.saxutils import escape
from diagrams_DI01000151_u1 import svg, arrowhead, P, INK
from diagrams_DI01000151_u1 import text as _text

F_TERM = "#E3F5E6"; S_TERM = "#2E7D32"
F_IO = "#E3F0FC"; S_IO = "#1565C0"
F_PROC = "#F1E8FC"; S_PROC = P
F_DEC = "#FFF1DE"; S_DEC = "#E07B00"
F_CON = "#FCE4EC"; S_CON = "#C2185B"
GREY = "#666"


def text(x, y, s, size=12, anchor="middle", color=INK, weight="normal", mono=False):
    t = _text(x, y, escape(s), size, anchor, color, weight)
    if mono:
        t = t.replace("<text ", '<text font-family="DejaVu Sans Mono, Consolas, monospace" ')
    return t


def line(d, color=INK, w=1.8, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>'


def arr(points, color=INK, label=None, lpos=None, lcolor=None):
    """Poly-line arrow through points [(x,y),...]; arrowhead at the last point. Optional label at lpos."""
    d = "M" + " L".join(f"{x} {y}" for x, y in points)
    (x1, y1), (x2, y2) = points[-2], points[-1]
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    out = line(d, color) + arrowhead(x2, y2, ang, 7, color)
    if label:
        lx, ly = lpos
        out += text(lx, ly, label, 10.5, color=lcolor or ("#2E7D32" if label.lower() in ("yes", "true") else "#C62828"), weight="bold")
    return out


def terminal(cx, cy, label, w=96, h=32, size=12):
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{h/2}" fill="{F_TERM}" stroke="{S_TERM}" stroke-width="1.8"/>'
            + text(cx, cy, label, size, weight="bold", color="#1B5E20"))


def process(cx, cy, label, w=130, h=34, size=11.5, mono=False):
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="{F_PROC}" stroke="{S_PROC}" stroke-width="1.8"/>'
            + text(cx, cy, label, size, mono=mono))


def io(cx, cy, label, w=130, h=34, size=11.5, sk=12, mono=False):
    pts = f"{cx-w/2+sk},{cy-h/2} {cx+w/2+sk/2},{cy-h/2} {cx+w/2-sk},{cy+h/2} {cx-w/2-sk/2},{cy+h/2}"
    return (f'<polygon points="{pts}" fill="{F_IO}" stroke="{S_IO}" stroke-width="1.8"/>' + text(cx, cy, label, size, mono=mono))


def decision(cx, cy, label, w=96, h=54, size=11, mono=False):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    return (f'<polygon points="{pts}" fill="{F_DEC}" stroke="{S_DEC}" stroke-width="1.8"/>' + text(cx, cy, label, size, mono=mono))


def connector(cx, cy, label, r=13):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{F_CON}" stroke="{S_CON}" stroke-width="1.8"/>'
            + text(cx, cy, label, 11, weight="bold", color=S_CON))


def predefined(cx, cy, label, w=130, h=34, size=11.5):
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="#FFF8E1" stroke="#8D6E00" stroke-width="1.8"/>'
            + line(f"M{cx-w/2+9} {cy-h/2} V{cy+h/2}", "#8D6E00") + line(f"M{cx+w/2-9} {cy-h/2} V{cy+h/2}", "#8D6E00")
            + text(cx, cy, label, size))


def rbox(cx, cy, w, h, label, fill=F_PROC, stroke=S_PROC, size=11.5, weight="normal", color=INK, rx=7, mono=False):
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
            + text(cx, cy, label, size, color=color, weight=weight, mono=mono))


def title(s, y=18, size=14.5):
    return text(180, y, s, size, weight="bold", color=P)


def down(x, y1, y2, color=INK):
    return arr([(x, y1), (x, y2)], color)
