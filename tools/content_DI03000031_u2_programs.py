"""DI03000031 RDBMS Unit 2 – query programs (Oracle SQL) with real output from sql_runner. Tables: EMP, DEPT, SALGRADE (sql_seed)."""
from sql_content import QE

P = []
DS = ("SYSDATE - hiredate", "__DSUB(SYSDATE, hiredate)")

# ------------------------------------------------------------------ sample tables
P.append(QE("q2_1", "Sample tables used in this unit: DEPT, EMP and SALGRADE", """
SELECT * FROM dept;

SELECT * FROM emp;

SELECT * FROM salgrade;
""", """
<p>All Unit 2 queries use these three tables (the classic Oracle SCOTT schema with Indian names).</p>
<ul><li><b>DEPT</b>: 4 departments. Department 40 (OPERATIONS) has <b>no employees</b>, which is useful for outer joins.</li>
<li><b>EMP</b>: 10 employees. <code>mgr</code> holds the empno of the employee's manager (used in the self join). Only salesmen have a <code>comm</code> (commission); others have NULL. MEHUL (110) is a trainee with <b>no department</b> (deptno NULL).</li>
<li><b>SALGRADE</b>: salary ranges for grades 1–5 (used in the non-equi join).</li></ul>
<p>SYSDATE is taken as <b>28-OCT-26</b> in all outputs.</p>
"""))

# ------------------------------------------------------------------ 2.1 operators
P.append(QE("q2_2", "Arithmetic operators and operator precedence", """
SELECT ename, sal,
       sal * 12 annual,
       sal + 1000 * 2 a,
       (sal + 1000) * 2 b,
       sal + comm total
FROM emp
WHERE deptno = 30;
""", """
<ul><li>Arithmetic operators: <code>+  -  *  /</code>. They work on NUMBER (and DATE) values.</li>
<li><b>Precedence:</b> * and / are done before + and -. So <code>sal + 1000 * 2</code> = sal + 2000, while <code>(sal + 1000) * 2</code> adds first. Brackets change the order.</li>
<li><b>Any arithmetic with NULL gives NULL.</b> PRIYA and VIJAY have no commission, so their <code>total</code> is blank. Use <code>NVL(comm, 0)</code> to fix this (see the NVL program).</li></ul>
"""))

P.append(QE("q2_3", "Special operators IN and BETWEEN", """
SELECT ename, job FROM emp
WHERE job IN ('CLERK', 'ANALYST');

SELECT ename, deptno FROM emp
WHERE deptno NOT IN (10, 20);

SELECT ename, sal FROM emp
WHERE sal BETWEEN 30000 AND 50000;
""", """
<ul><li><b>IN (list)</b> is true if the value equals <b>any</b> value in the list. It is a short form of <code>job = 'CLERK' OR job = 'ANALYST'</code>.</li>
<li><b>NOT IN</b> is the opposite. MEHUL (deptno NULL) is <b>not</b> returned: a comparison with NULL is never true.</li>
<li><b>BETWEEN a AND b</b> includes both limits: <code>sal &gt;= 30000 AND sal &lt;= 50000</code>. The smaller value must come first. It also works with dates and text.</li></ul>
"""))

P.append(QE("q2_4", "Pattern matching with LIKE", """
SELECT ename FROM emp
WHERE ename LIKE 'P%';

SELECT ename FROM emp
WHERE ename LIKE '%A';

SELECT ename FROM emp
WHERE ename LIKE '_I%';

SELECT ename FROM emp
WHERE ename LIKE '____';

SELECT ename FROM emp
WHERE ename NOT LIKE '%A%';
""", """
<ul><li><code>%</code> = any number of characters (even zero); <code>_</code> = exactly one character.</li>
<li><code>'P%'</code>: starts with P. <code>'%A'</code>: ends with A. <code>'_I%'</code>: second letter is I.</li>
<li><code>'____'</code> (4 underscores): names with exactly 4 letters.</li>
<li><code>NOT LIKE '%A%'</code>: names that contain no A at all.</li>
<li>LIKE is <b>case-sensitive</b>. To search for a real % or _, use ESCAPE: <code>LIKE '%\\_%' ESCAPE '\\'</code>.</li></ul>
"""))

