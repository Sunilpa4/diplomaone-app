"""DI04000021 OOP-Java - Unit 5 diagrams: modern features, streams, AI."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def timeline():
    b = title("Java Version Highlights (7 onwards)")
    stops = [
        ("7", "try-with-res., strings in switch, diamond, multi-catch"),
        ("8", "lambda, Stream API, java.time, default methods"),
        ("9", "modules (JPMS), jshell"),
        ("10", "var - local type inference"),
        ("11", "LTS, var in lambda, new HttpClient"),
        ("14", "switch expressions (arrow ->)"),
        ("15", "text blocks  \"\"\" ... \"\"\""),
        ("16", "records, pattern-matching instanceof"),
        ("17", "LTS, sealed classes"),
        ("21", "LTS, virtual threads, pattern matching++"),
    ]
    y = 48
    b += line("M28 %d L28 %d" % (y, y + len(stops) * 24), GREY, 1.6)
    for i, (v, t) in enumerate(stops):
        yy = y + i * 24
        c = BLUE if v not in ("11", "17", "21") else GREEN
        cf = BLUEF if c == BLUE else GREENF
        b += box(12, yy, 32, 18, cf, c, 5, 1.1)
        b += text(28, yy + 12, v, 8.6, weight="bold", color=c, anchor="middle")
        b += text(54, yy + 12, t, 8.4, anchor="start", color=INK)
    b += note(12, 300, 336, ["LTS = Long-Term Support (11, 17, 21):",
                             "the versions industries standardise on.",
                             "This course runs and tests Java 8+",
                             "features; 14+ syntax is study-exhibit."], size=9.0)
    return svg(360, 384, b)


def twr():
    b = title("try-with-resources vs try-finally (Java 7)")
    b += text(100, 56, "the old (Unit 4) way", 9.2, weight="bold", color=RED)
    b += text(268, 56, "try-with-resources", 9.2, weight="bold", color=GREEN)
    b += box(10, 64, 156, 118, REDF, RED, 7, 1.2)
    b += code(18, 80, ["Scanner sc = new",
                       "  Scanner(src);",
                       "try {",
                       "  use(sc);",
                       "} finally {",
                       "  if (sc != null)",
                       "    sc.close();",
                       "}"], 8.0, 12.5)
    b += box(194, 64, 156, 118, GREENF, GREEN, 7, 1.2)
    b += code(202, 80, ["try (Scanner sc =",
                        "  new Scanner(src)) {",
                        "  use(sc);",
                        "}",
                        "// close() happens",
                        "// automatically",
                        "// on every path"], 8.0, 12.5)
    b += grid(12, 196, [140, 196], [
        ["aspect", "finally vs try-with-resources"],
        ["close written by", "you vs the JVM"],
        ["exception-safe?", "only if careful vs always"],
    ], rh=19, size=8.2)
    b += note(12, 262, 336, ["Works with anything implementing",
                             "AutoCloseable (files, sockets, DB).",
                             "Multiple resources: try (A a; B b)"], size=9.2)
    return svg(360, 326, b)


def lambda_anatomy():
    b = title("Lambda Anatomy")
    b += box(12, 46, 336, 40, PF, P, 7, 1.3)
    b += code(24, 62, ["Calc add =  (x, y)  ->  x + y;"], 10, 16)
    b += text(180, 108, "parameters", 8.6, weight="bold", color=BLUE)
    b += text(242, 108, "arrow", 8.6, weight="bold", color=ORANGE)
    b += text(310, 108, "body / result", 8.6, weight="bold", color=GREEN)
    for x1, x2, yy in ((182, 162, 66), (240, 210, 66), (308, 258, 66)):
        b += line(f"M{x1} 102 L{x2} {yy+20}", GREY, 1.2, dash="4 3")
    b += text(24, 108, "typed name", 8.6, weight="bold", color=P, anchor="start")
    b += line("M76 104 L84 82", GREY, 1.2, dash="4 3")
    b += grid(12, 128, [150, 186], [
        ["shape", "example"],
        ["no params", "() -> 42"],
        ["one param", "n -> n * n   (parens free)"],
        ["two params", "(x, y) -> x + y"],
        ["block body", "n -> { int s = n*n; return s; }"],
    ], rh=19, size=8.2)
    b += note(12, 240, 336, ["A lambda targets a FUNCTIONAL interface:",
                             "one abstract method whose signature the",
                             "parameters and body must match."], size=9.2)
    return svg(360, 306, b)


def functional_ifaces():
    b = title("Ready-made Functional Interfaces")
    b += text(12, 50, "the ONE abstract method rule:", 9.2, weight="bold", color=P, anchor="start")
    b += code(14, 62, ["interface Runnable {  void run(); }",
                       "interface Speaker {  void speak(); }"], 8.4, 15)
    b += grid(12, 108, [100, 96, 128], [
        ["interface", "method", "used by / coined"],
        ["Runnable", "run()", "threads, tasks"],
        ["Supplier<T>", "T get()", "value on demand"],
        ["Consumer<T>", "accept(t)", "forEach"],
        ["Predicate<T>", "test(t)", "filter"],
        ["Function<T,R>", "apply(t)", "map"],
    ], rh=19, size=8.2)
    b += code(14, 232, ["@FunctionalInterface",
                        "interface Calc {",
                        "  int op(int x, int y);",
                        "}   // compile-checked"], 8.4, 14)
    b += note(12, 306, 336, ["@FunctionalInterface asks javac to reject",
                             "interfaces that accidentally grow a second",
                             "abstract method - keeps lambdas legal."], size=9.2)
    return svg(360, 376, b)


def stream_pipeline():
    b = title("Stream Pipeline: filter, map, collect")
    stages = [("source", "list.stream()", BLUE), ("filter", "m >= 50", ORANGE),
              ("sorted", "ascending", ORANGE), ("map", "m -> text", ORANGE),
              ("collect", "to a new List", GREEN)]
    xw = 62
    for i, (t, s, c) in enumerate(stages):
        x = 8 + i * 70
        cf = {BLUE: BLUEF, ORANGE: ORANGEF, GREEN: GREENF}[c]
        b += box(x, 52, xw, 34, cf, c, 6, 1.2)
        b += text(x + xw / 2, 66, t, 9.0, weight="bold", color=c)
        b += text(x + xw / 2, 79, s, 6.8, mono=True, color=INK)
        if i < len(stages) - 1:
            b += rarrow(x + xw + 2, x + 68, 69, GREY)
    b += text(180, 118, "marks: 88 45 72 95 61 50", 8.6, mono=True, color=GREY)
    for i, lbl in enumerate(["after filter: 88 72 95 61 50",
                             "after sorted: 50 61 72 88 95",
                             "after map: pass:50 ... pass:95"]):
        y = 140 + i * 22
        c = [ORANGE, ORANGE, GREEN][i]
        b += text(180, y, lbl, 8.6, mono=True, color=c)
    b += grid(12, 208, [120, 216], [
        ["kind", "intermediate vs terminal"],
        ["intermediate", "filter, map, sorted - LAZY"],
        ["terminal", "forEach, count, collect - GO"],
        ["source list", "never mutated"],
    ], rh=19, size=8.2)
    b += note(12, 292, 336, ["Nothing moves until the terminal step;",
                             "a used stream cannot be re-used -",
                             "open a fresh .stream() instead."], size=9.2)
    return svg(360, 356, b)


def ai_ml():
    b = title("AI, ML, DL - How They Nest")
    b += box(20, 48, 320, 110, BLUEF, BLUE, 9, 1.4)
    b += text(180, 66, "ARTIFICIAL INTELLIGENCE", 9.4, weight="bold", color=BLUE)
    b += text(180, 80, "machines doing tasks that need human-like smarts", 7.6, color=GREY)
    b += box(44, 90, 272, 60, GREENF, GREEN, 8, 1.4)
    b += text(180, 106, "MACHINE LEARNING", 9.2, weight="bold", color=GREEN)
    b += text(180, 120, "rules learned from DATA, not hand-written ifs", 7.4, color=GREY)
    b += box(100, 126, 160, 26, YEL, ORANGE, 7, 1.3)
    b += text(180, 143, "DEEP LEARNING (neural nets)", 8.2, weight="bold", color=ORANGE)
    b += grid(12, 172, [110, 226], [
        ["style", "example in this subject"],
        ["classic AI", "rules: if mark < 33 -> fail"],
        ["ML", "k-NN: learn from 5 students (jv5_13)"],
        ["result use", "predict pass/fail from new data"],
    ], rh=20, size=8.3)
    b += note(12, 266, 336, ["Definition for the exam: AI = goal",
                             "(behave intelligently); ML = the approach",
                             "(learn the behaviour from examples);",
                             "DL = ML with layered neural networks."], size=9.0)
    return svg(360, 344, b)


def ai_libs():
    b = title("Java's Role in AI + Its Libraries")
    b += text(12, 52, "where Java fits:", 9.4, weight="bold", color=P, anchor="start")
    b += grid(12, 60, [120, 216], [
        ["strength", "why it matters"],
        ["enterprise apps", "most company backends are Java"],
        ["data handling", "strong collections, streams, JDBC"],
        ["API integration", "call AI services from Java apps"],
    ], rh=20, size=8.2)
    b += text(12, 140, "libraries to know by name:", 9.4, weight="bold", color=P, anchor="start")
    b += box(12, 150, 160, 80, YEL, ORANGE, 7, 1.2)
    b += text(92, 168, "Deeplearning4j", 9.2, weight="bold", color=ORANGE)
    b += code(24, 182, ["deep learning IN Java",
                        "neural nets on GPUs",
                        "JVM ecosystem native"], 8.2, 13)
    b += box(188, 150, 160, 80, GREENF, GREEN, 7, 1.2)
    b += text(268, 168, "TensorFlow Java", 9.2, weight="bold", color=GREEN)
    b += code(200, 182, ["runs PRE-TRAINED",
                         "TF models from",
                         "inside Java code"], 8.2, 13)
    b += note(12, 250, 336, ["Pattern in industry: Python often TRAINS,",
                             "Java DEPLOYS at scale - a Java service",
                             "loads the model and answers requests.",
                             "jv5_13 shows the idea in 30 lines."], size=9.0)
    return svg(360, 330, b)


DIAGRAM_TITLES = {
    "jv5_timeline": ("Java Version Highlights (7 onwards)", timeline),
    "jv5_twr": ("try-with-resources vs try-finally (Java 7)", twr),
    "jv5_lambda": ("Lambda Anatomy", lambda_anatomy),
    "jv5_func_iface": ("Ready-made Functional Interfaces", functional_ifaces),
    "jv5_stream": ("Stream Pipeline: filter, map, collect", stream_pipeline),
    "jv5_aiml": ("AI, ML, DL - How They Nest", ai_ml),
    "jv5_ailibs": ("Java's Role in AI + Its Libraries", ai_libs),
}

if __name__ == "__main__":
    import subject_DI04000021 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
