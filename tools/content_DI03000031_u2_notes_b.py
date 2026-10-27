"""DI03000031 Unit 2 notes part B: 2.4 aggregate functions, GROUP BY, HAVING, ORDER BY; 2.5 joins; 2.6 sub-queries and set operators."""
from sql_content import make_TS

SN = {
    "s_group": """
SELECT col, aggregate(col2)
FROM table
[WHERE row_condition]
GROUP BY col
[HAVING group_condition]
[ORDER BY col [ASC | DESC]];
""",
    "s_order": """
ORDER BY col1 [ASC | DESC]
        [NULLS FIRST | NULLS LAST],
         col2 [ASC | DESC], ...
""",
    "s_join": """
SELECT t1.col, t2.col
FROM t1 [INNER] JOIN t2
ON t1.key = t2.key;

-- Oracle traditional syntax
SELECT t1.col, t2.col
FROM t1, t2
WHERE t1.key = t2.key;
""",
    "s_natural": """
SELECT ename, dname
FROM emp NATURAL JOIN dept;

SELECT ename, dname
FROM emp JOIN dept USING (deptno);
""",
    "s_outer": """
FROM t1 LEFT  [OUTER] JOIN t2 ON ...
FROM t1 RIGHT [OUTER] JOIN t2 ON ...
FROM t1 FULL  [OUTER] JOIN t2 ON ...

-- Oracle (+) syntax: + on the side
-- that may have no matching row
WHERE e.deptno = d.deptno(+)  -- LEFT
WHERE e.deptno(+) = d.deptno  -- RIGHT
""",
    "s_cross": """
SELECT c.color, s.sz
FROM colors c CROSS JOIN sizes s;

SELECT c.color, s.sz
FROM colors c, sizes s;
""",
    "s_self": """
SELECT w.ename worker, m.ename manager
FROM emp w JOIN emp m
ON w.mgr = m.empno;
""",
    "s_subq": """
SELECT columns FROM table
WHERE col operator
      (SELECT col FROM table
       WHERE condition);
""",
    "s_sub_other": """
-- in UPDATE
UPDATE emp SET sal = sal * 1.1
WHERE deptno = (SELECT deptno FROM dept
                WHERE dname = 'SALES');

-- in FROM (inline view)
SELECT d, avg_sal
FROM (SELECT deptno d, AVG(sal) avg_sal
      FROM emp GROUP BY deptno)
WHERE avg_sal > 40000;
""",
    "s_set": """
SELECT col_list FROM t1
UNION | UNION ALL | INTERSECT | MINUS
SELECT col_list FROM t2
[ORDER BY ...];
""",
}

T = make_TS(SN)