P.append(QE("q2_5", "IS NULL and IS NOT NULL", """
SELECT ename, comm FROM emp
WHERE comm IS NOT NULL;

SELECT ename, job FROM emp
WHERE mgr IS NULL;

SELECT ename FROM emp
WHERE comm = NULL;
""", """
<ul><li>NULL means unknown, so it cannot be compared with <code>=</code>. Use <b>IS NULL</b> / <b>IS NOT NULL</b>.</li>
<li>RAJESH is the president and has no manager, so <code>mgr IS NULL</code> finds him.</li>
<li><code>comm = NULL</code> is never true (the result is "unknown"), so it returns <b>no rows</b> even though 8 employees have no commission. This is a common mistake.</li></ul>
"""))

P.append(QE("q2_6", "ANY and ALL with a sub-query", """
SELECT ename, sal FROM emp
WHERE sal > ALL (SELECT sal FROM emp
                 WHERE deptno = 30);

SELECT ename, sal FROM emp
WHERE sal < ANY (SELECT sal FROM emp
                 WHERE job = 'CLERK');
""", """
<ul><li><b>&gt; ALL</b>: greater than <b>every</b> value in the list, i.e. greater than the maximum. The highest salary in dept 30 is 58000, so only 90000 and 60000 qualify.</li>
<li><b>&lt; ANY</b>: less than <b>at least one</b> value, i.e. less than the maximum. The clerks earn 22000 and 20000, so salaries below 22000 qualify.</li>
<li>Summary: <code>&gt; ANY</code> = more than the minimum; <code>&lt; ALL</code> = less than the minimum; <code>= ANY</code> is the same as IN.</li></ul>
"""))

P.append(QE("q2_7", "EXISTS and NOT EXISTS", """
SELECT d.deptno, d.dname
FROM dept d
WHERE EXISTS (SELECT 1 FROM emp e
              WHERE e.deptno = d.deptno);

SELECT d.deptno, d.dname
FROM dept d
WHERE NOT EXISTS
      (SELECT 1 FROM emp e
       WHERE e.deptno = d.deptno);
""", """
<ul><li><b>EXISTS</b> is true if the sub-query returns <b>at least one row</b>. The values returned do not matter, so <code>SELECT 1</code> is common.</li>
<li>For each department, the inner query checks whether some employee works there (a correlated sub-query).</li>
<li><b>NOT EXISTS</b> finds departments with no employees: OPERATIONS (40).</li>
<li>EXISTS stops searching at the first match, so it is often faster than IN for large tables.</li></ul>
"""))

# ------------------------------------------------------------------ 2.2 dual, numeric, character
P.append(QE("q2_8", "DUAL table and numeric functions", """
SELECT ABS(-25) a, POWER(2, 5) p,
       MOD(17, 5) m, SQRT(144) s
FROM dual;

SELECT ROUND(156.786, 2) r1,
       ROUND(156.786) r2,
       ROUND(156.786, -1) r3,
       TRUNC(156.786, 2) t1,
       TRUNC(156.786) t2
FROM dual;

SELECT CEIL(12.1) c, FLOOR(12.9) f,
       ROUND(-2.5) r, TRUNC(-2.7) t
FROM dual;
""", """
<p><b>DUAL</b> is a special one-row, one-column table owned by SYS. It is used to calculate expressions or call functions that do not need any table.</p>
<ul><li><code>ABS(n)</code>: absolute value. <code>POWER(m, n)</code>: m<sup>n</sup>. <code>MOD(m, n)</code>: remainder of m ÷ n. <code>SQRT(n)</code>: square root.</li>
<li><code>ROUND(n, d)</code>: rounds to d decimal places (5 and above goes up). A negative d rounds to the left of the decimal point: <code>ROUND(156.786, -1)</code> = 160.</li>
<li><code>TRUNC(n, d)</code>: cuts off the digits without rounding: 156.78.</li>
<li><code>CEIL(n)</code>: smallest integer ≥ n. <code>FLOOR(n)</code>: largest integer ≤ n.</li>
<li>For negatives: ROUND(-2.5) = -3, while TRUNC(-2.7) = -2 (it just drops the decimals).</li></ul>
"""))

P.append(QE("q2_9", "Numeric functions on table data", """
SELECT ename, sal,
       ROUND(sal / 12, 2) monthly,
       MOD(sal, 7) m7,
       TRUNC(sal * 0.0833) bonus
FROM emp
WHERE deptno = 20;
""", """
<ul><li>Functions are applied to every row of the result.</li>
<li><code>ROUND(sal / 12, 2)</code> shows the monthly pay to 2 decimals. Oracle drops trailing zeros (5000, not 5000.00); use TO_CHAR to format.</li>
<li><code>MOD(sal, 7)</code> gives the remainder when the salary is divided by 7.</li>
<li><code>TRUNC(sal * 0.0833)</code>: bonus with the paise removed.</li></ul>
"""))

