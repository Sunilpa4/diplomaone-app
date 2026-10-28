"""DI04000021 OOP-Java - Unit 2 diagrams."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def pillars():
    b = title("Four Principles of OOP")
    cols = [(10, 150, BLUE, BLUEF, "Abstraction", ["shows only what is", "needed, hides the", "working inside"]),
            (190, 150, GREEN, GREENF, "Encapsulation", ["data + methods in", "one safe box (private", "fields)"]),
            (10, 250, ORANGE, ORANGEF, "Inheritance", ["a class reuses its", "parent class", "(extends)"]),
            (190, 250, P, PF, "Polymorphism", ["same name, many", "behaviours", "(overloading)"])]
    for x, y, c, cf, t, ls in cols:
        b += box(x, y - 20, 160, 84, cf, c, 8, 1.4)
        b += text(x + 80, y, t, 10.5, weight="bold", color=c)
        for i, l in enumerate(ls):
            b += text(x + 80, y + 16 + 13 * i, l, 8.6, color="#333")
    b += note(12, 348, 336, ["ATM screen = abstraction; capsule = encapsulation;",
                             "child + parent classes = inheritance;",
                             "area() of many shapes = polymorphism."], size=9.2)
    return svg(360, 398, b)


def class_object():
    b = title("Class and Objects")
    b += box(30, 48, 120, 200, BLUEF, BLUE, 8, 1.4)
    b += text(90, 66, "class Student", 10, weight="bold", color=BLUE)
    b += line("M40 76 L140 76", BLUE, 1)
    b += code(40, 88, ["int roll;", "String name;", "", "setData()", "display()"], 8.4, 14)
    b += text(90, 240, "blueprint", 8.5, color=GREY)
    for i, (nm, r, n) in enumerate([("s1", "roll 1", "Asha"), ("s2", "roll 2", "Bhavesh"), ("s3", "roll 3", "Kiran")]):
        y = 48 + 70 * i
        b += rarrow(152, 182, y + 14, GREY)
        b += text(173, y + 10, "new", 8, weight="bold", color=GREY)
        b += box(196, y, 134, 58, GREENF, GREEN, 7, 1.2)
        b += text(263, y + 14, nm, 9.5, weight="bold", color=GREEN)
        b += text(206, y + 30, r, 8.4, anchor="start", color="#333")
        b += text(206, y + 44, "name " + n, 8.4, anchor="start", color="#333")
    b += note(12, 282, 336, ["One class, many independent objects;",
                             "each object has its own field values."], size=9.2)
    return svg(360, 328, b)


def ctor():
    b = title("Constructors")
    rows = [["Type", "Called by", "Purpose"],
            ["default", "new Book()", "fixed initial values"],
            ["parameterized", "new Book(\"Java\", 299)", "values from caller"],
            ["overloaded", "any of the above", "many ways to create"]]
    b += grid(8, 42, [90, 130, 126], rows, rh=22, size=8.2)
    b += box(10, 136, 340, 78, "#fff", "#999", 6, 1.2)
    b += code(20, 152, ["Book() { title = \"Java\"; }",
                        "Book(String t, double p) {",
                        "  title = t;  price = p;",
                        "}"], 9, 15)
    b += note(12, 226, 336, ["Same name as class, no return type;",
                             "runs automatically right after new;",
                             "not inherited by subclasses."], size=9.2)
    rows2 = [["Constructor", "Method"],
             ["class name", "any name"],
             ["no return type", "must declare one"],
             ["runs at new", "runs when called"],
             ["not inherited", "can be inherited"]]
    b += text(180, 290, "Constructor vs method", 10, weight="bold", color=P)
    b += grid(30, 300, [150, 150], rows2, rh=20, size=8.6)
    return svg(360, 412, b)


def this_static():
    b = title("this and static")
    b += box(10, 40, 160, 108, BLUEF, BLUE, 7, 1.3)
    b += text(90, 58, "this", 11, weight="bold", color=BLUE)
    b += code(20, 74, ["Book(String t) {", "  this.t = t;", "}"], 8.6, 13)
    b += text(20, 118, "this.field reads the object;", 7.8, anchor="start", color="#333")
    b += text(20, 130, "plain name reads the parameter.", 7.8, anchor="start", color="#333")
    b += text(20, 143, "this(args) -> another constructor", 7.8, anchor="start", color=BLUE)
    b += box(190, 40, 160, 108, GREENF, GREEN, 7, 1.3)
    b += text(270, 58, "static", 11, weight="bold", color=GREEN)
    b += code(200, 74, ["static int total;", "static void show()", "{ }"], 8.6, 13)
    b += text(200, 118, "one shared copy;", 7.8, anchor="start", color="#333")
    b += text(200, 130, "call via class name;", 7.8, anchor="start", color="#333")
    b += text(200, 143, "loaded before main()", 7.8, anchor="start", color=GREEN)
    b += box(10, 162, 340, 92, PF, P, 7, 1.2)
    b += text(180, 180, "Memory picture of a static variable", 9.4, weight="bold", color=P)
    b += box(30, 190, 90, 26, "#fff", P, 6, 1)
    b += text(75, 207, "total = 3", 9, color=P)
    for i, nm in enumerate(["c1", "c2", "c3"]):
        y = 190
        b += box(140 + 65 * i, y, 56, 26, "#fff", GREEN, 6, 1)
        b += text(168 + 65 * i, 207, nm + ".id=" + str(i + 1), 8, color="#333")
        b += rarrow(122, 138 + 65 * i, 203, GREY)
    b += text(180, 234, "all objects share the single total", 8.2, color=GREY)
    b += note(12, 268, 336, ["static methods can touch only static",
                             "members - no this inside them."], size=9.2)
    return svg(360, 314, b)


def access():
    b = title("Access Modifiers (visibility)")
    rows = [["Modifier", "class", "pack.", "child", "world"],
            ["public", "yes", "yes", "yes", "yes"],
            ["protected", "yes", "yes", "yes", "no"],
            ["default", "yes", "yes", "no", "no"],
            ["private", "yes", "no", "no", "no"]]
    b += grid(20, 42, [86, 56, 56, 56, 56], rows, rh=22, size=8.6)
    b += box(10, 166, 340, 68, "#fff", "#999", 6, 1.2)
    b += code(20, 180, ["private double bal;", "public double getBal() {",
                        "  return bal;   // controlled read", "}"], 8.8, 14)
    b += note(12, 248, 336, ["Most to least open: public > protected >",
                             "default > private. Encapsulation = private",
                             "fields + public methods."], size=9.2)
    return svg(360, 312, b)


def strings():
    b = title("Common String Methods")
    rows = [["Method", "Returns", "On \"GTU Diploma\""],
            ["length()", "int", "11"],
            ["charAt(4)", "char", "D"],
            ["substring(4)", "String", "Diploma"],
            ["substring(0,3)", "String", "GTU"],
            ["toUpperCase()", "String", "GTU DIPLOMA"],
            ["toLowerCase()", "String", "gtu diploma"],
            ["indexOf(\"Dip\")", "int", "4"],
            ["contains(\"oma\")", "boolean", "true"],
            ["trim()", "String", "trims spaces"],
            ["replace('D','d')", "String", "GTU diploma"],
            ["equals(t)", "boolean", "text same?"]]
    b += grid(6, 40, [104, 64, 172], rows, rh=19.5, size=8.2)
    b += note(12, 288, 336, ["Strings are immutable: methods return",
                             "NEW strings; the original never changes.",
                             "Compare text with equals(), not ==."], size=9.2)
    return svg(360, 336, b)


def boxing():
    b = title("Wrapper Classes, Autoboxing and Unboxing")
    b += rbox(70, 92, 100, 40, "int\nmarks", YEL, ORANGE, 9.4)
    b += text(70, 128, "primitive", 8, color=GREY)
    b += rbox(290, 92, 100, 40, "Integer\nmObj", BLUEF, BLUE, 9.4)
    b += text(290, 128, "wrapper object", 8, color=GREY)
    b += rarrow(122, 238, 80, GREEN)
    b += text(180, 72, "autoboxing (Java 5+)", 8.6, weight="bold", color=GREEN)
    b += line("M238 104 L122 104", RED, 1.6)
    b += f'<polygon points="122,104 132,99 132,109" fill="{RED}"/>'
    b += text(180, 122, "unboxing", 8.6, weight="bold", color=RED)
    b += code(36, 152, ["Integer mObj = marks;  // auto-box", "int m2 = mObj;         // auto-unbox",
                        "int n = Integer.parseInt(\"153\");"], 8.6, 15)
    rows = [["Primitive", "Wrapper"],
            ["byte, short", "Byte, Short"],
            ["int, long", "Integer, Long"],
            ["float, double", "Float, Double"],
            ["char", "Character"],
            ["boolean", "Boolean"]]
    b += text(180, 214, "All eight wrappers", 9.6, weight="bold", color=P)
    b += grid(70, 224, [100, 120], rows, rh=19, size=8.6)
    return svg(360, 348, b)


def gc():
    b = title("Garbage Collection and finalize()")
    b += box(10, 46, 340, 120, PF, P, 8, 1.2)
    b += text(180, 64, "Heap memory", 10, weight="bold", color=P)
    b += box(24, 76, 74, 30, GREENF, GREEN, 6, 1.2)
    b += text(61, 95, "pen (used)", 8.6, color=GREEN)
    b += box(112, 76, 74, 30, REDF, RED, 6, 1.2)
    b += text(149, 95, "book (lost)", 8.6, color=RED)
    b += box(24, 118, 120, 30, REDF, RED, 6, 1.2)
    b += text(84, 137, "bag (ref = null)", 8.6, color=RED)
    b += box(196, 76, 140, 70, GREENF, GREEN, 6, 1.2)
    b += text(266, 92, "Garbage Collector", 9.4, weight="bold", color=GREEN)
    b += text(266, 108, "removes objects", 8.4, color="#333")
    b += text(266, 122, "with no reference", 8.4, color="#333")
    b += text(266, 137, "finalize() runs first", 8.4, color=RED)
    b += rarrow(160, 194, 111, GREY)
    b += code(24, 204, ["it = null;        // object loses its ref",
                        "System.gc();      // request collection"], 8.8, 15)
    b += note(12, 246, 336, ["GC runs when IT decides - never trust",
                             "timing; finalize() is a last clean-up",
                             "chance, deprecated in modern Java."], size=9.2)
    return svg(360, 296, b)


DIAGRAM_TITLES = {
    "jv2_pillars": ("Four Principles of OOP", pillars),
    "jv2_class_object": ("Class and Objects", class_object),
    "jv2_ctor": ("Constructors", ctor),
    "jv2_this_static": ("this and static", this_static),
    "jv2_access": ("Access Modifiers", access),
    "jv2_strings": ("Common String Methods", strings),
    "jv2_boxing": ("Wrappers, Autoboxing, Unboxing", boxing),
    "jv2_gc": ("Garbage Collection and finalize()", gc),
}

if __name__ == "__main__":
    import subject_DI04000021 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
