"""Reusable Chemical-Engineering figure primitives, drawn with d1draw.

These are the pieces every Chemical note needs — a stirred tank, a column, a
manometer, a stream, a control volume — so a new unit only composes them instead
of redrawing equipment each time. All figures stay inside the app's visual
language (white ground, brand purple, 900x500 canvas unless stated).
"""
from __future__ import annotations

import os

from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

W, H = 900, 500


# --------------------------------------------------------------------- vessels
def tank(c: Canvas, x, y, w=170, h=190, fill="#FFFFFF", stroke=P, dashed=False):
    """Open-top cylindrical vessel; returns (left, right, top, bottom, axis_x)."""
    c.rect(x, y, w, h, fill, stroke, 1.8, rx=6, dash="6 5" if dashed else None)
    c.line(x, y + 3, x + w, y + 3, LINE, 1.2)          # liquid surface hint
    return x, x + w, y, y + h, x + w / 2


def agitator(c: Canvas, cx, y_top, y_bottom, blade=44):
    c.line(cx, y_top, cx, y_bottom - 22, INK, 2)
    c.line(cx - blade / 2, y_bottom - 22, cx + blade / 2, y_bottom - 22, INK, 2.6)
    c.line(cx - blade / 2, y_bottom - 22, cx - blade / 2, y_bottom - 12, INK, 2.2)
    c.line(cx + blade / 2, y_bottom - 22, cx + blade / 2, y_bottom - 12, INK, 2.2)


def column(c: Canvas, x, y, w=120, h=300, fill=LAV, stroke=P, trays=0, packing=False):
    c.rect(x, y, w, h, "#FFFFFF", stroke, 2, rx=10)
    cx = x + w / 2
    if packing:
        import random
        random.seed(7)
        for i in range(18):
            px = x + 12 + random.random() * (w - 24)
            py = y + 16 + i * (h - 30) / 18
            r = 5 + random.random() * 4
            c.circle(px, py, r, GREY_FILL, LINE, 1.1)
    for i in range(trays):
        ty = y + (i + 1) * h / (trays + 1)
        c.line(x + 8, ty, x + w - 26, ty, PD, 2.4)
        c.line(x + w - 26, ty, x + w - 26, ty + 14, PD, 2.4)   # downcomer
    return cx, x, x + w, y, y + h


def impeller_top(c: Canvas, cx, y):  # motor on top of a column / tank
    c.rect(cx - 22, y - 26, 44, 22, GREY_FILL, MUTED, 1.6, rx=4)
    c.text(cx, y - 15, "M", 12, "middle", MUTED, "bold")


def pump(c: Canvas, cx, cy, r=15):
    c.circle(cx, cy, r, "#FFFFFF", P, 1.9)
    c.poly([(cx - 5, cy - 6), (cx + 7, cy), (cx - 5, cy + 6)], P, P, 1.2)


def valve(c: Canvas, cx, cy, s=9):
    c.poly([(cx - s, cy - s), (cx + s, cy - s), (cx, cy)], "#FFFFFF", INK, 1.4)
    c.poly([(cx - s, cy + s), (cx + s, cy + s), (cx, cy)], "#FFFFFF", INK, 1.4)


def flange(c: Canvas, cx, cy, w=14, h=18):
    c.rect(cx - w / 2, cy - h / 2, w, h, GREY_FILL, MUTED, 1.4, rx=2)


# --------------------------------------------------------------------- streams
def stream(c: Canvas, pts, label=None, lpos=None, color=PD, sw=2.4, dashed=False):
    """Process stream, optionally labelled at lpos."""
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        c.line(x1, y1, x2, y2, color, sw, "7 5" if dashed else None)
    if label:
        lx, ly = lpos or pts[0]
        c.text(lx, ly - 10, label, 12, "middle", color, "bold")


def arrow_stream(c: Canvas, pts, label=None, lpos=None, color=PD, sw=2.4, dashed=False):
    for (x1, y1), (x2, y2) in zip(pts, pts[1:-1]):
        c.line(x1, y1, x2, y2, color, sw, "7 5" if dashed else None)
    c.arrow(*pts[-2], *pts[-1], color, sw, 9, "7 5" if dashed else None)
    if label:
        lx, ly = lpos or pts[0]
        c.text(lx, ly - 10, label, 12, "middle", color, "bold")