P.append(QE("q2_10", "Character functions: case and length", """
SELECT UPPER('gtu exam') u,
       LOWER('DIPLOMA') l,
       INITCAP('surat city') i,
       LENGTH('Gujarat') len
FROM dual;

SELECT ename, INITCAP(ename) name,
       LOWER(job) job,
       LENGTH(ename) len,
       CONCAT(ename, deptno) c,
       ename || '-' || job j
FROM emp
WHERE deptno = 10;
""", """
<ul><li><code>UPPER</code> / <code>LOWER</code>: convert to capitals / small letters.</li>
<li><code>INITCAP</code>: first letter of each word in capitals, the rest small.</li>
<li><code>LENGTH</code>: number of characters.</li>
<li><code>CONCAT(a, b)</code>: joins exactly <b>two</b> strings (numbers are converted automatically). The <code>||</code> operator can join any number of strings.</li>
<li>Searching without worrying about case: <code>WHERE UPPER(ename) = 'AMIT'</code>.</li></ul>
"""))

P.append(QE("q2_11", "Character functions: LTRIM, RTRIM, REPLACE, LPAD, RPAD", """
SELECT LTRIM('   GTU') a,
       RTRIM('xxGTUxx', 'x') b,
       LTRIM('000123', '0') c,
       REPLACE('JACK AND JUE', 'J', 'BL') d
FROM dual;

SELECT LPAD(ename, 8, '*') lp,
       RPAD(ename, 8, '.') rp,
       LPAD(sal, 7, '0') sal
FROM emp
WHERE deptno = 10;
""", """
<ul><li><code>LTRIM(s, set)</code> / <code>RTRIM(s, set)</code>: remove the given characters (default: spaces) from the left / right end. <code>TRIM(s)</code> removes spaces from both ends.</li>
<li><code>LTRIM('000123', '0')</code> removes leading zeros.</li>
<li><code>REPLACE(s, find, new)</code>: replaces every occurrence. Without the third argument the text is removed.</li>
<li><code>LPAD(s, n, c)</code> / <code>RPAD(s, n, c)</code>: pad on the left / right with character c up to total length n. LPAD is used to right-align numbers or add leading zeros.</li></ul>
"""))

P.append(QE("q2_12", "Character functions: SUBSTR and INSTR", """
SELECT SUBSTR('GUJARAT', 3, 3) a,
       SUBSTR('GUJARAT', 4) b,
       SUBSTR('GUJARAT', -3) c,
       INSTR('GUJARAT', 'A') d,
       INSTR('GUJARAT', 'A', 1, 2) e,
       INSTR('GUJARAT', 'Z') f
FROM dual;

SELECT ename, SUBSTR(ename, 1, 3) code,
       INSTR(ename, 'A') pos_a
FROM emp
WHERE deptno = 30;
""", """
<ul><li><code>SUBSTR(s, start, len)</code>: extracts <code>len</code> characters from position <code>start</code> (the first character is 1). Without <code>len</code> it goes to the end. A negative start counts from the right.</li>
<li><code>INSTR(s, find, start, n)</code>: the position of the <b>n-th</b> occurrence of <code>find</code>, searching from <code>start</code>. It returns <b>0</b> if not found.</li>
<li>SUBSTR(ename, 1, 3) makes a 3-letter code; INSTR gives 0 for SUNIL because it has no A.</li></ul>
"""))

