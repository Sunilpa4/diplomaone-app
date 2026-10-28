"""DI04007011 Introduction to Web Development - Unit 1 diagrams: Introduction to PHP."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def client_server():
    b = title("Client-Server: One Request Cycle")
    b += box(12, 50, 96, 56, BLUEF, BLUE, 8, 1.2)
    b += text(60, 72, "CLIENT", 9.5, weight="bold", color=BLUE)
    b += text(60, 86, "browser", 8.4)
    b += text(60, 98, "(Chrome...)", 7.6, color=GREY)
    b += box(252, 50, 96, 56, GREENF, GREEN, 8, 1.2)
    b += text(300, 66, "SERVER", 9.5, weight="bold", color=GREEN)
    b += text(300, 80, "Apache + PHP", 8.4)
    b += text(300, 92, "runs the script", 7.6, color=GREY)
    b += rarrow(112, 248, 62)
    b += text(180, 54, "1. HTTP request: hello.php", 7.8)
    b += text(180, 128, "3. pure HTML comes back", 7.8)
    b += line("M248 140 L118 140", INK, 1.6) + arrowhead(112, 140, 180, 7, INK)
    b += box(132, 116, 96, 34, ORANGEF, ORANGE, 7, 1.2)
    b += text(180, 130, "2. PHP engine", 8.2, weight="bold", color=ORANGE)
    b += text(180, 142, "executes <?php ?>", 7.6)
    b += down(300, 106, 116)
    b += down(156, 150, 150)  # dummy short segment, replaced by note below
    b += note(12, 176, 336, ["The browser NEVER sees PHP source -",
                             "only the HTML it echoes. Server-side",
                             "means the logic (and secrets) stay home."], size=9.2)
    return svg(360, 236, b)


def tier3():
    b = title("3-Tier Architecture of a Web App")
    tiers = [("PRESENTATION", "browser renders HTML/CSS", BLUEF, BLUE),
             ("APPLICATION", "Apache + PHP: business logic", GREENF, GREEN),
             ("DATA", "MySQL tables, files", ORANGEF, ORANGE)]
    for i, (h, s, f, st) in enumerate(tiers):
        y = 48 + i * 62
        b += box(30, y, 300, 44, f, st, 8, 1.2)
        b += text(180, y + 19, h, 9.5, weight="bold", color=st)
        b += text(180, y + 33, s, 8.4)
        if i < 2:
            b += down(150, y + 44, y + 62)
            b += line("M210 %d L210 %d" % (y + 62, y + 44), INK, 1.6) + arrowhead(210, y + 44, -90, 7, INK)
    b += note(30, 240, 300, ["request flows DOWN the tiers;",
                             "response bubbles back UP.",
                             "Development: one laptop hosts all three."], size=9.2)
    return svg(360, 296, b)


def xampp():
    b = title("XAMPP: The Whole Lab in One Install")
    chips = [("X", "any OS"), ("A", "Apache"), ("M", "MariaDB"), ("P", "PHP"), ("P", "Perl")]
    for i, (c, m) in enumerate(chips):
        x = 18 + i * 66
        b += box(x, 50, 58, 40, PF, P, 8, 1.2)
        b += text(x + 29, 66, c, 13, weight="bold", color=P)
        b += text(x + 29, 81, m, 7.6)
    steps = ["1. install XAMPP (apachefriends.org)",
             "2. control panel  ->  Start Apache",
             "3. save hello.php in htdocs/",
             "4. browse http://localhost/hello.php"]
    y = 108
    for s_ in steps:
        b += text(16, y + 8, s_, 8.6, anchor="start")
        y += 18
    b += note(12, 188, 336, ["Nothing goes live until Apache is green;",
                             "404? file not under htdocs. Blank page?",
                             "check PHP tags, then Apache error log."], size=9.0)
    return svg(360, 246, b)


def embed():
    b = title("Embedding PHP Inside HTML")
    src = ["<h1>Bus Booking</h1>",
           "<p>Today: <?php echo date('d M'); ?></p>",
           "<?php",
           "  $seats = 40 - 3;",
           "  echo \"<b>Seats left: $seats</b>\";",
           "?>"]
    b += code(14, 58, src, size=7.8, lh=13)
    b += text(14, 48, "page.php  (what you write)", 8.2, anchor="start", weight="bold", color=P)
    b += rarrow(250, 336, 92)
    out = ["Bus Booking (as h1)", "Today: 29 Oct", "Seats left: 37 (bold)"]
    b += box(24, 150, 312, 62, GREENF, GREEN, 8, 1.2)
    b += text(180, 166, "BROWSER RECEIVES (pure HTML)", 8.4, weight="bold", color=GREEN)
    b += text(180, 182, out[0] + "   |   " + out[1], 8.2)
    b += text(180, 198, out[2], 8.2)
    b += note(12, 224, 336, ["<?php ... ?> islands can appear anywhere;",
                             "the engine replaces each with its output,",
                             "then ships one flat HTML document."], size=9.0)
    return svg(360, 284, b)


def datatypes():
    b = title("PHP Data Types (Loosely Typed)")
    b += grid(12, 44, [96, 110, 130], [
        ["type", "example", "notes"],
        ["int", "42, -7", "whole numbers"],
        ["float", "3.14, 2e3", "aka double"],
        ["string", "\"hi\", 'yo'", "quotes both work"],
        ["bool", "true, false", "logic values"],
        ["NULL", "no value yet", "case-insensitive"],
        ["array", "[1,2,3]", "unit 2 in depth"],
        ["object", "new Class()", "unit 5 (MVC)"],
    ], rh=19, size=7.8)
    b += note(12, 208, 336, ["No declaration of types: $x = 5; makes an",
                             "int, $x = \"five\"; turns it into a string.",
                             "var_dump($x) reveals type AND value."], size=9.2)
    return svg(360, 268, b)


def operators():
    b = title("PHP Operator Families")
    b += grid(12, 44, [92, 132, 112], [
        ["family", "symbols", "use"],
        ["arithmetic", "+ - * / % **", "math on numbers"],
        ["assignment", "= += .= ", "store into vars"],
        ["comparison", "== === != < >  <=>", "test values"],
        ["logical", "&& || ! and or", "combine tests"],
        ["string", ".  .=", "glue text"],
        ["incr/decr", "++$i  $i--", "loop counters"],
    ], rh=19, size=7.8)
    b += box(12, 188, 336, 36, ORANGEF, ORANGE, 7, 1.2)
    b += text(180, 203, "== loose (5 == \"5\" is true)   === strict (also types)", 8.2, weight="bold", color=ORANGE)
    b += text(180, 216, "always prefer === in form checks", 7.8)
    b += note(12, 236, 336, ["Spaceship <=> returns -1, 0 or 1 - the",
                             "heart of custom sorting callbacks."], size=9.2)
    return svg(360, 296, b)


def ifelif():
    b = title("if - elseif - else Flow")
    b += terminal(180, 44, "evaluate", w=84, h=26)
    b += down(180, 57, 76)
    b += decision(180, 106, "cond1 ?", w=86, h=44)
    b += down(140, 128, 128)  # grid alignment helper (harmless)
    b += rbox(60, 150, 96, 30, "do A", fill=GREENF, stroke=GREEN, size=9)
    b += line("M137 106 L108 146", INK, 1.4) + arrowhead(108, 146, -125, 6, INK)
    b += text(118, 122, "true", 7.6, color=GREEN)
    b += decision(180, 176, "cond2 ?", w=86, h=44)
    b += down(180, 128, 154)
    b += text(192, 145, "false", 7.6, color=RED)
    b += rbox(300, 150, 96, 30, "do B", fill=GREENF, stroke=GREEN, size=9)
    b += line("M223 176 L252 154", INK, 1.4) + arrowhead(252, 154, -55, 6, INK)
    b += text(246, 186, "true", 7.6, color=GREEN)
    b += rbox(300, 216, 96, 30, "else: default", fill=PF, stroke=P, size=9)
    b += down(180, 198, 216)
    b += line("M180 216 L252 216", INK, 1.4) + arrowhead(252, 216, 0, 6, INK)
    b += text(180, 208, "false", 7.6, color=RED)
    b += down(60, 165, 258)  # do A to merge
    b += line("M60 258 L180 258", INK, 1.4)
    b += down(300, 231, 258)
    b += line("M300 258 L180 258", INK, 1.4)
    b += terminal(180, 276, "continue", w=84, h=26)
    b += down(180, 258, 263)
    return svg(360, 296, b)


def loops():
    b = title("Four Loops, Four Personalities")
    cards = [("for", "known count", "for ($i=1; $i<=5; $i++)"),
             ("while", "pre-checked", "while ($row = fetch())"),
             ("do-while", "runs once MINIMUM", "do {...} while ($more);"),
             ("foreach", "arrays (unit 2)", "foreach ($a as $v)")]
    for i, (h, sub, syn) in enumerate(cards):
        x = 12 + (i % 2) * 174
        y = 48 + (i // 2) * 66
        b += box(x, y, 162, 56, BLUEF if i % 3 else GREENF, BLUE if i % 3 else GREEN, 8, 1.2)
        b += text(x + 81, y + 17, h, 9.5, weight="bold", color=BLUE if i % 3 else GREEN)
        b += text(x + 81, y + 31, sub, 7.8)
        b += text(x + 81, y + 46, syn, 7.4, mono=True, color=GREY)
    b += note(12, 188, 336, ["break = exit the loop now;",
                             "continue = skip to next lap.",
                             "foreach is PHP's star player - forms,",
                             "rows, arrays all stream through it."], size=9.2)
    return svg(360, 272, b)


ALL = {"wd1_client_server": client_server, "wd1_3tier": tier3, "wd1_xampp": xampp,
       "wd1_embed": embed, "wd1_datatypes": datatypes, "wd1_operators": operators,
       "wd1_ifelif": ifelif, "wd1_loops": loops}

if __name__ == "__main__":
    import subject_DI04007011 as S
    for k, fn in ALL.items():
        with open(os.path.join(S.DIAG_DIR, k + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(ALL))
