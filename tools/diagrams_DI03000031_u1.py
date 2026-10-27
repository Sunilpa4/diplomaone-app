"""DI03000031 RDBMS - Unit 1 diagrams: data and information, database concepts, architecture, SQL command classes, DCL, transactions."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000031", "diagrams")
GREY = "#666"
PF = "#F1E8FC"


def lines(cx, y, ls, size=10, color=INK, lh=14, weight="normal", anchor="middle"):
    return "".join(text(cx, y + i * lh, s, size, color=color, weight=weight, anchor=anchor) for i, s in enumerate(ls))


def rarrow(x1, x2, y, color=INK):
    return line(f"M{x1} {y} L{x2 - 6} {y}", color, 1.6) + arrowhead(x2, y, 0, 7, color)


def grid(x, y, cw, rows, head_fill=P, rh=20, size=9, hl_col=None, hl_row=None):
    """Small table: rows[0] is the header."""
    b = ""
    for r, row in enumerate(rows):
        cx = x
        for c, v in enumerate(row):
            if r == 0:
                f, col, wt = head_fill, "#fff", "bold"
            else:
                f = "#fff"
                if hl_col is not None and c == hl_col:
                    f = YEL
                if hl_row is not None and r == hl_row:
                    f = GREENF
                col, wt = INK, "normal"
            b += box(cx, y + r * rh, cw[c], rh, f, "#C9B3EC", 0, 1)
            b += text(cx + cw[c] / 2, y + r * rh + rh / 2, v, size, color=col, weight=wt)
            cx += cw[c]
    return b


# ------------------------------------------------------------------ 1.1
def data_info():
    b = title("Data, Processing and Information")
    b += box(14, 44, 98, 112, BLUEF, BLUE, 8, 1.5) + text(63, 60, "DATA", 12, weight="bold", color=BLUE)
    b += lines(63, 80, ["Aarav", "82", "Surat", "CE"], 9.6)
    b += text(63, 146, "raw facts", 9, color=GREY)
    b += rarrow(114, 140, 100)
    b += box(142, 64, 76, 72, ORANGEF, ORANGE, 8, 1.5) + lines(180, 88, ["Processing", "sort, sum,", "compare"], 9.4, lh=14)
    b += rarrow(220, 246, 100)
    b += box(248, 44, 98, 112, GREENF, GREEN, 8, 1.5) + text(297, 60, "INFORMATION", 10.5, weight="bold", color=GREEN)
    b += lines(297, 82, ["Aarav of CE", "scored 82,", "rank 2 in", "class"], 9.2, lh=14)
    b += text(297, 146, "meaningful", 9, color=GREY)
    b += note(12, 172, 336, [(" Data: raw, unorganised facts (no meaning alone).", INK),
                             " Information: processed data that is meaningful", "  and useful for decision making.",
                             " Information of one step = data for the next step."], size=9.6)
    return svg(360, 244, b)


def hierarchy():
    b = title("Data Item, Record, File and Database")
    rows = [["ROLLNO", "NAME", "BRANCH", "MARKS"], ["1", "Aarav Patel", "CE", "82"], ["2", "Diya Shah", "IT", "91"],
            ["3", "Karan Mehta", "CE", "67"]]
    b += text(180, 42, "STUDENT file / table", 10.5, weight="bold", color=P)
    b += grid(40, 52, [56, 104, 60, 60], rows, hl_col=1, hl_row=2)
    b += text(40, 146, "yellow column = data item (field)", 9.4, anchor="start", color=YELS_C)
    b += text(40, 162, "green row = record (one student)", 9.4, anchor="start", color=GREEN)
    y = 182
    lv = [("Data item / field", "smallest unit: NAME = 'Diya Shah'", YEL, YELS_C),
          ("Record", "related fields of one entity", GREENF, GREEN),
          ("File / table", "collection of similar records", BLUEF, BLUE),
          ("Database", "collection of related files", PF, P)]
    for i, (a, d, f, s) in enumerate(lv):
        yy = y + i * 40
        b += box(20, yy, 320, 30, f, s, 7, 1.4)
        b += text(30, yy + 15, a, 10.2, anchor="start", weight="bold", color=s) + text(330, yy + 15, d, 9.2, anchor="end")
        if i < 3:
            b += down(180, yy + 30, yy + 40)
    return svg(360, y + 4 * 40 + 6, b)


YELS_C = "#9A7300"


def dictionary():
    b = title("Metadata in the Data Dictionary")
    b += text(180, 42, "Data dictionary entry for table STUDENT", 10, weight="bold", color=P)
    rows = [["Column", "Type", "Size", "Null?", "Key"], ["ROLLNO", "NUMBER", "3", "NO", "PK"],
            ["NAME", "VARCHAR2", "15", "NO", ""], ["BRANCH", "VARCHAR2", "5", "YES", ""], ["MARKS", "NUMBER", "3", "YES", ""]]
    b += grid(24, 52, [72, 78, 50, 56, 56], rows)
    b += note(12, 170, 336, [("Metadata = data about data.", P), "It describes the structure of the data: names,",
                             "types, sizes, constraints, owners, privileges.", ("Data dictionary (system catalog):", P),
                             "a set of read-only tables where the DBMS keeps", "all metadata. In Oracle: USER_TABLES,",
                             "USER_TAB_COLUMNS, USER_CONSTRAINTS ..."], size=9.6)
    return svg(360, 288, b)


# ------------------------------------------------------------------ 1.2
def file_vs_db():
    b = title("File System vs Database System")
    b += text(90, 42, "File processing", 10.5, weight="bold", color=RED)
    b += text(270, 42, "Database approach", 10.5, weight="bold", color=GREEN)
    b += line("M180 34 L180 236", "#ddd", 1.2, "4 3")
    for i, (a, f) in enumerate([("Fees app", "fees.dat"), ("Exam app", "exam.dat"), ("Library", "lib.dat")]):
        y = 62 + i * 52
        b += rbox(50, y + 10, 70, 26, a, BLUEF, BLUE, 9.4)
        b += rarrow(86, 104, y + 10)
        b += rbox(136, y + 10, 62, 26, f, REDF, RED, 9.2)
    b += text(90, 222, "same student data repeated", 9, color=RED)
    for i, a in enumerate(["Fees app", "Exam app", "Library"]):
        y = 62 + i * 52
        b += rbox(226, y + 10, 70, 26, a, BLUEF, BLUE, 9.4)
        b += line(f"M262 {y + 10} L282 {y + 10} L282 114", INK, 1.4)
    b += arrowhead(290, 114, 0, 7, INK)
    b += box(292, 86, 56, 56, GREENF, GREEN, 8, 1.6) + lines(320, 106, ["DBMS", "+ DB"], 10, weight="bold", color=GREEN)
    b += text(270, 222, "one shared database", 9, color=GREEN)
    b += note(12, 240, 336, [(" File system problems:", RED), "  redundancy, inconsistency, difficult access,",
                             "  no security, no concurrent access, no recovery.", (" DBMS solves them:", GREEN),
                             "  shared data, integrity, security, backup."], size=9.6)
    return svg(360, 330, b)


def environment():
    b = title("Database System Environment")
    us = [("Naive", "users"), ("App", "programmers"), ("Casual", "users"), ("DBA", "")]
    for i, (a, c) in enumerate(us):
        x = 54 + i * 84
        b += rbox(x, 50, 74, 34, "", GREENF, GREEN) + text(x, 45 if c else 50, a, 9.6, weight="bold", color=GREEN)
        if c:
            b += text(x, 58, c, 8.6, color=GREEN)
    b += line("M54 67 L54 82 M138 67 L138 82 M222 67 L222 82 M306 67 L306 82", GREY, 1.2)
    b += down(180, 82, 96)
    b += line("M54 82 L306 82", GREY, 1.2)
    b += rbox(180, 112, 300, 30, "Application programs / SQL queries", BLUEF, BLUE, 10, "bold", BLUE)
    b += down(180, 127, 144)
    b += box(30, 146, 300, 112, PF, P, 9, 2) + text(180, 162, "DBMS software", 11.5, weight="bold", color=P)
    b += rbox(105, 192, 130, 36, "", "#fff", P) + lines(105, 188, ["Query processor"], 9.6, weight="bold")
    b += text(105, 202, "parse, optimise, run", 8.4, color=GREY)
    b += rbox(255, 192, 130, 36, "", "#fff", P) + lines(255, 188, ["Storage manager"], 9.6, weight="bold")
    b += text(255, 202, "files, buffers, locks", 8.4, color=GREY)
    b += rbox(180, 236, 280, 22, "Transaction manager | Security | Recovery", "#fff", P, 9)
    b += down(105, 258, 278) + down(255, 258, 278)
    b += f'<ellipse cx="105" cy="284" rx="56" ry="7" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += box(49, 284, 112, 30, ORANGEF, ORANGE, 0, 1.4).replace('stroke-width="1.4"', 'stroke-width="0"')
    b += line("M49 284 L49 314 M161 284 L161 314", ORANGE, 1.4)
    b += f'<ellipse cx="105" cy="314" rx="56" ry="7" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += text(105, 298, "Stored database", 9.6, weight="bold", color=ORANGE)
    b += f'<ellipse cx="255" cy="284" rx="56" ry="7" fill="{TEALF}" stroke="{TEAL}" stroke-width="1.4"/>'
    b += box(199, 284, 112, 30, TEALF, TEAL, 0, 0)
    b += line("M199 284 L199 314 M311 284 L311 314", TEAL, 1.4)
    b += f'<ellipse cx="255" cy="314" rx="56" ry="7" fill="{TEALF}" stroke="{TEAL}" stroke-width="1.4"/>'
    b += text(255, 298, "Data dictionary", 9.6, weight="bold", color=TEAL)
    b += note(12, 330, 336, ["Components: hardware, software (DBMS), data,", "procedures and users."], size=9.6)
    return svg(360, 372, b)


def three_level():
    t = title("Three-Level (ANSI/SPARC) Architecture")
    b = ""
    for i, v in enumerate(["View 1", "View 2", "View 3"]):
        x = 80 + i * 100
        b += rbox(x, 54, 84, 28, v, GREENF, GREEN, 10, "bold", GREEN)
        b += line(f"M{x} 68 L180 104", GREY, 1.2)
    b += text(14, 31, "External level: user views", 9.6, anchor="start", weight="bold", color=GREEN)
    b += text(352, 88, "external/conceptual", 8.4, anchor="end", color=GREY) + text(352, 99, "mapping", 8.4, anchor="end", color=GREY)
    b += rbox(180, 120, 240, 32, "Conceptual schema", BLUEF, BLUE, 11, "bold", BLUE)
    b += text(14, 148, "Conceptual level: whole DB, tables, relations", 9.2, anchor="start", color=BLUE)
    b += down(180, 154, 178)
    b += text(352, 170, "conceptual/internal mapping", 8.4, anchor="end", color=GREY)
    b += rbox(180, 194, 240, 32, "Internal schema", ORANGEF, ORANGE, 11, "bold", ORANGE)
    b += text(14, 222, "Internal level: storage, indexes, file layout", 9.2, anchor="start", color=ORANGE)
    b += down(180, 228, 246)
    b += f'<ellipse cx="180" cy="252" rx="70" ry="7" fill="{PF}" stroke="{P}" stroke-width="1.4"/>'
    b += box(110, 252, 140, 26, PF, P, 0, 0) + line("M110 252 L110 278 M250 252 L250 278", P, 1.4)
    b += f'<ellipse cx="180" cy="278" rx="70" ry="7" fill="{PF}" stroke="{P}" stroke-width="1.4"/>'
    b += text(180, 266, "Stored database", 10, weight="bold", color=P)
    b += note(12, 296, 336, [("Logical data independence:", P), " change conceptual schema without changing views.",
                             ("Physical data independence:", P), " change internal schema without changing", " the conceptual schema."], size=9.6)
    return svg(360, 400, t + f'<g transform="translate(0,16)">{b}</g>')


# ------------------------------------------------------------------ 1.3
def schema_instance():
    b = title("Schema, Sub-schema and Instance")
    b += text(180, 42, "Schema (structure, rarely changes)", 10, weight="bold", color=BLUE)
    b += box(30, 50, 300, 26, BLUEF, BLUE, 6, 1.4)
    b += text(180, 63, "STUDENT(rollno, name, branch, city, marks)", 9.6, mono=True)
    b += text(180, 98, "Instance (data at one moment, changes often)", 10, weight="bold", color=GREEN)
    rows = [["ROLLNO", "NAME", "BRANCH", "CITY", "MARKS"], ["1", "Aarav", "CE", "Surat", "82"], ["2", "Diya", "IT", "Vadodara", "91"]]
    b += grid(30, 106, [54, 62, 56, 72, 56], rows)
    b += text(180, 186, "Sub-schema (part of schema seen by a user)", 10, weight="bold", color=ORANGE)
    b += box(30, 194, 300, 26, ORANGEF, ORANGE, 6, 1.4)
    b += text(180, 207, "Exam cell view: (rollno, name, marks)", 9.6, mono=True)
    b += note(12, 232, 336, ["Schema = design / blueprint (like a class).", "Instance = actual data stored now (like objects).",
                             "Sub-schema = subset of the schema for one user", "group; hides other data (security)."], size=9.6)
    return svg(360, 302, b)


# ------------------------------------------------------------------ 1.5
def sql_cmds():
    b = title("Classification of SQL Commands")
    b += rbox(180, 46, 120, 30, "SQL", PF, P, 13, "bold", P)
    groups = [("DDL", "Definition", ["CREATE", "ALTER", "DROP", "TRUNCATE", "RENAME"], BLUE, BLUEF),
              ("DML", "Manipulation", ["INSERT", "UPDATE", "DELETE"], GREEN, GREENF),
              ("DQL", "Query", ["SELECT"], TEAL, TEALF),
              ("DCL", "Control", ["GRANT", "REVOKE"], ORANGE, ORANGEF),
              ("TCL", "Transaction", ["COMMIT", "ROLLBACK", "SAVEPOINT"], RED, REDF)]
    w = 66
    for i, (a, d, cmds, s, f) in enumerate(groups):
        x = 15 + i * (w + 0) + i * 1
        cx = x + w / 2
        b += line(f"M180 61 L180 74 L{cx} 74 L{cx} 86", GREY, 1.2)
        b += box(x + 2, 86, w - 4, 38, f, s, 7, 1.5)
        b += text(cx, 101, a, 11.5, weight="bold", color=s) + text(cx, 116, d, 8.2, color=s)
        for j, c in enumerate(cmds):
            b += box(x + 4, 132 + j * 24, w - 8, 20, "#fff", s, 5, 1)
            b += text(cx, 142 + j * 24, c, 8.2, mono=True)
    b += note(12, 262, 336, ["DDL changes structure (auto-commit in Oracle).", "DML changes data rows (needs COMMIT).",
                             "DQL reads data. DCL gives/takes privileges.", "TCL controls transactions."], size=9.6)
    return svg(360, 334, b)


# ------------------------------------------------------------------ 1.6
def dcl():
    b = title("Users, Roles and Privileges (DCL)")
    b += rbox(180, 50, 120, 30, "DBA / owner", PF, P, 10.5, "bold", P)
    b += down(180, 65, 92)
    b += text(186, 82, "GRANT SELECT, INSERT", 9, anchor="start", color=GREEN, mono=True)
    b += rbox(180, 108, 150, 30, "ROLE: clerk_role", ORANGEF, ORANGE, 10.5, "bold", ORANGE)
    for i, u in enumerate(["ravi", "meena", "jay"]):
        x = 80 + i * 100
        b += line(f"M180 123 L{x} 150", GREY, 1.3) + arrowhead(x, 154, 90 if x == 180 else (115 if x < 180 else 65), 7, GREY)
        b += rbox(x, 170, 80, 28, "user " + u, BLUEF, BLUE, 9.6)
    b += text(180, 204, "every user of the role gets its privileges", 9, color=GREY)
    b += box(20, 216, 156, 76, GREENF, GREEN, 7, 1.3) + text(98, 232, "System privileges", 10, weight="bold", color=GREEN)
    b += lines(98, 250, ["CREATE SESSION", "CREATE TABLE", "CREATE VIEW"], 8.8, lh=13)
    b += box(184, 216, 156, 76, BLUEF, BLUE, 7, 1.3) + text(262, 232, "Object privileges", 10, weight="bold", color=BLUE)
    b += lines(262, 250, ["SELECT, INSERT, UPDATE", "DELETE, ALTER, INDEX", "on a table/view"], 8.8, lh=13)
    b += note(12, 302, 336, ["GRANT gives privileges; REVOKE takes them back.", "WITH GRANT OPTION lets the user grant further."], size=9.6)
    return svg(360, 346, b)


# ------------------------------------------------------------------ 1.7
def acid():
    b = title("ACID Properties of a Transaction")
    b += text(180, 40, "Transfer Rs 500 from account A to B", 10, weight="bold", color=P)
    b += box(60, 48, 240, 36, "#FBF8FF", P, 6, 1.2)
    b += text(180, 61, "UPDATE A: bal = bal - 500", 9.2, mono=True) + text(180, 76, "UPDATE B: bal = bal + 500", 9.2, mono=True)
    items = [("A", "Atomicity", ["all or nothing:", "both updates or none"], BLUE, BLUEF),
             ("C", "Consistency", ["A+B total stays", "the same (valid state)"], GREEN, GREENF),
             ("I", "Isolation", ["others don't see half-", "done work"], ORANGE, ORANGEF),
             ("D", "Durability", ["after COMMIT, change", "survives crash"], RED, REDF)]
    for i, (k, n, d, s, f) in enumerate(items):
        x = 14 + (i % 2) * 170
        y = 96 + (i // 2) * 82
        b += box(x, y, 162, 72, f, s, 8, 1.5)
        b += f'<circle cx="{x + 20}" cy="{y + 20}" r="12" fill="{s}"/>' + text(x + 20, y + 20, k, 12, weight="bold", color="#fff")
        b += text(x + 40, y + 20, n, 11, anchor="start", weight="bold", color=s)
        b += lines(x + 81, y + 44, d, 9.2, lh=13)
    b += note(12, 264, 336, ["Atomicity: ROLLBACK / recovery manager", "Consistency: constraints + correct program",
                             "Isolation: locking (concurrency control)", "Durability: redo logs, backup"], size=9.4)
    return svg(360, 336, b)


def tx_states():
    b = title("States of a Transaction")
    S = {"act": (56, 120, "Active"), "pc": (170, 62, "Partially\ncommitted"), "com": (306, 62, "Committed"),
         "fail": (170, 178, "Failed"), "abo": (306, 178, "Aborted")}
    cols = {"act": BLUE, "pc": ORANGE, "com": GREEN, "fail": RED, "abo": RED}
    fills = {"act": BLUEF, "pc": ORANGEF, "com": GREENF, "fail": REDF, "abo": REDF}

    def ar(a, c, lab, ly):
        (x1, y1, _), (x2, y2, _) = S[a], S[c]
        import math
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        sx, sy, ex, ey = x1 + dx * 41, y1 + dy * 24, x2 - dx * 43, y2 - dy * 24
        return line(f"M{sx:.1f} {sy:.1f} L{ex:.1f} {ey:.1f}", INK, 1.5) + arrowhead(ex + dx * 2, ey + dy * 2, ang, 7) + ly
    b += ar("act", "pc", "", text(96, 80, "last statement", 8.6, color=GREY, anchor="end"))
    b += ar("pc", "com", "", text(238, 52, "COMMIT", 8.2, color=GREEN, weight="bold"))
    b += ar("act", "fail", "", text(96, 166, "error", 8.6, color=RED, anchor="end"))
    b += ar("pc", "fail", "", text(176, 122, "failure", 8.6, color=RED, anchor="start"))
    b += ar("fail", "abo", "", text(238, 192, "ROLLBACK", 8.2, color=RED, weight="bold"))
    for k, (x, y, lab) in S.items():
        ls = lab.split("\n")
        b += box(x - 40, y - 22, 80, 44, fills[k], cols[k], 20, 1.6)
        b += lines(x, y - (len(ls) - 1) * 6, ls, 9.8, lh=12, weight="bold", color=cols[k])
    b += note(12, 214, 336, ["Active: statements are running.", "Partially committed: last statement done,",
                             " changes still in memory.", "Committed: changes saved permanently.",
                             "Failed/Aborted: error, changes undone; the", " transaction may be restarted or killed."], size=9.4)
    return svg(360, 314, b)


def savepoint():
    b = title("SAVEPOINT and ROLLBACK TO")
    steps = [("INSERT 6", BLUE), ("SAVEPOINT a", ORANGE), ("UPDATE", BLUE), ("SAVEPOINT b", ORANGE), ("DELETE 5", BLUE)]
    y0 = 58
    b += line(f"M30 {y0} L330 {y0}", INK, 2) + arrowhead(334, y0, 0, 8)
    b += text(330, y0 - 12, "time", 9, color=GREY, anchor="end")
    for i, (s, c) in enumerate(steps):
        x = 50 + i * 64
        b += f'<circle cx="{x}" cy="{y0}" r="6" fill="{c}"/>'
        b += text(x, y0 + 20, s.split()[0], 8.8, weight="bold", color=c) + text(x, y0 + 32, s.split()[1] if " " in s else "", 8.8, color=c)
    # rollback to b
    b += line(f"M306 {y0 + 44} Q 270 {y0 + 70} 242 {y0 + 44}", RED, 1.6, "4 3") + arrowhead(242, y0 + 42, 225, 7, RED)
    b += text(274, y0 + 84, "ROLLBACK TO b", 9.2, weight="bold", color=RED, mono=True)
    b += text(274, y0 + 97, "undoes DELETE only", 8.8, color=RED)
    b += line(f"M306 {y0 + 104} Q 200 {y0 + 160} 114 {y0 + 46}", ORANGE, 1.6, "4 3") + arrowhead(114, y0 + 44, 235, 7, ORANGE)
    b += text(160, y0 + 140, "ROLLBACK TO a", 9.2, weight="bold", color=ORANGE, mono=True)
    b += text(160, y0 + 153, "undoes UPDATE + DELETE", 8.8, color=ORANGE)
    b += note(12, 226, 336, ["ROLLBACK (no name): undoes everything since", " the last COMMIT; all savepoints are erased.",
                             "COMMIT: makes all changes permanent.", "DDL (CREATE/ALTER/DROP) commits automatically."], size=9.4)
    return svg(360, 298, b)


DIAGRAMS = {"db1_data_info": data_info, "db1_hierarchy": hierarchy, "db1_dictionary": dictionary, "db1_file_vs_db": file_vs_db,
            "db1_environment": environment, "db1_three_level": three_level, "db1_schema_instance": schema_instance,
            "db1_sql_cmds": sql_cmds, "db1_dcl": dcl, "db1_acid": acid, "db1_tx_states": tx_states, "db1_savepoint": savepoint}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
