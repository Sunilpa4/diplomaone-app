"""DI03000061 RWPD - Unit 2 diagrams: grid, images, typography, tables, forms, buttons, display."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT

BSB = "#0D6EFD"; BSG = "#198754"; BSR = "#DC3545"; BSY = "#FFC107"; BSC = "#0DCAF0"; BSGR = "#6C757D"; BSD = "#212529"


# ------------------------------------------------------------------ 2.1
def grid_anatomy():
    b = title("Bootstrap Grid Structure")
    b += box(12, 40, 336, 168, BLUEF, BLUE, 6, 1.6)
    b += text(22, 55, ".container", 10, anchor="start", weight="bold", color=BLUE, mono=True)
    b += box(24, 64, 312, 132, ORANGEF, ORANGE, 5, 1.4)
    b += text(34, 79, ".row", 10, anchor="start", weight="bold", color=ORANGE, mono=True)
    for i, (w, lab) in enumerate([(4, ".col-4"), (8, ".col-8")]):
        x = 36 + (0 if i == 0 else 4 * 24.5 + 4)
        b += box(x, 88, w * 24.5 - 4, 96, PF, P, 4, 1.3)
        b += text(x + (w * 24.5 - 4) / 2, 104, lab, 9.6, weight="bold", color=P, mono=True)
        b += box(x + 8, 114, w * 24.5 - 20, 58, "#fff", GREY, 3, 0.8)
        b += text(x + (w * 24.5 - 4) / 2, 146, "content", 9, color=GREY)
    b += code(16, 228, ['<div class="container">', '  <div class="row">', '    <div class="col-4">...</div>',
                        '    <div class="col-8">...</div>', '  </div>', '</div>'], 8.8, 13)
    b += note(196, 220, 152, ["Rules:", "1. rows inside a", "   container", "2. only columns in", "   a row", "3. content in columns",
                              "4. total = 12"], size=8.8, lh=13)
    return svg(360, 326, b)


def grid12():
    b = title("12-Column Grid")
    cw = 26.5
    for i in range(12):
        b += box(14 + i * (cw + 1.5) - 1.5 * 0, 40, cw, 22, PF, P, 2, 1)
        b += text(14 + i * (cw + 1.5) + cw / 2, 55, str(i + 1), 9, color=P)
    rows = [[12], [6, 6], [4, 4, 4], [3, 6, 3], [8, 4], [3, 3, 3, 3], [2, 10]]
    cols = [BLUEF, GREENF, ORANGEF, TEALF, REDF, BLUEF, GREENF]
    strokes = [BLUE, GREEN, ORANGE, TEAL, RED, BLUE, GREEN]
    for r, spans in enumerate(rows):
        y = 74 + r * 30
        x = 14
        for s in spans:
            w = s * (cw + 1.5) - 1.5
            b += box(x, y, w, 24, cols[r], strokes[r], 3, 1.1)
            b += text(x + w / 2, y + 16, f"col-{s}", 9, color=strokes[r], mono=True)
            x += w + 1.5
    b += note(12, 290, 336, ["Spans in a row should add up to 12.",
                             "More than 12: the extra column wraps to a new line.",
                             ".col (no number) = equal share of the row."], size=9.4)
    return svg(360, 350, b)


def containers():
    b = title("Containers")
    # phone + desktop for 3 types
    names = [(".container", BLUE, BLUEF, 0.72), (".container-fluid", GREEN, GREENF, 1.0), (".container-md", ORANGE, ORANGEF, 0.72)]
    b += text(70, 46, "Phone (< 576)", 9.6, weight="bold")
    b += text(240, 46, "Desktop (1200 px)", 9.6, weight="bold")
    for i, (n, s, f, frac) in enumerate(names):
        y = 58 + i * 64
        b += box(40, y, 60, 52, "#fff", INK, 5, 1.2)
        b += box(44, y + 6, 52, 40, f, s, 2, 1)
        b += box(140, y, 200, 52, "#fff", INK, 4, 1.2)
        w = 192 * frac
        b += box(140 + (200 - w) / 2, y + 6, w, 40, f, s, 2, 1)
        b += text(240, y + 30, n, 9.6, weight="bold", color=s, mono=True)
    b += text(70, 260, "all 100%", 9, color=GREY)
    rows = [["Class", "sm", "md", "lg", "xl", "xxl"],
            [".container", "540", "720", "960", "1140", "1320"],
            [".container-fluid", "100%", "100%", "100%", "100%", "100%"],
            [".container-md", "100%", "720", "960", "1140", "1320"]]
    b += grid(8, 272, [104, 48, 48, 48, 48, 48], rows, rh=20, size=8.6)
    b += text(180, 368, "max-width in px (below 576 px all are 100%)", 8.8, color=GREY)
    return svg(360, 380, b)


def offset_order():
    b = title("Offset and Reordering")
    b += text(14, 46, "Offset: col-4 offset-4", 9.8, anchor="start", weight="bold", color=P)
    cw = 27
    for i in range(12):
        b += box(14 + i * cw, 54, cw - 2, 10, "#F4F4F4", "#DDD", 1, 0.6)
    b += box(14, 68, 4 * cw - 2, 26, PF, P, 3, 1.2)
    b += text(14 + 2 * cw, 85, "col-4", 9, color=P, mono=True)
    b += box(14 + 4 * cw, 68, 4 * cw - 2, 26, "#fff", GREY, 3, 1)
    b += text(14 + 6 * cw, 85, "offset (empty)", 8.6, color=GREY)
    b += box(14 + 8 * cw, 68, 4 * cw - 2, 26, PF, P, 3, 1.2)
    b += text(14 + 10 * cw, 85, "col-4", 9, color=P, mono=True)
    b += box(14 + 3 * cw, 100, 6 * cw - 2, 24, GREENF, GREEN, 3, 1.2)
    b += text(14 + 6 * cw, 116, "col-6 offset-3 = centred", 8.8, color=GREEN, mono=True)
    # reorder
    b += text(14, 150, "Reordering: same HTML, different order", 9.8, anchor="start", weight="bold", color=P)
    b += box(14, 160, 120, 22, "#fff", GREY, 3, 1)
    b += code(20, 175, ["HTML: A  B  C"], 8.8)
    b += text(60, 200, "Phone", 9.4, weight="bold")
    for i, (l, f, s) in enumerate([("C order-first", ORANGEF, ORANGE), ("A", BLUEF, BLUE), ("B", GREENF, GREEN)]):
        b += box(14, 208 + i * 26, 92, 22, f, s, 3, 1.1)
        b += text(60, 223 + i * 26, l, 8.8, color=s)
    b += text(240, 200, "Desktop (md and up)", 9.4, weight="bold")
    for i, (l, f, s) in enumerate([("A", BLUEF, BLUE), ("C", ORANGEF, ORANGE), ("B order-md-last", GREENF, GREEN)]):
        b += box(128 + i * 74, 208, 70, 48, f, s, 3, 1.1)
        b += lines(163 + i * 74, 228, l.split(" ", 1) if " " in l else [l], 8.6, s, 12)
    b += note(12, 292, 336, ["order-0 ... order-5, order-first (-1), order-last (6).",
                             "Lower order comes first. Uses flexbox 'order'.",
                             "BS3: col-md-offset-*, col-md-push-*, col-md-pull-*."], size=9.2)
    return svg(360, 352, b)


def nesting():
    b = title("Nesting Columns")
    b += box(12, 40, 336, 196, ORANGEF, ORANGE, 5, 1.4)
    b += text(22, 55, ".row", 9.6, anchor="start", weight="bold", color=ORANGE, mono=True)
    b += box(22, 62, 214, 164, PF, P, 4, 1.3)
    b += text(32, 77, ".col-8", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(30, 86, 198, 132, "#fff", ORANGE, 4, 1.2)
    b += text(38, 100, "nested .row (12 again)", 8.8, anchor="start", color=ORANGE, mono=True)
    b += box(38, 108, 88, 46, BLUEF, BLUE, 3, 1)
    b += text(82, 135, "col-6", 9, color=BLUE, mono=True)
    b += box(132, 108, 88, 46, BLUEF, BLUE, 3, 1)
    b += text(176, 135, "col-6", 9, color=BLUE, mono=True)
    for i in range(3):
        b += box(38 + i * 62.5, 162, 57, 46, GREENF, GREEN, 3, 1)
        b += text(66.5 + i * 62.5, 189, "col-4", 9, color=GREEN, mono=True)
    b += box(244, 62, 94, 164, PF, P, 4, 1.3)
    b += text(291, 148, ".col-4", 9.6, weight="bold", color=P, mono=True)
    b += note(12, 246, 336, ["A nested .row goes INSIDE a column.",
                             "Its 12 columns divide the parent column's width,",
                             "so inner col-6 = half of col-8 (= 4 of 12 on page)."], size=9.4)
    return svg(360, 306, b)


# ------------------------------------------------------------------ 2.2
def img_shapes():
    b = title("Image Classes")
    def pic(x, y, w, h, rx, extra=""):
        r = box(x, y, w, h, "#B39DDB", P, rx, 0) if not extra else ""
        return r
    items = [(20, ".rounded", 8), (104, ".rounded-circle", 36), (188, ".img-thumbnail", 4), (272, ".rounded-pill", 28)]
    for x, lab, rx in items:
        if lab == ".img-thumbnail":
            b += box(x, 48, 72, 72, "#fff", "#CCC", 5, 1.2)
            b += box(x + 5, 53, 62, 62, "#B39DDB", "#B39DDB", 2, 0)
        elif lab == ".rounded-pill":
            b += box(x, 62, 72, 46, "#B39DDB", "#B39DDB", 23, 0)
        else:
            b += box(x, 48, 72, 72, "#B39DDB", "#B39DDB", rx, 0)
        b += text(x + 36, 138, lab, 7.6, color=P, mono=True)
    # img-fluid
    b += text(14, 166, ".img-fluid  (max-width:100%; height:auto)", 9.6, anchor="start", weight="bold", color=P)
    b += box(14, 176, 150, 70, "#fff", INK, 4, 1.2)
    b += box(20, 182, 138, 58, "#90CAF9", "#90CAF9", 2, 0)
    b += text(89, 215, "desktop: full size", 8.6, color=BLUE)
    b += box(196, 176, 56, 90, "#fff", INK, 6, 1.2)
    b += box(200, 196, 48, 20, "#90CAF9", "#90CAF9", 2, 0)
    b += text(224, 230, "phone:", 8, color=GREY)
    b += text(224, 241, "shrinks", 8, color=GREY)
    b += rarrow(168, 192, 211, GREY)
    b += text(300, 200, "Alignment", 9.2, weight="bold", color=P)
    b += lines(300, 216, ["float-start", "float-end", "d-block mx-auto", "text-center"], 8.4, INK, 12)
    b += note(12, 280, 336, ["BS3 .img-responsive / .img-circle / .img-rounded",
                             "= BS5 .img-fluid / .rounded-circle / .rounded.",
                             "Figure: .figure, .figure-img, .figure-caption."], size=9.2)
    return svg(360, 340, b)


def typography():
    b = title("Bootstrap Typography")
    rows = [["Class / tag", "Use"],
            [".display-1 ... 6", "very large headings"],
            [".h1 ... .h6", "heading style on any tag"],
            [".lead", "larger intro paragraph"],
            ["<mark>", "highlight text"],
            ["<small>, .small", "smaller / secondary text"],
            ["<abbr title>", "abbreviation tooltip"],
            [".blockquote", "quotation + footer"],
            [".list-unstyled", "list without bullets"],
            [".list-inline", "list items in one line"],
            ["text-start/center/end", "alignment"],
            ["text-uppercase etc.", "UPPER, lower, Capitalize"],
            ["fw-bold, fst-italic", "weight and style"]]
    b += grid(8, 38, [150, 194], rows, rh=20, size=8.8)
    b += note(12, 306, 336, ["Default font size 1rem (16 px), system font stack.",
                             "Reboot gives the same base styles in all browsers."], size=9.2)
    return svg(360, 352, b)


def tables():
    b = title("Table Classes")
    def mini(x, y, lab, stripe=False, border=False, dark=False, hover=False, colors=None):
        r = text(x + 76, y - 6, lab, 9, weight="bold", color=P, mono=True)
        for i in range(4):
            f = "#fff"
            if dark and i == 0: f = BSD
            elif stripe and i % 2 == 1: f = "#F2F2F2"
            if hover and i == 2: f = "#E2E3E5"
            if colors and i > 0: f = colors[i - 1]
            r += box(x, y + i * 16, 152, 16, f, "#999" if border else "#fff", 0, 0.8 if border else 0)
            r += line(f"M{x} {y + (i + 1) * 16} L{x + 152} {y + (i + 1) * 16}", "#CCC", 0.8)
            if border:
                r += line(f"M{x + 76} {y + i * 16} L{x + 76} {y + (i + 1) * 16}", "#999", 0.8)
        return r
    b += mini(12, 56, ".table-striped", stripe=True)
    b += mini(196, 56, ".table-bordered", border=True)
    b += mini(12, 148, ".table-dark head", dark=True)
    b += mini(196, 148, ".table-hover", hover=True)
    b += mini(12, 240, "contextual rows", colors=["#D1E7DD", "#FFF3CD", "#F8D7DA"])
    b += text(272, 234, ".table-responsive", 9, weight="bold", color=P, mono=True)
    b += box(204, 242, 136, 64, "#fff", INK, 4, 1.2)
    b += box(210, 250, 124, 40, "#fff", "#999", 0, 0.8)
    for i in range(5):
        b += line(f"M{210 + i * 40} 250 L{210 + i * 40} 290", "#999", 0.8)
    b += rarrow(230, 320, 298, GREY)
    b += note(12, 318, 336, ["Always start with .table. Add .table-sm for compact,",
                             ".table-borderless, .table-success / danger / warning."], size=9.2)
    return svg(360, 364, b)


# ------------------------------------------------------------------ 2.3
def form_layouts():
    b = title("Form Layouts")
    def inp(x, y, w):
        return box(x, y, w, 14, "#fff", "#999", 3, 0.9)
    def lab(x, y, w=36):
        return box(x, y, w, 6, "#999", "#999", 2, 0)
    panels = [(12, 40, "Vertical (default)"), (184, 40, "Grid (row + col)"),
              (12, 164, "Horizontal"), (184, 164, "Inline (row-cols-auto)")]
    for x, y, t in panels:
        b += box(x, y, 164, 112, "#fff", P, 6, 1.2)
        b += text(x + 82, y + 16, t, 9.4, weight="bold", color=P)
    # vertical
    for i in range(3):
        b += lab(22, 66 + i * 26) + inp(22, 74 + i * 26, 144)
    # grid
    b += lab(194, 66) + inp(194, 74, 68) + lab(270, 66) + inp(270, 74, 72)
    b += lab(194, 96) + inp(194, 104, 144)
    b += box(194, 126, 40, 14, BSB, BSB, 3, 0)
    # horizontal
    for i in range(3):
        b += lab(22, 194 + i * 24, 34) + inp(64, 188 + i * 24, 102)
    b += text(94, 266, "label col-sm-3 | input col-sm-9", 7.6, color=GREY)
    # inline
    b += inp(194, 202, 58) + inp(256, 202, 46)
    b += box(306, 202, 32, 14, BSG, BSG, 3, 0)
    b += text(266, 238, "all fields in one line", 8.4, color=GREY)
    b += note(12, 286, 336, [".form-label  .form-control  .form-select  .form-text",
                             ".form-check (+ -input, -label)  .form-floating",
                             ".was-validated + .invalid-feedback for validation"], size=9, mono=False)
    return svg(360, 344, b)


def buttons():
    b = title("Bootstrap Buttons")
    vs = [("primary", BSB, "#fff"), ("secondary", BSGR, "#fff"), ("success", BSG, "#fff"), ("danger", BSR, "#fff"),
          ("warning", BSY, INK), ("info", BSC, INK), ("light", "#F8F9FA", INK), ("dark", BSD, "#fff")]
    for i, (n, c, t) in enumerate(vs):
        x = 14 + (i % 4) * 84; y = 42 + (i // 4) * 34
        b += box(x, y, 78, 26, c, "#CCC" if n == "light" else c, 5, 1)
        b += text(x + 39, y + 17, n, 9.4, color=t)
    b += text(14, 126, "Outline", 9.6, anchor="start", weight="bold", color=P)
    for i, (n, c, t) in enumerate(vs[:4]):
        x = 14 + i * 84
        b += box(x, 134, 78, 26, "#fff", c, 5, 1.4)
        b += text(x + 39, 151, n, 9.4, color=c)
    b += text(14, 180, "Sizes and states", 9.6, anchor="start", weight="bold", color=P)
    b += box(14, 188, 86, 34, BSB, BSB, 6, 0) + text(57, 210, "btn-lg", 11, color="#fff")
    b += box(106, 192, 66, 26, BSB, BSB, 5, 0) + text(139, 209, "default", 9.4, color="#fff")
    b += box(178, 196, 50, 20, BSB, BSB, 4, 0) + text(203, 210, "btn-sm", 8, color="#fff")
    b += box(234, 192, 52, 26, "#0A58CA", "#0A58CA", 5, 0) + text(260, 209, "active", 9, color="#fff")
    b += f'<rect x="292" y="192" width="56" height="26" rx="5" fill="{BSB}" opacity="0.55"/>' + text(320, 209, "disabled", 9, color="#fff")
    b += text(14, 244, "Block (full width): wrapper .d-grid", 9.6, anchor="start", weight="bold", color=P)
    b += box(14, 252, 332, 24, BSB, BSB, 5, 0) + text(180, 268, "d-grid > .btn", 9.4, color="#fff")
    b += note(12, 288, 336, ["class=\"btn btn-primary\": base .btn + variant.",
                             "Works on <button>, <a role=button>, <input>.",
                             "BS4 .btn-block  ->  BS5 .d-grid gap-2"], size=9.2)
    return svg(360, 348, b)


# ------------------------------------------------------------------ 2.4
def display():
    b = title("Show / Hide with Display Classes")
    rows = [["Class", "xs", "sm", "md", "lg", "xl"],
            ["d-none", "hide", "hide", "hide", "hide", "hide"],
            ["d-none d-md-block", "hide", "hide", "show", "show", "show"],
            ["d-block d-md-none", "show", "show", "hide", "hide", "hide"],
            ["d-none d-lg-block", "hide", "hide", "hide", "show", "show"],
            ["d-md-none d-xl-block", "show", "show", "hide", "hide", "show"]]
    b += grid(8, 38, [124, 44, 44, 44, 44, 44], rows, rh=22, size=8.6)
    b += text(14, 192, "Other ways to hide", 9.8, anchor="start", weight="bold", color=P)
    rows2 = [["Class", "Visible?", "Takes space?"],
             [".d-none", "no", "no"],
             [".invisible", "no", "yes"],
             [".visually-hidden", "no (screen reader yes)", "no"]]
    b += grid(8, 200, [110, 140, 94], rows2, head_fill=TEAL, rh=21, size=8.8)
    b += text(14, 304, "Carets", 9.8, anchor="start", weight="bold", color=P)
    for i, (n, ang) in enumerate([(".dropdown", 90), (".dropup", 270), (".dropend", 0), (".dropstart", 180)]):
        x = 14 + i * 84
        b += box(x, 312, 78, 24, BSB, BSB, 5, 0)
        b += text(x + 33, 328, n[1:].replace("drop", "") or "down", 9, color="#fff")
        b += arrowhead(x + 64, 324, ang, 6, "#fff")
    b += note(12, 346, 336, [".dropdown-toggle draws the caret (BS3: span.caret).",
                             "BS3 .hidden-xs / .visible-md -> BS5 d-* classes."], size=9.2)
    return svg(360, 392, b)


DIAGRAMS = {"web2_grid_anatomy": grid_anatomy, "web2_grid12": grid12, "web2_containers": containers,
            "web2_offset_order": offset_order, "web2_nesting": nesting, "web2_img_shapes": img_shapes,
            "web2_typography": typography, "web2_tables": tables, "web2_form_layouts": form_layouts,
            "web2_buttons": buttons, "web2_display": display}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
