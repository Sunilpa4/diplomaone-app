"""Shared drawing helpers for the Engineering Graphics (DI01000111) diagrams.

Every figure is 360 units wide and built from computed coordinates, so the drawing always agrees with
the arithmetic printed in the notes.
"""
import math

from flowchart_lib import text

INK = "#222222"
GREY = "#666666"
THIN = "#9AA3AD"
BLUE = "#1565C0"
GREEN = "#2E7D32"
ORANGE = "#B66A00"
RED = "#BD2543"
PURPLE = "#7B2CD9"
TEAL = "#00695C"


def ln(x1, y1, x2, y2, color=INK, w=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round"{da}/>')


def poly(points, color=INK, w=1.8, dash=None, close=False):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in points) + ("Z" if close else "")
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    s = 5.0
    p1 = (x2 - s * math.cos(ang) + s * 0.32 * math.sin(ang),
          y2 - s * math.sin(ang) - s * 0.32 * math.cos(ang))
    p2 = (x2 - s * math.cos(ang) - s * 0.32 * math.sin(ang),
          y2 - s * math.sin(ang) + s * 0.32 * math.cos(ang))
    return (ln(x1, y1, x2, y2, color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" '
            f'fill="{color}"/>')


def dot(x, y, color=RED, r=2.2):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'


def ring(x, y, color=RED, r=3.4):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" stroke="{color}" '
            f'stroke-width="1.3"/>')


def heading(t, sub=None):
    b = text(180, 21, t, 12.4, weight="bold", color=INK)
    if sub:
        b += text(180, 39, sub, 9.4, color=GREY)
    return b


def foot(y, *lines):
    return "".join(text(180, y + 13 * i, s, 8.8, color=GREY) for i, s in enumerate(lines))


def xy(y, x0=16, x1=344, label=True):
    """The reference line, drawn the way a drawing sheet has it: thin and long."""
    b = ln(x0, y, x1, y, INK, 1.1)
    if label:
        b += text(x1 - 2, y - 5, "X Y", 7.2, anchor="end", color=GREY)
    return b


def tag(x, y, s, color=INK, dx=4, dy=-5, anchor="start", size=7.4, weight=None):
    return text(x + dx, y + dy, s, size, anchor=anchor, color=color, weight=weight)


def dash_box(x, y, w, h, fill="#F4F6F8"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" '
            f'stroke="{THIN}" stroke-width="0.9"/>')


def p2(x0, y0, length, angle_deg, up=True):
    """Endpoint at `length` from (x0, y0); angles are measured from the +x axis, `up` flips y."""
    a = math.radians(angle_deg)
    return (x0 + length * math.cos(a), y0 - (length * math.sin(a) if up else -length * math.sin(a)))
