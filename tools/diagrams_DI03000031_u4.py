"""DI03000031 RDBMS - Unit 4 diagrams: integrity constraints and database objects."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000031", "diagrams")


# ------------------------------------------------------------------ 4.1
def constraints():
    b = title("Types of Integrity Constraints")
    b += rbox(180, 42, 170, 30, "Integrity Constraints", PF, P, 11.5, "bold", P)
    groups = [("Domain", "valid values", ["NOT NULL", "CHECK"], BLUE, BLUEF),
              ("Entity", "unique rows", ["UNIQUE", "PRIMARY KEY"], GREEN, GREENF),
              ("Referential", "valid links", ["FOREIGN KEY", "REFERENCES", "ON DELETE", "CASCADE"], ORANGE, ORANGEF)]
    for i, (a, d, items, s, f) in enumerate(groups):
        x = 14 + i * 113
        cx = x + 54
        b += line(f"M180 72 L180 84 L{cx} 84 L{cx} 96", GREY, 1.2)
        b += box(x, 96, 108, 40, f, s, 7, 1.5)
        b += text(cx, 111, a, 11, weight="bold", color=s) + text(cx, 127, d, 8.6, color=s)
        if a == "Referential":
            items = ["FOREIGN KEY", "REFERENCES", "ON DELETE CASCADE"]
        for j, c in enumerate(items):
            b += box(x + 4, 146 + j * 26, 100, 21, "#fff", s, 5, 1)
            b += text(cx, 156.5 + j * 26, c, 8.4 if len(c) > 12 else 9, mono=True)
    b += note(12, 236, 336, ["Column level: written with the column definition.",
                             "Table level: written after all columns; needed for",
                             "composite keys. Unnamed constraints get SYS_Cnnnnnn."], size=9.4)
    return svg(360, 296, b)


def pk_unique():
    b = title("PRIMARY KEY vs UNIQUE")
    rows = [["Feature", "PRIMARY KEY", "UNIQUE"],
            ["Duplicate values", "Not allowed", "Not allowed"],
            ["NULL values", "Not allowed", "Allowed"],
            ["Number per table", "Only one", "Many"],
            ["Index created", "Unique index", "Unique index"],
            ["Referenced by FK", "Yes", "Yes"]]
    b += grid(14, 44, [116, 108, 108], rows, rh=24, size=9.4)
    b += text(14, 206, "STUDENT", 9.8, anchor="start", weight="bold", color=P)
    b += grid(14, 214, [70, 120], [["ROLL (PK)", "EMAIL (UNIQUE)"], ["1", "aarav@mail.com"], ["2", "(NULL)"], ["3", "(NULL)"]], rh=21, size=9)
    b += lines(214, 236, ["ROLL: unique and", "never NULL.", "EMAIL: unique, but", "many NULLs are", "allowed."], 9.2, anchor="start", lh=14)
    return svg(360, 306, b)


def fk():
    b = title("Foreign Key: Parent and Child")
    b += text(14, 42, "DEPT (parent)", 10, anchor="start", weight="bold", color=GREEN)
    b += grid(14, 50, [62, 84], [["DEPTNO", "DNAME"], ["10", "ACCOUNTS"], ["20", "RESEARCH"], ["30", "SALES"]], head_fill=GREEN, rh=22, size=9.2)
    b += text(14, 48 + 4 * 22 + 14, "primary key", 8.6, anchor="start", color=GREEN)
    b += text(200, 42, "EMP (child)", 10, anchor="start", weight="bold", color=ORANGE)
    b += grid(200, 50, [70, 76], [["DEPTNO", "ENAME"], ["20", "AMIT"], ["20", "NEHA"], ["10", "HETAL"]], head_fill=ORANGE, rh=22, size=9.2)
    b += text(200, 48 + 4 * 22 + 14, "foreign key", 8.6, anchor="start", color=ORANGE)
    for (y1, y2), xv in zip(((83, 105), (105, 105), (127, 83)), (186, 186, 172)):
        b += line(f"M200 {y1} L{xv} {y1} L{xv} {y2} L154 {y2}", GREY, 1.1, "3 3") + arrowhead(148, y2, 180, 6, GREY)
    b += box(200, 166, 146, 22, REDF, RED, 0, 1.2)
    b += text(235, 177, "50", 9.2, weight="bold", color=RED) + text(308, 177, "RAVI", 9.2)
    b += text(200, 202, "50 is not in DEPT", 9, anchor="start", color=RED)
    b += text(200, 215, "ORA-02291: parent key not found", 7.9, anchor="start", color=RED, mono=True)
    b += note(12, 232, 336, ["A child value must match a parent key (or be NULL).",
                             "A parent row cannot be deleted while children",
                             "exist: ORA-02292 child record found.",
                             "Create the parent table first, drop the child first."], size=9.4)
    return svg(360, 306, b)


def cascade():
    b = title("Delete Rules: DELETE FROM dept WHERE deptno = 10")
    b = title("Delete Rules for a Parent Row")
    b += text(180, 42, "DELETE FROM dept WHERE deptno = 10;", 9.2, mono=True, color=P)
    panels = [("Default (no rule)", "Delete is rejected", [["AMIT", "20"], ["HETAL", "10"], ["RAJESH", "10"]], None, RED, REDF,
               "ORA-02292: child record found"),
              ("ON DELETE CASCADE", "Child rows deleted too", [["AMIT", "20"], ["HETAL", "10"], ["RAJESH", "10"]], "del", GREEN, GREENF,
               "rows of dept 10 removed"),
              ("ON DELETE SET NULL", "Child FK becomes NULL", [["AMIT", "20"], ["HETAL", "NULL"], ["RAJESH", "NULL"]], "null", BLUE, BLUEF,
               "employees kept, no dept")]
    for i, (h, sub, rows, mode, s, f, foot) in enumerate(panels):
        y = 56 + i * 92
        b += box(12, y, 336, 84, f, s, 8, 1.3)
        b += text(22, y + 16, h, 10.2, anchor="start", weight="bold", color=s, mono=True)
        b += text(22, y + 32, sub, 9.2, anchor="start")
        b += text(22, y + 70, foot, 8.6, anchor="start", color=s, mono=mode is None)
        b += grid(206, y + 6, [72, 56], [["ENAME", "DEPTNO"]] + rows, head_fill=s, rh=18, size=8.8)
        if mode == "del":
            for r in (2, 3):
                yy = y + 6 + r * 18 + 9
                b += line(f"M210 {yy} L330 {yy}", RED, 1.6)
    return svg(360, 56 + 3 * 92 + 4, b)


# ------------------------------------------------------------------ 4.2
def objects():
    b = title("Oracle Database Objects")
    items = [("TABLE", "stores data in rows and columns", "CREATE TABLE", BLUE, BLUEF),
             ("VIEW", "virtual table: a stored query", "CREATE VIEW", GREEN, GREENF),
             ("SYNONYM", "another name (alias) for an object", "CREATE SYNONYM", TEAL, TEALF),
             ("SEQUENCE", "generates unique numbers", "CREATE SEQUENCE", ORANGE, ORANGEF),
             ("INDEX", "speeds up searching of rows", "CREATE INDEX", RED, REDF)]
    for i, (n, d, c, s, f) in enumerate(items):
        y = 42 + i * 46
        b += box(12, y, 336, 40, f, s, 8, 1.3)
        b += box(18, y + 7, 84, 26, "#fff", s, 6, 1.2) + text(60, y + 20, n, 10, weight="bold", color=s)
        b += text(112, y + 15, d, 9.4, anchor="start")
        b += text(112, y + 30, c, 8.8, anchor="start", mono=True, color=s)
    b += note(12, 276, 336, ["All objects are stored in the data dictionary and", "can be seen with USER_TABLES, USER_VIEWS,",
                             "USER_SYNONYMS, USER_SEQUENCES, USER_INDEXES."], size=9.4)
    return svg(360, 336, b)


def view():
    b = title("A View is a Window on a Table")
    b += text(14, 42, "EMP (base table)", 10, anchor="start", weight="bold", color=BLUE)
    rows = [["EMPNO", "ENAME", "SAL", "DEPTNO"], ["101", "RAJESH", "90000", "10"], ["102", "AMIT", "60000", "20"],
            ["104", "NEHA", "45000", "20"], ["106", "SUNIL", "30000", "30"], ["105", "KIRAN", "22000", "20"]]
    b += grid(14, 50, [52, 62, 54, 52], rows, head_fill=BLUE, rh=20, size=9)
    for r in (2, 3, 5):
        b += f'<rect x="14" y="{50 + r * 20}" width="114" height="20" fill="{GREEN}" fill-opacity="0.16" stroke="none"/>'
    b += f'<rect x="12" y="48" width="118" height="124" fill="none" stroke="{GREEN}" stroke-width="2" stroke-dasharray="5 3" rx="3"/>'
    b += text(296, 100, "only these", 8.8, color=GREEN) + text(296, 113, "columns + rows", 8.8, color=GREEN)
    b += text(296, 126, "(deptno = 20)", 8.8, color=GREEN)
    b += line("M71 172 L71 178", GREEN, 1.4) + arrowhead(71, 184, 90, 6, GREEN)
    b += box(14, 184, 332, 40, "#fff", GREEN, 6, 1.2)
    b += text(22, 198, "CREATE VIEW emp20 AS SELECT empno, ename", 8.8, anchor="start", mono=True)
    b += text(22, 213, "FROM emp WHERE deptno = 20;", 8.8, anchor="start", mono=True)
    b += text(14, 244, "EMP20 (view)", 10, anchor="start", weight="bold", color=GREEN)
    b += grid(14, 252, [60, 70], [["EMPNO", "ENAME"], ["102", "AMIT"], ["104", "NEHA"], ["105", "KIRAN"]], head_fill=GREEN, rh=20, size=9)
    b += lines(160, 266, ["No data is stored in the view;", "only the SELECT is saved.", "Each query on EMP20 reads EMP,",
                          "so it always shows current data."], 9.2, anchor="start", lh=15)
    return svg(360, 340, b)


def view_types():
    b = title("Simple View vs Complex View")
    rows = [["Feature", "Simple view", "Complex view"],
            ["Base tables", "One table", "One or more"],
            ["Functions, GROUP BY", "No", "Yes"],
            ["DISTINCT / joins", "No", "Yes"],
            ["Expression columns", "No", "Yes"],
            ["INSERT/UPDATE/DELETE", "Allowed", "Not always"]]
    b += grid(14, 44, [128, 102, 102], rows, rh=24, size=9.2)
    b += box(14, 200, 332, 54, GREENF, GREEN, 7, 1.2)
    b += text(22, 216, "WITH CHECK OPTION", 9.6, anchor="start", weight="bold", color=GREEN, mono=True)
    b += text(22, 232, "DML through the view must give rows that the", 9, anchor="start")
    b += text(22, 245, "view can see (else ORA-01402).", 9, anchor="start")
    b += box(14, 262, 332, 40, REDF, RED, 7, 1.2)
    b += text(22, 278, "WITH READ ONLY", 9.6, anchor="start", weight="bold", color=RED, mono=True)
    b += text(22, 293, "No DML allowed through the view (ORA-42399).", 9, anchor="start")
    return svg(360, 312, b)


def sequence():
    b = title("Sequence: Automatic Number Generator")
    b += box(14, 44, 150, 72, ORANGEF, ORANGE, 8, 1.5)
    b += text(89, 60, "SEQUENCE seq_roll", 9.4, weight="bold", color=ORANGE, mono=True)
    b += text(89, 78, "START WITH 1", 8.8, mono=True) + text(89, 92, "INCREMENT BY 1", 8.8, mono=True)
    b += text(89, 106, "MAXVALUE 999", 8.8, mono=True)
    b += text(240, 52, "seq_roll.NEXTVAL", 9.2, mono=True, color=ORANGE, weight="bold")
    for i, v in enumerate(("1", "2", "3")):
        y = 64 + i * 22
        b += line(f"M166 80 L196 80 L196 {y + 9} L218 {y + 9}", GREY, 1.1) + arrowhead(224, y + 9, 0, 6, GREY)
        b += box(226, y, 30, 18, "#fff", ORANGE, 4, 1.1) + text(241, y + 9, v, 9.4, weight="bold")
        b += text(262, y + 9, ["1st call", "2nd call", "3rd call"][i], 8.6, anchor="start", color=GREY)
    b += text(14, 152, "INSERT INTO student VALUES (seq_roll.NEXTVAL, ...);", 8.6, anchor="start", mono=True)
    b += grid(14, 162, [60, 90], [["ROLL", "NAME"], ["1", "Aarav"], ["2", "Diya"], ["3", "Karan"]], head_fill=ORANGE, rh=20, size=9)
    b += lines(180, 176, ["NEXTVAL: gives the next", "number (and advances).", "CURRVAL: the last number", "given in this session (3)."],
               9.2, anchor="start", lh=15)
    b += note(12, 252, 336, ["Used for primary keys such as roll no, bill no.",
                             "Numbers are never reused, even after ROLLBACK."], size=9.4)
    return svg(360, 296, b)


def index():
    b = title("Index on EMP(ENAME)")
    b += text(14, 42, "Index (sorted)", 10, anchor="start", weight="bold", color=RED)
    idx = [["ENAME", "ROWID"], ["AMIT", "r2"], ["HETAL", "r5"], ["KIRAN", "r1"], ["NEHA", "r4"], ["PRIYA", "r3"]]
    b += grid(14, 50, [62, 46], idx, head_fill=RED, rh=22, size=9)
    b += text(200, 42, "EMP table (unsorted)", 10, anchor="start", weight="bold", color=BLUE)
    tbl = [["ROW", "ENAME", "SAL"], ["r1", "KIRAN", "22000"], ["r2", "AMIT", "60000"], ["r3", "PRIYA", "58000"],
           ["r4", "NEHA", "45000"], ["r5", "HETAL", "40000"]]
    b += grid(200, 50, [36, 60, 50], tbl, head_fill=BLUE, rh=22, size=9)
    pairs = {1: 2, 2: 5, 3: 1, 4: 4, 5: 3}
    for i, r in pairs.items():
        y1, y2 = 50 + i * 22 + 11, 50 + r * 22 + 11
        b += line(f"M122 {y1} C160 {y1} 160 {y2} 192 {y2}", GREY if i != 4 else RED, 1.1 if i != 4 else 1.8) + arrowhead(198, y2, 0, 6, GREY if i != 4 else RED)
    b += text(14, 200, "WHERE ename = 'NEHA'", 9.2, anchor="start", mono=True, color=RED)
    b += note(12, 212, 336, ["Without index: every row is read (full table scan).",
                             "With index: search the sorted key, then jump to", "the row using its ROWID (like a book index).",
                             "PRIMARY KEY and UNIQUE create an index automatically."], size=9.4)
    return svg(360, 286, b)


DIAGRAMS = {"db4_constraints": constraints, "db4_pk_unique": pk_unique, "db4_fk": fk, "db4_cascade": cascade,
            "db4_objects": objects, "db4_view": view, "db4_view_types": view_types, "db4_sequence": sequence, "db4_index": index}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