# ------------------------------------------------------------------ 2.3 date + conversion
P.append(QE("q2_13", "Date functions: SYSDATE, ADD_MONTHS, MONTHS_BETWEEN, NEXT_DAY, LAST_DAY", """
SELECT SYSDATE today,
       ADD_MONTHS(SYSDATE, 3) plus3,
       ADD_MONTHS(SYSDATE, -1) minus1,
       LAST_DAY(SYSDATE) last,
       NEXT_DAY(SYSDATE, 'MONDAY') nxt
FROM dual;

SELECT ename, hiredate,
       ROUND(MONTHS_BETWEEN(SYSDATE,
             hiredate)) months,
       ADD_MONTHS(hiredate, 6) probation
FROM emp
WHERE deptno = 10;
""", """
<ul><li><code>SYSDATE</code>: the current date and time of the server.</li>
<li><code>ADD_MONTHS(d, n)</code>: adds n months (n may be negative). If d is the last day of a month, the result is the last day of the new month (31-JAN + 1 → 28/29-FEB).</li>
<li><code>MONTHS_BETWEEN(d1, d2)</code>: the number of months from d2 to d1 (it can be fractional); positive if d1 is later.</li>
<li><code>LAST_DAY(d)</code>: the last date of d's month.</li>
<li><code>NEXT_DAY(d, 'DAY')</code>: the date of the next given weekday after d. 28-OCT-26 is a Wednesday, so the next Monday is 02-NOV-26.</li></ul>
"""))

P.append(QE("q2_14", "ROUND and TRUNC on dates, and date arithmetic", """
SELECT ROUND(SYSDATE, 'MONTH') rm,
       TRUNC(SYSDATE, 'MONTH') tm,
       ROUND(SYSDATE, 'YEAR') ry,
       TRUNC(SYSDATE, 'YEAR') ty
FROM dual;

SELECT ename,
       TRUNC(SYSDATE - hiredate) days,
       TRUNC((SYSDATE - hiredate) / 7)
         weeks,
       hiredate + 90 review
FROM emp
WHERE deptno = 10;
""", """
<ul><li><code>ROUND(d, 'MONTH')</code>: to the 1st of the nearest month (day 16 or later rounds up). 28-OCT → 01-NOV.</li>
<li><code>TRUNC(d, 'MONTH')</code>: to the 1st of the same month. <code>'YEAR'</code> works the same way (July or later rounds up to the next year).</li>
<li><b>Date arithmetic:</b> date − date = number of <b>days</b> (with a fraction for the time); date + n = the date n days later.</li>
<li>TRUNC removes the fractional day, so we get complete days and weeks.</li></ul>
""", rewrite=[("SYSDATE - hiredate", "__DSUB(SYSDATE, hiredate)"), ("hiredate + 90", "__DADD(hiredate, 90)")]))

P.append(QE("q2_15", "TO_CHAR: format dates and numbers", """
SELECT TO_CHAR(SYSDATE, 'DD/MM/YYYY') a,
       TO_CHAR(SYSDATE, 'DD-MON-YYYY') b,
       TO_CHAR(SYSDATE, 'fmDay, DD Month')
         c,
       TO_CHAR(SYSDATE, 'HH24:MI:SS') t
FROM dual;

SELECT ename,
       TO_CHAR(hiredate, 'YYYY') yr,
       TO_CHAR(hiredate, 'Mon') mon,
       TO_CHAR(sal, '99,999.99') salary
FROM emp
WHERE deptno = 20;
""", """
<p><code>TO_CHAR(date, 'format')</code> converts a date to text in any format.</p>
<ul><li>Elements: <code>DD</code> day, <code>MM</code> month number, <code>MON</code> JAN, <code>MONTH</code> JANUARY, <code>YY/YYYY</code> year, <code>DAY</code> weekday, <code>DY</code> WED, <code>HH24:MI:SS</code> time, <code>Q</code> quarter.</li>
<li>The case of the format controls the output: <code>Mon</code> → Mar, <code>MON</code> → MAR.</li>
<li><code>fm</code> (fill mode) removes extra spaces from Day and Month names.</li>
<li><code>TO_CHAR(number, '99,999.99')</code>: 9 = a digit, comma = thousands separator, period = decimal point. One extra leading space is kept for the sign.</li></ul>
"""))

P.append(QE("q2_16", "TO_DATE and TO_NUMBER", """
SELECT TO_DATE('15-08-2026',
               'DD-MM-YYYY') d1,
       TO_DATE('January 26, 2027',
               'Month DD, YYYY') d2
FROM dual;

SELECT TO_NUMBER('5,000', '9,999') + 1 n,
       TO_NUMBER('12.75') * 2 m
FROM dual;

SELECT ename, hiredate FROM emp
WHERE hiredate > TO_DATE('01-01-2021',
                         'DD-MM-YYYY');
""", """
<ul><li><code>TO_DATE(text, 'format')</code> converts text to a DATE. The format must describe the text exactly; the result is shown in the default DD-MON-YY format.</li>
<li><code>TO_NUMBER(text, 'format')</code> converts text (which may contain commas) to a number so arithmetic can be done.</li>
<li>Always compare dates using TO_DATE, never with a plain string, because the default date format can differ between systems.</li></ul>
"""))

