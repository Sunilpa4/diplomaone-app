"""Drawing helpers for the Engineering Materials Science (DI01000181) figures.

The generic strokes, boxes, panels, axes and plots are re-used from the shared 360-wide drawing kit;
this module only adds the pictures that materials science needs and the other subjects do not:

* **atoms and bonds** - a single atom, an electron-transfer pair, a shared pair, the free electron sea
* **crystals** - an isometric unit cell with corner, body-centre and face-centre atoms, and the HCP
  prism with its three layers at c/a = 1.633
* **microstructure** - a field of irregular grains with boundaries, used for every micrograph in the
  subject
* **coatings** - a layer stack (substrate, primer, topcoat) used for paints, plating and thin films

Every figure is 360 units wide, and every label is placed from a computed anchor so that it stays
inside the canvas.
"""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, box, note_box, lbl, leader, poly, curve, dots, axes,
                                     guide, hatch_band)

__all__ = ["INK", "GREY", "THIN", "BLUE", "GREEN", "ORANGE", "RED", "PURPLE", "TEAL", "W", "AMBER",
           "SKY", "GLASS", "STEEL", "svg", "text", "ln", "arrow", "heading", "foot", "panel", "box",
           "note_box", "lbl", "leader", "poly", "curve", "dots", "axes", "guide", "hatch_band",
           "atom", "atom_pair", "electron", "isometric_cube", "unit_cell", "hcp_cell", "grain_field",
           "film_stack", "micro_scale"]


# ---------------------------------------------------------------- atoms and bonds
def atom(cx, cy, r, label=None, color=INK, fill="#FFFFFF", size=None, weight="bold"):
    """A nucleus drawn as a circle, optionally labelled (Fe, C, Cu ...)."""
    out = (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{color}" '
           f'stroke-width="1.2"/>')
    if label:
        out += text(cx, cy + (size or r) * 0.36, label, size or max(4.6, r * 1.05), color=color,
                    weight=weight)
    return out


def electron(cx, cy, r=1.9, color=RED):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{color}"/>'


def atom_pair(x1, y1, x2, y2, r=11, fill1="#FFFFFF", fill2="#FFFFFF", color1=INK, color2=INK,
              label1=None, label2=None):
    """Two atoms side by side, used for the bond panels."""
    return (atom(x1, y1, r, label1, color1, fill1) + atom(x2, y2, r, label2, color2, fill2))


# ---------------------------------------------------------------- crystals
def isometric_cube(x, y, a, color=INK, w=1.3, dash=None):
    """A cube drawn in oblique projection: the front square plus the back square offset up-right."""
    dx, dy = 0.42 * a, -0.34 * a
    out = ln(x, y, x + a, y, color, w, dash) + ln(x + a, y, x + a, y + a, color, w, dash)
    out += ln(x + a, y + a, x, y + a, color, w, dash) + ln(x, y + a, x, y, color, w, dash)
    out += ln(x, y, x + dx, y + dy, color, w, dash) + ln(x + a, y, x + a + dx, y + dy, color, w, dash)
    out += ln(x + a, y + a, x + a + dx, y + a + dy, color, w, dash)
    out += ln(x, y + a, x + dx, y + a + dy, color, w, dash)
    out += ln(x + dx, y + dy, x + a + dx, y + dy, color, w, dash)
    out += ln(x + a + dx, y + dy, x + a + dx, y + a + dy, color, w, dash)
    out += ln(x + a + dx, y + a + dy, x + dx, y + a + dy, color, w, dash)
    out += ln(x + dx, y + a + dy, x + dx, y + dy, color, w, dash)
    return out


def unit_cell(x, y, a, kind="bcc", color=INK, atom_color=BLUE, r=None, fill=None):
    """A cubic unit cell with the atoms of the given lattice.

    kind: "sc" (corners), "bcc" (corners + body centre), "fcc" (corners + six face centres).
    The atom radius defaults to a readable fraction of a, not the true hard-sphere radius.
    """
    r = r or 0.135 * a
    dx, dy = 0.42 * a, -0.34 * a
    out = isometric_cube(x, y, a, color)
    fill = fill or "#EAF2FB"
    corners = [(x, y), (x + a, y), (x + a, y + a), (x, y + a),
               (x + dx, y + dy), (x + a + dx, y + dy), (x + a + dx, y + a + dy),
               (x + dx, y + a + dy)]
    for cx, cy in corners:
        out += atom(cx, cy, r, None, atom_color, fill)
    if kind == "bcc":
        out += atom(x + a / 2 + dx / 2, y + a / 2 + dy / 2, r, None, atom_color, fill)
    elif kind == "fcc":
        faces = [(x + a / 2, y), (x + a / 2, y + a), (x, y + a / 2), (x + a, y + a / 2),
                 (x + a / 2 + dx, y + dy / 2), (x + a / 2 + dx, y + a + dy / 2)]
        for cx, cy in faces:
            out += atom(cx, cy, r, None, atom_color, fill)
    return out


