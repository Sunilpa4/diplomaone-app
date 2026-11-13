"""Tiny SVG helper for hand-drawn paper diagrams.

Only rect / path / line / circle / text are emitted, because the website reader's
paperDiagram() whitelist keeps exactly those (plus defs/marker, which we avoid).
Canvas is 360 wide like the notes diagrams; height is whatever the figure needs.
"""

W = 360


def svg(body, height, title=None):
    head = (f'<svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" '
            f'font-family="Arial, Helvetica, sans-serif">'
            f'<rect width="{W}" height="{height}" fill="#ffffff"/>')
    t = ''
    if title:
        t = (f'<text x="{W / 2}" y="20" font-size="13" font-weight="bold" text-anchor="middle" '
             f'fill="#6a2f86">{title}</text>')
    return head + t + body + '</svg>'


def char_w(fs):
    """Approximate advance width of Arial at a given font size."""
    return fs * 0.53


def wrap(text, width, fs, bold=False):
    """Break text into lines that fit inside `width` pixels at font size fs."""
    limit = max(6, int(width / (char_w(fs) * (1.06 if bold else 1.0))))
    words, lines, cur = str(text).split(), [], ''
    for word in words:
        candidate = f'{cur} {word}'.strip()
        if len(candidate) <= limit or not cur:
            cur = candidate
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def box(x, y, w, h, lines=(), stroke='#1565C0', fill='#E9F2FB', fs=9.5, radius=5,
        color='#1a2733', bold=False, lh=None):
    """Rounded box with centred, automatically wrapped text."""
    lines = [lines] if isinstance(lines, str) else list(lines)
    wrapped = []
    for line in lines:
        wrapped.extend(wrap(line, w - 10, fs, bold))
    # shrink the font until the text block fits the box height
    while True:
        lh = lh or fs + 3.2
        if len(wrapped) * lh <= h - 6 or fs <= 6.4:
            break
        fs -= 0.5
        wrapped = []
        for line in lines:
            wrapped.extend(wrap(line, w - 10, fs, bold))
    lh = fs + 3.2
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" '
           f'stroke="{stroke}" stroke-width="1.2"/>']
    total = len(wrapped) * lh
    start = y + (h - total) / 2 + fs * 0.95
    weight = ' font-weight="bold"' if bold else ''
    for i, line in enumerate(wrapped):
        out.append(f'<text x="{x + w / 2}" y="{start + i * lh:.1f}" font-size="{fs}" '
                   f'text-anchor="middle" fill="{color}"{weight}>{line}</text>')
    return ''.join(out)


class _Notes(str):
    """Rendered footer notes; `.bottom` is the y coordinate just below them."""
    bottom = 0.0


def notes(x, y, *lines, fs=8.1, width=330, color='#5b6572', lh=None):
    """Footer notes that wrap inside the canvas width.

    The returned string carries `.bottom`, so the figure height can be set to
    exactly what the wrapped text needs and nothing is ever clipped.
    """
    lh = lh or fs + 3.4
    out, row = [], 0
    for line in lines:
        for piece in wrap(line, width, fs):
            out.append(f'<text x="{x}" y="{y + row * lh:.1f}" font-size="{fs}" fill="{color}">'
                       f'{piece}</text>')
            row += 1
    text = _Notes(''.join(out))
    text.bottom = y + max(row - 1, 0) * lh + 10
    return text


def label(x, y, text, fs=9.5, anchor='start', color='#1a2733', bold=False, italic=False):
    weight = ' font-weight="bold"' if bold else ''
    style = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-size="{fs}" text-anchor="{anchor}" fill="{color}"'
            f'{weight}{style}>{text}</text>')


def arrow(x1, y1, x2, y2, color='#3c4655', width=1.3, head=5.5):
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    px, py = -math.sin(ang) * head * 0.5, math.cos(ang) * head * 0.5
    return (f'<line x1="{x1}" y1="{y1}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{color}" '
            f'stroke-width="{width}"/>'
            f'<path d="M{x2:.1f} {y2:.1f} L{bx + px:.1f} {by + py:.1f} L{bx - px:.1f} {by - py:.1f} Z" '
            f'fill="{color}"/>')


def line(x1, y1, x2, y2, color='#3c4655', width=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'


def circle(cx, cy, r, stroke='#1565C0', fill='#fff', width=1.2):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{width}"/>')


def path(d, stroke='#3c4655', fill='none', width=1.3):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


# palette
PURPLE, BLUE, GREEN, ORANGE, RED, GREY = '#6a2f86', '#1565C0', '#2E7D32', '#B66A00', '#BD2543', '#5b6572'
PURPLE_F, BLUE_F, GREEN_F, ORANGE_F, RED_F, GREY_F = '#F3ECF7', '#E9F2FB', '#EAF6EC', '#FDF1E1', '#FBE9EC', '#F1F3F5'
