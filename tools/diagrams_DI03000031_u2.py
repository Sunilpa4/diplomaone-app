"""DI03000031 RDBMS - Unit 2 diagrams: operators, functions, grouping, joins, sub-queries and set operators."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000031", "diagrams")


def card(x, y, w, h, ttl, ls, s, f, size=9.2, lh=13, mono=False):
    b = box(x, y, w, h, f, s, 8, 1.4) + text(x + w / 2, y + 15, ttl, 10.5, weight="bold", color=s)
    for i, t in enumerate(ls):
        b += text(x + w / 2, y + 33 + i * lh, t, size, mono=mono)
    return b


# ------------------------------------------------------------------ 2.1
def operators():
    b = title("SQL Operators")
    b += card(14, 34, 160, 96, "Arithmetic", ["+\u00a0\u00a0\u00a0-\u00a0\u00a0\u00a0*\u00a0\u00a0\u00a0/", "sal * 12", "sal + comm", "(no % ; use MOD)"], BLUE, BLUEF, mono=False)
    b += card(186, 34, 160, 96, "Comparison", ["=   <>  !=", ">   <   >=  <=", "sal >= 30000", "job <> 'CLERK'"], GREEN, GREENF)
    b += card(14, 140, 160, 96, "Logical", ["AND  OR  NOT", "TRUE only if both", "(AND) / any (OR)", "NOT reverses"], ORANGE, ORANGEF)
    b += card(186, 140, 160, 96, "Special", ["IN  BETWEEN  LIKE", "IS NULL  EXISTS", "ANY  ALL", "(+ NOT forms)"], P, PF)
    b += text(180, 256, "Precedence (high to low)", 10.5, weight="bold", color=P)
    pr = ["1. ( )   2. * /   3. + -   4. ||", "5. = <> < > <= >= IN LIKE BETWEEN", "   IS NULL   6. NOT   7. AND   8. OR"]
    b += box(14, 264, 332, 58, "#FBF8FF", P, 7, 1.1)
    for i, t in enumerate(pr):
        b += text(24, 280 + i * 16, t.replace(" ", "\u00a0"), 9.4, anchor="start", mono=True)
    return svg(360, 334, b)


def like():
    b = title("LIKE Wildcards: % and _")
    b += box(14, 34, 160, 46, BLUEF, BLUE, 7, 1.4) + text(94, 51, "%", 16, weight="bold", color=BLUE)
    b += text(94, 70, "zero or more characters", 9.2)
    b += box(186, 34, 160, 46, GREENF, GREEN, 7, 1.4) + text(266, 51, "_", 16, weight="bold", color=GREEN)
    b += text(266, 70, "exactly one character", 9.2)
    rows = [["Pattern", "Meaning", "Matches"], ["'P%'", "starts with P", "PRIYA, POOJA"], ["'%A'", "ends with A", "PRIYA, NEHA"],
            ["'%IT%'", "contains IT", "AMIT"], ["'_I%'", "2nd letter I", "KIRAN, VIJAY"], ["'____'", "exactly 4 chars", "AMIT, NEHA"],
            ["'%\\_%'", "has a real _", "ESCAPE '\\'"]]
    b += grid(14, 92, [80, 120, 132], rows, rh=22, size=9.2)
    b += note(12, 254, 336, ["LIKE is case-sensitive in Oracle: 'p%' does not", "match PRIYA. Use UPPER(ename) LIKE 'P%'.",
                             "NOT LIKE returns the rows that do not match."], size=9.4)
    return svg(360, 312, b)


# ------------------------------------------------------------------ 2.2
def functions():
    b = title("Types of SQL Functions")
    b += rbox(180, 46, 150, 28, "SQL functions", PF, P, 11.5, "bold", P)
    b += line("M180 60 L180 72 M90 72 L270 72 M90 72 L90 84 M270 72 L270 84", GREY, 1.3)
    b += box(14, 84, 152, 40, BLUEF, BLUE, 8, 1.5) + text(90, 99, "Single-row", 11, weight="bold", color=BLUE)
    b += text(90, 114, "one result per row", 8.8, color=BLUE)
    b += box(194, 84, 152, 40, GREENF, GREEN, 8, 1.5) + text(270, 99, "Multiple-row", 11, weight="bold", color=GREEN)
    b += text(270, 114, "one result per group", 8.8, color=GREEN)
    single = [("Character", "UPPER, SUBSTR, INSTR"), ("Numeric", "ROUND, MOD, POWER"), ("Date", "ADD_MONTHS, LAST_DAY"),
              ("Conversion", "TO_CHAR, TO_DATE"), ("General", "NVL, DECODE")]
    for i, (a, d) in enumerate(single):
        y = 134 + i * 38
        b += line(f"M22 124 L22 {y + 16} L30 {y + 16}", BLUE, 1.1)
        b += box(30, y, 136, 32, "#fff", BLUE, 6, 1.1)
        b += text(98, y + 11, a, 9.6, weight="bold", color=BLUE) + text(98, y + 24, d, 8.2, color=GREY)
    b += line("M202 124 L202 150 L210 150", GREEN, 1.1)
    b += box(210, 134, 136, 70, "#fff", GREEN, 6, 1.1) + text(278, 147, "Aggregate", 9.6, weight="bold", color=GREEN)
    b += lines(278, 162, ["COUNT, SUM, AVG,", "MAX, MIN", "used with GROUP BY"], 8.4, lh=12, color=GREY)
    b += note(194, 216, 152, ["Ignore NULL", "values (except", "COUNT(*))"], size=9, lh=13)
    return svg(360, 330, b)


def substr_instr():
    b = title("String Positions: SUBSTR and INSTR")
    s = "GUJARAT"
    x0, w = 54, 36
    for i, ch in enumerate(s):
        f = YEL if 2 <= i <= 4 else "#fff"
        b += box(x0 + i * w, 46, w, 30, f, P, 0, 1.4) + text(x0 + i * w + w / 2, 61, ch, 13, weight="bold", mono=True)
        b += text(x0 + i * w + w / 2, 88, str(i + 1), 9.2, color=BLUE)
        b += text(x0 + i * w + w / 2, 38, str(i - 7), 8.4, color=GREY)
    b += text(14, 88, "pos", 9, anchor="start", color=BLUE) + text(14, 38, "neg", 9, anchor="start", color=GREY)
    ex = [("SUBSTR('GUJARAT', 3, 3)", "JAR", "3 from 3rd"), ("SUBSTR('GUJARAT', 4)", "ARAT", "4th to end"),
          ("SUBSTR('GUJARAT', -3)", "RAT", "last 3 chars"), ("INSTR('GUJARAT', 'A')", "4", "first A"),
          ("INSTR('GUJARAT', 'A', 1, 2)", "6", "2nd A"), ("INSTR('GUJARAT', 'Z')", "0", "not found"),
          ("LENGTH('GUJARAT')", "7", "characters")]
    for i, (e, r, d) in enumerate(ex):
        y = 108 + i * 24
        b += text(14, y, e, 9.2, anchor="start", mono=True) + text(240, y, "→ " + r, 9.6, anchor="start", weight="bold", color=GREEN)
        b += text(346, y, d, 8.4, anchor="end", color=GREY)
    b += note(12, 280, 336, ["Positions start at 1 (not 0). A negative start", "counts from the right end."], size=9.4)
    return svg(360, 322, b)


# ------------------------------------------------------------------ 2.3
def date_funcs():
    b = title("Date Functions (SYSDATE = 28-OCT-26)")
    # mini calendars Oct and Nov 2026
    import calendar
    def cal(x, y, yr, mo, marks):
        out = text(x + 77, y, calendar.month_name[mo] + " " + str(yr), 10, weight="bold", color=P)
        for i, d in enumerate("MTWTFSS"):
            out += text(x + 11 + i * 22, y + 16, d, 8.4, color=GREY, weight="bold")
        first, n = calendar.monthrange(yr, mo)
        for d in range(1, n + 1):
            k = first + d - 1
            cx, cy = x + 11 + (k % 7) * 22, y + 32 + (k // 7) * 18
            if d in marks:
                c = marks[d]
                out += f'<circle cx="{cx}" cy="{cy}" r="9" fill="{c}"/>'
                out += text(cx, cy, str(d), 8.6, color="#fff", weight="bold")
            else:
                out += text(cx, cy, str(d), 8.6)
        return out
    b += cal(14, 40, 2026, 10, {28: BLUE, 31: RED})
    b += cal(192, 40, 2026, 11, {2: GREEN})
    lg = [(BLUE, "SYSDATE", "28-OCT-26 (Wed)"), (RED, "LAST_DAY(SYSDATE)", "31-OCT-26"),
          (GREEN, "NEXT_DAY(SYSDATE,'MONDAY')", "02-NOV-26"), (ORANGE, "ADD_MONTHS(SYSDATE, 3)", "28-JAN-27"),
          (ORANGE, "MONTHS_BETWEEN('28-DEC-26',", "2"), (ORANGE, "               SYSDATE)", ""),
          (TEAL, "SYSDATE + 7", "04-NOV-26"), (TEAL, "ROUND(SYSDATE,'MONTH')", "01-NOV-26"), (TEAL, "TRUNC(SYSDATE,'YEAR')", "01-JAN-26")]
    y = 178
    for i, (c, e, r) in enumerate(lg):
        yy = y + i * 18
        if r or i != 5:
            b += f'<circle cx="20" cy="{yy}" r="4" fill="{c}"/>'
        b += text(30, yy, e, 9, anchor="start", mono=True) + text(346, yy, r, 9.4, anchor="end", weight="bold", color=c)
    return svg(360, y + len(lg) * 18 + 4, b)


def conversion():
    b = title("Conversion Functions")
    pos = {"CHAR": (180, 64), "NUMBER": (60, 220), "DATE": (300, 220)}
    col = {"CHAR": P, "NUMBER": BLUE, "DATE": GREEN}
    fil = {"CHAR": PF, "NUMBER": BLUEF, "DATE": GREENF}

    def ar(x1, y1, x2, y2, lab, lx, ly, c, anchor="middle"):
        import math
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        return (line(f"M{x1} {y1} L{x2} {y2}", c, 1.6) + arrowhead(x2, y2, ang, 8, c) +
                text(lx, ly, lab, 9.4, weight="bold", color=c, anchor=anchor, mono=True))
    b += ar(150, 82, 74, 196, "TO_NUMBER", 92, 128, BLUE, "end")
    b += ar(92, 200, 166, 86, "TO_CHAR", 126, 196, P, "start")
    b += ar(212, 82, 290, 196, "TO_DATE", 270, 128, GREEN, "start")
    b += ar(270, 200, 194, 86, "TO_CHAR", 234, 196, P, "end")
    for k, (x, y) in pos.items():
        b += box(x - 50, y - 18, 100, 36, fil[k], col[k], 18, 1.8) + text(x, y, k, 12, weight="bold", color=col[k])
    b += note(12, 250, 336, ["TO_CHAR(SYSDATE, 'DD/MM/YYYY') → '28/10/2026'", "TO_CHAR(1234.5, '9,999.99') → ' 1,234.50'",
                             "TO_DATE('15-08-2026', 'DD-MM-YYYY') → date", "TO_NUMBER('5000') + 1 → 5001",
                             "Implicit conversion happens automatically, but", "explicit conversion is safer."], size=9.2, mono=False)
    return svg(360, 350, b)


# ------------------------------------------------------------------ 2.4
def groupby():
    b = title("GROUP BY and HAVING")
    rows = [("10", "90000"), ("10", "40000"), ("20", "60000"), ("20", "45000"), ("20", "22000"), ("30", "58000"), ("30", "30000"),
            ("30", "28000"), ("30", "20000")]
    cols = {"10": BLUEF, "20": GREENF, "30": ORANGEF}
    b += text(64, 40, "EMP rows", 10, weight="bold", color=P)
    b += box(14, 48, 50, 18, P, P, 0, 1) + text(39, 57, "DEPT", 8.6, color="#fff", weight="bold")
    b += box(64, 48, 52, 18, P, P, 0, 1) + text(90, 57, "SAL", 8.6, color="#fff", weight="bold")
    for i, (d, s) in enumerate(rows):
        y = 66 + i * 18
        b += box(14, y, 50, 18, cols[d], "#C9B3EC", 0, 1) + text(39, y + 9, d, 8.8)
        b += box(64, y, 52, 18, cols[d], "#C9B3EC", 0, 1) + text(90, y + 9, s, 8.8)
    b += text(186, 40, "GROUP BY deptno", 9.4, weight="bold", color=P, mono=True)
    out = [("10", "2", "130000", BLUEF), ("20", "3", "127000", GREENF), ("30", "4", "136000", ORANGEF)]
    for i, (d, c, s, f) in enumerate(out):
        y = 70 + i * 50
        b += line(f"M118 {66 + [0, 2, 5][i] * 18 + [2, 3, 4][i] * 9} L150 {y + 16}", GREY, 1.2) + arrowhead(154, y + 16, 0, 6, GREY)
        b += box(156, y, 180, 32, f, "#999", 6, 1.1)
        b += text(246, y + 16, f"dept {d}: COUNT {c}, SUM {s}", 9.2)
    b += text(246, 232, "HAVING COUNT(*) > 2", 9.4, weight="bold", color=RED, mono=True)
    b += text(246, 248, "keeps only groups 20 and 30", 9, color=RED)
    b += note(12, 238 + 30, 336, ["WHERE filters ROWS before grouping.", "HAVING filters GROUPS after grouping (can use",
                                  " aggregate functions).", "Every SELECT column that is not inside an aggregate",
                                  " must appear in GROUP BY."], size=9.4)
    return svg(360, 352, b)


def query_order():
    b = title("Order of Execution of a SELECT")
    steps = [("FROM / JOIN", "pick tables, join rows", BLUE, BLUEF), ("WHERE", "filter rows", BLUE, BLUEF),
             ("GROUP BY", "form groups", GREEN, GREENF), ("HAVING", "filter groups", GREEN, GREENF),
             ("SELECT", "compute columns, aliases", ORANGE, ORANGEF), ("DISTINCT", "remove duplicates", ORANGE, ORANGEF),
             ("ORDER BY", "sort result (can use alias)", P, PF)]
    for i, (a, d, s, f) in enumerate(steps):
        y = 36 + i * 38
        b += box(40, y, 280, 30, f, s, 7, 1.4)
        b += f'<circle cx="58" cy="{y + 15}" r="10" fill="{s}"/>' + text(58, y + 15, str(i + 1), 10, color="#fff", weight="bold")
        b += text(76, y + 15, a, 10.5, anchor="start", weight="bold", color=s, mono=True) + text(310, y + 15, d, 9, anchor="end")
        if i < len(steps) - 1:
            b += down(180, y + 30, y + 38)
    b += note(12, 306, 336, ["A column alias can be used in ORDER BY but not", "in WHERE (WHERE runs before SELECT)."], size=9.4)
    return svg(360, 348, b)


# ------------------------------------------------------------------ 2.5
def venn(cx, cy, fillL, fillM, fillR, lab, sub, c):
    r = 26
    xl, xr = cx - 14, cx + 14
    cid = f"c{int(cx)}{int(cy)}"
    out = f'<clipPath id="{cid}"><circle cx="{xr}" cy="{cy}" r="{r}"/></clipPath>'
    out += f'<circle cx="{xl}" cy="{cy}" r="{r}" fill="{fillL}"/><circle cx="{xr}" cy="{cy}" r="{r}" fill="{fillR}"/>'
    out += f'<circle cx="{xl}" cy="{cy}" r="{r}" fill="{fillM}" clip-path="url(#{cid})"/>'
    out += f'<circle cx="{xl}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
    out += f'<circle cx="{xr}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
    out += text(xl - 12, cy, "A", 9, weight="bold") + text(xr + 12, cy, "B", 9, weight="bold")
    out += text(cx, cy + 40, lab, 9.8, weight="bold", color=c) + text(cx, cy + 53, sub, 8.4, color=GREY)
    return out


def joins():
    b = title("Types of Joins (A = EMP, B = DEPT)")
    S, W = "#9C6ADE", "#fff"
    b += venn(94, 76, W, S, W, "INNER JOIN", "matching rows only", P)
    b += venn(266, 76, S, S, W, "LEFT OUTER JOIN", "all A + matching B", P)
    b += venn(94, 180, W, S, S, "RIGHT OUTER JOIN", "matching A + all B", P)
    b += venn(266, 180, S, S, S, "FULL OUTER JOIN", "all rows of A and B", P)
    rows = [["Join", "Rows (our EMP/DEPT)"], ["INNER", "9 (MEHUL has no dept)"], ["LEFT", "10 (MEHUL, dname NULL)"],
            ["RIGHT", "10 (dept 40, ename NULL)"], ["FULL", "11"], ["CROSS", "10 x 4 = 40"]]
    b += grid(30, 254, [70, 230], rows, rh=20, size=9.2)
    return svg(360, 382, b)


def self_join():
    b = title("Self Join: Employee and Manager")
    rows = [["EMPNO", "ENAME", "MGR"], ["101", "RAJESH", ""], ["102", "AMIT", "101"], ["104", "NEHA", "102"], ["105", "KIRAN", "102"]]
    b += text(84, 40, "EMP  w (worker)", 9.6, weight="bold", color=BLUE)
    b += grid(14, 48, [44, 56, 40], rows, head_fill=BLUE, rh=20, size=9)
    b += text(276, 40, "EMP  m (manager)", 9.6, weight="bold", color=GREEN)
    b += grid(206, 48, [44, 56, 40], rows, head_fill=GREEN, rh=20, size=9)
    # w.mgr -> m.empno for NEHA (row 3) -> AMIT (row 2)
    b += line("M154 118 C 180 118, 180 98, 204 98", RED, 1.6) + arrowhead(206, 98, 0, 7, RED)
    b += line("M154 138 C 180 138, 186 102, 204 100", RED, 1.2, "3 2")
    b += text(180, 162, "w.mgr = m.empno", 10, weight="bold", color=RED, mono=True)
    b += text(180, 182, "Result", 10, weight="bold", color=P)
    b += grid(110, 190, [70, 70], [["WORKER", "MANAGER"], ["AMIT", "RAJESH"], ["NEHA", "AMIT"], ["KIRAN", "AMIT"]], rh=20, size=9)
    b += note(12, 278, 336, ["A table is joined with ITSELF using two aliases.", "RAJESH has no manager: use LEFT JOIN to keep him."], size=9.4)
    return svg(360, 320, b)


def cross_join():
    b = title("Cross Join (Cartesian Product)")
    b += grid(20, 46, [70], [["COLOR"], ["Red"], ["Blue"]], head_fill=BLUE, rh=22, size=9.4)
    b += text(110, 80, "×", 18, weight="bold")
    b += grid(130, 46, [60], [["SIZE"], ["S"], ["M"], ["L"]], head_fill=GREEN, rh=22, size=9.4)
    b += text(204, 80, "=", 18, weight="bold")
    rr = [["COLOR", "SIZE"], ["Red", "S"], ["Red", "M"], ["Red", "L"], ["Blue", "S"], ["Blue", "M"], ["Blue", "L"]]
    b += grid(222, 46, [64, 54], rr, rh=22, size=9.4)
    b += note(12, 212, 336, ["Every row of table 1 is paired with every row of", "table 2: rows = m × n (2 × 3 = 6).",
                             "Written as CROSS JOIN, or FROM a, b with no", "join condition (often a mistake!)."], size=9.4)
    return svg(360, 282, b)


# ------------------------------------------------------------------ 2.6
def subquery():
    b = title("Sub-query and Correlated Sub-query")
    b += text(90, 42, "Nested (simple)", 10.5, weight="bold", color=BLUE)
    b += box(14, 52, 156, 40, BLUEF, BLUE, 7, 1.3) + lines(92, 66, ["Inner query runs", "ONCE first"], 9.2, lh=13)
    b += down(92, 92, 112) + text(98, 104, "result", 8.6, anchor="start", color=GREY)
    b += box(14, 112, 156, 40, "#fff", BLUE, 7, 1.3) + lines(92, 126, ["Outer query uses", "the result"], 9.2, lh=13)
    b += text(270, 42, "Correlated", 10.5, weight="bold", color=ORANGE)
    b += box(186, 52, 150, 40, ORANGEF, ORANGE, 7, 1.3) + lines(261, 66, ["Outer query takes", "a row"], 9.2, lh=13)
    b += down(261, 92, 112)
    b += box(186, 112, 150, 40, "#fff", ORANGE, 7, 1.3) + lines(261, 126, ["Inner query runs for", "THAT row"], 9.2, lh=13)
    b += line("M336 132 C 352 132, 352 72, 340 72", ORANGE, 1.4) + arrowhead(338, 72, 180, 7, ORANGE)
    b += text(261, 166, "repeats for every outer row", 8.6, color=ORANGE)
    b += box(14, 180, 332, 60, "#FBF8FF", P, 7, 1.1)
    for i, t in enumerate(["SELECT ename FROM emp", "WHERE sal > (SELECT AVG(sal)", "             FROM emp);"]):
        b += text(24, 196 + i * 15, t.replace(" ", "\u00a0"), 9.4, anchor="start", mono=True)
    b += box(14, 248, 332, 60, "#FFF8EE", ORANGE, 7, 1.1)
    for i, t in enumerate(["SELECT ename FROM emp e", "WHERE sal > (SELECT AVG(sal) FROM emp", "     WHERE deptno = e.deptno);"]):
        b += text(24, 264 + i * 15, t.replace(" ", "\u00a0"), 9.4, anchor="start", mono=True)
    b += note(12, 318, 336, ["Single-row sub-query: use =, >, <  ...", "Multiple-row sub-query: use IN, ANY, ALL, EXISTS"], size=9.4)
    return svg(360, 360, b)


def set_ops():
    b = title("Set Operators")
    S, W = "#9C6ADE", "#fff"
    b += venn(94, 76, S, S, S, "UNION", "A + B, no duplicates", P)
    b += venn(266, 76, S, "#5E2BA8", S, "UNION ALL", "A + B, keeps duplicates", P)
    b += venn(94, 180, W, S, W, "INTERSECT", "common to A and B", P)
    b += venn(266, 180, S, W, W, "MINUS", "in A but not in B", P)
    b += note(12, 252, 336, ["Rules: both queries must have the same number", "of columns with compatible data types.",
                             "Column names come from the first query.", "ORDER BY only once, at the very end.",
                             "UNION, INTERSECT, MINUS sort and remove duplicates."], size=9.4)
    return svg(360, 340, b)


DIAGRAMS = {"db2_operators": operators, "db2_like": like, "db2_functions": functions, "db2_substr_instr": substr_instr,
            "db2_date_funcs": date_funcs, "db2_conversion": conversion, "db2_groupby": groupby, "db2_query_order": query_order,
            "db2_joins": joins, "db2_self_join": self_join, "db2_cross_join": cross_join, "db2_subquery": subquery, "db2_set_ops": set_ops}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
