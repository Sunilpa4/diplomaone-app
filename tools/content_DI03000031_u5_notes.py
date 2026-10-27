"""DI03000031 Unit 5 notes: PL/SQL fundamentals, control structures, cursors, exceptions, procedures/functions, triggers."""
from sql_content import make_TS

SN = {
    "s_block": """
DECLARE
  -- declarations (optional)
BEGIN
  -- executable statements (mandatory)
EXCEPTION
  -- error handlers (optional)
END;
/
""",
    "s_hello": """
SET SERVEROUTPUT ON
BEGIN
  DBMS_OUTPUT.PUT_LINE('Hello');
END;
/
""",
    "s_declare": """
v_name  VARCHAR2(20);
v_count NUMBER(4) := 0;
v_rate  NUMBER(5,2) DEFAULT 8.5;
v_city  VARCHAR2(15) NOT NULL
        := 'Surat';
c_pi    CONSTANT NUMBER := 3.14;
v_flag  BOOLEAN := FALSE;
v_dob   DATE := SYSDATE;
""",
    "s_select_into": """
SELECT col1, col2
INTO   var1, var2
FROM   table_name
WHERE  condition;  -- exactly one row
""",
    "s_type": """
variable table.column%TYPE;

v_name emp.ename%TYPE;
v_sal  emp.sal%TYPE;
v_new  v_sal%TYPE;
""",
    "s_rowtype": """
record table%ROWTYPE;

v_emp emp%ROWTYPE;
...
SELECT * INTO v_emp
FROM emp WHERE empno = 106;
DBMS_OUTPUT.PUT_LINE(v_emp.ename);
""",
    "s_if": """
IF condition THEN
  statements;
END IF;

IF condition THEN
  statements;
ELSE
  statements;
END IF;

IF condition1 THEN
  statements;
ELSIF condition2 THEN
  statements;
ELSE
  statements;
END IF;
""",
    "s_case": """
-- simple CASE
CASE expression
  WHEN value1 THEN statements;
  WHEN value2 THEN statements;
  ELSE statements;
END CASE;

-- searched CASE
CASE
  WHEN condition1 THEN statements;
  WHEN condition2 THEN statements;
  ELSE statements;
END CASE;
""",
    "s_loop": """
LOOP
  statements;
  EXIT WHEN condition;
END LOOP;
""",
    "s_while": """
WHILE condition LOOP
  statements;
END LOOP;
""",
    "s_for": """
FOR counter IN [REVERSE] low..high
LOOP
  statements;
END LOOP;
""",
    "s_exit": """
<<outer>>
FOR i IN 1..3 LOOP
  FOR j IN 1..3 LOOP
    EXIT outer WHEN i * j = 4;
    CONTINUE WHEN j = 2;
    DBMS_OUTPUT.PUT(i * j || ' ');
  END LOOP;
END LOOP outer;
-- prints: 1 3 2
""",
    "s_goto": """
BEGIN
  IF v_marks < 35 THEN
    GOTO fail_label;
  END IF;
  DBMS_OUTPUT.PUT_LINE('Pass');
  GOTO end_label;
  <<fail_label>>
  DBMS_OUTPUT.PUT_LINE('Fail');
  <<end_label>>
  NULL;
END;
""",
    "s_null": """
IF v_sal > 50000 THEN
  v_tax := v_sal * 0.2;
ELSE
  NULL;  -- do nothing
END IF;
""",
    "s_implicit": """
UPDATE emp SET sal = sal + 2000
WHERE job = 'CLERK';
IF SQL%FOUND THEN
  DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT
    || ' rows updated');
END IF;
""",
    "s_explicit": """
DECLARE
  CURSOR c_emp IS
    SELECT ename, sal FROM emp;   -- 1
  v_name emp.ename%TYPE;
  v_sal  emp.sal%TYPE;
BEGIN
  OPEN c_emp;                     -- 2
  LOOP
    FETCH c_emp INTO v_name, v_sal; -- 3
    EXIT WHEN c_emp%NOTFOUND;
    -- process the row
  END LOOP;
  CLOSE c_emp;                    -- 4
END;
""",
    "s_cursor_for": """
FOR record IN cursor_name LOOP
  statements;  -- use record.column
END LOOP;

FOR r IN (SELECT ename FROM emp) LOOP
  DBMS_OUTPUT.PUT_LINE(r.ename);
END LOOP;
""",
    "s_param_cursor": """
CURSOR c_emp (p_dno NUMBER) IS
  SELECT ename FROM emp
  WHERE deptno = p_dno;
...
OPEN c_emp(20);
FOR r IN c_emp(30) LOOP ... END LOOP;
""",
    "s_exc": """
BEGIN
  statements;
EXCEPTION
  WHEN exception1 THEN
    statements;
  WHEN exception2 OR exception3 THEN
    statements;
  WHEN OTHERS THEN
    statements;
END;
""",
    "s_user_exc": """
DECLARE
  e_low_bal EXCEPTION;          -- declare
BEGIN
  IF v_amt > v_bal THEN
    RAISE e_low_bal;            -- raise
  END IF;
EXCEPTION
  WHEN e_low_bal THEN           -- handle
    DBMS_OUTPUT.PUT_LINE('Low balance');
END;
""",
    "s_pragma": """
DECLARE
  e_child EXCEPTION;
  PRAGMA EXCEPTION_INIT(e_child, -2292);
BEGIN
  DELETE FROM dept WHERE deptno = 10;
EXCEPTION
  WHEN e_child THEN
    DBMS_OUTPUT.PUT_LINE('Has employees');
END;
""",
    "s_rae": """
RAISE_APPLICATION_ERROR(
  error_number,  -- -20000 to -20999
  'message');

RAISE_APPLICATION_ERROR(-20010,
  'Salary below minimum');
""",
    "s_proc": """
CREATE [OR REPLACE] PROCEDURE name
  (param1 [IN|OUT|IN OUT] datatype,
   param2 ...)
IS | AS
  -- local declarations
BEGIN
  statements;
[EXCEPTION
  handlers;]
END [name];
/
""",
    "s_exec": """
-- from SQL*Plus
EXEC raise_sal(105)
EXECUTE raise_sal(108, 20)

-- from a PL/SQL block
BEGIN
  raise_sal(p_empno => 104, p_pct => 5);
END;
/
""",
    "s_modes": """
CREATE OR REPLACE PROCEDURE get_emp (
  p_no   IN  NUMBER,
  p_name OUT VARCHAR2,
  p_sal  OUT NUMBER) AS
BEGIN
  SELECT ename, sal INTO p_name, p_sal
  FROM emp WHERE empno = p_no;
END;
/
""",
    "s_func": """
CREATE [OR REPLACE] FUNCTION name
  (param1 [IN] datatype, ...)
RETURN datatype
IS | AS
  -- local declarations
BEGIN
  statements;
  RETURN value;
END [name];
/
""",
    "s_func_use": """
v_pay := annual_pay(107);

SELECT ename, annual_pay(empno)
FROM emp;
""",
    "s_drop_sub": """
DROP PROCEDURE raise_sal;
DROP FUNCTION annual_pay;

SELECT object_name, object_type
FROM user_objects
WHERE object_type IN
      ('PROCEDURE', 'FUNCTION');
""",
    "s_trigger": """
CREATE [OR REPLACE] TRIGGER name
{BEFORE | AFTER}
{INSERT | UPDATE [OF col] | DELETE}
  [OR ...]
ON table_name
[FOR EACH ROW]
[WHEN (condition)]
[DECLARE
  declarations]
BEGIN
  statements;
END;
/
""",
    "s_before": """
CREATE OR REPLACE TRIGGER trg_upper
BEFORE INSERT OR UPDATE ON emp
FOR EACH ROW
BEGIN
  :NEW.ename := UPPER(:NEW.ename);
  IF :NEW.sal < 0 THEN
    RAISE_APPLICATION_ERROR(-20002,
      'Salary cannot be negative');
  END IF;
END;
/
""",
    "s_after": """
CREATE OR REPLACE TRIGGER trg_sal_log
AFTER UPDATE OF sal ON emp
FOR EACH ROW
BEGIN
  INSERT INTO sal_log
  VALUES (:OLD.empno, :OLD.sal,
          :NEW.sal, SYSDATE);
END;
/
""",
    "s_stmt": """
CREATE OR REPLACE TRIGGER trg_emp_stmt
AFTER DELETE ON emp
BEGIN
  DBMS_OUTPUT.PUT_LINE('Rows deleted');
END;
/
""",
    "s_manage_trg": """
ALTER TRIGGER trg_upper DISABLE;
ALTER TRIGGER trg_upper ENABLE;
ALTER TABLE emp DISABLE ALL TRIGGERS;
ALTER TABLE emp ENABLE ALL TRIGGERS;
DROP TRIGGER trg_upper;

SELECT trigger_name, status
FROM user_triggers;
""",
}

