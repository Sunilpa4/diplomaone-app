"""DI03000031 Unit 2 notes part A: 2.1 operators, 2.2 DUAL, numeric and character functions, 2.3 date, conversion and general functions."""
import html
from sql_content import make_TS, result

SN = {
    "s_arith": """
SELECT ename, sal * 12 AS annual
FROM emp
WHERE sal * 12 > 500000
AND (job = 'MANAGER' OR job = 'ANALYST');
""",
    "s_special": """
WHERE col IN (v1, v2, ...)
WHERE col BETWEEN low AND high
WHERE col LIKE 'pattern'
WHERE col IS NULL
WHERE col > ANY (sub-query)
WHERE col > ALL (sub-query)
WHERE EXISTS (sub-query)
""",
    "s_dual": """
SELECT 25 * 4 + 10 FROM dual;
""",
    "s_case": """
SELECT ename, sal,
  CASE
    WHEN sal >= 50000 THEN 'HIGH'
    WHEN sal >= 25000 THEN 'MEDIUM'
    ELSE 'LOW'
  END AS category
FROM emp
WHERE deptno = 30;
""",
}

T = make_TS(SN)
DUAL_OUT = html.escape(result(SN["s_dual"]), quote=False)
CASE_OUT = html.escape(result(SN["s_case"]), quote=False)


def ftable(rows):
    out = "<table><tr><th>Function</th><th>Purpose</th><th>Example → Result</th></tr>"
    for f, p, e in rows:
        out += f"<tr><td><code>{f}</code></td><td>{p}</td><td><code>{e}</code></td></tr>"
    return out + "</table>"


