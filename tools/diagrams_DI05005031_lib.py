"""Drawing helpers for the Chemical Reaction Engineering (DI05005031) figures.

Two families of picture carry this subject:

* **equipment** - vessels, jackets, impellers, distributors, packing, sprays, pumps and the piping
  between them. They are drawn part by part so that a student can name every part of a reactor, which
  is what Unit IV asks for ("construction and working in detail").
* **plots** - rate against concentration, ln k against 1/T, the integrated rate equations, the
  Levenspiel plot. They are drawn from computed coordinates, so a figure can never disagree with the
  numbers printed in the notes.

Every figure is 360 units wide, like the rest of the app, and every label is placed from a computed
anchor so that it stays inside the canvas.
"""
import math

from flowchart_lib import svg, text  # noqa: F401  (svg/text re-exported for the unit modules)

INK = "#222222"
GREY = "#666666"
THIN = "#9AA3AD"
BLUE = "#1565C0"
SKY = "#DCEEFB"
STEEL = "#E7EDF3"
GREEN = "#2E7D32"
ORANGE = "#B66A00"
RED = "#BD2543"
PURPLE = "#7B2CD9"
TEAL = "#00695C"
AMBER = "#F6E3C5"
GLASS = "#F7FBFF"

W = 360  # the canvas width every figure is laid out in