T = make_TS(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Fundamentals of PL/SQL"},
    "items": [
        T("Basics of PL/SQL and Block Structure", """
<p><b>PL/SQL</b> (Procedural Language extension to SQL) is Oracle's programming language. It combines the <b>data manipulation power of SQL</b> with the <b>processing power of a procedural language</b>: variables, conditions, loops, error handling and subprograms.</p>
<p>SQL is a <b>non-procedural</b> language: it says <i>what</i> data is needed, but cannot use IF, loops or variables. PL/SQL adds these features, and SQL statements can be written directly inside PL/SQL.</p>
<h4>Structure of a PL/SQL block</h4>
<p>The basic unit of a PL/SQL program is a <b>block</b>. A block has three sections:</p>
<table><tr><th>Section</th><th>Keyword</th><th>Contents</th><th>Required?</th></tr>
<tr><td>Declaration</td><td>DECLARE</td><td>Variables, constants, cursors, user-defined exceptions</td><td>Optional</td></tr>
<tr><td>Executable</td><td>BEGIN</td><td>SQL and PL/SQL statements</td><td>Mandatory</td></tr>
<tr><td>Exception handling</td><td>EXCEPTION</td><td>Actions to take when an error occurs</td><td>Optional</td></tr></table>
<p>The block ends with <b>END;</b> and in SQL*Plus a <b>/</b> on a new line runs it.</p>
@@s_block@@
<h4>Types of blocks</h4>
<ul><li><b>Anonymous block:</b> has no name, is not stored in the database, and is compiled every time it runs.</li>
<li><b>Named blocks (subprograms):</b> procedures, functions, triggers (and packages). They are compiled once and <b>stored</b> in the database.</li>
<li>Blocks can be <b>nested</b>: a BEGIN ... END block can be written inside the executable or exception section of another block.</li></ul>
<h4>Displaying output</h4>
<p><b>DBMS_OUTPUT.PUT_LINE(text)</b> is a built-in procedure that prints a line. In SQL*Plus the command <b>SET SERVEROUTPUT ON</b> must be given first, otherwise nothing is displayed.</p>
@@s_hello@@
<p>Comments: <code>-- single line</code> and <code>/* multi-line */</code>. Every statement ends with a semicolon.</p>
""", diagram="db5_block", programs=["q5_1"]),
        T("Advantages of PL/SQL over SQL", """
<p>PL/SQL code is executed by the <b>PL/SQL engine</b> inside the Oracle server. Procedural statements (IF, loops, assignments) are executed by the procedural statement executor, and SQL statements are passed to the <b>SQL statement executor</b>.</p>
<h4>Advantages</h4>
<ol><li><b>Procedural capabilities:</b> variables, constants, conditions (IF, CASE) and loops (LOOP, WHILE, FOR), which plain SQL does not have.</li>
<li><b>Better performance / reduced network traffic:</b> SQL sends one statement at a time to the server. A PL/SQL block sends many statements together in one call.</li>
<li><b>Error handling:</b> errors are handled in the EXCEPTION section, so the program can show a proper message instead of stopping abruptly.</li>
<li><b>Modularity and reusability:</b> code can be stored as procedures, functions and packages and called by many applications.</li>
<li><b>Stored and pre-compiled:</b> stored subprograms are compiled once and kept in the database, so they run faster.</li>
<li><b>Security:</b> users can be given permission to execute a procedure without having direct access to the tables.</li>
<li><b>Triggers:</b> code that runs automatically on INSERT, UPDATE or DELETE, for business rules and auditing.</li>
<li><b>Tight integration with SQL:</b> all SQL data types, functions and DML statements can be used, and %TYPE / %ROWTYPE link variables to table columns.</li>
<li><b>Portability:</b> PL/SQL programs run on any operating system where Oracle runs.</li></ol>
<table><tr><th>SQL</th><th>PL/SQL</th></tr>
<tr><td>Non-procedural (declarative)</td><td>Procedural</td></tr>
<tr><td>Executes one statement at a time</td><td>Executes a whole block at a time</td></tr>
<tr><td>No variables, conditions or loops</td><td>Supports variables, IF, CASE, loops</td></tr>
<tr><td>No error handling</td><td>EXCEPTION section for error handling</td></tr>
<tr><td>Used to query and change data</td><td>Used to write programs, procedures, functions, triggers</td></tr>
<tr><td>Can be embedded in PL/SQL</td><td>Cannot be embedded in SQL (but functions can be called from SQL)</td></tr></table>
""", diagram="db5_engine"),
        T("Data Types, Variables and Constants", """
<p>A <b>variable</b> is a named memory location that holds a value during program execution. Every variable must be declared in the DECLARE section before it is used.</p>
<h4>Declaration syntax</h4>
<p><code>name [CONSTANT] datatype [NOT NULL] [:= | DEFAULT value];</code></p>
@@s_declare@@
<ul><li>A variable without an initial value is <b>NULL</b>.</li>
<li><b>CONSTANT</b> must be initialised and cannot be changed afterwards.</li>
<li><b>NOT NULL</b> variables must be initialised.</li>
<li>Naming convention: <code>v_</code> for variables, <code>c_</code> for constants, <code>p_</code> for parameters. This avoids confusion with column names.</li></ul>
<h4>PL/SQL data types</h4>
<table><tr><th>Category</th><th>Data types</th></tr>
<tr><td>Numeric</td><td>NUMBER(p,s), INTEGER, BINARY_INTEGER, PLS_INTEGER</td></tr>
<tr><td>Character</td><td>CHAR(n), VARCHAR2(n), LONG</td></tr>
<tr><td>Date / time</td><td>DATE, TIMESTAMP</td></tr>
<tr><td>Boolean</td><td>BOOLEAN (TRUE, FALSE, NULL) – only in PL/SQL, not a column type</td></tr>
<tr><td>LOB</td><td>CLOB, BLOB, BFILE</td></tr>
<tr><td>Anchored (attribute)</td><td>%TYPE, %ROWTYPE</td></tr>
<tr><td>Composite</td><td>RECORD, collections (TABLE, VARRAY)</td></tr></table>
<h4>Operators</h4>
<ul><li>Assignment: <code>:=</code> (comparison uses <code>=</code>).</li>
<li>Arithmetic: <code>+ - * / **</code>; concatenation: <code>||</code>.</li>
<li>Comparison: <code>= != &lt;&gt; &lt; &gt; &lt;= &gt;= BETWEEN IN LIKE IS NULL</code>; logical: AND, OR, NOT.</li></ul>
<h4>Reading table data: SELECT INTO</h4>
@@s_select_into@@
<p>SELECT INTO must return <b>exactly one row</b>: no row raises NO_DATA_FOUND, more than one raises TOO_MANY_ROWS. For many rows a cursor is used.</p>
""", programs=["q5_2", "q5_3"]),
        T("%TYPE Attribute", """
<p>The <b>%TYPE</b> attribute declares a variable with the <b>same data type as a table column</b> or another variable. The type is "anchored" to the column.</p>
@@s_type@@
<h4>Advantages</h4>
<ul><li>You need not know the exact data type and size of the column.</li>
<li>If the column definition changes (e.g. ENAME from VARCHAR2(10) to VARCHAR2(30)), the variable automatically uses the new type and the program does not need to be changed.</li>
<li>It avoids errors like VALUE_ERROR caused by a variable that is smaller than the column.</li></ul>
<p>%TYPE copies the data type and size, but not the NOT NULL constraint or the default value of the column.</p>
""", programs=["q5_4"]),
        T("%ROWTYPE Attribute", """
<p>The <b>%ROWTYPE</b> attribute declares a <b>record</b> that represents a <b>complete row</b> of a table, view or cursor. The record has one field for each column, with the same name and data type.</p>
@@s_rowtype@@
<ul><li>Fields are accessed with dot notation: <code>record.column</code>, e.g. <code>v_emp.sal</code>.</li>
<li><code>SELECT * INTO v_emp</code> fills all fields at once.</li>
<li>A cursor record can be declared with <code>cursor_name%ROWTYPE</code>.</li>
<li>If columns are added to or removed from the table, the record changes automatically.</li></ul>
<table><tr><th>%TYPE</th><th>%ROWTYPE</th></tr>
<tr><td>Data type of one column</td><td>Structure of a whole row</td></tr>
<tr><td>Declares a scalar variable</td><td>Declares a record (many fields)</td></tr>
<tr><td><code>v_sal emp.sal%TYPE;</code></td><td><code>v_emp emp%ROWTYPE;</code></td></tr>
<tr><td>Used directly: v_sal</td><td>Used with a field: v_emp.sal</td></tr></table>
""", diagram="db5_type_rowtype", programs=["q5_5"]),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 Control Structures"},
    "items": [
        T("Control Structures and IF Statements", """
<p><b>Control structures</b> decide the order in which statements are executed. PL/SQL has three types:</p>
<table><tr><th>Type</th><th>Purpose</th><th>Statements</th></tr>
<tr><td>Conditional (selection)</td><td>Run statements depending on a condition</td><td>IF-THEN, IF-THEN-ELSE, IF-THEN-ELSIF, CASE</td></tr>
<tr><td>Iterative (loops)</td><td>Repeat statements</td><td>LOOP, WHILE LOOP, FOR LOOP, EXIT, CONTINUE</td></tr>
<tr><td>Sequential</td><td>Jump or do nothing</td><td>GOTO, NULL</td></tr></table>
<h4>IF statements</h4>
@@s_if@@
<ul><li><b>IF-THEN:</b> statements run only if the condition is TRUE.</li>
<li><b>IF-THEN-ELSE:</b> one of two groups runs.</li>
<li><b>IF-THEN-ELSIF:</b> conditions are tested in order; the first TRUE branch runs and the rest are skipped. ELSE (optional) runs if none is TRUE.</li>
<li>A condition that is <b>NULL</b> is treated like FALSE.</li>
<li>The keyword is <b>ELSIF</b>, and every IF must end with <b>END IF;</b>. IF statements can be nested.</li></ul>
""", diagram="db5_if", programs=["q5_6", "q5_7"]),
        T("CASE Statement", """
<p>The <b>CASE</b> statement selects one sequence of statements from many alternatives. It is often clearer than a long IF-ELSIF ladder.</p>
@@s_case@@
<ul><li><b>Simple CASE:</b> compares one expression (selector) with values in the WHEN clauses.</li>
<li><b>Searched CASE:</b> has no selector; each WHEN has its own Boolean condition.</li>
<li>The first matching WHEN is executed. If nothing matches and there is no ELSE, the error <b>CASE_NOT_FOUND</b> (ORA-06592) is raised.</li>
<li>A CASE statement ends with <b>END CASE;</b>. A CASE <b>expression</b> returns a value and ends with END, e.g. <code>v_txt := CASE WHEN v_sal &gt; 50000 THEN 'High' ELSE 'Low' END;</code></li></ul>
""", programs=["q5_8"]),
        T("Iterative Control: LOOP, WHILE and FOR", """
<p>Loops execute a group of statements repeatedly. PL/SQL has three kinds of loops.</p>
<h4>1. Basic (simple) LOOP</h4>
@@s_loop@@
<p>Repeats until an <b>EXIT</b> or <b>EXIT WHEN</b> statement is reached. The condition is checked inside the loop, so the body runs <b>at least once</b>. Without EXIT it is an infinite loop.</p>
<h4>2. WHILE LOOP</h4>
@@s_while@@
<p>The condition is checked <b>before</b> each iteration. If it is FALSE (or NULL) at the start, the body never runs. The counter is managed by the programmer.</p>
<h4>3. Numeric FOR LOOP</h4>
@@s_for@@
<ul><li>Runs a <b>fixed number of times</b>, from low to high in steps of 1.</li>
<li>The counter is declared <b>implicitly</b>, is local to the loop, and cannot be assigned a value.</li>
<li><b>REVERSE</b> counts from high down to low (bounds are still written low..high).</li>
<li>If low &gt; high, the loop body does not run.</li></ul>
<p>A fourth kind, the <b>cursor FOR loop</b>, processes rows of a query (see Cursors).</p>
""", diagram="db5_loops", programs=["q5_9", "q5_10", "q5_11"]),
        T("Nested Loops, EXIT and CONTINUE", """
<p>A loop can be written inside another loop (<b>nested loop</b>). The inner loop completes all its iterations for each iteration of the outer loop.</p>
<ul><li><b>EXIT</b> leaves the innermost loop immediately; <b>EXIT WHEN condition</b> leaves it when the condition is TRUE.</li>
<li><b>CONTINUE</b> / <b>CONTINUE WHEN</b> skips the rest of the current iteration and starts the next one.</li>
<li>A loop can have a <b>label</b> <code>&lt;&lt;name&gt;&gt;</code>. <code>EXIT name</code> leaves the labelled (outer) loop directly.</li></ul>
@@s_exit@@
<p>Loops can also contain SQL statements: for example a FOR loop can insert many rows into a table in one block.</p>
""", programs=["q5_12", "q5_13"]),
        T("Sequential Control: GOTO and NULL", """
<p><b>Sequential control statements</b> change the normal top-to-bottom flow without a condition or loop.</p>
<h4>GOTO statement</h4>
<p><b>GOTO label;</b> transfers control unconditionally to the statement after the label <code>&lt;&lt;label&gt;&gt;</code>.</p>
@@s_goto@@
<ul><li>A label must be followed by at least one executable statement (NULL can be used).</li>
<li>GOTO cannot jump into an IF, a loop or a nested block, and cannot jump out of an exception handler back into the block.</li>
<li>GOTO makes programs hard to read, so it should be avoided; IF and loops are preferred.</li></ul>
<h4>NULL statement</h4>
<p>The <b>NULL;</b> statement does nothing; control passes to the next statement. It is used where a statement is required by the syntax but no action is needed, e.g. in an ELSE branch, after a label, or in an exception handler that ignores an error.</p>
@@s_null@@
"""),
    ],
}

SEC_5_3 = {
    "title": {"en": "5.3 Cursors"},
    "items": [
        T("Cursor: Concept and Types", """
<p>When Oracle executes an SQL statement it creates a private memory area called the <b>context area</b>. A <b>cursor</b> is a <b>pointer to this context area</b>. It holds the rows returned by a SELECT, called the <b>active set</b>, and points to one row at a time.</p>
<p>Cursors are needed because SELECT INTO can handle only one row. With a cursor, a program can process a multi-row result <b>row by row</b>.</p>
<h4>Types of static cursors</h4>
<table><tr><th>Implicit cursor</th><th>Explicit cursor</th></tr>
<tr><td>Created automatically by Oracle</td><td>Declared by the programmer in DECLARE</td></tr>
<tr><td>For INSERT, UPDATE, DELETE and SELECT INTO</td><td>For a SELECT returning many rows</td></tr>
<tr><td>Name is <b>SQL</b></td><td>Name given by the user</td></tr>
<tr><td>Opened, fetched and closed automatically</td><td>Programmer uses OPEN, FETCH, CLOSE</td></tr>
<tr><td>Attributes: SQL%FOUND, SQL%NOTFOUND, SQL%ROWCOUNT, SQL%ISOPEN</td><td>Attributes: c%FOUND, c%NOTFOUND, c%ROWCOUNT, c%ISOPEN</td></tr>
<tr><td>Less control</td><td>Full control over each row</td></tr></table>
<p>They are called <b>static</b> cursors because the SQL statement is fixed when the program is compiled.</p>
""", diagram="db5_cursor"),
        T("Implicit Cursor and its Attributes", """
<p>Oracle automatically opens an <b>implicit cursor</b> named <b>SQL</b> for every DML statement (INSERT, UPDATE, DELETE) and for SELECT INTO. Its attributes give information about the <b>most recent</b> statement.</p>
<table><tr><th>Attribute</th><th>Returns</th></tr>
<tr><td>SQL%FOUND</td><td>TRUE if the statement affected (or SELECT INTO returned) at least one row</td></tr>
<tr><td>SQL%NOTFOUND</td><td>TRUE if no row was affected (opposite of %FOUND)</td></tr>
<tr><td>SQL%ROWCOUNT</td><td>Number of rows affected</td></tr>
<tr><td>SQL%ISOPEN</td><td>Always FALSE, because the cursor is closed right after the statement</td></tr></table>
@@s_implicit@@
<p>The attributes must be checked immediately after the statement, because the next SQL statement overwrites them.</p>
""", programs=["q5_14"]),
        T("Explicit Cursor: Steps and Attributes", """
<p>An <b>explicit cursor</b> is declared by the programmer for a SELECT statement that returns more than one row. It is used in four steps:</p>
<ol><li><b>DECLARE</b> the cursor: <code>CURSOR name IS select_statement;</code></li>
<li><b>OPEN</b> the cursor: <code>OPEN name;</code> executes the query, builds the active set and places the pointer before the first row.</li>
<li><b>FETCH</b> rows: <code>FETCH name INTO variables | record;</code> copies the current row and moves the pointer forward. Usually done in a loop.</li>
<li><b>CLOSE</b> the cursor: <code>CLOSE name;</code> releases the memory.</li></ol>
@@s_explicit@@
<h4>Explicit cursor attributes</h4>
<table><tr><th>Attribute</th><th>Returns</th></tr>
<tr><td>%ISOPEN</td><td>TRUE if the cursor is open</td></tr>
<tr><td>%FOUND</td><td>TRUE if the last FETCH returned a row</td></tr>
<tr><td>%NOTFOUND</td><td>TRUE if the last FETCH returned no row (end of active set)</td></tr>
<tr><td>%ROWCOUNT</td><td>Number of rows fetched so far</td></tr></table>
<ul><li><code>EXIT WHEN c%NOTFOUND</code> should come immediately after FETCH.</li>
<li>Opening an open cursor raises CURSOR_ALREADY_OPEN; fetching from a closed cursor raises INVALID_CURSOR.</li></ul>
""", diagram="db5_cursor_steps", programs=["q5_15", "q5_16"]),
        T("Cursor FOR Loop and Parameterized Cursor", """
<h4>Cursor FOR loop</h4>
<p>A <b>cursor FOR loop</b> is the simplest way to process every row of a cursor. It automatically</p>
<ul><li>declares a record for the row,</li><li>opens the cursor,</li><li>fetches each row into the record,</li><li>exits when all rows are processed, and</li><li>closes the cursor.</li></ul>
@@s_cursor_for@@
<p>The SELECT can also be written directly in the loop (an <b>inline cursor</b>), without declaring a cursor.</p>
<h4>Parameterized cursor</h4>
<p>A cursor can accept <b>parameters</b>, so the same cursor can be opened many times with different values. Parameter data types are given without size.</p>
@@s_param_cursor@@
""", programs=["q5_17", "q5_18"]),
    ],
}

SEC_5_4 = {
    "title": {"en": "5.4 Exception Handling"},
    "items": [
        T("Exceptions: Concept and Syntax", """
<p>An <b>exception</b> is an error that occurs while a PL/SQL block is running, e.g. a SELECT INTO that finds no row or a division by zero. When an exception is <b>raised</b>, normal execution stops and control jumps to the <b>EXCEPTION</b> section.</p>
@@s_exc@@
<ul><li>The handler whose name matches the exception runs; then the block ends normally and control returns to the caller (or the enclosing block).</li>
<li><b>WHEN OTHERS</b> handles any exception not named before it, and must be the last handler.</li>
<li>If there is no matching handler, the exception <b>propagates</b> to the enclosing block. If no block handles it, the program stops with an error message.</li>
<li><b>SQLCODE</b> returns the error number and <b>SQLERRM</b> the error message (useful in WHEN OTHERS).</li></ul>
<h4>Types of exceptions</h4>
<table><tr><th>Type</th><th>Raised by</th><th>Name</th></tr>
<tr><td>Predefined</td><td>Oracle, automatically</td><td>Given by Oracle (e.g. NO_DATA_FOUND)</td></tr>
<tr><td>Non-predefined</td><td>Oracle, automatically</td><td>No name; programmer names it with PRAGMA EXCEPTION_INIT</td></tr>
<tr><td>User-defined</td><td>Programmer, with RAISE</td><td>Declared by the programmer</td></tr></table>
<p><b>Advantages:</b> errors are handled in one place, the program gives clear messages, and normal code is not mixed with error checks.</p>
""", diagram="db5_exceptions"),
        T("Predefined Exceptions", """
<p><b>Predefined exceptions</b> are common Oracle errors that already have a name. They are raised automatically.</p>
<table><tr><th>Exception</th><th>Oracle error</th><th>Raised when</th></tr>
<tr><td>NO_DATA_FOUND</td><td>ORA-01403</td><td>SELECT INTO returns no row</td></tr>
<tr><td>TOO_MANY_ROWS</td><td>ORA-01422</td><td>SELECT INTO returns more than one row</td></tr>
<tr><td>ZERO_DIVIDE</td><td>ORA-01476</td><td>A number is divided by zero</td></tr>
<tr><td>DUP_VAL_ON_INDEX</td><td>ORA-00001</td><td>Duplicate value in a primary key / unique column</td></tr>
<tr><td>VALUE_ERROR</td><td>ORA-06502</td><td>Value too large for a variable, or conversion error</td></tr>
<tr><td>INVALID_NUMBER</td><td>ORA-01722</td><td>Conversion of a string to a number fails in SQL</td></tr>
<tr><td>INVALID_CURSOR</td><td>ORA-01001</td><td>Illegal cursor operation, e.g. FETCH from a closed cursor</td></tr>
<tr><td>CURSOR_ALREADY_OPEN</td><td>ORA-06511</td><td>Opening a cursor that is already open</td></tr>
<tr><td>CASE_NOT_FOUND</td><td>ORA-06592</td><td>No WHEN matches in a CASE statement without ELSE</td></tr>
<tr><td>LOGIN_DENIED</td><td>ORA-01017</td><td>Invalid user name or password</td></tr></table>
<p>To continue after an error inside a loop, put the risky statement in a <b>nested block</b> with its own EXCEPTION section.</p>
""", programs=["q5_19", "q5_20"]),
        T("User-defined Exceptions, PRAGMA EXCEPTION_INIT and RAISE_APPLICATION_ERROR", """
<h4>User-defined exceptions</h4>
<p>The programmer can define exceptions for <b>business rules</b>, e.g. insufficient balance or invalid marks. Three steps:</p>
<ol><li><b>Declare</b> in DECLARE: <code>e_name EXCEPTION;</code></li>
<li><b>Raise</b> explicitly: <code>RAISE e_name;</code></li>
<li><b>Handle</b>: <code>WHEN e_name THEN ...</code></li></ol>
@@s_user_exc@@
<p>An unhandled user-defined exception gives ORA-06510. SQLCODE returns +1 for it.</p>
<h4>PRAGMA EXCEPTION_INIT (non-predefined exceptions)</h4>
<p>Many Oracle errors have no predefined name. <b>PRAGMA EXCEPTION_INIT</b> associates a user-declared exception name with an Oracle error number, so it can be handled by name.</p>
@@s_pragma@@
<h4>RAISE_APPLICATION_ERROR</h4>
<p>This built-in procedure stops the program and returns a <b>user-defined error number and message</b> to the caller, just like an Oracle error.</p>
@@s_rae@@
<ul><li>The error number must be between <b>-20000 and -20999</b>; the message can be up to 2048 bytes.</li>
<li>Any changes made by the failed statement are rolled back.</li>
<li>It is mainly used in stored procedures and triggers.</li></ul>
<table><tr><th>RAISE</th><th>RAISE_APPLICATION_ERROR</th></tr>
<tr><td>Raises a named exception</td><td>Raises an error with a number and message</td></tr>
<tr><td>Usually handled in the same block</td><td>Usually sent back to the application</td></tr>
<tr><td>No custom message</td><td>Custom message, number -20000 to -20999</td></tr></table>
""", programs=["q5_21", "q5_22"]),
    ],
}

SEC_5_5 = {
    "title": {"en": "5.5 Procedures and Functions"},
    "items": [
        T("Stored Procedures: Creating and Executing", """
<p>A <b>stored procedure</b> is a named PL/SQL block that performs a specific task. It is compiled once and <b>stored in the database</b>, and can be called many times by name, with parameters.</p>
@@s_proc@@
<ul><li><b>OR REPLACE</b> re-creates the procedure if it already exists (no need to drop it).</li>
<li>The header lists the parameters with their mode and data type (without size).</li>
<li>Local variables are declared after IS / AS; no DECLARE keyword is used.</li>
<li>SQL*Plus shows "Procedure created." If there are compilation errors it shows a warning; <code>SHOW ERRORS</code> lists them.</li></ul>
<h4>Executing a procedure</h4>
@@s_exec@@
<ul><li>Positional notation: arguments in the order of the parameters.</li>
<li>Named notation: <code>parameter =&gt; value</code>, in any order.</li>
<li>Parameters with DEFAULT values can be omitted.</li></ul>
<h4>Advantages of stored procedures</h4>
<ul><li>Better performance: compiled once, and one call executes many statements.</li>
<li>Reusability and modularity: one procedure is shared by all applications.</li>
<li>Security: users can be given EXECUTE permission without access to the tables.</li>
<li>Easy maintenance: a change is made in one place.</li></ul>
""", programs=["q5_23", "q5_25"]),
        T("Parameter Modes: IN, OUT and IN OUT", """
<p>Parameters pass values between the caller and a subprogram. The parameters in the header are <b>formal parameters</b>; the values passed in a call are <b>actual parameters</b>.</p>
<table><tr><th>Mode</th><th>Direction</th><th>Inside the subprogram</th><th>Actual parameter</th></tr>
<tr><td><b>IN</b> (default)</td><td>Caller → subprogram</td><td>Read-only (like a constant)</td><td>Constant, expression or variable</td></tr>
<tr><td><b>OUT</b></td><td>Subprogram → caller</td><td>Starts as NULL; a value is assigned</td><td>Must be a variable</td></tr>
<tr><td><b>IN OUT</b></td><td>Both directions</td><td>Can be read and changed</td><td>Must be a variable</td></tr></table>
@@s_modes@@
<p>A procedure can return <b>several values</b> using OUT parameters, e.g. name and salary of an employee.</p>
""", programs=["q5_24"]),
        T("Stored Functions", """
<p>A <b>stored function</b> is a named PL/SQL block that <b>returns exactly one value</b> using the RETURN statement. It is stored in the database like a procedure.</p>
@@s_func@@
<ul><li>The header must contain <b>RETURN datatype</b>.</li>
<li>The body must execute a <b>RETURN value;</b> statement; otherwise ORA-06503 (function returned without value) is raised.</li>
<li>A function is called as part of an <b>expression</b>, not as a statement.</li>
<li>Functions normally use only IN parameters.</li></ul>
@@s_func_use@@
<h4>Calling functions from SQL</h4>
<p>A stored function can be used in SELECT, WHERE, ORDER BY, etc. like built-in functions, provided it does not perform DML on tables, has only IN parameters and returns an SQL data type.</p>
<p>A function can call itself (<b>recursion</b>), e.g. factorial.</p>
<h4>Dropping subprograms</h4>
@@s_drop_sub@@
""", programs=["q5_26", "q5_27"]),
        T("Procedure vs Function", """
<table><tr><th>Procedure</th><th>Function</th></tr>
<tr><td>Performs an action (task)</td><td>Computes and returns a value</td></tr>
<tr><td>No RETURN clause in the header</td><td>Must have RETURN datatype in the header</td></tr>
<tr><td>Can return zero, one or many values through OUT parameters</td><td>Returns exactly one value through RETURN</td></tr>
<tr><td>Called as a statement: <code>EXEC p(1);</code> or <code>p(1);</code></td><td>Called in an expression: <code>v := f(1);</code></td></tr>
<tr><td>Cannot be used in a SELECT statement</td><td>Can be used in SQL statements (if it has no DML)</td></tr>
<tr><td>RETURN statement (without value) only exits</td><td>RETURN value is mandatory</td></tr>
<tr><td>Used for business logic and DML</td><td>Used for calculations</td></tr></table>
<h4>Common features</h4>
<ul><li>Both are named, compiled and stored in the database (stored subprograms).</li>
<li>Both can have parameters, local declarations and an exception section.</li>
<li>Both are listed in USER_OBJECTS / USER_PROCEDURES and their code is in USER_SOURCE.</li>
<li>Both are removed with DROP PROCEDURE / DROP FUNCTION.</li></ul>
""", diagram="db5_proc_func"),
    ],
}

SEC_5_6 = {
    "title": {"en": "5.6 Triggers"},
    "items": [
        T("Fundamentals of Triggers", """
<p>A <b>trigger</b> is a named PL/SQL block stored in the database that is executed (<b>fired</b>) <b>automatically</b> when a specified event occurs on a table, e.g. INSERT, UPDATE or DELETE.</p>
@@s_trigger@@
<h4>Parts of a trigger</h4>
<ul><li><b>Trigger timing:</b> BEFORE or AFTER the event.</li>
<li><b>Triggering event:</b> INSERT, UPDATE (optionally OF specific columns), DELETE, or a combination with OR.</li>
<li><b>Table:</b> ON table_name.</li>
<li><b>Trigger level:</b> FOR EACH ROW (row level) or statement level (default).</li>
<li><b>Restriction:</b> WHEN (condition) – row triggers only; NEW and OLD are written without a colon here.</li>
<li><b>Trigger body:</b> the PL/SQL block.</li></ul>
<h4>:NEW and :OLD</h4>
<p>In a row trigger, <b>:OLD</b> holds the column values before the change and <b>:NEW</b> the values after the change. Conditional predicates <b>INSERTING</b>, <b>UPDATING</b> and <b>DELETING</b> tell which event fired the trigger.</p>
<h4>Uses of triggers</h4>
<ul><li>Enforcing complex business rules and validation.</li><li>Auditing: recording who changed what and when.</li>
<li>Automatically generating or deriving column values.</li><li>Maintaining copies or summary data in other tables.</li>
<li>Preventing invalid transactions (e.g. deleting the president's record, changes on holidays).</li></ul>
<h4>Trigger vs procedure</h4>
<table><tr><th>Trigger</th><th>Procedure</th></tr>
<tr><td>Fires automatically on an event</td><td>Executed explicitly by a call (EXEC)</td></tr>
<tr><td>No parameters</td><td>Can have parameters</td></tr>
<tr><td>Cannot use COMMIT / ROLLBACK</td><td>Can use COMMIT / ROLLBACK</td></tr>
<tr><td>Attached to a table</td><td>Independent object</td></tr></table>
""", diagram="db5_trigger_flow"),
        T("Types of Triggers: BEFORE, AFTER, FOR EACH ROW, FOR EACH STATEMENT", """
<h4>Based on timing</h4>
<ul><li><b>BEFORE trigger:</b> fires before the INSERT / UPDATE / DELETE is performed. Used to <b>validate</b> data or <b>change :NEW values</b> before they are saved.</li>
<li><b>AFTER trigger:</b> fires after the statement is performed. Used for <b>auditing</b>, logging and updating other tables. :NEW cannot be changed.</li></ul>
<h4>Based on level</h4>
<ul><li><b>Row-level trigger</b> (FOR EACH ROW): fires <b>once for each row</b> affected. If no row is affected, it does not fire. :NEW and :OLD are available.</li>
<li><b>Statement-level trigger</b> (default, no FOR EACH ROW): fires <b>once per statement</b>, even if 0 rows are affected. :NEW and :OLD are not available.</li></ul>
<h4>Based on event</h4>
<p>INSERT, UPDATE and DELETE triggers. Combining 2 timings × 2 levels × 3 events gives <b>12 types</b> of DML triggers, e.g. BEFORE INSERT row trigger, AFTER DELETE statement trigger.</p>
<table><tr><th>Event</th><th>:OLD</th><th>:NEW</th></tr>
<tr><td>INSERT</td><td>NULL</td><td>New values</td></tr>
<tr><td>UPDATE</td><td>Values before update</td><td>Values after update</td></tr>
<tr><td>DELETE</td><td>Deleted values</td><td>NULL</td></tr></table>
<h4>Firing order for one statement</h4>
<ol><li>BEFORE statement trigger</li><li>For each row: BEFORE row trigger → row change → AFTER row trigger</li><li>AFTER statement trigger</li></ol>
@@s_stmt@@
<p>Other kinds of triggers (not DML) are INSTEAD OF triggers on views, and system / DDL triggers (e.g. on LOGON or CREATE).</p>
""", diagram="db5_trigger_types", programs=["q5_30"]),
        T("BEFORE Triggers", """
<p>A <b>BEFORE row trigger</b> runs before each row is inserted, updated or deleted. It is the right place to:</p>
<ul><li><b>Validate</b> data and reject it with RAISE_APPLICATION_ERROR.</li>
<li><b>Modify</b> the new values by assigning to :NEW (e.g. convert to upper case, set a default date).</li>
<li><b>Prevent</b> certain operations (e.g. deleting a manager, reducing a salary).</li></ul>
@@s_before@@
<ul><li>If the trigger raises an error, the triggering statement fails and its changes are rolled back. SQL*Plus shows the error, ORA-06512 with the trigger line, and ORA-04088 with the trigger name.</li>
<li><b>UPDATE OF col</b> makes the trigger fire only when that column is updated.</li>
<li><b>WHEN (condition)</b> restricts the rows for which the trigger body runs.</li></ul>
""", programs=["q5_28", "q5_31"]),
        T("AFTER Triggers and Auditing", """
<p>An <b>AFTER trigger</b> runs after the data has been changed. Because the change has already passed all constraints, AFTER triggers are used for:</p>
<ul><li><b>Auditing:</b> storing old and new values, the action and the date in a log table.</li>
<li><b>Maintaining other tables:</b> e.g. updating stock after a sale, or a total in a summary table.</li>
<li><b>Notifications / messages</b> after a change.</li></ul>
@@s_after@@
<p>One trigger can handle several events (INSERT OR UPDATE OR DELETE) and use the predicates INSERTING, UPDATING and DELETING to know which one occurred. In an AFTER row trigger :NEW and :OLD can be read but not changed.</p>
""", programs=["q5_29"]),
        T("Managing Triggers", """
<p>Triggers are database objects and can be enabled, disabled, viewed and dropped.</p>
@@s_manage_trg@@
<ul><li>A trigger is <b>enabled</b> when it is created. A disabled trigger still exists but does not fire.</li>
<li>Disabling is useful while loading a large amount of data.</li>
<li><b>USER_TRIGGERS</b> shows the trigger name, type, event, table, status and body.</li>
<li>Dropping a table drops all its triggers automatically.</li></ul>
<h4>Restrictions on triggers</h4>
<ul><li>A trigger cannot contain COMMIT, ROLLBACK or SAVEPOINT.</li>
<li>A row trigger cannot query or modify the table on which it is defined (mutating table error ORA-04091).</li>
<li>:NEW can be changed only in a BEFORE row trigger.</li>
<li>Too many triggers make DML slower and the logic harder to follow.</li></ul>
""", programs=["q5_32"]),
    ],
}

NOTES = [SEC_5_1, SEC_5_2, SEC_5_3, SEC_5_4, SEC_5_5, SEC_5_6]