SEC_2_1 = {
    "title": {"en": "2.1 Operators"},
    "items": [
        T("Arithmetic, Comparison and Logical Operators", """
<p>An <b>operator</b> is a symbol or keyword that performs an operation on values (operands) in an SQL expression or condition.</p>
<h4>1. Arithmetic operators</h4>
<p><code>+</code> addition, <code>-</code> subtraction, <code>*</code> multiplication, <code>/</code> division. They are used in SELECT expressions and in conditions. Oracle has no <code>%</code> operator; use <code>MOD()</code>. Any arithmetic with NULL gives NULL.</p>
<h4>2. Comparison (relational) operators</h4>
<table><tr><th>Operator</th><th>Meaning</th></tr>
<tr><td><code>=</code></td><td>equal to</td></tr>
<tr><td><code>&lt;&gt;</code>, <code>!=</code>, <code>^=</code></td><td>not equal to</td></tr>
<tr><td><code>&gt;</code>, <code>&lt;</code></td><td>greater than, less than</td></tr>
<tr><td><code>&gt;=</code>, <code>&lt;=</code></td><td>greater/less than or equal to</td></tr></table>
<h4>3. Logical operators</h4>
<ul><li><b>AND</b>: true if <b>both</b> conditions are true.</li>
<li><b>OR</b>: true if <b>at least one</b> condition is true.</li>
<li><b>NOT</b>: reverses the result of a condition.</li></ul>
<h4>Operator precedence (highest first)</h4>
<ol><li>Brackets ( )</li><li>* /</li><li>+ - and || (concatenation)</li><li>Comparison operators, IN, LIKE, BETWEEN, IS NULL</li><li>NOT</li><li>AND</li><li>OR</li></ol>
<p>Because AND is evaluated before OR, use brackets when mixing them:</p>
@@s_arith@@
""", diagram="db2_operators", programs=["q2_1", "q2_2"]),
        T("Special Operators: IN, BETWEEN and IS NULL", """
@@s_special@@
<ul><li><b>IN (list)</b>: true if the value matches any value in the list. It replaces many OR conditions. <b>NOT IN</b> is the opposite (be careful: if the list contains NULL, NOT IN returns no rows).</li>
<li><b>BETWEEN low AND high</b>: true if the value is in the range, <b>including</b> both limits. NOT BETWEEN gives values outside the range. It works for numbers, dates and text.</li>
<li><b>IS NULL / IS NOT NULL</b>: test for missing values. <code>= NULL</code> never works because NULL is not equal to anything, not even another NULL.</li></ul>
""", programs=["q2_3", "q2_5"]),
        T("Special Operator: LIKE", """
<p><b>LIKE</b> compares a text value with a <b>pattern</b> containing wildcard characters:</p>
<ul><li><code>%</code> (percent) matches <b>zero or more</b> characters.</li>
<li><code>_</code> (underscore) matches <b>exactly one</b> character.</li></ul>
<p>Examples: <code>'S%'</code> starts with S; <code>'%AN'</code> ends with AN; <code>'%RA%'</code> contains RA; <code>'__J%'</code> 3rd letter J; <code>'_____'</code> exactly 5 characters.</p>
<ul><li>LIKE is case-sensitive in Oracle; use <code>UPPER(col) LIKE 'S%'</code> for a case-insensitive search.</li>
<li>To search for a real % or _, define an escape character: <code>WHERE code LIKE 'A\\_%' ESCAPE '\\'</code>.</li>
<li><b>NOT LIKE</b> returns rows that do not match the pattern.</li></ul>
""", diagram="db2_like", programs=["q2_4"]),
        T("Special Operators: ANY, ALL and EXISTS", """
<p>These operators are used with a <b>sub-query</b> (or a list) that returns several values.</p>
<ul><li><b>ANY (SOME)</b>: the condition is true if it holds for <b>at least one</b> value returned.</li>
<li><b>ALL</b>: the condition is true only if it holds for <b>every</b> value returned.</li>
<li><b>EXISTS</b>: true if the sub-query returns <b>at least one row</b>; NOT EXISTS is true if it returns no rows.</li></ul>
<table><tr><th>Condition</th><th>Equivalent</th></tr>
<tr><td><code>&gt; ANY (list)</code></td><td>greater than the minimum</td></tr>
<tr><td><code>&lt; ANY (list)</code></td><td>less than the maximum</td></tr>
<tr><td><code>= ANY (list)</code></td><td>same as IN</td></tr>
<tr><td><code>&gt; ALL (list)</code></td><td>greater than the maximum</td></tr>
<tr><td><code>&lt; ALL (list)</code></td><td>less than the minimum</td></tr>
<tr><td><code>&lt;&gt; ALL (list)</code></td><td>same as NOT IN</td></tr></table>
<p>EXISTS is usually used with a correlated sub-query and stops at the first matching row, so it is efficient.</p>
""", programs=["q2_6", "q2_7"]),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 DUAL Table, Numeric and Character Functions"},
    "items": [
        T("SQL Functions and the DUAL Table", f"""
<p>A <b>function</b> is a built-in program that takes arguments, performs an operation and returns a value. Functions are used in SELECT lists, WHERE, ORDER BY and other clauses.</p>
<h4>Types of functions</h4>
<ol><li><b>Single-row (scalar) functions</b>: work on each row separately and return <b>one result per row</b>.
<ul><li>Character, numeric, date, conversion and general (NVL, DECODE) functions.</li></ul></li>
<li><b>Multiple-row (group / aggregate) functions</b>: work on a group of rows and return <b>one result per group</b>: COUNT, SUM, AVG, MAX, MIN.</li></ol>
<h4>The DUAL table</h4>
<p><b>DUAL</b> is a dummy table automatically created by Oracle in the SYS schema and accessible to all users. It has <b>one column</b> (DUMMY, VARCHAR2(1)) and <b>one row</b> (value 'X').</p>
<p>Since SELECT always needs a FROM clause in Oracle, DUAL is used to evaluate expressions, test functions or get values like SYSDATE that do not come from a table. Because it has one row, the result is shown once.</p>
<pre class="c">SQL&gt; SELECT 25 * 4 + 10 FROM dual;

{DUAL_OUT}</pre>
""", diagram="db2_functions"),
        T("Numeric Functions", ftable([
            ("ABS(n)", "absolute (positive) value", "ABS(-25) → 25"),
            ("POWER(m, n)", "m raised to the power n", "POWER(2, 5) → 32"),
            ("MOD(m, n)", "remainder of m / n", "MOD(17, 5) → 2"),
            ("SQRT(n)", "square root (n ≥ 0)", "SQRT(144) → 12"),
            ("ROUND(n, d)", "rounds to d decimal places", "ROUND(156.786, 2) → 156.79"),
            ("ROUND(n, -d)", "rounds left of the decimal point", "ROUND(156.786, -1) → 160"),
            ("TRUNC(n, d)", "cuts to d decimals (no rounding)", "TRUNC(156.786, 2) → 156.78"),
            ("CEIL(n)", "smallest integer ≥ n", "CEIL(12.1) → 13"),
            ("FLOOR(n)", "largest integer ≤ n", "FLOOR(12.9) → 12"),
            ("SIGN(n)", "-1, 0 or 1", "SIGN(-8) → -1"),
        ]) + """
<ul><li>If d is omitted in ROUND/TRUNC, it is 0 (whole number).</li>
<li><b>ROUND vs TRUNC</b>: ROUND(15.67) = 16 but TRUNC(15.67) = 15.</li>
<li><b>CEIL vs FLOOR</b>: CEIL(-4.2) = -4 and FLOOR(-4.2) = -5.</li>
<li>MOD(m, 0) returns m.</li></ul>
""", programs=["q2_8", "q2_9"]),
        T("Character Functions", ftable([
            ("LOWER(s)", "all small letters", "LOWER('GTU') → gtu"),
            ("UPPER(s)", "all capital letters", "UPPER('gtu') → GTU"),
            ("INITCAP(s)", "first letter of each word capital", "INITCAP('surat city') → Surat City"),
            ("LENGTH(s)", "number of characters", "LENGTH('Gujarat') → 7"),
            ("CONCAT(a, b)", "joins two strings", "CONCAT('Diploma', 'One') → DiplomaOne"),
            ("LTRIM(s, set)", "removes chars from the left", "LTRIM('xxGTU', 'x') → GTU"),
            ("RTRIM(s, set)", "removes chars from the right", "RTRIM('GTUxx', 'x') → GTU"),
            ("TRIM(s)", "removes spaces from both ends", "TRIM('  GTU  ') → GTU"),
            ("REPLACE(s, a, b)", "replaces every a by b", "REPLACE('JACK', 'J', 'BL') → BLACK"),
            ("SUBSTR(s, m, n)", "n chars from position m", "SUBSTR('GUJARAT', 3, 3) → JAR"),
            ("INSTR(s, t, m, n)", "position of n-th t from m", "INSTR('GUJARAT', 'A', 1, 2) → 6"),
            ("LPAD(s, n, c)", "pads on the left to length n", "LPAD('77', 5, '*') → ***77"),
            ("RPAD(s, n, c)", "pads on the right to length n", "RPAD('77', 5, '*') → 77***"),
        ]) + """
<ul><li>LTRIM and RTRIM remove spaces when the second argument is omitted. They remove <b>any</b> character from the set, not the exact string: <code>LTRIM('abcabcX', 'abc')</code> → X.</li>
<li>SUBSTR positions start at 1; a negative start counts from the end. Without n it returns up to the end.</li>
<li>INSTR returns 0 when the text is not found. m and n are optional (default 1).</li>
<li>The <code>||</code> operator also concatenates and can join more than two strings: <code>ename || ' (' || job || ')'</code>.</li></ul>
""", diagram="db2_substr_instr", programs=["q2_10", "q2_11", "q2_12"]),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Date, Conversion and General Functions"},
    "items": [
        T("Date Functions", """
<p>Oracle stores a DATE as century, year, month, day, hour, minute and second. The default display format is <b>DD-MON-YY</b>. <b>SYSDATE</b> returns the current date and time of the database server.</p>
""" + ftable([
            ("SYSDATE", "current date and time", "SYSDATE → 28-OCT-26"),
            ("ADD_MONTHS(d, n)", "adds n months (n can be −)", "ADD_MONTHS('28-OCT-26', 3) → 28-JAN-27"),
            ("MONTHS_BETWEEN(d1, d2)", "months from d2 to d1", "MONTHS_BETWEEN('28-DEC-26', '28-OCT-26') → 2"),
            ("LAST_DAY(d)", "last date of the month", "LAST_DAY('28-OCT-26') → 31-OCT-26"),
            ("NEXT_DAY(d, 'day')", "next given weekday after d", "NEXT_DAY('28-OCT-26', 'MONDAY') → 02-NOV-26"),
            ("ROUND(d, 'MONTH')", "nearest 1st of month", "ROUND('28-OCT-26', 'MONTH') → 01-NOV-26"),
            ("TRUNC(d, 'MONTH')", "1st of the same month", "TRUNC('28-OCT-26', 'MONTH') → 01-OCT-26"),
            ("ROUND(d, 'YEAR')", "nearest 1st January", "ROUND('28-OCT-26', 'YEAR') → 01-JAN-27"),
            ("TRUNC(d, 'YEAR')", "1st January of the year", "TRUNC('28-OCT-26', 'YEAR') → 01-JAN-26"),
        ]) + """
<h4>Rules</h4>
<ul><li>ROUND with 'MONTH' rounds up from the 16th day; with 'YEAR' from 1st July. ROUND/TRUNC without a format work on the day (remove the time).</li>
<li>ADD_MONTHS on the last day of a month gives the last day of the result month.</li>
<li>MONTHS_BETWEEN can return a fraction; it is negative if d1 is earlier than d2.</li></ul>
<h4>Date arithmetic</h4>
<table><tr><th>Expression</th><th>Result</th></tr>
<tr><td>date + n</td><td>date n days later</td></tr>
<tr><td>date − n</td><td>date n days earlier</td></tr>
<tr><td>date − date</td><td>number of days between</td></tr>
<tr><td>date + n/24</td><td>adds n hours</td></tr></table>
<p>Two dates cannot be added.</p>
""", diagram="db2_date_funcs", programs=["q2_13", "q2_14"]),
        T("Conversion Functions: TO_CHAR, TO_DATE, TO_NUMBER", """
<p>Conversion functions change a value from one data type to another. Oracle also converts types automatically (<b>implicit conversion</b>), but <b>explicit conversion</b> with these functions is clearer and safer.</p>
<ul><li><b>TO_CHAR(date, 'fmt')</b>: date → text in the given format.</li>
<li><b>TO_CHAR(number, 'fmt')</b>: number → formatted text.</li>
<li><b>TO_DATE(text, 'fmt')</b>: text → DATE. The format describes how the text is written.</li>
<li><b>TO_NUMBER(text, 'fmt')</b>: text → NUMBER.</li></ul>
<h4>Date format elements</h4>
<table><tr><th>Element</th><th>Meaning</th><th>For 28-OCT-2026</th></tr>
<tr><td>DD</td><td>day of month</td><td>28</td></tr>
<tr><td>DY / DAY</td><td>short / full weekday</td><td>WED / WEDNESDAY</td></tr>
<tr><td>MM</td><td>month number</td><td>10</td></tr>
<tr><td>MON / MONTH</td><td>short / full month name</td><td>OCT / OCTOBER</td></tr>
<tr><td>YY / YYYY</td><td>2- / 4-digit year</td><td>26 / 2026</td></tr>
<tr><td>HH24:MI:SS</td><td>hours (0–23), minutes, seconds</td><td>10:30:15</td></tr>
<tr><td>Q</td><td>quarter</td><td>4</td></tr>
<tr><td>fm</td><td>removes padding spaces</td><td>October (not 'October  ')</td></tr></table>
<h4>Number format elements</h4>
<table><tr><th>Element</th><th>Meaning</th><th>Example</th></tr>
<tr><td>9</td><td>a digit</td><td>TO_CHAR(123, '9999') → ' 123'</td></tr>
<tr><td>0</td><td>leading zero</td><td>TO_CHAR(45, '0000') → ' 0045'</td></tr>
<tr><td>, .</td><td>thousands separator, decimal point</td><td>TO_CHAR(1234.5, '9,999.99') → ' 1,234.50'</td></tr>
<tr><td>$</td><td>dollar sign</td><td>TO_CHAR(500, '$999') → ' $500'</td></tr></table>
<p>If the number does not fit the format, Oracle shows ####.</p>
""", diagram="db2_conversion", programs=["q2_15", "q2_16"]),
        T("General Functions: NVL, NVL2, DECODE and CASE", f"""
<ul><li><b>NVL(expr1, expr2)</b>: returns expr2 if expr1 is NULL, otherwise expr1. Both must have the same type. <code>NVL(comm, 0)</code>.</li>
<li><b>NVL2(expr1, expr2, expr3)</b>: returns expr2 if expr1 is NOT NULL, otherwise expr3.</li>
<li><b>NULLIF(a, b)</b>: returns NULL if a = b, otherwise a.</li>
<li><b>DECODE(expr, search1, result1, search2, result2, ..., default)</b>: Oracle's IF-THEN-ELSE. It compares expr with each search value in order and returns the matching result; if nothing matches it returns the default (or NULL).</li>
<li><b>CASE</b>: the ANSI standard conditional expression; it can test ranges and any conditions, whereas DECODE only tests equality.</li></ul>
@@s_case@@
<pre class="c">{CASE_OUT}</pre>
<p>GREATEST(list) and LEAST(list) return the largest and smallest values of a list.</p>
""", programs=["q2_17"]),
    ],
}

NOTES_A = [SEC_2_1, SEC_2_2, SEC_2_3]