SEC_2_4 = {
    "title": {"en": "2.4 Aggregate Functions, GROUP BY, HAVING and ORDER BY"},
    "items": [
        T("Aggregate (Group) Functions", """
<p>Aggregate functions work on a <b>set of rows</b> and return a <b>single value</b>. They can be used on the whole table or on groups made by GROUP BY.</p>
<table><tr><th>Function</th><th>Returns</th></tr>
<tr><td><code>COUNT(*)</code></td><td>number of rows (including NULLs and duplicates)</td></tr>
<tr><td><code>COUNT(col)</code></td><td>number of non-NULL values in col</td></tr>
<tr><td><code>COUNT(DISTINCT col)</code></td><td>number of different non-NULL values</td></tr>
<tr><td><code>SUM(col)</code></td><td>total of the values (numbers only)</td></tr>
<tr><td><code>AVG(col)</code></td><td>average of the values (numbers only)</td></tr>
<tr><td><code>MAX(col)</code></td><td>largest value (number, text or date)</td></tr>
<tr><td><code>MIN(col)</code></td><td>smallest value (number, text or date)</td></tr></table>
<ul><li>All aggregate functions <b>ignore NULL values</b>, except COUNT(*). So <code>AVG(comm)</code> = SUM of the commissions ÷ number of non-NULL commissions. Use <code>AVG(NVL(comm, 0))</code> to count NULLs as 0.</li>
<li>DISTINCT or ALL (the default) can be used inside: <code>SUM(DISTINCT sal)</code>.</li>
<li>An aggregate cannot be used in WHERE; use HAVING.</li>
<li>Without GROUP BY, a SELECT with an aggregate cannot also list a normal column (ORA-00937: not a single-group group function).</li></ul>
""", programs=["q2_18"]),
        T("GROUP BY and HAVING Clauses", """
@@s_group@@
<p><b>GROUP BY</b> divides the rows of a table into groups that have the same value in the given column(s). The aggregate functions are then calculated <b>for each group</b>, and the query returns one row per group.</p>
<ul><li>Every column in SELECT that is not inside an aggregate function must be written in GROUP BY. (A GROUP BY column need not appear in SELECT.)</li>
<li>Grouping can be on several columns: <code>GROUP BY deptno, job</code> makes one group for every combination.</li>
<li>NULL values form a group of their own.</li>
<li>Column aliases cannot be used in GROUP BY.</li></ul>
<p><b>HAVING</b> applies a condition to the <b>groups</b>, after grouping. It is normally used with aggregate functions: <code>HAVING COUNT(*) &gt; 2</code>.</p>
<h4>WHERE vs HAVING</h4>
<table><tr><th>WHERE</th><th>HAVING</th></tr>
<tr><td>Filters individual rows</td><td>Filters groups</td></tr>
<tr><td>Applied before GROUP BY</td><td>Applied after GROUP BY</td></tr>
<tr><td>Cannot use aggregate functions</td><td>Usually uses aggregate functions</td></tr>
<tr><td>Can be used without GROUP BY</td><td>Normally used with GROUP BY</td></tr>
<tr><td>Used in SELECT, UPDATE, DELETE</td><td>Used only in SELECT</td></tr></table>
""", diagram="db2_groupby", programs=["q2_19", "q2_20"]),
        T("ORDER BY Clause and Order of Execution", """
<p><b>ORDER BY</b> sorts the rows of the result. It is always the <b>last</b> clause of a SELECT.</p>
@@s_order@@
<ul><li><b>ASC</b> (ascending) is the default; <b>DESC</b> gives descending order.</li>
<li>Several columns: rows are sorted by the first column, and rows with equal values are sorted by the next one.</li>
<li>You can sort by a column name, an expression, a <b>column alias</b> or a <b>column position</b> (<code>ORDER BY 2</code>). The column need not be in the SELECT list (except with DISTINCT).</li>
<li>NULLs are treated as the largest values: last in ASC, first in DESC (unless NULLS FIRST/LAST is given).</li>
<li>Numbers sort by value, dates from earliest to latest, and text alphabetically (capital letters before small letters).</li>
<li>Without ORDER BY, the order of rows is not guaranteed.</li></ul>
<h4>Logical order of execution</h4>
<p>FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY. That is why an alias defined in SELECT can be used in ORDER BY but not in WHERE or HAVING.</p>
""", diagram="db2_query_order", programs=["q2_21"]),
    ],
}