P.append(QE("q2_17", "NVL, NVL2 and DECODE", """
SELECT ename, comm,
       NVL(comm, 0) c,
       sal + NVL(comm, 0) total,
       NVL2(comm, 'YES', 'NO') has_comm
FROM emp
WHERE deptno = 30;

SELECT ename, deptno,
       DECODE(deptno, 10, 'ACCOUNTS',
                      20, 'RESEARCH',
                      30, 'SALES',
                      'NO DEPT') dept
FROM emp
WHERE empno IN (101, 102, 103, 110);
""", """
<ul><li><code>NVL(expr, value)</code>: if expr is NULL, return value; otherwise return expr. Used to treat a missing commission as 0.</li>
<li><code>NVL2(expr, a, b)</code>: returns a if expr is <b>not</b> NULL, otherwise b.</li>
<li><code>DECODE(expr, s1, r1, s2, r2, ..., default)</code>: works like an IF-THEN-ELSE / switch-case. It compares expr with each search value and returns the matching result, or the default. MEHUL has no department, so he gets 'NO DEPT'.</li>
<li>The standard SQL equivalent of DECODE is the <code>CASE</code> expression.</li></ul>
"""))

# ------------------------------------------------------------------ 2.4 aggregate, group by
P.append(QE("q2_18", "Aggregate functions", """
SELECT COUNT(*) emps, COUNT(comm) c,
       SUM(sal) total, MAX(sal) max,
       MIN(sal) min, AVG(sal) avg
FROM emp;

SELECT COUNT(DISTINCT job) jobs,
       MIN(hiredate) first,
       MAX(ename) last_name
FROM emp;
""", """
<ul><li>Aggregate (group) functions return <b>one result for a set of rows</b>.</li>
<li><code>COUNT(*)</code> counts all rows; <code>COUNT(comm)</code> counts only non-NULL values (2). All aggregates except COUNT(*) <b>ignore NULLs</b>.</li>
<li><code>SUM</code> and <code>AVG</code> work on numbers; <code>MAX</code>, <code>MIN</code> and <code>COUNT</code> also work on dates and text (MAX(ename) = alphabetically last).</li>
<li><code>COUNT(DISTINCT job)</code> counts the different jobs.</li></ul>
"""))

P.append(QE("q2_19", "GROUP BY with ORDER BY", """
SELECT deptno, COUNT(*) emps,
       SUM(sal) total,
       ROUND(AVG(sal)) avg
FROM emp
WHERE deptno IS NOT NULL
GROUP BY deptno
ORDER BY deptno;

SELECT deptno, job, COUNT(*) n
FROM emp
WHERE deptno IN (20, 30)
GROUP BY deptno, job
ORDER BY deptno, n DESC, job;
""", """
<ul><li><b>GROUP BY</b> divides the rows into groups with the same value(s); each aggregate is calculated per group, giving one row per group.</li>
<li>Every column in the SELECT list that is not inside an aggregate function <b>must</b> be in GROUP BY (otherwise: ORA-00979 not a GROUP BY expression).</li>
<li>Grouping by two columns makes one group for every (deptno, job) combination.</li>
<li><code>ORDER BY</code> sorts the final result; <code>DESC</code> gives descending order, and the alias <code>n</code> can be used. Without ORDER BY, Oracle does not guarantee any row order.</li></ul>
"""))

P.append(QE("q2_20", "HAVING: filter groups", """
SELECT deptno, COUNT(*) emps,
       AVG(sal) avg_sal
FROM emp
WHERE deptno IS NOT NULL
GROUP BY deptno
HAVING COUNT(*) > 2;

SELECT job, SUM(sal) total
FROM emp
WHERE job <> 'PRESIDENT'
GROUP BY job
HAVING SUM(sal) >= 50000
ORDER BY total DESC;
""", """
<ul><li><b>WHERE</b> filters <b>rows</b> before grouping; it cannot use aggregate functions.</li>
<li><b>HAVING</b> filters <b>groups</b> after grouping; it is used with aggregate functions.</li>
<li>Second query: the president row is removed first (WHERE), then the rows are grouped by job, and only jobs with a total salary of at least 50000 are kept (HAVING). The result is sorted by total.</li></ul>
"""))

