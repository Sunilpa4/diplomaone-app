"""DI04000021 OOP-Java - Unit 1 diagrams."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def jdk_jre_jvm():
    b = title("JDK, JRE and JVM")
    b += box(20, 40, 320, 250, YEL, ORANGE, 10, 1.5)
    b += text(180, 62, "JDK = Java Development Kit", 11.5, weight="bold", color=ORANGE)
    b += text(180, 78, "(for the programmer: write + compile)", 8.5, color=GREY)
    b += box(40, 90, 280, 190, BLUEF, BLUE, 9, 1.5)
    b += text(180, 112, "JRE = Java Runtime Environment", 10.5, weight="bold", color=BLUE)
    b += text(180, 128, "(tools ready to RUN a program)", 8.5, color=GREY)
    b += box(60, 140, 240, 130, GREENF, GREEN, 8, 1.5)
    b += text(180, 162, "JVM = Java Virtual Machine", 10.5, weight="bold", color=GREEN)
    b += text(180, 178, "(executes the byte code)", 8.5, color=GREY)
    rows = [["JDK", "javac, java, debugger + JRE"],
            ["JRE", "class libraries + JVM"],
            ["JVM", "byte code -> machine code"]]
    b += grid(70, 190, [60, 172], rows, rh=20, size=8.5)
    b += note(12, 300, 336, ["Install only the JDK - it already",
                             "contains the JRE and the JVM."], size=9.2)
    return svg(360, 344, b)


def wora():
    b = title("Write Once, Run Anywhere (byte code)")
    b += box(10, 48, 100, 44, BLUEF, BLUE, 7, 1.3)
    b += text(60, 66, "Main.java", 9.5, weight="bold", color=BLUE)
    b += text(60, 80, "source code", 7.8, color=GREY)
    b += rarrow(112, 148, 70, GREY)
    b += text(130, 62, "javac", 8.5, weight="bold", color=GREY)
    b += box(150, 48, 110, 44, PF, P, 7, 1.3)
    b += text(205, 66, "Main.class", 9.5, weight="bold", color=P)
    b += text(205, 80, "byte code", 7.8, color=GREY)
    b += rarrow(262, 300, 70, GREY)
    b += box(296, 48, 54, 44, GREENF, GREEN, 7, 1.3)
    b += text(323, 70, "JVM", 10, weight="bold", color=GREEN)
    rows = [["OS", "its own JVM runs the same .class"],
            ["Windows", "Windows JVM"],
            ["Linux", "Linux JVM"],
            ["Mac", "Mac JVM"]]
    b += grid(60, 110, [70, 222], rows, rh=20, size=8.5)
    b += box(10, 218, 340, 56, GREENF, GREEN, 7, 1.2)
    b += text(20, 236, "The byte code is platform independent:", 9.2, anchor="start", weight="bold", color=GREEN)
    b += text(20, 252, "compile once anywhere, run on every OS.", 9.2, anchor="start", color="#333")
    b += text(20, 266, "Only the JVM is different for each OS.", 9.2, anchor="start", color="#333")
    b += note(12, 296, 336, ["C/C++ compile to machine code for one OS;",
                             "Java compiles to byte code for all OSes."], size=9.2)
    return svg(360, 340, b)


def structure():
    b = title("Structure of a Java Program")
    b += box(10, 40, 340, 176, "#fff", "#999", 6, 1.2)
    b += code(20, 56, ["// File: Main.java", "class Main {",
                       "  public static void main(String[] a) {",
                       '    System.out.println("Hello");', "  }", "}"], 9, 16)
    tags = [("class declaration; file name = class name", 56, BLUE),
            ("method where execution starts", 88, GREEN),
            ("statement that prints a line", 104, ORANGE)]
    for t, y, c in tags:
        b += f'<circle cx="352" cy="{y + 21}" r="4" fill="{c}"/>'
    b += f'<circle cx="352" cy="{56 + 0}" r="4" fill="{BLUE}"/>'
    lbl = [(BLUE, "class: container of the whole program", 232),
           (GREEN, "main(): starting point (public static void)", 256),
           (ORANGE, "every statement ends with ;", 280)]
    for c, t, y in lbl:
        b += f'<circle cx="20" cy="{y - 4}" r="4" fill="{c}"/>' + text(32, y, t, 9, anchor="start", color="#333")
    b += text(20, 306, "public: visible everywhere   static: no object needed", 8.6, anchor="start", color=GREY)
    b += text(20, 320, "void: returns nothing   String[] a: command-line args", 8.6, anchor="start", color=GREY)
    b += note(12, 332, 336, ["Java is case sensitive: Main != main.", "Save as Main.java for class Main."], size=9.2)
    return svg(360, 380, b)


def datatypes():
    b = title("Primitive Data Types of Java (8)")
    rows = [["Type", "Size", "Example"],
            ["byte", "1 B", "byte r = 7;"],
            ["short", "2 B", "short s = 400;"],
            ["int", "4 B", "int m = 452;"],
            ["long", "8 B", "long p = 9876543210L;"],
            ["float", "4 B", "float per = 78.5f;"],
            ["double", "8 B", "double cg = 8.25;"],
            ["char", "2 B", "char c = 'A';"],
            ["boolean", "~1 bit", "boolean ok = true;"]]
    b += grid(10, 40, [70, 52, 222], rows, rh=21, size=8.6)
    b += note(12, 224, 336, ["Suffixes: 9876543210L for long, 78.5f for float.",
                             "A plain decimal like 8.25 is double.",
                             "Strings are NOT primitive: String is a class."], size=9.2)
    return svg(360, 282, b)


def casting():
    b = title("Type Conversion and Casting")
    b += text(180, 56, "Widening - automatic, no data loss", 10, weight="bold", color=GREEN)
    ch = ["byte", "short", "int", "long", "float", "double"]
    for i, t in enumerate(ch):
        b += rbox(35 + 58 * i, 96, 48, 26, t, GREENF, GREEN, 9)
        if i:
            b += rarrow(35 + 58 * i - 30, 35 + 58 * i - 24, 96, GREY)
    b += text(180, 128, "int i = ch;   long l = i;   float f = l;", 8.8, mono=True, color="#333")
    b += text(180, 162, "Narrowing - manual cast, may lose data", 10, weight="bold", color=RED)
    b += rbox(90, 196, 60, 26, "double", REDF, RED, 9)
    b += rbox(268, 196, 60, 26, "int", REDF, RED, 9)
    b += rarrow(122, 236, 196, GREY)
    b += text(179, 190, "(int) cast needed", 8.2, weight="bold", color=RED)
    b += code(70, 232, ["int r = (int) 9.7;   // 9", "byte b = (byte) 130; // -126!"], 8.8, 15)
    rows = [["Rule", "Meaning"],
            ["small -> large", "done by Java itself"],
            ["large -> small", "you must write (type)"],
            ["char <-> int", "uses the character code"]]
    b += grid(10, 296, [128, 206], rows, rh=20, size=8.4)
    return svg(360, 420, b)


def operators():
    b = title("Operators in Java")
    rows = [["Group", "Symbols", "Example"],
            ["Arithmetic", "+ - * / %", "sum = a + b;"],
            ["Relational", "< > <= >= == !=", "a > b -> true"],
            ["Logical", "&& || !", "(a>5) && (b<5)"],
            ["Assignment", "= += -= *= /= %=", "sum += m;"],
            ["Conditional", "? :", "max = a>b ? a : b;"],
            ["Inc / Dec", "++ --", "i++  ++i"],
            ["Bitwise", "& | ^ << >>", "a & b"]]
    b += grid(6, 38, [86, 108, 148], rows, rh=21, size=8.4)
    b += code(16, 222, ["int c = a++;  // c=10, then a=11", "int d = ++a;  // a=12, then d=12"], 8.8, 15)
    b += note(12, 260, 336, ["Postfix uses the old value, prefix the new.",
                             "== compares values; use equals() for String.",
                             "% gives the remainder (17 % 5 = 2)."], size=9.2)
    return svg(360, 336, b)


def loops():
    b = title("Control Flow: Selection and Loops")
    rows = [["Loop", "Test", "Use when"],
            ["for", "before body", "count is known"],
            ["while", "before body", "count unknown"],
            ["do-while", "after body", "run at least once"]]
    b += text(180, 56, "Loops", 10.5, weight="bold", color=P)
    b += grid(16, 66, [86, 100, 148], rows, rh=21, size=8.6)
    rows2 = [["Selection", "Form"],
             ["if", "one condition, one block"],
             ["if-else", "two paths"],
             ["if-else-if ladder", "many ranges, first true"],
             ["switch-case", "many equal values + break"]]
    b += text(180, 176, "Selection statements", 10.5, weight="bold", color=P)
    b += grid(16, 186, [140, 194], rows2, rh=21, size=8.6)
    b += text(180, 308, "Jump statements", 10.5, weight="bold", color=P)
    b += box(20, 318, 150, 44, REDF, RED, 7, 1.2)
    b += text(95, 336, "break", 10, weight="bold", color=RED)
    b += text(95, 352, "leave loop/switch now", 8, color=GREY)
    b += box(190, 318, 150, 44, BLUEF, BLUE, 7, 1.2)
    b += text(265, 336, "continue", 10, weight="bold", color=BLUE)
    b += text(265, 352, "skip to next round", 8, color=GREY)
    b += note(12, 370, 336, ["break without label exits only the", "innermost loop or switch."], size=9.2)
    return svg(360, 414, b)


DIAGRAM_TITLES = {
    "jv1_jdk_jre_jvm": ("JDK, JRE and JVM", jdk_jre_jvm),
    "jv1_wora": ("Write Once, Run Anywhere", wora),
    "jv1_structure": ("Structure of a Java Program", structure),
    "jv1_datatypes": ("Primitive Data Types", datatypes),
    "jv1_casting": ("Type Conversion and Casting", casting),
    "jv1_operators": ("Operators in Java", operators),
    "jv1_loops": ("Control Flow Overview", loops),
}

if __name__ == "__main__":
    import subject_DI04000021 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
