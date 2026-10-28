"""DI04000021 OOP-Java - Unit 4 diagrams: exceptions and collections."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def error_types():
    b = title("Three Kinds of Errors")
    def row(y, t, ex, c, cf):
        s = box(12, y, 108, 30, cf, c, 7, 1.2)
        s += text(66, y + 19, t, 9.4, weight="bold", color=c, anchor="middle")
        s += code(132, y + 13, [ex], 8.6, 14)
        return s
    b += row(48, "compile-time", 'int n = "ten";  // javac stops', RED, REDF)
    b += row(90, "runtime", "int x = 5 / 0;  // exception!", ORANGE, ORANGEF)
    b += row(132, "logical", "avg = a + b / 2;  // wrong!", P, PF)
    b += text(12, 188, "when it appears", 9.2, weight="bold", color=GREY, anchor="start")
    b += grid(12, 198, [96, 236], [
        ["compile-time", "before the program runs"],
        ["runtime", "crashes while running"],
        ["logical", "runs - wrong output"],
    ], rh=20, size=8.4)
    b += note(12, 266, 336, ["Only runtime errors become EXCEPTIONS",
                             "objects the JVM throws and programs",
                             "can catch and recover from."], size=9.2)
    return svg(360, 316, b)


def hierarchy():
    b = title("Exception Hierarchy (simplified)")
    def bx(x, y, w, t, c=BLUE, cf=BLUEF):
        return box(x, y, w, 22, cf, c, 6, 1.1) + text(x + w / 2, y + 14, t, 8.6, weight="bold", color=c)
    def darrow(x, y1, y2, c=GREY):
        return line(f"M{x} {y1} L{x} {y2}", c, 1.3) + f'<polygon points="{x},{y2-4} {x-4},{y2+4} {x+4},{y2+4}" fill="{c}"/>'
    b += bx(140, 46, 80, "Throwable", GREY, TEALF)
    b += bx(30, 86, 60, "Error", RED, REDF) + bx(224, 86, 106, "Exception", BLUE, BLUEF)
    b += darrow(60, 79, 82) + darrow(277, 79, 82)
    b += bx(158, 126, 172, "RuntimeException", ORANGE, ORANGEF)
    b += darrow(244, 108, 122)
    b += text(60, 76, "serious - not caught", 7.6, color=RED)
    for i, n in enumerate(["ArithmeticException", "NullPointerException",
                           "ArrayIndexOutOfBounds", "NumberFormatException",
                           "IllegalArgument..."]):
        b += box(158, 158 + i * 24, 172, 20, YEL, ORANGE, 5, 1)
        b += text(244, 172 + i * 24, n, 8.2, color=P, anchor="middle")
    b += note(12, 300, 336, ["RuntimeException children = UNCHECKED:",
                             "javac does not force you to catch them.",
                             "Other Exception children = CHECKED:",
                             "javac forces try-catch or throws."], size=9.0)
    return svg(360, 380, b)


def try_flow():
    b = title("Control Flow: try / catch / finally")
    b += text(80, 54, "no exception", 9.4, weight="bold", color=GREEN)
    b += text(280, 54, "exception thrown", 9.4, weight="bold", color=RED)
    def path(x, c, cf, steps):
        s = ""
        y = 66
        for t in steps:
            s += box(x, y, 120, 22, cf, c, 6, 1.1)
            s += text(x + 60, y + 14, t, 8.6, color=c, weight="bold")
            y += 34
        return s, y
    s1, y1 = path(20, GREEN, GREENF, ["try block", "skip catch", "finally", "rest of main"])
    b += s1
    s2, y2 = path(220, RED, REDF, ["try (stops mid-way)", "catch block", "finally", "rest of main"])
    b += s2
    for x in (80, 280):
        for yy in range(88, 88 + 3 * 34, 34):
            b += line(f"M{x} {yy} L{x} {yy+12}", GREY, 1.3)
            b += f'<polygon points="{x},{yy+8} {x-3},{yy+16} {x+3},{yy+16}" fill="{GREY}"/>'
    b += note(12, y1 + 12, 336, ["finally runs on BOTH paths - it is the",
                                 "guaranteed cleanup point (also runs",
                                 "even if nothing catches the error)."], size=9.2)
    return svg(360, y1 + 82, b)


def throw_vs_throws():
    b = title("throw vs throws")
    b += box(12, 46, 160, 120, REDF, RED, 7, 1.2)
    b += text(92, 64, "throw", 10, weight="bold", color=RED, anchor="middle")
    b += code(24, 80, ["// inside the body:", "throw new", "  IllegalArgument",
      "    Exception(\"bad\");", "// does the raising"], 8.4, 13.5)
    b += box(188, 46, 160, 120, BLUEF, BLUE, 7, 1.2)
    b += text(268, 64, "throws", 10, weight="bold", color=BLUE, anchor="middle")
    b += code(200, 80, ["// in the header:", "void f(int x)", "  throws Exception {",
      "  ...", "// does the warning"], 8.4, 13.5)
    b += grid(12, 174, [86, 230], [
        ["throw", "raises one exception object"],
        ["throws", "may list several, separated by ,"],
    ], rh=20, size=8.4)
    b += note(12, 222, 336, ["throw = an ACTION (statement in the body)",
                             "throws = a PROMISE (clause in the header)",
                             "A checked exception in throws forces every",
                             "caller to catch it or re-declare it."], size=9.2)
    return svg(360, 314, b)


def catch_order():
    b = title("Multiple catch: First Match Wins")
    b += code(14, 44, ["try { ... }",
                       "} catch (NullPointerException e) {",
                       "} catch (RuntimeException e) {",
                       "} catch (Exception e) {",
                       "}"], 8.6, 15)
    ys = [59, 74, 89]
    labels = ["is it a NPE? -> yes, RUN", "else: RuntimeException?", "else: any Exception"]
    cols = [GREEN, ORANGE, GREY]
    for y, t, c in zip(ys, labels, cols):
        b += line("M222 " + str(y) + " L244 " + str(y), GREY, 1.2, dash="4 3")
        b += f'<polygon points="244,{y} 238,{y-3} 238,{y+3}" fill="{GREY}"/>'
        b += text(250, y + 3, t, 8.2, color=c)
    b += text(180, 122, "matching walk is TOP to BOTTOM", 9.0, weight="bold", color=P)
    b += box(12, 134, 336, 66, REDF, RED, 7, 1.2)
    b += code(24, 152, ["} catch (Exception e) {  // too early!",
                        "} catch (NullPointerException e) {",
                        "  // javac ERROR: already caught",
                        "}"], 8.4, 14)
    b += note(12, 220, 336, ["A parent catch placed first swallows all;",
                             "javac rejects the unreachable children.",
                             "Order: most specific ... most general."], size=9.2)
    return svg(360, 286, b)


def collections_hierarchy():
    b = title("Collections Framework: Overview")
    def bx(x, y, w, t, c=BLUE, cf=BLUEF, iface=False):
        dash = (", dash" ,)  # placeholder
        return box(x, y, w, 22, cf, c, 6, 1.1) + text(x + w / 2, y + 14, t, 8.6, weight="bold", color=c)
    def darrow(x, y1, y2, c=GREY):
        return line(f"M{x} {y1} L{x} {y2}", c, 1.3) + f'<polygon points="{x},{y2-4} {x-4},{y2+4} {x+4},{y2+4}" fill="{c}"/>'
    b += bx(128, 46, 104, "<<Collection>>", GREEN, GREENF)
    b += text(180, 42, "interface", 7.8, color=GREY, anchor="middle")
    b += bx(36, 90, 90, "<<List>>", GREEN, GREENF) + bx(234, 90, 90, "<<Set>>", GREEN, GREENF)
    b += darrow(81, 75, 86) + darrow(279, 75, 86)
    b += bx(36, 132, 90, "ArrayList", BLUE, BLUEF) + bx(234, 132, 90, "HashSet", BLUE, BLUEF)
    b += darrow(81, 112, 128) + darrow(279, 112, 128)
    b += text(81, 176, "ordered, duplicates OK", 8.0, color=BLUE)
    b += text(279, 176, "unique, no fixed order", 8.0, color=BLUE)
    b += grid(12, 190, [96, 240], [
        ["ArrayList", "get(i), add, remove, search"],
        ["HashSet", "unique members, fast contains"],
    ], rh=20, size=8.4)
    b += note(12, 250, 336, ["Also in the family: Map (key -> value),",
                             "Queue, LinkedList, TreeSet ... Same",
                             "ideas: interfaces on top, ready-made",
                             "classes below, for-each works on all."], size=9.0)
    return svg(360, 340, b)


def list_vs_set():
    b = title("ArrayList vs HashSet")
    b += grid(8, 40, [96, 118, 118], [
        ["aspect", "ArrayList", "HashSet"],
        ["interface", "List", "Set"],
        ["duplicates", "allowed", "rejected"],
        ["order kept?", "insertion order", "no guarantee"],
        ["position", "get(i), set(i)", "no index"],
        ["best for", "ordered records", "unique members"],
        ["search", "scan (slow)", "hash (fast)"],
    ], rh=20, size=8.4)
    b += code(14, 212, ["list: [tea, tea, milk]",
                        "set:  [tea, milk]"], 8.6, 15)
    b += note(12, 262, 336, ["Both are created with new, filled with",
                             "add(), walked with for-each - pick by",
                             "duplicates + order, not by syntax."], size=9.2)
    return svg(360, 330, b)


DIAGRAM_TITLES = {
    "jv4_error_types": ("Three Kinds of Errors", error_types),
    "jv4_hierarchy": ("Exception Hierarchy (simplified)", hierarchy),
    "jv4_try_flow": ("Control Flow: try / catch / finally", try_flow),
    "jv4_throw_throws": ("throw vs throws", throw_vs_throws),
    "jv4_catch_order": ("Multiple catch: First Match Wins", catch_order),
    "jv4_collections": ("Collections Framework: Overview", collections_hierarchy),
    "jv4_list_vs_set": ("ArrayList vs HashSet", list_vs_set),
}

if __name__ == "__main__":
    import subject_DI04000021 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
