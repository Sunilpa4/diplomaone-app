"""DI03000061 RWPD - Unit 3 diagrams: Bootstrap components."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT
from diagrams_DI03000061_u2 import BSB, BSG, BSR, BSY, BSC, BSGR, BSD


def caret(x, y, color="#fff", s=4, up=False):
    d = f"M{x - s} {y - s / 2} L{x + s} {y - s / 2} L{x} {y + s / 2} Z" if not up else f"M{x - s} {y + s / 2} L{x + s} {y + s / 2} L{x} {y - s / 2} Z"
    return f'<path d="{d}" fill="{color}"/>'


def btn(x, y, w, h, label, fill=BSB, color="#fff", size=9, rx=4, stroke=None):
    return box(x, y, w, h, fill, stroke or fill, rx, 1) + text(x + w / 2, y + h / 2 + size / 3, label, size, color=color)


# ------------------------------------------------------------------ 3.1
def components():
    b = title("Types of Bootstrap Components")
    groups = [(12, 42, BLUEF, BLUE, "Navigation", ["Navs (tabs, pills)", "Navbar", "Breadcrumb", "Pagination", "Dropdown"]),
              (184, 42, GREENF, GREEN, "Content boxes", ["Card (panel, thumbnail)", "List group", "Media object", "Jumbotron", "Accordion"]),
              (12, 158, ORANGEF, ORANGE, "Buttons and forms", ["Buttons", "Button group / toolbar", "Input group", "Close button", "Icons"]),
              (184, 158, TEALF, TEAL, "Feedback / status", ["Alerts", "Badges (labels)", "Progress bar", "Spinners", "Toasts"])]
    for x, y, f, s, h, ls in groups:
        b += box(x, y, 164, 106, f, s, 7, 1.4)
        b += text(x + 82, y + 16, h, 10, weight="bold", color=s)
        b += lines(x + 82, y + 34, ls, 9, INK, 15)
    b += note(12, 276, 336, ["Component = ready-made UI part built from HTML",
                             "+ Bootstrap classes (+ JavaScript for interactive",
                             "ones). Advantages: fast, consistent, responsive,",
                             "accessible, easy to customise."], size=9.2)
    return svg(360, 352, b)


def bs3_map():
    b = title("Bootstrap 3 Components in Bootstrap 5")
    rows = [["Bootstrap 3", "Bootstrap 5"],
            ["Glyphicons", "Bootstrap Icons (bi bi-*)"],
            [".label", ".badge"],
            [".panel", ".card + .card-header"],
            [".thumbnail", ".card / .img-thumbnail"],
            [".well", ".card / bg-light p-3"],
            [".jumbotron", "utilities: p-5 bg-body-tertiary"],
            [".page-header", "border-bottom pb-2 mb-3"],
            [".media", ".d-flex + .flex-shrink-0"],
            [".navbar-inverse", "data-bs-theme=\"dark\""],
            [".pull-right", ".float-end / ms-auto"],
            ["span.caret", ".dropdown-toggle (auto)"],
            ["data-toggle", "data-bs-toggle"]]
    b += grid(8, 38, [118, 226], rows, rh=21, size=8.8)
    b += note(12, 322, 336, ["GTU syllabus names are BS3; learn the BS5 way",
                             "and know the old name for viva."], size=9.2)
    return svg(360, 368, b)


def dropdown():
    b = title("Dropdown Menu Structure")
    b += btn(20, 44, 110, 28, "Courses", BSB, size=10)
    b += caret(116, 58)
    b += box(20, 76, 150, 150, "#fff", "#CCC", 5, 1.2)
    b += text(30, 94, "Diploma", 8.8, anchor="start", color=GREY)
    b += text(30, 116, "Computer", 9.4, anchor="start")
    b += box(21, 124, 148, 22, BSB, BSB, 0, 0) + text(30, 139, "IT  (.active)", 9.4, anchor="start", color="#fff")
    b += line("M28 156 L162 156", "#DDD", 1)
    b += text(30, 174, "Degree", 8.8, anchor="start", color=GREY)
    b += text(30, 196, "B.E.", 9.4, anchor="start")
    b += text(30, 216, "M.E. (.disabled)", 9.4, anchor="start", color="#AAA")
    labs = [(58, ".dropdown-toggle  (caret)"), (94, ".dropdown-header"), (116, ".dropdown-item"),
            (156, ".dropdown-divider"), (216, "disabled item")]
    for y, l in labs:
        b += line(f"M176 {y - 3} L196 {y - 3}", P, 1) + text(200, y, l, 8.8, anchor="start", color=P, mono=True)
    b += code(16, 250, ['<div class="dropdown">', '  <button class="btn dropdown-toggle"', '    data-bs-toggle="dropdown">..</button>',
                        '  <ul class="dropdown-menu">', '    <li><a class="dropdown-item">..</a></li>', '  </ul>', '</div>'], 8.4, 12.5)
    b += note(12, 344, 336, ["Direction: .dropup .dropend .dropstart.",
                             "Align right: .dropdown-menu-end. Needs bundle.js."], size=9.2)
    return svg(360, 390, b)


def card():
    b = title("Card Component")
    b += box(40, 40, 170, 250, "#fff", "#BBB", 7, 1.4)
    b += box(41, 41, 168, 26, "#F7F7F7", "#F7F7F7", 6, 0) + line("M41 67 L209 67", "#DDD", 1)
    b += text(125, 58, "Featured", 9.4)
    b += box(41, 67, 168, 76, "#B39DDB", "#B39DDB", 0, 0)
    b += text(125, 110, "image", 9.4, color="#fff")
    b += text(52, 162, "Card title", 11, anchor="start", weight="bold")
    b += text(52, 178, "Subtitle", 9, anchor="start", color=GREY)
    b += text(52, 196, "Some quick text for", 9, anchor="start")
    b += text(52, 209, "the card content.", 9, anchor="start")
    b += btn(52, 220, 60, 22, "Button", BSB, size=9)
    b += box(41, 256, 168, 33, "#F7F7F7", "#F7F7F7", 6, 0) + line("M41 256 L209 256", "#DDD", 1)
    b += text(125, 276, "Footer", 9, color=GREY)
    labs = [(56, ".card-header"), (106, ".card-img-top"), (160, ".card-title"), (178, ".card-subtitle"), (202, ".card-text"),
            (232, ".btn / .card-link"), (276, ".card-footer")]
    for y, l in labs:
        b += line(f"M212 {y - 3} L232 {y - 3}", P, 1) + text(236, y, l, 8.8, anchor="start", color=P, mono=True)
    b += box(244, 136, 104, 4, "#fff", "#fff", 0, 0)
    b += text(125, 306, ".card  >  .card-body (padding)", 9, color=P, mono=True)
    b += note(12, 316, 336, ["Replaces BS3 panel, well and thumbnail.",
                             "Layouts: grid of cards, .card-group, horizontal card,",
                             ".card-img-overlay, text-bg-* colours, h-100."], size=9.2)
    return svg(360, 376, b)


def btn_groups():
    b = title("Button Group and Toolbar")
    b += text(14, 48, ".btn-group", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(14, 56, 180, 28, BSB, BSB, 5, 0)
    for i, l in enumerate(["Left", "Middle", "Right"]):
        b += text(44 + i * 60, 74, l, 9.4, color="#fff")
        if i:
            b += line(f"M{14 + i * 60} 56 L{14 + i * 60} 84", "#0A58CA", 1)
    b += text(204, 74, "joined buttons", 9, anchor="start", color=GREY)
    b += text(14, 108, ".btn-toolbar  (groups in a row)", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(10, 114, 340, 40, "#fff", ORANGE, 5, 1)
    for gx, n, c in [(18, 3, BSGR), (130, 2, BSC), (222, 1, BSG)]:
        b += box(gx, 120, n * 32, 28, c, c, 5, 0)
        for i in range(n):
            b += text(gx + 16 + i * 32, 138, str(i + 1), 9.4, color="#fff" if c != BSC else INK)
        b += text(gx + n * 32 + 4, 150, "", 8)
    b += text(272, 138, "me-2 gaps", 8.6, anchor="start", color=GREY)
    b += text(14, 178, ".btn-group-vertical", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(14, 186, 70, 84, BSY, BSY, 5, 0)
    for i, l in enumerate(["Top", "Middle", "Bottom"]):
        b += text(49, 204 + i * 28, l, 9.2)
        if i:
            b += line(f"M14 {186 + i * 28} L84 {186 + i * 28}", "#D39E00", 1)
    b += text(160, 178, "Nested dropdown", 9.6, anchor="start", weight="bold", color=P)
    b += box(160, 186, 140, 28, BSR, BSR, 5, 0)
    b += text(190, 204, "Home", 9.4, color="#fff") + line("M220 186 L220 214", "#B02A37", 1)
    b += text(252, 204, "More", 9.4, color="#fff") + caret(282, 200)
    b += box(220, 216, 90, 50, "#fff", "#CCC", 4, 1)
    b += text(230, 234, "About", 9, anchor="start") + text(230, 254, "Contact", 9, anchor="start")
    b += note(12, 282, 336, ["Sizes: .btn-group-lg / .btn-group-sm.",
                             "Toggle buttons: input.btn-check + label.btn.",
                             "Add role=\"group\" / role=\"toolbar\"."], size=9.2)
    return svg(360, 342, b)


def input_group():
    b = title("Input Group")
    rows = [("@", "Username", None), ("+91", "Mobile", None), ("Rs.", "Amount", ".00"), (None, "Search", "Go")]
    for i, (pre, mid, post) in enumerate(rows):
        y = 44 + i * 40
        x = 30
        if pre:
            b += box(x, y, 44, 28, "#E9ECEF", "#CED4DA", 4, 1) + text(x + 22, y + 18, pre, 9.6)
            x += 44
        w = 180 if post else 230
        if not pre:
            w += 44
        b += box(x, y, w, 28, "#fff", "#CED4DA", 0 if pre or post else 4, 1) + text(x + 10, y + 18, mid, 9.4, anchor="start", color="#999")
        x += w
        if post == "Go":
            b += box(x, y, 50, 28, BSB, BSB, 4, 0) + text(x + 25, y + 18, "Go", 9.6, color="#fff")
        elif post:
            b += box(x, y, 50, 28, "#E9ECEF", "#CED4DA", 4, 1) + text(x + 25, y + 18, post, 9.6)
    b += text(52, 218, ".input-group-text", 8.6, color=P, mono=True)
    b += text(170, 218, ".form-control", 8.6, color=P, mono=True)
    b += text(300, 218, "button", 8.6, color=P, mono=True)
    b += code(16, 242, ['<div class="input-group">', '  <span class="input-group-text">@</span>',
                        '  <input class="form-control">', '</div>'], 8.6, 13)
    b += note(12, 300, 336, ["Addons before, after or both; checkbox, select,",
                             "button, dropdown, file input. Sizes -sm / -lg.",
                             "BS3 .input-group-addon -> BS5 .input-group-text"], size=9.2)
    return svg(360, 360, b)


# ------------------------------------------------------------------ 3.2
def navs():
    b = title("Navs: Tabs and Pills")
    b += text(14, 48, ".nav-tabs", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += line("M14 82 L346 82", "#DEE2E6", 1.2)
    b += f'<path d="M20 82 L20 60 Q20 56 24 56 L86 56 Q90 56 90 60 L90 82" fill="#fff" stroke="#DEE2E6" stroke-width="1.2"/>'
    b += line("M21 82 L89 82", "#fff", 2)
    for i, l in enumerate(["Unit 1", "Unit 2", "Unit 3"]):
        b += text(55 + i * 74, 73, l, 9.4, color=INK if i == 0 else BSB)
    b += text(14, 110, ".nav-pills", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(20, 118, 70, 26, BSB, BSB, 5, 0)
    for i, l in enumerate(["Day", "Week", "Month"]):
        b += text(55 + i * 62, 135, l, 9.4, color="#fff" if i == 0 else BSB)
    b += text(14, 172, ".nav-underline", 9.6, anchor="start", weight="bold", color=P, mono=True)
    for i, l in enumerate(["New", "Popular"]):
        b += text(40 + i * 64, 192, l, 9.4, color=INK if i == 0 else GREY)
    b += line("M24 198 L56 198", INK, 2)
    b += text(214, 110, "Vertical: .flex-column", 9.6, anchor="start", weight="bold", color=P, mono=True)
    b += box(220, 118, 120, 24, BSB, BSB, 5, 0) + text(230, 134, "Dashboard", 9.2, anchor="start", color="#fff")
    b += text(230, 158, "Students", 9.2, anchor="start", color=BSB)
    b += text(230, 180, "Settings", 9.2, anchor="start", color=BSB)
    b += text(14, 224, "Tab plug-in (switch content)", 9.8, anchor="start", weight="bold", color=P)
    b += code(16, 240, ['<button class="nav-link" data-bs-toggle="tab"', '  data-bs-target="#u2">Unit 2</button>',
                        '<div class="tab-content">', '  <div class="tab-pane fade" id="u2">..</div>', '</div>'], 8.4, 12.5)
    b += note(12, 312, 336, [".nav-fill / .nav-justified fill the width.",
                             "justify-content-center / -end align the items."], size=9.2)
    return svg(360, 358, b)


def navbar():
    b = title("Responsive Navbar")
    b += text(14, 46, "Desktop (from the -expand- breakpoint)", 9.4, anchor="start", weight="bold")
    b += box(14, 54, 332, 34, BSD, BSD, 4, 0)
    b += text(24, 76, "Brand", 10.4, anchor="start", weight="bold", color="#fff")
    for i, l in enumerate(["Home", "About", "Courses"]):
        b += text(96 + i * 50, 76, l, 9, anchor="start", color="#ddd")
    b += caret(243, 72, "#ddd", 3.5)
    b += box(250, 62, 52, 18, "#fff", "#fff", 3, 0) + text(256, 75, "Search", 8, anchor="start", color="#999")
    b += btn(306, 62, 34, 18, "Go", BSY, INK, 8)
    labs = [(40, ".navbar-brand"), (140, ".navbar-nav"), (276, "form.d-flex")]
    for x, l in labs:
        b += line(f"M{x} 90 L{x} 100", P, 1) + text(x, 110, l, 8.4, color=P, mono=True)
    b += text(14, 136, "Phone (collapsed)", 9.4, anchor="start", weight="bold")
    b += box(14, 144, 150, 30, BSD, BSD, 4, 0)
    b += text(24, 164, "Brand", 10.4, anchor="start", weight="bold", color="#fff")
    b += box(124, 150, 32, 18, BSD, "#888", 3, 1)
    for i in range(3):
        b += line(f"M131 {154 + i * 5} L149 {154 + i * 5}", "#ddd", 1.4)
    b += text(176, 160, ".navbar-toggler", 8.6, anchor="start", color=P, mono=True)
    b += text(176, 174, "tap -> menu opens", 8.6, anchor="start", color=GREY)
    b += box(14, 178, 150, 64, "#343A40", "#343A40", 4, 0)
    for i, l in enumerate(["Home", "About", "Courses"]):
        b += text(24, 194 + i * 17, l, 9, anchor="start", color="#ddd")
    b += text(176, 214, ".collapse.navbar-collapse", 8.6, anchor="start", color=P, mono=True)
    b += rows_table(14, 256)
    b += note(12, 330, 336, ["navbar-expand-lg: collapsed below 992 px.",
                             "Colour: bg-* + data-bs-theme=\"dark\"."], size=9.2)
    return svg(360, 376, b)


def rows_table(x, y):
    rows = [["Position class", "Behaviour"],
            [".fixed-top / .fixed-bottom", "always stays at top / bottom"],
            [".sticky-top", "scrolls, then sticks at top"]]
    return grid(x - 6, y, [150, 194], rows, rh=20, size=8.6)


def breadcrumb_pagination():
    b = title("Breadcrumb and Pagination")
    b += box(14, 42, 332, 30, "#F8F9FA", "#F8F9FA", 4, 0)
    x = 24
    for i, l in enumerate(["Home", "Computer", "Sem 3", "RWPD"]):
        last = i == 3
        b += text(x, 62, l, 9.6, anchor="start", color=GREY if last else BSB)
        x += len(l) * 6.4 + 8
        if not last:
            b += text(x, 62, "/", 9.6, anchor="start", color=GREY)
            x += 14
    b += text(90, 90, ".breadcrumb-item", 8.6, color=P, mono=True)
    b += text(270, 90, ".active (current page)", 8.6, color=P, mono=True)
    b += code(16, 112, ['<ol class="breadcrumb">', '  <li class="breadcrumb-item"><a href="#">Home</a></li>',
                        '  <li class="breadcrumb-item active">RWPD</li>', '</ol>'], 8.2, 12.5)
    b += text(14, 184, "Pagination", 9.8, anchor="start", weight="bold", color=P)
    items = ["Previous", "1", "2", "3", "Next"]
    x = 30
    for i, l in enumerate(items):
        w = 64 if len(l) > 2 else 32
        fill = BSB if l == "2" else ("#F1F1F1" if l == "Previous" else "#fff")
        col = "#fff" if l == "2" else ("#999" if l == "Previous" else BSB)
        b += box(x, 194, w, 30, fill, "#DEE2E6", 0, 1) + text(x + w / 2, 213, l, 9.4, color=col)
        x += w
    b += text(62, 242, ".disabled", 8.6, color=P, mono=True)
    b += text(158, 242, ".active", 8.6, color=P, mono=True)
    b += text(250, 242, ".page-link", 8.6, color=P, mono=True)
    b += note(12, 256, 336, ["ul.pagination > li.page-item > a.page-link",
                             "Sizes: .pagination-lg / -sm. Centre with",
                             "justify-content-center. JS shows items per page:",
                             "slice((page - 1) * per, page * per)."], size=9.2)
    return svg(360, 332, b)


# ------------------------------------------------------------------ 3.3
def alerts_badges():
    b = title("Alerts, Badges and Jumbotron")
    al = [("alert-success", "#D1E7DD", "#0F5132", "Saved successfully."), ("alert-danger", "#F8D7DA", "#842029", "Error! Fee not paid."),
          ("alert-warning", "#FFF3CD", "#664D03", "Last date 30 Nov.")]
    for i, (c, f, t, msg) in enumerate(al):
        y = 42 + i * 36
        b += box(14, y, 236, 30, f, f, 5, 0) + text(24, y + 19, msg, 9.2, anchor="start", color=t)
        b += text(256, y + 19, "." + c, 8.4, anchor="start", color=P, mono=True)
    b += text(232, 61 + 36, "x", 11, color="#842029")
    b += text(14, 164, ".alert-dismissible + .btn-close data-bs-dismiss=\"alert\"", 8.4, anchor="start", color=GREY, mono=True)
    b += text(14, 190, "Badges", 9.8, anchor="start", weight="bold", color=P)
    b += text(14, 214, "Notices", 13, anchor="start")
    b += btn(70, 201, 36, 18, "New", BSR, size=9)
    b += btn(120, 201, 30, 18, "4", BSGR, size=9)
    b += btn(160, 201, 40, 18, "Pill", BSB, size=9, rx=9)
    b += box(208, 198, 74, 24, BSB, BSB, 4, 1) + text(234, 213, "Inbox", 9, color="#fff")
    b += btn(262, 203, 14, 14, "7", "#fff", BSB, 8)
    b += btn(294, 198, 28, 24, "", BSD)
    b += f'<circle cx="322" cy="198" r="7" fill="{BSR}"/>' + text(322, 201, "3", 8, color="#fff")
    b += text(14, 246, "Jumbotron (BS5: utilities)", 9.8, anchor="start", weight="bold", color=P)
    b += box(14, 254, 332, 62, "#E9ECEF", "#E9ECEF", 8, 0)
    b += text(28, 278, "Learn Web Design", 14, anchor="start", weight="bold")
    b += text(28, 296, "lead text ...", 9, anchor="start", color=GREY)
    b += btn(260, 280, 72, 24, "Get started", BSB, size=9)
    b += note(12, 326, 336, ["div.p-5.mb-4.bg-body-tertiary.rounded-3 + .display-*",
                             "BS3 .label -> BS5 .badge; .jumbotron removed in BS5."], size=9)
    return svg(360, 372, b)


def progress():
    b = title("Progress Bars")
    items = [("a. basic 40%", 0.40, BSB, False, ""), ("b. label + height", 0.75, BSG, False, "75%"),
             ("c. striped", 0.60, BSY, True, "60%"), ("   animated (stripes move)", 0.85, BSR, True, "85%")]
    for i, (lab, v, c, st, t) in enumerate(items):
        y = 44 + i * 40
        b += text(14, y + 6, lab, 9, anchor="start", color=GREY)
        b += box(14, y + 12, 332, 14, "#E9ECEF", "#E9ECEF", 7, 0)
        b += box(14, y + 12, 332 * v, 14, c, c, 7, 0)
        if st:
            for k in range(0, int(332 * v) - 6, 14):
                b += f'<path d="M{14 + k} {y + 26} L{21 + k} {y + 12} L{28 + k} {y + 12} L{21 + k} {y + 26} Z" fill="#fff" fill-opacity="0.25"/>'
        if t:
            b += text(14 + 332 * v / 2, y + 22, t, 8.4, color="#fff")
    y = 210
    b += text(14, y - 4, "multiple: .progress-stacked", 9, anchor="start", color=GREY)
    for x0, w, c, t in [(14, 100, BSG, "Pass"), (114, 66, BSY, "ATKT"), (180, 34, BSR, "Fail")]:
        b += box(x0, y + 2, w, 14, c, c, 0, 0) + text(x0 + w / 2, y + 13, t, 8, color="#fff" if c != BSY else INK)
    b += box(214, y + 2, 132, 14, "#E9ECEF", "#E9ECEF", 0, 0)
    b += code(16, 246, ['<div class="progress">', '  <div class="progress-bar progress-bar-striped',
                        '    progress-bar-animated bg-danger"', '    style="width: 85%">85%</div>', '</div>'], 8.4, 12.5)
    b += note(12, 316, 336, ["JavaScript: bar.style.width = v + \"%\";",
                             "setInterval() to animate, clearInterval() to stop."], size=9.2)
    return svg(360, 362, b)


def media_list():
    b = title("Media Object and List Group")
    def person(x, y, r, lab, col):
        return f'<circle cx="{x + r}" cy="{y + r}" r="{r}" fill="{col}"/>' + text(x + 2 * r + 8, y + r - 2, lab, 9.2, anchor="start", weight="bold") + \
            text(x + 2 * r + 8, y + r + 11, "details ...", 8.4, anchor="start", color=GREY)
    b += person(14, 44, 18, "Grandfather", "#7E57C2")
    b += line("M32 82 L32 110 L50 110", GREY, 1)
    b += person(54, 96, 15, "Father", "#42A5F5")
    b += line("M69 126 L69 150 L86 150", GREY, 1)
    b += person(90, 138, 12, "Me", "#EF5350")
    b += line("M32 110 L32 190 L50 190", GREY, 1)
    b += person(54, 176, 15, "Uncle", "#26A69A")
    b += text(14, 228, 'd-flex > img.flex-shrink-0 + div.ms-3', 8.4, anchor="start", color=P, mono=True)
    b += text(14, 242, "nested: another d-flex inside div.ms-3", 8.4, anchor="start", color=GREY)
    # list group
    b += text(206, 48, "List group", 9.8, anchor="start", weight="bold", color=P)
    items = [("JioFiber", BSB, "#fff", "4.5"), ("Airtel", "#fff", INK, "4.3"), ("BSNL", "#fff", "#AAA", ""),
             ("DGVCL", "#D1E7DD", "#0F5132", ""), ("Emergency", "#F8D7DA", "#842029", "")]
    for i, (l, f, c, bd) in enumerate(items):
        y = 56 + i * 28
        b += box(206, y, 140, 28, f, "#DEE2E6", 0, 1) + text(216, y + 18, l, 9.2, anchor="start", color=c)
        if bd:
            b += btn(312, y + 7, 26, 15, bd, "#fff" if i == 0 else BSB, BSB if i == 0 else "#fff", 8)
    b += lines(276, 210, [".active  .disabled", ".list-group-item-success", "-action (clickable)"], 8.2, P, 12)
    b += note(12, 258, 336, ["Media (BS4 .media) -> BS5 flex utilities.",
                             "List group: .list-group > .list-group-item;",
                             ".list-group-flush inside a card (BS3 panel)."], size=9.2)
    return svg(360, 318, b)


DIAGRAMS = {"web3_components": components, "web3_bs3_map": bs3_map, "web3_dropdown": dropdown, "web3_card": card,
            "web3_btn_groups": btn_groups, "web3_input_group": input_group, "web3_navs": navs, "web3_navbar": navbar,
            "web3_breadcrumb": breadcrumb_pagination, "web3_alerts_badges": alerts_badges, "web3_progress": progress,
            "web3_media_list": media_list}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
