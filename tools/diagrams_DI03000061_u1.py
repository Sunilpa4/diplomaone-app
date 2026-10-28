"""DI03000061 RWPD - Unit 1 diagrams: jQuery basics and Bootstrap introduction."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000061", "diagrams")
NB = "\u00a0"


def code(x, y, ls, size=8.8, lh=13, color=INK):
    return "".join(text(x, y + i * lh, s.replace(" ", NB), size, anchor="start", mono=True, color=color) for i, s in enumerate(ls))


# ------------------------------------------------------------------ 1.1 jQuery
def jq_syntax():
    b = title("jQuery Syntax")
    # big statement
    b += box(14, 46, 332, 40, PF, P, 8, 1.5)
    parts = [("$", RED), ("(", INK), ('"#msg"', BLUE), (")", INK), (".", INK),
             ("hide", GREEN), ("(", INK), ("400", ORANGE), (");", INK)]
    cw = 12.04; x0 = 180 - 21 * cw / 2; pos = 0; mid = {}
    for s_, c in parts:
        for k, ch in enumerate(s_):
            b += text(x0 + (pos + k) * cw + cw / 2, 73, ch, 20, mono=True, weight="bold", color=c)
        mid[s_] = x0 + (pos + len(s_) / 2) * cw
        pos += len(s_)
    # labels
    labs = [(52, RED, ["$ = jQuery", "function"], "$"), (130, BLUE, ["selector", "(find)"], '"#msg"'),
            (230, GREEN, ["action", "(method)"], "hide"), (308, ORANGE, ["argument", "(speed ms)"], "400")]
    for x, c, ls, key in labs:
        m = mid[key]
        b += line(f"M{x} 104 L{m} 92", c, 1.4) + f'<circle cx="{m}" cy="90" r="2.5" fill="{c}"/>'
        b += box(x - 36, 106, 72, 34, "#fff", c, 6, 1.2)
        b += lines(x, 120, ls, 8.8, c, 12)
    b += text(14, 164, "Document ready - run code after the DOM is loaded", 9.6, anchor="start", weight="bold", color=P)
    b += box(14, 172, 332, 74, "#fff", GREY, 6, 1)
    b += code(24, 188, ['$(document).ready(function () {', '  $("#msg").hide(400);', '});'])
    b += code(24, 230, ['$(function () { ... });  // short form'], 8.6, color=GREY)
    b += note(12, 258, 336, ["Include jquery-3.7.1.min.js BEFORE your own script.",
                             "Chaining: $(\"p\").css(\"color\",\"red\").slideUp();",
                             "Getter: $(\"#a\").val()   Setter: $(\"#a\").val(\"5\")"], size=9.2)
    return svg(360, 318, b)


def selectors():
    b = title("jQuery Selectors")
    rows = [["Selector", "Example", "Selects"],
            ["Element", '$("p")', "all <p> elements"],
            ["#id", '$("#name")', "element with id=name"],
            [".class", '$(".note")', "all with class=note"],
            ["Universal", '$("*")', "every element"],
            ["Group", '$("h1, p")', "all <h1> and <p>"],
            ["Descendant", '$("ul li")', "<li> inside <ul>"],
            ["Attribute", '$("[href]")', "having href"],
            ["Attr value", '$("[type=\'text\']")', "type is text"],
            ["Filter", '$("li:first")', "first <li>"],
            ["Filter", '$("tr:even")', "rows 0, 2, 4 ..."],
            ["this", "$(this)", "current element"]]
    b += grid(8, 38, [78, 124, 142], rows, rh=21, size=8.8)
    b += note(12, 300, 336, ["jQuery uses CSS selector syntax, so any CSS",
                             "selector works. Index counting starts at 0."], size=9.4)
    return svg(360, 346, b)


def events():
    b = title("jQuery Events")
    cats = [(12, 42, BLUEF, BLUE, "Mouse events", ["click", "dblclick", "mouseenter", "mouseleave", "hover", "mousedown / up"]),
            (184, 42, GREENF, GREEN, "Keyboard events", ["keydown", "keyup", "keypress", "(event.which or", "event.key = key)"]),
            (12, 156, ORANGEF, ORANGE, "Form events", ["focus", "blur", "change", "submit", "select / input"]),
            (184, 156, TEALF, TEAL, "Document / window", ["ready", "load", "resize", "scroll", "unload"])]
    for x, y, f, s, h, ls in cats:
        b += box(x, y, 164, 104, f, s, 7, 1.4)
        b += text(x + 82, y + 16, h, 10, weight="bold", color=s)
        b += lines(x + 82, y + 31, ls, 9, INK, 12.4)
    b += text(14, 280, "Attaching an event handler", 9.8, anchor="start", weight="bold", color=P)
    b += box(14, 288, 332, 60, "#fff", GREY, 6, 1)
    b += code(22, 304, ['$("#btn").click(function (e) { ... });',
                        '$("#btn").on("click", function (e) { ... });',
                        '$("ul").on("click", "li", fn); // delegation'], 8.4)
    b += note(12, 358, 336, ["e = event object: e.type, e.target, e.pageX,",
                             "e.preventDefault() stops the default action."], size=9.4)
    return svg(360, 404, b)


# ------------------------------------------------------------------ 1.2 Bootstrap
def bs_history():
    b = title("History of Bootstrap")
    ev = [("2010", "Mark Otto and Jacob Thornton build", "\"Twitter Blueprint\" at Twitter"),
          ("2011", "v1.0 released as open source", "(19 August 2011)"),
          ("2012", "v2: responsive design added", "(12-column fluid grid)"),
          ("2013", "v3: mobile-first, flat design,", "Glyphicons, panels, jumbotron"),
          ("2018", "v4: Flexbox grid, Sass, cards,", "rem units, xl breakpoint"),
          ("2021", "v5: no jQuery, no IE, xxl, RTL,", "Utility API, Bootstrap Icons"),
          ("2023", "v5.3: colour modes (dark mode),", "data-bs-theme attribute")]
    b += line("M58 44 L58 330", P, 2.4)
    for i, (y, a, c) in enumerate(ev):
        cy = 50 + i * 41
        col = GREEN if i == len(ev) - 1 else (ORANGE if i >= 5 else P)
        b += f'<circle cx="58" cy="{cy + 8}" r="6" fill="{col}"/>'
        b += text(14, cy + 12, y, 10.4, anchor="start", weight="bold", color=col)
        b += text(74, cy + 6, a, 9.4, anchor="start")
        b += text(74, cy + 20, c, 9, anchor="start", color=GREY)
    b += note(12, 336, 336, ["Bootstrap = free, open-source front-end framework",
                             "of HTML, CSS and JavaScript (most popular today)."], size=9.4)
    return svg(360, 380, b)


def responsive():
    b = title("Responsive Web Design")
    # phone
    b += box(14, 48, 70, 132, "#fff", INK, 9, 1.6)
    for i in range(4):
        b += box(22, 62 + i * 27, 54, 22, PF, P, 3, 1)
        b += text(49, 77 + i * 27, str(i + 1), 9.6, color=P)
    b += text(49, 196, "Mobile", 9.6, weight="bold")
    b += text(49, 210, "1 per row", 8.8, color=GREY)
    # tablet
    b += box(100, 56, 100, 116, "#fff", INK, 8, 1.6)
    for i in range(4):
        x = 108 + (i % 2) * 44; y = 66 + (i // 2) * 48
        b += box(x, y, 40, 42, BLUEF, BLUE, 3, 1)
        b += text(x + 20, y + 25, str(i + 1), 9.6, color=BLUE)
    b += text(150, 196, "Tablet", 9.6, weight="bold")
    b += text(150, 210, "2 per row", 8.8, color=GREY)
    # desktop
    b += box(216, 60, 132, 86, "#fff", INK, 5, 1.6)
    b += line("M270 146 L266 162 M294 146 L298 162 M258 162 L306 162", INK, 1.6)
    for i in range(4):
        x = 223 + i * 31
        b += box(x, 72, 27, 62, GREENF, GREEN, 3, 1)
        b += text(x + 13.5, 107, str(i + 1), 9.6, color=GREEN)
    b += text(282, 196, "Desktop", 9.6, weight="bold")
    b += text(282, 210, "4 per row", 8.8, color=GREY)
    b += box(14, 222, 332, 24, PF, P, 5, 1)
    b += text(180, 238, 'class="col-12 col-sm-6 col-lg-3"', 9.6, mono=True, color=P)
    b += note(12, 256, 336, ["Same HTML, layout changes with screen width.",
                             "Needs: viewport meta tag, fluid grid, flexible",
                             "images and media queries (Bootstrap gives all).",
                             "Mobile first: design for small screens, then grow."], size=9.4)
    return svg(360, 332, b)


def setup():
    b = title("Setting up Bootstrap")
    # CDN
    b += box(12, 42, 164, 158, BLUEF, BLUE, 7, 1.4)
    b += text(94, 58, "Method 1: CDN", 10, weight="bold", color=BLUE)
    b += lines(94, 76, ["Link files from a Content", "Delivery Network server"], 8.8, INK, 12)
    b += box(20, 100, 148, 52, "#fff", BLUE, 4, 1)
    b += code(25, 113, ["<link href=", " \"https://cdn.jsdelivr", " .net/npm/bootstrap@5", " .3.3/dist/css/...\">"], 7.6, 10)
    b += lines(94, 168, ["+ fast, cached, no download", "- needs internet"], 8.8, INK, 13)
    # Local
    b += box(184, 42, 164, 158, GREENF, GREEN, 7, 1.4)
    b += text(266, 58, "Method 2: Local files", 10, weight="bold", color=GREEN)
    b += lines(266, 76, ["Download from", "getbootstrap.com"], 8.8, INK, 12)
    b += code(198, 108, ["my_site/", " |- index.html", " |- css/", " |   bootstrap.min.css", " |- js/", "     bootstrap.bundle", "      .min.js"], 8, 11)
    b += lines(266, 192, ["+ works offline"], 8.8, INK, 13)
    # template
    b += text(14, 222, "Basic template", 9.8, anchor="start", weight="bold", color=P)
    b += box(12, 230, 336, 128, "#fff", GREY, 6, 1)
    b += code(20, 245, ['<!DOCTYPE html>', '<html lang="en">', '<head>', ' <meta charset="UTF-8">',
                        ' <meta name="viewport" content=', '  "width=device-width, initial-scale=1">',
                        ' <link rel="stylesheet" href="css/bootstrap.min.css">',
                        '</head><body> ... content ...',
                        ' <script src="js/bootstrap.bundle.min.js"></script>',
                        '</body></html>'], 7.9, 11.4)
    b += note(12, 366, 336, ["CSS in <head>; JS just before </body>.",
                             "bundle.min.js = Bootstrap JS + Popper."], size=9.4)
    return svg(360, 412, b)


def viewport():
    b = title("The Viewport Meta Tag")
    # without
    b += text(90, 46, "Without viewport tag", 9.8, weight="bold", color=RED)
    b += box(44, 54, 92, 150, "#fff", INK, 10, 1.6)
    b += box(50, 66, 80, 38, REDF, RED, 2, 1)
    for i in range(3):
        b += box(52 + i * 26, 70, 24, 30, "#fff", RED, 1, 0.8)
    b += lines(90, 120, ["tiny desktop page,", "user must zoom"], 8.4, GREY, 12)
    b += lines(90, 220, ["renders at ~980 px", "and shrinks it"], 8.8, INK, 12)
    # with
    b += text(270, 46, "With viewport tag", 9.8, weight="bold", color=GREEN)
    b += box(224, 54, 92, 150, "#fff", INK, 10, 1.6)
    for i in range(3):
        b += box(232, 66 + i * 34, 76, 28, GREENF, GREEN, 3, 1)
        b += text(270, 84 + i * 34, f"Column {i + 1}", 9, color=GREEN)
    b += lines(270, 220, ["uses real device width,", "columns stack"], 8.8, INK, 12)
    b += box(12, 244, 336, 38, PF, P, 6, 1.2)
    b += code(20, 259, ['<meta name="viewport"', '  content="width=device-width, initial-scale=1">'], 8.4, 13)
    b += note(12, 292, 336, ["width=device-width: page width = screen width.",
                             "initial-scale=1: no zoom when the page opens.",
                             "Remove responsiveness: delete this tag, give",
                             ".container a fixed width, use col-4 (no -md)."], size=9.4)
    return svg(360, 366, b)


def features():
    b = title("Major Features of Bootstrap")
    items = [(70, 60, "Responsive", "12-column grid", BLUEF, BLUE),
             (180, 48, "Mobile first", "6 breakpoints", GREENF, GREEN),
             (290, 60, "Components", "navbar, card, ...", ORANGEF, ORANGE),
             (54, 176, "JS plug-ins", "modal, carousel", TEALF, TEAL),
             (306, 176, "Utilities", "spacing, flex...", BLUEF, BLUE),
             (70, 292, "Customisable", "Sass variables", REDF, RED),
             (180, 304, "Icons", "2000+ icons", GREENF, GREEN),
             (290, 292, "Browser", "support, docs", ORANGEF, ORANGE)]
    for x, y, a, c, f, s in items:
        b += line(f"M180 176 L{x} {y}", s, 1.2)
    b += f'<circle cx="180" cy="176" r="42" fill="{P}"/>'
    b += text(180, 173, "Bootstrap", 11, weight="bold", color="#fff")
    b += text(180, 189, "5", 11, weight="bold", color="#fff")
    for x, y, a, c, f, s in items:
        b += box(x - 50, y - 20, 100, 40, f, s, 7, 1.3)
        b += text(x, y - 4, a, 9.6, weight="bold", color=s)
        b += text(x, y + 11, c, 8.6, color=INK)
    b += note(12, 336, 336, ["Free and open source, consistent design, saves",
                             "development time, large community, good docs."], size=9.4)
    return svg(360, 380, b)


def breakpoints():
    b = title("Bootstrap 5 Breakpoints")
    rows = [["Name", "Infix", "Screen width", "Device"],
            ["Extra small", "(none)", "< 576 px", "phone"],
            ["Small", "sm", ">= 576 px", "large phone"],
            ["Medium", "md", ">= 768 px", "tablet"],
            ["Large", "lg", ">= 992 px", "laptop"],
            ["Extra large", "xl", ">= 1200 px", "desktop"],
            ["XX large", "xxl", ">= 1400 px", "large desktop"]]
    b += grid(8, 38, [84, 52, 96, 112], rows, rh=21, size=9)
    # bar
    segs = [(0, 576, "#F1E8FC"), (576, 768, BLUEF), (768, 992, GREENF), (992, 1200, ORANGEF), (1200, 1400, TEALF), (1400, 1600, REDF)]
    for a, c, f in segs:
        x1 = 14 + a * 332 / 1600; w = (c - a) * 332 / 1600
        b += box(x1, 200, w, 22, f, GREY, 0, 0.8)
    for v in (576, 768, 992, 1200, 1400):
        b += text(14 + v * 332 / 1600, 236, str(v), 8.4, color=GREY)
    for a, c, lab in [(0, 576, "xs"), (576, 768, "sm"), (768, 992, "md"), (992, 1200, "lg"), (1200, 1400, "xl"), (1400, 1600, "xxl")]:
        b += text(14 + (a + c) / 2 * 332 / 1600, 215, lab, 9, weight="bold", color=P)
    b += note(12, 250, 336, ["A class works from its breakpoint and UP:",
                             "col-md-6 = half width on tablet and larger,",
                             "full width below 768 px (mobile first).",
                             "Bootstrap 3 had only xs, sm, md, lg."], size=9.4)
    return svg(360, 324, b)


DIAGRAMS = {"web1_jq_syntax": jq_syntax, "web1_selectors": selectors, "web1_events": events,
            "web1_bs_history": bs_history, "web1_responsive": responsive, "web1_setup": setup,
            "web1_viewport": viewport, "web1_features": features, "web1_breakpoints": breakpoints}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
