"""Shared 2-D drawing kit for DiplomaOne diagrams.

Every new unit's diagrams are drawn with these primitives so that all 2,446+ figures
share one look: white background, brand purple, Arial/Helvetica metrics, no <marker>
and no CSS (both break inside flutter_svg on Android).

Coordinate space is a plain canvas measured in px; the helper `save()` writes a
self-contained SVG with a viewBox, which is what `DiagramPicture` needs to keep the
correct aspect ratio in the app.

    from d1draw import Canvas, save
    c = Canvas(900, 500, "Plant utility roles")
    c.box(120, 100, 220, 80, "Water / steam")
    c.arrow(230, 140, 300, 140)
    save(c, "content/.../diagrams/utilities.svg")
"""
from __future__ import annotations

import math
import os
from xml.sax.saxutils import escape

P = "#7B2CD9"          # brand purple
PD = "#6420B8"         # deep purple
LAV = "#EADDF7"        # lavender fill
INK = "#222222"
MUTED = "#6B6275"
LINE = "#B9A6CE"
GREEN = "#2E7D32"
GREEN_FILL = "#E3F5E6"
BLUE = "#1565C0"
BLUE_FILL = "#E3F0FC"
AMBER = "#E07B00"
AMBER_FILL = "#FFF1DE"
RED = "#C2185B"
RED_FILL = "#FCE4EC"
GREY_FILL = "#F4F1F7"

FONT = "Arial, Helvetica, sans-serif"


class Canvas:
    """A drawing surface with the shared visual language."""

    def __init__(self, w: int, h: int, title: str = "", subtitle: str = ""):
        self.w, self.h = w, h
        self.parts: list[str] = []
        if title:
            self.parts.append(self._t(24, 30, title, 19, "start", PD, "bold"))
        if subtitle:
            self.parts.append(self._t(24, 52, subtitle, 12, "start", MUTED))

    # ---------------------------------------------------------------- primitives
    def _t(self, x, y, s, size=12, anchor="middle", color=INK, weight="normal", family=FONT):
        out = ""
        lines = str(s).split("\n")
        for i, ln in enumerate(lines):
            dy = (i - (len(lines) - 1) / 2) * (size + 3)
            out += (
                f'<text x="{x:.1f}" y="{y + dy + size * 0.35:.1f}" font-family="{family}" '
                f'font-size="{size}" text-anchor="{anchor}" fill="{color}" font-weight="{weight}">'
                f"{escape(ln)}</text>"
            )
        return out

    def text(self, x, y, s, size=12, anchor="middle", color=INK, weight="normal"):
        self.parts.append(self._t(x, y, s, size, anchor, color, weight))
        return self

    def mono(self, x, y, s, size=11.5, anchor="middle", color=INK, weight="normal"):
        self.parts.append(self._t(x, y, s, size, anchor, color, weight, "DejaVu Sans Mono, Consolas, monospace"))
        return self

    def rect(self, x, y, w, h, fill="none", stroke=LINE, sw=2, rx=0, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )
        return self

    def box(self, x, y, w, h, label, fill=LAV, stroke=P, size=12, weight="normal", color=INK, rx=7):
        """Rectangle centred on (x, y) with a centred label."""
        self.rect(x - w / 2, y - h / 2, w, h, fill, stroke, 1.8, rx)
        if label:
            self.text(x, y, label, size, "middle", color, weight)
        return self

    def rbox(self, x, y, w, h, label, fill="#FFFFFF", stroke=P, size=12, weight="normal", color=INK, rx=4):
        """Rectangle given by its top-left corner (for layouts where boxes are easier to stack)."""
        self.rect(x, y, w, h, fill, stroke, 1.8, rx)
        if label:
            self.text(x + w / 2, y + h / 2, label, size, "middle", color, weight)
        return self

    def circle(self, x, y, r, fill="none", stroke=P, sw=1.8):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        return self

    def line(self, x1, y1, x2, y2, color=INK, sw=1.8, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}/>'
        )
        return self

    def poly(self, pts, fill="none", stroke=P, sw=1.8, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.parts.append(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
        return self

    def path(self, d_svg, fill="none", stroke=INK, sw=1.8, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<path d="{d_svg}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{da}/>'
        )
        return self

    # ---------------------------------------------------------------- arrows
    def arrow(self, x1, y1, x2, y2, color=INK, sw=1.9, head=8, dash=None, label=None, lpos=None, lcolor=None):
        """Straight arrow with a hand-drawn head (no <marker>, flutter_svg safe)."""
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
        self.line(x1, y1, bx, by, color, sw, dash)
        p1 = (x2 - head * math.cos(ang) + head * 0.45 * math.sin(ang),
              y2 - head * math.sin(ang) - head * 0.45 * math.cos(ang))
        p2 = (x2 - head * math.cos(ang) - head * 0.45 * math.sin(ang),
              y2 - head * math.sin(ang) + head * 0.45 * math.cos(ang))
        self.parts.append(
            f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>'
        )
        if label:
            lx, ly = lpos or ((x1 + x2) / 2, (y1 + y2) / 2 - 6)
            self.text(lx, ly, label, 11, "middle", lcolor or MUTED, "bold")
        return self

    def elbow(self, pts, color=INK, sw=1.9, head=8, label=None, lpos=None):
        """Poly-line arrow through pts [(x, y), ...]."""
        for (x1, y1), (x2, y2) in zip(pts, pts[1:-1]):
            self.line(x1, y1, x2, y2, color, sw)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        self.arrow(x1, y1, x2, y2, color, sw, head)
        if label:
            lx, ly = lpos or ((x1 + x2) / 2, (y1 + y2) / 2 - 6)
            self.text(lx, ly, label, 11, "middle", MUTED, "bold")
        return self

    def dim(self, x1, y1, x2, y2, label, offset=0, color=MUTED):
        """Dimension line with ticks at both ends and a label in the middle."""
        self.line(x1, y1, x2, y2, color, 1.2)
        for (x, y) in ((x1, y1), (x2, y2)):
            if abs(x2 - x1) >= abs(y2 - y1):
                self.line(x, y - 5, x, y + 5, color, 1.2)
            else:
                self.line(x - 5, y, x + 5, y, color, 1.2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if abs(x2 - x1) >= abs(y2 - y1):
            self.text(mx, my + offset - 8, label, 11.5, "middle", color)
        else:
            self.text(mx + offset + 8, my, label, 11.5, "start", color)
        return self

    # ---------------------------------------------------------------- composites
    def title_band(self, label, y=76, color=LAV, fg=PD):
        self.rect(0, y - 18, self.w, 34, color, "none", 0)
        self.text(18, y, label, 14, "start", fg, "bold")
        return self

    def note(self, s, y=None, x=24, size=11.5):
        self.text(x, y if y is not None else self.h - 14, s, size, "start", MUTED)
        return self

    def footer(self, s="Original teaching schematic \u2022 conceptual, not a construction/operating drawing"):
        self.text(24, self.h - 12, s, 10.5, "start", MUTED)
        return self

    # ---------------------------------------------------------------- output
    def svg(self) -> str:
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'font-family="{FONT}">'
            f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>'
            + "".join(self.parts)
            + "</svg>"
        )


def save(canvas: Canvas, path: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(canvas.svg())
    return path
