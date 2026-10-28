"""DI04000021 OOP-Java - Unit 3 diagrams: inheritance, interfaces, packages."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def inherit_types():
    b = title("Types of Inheritance")
    def lblbx(x, y, t, c=BLUE, cf=BLUEF, w=64):
        return box(x, y, w, 22, cf, c, 6, 1.1) + text(x + w / 2, y + 14, t, 8.6, weight="bold", color=c)
    def darrow(x, y1, y2, c=GREY):
        return line(f"M{x} {y1} L{x} {y2}", c, 1.4) + f'<polygon points="{x},{y2-4} {x-4},{y2+4} {x+4},{y2+4}" fill="{c}"/>'
    # single
    b += text(80, 56, "single", 9.5, weight="bold", color=P)
    b += lblbx(48, 66, "Person") + lblbx(48, 108, "Employee") + darrow(80, 88, 104)
    # multilevel
    b += text(200, 56, "multilevel", 9.5, weight="bold", color=P)
    b += lblbx(168, 66, "Person") + lblbx(160, 100, "Employee", w=76) + lblbx(168, 134, "Manager") + darrow(200, 88, 96) + darrow(200, 122, 130)
    # hierarchical
    b += text(300, 56, "hierarchical", 9.5, weight="bold", color=P)
    b += lblbx(268, 66, "Vehicle") + lblbx(246, 108, "Car", w=48) + lblbx(300, 108, "Bike", w=48)
    b += line("M284 88 L270 106", GREY, 1.4) + line("M284 88 L324 106", GREY, 1.4)
    b += f'<polygon points="270,106 268,99 273,103" fill="{GREY}"/><polygon points="324,106 322,99 327,103" fill="{GREY}"/>'
    # hybrid
    b += text(80, 192, "hybrid (mix)", 9.5, weight="bold", color=P)
    b += lblbx(48, 202, "Vehicle") + lblbx(16, 236, "Car", w=48) + lblbx(74, 236, "Bike", w=48) + lblbx(16, 270, "PetrolCar", BLUE, BLUEF, 72)
    b += line("M64 224 L40 234", GREY, 1.4) + line("M64 224 L98 234", GREY, 1.4) + darrow(40, 258, 266)
    # multiple crossed
    b += text(250, 192, "multiple - NOT allowed", 9.5, weight="bold", color=RED)
    b += lblbx(196, 202, "Teacher", RED, REDF, 72) + lblbx(280, 202, "Coach", RED, REDF, 60)
    b += lblbx(232, 244, "Student", RED, REDF, 72)
    b += line("M232 224 L268 244", RED, 1.4) + line("M310 224 L300 244", RED, 1.4)
    b += line("M196 236 L352 286", RED, 2)
    b += text(180, 300, "two class parents clash", 8.2, color=RED)
    b += note(12, 312, 336, ["Java classes: only one direct parent.",
                             "\"Multiple\" is achieved with several",
                             "interfaces instead (see interfaces)."], size=9.2)
    return svg(360, 358, b)


def super_this():
    b = title("this vs super")
    b += box(10, 40, 165, 118, BLUEF, BLUE, 7, 1.3)
    b += text(92, 58, "this - the same class", 9.5, weight="bold", color=BLUE)
    b += code(20, 72, ["this.title = t;   // field", "this(t);          // own ctor",
                       "return this;      // me"], 8.4, 14)
    b += text(92, 146, "refers to the CURRENT object", 7.6, color="#333")
    b += box(185, 40, 165, 118, GREENF, GREEN, 7, 1.3)
    b += text(268, 58, "super - the parent", 9.5, weight="bold", color=GREEN)
    b += code(195, 72, ["super(\"circle\"); // ctor", "super.info();    // method",
                        "super.name; // field"], 8.4, 14)
    b += text(268, 146, "refers to the PARENT part", 7.6, color="#333")
    b += box(10, 170, 340, 84, "#fff", "#999", 6, 1.2)
    b += code(20, 186, ["class Circle extends Shape {", "  Circle(double r) {", "    super(\"circle\");   // first!",
                        "    this.r = r;          // field", "  }", "}"], 8.6, 14)
    b += note(12, 272, 336, ["Both \"call constructors\" go first in a",
                             "constructor; you may use only one of",
                             "this() or super() in each constructor."], size=9.2)
    return svg(360, 322, b)


def override_vs():
    b = title("Overloading vs Overriding")
    rows = [["Point", "Overloading", "Overriding"],
            ["Where", "same class", "child class"],
            ["Signature", "must differ", "must be same"],
            ["Return type", "can differ", "must match"],
            ["Decided at", "compile time", "run time"],
            ["Relation", "static polymorph", "run-time polymorph"],
            ["Constraint", "none", "access not stricter"]]
    b += grid(8, 40, [86, 122, 128], rows, rh=21, size=8.4)
    b += box(10, 200, 340, 64, PF, P, 7, 1.2)
    b += code(20, 216, ["void print(String s) { }", "void print(String s, int n) { }   // overload",
                        "", "void header() { }   // child: override"], 8.6, 13)
    return svg(360, 278, b)


def dispatch():
    b = title("Dynamic Method Dispatch")
    b += rbox(60, 88, 100, 40, "Shape sh;", YEL, ORANGE, 9.5)
    b += text(60, 124, "parent reference", 8.2, color=GREY)
    b += rbox(250, 66, 96, 30, "new Circle()", GREENF, GREEN, 9)
    b += rbox(250, 128, 96, 30, "new Square()", BLUEF, BLUE, 9)
    b += line("M112 82 L200 81", GREEN, 1.6)
    b += f'<polygon points="200,81 190,76 190,86" fill="{GREEN}"/>'
    b += line("M112 108 L200 143", BLUE, 1.6)
    b += f'<polygon points="200,143 190,140 192,150" fill="{BLUE}"/>'
    b += code(24, 186, ["Shape sh;", "sh = new Circle();      sh.area();",
                        "   -> Circle.area()", "", "sh = new Square();      sh.area();",
                        "   -> Square.area()"], 8.8, 15)
    b += note(12, 290, 336, ["Which area() runs depends on the OBJECT",
                             "behind the reference - chosen at run time.",
                             "This is run-time polymorphism."], size=9.2)
    return svg(360, 340, b)


def abstract_vs():
    b = title("Abstract Class vs Interface")
    rows = [["Point", "Abstract class", "Interface"],
            ["Methods", "abstract + ready", "abstract (default ok)"],
            ["Fields", "any", "constants only"],
            ["Constructor", "yes", "no"],
            ["Extend/use", "extends 1 class", "implements many"],
            ["new?", "never", "never"]]
    b += grid(8, 40, [80, 126, 128], rows, rh=22, size=8.4)
    b += box(10, 186, 160, 66, REDF, RED, 7, 1.2)
    b += code(20, 202, ["abstract class Shape {", "  abstract double", "    area();  // no body",
                        "  void displayType(){}", "}"], 8.2, 12.5)
    b += box(190, 186, 160, 66, GREENF, GREEN, 7, 1.2)
    b += code(200, 202, ["interface Drawable {", "  void draw();", "  int UNIT = 20;", "  // constant",
                        "}"], 8.2, 12.5)
    b += note(12, 274, 336, ["Contract: \"every shape computes area\"",
                             "- the child MUST implement it, else the",
                             "child itself has to be abstract."], size=9.2)
    return svg(360, 322, b)


def interface_multi():
    b = title("Multiple Inheritance via Interfaces")
    b += rbox(60, 66, 100, 30, "interface", GREENF, GREEN, 8.6) + text(60, 104, "Printable", 9.4, weight="bold", color=GREEN)
    b += rbox(292, 66, 120, 30, "interface", GREENF, GREEN, 8.6) + text(292, 104, "Showable", 9.4, weight="bold", color=GREEN)
    b += rbox(180, 168, 120, 34, "class Report", BLUEF, BLUE, 9.5)
    b += line("M70 98 L126 168", GREEN, 1.6, dash="5 3") + line("M282 98 L234 168", GREEN, 1.6, dash="5 3")
    b += text(104, 138, "implements", 8.2, color=GREY) + text(248, 138, "implements", 8.2, color=GREY, anchor="end")
    b += code(24, 210, ["class Report implements", "    Printable, Showable {", "  public void print() { }",
                        "  public void show() { }", "}"], 8.8, 15)
    b += note(12, 300, 336, ["No clash: interface methods carry no body",
                             "and no state - the single child body of",
                             "Report satisfies both contracts."], size=9.2)
    return svg(360, 350, b)


def packages():
    b = title("Packages and import")
    b += box(10, 44, 150, 130, YEL, ORANGE, 7, 1.3)
    b += text(85, 62, "folder = package", 9.2, weight="bold", color=ORANGE)
    b += code(24, 78, ["college/", "  Student.java", "    package college;", "  Main.java", "    import college.Student;"], 8, 14)
    b += box(190, 44, 160, 130, PF, P, 7, 1.3)
    b += text(270, 62, "built-in packages", 9.2, weight="bold", color=P)
    b += code(204, 78, ["java.lang (auto)", "  String, Math", "java.util", "  Scanner, ArrayList", "java.io, java.time"], 8, 14)
    b += code(24, 204, ["import java.util.Date;", "import java.util.*;  // wildcard",
                        "// full name works without import:", "java.util.Date d = new java.util.Date();"], 8.4, 15)
    b += note(12, 288, 336, ["Cross-package use needs public members",
                             "(or protected for subclasses.)"], size=9.2)
    return svg(360, 336, b)


DIAGRAM_TITLES = {
    "jv3_inherit_types": ("Types of Inheritance", inherit_types),
    "jv3_super_this": ("this vs super", super_this),
    "jv3_override_vs": ("Overloading vs Overriding", override_vs),
    "jv3_dispatch": ("Dynamic Method Dispatch", dispatch),
    "jv3_abstract_vs": ("Abstract Class vs Interface", abstract_vs),
    "jv3_interface_multi": ("Multiple Inheritance via Interfaces", interface_multi),
    "jv3_packages": ("Packages and import", packages),
}

if __name__ == "__main__":
    import subject_DI04000021 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