# ---------------------------------------------------------------- basic strokes
def ln(x1, y1, x2, y2, color=INK, w=1.4, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round"{da}/>')


def poly(points, color=INK, w=1.6, dash=None, close=False, fill="none"):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in points) + ("Z" if close else "")
    return (f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.4, head=5.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(ang) + head * 0.36 * math.sin(ang),
          y2 - head * math.sin(ang) - head * 0.36 * math.cos(ang))
    p2 = (x2 - head * math.cos(ang) - head * 0.36 * math.sin(ang),
          y2 - head * math.sin(ang) + head * 0.36 * math.cos(ang))
    return (ln(x1, y1, x2, y2, color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" '
            f'fill="{color}"/>')


def pipe(points, color=INK, w=1.5, dash=None):
    """A run of pipe as a rounded polyline."""
    return poly(points, color, w, dash)


def lbl(x, y, s, anchor="start", size=7.6, weight="normal", color=INK):
    return text(x, y, s, size, anchor=anchor, color=color, weight=weight)


def leader(x1, y1, x2, y2, color=THIN, w=0.8, dot=True):
    b = ln(x1, y1, x2, y2, color, w, dash="2,2")
    if dot:
        b += f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="1.5" fill="{color}"/>'
    return b


def heading(t, sub=None):
    b = text(W / 2, 20, t, 12.2, weight="bold", color=INK)
    if sub:
        b += text(W / 2, 37, sub, 9.2, color=GREY)
    return b


def foot(y, *lines):
    return "".join(text(W / 2, y + 12.5 * i, s, 8.6, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- vessels
def vessel(x, y, w, h, color=INK, w_=1.9, fill=GLASS, rx=0, dome=0):
    """An upright shell. `dome` > 0 draws a round-topped head of that height."""
    if dome:
        b = (f'<path d="M{x:.1f} {y + dome:.1f}a{w / 2:.1f} {dome:.1f} 0 0 1 {w:.1f} 0'
             f'L{x + w:.1f} {y + h - rx:.1f}q0 {rx} {-rx:.1f} {rx:.1f}L{x + rx:.1f} {y + h:.1f}'
             f'q{-rx:.1f} 0 {-rx:.1f} {-rx:.1f}Z" fill="{fill}" stroke="{color}" '
             f'stroke-width="{w_}" stroke-linejoin="round"/>')
        return b
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{color}" stroke-width="{w_}"/>')


def liquid(x, y, w, h, level, color=SKY, level_line=BLUE):
    """Liquid filling the shell from `level` (absolute y) down to y + h."""
    return (f'<rect x="{x:.1f}" y="{level:.1f}" width="{w:.1f}" height="{max(0.0, y + h - level):.1f}" '
            f'rx="1" fill="{color}"/>' + ln(x, level, x + w, level, level_line, 1.3))


def jacket(x, y, w, h, color=TEAL, w_=1.2, side="both"):
    """A heating/cooling jacket drawn as an offset shell."""
    d = 7.0
    b = ""
    if side in ("both", "left"):
        b += ln(x - d, y + 4, x - d, y + h - 4, color, w_)
        b += ln(x - d, y + 4, x, y + 4, color, w_)
        b += ln(x - d, y + h - 4, x, y + h - 4, color, w_)
    if side in ("both", "right"):
        b += ln(x + w + d, y + 4, x + w + d, y + h - 4, color, w_)
        b += ln(x + w, y + 4, x + w + d, y + 4, color, w_)
        b += ln(x + w, y + h - 4, x + w + d, y + h - 4, color, w_)
    return b


def hatch_band(x, y, w, h, color=THIN, step=6):
    """A few diagonal ticks that read as 'jacket / insulation' without a pattern definition."""
    b = ""
    n = int(w // step) + 1
    for i in range(n):
        xx = x + i * step
        b += ln(xx, y + h, min(xx + h, x + w), y, color, 0.6)
    return b


def shaft(cx, y1, y2, color=INK, w=2.2):
    return ln(cx, y1, cx, y2, color, w)


def motor(cx, cy, w=24, h=13, color=INK):
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w}" height="{h}" rx="2" '
            f'fill="{AMBER}" stroke="{color}" stroke-width="1.3"/>'
            + lbl(cx, cy, "M", "middle", 7.4, "bold", color))


def impeller(cx, cy, r=15, color=INK, blades=4, angle0=0):
    """A four-blade turbine seen from the side: a hub with blades, drawn flat and convincing."""
    b = f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.4" fill="{color}"/>'
    for k in range(blades):
        a = math.radians(angle0 + k * 90)
        x2, y2 = cx + r * math.cos(a), cy + r * 0.42 * math.sin(a)
        b += ln(cx, cy, x2, y2, color, 2.0)
        b += ln(x2, y2 - 3.2, x2, y2 + 3.2, color, 2.0)
    return b


def baffle(x, y1, y2, color=INK):
    return ln(x, y1, x, y2, color, 2.6)


def distributor(x, y, w, color=INK, holes=7):
    """A perforated plate / sparger: the horizontal bar with its holes."""
    b = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="3.4" rx="1.7" fill="{color}"/>'
    step = w / (holes + 1)
    for i in range(1, holes + 1):
        b += f'<circle cx="{x + i * step:.1f}" cy="{y + 6.2:.1f}" r="1.15" fill="{color}"/>'
    return b


def bubbles(cx, y0, y1, width, n=9, seed=3, color=BLUE, rmin=1.2, rmax=3.0):
    """A rising swarm of bubbles, deterministic so the figure never changes between builds."""
    state = seed
    b = ""
    for i in range(n):
        state = (1103515245 * state + 12345) % 2147483648
        fx = state / 2147483648
        state = (1103515245 * state + 12345) % 2147483648
        fy = state / 2147483648
        state = (1103515245 * state + 12345) % 2147483648
        fr = state / 2147483648
        x = cx - width / 2 + fx * width
        y = y1 - fy * max(0.0, y1 - y0)
        r = rmin + fr * (rmax - rmin)
        b += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{color}" '
              f'stroke-width="0.85" opacity="0.85"/>')
    return b


def packing(x, y, w, h, color=TEAL, step=11, r=3.4):
    """A bed of packing: staggered circles that read as rings or saddles."""
    b = ""
    rows = int(h // step) + 1
    for j in range(rows):
        yy = y + 5 + j * step
        off = (step / 2) if j % 2 else 0
        for xx in range(int(x + 4 + off), int(x + w - 2), step):
            b += (f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="{r}" fill="none" stroke="{color}" '
                  f'stroke-width="0.9"/>')
    return b


def droplets(cx, y, spread, n=7, color=BLUE):
    """Spray droplets falling from a nozzle."""
    b = ""
    for i in range(n):
        f = (i + 0.5) / n
        x = cx - spread + 2 * spread * f
        yy = y + 10 + (i % 3) * 9
        b += f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="1.3" fill="{color}" opacity="0.8"/>'
    return b


def spray_cone(cx, y, spread, length, color=BLUE):
    return (poly([(cx, y), (cx - spread, y + length), (cx + spread, y + length)], color, 1.0,
                 dash="3,3"))

def pump(cx, cy, r=9, color=INK):
    b = f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="#fff" stroke="{color}" stroke-width="1.5"/>'
    b += poly([(cx - r * 0.55, cy - r * 0.55), (cx + r * 0.75, cy), (cx - r * 0.55, cy + r * 0.55)],
              color, 1.2, close=True, fill=color)
    return b


def valve(cx, cy, s=5.0, color=INK):
    return (poly([(cx - s, cy - s), (cx + s, cy + s), (cx + s, cy - s), (cx - s, cy + s)],
                 color, 1.2, close=True, fill="#fff"))


def bubble_glass(x, y, w, h, color=INK):
    """A sight glass / small window on a shell."""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="{h / 2}" fill="#fff" '
            f'stroke="{color}" stroke-width="1.2"/>')


# ---------------------------------------------------------------- plots
def axes(x0, y0, w, h, xlab, ylab, color=INK, xticks=(), yticks=(), size=8.2):
    """Cartesian axes with an arrow on each end and tick labels given as (fraction, label)."""
    b = arrow(x0, y0 + h, x0, y0 - 4, color, 1.3, 5)
    b += arrow(x0, y0 + h, x0 + w + 6, y0 + h, color, 1.3, 5)
    for f, s in xticks:
        xx = x0 + f * w
        b += ln(xx, y0 + h, xx, y0 + h + 3, color, 1.0)
        b += text(xx, y0 + h + 13, s, size, color=GREY)
    for f, s in yticks:
        yy = y0 + h - f * h
        b += ln(x0 - 3, yy, x0, yy, color, 1.0)
        b += text(x0 - 5, yy + 2.6, s, size, anchor="end", color=GREY)
    b += text(x0 + w + 6, y0 + h + 13, xlab, size + 0.6, anchor="end", color=INK, weight="bold")
    b += text(x0 - 3, y0 - 12, ylab, size + 0.6, color=INK, weight="bold")
    return b


def curve(pts, color=BLUE, w=2.0, dash=None):
    return poly(pts, color, w, dash)


def dots(pts, color=RED, r=2.0):
    return "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>' for x, y in pts)


def guide(x1, y1, x2, y2, color=THIN, dash="3,3"):
    return ln(x1, y1, x2, y2, color, 0.9, dash)


def panel(x, y, w, h, fill="#FBFCFD", color=THIN):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" fill="{fill}" '
            f'stroke="{color}" stroke-width="0.9"/>')


def note_box(x, y, w, h, title, lines, color=PURPLE, fill="#F5EEFD", size=7.6):
    b = (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5" fill="{fill}" '
         f'stroke="{color}" stroke-width="1"/>')
    b += text(x + w / 2, y + 12, title, size + 0.6, weight="bold", color=color)
    for i, s in enumerate(lines):
        b += text(x + w / 2, y + 26 + 11.5 * i, s, size, color=INK)
    return b


def box(x, y, w, h, title, lines=(), color=PURPLE, fill="#F5EEFD", size=7.6, r=5):
    b = (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" '
         f'stroke="{color}" stroke-width="1.5"/>')
    b += text(x + w / 2, y + h / 2 if not lines else y + 13, title, size + 0.8, weight="bold",
              color=color)
    for i, s in enumerate(lines):
        b += text(x + w / 2, y + 26 + 11 * i, s, size, color=INK)
    return b
