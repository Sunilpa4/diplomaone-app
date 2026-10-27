"""DI03000031 RDBMS - Unit 5 diagrams: PL/SQL and triggers."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000031", "diagrams")
NB = "\u00a0"


def code(x, y, ls, size=8.6, lh=13, color=INK):
    return "".join(text(x, y + i * lh, s.replace(" ", NB), size, anchor="start", mono=True, color=color) for i, s in enumerate(ls))


# ------------------------------------------------------------------ 5.1
def block():
    b = title("PL/SQL Block Structure")
    secs = [(44, 56, BLUEF, BLUE, "DECLARE", ["-- variables, constants,", "-- cursors, exceptions"], "Declaration section", "Optional"),
            (106, 62, GREENF, GREEN, "BEGIN", ["-- SQL statements and", "-- PL/SQL statements"], "Executable section", "Mandatory"),
            (174, 56, ORANGEF, ORANGE, "EXCEPTION", ["-- error handlers", "-- WHEN ... THEN"], "Exception section", "Optional"),
            (236, 26, PF, P, "END;", [], "End of block", "Mandatory")]
    for y, h, f, s, kw, cm, name, req in secs:
        b += box(14, y, 170, h, f, s, 6, 1.5)
        b += text(24, y + 15, kw, 10, anchor="start", weight="bold", color=s, mono=True)
        b += code(24, y + 31, cm, 8.4, 13, GREY)
        b += text(194, y + h / 2 - 4, name, 9.4, anchor="start", weight="bold", color=s)
        b += text(194, y + h / 2 + 10, req, 9, anchor="start", color=RED if req == "Mandatory" else GREY)
    b += note(12, 274, 336, ["Anonymous block: no name, not stored, runs once.",
                             "Named blocks: procedure, function, trigger; they",
                             "are compiled and stored in the database."], size=9.4)
    return svg(360, 340, b)


def engine():
    b = title("PL/SQL Engine")
    b += box(130, 42, 218, 174, PF, P, 8, 1.5)
    b += text(239, 56, "Oracle Server", 10, weight="bold", color=P)
    b += box(12, 58, 100, 84, BLUEF, BLUE, 6, 1.5)
    b += text(62, 71, "PL/SQL block", 9, weight="bold", color=BLUE)
    b += code(20, 87, ["BEGIN", " IF ...", " UPDATE ...", "END;"], 8.4, 13)
    b += rarrow(112, 142, 100, BLUE)
    b += line("M239 142 L239 160", ORANGE, 1.6) + arrowhead(239, 166, 90, 7, ORANGE)
    b += box(142, 66, 194, 76, "#fff", P, 6, 1.3)
    b += text(239, 79, "PL/SQL Engine", 9.6, weight="bold", color=P)
    b += box(152, 88, 174, 22, GREENF, GREEN, 4, 1.1)
    b += text(239, 99, "Procedural statement executor", 8.6, color=GREEN)
    b += text(239, 128, "IF, LOOP, :=, variables", 8.6, color=GREY)
    b += text(246, 154, "SQL statements", 8.4, anchor="start", color=ORANGE)
    b += box(142, 168, 194, 40, ORANGEF, ORANGE, 6, 1.3)
    b += text(239, 182, "SQL Statement Executor", 9.4, weight="bold", color=ORANGE)
    b += text(239, 198, "SELECT, INSERT, UPDATE ...", 8.6)
    b += note(12, 228, 336, ["SQL alone: every statement goes to the server",
                             "separately (many network trips).",
                             "PL/SQL: the whole block is sent at once. Procedural",
                             "parts run in the PL/SQL engine, SQL in the SQL engine."], size=9.2)
    return svg(360, 310, b)


def type_rowtype():
    b = title("%TYPE and %ROWTYPE")
    w = [56, 64, 72, 56, 56]
    b += text(28, 44, "EMP table", 9.6, anchor="start", weight="bold", color=P)
    b += grid(28, 50, w, [["EMPNO", "ENAME", "JOB", "SAL", "DEPTNO"], ["104", "NEHA", "ANALYST", "45000", "20"]], rh=22, size=9)
    b += line("M248 95 L248 124", BLUE, 1.5) + arrowhead(248, 130, 90, 7, BLUE)
    b += code(28, 140, ["v_sal emp.sal%TYPE;"], 9.4, color=BLUE)
    b += text(28, 157, "same data type as one column", 9, anchor="start")
    b += box(200, 132, 96, 24, BLUEF, BLUE, 5, 1.2) + text(248, 144, "v_sal = 45000", 9, mono=True)
    b += code(28, 190, ["v_emp emp%ROWTYPE;"], 9.4, color=GREEN)
    b += text(200, 190, "one field per column", 9, anchor="start", color=GREEN)
    b += grid(28, 200, w, [["empno", "ename", "job", "sal", "deptno"], ["104", "NEHA", "ANALYST", "45000", "20"]], head_fill=GREEN, rh=22, size=9)
    b += code(28, 262, ["v_emp.ename = 'NEHA'   v_emp.sal = 45000"], 8.6)
    b += note(12, 276, 336, ["Advantage: if the column type or table changes,",
                             "the variable changes automatically (no code edit)."], size=9.4)
    return svg(360, 328, b)


# ------------------------------------------------------------------ 5.2
def if_flow():
    b = title("IF-THEN-ELSIF-ELSE Flow")
    b += arr([(168, 76), (207, 76)], label="Yes", lpos=(187, 68))
    b += arr([(110, 101), (110, 125)], label="No", lpos=(124, 114))
    b += arr([(168, 150), (207, 150)], label="Yes", lpos=(187, 142))
    b += arr([(110, 175), (110, 207)], label="No", lpos=(124, 192))
    b += line("M317 76 L340 76 L340 284 L234 284") + arrowhead(228, 284, 180, 7, INK)
    b += line("M317 150 L340 150")
    b += arr([(110, 237), (110, 284), (132, 284)])
    b += decision(110, 76, "marks >= 70", w=116, h=50, size=10, mono=True)
    b += decision(110, 150, "marks >= 50", w=116, h=50, size=10, mono=True)
    b += process(262, 76, "grade := 'A'", w=110, h=30, size=10, mono=True)
    b += process(262, 150, "grade := 'B'", w=110, h=30, size=10, mono=True)
    b += process(110, 222, "grade := 'C'", w=110, h=30, size=10, mono=True)
    b += text(176, 222, "ELSE part", 8.8, anchor="start", color=GREY)
    b += terminal(180, 284, "END IF", w=96, h=28, size=10.5)
    b += note(12, 310, 336, ["Only the first TRUE condition runs. ELSE runs when",
                             "no condition is TRUE. Every IF needs END IF;"], size=9.4)
    return svg(360, 362, b)


def loops():
    b = title("Loops in PL/SQL")
    cols = [("Basic LOOP", BLUE, BLUEF, ["LOOP", "  i := i + 1;", "  EXIT WHEN", "    i > 5;", "END LOOP;"]),
            ("WHILE LOOP", GREEN, GREENF, ["WHILE i <= 5", "LOOP", "  i := i + 1;", "END LOOP;"]),
            ("FOR LOOP", ORANGE, ORANGEF, ["FOR i IN 1..5", "LOOP", "  stmt;", "END LOOP;"])]
    for k, (h, s, f, ls) in enumerate(cols):
        x = 10 + k * 116
        b += box(x, 44, 108, 24, s, s, 5, 1.2) + text(x + 54, 56, h, 9.6, weight="bold", color="#fff")
        b += box(x, 72, 108, 96, f, s, 5, 1.2)
        b += code(x + 8, 90, ls, 8.4, 15)
    rows = [["Feature", "Basic", "WHILE", "FOR"],
            ["Condition", "inside (EXIT)", "at start", "range"],
            ["Min. runs", "1", "0", "0"],
            ["Counter", "manual", "manual", "automatic"],
            ["Use when", "exit in middle", "count unknown", "count known"]]
    b += grid(6, 182, [96, 84, 84, 84], rows, rh=22, size=8.8)
    return svg(360, 304, b)


# ------------------------------------------------------------------ 5.3
def cursor():
    b = title("Cursor: Context Area and Active Set")
    b += code(14, 46, ["CURSOR c_emp IS SELECT ename, sal", "  FROM emp WHERE deptno = 20;"], 8.8)
    b += text(40, 80, "Active set (result rows)", 9, anchor="start", weight="bold", color=P)
    b += grid(40, 88, [80, 70], [["ENAME", "SAL"], ["AMIT", "60000"], ["NEHA", "45000"], ["KIRAN", "22000"]], rh=22, size=9, hl_row=2)
    b += line("M14 143 L32 143", RED, 1.8) + arrowhead(38, 143, 0, 7, RED)
    b += text(14, 192, "pointer after 2nd FETCH", 8.8, anchor="start", color=RED)
    b += line("M192 143 L226 143", GREEN, 1.6) + arrowhead(232, 143, 0, 7, GREEN)
    b += text(212, 135, "FETCH", 8.6, weight="bold", color=GREEN)
    b += box(236, 121, 112, 44, GREENF, GREEN, 6, 1.3)
    b += text(292, 136, "v_ename = NEHA", 8.6, mono=True) + text(292, 152, "v_sal = 45000", 8.6, mono=True)
    rows = [["", "Implicit", "Explicit"],
            ["Created by", "Oracle (auto)", "programmer"],
            ["Used for", "DML, SELECT INTO", "multi-row SELECT"],
            ["Name", "SQL", "user given"],
            ["Control", "none", "OPEN/FETCH/CLOSE"]]
    b += grid(11, 204, [82, 128, 128], rows, rh=21, size=8.8)
    return svg(360, 322, b)


def cursor_steps():
    b = title("Explicit Cursor: Four Steps")
    b += down(120, 76, 92) + down(120, 122, 136) + down(120, 171, 187)
    b += arr([(120, 240), (120, 265)], label="Yes", lpos=(134, 254))
    b += arr([(175, 214), (206, 214)], label="No", lpos=(190, 206))
    b += line("M262 199 L262 154 L197 154") + arrowhead(191, 154, 180, 7, INK)
    b += process(120, 62, "1. DECLARE cursor", w=150, h=28, size=10)
    b += process(120, 107, "2. OPEN cursor", w=150, h=28, size=10)
    b += io(120, 154, "3. FETCH INTO vars", w=140, h=32, size=10)
    b += decision(120, 214, "%NOTFOUND?", w=110, h=52, size=9.6, mono=True)
    b += process(262, 214, "Process row", w=100, h=30, size=10)
    b += process(120, 280, "4. CLOSE cursor", w=150, h=28, size=10)
    b += text(204, 62, "names the query", 8.8, anchor="start", color=GREY)
    b += text(204, 107, "runs the query", 8.8, anchor="start", color=GREY)
    b += text(204, 280, "frees the memory", 8.8, anchor="start", color=GREY)
    b += note(12, 304, 336, ["Attributes: %ISOPEN, %FOUND, %NOTFOUND, %ROWCOUNT.",
                             "A cursor FOR loop does OPEN, FETCH and CLOSE",
                             "automatically."], size=9.4)
    return svg(360, 370, b)


# ------------------------------------------------------------------ 5.4
def exceptions():
    b = title("Types of Exceptions")
    kids = [("Predefined", "named by Oracle", BLUE, BLUEF, ["NO_DATA_FOUND", "TOO_MANY_ROWS", "ZERO_DIVIDE", "DUP_VAL_ON_INDEX", "VALUE_ERROR", "INVALID_CURSOR"]),
            ("Non-predefined", "Oracle error, no name", ORANGE, ORANGEF, ["e EXCEPTION;", "PRAGMA", "EXCEPTION_INIT", "(e, -2292);", "", "gives a name"]),
            ("User-defined", "declared by you", GREEN, GREENF, ["e_low EXCEPTION;", "", "IF ... THEN", "  RAISE e_low;", "END IF;", ""])]
    for k, (h, d, s, f, items) in enumerate(kids):
        x = 8 + k * 116
        cx = x + 56
        b += line(f"M180 66 L180 78 L{cx} 78 L{cx} 90", GREY, 1.2)
        b += box(x, 90, 112, 40, f, s, 6, 1.5)
        b += text(cx, 105, h, 10, weight="bold", color=s) + text(cx, 121, d, 8.4, color=s)
        b += box(x, 138, 112, 96, "#fff", s, 5, 1.1)
        b += code(x + 6, 153, items, 8.2, 14)
    b += rbox(180, 52, 150, 28, "Exceptions", PF, P, 11, "bold", P)
    b += note(12, 246, 336, ["Error raised: control jumps to EXCEPTION section,",
                             "the matching WHEN handler runs, block ends normally.",
                             "No handler: error passes to the caller (propagation).",
                             "RAISE_APPLICATION_ERROR(-20000..-20999, 'msg')."], size=9.2)
    return svg(360, 328, b)


# ------------------------------------------------------------------ 5.5
def proc_func():
    b = title("Procedure vs Function")
    rows = [["Feature", "Procedure", "Function"],
            ["Purpose", "performs an action", "computes a value"],
            ["RETURN clause", "not in header", "RETURN datatype"],
            ["Returns", "0 or more via OUT", "exactly one value"],
            ["Called from", "EXEC / block", "expression / SELECT"],
            ["Used in SQL", "No", "Yes (if no DML)"],
            ["Keyword", "PROCEDURE", "FUNCTION"]]
    b += grid(8, 44, [100, 124, 120], rows, rh=24, size=8.8)
    b += text(14, 236, "Parameter modes", 10, anchor="start", weight="bold", color=P)
    modes = [("IN", "caller to procedure", "read only (default)", BLUE, BLUEF),
             ("OUT", "procedure to caller", "write a result", ORANGE, ORANGEF),
             ("IN OUT", "both directions", "read and write", GREEN, GREENF)]
    for k, (m, a, c, s, f) in enumerate(modes):
        x = 8 + k * 116
        b += box(x, 246, 112, 52, f, s, 6, 1.3)
        b += text(x + 56, 260, m, 10, weight="bold", color=s, mono=True)
        b += text(x + 56, 276, a, 8.6) + text(x + 56, 290, c, 8.6, color=GREY)
    return svg(360, 310, b)


# ------------------------------------------------------------------ 5.6
def trigger_flow():
    b = title("How a Trigger Fires")
    b += box(40, 120, 280, 116, "#fff", GREY, 6, 1.1).replace('/>', ' stroke-dasharray="4 3"/>')
    b += text(48, 132, "for each affected row", 8.6, anchor="start", color=GREY)
    for y1, y2 in ((69, 83), (109, 137), (163, 171), (197, 205), (231, 245)):
        b += down(180, y1, y2)
    b += rbox(180, 56, 300, 26, "UPDATE emp SET sal = ... WHERE ...;", BLUEF, BLUE, 9, mono=True)
    b += rbox(180, 96, 260, 26, "1. BEFORE statement trigger (once)", ORANGEF, ORANGE, 9.4)
    b += rbox(180, 150, 250, 26, "2. BEFORE row trigger (:NEW can change)", ORANGEF, ORANGE, 9.2)
    b += rbox(180, 184, 250, 26, "3. Row is changed in the table", GREENF, GREEN, 9.4)
    b += rbox(180, 218, 250, 26, "4. AFTER row trigger (e.g. audit)", TEALF, TEAL, 9.4)
    b += rbox(180, 258, 260, 26, "5. AFTER statement trigger (once)", TEALF, TEAL, 9.4)
    b += note(12, 282, 336, ["An error in any trigger (RAISE_APPLICATION_ERROR)",
                             "cancels the whole statement."], size=9.4)
    return svg(360, 334, b)


def trigger_types():
    b = title("Types of Triggers")
    rows = [["", "Row level", "Statement level"],
            ["Clause", "FOR EACH ROW", "(default)"],
            ["Fires", "once per row", "once per statement"],
            ["0 rows changed", "does not fire", "still fires once"],
            [":NEW / :OLD", "available", "not available"],
            ["Example", "audit each change", "log / time check"]]
    b += grid(8, 44, [96, 122, 126], rows, rh=22, size=8.8)
    b += text(14, 196, "Values available in row triggers", 9.8, anchor="start", weight="bold", color=P)
    rows2 = [["Event", ":OLD", ":NEW"], ["INSERT", "NULL", "new row"], ["UPDATE", "old values", "new values"], ["DELETE", "deleted row", "NULL"]]
    b += grid(8, 204, [96, 122, 126], rows2, head_fill=TEAL, rh=21, size=8.8)
    b += note(12, 298, 336, ["BEFORE: check or change data before it is saved.",
                             "AFTER: audit or copy data after it is saved.",
                             "2 timings x 2 levels x 3 events = 12 basic types."], size=9.4)
    return svg(360, 364, b)


DIAGRAMS = {"db5_block": block, "db5_engine": engine, "db5_type_rowtype": type_rowtype, "db5_if": if_flow, "db5_loops": loops,
            "db5_cursor": cursor, "db5_cursor_steps": cursor_steps, "db5_exceptions": exceptions, "db5_proc_func": proc_func,
            "db5_trigger_flow": trigger_flow, "db5_trigger_types": trigger_types}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