P.append(QE("q2_21", "ORDER BY: ascending, descending, multiple columns, NULLs", """
SELECT ename, deptno, sal
FROM emp
WHERE sal >= 40000
ORDER BY deptno, sal DESC;

SELECT ename, comm FROM emp
WHERE deptno = 30
ORDER BY comm DESC;

SELECT ename, sal * 12 annual
FROM emp
WHERE deptno = 20
ORDER BY 2;
""", """
<ul><li><code>ORDER BY deptno, sal DESC</code>: sort by deptno (ascending, the default); within the same deptno, by salary in descending order.</li>
<li>In Oracle, <b>NULLs are treated as the largest value</b>: they come last in ASC and <b>first in DESC</b> (change with <code>NULLS FIRST / NULLS LAST</code>).</li>
<li>You can sort by a column position (<code>ORDER BY 2</code>) or by an alias.</li>
<li>ORDER BY is always the last clause of a query.</li></ul>
"""))

# ------------------------------------------------------------------ 2.5 joins
P.append(QE("q2_22", "Inner (equi) join and non-equi join", """
SELECT e.ename, e.job, d.dname, d.loc
FROM emp e INNER JOIN dept d
ON e.deptno = d.deptno
WHERE e.sal >= 45000;

-- Oracle traditional syntax
SELECT e.ename, d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno
AND d.loc = 'VADODARA';

-- Non-equi join
SELECT e.ename, e.sal, s.grade
FROM emp e JOIN salgrade s
ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.deptno = 30
ORDER BY s.grade, e.ename;
""", """
<ul><li>An <b>inner join</b> returns only the rows that have a match in both tables. MEHUL (no department) and OPERATIONS (no employees) never appear.</li>
<li>An <b>equi join</b> uses <code>=</code> in the join condition. The ANSI syntax uses <code>JOIN ... ON</code>; the traditional Oracle syntax lists the tables with commas and puts the condition in WHERE.</li>
<li><b>Table aliases</b> (e, d) make the query short, and they are needed when both tables have a column with the same name (deptno).</li>
<li>A <b>non-equi join</b> uses an operator other than = (here BETWEEN) to match each salary with its grade.</li></ul>
"""))

P.append(QE("q2_23", "Outer joins: LEFT, RIGHT and FULL", """
SELECT e.ename, d.dname
FROM emp e LEFT OUTER JOIN dept d
ON e.deptno = d.deptno
WHERE e.empno >= 108;

SELECT d.dname, COUNT(e.empno) emps
FROM emp e RIGHT OUTER JOIN dept d
ON e.deptno = d.deptno
GROUP BY d.dname
ORDER BY emps;

SELECT e.ename, d.dname
FROM emp e FULL OUTER JOIN dept d
ON e.deptno = d.deptno
WHERE e.ename IS NULL
   OR d.dname IS NULL;
""", """
<ul><li><b>LEFT OUTER JOIN</b>: all rows of the left table (emp) plus the matching rows of the right table. MEHUL appears with a NULL dname.</li>
<li><b>RIGHT OUTER JOIN</b>: all rows of the right table (dept). OPERATIONS appears with no employee, so <code>COUNT(e.empno)</code> = 0.</li>
<li><b>FULL OUTER JOIN</b>: all rows of both tables. The WHERE keeps only the unmatched rows from either side.</li>
<li>Old Oracle syntax for an outer join uses <code>(+)</code> on the side that may be missing: <code>WHERE e.deptno = d.deptno(+)</code> is a left join.</li></ul>
"""))

P.append(QE("q2_24", "Cross join and self join", """
SELECT e.ename, d.dname
FROM emp e CROSS JOIN dept d
WHERE e.empno = 101;

SELECT w.ename worker, m.ename manager
FROM emp w JOIN emp m
ON w.mgr = m.empno
WHERE m.job = 'MANAGER'
ORDER BY manager, worker;
""", """
<ul><li>A <b>cross join</b> (Cartesian product) pairs every row of one table with every row of the other: 10 × 4 = 40 rows. Here only RAJESH's 4 combinations are shown.</li>
<li>A <b>self join</b> joins a table with <b>itself</b> using two different aliases. Here <code>w</code> plays the worker and <code>m</code> plays the manager; the condition <code>w.mgr = m.empno</code> finds each worker's manager.</li>
<li>Use <code>LEFT JOIN</code> in the self join to also list RAJESH, who has no manager.</li></ul>
"""))

