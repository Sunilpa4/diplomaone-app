# -*- coding: utf-8 -*-
"""Shared 360-wide SVG helpers for DI04005071 (NOTES-GUIDE rules)."""
P, BL, G, O, R = "#7B2CD9", "#1565C0", "#2E7D32", "#B66A00", "#BD2543"
FILLS = {P: "#F3E5F5", BL: "#E3F2FD", G: "#E8F5E9", O: "#FFF3E0", R: "#FCE4EC"}
def t(x, y, s, size=10.5, fill="#272134", bold=False, anchor="middle"):
    w = ' font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{s}</text>'
def r(x, y, w, h, stroke, fill="#ffffff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
def a(x1, y1, x2, y2, color="#444444"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.4"/>'
            f'<polygon points="{x2},{y2} {x2-4},{y2-7} {x2+4},{y2-7}" fill="{color}"/>')
def svg_doc(title, height, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" '
            f'viewBox="0 0 360 {height}" font-family="DejaVu Sans, Arial, sans-serif">'
            f'<rect width="360" height="{height}" fill="#ffffff"/>'
            + t(180, 20, title, 13, P, True) + body + "</svg>")
def flow(title, steps, sub=None):
    """steps: [(label, colour)] vertical boxes with arrows."""
    b = t(180, 42, sub, 9.5, "#666666") if sub else ""
    y = 52 if sub else 42
    for i, (s, c) in enumerate(steps):
        # wrap long labels manually: split at ' — ' or after 34 chars
        lines = [s]
        if len(s) > 38 and " — " in s:
            a_, b_ = s.split(" — ", 1); lines = [a_ + " —", b_]
        elif len(s) > 40:
            words, cur = s.split(), ""
            lines = []
            for w_ in words:
                if len(cur) + len(w_) > 38 and cur: lines.append(cur); cur = w_
                else: cur = (cur + " " + w_).strip()
            if cur: lines.append(cur)
        h = 34 if len(lines) == 1 else 46
        b += r(42, y, 276, h, c, FILLS[c])
        for j, ln in enumerate(lines):
            b += t(180, y + 21 + j*14, ln, 10, c, True)
        if i < len(steps) - 1:
            b += a(180, y + h + 1, 180, y + h + 13)
        y += h + 14
    return svg_doc(title, y + 2, b)
def boxes(title, rows, sub=None):
    """rows: [(name, desc, colour)] stacked classification boxes."""
    b = t(180, 42, sub, 9.5, "#666666") if sub else ""
    y = 52 if sub else 42
    for name, desc, c in rows:
        b += r(18, y, 324, 52, c, FILLS[c]) + t(180, y + 21, name, 11, c, True) + t(180, y + 40, desc, 9.5, "#444444")
        y += 62
    return svg_doc(title, y + 4, b)
