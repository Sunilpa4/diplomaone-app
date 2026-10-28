"""DI04000011 Software Engineering - Unit 4 diagrams: coding and testing."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def standards():
    b = title("Coding Standards: What They Police")
    items = ["naming rules", "indentation + layout", "comment density", "error handling style",
             "no GOTOs/globals", "function size limits"]
    for i, t in enumerate(items):
        x = 12 + (i % 2) * 174
        y = 46 + (i // 2) * 36
        b += box(x, y, 164, 28, GREENF, GREEN, 6, 1.1)
        b += text(x + 82, y + 18, t, 8.2, weight="bold", color=GREEN)
    b += note(12, 166, 336, ["One team's style = one team's mind: any",
                             "developer can read (and safely repair)",
                             "any module. Standards make that true."], size=9.2)
    return svg(360, 226, b)


def review():
    b = title("Walkthrough vs Inspection")
    b += grid(12, 44, [86, 126, 124], [
        ["point", "walkthrough", "inspection"],
        ["author's role", "leads the walk", "only answers"],
        ["formality", "informal", "highly formal"],
        ["prepared?", "little", "checklists, roles"],
        ["goal", "share knowledge", "find defects NOW"],
        ["output", "comments", "defect log for fix"],
    ], rh=19, size=8.0)
    b += box(12, 168, 336, 40, PF, P, 7, 1.2)
    b += text(180, 184, "review beats testing at cost:", 8.6, weight="bold", color=P)
    b += text(180, 198, "a requirement caught in review costs ~1; in live use, ~100.", 8.2, color=INK)
    b += note(12, 222, 336, ["Both happen BEFORE code runs: static",
                             "verification, eyeballs on work products."], size=9.2)
    return svg(360, 282, b)


def docs():
    b = title("Internal vs External Documentation")
    b += box(12, 46, 160, 116, BLUEF, BLUE, 8, 1.3)
    b += text(92, 64, "INTERNAL", 9.6, weight="bold", color=BLUE)
    b += code(22, 80, ["lives INSIDE the code:", "// comments", "doc-strings",
                       "meaningful names", "class + module headers"], 8.0, 14)
    b += box(188, 46, 160, 116, GREENF, GREEN, 8, 1.3)
    b += text(268, 64, "EXTERNAL", 9.6, weight="bold", color=GREEN)
    b += code(198, 80, ["lives BESIDE the code:", "user manual", "install guide",
                        "SRS + design docs", "API reference"], 8.0, 14)
    b += note(12, 180, 336, ["Internal serves the next developer;",
                             "external serves users and reviewers.",
                             "Both are DELIVERABLES, not extras."], size=9.2)
    return svg(360, 244, b)


def test_levels():
    b = title("Levels of Testing")
    lv = [("unit", "each function/method alone", GREEN, GREENF),
          ("integration", "modules wired together", TEAL, TEALF),
          ("system", "whole built product", ORANGE, ORANGEF),
          ("acceptance", "customer says yes", RED, REDF)]
    for i, (t, d, c, cf) in enumerate(lv):
        y = 192 - i * 46
        w = 120 + i * 42
        x = 180 - w / 2
        b += box(x, y, w, 38, cf, c, 6, 1.2)
        b += text(180, y + 15, t, 9.0, weight="bold", color=c)
        b += text(180, y + 29, d, 7.6, color=GREY)
    b += text(316, 52, "broader up", 7.4, color=GREY, anchor="end")
    b += arrow_up(320, 200, 52) if False else ""
    b += line("M322 200 L322 52", GREY, 1.3)
    b += f'<polygon points="322,52 318,60 326,60" fill="{GREY}"/>'
    b += note(12, 242, 336, ["Bottom layers are cheap and narrow; top",
                             "layers are realistic and costly. Alpha/",
                             "beta live near acceptance level."], size=9.2)
    return svg(360, 312, b)


def blackbox():
    b = title("Black-Box Testing: Inputs Only")
    b += rbox(70, 74, 96, 30, "test inputs", BLUEF, BLUE, 8.6)
    b += rarrow(120, 132, 89, GREY)
    b += box(136, 62, 96, 54, "#EEE", GREY, 6, 1.4)
    b += text(184, 90, "SYSTEM (opaque)", 7.8, weight="bold", mono=True, color=GREY)
    b += rarrow(234, 268, 89, GREY)
    b += rbox(298, 74, 108, 30, "compare output", GREENF, GREEN, 8.4)
    b += text(180, 148, "no source code is read", 8.2, weight="bold", color=P)
    b += code(14, 164, ["techniques:", "equivalence classes:  ages 5..60",
                        "  -> test 10, 45 (valid) + -3, 90 (invalid)",
                        "boundary values:   5, 60, 4, 61",
                        "cause-effect + error guessing"], 8.0, 13)
    b += note(12, 252, 336, ["One class stands for a thousand inputs;",
                             "boundaries are where bugs breed."], size=9.2)
    return svg(360, 316, b)


def whitebox():
    b = title("White-Box Testing: Cover the Code")
    b += code(14, 50, ["if (x > 0) {        // branch point",
                       "  y = f(x);  // path A",
                       "} else {",
                       "  y = g(x);  // path B",
                       "}              // then common z(y)"], 8.6, 15)
    b += grid(12, 140, [92, 244], [
        ["coverage", "meaning"],
        ["statement", "every line ran at least once"],
        ["branch", "every if took BOTH sides"],
        ["path", "every route through ran"],
    ], rh=19, size=8.2)
    b += text(180, 226, "example: tests x=3 and x=-7 -> 100% branch here", 8.2, color=P)
    b += note(12, 240, 336, ["Our eyes are INSIDE the box: pick inputs",
                             "that exercise structures (loops, edges) -",
                             "complements black-box, never replaces it.",
                             "Basis path / cyclomatic complexity counts",
                             "independent routes."], size=9.0)
    return svg(360, 326, b)


def ab_testing():
    b = title("Alpha and Beta Testing")
    b += box(12, 48, 160, 104, BLUEF, BLUE, 8, 1.3)
    b += text(92, 66, "ALPHA", 10, weight="bold", color=BLUE)
    b += code(22, 82, ["done IN-HOUSE at the",
                       "developer's site", "friendly users inside",
                       "the org watch crashes", "late in development"], 8.0, 13.5)
    b += box(188, 48, 160, 104, GREENF, GREEN, 8, 1.3)
    b += text(268, 66, "BETA", 10, weight="bold", color=GREEN)
    b += code(198, 82, ["done in the WILD at",
                        "real client sites", "real users, real data,",
                        "uncontrolled env", "feeds final fixes"], 8.0, 13.5)
    b += note(12, 170, 336, ["Order: alpha first in the lab, then beta",
                             "at selected customers - then release",
                             "candidate, then the real release."], size=9.2)
    return svg(360, 238, b)


def test_case():
    b = title("Test Case Template (Practical 15)")
    rows = [["TC-ID", "TC-07"], ["module", "booking/seat-assign"],
            ["title", "no double-booking of a seat"],
            ["precondition", "seat 12A already booked"],
            ["steps", "login as user2 -> book 12A"],
            ["test data", "route R5, seat 12A"],
            ["expected", "error + seat unchanged"],
            ["actual", "..filled during run.."],
            ["status", "pass / fail"]]
    y = 44
    for k, v in rows:
        b += box(12, y, 96, 22, PF, P, 4, 1)
        b += text(60, y + 15, k, 7.8, weight="bold", color=P)
        b += box(108, y, 240, 22, "white", GREY, 4, 1)
        b += text(118, y + 15, v, 7.6, anchor="start", color=INK)
        y += 22
    b += note(12, y + 10, 336, ["Write the EXPECTED result before running;",
                                "a test without expectations is only a",
                                "demo, not a test."], size=9.2)
    return svg(360, y + 72, b)


DIAGRAM_TITLES = {
    "se4_standards": ("Coding Standards: What They Police", standards),
    "se4_review": ("Walkthrough vs Inspection", review),
    "se4_docs": ("Internal vs External Documentation", docs),
    "se4_levels": ("Levels of Testing", test_levels),
    "se4_blackbox": ("Black-Box Testing: Inputs Only", blackbox),
    "se4_whitebox": ("White-Box Testing: Cover the Code", whitebox),
    "se4_ab": ("Alpha and Beta Testing", ab_testing),
    "se4_testcase": ("Test Case Template", test_case),
}

if __name__ == "__main__":
    import subject_DI04000011 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
