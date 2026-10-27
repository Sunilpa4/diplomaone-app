"""DI03000031 RDBMS Unit 5 – PL/SQL and triggers (practicals 14-18). Real output from OraSim3 (tools/plsql.py)."""
from sql_content import QE
from sql_seed import SCOTT

P = []

# ------------------------------------------------------------------ 5.1 fundamentals
P.append(QE("q5_1", "First PL/SQL block: variables, constants and output", """
SET SERVEROUTPUT ON
DECLARE
  v_name  VARCHAR2(20) := 'Aarav';
  v_marks NUMBER(3)    := 82;
  c_univ  CONSTANT VARCHAR2(5) := 'GTU';
  v_today DATE := SYSDATE;
  v_pass  BOOLEAN := TRUE;
BEGIN
  DBMS_OUTPUT.PUT_LINE('Hello PL/SQL');
  DBMS_OUTPUT.PUT_LINE('Name : '
    || v_name);
  DBMS_OUTPUT.PUT_LINE('Marks: '
    || v_marks);
  DBMS_OUTPUT.PUT_LINE('Univ : '
    || c_univ);
  DBMS_OUTPUT.PUT_LINE('Date : '
    || TO_CHAR(v_today, 'DD-MON-YYYY'));
  IF v_pass THEN
    DBMS_OUTPUT.PUT_LINE('Result: PASS');
  END IF;
END;
/
""", """
<ul><li><b>SET SERVEROUTPUT ON</b> is a SQL*Plus command. Without it the lines written by DBMS_OUTPUT are not displayed.</li>
<li>The <b>DECLARE</b> section creates variables. <code>:=</code> is the assignment operator. A <b>CONSTANT</b> must get a value when declared and cannot be changed later.</li>
<li><b>DBMS_OUTPUT.PUT_LINE</b> prints one line; <code>||</code> joins strings. Numbers and dates are converted to text automatically, but TO_CHAR gives control over the format.</li>
<li>A BOOLEAN variable (TRUE / FALSE / NULL) can be tested with IF, but it cannot be printed directly.</li>
<li>The <b>/</b> on its own line sends the block to Oracle. After a successful run SQL*Plus shows <i>PL/SQL procedure successfully completed.</i></li></ul>
""", setup=""))

P.append(QE("q5_2", "Simple calculations: sum, average and area", """
SET SERVEROUTPUT ON
DECLARE
  a      NUMBER := 25;
  b      NUMBER := 40;
  c      NUMBER := 31;
  v_sum  NUMBER;
  v_avg  NUMBER(6,2);
  pi     CONSTANT NUMBER := 3.14;
  r      NUMBER := 7;
  v_area NUMBER;
BEGIN
  v_sum := a + b + c;
  v_avg := v_sum / 3;
  v_area := pi * r * r;
  DBMS_OUTPUT.PUT_LINE('Sum     = '
    || v_sum);
  DBMS_OUTPUT.PUT_LINE('Average = '
    || v_avg);
  DBMS_OUTPUT.PUT_LINE('Area    = '
    || v_area);
  DBMS_OUTPUT.PUT_LINE('Square  = '
    || POWER(a, 2));
  DBMS_OUTPUT.PUT_LINE('Mod     = '
    || MOD(b, 7));
END;
/
""", """
<ul><li>Arithmetic operators in PL/SQL are the same as in SQL: <code>+ - * /</code> and <code>**</code> for power.</li>
<li><b>v_avg</b> is declared as NUMBER(6,2), so 96 / 3 = 32 is stored as 32 (trailing zeros are not printed).</li>
<li>SQL single-row functions such as POWER, MOD, ROUND, UPPER and SUBSTR can be used directly in PL/SQL expressions.</li>
<li>Area = 3.14 × 7 × 7 = 153.86.</li>
<li>In the lab you can read values with substitution variables, e.g. <code>a NUMBER := &amp;a;</code>; SQL*Plus asks for the value before running the block.</li></ul>
""", setup=""))