def hcp_cell(cx, cy, r, color=INK, atom_color=GREEN, atom_fill="#EAF6EC"):
    """The hexagonal close-packed prism: two hexagon layers with the middle layer between them."""
    def hexpts(ax, ay, rad):
        return [(ax + rad * math.cos(math.radians(60 * i + 30)),
                 ay + rad * math.sin(math.radians(60 * i + 30))) for i in range(6)]

    top = hexpts(cx, cy - 0.55 * r, r)
    bot = hexpts(cx, cy + 0.55 * r, r)
    out = poly(bot, color, 1.2) + poly(top, color, 1.2)
    for i in range(6):
        out += ln(top[i][0], top[i][1], bot[i][0], bot[i][1], color, 0.9)
    ar = 0.20 * r
    for pts in (top, bot):
        for px, py in pts:
            out += atom(px, py, ar, None, atom_color, atom_fill)
        out += atom(cx, (cy - 0.55 * r) if pts is top else (cy + 0.55 * r), ar, None, atom_color,
                    atom_fill)
    # three atoms of the middle layer sit in the hollows
    for ang in (90, 210, 330):
        px = cx + 0.5 * r * math.cos(math.radians(ang))
        py = cy + 0.5 * r * math.sin(math.radians(ang)) * 0.55
        out += atom(px, py, ar, None, ORANGE, "#FDF1E3")
    return out


# ---------------------------------------------------------------- microstructure
def grain_field(x, y, w, h, cols=5, rows=3, seed=7, color=INK, fills=("#F3F6F9", "#E9EFF5",
                                                                      "#F7F4EC", "#EEF3F7"),
                jitter=0.34, lw=1.0):
    """A field of irregular grains drawn as jittered hexagonal cells - the micrograph of the subject."""
    state = seed or 1

    def rnd():
        nonlocal state
        state = (1103515245 * state + 12345) % (2 ** 31)
        return state / (2 ** 31)

    cw, ch = w / cols, h / rows
    out = ""
    for j in range(rows):
        for i in range(cols):
            cx = x + (i + 0.5 + (0.5 if j % 2 else 0.0)) * cw
            cy = y + (j + 0.5) * ch
            pts = []
            for k in range(6):
                ang = math.radians(60 * k + (30 if j % 2 else 0))
                rad = (1 - jitter / 2 + jitter * rnd()) * (cw * 0.62)
                pts.append((cx + rad * math.cos(ang), cy + rad * 0.72 * math.sin(ang)))
            if cx - cw > x + w or cy - ch > y + h:
                continue
            out += poly(pts, color, lw, close=True, fill=fills[(i + j) % len(fills)])
    # clip nothing: the caller keeps the field inside a rectangular frame
    return out


# ---------------------------------------------------------------- coatings
def film_stack(x, y, w, layers, color=INK, label_x=None, size=6.8):
    """A stack of horizontal layers from the top down.

    layers: list of (height, fill, stroke, label). The first entry is drawn first (topmost).
    """
    out = ""
    cy = y
    for hgt, fill, stroke, label in layers:
        out += f'<rect x="{x:.1f}" y="{cy:.1f}" width="{w:.1f}" height="{hgt:.1f}" ' \
               f'fill="{fill}" stroke="{stroke}" stroke-width="1.1"/>'
        if label:
            out += text(x + (label_x if label_x is not None else w / 2), cy + hgt / 2 + 2.4,
                        label, size, color=stroke, anchor="middle" if label_x is None else "start")
        cy += hgt
    return out


def micro_scale(x, y, w, bar_um=100, size=6.4, color=GREY):
    """A scale bar for a micrograph, labelled in micrometres."""
    return (ln(x, y, x + w, y, color, 2.2) + ln(x, y - 3, x, y + 3, color, 1.2)
            + ln(x + w, y - 3, x + w, y + 3, color, 1.2)
            + text(x + w / 2, y - 5, f"{bar_um} micron", size, color=color))