# ------------------------------------------------------------------ 2.6 sub-queries, set operators
P.append(QE("q2_25", "Single-row and multiple-row sub-queries", """
SELECT ename, sal FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp);

SELECT ename, job FROM emp
WHERE job = (SELECT job FROM emp
             WHERE ename = 'NEHA');

SELECT ename, deptno FROM emp
WHERE deptno IN (SELECT deptno FROM dept
                 WHERE loc IN ('SURAT',
                               'RAJKOT'));
""", """
<ul><li>A <b>sub-query</b> (inner query) is a SELECT inside another SQL statement. The inner query runs first and its result is used by the outer query.</li>
<li><b>Single-row sub-query</b>: returns one value. Use single-row operators <code>= &gt; &lt; &gt;= &lt;= &lt;&gt;</code>. The average salary is 40800.</li>
<li><b>Multiple-row sub-query</b>: returns many values. Use <code>IN</code>, <code>ANY</code>, <code>ALL</code> or <code>EXISTS</code>. Using = with many rows gives ORA-01427.</li>
<li>A sub-query is always written in brackets and cannot have its own ORDER BY.</li></ul>
"""))

P.append(QE("q2_26", "Nested sub-query up to 3 levels", """
-- Employees working in the department
-- of the highest-paid manager
SELECT ename, job, deptno FROM emp
WHERE deptno =
  (SELECT deptno FROM emp
   WHERE sal =
     (SELECT MAX(sal) FROM emp
      WHERE job = 'MANAGER'));

-- 2nd highest salary
SELECT MAX(sal) second_max FROM emp
WHERE sal < (SELECT MAX(sal) FROM emp);
""", """
<p>Sub-queries can be nested inside each other (up to 255 levels in Oracle). The <b>innermost</b> query runs first:</p>
<ol><li>Level 3: <code>MAX(sal)</code> of managers = 60000.</li>
<li>Level 2: the deptno of the employee earning 60000 = 20.</li>
<li>Level 1: all employees of department 20.</li></ol>
<p>The second query is a classic exam question: the highest salary among those that are less than the overall maximum gives the 2nd highest salary.</p>
"""))

P.append(QE("q2_27", "Correlated sub-query", """
-- Earns more than own dept average
SELECT e.ename, e.deptno, e.sal
FROM emp e
WHERE e.sal > (SELECT AVG(sal)
               FROM emp
               WHERE deptno = e.deptno);

-- Highest paid in each department
SELECT ename, deptno, sal FROM emp e
WHERE sal = (SELECT MAX(sal) FROM emp
             WHERE deptno = e.deptno)
ORDER BY deptno;
""", """
<ul><li>In a <b>correlated sub-query</b>, the inner query uses a column of the outer query (<code>e.deptno</code>), so it cannot run alone.</li>
<li>It is executed <b>once for every row</b> of the outer query: for NEHA (dept 20), it calculates the average of dept 20 (42333.33) and compares her salary 45000.</li>
<li>A normal (nested) sub-query runs only <b>once</b>; a correlated sub-query runs many times, so it can be slower.</li>
<li>MEHUL has a NULL deptno, so <code>deptno = NULL</code> never matches and he is not listed.</li></ul>
"""))

P.append(QE("q2_28", "Set operators: UNION, UNION ALL, INTERSECT, MINUS", """
SELECT job FROM emp WHERE deptno = 10
UNION
SELECT job FROM emp WHERE deptno = 30;

SELECT job FROM emp WHERE deptno = 10
UNION ALL
SELECT job FROM emp WHERE deptno = 30;

SELECT job FROM emp WHERE deptno = 20
INTERSECT
SELECT job FROM emp WHERE deptno = 30;

SELECT deptno FROM dept
MINUS
SELECT deptno FROM emp;
""", """
<ul><li><b>UNION</b>: rows from both queries, with duplicates removed and the result sorted.</li>
<li><b>UNION ALL</b>: all rows from both queries, <b>including duplicates</b> (SALESMAN twice), not sorted. It is faster.</li>
<li><b>INTERSECT</b>: only rows present in <b>both</b> results: jobs found in both dept 20 and 30.</li>
<li><b>MINUS</b>: rows of the first query that are <b>not</b> in the second: departments without employees (40).</li>
<li>Both queries must select the same number of columns with compatible types.</li></ul>
"""))

PROGRAMS = P
