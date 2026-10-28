"""DI03000061 RWPD - Unit 5 diagrams: utilities and customization."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT
from diagrams_DI03000061_u2 import BSB, BSG, BSR, BSY, BSC, BSGR, BSD


def utility_class():
    b = title("Anatomy of a Spacing Class")
    b += text(180, 62, "m  t  -  3", 30, mono=True, weight="bold", color=P)
    b += line("M120 72 L120 96", BLUE, 1.4) + line("M160 72 L160 96", GREEN, 1.4)
    b += line("M235 72 L235 96", ORANGE, 1.4)
    b += text(120, 110, "property", 9, weight="bold", color=BLUE)
    b += text(120, 124, "m = margin", 8.6, color=GREY)
    b += text(120, 137, "p = padding", 8.6, color=GREY)
    b += text(160, 154, "sides", 9, weight="bold", color=GREEN)
    b += text(160, 168, "t b s e x y (none = all)", 8.6, color=GREY)
    b += text(235, 110, "size", 9, weight="bold", color=ORANGE)
    b += text(235, 124, "0 1 2 3 4 5 auto", 8.6, color=GREY) + text(235, 137, "(for margin)", 8.2, color=GREY)
    rows = [["Examples", "Meaning"],
            ["mt-3", "margin top 1rem"],
            ["px-2", "padding left+right 0.5rem"],
            ["ms-auto", "start margin auto"],
            ["p-md-4", "padding 1.5rem from 768px"]]
    b += grid(10, 184, [120, 222], rows, rh=21, size=8.6)
    b += note(12, 322, 336, ["Sizes: 1 = 0.25rem, 2 = 0.5, 3 = 1, 4 = 1.5, 5 = 3rem.",
                             "Bootstrap 4 used l/r; Bootstrap 5 uses s/e (start/end)."], size=9)
    return svg(360, 368, b)


def group_map():
    b = title("Bootstrap Utility Families")
    rows = [["Utility", "Example class", "Use"],
            ["Spacing", "p-3 ms-auto gap-2", "space in / around"],
            ["Sizing", "w-50 vh-100 ratio-16x9", "width / height"],
            ["Display", "d-none d-md-flex", "show / hide / flow"],
            ["Visibility", "invisible", "hide, keep space"],
            ["Position", "top-0 z-1", "place element"],
            ["Flexbox", "justify-content-center", "row / column lay"],
            ["Border", "border rounded-pill", "edges / corners"],
            ["Background", "bg-primary bg-gradient", "fill colour"],
            ["Opacity", "opacity-50", "transparency"],
            ["Overflow", "overflow-hidden", "clip / scroll"],
            ["Shadow", "shadow-lg", "depth"]]
    b += grid(6, 38, [92, 130, 114], rows, rh=20, size=8.2)
    b += note(12, 294, 336, ["Same pattern everywhere:",
                             "{utility}-{breakpoint}-{value},",
                             "e.g. d-lg-inline-block, p-xl-5."], size=9.2)
    return svg(360, 352, b)


def responsive():
    b = title("Mobile-First Responsive Infix")
    b += text(180, 58, "flex-column  flex-md-row  gap-lg-4", 10.5, mono=True, weight="bold", color=P)
    b += text(180, 76, "{utility}-{breakpoint}-{value}", 9.4, mono=True, color=GREY)
    xs = [(10, "xs", "base class", "applies everywhere"), (100, "sm", ">= 576px", "small"),
          (190, "md", ">= 768px", "tablet"), (280, "lg / xl / xxl", ">= 992px", "desktop")]
    for x, bp, px_, lab in xs:
        w = 80 if x < 190 else 72
        b += box(x, 96, w, 44, BSB, BSB, 7, 0)
        b += text(x + w / 2, 112, bp, 9.5, weight="bold", color="#fff")
        b += text(x + w / 2, 127, px_, 6.8, color="#fff")
    b += rarrow(90, 99, 118, "#999") + rarrow(180, 189, 118, "#999") + rarrow(270, 279, 118, "#999")
    b += box(10, 158, 340, 88, BLUEF, BLUE, 7, 1.2)
    b += text(20, 176, "Cascade (min-width): larger wins", 9.4, anchor="start", weight="bold", color=BLUE)
    b += code(20, 192, ['<div class="p-2 p-md-4">',
                        '  phone: padding 0.5rem (p-2)',
                        '  from 768px: padding 1.5rem (p-md-4)',
                        '</div>'], 8.6, 15)
    b += note(12, 262, 336, ["Classes without a breakpoint apply to ALL sizes;",
                             "{bp}- classes override them from that width up.",
                             "Not responsive: colours, borders, w-*, h-*."], size=9.2)
    return svg(360, 312, b)


def flex_axes():
    b = title("Flexbox Axes and Alignment")
    b += box(30, 46, 300, 130, PF, P, 7, 1.2)
    for i, (x, h) in enumerate([(120, 26), (170, 40), (220, 30)]):
        b += box(x, 96 - h / 2 + 30, 36, h, BSB, BSB, 4, 0)
    b += rarrow(50, 310, 58, BSB)
    b += text(183, 50, "main axis (row) -> justify-content-*", 8.8, weight="bold", color=BSB, anchor="middle")
    ax = line("M40 84 L40 168", BSR, 1.6)
    b += ax + f'<polygon points="40,74 35,86 45,86" fill="{BSR}"/>'
    b += text(52, 152, "cross", 8.8, weight="bold", color=BSR, anchor="start")
    b += text(52, 163, "axis:", 8.8, weight="bold", color=BSR, anchor="start")
    b += text(52, 174, "align-items-*", 8.2, weight="bold", color=BSR, anchor="start")
    rows = [["Main axis", "justify-content-*"],
            ["start center end", "items pushed together"],
            ["space-between", "largest gaps between"],
            ["space-around / evenly", "equal outer space"],
            ["Cross axis", "align-items-*"],
            ["start / center / end", "move all items"],
            ["stretch", "fill the height"],
            ["align-self-*", "override one item"]]
    b += grid(10, 200, [128, 204], rows, rh=19.5, size=8.2)
    b += note(12, 376, 336, ["flex-wrap lets items go to a new line;",
                             "order-*, flex-grow-1, ms-auto tune items.",
                             "In flex-column the two axes swap."])
    return svg(360, 426, b)


def customize_levels():
    b = title("Levels of Bootstrap Customization")
    lv = [("1. CSS variables", ":root { --bs-primary: ...; }", "runtime, no tools", BSC),
          ("2. Sass variables", "$primary: #198754; (before import)", "whole library", BSB),
          ("3. Sass maps + utility API", "map-merge($theme-colors, ...)", "own colours / utils", TEAL),
          ("4. Component variables", "$card-border-radius: 1rem;", "one component", ORANGE),
          ("5. Themes", "packaged set of 1-4 per theme", "site identity", BSG)]
    y = 44
    for t, c, d, col in lv:
        b += box(14, y, 332, 46, "#fff", col, 7, 1.4)
        b += text(26, y + 15, t, 9.4, anchor="start", weight="bold", color=col)
        b += text(26, y + 28, c, 8.2, anchor="start", mono=True, color="#333")
        b += text(26, y + 40, d, 8, anchor="start", color=GREY)
        y += 54
    b += note(12, y + 4, 336, ["Simple -> powerful, top to bottom.",
                             "Bootstrap is !default-driven: your Sass",
                             "values set before import always win."], size=9.2)
    return svg(360, y + 56, b)


def sass_flow():
    b = title("Sass Customization Workflow")
    b += box(10, 46, 160, 84, YEL, "#333", 7, 1.4)
    b += text(90, 62, "my-project/", 9.5, weight="bold")
    b += code(20, 78, ["scss/_custom.scss", "  $primary: #198754;", "  $border-radius: 0.75rem;", '  @import "bootstrap";'], 7.8, 13)
    b += box(200, 46, 150, 52, BSB, BSB, 7, 0)
    b += text(275, 66, "dart-sass", 10, weight="bold", color="#fff")
    b += text(275, 80, "compiler (npm build)", 7.8, color="#fff")
    b += text(275, 92, "scss -> css", 7.8, color="#fff")
    b += rarrow(172, 198, 72, GREY)
    b += box(200, 112, 150, 40, BSG, BSG, 7, 0)
    b += text(275, 128, "css/custom.css", 9.5, weight="bold", color="#fff")
    b += text(275, 142, "Bootstrap with your defaults", 7.2, color="#fff")
    b += line("M275 98 L275 112", BSG, 1.6)
    b += f'<polygon points="275,112 270,104 280,104" fill="{BSG}"/>'
    b += box(10, 158, 340, 34, PF, P, 7, 1.2)
    b += code(22, 172, ['<link href="css/custom.css" rel="stylesheet">'], 8.6, 14)
    b += text(22, 186, "instead of bootstrap.css", 8, anchor="start", color=GREY)
    b += text(180, 218, "Rebuild whenever variables change.", 9, color=GREY)
    b += note(12, 232, 336, ["Dart Sass is the official compiler;",
                             "many editors rebuild on save (VS Code,",
                             "npm scripts). Only the final CSS ships."], size=9.2)
    return svg(360, 282, b)


def themes():
    b = title("Colour Modes and Themes")
    b += box(10, 46, 340, 34, GREY, GREY, 7, 0)
    b += text(180, 60, '<html data-bs-theme="light">  ... or on one section', 8.6, color="#fff")
    b += text(180, 74, "built-in modes: light, dark", 8, color="#fff")
    b += box(10, 90, 160, 96, "#fff", "#bbb", 7, 1.2)
    b += text(90, 106, "light", 9.5, weight="bold")
    b += box(24, 114, 40, 14, BSB, BSB, 3, 0) + text(44, 124, "badge", 6.4, color="#fff")
    b += box(24, 134, 50, 14, "#fff", BSB, 3, 1.2) + text(49, 143, "card", 6.8)
    b += box(24, 154, 34, 14, BSB, BSB, 3, 0) + text(41, 164, "Open", 6.8, color="#fff")
    b += box(190, 90, 160, 96, "#212529", "#555", 7, 1.2)
    b += text(270, 106, "dark", 9.5, weight="bold", color="#fff")
    b += box(204, 114, 40, 14, BSB, BSB, 3, 0) + text(224, 124, "badge", 6.4, color="#fff")
    b += box(204, 134, 50, 14, "#2b3035", "#6c757d", 3, 1.2) + text(229, 143, "card", 6.8, color="#dee2e6")
    b += box(204, 154, 34, 14, BSB, BSB, 3, 0) + text(221, 164, "Open", 6.8, color="#fff")
    b += rarrow(172, 188, 136, GREY)
    b += note(12, 196, 336, ["One attribute switches every variable:",
                             "bg, text, borders, shadows adapt."])
    rows = [["Custom theme", "approach"],
            ["CSS-level", "[data-bs-theme=x] { --bs-... }"],
            ["Sass-level", "one custom build per theme"],
            ["Packaged", "Bootswatch, Start Bootstrap"]]
    b += grid(10, 242, [108, 226], rows, rh=21, size=8.4)
    b += note(12, 324, 336, ["Rule: always style with semantic classes;",
                             "never hard-code hex colours in markup."], size=9.2)
    return svg(360, 370, b)


DIAGRAM_TITLES = {
    "web5_utility_class": ("Anatomy of a Utility Class", utility_class),
    "web5_group_map": ("Bootstrap Utility Families", group_map),
    "web5_responsive": ("Mobile-First Responsive Infix", responsive),
    "web5_flex_axes": ("Flexbox Axes and Alignment", flex_axes),
    "web5_customize_levels": ("Levels of Bootstrap Customization", customize_levels),
    "web5_sass_flow": ("Sass Customization Workflow", sass_flow),
    "web5_themes": ("Colour Modes and Themes", themes),
}

if __name__ == "__main__":
    import subject_DI03000061 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
