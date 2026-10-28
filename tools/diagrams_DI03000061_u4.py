"""DI03000061 RWPD - Unit 4 diagrams: Bootstrap plug-ins."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT
from diagrams_DI03000061_u2 import BSB, BSG, BSR, BSY, BSC, BSGR, BSD
from diagrams_DI03000061_u3 import btn, caret


def plugins():
    b = title("Bootstrap Plug-ins (bootstrap.bundle.js)")
    rows = [["Plug-in", "Data attribute", "Main use"],
            ["Modal", "data-bs-toggle=\"modal\"", "dialog box"],
            ["Dropdown", "data-bs-toggle=\"dropdown\"", "menus"],
            ["Scrollspy", "data-bs-spy=\"scroll\"", "active link on scroll"],
            ["Tab", "data-bs-toggle=\"tab\"", "switch panes"],
            ["Tooltip *", "data-bs-toggle=\"tooltip\"", "hover label"],
            ["Popover *", "data-bs-toggle=\"popover\"", "click box"],
            ["Alert", "data-bs-dismiss=\"alert\"", "close message"],
            ["Button", "data-bs-toggle=\"button\"", "toggle state"],
            ["Collapse", "data-bs-toggle=\"collapse\"", "show / hide"],
            ["Carousel", "data-bs-ride=\"carousel\"", "slideshow"],
            ["Offcanvas", "data-bs-toggle=\"offcanvas\"", "side panel"]]
    b += grid(6, 38, [70, 162, 116], rows, rh=21, size=8.4)
    b += note(12, 300, 336, ["* opt-in: must be created with new bootstrap.X(el).",
                             "Removed: transition (built in), affix (sticky-top).",
                             "Bootstrap 5 needs no jQuery; Popper is in the bundle."], size=9)
    return svg(360, 360, b)


def api():
    b = title("Two Ways to Use a Plug-in")
    b += box(10, 40, 340, 74, BLUEF, BLUE, 7, 1.3)
    b += text(20, 58, "1. Data attributes (no JavaScript)", 10, anchor="start", weight="bold", color=BLUE)
    b += code(20, 74, ['<button data-bs-toggle="collapse"', '        data-bs-target="#box">'], 8.6, 13)
    b += box(10, 124, 340, 136, GREENF, GREEN, 7, 1.3)
    b += text(20, 142, "2. JavaScript API", 10, anchor="start", weight="bold", color=GREEN)
    b += code(20, 158, ['var c = new bootstrap.Collapse(el, {', '          toggle: false });   // options',
                        'c.show();  c.hide();  c.toggle(); // methods',
                        'bootstrap.Collapse.getOrCreateInstance(el);',
                        'el.addEventListener("shown.bs.collapse",',
                        '                    fn);           // events'], 8.4, 15.5)
    b += text(180, 284, "Event names: action.bs.plugin", 10, weight="bold", color=P)
    tl = [(20, "show", BSB), (100, "shown", BSG), (180, "hide", BSY), (260, "hidden", BSR)]
    b += line("M20 318 L340 318", GREY, 1.2)
    for x, l, c in tl:
        b += f'<circle cx="{x + 30}" cy="318" r="5" fill="{c}"/>' + text(x + 30, 306, l, 9.4, weight="bold", color=c)
    b += text(70, 336, "before", 8.4, color=GREY) + text(150, 336, "after anim.", 8.4, color=GREY)
    b += text(230, 336, "before", 8.4, color=GREY) + text(310, 336, "after anim.", 8.4, color=GREY)
    b += note(12, 346, 336, ["e.preventDefault() in show / hide cancels the action."], size=9.2)
    return svg(360, 378, b)


def modal():
    b = title("Modal Dialog Structure")
    b += box(10, 40, 340, 210, "#7A7A7A", "#7A7A7A", 6, 0)
    b += text(20, 56, ".modal-backdrop (dark layer)", 8.6, anchor="start", color="#fff", mono=True)
    b += box(40, 66, 280, 170, "#fff", "#999", 7, 1.2)
    b += line("M40 98 L320 98", "#DDD", 1) + line("M40 196 L320 196", "#DDD", 1)
    b += text(52, 87, "Delete record?", 11, anchor="start", weight="bold")
    b += text(306, 88, "x", 12, color=GREY)
    b += text(52, 120, "Priya Shah will be removed.", 9.4, anchor="start")
    b += text(52, 138, "This cannot be undone.", 9.4, anchor="start", color=GREY)
    b += btn(184, 204, 54, 24, "No", BSGR, size=9) + btn(244, 204, 64, 24, "Delete", BSR, size=9)
    b += text(180, 270, ".modal.fade > .modal-dialog > .modal-content", 8.8, color=P, mono=True)
    b += text(180, 286, "> .modal-header | .modal-body | .modal-footer", 8.8, color=P, mono=True)
    rows = [["Action", "How"], ["Open", "data-bs-toggle=\"modal\" data-bs-target"], ["Close", "data-bs-dismiss=\"modal\", Esc, backdrop"],
            ["Size", "modal-sm / -lg / -xl / -fullscreen"], ["Place", "modal-dialog-centered / -scrollable"],
            ["Static", "data-bs-backdrop=\"static\" keyboard false"]]
    b += grid(10, 298, [60, 280], rows, rh=19, size=8.4)
    return svg(360, 420, b)


def modal_api():
    b = title("Modal: Options, Methods, Events")
    cols = [(10, BLUEF, BLUE, "Options", ["backdrop", " true/false/static", "keyboard", " Esc closes", "focus"]),
            (126, GREENF, GREEN, "Methods", ["show()", "hide()", "toggle()", "handleUpdate()", "dispose()", "getInstance()"]),
            (242, ORANGEF, ORANGE, "Events", ["show.bs.modal", "shown.bs.modal", "hide.bs.modal", "hidden.bs.modal", "hidePrevented"])]
    for x, f, s, h, ls in cols:
        b += box(x, 40, 108, 140, f, s, 7, 1.3)
        b += text(x + 54, 58, h, 10, weight="bold", color=s)
        b += lines(x + 54, 78, ls, 8.6, INK, 17)
    # flow
    b += text(180, 204, "Event flow when a button opens the modal", 9.6, weight="bold", color=P)
    steps = [("click", BSGR), ("show", BSB), ("visible", BSD), ("shown", BSG)]
    for i, (l, c) in enumerate(steps):
        x = 14 + i * 86
        b += btn(x, 214, 72, 26, l, c, size=9)
        if i < 3:
            b += rarrow(x + 73, x + 86, 227)
    b += code(16, 262, ['el.addEventListener("show.bs.modal", function (e) {', '  var btn = e.relatedTarget; // opener button',
                        '  title.textContent = btn.dataset.name;', '});'], 8.4, 13)
    b += note(12, 322, 336, ["relatedTarget lets one modal serve many rows.",
                             "BS3: $(\"#m\").modal(\"show\") with jQuery."], size=9.2)
    return svg(360, 368, b)


def scrollspy():
    b = title("Scrollspy")
    b += box(14, 40, 332, 30, "#F8F9FA", "#DDD", 4, 1)
    labs = ["Story", "Photos", "Route", "Opinion"]
    for i, l in enumerate(labs):
        x = 22 + i * 80
        if i == 1:
            b += box(x, 44, 70, 22, BSB, BSB, 5, 0)
        b += text(x + 35, 59, l, 9.4, color="#fff" if i == 1 else BSB)
    b += text(180, 86, "nav#newsNav (target)", 8.6, color=P, mono=True)
    b += box(14, 94, 230, 170, "#fff", "#BBB", 5, 1.2)
    b += box(232, 100, 8, 158, "#EEE", "#EEE", 4, 0) + box(232, 140, 8, 50, "#AAA", "#AAA", 4, 0)
    secs = [(84, "#s1 Story", "#ccc"), (130, "#s2 Photos", INK), (220, "#s3 Route", "#ccc")]
    b += box(18, 120, 210, 90, "#E7F1FF", "#E7F1FF", 3, 0)
    for y, l, c in secs:
        if y > 94:
            b += text(28, y + 8, l, 10, anchor="start", weight="bold", color=c)
            b += line(f"M28 {y + 18} L200 {y + 18}", "#DDD", 4) + line(f"M28 {y + 30} L170 {y + 30}", "#DDD", 4)
    b += text(250, 132, "visible", 8.8, anchor="start", color=BSB)
    b += text(250, 146, "section", 8.8, anchor="start", color=BSB)
    b += text(250, 160, "-> its link", 8.8, anchor="start", color=BSB)
    b += text(250, 174, "becomes", 8.8, anchor="start", color=BSB)
    b += text(250, 188, ".active", 8.8, anchor="start", color=BSB, mono=True)
    b += code(16, 282, ['<div data-bs-spy="scroll" data-bs-target="#newsNav"', '     tabindex="0" style="height:300px;overflow-y:auto">',
                        '  <section id="s1">..</section>', '</div>'], 8.2, 12.5)
    b += note(12, 340, 336, ["href of each link = id of a section. Options:",
                             "smoothScroll, rootMargin (BS3 offset). Method",
                             "refresh(). Event activate.bs.scrollspy."], size=9.2)
    return svg(360, 400, b)


def tooltip_popover():
    b = title("Tooltip and Popover")
    # tooltip
    b += text(14, 50, "Tooltip", 10.4, anchor="start", weight="bold", color=P)
    b += btn(40, 92, 70, 26, "Hover", BSGR, size=9.4)
    b += box(28, 60, 94, 22, "#222", "#222", 4, 0) + text(75, 75, "Short label", 9, color="#fff")
    b += f'<path d="M70 82 L80 82 L75 88 Z" fill="#222"/>'
    b += lines(140, 66, ["title=\"Short label\"", "hover / focus", "text only (or html)"], 8.6, INK, 15, anchor="start")
    # popover
    b += text(14, 148, "Popover", 10.4, anchor="start", weight="bold", color=P)
    b += box(20, 156, 150, 66, "#fff", "#BBB", 6, 1)
    b += box(21, 157, 148, 22, "#F0F0F0", "#F0F0F0", 5, 0) + text(30, 172, "Last date", 9.6, anchor="start", weight="bold")
    b += text(30, 196, "Fees must be paid", 9, anchor="start") + text(30, 210, "by 30 Nov.", 9, anchor="start")
    b += f'<path d="M85 222 L95 222 L90 228 Z" fill="#fff" stroke="#BBB"/>'
    b += btn(55, 232, 70, 26, "Click", BSR, size=9.4)
    b += lines(190, 166, ["data-bs-title", "data-bs-content", "click (default)", "focus = dismiss on", "next click"], 8.6, INK, 15, anchor="start")
    rows = [["", "Tooltip", "Popover"], ["Content", "title only", "title + content"], ["Trigger", "hover focus", "click"],
            ["Init", "new bootstrap.Tooltip", "new bootstrap.Popover"], ["Events", "*.bs.tooltip", "*.bs.popover"]]
    b += grid(8, 270, [74, 132, 138], rows, rh=19, size=8.4)
    b += note(12, 372, 336, ["Both are opt-in, use Popper, and share options:",
                             "placement, trigger, html, delay, offset, container."], size=9.2)
    return svg(360, 418, b)


def collapse():
    b = title("Collapse and Accordion")
    b += btn(14, 42, 110, 26, "Read more", BSB, size=9.4)
    b += rarrow(126, 150, 55)
    states = [(156, ".collapse", "hidden", 0), (220, ".collapsing", "animating", 14), (288, ".collapse.show", "visible", 30)]
    for x, c, l, h in states:
        b += box(x, 44, 56, 32, "#fff", "#BBB", 4, 1)
        if h:
            b += box(x + 4, 48, 48, h * 24 / 30, "#CFE2FF", "#CFE2FF", 2, 0)
        b += text(x + 28, 90, c, 7.8, color=P, mono=True) + text(x + 28, 102, l, 8, color=GREY)
    b += text(14, 126, "Accordion (data-bs-parent)", 10, anchor="start", weight="bold", color=P)
    items = [("Who can apply?", False), ("How is merit decided?", True), ("Course duration?", False)]
    y = 134
    for q, op in items:
        b += box(14, y, 332, 26, "#CFE2FF" if op else "#fff", "#CCC", 0, 1)
        b += text(24, y + 17, q, 9.4, anchor="start", color="#052C65" if op else INK)
        b += caret(330, y + 13, INK, 4, up=op)
        y += 26
        if op:
            b += box(14, y, 332, 30, "#fff", "#CCC", 0, 1) + text(24, y + 19, "By SSC marks (only this one is open).", 9, anchor="start")
            y += 30
    b += code(16, 252, ['<div class="accordion" id="faq">', '  <button class="accordion-button" data-bs-toggle=',
                        '    "collapse" data-bs-target="#q1">', '  <div id="q1" class="accordion-collapse collapse"',
                        '    data-bs-parent="#faq">..</div>'], 8.2, 12.5)
    b += note(12, 322, 336, ["Options: parent, toggle. Methods: show() hide()",
                             "toggle(). Events: show/shown/hide/hidden.bs.collapse.",
                             ".collapse-horizontal animates width."], size=9.2)
    return svg(360, 382, b)


def carousel():
    b = title("Carousel Structure")
    b += box(14, 40, 332, 170, "#E07B00", "#E07B00", 7, 0)
    b += f'<path d="M14 210 L120 120 L200 180 L250 140 L346 210 Z" fill="#fff" fill-opacity="0.25"/>'
    b += f'<circle cx="280" cy="80" r="22" fill="#fff" fill-opacity="0.35"/>'
    b += box(100, 140, 160, 40, "#000", "#000", 6, 0).replace('fill="#000"', 'fill="#000" fill-opacity="0.45"', 1)
    b += text(180, 157, "Rani ki Vav", 10.4, weight="bold", color="#fff") + text(180, 172, "Stepwell in Patan", 8.6, color="#fff")
    b += f'<path d="M36 112 L28 125 L36 138" fill="none" stroke="#fff" stroke-width="2.4"/>'
    b += f'<path d="M324 112 L332 125 L324 138" fill="none" stroke="#fff" stroke-width="2.4"/>'
    for i in range(7):
        b += line(f"M{124 + i * 17} 196 L{136 + i * 17} 196", "#fff", 3 if i == 2 else 2)
    b += text(180, 128, ".carousel-caption", 8.4, color="#fff", mono=True)
    b += text(14, 226, "arrows: .carousel-control-prev / -next", 8.4, anchor="start", color=P, mono=True)
    b += text(14, 240, "bars: .carousel-indicators", 8.4, anchor="start", color=P, mono=True)
    b += code(16, 260, ['<div id="g" class="carousel slide" data-bs-ride="carousel">', '  <div class="carousel-indicators">..</div>',
                        '  <div class="carousel-inner">', '    <div class="carousel-item active"><img ..>',
                        '      <div class="carousel-caption">..</div></div>', '  </div>',
                        '  <button class="carousel-control-prev"', '    data-bs-target="#g" data-bs-slide="prev">'], 8.0, 12)
    rows = [["Part", "Members"], ["Options", "interval, ride, pause, wrap, keyboard, touch"], ["Methods", "cycle() pause() prev() next() to(n)"],
            ["Events", "slide.bs.carousel, slid.bs.carousel (e.to)"], ["Effect", ".slide or .carousel-fade"]]
    b += grid(8, 364, [62, 282], rows, rh=19, size=8.4)
    return svg(360, 466, b)


def affix():
    b = title("Affix (BS3) and Sticky (BS5)")
    for k, (x, lab, scrolled) in enumerate([(14, "Before scrolling", False), (190, "After scrolling", True)]):
        b += text(x + 78, 50, lab, 9.6, weight="bold")
        b += box(x, 58, 156, 190, "#fff", "#999", 5, 1.2)
        y = 62
        if not scrolled:
            b += box(x + 4, y, 148, 34, BSB, BSB, 3, 0) + text(x + 78, y + 21, "Header", 9.4, color="#fff")
            y += 38
        b += box(x + 4, y, 148, 22, BSD, BSD, 3, 0) + text(x + 78, y + 15, "Menu (sticky-top)", 8.8, color="#fff")
        y += 26
        start = 1 if not scrolled else 4
        while y < 222:
            b += box(x + 8, y, 140, 22, "#F3F3F3", "#DDD", 3, 1) + text(x + 16, y + 15, f"Post {start}", 8.6, anchor="start")
            y += 26
            start += 1
        if scrolled:
            b += text(x + 78, 260, "menu stays at top", 8.8, color=P)
    rows = [["Bootstrap 3 affix", "Bootstrap 5"], ["data-spy=\"affix\"", ".sticky-top / .sticky-bottom"],
            ["data-offset-top=\"200\"", "CSS position: sticky; top: 0"], [".affix-top / .affix", ".sticky-md-top (responsive)"],
            ["needs JavaScript", "pure CSS (scroll event for extras)"]]
    b += grid(8, 274, [140, 204], rows, rh=19, size=8.4)
    b += note(12, 378, 336, ["Affix was removed in Bootstrap 4; .fixed-top is always",
                             "fixed, .sticky-top sticks only after reaching the top."], size=9)
    return svg(360, 424, b)


DIAGRAMS = {"web4_plugins": plugins, "web4_api": api, "web4_modal": modal, "web4_modal_api": modal_api,
            "web4_scrollspy": scrollspy, "web4_tooltip_popover": tooltip_popover, "web4_collapse": collapse,
            "web4_carousel": carousel, "web4_affix": affix}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