SEC_2_5 = {
    "title": {"en": "2.5 Joins"},
    "items": [
        T("Joins: Inner (Equi), Natural and Non-Equi Join", """
<p>A <b>join</b> combines rows from two or more tables based on a related column, so that data stored in separate tables (normalised data) can be shown together.</p>
<p><b>Types of joins:</b> inner join (equi, natural, non-equi), outer join (left, right, full), cross join and self join.</p>
<h4>Inner join</h4>
<p>Returns only those rows that have <b>matching values in both tables</b>. Unmatched rows of either table are left out.</p>
@@s_join@@
<ul><li><b>Equi join</b>: the join condition uses the equality operator <code>=</code>, usually primary key = foreign key.</li>
<li>When the same column name exists in both tables, it must be qualified with the table name or alias (<code>e.deptno</code>), otherwise ORA-00918: column ambiguously defined.</li>
<li>To join n tables you need at least n − 1 join conditions.</li></ul>
<h4>Natural join and USING</h4>
@@s_natural@@
<p>A <b>natural join</b> automatically joins on all columns with the same name in both tables (and shows the common column once). <code>USING (col)</code> names the common column explicitly.</p>
<h4>Non-equi join</h4>
<p>A join whose condition uses an operator other than <code>=</code>, such as BETWEEN, &lt;, &gt;. Example: finding each employee's salary grade from the SALGRADE table using <code>e.sal BETWEEN s.losal AND s.hisal</code>.</p>
""", diagram="db2_joins", programs=["q2_22"]),
        T("Outer Joins: Left, Right and Full", """
<p>An <b>outer join</b> returns the matching rows <b>plus</b> the rows that have no match in the other table. The missing columns are filled with NULL.</p>
@@s_outer@@
<ul><li><b>LEFT OUTER JOIN</b>: all rows from the <b>left</b> table + matching rows of the right table. Example: every employee, even one without a department.</li>
<li><b>RIGHT OUTER JOIN</b>: all rows from the <b>right</b> table + matching rows of the left table. Example: every department, even one without employees.</li>
<li><b>FULL OUTER JOIN</b>: all rows from <b>both</b> tables, matched where possible.</li>
<li>The Oracle <b>(+)</b> operator is placed on the side of the <b>deficient</b> table (the one whose columns may be NULL). It cannot be used for a full outer join.</li></ul>
<h4>Inner join vs outer join</h4>
<table><tr><th>Inner join</th><th>Outer join</th></tr>
<tr><td>Only matching rows</td><td>Matching + non-matching rows</td></tr>
<tr><td>No NULLs added</td><td>NULLs for missing columns</td></tr>
<tr><td>One type</td><td>Left, right, full</td></tr>
<tr><td>Fewer (or equal) rows</td><td>More (or equal) rows</td></tr></table>
""", programs=["q2_23"]),
        T("Cross Join (Cartesian Product)", """
<p>A <b>cross join</b> returns the <b>Cartesian product</b> of two tables: every row of the first table combined with every row of the second. If the tables have m and n rows, the result has <b>m × n</b> rows.</p>
@@s_cross@@
<ul><li>It has no join condition.</li>
<li>A cross join happens accidentally when the join condition is forgotten in the traditional syntax; with large tables this produces a huge result.</li>
<li>Uses: generating all combinations (colours × sizes, students × subjects), test data.</li></ul>
""", diagram="db2_cross_join"),
        T("Self Join", """
<p>A <b>self join</b> joins a table <b>with itself</b>. The same table is used twice with two different aliases, as if they were two separate tables.</p>
@@s_self@@
<ul><li>Used when a table has a column that refers to another row of the same table (a <b>recursive relationship</b>), e.g. <code>emp.mgr</code> refers to <code>emp.empno</code> of the manager.</li>
<li>Other uses: finding employees in the same city, students with the same marks, or comparing rows within a table.</li>
<li>A self join can be an inner join or an outer join (LEFT JOIN keeps the employee who has no manager).</li></ul>
""", diagram="db2_self_join", programs=["q2_24"]),
    ],
}