# --------------------------------------------------------------------- gauges
def manometer(c: Canvas, cx, y_top, fluid_h, span=110, wall=8, label=None):
    """U-tube manometer centred on cx, vertical limbs of the given height."""
    left, right = cx - span / 2, cx + span / 2
    y_bot = y_top + fluid_h + 40
    # limbs
    c.line(left, y_top, left, y_bot, INK, 1.6)
    c.line(right, y_top, right, y_bot, INK, 1.6)
    # fluid (drawn as a thicker coloured column)
    c.line(left, y_bot - fluid_h, left, y_bot, P, 7)
    c.line(right, y_bot - fluid_h + 26, right, y_bot, P, 7)
    c.path(f"M{left} {y_bot} Q{cx} {y_bot + 26} {right} {y_bot}", "none", INK, 1.6)
    c.line(left + 4, y_bot - fluid_h, right - 4, y_bot - fluid_h, MUTED, 1, "4 4")
    c.line(left + 4, y_bot - fluid_h + 26, right - 4, y_bot - fluid_h + 26, MUTED, 1, "4 4")
    c.dim(right + 26, y_bot - fluid_h, right + 26, y_bot - fluid_h + 26, "h", offset=0)
    if label:
        c.text(cx, y_bot + 52, label, 12, "middle", MUTED)
    return left, right, y_bot


def pressure_gauge(c: Canvas, cx, cy, r=22, label="P"):
    c.circle(cx, cy, r, "#FFFFFF", P, 2)
    c.line(cx, cy, cx + r * 0.55, cy - r * 0.55, RED, 2)
    c.text(cx, cy + r + 14, label, 12, "middle", MUTED, "bold")


def thermometer(c: Canvas, cx, cy, h=60):
    c.rect(cx - 4, cy - h / 2, 8, h, "#FFFFFF", MUTED, 1.4, rx=4)
    c.circle(cx, cy + h / 2, 7, RED_FILL, RED, 1.4)
    c.line(cx, cy + h / 2 - 6, cx, cy + h / 2 - 6, "none", 0)
    c.text(cx, cy - h / 2 - 12, "T", 12, "middle", MUTED, "bold")


# --------------------------------------------------------------------- plots
def axes(c: Canvas, x, y, w, h, xlabel, ylabel, xticks=None, yticks=None, title=None):
    """Cartesian plot frame with optional ticks. Returns a mapping helper."""
    c.arrow(x, y + h, x + w, y + h, INK, 1.6)      # x-axis
    c.arrow(x, y + h, x, y, INK, 1.6)              # y-axis
    c.text(x + w / 2, y + h + 34, xlabel, 12.5, "middle", INK, "bold")
    c.text(x - 72, y + h / 2, ylabel, 12.5, "middle", INK, "bold")
    for t in (xticks or []):
        px = x + t * w
        c.line(px, y + h, px, y + h + 6, INK, 1.2)
        c.text(px, y + h + 16, str(t), 10.5, "middle", MUTED)
    for t in (yticks or []):
        py = y + h - t * h
        c.line(x - 6, py, x, py, INK, 1.2)
        c.text(x - 12, py, str(t), 10.5, "end", MUTED)
    if title:
        c.text(x + w / 2, y - 14, title, 13, "middle", PD, "bold")
    return lambda fx, fy: (x + fx * w, y + h - fy * h)


def slope_line(c: Canvas, pt, y1, y2, label=None, color=PD, dash=None, sw=2):
    c.line(*pt(0, y1), *pt(1, y2), color, sw, dash)
    if label:
        lx, ly = pt(0.72, y1 + 0.72 * (y2 - y1))
        c.text(lx + 8, ly - 8, label, 11.5, "start", color, "bold")


# --------------------------------------------------------------------- files
def out_path(branch: str, sem: int, code: str, name: str) -> str:
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content",
                        branch, f"sem{sem}", code, "diagrams")
    return os.path.abspath(os.path.join(root, name + ".svg"))