P.append(QE("q5_3", "SELECT INTO: read a row into variables", """
SET SERVEROUTPUT ON
DECLARE
  v_empno  NUMBER := 104;
  v_name   VARCHAR2(10);
  v_job    VARCHAR2(9);
  v_sal    NUMBER(7,2);
  v_annual NUMBER(9,2);
BEGIN
  SELECT ename, job, sal
  INTO   v_name, v_job, v_sal
  FROM   emp
  WHERE  empno = v_empno;

  v_annual := v_sal * 12;
  DBMS_OUTPUT.PUT_LINE('Employee : '
    || v_name);
  DBMS_OUTPUT.PUT_LINE('Job      : '
    || v_job);
  DBMS_OUTPUT.PUT_LINE('Monthly  : '
    || v_sal);
  DBMS_OUTPUT.PUT_LINE('Annual   : '
    || v_annual);
END;
/
""", """
<ul><li><b>SELECT ... INTO</b> copies the column values of <b>exactly one row</b> into PL/SQL variables. The INTO list must match the SELECT list in number, order and type.</li>
<li>A PL/SQL variable (v_empno) can be used in the WHERE clause.</li>
<li>If no row matches, Oracle raises NO_DATA_FOUND; if more than one row matches, TOO_MANY_ROWS (see the exception programs).</li>
<li>Here the variables are declared with fixed types. The next program uses %TYPE, which is safer.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_4", "%TYPE attribute: anchored data types", """
SET SERVEROUTPUT ON
DECLARE
  v_name  emp.ename%TYPE;
  v_sal   emp.sal%TYPE;
  v_dname dept.dname%TYPE;
  v_new   v_sal%TYPE;
BEGIN
  SELECT e.ename, e.sal, d.dname
  INTO   v_name, v_sal, v_dname
  FROM   emp e, dept d
  WHERE  e.deptno = d.deptno
  AND    e.empno = 102;

  v_new := v_sal * 1.10;
  DBMS_OUTPUT.PUT_LINE(v_name
    || ' works in ' || v_dname);
  DBMS_OUTPUT.PUT_LINE('Salary : '
    || v_sal);
  DBMS_OUTPUT.PUT_LINE('After 10% raise : '
    || v_new);
END;
/
""", """
<ul><li><code>v_name emp.ename%TYPE</code> gives v_name <b>the same data type and size</b> as the ENAME column (VARCHAR2(10)).</li>
<li>%TYPE can also refer to another variable: <code>v_new v_sal%TYPE</code>.</li>
<li><b>Advantage:</b> if the column is later changed (e.g. ENAME becomes VARCHAR2(30)), the program still works without any change.</li>
<li>The SELECT can contain a join; it must still return only one row.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_5", "%ROWTYPE attribute: a record for a whole row", """
SET SERVEROUTPUT ON
DECLARE
  v_emp  emp%ROWTYPE;
  v_dept dept%ROWTYPE;
BEGIN
  SELECT * INTO v_emp
  FROM emp WHERE empno = 106;

  SELECT * INTO v_dept
  FROM dept WHERE deptno = v_emp.deptno;

  DBMS_OUTPUT.PUT_LINE('Empno : '
    || v_emp.empno);
  DBMS_OUTPUT.PUT_LINE('Name  : '
    || v_emp.ename);
  DBMS_OUTPUT.PUT_LINE('Job   : '
    || v_emp.job);
  DBMS_OUTPUT.PUT_LINE('Total : '
    || (v_emp.sal + v_emp.comm));
  DBMS_OUTPUT.PUT_LINE('Dept  : '
    || v_dept.dname || ', ' || v_dept.loc);
END;
/
""", """
<ul><li><code>v_emp emp%ROWTYPE</code> declares a <b>record</b> with one field for every column of EMP, with the same names and types.</li>
<li>A field is used with dot notation: <code>v_emp.ename</code>, <code>v_emp.sal</code>.</li>
<li><code>SELECT * INTO v_emp</code> fills all fields at once.</li>
<li>Total = 30000 + 3000 = 33000 for SUNIL. The record field v_emp.deptno is then used to read his department.</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ 5.2 control structures
P.append(QE("q5_6", "IF-THEN-ELSE: even/odd and largest of three", """
SET SERVEROUTPUT ON
DECLARE
  n NUMBER := 17;
  a NUMBER := 45;
  b NUMBER := 72;
  c NUMBER := 38;
BEGIN
  IF MOD(n, 2) = 0 THEN
    DBMS_OUTPUT.PUT_LINE(n || ' is even');
  ELSE
    DBMS_OUTPUT.PUT_LINE(n || ' is odd');
  END IF;

  IF a > b AND a > c THEN
    DBMS_OUTPUT.PUT_LINE('Largest: ' || a);
  ELSIF b > c THEN
    DBMS_OUTPUT.PUT_LINE('Largest: ' || b);
  ELSE
    DBMS_OUTPUT.PUT_LINE('Largest: ' || c);
  END IF;
END;
/
""", """
<ul><li><b>IF condition THEN ... ELSE ... END IF;</b> runs one of two groups of statements.</li>
<li>MOD(17, 2) = 1, so the ELSE part runs.</li>
<li>For the largest number, the first condition is FALSE (45 is not greater than 72), the ELSIF condition 72 &gt; 38 is TRUE.</li>
<li>Note the spelling <b>ELSIF</b> (not ELSEIF) and that every IF ends with <b>END IF;</b>.</li></ul>
""", setup=""))

P.append(QE("q5_7", "IF-ELSIF ladder: grade of a student", """
SET SERVEROUTPUT ON
DECLARE
  v_name  student.name%TYPE;
  v_marks student.marks%TYPE;
  v_grade CHAR(2);
BEGIN
  SELECT name, marks INTO v_name, v_marks
  FROM student WHERE rollno = 3;

  IF v_marks >= 85 THEN
    v_grade := 'AA';
  ELSIF v_marks >= 75 THEN
    v_grade := 'AB';
  ELSIF v_marks >= 65 THEN
    v_grade := 'BB';
  ELSIF v_marks >= 55 THEN
    v_grade := 'BC';
  ELSE
    v_grade := 'FF';
  END IF;
  DBMS_OUTPUT.PUT_LINE(v_name || ' : '
    || v_marks || ' marks, grade '
    || v_grade);
END;
/
""", """
<ul><li>An <b>IF-ELSIF</b> ladder tests conditions from top to bottom. Only the <b>first</b> TRUE branch runs; the rest are skipped.</li>
<li>Karan has 67 marks: 67 &gt;= 85 and 67 &gt;= 75 are FALSE, 67 &gt;= 65 is TRUE, so the grade is BB.</li>
<li>Because the conditions are checked in order, there is no need to write <code>v_marks &gt;= 65 AND v_marks &lt; 75</code>.</li></ul>
"""))

P.append(QE("q5_8", "CASE statement: simple and searched", """
SET SERVEROUTPUT ON
DECLARE
  v_day  NUMBER := 4;
  v_txt  VARCHAR2(10);
  v_sal  emp.sal%TYPE;
  v_name emp.ename%TYPE;
BEGIN
  CASE v_day
    WHEN 1 THEN v_txt := 'Monday';
    WHEN 2 THEN v_txt := 'Tuesday';
    WHEN 3 THEN v_txt := 'Wednesday';
    WHEN 4 THEN v_txt := 'Thursday';
    ELSE v_txt := 'Other';
  END CASE;
  DBMS_OUTPUT.PUT_LINE('Day ' || v_day
    || ' is ' || v_txt);

  SELECT ename, sal INTO v_name, v_sal
  FROM emp WHERE empno = 109;
  CASE
    WHEN v_sal >= 50000 THEN
      v_txt := 'High';
    WHEN v_sal >= 30000 THEN
      v_txt := 'Medium';
    ELSE
      v_txt := 'Low';
  END CASE;
  DBMS_OUTPUT.PUT_LINE(v_name || ' ('
    || v_sal || '): ' || v_txt);
END;
/
""", """
<ul><li><b>Simple CASE</b> compares one expression (v_day) with a list of values.</li>
<li><b>Searched CASE</b> has no expression after CASE; each WHEN contains its own condition. HETAL earns 40000, so the second WHEN is TRUE.</li>
<li>The CASE <i>statement</i> ends with <b>END CASE;</b>. If no WHEN matches and there is no ELSE, Oracle raises CASE_NOT_FOUND.</li>
<li>A CASE <i>expression</i> (ending with just END) can be used inside an assignment, e.g. <code>v_txt := CASE v_day WHEN 1 THEN 'Mon' END;</code></li></ul>
""", setup=SCOTT))

P.append(QE("q5_9", "Basic LOOP with EXIT WHEN: multiplication table", """
SET SERVEROUTPUT ON
DECLARE
  n NUMBER := 7;
  i NUMBER := 1;
BEGIN
  LOOP
    DBMS_OUTPUT.PUT_LINE(n || ' x ' || i
      || ' = ' || n * i);
    i := i + 1;
    EXIT WHEN i > 10;
  END LOOP;
END;
/
""", """
<ul><li>A <b>basic LOOP</b> repeats its statements until an <b>EXIT</b> or <b>EXIT WHEN</b> statement stops it. Without an exit it would run forever.</li>
<li>The condition is checked <b>inside</b> the loop, so the body always runs at least once.</li>
<li>The counter i must be declared, initialised and increased by the programmer.</li></ul>
""", setup=""))

P.append(QE("q5_10", "WHILE loop: reverse a number and sum of digits", """
SET SERVEROUTPUT ON
DECLARE
  n     NUMBER := 5274;
  t     NUMBER;
  d     NUMBER;
  v_rev NUMBER := 0;
  v_sum NUMBER := 0;
BEGIN
  t := n;
  WHILE t > 0 LOOP
    d := MOD(t, 10);
    v_rev := v_rev * 10 + d;
    v_sum := v_sum + d;
    t := TRUNC(t / 10);
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Number  : ' || n);
  DBMS_OUTPUT.PUT_LINE('Reverse : '
    || v_rev);
  DBMS_OUTPUT.PUT_LINE('Sum     : '
    || v_sum);
  IF v_rev = n THEN
    DBMS_OUTPUT.PUT_LINE('Palindrome');
  ELSE
    DBMS_OUTPUT.PUT_LINE('Not palindrome');
  END IF;
END;
/
""", """
<ul><li>A <b>WHILE loop</b> checks its condition <b>before</b> every iteration; if the condition is FALSE at the start, the body never runs.</li>
<li>MOD(t, 10) gives the last digit; TRUNC(t / 10) removes it. (PL/SQL division gives a decimal, so TRUNC is needed.)</li>
<li>5 + 2 + 7 + 4 = 18. The reverse 4725 is not equal to 5274, so the number is not a palindrome.</li></ul>
""", setup=""))

P.append(QE("q5_11", "FOR loop: factorial and REVERSE counting", """
SET SERVEROUTPUT ON
DECLARE
  n      NUMBER := 6;
  v_fact NUMBER := 1;
BEGIN
  FOR i IN 1..n LOOP
    v_fact := v_fact * i;
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Factorial of '
    || n || ' = ' || v_fact);

  FOR i IN REVERSE 1..5 LOOP
    DBMS_OUTPUT.PUT(i || ' ');
  END LOOP;
  DBMS_OUTPUT.NEW_LINE;

  FOR i IN 1..20 LOOP
    IF MOD(i, 3) = 0 THEN
      DBMS_OUTPUT.PUT(i || ' ');
    END IF;
  END LOOP;
  DBMS_OUTPUT.NEW_LINE;
END;
/
""", """
<ul><li>A <b>numeric FOR loop</b> runs a fixed number of times. The counter i is declared <b>automatically</b>, increases by 1 and cannot be assigned inside the loop.</li>
<li>6! = 1 × 2 × 3 × 4 × 5 × 6 = 720.</li>
<li><b>REVERSE</b> counts from the upper bound down to the lower bound; the range is still written low..high.</li>
<li><b>DBMS_OUTPUT.PUT</b> writes without ending the line; <b>NEW_LINE</b> ends it. The last loop prints the multiples of 3 up to 20.</li></ul>
""", setup=""))

P.append(QE("q5_12", "Nested loops: prime numbers from 2 to 30", """
SET SERVEROUTPUT ON
DECLARE
  v_prime BOOLEAN;
  v_count NUMBER := 0;
BEGIN
  FOR n IN 2..30 LOOP
    v_prime := TRUE;
    FOR d IN 2..TRUNC(SQRT(n)) LOOP
      IF MOD(n, d) = 0 THEN
        v_prime := FALSE;
        EXIT;
      END IF;
    END LOOP;
    IF v_prime THEN
      DBMS_OUTPUT.PUT(n || ' ');
      v_count := v_count + 1;
    END IF;
  END LOOP;
  DBMS_OUTPUT.NEW_LINE;
  DBMS_OUTPUT.PUT_LINE('Total primes: '
    || v_count);
END;
/
""", """
<ul><li>The outer loop takes each number n; the inner loop tries divisors from 2 to √n.</li>
<li><b>EXIT</b> leaves only the inner loop as soon as a divisor is found.</li>
<li>For n = 2 and 3 the inner range is 2..1, which is empty, so the inner loop does not run and the number stays prime.</li>
<li>A BOOLEAN flag (v_prime) remembers the result of the inner loop.</li></ul>
""", setup=""))

P.append(QE("q5_13", "FOR loop with DML: insert rows into a table", """
SET SERVEROUTPUT ON
CREATE TABLE squares (
  num NUMBER(3),
  sq  NUMBER(5),
  cube NUMBER(6)
);

BEGIN
  FOR i IN 1..6 LOOP
    INSERT INTO squares
    VALUES (i, i * i, i * i * i);
  END LOOP;
  COMMIT;
  DBMS_OUTPUT.PUT_LINE('Rows inserted');
END;
/

SELECT * FROM squares ORDER BY num;
""", """
<ul><li>SQL statements (INSERT, UPDATE, DELETE, COMMIT) can be written directly inside a PL/SQL block; the loop counter i is used as a value.</li>
<li>All six INSERTs are sent to the server in <b>one</b> block, which is faster than six separate SQL statements.</li>
<li>COMMIT makes the rows permanent. The SELECT afterwards is an ordinary SQL statement.</li></ul>
""", setup=""))

# ------------------------------------------------------------------ 5.3 cursors
P.append(QE("q5_14", "Implicit cursor attributes: SQL%FOUND, %NOTFOUND, %ROWCOUNT", """
SET SERVEROUTPUT ON
BEGIN
  UPDATE emp SET sal = sal + 2000
  WHERE job = 'CLERK';
  IF SQL%FOUND THEN
    DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT
      || ' clerks got a raise');
  END IF;

  DELETE FROM emp WHERE deptno = 40;
  IF SQL%NOTFOUND THEN
    DBMS_OUTPUT.PUT_LINE('No employee'
      || ' in dept 40');
  END IF;

  UPDATE emp SET comm = 1000
  WHERE comm IS NULL AND job = 'MANAGER';
  DBMS_OUTPUT.PUT_LINE('Rows changed: '
    || SQL%ROWCOUNT);
  ROLLBACK;
END;
/
""", """
<ul><li>Oracle opens an <b>implicit cursor</b> named <b>SQL</b> for every INSERT, UPDATE, DELETE and SELECT INTO.</li>
<li><b>SQL%FOUND</b> is TRUE if the last statement affected at least one row; <b>SQL%NOTFOUND</b> is the opposite.</li>
<li><b>SQL%ROWCOUNT</b> gives the number of rows affected: 2 clerks (KIRAN, VIJAY) and 2 managers.</li>
<li><b>SQL%ISOPEN</b> is always FALSE, because Oracle closes the implicit cursor immediately after the statement.</li>
<li>ROLLBACK cancels the changes so the table stays unchanged.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_15", "Explicit cursor: DECLARE, OPEN, FETCH, CLOSE", """
SET SERVEROUTPUT ON
DECLARE
  CURSOR c_emp IS
    SELECT ename, sal FROM emp
    WHERE deptno = 30
    ORDER BY sal DESC;
  v_name  emp.ename%TYPE;
  v_sal   emp.sal%TYPE;
  v_total NUMBER := 0;
BEGIN
  OPEN c_emp;
  LOOP
    FETCH c_emp INTO v_name, v_sal;
    EXIT WHEN c_emp%NOTFOUND;
    v_total := v_total + v_sal;
    DBMS_OUTPUT.PUT_LINE(c_emp%ROWCOUNT
      || '. ' || RPAD(v_name, 8) || v_sal);
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Employees: '
    || c_emp%ROWCOUNT);
  CLOSE c_emp;
  DBMS_OUTPUT.PUT_LINE('Total sal: '
    || v_total);
END;
/
""", """
<ul><li><b>DECLARE</b>: <code>CURSOR c_emp IS SELECT ...</code> names the query.</li>
<li><b>OPEN</b> runs the query and builds the <b>active set</b>; the pointer is placed before the first row.</li>
<li><b>FETCH</b> copies the current row into variables and moves the pointer to the next row.</li>
<li><b>EXIT WHEN c_emp%NOTFOUND</b> must come right after FETCH, so the last row is not processed twice.</li>
<li><b>%ROWCOUNT</b> is the number of rows fetched so far (used here as a serial number). It must be read before CLOSE.</li>
<li><b>CLOSE</b> releases the memory. Using a closed cursor raises INVALID_CURSOR.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_16", "Explicit cursor with %ROWTYPE and %ISOPEN", """
SET SERVEROUTPUT ON
DECLARE
  CURSOR c_dept IS
    SELECT * FROM dept ORDER BY deptno;
  r c_dept%ROWTYPE;
BEGIN
  IF NOT c_dept%ISOPEN THEN
    OPEN c_dept;
    DBMS_OUTPUT.PUT_LINE('Cursor opened');
  END IF;
  FETCH c_dept INTO r;
  WHILE c_dept%FOUND LOOP
    DBMS_OUTPUT.PUT_LINE(r.deptno || ' '
      || RPAD(r.dname, 11) || r.loc);
    FETCH c_dept INTO r;
  END LOOP;
  CLOSE c_dept;
END;
/
""", """
<ul><li><code>r c_dept%ROWTYPE</code> declares a record with the same fields as the cursor's SELECT list.</li>
<li><b>%ISOPEN</b> is TRUE when the cursor is open; it is used to avoid opening an already open cursor (CURSOR_ALREADY_OPEN error).</li>
<li>This version uses a <b>WHILE loop with %FOUND</b>: one FETCH before the loop, and the next FETCH at the end of each iteration.</li>
<li>RPAD pads the name to 11 characters so the columns line up.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_17", "Cursor FOR loop", """
SET SERVEROUTPUT ON
DECLARE
  CURSOR c_clerk IS
    SELECT empno, ename, sal FROM emp
    WHERE job = 'CLERK' ORDER BY empno;
BEGIN
  FOR r IN c_clerk LOOP
    UPDATE emp SET sal = sal * 1.05
    WHERE empno = r.empno;
    DBMS_OUTPUT.PUT_LINE(r.ename || ': '
      || r.sal || ' -> ' || r.sal * 1.05);
  END LOOP;

  FOR r IN (SELECT dname, loc FROM dept
            WHERE loc LIKE 'S%') LOOP
    DBMS_OUTPUT.PUT_LINE(r.dname || ' at '
      || r.loc);
  END LOOP;
END;
/
""", """
<ul><li>A <b>cursor FOR loop</b> opens the cursor, fetches every row into the record r, and closes the cursor <b>automatically</b>. No OPEN, FETCH, CLOSE or EXIT is needed.</li>
<li>The record r is declared implicitly with the cursor's columns (r.empno, r.ename, r.sal).</li>
<li>The second loop uses an <b>inline SELECT</b> in place of a named cursor.</li>
<li>Clerks get a 5% raise: 22000 → 23100 and 20000 → 21000. The record still holds the value fetched before the UPDATE.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_18", "Parameterized cursor: employees of each department", """
SET SERVEROUTPUT ON
DECLARE
  CURSOR c_dept IS
    SELECT deptno, dname FROM dept
    WHERE deptno IN (10, 20)
    ORDER BY deptno;
  CURSOR c_emp (p_dno NUMBER) IS
    SELECT ename, job FROM emp
    WHERE deptno = p_dno ORDER BY ename;
BEGIN
  FOR d IN c_dept LOOP
    DBMS_OUTPUT.PUT_LINE('== ' || d.dname);
    FOR e IN c_emp(d.deptno) LOOP
      DBMS_OUTPUT.PUT_LINE('   '
        || RPAD(e.ename, 8) || e.job);
    END LOOP;
  END LOOP;
END;
/
""", """
<ul><li>A <b>parameterized cursor</b> receives values when it is opened: <code>CURSOR c_emp (p_dno NUMBER) IS ...</code>. Parameter sizes are not given (NUMBER, not NUMBER(2)).</li>
<li>The same cursor is reused for each department: <code>c_emp(d.deptno)</code> or <code>OPEN c_emp(20);</code></li>
<li>The outer loop prints a department; the inner loop prints its employees (a master-detail report).</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ 5.4 exception handling
P.append(QE("q5_19", "Predefined exceptions: NO_DATA_FOUND, TOO_MANY_ROWS, ZERO_DIVIDE", """
SET SERVEROUTPUT ON
DECLARE
  v_sal emp.sal%TYPE;
  v_x   NUMBER;
BEGIN
  BEGIN
    SELECT sal INTO v_sal FROM emp
    WHERE empno = 500;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('1. Employee '
        || '500 not found');
  END;

  BEGIN
    SELECT sal INTO v_sal FROM emp
    WHERE deptno = 30;
  EXCEPTION
    WHEN TOO_MANY_ROWS THEN
      DBMS_OUTPUT.PUT_LINE('2. More than '
        || 'one row returned');
  END;

  BEGIN
    v_x := 100 / 0;
  EXCEPTION
    WHEN ZERO_DIVIDE THEN
      DBMS_OUTPUT.PUT_LINE('3. Cannot '
        || 'divide by zero');
  END;
  DBMS_OUTPUT.PUT_LINE('Block finished');
END;
/
""", """
<ul><li>A <b>predefined exception</b> has a name given by Oracle and is raised automatically when the error occurs.</li>
<li>Each error is placed in its own <b>nested block</b> (BEGIN ... EXCEPTION ... END). After the handler runs, control continues with the next statement of the outer block, so all three tests run.</li>
<li>NO_DATA_FOUND (ORA-01403): SELECT INTO found no row. TOO_MANY_ROWS (ORA-01422): SELECT INTO found 4 rows. ZERO_DIVIDE (ORA-01476): division by zero.</li>
<li>Without the handlers, the first error would stop the whole block.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_20", "DUP_VAL_ON_INDEX, VALUE_ERROR and OTHERS with SQLCODE, SQLERRM", """
SET SERVEROUTPUT ON
DECLARE
  v_code VARCHAR2(3);
BEGIN
  BEGIN
    INSERT INTO dept
    VALUES (20, 'HR', 'SURAT');
  EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
      DBMS_OUTPUT.PUT_LINE('Dept 20 '
        || 'already exists');
  END;

  BEGIN
    v_code := 'COMP';
  EXCEPTION
    WHEN VALUE_ERROR THEN
      DBMS_OUTPUT.PUT_LINE('Value too '
        || 'large for v_code');
  END;

  BEGIN
    INSERT INTO emp (empno, ename, deptno)
    VALUES (120, 'RAVI', 60);
  EXCEPTION
    WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('SQLCODE: '
        || SQLCODE);
      DBMS_OUTPUT.PUT_LINE('SQLERRM: '
        || SQLERRM);
  END;
END;
/
""", """
<ul><li><b>DUP_VAL_ON_INDEX</b> (ORA-00001): a duplicate value for a primary key or unique column.</li>
<li><b>VALUE_ERROR</b> (ORA-06502): a value is too large for the variable, or a conversion fails.</li>
<li><b>WHEN OTHERS</b> catches every exception not handled by an earlier WHEN. It must be the <b>last</b> handler.</li>
<li><b>SQLCODE</b> returns the error number (negative for Oracle errors) and <b>SQLERRM</b> returns the error message. Here department 60 does not exist, so the foreign key is violated (ORA-02291).</li></ul>
""", setup=SCOTT))

P.append(QE("q5_21", "User-defined exception with RAISE: bank withdrawal", """
SET SERVEROUTPUT ON
CREATE TABLE account (
  acc_no  NUMBER(4) PRIMARY KEY,
  holder  VARCHAR2(15),
  balance NUMBER(9,2)
);
INSERT INTO account
VALUES (1, 'Mehul', 5000);

DECLARE
  e_low_bal EXCEPTION;
  e_bad_amt EXCEPTION;
  v_bal account.balance%TYPE;
  v_amt NUMBER;
BEGIN
  FOR i IN 1..3 LOOP
    v_amt := CASE i WHEN 1 THEN 2000
             WHEN 2 THEN 7000 ELSE -50 END;
    BEGIN
      IF v_amt <= 0 THEN
        RAISE e_bad_amt;
      END IF;
      SELECT balance INTO v_bal
      FROM account WHERE acc_no = 1;
      IF v_amt > v_bal THEN
        RAISE e_low_bal;
      END IF;
      UPDATE account
      SET balance = balance - v_amt
      WHERE acc_no = 1;
      DBMS_OUTPUT.PUT_LINE('Withdrawn '
        || v_amt || ', balance '
        || (v_bal - v_amt));
    EXCEPTION
      WHEN e_low_bal THEN
        DBMS_OUTPUT.PUT_LINE(v_amt
          || ': insufficient balance');
      WHEN e_bad_amt THEN
        DBMS_OUTPUT.PUT_LINE(v_amt
          || ': invalid amount');
    END;
  END LOOP;
END;
/
""", """
<ul><li>A <b>user-defined exception</b> is declared like a variable: <code>e_low_bal EXCEPTION;</code></li>
<li>It is raised explicitly with <b>RAISE e_low_bal;</b> when a business rule is broken, and handled with <code>WHEN e_low_bal THEN</code>.</li>
<li>First withdrawal 2000 succeeds (balance 3000). 7000 is more than 3000, so e_low_bal is raised. -50 raises e_bad_amt.</li>
<li>An unhandled user-defined exception gives <b>ORA-06510: PL/SQL: unhandled user-defined exception</b>.</li></ul>
""", setup=""))

P.append(QE("q5_22", "PRAGMA EXCEPTION_INIT and RAISE_APPLICATION_ERROR", """
SET SERVEROUTPUT ON
DECLARE
  e_child EXCEPTION;
  PRAGMA EXCEPTION_INIT(e_child, -2292);
BEGIN
  DELETE FROM dept WHERE deptno = 10;
EXCEPTION
  WHEN e_child THEN
    DBMS_OUTPUT.PUT_LINE('Cannot delete:'
      || ' dept has employees');
END;
/

DECLARE
  v_sal emp.sal%TYPE;
BEGIN
  SELECT sal INTO v_sal
  FROM emp WHERE empno = 110;
  IF v_sal < 20000 THEN
    RAISE_APPLICATION_ERROR(-20010,
      'Salary below minimum: ' || v_sal);
  END IF;
END;
/
""", """
<ul><li><b>PRAGMA EXCEPTION_INIT</b> gives a name to an Oracle error that has no predefined name (a <b>non-predefined</b> exception). Here ORA-02292 (child record found) is named e_child and handled.</li>
<li><b>RAISE_APPLICATION_ERROR(number, message)</b> stops the block with a <b>user-defined error number</b> between -20000 and -20999 and a custom message.</li>
<li>The second block does not handle the error, so SQL*Plus shows it like an Oracle error: ORA-20010 with the message, and ORA-06512 gives the line number where it was raised.</li>
<li>RAISE_APPLICATION_ERROR is mostly used in procedures and triggers to send a meaningful error to the application.</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ 5.5 procedures and functions
P.append(QE("q5_23", "Stored procedure with IN parameters: create and execute", """
SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE raise_sal (
  p_empno IN emp.empno%TYPE,
  p_pct   IN NUMBER DEFAULT 10
) IS
  v_old emp.sal%TYPE;
BEGIN
  SELECT sal INTO v_old
  FROM emp WHERE empno = p_empno;
  UPDATE emp
  SET sal = sal + sal * p_pct / 100
  WHERE empno = p_empno;
  DBMS_OUTPUT.PUT_LINE(p_empno || ': '
    || v_old || ' -> '
    || (v_old + v_old * p_pct / 100));
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('No employee '
      || p_empno);
END raise_sal;
/

EXEC raise_sal(105)
EXEC raise_sal(108, 20)
EXEC raise_sal(p_pct => 5, p_empno => 104)

BEGIN
  raise_sal(999);
END;
/
""", """
<ul><li><b>CREATE OR REPLACE PROCEDURE</b> compiles the procedure and stores it in the database ("Procedure created."). OR REPLACE allows changing it later without dropping it.</li>
<li>Parameters have a <b>mode</b>: IN (default) passes a value into the procedure. <b>DEFAULT 10</b> is used when the second argument is omitted.</li>
<li>Execute it with <b>EXEC</b> (EXECUTE) in SQL*Plus or call it by name from another PL/SQL block.</li>
<li>Arguments can be positional <code>raise_sal(108, 20)</code> or named <code>p_pct =&gt; 5</code>.</li>
<li>For 999 the exception is handled inside the procedure.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_24", "Procedure with OUT and IN OUT parameters", """
SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE get_emp (
  p_no   IN  NUMBER,
  p_name OUT VARCHAR2,
  p_sal  OUT NUMBER
) AS
BEGIN
  SELECT ename, sal INTO p_name, p_sal
  FROM emp WHERE empno = p_no;
END;
/

CREATE OR REPLACE PROCEDURE swap (
  a IN OUT NUMBER,
  b IN OUT NUMBER
) IS
  t NUMBER;
BEGIN
  t := a;
  a := b;
  b := t;
END;
/

DECLARE
  v_name VARCHAR2(10);
  v_sal  NUMBER;
  x      NUMBER := 15;
  y      NUMBER := 40;
BEGIN
  get_emp(103, v_name, v_sal);
  DBMS_OUTPUT.PUT_LINE(v_name
    || ' earns ' || v_sal);
  swap(x, y);
  DBMS_OUTPUT.PUT_LINE('x = ' || x
    || ', y = ' || y);
END;
/
""", """
<ul><li>An <b>OUT</b> parameter returns a value from the procedure to the caller. The caller must pass a <b>variable</b>, not a constant.</li>
<li>An <b>IN OUT</b> parameter passes a value in and returns a (changed) value back. swap exchanges x and y.</li>
<li>A procedure can return several values through OUT parameters (here name and salary), which a function cannot do with RETURN.</li>
<li>IS and AS mean the same in the procedure header.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_25", "Procedure with a cursor: department report", """
SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE dept_report (
  p_dno IN dept.deptno%TYPE
) IS
  v_dname dept.dname%TYPE;
  v_total NUMBER := 0;
BEGIN
  SELECT dname INTO v_dname
  FROM dept WHERE deptno = p_dno;
  DBMS_OUTPUT.PUT_LINE('Department: '
    || v_dname);
  FOR r IN (SELECT ename, sal FROM emp
            WHERE deptno = p_dno
            ORDER BY sal DESC) LOOP
    DBMS_OUTPUT.PUT_LINE('  '
      || RPAD(r.ename, 8) || r.sal);
    v_total := v_total + r.sal;
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('  Total   '
    || v_total);
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('Invalid dept '
      || p_dno);
END;
/

EXEC dept_report(10)
EXEC dept_report(50)
""", """
<ul><li>A procedure can contain any PL/SQL: cursors, loops and exception handlers.</li>
<li>Once stored, the same code is reused for any department just by changing the argument; it is compiled only once.</li>
<li>Department 50 does not exist, so SELECT INTO raises NO_DATA_FOUND, which is handled inside the procedure.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_26", "Stored function: call from a block and from SELECT", """
SET SERVEROUTPUT ON
CREATE OR REPLACE FUNCTION annual_pay (
  p_empno IN NUMBER
) RETURN NUMBER IS
  v_sal  emp.sal%TYPE;
  v_comm emp.comm%TYPE;
BEGIN
  SELECT sal, NVL(comm, 0)
  INTO v_sal, v_comm
  FROM emp WHERE empno = p_empno;
  RETURN (v_sal + v_comm) * 12;
END annual_pay;
/

DECLARE
  v_pay NUMBER;
BEGIN
  v_pay := annual_pay(107);
  DBMS_OUTPUT.PUT_LINE('Annual pay: '
    || v_pay);
END;
/

SELECT ename, sal, comm,
       annual_pay(empno) annual
FROM   emp
WHERE  deptno = 30
ORDER  BY empno;
""", """
<ul><li>A <b>function</b> must have a <b>RETURN datatype</b> in its header and must execute a <b>RETURN value</b> statement.</li>
<li>It is called as part of an expression: <code>v_pay := annual_pay(107);</code> gives (28000 + 5000) × 12 = 396000.</li>
<li>A function (without DML statements) can be used directly in SQL, like a built-in function: in the SELECT list, WHERE or ORDER BY.</li>
<li>NVL(comm, 0) avoids a NULL result for employees without commission.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_27", "Functions: count, recursion, USER_OBJECTS and DROP", """
SET SERVEROUTPUT ON
CREATE OR REPLACE FUNCTION count_emp (
  p_dno NUMBER
) RETURN NUMBER IS
  v_cnt NUMBER;
BEGIN
  SELECT COUNT(*) INTO v_cnt
  FROM emp WHERE deptno = p_dno;
  RETURN v_cnt;
END;
/

CREATE OR REPLACE FUNCTION fact (
  n NUMBER
) RETURN NUMBER IS
BEGIN
  IF n <= 1 THEN
    RETURN 1;
  END IF;
  RETURN n * fact(n - 1);
END;
/

SELECT deptno, dname,
       count_emp(deptno) total
FROM dept ORDER BY deptno;

EXEC DBMS_OUTPUT.PUT_LINE(fact(5))

SELECT object_name, object_type, status
FROM user_objects
WHERE object_type = 'FUNCTION'
ORDER BY object_name;

DROP FUNCTION fact;
""", """
<ul><li>count_emp is used in a SELECT to show the number of employees in each department.</li>
<li>fact is <b>recursive</b>: it calls itself with n - 1 until n &lt;= 1. 5! = 120.</li>
<li>EXEC can run any single PL/SQL statement, e.g. a DBMS_OUTPUT call.</li>
<li>Stored procedures and functions are listed in <b>USER_OBJECTS</b> (and their code in USER_SOURCE). <b>DROP FUNCTION</b> / <b>DROP PROCEDURE</b> removes them.</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ 5.6 triggers
P.append(QE("q5_28", "BEFORE row trigger: validate and modify data", """
SET SERVEROUTPUT ON
CREATE OR REPLACE TRIGGER trg_stu_check
BEFORE INSERT OR UPDATE ON student
FOR EACH ROW
BEGIN
  :NEW.name := INITCAP(:NEW.name);
  :NEW.branch := UPPER(:NEW.branch);
  IF :NEW.marks NOT BETWEEN 0 AND 100
  THEN
    RAISE_APPLICATION_ERROR(-20001,
      'Marks must be 0 to 100');
  END IF;
END;
/

INSERT INTO student
VALUES (6, 'meera trivedi', 'it',
        'Anand', 88);

INSERT INTO student
VALUES (7, 'raj soni', 'ce',
        'Surat', 105);

UPDATE student SET marks = -5
WHERE rollno = 1;

SELECT * FROM student
WHERE rollno >= 6;
""", """
<ul><li>A <b>BEFORE row-level trigger</b> runs before each row is saved. It can check the data and even <b>change :NEW values</b>.</li>
<li>The name is converted to Initcap and the branch to upper case automatically, whatever the user typed.</li>
<li>Marks 105 and -5 make the trigger call RAISE_APPLICATION_ERROR, so the INSERT / UPDATE is rejected. ORA-06512 shows the trigger line and <b>ORA-04088</b> names the trigger.</li>
<li>:NEW can be changed only in a BEFORE row trigger, not in an AFTER trigger.</li></ul>
"""))

P.append(QE("q5_29", "AFTER row trigger for auditing INSERT, UPDATE, DELETE", """
SET SERVEROUTPUT ON
CREATE TABLE emp_audit (
  empno   NUMBER(4),
  action  VARCHAR2(6),
  old_sal NUMBER(7),
  new_sal NUMBER(7),
  adate   DATE
);

CREATE OR REPLACE TRIGGER trg_emp_audit
AFTER INSERT OR UPDATE OR DELETE ON emp
FOR EACH ROW
DECLARE
  v_act VARCHAR2(6);
BEGIN
  IF INSERTING THEN
    v_act := 'INSERT';
  ELSIF UPDATING THEN
    v_act := 'UPDATE';
  ELSE
    v_act := 'DELETE';
  END IF;
  INSERT INTO emp_audit
  VALUES (NVL(:NEW.empno, :OLD.empno),
          v_act, :OLD.sal, :NEW.sal,
          SYSDATE);
END;
/

INSERT INTO emp (empno, ename, sal)
VALUES (121, 'RAVI', 18000);
UPDATE emp SET sal = sal + 500
WHERE deptno = 10;
DELETE FROM emp WHERE empno = 121;

SELECT * FROM emp_audit;
""", """
<ul><li>An <b>AFTER row trigger</b> fires after each row is changed. It is commonly used for <b>auditing</b>: keeping a history of changes in another table.</li>
<li>One trigger can handle several events (INSERT OR UPDATE OR DELETE). The predicates <b>INSERTING</b>, <b>UPDATING</b> and <b>DELETING</b> tell which event fired it.</li>
<li>:OLD is NULL for INSERT and :NEW is NULL for DELETE, so NVL picks whichever empno exists.</li>
<li>The UPDATE changed 2 rows of department 10, so 2 audit rows were written.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_30", "Row-level vs statement-level trigger", """
SET SERVEROUTPUT ON
CREATE OR REPLACE TRIGGER trg_row
AFTER UPDATE ON emp
FOR EACH ROW
BEGIN
  DBMS_OUTPUT.PUT_LINE('Row trigger: '
    || :OLD.ename);
END;
/

CREATE OR REPLACE TRIGGER trg_stmt
AFTER UPDATE ON emp
BEGIN
  DBMS_OUTPUT.PUT_LINE('Statement'
    || ' trigger fired');
END;
/

UPDATE emp SET sal = sal + 100
WHERE deptno = 20;

UPDATE emp SET sal = sal + 100
WHERE deptno = 40;
""", """
<ul><li><b>trg_row</b> has FOR EACH ROW, so it fires <b>once for every row</b> changed (3 rows in department 20). It can use :OLD and :NEW.</li>
<li><b>trg_stmt</b> has no FOR EACH ROW, so it fires <b>once per statement</b>, after all rows are changed.</li>
<li>The second UPDATE changes 0 rows: the row trigger does not fire, but the statement trigger still fires once.</li>
<li>Order for one statement: BEFORE statement → (BEFORE row → change → AFTER row) for each row → AFTER statement.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_31", "BEFORE DELETE / UPDATE OF trigger: block invalid changes", """
SET SERVEROUTPUT ON
CREATE OR REPLACE TRIGGER trg_no_del
BEFORE DELETE ON emp
FOR EACH ROW
WHEN (OLD.job = 'PRESIDENT')
BEGIN
  RAISE_APPLICATION_ERROR(-20005,
    'President cannot be deleted');
END;
/

CREATE OR REPLACE TRIGGER trg_sal_cut
BEFORE UPDATE OF sal ON emp
FOR EACH ROW
BEGIN
  IF :NEW.sal < :OLD.sal THEN
    RAISE_APPLICATION_ERROR(-20006,
      'Salary of ' || :OLD.ename
      || ' cannot be reduced');
  END IF;
END;
/

DELETE FROM emp WHERE empno = 101;
DELETE FROM emp WHERE empno = 110;
UPDATE emp SET sal = sal - 1000
WHERE empno = 104;
UPDATE emp SET job = 'SR ANALYST'
WHERE empno = 104;
""", """
<ul><li>The <b>WHEN</b> clause adds a condition: trg_no_del fires only for the president's row. In WHEN, NEW and OLD are written <b>without the colon</b>.</li>
<li>Deleting employee 110 is allowed, but deleting 101 (PRESIDENT) is rejected.</li>
<li><b>UPDATE OF sal</b> makes trg_sal_cut fire only when the SAL column is updated. A salary cut is rejected, but changing JOB does not fire the trigger.</li>
<li>Triggers like these enforce business rules that cannot be written as constraints.</li></ul>
""", setup=SCOTT))

P.append(QE("q5_32", "Managing triggers: USER_TRIGGERS, DISABLE, ENABLE, DROP", """
SET SERVEROUTPUT ON
CREATE OR REPLACE TRIGGER trg_dept_loc
BEFORE INSERT OR UPDATE ON dept
FOR EACH ROW
BEGIN
  :NEW.loc := UPPER(:NEW.loc);
END;
/

SELECT trigger_name, trigger_type,
       triggering_event, status
FROM user_triggers;

ALTER TRIGGER trg_dept_loc DISABLE;
INSERT INTO dept
VALUES (50, 'HR', 'Bharuch');

ALTER TRIGGER trg_dept_loc ENABLE;
INSERT INTO dept
VALUES (60, 'IT', 'Navsari');

SELECT * FROM dept
WHERE deptno >= 50 ORDER BY deptno;

DROP TRIGGER trg_dept_loc;
""", """
<ul><li><b>USER_TRIGGERS</b> lists the triggers of the current user with their type, event and status.</li>
<li><b>ALTER TRIGGER name DISABLE</b> switches a trigger off without deleting it (useful while bulk-loading data). Row 50 is saved as 'Bharuch' because the trigger was disabled.</li>
<li><b>ENABLE</b> switches it on again, so 'Navsari' becomes 'NAVSARI'.</li>
<li><code>ALTER TABLE dept DISABLE ALL TRIGGERS;</code> disables all triggers of a table. <b>DROP TRIGGER</b> deletes the trigger; dropping a table also drops its triggers.</li></ul>
""", setup=SCOTT))

PROGRAMS = P
