"""DI03000031 RDBMS - Unit 3 diagrams: anomalies, functional dependencies, keys, normal forms."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000031", "diagrams")


def rel(x, y, name, attrs, keys=(), w=None, color=BLUE, fill=BLUEF, size=9.2):
    """Relation schema drawn as a row of boxes; key attributes underlined and bold."""
    cw = w or [max(40, 7.0 * len(a) + 12) for a in attrs]
    b = text(x, y - 8, name, 9.6, anchor="start", weight="bold", color=color)
    cx = x
    for a, ww in zip(attrs, cw):
        k = a in keys
        b += box(cx, y, ww, 22, fill if k else "#fff", color, 0, 1.2)
        b += text(cx + ww / 2, y + 11, a, size, weight="bold" if k else "normal")
        if k:
            tw = 6.0 * len(a)
            b += line(f"M{cx + ww / 2 - tw / 2} {y + 17} L{cx + ww / 2 + tw / 2} {y + 17}", INK, 1)
        cx += ww
    return b, cw


def arc(x1, x2, y, h, color=INK, up=False, dash=None):
    """Dependency arrow from attribute centre x1 to x2 drawn below (or above) a schema row."""
    yy = y - h if up else y + h
    d = f"M{x1} {y} L{x1} {yy} L{x2} {yy} L{x2} {y + (-6 if up else 6)}"
    return line(d, color, 1.4, dash) + arrowhead(x2, y, 90 if up else -90, 7, color)


# ------------------------------------------------------------------ 3.1
def anomalies():
    b = title("Redundancy and Anomalies")
    rows = [["ROLL", "NAME", "CID", "CNAME", "FEES"], ["1", "Aarav", "C1", "DBMS", "5000"], ["2", "Diya", "C1", "DBMS", "5000"],
            ["3", "Karan", "C1", "DBMS", "5000"], ["4", "Isha", "C2", "Python", "4000"]]
    b += text(154, 40, "STUD_COURSE (not normalized)", 10, weight="bold", color=P)
    b += grid(14, 48, [44, 64, 44, 64, 64], rows, rh=22, size=9.2)
    b += f'<rect x="166" y="70" width="128" height="66" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>'
    b += text(300, 98, "repeated", 8.6, anchor="start", color=RED)
    b += text(300, 110, "3 times", 8.6, anchor="start", color=RED)
    items = [("Insertion anomaly", "A new course C3 cannot be added until a", "student joins it (ROLL would be NULL).", ORANGE, ORANGEF),
             ("Update anomaly", "Changing DBMS fees needs 3 updates; missing", "one row makes the data inconsistent.", BLUE, BLUEF),
             ("Deletion anomaly", "Deleting Isha (only Python student) also", "deletes all facts about course C2.", RED, REDF)]
    for i, (t, l1, l2, s, f) in enumerate(items):
        y = 168 + i * 58
        b += box(14, y, 332, 50, f, s, 7, 1.4) + text(24, y + 14, t, 10.2, anchor="start", weight="bold", color=s)
        b += text(24, y + 30, l1, 9.2, anchor="start") + text(24, y + 43, l2, 9.2, anchor="start")
    return svg(360, 168 + 3 * 58 + 6, b)


# ------------------------------------------------------------------ 3.2
def fd():
    b = title("Functional Dependency X → Y")
    b += box(40, 46, 100, 40, BLUEF, BLUE, 8, 1.6) + text(90, 60, "X", 13, weight="bold", color=BLUE) + text(90, 76, "determinant", 8.6, color=BLUE)
    b += rarrow(142, 216, 66)
    b += text(179, 56, "determines", 8.6, color=GREY)
    b += box(218, 46, 100, 40, GREENF, GREEN, 8, 1.6) + text(268, 60, "Y", 13, weight="bold", color=GREEN) + text(268, 76, "dependent", 8.6, color=GREEN)
    b += text(180, 108, "For each value of X there is exactly ONE value of Y", 9.4, weight="bold", color=P)
    rows = [["ROLLNO", "NAME", "CITY"], ["1", "Aarav", "Surat"], ["2", "Diya", "Vadodara"], ["1", "Aarav", "Surat"]]
    b += grid(70, 122, [70, 80, 70], rows, rh=20, size=9.2)
    b += text(180, 214, "ROLLNO → NAME holds (1 always gives Aarav)", 9.2, color=GREEN)
    b += text(180, 230, "NAME → ROLLNO may fail (two students can be Amit)", 9.2, color=RED)
    b += note(12, 244, 336, [("Armstrong's axioms:", P), "Reflexivity: if Y ⊆ X then X → Y",
                             "Augmentation: if X → Y then XZ → YZ", "Transitivity: if X → Y and Y → Z then X → Z",
                             ("Closure X+ = all attributes determined by X.", P)], size=9.4)
    return svg(360, 334, b)


def fd_types():
    b = title("Full, Partial and Transitive Dependency")
    # full
    b += text(14, 44, "1. Full functional dependency", 10.2, anchor="start", weight="bold", color=GREEN)
    s, cw = rel(30, 54, "", ["ROLL", "CID", "MARKS"], keys=("ROLL", "CID"), color=GREEN, fill=GREENF)
    b += s
    xs = [30 + sum(cw[:i]) + cw[i] / 2 for i in range(3)]
    b += line(f"M{xs[0]} 76 L{xs[0]} 90 M{xs[1]} 76 L{xs[1]} 90 M{xs[0]} 90 L{xs[2]} 90", GREEN, 1.4) + arrowhead(xs[2], 77, -90, 7, GREEN)
    b += line(f"M{xs[2]} 90 L{xs[2]} 82", GREEN, 1.4)
    b += lines(222, 62, ["MARKS needs the WHOLE", "key (ROLL + CID)"], 9, lh=13, anchor="start")
    # partial
    b += text(14, 124, "2. Partial dependency (violates 2NF)", 10.2, anchor="start", weight="bold", color=ORANGE)
    s, cw = rel(30, 134, "", ["ROLL", "CID", "NAME"], keys=("ROLL", "CID"), color=ORANGE, fill=ORANGEF)
    b += s
    xs = [30 + sum(cw[:i]) + cw[i] / 2 for i in range(3)]
    b += arc(xs[0], xs[2], 156, 14, ORANGE)
    b += lines(222, 142, ["NAME depends on ROLL", "only (part of the key)"], 9, lh=13, anchor="start")
    # transitive
    b += text(14, 204, "3. Transitive dependency (violates 3NF)", 10.2, anchor="start", weight="bold", color=RED)
    s, cw = rel(30, 214, "", ["EMPNO", "DEPTNO", "DNAME"], keys=("EMPNO",), color=RED, fill=REDF)
    b += s
    xs = [30 + sum(cw[:i]) + cw[i] / 2 for i in range(3)]
    b += arc(xs[0], xs[1] - 8, 236, 12, RED) + arc(xs[1] + 8, xs[2], 236, 24, RED)
    b += lines(234, 222, ["EMPNO → DEPTNO", "DEPTNO → DNAME", "so EMPNO → DNAME", "through DEPTNO"], 9, lh=13, anchor="start")
    b += note(12, 282, 336, ["Partial: non-key attribute depends on PART of a", " composite key.",
                             "Transitive: non-key attribute depends on another", " non-key attribute."], size=9.4)
    return svg(360, 354, b)


def keys():
    b = title("Types of Keys")
    b += f'<ellipse cx="180" cy="130" rx="166" ry="92" fill="{BLUEF}" stroke="{BLUE}" stroke-width="1.6"/>'
    b += text(180, 54, "Super keys", 10.5, weight="bold", color=BLUE)
    b += text(180, 68, "{ROLL}, {ROLL, NAME}, {EMAIL, CITY} ...", 8.6, color=BLUE)
    b += f'<ellipse cx="180" cy="144" rx="120" ry="60" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.6"/>'
    b += text(180, 100, "Candidate keys (minimal)", 10, weight="bold", color=GREEN)
    b += text(180, 114, "{ROLL}, {EMAIL}, {AADHAAR}", 8.8, color=GREEN)
    b += box(84, 128, 92, 46, PF, P, 8, 1.6) + text(130, 144, "Primary key", 9.6, weight="bold", color=P) + text(130, 160, "ROLL", 9.4, mono=True)
    b += box(184, 128, 92, 46, ORANGEF, ORANGE, 8, 1.6) + text(230, 144, "Alternate keys", 9.4, weight="bold", color=ORANGE)
    b += text(230, 160, "EMAIL, AADHAAR", 8.4, mono=True)
    b += note(12, 234, 336, ["Super key: any set of attributes that uniquely", " identifies a row.",
                             "Candidate key: minimal super key.", "Primary key: candidate key chosen by designer.",
                             "Alternate key: candidate keys not chosen.", "Composite key: key with 2+ attributes.",
                             "Foreign key: refers to the primary key of", " another table."], size=9.4)
    return svg(360, 364, b)


def steps():
    b = title("Steps of Normalization")
    st = [("UNF", "Unnormalized: repeating groups,", "multi-valued cells", "#F2F2F2", "#777"),
          ("1NF", "Atomic values, no repeating", "groups, primary key defined", BLUEF, BLUE),
          ("2NF", "1NF + no partial dependency", "(full dependency on key)", GREENF, GREEN),
          ("3NF", "2NF + no transitive dependency", "(non-key depends on key only)", ORANGEF, ORANGE),
          ("BCNF", "every determinant is a", "candidate key", PF, P)]
    acts = ["remove repeating groups", "remove partial dependency", "remove transitive dep.", "determinants = keys"]
    for i, (n, l1, l2, f, s) in enumerate(st):
        x, y = 14 + i * 22, 40 + i * 58
        b += box(x, y, 250, 42, f, s, 8, 1.6)
        b += text(x + 30, y + 21, n, 12, weight="bold", color=s)
        b += text(x + 64, y + 15, l1, 9, anchor="start") + text(x + 64, y + 29, l2, 9, anchor="start")
        if i < 4:
            b += line(f"M{x + 150} {y + 42} L{x + 150} {y + 52} L{x + 172 - 6} {y + 52}", GREY, 1.2)
            b += line(f"M{x + 172} {y + 42 + 4} L{x + 172} {y + 58}", GREY, 1.2) + arrowhead(x + 172, y + 58, 90, 6, GREY)
            b += text(x + 180, y + 51, acts[i], 8.2, anchor="start", color=s if i else "#777")
    b += note(12, 336, 336, ["Each higher normal form also satisfies all the", "lower ones. In practice, 3NF is usually enough."], size=9.4)
    return svg(360, 378, b)


def nf1():
    b = title("Converting to First Normal Form")
    b += text(14, 42, "UNF: multi-valued cells", 10, anchor="start", weight="bold", color=RED)
    b += grid(14, 50, [44, 64, 100], [["ROLL", "NAME", "COURSES"], ["1", "Aarav", "DBMS, OS"], ["2", "Diya", "DBMS"],
                                       ["3", "Karan", "OS, CN, Java"]], rh=22, size=9.2)
    b += f'<rect x="122" y="72" width="100" height="22" fill="none" stroke="{RED}" stroke-width="2"/>'
    b += f'<rect x="122" y="116" width="100" height="22" fill="none" stroke="{RED}" stroke-width="2"/>'
    b += text(234, 84, "not atomic", 9, anchor="start", color=RED)
    b += down(118, 142, 160)
    b += text(14, 176, "1NF: one value per cell", 10, anchor="start", weight="bold", color=GREEN)
    rows = [["ROLL", "NAME", "COURSE"], ["1", "Aarav", "DBMS"], ["1", "Aarav", "OS"], ["2", "Diya", "DBMS"], ["3", "Karan", "OS"],
            ["3", "Karan", "CN"], ["3", "Karan", "Java"]]
    b += grid(14, 184, [44, 64, 100], rows, rh=20, size=9.2, head_fill=GREEN)
    b += box(232, 196, 116, 82, PF, P, 7, 1.2)
    b += lines(290, 212, ["Primary key:", "(ROLL, COURSE)", "", "NAME repeats", "→ needs 2NF"], 9, lh=13)
    return svg(360, 334, b)


def nf2():
    t = title("1NF → 2NF (Partial Dependency)")
    b = text(14, 28, "RESULT (1NF)", 9.6, anchor="start", weight="bold", color=BLUE)
    s, cw = rel(14, 52, "", ["ROLL", "CID", "NAME", "CNAME", "MARKS"], keys=("ROLL", "CID"), w=[52, 46, 62, 66, 60])
    b += s
    xs = [14 + sum(cw[:i]) + cw[i] / 2 for i in range(5)]
    b += arc(xs[0], xs[2], 74, 12, ORANGE)
    b += arc(xs[1], xs[3], 74, 24, ORANGE)
    b += line(f"M{xs[0]} 52 L{xs[0]} 40 L{xs[4]} 40 L{xs[4]} 46", GREEN, 1.4) + line(f"M{xs[1]} 52 L{xs[1]} 40", GREEN, 1.4)
    b += arrowhead(xs[4], 52, 90, 7, GREEN)
    b += text(300, 88, "partial", 9, anchor="start", color=ORANGE, weight="bold")
    b += text(300, 34, "full", 9, anchor="start", color=GREEN, weight="bold")
    b += down(150, 104, 124)
    s, _ = rel(14, 148, "STUDENT", ["ROLL", "NAME"], keys=("ROLL",), w=[52, 70], color=GREEN, fill=GREENF)
    b += s
    s, _ = rel(150, 148, "COURSE", ["CID", "CNAME"], keys=("CID",), w=[50, 70], color=GREEN, fill=GREENF)
    b += s
    s, _ = rel(14, 204, "RESULT", ["ROLL", "CID", "MARKS"], keys=("ROLL", "CID"), w=[52, 50, 64], color=GREEN, fill=GREENF)
    b += s
    b += note(12, 240, 336, ["Key = (ROLL, CID).", "ROLL → NAME and CID → CNAME are partial.",
                             "Move each partial dependency to its own table;", "keep the full dependency with the whole key."], size=9.4)
    return svg(360, 326, t + f'<g transform="translate(0,14)">{b}</g>')


def nf3():
    t = title("2NF → 3NF (Transitive Dependency)")
    b = text(14, 28, "EMPLOYEE (2NF)", 9.6, anchor="start", weight="bold", color=BLUE)
    s, cw = rel(14, 52, "", ["EMPNO", "ENAME", "DEPTNO", "DNAME", "LOC"], keys=("EMPNO",), w=[60, 62, 66, 66, 54])
    b += s
    xs = [14 + sum(cw[:i]) + cw[i] / 2 for i in range(5)]
    b += line(f"M{xs[0]} 52 L{xs[0]} 40 L{xs[2]} 40 L{xs[2]} 46", BLUE, 1.4) + arrowhead(xs[2], 52, 90, 7, BLUE)
    b += line(f"M{xs[1]} 40 L{xs[1]} 46", BLUE, 1.4) + arrowhead(xs[1], 52, 90, 7, BLUE)
    b += arc(xs[2] - 8, xs[3], 74, 12, RED) + arc(xs[2] + 8, xs[4], 74, 24, RED)
    b += text(14, 106, "DEPTNO → DNAME, LOC (non-key → non-key)", 9.2, anchor="start", color=RED, weight="bold")
    b += down(150, 112, 130)
    s, _ = rel(14, 152, "EMP", ["EMPNO", "ENAME", "DEPTNO"], keys=("EMPNO",), w=[60, 62, 66], color=GREEN, fill=GREENF)
    b += s
    s, _ = rel(214, 152, "DEPT", ["DEPTNO", "DNAME", "LOC"], keys=("DEPTNO",), w=[52, 50, 40], color=GREEN, fill=GREENF, size=8.6)
    b += s
    b += text(150, 192, "EMP.DEPTNO is a foreign key → DEPT.DEPTNO", 9.2, color=P)
    b += note(12, 206, 336, ["EMPNO → DEPTNO → DNAME is transitive.", "Move the dependency DEPTNO → DNAME, LOC to a",
                             "new table DEPT; keep DEPTNO in EMP as a", "foreign key. Department data is now stored once."], size=9.4)
    return svg(360, 292, t + f'<g transform="translate(0,14)">{b}</g>')


DIAGRAMS = {"db3_anomalies": anomalies, "db3_fd": fd, "db3_fd_types": fd_types, "db3_keys": keys, "db3_steps": steps,
            "db3_1nf": nf1, "db3_2nf": nf2, "db3_3nf": nf3}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