SEC_2_6 = {
    "title": {"en": "2.6 Sub-queries and Set Operators"},
    "items": [
        T("Sub-queries: Single-row, Multiple-row and Nested", """
<p>A <b>sub-query</b> (inner query / nested query) is a SELECT statement written inside another SQL statement (the outer query). The result of the inner query is used by the outer query.</p>
@@s_subq@@
<h4>Rules</h4>
<ul><li>A sub-query is enclosed in brackets and is usually placed on the right side of the comparison.</li>
<li>A simple (non-correlated) sub-query runs <b>once, before</b> the outer query.</li>
<li>ORDER BY is not allowed inside a sub-query in WHERE.</li>
<li>Use single-row operators with single-row sub-queries and multiple-row operators with multiple-row sub-queries.</li></ul>
<h4>Types</h4>
<ol><li><b>Single-row sub-query</b>: returns exactly one value; used with <code>= &lt;&gt; &gt; &lt; &gt;= &lt;=</code>. Often uses an aggregate (MAX, AVG).</li>
<li><b>Multiple-row sub-query</b>: returns several rows; used with <code>IN, NOT IN, ANY, ALL, EXISTS</code>. If = is used with many rows, ORA-01427 occurs.</li>
<li><b>Multiple-column sub-query</b>: returns more than one column: <code>WHERE (deptno, sal) IN (SELECT deptno, MAX(sal) ... GROUP BY deptno)</code>.</li>
<li><b>Nested sub-query</b>: a sub-query inside another sub-query. The innermost one runs first.</li>
<li><b>Correlated sub-query</b>: uses columns of the outer query (next topic).</li></ol>
<p>Sub-queries can also be used in INSERT, UPDATE, DELETE, CREATE TABLE and in the FROM clause (an inline view):</p>
@@s_sub_other@@
""", diagram="db2_subquery", programs=["q2_25", "q2_26"]),
        T("Correlated Sub-query", """
<p>A <b>correlated sub-query</b> is a sub-query that refers to a column of the <b>outer query</b>. Because it depends on the current outer row, it is executed <b>once for each row</b> processed by the outer query.</p>
<h4>Working</h4>
<ol><li>The outer query takes a candidate row.</li>
<li>The inner query is executed using the values of that row.</li>
<li>The outer row is kept or rejected depending on the inner result.</li>
<li>The steps repeat for the next outer row.</li></ol>
<h4>Nested vs correlated sub-query</h4>
<table><tr><th>Nested (simple)</th><th>Correlated</th></tr>
<tr><td>Inner query is independent</td><td>Inner query uses outer columns</td></tr>
<tr><td>Executed once</td><td>Executed once per outer row</td></tr>
<tr><td>Inner runs first, then outer</td><td>Outer row first, then inner</td></tr>
<tr><td>Faster</td><td>Slower for big tables</td></tr>
<tr><td>Can run alone</td><td>Cannot run alone</td></tr></table>
<p>Typical uses: comparing each row with its own group (salary above the department average), EXISTS / NOT EXISTS tests, finding the top earner in each department.</p>
""", programs=["q2_27"]),
        T("Set Operators: UNION, UNION ALL, INTERSECT and MINUS", """
<p><b>Set operators</b> combine the <b>results of two or more SELECT statements</b> into one result.</p>
@@s_set@@
<table><tr><th>Operator</th><th>Returns</th></tr>
<tr><td><b>UNION</b></td><td>all distinct rows from both queries (duplicates removed, sorted)</td></tr>
<tr><td><b>UNION ALL</b></td><td>all rows from both queries, including duplicates (not sorted, fastest)</td></tr>
<tr><td><b>INTERSECT</b></td><td>only the rows common to both queries</td></tr>
<tr><td><b>MINUS</b></td><td>rows of the first query that are not in the second</td></tr></table>
<h4>Rules</h4>
<ul><li>Each SELECT must have the <b>same number of columns</b>, and the corresponding columns must have <b>compatible data types</b>.</li>
<li>The column headings are taken from the <b>first</b> SELECT.</li>
<li>ORDER BY may appear only once, at the end, and applies to the whole result.</li>
<li>All set operators have equal precedence and are evaluated from top to bottom; use brackets to change the order.</li>
<li>UNION and INTERSECT are commutative (order of queries does not matter); MINUS is not.</li></ul>
<h4>Join vs set operator</h4>
<p>A join combines <b>columns</b> of tables side by side (horizontally); a set operator combines <b>rows</b> of query results (vertically).</p>
""", diagram="db2_set_ops", programs=["q2_28"]),
    ],
}

NOTES_B = [SEC_2_4, SEC_2_5, SEC_2_6]
